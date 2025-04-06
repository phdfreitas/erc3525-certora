using ERC3525 as id;

rule totalSupplyAlwaysPositive() {
    assert ERC3525.totalSupply() >= 0;
}