# code probe pipeline

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_probe-pipeline_20260515T065409_result.json`
- **Structured JSON:** [`f16fa4f9c472de8e213b.json`](../../sessions/f1/f16fa4f9c472de8e213b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已部署到 `/root/vla-ssd/scripts/`：

| 脚本 | 大小 | 功能 |
|------|------|------|
| `train_probes.py` | 18K | Probe 训练（temporal_distance / subtask_predicate / oracle） |
| `analyze_results.py` | 13K | 多模型结果对比、可视化、PASS/FAIL 判定 |
| `init_untrained.py` | 3.5K | OpenVLA LLM backbone 随机重初始化 |

**使用示例**：

```bash
# 1. Temporal distance probe（对每层训练线性 probe）
python scripts/train_probes.py \
  --features_dir features/trained/ \
  --output_dir results/trained/ \
  --probe_type temporal_distance

# 2. Oracle 基线（输入=时间差标量，预期 ρ≈1.0）
python scripts/train_probes.py \
  --features_dir features/trained/ \
  --output_dir results/trained/ \
  --probe_type oracle

# 3. Sub-task predicate probe（需要 label 文件）
python scripts/train_probes.py \
  --features_dir features/trained/ \
  --output_dir results/trained/ \
  --probe_type subtask_predicate \
  --label_file labels/predicates.json

# 4. 初始化 untrained 模型
python scripts/init_untrained.py \
  --model_path checkpoints/openvla-7b \
  --output_path checkpoints/openvla-7b-untrained/

# 5. 结果分析与对比
python scripts/analyze_results.py \
  --results_dirs trained:results/trained/,untrained:results/untrained/,dinov2:results/dinov2/ \
  --output_dir results/analysis/
```

**关键设计**：
- 逐层加载特征（避免一次性加载 33 层 × 所有轨迹的内存爆炸）
- 自动检测 OpenVLA（`demo_N/last_preaction`）和 DINO-V2（`traj_N/cls_token`）格式
- Distance-stratified sampling：10 bins × 50 pairs/bin/traj → 训练约 200K pairs
- 分析脚本自动检测 oracle 结果并画入对比图，输出 PNG + PDF

---
