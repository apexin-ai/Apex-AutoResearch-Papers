# code precheck compounding sweeps

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_precheck_compounding_sweeps_20260516T070832_result.json`
- **Structured JSON:** [`4c4c654f1f97601bf3c9.json`](../../sessions/4c/4c4c654f1f97601bf3c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`einops` is available. Now I have everything needed for the report.

---

## 预检结果

| 架构 | 脚本存在 | k值范围 | 模型路径正确 | 特殊patch | 就绪 |
|------|---------|--------|-------------|----------|------|
| Yi-1.5-9B | Y (本地未提交) | [0,2,4,8,16,32,64,128,256] | Y (4 safetensors) | N/A | **N** — 需同步 |
| Gemma-2-9b | Y (本地未提交) | [0,2,4,8,16,32,64,128,256] | Y (8 safetensors) | BOS prepend ✓, eager attn ✓ | **N** — 需同步 |
| CodeLlama-7b | Y (本地未提交) | [0,2,4,8,16,32,64,128,256] | Y (2 safetensors) | N/A | **N** — 需同步 |
| Phi-3-medium | Y (本地未提交) | [0,2,4,8,16,32,64,128,256] | **N** — 模型未下载 | fused qkv via eval_ppl ✓ | **N** — 需同步+下模型 |
| InternLM2-7b | Y (本地未提交) | [0,2,4,8,16,32,64,128,256] | ⚠ .bin 格式 (15G, 无safetensors) | einops wqkv patch ✓ | **N** — 需同步 |

### 阻塞项

1. **全部 5 个脚本未提交 git** — 本地 untracked，服务器上不存在。需要 commit → push → 服务器 pull。

2. **Phi-3 模型未下载** — 路径 `/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct` 不存在，服务器上找不到任何 Phi-3 相关文件。需要下载（~28GB，建议用 ModelScope）。

3. **InternLM2 使用 .bin 格式** — 有 `pytorch_model-00001-of-00002.bin` (15GB total)，transformers 可以加载但比 safetensors 慢。功能上不阻塞。

### 特殊 patch 验证

- **Gemma-2**: BOS prepend 在 `load_calibration_data_bos` 中实现 ✓；使用 `attn_implementation="eager"` 规避 sliding window SDPA 问题 ✓
- **InternLM2**: 自定义 `patch_attention_internlm2` 函数，用 einops rearrange 处理 fused wqkv ✓；`einops` 已安装 ✓
- **Phi-3**: 通过 `eval_ppl.patch_attention` 自动检测 `qkv_proj` 属性处理 fused qkv ✓；需 `trust_remote_code=True` ✓

### 解除阻塞需要的操作

1. `git add` 5 个脚本 → commit → push → 服务器 `git pull`
2. 服务器下载 Phi-3-medium-128k-instruct（优先 ModelScope CDN）

---
