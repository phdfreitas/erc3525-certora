rule totalSupplyNonNegative() {
    env e;
    assert totalSupply() >= 0;
}
