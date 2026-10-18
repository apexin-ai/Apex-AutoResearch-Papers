# code nli gate full validation

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nli_gate_full_validation_20260521T114504_result.json`
- **Structured JSON:** [`2b981203faf31179c5fd.json`](../../sessions/2b/2b981203faf31179c5fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量验证完成。结果：

| | Formality | Verbosity | Overall |
|---|---|---|---|
| N | 100 | 100 | 200 |
| Agreement | **88.0%** | **79.0%** | **83.5%** |
| Cohen's κ | 0.47 | 0.31 | 0.38 |
| Pass precision | 92.1% | 82.6% | 87.4% |
| Fail recall | 58.3% | 57.1% | 57.7% |
| Base rate pass | 88% | 86% | 87% |

**Confusion (overall)**: TP=152, FP=22, TN=15, FN=11

**vs spot-check**: Full agreement 83.5% vs spot-check 65.0% (+18.5pp)。差异主要因为 spot-check 人为平衡了 50 pass/50 fail，而全量数据 pass 占 87%——pass 组 agreement 高（~92%）拉高了整体。

关键发现：
- NLI pass 判定可靠（pass precision 87-92%）
- NLI fail 判定较弱（fail recall 仅 58%）——GPT-4o 认为约 42% 的 NLI-fail 对实际保留了语义
- Formality 表现优于 verbosity（κ=0.47 vs 0.31）

脚本 `csd_pipeline/nli_gate_full_validation.py`，结果 `data/nli_gate_full_validation.json`。

---
