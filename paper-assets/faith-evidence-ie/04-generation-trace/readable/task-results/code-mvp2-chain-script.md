# code mvp2 chain script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp2-chain-script_20260514T084119_result.json`
- **Structured JSON:** [`2057d5bd77f7dce11949.json`](../../sessions/20/2057d5bd77f7dce11949.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。脚本已写入 `/root/autodl-tmp/run_mvp2_chain.sh` 并设为可执行。

### 参数验证总结

**grpo_trainer.py 参数**（已对齐）：
- `--model_name`, `--sft_adapter`, `--data_dir`, `--output_dir`, `--stage`
- `--tau_start`, `--tau_end`, `--reward_device` — stage≥2 时使用，stage 1 不需要
- `--num_generations`, `--per_device_batch_size`, `--gradient_accumulation_steps`, `--num_epochs`, `--learning_rate`, `--seed`, `--wandb_run_name`

**inference.py 参数**（已对齐）：
- `--model_path`（必填）, `--base_model`（默认 Qwen3-4B）, `--data_path`（必填）, `--output_dir`（必填）
- `--batch_size`, `--max_new_tokens`, `--split`（默认 dev）, `--seed`, `--quantize`

### 6 个 Phase

| Phase | 类型 | 输出 |
|-------|------|------|
| 1 | SFT Eval | `eval_sft/` |
| 2 | CED Eval | `eval_ced/` |
| 3 | flat-NLI Train (stage 2) | `grpo_s2/` |
| 4 | flat-NLI Eval | `eval_flatnli/` |
| 5 | extraction-only Train (stage 1) | `grpo_s1/` |
| 6 | extraction-only Eval | `eval_extract/` |

---
