# reviewer / loop_6.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`046011fe119fce33e395.json`](../../sessions/04/046011fe119fce33e395.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-16T10:20:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-38874 只有 cuda:0（1× RTX PRO 6000 Blackwell 98GB），不存在多卡越界风险，但注意当前 GPU 应空闲
- 论文中 +1.4pp batch composition 结果必须标注 "not statistically significant (p≈0.19)"——此前因 false significance claim 被我 CRITICAL 打回过两次
- 所有 decomposition 条件（graph coloring / random / single-type）均使用 oracle routing，论文中必须显式声明
- FewRel count=40 必须写 "40-rel subsets sampled from the 80-relation pool"（约束 C001）
- BCS 定义已统一为 MEAN（D038），不要用 MAX

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874(root)，工作目录 /root/schema-dag-extraction
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction
- 论文源文件：本地 workspace `docs/paper/` 下（main.tex, results.tex, introduction.tex, abstract.tex, discussion.tex, sdgd_negative.tex, experimental_setup.tex, related.tex）
- 数据：服务器 data/fewrel_parquet/, artifacts/ 下各实验结果
- SCS 矩阵：artifacts/fewrel_qwen3_sim_matrix.pt, artifacts/maven_minilm_sim_matrix.pt 等
- 模型：Qwen3-32B-FP8 via vLLM（本地服务器），cross-model 用 Llama-3.1-8B-Instruct
- 活跃进程：无（GPU 空闲）
- exp-017 GPT-4o-mini：已 killed（TUM proxy 不可用）

### 3. 📊 当前状态
**刚完成**：D044 framing rewrite 全流程审查（Round 4 审稿反馈驱动的全文降调修正）。我审查了 4 轮 Worker 提交：
1. D044 framing rewrite（Title/Abstract/Intro）— 发现并修复 MAVEN 语义倒置 CRITICAL
2. exp_fewrel_partial_corr_freq（CPU 实验）— FewRel 完全均衡，frequency confound 不成立
3. D044 critical fixes（Conclusion 一致性 + quasi-experimental 统一）— PASS
4. §4 fixes（C3 80-rel null result 提升 + S10 tautology + amplification 论证）— PASS
5. §5 + Discussion 扩展 — 发现 2 个 WARNING（chunk boundary 术语 + SCS>0.75 阈值未验证）

**Registry RUNNING/PREPARING**：无活跃实验。全部 DONE 或 killed。

**等待中**：
- Worker 可能会提交 §5 chunk boundary 术语修复 + SCS threshold 措辞修改
- Action matrix 中 S1(MAVEN scope), S2(embedding 不一致+循环性), S5(加 figure), S11(orphan bib) 尚未安排 Worker

### 4. 📋 待办
- §5 terminology fix Worker 回调 → 验证 "chunk boundaries" 改为准确描述、SCS>0.75 改为软性措辞或有数据支撑
- S2 embedding 段落 Worker 回调 → 核实是否提到 MiniLM r=0.172 > Qwen3 r=0.112 消除循环性疑虑
- S11 bib 清理 Worker 回调 → 检查 orphan 条目删除 + 新引用添加
- 最终 PDF 编译 → 用 paper-visual-review skill 检查排版（页数是否≤8、figure 渲染、表格溢出）
- 如果 Director 决定提交 → 做最终数值一致性扫描（abstract/intro/results/conclusion 的所有数字交叉验证）

### 5. 🎯 战略上下文
**核心结论**：Schema-induced degradation 通过两个可分离 channel 运作——count→recall decline, confusability→type confusion。Pairwise SCS 预测 confusion（r=0.112-0.129），batch-level R²=22-53%。效果在 typical batching 下 modest（2-4pp），extreme-batch 下显著（31.2pp）。

**D044 后论文定位**：从 "confusability drives degradation" 降调为 "confusability shapes degradation, is statistically detectable and theoretically informative, but practically modest under typical sampling"。目标 EMNLP 2026 ARR May 25，Main track 提交但 Findings 是合理落点。

**最容易判断错的事**：
1. 不要被 31.2pp 的 extreme-batch gap 误导——这是人工构造的最大 BCS 对比，typical-batch 差异只有 2-4pp。abstract/intro 已反转 framing，后续修改不要退回 31.2pp 为 headline
2. Registry exp-018 single_pass 值 0.8188 是错的（应为 0.504），results.json 是真值——如果需要更新 registry metrics 注意用 results.json 而非 registry 现有值
3. MAVEN 是 same-domain schema，不是 cross-domain——此前 Worker 写反过一次
4. FewRel 是完全均衡数据集（700 samples/type），type frequency 不是 confound——这是论文的天然优势，应该在 §4 中提及
5. 论文 Limitations #6 说 "correlational evidence"，§4.3 用 "controlled stratified comparison"——这两个已经统一过，不要再改回 "quasi-experimental"


---
