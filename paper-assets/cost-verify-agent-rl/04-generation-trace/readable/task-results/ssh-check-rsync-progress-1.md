# ssh check rsync progress 1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_rsync_progress_1_20260523T043403_result.json`
- **Structured JSON:** [`6387adcd5959e60ce417.json`](../../sessions/63/6387adcd5959e60ce417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## rsync 迁移进度汇总

### 进程状态

| PID | 任务 | 状态 | 运行时长 |
|-----|------|------|----------|
| 372901 | code | **已完成** ✓ | — |
| 372903 | alfworld | **已完成** ✓ | — |
| 372886 | checkpoints | **运行中** | 2h 26m |
| 372894 | models | **运行中** | 2h 22m |

### bjb1 已接收数据量 vs westd 源数据量

| 目录 | bjb1 已接收 | westd 源总量 | 进度 |
|------|------------|-------------|------|
| cost-verify-agent-rl (code) | 629M | — | **完成** |
| alfworld | 2.2G | — | **完成** |
| checkpoints | 962M | 109G | **~0.9%** |
| models | 1.1G | 20G | **~5.5%** |

### 日志末尾

- **code**: 正常结束，`total size is 650MB, speedup 4.01`
- **alfworld**: 正常结束，`total size is 2.3GB, speedup 9.34`
- **checkpoints**: 正在传 `exp029-seed100/global_step_10/actor/` 的 FSDP 分片文件
- **models**: 正在传 `Qwen3-1.7B` 的 safetensors 文件

### 结论

两个大目录（checkpoints 109G、models 20G）传输才刚开始，按当前速度预计还需较长时间。已完成的 code 和 alfworld 日志无 error。

---
