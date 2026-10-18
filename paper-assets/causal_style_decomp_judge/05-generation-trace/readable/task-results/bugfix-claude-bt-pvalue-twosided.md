# bugfix claude bt pvalue twosided

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_claude-bt-pvalue-twosided_20260523T014657_result.json`
- **Structured JSON:** [`c1a8ed7359b1eea76048.json`](../../sessions/c1/c1a8ed7359b1eea76048.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Old vs New p-value 对比：

| Config | Old p (one-sided) | New p (two-sided) | Status |
|---|---|---|---|
| LLMBar formality | 0.0617 | **0.1234** | NS (仍 >0.05) |
| LLMBar verbosity | 0.1769 | **0.3538** | NS |
| AlpacaEval formality | 0.0 | **0.0** | *** |
| AlpacaEval verbosity | 0.0 | **0.0** | *** |
| MT-Bench formality | 0.0 | **0.0** | *** |

符合预期：LLMBar formality 从 0.0617 → 0.1234（恰好翻倍，因为偏向单侧），LLMBar verbosity 同理翻倍。三个 p=0.0 的配置不变（10000 次 bootstrap 中没有一次跨过 0.5）。所有显著性判断不受影响。

代码修改：服务器 `claude_crossbench_analysis.py:121` 从 `np.mean(boots <= 0.5)` 改为 `min(2 * min(np.mean(boots <= 0.5), np.mean(boots >= 0.5)), 1.0)`。

---
