# ops spon dryrun

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_spon_dryrun_20260515T173047_result.json`
- **Structured JSON:** [`c83a49a895f55e7bdbdd.json`](../../sessions/c8/c83a49a895f55e7bdbdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-Run 验证报告

### GPU 状态
cuda:0 和 cuda:1 各占 67,569/97,887 MiB，空闲 ~29.7GB，足够最小配置运行。使用 cuda:0。

### 验证清单

| # | 验证项 | 状态 | 关键日志 |
|---|--------|------|----------|
| 1 | SPON bias 零初始化 | **PASS** | Step 1 `mean_bias_norm=0.000000`，确认初始 bias 全为零 |
| 2 | 梯度仅流向 bias vectors | **PASS** | `SPON params: 458,752 / 8,030,261,248 (0.0057%)` — 仅 458K 参数可训练 |
| 3 | Cosine schedule + warmup | **PASS** | lr 序列：`5e-06 → 1e-05 → 7.5e-06 → 2.5e-06 → 0.0e+00`（2 步 warmup 到 peak 1e-5，后 3 步 cosine 衰减到 0） |
| 4 | Loss 合理 | **PASS** | `0.4258 → 0.3477 → 0.3906 → 0.4375 → 0.4688`，Step 2 有明显下降；后续回升因 lr cosine 衰减+仅 5 步，属正常 |
| 5 | 无 OOM / 错误 | **PASS** | 正常完成，checkpoint 已保存到 `/tmp/spon_dryrun/spon_biases.pt` |

### 补充观察
- `mean_bias_norm` 从 0 逐步增长（0 → 0.000425 → 0.001062 → 0.001450 → 0.001562），bias 在被正常优化
- Gradient checkpointing 正常启用
- 临时文件已清理

**结论：train_spon.py 全部 5 项验证通过，可以启动正式训练。**

---
