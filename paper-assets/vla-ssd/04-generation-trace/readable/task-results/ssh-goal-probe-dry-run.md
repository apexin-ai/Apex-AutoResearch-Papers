# ssh goal probe dry run

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_goal-probe-dry-run_20260515T172856_result.json`
- **Structured JSON:** [`2d2844f0b6c81f43c9c2.json`](../../sessions/2d/2d2844f0b6c81f43c9c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇报如下：

---

## 验证结果

### 1. train_probes.py goal_classification 代码完整性：✅

| 组件 | 行号 | 状态 |
|------|------|------|
| `GoalClassificationProbe` | L335 | ✅ MLP D→256→n_classes, ReLU+Dropout(0.1) |
| `train_goal_classification_probe()` | L469 | ✅ CrossEntropyLoss, early stopping on val **accuracy** (patience=5) |
| `run_goal_classification()` | L895 | ✅ 复用 scan_features/split_by_task/load_layer_features |
| 输出指标 | L525-532 | ✅ accuracy, macro_f1, per_class_accuracy, confusion_matrix, traj_accuracy (majority vote), val_preds |
| save_results 处理 | L1029-1043 | ✅ best_layer/best_accuracy/best_macro_f1/best_traj_accuracy/accuracy_by_layer/traj_accuracy_by_layer |

### 2. analyze_goal_probes.py：✅

- 存在，5342 bytes，May 16 更新
- 读取 trained/untrained/dinov2 三组 `goal_classification/summary.json`
- 输出 per-layer accuracy 对比表（含 traj_acc）、best layer summary
- Gate 判定：trained acc > 0.50 **AND** trained−DINO gap > 0.40pp

### 3. 特征文件 H5 结构：✅

**进度（比预期更好）：**
- trained: **9/10**（缺 `turn_on_the_stove.h5`）
- untrained: **8/10**（缺 `turn_on_the_stove.h5` + `put_the_wine_bottle_on_top_of_the_cabinet.h5`）
- 源数据: 10 个 hdf5 文件齐全

**H5 结构：**
```
demo_N/
  image_mean:      (T, 33, 4096) float16
  last_preaction:  (T, 33, 4096) float16
```
- 50 demos per task, layer dim 在 axis=1（非 layer_0 分组）
- `load_layer_features` 用 `ds[:, layer, :]` 切片，与此结构匹配

### 4. DINO 提取命令：✅ 就绪

- `extract_dinov2.py` 通过 `glob(data_dir/*.hdf5)` 发现数据，兼容 libero_goal
- DINOv2-large checkpoint 已在 `/root/autodl-tmp/vla-ssd/checkpoints/dinov2-large/`（config.json + model.safetensors）

就绪命令：
```bash
cd /root/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python scripts/extract_dinov2.py \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \
  --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ \
  --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large \
  --gpu 0
```

### 5. 注意事项

- **n_classes 动态计算**：`run_goal_classification` 中 `n_classes = len(task_names)` 基于 h5 文件数。当前 trained 9 个文件 → 9-class 问题。10 个全齐后需重跑才是完整的 10-class 对比。不影响代码正确性，但结果不可直接与 10-class 版本比较。
- **无 bug 发现**，代码路径完整，无缺失依赖。

---
