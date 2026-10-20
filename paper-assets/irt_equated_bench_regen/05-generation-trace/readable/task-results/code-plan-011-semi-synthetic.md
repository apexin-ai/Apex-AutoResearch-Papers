# code plan 011 semi synthetic

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_011_semi_synthetic_20260520T213716_result.json`
- **Structured JSON:** [`7a12e85e18997e08cb1b.json`](../../sessions/7a/7a12e85e18997e08cb1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。核心结论：

**MH-DIF 能够检测注入的差异性污染**，验证通过。

### 关键数字（external MH，最佳匹配）

| Cohort | p=0 (baseline) TPR | p=1.0 TPR | ΔTPR | FPR (constant) |
|--------|---------------------|-----------|------|----------------|
| **temporal** | 0.326 | **1.000** | **+0.674** | 0.314 |
| **ability** | 0.498 | **0.800** | **+0.302** | 0.493 |

### 三个发现

1. **DIF 方法 work** — temporal cohort 在 p≥0.5 时 TPR 已达 0.83，p=1.0 时 100%。剂量-响应关系单调递增，Fisher exact p < 0.0001。

2. **plan_001 失败是 ground truth 不匹配** — Li et al. 的 web-overlap 标签标记的是全局性污染（所有模型都能从 Common Crawl 获益），不会产生 group-specific DIF。MH-DIF 只能检测差异性效应。

3. **匹配变量污染效应** — 注入 100/500=20% items 时，standard MH 的 FPR 随 p 上升（temporal 从 0.30 → 0.62），因为注入项膨胀了 focal 总分。anchor/external 变体中 FPR 保持恒定，确认了这是匹配变量污染而非方法缺陷。

### 注意事项

- Ability cohort 因 Q1-2 与 Q4-5 accuracy 无重叠，即使 external matching 仍有 ~49% baseline FPR（5 层分层不足以消除极端能力差异）
- 修复了 plan_001 代码中的 inf-delta 分类 bug（`np.isfinite(delta)==False` 时应为 extreme DIF，非 class A）

---
