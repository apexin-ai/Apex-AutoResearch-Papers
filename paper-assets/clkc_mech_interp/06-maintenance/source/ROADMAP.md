# clkc_mech_interp — Research Dashboard

> 最后更新: 2026-05-26 09:47 UTC | 更新原因: 匿名代码仓库完成 + PAT 清理完成，更新任务清单

## 核心方向
跨语言知识冲突的机制可解释性：residual stream probing 检测冲突、不对称性分析、因果 steering。详见 paper_framing.md。

## 当前进展
**EMNLP 2026 ARR — 论文修复全部完成，待 Round 4 审稿**。评分目标 3.5+（Findings 线以上）。
R3 全部 14 项修复 + 额外 6 项数据一致性修复（3 CRITICAL + 3 WARNING）全部完成。
Figure 1 (Hero) + Figure 2 (Pipeline) PaperBanana 重设计已部署。
check_paper_consistency: 0 critical, 0 warning, 1 info。
匿名代码仓库已完成（artifacts/anonymous_repo.zip, 54K, art_20260526_a56cca）。
Round 4 审稿已提交（apr_20260525T161136_iqqg），等待用户批准审稿模式。

### 策略
- **Claim 收缩**: Mirror→Consistent With; Contribution 3 限定 Llama-specific; COMET tercile 降为辅助
- **Evidence addition**: MLP probe 数据验证非线性假说；selectivity control + AUROC 补充完毕
- **数据一致性**: Abstract/Conclusion/Appendix D-F 全部与实验数据对齐
- **匿名代码仓库**: ✅ 已完成（zip 已打包，提交前确认 abstract footnote URL 一致）
- **Figure 1 + Figure 2 重设计**: ✅ 已完成并部署

### Contribution 状态（对应论文 4 点 Contribution）
- **C1 detectability** ✅ 三模型 matched-condition：Llama 90.0% (L13, N=201), Gemma 88.0-89.5% (L16-L18, N=171), Qwen 71.0-72.9% (L13-L15, N=131)
- **C2 asymmetry consistent with XNLI** ✅ 三模型 ~7pp（Consistent With 措辞）
- **C3 detection-decision dissociation (Llama-specific)** ✅ L13 peak 因果节点（matched-condition N=201: L14/L16 也 Bonferroni 显著，因果窗口 L13-L16；论文 provenance 基于原始 N=136 数据，L13 为唯一显著点——见 D021）
- **C4 cross-task transfer + preliminary hypothesis validation** ✅ 合并后的贡献点

### 数据源备注（D021）
论文 steering claims (provenance C023/C045/C047/C062/C068) 基于原始 N=136 数据（steering_107_L13），L13 唯一显著。matched-condition N=201 层扫描显示 L13/L14/L16 三层均 Bonferroni 显著，因果窗口更宽。是否更新论文到 matched-condition 数据待 Round 4 审稿后决定。

## 近期任务
- [x] Paper Agent 6 项修复（数据一致性 + 模板清理 + Figure 重设计）
- [x] check_paper_consistency 全部通过
- [x] 匿名代码仓库完成（zip 打包 + 安全审计通过）
- [x] GitHub PAT 泄露清理
- [ ] Round 4 审稿批准（等待用户批准模式）
- [ ] Round 4 通过后 → OpenReview ARR 表单提交（待用户确认）

## GPU 预算
- westd-14391: 1× RTX PRO 6000 Blackwell (96GB)，当前空闲
- 所有 GPU 实验已完成，无活跃 GPU 需求

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D021 | 2026-05-26 | Matched-condition N=201 层扫描推翻 D019 部分结论：L14/L16 也通 | steering_llama_L13_repl_126, steering_llama_L14_125, steering_llama_L16_127, steering_llama_L16_123 |
| D020 | 2026-05-24 | Detection≠Decision 叙事从 "L28 peak vs L13 causal = 大 | multi_seed_probing |
| D019 | 2026-05-23 | 第二轮 steering 实验全部 negative：Qwen L18、Llama L16、Gemm | steering-qwen-L18-122, steering-llama-L16-123, steering-gemma-L24-121 |
| D018 | 2026-05-23 | 推翻 D016 中 cross-task transfer "不加入"的决定：用户批准加入论文，bo | cross-task-transfer-116, cross-task-bootstrap-119 |
| D017 | 2026-05-23 | Reviewer 独立终审确认：GPU 实验全部完成，无需追加 Gemma 额外 steering  | steering_107_gemma_L17, steering_107_gemma_L21, steering_107_qwen_L14, cross-task-transfer-116 |
| D016 | 2026-05-23 | 三个 piggyback 验证实验完成：cross-task transfer 有价值但不加入当前提 | cross-task-transfer-116, probe-cosine-sim-117, tost-equivalence-118 |
| D015 | 2026-05-22 | C6 steering 确认为 Llama-specific；Gemma L17 informati | steering_107_gemma_L17, steering_107_L13, steering_107_qwen_L14 |
| D014 | 2026-05-22 | Steering L13 SUCCESS (p=0.0009/0.002)! 因果节点在 mid-l | steering_107_L13, steering_107, steering_107_L18, steering_107_L28_all |
| D013 | 2026-05-22 | DDL确认: EMNLP 2026 ARR May 25 (3天), 立即启动论文写作 | mvp_probe_llama_v1, mvp_probe_v1, xnli_baseline_110, steering_107 |
| D012 | 2026-05-22 | D009 撤回：C3 non-linearity 降为 "trend only"，双模型 boots | xnli_baseline_110, mvp_002 |



