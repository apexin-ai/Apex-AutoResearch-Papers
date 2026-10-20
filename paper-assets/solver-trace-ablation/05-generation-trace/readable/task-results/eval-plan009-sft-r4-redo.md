# eval plan009 sft r4 redo

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan009-sft-r4-redo_20260514T122554_result.json`
- **Structured JSON:** [`eb90d8519225c08ce5e8.json`](../../sessions/eb/eb90d8519225c08ce5e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**plan009-sft-baseline-s42-r4 训练已完成**，但 eval 无法执行——两卡均满载（~80GB/97GB）。

### 已完成
- Checkpoint 确认存在：`/root/autodl-tmp/outputs/plan009_sft_baseline_s42`（7.5GB model + 15GB optimizer in checkpoint-500/）
- 训练 500 steps 正常结束（TRL SFT, Qwen3-4B, seed=42）
- Registry 已更新：checkpoint_path, log_path, notes

### 待 GPU 释放后执行
```bash
# 1. eval_sta.py
export CUDA_VISIBLE_DEVICES=N && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_sta.py --model_path /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --data_path data/train_500_seed42.jsonl --output_path /root/autodl-tmp/outputs/plan009_sft_s42_r4_eval.json

# 2. classify_h7.py
export CUDA_VISIBLE_DEVICES=N && python3 scripts/classify_h7.py --eval_path /root/autodl-tmp/outputs/plan009_sft_s42_r4_eval.json

# 3. 清理 checkpoint-500/ (15GB optimizer.pt)
```

### GPU 占用
- cuda:0: PID 564905, 80214 MiB（可能是 plan018-additive-random-b01-s44）
- cuda:1: PID 587160, 79962 MiB（plan006-prolog-exec-s43）

需要等其中一张卡释放后再跑 eval。

---
