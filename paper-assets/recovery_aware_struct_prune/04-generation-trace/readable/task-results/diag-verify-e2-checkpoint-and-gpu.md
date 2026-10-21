# diag verify e2 checkpoint and gpu

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_verify_e2_checkpoint_and_gpu_20260518T214435_result.json`
- **Structured JSON:** [`eb693c6d89dcef49b9bb.json`](../../sessions/eb/eb693c6d89dcef49b9bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### Checkpoint 完整性：完整

| 项目 | 状态 |
|------|------|
| 目录存在 | `/grpo_cka_only_20_extended_300/` |
| model.safetensors | 12GB（单文件，7B 模型合理） |
| config.json | 1.7K |
| tokenizer.json + tokenizer_config.json | 齐全 |
| chat_template.jinja | 齐全 |
| generation_config.json | 齐全 |
| training_args.bin | 齐全 |
| checkpoint-300/ 子目录 | 存在，含完整 optimizer/scheduler/rng state（27GB） |
| 总大小 | 38GB |

Checkpoint 完整，可直接用于后续 eval。

### GPU 状态

| GPU | 显存占用 | 状态 | 运行任务 |
|-----|---------|------|---------|
| cuda:0 | 0 MiB / 97887 MiB | **空闲** | 无（E2 GRPO 训练已结束） |
| cuda:1 | 19251 MiB | 运行中 | `eval_math500` — grpo_standard_20_fair_v2（tmux: `eval_math500_v2`） |
| cuda:2 | 17019 MiB | 运行中 | `eval_math500` — sft_cka_only_20_v4（tmux: `sft_cka_eval_v4`） |
| cuda:3 | 17541 MiB | 运行中 | `eval_math500` — grpo_rasp_20_fair（tmux: `rasp_grpo_eval`） |

cuda:0 空闲，可立即用于下一步任务。另外注意有两个 DeepSeek-R1-Distill-Qwen-7B 下载进程在后台运行（无 GPU 占用）。

---
