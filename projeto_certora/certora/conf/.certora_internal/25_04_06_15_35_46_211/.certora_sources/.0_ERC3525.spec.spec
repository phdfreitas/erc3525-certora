// Regra para testar a configuração do certora. 
rule totalSupplyNonNegative() {
    env e;
    assert totalSupply(e) >= 0;
}

/** Um token só pode ser transferido por seu proprietário ou alguém autorizado */
rule onlyAuthorizedCanTransfer(address from, address to, uint256 tokenId) {
    env e;
    // Captura o dono original do token antes da transferência
    address ownerBefore = ownerOf(e, tokenId);
    transferFrom(e, from, to, tokenId);  // tenta transferir o tokenId de `from` para `to`
    
    if (ownerOf(e, tokenId) == to) {  
        // Se a transferência não revertou e o proprietário mudou para `to`, então:
        assert ownerBefore == from, 
            "O parâmetro `from` deve ser o dono atual do token em caso de sucesso";
        assert (e.msg.sender == ownerBefore) 
            || (isApprovedForAll(e, ownerBefore, e.msg.sender)) 
            || (getApproved(e, tokenId) == e.msg.sender),
            "Transferência bem-sucedida somente se caller for dono ou aprovado";
    }

    satisfy
}

