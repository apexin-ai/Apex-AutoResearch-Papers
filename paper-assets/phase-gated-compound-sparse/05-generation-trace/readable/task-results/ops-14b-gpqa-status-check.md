# ops 14b gpqa status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b_gpqa_status_check_20260517T003045_result.json`
- **Structured JSON:** [`b4b9a8acfbe2aafccbd2.json`](../../sessions/b4/b4b9a8acfbe2aafccbd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 14B 模型 ===
状态: 完成
路径: /root/autodl-tmp/pacs/checkpoints/Qwen2.5-14B-Instruct -> /root/autodl-tmp/models/Qwen/Qwen2___5-14B-Instruct
大小: 28G
文件: config.json + 8x model*.safetensors + tokenizer.json + tokenizer_config.json ✓

=== GPQA Pipeline ===
数据: 就绪 (198 题)
已完成条件:
  - profiling_output_gpqa_ds_importance_s015/ — profiling_results.json ✓ + generations.json ✓

进行中条件:
  - profiling_output_gpqa_ds_importance_s020/ — 116/198 (58%), GPU0, 运行 ~7h
  - profiling_output_gpqa_ds_importance_s025/ — 26/198 (13%), GPU1, 运行 ~1.3h

适配状态: 无需额外适配
  - 使用 --raw_prompt + --max_new_tokens 8192 + --max_problems 198
  - 有 gpqa_batch_launcher.sh 和 gpqa_remaining_commands.txt 用于批量管理
  - test_dsr1_gpqa.py 用于验证

另外注意: GPU2/GPU3 正在跑 MATH500 的 recency masking 实验 (s025/s030)
```

---
