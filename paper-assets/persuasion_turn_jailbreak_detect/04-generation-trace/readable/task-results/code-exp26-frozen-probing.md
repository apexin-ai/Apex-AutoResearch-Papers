# code exp26 frozen probing

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp26-frozen-probing_20260520T144105_result.json`
- **Structured JSON:** [`3b0922ca45c7dc5c9c65.json`](../../sessions/3b/3b0922ca45c7dc5c9c65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp26 完成。结果摘要：

**Frozen Probing (mean ± std, 3 seeds)**

| Metric | Frozen Probing | E2E (exp18) |
|--------|---------------|-------------|
| IID | 1.000 ± 0.000 | 1.000 |
| DD OOD k1 | 0.990 ± 0.013 | — |
| DD OOD k2 | 0.981 ± 0.013 | — |
| DD OOD k3 | 0.972 ± 0.026 | — |
| DD OOD k5 | 0.997 ± 0.005 | — |
| DD OOD full | 0.997 ± 0.005 | 1.000 |
| AA OOD full | 0.972 ± 0.026 | 0.997 |
| FITD OOD full | 1.000 ± 0.000 | — |

冻结 DAPT encoder + 随机初始化 BiGRU 即可达到接近 e2e 微调的 OOD 泛化性能。AA OOD 上有 ~2.5pp 差距，但在方差范围内。DAPT representation quality alone 足以携带跨攻击类型的泛化信号。

---
