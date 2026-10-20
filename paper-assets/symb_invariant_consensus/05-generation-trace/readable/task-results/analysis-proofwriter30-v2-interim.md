# analysis proofwriter30 v2 interim

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_proofwriter30_v2_interim_20260516T012158_result.json`
- **Structured JSON:** [`e173fa57c8732dd1aa8b.json`](../../sessions/e1/e173fa57c8732dd1aa8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心结论：

**SICA 严格劣于 SC**（87.5% vs 93.75%，gap = −6.25pp）。

三个关键问题：
1. **Problem #11 反向翻转**：SC 以 11:1 正确投票 False，但 SICA 的约束加权评分 (F:27 vs T:38) 将答案错误翻转为 True。少数错误 trace 产生了更多约束权重。
2. **约束提取率仅 48.4%**（trace 级），99 条 "No JSON found" 警告全部是约束提取失败（答案提取正常）。3 题（#4, #5, #14）完全零约束。
3. **零矛盾检出**：所有 16 题 satisfied_ratio=1.000，excluded=0。MaxSAT 从未排除任何约束。

D012 预测：C2（矛盾检出）和 C3（SICA≥SC）极可能 FAIL。

---
