# analysis verify ced s43 s45 r3 startup

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_ced_s43_s45_r3_startup_20260516T002137_result.json`
- **Structured JSON:** [`3b46c1f913c049c2fdcf.json`](../../sessions/3b/3b46c1f913c049c2fdcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：s43 通过，s45 失败（OOM）。**

### s43 (PID 277310, cuda:1) — 正常运行
- [x] PID 存活，运行 00:46，子进程 277315 占用 GPU 30204 MiB
- [x] data_path = rsft_filtered/rsft_train.jsonl
- [x] data_count = 2718
- [x] weighted_sampling=True
- [x] 已到 step 4/510，输出目录有 checkpoint-50
- [x] 无错误

### s45 (PID 277407, cuda:2) — 已崩溃
- **进程已死**（ps 未返回 277407）
- **原因**：`CUDA error: out of memory` — 模型加载阶段 OOM
- **根因**：cuda:2 被 PID 276148 占用 31628 MiB，s45 无法分配显存
- EXIT_CODE=1

这又是 C001 约束场景：cuda:2 在提交时已被占用。需要等 276148 结束释放 cuda:2 后重新提交 s45，或改用空闲 GPU。

当前 GPU 占用：
| GPU | PID | 显存 |
|-----|-----|------|
| GPU-0 | 270467 | 10846 MiB |
| GPU-1 | 277315 (s43) | 30204 MiB |
| GPU-2 | 276148 | 31628 MiB |
| GPU-3 | 272169 | 10850 MiB |

四卡全部被占用，暂无空闲 GPU 可用。需等待 GPU-0/2/3 上任一进程结束后重提 s45。

---
