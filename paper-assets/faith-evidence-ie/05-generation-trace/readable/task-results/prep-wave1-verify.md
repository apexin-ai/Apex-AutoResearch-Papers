# prep wave1 verify

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_wave1_verify_20260518T090632_result.json`
- **Structured JSON:** [`efad1624bd28dc4852a0.json`](../../sessions/ef/efad1624bd28dc4852a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。以下是汇总：

---

## 脚本验证结果

### sft_seed43.sh: **问题 x2**
1. **[CRITICAL] GPU 冲突**: `CUDA_VISIBLE_DEVICES=0,1,2,3` + `accelerate_4gpu.yaml` (num_processes=4, DeepSpeed ZeRO-2) — 占用全部 4 卡。按计划应只用 cuda:0，但 SFT 原本就是 4 卡分布式训练，单卡跑不了这个 accelerate config。**两个 SFT 和 GRPO/RSFT 无法同时运行。**
2. **[MISSING] 无 save_total_limit** — 可能保留所有 checkpoint

### sft_seed44.sh: **问题 x2**
同 sft_seed43.sh（CUDA_VISIBLE_DEVICES=0,1,2,3 + 无 save_total_limit）

### grpo_bf16_g4.sh: **问题 x2**
1. **[WRONG GPU]** `CUDA_VISIBLE_DEVICES=0`，按计划应为 `2`
2. **[HIGH]** `save_total_limit=10`，应为 `2`（200 steps / save_every 20 = 10 checkpoints 全保留，bf16 无量化 checkpoint 更大）
3. (minor) 缺 `--wandb_project`

### random_rsft.sh: **问题 x3**
1. **[BUG] 路径错误**: `python /tmp/d102_next_batch/random_rsft_select.py` — 脚本实际在 `/root/autodl-tmp/freige/scripts/d102_next_batch/random_rsft_select.py`，运行时会 FileNotFoundError
2. **[WRONG GPU]** `CUDA_VISIBLE_DEVICES=1`，按计划应为 `3`
3. **[HIGH]** `save_total_limit=5`，应为 `2`

### random_rsft_select.py: **OK**
- 逻辑正确：按 doc_id 分组，每组随机选 1 个，seed=42
- 21968 candidates / 2716 unique docs → 选出 2716 samples（与 CED k=1 同维度，都是 per-doc 选 1）
- 输出格式与 rsft_trainer 兼容

### Dry-run 导入: **OK**
- SFT OK, GRPO OK, RSFT OK（vLLM 版本 warning 不影响训练）

### 路径存在性: **OK**
- `/root/autodl-tmp/models/Qwen3-4B` ✓
- `/root/autodl-tmp/data/docred` ✓
- `/root/autodl-tmp/sft_output` (adapter) ✓
- `/root/autodl-tmp/rsft_generations/generations.jsonl` ✓
- 4 个输出目录均不存在，无覆盖风险 ✓

---

## 磁盘预估
| 实验 | 预估 |
|---|---|
| sft_seed43 (参考 sft_output=5.8G) | ~6GB |
| sft_seed44 | ~6GB |
| grpo_bf16_g4 (bf16 LoRA, save_total_limit 若改为 2) | ~3GB |
| random_rsft (参考 rsft_output_ced_s43=8G, save_total_limit 若改为 2) | ~4GB |
| **合计** | **~19GB** |

当前可用 148GB，**充足**。

---

## 核心问题需决策

**SFT 4 卡 vs 4 实验并行矛盾**：两个 SFT 脚本设计为 4 卡 DeepSpeed 训练，与 GRPO/RSFT 占用的卡冲突。可选方案：
- **A**: SFT 串行跑（seed43 → seed44，各用 4 卡，~2h x2），完成后再并行跑 GRPO (cuda:2) + RSFT (cuda:3)
- **B**: 改 SFT 为单卡训练（去掉 accelerate，改 batch size / gradient accumulation），4 实验真正并行
- **C**: SFT 用 2 卡（seed43 用 0,1; seed44 用 2,3），GRPO/RSFT 等 SFT 完成后再跑

---
