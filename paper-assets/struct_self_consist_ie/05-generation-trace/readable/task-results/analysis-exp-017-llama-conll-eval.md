# analysis exp 017 llama conll eval

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_017_llama_conll_eval_20260514T175246_result.json`
- **Structured JSON:** [`0107b7d15e44428758b7.json`](../../sessions/01/0107b7d15e44428758b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

## exp_017 LLaMA CoNLL-2003 NER N=8 — 5-signal 结果

| Signal | ρ (full) | ρ (cond) | AUROC (full) | AUROC (cond) |
|--------|----------|----------|--------------|--------------|
| **SJ** | **0.4314** | **0.4356** | 0.7039 | 0.7225 |
| FK | 0.4277 | 0.4310 | 0.7026 | 0.7208 |
| logprob | 0.3072 | 0.3282 | **0.7610** | **0.8102** |
| EM | 0.4306 | **0.4403** | 0.7046 | 0.7257 |
| voting_conf | 0.4256 | 0.3743 | 0.7088 | 0.6989 |

**Conclusion: success**
- SJ ρ=0.431 > logprob ρ=0.307（Δ=+0.124），结构信号在相关性维度胜出
- ρ-AUROC 分离持续存在：logprob AUROC=0.761 > SJ AUROC=0.704
- EM 在 conditional split 上 ρ 最高（0.4403）
- N=8（非 N=16），因 3453 test instances 成本约束
- 与 exp_002（Qwen CoNLL N=8）和 exp_007（LLaMA SciERC N=8）直接可比

---
