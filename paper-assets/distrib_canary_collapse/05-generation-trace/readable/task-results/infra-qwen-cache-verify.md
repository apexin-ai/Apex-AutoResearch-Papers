# infra qwen cache verify

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_qwen_cache_verify_20260518T184154_result.json`
- **Structured JSON:** [`fb8cfb8b0cf5040b38c6.json`](../../sessions/fb/fb8cfb8b0cf5040b38c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器验证完毕。

## 结果汇总

| | westd-19828 | westd-17855 |
|---|---|---|
| **权重位置** | `/root/autodl-tmp/models/Qwen3.5-0.8B-Base/` | `/root/autodl-tmp/models/Qwen3.5-0.8B-Base/` |
| **文件** | `model.safetensors-00001-of-00001.safetensors` (1,746,942,600 bytes) | 同左 |
| **目录大小** | 1.7G | 1.7G |
| **Model class** | `Qwen3_5ForCausalLM` | `Qwen3_5ForCausalLM` |
| **参数量** | 0.75B | 0.75B |
| **Vocab** | 248,044 | 248,044 |
| **Generate** | 成功 | 成功 |
| **HF cache** | 仅 refs/main（无权重副本） | 无 |
| **结论** | **可用** | **可用** |

注意事项：
1. 两台服务器的权重都在显式目录而非 HF cache，加载时需指定本地路径 `/root/autodl-tmp/models/Qwen3.5-0.8B-Base`，不能直接用 `Qwen/Qwen3.5-0.8B-Base` hub ID
2. weight_map 含 `model.visual.merger` 键，但实际加载为 `Qwen3_5ForCausalLM`（纯文本 CausalLM），参数量 0.75B 符合预期
3. 缺少 `flash-linear-attention` 和 `causal-conv1d`，当前 fallback 到 torch 实现（训练时可能需要安装以获得加速）

---
