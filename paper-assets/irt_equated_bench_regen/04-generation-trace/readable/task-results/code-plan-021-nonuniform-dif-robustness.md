# code plan 021 nonuniform dif robustness

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_021_nonuniform_dif_robustness_20260521T052135_result.json`
- **Structured JSON:** [`3afd4568acc691d2d6b7.json`](../../sessions/3a/3afd4568acc691d2d6b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**9 个 MMLU subjects（1787 items），Logistic Regression DIF 结果：**

| 指标 | 数值 |
|------|------|
| Uniform DIF only | 472 (26.4%) |
| Non-uniform DIF only | 171 (9.6%) |
| Both | 520 (29.1%) |
| Neither | 624 (34.9%) |
| **Any non-uniform DIF** | **691 (38.7%)** |

**MH 一致性**: MH C-class items 中 92.1% 也被 LR 标记为 uniform DIF — 方法间高度吻合。

**关键发现**: Non-uniform DIF 比例较高（38.7%）且 effect size 不小（|β_interaction| 中位数 0.58），说明 2023→2024 的 temporal shift 不仅是 difficulty shift，还有 discrimination 差异。这**强化**了论文的论点——MMLU 的 temporal instability 比 MH 单独检测到的更严重。MH A/B items 中有 29.8% 存在 non-uniform DIF，是 MH 结构性盲区。

产出文件在 `artifacts/plan_021/`，报告和数据已注册。

---
