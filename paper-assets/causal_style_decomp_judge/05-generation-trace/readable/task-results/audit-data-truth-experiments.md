# audit data truth experiments

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-truth-experiments_20260525T194216_result.json`
- **Structured JSON:** [`83c5dbd7efd029f5d970.json`](../../sessions/83/83c5dbd7efd029f5d970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**Table 1 & Table 2：** 绝大多数 cell 验证通过。14/14 BT 值正确，12/12 GEE 配置基本正确（Gemini verbosity 有源文件追溯性缺口但 registry 值一致）。

**3 个 HIGH 问题（必须修复）：**
1. **L166 Sobel z/p 完全错误** — 论文写 z=2.15, p=.031，源文件记录 z=3.60, p=0.0003。可能将 Style OR 2.15 误抄为 Sobel z
2. **L166 "direct-effect Style OR=2.15 for GPT-4o (total OR=2.70)"** — 无法追溯。GPT-4o formality Style OR=2.58 不是 2.70，2.15 恰等于 Qwen3 n=355 数据，可能 judge 混淆
3. **L168 Llama-70B AlpacaEval "Style OR=7.64"** — GEE 为 degenerate，7.64 无任何源文件

**4 个 MEDIUM 问题：** sign test p 值混用两个分析、verbosity 方向百分比 90.7%/80.6% vs 源 91.2%/82.8%、Gemini verbosity GEE 底层 JSON 不匹配、100pt scaling p>0.15 断言与 GPT-4o verbosity 数据矛盾。

---
