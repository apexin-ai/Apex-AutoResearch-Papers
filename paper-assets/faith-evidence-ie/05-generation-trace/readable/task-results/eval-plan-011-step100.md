# eval plan 011 step100

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_011_step100_20260515T144401_result.json`
- **Structured JSON:** [`d03f026bc97df65b9bd4.json`](../../sessions/d0/d03f026bc97df65b9bd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:3 上已经在跑 checkpoint-100 的 eval（PID 215286，启动 1 分 12 秒前）。**

具体进程：

| PID | 运行时间 | 任务 |
|-----|---------|------|
| 208155 | 47m | RSFT score filter (NLI scoring) |
| 214562 | 3m29s | **checkpoint-80 eval** |
| 215286 | 1m12s | **checkpoint-100 eval** ← 你要提交的任务 |

PID 215286 的完整命令：
```
python -m freige.eval.inference \
  --model_path /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100 \
  --sft_adapter /root/autodl-tmp/sft_output \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --data_path /root/autodl-tmp/data/docred \
  --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 \
  --output_dir /root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-100 \
  --no-quantize
```

checkpoint-100 eval 已经在运行中，无需重复提交。三个参数（`--base_model` + `--sft_adapter` + `--model_path`）都已正确传入。结果将输出到 `/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-100`。

---
