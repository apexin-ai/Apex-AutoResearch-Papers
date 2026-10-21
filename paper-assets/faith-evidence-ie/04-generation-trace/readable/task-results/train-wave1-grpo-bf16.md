# train wave1 grpo bf16

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_wave1_grpo_bf16_20260518T124324_result.json`
- **Structured JSON:** [`35346fc05655ef675b62.json`](../../sessions/35/35346fc05655ef675b62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功提交并注册。

**总结：**

| 项目 | 值 |
|---|---|
| exp_id | `wave1_grpo_bf16_g4` |
| PID | 542121 |
| GPU | cuda:2 (10.4 GB 占用) |
| 状态 | RUNNING |
| 输出目录 | `/root/autodl-tmp/grpo_bf16_g4` |
| 日志 | `/root/autodl-tmp/grpo_bf16_g4.log` |
| RSFT checkpoint | `/root/autodl-tmp/sft_output` |
| 训练参数 | bf16 no-quantize, G=4, grad_accum=16, max_steps=200, kl=0.0 |

修复了一个 bug：脚本中 `--no_quantize` 改为 `--no-quantize`（argparse 连字符格式）。训练已进入 GRPO generation 阶段，首步 generation 较慢属正常。

---
