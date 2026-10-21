# ops prepare qwen7b head2048 command

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_qwen7b_head2048_command_20260518T080125_result.json`
- **Structured JSON:** [`9502a762f331ed36f85d.json`](../../sessions/95/9502a762f331ed36f85d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。

## 关键发现

| 项目 | 结果 |
|---|---|
| `full_trace_head` condition | 有效 (train_sft.py 已支持) |
| 模型路径 | `/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct` (符合 C002) |
| 数据文件 | 存在于默认数据目录，train=4720 / test=1190 条 |
| 默认 data_dir | `/root/autodl-tmp/trace-verdict-study-data/` (脚本默认值，无需显式指定) |

## 确认的训练命令

```bash
bash -c 'cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_head --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_head2048_seed42 --seed 42 --wandb_project trace-verdict-study --wandb_run_name qwen7b_full_trace_head2048_seed42 --gradient_checkpointing'
```

注意事项：
- 使用 `/root/miniconda3/bin/python` (C002)
- 使用 `/root/trace-verdict-study/models/` 路径 (C002)
- 带 `--gradient_checkpointing` (C002, Qwen-7B 必须)
- 未指定 `--data_dir`，脚本默认 `/root/autodl-tmp/trace-verdict-study-data/`
- 未指定 `--max_steps`，将执行完整训练 (默认 -1)

---
