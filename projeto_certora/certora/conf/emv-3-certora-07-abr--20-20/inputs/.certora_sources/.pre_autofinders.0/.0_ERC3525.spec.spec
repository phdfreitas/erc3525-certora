// Regra para testar a configuração do certora. 
rule totalSupplyNonNegative() {
    env e;
    assert totalSupply(e) >= 0;
}

/** Um token só pode ser transferido por seu proprietário (teste válido) */
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

rule unauthorazedTransfer(address from, address to, uint256 tokenId) {
    env e;

    // Garante que o remetente não é o dono e não tem aprovação
    require ownerOf(e, tokenId) != e.msg.sender;
    require getApproved(e, tokenId) != e.msg.sender;
    require !isApprovedForAll(e, ownerOf(e, tokenId), e.msg.sender);

    transferFrom(e, from, to, tokenId);

    assert reverted();
}


// escrevendo essa função pois outras estavam dando erro de sintaxe
rule slotDeveSerConsistente(uint256 tokenId) {
    env e;

    uint256 slotAntes = slotOf(e, tokenId);
    
    uint256 slotDepois = slotOf(e, tokenId);
    assert slotAntes == slotDepois;
}

// teste valido
rule transferValueToNewToken(uint256 fromTokenId, address recipient, uint256 value) {
    env e;

    // Pré-condições usando require
    require ownerOf(e, fromTokenId) == e.msg.sender;
    require balanceOf(e, fromTokenId) >= value;

    // Valores antes da transferência
    uint256 balBefore = balanceOf(e, fromTokenId);
    uint256 slotBefore = slotOf(e, fromTokenId);
    uint256 supplyBefore = totalSupply(e);

    // Ação
    uint256 newId = transferFrom(e, fromTokenId, recipient, value);

    // Pós-condições
    assert balanceOf(e, fromTokenId) == balBefore - value;
    assert ownerOf(e, newId) == recipient;
    assert balanceOf(e, newId) == value;
    assert slotOf(e, newId) == slotBefore;
    assert totalSupply(e) == supplyBefore + 1;
}



