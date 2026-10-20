# code baseline and main

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_and_main_20260512T115620_result.json`
- **Structured JSON:** [`9eaa07f357be1e6ea0bd.json`](../../sessions/9e/9eaa07f357be1e6ea0bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入且语法正确：

- **`baselines/golden_ratio_baseline.py`** — 固定比例混合 baseline。G0 用真实数据，G1+ 按 `--real_ratio` 混合真实+合成数据。复用 `train_generation`、`prepare_real_data`、`prepare_synthetic_data` 等现有模块，输出格式与 pilot_pipeline 一致。

- **`main_experiment.py`** — 全量对比实验编排。训练共享 G0 后，对 3 个条件独立运行 G1+：
  - `pure_synthetic`：100% 合成数据
  - `fixed_mix`：固定比例混合
  - `pi_controller`：每个 checkpoint 间隔计算谱有效秩 → 输入 `CollapseAwareController` → 获取 `w_t` → 重新混合数据训练下一段（segment-level 控制，每段 `save_steps` 步）
  
  输出每个条件的 `summary.json` + 跨条件 `comparison_summary.json` 和 `comparison.csv`。

---
