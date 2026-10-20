# Step 5 Reviewer Report

## Critical Issues (必须修复)

- **[experiments.tex:79]** Phase 1 adaptive mixing comparison 整个 section 是 `\todo{}` 占位符，没有实际内容。论文 Abstract、Introduction、Conclusion 都 claim 了 C3（closed-loop controller + signal attenuation paradox），但 Experiments 中没有任何支撑数据。这是论文最严重的完整性缺陷。

- **[全文]** 缺少所有 Figure 环境。论文引用了 `Figure~\ref{fig:spectral_trajectory}`（experiments.tex:59）和 `Figure~\ref{fig:comparison}`（experiments.tex:79 TODO 中），但没有任何 `\begin{figure}` 定义。编译后会产生 `[??]` 引用。

- **[experiments.tex:56, abstract.tex:5, introduction.tex:20, conclusion.tex:3]** 2.43× 加速率数据不一致。论文声称 "Phase III (Gen 4-10) 的 per-generation decline rate 是 Phase II (Gen 2-4) 的 2.43×"，但从 Table 1 数据验证：
  - 绝对值：Phase II = 5.39/gen, Phase III = 7.20/gen → **1.34×**
  - 百分比且 Phase II 仅用 Gen 2→3：Phase II = 0.63%/gen, Phase III = 1.54%/gen → **2.44×**
  - 百分比且 Phase II 用完整 Gen 2-4：Phase II = 1.09%/gen, Phase III = 1.54%/gen → **1.41×**
  
  2.43× 仅在 Phase II 缩窄为 Gen 2→3 单代且使用百分比时可复现，但论文文字明确写的是 "Phase II (Gen 2-4)"。需要修正数字或修正 Phase 定义。

## Major Issues (建议修复)

- **[experiments.tex:8]** 写 "four spectral indicators" 但实际只列了三个（effective rank, SLV, leading singular value），然后接 "and three downstream metrics"。应改为 "three spectral indicators"。

- **[experiments.tex:8 vs method.tex:9]** SLV 公式记法不一致。method.tex 写 `$\frac{1}{2} \log \det \mathbf{G}$`，experiments.tex 写 `$\log \det \mathbf{G}^{1/2}$`。数学上等价，但记法应统一。

- **[全文]** "Early Warning Signals" 出现在标题中，但相关 EWS 文献完全没有引用。references.bib 中有 scheffer2009ews、bury2021deeplearning、dakos2012methods 三篇核心 EWS 文献，但均未在正文中 cite。审稿人会立刻注意到标题核心概念缺少文献支撑。

- **[全文]** 12 条 bib 条目未被引用：dohmatob2024demystified, naderi2025mindgap, chen2025aioli, kazdan2024collapsethrive, gudibande2024falsepromise, feng2024verification, keisha2025knowledge, briesch2023entropy, gao2020pile, garg2025, scheffer2009ews, bury2021deeplearning, dakos2012methods。其中部分应纳入 Related Work 以增强引用覆盖度，其余应删除以保持 bib 整洁。

- **[experiments.tex, method.tex]** "distinct-4" 指标未定义。读者无法知道这是 unique 4-gram ratio 还是其他定义。首次使用时需给出定义。

- **[experiments.tex, method.tex]** "EMA" 缩写未展开。method.tex:34 直接写 "EMA-smoothed SLV"，应写 "exponential moving average (EMA)"。

- **[experiments.tex]** HellaSwag 没有引用。作为核心评估指标之一，应引用原论文（Zellers et al., 2019）。

- **[experiments.tex]** OpenWebText 数据集没有引用。

## Minor Issues (可选修复)

- **[main.tex]** Related Work 在 Experiments 之后（Section 4）。EMNLP short paper 允许此布局，但更常见的做法是放在 Method 之前或 Introduction 之后。

- **[abstract.tex:4]** Abstract 中提到 "Pythia-410M" 和 "Pythia-1B"，但未说明这是 EleutherAI 的模型。对不熟悉 Pythia 的读者可能不够清晰。

- **[method.tex:34]** Controller 参数 $\widetilde{S}_0$ 的初始值 "SLV${}=2366.68$" 直接写死在正文中。这个数字来自 Table 1 Gen 0 行，应通过引用表格而非硬编码。

- **[conclusion.tex:10]** "Future work should explore cumulative indicators that do not rely on per-generation deltas, validate the three-phase pattern at larger scales and over longer generation horizons, and develop controller architectures that remain effective as their own interventions dampen the collapse signal." 这是一个过长的单句（42 words），建议拆分。

- **[main.tex:3]** 使用 `\usepackage[review]{acl}` 包。确认 EMNLP ARR 接受 ACL 模板（通常是的，因为共用 acl.sty，但应确认年份版本）。

## AI Style Markers Found

- **[related_work.tex:24]** "...during recursive training, guided by real-time spectral feedback from the model's own representations rather than a priori proxy estimates." — -ing 分词短语结尾（"guided by..."），典型 AI 写作模式。建议改写为独立从句。

- 无 em-dash (—) ✓
- 无解释性 en-dash ( – ) ✓
- 无连续 Furthermore/Moreover/Additionally ✓
- 无黑名单用词 (delve/leverage/utilize/facilitate/myriad/plethora) ✓
- 无 "Notably" / "It is worth noting" ✓
- 分段节奏合理，无过度分段 ✓

## Summary

论文核心叙事（三阶段谱坍缩 + SLV 作为监测指标）连贯且有说服力，Phase 0 实验数据充实、表格清晰。AI 写作痕迹极少，语言质量高于平均投稿。

最严重的问题是 **Phase 1 实验结果完全缺失**（\todo 占位符），导致 C3 贡献（controller + signal attenuation paradox）没有数据支撑——这三项内容在 Abstract、Introduction、Conclusion 中都被 claim，但 Experiments 中是空白。其次，**2.43× 加速率与 Table 1 数据不一致**（按论文定义的 Phase II Gen 2-4 计算得 ~1.4×，非 2.43×），以及**标题中的 "Early Warning Signals" 概念缺少 EWS 文献引用**。

改进优先级：(1) 补全 Phase 1 实验结果或删除 C3 claim；(2) 修正/验证 2.43× 数字；(3) 添加 EWS 核心文献引用；(4) 补全缺失 Figure 环境；(5) 统一公式记法和术语定义。
