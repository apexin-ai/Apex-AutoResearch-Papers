# ops verify gpu split

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_gpu_split_20260519T045944_result.json`
- **Structured JSON:** [`127ea7c4c513f57e9c16.json`](../../sessions/12/127ea7c4c513f57e9c16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验确认正常运行：

**nvidia-smi:**
| GPU | PID | 显存 | GPU-Util |
|-----|-----|------|----------|
| cuda:0 | 776616 (temp09) | 32304 MiB | 97% |
| cuda:1 | 787051 (topk50) | 32302 MiB | 97% |

**topk50 日志头部确认：**
- `CUDA_VISIBLE_DEVICES=1` — 正确绑定 cuda:1
- 模型已加载完成（579/579 shards），正在生成 d0（5000 unconditional samples）
- 配置：Qwen2.5-14B FP16, top-k k=50, depths 0-3

两张卡各跑一个 14B 实验，互不干扰，GPU 利用率都在 97%。注意 topk50 的实际 PID 是 787051（不是预期的 787031，差异正常，可能是启动时的进程分配）。

---
