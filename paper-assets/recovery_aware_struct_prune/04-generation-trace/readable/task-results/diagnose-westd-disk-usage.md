# diagnose westd disk usage

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_disk_usage_20260521T173835_result.json`
- **Structured JSON:** [`fd23f510190469f427f1.json`](../../sessions/fd/fd23f510190469f427f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘使用报告

**总量**: 619G/619G (100% 满, 仅剩 212K)

### Top-level 分布

| 目录 | 大小 |
|------|------|
| recovery_aware_struct_prune/ | **605G** |
| DeepSeek-R1-Distill-Qwen-7B/ | **15G** |
| .hf_cache/ | 86M |
| 其他 | ~7M |

### recovery_aware_struct_prune 内部 (~50 个模型目录, 每个 10-15G)

按类别：
- **pruned_* (剪枝基础模型)**: ~16个, 合计 ~185G
- **sft_* (SFT 微调模型)**: ~15个, 合计 ~175G
- **grpo_* (GRPO 模型)**: ~20个, 合计 ~228G
- **shortgpt_20 + sft/grpo**: 3个, ~39G
- **1.5B 系列** (6个 × 2.8G): ~17G

---

### 可安全清理的候选

| 候选 | 大小 | 风险 | 说明 |
|------|------|------|------|
| **pruned_alpha4_20/** | **9.7G** | 无 | α=4.0 pipeline 因磁盘满失败的残留，model.safetensors 可能不完整 |
| **grpo_standard_15_seed123/** | 212K | 无 | 几乎为空，失败的 run |
| **grpo_standard_15_seed456/** | 208K | 无 | 几乎为空，失败的 run |
| **grpo_standard_15/** | 104K | 无 | 几乎为空，失败的 run |
| **grpo_standard_15_seed123_v4/** | 0 | 无 | 空目录 |
| **grpo_standard_15_seed456_v4/** | 0 | 无 | 空目录 |
| **grpo_cka_only_15/** | **3.7G** | 低 | 仅有 checkpoint-20 (3.7G 的 model.safetensors)，被 v2/seed 版本取代 |
| **sft_standard_20_westd/** | 12K | 无 | 几乎为空 |
| 7个空目录 (eval_results, outputs, src 等) | 0 | 无 | 空目录 |
| **小计** | **~13.4G** | | |

### 需要确认的候选（释放更多空间）

| 候选 | 大小 | 风险 | 说明 |
|------|------|------|------|
| **DeepSeek-R1-Distill-Qwen-7B/** | **15G** | 中 | 基础模型，可从 ModelScope 重新下载 |
| **grpo_cka_only_15_v2/** | 13G | 中 | 如已被 seed456/seed123 取代 |
| **grpo_standard_15_v2/** | 13G | 中 | 如已被 v3 seed 版本取代 |
| **sft_unpruned_baseline/** | 0 | 无 | 空目录 |
| **pruned_rasp_rlvr_20/** | 0 | 无 | 空目录（qwen_math 版本存在，此目录为空） |

---

### Eval 运行状态

两个 eval 进程**正常运行中**：
- PID 382472: `eval_math500_grpo_random_20_v2` (RSS 2.0G) — 读取 grpo_random_20/checkpoint-100
- PID 385685: `eval_math500_sft_random_20` (RSS 2.1G) — 读取 sft_random_20

输出写到 `/root/runs/`（根分区），不写数据盘，**不受磁盘满影响**。但 `grpo_random_20` 和 `sft_random_20` 在 eval 完成前**不能删除**。

### α=4.0 残留

`pruned_alpha4_20/` 含 config.json + generation_config.json + model.safetensors (9.7G)。safetensors 文件在 01:33 写入完成（大小 10344202240 字节），看起来写入**完成了**（与 DeepSeek-R1-Distill-Qwen-7B 原始模型同一大小），但因后续步骤失败（缺 tokenizer 等文件），这个目录仍然不完整。**可安全删除并重新运行 pipeline**。

---

### 建议操作优先级

1. **立即清理** pruned_alpha4_20 + 失败/空目录 → 回收 ~13.4G
2. **确认后清理** DeepSeek base model → 额外 15G
3. **确认后清理** 被取代的 v2 版本 → 额外 ~26G
4. 如仍需更多空间，需判断哪些实验已完成不再需要

---
