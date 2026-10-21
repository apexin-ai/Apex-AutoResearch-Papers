# audit related work completeness

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_related_work_completeness_20260514T021616_result.json`
- **Structured JSON:** [`6d0aad12197931f4a83a.json`](../../sessions/6d/6d0aad12197931f4a83a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Related Work 审查报告

---

### 1. 关键 baseline 覆盖情况

| 方法 | 状态 | 备注 |
|------|------|------|
| DivEye (Basani 2026) | ✅ | line 20 |
| **Binoculars (Hans et al. 2024)** | ❌ 缺失 | 重要 zero-shot 检测方法，与 DetectGPT/Min-K%++ 同级 |
| DetectGPT (Mitchell et al. 2023) | ✅ | line 19 |
| Min-K%++ (Zhang 2024) | ✅ | line 20 |
| CoDeC (Zawalski 2026) | ✅ | line 21 |
| **GLTR (Gehrmann et al. 2019)** | ❌ 缺失 | 早期 statistical detection 开创工作，作为 detection 历史线应提及 |
| Shumailov et al. 2024 (Nature) | ✅ | line 6 |
| Alemohammad et al. 2024 | ✅ | line 7 |
| Dohmatob et al. 2024 | ✅ | line 8 |
| Schaeffer et al. 2025 | ✅ | line 9 |
| DSIR (Xie et al. 2023) | ✅ | line 30 |
| D4 (Tirumala et al. 2023) | ✅ | line 31 |
| DoReMi (Xie et al. 2023) | ✅ | line 31 |
| Drayson et al. 2025 | ✅ | line 34，定位准确 |
| **Ordinal classification baselines** | ❌ 缺失 | 无任何 ordinal regression 引用（见下） |

---

### 2. 潜在遗漏的重要相关工作

**高优先级（建议补充）：**

1. **Binoculars (Hans et al., 2024)** — 用两个 LLM 的 cross-perplexity 比值做 zero-shot 检测，是当前 binary detection 的 SOTA 之一。Binary detection 段落列了 DetectGPT/DivEye/Min-K%++/CoDeC 但漏了 Binoculars，不合理。

2. **GLTR (Gehrmann et al., 2019)** — 基于 token-level 统计（top-k 分布）的早期检测方法，是 statistical fingerprinting 的奠基工作。与论文使用 surprisal 特征的方法论直接相关。

3. **Ordinal regression/classification methods** — 论文将 depth estimation 建模为 ordinal 问题，但 related work 完全没有提及 ordinal classification 文献（如 CORAL [Cao et al. 2020]、ordinal regression 经典方法）。建议加一小段说明为什么 ordinal 建模合适，以及现有 ordinal 方法在此场景的局限。

**中优先级（视篇幅考虑）：**

4. **Benchmark contamination detection** — Shi et al. "Detecting Pretraining Data from Large Language Models" (2023), Golchin & Surdeanu "Time Travel in LLMs" (2024) 等。与本文的 "contamination" 概念有语义重叠，读者可能期望看到区分说明。

5. **Text quality filtering for pretraining** — CCNet (Wenzek et al. 2020)、RefinedWeb (Penedo et al. 2023)、FineWeb。Data Selection 段落只覆盖了 distribution-matching 类方法，heuristic quality filtering 这条线缺失。这些方法与 depth-aware curation 是替代方案关系。

6. **Fast-DetectGPT (Bao et al. 2024)** — DetectGPT 的加速版本，已成为常用 baseline。

**低优先级（可不加）：**

7. **Watermarking 扩展** — 当前只引了 Kirchenbauer 2023 一篇，作为一个独立段落稍薄。但如果篇幅紧张，一篇代表性引用够了。

8. **Information-theoretic analysis** — 与论文方法论关联不够直接，可省略。

---

### 3. 引用真实性抽查

**需验证的可疑引用（2025-2026）：**

| 引用 | 可疑点 | 风险级别 |
|------|--------|---------|
| `shi2025generalization` arXiv:2509.16499 | arXiv ID 为 2509.16499（2025 年 9 月），NeurIPS 2025 Spotlight。作者含 Dacheng Tao（真实知名学者），但其余作者组合需验证 | 中 |
| `basani2026diveye` arXiv:2509.18880 | TMLR 2026 发表。"Yash Basani" 不是该领域常见作者名，需验证 | 中 |
| `zawalski2026codec` arXiv:2510.27055 | ICLR 2026。使用了 `{others}` 省略作者列表，需补全并验证 | 中 |
| `gambetta2025surplexity` arXiv:2410.12341 | "Surplexity" 是自造术语，arXiv ID (2410) 对应 2024 年 10 月，相对可查 | 低-中 |

**bib 文件格式问题：**

- `tirumala2024d4`：bib key 含 "2024" 但 `year={2023}`，NeurIPS 2023 — 年份字段正确但 key 误导
- `xie2024doremi`：同上，key 含 "2024" 但 `year={2023}` — NeurIPS 2023
- `zawalski2026codec` 和 `amin2025escaping`：作者字段用 `{others}` 偷懒，最终提交前必须补全完整作者列表

**bib 文件头部声明（line 2-3）明确标注 "PENDING formal verification"** — 说明团队自身也意识到需要验证。建议在提交前用 Semantic Scholar API 或手动逐条核实所有 2025-2026 引用。

---

### 4. 结构完整性

**当前结构（4 段）：**
1. Model Collapse and Recursive Generation ✅
2. Binary Synthetic Text Detection ✅
3. Data Selection and Curation ✅
4. Watermarking and Provenance ✅

**Gap statement 检查：**
- ¶1 line 14: "do not provide tools for per-text generational depth estimation" ✅
- ¶2 lines 23-26: "produce binary outputs and do not distinguish generational depth" ✅
- ¶3 lines 35-36: "We generalize this binary formulation to ordinal depth estimation" ✅
- ¶4 lines 43-44: "watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings" ✅

每段结尾的 gap statement 都清晰地指向本文贡献，叙事逻辑通顺。

**结构性缺陷：**

- **缺少 Ordinal Classification 段落**：论文核心贡献是将 binary 问题升级为 ordinal 问题，但 related work 没有任何 ordinal regression/classification 文献。这是一个明显的结构缺口——reviewer 几乎一定会问 "why ordinal and not standard multi-class?"。建议在 Binary Detection 和 Data Selection 之间插入一段，讨论 ordinal 方法及其在 NLP 中的应用。

- **Binary Detection 段落偏长**（lines 17-26, ~10 行正文）：包含了方法枚举 + 限制分析 + membership inference 联系 + false positive 讨论。可以考虑将 false positive / self-refinement 讨论移到 introduction 或 discussion。

---

### 改进建议清单

| 优先级 | 建议 |
|--------|------|
| **P0** | 补充 Binoculars (Hans et al. 2024) 到 Binary Detection 段 |
| **P0** | 新增 Ordinal Classification 段落（~5-8 行），引用 CORAL 等经典方法 |
| **P0** | 验证所有 2025-2026 引用的真实性（bib 文件自己也标了 PENDING） |
| **P1** | 补充 GLTR (Gehrmann et al. 2019) 作为 statistical detection 起源 |
| **P1** | 补全 `zawalski2026codec` 和 `amin2025escaping` 的完整作者列表 |
| **P1** | 修正 `tirumala2024d4` 和 `xie2024doremi` 的 bib key 与 year 不一致 |
| **P2** | Data Selection 段补充 heuristic quality filtering 线（CCNet/RefinedWeb） |
| **P2** | 考虑加一句区分 benchmark contamination detection 与本文的 generational contamination |
| **P2** | 补充 Fast-DetectGPT 到 Binary Detection 段 |

---
