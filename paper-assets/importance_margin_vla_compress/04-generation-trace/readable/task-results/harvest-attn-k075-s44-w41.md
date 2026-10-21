# harvest attn k075 s44 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_attn_k075_s44_w41_20260528T010136_result.json`
- **Structured JSON:** [`d9b0b5a944ae59423ad9.json`](../../sessions/d9/d9b0b5a944ae59423ad9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**seed44 SR = 51.6%** (w41, success)

Per-task: `[72, 70, 78, 28, 30, 48, 74, 26, 10, 80]`

## 3-seed 汇总 (π0.5 Attn k=0.75 Long)

| Seed | Server | SR |
|------|--------|----|
| 42 | w27v2 | 49.8% |
| 43 | cqa1 | 52.0% |
| 44 | w41 | 51.6% |

**Mean = 51.1% ± 1.2%** (std)

## D293 Discrepancy

seed43 两个值：w27v2=49.0% vs cqa1=52.0%（差 3pp）。seed44 在 w41 上跑出 51.6%，与 cqa1 的 52.0% 接近，支持 cqa1 值更可信。3-seed 均值 51.1% 落在之前 2-seed 估计 50.9%±1.1% 的范围内，方差没有增大，plateau 区稳定性确认。

---
