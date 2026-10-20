# fix all seeds tiebreaking audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_all-seeds-tiebreaking-audit_20260523T184334_result.json`
- **Structured JSON:** [`08d5dd7bcd901db303f9.json`](../../sessions/08/08d5dd7bcd901db303f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结果。

---

## Tiebreaking 审计结果

### 1. SC Tiebreaking: 全部 OK

所有 8 个多种子实验的 SC 答案与 alphabetical tiebreaking 重算结果**完全一致**（0 mismatches）。seeds 123/456/789 的实验脚本已正确使用 alphabetical tiebreaking。**无需修复。**

### 2. SICA Tiebreaking: 微小差异

每个实验有 2-5 个 SICA tie（MaxSAT 分数相同），存储的 SICA 答案使用了 dict 插入序（倾向 "Unknown"），与 alphabetical 有微小偏差。精度变化在 ±0.33pp 以内。

### 3. 修正后完整多种子汇总表（alphabetical tiebreaking）

**Mistral-7B PW-600** (4 seeds)

| Seed | SC% | SICA% | Δ(pp) | McNemar p |
|------|-------|-------|--------|-----------|
| 42 | 39.33 | 36.50 | −2.83 | (Table 1) |
| 123 | 40.83 | 37.50 | −3.33 | 0.0091 |
| 456 | 39.83 | 38.50 | −1.33 | 0.3222 |
| 789 | 38.83 | 37.17 | −1.67 | 0.1839 |
| **Mean±Std** | **39.70±0.85** | **37.42±0.83** | **−2.29±0.95** | |

**LLaMA-3.1-8B PW-600** (3 seeds, seed456 still running)

| Seed | SC% | SICA% | Δ(pp) | McNemar p |
|------|-------|-------|--------|-----------|
| 42 | 72.50 | 65.00 | −7.50 | 6.27e-08 |
| 123 | 71.33 | 64.00 | −7.33 | 5.0e-06 |
| 789 | 71.17 | 66.50 | −4.67 | 0.0009 |
| **Mean±Std** | **71.67±0.73** | **65.17±1.26** | **−6.50±1.59** | |

**Qwen2.5-14B PW-600** (4 seeds)

| Seed | SC% | SICA% | Δ(pp) | McNemar p |
|------|-------|-------|--------|-----------|
| 42 | 74.00 | 71.50 | −2.50 | (Table 1) |
| 123 | 72.33 | 70.83 | −1.50 | 0.1877 |
| 456 | 73.00 | 72.33 | −0.67 | 0.5716 |
| 789 | 73.67 | 71.83 | −1.83 | 0.0895 |
| **Mean±Std** | **73.25±0.74** | **71.62±0.63** | **−1.63±0.76** | |

### 4. SICA 修正详情

SICA 修正幅度（stored → alphabetical）：

| Experiment | Stored SICA% | Alpha SICA% | Diff |
|---|---|---|---|
| mistral_seed123 | 37.50 | 37.50 | 0 |
| mistral_seed456 | 38.67 | 38.50 | −0.17pp |
| mistral_seed789 | 37.17 | 37.17 | 0 |
| llama8b_seed123 | 64.17 | 64.00 | −0.17pp |
| llama8b_seed789 | 66.17 | 66.50 | +0.33pp |
| qwen25_seed123 | 71.17 | 70.83 | −0.33pp |
| qwen25_seed456 | 72.17 | 72.33 | +0.17pp |
| qwen25_seed789 | 71.67 | 71.83 | +0.17pp |

### 结论

1. **SC: 无需修复**，所有 seeds 已使用 alphabetical tiebreaking
2. **SICA: 存在微小差异**（最大 ±0.33pp），汇总表中已用 alphabetical 修正值
3. **seed42: 使用 Table 1 canonical 值**（已确认正确）
4. **llama8b_seed456: 仅完成 184/600**（30973 上运行中），未纳入汇总

---
