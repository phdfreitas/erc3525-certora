/** @notice totalSupply deve ser sempre ≥ 0 (não negativo) */
rule totalSupplyNonNegative() {
    env e;
    assert totalSupply() >= 0, 
        "totalSupply deve ser não-negativo";
}
