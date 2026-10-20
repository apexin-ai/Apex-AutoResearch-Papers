# code accelerate llama download

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_accelerate-llama-download_20260514T054935_result.json`
- **Structured JSON:** [`ec736ea308d26d16da49.json`](../../sessions/ec/ec736ea308d26d16da49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载完成，验证通过。

**结果汇总：**

| 项目 | 内容 |
|------|------|
| 成功方案 | 方案 4 — ModelScope 后台下载（已在跑的进程） |
| 下载速度 | 平均 5-8 MB/s/shard（3 shard 并行），峰值 17 MB/s（单 shard 独占带宽时） |
| 总耗时 | ~14 分钟（从日志 0:00 到 14:14） |
| 模型路径 | `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct` |
| 验证 | layers=32, dim=4096, vocab=128000, `LLAMA_VERIFY_OK` |

方案 1（共享目录）不可用 — `/root/autodl-pub/` 只有 CV 数据集，无 LLM 模型。方案 2/3 未启动，因 ModelScope 已在跑且速度足够，启动竞争下载会互相抢带宽。

---
