# ssh v71 probe a step20k dual

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v71-probe-a-step20k-dual_20260517T095759_result.json`
- **Structured JSON:** [`82778965fbbe03f9116c.json`](../../sessions/82/82778965fbbe03f9116c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Seed1 — Probe A (step 20000)
| Pair | Cosine |
|------|--------|
| inst 0 vs 1 | 0.8517 |
| inst 0 vs 2 | 0.8656 |
| inst 1 vs 2 | 0.9368 |

### Seed2 — Probe A (step 20000)
| Pair | Cosine |
|------|--------|
| inst 0 vs 1 | 0.6098 |
| inst 0 vs 2 | 0.4920 |
| inst 1 vs 2 | 0.9438 |

### 判定

- **Seed1: FAIL** — 所有 3 pairs cos > 0.8 (0.85, 0.87, 0.94)，scorer 对 language condition 有依赖但区分度不足
- **Seed2: PASS** — 2/3 pairs cos < 0.8 (0.61, 0.49)，说明 scorer 明显区分不同 instruction

注意 seed2 的 pair (1 vs 2) 极高 (0.94)，但这两条 instruction 语义本就相似（都是 "pick up the black bowl ... place it on the plate"），所以高 cosine 合理。

**总结**：Seed2 通过，Seed1 不通过。两个 seed 表现不一致——seed2 的 scorer 学到了更强的语言条件依赖。

---
