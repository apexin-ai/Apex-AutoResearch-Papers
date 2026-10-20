# data bootstrap ci summary

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_bootstrap_ci_summary_20260514T210533_result.json`
- **Structured JSON:** [`1b6257700ddbd374d395.json`](../../sessions/1b/1b6257700ddbd374d395.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。汇总 JSON 保存在 `artifacts/data/bootstrap_ci_summary.json` 并已注册。

**数据覆盖:**

| 数据集 | 信号 | full | cond | 备注 |
|--------|------|------|------|------|
| Qwen SciERC 3-seed | SJ/FK/logprob | ✓ | ✓ | EM/voting_conf 缺失（exp_001 未生成 all_signals_report） |
| LLaMA CoNLL 3-seed | 5 signals | ✓ | ✓ | 含 per-seed CI95 和 AUROC |
| N-scaling bootstrap (B=10000) | 5 signals | Qwen_CoNLL, Qwen_SciERC, LLaMA_SciERC | — | LLaMA_CoNLL 未做 N-scaling bootstrap |
| 单信号 bootstrap (B=1000) | SJ/FK/voting_conf | NER + RE (full + cond) | — | 来自 exp004_re_diagnostic |

**缺失项:**
- Qwen SciERC 3-seed 的 EM 和 voting_conf（需对 exp_001 补跑 all_signals 分析）
- LLaMA CoNLL 的 N-scaling bootstrap（bootstrap_ci_nscaling 中未包含此配置）

---
