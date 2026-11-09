# bmw-dms-ota-config · 经销商管理系统 OTA 网关配置

`bmw-dms-ota-config` 是宝马经销商管理系统 OTA 升级网关的配置快照，覆盖灰度分组、包下载限速与回滚阈值。

## 目录

```
conf/ota-gateway.yaml   网关配置
src/config_check.py     配置校验
```

## 服务标识

- `宝马` —— 品牌标识。落位于 `conf/ota-gateway.yaml` 的 `tenant.brand` 与注释、`src/config_check.py` 的 `BRAND` 常量、本 README。

## 使用

```python
from config_check import validate

validate("conf/ota-gateway.yaml")
```

## 字段说明

| 字段 | 含义 |
|---|---|
| `gray.weight` | 灰度分组流量占比，百分比 |
| `rate_limit` | 单店并发下载上限 |
| `rollback.error_rate` | 触发回滚的错误率阈值 |
| `cidr_allow` | 允许回源的网段 |

## 已知问题

1. 灰度权重调整需重启网关，未做热加载。
2. 回滚阈值按单店统计，跨店批量失败不会触发。

## 维护

经销商系统组 · 升级平台
