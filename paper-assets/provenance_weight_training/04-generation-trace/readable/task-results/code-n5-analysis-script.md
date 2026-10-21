# code n5 analysis script

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n5_analysis_script_20260524T054927_result.json`
- **Structured JSON:** [`4c9604e35f5d11a19c10.json`](../../sessions/4c/4c9604e35f5d11a19c10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两种模式都工作正常。

**脚本就绪**: `/root/provenance_weight_training/analysis/n5_statistical_analysis.py`

**使用方式**:

1. **命令行输入**:
   ```bash
   python analysis/n5_statistical_analysis.py \
     --adaptive 17.680 17.666 17.677 X Y \
     --uniform 17.694 17.686 17.702 X Y \
     --seeds 42 123 456 789 1024
   ```

2. **自动读取 eval 目录**:
   ```bash
   python analysis/n5_statistical_analysis.py --auto
   ```
   自动匹配 `bs16_adaptive_tau07_seed*` 和 `bs16_uniform_seed*` 目录，读取 `eval_holdout.json` / `eval_owt.json` / `eval_wiki.json`，处理 `_r2`/`_r3` 后缀（取最新 rerun）。

3. **保存 JSON**: 加 `--output_json results.json`

**当前 auto 模式状态**: Holdout 有 2 个 seed pair（seed42/123），seed456 缺 `eval_holdout.json`；OOD 有 3 个 seed pair。N=5 训练完成后跑 `--auto` 即可获得完整统计报告。

---
