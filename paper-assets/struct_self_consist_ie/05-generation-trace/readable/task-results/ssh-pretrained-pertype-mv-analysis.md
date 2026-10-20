# ssh pretrained pertype mv analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_pretrained_pertype_mv_analysis_20260521T215145_result.json`
- **Structured JSON:** [`20a4f8ce853797006136.json`](../../sessions/20/20a4f8ce853797006136.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pretrained FewNERD Per-Type MV Analysis (θ=0.5 strict)

### 3-seed average
| Entity Type | n_inst | greedy_f1 | MV F1 | MV Δ (pp) |
|-------------|--------|-----------|-------|-----------|
| person | 8,016 | 0.6374±0.0003 | 0.6792±0.0046 | **+4.17±0.43** |
| organization | 6,647 | 0.5247±0.0007 | 0.5562±0.0059 | **+3.15±0.54** |
| location | 8,023 | 0.5650±0.0008 | 0.5898±0.0007 | **+2.47±0.01** |
| event | 1,306 | 0.4277±0.0008 | 0.4510±0.0021 | **+2.34±0.28** |
| building | 1,587 | 0.4379±0.0017 | 0.4577±0.0021 | **+1.98±0.04** |
| product | 2,276 | 0.4932±0.0017 | 0.5110±0.0008 | **+1.78±0.24** |
| art | 1,277 | 0.4224±0.0009 | 0.4297±0.0073 | **+0.73±0.70** |
| other | 3,433 | 0.3761±0.0014 | 0.3717±0.0029 | −0.45±0.32 |

Pearson r(greedy_f1, MV_delta): **r=0.8620, p=0.0059**

### Pretrained vs Finetuned 对比
| Entity Type | Pretrained MV Δ | Finetuned MV Δ | Direction |
|-------------|----------------|----------------|-----------|
| person | +4.17pp | −0.67pp | **FLIP** |
| organization | +3.15pp | −2.65pp | **FLIP** |
| location | +2.47pp | −1.52pp | **FLIP** |
| event | +2.34pp | −3.17pp | **FLIP** |
| building | +1.98pp | −3.90pp | **FLIP** |
| product | +1.78pp | −3.38pp | **FLIP** |
| art | +0.73pp | −1.51pp | **FLIP** |
| other | −0.45pp | −3.02pp | SAME |

**7/8 types flip**: pretrained MV positive (SC helps), finetuned MV negative (SC hurts). Only "other"（异质性最高的 catch-all 类别，greedy F1 最低）在两种设定下均为负。Pretrained 中 greedy F1 越高的 type 从 MV 中获益越多（r=0.86），说明 SC 放大了模型已有能力。

Finetuned reference (θ=0.5, exp_021 seed=42):
person: −0.67pp, art: −1.51pp, location: −1.52pp, organization: −2.65pp,
other: −3.02pp, event: −3.17pp, product: −3.38pp, building: −3.90pp

JSON 已保存至 `autodl-5090:output/pretrained_fewnerd_per_type_mv_analysis.json`，artifact 写入 `artifacts/pretrained_fewnerd_per_type_mv_analysis.md`。

---
