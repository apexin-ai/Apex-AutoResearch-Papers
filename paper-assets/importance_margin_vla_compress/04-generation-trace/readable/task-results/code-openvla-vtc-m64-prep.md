# code openvla vtc m64 prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_vtc_m64_prep_20260519T212907_result.json`
- **Structured JSON:** [`65b79640188ca31b0aea.json`](../../sessions/65/65b79640188ca31b0aea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

### 产出

**M=64 配置文件**: `/root/autodl-tmp/importance_margin_vla_compress/configs/openvla_smart_compress_m64.yaml`
- `num_queries: 64`（256→64 tokens, 75% 压缩）
- VTC-only，无 LoRA
- 其他超参与 M=32 一致

**Dry-run 结果** (GPU 1, 3 steps):
- 模型加载: 7.54B params, VisionTokenCompressor 403M trainable (5.07%)
- 数据集: 273465 samples, 34183 batches/epoch
- step 0: loss=15.6064, grad_norm=762.61
- 正常完成，GPU 1 已释放

**正式启动命令**:
```bash
cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export WANDB_MODE=offline && CUDA_VISIBLE_DEVICES=1 python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m64.yaml
```

**注意**: 环境变量必须用 `HF_HOME=/root/autodl-tmp/.hf_cache` + `TRANSFORMERS_OFFLINE=1`（不是 `HF_HUB_OFFLINE=1`），否则数据集加载会报错。这与当前 GPU 0 上运行的 M=128 训练一致。

---
