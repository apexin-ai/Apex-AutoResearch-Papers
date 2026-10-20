# code dino action probe prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dino-action-probe-prep_20260515T141941_result.json`
- **Structured JSON:** [`72a09979473693e501d6.json`](../../sessions/72/72a09979473693e501d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。

## 结果

**兼容性**：train_probes.py 原生支持 DINO 特征，无需任何修改。
- DINO `.h5` 文件包含 `cls_token` (T, 1024) 和 `patch_mean` (T, 1024)
- `scan_features` 自动检测为单层 (n_layers=1, hidden_dim=1024)
- `AGG_MAP` fallback 机制自动选择 `cls_token`

**Dry-run 指标** (Layer 0, 唯一层):
- overall R² = 0.6689
- per_task_mean_R² = 0.6759
- gripper_accuracy = 0.9001
- epochs = 17, 耗时 7.3s

**最终启动命令**（DINO 只有单层，跑完就是全部结果）：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_prediction --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0"
```

实际上 dry-run 已经产出了完整结果（单层 7 秒跑完），结果已存于 `/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/`。

---
