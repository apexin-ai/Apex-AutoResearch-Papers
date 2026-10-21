# audit data truth appendix

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-truth-appendix_20260525T194238_result.json`
- **Structured JSON:** [`1fcaae9388512e10ff9a.json`](../../sessions/1f/1fcaae9388512e10ff9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是核心发现：

**覆盖**：24 个附录表格，~540 个数字，其中 ~380 个与服务器 JSON 源逐一对账。

**11 个问题**：
- **严重（2）**：
  - `tab:claude_crossbench` AEval Verb Likert d（论文 .252 vs 源 .298）和 p（.002 vs .0004）
  - `tab:cross_bench` GPT-4o MTB Likert d（.111 vs .135）和 p（.016 vs .007）
- **中等（5）**：
  - `tab:nli_ablation` "All" 列两个 cell 与源差 0.5-1.0pp（63.0% vs 63.5%，76.0% vs 77.0%）
  - `tab:gee_ci` Gemini verb Style OR（8.98 vs 源 9.16）
  - `tab:holm8` Gemini Form raw p（.0306 vs 源 .0448）
- **轻微（4）**：舍入偏差（TOST p 值 ±0.001）、fk_desc caption "all pairs" 实际匹配 NLI-passed

**已确认修复**：GEE 脚注 n=88/n=86 已正确区分。

**缺源 JSON**：tab:verb_n355、tab:concordance、tab:power、tab:bayesian_equiv 等 ~120 个数字仅有原始 JSONL/脚本，无预计算汇总，建议补充存档。

---
