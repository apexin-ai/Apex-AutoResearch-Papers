# ops 20k gate prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_20k_gate_prep_20260520T024314_result.json`
- **Structured JSON:** [`2841ef69a953c732c8b3.json`](../../sessions/28/2841ef69a953c732c8b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。

```
M-sweep Launch Readiness (westd-41074)
========================================

[C4-ext M128 训练状态]
  当前: step 17350/100000, 0.6 sps
  ETA 到 20K: ~74 min (~12:00 UTC)
  ETA 到 50K: ~15 hours (~01:45 UTC May 21)
  Checkpoint: checkpoint.pt + checkpoint_step10000.pt
  save_every=10000 → 20K checkpoint 会自动保存

[M-sweep 资源]
  M=64 config:    EXISTS  configs/openvla_smart_compress_m64.yaml (num_queries=64)
  M=96 config:    EXISTS  configs/openvla_smart_compress_m96.yaml (num_queries=96)
  HF dataset:     CACHED  66GB (/root/autodl-tmp/.hf_cache/datasets/parquet/)
  Base model:     EXISTS  15GB (/root/autodl-tmp/openvla-libero-object/)
  Train script:   EXISTS  train_openvla_smart_compress.py
  Eval script:    EXISTS  eval_openvla_smart_compress.py
  Disk:           85GB free (250GB total)

[⚠️ 冲突]
  M128 训练正在占用 GPU (tmux session: train_openvla_sc_m128_seed42)
  M=64/96 训练需等 M128 结束 或 使用其他服务器

[Launch 命令模板]
  # M=64 训练
  python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m64.yaml

  # M=96 训练
  python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m96.yaml

  # C4-ext 20K eval (M128)
  python eval_openvla_smart_compress.py \
    --n_queries 128 \
    --checkpoint_path checkpoints/openvla_sc_m128/checkpoint_step20000.pt \
    --suite libero_object \
    --num_episodes 50 --gpu 0

  # C4-ext 50K eval (M128)
  python eval_openvla_smart_compress.py \
    --n_queries 128 \
    --checkpoint_path checkpoints/openvla_sc_m128/checkpoint_step50000.pt \
    --suite libero_object \
    --num_episodes 50 --gpu 0

[缺失项]
  无——所有脚本、config、数据、模型均已就绪
  唯一瓶颈: GPU 占用，M=64/96 需等 M128 完成或另开机器
```

**关键决策点**: M128 再跑 ~1.2h 到 20K。如果 20K gate 通过要立即起 M=64/96，有两个选择：
1. **停掉 M128**，先跑 M=64/96（M128 之后从 checkpoint 恢复）
2. **另开服务器**跑 M=64/96，westd-41074 继续跑 M128 到 50K/100K

---
