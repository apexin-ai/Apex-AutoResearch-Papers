# ops westd32935 setup batch 20260522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd32935_setup_batch_20260522_20260522T034633_result.json`
- **Structured JSON:** [`7fd92ef1a60efc7bca0f.json`](../../sessions/7f/7fd92ef1a60efc7bca0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== 连接 ==
westd-32935: OK

== 环境 ==
GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition 96GB x 4
Python: 3.12.3 (miniconda3)
PyTorch: 2.11.0+cu128
transformers: 5.8.1

== Checkpoint 检查 ==
sft_alpha4_20: OK
grpo_alpha4_20/checkpoint-100: OK
grpo_stage2_standard_20_fair: OK
sft_random_20: OK

== 修复 ==
- 安装了缺失的 sentencepiece（sft_random_20 tokenizer 依赖）
- sft_alpha4_20 首次加载时 attention reshape 报错，第二次启动正常运行

== 提交结果 ==
| GPU | exp_id | PID | 验证 |
|-----|--------|-----|------|
| 0 | eval_math500_grpo_standard_20_fair_2048_v2 | 2234 | OK (16521 MiB, 97%) |
| 1 | eval_math500_sft_random_20_v2 | 3886 | OK (12335 MiB, 加载中) |
| 2 | eval_gsm8k_sft_alpha4_20_v5 | 3586 | OK (12675 MiB, 92%) |
| 3 | eval_gsm8k_grpo_alpha4_20_v3 | 2737 | OK (12747 MiB, 90%) |

== Cron ==
全部已注册（120s 轮询）

== 磁盘 ==
/root/autodl-tmp: 650G 总量，280G 已用 (43%)
```

---
