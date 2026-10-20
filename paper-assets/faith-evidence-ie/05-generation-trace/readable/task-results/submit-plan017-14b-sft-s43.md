# submit plan017 14b sft s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_plan017_14b_sft_s43_20260522T161048_result.json`
- **Structured JSON:** [`d2d9279c1fe55df2a365.json`](../../sessions/d2/d2d9279c1fe55df2a365.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动并注册。汇总：

**plan017_14b_sft_s43** — PID 189766, cuda:1

| 参数 | 值 |
|------|-----|
| model | Qwen3-14B (bf16, LoRA r=64 α=128) |
| data | docred train_annotated (3027 docs) |
| batch | 1 × 64 grad_accum = effective 64 |
| epochs | 3 (144 steps) |
| lr | 2e-4, warmup 5% |
| seed | 43 |
| output | /root/autodl-tmp/sft_output_14b_s43 |
| log | /root/runs/faith-evidence-ie/plan017_14b_sft_s43.log |
| wandb | freige-sft / sft-14b-s43 |

与 s42 的差异：单卡运行（无 DeepSpeed），gradient_accumulation_steps 从 32 调为 64 以保持相同的 effective batch size。训练动态等价。

预估时长：s42 双卡约 66 分钟，单卡约 2-2.5 小时。

---
