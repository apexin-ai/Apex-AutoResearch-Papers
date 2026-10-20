# analysis d158 14b rsft s44 train diag

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d158_14b_rsft_s44_train_diag_20260525T090017_result.json`
- **Structured JSON:** [`d0596dd0f686f212bcee.json`](../../sessions/d0/d0596dd0f686f212bcee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**训练诊断**：d158_14b_rsft_s44_train 训练成功
- 567/567 步，3 epochs，train_loss=0.5063，accuracy=0.8678，耗时 67 分钟
- Checkpoint: `/root/autodl-tmp/rsft_output_14b_s44/`（adapter_model.safetensors 980MB）
- Registry 已更新为 DONE/success

**Eval 已提交**：
| 实验 | GPU | PID | 说明 |
|------|-----|-----|------|
| d158_14b_rsft_s44_eval | cuda:0 | 366546 | dev set (985 docs) |
| d158_14b_rsft_s44_test_with_evi | cuda:1 | 366690 | test_revised (500 docs) |

---
