# infra deepseek prep verify

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_deepseek_prep_verify_20260515T113321_result.json`
- **Structured JSON:** [`16973c91782edd9cc8fb.json`](../../sessions/16/16973c91782edd9cc8fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总如下：

---

## deepseek_vota_seed42 进度

- **Step**: 159/444 (35.8%)
- **Epoch**: ~1.07 (刚完成第 1 轮 eval)
- **Loss 趋势**: 0.467 → 0.052 (epoch 0→1)，正常下降
- **Token accuracy**: 98.4%
- **速度**: ~17-18s/step
- **预计剩余**: 285 steps × ~17.5s ≈ **83 分钟** (~1h23m)

## ae_only 进度

- **Step**: 358/444 (80.6%)
- **Epoch**: 2.37
- **Loss**: 0.023，token accuracy 99.3%
- **速度**: ~19s/step
- **预计剩余**: 86 steps × ~19s ≈ **27 分钟**

## 数据文件验证

全部 6 个文件存在，行数一致：

| 条件 | Train | Test |
|------|-------|------|
| exception_only | 4720 | 1190 |
| full_trace | 4720 | 1190 |
| no_trace | 4720 | 1190 |

## 脚本兼容性

- `train/train_sft.py`: 支持 `--model_path`（L63），默认 Qwen，可覆盖为 DeepSeek 路径
- `eval/evaluate.py`: 支持 `--model_path`（L114）和 `--output`（L119）

## 3 个 DeepSeek 提交命令

**1. exception_only**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final/eval_results.json"
```

**2. no_trace**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final/eval_results.json"
```

**3. full_trace**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace/final/eval_results.json"
```

## 风险/注意事项

- **GPU 竞争**: deepseek_vota 和 ae_only 都在 `--gpu 0` 运行。服务器有 2 张卡，但当前两个 tmux session 可能占满。提交新任务前需确认 ae_only 已完成或使用 `CUDA_VISIBLE_DEVICES=1` 分配到另一张卡。
- **ae_only 约 27 分钟完成**，完成后 GPU 1 会空出来（如果它在 GPU 1 上的话），或需要等 deepseek_vota 也完成才能在同一张卡上排队。
- **full_trace 数据量最大**（32MB train），训练时间会比其他条件更长。

---
