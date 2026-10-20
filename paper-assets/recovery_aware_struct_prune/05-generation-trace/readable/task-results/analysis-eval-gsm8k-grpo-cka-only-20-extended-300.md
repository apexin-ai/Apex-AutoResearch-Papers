# analysis eval gsm8k grpo cka only 20 extended 300

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_gsm8k_grpo_cka_only_20_extended_300_20260519T034758_result.json`
- **Structured JSON:** [`9f7eddb9610d084bc33d.json`](../../sessions/9f/9f7eddb9610d084bc33d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**GSM8K 准确率: 64.37% (849/1319)** — 与 100 步完全相同。

| 模型 | 步数 | GSM8K |
|------|------|-------|
| CKA-only 20% GRPO | 100 | 64.37% |
| CKA-only 20% GRPO | **300** | **64.37%** |
| Standard 20% GRPO | 100 | 58.91% |
| RASP 20% GRPO | 100 | 56.71% |
| Dense (unpruned) | — | 72.78% |

**结论: negative** — 300 步训练在 GSM8K (ID) 上没有任何提升，模型在 100 步已饱和。Registry 已更新为 DONE/negative，分析报告已注册为 artifact。

---
