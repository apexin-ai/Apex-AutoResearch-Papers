# code rank32 eval script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rank32-eval-script_20260515T132749_result.json`
- **Structured JSON:** [`2cd5a15e830caaa127ff.json`](../../sessions/2c/2cd5a15e830caaa127ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。eval 命令已写入 `artifacts/cwm_rank32_eval_command.sh` 并注册。

关键信息：
- **eval 脚本**: `eval_cwm_baseline.py`，读取 `data/cwm_test.jsonl`（1890 samples，function-level）
- **参数与 baseline 一致**: `batch_size=16, max_seq_length=2048, max_new_tokens=64, --save_predictions`
- **checkpoint**: `checkpoints_cwm_rank32/best`（训练完成后自动生成，备选 `checkpoint-1434`）
- **输出**: `eval_results/cwm_rank32_eval/eval_cwm_rank32_results.json`
- **GPU**: `CUDA_VISIBLE_DEVICES=0`（训练完成释放后可用）
- eval 脚本无 `--device` 参数，用 `model.cuda()` 硬编码，需通过 `CUDA_VISIBLE_DEVICES` 控制

---
