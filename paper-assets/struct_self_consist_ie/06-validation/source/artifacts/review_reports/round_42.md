---
round: 42
review_mode: continue
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T07:23:38.479102+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 42 (Continue)

**论文**: "Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap"
**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性; R2: 新颖性/完整性）
**审稿模式**: 继续审稿（基于 R41 修改验证）
**交叉分享**: R1, R2 均完成交叉回应，达成部分共识

---

## Summary

Round 42 是对 R41 提出的 5 个 Must-Fix、6 个 Should-Fix 的修改验证轮。论文对全部 5 个 Must-Fix 进行了实质性修改：§6.3 将 bound 重定位为 necessary condition screening test；§7.5 透明报告双重 p 值并提供 family 划分先验理由；§4 标注 probe 模型差异并新增 Qwen3-8B ESJ 交叉验证；§2 扩展 Landesberg 系统对比为 4 维度 + Table 1 增加 failure mechanism 行；Abstract 对 +1.40pp 加入 3-epoch 条件限定。Should-Fix 中 4 项（W1 叙事定位、W3 RE/SQL 措辞、W4 缺失引用、W6 free-form ablation）已修复。

两位 Reviewer 对所有 R41 Must-Fix 验证为 RESOLVED，Soundness 达成共识升至 4.0。评分分歧：R1=4.0 (Conference)，R2=3.5 (Borderline Conference)。分歧根源为 Excitement 的主观权重——R2 认为 concurrent discovery (Landesberg 2026) 限制了 novelty increment，R1 认为诊断框架的系统性分析具有独立 Conference 价值。双方明确认为 3.5-4.0 均为合理评分。

---

## R41 Issue Resolution Status

### Must-Fix（5/5 RESOLVED — 双方共识）

| ID | Issue | R42 Status | 说明 |
|----|-------|-----------|------|
| N1 | Bound 仅恢复 3-12% | ✅ RESOLVED | §6.3 成功重定位为 "intentionally loose necessary condition test"，不再 oversell |
| N2 | 统计显著性依赖校正方案 | ✅ RESOLVED | §7.5 双 p 值透明报告（global 0.055, per-family 0.006），family 划分有先验理由，明确声明 not pre-registered |
| N3 | Probe 模型不一致 | ✅ RESOLVED | §4 显式标注 Qwen2.5-7B-Instruct，ESJ Qwen3-8B 交叉验证确认 chance-level (AUROC 0.50-0.55)，Limitations 更新 |
| N4 | Landesberg 区分不足 | ✅ RESOLVED | §2 扩展为 4 维度系统对比（domain/mechanism/granularity/prescriptive），Table 1 新增 failure mechanism 行 |
| N5 | Epoch confound 削弱正面结果 | ✅ RESOLVED | Abstract 限定 "under 3-epoch training; diminishes at convergence"，§7.5 完整呈现 94%/77% reduction |

### Should-Fix（4/6 RESOLVED, 2 open — response-letter items）

| ID | Issue | R42 Status | 说明 |
|----|-------|-----------|------|
| W1 | Diagnostic/prescriptive 不一致 | ✅ RESOLVED | 全文统一为 "primarily diagnostic with limited predictive power" |
| W2 | 2-3 seeds 统计推断力不足 | ⚪ OPEN | Response-letter item，论文未修改 |
| W3 | RE/SQL 扩展过薄 | ✅ RESOLVED | Abstract "preliminary RE (n=397) and SQL (n=196) pilots" 措辞充分 |
| W4 | Related Work 遗漏 | ✅ RESOLVED | Eikema et al. (2025), li2026rewardtail, desai2020calibration, xiao2022uncertainty 全部添加 |
| W5 | Entity-level 增量论证不足 | ⚪ OPEN | Response-letter item，论文未修改 |
| W6 | Free-form ablation 不足 | ✅ RESOLVED | 扩展到 SciERC + CoNLL + Few-NERD（LP std ratio 0.86×-1.00×），Discussion 引用跨数据集证据 |

---

## Strengths（承袭 R41 + R42 新增）

1. **研究问题重要且定位精准**：SC 在结构化预测上失败的诊断分析填补社区空白。[R1, R2 共识，承袭]

2. **实验极其详尽且透明**：4 数据集 × 2 模型家族 × 5 信号 × 9 方法类别，59 个 tables + 11 个 figures 的附录，统计检验覆盖面在 NLP 实证研究中属上乘。三重统计校正透明报告 + 非预注册声明超越 NLP 领域标准实践。[R1, R2 共识，承袭+R42增强]

3. **Degeneracy 概念有实证价值**：12-68% 的 NER 实例产生相同 entity set，作为 pre-deployment check 有应用价值。[R1, R2 共识，承袭]

4. **MBR decoding 理论连接**：Proposition 1 将 entity construction 形式化为 MBR 特例，理论锚点清晰。Eikema et al. (2025) 引用增强了文献连接。[R1, R2 共识，承袭+增强]

5. **R42 修改质量高**：所有 Must-Fix 修改实质性地解决了问题。R2 特别指出：epoch confound 的 reframing 和三重统计校正的透明报告是高质量的学术回应，超越 surface-level 修补。修订展现了良好的学术素养。[R1, R2 共识，R42 新增]

6. **Claims-evidence 对齐**：R42 版本达到了 claims 与 evidence 的良好对齐——没有 overclaim，边界清晰，hedging 恰当。R2 认为这是 Conference 级论文的必要条件（但非充分条件）。[R1, R2 共识，R42 新增]

7. **Negative results 诚实报告**：明确报告 cross-dataset transfer 失败、RE 局限、epoch confound。Appendix ah 自审 12 个 potential objections。[R2，承袭]

8. **Reproducibility 高**：承诺开源代码/checkpoint/数据，超参数报告详尽。[R1, R2 共识，承袭]

---

## Remaining Weaknesses

### R42 新发现问题（2 项 — 双方共识不影响评分）

**NEW-1** [R1 AGREE, R2] **Abstract/§7.5 数值引用不一致** (warning)
- Abstract: "Entity-level construction yields conditional gains (+1.40pp on Few-NERD under 3-epoch training; diminishes to +0.09pp at convergence)"
- +0.09pp 是 LP selection（非 entity construction）在 5-epoch 下的数字
- Entity construction 在 5-epoch 下应为 +0.20pp（§7.5: "entity construction: +0.88→+0.20pp"）
- 同一句中混淆了两个不同 metric
- **双方共识**：camera-ready 级修正项，不影响核心结论（无论 0.09 还是 0.20，5-epoch 收益接近零，epoch confound 结论不变）
- **建议**：修正为 "+1.40pp...diminishes to +0.20pp at convergence" 或拆分两个 metric

**NEW-2** [R1 AGREE, R2] **§7.5 entity construction 3-epoch 数字不一致** (info)
- §7.5 Prescriptive Results: "LP-weighted construction yields +1.40±0.51pp"
- §7.5 Training convergence: "entity construction: +0.88→+0.20pp, 77% reduction"
- 同一 subsection 中 3-epoch entity construction 出现 +1.40pp 和 +0.88pp 两个值
- 可能源于不同变体（LP-weighted vs uniform），但未明确标注
- **双方共识**：camera-ready 级修正项，不影响核心判断
- **建议**：统一标注变体名称

### R41 遗留未修改问题（2 项 open Should-Fix + 1 项 divergence）

**W2** [承袭] 2-3 seeds 统计推断力不足 — Response-letter item

**W5** [承袭] Entity-level decomposition 增量贡献需更强论证 — Response-letter item

**D2** [持续分歧] 正文数字密度过高 — R2 认为影响可读性，R1 认为诊断论文属性

**D1** [R2 撤回] 标题 "Why SC Fails" 匹配度 — R2 在交叉回应中撤回此关注："标题是风格选择，不应影响实质性评分"

---

## Questions（R42 残留）

1. Abstract 中 "+0.09pp at convergence" 应改为 "+0.20pp"（entity construction）或明确标注为 LP selection？[R1, R2 共识]
2. §7.5 中 "+1.40pp" (LP-weighted) 与 "+0.88pp" (generic entity construction) 的关系——如果是不同变体，77% reduction 的基线是哪个？[R1, R2 共识]
3. §4 "AUROC 0.50-0.55" vs §5 "AUROC 0.50-0.52" 可能源于不同实验子集（entity-level vs class-level），应标注来源。[R1 发现, R2 AGREE]

---

## Missing References

R41 指出的遗漏已全部修复。R42 无新的遗漏引用。

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿（状态：not_requested）。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时 ~4 分钟）

| 严重度 | 页面 | 发现 |
|--------|------|------|
| 🔴 critical | p.23 | 几乎空白页：仅顶部 9 行文字，~85% 空白。应合并到前/后页 |
| ⚠️ warning | p.7 | 三个 display items 挤在同一页，Figure 尺寸偏小 |
| ⚠️ warning | p.2 | Figure 1 内部注释文字偏小 |
| ℹ️ info | p.15 | Figure 7 热力图灰度打印区分度下降 |
| ℹ️ info | p.8 | 主文最后一页纯文本（Discussion/Conclusion 可接受） |
| ℹ️ info | p.46 | Table 69 文字约 6-7pt |
| ℹ️ info | p.12 | Figure 5 字号偏小但可读 |
| ℹ️ info | pp.12-47 | 附录 36 页，建议开头加导读 |

1 critical（Appendix 空白页）, 2 warning, 5 info。主文排版无阻断问题。

---

## Score Divergence Analysis

### R1 评分：4.0 (Conference) — 维持
**核心论据**：
- Must-Fix 全部解决，修改展示深入理解
- Bound 重定位、ESJ 跨模型验证、free-form ablation 增强证据链
- 系统性诊断分析（解释一个广泛观察到但未被理解的现象）具有独立 Conference 价值
- Claims-evidence 正确对齐

### R2 评分：3.5 (Borderline Conference) — 维持（附维度更新）
**核心论据**（交叉回应后精炼）：
- **决定性因素**：Landesberg (2026) 独立发现 correlation-selection gap 限制了 Excitement 上限。论文从 "discovering a new phenomenon" 降级为 "extending a known phenomenon to a new domain with mechanistic analysis"——有价值但 incremental
- **支撑性因素**：Entity construction 正面结果 conditional 且 global p_adj=0.055，不足以作为独立卖点。如果论文完全放弃正面 claim（纯负面结果 + 诊断），R2 可能反而更倾向 4.0
- **撤回**：标题关注（"标题是风格选择，不应影响实质性评分"）
- R2 明确认可 4.0 是 "一个合理的评分"，R1 论据 "在逻辑上是自洽的"

### 交叉回应后达成的共识

| 项目 | R1 | R2 | 状态 |
|------|----|----|------|
| R41 Must-Fix 全部 RESOLVED | ✅ | ✅ | **共识** |
| Soundness 4.0 | ✅ | ✅ | **共识**（R2 从 3.5 升至 4.0） |
| Excitement | 3.5 | 3.0 | **分歧**（0.5 差距） |
| Overall | 4.0 | 3.5 | **分歧**（0.5 差距） |
| NEW-1/NEW-2 不影响评分 | ✅ | ✅ | **共识** |
| 3.5-4.0 均为合理评分 | ✅ | ✅ | **共识** |

### Director 判断
分歧已收敛至最小可能范围：双方在所有事实判断上一致（issue 状态、Soundness 4.0、NEW-1/NEW-2 为 camera-ready 修正），唯一分歧点是 Excitement 的主观权重——R1 认为 well-documented negative result + 诊断框架对社区的信息价值值 3.5，R2 认为 concurrent discovery 限制信息增量至 3.0。这是合理的主观分歧，不可通过额外论证消解。

---

## Overall Assessment

**评分**: 3.5 / 5 (Borderline Conference)
**置信度**: 4 / 5
**相较 R41 变化**: 从 "weak 3.5" 提升至 "strong 3.5 / borderline 4.0"

### 维度分数

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 4.0 | 4.0 | **4.0**（共识） |
| Excitement | 3.5 | 3.0 | 3.0-3.5 |
| Reproducibility | 4.0 | 4.0 | **4.0**（共识） |

### 评分理由

论文在 R42 中展示了对所有 R41 Must-Fix 的高质量修改回应。5 个 critical issues 全部 RESOLVED，Soundness 达成 4.0 共识。这是显著的进步——R41 的 5 个 Must-Fix 从根本上动摇了论文的核心贡献支柱，R42 的修改全部实质性解决。

维持 3.5 而非升至 4.0 的原因：
1. **Excitement 分歧**：Concurrent discovery (Landesberg 2026) 如何影响论文信息增量是核心争议。R2 的分析有理：对一个读过 Landesberg 的读者，本文的增量贡献从"发现新现象"变为"已知现象的领域扩展 + 机制分析"。这一区分直接降低 Excitement 评分。
2. **Prescriptive 贡献条件化**：R2 指出一个微妙观察——如果论文完全放弃正面 claim（纯负面结果），其作为 clean negative result 的价值可能更高。当前仍试图 claim entity construction 的条件性正面结果，使 limited impact 成为削弱因素。

论文的 lower bound 为 3.0 (Findings)。R1 的 4.0 评估合理反映了修改后论文的 Soundness 和 transparency 提升，以及对诊断框架独立价值的合理评估。

**最终建议**：**3.5 (Borderline Conference)**。Conference accept 或 Findings accept 均为合理结果（R2 原话："无论最终决定是 Conference accept 还是 Findings accept，都不会是错误判断"）。

### 与 R41 的进步

| 指标 | R41 | R42 |
|------|-----|-----|
| Must-Fix | 5 open | **0 open (全部 RESOLVED)** |
| Should-Fix | 6 open | **2 open (response-letter items)** |
| Soundness | 3.5 / 3.5 | **4.0 / 4.0 (共识升级)** |
| Excitement | 3.5 / 2.5 | 3.5 / 3.0 (R2 +0.5) |
| Overall | 3.5 / 3.5 | 4.0 / 3.5 (R1 升级) |
| Claims-evidence 对齐 | 有 overclaim | **无 overclaim** |
| 统计透明度 | Cherry-picked | **三重校正全部透明** |

### 遗留问题清单

Camera-ready 或下轮修正：
1. **NEW-1** (warning): Abstract "+0.09pp" 应改为 "+0.20pp" 或分别报告
2. **NEW-2** (info): §7.5 明确标注 LP-weighted vs uniform construction
3. **AUROC minor**: §4 vs §5 的 AUROC 范围标注来源
4. **W2** (response-letter): 3 seeds 统计推断力
5. **W5** (response-letter): Entity-level vs task-level 增量论证
6. **Visual p.23**: Appendix 空白页

---

## Detailed Comments

### §Abstract
- R41 修改验证：条件限定（"under 3-epoch training"）到位
- **NEW-1**："+0.09pp at convergence" 混淆 LP selection 与 entity construction → 必须修正
- 双 p 值报告透明度好

### §2 Related Work
- Landesberg 4 维度系统对比充分，Table 1 七维度清晰
- 新增引用（Eikema, calibration, TTS）全部到位
- R2 交叉回应确认：differentiation RESOLVED，但 novelty increment 仍受 concurrent discovery 限制——这是评估性判断而非论文缺陷

### §4 Where Single-Signal Selection Fails
- Probe 模型标注到位，Qwen3-8B ESJ 交叉验证增强证据链
- R2 承认在 R42 初审中可能遗漏了 ESJ 跨模型验证这一改进
- AUROC 0.50-0.55 vs 0.50-0.52 minor inconsistency → camera-ready 修正

### §6.3 Degeneracy Decomposition
- 重定位成功——"intentionally loose necessary condition test"
- R2 确认：这一重定位从 overselling 转为诚实定位，是正确的学术选择

### §7.5 Prescriptive Results
- Family 划分先验理由到位
- 三重校正透明报告（R2："超越 NLP 领域标准实践"）
- **NEW-2**：+1.40pp vs +0.88pp 需区分标注
- Epoch confound 完整呈现

### §8 Discussion/Conclusion
- LP compression 跨数据集确认（std ratio 0.86-1.00×）
- 定位一致

### Limitations
- 覆盖充分，长度适当
- Probe 模型差异 + ESJ 复制 + free-form 跨数据集 + 双 p 值 均已到位