# diagnose eval openvla attn k09 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_attn_k09_long_seed42_v3_20260525T140644_result.json`
- **Structured JSON:** [`12993f9eab34445f6d45.json`](../../sessions/12/12993f9eab34445f6d45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

**不需要重新提交。** 实验 `eval_openvla_attn_k09_long_seed42_v3` 实际已成功完成。

| 项目 | 详情 |
|------|------|
| 失败根因 | 监控误报 — 检查了不存在的日志路径 `~/runs/...`，实际日志在 `/root/autodl-tmp/logs/` |
| 实验状态 | ✅ 完成，attention_prune k=0.9 on libero_10 |
| **Overall SR** | **0.4400 (220/500)** |
| 耗时 | 544.2 min |
| 结果文件 | 已从日志重建并保存为 `openvla_attn_prune_k09_10_seed42.json` |

**需要修的 bug**：`eval_openvla_l2norm_libero.py` 第 393 行 `else` 分支把 `attention_prune` 和 `l2norm_prune` 的输出写到同一文件名，导致后跑的实验覆盖前面的结果。应加一个 `elif args.mode == "attention_prune"` 分支用 `openvla_attn_prune_*` 命名。

GPU 0-3 全部空闲，可用于其他任务。

---
