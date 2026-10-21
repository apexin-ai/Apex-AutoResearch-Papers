# audit data integrity critical

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-integrity-critical_20260522T202743_result.json`
- **Structured JSON:** [`dd07fd3dda7e6c8cf30a.json`](../../sessions/dd/dd07fd3dda7e6c8cf30a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部审计完成。以下是三个问题的完整追溯报告。

---

## 问题 1: Qwen2.5-14B × FOLIO — 三个不同的 SC 值

### 原始数据 (exp036_qwen25_14b_folio204, N=204)

| 指标 | 正确数 | 百分比 |
|------|--------|--------|
| SC (stored, 原始 tie-breaking) | 158 | **77.45%** |
| SC (D061, alphabetical tie-breaking) | 155 | **75.98%** |
| SICA | 154 | **75.49%** |

4 个 tie-diff 样本 (6:6 平票)：
- `folio_16`, `folio_49`, `folio_95`, `folio_117`

### 4-seed 结果 (表中标注 `4s`)

| Seed | SC_stored | SC_D061 | SICA |
|------|-----------|---------|------|
| exp036 | 77.45% | 75.98% | 75.49% |
| seed123 | 74.51% | 74.51% | 73.04% |
| seed456 | 74.02% | 74.02% | 74.02% |
| seed789 | 74.02% | 74.02% | 72.55% |
| **4-seed 均值** | **75.00%** | **74.63%** | **73.77%** |

### Table 1 当前值 vs 正确值

| 列 | Table 1 当前 | 实际来源 | 正确值 (D061, 4-seed avg) |
|----|-------------|---------|--------------------------|
| SC | 75.49% | **exp036 的 SICA**（填反了） | **74.63%** |
| SICA | 74.51% | **seed123 的 SC_stored**（来源错误） | **73.77%** |
| Δ | -0.98 | 两个错值相减 | **-0.86** |

**根因**: 表格编译脚本读取了 `sica_accuracy` 字段填入 SC 列，且不同 seed 之间的值被混用。

---

## 问题 2: Qwen3-14B × FOLIO — SC/SICA 列填反

### 原始数据 (exp_folio_2x2_qwen3, N=204)

| 指标 | 正确数 | 百分比 |
|------|--------|--------|
| SC (stored = D061, 无 tie 差异) | 170 | **83.33%** |
| SICA | 173 | **84.80%** |

2x2 metrics 交叉验证 (cell_d = Qwen3→Qwen3): `sc_acc=83.33, sica_acc=84.80` — 完全吻合。

### Table 1 当前值 vs 正确值

| 列 | Table 1 当前 | 实际来源 | 正确值 |
|----|-------------|---------|--------|
| SC | 84.80% | **SICA**（填反了） | **83.33%** |
| SICA | 84.31% (172/204) | **不匹配任何原始指标** | **84.80%** |
| Δ | -0.49 | — | **+1.47** |

**确认填反**。84.31% (172/204) 既不是 SC(170) 也不是 SICA(173)，来源不明（可能是脚本将错误的 SC 值减去某个 delta 反算得出）。

**注意**: 修正后 Δ 从 **-0.49** 变为 **+1.47pp**，SICA 对 Qwen3 FOLIO 实际上是正向提升（虽然仍不显著）。

---

## 问题 3: Mistral PW PID 对齐

### 结果: **0 个 PID 不匹配**

| 对比 | 不匹配数 |
|------|---------|
| mistral_pw_seed42 vs proofwriter_full.json | **0** |
| mistral_pw_seed123 vs proofwriter_full.json | **0** |
| mistral_pw_seed456 vs proofwriter_full.json | **0** |
| r11_3verifier_canonical vs proofwriter_full.json | **0** |

所有 600 个 PID 完全对齐，不存在 Q4/Q8 变体问题。

**但注意另一个差异**: r11_canonical (SC=39.33%, 236/600) 和 seed42 (SC=40.00%, 240/600) 的 SC 预测在 **90 个样本**上不同——这是因为它们是不同实验 run 的结果，不是 PID 对齐问题。seed789 仅完成 259/600（未跑完）。

---

### 修正优先级

1. **Qwen3-14B × FOLIO** (line 50): SC=83.33, SICA=84.80, Δ=+1.47 — **Δ 方向翻转**
2. **Qwen2.5-14B × FOLIO** (line 46): SC=74.63, SICA=73.77, Δ=-0.86 (4-seed D061 avg)
3. **Mistral PW PID**: 无需修复

---
