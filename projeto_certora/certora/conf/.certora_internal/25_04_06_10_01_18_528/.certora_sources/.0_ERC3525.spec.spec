using ERC3525 as asset

rule totalSupplyAlwaysPositive() {
    assert ERC3525.totalSupply() >= 0;
}