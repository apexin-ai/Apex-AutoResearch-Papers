# analysis exp 081 082 status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-081-082-status-check_20260519T230809_result.json`
- **Structured JSON:** [`245551d352d7471e609e.json`](../../sessions/24/245551d352d7471e609e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均 **仍在运行中**，状态汇总：

### exp-081: Debate × Mistral-7B × FOLIO-204 (seed=123)
- **状态**: 运行中，116/204 (56.9%)
- **已用时间**: ~100 min，ETA ~78 min
- **当前中间指标** (n=115):
  - debate_accuracy = **0.4174**
  - sc_accuracy = **0.5739**
  - delta = **-0.1565** (debate 比 SC 差)
  - fallback_count = 11
  - total_debate_constraints = 2,347

### exp-082: Contrastive × Mistral-7B × FOLIO-204 (seed=123)
- **状态**: 运行中，105/204 (51.5%)
- **已用时间**: ~100 min，ETA ~97 min
- **当前中间指标** (n=104):
  - contrastive_accuracy = **0.5096**
  - sc_accuracy = **0.5769**
  - delta = **-0.0673** (contrastive 比 SC 差)
  - degenerate_count = 18
  - pro_constraints = 533, con_constraints = 478

两个方法目前都未超过 SC baseline。Contrastive 的 delta (-0.067) 比 Debate 的 (-0.157) 小，表现相对更好。预计两个实验还需 ~1.5 小时完成。

---
