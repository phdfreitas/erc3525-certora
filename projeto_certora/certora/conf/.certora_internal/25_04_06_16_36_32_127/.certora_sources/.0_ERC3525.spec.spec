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

    // Pré-condição: o caller deve ser o owner
    assume ownerOf(e, fromTokenId) == e.msg.sender;

    // Pré-condição: saldo suficiente
    uint256 before = balanceOf(e, fromTokenId);
    assume !(before < value);

    // Executa a transferência
    transferFrom(e, fromTokenId, recipient, value);

    // Garante que o novo saldo somado ao valor transferido dá o saldo anterior
    uint256 afterBalance = balanceOf(e, fromTokenId);
    assert add(afterBalance, value) == before;
}

