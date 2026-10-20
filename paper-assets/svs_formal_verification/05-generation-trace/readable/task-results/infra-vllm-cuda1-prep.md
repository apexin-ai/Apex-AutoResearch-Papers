# infra vllm cuda1 prep

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_vllm_cuda1_prep_20260514T070433_result.json`
- **Structured JSON:** [`bb9b207acd602851e879.json`](../../sessions/bb/bb9b207acd602851e879.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**异常：无法在 cuda:1 上启动第二个实例。**

当前 cuda:0 上的 vLLM 使用了 `--tensor-parallel-size 2`，横跨 GPU 0 和 GPU 1（两块卡各占 ~30GB）。cuda:1 已被占满，无法再启动新实例。

当前状态：
- **Port 8001**: 正常运行，FP16 + tensor-parallel-size 2，使用 GPU 0+1
- **Port 8002**: 未运行
- **GPU 2, 3**: 空闲（0 MiB）
- **MVP dry run** (PID 15710) 正在执行中

可选方案：
1. **在 GPU 2 上启动第二个实例**（`CUDA_VISIBLE_DEVICES=2`，port 8002）— 不影响现有服务
2. **重启 port 8001 为 TP=1（仅 GPU 0）**，然后在 GPU 1 上启动第二个 — 但会中断正在跑的 MVP dry run
3. **维持现状** — TP=2 的单实例性能更好，等 MVP 跑完再决定

建议方案 1，最安全。需要哪个？

---
