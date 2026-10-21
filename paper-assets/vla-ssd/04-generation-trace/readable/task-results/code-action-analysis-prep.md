# code action analysis prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action-analysis-prep_20260515T142500_result.json`
- **Structured JSON:** [`45691fa277fa2cf10459.json`](../../sessions/45/45691fa277fa2cf10459.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都已写好并 dry-run 通过：

**`/root/vla-ssd/scripts/analyze_action_probes.py`**
- 读取 trained/untrained/dinov2 的 `action_prediction` 和 `action_delta` 结果
- 输出 per-layer R² 对比表、per-dim R² (7维)、per-task R² (10 tasks)、per-task consistency
- G1/G1-delta/G2-delta/G3 四个 gate 判定
- 保存 JSON 摘要到 analysis 目录
- 支持部分结果（缺失模型/层会标 SKIP/N/A）

**`/root/vla-ssd/scripts/plot_action_probes.py`**
- Fig 1: per-layer R²(action) 曲线 + DINO 水平线 + copy_baseline(0.97)
- Fig 2: per-layer R²(action-delta) 曲线 + copy_baseline(0)
- Fig 3: per-dim R² 分组柱状图 (best layer)
- Fig 4: per-task R² heatmap (trained/untrained 并排)
- PDF + PNG 输出到 `results/figures/`

当前只有 DINO 的 1 层数据，dry-run 生成了 Fig 1 和 Fig 3。trained/untrained 实验完成后直接跑即可。

---
