# analysis qwen14b oracle check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b-oracle-check_20260521T103216_result.json`
- **Structured JSON:** [`9fb135f454138c21069e.json`](../../sessions/9f/9fb135f454138c21069e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

**Oracle 86.67% 来自 exp-022**（`exp-022-oracle-proofwriter`），运行在 westd-32608，**不是 exp032**。

关键数据对比：

| 来源 | SC | SICA/Oracle | 备注 |
|------|-----|-------------|------|
| exp032 (westd-16639) | 73.5% (441/600) | 71.5% (429/600) | canonical SICA run |
| exp-022 (westd-32608) | 75.17% (451/600) | 86.67% (520/600) | oracle run，traces 标注为 "sica_expanded_14b" |
| 论文 Table 1 标准行 | **74.00%** | 71.50% | SICA 与 exp032 吻合，SC 不吻合 |
| 论文 Table 1 Oracle 行 | **74.00%** | **86.67%** | Oracle 与 exp-022 吻合，SC=74.00% 来源不明 |

**问题：**

1. **exp-022 的 traces 可能不是 exp032 的 traces** — SC baseline 不一致（75.17% vs 73.5%），说明 exp-022 用的是更早/不同的 Qwen14B traces（"sica_expanded_14b"）
2. **论文 SC=74.00% (444/600) 的来源不明** — 既不是 exp032 (73.5%) 也不是 exp-022 (75.17%)，可能来自某次 tiebreak 修正或其他 run
3. **论文 Delta +12.67pp 是用 74.00% 重算的**，而 exp-022 原始 delta 是 +11.50pp（基于其内部 SC=75.17%）

**建议：需要用 exp032 的 traces 重跑 Oracle，确保标准行和 Oracle 行共享同一组 traces。** 当前 Oracle 数据与 canonical run (exp032) 的对应关系不确定。

---
