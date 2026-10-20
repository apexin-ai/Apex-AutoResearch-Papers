# analysis oh cmdrep distribution

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oh-cmdrep-distribution_20260514T183233_result.json`
- **Structured JSON:** [`6d17776a5c98d755ec7a.json`](../../sessions/6d/6d17776a5c98d755ec7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**cmd_rep 在 OH 上的问题不是 FPR 高（仅 0.7%），而是 PROGRESS 标签严重不可靠（precision=48.5%）。**

根因：OH agent 的 stagnation 表现为"广泛但无效的探索"（view 不同文件、cd 不同路径、grep 不同模式）——每条命令文本都唯一，但整体没有进展。98.2% 的 OH stagnation 窗口命令完全唯一，触发了 `all_unique → PROGRESS` 规则，导致 36,901 个错误 PROGRESS 标签注入多数投票。

相比之下，SWE-agent 的 stagnation 表现为字面命令重复（反复 edit 同一行），cmd_rep 能正确捕捉。

推荐修复：**移除 `all_unique → PROGRESS` 规则**，改为 ABSTAIN。这是最小改动且能消除全部噪声。报告写在 `analysis/oh_cmdrep_distribution.md`。

---
