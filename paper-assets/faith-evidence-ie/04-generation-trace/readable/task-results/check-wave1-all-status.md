# check wave1 all status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_wave1_all_status_20260518T133812_result.json`
- **Structured JSON:** [`9f9f0f3b22df5966dc86.json`](../../sessions/9f/9f9f0f3b22df5966dc86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验仍在运行中，没有完成。GPU 并非空闲。

| exp_id | GPU | PID | 状态 | 进度 | 预计剩余 |
|--------|-----|-----|------|------|----------|
| wave1_sft_4b_s43 | cuda:0 (22GB) | 540786 | RUNNING | 105/144 steps (73%) | ~20 min |
| wave1_sft_4b_s44 | cuda:1 (28GB) | 540991 | RUNNING | 106/144 steps (74%) | ~18 min |
| wave1_grpo_bf16_g4 | cuda:2 (17GB) | 542126 | RUNNING | 25/200 steps (12.5%) | ~5-6 hours |
| seed_llama_rsft_k1_s43_eval | cuda:3 (18GB) | 541954 | RUNNING | 86/247 batches (35%) | ~90 min |

详细进度：
- **SFT s43/s44**: 两个 SFT 训练进度接近，都在 ~73-74%，每 step ~30s，内层 eval loop 985 samples 已完成多轮。约 20 分钟后完成。
- **GRPO bf16 g4**: 仅完成 25/200 steps，每 step ~2 min（含 generation），预计还需 5-6 小时。
- **LLaMA eval**: 86/247 inference batches，~35s/batch，输出目录尚为空（结果在推理全部完成后写入），约 90 分钟完成。

Director 报告"4 张 GPU 全部空闲"与实际不符。无需更新 registry，所有实验维持 RUNNING 状态。

---
