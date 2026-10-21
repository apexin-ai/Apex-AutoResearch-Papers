# code westd grpo restart save100

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd_grpo_restart_save100_20260516T144841_result.json`
- **Structured JSON:** [`a085c56f7b1039c609cb.json`](../../sessions/a0/a085c56f7b1039c609cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部成功启动，确认运行中。

**结果汇总：**

| 实验 | GPU | PID | tmux session |
|------|-----|-----|-------------|
| grpo_rasp_qwen_math_v3 | cuda:0 | 16817 | grpo_rasp_qwen_math_v3 |
| grpo_standard_qwen_math_v3 | cuda:1 | 16892 | grpo_standard_qwen_math_v3 |
| grpo_rasp_25_qwen_math | cuda:2 | 16983 | grpo_rasp_25_qwen_math |
| grpo_standard_25_qwen_math | cuda:3 | 17067 | grpo_standard_25_qwen_math |

全部配置 `save_steps=100`，预计 ~45 分钟完成。wandb run ID 需等训练初始化后从日志中获取。

---
