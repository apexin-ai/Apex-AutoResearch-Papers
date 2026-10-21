# code prepare crossseed plan017

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_crossseed_plan017_20260518T141456_result.json`
- **Structured JSON:** [`825c3e22860038b45009.json`](../../sessions/82/825c3e22860038b45009.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

命令模板已保存到 `artifacts/plan017_commands.md`。

验证结果：
- `--condition full_trace_tail_512` 在 train_sft.py 和 evaluate.py 的 choices 中均存在，数据文件 `full_trace_tail_512_{train,test}.jsonl` 已就绪
- `--seed`、`--label_only_loss`、`--gradient_checkpointing` 参数均可用
- 所有命令使用 `/root/miniconda3/bin/python`，Qwen-7B/CodeLlama-13B 带 `--gradient_checkpointing`，CodeLlama 带 `--label_only_loss`

需注意：现有 Qwen-7B seed42 实验 (`full_trace_tail_seed42`) 实际使用的 condition 是 `full_trace_tail` 而非 `full_trace_tail_512`。新 seed 实验统一用 `full_trace_tail_512` 以保持跨模型一致性。如果 seed42 也需要用 `full_trace_tail_512` 重跑 Qwen-7B，请确认。

8 个实验顺序执行预计总 GPU 时间 ~13.2h。

---
