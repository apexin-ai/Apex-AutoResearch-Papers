# code read code audit

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_read_code_audit_20260513T193010_result.json`
- **Structured JSON:** [`2e2c06d391c3f59b49e9.json`](../../sessions/2e/2e2c06d391c3f59b49e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有代码文件已读取完毕（来自本地 `artifacts/code/` 副本，无 `.sh` 脚本文件）。以下是完整文件内容和关键发现。

---

## 文件 1: `diversity_selection.py` (243 行)

**存在**: 是

&lt;details>
&lt;summary>完整内容（已在上面读取）&lt;/summary>

关键函数:
- `fit_pca()` (line 9): PCA 降维
- `project()` (line 25): PCA 投影
- `compute_normalized_eigenvalue_variance()` (line 35): 核心目标函数
- `quality_filter()` (line 53): 质量过滤
- `greedy_disf_selection()` (line 115): 贪心选择主函数
- `select_data()` (line 173): 完整 pipeline
&lt;/details>

---

## 文件 2: `evaluate.py` (184 行)

**存在**: 是

关键函数:
- `compute_held_out_perplexity()` (line 38)
- `compute_rare_ngram_survival()` (line 63) — **重点**
- `compute_rank_correlation()` (line 94)

---

## 文件 3: `run_phase2.sh`

**不存在**。本地 artifacts 中没有任何 `.sh` 文件。

---

## 文件 4: `generate.py` (121 行)

**存在**: 是

---

## 文件 5: `run_mvp.py` (333 行)

**存在**: 是 — 这是主 pipeline 文件。

---

## 回答 7 个关键问题

### 1. `greedy_disf_selection` 的目标函数

**Eigenvalue variance minimization**，不是 facility location。

`diversity_selection.py:115-170` — 每步贪心选择使 `compute_normalized_eigenvalue_variance(trial)` 最小化的候选。该函数计算 `||C(S∪{x})||_F / trace(C(S∪{x}))²`（协方差矩阵的 Frobenius 范数除以迹的平方）。值越低 = 特征值越均匀 = 空间覆盖越多样。

### 2. PCA 降维

**有**。默认降到 **32 维**。

- `diversity_selection.py:9` — `fit_pca(reference_embeddings, n_components=32)`
- `run_mvp.py:44` — `--pca_dim, default=32`
- `diversity_selection.py:230-232` — PCA 拟合在 reference embeddings 上，然后投影 candidates

### 3. External-only 是否使用相同的选择算法

**是**。`run_mvp.py:99` 中 external_only 方法设 `selection_method = "contriever"`，然后调用 **同一个** `select_data()` 函数（`run_mvp.py:123-127`）。`select_data()` 内部走完全相同的 pipeline：quality filter → embed → PCA → `greedy_disf_selection`。唯一区别是 embedding 来源（Contriever 而非 student internal）。

### 4. Rare n-gram 定义

**Percentile-based**，不是固定阈值。

- `evaluate.py:63` — `compute_rare_ngram_survival(reference_texts, synthetic_texts, n=3, rare_percentile=10)`
- 参数: `n=3`（trigram），`rare_percentile=10`（底 10% 频率的 n-gram 被定义为 rare）
- `evaluate.py:78` — `threshold = counts[max(0, len(counts) * rare_percentile // 100)]`，然后 `c <= threshold` 的 n-gram 为 rare
- `data_prep.py:32` 中 `compute_ngram_rarity()` 使用相同逻辑（`n=3, rare_percentile=10`）

### 5. Generation 0 是否执行了 selection

**是，每个方法的每个 generation（包括 Gen 0）都执行 selection。**

`run_mvp.py:244` — 循环 `for gen in range(args.num_generations)` 从 0 开始，每轮都经过 generate → select → train → evaluate。三个方法不共享 Gen 0：
- `rgds`: 监控 RankMe/kNN 后选 internal 或 contriever
- `external_only`: 始终用 contriever embedding
- `uncurated`: 不选（返回全部 candidates，`run_mvp.py:97`）

### 6. temperature 和 top_p 默认值

- `generate.py:23` — `--temperature, default=0.8`
- `generate.py:24` — `--top_p, default=0.95`
- `run_mvp.py:56-57` — `--gen_temperature, default=0.8`，`--gen_top_p, default=0.95`

### 7. Quality filter 参数

**有**。

- `diversity_selection.py:53` — `quality_filter(candidates, model, tokenizer, reference_set, device, percentile=90, batch_size=32)`
- `run_mvp.py` 没有暴露 quality_percentile 为命令行参数，但 `select_data()` 接受 `quality_percentile` 参数，默认值 **90**（即 perplexity 超过 reference set 第 90 百分位的 candidates 被过滤掉）
- `uncurated` 方法跳过 selection（`run_mvp.py:97`），因此也跳过了 quality filter

---

**注意**: 以上内容来自本地 `artifacts/code/` 副本。如果服务器代码已被修改但未同步回本地，可能存在差异。当前 session 无 SSH 工具可用，无法直接读取服务器文件。如需确认服务器最新版本，可通过 spawn_worker（带 ssh tool group）来完成。

---
