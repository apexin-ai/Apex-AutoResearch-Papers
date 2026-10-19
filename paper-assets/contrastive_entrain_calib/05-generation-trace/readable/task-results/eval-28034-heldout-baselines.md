# eval 28034 heldout baselines

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-heldout-baselines_20260523T071648_result.json`
- **Structured JSON:** [`359249246bc56438028f.json`](../../sessions/35/359249246bc56438028f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**1. eval_held_out.jsonl 传输** — 无需传输，28034 已有该文件（70 行，70992 bytes），与 29046 上的 eval_split.jsonl 一致。

**2. Vanilla baseline eval (cuda:2)**
- PID: 56465（子进程已启动）
- 状态：模型已加载，正在推理 70 对数据
- GPU 占用：16458 MiB / 32607 MiB
- 命令：
```
CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --data_path /root/contrastive_entrain_calib/data/eval_held_out.jsonl \
  --output_dir eval_results/heldout_vanilla_baseline/ \
  --exp_id heldout_vanilla_baseline
```

**3. R3-only ckpt-6500 eval (cuda:3)**
- PID: 56851（子进程已启动）
- 状态：模型+LoRA adapter 已加载，正在推理 70 对数据
- GPU 占用：16844 MiB / 32607 MiB
- Checkpoint 路径：`/root/autodl-tmp/checkpoints/exp003/checkpoint-6500`
- 命令：
```
CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --lora_path /root/autodl-tmp/checkpoints/exp003/checkpoint-6500 \
  --data_path /root/contrastive_entrain_calib/data/eval_held_out.jsonl \
  --output_dir eval_results/heldout_r3only_ckpt6500/ \
  --exp_id heldout_r3only_ckpt6500
```

**4. rl-ckpt-7000 eval (PID 55429, cuda:0)**
- 仍在运行（已 14 分钟），进度 320/362，预计 ~2 分钟完成
- 注意：跑的是默认 sycophancy_bench 全量数据（362 对），不是 held-out 的 70 对

**5. 备注**
- eval 脚本无 `--preset` / `--gpu` 参数，实际参数为 `--model_path`, `--lora_path`, `--data_path`, `--output_dir`, `--exp_id`
- 70 对数据推理预计 5-10 分钟完成

---
