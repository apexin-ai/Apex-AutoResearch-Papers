# analysis exp 033

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-033_20260518T190340_result.json`
- **Structured JSON:** [`0613d28377858175ee6c.json`](../../sessions/06/0613d28377858175ee6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**exp-033 结果与 capability trap 假设矛盾。**

| 指标 | 值 |
|---|---|
| n | 198/204 (97.1%) |
| SC accuracy | 54.04% |
| SICA accuracy | 59.09% |
| **Delta** | **+5.05pp** |
| McNemar exact p | **0.013** (显著) |
| 不一致对 | SICA纠正12题, SC纠正2题 |

关键解读：
- Mistral-7B 上 SICA 显著优于 SC，这是所有实验中最大的正向 delta
- 与 Qwen2.5-14B 的 delta=+0.25pp（不显著）和 pilot exp-010 的 delta=0 形成鲜明对比
- **Capability trap 假设过于简单化**：弱模型并非 "约束质量差所以无法提升"，而是 SC 共识低时 SICA 的约束加权反而提供了额外区分信号
- Pilot exp-010 (n=60) 的 delta=0 可能是小样本不具代表性

实验状态：198/204 题完成后进程中断（无完成标记），6 题缺失不影响显著性结论。JSON 的 summary 部分是 n=188 时的快照，实际 results 数组有 198 条记录。

报告已写入 `artifacts/exp033_analysis.md`。

---
