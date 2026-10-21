# analysis f2 discriminative analysis

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_f2-discriminative-analysis_20260518T110418_result.json`
- **Structured JSON:** [`7f0cd1c52b2affae5426.json`](../../sessions/7f/7f0cd1c52b2affae5426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已保存到 `artifacts/f2_discriminative_analysis.md`。

核心发现：

- **r = -0.58**: constraint count 与 exclusion rate 强负相关，更多约束 = 更多噪声（domain facts 堆积），直接支持 capability trap 叙事
- **85% 问题只有 1 个 excluded constraint**: SICA 的整个机制在绝大多数情况下依赖单个判别性约束的权重
- **entropy=1.0 是 SICA 的核心优势区间**: 38 个 4:4 平票问题上 SICA +10.5pp（55.3% vs 44.7%），52.6% 发生 flip，SICA 赢 12:8
- **GT=Unknown 问题 SICA 优势最大**: flipped 案例中 SICA 6:3 赢 SC，约束对开放世界推理（"不确定"作为合法答案）帮助最大
- **低 cc + 高 ER vs 高 cc + 低 ER**: 12pp 准确率差距（69.5% vs 57.5%），少而精的约束远优于多而泛的约束

---
