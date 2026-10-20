# analysis a075 s43 5method leadlag

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a075_s43_5method_leadlag_20260516T142157_result.json`
- **Structured JSON:** [`9fce660d02179fa5afe1.json`](../../sessions/9f/9fce660d02179fa5afe1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成

### s43 单独结果
| Metric | Value |
|--------|-------|
| Perm Granger FDR forward | **5/8** sig |
| Perm Granger FDR reverse | **0/8** |
| Consensus ≥3/5 | **6/8** robust |
| Threshold onset | **4/8** (entropy leads 1 gen) |

### Cross-seed 汇总 (s42/s43/s44, 统一 pipeline)

| Pair | s42 | s43 | s44 | 3-seed consistent |
|------|-----|-----|-----|-------------------|
| ece→d1 | * | * | * | **YES** |
| ece→d2 | * | * | * | **YES** |
| ece→d3 | * | * | * | **YES** |
| 其余5对 | mixed | mixed | mixed | no |

**关键结论**：
- 方向性完全稳定：24 次 reverse 测试全部 non-sig
- ECE → diversity (d1/d2/d3) 是最可复现的 Granger 信号（3/3 seeds）
- token_entropy 在 threshold onset 上完美稳定（4/8 all seeds，all lead=1 gen）
- 注意：s42 用统一 pipeline 重跑后为 8/8（旧版 3/8 因代码版本差异）

### 产出
- `artifacts/alpha_sweep_a075_s43/data/a075_s43_5method_results.json`
- `artifacts/alpha_sweep_a075_s43/report/a075_s43_5method_analysis.md`
- `artifacts/_project/data/a075_3seed_cross_seed_summary.txt`
- 服务器完整 JSON: `results/alpha_sweep/a075_s43/analysis/5method_leadlag.json`

---
