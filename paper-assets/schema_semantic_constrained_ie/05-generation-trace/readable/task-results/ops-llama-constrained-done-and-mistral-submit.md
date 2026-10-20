# ops llama constrained done and mistral submit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_constrained_done_and_mistral_submit_20260516T045111_result.json`
- **Structured JSON:** [`d5ae648d78d990eeb72b.json`](../../sessions/d5/d5ae648d78d990eeb72b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## Llama FT Constrained Eval Metrics

| 指标 | Constrained | Unconstrained | Delta |
|---|---|---|---|
| E-F1 | **85.23%** | 85.17% | +0.06pp |
| R-F1 (all_set) | **44.23%** | 44.15% | +0.08pp |
| ET violations | 0 (0%) | 0 (0%) | — |
| RV violations | 0 (0%) | 24 (0.1%) | **-0.1pp** |
| DR violations | 33 (0.2%) | 80 (0.5%) | **-0.3pp** |
| Parse fail | 25 (2.51%) | 23 (2.30%) | +0.21pp |

**结论**：constrained 解码在 fine-tuned Llama DocRED 上将 DR 从 0.5%→0.2%（降 60%），RV 从 0.1%→0%（完全消除），同时 E-F1 和 R-F1 均微升，无性能损失。Composability 验证通过。

## Mistral SciERC Unconstrained 提交状态

- **exp_id**: w6_mistral_scierc_unconstrained
- **GPU**: cuda:0 @ westd-16980
- **PID**: 332156（GPU 子进程）
- **数据量**: 100 条 SciERC test
- **Registry**: RUNNING

---
