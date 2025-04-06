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
    address owner = ownerOf(e, fromTokenId);
    assume owner == e.msg.sender;

    // Pré-condição: saldo suficiente
    uint256 before = balanceOf(e, fromTokenId);
    assume before >= value;

    // Executa a transferência
    transferFrom(e, fromTokenId, recipient, value);

    // Pós-condição: saldo novo + valor == saldo anterior
    uint256 afterBalance = balanceOf(e, fromTokenId);
    assert afterBalance + value == before;
}


