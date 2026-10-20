# eval home v5 checkpoint sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-v5-checkpoint-sweep_20260514T030314_result.json`
- **Structured JSON:** [`7d817c1f76e4e1c92cb5.json`](../../sessions/7d/7d817c1f76e4e1c92cb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 tmux session 都在运行。

## 汇总

### seed123 sweep（进行中）
| checkpoint | accuracy | 状态 |
|-----------|----------|------|
| ckpt-400 | **75.05%** | ✓ 完成 |
| ckpt-600 | **80.73%** | ✓ 完成 |
| ckpt-800 | ~73.8% running | 进行中（~60%，预计 20:15 完成）|
| ckpt-1000 | - | 排队（预计 20:42 完成）|

### CLS v5 (seed42) 发现
- **实际可用 checkpoint**: 600, 4000, 4200, 4400, 4600
- **预期的 ckpt-400/800/1000 不存在** — v5 训练到了更长步数
- ckpt-600 之前有 76.92% 的结果但无结果文件，本次 sweep 会重新评估

### v5 sweep 已启动
tmux session `eval_v5_sweep` 正在等待 GPU 空闲（seed123 完成后自动开始），将按顺序评估 ckpt-600 → 4000 → 4200 → 4400 → 4600，每个约 27 分钟，总计约 2.5 小时。

---
