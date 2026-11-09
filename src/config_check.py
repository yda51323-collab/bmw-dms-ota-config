# -*- coding: utf-8 -*-
"""OTA 网关配置校验。"""
import ipaddress

BRAND = "宝马"
REQUIRED = ("tenant.brand", "gateway.host", "upstream.cidr_allow", "rollback.error_rate")


def _flat(d, prefix=""):
    out = {}
    for k, v in d.items():
        key = prefix + k
        if isinstance(v, dict):
            out.update(_flat(v, key + "."))
        else:
            out[key] = v
    return out


def validate(path):
    import yaml
    with open(path, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    flat = _flat(cfg)
    miss = [k for k in REQUIRED if k not in flat]
    bad_cidr = []
    for c in flat.get("upstream.cidr_allow", []):
        try:
            ipaddress.ip_network(c)
        except ValueError:
            bad_cidr.append(c)
    if flat.get("tenant.brand") != BRAND:
        miss.append("tenant.brand.mismatch")
    return {"missing": miss, "bad_cidr": bad_cidr, "brand": BRAND}
