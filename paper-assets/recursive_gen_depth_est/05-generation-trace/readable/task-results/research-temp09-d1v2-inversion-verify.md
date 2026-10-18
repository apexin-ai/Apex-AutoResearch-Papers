# research temp09 d1v2 inversion verify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_temp09_d1v2_inversion_verify_20260515T044917_result.json`
- **Structured JSON:** [`4fa7cb6914f0783c529d.json`](../../sessions/4f/4fa7cb6914f0783c529d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**结论：(B) 协变量偏移（Covariate Shift）**

核心发现：temp09 在每个递归深度的特征值系统性低于 nucleus/topk50 约一个深度级别。例如 GPT-2 XL 的 p90_ppl（最重要特征）：
- temp09 d1 中位数 = 92.2，恰好落在训练数据 d2 范围（65–92）内
- temp09 d2 中位数 = 39.0，落在训练数据 d3 范围内

关键证据：
- 对每个策略独立做 z-score 标准化后重训，GPT-2 XL d1v2 AUC 从 0.1288 恢复到 **0.6817**，OLMo 从 0.2529 恢复到 **0.8340**
- 混淆矩阵显示分类器将 temp09 d1 判为 d2/d3（52%+25%），将 d2 判为 d3（96%）—— 是系统性深度高估，不是标签反转
- 组内 d1v2 AUC 分别为 0.9368/0.9029/0.8341，标签完全正确

物理解释：temperature=0.9 对 logit 分布的修改是均匀缩放而非截断（不同于 nucleus/top-k），模型在递归过程中更快收敛到 attractor 分布，使得 temp09 在 depth N 的统计特性等同于 nucleus/topk50 在 depth N+1 的特性。

报告已写入 `artifacts/temp09_d1v2_inversion_analysis.md`。

---
