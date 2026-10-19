# infra p2b gpu check restart

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_p2b_gpu_check_restart_20260512T144458_result.json`
- **Structured JSON:** [`bcc6d12c211d09ba7e36.json`](../../sessions/bc/bcc6d12c211d09ba7e36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态报告

| 项目 | 状态 |
|------|------|
| PID 132149 | **存活** — wrapper 进程正常 |
| GPU 4 | **在用** — PID 132163 占用 8152 MiB |
| 模型文件 | **完整** — 2 个 safetensors (4.96GB + 1.21GB) |
| 根分区 | 12G/30G (39%) |
| 数据盘 | 110G/169G (65%) |

### 训练进度（9 runs: 3 策略 × 3 seed）

| Run | 状态 | 备注 |
|-----|------|------|
| 1/9 `p2b_random_s42` | **完成** | checkpoints 200/400/600/final 齐全 |
| 2/9 `p2b_random_s123` | **进行中** | checkpoints 200/400/600 已写入，等待 final |
| 3-9 | 待执行 | |

### 结论

**GPU 4 不空闲，训练正常进行中。** 脚本 skip 逻辑正常工作（跳过了已完成的 run 1）。当前 run 2 已到 step 600，预计很快完成并自动进入 run 3。

Registry 中 `mvp_p2b_contrastive_training` 显示 DONE/failed 是旧状态，但状态机不允许 DONE→RUNNING 回退，无法更新。实际进程正常运行，无需干预。

---
