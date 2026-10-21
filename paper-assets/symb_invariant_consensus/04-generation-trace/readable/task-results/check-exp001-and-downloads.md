# check exp001 and downloads

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp001-and-downloads_20260516T182527_result.json`
- **Structured JSON:** [`0dfb62e1386b7467c7d6.json`](../../sessions/0d/0dfb62e1386b7467c7d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

## exp-001 进度

| 指标 | 值 |
|------|-----|
| PID | 181491 ✅ 存活 |
| 运行时间 | 13h 10m |
| ProofWriter | **600/600** ✅ 完成 |
| FOLIO | **159/204** 进行中 |
| 总进度 | **759/804 (94.4%)** |
| ETA | ~45 题剩余，按当前速率约 1-2h 完成 |

## 模型下载状态

| 模型 | 状态 | 路径 | 备注 |
|------|------|------|------|
| **Mistral-7B-Instruct-v0.3** | ✅ 完整 | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/mistralai/Mistral-7B-Instruct-v0___3` | 3 shards (11GB), vocab=32768, tokenizer OK. 有一个空 `._____temp` 目录（无害） |
| **LLaMA-3.1-8B-Instruct** | ✅ 完整 | `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct` | 4 shards (14GB), vocab=128000, tokenizer OK, 无 temp 文件 |
| **DeepSeek-R1-Distill-LLaMA-8B** | ✅ 完整 | `/root/autodl-tmp/models/DeepSeek-R1-Distill-Llama-8B/` | 2 shards (15GB) |

## vLLM 脚本

`scripts/start_vllm_mistral_7b.sh` ✅ 已存在，路径正确，端口 8001，配置合理。

---
