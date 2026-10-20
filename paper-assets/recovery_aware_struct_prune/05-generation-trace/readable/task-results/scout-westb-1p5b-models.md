# scout westb 1p5b models

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scout_westb_1p5b_models_20260519T185019_result.json`
- **Structured JSON:** [`8f9d343745c1608b7836.json`](../../sessions/8f/8f9d343745c1608b7836.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GRPO checkpoint 的模型文件在 `checkpoint-100/` 子目录中。汇总如下：

## westb-23072 1.5B Checkpoint 清单

### 完整可用（根目录有 config.json + model.safetensors）

| # | 路径 | 剪枝方法 | 阶段 |
|---|------|----------|------|
| 1 | `models/DeepSeek-R1-Distill-Qwen-1.5B` | — | Dense 原模型 |
| 2 | `pruned_standard_20_1p5b` | Standard 20% | 剪枝后 |
| 3 | `pruned_cka_only_20_1p5b` | CKA-only 20% | 剪枝后 |
| 4 | `pruned_rasp_20_1p5b` | RASP 20% | 剪枝后 |
| 5 | `sft_standard_20_1p5b` | Standard 20% | SFT 恢复 |
| 6 | `sft_cka_only_20_1p5b` | CKA-only 20% | SFT 恢复 |
| 7 | `sft_rasp_20_1p5b` | RASP 20% | SFT 恢复 |
| 8 | `grpo_standard_20_1p5b` | Standard 20% | GRPO 恢复 |

所有路径前缀: `/root/autodl-tmp/recovery_aware_struct_prune/`

### 需用子目录路径（模型在 checkpoint-100/ 下）

| # | 路径 | 剪枝方法 | 阶段 |
|---|------|----------|------|
| 9 | `grpo_cka_only_20_1p5b/checkpoint-100` | CKA-only 20% | GRPO 恢复 |
| 10 | `grpo_rasp_20_1p5b/checkpoint-100` | RASP 20% | GRPO 恢复 |

### eval_mbpp.py
**已就绪** — `/root/recovery_aware_struct_prune/src/eval_mbpp.py` 存在。

### 磁盘警告
**数据盘 100% 满**（250G/250G，仅剩 159MB）。MBPP eval 如果需要写临时文件或缓存，可能会失败。建议先清理空间。

---
