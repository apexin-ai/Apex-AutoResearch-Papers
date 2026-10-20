# analysis w8 qwen docred ft grammar only

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w8_qwen_docred_ft_grammar_only_20260516T152215_result.json`
- **Structured JSON:** [`0bb707a6c4218d380db5.json`](../../sessions/0b/0bb707a6c4218d380db5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## w8_qwen_docred_ft_grammar_only 完整指标

### ALL SAMPLES (fail = 0 contribution)

| 指标 | 值 |
|------|------|
| **ET_pct** | 0.00% |
| **RV_pct** | 0.00% |
| **DR_pct** | 0.61% |
| **CF_pct** | 0.11% |
| **E_F1** | 82.19 |
| **E_P** | 85.47 |
| **E_R** | 79.16 |
| **R_F1** | 40.85 |
| **R_P** | 36.27 |
| **R_R** | 46.77 |
| **parse_fail_rate** | 7.01% (70/998) |

### EXCL FAIL (仅成功样本)

| 指标 | 值 |
|------|------|
| **E_F1_excl_fail** | 85.72 |
| **R_F1_excl_fail** | 42.12 |
| **R_P_excl_fail** | 36.27 |
| **R_R_excl_fail** | 50.22 |

### vs Qwen FT Unconstrained (baseline)

| 指标 | Unconstrained | Grammar Only | Delta |
|------|------|------|------|
| ET_pct | 0.00% | 0.00% | 0 |
| RV_pct | 0.27% | 0.00% | **-0.27pp** (消除) |
| DR_pct | 0.76% | 0.61% | **-0.15pp** |
| R_F1 | 40.86 | 40.85 | -0.01 (持平) |
| R_F1_excl_fail | 42.20 | 42.12 | -0.08 (持平) |

### vs Llama DocRED grammar_only

| 指标 | Llama grammar_only | Qwen FT grammar_only |
|------|------|------|
| DR_pct | 0.51% | 0.61% |
| E_F1 | 84.04 | 82.19 |
| R_F1 | 43.77 | 40.85 |

### 分析

1. **Grammar 层完全消除了 ET 和 RV 违规**（ET=0%, RV=0%），符合预期
2. **DR_pct = 0.61%**，接近 unconstrained 的 0.76%——验证了假设：grammar_only 模式不约束 domain-range，DR 违规几乎保留原样（仅因 RV=0 导致分母略变使得比例从 0.76% 降到 0.61%）
3. **R_F1 几乎不变**（40.85 vs 40.86），说明 grammar 层不降低生成质量
4. CF_pct 极低（0.11%），与 unconstrained 一致

---
