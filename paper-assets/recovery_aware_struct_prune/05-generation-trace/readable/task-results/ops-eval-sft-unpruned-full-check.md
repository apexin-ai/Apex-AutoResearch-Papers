# ops eval sft unpruned full check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-sft-unpruned-full-check_20260516T024504_result.json`
- **Structured JSON:** [`f6087a504831ea79f844.json`](../../sessions/f6/f6087a504831ea79f844.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**eval_sft_unpruned_full 结果：**
- **Accuracy: 81.27% ± 1.07% (1072/1319)**
- EOS rate: 99.70% (仅 4 条 truncated)
- 平均 response 长度: 207.18 tokens
- 结果文件: `/root/recovery_aware_struct_prune/results/eval_sft_unpruned_baseline_full.json`

**三方对比（GSM8K full N=1319）：**
| 模型 | Accuracy |
|------|----------|
| Unpruned SFT | **81.27%** |
| RASP 20% pruned + SFT | 61.49% |
| Standard 20% pruned + SFT | 59.29% |

Registry 已更新为 DONE/success，cron 已清除。

---
