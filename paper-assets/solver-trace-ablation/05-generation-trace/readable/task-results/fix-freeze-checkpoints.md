# fix freeze checkpoints

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_freeze-checkpoints_20260516T050910_result.json`
- **Structured JSON:** [`74a418d9d43180cd2b0d.json`](../../sessions/74/74a418d9d43180cd2b0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

14 个 .freeze 标记全部到位。磁盘 197G/250G (79%)，无 crontab 或清理脚本。

## 完整报告

### Success 实验 checkpoint 状态

| exp_id | checkpoint_path | 状态 | .freeze |
|--------|----------------|------|---------|
| sweep-isr-b02-s42 | sweep_isr_b02_s42_v2/checkpoint-500 | **存活（有权重）** | ✅ |
| sweep-isr-b005-s42 | sweep_isr_b005_s42/checkpoint-500 | **存活（有权重）** | ✅ |
| plan001-exec-only-s43-1000-r2 | plan001_exec_only_s43_1000_r2/ | **存活（有权重）** | ✅ |
| plan001-exec-only-s44-1000-r2 | plan001_exec_only_s44_1000_r2/ | **存活（有权重）** | ✅ |
| exp1-random-b03-s44-r2 | exp1_random_b03_s44_r2/ | 目录在，权重已删 | ✅ |
| exp1-random-b03-s43-r4 | exp1_random_b03_s43_r4/ | 目录在，权重已删 | ✅ |
| exp1-isr-b03-s44-r2 | exp1_isr_b03_s44_r2/ | 目录在，权重已删 | ✅ |
| plan009-sft-baseline-s44-1000 | plan009_sft_baseline_s44_1000/ | 目录在，权重已删 | ✅ |
| plan009-sft-baseline-s43-1000 | plan009_sft_baseline_s43_1000/ | 目录在，权重已删 | ✅ |
| plan009-sft-baseline-s42-1000 | plan009_sft_baseline_s42_1000/ | 目录在，权重已删 | ✅ |
| plan009-sft-baseline-s44-1000-r3 | plan009_sft_baseline_s44_1000/ | 同上（共用目录） | ✅ |
| plan009-sft-baseline-s44 | plan009_sft_baseline_s44/ | 目录在，权重已删 | ✅ |
| plan009-sft-baseline-s43 | plan009_sft_baseline_s43/ | 目录在，权重已删 | ✅ |
| plan016-extended-1000-s42 | plan016_extended_1000_s42 | **已删（目录不存在）** | — |
| exp1-random-b03-s43 | exp1_random_b03_s43/ | **已删（目录不存在）** | — |
| plan013-random-reward-s42-r4 | plan013_random_reward_s42_r4/ | **已删（目录不存在）** | — |
| exp1-isr-b03-s43 | exp1_isr_b03_s43/ | **已删（目录不存在）** | — |
| plan001-exec-only-s42-r2 | plan001_exec_only_s42/ | **已删（目录不存在）** | — |
| exp1-isr-b03-s43-r3 | exp1_isr_b03_s43_r3/ | **已删（目录不存在）** | — |
| plan009-sft-baseline-s42-r4 | plan009_sft_baseline_s42/ | **已删（目录不存在）** | — |
| plan018-additive-random-b01-s44 | plan018_additive_random_b01_s44/ | **已删（目录不存在）** | — |
| sta-phase1-exec-only-r5 | grpo_exec_only/ | **已删（目录不存在）** | — |
| exp2-exec-s43-greedy | N/A（eval only） | N/A | — |
| exp4-100step-h1h7 | json 文件 | N/A | — |
| plan012-hacking-taxonomy | N/A（分析任务） | N/A | — |
| plan003-eval-exec-only-r5 | json 文件 | N/A | — |
| sta-gt-isr-baseline | json 文件（存活） | N/A | — |
| sta-phase0-baseline | json 文件（存活） | N/A | — |

### 汇总

- **4 个实验有完整模型权重** → 已冻结
- **8 个实验目录存在但权重已被清理**（仅剩 training_args.bin）→ 已冻结防进一步删除
- **9 个实验目录完全不存在** → 无法恢复
- **5 个实验为 eval/分析任务**，无模型 checkpoint
- 磁盘：197G/250G (79%)
- 无 crontab 或自动清理脚本

---
