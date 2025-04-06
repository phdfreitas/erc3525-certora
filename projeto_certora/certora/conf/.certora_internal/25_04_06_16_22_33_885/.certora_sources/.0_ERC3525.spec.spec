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

/** @notice Transferência parcial deve preservar valor e slot ao criar novo token */
rule transferValueToNewToken(uint256 fromTokenId, address recipient, uint256 value) {
    env e;

    address owner = ownerOf(e, fromTokenId);
    uint256 balBefore = balanceOf(e, fromTokenId);

    // Em vez de "owner == e.msg.sender"
    assume owner == e.msg.sender;

    // Em vez de "balBefore >= value"
    assume balBefore >= value;

    uint256 totalCountBefore = totalSupply();
    uint256 newId = transferFrom(e, fromTokenId, recipient, value);

    // Pós-condições esperadas
    assert !(balanceOf(e, fromTokenId) != balBefore - value);  // saldo do token de origem
    assert !(ownerOf(e, newId) != recipient);                  // novo token é do destinatário
    assert !(balanceOf(e, newId) != value);                    // novo token tem o valor esperado
    assert !(slotOf(e, newId) != slotOf(e, fromTokenId));      // mesmo slot
    assert !(totalSupply() != totalCountBefore + 1);           // totalSupply aumentou
}



