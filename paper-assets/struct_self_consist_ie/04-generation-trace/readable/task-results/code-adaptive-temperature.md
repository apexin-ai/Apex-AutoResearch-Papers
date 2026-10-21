# code adaptive temperature

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_adaptive_temperature_20260518T173330_result.json`
- **Structured JSON:** [`7adc67760ac6c637aa78.json`](../../sessions/7a/7adc67760ac6c637aa78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Adaptive Temperature Protocol — Results

| Dataset | Degen@T1.0 | Switch? | Greedy F1 | LP@AdaptT | Delta (pp) | 95% CI |
|---------|-----------|---------|-----------|-----------|-----------|--------|
| SciERC | 11.7% | no | 0.6442 | 0.6468 | +0.26 | [-1.13, +1.65] NS |
| CoNLL2003 | 60.6% | **YES** | 0.9077 | 0.8976 | **-1.01** | [-1.49, -0.55] ** |
| FewNERD | 9.4% | no | 0.7480 | 0.7624 | **+1.44** | [+1.26, +1.61] ** |

**核心发现：假说被 CoNLL 反驳。** CoNLL 是唯一触发切换的数据集（degeneracy 60.6% > 30%），T=1.2 确实降低了 degeneracy（60.6% → 49.6%，降 11pp），但 LP selection@T=1.2 反而比 greedy@T=1.0 差 1.01pp，CI 完全为负。

对比之下，FewNERD 在 T=1.0 天然低 degeneracy（9.4%）下 LP selection 就能获得显著 +1.44pp 增益。说明 LP selection 有效的前提是模型本身采样质量好（自然多样性），而不是靠升温强行多样化。

- JSON 结果：`output/adaptive_temperature_results.json`
- 报告已注册：`art_20260518_188ce3`
- FewNERD T=1.2 推理仍在进行（~6.6%，预计还需 ~1.5h），但不影响 adaptive protocol 结论（degeneracy 9.4% < 30%，保持 T=1.0）

---
