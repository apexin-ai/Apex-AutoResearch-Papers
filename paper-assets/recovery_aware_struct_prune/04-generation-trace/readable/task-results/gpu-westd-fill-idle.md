# gpu westd fill idle

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_westd_fill_idle_20260516T184831_result.json`
- **Structured JSON:** [`a271c472e2ba27fbca95.json`](../../sessions/a2/a271c472e2ba27fbca95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在加载数据集，即将开始推理。

## 汇报

### westd-11672 GPU 分配状态（全满）

| GPU | 显存占用 | 任务 | 备注 |
|-----|---------|------|------|
| cuda:0 | 58.7GB/97.9GB | `grpo_rasp_rlvr_20_qwen_math` (训练) | PID 32087，已有 |
| cuda:1 | 55.8GB/97.9GB | `grpo_standard_25` (训练) | PID 32427，已有 |
| cuda:2 | 36.9GB/97.9GB | `eval_pass_k8_standard_20_grpo_qwen_math` (已有) + **eval_grpo_rasp_25** (新启) | 共存无冲突 |
| cuda:3 | 11.8GB/97.9GB | **eval_sft_rasp_25** (新启) | N=1319 full eval |

### 新启动实验

1. **cuda:2 — eval_grpo_rasp_25** (N=1319, full GSM8K, greedy)
   - 模型: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25`
   - 输出: `results/eval_grpo_rasp_25.json`
   - 意义: 论文核心数据——验证 25% RASP 剪枝后 GRPO 恢复的 accuracy

2. **cuda:3 — eval_sft_rasp_25** (N=1319, full GSM8K, greedy)
   - 模型: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25`
   - 输出: `results/eval_sft_rasp_25.json`
   - 意义: SFT recovery baseline，之前的 run 在 163/1319 中断

### 可用模型 checkpoint 全列表

**GRPO 输出:**
- `grpo_rasp_25`, `grpo_rasp_25_qwen_math`, `grpo_rasp_qwen_math`, `grpo_rasp_rlvr_20_qwen_math`
- `grpo_standard_25`, `grpo_standard_25_qwen_math`, `grpo_standard_qwen_math`
- `grpo_standard_v8_step50`, `grpo_unpruned_v2`

**Pruned 模型:**
- `pruned_rasp_25`, `pruned_rasp_25_qwen_math`, `pruned_rasp_20`
- `pruned_standard_25`, `pruned_standard_25_qwen_math`, `pruned_standard_20`
- `pruned_qwen_math_rasp_20`, `pruned_qwen_math_standard_20`
- `pruned_rasp_rlvr_20`, `pruned_rasp_rlvr_20_qwen_math`

**SFT 模型:**
- `sft_rasp_25`, `sft_rasp_25.log`, `sft_rasp_20_westd`
- `sft_standard_25`, `sft_standard_20_westd`
- `sft_qwen_math_rasp_20/25`, `sft_qwen_math_standard_20/25`
- `sft_rasp_rlvr_20_qwen_math`, `sft_unpruned_baseline`

### 未启动原因

- **cuda:0**: 被 `grpo_rasp_rlvr_20_qwen_math` 训练占满，无法另行分配
- 原计划的 eval_grpo_rasp_25 改在 cuda:2 上跑（与已有 pass@8 eval 共存，显存充足）

---
