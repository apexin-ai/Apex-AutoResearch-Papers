# ops provenance phantom cleanup

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_provenance-phantom-cleanup_20260523T105406_result.json`
- **Structured JSON:** [`516ddb21ae82b7eab04d.json`](../../sessions/51/516ddb21ae82b7eab04d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All phantom IDs cleared. Here's the summary:

## 映射结果

| Phantom ID | Registry ID | 依据 | 出现位置 |
|---|---|---|---|
| `exp-005` | **`exp-002`** | C362 "cosine reward cannot separate" → exp-002 是 tanh gate cosine 公式，因 activation norms 100-1200x 导致 gate saturation | C355, C358, C362, C388, C397, C436 (5处) |
| `exp-006` | **`exp-002v2`** | C362 同上 → exp-002v2 是 pure cosine 公式，gap 仅 0.098 | C355, C358, C362, C397 (4处) |
| `exp-007` | **`exp-002v3`** | C358 "every formulation fails" 中第三个 cosine 变体 → exp-002v3 是 scaled cosine，R3 saturates at 0.9998 | C355, C358, C397 (3处) |
| `exp-002v2-recalib` | **`exp002v2-recalib`** | 命名不一致（多了一个连字符），registry 中为 `exp002v2-recalib` | C407, C449 (2处) |

共替换 14 处引用，0 个 phantom ID 残留。

---
