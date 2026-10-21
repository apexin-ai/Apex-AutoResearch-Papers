# Paper Consistency Audit — 2026-05-16 (Updated)

## Summary
- 审计文件数: 10 (.tex) + paper_framing.md + registry (40 experiments, DONE/success)
- 发现问题数: 12 (critical: 5, warning: 4, minor: 3)
- 前次审计 C2/C3（intro PPL 17.650→17.651, ESS-only 17.722→17.723）已修复

---

## Critical Issues

### C1. [method.tex:136] n_min=1 "ceiling-hitting" 统计量标注错误
- **论文**: "46.7% of batches hitting the search ceiling at $b_{\max}=20$"
- **Registry**: nmin1_seed42 → `b_star_pct_above_2 = 46.7`（即 b\*>2 的比例，非 hitting ceiling）
- **实际**: p75=20 暗示 ≥25% 在 ceiling，但 46.7% 是 b\*>2 的比例，包含 b\*∈(2,20) 的 batch
- **修复**: 改为 "46.7% of batches select b\* > 2, with the 75th percentile saturating at $b_{\max}{=}20$"

### C2. [experiments.tex:19] Holdout 文档数描述不准确
- **论文**: "a held-out subset of FineWeb (67.8K documents, ~4M tokens)"
- **Registry**: 所有 eval_method 均为 `max_docs=5000`，eval_holdout_tokens=4,077,068
- **实际**: 4M tokens 来自 5,000 篇文档评估，非 67.8K 篇
- **修复**: "5,000 documents sampled from a larger holdout pool, ~4M tokens" 或 "a held-out pool of 67.8K documents, from which we evaluate on 5,000 documents (~4M tokens)"

### C3. [discussion.tex:17] Citation key 不匹配
- **论文**: `\citet{wang2026survive}`
- **其余文件**: method.tex, conclusion.tex, related_work.tex 均用 `\citet{wang_2026_survive_contamination}`
- **影响**: LaTeX 编译产生 undefined citation
- **修复**: `wang2026survive` → `wang_2026_survive_contamination`

### C4. [method.tex:93] 51,913 micro-batches 与训练配置不符
- **论文**: "Across 51,913 micro-batches in our main experiment (ρ=0.4, τ=0.8, n_min=2)"
- **实际**: 6,103 steps × 4 grad_accum = **24,412** micro-batches
- **Registry**: adaptive_fix_seed42 的 b_star_count=26,458（含 checkpoint 记录？）
- 51,913 可能来自旧版 n_min=3 分析或多 seed 合并，与当前 n_min=2 single-seed 不符
- **注**: method_3f5a58.tex（hash 版本）不含此数字。如编译用 base method.tex 则需修复

### C5. [results.tex τ table] τ=0.9 和 τ=0.95 数据无 registry 对应
- **论文**: τ=0.9 PPL=17.712 (b̄\*=2.36), τ=0.95 PPL=17.723 (b̄\*=3.08)
- **Registry**: 40 个 DONE/success 实验中无 tau_09_seed42 或 tau_095_seed42
- paper_framing.md 引用相同数据，说明数据确实存在，但未注册到 registry
- **修复**: 补录这两个实验到 registry，或确认它们以其他名称存在

---

## Warning Issues

### W1. [table1_main_results.tex vs results.tex] 表格冲突
- table1 包含 Adaptive n_min=3 行（bold best, PPL 17.639, Δ=-0.055）和 n_min=2 行
- results.tex 仅展示 n_min=2 为 "Adaptive (ours)"（PPL 17.651）
- 两文件均有 `\label{tab:main}` / `\label{tab:main-results}` 但 text 中 `\ref{tab:main}` 可能指向错误表
- table1 中 n_min=3 被标注为"historical" 脚注（†），但 bold + best 列与 footnote 矛盾
- **修复**: 确定 canonical table。建议保留 results.tex 版本（与全文一致），将 table1 归档

### W2. [introduction.tex vs introduction_c6a67f.tex] Citation key 格式不同
- Base files: 下划线键 (`cheng_2025_contamination_survey`)
- Hash files: 短键 (`cheng2025contamination`)
- 混用会导致 undefined citations
- **修复**: 确保 main.tex 中 \input 的所有 section 使用统一 key 格式

### W3. [introduction_c6a67f.tex:32] PPL 精度不一致
- "uniform training (PPL $17.69$)" / "ESS-only (PPL $17.73$)" — 2dp
- 全文其他位置均用 3dp (17.694, 17.723)
- **修复**: 统一为 3dp

### W4. [results.tex:85] batch_size=8 实验数据无 registry 对应
- "At batch size B=8 with n_min=2 ... yielding PPL 17.73"
- Registry 中无 batch_size=8 实验
- **修复**: 补录此实验到 registry

---

## Minor Issues

### M1. [introduction.tex contribution 3] "comparable to stronger neural detectors" 无直接实验支撑
- 论文未运行 ModernBERT 等 neural detector 实验，无法说 "comparable"
- 仅能说 TF-IDF+LR "suffices for effective reweighting"

### M2. [paper_framing.md] MVP 数据表使用旧 eval 数据
- Uniform PPL: 17.690/17.690/17.700（framing）vs 17.694/17.686/17.702（registry post-hoc）
- .tex 文件已使用正确数据，但 framing 未同步

### M3. [table1_main_results.tex:12] n_min=3 的 b̄\*=1.43 无 registry 验证
- adaptive_seed42 registry 仅记录 `b_star: "per-batch adaptive (0.0-3.8)"`，无 mean

---

## Verified OK — 全部数值经 registry 验证正确

### Main Table (results.tex / results_d0d647.tex)
| Method | Seed 42 | Seed 123 | Seed 456 | Mean | Registry Match |
|--------|---------|----------|----------|------|---------------|
| Uniform | 17.694 | 17.686 | 17.702 | 17.694 | ✓ (17.6939/17.6861/17.7015) |
| Grid-best b=0.5 | 17.651 | 17.638 | 17.650 | 17.646 | ✓ |
| ESS-only | 17.730 | 17.720 | 17.719 | 17.723 | ✓ (17.73/17.72/17.719) |
| Golden Ratio | 17.654 | — | — | — | ✓ |
| Adaptive (n_min=2) | 17.653 | 17.643 | 17.657 | 17.651 | ✓ (17.6527/17.6432/17.6566) |

### τ Sweep Table (results.tex)
| τ | PPL (paper) | PPL (registry) | b̄\* (paper) | b̄\* (registry) | Match |
|---|------------|----------------|------------|----------------|-------|
| 0.50 | 17.688 | 17.688 | 0.39 | 0.3923 | ✓ |
| 0.60 | 17.681 | 17.6805 | 0.59 | 0.5899 | ✓ (3dp round) |
| 0.70 | 17.679 | 17.6793 | 0.89 | 0.8943 | ✓ (3dp round) |
| 0.80 | 17.653 | 17.6527 | 1.40 | 1.399 | ✓ |
| 0.90 | 17.712 | **N/A** | 2.36 | **N/A** | ⚠ unverifiable |
| 0.95 | 17.723 | **N/A** | 3.08 | **N/A** | ⚠ unverifiable |

### n_min Table (results.tex)
| n_min | PPL (paper) | PPL (registry) | b̄\* (paper) | b̄\* (registry) | Match |
|-------|------------|----------------|------------|----------------|-------|
| 1 | 17.789 | 17.789 | 7.20 | 7.197 | ✓ |
| 2 | 17.653 | 17.6527 | 1.40 | 1.399 | ✓ |
| 3† | 17.644 | 17.644 | 1.43 | N/A | PPL ✓, b̄\* unverified |
| 4 | 17.695 | 17.6947 | 0.00 | 0 | ✓ |

### Detector (experiments.tex)
| Metric | Paper | Registry | Match |
|--------|-------|----------|-------|
| AUC | 0.939 | 0.939 | ✓ |
| ECE (calibrated) | 0.048 | 0.048 | ✓ |
| Temperature T | 0.204 | 0.204 | ✓ |
| q-score mean | 0.60 | 0.6 | ✓ |
| q-score std | 0.37 | 0.374 | ✓ |
| q-score median | 0.71 | 0.707 | ✓ |
| Mid-range [0.2,0.8] | 46.3% | 0.463 | ✓ |

### Other Verified Claims
- Grid sweep monotonic: b=0.5→17.651, b=5.0→17.818 (seed42) ✓
- Per-seed adaptive improvement: 0.041, 0.043, 0.045 ✓
- Adaptive vs Golden Ratio gap: |17.653−17.654| = 0.001 ✓
- b\* distribution: median 0.87, IQR [0.54, 1.51], mean 1.40 ✓
- τ range PPL span: 17.688−17.653 = 0.035 ✓
- n_min=1 degradation: 17.789−17.653 ≈ +0.14 ✓
- PPL improvement over uniform: 17.694−17.651 = 0.043 ✓
- eval_holdout_tokens = 4,077,068 (~4M) ✓
- total_steps = 6,103 ✓
- data_count = 371,499 ✓
- contamination_60_ess_only PPL = 17.77 ✓

### Files with no quantitative issues
- conclusion.tex ✓
- related_work.tex ✓ (no quantitative claims)

---

## Action Items (优先级排序)

| # | 优先级 | 文件 | 操作 |
|---|--------|------|------|
| 1 | 🔴 紧急 | discussion.tex:17 | 修复 citation key: `wang2026survive` → `wang_2026_survive_contamination` |
| 2 | 🔴 紧急 | experiments.tex:19 | 修正 holdout 描述: 67.8K → 5,000 documents evaluated |
| 3 | 🔴 紧急 | method.tex:136 | 修正 n_min=1 统计: "46.7% hitting ceiling" → 准确表述 |
| 4 | 🔴 紧急 | method.tex:93 | 确认 51,913 micro-batches 来源，或改为 24,412 |
| 5 | 🟡 高优 | registry | 补录 τ=0.9, τ=0.95, batch_size=8 实验 |
| 6 | 🟡 高优 | table1 vs results | 确定 canonical main table，删除冗余 |
| 7 | 🟡 高优 | 全局 | 确认 main.tex 使用哪套 citation key 格式 |
| 8 | 🟢 低优 | introduction_c6a67f.tex:32 | 统一 PPL 精度为 3dp |
| 9 | 🟢 低优 | paper_framing.md | 更新 MVP 表为 post-hoc eval 数值 |
| 10 | 🟢 低优 | introduction.tex | Contribution 3 表述弱化: "comparable to" → "suffices" |
