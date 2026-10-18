# ops oft kill cqa1 check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_oft-kill-cqa1-check_20260520T131035_result.json`
- **Structured JSON:** [`833de8d6fe24484e18ae.json`](../../sessions/83/833de8d6fe24484e18ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

### 1. westd-41074 GPU 0/1 释放情况

**GPU 0 和 GPU 1 已成功释放。** 三个 OFT 进程（434280, 418851, 418848）已全部被 kill，ps 确认不存在。nvidia-smi 现在只剩 GPU 2/3 上的进程：
- GPU 2: PID 68539, 28546 MiB
- GPU 3: PID 68852, 27526 MiB

### 2. cqa1-33015 GPU 状态

只有 2 个 GPU 在使用：
- GPU 0 (a2a1...): PID 868193, 4197 MiB — 跑 X-VLA seed43 eval
- GPU 1 (c242...): PID 894197, 4521 MiB — 跑 X-VLA seed43 eval
- GPU 2/3: 空闲

### 3. OFT CV 计算

**已崩溃。** 报错：`RuntimeError: expected mat1 and mat2 to have the same dtype, but got: float != c10::BFloat16`（发生在 LLaMA attention 的 q_proj linear layer）。dtype 不匹配问题，需要修复。

### 4. X-VLA seed43 三个 k 值进度

| k 值 | 状态 | SR | 详情 |
|------|------|----|------|
| **k=0.9** | **完成** | **97.6%** (488/500) | Wilson CI 95%: [95.9%, 98.6%]，45/50 vision tokens 保留 |
| **k=0.7** | 运行中 | 当前 task 全 FAIL | Ep 30/50，连续 FAIL，steps=800 超时 |
| **k=0.5** | 运行中 | 当前 task 全 FAIL | Ep 40/50，连续 FAIL，steps=800 超时 |

### 5. Eval Results JSON

仅 k=0.9 有结果文件（`xvla_prune_k0.9_libero_object_seed43.json`）：
- 整体 SR = **97.6%**
- per-task SR 范围：92%–100%
- 最低：tomato sauce 92%, alphabet soup 94%
- 6 个 task 达到 96%+，4 个 task 达到 100%

k=0.7 和 k=0.5 从当前日志看表现很差，大量连续 FAIL，最终 SR 预计会很低。

---
