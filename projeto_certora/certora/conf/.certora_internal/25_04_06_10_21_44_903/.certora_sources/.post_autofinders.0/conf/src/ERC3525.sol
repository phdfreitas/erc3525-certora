// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "../libs/openzeppelin-contracts/contracts/utils/Context.sol";
import "../libs/openzeppelin-contracts/contracts/utils/introspection/IERC165.sol";
import "../libs/openzeppelin-contracts/contracts/utils/Strings.sol";
import "./IERC721.sol";
import "./IERC3525.sol";
import "./IERC721Receiver.sol";
import "./IERC3525Receiver.sol";
import "./extensions/IERC721Enumerable.sol";
import "./extensions/IERC721Metadata.sol";
import "./extensions/IERC3525Metadata.sol";
import "./periphery/interface/IERC3525MetadataDescriptor.sol";

contract ERC3525 is Context, IERC3525Metadata, IERC721Enumerable {
    using Strings for address;
    using Strings for uint256;

    event SetMetadataDescriptor(address indexed metadataDescriptor);

    struct TokenData {
        uint256 id;
        uint256 slot;
        uint256 balance;
        address owner;
        address approved;
        address[] valueApprovals;
    }

    struct AddressData {
        uint256[] ownedTokens;
        mapping(uint256 => uint256) ownedTokensIndex;
        mapping(address => bool) approvals;
    }

    string private _name;
    string private _symbol;
    uint8 private _decimals;
    uint256 private _tokenIdGenerator;

    // id => (approval => allowance)
    // @dev _approvedValues cannot be defined within TokenData, cause struct containing mappings cannot be constructed.
    mapping(uint256 => mapping(address => uint256)) private _approvedValues;

    TokenData[] private _allTokens;

    // key: id
    mapping(uint256 => uint256) private _allTokensIndex;

    mapping(address => AddressData) private _addressData;

    IERC3525MetadataDescriptor public metadataDescriptor;

    ERC3525 public immutable asset;

    constructor(ERC3525 _asset, string memory name_, string memory symbol_, uint8 decimals_) {
        _tokenIdGenerator = 1;
        _name = name_;
        _symbol = symbol_;
        _decimals = decimals_;
        asset = _asset;
    }

    function supportsInterface(bytes4 interfaceId) public view virtual override returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a60000, 1037618708646) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a60001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a60005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a66000, interfaceId) }
        return
            interfaceId == type(IERC165).interfaceId ||
            interfaceId == type(IERC3525).interfaceId ||
            interfaceId == type(IERC721).interfaceId ||
            interfaceId == type(IERC3525Metadata).interfaceId ||
            interfaceId == type(IERC721Enumerable).interfaceId || 
            interfaceId == type(IERC721Metadata).interfaceId;
    }

    /**
     * @dev Returns the token collection name.
     */
    function name() public view virtual override returns (string memory) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b80000, 1037618708664) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b80001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b80004, 0) }
        return _name;
    }

    /**
     * @dev Returns the token collection symbol.
     */
    function symbol() public view virtual override returns (string memory) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ab0000, 1037618708651) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ab0001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ab0004, 0) }
        return _symbol;
    }

    /**
     * @dev Returns the number of decimals the token uses for value.
     */
    function valueDecimals() public view virtual override returns (uint8) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b50000, 1037618708661) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b50001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b50004, 0) }
        return _decimals;
    }

    function balanceOf(uint256 tokenId_) public view virtual override returns (uint256) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b20000, 1037618708658) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b20001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b20005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b26000, tokenId_) }
        _requireMinted(tokenId_);
        return _allTokens[_allTokensIndex[tokenId_]].balance;
    }

    function ownerOf(uint256 tokenId_) public view virtual override returns (address owner_) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a50000, 1037618708645) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a50001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a50005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a56000, tokenId_) }
        _requireMinted(tokenId_);
        owner_ = _allTokens[_allTokensIndex[tokenId_]].owner;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000071,owner_)}
        require(owner_ != address(0), "ERC3525: invalid token ID");
    }

    function slotOf(uint256 tokenId_) public view virtual override returns (uint256) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ba0000, 1037618708666) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ba0001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ba0005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ba6000, tokenId_) }
        _requireMinted(tokenId_);
        return _allTokens[_allTokensIndex[tokenId_]].slot;
    }

    function _baseURI() internal view virtual returns (string memory) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00820000, 1037618708610) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00820001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00820004, 0) }
        return "";
    }

    function contractURI() public view virtual override returns (string memory) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00aa0000, 1037618708650) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00aa0001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00aa0004, 0) }
        string memory baseURI = _baseURI();assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0001004f,0)}
        return 
            address(metadataDescriptor) != address(0) ? 
                metadataDescriptor.constructContractURI() :
                bytes(baseURI).length > 0 ? 
                    string(abi.encodePacked(baseURI, "contract/", Strings.toHexString(address(this)))) : 
                    "";
    }

    function slotURI(uint256 slot_) public view virtual override returns (string memory) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00950000, 1037618708629) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00950001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00950005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00956000, slot_) }
        string memory baseURI = _baseURI();assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00010050,0)}
        return 
            address(metadataDescriptor) != address(0) ? 
                metadataDescriptor.constructSlotURI(slot_) : 
                bytes(baseURI).length > 0 ? 
                    string(abi.encodePacked(baseURI, "slot/", slot_.toString())) : 
                    "";
    }

    /**
     * @dev Returns the Uniform Resource Identifier (URI) for `tokenId` token.
     */
    function tokenURI(uint256 tokenId_) public view virtual override returns (string memory) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b00000, 1037618708656) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b00001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b00005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b06000, tokenId_) }
        _requireMinted(tokenId_);
        string memory baseURI = _baseURI();assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00010051,0)}
        return 
            address(metadataDescriptor) != address(0) ? 
                metadataDescriptor.constructTokenURI(tokenId_) : 
                bytes(baseURI).length > 0 ? 
                    string(abi.encodePacked(baseURI, tokenId_.toString())) : 
                    "";
    }

    function approve(uint256 tokenId_, address to_, uint256 value_) public payable virtual override {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00970000, 1037618708631) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00970001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00970005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00976002, value_) }
        address owner = ERC3525.ownerOf(tokenId_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000052,owner)}
        require(to_ != owner, "ERC3525: approval to current owner");

        require(_isApprovedOrOwner(_msgSender(), tokenId_), "ERC3525: approve caller is not owner nor approved");

        _approveValue(tokenId_, to_, value_);
    }

    function allowance(uint256 tokenId_, address operator_) public view virtual override returns (uint256) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a90000, 1037618708649) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a90001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a90005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a96001, operator_) }
        _requireMinted(tokenId_);
        return _approvedValues[tokenId_][operator_];
    }

    function transferFrom(
        uint256 fromTokenId_,
        address to_,
        uint256 value_
    ) public payable virtual override returns (uint256 newTokenId) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b60000, 1037618708662) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b60001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b60005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b66002, value_) }
        _spendAllowance(_msgSender(), fromTokenId_, value_);

        newTokenId = _createDerivedTokenId(fromTokenId_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000072,newTokenId)}
        _mint(to_, newTokenId, ERC3525.slotOf(fromTokenId_), 0);
        _transferValue(fromTokenId_, newTokenId, value_);
    }

    function transferFrom(
        uint256 fromTokenId_,
        uint256 toTokenId_,
        uint256 value_
    ) public payable virtual override {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b70000, 1037618708663) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b70001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b70005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b76002, value_) }
        _spendAllowance(_msgSender(), fromTokenId_, value_);
        _transferValue(fromTokenId_, toTokenId_, value_);
    }

    function balanceOf(address owner_) public view virtual override returns (uint256 balance) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a70000, 1037618708647) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a70001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a70005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a76000, owner_) }
        require(owner_ != address(0), "ERC3525: balance query for the zero address");
        return _addressData[owner_].ownedTokens.length;
    }

    function transferFrom(
        address from_,
        address to_,
        uint256 tokenId_
    ) public payable virtual override {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ae0000, 1037618708654) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ae0001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ae0005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ae6002, tokenId_) }
        require(_isApprovedOrOwner(_msgSender(), tokenId_), "ERC3525: transfer caller is not owner nor approved");
        _transferTokenId(from_, to_, tokenId_);
    }

    function safeTransferFrom(
        address from_,
        address to_,
        uint256 tokenId_,
        bytes memory data_
    ) public payable virtual override {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00af0000, 1037618708655) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00af0001, 4) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00af0005, 585) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00af6003, data_) }
        require(_isApprovedOrOwner(_msgSender(), tokenId_), "ERC3525: transfer caller is not owner nor approved");
        _safeTransferTokenId(from_, to_, tokenId_, data_);
    }

    function safeTransferFrom(
        address from_,
        address to_,
        uint256 tokenId_
    ) public payable virtual override {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00960000, 1037618708630) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00960001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00960005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00966002, tokenId_) }
        safeTransferFrom(from_, to_, tokenId_, "");
    }

    function approve(address to_, uint256 tokenId_) public payable virtual override {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a80000, 1037618708648) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a80001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a80005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a86001, tokenId_) }
        address owner = ERC3525.ownerOf(tokenId_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000053,owner)}
        require(to_ != owner, "ERC3525: approval to current owner");

        require(
            _msgSender() == owner || ERC3525.isApprovedForAll(owner, _msgSender()),
            "ERC3525: approve caller is not owner nor approved for all"
        );

        _approve(to_, tokenId_);
    }

    function getApproved(uint256 tokenId_) public view virtual override returns (address) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b90000, 1037618708665) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b90001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b90005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b96000, tokenId_) }
        _requireMinted(tokenId_);
        return _allTokens[_allTokensIndex[tokenId_]].approved;
    }

    function setApprovalForAll(address operator_, bool approved_) public virtual override {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b30000, 1037618708659) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b30001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b30005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b36001, approved_) }
        _setApprovalForAll(_msgSender(), operator_, approved_);
    }

    function isApprovedForAll(address owner_, address operator_) public view virtual override returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ac0000, 1037618708652) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ac0001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ac0005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ac6001, operator_) }
        return _addressData[owner_].approvals[operator_];
    }

    function totalSupply() public view virtual override returns (uint256) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b10000, 1037618708657) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b10001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b10004, 0) }
        return _allTokens.length;
    }

    function tokenByIndex(uint256 index_) public view virtual override returns (uint256) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b40000, 1037618708660) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b40001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b40005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00b46000, index_) }
        require(index_ < ERC3525.totalSupply(), "ERC3525: global index out of bounds");
        return _allTokens[index_].id;
    }

    function tokenOfOwnerByIndex(address owner_, uint256 index_) public view virtual override returns (uint256) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ad0000, 1037618708653) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ad0001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ad0005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00ad6001, index_) }
        require(index_ < ERC3525.balanceOf(owner_), "ERC3525: owner index out of bounds");
        return _addressData[owner_].ownedTokens[index_];
    }

    function _setApprovalForAll(
        address owner_,
        address operator_,
        bool approved_
    ) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00830000, 1037618708611) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00830001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00830005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00836002, approved_) }
        require(owner_ != operator_, "ERC3525: approve to caller");

        _addressData[owner_].approvals[operator_] = approved_;

        emit ApprovalForAll(owner_, operator_, approved_);
    }

    function _isApprovedOrOwner(address operator_, uint256 tokenId_) internal view virtual returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00850000, 1037618708613) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00850001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00850005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00856001, tokenId_) }
        address owner = ERC3525.ownerOf(tokenId_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000054,owner)}
        return (
            operator_ == owner ||
            ERC3525.isApprovedForAll(owner, operator_) ||
            ERC3525.getApproved(tokenId_) == operator_
        );
    }

    function _spendAllowance(address operator_, uint256 tokenId_, uint256 value_) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00860000, 1037618708614) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00860001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00860005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00866002, value_) }
        uint256 currentAllowance = ERC3525.allowance(tokenId_, operator_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000055,currentAllowance)}
        if (!_isApprovedOrOwner(operator_, tokenId_) && currentAllowance != type(uint256).max) {
            require(currentAllowance >= value_, "ERC3525: insufficient allowance");
            _approveValue(tokenId_, operator_, currentAllowance - value_);
        }
    }

    function _exists(uint256 tokenId_) internal view virtual returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00840000, 1037618708612) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00840001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00840005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00846000, tokenId_) }
        return _allTokens.length != 0 && _allTokens[_allTokensIndex[tokenId_]].id == tokenId_;
    }

    function _requireMinted(uint256 tokenId_) internal view virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00870000, 1037618708615) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00870001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00870005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00876000, tokenId_) }
        require(_exists(tokenId_), "ERC3525: invalid token ID");
    }

    function _mint(address to_, uint256 slot_, uint256 value_) internal virtual returns (uint256 tokenId) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00880000, 1037618708616) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00880001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00880005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00886002, value_) }
        tokenId = _createOriginalTokenId();assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000073,tokenId)}
        _mint(to_, tokenId, slot_, value_);  
    }

    function _mint(address to_, uint256 tokenId_, uint256 slot_, uint256 value_) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00890000, 1037618708617) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00890001, 4) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00890005, 585) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00896003, value_) }
        require(to_ != address(0), "ERC3525: mint to the zero address");
        require(tokenId_ != 0, "ERC3525: cannot mint zero tokenId");
        require(!_exists(tokenId_), "ERC3525: token already minted");

        _beforeValueTransfer(address(0), to_, 0, tokenId_, slot_, value_);
        __mintToken(to_, tokenId_, slot_);
        __mintValue(tokenId_, value_);
        _afterValueTransfer(address(0), to_, 0, tokenId_, slot_, value_);
    }

    function _mintValue(uint256 tokenId_, uint256 value_) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008a0000, 1037618708618) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008a0001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008a0005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008a6001, value_) }
        address owner = ERC3525.ownerOf(tokenId_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000056,owner)}
        uint256 slot = ERC3525.slotOf(tokenId_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000057,slot)}
        _beforeValueTransfer(address(0), owner, 0, tokenId_, slot, value_);
        __mintValue(tokenId_, value_);
        _afterValueTransfer(address(0), owner, 0, tokenId_, slot, value_);
    }

    function __mintValue(uint256 tokenId_, uint256 value_) private {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008b0000, 1037618708619) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008b0001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008b0005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008b6001, value_) }
        _allTokens[_allTokensIndex[tokenId_]].balance += value_;
        emit TransferValue(0, tokenId_, value_);
    }

    function __mintToken(address to_, uint256 tokenId_, uint256 slot_) private {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008c0000, 1037618708620) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008c0001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008c0005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008c6002, slot_) }
        TokenData memory tokenData = TokenData({
            id: tokenId_,
            slot: slot_,
            balance: 0,
            owner: to_,
            approved: address(0),
            valueApprovals: new address[](0)
        });assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00010058,0)}

        _addTokenToAllTokensEnumeration(tokenData);
        _addTokenToOwnerEnumeration(to_, tokenId_);

        emit Transfer(address(0), to_, tokenId_);
        emit SlotChanged(tokenId_, 0, slot_);
    }

    function _burn(uint256 tokenId_) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008d0000, 1037618708621) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008d0001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008d0005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008d6000, tokenId_) }
        _requireMinted(tokenId_);

        TokenData storage tokenData = _allTokens[_allTokensIndex[tokenId_]];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00010059,0)}
        address owner = tokenData.owner;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0000005a,owner)}
        uint256 slot = tokenData.slot;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0000005b,slot)}
        uint256 value = tokenData.balance;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0000005c,value)}

        _beforeValueTransfer(owner, address(0), tokenId_, 0, slot, value);

        _clearApprovedValues(tokenId_);
        _removeTokenFromOwnerEnumeration(owner, tokenId_);
        _removeTokenFromAllTokensEnumeration(tokenId_);

        emit TransferValue(tokenId_, 0, value);
        emit SlotChanged(tokenId_, slot, 0);
        emit Transfer(owner, address(0), tokenId_);

        _afterValueTransfer(owner, address(0), tokenId_, 0, slot, value);
    }

    function _burnValue(uint256 tokenId_, uint256 burnValue_) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008e0000, 1037618708622) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008e0001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008e0005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008e6001, burnValue_) }
        _requireMinted(tokenId_);

        TokenData storage tokenData = _allTokens[_allTokensIndex[tokenId_]];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0001005d,0)}
        address owner = tokenData.owner;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0000005e,owner)}
        uint256 slot = tokenData.slot;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0000005f,slot)}
        uint256 value = tokenData.balance;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000060,value)}

        require(value >= burnValue_, "ERC3525: burn value exceeds balance");

        _beforeValueTransfer(owner, address(0), tokenId_, 0, slot, burnValue_);
        
        tokenData.balance -= burnValue_;uint256 certora_local116 = tokenData.balance;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000074,certora_local116)}
        emit TransferValue(tokenId_, 0, burnValue_);
        
        _afterValueTransfer(owner, address(0), tokenId_, 0, slot, burnValue_);
    }

    function _addTokenToOwnerEnumeration(address to_, uint256 tokenId_) private {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008f0000, 1037618708623) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008f0001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008f0005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff008f6001, tokenId_) }
        _allTokens[_allTokensIndex[tokenId_]].owner = to_;

        _addressData[to_].ownedTokensIndex[tokenId_] = _addressData[to_].ownedTokens.length;
        _addressData[to_].ownedTokens.push(tokenId_);
    }

    function _removeTokenFromOwnerEnumeration(address from_, uint256 tokenId_) private {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00900000, 1037618708624) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00900001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00900005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00906001, tokenId_) }
        _allTokens[_allTokensIndex[tokenId_]].owner = address(0);

        AddressData storage ownerData = _addressData[from_];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00010061,0)}
        uint256 lastTokenIndex = ownerData.ownedTokens.length - 1;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000062,lastTokenIndex)}
        uint256 lastTokenId = ownerData.ownedTokens[lastTokenIndex];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000063,lastTokenId)}
        uint256 tokenIndex = ownerData.ownedTokensIndex[tokenId_];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000064,tokenIndex)}

        ownerData.ownedTokens[tokenIndex] = lastTokenId;uint256 certora_local117 = ownerData.ownedTokens[tokenIndex];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000075,certora_local117)}
        ownerData.ownedTokensIndex[lastTokenId] = tokenIndex;uint256 certora_local118 = ownerData.ownedTokensIndex[lastTokenId];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000076,certora_local118)}

        delete ownerData.ownedTokensIndex[tokenId_];
        ownerData.ownedTokens.pop();
    }

    function _addTokenToAllTokensEnumeration(TokenData memory tokenData_) private {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00910000, 1037618708625) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00910001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00910005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00916000, tokenData_) }
        _allTokensIndex[tokenData_.id] = _allTokens.length;
        _allTokens.push(tokenData_);
    }

    function _removeTokenFromAllTokensEnumeration(uint256 tokenId_) private {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009d0000, 1037618708637) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009d0001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009d0005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009d6000, tokenId_) }
        // To prevent a gap in the tokens array, we store the last token in the index of the token to delete, and
        // then delete the last slot (swap and pop).

        uint256 lastTokenIndex = _allTokens.length - 1;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000065,lastTokenIndex)}
        uint256 tokenIndex = _allTokensIndex[tokenId_];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000066,tokenIndex)}

        // When the token to delete is the last token, the swap operation is unnecessary. However, since this occurs so
        // rarely (when the last minted token is burnt) that we still do the swap here to avoid the gas cost of adding
        // an 'if' statement (like in _removeTokenFromOwnerEnumeration)
        TokenData memory lastTokenData = _allTokens[lastTokenIndex];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00010067,0)}

        _allTokens[tokenIndex] = lastTokenData; // Move the last token to the slot of the to-delete token
        _allTokensIndex[lastTokenData.id] = tokenIndex; // Update the moved token's index

        // This also deletes the contents at the last position of the array
        delete _allTokensIndex[tokenId_];
        _allTokens.pop();
    }

    function _approve(address to_, uint256 tokenId_) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009c0000, 1037618708636) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009c0001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009c0005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009c6001, tokenId_) }
        _allTokens[_allTokensIndex[tokenId_]].approved = to_;
        emit Approval(ERC3525.ownerOf(tokenId_), to_, tokenId_);
    }

    function _approveValue(
        uint256 tokenId_,
        address to_,
        uint256 value_
    ) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009b0000, 1037618708635) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009b0001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009b0005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009b6002, value_) }
        require(to_ != address(0), "ERC3525: approve value to the zero address");
        if (!_existApproveValue(to_, tokenId_)) {
            _allTokens[_allTokensIndex[tokenId_]].valueApprovals.push(to_);
        }
        _approvedValues[tokenId_][to_] = value_;

        emit ApprovalValue(tokenId_, to_, value_);
    }

    function _clearApprovedValues(uint256 tokenId_) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009e0000, 1037618708638) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009e0001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009e0005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009e6000, tokenId_) }
        TokenData storage tokenData = _allTokens[_allTokensIndex[tokenId_]];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00010068,0)}
        uint256 length = tokenData.valueApprovals.length;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000069,length)}
        for (uint256 i = 0; i < length; i++) {
            address approval = tokenData.valueApprovals[i];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000079,approval)}
            delete _approvedValues[tokenId_][approval];
        }
        delete tokenData.valueApprovals;
    }

    function _existApproveValue(address to_, uint256 tokenId_) internal view virtual returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009f0000, 1037618708639) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009f0001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009f0005, 9) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009f6001, tokenId_) }
        uint256 length = _allTokens[_allTokensIndex[tokenId_]].valueApprovals.length;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0000006a,length)}
        for (uint256 i = 0; i < length; i++) {
            if (_allTokens[_allTokensIndex[tokenId_]].valueApprovals[i] == to_) {
                return true;
            }
        }
        return false;
    }

    function _transferValue(
        uint256 fromTokenId_,
        uint256 toTokenId_,
        uint256 value_
    ) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a00000, 1037618708640) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a00001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a00005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a06002, value_) }
        require(_exists(fromTokenId_), "ERC3525: transfer from invalid token ID");
        require(_exists(toTokenId_), "ERC3525: transfer to invalid token ID");

        TokenData storage fromTokenData = _allTokens[_allTokensIndex[fromTokenId_]];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0001006b,0)}
        TokenData storage toTokenData = _allTokens[_allTokensIndex[toTokenId_]];assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0001006c,0)}

        require(fromTokenData.balance >= value_, "ERC3525: insufficient balance for transfer");
        require(fromTokenData.slot == toTokenData.slot, "ERC3525: transfer to token with different slot");

        _beforeValueTransfer(
            fromTokenData.owner,
            toTokenData.owner,
            fromTokenId_,
            toTokenId_,
            fromTokenData.slot,
            value_
        );

        fromTokenData.balance -= value_;uint256 certora_local119 = fromTokenData.balance;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000077,certora_local119)}
        toTokenData.balance += value_;uint256 certora_local120 = toTokenData.balance;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000078,certora_local120)}

        emit TransferValue(fromTokenId_, toTokenId_, value_);

        _afterValueTransfer(
            fromTokenData.owner,
            toTokenData.owner,
            fromTokenId_,
            toTokenId_,
            fromTokenData.slot,
            value_
        );

        require(
            _checkOnERC3525Received(fromTokenId_, toTokenId_, value_, ""),
            "ERC3525: transfer rejected by ERC3525Receiver"
        );
    }

    function _transferTokenId(
        address from_,
        address to_,
        uint256 tokenId_
    ) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a10000, 1037618708641) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a10001, 3) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a10005, 73) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a16002, tokenId_) }
        require(ERC3525.ownerOf(tokenId_) == from_, "ERC3525: transfer from invalid owner");
        require(to_ != address(0), "ERC3525: transfer to the zero address");

        uint256 slot = ERC3525.slotOf(tokenId_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0000006d,slot)}
        uint256 value = ERC3525.balanceOf(tokenId_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0000006e,value)}

        _beforeValueTransfer(from_, to_, tokenId_, tokenId_, slot, value);

        _approve(address(0), tokenId_);
        _clearApprovedValues(tokenId_);

        _removeTokenFromOwnerEnumeration(from_, tokenId_);
        _addTokenToOwnerEnumeration(to_, tokenId_);

        emit Transfer(from_, to_, tokenId_);

        _afterValueTransfer(from_, to_, tokenId_, tokenId_, slot, value);
    }

    function _safeTransferTokenId(
        address from_,
        address to_,
        uint256 tokenId_,
        bytes memory data_
    ) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a20000, 1037618708642) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a20001, 4) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a20005, 585) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a26003, data_) }
        _transferTokenId(from_, to_, tokenId_);
        require(
            _checkOnERC721Received(from_, to_, tokenId_, data_),
            "ERC3525: transfer to non ERC721Receiver"
        );
    }

    function _checkOnERC3525Received( 
        uint256 fromTokenId_, 
        uint256 toTokenId_, 
        uint256 value_, 
        bytes memory data_
    ) internal virtual returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a30000, 1037618708643) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a30001, 4) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a30005, 585) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a36003, data_) }
        address to = ERC3525.ownerOf(toTokenId_);assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff0000006f,to)}
        if (_isContract(to)) {
            try IERC165(to).supportsInterface(type(IERC3525Receiver).interfaceId) returns (bool retval) {
                if (retval) {
                    bytes4 receivedVal = IERC3525Receiver(to).onERC3525Received(_msgSender(), fromTokenId_, toTokenId_, value_, data_);
                    return receivedVal == IERC3525Receiver.onERC3525Received.selector;
                } else {
                    return true;
                }
            } catch (bytes memory /** reason */) {
                return true;
            }
        } else {
            return true;
        }
    }

    /**
     * @dev Internal function to invoke {IERC721Receiver-onERC721Received} on a target address.
     * The call is not executed if the target address is not a contract.
     *
     * @param from_ address representing the previous owner of the given token ID
     * @param to_ target address that will receive the tokens
     * @param tokenId_ uint256 ID of the token to be transferred
     * @param data_ bytes optional data to send along with the call
     * @return bool whether the call correctly returned the expected magic value
     */
    function _checkOnERC721Received(
        address from_,
        address to_,
        uint256 tokenId_,
        bytes memory data_
    ) private returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a40000, 1037618708644) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a40001, 4) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a40005, 585) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00a46003, data_) }
        if (_isContract(to_)) {
            try 
                IERC721Receiver(to_).onERC721Received(_msgSender(), from_, tokenId_, data_) returns (bytes4 retval) {
                return retval == IERC721Receiver.onERC721Received.selector;
            } catch (bytes memory reason) {
                if (reason.length == 0) {
                    revert("ERC721: transfer to non ERC721Receiver implementer");
                } else {
                    /// @solidity memory-safe-assembly
                    assembly {
                        revert(add(32, reason), mload(reason))
                    }
                }
            }
        } else {
            return true;
        }
    }

    /* solhint-disable */
    function _beforeValueTransfer(
        address from_,
        address to_,
        uint256 fromTokenId_,
        uint256 toTokenId_,
        uint256 slot_,
        uint256 value_
    ) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00980000, 1037618708632) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00980001, 6) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00980005, 37449) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00986005, value_) }}

    function _afterValueTransfer(
        address from_,
        address to_,
        uint256 fromTokenId_,
        uint256 toTokenId_,
        uint256 slot_,
        uint256 value_
    ) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00990000, 1037618708633) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00990001, 6) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00990005, 37449) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00996005, value_) }}
    /* solhint-enable */

    function _setMetadataDescriptor(address metadataDescriptor_) internal virtual {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009a0000, 1037618708634) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009a0001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009a0005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff009a6000, metadataDescriptor_) }
        metadataDescriptor = IERC3525MetadataDescriptor(metadataDescriptor_);
        emit SetMetadataDescriptor(metadataDescriptor_);
    }

    function _createOriginalTokenId() internal virtual returns (uint256) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00920000, 1037618708626) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00920001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00920004, 0) }
        return _tokenIdGenerator++;
    }

    function _createDerivedTokenId(uint256 fromTokenId_) internal virtual returns (uint256) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00930000, 1037618708627) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00930001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00930005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00936000, fromTokenId_) }
        fromTokenId_;
        return _createOriginalTokenId();
    }

    function _isContract(address addr_) private view returns (bool) {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00940000, 1037618708628) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00940001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00940005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00946000, addr_) }
        uint32 size;assembly ("memory-safe"){mstore(0xffffff6e4604afefe123321beef1b02fffffffffffffffffffffffff00000070,size)}
        assembly {
            size := extcodesize(addr_)
        }
        return (size > 0);
    }
}

