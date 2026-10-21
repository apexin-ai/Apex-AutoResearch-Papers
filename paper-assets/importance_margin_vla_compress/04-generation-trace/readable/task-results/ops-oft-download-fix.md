# ops oft download fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_oft-download-fix_20260520T114944_result.json`
- **Structured JSON:** [`be8c10aed8bdfae24e0b.json`](../../sessions/be/be8c10aed8bdfae24e0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 下载状态报告

**正确的 HF repo**: `moojink/openvla-7b-oft-finetuned-libero-object`（不是 `jxu124/OpenVLA-oft`）

**已完成文件**（均经 Content-Length 校验）：

| 文件 | 大小 | 状态 |
|------|------|------|
| model-00001-of-00004.safetensors | 4.59 GB | ✓ |
| model-00002-of-00004.safetensors | 4.61 GB | ✓ |
| model-00003-of-00004.safetensors | 4.61 GB | ✓ |
| action_head--150000_checkpoint.pt | 302 MB | ✓ |
| lora_adapter/adapter_model.safetensors | 484 MB | ✓ |
| proprio_projector--150000_checkpoint.pt | 67 MB | ✓ |
| config/tokenizer 等小文件 | ~2.5 MB | ✓ |

**下载中**：
- `model-00004-of-00004.safetensors`: 53/250 MB (21%), ~100KB/s via xet bridge, ETA ~30 min
- aria2c PID=237350 后台运行

**模型路径**: `/root/autodl-tmp/openvla-oft-libero-object/`（与 `analyze_openvla_oft.py` 中 `CHECKPOINT_PATH` 匹配）

**解决方案总结**：
1. ModelScope 没有此模型 → 404
2. `HF_HUB_DISABLE_XET=1` 导致下载到的是指针文件（非真实权重）
3. xet 下载返回 401（即使配了 HF token）
4. 最终方案：`wget + Authorization header` 直接从 HuggingFace CDN 下载大文件，model-00004 走 xet bridge（aria2c 16 连接加速）

**下载完成后需要验证**：确认 `.aria2` 文件消失即为完成。

---
