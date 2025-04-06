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

    // Pré-condições
    address owner = ownerOf(e, fromTokenId);
    uint256 balBefore = balanceOf(e, fromTokenId);
    uint256 slot = slotOf(e, fromTokenId);
    uint256 supplyBefore = totalSupply();

    assume e.msg.sender == owner;
    assume balBefore >= value;

    uint256 newId = transferFrom(e, fromTokenId, recipient, value);

    // Pós-condições esperadas
    assert balanceOf(e, fromTokenId) == balBefore - value;
    assert ownerOf(e, newId) == recipient;
    assert balanceOf(e, newId) == value;
    assert slotOf(e, newId) == slot;
    assert totalSupply() == supplyBefore + 1;
}




