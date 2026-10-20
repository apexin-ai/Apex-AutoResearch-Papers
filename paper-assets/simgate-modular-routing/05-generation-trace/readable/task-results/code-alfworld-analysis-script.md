# code alfworld analysis script

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alfworld-analysis-script_20260520T095619_result.json`
- **Structured JSON:** [`41a4ba811708e07434c7.json`](../../sessions/41/41a4ba811708e07434c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。111 episodes（比刚才多了 2 行，实验还在跑）。结果摘要：

| 指标 | Llama | Qwen |
|------|-------|------|
| det-preferred | 14.4% | 25.9% |
| int-preferred | 0.0% | 0.0% |
| no-preference | 85.6% | 72.6% |
| det-leaning (non-tie) | 100.0% | 100.0% |
| DAF | 0% | 0% |
| det-preferred 95% CI | [8.1%, 20.7%] | — |
| Δ_full (det-int) | 0.1439 [0.0811, 0.2072] | — |

脚本已部署到 `src/analyze_alfworld_llama.py`，输出 `analysis.json` 和 `latex_table.tex` 已保存到 `results/alfworld_llama_counterfactual/`。

---
