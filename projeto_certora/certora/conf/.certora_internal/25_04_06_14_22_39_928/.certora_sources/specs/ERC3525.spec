rule totalSupplyNonNegative() {
    env e;
    assert totalSupply(e) >= 0;
}
