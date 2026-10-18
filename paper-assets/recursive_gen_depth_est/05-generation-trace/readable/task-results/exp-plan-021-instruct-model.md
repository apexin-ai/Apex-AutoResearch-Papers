# exp plan 021 instruct model

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_021_instruct_model_20260517T145549_result.json`
- **Structured JSON:** [`63515f92227363d2b83f.json`](../../sessions/63/63515f92227363d2b83f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并配置完毕。

**状态总结：**
- **exp_id**: `qwen25-1p5b-instruct-001`
- **GPU**: cuda:1 on gpu-6000pro-2
- **tmux session**: `qwen25-1p5b-instruct-001` (pid 788285)
- **当前状态**: 等待 aria2c 下载 model.safetensors (2.8GB, ~1MB/s, ETA ~40min)
- **下载完成后自动执行**: d0 生成 → LoRA finetune d0 → d1 生成 → ... → d3 生成 → 特征提取 → RF/LR 分类
- **Cron 监控**: 已注册，每 5 分钟检查
- **预计总时长**: 下载 ~40min + pipeline ~3-4h = ~4-5h

Pipeline 脚本:
- `/root/autodl-tmp/recursive_gen_depth_est/scripts/run_qwen25_1.5b_instruct_pipeline.sh`
- `/root/autodl-tmp/recursive_gen_depth_est/scripts/qwen25_1.5b_instruct_pipeline.py`

---
