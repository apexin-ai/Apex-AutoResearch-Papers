# diagnose urgent full status and cascade

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-full-status-and-cascade_20260522T181214_result.json`
- **Structured JSON:** [`91492944ce3b250e7150.json`](../../sessions/91/91492944ce3b250e7150.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registry entries updated to RUNNING. Here's the full status summary:

## 完成的实验（已更新 registry）

| 实验 | GPU | ign_f1 | Evidence Tax | 关键发现 |
|------|-----|--------|-------------|---------|
| **14B RSFT no-evi** | cuda:0 | 0.3926 | **+0.77pp** | no-evi 反而更好！with-evi=0.3849 |
| **8B RSFT no-evi** | cuda:3 | 0.3319 | **-0.34pp** | evidence 微弱帮助, with-evi=0.3353 |
| **14B SFT s43** | cuda:1 | train_loss=0.6052, eval_loss=0.6552 | — | s42对比: train=0.5457, eval=0.6292, s43略高 |

## 仍在运行

| 实验 | GPU | 进度 | ETA |
|------|-----|------|-----|
| **1.7B RSFT no-evi** | cuda:2 (6GB) | 146/500 (29%) | ~5h |

## 级联提交（3 个新任务已启动）

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| **test_eval_4b_rsft_s42_no_evi** | cuda:0 (9.5GB) | 194600 | RUNNING |
| **plan017_14b_rsft_s43_generate** | cuda:1 (28.7GB) | 194682 | RUNNING |
| **test_eval_llama_rsft_s42_no_evi** | cuda:3 (36.7GB) | 194438 | RUNNING |

**14B evidence tax 结果出乎意料**：no-evidence 模式在 test set 上 ign_f1=0.3926 比 with-evidence 的 0.3849 高 0.77pp。这与 dev set 上 evidence 帮助 -4.54pp 的方向相反，说明 14B RSFT 的 evidence benefit 在 dev/test 之间不一致（类似 8B SFT 曾出现的 dev-test 方向反转）。

---
