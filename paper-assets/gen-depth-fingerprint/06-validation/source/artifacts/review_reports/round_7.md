---
round: 7
overall_score: 3.0 - Findings
timestamp: 2026-05-17T12:50:27.970849+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 8 审稿报告（修订评估）

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**目标 venue**: EMNLP 2026 ARR (Long Paper)
**审稿轮次**: Round 8（基于 Round 7 修订的 continuation review）
**Reviewer**: R1 (方法/实验严谨性), R2 (新颖性/完整性)
**交叉分享**: 完成，两轮（初审 + 交叉回应），已收敛

---

## Summary

论文提出 ordinal depth estimation 任务，用 7 个统计特征（5 个 NLL + TTR + hapax ratio）+ XGBoost 分类器区分 gen-0/gen-1/gen-2+ 文本。核心发现是 differential depth response (DDR)：中心趋势特征随深度单调漂移，形状特征近似稳定。8 个 base models（5 families, 0.6B-8.2B）上验证。Round 8 评估针对 Round 7 提出的 12 个问题的修订情况。

---

## Round 7 Issue 修订状态

### 已解决（7/12）— 两位 Reviewer 一致确认

| Issue | 修订内容 |
|-------|---------|
| R1-W5 (downstream TOST) | TOST equivalence test 已添加（±2% margin, p=1.1e-4）；Contribution 3 移为散文句 |
| R7-W2 (DDR guarantee) | 改为 "tendency of standard decoding rather than an architectural guarantee" |
| R7-W3 (efficiency) | Table 4 新增 ms/text 列（9.7 vs 22.8ms）+ memory（905MB vs 2868MB） |
| R7-W5 (instruct framing) | Introduction 转向 characterization/understanding；Limitations 增加定量证据 |
| R7-W6 (gen-1/gen-2+ discussion) | Discussion 新增专门段落：86% FN, depth-2 error 48% vs depth-4 20%, Mistral 45% vs Pythia 18% |
| R7-M3 (NLL + topic drift) | NLL 展开；topic drift OLS 回归规格写明 |
| R7-M4 (missing refs) | ghostbuster, radar, gutierrez_ordinal_survey 均已添加 |

### 部分解决（3/12）

| Issue | 修订内容 | 残留问题 |
|-------|---------|---------|
| R7-W1 (gen-0 overlap) | Results 正确声明 binary 为 primary metric + gen-0 overlap 说明 | **Abstract 仅报告 3-class F1（0.809, 0.762），未报告 binary F1，与 Table 1 primary metric 声明矛盾** |
| R7-M1 ("strong"→"substantial") | results.tex L61 已修改 ✓ | method.tex L62 和 Figure 1 caption 仍写 "strong"（3 处中仅 1 处修改） |
| R7-M2 (bib issues) | 旧 orphans 已删除 ✓ | self_consuming_mad/qwen3/llama3 author 字段未修正（minor） |

### 未解决（1/12）— BLOCKING

| Issue | 状态 |
|-------|------|
| **R1-W1 (method.tex vs Table 4 超参矛盾)** | method.tex L77 仍写 "All other methods use n_estimators=100, max_depth=3"，Table 4 caption 已更新为 "all methods use 200/6"。**同一论文对同一实验的超参描述直接矛盾，影响可复现性。两位 Reviewer 一致认定为 blocking issue。** |

### 持续分歧（1/12）

| Issue | 状态 |
|-------|------|
| R7-W4 (method novelty) | R1 认为 task formulation + DDR 足够 Findings-borderline Conference；R2 认为方法层面无创新限制上限。双方理解对方立场，同意至少达 Findings 水平。 |

---

## Round 8 新发现（2 个）

### R8-N1: entropy_std 分组不一致（info）

method.tex L62 将 entropy_std 归入 "moderate drift" 组（|ρ|=0.17-0.41），但 Figure 1 caption 将其归入 "shape features (entropy std, tail decay) remain near-stationary"。分组矛盾。entropy_std（|ρ|=0.17）是边界案例，论文需统一分类并在 Discussion 中承认这一灰色地带。两位 Reviewer 一致确认。

### R8-N2: Abstract vs primary metric 声明不一致（warning）

Table 1 caption 声明 "Binary F1 is the primary metric"，但 Abstract 仅报告 3-class F1（0.809, 0.762），未提及 binary F1。这直接源于 R7-W1 的修复不完整——Results 正确提升了 binary 地位但 Abstract 未同步更新。两位 Reviewer 一致要求 Abstract 补充 binary F1。

---

## Strengths（修订后改善的方面）

1. **实验公正性显著提升**: Table 4 统一超参（200/6 for all）+ efficiency 定量对比（ms/text, memory）。论文不再 claim performance superiority，而是正确定位为 efficiency-interpretability trade-off。
2. **downstream 实验严谨化**: TOST equivalence test 提供了负结论的统计支撑，Contribution 3 降级为 prose 符合其实际贡献。
3. **DDR 叙事更审慎**: "tendency" 取代 "guarantee"，sampling ablation 结果与理论解释一致。
4. **gen-1/gen-2+ 讨论充实**: Discussion 新增段落包含定量错误分析、机制解释和 generator-specific patterns。
5. **self-positioning 诚实**: 承认 4-det+surface 略优，以 efficiency 和 single-reference simplicity 定位自身价值。

## Weaknesses（修订后仍存在的问题）

1. **[BLOCKING] method.tex vs Table 4 超参文本矛盾**: 同一论文两处对 baseline 超参的描述不一致。这是一个简单的文本修复，但未修复状态下严重损害可信度。
2. **Abstract 与 primary metric 声明脱节**: Table 1 声明 binary 为 primary，Abstract 仅报告 3-class。在 gen-0 seed sharing 已被明确指出的情况下，Abstract 仍以可能 inflated 的 3-class F1 为 headline，对读者形成误导。
3. **方法新颖性有限（持续分歧）**: 7 个已知特征 + XGBoost，无算法创新。DDR 是经验观察而非理论贡献。Base-model-only + ≤8.2B 限制影响力。
4. **文本一致性不足**: "strong"/"substantial" 不统一（3 处仅改 1 处），entropy_std 分组矛盾，bib author 字段未修正。这些单独是 minor，但累计反映 proofreading 不充分。

## Questions for Authors

1. method.tex L77 描述的 100/3 和 Table 4 caption 的 200/6，哪个是实验实际使用的超参？请统一。
2. 如果 binary F1 是 primary metric（Table 1 caption），为何 Abstract 不报告 binary F1？
3. entropy_std（|ρ|=0.17）应归入 "moderate drift" 还是 "near-stationary"？当前 method.tex 和 Figure 1 caption 说法矛盾。

## Missing References

Round 7 遗漏的引用（Ghostbuster, RADAR, Gutierrez ordinal survey）均已添加。当前无新的 missing reference 问题。

---

## Overall Assessment

### 评分

| Reviewer | Score | 理由 |
|----------|-------|------|
| R1 | **3.5/5** (Borderline Conference) | DDR characterization + task formulation 有独立价值；实验系统全面；修订回应充分。method.tex 矛盾修复后可达 Findings-Conference 边界。 |
| R2 | **3.0/5** (Findings) | 方法新颖性不足是根本限制；base-model-only + ≤8.2B 范围限制影响力。条件性上调至 3.5 可能——若修复全部文本一致性问题。 |

### Director 综合评分: **3.0/5 (Findings)**

**理由**:
- 论文在 Round 7→8 的修订中解决了大部分实质性问题（7/12 fully resolved），包括两个前 critical issue（baseline 公正性的实验部分、downstream 统计严谨性）。修订质量整体良好。
- 残留的 blocking issue（method.tex vs Table 4 矛盾）是简单文本修复，不影响实验本身的有效性。
- 方法新颖性（R7-W4）是论文的结构性限制，无法通过修订解决：全部 7 个特征为已知指标，分类器为标准 XGBoost，DDR 是经验观察。这将论文上限锁定在 Findings 水平。
- 论文的真正价值在于：(a) 定义了一个之前未被形式化的任务（ordinal depth estimation），(b) 提供了系统性的 empirical characterization（8 generators, 5 families, 12 appendices），(c) DDR finding 为理解 recursive generation 提供了有意义的框架。这些在 Findings venue 中是合理的贡献。
- 文本一致性问题（"strong"/"substantial"、entropy_std 分组、Abstract vs primary metric）累计反映 proofreading 不充分，降低整体印象但不影响技术判断。

### ARR 维度评分

| 维度 | 评分 | 说明 |
|------|------|------|
| Soundness | 3.5 | 实验方法论严谨（统一超参、TOST、LOGO/LOFO），但 method.tex 文本矛盾和 gen-0 overlap 处理不完美 |
| Excitement | 2.5 | 新任务定义有价值，但方法无创新；DDR 是经验发现非理论贡献；base-model-only 限制应用范围 |
| Reproducibility | 3.5 | 超参、数据规模、统计检验均报告；method.tex 矛盾修复后可复现；代码承诺发布 |
| Confidence | 4.0 | 两位 Reviewer 充分审读论文和附录，交叉分享达成强共识 |

### 必须修复项（投稿前）

1. **method.tex L77**: 统一超参描述为 200/6（与 Table 4 caption 一致）
2. **Abstract**: 补充 binary F1（与 Table 1 primary metric 声明一致）
3. **"strong" → "substantial"**: method.tex L62 和 Figure 1 caption 中替换
4. **entropy_std 分组**: method.tex 和 Figure 1 caption 统一分类

### 建议修复项（非 blocking）

5. bib author 字段：self_consuming_mad/qwen3/llama3 与最终发表版本同步
6. Rebuttal 准备：针对 R7-W4（方法新颖性），准备 DDR vs model collapse 方向差异、task formulation 作为独立贡献的论证

### 推荐

**Findings 接收**（修复上述 4 个必须项后）。论文提供了有价值的 empirical contribution，但方法新颖性不足以支撑 main conference。如果 R2 在所有文本修复后上调至 3.5，论文可进入 Borderline Conference 讨论；但基于当前证据，Findings 是更稳健的定位。