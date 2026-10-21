# diagnose eval pi05 attn k09 long seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_attn_k09_long_seed42_strict_20260527T064758_result.json`
- **Structured JSON:** [`1ea2628b5a3451f2c551.json`](../../sessions/1e/1ea2628b5a3451f2c551.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

| 项目 | 结果 |
|---|---|
| **失败根因** | **误报**。实验已于 14:35:21 正常完成，SR=64.0%。cron 监控在 `~/runs/.../logs/` 查找日志，但实际日志在 `/root/autodl-tmp/.../logs/`，路径不匹配导致判定为失败。 |
| **GPU2 状态** | 空闲（1 MiB / 97887 MiB, 0% 利用率），可用于新实验 |
| **是否需修改** | 不需要。实验代码和命令正常，结果已保存到 `eval_results/pi05_attention_k0.90_libero_10_seed42.json` |
| **重跑建议** | **无需重跑**。已更正 registry：conclusion → success，metrics → SR=64.0% |

**附带发现**：`~/runs/importance_margin_vla_compress/` 下的 strict 实验日志（如 `eval_pi05_random_k085_long_seed42_strict.log`）是从另一个路径复制或由不同 cwd 生成的。cron 监控的 log_path 配置需要统一指向 `/root/autodl-tmp/importance_margin_vla_compress/logs/`，否则后续 strict 实验可能继续被误报。

---
