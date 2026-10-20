# diagnosis maxsat root cause

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_maxsat_root_cause_20260516T013133_result.json`
- **Structured JSON:** [`f14a90c2ab47a5e4c745.json`](../../sessions/f1/f14a90c2ab47a5e4c745.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心结论：

**MaxSAT 全满足是三个问题叠加，不是单一 bug：**

1. **约束提取失败 54.4%** — QwQ-32B 收到 extraction prompt 后重新推理而非输出 JSON。最致命的是，3/4 多候选题（最需要 SICA 的场景）提取为零。

2. **一致投票 = 一致约束** — 14/17 题 12/12 同一答案，提取出的约束天然不矛盾。这是正确行为，不是 bug。

3. **评分偏差** — 唯一 SICA≠SC 的题 (498_Q8)，SICA 给 1 票的少数派打了 38 分 > 多数派 27 分，因为提取失败是非随机的。SICA 反而比 SC 差（87.5% vs 93.75%）。

**MaxSAT 求解器本身无 bug**（注入测试 6/6 通过）。

**推荐最小修复（~1 小时）**：
- **L3**：每条 trace 自动注入 `answer == &lt;trace_answer>` 约束，使不同答案的 trace 必有冲突
- **L1**：提取用 system prompt 强制 JSON-only，或换用 instruction-following 模型做提取

报告已写入 artifacts。

---
