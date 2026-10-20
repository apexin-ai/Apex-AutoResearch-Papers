# code r4 prompt sensitivity analysis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r4_prompt_sensitivity_analysis_20260517T141135_result.json`
- **Structured JSON:** [`3e1c7b361fb5f67bac96.json`](../../sessions/3e/3e1c7b361fb5f67bac96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个产出已注册：

**核心结果：**

| Prompt | Mode | ET% | RV% | DR% | ΔDR | E-F1 | R-F1 |
|--------|------|-----|-----|-----|-----|------|------|
| Default | Uncon | 0.40 | 1.39 | 15.37 | 94.0% | 31.01 | 8.23 |
| Default | Con | 0.00 | 0.00 | 0.93 | | 30.98 | 8.36 |
| Minimal | Uncon | 0.58 | 1.16 | 16.91 | 94.6% | 31.98 | 7.91 |
| Minimal | Con | 0.00 | 0.00 | 0.92 | | 31.99 | 7.85 |
| Detailed | Uncon | 0.22 | 0.45 | 11.07 | 94.2% | 33.55 | 10.48 |
| Detailed | Con | 0.00 | 0.00 | 0.64 | | 33.56 | 10.48 |

**关键发现：**
- ET/RV 在所有 prompt 下 100% 消除
- DR 降幅 94.0%–94.6%，σ=0.3pp，高度一致
- F1 最大变化 0.13pp，可忽略
- Prompt 对 unconstrained DR 的影响范围 5.84pp，constrained 下收窄至 0.29pp（20x 压缩），确认约束机制与 prompt 正交

**产出：**
- `art_20260517_2f2969` — `r4_prompt_sensitivity_results.md`（完整数据和分析）
- `art_20260517_27c027` — `appendix_prompt_sensitivity.tex`（LaTeX appendix，含表格和分析段落）

---
