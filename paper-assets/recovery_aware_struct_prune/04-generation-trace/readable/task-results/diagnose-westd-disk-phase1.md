# diagnose westd disk phase1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_disk_phase1_20260521T182334_result.json`
- **Structured JSON:** [`f1ab6afdcc18f8c5cc9a.json`](../../sessions/f1/f1ab6afdcc18f8c5cc9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整诊断报告。

---

## 磁盘总况

| 指标 | 值 |
|------|-----|
| 总容量 | 619G |
| 已用 | 619G (**100%**) |
| 可用 | 4.0M |
| 项目目录占用 | 605G |
| DeepSeek 基础模型 | 15G |

## sft_warmup.py 保存参数

`save_strategy="epoch"`，最终 `trainer.save_model()` + `tokenizer.save_pretrained()`。**未使用 `save_only_model` 或 `save_total_limit`**，所以 sft_alpha4_20/ 内含 checkpoint-468 子目录（optimizer state 等冗余文件，导致 27G 而非 ~12G）。

## 正在被 eval 使用的模型（不可删）

| 模型路径 | PID | GPU |
|----------|-----|-----|
| `grpo_stage2_standard_20_fair` | tmux session (May19) | cuda:1 |
| `grpo_random_20/checkpoint-100` | 382472 | cuda:1 |
| `sft_random_20` | 385685 | cuda:3 |

---

## 目录分类清单

### 预批准删除

#### [ShortGPT] — 39G
| 目录 | 大小 |
|------|------|
| shortgpt_20/ | 13G |
| sft_shortgpt_20/ | 13G |
| grpo_shortgpt_20/ | 13G |

#### [1.5B] — 16.8G
| 目录 | 大小 |
|------|------|
| grpo_cka_only_20_1p5b/ | 2.8G |
| grpo_rasp_20_1p5b/ | 2.8G |
| grpo_standard_20_1p5b/ | 2.8G |
| sft_cka_only_20_1p5b/ | 2.8G |
| sft_rasp_20_1p5b/ | 2.8G |
| sft_standard_20_1p5b/ | 2.8G |

#### [α=4.0 残留] — 27G
| 目录 | 大小 | 备注 |
|------|------|------|
| sft_alpha4_20/ | 27G | 含 checkpoint-468 子目录（无 save_only_model，含 optimizer state） |

#### [Qwen-Math] — 116G
| 目录 | 大小 |
|------|------|
| pruned_qwen_math_rasp_20/ | 12G |
| pruned_qwen_math_standard_20/ | 12G |
| pruned_rasp_25_qwen_math/ | 11G |
| pruned_standard_25_qwen_math/ | 11G |
| pruned_rasp_rlvr_20_qwen_math/ | 12G |
| sft_qwen_math_rasp_20/ | 12G |
| sft_qwen_math_rasp_25/ | 11G |
| sft_qwen_math_standard_20/ | 12G |
| sft_qwen_math_standard_25/ | 11G |
| sft_rasp_rlvr_20_qwen_math/ | 12G |

#### [旧版被取代] — 53G
| 目录 | 大小 | 原因 |
|------|------|------|
| grpo_cka_only_20/ | 12G | 被 seed456 版取代 |
| grpo_standard_15_seed123_v3/ | 13G | _v3 旧版 |
| grpo_standard_15_seed456_v3/ | 13G | _v3 旧版 |
| grpo_unpruned_v2/ | 15G | _v2 旧版 |

#### [pruned 中间产物] — 36G
| 目录 | 大小 |
|------|------|
| pruned_standard_20/ | 12G |
| pruned_rasp_20/ | 12G |
| pruned_random_20/ | 12G |

### **预批准删除合计：~288G**

---

### 保留

| 目录 | 大小 | 原因 |
|------|------|------|
| /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/ | 15G | 基础模型 |
| pruned_alpha4_20/ | 12G | 明确保留 |
| grpo_random_20/ | 12G | eval 进行中 (PID 382472) |
| sft_random_20/ | 12G | eval 进行中 (PID 385685) |
| grpo_stage2_standard_20_fair/ | 12G | eval 进行中 (tmux) |

---

### 未分类（需 Director 决策）

#### 可能是最终版 SFT+GRPO checkpoint（15%/20%/25%/30%）

| 目录 | 大小 | 推测类别 |
|------|------|----------|
| grpo_cka_only_15_seed123/ | 14G | 15% GRPO seed |
| grpo_cka_only_15_seed456/ | 13G | 15% GRPO seed |
| grpo_cka_only_20_seed456/ | 12G | 20% GRPO seed |
| grpo_cka_only_25/ | 11G | 25% GRPO |
| grpo_rasp_20_seed456/ | 12G | 20% GRPO seed |
| grpo_rasp_25/ | 11G | 25% GRPO |
| grpo_stage2_rasp_20_fair/ | 12G | 20% fair GRPO |
| grpo_standard_20_seed123/ | 12G | 20% GRPO seed |
| grpo_standard_20_seed456/ | 12G | 20% GRPO seed |
| grpo_standard_25/ | 11G | 25% GRPO |
| pruned_cka_only_15/ | 13G | 15% pruned |
| pruned_cka_only_25/ | 11G | 25% pruned |
| pruned_cka_only_30/ | 11G | 30% pruned |
| pruned_rasp_25/ | 11G | 25% pruned |
| pruned_standard_15/ | 13G | 15% pruned |
| pruned_standard_25/ | 11G | 25% pruned |
| pruned_standard_30/ | 11G | 30% pruned |
| sft_cka_only_15/ | 13G | 15% SFT |
| sft_cka_only_20/ | 12G | 20% SFT |
| sft_cka_only_25/ | 11G | 25% SFT |
| sft_rasp_20_westd/ | 12G | 20% SFT |
| sft_rasp_25/ | 11G | 25% SFT |
| sft_standard_15/ | 13G | 15% SFT |
| sft_standard_20/ | 12G | 20% SFT |
| sft_standard_25/ | 11G | 25% SFT |

#### 小目录（可忽略）
| 目录 | 大小 |
|------|------|
| artifacts/ | 4.0K |
| logs/ | 2.4M |
| results/ | 55M |
| wandb/ | 78M |
| grpo_rasp_25_transfer_log/ | 0 |

**未分类合计：~295G**（其中 25 个目录，多数疑似论文最终实验所需）

---

## 小结

- 预批准可删：**~288G**（30 个目录），删除后磁盘使用率降至约 53%
- 保留：63G（5 个目录）
- 未分类：~295G（25 个模型目录 + 5 个小目录），需 Director 判断哪些是论文最终版

---
