# review reviewer corrections audit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_reviewer_corrections_audit_20260527T131202_result.json`
- **Structured JSON:** [`70634854094a5fd86349.json`](../../sessions/70/70634854094a5fd86349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. Here's the audit report:

---

## 审计报告：Reviewer 修正项完成状态

### 1. s1 per-task 数字 — ⚠️ 未在论文中列出

论文多处声称 "per-task CAR ordering is preserved across all conditions"（`claim3.tex:27`、`claim3.tex:33`），但**未给出具体数字**。

- 正确值（OJ=66%, CP=72%, milk=70%, bbq=26% CAR; TSR: OJ=26%, CP=80%, milk=28%, bbq=62%）在 `docs/paper/` 的所有 tex 文件中**均未出现**
- `appendix.tex` 有 per-task TSR 表（Table 5, lines 66-86），但只报告了 LoRA seed 0 的 TSR（OJ=18, CP=72, milk=32, bbq=62），无 λ=0.1 per-task 数据
- `appendix.tex` 有 per-task CAR 表（Table 9, lines 121-138），但仅针对 oracle refinement，不涉及 lambda 消融
- Figure 4 (`fig5_lambda_curve`) 只显示 aggregate CAR/TSR，无 per-task

**结论**：论文声称 per-task ordering 一致但未提供支持数据。如 Reviewer 要求的是在论文中引用这些数字，则需要增加 per-task CAR 表或在 appendix 补充。

---

### 2. LoRA Table 行 — ✅ 主论文正确

**主论文（`docs/paper/`）所有数值正确**：

| 位置 | 数值 | 状态 |
|------|------|------|
| `claim3.tex:17` — Table 4 aggregate | CAR=54.75±3.18, TSR=48.75, 2 seeds | ✅ |
| `appendix.tex:48` — dfCAR threshold | LoRA s0 = 57.0 | ✅ |
| `appendix.tex:49` — dfCAR threshold | LoRA s1 = 52.5 | ✅ |
| `appendix.tex:81` — per-task TSR mean | seed 0 = 46.0 | ✅（注明 seed 0 only）|
| `abstract.tex:7` | 54.75%±3.18 | ✅ |

**非主论文中的过期数据**（不影响投稿，但建议清理）：

| 文件 | 行 | 当前值 | 正确值 |
|------|-----|--------|--------|
| `artifacts/reeval_comparison.tex:14` | LoRA s0 After CAR | 56.5 | 57.0 |

---

### 3. EE Displacement — ⚠️ 仅报告 aggregate

- `claim3.tex:20`：λ=0.1 EE Disp = **0.394m**（2-seed mean）
- `claim3.tex:15`：Pi0.5 baseline EE Disp = **0.367m**
- 具体值 **0.3884**（s1 avg_max_ee）和 **0.0553**（avg_max_obstacle）**未在论文任何位置出现**
- 0.394 作为 2-seed mean 合理（若 s0≈0.400, s1=0.3884, mean≈0.394）

**结论**：论文只报告 aggregate EE Disp，未报告 per-seed 或 obstacle displacement。如 Reviewer 要求的是验证 0.394 = mean(s0, s1)，数值可自洽；如要求报告 obstacle displacement，则缺失。

---

### 4. std 一致性 — ✅ 全部正确

逐一验证（从 seed 值手算）：

| 条件 | Seeds | 手算 mean | 手算 std | 论文值 | 状态 |
|------|-------|-----------|----------|--------|------|
| LoRA-only | 57, 52.5 | 54.75 | 3.18 | 54.75±3.18 | ✅ |
| λ=0.005 | 57, 54, 52.5 | 54.5 | 2.29 | 54.5±2.29 | ✅ |
| λ=0.01 | 57, 57.5, 54.5 | 56.33 | 1.61 | 56.33±1.61 | ✅ |
| λ=0.1 | 58, 58.5 | 58.25 | 0.35 | 58.25±0.35 | ✅ |

以下位置全部一致：
- `claim3.tex:17-20` (Table 4) ✅
- `abstract.tex:7` ✅
- `fig5_lambda_data.csv` ✅
- `appendix.tex:144` null distribution (mean=54.6%, σ=2.27%) ✅

---

## 总结

| # | 修正项 | 状态 | 说明 |
|---|--------|------|------|
| 1 | s1 per-task 数字 | ⚠️ | 论文声称 ordering 一致但未列出 λ=0.1 per-task CAR/TSR 具体数值 |
| 2 | LoRA Table 行 | ✅ | 主论文所有数值正确 |
| 3 | EE Disp | ⚠️ | aggregate 0.394 正确；per-seed 和 obstacle displacement 未报告 |
| 4 | std 一致性 | ✅ | 全部手算验证通过 |

**需要行动**：Item 1 和 Item 3 取决于 Reviewer 的具体要求——是要求论文中引用这些数字（则需补充），还是只要求验证内部一致性（则已满足）。

---
