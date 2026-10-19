# code run plan 001 script

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_run_plan_001_script_20260521T024821_result.json`
- **Structured JSON:** [`55549123107dc2e82ae8.json`](../../sessions/55/55549123107dc2e82ae8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`run_plan_001.sh` 已部署到 `westd-13176:/root/xling_calib_direction/run_plan_001.sh`，语法检查通过。

**关键设计点**:

1. **GPTQ 加载**: 用 `--quantization none`，让 HF 从模型 config 自动检测 GPTQ 量化。`--quantization int4` 是 bitsandbytes NF4，对已量化 GPTQ 模型无意义且可能冲突。需要 `auto-gptq` 或 `gptqmodel` 后端（Step 0 自动检测安装）。

2. **Train/eval split 衔接**: `--split_ratio 0.7` 输出 `layer{i}_{lang}_train.pt` / `_eval.pt`，但下游脚本期望 `layer{i}_{lang}.pt`。通过 symlink 目录解决：
   - `train/` — 所有语言 train split 的 symlink（供 train_probe 使用）
   - `for_eval/` — EN 指向 train split（与 probe 训练数据一致），target langs 指向 eval split（held-out 评估）

3. **4 步流水线**: 模型验证 → 激活提取 → EN probe 训练 → 5 种 transfer 方法评估（zero-shot、mean-shift、Procrustes-100、few-shot-25、few-shot-100）

---
