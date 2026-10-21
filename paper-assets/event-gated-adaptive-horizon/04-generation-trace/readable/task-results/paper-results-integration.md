# paper results integration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_results-integration_20260516T195701_result.json`
- **Structured JSON:** [`0c7702e83d921a13cf04.json`](../../sessions/0c/0c7702e83d921a13cf04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results section 草稿已写入 `artifacts/paper_drafts/results_section_draft.md`。

结构覆盖全部 7 个 Finding（F1–F7），每个 Finding 包含：
- 实验配置与 exp_id
- 关键数字（NVE、eval return、collapse 时间点）
- 与 baseline/对照组的直接对比
- Bootstrap CI（有数据时标注）
- 语言强度严格匹配证据量（n=1 标注 proof-of-concept，n≥3 用 reliably）

主要注意事项：
- F6 (Full-SGS) 和 F4 (Cheetah) 均为 n=1，已明确标注为 proof-of-concept / single-environment replication
- F2 的 effect size CI [+0.91, +3.10] 排除零，是最强统计支撑
- F7 (Pathway B) 作为 open problem 呈现，诚实报告 SGS 未覆盖的残余风险
- 未使用 "significantly" 一词（无正式假设检验），仅报告 CI 和 effect size

---
