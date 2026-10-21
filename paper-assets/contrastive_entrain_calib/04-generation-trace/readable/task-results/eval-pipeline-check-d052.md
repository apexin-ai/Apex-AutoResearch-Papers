# eval pipeline check d052

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_pipeline-check-d052_20260522T102217_result.json`
- **Structured JSON:** [`03d1960637fc17b6ad83.json`](../../sessions/03/03d1960637fc17b6ad83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

28034 所有 eval 已完成，GPU 全部空闲。

## 结果汇总

**ACT seed 2 (exp-004-s2) trajectory:**

| Checkpoint | SYCONScore | vs vanilla (+%) |
|-----------|-----------|-----------------|
| ckpt-500  | 0.223 | +67% |
| ckpt-1000 | **0.256** | +91% |
| ckpt-1500 | 0.214 | +60% |
| ckpt-2000 | 0.214 | +60% |

Peak at ckpt-1000，然后 plateau 在 ~0.214。对比 seed 1 peak 在 ckpt-2000 (0.255)，seed 2 peak 更早但幅度相似。

**R3-only seed 2 ckpt-7000:** SYCONScore = 0.095 (低于 vanilla 0.134)

## Registry 更新
- `exp-004-s2-eval-ckpt2000`: RUNNING → DONE (metrics + conclusion=success)
- 其余 eval（ckpt-500/1000/1500, R3-only s2 ckpt-7000）已经是 DONE

---
