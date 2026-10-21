# ops check running status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-status_20260514T212958_result.json`
- **Structured JSON:** [`73d23fb5271f9ae6c109.json`](../../sessions/73/73d23fb5271f9ae6c109.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验存活状态

### alpha_sweep_a000_s42 (cuda:0)
- **存活** — PID 46716（wrapper）和 46721（python）均在运行
- 运行时长：**2h 28m 39s**
- 参数：`--synthetic_ratio 0.0 --seed 42 --steps_per_gen 5000 --num_generations 10`

### alpha_sweep_a025_s42_v3 (cuda:1)
- **存活** — PID 53069（wrapper）和 53074（python）均在运行
- 运行时长：**26m 12s**
- 参数：`--synthetic_ratio 0.25 --seed 42 --steps_per_gen 5000 --num_generations 10`

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 42% | 14,391 MiB |
| 1 | 61% | 12,753 MiB |

两个实验均正常运行，GPU 活跃且显存占用合理，无异常。

---
