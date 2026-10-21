# code baseline control script

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_control_script_20260518T121253_result.json`
- **Structured JSON:** [`c1f19adc2e1c20bcb21d.json`](../../sessions/c1/c1f19adc2e1c20bcb21d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。结果总结：

**脚本路径**: `/root/autodl-tmp/importance_margin_vla_compress/train_baseline_control.py`
**Config 路径**: `/root/autodl-tmp/importance_margin_vla_compress/configs/baseline_control.yaml`
**Checkpoint 路径**: `checkpoints/libero_full_ft/step_099999/checkpoint.pt` (step 99999, 确认存在)

**Dry-run 结果**:
- Checkpoint 加载成功 (step 99999)
- Trainable params: **99,880,992** / 450,046,176 (**22.19%**) -- 只有 action expert + projections
- Expert 接收梯度: True
- Frozen params 无梯度: True
- Vision tokens: 128 (无压缩)
- Forward loss: 0.0780

**启动命令**:
```bash
export PATH=/root/miniconda3/bin:$PATH
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
cd /root/autodl-tmp/importance_margin_vla_compress

python train_baseline_control.py \
    --config configs/baseline_control.yaml \
    --wandb_project smart-compress-vla \
    --wandb_run baseline_control_fresh_lr
```

**配置对照**:
| 参数 | Smart Compress | Baseline Control |
|------|---------------|-----------------|
| Init checkpoint | smolvla_base (pretrained) | libero_full_ft step_099999 |
| Vision tokens | 128 → 32 (compressor) | 128 (原始) |
| Trainable | compressor + expert | expert only |
| lr | 1e-4 cosine | 1e-4 cosine |
| Steps | 100K | 100K |
| Batch size | 4 | 4 |
| Warmup | 1000 | 1000 |

---
