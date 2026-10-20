# code write eval runner

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_write-eval-runner_20260514T074007_result.json`
- **Structured JSON:** [`cdfff4aca0bea9f7053d.json`](../../sessions/cd/cdfff4aca0bea9f7053d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `/root/autodl-tmp/freige/eval/run_eval.py`，导入和参数解析验证通过。

运行示例：
```bash
cd /root/autodl-tmp && python -m freige.eval.run_eval \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --adapter_path /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/eval_results/sft \
  --batch_size 4 --max_new_tokens 1024 --split dev
```

输出两个文件到 `--output_dir`：
- `metrics.json` — F1, Ign-F1, Evi-F1, EDCR, format_compliance_rate, n_truncated 等
- `raw_predictions.json` — 每个文档的原始模型输出 + truncated 标记

---
