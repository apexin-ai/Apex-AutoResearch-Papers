# eval 15B s123 para aligned batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_15B_s123_para_aligned_batch_20260515T200721_result.json`
- **Structured JSON:** [`ad75e036d4bac5b1e3c1.json`](../../sessions/ad/ad75e036d4bac5b1e3c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并运行中。汇总：

**Checkpoints（4/4 存在）：**
| Dose | Path |
|------|------|
| d000 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter` |
| d005 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter` |
| d025 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter` |
| d100 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter` |

**已有 eval 结果：** 无（4 个全部 MISSING，无跳过）

**提交状态：**
- PID: 627600 (tmux 内实际 PID 627614)
- tmux session: `exp_001_eval_15B_s123_para_aligned_batch`
- GPU: cuda:3, 已占用 3654 MiB
- Log: `~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log`

**Log 前几行：** 模型加载正常，bitsandbytes 有非致命 warning（libnvJitLink.so.13 缺失，不影响 eval），已开始评估 d000 的 mmlu paraphrased（加载 6596 条 QC-passed paraphrased items）。

---
