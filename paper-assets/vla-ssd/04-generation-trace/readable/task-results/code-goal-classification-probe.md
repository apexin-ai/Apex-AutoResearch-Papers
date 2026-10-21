# code goal classification probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_goal-classification-probe_20260515T162300_result.json`
- **Structured JSON:** [`6ff1414701ee3a1c9b96.json`](../../sessions/6f/6ff1414701ee3a1c9b96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结已实现的内容：

**`/root/vla-ssd/scripts/train_probes.py` 新增：**
- `GoalClassificationProbe` (line 335) — MLP (D → 256 → n_classes)，ReLU + Dropout(0.1)
- `train_goal_classification_probe()` (line 469) — CrossEntropyLoss，early stopping on val accuracy (patience=5)
- `run_goal_classification()` (line 894) — 复用 `scan_features` / `split_by_task` / `load_layer_features`；每帧一个样本，label = task index；per-layer 独立训练
- 输出：accuracy, macro_f1, per_class_accuracy, confusion_matrix, best_layer, accuracy_by_layer
- `parse_args` / `save_results` / `main()` 均已更新

**`/root/vla-ssd/scripts/analyze_goal_probes.py` 新建：**
- 读取 trained/untrained/dinov2 三组结果
- Per-layer accuracy 对比表 + best layer summary
- Gate: trained acc > 50% AND trained-DINO gap > 40pp

**Dry-run 验证**（LIBERO-10 trained features, layer 16）：
- 500 trajs → 400 train / 100 val → 110660/27430 samples → acc=1.00, F1=1.00, 6 epochs, 30s
- 100% accuracy 符合预期：LIBERO-10 各 task 来自不同 scene，视觉即可区分
- LIBERO-Goal（同一 scene 不同 goal）才是真正有意义的测试目标

运行命令示例：
```bash
python scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/trained/ \
  --probe_type goal_classification
```

---
