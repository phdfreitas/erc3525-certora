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

// escrevendo essa função pois outras estavam dando erro de sintaxe
rule slotDeveSerConsistente(uint256 tokenId) {
    env e;

    uint256 slotAntes = slotOf(e, tokenId);
    
    uint256 slotDepois = slotOf(e, tokenId);
    assert slotAntes == slotDepois;
}

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

/** @notice Transferência parcial entre tokens existentes somente com slots iguais e conserva valor */
rule transferValueBetweenTokens(uint256 fromTokenId, uint256 toTokenId, uint256 value) {
    env e;

    // Pré-condições com require:
    if (!(fromTokenId != toTokenId &&
          ownerOf(e, fromTokenId) == e.msg.sender &&
          balanceOf(e, fromTokenId) >= value)) {
        skip;
    }

    // Valores antes da transferência
    uint256 slotFrom = slotOf(e, fromTokenId);
    uint256 slotTo   = slotOf(e, toTokenId);
    uint256 balFromBefore = balanceOf(e, fromTokenId);
    uint256 balToBefore   = balanceOf(e, toTokenId);

    transferFrom(e, fromTokenId, toTokenId, value);

    if (!reverted()) {
        // Verificações pós-condição
        assert slotFrom == slotTo,
            "Tokens com slots diferentes não deveriam permitir transferência de valor";

        assert balanceOf(e, fromTokenId) == balFromBefore - value &&
               balanceOf(e, toTokenId) == balToBefore + value,
            "Valor deve ser conservado: deduzido de fromToken e somado em toToken";
    }
}


