# diagnose harvest 8b eval and rsft s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_harvest_8b_eval_and_rsft_s44_20260518T234226_result.json`
- **Structured JSON:** [`abc3cb0d4fc658c52c33.json`](../../sessions/ab/abc3cb0d4fc658c52c33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

### 实验 1：plan019_8b_sft_s44_eval — 完成

| 指标 | 值 |
|------|-----|
| ign_f1 | **0.4681** |
| f1 | 0.4841 |
| evi_f1_joint (DREEAM) | 0.3839 |
| evi_f1 (TP) | 0.8361 |
| edcr | 0.6697 |
| format | 985/985 (100%) |
| truncated | 306/985 |

vs s42 canonical ign_f1=0.5051，s44 低了 **3.7pp**。8B SFT seed 方差较大。

### 实验 2：plan019_8b_rsft_s44 — 训练完成

| 指标 | 值 |
|------|-----|
| train_loss | 0.4725 |
| total_steps | 1134 (3 epochs) |
| mean_token_accuracy | 0.8734 |
| checkpoint | `/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44/` |

等待 eval 才能得到 ign_f1。

### GPU 状态

| GPU | 状态 |
|-----|------|
| cuda:0 | 占用 10.4GB (d111_4b_sft_s42_reeval, PID 579965) |
| cuda:1 | **空闲** |
| cuda:2 | **空闲** |
| cuda:3 | 占用 20.4GB (d112_rsft_s44_generate, PID 584466) |

cuda:1 和 cuda:2 确认空闲，可用于下一步任务（如 8B RSFT s44 eval）。

---
