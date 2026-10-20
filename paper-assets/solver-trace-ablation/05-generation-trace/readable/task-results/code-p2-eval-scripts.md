# code p2 eval scripts

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p2-eval-scripts_20260513T222126_result.json`
- **Structured JSON:** [`5889ba43e35c1bc05f33.json`](../../sessions/58/5889ba43e35c1bc05f33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本全部通过语法检查：

| 脚本 | 状态 | 说明 |
|------|------|------|
| `scripts/eval_sta.py` | 已存在 | plan_003 全 STA 评估，含 prove_rate / mean_isr / isr_std / median_isr / isr_pr_ratio |
| `scripts/eval_o1_vs_on.py` | **新建** | plan_004 O(1)二值 vs O(N)连续 ISR 对比，输出 correlation / agreement / case breakdown |
| `scripts/train_sft.py` | **新建** | plan_009 SFT baseline，trl.SFTTrainer + chat-format NL→FOL 训练对，支持 wandb / bf16 / gradient_checkpointing |

---
