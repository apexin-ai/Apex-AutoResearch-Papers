# code timestep accuracy analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_timestep-accuracy-analysis_20260515T170152_result.json`
- **Structured JSON:** [`c40427fce53c42e80db0.json`](../../sessions/c4/c40427fce53c42e80db0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都已创建并验证通过。

**已完成：**

1. **`/root/vla-ssd/scripts/analyze_timestep_accuracy.py`** — Per-timestep goal classification accuracy 分析
   - 复用 `train_probes.py` 的 `scan_features`、`load_layer_features`、`GoalClassificationProbe` 等
   - 对每层重新训练 probe，评估时按 relative timestep (t/T) 分 N 个 bin 计算 accuracy
   - 额外计算 front 30% 和 back 30% accuracy，检测是否存在后期泄漏
   - 输出 JSON 到 `{output_dir}/goal_classification/timestep_analysis.json`
   - 支持 `--best_layer_only` 快速分析单层

2. **`/root/vla-ssd/scripts/plot_timestep_accuracy.py`** — 可视化
   - 读取三个模型的 `timestep_analysis.json`
   - 画 line plot: 三条线 (trained/untrained/DINO) + chance level (10%) + 25% gate 线
   - 绿色阴影标注 "front 30%" 区域
   - 额外生成 front-30% vs back-30% bar chart
   - PDF + PNG 输出到 `results/figures/`

---
