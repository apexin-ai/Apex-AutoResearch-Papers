# ops d158 b1 completion check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d158_b1_completion_check_20260524T100817_result.json`
- **Structured JSON:** [`d24558288967d1e24c87.json`](../../sessions/d2/d24558288967d1e24c87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**d158_14b_sft_s44: 成功完成**

| 项目 | 值 |
|------|-----|
| train_loss | 0.6083 |
| eval_loss | 0.6541 |
| eval_mean_token_accuracy | 0.8446 |
| runtime | ~71 min (4255s), 3 epochs |
| adapter 路径 | `/root/autodl-tmp/sft_output_14b_s44` |
| 文件 | adapter_config.json + adapter_model.safetensors (980MB) 完整 |

**GPU 状态：**
- cuda:0: 7.2GB 占用（其他进程）
- cuda:1/2/3: 空闲 (0 MiB)

cuda:2 已释放，可用于下一步 B2 (14B candidate generation)。Cron 已删除，registry 已标记 DONE/success。

---
