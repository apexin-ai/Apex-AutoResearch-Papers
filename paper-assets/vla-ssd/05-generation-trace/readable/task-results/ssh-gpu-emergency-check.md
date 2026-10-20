# ssh gpu emergency check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_emergency_check_20260521T201649_result.json`
- **Structured JSON:** [`bb43b64b6e9fa7ef0e4c.json`](../../sessions/bb/bb43b64b6e9fa7ef0e4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态：两个实验仍在运行，正常

**不是卡死**——Phase 4 (cross-instruction classification) 是 CPU 密集的 Ridge/SVM 分类，不用 GPU 计算，所以 GPU util = 0% 是预期行为。GPU 内存仍被占用（各 8630MiB）说明模型还在显存中，进程活跃。

### 当前进度

| 实验 | GPU | 当前阶段 | 进度 | 最后日志时间 | 预估剩余 |
|------|-----|----------|------|-------------|----------|
| tracvla_long_v1 | cuda:0 | Phase 4 cross-instr | L15/31 | 04:15:59 | ~16 min (Phase 4) + Phase 5 |
| tracvla_goal_v1 | cuda:1 | Phase 4 cross-instr | L19/31 | 04:15:26 | ~40 min (Phase 4, 越来越慢) + Phase 5 |

### 速度观察

- **tracvla_long_v1**: ~1 min/layer，较快
- **tracvla_goal_v1**: 从 ~3 min/layer 递增到 ~4 min/layer（L15→L19），后续层会更慢

### Phase 4 已出的中间结果

**tracvla_long_v1** (trained): 所有层 cross-instr accuracy = 1.000（img 和 last_pre 都是满分）

**tracvla_goal_v1** (trained): img 在 0.998-1.000，last_pre 从 L0=0.970 跳到 L1+ 全部 1.000

Phase 4 完成后还有 Phase 5 (counterfactual)，之后实验才算结束。无需干预，等待自然完成即可。

---
