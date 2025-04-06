using asset as asset;

rule totalSupplyAlwaysPositive() {
    assert asset.totalSupply() >= 0;
}