# submit rsft ced s43 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_rsft_ced_s43_r2_20260516T000955_result.json`
- **Structured JSON:** [`fd747baf4498cd04ff98.json`](../../sessions/fd/fd747baf4498cd04ff98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Flag 检查

| Flag | rsft_trainer.py 默认值 | s42 实际 | s44 实际 | s43 r2 实际 |
|------|----------------------|---------|---------|------------|
| `--bf16` | `default=True` | ✓ (默认开启) | ✓ (默认开启) | ✓ (默认开启) |
| `--weighted_sampling` | `store_true` (默认 False) | `weighted=True` ✓ | `weighted=True` ✓ | `weighted=True` ✓ |

三个 seed 一致：都用了 `--weighted_sampling`，`--bf16` 默认开启无需显式传。

### rsft_ced_s43_train_r2 已在运行

- **已在 cuda:1 上训练**（PID 275269, 28216MiB）
- 启动时间：2026-05-16 08:10:30
- 进度：step 7/510（刚启动不久）
- 日志确认 `weighted=True`，无报错

**无需重复提交**，训练已在进行中。

---
