using ERC3525 as token;

rule totalSupplyAlwaysPositive() {
    assert token.totalSupply() >= 0;
}
