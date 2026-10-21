# code dino action probe adaptation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dino-action-probe-adaptation_20260515T142009_result.json`
- **Structured JSON:** [`bf0e3d4f56d08212d2a8.json`](../../sessions/bf/bf0e3d4f56d08212d2a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。

## 结论

**状态: ready** — 无需修改代码。

`train_probes.py` 已经完全兼容 DINO features：
- `scan_features` 通过 `AGG_MAP` fallback 找到 `cls_token`，检测 2D shape → `n_layers=1, hidden_dim=1024`
- `load_layer_features` 对 2D 数据直接 `ds[:]`，忽略 layer 参数
- `ActionMLPProbe(1024)` 自动适配输入维度
- 只 sweep 1 层 (`[0]`)，500 trajs (400 train / 100 val)

**执行命令:**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ \
  --probe_type action_prediction \
  --epochs 50 --patience 5 --batch_size 256 --lr 1e-3 --gpu 0
```

**预估运行时间:** 1-2 分钟。只有 1 层，维度 1024（比 VLA 的 4096 小 4x），50 epochs with early stopping，数据量 ~120k samples。

---
