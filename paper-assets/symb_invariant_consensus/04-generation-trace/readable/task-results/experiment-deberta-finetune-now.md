# experiment deberta finetune now

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_deberta-finetune-now_20260522T155530_result.json`
- **Structured JSON:** [`44885dec33c74582a126.json`](../../sessions/44/44885dec33c74582a126.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。

## 汇报

| 项目 | 详情 |
|------|------|
| **PID** | 640384 |
| **GPU** | cuda:0, NVIDIA RTX PRO 6000 Blackwell (94GB), 已用 8159 MiB |
| **训练数据** | tasksource/proofwriter 全量 585,552 条 (True: 158,805 / False: 158,805 / Unknown: 267,942) |
| **总 steps** | 182,985 (5 epochs × 585,552 / batch_size 16) |
| **当前速度** | ~3.9 it/s |
| **预计总耗时** | ~13 小时 |
| **checkpoint 路径** | `/root/symb_invariant_consensus/checkpoints/deberta-large-pw-finetuned/` |
| **日志** | `/tmp/deberta_finetune.log` |

**修复记录**：
1. `scripts/finetune_deberta_pw.py` line 76: `row["context"]` → `row["theory"]`（HF 数据集列名不同）
2. 添加 `LD_LIBRARY_PATH` 指向 `/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib`（修复 `libnvrtc-builtins.so.13.0` 找不到的问题）
3. CLASSES tiebreaking bug 已在之前修复过（line 30 已经是 `sorted()`）

**注意**：训练用了全部 585K 数据（包含所有 depth），因为该 HF 数据集的 config 列不含 "OWA" 标签。如果只需 OWA 子集，需要调整过滤逻辑。

---
