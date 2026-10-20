# code lg instruction probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lg-instruction-probe_20260515T165250_result.json`
- **Structured JSON:** [`5ee636960e762e4b11f8.json`](../../sessions/5e/5ee636960e762e4b11f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本参数解析均通过。

---

## 报告

### LIBERO-Goal 数据结构

10 个任务共享同一 kitchen scene，50 demos/task：

| # | Task |
|---|------|
| 0 | open_the_middle_drawer_of_the_cabinet |
| 1 | open_the_top_drawer_and_put_the_bowl_inside |
| 2 | push_the_plate_to_the_front_of_the_stove |
| 3 | put_the_bowl_on_the_plate |
| 4 | put_the_bowl_on_the_stove |
| 5 | put_the_bowl_on_top_of_the_cabinet |
| 6 | put_the_cream_cheese_in_the_bowl |
| 7 | put_the_wine_bottle_on_the_rack |
| 8 | put_the_wine_bottle_on_top_of_the_cabinet |
| 9 | turn_on_the_stove |

特征格式与 LIBERO-10 相同。Chance level = 10%。

特征提取进度：trained 2/10, untrained 1/10, DINO 目录尚未创建。

### 代码设计决策

1. **`train_goal_probe.py`** — 复用 `train_probes.py` 的 `scan_features`, `split_by_task`, `load_layer_features`, `parse_layers`, `apply_pca`, `train_goal_classification_probe`, `save_results`。不重复实现基础设施，只添加 goal-specific 逻辑：
   - 类别平衡报告（每个 task 的 train/val trajectory 数）
   - Chance level 计算和 Δchance 输出
   - `--shuffle_labels` 排列检验（阴性对照）
   - 输出兼容现有 `save_results` 格式（per-layer JSON + summary.csv + summary.json）

2. **`analyze_goal_results.py`** — 独立脚本，无 torch 依赖。三级判定：
   - **G1**: peak acc > chance + 20pp → trained 编码了 goal
   - **G2**: Δacc(trained−untrained) > 10pp 在 ≥5 层 → 训练提升了区分度
   - **G3**: trained peak > DINO peak → VLA > 纯视觉
   - 阈值可通过 `--g1_margin`, `--g2_margin`, `--g2_min_layers` 调节
   - 同时输出 markdown 和 JSON

3. **与现有代码的关系**：服务器上已有 `train_instruction_probes.py`（带场景分组）和 `analyze_goal_probes.py`（简单 gate）。新脚本的区别：`train_goal_probe.py` 更轻量（不做场景分组，LIBERO-Goal 全部同场景所以不需要），`analyze_goal_results.py` 增加了 G1/G2/G3 三级判定和 per-layer delta 分析。

---
