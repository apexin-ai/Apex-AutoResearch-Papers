# infra accelerate download

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_accelerate-download_20260520T105656_result.json`
- **Structured JSON:** [`2c9395609e657a68dea3.json`](../../sessions/2c/2c9395609e657a68dea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘空间不足以下载 Qwen3-14B-Base（~29G），当前只剩 18G。**

可能可以清理的模型（需要你确认）：
| 模型 | 大小 | 备注 |
|------|------|------|
| `mistral-7b-v0.3` + `Mistral-7B-Instruct-v0.3` | 28G | 两个 Mistral 版本 |
| `Qwen/Qwen2___5-14B-Instruct` (ModelScope格式) | 28G | 可能与 `Qwen2.5-14B` (8.1G) 重复 |
| `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` | 28G | |
| `Llama-3.2-3B-Instruct-ms` | 12G | |

删除任意 ~11G 的模型即可释放足够空间。请告知哪些模型可以删除？

同时报告下载方案对比：
- **ModelScope SDK**: ~450 kB/s，预计 17h
- **aria2c + 代理 → xethub CDN**: 初始 8-10 MB/s，但连接不稳定，衰减到 ~376 kB/s
- **aria2c + hf-mirror（无代理）**: xethub CDN 重定向卡死，无法工作
- **推荐方案**: aria2c + 代理，一次下一个文件（集中带宽），预计 1-2h

---
