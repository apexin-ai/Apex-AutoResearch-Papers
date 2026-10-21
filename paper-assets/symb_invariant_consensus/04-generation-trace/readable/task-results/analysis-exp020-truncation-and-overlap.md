# analysis exp020 truncation and overlap

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp020-truncation-and-overlap_20260517T095938_result.json`
- **Structured JSON:** [`218bf0165dab4f57a38e.json`](../../sessions/21/218bf0165dab4f57a38e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整。下面是两个分析的结论。

---

## 分析 1: Truncation 影响

**78 题中 5 题有 truncation（共 8/936 条 trace 被截断）**

| 分组 | n | SICA | SC | SICA−SC |
|------|---|------|-----|---------|
| Truncated | 5 | 20.0% | 40.0% | **-20.0pp** |
| Clean | 73 | 67.1% | 68.5% | -1.4pp |

关键发现：
- **被截断的 trace 正确率 = 0%**（0/8），而正常 trace 正确率 63.4%（588/928）。截断的 trace 是纯噪声。
- 5 个 truncated 问题中 SICA 只对了 1 个，SC 对了 2 个。SICA 在截断题上表现更差（-20pp），可能因为 SICA 的约束提取依赖完整推理链，截断链提取出的约束是错误的。
- **但 truncation 不是 SICA 整体落后的主要原因**：clean 问题上 SICA−SC 仍为 -1.4pp，即使去掉截断题 SICA 依然没赢。

## 分析 2: exp-011 vs exp-020 同题对比（n=30）

| 实验 | SICA | SC | SICA−SC |
|------|------|-----|---------|
| exp-011 | 70.0% | 60.0% | **+10.0pp** |
| exp-020 | 66.7% | 70.0% | **-3.3pp** |

关键发现：
- **exp-011 的 +10pp 优势完全不可复现**。同样 30 题，exp-020 中 SICA−SC 反转为 -3.3pp。
- 一致性极低：SICA 仅 56.7% agreement（17/30），SC 仅 63.3% agreement（19/30）。14/30 题至少有一个指标翻转。
- exp-020 中 SC 从 60% 涨到 70%（+10pp），SICA 从 70% 降到 66.7%（-3.3pp），波动幅度巨大。
- exp-011 中 SICA-only wins 有 3 题，其中 2 题在 exp-020 中两个方法都错了，说明那些"独赢"不稳定。

**结论**：k=12 下 30 题的方差极大，exp-011 观察到的 +10pp 是随机波动而非真实信号。需要等 exp-020 全部 204 题完成才能得到可靠估计。

---
