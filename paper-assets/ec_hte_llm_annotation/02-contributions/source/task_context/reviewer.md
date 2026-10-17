---
loop: 4
reason: max_wall_time
updated: '2026-05-25T03:22:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目是纯理论+模拟实验，**无 GPU 训练**。服务器仅用于 MC 模拟（CPU-bound）和论文编译
- **etaiwi2025comparative (arXiv:2506.18501)** 引用已验证真实存在，但论文中数字从 "GPT-4 at ~85%" 已修正为 "~80%"。如有人再动这个引用，必须保持修正后的版本
- **Abstract ≤200 words** (EMNLP 2026 ARR 硬约束)，当前约 160 词
- **主文 ≤8 页**，当前刚好 8 页（Conclusion 在第 8 页，Limitations 从第 8 页开始）。任何新增文字必须同步裁剪等量空间
- 一篇文章**只能有一个 limitations section**，在正文里，appendix 不能有
- Remark 引用统一用 `\ref{rem:asymmetric}`，不要硬编码 "Remark 1" 或 "Remark 2"

### 2. 🖥️ 基础设施快照
- 服务器：`local-cpu(root)` + `autodl-ec-hte(root)`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/`
- 论文源码：`docs/paper/` 下（abstract.tex, introduction.tex, theory.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex, appendix_agnews.tex, references.bib）
- 远程代码根目录：`/root/ec_hte_llm_annotation`
- 无活跃进程/训练/tmux/cron。所有 43 个实验均为 DONE 状态
- 无 wandb 配置（本项目不用 wandb）

### 3. 📊 当前状态
**我刚完成 R21 审稿报告的 Action Matrix 独立审查并提交给 Director。**

审稿分数轨迹：R17=3.5 → R18=3.0 → R20=3.5 → R21=3.5（Borderline Conference）。

已完成的关键修复（全部验证通过）：
- C1: Abstract R² 表述修正（aggregate 0.975 + per-model 0.76-0.99）✅
- C2: AUC=1.0 从 Abstract 移除（5 轮后终于修复）✅
- C3: 7.4× 加 "under extreme heterogeneity" ✅
- A2 假设降级为 "expository simplification" + Remark 2 完整非对称处理 ✅
- "eliminates sign reversal entirely" → "in the primary K=2 configuration"（intro + experiments 同步）✅
- AG News 引用修正（GPT-4→generic LLM, 85%→80%）✅
- "16 CMs" 计数一致性修复 ✅
- Figure 2 色盲修复（green→blue）✅
- Noisy label learning 段落新增（Natarajan 2013, Patrini 2017, Cheng 2020）✅
- F-L nesting statement 新增 ✅
- Conclusion 扩展到 3 句 ✅

**等待 Director 对 R21 修复方案的决策**，然后 worker 实施后需要验证。

### 4. 📋 待办
- R21 修复 worker 完成 → 逐条验证（重点：SF7 数值示例、MF3 sign reversal novelty statement、MF1 诊断 matrix vs scalar 前置区分）
- Knox 2020 + Blette 2024 补回 appendix extended related work → 验证 \cite 存在
- R21-REF1 Veitch 2020 + Wood-Doughty 2018 bib 条目 → 验证引用真实性（未做过）
- 论文最终提交前 → 全文一致性扫描（Abstract/Intro/Experiments/Conclusion 数字对齐、\ref 交叉引用完整性）
- 如收到 paper_agent_request_review → 用 §5.3 模板评分（维度 1-4 + Overall 1-10 + checklist）

### 5. 🎯 战略上下文
- **核心贡献**：bias identity（δ_s · Δτ / (1-2π̄)）是精确恒等式，sign reversal 14.9% 是最有冲击力的数字，EC-HTE 是 "one concrete instantiation"（15% 权重）
- **贡献结构**：60% Identity+SignReversal / 25% "When NOT to correct" / 15% EC-HTE。不要再改这个比例
- **3.5 分停滞的根因是结构性的**：(1) causal methods paper at NLP venue = venue fit tension; (2) synthetic-only evaluation; (3) scalar form prominent but degrades under asymmetry。写作修复只能维持不能突破。不要建议降级 venue 或降级 claim——Rebuttal 才是翻分关键
- **易判断错的事**：
  - "R² as low as 0.08" 是错的（那是 max|[B_s]_{z,1}| 列被误读），实际最低 per-model R²=0.756
  - R² 0.73 vs 0.975 不矛盾（前者是 per-config minimum at Δπ≥0.10，后者是 aggregate pooled R²）
  - "EC-HTE eliminates sign reversal entirely" 是假命题（stance 3.3%、AG News 3% 残留），所有相关文本已改为 "in the primary K=2 configuration"
  - Abstract 说 "under symmetric errors (generalizing to...)" 是刻意措辞——不要改回 "under symmetric misclassification"，那会过度限缩贡献
- **最容易踩的坑**：改一处数字/表述后忘记同步其他文件。Abstract、Intro contributions、Experiments、Conclusion 四处必须交叉检查一致性
