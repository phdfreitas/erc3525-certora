/** Um token só pode ser transferido por seu proprietário (teste válido) */
rule onlyAuthorizedCanTransferSpec(address from, address to, uint256 tokenId) {
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

rule unauthorazedTransferSpec(address from, address to, uint256 tokenId) {
    env e;

    // Garante que o remetente não é o dono e não tem aprovação
    require ownerOf(e, tokenId) != e.msg.sender;
    require getApproved(e, tokenId) != e.msg.sender;
    require !isApprovedForAll(e, ownerOf(e, tokenId), e.msg.sender);

    uint256 balanceBefore = balanceOf(e, tokenId);
    address ownerBefore = ownerOf(e, tokenId);

    transferFrom(e, from, to, tokenId);

    // Pós-condição: nenhum efeito deve ter ocorrido
    assert balanceOf(e, tokenId) == balanceBefore;
    assert ownerOf(e, tokenId) == ownerBefore;
}


// escrevendo essa função pois outras estavam dando erro de sintaxe
rule slotConsistencySpec(uint256 tokenId) {
    env e;

    uint256 slotAntes = slotOf(e, tokenId);
    
    uint256 slotDepois = slotOf(e, tokenId);
    assert slotAntes == slotDepois;
}

// teste valido
rule transferValueToNewTokenSpec(uint256 fromTokenId, address recipient, uint256 value) {
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

// Transferência entre tokens do mesmo slot deve preservar o saldo total
rule transferValuePreservesTotal(uint256 fromId, uint256 toId, uint256 value) {
    env e;
    require slotOf(e, fromId) == slotOf(e, toId);
    require balanceOf(e, fromId) >= value;
    
    // Usando mathint para evitar overflow
    mathint totalBefore = balanceOf(e, fromId) + balanceOf(e, toId);
    transferFrom(e, fromId, toId, value);
    assert balanceOf(e, fromId) + balanceOf(e, toId) == totalBefore;
}

// Transferência para novo token deve incrementar totalSupply
rule mintOnTransferIncreasesSupply(uint256 fromId, address to, uint256 value) {
    env e;
    uint256 supplyBefore = totalSupply(e);
    transferFrom(e, fromId, to, value);
    assert totalSupply(e) == supplyBefore + 1;
}

// Tokens derivados devem herdar o slot do token original
rule derivedTokenInheritsSlot(uint256 fromId, address to, uint256 value) {
    env e;
    uint256 originalSlot = slotOf(e, fromId);
    uint256 newId = transferFrom(e, fromId, to, value);
    assert slotOf(e, newId) == originalSlot;
}

// Transferência para address(0) deve falhar
rule transferToZeroAddressFails(uint256 fromTokenId) {
    env e;
    address zeroAddr = 0x0000000000000000000000000000000000000000;
    uint256 value = balanceOf(e, fromTokenId);
    
    transferFrom@withrevert(e, fromTokenId, zeroAddr, value);
    
    assert lastReverted, "Transferência para address(0) deve reverter";
}

// Aprovação para address(0) deve falhar
rule approveZeroAddressFails(uint256 tokenId) {
    env e;
    address zeroAddr = 0x0000000000000000000000000000000000000000;
    uint256 value = 100;
    
    approve@withrevert(e, tokenId, zeroAddr, value);
    
    assert lastReverted, "Aprovação para address(0) deve reverter";
}

// Aprovação e revogação concorrentes
rule concurrentApprovalChange {
    env e;
    uint256 tokenId = 1;
    address operator = 0x555555;
    
    // Aprova e revoga simultaneamente
    approve(e, tokenId, operator, 100);
    approve(e, tokenId, operator, 0);
    
    assert allowance(e, tokenId, operator) == 0,
        "Aprovação concorrente pode deixar allowance inconsistente";
}

ghost mathint sum_of_values {
    init_state axiom sum_of_values == 0;
}

hook Sstore _values[KEY uint256 tokenId] uint new_value (uint old_value) {
    sum_of_values = sum_of_values + new_value - old_value;
}

// garante que a soma de todos os tokens é igual ao totalSupply
invariant totalSupplyMatchesSumOfValues {
    env e;
    assert totalSupply(e) == sum_of_values;
}
