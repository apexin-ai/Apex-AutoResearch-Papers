# research westb1 experiment proposal

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_westb1_experiment_proposal_20260519T182410_result.json`
- **Structured JSON:** [`4fb04fdf45cc37461630.json`](../../sessions/4f/4fb04fdf45cc37461630.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## westb 当前状态

| GPU | 占用 | 实验 |
|-----|------|------|
| westb:0 | 4323 MiB | `eval_humaneval_sft_rasp_20_1p5b_2048` (PID 909411) |
| westb:1 | **0 MiB — 空闲** | — |

## westb 上所有可用 checkpoint

**1.5B 系列 (每个 ~2.8G):**
| Checkpoint | 类型 |
|---|---|
| `pruned_cka_only_20_1p5b` | post-prune |
| `pruned_rasp_20_1p5b` | post-prune |
| `pruned_standard_20_1p5b` | post-prune |
| `sft_cka_only_20_1p5b` | SFT recovery |
| `sft_rasp_20_1p5b` | SFT recovery |
| `sft_standard_20_1p5b` | SFT recovery |
| `grpo_cka_only_20_1p5b` | GRPO recovery |
| `grpo_rasp_20_1p5b` | GRPO recovery |
| `grpo_standard_20_1p5b` | GRPO recovery |

**7B 系列 (每个 ~11-12G):**
sft/grpo/pruned × {cka_only_20, random_20, rasp_25, standard_25, rasp_rlvr_20, gradient_20} + `grpo_cka_only_20_seed123` (38G, 含多 checkpoint)

## Registry 缺口分析

**1.5B HumanEval 矩阵 — 差 1 个:**
- ✅ sft_cka_only (0.61%), sft_standard (0.61%), grpo_cka_only (0%), grpo_standard (done)
- 🔄 sft_rasp → westb:0 正在跑
- ❌ **grpo_rasp** → 未跑，checkpoint 在 westb

**MBPP 7B 矩阵 — 差 4 个:**
- ✅ Dense (53.48%), GRPO CKA-only (14.17%)
- 🔄 GRPO Standard → westd:2 正在跑
- ❌ **SFT CKA-only, SFT Standard, SFT RASP, GRPO RASP** → 全未跑，7B checkpoint 都在 westb

**CKA scoring stability (plan_014):** `run_cka_reliability.py` 代码存在，但 registry 中无 plan_014 实验记录。之前 `scoring_ablation_batch_v2` 失败（磁盘满）。代码 ready，需要 base model。

---

## 建议方案

**方案 A（推荐）：先快后慢，两阶段**

**阶段 1** — `eval_humaneval_grpo_rasp_20_1p5b_2048`（westb:1）
- 1.5B 模型仅 2.8G，HumanEval 164 题，预计 ~20-30 min
- 补全 1.5B HumanEval 矩阵最后一格
- Hypothesis: GRPO RASP 1.5B HumanEval ≈ 0%（与其他 1.5B 方法一致，1.5B 模型容量不足以做 code gen）

```bash
CUDA_VISIBLE_DEVICES=1 python src/eval_humaneval.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b \
  --max_new_tokens 2048 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_1p5b_2048.json \
  --seed 42
```

**阶段 2** — `eval_mbpp_sft_cka_only_20`（westb:1，阶段1完成后）
- MBPP P0 矩阵最关键的一格：CKA-only SFT
- 7B 模型 12G，可放入 westb:1
- Hypothesis: SFT CKA-only MBPP > SFT Standard/RASP（与 GSM8K/HumanEval 一致的 capability breadth 优势）

```bash
CUDA_VISIBLE_DEVICES=1 python src/eval_mbpp.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20.json \
  --max_new_tokens 2048 --seed 42
```

**方案 B（如果 Director 想优先 plan_014）：** CKA reliability ablation 代码 ready，但需要确认 base model（`models/` 目录 3.4G）和校准数据集是否完整。之前 `scoring_ablation_batch_v2` 因磁盘满失败，需确认 `/root/autodl-tmp/` 空间足够。

**建议走方案 A** — 两个 eval 都是 ROADMAP P0 的 MBPP 矩阵和 1.5B cross-scale 补全，直接填论文表格。

---
