# train smart compress m96 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_smart_compress_m96_seed43_20260518T123650_result.json`
- **Structured JSON:** [`e7c1e477ee33d34825b1.json`](../../sessions/e7/e7c1e477ee33d34825b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。

---

**汇总：**

**Config** (`configs/smart_compress_m96_seed43.yaml`):
```yaml
_base_: smart_compress.yaml
compressor:
  num_queries: 96
training:
  output_dir: "checkpoints/smart_compress_m96_seed43"
  seed: 43
```

**提交命令**:
```bash
bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/importance_margin_vla_compress && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline CUDA_VISIBLE_DEVICES=2 python -u train_smart_compress.py --config configs/smart_compress_m96_seed43.yaml --wandb_run smart_compress_m96_seed43 --seed 43 --gpu 0"
```

**Dry-run**: 通过。Loss=1.3307, M=96, compression=1.33x, 梯度正常。

**训练状态**: 已启动，step=50 时 loss=0.6729, sps=3.2。cqa1-33015 cuda:2, tmux session `train_smart_compress_m96_seed43`, registry 状态 RUNNING。

---
