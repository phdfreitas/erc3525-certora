rule totalSupplyAlwaysPositive() {
    assert totalSupply() >= 0;
}