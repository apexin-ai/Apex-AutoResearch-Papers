# diagnose eval official smolvla prune k05 spatial v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_official_smolvla_prune_k05_spatial_v2_20260519T143506_result.json`
- **Structured JSON:** [`0c8d3b950683f29c2043.json`](../../sessions/0c/0c8d3b950683f29c2043.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**失败原因：VLM backbone 未缓存 + 无网络访问**

SmolVLA checkpoint (`smolvla_libero_official/config.json`) 引用 VLM backbone `HuggingFaceTB/SmolVLM2-500M-Instruct`，加载时 transformers 尝试从 HuggingFace 下载，但：

1. 服务器 HF 缓存中只有 `SmolVLM2-500M-Video-Instruct`（注意多了 **Video**），没有所需的 `SmolVLM2-500M-Instruct`
2. 服务器无法连接 `huggingface.co`（AutoDL 默认无外网，启动命令中未 `source /etc/network_turbo`）

之前 baseline 成功可能是当时网络可用或 VLM 权重恰好在缓存中。

**可修复，两种方案：**

1. **重新提交时加网络初始化**：命令前加 `source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache`，让 transformers 自动下载缺失的 VLM backbone
2. **预下载 VLM 权重**：先单独执行 `source /etc/network_turbo && python -c "from transformers import AutoModelForImageTextToText; AutoModelForImageTextToText.from_pretrained('HuggingFaceTB/SmolVLM2-500M-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')"` 缓存好后再跑 eval

方案 1 更简单，只需修改提交命令即可。

---
