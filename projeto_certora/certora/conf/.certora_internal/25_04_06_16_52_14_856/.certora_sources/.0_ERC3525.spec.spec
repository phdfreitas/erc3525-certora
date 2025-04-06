// Regra para testar a configuração do certora. 
rule totalSupplyNonNegative() {
    env e;
    assert totalSupply(e) >= 0;
}

/** Um token só pode ser transferido por seu proprietário */
rule onlyAuthorizedCanTransfer(address from, address to, uint256 tokenId) {
    env e;
    address ownerBefore = ownerOf(e, tokenId);
    transferFrom(e, from, to, tokenId);
    address ownerAfter = ownerOf(e, tokenId);

    bool changedOwner = ownerAfter == to;

    bool ownerTransfering =
        ownerBefore == from &&
        (
            e.msg.sender == ownerBefore ||
            isApprovedForAll(e, ownerBefore, e.msg.sender) ||
            getApproved(e, tokenId) == e.msg.sender
        );

    // Se a transferência foi bem-sucedida (mudou de dono), então ela deve ser autorizada
    assert !changedOwner || ownerTransfering;
}

rule transferDecreasesBalance(uint256 fromTokenId, address recipient, uint256 value) {
    env e;

    address owner = ownerOf(e, fromTokenId);
    assume owner == e.msg.sender;

    uint256 before = balanceOf(e, fromTokenId);
    assume before >= value;

    transferFrom(e, fromTokenId, recipient, value);

    uint256 afterBalance = balanceOf(e, fromTokenId);
    assert add(afterBalance, value) == before;
}


