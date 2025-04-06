module ERC3525 {
    rule totalSupplyAlwaysPositive() {
        assert totalSupply() >= 0;
    }
}
