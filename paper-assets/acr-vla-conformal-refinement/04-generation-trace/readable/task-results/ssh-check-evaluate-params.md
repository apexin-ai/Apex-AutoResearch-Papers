# ssh check evaluate params

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-evaluate-params_20260520T071903_result.json`
- **Structured JSON:** [`b97d2558fb3eaf7fcc89.json`](../../sessions/b9/b97d2558fb3eaf7fcc89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
--adaptive_threshold vs --threshold: 不等价 — 不存在 --threshold 参数。只有 --adaptive_threshold（default=0.1）。传 --threshold 会报错 unrecognized arguments。

--k_full vs --K: 不等价 — 两个独立的 add_argument，含义不同。
  - --K (default=10): 主采样数，用于非 adaptive 模式
  - --k_full (default=5): adaptive K 模式下扩展时的采样数
  传 --k_full 不会影响 --K，反之亦然。用错参数名不会报错，但会静默使用默认值（这比报错更危险）。
```

---
