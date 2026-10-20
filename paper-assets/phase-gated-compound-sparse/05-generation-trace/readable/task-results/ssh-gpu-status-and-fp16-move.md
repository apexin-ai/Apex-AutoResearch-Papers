# ssh gpu status and fp16 move

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-status-and-fp16-move_20260514T054813_result.json`
- **Structured JSON:** [`b3ee18be099709ac6d36.json`](../../sessions/b3/b3ee18be099709ac6d36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. v6_random_s030_r2 状态

**异常终止**，不是预期的 EXIT_CODE=127 快速失败。日志显示它实际运行了 21/50 个问题（13:37–13:43），然后进程消失，**无 exit 文件**。推测 bash/sh 不兼容导致 exit trap 未正确注册，进程终止时没有记录退出码。已被 r3 替代，无需处理。

### 2. GPU 当前状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 0 MiB / 98 GB | 0% | **空闲** |
| 1 | 0 MiB / 98 GB | 0% | **空闲** |
| 2 | 26 GB / 98 GB | 73% | v6_random_s030_r3 (26/50) |
| 3 | 32 GB / 98 GB | 100% | v6_random_s025 (48/50, 即将完成) |

### 3. 已完成的 v6_random 实验

- **v6_random_s015**: EXIT_CODE=0 ✓
- **v6_random_s020**: EXIT_CODE=0 ✓
- **v6_random_s030 (r1)**: EXIT_CODE=143 (SIGTERM, 被 kill 替换)
- **v6_random_s025**: 运行中 48/50, 几分钟内完成
- **v6_random_s030_r3**: 运行中 26/50, 预计还需 ~15-20 分钟

### 4. fp16 结果移动

**暂不执行。** s025 和 s030_r3 仍在写入输出目录，需等这两个实验完成后再移动。

### 5. bf16 Batch 1 Ready?

**部分 ready。** GPU 0 和 GPU 1 立即可用，可先启动 2 个 bf16 实验。GPU 2/3 需等当前 fp16 实验完成（预计 ~20 分钟内全部空闲）。

---
