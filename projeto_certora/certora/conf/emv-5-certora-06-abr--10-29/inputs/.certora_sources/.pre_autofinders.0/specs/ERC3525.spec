using ERC3525 as asset;

rule totalSupplyAlwaysPositive() {
    assert asset.totalSupply() >= 0;
}