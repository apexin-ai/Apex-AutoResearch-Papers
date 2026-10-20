# infra gpu status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260515T213424_result.json`
- **Structured JSON:** [`5b037e3fa5b717f2e7b9.json`](../../sessions/5b/5b037e3fa5b717f2e7b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报

**无 GPU 碰撞，两个实验分别占用不同 GPU。**

| GPU | 进程 | PID | 显存占用 | 温度 | 功耗 | 利用率 |
|-----|------|-----|---------|------|------|--------|
| cuda:0 | `deepseek_exception_only_seed456` | 160932 | 22,414 / 97,887 MiB | 72°C | 467W | 100% |
| cuda:1 | `deepseek_full_trace_seed42_v3` | 163109 | 22,386 / 97,887 MiB | 75°C | 488W | 100% |

**进程状态：** 两个 PID 都在运行，CPU 占用均 ~100%。

**GPU 分配细节：**
- PID 160932 启动时设了 `CUDA_VISIBLE_DEVICES=0` → 物理 GPU 0
- PID 163109 启动时设了 `CUDA_VISIBLE_DEVICES=1` → 物理 GPU 1（代码里 `--gpu 0` 指的是可见设备中的第 0 个，即物理 GPU 1）

**cuda:1 不空闲**，正被 full_trace_v3 占用。两张卡都在满负荷训练。

---
