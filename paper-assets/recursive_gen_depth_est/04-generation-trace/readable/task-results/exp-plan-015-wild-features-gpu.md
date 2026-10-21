# exp plan 015 wild features gpu

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_015_wild_features_gpu_20260517T151732_result.json`
- **Structured JSON:** [`6b2d84367f576cfa1ff7.json`](../../sessions/6b/6b2d84367f576cfa1ff7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均已启动并在运行：

**子任务 1 - Wild Data 特征提取**
- PID 788803, tmux session `wild_data_features_001`
- 进度: c4_10k 2000/10000（正常推进中）
- Registry: `wild_data_features_001` → RUNNING
- Log: `~/runs/recursive_gen_depth_est/wild_data_features_001.log`

**子任务 2 - Qwen2.5-14B 下载**
- PID 789171, `hf download` 替代已废弃的 `huggingface-cli`
- 现有: shards 1-4 已下载 (~15GB), 还需下载 shards 5-8 (~15GB)
- 下载目标路径: `/root/autodl-tmp/models/qwen25_14b/`
- 磁盘剩余 97GB，空间充足
- Log: `/root/autodl-tmp/recursive_gen_depth_est/logs/qwen25_14b_download.log`

注意: 还有 2 个先前的 Qwen2.5-1.5B-Instruct 下载进程在后台运行 (PID 787385, 787711)，可能是 `qwen25-1p5b-instruct-001` 实验的准备步骤。

---
