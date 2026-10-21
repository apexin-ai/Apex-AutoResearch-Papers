# verify seed6 v3 gpu isolation

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_seed6_v3_gpu_isolation_20260521T081226_result.json`
- **Structured JSON:** [`91c20b4d415052e26eb9.json`](../../sessions/91/91c20b4d415052e26eb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 隔离验证结果：有严重问题。**

### 关键发现：CUDA_VISIBLE_DEVICES 配置错误

Seed 6 v3 的配置中 `CUDA_VISIBLE_DEVICES` 设为 **`0,1`** 而非预期的 **`2,3`**：

```
'system': {'CUDA_VISIBLE_DEVICES': '0,1'}
```

日志也确认输出：`CUDA_VISIBLE_DEVICES: 0,1`

### 当前 GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 37,655 MiB / 97,887 MiB | 100% | Seed 5 (PID 886568) |
| 1 | 38,211 MiB / 97,887 MiB | 100% | Seed 5 (PID 886569) |
| 2 | 3 MiB / 97,887 MiB | 0% | 无 |
| 3 | 3 MiB / 97,887 MiB | 0% | 无 |

### 详细判定

- **GPU 2,3 未被 Seed 6 占用** — 空闲状态，因为 Seed 6 还在 Ray 初始化阶段（TaskRunner pid=895770 刚输出 config dump）
- **GPU 0,1 上 Seed 5 目前正常** — 但 Seed 6 一旦开始加载模型，将尝试占用 GPU 0,1，与 Seed 5 **直接冲突**
- **save_freq=5** — 确认正确
- **CUDA_VISIBLE_DEVICES=0,1** — **错误**，应为 `2,3`
- **无 runtime error** — 目前只有初始化阶段的 warnings（tokenizer regex、Ray docker CPU、hydra defaults_list），均为非关键

### 结论

**Seed 6 v3 必须立即停止。** 配置文件中 `CUDA_VISIBLE_DEVICES` 写错了 `0,1`，如果继续运行，模型加载后将挤占 Seed 5 的 GPU 0,1，导致两个实验同时崩溃。需要修正配置为 `2,3` 后重新启动。

---
