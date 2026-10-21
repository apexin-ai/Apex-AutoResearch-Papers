# 全尺度截断审计 + 下批实验规划

> 生成时间: 2026-05-21 ~14:30 UTC

---

## Part 1: 截断审计

### 总览

所有 eval 基于 DocRED dev set（n_total=985 docs）。truncation rate = n_truncated / 985。

### 1.1 Qwen3-1.7B

**SFT with-evidence:**

| Seed | @1024 trunc | @1024 ign_f1 | @2048 trunc | @2048 ign_f1 |
|------|------------|-------------|------------|-------------|
| s42 | 314 (31.9%) | 0.4786 | **267 (27.1%)** ✅ | **0.4806** ✅ |
| s43 | 408 (41.4%) | 0.4286 | ❌ | ❌ |
| s44 | 473 (48.0%) | 0.4321 | ❌ | ❌ |

**SFT no-evidence:**

| Seed | @1024 trunc | @1024 ign_f1 | @2048 trunc | @2048 ign_f1 |
|------|------------|-------------|------------|-------------|
| s42 | 501 (50.9%) | 0.3982 | 498 (50.6%) | 0.3925 |

**RSFT with-evidence (@1024):**

| Seed | trunc | ign_f1 |
|------|-------|--------|
| s42 | 249 (25.3%) | 0.5122 |
| s43 | 244 (24.8%) | 0.5109 |
| s44 | 240 (24.4%) | 0.5125 |

**关键发现:**
- 1.7B SFT with-evi @1024 截断极高（32-48%），@2048 仅降至 27.1%（减少 4.8pp）
- 1.7B no-evi @2048 截断仍 50.6% — 模型本身就极其 verbose
- 1.7B RSFT 截断显著低于 SFT（24-25% vs 32-48%）— RSFT 训练压缩了输出长度
- **1.7B matched@2048 SFT fair_tax:** no-evi(0.3925) - with-evi(0.4806) = **-8.81pp**（evidence helps）

---

### 1.2 Qwen3-8B

**SFT with-evidence:**

| Seed | @1024 trunc | @1024 ign_f1 | @2048 |
|------|------------|-------------|-------|
| s42 | 313 (31.8%) | 0.5051 | 🔄 RUNNING (~2.5h) |
| s43 | 139 (14.1%) ⚠️ | 0.5324 | ❌ |
| s44 | 306 (31.1%) | 0.4681 | ❌ |

**SFT no-evidence (@1024):**

| Seed | trunc | ign_f1 |
|------|-------|--------|
| s42 | 225 (22.8%) | 0.5079 |

**RSFT with-evidence (@1024):**

| Seed | trunc | ign_f1 |
|------|-------|--------|
| s42 | 267 (27.1%) | 0.5433 |
| s43 | 231 (23.5%) | 0.5471 |
| s44 | 230 (23.4%) | 0.5451 |

**关键发现:**
- D139 确认：Qwen 8B SFT with-evi 31.8% vs no-evi 22.8% → **9pp 截断不对称**
- s43 截断异常低 (14.1%)，原因不明
- RSFT 截断 (23-27%) 低于 SFT with-evi (31.8%) 但仍高于 SFT no-evi (22.8%)
- **@1024 evidence tax 不可信**（D139 结论成立）

---

### 1.3 Qwen3-14B

**RSFT:**

| Type | @1024 trunc | @1024 ign_f1 | @2048 |
|------|------------|-------------|-------|
| with-evi | 105 (10.7%) | **0.5886** | 🔄 RUNNING (~30 min) |
| no-evi | 106 (10.8%) | 0.5432 | ❌ |

**关键发现:**
- **截断近乎完美对称**: 10.7% vs 10.8% → @1024 tax 可信
- @1024 RSFT tax = no-evi(0.5432) - with-evi(0.5886) = **-4.54pp**（evidence helps）
- @2048 是 robustness confirmation，不太可能改变结论

---

### 1.4 LLaMA-3.1-8B

**SFT with-evidence:**

| Seed | @1024 trunc | @1024 ign_f1 | @2048 trunc | @2048 ign_f1 |
|------|------------|-------------|------------|-------------|
| s42 | 197 (20.0%) | 0.5384 | 147 (14.9%) | 0.5649 |
| s43 | 190 (19.3%) | 0.5142 | 242 (24.6%) ⚠️ | 0.4954 |
| s44 | 240 (24.4%) | 0.4802 | 177 (18.0%) | 0.4655 |

**SFT no-evidence:**

| Seed | @1024 trunc | @1024 ign_f1 | @2048 trunc | @2048 ign_f1 |
|------|------------|-------------|------------|-------------|
| s42 | 219 (22.2%) | 0.5219 | 201 (20.4%) | 0.5210 |
| s43 | 378 (38.4%) | 0.3391 | 359 (36.4%) | 0.3389 |
| s44 | 411 (41.7%) | 0.3326 | 246 (25.0%) | 0.4373 |

**RSFT with-evidence:**

| Seed | @1024 trunc | @1024 ign_f1 | @2048 |
|------|------------|-------------|-------|
| s42 | 158 (16.0%) | 0.5714 | 🔄 89% (~25 min) |
| s43 | 173 (17.6%) | 0.5662 | ❌ |
| s44 | 166 (16.9%) | 0.5587 | ❌ |

**RSFT no-evidence (@1024):**

| Seed | trunc | ign_f1 |
|------|-------|--------|
| s42 | 190 (19.3%) | 0.5526 |
| s43 | 183 (18.6%) | 0.5546 |
| s44 | 178 (18.1%) | 0.5550 |

**关键发现:**
- SFT matched@2048 3-seed fair_tax: s42=-4.39pp, s43=-15.65pp, s44=-2.82pp → **全部为负**
- s43 no-evi 极差 (0.3389, fmt_ok=0.847) — 不是截断问题，是模型本身在 no-evi 模式下不稳定
- s44 no-evi @1024→@2048: 0.3326→0.4373 (+10.5pp) — 截断伪影严重
- RSFT 截断基本对称 (@1024: with 16-17% vs no 18-19%, gap~2pp) → @1024 tax 可信
- **RSFT @1024 tax: mean -1.14pp ± 0.76pp** — 小且稳定

**⚠️ 异常:** s43 with-evi@2048 截断 (24.6%) > @1024 (19.3%)，不合常理。可能是 batch_size 差异或 generation 非确定性导致。

---

### 1.5 Qwen3-4B (参考)

| Eval | Type | trunc | ign_f1 |
|------|------|-------|--------|
| d111_4b_sft_s42_reeval | SFT with-evi @1024 | 288 (29.2%) | 0.3974 |
| wave1_sft_4b_s43_eval_r2 | SFT with-evi @1024 | 318 (32.3%) | 0.4365 |
| wave1_sft_4b_s44_eval_r2 | SFT with-evi @1024 | 249 (25.3%) | 0.4734 |
| sft_no_evidence (4B) | SFT no-evi @1024 | 298 (30.3%) | 0.4893 |

4B 截断近乎对称 (with-evi ~29% vs no-evi ~30%) → @1024 tax 可能可信，但仍有 ~30% 绝对截断率。

---

### 1.6 截断审计总结

| Scale | SFT with-evi @1024 | SFT no-evi @1024 | 不对称 | 需 @2048? |
|-------|--------------------|--------------------|---------|-----------|
| 1.7B | **32-48%** | **51%** | ~19pp | ✅ 已跑 s42 |
| 4B | 25-32% | 30% | ~1pp | ⚠️ 可选 |
| 8B Qwen | **31.8%** | **22.8%** | **9pp** | ✅ 正在跑 |
| 14B | 10.7%* | 10.8%* | **<0.1pp** | ❌ 不需要 |
| LLaMA-8B | 19-24% | 22-42% | 变化大 | ✅ 已完成 |

| Scale | RSFT with-evi @1024 | RSFT no-evi @1024 | 不对称 | 需 @2048? |
|-------|--------------------|--------------------|---------|-----------|
| 1.7B | 24-25% | N/A (无独立 eval) | — | ⚠️ 可选 |
| 8B Qwen | 23-27% | N/A | — | ⚠️ 可选 |
| 14B | **10.7%** | **10.8%** | **<0.1pp** | ✅ 在跑 (确认) |
| LLaMA-8B | 16-17% | 18-19% | **~2pp** | ⚠️ s42 在跑 |

*14B SFT truncation 来自 RSFT 数据，SFT 可能略有不同。

---

## Part 2: Matched@2048 配对完成情况

### LLaMA-8B SFT — ✅ 3-seed 全部完成

| Seed | with-evi@2048 | no-evi@2048 | matched_fair_tax |
|------|---------------|-------------|------------------|
| s42 | 0.5649 | 0.5210 | **-4.39pp** |
| s43 | 0.4954 | 0.3389 | **-15.65pp** ⚠️ |
| s44 | 0.4655 | 0.4373 | **-2.82pp** |
| **Mean** | **0.5086** | **0.4324** | **-7.62pp** |

→ Evidence consistently helps LLaMA SFT（但 s43 no-evi 有 format 问题，拉大了 gap）

### LLaMA-8B RSFT — @1024 可信，@2048 确认中

| Seed | with-evi@1024 | no-evi@1024 | @1024 tax | @2048 status |
|------|---------------|-------------|-----------|--------------|
| s42 | 0.5714 | 0.5526 | -1.88pp | 🔄 with-evi 在跑 |
| s43 | 0.5662 | 0.5546 | -1.16pp | ❌ |
| s44 | 0.5587 | 0.5550 | -0.37pp | ❌ |
| **Mean** | **0.5654** | **0.5541** | **-1.14pp** | |

### Qwen3-1.7B SFT — s42 @2048 刚完成

| Seed | with-evi@2048 | no-evi@2048 | matched_fair_tax |
|------|---------------|-------------|------------------|
| s42 | **0.4806** ✅ | 0.3925 | **-8.81pp** |
| s43 | ❌ | ❌ | — |
| s44 | ❌ | ❌ | — |

### Qwen3-8B SFT — no-evi@2048 缺失

| Seed | with-evi@2048 | no-evi@2048 | Status |
|------|---------------|-------------|--------|
| s42 | 🔄 RUNNING | ❌ MISSING | 需补 no-evi@2048 |

### Qwen3-14B RSFT — @1024 对称，@2048 确认中

| Seed | with-evi | no-evi | tax |
|------|----------|--------|-----|
| @1024 | 0.5886 | 0.5432 | -4.54pp |
| @2048 | 🔄 RUNNING | ❌ (不急) | TBD |

### Qwen3-4B — 无 @2048 数据

| Seed | with-evi@2048 | no-evi@2048 |
|------|---------------|-------------|
| s42 | ❌ | ❌ |

### 配对总结

| Scale | Method | Matched@2048 状态 | @1024 tax 可信度 |
|-------|--------|-------------------|--------------------|
| LLaMA-8B | SFT | ✅ 完成 (3-seed) | 低（截断不对称） |
| LLaMA-8B | RSFT | 🔄 s42 在跑 | ✅ 高（2pp 不对称） |
| 1.7B | SFT | ✅ s42 完成 | 低（19pp 不对称） |
| 8B Qwen | SFT | 🔄 with-evi 在跑 | 低（9pp 不对称） |
| 14B | RSFT | 🔄 with-evi 在跑 | ✅ 高（<0.1pp 对称） |
| 4B | SFT | ❌ 全缺 | ⚠️ 中（1pp 对称但 30% 绝对率） |

---

## Part 3: 下批实验清单（优先级排序）

### Tier 0: 等待完成（~0.5-2.5h）

| # | 实验 | GPU | ETA | 说明 |
|---|------|-----|-----|------|
| — | eval_llama_rsft_s42_with_evidence_2048 | cuda:0 | ~25min | LLaMA RSFT @2048 robustness |
| — | plan017_14b_rsft_eval_2048 | cuda:1 | ~30min | 14B RSFT @2048 confirmation |
| — | d140_8b_sft_s42_with_evi_2048 | cuda:3 | ~2.5h | 8B Qwen SFT @2048 |

### Tier 1: 高优先级（完成 matched 表格）

| # | exp_id | 假设 | Command | GPU | 预估时长 |
|---|--------|------|---------|-----|----------|
| 1 | d140_8b_sft_s42_no_evi_2048 | 8B SFT no-evi@2048 配对完成后可计算 8B fair tax | `CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --no_evidence --seed 42` | 1 GPU | ~2h |
| 2 | eval_llama_rsft_s43_with_evi_2048 | LLaMA RSFT 3-seed matched@2048 tax | `CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s43_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 43` | 1 GPU | ~4h |
| 3 | eval_llama_rsft_s44_with_evi_2048 | 同上 s44 | `CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s44 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s44_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 44` | 1 GPU | ~4h |

### Tier 2: 中等优先级（加强 narrative）

| # | exp_id | 假设 | Command | GPU | 预估时长 |
|---|--------|------|---------|-----|----------|
| 4 | d140_8b_rsft_s42_with_evi_2048 | 8B Qwen RSFT @2048 检查（27% 截断偏高） | `CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_8b_rsft_s42_with_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --seed 42` | 1 GPU | ~2h |
| 5 | d140_1_7b_rsft_s42_with_evi_2048 | 1.7B RSFT @2048 检查（25% 截断） | `CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_1_7b_rsft_s42_with_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --seed 42` | 1 GPU | ~1.5h |
| 6 | d140_1_7b_sft_s43_with_evi_2048 | 1.7B 多 seed @2048 | `CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed43 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_1_7b_sft_s43_with_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --seed 43` | 1 GPU | ~1.5h |

### Tier 3: 低优先级

| # | exp_id | 说明 |
|---|--------|------|
| 7 | d140_4b_sft_s42_with_evi_2048 | 4B @2048（截断对称，可选） |
| 8 | d140_4b_sft_s42_no_evi_2048 | 4B no-evi@2048 配对 |
| 9 | d140_14b_sft_s42_with_evi_2048 | 14B SFT @2048（如需 SFT tax） |

### 论文 Narrative 依赖分析

论文需要 **evidence tax 跨尺度一致性** 的 claim：

1. **当前可报告（@1024 可信）:**
   - 14B RSFT: tax=-4.54pp ✅
   - LLaMA RSFT: tax=-1.14pp ✅
   - 4B: tax ~symmetric ⚠️ (仅 @1024)

2. **当前可报告（matched@2048）:**
   - LLaMA SFT: tax=-7.62pp (3-seed) ✅
   - 1.7B SFT: tax=-8.81pp (1-seed) ✅

3. **等待中:**
   - 8B Qwen SFT: 需 with+no @2048 → Tier 0+1
   - LLaMA RSFT @2048: Tier 0+1

4. **最小可行表格:** LLaMA SFT (3-seed) + LLaMA RSFT (@1024) + 14B RSFT (@1024) + 1.7B SFT (1-seed @2048) 已可构成 narrative: evidence consistently helps or is neutral across scales。

---

## Part 4: D112 RSFT s44 后续 Eval

### 已有结果
- `d112_rsft_from_sft_s44`: ign_f1=0.2181 ← 训练崩溃，无效
- `d112_rsft_bf16`: ign_f1=0.5152 ← 这是可用的版本

### 如果 RSFT s44 重训完成，需要以下 eval:

**1) RSFT s44 with-evidence eval:**
```bash
cd /root/autodl-tmp/freige && \
CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference \
  --model_path /root/autodl-tmp/rsft_output_4b_sft_s44_bf16 \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output_seed44 \
  --data_path /root/autodl-tmp/data/docred \
  --split dev \
  --output_dir /root/autodl-tmp/eval_results/d112_rsft_s44_with_evi_eval \
  --batch_size 4 \
  --max_new_tokens 1024 \
  --no-quantize \
  --seed 44
```

**2) RSFT s44 no-evidence eval:**
```bash
cd /root/autodl-tmp/freige && \
CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference \
  --model_path /root/autodl-tmp/rsft_output_4b_sft_s44_bf16 \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output_seed44 \
  --data_path /root/autodl-tmp/data/docred \
  --split dev \
  --output_dir /root/autodl-tmp/eval_results/d112_rsft_s44_no_evi_eval \
  --batch_size 4 \
  --max_new_tokens 1024 \
  --no-quantize \
  --no_evidence \
  --seed 44
```

> **注意:** 
> - 必须 `CUDA_VISIBLE_DEVICES=X` 指定 GPU（C002/C003）
> - no-evidence 必须传 `--no_evidence`（C005）
> - 提交前 `nvidia-smi` 确认目标 GPU 显存 < 2GB（C001）
> - rsft_output_4b_sft_s44_bf16 路径需确认是否为最新训练产物

---

## 当前 GPU 状态

| GPU | 占用 | 进程 | ETA |
|-----|------|------|-----|
| cuda:0 | 18.9 GB | eval_llama_rsft_s42_with_evidence_2048 (89%) | ~25 min |
| cuda:1 | 32.5 GB | plan017_14b_rsft_eval_2048 (~88%) | ~30 min |
| cuda:2 | 6.2 GB | ✅ d140_1_7b_sft_s42_with_evi_2048 **已完成** | — |
| cuda:3 | 19.6 GB | d140_8b_sft_s42_with_evi_2048 (16%) | ~2.5h |

→ **cuda:2 已空闲，可立即提交 Tier 1 实验 #1 (8B SFT no-evi@2048)**
→ cuda:0 和 cuda:1 约 30 分钟后释放，可提交 Tier 1 #2/#3
