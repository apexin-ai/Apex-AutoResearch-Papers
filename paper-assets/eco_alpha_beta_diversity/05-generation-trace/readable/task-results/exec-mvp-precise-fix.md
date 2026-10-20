# exec mvp precise fix

**eco alpha beta diversity** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_mvp_precise_fix_20260521T140024_result.json`
- **Structured JSON:** [`0a9ab33aa02c04e1903e.json`](../../sessions/0a/0a9ab33aa02c04e1903e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All artifacts registered. Here's the complete results report:

---

## 修复记录

**data_loader.py — 3 bug + 1 防御性修复：**

| Bug | 根因 | 修复 |
|-----|------|------|
| Bug 1 (文本列) | `_guess_text_col` 子串匹配 "story" 命中 69 列 | 精确匹配 `ai_story_gen.1.player.story` → 后缀匹配 `.story`/`.text` → 候选列 avg_len>50 过滤 → RuntimeError |
| Bug 2 (条件映射) | `"human" in v` 子串匹配导致 `human_1ai`/`human_5ai` 可能误映射；NaN 行未过滤 | 精确字典 `CONDITION_MAP`，`_map_condition` 返回 None 跳过未知/NaN |
| Bug 3 (文件顺序) | evaluators 按字母序排在 writers 前 | writer 文件优先排序 |
| 静默 fallback | `_guess_text_col` 返回 None 时静默 skip | 改为 RuntimeError，`load_stories` 终态抛 RuntimeError |

**run_mvp.py：** `metadata.dataset` 从 `"Doshi & Hauser (2024)"` 改为 `"doshi_hauser_2024"`。

---

## 完整结果

### (A) 数据集信息

| 条件 | n | mean words | median | std |
|------|---|-----------|--------|-----|
| no-AI | 98 | 130 | 124 | 53 |
| AI-editor | 100 | 145 | 141 | 49 |
| AI-ideas+editor | 99 | 155 | 139 | 63 |

来源：Doshi & Hauser 2024 Dryad (`writers-2023-06-28.csv`)，297 stories（500行中309有效条件，过滤 len<30 和 tokens<10 后 297）。

### (B) Hill numbers (q=0, 1, 2)

| q | Condition | alpha | alpha CI | gamma | beta | beta CI |
|---|-----------|-------|----------|-------|------|---------|
| 0 | no-AI | 84.19 | [79.2, 89.5] | 2702 | 32.09 | [22.2, 25.9] |
| 0 | AI-editor | 92.82 | [88.5, 98.1] | 2860 | 30.81 | [21.4, 25.1] |
| 0 | AI-ideas+editor | 97.97 | [93.0, 103.7] | 3057 | 31.20 | [21.6, 25.5] |
| 1 | no-AI | 61.99 | [58.0, 65.4] | 553.3 | 8.93 | [7.16, 8.28] |
| 1 | AI-editor | 68.59 | [64.8, 72.0] | 537.5 | 7.84 | [6.58, 7.24] |
| 1 | AI-ideas+editor | 71.26 | [67.6, 75.0] | 566.8 | 7.95 | [6.68, 7.36] |
| 2 | no-AI | 41.47 | [39.2, 43.6] | 95.1 | 2.29 | [2.09, 2.48] |
| 2 | AI-editor | 45.12 | [42.8, 47.3] | 90.9 | 2.01 | [1.90, 2.10] |
| 2 | AI-ideas+editor | 46.16 | [43.4, 48.5] | 90.1 | 1.95 | [1.84, 2.02] |

### (C) Baselga 分解

| Condition | BC_total | BC_balanced | BC_bal CI | BC_gradient | BC_gra CI |
|-----------|----------|-------------|-----------|-------------|-----------|
| no-AI | 0.7910 | 0.7269 | [0.705, 0.735] | 0.0641 | [0.054, 0.074] |
| AI-editor | 0.7643 | 0.7094 | [0.692, 0.713] | 0.0548 | [0.046, 0.062] |
| AI-ideas+editor | 0.7668 | 0.7037 | [0.684, 0.710] | 0.0630 | [0.052, 0.073] |

### (D) Rarefaction (归一化到 31 words)

方向一致：AI 条件下 alpha 微高、beta 微低，但差异极小（<1%）。长度归一化后差异几乎消失，说明原始差异部分由文本长度驱动。

### (E) Cosine similarity

- Within-cond: mean=0.1332 ± 0.0578
- Between-cond: mean=0.1295 ± 0.0568
- Point-biserial r=0.0312, p=5.9e-11

r 虽然显著（大样本），但远小于 0.3 阈值。

### (F) 6 个 Pass/Fail 标准

| 标准 | 结果 | 详情 |
|------|------|------|
| **PASS 1** (alpha↑) | **False** | q1: AI-ideas+editor CI 不重叠 ✓，但 AI-editor CI 重叠 ✗ → q1_pass=True 但需两个 AI 条件都通过 |
| **PASS 2** (beta↓) | **False** | q1: 两个 AI 条件 CI 均与 no-AI 重叠；仅 q2 AI-ideas+editor 通过 |
| **PASS 3** (Baselga) | **True** | 3 个条件的 balanced-variation CI 互不重叠 |
| **PASS 4** (cosine r) | **False** | r=0.031 < 0.3 阈值 |
| **FAIL 1** (no pattern) | **True** (triggered) | PASS 1 和 PASS 2 均未通过 → 模式不存在 |
| **FAIL 2** (flat≈eco) | **True** (triggered) | tfidf_fail=True, reg_fail=True, combined=True |

### (G) 最终判定

**OVERALL: FAIL**

### (H) q=2 beta 方向

q=2 beta: no-AI=2.29 > AI-editor=2.01 > AI-ideas+editor=1.95。**AI 条件下 q=2 beta 更低**，方向符合预期（AI 使写作更同质化）。CI 不重叠：no-AI [2.09, 2.48] vs AI-ideas+editor [1.84, 2.02]。这是唯一 beta↓ 显著的 q 值。

### (I) 注册文件

| artifact_id | 文件 |
|-------------|------|
| art_20260521_a03459 | mvp_results.json |
| art_20260521_aaaf57 | hill_numbers_comparison.png |
| art_20260521_af982d | baselga_decomposition.png |
| art_20260521_497fcd | cosine_similarity_heatmap.png |
| art_20260521_ef39fc | rarefaction_curves.png |

---

**核心发现**：真实数据存在预期方向的 alpha↑ / beta↓ 趋势，但效应量小、CI 大量重叠。唯一统计显著的是 q=2 beta（衡量 dominant species turnover）和 Baselga balanced-variation 分解。Cosine 基线几乎无区分力（r=0.03），FAIL-2 触发说明 flat metric 无法恢复 Baselga 的比例结构。

---
