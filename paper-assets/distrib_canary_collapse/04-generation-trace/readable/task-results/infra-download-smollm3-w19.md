# infra download smollm3 w19

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download_smollm3_w19_20260518T191121_result.json`
- **Structured JSON:** [`8de804bed9acddec108a.json`](../../sessions/8d/8de804bed9acddec108a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

```
--- 文件列表 ---
total 5.8G
-rw-r--r-- 1 root root  13K  README.md
-rw-r--r-- 1 root root  943  config.json
-rw-r--r-- 1 root root  126  generation_config.json
-rw-r--r-- 1 root root 4.7G  model-00001-of-00002.safetensors
-rw-r--r-- 1 root root 1.2G  model-00002-of-00002.safetensors
-rw-r--r-- 1 root root  27K  model.safetensors.index.json
-rw-r--r-- 1 root root 311K  notebook.ipynb
-rw-r--r-- 1 root root  151  special_tokens_map.json
-rw-r--r-- 1 root root  17M  tokenizer.json
-rw-r--r-- 1 root root  50K  tokenizer_config.json

--- 目录总大小 ---
5.8G  /root/autodl-tmp/models/SmolLM3-3B-Base/

--- 模型验证 ---
Vocab size: 128000
Model class: SmolLM3ForCausalLM
Params: 3.08B
Output: The meaning of life is a question that has been asked by philosophers, theolog
SUCCESS
```

模型已下载到 `/root/autodl-tmp/models/SmolLM3-3B-Base/`，3.08B 参数，CPU bf16 加载和生成均正常。onnx 目录是第一次下载残留的空目录，不影响使用。

---
