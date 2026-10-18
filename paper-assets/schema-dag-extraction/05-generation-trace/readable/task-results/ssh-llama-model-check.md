# ssh llama model check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama-model-check_20260515T063112_result.json`
- **Structured JSON:** [`16835f382fcaae9ab671.json`](../../sessions/16/16835f382fcaae9ab671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**模型未缓存，且磁盘空间不足。**

| 项目 | 结果 |
|------|------|
| 模型缓存 | **NOT_CACHED** — HF cache 和 autodl-tmp 下均未找到任何 Llama-70B 相关目录 |
| 磁盘空间 | `/root/autodl-tmp/` 总计 250G，已用 219G，**剩余仅 32G** |
| FP8 70B 模型需求 | 约 **70-80GB** |
| 结论 | **空间不足，无法下载**。缺口约 40-50GB |

需要先清理磁盘腾出空间才能下载。可以检查一下 autodl-tmp 下哪些东西占空间大，看有没有可清理的。要查看吗？

---
