# redundancy-compound-sparsity — Research Dashboard

> 最后更新: 2026-05-12 04:07 UTC | 更新原因: D006: Reviewer战略评估确认EMNLP投稿不可行，诚实更新dashboard

## 核心方向
**Cross-axis redundancy hypothesis（KV similarity → MLP sparsity tolerance）的系统性验证。**
当前结论：假设在已测试的所有条件下均未获得足以支撑论文 claim 的正面证据。继续 confound 对照实验以理解现象本身。

## 当前进展
- **阶段**: Research — 诚实评估（D006: EMNLP 2026 投稿不可行）
- **目标**: ~~EMNLP 2026 ARR (DDL: 2026-05-25)~~ → 待用户决定
- **GPU**: seetacloud-bjb2-structtts (1× RTX 5090 32GB)
- **成功率**: 0/7 已完成实验产出可用正面 claim
- **关键问题**:
  - Δpert=+6.6% 在 Llama 上跨 sparsity 恒定 → 无差异化预测力
  - kv-bench-002 设计失败（文本 194 tokens，eviction 未触发）
  - paper_framing SUSPENDED（MLA 误判 + generation regime novelty 不足）
  - 连续 4 次 pivot（D003→D004→D005→?），rationalization 模式

## 近期任务
- [ ] **confound-ctrl-001**: 等待结果（科学价值，非投稿导向）
- [ ] confound-ctrl-002: Qwen2-7B-Instruct 对照
- [ ] 修复分析文件中的 MLA 误标（llama_vs_deepseek_analysis.py, llama_vs_deepseek_summary.md）
- [ ] 更新 kv-bench-002 registry 状态（PREPARING → DONE）
- [ ] **待用户决定**: 是否放弃 EMNLP 2026，转为扎实研究后投下一轮

## GPU 预算
- 当前: seetacloud-bjb2-structtts (1× RTX 5090 32GB)
- 已用: ~6h | confound 对照: ~4h
- 注意: confound-ctrl 完成后如用户决定不投 EMNLP，GPU 可释放或用于扎实的后续研究

## Reviewer 战略评估摘要 (2026-05-12)
- Δpert 恒定 → cross-axis claim 实践上不成立
- kv-bench-002 无效 → Claim 4 零支撑
- "Generation regime dependence" novelty 不足
- 识别到 rationalization 模式，建议停止为凑 DDL 而 pivot

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D006 | 2026-05-12 | EMNLP 2026 投稿不可行 — 0 个有效正面 claim，建议用户放弃本轮 DDL，转为扎实 | mvp-001, mvp-001b, mvp-001c, neg-cross-model-001, llama-sparsity-sweep, kv-bench-002, confound-ctrl-001 |
| D005 | 2026-05-12 | D004 架构误判修正：DeepSeek-R1-Distill-Qwen-7B 是 GQA 不是 M | mvp-001b, neg-cross-model-001, confound-ctrl-001 |
| D004 | 2026-05-12 | Narrative 升级为 Option A: Architecture-Dependent Cro | mvp-001b, mvp-001c, neg-cross-model-001 |
| D003 | 2026-05-11 | MVP FAIL — 跨轴假设不成立，选择 Option B: 负面证据 + O(1) KV evi | mvp-001, mvp-001b |
| D002 | 2026-05-11 | 服务器切换：home-1x5090 → seetacloud-bjb2-structtts（唯一允许 | — |
| D001 | 2026-05-11 | MVP 用 DeepSeek-R1-Distill-Qwen-7B 在 RTX 5090 上验证跨轴 | — |


