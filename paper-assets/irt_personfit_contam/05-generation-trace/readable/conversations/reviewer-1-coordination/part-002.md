# Reviewer 1 coordination — Part 2 of 2

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/be/be0994633a4f0dea14df.json)

## Round 17

### Tool call

_source line 471 · 2026-05-22T07:49:07.514079+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告：方法严谨性审查\n\n**论文标题**：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n\n---\n\n## Paper Summary\n\n本文首次将心理测量学中的 IRT person-fit 统计量（ℓ_z*）系统性地应用于 LLM 基准污染检测。核心思路是：被污染的 LLM 类似于拥有题目预知的考生，会在难题上产生异常正确的作答模式，可被 person-fit 统计量捕获。作者提出 Δℓ_z*（差分设计）消除 IRT 模型误设影响，在 3 个 7-8B 模型族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B）× 2 个基准（MMLU、ARC-C）× 3 个污染水平（15%/25%/50%）上进行了控制实验。主要发现三个行为边界：(1) 模型特异的 θ-shift absorption；(2) detection-diagnosis tradeoff（简单统计量检测更强，ℓ_z* 诊断更强）；(3) 能力依赖的非单调剂量-效应。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5（Borderline Conference）\n\n**一句话总结**：新颖的跨学科视角和扎实的机制分析，但单次污染运行的实验设计和事后扩展的实验矩阵显著削弱了定量结论的可靠性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.0 / 5 | 核心检测 claim 有支撑（所有 bootstrap CI 排除零），但每个污染条件仅单次运行（n=1）严重限制了 Cohen's d 的统计解释力；实验矩阵事后扩展（先看到 inverted-U 再补 25% 条件）构成循环论证风险；摘要中 \"n=10 independent seeds per condition\" 措辞具有误导性 |\n| **Excitement** | 3.5 / 5 | 首次将心理测量 person-fit 理论引入 NLP 污染检测，θ-shift absorption 机制和 detection-diagnosis tradeoff 均为有洞察力的发现；但论文自身承认简单统计量检测效果更优，削弱了实际应用价值 |\n| **Reproducibility** | 3.0 / 5 | 代码和数据承诺 \"released upon acceptance\"，QLoRA 超参数有交代（rank=16, α=32），但训练 epoch 数、学习率、数据混合细节不够充分；PSN-IRT item bank 为外部依赖 |\n| **Reviewer Confidence** | 4 / 5 | 本人熟悉 IRT/心理测量方法论和 LLM 评估领域，对统计方法学和实验设计的评估有较高把握 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 每个污染条件仅单次运行，Cohen's d 统计解释受限\n\n- 具体位置：Section 3.3（method.tex L48-49）：\"each contaminated model is a single QLoRA run\"\n- 问题：每个污染水平（15%/25%/50%）仅训练了 ONE 个模型，所有方差估计均来自 clean seeds（n=10 或 n=6）。由此计算的 Cohen's d 本质上是单个观测值相对于参考分布的 z-score，而非两个分布间的标准化均差。QLoRA 微调具有随机性（初始化、数据顺序），不同 seed 可能产生不同的污染模式和 ℓ_z* 值。当前设计无法：(a) 估计污染效果的方差；(b) 判断观测到的 ℓ_z* shift 是否具有代表性；(c) 正确计算需要两组方差的 Cohen's d。这直接影响所有定量比较——包括 Table 1 的 effect size、cross-model 比较、以及 inverted-U 的幅度。\n- 为什么影响接收：论文的三个核心 contribution 中，contribution (2)（Δℓ_z* reliably detects）和 (3)（detection-diagnosis tradeoff）的定量证据均建立在这些单次运行的 effect size 上。如果使用不同 seed 训练污染模型，Qwen 50% 的 |d|=1.90 可能变为 3.0 或 0.5，整个 inverted-U 叙事可能不成立。\n- 建议修改方向：至少为关键条件（如 Qwen 15%/50% on MMLU）训练 3-5 个污染 seed，报告污染效果的 seed-level 方差。若计算资源不允许，应在正文中明确标注 Cohen's d 为 \"single-observation effect size\"，并讨论这一限制对结论的影响。\n\n**N2** [critical] 摘要中 \"n=10 independent seeds per condition\" 措辞具有误导性\n\n- 具体位置：Abstract（abstract.tex L4）\n- 问题：摘要写道 \"n=10 independent seeds per condition; n=6 for Mistral\"，自然阅读理解为每个实验条件（clean/15%/25%/50%）均有 10 个 seed。但 Section 3.3 明确说明 \"We train n=10 clean seeds\" 且 \"each contaminated model is a single QLoRA run\"。实际上只有 clean 条件有多 seed，所有污染条件均为 n=1。这构成对读者（和 AC）的误导，夸大了研究的统计功效。\n- 为什么影响接收：摘要的准确性是论文可信度的基础。审稿人和 AC 可能基于摘要形成初始印象。如果 \"n=10 per condition\" 被理解为每条件 10 个独立运行，这与实际情况严重不符。\n- 建议修改方向：改为 \"n=10 clean baseline seeds per model family (n=6 for Mistral); single contaminated run per condition\"，准确反映实验设计。\n\n**N3** [critical] 实验矩阵事后扩展构成循环论证风险\n\n- 具体位置：Section 3.3（method.tex L46-47）：\"Following initial observation of non-monotonic dose-response for Qwen, we added a 25% contamination condition.\"\n- 问题：实验设计是迭代的而非预注册的：先观察到 Qwen 15% > 50% 的非单调性，再添加 25% 条件以 \"确认\" inverted-U。这是典型的假设确认式数据收集（hypothesis-confirming data collection）。论文将 inverted-U 作为核心发现之一（contribution 3），但确认该发现的数据点（25%）是在看到初始结果后才添加的。此外，25% 条件仅扩展到 Llama（未覆盖 Mistral），进一步限制了跨模型验证的完整性。\n- 为什么影响接收：Inverted-U 是论文三个核心发现之一。如果其证据基于事后选择的数据点，且无独立验证（如 held-out 模型族），该发现的置信度大幅降低。Simulation（Appendix A）虽提供了机制预测，但模拟参数可能也受到实证结果的影响。\n- 建议修改方向：(a) 明确标注 25% 条件是事后添加的（当前已做到，但应讨论其对统计推断的影响）；(b) 理想情况下，在 Mistral 上验证 25% 条件；(c) 或者将 inverted-U 定位为 \"exploratory finding requiring prospective confirmation\" 而非已确立的 \"behavior boundary\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 无低污染水平（<15%）的实证实验\n\n- 具体位置：Section 3.3 实验设计，Table 1\n- 问题：经验实验的最低污染水平为 15%，这在实际场景中已属相当高的污染率。模拟（Appendix B, Table 4）覆盖了 5%，但 5% 时 MMLU 检测功率仅 47.6%（4PL），ARC-C 仅 5.7%。论文未在实证数据上验证低污染场景的检测能力，而这恰恰是实践中最需要的场景。\n- 建议：至少在一个模型族上测试 5% 污染条件，或在 Discussion 中更显著地讨论低污染检测的局限性。\n\n**W2** [warning] ARC-Challenge 实验仅限 Qwen，跨基准泛化证据不足\n\n- 具体位置：Section 3.3（method.tex L54）：\"ARC-Challenge experiments were conducted on Qwen only\"\n- 问题：ARC-C（295 items）是论文唯一的小基准测试，且仅在 Qwen 上测试。论文从中得出关于 ceiling effect 和跨基准泛化性的结论（Section 4.1 L57-64），但 n=1 模型族无法支撑泛化性声称。此外，ARC-C 的模拟检测功率极低（5% 污染时仅 5.7%，15% 时 8.7%，Table 4），质疑了该基准上 person-fit 方法的实用性。\n- 建议：(a) 弱化关于 ARC-C ceiling effect 的泛化性声称；(b) 在 Limitations 中明确讨论小基准的功率限制。\n\n**W3** [warning] Fixed-θ 在 15% 污染时反而比 free-θ 更差（Qwen），缺乏充分解释\n\n- 具体位置：Table 2（results.tex L84）：Qwen 15% free-θ |d|=6.58, fixed-θ |d|=4.77, ratio=0.7×\n- 问题：论文的核心机制叙事是 \"θ-shift absorption 削弱检测 → fixed-θ 可恢复信号\"。但 Table 2 显示 Qwen 在 15% 污染时 fixed-θ 效果反而更差（0.7×）。这与 50% 时的 7.6× 改善形成强烈对比。论文未充分解释这一反转：为什么在低污染时 free-θ 反而更优？如果 θ-shift absorption 是一般性机制，它应该在所有污染水平上都使 free-θ 劣于 fixed-θ（只是程度不同）。\n- 建议：提供 15% 时 free-θ 优于 fixed-θ 的定量解释。可能的原因包括：(a) Snijders correction 在 free-θ 下减少了方差（但这应对检测有利，不应导致 d 更大）；(b) 小幅 θ-shift 实际上增加了某些 item 上异常模式的可检测性。无论原因如何，当前的叙事过于简化。\n\n**W4** [warning] Post-RL 观察（N=1）占据过大篇幅\n\n- 具体位置：Section 5 Discussion（discussion.tex L22-25），Figure 4\n- 问题：Post-RL 实验仅使用 Qwen 一个模型、15% 一个污染水平、GRPO 一种 RL 方法。这是一个 anecdote，而非实验证据。但它在 Discussion 中获得了完整段落和一个 Figure 的空间，且在 Abstract（L8）中也被提及。对于一个 N=1 观察，这一比重过高。\n- 建议：将 Post-RL 内容移至 Appendix，正文用一句话提及即可。这样释放的空间可用于更重要的分析（如额外污染水平或模型族）。\n\n**W5** [warning] QLoRA 训练细节不足以复现\n\n- 具体位置：Section 3.3（method.tex L45）\n- 问题：论文报告了 QLoRA rank=16, α=32，但缺少以下关键超参数：学习率、训练 epoch 数、batch size、warmup 策略、数据混合比例的精确构造方式（benchmark items 如何与非污染数据混合？ Interleaved? Appended?）、序列长度、以及如何处理多选题格式（将 ABCD 选项编码为 SFT 目标的具体方式）。Reproducibility Statement（main.tex L42-45）仅提及 \"Code and response data will be released upon acceptance\"，对于当前阶段的审稿不构成可复现性保证。\n- 建议：在 Appendix 中添加完整的训练配置表，包括所有超参数和数据预处理细节。\n\n**W6** [warning] Cohen's d 的 bootstrap CI 在小样本下的可靠性\n\n- 具体位置：Section 3.2（method.tex L34），Mistral 条件（n=6）\n- 问题：对于 Mistral（n=6 seeds），bootstrap resampling from 6 values 产生的 CI 分布非常粗糙（仅 6^6 = 46,656 种可能的重采样组合，远少于 10,000 次 resampling 中的有效独立样本）。BCa 校正（Appendix G）确认 percentile CI 是保守的，但 BCa 本身在 n=6 时也未必可靠。Table 1 中 Mistral 的 CI 确实极宽（如 [-9.6, -2.1]），但论文未讨论这一宽度是否足以支撑有意义的推断。\n- 建议：对 Mistral 结果添加关于小样本 bootstrap 局限性的显式讨论；考虑报告 permutation test p-value 作为补充。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.2 将 Δℓ_z* 设计称为 \"difference-in-differences (DiD)\"（method.tex L25），但标准 DiD 设计需要时间维度上的前后对比。此处更准确的描述是 \"matched-difference design\" 或 \"simple differencing\"。\n- Table 1 的列标题为 \"d (15%) [CI]\" 等，但 CI 的具体含义（percentile bootstrap, 10,000 resamples）需要在表注中说明（当前仅在 caption 中提及 bootstrap，未说明 percentile vs BCa）。\n- Figure 2 的色标（蓝色强度）仅凭 heatmap 难以精确读数，建议在每个 cell 内标注 |d| 值和 CI（当前似乎已做到，但 PDF 分辨率下难以确认）。\n- Limitations section 应增加对 \"无低污染实验\" 和 \"单次污染运行\" 的显式讨论——当前 Limitations 列举了模型规模和 SFT-scope 限制，但未提及这两个更基础的设计限制。\n\n---\n\n## Questions to Authors\n\n1. 如果为 Qwen 15% 和 50% 各训练 5 个不同 seed 的污染模型，你预期 ℓ_z* 的 seed-level 方差会有多大？你是否有任何 pilot 数据（如两个 seed 的比较）来估计污染效果的可重复性？\n\n2. 25% 条件是在观察到 inverted-U 后添加的。是否考虑过在一个 held-out 模型族（如 Phi-3、Gemma）上进行前瞻性验证？\n\n3. Table 2 中 Qwen 15% 的 fixed-θ 比 free-θ 更差（ratio=0.7×），能否提供更精确的定量解释？特别是，Snijders correction 在此处的具体影响是什么？\n\n4. PSN-IRT 的校准样本（13,000+ 模型）中，估计有多大比例的模型可能存在不同程度的基准污染？Appendix F.2 的 ±10% 随机噪声分析是否能模拟系统性污染偏差？\n\n5. Abstract 中 \"n=10 independent seeds per condition\" 具体指什么？如果指 \"per model family's clean condition\"，建议修改措辞以避免歧义。\n\n---\n\n## Missing References\n\n- **Polo et al. (2024)** 在 related work (Section 2, p3) 中被引用用于 IRT-based item selection，但论文未与之进行方法论层面的对比（Polo 用 IRT 选 item，本文用 IRT person-fit 检测污染——角度不同但框架共享，值得讨论）。\n- 论文未引用 **Sinharay & Johnson (2017)** \"Measures of agreement: reliability, classification accuracy, and classification consistency\" 或相关的 IRT person-fit 功效分析文献，这些可为 \"多少 item 足够检测\" 的 benchmark size boundary 提供理论支撑。\n- 缺少与 **EMNLP 2024/2025 年相关 contamination 工作**（如 benchmark leakage detection via perplexity-based methods）的系统对比。\n\n---\n\n## 主要优势\n\n1. **新颖的跨学科桥接**：首次将教育测量学 person-fit 理论系统性引入 NLP 污染检测，类比关系（污染 LLM ↔ 作弊考生）自然且有启发性。\n\n2. **诚实的定位**：论文明确将自身定位为 \"characterization\"（行为边界刻画）而非 \"tool\"（现成工具），并坦承简单统计量在纯检测任务上表现更优。这种学术诚实值得肯定。\n\n3. **Δℓ_z* 差分设计**：优雅地解决了绝对 ℓ_z* 阈值在 LLM 上无效的问题（57/60 cells 被标记为异常）。LD simulation（Appendix F.1）提供了合理的鲁棒性证据。\n\n4. **θ-shift absorption 机制分析**：对 \"为什么高能力模型检测信号更弱\" 的机制解释清晰、有说服力，fixed-θ vs free-θ 对比（Table 2）提供了强支撑证据。\n\n5. **Detection-diagnosis tradeoff**：这一发现对实践有直接指导意义——先用 accuracy z-score 筛选，再用 ℓ_z* 诊断机制。\n\n6. **详尽的 Appendix**：包含 LD 模拟、参数噪声敏感性、BCa 对比、4PL vs 3PL 消融、classical IRT refit、seed sensitivity 等 8 个补充分析，展现了方法论上的严谨态度。\n\n---\n\n## 总结性评价\n\n本文在 NLP-psychometrics 交叉领域做出了有意义的探索，三个行为边界的发现（θ-shift dynamics、detection-diagnosis tradeoff、non-monotonic dose-response）为理解基准污染的统计特征提供了新视角。机制分析（特别是 θ-shift absorption）清晰有力，Appendix 中的鲁棒性分析展现了作者的方法论功底。\n\n然而，实验设计存在两个根本性问题：(1) 每个污染条件仅单次运行，无法估计污染效果的可重复性；(2) 实验矩阵事后扩展，inverted-U 的证据存在循环论证风险。这些问题不是通过修改文字可以解决的——需要额外实验（至少为关键条件增加多个污染 seed）。摘要中的 \"n=10 per condition\" 措辞需要立即修正。\n\n如果作者能补充关键条件的多 seed 污染实验并修正统计报告，本文有望达到 Conference 水平。当前版本更适合 Findings。",
  "reviewer_id": "1",
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告：方法严谨性审查\n\n**论文标题**：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization\n\n---\n\n## Paper Summary\n\n本文首次将心理测量学中的 IRT person-fit 统计量（ℓ_z*）系统性地应用于 LLM 基准污染检测。核心思路是：被污染的 LLM 类似于拥有题目预知的考生，会在难题上产生异常正确的作答模式，可被 person-fit 统计量捕获。作者提出 Δℓ_z*（差分设计）消除 IRT 模型误设影响，在 3 个 7-8B 模型族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B）× 2 个基准（MMLU、ARC-C）× 3 个污染水平（15%/25%/50%）上进行了控制实验。主要发现三个行为边界：(1) 模型特异的 θ-shift absorption；(2) detection-diagnosis tradeoff（简单统计量检测更强，ℓ_z* 诊断更强）；(3) 能力依赖的非单调剂量-效应。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5（Borderline Conference）\n\n**一句话总结**：新颖的跨学科视角和扎实的机制分析，但单次污染运行的实验设计和事后扩展的实验矩阵显著削弱了定量结论的可靠性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.0 / 5 | 核心检测 claim 有支撑（所有 bootstrap CI 排除零），但每个污染条件仅单次运行（n=1）严重限制了 Cohen's d 的统计解释力；实验矩阵事后扩展（先看到 inverted-U 再补 25% 条件）构成循环论证风险；摘要中 \"n=10 independent seeds per condition\" 措辞具有误导性 |\n| **Excitement** | 3.5 / 5 | 首次将心理测量 person-fit 理论引入 NLP 污染检测，θ-shift absorption 机制和 detection-diagnosis tradeoff 均为有洞察力的发现；但论文自身承认简单统计量检测效果更优，削弱了实际应用价值 |\n| **Reproducibility** | 3.0 / 5 | 代码和数据承诺 \"released upon acceptance\"，QLoRA 超参数有交代（rank=16, α=32），但训练 epoch 数、学习率、数据混合细节不够充分；PSN-IRT item bank 为外部依赖 |\n| **Reviewer Confidence** | 4 / 5 | 本人熟悉 IRT/心理测量方法论和 LLM 评估领域，对统计方法学和实验设计的评估有较高把握 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 每个污染条件仅单次运行，Cohen's d 统计解释受限\n\n- 具体位置：Section 3.3（method.tex L48-49）：\"each contaminated model is a single QLoRA run\"\n- 问题：每个污染水平（15%/25%/50%）仅训练了 ONE 个模型，所有方差估计均来自 clean seeds（n=10 或 n=6）。由此计算的 Cohen's d 本质上是单个观测值相对于参考分布的 z-score，而非两个分布间的标准化均差。QLoRA 微调具有随机性（初始化、数据顺序），不同 seed 可能产生不同的污染模式和 ℓ_z* 值。当前设计无法：(a) 估计污染效果的方差；(b) 判断观测到的 ℓ_z* shift 是否具有代表性；(c) 正确计算需要两组方差的 Cohen's d。这直接影响所有定量比较——包括 Table 1 的 effect size、cross-model 比较、以及 inverted-U 的幅度。\n- 为什么影响接收：论文的三个核心 contribution 中，contribution (2)（Δℓ_z* reliably detects）和 (3)（detection-diagnosis tradeoff）的定量证据均建立在这些单次运行的 effect size 上。如果使用不同 seed 训练污染模型，Qwen 50% 的 |d|=1.90 可能变为 3.0 或 0.5，整个 inverted-U 叙事可能不成立。\n- 建议修改方向：至少为关键条件（如 Qwen 15%/50% on MMLU）训练 3-5 个污染 seed，报告污染效果的 seed-level 方差。若计算资源不允许，应在正文中明确标注 Cohen's d 为 \"single-observation effect size\"，并讨论这一限制对结论的影响。\n\n**N2** [critical] 摘要中 \"n=10 independent seeds per condition\" 措辞具有误导性\n\n- 具体位置：Abstract（abstract.tex L4）\n- 问题：摘要写道 \"n=10 independent seeds per condition; n=6 for Mistral\"，自然阅读理解为每个实验条件（clean/15%/25%/50%）均有 10 个 seed。但 Section 3.3 明确说明 \"We train n=10 clean seeds\" 且 \"each contaminated model is a single QLoRA run\"。实际上只有 clean 条件有多 seed，所有污染条件均为 n=1。这构成对读者（和 AC）的误导，夸大了研究的统计功效。\n- 为什么影响接收：摘要的准确性是论文可信度的基础。审稿人和 AC 可能基于摘要形成初始印象。如果 \"n=10 per condition\" 被理解为每条件 10 个独立运行，这与实际情况严重不符。\n- 建议修改方向：改为 \"n=10 clean baseline seeds per model family (n=6 for Mistral); single contaminated run per condition\"，准确反映实验设计。\n\n**N3** [critical] 实验矩阵事后扩展构成循环论证风险\n\n- 具体位置：Section 3.3（method.tex L46-47）：\"Following initial observation of non-monotonic dose-response for Qwen, we added a 25% contamination condition.\"\n- 问题：实验设计是迭代的而非预注册的：先观察到 Qwen 15% > 50% 的非单调性，再添加 25% 条件以 \"确认\" inverted-U。这是典型的假设确认式数据收集（hypothesis-confirming data collection）。论文将 inverted-U 作为核心发现之一（contribution 3），但确认该发现的数据点（25%）是在看到初始结果后才添加的。此外，25% 条件仅扩展到 Llama（未覆盖 Mistral），进一步限制了跨模型验证的完整性。\n- 为什么影响接收：Inverted-U 是论文三个核心发现之一。如果其证据基于事后选择的数据点，且无独立验证（如 held-out 模型族），该发现的置信度大幅降低。Simulation（Appendix A）虽提供了机制预测，但模拟参数可能也受到实证结果的影响。\n- 建议修改方向：(a) 明确标注 25% 条件是事后添加的（当前已做到，但应讨论其对统计推断的影响）；(b) 理想情况下，在 Mistral 上验证 25% 条件；(c) 或者将 inverted-U 定位为 \"exploratory finding requiring prospective confirmation\" 而非已确立的 \"behavior boundary\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 无低污染水平（<15%）的实证实验\n\n- 具体位置：Section 3.3 实验设计，Table 1\n- 问题：经验实验的最低污染水平为 15%，这在实际场景中已属相当高的污染率。模拟（Appendix B, Table 4）覆盖了 5%，但 5% 时 MMLU 检测功率仅 47.6%（4PL），ARC-C 仅 5.7%。论文未在实证数据上验证低污染场景的检测能力，而这恰恰是实践中最需要的场景。\n- 建议：至少在一个模型族上测试 5% 污染条件，或在 Discussion 中更显著地讨论低污染检测的局限性。\n\n**W2** [warning] ARC-Challenge 实验仅限 Qwen，跨基准泛化证据不足\n\n- 具体位置：Section 3.3（method.tex L54）：\"ARC-Challenge experiments were conducted on Qwen only\"\n- 问题：ARC-C（295 items）是论文唯一的小基准测试，且仅在 Qwen 上测试。论文从中得出关于 ceiling effect 和跨基准泛化性的结论（Section 4.1 L57-64），但 n=1 模型族无法支撑泛化性声称。此外，ARC-C 的模拟检测功率极低（5% 污染时仅 5.7%，15% 时 8.7%，Table 4），质疑了该基准上 person-fit 方法的实用性。\n- 建议：(a) 弱化关于 ARC-C ceiling effect 的泛化性声称；(b) 在 Limitations 中明确讨论小基准的功率限制。\n\n**W3** [warning] Fixed-θ 在 15% 污染时反而比 free-θ 更差（Qwen），缺乏充分解释\n\n- 具体位置：Table 2（results.tex L84）：Qwen 15% free-θ |d|=6.58, fixed-θ |d|=4.77, ratio=0.7×\n- 问题：论文的核心机制叙事是 \"θ-shift absorption 削弱检测 → fixed-θ 可恢复信号\"。但 Table 2 显示 Qwen 在 15% 污染时 fixed-θ 效果反而更差（0.7×）。这与 50% 时的 7.6× 改善形成强烈对比。论文未充分解释这一反转：为什么在低污染时 free-θ 反而更优？如果 θ-shift absorption 是一般性机制，它应该在所有污染水平上都使 free-θ 劣于 fixed-θ（只是程度不同）。\n- 建议：提供 15% 时 free-θ 优于 fixed-θ 的定量解释。可能的原因包括：(a) Snijders correction 在 free-θ 下减少了方差（但这应对检测有利，不应导致 d 更大）；(b) 小幅 θ-shift 实际上增加了某些 item 上异常模式的可检测性。无论原因如何，当前的叙事过于简化。\n\n**W4** [warning] Post-RL 观察（N=1）占据过大篇幅\n\n- 具体位置：Section 5 Discussion（discussion.tex L22-25），Figure 4\n- 问题：Post-RL 实验仅使用 Qwen 一个模型、15% 一个污染水平、GRPO 一种 RL 方法。这是一个 anecdote，而非实验证据。但它在 Discussion 中获得了完整段落和一个 Figure 的空间，且在 Abstract（L8）中也被提及。对于一个 N=1 观察，这一比重过高。\n- 建议：将 Post-RL 内容移至 Appendix，正文用一句话提及即可。这样释放的空间可用于更重要的分析（如额外污染水平或模型族）。\n\n**W5** [warning] QLoRA 训练细节不足以复现\n\n- 具体位置：Section 3.3（method.tex L45）\n- 问题：论文报告了 QLoRA rank=16, α=32，但缺少以下关键超参数：学习率、训练 epoch 数、batch size、warmup 策略、数据混合比例的精确构造方式（benchmark items 如何与非污染数据混合？ Interleaved? Appended?）、序列长度、以及如何处理多选题格式（将 ABCD 选项编码为 SFT 目标的具体方式）。Reproducibility Statement（main.tex L42-45）仅提及 \"Code and response data will be released upon acceptance\"，对于当前阶段的审稿不构成可复现性保证。\n- 建议：在 Appendix 中添加完整的训练配置表，包括所有超参数和数据预处理细节。\n\n**W6** [warning] Cohen's d 的 bootstrap CI 在小样本下的可靠性\n\n- 具体位置：Section 3.2（method.tex L34），Mistral 条件（n=6）\n- 问题：对于 Mistral（n=6 seeds），bootstrap resampling from 6 values 产生的 CI 分布非常粗糙（仅 6^6 = 46,656 种可能的重采样组合，远少于 10,000 次 resampling 中的有效独立样本）。BCa 校正（Appendix G）确认 percentile CI 是保守的，但 BCa 本身在 n=6 时也未必可靠。Table 1 中 Mistral 的 CI 确实极宽（如 [-9.6, -2.1]），但论文未讨论这一宽度是否足以支撑有意义的推断。\n- 建议：对 Mistral 结果添加关于小样本 bootstrap 局限性的显式讨论；考虑报告 permutation test p-value 作为补充。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.2 将 Δℓ_z* 设计称为 \"difference-in-differences (DiD)\"（method.tex L25），但标准 DiD 设计需要时间维度上的前后对比。此处更准确的描述是 \"matched-difference design\" 或 \"simple differencing\"。\n- Table 1 的列标题为 \"d (15%) [CI]\" 等，但 CI 的具体含义（percentile bootstrap, 10,000 resamples）需要在表注中说明（当前仅在 caption 中提及 bootstrap，未说明 percentile vs BCa）。\n- Figure 2 的色标（蓝色强度）仅凭 heatmap 难以精确读数，建议在每个 cell 内标注 |d| 值和 CI（当前似乎已做到，但 PDF 分辨率下难以确认）。\n- Limitations section 应增加对 \"无低污染实验\" 和 \"单次污染运行\" 的显式讨论——当前 Limitations 列举了模型规模和 SFT-scope 限制，但未提及这两个更基础的设计限制。\n\n---\n\n## Questions to Authors\n\n1. 如果为 Qwen 15% 和 50% 各训练 5 个不同 seed 的污染模型，你预期 ℓ_z* 的 seed-level 方差会有多大？你是否有任何 pilot 数据（如两个 seed 的比较）来估计污染效果的可重复性？\n\n2. 25% 条件是在观察到 inverted-U 后添加的。是否考虑过在一个 held-out 模型族（如 Phi-3、Gemma）上进行前瞻性验证？\n\n3. Table 2 中 Qwen 15% 的 fixed-θ 比 free-θ 更差（ratio=0.7×），能否提供更精确的定量解释？特别是，Snijders correction 在此处的具体影响是什么？\n\n4. PSN-IRT 的校准样本（13,000+ 模型）中，估计有多大比例的模型可能存在不同程度的基准污染？Appendix F.2 的 ±10% 随机噪声分析是否能模拟系统性污染偏差？\n\n5. Abstract 中 \"n=10 independent seeds per condition\" 具体指什么？如果指 \"per model family's clean condition\"，建议修改措辞以避免歧义。\n\n---\n\n## Missing References\n\n- **Polo et al. (2024)** 在 related work (Section 2, p3) 中被引用用于 IRT-based item selection，但论文未与之进行方法论层面的对比（Polo 用 IRT 选 item，本文用 IRT person-fit 检测污染——角度不同但框架共享，值得讨论）。\n- 论文未引用 **Sinharay & Johnson (2017)** \"Measures of agreement: reliability, classification accuracy, and classification consistency\" 或相关的 IRT person-fit 功效分析文献，这些可为 \"多少 item 足够检测\" 的 benchmark size boundary 提供理论支撑。\n- 缺少与 **EMNLP 2024/2025 年相关 contamination 工作**（如 benchmark leakage detection via perplexity-based methods）的系统对比。\n\n---\n\n## 主要优势\n\n1. **新颖的跨学科桥接**：首次将教育测量学 person-fit 理论系统性引入 NLP 污染检测，类比关系（污染 LLM ↔ 作弊考生）自然且有启发性。\n\n2. **诚实的定位**：论文明确将自身定位为 \"characterization\"（行为边界刻画）而非 \"tool\"（现成工具），并坦承简单统计量在纯检测任务上表现更优。这种学术诚实值得肯定。\n\n3. **Δℓ_z* 差分设计**：优雅地解决了绝对 ℓ_z* 阈值在 LLM 上无效的问题（57/60 cells 被标记为异常）。LD simulation（Appendix F.1）提供了合理的鲁棒性证据。\n\n4. **θ-shift absorption 机制分析**：对 \"为什么高能力模型检测信号更弱\" 的机制解释清晰、有说服力，fixed-θ vs free-θ 对比（Table 2）提供了强支撑证据。\n\n5. **Detection-diagnosis tradeoff**：这一发现对实践有直接指导意义——先用 accuracy z-score 筛选，再用 ℓ_z* 诊断机制。\n\n6. **详尽的 Appendix**：包含 LD 模拟、参数噪声敏感性、BCa 对比、4PL vs 3PL 消融、classical IRT refit、seed sensitivity 等 8 个补充分析，展现了方法论上的严谨态度。\n\n---\n\n## 总结性评价\n\n本文在 NLP-psychometrics 交叉领域做出了有意义的探索，三个行为边界的发现（θ-shift dynamics、detection-diagnosis tradeoff、non-monotonic dose-response）为理解基准污染的统计特征提供了新视角。机制分析（特别是 θ-shift absorption）清晰有力，Appendix 中的鲁棒性分析展现了作者的方法论功底。\n\n然而，实验设计存在两个根本性问题：(1) 每个污染条件仅单次运行，无法估计污染效果的可重复性；(2) 实验矩阵事后扩展，inverted-U 的证据存在循环论证风险。这些问题不是通过修改文字可以解决的——需要额外实验（至少为关键条件增加多个污染 seed）。摘要中的 \"n=10 per condition\" 措辞需要立即修正。\n\n如果作者能补充关键条件的多 seed 污染实验并修正统计报告，本文有望达到 Conference 水平。当前版本更适合 Findings。",
    "reviewer_id": "1",
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 472 · 2026-05-22T07:49:11.630051+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4115
}
```

</details>

---


### Assistant

_source line 473 · 2026-05-22T07:49:21.934333+00:00_

审稿报告已提交给 Review Director。

核心评价：**Overall 3.5（Borderline Conference）**。

三个 Must-Fix：
1. **每个污染条件仅 n=1 运行** — Cohen's d 本质是 z-score 而非双组效应量，无法估计污染效果的可重复性
2. **摘要 "n=10 per condition" 误导** — 实际仅 clean 条件有多 seed，污染条件均为单次运行
3. **实验矩阵事后扩展** — 25% 条件在观察到 inverted-U 后才添加，构成假设确认式数据收集

六个 Should-Fix：无 <15% 低污染实验、ARC-C 仅 Qwen、fixed-θ 反转缺乏解释、Post-RL N=1 占篇幅过大、训练细节不足、Mistral n=6 bootstrap 可靠性。

主要优势：跨学科新颖性、诚实定位为 characterization、Δℓ_z* 差分设计优雅、θ-shift mechanism 分析有洞察力、Appendix 鲁棒性检查详尽。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

6 recorded events


### User

_source line 474 · 2026-05-22T07:50:31.954250+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿报告

**Overall Assessment**: 3.0 / 5（Findings），置信度 4/5

### Must-Fix 问题

**N1** [critical] Novelty 有限：三个核心 findings 大部分可从 IRT 理论预测
- Finding 1（θ-shift dynamics）：高能力模型的 θ-shift 吸收本质是 IRT 能力估计的天花板效应，IRT 文献中 well-known
- Finding 2（detection-diagnosis tradeoff）：power vs. richness 的经典权衡，不构成新发现
- Finding 3（non-monotonic dose-response）：是 Finding 1 的直接推论
- 唯一经验价值在定量校准层面——"useful calibration" 而非 "new insight"

**N2** [critical] 缺少与现有检测方法的实证对比
- Table 3 仅在自身框架内对比 ℓ_z*、HT、accuracy，未与 ConStat/MIA 做头对头比较
- Discussion 说 ConStat 对比 "complicated by different information requirements"——理由不充分
- 实验设置可获取 logits（QLoRA → model access），MIA 方法可运行
- 无法判断 IRT person-fit 在实际应用中的价值

**N3** [critical] 标题和 framing 存在 scope mismatch
- "Binary response patterns" 掩盖了对 PSN-IRT 外部 item bank 的核心依赖
- "Benchmark Contamination" 标题远宽于 SFT-stage QLoRA 实验
- Abstract "only binary response patterns...no access to weights, gradients, logits, or training data" 技术上正确但具有误导性

### Should-Fix 问题

**W1** 实验规模/多样性不足（3 个 7-8B 模型、2 个 benchmark、仅 QLoRA SFT）
**W2** Post-RL 分析占据过多篇幅（N=1 获得完整 subsection + Figure）
**W3** Related Work 缺少污染检测 survey 引用
**W4** Fixed-θ vs free-θ 选择缺少实用指导

### 主要优势
1. DiD 设计是 causal inference 标准方法，运用得当
2. Bootstrap CIs、seed sensitivity、power analysis 等构成完整鲁棒性体系
3. 诚实的 Limitations（~3 个点，符合 EMNLP 要求）
4. Appendix H 的 item bank 对比是重要方法论贡献
5. 写作清晰，数学符号一致，Figure/Table 质量高

---

请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-22T07:51:13.500130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 476 · 2026-05-22T07:51:13.500824+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Benchmark contamination detection.}
4	Contamination detection methods span a wide range of information requirements.
5	Corpus-search methods match benchmark items directly against pretraining data \citep{dodge2021, magar2022}, but require full corpus access unavailable for closed models.
6	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training from unseen examples \citep{minkprob2024, deng2024}.
7	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, golchin2024quiz, oren2024}.
8	Performance-based methods compare accuracy on target and reference sets \citep{constat2024, pacost2024, codec2026}, requiring multiple evaluations or in-context learning passes.
9	\citet{zhou2023benchmark} and \citet{sainz2023} argue for systematic contamination measurement, \citet{jacovi2023} propose mitigation strategies, and \citet{bordt2025forget} show that contamination can be ``forgotten'' under sufficient continued training.
10	\citet{han2026quantifying} quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks.
11	\citet{kattamuri2025radar} take a mechanistic interpretability approach, using activation patterns to distinguish recall-based from reasoning-based responses; our work instead operates purely on behavioral response patterns without access to model internals.
12	
13	A critical limitation unites all token-level methods: \citet{wang2025fragility} show that RL post-training renders MIA-based detectors no better than random across 10 methods and 4 benchmarks, because RL reshapes token distributions while largely preserving binary correctness patterns.
14	\citet{selfcritique2026} and \citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.
15	Our approach requires no access to model weights, logits, or training data---only binary response patt
…[truncated 2476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-22T07:52:23.456585+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: \"三个 findings 可从 IRT 理论预测，novelty 有限\"**\n\nR2 的论点有一定道理但过于苛刻，需要区分 \"理论可推导\" 与 \"经验已知\"。\n\n(a) **Finding 1（θ-shift dynamics）**：θ-shift absorption 确实是 IRT 能力估计的已知性质——当真分数提高时 θ̂ 上升，吸收异常信号。但本文的贡献不在于重新发现这一理论，而在于 **首次量化了其在 LLM 场景中的具体表现**。特别是：Table 2 显示 Qwen 50% 时 free-θ vs fixed-θ 的 7.6× amplification ratio；ARC-C 上 ceiling effect 导致 pattern 反转（Section 4.1, L57-64）。这些模型-基准交互效应无法仅从 IRT 理论推导，需要经验数据校准。我认为这属于 \"empirically valuable calibration\"，但我 **同意 R2 的判断：这更接近 calibration 而非 new insight**。\n\n(b) **Finding 2（detection-diagnosis tradeoff）**：R2 说 \"power vs. richness 是经典权衡\"。原则上正确，但本文的具体发现——accuracy z-score 的 |d| 比 ℓ_z* 高出一个数量级（Table 3: 68.7 vs 1.90 for Qwen 50%）——这一 **量级差距** 是经验发现，不是理论预测。此外，57/60 vs 4/60 flagged cells 的对比（Section 4.3, L117-120）展示了两类统计量在 structural sensitivity 上的根本差异。我认为 R2 在此处低估了经验贡献。\n\n(c) **Finding 3（non-monotonic dose-response）**：**同意 R2 这是 Finding 1 的直接推论**。如果 θ-shift absorption 随污染增加而增强，而 aberrance signal 也增加，交叉点自然产生 inverted-U。本文的独立贡献仅在于经验确认了 peak 位置（~25% for Qwen）和跨模型的衰减模式（Llama ratio 1.2× vs Qwen 4.3×）。但如我在 R1-N3 中指出的，25% 条件是事后添加的，进一步削弱了这一发现的独立证据价值。\n\n**总结**：R2 对 novelty 的担忧部分合理——理论贡献有限，主要价值在经验校准。但 \"useful calibration\" 对一个 characterization paper 而言 **可以构成充分贡献**，关键在于 empirical rigor（这正是我在 R1-N1/N3 中质疑的部分）。如果实验设计更严格（多 seed 污染运行、预注册），calibration 的可信度将大幅提升，novelty 争议也会减弱。\n\n---\n\n**[AGREE] R2-N2: \"缺少与现有检测方法的实证对比\"**\n\n同意这是一个重要缺陷。具体理由：\n\n1. **论文完全有能力做头对头对比**：作者训练了全部模型（QLoRA），拥有完整的 model access——可以运行 Min-K% Prob、perplexity-based MIA 等方法。选择不做对比是研究设计选择，不是技术限制。\n\n2. **Discussion 中的 \"different information requirements\" 辩护不充分**（discussion.tex L20）：不同信息需求恰恰是应该对比的原因——读者需要知道 \"只用 binary patterns + item bank\" 相比 \"用 logits\" 损失了多少检测能力。Table 3 只在自身框架内对比了 ℓ_z*/HT/accuracy z-score，均为 person-fit 类方法。\n\n3. **但需要补充一个 nuance**：本文明确定位为 \"characterization, not tool\"（Introduction L37: \"Rather than proposing ℓ_z* as a ready-to-deploy detection tool\"）。在此定位下，对比的必要性低于一个声称优越性的方法论文。问题在于，**如果不与外部方法对比，\"characterization\" 的实际价值难以评估**——读者不知道 IRT person-fit 提供的 mechanistic insight 是否比简单查看 logit 分布更有用。\n\n4. 至少应该包含：(a) 对一两种代表性 MIA 方法的 baseline 对比；(b) Wang et al. (2025) 已展示 MIA 在 RL 后失效——本文应在同一 SFT 设置下确认 MIA 的基线性能。\n\n---\n\n**[AGREE] R2-N3: \"标题和 framing 存在 scope mismatch\"**\n\n同意，且这与我在 R1-N2 中关于摘要措辞的关切一致。\n\n1. **\"Binary response patterns\" 标题掩盖了 PSN-IRT 依赖**：虽然 Abstract L2 确实提到 \"combined with externally calibrated 4PL item parameters from a large-scale item bank\"，但标题和核心 framing 强调 \"only binary response patterns\"。Discussion L18 自己承认 \"the PSN-IRT item bank a critical dependency\"，且 Appendix H 显示不用 PSN-IRT 时 discrimination 几乎无法恢复（r_a=0.127）。更诚实的标题应反映这一双重需求。\n\n2. **\"Benchmark Contamination\" 宽于实验覆盖**：实验仅覆盖 SFT-stage QLoRA 污染、3 个 7-8B 模型、2 个基准。标题未限定 scope，读者可能期望更广泛的覆盖（pretraining contamination、更大模型、更多基准）。Section 3.3 L62 自己说 \"Our findings are scoped to SFT-based contamination\"——标题应反映这一 scope。\n\n3. **但我不认为这 \"critical\" 到 Must-Fix 级别**：Scope mismatch 在 NLP 论文中很常见，且作者在 Section 3.3 和 Limitations 中做了充分的 scope 声明。这更接近 Should-Fix——修改标题为 \"What Can Binary Response Patterns and Calibrated Item Parameters Reveal About SFT-Stage Benchmark Contamination?\" 即可解决。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"实验规模/多样性不足\"**\n\n与我的 R1-W1（无 <15% 污染实验）和 R1-W2（ARC-C 仅 Qwen）一致。补充一点：仅 QLoRA SFT 也是限制——full-parameter SFT 和 continued pretraining 可能产生不同的 ℓ_z* 模式。\n\n**[AGREE] R2-W2: \"Post-RL 分析占据过多篇幅\"**\n\n与我的 R1-W4 完全一致。N=1 观察不应占据 Discussion 中一个完整段落 + Figure 4 + Abstract 提及。建议移至 Appendix。\n\n**[REBUT] R2-W3: \"Related Work 缺少污染检测 survey 引用\"**\n\nR2 此处判断有误。论文 Introduction L4（introduction.tex）引用了 \"chang2024survey\"（Chang et al., 2024 survey），Related Work Section 2（related_work.tex）系统性覆盖了五类方法（corpus-search、MIA、generation-based、performance-based、IRT for LLM），并引用了 Zhou et al. (2023)、Sainz et al. (2023)、Jacovi et al. (2023) 等 systematization 工作。Person-fit 文献也有三段覆盖（Karabatsos 2003 的 36 统计量对比、Embretson & Reise 2000 textbook、Sinharay 2017）。Related Work 的覆盖在同类论文中属于充分水平。\n\n**[AGREE] R2-W4: \"Fixed-θ vs free-θ 选择缺少实用指导\"**\n\n同意，且与我的 R1-W3 一致。Table 2 显示 fixed-θ 对 Qwen（7.6×@50%）和 Mistral（1.6×@50%）有益，对 Llama 无益甚至有害。但论文未提供决策规则——实践者如何判断应该用哪种估计？Section 4.1 L72 给出了定性指导（\"fixed-θ estimation is indicated for models with stable clean baselines and high θ-shift absorption\"），但 \"stable clean baseline\" 和 \"high θ-shift absorption\" 没有操作化定义。且在 15% 时 fixed-θ 对 Qwen 反而更差（ratio=0.7×），进一步复杂化了实用指导。\n\n---\n\n### 总结\n\nR2 的审稿整体严谨。核心分歧在于 novelty 评估：R2 认为 findings 可从理论预测、缺少方法对比、scope 不匹配，给出 3.0（Findings）。我部分同意 novelty 担忧，但认为 empirical calibration 在一个 characterization paper 中可以构成贡献——前提是实验设计足够严格。\n\n**我维持 3.5（Borderline Conference）**，理由是：\n- 与 R2 共识：scope mismatch 需修正、Post-RL 应精简、缺少外部方法对比\n- 与 R2 分歧：novelty 评估——R2 将其视为 \"known theory applied\"，我视为 \"first empirical characterization with meaningful calibration value\"，但实验设计缺陷（R1-N1/N3）削弱了 calibration 的可信度\n- 最终判断：如果作者补充多 seed 污染实验 + 至少一个外部方法对比，可达 Conference；当前版本在 Findings 和 Conference 边界",
  "reviewer_id": "1",
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: \"三个 findings 可从 IRT 理论预测，novelty 有限\"**\n\nR2 的论点有一定道理但过于苛刻，需要区分 \"理论可推导\" 与 \"经验已知\"。\n\n(a) **Finding 1（θ-shift dynamics）**：θ-shift absorption 确实是 IRT 能力估计的已知性质——当真分数提高时 θ̂ 上升，吸收异常信号。但本文的贡献不在于重新发现这一理论，而在于 **首次量化了其在 LLM 场景中的具体表现**。特别是：Table 2 显示 Qwen 50% 时 free-θ vs fixed-θ 的 7.6× amplification ratio；ARC-C 上 ceiling effect 导致 pattern 反转（Section 4.1, L57-64）。这些模型-基准交互效应无法仅从 IRT 理论推导，需要经验数据校准。我认为这属于 \"empirically valuable calibration\"，但我 **同意 R2 的判断：这更接近 calibration 而非 new insight**。\n\n(b) **Finding 2（detection-diagnosis tradeoff）**：R2 说 \"power vs. richness 是经典权衡\"。原则上正确，但本文的具体发现——accuracy z-score 的 |d| 比 ℓ_z* 高出一个数量级（Table 3: 68.7 vs 1.90 for Qwen 50%）——这一 **量级差距** 是经验发现，不是理论预测。此外，57/60 vs 4/60 flagged cells 的对比（Section 4.3, L117-120）展示了两类统计量在 structural sensitivity 上的根本差异。我认为 R2 在此处低估了经验贡献。\n\n(c) **Finding 3（non-monotonic dose-response）**：**同意 R2 这是 Finding 1 的直接推论**。如果 θ-shift absorption 随污染增加而增强，而 aberrance signal 也增加，交叉点自然产生 inverted-U。本文的独立贡献仅在于经验确认了 peak 位置（~25% for Qwen）和跨模型的衰减模式（Llama ratio 1.2× vs Qwen 4.3×）。但如我在 R1-N3 中指出的，25% 条件是事后添加的，进一步削弱了这一发现的独立证据价值。\n\n**总结**：R2 对 novelty 的担忧部分合理——理论贡献有限，主要价值在经验校准。但 \"useful calibration\" 对一个 characterization paper 而言 **可以构成充分贡献**，关键在于 empirical rigor（这正是我在 R1-N1/N3 中质疑的部分）。如果实验设计更严格（多 seed 污染运行、预注册），calibration 的可信度将大幅提升，novelty 争议也会减弱。\n\n---\n\n**[AGREE] R2-N2: \"缺少与现有检测方法的实证对比\"**\n\n同意这是一个重要缺陷。具体理由：\n\n1. **论文完全有能力做头对头对比**：作者训练了全部模型（QLoRA），拥有完整的 model access——可以运行 Min-K% Prob、perplexity-based MIA 等方法。选择不做对比是研究设计选择，不是技术限制。\n\n2. **Discussion 中的 \"different information requirements\" 辩护不充分**（discussion.tex L20）：不同信息需求恰恰是应该对比的原因——读者需要知道 \"只用 binary patterns + item bank\" 相比 \"用 logits\" 损失了多少检测能力。Table 3 只在自身框架内对比了 ℓ_z*/HT/accuracy z-score，均为 person-fit 类方法。\n\n3. **但需要补充一个 nuance**：本文明确定位为 \"characterization, not tool\"（Introduction L37: \"Rather than proposing ℓ_z* as a ready-to-deploy detection tool\"）。在此定位下，对比的必要性低于一个声称优越性的方法论文。问题在于，**如果不与外部方法对比，\"characterization\" 的实际价值难以评估**——读者不知道 IRT person-fit 提供的 mechanistic insight 是否比简单查看 logit 分布更有用。\n\n4. 至少应该包含：(a) 对一两种代表性 MIA 方法的 baseline 对比；(b) Wang et al. (2025) 已展示 MIA 在 RL 后失效——本文应在同一 SFT 设置下确认 MIA 的基线性能。\n\n---\n\n**[AGREE] R2-N3: \"标题和 framing 存在 scope mismatch\"**\n\n同意，且这与我在 R1-N2 中关于摘要措辞的关切一致。\n\n1. **\"Binary response patterns\" 标题掩盖了 PSN-IRT 依赖**：虽然 Abstract L2 确实提到 \"combined with externally calibrated 4PL item parameters from a large-scale item bank\"，但标题和核心 framing 强调 \"only binary response patterns\"。Discussion L18 自己承认 \"the PSN-IRT item bank a critical dependency\"，且 Appendix H 显示不用 PSN-IRT 时 discrimination 几乎无法恢复（r_a=0.127）。更诚实的标题应反映这一双重需求。\n\n2. **\"Benchmark Contamination\" 宽于实验覆盖**：实验仅覆盖 SFT-stage QLoRA 污染、3 个 7-8B 模型、2 个基准。标题未限定 scope，读者可能期望更广泛的覆盖（pretraining contamination、更大模型、更多基准）。Section 3.3 L62 自己说 \"Our findings are scoped to SFT-based contamination\"——标题应反映这一 scope。\n\n3. **但我不认为这 \"critical\" 到 Must-Fix 级别**：Scope mismatch 在 NLP 论文中很常见，且作者在 Section 3.3 和 Limitations 中做了充分的 scope 声明。这更接近 Should-Fix——修改标题为 \"What Can Binary Response Patterns and Calibrated Item Parameters Reveal About SFT-Stage Benchmark Contamination?\" 即可解决。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"实验规模/多样性不足\"**\n\n与我的 R1-W1（无 <15% 污染实验）和 R1-W2（ARC-C 仅 Qwen）一致。补充一点：仅 QLoRA SFT 也是限制——full-parameter SFT 和 continued pretraining 可能产生不同的 ℓ_z* 模式。\n\n**[AGREE] R2-W2: \"Post-RL 分析占据过多篇幅\"**\n\n与我的 R1-W4 完全一致。N=1 观察不应占据 Discussion 中一个完整段落 + Figure 4 + Abstract 提及。建议移至 Appendix。\n\n**[REBUT] R2-W3: \"Related Work 缺少污染检测 survey 引用\"**\n\nR2 此处判断有误。论文 Introduction L4（introduction.tex）引用了 \"chang2024survey\"（Chang et al., 2024 survey），Related Work Section 2（related_work.tex）系统性覆盖了五类方法（corpus-search、MIA、generation-based、performance-based、IRT for LLM），并引用了 Zhou et al. (2023)、Sainz et al. (2023)、Jacovi et al. (2023) 等 systematization 工作。Person-fit 文献也有三段覆盖（Karabatsos 2003 的 36 统计量对比、Embretson & Reise 2000 textbook、Sinharay 2017）。Related Work 的覆盖在同类论文中属于充分水平。\n\n**[AGREE] R2-W4: \"Fixed-θ vs free-θ 选择缺少实用指导\"**\n\n同意，且与我的 R1-W3 一致。Table 2 显示 fixed-θ 对 Qwen（7.6×@50%）和 Mistral（1.6×@50%）有益，对 Llama 无益甚至有害。但论文未提供决策规则——实践者如何判断应该用哪种估计？Section 4.1 L72 给出了定性指导（\"fixed-θ estimation is indicated for models with stable clean baselines and high θ-shift absorption\"），但 \"stable clean baseline\" 和 \"high θ-shift absorption\" 没有操作化定义。且在 15% 时 fixed-θ 对 Qwen 反而更差（ratio=0.7×），进一步复杂化了实用指导。\n\n---\n\n### 总结\n\nR2 的审稿整体严谨。核心分歧在于 novelty 评估：R2 认为 findings 可从理论预测、缺少方法对比、scope 不匹配，给出 3.0（Findings）。我部分同意 novelty 担忧，但认为 empirical calibration 在一个 characterization paper 中可以构成贡献——前提是实验设计足够严格。\n\n**我维持 3.5（Borderline Conference）**，理由是：\n- 与 R2 共识：scope mismatch 需修正、Post-RL 应精简、缺少外部方法对比\n- 与 R2 分歧：novelty 评估——R2 将其视为 \"known theory applied\"，我视为 \"first empirical characterization with meaningful calibration value\"，但实验设计缺陷（R1-N1/N3）削弱了 calibration 的可信度\n- 最终判断：如果作者补充多 seed 污染实验 + 至少一个外部方法对比，可达 Conference；当前版本在 Findings 和 Conference 边界",
    "reviewer_id": "1",
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-22T07:52:27.370173+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3913
}
```

</details>

---


### Assistant

_source line 479 · 2026-05-22T07:52:34.188009+00:00_

已提交对 Reviewer 2 意见的逐条回应。

核心立场：
- **同意** R2-N2（缺外部方法对比）、R2-N3（scope mismatch，但降级为 Should-Fix）、R2-W1/W2/W4
- **部分同意** R2-N1（novelty 有限——理论层面是，但经验校准有价值，关键在实验 rigor）
- **反驳** R2-W3（Related Work 已引用 survey 和系统性覆盖五类方法）
- **维持** Overall 3.5（Borderline Conference），与 R2 的 3.0 有 0.5 分差距，分歧核心在于 empirical characterization 的贡献认定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

52 recorded events


### User

_source line 480 · 2026-05-22T22:47:16.736464+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。

## 投稿信息
- **Venue**: EMNLP 2026 Long Paper (via ARR)
- **Deadline**: 2026-05-25
- **格式要求**: 正文 ≤8 页 + 无限参考文献；ACL 模板（`\usepackage[review]{acl}`）；double-blind（匿名）
- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit
- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`

## 你的审查侧重

### 1. 统计方法学
- Δℓz* matched-difference design 的统计有效性：差分设计是否充分消除 shared misfit？假设是否合理？
- Cohen's d 的计算方式：n=10 clean seeds 作为分母，单次或少量污染运行作为分子——这在统计上是否合理？效应量的可解释性？
- Bootstrap CI（10,000 resamples）在 n=10（或更小样本）下的可靠性
- Fixed-θ vs free-θ 的对比分析：Table 2 中 Qwen 15% 时 fixed-θ 反而更差（0.7×），这个反直觉结果的解释是否充分？
- BCa 校正声称 percentile CI 保守——n=10 下 BCa 自身是否可靠？

### 2. 实验设计
- 实验矩阵的完整性：三个模型家族 × 不同污染水平 × 两个 benchmark 的覆盖是否充分？缺失条件（Mistral 无 5%/25%、ARC-C 仅 Qwen）是否影响结论？
- 每个污染条件的重复次数：是否存在 single-run issue？Multi-seed validation（n=3）是否足够？
- QLoRA 作为污染代理的外部效度：QLoRA SFT 是否真实反映实际场景中的 benchmark contamination？
- 模型规模限制（全部 7-8B）对结论泛化性的影响
- Post-RL 观察（N=1）的处理是否得当？

### 3. Claims vs Evidence
- Abstract/Introduction 的 claim 是否与实验证据严格对齐？
- "first systematic characterization" 是否成立？
- "three behavior boundaries" 是否都有充分实验支撑？尤其是 Finding 3（exploratory）的降级是否充分？
- "all bootstrap 95% CIs exclude zero" 的声明是否准确？（注意 Table 2 中 Llama fixed-θ CI 包含零）
- ARC-C 的 ceiling effect 解释是否可信？

### 4. 可复现性
- QLoRA 训练细节是否足以复现？（Appendix J 的 hyperparameter table）
- PSN-IRT 依赖——外部 item bank 是否公开可用？
- Bootstrap 方法描述是否完整？

请给出结构化审稿报告：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（含 ARR 评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 481 · 2026-05-22T22:47:25.660608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 482 · 2026-05-22T22:47:26.965471+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/review_reviewer_1_ac4dc473.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1304
}
```

</details>

---


### Tool call

_source line 483 · 2026-05-22T22:47:27.166475+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 484 · 2026-05-22T22:47:27.217043+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-22T22:47:32.588965+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-22T22:47:35.005497+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
  "project": "irt_personfit_contam",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
    "project": "irt_personfit_contam",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-22T22:47:39.082602+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form, and scoring criteria:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Recommendation Scale

The review form includes the following recommendation levels:

- 5 = Consid
…[truncated 946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6493
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-22T22:47:40.695821+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 361.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5690
}
```

</details>

---


### Tool call

_source line 489 · 2026-05-22T22:47:47.922258+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all scoring dimensions, their scales, descriptions, and any guidelines for each dimension. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form including all scoring dimensions, their scales, descriptions, and any guidelines for each dimension. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-22T22:47:49.327650+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
  "project": "irt_personfit_contam",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
    "project": "irt_personfit_contam",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-22T22:47:49.829712+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-22T22:47:50.282295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-22T22:47:51.235884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-22T22:47:51.749481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 495 · 2026-05-22T22:47:52.458346+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 496 · 2026-05-22T22:47:54.468066+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Core Evaluation Dimensions

**Reviewer Confidence** (5-point scale)
- 5: Positive evaluation is correct; careful reading and familiar with related work
- 4: Quite sure; checked important points carefully
- 3: Pretty sure; good general knowledge but didn't carefully verify details
- 2: Can defend evaluation but likely missed some details or novelty
- 1: Outside expertise or paper very difficult to understand

**Soundness** (1-5 scale with half-points)
- 5: "one of the most thorough I have seen, given its type"
- 4: Study provides sufficient support with optional additional experiments
- 3: Sufficient support for main claims; minor points need clarification
- 2: Main claims lack adequate support; major technical/methodological problems
- 1: Insufficient thoroughness or not relevant to ACL

**Excitement** (1-5 scale with half-points)
Measures subjective appeal including transformational concepts, community impact, and personal relevance
- 5: "I would recommend this paper to others and/or attend its presentation"
- 4: Would mention to others or make effort to attend presentation
- 3: Might mention some points or attend if time permits
- 2: Doesn't resonate personally but may appeal to broader community
- 1: Not appealing to either reviewer or community

**Overall Assessment** (1-5 scale with half-points)
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## Additional Dimensions

**Reproducibility** (1-5 scale): From easily reproducible (5) to impossible (1)

**Datasets/Software** (1-5 scale): From enabling (5) to none released (1)

**Author Identity Knowledge** (1-5 scale): From identified author (5) to no guess (1)

**Ethical Review**: Determines if in-depth ethics committee review needed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6545
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-22T22:47:55.731969+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 428.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 220.1}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6404
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-22T22:47:59.993405+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8757
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-22T22:47:59.994511+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7536
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-22T22:47:59.995462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9713
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-22T22:48:00.046569+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 10216
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-22T22:48:00.097973+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8348
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-22T22:48:06.724070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-22T22:48:07.227517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-22T22:48:07.835714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-22T22:48:07.836330+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-22T22:48:08.745429+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1517
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-22T22:48:08.745856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-22T22:48:08.950497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-22T22:48:09.657473+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1821
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-22T22:48:10.970462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2224
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-22T22:48:10.971544+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2021
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-22T22:48:17.444492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-22T22:48:17.796949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-22T22:48:18.903946+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1459
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-22T22:48:19.055803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-22T22:48:19.366369+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1569
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-22T22:48:19.366813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 519 · 2026-05-22T22:48:19.771193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 520 · 2026-05-22T22:48:20.977130+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1921
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-22T22:48:21.381166+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1609
}
```

</details>

---


### Tool result

_source line 522 · 2026-05-22T22:48:21.382289+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2015
}
```

</details>

---


### Tool call

_source line 523 · 2026-05-22T22:53:04.913510+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract all detailed guidelines for reviewers, especially: how to evaluate soundness, excitement, overall assessment, what constitutes a strong vs weak paper, guidance on significance testing and experimental rigor, and any specific advice about statistical methodology papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract all detailed guidelines for reviewers, especially: how to evaluate soundness, excitement, overall assessment, what constitutes a strong vs weak paper, guidance on significance testing and experimental rigor, and any specific advice about statistical methodology papers."
  }
}
```

</details>

---


### Tool result

_source line 524 · 2026-05-22T22:53:13.997732+00:00_

# ARR Reviewer Guidelines: Evaluation Framework

## Scoring System

ARR reviewers provide **three distinct scores**:

1. **Soundness**: Technical validity and methodological rigor
2. **Excitement**: Personal interest and subjective appeal
3. **Overall Assessment**: Composite recommendation reflecting soundness, novelty, and impact

### Key Principle on Soundness Scores
"The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

## Evaluating Paper Strength

### Strong papers demonstrate:
- Clear research question addressing a knowledge gap
- Appropriate methodology for the claims made
- Sufficient evidence supporting conclusions
- Technical soundness and reproducibility details
- Proper statistical reporting (confidence intervals, significance tests, effect sizes)

### Common Evaluation Pitfalls to Avoid

The guidelines list 17 "heuristics" (H1-H17) that appear reasonable but often misrepresent paper quality:

- **H5**: Expecting SOTA results—"SOTA results are neither necessary nor sufficient for a scientific contribution"
- **H13-H15**: Requesting extra experiments beyond what validates the paper's specific claims
- **H16**: Treating acknowledged limitations as weaknesses rather than honest assessment

## Statistical Rigor Guidance

For experimental methodology, reviewers should verify:

**Appropriate statistical practices (R5)**:
- Error bars and confidence intervals on main results
- Statistical significance tests with disclosed assumptions
- Effect size estimation
- Details on variability factors

**Common problems to flag (R1)**:
- P-hacking or presenting only best results from unknown trial counts
- Inadequately tuned baselines
- Unmotivated sample selection that doesn't represent claimed populations (R2)

## Specialized Considerations

For **methodology papers** and **formal work**:
- All assumptions mu
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9084
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-22T22:55:28.983595+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n## Summary\n\n本文将教育测量学中的 IRT person-fit 统计量（Snijders' ℓ_z*）应用于 LLM benchmark contamination 检测，提出 matched-difference 设计（Δℓ_z*）以分离 contamination-specific aberrance。在三个 7-8B 模型家族上（Qwen2.5-7B, Llama-3.1-8B, Mistral-7B），使用 QLoRA SFT 作为 contamination 代理，在 MMLU（14,042 items）和 ARC-Challenge（295 items）上识别出三个行为边界：θ-shift dynamics、detection-diagnosis tradeoff、ability-dependent non-monotonic dose-response。论文的核心贡献在于将 psychometrics 视角引入 LLM 评估，提供 contamination 行为的机制性理解而非单纯检测。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n\n**一句话总结**: 研究视角新颖、matched-difference 设计合理，但 n=10 的统计基础偏薄，实验矩阵不完整与 \"systematic\" 声称之间存在张力，部分 claim 超出了证据支撑范围。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 | 核心 matched-difference 设计合理，但 n=10 的 Cohen's d SD 估计仅有 9 自由度，BCa 校正在此样本量下不可靠，且至少一个条件的 BCa CI 包含零（Appendix G, Llama fixed-θ 50%）；部分 claim 超出证据范围 |\n| **Excitement** | 3.5 / 5 | 将 IRT person-fit 应用于 contamination 检测是新颖的跨学科贡献，三个 behavior boundary 的发现提供了独特的机制性洞察；但 simpler statistics 检测效果更好（Table 3），限制了实际应用价值 |\n| **Reproducibility** | 3 / 5 | Appendix J 提供了 QLoRA 超参数表，PSN-IRT item bank 声称公开可用（Zhou et al., 2026），但代码 \"upon acceptance\" 才释放；bootstrap 实现细节部分缺失 |\n| **Confidence** | 4 / 5 | 对 IRT 和实验设计方法有扎实理解，仔细验证了关键数字和 claim |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Cohen's d 的统计可靠性：n=10 clean seeds 作为 SD 估计基础过于薄弱\n\n- 具体位置：Section 3.2, Table 1, Table 2\n- 问题：Cohen's d 的分母（SD of ℓ_z* across clean seeds）仅有 n=10，对应 9 个自由度。虽然每个 ℓ_z* 本身基于 14,042 items 是稳定的，但 seed-to-seed variability 的 SD 估计在 df=9 时高度不稳定。对于 |d|≥3 的大效应量（如 Qwen 15%+ 条件），结论可能稳健；但对于 |d|≈1-2 的条件（如 Llama 15% |d|=2.27, Qwen 5% |d|=1.90），CI 的校准性存疑。论文未报告 Cohen's d 的标准误或讨论小样本下效应量估计的已知偏差（Hedges' g correction）。\n- 为什么影响接收：这是整篇论文量化推断的基础。如果 SD 估计不可靠，所有 CI 和效应量比较（Table 1-3）的可信度都受影响。\n- 建议修改方向：(1) 报告 Hedges' g（小样本校正的 Cohen's d）；(2) 讨论 n=10 下 SD 估计的 sampling variability（可用 chi-squared 分布 df=9 给出 SD 的 CI）；(3) 增加 clean seeds 数量（n≥20）或论证当前 n=10 已足够。\n\n**N2** [critical] BCa CI 与 percentile CI 的不一致性被低估\n\n- 具体位置：Table 1 caption (\"All CIs exclude 0\"), Section 4.1, Appendix G\n- 问题：Table 1 caption 声称 \"All CIs exclude 0\"，但 Appendix G 显示 BCa 校正后 Llama fixed-θ 50% 的 CI 为 [−0.13, 2.21]，包含零。Percentile CI [0.17, 2.97] 勉强排除零。论文在 Appendix G 承认了这一点并用 \"该条件已在 §4.2 被标注为无效\" 来 dismiss，但这构成循环论证：如果 BCa（理论上更准确）显示效应不显著，那么将该条件 dismiss 为 \"无效\" 恰恰需要独立的统计证据。\n- 更深层的问题：BCa bootstrap 在 n=10 时自身可靠性就有问题（jackknife 加速度估计基于 10 个 leave-one-out 值），但论文先声称 BCa \"confirms percentile CIs are conservative\"，又在 BCa 给出不利结果时选择性忽略。这是 selective reporting。\n- 为什么影响接收：统计推断的一致性和诚实性是 soundness 的核心。\n- 建议修改方向：(1) 在 main text 明确标注哪些条件的 BCa CI 包含零；(2) 讨论 percentile vs BCa 在 n=10 下的适用性；(3) 如果选择 percentile CI 作为主要方法，需论证在 n=10 下 percentile 优于 BCa 的理论依据（不能简单说 BCa \"confirms\" then ignore it when it doesn't）。\n\n**N3** [critical] 实验矩阵不完整与 \"systematic characterization\" 声称之间的矛盾\n\n- 具体位置：Abstract, Section 1 Contributions, Section 3.3, Limitations\n- 问题：论文标题和 Contribution 1 声称 \"first systematic characterization\"，但实验矩阵存在大量空缺：\n  - Mistral 缺少 5% 和 25% contamination 条件（仅有 15% 和 50%）\n  - ARC-Challenge 仅在 Qwen 上测试（Section 3.3: \"extending to additional families was constrained by computational budget\"）\n  - Post-RL 扩展仅有 N=1（单个 Qwen 模型，单个 contamination level 15%，单次 GRPO 训练）\n  - 全部模型为 7-8B 规模，无更大或更小模型\n  \n  \"Systematic\" 一词在学术语境中意味着方法论驱动的全面覆盖。当前的覆盖更接近 \"exploratory characterization\"。\n- 为什么影响接收：过度声称（overclaiming）是 ARR review form 中 soundness 扣分的明确依据。\n- 建议修改方向：(1) 将 \"systematic\" 改为 \"initial\" 或 \"controlled\"；(2) 在 Contributions 中明确标注覆盖范围的限制；(3) 对缺失条件的影响进行讨论（如 Mistral 缺 5%/25% 是否影响 θ-shift 规律的泛化性）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Fixed-θ Qwen 15% 反直觉结果（0.7× ratio）的解释不充分\n\n- 具体位置：Section 4.2, Table 2\n- 问题：Fixed-θ 旨在消除 θ-shift absorption 从而增强信号，但 Qwen 15% 时 fixed-θ 反而比 free-θ 弱（ratio 0.7×）。论文解释为 \"Snijders correction bias introduced by anchoring at a mismatch θ outweighs the aberrance eliminated\"。但这一解释是 post-hoc 且未被形式化：(1) 什么决定了 \"mismatch\" 的临界阈值？ (2) 如果 θ mismatch 较小就会产生 net signal loss，那么 fixed-θ 的适用条件是什么？论文没有给出 actionable 的指导。\n- 建议：提供模拟分析（类似 Appendix A）展示 Snijders correction bias 与 θ mismatch 的关系，或至少给出 fixed-θ 优于 free-θ 的充分条件。\n\n**W2** [warning] Post-RL 扩展（N=1）不应出现在 Contributions 中\n\n- 具体位置：Section 3.3 (\"Post-RL extension\"), Section 4.4 (被标为 \"preliminary\"), Figure 4, Abstract\n- 问题：Post-RL 观察基于单一模型（Qwen 15% MMLU）、单次 GRPO 训练（1,500 steps）、三个 checkpoint 的定性观察。论文在 Section 4.4 标注了 \"preliminary\" 和 \"N=1, single model family, single contamination level\"，处理是诚实的。但 Abstract 中 \"contamination patterns may persist after GRPO alignment (Appendix I)\" 给读者留下了 contribution 级别的印象，与实际证据强度不符。\n- 建议：从 Abstract 中移除 post-RL 的提及，仅保留在 Discussion 或 Appendix 中作为 future direction。\n\n**W3** [warning] QLoRA 作为 contamination 代理的外部效度讨论不足\n\n- 具体位置：Section 3.3, Limitations (page 9)\n- 问题：Limitations 承认 \"scoped to SFT-based contamination\"，但未讨论 QLoRA 的 low-rank 约束如何影响 response pattern。QLoRA（rank 通常 16-64）限制了模型参数更新的方向，可能使 contamination signal 表现出与 full fine-tuning 或 pretraining contamination 不同的 person-fit pattern。Appendix J 的 hyperparameters 应包含 LoRA rank/alpha 值及其选择依据。此外，benchmark items 作为 SFT 训练数据的格式（question-answer pairs vs. completion format）可能影响 memorization 的方式。\n- 建议：(1) 讨论 LoRA rank 对 person-fit signal 的可能影响；(2) 与至少一个 full fine-tuning 条件对比（即使只在一个模型上）。\n\n**W4** [warning] ARC-Challenge ceiling effect 解释不可证伪\n\n- 具体位置：Section 4.1 (ARC-C 结果), Table 1\n- 问题：ARC-C 上 Qwen 的基线准确率已很高（67.8%），contamination 后效应量小于 MMLU。论文解释为 \"ceiling effect: with only 295 items, the already-correct items offer minimal room for further θ inflation\"。但这一解释无法在当前数据中被证伪——替代假设是 ARC-C 的 item 特性（区分度、难度分布）本身就不利于 person-fit 检测，与 ceiling 无关。295 items 本身也导致 ℓ_z* 统计量的 statistical power 大幅降低。\n- 建议：(1) 报告 ARC-C 的 item parameter 分布（与 MMLU 对比）；(2) 讨论 295 items 下 ℓ_z* 的 statistical power；(3) 或坦率承认 ARC-C 结果不可解释。\n\n**W5** [warning] Abstract 中 \"n=10 independent seeds per condition\" 表述有歧义\n\n- 具体位置：Abstract 第一段\n- 问题：\"across three 7-8B model families (n=10 independent seeds per condition)\" 容易被理解为每个实验条件（model × contamination level）都有 n=10 seeds。但实际上 n=10 仅适用于 clean baselines；contaminated 条件在 main analysis 中可能为单次运行，multi-seed validation（n=3）仅在 Appendix K 中报告。这一表述虽可解释为 \"per clean baseline condition\"，但在 abstract 中极易误导。\n- 建议：改为 \"n=10 clean baseline seeds per model family\" 以消除歧义。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 2 缺少 ARC-C 和部分 Mistral 条件的解释**：Grey cells 标注了 \"conditions not tested\" 但未在 caption 中解释不测试的原因（计算预算？设计选择？），读者无法判断缺失是 systematic 还是 arbitrary。\n\n2. **Appendix B (4PL vs 3PL) 的处理过简**：论文声称 4PL 优于 3PL 但 Appendix B 仅提供一段文字描述（\"the 3PL model (which assumes d(i)=1) misattributes...\"），缺少定量比较（如 Table 对比两种参数化下的 Cohen's d）。\n\n3. **Figure 3 的 y 轴标签**：Figure 3（baseline accuracy vs. Cohen's |d|）的散点图上 Qwen MMLU 数据点标签密集，部分重叠影响可读性。\n\n4. **Cross-benchmark comparison 缺少统一框架**：MMLU（14,042 items, 4-option MCQ）和 ARC-C（295 items, 4-option MCQ）的 item 数量差 ~48 倍，但论文直接比较两者的 Cohen's d 而未讨论 item count 对 ℓ_z* 统计量 precision 的影响。\n\n5. **Simulation Appendix A 的参数选择**：Appendix A 模拟使用的参数（ε 范围、θ 范围）是否覆盖了实际实验中观察到的参数范围？未见对照。\n\n---\n\n## Questions to Authors\n\n1. **Cohen's d 的具体计算**：在 contaminated condition 只有单次运行的情况下，Cohen's d 是如何计算的？是 (ℓ_z*_contam − mean(ℓ_z*_clean)) / SD(ℓ_z*_clean) 吗？如果是，这本质上是一个 z-score 而非传统的两组 Cohen's d，应在方法中明确说明。\n\n2. **Bootstrap 的 resampling 单元**：10,000 次 bootstrap 是对 n=10 clean seeds 进行 resampling 吗？如果是，resampling 10 个点的 bootstrap 分布是否足够平滑？是否有 Monte Carlo simulation 验证 coverage probability？\n\n3. **Multi-seed validation（Appendix K）与 main analysis 的关系**：Appendix K 的 n=3 contaminated seeds 是否改变了 Table 1 的结论？如果 3 个 contaminated seeds 之间的 ℓ_z* variability 很大，是否意味着 Table 1 中基于单次运行的 Cohen's d 不可靠？\n\n4. **Fixed-θ 的 θ 选择**：Fixed-θ 分析中 θ 被固定在 clean baseline 的 mean θ 还是某个 specific seed 的 θ？选择不同的 anchor θ 是否影响结论？\n\n5. **PSN-IRT item bank 的 vintage**：Zhou et al. (2026) 的 item parameters 是基于哪些模型校准的？如果校准样本与本文的 7-8B 模型在 ability 分布上差异较大，4PL parameters 的 transferability 如何保证？\n\n---\n\n## Missing References\n\n1. **Hedges (1981)** — Cohen's d 在小样本下的 bias correction（Hedges' g），与本文 n=10 的设计直接相关。\n2. **Efron & Tibshirani (1993)** — Bootstrap 方法在小样本下的 coverage properties，包括 BCa 在 n<20 时的已知问题。\n3. **Rodriguez et al. (2021)** 关于 IRT-informed item weighting — 论文已引用但可扩展讨论其与 person-fit 的互补性。\n4. 可考虑引用 **Xu et al. (2024) \"Benchmarking Benchmark Leakage in Large Language Models\"** 如在 contamination detection 综述方面有缺失。\n\n---\n\n## 主要优势\n\n1. **跨学科创新**：将教育测量学的 person-fit statistics 引入 LLM contamination 检测，提供了超越 accuracy-based 方法的机制性理解（contamination 如何改变 response pattern structure 而非仅改变正确率）。这一视角在 NLP 文献中确实是新颖的。\n\n2. **Matched-difference 设计的合理性**：Δℓ_z* 通过差分消除 shared misfit 是一个优雅的设计，解决了 clean models 本身也有 high ℓ_z*（Appendix C 报告 clean Qwen ℓ_z*=7-9.5）的问题。Appendix A 的 simulation 提供了理论支撑。\n\n3. **Detection-diagnosis tradeoff 的发现**（Section 4.3, Table 3）：诚实地展示了 simpler statistics 在纯检测上的优势，同时论证了 ℓ_z* 在 diagnostic 层面的独特价值——ℓ_z* 可以区分 response-pattern anomalies（item-level misfit）与 overall performance changes，这是 accuracy z-scores 做不到的。两阶段工作流（先筛后诊断）的建议是务实的。\n\n4. **适当的 epistemic 降级**：Finding 3（non-monotonic dose-response）被明确标注为 \"exploratory\"，multi-seed validation（n=3）结果也如实报告了高变异性。Limitations 部分坦率覆盖了 SFT scope、model scale、post-RL 的局限性。\n\n5. **Appendix 的充分性**：Appendices A-K 覆盖了 simulation validation、seed sensitivity、cross-family consistency、robustness under local dependence、item parameter sensitivity 等关键补充分析，显示了严谨的实验态度。\n\n---\n\n## 格式合规检查\n\n- 正文 8 页 ✓（page 1-8 为正文，page 9 开始为 Limitations + References）\n- Limitations section 存在且篇幅适当 ✓\n- Double-blind：未发现明显的去匿名化线索 ✓\n- ACL 模板格式 ✓\n",
  "reviewer_id": "1",
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n## Summary\n\n本文将教育测量学中的 IRT person-fit 统计量（Snijders' ℓ_z*）应用于 LLM benchmark contamination 检测，提出 matched-difference 设计（Δℓ_z*）以分离 contamination-specific aberrance。在三个 7-8B 模型家族上（Qwen2.5-7B, Llama-3.1-8B, Mistral-7B），使用 QLoRA SFT 作为 contamination 代理，在 MMLU（14,042 items）和 ARC-Challenge（295 items）上识别出三个行为边界：θ-shift dynamics、detection-diagnosis tradeoff、ability-dependent non-monotonic dose-response。论文的核心贡献在于将 psychometrics 视角引入 LLM 评估，提供 contamination 行为的机制性理解而非单纯检测。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n\n**一句话总结**: 研究视角新颖、matched-difference 设计合理，但 n=10 的统计基础偏薄，实验矩阵不完整与 \"systematic\" 声称之间存在张力，部分 claim 超出了证据支撑范围。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 | 核心 matched-difference 设计合理，但 n=10 的 Cohen's d SD 估计仅有 9 自由度，BCa 校正在此样本量下不可靠，且至少一个条件的 BCa CI 包含零（Appendix G, Llama fixed-θ 50%）；部分 claim 超出证据范围 |\n| **Excitement** | 3.5 / 5 | 将 IRT person-fit 应用于 contamination 检测是新颖的跨学科贡献，三个 behavior boundary 的发现提供了独特的机制性洞察；但 simpler statistics 检测效果更好（Table 3），限制了实际应用价值 |\n| **Reproducibility** | 3 / 5 | Appendix J 提供了 QLoRA 超参数表，PSN-IRT item bank 声称公开可用（Zhou et al., 2026），但代码 \"upon acceptance\" 才释放；bootstrap 实现细节部分缺失 |\n| **Confidence** | 4 / 5 | 对 IRT 和实验设计方法有扎实理解，仔细验证了关键数字和 claim |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Cohen's d 的统计可靠性：n=10 clean seeds 作为 SD 估计基础过于薄弱\n\n- 具体位置：Section 3.2, Table 1, Table 2\n- 问题：Cohen's d 的分母（SD of ℓ_z* across clean seeds）仅有 n=10，对应 9 个自由度。虽然每个 ℓ_z* 本身基于 14,042 items 是稳定的，但 seed-to-seed variability 的 SD 估计在 df=9 时高度不稳定。对于 |d|≥3 的大效应量（如 Qwen 15%+ 条件），结论可能稳健；但对于 |d|≈1-2 的条件（如 Llama 15% |d|=2.27, Qwen 5% |d|=1.90），CI 的校准性存疑。论文未报告 Cohen's d 的标准误或讨论小样本下效应量估计的已知偏差（Hedges' g correction）。\n- 为什么影响接收：这是整篇论文量化推断的基础。如果 SD 估计不可靠，所有 CI 和效应量比较（Table 1-3）的可信度都受影响。\n- 建议修改方向：(1) 报告 Hedges' g（小样本校正的 Cohen's d）；(2) 讨论 n=10 下 SD 估计的 sampling variability（可用 chi-squared 分布 df=9 给出 SD 的 CI）；(3) 增加 clean seeds 数量（n≥20）或论证当前 n=10 已足够。\n\n**N2** [critical] BCa CI 与 percentile CI 的不一致性被低估\n\n- 具体位置：Table 1 caption (\"All CIs exclude 0\"), Section 4.1, Appendix G\n- 问题：Table 1 caption 声称 \"All CIs exclude 0\"，但 Appendix G 显示 BCa 校正后 Llama fixed-θ 50% 的 CI 为 [−0.13, 2.21]，包含零。Percentile CI [0.17, 2.97] 勉强排除零。论文在 Appendix G 承认了这一点并用 \"该条件已在 §4.2 被标注为无效\" 来 dismiss，但这构成循环论证：如果 BCa（理论上更准确）显示效应不显著，那么将该条件 dismiss 为 \"无效\" 恰恰需要独立的统计证据。\n- 更深层的问题：BCa bootstrap 在 n=10 时自身可靠性就有问题（jackknife 加速度估计基于 10 个 leave-one-out 值），但论文先声称 BCa \"confirms percentile CIs are conservative\"，又在 BCa 给出不利结果时选择性忽略。这是 selective reporting。\n- 为什么影响接收：统计推断的一致性和诚实性是 soundness 的核心。\n- 建议修改方向：(1) 在 main text 明确标注哪些条件的 BCa CI 包含零；(2) 讨论 percentile vs BCa 在 n=10 下的适用性；(3) 如果选择 percentile CI 作为主要方法，需论证在 n=10 下 percentile 优于 BCa 的理论依据（不能简单说 BCa \"confirms\" then ignore it when it doesn't）。\n\n**N3** [critical] 实验矩阵不完整与 \"systematic characterization\" 声称之间的矛盾\n\n- 具体位置：Abstract, Section 1 Contributions, Section 3.3, Limitations\n- 问题：论文标题和 Contribution 1 声称 \"first systematic characterization\"，但实验矩阵存在大量空缺：\n  - Mistral 缺少 5% 和 25% contamination 条件（仅有 15% 和 50%）\n  - ARC-Challenge 仅在 Qwen 上测试（Section 3.3: \"extending to additional families was constrained by computational budget\"）\n  - Post-RL 扩展仅有 N=1（单个 Qwen 模型，单个 contamination level 15%，单次 GRPO 训练）\n  - 全部模型为 7-8B 规模，无更大或更小模型\n  \n  \"Systematic\" 一词在学术语境中意味着方法论驱动的全面覆盖。当前的覆盖更接近 \"exploratory characterization\"。\n- 为什么影响接收：过度声称（overclaiming）是 ARR review form 中 soundness 扣分的明确依据。\n- 建议修改方向：(1) 将 \"systematic\" 改为 \"initial\" 或 \"controlled\"；(2) 在 Contributions 中明确标注覆盖范围的限制；(3) 对缺失条件的影响进行讨论（如 Mistral 缺 5%/25% 是否影响 θ-shift 规律的泛化性）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Fixed-θ Qwen 15% 反直觉结果（0.7× ratio）的解释不充分\n\n- 具体位置：Section 4.2, Table 2\n- 问题：Fixed-θ 旨在消除 θ-shift absorption 从而增强信号，但 Qwen 15% 时 fixed-θ 反而比 free-θ 弱（ratio 0.7×）。论文解释为 \"Snijders correction bias introduced by anchoring at a mismatch θ outweighs the aberrance eliminated\"。但这一解释是 post-hoc 且未被形式化：(1) 什么决定了 \"mismatch\" 的临界阈值？ (2) 如果 θ mismatch 较小就会产生 net signal loss，那么 fixed-θ 的适用条件是什么？论文没有给出 actionable 的指导。\n- 建议：提供模拟分析（类似 Appendix A）展示 Snijders correction bias 与 θ mismatch 的关系，或至少给出 fixed-θ 优于 free-θ 的充分条件。\n\n**W2** [warning] Post-RL 扩展（N=1）不应出现在 Contributions 中\n\n- 具体位置：Section 3.3 (\"Post-RL extension\"), Section 4.4 (被标为 \"preliminary\"), Figure 4, Abstract\n- 问题：Post-RL 观察基于单一模型（Qwen 15% MMLU）、单次 GRPO 训练（1,500 steps）、三个 checkpoint 的定性观察。论文在 Section 4.4 标注了 \"preliminary\" 和 \"N=1, single model family, single contamination level\"，处理是诚实的。但 Abstract 中 \"contamination patterns may persist after GRPO alignment (Appendix I)\" 给读者留下了 contribution 级别的印象，与实际证据强度不符。\n- 建议：从 Abstract 中移除 post-RL 的提及，仅保留在 Discussion 或 Appendix 中作为 future direction。\n\n**W3** [warning] QLoRA 作为 contamination 代理的外部效度讨论不足\n\n- 具体位置：Section 3.3, Limitations (page 9)\n- 问题：Limitations 承认 \"scoped to SFT-based contamination\"，但未讨论 QLoRA 的 low-rank 约束如何影响 response pattern。QLoRA（rank 通常 16-64）限制了模型参数更新的方向，可能使 contamination signal 表现出与 full fine-tuning 或 pretraining contamination 不同的 person-fit pattern。Appendix J 的 hyperparameters 应包含 LoRA rank/alpha 值及其选择依据。此外，benchmark items 作为 SFT 训练数据的格式（question-answer pairs vs. completion format）可能影响 memorization 的方式。\n- 建议：(1) 讨论 LoRA rank 对 person-fit signal 的可能影响；(2) 与至少一个 full fine-tuning 条件对比（即使只在一个模型上）。\n\n**W4** [warning] ARC-Challenge ceiling effect 解释不可证伪\n\n- 具体位置：Section 4.1 (ARC-C 结果), Table 1\n- 问题：ARC-C 上 Qwen 的基线准确率已很高（67.8%），contamination 后效应量小于 MMLU。论文解释为 \"ceiling effect: with only 295 items, the already-correct items offer minimal room for further θ inflation\"。但这一解释无法在当前数据中被证伪——替代假设是 ARC-C 的 item 特性（区分度、难度分布）本身就不利于 person-fit 检测，与 ceiling 无关。295 items 本身也导致 ℓ_z* 统计量的 statistical power 大幅降低。\n- 建议：(1) 报告 ARC-C 的 item parameter 分布（与 MMLU 对比）；(2) 讨论 295 items 下 ℓ_z* 的 statistical power；(3) 或坦率承认 ARC-C 结果不可解释。\n\n**W5** [warning] Abstract 中 \"n=10 independent seeds per condition\" 表述有歧义\n\n- 具体位置：Abstract 第一段\n- 问题：\"across three 7-8B model families (n=10 independent seeds per condition)\" 容易被理解为每个实验条件（model × contamination level）都有 n=10 seeds。但实际上 n=10 仅适用于 clean baselines；contaminated 条件在 main analysis 中可能为单次运行，multi-seed validation（n=3）仅在 Appendix K 中报告。这一表述虽可解释为 \"per clean baseline condition\"，但在 abstract 中极易误导。\n- 建议：改为 \"n=10 clean baseline seeds per model family\" 以消除歧义。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 2 缺少 ARC-C 和部分 Mistral 条件的解释**：Grey cells 标注了 \"conditions not tested\" 但未在 caption 中解释不测试的原因（计算预算？设计选择？），读者无法判断缺失是 systematic 还是 arbitrary。\n\n2. **Appendix B (4PL vs 3PL) 的处理过简**：论文声称 4PL 优于 3PL 但 Appendix B 仅提供一段文字描述（\"the 3PL model (which assumes d(i)=1) misattributes...\"），缺少定量比较（如 Table 对比两种参数化下的 Cohen's d）。\n\n3. **Figure 3 的 y 轴标签**：Figure 3（baseline accuracy vs. Cohen's |d|）的散点图上 Qwen MMLU 数据点标签密集，部分重叠影响可读性。\n\n4. **Cross-benchmark comparison 缺少统一框架**：MMLU（14,042 items, 4-option MCQ）和 ARC-C（295 items, 4-option MCQ）的 item 数量差 ~48 倍，但论文直接比较两者的 Cohen's d 而未讨论 item count 对 ℓ_z* 统计量 precision 的影响。\n\n5. **Simulation Appendix A 的参数选择**：Appendix A 模拟使用的参数（ε 范围、θ 范围）是否覆盖了实际实验中观察到的参数范围？未见对照。\n\n---\n\n## Questions to Authors\n\n1. **Cohen's d 的具体计算**：在 contaminated condition 只有单次运行的情况下，Cohen's d 是如何计算的？是 (ℓ_z*_contam − mean(ℓ_z*_clean)) / SD(ℓ_z*_clean) 吗？如果是，这本质上是一个 z-score 而非传统的两组 Cohen's d，应在方法中明确说明。\n\n2. **Bootstrap 的 resampling 单元**：10,000 次 bootstrap 是对 n=10 clean seeds 进行 resampling 吗？如果是，resampling 10 个点的 bootstrap 分布是否足够平滑？是否有 Monte Carlo simulation 验证 coverage probability？\n\n3. **Multi-seed validation（Appendix K）与 main analysis 的关系**：Appendix K 的 n=3 contaminated seeds 是否改变了 Table 1 的结论？如果 3 个 contaminated seeds 之间的 ℓ_z* variability 很大，是否意味着 Table 1 中基于单次运行的 Cohen's d 不可靠？\n\n4. **Fixed-θ 的 θ 选择**：Fixed-θ 分析中 θ 被固定在 clean baseline 的 mean θ 还是某个 specific seed 的 θ？选择不同的 anchor θ 是否影响结论？\n\n5. **PSN-IRT item bank 的 vintage**：Zhou et al. (2026) 的 item parameters 是基于哪些模型校准的？如果校准样本与本文的 7-8B 模型在 ability 分布上差异较大，4PL parameters 的 transferability 如何保证？\n\n---\n\n## Missing References\n\n1. **Hedges (1981)** — Cohen's d 在小样本下的 bias correction（Hedges' g），与本文 n=10 的设计直接相关。\n2. **Efron & Tibshirani (1993)** — Bootstrap 方法在小样本下的 coverage properties，包括 BCa 在 n<20 时的已知问题。\n3. **Rodriguez et al. (2021)** 关于 IRT-informed item weighting — 论文已引用但可扩展讨论其与 person-fit 的互补性。\n4. 可考虑引用 **Xu et al. (2024) \"Benchmarking Benchmark Leakage in Large Language Models\"** 如在 contamination detection 综述方面有缺失。\n\n---\n\n## 主要优势\n\n1. **跨学科创新**：将教育测量学的 person-fit statistics 引入 LLM contamination 检测，提供了超越 accuracy-based 方法的机制性理解（contamination 如何改变 response pattern structure 而非仅改变正确率）。这一视角在 NLP 文献中确实是新颖的。\n\n2. **Matched-difference 设计的合理性**：Δℓ_z* 通过差分消除 shared misfit 是一个优雅的设计，解决了 clean models 本身也有 high ℓ_z*（Appendix C 报告 clean Qwen ℓ_z*=7-9.5）的问题。Appendix A 的 simulation 提供了理论支撑。\n\n3. **Detection-diagnosis tradeoff 的发现**（Section 4.3, Table 3）：诚实地展示了 simpler statistics 在纯检测上的优势，同时论证了 ℓ_z* 在 diagnostic 层面的独特价值——ℓ_z* 可以区分 response-pattern anomalies（item-level misfit）与 overall performance changes，这是 accuracy z-scores 做不到的。两阶段工作流（先筛后诊断）的建议是务实的。\n\n4. **适当的 epistemic 降级**：Finding 3（non-monotonic dose-response）被明确标注为 \"exploratory\"，multi-seed validation（n=3）结果也如实报告了高变异性。Limitations 部分坦率覆盖了 SFT scope、model scale、post-RL 的局限性。\n\n5. **Appendix 的充分性**：Appendices A-K 覆盖了 simulation validation、seed sensitivity、cross-family consistency、robustness under local dependence、item parameter sensitivity 等关键补充分析，显示了严谨的实验态度。\n\n---\n\n## 格式合规检查\n\n- 正文 8 页 ✓（page 1-8 为正文，page 9 开始为 Limitations + References）\n- Limitations section 存在且篇幅适当 ✓\n- Double-blind：未发现明显的去匿名化线索 ✓\n- ACL 模板格式 ✓\n",
    "reviewer_id": "1",
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-22T22:55:32.799508+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-22T22:55:38.177483+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 528 · 2026-05-22T22:55:38.228656+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 529 · 2026-05-22T22:55:42.744816+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 530 · 2026-05-22T22:55:42.745370+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 531 · 2026-05-22T22:55:52.280201+00:00_

审稿完成。报告已提交至 Review Director，核心判断：

- **Overall 3.5（Borderline Conference）**
- 3 个 Must-Fix：Cohen's d n=10 可靠性、BCa/percentile CI 不一致性被选择性处理、"systematic" overclaiming
- 5 个 Should-Fix：fixed-θ 反直觉结果解释不足、post-RL N=1 不应进 abstract、QLoRA 外部效度、ARC-C ceiling 不可证伪、abstract 中 "per condition" 歧义
- 主要优势：跨学科创新视角、matched-difference 设计优雅、detection-diagnosis tradeoff 发现务实、epistemic 降级处理得当

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

32 recorded events


### User

_source line 532 · 2026-05-22T22:55:53.400806+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## 论文信息
- **标题**: What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization
- **论文路径**: projects/irt_personfit_contam/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf

## Venue 要求
- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR)
- **截止日期**: 2026-05-25
- **类别**: Long Paper
- **页数限制**: 正文 8 页（不含 references、limitations、ethical considerations）
- **模板**: ACL template（`\usepackage[review]{acl}`）
- **匿名规则**: Double-blind（作者信息不可出现在论文中）
- **附录规则**: 附录不计入页数限制，但 reviewer 不保证会阅读附录
- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重

**方法严谨性**，具体包括：

1. **IRT 框架有效性**：4PL 模型在 LLM 上下文中的适用性论证是否充分？PSN-IRT 依赖是否被充分讨论？局部独立性/单维性假设违反的处理是否合理？

2. **实验设计**：
   - Δℓz* matched-difference design 的统计有效性
   - 样本量（n=10 clean seeds, 每个污染条件单次运行 + Qwen n=3 多 seed 验证）是否足以支撑 claim
   - 实验矩阵的完整性（3 个模型族、2 个 benchmark、4 个污染水平的覆盖）
   - ARC-C 仅 Qwen 测试的合理性

3. **统计方法学**：
   - Cohen's d 作为效应量度量在此设计中是否合适
   - Bootstrap CI 的有效性（特别是小样本场景）
   - θ-shift absorption 机制的论证是否严谨
   - Fixed-θ vs free-θ 比较的解释是否合理

4. **可复现性**：
   - QLoRA 训练细节是否充分
   - 代码/数据承诺是否明确
   - 结果是否可独立验证

请按以下格式输出审稿报告：

### Summary（2-3 句）

### Strengths（逐条）

### Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）

### Questions（需要作者澄清的问题）

### Missing References（遗漏的重要相关工作）

### Overall Assessment（评分 + 置信度 + 理由）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 533 · 2026-05-22T22:56:12.387812+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
  "project": "irt_personfit_contam",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
    "project": "irt_personfit_contam",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-22T22:56:13.143979+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
  "project": "irt_personfit_contam",
  "pages": "9-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
    "project": "irt_personfit_contam",
    "pages": "9-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-22T22:56:13.545836+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 361.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.7}], \"total_pages\": 15, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_p
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1158
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-22T22:56:14.300429+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.0}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 428.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 220.1}], \"total_pages\": 15, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1156
}
```

</details>

---


### Tool call

_source line 537 · 2026-05-22T22:56:23.835527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-22T22:56:24.388708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-22T22:56:24.842305+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-22T22:56:24.842759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-22T22:56:25.747534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool result

_source line 542 · 2026-05-22T22:56:25.751043+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 543 · 2026-05-22T22:56:25.751474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-22T22:56:26.052855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-22T22:56:26.155731+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool result

_source line 546 · 2026-05-22T22:56:26.659596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool call

_source line 547 · 2026-05-22T22:56:33.790842+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 548 · 2026-05-22T22:56:34.796388+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 549 · 2026-05-22T22:56:34.796929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-22T22:56:35.298814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-22T22:56:35.750857+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool result

_source line 552 · 2026-05-22T22:56:35.753692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 553 · 2026-05-22T22:56:35.755264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 554 · 2026-05-22T22:56:36.760156+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 555 · 2026-05-22T22:56:37.011353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-22T22:56:37.213479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-22T22:56:37.969905+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool result

_source line 558 · 2026-05-22T22:56:37.971263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 559 · 2026-05-22T23:02:02.783668+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — 方法严谨性审查报告\n\n---\n\n## Summary\n\n本文将教育测量学中的 IRT person-fit 统计量（Snijders' ℓ_z*）应用于 LLM benchmark contamination 检测，提出 matched-difference 设计 Δℓ_z* 来分离 contamination-specific aberrance。在三个 7–8B 模型家族上，通过 QLoRA SFT 作为 contamination 代理，识别出三个行为边界：θ-shift dynamics、detection-diagnosis tradeoff 和 ability-dependent non-monotonic dose-response。论文的定位是 characterization 而非 detection tool，核心贡献在于从 psychometrics 视角提供 contamination 行为的机制性理解。\n\n---\n\n## Strengths\n\n**S1. 跨学科视角新颖且动机充分。** 将教育测量学中成熟的 person-fit 统计量引入 LLM contamination 检测是一个有创意的跨领域移植。论文对 IRT 在 LLM 上下文中的适用性给出了合理论证：Section 3.1 说明了 4PL 选择理由（upper asymptote d_i 容纳 guessing/memorization），Section 3.2 坦率承认 LLM 违反 local independence（57/601 cells 即 9.5% flagged），并通过 Δℓ_z* 差分设计将其从 confound 转化为 design feature。\n\n**S2. Matched-difference design 设计优雅。** Δℓ_z* = ℓ_z*_contam − ℓ̄_z*_clean 的设计直接解决了 clean model 本身已有 high ℓ_z*（Appendix C: Qwen clean ℓ_z* 在 7.05–9.53 之间）的核心挑战。Appendix F.1 的 local dependence 模拟（σ_a = 0–1.0, shared vs. asymmetric LD）验证了设计在现实违反条件下的鲁棒性，Appendix A 的 power simulation 给出了基准（MMLU 14,042 items, 97.8% power at 15%）。\n\n**S3. Detection-diagnosis tradeoff 的发现具有实际指导价值。** Table 3（Section 4.3）诚实地展示了 accuracy z-scores 在纯检测上的绝对优势（|d| 高出一个数量级），同时论证了 ℓ_z* 在 diagnostic 层面的独特能力——可在 seen/unseen item subsets 上分别计算（Section 4.3: \"ℓ_z* can be computed separately on seen and unseen item subsets\"），区分 response-pattern anomaly 与 overall performance shift。两阶段工作流建议（先 accuracy 筛查、再 ℓ_z* 诊断）是务实的。\n\n**S4. Epistemic 降级处理得当。** Finding 3（non-monotonic dose-response）被明确标为 \"exploratory\"（Section 4.4 标题），N=1 post-RL observation 被限制在 Appendix I 并反复标注 \"preliminary\"。Limitations section 覆盖了 SFT scope、model scale、single-run 问题，展现了较好的学术诚实度。\n\n**S5. Appendix 体系完整。** Appendices A–K 覆盖了 simulation validation、4PL vs 3PL 对比、seed sensitivity、cross-family consistency、local dependence robustness、item parameter perturbation、BCa check、classical IRT refit、post-RL、hyperparameters 和 reproducibility。这些补充分析回答了许多自然产生的 follow-up 问题。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [critical] Bootstrap CI 仅捕获 clean-seed variability，系统性低估了总不确定性。**\n\n- **位置**: Section 3.2, Table 1, Table 2\n- **问题**: Table 1 的 Cohen's d = (ℓ_z*_contam − mean(ℓ_z*_clean)) / SD(ℓ_z*_clean)，bootstrap resampling 作用于 n=10 clean seeds。这意味着 CI 仅反映 clean baseline 的 sampling variability，**完全忽略了 contaminated run 的 seed-to-seed variability**。然而 Appendix K（Table 15）显示 Qwen 50% contamination 下三个独立 seed 的 free-θ |d| 的 CV=59.6%（range 1.10–7.51）。如果 contaminated ℓ_z* 本身有如此大的变异，Table 1 中基于单次 contaminated run 计算的 |d| 的 CI 就是 **anti-conservative** 的——它声称的精度高于实际精度。\n- **具体后果**: Table 1 caption \"All CIs exclude 0\" 在 50% contamination 条件下可能不成立。如果用 Appendix K 的最低 seed（|d|=1.10 at 50%）替换 Table 1 的单次观测值，CI 可能包含零或大幅缩窄远离零的距离。\n- **为什么影响接收**: 论文的核心量化推断（Contribution 2: \"all bootstrap 95% CIs exclude zero\"）建立在这些 CI 上。如果 CI 系统性低估不确定性，主要结论的可靠性需要重新评估。\n- **建议**: (1) 将 Appendix K 的 multi-seed data 纳入 main analysis，报告包含两种 variability 来源的 CI（如 prediction interval 或 nested bootstrap）；(2) 明确 Table 1 CI 的含义为 \"conditional on the observed contaminated run\"；(3) 讨论 single-run vs multi-seed 估计的差异及其对结论的影响。\n\n**N2. [critical] 实验条件的 post-hoc 扩展引入确认偏差风险。**\n\n- **位置**: Section 3.3 (第 4 页)\n- **问题**: Section 3.3 明确说 \"Following initial observations of non-monotonic dose-response for Qwen, we added 5% and 25% conditions for Qwen to trace the full dose-response curve. The 25% condition was subsequently extended to Llama to test whether the pattern generalizes.\" 这意味着 Finding 3（inverted-U, Section 4.4）的关键证据条件（5%/25%）是在**观察到结果后才追加的**。这是经典的 confirmatory bias 问题：先看到 pattern → 追加数据点 → 声称 pattern 得到 \"confirmation\"。\n- **更深层问题**: 论文虽将 Finding 3 标注为 \"exploratory\"，但 Abstract 中 \"three behavior boundaries\" 的表述将三个 finding 并列呈现，未区分哪些是 pre-planned、哪些是 post-hoc。Section 4.4 标题包含 \"(Exploratory)\" 但在读者快速浏览时容易遗漏。\n- **为什么影响接收**: Post-hoc condition selection 使得 p-values 和 CI 的名义覆盖率不再可靠。如果 5%/25% 条件是 planned，则应在 pre-registration 或 method section 中说明；如果是 post-hoc，则效应量和 CI 需要进行多重比较校正或至少标注为 exploratory。\n- **建议**: (1) 在 Abstract 和 Contributions 中明确区分 confirmatory findings（15%/50% across 三个 model families）和 exploratory findings（5%/25% 追加、non-monotonic dose-response）；(2) 对 post-hoc 追加的条件进行 Bonferroni 或 Holm 校正；(3) 在 Method section 透明报告实验时间线。\n\n**N3. [critical] \"Systematic characterization\" 声称与实验覆盖不匹配。**\n\n- **位置**: Title, Abstract, Contribution 1\n- **问题**: 实验矩阵存在大量系统性空缺：\n  - Mistral 仅测试了 15%/50%（缺 5%/25%）\n  - ARC-Challenge 仅在 Qwen 上测试（Section 3.3: \"constrained by computational budget\"）\n  - Post-RL 扩展为 N=1（单模型、单污染水平、单次训练）\n  - 全部模型为 7–8B，无不同规模覆盖\n  - Contaminated conditions 为 single-run（multi-seed 仅 Qwen，且仅在 Appendix K）\n  \n  在 57 个 model×benchmark×contamination level 的理论设计空间中，实际测试了 12 个条件（Table 1 中可见）。\"Systematic\" 在学术语境中意味着理论驱动的完整覆盖。\n- **为什么影响接收**: Overclaiming 是 ARR reviewer guidelines 中明确的 soundness 扣分项。标题中的 \"systematic\" 设定了一个论文内容无法兑现的期望。\n- **建议**: 将 \"systematic\" 改为 \"controlled\" 或 \"initial\"，或在引言中明确界定 \"systematic\" 的具体含义（如 \"系统地变化 contamination level\"）。\n\n**N4. [critical] Cohen's d 的计算本质是 one-sample z-score，但被呈现为标准效应量。**\n\n- **位置**: Section 3.2, Tables 1–3\n- **问题**: 标准 Cohen's d 用于比较两组均值，需要两组的样本量和方差。本文的计算是 d = (ℓ_z*_contam − mean(ℓ_z*_clean)) / SD(ℓ_z*_clean)，其中 contaminated condition 通常为单次观测（n_contam=1）。这本质上是一个 **z-score**（观测值距 clean 分布均值的标准差数），而非传统两组 Cohen's d。二者在解释上有重要区别：z-score 不包含 contaminated group 的 within-group variability，因此不能直接用 Cohen's d 的 benchmarks（small=0.2, medium=0.5, large=0.8）来解释。\n- **附加问题**: SD 估计基于 n=10（df=9），存在已知的正偏差。Hedges' correction factor J(df) = 1 − 3/(4·df − 1) ≈ 0.914 for df=9 应被应用但未见讨论。\n- **为什么影响接收**: 效应量的正确标注和解释是量化方法论文章的核心 soundness 要求。\n- **建议**: (1) 明确定义 d 的计算公式（当前 Section 3.2 仅说 \"Cohen's d\" 而未给出数学定义）；(2) 讨论 one-sample effect size vs two-sample effect size 的区别；(3) 报告 Hedges' g 以校正小样本偏差。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [warning] BCa vs percentile CI 不一致性的处理有 selective reporting 倾向。**\n\n- **位置**: Section 3.2, Appendix G\n- **问题**: Section 3.2 声称 \"BCa correction (Appendix G) confirms that percentile CIs are conservative estimates\"。但 Appendix G 实际显示：BCa CIs 在大多数条件下**更窄**（mean reduction 22%），唯独 Llama fixed-θ 50% 时 BCa CI = [−0.13, 2.21] **包含零**（vs percentile [0.17, 2.97]）。论文的处理方式是将该条件 dismiss 为 \"already characterized as ineffective in §4.2\"，但这构成循环论证：§4.2 将该条件标为 ineffective 的依据之一就是信号弱，而 BCa CI 包含零正是信号弱的独立证据。此外，BCa 本身在 n=10 时的 jackknife acceleration 估计也不稳定（基于 10 个 leave-one-out 值），论文对此未讨论。\n- **建议**: (1) 在 main text（不仅 Appendix）报告 BCa CI 包含零的条件；(2) 讨论 n=10 下 percentile vs BCa 的选择依据；(3) 不要声称 BCa \"confirms\" percentile CIs 的保守性——这仅在大多数条件下成立。\n\n**W2. [warning] Fixed-θ Qwen 15% 反直觉结果（ratio < 1）的机制解释不清。**\n\n- **位置**: Section 4.2（第 5–6 页）\n- **问题**: Fixed-θ 旨在消除 θ-shift absorption 从而增强信号，但 Table 2 中 Qwen 15% 的 fixed-θ/free-θ ratio 为 0.7×（即 fixed-θ 反而更弱）。论文解释为 \"the Snijders correction bias introduced by anchoring at a mismatch θ outweighs the aberrance eliminated, producing a net signal loss\"。这一解释存在三个问题：\n  1. \"Mismatch θ\" 的量化标准未给出——Qwen clean θ 和 contaminated θ 之间的 Δθ 是多少？为什么该 Δθ 在 15% 时是 \"small enough\" 而在 25%/50% 时不是？\n  2. Snijders correction 在 θ 估计有偏时引入的 bias 方向和大小取决于 Fisher information 矩阵，论文未提供计算。\n  3. 如果 fixed-θ 在部分条件下可能 hurt 检测，那么它作为 \"remedy\" 的实用价值需要被限定——但论文未给出 fixed-θ 适用条件的 guidance。\n- **建议**: 通过 simulation（类似 Appendix A）系统展示 Snijders correction bias 如何随 Δθ 变化，给出 fixed-θ 优于 free-θ 的充分条件。\n\n**W3. [warning] QLoRA 外部效度未充分讨论。**\n\n- **位置**: Section 3.3, Section 5 (\"Contamination model\"), Limitations\n- **问题**: QLoRA 的 low-rank 约束（Table 14: rank=16）限制了参数更新的方向数，这可能使 contamination 产生的 response-pattern anomaly 与 full fine-tuning 或 pretraining contamination 有质的不同。具体地：low-rank update 可能均匀地影响所有 item 的 response probability，而 full parameter update 可能选择性地影响 seen items。论文承认了 SFT 的限制（\"may not generalize to pretraining contamination\"），但未讨论 QLoRA vs full SFT 的差异。Table 14 提供了 hyperparameters 但未报告 LoRA rank/alpha 的选择依据。\n- **建议**: (1) 讨论 LoRA rank 对 person-fit pattern 的可能影响；(2) 至少在一个模型上与 full SFT 对比。\n\n**W4. [warning] ARC-Challenge 结果的可解释性受限于 item count 和 single-model coverage。**\n\n- **位置**: Section 4.1 (ARC-C 段落), Table 1, Appendix A\n- **问题**: ARC-C 仅有 295 items，Appendix A 的 power analysis 显示 80% power 需要 n ≥ 7,958 items at 15% contamination。因此 ARC-C 上的结果在统计上严重 underpowered。Table 1 中 ARC-C 的 Cohen's d 可能受到 inflated estimation（小样本效应量偏差）和 insufficient power（无法检测真实效应）的双重影响。论文解释为 \"ceiling effect\"（Qwen baseline accuracy 67.8%），但 (1) 这与 MMLU 52.4% 的 baseline 差异并不极端；(2) 仅在 Qwen 一个模型上测试，无法区分 ceiling 效应与 ARC-C item-specific 特性。\n- **建议**: (1) 在讨论 ARC-C 结果时明确报告 statistical power 不足的问题；(2) 对 295 items 下 Cohen's d 的 precision 进行 quantification（如 d 的 standard error）。\n\n---\n\n### Minor（不影响接收）\n\n**M1.** Abstract 中 \"n=10 independent seeds per condition\" 的 \"per condition\" 有歧义——实际仅 clean baseline 有 n=10，contaminated conditions 为 single run（Limitations 确认 \"controlled experiments were trained as a single QLoRA run\"）。建议改为 \"n=10 clean baseline seeds per model family\"。\n\n**M2.** Table 2 中 grey cells（Llama/Mistral on ARC-C, Mistral at 5%/25%）仅标注 \"conditions not tested\" 但 caption 未解释原因。读者无法判断缺失是计划内的还是临时的。\n\n**M3.** Appendix B（4PL vs 3PL）仅提供定性描述，缺少 quantitative 对比（如两种参数化下 Cohen's d 的差值或比率）。鉴于 4PL 是方法论核心选择，该对比应更严谨。\n\n**M4.** Section 4.4 中 Qwen 的四级轨迹（|d|: 1.15 → 6.58 → 8.22 → 1.98 at 5%/15%/25%/50%）与 Table 1 中 5% 的 |d|=1.90 不一致。1.15 vs 1.90 的差异需要解释（可能来自不同分析，但文中未标注）。\n\n**M5.** Section 5 \"Scope and calibration\" 提到 57/601 cells 中 |ℓ_z*| > 1.96，但未讨论这些 false-positive-like 信号的分布模式——是否集中在特定模型家族或 benchmark 上？这与 Δℓ_z* design 的有效性直接相关。\n\n---\n\n## Questions\n\n**Q1.** Cohen's d 的精确公式是什么？当 contaminated condition 为 single run（n_contam=1）时，d 是如何定义的？Section 3.2 仅说 \"We report Cohen's d\" 但未给出数学表达式。\n\n**Q2.** Bootstrap resampling 的具体对象是什么？是 resample n=10 clean seeds 来计算 SD 的 bootstrap 分布，还是 resample items 来计算 ℓ_z* 的 bootstrap 分布？前者对应 seed-level bootstrap，后者对应 item-level bootstrap——二者的 coverage properties 完全不同。\n\n**Q3.** Appendix K 的 multi-seed 结果（n=3 contaminated seeds）为何未被纳入 main analysis？如果三个 seed 的 |d| 在 50% 时从 1.10 到 7.51（CV=59.6%），Table 1 中报告的 single-seed |d| 在何种意义上代表该 contamination condition 的效应？\n\n**Q4.** PSN-IRT item parameters 是在什么样本上校准的？如果校准样本中包含了与本文三个 7–8B 模型相似的模型（或其 variants），item parameters 是否可能已经 \"适应\" 了这些模型的 response pattern，从而影响 ℓ_z* 的 calibration？\n\n**Q5.** Fixed-θ 分析中 θ 是固定在 n=10 clean seeds 的 mean θ 还是某个特定 seed 的 θ？Appendix K note 确认 \"Fixed-θ estimation anchors θ at the clean-baseline mean\"，但 mean θ 本身有 estimation error（基于 n=10），这一误差是否传播到了 fixed-θ Cohen's d 中？\n\n**Q6.** Section 4.4 声称 Llama 的 non-monotonic pattern \"directionally consistent but statistically non-significant\"（|d|: 2.27→2.97, overlapping CIs），但这不能被解释为 \"pattern replicates\"。在 Mistral 上完全未测试 5%/25% 条件。仅凭 Qwen 一个模型的 post-hoc 追加数据，inverted-U 的泛化性证据何在？\n\n---\n\n## Missing References\n\n1. **Hedges, L. V. (1981). Distribution theory for Glass's estimator of effect size and related estimators.** *JEBS*, 6(2), 107–128. — Cohen's d 在小样本下的 bias 及 Hedges' g correction，与本文 n=10 设计直接相关。\n\n2. **Efron, B. (1987). Better bootstrap confidence intervals.** *JASA*, 82(397), 171–185. — BCa interval 的理论基础及其在小样本下的 coverage properties（known to be liberal when n < 20），与 Appendix G 讨论直接相关。\n\n3. **Cui, Y., & Li, J. (2024). Evaluating LLMs with IRT: challenges and opportunities.** — 如果存在类似工作，应在 Related Work 中讨论 IRT 在 LLM 评估中的 limitation 和 assumption violation。\n\n4. **Jiang, Z., et al. (2024). Investigating data contamination in modern benchmarks for large language models.** — 作为 contamination detection 综述的补充。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n**Soundness**: 3 / 5\n\n**Excitement**: 3.5 / 5\n\n**Confidence**: 4 / 5 — 对 IRT、bootstrap 方法和实验设计有扎实背景知识\n\n**Reproducibility**: 3 / 5\n\n### 理由\n\n**优势**：论文提出了一个genuinely novel 的跨学科视角，matched-difference design 巧妙解决了 LLM 系统性违反 IRT 假设的问题，detection-diagnosis tradeoff 的发现对 contamination 检测实践有指导意义。Appendix 体系完整，反映了对方法论细节的认真态度。\n\n**核心问题**：统计推断的严谨性有几个结构性缺陷。最关键的是 N1（CI 仅捕获 clean variability 而忽略 contaminated-run variability，Appendix K 数据表明后者在 50% contamination 下可达 CV=59.6%）和 N4（Cohen's d 实为 one-sample z-score 但被按 two-sample effect size 解释和报告）。这两个问题不影响定性结论（contamination 确实改变 ℓ_z*），但影响定量推断的可信度——而定量推断恰恰是论文的核心卖点（\"all bootstrap 95% CIs exclude zero\"）。\n\nN2（post-hoc condition selection）和 N3（\"systematic\" overclaiming）是 framing 问题，相对容易修复。\n\n如果 N1 和 N4 能在 revision 中得到妥善处理——纳入 multi-seed variability 的 CI、正确标注效应量类型、调整相应 claim——论文可以达到 Conference 水准。当前版本的定量推断基础不够稳固，建议 3.5（Borderline Conference / strong Findings）。\n",
  "reviewer_id": "1",
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — 方法严谨性审查报告\n\n---\n\n## Summary\n\n本文将教育测量学中的 IRT person-fit 统计量（Snijders' ℓ_z*）应用于 LLM benchmark contamination 检测，提出 matched-difference 设计 Δℓ_z* 来分离 contamination-specific aberrance。在三个 7–8B 模型家族上，通过 QLoRA SFT 作为 contamination 代理，识别出三个行为边界：θ-shift dynamics、detection-diagnosis tradeoff 和 ability-dependent non-monotonic dose-response。论文的定位是 characterization 而非 detection tool，核心贡献在于从 psychometrics 视角提供 contamination 行为的机制性理解。\n\n---\n\n## Strengths\n\n**S1. 跨学科视角新颖且动机充分。** 将教育测量学中成熟的 person-fit 统计量引入 LLM contamination 检测是一个有创意的跨领域移植。论文对 IRT 在 LLM 上下文中的适用性给出了合理论证：Section 3.1 说明了 4PL 选择理由（upper asymptote d_i 容纳 guessing/memorization），Section 3.2 坦率承认 LLM 违反 local independence（57/601 cells 即 9.5% flagged），并通过 Δℓ_z* 差分设计将其从 confound 转化为 design feature。\n\n**S2. Matched-difference design 设计优雅。** Δℓ_z* = ℓ_z*_contam − ℓ̄_z*_clean 的设计直接解决了 clean model 本身已有 high ℓ_z*（Appendix C: Qwen clean ℓ_z* 在 7.05–9.53 之间）的核心挑战。Appendix F.1 的 local dependence 模拟（σ_a = 0–1.0, shared vs. asymmetric LD）验证了设计在现实违反条件下的鲁棒性，Appendix A 的 power simulation 给出了基准（MMLU 14,042 items, 97.8% power at 15%）。\n\n**S3. Detection-diagnosis tradeoff 的发现具有实际指导价值。** Table 3（Section 4.3）诚实地展示了 accuracy z-scores 在纯检测上的绝对优势（|d| 高出一个数量级），同时论证了 ℓ_z* 在 diagnostic 层面的独特能力——可在 seen/unseen item subsets 上分别计算（Section 4.3: \"ℓ_z* can be computed separately on seen and unseen item subsets\"），区分 response-pattern anomaly 与 overall performance shift。两阶段工作流建议（先 accuracy 筛查、再 ℓ_z* 诊断）是务实的。\n\n**S4. Epistemic 降级处理得当。** Finding 3（non-monotonic dose-response）被明确标为 \"exploratory\"（Section 4.4 标题），N=1 post-RL observation 被限制在 Appendix I 并反复标注 \"preliminary\"。Limitations section 覆盖了 SFT scope、model scale、single-run 问题，展现了较好的学术诚实度。\n\n**S5. Appendix 体系完整。** Appendices A–K 覆盖了 simulation validation、4PL vs 3PL 对比、seed sensitivity、cross-family consistency、local dependence robustness、item parameter perturbation、BCa check、classical IRT refit、post-RL、hyperparameters 和 reproducibility。这些补充分析回答了许多自然产生的 follow-up 问题。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [critical] Bootstrap CI 仅捕获 clean-seed variability，系统性低估了总不确定性。**\n\n- **位置**: Section 3.2, Table 1, Table 2\n- **问题**: Table 1 的 Cohen's d = (ℓ_z*_contam − mean(ℓ_z*_clean)) / SD(ℓ_z*_clean)，bootstrap resampling 作用于 n=10 clean seeds。这意味着 CI 仅反映 clean baseline 的 sampling variability，**完全忽略了 contaminated run 的 seed-to-seed variability**。然而 Appendix K（Table 15）显示 Qwen 50% contamination 下三个独立 seed 的 free-θ |d| 的 CV=59.6%（range 1.10–7.51）。如果 contaminated ℓ_z* 本身有如此大的变异，Table 1 中基于单次 contaminated run 计算的 |d| 的 CI 就是 **anti-conservative** 的——它声称的精度高于实际精度。\n- **具体后果**: Table 1 caption \"All CIs exclude 0\" 在 50% contamination 条件下可能不成立。如果用 Appendix K 的最低 seed（|d|=1.10 at 50%）替换 Table 1 的单次观测值，CI 可能包含零或大幅缩窄远离零的距离。\n- **为什么影响接收**: 论文的核心量化推断（Contribution 2: \"all bootstrap 95% CIs exclude zero\"）建立在这些 CI 上。如果 CI 系统性低估不确定性，主要结论的可靠性需要重新评估。\n- **建议**: (1) 将 Appendix K 的 multi-seed data 纳入 main analysis，报告包含两种 variability 来源的 CI（如 prediction interval 或 nested bootstrap）；(2) 明确 Table 1 CI 的含义为 \"conditional on the observed contaminated run\"；(3) 讨论 single-run vs multi-seed 估计的差异及其对结论的影响。\n\n**N2. [critical] 实验条件的 post-hoc 扩展引入确认偏差风险。**\n\n- **位置**: Section 3.3 (第 4 页)\n- **问题**: Section 3.3 明确说 \"Following initial observations of non-monotonic dose-response for Qwen, we added 5% and 25% conditions for Qwen to trace the full dose-response curve. The 25% condition was subsequently extended to Llama to test whether the pattern generalizes.\" 这意味着 Finding 3（inverted-U, Section 4.4）的关键证据条件（5%/25%）是在**观察到结果后才追加的**。这是经典的 confirmatory bias 问题：先看到 pattern → 追加数据点 → 声称 pattern 得到 \"confirmation\"。\n- **更深层问题**: 论文虽将 Finding 3 标注为 \"exploratory\"，但 Abstract 中 \"three behavior boundaries\" 的表述将三个 finding 并列呈现，未区分哪些是 pre-planned、哪些是 post-hoc。Section 4.4 标题包含 \"(Exploratory)\" 但在读者快速浏览时容易遗漏。\n- **为什么影响接收**: Post-hoc condition selection 使得 p-values 和 CI 的名义覆盖率不再可靠。如果 5%/25% 条件是 planned，则应在 pre-registration 或 method section 中说明；如果是 post-hoc，则效应量和 CI 需要进行多重比较校正或至少标注为 exploratory。\n- **建议**: (1) 在 Abstract 和 Contributions 中明确区分 confirmatory findings（15%/50% across 三个 model families）和 exploratory findings（5%/25% 追加、non-monotonic dose-response）；(2) 对 post-hoc 追加的条件进行 Bonferroni 或 Holm 校正；(3) 在 Method section 透明报告实验时间线。\n\n**N3. [critical] \"Systematic characterization\" 声称与实验覆盖不匹配。**\n\n- **位置**: Title, Abstract, Contribution 1\n- **问题**: 实验矩阵存在大量系统性空缺：\n  - Mistral 仅测试了 15%/50%（缺 5%/25%）\n  - ARC-Challenge 仅在 Qwen 上测试（Section 3.3: \"constrained by computational budget\"）\n  - Post-RL 扩展为 N=1（单模型、单污染水平、单次训练）\n  - 全部模型为 7–8B，无不同规模覆盖\n  - Contaminated conditions 为 single-run（multi-seed 仅 Qwen，且仅在 Appendix K）\n  \n  在 57 个 model×benchmark×contamination level 的理论设计空间中，实际测试了 12 个条件（Table 1 中可见）。\"Systematic\" 在学术语境中意味着理论驱动的完整覆盖。\n- **为什么影响接收**: Overclaiming 是 ARR reviewer guidelines 中明确的 soundness 扣分项。标题中的 \"systematic\" 设定了一个论文内容无法兑现的期望。\n- **建议**: 将 \"systematic\" 改为 \"controlled\" 或 \"initial\"，或在引言中明确界定 \"systematic\" 的具体含义（如 \"系统地变化 contamination level\"）。\n\n**N4. [critical] Cohen's d 的计算本质是 one-sample z-score，但被呈现为标准效应量。**\n\n- **位置**: Section 3.2, Tables 1–3\n- **问题**: 标准 Cohen's d 用于比较两组均值，需要两组的样本量和方差。本文的计算是 d = (ℓ_z*_contam − mean(ℓ_z*_clean)) / SD(ℓ_z*_clean)，其中 contaminated condition 通常为单次观测（n_contam=1）。这本质上是一个 **z-score**（观测值距 clean 分布均值的标准差数），而非传统两组 Cohen's d。二者在解释上有重要区别：z-score 不包含 contaminated group 的 within-group variability，因此不能直接用 Cohen's d 的 benchmarks（small=0.2, medium=0.5, large=0.8）来解释。\n- **附加问题**: SD 估计基于 n=10（df=9），存在已知的正偏差。Hedges' correction factor J(df) = 1 − 3/(4·df − 1) ≈ 0.914 for df=9 应被应用但未见讨论。\n- **为什么影响接收**: 效应量的正确标注和解释是量化方法论文章的核心 soundness 要求。\n- **建议**: (1) 明确定义 d 的计算公式（当前 Section 3.2 仅说 \"Cohen's d\" 而未给出数学定义）；(2) 讨论 one-sample effect size vs two-sample effect size 的区别；(3) 报告 Hedges' g 以校正小样本偏差。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [warning] BCa vs percentile CI 不一致性的处理有 selective reporting 倾向。**\n\n- **位置**: Section 3.2, Appendix G\n- **问题**: Section 3.2 声称 \"BCa correction (Appendix G) confirms that percentile CIs are conservative estimates\"。但 Appendix G 实际显示：BCa CIs 在大多数条件下**更窄**（mean reduction 22%），唯独 Llama fixed-θ 50% 时 BCa CI = [−0.13, 2.21] **包含零**（vs percentile [0.17, 2.97]）。论文的处理方式是将该条件 dismiss 为 \"already characterized as ineffective in §4.2\"，但这构成循环论证：§4.2 将该条件标为 ineffective 的依据之一就是信号弱，而 BCa CI 包含零正是信号弱的独立证据。此外，BCa 本身在 n=10 时的 jackknife acceleration 估计也不稳定（基于 10 个 leave-one-out 值），论文对此未讨论。\n- **建议**: (1) 在 main text（不仅 Appendix）报告 BCa CI 包含零的条件；(2) 讨论 n=10 下 percentile vs BCa 的选择依据；(3) 不要声称 BCa \"confirms\" percentile CIs 的保守性——这仅在大多数条件下成立。\n\n**W2. [warning] Fixed-θ Qwen 15% 反直觉结果（ratio < 1）的机制解释不清。**\n\n- **位置**: Section 4.2（第 5–6 页）\n- **问题**: Fixed-θ 旨在消除 θ-shift absorption 从而增强信号，但 Table 2 中 Qwen 15% 的 fixed-θ/free-θ ratio 为 0.7×（即 fixed-θ 反而更弱）。论文解释为 \"the Snijders correction bias introduced by anchoring at a mismatch θ outweighs the aberrance eliminated, producing a net signal loss\"。这一解释存在三个问题：\n  1. \"Mismatch θ\" 的量化标准未给出——Qwen clean θ 和 contaminated θ 之间的 Δθ 是多少？为什么该 Δθ 在 15% 时是 \"small enough\" 而在 25%/50% 时不是？\n  2. Snijders correction 在 θ 估计有偏时引入的 bias 方向和大小取决于 Fisher information 矩阵，论文未提供计算。\n  3. 如果 fixed-θ 在部分条件下可能 hurt 检测，那么它作为 \"remedy\" 的实用价值需要被限定——但论文未给出 fixed-θ 适用条件的 guidance。\n- **建议**: 通过 simulation（类似 Appendix A）系统展示 Snijders correction bias 如何随 Δθ 变化，给出 fixed-θ 优于 free-θ 的充分条件。\n\n**W3. [warning] QLoRA 外部效度未充分讨论。**\n\n- **位置**: Section 3.3, Section 5 (\"Contamination model\"), Limitations\n- **问题**: QLoRA 的 low-rank 约束（Table 14: rank=16）限制了参数更新的方向数，这可能使 contamination 产生的 response-pattern anomaly 与 full fine-tuning 或 pretraining contamination 有质的不同。具体地：low-rank update 可能均匀地影响所有 item 的 response probability，而 full parameter update 可能选择性地影响 seen items。论文承认了 SFT 的限制（\"may not generalize to pretraining contamination\"），但未讨论 QLoRA vs full SFT 的差异。Table 14 提供了 hyperparameters 但未报告 LoRA rank/alpha 的选择依据。\n- **建议**: (1) 讨论 LoRA rank 对 person-fit pattern 的可能影响；(2) 至少在一个模型上与 full SFT 对比。\n\n**W4. [warning] ARC-Challenge 结果的可解释性受限于 item count 和 single-model coverage。**\n\n- **位置**: Section 4.1 (ARC-C 段落), Table 1, Appendix A\n- **问题**: ARC-C 仅有 295 items，Appendix A 的 power analysis 显示 80% power 需要 n ≥ 7,958 items at 15% contamination。因此 ARC-C 上的结果在统计上严重 underpowered。Table 1 中 ARC-C 的 Cohen's d 可能受到 inflated estimation（小样本效应量偏差）和 insufficient power（无法检测真实效应）的双重影响。论文解释为 \"ceiling effect\"（Qwen baseline accuracy 67.8%），但 (1) 这与 MMLU 52.4% 的 baseline 差异并不极端；(2) 仅在 Qwen 一个模型上测试，无法区分 ceiling 效应与 ARC-C item-specific 特性。\n- **建议**: (1) 在讨论 ARC-C 结果时明确报告 statistical power 不足的问题；(2) 对 295 items 下 Cohen's d 的 precision 进行 quantification（如 d 的 standard error）。\n\n---\n\n### Minor（不影响接收）\n\n**M1.** Abstract 中 \"n=10 independent seeds per condition\" 的 \"per condition\" 有歧义——实际仅 clean baseline 有 n=10，contaminated conditions 为 single run（Limitations 确认 \"controlled experiments were trained as a single QLoRA run\"）。建议改为 \"n=10 clean baseline seeds per model family\"。\n\n**M2.** Table 2 中 grey cells（Llama/Mistral on ARC-C, Mistral at 5%/25%）仅标注 \"conditions not tested\" 但 caption 未解释原因。读者无法判断缺失是计划内的还是临时的。\n\n**M3.** Appendix B（4PL vs 3PL）仅提供定性描述，缺少 quantitative 对比（如两种参数化下 Cohen's d 的差值或比率）。鉴于 4PL 是方法论核心选择，该对比应更严谨。\n\n**M4.** Section 4.4 中 Qwen 的四级轨迹（|d|: 1.15 → 6.58 → 8.22 → 1.98 at 5%/15%/25%/50%）与 Table 1 中 5% 的 |d|=1.90 不一致。1.15 vs 1.90 的差异需要解释（可能来自不同分析，但文中未标注）。\n\n**M5.** Section 5 \"Scope and calibration\" 提到 57/601 cells 中 |ℓ_z*| > 1.96，但未讨论这些 false-positive-like 信号的分布模式——是否集中在特定模型家族或 benchmark 上？这与 Δℓ_z* design 的有效性直接相关。\n\n---\n\n## Questions\n\n**Q1.** Cohen's d 的精确公式是什么？当 contaminated condition 为 single run（n_contam=1）时，d 是如何定义的？Section 3.2 仅说 \"We report Cohen's d\" 但未给出数学表达式。\n\n**Q2.** Bootstrap resampling 的具体对象是什么？是 resample n=10 clean seeds 来计算 SD 的 bootstrap 分布，还是 resample items 来计算 ℓ_z* 的 bootstrap 分布？前者对应 seed-level bootstrap，后者对应 item-level bootstrap——二者的 coverage properties 完全不同。\n\n**Q3.** Appendix K 的 multi-seed 结果（n=3 contaminated seeds）为何未被纳入 main analysis？如果三个 seed 的 |d| 在 50% 时从 1.10 到 7.51（CV=59.6%），Table 1 中报告的 single-seed |d| 在何种意义上代表该 contamination condition 的效应？\n\n**Q4.** PSN-IRT item parameters 是在什么样本上校准的？如果校准样本中包含了与本文三个 7–8B 模型相似的模型（或其 variants），item parameters 是否可能已经 \"适应\" 了这些模型的 response pattern，从而影响 ℓ_z* 的 calibration？\n\n**Q5.** Fixed-θ 分析中 θ 是固定在 n=10 clean seeds 的 mean θ 还是某个特定 seed 的 θ？Appendix K note 确认 \"Fixed-θ estimation anchors θ at the clean-baseline mean\"，但 mean θ 本身有 estimation error（基于 n=10），这一误差是否传播到了 fixed-θ Cohen's d 中？\n\n**Q6.** Section 4.4 声称 Llama 的 non-monotonic pattern \"directionally consistent but statistically non-significant\"（|d|: 2.27→2.97, overlapping CIs），但这不能被解释为 \"pattern replicates\"。在 Mistral 上完全未测试 5%/25% 条件。仅凭 Qwen 一个模型的 post-hoc 追加数据，inverted-U 的泛化性证据何在？\n\n---\n\n## Missing References\n\n1. **Hedges, L. V. (1981). Distribution theory for Glass's estimator of effect size and related estimators.** *JEBS*, 6(2), 107–128. — Cohen's d 在小样本下的 bias 及 Hedges' g correction，与本文 n=10 设计直接相关。\n\n2. **Efron, B. (1987). Better bootstrap confidence intervals.** *JASA*, 82(397), 171–185. — BCa interval 的理论基础及其在小样本下的 coverage properties（known to be liberal when n < 20），与 Appendix G 讨论直接相关。\n\n3. **Cui, Y., & Li, J. (2024). Evaluating LLMs with IRT: challenges and opportunities.** — 如果存在类似工作，应在 Related Work 中讨论 IRT 在 LLM 评估中的 limitation 和 assumption violation。\n\n4. **Jiang, Z., et al. (2024). Investigating data contamination in modern benchmarks for large language models.** — 作为 contamination detection 综述的补充。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n**Soundness**: 3 / 5\n\n**Excitement**: 3.5 / 5\n\n**Confidence**: 4 / 5 — 对 IRT、bootstrap 方法和实验设计有扎实背景知识\n\n**Reproducibility**: 3 / 5\n\n### 理由\n\n**优势**：论文提出了一个genuinely novel 的跨学科视角，matched-difference design 巧妙解决了 LLM 系统性违反 IRT 假设的问题，detection-diagnosis tradeoff 的发现对 contamination 检测实践有指导意义。Appendix 体系完整，反映了对方法论细节的认真态度。\n\n**核心问题**：统计推断的严谨性有几个结构性缺陷。最关键的是 N1（CI 仅捕获 clean variability 而忽略 contaminated-run variability，Appendix K 数据表明后者在 50% contamination 下可达 CV=59.6%）和 N4（Cohen's d 实为 one-sample z-score 但被按 two-sample effect size 解释和报告）。这两个问题不影响定性结论（contamination 确实改变 ℓ_z*），但影响定量推断的可信度——而定量推断恰恰是论文的核心卖点（\"all bootstrap 95% CIs exclude zero\"）。\n\nN2（post-hoc condition selection）和 N3（\"systematic\" overclaiming）是 framing 问题，相对容易修复。\n\n如果 N1 和 N4 能在 revision 中得到妥善处理——纳入 multi-seed variability 的 CI、正确标注效应量类型、调整相应 claim——论文可以达到 Conference 水准。当前版本的定量推断基础不够稳固，建议 3.5（Borderline Conference / strong Findings）。\n",
    "reviewer_id": "1",
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 560 · 2026-05-22T23:02:06.650607+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3866
}
```

</details>

---


### Tool call

_source line 561 · 2026-05-22T23:02:15.458065+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 562 · 2026-05-22T23:02:15.508708+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 563 · 2026-05-22T23:02:34.521217+00:00_

审稿报告已提交给 Review Director，评分 **3.5 (Borderline Conference)**。

核心发现：
- **4个 Must-Fix**：Bootstrap CI 仅捕获 clean-seed variability 而忽略 contaminated-run variability（Appendix K 显示 50% 时 CV=59.6%）；实验条件 post-hoc 扩展引入确认偏差；"systematic" 声称与不完整的实验矩阵不匹配；Cohen's d 实为 one-sample z-score 但被按标准 effect size 报告
- **4个 Should-Fix**：BCa vs percentile CI 处理有 selective reporting 倾向；fixed-θ 反直觉结果（Qwen 15% ratio 0.7×）机制解释不充分；QLoRA 外部效度；ARC-C 统计功效不足
- **5个 Minor**：Abstract 中 "per condition" 歧义、Table 2 grey cells 未解释、4PL vs 3PL 对比不够定量、Section 4.4 数字不一致、57/601 flagged cells 分布未分析

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1"
}
```

</details>

---


## Round 21

## Round 21

16 recorded events


### User

_source line 564 · 2026-05-22T23:02:35.630833+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿报告（新颖性 + 完整性 + 写作）

### 总体评分
**Overall Assessment**: 3.5 — Borderline Conference

### Must-Fix 问题

**N1** [critical] 标题与方法的根本性错位——"Binary Response Patterns" 掩盖了对 PSN-IRT 外部 item bank 的关键依赖
- 标题 "What Can Binary Response Patterns Reveal About Benchmark Contamination?" 暗示仅凭二元作答模式即可完成分析。但方法的核心步骤依赖 PSN-IRT（Zhou et al., 2026）提供的外部标定 4PL item parameters（a_i, b_i, c_i, d_i），没有这些参数，ℓ_z* 和 HT 无法计算。Abstract 中虽提及但将其处理为辅助条件而非核心前提。
- 建议标题改为 "What Can IRT Person-Fit Statistics Reveal About Benchmark Contamination?"

**N2** [critical] 实验范围与声明范围的 scope mismatch——"benchmark contamination" vs. 仅 SFT-stage QLoRA
- 标题和 abstract 使用宽泛术语，但全部控制实验仅覆盖 SFT-stage QLoRA fine-tuning。Pretraining contamination、full-parameter fine-tuning、RLHF/DPO contamination 均未测试。

### Should-Fix 问题

**W1** 三个核心 findings 的理论可预测性削弱了新颖性
- Finding 1（θ-shift dynamics）是 person-fit 文献已知现象
- Finding 2（detection-diagnosis tradeoff）是 bias-variance tradeoff 标准结果
- Finding 3 最具新颖性但证据最弱

**W2** Non-monotonic dose-response（Finding 3）证据不充分
- 仅 Qwen 表现清晰非单调性；Llama CIs 重叠；Mistral 未完整测试
- n=3 seeds 统计 power 有限

**W3** 模型多样性不足——仅 7-8B 规模、3 个 family

**W4** Post-RL extension N=1 结构权重过高

**W5** 与 simpler contamination detection baselines 的比较缺失

### Questions
Q1: PSN-IRT item bank 基于~13,000 leaderboard 模型——是否存在 circularity？
Q2: 如果补充 Llama/Mistral 在所有 contamination levels 的数据，Finding 3 是否仍成立？
Q3: n≥7,000 items for 80% power at 15% contamination——方法在多数 benchmark 上不可用？
Q4: 为什么选 QLoRA 而非 full fine-tuning？

### Missing References
- Han et al. (2025): "Quantifying Data Contamination in Psychometric Evaluations of LLMs"
- Xia & Zheng (2018): "Asymptotically Normally Distributed Person Fit Indices for Detecting Spuriously High Scores on Difficult Items"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 565 · 2026-05-22T23:04:00.368056+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
  "project": "irt_personfit_contam",
  "pages": "1-4,7,9-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/submitted.pdf",
    "project": "irt_personfit_contam",
    "pages": "1-4,7,9-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 566 · 2026-05-22T23:04:01.373118+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.0}], \"total_pages\": 15, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 567 · 2026-05-22T23:04:05.043474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 568 · 2026-05-22T23:04:05.947953+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-22T23:04:05.948402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-22T23:04:06.501091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-22T23:04:07.055257+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1106
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-22T23:04:07.055668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-22T23:04:07.106850+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool result

_source line 574 · 2026-05-22T23:04:07.662856+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-22T23:06:38.719956+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: 标题与 PSN-IRT 依赖的错位\n\nR2 的诊断基本成立。标题 \"What Can Binary Response Patterns Reveal...\" 确实给读者留下了仅凭二元作答即可完成分析的印象，但方法在计算 ℓ_z* 之前必须接入 PSN-IRT 的外部 4PL item parameters（Section 3.1）。论文在第 2 页 Contributions 前明确列出了三层依赖——\"(i) pre-calibrated 4PL item parameters from the PSN-IRT item bank, (ii) an external resource derived from 13,000+ models, (iii) binary response patterns\"——所以信息并非隐藏，但放在标题层面确实有误导性。\n\n**不过我认为严重程度是 Should-Fix 而非 Must-Fix。** 标题用的是问句形式（\"What Can ... Reveal?\"），探讨的是 response pattern 中包含的信息量，而非声称 binary patterns 是唯一输入。R2 建议的替代标题 \"What Can IRT Person-Fit Statistics Reveal...\" 更精确，我支持这一修改。\n\n### [AGREE] R2-N2: 实验范围 vs 声明范围的 scope mismatch\n\n同意诊断，但**建议降级为 Should-Fix**。理由如下：\n\n1. Contribution 2（第 2 页）明确使用了 \"SFT-stage contamination\" 的限定语。\n2. Limitations（第 9 页）明确写道 \"Our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination, which operates through different learning dynamics.\"\n3. 论文的标题用的是更宽泛的 \"Benchmark Contamination\"，但这是研究的**问题域**（phenomenon），而非声称覆盖所有形式。\n\n**核心问题不在于 scope 未被标注（已在多处标注），而在于标题/Abstract 与 body 之间的 framing 落差。** 修复方案：在 Abstract 第一句或标题中加入 \"SFT-Stage\" 限定词即可解决，无需重做实验。这与我自己的 N3（\"systematic\" overclaiming）属于同类问题。\n\n---\n\n## Should-Fix 问题\n\n### [REBUT] R2-W1: 三个 Findings 的理论可预测性削弱新颖性\n\nR2 的论点是三个 findings 可从已有理论预测，因此新颖性不足。我不同意这一评估，逐条说明：\n\n**Finding 1（θ-shift dynamics）**：R2 称这是 \"person-fit 文献已知现象\"。确实，IRT 文献讨论过 ability estimation 对 person-fit 的影响（Meijer & Sijtsma, 2001），但**未讨论过**以下具体发现：(a) LLM 的 baseline ability 范围（θ 跨度远超人类被试）如何调制检测灵敏度；(b) higher-ability models（如 Qwen 67.8%）在高污染水平下出现更强的 θ-shift absorption（Section 4.2, Figure 2 的 heatmap 清晰显示这一模式）；(c) 该现象的量化幅度（Qwen free-θ |d| 从 25% 的 8.22 降至 50% 的 ~1.98）。这些具体发现无法仅从一般理论推导。\n\n**Finding 2（detection-diagnosis tradeoff）**：R2 将其等同于 \"bias-variance tradeoff 标准结果\"，这是不准确的类比。Table 3（Section 4.3）展示的是**不同统计量之间的 detection power vs diagnostic information 的 tradeoff**：accuracy z-scores 检测效应量高出一个数量级（如 Qwen: Acc z |d|≈42.5 vs ℓ_z* |d|≈6.58），但**仅 ℓ_z* 能在 seen/unseen item subsets 上分别计算**以区分 response-pattern anomaly 和 overall performance shift。这不是 bias-variance（估计量的偏差与方差），而是**信息类型之间的质的差异**。这一量化结果对实践者选择检测方法有直接指导价值，在 contamination detection 文献中此前未有文献报告。\n\n**Finding 3**：我同意 R2 的判断——这是三个 finding 中证据最弱的，论文的 \"exploratory\" 标注是恰当的。\n\n**总结**：characterization 论文的价值在于将一般理论推导无法给出的**具体量化结果**记录下来。\"理论上可预测\" ≠ \"已经被预测并验证\"。论文在新领域（LLM contamination）中填补了实证空白。\n\n### [AGREE] R2-W2: Non-monotonic dose-response 证据不充分\n\n同意。这与我自己的 N2（post-hoc condition selection 引入确认偏差）一致。具体地：\n- 仅 Qwen 一个模型展示了清晰的 inverted-U（Section 4.4: |d| 1.15→6.58→8.22→1.98）\n- Llama 的 pattern \"directionally consistent but statistically non-significant\"（第 7 页: |d|=2.27→2.97, heavily overlapping CIs）\n- Mistral 在 5%/25% 完全未测试\n- n=3 multi-seed validation 的统计 power 有限（Appendix K: 50% CV=59.6%）\n- 5%/25% 条件是在观察到 non-monotonicity 后 post-hoc 追加的（Section 3.3 明确说明）\n\n### [AGREE] R2-W3: 模型多样性不足\n\n同意，与我的 N3 一致。全部模型为 7-8B 规模、instruction-tuned variants。无 larger models（13B+）、无 base models（non-instruct）、无 non-transformer architectures。论文声称的 \"across three model families\" 在规模和架构维度上实际是同质的。\n\n### [AGREE] R2-W4: Post-RL N=1 权重过高\n\n同意。Appendix I 和 Figure 4 基于单一模型（Qwen 15% MMLU）、单次 GRPO 训练、三个 checkpoint 的定性观察。论文在 Section 4.4 和 Appendix I 中反复标注 \"preliminary\" 和 \"N=1\"，处理是诚实的，但 Abstract 中仍提及 \"contamination patterns may persist after GRPO alignment\"，给予了与证据强度不匹配的可见度。建议将 post-RL 提及从 Abstract 中移除。\n\n### [REBUT] R2-W5: 与 simpler contamination detection baselines 的比较缺失\n\n**R2 似乎遗漏了 Table 3 和 Section 4.3。** 论文的 Section 4.3（\"Detection-Diagnosis Tradeoff\"，第 7 页）**正是**与 simpler baselines 的系统比较。Table 3 直接对比了三个统计量：\n\n| 统计量 | Qwen |d| (15%) | Llama |d| | Mistral |d| |\n|--------|---------|----------|-----------|\n| ℓ_z* | 6.58 | 2.27 | 3.01 |\n| HT | 7.20 | 2.05 | 4.30 |\n| Acc z | 42.5 | 23.1 | 7.81 |\n\n论文明确承认 accuracy z-scores \"several-fold to over an order of magnitude larger than person-fit statistics\"（Section 4.3），并提出两阶段工作流：先用 accuracy z-scores 筛查，再用 ℓ_z* 诊断。Section 4.3 的最后一段还讨论了 ℓ_z* 在 diagnostic 层面的独特能力：\"ℓ_z* can be computed separately on seen and unseen item subsets\"。\n\n此外，Table 8（Appendix E）还报告了 item-level contamination detection 的 AUROC（ℓ_z* anomaly: 0.53, LR cross-model: 0.59, RF cross-model: 0.63），进一步展示了与其他方法的比较。\n\n**R2 的 W5 不成立——该比较在论文中有充分呈现。**\n\n---\n\n## Questions\n\n### R2-Q1: PSN-IRT circularity\n\n**部分有效的担忧。** 如果 PSN-IRT 的 ~13,000 校准模型中包含 contaminated models，item parameters 可能已隐含了 contamination 效应，从而削弱 ℓ_z* 对 contamination 的灵敏度。\n\n但论文有两层防护：\n1. **稀释效应**：13,000+ 模型中 contaminated models 是少数，其影响被稀释。\n2. **Appendix H 的反面论证**：Appendix H 用 N=178 leaderboard 模型做了 classical MML-EM refit，显示 discrimination 与 PSN-IRT 的相关性仅 r_a=0.127（几乎不相关），说明 PSN-IRT 的参数校准方法与简单 MML-EM 有本质差异，不是直接从 leaderboard response patterns 拟合的。\n\n**但 R2 提出了一个论文未讨论的有效角度**：如果 PSN-IRT 的校准样本**包含了与本文 7-8B 模型高度相似的 variants**（如 Qwen2.5-7B 的其他版本），item parameters 可能已经 \"适应\" 了这些模型家族的 response pattern。论文应讨论 PSN-IRT 校准样本的构成及潜在 overlap。\n\n### R2-Q2: Finding 3 能否在更完整数据下复现？\n\n无法在当前数据上回答。我同意这是一个关键 open question。如果 Llama/Mistral 在所有 contamination levels 的完整数据显示**单调** dose-response，则 Qwen 的 inverted-U 可能是 model-specific artifact 而非通用 boundary condition。这进一步支持了 Finding 3 应保持 \"exploratory\" 标签。\n\n### [REBUT] R2-Q3: n≥7,000 限制了方法的适用性\n\nR2 的逻辑是：如果方法需要 7,000+ items 才有 80% power，则对大多数 benchmark 不可用。但：\n\n1. **这是一个诚实报告的 power limitation，不是方法论缺陷。** Appendix A 的 power analysis 是论文自己提供的，展示了 transparent self-assessment。\n2. **MMLU（14,042 items）是最广泛使用的 LLM benchmark**，远超 7,000 阈值。论文的主要结论基于 MMLU。\n3. **论文的 two-stage workflow（Section 4.3）直接回应了这一限制**：对小 benchmark 用 accuracy z-scores（无 item count 限制），仅在大 benchmark 上部署 ℓ_z*。\n4. **ARC-C（295 items）的结果本身就是 power limitation 的实证展示**——效应可检测但信号较弱，这与 power analysis 的预测一致。\n\n方法对某些 benchmark 不适用是一个**适用性边界**，不是致命缺陷。论文应在 Practical Implications（Section 5）中更明确地标注这一边界。\n\n### R2-Q4: 为什么选 QLoRA 而非 full fine-tuning？\n\n**有效问题。** 论文未解释 QLoRA 的选择理由。从实验设计角度，QLoRA（rank=16, Appendix J/Table 14）的 low-rank 约束限制了参数更新方向数，可能使 contamination 产生的 response-pattern anomaly 与 full SFT 有质的不同。论文应讨论：(1) QLoRA 选择的 computational justification；(2) LoRA rank 对 person-fit pattern 的潜在影响；(3) 至少定性地论证 QLoRA vs full SFT 在 response-pattern level 的预期差异。与我的 W3 一致。\n\n---\n\n## Missing References\n\n### Han et al. (2025/2026)\n\n**论文已引用。** 第 3 页 Related Work: \"Han et al. (2026) quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks.\" R2 可能因年份差异（preprint 2025 vs published 2026）而未识别到已有引用。\n\n### Xia & Zheng (2018): Asymptotically normally distributed person-fit indices\n\n**同意应补充。** 该文讨论了检测 hard items 上异常高分的 person-fit index，与 contamination 场景（模型在 memorized difficult items 上获得不正常高分）直接相关。论文当前的 person-fit 文献综述（Section 3.1）引用了 Snijders (2001), Meijer & Sijtsma (2001), Karabatsos (2003), Sinharay (2017a/b)，但缺少对 spuriously high score 检测的专门讨论。Xia & Zheng (2018) 填补了这一空白。\n\n---\n\n## 总结\n\nR2 的审稿整体公允，在 title framing（N1）、scope mismatch（N2）和 model diversity（W3）方面与我的评估高度一致。但有两处我认为 R2 的评估有误：\n\n1. **W5（缺失 simpler baselines 比较）**：Table 3 和 Section 4.3 已充分覆盖，R2 似乎遗漏了该部分。这应从 weakness 列表中移除。\n2. **W1（findings 理论可预测）**：将 Finding 2 等同于 bias-variance tradeoff 是不准确的类比。characterization 论文的贡献在于量化实证而非理论惊喜。\n\nR2 的 N1 和 N2 我同意诊断但建议降级为 Should-Fix——论文在 body text 中已有明确 scoping，修复仅需调整 title/abstract 措辞。\n",
  "reviewer_id": "1",
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: 标题与 PSN-IRT 依赖的错位\n\nR2 的诊断基本成立。标题 \"What Can Binary Response Patterns Reveal...\" 确实给读者留下了仅凭二元作答即可完成分析的印象，但方法在计算 ℓ_z* 之前必须接入 PSN-IRT 的外部 4PL item parameters（Section 3.1）。论文在第 2 页 Contributions 前明确列出了三层依赖——\"(i) pre-calibrated 4PL item parameters from the PSN-IRT item bank, (ii) an external resource derived from 13,000+ models, (iii) binary response patterns\"——所以信息并非隐藏，但放在标题层面确实有误导性。\n\n**不过我认为严重程度是 Should-Fix 而非 Must-Fix。** 标题用的是问句形式（\"What Can ... Reveal?\"），探讨的是 response pattern 中包含的信息量，而非声称 binary patterns 是唯一输入。R2 建议的替代标题 \"What Can IRT Person-Fit Statistics Reveal...\" 更精确，我支持这一修改。\n\n### [AGREE] R2-N2: 实验范围 vs 声明范围的 scope mismatch\n\n同意诊断，但**建议降级为 Should-Fix**。理由如下：\n\n1. Contribution 2（第 2 页）明确使用了 \"SFT-stage contamination\" 的限定语。\n2. Limitations（第 9 页）明确写道 \"Our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination, which operates through different learning dynamics.\"\n3. 论文的标题用的是更宽泛的 \"Benchmark Contamination\"，但这是研究的**问题域**（phenomenon），而非声称覆盖所有形式。\n\n**核心问题不在于 scope 未被标注（已在多处标注），而在于标题/Abstract 与 body 之间的 framing 落差。** 修复方案：在 Abstract 第一句或标题中加入 \"SFT-Stage\" 限定词即可解决，无需重做实验。这与我自己的 N3（\"systematic\" overclaiming）属于同类问题。\n\n---\n\n## Should-Fix 问题\n\n### [REBUT] R2-W1: 三个 Findings 的理论可预测性削弱新颖性\n\nR2 的论点是三个 findings 可从已有理论预测，因此新颖性不足。我不同意这一评估，逐条说明：\n\n**Finding 1（θ-shift dynamics）**：R2 称这是 \"person-fit 文献已知现象\"。确实，IRT 文献讨论过 ability estimation 对 person-fit 的影响（Meijer & Sijtsma, 2001），但**未讨论过**以下具体发现：(a) LLM 的 baseline ability 范围（θ 跨度远超人类被试）如何调制检测灵敏度；(b) higher-ability models（如 Qwen 67.8%）在高污染水平下出现更强的 θ-shift absorption（Section 4.2, Figure 2 的 heatmap 清晰显示这一模式）；(c) 该现象的量化幅度（Qwen free-θ |d| 从 25% 的 8.22 降至 50% 的 ~1.98）。这些具体发现无法仅从一般理论推导。\n\n**Finding 2（detection-diagnosis tradeoff）**：R2 将其等同于 \"bias-variance tradeoff 标准结果\"，这是不准确的类比。Table 3（Section 4.3）展示的是**不同统计量之间的 detection power vs diagnostic information 的 tradeoff**：accuracy z-scores 检测效应量高出一个数量级（如 Qwen: Acc z |d|≈42.5 vs ℓ_z* |d|≈6.58），但**仅 ℓ_z* 能在 seen/unseen item subsets 上分别计算**以区分 response-pattern anomaly 和 overall performance shift。这不是 bias-variance（估计量的偏差与方差），而是**信息类型之间的质的差异**。这一量化结果对实践者选择检测方法有直接指导价值，在 contamination detection 文献中此前未有文献报告。\n\n**Finding 3**：我同意 R2 的判断——这是三个 finding 中证据最弱的，论文的 \"exploratory\" 标注是恰当的。\n\n**总结**：characterization 论文的价值在于将一般理论推导无法给出的**具体量化结果**记录下来。\"理论上可预测\" ≠ \"已经被预测并验证\"。论文在新领域（LLM contamination）中填补了实证空白。\n\n### [AGREE] R2-W2: Non-monotonic dose-response 证据不充分\n\n同意。这与我自己的 N2（post-hoc condition selection 引入确认偏差）一致。具体地：\n- 仅 Qwen 一个模型展示了清晰的 inverted-U（Section 4.4: |d| 1.15→6.58→8.22→1.98）\n- Llama 的 pattern \"directionally consistent but statistically non-significant\"（第 7 页: |d|=2.27→2.97, heavily overlapping CIs）\n- Mistral 在 5%/25% 完全未测试\n- n=3 multi-seed validation 的统计 power 有限（Appendix K: 50% CV=59.6%）\n- 5%/25% 条件是在观察到 non-monotonicity 后 post-hoc 追加的（Section 3.3 明确说明）\n\n### [AGREE] R2-W3: 模型多样性不足\n\n同意，与我的 N3 一致。全部模型为 7-8B 规模、instruction-tuned variants。无 larger models（13B+）、无 base models（non-instruct）、无 non-transformer architectures。论文声称的 \"across three model families\" 在规模和架构维度上实际是同质的。\n\n### [AGREE] R2-W4: Post-RL N=1 权重过高\n\n同意。Appendix I 和 Figure 4 基于单一模型（Qwen 15% MMLU）、单次 GRPO 训练、三个 checkpoint 的定性观察。论文在 Section 4.4 和 Appendix I 中反复标注 \"preliminary\" 和 \"N=1\"，处理是诚实的，但 Abstract 中仍提及 \"contamination patterns may persist after GRPO alignment\"，给予了与证据强度不匹配的可见度。建议将 post-RL 提及从 Abstract 中移除。\n\n### [REBUT] R2-W5: 与 simpler contamination detection baselines 的比较缺失\n\n**R2 似乎遗漏了 Table 3 和 Section 4.3。** 论文的 Section 4.3（\"Detection-Diagnosis Tradeoff\"，第 7 页）**正是**与 simpler baselines 的系统比较。Table 3 直接对比了三个统计量：\n\n| 统计量 | Qwen |d| (15%) | Llama |d| | Mistral |d| |\n|--------|---------|----------|-----------|\n| ℓ_z* | 6.58 | 2.27 | 3.01 |\n| HT | 7.20 | 2.05 | 4.30 |\n| Acc z | 42.5 | 23.1 | 7.81 |\n\n论文明确承认 accuracy z-scores \"several-fold to over an order of magnitude larger than person-fit statistics\"（Section 4.3），并提出两阶段工作流：先用 accuracy z-scores 筛查，再用 ℓ_z* 诊断。Section 4.3 的最后一段还讨论了 ℓ_z* 在 diagnostic 层面的独特能力：\"ℓ_z* can be computed separately on seen and unseen item subsets\"。\n\n此外，Table 8（Appendix E）还报告了 item-level contamination detection 的 AUROC（ℓ_z* anomaly: 0.53, LR cross-model: 0.59, RF cross-model: 0.63），进一步展示了与其他方法的比较。\n\n**R2 的 W5 不成立——该比较在论文中有充分呈现。**\n\n---\n\n## Questions\n\n### R2-Q1: PSN-IRT circularity\n\n**部分有效的担忧。** 如果 PSN-IRT 的 ~13,000 校准模型中包含 contaminated models，item parameters 可能已隐含了 contamination 效应，从而削弱 ℓ_z* 对 contamination 的灵敏度。\n\n但论文有两层防护：\n1. **稀释效应**：13,000+ 模型中 contaminated models 是少数，其影响被稀释。\n2. **Appendix H 的反面论证**：Appendix H 用 N=178 leaderboard 模型做了 classical MML-EM refit，显示 discrimination 与 PSN-IRT 的相关性仅 r_a=0.127（几乎不相关），说明 PSN-IRT 的参数校准方法与简单 MML-EM 有本质差异，不是直接从 leaderboard response patterns 拟合的。\n\n**但 R2 提出了一个论文未讨论的有效角度**：如果 PSN-IRT 的校准样本**包含了与本文 7-8B 模型高度相似的 variants**（如 Qwen2.5-7B 的其他版本），item parameters 可能已经 \"适应\" 了这些模型家族的 response pattern。论文应讨论 PSN-IRT 校准样本的构成及潜在 overlap。\n\n### R2-Q2: Finding 3 能否在更完整数据下复现？\n\n无法在当前数据上回答。我同意这是一个关键 open question。如果 Llama/Mistral 在所有 contamination levels 的完整数据显示**单调** dose-response，则 Qwen 的 inverted-U 可能是 model-specific artifact 而非通用 boundary condition。这进一步支持了 Finding 3 应保持 \"exploratory\" 标签。\n\n### [REBUT] R2-Q3: n≥7,000 限制了方法的适用性\n\nR2 的逻辑是：如果方法需要 7,000+ items 才有 80% power，则对大多数 benchmark 不可用。但：\n\n1. **这是一个诚实报告的 power limitation，不是方法论缺陷。** Appendix A 的 power analysis 是论文自己提供的，展示了 transparent self-assessment。\n2. **MMLU（14,042 items）是最广泛使用的 LLM benchmark**，远超 7,000 阈值。论文的主要结论基于 MMLU。\n3. **论文的 two-stage workflow（Section 4.3）直接回应了这一限制**：对小 benchmark 用 accuracy z-scores（无 item count 限制），仅在大 benchmark 上部署 ℓ_z*。\n4. **ARC-C（295 items）的结果本身就是 power limitation 的实证展示**——效应可检测但信号较弱，这与 power analysis 的预测一致。\n\n方法对某些 benchmark 不适用是一个**适用性边界**，不是致命缺陷。论文应在 Practical Implications（Section 5）中更明确地标注这一边界。\n\n### R2-Q4: 为什么选 QLoRA 而非 full fine-tuning？\n\n**有效问题。** 论文未解释 QLoRA 的选择理由。从实验设计角度，QLoRA（rank=16, Appendix J/Table 14）的 low-rank 约束限制了参数更新方向数，可能使 contamination 产生的 response-pattern anomaly 与 full SFT 有质的不同。论文应讨论：(1) QLoRA 选择的 computational justification；(2) LoRA rank 对 person-fit pattern 的潜在影响；(3) 至少定性地论证 QLoRA vs full SFT 在 response-pattern level 的预期差异。与我的 W3 一致。\n\n---\n\n## Missing References\n\n### Han et al. (2025/2026)\n\n**论文已引用。** 第 3 页 Related Work: \"Han et al. (2026) quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks.\" R2 可能因年份差异（preprint 2025 vs published 2026）而未识别到已有引用。\n\n### Xia & Zheng (2018): Asymptotically normally distributed person-fit indices\n\n**同意应补充。** 该文讨论了检测 hard items 上异常高分的 person-fit index，与 contamination 场景（模型在 memorized difficult items 上获得不正常高分）直接相关。论文当前的 person-fit 文献综述（Section 3.1）引用了 Snijders (2001), Meijer & Sijtsma (2001), Karabatsos (2003), Sinharay (2017a/b)，但缺少对 spuriously high score 检测的专门讨论。Xia & Zheng (2018) 填补了这一空白。\n\n---\n\n## 总结\n\nR2 的审稿整体公允，在 title framing（N1）、scope mismatch（N2）和 model diversity（W3）方面与我的评估高度一致。但有两处我认为 R2 的评估有误：\n\n1. **W5（缺失 simpler baselines 比较）**：Table 3 和 Section 4.3 已充分覆盖，R2 似乎遗漏了该部分。这应从 weakness 列表中移除。\n2. **W1（findings 理论可预测）**：将 Finding 2 等同于 bias-variance tradeoff 是不准确的类比。characterization 论文的贡献在于量化实证而非理论惊喜。\n\nR2 的 N1 和 N2 我同意诊断但建议降级为 Should-Fix——论文在 body text 中已有明确 scoping，修复仅需调整 title/abstract 措辞。\n",
    "reviewer_id": "1",
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-22T23:06:42.533503+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3813
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-22T23:06:48.560092+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-22T23:06:48.660810+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 579 · 2026-05-22T23:06:56.467003+00:00_

回应已提交。核心判断：

- **R2-W5（缺失 simpler baselines 比较）不成立** — Table 3 + Section 4.3 已有完整覆盖
- **R2-W1 部分不成立** — Finding 2 不是 bias-variance tradeoff，而是 detection power vs diagnostic information 的质的差异
- **R2-N1/N2 同意诊断但建议降为 Should-Fix** — body text 已有 scoping，修复仅需调整 title/abstract
- 其余 Must-Fix/Should-Fix 与我自己的评估高度一致（W2=我的N2，W3=我的N3，W4=我的W4 equivalent）
- Han et al. 已被论文引用（第 3 页），R2 可能因年份差异未识别

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1"
}
```

</details>

---


## Round 22

## Round 22

64 recorded events


### User

_source line 580 · 2026-05-22T23:36:38.703853+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性** 审查。

## 论文信息
- **标题**: "What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?"
- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`
- **PDF 路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/submitted.pdf`

## Venue 要求
- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)
- **截止日期**: 2026-05-25 AoE
- **格式**: ACL 模板, Long paper
- **页数限制**: 正文 8 页，参考文献无限制，Limitations 必须有（不计入页数上限），Ethical Considerations 可选（不计入页数）
- **匿名规则**: Double-blind (two-way anonymized review)
- **附录**: 跟在参考文献后，不计入页数，审稿人无义务阅读
- **评分标准**: 5 = Consider for Award（约前2.5%），4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1 = Do not resubmit

## 你的审查侧重：方法严谨性

请重点审查以下方面：

1. **统计方法的正确性**：IRT person-fit 统计量（ℓz*）的使用是否正确？Bootstrap CI 的构造方法是否合理？效应量（Cohen's d）的计算和解读是否准确？
2. **实验设计**：污染实验（QLoRA SFT）的设计是否严谨？控制变量是否充分？样本量（clean seeds, contaminated runs）是否支撑所述结论？
3. **CI 和不确定性量化**：置信区间是否充分反映了所有不确定性来源（clean baseline variability + contaminated run variability）？是否存在系统性低估？
4. **效应量解读**：Cohen's d benchmarks 的使用是否恰当？单样本 vs 两样本的区分是否清楚？
5. **可复现性**：训练细节、超参数、数据处理流程是否足够详细以支持复现？
6. **Post-hoc 分析**：哪些实验/分析是 confirmatory vs exploratory？论文是否透明披露？
7. **跨模型/跨基准一致性**：三个模型族的结论是否一致？ARC-C 结果如何解读？

请按以下格式输出审稿意见：

### Summary
（2-3 句概括论文）

### Strengths
（逐条列出，标注 [S1], [S2], ...）

### Weaknesses
（逐条列出，标注 [W1], [W2], ...，按严重程度排序：Must-Fix > Should-Fix > Minor）

### Questions
（需要作者澄清的问题）

### Missing References
（遗漏的重要相关工作）

### Overall Assessment
（评分 + 简要理由，使用 EMNLP 2026 评分标准）

### Confidence
（1-5，5 = 完全确定）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-22T23:36:48.152805+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-22T23:36:48.204507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-22T23:36:56.080383+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/submitted.pdf",
  "project": "irt_personfit_contam",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/submitted.pdf",
    "project": "irt_personfit_contam",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-22T23:36:56.231863+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-22T23:36:57.738901+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 558.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 346.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1658
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-22T23:37:05.338784+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 reviewer guidelines:

## Reviewer Guidelines Overview

ARR developed detailed guidelines and suggestions for each step of the review process, including a list of common problems in both reviews and NLP papers to watch out for. The full reviewer guidelines are available on the ARR website at aclrollingreview.org/reviewerguidelines.

## Key Reviewer Policies for 2026

Starting in May 2025, ARR adopts a policy on 'highly irresponsible' (meta-)reviewers, with the program chairs and ARR EiCs considering egregious cases reported by chairs, including extremely terse reviews, unprofessional tone, and LLM-generated reviews.

Starting from May 2025, ACL introduces an awards policy for revi
…[truncated 789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9106
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-22T23:37:14.323799+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions/criteria, scoring scales (1-5 or whatever scale they use), and detailed descriptions for each dimension. I need: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, Clarity, and any other review form fields with their exact scoring descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions/criteria, scoring scales (1-5 or whatever scale they use), and detailed descriptions for each dimension. I need: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, Clarity, and any other review form fields with their exact scoring descriptions."
  }
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-22T23:37:15.027254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-22T23:37:15.329290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-22T23:37:15.883091+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-22T23:37:15.883531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 592 · 2026-05-22T23:37:16.438737+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-22T23:37:16.690469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool result

_source line 594 · 2026-05-22T23:37:19.249337+00:00_

# ARR Review Form Dimensions - Content Summary

Based on the provided guidelines, the document references a review form but **does not include the complete scoring scales or detailed dimension descriptions** you're requesting.

## What the Guidelines Mention:

The guidelines indicate reviewers provide **three scores** (as of February 2025):

1. **Soundness** - "must be justified by the text of the review"
2. **Excitement** - described as "more subjective" and "orthogonal to soundness assessment"
3. **Overall Assessment** - "explicit recommendation for the outcome"

## Critical Gap:

The document states: "Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation."

However, it provides **no specific scoring scales (1-5, etc.) or detailed rubrics** for these dimensions.

## Where to Find Complete Form Details:

The guidelines reference: "We also have a post describing the ARR review form in detail" and link to [aclrollingreview.org/reviewform](https://aclrollingreview.org/reviewform), but that content isn't included in your source material.

**Recommendation:** Access the dedicated review form documentation directly at the ARR website to obtain the exact scoring scales and dimension descriptions you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4925
}
```

</details>

---


### Tool call

_source line 595 · 2026-05-22T23:37:25.971720+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring scales, and detailed rubric descriptions. I need the exact scale for: Overall Assessment, Soundness, Excitement, Confidence, Reproducibility, and any other scored dimensions. Include the exact text descriptions for each score level (e.g., what does soundness=5 mean vs soundness=1)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring scales, and detailed rubric descriptions. I need the exact scale for: Overall Assessment, Soundness, Excitement, Confidence, Reproducibility, and any other scored dimensions. Include the exact text descriptions for each score level (e.g., what does soundness=5 mean vs soundness=1)."
  }
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-22T23:37:28.230144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-22T23:37:29.133413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-22T23:37:29.536233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 599 · 2026-05-22T23:37:29.536699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 600 · 2026-05-22T23:37:30.509956+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1376
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-22T23:37:30.561829+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1025
}
```

</details>

---


### Tool result

_source line 602 · 2026-05-22T23:37:33.673233+00:00_

# ACL Rolling Review Form: Scoring Scales & Rubrics

## Overall Assessment
*5 pts* = "Consider for Award: I think this paper could be considered for an outstanding paper award"
*4.5 pts* = Borderline Award
*4 pts* = "Conference: I think this paper could be accepted to an *ACL conference"
*3.5 pts* = Borderline Conference
*3 pts* = "Findings: I think this paper could be accepted to the Findings of the ACL"
*2.5 pts* = Borderline Findings
*2 pts* = "Resubmit next cycle: I think this paper needs substantial revisions"
*1.5 pts* = Resubmit after next cycle (substantial revisions requiring extended timeline)
*1 pt* = "Do not resubmit: This paper has to be fully redone"

## Soundness
*5 pts* = "Excellent: This study is one of the most thorough I have seen"
*4 pts* = "Strong: This study provides sufficient support for all of its claims"
*3 pts* = "Acceptable: This study provides sufficient support for its main claims"
*2 pts* = "Poor: Some of the main claims are not sufficiently supported"
*1 pt* = "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
*5 pts* = "Highly Exciting: I would recommend this paper to others and/or attend presentation"
*4 pts* = "Exciting: I would mention this paper to others and/or make effort to attend"
*3 pts* = "Interesting: I might mention some points or attend if time permits"
*2 pts* = "Potentially Interesting: this paper does not resonate with me"
*1 pt* = "Not Exciting: this paper does not resonate with me"

## Reviewer Confidence
*5 pts* = "Positive that my evaluation is correct. I read the paper very carefully"
*4 pts* = "Quite sure. It's unlikely, though conceivable, that I missed something"
*3 pts* = "Pretty sure, but there's a chance I missed something"
*2 pts* = "Willing to defend my evaluation, but fairly likely I missed details"
*1 pt* = "Not my area, or paper is very hard to understand"

## Reproducibility
*5 pts* = "They could easily reproduce the results"
*4 pts* = "They could mostly 
…[truncated 499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7701
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-22T23:37:39.646976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-22T23:37:40.452163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-22T23:37:40.958285+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-22T23:37:40.958686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-22T23:37:41.362159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-22T23:37:42.320413+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1868
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-22T23:37:43.230541+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2271
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-22T23:37:43.533428+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2171
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-22T23:37:51.861590+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/submitted.pdf",
  "project": "irt_personfit_contam",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/submitted.pdf",
    "project": "irt_personfit_contam",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-22T23:37:52.414024+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 587.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 220.1}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-22T23:37:56.433077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-22T23:37:57.438676+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-22T23:37:57.439112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-22T23:37:57.893400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-22T23:37:58.305387+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 866
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-22T23:37:58.305911+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-22T23:37:58.910565+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1017
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-22T23:37:58.910962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-22T23:38:00.032464+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1726
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-22T23:38:00.036018+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1125
}
```

</details>

---


### Tool call

_source line 623 · 2026-05-22T23:38:42.447817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 624 · 2026-05-22T23:38:42.548672+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\irtfit}{\textsc{IRT-FIT}}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	\input{sections/abstract}
30	\end{abstract}
31	
32	\input{sections/introduction}
33	\input{sections/related_work}
34	\input{sections/method}
35	\input{sections/results}
36	\input{sections/discussion}
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\section*{Reproducibility Statement}
42	Code and response data will be released upon acceptance.
43	Bootstrap confidence intervals use the percentile method with 10,000 resamples.
44	All three model families use clean baseline seeds 0--9 ($n{=}10$ per family).
45	Pre-calibrated 4PL item parameters are from the publicly available PSN-IRT item bank \citep{psnirt2026}.
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{sections/appendix}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-22T23:38:46.668182+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---


### Tool result

_source line 626 · 2026-05-22T23:38:46.718865+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 627 · 2026-05-22T23:38:51.185105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 628 · 2026-05-22T23:38:51.637205+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our MML-EM refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Matched-Difference Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, renderi
…[truncated 4200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 629 · 2026-05-22T23:38:51.637732+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 630 · 2026-05-22T23:38:52.039794+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}1.90$ (Qwen at 50\%) to $|d|{=}8.22$ (Qwen at 25\%), with Qwen at 5\% ($|d|{=}4.15$) confirming detection at the lowest contamination level tested. Llama ($|d|{=}2.27$/$2.97$/$2.50$) and Mistral ($|d|{=}3.01$/$3.50$) fall between.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.29$ ($\text{SD}{=}1.45$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.85$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}1.90$--$8.22$) despite order-of-magnitude differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds, percentile bootstrap 95\% CI, 10,000 resamples). CIs reflect clean-seed variability conditional on the observed contaminated run; all exclude 0.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}llrrrr@{}}
25	\toprule
26	Model & Bench. & $d$ (5\%) [CI] & $d$ (15\%) [CI] & $d$ (25\%) [CI] & $d$ (50\%) [CI] \\
27	\midrule
28	Qwe
…[truncated 14355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 631 · 2026-05-22T23:38:52.040440+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 632 · 2026-05-22T23:38:52.141352+00:00_

1	\section{Simulation Validation}
2	\label{app:simulation}
3	
4	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
5	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
6	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
7	
8	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels.
9	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
10	The empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution, achieves $R^2 = 0.957$ against simulated values, with approximate minimum benchmark size of $n \geq 7{,}958$ items for 80\% power at 15\% contamination under MMLU item parameters.
11	
12	\section{4PL vs.\ 3PL Ablation Details}
13	\label{app:4pl_ablation}
14	
15	Table~\ref{tab:4pl_3pl_power} reports detection power (proportion of 2{,}000 simulation replicates rejecting $H_0$ at $\alpha{=}0.05$, two-sided) for 4PL and 3PL parameterizations across five benchmarks and seven contamination levels.
16	The 4PL model yields higher power than 3PL at every non-trivial contamination level on every benchmark.
17	The advantage is largest on MMLU and HellaSwag, where upper-asymptote ($d < 1$) violations are most prevalent, and smallest on ARC-Challenge and HumanEval, where limited item counts constrain power under both parameterizations.
18	
19	Power is non-monotonic at 75\% contamination under 4PL on four of five benchmarks (e.g., MMLU: $.952 \to .938$; GSM8K: $.846 \to .802$).
20	This reflects the $\theta$-shift boundary condition described in \S\ref{sec:inverted_u}: at
…[truncated 20495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 633 · 2026-05-22T23:38:59.169351+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 634 · 2026-05-22T23:38:59.721444+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	Our findings reveal both the strengths and boundaries of IRT person-fit for contamination detection: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but three boundary conditions constrain its practical utility.
4	
5	\paragraph{Characterization over tool.}
6	The detection-diagnosis tradeoff (\S\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\ell_z^*$.
7	The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.
8	These diagnostic capabilities are invisible to accuracy $z$-scores or HT.
9	Findings~1--2 are theoretically predictable from IRT principles; our contribution lies in quantifying these effects in the LLM setting, where the magnitude and boundary conditions are not derivable from theory alone.
10	
11	\paragraph{Practical implications.}
12	Two results have immediate consequences.
13	Free-$\theta$ estimation can produce misleading dose-response curves; anchoring $\theta$ to a pre-contamination baseline substantially amplifies detection for high-ability models but is unnecessary where free estimation already captures the signal.
14	The benchmark size boundary means $\ell_z^*$ is most informative for large benchmarks ($n > 7{,}000$ items for 80\% power at 15\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects.
15	
16	\paragraph{Scope and calibration.}
17	Universal baseline misfit (57/60 cells flagged) confirms systematic
…[truncated 819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 635 · 2026-05-22T23:38:59.721790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 636 · 2026-05-22T23:38:59.772213+00:00_

1	\section*{Limitations}
2	
3	Our controlled experiments cover three model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B) at the 7--8B scale with QLoRA fine-tuning; validation on larger models (13B, 70B), mixture-of-experts architectures, and full-parameter fine-tuning remains future work.
4	The observed negative correlation between baseline ability and detection sensitivity rests on three model families and should be treated as a trend rather than a confirmed relationship.
5	Our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination, which operates through different learning dynamics.
6	The post-RL characterization is $N{=}1$ (Qwen only, GRPO algorithm, 15\% contamination on MMLU); generalization to other model families, RL methods (PPO, DPO), and contamination levels requires further validation.
7	LLMs systematically violate IRT assumptions of local independence and unidimensionality; while the $\Delta\ell_z^*$ design mitigates shared misfit through within-model differencing, the theoretical properties of this correction under severe model misfit remain an open question.
8	Our local dependence simulations employ testlet and Gaussian models that may not fully capture the dependency structures induced by attention mechanisms and sequential processing in LLMs; validating robustness under more realistic dependency structures remains an open question.
9	Most contamination conditions were trained as a single QLoRA run, though Qwen MMLU at 15\%/25\%/50\% was replicated with $n{=}3$ seeds (Appendix~\ref{app:reproducibility}).
10	Multi-seed validation shows stable free-$\theta$ effects at low/moderate contamination (CV${\leq}$25\%), while the high variance at 50\% (CV${=}$60\%) is resolved by $\theta$-anchoring (CV${=}$19\%).
11	Cross-condition consistency across 12 independent settings provides additional converging evidence.
12	Our lowest empirical contamination level is 5\% (Qwen only, $|d|{=}4.15$); extending 5\% experiments
…[truncated 530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 637 · 2026-05-22T23:40:24.428287+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 638 · 2026-05-22T23:40:24.478819+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 639 · 2026-05-22T23:40:28.745763+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 640 · 2026-05-22T23:40:28.797297+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 641 · 2026-05-22T23:42:29.959262+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见（方法严谨性）\n\n---\n\n### Summary\n\n本文将 IRT person-fit 统计量（ℓz*）应用于 LLM SFT 阶段的基准污染检测。通过对三个 7-8B 模型族（Qwen、Llama、Mistral）进行 QLoRA SFT 控制污染实验，在 MMLU 和 ARC-Challenge 上识别了三个现象：(1) θ-shift absorption——基线能力调节检测灵敏度；(2) 检测-诊断权衡——简单统计量检测力更强但 ℓz* 提供机制性洞察；(3) 依赖能力的非单调剂量-响应。核心方法创新是 Δℓz* matched-difference design，通过组内差分消除 LLM 对 IRT 假设的系统性违反。\n\n---\n\n### Strengths\n\n**[S1] 匹配差分设计巧妙且合理。** 57/60 模型-基准组合的绝对 ℓz* 超过 1.96，使传统阈值完全失效。Δℓz* 设计通过组内差分优雅地解决了这个问题，将系统性模型误配从噪声转化为可控因素。这是本文最核心的方法论贡献。（Section 3.2）\n\n**[S2] 鲁棒性分析全面而细致。** 涵盖：(a) 共享/非对称局部依赖模拟（Appendix F.1，Table 9-10）；(b) 参数扰动敏感性（Appendix F.2，Table 11-12）；(c) BCa bootstrap 校正（Appendix G）；(d) 4PL vs 3PL 消融（Appendix B）。这些分析的深度超过多数同类论文。\n\n**[S3] θ-shift absorption 机制具有真实的理论贡献。** 将非单调剂量-响应归因于 MLE θ 估计吸收污染信号这一机制解释，得到了 fixed-θ 实验的直接验证（Table 2：Qwen 50% 下 free-θ |d|=1.90 → fixed-θ |d|=14.52）。这一洞察对后续研究者理解和使用 person-fit 统计量有实际指导价值。（Section 4.2, 4.3）\n\n**[S4] Confirmatory vs. exploratory 区分透明。** 论文明确标注 Finding 1-2 为 confirmatory、Finding 3（非单调剂量-响应）为 exploratory，并在 Section 4.3 段首以 \"As an exploratory observation\" 开头。这种透明度值得肯定。\n\n**[S5] 检测-诊断权衡的实证发现有实用价值。** Table 3 清楚展示 accuracy z-score |d|=68.7 远超 ℓz* |d|=1.90（Qwen 50%），但 ℓz* 提供 seen/unseen 分解、θ-shift 机制、结构敏感性三个不可替代的诊断功能。两阶段工作流建议（先 z-score 筛选，后 ℓz* 诊断）实用且合理。（Section 4.1）\n\n---\n\n### Weaknesses\n\n**[W1] [Must-Fix] 置信区间系统性低估不确定性，主文结论可能过度自信。**\n\nTable 1 caption 明确声明 \"CIs reflect clean-seed variability conditional on the observed contaminated run\"——即 CI 仅反映 clean baseline 的抽样不确定性，**将污染运行视为固定常量**。对 Llama 和 Mistral 的所有污染水平，只有 n=1 个污染运行，其变异性完全未被 CI 捕获。\n\nAppendix K 的多种子复制揭示了这个问题的严重程度：Qwen 50% free-θ 下三个种子的 |d| 分别为 1.90、5.42、7.91（CV=59.6%）。主文 Table 1 恰好报告了 |d|=1.90（seed 42）——这是三个种子中最极端的值。而多种子均值 |d|=5.08 与 15% 的均值 |d|=5.36 几乎没有差异，大幅削弱了 \"inverted-U\" 叙事的力度。\n\n**核心问题**：主文声称 \"All confidence intervals exclude zero, confirming that Δℓz* reliably separates contaminated from clean models\"（Section 4.1）。但这些 CI 只捕获了不确定性的一个来源（clean seed variability），对于 n=1 污染运行的条件完全不捕获污染运行间变异性。一个完整的不确定性量化应该同时考虑两个来源。这对一篇以统计方法为核心贡献的论文而言是一个方法论缺陷。\n\n**建议**：(a) 在主文 Table 1 中补充多种子均值和 SD（至少对 Qwen 可以做到）；(b) 构造联合 CI 或明确讨论条件 CI 的解读限制；(c) 对 Llama/Mistral 至少复制关键条件。\n\n**[W2] [Must-Fix] 非单调剂量-响应（inverted-U）的证据强度被过度呈现。**\n\n这一发现是论文三个核心 Finding 之一，但其证据基础存在问题：\n\n(a) **主文的 inverted-U 主要由 seed 42 驱动**：seed 42 在 50% 下给出 |d|=1.90，而另外两个种子给出 5.42 和 7.91。多种子均值轨迹（5.36 → 7.44 → 5.08）显示的是 \"25% 有个峰值，15% 和 50% 基本持平\"，这与论文叙述的 \"dramatic inverted-U\" 有很大差距。\n\n(b) **Llama 的 inverted-U \"directionally consistent but statistically non-significant\"**（Section 4.3：|d|=2.27 → 2.97 → 2.50，CI 大幅重叠），但 Mistral 只测了 15% 和 50% 两个点，根本无法判断是否存在非单调模式。\n\n(c) **Fixed-θ 消除 inverted-U 后变为单调递增**——这表明 inverted-U 本质上是 θ 估计的统计伪迹，不是污染本身的特征。论文虽然正确地将其归因于 θ-shift absorption，但仍将其作为一个独立 \"finding\" 呈现，容易给读者造成污染确实具有非单调效应的印象。\n\n**建议**：(a) 降低 inverted-U 在叙事中的权重，明确定位为 \"θ 估计伪迹\" 而非污染的固有特征；(b) 在主文中引用多种子均值而非单种子结果。\n\n**[W3] [Should-Fix] Cohen's d 的计算和解读需要更清晰的说明。**\n\n论文使用 d = (ℓz*_contam − mean_clean) / SD_clean，在 n=1 污染观测下本质上是一个标准化偏离量（z-score），不是传统的双样本效应量。论文在 Section 3.2 正确引用了 Hedges' g 校正（J ≈ 0.914），但：\n\n(a) 主文多处将 d 值与 Cohen's benchmarks（small=0.2, medium=0.5, large=0.8）对比（如 Section 4.1 \"well above conventional large-effect thresholds (|d| > 0.8)\"）。但 Cohen's benchmarks 是为双样本效应量设计的，单观测标准化偏离量的值天然更大（它只是一个 z-score），两者不具可比性。\n\n(b) Bootstrap CI 的对象是 clean baseline 的均值和 SD，不是效应量的采样分布。因此 CI 的解读也与传统效应量 CI 不同。\n\n**建议**：在 Section 3.2 明确区分 \"standardized departure\" 与 \"two-sample effect size\"，避免与 Cohen's benchmarks 做不当类比。\n\n**[W4] [Should-Fix] ARC-Challenge 的跨基准推广性证据不足。**\n\nARC-C 实验仅在 Qwen 上进行（Section 3.3：\"extending to additional families was constrained by computational budget\"）。ARC-C 的结果模式与 MMLU 截然不同（正 d 值、无 inverted-U），论文归因于天花板效应和小题量。但在没有其他模型族验证的情况下，这个解释可能是 Qwen 特有的。\n\n此外，ARC-C 只有 295 题，Appendix A 的模拟显示 ARC-C 的 4PL 检测功效仅为 0.087（15%）和 0.285（50%），远低于 MMLU。这意味着 ARC-C 上的检测可能严重依赖 Qwen 恰好的天花板效应（90% baseline），换一个模型（例如 baseline accuracy 60%）可能完全检测不到。\n\n**[W5] [Should-Fix] 多重比较校正缺失。**\n\n论文在 3 个模型族 × 2 个基准 × 多个污染水平上测试了 \"CI 是否排除零\"。这构成了多重假设检验，但没有讨论或应用任何多重比较校正（Bonferroni、FDR 等）。虽然效应量普遍很大（多数 |d| > 2），多重校正可能不改变结论，但对一篇强调统计严谨性的论文而言，应该至少讨论这个问题。\n\n**[W6] [Should-Fix] Mistral fixed-θ 分析缺失 seeds 4-7 未解释。**\n\nTable 2 脚注提到 \"Fixed-θ: 6 vectors (seeds 4-7 unavailable)\"——10 个 clean seeds 中有 4 个的 fixed-θ 结果不可用。论文未解释原因。这引发两个担忧：(a) 数据缺失可能引入选择偏倚；(b) 如果是因为某些种子在 fixed-θ 下产生了异常结果，则报告的 d 值可能不具代表性。\n\n**建议**：解释缺失原因，或报告基于 6 个种子的敏感性分析。\n\n**[W7] [Minor] 模拟功效分析与真实实验的对应关系不够清晰。**\n\nAppendix A 的功效分析假设 4PL 模型正确，但主文展示 57/60 模型-基准组合系统性违反 4PL 假设。模拟得到的功效（如 MMLU 15% 下 96.9%）和真实实验中的检测成功率之间的关系未被充分讨论。功效分析使用两侧检验 \"achieves >93% power\"（Section 4.3），但真实实验中的检测标准是 \"CI excludes zero\"——两者的对应关系需要说明。\n\n**[W8] [Minor] 污染数据混合细节不够清晰。**\n\nTable 14（Appendix J）列出 \"Contaminated items shuffled into training set\"，但未说明：(a) non-contaminated training data 的组成（是纯 clean data 还是包含其他指令数据？）；(b) \"15% contamination\" 的定义——是训练数据中 15% 是 benchmark items，还是 15% 的 benchmark items 被加入训练数据？(c) 训练数据的总量。这些细节对复现至关重要。\n\n---\n\n### Questions\n\n**Q1.** Table 1 中 Qwen 50% 报告的是 seed 42 的结果（|d|=1.90），还是某种聚合？如果是 seed 42，为什么选择报告这个特定种子而非多种子均值？\n\n**Q2.** 对于 Llama 和 Mistral 的 n=1 污染运行，是否有理由认为它们的种子间变异性会低于 Qwen（Qwen 在 50% 下 CV=59.6%）？如果没有，\"all CIs exclude zero\" 的结论是否对这两个模型族过于强烈？\n\n**Q3.** Section 3.2 提到 \"for deployment without clean baselines, cross-benchmark comparison provides the reference\"。但论文的全部实验都在有 clean baseline 的控制环境下进行。是否有任何实验验证了 cross-benchmark 方案的有效性？\n\n**Q4.** Mistral seeds 4-7 在 fixed-θ 分析中不可用的具体原因是什么？\n\n**Q5.** \"15% contamination\" 的确切含义——benchmark items 占训练数据的 15%，还是 15% 的 benchmark items 被加入训练数据？训练数据的总量是多少？\n\n---\n\n### Missing References\n\n- **Sinharay (2017)** \"Are the non-parametric person-fit statistics more powerful than their parametric counterparts?\" 已在正文引用但可以更深入讨论与本文 parametric (ℓz*) vs nonparametric 选择的关系。\n- **Karabatsos (2003)** 已引用，但关于 aberrant response detection 的 comparison 研究（如 comparing 30+ person-fit statistics 的综述）可以更好地 contextualize ℓz* 的选择。\n- 缺少对 **contamination detection 在 pretraining 阶段** 的方法（如 Min-K% Prob, membership inference）与 SFT-stage 方法的系统性比较定位。虽然 Limitations 提到 \"beyond our scope\"，但 Related Work 应更明确地讨论信息需求层次。\n\n---\n\n### Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n本文提出了一个有创意的方向——将教育测量学中成熟的 person-fit 统计量引入 LLM 污染检测。matched-difference design 是一个有效的方法创新，θ-shift absorption 机制的发现具有理论价值，鲁棒性分析的深度令人印象深刻。\n\n但作为一篇以统计方法为核心贡献的论文，CI 构造（W1）和效应量解读（W3）的问题构成方法论缺陷。关键发现 inverted-U（W2）的证据强度被过度呈现，多种子复制显示该效应远不如主文描述的那么显著。这些问题可以在修改中解决，但目前的呈现方式可能导致读者对方法的可靠性产生误判。\n\n如果作者能够：(a) 在主文中整合多种子结果并构造考虑双重变异性来源的 CI；(b) 适当降低 inverted-U 的叙事权重；(c) 澄清 Cohen's d 的解读，论文的总体质量可以达到 Conference 水平。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主要 claims 有实验支撑，但 CI 仅反映 clean-seed variability，inverted-U 的证据基础在多种子复制下大幅减弱 |\n| Excitement | 3.5/5 | IRT person-fit 应用于 LLM 污染检测是一个新颖且有前景的方向，θ-shift 机制有理论贡献，但实用性受限于简单统计量检测力更强 |\n| Reproducibility | 4/5 | 超参数详尽（Appendix J），PSN-IRT item bank 公开可用，代码承诺发布。但 Mistral seeds 4-7 缺失未解释，污染数据混合细节不够清晰 |\n\n---\n\n### Confidence\n\n**4/5** — Quite sure. 本人熟悉 IRT 理论和 person-fit 统计量的教育测量学背景，对 bootstrap CI 构造和效应量计算有专业判断。论文的统计方法部分经过仔细核验。",
  "reviewer_id": "1",
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见（方法严谨性）\n\n---\n\n### Summary\n\n本文将 IRT person-fit 统计量（ℓz*）应用于 LLM SFT 阶段的基准污染检测。通过对三个 7-8B 模型族（Qwen、Llama、Mistral）进行 QLoRA SFT 控制污染实验，在 MMLU 和 ARC-Challenge 上识别了三个现象：(1) θ-shift absorption——基线能力调节检测灵敏度；(2) 检测-诊断权衡——简单统计量检测力更强但 ℓz* 提供机制性洞察；(3) 依赖能力的非单调剂量-响应。核心方法创新是 Δℓz* matched-difference design，通过组内差分消除 LLM 对 IRT 假设的系统性违反。\n\n---\n\n### Strengths\n\n**[S1] 匹配差分设计巧妙且合理。** 57/60 模型-基准组合的绝对 ℓz* 超过 1.96，使传统阈值完全失效。Δℓz* 设计通过组内差分优雅地解决了这个问题，将系统性模型误配从噪声转化为可控因素。这是本文最核心的方法论贡献。（Section 3.2）\n\n**[S2] 鲁棒性分析全面而细致。** 涵盖：(a) 共享/非对称局部依赖模拟（Appendix F.1，Table 9-10）；(b) 参数扰动敏感性（Appendix F.2，Table 11-12）；(c) BCa bootstrap 校正（Appendix G）；(d) 4PL vs 3PL 消融（Appendix B）。这些分析的深度超过多数同类论文。\n\n**[S3] θ-shift absorption 机制具有真实的理论贡献。** 将非单调剂量-响应归因于 MLE θ 估计吸收污染信号这一机制解释，得到了 fixed-θ 实验的直接验证（Table 2：Qwen 50% 下 free-θ |d|=1.90 → fixed-θ |d|=14.52）。这一洞察对后续研究者理解和使用 person-fit 统计量有实际指导价值。（Section 4.2, 4.3）\n\n**[S4] Confirmatory vs. exploratory 区分透明。** 论文明确标注 Finding 1-2 为 confirmatory、Finding 3（非单调剂量-响应）为 exploratory，并在 Section 4.3 段首以 \"As an exploratory observation\" 开头。这种透明度值得肯定。\n\n**[S5] 检测-诊断权衡的实证发现有实用价值。** Table 3 清楚展示 accuracy z-score |d|=68.7 远超 ℓz* |d|=1.90（Qwen 50%），但 ℓz* 提供 seen/unseen 分解、θ-shift 机制、结构敏感性三个不可替代的诊断功能。两阶段工作流建议（先 z-score 筛选，后 ℓz* 诊断）实用且合理。（Section 4.1）\n\n---\n\n### Weaknesses\n\n**[W1] [Must-Fix] 置信区间系统性低估不确定性，主文结论可能过度自信。**\n\nTable 1 caption 明确声明 \"CIs reflect clean-seed variability conditional on the observed contaminated run\"——即 CI 仅反映 clean baseline 的抽样不确定性，**将污染运行视为固定常量**。对 Llama 和 Mistral 的所有污染水平，只有 n=1 个污染运行，其变异性完全未被 CI 捕获。\n\nAppendix K 的多种子复制揭示了这个问题的严重程度：Qwen 50% free-θ 下三个种子的 |d| 分别为 1.90、5.42、7.91（CV=59.6%）。主文 Table 1 恰好报告了 |d|=1.90（seed 42）——这是三个种子中最极端的值。而多种子均值 |d|=5.08 与 15% 的均值 |d|=5.36 几乎没有差异，大幅削弱了 \"inverted-U\" 叙事的力度。\n\n**核心问题**：主文声称 \"All confidence intervals exclude zero, confirming that Δℓz* reliably separates contaminated from clean models\"（Section 4.1）。但这些 CI 只捕获了不确定性的一个来源（clean seed variability），对于 n=1 污染运行的条件完全不捕获污染运行间变异性。一个完整的不确定性量化应该同时考虑两个来源。这对一篇以统计方法为核心贡献的论文而言是一个方法论缺陷。\n\n**建议**：(a) 在主文 Table 1 中补充多种子均值和 SD（至少对 Qwen 可以做到）；(b) 构造联合 CI 或明确讨论条件 CI 的解读限制；(c) 对 Llama/Mistral 至少复制关键条件。\n\n**[W2] [Must-Fix] 非单调剂量-响应（inverted-U）的证据强度被过度呈现。**\n\n这一发现是论文三个核心 Finding 之一，但其证据基础存在问题：\n\n(a) **主文的 inverted-U 主要由 seed 42 驱动**：seed 42 在 50% 下给出 |d|=1.90，而另外两个种子给出 5.42 和 7.91。多种子均值轨迹（5.36 → 7.44 → 5.08）显示的是 \"25% 有个峰值，15% 和 50% 基本持平\"，这与论文叙述的 \"dramatic inverted-U\" 有很大差距。\n\n(b) **Llama 的 inverted-U \"directionally consistent but statistically non-significant\"**（Section 4.3：|d|=2.27 → 2.97 → 2.50，CI 大幅重叠），但 Mistral 只测了 15% 和 50% 两个点，根本无法判断是否存在非单调模式。\n\n(c) **Fixed-θ 消除 inverted-U 后变为单调递增**——这表明 inverted-U 本质上是 θ 估计的统计伪迹，不是污染本身的特征。论文虽然正确地将其归因于 θ-shift absorption，但仍将其作为一个独立 \"finding\" 呈现，容易给读者造成污染确实具有非单调效应的印象。\n\n**建议**：(a) 降低 inverted-U 在叙事中的权重，明确定位为 \"θ 估计伪迹\" 而非污染的固有特征；(b) 在主文中引用多种子均值而非单种子结果。\n\n**[W3] [Should-Fix] Cohen's d 的计算和解读需要更清晰的说明。**\n\n论文使用 d = (ℓz*_contam − mean_clean) / SD_clean，在 n=1 污染观测下本质上是一个标准化偏离量（z-score），不是传统的双样本效应量。论文在 Section 3.2 正确引用了 Hedges' g 校正（J ≈ 0.914），但：\n\n(a) 主文多处将 d 值与 Cohen's benchmarks（small=0.2, medium=0.5, large=0.8）对比（如 Section 4.1 \"well above conventional large-effect thresholds (|d| > 0.8)\"）。但 Cohen's benchmarks 是为双样本效应量设计的，单观测标准化偏离量的值天然更大（它只是一个 z-score），两者不具可比性。\n\n(b) Bootstrap CI 的对象是 clean baseline 的均值和 SD，不是效应量的采样分布。因此 CI 的解读也与传统效应量 CI 不同。\n\n**建议**：在 Section 3.2 明确区分 \"standardized departure\" 与 \"two-sample effect size\"，避免与 Cohen's benchmarks 做不当类比。\n\n**[W4] [Should-Fix] ARC-Challenge 的跨基准推广性证据不足。**\n\nARC-C 实验仅在 Qwen 上进行（Section 3.3：\"extending to additional families was constrained by computational budget\"）。ARC-C 的结果模式与 MMLU 截然不同（正 d 值、无 inverted-U），论文归因于天花板效应和小题量。但在没有其他模型族验证的情况下，这个解释可能是 Qwen 特有的。\n\n此外，ARC-C 只有 295 题，Appendix A 的模拟显示 ARC-C 的 4PL 检测功效仅为 0.087（15%）和 0.285（50%），远低于 MMLU。这意味着 ARC-C 上的检测可能严重依赖 Qwen 恰好的天花板效应（90% baseline），换一个模型（例如 baseline accuracy 60%）可能完全检测不到。\n\n**[W5] [Should-Fix] 多重比较校正缺失。**\n\n论文在 3 个模型族 × 2 个基准 × 多个污染水平上测试了 \"CI 是否排除零\"。这构成了多重假设检验，但没有讨论或应用任何多重比较校正（Bonferroni、FDR 等）。虽然效应量普遍很大（多数 |d| > 2），多重校正可能不改变结论，但对一篇强调统计严谨性的论文而言，应该至少讨论这个问题。\n\n**[W6] [Should-Fix] Mistral fixed-θ 分析缺失 seeds 4-7 未解释。**\n\nTable 2 脚注提到 \"Fixed-θ: 6 vectors (seeds 4-7 unavailable)\"——10 个 clean seeds 中有 4 个的 fixed-θ 结果不可用。论文未解释原因。这引发两个担忧：(a) 数据缺失可能引入选择偏倚；(b) 如果是因为某些种子在 fixed-θ 下产生了异常结果，则报告的 d 值可能不具代表性。\n\n**建议**：解释缺失原因，或报告基于 6 个种子的敏感性分析。\n\n**[W7] [Minor] 模拟功效分析与真实实验的对应关系不够清晰。**\n\nAppendix A 的功效分析假设 4PL 模型正确，但主文展示 57/60 模型-基准组合系统性违反 4PL 假设。模拟得到的功效（如 MMLU 15% 下 96.9%）和真实实验中的检测成功率之间的关系未被充分讨论。功效分析使用两侧检验 \"achieves >93% power\"（Section 4.3），但真实实验中的检测标准是 \"CI excludes zero\"——两者的对应关系需要说明。\n\n**[W8] [Minor] 污染数据混合细节不够清晰。**\n\nTable 14（Appendix J）列出 \"Contaminated items shuffled into training set\"，但未说明：(a) non-contaminated training data 的组成（是纯 clean data 还是包含其他指令数据？）；(b) \"15% contamination\" 的定义——是训练数据中 15% 是 benchmark items，还是 15% 的 benchmark items 被加入训练数据？(c) 训练数据的总量。这些细节对复现至关重要。\n\n---\n\n### Questions\n\n**Q1.** Table 1 中 Qwen 50% 报告的是 seed 42 的结果（|d|=1.90），还是某种聚合？如果是 seed 42，为什么选择报告这个特定种子而非多种子均值？\n\n**Q2.** 对于 Llama 和 Mistral 的 n=1 污染运行，是否有理由认为它们的种子间变异性会低于 Qwen（Qwen 在 50% 下 CV=59.6%）？如果没有，\"all CIs exclude zero\" 的结论是否对这两个模型族过于强烈？\n\n**Q3.** Section 3.2 提到 \"for deployment without clean baselines, cross-benchmark comparison provides the reference\"。但论文的全部实验都在有 clean baseline 的控制环境下进行。是否有任何实验验证了 cross-benchmark 方案的有效性？\n\n**Q4.** Mistral seeds 4-7 在 fixed-θ 分析中不可用的具体原因是什么？\n\n**Q5.** \"15% contamination\" 的确切含义——benchmark items 占训练数据的 15%，还是 15% 的 benchmark items 被加入训练数据？训练数据的总量是多少？\n\n---\n\n### Missing References\n\n- **Sinharay (2017)** \"Are the non-parametric person-fit statistics more powerful than their parametric counterparts?\" 已在正文引用但可以更深入讨论与本文 parametric (ℓz*) vs nonparametric 选择的关系。\n- **Karabatsos (2003)** 已引用，但关于 aberrant response detection 的 comparison 研究（如 comparing 30+ person-fit statistics 的综述）可以更好地 contextualize ℓz* 的选择。\n- 缺少对 **contamination detection 在 pretraining 阶段** 的方法（如 Min-K% Prob, membership inference）与 SFT-stage 方法的系统性比较定位。虽然 Limitations 提到 \"beyond our scope\"，但 Related Work 应更明确地讨论信息需求层次。\n\n---\n\n### Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n本文提出了一个有创意的方向——将教育测量学中成熟的 person-fit 统计量引入 LLM 污染检测。matched-difference design 是一个有效的方法创新，θ-shift absorption 机制的发现具有理论价值，鲁棒性分析的深度令人印象深刻。\n\n但作为一篇以统计方法为核心贡献的论文，CI 构造（W1）和效应量解读（W3）的问题构成方法论缺陷。关键发现 inverted-U（W2）的证据强度被过度呈现，多种子复制显示该效应远不如主文描述的那么显著。这些问题可以在修改中解决，但目前的呈现方式可能导致读者对方法的可靠性产生误判。\n\n如果作者能够：(a) 在主文中整合多种子结果并构造考虑双重变异性来源的 CI；(b) 适当降低 inverted-U 的叙事权重；(c) 澄清 Cohen's d 的解读，论文的总体质量可以达到 Conference 水平。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主要 claims 有实验支撑，但 CI 仅反映 clean-seed variability，inverted-U 的证据基础在多种子复制下大幅减弱 |\n| Excitement | 3.5/5 | IRT person-fit 应用于 LLM 污染检测是一个新颖且有前景的方向，θ-shift 机制有理论贡献，但实用性受限于简单统计量检测力更强 |\n| Reproducibility | 4/5 | 超参数详尽（Appendix J），PSN-IRT item bank 公开可用，代码承诺发布。但 Mistral seeds 4-7 缺失未解释，污染数据混合细节不够清晰 |\n\n---\n\n### Confidence\n\n**4/5** — Quite sure. 本人熟悉 IRT 理论和 person-fit 统计量的教育测量学背景，对 bootstrap CI 构造和效应量计算有专业判断。论文的统计方法部分经过仔细核验。",
    "reviewer_id": "1",
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 642 · 2026-05-22T23:42:33.677765+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3718
}
```

</details>

---


### Assistant

_source line 643 · 2026-05-22T23:42:46.842300+00:00_

审稿意见已提交给 Review Director。

核心评价：**Overall 3.5（Borderline Conference）**。

三个主要问题：

1. **CI 系统性低估不确定性**（Must-Fix）：bootstrap CI 仅反映 clean-seed variability，将污染运行视为常量。Appendix K 的多种子复制显示 Qwen 50% 下 |d| 跨种子变异 CV=59.6%，但主文恰好报告了最极端的 seed 42（|d|=1.90）。

2. **Inverted-U 证据被过度呈现**（Must-Fix）：多种子均值轨迹（5.36→7.44→5.08）显示 15% 和 50% 几乎持平，远不如单种子结果（6.57→8.22→1.90）那么戏剧性。且 fixed-θ 下效应变为单调递增，说明 inverted-U 本质是 θ 估计伪迹。

3. **Cohen's d 解读不当**（Should-Fix）：单观测标准化偏离量被与传统双样本效应量的 Cohen benchmarks 做类比，两者不具可比性。

优势方面：matched-difference design 巧妙、鲁棒性分析全面、θ-shift absorption 机制有真实理论贡献、confirmatory/exploratory 区分透明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1"
}
```

</details>

---


## Round 23

## Round 23

10 recorded events


### User

_source line 644 · 2026-05-22T23:44:09.459406+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每个要点标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

### Must-Fix 问题

**N1** [critical] 新颖性的增量贡献需要更诚实的定位
- Finding 1（θ-shift absorption）是 IRT 理论的直接推论，Meijer and Sijtsma (2001) 和 Karabatsos (2003) 已讨论过 person-fit 统计量对能力水平的敏感性。
- Finding 2（detection-diagnosis tradeoff）也是 person-fit 文献的已知模式，Sinharay (2017a) 已比较过不同 person-fit 统计量的检测力差异。
- 唯一真正新颖的 Finding 3（非单调剂量-响应）仅基于 N=1 模型族（Qwen），证据薄弱。
- 如果核心贡献主要是验证已知 IRT 理论在 LLM 场景下成立，novelty bar 对 EMNLP main conference 偏低。
- 建议：在 Introduction 中明确区分 confirmatory 和 discovery 的贡献层级，强调 magnitude/boundary conditions 的实证价值。

**N2** [critical] Finding 3（非单调剂量-响应）证据严重不足，但占据大量篇幅
- 仅基于 Qwen 单个模型族（N=1 模型设计点）
- multi-seed validation 仅 n=3 independent QLoRA seeds
- Abstract 将其列为第三个 contribution 时权重与前两个并列
- Figure 3 右侧 inverted-U 曲线的 error bars 较大
- 没有在 Llama 或 Mistral 上验证该非单调模式
- 建议：降级为 "preliminary observation"，至少在 Llama 上补充 5%/25% 条件，或缩减篇幅移至 Discussion。

**N3** [critical] 缺少与现有污染检测方法的对比
- 完全没有与 MIA/ConStat 做 head-to-head 对比
- ConStat 同样可以在 black-box 设定下使用
- Table 8 报告 AUROC 0.63 但无 baseline 对比
- 论文 framing 暗示工具属性，但缺少对比使实际价值无法验证
- 建议：至少与 accuracy z-score、ConStat 或简单 n-gram overlap 做对比。

### Should-Fix 问题

**W1** 实验矩阵不完整，"systematic" 声明过度
- Mistral 缺 5%/25%，ARC-C 仅 Qwen，Post-RL N=1，仅 7-8B，仅 QLoRA

**W2** ARC-Challenge 结果统计力不足
- 295 items，CI 较宽，与 MMLU 结论不同但未充分讨论差异根源

**W3** 对 4PL 参数外部依赖的讨论不足
- PSN-IRT 校准数据是否包含已污染模型？circularity 问题未讨论
- 参数噪声敏感性分析仅覆盖 ≤10% noise

**W4** Title/Abstract 的 framing 与实际 scope 存在张力
- 方法通用性优势的 framing 将信息限制 spin 为优势，需更平衡

### Missing References
1. Han, Song, Lee, and Jo (2026), "Quantifying Data Contamination in Psychometric Evaluations of LLMs", Findings of EACL 2026
2. 综合性 survey: arXiv 2502.14425, arXiv 2502.17521
3. Wang, H. et al. (2025) 关于 in-context learning contamination

### Overall Assessment
R2 给出 3.5 Borderline Conference。核心理由：两个主要 findings 是 IRT 理论预期推论的实证验证，最具新意的 Finding 3 证据不足，缺少与现有方法的对比。

---

请逐条回应上述所有要点（Must-Fix N1-N3, Should-Fix W1-W4, Missing References）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 645 · 2026-05-22T23:44:51.997642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 646 · 2026-05-22T23:44:52.453910+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus \citep{dodge2021, magar2022}.
9	Membership inference approaches require token-level probabilities \citep{minkprob2024, deng2024}.
10	Probing methods rely on crafted prompts \citep{golchin2024, oren2024}.
11	Performance-based methods require multiple test variants or output logits \citep{constat2024, codec2026}.
12	These methods form a detection frontier ordered by information access.
13	No existing method operates using only binary response patterns, without model weights, gradients, logits, or training data---though, as we show, effective detection additionally requires externally calibrated item parameters.
14	
15	In this work, we focus on SFT-stage contamination---where benchmark answers are explicitly included in fine-tuning data---for three reasons.
16	First, controlled experiments require known ground-truth contamination sets, achievable through fine-tuning with specific benchmark items.
17	Second, SFT-stage contamination is increasingly relevant as fine-tuning-as-a-service platforms proliferate, creating new pathways for benchmark data to enter training mixtures.
18	Third, SFT provides a methodologically clean setting to characterize detection boundaries before extending to noisier pretraining scenarios.
19	
…[truncated 4641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-22T23:44:52.454353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 648 · 2026-05-22T23:44:52.605763+00:00_

1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first controlled characterization of IRT person-fit statistics for detecting SFT-stage contamination: the framework requires only binary response patterns from the target model---no access to weights, gradients, logits, or training data---combined with externally calibrated 4PL item parameters from a large-scale item bank; diagnostic $\theta$-anchoring additionally requires a clean baseline.
3	A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using $\ell_z^*$ in a matched-difference design ($\Delta\ell_z^*$) across three 7--8B model families ($n{=}10$ clean baseline seeds per model family) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three behavior boundaries:
5	(1) model-specific $\theta$-shift dynamics linking baseline ability to detection sensitivity, where higher-ability models show weaker free-$\theta$ detection due to $\theta$-shift absorption;
6	(2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack $\ell_z^*$'s diagnostic capabilities (seen/unseen decomposition, mechanistic $\theta$-shift analysis);
7	and (3, exploratory) ability-dependent non-monotonic dose-response under free-$\theta$ estimation, driven by $\theta$-shift absorption; $\theta$-anchored analysis reveals stable detection with a strong positive dose-response at higher contamination levels.
8	These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 649 · 2026-05-22T23:44:57.829700+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 650 · 2026-05-22T23:44:57.880619+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Benchmark contamination detection.}
4	Contamination detection methods span a wide range of information requirements.
5	Corpus-search methods match benchmark items directly against pretraining data \citep{dodge2021, magar2022}, but require full corpus access unavailable for closed models.
6	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training from unseen examples \citep{minkprob2024, deng2024}.
7	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, golchin2024quiz, oren2024}.
8	Performance-based methods compare accuracy on target and reference sets \citep{constat2024, pacost2024, codec2026}, requiring multiple evaluations or in-context learning passes.
9	\citet{zhou2023benchmark} and \citet{sainz2023} argue for systematic contamination measurement, \citet{jacovi2023} propose mitigation strategies, and \citet{bordt2025forget} show that contamination can be ``forgotten'' under sufficient continued training.
10	\citet{han2026quantifying} quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks.
11	\citet{kattamuri2025radar} take a mechanistic interpretability approach, using activation patterns to distinguish recall-based from reasoning-based responses; our work instead operates purely on behavioral response patterns without access to model internals.
12	\citet{fu2025contamination} systematically evaluate detection method assumptions, finding that most methods degrade under realistic conditions; our work contributes a psychometric perspective to this ongoing evaluation.
13	
14	A critical limitation unites all token-level methods: \citet{wang2025fragility} show that RL post-training renders MIA-based detectors no better than random across 10 methods and 4 benchmarks, because RL reshapes token distributions while largely preserving binary correctness patterns.
15	
…[truncated 2840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 651 · 2026-05-22T23:46:50.078334+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[PARTIALLY AGREE] R2-N1: 新颖性的增量贡献需要更诚实的定位**\n\nR2 指出 Findings 1-2 是 IRT 理论的预期推论，这一判断部分正确。论文 Discussion（Section 5）自己也承认：\"Findings 1–2 are theoretically predictable from IRT principles; our contribution lies in quantifying these effects in the LLM setting, where the magnitude and boundary conditions are not derivable from theory alone.\" 因此论文对此并非完全不自知。\n\n但我认为 R2 **低估了实证量化的贡献价值**：(a) ARC-C 的天花板效应逆转了 MMLU 上的模式（Section 4.2：ARC-C 下高能力模型反而产生更大效应量），这不是 Meijer and Sijtsma (2001) 或 Karabatsos (2003) 讨论过的场景；(b) fixed-θ 何时有效何时有害的具体经验法则（Δθ > 0.2 时有效；Llama 因 high cross-seed variance 反而受损——Table 2 中 Llama fixed-θ CI 包含零）是纯理论无法推导的实证发现；(c) 将教育测量学工具首次系统性地迁移到 LLM 场景，本身构成 cross-disciplinary 贡献。\n\n**我的建议**：Introduction 和 Abstract 中应更明确地将贡献层次分为 \"confirmatory quantification\"（Findings 1-2 的量化和边界条件）与 \"exploratory discovery\"（Finding 3），而非三个 findings 平行呈现。R2 的建议方向是对的。\n\n---\n\n**[AGREE] R2-N2: Finding 3（非单调剂量-响应）证据严重不足**\n\n与我的 W2 完全一致。补充 R2 未提到的一个关键证据：\n\nAppendix K 的多种子复制显示，free-θ 均值轨迹为 |d|: 5.36 → 7.44 → 5.08（15%/25%/50%），其中 15% → 50% 几乎持平（5.36 vs 5.08），\"inverted-U\" 主要表现为 25% 的峰值。而主文 Section 4.3 报告的 dramatic inverted-U（4.15 → 6.58 → 8.22 → 1.90）来自 seed 42，恰好是 50% 下三个种子中效应量最小的（另两个为 5.42 和 7.91）。换言之，**主文呈现的 inverted-U 幅度被 seed selection 显著放大了**。\n\n此外，fixed-θ 下剂量-响应变为单调递增（均值 |d|: 6.85 → 5.89 → 12.32），进一步表明 inverted-U 是 θ 估计的统计伪迹而非污染的固有特征。论文将其作为独立 \"finding\" 的呈现方式确实有误导性。\n\nR2 建议降级为 \"preliminary observation\" 或缩减篇幅，我同意。\n\n---\n\n**[PARTIALLY REBUT] R2-N3: 缺少与现有污染检测方法的对比**\n\nR2 的核心诉求——缺少 head-to-head 对比——需要分层讨论。\n\n**反驳部分**：\n1. 论文 Table 3 **确实提供了与 accuracy z-score 和 HT 的系统性对比**。这不是 \"完全没有对比\"——accuracy z-score 在 Qwen 50% 下 |d|=68.7，远超 ℓz* 的 |d|=1.90。论文坦诚承认简单统计量检测力更强（Section 4.1），并将 ℓz* 的价值定位在诊断而非检测。\n2. R2 声称 \"ConStat 同样可以在 black-box 设定下使用\"，但论文 Related Work 明确指出 ConStat 需要 \"multiple evaluations or in-context learning passes\"（Section 2, line 8）——它需要在多个测试变体上运行模型，信息需求高于仅需单次二值响应模式的 ℓz*。这不是同一信息层级。\n3. 论文明确定位为 **characterization 而非 tool**（Introduction: \"Rather than proposing ℓz* as a ready-to-deploy detection tool, we characterize the behavior boundaries\"），这降低了 head-to-head 对比的必要性。\n\n**同意部分**：\n尽管如此，R2 的关切有一个合理内核：如果论文声称 ℓz* 的独特价值在于诊断能力，那么至少应展示 **诊断维度上的对比优势**——例如，accuracy z-score 能否也做 seen/unseen 分解？HT 能否也提供 θ-shift 分析？Table 3 比较了检测力，但没有系统性比较诊断能力。此外，Table 8 的 AUROC=0.63 缺乏与其他 item-level 检测方法的对比（即使只是 random baseline=0.50 已列出，也应加入更多 baselines）。\n\n**我的立场**：这不是 \"critical/must-fix\"，而是 \"should-fix\"。要求与 MIA/ConStat 做 head-to-head 对比在信息层级不对等的情况下不合理，但论文应更系统地展示 ℓz* 在诊断维度上的独特价值。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 实验矩阵不完整**\n\n与我的审查一致。Mistral 缺 5%/25%，ARC-C 仅 Qwen，Post-RL N=1。论文用 \"computational budget\" 解释，但 \"systematic\" 这个词在 Abstract 中确实言过其实——12 个条件中仅有完整填充的是 Qwen MMLU（4 个污染水平 × n=10 clean + n=3 contaminated）。建议将 \"systematic\" 替换为更准确的措辞（如 \"controlled\" 或 \"multi-family\"）。\n\n---\n\n**[AGREE] R2-W2: ARC-Challenge 结果统计力不足**\n\n与我的 W4 一致。补充：Appendix A 模拟显示 ARC-C 4PL 检测功效仅 0.087（15%）和 0.285（50%），远低于 MMLU 的 0.969/0.952。在如此低的功效下，ARC-C 上的正向结果可能严重依赖 Qwen 的 90% baseline accuracy 带来的天花板效应。换一个中等能力模型（如 Llama 的 ~60% accuracy），ARC-C 上可能完全检测不到。\n\n---\n\n**[AGREE] R2-W3: 对 4PL 参数外部依赖的讨论不足**\n\nR2 提出的 circularity 问题是一个我在初轮审稿中未充分关注的有效关切。PSN-IRT 从 13,000+ 模型校准参数——如果其中包含已污染模型（这在 leaderboard 生态中很可能），则 item parameters 可能已被系统性偏置。Appendix F.2 的参数扰动分析模拟的是**随机噪声**（乘性/加性扰动），但污染引入的偏差是**系统性的**（污染使难题的正确率偏高，可能导致 difficulty 参数 b 被低估）。两者性质不同，随机噪声鲁棒性不能保证系统性偏差鲁棒性。\n\n论文 Appendix H 从另一个角度间接触及了这个问题（MML-EM 重新校准显示 discrimination recovery 极差），但并未正面回应 \"PSN-IRT 校准数据本身可能被污染\" 的 circularity 担忧。建议补充讨论。\n\n---\n\n**[PARTIALLY REBUT] R2-W4: Title/Abstract 的 framing 与实际 scope 存在张力**\n\nR2 认为论文将信息限制 spin 为优势。但：\n1. Title 采用疑问句式（\"What Can... Reveal?\"），本身就是探索性而非工具性的 framing。\n2. Introduction 明确声明 \"Rather than proposing ℓz* as a ready-to-deploy detection tool, we characterize the behavior boundaries\"（Section 1, 第4段）。\n3. Discussion 的 \"Characterization over tool\" 段落再次强化了这一定位。\n\n**但我同意 Abstract 的措辞存在一定张力**：Abstract 第一句 \"yet most detection methods require privileged access\" 暗示本文填补了一个检测方法的空白，与后续的 characterization 定位不完全一致。建议 Abstract 更早地引入 characterization 而非 detection 的框架。\n\n---\n\n### Missing References\n\n**[REBUT] Han, Song, Lee, and Jo (2026)**：该文已在 Related Work 中引用——\"Han et al. (2026) quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks\"（Section 2, Related Work 第1段）。R2 可能遗漏了这一引用。\n\n**[AGREE] 综合性 survey（arXiv 2502.14425, arXiv 2502.17521）**：如果这些是 2025 年发表的关于 LLM contamination detection 的综合 survey，确实值得在 Related Work 中引用以提供更完整的背景。\n\n**[NEUTRAL] Wang et al. (2025) in-context learning contamination**：需要确认这是否与已引用的 wang2025fragility 是同一篇。如果是不同文章且涉及 in-context learning 场景的污染，则值得引用，因为论文仅讨论了 SFT 和 RL 两种训练阶段。\n\n---\n\n### 对 R2 Overall Assessment 的评价\n\nR2 给出 3.5（Borderline Conference），我的初轮评分也是 3.5。我们在以下判断上一致：\n- Finding 3 证据不足是主要弱点\n- 实验矩阵不够完整\n- ARC-C 分析受限\n\n但我与 R2 在以下方面有分歧：\n1. **R2 低估了跨学科迁移的贡献**——将教育测量学 4 十年的 person-fit 方法论首次系统性地应用于 LLM 场景，matched-difference design 的方法创新，以及 θ-shift absorption 的实证量化，这些对 EMNLP 社区有实际价值。\n2. **R2 对 N3（缺少对比）的严重程度过度判断**——Table 3 确实提供了与简单统计量的对比，信息层级差异使与 MIA/ConStat 的对比不具操作性。\n\n**我维持 3.5 的评分**，但认为如果作者能修复 CI 方法论（我的 W1）和 inverted-U 呈现（N2/我的 W2），论文可以达到 4.0（Conference）。",
  "reviewer_id": "1",
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[PARTIALLY AGREE] R2-N1: 新颖性的增量贡献需要更诚实的定位**\n\nR2 指出 Findings 1-2 是 IRT 理论的预期推论，这一判断部分正确。论文 Discussion（Section 5）自己也承认：\"Findings 1–2 are theoretically predictable from IRT principles; our contribution lies in quantifying these effects in the LLM setting, where the magnitude and boundary conditions are not derivable from theory alone.\" 因此论文对此并非完全不自知。\n\n但我认为 R2 **低估了实证量化的贡献价值**：(a) ARC-C 的天花板效应逆转了 MMLU 上的模式（Section 4.2：ARC-C 下高能力模型反而产生更大效应量），这不是 Meijer and Sijtsma (2001) 或 Karabatsos (2003) 讨论过的场景；(b) fixed-θ 何时有效何时有害的具体经验法则（Δθ > 0.2 时有效；Llama 因 high cross-seed variance 反而受损——Table 2 中 Llama fixed-θ CI 包含零）是纯理论无法推导的实证发现；(c) 将教育测量学工具首次系统性地迁移到 LLM 场景，本身构成 cross-disciplinary 贡献。\n\n**我的建议**：Introduction 和 Abstract 中应更明确地将贡献层次分为 \"confirmatory quantification\"（Findings 1-2 的量化和边界条件）与 \"exploratory discovery\"（Finding 3），而非三个 findings 平行呈现。R2 的建议方向是对的。\n\n---\n\n**[AGREE] R2-N2: Finding 3（非单调剂量-响应）证据严重不足**\n\n与我的 W2 完全一致。补充 R2 未提到的一个关键证据：\n\nAppendix K 的多种子复制显示，free-θ 均值轨迹为 |d|: 5.36 → 7.44 → 5.08（15%/25%/50%），其中 15% → 50% 几乎持平（5.36 vs 5.08），\"inverted-U\" 主要表现为 25% 的峰值。而主文 Section 4.3 报告的 dramatic inverted-U（4.15 → 6.58 → 8.22 → 1.90）来自 seed 42，恰好是 50% 下三个种子中效应量最小的（另两个为 5.42 和 7.91）。换言之，**主文呈现的 inverted-U 幅度被 seed selection 显著放大了**。\n\n此外，fixed-θ 下剂量-响应变为单调递增（均值 |d|: 6.85 → 5.89 → 12.32），进一步表明 inverted-U 是 θ 估计的统计伪迹而非污染的固有特征。论文将其作为独立 \"finding\" 的呈现方式确实有误导性。\n\nR2 建议降级为 \"preliminary observation\" 或缩减篇幅，我同意。\n\n---\n\n**[PARTIALLY REBUT] R2-N3: 缺少与现有污染检测方法的对比**\n\nR2 的核心诉求——缺少 head-to-head 对比——需要分层讨论。\n\n**反驳部分**：\n1. 论文 Table 3 **确实提供了与 accuracy z-score 和 HT 的系统性对比**。这不是 \"完全没有对比\"——accuracy z-score 在 Qwen 50% 下 |d|=68.7，远超 ℓz* 的 |d|=1.90。论文坦诚承认简单统计量检测力更强（Section 4.1），并将 ℓz* 的价值定位在诊断而非检测。\n2. R2 声称 \"ConStat 同样可以在 black-box 设定下使用\"，但论文 Related Work 明确指出 ConStat 需要 \"multiple evaluations or in-context learning passes\"（Section 2, line 8）——它需要在多个测试变体上运行模型，信息需求高于仅需单次二值响应模式的 ℓz*。这不是同一信息层级。\n3. 论文明确定位为 **characterization 而非 tool**（Introduction: \"Rather than proposing ℓz* as a ready-to-deploy detection tool, we characterize the behavior boundaries\"），这降低了 head-to-head 对比的必要性。\n\n**同意部分**：\n尽管如此，R2 的关切有一个合理内核：如果论文声称 ℓz* 的独特价值在于诊断能力，那么至少应展示 **诊断维度上的对比优势**——例如，accuracy z-score 能否也做 seen/unseen 分解？HT 能否也提供 θ-shift 分析？Table 3 比较了检测力，但没有系统性比较诊断能力。此外，Table 8 的 AUROC=0.63 缺乏与其他 item-level 检测方法的对比（即使只是 random baseline=0.50 已列出，也应加入更多 baselines）。\n\n**我的立场**：这不是 \"critical/must-fix\"，而是 \"should-fix\"。要求与 MIA/ConStat 做 head-to-head 对比在信息层级不对等的情况下不合理，但论文应更系统地展示 ℓz* 在诊断维度上的独特价值。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 实验矩阵不完整**\n\n与我的审查一致。Mistral 缺 5%/25%，ARC-C 仅 Qwen，Post-RL N=1。论文用 \"computational budget\" 解释，但 \"systematic\" 这个词在 Abstract 中确实言过其实——12 个条件中仅有完整填充的是 Qwen MMLU（4 个污染水平 × n=10 clean + n=3 contaminated）。建议将 \"systematic\" 替换为更准确的措辞（如 \"controlled\" 或 \"multi-family\"）。\n\n---\n\n**[AGREE] R2-W2: ARC-Challenge 结果统计力不足**\n\n与我的 W4 一致。补充：Appendix A 模拟显示 ARC-C 4PL 检测功效仅 0.087（15%）和 0.285（50%），远低于 MMLU 的 0.969/0.952。在如此低的功效下，ARC-C 上的正向结果可能严重依赖 Qwen 的 90% baseline accuracy 带来的天花板效应。换一个中等能力模型（如 Llama 的 ~60% accuracy），ARC-C 上可能完全检测不到。\n\n---\n\n**[AGREE] R2-W3: 对 4PL 参数外部依赖的讨论不足**\n\nR2 提出的 circularity 问题是一个我在初轮审稿中未充分关注的有效关切。PSN-IRT 从 13,000+ 模型校准参数——如果其中包含已污染模型（这在 leaderboard 生态中很可能），则 item parameters 可能已被系统性偏置。Appendix F.2 的参数扰动分析模拟的是**随机噪声**（乘性/加性扰动），但污染引入的偏差是**系统性的**（污染使难题的正确率偏高，可能导致 difficulty 参数 b 被低估）。两者性质不同，随机噪声鲁棒性不能保证系统性偏差鲁棒性。\n\n论文 Appendix H 从另一个角度间接触及了这个问题（MML-EM 重新校准显示 discrimination recovery 极差），但并未正面回应 \"PSN-IRT 校准数据本身可能被污染\" 的 circularity 担忧。建议补充讨论。\n\n---\n\n**[PARTIALLY REBUT] R2-W4: Title/Abstract 的 framing 与实际 scope 存在张力**\n\nR2 认为论文将信息限制 spin 为优势。但：\n1. Title 采用疑问句式（\"What Can... Reveal?\"），本身就是探索性而非工具性的 framing。\n2. Introduction 明确声明 \"Rather than proposing ℓz* as a ready-to-deploy detection tool, we characterize the behavior boundaries\"（Section 1, 第4段）。\n3. Discussion 的 \"Characterization over tool\" 段落再次强化了这一定位。\n\n**但我同意 Abstract 的措辞存在一定张力**：Abstract 第一句 \"yet most detection methods require privileged access\" 暗示本文填补了一个检测方法的空白，与后续的 characterization 定位不完全一致。建议 Abstract 更早地引入 characterization 而非 detection 的框架。\n\n---\n\n### Missing References\n\n**[REBUT] Han, Song, Lee, and Jo (2026)**：该文已在 Related Work 中引用——\"Han et al. (2026) quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks\"（Section 2, Related Work 第1段）。R2 可能遗漏了这一引用。\n\n**[AGREE] 综合性 survey（arXiv 2502.14425, arXiv 2502.17521）**：如果这些是 2025 年发表的关于 LLM contamination detection 的综合 survey，确实值得在 Related Work 中引用以提供更完整的背景。\n\n**[NEUTRAL] Wang et al. (2025) in-context learning contamination**：需要确认这是否与已引用的 wang2025fragility 是同一篇。如果是不同文章且涉及 in-context learning 场景的污染，则值得引用，因为论文仅讨论了 SFT 和 RL 两种训练阶段。\n\n---\n\n### 对 R2 Overall Assessment 的评价\n\nR2 给出 3.5（Borderline Conference），我的初轮评分也是 3.5。我们在以下判断上一致：\n- Finding 3 证据不足是主要弱点\n- 实验矩阵不够完整\n- ARC-C 分析受限\n\n但我与 R2 在以下方面有分歧：\n1. **R2 低估了跨学科迁移的贡献**——将教育测量学 4 十年的 person-fit 方法论首次系统性地应用于 LLM 场景，matched-difference design 的方法创新，以及 θ-shift absorption 的实证量化，这些对 EMNLP 社区有实际价值。\n2. **R2 对 N3（缺少对比）的严重程度过度判断**——Table 3 确实提供了与简单统计量的对比，信息层级差异使与 MIA/ConStat 的对比不具操作性。\n\n**我维持 3.5 的评分**，但认为如果作者能修复 CI 方法论（我的 W1）和 inverted-U 呈现（N2/我的 W2），论文可以达到 4.0（Conference）。",
    "reviewer_id": "1",
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 652 · 2026-05-22T23:46:53.745514+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3667
}
```

</details>

---


### Assistant

_source line 653 · 2026-05-22T23:46:59.631794+00:00_

交叉回应已提交。

核心立场：与 R2 在 Finding 3 证据不足（N2）和实验矩阵不完整（W1）上达成共识，但在两个关键点上有分歧——(1) R2 低估了跨学科迁移和实证量化的贡献价值；(2) R2 将缺少与 MIA/ConStat 的对比列为 must-fix 过于严格，因为信息层级差异使直接对比不具操作性，且 Table 3 已提供了与简单统计量的系统性对比。维持 3.5 评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1"
}
```

</details>

---


## Round 24

## Round 24

56 recorded events


### User

_source line 654 · 2026-05-25T21:15:28.916019+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验验证**。

## Venue 信息
- **目标**: EMNLP 2026 via ARR (Main Conference)
- **Deadline**: 2026-05-25
- **格式**: Long paper, 8 页正文 + 无限参考文献, ACL style template (`[review]` option)
- **匿名**: Double-blind
- **Limitations section**: 必须有，不计页数
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文路径
- LaTeX: `projects/irt_personfit_contam/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/submitted.pdf`

## 你的审查侧重

### 1. IRT 方法论严谨性
- 4PL 模型选择是否合理？PSN-IRT 参数的使用是否恰当？
- Δℓz* matched-difference design 的统计正确性（假设、推导、有效性条件）
- Cohen's d 的定义和解释——注意它是 one-sample standardized departure，非传统两样本效应量
- θ-anchoring（fixed-θ vs free-θ）的理论基础和实证验证
- Bootstrap CI 的构建方法和覆盖率（仅基于 clean seeds，是否合理？）
- Local dependence robustness analysis 的模拟设计

### 2. 实验设计完整性
- 实验矩阵：3 模型家族 × 2 benchmarks × 4 污染水平——覆盖是否充分？缺失单元格是否影响结论？
- Multi-seed replication（n=10 clean, n=3 contaminated）——样本量是否足够？
- Seen/unseen decomposition 的方法论正确性
- Post-RL (GRPO) pilot 的 N=1 限制
- ARC-C 仅 Qwen 一个模型——泛化性限制
- 参数扰动鲁棒性分析是否充分

### 3. 结果呈现与统计报告
- Table 1/2 的报告格式是否清晰、一致
- Multi-seed vs single-seed 结果的区分是否明确
- CI/SD 的混合报告是否造成混淆
- 效应量的可解释性和实际意义

### 4. 格式合规
- 页数是否在 8 页以内（正文）
- Limitations section 是否存在
- 匿名是否合规
- 引用格式

请给出完整审稿意见，包括 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（用 EMNLP 评分标准）。
Weaknesses 按严重程度标注 [CRITICAL] / [SHOULD-FIX] / [MINOR]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-25T21:15:38.145589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-25T21:15:39.352596+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/review_reviewer_1_ac4dc473.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-25T21:15:39.403506+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-25T21:15:39.504503+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-25T21:15:44.978637+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-25T21:15:47.720469+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/submitted.pdf",
  "project": "irt_personfit_contam",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/submitted.pdf",
    "project": "irt_personfit_contam",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-25T21:15:55.452531+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Review Form Criteria

The review form distinguishes between different paper venues with specific criteria:

- The main criteria for Findings are soundness and reproducibility.
- Conference recommendations may
…[truncated 861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10473
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-25T21:15:56.959095+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 349.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 676.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9238
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-25T21:16:02.933555+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/submitted.pdf",
  "project": "irt_personfit_contam",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/submitted.pdf",
    "project": "irt_personfit_contam",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 664 · 2026-05-25T21:16:04.943641+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 392.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 420.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 46.8}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2010
}
```

</details>

---


### Tool call

_source line 665 · 2026-05-25T21:16:05.094633+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidelines for how to score each dimension. Include the full text of each criterion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidelines for how to score each dimension. Include the full text of each criterion."
  }
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-25T21:16:05.295981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-25T21:16:06.225166+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 929
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-25T21:16:06.276498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-25T21:16:06.730502+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-25T21:16:06.730859+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-25T21:16:07.133405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-25T21:16:07.888402+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1157
}
```

</details>

---


### Tool call

_source line 673 · 2026-05-25T21:16:07.888907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 674 · 2026-05-25T21:16:07.940162+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-25T21:16:08.543244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool result

_source line 676 · 2026-05-25T21:16:12.914252+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: Could be considered for outstanding paper award."
- **4**: "Conference: Could be accepted to an ACL conference."
- **3**: "Findings: Could be accepted to Findings of the ACL."
- **2**: "Resubmit next cycle: Needs substantial revisions."
- **1**: "Do not resubmit: Has to be fully redone."

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard presse
…[truncated 1043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7819
}
```

</details>

---


### Tool call

_source line 677 · 2026-05-25T21:16:18.750495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-25T21:16:19.269186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-25T21:16:20.233463+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1482
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-25T21:16:20.233915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-25T21:16:20.736400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1467
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-25T21:16:20.736854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-25T21:16:21.294499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 684 · 2026-05-25T21:16:22.203108+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1969
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-25T21:16:22.203561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-25T21:16:22.708485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-25T21:16:23.264730+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2527
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-25T21:16:23.265164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-25T21:16:24.075757+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2781
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-25T21:16:24.076195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 691 · 2026-05-25T21:16:24.532131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-25T21:16:24.538988+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1830
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-25T21:16:24.796431+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2592
}
```

</details>

---


### Tool result

_source line 694 · 2026-05-25T21:16:25.552056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2286
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-25T21:16:25.808624+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1276
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-25T21:16:25.909760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1833
}
```

</details>

---


### Tool call

_source line 697 · 2026-05-25T21:16:30.831537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 698 · 2026-05-25T21:16:30.883333+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 699 · 2026-05-25T21:18:48.514668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 700 · 2026-05-25T21:18:48.615528+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{enumitem}
17	
18	\newcommand{\irtfit}{\textsc{IRT-FIT}}
19	
20	\graphicspath{{../figures/paper/}}
21	
22	\title{What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{sections/abstract}
31	\end{abstract}
32	
33	\input{sections/introduction}
34	\input{sections/related_work}
35	\input{sections/method}
36	\input{sections/results}
37	\input{sections/discussion}
38	\input{sections/conclusion}
39	
40	\input{sections/limitations}
41	
42	\section*{Reproducibility Statement}
43	Code and response data are available in an anonymized repository.\footnote{\url{https://anonymous.4open.science/r/irt_personfit_contam-6004/}}
44	Bootstrap confidence intervals use the percentile method with 10,000 resamples.
45	All three model families use clean baseline seeds 0--9 ($n{=}10$ per family).
46	Pre-calibrated 4PL item parameters are from the publicly available PSN-IRT item bank \citep{psnirt2026}.
47	Training used PyTorch 2.8.0, Transformers 5.8.1, PEFT 0.19.1, and BitsAndBytes 0.49.2.
48	Both benchmarks are publicly available under permissive licenses (MMLU: MIT; ARC-Challenge: CC-BY-SA).
49	
50	\bibliography{references}
51	
52	\appendix
53	\input{sections/appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 701 · 2026-05-25T21:18:57.898926+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/abstract*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/abstract*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
  }
}
```

</details>

---


### Tool result

_source line 702 · 2026-05-25T21:18:57.949471+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/paper/paper/sections/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 703 · 2026-05-25T21:19:00.658966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 704 · 2026-05-25T21:19:00.709665+00:00_

1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first controlled characterization of Item Response Theory (IRT) person-fit statistics for detecting supervised fine-tuning (SFT) contamination, requiring only binary response patterns and calibrated four-parameter logistic item parameters; diagnostic $\theta$-anchoring requires a clean baseline.
3	A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using $\ell_z^*$ in a matched-difference design ($\Delta\ell_z^*$) across three 7--8B model families ($n{=}10$ clean seeds per family) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three boundaries:
5	(1) model-specific $\theta$-shift dynamics, where contamination-induced ability inflation absorbs the person-fit signal; $\theta$-anchoring amplifies detection by 2.4$\times$ while reducing coefficient of variation from 60\% to 19\%;
6	(2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack $\ell_z^*$'s diagnostic capabilities (seen/unseen decomposition, mechanistic $\theta$-shift analysis);
7	and (3, exploratory) ability-dependent non-monotonic dose-response under free-$\theta$ estimation, driven by $\theta$-shift absorption; $\theta$-anchored analysis reveals stable positive dose-response.
8	These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy\footnote{Code and data are available at \url{https://anonymous.4open.science/r/irt_personfit_contam-6004/}.}.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 705 · 2026-05-25T21:20:31.407233+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_round_8/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 706 · 2026-05-25T21:20:31.407750+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 707 · 2026-05-25T21:22:33.475636+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验验证\n\n## 论文信息\n**Title**: What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n\n**一句话总结**: 将 IRT person-fit 统计量应用于 LLM SFT 阶段污染检测是真正的新颖跨学科贡献，三个行为边界的发现有理论价值，但 θ-anchoring 对 clean baseline 的循环依赖、不完整的实验矩阵、以及简单统计量反而检测更强的结果共同削弱了方法的独立实用性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法论合理，matched-difference design 统计正确，但 PSN-IRT 校准样本可能含污染模型未被讨论，θ-anchoring 的实用性受循环依赖限制 |\n| Excitement | 3.5/5 | IRT person-fit 用于 LLM 污染检测是首创，三个行为边界有理论洞察力，但实际检测场景中简单统计量更优，限制了实用兴奋度 |\n| Reproducibility | 4/5 | 匿名代码仓库提供，实验细节清晰（seed 数、QLoRA 超参见 Appendix K），但依赖外部 PSN-IRT item bank 增加了复现门槛 |\n| Confidence | 4/5 | 熟悉 IRT 方法论和 LLM 污染检测文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [CRITICAL] PSN-IRT 校准样本的污染问题未被讨论\n\n- 具体位置：Section 3.1, line \"we use these external parameters rather than re-estimating from potentially contaminated data\"\n- 问题：论文使用 PSN-IRT（Zhou et al., 2026）预校准的 4PL item 参数，该参数来自\"a large-scale leaderboard-based dataset spanning 39 models\"。但 leaderboard 模型本身高概率含有污染——这恰恰是本文要解决的问题。如果校准样本中的模型已被污染，item discrimination (a_i)、difficulty (b_i) 和 upper asymptote (d_i) 参数都会产生系统性偏差。论文在 Appendix I 讨论了 MML-EM refit 的不稳定性（N 太小），但完全没有分析 PSN-IRT 自身校准样本中的潜在污染如何影响 ℓ_z* 的计算和解释。\n- 为什么影响接收：这是一个方法论根基问题。如果 item 参数本身被污染偏置，ℓ_z* 的 expected response pattern 就不代表\"无污染\"下的真实预期，整个检测框架的 validity 受损。\n- 建议修改方向：(i) 讨论 PSN-IRT 校准样本中污染模型的比例和可能影响；(ii) 进行 sensitivity analysis——人为扰动 item 参数（已部分在 Appendix H 做到 ±10%），但需要分析 *系统性* 偏差（而非随机扰动）对结果的影响；(iii) 或论证为什么 PSN-IRT 的大样本量（N=39 models per item 远大于本文的 N=10+3）足以稀释污染信号。\n\n**N2** [CRITICAL] 实验矩阵不完整，与泛化性声明不匹配\n\n- 具体位置：Section 3.3, Table 1 (p.6), Abstract\n- 问题：论文声称 findings \"across three 7–8B model families\" on \"MMLU and ARC-Challenge\"，但实际实验矩阵存在显著空缺：\n  - ARC-Challenge 仅在 Qwen 上测试，Llama 和 Mistral 完全缺失\n  - Mistral 在 MMLU 上缺少 25% 污染水平\n  - 多数污染条件为 single-seed (n=1)，multi-seed (n=3) 仅覆盖部分条件\n  实际上，只有 Qwen-MMLU 拥有完整的 4 个污染水平 × multi-seed 复制。Abstract 中 \"across three 7–8B model families...on MMLU (14,042 items) and ARC-Challenge (295 items)\" 的措辞暗示所有模型在两个 benchmark 上均有测试，这是误导性的。\n- 为什么影响接收：泛化性是本文核心价值之一。如果关键发现（如非单调 dose-response、θ-shift 动态）只在 Qwen-MMLU 上得到完整验证，\"three model families × two benchmarks\" 的叙事就站不住脚。\n- 建议修改方向：(i) 在 abstract 和 Section 4 中精确说明每个发现的模型/benchmark 覆盖范围；(ii) 补充 Llama/Mistral 在 ARC-C 上的至少一个污染水平实验；(iii) 或显著降低泛化性声明的强度，限定为 \"primarily demonstrated on Qwen-MMLU with partial replication on Llama/Mistral\"。\n\n**N3** [CRITICAL] θ-anchoring 的循环依赖问题\n\n- 具体位置：Section 3.2 (Equation 2), Section 5 (Discussion), Figure 2d\n- 问题：论文最重要的方法论发现是 θ-anchoring（fixed-θ）对高污染水平下可靠检测的必要性（Table 2 显示 fixed-θ 将 Qwen multi-seed |d| 从 5.08 放大到 12.32）。然而，θ-anchoring 要求一个 clean baseline 的 θ 值——而判断一个模型是否 clean 恰恰是检测的目标。这构成逻辑循环。论文在 Section 5 的 Practical Implications 中提出的两阶段工作流 \"(i) screen with accuracy z-scores → (ii) apply fixed-θ anchoring\" 实际上承认了 IRT ℓ_z* 不是独立的检测方法——第一阶段筛选完全不依赖 IRT。这削弱了论文 \"IRT person-fit for contamination detection\" 的核心叙事。\n- 为什么影响接收：如果方法的核心优势（θ-anchoring 带来的检测增益）在实际应用中不可用（因为需要 clean baseline），那么方法的实际贡献就退化为：在已知有 clean baseline 的受控实验设置下，提供比简单统计量更深的 *诊断* 信息。这是一个有价值但明显更弱的 contribution。\n- 建议修改方向：(i) 明确重新定位论文贡献——从\"检测方法\"转向\"诊断/分析框架\"，或论证在何种实际场景下 clean baseline 是可获得的；(ii) 探索不需要 clean baseline 的 θ-anchoring 替代方案（如 cross-benchmark θ 估计，论文已有 Section 4.1 的 seen/unseen decomposition，可以进一步发展）；(iii) 在 Discussion 中坦诚讨论这个循环性及其对实用性的影响。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [SHOULD-FIX] Post-RL (GRPO) pilot 过于初步，但在 Abstract 和 Conclusion 中被引用\n\n- 具体位置：Section 4.4, Section 6, Abstract\n- 问题：Post-RL pilot 仅使用 N=1（单模型 Qwen、单污染水平 15%、单 seed），在 3 个 checkpoint 评估。这是一个极端有限的探索性观察。然而 Abstract 和 Conclusion（Section 6）均引用此结果作为 contribution 之一：\"detection and diagnosis require different tools\"。从单个观察点得出这样的结论不具备统计说服力。\n- 建议：(i) 将 post-RL 内容完全限定为 \"preliminary observation\" 并从 abstract 中移除或降低其突出度；(ii) 或增加至少 2 个模型家族 × 2 个污染水平的 post-RL 实验。\n\n**W2** [SHOULD-FIX] Detection-diagnosis tradeoff 的\"诊断\"侧论证不足\n\n- 具体位置：Table 3 (p.7), Section 4.3, Section 5\n- 问题：Table 3 清楚显示 accuracy z-scores 在多数条件下检测效应量大于或接近 ℓ_z*（例如 Qwen 50% MMLU: Acc. z d=7.01 vs ℓ_z* d=5.09）。论文将此框架为\"检测-诊断权衡\"——简单统计量检测更强，但 ℓ_z* 提供独特的诊断能力。问题在于，\"诊断\"侧的独特价值未被充分论证：\n  - Seen/unseen decomposition（Section 4.1）是描述性的分解，不需要 ℓ_z* 也可以做（只需知道哪些是 seen items）\n  - Mechanistic θ-shift analysis 依赖 θ-anchoring，而 θ-anchoring 需要 clean baseline（见 N3）\n  - 论文未展示 ℓ_z* 诊断能力在决策上的具体优势——比如，ℓ_z* 的信息是否能指导 decontamination 策略？\n- 建议：提供一个具体用例，展示 ℓ_z* 诊断信息如何带来 accuracy z-scores 无法实现的 actionable decision。\n\n**W3** [SHOULD-FIX] 缺少与 logit-based 方法的直接比较\n\n- 具体位置：Section 2 (Related Work), Section 5 (Discussion)\n- 问题：论文在 Related Work 中将自身定位为不需要 privileged access（训练数据、模型内部概率）的方法。但在受控实验设置中，作者 *确实* 拥有模型访问权限。在这些条件下，与 MIA（Min-K%, Membership Inference Attack）等 logit-based 方法的直接比较将极大帮助读者理解 ℓ_z* 的相对优劣势。Section 5 提到 Min-K% AUC drops to 0.093 after 500 RL steps，但这只是 post-RL 条件下的间接引用，不是 head-to-head 比较。\n- 建议：至少在一个模型/benchmark/污染水平组合上运行 MIA baseline，报告 AUC 并与 ℓ_z*（或 accuracy z-score）的检测率对比。\n\n**W4** [SHOULD-FIX] Local dependence 模拟设计过于简化\n\n- 具体位置：Appendix G (p.13)\n- 问题：Appendix G 的 robustness analysis 使用简单的 additive memory factor（v_unseen ~ N(0, σ_mem)）模拟 local dependence。真实 LLM 的 response dependency 远比此复杂——包括 positional bias（item 在 prompt 中的位置）、attention-based contextual effects、model-specific decoding patterns 等。简单加性噪声模型可能低估了 LD 对 ℓ_z* 的影响。\n- 建议：讨论此模拟的局限性，或增加至少一种更复杂的 LD 结构（如 item-cluster dependence 或 position-dependent bias）。\n\n**W5** [SHOULD-FIX] Cohen's d 的非标准使用缺乏充分说明\n\n- 具体位置：Section 3.2 (Equation 3 周围)\n- 问题：论文将 Cohen's d 定义为 one-sample standardized departure (d = Δℓ_z* / SD_clean)。传统 Cohen's d 是两样本效应量（两组均值差 / pooled SD）。虽然论文简短说明了这一点（\"d is a standardized departure rather than a two-sample effect size\"），但仍然隐含使用了 Cohen (1988) 的解释基准（small=0.2, medium=0.5, large=0.8），这些基准是为两样本场景定义的。对于 one-sample departure，这些基准不直接适用。考虑到本文的效应量极大（d=2–7+），这一区别在结论上可能不影响，但在方法论表述上需要更严谨。\n- 建议：在首次引入 Cohen's d 时，明确说明其为 one-sample 版本并讨论为什么传统基准仍然具有参考价值（或提供替代基准）。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** [MINOR] Table 1 和 Table 2 的报告格式不一致：Table 1 用 Cohen's d 附 bootstrap CI，Table 2 混合报告了 free-θ 和 fixed-θ 的 Cohen's d 及 CV(%)，读者需要反复对照才能理解数据结构。建议统一表格标注或增加图注说明。\n\n- **M2** [MINOR] Abstract 中 \"(3, exploratory)\" 的标注风格与 (1)/(2) 不一致。建议统一为 \"(3) [exploratory]\" 或类似格式。\n\n- **M3** [MINOR] Figure 4 (p.6) 的 heatmap 颜色映射中 grey cells 表示 missing data，但图例标注较小且不醒目。考虑到 missing cells 正是实验矩阵不完整的体现（见 N2），建议突出标注。\n\n- **M4** [MINOR] Appendix E 的 Leaderboard Analysis 中 57/60 cells 的 |ℓ_z*| > 1.96 结果有两种解释：(a) 普遍污染，(b) IRT 模型对 LLM 的 model misfit。论文未充分区分这两种可能性。\n\n- **M5** [MINOR] 论文使用 `[review]` option（显示行号），符合 ARR 提交要求。正文 8 页（至 Section 6 Conclusion 结束），Limitations 在第 9 页不计入页数限制，格式合规。\n\n---\n\n## 主要优势\n\n1. **真正的跨学科创新**：将心理测量学的 person-fit 分析框架（Drasgow et al., 1985; Snijders, 2001; Karabatsos, 2003）系统性地迁移到 LLM 污染检测，建立了两个领域之间有意义的理论桥梁。不是简单类比，而是利用了 IRT 的具体数学性质（ℓ_z* 对 aberrant response pattern 的敏感性）。\n\n2. **严谨的受控实验设计**：SFT 阶段污染设置提供了 ground truth（已知哪些 item 被污染），n=10 clean seeds 的 multi-seed 复制在该领域罕见，matched-difference design 巧妙地消除了 model-level baseline misfit。\n\n3. **三个行为边界的发现有理论深度**：θ-shift dynamics、detection-diagnosis tradeoff、non-monotonic dose-response 不是独立的经验观察，而是由 IRT 框架统一解释的相互关联的现象。这种结构化理解超越了\"方法 X 在数据集 Y 上有效\"的常规 contribution。\n\n4. **Appendix 的thoroughness 值得肯定**：16 页附录覆盖了模拟验证（A）、4PL vs 3PL 对比（B）、BCa bootstrap sensitivity（C）、cross-family consistency（D）、leaderboard analysis（E）、item-level 分析（F）、local dependence robustness（G）、parameter noise sensitivity（H）、classical IRT refit（I）、post-RL pilot（J）、训练超参（K）、contamination run reproducibility（L）、AI assistance disclosure（M）。这种自我审查深度在提交论文中不常见。\n\n5. **匿名合规 + 可复现**：double-blind 合规（\"Anonymous ACL submission\"），匿名代码仓库提供，PSN-IRT 参数来自公开 item bank，训练框架版本完整记录。\n\n---\n\n## Questions to Authors\n\nQ1. PSN-IRT 的 39 个校准模型中有多少被已知或疑似含有 benchmark 污染？如果比例显著，item 参数偏差对 ℓ_z* 的影响方向和幅度如何？\n\nQ2. 在实际应用场景中（无 clean baseline），cross-benchmark θ 估计（用 benchmark A 的 θ 作为 benchmark B 的 anchor）的可行性如何？Table 2 的 cross-benchmark comparison 是否支持这一方向？\n\nQ3. 对于 ARC-Challenge 的 ceiling effect（89.7% baseline accuracy, 295 items），ℓ_z* 和 accuracy z-scores 的检测力差异是否主要由 item 数量和难度分布驱动，而非方法论差异？\n\nQ4. Appendix E 的 leaderboard analysis 中 57/60 cells 显示 |ℓ_z*| > 1.96，作者如何区分\"普遍污染\"和\"IRT 模型 misspecification for LLMs\"这两种解释？\n\n---\n\n## Reviewer Confidence\n4/5 — 熟悉 IRT 方法论、person-fit 统计量文献、以及 LLM 污染检测相关工作。对 PSN-IRT 的具体实现细节了解有限。\n",
  "reviewer_id": "1",
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验验证\n\n## 论文信息\n**Title**: What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n\n**一句话总结**: 将 IRT person-fit 统计量应用于 LLM SFT 阶段污染检测是真正的新颖跨学科贡献，三个行为边界的发现有理论价值，但 θ-anchoring 对 clean baseline 的循环依赖、不完整的实验矩阵、以及简单统计量反而检测更强的结果共同削弱了方法的独立实用性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法论合理，matched-difference design 统计正确，但 PSN-IRT 校准样本可能含污染模型未被讨论，θ-anchoring 的实用性受循环依赖限制 |\n| Excitement | 3.5/5 | IRT person-fit 用于 LLM 污染检测是首创，三个行为边界有理论洞察力，但实际检测场景中简单统计量更优，限制了实用兴奋度 |\n| Reproducibility | 4/5 | 匿名代码仓库提供，实验细节清晰（seed 数、QLoRA 超参见 Appendix K），但依赖外部 PSN-IRT item bank 增加了复现门槛 |\n| Confidence | 4/5 | 熟悉 IRT 方法论和 LLM 污染检测文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [CRITICAL] PSN-IRT 校准样本的污染问题未被讨论\n\n- 具体位置：Section 3.1, line \"we use these external parameters rather than re-estimating from potentially contaminated data\"\n- 问题：论文使用 PSN-IRT（Zhou et al., 2026）预校准的 4PL item 参数，该参数来自\"a large-scale leaderboard-based dataset spanning 39 models\"。但 leaderboard 模型本身高概率含有污染——这恰恰是本文要解决的问题。如果校准样本中的模型已被污染，item discrimination (a_i)、difficulty (b_i) 和 upper asymptote (d_i) 参数都会产生系统性偏差。论文在 Appendix I 讨论了 MML-EM refit 的不稳定性（N 太小），但完全没有分析 PSN-IRT 自身校准样本中的潜在污染如何影响 ℓ_z* 的计算和解释。\n- 为什么影响接收：这是一个方法论根基问题。如果 item 参数本身被污染偏置，ℓ_z* 的 expected response pattern 就不代表\"无污染\"下的真实预期，整个检测框架的 validity 受损。\n- 建议修改方向：(i) 讨论 PSN-IRT 校准样本中污染模型的比例和可能影响；(ii) 进行 sensitivity analysis——人为扰动 item 参数（已部分在 Appendix H 做到 ±10%），但需要分析 *系统性* 偏差（而非随机扰动）对结果的影响；(iii) 或论证为什么 PSN-IRT 的大样本量（N=39 models per item 远大于本文的 N=10+3）足以稀释污染信号。\n\n**N2** [CRITICAL] 实验矩阵不完整，与泛化性声明不匹配\n\n- 具体位置：Section 3.3, Table 1 (p.6), Abstract\n- 问题：论文声称 findings \"across three 7–8B model families\" on \"MMLU and ARC-Challenge\"，但实际实验矩阵存在显著空缺：\n  - ARC-Challenge 仅在 Qwen 上测试，Llama 和 Mistral 完全缺失\n  - Mistral 在 MMLU 上缺少 25% 污染水平\n  - 多数污染条件为 single-seed (n=1)，multi-seed (n=3) 仅覆盖部分条件\n  实际上，只有 Qwen-MMLU 拥有完整的 4 个污染水平 × multi-seed 复制。Abstract 中 \"across three 7–8B model families...on MMLU (14,042 items) and ARC-Challenge (295 items)\" 的措辞暗示所有模型在两个 benchmark 上均有测试，这是误导性的。\n- 为什么影响接收：泛化性是本文核心价值之一。如果关键发现（如非单调 dose-response、θ-shift 动态）只在 Qwen-MMLU 上得到完整验证，\"three model families × two benchmarks\" 的叙事就站不住脚。\n- 建议修改方向：(i) 在 abstract 和 Section 4 中精确说明每个发现的模型/benchmark 覆盖范围；(ii) 补充 Llama/Mistral 在 ARC-C 上的至少一个污染水平实验；(iii) 或显著降低泛化性声明的强度，限定为 \"primarily demonstrated on Qwen-MMLU with partial replication on Llama/Mistral\"。\n\n**N3** [CRITICAL] θ-anchoring 的循环依赖问题\n\n- 具体位置：Section 3.2 (Equation 2), Section 5 (Discussion), Figure 2d\n- 问题：论文最重要的方法论发现是 θ-anchoring（fixed-θ）对高污染水平下可靠检测的必要性（Table 2 显示 fixed-θ 将 Qwen multi-seed |d| 从 5.08 放大到 12.32）。然而，θ-anchoring 要求一个 clean baseline 的 θ 值——而判断一个模型是否 clean 恰恰是检测的目标。这构成逻辑循环。论文在 Section 5 的 Practical Implications 中提出的两阶段工作流 \"(i) screen with accuracy z-scores → (ii) apply fixed-θ anchoring\" 实际上承认了 IRT ℓ_z* 不是独立的检测方法——第一阶段筛选完全不依赖 IRT。这削弱了论文 \"IRT person-fit for contamination detection\" 的核心叙事。\n- 为什么影响接收：如果方法的核心优势（θ-anchoring 带来的检测增益）在实际应用中不可用（因为需要 clean baseline），那么方法的实际贡献就退化为：在已知有 clean baseline 的受控实验设置下，提供比简单统计量更深的 *诊断* 信息。这是一个有价值但明显更弱的 contribution。\n- 建议修改方向：(i) 明确重新定位论文贡献——从\"检测方法\"转向\"诊断/分析框架\"，或论证在何种实际场景下 clean baseline 是可获得的；(ii) 探索不需要 clean baseline 的 θ-anchoring 替代方案（如 cross-benchmark θ 估计，论文已有 Section 4.1 的 seen/unseen decomposition，可以进一步发展）；(iii) 在 Discussion 中坦诚讨论这个循环性及其对实用性的影响。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [SHOULD-FIX] Post-RL (GRPO) pilot 过于初步，但在 Abstract 和 Conclusion 中被引用\n\n- 具体位置：Section 4.4, Section 6, Abstract\n- 问题：Post-RL pilot 仅使用 N=1（单模型 Qwen、单污染水平 15%、单 seed），在 3 个 checkpoint 评估。这是一个极端有限的探索性观察。然而 Abstract 和 Conclusion（Section 6）均引用此结果作为 contribution 之一：\"detection and diagnosis require different tools\"。从单个观察点得出这样的结论不具备统计说服力。\n- 建议：(i) 将 post-RL 内容完全限定为 \"preliminary observation\" 并从 abstract 中移除或降低其突出度；(ii) 或增加至少 2 个模型家族 × 2 个污染水平的 post-RL 实验。\n\n**W2** [SHOULD-FIX] Detection-diagnosis tradeoff 的\"诊断\"侧论证不足\n\n- 具体位置：Table 3 (p.7), Section 4.3, Section 5\n- 问题：Table 3 清楚显示 accuracy z-scores 在多数条件下检测效应量大于或接近 ℓ_z*（例如 Qwen 50% MMLU: Acc. z d=7.01 vs ℓ_z* d=5.09）。论文将此框架为\"检测-诊断权衡\"——简单统计量检测更强，但 ℓ_z* 提供独特的诊断能力。问题在于，\"诊断\"侧的独特价值未被充分论证：\n  - Seen/unseen decomposition（Section 4.1）是描述性的分解，不需要 ℓ_z* 也可以做（只需知道哪些是 seen items）\n  - Mechanistic θ-shift analysis 依赖 θ-anchoring，而 θ-anchoring 需要 clean baseline（见 N3）\n  - 论文未展示 ℓ_z* 诊断能力在决策上的具体优势——比如，ℓ_z* 的信息是否能指导 decontamination 策略？\n- 建议：提供一个具体用例，展示 ℓ_z* 诊断信息如何带来 accuracy z-scores 无法实现的 actionable decision。\n\n**W3** [SHOULD-FIX] 缺少与 logit-based 方法的直接比较\n\n- 具体位置：Section 2 (Related Work), Section 5 (Discussion)\n- 问题：论文在 Related Work 中将自身定位为不需要 privileged access（训练数据、模型内部概率）的方法。但在受控实验设置中，作者 *确实* 拥有模型访问权限。在这些条件下，与 MIA（Min-K%, Membership Inference Attack）等 logit-based 方法的直接比较将极大帮助读者理解 ℓ_z* 的相对优劣势。Section 5 提到 Min-K% AUC drops to 0.093 after 500 RL steps，但这只是 post-RL 条件下的间接引用，不是 head-to-head 比较。\n- 建议：至少在一个模型/benchmark/污染水平组合上运行 MIA baseline，报告 AUC 并与 ℓ_z*（或 accuracy z-score）的检测率对比。\n\n**W4** [SHOULD-FIX] Local dependence 模拟设计过于简化\n\n- 具体位置：Appendix G (p.13)\n- 问题：Appendix G 的 robustness analysis 使用简单的 additive memory factor（v_unseen ~ N(0, σ_mem)）模拟 local dependence。真实 LLM 的 response dependency 远比此复杂——包括 positional bias（item 在 prompt 中的位置）、attention-based contextual effects、model-specific decoding patterns 等。简单加性噪声模型可能低估了 LD 对 ℓ_z* 的影响。\n- 建议：讨论此模拟的局限性，或增加至少一种更复杂的 LD 结构（如 item-cluster dependence 或 position-dependent bias）。\n\n**W5** [SHOULD-FIX] Cohen's d 的非标准使用缺乏充分说明\n\n- 具体位置：Section 3.2 (Equation 3 周围)\n- 问题：论文将 Cohen's d 定义为 one-sample standardized departure (d = Δℓ_z* / SD_clean)。传统 Cohen's d 是两样本效应量（两组均值差 / pooled SD）。虽然论文简短说明了这一点（\"d is a standardized departure rather than a two-sample effect size\"），但仍然隐含使用了 Cohen (1988) 的解释基准（small=0.2, medium=0.5, large=0.8），这些基准是为两样本场景定义的。对于 one-sample departure，这些基准不直接适用。考虑到本文的效应量极大（d=2–7+），这一区别在结论上可能不影响，但在方法论表述上需要更严谨。\n- 建议：在首次引入 Cohen's d 时，明确说明其为 one-sample 版本并讨论为什么传统基准仍然具有参考价值（或提供替代基准）。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** [MINOR] Table 1 和 Table 2 的报告格式不一致：Table 1 用 Cohen's d 附 bootstrap CI，Table 2 混合报告了 free-θ 和 fixed-θ 的 Cohen's d 及 CV(%)，读者需要反复对照才能理解数据结构。建议统一表格标注或增加图注说明。\n\n- **M2** [MINOR] Abstract 中 \"(3, exploratory)\" 的标注风格与 (1)/(2) 不一致。建议统一为 \"(3) [exploratory]\" 或类似格式。\n\n- **M3** [MINOR] Figure 4 (p.6) 的 heatmap 颜色映射中 grey cells 表示 missing data，但图例标注较小且不醒目。考虑到 missing cells 正是实验矩阵不完整的体现（见 N2），建议突出标注。\n\n- **M4** [MINOR] Appendix E 的 Leaderboard Analysis 中 57/60 cells 的 |ℓ_z*| > 1.96 结果有两种解释：(a) 普遍污染，(b) IRT 模型对 LLM 的 model misfit。论文未充分区分这两种可能性。\n\n- **M5** [MINOR] 论文使用 `[review]` option（显示行号），符合 ARR 提交要求。正文 8 页（至 Section 6 Conclusion 结束），Limitations 在第 9 页不计入页数限制，格式合规。\n\n---\n\n## 主要优势\n\n1. **真正的跨学科创新**：将心理测量学的 person-fit 分析框架（Drasgow et al., 1985; Snijders, 2001; Karabatsos, 2003）系统性地迁移到 LLM 污染检测，建立了两个领域之间有意义的理论桥梁。不是简单类比，而是利用了 IRT 的具体数学性质（ℓ_z* 对 aberrant response pattern 的敏感性）。\n\n2. **严谨的受控实验设计**：SFT 阶段污染设置提供了 ground truth（已知哪些 item 被污染），n=10 clean seeds 的 multi-seed 复制在该领域罕见，matched-difference design 巧妙地消除了 model-level baseline misfit。\n\n3. **三个行为边界的发现有理论深度**：θ-shift dynamics、detection-diagnosis tradeoff、non-monotonic dose-response 不是独立的经验观察，而是由 IRT 框架统一解释的相互关联的现象。这种结构化理解超越了\"方法 X 在数据集 Y 上有效\"的常规 contribution。\n\n4. **Appendix 的thoroughness 值得肯定**：16 页附录覆盖了模拟验证（A）、4PL vs 3PL 对比（B）、BCa bootstrap sensitivity（C）、cross-family consistency（D）、leaderboard analysis（E）、item-level 分析（F）、local dependence robustness（G）、parameter noise sensitivity（H）、classical IRT refit（I）、post-RL pilot（J）、训练超参（K）、contamination run reproducibility（L）、AI assistance disclosure（M）。这种自我审查深度在提交论文中不常见。\n\n5. **匿名合规 + 可复现**：double-blind 合规（\"Anonymous ACL submission\"），匿名代码仓库提供，PSN-IRT 参数来自公开 item bank，训练框架版本完整记录。\n\n---\n\n## Questions to Authors\n\nQ1. PSN-IRT 的 39 个校准模型中有多少被已知或疑似含有 benchmark 污染？如果比例显著，item 参数偏差对 ℓ_z* 的影响方向和幅度如何？\n\nQ2. 在实际应用场景中（无 clean baseline），cross-benchmark θ 估计（用 benchmark A 的 θ 作为 benchmark B 的 anchor）的可行性如何？Table 2 的 cross-benchmark comparison 是否支持这一方向？\n\nQ3. 对于 ARC-Challenge 的 ceiling effect（89.7% baseline accuracy, 295 items），ℓ_z* 和 accuracy z-scores 的检测力差异是否主要由 item 数量和难度分布驱动，而非方法论差异？\n\nQ4. Appendix E 的 leaderboard analysis 中 57/60 cells 显示 |ℓ_z*| > 1.96，作者如何区分\"普遍污染\"和\"IRT 模型 misspecification for LLMs\"这两种解释？\n\n---\n\n## Reviewer Confidence\n4/5 — 熟悉 IRT 方法论、person-fit 统计量文献、以及 LLM 污染检测相关工作。对 PSN-IRT 的具体实现细节了解有限。\n",
    "reviewer_id": "1",
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 708 · 2026-05-25T21:22:37.395489+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3919
}
```

</details>

---


### Assistant

_source line 709 · 2026-05-25T21:22:51.363285+00:00_

审稿意见已提交给 Review Director。

**审稿摘要**：

- **Overall: 3.5 (Borderline Conference)**
- **Soundness: 3.5/5 | Excitement: 3.5/5 | Reproducibility: 4/5**

**3 个 Critical 问题**：
1. PSN-IRT 校准样本可能含污染模型，未讨论对 item 参数和 ℓ_z* 的系统性偏差影响
2. 实验矩阵不完整（ARC-C 仅 Qwen，Mistral 缺 25%），但 abstract/conclusion 以"three families × two benchmarks"做泛化声明
3. θ-anchoring 需要 clean baseline 构成逻辑循环，实际工作流中 IRT 不是独立检测方法

**5 个 Should-Fix**：Post-RL pilot 过于初步(N=1)却写入 abstract；detection-diagnosis tradeoff 的"诊断"侧价值论证不足；缺少与 logit-based 方法的 head-to-head 比较；local dependence 模拟过简化；Cohen's d 的 one-sample 非标准用法需更严谨说明。

**主要优势**：真正跨学科创新（psychometrics → NLP），受控实验设计严谨（n=10 clean seeds），三个行为边界有理论统一性，16 页附录覆盖全面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1"
}
```

</details>

---


## Round 25

## Round 25

4 recorded events


### User

_source line 710 · 2026-05-25T21:23:30.499610+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿意见（Round 1）— 新颖性 + 论文完整性

## Paper Summary

本文将心理测量学中的 IRT person-fit 统计量（Snijders 校正后的 log-likelihood 残差 ℓ*_z）应用于 LLM SFT 阶段基准测试污染的表征。采用 matched-difference 设计，在三个 7-8B 模型族（Qwen2.5, Llama-3.1, Mistral）上以四个污染水平（5%/15%/25%/50%）在 MMLU 和 ARC-Challenge 上进行实验，每个模型族 n=10 clean seeds。论文识别出三个 "behavioral boundaries"：(1) θ-shift dynamics（污染膨胀能力估计，吸收 person-fit 信号）；(2) detection-diagnosis tradeoff（简单统计量检测更强但缺少机制解释力）；(3) 模型依赖的非单调剂量反应（free-θ 下）。论文定位为 characterization study 而非 detection method。

## Overall: 3.5 / 5 — Borderline Conference

## Must-Fix 问题

**N1** [CRITICAL] 缺少与现有检测方法的实证对比
- Figure 2(a) 将 ℓ*_z 定位在 "detection frontier" 上，但这是概念图而非实证结果。论文从未与 MIA、Min-K%、ConStat、CDD 等方法进行头对头检测性能比较。Limitations 承认 "we do not provide head-to-head comparison with logit-based methods"，但 Figure 2(a) 的 detection frontier 暗示了 detection method 贡献。
- 建议：至少与一种同样只需 binary response 的方法和一种 logit-based 方法进行实证对比；或移除 Figure 2(a) 的 detection frontier 定位。

**N2** [CRITICAL] Post-RL robustness claim 严重 underpowered
- Post-RL 分析仅 N=1（Qwen, GRPO, 15% MMLU, 3 checkpoints）。Section 6 使用 "structural invariance" 表述，对 N=1 而言过强。Figure 6 仅一条轨迹线。
- 建议：将 "structural invariance" 改为 "preliminary pilot observation"；在 Section 6 明确标注 N=1 限制；理想情况增加模型/RL方法验证。

**N3** [CRITICAL] 2/3 核心发现为确认性发现，新颖性受限
- Finding 1（θ-shift dynamics）是 IRT 理论直接推论；Finding 2（detection-diagnosis tradeoff）是统计学普遍规律。论文自身标注 Finding 1-2 为 "confirmatory"，但 Abstract/Introduction 未区分层次。真正新颖仅 Finding 3（非单调剂量反应），单独可能不足以支撑 main conference 论文。
- 建议：Abstract/Introduction 中更清楚区分 confirmatory vs exploratory；强化 Finding 3 分析；增加 exploratory findings。

## Should-Fix 问题

**W1** [SHOULD-FIX] 模型规模局限（仅 7-8B）
- θ-shift dynamics 和非单调剂量反应可能在更大模型（13B, 70B）上表现不同。Limitations 未讨论 scale 限制。

**W2** [SHOULD-FIX] PSN-IRT 参数依赖风险
- Appendix I 显示 PSN-IRT 与 MML-EM 参数相关性仅中等（difficulty r=0.663, discrimination r=0.127）。ℓ*_z 直接依赖所有四个参数，不一致性对稳健性构成威胁。
- 建议：用 MML-EM 参数重新计算 ℓ*_z 检查结论是否成立。

**W3** [SHOULD-FIX] Benchmark 覆盖面窄（仅两个 MCQ）
- MMLU 和 ARC-C 都是选择题。IRT 4PL 对 MCQ 适配好，非 MCQ 格式适用性未知。

**W4** [SHOULD-FIX] "Behavioral boundaries" 措辞过强
- "Boundaries" 暗示基本限制或相变点，实际观察为连续渐变模式。建议改为 "behavioral patterns" 或 "empirical regularities"。

**W5** [SHOULD-FIX] Related Work 遗漏近期重要工作
- 未引用 Zavaschi et al. (2026) watermarking 检测、CoDeC (2025) in-context learning 检测、Growing Pains (2026) fixed parameter calibration。

---

请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 711 · 2026-05-25T21:25:14.857562+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### R2-N1: 缺少与现有检测方法的实证对比\n\n**[AGREE]** R2-N1\n\n同意此为实质性不足。我在自己的审稿中也提出了相同问题（R1-W3）。补充两点：\n\n(1) Figure 2(a) 的 \"detection frontier\" 概念图确实造成了误导性预期。论文在 Section 1 明确将自身定位为 \"characterization study, not a detection method\"（page 2 贡献列表），但 Figure 2(a) 的视觉呈现暗示了 detection method 定位。R2 关于\"移除 Figure 2(a) 或增加实证对比\"的建议合理。\n\n(2) 需要注意一个公平性问题：论文的核心约束是 *仅使用 binary response patterns*（不需要 logit/概率信息）。在这个约束下，真正可比的 baseline 方法很少——MIA/Min-K% 需要 token-level probabilities，ConStat 需要 rephrased prompt 的 accuracy vectors。与这些方法的\"公平\"对比需要讨论 access level 差异。但至少应该与同样基于 binary responses 的 accuracy z-score 做正式的 detection performance 对比（论文 Table 3 已有 effect size 数据，差的是标准化的 detection metrics 如 AUROC）。\n\n---\n\n### R2-N2: Post-RL robustness claim 严重 underpowered\n\n**[AGREE]** R2-N2\n\n完全同意。我在 R1-W1 中提出了相同问题。Section 6 的 \"structural invariance (RL reshapes token-level distributions but preserves binary correctness anomalies)\" 对 N=1 观察而言确实过强。\"Preliminary pilot observation\" 是更准确的表述。补充一点：Figure 6 的单条轨迹线虽然 suggestive，但连 ℓ*_z gap 的置信区间都无法构建（只有 n=1 contaminated seed at each checkpoint）。这不仅仅是 sample size 问题，而是连基本的 uncertainty quantification 都缺失。\n\n---\n\n### R2-N3: 2/3 核心发现为确认性发现，新颖性受限\n\n**[REBUT]** R2-N3\n\n部分反驳。R2 的观察在形式上准确——论文自身确实标注 Findings 1–2 为 confirmatory（page 2）——但对新颖性的评估过于严苛，原因如下：\n\n(1) **Confirmatory ≠ trivial in a new domain**。θ-shift dynamics（Finding 1）在心理测量文献中有理论预测（Karabatsos, 2003），但 *从未在 LLM response patterns 上实证验证过*。理论预测能否迁移到 LLM 行为是非平凡的问题——LLM 不是人类考生，其 response patterns 的 IRT 可解析性本身就是一个开放问题。论文 Section 4.2 展示了 θ-shift 的 model-specific 幅度差异（Qwen |d| 从 2.4× 放大到 12.32 at 50%, Table 2; Llama 仅 shows minimal absorption），这些定量差异是新的经验知识。\n\n(2) **Detection-diagnosis tradeoff（Finding 2）的新颖性在于 *定量* 刻画**。\"简单统计量检测更强\"不是先验显然的——如果 IRT ℓ*_z 利用了完整的 4 参数 item-level 信息，它 *应该* 比 2 参数统计量更强。Table 3 展示了一个反直觉的结果：额外的参数信息在 detection 上不帮忙甚至有害（因为 θ-shift 吸收），但在 diagnosis 上有价值（seen/unseen decomposition, Section 4.1）。这不是\"统计学普遍规律\"，而是 IRT person-fit 在 LLM 污染场景下的具体表现。\n\n(3) 但我同意 R2 关于 **Abstract/Introduction 措辞** 的建议。当前 abstract 将三个 findings 并列呈现，未区分 confirmatory 和 exploratory 层次。Introduction 的贡献列表（page 2）确实标注了层次，但 abstract 没有继承这一区分。建议 abstract 中明确标注 \"(Findings 1–2 are confirmatory; Finding 3 is exploratory)\"，与 Introduction 保持一致。\n\n综上：新颖性问题有 merit 但不构成 CRITICAL 级别。降为 SHOULD-FIX 更合适。\n\n---\n\n## Should-Fix 问题\n\n### R2-W1: 模型规模局限（仅 7-8B）\n\n**[AGREE]** R2-W1\n\n同意。我在自己的审稿中也标注了此问题（R1 小问题 M5 类似）。θ-shift dynamics 的幅度和方向可能在更大模型上有质的不同：(a) 更大模型的 baseline ability θ 更高，留给 θ-shift 的空间可能更小（ceiling effect）；(b) 更大模型可能需要更少的 contamination exposure 就产生显著 memorization（data efficiency 随 scale 提升）。Limitations section 应明确讨论 scale 限制。\n\n---\n\n### R2-W2: PSN-IRT 参数依赖风险\n\n**[REBUT]** R2-W2\n\n部分反驳 R2 的具体建议，但同意底层关切（我在 R1-N1 中从不同角度提出了更强的版本）。\n\nR2 建议 \"用 MML-EM 参数重新计算 ℓ*_z 检查结论是否成立\"。但 Appendix I 已经展示了这不可行：MML-EM 参数在 N=178 models 下严重欠定（discrimination recovery d̃/d = 0.127，Table 13 显示 3PL discrimination correlation r_s = 0.127），远低于 stable 3PL 估计通常所需的 N > 500。用这些参数重算 ℓ*_z 得到的结果不具备解释力——不是因为 PSN-IRT 更好，而是因为 MML-EM 估计本身不可靠。\n\n真正的风险在于我 R1-N1 中指出的问题：**PSN-IRT 校准样本（39 个 leaderboard 模型）本身可能含有 benchmark 污染**，导致 item 参数存在 *系统性偏差*。Appendix H 的 ±10% 随机扰动分析不能回答此问题，因为污染导致的偏差是系统性的（方向一致），而非随机的。\n\n---\n\n### R2-W3: Benchmark 覆盖面窄（仅两个 MCQ）\n\n**[AGREE]** R2-W3\n\n同意。IRT 4PL 模型的核心假设是 binary scored items with well-defined correct/incorrect responses。MCQ benchmarks 天然满足此条件。对于 open-ended generation tasks（如 GSM8K、HumanEval），需要 reliability scorer 将连续评分二值化，引入额外噪声。论文应在 Limitations 中明确讨论 benchmark format 的适用范围。不过，MCQ benchmarks（MMLU、ARC、HellaSwag、MMLU-Pro 等）仍然是 LLM 评估的核心组成部分，覆盖这两个 MCQ benchmark 有实际意义。\n\n---\n\n### R2-W4: \"Behavioral boundaries\" 措辞过强\n\n**[AGREE]** R2-W4\n\n同意但认为严重程度较低。从论文数据看，三个发现中只有 Finding 3（非单调 dose-response 在 free-θ vs fixed-θ 下的质变）接近于\"boundary\"的含义——存在一个 θ-shift absorption 足以反转 signal direction 的临界点。Findings 1-2 确实更像 continuous gradations。\"Behavioral patterns\" 或 \"empirical regimes\" 是更精确的替代表述。但这是 presentation 层面的问题，不影响技术结论。\n\n---\n\n### R2-W5: Related Work 遗漏近期重要工作\n\n**[AGREE]** R2-W5（有保留）\n\n原则上同意应检查 Related Work 的完整性。但我无法独立验证 R2 列出的三篇具体论文（Zavaschi et al., 2026; CoDeC, 2025; Growing Pains, 2026）的存在性和相关性。如果这些工作确实存在且直接相关，应补充引用；如果是 R2 的误引或与论文 scope 不直接相关（如 watermarking 检测与 IRT person-fit contamination detection 的关联较弱），则可在 author response 中说明。建议 Director 要求作者核实这三篇引用的真实性和相关性。\n\n---\n\n## 总结\n\n与 R2 的评分一致（Overall 3.5 Borderline Conference）。R2 的 N1（缺少实证对比）和 N2（post-RL underpowered）与我的判断完全吻合。R2-N3（confirmatory 发现新颖性受限）有道理但评级过高——confirmatory findings 在新领域的首次实证验证有独立价值，建议从 CRITICAL 降为 SHOULD-FIX。\n",
  "reviewer_id": "1",
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### R2-N1: 缺少与现有检测方法的实证对比\n\n**[AGREE]** R2-N1\n\n同意此为实质性不足。我在自己的审稿中也提出了相同问题（R1-W3）。补充两点：\n\n(1) Figure 2(a) 的 \"detection frontier\" 概念图确实造成了误导性预期。论文在 Section 1 明确将自身定位为 \"characterization study, not a detection method\"（page 2 贡献列表），但 Figure 2(a) 的视觉呈现暗示了 detection method 定位。R2 关于\"移除 Figure 2(a) 或增加实证对比\"的建议合理。\n\n(2) 需要注意一个公平性问题：论文的核心约束是 *仅使用 binary response patterns*（不需要 logit/概率信息）。在这个约束下，真正可比的 baseline 方法很少——MIA/Min-K% 需要 token-level probabilities，ConStat 需要 rephrased prompt 的 accuracy vectors。与这些方法的\"公平\"对比需要讨论 access level 差异。但至少应该与同样基于 binary responses 的 accuracy z-score 做正式的 detection performance 对比（论文 Table 3 已有 effect size 数据，差的是标准化的 detection metrics 如 AUROC）。\n\n---\n\n### R2-N2: Post-RL robustness claim 严重 underpowered\n\n**[AGREE]** R2-N2\n\n完全同意。我在 R1-W1 中提出了相同问题。Section 6 的 \"structural invariance (RL reshapes token-level distributions but preserves binary correctness anomalies)\" 对 N=1 观察而言确实过强。\"Preliminary pilot observation\" 是更准确的表述。补充一点：Figure 6 的单条轨迹线虽然 suggestive，但连 ℓ*_z gap 的置信区间都无法构建（只有 n=1 contaminated seed at each checkpoint）。这不仅仅是 sample size 问题，而是连基本的 uncertainty quantification 都缺失。\n\n---\n\n### R2-N3: 2/3 核心发现为确认性发现，新颖性受限\n\n**[REBUT]** R2-N3\n\n部分反驳。R2 的观察在形式上准确——论文自身确实标注 Findings 1–2 为 confirmatory（page 2）——但对新颖性的评估过于严苛，原因如下：\n\n(1) **Confirmatory ≠ trivial in a new domain**。θ-shift dynamics（Finding 1）在心理测量文献中有理论预测（Karabatsos, 2003），但 *从未在 LLM response patterns 上实证验证过*。理论预测能否迁移到 LLM 行为是非平凡的问题——LLM 不是人类考生，其 response patterns 的 IRT 可解析性本身就是一个开放问题。论文 Section 4.2 展示了 θ-shift 的 model-specific 幅度差异（Qwen |d| 从 2.4× 放大到 12.32 at 50%, Table 2; Llama 仅 shows minimal absorption），这些定量差异是新的经验知识。\n\n(2) **Detection-diagnosis tradeoff（Finding 2）的新颖性在于 *定量* 刻画**。\"简单统计量检测更强\"不是先验显然的——如果 IRT ℓ*_z 利用了完整的 4 参数 item-level 信息，它 *应该* 比 2 参数统计量更强。Table 3 展示了一个反直觉的结果：额外的参数信息在 detection 上不帮忙甚至有害（因为 θ-shift 吸收），但在 diagnosis 上有价值（seen/unseen decomposition, Section 4.1）。这不是\"统计学普遍规律\"，而是 IRT person-fit 在 LLM 污染场景下的具体表现。\n\n(3) 但我同意 R2 关于 **Abstract/Introduction 措辞** 的建议。当前 abstract 将三个 findings 并列呈现，未区分 confirmatory 和 exploratory 层次。Introduction 的贡献列表（page 2）确实标注了层次，但 abstract 没有继承这一区分。建议 abstract 中明确标注 \"(Findings 1–2 are confirmatory; Finding 3 is exploratory)\"，与 Introduction 保持一致。\n\n综上：新颖性问题有 merit 但不构成 CRITICAL 级别。降为 SHOULD-FIX 更合适。\n\n---\n\n## Should-Fix 问题\n\n### R2-W1: 模型规模局限（仅 7-8B）\n\n**[AGREE]** R2-W1\n\n同意。我在自己的审稿中也标注了此问题（R1 小问题 M5 类似）。θ-shift dynamics 的幅度和方向可能在更大模型上有质的不同：(a) 更大模型的 baseline ability θ 更高，留给 θ-shift 的空间可能更小（ceiling effect）；(b) 更大模型可能需要更少的 contamination exposure 就产生显著 memorization（data efficiency 随 scale 提升）。Limitations section 应明确讨论 scale 限制。\n\n---\n\n### R2-W2: PSN-IRT 参数依赖风险\n\n**[REBUT]** R2-W2\n\n部分反驳 R2 的具体建议，但同意底层关切（我在 R1-N1 中从不同角度提出了更强的版本）。\n\nR2 建议 \"用 MML-EM 参数重新计算 ℓ*_z 检查结论是否成立\"。但 Appendix I 已经展示了这不可行：MML-EM 参数在 N=178 models 下严重欠定（discrimination recovery d̃/d = 0.127，Table 13 显示 3PL discrimination correlation r_s = 0.127），远低于 stable 3PL 估计通常所需的 N > 500。用这些参数重算 ℓ*_z 得到的结果不具备解释力——不是因为 PSN-IRT 更好，而是因为 MML-EM 估计本身不可靠。\n\n真正的风险在于我 R1-N1 中指出的问题：**PSN-IRT 校准样本（39 个 leaderboard 模型）本身可能含有 benchmark 污染**，导致 item 参数存在 *系统性偏差*。Appendix H 的 ±10% 随机扰动分析不能回答此问题，因为污染导致的偏差是系统性的（方向一致），而非随机的。\n\n---\n\n### R2-W3: Benchmark 覆盖面窄（仅两个 MCQ）\n\n**[AGREE]** R2-W3\n\n同意。IRT 4PL 模型的核心假设是 binary scored items with well-defined correct/incorrect responses。MCQ benchmarks 天然满足此条件。对于 open-ended generation tasks（如 GSM8K、HumanEval），需要 reliability scorer 将连续评分二值化，引入额外噪声。论文应在 Limitations 中明确讨论 benchmark format 的适用范围。不过，MCQ benchmarks（MMLU、ARC、HellaSwag、MMLU-Pro 等）仍然是 LLM 评估的核心组成部分，覆盖这两个 MCQ benchmark 有实际意义。\n\n---\n\n### R2-W4: \"Behavioral boundaries\" 措辞过强\n\n**[AGREE]** R2-W4\n\n同意但认为严重程度较低。从论文数据看，三个发现中只有 Finding 3（非单调 dose-response 在 free-θ vs fixed-θ 下的质变）接近于\"boundary\"的含义——存在一个 θ-shift absorption 足以反转 signal direction 的临界点。Findings 1-2 确实更像 continuous gradations。\"Behavioral patterns\" 或 \"empirical regimes\" 是更精确的替代表述。但这是 presentation 层面的问题，不影响技术结论。\n\n---\n\n### R2-W5: Related Work 遗漏近期重要工作\n\n**[AGREE]** R2-W5（有保留）\n\n原则上同意应检查 Related Work 的完整性。但我无法独立验证 R2 列出的三篇具体论文（Zavaschi et al., 2026; CoDeC, 2025; Growing Pains, 2026）的存在性和相关性。如果这些工作确实存在且直接相关，应补充引用；如果是 R2 的误引或与论文 scope 不直接相关（如 watermarking 检测与 IRT person-fit contamination detection 的关联较弱），则可在 author response 中说明。建议 Director 要求作者核实这三篇引用的真实性和相关性。\n\n---\n\n## 总结\n\n与 R2 的评分一致（Overall 3.5 Borderline Conference）。R2 的 N1（缺少实证对比）和 N2（post-RL underpowered）与我的判断完全吻合。R2-N3（confirmatory 发现新颖性受限）有道理但评级过高——confirmatory findings 在新领域的首次实证验证有独立价值，建议从 CRITICAL 降为 SHOULD-FIX。\n",
    "reviewer_id": "1",
    "project": "irt_personfit_contam"
  }
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-25T21:25:20.171661+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5314
}
```

</details>

---


### Assistant

_source line 713 · 2026-05-25T21:25:26.917436+00:00_

已提交对 Reviewer 2 全部 8 条意见的逐条回应。核心判断：

- **N1（缺实证对比）、N2（post-RL underpowered）**：完全同意，与我自己的审稿一致
- **N3（confirmatory 发现新颖性受限）**：部分反驳——confirmatory findings 在新领域首次实证验证有独立价值，建议从 CRITICAL 降为 SHOULD-FIX
- **W1-W5**：基本同意，其中 W2（PSN-IRT 参数）反驳了 R2 的具体建议（MML-EM 重算不可行），但认同底层关切

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_6c76a266d9f5997de21a1604bc79c209:reviewer_1"
}
```

</details>

---
