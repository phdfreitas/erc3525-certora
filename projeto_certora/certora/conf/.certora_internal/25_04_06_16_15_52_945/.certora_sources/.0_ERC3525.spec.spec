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



rule transferValueToNewToken(uint256 fromTokenId, address recipient, uint256 value) {
    env e;

    let owner = ownerOf(e, fromTokenId);
    let balBefore = balanceOf(e, fromTokenId);
    assume owner == e.msg.sender;
    assume balBefore >= value;

    let totalCountBefore = totalSupply();
    let newId = transferFrom(e, fromTokenId, recipient, value);

    let balAfter = balanceOf(e, fromTokenId);
    let expected = balBefore - value;

    let valid = balAfter - expected;
    assert valid == 0;
}


