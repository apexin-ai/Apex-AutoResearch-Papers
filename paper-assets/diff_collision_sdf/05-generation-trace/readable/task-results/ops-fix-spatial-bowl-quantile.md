# ops fix spatial bowl quantile

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_spatial_bowl_quantile_20260525T095942_result.json`
- **Structured JSON:** [`21d7d64aea594675d4a1.json`](../../sessions/21/21d7d64aea594675d4a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，通过了 quantile norm 检查。q01/q99 值已正确加载，数据加载完成，进入训练阶段。

**修复总结**：`spatial_bowl` 的 `norm_stats.json` 缺少 q01/q99 分位数统计（全为 null），而 PI05 模型强制 `use_quantile_norm=True`。从 5068 帧 parquet 数据计算了 1st/99th 百分位数并写入 `/root/colliforce-vla/assets/baseline_spatial_bowl/safelibero_spatial/norm_stats.json`。

同时建议后续修复 `compute_norm_stats_custom.py` 脚本，让它也计算 q01/q99，避免新场景再次遇到同样问题。

---
