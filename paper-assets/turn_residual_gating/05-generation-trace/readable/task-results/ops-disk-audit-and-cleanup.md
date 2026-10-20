# ops disk audit and cleanup

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_audit_and_cleanup_20260519T072033_result.json`
- **Structured JSON:** [`a883d7aec527c088bbfa.json`](../../sessions/a8/a883d7aec527c088bbfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认 `Qwen2.5-7B-Instruct` 是指向 `Qwen2___5-7B-Instruct` 的符号链接（同一 inode），实际只占 15G。

---

## 磁盘审计报告

### 总体状态

| 指标 | 值 |
|---|---|
| 总容量 | 30G |
| 已用 | 25G (82%) |
| **可用** | **5.6G** |
| Llama-3.1-8B-Instruct 需要 | ~16G |
| **缺口** | **~10.4G** |

### Runs 目录审计

| 目录 | 大小 | 状态 | 可删除？ |
|---|---|---|---|
| `runs/phase2_tg_s42/` | 不存在 | v1, 已清理 | — |
| `runs/phase2_tg_s42_v2/` | 不存在 | killed, 已清理 | — |
| `runs/phase2_tg_s42_v3/` | 不存在 | negative, 已清理（仅留 log） | — |
| `runs/phase2_tg_s42_v3b/` | **23M** | success, superseded by v7 | 待确认 |
| `runs/phase2_tg_s42_v4/` | 不存在 | failed, 已清理（仅留 log） | — |
| `runs/phase2_tg_s42_v4_dryrun/` | **23M** | dryrun | 待确认 |
| `runs/phase2_tg_s42_v5/` | 不存在 | negative, 已清理 | — |
| `runs/phase2_tg_s42_v6/` | **23M** | negative | 待确认 |
| `runs/phase2_tg_s42_v7/` | 91M | **success, 保留** | 否 |
| `runs/phase2_ug_s42/` | 91M | **success, 保留** | 否 |
| `runs/phase2_lora_only_s42/` | 不存在 | 未开始 | — |

**旧 runs 可释放：~69M** — 杯水车薪。

### 缓存目录（关键）

| 目录 | 大小 | 说明 | 可删除？ |
|---|---|---|---|
| `modelscope/Qwen/Qwen2___5-7B-Instruct/` | **15G** | 基座模型（训练/eval 用） | **待确认** |
| `modelscope/hub/.../Meta-Llama-3___1-8B-Instruct/` | 11M | 下载失败残留 | 是 |
| `huggingface/hub/models--Qwen--Qwen2.5-7B-Instruct/` | 551M | tokenizer/config 缓存 | 待确认 |
| `huggingface/hub/datasets--HuggingFaceH4--ultrachat_200k/` | **1.6G** | 训练数据集缓存 | 待确认 |

### 结论

1. **删除旧 runs (v3b/v4_dryrun/v6) 只能释放 ~69M，远不够。**

2. **唯一能腾出足够空间的方案是清理 Qwen 模型缓存（15G）：**
   - 如果 v7 和 UG 的 eval 已完成，且不再需要跑新实验，可以删除
   - 删除 Qwen 缓存 (15G) + ultrachat 数据集 (1.6G) + 旧 runs (69M) + Llama 残留 (11M) → 释放 **~16.7G**
   - 加上现有 5.6G 可用 → 总可用 **~22.3G**，足够下载 Llama-3.1

3. **如果 Qwen 模型仍需保留，则当前磁盘无法容纳 Llama-3.1，需要扩容或换盘。**

---
