# analysis eval math500 sft rasp alpha4p0 20 fixed

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550_result.json`
- **Structured JSON:** [`6a10afaa9c81d92f8e2c.json`](../../sessions/6a/6a10afaa9c81d92f8e2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总：

| 指标 | 值 |
|------|-----|
| **Accuracy** | **27.80%** (139/500, ±2.00%) |
| **avg_response_length** | 947.996 tokens |
| **natural_eos** | 310 (62%) |
| **truncated** | 190 (38%) |
| **W&B run** | 无（eval 脚本未接入 W&B） |
| **checkpoint_path** | `/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20` |
| **log_path** | `~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log` |
| **异常/警告** | 仅 HF Hub offline mode 使用本地缓存，无实质错误 |
| **耗时** | 5h53m（~6 GPU-hours） |
| **EXIT_CODE** | 0 |

值得注意：38% 的回答被 truncated（达到 2048 token 上限），avg_response_length 仅 948 tokens，说明模型生成长度分布不均——部分问题生成很短就结束，部分则打满 2048。

---
