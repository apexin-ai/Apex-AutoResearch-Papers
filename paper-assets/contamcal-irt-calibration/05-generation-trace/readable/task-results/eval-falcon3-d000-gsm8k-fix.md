# eval falcon3 d000 gsm8k fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_falcon3-d000-gsm8k-fix_20260523T075319_result.json`
- **Structured JSON:** [`62b85d7a4ba561955629.json`](../../sessions/62/62b85d7a4ba561955629.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**汇总：**
- **修复**：`evaluate.py` line 323，`evaluate_gsm8k` 中加 `tokenizer.chat_template is not None` 判断，无 chat template 时直接用 raw prompt（与 `evaluate_mcq` 一致）
- **tmux session**：`eval_falcon3_d000_gsm8k`
- **PID**：788671，GPU 0
- **进度**：330 batches（GSM8K test 1319 items, batch_size=4），已开始推理
- **Registry**：`eval_falcon3_d000_gsm8k_s42_v2` → RUNNING
- **输出目录**：`/root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_d000_gsm8k_s42/`
- **日志**：`/root/autodl-tmp/exp001/logs/eval_falcon3_d000_gsm8k.log`

---
