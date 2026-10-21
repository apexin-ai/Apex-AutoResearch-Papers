# check exp026 and qwen3 status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp026-and-qwen3-status_20260518T125438_result.json`
- **Structured JSON:** [`c06789f5fe47d69bdab8.json`](../../sessions/c0/c06789f5fe47d69bdab8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 任务 1: FOLIO trace 重生成 (PID 27245)
- **进程**: 运行中 (sleeping)
- **进度**: **124/204** (~61%)，相比之前的 53/204 有明显推进
- **结果文件**: 存在，87810 bytes，2406 行，最后修改 20:54
- **日志**: 仅 42 行（脚本日志极少，进度主要体现在 results JSON 增量写入）

### 任务 2: Qwen3-14B 下载 (PID 29779)
- **进程**: 运行中 (sleeping)
- **已下载**: 11G
- **状态**: 8 个 safetensors 分片全在 `._____temp/` 临时目录中（~7.4G），尚未移出 = 下载/校验进行中
- config.json、merges.txt 等小文件已就位

### 额外检查
- **LLaMA-8B 下载 (PID 17783)**: 运行中
- **磁盘**:
  - `/root`: 12G/30G (38%)
  - `/root/autodl-tmp`: 153G/250G (61%)，空间充足
- **GPU**: 4× RTX PRO 6000 Blackwell (98GB each)
  - GPU 0: 88GB/98GB, 97% util — vLLM 引擎 (PID 23449) 服务 FOLIO 推理
  - GPU 1-2: 空闲
  - GPU 3: 0GB 显存但 100% util（可能是短暂计算任务）

---
