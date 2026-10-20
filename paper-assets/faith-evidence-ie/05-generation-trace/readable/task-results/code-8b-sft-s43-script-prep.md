# code 8b sft s43 script prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b_sft_s43_script_prep_20260519T105913_result.json`
- **Structured JSON:** [`7c11eed04cb9a681f40b.json`](../../sessions/7c/7c11eed04cb9a681f40b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建并通过语法检查。

**训练脚本** `/root/autodl-tmp/freige/scripts/seed_expansion/sft_8b_s43.sh`：
- 参数与 `sft_8b_s44.sh` 完全一致（lora_rank=64, lr=2e-4, grad_accum=16, epochs=3）
- seed=43, output → `/root/autodl-tmp/sft_output_8b_seed43`
- wandb run: `sft-8b-s43`

**Eval 脚本** `/root/autodl-tmp/freige/scripts/seed_expansion/eval_sft_8b_s43.sh`：
- D076 协议：`--no-quantize`, `--batch_size 4`, `--max_new_tokens 1024`, `--seed 42`
- 无 `--sft_adapter`（SFT 直接推理）
- output → `/root/autodl-tmp/eval_results/sft_8b_s43_eval`

注意：用户指定的 `--base_model` 路径 `/root/autodl-tmp/models/Qwen3-8B` 不存在，实际路径是 `/root/autodl-tmp/models/Qwen/Qwen3-8B`（有 `Qwen/` 子目录），脚本中已用正确路径。两个脚本均未设 `CUDA_VISIBLE_DEVICES`，由 tmux wrapper 处理。

---
