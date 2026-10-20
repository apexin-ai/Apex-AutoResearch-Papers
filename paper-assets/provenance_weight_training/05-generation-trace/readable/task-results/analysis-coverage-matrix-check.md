# analysis coverage matrix check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_coverage_matrix_check_20260515T085216_result.json`
- **Structured JSON:** [`1e1ee0519396e567de39.json`](../../sessions/1e/1e1ee0519396e567de39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已保存到 `artifacts/coverage_matrix_analysis.md`。

## 核心发现

**总体覆盖率 ~55%**，有 3 个 CRITICAL/HIGH 缺口必须在投稿前填补：

### 🔴 CRITICAL Gaps

| # | 缺口 | 影响 | GPU 时间 |
|---|------|------|---------|
| **G1** | ESS-only baseline | Claim 1 完全无证据（min vs max intervention） | ~3.5h |
| **G2** | τ sweep (0.6/0.7/0.8/0.9) | Claim 3 "τ 不敏感" 只是断言 | ~14h |
| **G3** | Golden Ratio oracle | Positioning 缺 oracle upper bound | ~3.5h |

### 已完成的实验基础是扎实的

- Claim 2 (adaptive ≈ grid-best) **已 PASS** — 3 seeds 一致，aggregate 88.6%
- 主结果表数据齐全：uniform/grid-best/adaptive × 3 seeds
- Grid landscape seed42 + seed123 全部 6 个 b 值完成，seed456 即将完成
- b* 轨迹、α_eff/ESS 双约束图可从现有 step_metrics 生成

### 时间评估

10 天**足够但紧张**。当前 4 个 RUNNING 实验即将释放 GPU，G1-G3 约 1 天可并行完成。加上 n_min/batchsize 消融再 1 天。剩余 6-7 天写论文。

**关键风险**：如果 ESS-only baseline ≈ dual-constraint，Claim 1 差异化消失，需要额外 1-2 天 reframe。

---
