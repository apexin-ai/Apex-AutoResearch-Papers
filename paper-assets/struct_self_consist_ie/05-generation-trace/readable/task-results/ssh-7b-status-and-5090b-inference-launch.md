# ssh 7b status and 5090b inference launch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-status-and-5090b-inference-launch_20260520T022051_result.json`
- **Structured JSON:** [`26570ef2209871ac6095.json`](../../sessions/26/26570ef2209871ac6095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

### 5090-c: 7B Pipeline 正常运行中

- **PID 71837** 存活，运行 14h52m
- **训练已完成**，merged model 已导出到 `checkpoints/qwen25-7b-fewnerd-merged/`（14.2GB，4 个 safetensors，时间戳 10:13）
- **Inference 进行中**：seed 42，5% 完成（15288/301184 prompts），速度 ~56 it/s
  - 命令：`python code/run_mvp_pilot.py --model_path checkpoints/qwen25-7b-fewnerd-merged --n_samples 8 --seed 42 --collect_logprobs --output_dir output/fewnerd_7b/qwen25_7b_n8_seed42`
  - vLLM 单 GPU（GPU 2，29.8GB），预计 seed 42 剩余 ~85 分钟
  - Pipeline 脚本应会自动继续 seed 123、456，总计还需 ~4-5 小时
- **14B 训练**同时在 GPU 0-1 上运行（`train_config_qwen25_14b_fewnerd_s42.yaml`，双卡 torchrun）
- **GPU 3 空闲**

### 5090-b: 模型下载完成

- PID 160848 已结束
- `/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct/` 完整（15GB，4 个 safetensors）

### 判断

Pipeline 在 5090-c 上已经进入 inference 阶段，按指令**不在 5090-b 上重复启动**。但 5090-c 只用单 GPU 跑 inference，3 个 seed 串行预计需要 4-5 小时。如果想加速，可以考虑在 5090-b 上并行跑 seed 123 和 456（不会与 5090-c 的 seed 42 重复），但这需要先把 merged model rsync 过去。是否需要这样做？

---
