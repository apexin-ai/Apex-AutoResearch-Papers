# analysis eval gsm8k grpo cka only 20 verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_gsm8k_grpo_cka_only_20_verify_20260523T161315_result.json`
- **Structured JSON:** [`88cbc4c5981a071199b6.json`](../../sessions/88/88cbc4c5981a071199b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

| | 原始 (v2) | Verify | 差异 |
|---|---|---|---|
| accuracy | 64.37% | 64.06% | -0.31pp |
| n_correct | 849 | 845 | -4 |
| n_total | 1319 | 1319 | — |
| stderr | — | ±1.32% | — |

**Conclusion: success.** 差异 0.31pp 远小于 stderr 1.32%，跨服务器（westd → westb）可重复性确认。论文 Tab 1/Tab 2 中 64.37% 的数据点可靠。

---
