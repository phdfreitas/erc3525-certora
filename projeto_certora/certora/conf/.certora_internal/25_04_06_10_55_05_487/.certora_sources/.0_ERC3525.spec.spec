methods {
    function totalSupply() external returns uint256 envfree;
}

rule totalSupplyAlwaysPositive() {
    assert ERC3525.totalSupply() >= 0;
}