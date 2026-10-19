# eval sft baseline ood v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_sft_baseline_ood_v2_20260521T115503_result.json`
- **Structured JSON:** [`aad7e9261e9831b844cd.json`](../../sessions/aa/aad7e9261e9831b844cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已确认正在运行！GPU 利用率更新：

| GPU | 内存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 45441/97887 MiB | 100% | 训练（不变） |
| **1** | **53204/97887 MiB** | **100%** | **训练 + eval 共存** |
| 2 | 91475/97887 MiB | 100% | 训练（不变） |
| 3 | 91475/97887 MiB | 100% | 训练（不变） |

**执行总结：**

1. **服务器**: westd-47453, **GPU 1**（与训练共享，eval 仅占 ~8.7GB）
2. **PID**: 189083 (bash) → 195885 (TaskRunner) → 196655 (WorkerDict)
3. **WandB**: run `sft-1.7b-baseline-ood-eval` / ID `oa90j1t0`
4. **训练影响**: 无。GPU 0/2/3 内存完全不变，GPU 1 新增 8.7GB（总 53.2/97.9GB，余量 44.7GB）
5. **配置**: `gpu_memory_utilization=0.10`, 单 GPU, 134 OOD tasks, τ=0.4

日志缓冲正常 — ALFWorld 多轮 rollout 输出在 Ray worker 中，首批结果出来后会刷新到日志。134 个 task 预计需要 30-60 分钟完成。

---
