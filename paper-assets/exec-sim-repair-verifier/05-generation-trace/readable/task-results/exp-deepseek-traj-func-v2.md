# exp deepseek traj func v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_deepseek-traj-func-v2_20260516T131901_result.json`
- **Structured JSON:** [`9a96521d64a175bfb898.json`](../../sessions/9a/9a96521d64a175bfb898.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，汇报如下：

| 项目 | 值 |
|------|-----|
| PID | 511671 |
| GPU | cuda:2, 14977/32607 MiB |
| Total steps | 756 (8052 samples ÷ batch 32 × 3 epochs) |
| 速度 | ~4.2 s/step |
| 预估总时长 | ~53 分钟 |
| LoRA | rank=16, alpha=32, trainable 16.7M params (0.25%) |
| 标签 | LABEL_MAP = {1: "resolved", 0: "unresolved"} ✓ |
| 截断率 | 0% (train + val) |
| 输出目录 | `/root/autodl-tmp/checkpoints_deepseek_traj_v2/` |

**无需修改脚本** — `train_traj_verifier.py` 使用 AutoTokenizer/AutoModelForCausalLM，对 DeepSeek 开箱即用。`detect_thinking_support` 返回 `{'enable_thinking': False}`（无害，DeepSeek tokenizer 接受该 kwarg）。

日志路径：`/tmp/deepseek_traj_v2.log`

---
