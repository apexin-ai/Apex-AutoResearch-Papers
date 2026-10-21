# infra qwen completion shards

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_qwen_completion_shards_20260521T022059_result.json`
- **Structured JSON:** [`e5f656e3c40c257981e1.json`](../../sessions/e5/e5f656e3c40c257981e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态汇报：**

- **Qwen download: 进行中** — 15GB / ~15.3GB (总 5 个 shard)
  - shard 1-4: 已完成 (3.8G + 3.8G + 3.7G + 3.0G)
  - shard 5 (model-00005-of-00005.safetensors): **74% (882M/1.16G)**，速度 ~480 kB/s，预计剩余 **~10 分钟**
- **Model validation**: 待下载完成
- **Qwen shards**: 待生成

注意：当前有两个下载进程同时在跑（HF hub PID 63161 + ModelScope PID 70309），均在下载 shard 5。不干预，等待完成。

---
