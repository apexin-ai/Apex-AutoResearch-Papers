# infra download 69b westd17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download_69b_westd17855_20260518T173736_result.json`
- **Structured JSON:** [`590023c9df61b5310443.json`](../../sessions/59/590023c9df61b5310443.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载完成。结果汇总：

**westd-17855 上 Pythia-6.9B 缓存状态：**

| 项目 | 状态 |
|------|------|
| 缓存路径 | `/root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-6.9b/` |
| 总大小 | **13G**（safetensors 格式，不含冗余 .bin） |
| model-00001-of-00002.safetensors | 9.3G ✓ |
| model-00002-of-00002.safetensors | 3.7G ✓ |
| config.json / tokenizer / index | ✓ |
| Config 验证 | hidden_size=4096, num_layers=32 ✓ |
| pytorch .bin 文件 | 未下载（冗余，safetensors 优先） |

模型已缓存就绪，后续实验可直接通过 `HF_HOME=/root/autodl-tmp/.hf_cache` 加载。

---
