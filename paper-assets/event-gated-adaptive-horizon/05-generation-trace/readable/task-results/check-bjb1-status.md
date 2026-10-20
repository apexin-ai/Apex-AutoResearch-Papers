# check bjb1 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1_status_20260525T193155_result.json`
- **Structured JSON:** [`a2b527ab2bfb0e37febc.json`](../../sessions/a2/a2b527ab2bfb0e37febc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 实验 | 状态 | 最终 step | eval_return@105k | best eval | CIVO onset |
|------|------|-----------|-----------------|-----------|------------|
| exp_084 (s0) | **COMPLETED** | 112k | 281.48 | 334.06@95k | 无 |
| exp_085 (s1) | **COMPLETED** | 69.26 | 69.26 | 281.53@65k | 无 |

两个实验均已正常完成，进程退出，GPU 空闲。两者 gate 均 100% 锁定在 dt=2（frozen embedding 预期行为），无 CIVO alert。

s0 表现显著优于 s1（281 vs 69），与 trained dt_emb 下的 seed 间方差模式一致，但两者均无 value explosion — 再次确认 frozen dt_emb 是 CIVO 的有效消融控制。

状态已追加到 memory.md。

---
