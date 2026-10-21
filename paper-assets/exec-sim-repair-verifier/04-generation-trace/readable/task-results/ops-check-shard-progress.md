# ops check shard progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-shard-progress_20260516T043142_result.json`
- **Structured JSON:** [`5cda58168ffe7c821c2a.json`](../../sessions/5c/5cda58168ffe7c821c2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM 8B ckpt-400 Test Eval 进度汇报

### 各 Shard 状态

| Shard | PID | GPU | 存活 | 范围 | 已完成 / 总数 | 进度 | 速度 | ETA (UTC) |
|-------|-----|-----|------|------|--------------|------|------|-----------|
| **v3** | 443221 | cuda:3 | ✅ 运行 3h45m | 0-9784 (全量, resumed@5287) | 7224 / 9784 | **73.8%** | ~8.4/min | ~17:35 |
| **shard2** | 448100 | cuda:1 | ✅ 运行 3h06m | 7680-9784 | 1608 / 2104 | **76.4%** | ~8.7/min | ~13:30 |
| **shard3** | 453335 | cuda:0 | ✅ 运行 1h54m | 6200-7680 | 968 / 1480 | **65.4%** | ~8.5/min | ~13:32 |
| **shard4** | — | — | ❌ 已完成 | 9100-9784 | 688 / 688 | **100%** | — | — |

### Shard4 已完成 — 结果摘要

- 输出: `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard4/`
- **accuracy: 65.55%**, majority baseline: 75.73%, gap: -10.17pp
- f1_macro: 52.66, f1_pass: 77.36, f1_fail: 27.96
- **unparseable: 504/688 (73.3%)**
- truncated: 49/688 (7.1%), truncated 样本 accuracy 85.71%
- 进程已退出，无 PID 可注册 cron

### Running Accuracy

- v3 当前: **64.5%** (new=1937 + resumed=5287)
- shard4 最终: **65.55%**

### 关键时间线

- **~13:30 UTC（约1小时后）**: shard2 + shard3 完成 → 加上 shard4 和 v3 已有数据，6200-9784 全部覆盖
- **~17:35 UTC（约5小时后）**: v3 跑完全量 0-9784（v3 单独就能覆盖所有样本）
- 如果只需要合并去重，shard2+3 完成后（~1h）可以用 v3 的 0-7224 + shard3 的 6200-7680 + shard2 的 7680-9784 拼出完整 0-9784，无需等 v3 跑完

### 注意事项

- shard4 的 unparseable rate 73.3% 很高，需要关注其他 shard 完成后的整体 unparseable rate
- 3 个 GPU（cuda:0/1/3）满载 ~21GB 显存，cuda:2 空闲（shard4 已完成释放）

---
