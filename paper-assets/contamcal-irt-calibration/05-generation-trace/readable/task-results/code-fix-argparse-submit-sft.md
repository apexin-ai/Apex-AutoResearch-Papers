# code fix argparse submit sft

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_argparse_submit_sft_20260515T161123_result.json`
- **Structured JSON:** [`bfa90f2b9ad74d018fcf.json`](../../sessions/bf/bfa90f2b9ad74d018fcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已提交成功。

**修复内容**: `train_sft.py` 缺少 `--gpu` argparse 定义，导致 CLI 传 `--gpu 0` 时解析报错。已添加参数并 commit (`834fd2b`)。注意 `--lora-alpha` 的传递路径本身是正确的（`LoraConfig` 已使用 `args.lora_alpha`），不存在硬编码覆盖的 bug。

**实验状态**:
| 实验 | GPU | PID | tmux session |
|------|-----|-----|-------------|
| `exp_001_sft_3B_d100_s42_a32` | cuda:4 | 590776 | `exp_001_sft_3B_d100_s42_a32` |
| `exp_001_sft_3B_d025_s42_a32` | cuda:5 | 590861 | `exp_001_sft_3B_d025_s42_a32` |

Output dirs: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d{100,025}_a32_s42`

---
