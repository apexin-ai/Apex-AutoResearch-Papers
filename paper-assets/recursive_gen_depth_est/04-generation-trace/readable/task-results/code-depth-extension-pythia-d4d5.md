# code depth extension pythia d4d5

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_depth_extension_pythia_d4d5_20260515T035720_result.json`
- **Structured JSON:** [`2d5dc0c7e8e70bd5fa6c.json`](../../sessions/2d/2d5dc0c7e8e70bd5fa6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功提交并运行中。

**状态汇总：**
- **exp_id**: `depth_extension_pythia_d4d5_001` → RUNNING
- **PID**: 31646 (lora_finetune.py on depth_3)，GPU 0 占用 11.6GB
- **训练速度**: ~3.4 it/s，939 steps（3 epochs × 5000/8/2），预计 Step 1 约 4.5 分钟
- **tmux session**: `depth_ext`
- **日志**: `~/runs/recursive_gen_depth_est/depth_extension_pythia_d4d5_001.log`

**Pipeline 7 步：**
1. Finetune d3 → lora_depth_3 ← 进行中
2. Generate d4 (5000 samples, nucleus p=0.95)
3. Finetune d4 → lora_depth_4
4. Generate d5 (5000 samples)
5. Feature extraction d0-d5 (6-class, `--max_depth 5`)
6. RF/LR 6-class classification
7. Data summary

**修改内容：**
- `scripts/extract_features.py` — 新增 `--max_depth` 参数（默认 3，向后兼容）
- `scripts/run_depth_extension.sh` — 新建，完整 7 步 pipeline

参考 parent 实验 (mvp_pipeline_pythia_002) 的 wall_clock ~6400s，本实验有 2 轮 finetune+generate + 6-class feature extraction，预计总耗时约 1.5-2 小时。

---
