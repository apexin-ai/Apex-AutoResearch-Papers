# code pvalue sweep fix

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pvalue_sweep_fix_20260519T063141_result.json`
- **Structured JSON:** [`7037f3d8beba8081a181.json`](../../sessions/70/7037f3d8beba8081a181.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。汇总：

### FINAL_REPORT.md — 19 行修改

**Section 4.1 叙事文本（3处）：**
- L70 GDN: `p = 0.037` → `one-tailed p = 0.0417`
- L74 HGRN2: `one-tailed p < 0.01` → `one-tailed p = 0.0083`
- L76 RetNet: `p = 0.037` → `one-tailed p = 0.0417`

**Section 4.2 收敛表（7处）：**
- 表头 `p-value` → `p (1-tail)`
- LAMBADA: `<0.01` → `0.0083`
- HellaSwag: `0.624` → `0.3417`
- Winogrande: `0.873` → `0.4750`
- ARC-Easy: `0.188` → `0.1167`
- ARC-Challenge: `0.285` → `0.1750`
- MMLU: `0.188` → `0.1167`
- L95 叙事: `p < 0.01` → `p = 0.0083`

**Section 4.3 每架构表（7处）：**
- 表头列名加 `(1-tail)`
- LAMBADA: GDN/RetNet `0.037` → `0.0417`，HGRN2 `<0.01` → `0.0083`
- 其余 15 个 p 值全部替换为精确排列检验 one-tailed 值

### convergence_analysis.py
- 添加 `exact_spearman_p()` 暴力枚举函数
- `spearmanr()` 调用替换为精确排列检验
- 输出已验证：two-tailed 精确值与枚举一致

### 未修改
- `cross_scale_convergence.py`：已使用精确排列检验，无需修改
- `lambada_matched_comparison.py`：无 Spearman p 值

### 精确排列检验参考值（n=5, 暴力枚举验证）

| |ρ| | two-tailed | one-tailed |
|---|---|---|
| 1.0 | 2/120 = 0.0167 | 0.0083 |
| 0.9 | 10/120 = 0.0833 | 0.0417 |
| 0.7 | 28/120 = 0.2333 | 0.1167 |
| 0.6 | 42/120 = 0.3500 | 0.1750 |
| 0.5 | 54/120 = 0.4500 | 0.2250 |
| 0.4 | 62/120 = 0.5167 | 0.2583 |
| 0.3 | 82/120 = 0.6833 | 0.3417 |
| 0.2 | 94/120 = 0.7833 | 0.3917 |
| 0.1 | 114/120 = 0.9500 | 0.4750 |

注意：用户提供的参考表中 |ρ|=0.8 以下部分计数有误（如 |ρ|=0.8 实际为 16/120=0.1333 而非 20/120=0.1667），所有修改均基于暴力枚举验证值。

---
