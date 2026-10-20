# code scierc 4b merge inference v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scierc_4b_merge_inference_v2_20260515T194913_result.json`
- **Structured JSON:** [`08b631d5666ef235eb4f.json`](../../sessions/08/08b631d5666ef235eb4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**GPU 诊断结果**
| GPU | 状态 | 进程 |
|-----|------|------|
| cuda:0 | 空闲 | v4 finetune 已完成 |
| cuda:1 | 运行中 | CoNLL inference (exp_qwen3_4b_conll_scs_inference_v2) |
| cuda:2 | 运行中 | **SciERC SCS inference** (刚启动) |
| cuda:3 | 空闲 | — |

**已执行操作**
1. **Kill PID 231733** — cuda:2 上重复的 CoNLL inference 已清除
2. **v4 finetune 确认完成** — 585/585 步，best checkpoint = checkpoint-400 (eval_loss=0.0898)
3. **Merge 完成** — `checkpoints/qwen3-4b-scierc-merged/` (5 shards, ~7.5GB)
4. **SCS inference 已启动** — PID 234209 在 cuda:2，4408 prompts (551 samples × 8)，处理中 (~12 it/s)，预计 ~6 分钟完成
5. **Registry** — `exp_qwen3_4b_scierc_scs_inference` 状态 RUNNING

日志位置：`/tmp/exp_qwen3_4b_scierc_scs_inference.log`

---
