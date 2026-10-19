# code run plan 002 script

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_run_plan_002_script_20260521T022924_result.json`
- **Structured JSON:** [`686a834e2433c4110260.json`](../../sessions/68/686a834e2433c4110260.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**脚本**: `/root/xling_calib_direction/run_plan_002.sh` (westd-13176)

4 个 step：
1. 验证模型 — 检查 14 个 safetensors shards + tokenizer
2. 提取激活 — 12 层 × 20 语言，`--split_ratio 0.7`，输出到 `/root/autodl-tmp/activations/llama4_scout/`
3. 训练 + 评估 — 用 train split 训 EN probe，用 eval split 跑 5 种 transfer methods (zero_shot / mean_shift / procrustes_100 / few_shot_25 / few_shot_100)
4. 汇总 — 结果写入 `/root/xling_calib_direction/results_plan002/`

关键处理：`--split_ratio` 产出的 `_train.pt`/`_eval.pt` 文件通过 symlink 桥接到下游脚本期望的 `layer{i}_{lang}.pt` 格式。Procrustes 阶段 EN eval 和 target eval 来自相同 MMLU items，确保 parallel pairs 正确对齐。

---
