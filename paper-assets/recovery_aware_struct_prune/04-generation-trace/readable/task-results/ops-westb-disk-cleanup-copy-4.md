# ops westb disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_disk_cleanup_20260520T092509_result.json`
- **Structured JSON:** [`525d4e521649350d8a08.json`](../../sessions/52/525d4e521649350d8a08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

探查完毕。情况比预期复杂——没有 optimizer 文件可清，也没有损坏的 checkpoint。

## 磁盘现状

| 区域 | 大小 |
|------|------|
| 总计已用 | 218G / 250G |
| 当前可用 | **33G** |
| 需释放 | **≥67G** |

## 预期的"快速清理"不可用

- **optimizer.pt**：所有 checkpoint 都没有 optimizer 文件，已是最精简状态
- **损坏的 checkpoint-1870**：不存在。`sft_qwen_math_cka_only_20` 只有 `checkpoint-935`（12G，model.safetensors 正常）

## 空间分布

**项目外** (30G)：
| 目录 | 大小 | 说明 |
|------|------|------|
| `DeepSeek-R1-Distill-Qwen-7B/` | 15G | base 7B 模型，可重新下载 |
| `models/Qwen2.5-Math-7B/` | 15G | base Qwen-Math 模型，可重新下载 |

**项目内 7B 实验** (每个 ~12G，共 14 个 ≈ 160G)：
| 目录 | 大小 | 说明 |
|------|------|------|
| `pruned_standard_25` | 11G | 25% Standard 剪枝 |
| `sft_standard_25` | 11G | ↑ 的 SFT (完成) |
| `pruned_rasp_rlvr_20` | 12G | 20% RASP-RLVR 剪枝 |
| `sft_rasp_rlvr_20` | 12G | ↑ 的 SFT (完成) |
| `pruned_cka_only_20` | 12G | 20% CKA 剪枝 |
| `sft_cka_only_20` | 12G | ↑ 的 SFT (完成) |
| `grpo_cka_only_20` | 12G | ↑ 的 GRPO (完成) |
| `pruned_standard_20` | 12G | 20% Standard 剪枝 |
| `pruned_rasp_20` | 12G | 20% RASP 剪枝 |
| `grpo_cka_only_20_seed123` | 12G | CKA GRPO seed=123 |
| `pruned_cka_only_20_qwen_math` | 12G | CKA Qwen-Math 剪枝 |
| `pruned_standard_20_qwen_math` | 12G | Standard Qwen-Math 剪枝 |
| `sft_qwen_math_cka_only_20` | 12G | CKA Qwen-Math SFT (**半途崩溃**, checkpoint-935/1870) |
| `sft_standard_20_qwen_math` | 12G | Standard Qwen-Math SFT (**半途崩溃**, checkpoint-935/1870) |

**项目内 1.5B 实验** (每个 ~2.8G，共 9 个 ≈ 25G)：
pruned/sft/grpo × standard/cka/rasp 各一个

## 需要你决定

仅靠删 base 模型（可重新下载）能回收 **30G**，达到 63G 可用，仍不够 100G。

请告知以下哪些可以删除：
1. **`DeepSeek-R1-Distill-Qwen-7B/`** (15G) — base 7B 模型
2. **`models/Qwen2.5-Math-7B/`** (15G) — base Qwen-Math 模型
3. **两个崩溃的 SFT checkpoint** (`sft_qwen_math_cka_only_20` + `sft_standard_20_qwen_math`, 各 12G = 24G) — 删除意味着 SFT 需从 step 0 重新跑，不能从 935 恢复
4. **25% 剪枝实验** (`pruned_standard_25` + `sft_standard_25`, 22G) — 如果不再需要 25% 剪枝率的结果
5. **旧 DeepSeek 实验中的冗余目录** — 如 `pruned_standard_20`/`pruned_rasp_20`（没有对应的 SFT/GRPO，各 12G = 24G）
6. **`grpo_cka_only_20_seed123`** (12G) — seed 实验

删 1+2+3 可达 **~96G 可用**，接近目标。再加任意一个就超过 100G。

---
