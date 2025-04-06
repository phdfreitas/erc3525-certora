rule totalSupplyAlwaysPositive() {
    assert ERC3525.totalSupply() >= 0;
}