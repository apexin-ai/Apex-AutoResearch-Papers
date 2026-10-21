# analyze grasp baseline westd final

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grasp_baseline_westd_final_20260515T151132_result.json`
- **Structured JSON:** [`5025d2270516f0136b77.json`](../../sessions/50/5025d2270516f0136b77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行，尚未完成。**

| 项目 | 状态 |
|------|------|
| PID 38120 | **运行中** (Rl, elapsed 01:21:08) |
| 进度 | **56/100** (~56%) |
| 50-sample 中间 accuracy | **6.00%** (3/50) |
| 50-sample eos_rate | 2.00% |
| 50-sample avg_len | 4018 |
| JSON 结果文件 | 尚未生成 |

中间指标比之前看到的 8% (51 samples) 略降到 6% (50-sample checkpoint)。按当前速度 (~51s/it)，剩余 44 samples 预计还需 ~37 分钟完成。

GraSP baseline 的 post-prune accuracy 预计会远低于 RASP (31%) 和 Standard (27%)，进一步验证了 recovery-aware 方法的优势。需要等完成后再读取最终结果。

---
