# Paper Preparation Audit — symb_invariant_consensus
> 审查日期: 2026-05-16 | D012 checkpoint: May 19 UTC

## 1. paper_framing.md — ❌ 不存在

文件缺失。当前无论文叙事框架文档。

ROADMAP.md 有方法概述（SICA = 符号约束 + partial MAX-SAT 替代统计共识）和模型 pivot 背景，但属于运营文档，不是论文叙事。需要创建 paper_framing.md，至少覆盖：

- **Narrative arc**: reasoning model 自一致性过强 → SICA 需要 trace 多样性 → 非 reasoning model（14B）提供操作空间 → SICA 在逻辑域超越 SC
- **Contribution framing**: (1) SICA 方法本身, (2) 发现 reasoning model vs non-reasoning model 对 SC 类方法的结构性差异, (3) 符号约束提取 + MAX-SAT 的可解释性
- **Target venue positioning**: EMNLP 2026 (May 25 ARR) 主投，AAAI 2027 (Aug 1) 后备

**状态**: 🔴 需从零创建

## 2. writing_plan.yaml — ❌ 不存在

文件缺失。无写作计划、章节分工、时间线。

若 D012 PASS（May 19），到 ARR May 25 只有 ~6 天写完全文，极其紧张。需要立即创建 writing_plan，包含：
- 章节结构与内容大纲
- 图表清单（至少需要：pipeline overview, multi-candidate rate comparison QwQ vs 14B, accuracy table, constraint extraction example）
- 写作优先级排序（实验/方法 > intro/related work）
- 日历级时间线

**状态**: 🔴 需从零创建

## 3. literature_map.yaml — ❌ 不存在

文件缺失。无文献覆盖评估。

需要覆盖的关键领域：

| 类别 | 需覆盖的工作 | 状态 |
|------|-------------|------|
| **直接竞争者** | Self-Consistency (Wang et al. 2023), CRAFT, Universal Self-Consistency (USC) | ❌ 未整理 |
| **符号推理+LLM** | Logic-LM, LINC, SatLM, Faithful CoT | ❌ 未整理 |
| **LLM 逻辑推理** | Chain-of-Thought, Tree-of-Thought, reasoning scaling laws | ❌ 未整理 |
| **MAX-SAT/约束求解** | partial MAX-SAT 文献, Z3 in NLP | ❌ 未整理 |
| **模型多样性/采样** | reasoning model 自一致性相关研究 | ❌ 未整理 |
| **数据集** | ProofWriter, FOLIO 原始论文 | ❌ 未整理 |

**状态**: 🔴 需从零创建

## 4. 实验格子状态

### 已完成 ✅
| 实验 | 模型 | 数据 | 结论 |
|------|------|------|------|
| sica_d016_c0_precheck | Qwen2.5-14B | FOLIO-10 + PW-16 (26q) | C0 PASS: 46% 多候选率 |
| sica_aime30_v3 | QwQ-32B | AIME 22/30 | 0% 多候选, SICA≡SC |
| sica_proofwriter30_v2 | QwQ-32B | ProofWriter 16/30 | 18.75% 多候选, D012 FAIL |
| sica_folio30 | QwQ-32B | FOLIO-30 | killed, 被 D012 覆盖 |
| sica_temp_diversity | QwQ-32B | 3q diagnostic | 0 分歧, T=0.7/0.9/1.0 均无效 |
| sica_smoke_5q | QwQ-32B | MATH 5q | Pipeline 验证通过 |
| crd_folio_main | Qwen3-32B-AWQ | FOLIO 204q | CRD 方法, 非 SICA |

### 正在运行 🔄
| 实验 | 模型 | 数据 | 说明 |
|------|------|------|------|
| **sica_d012_14b** | Qwen2.5-14B | PW-30 + FOLIO-30 (60q), K=12 | **关键 D012 评估**, PID 177178 |

### 仍需补充（若 D012 PASS）
| 缺口 | 优先级 | 说明 |
|------|--------|------|
| K 消融 (K=4,8,12,16) | P1 | Reviewer 必问：K 对结果的影响 |
| Temperature 消融 (T=0.5,0.7,0.9) | P1 | 采样多样性敏感度 |
| 更大规模验证 (100+ 题) | P2 | 30+30=60 题可能被质疑统计效力 |
| 其他非 reasoning model 对比 | P2 | Llama-3-70B 等, 排除模型特异性 |
| SC 以外的 baseline | P2 | USC, CRAFT 等直接竞争者 |
| Error analysis / case study | P1 | SICA 翻转成功/失败的典型案例 |

## 5. D012 PASS 后 Ready/Not-Ready 清单

### ✅ Ready
- [x] SICA pipeline 代码完整，端到端可运行
- [x] 模型 pivot 叙事清晰（ROADMAP + memory 有完整记录）
- [x] QwQ-32B 负面结果充分（~56 题跨三域, 3.6% 多候选率）
- [x] C0 预检数据可用作 pilot study
- [x] MaxSAT 求解器验证通过（注入测试 6/6）
- [x] L3+L1 修复有代码 commit 记录
- [x] 服务器环境就绪（vLLM 14B 运行中）

### ❌ Not Ready
- [ ] **paper_framing.md** — 论文叙事框架不存在
- [ ] **writing_plan.yaml** — 写作计划不存在
- [ ] **literature_map.yaml** — 文献地图不存在
- [ ] **LaTeX 模板** — 未选择/设置（EMNLP 2026 模板）
- [ ] **消融实验** — K/T 消融未做，D012 只是单点结果
- [ ] **额外 baseline** — 仅对比 SC，缺 USC/CRAFT
- [ ] **统计检验** — 60 题样本量需要 paired bootstrap 或 McNemar test 准备
- [ ] **图表** — 无任何论文图表

### ⚠️ 风险
- **时间极紧**: D012 结果 May 19 → ARR May 25 只有 6 天
- **60 题样本量**: Reviewer 可能质疑统计效力，建议准备 bootstrap CI
- **单模型**: 仅 Qwen2.5-14B，如被质疑模型特异性缺乏回应数据
- **EMNLP vs AAAI**: 若 May 25 来不及，AAAI Aug 1 有更多时间做消融

## 6. 建议优先级（若 D012 PASS）

1. **立即**: 创建 paper_framing.md + writing_plan.yaml + literature_map.yaml
2. **Day 1-2**: 写 Method + Experiments 章节（最独立，不依赖后续数据）
3. **Day 2-3**: 画核心图表（pipeline overview, accuracy table, multi-candidate comparison）
4. **Day 3-4**: K/T 消融实验（可与写作并行）
5. **Day 4-5**: Introduction + Related Work + Analysis
6. **Day 6**: Abstract + 全文打磨 + 引用检查