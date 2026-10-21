# infra redownload models w19

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_redownload_models_w19_20260518T180110_result.json`
- **Structured JSON:** [`a0cc99cb27423b9f9672.json`](../../sessions/a0/a0cc99cb27423b9f9672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：两个模型之前已完整下载，无需重新下载。**

| 模型 | 目录大小 | 权重文件 | 验证结果 |
|---|---|---|---|
| Gemma 4 E2B | 9.6G | `model.safetensors` (9.5GB) | Config 加载成功：text hidden=1536, 35 layers, vocab=262144。多模态模型 (Gemma4ForConditionalGeneration) |
| Qwen3.5-0.8B-Base | 1.7G | `model.safetensors-00001-of-00001.safetensors` (1.6GB) | 模型加载+forward pass 成功：0.75B params, vocab=248044 |

磁盘剩余：76G 可用 (250G 总, 175G 已用)。

safetensors 文件头包含真实张量 metadata，确认是完整权重而非 LFS 指针或空壳。

---
