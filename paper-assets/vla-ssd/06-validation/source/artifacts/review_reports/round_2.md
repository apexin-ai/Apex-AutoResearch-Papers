---
round: 2
overall_score: borderline
timestamp: 2026-05-17T06:11:31.855672+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 圆桌审稿报告 — Round 2（修订评估）

**论文**: "Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models"
**Venue**: CoRL 2026 (Deadline: 2026-05-29)
**Reviewers**: R1 (方法/实验), R2 (新颖性/意义), R3 (写作/格式)

---

## Summary

Round 2 论文在写作和 framing 层面有实质改善：删除 "first" novelty claim、Related Work 从 3 段扩展至 5 段（+12 引用）、新增 "Why RSA over CKA" 方法论辩护、正文 em-dash 全部清除、Limitations 内容大幅扩展、confound 在实验章节显式 acknowledge。但核心科学问题（Llama-2 base 对照缺失、design implications 的因果 gap）未通过新实验数据解决，Abstract/Conclusion 的 assertive 语气与 Limitations 的 caveats 存在不一致。

---

## Round 1 → Round 2 变化总结

### 已解决 (RESOLVED)
| Issue | 状态 | 修改内容 |
|-------|------|----------|
| R1-W2 CKA/RSA 矛盾 | ✅ RESOLVED | Method 新增 "Why RSA over CKA" 段，全票认可 |
| R3-N2 Em-dash AI 痕迹 | ✅ RESOLVED | 正文 prose 零残留解释性 em-dash |
| R3-W4 Related Work 过短 | ✅ RESOLVED | 3→5 段，21→33 引用，覆盖 4 个新类别 |

### 部分解决 (PARTIALLY_RESOLVED)
| Issue | 状态 | 残留问题 |
|-------|------|----------|
| R1-N1 Baseline confound | ⚠️ | 充分 acknowledge，但无新数据；标题/Abstract 仍 causal |
| R1-N4 Speculative implications | ⚠️ | Discussion caveat 良好，但 Abstract L8 仍为 "should"/"primary lever" 无 hedge |
| R1-N2/R2-N4 单模型泛化性 | ⚠️ | Abstract 限定了 "(OpenVLA-7B)"，但 Title 仍复数 |
| R2-N1 Novelty positioning | ⚠️ | "First" 删除，但 Neo et al. 仍未引用 |
| R1-N3 RSA selection bias | ⚠️ | 叙事改善（"where vs how high"），Table 结构未调整 |
| R2-W1 Related Work 覆盖 | ⚠️ | 33 引用达标，但仍缺 Neo et al. + Raghu et al. 2021 |
| R3-N1 Limitations 格式 | ⚠️ | 内容充分，格式仍为 \paragraph{}（需改 \subsection） |

### 未解决 (STILL_OPEN)
| Issue | 状态 | 说明 |
|-------|------|------|
| R1-W1 "Instruction-blind" overclaim | ❌ | 无任何修改（标题、措辞、实验均未动） |
| R3-W5 Code/data 声明 | ❌ | 未添加 |
| R2-N2 无方法创新 | ❌ | 无新方法/验证实验（R1+R3 认为可通过 insight novelty 弥补）|

---

## Strengths（Round 2 新增/强化）

1. **Confound 的透明度显著提升**：在实验章节正文（非仅 Limitations）即 acknowledge baseline 的局限性，让读者在遇到数据时就能正确理解 scope
2. **"Why RSA over CKA" 方法论辩护**：不是 post-hoc cherry-picking，而是基于 metric 数学性质的 principled argument（scale-invariance for cross-dimensional comparison）
3. **Related Work positioning 质量高**：Grant 2026 的三点显式差异化（token-level vs feature-level；32-layer profile；factorial control）是真正的 positioning 而非 survey
4. **写作修订到位**：em-dash 清除、section 标题从 "learns" → "establishes"、contribution list 重定位

---

## Weaknesses（Round 2 残留）

### Critical（影响接收决定）

**W-Critical-1: Abstract/Conclusion 与 Limitations 的语气不一致**
- Abstract L8: "VLA architectures should optimize routing; vision encoder quality is the primary design lever" — 未加任何 hedge
- Conclusion L8: "These results suggest that VLA architectures should optimize routing..." — 有 "suggest" 但 "should" 仍在
- Discussion Limitations: "they do not address whether architectural interventions... would preserve action quality"
- **内部矛盾**：开头做强处方 → 结尾否认验证能力
- **全票共识需修改**

**W-Critical-2: 无 Llama-2 base 实验数据（核心 confound 未消除）**
- 论文承认 "currently conducting" 但未在本版呈现数据
- Finding 2 "VLA training establishes deliberate instruction routing" 的因果归因仍不完全成立
- 如果 Llama-2 base 也展现 instruction-dominant attention → 核心叙事需根本重写
- **R1 核心 concern，R2 AGREE**

**W-Critical-3: Neo et al. (ICLR 2025) 未引用**
- VLM token-level layer-wise 分析的直接先行工作（probing + attention + position ablation on LLaVA）
- Introduction L10 "No prior work has provided a systematic token-level decomposition" 在 VLM 文献存在的情况下不完全成立
- **R2 核心 concern，R1 同意应引用但认为不影响 internal validity**

### Warning（影响评分）

**W-Warning-1: Title 仍为复数 "Vision-Language-Action Models"**
- 暗示一般性结论，与单模型证据不匹配
- **全票共识**

**W-Warning-2: "Instruction-blind" claim 完全未修改**
- Section 4.1 段落标题仍为 "Image tokens are instruction-blind"
- 无 MLP probe instruction classification 实验
- 无措辞限定
- **R1 标为 STILL_OPEN**

**W-Warning-3: Limitations 格式仍为 \paragraph{}**
- CoRL 2026 CFP: "include a Limitations section"
- 一行改动 (\paragraph → \subsection) 即可修复
- **R3 标注**

---

## Reviewer Consensus [Round 2]

所有 Reviewer 达成共识：
1. Abstract L8 必须加 hedge（"suggest"/"may benefit from"/"emerges as a candidate"）
2. Neo et al. 应被引用并 differentiate
3. CKA/RSA 问题已 RESOLVED
4. 修订展示了作者的诚实态度和对问题的理解
5. 论文在写作/呈现维度已达 accept 标准（R3 确认）
6. 核心瓶颈是科学层面：无 Llama-2 base 数据 + assertive claims 超出证据

---

## Reviewer Divergence [Round 2]

| 分歧点 | 立场 | 分析 |
|--------|------|------|
| 整体评分 | R1: 5, R2: 5, R3: 7 | 由评审维度差异解释，非实质矛盾 |
| 无方法创新是否致命 | R2: concern / R1+R3: 可接受 | 多数认为 insight novelty 可弥补 |
| Neo et al. 影响程度 | R2: critical / R1: positioning issue only | R1 认为不影响 internal validity |

---

## Overall Assessment

**Score: Weak Reject → Borderline (5/10)**
**Confidence: High (4/5)**

| Reviewer | Round 1 | Round 2 | 变化 |
|----------|---------|---------|------|
| R1 | 5/10 | 5/10 | 维持 |
| R2 | 4/10 | 5/10 | +1 |
| R3 | 6/10 | 7/10 | +1 |
| **Consensus** | **4.5/10** | **5.3/10** | **+0.8** |

**与 Round 1 的差异**：
- 论文在 presentation readiness 上从 "below standard" 提升至 "at standard"
- 科学问题的 transparency 提升（confound acknowledge、metric justification）
- 但核心科学 gap（无对照数据、无因果验证）未通过新实验消除

---

## 具体可操作修改建议（按优先级）

### P0（可能改变 acceptance decision）
1. **Llama-2 base checkpoint 实验数据**（如能在 deadline 前完成）
2. **Abstract L8 hedge**: "should optimize" → "may benefit from optimizing"; "is the primary design lever" → "emerges as a candidate primary design lever in our analysis"

### P1（全票共识的必要修改）
3. **Neo et al. 引用** + Introduction L10 限定为 "systematic multi-metric decomposition of a VLA with factorial controls"
4. **Limitations 格式**: \paragraph{Limitations.} → \subsection{Limitations}
5. **Title 限定**: 改为 "...of a Vision-Language-Action Model" (单数) 或加副标题 "A Case Study of OpenVLA"
6. **Section 4.2 标题**: "Training Establishes..." → "Trained VLA Exhibits..."

### P2（改善评分但非 blocking）
7. §4.1 标题 "instruction-blind" → "instruction-invariant under linear probing"
8. Table 3 same-layer comparison 调整为首行
9. Table 1 caption "(L0--L8 shown)" → "(selected layers shown)"
10. Conclusion 加 reproducibility statement
11. Abstract "LOOCV-verified" → "cross-validated"

---

## 给 Research Director 的判断

**当前状态**：论文处于 borderline (5/10)。写作已达标，科学方法论有一个不可通过文字修改完全解决的 gap（Llama-2 base 对照）。

**升至 Accept (6/10) 的路径**：
- **路径 A（最优）**：P0.1（Llama-2 base 数据）+ P0.2（Abstract hedge）+ P1 全部 → 预计 R1 升至 6，R2 升至 6，整体 6.3/10
- **路径 B（纯文字修改）**：P0.2 + P1 全部 + P2 全部 → 预计 R2 升至 6，R1 仍为 5-5.5，整体 5.8/10（仍在 borderline）
- **路径 C（最小修改）**：仅做 P0.2 + P1.3-4 → 预计变化不大

**建议**：如果 Llama-2 base 实验能在 deadline (05-29) 前获得至少 attention analysis + cross-instruction probe 结果，论文有实质性机会突破 acceptance threshold。否则，纯文字修改只能将论文从 weak reject 推至 borderline，最终 decision 将取决于 AC 对 "well-executed analysis paper with acknowledged confound" 的容忍度。