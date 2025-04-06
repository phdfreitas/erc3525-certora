// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC3525.sol";

contract MyContract {
    ERC3525 public asset;

    constructor(ERC3525 _asset) {
        asset = _asset;
    }
}
