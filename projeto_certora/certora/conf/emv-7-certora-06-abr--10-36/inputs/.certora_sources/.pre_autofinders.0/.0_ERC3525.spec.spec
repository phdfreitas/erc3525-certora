rule totalSupplyAlwaysPositive() {
    assert asset.totalSupply() >= 0;
}