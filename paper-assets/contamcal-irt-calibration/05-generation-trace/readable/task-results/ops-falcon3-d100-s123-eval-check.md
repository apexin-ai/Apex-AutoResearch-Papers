# ops falcon3 d100 s123 eval check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-d100-s123-eval-check_20260523T005017_result.json`
- **Structured JSON:** [`2903a8f23c03edc97b64.json`](../../sessions/29/2903a8f23c03edc97b64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动。GPU 0 显存 14796MiB / 24564MiB，PID 752802。

## 报告

### Part 1: Eval 结果 (eval_falcon3_d100_s123)
| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | **62.68%** | 8801/14042 |
| ARC-Challenge | **84.22%** | 987/1172 |

Registry 已更新为 success，cron 已删除。

### Part 2: Volume Control 训练 (sft_falcon3_7b_volume_control)
- **PID**: 752802
- **GPU**: cuda:0, 14796MiB / 24564MiB (60%)
- **tmux**: `falcon3_volctrl`
- **数据**: 66533 items, tokenize 完成，训练已开始
- **配置**: Falcon3-7B-Base, LoRA r=16 α=32, lr=5e-5, bs=1 ga=16, gradient_checkpointing
- Registry 已注册为 RUNNING

---
