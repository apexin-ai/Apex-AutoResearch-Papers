# infra predownload baseline models

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_predownload-baseline-models_20260519T143814_result.json`
- **Structured JSON:** [`7cc7b74c133b8283ee21.json`](../../sessions/7c/7cc7b74c133b8283ee21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型均已下载完成，残留文件已清理。

**最终结果：**

| 模型 | 缓存路径 | 大小 | 状态 |
|------|----------|------|------|
| `google-t5/t5-large` | `/root/autodl-tmp/.hf_cache/hub/models--google-t5--t5-large/snapshots/150ebc2c4b72291e770f58e6057481c8d2ed331a` | 2.8GB | ✓ |
| `EleutherAI/pythia-410m` | `/root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f` | 1.1GB | ✓ |

两个模型都已缓存到数据盘 `/root/autodl-tmp/.hf_cache/`，snapshot 目录完整（config.json、tokenizer、model.safetensors 等文件齐全），后续 `from_pretrained` 加载时会直接走本地缓存，不再需要下载。

---
