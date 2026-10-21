# Paper Audit Report

Generated: 2026-05-15

## 编译检查

### \input{} 引用完整性
- [x] introduction.tex — 存在 ✅
- [x] related_work.tex — 存在 ✅
- [x] method.tex — 存在 ✅
- [x] results.tex — 存在 ✅
- [ ] discussion.tex — 已注释掉（文件存在）
- [ ] limitations.tex — 已注释掉（文件存在）
- [ ] conclusion.tex — 已注释掉（文件存在）
- [ ] ethics.tex — 已注释掉（文件存在）

### 图片文件存在性
- [x] fig1_differential_response.pdf — `artifacts/_project/chart/` 中存在 ✅
- [x] fig3_baseline_comparison.png — `artifacts/_project/chart/` 中存在 ✅
- [x] `\graphicspath{{../chart/}}` 相对路径正确 ✅

### bib 文件存在性
- [ ] references.bib — **不在 paper 目录中** ❌
  - `build.sh` 从 `docs/paper/references.bib` 复制（源文件存在 ✅）
  - 必须通过 build.sh 编译，直接 pdflatex 会失败

### 缺失文件清单
| 文件 | 状态 | 影响 |
|------|------|------|
| `acl.sty` | ❌ 缺失 | 编译失败，需从 ACL style files 下载 |
| `acl_natbib.bst` | ❌ 可能缺失 | bibtex 可能失败 |
| `references.bib`（本地副本） | ❌ 需 build.sh 复制 | 直接 pdflatex 失败 |

### 其他编译问题
- 4 个 section（discussion/limitations/conclusion/ethics）在 main.tex 中被注释掉，PDF 将只包含 Introduction—Results

---

## 数字一致性

### 6-gen LOGO 分类结果（Registry: plan-014）

#### results.tex 内联表 vs table1.tex vs Registry

| Generator | results.tex | table1.tex | Registry | results.tex 匹配？ | table1.tex 匹配？ |
|-----------|------------|------------|----------|-------------------|-------------------|
| Pythia-1B | 0.855 | 0.856 | 0.8562 | ❌ (应为 0.856) | ✅ |
| Pythia-2.8B | 0.804 | 0.804 | 0.8041 | ✅ | ✅ |
| OLMo-2-1B | 0.762 | 0.764 | 0.7635 | ❌ (应为 0.764) | ✅ |
| Qwen3-0.6B | 0.823 | 0.824 | 0.8243 | ❌ (应为 0.824) | ✅ |
| Qwen3-1.7B | 0.809 | 0.805 | 0.8046 | ❌ (应为 0.805) | ✅ |
| Qwen3-8B | 0.685 | 0.683 | 0.6832 | ❌ (应为 0.683) | ✅ |
| **Average (6-gen)** | **0.790** | **0.789** | **0.7893** | ❌ (应为 0.789) | ✅ |

**结论**: results.tex 内联 LOGO 表中 7 个数字有 6 个与 registry 不一致。table1.tex 全部正确但未被 \input。

#### OLMo-2-1B 参数量不一致
| 位置 | 值 |
|------|-----|
| results.tex 内联表 | 1.2B |
| table1.tex | 1.5B |

两处不一致，需确认模型实际参数量。

### Feature Importance（Registry: plan-014）

| 位置 | hapax_ratio | entropy_mean | ttr | 匹配？ |
|------|------------|-------------|-----|--------|
| Registry | 0.269 | 0.1637 | 0.159 | — |
| table2.tex caption | 0.269 | 0.164 | 0.159 | ✅ |
| results.tex 文本 (L72) | 0.271 | 0.156 | 0.165 | ❌ 三个都错 |
| results.tex 内联表 | 0.271 | — | — | ❌ |

### Spearman Correlations（Registry: plan-014）

| Feature | Registry | Paper (results.tex L66-67) | 匹配？ |
|---------|----------|---------------------------|--------|
| hapax_ratio | -0.5578 | -0.558 | ✅ (3dp 四舍五入) |
| ttr | -0.5419 | -0.543 | ❌ (应为 -0.542) |
| entropy_mean | -0.4754 | -0.476 | ❌ (应为 -0.475) |
| entropy_std | \|−0.0755\| | 0.076 | ✅ |
| tail_decay | \|−0.0894\| | 0.087 | ❌ (应为 0.089) |

### Feature Ablation（results.tex 内联表 vs table2.tex）

| Feature Set | results.tex | table2.tex | 一致？ |
|-------------|------------|------------|--------|
| Full (7 features) | 0.790 | 0.789 | ❌ |
| Surface only | 0.729 | 0.729 | ✅ |
| Reference only | 0.745 | 0.745 | ✅ |

注：这些是 6-gen LOGO 消融值。Registry 仅有 5-gen LOFO 消融（plan-002-eval: full=0.8037, surface=0.7471, reference=0.7543），无法直接验证 6-gen 消融数字。

### Baselines（Registry: plan-015-v2, 5-gen LOGO）

| Method | results.tex | Registry | 匹配？ |
|--------|------------|----------|--------|
| 7-feature ensemble | 0.798 | 0.798 | ✅ |
| 95% CI | [0.786, 0.799] | [0.786, 0.799] | ✅ |
| Avg-LogProb | 0.765 | 0.7653 | ✅ |
| Avg-LogProb CI | [0.616, 0.820] | [0.616, 0.82] | ✅ |
| LD-Score | 0.721 | 0.7212 | ✅ |
| LD-Score CI | [0.588, 0.770] | [0.588, 0.77] | ✅ |
| FastDetectGPT | 0.627 | 0.6269 | ✅ |
| FastDetectGPT CI | [0.511, 0.762] | [0.511, 0.762] | ✅ |
| Binoculars | 0.579 | 0.579 | ✅ |
| Binoculars CI | [0.405, 0.664] | [0.405, 0.664] | ✅ |

**Baselines 全部匹配** ✅

### Downstream Perplexity（Registry: plan-004-v2）

| Variant | results.tex | table3.tex | Registry | 匹配？ |
|---------|------------|------------|----------|--------|
| All depths | 2.335 | 2.335 | 2.335 | ✅ |
| Size-matched | 2.367 | 2.367 | 2.367 | ✅ |
| Depth 0-1 | 2.387 | 2.387 | 2.387 | ✅ |
| Binary-filtered | 2.389 | 2.389 | 2.389 | ✅ |
| Depth 0 only | 2.681 | 2.681 | 2.681 | ✅ |

**Downstream 全部匹配** ✅

### Cross-Reference Models（Registry: plan-003）

| Ref Model | table4.tex | Registry | 匹配？ |
|-----------|------------|----------|--------|
| Pythia-410M | 0.803 | 0.8034 | ✅ |
| OLMo-2-1B | 0.807 | 0.8072 | ✅ |
| Qwen3-0.6B | 0.816 | 0.8158 | ✅ |

**Cross-ref 全部匹配** ✅

### 跨 Section 交叉一致性

| Claim | 位置 | 值 | Registry 值 | 匹配？ |
|-------|------|-----|-------------|--------|
| 6-gen LOGO F1 | main.tex abstract | 0.79 | 0.7893 | ✅ (2dp) |
| 6-gen LOGO F1 | introduction.tex | 0.79 | 0.7893 | ✅ (2dp) |
| 6-gen LOGO F1 | conclusion.tex | 0.79 | 0.7893 | ✅ (2dp) |
| 6-gen LOGO CI | main.tex abstract | [0.786, 0.799] | [0.786, 0.799] | ✅ |
| Per-gen range | main.tex abstract | — | — | (无具体数字) |
| Per-gen range | abstract.tex | 0.68 to 0.86 | 0.6832–0.8562 | ✅ |
| Per-gen range | introduction.tex | 0.69 to 0.85 | 0.6832–0.8562 | ❌ (应为 0.68–0.86) |
| Per-gen range | conclusion.tex | 0.68 to 0.86 | 0.6832–0.8562 | ✅ |
| CI range (baselines) | abstract.tex | 0.41–0.82 | 0.405–0.820 | ✅ |
| CI range (baselines) | introduction.tex | 0.59–0.82 | 0.588–0.820 | ✅ (不含 Binoculars) |
| CI range (baselines) | related_work.tex | 0.59–0.82 | 0.588–0.820 | ✅ |
| Downstream ppl | introduction.tex | 2.367 vs 2.387 | 2.367 vs 2.387 | ✅ |
| Qwen3-8B held-out | results.tex text | 0.685 | 0.6832 | ❌ (应为 0.683) |
| Qwen3-8B held-out | limitations.tex | 0.685 | 0.6832 | ❌ (应为 0.683) |
| Qwen3-8B CI | results.tex text | [0.672, 0.698] | — | (registry 无 CI 数据) |
| 5-gen avg | results.tex | 0.804 | 0.8 | ⚠️ 不同量：5-gen LOGO avg ≠ 6-gen LOGO 中 5 小模型平均 |
| CI width | 多处 | 1.3 pp | 0.799−0.786=1.3 pp | ✅ |

### abstract.tex vs main.tex 内联 abstract 不一致

abstract.tex 是独立文件（未被 \input），main.tex 有自己的内联 abstract。两者存在数值差异：

| Claim | main.tex abstract | abstract.tex | 哪个正确？ |
|-------|------------------|-------------|-----------|
| Ablation full F1 | — | 0.80 | — |
| Surface-only F1 | — | 0.75 | 需验证 |
| Reference-only F1 | — | 0.75 | 需验证 |
| CI width | 1.3 pp | — | — |
| CIs span | 18–26 pp | — | — |
| Baseline CI range | — | 0.41–0.82 | ✅ |
| Per-gen range | — | 0.68–0.86 | ✅ |

两个 abstract 互不矛盾但侧重点不同。abstract.tex 中 "surface-only (0.75)" 和 "reference-only (0.75)" 对应 LOFO ablation (plan-002-eval: 0.7471≈0.75, 0.7543≈0.75)，与 results.tex 的 6-gen LOGO ablation (0.729, 0.745) 是不同实验，但 abstract.tex 未注明评估设置。

---

## 发现的问题

### 严重（数字不一致，可能影响审稿）

1. **results.tex 内联 LOGO 表数字偏差**: 6/7 个值与 registry 不一致（Pythia-1B 0.855→0.856, OLMo 0.762→0.764, Qwen3-0.6B 0.823→0.824, Qwen3-1.7B 0.809→0.805, Qwen3-8B 0.685→0.683, avg 0.790→0.789）。table1.tex 有正确值但未被引用。

2. **results.tex Feature Importance 偏差**: 文本中 hapax 0.271/TTR 0.165/entropy_mean 0.156 与 registry（0.269/0.159/0.164）不符。table2.tex caption 有正确值。

3. **Spearman 四舍五入错误**: TTR 写 -0.543（应为 -0.542），entropy_mean 写 -0.476（应为 -0.475），tail_decay 写 0.087（应为 0.089）。

4. **introduction.tex per-gen range 不一致**: 写 "0.69 to 0.85"，但 abstract.tex 和 conclusion.tex 均写 "0.68 to 0.86"（与 registry 一致）。

### 中等（编译问题）

5. **acl.sty 缺失**: 无法编译。需下载 ACL 2023 style files。

6. **4 个 section 被注释掉**: discussion/limitations/conclusion/ethics 不会出现在 PDF 中。

7. **OLMo-2-1B 参数量矛盾**: results.tex 写 1.2B，table1.tex 写 1.5B。

### 轻微

8. **table1-4.tex 未被 \input**: 这些独立表文件（数字更准确）不参与编译。results.tex 已有内联表，但数字不如 table*.tex 准确。

9. **abstract.tex 未被 \input**: 独立文件，main.tex 有自己的内联 abstract。

---

## 建议修复

### 优先级 P0（影响审稿可信度）

1. **用 table1.tex 的正确数字更新 results.tex 内联 LOGO 表**: 将 Pythia-1B→0.856, OLMo→0.764, Qwen3-0.6B→0.824, Qwen3-1.7B→0.805, Qwen3-8B→0.683, avg→0.789。同步更新 results.tex 正文中引用这些数字的地方。

2. **修正 results.tex Feature Importance**: L72 改为 hapax 0.269, entropy_mean 0.164, TTR 0.159（与 registry 和 table2.tex 一致）。内联 ablation 表的 0.271 改为 0.269。

3. **修正 Spearman 四舍五入**: TTR -0.543→-0.542, entropy_mean -0.476→-0.475, tail_decay 0.087→0.089。

4. **修正 introduction.tex per-gen range**: "0.69 to 0.85" → "0.68 to 0.86"。

5. **统一 Qwen3-8B held-out F1**: results.tex 和 limitations.tex 的 0.685 → 0.683。

### 优先级 P1（编译修复）

6. **下载 ACL style files**: 放置 `acl.sty` 和 `acl_natbib.bst` 到 paper 目录。

7. **取消注释 4 个 section**: 在 main.tex 中启用 discussion/limitations/conclusion/ethics。

8. **确认 OLMo-2-1B 参数量**: 查阅模型文档统一为正确值。

### 优先级 P2（整理）

9. **考虑用 \input{table1} 替代内联表**: 减少维护两套数字的风险。或删除 table*.tex 独立文件以避免混淆。

10. **同步 abstract.tex 与 main.tex abstract**: 选定一个作为真实来源。
