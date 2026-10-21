# research paper readiness audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-readiness-audit_20260515T012853_result.json`
- **Structured JSON:** [`03ae43720ea1a78f3a4a.json`](../../sessions/03/03ae43720ea1a78f3a4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

# 论文就绪度审计报告

**项目**: gen-depth-fingerprint  
**日期**: 2026-05-15  
**目标投稿**: EMNLP 2026 ARR (deadline: May 25, 2026) — 剩余 **10 天**

---

## 1. Framing 审计

paper_framing.md 定义了 3 条 core claims + 11 个 reviewer concerns (RC1–RC11)。逐条证据映射：

| Claim / RC | 要求的证据 | 现状 | Gap |
|---|---|---|---|
| Claim 1 — Depth Discriminability | LOGO F1 显著高于 chance，跨生成器泛化 | ✅ LOGO 0.80 [0.786, 0.799]，LOFO 0.77 | 无 |
| Claim 2 — Differential Response | drift vs stationary 分离 + 3 ref model 验证 | ✅ plan-001 + plan-003 confirmed | 无 |
| Claim 2 — Complementarity | 7-feat > surface-only + ref-only | ✅ plan-015: p<0.001 vs all baselines | 无 |
| Claim 3 — Downstream Utility | depth-aware filtering > binary filtering，多种子+CI | 🔄 plan-004-v2: 5/15 runs done，ETA ~2h | **阻塞**：数据不全 |
| RC1 — Length confound | 长度非混淆因素 | ✅ plan-013: 三重证据 | 无 |
| RC2 — Beyond Pythia | 跨家族泛化 | ✅ plan-003: 3 ref models，LOGO 0.80-0.82 | 无 |
| RC7 — LD-Score 预注册 | LD-Score 作为 level feature 验证 | ✅ plan-015 确认 | 无 |
| RC8 — OOD detection 定位 | 论文承认特征是标准 NLL 统计量 | ⚠️ 仅在 framing 中规划，未落笔 | 需在写作中体现 |
| RC9 — 7B+ Generator | 至少一个 7B+ 生成器 | 🔄 plan-014: Qwen3-8B 265/996 seeds，ETA ~3h | **阻塞**：待完成+特征提取+评估 |
| RC10 — Length confound control | 同 RC1 | ✅ | 无 |
| RC11 — Downstream 多种子 | OLMo-1B + 多种子 + CI | 🔄 同 Claim 3 | **阻塞** |

**结论**：Claim 1 和 Claim 2 证据完备。Claim 3 和 RC9 各有一个 running 实验阻塞。

---

## 2. 可立即开写的章节

| Section | 理由 | 预估工作量 |
|---|---|---|
| **Method** | 特征提取管线（7 features）、XGBoost 分类器、LOGO/LOFO 协议全部确定 | 2-3 天 |
| **Experimental Setup** | 5 generators、3 ref models、4 domains、生成参数、评估指标全部固定 | 1-2 天 |
| **Results §1-2** (Claim 1 + 2) | 所有数字、CI、显著性检验均已产出 | 2-3 天 |
| **Introduction** (框架) | story spine 已定义，可先写 draft | 1 天 |
| **Related Work** (骨架) | 方向明确但需大量引用填充 | 见下文 |

---

## 3. 等待中的章节

| Section | 阻塞因素 | ETA |
|---|---|---|
| **Results §3** (Downstream Utility) | plan-004-v2 完成 + 结果分析 | 5/15 晚间（ETA ~2h for runs，+数小时分析） |
| **Results §4** / Discussion (7B+ Scale) | plan-014 完成 + 特征提取 + LOGO 评估 | 5/15–5/16（ETA ~3h generation + 后处理） |
| **Discussion / Limitations** | 需要全部实验结果才能写出完整 limitations | 5/16–5/17 |
| **Abstract / Conclusion** | 需 Claim 3 和 RC9 最终数字 | 最后写 |

---

## 4. 文献覆盖

**严重缺失**。`literature_map.yaml` 不存在。paper_framing.md 列出了需要覆盖的 30+ 引用类别：

| 文献线 | 状态 | 紧迫度 |
|---|---|---|
| Perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars) | 仅在 framing 中提及名字 | 🔴 高 |
| Model collapse theory (Alemohammad, Dohmatob, Gerstgrasser, Guo) | 同上 | 🔴 高 |
| OOD detection (Hendrycks & Gimpel) | 同上 | 🔴 高 |
| Data quality scoring (DSIR, QuRating, CCNet) | 同上 | 🟡 中 |
| Watermarking (Kirchenbauer et al.) | 同上 | 🟡 中 |
| Vocabulary diversity (Guo 2024, Padmakumar & He 2024, Holtzman 2020) | 同上 | 🔴 高 |
| **Stylometry/authorship attribution** (Stamatatos, Koppel) | 同上 | 🔴 高 |
| Iterative generation (Broken Telephone ACL 2025, Markovian chains) | 同上 | 🔴 高（direct competitor） |
| Membership inference (Shi et al. 2024) | 同上 | 🟡 中 |

**风险**：无 literature_map 意味着目前没有确认任何引用的真实性和完整书目信息。按 framing 要求 30+ 引用，从零构建 related work 需要 2-3 天集中精力。

---

## 5. EMNLP 可行性评估

### 时间线（今天 5/15 → deadline 5/25）

| 日期 | 里程碑 | 前置条件 |
|---|---|---|
| 5/15–5/16 | plan-004-v2 + plan-014 完成；开始 Method + Setup 写作 | 实验按时完成 |
| 5/16–5/17 | plan-014 后处理（特征提取+LOGO）；Claim 1+2 Results draft | — |
| 5/17–5/19 | Claim 3 Results + Scale results；Related Work 填充 | 文献搜索并行 |
| 5/19–5/21 | Introduction + Discussion + Limitations | 全部数字就绪 |
| 5/21–5/23 | Abstract + Conclusion；全文统稿；图表制作 | — |
| 5/23–5/24 | 内审 + 校对 + LaTeX 排版 | — |
| 5/25 | 提交 | — |

### 判断：**极其紧张但技术上可行，前提是：**

1. plan-004-v2 和 plan-014 在 5/16 前完成且结果正面
2. 论文 scope 收窄为 EMNLP stretch 版本（RQ1+RQ4 minimal scope，如 framing 所定义）
3. 写作立即并行启动（Method/Setup 今天就开始）
4. Related Work 采用高效策略（先搜集 BibTeX，骨架式写作）
5. 如果 plan-014 结果不支持 RC9（7B+ signal 弱），诚实报告为 limitation 而非等新实验

### 现实风险评估：**建议以 AAAI 2027 (Aug 2) 为主目标**

EMNLP 10 天内从零写完一篇 8 页论文 + 30+ 引用，同时还在等 2 个关键实验，容错率接近零。任何一个环节延误（实验结果不理想需要修补、图表迭代、写作瓶颈）都会导致无法按时提交。

---

## 6. 风险清单

| 风险 | 概率 | 影响 | 缓解 |
|---|---|---|---|
| plan-004-v2 结果不显著（depth-aware filtering 优势不明显） | 中 | 🔴 Claim 3 丢失，论文从 3-claim 降为 2-claim | 调整为 "depth signal exists but downstream utility requires further investigation"；EMNLP minimal scope 本就只需 RQ1+RQ4 |
| plan-014 7B+ depth signal 弱 | 中 | 🟡 RC9 unresolved，但可报告为 honest limitation | 论文写 "future work"，不阻塞提交 |
| 文献覆盖不足被 desk reject | 高 | 🔴 直接拒稿 | 立即启动 literature_map 构建，优先覆盖 direct competitor |
| 无 writing_plan / paper_checklist / paper_provenance | 高 | 🟡 写作效率低、溯源困难 | 立即创建 writing_plan.yaml 分配写作任务 |
| GPU 预算接近上限（119.5h/200h） | 低 | 🟡 若需补充实验可能不够 | 剩余 80h 足够 plan-004-v2 + plan-014，但无余量做新实验 |
| 10 天写完整篇论文 | 高 | 🔴 质量不达标或无法按时提交 | 优先保证 AAAI 2027，EMNLP 作为 stretch goal |

---

## 总结

**证据就绪度：~70%**。Claim 1+2 完备，Claim 3 和 7B+ scale 预计 24h 内有结果。核心 gap 不在实验而在 **写作基础设施**：无 writing_plan、无 literature_map、无 paper_checklist，从零写 8 页论文+30 引用需要至少 7-8 天净工时。

**建议**：立即启动可并行的写作（Method / Setup / Claim 1+2 Results），同时构建 literature_map。以 AAAI 2027 (Aug 2) 为主目标，EMNLP 仅在一切顺利时作为 stretch 尝试。

---
