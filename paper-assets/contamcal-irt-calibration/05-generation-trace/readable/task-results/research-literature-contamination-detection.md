# research literature contamination detection

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-contamination-detection_20260514T084624_result.json`
- **Structured JSON:** [`db4188c19889625d7f29.json`](../../sessions/db/db4188c19889625d7f29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有完整信息可以做 gap 分析了。

## Gap 分析结果

### 已覆盖的主题

| 主题 | 状态 | 覆盖位置 |
|------|------|----------|
| IRT for LLM evaluation | ✅ 充分 | 6 篇 (PSN-IRT, Growing Pains, ATLAS, TinyBenchmarks, HiBayES, Lalor) |
| Contamination detection methods | ✅ 充分 | 6 篇 (Min-K++, ConStat, Self-Critique, KDS, Oren, CDD) |
| Contamination mitigation & impact | ✅ 充分 | 5 篇 (Emperor, Dong dose-response, Yang RL, Zhang forget, LiveBench) |
| Item compromise in educational measurement | ✅ 充分 | 4 篇 (Eckerly, Sinharay, De Boeck, Mislevy) |
| DIF literature | ✅ 充分 | 3 篇 (Holland, Thissen, Zumbo) |
| Score adjustment / decontamination | ✅ 充分 | 3 篇 (DCR, Inference-Time Decontam, Silicon Bureaucracy) |
| ML calibration disambiguation | ✅ 有 | 1 篇 (Guo 2017) |
| Conformal prediction alternative | ✅ 有 | 1 篇 (Angelopoulos 2023) |
| Data attribution (Future Work) | ✅ 有 | 2 篇 (TracIn, TRAK) |
| Multidimensional IRT | ✅ 有 | 1 篇 (Reckase 2009) |

### 缺失的 4 个主题（与 exp-004 bias 反转发现直接相关）

**1. Exposure-ability collinearity / confounding in IRT — GAP**
- exp-004 发现高 AUC 下 posterior variance inflation 源于 exposure-ability collinearity，γ 被低估 (−0.016)
- `references.bib` 和 `related_work.tex` 中**零篇**讨论 IRT 参数 collinearity 或 confounding 的文献
- 需要引用：educational measurement 中关于 ability-covariate confounding 的理论工作（如 Haberman 2007 关于 person-fit 与 ability confounding；Wainer & Thissen 2000 关于 testlet effects 导致的参数相关性）
- **Discussion 必须有理论支撑来解释 bias 方向反转机制**

**2. Signal quality (AUC) 与 calibration 精度的关系 — GAP**
- exp-004 核心发现之一：AUC=0.55 即可恢复 γ，但高 AUC 反而引入 attenuation bias
- 没有文献讨论 detection signal quality 如何影响下游 calibration 任务
- 这可能是 ContamCal 的 **novel finding**，Discussion 中需与 measurement error literature 对接（如 Carroll et al. 2006 "Measurement Error in Nonlinear Models" 中 attenuation bias 的经典理论）

**3. Item-level contamination detection 的 power analysis — GAP**
- Fisher Information 推导已完成（appendix.tex），但 `references.bib` 中没有 power analysis / sample size determination 在 IRT 中的文献
- 需要引用：Thissen & Wainer 2001 ("Test Scoring") 关于 IRT 参数估计精度；或 Embretson & Reise 2000 ("Item Response Theory for Psychologists") 关于信息函数与精度的关系

**4. 4PL IRT model 在 LLM evaluation 中的应用 — 部分覆盖**
- PSN-IRT 用了 4PL，已引用
- 但缺少对 4PL 中 upper asymptote (d parameter) 在 LLM 场景下合理性的讨论文献。Barton & Lord 1981 是 4PL 原始提出；Liao et al. 2012 讨论 4PL 的 identifiability 问题——与 exp-004 的 identifiability 研究直接相关

### 建议优先级

| 优先级 | Gap | 对论文的影响 |
|--------|-----|-------------|
| **P0** | Exposure-ability collinearity 文献 | Discussion 中 bias 反转解释无理论支撑 |
| **P0** | Measurement error attenuation bias 文献 | 同上，且与 C3 claim (identifiability) 直接相关 |
| **P1** | IRT power analysis / information function 文献 | Appendix Fisher 推导需要引用 |
| **P2** | 4PL identifiability 文献 | 强化方法选择的理论论证 |

**结论**：literature_map.yaml 需要创建。当前 references.bib 有 39 篇，覆盖了 paper_framing.md 中 Dream D2 要求的大部分类别，但**缺失与 exp-004 bias 反转发现直接相关的理论文献**——特别是 collinearity/confounding 和 measurement error attenuation 两个方向。这两个 gap 会让 Discussion section 中对 "高 AUC 下 γ 被低估" 的解释缺乏理论锚点。

---
