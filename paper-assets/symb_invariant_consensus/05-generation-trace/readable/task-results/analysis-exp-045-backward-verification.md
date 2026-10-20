# analysis exp 045 backward verification

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-045-backward-verification_20260518T194233_result.json`
- **Structured JSON:** [`49a423f7f7cc81f535a5.json`](../../sessions/49/49a423f7f7cc81f535a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-045-backward-verification 分析完成。Conclusion: NEGATIVE。**

核心发现：

- **BV accuracy = 53.92%，SC baseline = 75.00%，delta = -21.08pp**。这是目前测试过的最差方法。
- **严重 True 偏置**：预测 72.5% 为 True（gold 仅 35.3%）。True 准确率 90.3%，但 False 仅 20.6%，Unknown 仅 46.4%。
- **Z3 无判别力**：SAT rate 高达 95.3%（supporting 98.4%, contradicting 89.7%）。LLM 生成的 backward FOL 几乎全部被 Z3 满足，scoring 机制退化为统计 FOL 表达式数量而非逻辑有效性。
- **42.5% 的 rounds 出现 score ties**，进一步削弱决策质量。

**根因**：Backward verification 没有绕过 capability trap，而是把瓶颈从 forward FOL extraction 转移到 backward FOL generation。LLM 生成的 backward FOL 质量同样差，只是表现形式不同（uniformly SAT 而非 incorrect constraints）。验证方向无关紧要，FOL 质量才是约束。

报告已写入 `artifacts/analysis_exp045.md`，registry 已更新（conclusion=negative, metrics, checkpoint_path）。

---
