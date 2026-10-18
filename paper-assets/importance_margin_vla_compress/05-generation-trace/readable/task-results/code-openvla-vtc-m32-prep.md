# code openvla vtc m32 prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_vtc_m32_prep_20260519T210659_result.json`
- **Structured JSON:** [`a76f4720a73b20a5fd38.json`](../../sessions/a7/a76f4720a73b20a5fd38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置验证通过。全部准备完成。

---

**M=32 配置已就绪**: `configs/openvla_smart_compress_m32.yaml`

与 M=128 的差异：
- `num_queries`: 128 → **32** (256→32 tokens, 87.5% 压缩)
- `output_dir`: `openvla_sc_m128_seed42` → `openvla_sc_m32_seed42`
- **lora 段已移除**（VTC-only，无 LoRA）

**启动命令**（等你准备好时执行）：
```bash
cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml
```

WandB run name 会自动生成为 `openvla_sc_m32`（脚本第 580 行从 `num_queries` 推导）。

---
