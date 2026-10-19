# ops verify nli on 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-nli-on-29046_20260523T101355_result.json`
- **Structured JSON:** [`637f43afc1ca1c7c37ec.json`](../../sessions/63/637f43afc1ca1c7c37ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**NLI 模型已就位**，但不在代码预期的本地目录，而是在 HuggingFace cache 中：

| 项 | 状态 |
|---|---|
| 预期路径 `eval/nli-deberta-v3-base-local/` | **不存在** |
| HF cache (autodl-tmp) | `/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/` — **715MB，完整** |
| HF cache (默认) | `/root/.cache/huggingface/hub/models--cross-encoder--nli-deberta-v3-base/` — **715MB，完整** |
| 关键文件 | `config.json` ✓, `model.safetensors` ✓, `tokenizer.json` ✓, `spm.model` ✓ |
| snapshot | `6c749ce3425cd33b46d187e45b92bbf96ee12ec7` |

模型存在两份 cache 副本（可能是 `HF_HOME` 设置变更所致）。如果代码硬编码了 `nli-deberta-v3-base-local/` 路径则需要改为从 cache 加载（`cross-encoder/nli-deberta-v3-base`），或创建符号链接。

---
