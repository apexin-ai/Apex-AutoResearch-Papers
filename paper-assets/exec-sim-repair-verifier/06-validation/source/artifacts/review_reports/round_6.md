---
round: 6
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-22T14:08:59.929273+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 8 (Fresh Review)

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study"
**Venue**: EMNLP 2026 via ACL Rolling Review
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: Novelty + Completeness + Writing Quality）
**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 1 轮收敛

---

## Summary

本文系统比较了三种 execution-free 代码验证 formulation（CLS 分类、CWM 输出生成、TRAJ 轨迹评分），在 matched conditions（≤8B LoRA、相同数据/compute/模型家族）下的效果差异。核心发现：(1) 函数级三种 formulation 统计等价；(2) 仓库级 CLS 大幅优于 CWM（18–26pp），主因 format collapse；(3) 错误互补性暗示集成潜力。统计方法论全面（TOST、clustered bootstrap、mixed-effects LPM、Holm-Bonferroni），附丰富消融和 threats-to-validity 分析。

---

## Strengths（全票共识）

**S1. Matched experimental design 填补重要空白。** 固定模型容量、训练数据、compute 仅改变 formulation，在该领域首次实现真正的 matched comparison。[R1-S1, R2-S2, 全票 AGREE]

**S2. 统计方法论远超同类 empirical study。** 四层工具（clustered bootstrap with ICC=0.191/DEFF=3.97 → TOST with SESOI ±2pp → mixed-effects LPM → Holm-Bonferroni k=4）形成完整证据链。[R1-S2, R2-S1, 全票 AGREE]

**S3. Failure mode taxonomy 有实用价值。** Table 4（format collapse / decision collapse / aggregation penalty）为每种 formulation 的适用边界提供可操作的诊断标准。[R1-S3, R2-S3, 全票 AGREE]

**S4. CWM 退化诊断链有说服力。** 四种干预全部失败 + accidental training artifact（CWM 在 CLS 格式数据上 86.05%/0% unparseable）+ convergence analysis，排除多种替代解释。[R1-S4, R2 implicit, 全票 AGREE]

**S5. Threats to Validity 量化分析罕见。** 五个 confound 逐一量化，worst-case compounding ~11.5pp，显示 18–26pp gap 仍有 ≥7.5pp residual margin。[R1-S5, R2-S4, 全票 AGREE]

**S6. 写作干净、hedging 恰当。** 几乎无 AI 痕迹，术语一致，大量使用 "under our protocol"、"conditional on ≤8B LoRA regime" 等限定语。[R2-S6, R1 implicit, 全票 AGREE]

---

## Weaknesses

### Must-Fix（共识 Critical）

**C1. TOST p=0.007 被错误归属于 CLS–CWM 比较** [R1-N1, R2 独立验证 AGREE]

- Abstract 声称 "CLS and CWM are statistically equivalent across both families (TOST, 5 seeds)"
- Conclusion 给出 "CLS and CWM are statistically equivalent (TOST p=0.007, 5 seeds)"
- 但 §3.4 标题 "Per-Test vs. Trajectory-Level Equivalence"，执行 TOST 对象是 **CLS vs TRAJ**（p=0.007）
- Table 15 Holm-Bonferroni Rank 2 标注 "Func: CLS vs TRAJ (TOST ±2pp)"
- **全文没有 CLS–CWM 的正式 TOST 检验**
- R2 补充：Abstract 说 "5 seeds" 但 CLS–CWM 在 DeepSeek 仅 2 seeds，Qwen3 虽有 5 seeds 但同样未做 TOST
- **影响**：论文第一条 contribution 的核心统计证据存在 misattribution。这是事实性错误。
- **修复路径**：(1) 补做 CLS–CWM TOST（Table 1 gap 仅 0.02–1.24pp，预期通过 ±2pp margin）；(2) 修正 Abstract/Conclusion 中 p 值归属；(3) Holm-Bonferroni 表加入 CLS–CWM 条目并更新 k

**C2. Abstract 对 repo-level CWM 结论缺少 regime qualifier** [R1-N2 Critical, R2 Strong Warning, Director 裁定 Critical]

- CWM 在 repo-level 面临多重系统性劣势：(a) NaN val loss 被迫用 final epoch checkpoint（eval loss 达最优值 1.8×）；(b) max_new_tokens=512 限制有效上下文至 ~1,536 tokens（vs CLS 5,120–8,192）；(c) 原始 CWM（Meta, 32B + execution trace mid-training）与本文 ≤8B LoRA 条件根本不同
- Abstract 说 "the CLS–CWM gap widens to 18–26pp" 但未像 Conclusion 那样加上 "under ≤8B LoRA fine-tuning"
- **分歧**：R1 认为 critical（Abstract 是独立阅读入口），R2 认为 strong warning（body text 已有 hedging，只需 ~5 词修改）
- **Director 裁定**：保持 critical——修复成本极低但影响大。额外建议：§3.5 讨论 early-stopped CWM 对 gap 的影响（DeepSeek epoch-1 75.45% vs epoch-3 57.31%，gap 从 ~26pp 缩至 ~9pp）

---

### Should-Fix（共识或多数同意）

**W1. n=48 variant 样本量导致 repo-level 比较严重欠 power** [R1-W1, R2 AGREE]

MDE ≈ 25pp，CLS–TRAJ repo-level gap（<10pp）无法被统计检验。Conclusion 推荐 CLS "for both accuracy and throughput" 中 accuracy 部分证据不足。建议明确推荐主要基于 throughput（217×）和 per-test 诊断能力，而非 accuracy 优势。

**W2. Oracle 互补性估计为单种子、无置信区间** [R1-W2, R2-W4, 全票 AGREE]

Repo-level oracle 95.83% 在 n=48 上 binomial 95% CI 约 [85.7%, 99.5%]，非常宽。Function-level oracle 90.63% 同为单种子。论文将此作为 "the strongest practical argument for exploring the formulation design space"（§1），但不确定性量化缺失。至少应提供 bootstrap/binomial CI 并在 Abstract 标注 "single-seed estimate"。Function-level 有 5 种子数据，多种子 oracle 可直接计算。

**W3. CWM checkpoint 消融不对称** [R1-W4, R2 AGREE]

CLS 有 checkpoint 消融（epoch 1/val-selected/final，range <1pp）。CWM 在 DeepSeek 上 epoch-1 vs epoch-3 差 +18.14pp（75.45% vs 57.31%），但 Qwen3（primary model family）没做同样消融。如果 Qwen3 CWM early-stopped 也达 ~75%，CLS–CWM gap 从 ~18pp 缩至 ~10pp，effect size 定性解读从 "crushing" 变为 "moderate"。建议补一个 Qwen3 CWM epoch-1 评估。

**W4. z=−23.7 interaction 仅基于 DeepSeek-Coder，Abstract 未标注** [R2-W3, R1 AGREE]

§3.5 明确说明仅用 DeepSeek-Coder（"the only family with both function- and repo-level CWM evaluations under matched conditions"），但 Abstract/Introduction 未标注。建议 Abstract 改为 "a significant interaction (z=−23.7, DeepSeek-Coder)"。

**W5. 遗漏 GenRM 等关键相关工作** [R2-W5, R1 AGREE on citation]

GenRM (Zhang et al., ICLR 2025) 直接比较 discriminative vs. generative formulation for verification，发现 generative 在数学推理上显著优于 discriminative（GSM8K 73%→93.4%）。与本文 repo-level 代码验证的相反发现形成重要对比。R1 补充：这个 domain difference 本身有信息量，引用并讨论会增强论文 positioning。另遗漏 RepoExec (Ding et al., 2024) 和 Chen et al. (2024) "Benchmarking LLM-based Verifiers"。

---

### Should-Fix（有分歧，Director 裁定降级）

**W6. CWM baseline 偏弱削弱核心结论** [R2-W1 Must-Fix, R1 REBUT → Director 裁定 Should-Fix]

- **R2**：≤8B LoRA CWM vs 原始 32B+mid-training 差距根本性，18–26pp gap 可能主要归因于 pretraining 不足
- **R1 反驳**：(1) parseable CWM 准确率仅 38–43%（vs CLS 85%+），问题不仅是格式；(2) accidental artifact 86.05% 证明同一架构在不需 trace generation 时完全胜任；(3) 四项 intervention 全部失败（rank 增加、majority voting、relaxed matching、model scaling）；(4) 要求 32B 实验超出合理修改范围
- **Director 裁定**：降为 Should-Fix。R1 引用的 parseable accuracy 和 artifact 证据构成强有力的反事实论证。与 C2 合并处理：Abstract 加明确 regime 限定即可，无需补 32B 实验。

---

### Novelty 分歧（记录，不作为独立 Must-Fix）

**R2-W2: Novelty 不足以达 Conference 水平**

- **R2**：三个 finding 均未超越 practitioner 直觉——(1) 短输出 generation≈classification trivial；(2) 长输出 format collapse 广泛已知；(3) re-repair p=0.42 削弱 complementarity。没有新方法或 surprising insight。
- **R1 反驳**：(1) CWM function-level 生成完整执行输出非 1 token，与 CLS 等价不是 trivial（GenRM 在数学推理上发现相反结果恰恰说明需要实验验证）；(2) 从 "有时出错" 到 "53–74% unparseable + parseable 准确率比 CLS 低 40pp+" 的系统性量化是 empirical study 的价值；(3) negative re-repair result 区分了 structural complementarity 和 downstream utility，对后续研究有指导意义
- **Director 评估**：R2 的 novelty 关切对 main conference 有道理（excitement 2.5 反映了这一点），但 R1 的反驳在 Findings track 语境下成立。论文的价值在于方法论驱动的量化分析。不作为独立 Must-Fix，但影响 excitement 评分和 overall 定位。

---

### Minor

| ID | 问题 | 共识 |
|----|------|------|
| M1 | LPM 未报告 robust standard errors（R1-M1）| R2 AGREE |
| M2 | Prompt templates 未在论文中展示，仅指向 code repo（R1-M2）| R2 AGREE |
| M3 | Figure 2 y 轴截断 ~55%（R1-M3）| R2 部分 REBUT（caption 已暗示，加一句 "y-axis begins at 55%" 即可）|
| M4 | Scaling 分析 2 种子 power 极低，"CWM flat scaling" 应标注 exploratory（R1-M4）| R2 AGREE |
| M5 | Xia et al. 年份不一致（R1-M5）| R2 需核实 |
| M6 | §3.5 过度压缩，信息密度过高（R2-W7）| R1 AGREE（但反对压缩 §3.3）|
| M7 | TOST 混合精度 bfloat16/NF4 交互（R1-W3）| R2 REBUT 降为 Minor（direction consistent），Director 同意降级 |
| M8 | Figure 2 信息冗余（R2-W8）| R1 REBUT（直接支撑 core claim）|
| M9 | Limitations 过短（R2-W9）| R1 REBUT（§3.7 已覆盖，符合 EMNLP norm）|
| M10 | TRAJ 训练数据量差异 175×（R2-W6）| R1 REBUT 降为 Minor（formulation 固有 + downsample ablation 已做）|

---

## Reviewer Consensus

1. **TOST 归属错误是 critical 事实性错误**——两人独立验证，全票同意
2. **Abstract 需要更强的 regime qualifier**——两人均认为 repo-level 结论表述不够限定
3. **Oracle 结果需要 CI**——两人均同意至少加 binomial/bootstrap CI
4. **CWM checkpoint 消融不对称需补充**——两人均同意 Qwen3 CWM epoch-1 评估有价值
5. **GenRM 是重要遗漏**——两人均同意应在 Related Work 中引用并讨论
6. **统计方法论和 matched design 是最突出优势**——全票认可
7. **Findings track (3.0) 适合本文定位**——两人均给 3.0

## Reviewer Divergence

1. **Novelty 是否足够**：R2 认为 Must-Fix（三个 finding 不超越直觉），R1 认为 empirical study 标准下 novelty 足够（量化分析 ≠ trivial）
2. **CWM baseline 偏弱的严重性**：R2 认为 Must-Fix（可能归因于 scale/pretraining），R1 引用 parseable accuracy + artifact 证据反驳为 Should-Fix
3. **N2 severity**：R1 认为 critical，R2 认为 strong warning（body text 已有 hedging）
4. **混合精度对 TOST 的影响**：R1 认为 Should-Fix，R2 认为 Minor（direction consistent + Appendix O）
5. **TRAJ 训练数据不公平**：R2 认为 Should-Fix，R1 认为 Minor（formulation 固有 + 已有 ablation）

---

## Questions to Authors

**Q1** [共识 — 最高优先级]: TOST p=0.007 究竟是 CLS–CWM 还是 CLS–TRAJ 的结果？CLS–CWM 是否有单独的 TOST 检验？

**Q2** [共识]: Qwen3-8B CWM epoch-1 或 step ~400 checkpoint 的 repo-level 评估结果？

**Q3** [共识]: Oracle 互补性能否扩展到多种子（至少 function-level 有 5 种子数据）？

**Q4** [R2]: GenRM (ICLR 2025) 发现 generative verifier 在数学推理上优于 discriminative。如何解释代码验证领域的相反趋势？

**Q5** [R2]: CWM 输出改为 short structured format（如 JSON）后 format collapse 是否会显著减少？

**Q6** [R2]: Re-repair pilot p=0.42 是否意味着 CLS 的 diagnostic advantage 仅是 theoretical？

**Q7** [R1]: Mixed-effects LPM 是否检验过 logistic regression 结果的一致性？

---

## Missing References

| 论文 | 推荐者 | 共识 | 优先级 |
|------|--------|------|--------|
| Zhang et al. (2024/2025) "Generative Verifiers" (GenRM), ICLR 2025 | R2, R1 同意 | **Must-cite** | 高 |
| Ding et al. (2024) "RepoExec" | R1, R2 同意 | Should-cite | 中 |
| Chen et al. (2024) "Benchmarking LLM-based Verifiers" | R1, R2 同意 | Should-cite | 中 |
| CVeDRL (2026, arXiv 2601.22803) | R2 | 待核实 | 低 |
| GenPRM (2025, arXiv 2504.00891) | R2 | 待核实 | 低 |

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求。

---

## Visual Layout Check（非评分项）

**状态**：done（2026-05-22 13:40–13:43 UTC）| 0 critical, 1 warning, 4 info

| Severity | 位置 | 发现 |
|----------|------|------|
| Warning | Page 22 | 附录最后一页仅 ~10% 填充（17 行），~90% 空白。建议合并 Appendix O 或调整附录顺序 |
| Info | Pages 1-2 | 连续 2 页纯文本无 display item（Abstract + Intro）。Figure 1 在 page 3。ACL 格式常见 |
| Info | Page 7 | Figure 2 axis/bar labels 偏小（约正文字号 65-70%），建议放大 |
| Info | Page 4 | Tables 1+2 紧密排布，密度高但可读 |
| Info | Pages 13-14 | 附录 Tables 5-9 集中 2 页，密度极高但无溢出 |

---

## Overall Assessment

### 官方维度打分（合成）

| 维度 | R1 | R2 | 合成 | 理由 |
|------|----|----|------|------|
| **Soundness** | 3.5 | 3.0 | **3.0** | 统计框架整体严谨，但 TOST 误归属（C1）是事实性错误，CWM 比较条件不对等（C2）削弱 formulation-level claims。修复 C1+C2 后可达 3.5+ |
| **Excitement** | ~3.0 | 2.5 | **2.5** | 研究问题填补实际空白，failure mode taxonomy 有洞察力，但核心发现的 surprise factor 有限（R2 novelty 关切部分成立），结论受限于 ≤8B regime |
| **Reproducibility** | 4.0 | 4.0 | **4.0** | 超参数完整（Table 11）、compute 明确（~370 GPU-hrs）、承诺 release all。扣分：prompt templates 未在论文中给出，部分 repo-level 结果 seed 数不足 |

### Overall: **3.0 — Findings**

### 判断依据

1. **核心硬伤（C1）修复成本低但影响大**：TOST p 值 misattribution 构成事实性错误，直接影响论文第一条 contribution 的证据基础。预期补做 CLS–CWM TOST 可通过（gap 仅 0.02–1.24pp），但在修复前 soundness 有裂缝。

2. **CWM 比较公平性（C2 + W3 + W6）形成系统性关切**：checkpoint 不对称、context length 不对称、与原始 CWM 设定差距巨大——虽在 body text 中被讨论，但 Abstract 级别 framing 不够谨慎。R1 引用的 parseable accuracy 和 artifact 证据表明问题确实不仅是 scale，但 effect size 的定性解读仍受影响。

3. **Novelty 处于 Findings 合理区间**：matched experimental design + 统计方法论 + failure mode taxonomy 是有价值的 methodological contributions，但三个核心 finding 的 surprise factor 有限。对 main conference 来说 novelty 不够突出，但符合 Findings track 标准。

4. **修复后上限**：修复 C1 + C2 + W1-W5 后，论文可达 **3.5 (Borderline Conference)**。Failure mode taxonomy、interaction 分析（z=−23.7）和 oracle framework 是有价值贡献，但 novelty ceiling 使其难以达到 4.0。

---

## Detailed Comments（按论文结构）

### Abstract
- **[C1]** "CLS and CWM are statistically equivalent (TOST, 5 seeds)" → 需修正为 CLS–TRAJ，或补做 CLS–CWM TOST 后同时报告
- **[C2]** "the CLS–CWM gap widens to 18–26pp" → 加 "under our ≤8B LoRA protocol"
- **[W4]** "a significant interaction (z=−23.7)" → 加 "(DeepSeek-Coder)"
- **[W2]** Oracle 数字引用时标注 "single-seed estimate"

### §3.4 Per-Test vs. Trajectory-Level Equivalence
- **[C1]** 补做 CLS–CWM TOST 检验并报告结果
- **[M7]** 增加 bfloat16 vs NF4 子集的均值 gap 对比数据

### §3.5 Repository-Level Results
- **[C2]** 增加一段讨论 early-stopped CWM 的 gap 影响（epoch-1 75.45% → gap ~9pp）
- **[W3]** 补 Qwen3-8B CWM epoch-1 评估

### §3.6 Error Complementarity
- **[W2]** Oracle 结果加 bootstrap/binomial CI；function-level 做多种子 oracle

### §3.7 Threats to Validity
- **[W3]** 量化 CWM checkpoint selection confound 的 upper bound

### §4 Related Work
- **[W5]** 加入 GenRM (Zhang et al., ICLR 2025) 讨论 + domain difference 分析
- **[W5]** 引用 RepoExec、Chen et al.

### §5 Conclusion
- **[C1]** 修正 TOST p 值归属
- **[W1]** CLS 推荐明确基于 throughput + per-test 诊断，非 accuracy 优势

### Appendix
- **[M2]** 展示每种 formulation 完整 prompt 示例
- **[M1]** Appendix L 加 robust SEs 说明
- **[C1]** Holm-Bonferroni 表加入 CLS–CWM 条目，更新 k

### Table 15 (Holm-Bonferroni)
- **[C1]** 加入 CLS–CWM TOST 行，更新 k 值和 adjusted α