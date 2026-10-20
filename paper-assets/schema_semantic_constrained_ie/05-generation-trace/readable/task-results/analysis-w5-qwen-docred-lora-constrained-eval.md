# analysis w5 qwen docred lora constrained eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w5_qwen_docred_lora_constrained_eval_20260516T080646_result.json`
- **Structured JSON:** [`742085b69491ad0cd4d8.json`](../../sessions/74/742085b69491ad0cd4d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## W5 Qwen DocRED LoRA Constrained Eval 结果

### Constrained Metrics

| Metric | Constrained | Unconstrained | Delta |
|--------|-------------|---------------|-------|
| **ET_pct** | 0.00% | 0.00% | 0.00pp |
| **RV_pct** | 0.00% | 0.27% | **-0.27pp** |
| **DR_pct** | 0.01% | 0.76% | **-0.75pp** |
| **CF_pct** | 0.41% | 0.12% | +0.29pp |
| **E_F1** | 81.43 | 82.15 | -0.72pp |
| **E_P** | 85.41 | 85.44 | -0.03pp |
| **E_R** | 77.81 | 79.11 | -1.30pp |
| **R_F1** | 40.56 | 40.86 | -0.30pp |
| **R_P** | 36.35 | 36.41 | -0.06pp |
| **R_R** | 45.86 | 46.56 | -0.70pp |
| parse_fail_rate | 8.52% | 7.11% | +1.41pp |
| total_samples | 998 | 998 | — |
| success/fail | 913/85 | — | — |
| total_entities_pred | 17799 | — | — |
| total_relations_pred | 15563 | — | — |
| **E_F1_excl_fail** | 85.69 | 85.72 | -0.03pp |
| **R_F1_excl_fail** | 42.23 | 42.20 | **+0.03pp** |

### Composability 结论

1. **DR 几乎消除**：0.76% → 0.01%（98.7% 相对下降，15563 个 relation 中仅剩 2 个违规）
2. **RV 完全消除**：0.27% → 0.00%
3. **R_F1 保持不变**：excl_fail 口径下 42.20 → 42.23（+0.03pp），overall 的微降（-0.30pp）完全由 parse_fail_rate 上升解释
4. **CF 略升**：0.12% → 0.41%，cross-field consistency 是 constrained decoding 未覆盖的维度

### 与 Llama 对比

| Model | DR_uncon | DR_con | ΔDR | ΔR_F1 (excl_fail) |
|-------|----------|--------|-----|-----|
| **Qwen** | 0.76% | 0.01% | **-0.75pp** (98.7% ↓) | +0.03pp |
| Llama | 0.49% | 0.20% | -0.29pp (59.2% ↓) | +0.22pp |

**发现**：Qwen constrained decoding 在 DR 消除上显著优于 Llama（98.7% vs 59.2% 相对消除率），同时 R_F1 保持中性。Qwen 的 constrained decoding 更彻底地执行了 domain-range 约束。

---
