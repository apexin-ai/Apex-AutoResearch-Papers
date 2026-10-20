# code training framework

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_training-framework_20260514T044803_result.json`
- **Structured JSON:** [`27a82e12683f7d80083c.json`](../../sessions/27/27a82e12683f7d80083c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。创建的文件清单：

| 文件 | 说明 |
|------|------|
| `src/prompts.py` | Prompt 模板 + SFT/GRPO 格式化函数 |
| `src/sandbox.py` | 沙箱执行：`execute_code`、`execute_probe`、`run_tests` |
| `src/reward_funcs.py` | GRPO reward：format/execution/diagnostic/probe_dependence |
| `src/train_sft.py` | SFT 训练（TRL SFTTrainer + LoRA） |
| `src/train_grpo.py` | GRPO 训练（TRL GRPOTrainer，从 SFT checkpoint 继续） |
| `src/evaluate.py` | 三模式评估（base/sft/grpo）+ bootstrap CI |
| `src/run_mvp.sh` | MVP 全流程串联脚本，支持 `--start-from` |
| `src/__init__.py` | 包初始化 |

---
