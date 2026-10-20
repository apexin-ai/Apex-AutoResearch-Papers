# ssh b2 v2 multi domain joint

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_b2-v2-multi-domain-joint_20260520T113822_result.json`
- **Structured JSON:** [`7f124a446ba5ca04c953.json`](../../sessions/7f/7f124a446ba5ca04c953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。所有产出在 `artifacts/b2_v2_multi_domain/`。

## 核心结果

| Fold | Test Dataset | LGB AUC | ECE | F1 Δ vs Greedy |
|------|-------------|---------|-----|----------------|
| 1 | CoNLL | 0.9378 | 0.030 | +0.003 |
| 2 | SciERC | 0.8006 | 0.127 | +0.005 |
| 3 | **FewNERD** | **0.8477** | 0.136 | **-0.008** |
| 4 | IID (upper bound) | 0.9313 | 0.007 | — |

## vs B2 Original (Fold 3)

- LGB AUC: 0.8335 → **0.8477 (+0.014)**, XGB: 0.8282 → **0.8603 (+0.032)**
- 但 **F1 delta 仍为负** (-0.008)，AUC 提升未转化为下游收益
- 原因：cross-domain ECE=0.136（IID 仅 0.007），预测概率严重 miscalibrated

## Feature 稳定性核心发现

- **最具判别力的 feature (agreement_count, vc, sj) 跨域稳定性最差** (std=0.12-0.14)
- **最稳定的 feature (lp_span, lp_token)** 判别力中等 (r≈0.26-0.34, std≈0.01)
- dataset_enc 在 Fold 3 占 XGB gain 的 9.4%，模型依赖数据集身份——跨域泛化的隐患

## 结论

Joint training 提升了 AUC，但 cross-domain calibration gap 未解决。verifier-weighted construction 在 FewNERD 上仍然是负迁移。需要 domain-specific calibration 或设计同时具备判别力和跨域稳定性的 feature。

---
