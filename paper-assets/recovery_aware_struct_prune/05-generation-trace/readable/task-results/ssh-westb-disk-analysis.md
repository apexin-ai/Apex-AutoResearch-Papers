# ssh westb disk analysis

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_disk_analysis_20260523T124345_result.json`
- **Structured JSON:** [`133301432962a7383f92.json`](../../sessions/13/133301432962a7383f92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是分析结果：

---

```
总体: 241G/250G (97%) — 仅剩 9.2G

大目录:
- /root/autodl-tmp/recovery_aware_struct_prune/: 226G (本项目)
- /root/autodl-tmp/models/Qwen2.5-Math-7B:       15G  (基座模型)
- /root/autodl-tmp/data/:                          1.5G
- /root/autodl-tmp/logs/:                          64M
```

### recovery_aware_struct_prune 子目录明细 (226G)

| 目录 | 大小 | 有 final model? | 有 checkpoint? |
|------|------|-----------------|----------------|
| **7B 模型 (~12G/个)** | | | |
| grpo_qwen_math_cka_only_20 | **24G** | ✅ model.safetensors | checkpoint-100 (12G 冗余) |
| grpo_rasp_alpha0p5_20 | **23G** | ✅ model.safetensors | checkpoint-100 (~11G 冗余) |
| grpo_cka_only_20 | 12G | ❌ | checkpoint-100 (即最终模型) |
| grpo_cka_only_20_seed123 | 12G | ✅ model.safetensors | 无 |
| sft_rasp_rlvr_20 | 12G | ❌ | checkpoint-1870 (即最终模型) |
| sft_rasp_alpha3p0_20 | 12G | ❌ | checkpoint-935 (即最终模型) |
| sft_random_20 | 12G | — | — |
| sft_cka_only_20 | 12G | — | — |
| pruned_rasp_rlvr_20 | 12G | — | — |
| pruned_standard_25 | 11G | — | — |
| pruned_cka_only_20_qwen_math | 12G | — | — |
| pruned_standard_20_qwen_math | 12G | — | — |
| sft_qwen_math_cka_only_20_final | 12G | — | — |
| sft_standard_20_qwen_math_final | 12G | — | — |
| pruned_rasp_alpha3p0_20 | 12G | — | — |
| **1.5B 模型 (~2.8G/个)** | | | |
| pruned_standard_20_1p5b | 2.8G | — | — |
| pruned_cka_only_20_1p5b | 2.8G | — | — |
| pruned_rasp_20_1p5b | 2.8G | — | — |
| sft_cka_only_20_1p5b | 2.8G | — | — |
| sft_standard_20_1p5b | 2.8G | — | — |
| sft_rasp_20_1p5b | 2.8G | — | — |
| grpo_cka_only_20_1p5b | 2.8G | ❌ | checkpoint-100 |
| grpo_standard_20_1p5b | 2.8G | ✅ | 无 |
| grpo_rasp_20_1p5b | 2.8G | ❌ | checkpoint-100 |
| **其他** | | | |
| grpo_alpha4_20_eval | 2.9G | ✅ | 无 |
| models/DeepSeek-R1-Distill-Qwen-1.5B | 3.4G | — | — |
| **空/废弃** | | | |
| grpo_random_20_seed456 | 0 | — | 空目录 |
| grpo_rasp_alpha3p0_20 | 132K | — | 仅 completions |

---

### 可安全删除（本项目）

| 路径 | 大小 | 原因 |
|------|------|------|
| `grpo_qwen_math_cka_only_20/checkpoint-100/` | **~12G** | 冗余中间 checkpoint，final model 已存在于根目录 |
| `grpo_rasp_alpha0p5_20/checkpoint-100/` | **~11G** | 同上 |
| `grpo_random_20_seed456/` | 0 | 空目录，无任何文件 |
| `grpo_rasp_alpha3p0_20/` | 132K | 近乎空目录，仅 completions，无模型文件 |

### 需确认后可删除

| 路径 | 大小 | 需确认 |
|------|------|--------|
| `models/Qwen2.5-Math-7B` | **15G** | 是否仍需要此基座模型？如 Qwen-Math 实验已完成且不再需要重新剪枝，可删 |
| `pruned_standard_25/` | **11G** | 25% 剪枝率实验，其他均为 20%，是否为已弃用的旧实验？ |

### 不可删除

| 路径 | 大小 | 原因 |
|------|------|------|
| 所有含 final model 的 `grpo_*/sft_*/pruned_*` 目录 | ~190G | 论文实验所需的最终模型 |
| `models/DeepSeek-R1-Distill-Qwen-1.5B` | 3.4G | 1.5B 实验基座模型 |

---

```
确定可释放:   ~23G  (两个冗余 checkpoint)
确认后可释放: ~26G  (Qwen-Math-7B 基座 + pruned_standard_25)
清理后剩余:   ~32-58G 可用空间 (从 9.2G 提升)
```

---
