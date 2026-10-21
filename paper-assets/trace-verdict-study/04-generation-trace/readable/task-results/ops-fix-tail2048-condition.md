# ops fix tail2048 condition

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_tail2048_condition_20260518T034945_result.json`
- **Structured JSON:** [`ade920deebfb81dc81dc.json`](../../sessions/ad/ade920deebfb81dc81dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查结果：

**`full_trace_tail_2048` 不存在。** choices 里没有这个 condition，也没有对应的数据文件。

**`full_trace_tail` 就是 tail-2048。** 逻辑：
- `full_trace_tail` 加载 `full_trace_tail_train.jsonl`（不做 trace token 截断）
- `to_chat_text` 把整个序列截断到 `max_length=2048`
- 因为数据本身是 tail 格式（保留 trace 的尾部），最终效果 = tail-2048
- 与之对比：`full_trace_tail_1024` / `_512` / `_256` 是先把 trace 截到 N tokens 再套 2048 总长

**CodeLlama-13B 模型路径**：`/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf`（注意在 autodl-tmp 下，不在 trace-verdict-study/models/ 下）

**正确命令：**
```bash
/root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail \
  --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail_seed42 \
  --wandb_run_name codellama13b_full_trace_tail_seed42 \
  --gradient_checkpointing \
  --max_steps 444
```

注：`--max_steps 444` 参照之前 codellama13b tail 实验的 step 数（从 tail512 log 可见 444 steps）。如果需要匹配其他实验的 step 数请确认。

---
