# eval submit 3 evals gpu saturation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_submit_3_evals_gpu_saturation_20260518T163339_result.json`
- **Structured JSON:** [`42e27a9f73bc057c1df8.json`](../../sessions/42/42e27a9f73bc057c1df8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 张卡已开始加载模型，确认全部在跑。

**提交汇总：**

| Eval | GPU | PID | 命令关键参数 |
|---|---|---|---|
| `plan019_1_7b_sft_s44_eval` | cuda:0 | 558241 | `--model_path .../Qwen3-1.7B --sft_adapter .../sft_output_qwen3_1_7b_bf16_seed44/` |
| `random_rsft_k1_eval` | cuda:1 | 558320 | `--model_path .../rsft_output_random_k1/checkpoint-1020 --base_model .../Qwen3-4B --sft_adapter .../sft_output/` |
| `grpo_bf16_g4_ckpt100_eval` | cuda:3 | 558467 | `--model_path .../grpo_bf16_g4/checkpoint-100 --base_model .../Qwen3-4B --sft_adapter .../sft_output/` |

**注意事项：**
- 1.7B SFT s44 adapter 实际路径为 `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed44/`（非指令中的 `sft_output_qwen3_1_7b_s44`）
- 4B base model 路径为 `/root/autodl-tmp/models/Qwen3-4B`
- 所有命令均设置了 `CUDA_VISIBLE_DEVICES`（C002/C003），提交前已验证目标 GPU 显存 < 2GB（C001）
- D076 协议参数全部已加：`--batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize`

---
