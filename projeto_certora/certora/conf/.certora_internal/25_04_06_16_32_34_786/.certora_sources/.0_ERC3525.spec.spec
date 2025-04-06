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

/*
/** @notice Transferência parcial deve preservar valor e slot ao criar novo token */
rule transferValueToNewToken(uint256 fromTokenId, address recipient, uint256 value) {
    env e;
    // Pré-condições: assume que `fromTokenId` existe e `msg.sender` é autorizado 
    address owner = ownerOf(e, fromTokenId);
    uint256 balBefore = balanceOf(e, fromTokenId);
    assume owner == e.msg.sender;               // caller é dono (ou poderíamos assumir allowance suficiente)
    assume balBefore >= value;                 // há saldo suficiente para transferir
    
    uint256 totalCountBefore = totalSupply();
    uint256 newId = transferFrom(e, fromTokenId, recipient, value);
    
    // Pós-condições esperadas
    assert balanceOf(fromTokenId) == balBefore - value;           // Saldo do token de origem deve diminuir pelo valor transferido
    assert ownerOf(newId) == recipient;                           // Novo token criado deve pertencer ao destinatário
    assert balanceOf(newId) == value;                             // Novo token deve conter exatamente o valor transferido
    assert slotOf(newId) == slotOf(fromTokenId);                  // Slot deve ser o mesmo
    assert totalSupply() == totalCountBefore + 1;                 // Total supply deve aumentar em 1
}*/
