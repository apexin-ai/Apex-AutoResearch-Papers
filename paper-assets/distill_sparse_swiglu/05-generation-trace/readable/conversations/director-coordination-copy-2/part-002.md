# Director coordination — Part 2 of 8

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/e0/e0d2e26e51128e828a96.json)

## Round 34

### Tool call

_source line 358 · 2026-05-17T09:32:54.034563+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # === Round 1-2 resolved issues (compact) ===\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"desk-reject 条件\"}]\n    action_items: [{round: 1, action: \"拆为独立 section*\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit 7018701\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2 提出\"}]\n    action_items: [{round: 1, action: \"确认页数\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"8p main + 2p appendix\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1 critical\"}]\n    action_items: [{round: 1, action: \"C4 validation PPL\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"C4: Dense=9.21, KL=18.40, TEAL=38.75\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Structural failure 证据不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"两位独立指出\"}]\n    action_items: [{round: 1, action: \"BCE+Gumbel ×3 LR 对照\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"BCE best=38.02 vs KL=11.79\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融缺关键维度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"全维度 sweep\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Appendix B-C 全覆盖\"\n    resolution_round: 1\n\n  - id: \"R1-W1-Rd2\"\n    summary: \"Lagrangian 术语误用\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items:\n      - {round: 2, action: \"全文术语替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 2, action: \"启发式 schedule 说明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commits fe7c034 + e00d270\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"λ/sparsity 时序曲线缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"遗留修复\"}]\n    action_items: [{round: 2, action: \"Figure 生成+集成\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"lagrangian_dynamics.pdf in Appendix C\"\n    resolution_round: 2\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"需报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"添加 KL/Dense ratio\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"加 scale qualifier\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"30% MMLU 异常缺 per-layer 分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items: [{round: 2, action: \"Retention 分析+叙事修正\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"Late-layer starvation mechanism (commits f22d330 + 377ed61)\"\n    resolution_round: 2\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"引用偏低\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W4: 32篇仍偏低(typical 40-60), 遗漏 MiniLLM/GKD 等\"}\n    action_items:\n      - {round: 2, action: \"补到 30+\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"补 MiniLLM, GKD, SparseLoRA 等至 40+\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"Em-dash AI 写作信号\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"降为 info\"}]\n    action_items: [{round: 2, action: \"全文清理\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"SNR 缺数学定义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"降为 info\"}]\n    action_items: [{round: 2, action: \"§3.5 加公式\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit cb05c11\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 informal\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W4\"}]\n    action_items: [{round: 1, action: \"弱化+SNR\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Gradient-Based Motivation + SNR 5.76×\"\n    resolution_round: 2\n\n  - id: \"R1-W2\"\n    summary: \"Cross-arch 仅 1 点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W2\"}]\n    action_items: [{round: 1, action: \"6-point table\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Cross-arch 6-point table\"\n    resolution_round: 2\n\n  - id: \"R2-N3\"\n    summary: \"与 SPON 区分度不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"per-token vs static\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2-W5 Round 1\"}]\n    action_items: [{round: 1, action: \"加 caveat\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  # === Round 3 issues — status updated per Round 4 findings ===\n\n  - id: \"R3-C1\"\n    summary: \"Responsible NLP Research Checklist + Ethics Statement 缺失\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE. ARR 强制要求。\"}\n      - {round: 4, reviewers: [], note: \"本轮未提及。ethics.tex 已包含 Ethics Statement + 完整 Checklist (A1-E1)。\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 添加 checklist + Ethics Statement\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"ethics.tex 包含完整 Ethics Statement + ARR Responsible NLP Research Checklist\"\n    resolution_round: 4\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect: KL global MMLU≈random, PPL framing 自相矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE. 最严重问题。\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N2 + R2-N3, 交叉全 AGREE. 30% KL global MMLU=25.27%≈random, 比 TEAL 38.61% 差 13pp. Primary protocol KL+global 在所有设定下 MMLU 不可用. Narrative vs evidence 矛盾未解.\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 重写: 诚实呈现 downstream mixed results\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"重新定位 KL+uniform 为推荐配置; Abstract 中 equal prominence 报告 PPL 改善和 downstream degradation; 明确 global allocation 作为分析对象而非推荐方案\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C3\"\n    summary: \"无 wall-clock speedup, efficiency framing 误导\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N2, R1-W2. R1 介于 critical/warning. 6.4% overhead 事实不变. Abstract 仍未明确声明无 speedup. Conclusion 仍提 wall-clock 作 future direction (与 understanding framing 矛盾).\"}\n    action_items:\n      - {round: 3, action: \"D047 reframe: understanding paper, 明确声明无 speedup\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"Abstract 明确 'prediction quality, not wall-clock speedup'; Conclusion 删除 efficiency future direction 或改为 analysis-oriented\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C4\"\n    summary: \"Train-inference mask mismatch 未量化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE with nuance.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W3, R2 AGREE. soft mask(τ=0.1) vs hard top-k gap 仍未 clean 分离. §4.5 gap decomposition 混合了 discretization 和 allocation 两个效应. 需要: soft per-token→hard per-token (隔离 discretization) + hard per-token→hard global (隔离 allocation).\"}\n    action_items:\n      - {round: 3, action: \"per-token hard eval\", assigned_to: \"main_agent\", status: in_progress}\n      - {round: 4, action: \"补充 soft→hard per-token PPL 对比, 干净分离 discretization vs allocation gap\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S1\"\n    summary: \"MaskLLM 技术重叠讨论不足 → 升级: 核心新颖性与 MaskLLM 区分不足\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise critical, R1 REBUT → 降 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N1 升为 critical, R1 交叉 AGREE. 共享 frozen weights+Gumbel+KL 范式, 本文 delta 是 weight→activation sparsity 迁移. Structural mismatch 分析是 task-specific 适配非通用洞察. 唯一方法新增是 multiplicative penalty (augmented Lagrangian heuristic). 建议重定位为 empirical analysis paper.\"}\n    action_items:\n      - {round: 3, action: \"Related Work 添加 MaskLLM 深度对比段\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"实验性区分: 测试 MaskLLM-style baseline 在 activation sparsity 上的表现; 或重定位为 empirical analysis contribution 而非 method contribution\", assigned_to: \"paper_agent+main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S2\"\n    summary: \"BCE 对比是 pipeline 差异非仅 loss 差异\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N3 (critical), R2 REBUT→warning. R2 认为 Table 3 ablation 虽不完美但 reasonable. 共识: warning. 缺 MSE intermediate ablation 和 per-layer KL ablation. '6.6× loss effect' 计算混淆变量.\"}\n    action_items:\n      - {round: 3, action: \"§4.3 明确说明 loss+infrastructure 组合\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"补充 MSE on hidden states ablation (intermediate coupling); 补充 per-layer KL ablation (解耦 cross-layer Jacobian); 修正 claim 为 'KL+Gumbel+Penalty 组合优势' 而非单独 loss\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S4\"\n    summary: \"仅 7-8B 实验规模\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W5, R2 AGREE. Title 'SwiGLU LLMs' 过于宽泛. 建议限定 '7-8B SwiGLU LLMs' 或补充 13B.\"}\n    action_items:\n      - {round: 3, action: \"已有 scale qualifiers, 进一步弱化\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"Title 加 '7-8B' 限定词; 或补充至少 1 个 13B 模型\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S5\"\n    summary: \"Regime 分析证据不足 (6 数据点)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W1 + R2-W3, 交叉全 AGREE. 每 regime 仅 1 数据点. 30%→40% preference reversal 边界未定位. Mistral 无 downstream regime 数据. 措辞应降为 'preliminary observations'.\"}\n    action_items:\n      - {round: 3, action: \"降为 empirical observation on 7-8B models\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"补充 35%/45% 数据点定位 regime boundary; 或降级措辞为 'non-monotonic behavior suggestive of distinct operating regimes'\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S6\"\n    summary: \"'Parameter-free' penalty controller 不准确\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W6 新角度: §3.4 claim 'converges within 40-110 steps across all targets' 与 30%/70% λ hit cap (saturation, not convergence) 矛盾. 30% deviation=5.0%.\"}\n    action_items:\n      - {round: 3, action: \"删除 parameter-free, 承认 λ_max\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"区分 'convergence' 和 'saturation at cap'; 修正 §3.4 convergence claim; 讨论 cap saturation 对训练质量的影响\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S7\"\n    summary: \"D2DMoE 遗漏 → 扩展: D2DMoE taxonomy positioning 不准确 + 更多 missing refs\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W5: D2DMoE 归为 'Intermediate(MSE)' 过度简化, 其训练含 router+expert conversion. R2-W4: 遗漏 MiniLLM(ICLR 2024, forward vs reverse KL), SparseLoRA(ICML 2025), GKD 等. 32 篇引用偏少(typical 40-60).\"}\n    action_items:\n      - {round: 3, action: \"引用 + 更新 Table 1\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"核实 D2DMoE 训练信号, 更新 taxonomy 分类; 补 MiniLLM/GKD/SparseLoRA 引用至 40+; 讨论 forward vs reverse KL 与 MiniLLM 结论差异\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S8\"\n    summary: \"Abstract 数字堆砌 / PPL-centric 叙事\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"本轮以 R2-N3/R1-N2 形式复发: Abstract headline 是 '49% PPL reduction' 但 downstream collapse 未获 equal prominence. 数字堆砌问题与叙事失衡问题合并.\"}\n    action_items:\n      - {round: 3, action: \"精简到 3-4 核心数字, 叙事驱动\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"合并入 R3-C2 处理: Abstract 同等权重报告 PPL 改善和 downstream 退化\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S9\"\n    summary: \"Taxonomy 5/9 cells 空, post-hoc 质疑\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 部分 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W2: post-hoc 无 predictive power. R1 交叉部分 REBUT (有 organizational utility) 但同意: 不应作独立 contribution; 空 cell 未讨论原因. 共识: taxonomy 降为 Related Work 组织框架, 从 contribution list 移除.\"}\n    action_items:\n      - {round: 3, action: \"补 DejaVu/D2DMoE + 讨论轴选择依据\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"Taxonomy 从 contribution list 移除, 降为 Related Work 组织框架; 讨论空 cell 原因\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M\"\n    summary: \"11 条 minor (AdamW wd, BCE threshold, ShadowLLM, bib years, GPU, -ing phrases, Figure label, Conclusion 过短等)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"混合来源\"}\n      - {round: 4, reviewers: [1, 2], note: \"部分复发: bib xu2026spon key/year 不一致(R1+R2 均提); SPON eval protocol 不同(R1+R2 P1); d030 exp_id naming 问题(见 R4-W1). AI 写作痕迹已清理(R2-S5 确认无 em-dash 等).\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 批量修复\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"修复 bib key; 统一 SPON eval protocol 或更显著标注差异\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"6.4% 延迟与效率叙事矛盾\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7 Round 1\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-C3 再次 raise\"}\n      - {round: 4, reviewers: [1, 2], note: \"合并入 R3-C3 处理. 6.4% overhead 事实不变.\"}\n    action_items:\n      - {round: 1, action: \"Reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 3, action: \"understanding paper not efficiency paper\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"三 seed 统计效力弱 → 升级: 主表全部单 seed\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出, R2 REBUT\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-S3, 升为 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W4, R2 AGREE. Table 2 所有关键对比单 seed. '49% PPL reduction' 无 error bars. 30% MMLU=25.27% 若有 ±2pp variance 可能与 random 无显著差异. 3-seed 仅限 50% uniform 一个配置.\"}\n    action_items:\n      - {round: 3, action: \"标注已有 4-seed mean±0.07\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"Table 2 关键行 (KL global 30%/50%, TEAL 30%/50%) 做 3-seed 评估; 报告 downstream metrics 的 seed variance\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 4 new issues ===\n\n  - id: \"R4-C1\"\n    summary: \"PPL 22.51 幽灵数字: 贯穿 Abstract/Intro/§4.3 的 '91% worse PPL' claim 无表格数据支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [1, 2], note: \"R1-N1 raise, R2 交叉强 AGREE. 22.51 不出现在任何表格. Table 2 BCE=27.97(137% worse). experiments.tex:65-66 同段出现 22.51 和 27.97 指向同一 exp_id. 数据溯源链断裂.\"}]\n    action_items:\n      - {round: 4, action: \"确认 22.51 来源(1000-step BCE?), 在 Table 2 或 Table 3 补充对应数据行; 或用 Table 中已有数字(27.97)重算百分比并全文替换 '91%'\", assigned_to: \"paper_agent+main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W1\"\n    summary: \"d030 exp_id 暗示 regime analysis 使用了错误 sparsity target 的 predictor\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [2], note: \"交叉分享中发现. d030_kl40_uniform/d030_kl50_uniform 命名暗示用 30%-trained predictor. 若属实, Table 5 caption 'each row uses a predictor trained at the respective sparsity target' 是虚假陈述, 整个 regime analysis 的 global vs uniform preference reversal 可能是 artifact.\"}]\n    action_items:\n      - {round: 4, action: \"确认 d030 前缀含义: 是 predictor training target 还是 batch 编号; 若确为 30%-trained predictor, 重跑 40%/50%-trained uniform 或修正 Table 5 caption\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"Structural mismatch 洞察新颖性: end-to-end > decomposed 是深度学习基本原则\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [1, 2], note: \"R2-W1, R1 交叉 AGREE. §3.5 梯度分析本质是 chain rule 标准应用. Factor (b) Jacobian 耦合是任何 end-to-end loss 固有性质. 但 'F1 高反而 PPL 差' 的 empirical finding 有价值. 建议降低 formal analysis 权重, 强调 empirical 验证.\"}]\n    action_items:\n      - {round: 4, action: \"降低 'structural mismatch' 在叙事中的理论权重; 强调 empirical finding (F1-PPL disconnect) 而非 gradient formalism\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"Training/evaluation domain overlap: WikiText-103 训练 + WikiText-2 评测, OOD 仅 50%\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [1, 2], note: \"R2-W6, R1 部分 REBUT (relative advantage 保持). 但 OOD 仅 50% 一个 sparsity, 缺 30%/40% OOD. C4 PPL 18.40 vs WikiText-2 11.79 (56% higher), dense gap 类似(50.5%). Relative advantage 保持(49%→52.5%).\"}]\n    action_items:\n      - {round: 4, action: \"补充 30%/40% sparsity 的 C4 OOD 评估; 将 OOD 结果放入主表或正文并行报告\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # === Round 1-2 resolved issues (compact) ===\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"desk-reject 条件\"}]\n    action_items: [{round: 1, action: \"拆为独立 section*\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit 7018701\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2 提出\"}]\n    action_items: [{round: 1, action: \"确认页数\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"8p main + 2p appendix\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1 critical\"}]\n    action_items: [{round: 1, action: \"C4 validation PPL\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"C4: Dense=9.21, KL=18.40, TEAL=38.75\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Structural failure 证据不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"两位独立指出\"}]\n    action_items: [{round: 1, action: \"BCE+Gumbel ×3 LR 对照\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"BCE best=38.02 vs KL=11.79\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融缺关键维度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"全维度 sweep\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Appendix B-C 全覆盖\"\n    resolution_round: 1\n\n  - id: \"R1-W1-Rd2\"\n    summary: \"Lagrangian 术语误用\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items:\n      - {round: 2, action: \"全文术语替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 2, action: \"启发式 schedule 说明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commits fe7c034 + e00d270\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"λ/sparsity 时序曲线缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"遗留修复\"}]\n    action_items: [{round: 2, action: \"Figure 生成+集成\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"lagrangian_dynamics.pdf in Appendix C\"\n    resolution_round: 2\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"需报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"添加 KL/Dense ratio\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"加 scale qualifier\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"30% MMLU 异常缺 per-layer 分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items: [{round: 2, action: \"Retention 分析+叙事修正\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"Late-layer starvation mechanism (commits f22d330 + 377ed61)\"\n    resolution_round: 2\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"引用偏低\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W4: 32篇仍偏低(typical 40-60), 遗漏 MiniLLM/GKD 等\"}\n    action_items:\n      - {round: 2, action: \"补到 30+\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"补 MiniLLM, GKD, SparseLoRA 等至 40+\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"Em-dash AI 写作信号\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"降为 info\"}]\n    action_items: [{round: 2, action: \"全文清理\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"SNR 缺数学定义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"降为 info\"}]\n    action_items: [{round: 2, action: \"§3.5 加公式\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit cb05c11\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 informal\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W4\"}]\n    action_items: [{round: 1, action: \"弱化+SNR\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Gradient-Based Motivation + SNR 5.76×\"\n    resolution_round: 2\n\n  - id: \"R1-W2\"\n    summary: \"Cross-arch 仅 1 点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W2\"}]\n    action_items: [{round: 1, action: \"6-point table\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Cross-arch 6-point table\"\n    resolution_round: 2\n\n  - id: \"R2-N3\"\n    summary: \"与 SPON 区分度不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"per-token vs static\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2-W5 Round 1\"}]\n    action_items: [{round: 1, action: \"加 caveat\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  # === Round 3 issues — status updated per Round 4 findings ===\n\n  - id: \"R3-C1\"\n    summary: \"Responsible NLP Research Checklist + Ethics Statement 缺失\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE. ARR 强制要求。\"}\n      - {round: 4, reviewers: [], note: \"本轮未提及。ethics.tex 已包含 Ethics Statement + 完整 Checklist (A1-E1)。\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 添加 checklist + Ethics Statement\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"ethics.tex 包含完整 Ethics Statement + ARR Responsible NLP Research Checklist\"\n    resolution_round: 4\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect: KL global MMLU≈random, PPL framing 自相矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE. 最严重问题。\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N2 + R2-N3, 交叉全 AGREE. 30% KL global MMLU=25.27%≈random, 比 TEAL 38.61% 差 13pp. Primary protocol KL+global 在所有设定下 MMLU 不可用. Narrative vs evidence 矛盾未解.\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 重写: 诚实呈现 downstream mixed results\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"重新定位 KL+uniform 为推荐配置; Abstract 中 equal prominence 报告 PPL 改善和 downstream degradation; 明确 global allocation 作为分析对象而非推荐方案\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C3\"\n    summary: \"无 wall-clock speedup, efficiency framing 误导\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N2, R1-W2. R1 介于 critical/warning. 6.4% overhead 事实不变. Abstract 仍未明确声明无 speedup. Conclusion 仍提 wall-clock 作 future direction (与 understanding framing 矛盾).\"}\n    action_items:\n      - {round: 3, action: \"D047 reframe: understanding paper, 明确声明无 speedup\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"Abstract 明确 'prediction quality, not wall-clock speedup'; Conclusion 删除 efficiency future direction 或改为 analysis-oriented\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C4\"\n    summary: \"Train-inference mask mismatch 未量化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE with nuance.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W3, R2 AGREE. soft mask(τ=0.1) vs hard top-k gap 仍未 clean 分离. §4.5 gap decomposition 混合了 discretization 和 allocation 两个效应. 需要: soft per-token→hard per-token (隔离 discretization) + hard per-token→hard global (隔离 allocation).\"}\n    action_items:\n      - {round: 3, action: \"per-token hard eval\", assigned_to: \"main_agent\", status: in_progress}\n      - {round: 4, action: \"补充 soft→hard per-token PPL 对比, 干净分离 discretization vs allocation gap\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S1\"\n    summary: \"MaskLLM 技术重叠讨论不足 → 升级: 核心新颖性与 MaskLLM 区分不足\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise critical, R1 REBUT → 降 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N1 升为 critical, R1 交叉 AGREE. 共享 frozen weights+Gumbel+KL 范式, 本文 delta 是 weight→activation sparsity 迁移. Structural mismatch 分析是 task-specific 适配非通用洞察. 唯一方法新增是 multiplicative penalty (augmented Lagrangian heuristic). 建议重定位为 empirical analysis paper.\"}\n    action_items:\n      - {round: 3, action: \"Related Work 添加 MaskLLM 深度对比段\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"实验性区分: 测试 MaskLLM-style baseline 在 activation sparsity 上的表现; 或重定位为 empirical analysis contribution 而非 method contribution\", assigned_to: \"paper_agent+main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S2\"\n    summary: \"BCE 对比是 pipeline 差异非仅 loss 差异\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N3 (critical), R2 REBUT→warning. R2 认为 Table 3 ablation 虽不完美但 reasonable. 共识: warning. 缺 MSE intermediate ablation 和 per-layer KL ablation. '6.6× loss effect' 计算混淆变量.\"}\n    action_items:\n      - {round: 3, action: \"§4.3 明确说明 loss+infrastructure 组合\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"补充 MSE on hidden states ablation (intermediate coupling); 补充 per-layer KL ablation (解耦 cross-layer Jacobian); 修正 claim 为 'KL+Gumbel+Penalty 组合优势' 而非单独 loss\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S4\"\n    summary: \"仅 7-8B 实验规模\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W5, R2 AGREE. Title 'SwiGLU LLMs' 过于宽泛. 建议限定 '7-8B SwiGLU LLMs' 或补充 13B.\"}\n    action_items:\n      - {round: 3, action: \"已有 scale qualifiers, 进一步弱化\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"Title 加 '7-8B' 限定词; 或补充至少 1 个 13B 模型\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S5\"\n    summary: \"Regime 分析证据不足 (6 数据点)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W1 + R2-W3, 交叉全 AGREE. 每 regime 仅 1 数据点. 30%→40% preference reversal 边界未定位. Mistral 无 downstream regime 数据. 措辞应降为 'preliminary observations'.\"}\n    action_items:\n      - {round: 3, action: \"降为 empirical observation on 7-8B models\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"补充 35%/45% 数据点定位 regime boundary; 或降级措辞为 'non-monotonic behavior suggestive of distinct operating regimes'\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S6\"\n    summary: \"'Parameter-free' penalty controller 不准确\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W6 新角度: §3.4 claim 'converges within 40-110 steps across all targets' 与 30%/70% λ hit cap (saturation, not convergence) 矛盾. 30% deviation=5.0%.\"}\n    action_items:\n      - {round: 3, action: \"删除 parameter-free, 承认 λ_max\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"区分 'convergence' 和 'saturation at cap'; 修正 §3.4 convergence claim; 讨论 cap saturation 对训练质量的影响\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S7\"\n    summary: \"D2DMoE 遗漏 → 扩展: D2DMoE taxonomy positioning 不准确 + 更多 missing refs\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W5: D2DMoE 归为 'Intermediate(MSE)' 过度简化, 其训练含 router+expert conversion. R2-W4: 遗漏 MiniLLM(ICLR 2024, forward vs reverse KL), SparseLoRA(ICML 2025), GKD 等. 32 篇引用偏少(typical 40-60).\"}\n    action_items:\n      - {round: 3, action: \"引用 + 更新 Table 1\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"核实 D2DMoE 训练信号, 更新 taxonomy 分类; 补 MiniLLM/GKD/SparseLoRA 引用至 40+; 讨论 forward vs reverse KL 与 MiniLLM 结论差异\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S8\"\n    summary: \"Abstract 数字堆砌 / PPL-centric 叙事\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"本轮以 R2-N3/R1-N2 形式复发: Abstract headline 是 '49% PPL reduction' 但 downstream collapse 未获 equal prominence. 数字堆砌问题与叙事失衡问题合并.\"}\n    action_items:\n      - {round: 3, action: \"精简到 3-4 核心数字, 叙事驱动\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"合并入 R3-C2 处理: Abstract 同等权重报告 PPL 改善和 downstream 退化\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S9\"\n    summary: \"Taxonomy 5/9 cells 空, post-hoc 质疑\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 部分 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W2: post-hoc 无 predictive power. R1 交叉部分 REBUT (有 organizational utility) 但同意: 不应作独立 contribution; 空 cell 未讨论原因. 共识: taxonomy 降为 Related Work 组织框架, 从 contribution list 移除.\"}\n    action_items:\n      - {round: 3, action: \"补 DejaVu/D2DMoE + 讨论轴选择依据\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"Taxonomy 从 contribution list 移除, 降为 Related Work 组织框架; 讨论空 cell 原因\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M\"\n    summary: \"11 条 minor (AdamW wd, BCE threshold, ShadowLLM, bib years, GPU, -ing phrases, Figure label, Conclusion 过短等)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"混合来源\"}\n      - {round: 4, reviewers: [1, 2], note: \"部分复发: bib xu2026spon key/year 不一致(R1+R2 均提); SPON eval protocol 不同(R1+R2 P1); d030 exp_id naming 问题(见 R4-W1). AI 写作痕迹已清理(R2-S5 确认无 em-dash 等).\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 批量修复\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"修复 bib key; 统一 SPON eval protocol 或更显著标注差异\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"6.4% 延迟与效率叙事矛盾\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7 Round 1\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-C3 再次 raise\"}\n      - {round: 4, reviewers: [1, 2], note: \"合并入 R3-C3 处理. 6.4% overhead 事实不变.\"}\n    action_items:\n      - {round: 1, action: \"Reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 3, action: \"understanding paper not efficiency paper\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"三 seed 统计效力弱 → 升级: 主表全部单 seed\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出, R2 REBUT\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-S3, 升为 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W4, R2 AGREE. Table 2 所有关键对比单 seed. '49% PPL reduction' 无 error bars. 30% MMLU=25.27% 若有 ±2pp variance 可能与 random 无显著差异. 3-seed 仅限 50% uniform 一个配置.\"}\n    action_items:\n      - {round: 3, action: \"标注已有 4-seed mean±0.07\", assigned_to: \"paper_agent\", status: in_progress}\n      - {round: 4, action: \"Table 2 关键行 (KL global 30%/50%, TEAL 30%/50%) 做 3-seed 评估; 报告 downstream metrics 的 seed variance\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 4 new issues ===\n\n  - id: \"R4-C1\"\n    summary: \"PPL 22.51 幽灵数字: 贯穿 Abstract/Intro/§4.3 的 '91% worse PPL' claim 无表格数据支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [1, 2], note: \"R1-N1 raise, R2 交叉强 AGREE. 22.51 不出现在任何表格. Table 2 BCE=27.97(137% worse). experiments.tex:65-66 同段出现 22.51 和 27.97 指向同一 exp_id. 数据溯源链断裂.\"}]\n    action_items:\n      - {round: 4, action: \"确认 22.51 来源(1000-step BCE?), 在 Table 2 或 Table 3 补充对应数据行; 或用 Table 中已有数字(27.97)重算百分比并全文替换 '91%'\", assigned_to: \"paper_agent+main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W1\"\n    summary: \"d030 exp_id 暗示 regime analysis 使用了错误 sparsity target 的 predictor\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [2], note: \"交叉分享中发现. d030_kl40_uniform/d030_kl50_uniform 命名暗示用 30%-trained predictor. 若属实, Table 5 caption 'each row uses a predictor trained at the respective sparsity target' 是虚假陈述, 整个 regime analysis 的 global vs uniform preference reversal 可能是 artifact.\"}]\n    action_items:\n      - {round: 4, action: \"确认 d030 前缀含义: 是 predictor training target 还是 batch 编号; 若确为 30%-trained predictor, 重跑 40%/50%-trained uniform 或修正 Table 5 caption\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"Structural mismatch 洞察新颖性: end-to-end > decomposed 是深度学习基本原则\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [1, 2], note: \"R2-W1, R1 交叉 AGREE. §3.5 梯度分析本质是 chain rule 标准应用. Factor (b) Jacobian 耦合是任何 end-to-end loss 固有性质. 但 'F1 高反而 PPL 差' 的 empirical finding 有价值. 建议降低 formal analysis 权重, 强调 empirical 验证.\"}]\n    action_items:\n      - {round: 4, action: \"降低 'structural mismatch' 在叙事中的理论权重; 强调 empirical finding (F1-PPL disconnect) 而非 gradient formalism\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"Training/evaluation domain overlap: WikiText-103 训练 + WikiText-2 评测, OOD 仅 50%\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [1, 2], note: \"R2-W6, R1 部分 REBUT (relative advantage 保持). 但 OOD 仅 50% 一个 sparsity, 缺 30%/40% OOD. C4 PPL 18.40 vs WikiText-2 11.79 (56% higher), dense gap 类似(50.5%). Relative advantage 保持(49%→52.5%).\"}]\n    action_items:\n      - {round: 4, action: \"补充 30%/40% sparsity 的 C4 OOD 评估; 将 OOD 结果放入主表或正文并行报告\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-17T09:32:54.188584+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 21798}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 154
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-17T09:35:45.552608+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "report": "# 圆桌审稿报告 — Round 4\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性)\n**轮次**: Round 1 独立审稿 + 交叉分享, 1 轮收敛\n\n---\n\n## Summary\n\n本文研究用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor。核心论点是 BCE 的 per-neuron 梯度与 TEAL 推理时 global top-k 分配存在结构性不匹配，而 KL 目标通过计算图耦合所有神经元。一个轻量 predictor (75.9M params, &lt;1% of base) 通过 Gumbel-Sigmoid relaxation 实现端到端蒸馏，在 LLaMA-3.1-8B 50% sparsity 下 PPL 11.79 vs TEAL 23.31 (49% 改善)。论文同时提出 2D taxonomy 分类先前方法和三 sparsity regime 分析。然而，headline method (KL+global allocation) 在最重要的 downstream task 上退化至随机水平 (MMLU 25.27% ≈ 4-choice random)，实际推理增加 6.4% overhead 而非加速，且核心定量 claim (\"91% worse PPL\") 依赖的数据无法从论文中验证。\n\n---\n\n## Strengths\n\n**S1. 问题定义清晰且有意义** [R1+R2 共识]\nPer-neuron BCE 与 global top-k 之间的 structural mismatch 是一个真实问题。梯度分析框架（Eq. 7-10, 4-factor 分解）虽本质是 chain rule 展开，但将其 formalize 并与 oracle F1/SNR 联系的分析思路清晰。\"F1 高反而 PPL 差\" 的 empirical finding 有独立价值。\n\n**S2. 系统的 ablation 设计** [R1+R2 共识]\nTable 3 覆盖 divergence direction (forward/reverse/JSD)、relaxation (Gumbel/STE)、BCE variants (±compensation, +Gumbel)，多维度隔离了设计选择。每个 ablation 有独立 exp_id，可溯源。\n\n**S3. 诚实报告负面结果** [R1+R2 共识]\n论文未隐瞒 MMLU 退化、无 wall-clock 加速等问题，而是将其作为分析对象（regime analysis, late-layer starvation）。这种诚实态度值得肯定。\n\n**S4. 跨架构一致性** [R2]\nTable 7 在 Mistral-7B-v0.3 上验证 KL/TEAL advantage ratio 一致性（≤50% 内 7% 偏差）。\n\n**S5. 写作质量** [R2]\n全文无 AI 写作典型标志（无 em-dash、无 -ing 结尾短语），段落过渡自然，数学符号一致。\n\n**S6. Reproducibility** [R1+R2 共识]\n超参全量报告、training convergence curve、bottleneck sensitivity sweep、训练成本低 (17min on A6000)。\n\n---\n\n## Weaknesses\n\n### Critical Issues (影响接收决定)\n\n**C1. [critical] PPL 22.51 幽灵数字——核心 claim 数据溯源链断裂** [R1 raise, R2 强 AGREE]\n\n§4.3 写到 \"BCE achieves +13pp oracle F1 (0.613 vs. 0.540) with 91% worse PPL (22.51 vs. 11.79)\"。\"91% worse perplexity\" 贯穿 Abstract、Introduction、Experiments 三处，是论文最核心的定量 claim 之一。然而 22.51 **不出现在论文任何表格中**：Table 2 BCE (2700 steps) = 27.97, BCE+Compensation = 25.44。若用 Table 2 的 27.97，则是 137% worse，而非 91%。\n\n更严重的是，experiments.tex:65-66 中 22.51 和 27.97 在同段相邻两句出现，指向相同 exp_id (bce_isocompute_s42)，自相矛盾。这不是 typo——是数据溯源链的根本断裂。审稿人无法从提交材料中验证论文最核心的 quantitative claim。\n\n**C2. [critical] Headline method 在 downstream tasks 上退化至随机水平，与论文叙事根本矛盾** [R1-N2 + R2-N3, 交叉全 AGREE]\n\n论文主推方法 \"KL global (Ours)\" 的 downstream 表现：\n- 30% sparsity: MMLU 25.27% (4-choice random = 25%, 差 0.27pp; TEAL vanilla = 38.61%, 高 13.3pp)\n- 50% sparsity: MMLU 27.89%, GSM8K 1.29% (完全失效)\n- 即使 \"best case\" 30% KL uniform = 40.61%, 仍比 dense 65.27% 低 24.7pp\n\n论文的 primary inference protocol \"KL + TEAL global\"（experiments.tex:18-19 定义为 \"predictor-TEAL\"）在所有设定下 MMLU 不可用。论文全篇以 \"optimizes for global allocation quality\" 为核心叙事（Abstract, §1, §3.5），但实验结论表明 global allocation 在实践中损害 downstream performance。这是 narrative vs evidence 的根本矛盾。\n\n论文 §4.5 的 \"allocation strategy rather than KL training quality\" 归因虽技术上可能正确，但在叙事上自我矛盾——如果方法必须搭配不同的 allocation strategy 才能工作，而论文全篇以 global allocation 为主线，这就是 framing 失败。\n\n**C3. [critical] 核心新颖性不足：与 MaskLLM 框架高度重叠** [R2-N1, R1 交叉 AGREE]\n\nMaskLLM (Fang et al., NeurIPS 2024) 的高层框架与本文几乎完全一致：frozen base model weights + learnable masks + Gumbel relaxation + KL divergence training。本文的 delta 是将这一已验证有效的训练范式从 weight N:M sparsity 迁移到 activation per-token sparsity。\n\n论文 §2 的辩护——\"structural mismatch does not arise in MaskLLM's per-group categorical setting\"——恰好说明本文的核心 \"insight\" 是 task-specific 适配而非通用方法论贡献。方法部分（§3.1-§3.4）除 adaptive penalty controller（一个 augmented Lagrangian 的简化 heuristic，§3.4 脚注自承）外，每个组件都有直接对应：Gumbel-Sigmoid→MaskLLM/Concrete，KL distillation→MaskLLM/standard KD，per-layer MLP predictor→DejaVu/FastForward。\n\n如果重定位为 **empirical analysis paper**（\"验证 KL 范式在 activation sparsity + global allocation 下的表现，发现 structural mismatch 和 regime 现象\"），novelty 问题会缓解。但当前 framing 混合了 method contribution 和 analytical contribution，拉高了 novelty expectation。\n\n**C4. [critical] 无 wall-clock speedup，效率动机空洞** [R2-N2, R1 AGREE (介于 critical/warning)]\n\nTable 8 (Appendix A) 显示 KL predictor 在 50% sparsity 下 latency 126.78ms vs dense 119.11ms，即**增加 6.4% 延迟**。Unstructured element-wise masks 无法利用硬件稀疏加速。Title \"Contextual Sparsity Prediction\" 和 Introduction 从 inference efficiency 角度切入，建立了效率提升的预期。Abstract 的 \"49% reduction\" PPL 容易被误读为速度提升。\n\nLimitations 的坦诚报告和 Conclusion 的 \"prediction quality rather than systems optimization\" 部分缓解了此问题，但 Conclusion 最后一段又提到 \"wall-clock speedup\" 和 \"practical deployment value\" 作为 future directions，与 understanding framing 矛盾。\n\n### Should-Fix Issues (影响评分但不一票否决)\n\n**W1. [warning] BCE vs KL 对比存在 pipeline 混淆变量** [R1-N3 (critical), R2 REBUT→warning; 共识 warning]\n\nKL 和 BCE 使用完全不同的 pipeline：KL 用 Gumbel-Sigmoid soft masks + adaptive penalty + KL loss, BCE 用 hard masks + compensation (optional) + BCE loss。论文 claim \"the failure is structural\" (§4.3) 无法从现有实验 cleanly 验证。\n\nTable 3 的 isolation 实验提供了 reasonable（但非 definitive）evidence：Forward KL+Gumbel (11.79) vs KL+STE (15.77) 隔离了 relaxation (+3.98); KL+Gumbel (11.79) vs BCE+Gumbel+Penalty (38.02) 隔离了 loss (+26.23)。但 BCE+Gumbel+Penalty 之所以差，可能是 penalty 破坏了 BCE 的 per-neuron convergence，而非 KL 本身好。\n\n关键缺失：(1) MSE on hidden states ablation (intermediate coupling, 对应 Table 1 intermediate 列); (2) Per-layer KL ablation (解耦 cross-layer Jacobian coupling)。\n\n**W2. [warning] 三 regime 分析证据密度不足** [R1-W1 + R2-W3, 交叉全 AGREE]\n\nBudget-surplus/constrained/limited 三个 regime 基于 3 个 sparsity level (30%/40%/50%) × 2 allocation = 6 data points。每个 regime 仅 1 个观测。30%→40% preference reversal 的 boundary 未定位（缺 35% 数据）。Mistral 上无 downstream regime 数据。措辞应降为 \"preliminary observations\" 而非 \"three regimes\"。\n\n**W3. [warning] d030 exp_id 暗示 regime analysis 可能使用了错误 predictor** [R2 交叉中发现, R1 未覆盖]\n\nTable 5 中 d030_kl40_uniform 和 d030_kl50_uniform 的 \"d030\" 前缀强烈暗示使用了 30%-trained predictor，而 Table 5 caption 声称 \"Each row uses a predictor trained at the respective sparsity target\"。若属实：(1) 40%/50% uniform 行使用了 mismatched predictor → 与 global 行（properly trained）的对比不公平; (2) 整个 regime analysis 的 global vs uniform preference reversal 可能是 artifact。需要作者确认 d030 前缀含义。\n\n**W4. [warning] Train-inference mask mismatch 未量化** [R1-W3, R2 交叉 AGREE]\n\n训练 soft masks (τ=0.1) vs 推理 hard binary masks from global top-k，gap 未 clean 分离。§4.5 gap decomposition (\"53% predictor error + 47% allocation loss\") 混合了 discretization 和 allocation 两个效应。需要：soft per-token→hard per-token (隔离 discretization) + hard per-token→hard global (隔离 allocation) 的 controlled comparison。\n\n**W5. [warning] 主表结果单 seed** [R1-W4, R2 AGREE]\n\nTable 2 所有关键对比（KL global 11.79, TEAL 23.31 等）均为单 seed。3-seed 仅限 50% uniform (PPL 11.92±0.07)。30% MMLU=25.27% 若有 ±2pp variance 可能与 random baseline 无显著差异。\n\n**W6. [warning] 模型规模局限** [R1-W5, R2 AGREE]\n\n仅 7-8B 规模 (LLaMA-3.1-8B, Mistral-7B-v0.3)。Title \"SwiGLU LLMs\" 暗示广泛适用性。Regime boundaries 很可能 scale-dependent。\n\n**W7. [warning] Penalty controller \"convergence\" claim 不准确** [R1-W6, R2 AGREE]\n\n§3.4 claim \"converges within 40-110 steps across all targets\"，但 Appendix C Table 11 显示 30% target λ=5000 (cap, deviation=5.0%) 和 70% target λ=1000 (cap, deviation=1.7%)。Hit cap ≠ convergence，是 saturation。只有 40% 和 50% 真正收敛。\n\n**W8. [warning] Structural mismatch 洞察新颖性受限** [R2-W1, R1 AGREE]\n\nEnd-to-end 目标优于 decomposed 目标是深度学习基本原则。§3.5 的梯度分析本质是 chain rule 标准应用——factor (b) 的 Jacobian 耦合是任何 end-to-end loss 的固有性质。\"F1 高反而 PPL 差\" 的 empirical finding 有独立价值，但将其包装为 \"formal gradient analysis\" 级别理论贡献属过度。\n\n**W9. [warning] Taxonomy (Table 1) 贡献价值有限** [R2-W2, R1 部分 REBUT→共识: organizational utility but not independent contribution]\n\n2D taxonomy 是 post-hoc organization，无 predictive power。空 cell (Static×Decomposed, Static×Intermediate) 未讨论原因。共识：taxonomy 有组织价值但不应作为独立 contribution，适合降为 Related Work 组织框架。\n\n**W10. [warning] Missing references** [R2-W4, R1 AGREE]\n\n32 篇引用对 EMNLP long paper 偏少 (typical 40-60)。关键遗漏：\n- MiniLLM (Gu et al., ICLR 2024): forward vs reverse KL for LLM distillation，与 §4.4 ablation 直接相关且结论相反（MiniLLM 发现 reverse KL 更好）\n- SparseLoRA (ICML 2025): contextual sparsity for fine-tuning\n- Broader LLM distillation literature (GKD, DistiLLM 等)\n- D2DMoE taxonomy positioning 过度简化（其训练含 router + expert conversion，非单纯 MSE）\n\n**W11. [warning] Training/eval domain overlap** [R2-W6, R1 部分 REBUT]\n\nWikiText-103 训练 + WikiText-2 评测。C4 OOD 仅 50% sparsity。Relative advantage 保持 (49%→52.5%) 是正面信号，但缺 30%/40% OOD 数据。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成完全共识：\n\n1. **C1 (22.51 ghost number)**: 核心 claim 数据不可验证——不可接受 [R1 raise, R2 强 AGREE]\n2. **C2 (downstream collapse vs narrative)**: Headline method MMLU≈random, narrative 矛盾——需要根本性 reframing [R1-N2=R2-N3, 交叉全 AGREE]\n3. **C3 (MaskLLM novelty)**: 核心框架与 MaskLLM 高度重叠，novelty delta 有限 [R2 raise, R1 AGREE]\n4. **C4 (no speedup)**: 效率动机空洞，需明确 understanding 定位 [R2 raise, R1 AGREE]\n5. **W2 (regime data)**: 每 regime 仅 1 数据点，证据不足 [R1-W1=R2-W3]\n6. **W5 (single seed)**: 主表核心对比缺 error bars [R1-W4, R2 AGREE]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n唯一实质分歧：\n\n**W1 (pipeline confound) severity**: R1 评 critical（KL vs BCE 变量未 clean 隔离），R2 降为 warning（Table 3 ablation 提供 reasonable evidence）。\n\nR1 论据：loss 和 relaxation jointly varied，\"6.6× loss effect\" 计算混淆变量。\nR2 反驳：Table 3 中 KL+Gumbel vs KL+STE 和 KL+Gumbel vs BCE+Gumbel+Penalty 构成了 reasonable（虽非 perfect）controlled pairs。\n\n**Director 判断**：采纳 R2 的 warning 级别。Table 3 的 ablation 结构虽不完美但提供了方向性证据。缺 MSE 和 per-layer KL 是 should-fix 而非 must-fix。\n\n---\n\n## Questions to Authors\n\n1. §4.3 中 BCE PPL=22.51 对应哪个具体实验配置？与 Table 2 的 27.97 是什么关系？为什么不在任何表格中？\n2. MaskLLM 的训练范式（frozen weights + Gumbel + KL）直接迁移到 per-token activation sparsity 的效果如何？\n3. Table 5 中 d030_kl40_uniform/d030_kl50_uniform 的 \"d030\" 前缀含义是什么？是否使用了 30%-trained predictor？\n4. 如果 KL+global 在所有 downstream 设定下不可用，为什么不将 KL+uniform 定为推荐配置？\n5. Forward KL 优于 reverse KL (Table 3: 11.79 vs 12.80) 与 MiniLLM (ICLR 2024) 的结论相反——如何解释？\n6. 训练结束时 soft mask (τ=0.1) 与 hard mask 的 PPL gap 是多少？\n\n---\n\n## Missing References\n\n1. **MiniLLM** (Gu et al., ICLR 2024): Forward vs reverse KL for LLM distillation——与 §4.4 ablation 直接相关且结论相反\n2. **SparseLoRA** (ICML 2025): Contextual sparsity for fine-tuning\n3. **GKD / DistiLLM** 等 2023-2025 LLM-specific distillation 工作\n4. **Griffin** (De et al., 2024) / **Mixture-of-Depths** (Raposo et al., 2024): Dynamic compute allocation\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 paperreview.ai）。\n\n---\n\n## Overall Assessment\n\n**Score: 2.5 / 5 — Weak Reject (Borderline Findings)**\n**Confidence: 4 / 5**\n\n| 维度 | R1 | R2 | 合议 |\n|------|----|----|------|\n| Soundness | 2.5 | 3.0 | 2.5 |\n| Excitement | 2.5 | 2.0 | 2.0 |\n| Reproducibility | 3.5 | 4.0 | 3.5 |\n| Overall | 2.5 | 2.5 | 2.5 |\n\n**核心判断**：论文提出了一个有意义的问题（per-neuron BCE vs global allocation mismatch），梯度分析框架和 ablation 设计值得肯定。但四个 critical 问题共同削弱了论文的可接收性：\n\n1. **数据完整性** (C1): \"91% worse PPL\" 这一核心 claim 依赖的 22.51 数字无法从论文验证——这是提交标准的底线问题\n2. **叙事与证据矛盾** (C2): Headline method 在最重要 downstream task 上退化至 random，与 \"optimize for global allocation quality\" 叙事根本矛盾\n3. **有限新颖性** (C3): 核心框架是 MaskLLM 从 weight→activation sparsity 的迁移应用，方法论增量不足支撑独立 conference contribution\n4. **效率动机空洞** (C4): 以 sparsity prediction 为题暗示加速但实际增加 overhead\n\n**修复路径**：(a) 修复 22.51 数据溯源; (b) 重定位为 empirical analysis/mechanistic understanding paper 而非 method paper; (c) 以 KL+uniform 为推荐配置, global allocation 作分析对象; (d) Abstract/Intro 明确 \"prediction quality, not wall-clock speedup\"; (e) 补 MSE ablation + 更多 regime 数据点; (f) 确认 d030 exp_id 问题。修复后有 Findings 潜力。\n\n---\n\n## Detailed Comments (Per Section)\n\n### Abstract\n- \"91% worse perplexity\" 依赖不可验证的 22.51 (C1)\n- Headline \"49% PPL reduction\" 未给 downstream collapse 同等 prominence (C2)\n- 未明确声明无 wall-clock speedup (C4)\n\n### Introduction\n- Structural mismatch 分析清晰但新颖性受限 (W8)\n- Contribution #2 将 taxonomy 作为独立贡献过度 (W9)\n- 每条 contribution 有对应 section/table 支撑——结构合理\n\n### Related Work\n- MaskLLM 区分段落存在但深度不足 (C3)\n- D2DMoE 分类过于简化 (W10)\n- 缺 MiniLLM、SparseLoRA、GKD 等 (W10)\n- 引用数量偏少 (32 vs typical 40-60) (W10)\n\n### Method\n- §3.4 penalty controller \"converges\" claim 需修正为 \"saturates at cap\" (W7)\n- §3.5 梯度分析数学正确但属 chain rule 标准应用 (W8)\n- Taxonomy 适合降为 organizational framework (W9)\n\n### Experiments\n- 22.51 vs 27.97 同段矛盾 (C1)\n- Table 2 单 seed (W5)\n- Table 5 d030 命名需确认 (W3)\n- SPON analysis 使用不同 eval protocol (minor)\n- Gap decomposition 混合了 discretization 和 allocation (W4)\n- Regime analysis 每 regime 仅 1 数据点 (W2)\n\n### Conclusion\n- Wall-clock speedup 作 future direction 与 understanding framing 矛盾 (C4)\n- 长度适当，总结合理\n\n### Limitations\n- 诚实且全面\n- WikiText 训练/评测同源提及但 OOD 评测不充分 (W11)\n\n### Ethics / Checklist\n- 完整且合规。E1 (AI assistants) 诚实披露。\n\n### Appendix\n- Appendix A latency data 证实无 speedup (C4)\n- Appendix B-E 覆盖 sensitivity/convergence/OOD/stability——充分\n- 格式合规（双栏，在 references 之后）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "report": "# 圆桌审稿报告 — Round 4\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性)\n**轮次**: Round 1 独立审稿 + 交叉分享, 1 轮收敛\n\n---\n\n## Summary\n\n本文研究用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor。核心论点是 BCE 的 per-neuron 梯度与 TEAL 推理时 global top-k 分配存在结构性不匹配，而 KL 目标通过计算图耦合所有神经元。一个轻量 predictor (75.9M params, &lt;1% of base) 通过 Gumbel-Sigmoid relaxation 实现端到端蒸馏，在 LLaMA-3.1-8B 50% sparsity 下 PPL 11.79 vs TEAL 23.31 (49% 改善)。论文同时提出 2D taxonomy 分类先前方法和三 sparsity regime 分析。然而，headline method (KL+global allocation) 在最重要的 downstream task 上退化至随机水平 (MMLU 25.27% ≈ 4-choice random)，实际推理增加 6.4% overhead 而非加速，且核心定量 claim (\"91% worse PPL\") 依赖的数据无法从论文中验证。\n\n---\n\n## Strengths\n\n**S1. 问题定义清晰且有意义** [R1+R2 共识]\nPer-neuron BCE 与 global top-k 之间的 structural mismatch 是一个真实问题。梯度分析框架（Eq. 7-10, 4-factor 分解）虽本质是 chain rule 展开，但将其 formalize 并与 oracle F1/SNR 联系的分析思路清晰。\"F1 高反而 PPL 差\" 的 empirical finding 有独立价值。\n\n**S2. 系统的 ablation 设计** [R1+R2 共识]\nTable 3 覆盖 divergence direction (forward/reverse/JSD)、relaxation (Gumbel/STE)、BCE variants (±compensation, +Gumbel)，多维度隔离了设计选择。每个 ablation 有独立 exp_id，可溯源。\n\n**S3. 诚实报告负面结果** [R1+R2 共识]\n论文未隐瞒 MMLU 退化、无 wall-clock 加速等问题，而是将其作为分析对象（regime analysis, late-layer starvation）。这种诚实态度值得肯定。\n\n**S4. 跨架构一致性** [R2]\nTable 7 在 Mistral-7B-v0.3 上验证 KL/TEAL advantage ratio 一致性（≤50% 内 7% 偏差）。\n\n**S5. 写作质量** [R2]\n全文无 AI 写作典型标志（无 em-dash、无 -ing 结尾短语），段落过渡自然，数学符号一致。\n\n**S6. Reproducibility** [R1+R2 共识]\n超参全量报告、training convergence curve、bottleneck sensitivity sweep、训练成本低 (17min on A6000)。\n\n---\n\n## Weaknesses\n\n### Critical Issues (影响接收决定)\n\n**C1. [critical] PPL 22.51 幽灵数字——核心 claim 数据溯源链断裂** [R1 raise, R2 强 AGREE]\n\n§4.3 写到 \"BCE achieves +13pp oracle F1 (0.613 vs. 0.540) with 91% worse PPL (22.51 vs. 11.79)\"。\"91% worse perplexity\" 贯穿 Abstract、Introduction、Experiments 三处，是论文最核心的定量 claim 之一。然而 22.51 **不出现在论文任何表格中**：Table 2 BCE (2700 steps) = 27.97, BCE+Compensation = 25.44。若用 Table 2 的 27.97，则是 137% worse，而非 91%。\n\n更严重的是，experiments.tex:65-66 中 22.51 和 27.97 在同段相邻两句出现，指向相同 exp_id (bce_isocompute_s42)，自相矛盾。这不是 typo——是数据溯源链的根本断裂。审稿人无法从提交材料中验证论文最核心的 quantitative claim。\n\n**C2. [critical] Headline method 在 downstream tasks 上退化至随机水平，与论文叙事根本矛盾** [R1-N2 + R2-N3, 交叉全 AGREE]\n\n论文主推方法 \"KL global (Ours)\" 的 downstream 表现：\n- 30% sparsity: MMLU 25.27% (4-choice random = 25%, 差 0.27pp; TEAL vanilla = 38.61%, 高 13.3pp)\n- 50% sparsity: MMLU 27.89%, GSM8K 1.29% (完全失效)\n- 即使 \"best case\" 30% KL uniform = 40.61%, 仍比 dense 65.27% 低 24.7pp\n\n论文的 primary inference protocol \"KL + TEAL global\"（experiments.tex:18-19 定义为 \"predictor-TEAL\"）在所有设定下 MMLU 不可用。论文全篇以 \"optimizes for global allocation quality\" 为核心叙事（Abstract, §1, §3.5），但实验结论表明 global allocation 在实践中损害 downstream performance。这是 narrative vs evidence 的根本矛盾。\n\n论文 §4.5 的 \"allocation strategy rather than KL training quality\" 归因虽技术上可能正确，但在叙事上自我矛盾——如果方法必须搭配不同的 allocation strategy 才能工作，而论文全篇以 global allocation 为主线，这就是 framing 失败。\n\n**C3. [critical] 核心新颖性不足：与 MaskLLM 框架高度重叠** [R2-N1, R1 交叉 AGREE]\n\nMaskLLM (Fang et al., NeurIPS 2024) 的高层框架与本文几乎完全一致：frozen base model weights + learnable masks + Gumbel relaxation + KL divergence training。本文的 delta 是将这一已验证有效的训练范式从 weight N:M sparsity 迁移到 activation per-token sparsity。\n\n论文 §2 的辩护——\"structural mismatch does not arise in MaskLLM's per-group categorical setting\"——恰好说明本文的核心 \"insight\" 是 task-specific 适配而非通用方法论贡献。方法部分（§3.1-§3.4）除 adaptive penalty controller（一个 augmented Lagrangian 的简化 heuristic，§3.4 脚注自承）外，每个组件都有直接对应：Gumbel-Sigmoid→MaskLLM/Concrete，KL distillation→MaskLLM/standard KD，per-layer MLP predictor→DejaVu/FastForward。\n\n如果重定位为 **empirical analysis paper**（\"验证 KL 范式在 activation sparsity + global allocation 下的表现，发现 structural mismatch 和 regime 现象\"），novelty 问题会缓解。但当前 framing 混合了 method contribution 和 analytical contribution，拉高了 novelty expectation。\n\n**C4. [critical] 无 wall-clock speedup，效率动机空洞** [R2-N2, R1 AGREE (介于 critical/warning)]\n\nTable 8 (Appendix A) 显示 KL predictor 在 50% sparsity 下 latency 126.78ms vs dense 119.11ms，即**增加 6.4% 延迟**。Unstructured element-wise masks 无法利用硬件稀疏加速。Title \"Contextual Sparsity Prediction\" 和 Introduction 从 inference efficiency 角度切入，建立了效率提升的预期。Abstract 的 \"49% reduction\" PPL 容易被误读为速度提升。\n\nLimitations 的坦诚报告和 Conclusion 的 \"prediction quality rather than systems optimization\" 部分缓解了此问题，但 Conclusion 最后一段又提到 \"wall-clock speedup\" 和 \"practical deployment value\" 作为 future directions，与 understanding framing 矛盾。\n\n### Should-Fix Issues (影响评分但不一票否决)\n\n**W1. [warning] BCE vs KL 对比存在 pipeline 混淆变量** [R1-N3 (critical), R2 REBUT→warning; 共识 warning]\n\nKL 和 BCE 使用完全不同的 pipeline：KL 用 Gumbel-Sigmoid soft masks + adaptive penalty + KL loss, BCE 用 hard masks + compensation (optional) + BCE loss。论文 claim \"the failure is structural\" (§4.3) 无法从现有实验 cleanly 验证。\n\nTable 3 的 isolation 实验提供了 reasonable（但非 definitive）evidence：Forward KL+Gumbel (11.79) vs KL+STE (15.77) 隔离了 relaxation (+3.98); KL+Gumbel (11.79) vs BCE+Gumbel+Penalty (38.02) 隔离了 loss (+26.23)。但 BCE+Gumbel+Penalty 之所以差，可能是 penalty 破坏了 BCE 的 per-neuron convergence，而非 KL 本身好。\n\n关键缺失：(1) MSE on hidden states ablation (intermediate coupling, 对应 Table 1 intermediate 列); (2) Per-layer KL ablation (解耦 cross-layer Jacobian coupling)。\n\n**W2. [warning] 三 regime 分析证据密度不足** [R1-W1 + R2-W3, 交叉全 AGREE]\n\nBudget-surplus/constrained/limited 三个 regime 基于 3 个 sparsity level (30%/40%/50%) × 2 allocation = 6 data points。每个 regime 仅 1 个观测。30%→40% preference reversal 的 boundary 未定位（缺 35% 数据）。Mistral 上无 downstream regime 数据。措辞应降为 \"preliminary observations\" 而非 \"three regimes\"。\n\n**W3. [warning] d030 exp_id 暗示 regime analysis 可能使用了错误 predictor** [R2 交叉中发现, R1 未覆盖]\n\nTable 5 中 d030_kl40_uniform 和 d030_kl50_uniform 的 \"d030\" 前缀强烈暗示使用了 30%-trained predictor，而 Table 5 caption 声称 \"Each row uses a predictor trained at the respective sparsity target\"。若属实：(1) 40%/50% uniform 行使用了 mismatched predictor → 与 global 行（properly trained）的对比不公平; (2) 整个 regime analysis 的 global vs uniform preference reversal 可能是 artifact。需要作者确认 d030 前缀含义。\n\n**W4. [warning] Train-inference mask mismatch 未量化** [R1-W3, R2 交叉 AGREE]\n\n训练 soft masks (τ=0.1) vs 推理 hard binary masks from global top-k，gap 未 clean 分离。§4.5 gap decomposition (\"53% predictor error + 47% allocation loss\") 混合了 discretization 和 allocation 两个效应。需要：soft per-token→hard per-token (隔离 discretization) + hard per-token→hard global (隔离 allocation) 的 controlled comparison。\n\n**W5. [warning] 主表结果单 seed** [R1-W4, R2 AGREE]\n\nTable 2 所有关键对比（KL global 11.79, TEAL 23.31 等）均为单 seed。3-seed 仅限 50% uniform (PPL 11.92±0.07)。30% MMLU=25.27% 若有 ±2pp variance 可能与 random baseline 无显著差异。\n\n**W6. [warning] 模型规模局限** [R1-W5, R2 AGREE]\n\n仅 7-8B 规模 (LLaMA-3.1-8B, Mistral-7B-v0.3)。Title \"SwiGLU LLMs\" 暗示广泛适用性。Regime boundaries 很可能 scale-dependent。\n\n**W7. [warning] Penalty controller \"convergence\" claim 不准确** [R1-W6, R2 AGREE]\n\n§3.4 claim \"converges within 40-110 steps across all targets\"，但 Appendix C Table 11 显示 30% target λ=5000 (cap, deviation=5.0%) 和 70% target λ=1000 (cap, deviation=1.7%)。Hit cap ≠ convergence，是 saturation。只有 40% 和 50% 真正收敛。\n\n**W8. [warning] Structural mismatch 洞察新颖性受限** [R2-W1, R1 AGREE]\n\nEnd-to-end 目标优于 decomposed 目标是深度学习基本原则。§3.5 的梯度分析本质是 chain rule 标准应用——factor (b) 的 Jacobian 耦合是任何 end-to-end loss 的固有性质。\"F1 高反而 PPL 差\" 的 empirical finding 有独立价值，但将其包装为 \"formal gradient analysis\" 级别理论贡献属过度。\n\n**W9. [warning] Taxonomy (Table 1) 贡献价值有限** [R2-W2, R1 部分 REBUT→共识: organizational utility but not independent contribution]\n\n2D taxonomy 是 post-hoc organization，无 predictive power。空 cell (Static×Decomposed, Static×Intermediate) 未讨论原因。共识：taxonomy 有组织价值但不应作为独立 contribution，适合降为 Related Work 组织框架。\n\n**W10. [warning] Missing references** [R2-W4, R1 AGREE]\n\n32 篇引用对 EMNLP long paper 偏少 (typical 40-60)。关键遗漏：\n- MiniLLM (Gu et al., ICLR 2024): forward vs reverse KL for LLM distillation，与 §4.4 ablation 直接相关且结论相反（MiniLLM 发现 reverse KL 更好）\n- SparseLoRA (ICML 2025): contextual sparsity for fine-tuning\n- Broader LLM distillation literature (GKD, DistiLLM 等)\n- D2DMoE taxonomy positioning 过度简化（其训练含 router + expert conversion，非单纯 MSE）\n\n**W11. [warning] Training/eval domain overlap** [R2-W6, R1 部分 REBUT]\n\nWikiText-103 训练 + WikiText-2 评测。C4 OOD 仅 50% sparsity。Relative advantage 保持 (49%→52.5%) 是正面信号，但缺 30%/40% OOD 数据。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成完全共识：\n\n1. **C1 (22.51 ghost number)**: 核心 claim 数据不可验证——不可接受 [R1 raise, R2 强 AGREE]\n2. **C2 (downstream collapse vs narrative)**: Headline method MMLU≈random, narrative 矛盾——需要根本性 reframing [R1-N2=R2-N3, 交叉全 AGREE]\n3. **C3 (MaskLLM novelty)**: 核心框架与 MaskLLM 高度重叠，novelty delta 有限 [R2 raise, R1 AGREE]\n4. **C4 (no speedup)**: 效率动机空洞，需明确 understanding 定位 [R2 raise, R1 AGREE]\n5. **W2 (regime data)**: 每 regime 仅 1 数据点，证据不足 [R1-W1=R2-W3]\n6. **W5 (single seed)**: 主表核心对比缺 error bars [R1-W4, R2 AGREE]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n唯一实质分歧：\n\n**W1 (pipeline confound) severity**: R1 评 critical（KL vs BCE 变量未 clean 隔离），R2 降为 warning（Table 3 ablation 提供 reasonable evidence）。\n\nR1 论据：loss 和 relaxation jointly varied，\"6.6× loss effect\" 计算混淆变量。\nR2 反驳：Table 3 中 KL+Gumbel vs KL+STE 和 KL+Gumbel vs BCE+Gumbel+Penalty 构成了 reasonable（虽非 perfect）controlled pairs。\n\n**Director 判断**：采纳 R2 的 warning 级别。Table 3 的 ablation 结构虽不完美但提供了方向性证据。缺 MSE 和 per-layer KL 是 should-fix 而非 must-fix。\n\n---\n\n## Questions to Authors\n\n1. §4.3 中 BCE PPL=22.51 对应哪个具体实验配置？与 Table 2 的 27.97 是什么关系？为什么不在任何表格中？\n2. MaskLLM 的训练范式（frozen weights + Gumbel + KL）直接迁移到 per-token activation sparsity 的效果如何？\n3. Table 5 中 d030_kl40_uniform/d030_kl50_uniform 的 \"d030\" 前缀含义是什么？是否使用了 30%-trained predictor？\n4. 如果 KL+global 在所有 downstream 设定下不可用，为什么不将 KL+uniform 定为推荐配置？\n5. Forward KL 优于 reverse KL (Table 3: 11.79 vs 12.80) 与 MiniLLM (ICLR 2024) 的结论相反——如何解释？\n6. 训练结束时 soft mask (τ=0.1) 与 hard mask 的 PPL gap 是多少？\n\n---\n\n## Missing References\n\n1. **MiniLLM** (Gu et al., ICLR 2024): Forward vs reverse KL for LLM distillation——与 §4.4 ablation 直接相关且结论相反\n2. **SparseLoRA** (ICML 2025): Contextual sparsity for fine-tuning\n3. **GKD / DistiLLM** 等 2023-2025 LLM-specific distillation 工作\n4. **Griffin** (De et al., 2024) / **Mixture-of-Depths** (Raposo et al., 2024): Dynamic compute allocation\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 paperreview.ai）。\n\n---\n\n## Overall Assessment\n\n**Score: 2.5 / 5 — Weak Reject (Borderline Findings)**\n**Confidence: 4 / 5**\n\n| 维度 | R1 | R2 | 合议 |\n|------|----|----|------|\n| Soundness | 2.5 | 3.0 | 2.5 |\n| Excitement | 2.5 | 2.0 | 2.0 |\n| Reproducibility | 3.5 | 4.0 | 3.5 |\n| Overall | 2.5 | 2.5 | 2.5 |\n\n**核心判断**：论文提出了一个有意义的问题（per-neuron BCE vs global allocation mismatch），梯度分析框架和 ablation 设计值得肯定。但四个 critical 问题共同削弱了论文的可接收性：\n\n1. **数据完整性** (C1): \"91% worse PPL\" 这一核心 claim 依赖的 22.51 数字无法从论文验证——这是提交标准的底线问题\n2. **叙事与证据矛盾** (C2): Headline method 在最重要 downstream task 上退化至 random，与 \"optimize for global allocation quality\" 叙事根本矛盾\n3. **有限新颖性** (C3): 核心框架是 MaskLLM 从 weight→activation sparsity 的迁移应用，方法论增量不足支撑独立 conference contribution\n4. **效率动机空洞** (C4): 以 sparsity prediction 为题暗示加速但实际增加 overhead\n\n**修复路径**：(a) 修复 22.51 数据溯源; (b) 重定位为 empirical analysis/mechanistic understanding paper 而非 method paper; (c) 以 KL+uniform 为推荐配置, global allocation 作分析对象; (d) Abstract/Intro 明确 \"prediction quality, not wall-clock speedup\"; (e) 补 MSE ablation + 更多 regime 数据点; (f) 确认 d030 exp_id 问题。修复后有 Findings 潜力。\n\n---\n\n## Detailed Comments (Per Section)\n\n### Abstract\n- \"91% worse perplexity\" 依赖不可验证的 22.51 (C1)\n- Headline \"49% PPL reduction\" 未给 downstream collapse 同等 prominence (C2)\n- 未明确声明无 wall-clock speedup (C4)\n\n### Introduction\n- Structural mismatch 分析清晰但新颖性受限 (W8)\n- Contribution #2 将 taxonomy 作为独立贡献过度 (W9)\n- 每条 contribution 有对应 section/table 支撑——结构合理\n\n### Related Work\n- MaskLLM 区分段落存在但深度不足 (C3)\n- D2DMoE 分类过于简化 (W10)\n- 缺 MiniLLM、SparseLoRA、GKD 等 (W10)\n- 引用数量偏少 (32 vs typical 40-60) (W10)\n\n### Method\n- §3.4 penalty controller \"converges\" claim 需修正为 \"saturates at cap\" (W7)\n- §3.5 梯度分析数学正确但属 chain rule 标准应用 (W8)\n- Taxonomy 适合降为 organizational framework (W9)\n\n### Experiments\n- 22.51 vs 27.97 同段矛盾 (C1)\n- Table 2 单 seed (W5)\n- Table 5 d030 命名需确认 (W3)\n- SPON analysis 使用不同 eval protocol (minor)\n- Gap decomposition 混合了 discretization 和 allocation (W4)\n- Regime analysis 每 regime 仅 1 数据点 (W2)\n\n### Conclusion\n- Wall-clock speedup 作 future direction 与 understanding framing 矛盾 (C4)\n- 长度适当，总结合理\n\n### Limitations\n- 诚实且全面\n- WikiText 训练/评测同源提及但 OOD 评测不充分 (W11)\n\n### Ethics / Checklist\n- 完整且合规。E1 (AI assistants) 诚实披露。\n\n### Appendix\n- Appendix A latency data 证实无 speedup (C4)\n- Appendix B-E 覆盖 sensitivity/convergence/OOD/stability——充分\n- 格式合规（双栏，在 references 之后）"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-17T09:35:49.931952+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4379
}
```

</details>

---


### Assistant

_source line 362 · 2026-05-17T09:36:01.727505+00:00_

审稿报告已投递至 Research Director。

**Round 4 圆桌审稿完成**。

最终评分：**2.5/5 (Weak Reject / Borderline Findings)**，置信度 4/5。

**4 个 Critical 问题**：
1. **C1** — PPL 22.51 幽灵数字：贯穿全文的 "91% worse" claim 数据无法验证
2. **C2** — Downstream collapse 与叙事矛盾：KL+global 在 MMLU 上 ≈ random (25.27%)，比 TEAL (38.61%) 差 13pp
3. **C3** — 与 MaskLLM 新颖性区分不足：核心框架是已有范式的 sparsity type 迁移
4. **C4** — 无 wall-clock speedup：6.4% overhead，效率动机空洞

**11 个 Warning 问题**（pipeline confound、regime 数据不足、d030 exp_id 疑问、train-inference mismatch、单 seed、模型规模、penalty convergence claim、structural mismatch 新颖性、taxonomy 贡献、missing references、domain overlap）。

**修复路径**：修数据溯源 → 重定位为 empirical analysis paper → KL+uniform 为推荐配置 → 补 MSE ablation 和 regime 数据点 → 引用扩充至 40+。修复后有 Findings 潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 363 · 2026-05-17T09:36:04.246145+00:00_

[Reviewer 2 审稿结果]:
交叉审稿回应已提交。

总结：R1 的 5 个 Must-Fix 和 Should-Fix 中，我同意 N1（22.51 幽灵数字）、N2（MMLU 随机水平）、W1-W6 全部，仅对 N3（pipeline 混淆变量）部分反驳——认为论文的 ablation 虽不完美但 severity 应从 critical 降至 warning。R1 发现的 `d030` exp_id 问题和 penalty convergence 问题是我 Round 1 中遗漏的，如果 `d030` 确认是训练 sparsity 标记，则 regime analysis 可能整体不可信。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 364 · 2026-05-17T09:36:17.857342+00:00_

审稿报告已投递至 Research Director。

**本轮审稿完成总结**：

- **评分**：2.5/5 (Weak Reject / Borderline Findings)
- **Reviewers**：2 人，1 轮收敛（交叉分享后关键问题全部达成共识）
- **4 个 Critical 问题**：
  1. PPL 22.51 幽灵数字——"91% worse" 核心 claim 无法验证
  2. Headline method MMLU≈random，与 "global allocation quality" 叙事根本矛盾
  3. 与 MaskLLM 框架高度重叠，novelty delta 不足
  4. 无 wall-clock speedup，效率动机空洞
- **11 个 Warning 问题**：pipeline 混淆、regime 数据不足、d030 exp_id 可疑、train-inference mismatch、单 seed、模型规模局限等
- **修复路径**：重定位为 empirical analysis paper，修复数据溯源，以 KL+uniform 为推荐配置，补 MSE ablation 和引用

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 36

## Round 36

60 recorded events


### User

_source line 365 · 2026-05-17T10:29:22.187990+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026 cycle
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-17T10:29:30.842364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-17T10:29:31.045650+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-17T10:29:35.765338+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,request_external_review,get_external_review_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,request_external_review,get_external_review_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-17T10:29:35.765674+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-17T10:29:40.139899+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__request_study_approval",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__request_study_approval",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-17T10:29:40.140373+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-17T10:29:46.064873+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-17T10:29:47.507247+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (104 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 今日完成的分析任务（全部 success 或 negative，已写入 paper）\n\n| exp_id | 结论 | 关键发现 |\n|--------|------|---------|\n| kl_bce_f1_oracle | success | BCE F1=0.613 > KL F1=0.540，但 KL PPL=11.79 远优于 BCE PPL=22.51。证明 per-neuron mask accuracy 是错误优化目标 |\n| global_30pct_retention | negative | 30% 全局 top-k 饿死 late layers (L27-31)，L31 仅 28.4% retention。原 hypothesis \"中层知识层挨饿\" 被推翻 |\n| global_50pct_retention | success | 50% 下 late layers retention 降至 0.342，knowledge layers (L12-20) 保持 0.606，确认全局分配优先喂中层 |\n| global_70pct_retention | success | 70% 下 starvation 扩散到 L10-L12（min=0.167），相变：全局分配无法同时保护中层和早期层 |\n| reverse_kl_50pct_s42 | negative | PPL=12.8 vs Forward KL=11.79（+8.6%），Forward KL 仍最优 |\n| jsd_50pct_s42 | negative | PPL=12.54 vs Forward KL=11.79（+6.4%），Forward KL 仍最优 |\n| gradient_snr_constrained | success | 带 Lagrangian 约束下 KL SNR 仍 103.2× > BCE，直接回应 R1-W5 |\n| lagrangian_dynamics_fix | success | 重新生成完整 1000-step Lagrangian 动态图（50% 数据修复） |\n| teal_kl_overlap_corrected | success | 排列检验 z=7260，确认 TEAL-KL 重叠非随机（回应选择偏差） |\n| natural_sparsity_floor_extended | success | 30/50/70% 三级自然稀疏下限分析完成 |\n\n## 产出物（已同步/待同步到本地）\n- `figures/paper/lagrangian_dynamics.pdf` — 已同步\n- `figures/paper/per_layer_retention_
…[truncated 339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1442
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-17T10:29:48.009578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-17T10:29:48.561993+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-17T10:29:49.014128+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-17T10:29:49.014481+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-17T10:29:49.516537+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-17T10:29:49.968734+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-17T10:29:50.270431+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-17T10:29:50.321168+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_5.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-17T10:30:19.525679+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-17T10:30:19.927944+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-17T10:30:21.440597+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-17T10:30:21.893135+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-17T10:30:21.894233+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "paper_framing.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-17T10:30:25.060697+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, here is the information about EMNLP 2026 call for papers:

## Submission Deadline

The EMNLP 2026 paper submission deadline is 2026-05-25 23:59:59 (UTC-12).

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Additionally, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Submission Process

All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026. The mandatory Limitations sectio
…[truncated 219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5132
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-17T10:30:26.767833+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission guidelines author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the search results, here is information about ACL Rolling Review (ARR) submission guidelines and author instructions:

## Key Author Submission Guidelines

All submitting authors must sign up as reviewers with a deadline of 48 hours after the submission deadline. ACL has adopted a policy requiring all authors to sign up as reviewers, with assignments
…[truncated 1228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7242
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-17T10:30:26.818680+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \\\"unfair comparison\\\" attacks. **Iso-compute evidence (eval_bce_v3_s42)**: with 2.71× more gradient updates, BCE TEAL PPL=27.97 vs KL=12.00 (2.33× gap persists), and BCE loss saturates (step 500→2700: Δ=-0.006). The advantage is structural: BCE optimizes per-neuron binary classification, but inference uses global top-k budget allocation — per-neuron scoring is suboptimal under global reallocation. KL directly optimizes output distribution, naturally compatible with any allocation strategy. (Headline claim)\\n\\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \\\"subsuming\\\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that K
…[truncated 4374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4924
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-17T10:30:39.524062+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-17T10:30:40.027430+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	Gradient coupling analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions, achieving higher oracle F1 (0.613 vs.\ 0.540) yet 137\% worse perplexity.
4	A lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution.
5	On LLaMA-3.1-8B at 50\% sparsity with uniform per-layer allocation, the KL predictor achieves PPL 11.96 with MMLU 27.77\%, improving over magnitude-based TEAL (PPL 23.31); under global allocation, PPL drops further to 11.79 but late-layer starvation (L31 retention 28.4\%) degrades downstream tasks.
6	We identify three operating regions at the 7--8B scale (budget-surplus, budget-constrained, capacity-limited) that govern allocation-quality tradeoffs, with consistent KL-over-TEAL improvements on Mistral-7B-v0.3 (within 8\% ratio at $\leq$50\% sparsity).
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-17T10:30:40.078950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-17T10:30:40.430944+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	We provide this analysis.
9	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of $j$ alone, independent of every other neuron.
10	Under KL divergence, the gradient for neuron $j$ in layer $\ell$ factors as:
11	\begin{equation*}
12	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
13	\end{equation*}
14	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, coupling each neuron's gradient to every other neuron's mask state.
15	This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 137\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preser
…[truncated 1998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-17T10:30:40.431717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-17T10:30:40.934692+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 14269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-17T10:30:40.935231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-17T10:30:41.388101+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25
…[truncated 14326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-17T10:30:41.438790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-17T10:30:42.443196+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision, providing intermediate coupling within each layer but no end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
14	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
15	The structural mismatch we identify (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns
…[truncated 2689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-17T10:30:42.694453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-17T10:30:42.895780+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that KL distillation resolves the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation in SwiGLU sparsity prediction.
5	The coupled gradient signal enables a lightweight predictor (75.9M params, $<$1\% of base) to achieve PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, with consistent improvements on both LLaMA-3.1-8B and Mistral-7B-v0.3 (within 8\% ratio consistency at $\leq$50\% sparsity).
6	Analysis of allocation strategies reveals that global top-$k$ starves late layers, degrading downstream tasks, while uniform allocation recovers performance comparable to TEAL, confirming that allocation strategy rather than predictor quality is the primary bottleneck.
7	
8	Open directions include scaling to 13B--70B models to test generality beyond 7--8B, adaptive per-layer allocation that bridges the global-PPL and uniform-downstream gap, and downstream-aware training objectives that directly optimize task accuracy rather than output-distribution fidelity.
9	
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-17T10:30:42.946582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-17T10:30:42.997214+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	Out-of-distribution evaluation (Appendix~\ref{app:ood}) covers only 50\% sparsity on C4; extending to 30\% and 70\% is left to future work.
7	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
8	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-17T10:30:46.612397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-17T10:30:46.613389+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText a
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-17T10:30:46.826800+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-17T10:30:46.827801+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overh
…[truncated 8907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-17T10:30:46.952761+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-17T10:30:47.066207+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 113
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-17T10:30:54.024072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit anonymity requirements template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit anonymity requirements template"
  }
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-17T10:30:54.576347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-17T10:30:55.078828+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 14316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 413 · 2026-05-17T10:30:55.583318+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 414 · 2026-05-17T10:30:55.634337+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_1.md:170:外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/worker_util_copy_lagrangian_fig_20260517T070307.jsonl:138:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:6:{"ts": "2026-05-16T18:52:55.359976+00:00", "role": "tool", "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:director_get_project_overview,read_project_file,request_external_review,get_ext
…[truncated 11967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-17T10:31:01.082838+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit anonymity requirements template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission requirements:

## Page Limits

Long papers are limited to 8 pages, short papers to 4 pages, excluding ethical considerations and limitations. Appendices should come after the references in the submitted pdf but do not
…[truncated 1266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7058
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-17T10:31:20.969170+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-17T10:31:21.873126+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-17T10:31:22.024052+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && pdftotext main.pdf - 2>/dev/null | wc -l; pdfinfo main.pdf 2>/dev/null | grep Pages",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && pdftotext main.pdf - 2>/dev/null | wc -l; pdfinfo main.pdf 2>/dev/null | grep Pages",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-17T10:31:22.376902+00:00_

2990
Pages:           13
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-17T10:32:08.988228+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）\n- **模板**: ACL 两栏 11pt (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind，论文中不得出现作者信息，自引不得暴露身份\n- **附录规则**: 附录在 references 后，不计入页数，但审稿人可选择是否审阅\n\n### 论文文件\n- 主文件: `projects/distill_sparse_swiglu/paper/main.tex`\n- 各章节: abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\n- 参考文献: references.bib\n- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n### 你的审查侧重\n\n**核心职责**: 评估方法的技术严谨性和实验的可信度。\n\n请重点审查以下方面：\n\n1. **梯度分析的严谨性**（§3.6 / §3.5）\n   - BCE vs KL 梯度结构分析是否数学正确？\n   - \"structural mismatch\" 的论证是否充分？是否存在 overclaim？\n   - Gradient SNR 实验（80 steps, C4 data）的设置是否充分？统计显著性如何？\n\n2. **KL vs BCE 对比的公平性**\n   - BCE 使用 oracle masks (magnitude-based)，KL 使用 Gumbel-Sigmoid relaxation——训练目标和推理协议是否一致？\n   - \"137% worse PPL\" 的 claim：BCE 和 KL 是否在完全相同条件下对比（架构、步数、数据、推理协议）？\n   - Iso-compute analysis (§4.2): BCE 2700 steps vs KL 1000 steps 的对比是否足够公平？\n\n3. **实验设置的可信度**\n   - 仅使用 LLaMA-3.1-8B + Mistral-7B-v0.3（7-8B 规模）——泛化性声明是否过度？\n   - 训练数据 WikiText-103 (1000 steps) 是否太小？\n   - 单种子 vs 三种子：哪些结果是单种子的？variance 报告是否充分？\n   - Downstream benchmarks（ARC-c, WG, MMLU, GSM8K）在 50% 稀疏度下全部崩溃——这是否削弱了核心 claim？\n\n4. **消融实验的完整性**\n   - Table 3 消融是否覆盖所有关键设计选择？\n   - Gumbel vs STE 的对比是否孤立了正确的变量？\n   - SPON orthogonality analysis 的 cosine similarity 0.196 是否充分支持 \"near-orthogonal\" claim？\n\n5. **Adaptive Penalty Controller**\n   - 数学表述是否正确？与标准 augmented Lagrangian 的区别是否说清？\n   - 30% 和 70% 目标偏差 5%/1.7% 是否太大？对结果影响如何？\n\n6. **数据一致性**\n   - 表格间数据是否一致（同一实验在不同表格/文字中引用时数值是否一致）？\n   - PPL 数据的小数精度是否统一？\n\n### 输出格式\n\n请按以下结构输出你的审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix] ...\nW2. [Should-Fix] ...\nW3. [Minor] ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Overall Assessment\n评分: strong reject / weak reject / borderline / weak accept / strong accept\n置信度: low / medium / high\n```",
  "project": "distill_sparse_swiglu"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）\n- **模板**: ACL 两栏 11pt (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind，论文中不得出现作者信息，自引不得暴露身份\n- **附录规则**: 附录在 references 后，不计入页数，但审稿人可选择是否审阅\n\n### 论文文件\n- 主文件: `projects/distill_sparse_swiglu/paper/main.tex`\n- 各章节: abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\n- 参考文献: references.bib\n- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n### 你的审查侧重\n\n**核心职责**: 评估方法的技术严谨性和实验的可信度。\n\n请重点审查以下方面：\n\n1. **梯度分析的严谨性**（§3.6 / §3.5）\n   - BCE vs KL 梯度结构分析是否数学正确？\n   - \"structural mismatch\" 的论证是否充分？是否存在 overclaim？\n   - Gradient SNR 实验（80 steps, C4 data）的设置是否充分？统计显著性如何？\n\n2. **KL vs BCE 对比的公平性**\n   - BCE 使用 oracle masks (magnitude-based)，KL 使用 Gumbel-Sigmoid relaxation——训练目标和推理协议是否一致？\n   - \"137% worse PPL\" 的 claim：BCE 和 KL 是否在完全相同条件下对比（架构、步数、数据、推理协议）？\n   - Iso-compute analysis (§4.2): BCE 2700 steps vs KL 1000 steps 的对比是否足够公平？\n\n3. **实验设置的可信度**\n   - 仅使用 LLaMA-3.1-8B + Mistral-7B-v0.3（7-8B 规模）——泛化性声明是否过度？\n   - 训练数据 WikiText-103 (1000 steps) 是否太小？\n   - 单种子 vs 三种子：哪些结果是单种子的？variance 报告是否充分？\n   - Downstream benchmarks（ARC-c, WG, MMLU, GSM8K）在 50% 稀疏度下全部崩溃——这是否削弱了核心 claim？\n\n4. **消融实验的完整性**\n   - Table 3 消融是否覆盖所有关键设计选择？\n   - Gumbel vs STE 的对比是否孤立了正确的变量？\n   - SPON orthogonality analysis 的 cosine similarity 0.196 是否充分支持 \"near-orthogonal\" claim？\n\n5. **Adaptive Penalty Controller**\n   - 数学表述是否正确？与标准 augmented Lagrangian 的区别是否说清？\n   - 30% 和 70% 目标偏差 5%/1.7% 是否太大？对结果影响如何？\n\n6. **数据一致性**\n   - 表格间数据是否一致（同一实验在不同表格/文字中引用时数值是否一致）？\n   - PPL 数据的小数精度是否统一？\n\n### 输出格式\n\n请按以下结构输出你的审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix] ...\nW2. [Should-Fix] ...\nW3. [Minor] ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Overall Assessment\n评分: strong reject / weak reject / borderline / weak accept / strong accept\n置信度: low / medium / high\n```",
    "project": "distill_sparse_swiglu"
  }
}
````

</details>

---


### Tool result

_source line 421 · 2026-05-17T10:32:32.211407+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23223
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-17T10:32:32.413396+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 2（新颖性 + 相关工作 + 写作质量 + 完整性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）\n- **模板**: ACL 两栏 11pt (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind，论文中不得出现作者信息，自引不得暴露身份\n- **附录规则**: 附录在 references 后，不计入页数，但审稿人可选择是否审阅\n\n### 论文文件\n- 主文件: `projects/distill_sparse_swiglu/paper/main.tex`\n- 各章节: abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\n- 参考文献: references.bib\n- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n### 你的审查侧重\n\n**核心职责**: 评估论文的新颖性、相关工作覆盖度、写作质量和整体完整性。\n\n请重点审查以下方面：\n\n1. **新颖性评估**\n   - \"KL distillation for contextual sparsity prediction\" 的核心贡献是否足够新颖？\n   - MaskLLM 也使用 frozen weights + learnable masks + KL training——论文对差异的论述是否充分？\n   - Gumbel-Sigmoid + KL + Lagrangian penalty 的组合是否只是已有技术的直接拼接？\n   - 梯度分析（BCE vs KL gradient structure）是否提供了真正的新洞察？\n   - \"Three operating regions\" 发现的贡献有多大？\n\n2. **相关工作覆盖度**\n   - 引用是否覆盖所有直接相关方法（特别是近 1-2 年的新工作）？\n   - 是否遗漏重要 baseline 或竞争方法？\n   - 用 WebSearch 搜索 2024-2026 年的 activation sparsity / contextual sparsity prediction 最新工作，检查是否有遗漏\n   - Related Work 的 positioning 是否准确？是否有 mischaracterization？\n\n3. **Claims vs Evidence 对齐**\n   - Abstract/Introduction 的 claims 是否每条都有实验支撑？\n   - \"eliminates the need for error compensation\" 的 claim 是否过度？（BCE+compensation 的 PPL 25.44 vs KL 11.79——但如果用 KL+compensation 呢？）\n   - \"consistent improvements on Mistral\" 的 claim vs 实际数据是否匹配？\n   - Contribution 列表中的每条是否都有对应的 section/table 支撑？\n\n4. **写作质量**\n   - 是否有 AI 写作痕迹？检查：em-dash (—)、解释性 en-dash ( – )、-ing 短语结尾、过度分段、过渡词堆砌\n   - 术语一致性：同一概念是否使用一致的名称？\n   - 专有名词首次出现时是否有定义？\n   - 叙事连贯性：Abstract → Introduction → Method → Experiments → Conclusion 是否形成一条主线？\n   - 段落结构是否合理？是否有过度分段？\n\n5. **格式合规性**\n   - 正文是否在 8 页以内？\n   - 匿名化是否完整（无作者信息、无暴露身份的自引）？\n   - Limitations section 是否存在且内容充分？\n   - Ethics Statement 是否存在？\n   - Responsible NLP Checklist 是否完整？\n   - 图表 caption 是否自包含？图表引用是否正确？\n   - 参考文献格式是否一致（年份、venue、URL）？\n\n6. **图表质量**\n   - Figure 1 (method overview) 信息密度是否足够？\n   - Figure 2 (sparsity sweep) 是否清晰可读？\n   - 所有表格的格式是否统一（小数精度、加粗规则）？\n   - 图表是否占用了过多空间相对于其信息量？\n\n### 输出格式\n\n请按以下结构输出你的审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix] ...\nW2. [Should-Fix] ...\nW3. [Minor] ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有，列出遗漏的重要工作，附 citation 信息）\n\n## Overall Assessment\n评分: strong reject / weak reject / borderline / weak accept / strong accept\n置信度: low / medium / high\n```",
  "project": "distill_sparse_swiglu"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 2（新颖性 + 相关工作 + 写作质量 + 完整性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）\n- **模板**: ACL 两栏 11pt (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind，论文中不得出现作者信息，自引不得暴露身份\n- **附录规则**: 附录在 references 后，不计入页数，但审稿人可选择是否审阅\n\n### 论文文件\n- 主文件: `projects/distill_sparse_swiglu/paper/main.tex`\n- 各章节: abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\n- 参考文献: references.bib\n- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n### 你的审查侧重\n\n**核心职责**: 评估论文的新颖性、相关工作覆盖度、写作质量和整体完整性。\n\n请重点审查以下方面：\n\n1. **新颖性评估**\n   - \"KL distillation for contextual sparsity prediction\" 的核心贡献是否足够新颖？\n   - MaskLLM 也使用 frozen weights + learnable masks + KL training——论文对差异的论述是否充分？\n   - Gumbel-Sigmoid + KL + Lagrangian penalty 的组合是否只是已有技术的直接拼接？\n   - 梯度分析（BCE vs KL gradient structure）是否提供了真正的新洞察？\n   - \"Three operating regions\" 发现的贡献有多大？\n\n2. **相关工作覆盖度**\n   - 引用是否覆盖所有直接相关方法（特别是近 1-2 年的新工作）？\n   - 是否遗漏重要 baseline 或竞争方法？\n   - 用 WebSearch 搜索 2024-2026 年的 activation sparsity / contextual sparsity prediction 最新工作，检查是否有遗漏\n   - Related Work 的 positioning 是否准确？是否有 mischaracterization？\n\n3. **Claims vs Evidence 对齐**\n   - Abstract/Introduction 的 claims 是否每条都有实验支撑？\n   - \"eliminates the need for error compensation\" 的 claim 是否过度？（BCE+compensation 的 PPL 25.44 vs KL 11.79——但如果用 KL+compensation 呢？）\n   - \"consistent improvements on Mistral\" 的 claim vs 实际数据是否匹配？\n   - Contribution 列表中的每条是否都有对应的 section/table 支撑？\n\n4. **写作质量**\n   - 是否有 AI 写作痕迹？检查：em-dash (—)、解释性 en-dash ( – )、-ing 短语结尾、过度分段、过渡词堆砌\n   - 术语一致性：同一概念是否使用一致的名称？\n   - 专有名词首次出现时是否有定义？\n   - 叙事连贯性：Abstract → Introduction → Method → Experiments → Conclusion 是否形成一条主线？\n   - 段落结构是否合理？是否有过度分段？\n\n5. **格式合规性**\n   - 正文是否在 8 页以内？\n   - 匿名化是否完整（无作者信息、无暴露身份的自引）？\n   - Limitations section 是否存在且内容充分？\n   - Ethics Statement 是否存在？\n   - Responsible NLP Checklist 是否完整？\n   - 图表 caption 是否自包含？图表引用是否正确？\n   - 参考文献格式是否一致（年份、venue、URL）？\n\n6. **图表质量**\n   - Figure 1 (method overview) 信息密度是否足够？\n   - Figure 2 (sparsity sweep) 是否清晰可读？\n   - 所有表格的格式是否统一（小数精度、加粗规则）？\n   - 图表是否占用了过多空间相对于其信息量？\n\n### 输出格式\n\n请按以下结构输出你的审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix] ...\nW2. [Should-Fix] ...\nW3. [Minor] ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有，列出遗漏的重要工作，附 citation 信息）\n\n## Overall Assessment\n评分: strong reject / weak reject / borderline / weak accept / strong accept\n置信度: low / medium / high\n```",
    "project": "distill_sparse_swiglu"
  }
}
````

</details>

---


### Tool result

_source line 423 · 2026-05-17T10:32:33.777219+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1363
}
```

</details>

---


### Assistant

_source line 424 · 2026-05-17T10:32:42.610783+00:00_

两位 Reviewer 已派出，正在独立审稿中：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 实验有效性 | 审稿中 |
| R2 | 新颖性 + 相关工作 + 写作质量 | 审稿中 |

等待 Reviewer 返回审稿意见后，将进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 37

## Round 37

2 recorded events


### User

_source line 425 · 2026-05-17T10:37:05.923927+00:00_

[Reviewer 1 审稿意见]:
## Summary

本文分析了 SwiGLU LLM 中 per-neuron BCE 训练与 global top-k 推理之间的结构性不匹配，提出用 forward KL 蒸馏 + Gumbel-Sigmoid 松弛训练轻量级稀疏预测器。在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上验证了 KL 在 PPL 指标上优于 TEAL 和 BCE baseline，并分析了分配策略如何影响下游任务表现。

---

## Strengths

**S1. 梯度结构分析提供了有价值的理论洞察（§3.6）**
BCE 梯度 per-neuron 独立、KL 梯度通过 Jacobian 耦合所有 neuron 的分析在数学上是正确的，chain rule 分解清晰。这为选择 KL 目标提供了原则性动机，而非仅靠经验对比。

**S2. 实验设计系统且消融充分（§4.3, Table 3）**
消融覆盖了 divergence 方向（forward/reverse KL/JSD）、松弛方式（Gumbel vs STE）、loss function 隔离（BCE+Gumbel+Penalty），每个 design choice 的贡献量化清晰。Loss effect (6.6×) vs relaxation effect 的分解有信息量。

**S3. 三操作区域分析具有实用价值（§4.4, Table 4）**
Budget-surplus/constrained/capacity-limited 的区分为实际部署提供了指导，且在两个模型上验证了一致性。global vs uniform allocation 的 non-monotonic preference 是一个非 trivial 的发现。

**S4. 论文诚实报告了负面结果**
50% sparsity 下游崩溃、penalty controller 的偏差、PPL 与下游任务的脱节——这些局限性被坦诚讨论，增加了结果可信度。

**S5. 方法简洁，无 compensation network**
消除了 FastForward 式的补偿网络，predictor 参数 <1% base model，推理流程简化。

---

## Weaknesses

**W1. [Must-Fix] Iso-compute 对比存在严重不公平（§4.2）**

论文声称 BCE 2700 steps 与 KL 1000 steps 是 "iso-compute" 对比（2.71×），但完全忽略了 per-step 计算成本的巨大差异：
- KL 训练每步需要：dense forward pass（获取 target logits）+ sparse forward pass（经过 Gumbel masks 的完整前向）+ backward through the entire base model（虽然 frozen，但梯度需流经所有下游层以计算 mask 梯度 factor (b)）
- BCE 训练每步仅需：一次 forward pass 获取 oracle masks + predictor forward + backward through predictor only

KL 每步的实际 FLOP 远高于 BCE（至少 3-5×，因为需要 full backward through 8B model）。真正的 iso-compute 应该让 BCE 训练 8000-13000 steps。当前 2700 steps 的 "iso-compute" 表述是误导性的。

建议：(1) 明确报告两种训练的 wall-clock time 和 GPU memory（Limitations 提到 KL 45min vs BCE 17min，即 2.65× per-step cost，这意味着 iso-compute 应让 BCE 运行约 7000 steps）；(2) 或修改措辞为 "extended training" 而非 "iso-compute"。

**W2. [Must-Fix] BCE baseline 的 oracle 选择使对比不公平，coupling 论证存在混淆（§3.6, §4.2）**

核心论证存在一个未讨论的混淆因素：

- BCE 训练的 oracle masks 来自 activation magnitude (m_j* = 1[|g_j| >= global threshold])
- KL 直接优化 output distribution preservation

论文将 KL 的优势归因于 "gradient coupling"（factor (b)），但存在另一个完全不同的解释：magnitude-based oracle 本身就是 output preservation 的 poor proxy。即使 BCE 有完美的 "coupling"，如果 oracle 本身与 PPL 不对齐，也不会得到好的 PPL。

具体证据：BCE oracle F1 = 0.613（即完美匹配 magnitude oracle），但 PPL 仍然差。这说明问题可能不在于 "gradient coupling" 而在于 oracle 质量本身——用 magnitude 定义的 "重要" 与用 output distribution 定义的 "重要" 是不同的东西。

要真正证明 "coupling" 是关键因素，需要一个 ablation：用 KL-optimal masks 作为 BCE oracle（而非 magnitude-based masks），看 BCE 在该 oracle 下能否缩小与 KL 的差距。如果 BCE + better oracle 仍然差很多，才能证明 coupling 是核心因素。

**W3. [Must-Fix] 50% sparsity 下游完全崩溃，削弱核心实用性主张（Table 1, §4.1）**

50% sparsity（论文展示最大 PPL 优势的区间）：
- MMLU: 27.89% (global) / 27.77% (uniform) ≈ 随机（25%）
- GSM8K: <2.2% 所有方法

这意味着 KL predictor 在 50% sparsity 虽然 PPL 好很多（11.79 vs 23.31），但模型的实际能力已完全丧失。PPL 的改善没有转化为任何有意义的下游能力保持。

在唯一有意义下游表现的 30% sparsity：
- KL uniform PPL 8.82 vs TEAL 10.97（19% improvement，不是 dramatic）
- MMLU: 40.61% vs TEAL 38.61%（仅 +2pp）

这意味着论文的核心卖点（"49% PPL reduction"）发生在一个实际无用的区间。论文承认了这一点但仍以 50% 结果为主要展示。Introduction 和 Abstract 应更突出 30% 为推荐操作点以及该操作点下相对温和的改善幅度。

**W4. [Should-Fix] Gradient SNR 实验统计力度不足（§3.6）**

- 仅 80 steps，无 error bars，无统计显著性检验
- SNR 绝对值极低（5.77×10⁻⁵ vs 1.00×10⁻⁵），两者都接近零——质疑这些梯度信号是否实际有用
- "Early-layer BCE SNR collapses to ~10⁻⁸ after step 10"——这是一个重大声明但缺乏验证：为什么 collapse？是 vanishing gradient 还是 convergence？如果 BCE 已经在 10 步内拟合了 oracle masks，SNR 应该下降（因为 loss 已很小）
- 建议：报告 95% CI 或 bootstrap intervals，增加到至少 200-500 steps 覆盖不同训练阶段

**W5. [Should-Fix] 大部分结果为 single-seed，稳定性评估不充分（Table 1 note, Appendix E）**

- 仅 50% uniform 有 3-seed 评估（PPL 11.92±0.07）
- 30%、70%、cross-arch、iso-compute 等核心结果全部 single-seed
- Gumbel sampling 的随机性可能导致不同 seed 下显著差异，尤其在极端 sparsity（70%）下
- 这在 ARR 标准下属于 reproducibility 扣分项

**W6. [Should-Fix] "Near-orthogonal" 声称缺乏依据（§4.5）**

Cosine similarity = 0.196 被描述为 "near-orthogonal"。在数学上，orthogonal 意味着 cosine = 0。0.196 表示约 11° 偏离正交（arccos(0.196) ≈ 79°，正交为 90°）。这不是 "near-orthogonal"，这是 "低相关但非正交"。

高维空间中随机向量的 expected cosine similarity 约为 0（stddev ≈ 1/√d），所以 0.196 在高维中其实是 statistically significant 的非零相关。建议改为 "weakly correlated" 或提供随机 baseline 的 cosine distribution 作对比。

**W7. [Should-Fix] Adaptive penalty 30% target 偏差 5% 未讨论对实验结果的影响（Appendix B, Table 7）**

30% target 实际达到 28.5%（偏差 5%）。TEAL vanilla 在 30% 报告 PPL 10.97——那在 28.5% sparsity 下 TEAL 的 PPL 是多少？如果 TEAL 在 28.5% 也明显更好，则 KL 的优势被高估（因为它实际上在更低的 sparsity 下运行）。

建议：报告 TEAL 在实际达成的 sparsity level（28.5%）下的 PPL，或说明影响可忽略。

**W8. [Should-Fix] Training/evaluation 数据同源性（§4.1）**

WikiText-103 训练 → WikiText-2 评估。这两个数据集来自同一来源（Wikipedia），vocabulary 和 domain 高度重叠。OOD 评估（Appendix D）仅覆盖 50% sparsity 下的 C4，未覆盖 30%（推荐操作点）。建议在 30% sparsity 下也报告 C4 PPL。

**W9. [Minor] Table 1 中 BCE 行标注 "different inference protocol" 但解释不充分**

注释说 "BCE uses a different inference protocol (hard mask + compensation network)"，但正文 §4.2 的 iso-compute 比较中 BCE 使用的是 TEAL allocation（无 compensation），而 Table 1 row "BCE (2700 steps)" 标了 asterisk 说用了不同协议。这导致混淆：iso-compute 分析中 BCE 的 PPL 27.97 是 with compensation 还是 without？从 Table 3 看，"BCE (no compensation)" = 27.97, "BCE + Compensation" = 25.44——Table 1 的 27.97 应该是 no compensation 版本但标注说 "different protocol"，不一致。

**W10. [Minor] Scale 限制的 generalization claims 需要更谨慎措辞**

论文多处使用 "at the 7-8B scale" 作为 qualifier，这很好。但 conclusion 中 "open directions include scaling to 13B-70B" 暗示当前发现可能 generalize。考虑到 SwiGLU activation distribution 随 model size 变化（cf. Sparsing Law），当前结论严格限于 7-8B。

**W11. [Minor] Forward KL 方向选择的理由偏弱（§3.4）**

"The goal is to preserve the dense model's primary predictions rather than explore alternative modes" 是正确的直觉，但实验中 forward KL 仅优于 reverse KL 1.01 PPL（8.6%），优于 JSD 0.75 PPL（6.4%）——这些差异在缺乏 error bars 的情况下是否可靠？

---

## Questions

**Q1.** KL 每步的实际 GPU wall-clock time 和 peak memory 是多少？BCE 每步的对应数据是多少？Limitations 提到 KL 45min vs BCE 17min for 1000 steps——这意味着 KL 每步成本约 2.65× BCE，若给 BCE 同等 wall-clock (2650 steps)，PPL 能降到多少？

**Q2.** 如果用 KL-trained predictor 的 hard masks 作为 BCE 的 oracle target（而非 magnitude-based masks），BCE 能否缩小差距？这能分离 "coupling" 效应和 "oracle quality" 效应。

**Q3.** Table 3 中 "BCE + Gumbel + Penalty" (PPL 38.02) 比 vanilla BCE (27.97) 还差——这意味着 Gumbel+Penalty 框架不是通用的改进而是 KL-specific 的。请解释为什么 Gumbel 帮助了 KL 却伤害了 BCE？这是否暗示优势来自 loss function 与 relaxation 的 interaction 而非纯粹的 coupling？

**Q4.** 30% sparsity 下 penalty 达到 λ_max=5000 且偏差 5%——这是否意味着 SwiGLU 的 natural activation density 与 30% target 不兼容，训练实际上在对抗网络的内在分布？

**Q5.** Gradient SNR 中 "BCE early-layer SNR collapses to ~10⁻⁸ after step 10"——这是否因为 BCE 在 10 步内已对 oracle masks 过拟合（loss 接近 0 → gradient 接近 0）？如果是，这不是缺陷而是收敛。

---

## Missing References

- **ThunderKittens / FlashInfer** — sparse kernel implementations，与 wall-clock speedup 讨论相关
- **Deja Vu++ / Brain-inspired Sparse Training** — 更近期的 predictor-based sparsity 工作（如果存在）
- 当前引用覆盖度尚可（26篇），但缺少 hardware-aware pruning 方向的引用（如 nm-sparsity 的 Nvidia 工作）

---

## Overall Assessment

**Soundness: 3/5 (Acceptable)**
梯度分析数学正确但论证存在混淆（W2）；iso-compute claim 有误导性（W1）；核心实验单 seed（W5）。主要 claims 有支撑但关键对比的 fairness 存在问题。

**Excitement: 3/5 (Interesting)**
问题定义有价值（BCE vs KL for sparsity prediction 是实际存在的设计选择），三操作区域分析有实用意义。但 50% 下游崩溃和 30% 下温和改善限制了实际影响力。

**Reproducibility: 3.5/5**
超参完整报告，架构细节充分，但大部分结果单 seed 且缺少代码承诺。

**Overall: 2.5 (Borderline: between Resubmit and Findings)**

核心问题：(1) iso-compute claim 不公平需要修正或重新措辞；(2) coupling vs oracle-quality 的因果分离不足，核心叙事 "structural mismatch → KL solves it via coupling" 可能是 overclaim；(3) 实际可用区间（30%）的改善幅度温和（PPL 19%, MMLU +2pp）。

如果作者能够：修正 iso-compute 表述、增加 oracle-quality ablation、在 30% 补充 multi-seed + OOD 评估，论文有望达到 Findings 水平。当前版本的 overclaim 和实验 gaps 使其处于 borderline 状态。

**置信度: High (4/5)**
我仔细检查了梯度推导、数值计算和实验逻辑。对 sparsity prediction 和 KL distillation 文献有较好了解。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 426 · 2026-05-17T10:37:13.244727+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 427 · 2026-05-17T10:37:16.032899+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：论文在梯度结构分析和消融实验设计上有值得肯定之处，但存在三个核心问题：(1) iso-compute 对比忽略了 KL 每步 2.65× 的成本差异，表述有误导性；(2) coupling vs oracle-quality 的因果归因未被分离，"structural mismatch" 可能是 overclaim；(3) 方法的实际价值集中在 30% sparsity（PPL 19% improvement, MMLU +2pp），而论文主推的 50% 区间下游任务完全崩溃。评分 borderline (2.5/5)，建议修正后可达 Findings 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 428 · 2026-05-17T10:37:22.477765+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成审稿后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 39

## Round 39

6 recorded events


### User

_source line 429 · 2026-05-17T10:39:19.228384+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)
**审查侧重**: 新颖性 + 相关工作覆盖度 + 写作质量 + 完整性

---

## Summary

本文提出用 forward KL distillation + Gumbel-Sigmoid relaxation 训练 SwiGLU LLM 的 contextual sparsity predictor，替代标准 BCE 训练。核心论点是 BCE 的 per-neuron 独立梯度结构与 global top-k 推理分配不匹配，而 KL 的耦合梯度信号通过所有下游层传播，能更好地优化输出分布保真度。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 从 23.31 降至 11.79，并在 Mistral-7B-v0.3 上验证了跨架构一致性。

---

## 总体评分

**Overall**: 2.5 / 5（Borderline Findings）
**一句话总结**: 实验扎实但新颖性有限——核心贡献是将已有技术（KL distillation + Gumbel relaxation + Lagrangian penalty）组合应用于 sparsity prediction，梯度分析形式化了一个从计算图即可推导的显然性质。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 核心 claims 大部分有实验支撑，但 "eliminates compensation" 未经测试（缺 KL+compensation 实验），单 seed 主结果，三区域发现仅 3 个采样点 |
| Excitement | 2.5 / 5 | 增量贡献：将 KL 替换 BCE 用于 sparsity prediction 是合理的工程改进，但缺乏深层新理解；实际应用价值受限于严重的下游任务退化 |
| Overall | 2.5 / 5 | Borderline Findings，实验工作高于平均水平，但新颖性和实际影响力未达 main conference 门槛 |
| Reproducibility | 4 / 5 | 超参数完整，架构清晰，使用标准 benchmark；单 seed 是减分项 |
| Confidence | 4 / 5 | 熟悉 sparsity prediction 和 knowledge distillation 文献 |

---

## Strengths

**S1.** 梯度分析提供清晰的动机框架。§3.6 的 BCE vs. KL 梯度结构对比（Eq. 10 vs. 11）简洁地展示了 per-neuron 独立梯度 vs. 通过 Jacobian 耦合的全局梯度，SNR 实测（5.77×10⁻⁵ vs. 1.00×10⁻⁵，early layers 34-156×）提供了具体数值支撑。

**S2.** 消融实验设计全面。Table 3 清晰隔离了各组件贡献：divergence 方向（Forward KL vs. Reverse KL vs. JSD）、relaxation（Gumbel vs. STE，Δ=3.98）、loss isolation（BCE+Gumbel+Penalty = 38.02 证明 penalty 与 per-neuron 优化冲突）。这组消融有效排除了替代解释。

**S3.** 三区域发现（Table 5）具有实证价值。Budget-surplus（≤30%）偏好 uniform（MMLU 40.61% vs. 25.27%），budget-constrained（~40%）偏好 global（MMLU 38.06% vs. 30.68%），capacity-limited（≥50%）二者趋同——这种非单调性是一个有趣的经验发现。

**S4.** 跨架构验证（Table 6）在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上展示了一致的 KL/TEAL 优势比（≤50% sparsity 内 8% 以内），排除了模型特异性解释。

**S5.** 二维 taxonomy（Table 1: correction granularity × training signal coupling）对该领域的方法组织提供了有用的视角，清晰地标示了论文在方法空间中的位置。

**S6.** 写作质量整体良好。无 em-dash 或解释性 en-dash；-ing 短语使用合理；无明显的 AI 写作痕迹；段落结构紧凑。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 新颖性有限：核心贡献是已有技术的直接组合
- 具体位置：Method §3 全节；Related Work §2 line 13-15
- 问题：论文的核心方法是将三个已有技术组合应用于 sparsity prediction：(1) Forward KL distillation（标准 model distillation 技术，Hinton 2015），(2) Gumbel-Sigmoid relaxation（Jang et al. 2017），(3) Lagrangian/adaptive penalty（标准约束优化）。论文自身承认 MaskLLM 也使用 "frozen weights + learnable masks + KL training"（Related Work line 14），区别仅在于 dynamic per-token vs. static N:M。这是一个适用范围的扩展，而非方法论创新。
- 为什么影响接收：EMNLP main conference 期望方法论或理论层面的新贡献，而非已有组件的新组合。如果审稿人问 "what is the new algorithmic idea that didn't exist before?"，答案只能是 "we applied KL instead of BCE for this specific use case"。
- 建议修改方向：(1) 重新定位贡献为经验分析论文（empirical study），而非方法论论文；或 (2) 提出新的技术机制（如 adaptive per-layer allocation learnt jointly with the predictor），而非仅使用现成组件。

**N2** [critical] 梯度分析形式化了一个显然的性质
- 具体位置：§3.6 (Method: Gradient-Based Motivation)
- 问题：§3.6 的核心观察是：KL loss 的梯度通过所有下游层的 Jacobian (factor (b) in Eq. 11) 耦合了所有 neuron 的 mask state，而 BCE 的梯度是 per-neuron 独立的 (Eq. 10)。但这是 backpropagation 通过复合函数的基本性质——任何 end-to-end loss（不限于 KL）都会产生这种耦合，包括 MSE on output logits、cosine similarity 等。论文将此表述为 "structural mismatch" 的发现，但任何了解反向传播的读者都会认为这是显而易见的。
- 为什么影响接收：如果论文的主要理论贡献（Contribution 1）仅是形式化一个 trivial property，则论文的理论深度不足。SNR 实测数据有价值，但单独不足以撑起一条 contribution。
- 建议修改方向：(1) 深化分析，例如推导 KL 梯度在哪些条件下退化为 BCE 等效（什么时候耦合不重要？）；(2) 提供 per-layer 的消融实验，展示在不同 layer depth 下 KL 的优势如何变化，以验证 Jacobian chain length 的理论预测。

**N3** [critical] "eliminates the need for error compensation" 的 claim 未经验证
- 具体位置：Abstract line 4, Method §3 line 5, Table 3
- 问题：论文声称 KL distillation "eliminates the need for auxiliary error compensation networks at inference"，但从未测试 KL + compensation 的组合。Table 3 只比较了 KL (11.79) vs. BCE+compensation (25.44)。如果 KL+compensation 能进一步改善到 10.x，则 "eliminates the need" 是错误的——正确的 claim 应是 "achieves better results than BCE+compensation without requiring compensation"。这是论文 Abstract 级 claim 的一个关键漏洞。
- 为什么影响接收：核心 claim 缺乏必要的控制实验。
- 建议修改方向：(1) 补充 KL+compensation 实验；如果确实无改善则 claim 成立；如有改善则需修改 framing；或 (2) 弱化 claim 为 "enables competitive performance without compensation"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 推荐配置下的下游任务退化严重，削弱实际价值
- 具体位置：Table 2, Table 5; Limitations §
- 问题：论文推荐 30% sparsity + uniform allocation 作为 deployment 配置（Limitations line 3）。在此配置下：MMLU 65.27%→40.61%（38% 相对退化），GSM8K 48.75%→7.35%（85% 退化）。50% sparsity 下 MMLU 退化至随机水平。论文的 framing 强调 PPL 改进（18%@30%, 49%@50%），但实际推理能力的大幅丧失使得方法的实际部署价值存疑。
- 建议：在 Abstract/Introduction 中更显著地 acknowledge 下游退化幅度，避免给读者留下 "49% PPL reduction" 等于 "49% 质量提升" 的误导。

**W2** [warning] 单 seed 主结果，统计可信度不足
- 具体位置：Table 2 caption
- 问题：除 50% uniform（3-seed: 11.92±0.07）外，所有主结果均为单 seed。30% sparsity 下 KL uniform (8.82) vs. TEAL (10.97) 的差距为 2.15 PPL——如果 seed variance 为 0.5（合理估计），则差距的显著性无法判断。
- 建议：至少对 Table 2 的所有行提供 3-seed mean±std，这是一天以内可完成的计算。

**W3** [warning] 三区域发现的采样密度不足
- 具体位置：Table 5, §4.5 "Three Operating Regions"
- 问题：三个 "region" 基于仅 3 个采样点（30%, 40%, 50%）定义。论文自己承认 "Denser sampling (e.g., 35% sparsity) would be needed"（Table 5 caption）。两个相邻采样点之间的行为反转不能可靠地定义一个 "region"——它可能只是噪声或非单调的局部波动。
- 建议：补充 35% 和 45% 采样点；如果时间不够则弱化 claim 为 "observation" 而非 "three operating regions"。

**W4** [warning] 遗漏相关工作
- 具体位置：Related Work §2
- 问题：
  (a) **SparseInfer** (Shin et al., DATE 2025, arXiv:2411.12692)：Training-free XOR-based activation sparsity prediction，直接相关的 baseline 对比方法，未被引用。
  (b) **SVD Contextual Sparsity Predictors** (Serbin et al., March 2026, arXiv:2603.14110)：SVD-based training-free contextual sparsity predictors，非常新但直接相关，未被引用。
  这两篇代表了 training-free prediction 的最新进展，与论文的 learned prediction 方法形成直接对比。
- 建议：在 Related Work 的 "Training-Free Activation Sparsity" 段落补充讨论，并在 experiments 中考虑是否需要与 SparseInfer 进行 PPL 对比。

**W5** [warning] "consistent improvements on Mistral" 的证据薄弱
- 具体位置：Introduction line 20, Table 6, §4.6
- 问题：跨架构 claim 基于仅 1 个额外架构的 3 个 PPL 数据点（Table 6），且未报告 Mistral 的下游任务结果。"Within 8% ratio consistency at ≤50% sparsity" 的 claim 基于 2 个数据点（30%: 1.24× vs 1.22×; 50%: 2.12× vs 1.98×）。
- 建议：补充 Mistral 的下游任务评估（至少 MMLU），或弱化 "consistent" claim 为 "preliminary evidence"。

**W6** [warning] 训练/评估域内同质性
- 具体位置：§4.1 Training, Appendix D
- 问题：训练 WikiText-103，评估 WikiText-2——同域（均为 Wikipedia 文本）。OOD 评估（Appendix D, C4）仅覆盖 50% sparsity。predictor 可能学到了 WikiText 特异的 neuron importance pattern 而非通用 pattern。
- 建议：补充 30% 和 70% 在 C4 上的 OOD 评估。

---

## 小问题（不影响接收）

**M1.** Abstract 数字密度过高（137%, 11.96, 27.77%, 23.31, 11.79, 28.4%, 8%），接近数据堆砌而非叙事。建议精简至 2-3 个关键数字。

**M2.** 术语不一致：同一方法在不同位置被称为 "predictor-TEAL"（§4.1）、"KL predictor"（多处）、"KL global"/"KL uniform"（表格）。建议统一。

**M3.** 40% MMLU 反转（Table 5: uniform 30.68% vs. global 38.06%）无 error bars，可能是 seed noise。

**M4.** 无 wall-clock speedup 证明：pipeline adds 6.4% overhead（Appendix A），但 unstructured masks 不能直接加速。论文已在 Limitations 中 acknowledge，但 Introduction 的 motivation 暗示了推理加速的前景。

**M5.** Table 2 中 BCE 行标注 "uses a different inference protocol (hard mask + compensation network)"——这使得 BCE 行与其他行的比较不完全 fair，需更显著的说明。

---

## Questions

**Q1.** KL + compensation 的效果如何？这是直接验证 "eliminates the need for compensation" 这一核心 claim 的必要实验。

**Q2.** 任何 end-to-end output loss（如 MSE on logits, cosine similarity on hidden states）都会产生耦合梯度。是否测试过 MSE on output logits 作为中间方案？这能更好地隔离 "coupling" 和 "distributional matching" 的各自贡献。

**Q3.** Early-layer SNR 优势（34-156×）vs. late-layer 优势（1.7-3.8×）——per-layer 的 PPL 贡献分解是否与此 SNR pattern 一致？如果大部分增益来自 early layers，这对 late-layer starvation 问题有什么启示？

**Q4.** 表格中 predictor 在 MMLU 上从未超过 TEAL vanilla（30% global: 25.27% vs. 38.61%；uniform 恢复到 40.61% 仅 comparable）。如果 KL predictor 的核心优势只体现在 PPL 而非 downstream tasks，这是否说明 distributional fidelity 和 task-relevant preservation 之间存在 gap？

---

## Missing References

1. **SparseInfer**: Jiho Shin, Hoeseok Yang, Youngmin Yi. "SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference." DATE 2025. arXiv:2411.12692.
2. **SVD Contextual Sparsity Predictors**: Georgii Serbin, Kirill Koshkin, Zhongao Sun, et al. "SVD Contextual Sparsity Predictors for Fast LLM Inference." March 2026. arXiv:2603.14110.

---

## Overall Assessment

**评分**: 2.5 / 5（Borderline Findings）
**置信度**: 4 / 5（High）

论文的实验工作扎实——消融设计全面、跨架构验证到位、hyperparameter robustness 有据可查。但核心新颖性不足以支撑 main conference 接收：(1) 方法是已有技术（KL + Gumbel + Lagrangian）的直接组合应用；(2) 梯度分析形式化了从计算图即可推导的显然性质；(3) "eliminates compensation" 的核心 claim 缺少关键控制实验。实际价值也受限于推荐配置（30% uniform）下 MMLU 退化 38%、GSM8K 退化 85%，以及缺乏 wall-clock speedup。建议 (a) 重新定位为 empirical analysis 论文，弱化方法论贡献的 claim；(b) 补充 KL+compensation 实验和多 seed 评估以加强 soundness；(c) 考虑投递 Findings track。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-17T10:40:04.695830+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 — Round 1 审稿意见\n\n## Summary\n本文提出用 forward KL distillation + Gumbel-Sigmoid relaxation 训练 SwiGLU LLM 的 contextual sparsity predictor，替代标准 BCE 训练。核心论点是 BCE 的 per-neuron 独立梯度结构与 global top-k 推理分配不匹配，而 KL 的耦合梯度信号通过所有下游层传播，能更好地优化输出分布保真度。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 从 23.31 降至 11.79，并在 Mistral-7B-v0.3 上验证了跨架构一致性。\n\n## 总体评分\n**Overall**: 2.5 / 5（Borderline Findings）\n**一句话总结**: 实验扎实但新颖性有限——核心贡献是将已有技术（KL distillation + Gumbel relaxation + Lagrangian penalty）组合应用于 sparsity prediction，梯度分析形式化了一个从计算图即可推导的显然性质。\n\n## Strengths\nS1. 梯度分析提供清晰的动机框架\nS2. 消融实验设计全面\nS3. 三区域发现具有实证价值\nS4. 跨架构验证\nS5. 二维 taxonomy 有用\nS6. 写作质量整体良好\n\n## Must-Fix 问题\n\n**N1** [critical] 新颖性有限：核心贡献是已有技术的直接组合\n- 论文的核心方法是将三个已有技术组合应用于 sparsity prediction：(1) Forward KL distillation（Hinton 2015），(2) Gumbel-Sigmoid relaxation（Jang 2017），(3) Lagrangian/adaptive penalty。论文自身承认 MaskLLM 也使用 \"frozen weights + learnable masks + KL training\"。\n- EMNLP main conference 期望方法论或理论层面的新贡献，而非已有组件的新组合。\n- 建议：重新定位为 empirical analysis 论文，或提出新的技术机制。\n\n**N2** [critical] 梯度分析形式化了一个显然的性质\n- §3.6 的核心观察是 KL loss 的梯度通过 Jacobian 耦合所有 neuron，而 BCE 是 per-neuron 独立的。但这是 backpropagation 通过复合函数的基本性质——任何 end-to-end loss 都会产生这种耦合。\n- 如果论文的主要理论贡献仅是形式化一个 trivial property，则理论深度不足。\n- 建议：深化分析，推导 KL 梯度退化为 BCE 等效的条件，或 per-layer 消融验证 Jacobian chain length 的预测。\n\n**N3** [critical] \"eliminates the need for error compensation\" 的 claim 未经验证\n- 论文从未测试 KL + compensation 的组合。如果 KL+compensation 能改善到 10.x，则 \"eliminates the need\" 是错误的。\n- 建议：补充 KL+compensation 实验，或弱化 claim。\n\n## Should-Fix 问题\n\n**W1** 推荐配置下下游任务退化严重（MMLU 65→40%，GSM8K 48→7%）\n**W2** 单 seed 主结果\n**W3** 三区域发现仅 3 个采样点\n**W4** 遗漏相关工作：SparseInfer (Shin et al., DATE 2025), SVD Contextual Sparsity Predictors (Serbin et al., 2026)\n**W5** \"consistent improvements on Mistral\" 基于仅 1 个额外架构的 3 个 PPL 数据点，无下游结果\n**W6** 训练/评估域内同质性\n\n## 小问题\nM1. Abstract 数字密度过高\nM2. 术语不一致（predictor-TEAL / KL predictor / KL global）\nM3. 40% MMLU 反转无 error bars\nM4. 无 wall-clock speedup\nM5. Table 2 中 BCE 行标注的比较公平性\n\n## Questions\nQ1. KL + compensation 效果如何？\nQ2. MSE on output logits 是否测试过？\nQ3. Per-layer PPL 贡献是否与 SNR pattern 一致？\nQ4. KL 优势只在 PPL 而非 downstream——distributional fidelity 和 task-relevant preservation 是否存在 gap？\n\n## Missing References\n1. SparseInfer (Shin et al., DATE 2025, arXiv:2411.12692)\n2. SVD Contextual Sparsity Predictors (Serbin et al., 2026, arXiv:2603.14110)\n\n---\n\n请对以上每条 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q4) 和 Missing References 逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 — Round 1 审稿意见\n\n## Summary\n本文提出用 forward KL distillation + Gumbel-Sigmoid relaxation 训练 SwiGLU LLM 的 contextual sparsity predictor，替代标准 BCE 训练。核心论点是 BCE 的 per-neuron 独立梯度结构与 global top-k 推理分配不匹配，而 KL 的耦合梯度信号通过所有下游层传播，能更好地优化输出分布保真度。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 从 23.31 降至 11.79，并在 Mistral-7B-v0.3 上验证了跨架构一致性。\n\n## 总体评分\n**Overall**: 2.5 / 5（Borderline Findings）\n**一句话总结**: 实验扎实但新颖性有限——核心贡献是将已有技术（KL distillation + Gumbel relaxation + Lagrangian penalty）组合应用于 sparsity prediction，梯度分析形式化了一个从计算图即可推导的显然性质。\n\n## Strengths\nS1. 梯度分析提供清晰的动机框架\nS2. 消融实验设计全面\nS3. 三区域发现具有实证价值\nS4. 跨架构验证\nS5. 二维 taxonomy 有用\nS6. 写作质量整体良好\n\n## Must-Fix 问题\n\n**N1** [critical] 新颖性有限：核心贡献是已有技术的直接组合\n- 论文的核心方法是将三个已有技术组合应用于 sparsity prediction：(1) Forward KL distillation（Hinton 2015），(2) Gumbel-Sigmoid relaxation（Jang 2017），(3) Lagrangian/adaptive penalty。论文自身承认 MaskLLM 也使用 \"frozen weights + learnable masks + KL training\"。\n- EMNLP main conference 期望方法论或理论层面的新贡献，而非已有组件的新组合。\n- 建议：重新定位为 empirical analysis 论文，或提出新的技术机制。\n\n**N2** [critical] 梯度分析形式化了一个显然的性质\n- §3.6 的核心观察是 KL loss 的梯度通过 Jacobian 耦合所有 neuron，而 BCE 是 per-neuron 独立的。但这是 backpropagation 通过复合函数的基本性质——任何 end-to-end loss 都会产生这种耦合。\n- 如果论文的主要理论贡献仅是形式化一个 trivial property，则理论深度不足。\n- 建议：深化分析，推导 KL 梯度退化为 BCE 等效的条件，或 per-layer 消融验证 Jacobian chain length 的预测。\n\n**N3** [critical] \"eliminates the need for error compensation\" 的 claim 未经验证\n- 论文从未测试 KL + compensation 的组合。如果 KL+compensation 能改善到 10.x，则 \"eliminates the need\" 是错误的。\n- 建议：补充 KL+compensation 实验，或弱化 claim。\n\n## Should-Fix 问题\n\n**W1** 推荐配置下下游任务退化严重（MMLU 65→40%，GSM8K 48→7%）\n**W2** 单 seed 主结果\n**W3** 三区域发现仅 3 个采样点\n**W4** 遗漏相关工作：SparseInfer (Shin et al., DATE 2025), SVD Contextual Sparsity Predictors (Serbin et al., 2026)\n**W5** \"consistent improvements on Mistral\" 基于仅 1 个额外架构的 3 个 PPL 数据点，无下游结果\n**W6** 训练/评估域内同质性\n\n## 小问题\nM1. Abstract 数字密度过高\nM2. 术语不一致（predictor-TEAL / KL predictor / KL global）\nM3. 40% MMLU 反转无 error bars\nM4. 无 wall-clock speedup\nM5. Table 2 中 BCE 行标注的比较公平性\n\n## Questions\nQ1. KL + compensation 效果如何？\nQ2. MSE on output logits 是否测试过？\nQ3. Per-layer PPL 贡献是否与 SNR pattern 一致？\nQ4. KL 优势只在 PPL 而非 downstream——distributional fidelity 和 task-relevant preservation 是否存在 gap？\n\n## Missing References\n1. SparseInfer (Shin et al., DATE 2025, arXiv:2411.12692)\n2. SVD Contextual Sparsity Predictors (Serbin et al., 2026, arXiv:2603.14110)\n\n---\n\n请对以上每条 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q4) 和 Missing References 逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-17T10:40:34.556644+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29860
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-17T10:40:34.758120+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 1 — Round 1 审稿意见\n\n## Summary\n本文分析了 SwiGLU LLM 中 per-neuron BCE 训练与 global top-k 推理之间的结构性不匹配，提出用 forward KL 蒸馏 + Gumbel-Sigmoid 松弛训练轻量级稀疏预测器。在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上验证了 KL 在 PPL 指标上优于 TEAL 和 BCE baseline，并分析了分配策略如何影响下游任务表现。\n\n## Strengths\nS1. 梯度结构分析有价值\nS2. 实验设计系统且消融充分\nS3. 三操作区域分析有实用价值\nS4. 诚实报告负面结果\nS5. 方法简洁，无 compensation network\n\n## Weaknesses\n\n**W1. [Must-Fix] Iso-compute 对比存在严重不公平（§4.2）**\n- KL 每步需要 dense forward + sparse forward + backward through entire base model\n- BCE 每步仅需 forward pass + predictor backward\n- KL 每步成本约 2.65× BCE（45min vs 17min for 1000 steps）\n- 真正的 iso-compute 应让 BCE 训练约 7000 steps\n- 建议：明确报告 wall-clock time，或修改为 \"extended training\"\n\n**W2. [Must-Fix] BCE baseline 的 oracle 选择使对比不公平，coupling 论证存在混淆**\n- BCE 的 oracle 来自 activation magnitude，KL 直接优化 output distribution\n- 论文将优势归因于 \"gradient coupling\"，但另一解释是 magnitude-based oracle 本身是 poor proxy\n- 需要 ablation：用 KL-optimal masks 作为 BCE oracle，分离 coupling vs oracle quality\n\n**W3. [Must-Fix] 50% sparsity 下游完全崩溃，削弱核心实用性**\n- 50% sparsity MMLU ≈ 随机，GSM8K <2.2%\n- PPL 改善未转化为下游能力\n- 30% sparsity 改善温和（PPL 19%, MMLU +2pp）\n- Introduction/Abstract 应更突出 30% 为推荐操作点\n\n**W4. [Should-Fix] Gradient SNR 统计力度不足**\n- 仅 80 steps，无 error bars\n- SNR 绝对值极低\n- \"BCE SNR collapses after step 10\" 可能是收敛而非缺陷\n\n**W5. [Should-Fix] 大部分结果 single-seed**\n\n**W6. [Should-Fix] \"Near-orthogonal\" 声称缺乏依据**\n- cosine similarity 0.196 ≠ near-orthogonal\n- 高维空间中 0.196 是 statistically significant 的非零相关\n\n**W7. [Should-Fix] 30% target 偏差 5% 未讨论影响**\n\n**W8. [Should-Fix] 训练/评估数据同源性**\n\n**W9. [Minor] Table 1 BCE 行标注混淆**\n\n**W10. [Minor] Scale 限制需更谨慎措辞**\n\n**W11. [Minor] Forward KL 方向选择的理由偏弱**\n\n## Questions\nQ1. KL vs BCE per-step wall-clock time 和 peak memory？给 BCE 同等 wall-clock 能到多少？\nQ2. 用 KL-trained masks 作 BCE oracle 能否缩小差距？\nQ3. BCE+Gumbel+Penalty 比 vanilla BCE 还差——为什么 Gumbel 帮助了 KL 却伤害了 BCE？\nQ4. 30% λ_max=5000 且偏差 5%——是否 SwiGLU natural density 与 30% 不兼容？\nQ5. BCE SNR collapse after step 10 是过拟合还是收敛？\n\n## Missing References\n- ThunderKittens / FlashInfer（sparse kernel）\n- nm-sparsity 的 Nvidia 工作\n\n## Overall Assessment\nOverall: 2.5 (Borderline)\n置信度: High (4/5)\n\n---\n\n请对以上每条 Must-Fix (W1-W3)、Should-Fix (W4-W8)、Minor (W9-W11)、Questions (Q1-Q5) 和 Missing References 逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 1 — Round 1 审稿意见\n\n## Summary\n本文分析了 SwiGLU LLM 中 per-neuron BCE 训练与 global top-k 推理之间的结构性不匹配，提出用 forward KL 蒸馏 + Gumbel-Sigmoid 松弛训练轻量级稀疏预测器。在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上验证了 KL 在 PPL 指标上优于 TEAL 和 BCE baseline，并分析了分配策略如何影响下游任务表现。\n\n## Strengths\nS1. 梯度结构分析有价值\nS2. 实验设计系统且消融充分\nS3. 三操作区域分析有实用价值\nS4. 诚实报告负面结果\nS5. 方法简洁，无 compensation network\n\n## Weaknesses\n\n**W1. [Must-Fix] Iso-compute 对比存在严重不公平（§4.2）**\n- KL 每步需要 dense forward + sparse forward + backward through entire base model\n- BCE 每步仅需 forward pass + predictor backward\n- KL 每步成本约 2.65× BCE（45min vs 17min for 1000 steps）\n- 真正的 iso-compute 应让 BCE 训练约 7000 steps\n- 建议：明确报告 wall-clock time，或修改为 \"extended training\"\n\n**W2. [Must-Fix] BCE baseline 的 oracle 选择使对比不公平，coupling 论证存在混淆**\n- BCE 的 oracle 来自 activation magnitude，KL 直接优化 output distribution\n- 论文将优势归因于 \"gradient coupling\"，但另一解释是 magnitude-based oracle 本身是 poor proxy\n- 需要 ablation：用 KL-optimal masks 作为 BCE oracle，分离 coupling vs oracle quality\n\n**W3. [Must-Fix] 50% sparsity 下游完全崩溃，削弱核心实用性**\n- 50% sparsity MMLU ≈ 随机，GSM8K <2.2%\n- PPL 改善未转化为下游能力\n- 30% sparsity 改善温和（PPL 19%, MMLU +2pp）\n- Introduction/Abstract 应更突出 30% 为推荐操作点\n\n**W4. [Should-Fix] Gradient SNR 统计力度不足**\n- 仅 80 steps，无 error bars\n- SNR 绝对值极低\n- \"BCE SNR collapses after step 10\" 可能是收敛而非缺陷\n\n**W5. [Should-Fix] 大部分结果 single-seed**\n\n**W6. [Should-Fix] \"Near-orthogonal\" 声称缺乏依据**\n- cosine similarity 0.196 ≠ near-orthogonal\n- 高维空间中 0.196 是 statistically significant 的非零相关\n\n**W7. [Should-Fix] 30% target 偏差 5% 未讨论影响**\n\n**W8. [Should-Fix] 训练/评估数据同源性**\n\n**W9. [Minor] Table 1 BCE 行标注混淆**\n\n**W10. [Minor] Scale 限制需更谨慎措辞**\n\n**W11. [Minor] Forward KL 方向选择的理由偏弱**\n\n## Questions\nQ1. KL vs BCE per-step wall-clock time 和 peak memory？给 BCE 同等 wall-clock 能到多少？\nQ2. 用 KL-trained masks 作 BCE oracle 能否缩小差距？\nQ3. BCE+Gumbel+Penalty 比 vanilla BCE 还差——为什么 Gumbel 帮助了 KL 却伤害了 BCE？\nQ4. 30% λ_max=5000 且偏差 5%——是否 SwiGLU natural density 与 30% 不兼容？\nQ5. BCE SNR collapse after step 10 是过拟合还是收敛？\n\n## Missing References\n- ThunderKittens / FlashInfer（sparse kernel）\n- nm-sparsity 的 Nvidia 工作\n\n## Overall Assessment\nOverall: 2.5 (Borderline)\n置信度: High (4/5)\n\n---\n\n请对以上每条 Must-Fix (W1-W3)、Should-Fix (W4-W8)、Minor (W9-W11)、Questions (Q1-Q5) 和 Missing References 逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-17T10:40:36.066601+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1308
}
```

</details>

---


### Assistant

_source line 434 · 2026-05-17T10:40:41.720415+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 435 · 2026-05-17T10:40:44.230777+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿总结**：

- **Overall**: 2.5/5 (Borderline Findings)
- **Soundness**: 3.0/5 | **Excitement**: 2.5/5

**3 个 Must-Fix 问题**：
1. 新颖性有限——KL + Gumbel + Lagrangian 三个已有技术的直接组合，MaskLLM 已使用相同原则
2. 梯度分析形式化了 backpropagation 的基本性质（end-to-end loss 必然产生耦合梯度），理论深度不足
3. "eliminates the need for compensation" 的核心 claim 缺少 KL+compensation 控制实验

**6 个 Should-Fix 问题**：下游任务退化严重（30% sparsity 下 GSM8K 退化 85%）、单 seed 主结果、三区域发现仅 3 采样点、遗漏 SparseInfer 和 SVD-CSP 两篇直接相关工作、Mistral 跨架构证据薄弱、训练/评估同域

**写作质量**：整体良好，无 AI 写作痕迹，术语有少量不一致。格式完全合规（8 页正文、匿名、Limitations/Ethics/Checklist 齐全）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 436 · 2026-05-17T10:40:48.472139+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 41

## Round 41

2 recorded events


### User

_source line 437 · 2026-05-17T10:41:43.783814+00:00_

[Reviewer 1 审稿意见]:
## 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条评价

---

### Must-Fix 问题

**[AGREE with nuance] R2-N1: 新颖性有限，已有技术的直接组合**

同意核心判断：KL distillation (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + adaptive penalty 确实都是已有技术。论文 Related Work 自身承认与 MaskLLM 共享 "frozen weights + learnable masks + KL training" 原则（§5, Related Work paragraph 2）。

但需要注意的细微差异：(1) MaskLLM 解决 static N:M weight sparsity（per-group categorical，无跨组预算竞争），而本文解决 dynamic per-token activation sparsity under global budget constraint——优化问题本质不同；(2) 此前确实无人将 KL 应用于 per-token activation predictor 的训练，Table 2 的 "Per-token × Coupled" cell 确实是空的。

因此，技术新颖性确实有限，但 **问题新颖性** 存在——将其定位为 empirical analysis + mechanistic understanding 论文（如 "understanding when and why KL outperforms BCE"）可能更准确。对于 EMNLP Findings 而非 Main 可能更合适。

**[REBUT] R2-N2: 梯度分析形式化了一个显然的性质**

部分反驳。Reviewer 2 的论点——"任何 end-to-end loss 都会产生 Jacobian 耦合"——在数学上是正确的，但忽略了论文的实际贡献点：

1. **形式化本身有价值**：尽管 backprop coupling 是 "基本性质"，但此前文献（DejaVu, FastForward, ShadowLLM）从未讨论过这个性质对 **global top-k allocation** 的具体影响。将显然性质 formalize 并指出其在特定场景下的后果是合法的贡献——类似于 batch normalization 论文形式化了 internal covariate shift 这个 "显然" 的现象。

2. **实证验证非 trivial**：§3.6 的 SNR 测量、early-layer collapse 模式、以及 layer-depth vs advantage ratio 的 pattern（early layers 34-156×, late layers 1.7-3.8×）确实验证了 Jacobian chain length 的预测（layer 越靠前→chain 越长→coupling 优势越大）。这回应了 Reviewer 2 建议的 "per-layer 消融验证 Jacobian chain length 的预测"——论文已经做了这个分析。

3. **但我在自己的审稿中指出**：该分析存在 confound——论文未分离 "coupling effect" 和 "oracle quality effect"（我的 W2）。所以梯度分析虽然数学正确且非完全 trivial，但其因果解释力确实被高估了。

综合评价：N2 作为 "critical" 过于严厉。梯度分析的 formalization 和验证有增量贡献，但不是 groundbreaking 理论。降级为 Should-Fix 更合理。

**[AGREE] R2-N3: "eliminates the need for error compensation" 未验证**

完全同意。Table 3 有 "BCE + Compensation" (25.44) 但没有 "KL + Compensation"。论文声称 KL "eliminates" compensation need，但未验证 KL+compensation 是否能进一步改善到 e.g., PPL 10.x。这是一个简单的实验 gap。

从现有数据推测：SPON 分析（§4.5）显示 SPON bias correction 对 KL 仅贡献 2.4% improvement（12.08→11.79），暗示 "low-hanging fruit" 已被 KL 捕获。但 SPON 不等于 compensation network——后者可能捕获不同类型的残差。

建议作者：跑 KL+compensation 实验，或将 claim 弱化为 "reduces the need for" 而非 "eliminates"。

---

### Should-Fix 问题

**[AGREE] R2-W1: 推荐配置下下游任务退化严重**

同意，与我的 W3 一致。30% sparsity（推荐操作点）：MMLU 65→40%（-25pp），GSM8K 48→7%（-41pp）。这是巨大的退化。论文的 recommended configuration 仍然会让模型在 reasoning 任务上基本不可用。

**[AGREE] R2-W2: 单 seed 主结果**

同意，与我的 W5 一致。

**[AGREE with nuance] R2-W3: 三区域发现仅 3 个采样点**

同意这是一个弱点，但论文 §4.4 自身承认 "Denser sampling (e.g., 35% sparsity) would be needed to precisely locate region boundaries"。三区域的定性观察（non-monotonic allocation preference）从 30/40/50% 三个点可以建立，但精确边界需要更多数据。作为 exploratory finding 而非 definitive claim，3 个点是可接受的最低限度。但如果论文将此作为 core contribution（Introduction contribution list 第 3 条），则确实需要更多支撑。

**[PARTIALLY AGREE] R2-W4: 遗漏相关工作**

- SparseInfer (Shin et al., DATE 2025, arXiv:2411.12692)：如果确实是 hardware-aware sparse inference 方法，属于 "Training-Free" 类别，应在 §5 第一段提及。
- SVD Contextual Sparsity Predictors (Serbin et al., 2026, arXiv:2603.14110)：如果是 predictor-based contextual sparsity 方法，则与本文直接相关，必须讨论。

但需注意：我无法独立验证这两篇论文的真实性和内容。如果 Reviewer 2 能确认这些是真实发表/预印本且内容直接相关，则同意应引用。建议作者用 verify_references 工具核实。

**[AGREE] R2-W5: 跨架构 claim 基于有限数据**

同意。Mistral-7B 仅报告 PPL（Table 5），无下游 benchmarks。"consistent improvements" 的 claim 仅基于 3 个 PPL 数据点（30/50/70% sparsity）在 1 个额外架构上。这不足以支撑 "cross-architecture" 泛化的强结论。

**[AGREE] R2-W6: 训练/评估域内同质性**

同意，与我的 W8 一致。WikiText-103→WikiText-2 几乎是同分布。OOD 评估仅覆盖 50% 下的 C4。

---

### Questions

**[AGREE - valid question] R2-Q1: KL + compensation 效果如何？**

同上 N3 分析。这是论文应回答的关键问题。

**[AGREE - valid question] R2-Q2: MSE on output logits 是否测试过？**

好问题。论文 Table 2 taxonomy 列出了 "Intermediate (MSE)" 作为 ShadowLLM/D2DMoE 使用的 coupling level，但未在自己的 ablation 中测试 MSE on final logits（比 per-layer MSE 更强的 coupling）。这是一个有价值的 ablation：MSE on logits 也会产生 Jacobian coupling（因为 end-to-end），但优化的是 L2 距离而非 distributional distance。如果 MSE-on-logits 也大幅优于 BCE，则优势可能不是 KL-specific 而是 end-to-end-specific。

论文 §4.2 末尾确实提到 "Future work could further isolate coupling effects through MSE on hidden states and per-layer KL ablations"——承认了这个 gap 但未执行。

**[AGREE - insightful] R2-Q3: Per-layer PPL 贡献是否与 SNR pattern 一致？**

非常好的问题。如果 KL 的优势主要来自 early-layer 的更好 SNR（§3.6: early layers 34-156× advantage），那么 per-layer PPL 分解应显示 KL 的 early-layer masks 质量显著高于 BCE。这可以通过 per-layer mask ablation 验证（每次只用一层的 KL mask，其余用 BCE mask）。论文未做此分析。

**[AGREE - important] R2-Q4: KL 优势只在 PPL 而非 downstream**

这是我在 W3 中强调的核心问题的另一种表述。50% sparsity 下 KL PPL >>> TEAL 但 MMLU/GSM8K 均崩溃。30% 下 PPL 改善 19% 但 MMLU 仅 +2pp（40.61 vs 38.61, Table 4）。distributional fidelity (PPL) 和 task-relevant preservation (downstream) 之间确实存在 gap。这挑战了论文 "output-distribution preservation is the right objective" 的核心前提。

---

### Missing References

**[PARTIALLY AGREE] R2-Missing References**

1. SparseInfer (Shin et al., DATE 2025)：如果真实存在且是 activation sparsity 相关，应引用于 Training-Free 段落。
2. SVD Contextual Sparsity Predictors (Serbin et al., 2026)：如果真实存在且是 predictor-based 方法，应引用于 Predictor-Based 段落。

但在我的审稿中也注意到引用覆盖的其他 gap：hardware-aware pruning direction（如 nm-sparsity 相关的 Nvidia 工作）也应提及。

---

### 总结评价

Reviewer 2 的审稿意见整体中肯。主要分歧在 N2（梯度分析的 trivialness）：
- R2 认为这完全 trivial → "critical"
- 我认为 formalization + empirical verification 有增量价值，但确实不构成 strong theoretical contribution → 更适合 "Should-Fix" 级别

其余问题我大致同意，尤其是 N1（novelty）、N3（compensation claim）、W1-W6 的方向判断与我自己的审稿结论一致。

**我的 overall 评分 (2.5) 与 Reviewer 2 (2.5) 一致**，论文处于 Borderline Findings 水平。核心问题是：技术新颖性有限 + 实用价值（下游任务保持）不够 convincing + 关键对比的公平性存疑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 438 · 2026-05-17T10:41:48.855545+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 439 · 2026-05-17T10:41:51.381278+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心结论：与 Reviewer 2 在大方向上一致（overall 2.5），主要分歧在 N2 的严重程度（我认为 Should-Fix 而非 Critical，因为 formalization + SNR 验证有增量价值）。两位 reviewer 共同识别的最关键问题是：iso-compute 不公平、下游任务退化严重、单 seed 结果、compensation claim 未验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 440 · 2026-05-17T10:41:59.608486+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 43

## Round 43

8 recorded events


### User

_source line 441 · 2026-05-17T10:44:13.994129+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

逐条回应如下。

---

## Must-Fix

### R1-W1: Iso-compute 对比存在严重不公平

**[REBUT]** R1 的 7000 步计算存在数学错误。

根据 Limitations 节报告的 wall-clock 时间：KL 1000 步 = 45 min，BCE 1000 步 = 17 min。因此 KL 每步耗时 0.045 min，BCE 每步 0.017 min。等量 wall-clock 计算：45 min / 0.017 min per step = **2647 BCE 步**。论文给了 BCE **2700 步**（2700 × 0.017 = 45.9 min），这实际上已经非常接近 iso-wall-clock。

R1 声称"真正的 iso-compute 应让 BCE 训练约 7000 steps"，但 7000 = 2700 × 2.65，属于将步数比和每步成本比重复相乘的错误。

**但 R1 有两点合理之处**：(1) "Iso-Compute Analysis" 这个 section 标题确实具有误导性，因为 "2.71× the KL budget" 指的是步数而非 FLOPs，实际等效关系需要读者自行从 Limitations 节的训练时间推算；(2) FLOP 比率可能高于 wall-clock 比率（KL 需要 backward through 8B base model，BCE 仅 backward through 75.9M predictor），但 wall-clock 是更实际的对比指标。

**结论**：R1 的核心数字 claim 有误，但术语建议（改为 "extended training"）合理。这不应作为 Must-Fix。

---

### R1-W2: BCE baseline 的 oracle 选择使对比不公平，coupling 论证存在混淆

**[AGREE]** 这是一个有力的观点。

论文将 BCE vs KL 的差距归因于 "gradient coupling"（§3.6），但存在混淆变量：BCE 的 oracle 来自 activation magnitude（TEAL 的 top-k），而 KL 直接优化 output distribution。因此观察到的差距可能来自两个独立来源：(1) 耦合梯度 vs. 独立梯度；(2) magnitude-based oracle 本身是 poor proxy for output preservation。

Table 3 的 BCE+Gumbel+Penalty 消融（PPL 38.02 > vanilla BCE 27.97）部分解决了这个混淆——它表明给 BCE 相同的 Gumbel 基础设施反而更差。但 R1 提出的关键实验（用 KL-optimal masks 作为 BCE oracle）仍然缺失，这个实验能直接分离 coupling effect 和 oracle quality effect。

这与我的 N2（梯度分析形式化了显然性质）相互支撑：如果 coupling 并非核心因素而是 oracle quality 驱动了差异，则论文的理论贡献进一步弱化。

---

### R1-W3: 50% sparsity 下游完全崩溃，削弱核心实用性

**[AGREE]** 与我的 W1 完全一致。

补充数据：推荐配置（30% uniform）下，MMLU 65.27%→40.61%（−38% 相对），GSM8K 48.75%→7.35%（−85% 相对）。50% 下所有方法 MMLU ≈ random（Table 2, Table 5）。

论文的 Abstract/Introduction 重点引用的是 PPL 数字（"49% reduction"、"137% worse"），但 §4.5 和 Limitations 自身承认 "PPL is a poor proxy for reasoning"。这构成一个自我矛盾：论文用自己承认不可靠的指标作为主要 selling point。R1 建议 "Introduction/Abstract 应更突出 30% 为推荐操作点" 是正确的。

---

## Should-Fix

### R1-W4: Gradient SNR 统计力度不足

**[AGREE]** 部分同意。

80 steps 采样量确实有限，无 error bars 是方法论缺陷。但我更关注的是 SNR 分析的理论深度问题（我的 N2）而非统计力度。

R1 提出的 "BCE SNR collapses after step 10 可能是收敛而非缺陷" 是一个有力的替代解释——如果 BCE predictor 在前 10 步已经达到了其目标（per-neuron classification）的最优解，SNR 下降是正常现象而非 "collapse"。论文将此解释为 "why extended training cannot close the gap"（§3.6 line 153），但这个因果链需要更强的论证。

---

### R1-W5: 大部分结果 single-seed

**[AGREE]** 与我的 W2 完全一致。无需补充。

---

### R1-W6: "Near-orthogonal" 声称缺乏依据

**[AGREE]** R1 的技术论点正确。

在 d=4096 维空间中，随机向量的 cosine similarity 期望 ≈ 0，标准差 ≈ 1/√4096 ≈ 0.016。cosine similarity 0.196 ≈ 12σ，在统计意义上是高度显著的非零相关。

但我认为论文的实际论点可以用更弱的 claim 保全："near-orthogonal" 改为 "weakly correlated"，辅以 R² = 0.196² = 0.038（仅 3.8% 共享方差）和 2.4% PPL 改善的功能证据。问题在于措辞过强，而非结论错误。

---

### R1-W7: 30% target 偏差 5% 未讨论影响

**[AGREE]** 这是一个合理的质疑。

Appendix C Table 7 显示 30% target 的实际 sparsity 为 0.285（28.5%），偏差 5%。这意味着 "30% sparsity" 结果实际在 28.5% 运行，可能高估了该操作点的性能。论文应在 30% 结果旁标注实际 sparsity，并讨论对 PPL/downstream 的影响幅度。

---

### R1-W8: 训练/评估数据同源性

**[AGREE]** 与我的 W6 完全一致。补充：C4 OOD 评估仅覆盖 50% sparsity（Appendix D），而 30%（推荐操作点）缺失。

---

## Minor

### R1-W9: Table 1 BCE 行标注混淆

**[AGREE]** 这是 Table 2（不是 Table 1）的注释 "uses a different inference protocol (hard mask + compensation network)" 的问题。BCE 使用了不同的推理流程，与其他行不在同一比较基准上。建议要么统一 protocol，要么更显著地标注差异（如用分隔线或脚注）。

---

### R1-W10: Scale 限制需更谨慎措辞

**[AGREE]** 论文在多处使用 "at the 7–8B scale" 的限定语（Introduction line 27, §4.5 line 180, Conclusion line 5），这是诚实的。但 Introduction 的 contribution 列表中 Contribution 3 说 "three operating regions at the 7–8B scale"，这个限定可能被读者忽略。建议在 Abstract 中也加入 scale 限定。

---

### R1-W11: Forward KL 方向选择的理由偏弱

**[REBUT]** 部分反驳。

论文在 §4.3 提供了具体的技术论证：forward KL (mode-covering) 直接惩罚 q(x)≈0 where p(x)>0（即确保不遗漏重要 neuron），而 reverse KL (mode-seeking) 在 mask prediction 中可能过度集中于少数高确信 neuron。这个论证与 MiniLLM 的对比（reverse KL better for generation, forward KL better for mask prediction）形成了有意义的对比。

消融数据也支持：Forward KL (11.79) > JSD (12.54, +6.4%) > Reverse KL (12.80, +8.6%)，Table 3。

R1 说 "理由偏弱" 可能是因为论文在 §3.4 的解释过于简短（"the goal is to preserve the dense model's primary predictions rather than explore alternative modes"，仅一句话），而更详细的讨论在 §4.3。建议在 §3.4 增加交叉引用到 §4.3 的讨论。

---

## Questions

### R1-Q1: KL vs BCE per-step wall-clock time 和 peak memory？

**[AGREE]** 如上所述，wall-clock 数据已在 Limitations 中存在但不在实验部分（45 min vs 17 min），应在 §4.2 iso-compute 分析中显式报告。Peak memory 未报告，这是一个合理的信息请求。

---

### R1-Q2: 用 KL-trained masks 作 BCE oracle 能否缩小差距？

**[AGREE]** 这是 W2 的配套实验，是分离 coupling vs oracle quality 的关键。这个实验的缺失是论文理论贡献论证的重要漏洞。

---

### R1-Q3: BCE+Gumbel+Penalty 比 vanilla BCE 还差——为什么 Gumbel 帮助了 KL 却伤害了 BCE？

**[AGREE]** 这是一个有洞察力的问题。

论文给出的解释很简短（§4.3 line 108: "the penalty interferes with per-neuron optimization without global coordination"），但未深入分析。可能的机制：Gumbel noise 在 KL 下提供了有益的 mask configuration exploration（因为 KL 能通过 downstream effects 评估 configuration quality），但在 BCE 下只是增加了 per-neuron classification 的噪声（因为 BCE oracle 是固定的，噪声无法提供有用的 exploration signal）。这个分析如果写入论文会加强 coupling vs decomposed 的论证。

---

### R1-Q4: 30% λ_max=5000 且偏差 5%——是否 SwiGLU natural density 与 30% 不兼容？

**[AGREE]** 与 W7 一致。SwiGLU gate distribution 的 natural density 可能在 ~50% 附近（λ=8 for 50% target），强制压低到 30% 需要极端 penalty（λ→5000）且仍有 5% 偏差。这暗示 30% 可能超出了该方法在 SwiGLU 上的 "comfortable operating range"，而这恰恰是推荐的 deployment 操作点。

---

### R1-Q5: BCE SNR collapse after step 10 是过拟合还是收敛？

**[AGREE]** 如 W4 回应中所述，这是一个重要的替代假设。BCE predictor 对 magnitude-based oracle 的学习任务可能更简单（per-neuron independent classification），10 步内达到高准确率是合理的。SNR "collapse" 可能只是 convergence to optimum with near-zero gradient，而非信号质量问题。论文应提供 BCE 的 training loss curve 来区分这两种解释。

---

## Missing References

### ThunderKittens / FlashInfer（sparse kernel）

**[REBUT]** 论文明确限定了贡献为 prediction quality 而非 systems optimization（Appendix A line 34, Limitations line 7）。引用 sparse kernel 实现虽然 nice-to-have，但不是 related work 的必要组成部分。这是 Minor 级别，不是 Should-Fix。

### nm-sparsity 的 Nvidia 工作

**[AGREE]** 如果指 ASP (Automatic SParsity) / 2:4 structured sparsity，与 MaskLLM 的 N:M setting 相关。但论文已讨论了 MaskLLM。如果指其他具体工作，R1 需要给出具体 citation。

---

## 我与 R1 的共识和分歧总结

### 高度一致的问题（均为 Must-Fix 或 Should-Fix）
1. **下游任务退化严重**（R1-W3 = 我的 W1）
2. **Single-seed 主结果**（R1-W5 = 我的 W2）
3. **训练/评估同源性**（R1-W8 = 我的 W6）
4. **BCE oracle confound**（R1-W2，我在 N2 中从不同角度提出类似质疑）

### 我的额外关注点（R1 未充分覆盖）
1. **新颖性不足**（我的 N1）——核心方法是已有技术的直接组合
2. **梯度分析的理论深度**（我的 N2）——形式化了 backpropagation 的基本性质
3. **"eliminates compensation" claim 缺少控制实验**（我的 N3）——未测试 KL+compensation
4. **遗漏近期相关工作**（我的 W4）——SparseInfer (DATE 2025), SVD-CSP (arXiv Mar 2026)

### 我与 R1 的分歧
1. **R1-W1 (iso-compute 不公平)**：R1 的 7000 步数字是计算错误，2700 步 BCE 已接近 iso-wall-clock。术语建议合理但这不是 Must-Fix。
2. **R1-W11 (Forward KL 理由偏弱)**：论文在 §4.3 有合理的技术论证和消融支持。
3. **Missing References (sparse kernels)**：论文已限定贡献范围，sparse kernel 引用非必需。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-17T10:44:42.114414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-17T10:44:42.165657+00:00_

1	issues:
2	  # === Round 1-2 resolved issues (compact) ===
3	  - id: "R2-N1"
4	    summary: "Limitations section 格式不合规"
5	    category: format
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 1
10	    mentions: [{round: 1, reviewers: [1, 2], note: "desk-reject 条件"}]
11	    action_items: [{round: 1, action: "拆为独立 section*", assigned_to: "paper_agent", status: done}]
12	    resolution: "Commit 7018701"
13	    resolution_round: 1
14	
15	  - id: "R2-N2"
16	    summary: "页数超限"
17	    category: format
18	    severity: critical
19	    status: resolved
20	    first_raised_round: 1
21	    last_seen_round: 1
22	    mentions: [{round: 1, reviewers: [1, 2], note: "R2 提出"}]
23	    action_items: [{round: 1, action: "确认页数", assigned_to: "paper_agent", status: done}]
24	    resolution: "8p main + 2p appendix"
25	    resolution_round: 1
26	
27	  - id: "R1-N1"
28	    summary: "缺 OOD PPL 评估"
29	    category: experiment
30	    severity: critical
31	    status: resolved
32	    first_raised_round: 1
33	    last_seen_round: 1
34	    mentions: [{round: 1, reviewers: [1, 2], note: "R1 critical"}]
35	    action_items: [{round: 1, action: "C4 validation PPL", assigned_to: "main_agent", status: done}]
36	    resolution: "C4: Dense=9.21, KL=18.40, TEAL=38.75"
37	    resolution_round: 1
38	
39	  - id: "R1-N2"
40	    summary: "Structural failure 证据不足"
41	    category: method
42	    severity: critical
43	    status: resolved
44	    first_raised_round: 1
45	    last_seen_round: 1
46	    mentions: [{round: 1, reviewers: [1, 2], note: "两位独立指出"}]
47	    action_items: [{round: 1, action: "BCE+Gumbel ×3 LR 对照", assigned_to: "main_agent", status: done}]
48	    resolution: "BCE best=38.02 vs KL=11.79"
49	    resolution_round: 1
50	
51	  - id: "R1-N3"
52	    summary: "消融缺关键维度"
53	    category: experiment
54	    severity: warning
55	    status: resolved
56	    first_raised_round: 1
57	    last_seen_round: 1
58	    mentions: [{round: 1, reviewers: [1, 2], no
…[truncated 19829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-17T10:48:33.181337+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # === Round 1-2 resolved issues (compact) ===\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"desk-reject 条件\"}]\n    action_items: [{round: 1, action: \"拆为独立 section*\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit 7018701\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2 提出\"}]\n    action_items: [{round: 1, action: \"确认页数\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"8p main + 2p appendix\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1 critical\"}]\n    action_items: [{round: 1, action: \"C4 validation PPL\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"C4: Dense=9.21, KL=18.40, TEAL=38.75\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Structural failure 证据不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"两位独立指出\"}]\n    action_items: [{round: 1, action: \"BCE+Gumbel ×3 LR 对照\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"BCE best=38.02 vs KL=11.79\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融缺关键维度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"全维度 sweep\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Appendix B-C 全覆盖\"\n    resolution_round: 1\n\n  - id: \"R1-W1-Rd2\"\n    summary: \"Lagrangian 术语误用\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items:\n      - {round: 2, action: \"全文术语替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 2, action: \"启发式 schedule 说明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commits fe7c034 + e00d270\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"λ/sparsity 时序曲线缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"遗留修复\"}]\n    action_items: [{round: 2, action: \"Figure 生成+集成\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"lagrangian_dynamics.pdf in Appendix C\"\n    resolution_round: 2\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"需报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"添加 KL/Dense ratio\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"加 scale qualifier\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"30% MMLU 异常缺 per-layer 分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items: [{round: 2, action: \"Retention 分析+叙事修正\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"Late-layer starvation mechanism (commits f22d330 + 377ed61)\"\n    resolution_round: 2\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"引用偏低\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 6\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W4: 32篇仍偏低(typical 40-60), 遗漏 MiniLLM/GKD 等\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-W4: 遗漏 SparseInfer (DATE 2025) 和 SVD-CSP (arXiv 2026). R1 部分同意.\"}\n    action_items:\n      - {round: 2, action: \"补到 30+\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"补 MiniLLM, GKD, SparseLoRA, Mixture-of-Depths, D2DMoE 至 36\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"补充 SparseInfer (arXiv:2411.12692) 和 SVD-CSP (arXiv:2603.14110) 到 Related Work\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"Em-dash AI 写作信号\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 6\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"降为 info\"}\n      - {round: 6, reviewers: [2], note: \"本轮确认无 AI 写作痕迹 (S6)\"}\n    action_items: [{round: 2, action: \"全文清理\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034. Round 6 确认已清理干净.\"\n    resolution_round: 2\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"SNR 缺数学定义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"降为 info\"}]\n    action_items: [{round: 2, action: \"§3.5 加公式\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit cb05c11\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 informal\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W4\"}]\n    action_items: [{round: 1, action: \"弱化+SNR\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Gradient-Based Motivation + SNR 5.76×\"\n    resolution_round: 2\n\n  - id: \"R1-W2\"\n    summary: \"Cross-arch 仅 1 点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W2\"}]\n    action_items: [{round: 1, action: \"6-point table\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Cross-arch 6-point table\"\n    resolution_round: 2\n\n  - id: \"R2-N3\"\n    summary: \"与 SPON 区分度不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"per-token vs static\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2-W5 Round 1\"}]\n    action_items: [{round: 1, action: \"加 caveat\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  # === Round 3-4 issues ===\n\n  - id: \"R3-C1\"\n    summary: \"Responsible NLP Research Checklist + Ethics Statement 缺失\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE. ARR 强制要求。\"}\n      - {round: 4, reviewers: [], note: \"本轮未提及。ethics.tex 已包含 Ethics Statement + 完整 Checklist (A1-E1)。\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及，格式合规已确认。\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 添加 checklist + Ethics Statement\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"ethics.tex 包含完整 Ethics Statement + ARR Responsible NLP Research Checklist\"\n    resolution_round: 4\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect: KL global MMLU≈random, PPL framing 自相矛盾\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE. 最严重问题。\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N2 + R2-N3, 交叉全 AGREE. Narrative vs evidence 矛盾.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W3 + R2-W1, 交叉全 AGREE. 50% 主推区间 downstream 崩溃; 30% 推荐操作点改善温和(PPL 19%, MMLU +2pp). 论文仍以'49% PPL reduction'为主要 selling point 但自身承认 PPL is poor proxy.\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 重写\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"KL+uniform 为推荐配置; Abstract equal prominence; global 作分析对象\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract/Introduction 进一步突出 30% 为推荐操作点及该操作点的温和改善幅度; 避免用自认不可靠的 PPL 指标作为 headline claim\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C3\"\n    summary: \"无 wall-clock speedup, efficiency framing 误导\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N2, R1-W2. Conclusion 提 wall-clock 与 understanding framing 矛盾.\"}\n      - {round: 6, reviewers: [2], note: \"M4: pipeline adds 6.4% overhead, unstructured masks 不加速. 论文已 acknowledge 但 Intro motivation 仍暗示加速.\"}\n    action_items:\n      - {round: 3, action: \"D047 reframe: understanding paper\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Conclusion 删除 wall-clock speedup future direction; 改为 analysis-oriented future work\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C4\"\n    summary: \"Train-inference mask mismatch 未量化\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE with nuance.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W3, R2 AGREE. Gap decomposition 混合 discretization+allocation.\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及，可能已通过 gap decomposition 部分解决。\"}\n    action_items:\n      - {round: 3, action: \"per-token hard eval\", assigned_to: \"main_agent\", status: done}\n      - {round: 4, action: \"Gap decomposition paragraph added: 53% predictor / 47% allocation. Clean discretization isolation remains future work.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S1\"\n    summary: \"MaskLLM 技术重叠讨论不足 → 核心新颖性与 MaskLLM 区分不足\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise critical, R1 REBUT → 降 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N1 升 critical, R1 AGREE. 建议重定位为 empirical analysis.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-N1 critical + R1 AGREE with nuance. 共识: 技术新颖性有限(已有组件组合), 但问题新颖性存在(Per-token×Coupled cell 为空). 建议重定位为 empirical analysis 论文, EMNLP Findings 更适合.\"}\n    action_items:\n      - {round: 3, action: \"Related Work 添加 MaskLLM 深度对比\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"重定位为 empirical analysis contribution; MaskLLM 对比改进\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"进一步弱化方法论创新 claim, 强化 empirical analysis 和 mechanistic understanding 定位\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S2\"\n    summary: \"BCE 对比是 pipeline 差异非仅 loss 差异\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N3 critical, R2 REBUT→warning. 共识 warning. 缺 MSE/per-layer KL ablation.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W2 Must-Fix, R2 AGREE. 新角度: coupling vs oracle quality confound. BCE oracle 来自 magnitude, KL 直接优化 output distribution. 需 ablation: KL-optimal masks 作 BCE oracle. R2-Q2 还要求测试 MSE on output logits.\"}\n    action_items:\n      - {round: 3, action: \"§4.3 明确说明 loss+infrastructure 组合\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"§4.3 添加 future work sentence acknowledging MSE/per-layer KL ablation need\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"补充 coupling vs oracle quality 分离实验 (KL-optimal masks as BCE oracle); 或弱化 coupling 因果 claim 为相关性观察\", assigned_to: \"paper_agent+main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S4\"\n    summary: \"仅 7-8B 实验规模\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W5, R2 AGREE. Title 过于宽泛.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W10 Minor. 论文已有 '7-8B scale' qualifier, 但 Abstract 缺此限定.\"}\n    action_items:\n      - {round: 3, action: \"已有 scale qualifiers\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Intro/Conclusion 明确 '7-8B scale tested here'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract 中也加入 scale 限定\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S5\"\n    summary: \"Regime 分析证据不足 (6 数据点)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W1 + R2-W3. 每 regime 仅 1 数据点.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-W3: 仍仅 3 采样点(30/40/50%). R1 认为 3 点可建立定性观察但不足以定义 'region'. 建议补充 35%/45% 或弱化为 observation.\"}\n    action_items:\n      - {round: 3, action: \"降为 empirical observation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Wording changed to 'three operating regions' (non-monotonic)\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"补充 35%/45% 采样点以加强三区域 claim; 或进一步弱化措辞为 'observation at three sampled sparsity levels'\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S6\"\n    summary: \"'Parameter-free' penalty controller + 'converges' 不准确\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W6: 30%/70% λ hit cap ≠ convergence.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W7: 30% target 偏差 5%(实际 28.5%), 未讨论对 TEAL 对比的影响. R2 AGREE.\"}\n    action_items:\n      - {round: 3, action: \"删除 parameter-free, 承认 λ_max\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"'requires only λ_max'; convergence→'reaches target for 40-50%, saturates at λ_max for 30%/70%'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"报告 TEAL 在 28.5% sparsity 下的 PPL 作对比; 或讨论 5% 偏差的影响可忽略\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S7\"\n    summary: \"D2DMoE 遗漏 + missing refs (MiniLLM/GKD/SparseLoRA)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"D2DMoE taxonomy 简化; MiniLLM/GKD/SparseLoRA 遗漏; 32篇偏少.\"}\n      - {round: 6, reviewers: [], note: \"本轮未单独提及(已合并入 R2-W7-Rd2 引用偏低 issue)\"}\n    action_items:\n      - {round: 3, action: \"引用 + 更新 Table 1\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"D2DMoE added to taxonomy; MiniLLM/GKD/SparseLoRA cited. 36 refs.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S8\"\n    summary: \"Abstract PPL-centric 叙事\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"Abstract headline 是 PPL reduction 但 downstream collapse 未 equal prominence.\"}\n      - {round: 6, reviewers: [2], note: \"M1: Abstract 数字密度过高(137%, 11.96, 27.77%, 23.31 等). 建议精简至 2-3 个关键数字.\"}\n    action_items:\n      - {round: 3, action: \"精简到 3-4 核心数字\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Abstract rewritten: PPL + downstream + allocation analysis with balanced treatment\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract 数字进一步精简(当前仍有 7+ 个数字); 叙事重心调整\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S9\"\n    summary: \"Taxonomy 5/9 cells 空, post-hoc 质疑\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 部分 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W2: post-hoc 无 predictive power.\"}\n      - {round: 6, reviewers: [], note: \"本轮未单独提及. Taxonomy 保留为组织框架(S5 positive).\"}\n    action_items:\n      - {round: 3, action: \"补 DejaVu/D2DMoE\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Taxonomy dropped from contribution list; kept as §3.6 organizational framework\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M\"\n    summary: \"11 条 minor (AdamW wd, BCE threshold, ShadowLLM, bib years, GPU, Conclusion 过短等)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"混合来源\"}\n      - {round: 4, reviewers: [1, 2], note: \"部分复发: bib xu2026spon year fixed; AI 写作痕迹已清理.\"}\n      - {round: 6, reviewers: [2], note: \"M2 术语不一致(predictor-TEAL/KL predictor/KL global); M5 Table 2 BCE 行标注不清.\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 批量修复\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"SPON year 2026→2025 fixed; weight decay reported\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"统一术语(选定一个名称); Table 2 BCE 行标注更显著\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"6.4% 延迟与效率叙事矛盾\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7 Round 1\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-C3 再次 raise\"}\n      - {round: 4, reviewers: [1, 2], note: \"合并入 R3-C3. 6.4% overhead 事实不变.\"}\n      - {round: 6, reviewers: [], note: \"本轮未单独提及，已合并入 R3-C3.\"}\n    action_items:\n      - {round: 1, action: \"Reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 3, action: \"understanding paper reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Merged with R3-C3\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"三 seed 统计效力弱 → 主表全部单 seed\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 6\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出, R2 REBUT\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-S3, 升为 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W4, R2 AGREE. Table 2 所有关键对比单 seed.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W5 + R2-W2, 交叉 AGREE. 仅 50% uniform 有 3-seed(11.92±0.07), 其余全部单 seed. Gumbel 随机性可能导致差异.\"}\n    action_items:\n      - {round: 3, action: \"标注已有 4-seed mean±0.07\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"需 GPU 时间跑 multi-seed\", assigned_to: \"main_agent\", status: open}\n      - {round: 6, action: \"至少对 Table 2 所有行提供 3-seed mean±std\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 4 issues ===\n\n  - id: \"R4-C1\"\n    summary: \"PPL 22.51 幽灵数字: '91% worse PPL' claim 无表格数据支撑\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R1-N1 raise, R2 强 AGREE. 22.51 不出现在任何表格. 数据溯源链断裂.\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及. 论文已修正为 27.97/137%.\"}\n    action_items:\n      - {round: 4, action: \"22.51→27.97 全文替换, 91%→137% 全文替换. Commit a7ae77b.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit a7ae77b. Round 6 确认数据已修正.\"\n    resolution_round: 6\n\n  - id: \"R4-W1\"\n    summary: \"d030 exp_id 暗示 regime analysis 使用了错误 sparsity target 的 predictor\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [2], note: \"交叉分享中发现. d030 前缀含义待确认.\"}]\n    action_items:\n      - {round: 4, action: \"确认 d030=batch prefix 非 predictor mismatch (false alarm)\", assigned_to: \"main_agent\", status: done}\n    resolution: \"d030 是 batch 编号前缀, 非 predictor training target. 每行使用正确 sparsity target 训练的 predictor.\"\n    resolution_round: 4\n\n  - id: \"R4-W2\"\n    summary: \"Structural mismatch 洞察新颖性: end-to-end > decomposed 是基本原则\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R2-W1, R1 AGREE. 建议降低 formal analysis 权重, 强调 empirical.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-N2 critical, R1 REBUT→Should-Fix. 分歧: R2 认为完全 trivial, R1 认为 formalization+SNR 有增量价值. 共识: 不构成 strong theoretical contribution, 降低其在贡献列表中的权重.\"}\n    action_items:\n      - {round: 4, action: \"Contributions rewritten as empirical validation. Commit a7ae77b.\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"进一步弱化 Contribution 1 措辞: 从 'Identification' 改为 'Empirical observation and quantification'; 或深化分析(推导 KL 退化为 BCE 等效的条件)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"Training/eval domain overlap: WikiText-103 训练 + WikiText-2 评测, OOD 仅 50%\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R2-W6. OOD 仅 50% 一个 sparsity.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W8 + R2-W6, 交叉 AGREE. 30%(推荐操作点)缺 C4 OOD 评估.\"}\n    action_items:\n      - {round: 4, action: \"30%/40% C4 OOD eval 需 GPU 时间\", assigned_to: \"main_agent\", status: open}\n      - {round: 6, action: \"至少补充 30% sparsity 下的 C4 OOD 评估\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 6 new issues ===\n\n  - id: \"R6-N1\"\n    summary: \"'Eliminates the need for compensation' claim 缺 KL+compensation 控制实验\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R2-N3 raise critical, R1 AGREE. Table 3 有 BCE+compensation(25.44) 但无 KL+compensation. 若 KL+comp 能到 10.x 则 'eliminates' 错误. SPON 2.4% improvement 暗示 low-hanging fruit 已被 KL 捕获, 但 SPON ≠ compensation network.\"}\n    action_items:\n      - {round: 6, action: \"补 KL+compensation 实验; 或弱化 claim 为 'enables competitive performance without compensation'\", assigned_to: \"paper_agent+main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W1\"\n    summary: \"Iso-compute 术语误导: '2.71× the KL budget' 指步数非 FLOPs\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W1 Must-Fix, R2 REBUT 计算错误但同意术语建议. 实际 2700 BCE steps ≈ iso-wall-clock(45min). R1 的 7000 步是重复乘法错误. 但 'Iso-Compute Analysis' 标题仍需修改.\"}\n    action_items:\n      - {round: 6, action: \"§4.2 标题改为 'Extended Training Analysis' 或 'Iso-Wall-Clock Analysis'; 正文明确报告 wall-clock 对比\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W2\"\n    summary: \"Near-orthogonal 措辞过强: cosine 0.196 ≈ 12σ 非 near-orthogonal\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W6, R2 AGREE. d=4096 下 cosine 0.196 是统计显著非零相关. 但 R²=0.038 仅 3.8% 共享方差, 功能影响小(2.4% PPL). 措辞问题非结论问题.\"}\n    action_items:\n      - {round: 6, action: \"'near-orthogonal' 改为 'weakly correlated'; 补充 R²=0.038 和随机 baseline 对比\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W3\"\n    summary: \"SNR 实验统计力度不足: 80 steps, 无 error bars, BCE collapse 替代解释\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W4 Should-Fix, R2 部分 AGREE. 80 步无 CI; SNR 绝对值极低(两者接近零); BCE SNR collapse after step 10 可能是收敛(loss→0 → gradient→0)而非信号质量问题. 需 BCE training loss curve 区分两种解释.\"}\n    action_items:\n      - {round: 6, action: \"增加 SNR 采样至 200+ steps 并报告 95% CI; 提供 BCE training loss curve 排除收敛假说\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W4\"\n    summary: \"30% target 实际 sparsity 28.5%, 偏差 5% 对 TEAL 对比的影响未讨论\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W7, R2 AGREE. 30% 结果实际在 28.5% 运行. SwiGLU natural density ≈50%(λ=8 for 50%), 30% 可能超出 comfortable operating range 但恰恰是推荐操作点.\"}\n    action_items:\n      - {round: 6, action: \"30% 结果旁标注实际 sparsity; 报告 TEAL@28.5% 对比; 或讨论影响可忽略\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W5\"\n    summary: \"Mistral 跨架构 claim 仅 PPL 无 downstream, 3 数据点不足以支撑 'consistent'\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R2-W5, R1 AGREE. Table 6 仅 PPL, 无 MMLU/ARC-c 等. 'Within 8% ratio consistency' 基于 2 数据点(30%, 50%).\"}\n    action_items:\n      - {round: 6, action: \"补充 Mistral downstream 评估(至少 MMLU); 或弱化 'consistent' 为 'preliminary evidence'\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W6\"\n    summary: \"Table 2 BCE 行标注与正文 iso-compute 描述不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1], note: \"R1-W9 Minor. Table 2 BCE(2700 steps)标 'different inference protocol' 但 §4.2 iso-compute 中 BCE 使用 TEAL allocation(无 compensation). Table 3 区分了 BCE(no comp)=27.97 和 BCE+Comp=25.44. Table 2 的 27.97 应是 no compensation 但标注暗示有差异.\"}\n    action_items:\n      - {round: 6, action: \"统一 Table 2 和 Table 3 的 BCE 标注, 消除歧义\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M1\"\n    summary: \"Forward KL 方向选择论证分散(§3.4 一句话, §4.3 详细讨论)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W11 Minor, R2 REBUT(§4.3 有足够论证). 分歧在于 §3.4 是否需要更详细解释. 消融支持: Forward KL > JSD(+6.4%) > Reverse KL(+8.6%). 但无 error bars 下这些差异是否可靠存疑.\"}\n    action_items:\n      - {round: 6, action: \"§3.4 增加交叉引用到 §4.3 的讨论\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # === Round 1-2 resolved issues (compact) ===\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"desk-reject 条件\"}]\n    action_items: [{round: 1, action: \"拆为独立 section*\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit 7018701\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2 提出\"}]\n    action_items: [{round: 1, action: \"确认页数\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"8p main + 2p appendix\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1 critical\"}]\n    action_items: [{round: 1, action: \"C4 validation PPL\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"C4: Dense=9.21, KL=18.40, TEAL=38.75\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Structural failure 证据不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"两位独立指出\"}]\n    action_items: [{round: 1, action: \"BCE+Gumbel ×3 LR 对照\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"BCE best=38.02 vs KL=11.79\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融缺关键维度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"全维度 sweep\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Appendix B-C 全覆盖\"\n    resolution_round: 1\n\n  - id: \"R1-W1-Rd2\"\n    summary: \"Lagrangian 术语误用\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items:\n      - {round: 2, action: \"全文术语替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 2, action: \"启发式 schedule 说明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commits fe7c034 + e00d270\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"λ/sparsity 时序曲线缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"遗留修复\"}]\n    action_items: [{round: 2, action: \"Figure 生成+集成\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"lagrangian_dynamics.pdf in Appendix C\"\n    resolution_round: 2\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"需报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"添加 KL/Dense ratio\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"加 scale qualifier\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"30% MMLU 异常缺 per-layer 分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items: [{round: 2, action: \"Retention 分析+叙事修正\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"Late-layer starvation mechanism (commits f22d330 + 377ed61)\"\n    resolution_round: 2\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"引用偏低\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 6\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W4: 32篇仍偏低(typical 40-60), 遗漏 MiniLLM/GKD 等\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-W4: 遗漏 SparseInfer (DATE 2025) 和 SVD-CSP (arXiv 2026). R1 部分同意.\"}\n    action_items:\n      - {round: 2, action: \"补到 30+\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"补 MiniLLM, GKD, SparseLoRA, Mixture-of-Depths, D2DMoE 至 36\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"补充 SparseInfer (arXiv:2411.12692) 和 SVD-CSP (arXiv:2603.14110) 到 Related Work\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"Em-dash AI 写作信号\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 6\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"降为 info\"}\n      - {round: 6, reviewers: [2], note: \"本轮确认无 AI 写作痕迹 (S6)\"}\n    action_items: [{round: 2, action: \"全文清理\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034. Round 6 确认已清理干净.\"\n    resolution_round: 2\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"SNR 缺数学定义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"降为 info\"}]\n    action_items: [{round: 2, action: \"§3.5 加公式\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit cb05c11\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 informal\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W4\"}]\n    action_items: [{round: 1, action: \"弱化+SNR\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Gradient-Based Motivation + SNR 5.76×\"\n    resolution_round: 2\n\n  - id: \"R1-W2\"\n    summary: \"Cross-arch 仅 1 点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W2\"}]\n    action_items: [{round: 1, action: \"6-point table\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Cross-arch 6-point table\"\n    resolution_round: 2\n\n  - id: \"R2-N3\"\n    summary: \"与 SPON 区分度不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"per-token vs static\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2-W5 Round 1\"}]\n    action_items: [{round: 1, action: \"加 caveat\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  # === Round 3-4 issues ===\n\n  - id: \"R3-C1\"\n    summary: \"Responsible NLP Research Checklist + Ethics Statement 缺失\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE. ARR 强制要求。\"}\n      - {round: 4, reviewers: [], note: \"本轮未提及。ethics.tex 已包含 Ethics Statement + 完整 Checklist (A1-E1)。\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及，格式合规已确认。\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 添加 checklist + Ethics Statement\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"ethics.tex 包含完整 Ethics Statement + ARR Responsible NLP Research Checklist\"\n    resolution_round: 4\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect: KL global MMLU≈random, PPL framing 自相矛盾\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE. 最严重问题。\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N2 + R2-N3, 交叉全 AGREE. Narrative vs evidence 矛盾.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W3 + R2-W1, 交叉全 AGREE. 50% 主推区间 downstream 崩溃; 30% 推荐操作点改善温和(PPL 19%, MMLU +2pp). 论文仍以'49% PPL reduction'为主要 selling point 但自身承认 PPL is poor proxy.\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 重写\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"KL+uniform 为推荐配置; Abstract equal prominence; global 作分析对象\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract/Introduction 进一步突出 30% 为推荐操作点及该操作点的温和改善幅度; 避免用自认不可靠的 PPL 指标作为 headline claim\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C3\"\n    summary: \"无 wall-clock speedup, efficiency framing 误导\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N2, R1-W2. Conclusion 提 wall-clock 与 understanding framing 矛盾.\"}\n      - {round: 6, reviewers: [2], note: \"M4: pipeline adds 6.4% overhead, unstructured masks 不加速. 论文已 acknowledge 但 Intro motivation 仍暗示加速.\"}\n    action_items:\n      - {round: 3, action: \"D047 reframe: understanding paper\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Conclusion 删除 wall-clock speedup future direction; 改为 analysis-oriented future work\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C4\"\n    summary: \"Train-inference mask mismatch 未量化\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE with nuance.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W3, R2 AGREE. Gap decomposition 混合 discretization+allocation.\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及，可能已通过 gap decomposition 部分解决。\"}\n    action_items:\n      - {round: 3, action: \"per-token hard eval\", assigned_to: \"main_agent\", status: done}\n      - {round: 4, action: \"Gap decomposition paragraph added: 53% predictor / 47% allocation. Clean discretization isolation remains future work.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S1\"\n    summary: \"MaskLLM 技术重叠讨论不足 → 核心新颖性与 MaskLLM 区分不足\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise critical, R1 REBUT → 降 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N1 升 critical, R1 AGREE. 建议重定位为 empirical analysis.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-N1 critical + R1 AGREE with nuance. 共识: 技术新颖性有限(已有组件组合), 但问题新颖性存在(Per-token×Coupled cell 为空). 建议重定位为 empirical analysis 论文, EMNLP Findings 更适合.\"}\n    action_items:\n      - {round: 3, action: \"Related Work 添加 MaskLLM 深度对比\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"重定位为 empirical analysis contribution; MaskLLM 对比改进\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"进一步弱化方法论创新 claim, 强化 empirical analysis 和 mechanistic understanding 定位\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S2\"\n    summary: \"BCE 对比是 pipeline 差异非仅 loss 差异\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N3 critical, R2 REBUT→warning. 共识 warning. 缺 MSE/per-layer KL ablation.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W2 Must-Fix, R2 AGREE. 新角度: coupling vs oracle quality confound. BCE oracle 来自 magnitude, KL 直接优化 output distribution. 需 ablation: KL-optimal masks 作 BCE oracle. R2-Q2 还要求测试 MSE on output logits.\"}\n    action_items:\n      - {round: 3, action: \"§4.3 明确说明 loss+infrastructure 组合\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"§4.3 添加 future work sentence acknowledging MSE/per-layer KL ablation need\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"补充 coupling vs oracle quality 分离实验 (KL-optimal masks as BCE oracle); 或弱化 coupling 因果 claim 为相关性观察\", assigned_to: \"paper_agent+main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S4\"\n    summary: \"仅 7-8B 实验规模\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W5, R2 AGREE. Title 过于宽泛.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W10 Minor. 论文已有 '7-8B scale' qualifier, 但 Abstract 缺此限定.\"}\n    action_items:\n      - {round: 3, action: \"已有 scale qualifiers\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Intro/Conclusion 明确 '7-8B scale tested here'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract 中也加入 scale 限定\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S5\"\n    summary: \"Regime 分析证据不足 (6 数据点)\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W1 + R2-W3. 每 regime 仅 1 数据点.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-W3: 仍仅 3 采样点(30/40/50%). R1 认为 3 点可建立定性观察但不足以定义 'region'. 建议补充 35%/45% 或弱化为 observation.\"}\n    action_items:\n      - {round: 3, action: \"降为 empirical observation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Wording changed to 'three operating regions' (non-monotonic)\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"补充 35%/45% 采样点以加强三区域 claim; 或进一步弱化措辞为 'observation at three sampled sparsity levels'\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S6\"\n    summary: \"'Parameter-free' penalty controller + 'converges' 不准确\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W6: 30%/70% λ hit cap ≠ convergence.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W7: 30% target 偏差 5%(实际 28.5%), 未讨论对 TEAL 对比的影响. R2 AGREE.\"}\n    action_items:\n      - {round: 3, action: \"删除 parameter-free, 承认 λ_max\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"'requires only λ_max'; convergence→'reaches target for 40-50%, saturates at λ_max for 30%/70%'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"报告 TEAL 在 28.5% sparsity 下的 PPL 作对比; 或讨论 5% 偏差的影响可忽略\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S7\"\n    summary: \"D2DMoE 遗漏 + missing refs (MiniLLM/GKD/SparseLoRA)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"D2DMoE taxonomy 简化; MiniLLM/GKD/SparseLoRA 遗漏; 32篇偏少.\"}\n      - {round: 6, reviewers: [], note: \"本轮未单独提及(已合并入 R2-W7-Rd2 引用偏低 issue)\"}\n    action_items:\n      - {round: 3, action: \"引用 + 更新 Table 1\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"D2DMoE added to taxonomy; MiniLLM/GKD/SparseLoRA cited. 36 refs.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S8\"\n    summary: \"Abstract PPL-centric 叙事\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"Abstract headline 是 PPL reduction 但 downstream collapse 未 equal prominence.\"}\n      - {round: 6, reviewers: [2], note: \"M1: Abstract 数字密度过高(137%, 11.96, 27.77%, 23.31 等). 建议精简至 2-3 个关键数字.\"}\n    action_items:\n      - {round: 3, action: \"精简到 3-4 核心数字\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Abstract rewritten: PPL + downstream + allocation analysis with balanced treatment\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract 数字进一步精简(当前仍有 7+ 个数字); 叙事重心调整\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S9\"\n    summary: \"Taxonomy 5/9 cells 空, post-hoc 质疑\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 部分 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W2: post-hoc 无 predictive power.\"}\n      - {round: 6, reviewers: [], note: \"本轮未单独提及. Taxonomy 保留为组织框架(S5 positive).\"}\n    action_items:\n      - {round: 3, action: \"补 DejaVu/D2DMoE\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Taxonomy dropped from contribution list; kept as §3.6 organizational framework\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M\"\n    summary: \"11 条 minor (AdamW wd, BCE threshold, ShadowLLM, bib years, GPU, Conclusion 过短等)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"混合来源\"}\n      - {round: 4, reviewers: [1, 2], note: \"部分复发: bib xu2026spon year fixed; AI 写作痕迹已清理.\"}\n      - {round: 6, reviewers: [2], note: \"M2 术语不一致(predictor-TEAL/KL predictor/KL global); M5 Table 2 BCE 行标注不清.\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 批量修复\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"SPON year 2026→2025 fixed; weight decay reported\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"统一术语(选定一个名称); Table 2 BCE 行标注更显著\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"6.4% 延迟与效率叙事矛盾\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7 Round 1\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-C3 再次 raise\"}\n      - {round: 4, reviewers: [1, 2], note: \"合并入 R3-C3. 6.4% overhead 事实不变.\"}\n      - {round: 6, reviewers: [], note: \"本轮未单独提及，已合并入 R3-C3.\"}\n    action_items:\n      - {round: 1, action: \"Reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 3, action: \"understanding paper reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Merged with R3-C3\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"三 seed 统计效力弱 → 主表全部单 seed\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 6\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出, R2 REBUT\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-S3, 升为 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W4, R2 AGREE. Table 2 所有关键对比单 seed.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W5 + R2-W2, 交叉 AGREE. 仅 50% uniform 有 3-seed(11.92±0.07), 其余全部单 seed. Gumbel 随机性可能导致差异.\"}\n    action_items:\n      - {round: 3, action: \"标注已有 4-seed mean±0.07\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"需 GPU 时间跑 multi-seed\", assigned_to: \"main_agent\", status: open}\n      - {round: 6, action: \"至少对 Table 2 所有行提供 3-seed mean±std\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 4 issues ===\n\n  - id: \"R4-C1\"\n    summary: \"PPL 22.51 幽灵数字: '91% worse PPL' claim 无表格数据支撑\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R1-N1 raise, R2 强 AGREE. 22.51 不出现在任何表格. 数据溯源链断裂.\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及. 论文已修正为 27.97/137%.\"}\n    action_items:\n      - {round: 4, action: \"22.51→27.97 全文替换, 91%→137% 全文替换. Commit a7ae77b.\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit a7ae77b. Round 6 确认数据已修正.\"\n    resolution_round: 6\n\n  - id: \"R4-W1\"\n    summary: \"d030 exp_id 暗示 regime analysis 使用了错误 sparsity target 的 predictor\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [2], note: \"交叉分享中发现. d030 前缀含义待确认.\"}]\n    action_items:\n      - {round: 4, action: \"确认 d030=batch prefix 非 predictor mismatch (false alarm)\", assigned_to: \"main_agent\", status: done}\n    resolution: \"d030 是 batch 编号前缀, 非 predictor training target. 每行使用正确 sparsity target 训练的 predictor.\"\n    resolution_round: 4\n\n  - id: \"R4-W2\"\n    summary: \"Structural mismatch 洞察新颖性: end-to-end > decomposed 是基本原则\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R2-W1, R1 AGREE. 建议降低 formal analysis 权重, 强调 empirical.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-N2 critical, R1 REBUT→Should-Fix. 分歧: R2 认为完全 trivial, R1 认为 formalization+SNR 有增量价值. 共识: 不构成 strong theoretical contribution, 降低其在贡献列表中的权重.\"}\n    action_items:\n      - {round: 4, action: \"Contributions rewritten as empirical validation. Commit a7ae77b.\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"进一步弱化 Contribution 1 措辞: 从 'Identification' 改为 'Empirical observation and quantification'; 或深化分析(推导 KL 退化为 BCE 等效的条件)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"Training/eval domain overlap: WikiText-103 训练 + WikiText-2 评测, OOD 仅 50%\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R2-W6. OOD 仅 50% 一个 sparsity.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W8 + R2-W6, 交叉 AGREE. 30%(推荐操作点)缺 C4 OOD 评估.\"}\n    action_items:\n      - {round: 4, action: \"30%/40% C4 OOD eval 需 GPU 时间\", assigned_to: \"main_agent\", status: open}\n      - {round: 6, action: \"至少补充 30% sparsity 下的 C4 OOD 评估\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 6 new issues ===\n\n  - id: \"R6-N1\"\n    summary: \"'Eliminates the need for compensation' claim 缺 KL+compensation 控制实验\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R2-N3 raise critical, R1 AGREE. Table 3 有 BCE+compensation(25.44) 但无 KL+compensation. 若 KL+comp 能到 10.x 则 'eliminates' 错误. SPON 2.4% improvement 暗示 low-hanging fruit 已被 KL 捕获, 但 SPON ≠ compensation network.\"}\n    action_items:\n      - {round: 6, action: \"补 KL+compensation 实验; 或弱化 claim 为 'enables competitive performance without compensation'\", assigned_to: \"paper_agent+main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W1\"\n    summary: \"Iso-compute 术语误导: '2.71× the KL budget' 指步数非 FLOPs\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W1 Must-Fix, R2 REBUT 计算错误但同意术语建议. 实际 2700 BCE steps ≈ iso-wall-clock(45min). R1 的 7000 步是重复乘法错误. 但 'Iso-Compute Analysis' 标题仍需修改.\"}\n    action_items:\n      - {round: 6, action: \"§4.2 标题改为 'Extended Training Analysis' 或 'Iso-Wall-Clock Analysis'; 正文明确报告 wall-clock 对比\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W2\"\n    summary: \"Near-orthogonal 措辞过强: cosine 0.196 ≈ 12σ 非 near-orthogonal\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W6, R2 AGREE. d=4096 下 cosine 0.196 是统计显著非零相关. 但 R²=0.038 仅 3.8% 共享方差, 功能影响小(2.4% PPL). 措辞问题非结论问题.\"}\n    action_items:\n      - {round: 6, action: \"'near-orthogonal' 改为 'weakly correlated'; 补充 R²=0.038 和随机 baseline 对比\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W3\"\n    summary: \"SNR 实验统计力度不足: 80 steps, 无 error bars, BCE collapse 替代解释\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W4 Should-Fix, R2 部分 AGREE. 80 步无 CI; SNR 绝对值极低(两者接近零); BCE SNR collapse after step 10 可能是收敛(loss→0 → gradient→0)而非信号质量问题. 需 BCE training loss curve 区分两种解释.\"}\n    action_items:\n      - {round: 6, action: \"增加 SNR 采样至 200+ steps 并报告 95% CI; 提供 BCE training loss curve 排除收敛假说\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W4\"\n    summary: \"30% target 实际 sparsity 28.5%, 偏差 5% 对 TEAL 对比的影响未讨论\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W7, R2 AGREE. 30% 结果实际在 28.5% 运行. SwiGLU natural density ≈50%(λ=8 for 50%), 30% 可能超出 comfortable operating range 但恰恰是推荐操作点.\"}\n    action_items:\n      - {round: 6, action: \"30% 结果旁标注实际 sparsity; 报告 TEAL@28.5% 对比; 或讨论影响可忽略\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W5\"\n    summary: \"Mistral 跨架构 claim 仅 PPL 无 downstream, 3 数据点不足以支撑 'consistent'\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R2-W5, R1 AGREE. Table 6 仅 PPL, 无 MMLU/ARC-c 等. 'Within 8% ratio consistency' 基于 2 数据点(30%, 50%).\"}\n    action_items:\n      - {round: 6, action: \"补充 Mistral downstream 评估(至少 MMLU); 或弱化 'consistent' 为 'preliminary evidence'\", assigned_to: \"main_agent+paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W6\"\n    summary: \"Table 2 BCE 行标注与正文 iso-compute 描述不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1], note: \"R1-W9 Minor. Table 2 BCE(2700 steps)标 'different inference protocol' 但 §4.2 iso-compute 中 BCE 使用 TEAL allocation(无 compensation). Table 3 区分了 BCE(no comp)=27.97 和 BCE+Comp=25.44. Table 2 的 27.97 应是 no compensation 但标注暗示有差异.\"}\n    action_items:\n      - {round: 6, action: \"统一 Table 2 和 Table 3 的 BCE 标注, 消除歧义\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M1\"\n    summary: \"Forward KL 方向选择论证分散(§3.4 一句话, §4.3 详细讨论)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W11 Minor, R2 REBUT(§4.3 有足够论证). 分歧在于 §3.4 是否需要更详细解释. 消融支持: Forward KL > JSD(+6.4%) > Reverse KL(+8.6%). 但无 error bars 下这些差异是否可靠存疑.\"}\n    action_items:\n      - {round: 6, action: \"§3.4 增加交叉引用到 §4.3 的讨论\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-17T10:48:33.384834+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 28202}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-17T10:51:12.046357+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "report": "# Round 6 审稿报告 — Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+相关工作+写作+完整性)\n**轮次**: Round 1 独立审稿 + 交叉回应，1 轮收敛\n\n---\n\n## Summary\n\n本文分析了 SwiGLU LLM 中 per-neuron BCE 训练与 global top-k 推理之间的结构性不匹配，提出用 forward KL 蒸馏 + Gumbel-Sigmoid 松弛训练轻量级稀疏预测器（75.9M params, <1% base model）。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 从 23.31 降至 11.79（49%），并在 Mistral-7B-v0.3 上验证跨架构一致性。论文同时发现了 global vs uniform allocation 的三个操作区域（budget-surplus / budget-constrained / capacity-limited）。\n\n---\n\n## Strengths\n\n**S1. 梯度结构分析提供清晰的方法动机**（R1-S1, R2-S1 共识）\nBCE 梯度 per-neuron 独立 vs KL 梯度通过 Jacobian 耦合的形式化分析在数学上正确，SNR 实测（5.77×10⁻⁵ vs 1.00×10⁻⁵，early layers 34-156×）提供了定量支撑。尽管 backprop coupling 是基本性质（R2-N2），但将其 formalize 并指出对 global top-k 的具体后果有增量价值。\n\n**S2. 消融实验设计全面且有信息量**（R1-S2, R2-S2 共识）\nTable 3 清晰隔离了各组件贡献：divergence 方向（Forward/Reverse KL/JSD）、relaxation（Gumbel vs STE，Δ=3.98）、loss isolation（BCE+Gumbel+Penalty=38.02 证明 penalty 与 per-neuron 优化冲突）。Loss effect (6.6×) vs relaxation effect 的分解有信息量。\n\n**S3. 三操作区域分析有实用价值**（R1-S3, R2-S3 共识）\nNon-monotonic allocation preference（uniform@30% → global@40% → irrelevant@50%）是非 trivial 的经验发现，为部署决策提供指导。在两个架构上验证了一致性。\n\n**S4. 诚实报告负面结果**（R1-S4）\n50% downstream 崩溃、penalty 偏差、PPL-downstream 脱节均被坦诚讨论。\n\n**S5. 写作质量良好**（R2-S6）\n无 AI 写作痕迹（em-dash、-ing 短语等）。段落结构紧凑，叙事连贯。格式合规（8 页正文、匿名、Limitations/Ethics/Checklist 齐全）。\n\n**S6. 二维 taxonomy 有组织价值**（R2-S5）\nCorrection granularity × Training signal coupling 的分类框架清晰地定位了本文方法。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. [Critical] \"Eliminates the need for compensation\" 核心 claim 缺少控制实验**\n- R2-N3 raise，R1 AGREE\n- Table 3 有 BCE+Compensation (25.44) 但无 KL+Compensation。若 KL+compensation 能进一步降至 ~10.x PPL，则 \"eliminates the need\" 为错误 claim。\n- SPON 分析（2.4% PPL improvement）暗示 KL 已捕获大部分可恢复信号，但 SPON ≠ compensation network，不能替代此实验。\n- **要求**：补充 KL+compensation 实验；或弱化 claim 为 \"enables competitive performance without compensation\"。\n\n**C2. [Critical] 技术新颖性有限，已有组件的直接组合**\n- R2-N1 raise，R1 AGREE with nuance\n- 核心方法由三个已有技术组成：Forward KL distillation (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + adaptive penalty（标准约束优化）。MaskLLM 已使用相同原则（frozen weights + learnable masks + KL training）。\n- R1 指出：问题新颖性存在（Per-token × Coupled cell 此前为空），但技术新颖性有限。\n- **共识**：论文更适合定位为 empirical analysis / mechanistic understanding 论文而非方法论论文。EMNLP Findings 可能比 Main Conference 更合适。\n\n**C3. [Critical] Coupling vs oracle quality 因果归因未分离**\n- R1-W2 raise，R2 AGREE\n- 论文将 KL 优势归因于 \"gradient coupling\"（§3.6），但存在混淆变量：BCE 的 oracle 来自 activation magnitude，KL 直接优化 output distribution。观察到的差距可能源于 (1) 耦合梯度 vs 独立梯度，或 (2) magnitude-based oracle 本身是 output preservation 的 poor proxy。\n- **缺失实验**：用 KL-optimal masks 作为 BCE oracle，分离 coupling effect 和 oracle quality effect。\n- 此问题与 C2（理论深度）相互加强：如果 coupling 并非核心因素，则论文的理论贡献进一步弱化。\n\n### Warning（影响评分但不一票否决）\n\n**W1. PPL-downstream disconnect 持续存在（跨 4 轮未解决）**\n- R1-W3 + R2-W1，交叉全 AGREE。历史 issue R3-C2，已修改多轮但仍存在。\n- 50% sparsity（PPL 最大优势区间）：MMLU ≈ random，GSM8K < 2.2%。\n- 30% sparsity（推荐操作点）：PPL 改善 19%，但 MMLU 仅 +2pp（40.61 vs 38.61），GSM8K 48.75→7.35%（-85%）。\n- 论文以 \"49% PPL reduction\" 为 headline 但自身承认 PPL is poor proxy——构成自我矛盾。\n- **要求**：Abstract/Introduction 更突出 30% 为推荐操作点及该操作点的温和改善幅度。\n\n**W2. 主要结果为单 seed（跨 6 轮未解决）**\n- R1-W5 + R2-W2，交叉 AGREE。历史 issue R1-W3，持续 open。\n- 仅 50% uniform 有 3-seed（11.92±0.07），其余全部单 seed。\n- Gumbel sampling 的随机性在极端 sparsity（70%）下可能导致显著差异。\n- **要求**：至少 Table 2 所有行提供 3-seed mean±std。\n\n**W3. Iso-compute 术语误导**\n- R1-W1 raise Must-Fix，R2 REBUT 计算错误但同意术语建议。\n- R2 正确指出：R1 的 \"7000 步\" 计算为重复乘法错误。实际 2700 BCE 步 ≈ iso-wall-clock（45 min vs 45.9 min）。但 \"Iso-Compute Analysis\" 标题中 \"2.71× the KL budget\" 指步数非 FLOPs/wall-clock，具有误导性。\n- **要求**：§4.2 标题改为 \"Extended Training Analysis\"；正文明确报告 wall-clock 对比。\n\n**W4. 训练/评估域内同质性（跨 2 轮未解决）**\n- R1-W8 + R2-W6，交叉 AGREE。历史 issue R4-W3。\n- WikiText-103 训练 → WikiText-2 评估，同域（均为 Wikipedia）。OOD 评估（C4）仅覆盖 50% sparsity。\n- **要求**：至少补充 30% sparsity 下的 C4 OOD 评估。\n\n**W5. 三区域发现仅 3 个采样点**\n- R2-W3 + R1 部分 AGREE。历史 issue R3-S5。\n- 三个 \"operating regions\" 基于 30/40/50% 三个采样点。R1 认为定性观察可建立但精确边界需更多数据。\n- **要求**：补充 35%/45% 采样点；或进一步弱化为 \"observation at three sampled sparsity levels\"。\n\n**W6. 遗漏近期相关工作**\n- R2-W4 raise，R1 部分 AGREE。历史 issue R2-W7-Rd2。\n- 遗漏：SparseInfer (Shin et al., DATE 2025, arXiv:2411.12692)，SVD Contextual Sparsity Predictors (Serbin et al., 2026, arXiv:2603.14110)。\n- **要求**：Related Work 补充讨论（需先验证论文真实性）。\n\n**W7. Mistral 跨架构 claim 缺下游结果**\n- R2-W5 + R1 AGREE。\n- Table 6 仅报告 PPL，无 downstream benchmarks。\"Consistent improvements\" 基于 3 个 PPL 数据点。\n- **要求**：补充 Mistral downstream 评估（至少 MMLU）；或弱化为 \"preliminary evidence\"。\n\n**W8. SNR 实验统计力度不足**\n- R1-W4 + R2 部分 AGREE。\n- 仅 80 steps，无 error bars。BCE SNR collapse after step 10 存在替代解释（收敛而非信号质量问题）。\n- **要求**：增加采样至 200+ steps 并报告 95% CI；提供 BCE training loss curve 区分两种解释。\n\n**W9. \"Near-orthogonal\" 措辞过强**\n- R1-W6 + R2 AGREE。\n- Cosine similarity 0.196 在 d=4096 维下 ≈ 12σ，是统计显著的非零相关。但 R²=0.038（3.8% 共享方差），功能影响小（2.4% PPL）。\n- **要求**：改为 \"weakly correlated\"。\n\n**W10. 30% target 实际 sparsity 28.5%，偏差未讨论**\n- R1-W7 + R2 AGREE。\n- 30% 结果实际在 28.5% sparsity 运行，可能高估该操作点性能。\n- **要求**：标注实际 sparsity；报告 TEAL@28.5% 对比；或讨论影响可忽略。\n\n### Minor\n\n**M1.** Abstract 数字密度过高（7+ 个数字），建议精简至 2-3 个关键数字。（R2-M1）\n**M2.** 术语不一致：predictor-TEAL / KL predictor / KL global / KL uniform。（R2-M2）\n**M3.** Table 2 BCE 行标注与 §4.2 描述不一致（inference protocol 差异不清晰）。（R1-W9, R2-M5）\n**M4.** §3.4 Forward KL 方向选择的论证过于简短，与 §4.3 的详细讨论脱节。（R1-W11）\n\n---\n\n## Reviewer Consensus（交叉回应后共识）\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Compensation claim 未验证 (C1) | AGREE | Raise | **Critical** |\n| 技术新颖性有限 (C2) | AGREE with nuance | Raise | **Critical** (共识: 问题新颖性存在但技术为组合) |\n| Coupling vs oracle confound (C3) | Raise | AGREE | **Critical** |\n| PPL-downstream disconnect (W1) | Raise | AGREE | **Warning** (持续 4 轮) |\n| Single seed (W2) | Raise | AGREE | **Warning** (持续 6 轮) |\n| Iso-compute 术语 (W3) | Raise Must-Fix | REBUT 数字 + AGREE 术语 | **Warning** (R2 纠正了 R1 的计算错误) |\n| OOD 评估不足 (W4) | Raise | AGREE | **Warning** |\n| 三区域采样不足 (W5) | Partial AGREE | Raise | **Warning** |\n| Missing refs (W6) | Partial AGREE | Raise | **Warning** (需验证) |\n| Mistral 缺下游 (W7) | AGREE | Raise | **Warning** |\n| SNR 统计 (W8) | Raise | Partial AGREE | **Warning** |\n\n---\n\n## Reviewer Divergence\n\n| Issue | R1 立场 | R2 立场 | Director 判断 |\n|-------|---------|---------|--------------|\n| 梯度分析 triviality | Should-Fix（formalization + SNR 有增量价值）| Critical（backprop 基本性质）| **Should-Fix → 合并入 C3**。Formalization 有边际价值，但论文将此作为 Contribution 1 则权重过高。核心问题是 C3 的因果归因缺失。|\n| Iso-compute 严重程度 | Must-Fix（7000 步计算）| REBUT（2700 步已 iso-wall-clock）| **Warning**。R2 正确纠正了 R1 的算术错误。实际已接近 iso-wall-clock，但术语应修正。|\n| Forward KL 理由 | 偏弱 | 充分（§4.3 有论证）| **Minor**。§4.3 确实提供了技术论证和消融支持，但 §3.4 太简略需要交叉引用。|\n\n---\n\n## Questions（需作者回应）\n\n**Q1.** KL + compensation 的效果如何？这是直接验证核心 claim 的必要实验。（R2-N3, R1 AGREE）\n\n**Q2.** 如果用 KL-optimal masks（而非 magnitude-based masks）作为 BCE oracle，BCE 能否缩小与 KL 的差距？这能分离 coupling effect 和 oracle quality effect。（R1-W2, R2 AGREE）\n\n**Q3.** 是否测试过 MSE on output logits 作为中间方案？这能隔离 \"coupling\"（任何 end-to-end loss 都有）和 \"distributional matching\"（KL-specific）的各自贡献。（R2-Q2, R1 AGREE）\n\n**Q4.** BCE+Gumbel+Penalty (38.02) 比 vanilla BCE (27.97) 还差——为什么 Gumbel 帮助了 KL 却伤害了 BCE？论文 §4.3 的解释过于简短。（R1-Q3, R2 AGREE 并提出机制假说）\n\n**Q5.** BCE SNR collapse after step 10 是过拟合还是收敛？请提供 BCE training loss curve。（R1-Q5, R2 AGREE）\n\n**Q6.** Per-layer PPL 贡献分解是否与 SNR pattern（early layers 34-156×, late layers 1.7-3.8×）一致？（R2-Q3, R1 AGREE）\n\n**Q7.** KL 优势主要在 PPL 而非 downstream tasks——distributional fidelity 和 task-relevant preservation 之间是否存在 fundamental gap？（R2-Q4, R1 AGREE）\n\n---\n\n## Missing References\n\n1. **SparseInfer**: Jiho Shin, Hoeseok Yang, Youngmin Yi. \"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference.\" DATE 2025. arXiv:2411.12692. （R2 raise，R1 部分 AGREE。需验证真实性。）\n2. **SVD Contextual Sparsity Predictors**: Georgii Serbin et al. \"SVD Contextual Sparsity Predictors for Fast LLM Inference.\" March 2026. arXiv:2603.14110. （R2 raise，R1 部分 AGREE。需验证真实性。）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。\n\n---\n\n## Overall Assessment\n\n**评分: Borderline (2.5/5) — Borderline Findings**\n**置信度: High (4/5)**\n\n两位 Reviewer 独立给出一致评分（均 2.5/5），交叉回应后主要分歧在严重程度而非方向，整体收敛良好。\n\n### 核心判断\n\n本文在实验层面做了扎实的工作——消融设计全面（Table 3）、跨架构验证到位（Table 6）、三区域分析有实用价值（Table 5）、负面结果诚实报告。写作质量良好，格式完全合规。\n\n但三个 Critical 问题阻碍 Main Conference 接收：\n\n1. **核心 claim 未验证**（C1）：论文最突出的 claim \"eliminates the need for compensation\" 缺少 KL+compensation 控制实验。这是一个简单但关键的实验 gap。\n\n2. **技术新颖性有限**（C2）：方法是已有技术（KL + Gumbel + Lagrangian）的直接组合。MaskLLM 已展示了相同原则在 N:M sparsity 中的应用。Per-token × Coupled 的问题空间填充有价值，但单纯的组合应用不构成 EMNLP Main 级别的方法论贡献。\n\n3. **因果归因不足**（C3）：将 KL 优势归因于 \"gradient coupling\" 但未分离 coupling effect 和 oracle quality effect。梯度分析形式化了 backpropagation 的基本性质（R2 观点）/ 有增量价值但不构成 strong theory（R1 观点）。\n\n### 实际影响力的限制\n\n- 推荐操作点（30% sparsity）：MMLU 65→40%（-38%），GSM8K 48→7%（-85%），改善温和（PPL 19%, MMLU +2pp vs TEAL）\n- 50% sparsity（最大 PPL 优势区间）：downstream 完全崩溃\n- 6.4% 推理开销、无 wall-clock speedup\n\n### 建议\n\n1. **重新定位**：将论文定位为 empirical analysis / mechanistic understanding 论文，而非方法论论文。降低 \"structural mismatch\" 理论贡献的权重，强化经验分析的贡献（三区域发现、PPL-downstream disconnect 的量化、BCE 失败模式分析）。\n2. **补充关键实验**：KL+compensation、KL-oracle BCE ablation、multi-seed、30% C4 OOD、Mistral downstream\n3. **修正 claims**：弱化 \"eliminates compensation\"、修正 \"near-orthogonal\"、修正 \"iso-compute\" 术语\n4. **考虑 Findings track**：论文的实验工作高于平均水平，定位为 Findings 论文更合适\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 数字密度过高（7+ 个数字），建议精简至 2-3 个关键数字\n- 缺少 scale 限定（\"at the 7-8B scale\"）\n- \"49% PPL reduction\" 作为 headline 但论文自身承认 PPL is poor proxy\n\n### Introduction\n- 梯度分析的呈现清晰（Eq. 10 vs 11）\n- Contribution 1（\"Identification of structural mismatch\"）可进一步弱化为 \"Empirical observation and quantification\"\n- 建议更突出 30% 为推荐操作点\n\n### Method (§3)\n- 数学表述正确，SwiGLU、Gumbel-Sigmoid、KL loss 的推导无误\n- Adaptive penalty controller：footnote 正确区分了与 augmented Lagrangian 的差异\n- Taxonomy（Table 1）作为组织框架有价值\n\n### Experiments (§4)\n- §4.2 Iso-compute：标题需修改；wall-clock 数据应显式报告\n- §4.3 消融：设计优秀，是论文最强的部分\n- §4.4 三区域：仅 3 采样点，需更多数据或弱化 claim\n- §4.5 SPON：\"near-orthogonal\" 需修正\n- §4.6 Cross-arch：缺 downstream 数据\n\n### Related Work (§5)\n- 覆盖度可接受但可补充 SparseInfer、SVD-CSP\n- MaskLLM 对比已较充分\n\n### Conclusion\n- 简洁得体\n- Future directions 与 understanding paper 定位一致\n\n### Limitations\n- 坦诚全面\n- 可补充 coupling vs oracle quality confound 的讨论\n\n### Appendix\n- 内容扎实（latency、sensitivity、Lagrangian dynamics、OOD、stability）\n- 信息密度高\n\n---\n\n## Issue Tracker 同步\n\n本轮新增 7 个 issues（R6-N1, R6-W1 至 R6-W6, R6-M1），更新 8 个跨轮 issues 的 mentions 和 action_items。详见 `artifacts/review_issues.yaml`。\n\n跨轮持续未解决的核心问题：\n- PPL-downstream disconnect（R3-C2）：已修改 4 轮，仍存在自我矛盾\n- Single seed（R1-W3）：持续 6 轮 open\n- OOD 评估不足（R4-W3）：持续 2 轮 open\n- 新颖性定位（R3-S1）：已修改 3 轮，建议进一步弱化方法论 claim",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "report": "# Round 6 审稿报告 — Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+相关工作+写作+完整性)\n**轮次**: Round 1 独立审稿 + 交叉回应，1 轮收敛\n\n---\n\n## Summary\n\n本文分析了 SwiGLU LLM 中 per-neuron BCE 训练与 global top-k 推理之间的结构性不匹配，提出用 forward KL 蒸馏 + Gumbel-Sigmoid 松弛训练轻量级稀疏预测器（75.9M params, <1% base model）。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 从 23.31 降至 11.79（49%），并在 Mistral-7B-v0.3 上验证跨架构一致性。论文同时发现了 global vs uniform allocation 的三个操作区域（budget-surplus / budget-constrained / capacity-limited）。\n\n---\n\n## Strengths\n\n**S1. 梯度结构分析提供清晰的方法动机**（R1-S1, R2-S1 共识）\nBCE 梯度 per-neuron 独立 vs KL 梯度通过 Jacobian 耦合的形式化分析在数学上正确，SNR 实测（5.77×10⁻⁵ vs 1.00×10⁻⁵，early layers 34-156×）提供了定量支撑。尽管 backprop coupling 是基本性质（R2-N2），但将其 formalize 并指出对 global top-k 的具体后果有增量价值。\n\n**S2. 消融实验设计全面且有信息量**（R1-S2, R2-S2 共识）\nTable 3 清晰隔离了各组件贡献：divergence 方向（Forward/Reverse KL/JSD）、relaxation（Gumbel vs STE，Δ=3.98）、loss isolation（BCE+Gumbel+Penalty=38.02 证明 penalty 与 per-neuron 优化冲突）。Loss effect (6.6×) vs relaxation effect 的分解有信息量。\n\n**S3. 三操作区域分析有实用价值**（R1-S3, R2-S3 共识）\nNon-monotonic allocation preference（uniform@30% → global@40% → irrelevant@50%）是非 trivial 的经验发现，为部署决策提供指导。在两个架构上验证了一致性。\n\n**S4. 诚实报告负面结果**（R1-S4）\n50% downstream 崩溃、penalty 偏差、PPL-downstream 脱节均被坦诚讨论。\n\n**S5. 写作质量良好**（R2-S6）\n无 AI 写作痕迹（em-dash、-ing 短语等）。段落结构紧凑，叙事连贯。格式合规（8 页正文、匿名、Limitations/Ethics/Checklist 齐全）。\n\n**S6. 二维 taxonomy 有组织价值**（R2-S5）\nCorrection granularity × Training signal coupling 的分类框架清晰地定位了本文方法。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. [Critical] \"Eliminates the need for compensation\" 核心 claim 缺少控制实验**\n- R2-N3 raise，R1 AGREE\n- Table 3 有 BCE+Compensation (25.44) 但无 KL+Compensation。若 KL+compensation 能进一步降至 ~10.x PPL，则 \"eliminates the need\" 为错误 claim。\n- SPON 分析（2.4% PPL improvement）暗示 KL 已捕获大部分可恢复信号，但 SPON ≠ compensation network，不能替代此实验。\n- **要求**：补充 KL+compensation 实验；或弱化 claim 为 \"enables competitive performance without compensation\"。\n\n**C2. [Critical] 技术新颖性有限，已有组件的直接组合**\n- R2-N1 raise，R1 AGREE with nuance\n- 核心方法由三个已有技术组成：Forward KL distillation (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + adaptive penalty（标准约束优化）。MaskLLM 已使用相同原则（frozen weights + learnable masks + KL training）。\n- R1 指出：问题新颖性存在（Per-token × Coupled cell 此前为空），但技术新颖性有限。\n- **共识**：论文更适合定位为 empirical analysis / mechanistic understanding 论文而非方法论论文。EMNLP Findings 可能比 Main Conference 更合适。\n\n**C3. [Critical] Coupling vs oracle quality 因果归因未分离**\n- R1-W2 raise，R2 AGREE\n- 论文将 KL 优势归因于 \"gradient coupling\"（§3.6），但存在混淆变量：BCE 的 oracle 来自 activation magnitude，KL 直接优化 output distribution。观察到的差距可能源于 (1) 耦合梯度 vs 独立梯度，或 (2) magnitude-based oracle 本身是 output preservation 的 poor proxy。\n- **缺失实验**：用 KL-optimal masks 作为 BCE oracle，分离 coupling effect 和 oracle quality effect。\n- 此问题与 C2（理论深度）相互加强：如果 coupling 并非核心因素，则论文的理论贡献进一步弱化。\n\n### Warning（影响评分但不一票否决）\n\n**W1. PPL-downstream disconnect 持续存在（跨 4 轮未解决）**\n- R1-W3 + R2-W1，交叉全 AGREE。历史 issue R3-C2，已修改多轮但仍存在。\n- 50% sparsity（PPL 最大优势区间）：MMLU ≈ random，GSM8K < 2.2%。\n- 30% sparsity（推荐操作点）：PPL 改善 19%，但 MMLU 仅 +2pp（40.61 vs 38.61），GSM8K 48.75→7.35%（-85%）。\n- 论文以 \"49% PPL reduction\" 为 headline 但自身承认 PPL is poor proxy——构成自我矛盾。\n- **要求**：Abstract/Introduction 更突出 30% 为推荐操作点及该操作点的温和改善幅度。\n\n**W2. 主要结果为单 seed（跨 6 轮未解决）**\n- R1-W5 + R2-W2，交叉 AGREE。历史 issue R1-W3，持续 open。\n- 仅 50% uniform 有 3-seed（11.92±0.07），其余全部单 seed。\n- Gumbel sampling 的随机性在极端 sparsity（70%）下可能导致显著差异。\n- **要求**：至少 Table 2 所有行提供 3-seed mean±std。\n\n**W3. Iso-compute 术语误导**\n- R1-W1 raise Must-Fix，R2 REBUT 计算错误但同意术语建议。\n- R2 正确指出：R1 的 \"7000 步\" 计算为重复乘法错误。实际 2700 BCE 步 ≈ iso-wall-clock（45 min vs 45.9 min）。但 \"Iso-Compute Analysis\" 标题中 \"2.71× the KL budget\" 指步数非 FLOPs/wall-clock，具有误导性。\n- **要求**：§4.2 标题改为 \"Extended Training Analysis\"；正文明确报告 wall-clock 对比。\n\n**W4. 训练/评估域内同质性（跨 2 轮未解决）**\n- R1-W8 + R2-W6，交叉 AGREE。历史 issue R4-W3。\n- WikiText-103 训练 → WikiText-2 评估，同域（均为 Wikipedia）。OOD 评估（C4）仅覆盖 50% sparsity。\n- **要求**：至少补充 30% sparsity 下的 C4 OOD 评估。\n\n**W5. 三区域发现仅 3 个采样点**\n- R2-W3 + R1 部分 AGREE。历史 issue R3-S5。\n- 三个 \"operating regions\" 基于 30/40/50% 三个采样点。R1 认为定性观察可建立但精确边界需更多数据。\n- **要求**：补充 35%/45% 采样点；或进一步弱化为 \"observation at three sampled sparsity levels\"。\n\n**W6. 遗漏近期相关工作**\n- R2-W4 raise，R1 部分 AGREE。历史 issue R2-W7-Rd2。\n- 遗漏：SparseInfer (Shin et al., DATE 2025, arXiv:2411.12692)，SVD Contextual Sparsity Predictors (Serbin et al., 2026, arXiv:2603.14110)。\n- **要求**：Related Work 补充讨论（需先验证论文真实性）。\n\n**W7. Mistral 跨架构 claim 缺下游结果**\n- R2-W5 + R1 AGREE。\n- Table 6 仅报告 PPL，无 downstream benchmarks。\"Consistent improvements\" 基于 3 个 PPL 数据点。\n- **要求**：补充 Mistral downstream 评估（至少 MMLU）；或弱化为 \"preliminary evidence\"。\n\n**W8. SNR 实验统计力度不足**\n- R1-W4 + R2 部分 AGREE。\n- 仅 80 steps，无 error bars。BCE SNR collapse after step 10 存在替代解释（收敛而非信号质量问题）。\n- **要求**：增加采样至 200+ steps 并报告 95% CI；提供 BCE training loss curve 区分两种解释。\n\n**W9. \"Near-orthogonal\" 措辞过强**\n- R1-W6 + R2 AGREE。\n- Cosine similarity 0.196 在 d=4096 维下 ≈ 12σ，是统计显著的非零相关。但 R²=0.038（3.8% 共享方差），功能影响小（2.4% PPL）。\n- **要求**：改为 \"weakly correlated\"。\n\n**W10. 30% target 实际 sparsity 28.5%，偏差未讨论**\n- R1-W7 + R2 AGREE。\n- 30% 结果实际在 28.5% sparsity 运行，可能高估该操作点性能。\n- **要求**：标注实际 sparsity；报告 TEAL@28.5% 对比；或讨论影响可忽略。\n\n### Minor\n\n**M1.** Abstract 数字密度过高（7+ 个数字），建议精简至 2-3 个关键数字。（R2-M1）\n**M2.** 术语不一致：predictor-TEAL / KL predictor / KL global / KL uniform。（R2-M2）\n**M3.** Table 2 BCE 行标注与 §4.2 描述不一致（inference protocol 差异不清晰）。（R1-W9, R2-M5）\n**M4.** §3.4 Forward KL 方向选择的论证过于简短，与 §4.3 的详细讨论脱节。（R1-W11）\n\n---\n\n## Reviewer Consensus（交叉回应后共识）\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Compensation claim 未验证 (C1) | AGREE | Raise | **Critical** |\n| 技术新颖性有限 (C2) | AGREE with nuance | Raise | **Critical** (共识: 问题新颖性存在但技术为组合) |\n| Coupling vs oracle confound (C3) | Raise | AGREE | **Critical** |\n| PPL-downstream disconnect (W1) | Raise | AGREE | **Warning** (持续 4 轮) |\n| Single seed (W2) | Raise | AGREE | **Warning** (持续 6 轮) |\n| Iso-compute 术语 (W3) | Raise Must-Fix | REBUT 数字 + AGREE 术语 | **Warning** (R2 纠正了 R1 的计算错误) |\n| OOD 评估不足 (W4) | Raise | AGREE | **Warning** |\n| 三区域采样不足 (W5) | Partial AGREE | Raise | **Warning** |\n| Missing refs (W6) | Partial AGREE | Raise | **Warning** (需验证) |\n| Mistral 缺下游 (W7) | AGREE | Raise | **Warning** |\n| SNR 统计 (W8) | Raise | Partial AGREE | **Warning** |\n\n---\n\n## Reviewer Divergence\n\n| Issue | R1 立场 | R2 立场 | Director 判断 |\n|-------|---------|---------|--------------|\n| 梯度分析 triviality | Should-Fix（formalization + SNR 有增量价值）| Critical（backprop 基本性质）| **Should-Fix → 合并入 C3**。Formalization 有边际价值，但论文将此作为 Contribution 1 则权重过高。核心问题是 C3 的因果归因缺失。|\n| Iso-compute 严重程度 | Must-Fix（7000 步计算）| REBUT（2700 步已 iso-wall-clock）| **Warning**。R2 正确纠正了 R1 的算术错误。实际已接近 iso-wall-clock，但术语应修正。|\n| Forward KL 理由 | 偏弱 | 充分（§4.3 有论证）| **Minor**。§4.3 确实提供了技术论证和消融支持，但 §3.4 太简略需要交叉引用。|\n\n---\n\n## Questions（需作者回应）\n\n**Q1.** KL + compensation 的效果如何？这是直接验证核心 claim 的必要实验。（R2-N3, R1 AGREE）\n\n**Q2.** 如果用 KL-optimal masks（而非 magnitude-based masks）作为 BCE oracle，BCE 能否缩小与 KL 的差距？这能分离 coupling effect 和 oracle quality effect。（R1-W2, R2 AGREE）\n\n**Q3.** 是否测试过 MSE on output logits 作为中间方案？这能隔离 \"coupling\"（任何 end-to-end loss 都有）和 \"distributional matching\"（KL-specific）的各自贡献。（R2-Q2, R1 AGREE）\n\n**Q4.** BCE+Gumbel+Penalty (38.02) 比 vanilla BCE (27.97) 还差——为什么 Gumbel 帮助了 KL 却伤害了 BCE？论文 §4.3 的解释过于简短。（R1-Q3, R2 AGREE 并提出机制假说）\n\n**Q5.** BCE SNR collapse after step 10 是过拟合还是收敛？请提供 BCE training loss curve。（R1-Q5, R2 AGREE）\n\n**Q6.** Per-layer PPL 贡献分解是否与 SNR pattern（early layers 34-156×, late layers 1.7-3.8×）一致？（R2-Q3, R1 AGREE）\n\n**Q7.** KL 优势主要在 PPL 而非 downstream tasks——distributional fidelity 和 task-relevant preservation 之间是否存在 fundamental gap？（R2-Q4, R1 AGREE）\n\n---\n\n## Missing References\n\n1. **SparseInfer**: Jiho Shin, Hoeseok Yang, Youngmin Yi. \"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference.\" DATE 2025. arXiv:2411.12692. （R2 raise，R1 部分 AGREE。需验证真实性。）\n2. **SVD Contextual Sparsity Predictors**: Georgii Serbin et al. \"SVD Contextual Sparsity Predictors for Fast LLM Inference.\" March 2026. arXiv:2603.14110. （R2 raise，R1 部分 AGREE。需验证真实性。）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。\n\n---\n\n## Overall Assessment\n\n**评分: Borderline (2.5/5) — Borderline Findings**\n**置信度: High (4/5)**\n\n两位 Reviewer 独立给出一致评分（均 2.5/5），交叉回应后主要分歧在严重程度而非方向，整体收敛良好。\n\n### 核心判断\n\n本文在实验层面做了扎实的工作——消融设计全面（Table 3）、跨架构验证到位（Table 6）、三区域分析有实用价值（Table 5）、负面结果诚实报告。写作质量良好，格式完全合规。\n\n但三个 Critical 问题阻碍 Main Conference 接收：\n\n1. **核心 claim 未验证**（C1）：论文最突出的 claim \"eliminates the need for compensation\" 缺少 KL+compensation 控制实验。这是一个简单但关键的实验 gap。\n\n2. **技术新颖性有限**（C2）：方法是已有技术（KL + Gumbel + Lagrangian）的直接组合。MaskLLM 已展示了相同原则在 N:M sparsity 中的应用。Per-token × Coupled 的问题空间填充有价值，但单纯的组合应用不构成 EMNLP Main 级别的方法论贡献。\n\n3. **因果归因不足**（C3）：将 KL 优势归因于 \"gradient coupling\" 但未分离 coupling effect 和 oracle quality effect。梯度分析形式化了 backpropagation 的基本性质（R2 观点）/ 有增量价值但不构成 strong theory（R1 观点）。\n\n### 实际影响力的限制\n\n- 推荐操作点（30% sparsity）：MMLU 65→40%（-38%），GSM8K 48→7%（-85%），改善温和（PPL 19%, MMLU +2pp vs TEAL）\n- 50% sparsity（最大 PPL 优势区间）：downstream 完全崩溃\n- 6.4% 推理开销、无 wall-clock speedup\n\n### 建议\n\n1. **重新定位**：将论文定位为 empirical analysis / mechanistic understanding 论文，而非方法论论文。降低 \"structural mismatch\" 理论贡献的权重，强化经验分析的贡献（三区域发现、PPL-downstream disconnect 的量化、BCE 失败模式分析）。\n2. **补充关键实验**：KL+compensation、KL-oracle BCE ablation、multi-seed、30% C4 OOD、Mistral downstream\n3. **修正 claims**：弱化 \"eliminates compensation\"、修正 \"near-orthogonal\"、修正 \"iso-compute\" 术语\n4. **考虑 Findings track**：论文的实验工作高于平均水平，定位为 Findings 论文更合适\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 数字密度过高（7+ 个数字），建议精简至 2-3 个关键数字\n- 缺少 scale 限定（\"at the 7-8B scale\"）\n- \"49% PPL reduction\" 作为 headline 但论文自身承认 PPL is poor proxy\n\n### Introduction\n- 梯度分析的呈现清晰（Eq. 10 vs 11）\n- Contribution 1（\"Identification of structural mismatch\"）可进一步弱化为 \"Empirical observation and quantification\"\n- 建议更突出 30% 为推荐操作点\n\n### Method (§3)\n- 数学表述正确，SwiGLU、Gumbel-Sigmoid、KL loss 的推导无误\n- Adaptive penalty controller：footnote 正确区分了与 augmented Lagrangian 的差异\n- Taxonomy（Table 1）作为组织框架有价值\n\n### Experiments (§4)\n- §4.2 Iso-compute：标题需修改；wall-clock 数据应显式报告\n- §4.3 消融：设计优秀，是论文最强的部分\n- §4.4 三区域：仅 3 采样点，需更多数据或弱化 claim\n- §4.5 SPON：\"near-orthogonal\" 需修正\n- §4.6 Cross-arch：缺 downstream 数据\n\n### Related Work (§5)\n- 覆盖度可接受但可补充 SparseInfer、SVD-CSP\n- MaskLLM 对比已较充分\n\n### Conclusion\n- 简洁得体\n- Future directions 与 understanding paper 定位一致\n\n### Limitations\n- 坦诚全面\n- 可补充 coupling vs oracle quality confound 的讨论\n\n### Appendix\n- 内容扎实（latency、sensitivity、Lagrangian dynamics、OOD、stability）\n- 信息密度高\n\n---\n\n## Issue Tracker 同步\n\n本轮新增 7 个 issues（R6-N1, R6-W1 至 R6-W6, R6-M1），更新 8 个跨轮 issues 的 mentions 和 action_items。详见 `artifacts/review_issues.yaml`。\n\n跨轮持续未解决的核心问题：\n- PPL-downstream disconnect（R3-C2）：已修改 4 轮，仍存在自我矛盾\n- Single seed（R1-W3）：持续 6 轮 open\n- OOD 评估不足（R4-W3）：持续 2 轮 open\n- 新颖性定位（R3-S1）：已修改 3 轮，建议进一步弱化方法论 claim",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-17T10:51:16.316364+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4270
}
```

</details>

---


### Assistant

_source line 448 · 2026-05-17T10:51:27.678534+00:00_

审稿报告已投递至 Research Director。

---

**Round 6 审稿完成。** 两位 Reviewer 评分一致（2.5/5 Borderline Findings），1 轮收敛。

核心结论：

- **3 个 Critical**：(1) "eliminates compensation" claim 缺 KL+compensation 实验；(2) 技术新颖性有限（已有组件组合）；(3) coupling vs oracle quality 因果归因未分离
- **10 个 Warning**：PPL-downstream disconnect（跨 4 轮）、单 seed（跨 6 轮）、iso-compute 术语、OOD 评估不足、三区域采样不足、遗漏近期相关工作、Mistral 缺下游、SNR 统计力度、near-orthogonal 措辞、30% 偏差未讨论
- **建议**：重定位为 empirical analysis 论文，考虑 EMNLP Findings track

Issue tracker 已同步更新（7 个新 issue + 8 个跨轮更新）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 449 · 2026-05-17T10:51:30.202466+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**核心判断**：

- **R1-W1 (iso-compute 不公平)**：[REBUT] — R1 的 7000 步数字是计算错误。45 min KL / 0.017 min per BCE step = 2647 步，论文给了 2700 步，已接近 iso-wall-clock。但术语建议合理。
- **R1-W2 (oracle confound)**：[AGREE] — coupling vs oracle quality 未分离，与我的 N2 相互支撑。
- **R1-W3 (downstream collapse)**：[AGREE] — 与我的 W1 完全一致。
- **R1-W6 (near-orthogonal)**：[AGREE] — cosine 0.196 在 4096 维空间中 ≈ 12σ，统计上非零。但功能影响仅 2.4%，措辞改为 "weakly correlated" 即可。
- **R1-W11 (Forward KL rationale)**：[REBUT] — §4.3 有具体论证且消融支持。
- **与 R1 的高度共识**：downstream collapse、single-seed、训练/评估同源性、BCE oracle confound 四大问题。
- **我的额外关注**：新颖性不足、"eliminates compensation" 缺控制实验、遗漏 SparseInfer/SVD-CSP。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 450 · 2026-05-17T10:51:44.655329+00:00_

审稿报告已提交至 Research Director。

**Round 6 审稿结论**：

- **评分**：Borderline (2.5/5)，两位 Reviewer 一致
- **置信度**：High (4/5)

**3 个 Critical 问题**：
1. "Eliminates compensation" 核心 claim 缺 KL+compensation 控制实验
2. 技术新颖性有限（已有组件 KL+Gumbel+Lagrangian 的直接组合）
3. Coupling vs oracle quality 因果归因未分离

**10 个 Warning 问题**：PPL-downstream disconnect（跨 4 轮）、单 seed（跨 6 轮）、iso-compute 术语误导、OOD 评估不足、三区域仅 3 采样点、遗漏近期相关工作、Mistral 缺下游结果、SNR 统计力度不足、near-orthogonal 措辞过强、30% target 偏差 5%

**建议**：重新定位为 empirical analysis 论文，补充关键实验（KL+compensation、multi-seed、30% OOD），弱化方法论 claim，考虑 EMNLP Findings track。Issue tracker 已同步更新（7 新增 + 8 更新）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 451 · 2026-05-17T10:58:22.357668+00:00_

[RESET REQUEST] Main Agent 达到硬限
  触发原因：运行时长 8h4m
  本轮累计 56 条消息 / 8h 4min

⚠️ 你自己的 context 状态：已 56 条消息 / 8h 4min

请回复：
  [RESET AGENT]     只重置 Main Agent，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Main Agent 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 452 · 2026-05-17T10:58:30.904490+00:00_

审稿报告已成功投递，圆桌审稿流程完成。本轮讨论已完全收敛。

[RESET BOTH]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 46

## Round 46

56 recorded events


### User

_source line 453 · 2026-05-18T12:21:38.960260+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Efficient Methods for NLP
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-18T12:21:50.245811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-18T12:21:50.296819+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-18T12:21:54.865204+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-18T12:21:54.915818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-18T12:22:01.949531+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-18T12:22:03.306250+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (177 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- wallclock_speedup_30_50（准备中）\n- c4_download（准备中）\n- 其他 PREPARING 实验若干\n\n## 近期结论（本轮关键）\n\n### Compensation null result（⚠️ 影响 Claim 1）\n- **kl_comp_50pct_s42_eval** (success): 50% comp = KL-only，5 个指标完全一致（PPL 11.79, ARC 0.3285, WG 0.6346, MMLU 0.2789, GSM8K 0.0129）\n- **kl_comp_30pct_s42_eval** (success): 30% comp = KL-only，全在噪声范围（PPL 8.98 vs 8.98, ARC +0.25pp, WG -1.2pp）\n- **kl_comp_30pct_s123_eval** (success): 与 s42 完全一致（5 指标相同），因共享 base predictor\n- **kl_comp_30pct_s456_eval** (success): 全面优于 s42/s123（ARC +4.7pp, WG +2.5pp），但是底层 predictor 差异，非 comp 效果\n\n### 50% uniform multi-seed\n- **kl50_s456_uniform_eval** (success): PPL 11.95, ARC 0.3831, WG 0.6196, MMLU 0.2750, GSM8K 0.0288\n- 与 s42 uniform 对比：ARC +5.7pp, 其余接近\n\n### 训练完成\n- **kl_comp_30pct_s456** (success): 1000 steps, loss 0.6797\n- **kl_comp_50pct_s42** (success): 1000 steps, loss 1.0703\n\n## 关键发现\n**Compensation 在 30% 和 50% 均为 null result。** 训练 loss 收敛，但对 downstream 指标无任何影响。Director 需决策 Claim 1 framing。\n\n## 趋势\n成功 114 / 负向 19 / 失败 21 / 共 164\n\n## 下一步\n1. Director 决策 Claim 1 framing\n2. 4 卡全部空闲，等指令安排下一批\n3. 候选：wall-clock speedup benchmark、C4 OOD 补充\n\n## 资源状态\nwestd-34887: 0/2 GPU 占用（双卡空闲）\nwestd-417
…[truncated 52 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-18T12:22:03.306770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-18T12:22:03.307125+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-18T12:22:03.859582+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-18T12:22:03.910192+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-18T12:22:09.332398+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 465 · 2026-05-18T12:22:10.287371+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-18T12:22:10.438363+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-18T12:22:10.489122+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 468 · 2026-05-18T12:22:16.891760+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the ACL Rolling Review submission guidelines, here are the key page limit and format requirements for 2026:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). Sections on ethical considerations and limitations do not count towards page limit.

## Format Requirements

All long, short, and theme 
…[truncated 993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6604
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-18T12:22:17.846123+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here are the key details about EMNLP 2026 call for papers submission guidelines and author instructions:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to tradi
…[truncated 1691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 8513
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-18T12:22:23.017327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-18T12:22:23.369605+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions and achieves higher oracle F1 yet 139\% worse perplexity than a KL-trained predictor.
4	A lightweight predictor ($<$1\% of base parameters) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution, rendering post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
5	On LLaMA-3.1-8B at the recommended 30\% sparsity, KL reduces PPL degradation 18\% over TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$, eliminating seed-dependent instability.
6	At 50\% sparsity, the PPL advantage widens to 49\% but downstream tasks degrade regardless of allocation, revealing allocation-dependent operating regions at 7--8B scale.
7	Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though 14B reveals a scale-dependent MMLU gap not resolved by allocation strategy.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-18T12:22:23.470424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-18T12:22:23.822232+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	We provide this analysis.
9	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of $j$ alone, independent of every other neuron.
10	Under KL divergence, the gradient for neuron $j$ in layer $\ell$ factors as:
11	\begin{equation*}
12	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
13	\end{equation*}
14	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, coupling each neuron's gradient to every other neuron's mask state.
15	This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 139\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preser
…[truncated 1574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-18T12:22:23.822619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-18T12:22:24.325045+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden sta
…[truncated 14198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-18T12:22:24.325534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-18T12:22:25.279873+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}
…[truncated 16769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-18T12:22:25.280374+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-18T12:22:25.732677+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
15	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups
…[truncated 2535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-18T12:22:25.733213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-18T12:22:26.185683+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-2pt}
4	
5	A $<$1\% predictor with KL distillation halves TEAL's PPL across 7--14B; uniform allocation cuts cross-seed $\sigma$ $7.5\times$.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-18T12:22:26.186206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-18T12:22:26.688557+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	Our recommended operating point (30\% sparsity, uniform allocation) is validated at 7--8B scale; at 14B (Qwen-2.5-14B), KL's PPL advantage persists but the MMLU gap relative to TEAL/BCE is not resolved by uniform allocation (+0.8pp vs.\ +5.0pp at 8B), suggesting that KL's output-preservation objective may underweight task-specific features at higher knowledge densities. Scaling to 70B remains untested.
6	Out-of-distribution evaluation (Appendix~\ref{app:ood}) covers 30\% and 50\% sparsity on C4; extending to 70\% is left to future work.
7	Our attribution of KL's advantage to gradient coupling (\S\ref{sec:method:gradient}) is supported by SNR measurements and the BCE isolation ablation, but does not fully disentangle coupling from oracle quality: BCE uses magnitude-based oracles while KL directly optimizes output preservation, and an ablation using KL-derived masks as BCE targets would more precisely isolate the coupling effect.
8	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.
9	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on predict
…[truncated 246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-18T12:22:26.689105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-18T12:22:27.593207+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net ac
…[truncated 12466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-18T12:22:27.643873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-18T12:22:27.744721+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText a
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-18T12:22:27.946005+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-18T12:22:27.996850+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml\", \"content\": \"# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction\\n# Last updated: 2026-05-15\\n# Survey scope: 2023-2026, 4 directions\\n\\n# =============================================================================\\n# Direction 1: KL distillation for structured/activation sparsity\\n# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.\\n# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for\\n# learnable bias correction, not predictor training. This is our novelty.\\n# =============================================================================\\n\\n- title: \\\"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\\\"\\n  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]\\n  venue: ICML 2026\\n  year: 2026\\n  arxiv_id: \\\"2512.12744\\\"\\n  category: direct-competitor\\n  role: \\\"最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor\\\"\\n  key_finding: \\\"SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销\\\"\\n  relevance_to_us: \\\"SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致\\\"\\n\\n- title: \\\"Compact Language Models via Pruning and Knowledge Distillation\\\"\\n  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv_id: \\\"2407.14679\\\"\\n  category: method-component\\n  role: \\\"KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching\\\"\\n  key_finding: \\
…[truncated 3648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-18T12:22:37.585073+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-18T12:22:37.686218+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-18T12:22:39.545237+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf 2>/dev/null",
  "description": "Check existing review reports, issues tracker, and PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf 2>/dev/null",
    "description": "Check existing review reports, issues tracker, and PDF"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-18T12:22:39.997253+00:00_

round_1.md
round_3.md
round_4.md
round_5.md
round_6.md
---
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml
---
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-18T12:22:40.449277+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-18T12:22:40.550219+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \\\"unfair comparison\\\" attacks. **Iso-compute evidence (eval_bce_v3_s42)**: with 2.71× more gradient updates, BCE TEAL PPL=27.97 vs KL=12.00 (2.33× gap persists), and BCE loss saturates (step 500→2700: Δ=-0.006). The advantage is structural: BCE optimizes per-neuron binary classification, but inference uses global top-k budget allocation — per-neuron scoring is suboptimal under global reallocation. KL directly optimizes output distribution, naturally compatible with any allocation strategy. (Headline claim)\\n\\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \\\"subsuming\\\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that K
…[truncated 3353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-18T12:23:16.102683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-18T12:23:16.605797+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 15271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-18T12:23:16.756819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-18T12:23:16.757270+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-18T12:23:17.059315+00:00_

1	issues:
2	  # === Round 1-2 resolved issues (compact) ===
3	  - id: "R2-N1"
4	    summary: "Limitations section 格式不合规"
5	    category: format
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 1
10	    mentions: [{round: 1, reviewers: [1, 2], note: "desk-reject 条件"}]
11	    action_items: [{round: 1, action: "拆为独立 section*", assigned_to: "paper_agent", status: done}]
12	    resolution: "Commit 7018701"
13	    resolution_round: 1
14	
15	  - id: "R2-N2"
16	    summary: "页数超限"
17	    category: format
18	    severity: critical
19	    status: resolved
20	    first_raised_round: 1
21	    last_seen_round: 1
22	    mentions: [{round: 1, reviewers: [1, 2], note: "R2 提出"}]
23	    action_items: [{round: 1, action: "确认页数", assigned_to: "paper_agent", status: done}]
24	    resolution: "8p main + 2p appendix"
25	    resolution_round: 1
26	
27	  - id: "R1-N1"
28	    summary: "缺 OOD PPL 评估"
29	    category: experiment
30	    severity: critical
31	    status: resolved
32	    first_raised_round: 1
33	    last_seen_round: 1
34	    mentions: [{round: 1, reviewers: [1, 2], note: "R1 critical"}]
35	    action_items: [{round: 1, action: "C4 validation PPL", assigned_to: "main_agent", status: done}]
36	    resolution: "C4: Dense=9.21, KL=18.40, TEAL=38.75"
37	    resolution_round: 1
38	
39	  - id: "R1-N2"
40	    summary: "Structural failure 证据不足"
41	    category: method
42	    severity: critical
43	    status: resolved
44	    first_raised_round: 1
45	    last_seen_round: 1
46	    mentions: [{round: 1, reviewers: [1, 2], note: "两位独立指出"}]
47	    action_items: [{round: 1, action: "BCE+Gumbel ×3 LR 对照", assigned_to: "main_agent", status: done}]
48	    resolution: "BCE best=38.02 vs KL=11.79"
49	    resolution_round: 1
50	
51	  - id: "R1-N3"
52	    summary: "消融缺关键维度"
53	    category: experiment
54	    severity: warning
55	    status: resolved
56	    first_raised_round: 1
57	    last_seen_round: 1
58	    mentions: [{round: 1, reviewers: [1, 2], no
…[truncated 30119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-18T12:23:17.110007+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-18T12:24:20.013383+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Round 7 Reviewer 1，负责 **方法严谨性 + 实验充分性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL style, Long paper ≤8 页正文, double-blind\n- **评分标准**: 5=Award(前2.5%), 4=Conference(主会议), 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`\n（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n\n## 论文概要\n提出用 forward KL 蒸馏（替代 BCE）训练 SwiGLU LLM 的激活稀疏性预测器。核心论点：BCE 的 per-neuron 梯度与 TEAL 的 global top-k 推理分配存在结构性错配；KL 通过端到端梯度耦合解决此问题。在 LLaMA-3.1-8B 上，KL predictor (<1% params) 在 30% 稀疏度下 PPL 降低 18%，在 50% 下降低 49%，且 compensation network 冗余。跨架构验证涵盖 Mistral-7B 和 Qwen-2.5-14B。\n\n## 你的审查重点\n\n### 方法严谨性\n1. **梯度分析 (§3.5)**: BCE vs KL 梯度结构分析是否严谨？\"structural mismatch\" 论证是否过度包装了一个基本原理（end-to-end > decomposed）？SNR 测量的统计力度（步数、CI、替代解释）。\n2. **Gumbel-Sigmoid 松弛 (§3.3)**: 训练（soft mask）和推理（hard mask via TEAL top-k）之间的 gap 是否被充分量化？\n3. **自适应惩罚控制器 (§3.5)**: 30% 目标偏差 5%（实际 28.5%），对 TEAL 对比的影响是否讨论清楚？术语是否准确？\n4. **BCE 对比公平性 (§4.2-4.3)**: KL 与 BCE 的差异是 loss function 差异还是 pipeline 差异（oracle 来源、Gumbel vs hard mask、penalty vs threshold）？confound 是否被承认？\n\n### 实验充分性\n5. **统计效力**: 主表中多少结果有 multi-seed？单 seed 结果的可靠性？Gumbel 随机性是否被充分考虑？\n6. **OOD 评估**: 训练用 WikiText-103、评测用 WikiText-2（同源）。C4 OOD 覆盖哪些 sparsity levels？\n7. **跨架构/跨规模**: Mistral 仅 PPL 无 downstream？Qwen-14B 的 MMLU gap 是否被充分分析？\n8. **Regime 分析 (Table 4)**: 3 个采样点（30/40/50%）是否足够支撑 \"three operating regions\" 的结论？\n9. **Compensation 冗余 claim**: KL+compensation 控制实验是否存在？数据是否充分？\n\n请按 ACL 审稿标准输出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分+置信度)。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Round 7 Reviewer 1，负责 **方法严谨性 + 实验充分性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL style, Long paper ≤8 页正文, double-blind\n- **评分标准**: 5=Award(前2.5%), 4=Conference(主会议), 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`\n（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n\n## 论文概要\n提出用 forward KL 蒸馏（替代 BCE）训练 SwiGLU LLM 的激活稀疏性预测器。核心论点：BCE 的 per-neuron 梯度与 TEAL 的 global top-k 推理分配存在结构性错配；KL 通过端到端梯度耦合解决此问题。在 LLaMA-3.1-8B 上，KL predictor (<1% params) 在 30% 稀疏度下 PPL 降低 18%，在 50% 下降低 49%，且 compensation network 冗余。跨架构验证涵盖 Mistral-7B 和 Qwen-2.5-14B。\n\n## 你的审查重点\n\n### 方法严谨性\n1. **梯度分析 (§3.5)**: BCE vs KL 梯度结构分析是否严谨？\"structural mismatch\" 论证是否过度包装了一个基本原理（end-to-end > decomposed）？SNR 测量的统计力度（步数、CI、替代解释）。\n2. **Gumbel-Sigmoid 松弛 (§3.3)**: 训练（soft mask）和推理（hard mask via TEAL top-k）之间的 gap 是否被充分量化？\n3. **自适应惩罚控制器 (§3.5)**: 30% 目标偏差 5%（实际 28.5%），对 TEAL 对比的影响是否讨论清楚？术语是否准确？\n4. **BCE 对比公平性 (§4.2-4.3)**: KL 与 BCE 的差异是 loss function 差异还是 pipeline 差异（oracle 来源、Gumbel vs hard mask、penalty vs threshold）？confound 是否被承认？\n\n### 实验充分性\n5. **统计效力**: 主表中多少结果有 multi-seed？单 seed 结果的可靠性？Gumbel 随机性是否被充分考虑？\n6. **OOD 评估**: 训练用 WikiText-103、评测用 WikiText-2（同源）。C4 OOD 覆盖哪些 sparsity levels？\n7. **跨架构/跨规模**: Mistral 仅 PPL 无 downstream？Qwen-14B 的 MMLU gap 是否被充分分析？\n8. **Regime 分析 (Table 4)**: 3 个采样点（30/40/50%）是否足够支撑 \"three operating regions\" 的结论？\n9. **Compensation 冗余 claim**: KL+compensation 控制实验是否存在？数据是否充分？\n\n请按 ACL 审稿标准输出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分+置信度)。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-18T12:24:40.908230+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20894
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-18T12:24:41.360010+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Round 7 Reviewer 2，负责 **新颖性 + 完整性 + 写作格式**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL style, Long paper ≤8 页正文, double-blind\n- **评分标准**: 5=Award(前2.5%), 4=Conference(主会议), 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`\n（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, references.bib）\n\n## 论文概要\n提出用 forward KL 蒸馏（替代 BCE）训练 SwiGLU LLM 的激活稀疏性预测器。Gumbel-Sigmoid 松弛实现可微分训练。核心发现：(1) BCE 的 per-neuron 梯度与 global top-k 推理错配，KL 通过端到端耦合解决；(2) Compensation network 冗余；(3) 三个稀疏度操作区间的发现。跨架构验证涵盖 LLaMA-8B、Mistral-7B、Qwen-14B。\n\n## 你的审查重点\n\n### 新颖性评估\n1. **与 MaskLLM 的区分**: MaskLLM 也用 frozen weights + learnable masks + KL training + Gumbel relaxation。论文声称解决不同的优化问题（N:M static vs dynamic per-token global budget），但核心技术组件高度重叠。技术新颖性 vs 问题新颖性的平衡是否合理？论文是否应重新定位为 empirical analysis paper？\n2. **\"Structural mismatch\" 洞察**: end-to-end objective 优于 decomposed objective 是否是已知原则？SNR 形式化是否提供了真正的新知识？\n3. **Taxonomy (Table 1)**: \"Per-token × Coupled\" cell 为空是否构成充分的 novelty argument？仅 2×3 table，5/6 cells 有方法。\n4. **与 SPON 的关系**: SPON 也用 KL 做 sparsity，但训练 bias 而非 predictor。区分是否清晰？\n\n### 完整性评估\n5. **叙事一致性**: Abstract → Intro → Method → Results → Conclusion 是否讲述一条连贯主线？50% 的 \"49% PPL reduction\" headline vs downstream collapse 之间的张力如何处理？论文自身说 \"PPL is a poor proxy\" 但仍以 PPL 为主要卖点。\n6. **30% 推荐操作点的 selling power**: 30% 的改善幅度（PPL 18%, MMLU +2pp）是否足够支撑一篇 EMNLP 论文？\n7. **Contribution 列表与证据匹配**: 每条 contribution 是否有对应的 section/table 支撑？\n\n### 写作与格式\n8. **引用覆盖**: 36 篇引用是否达到 EMNLP 水平（典型 40-60）？是否遗漏重要相关工作？\n9. **AI 写作痕迹**: 检查 em-dash (—)、en-dash (–)、-ing 分词结尾、过度分段、禁用词（leverage/delve/utilize/myriad/plethora）。\n10. **页数合规**: 正文是否 ≤8 页？\n11. **Conclusion 长度**: 是否过于简短？\n12. **术语一致性**: predictor-TEAL / KL predictor / KL global 等术语是否统一？\n\n请按 ACL 审稿标准输出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分+置信度)。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Round 7 Reviewer 2，负责 **新颖性 + 完整性 + 写作格式**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL style, Long paper ≤8 页正文, double-blind\n- **评分标准**: 5=Award(前2.5%), 4=Conference(主会议), 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`\n（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, references.bib）\n\n## 论文概要\n提出用 forward KL 蒸馏（替代 BCE）训练 SwiGLU LLM 的激活稀疏性预测器。Gumbel-Sigmoid 松弛实现可微分训练。核心发现：(1) BCE 的 per-neuron 梯度与 global top-k 推理错配，KL 通过端到端耦合解决；(2) Compensation network 冗余；(3) 三个稀疏度操作区间的发现。跨架构验证涵盖 LLaMA-8B、Mistral-7B、Qwen-14B。\n\n## 你的审查重点\n\n### 新颖性评估\n1. **与 MaskLLM 的区分**: MaskLLM 也用 frozen weights + learnable masks + KL training + Gumbel relaxation。论文声称解决不同的优化问题（N:M static vs dynamic per-token global budget），但核心技术组件高度重叠。技术新颖性 vs 问题新颖性的平衡是否合理？论文是否应重新定位为 empirical analysis paper？\n2. **\"Structural mismatch\" 洞察**: end-to-end objective 优于 decomposed objective 是否是已知原则？SNR 形式化是否提供了真正的新知识？\n3. **Taxonomy (Table 1)**: \"Per-token × Coupled\" cell 为空是否构成充分的 novelty argument？仅 2×3 table，5/6 cells 有方法。\n4. **与 SPON 的关系**: SPON 也用 KL 做 sparsity，但训练 bias 而非 predictor。区分是否清晰？\n\n### 完整性评估\n5. **叙事一致性**: Abstract → Intro → Method → Results → Conclusion 是否讲述一条连贯主线？50% 的 \"49% PPL reduction\" headline vs downstream collapse 之间的张力如何处理？论文自身说 \"PPL is a poor proxy\" 但仍以 PPL 为主要卖点。\n6. **30% 推荐操作点的 selling power**: 30% 的改善幅度（PPL 18%, MMLU +2pp）是否足够支撑一篇 EMNLP 论文？\n7. **Contribution 列表与证据匹配**: 每条 contribution 是否有对应的 section/table 支撑？\n\n### 写作与格式\n8. **引用覆盖**: 36 篇引用是否达到 EMNLP 水平（典型 40-60）？是否遗漏重要相关工作？\n9. **AI 写作痕迹**: 检查 em-dash (—)、en-dash (–)、-ing 分词结尾、过度分段、禁用词（leverage/delve/utilize/myriad/plethora）。\n10. **页数合规**: 正文是否 ≤8 页？\n11. **Conclusion 长度**: 是否过于简短？\n12. **术语一致性**: predictor-TEAL / KL predictor / KL global 等术语是否统一？\n\n请按 ACL 审稿标准输出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分+置信度)。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-18T12:24:43.272211+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1912
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-18T12:24:44.227663+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "Round 7 审稿。论文主题：KL distillation for activation sparsity prediction in SwiGLU LLMs。目标 track: Efficient Methods for NLP。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "Round 7 审稿。论文主题：KL distillation for activation sparsity prediction in SwiGLU LLMs。目标 track: Efficient Methods for NLP。"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-18T12:24:44.830262+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 602
}
```

</details>

---


### Assistant

_source line 508 · 2026-05-18T12:24:52.222398+00:00_

两位 Reviewer 和外部审稿请求均已启动：

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性 + 实验充分性 | 审稿中 |
| Reviewer 2 | 新颖性 + 完整性 + 写作格式 | 审稿中 |
| 外部审稿 (Stanford Agentic Reviewer) | 7 维独立评估 | pending（8h 后自动提醒） |

等待两位 Reviewer 返回初审报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 47

## Round 47

6 recorded events


### User

_source line 509 · 2026-05-18T12:31:04.411806+00:00_

[Reviewer 1 审稿意见]:
## Round 7 Reviewer 1 审稿报告：方法严谨性 + 实验充分性

## 总体评分
**Overall**: 3.0 (Findings)
**Confidence**: 4/5 (Quite sure)
**一句话总结**: 实用的 KL 蒸馏方案替代 BCE 训练稀疏预测器，但核心 "structural mismatch" 叙事的因果证据不足——KL 与 BCE 的比较被多重流水线差异混淆，且缺少中间耦合度方法 (ShadowLLM/D2DMoE) 的关键 baseline。

---

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 核心方法可行，但 BCE vs KL 比较存在未解混淆变量（oracle 来源、mask 类型、sparsity 控制方式同时不同）；"structural mismatch" 论证在严格意义上是循环论证 |
| Excitement | 3.0/5 | 问题实际相关，compensation 冗余发现实用，但贡献偏 incremental（替换一个 loss），Qwen-14B 的 MMLU 负结果削弱泛化故事 |
| Reproducibility | 4.0/5 | 超参数完整，训练/评估协议清晰，缺少代码但提供了充足细节 |
| Overall Assessment | 3.0 | Findings 水平——有扎实的实验工作和诚实的局限性讨论，但因果证据的缺口和缺失的 intermediate baseline 使核心 claim 证据不充分 |

---

## 主要优势

1. **问题定义清晰且实际相关**：per-neuron training 与 global inference allocation 之间的不匹配是真实工程问题。

2. **Ablation 设计系统全面**：Table 3 逐一隔离 divergence direction、Gumbel vs STE、compensation 效果。

3. **诚实的局限性讨论**：主动承认 confound 未完全 disentangle、Qwen-14B MMLU gap、single-seed 局限。

4. **Compensation 冗余的实用价值**：KL predictor 使 67.2M 参数 compensation network 冗余，减少 2.7% inference latency。

5. **Training 效率极高**：1000 步/45 分钟训练达到饱和。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] BCE 与 KL 比较存在多重混淆变量，不能支撑 "structural mismatch" 因果 claim

- 具体位置：§3.6、§4.3、Table 3
- 问题：KL 与 BCE 的比较存在至少四个同时变化的因素：(1) loss function；(2) oracle 来源（output distribution vs magnitude-based threshold）；(3) mask 类型（Gumbel-Sigmoid 连续 vs hard threshold）；(4) sparsity 控制（adaptive penalty vs oracle 内建 threshold）。论文的 "loss isolation" ablation（BCE + Gumbel + Penalty = PPL 38.02）并未清楚隔离 loss 效果——adaptive penalty 对 BCE per-neuron 目标产生干扰。关键缺失实验：(a) BCE trained on KL-derived oracle masks，或 (b) KL with magnitude-based oracle constraints。论文在 §4.3 和 Limitations 中承认此问题但未执行。
- 影响：论文核心叙事建立在 "structural mismatch → KL coupling resolves it" 的因果链上。当前证据无法区分 "梯度耦合本身有益" 和 "直接优化正确指标有益" 两种解释。
- 建议：执行 oracle-swap ablation；或将 "structural mismatch" 从因果 claim 降级为 motivating hypothesis。

**N2** [critical] 缺少 intermediate coupling (MSE) baseline 比较

- 具体位置：Table 1、§2 Related Work
- 问题：Taxonomy 将方法分为 Decomposed/Intermediate/Coupled 三级，但实验只比较两个极端。ShadowLLM 和 D2DMoE（MSE, intermediate）从未作为 baseline。如果 intermediate coupling 已获得大部分优势，full end-to-end KL 的额外复杂性失去正当性。
- 建议：实现 MSE hidden-state loss baseline；如资源不足，明确讨论此缺失。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Three operating regions" 结论基于 3 个数据点

- 具体位置：§4.5、Table 4
- 30/40/50% 三点拟合三类 regime，自由度为零。40% 全部 single seed。
- 建议：补充中间 sparsity 点或降级为 "preliminary observation"。

**W2** [warning] 40% uniform PPL (8.36) 低于 30% uniform PPL (8.82) 的反直觉结果未讨论

- 具体位置：Table 4
- 更高稀疏度应导致更高 PPL。可能与 30% target penalty controller 饱和（λ→5000）导致 predictor 质量下降有关。
- 建议：分析 30% vs 40% predictor 的纯 KL loss 分量。

**W3** [warning] 训练-推理 gap（soft → hard mask）未被量化讨论

- 具体位置：§3.3、Appendix B
- Per-token evaluation PPL 9.218 vs TEAL global PPL 11.963——30% gap 未讨论。
- 建议：正式讨论此 gap，量化 soft vs hard mask 的分离效应。

**W4** [warning] Qwen-14B MMLU 降幅对论文 framing 影响不足

- 具体位置：§4.5、Table 5、Abstract
- KL MMLU 63.7% vs TEAL/BCE >71%。Abstract 以 "PPL advantage" 领衔，低估了实用场景中 MMLU 的重要性。
- 建议：在 Abstract 中更对等呈现；讨论 KL output-preservation 与 task-specific feature preservation 的 trade-off 机制。

**W5** [warning] Mistral-7B 仅 PPL 无 downstream

- 论文反复强调 "PPL is a poor proxy for reasoning"，但 Mistral 跨架构验证仅有 PPL。
- 建议：至少报告 Mistral 30% 的 MMLU 和 ARC-c。

**W6** [warning] SNR 分析仅覆盖前 300/1000 步

- 非单调性（BCE 在 step 100-250 超过 KL）意味着 KL SNR 优势是 late-training 现象，可能与收敛动态有关而非结构性质。
- 建议：扩展至 1000 步完整 trajectory。

---

## 小问题

- Conclusion 仅一句话
- WikiText-103→WikiText-2 非真正 OOD；C4 仅覆盖 30/50%
- 40% uniform exp_id `d030_kl40_uniform` 前缀暗示可能使用 30% predictor，与 caption 矛盾
- Table 5 Qwen uniform 行缺少 GSM8K 数据未解释
- 引用整体可靠（35/39 verified），4 个 minor mismatch 为作者姓格式差异

---

## Questions to Authors

1. Table 4 中 40% uniform PPL (8.36) 低于 30% uniform PPL (8.82)，请解释。exp_id d030 是否意味着使用了 30% predictor？
2. 是否计划执行 oracle-swap ablation？
3. Qwen-14B MMLU gap 是否在其他 knowledge-intensive task 上也存在？
4. Per-token PPL (9.218) 与 TEAL global PPL (11.963) 的 30% gap 中，soft→hard 和 per-token→global 各贡献多少？

---

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 7 审稿报告

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性 + 完整性 + 写作格式

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**Confidence**: 4/5（熟悉 activation sparsity 和 KL distillation 文献，仔细核实了关键数据）
**一句话总结**: 实验扎实、报告诚实，但技术新颖性有限（已有组件的新问题组合），且核心叙事存在 headline 数字与实际推荐操作点之间的严重张力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 多种子实验+丰富消融，但 BCE 对比存在混淆变量（oracle 质量 vs 训练目标），14B 负面结果削弱泛化 claim |
| Excitement | 2.5/5 | 增量贡献（已知技术组合到新 problem setting），推荐操作点改善幅度有限，无实际推理加速 |
| Overall | 3.0/5 | Findings 级别：实验分析有价值但缺乏足够的技术新颖性或实际影响力进入主会议 |

---

## Summary

本文研究用 forward KL distillation 替代 BCE 训练 SwiGLU LLM 的激活稀疏性预测器。通过梯度分析揭示 BCE 的 per-neuron 训练信号与 TEAL 的 global top-k 推理分配之间存在结构性错配；采用 Gumbel-Sigmoid 松弛实现可微分掩码训练。核心发现包括：KL predictor 使 compensation network 冗余、三个稀疏度操作区间、跨架构 PPL 优势。在 LLaMA-8B、Mistral-7B、Qwen-14B 上验证。

---

## 主要优势

**S1. 诚实透明的实验报告。** 论文坦诚报告负面结果：50% sparsity 下 downstream collapse（MMLU ≈ random, §4.5）、14B 的 MMLU 退化（Table 5, 63.7% vs 71.8%）、PPL 作为 reasoning proxy 的局限性（§4.5, "PPL is a poor proxy for reasoning"）。这种诚实在投稿论文中值得肯定。

**S2. 系统性消融设计。** Table 3 的消融逐一隔离了 KL vs BCE（+16.18 PPL）、Gumbel vs STE（+3.98）、forward vs reverse KL（+1.01）、compensation 冗余性。Loss isolation 实验（BCE+Gumbel+Penalty = PPL 38.02）明确证明 penalty 机制依赖 KL 的全局耦合才能生效。

**S3. 多种子统计和方差报告。** 3-seed 评估覆盖主要 claim（PPL CV < 1%, Appendix E），且发现了 30% global allocation 下 MMLU 的高 seed variance（σ=9.5pp），这本身是一个有价值的发现。

**S4. 写作质量。** 全文无 em-dash、en-dash、禁用词（leverage/delve/utilize 等）。段落结构合理，无明显 AI 写作痕迹。数学推导清晰准确。

**S5. Gradient 分析提供清晰直觉。** Eq. 7-10 的链式法则分解，特别是 factor (b) 中 Jacobian 的跨层耦合机制，为 KL 优于 BCE 提供了可理解的结构性解释（§3.6）。

---

## Must-Fix 问题（影响接收决定）

**N1 [critical] 技术新颖性有限：已有组件的新问题组合**

- 具体位置：§2 Related Work (line 14-18), Table 1
- 问题：论文的核心技术组件——frozen weights + learnable masks + KL training + Gumbel relaxation——全部来自 MaskLLM (Fang et al., 2024)。论文自己承认 "Both share the principle of frozen weights + learnable masks + KL training"（§2, line 15）并将贡献定位为 "primarily empirical"（§2, line 18）。区分点是 N:M static weight sparsity vs dynamic per-token activation sparsity，这是 problem formulation 层面的不同而非方法层面的创新。Table 1 的 taxonomy（2×3, 5/6 cells filled）中填充一个空 cell 构成的新颖性论证较弱。
- 为什么影响接收：EMNLP 主会议对方法新颖性有明确要求。当论文自身定位为 "primarily empirical" 且核心技术全部来自一篇先行工作时，贡献更适合 Findings track 而非主会议。
- 建议修改方向：(1) 更清晰地论证 problem formulation 的新颖性为什么不是 trivial adaptation——dynamic per-token + global budget 带来了哪些 MaskLLM 没有的技术挑战？(2) 强化 structural mismatch 分析的独立价值，使其不仅是 KL 的动机而是一个独立的分析贡献。(3) 考虑重新定位为 empirical analysis paper，将 taxonomy + 三区间分析 + compensation 冗余作为主要贡献。

**N2 [critical] Headline 数字与推荐操作点之间的叙事张力**

- 具体位置：Abstract (line 6: "49%"), Conclusion ("halves TEAL's PPL"), §4.2 (Table 2), §4.5 (Table 4)
- 问题：论文的 headline 数字来自 50% sparsity（"49% PPL reduction", "halves TEAL's PPL"），但论文自身承认这个 regime 下 downstream tasks 全面崩溃（MMLU ≈ 28% = random, GSM8K < 2.2%, §4.5）。推荐操作点是 30% sparsity，此时改善为：PPL 18%, MMLU +2.1pp（uniform vs TEAL）。更关键的是，uniform 30% 在 ARC-c（40.78 vs 42.32）和 GSM8K（7.35 vs 7.88）上实际 *劣于* TEAL vanilla。Abstract 和 Conclusion 以 "49%" 和 "halves" 为卖点，但这些数字来自一个作者自己认为无用的 regime，构成 overclaiming。
- 为什么影响接收：审稿人会立即注意到 headline claim 与实际有效区间的矛盾。当论文自己说 "PPL is a poor proxy" 却以 PPL improvement 为主要卖点时，叙事可信度受损。
- 建议修改方向：(1) Abstract 和 Conclusion 应以 30% 推荐操作点为主叙事，50% 作为 scaling analysis 的一部分而非 headline；(2) 正面讨论 30% uniform 在 ARC-c/GSM8K 上劣于 TEAL 的事实，而非仅突出 MMLU 和 PPL 的优势；(3) 调整 Conclusion（当前仅一句话），增加对不同 regime 结论的平衡讨论。

**N3 [critical] 14B 结果实质性削弱泛化 claim**

- 具体位置：Table 5 (§4.5), Abstract (line 7: "confirms the PPL advantage across 7-14B")
- 问题：Qwen-14B 上 KL 的 MMLU 比 TEAL 低 8.1pp（63.72% vs 71.83%），比 BCE 低 7.95pp（63.72% vs 71.67%）。Uniform allocation 仅恢复 +0.8pp（64.49%），远不够弥合差距。Abstract 称 "confirms the PPL advantage across 7-14B, though 14B reveals a scale-dependent MMLU gap"，将严重的 downstream 退化轻描淡写为 "though" 从句。PPL 优势在 downstream 指标上不仅没有转化为优势，反而严重退化——这不是 "confirms" 什么，而是 disconfirms KL 方法在更大规模上的有效性。
- 为什么影响接收：跨 scale 泛化是论文 contribution C3 的核心声称。14B 的结果表明 KL 的 output-preservation objective 在知识密度更高的模型上可能系统性地 underweight task-specific features，这是一个根本性的方法论局限而非边缘案例。
- 建议修改方向：(1) Abstract 不应用 "confirms" 描述 14B 结果；(2) 正文中增加对 KL 在 14B 失效机制的分析（为什么 PPL 改善但 MMLU 退化？是 KL 优化 distributional 保真度时牺牲了 long-tail knowledge？）；(3) 明确限定 claim 的 scale 范围："PPL advantage at 7-14B, downstream advantage validated only at 7-8B"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] BCE 对比存在混淆变量**

- 具体位置：§4.3 (line 67-68), Limitations (line 7)
- 问题：BCE 使用 magnitude-based oracle targets，KL 直接优化 output distribution。"139% worse PPL" 的对比混淆了两个因素：(a) 训练目标（BCE vs KL）和 (b) 监督信号来源（magnitude oracle vs output distribution）。论文承认 "an ablation using KL-derived masks as BCE targets would isolate the coupling effect"（Limitations），但未执行此消融。
- 建议：这个消融对于区分 "KL 的梯度耦合" vs "KL 的 target 质量" 至关重要，应当执行而非仅在 Limitations 中提及。

**W2 [warning] 无实际推理加速，实用价值不明**

- 具体位置：§4.5 last paragraph, Appendix A
- 问题：KL predictor 增加 6.4% overhead（Table 6），且由于使用 unstructured masks，无法获得 wall-clock speedup（"net acceleration requires kernel-level sparse computation optimizations"）。在 30% 推荐操作点，用户获得 PPL 从 6.12 升到 8.82（44% 退化）加上 6.4% 额外延迟。实用价值取决于未来 sparse kernel 的实现，这不在本文控制范围内。
- 建议：明确讨论在什么条件下（具体的 sparse kernel 加速比）本方法才能在实际部署中提供净收益。30% unstructured sparsity 即使有完美的 sparse kernel 支持，理论加速也有限。

**W3 [warning] Conclusion 过于简短**

- 具体位置：§6 Conclusion
- 问题：Conclusion 仅一句话（"A <1% predictor with KL distillation halves TEAL's PPL across 7-14B; uniform allocation cuts cross-seed σ 7.5×"）。这不符合 EMNLP 论文的常规期望：Conclusion 应包括核心发现总结、局限性承认（虽然有单独 Limitations 节）、和 future directions。一句话 conclusion 也再次以 "halves TEAL's PPL" 为卖点，强化了 N2 中的 overclaiming 问题。
- 建议：扩展为 3-5 句话，涵盖推荐操作点、已知局限（14B gap、no speedup）、和最重要的 open questions。

**W4 [warning] \enlargethispage{8\baselineskip} 页面操纵**

- 具体位置：experiments.tex line 253
- 问题：`\enlargethispage{8\baselineskip}` 在 experiments 末尾将当前页面扩大约 96pt（≈1.3 inches），以便在 8 页限制内容纳全部正文。8 个 baselines 的扩张相当激进，可能被视为 margin manipulation。虽然 LaTeX 技术上允许此操作，但 ACL 格式规范要求不修改页面尺寸。
- 建议：通过压缩正文内容（例如精简 §4.5 的三区间描述，或将 SPON 分析移入 Appendix）来自然适配 8 页，而非通过 \enlargethispage hack。

**W5 [warning] "Structural mismatch" 洞察的新颖性深度**

- 具体位置：§3.6, §1 Introduction
- 问题："End-to-end objective 优于 decomposed objective" 是 knowledge distillation 领域的已知原则（Hinton et al., 2015 → 本文已引用）。将其应用于 sparsity prediction 的具体形式（BCE per-neuron gradient vs KL Jacobian coupling）是合理的形式化，但 Eq. 7-10 的推导本质上是标准链式法则，SNR 测量（5.14× at convergence）提供了经验支撑但未揭示超出 "KL 更好因为它是 end-to-end 的" 之外的新机制。
- 建议：如果想将 gradient analysis 作为独立贡献，需要更深入的分析——例如哪些 layer 的梯度耦合最关键、early vs late layers 的不同行为是否可以指导 layer-specific 训练策略。

---

## 小问题（不影响接收）

- **M1**: Table 2 和 Table 4 内容高度重叠（30% 和 50% 数据在两个表中重复出现），空间效率低。可将 Table 4 作为 Table 2 的扩展（增加 40% 行），节省约 1/4 页。
- **M2**: 39 篇引用处于 EMNLP 的下限（典型 40-60 篇），但覆盖了直接相关方法、baseline、benchmark 和理论基础。可能遗漏的引用方向：quantization + sparsity 组合工作（AWQ 等）、更广泛的 dynamic inference survey。
- **M3**: §4.1 定义 "predictor-TEAL" 术语，但后续正文中 "KL global"、"KL predictor"、"KL uniform" 混用，Table caption 中的命名也不完全一致。建议统一。
- **M4**: Introduction 中 "We provide this analysis."（§1, line 8）作为独立短句略显突兀，可融入上下文。
- **M5**: experiments.tex 中的 `% exp_id: ...` 注释未被清除，虽然不影响编译但会出现在源码审查中。

---

## Questions to Authors

**Q1**: 30% uniform 在 ARC-c（40.78 vs 42.32）和 GSM8K（7.35 vs 7.88）上劣于 TEAL vanilla，为什么仍推荐这个 setting？是否存在一个 allocation strategy 或 sparsity level 能在所有 downstream tasks 上同时优于 TEAL？

**Q2**: 14B 的 MMLU 退化是否可能通过调整 KL 训练的 temperature（当前 T=1）或混合 KL + task-specific loss 来缓解？是否尝试过？

**Q3**: MaskLLM 的 Gumbel-Softmax（categorical）和本文的 Gumbel-Sigmoid（binary）在优化 landscape 上有什么实质区别？为什么不将 MaskLLM 直接适配为 per-token predictor 作为更强的 baseline？

**Q4**: Limitations 中提到的 "ablation using KL-derived masks as BCE targets" 是否已有初步结果？这是区分 coupling effect 和 target quality effect 的关键实验。

---

## Missing References

以下方向的引用可能需要补充：
1. **Quantization + Sparsity 联合优化**: AWQ (Lin et al., 2024), SqueezeLLM (Kim et al., 2024) — 与 activation sparsity 互补的效率方向
2. **Dynamic inference 综述**: 如 Schuster et al. (2022) "Confident Adaptive Language Modeling", Han et al. (2021) "Dynamic Neural Networks: A Survey"
3. **FLAP** (An et al., 2024) — fluctuation-based activation pruning，直接相关
4. **LLM-Pruner** (Ma et al., 2024) — structured pruning with gradient information，方法论上有交集

---

## Overall Assessment

**评分: 3.0 (Findings)**

本文在实验设计和报告质量上表现出色，特别是多种子评估、系统消融、和对负面结果的诚实呈现。compensation 冗余和三操作区间的发现对社区有实际价值。

但三个核心问题阻止了更高评分：(1) 技术新颖性不足——核心方法组件完全来自 MaskLLM，论文自身定位为 primarily empirical；(2) headline 数字来自无效 regime（50% downstream collapse），推荐操作点（30%）的改善幅度有限且在部分 benchmark 上劣于 baseline；(3) 14B 结果实质性削弱了跨 scale 泛化的 claim。

论文适合 Findings track：提供了对 KL distillation 在 activation sparsity prediction 中的系统性实验分析，虽然技术新颖性不足以进入主会议，但实验发现对后续研究有指导价值。

**Confidence: 4/5**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-18T12:31:42.428868+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**Overall**: 3.0 (Findings), Confidence 4/5\n\n### 主要优势\n1. 问题定义清晰且实际相关\n2. Ablation 设计系统全面\n3. 诚实的局限性讨论\n4. Compensation 冗余的实用价值\n5. Training 效率极高\n\n### Must-Fix 问题\n\n**N1** [critical] BCE 与 KL 比较存在多重混淆变量，不能支撑 \"structural mismatch\" 因果 claim\n- KL 与 BCE 的比较存在至少四个同时变化的因素：(1) loss function；(2) oracle 来源（output distribution vs magnitude-based threshold）；(3) mask 类型（Gumbel-Sigmoid 连续 vs hard threshold）；(4) sparsity 控制（adaptive penalty vs oracle 内建 threshold）。论文的 \"loss isolation\" ablation（BCE + Gumbel + Penalty = PPL 38.02）并未清楚隔离 loss 效果。关键缺失实验：(a) BCE trained on KL-derived oracle masks，或 (b) KL with magnitude-based oracle constraints。\n- 影响：当前证据无法区分 \"梯度耦合本身有益\" 和 \"直接优化正确指标有益\" 两种解释。\n\n**N2** [critical] 缺少 intermediate coupling (MSE) baseline 比较\n- Taxonomy 将方法分为 Decomposed/Intermediate/Coupled 三级，但实验只比较两个极端。ShadowLLM 和 D2DMoE（MSE, intermediate）从未作为 baseline。\n\n### Should-Fix 问题\n\n**W1** \"Three operating regions\" 结论基于 3 个数据点，自由度为零\n**W2** 40% uniform PPL (8.36) 低于 30% uniform PPL (8.82) 的反直觉结果未讨论\n**W3** 训练-推理 gap（soft → hard mask）未被量化讨论。Per-token PPL 9.218 vs TEAL global PPL 11.963——30% gap 未讨论\n**W4** Qwen-14B MMLU 降幅对论文 framing 影响不足\n**W5** Mistral-7B 仅 PPL 无 downstream\n**W6** SNR 分析仅覆盖前 300/1000 步，非单调性可能反映收敛动态而非结构性质\n\n### 小问题\n- Conclusion 仅一句话\n- WikiText-103→WikiText-2 非真正 OOD\n- 40% exp_id d030 前缀暗示可能使用错误 predictor\n- Table 5 Qwen uniform 缺 GSM8K 未解释\n\n### Questions\n1. 40% uniform PPL < 30% uniform PPL 的解释？d030 前缀含义？\n2. 是否计划执行 oracle-swap ablation？\n3. Qwen-14B MMLU gap 是否在其他 knowledge-intensive task 上存在？\n4. Per-token PPL (9.218) 与 TEAL global PPL (11.963) 的 gap 中，soft→hard 和 per-token→global 各贡献多少？\n\n---\n\n请对以上每个 Must-Fix (N1, N2)、Should-Fix (W1-W6)、小问题、和 Questions 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**Overall**: 3.0 (Findings), Confidence 4/5\n\n### 主要优势\n1. 问题定义清晰且实际相关\n2. Ablation 设计系统全面\n3. 诚实的局限性讨论\n4. Compensation 冗余的实用价值\n5. Training 效率极高\n\n### Must-Fix 问题\n\n**N1** [critical] BCE 与 KL 比较存在多重混淆变量，不能支撑 \"structural mismatch\" 因果 claim\n- KL 与 BCE 的比较存在至少四个同时变化的因素：(1) loss function；(2) oracle 来源（output distribution vs magnitude-based threshold）；(3) mask 类型（Gumbel-Sigmoid 连续 vs hard threshold）；(4) sparsity 控制（adaptive penalty vs oracle 内建 threshold）。论文的 \"loss isolation\" ablation（BCE + Gumbel + Penalty = PPL 38.02）并未清楚隔离 loss 效果。关键缺失实验：(a) BCE trained on KL-derived oracle masks，或 (b) KL with magnitude-based oracle constraints。\n- 影响：当前证据无法区分 \"梯度耦合本身有益\" 和 \"直接优化正确指标有益\" 两种解释。\n\n**N2** [critical] 缺少 intermediate coupling (MSE) baseline 比较\n- Taxonomy 将方法分为 Decomposed/Intermediate/Coupled 三级，但实验只比较两个极端。ShadowLLM 和 D2DMoE（MSE, intermediate）从未作为 baseline。\n\n### Should-Fix 问题\n\n**W1** \"Three operating regions\" 结论基于 3 个数据点，自由度为零\n**W2** 40% uniform PPL (8.36) 低于 30% uniform PPL (8.82) 的反直觉结果未讨论\n**W3** 训练-推理 gap（soft → hard mask）未被量化讨论。Per-token PPL 9.218 vs TEAL global PPL 11.963——30% gap 未讨论\n**W4** Qwen-14B MMLU 降幅对论文 framing 影响不足\n**W5** Mistral-7B 仅 PPL 无 downstream\n**W6** SNR 分析仅覆盖前 300/1000 步，非单调性可能反映收敛动态而非结构性质\n\n### 小问题\n- Conclusion 仅一句话\n- WikiText-103→WikiText-2 非真正 OOD\n- 40% exp_id d030 前缀暗示可能使用错误 predictor\n- Table 5 Qwen uniform 缺 GSM8K 未解释\n\n### Questions\n1. 40% uniform PPL < 30% uniform PPL 的解释？d030 前缀含义？\n2. 是否计划执行 oracle-swap ablation？\n3. Qwen-14B MMLU gap 是否在其他 knowledge-intensive task 上存在？\n4. Per-token PPL (9.218) 与 TEAL global PPL (11.963) 的 gap 中，soft→hard 和 per-token→global 各贡献多少？\n\n---\n\n请对以上每个 Must-Fix (N1, N2)、Should-Fix (W1-W6)、小问题、和 Questions 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-18T12:31:58.566077+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16137
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-18T12:31:58.767373+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Overall**: 3.0 (Findings), Confidence 4/5\n\n### 主要优势\nS1. 诚实透明的实验报告（负面结果坦诚呈现）\nS2. 系统性消融设计（Table 3 逐一隔离各因素）\nS3. 多种子统计和方差报告\nS4. 写作质量（无 AI 写作痕迹）\nS5. Gradient 分析提供清晰直觉\n\n### Must-Fix 问题\n\n**N1** [critical] 技术新颖性有限：已有组件的新问题组合\n- 核心技术组件（frozen weights + learnable masks + KL training + Gumbel relaxation）全部来自 MaskLLM。区分点是 N:M static weight sparsity vs dynamic per-token activation sparsity——problem formulation 层面的不同而非方法层面的创新。Table 1 taxonomy（2×3, 5/6 cells filled）填充空 cell 的新颖性论证较弱。论文自身定位 \"primarily empirical\"。\n\n**N2** [critical] Headline 数字与推荐操作点之间的叙事张力\n- 50% sparsity 的 \"49% PPL reduction\" 是 headline，但该 regime 下 downstream 全面崩溃。推荐操作点 30% 改善为 PPL 18%, MMLU +2.1pp，且 ARC-c (40.78 vs 42.32) 和 GSM8K (7.35 vs 7.88) 实际劣于 TEAL vanilla。Conclusion 仅一句以 \"halves PPL\" 为卖点——overclaiming。\n\n**N3** [critical] 14B 结果实质性削弱泛化 claim\n- Qwen-14B MMLU 比 TEAL 低 8.1pp，比 BCE 低 7.95pp。Uniform 仅恢复 +0.8pp。Abstract 称 \"confirms the PPL advantage\" 将严重退化轻描淡写。\n\n### Should-Fix 问题\n\n**W1** BCE 对比存在混淆变量（oracle 质量 vs 训练目标）\n**W2** 无实际推理加速（+6.4% overhead, unstructured masks）\n**W3** Conclusion 过于简短（一句话）\n**W4** `\\enlargethispage{8\\baselineskip}` 页面操纵（≈1.3 inches expansion）\n**W5** \"Structural mismatch\" 洞察本质是标准链式法则应用\n\n### 小问题\nM1: Table 2/4 高度重叠\nM2: 39 篇引用处于下限\nM3: 术语不一致\nM4: \"We provide this analysis.\" 突兀\nM5: exp_id 注释未清除\n\n### Questions\nQ1: 30% uniform 在 ARC-c/GSM8K 劣于 TEAL，为何仍推荐？\nQ2: 14B MMLU 退化能否通过 temperature 调整或混合 loss 缓解？\nQ3: MaskLLM Gumbel-Softmax vs 本文 Gumbel-Sigmoid 在优化 landscape 上有什么实质区别？\nQ4: KL-derived masks 作 BCE targets 的 ablation 是否有初步结果？\n\n### Missing References\n1. Quantization + Sparsity（AWQ, SqueezeLLM）\n2. Dynamic inference 综述（Schuster et al., Han et al.）\n3. FLAP（fluctuation-based activation pruning）\n4. LLM-Pruner（structured pruning with gradient）\n\n---\n\n请对以上每个 Must-Fix (N1, N2, N3)、Should-Fix (W1-W5)、小问题 (M1-M5)、Questions (Q1-Q4)、和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Overall**: 3.0 (Findings), Confidence 4/5\n\n### 主要优势\nS1. 诚实透明的实验报告（负面结果坦诚呈现）\nS2. 系统性消融设计（Table 3 逐一隔离各因素）\nS3. 多种子统计和方差报告\nS4. 写作质量（无 AI 写作痕迹）\nS5. Gradient 分析提供清晰直觉\n\n### Must-Fix 问题\n\n**N1** [critical] 技术新颖性有限：已有组件的新问题组合\n- 核心技术组件（frozen weights + learnable masks + KL training + Gumbel relaxation）全部来自 MaskLLM。区分点是 N:M static weight sparsity vs dynamic per-token activation sparsity——problem formulation 层面的不同而非方法层面的创新。Table 1 taxonomy（2×3, 5/6 cells filled）填充空 cell 的新颖性论证较弱。论文自身定位 \"primarily empirical\"。\n\n**N2** [critical] Headline 数字与推荐操作点之间的叙事张力\n- 50% sparsity 的 \"49% PPL reduction\" 是 headline，但该 regime 下 downstream 全面崩溃。推荐操作点 30% 改善为 PPL 18%, MMLU +2.1pp，且 ARC-c (40.78 vs 42.32) 和 GSM8K (7.35 vs 7.88) 实际劣于 TEAL vanilla。Conclusion 仅一句以 \"halves PPL\" 为卖点——overclaiming。\n\n**N3** [critical] 14B 结果实质性削弱泛化 claim\n- Qwen-14B MMLU 比 TEAL 低 8.1pp，比 BCE 低 7.95pp。Uniform 仅恢复 +0.8pp。Abstract 称 \"confirms the PPL advantage\" 将严重退化轻描淡写。\n\n### Should-Fix 问题\n\n**W1** BCE 对比存在混淆变量（oracle 质量 vs 训练目标）\n**W2** 无实际推理加速（+6.4% overhead, unstructured masks）\n**W3** Conclusion 过于简短（一句话）\n**W4** `\\enlargethispage{8\\baselineskip}` 页面操纵（≈1.3 inches expansion）\n**W5** \"Structural mismatch\" 洞察本质是标准链式法则应用\n\n### 小问题\nM1: Table 2/4 高度重叠\nM2: 39 篇引用处于下限\nM3: 术语不一致\nM4: \"We provide this analysis.\" 突兀\nM5: exp_id 注释未清除\n\n### Questions\nQ1: 30% uniform 在 ARC-c/GSM8K 劣于 TEAL，为何仍推荐？\nQ2: 14B MMLU 退化能否通过 temperature 调整或混合 loss 缓解？\nQ3: MaskLLM Gumbel-Softmax vs 本文 Gumbel-Sigmoid 在优化 landscape 上有什么实质区别？\nQ4: KL-derived masks 作 BCE targets 的 ablation 是否有初步结果？\n\n### Missing References\n1. Quantization + Sparsity（AWQ, SqueezeLLM）\n2. Dynamic inference 综述（Schuster et al., Han et al.）\n3. FLAP（fluctuation-based activation pruning）\n4. LLM-Pruner（structured pruning with gradient）\n\n---\n\n请对以上每个 Must-Fix (N1, N2, N3)、Should-Fix (W1-W5)、小问题 (M1-M5)、Questions (Q1-Q4)、和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-18T12:32:00.231209+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1463
}
```

</details>

---


### Assistant

_source line 514 · 2026-05-18T12:32:03.235291+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 48

## Round 48

4 recorded events


### User

_source line 515 · 2026-05-18T12:32:04.423721+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论：Overall 3.0 (Findings)**

核心发现：
- 2 个 Must-Fix：(1) BCE vs KL 比较被 4 个混淆变量污染，无法支撑因果 claim；(2) 缺少 intermediate coupling (MSE) baseline，taxonomy 自建框架未被实验覆盖
- 6 个 Should-Fix：regime analysis 数据点不足、40% PPL 反直觉异常、soft→hard mask gap 未量化、Qwen-14B MMLU framing 不对等、Mistral 无 downstream、SNR 仅 30% 训练步数
- 优势：问题实际相关、ablation 系统、诚实的局限性讨论、compensation 冗余发现有实用价值

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.0 (Findings)**。三个 Must-Fix 问题：

1. **技术新颖性不足** — frozen weights + learnable masks + KL + Gumbel 全部来自 MaskLLM，论文自身承认 "primarily empirical"，填充 2×3 taxonomy 中一个空 cell 不构成充分的新颖性论证。

2. **Headline 数字与推荐操作点的叙事张力** — Abstract/Conclusion 以 "49% PPL reduction" 和 "halves" 为卖点，但这来自 50% sparsity（downstream 全面崩溃）。推荐的 30% 操作点仅 18% PPL 改善，且 uniform allocation 在 ARC-c 和 GSM8K 上实际劣于 TEAL vanilla。

3. **14B 结果削弱泛化 claim** — Qwen-14B 上 KL 的 MMLU 比 TEAL 低 8.1pp，Abstract 用 "confirms...though" 轻描淡写是 overclaiming。

写作格式方面：无 AI 写作痕迹（无 em-dash/en-dash/禁用词），但 Conclusion 仅一句话过于简短，且 `\enlargethispage{8\baselineskip}` 页面操纵值得关注。39 篇引用处于下限但基本覆盖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-18T12:32:51.514204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-18T12:32:51.616432+00:00_

1	issues:
2	  # === Round 1-2 resolved issues (compact) ===
3	  - id: "R2-N1"
4	    summary: "Limitations section 格式不合规"
5	    category: format
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 1
10	    mentions: [{round: 1, reviewers: [1, 2], note: "desk-reject 条件"}]
11	    action_items: [{round: 1, action: "拆为独立 section*", assigned_to: "paper_agent", status: done}]
12	    resolution: "Commit 7018701"
13	    resolution_round: 1
14	
15	  - id: "R2-N2"
16	    summary: "页数超限"
17	    category: format
18	    severity: critical
19	    status: resolved
20	    first_raised_round: 1
21	    last_seen_round: 1
22	    mentions: [{round: 1, reviewers: [1, 2], note: "R2 提出"}]
23	    action_items: [{round: 1, action: "确认页数", assigned_to: "paper_agent", status: done}]
24	    resolution: "8p main + 2p appendix"
25	    resolution_round: 1
26	
27	  - id: "R1-N1"
28	    summary: "缺 OOD PPL 评估"
29	    category: experiment
30	    severity: critical
31	    status: resolved
32	    first_raised_round: 1
33	    last_seen_round: 1
34	    mentions: [{round: 1, reviewers: [1, 2], note: "R1 critical"}]
35	    action_items: [{round: 1, action: "C4 validation PPL", assigned_to: "main_agent", status: done}]
36	    resolution: "C4: Dense=9.21, KL=18.40, TEAL=38.75"
37	    resolution_round: 1
38	
39	  - id: "R1-N2"
40	    summary: "Structural failure 证据不足"
41	    category: method
42	    severity: critical
43	    status: resolved
44	    first_raised_round: 1
45	    last_seen_round: 1
46	    mentions: [{round: 1, reviewers: [1, 2], note: "两位独立指出"}]
47	    action_items: [{round: 1, action: "BCE+Gumbel ×3 LR 对照", assigned_to: "main_agent", status: done}]
48	    resolution: "BCE best=38.02 vs KL=11.79"
49	    resolution_round: 1
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Assistant

_source line 518 · 2026-05-18T12:33:34.448565+00:00_

两位 Reviewer 均给出 3.0 (Findings)，核心关切高度重合。进入 **Step 3 — 收敛判断**。

**收敛分析**：
- **关键共识**: BCE 混淆变量 (R1-N1 ↔ R2-W1)、headline overclaiming (R2-N2 ↔ R1-W4)、14B 泛化削弱 (R2-N3 ↔ R1-W4)、技术新颖性有限 (R2-N1 ↔ R1-N2 taxonomy 未验证)
- **无重大分歧**: 两位评分一致 (3.0)，问题方向一致
- **判断**: 已收敛，无需第二轮。进入 Step 4 汇总报告。

现在同步更新 Issue Tracker 并撰写最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 49

## Round 49

74 recorded events


### User

_source line 519 · 2026-05-18T12:37:54.518910+00:00_

[Reviewer 2 审稿结果]:
已确认关键细节。现在提交对 Reviewer 1 的逐条回应。

---

[飞书用户 曹晓玉 (ou_3336880608784c89d07a6204b6482e8e)]: 继续

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-18T12:38:04.079637+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,get_external_review_status,read_project_file,update_review_issues,submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,get_external_review_status,read_project_file,update_review_issues,submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-18T12:38:04.131221+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-18T12:38:07.154923+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-18T12:38:07.205692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-18T12:38:11.359192+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-18T12:38:11.510214+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-18T12:24:44.805959+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_dbbf8d2c695f1e79e11713aebc107790\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-18T12:38:11.562156+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-18T12:38:12.064807+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (177 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- wallclock_speedup_30_50（准备中）\n- c4_download（准备中）\n- 其他 PREPARING 实验若干\n\n## 近期结论（本轮关键）\n\n### Compensation null result（⚠️ 影响 Claim 1）\n- **kl_comp_50pct_s42_eval** (success): 50% comp = KL-only，5 个指标完全一致（PPL 11.79, ARC 0.3285, WG 0.6346, MMLU 0.2789, GSM8K 0.0129）\n- **kl_comp_30pct_s42_eval** (success): 30% comp = KL-only，全在噪声范围（PPL 8.98 vs 8.98, ARC +0.25pp, WG -1.2pp）\n- **kl_comp_30pct_s123_eval** (success): 与 s42 完全一致（5 指标相同），因共享 base predictor\n- **kl_comp_30pct_s456_eval** (success): 全面优于 s42/s123（ARC +4.7pp, WG +2.5pp），但是底层 predictor 差异，非 comp 效果\n\n### 50% uniform multi-seed\n- **kl50_s456_uniform_eval** (success): PPL 11.95, ARC 0.3831, WG 0.6196, MMLU 0.2750, GSM8K 0.0288\n- 与 s42 uniform 对比：ARC +5.7pp, 其余接近\n\n### 训练完成\n- **kl_comp_30pct_s456** (success): 1000 steps, loss 0.6797\n- **kl_comp_50pct_s42** (success): 1000 steps, loss 1.0703\n\n## 关键发现\n**Compensation 在 30% 和 50% 均为 null result。** 训练 loss 收敛，但对 downstream 指标无任何影响。Director 需决策 Claim 1 framing。\n\n## 趋势\n成功 114 / 负向 19 / 失败 21 / 共 164\n\n## 下一步\n1. Director 决策 Claim 1 framing\n2. 4 卡全部空闲，等指令安排下一批\n3. 候选：wall-clock speedup benchmark、C4 OOD 补充\n\n## 资源状态\nwestd-34887: 0/2 GPU 占用（双卡空闲）\nwestd-417
…[truncated 52 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-18T12:38:17.739159+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-18T12:38:17.789833+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-18T12:38:20.707081+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-18T12:38:21.109101+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-18T12:38:21.260200+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-18T12:38:21.311212+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-18T12:38:24.223392+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-18T12:38:24.525443+00:00_

1	---
2	round: 6
3	overall_score: borderline
4	timestamp: 2026-05-17T10:51:12.070132+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# Round 6 审稿报告 — Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
11	
12	**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)
13	**Deadline**: 2026-05-25
14	**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+相关工作+写作+完整性)
15	**轮次**: Round 1 独立审稿 + 交叉回应，1 轮收敛
16	
17	---
18	
19	## Summary
20	
21	本文分析了 SwiGLU LLM 中 per-neuron BCE 训练与 global top-k 推理之间的结构性不匹配，提出用 forward KL 蒸馏 + Gumbel-Sigmoid 松弛训练轻量级稀疏预测器（75.9M params, <1% base model）。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 从 23.31 降至 11.79（49%），并在 Mistral-7B-v0.3 上验证跨架构一致性。论文同时发现了 global vs uniform allocation 的三个操作区域（budget-surplus / budget-constrained / capacity-limited）。
22	
23	---
24	
25	## Strengths
26	
27	**S1. 梯度结构分析提供清晰的方法动机**（R1-S1, R2-S1 共识）
28	BCE 梯度 per-neuron 独立 vs KL 梯度通过 Jacobian 耦合的形式化分析在数学上正确，SNR 实测（5.77×10⁻⁵ vs 1.00×10⁻⁵，early layers 34-156×）提供了定量支撑。尽管 backprop coupling 是基本性质（R2-N2），但将其 formalize 并指出对 global top-k 的具体后果有增量价值。
29	
30	**S2. 消融实验设计全面且有信息量**（R1-S2, R2-S2 共识）
31	Table 3 清晰隔离了各组件贡献：divergence 方向（Forward/Reverse KL/JSD）、relaxation（Gumbel vs STE，Δ=3.98）、loss isolation（BCE+Gumbel+Penalty=38.02 证明 penalty 与 per-neuron 优化冲突）。Loss effect (6.6×) vs relaxation effect 的分解有信息量。
32	
33	**S3. 三操作区域分析有实用价值**（R1-S3, R2-S3 共识）
34	Non-monotonic allocation preference（uniform@30% → global@40% → irrelevant@50%）是非 trivial 的经验发现，为部署决策提供指导。在两个架构上验证了一致性。
35	
36	**S4. 诚实报告负面结果**（R1-S4）
37	50% downstream 崩溃、penalty 偏差、PPL-downstream 脱节均被坦诚讨论。
38	
39	**S5. 写作质量良好**（R2-S6）
40	无 AI 写作痕迹（em-dash、-ing 短语等）。段落结构紧凑，叙事连贯。格式合规（8 页正文、匿名、Limitations/Ethics/Checklist 齐全）。
41	
42	**S6. 二维 taxonomy 有组织价值**（R2-S5）
43	Correction granularity × Training signal coupling 的分类框架清晰地定位了本文方法。
44	
45	---
46	
47	## Weaknesses
48	
49	### Critical（影响接收决定）
50	
51	**C1. [Critical] "Eliminates the need for compensation" 核心 claim 缺少控制实验**
52	- R2-N3
…[truncated 9976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-18T12:38:24.576105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-18T12:38:24.878495+00:00_

1	issues:
2	  # === Round 1-2 resolved issues (compact) ===
3	  - id: "R2-N1"
4	    summary: "Limitations section 格式不合规"
5	    category: format
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 1
10	    mentions: [{round: 1, reviewers: [1, 2], note: "desk-reject 条件"}]
11	    action_items: [{round: 1, action: "拆为独立 section*", assigned_to: "paper_agent", status: done}]
12	    resolution: "Commit 7018701"
13	    resolution_round: 1
14	
15	  - id: "R2-N2"
16	    summary: "页数超限"
17	    category: format
18	    severity: critical
19	    status: resolved
20	    first_raised_round: 1
21	    last_seen_round: 1
22	    mentions: [{round: 1, reviewers: [1, 2], note: "R2 提出"}]
23	    action_items: [{round: 1, action: "确认页数", assigned_to: "paper_agent", status: done}]
24	    resolution: "8p main + 2p appendix"
25	    resolution_round: 1
26	
27	  - id: "R1-N1"
28	    summary: "缺 OOD PPL 评估"
29	    category: experiment
30	    severity: critical
31	    status: resolved
32	    first_raised_round: 1
33	    last_seen_round: 1
34	    mentions: [{round: 1, reviewers: [1, 2], note: "R1 critical"}]
35	    action_items: [{round: 1, action: "C4 validation PPL", assigned_to: "main_agent", status: done}]
36	    resolution: "C4: Dense=9.21, KL=18.40, TEAL=38.75"
37	    resolution_round: 1
38	
39	  - id: "R1-N2"
40	    summary: "Structural failure 证据不足"
41	    category: method
42	    severity: critical
43	    status: resolved
44	    first_raised_round: 1
45	    last_seen_round: 1
46	    mentions: [{round: 1, reviewers: [1, 2], note: "两位独立指出"}]
47	    action_items: [{round: 1, action: "BCE+Gumbel ×3 LR 对照", assigned_to: "main_agent", status: done}]
48	    resolution: "BCE best=38.02 vs KL=11.79"
49	    resolution_round: 1
50	
51	  - id: "R1-N3"
52	    summary: "消融缺关键维度"
53	    category: experiment
54	    severity: warning
55	    status: resolved
56	    first_raised_round: 1
57	    last_seen_round: 1
58	    mentions: [{round: 1, reviewers: [1, 2], no
…[truncated 30119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-18T12:39:24.764589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/external_review_state.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/external_review_state.json"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-18T12:39:25.266940+00:00_

1	{
2	  "status": "pending",
3	  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
4	  "venue": "EMNLP 2026",
5	  "requested_at": "2026-05-18T12:24:44.805959+00:00",
6	  "reminder_hours": 8,
7	  "chat_id": "oc_dbbf8d2c695f1e79e11713aebc107790"
8	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-18T12:39:25.319204+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && git log --oneline -20",
  "description": "Show recent git commits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && git log --oneline -20",
    "description": "Show recent git commits"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-18T12:39:26.172881+00:00_

180b1e4 [paper] Fix comp convergence appendix: replace inaccurate <5% with absolute loss units
0898abc [paper] Restore comp claim to both 30%+50%, 2-seed for 30%, add convergence appendix
8f3db37 [paper] Downgrade comp claim: 30%-only 2-seed, suspend 50% pending predictor verification
1910c3b [paper] D057 compensation redundancy upgrade: both 30% and 50% identical to KL-only
7231663 [paper] C1 compensation redundancy: KL+Comp no benefit at 30%, page budget fix
d123181 [paper] Update C4 OOD 30% to 2-seed mean±std (16.03±0.01), responding to W4
e8388f6 [paper] Fix 3 reviewer-audit issues: 14B +8.1pp→+5.0pp, intro sparsity context, SNR display precision
71aa753 [paper] Revert σ ratio to 7.5× + add TEAL determinism framing for 9.5pp variance
2e03aa8 [paper] Fix cross-seed σ ratio: 7.5× → 7.3× (9.5/1.3=7.31)
e7e8fc4 [paper] D055 checkpoint consistency: revert MMLU std to 9.5pp (westd-34887 source)
33c22b9 [paper] Fix SNR extended overclaim: acknowledge mid-training BCE>KL crossover
c9b600a [paper] Multi-seed Table 2 + SNR extended analysis (R6-W3)
965bf23 [paper] Fix Conclusion 14B overclaim + update Abstract/Intro to reflect 14B mixed result
23d0f78 [paper] Add 14B uniform allocation results: KL MMLU gap intrinsic to output-preservation objective, not allocation-dependent
4ae121c [paper] Fix 14B narrative dishonesty + table bolding: acknowledge KL MMLU gap, correct bold per sparse-only convention
dd37cbc [paper] Round 6 reviewer fixes: weaken claims, add confound, OOD 30%, sparsity deviation
c15c79a [paper] Fix 14B TEAL PPL misattribution: remove unverified 8.76, keep KL 7.62
17a0fb5 [paper] Upgrade 50% global KL MMLU to 3-seed mean±std (28.1±0.2)
ddbb07c [paper] Fix statistical terminology: variance→standard deviation, CV→σ, 9.46→9.5pp
2aa4924 [paper] Table 2: sync 30% KL MMLU to 3-seed mean±std for Table 5 consistency
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-18T12:39:26.173487+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_reports/round_7*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_reports/round_7*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-18T12:39:26.224043+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-18T12:39:45.354496+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && git diff round_6..HEAD --stat paper/ 2>/dev/null || git diff HEAD~20..HEAD --stat paper/",
  "description": "Show file changes in paper directory since Round 6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && git diff round_6..HEAD --stat paper/ 2>/dev/null || git diff HEAD~20..HEAD --stat paper/",
    "description": "Show file changes in paper directory since Round 6"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-18T12:39:45.856870+00:00_

 paper/abstract.tex     |  10 ++---
 paper/appendix.tex     |  72 ++++++++++++++++++++++++++++-------
 paper/conclusion.tex   |   5 +--
 paper/experiments.tex  | 100 ++++++++++++++++++++++++++++++-------------------
 paper/introduction.tex |  13 ++++---
 paper/limitations.tex  |   6 +--
 paper/main.bbl         |   7 +++-
 paper/method.tex       |  11 +++---
 paper/references.bib   |   8 ++++
 paper/related_work.tex |   4 +-
 10 files changed, 158 insertions(+), 78 deletions(-)
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-18T12:39:45.907701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-18T12:39:45.958365+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-18T12:39:48.919734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-18T12:39:49.422130+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions and achieves higher oracle F1 yet 139\% worse perplexity than a KL-trained predictor.
4	A lightweight predictor ($<$1\% of base parameters) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution, rendering post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
5	On LLaMA-3.1-8B at the recommended 30\% sparsity, KL reduces PPL degradation 18\% over TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$, eliminating seed-dependent instability.
6	At 50\% sparsity, the PPL advantage widens to 49\% but downstream tasks degrade regardless of allocation, revealing allocation-dependent operating regions at 7--8B scale.
7	Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though 14B reveals a scale-dependent MMLU gap not resolved by allocation strategy.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-18T12:39:49.422486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-18T12:39:49.673756+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	We provide this analysis.
9	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of $j$ alone, independent of every other neuron.
10	Under KL divergence, the gradient for neuron $j$ in layer $\ell$ factors as:
11	\begin{equation*}
12	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
13	\end{equation*}
14	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, coupling each neuron's gradient to every other neuron's mask state.
15	This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 139\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preser
…[truncated 1574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-18T12:39:49.775064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-18T12:39:49.776603+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}
…[truncated 16769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-18T12:39:55.656829+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-18T12:39:56.661298+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-2pt}
4	
5	A $<$1\% predictor with KL distillation halves TEAL's PPL across 7--14B; uniform allocation cuts cross-seed $\sigma$ $7.5\times$.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-18T12:39:56.661639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-18T12:39:56.762369+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	Our recommended operating point (30\% sparsity, uniform allocation) is validated at 7--8B scale; at 14B (Qwen-2.5-14B), KL's PPL advantage persists but the MMLU gap relative to TEAL/BCE is not resolved by uniform allocation (+0.8pp vs.\ +5.0pp at 8B), suggesting that KL's output-preservation objective may underweight task-specific features at higher knowledge densities. Scaling to 70B remains untested.
6	Out-of-distribution evaluation (Appendix~\ref{app:ood}) covers 30\% and 50\% sparsity on C4; extending to 70\% is left to future work.
7	Our attribution of KL's advantage to gradient coupling (\S\ref{sec:method:gradient}) is supported by SNR measurements and the BCE isolation ablation, but does not fully disentangle coupling from oracle quality: BCE uses magnitude-based oracles while KL directly optimizes output preservation, and an ablation using KL-derived masks as BCE targets would more precisely isolate the coupling effect.
8	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.
9	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on predict
…[truncated 246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-18T12:39:56.863266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-18T12:39:56.863840+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net ac
…[truncated 12466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-18T12:40:03.141983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-18T12:40:03.192807+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden sta
…[truncated 14198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-18T12:40:03.243570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-18T12:40:03.344385+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
15	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups
…[truncated 2535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-18T12:40:09.831458+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -n \"—\" paper/*.tex | head -20",
  "description": "Check for em-dash AI writing signals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -n \"—\" paper/*.tex | head -20",
    "description": "Check for em-dash AI writing signals"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-18T12:40:10.284723+00:00_

Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-18T12:40:10.837469+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -n \" – \" paper/*.tex | head -20",
  "description": "Check for explanatory en-dash AI writing signals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -n \" – \" paper/*.tex | head -20",
    "description": "Check for explanatory en-dash AI writing signals"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-18T12:40:11.289648+00:00_

Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-18T12:40:11.541035+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -cn \"ing,\" paper/*.tex",
  "description": "Count -ing phrase patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -cn \"ing,\" paper/*.tex",
    "description": "Count -ing phrase patterns"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-18T12:40:11.591744+00:00_

paper/abstract.tex:0
paper/appendix.tex:0
paper/conclusion.tex:0
paper/ethics.tex:1
paper/experiments.tex:0
paper/introduction.tex:0
paper/limitations.tex:0
paper/main.tex:0
paper/method.tex:2
paper/related_work.tex:3
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-18T12:40:15.958903+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && wc -l paper/*.tex && pdfinfo paper/main.pdf 2>/dev/null | grep \"Pages\" || echo \"pdfinfo not available\"",
  "description": "Count lines per file and check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && wc -l paper/*.tex && pdfinfo paper/main.pdf 2>/dev/null | grep \"Pages\" || echo \"pdfinfo not available\"",
    "description": "Count lines per file and check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-18T12:40:16.461246+00:00_

    7 paper/abstract.tex
  235 paper/appendix.tex
    6 paper/conclusion.tex
   43 paper/ethics.tex
  256 paper/experiments.tex
   27 paper/introduction.tex
   10 paper/limitations.tex
   40 paper/main.tex
  193 paper/method.tex
   33 paper/related_work.tex
  850 total
Pages:           14
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-18T12:40:16.612219+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -c \"\\\\\\\\cite\" paper/*.tex",
  "description": "Count citation commands per file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -c \"\\\\\\\\cite\" paper/*.tex",
    "description": "Count citation commands per file"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-18T12:40:16.662898+00:00_

paper/abstract.tex:0
paper/appendix.tex:2
paper/conclusion.tex:0
paper/ethics.tex:2
paper/experiments.tex:13
paper/introduction.tex:5
paper/limitations.tex:0
paper/main.tex:0
paper/method.tex:10
paper/related_work.tex:14
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-18T12:40:23.741928+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-18T12:40:23.792536+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-18T12:40:27.256323+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission guidelines page limits template requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission guidelines page limits template requirements"
  }
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-18T12:40:28.762379+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && git diff HEAD~20..HEAD -- paper/abstract.tex paper/experiments.tex paper/introduction.tex paper/method.tex paper/appendix.tex paper/limitations.tex paper/conclusion.tex",
  "description": "Show detailed diff of paper changes since Round 6",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && git diff HEAD~20..HEAD -- paper/abstract.tex paper/experiments.tex paper/introduction.tex paper/method.tex paper/appendix.tex paper/limitations.tex paper/conclusion.tex",
    "description": "Show detailed diff of paper changes since Round 6",
    "timeout": "30000"
  }
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-18T12:40:34.336597+00:00_

Web search results for query: "EMNLP 2026 ARR submission guidelines page limits template requirements"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here's information about EMNLP 2026 ARR submission guidelines regarding page limits, templates, and requirements:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The submission requirements are the same as first-round review (4-page limit for short papers, 8 pages for long papers).

## Template Requirements

Manuscripts should be submitted electronically, in PDF format and formatted using the templates available here. Please do not modify these style files, nor s
…[truncated 932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7080
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-18T12:40:34.438551+00:00_

&lt;persisted-output>
Output too large (44.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-director-e331551e/a69ef28f-f9be-4f3c-8ba1-eaa1e2152e95/tool-results/bz8ntt3uv.txt

Preview (first 2KB):
diff --git a/paper/abstract.tex b/paper/abstract.tex
index 1ffe2db..d9566d8 100644
--- a/paper/abstract.tex
+++ b/paper/abstract.tex
@@ -1,7 +1,7 @@
 We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
 Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
-Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions, achieving higher oracle F1 yet 137\% worse perplexity than a KL-trained predictor.
-A lightweight predictor ($<$1\% of base parameters) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution.
-At the recommended 30\% sparsity operating point on LLaMA-3.1-8B, KL distillation reduces PPL degradation by 18\% over magnitude-based TEAL; uniform allocation provides $7.5\times$ lower cross-seed downstream variance than global top-$k$, eliminating seed-dependent performance instability.
-At higher sparsity (50\%), PPL advantage widens (49\% over TEAL) but downstream tasks degrade regardless of allocation strategy, revealing allocation-dependent operating regions at the 7--8B scale.
-Cross-architecture evaluation on Mistral-7B-v0.3 confirms consistent improvements (within 8\% ratio at $\leq$50\% sparsity).
+Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions and achieves higher oracle F1 yet 139\% worse perplexity than a KL-trained predictor.
+A lightweight predicto
…[truncated 422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 5676
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-18T12:40:38.254707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-director-e331551e/a69ef28f-f9be-4f3c-8ba1-eaa1e2152e95/tool-results/bz8ntt3uv.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-director-e331551e/a69ef28f-f9be-4f3c-8ba1-eaa1e2152e95/tool-results/bz8ntt3uv.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-18T12:40:38.305616+00:00_

1	diff --git a/paper/abstract.tex b/paper/abstract.tex
2	index 1ffe2db..d9566d8 100644
3	--- a/paper/abstract.tex
4	+++ b/paper/abstract.tex
5	@@ -1,7 +1,7 @@
6	 We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
7	 Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
8	-Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions, achieving higher oracle F1 yet 137\% worse perplexity than a KL-trained predictor.
9	-A lightweight predictor ($<$1\% of base parameters) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution.
10	-At the recommended 30\% sparsity operating point on LLaMA-3.1-8B, KL distillation reduces PPL degradation by 18\% over magnitude-based TEAL; uniform allocation provides $7.5\times$ lower cross-seed downstream variance than global top-$k$, eliminating seed-dependent performance instability.
11	-At higher sparsity (50\%), PPL advantage widens (49\% over TEAL) but downstream tasks degrade regardless of allocation strategy, revealing allocation-dependent operating regions at the 7--8B scale.
12	-Cross-architecture evaluation on Mistral-7B-v0.3 confirms consistent improvements (within 8\% ratio at $\leq$50\% sparsity).
13	+Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions and achieves higher oracle F1 yet 139\% worse perplexity than a KL-trained predictor.
14	+A lightweight predictor ($<$1\% of base parameters) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution, rendering post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
15	+On LLaMA-3.1-8B at the re
…[truncated 16990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-18T12:40:45.083089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-director-e331551e/a69ef28f-f9be-4f3c-8ba1-eaa1e2152e95/tool-results/bz8ntt3uv.txt",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-director-e331551e/a69ef28f-f9be-4f3c-8ba1-eaa1e2152e95/tool-results/bz8ntt3uv.txt",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-18T12:40:45.334877+00:00_

200	@@ -62,9 +63,9 @@ Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
201	 \label{sec:isocompute}
202	 
203	 To test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\times$ the KL step budget, approximately equal wall-clock time: $\sim$46 min BCE vs.\ $\sim$45 min KL on RTX PRO 6000).
204	-The BCE predictor achieves PPL 27.97, still 2.37$\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce_isocompute_s42
205	-The failure is structural, not due to architectural or compute differences: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\ 0.540) with 137\% worse PPL (27.97 vs.\ 11.79). KL's near-random precision (0.51) confirms it learns a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42
206	-Future work could further isolate coupling effects through MSE on hidden states and per-layer KL ablations.
207	+The BCE predictor achieves PPL 28.13$\pm$0.20 (3-seed), still 2.39$\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce50_3seed
208	+The difference is systematic, not due to architectural or compute limitations: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\ 0.540) with 139\% worse PPL (28.13 vs.\ 11.79). KL's near-random precision (0.51) is consistent with learning a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42
209	+Coupled training correlates with better output preservation, but disentangling gradient coupling from oracle quality remains open (BCE uses magnitude oracles while KL optimizes output directly; an ablation using KL-derived masks as BCE targets would isolate the effect).
210	 
211	 
212	 \subsection{Ablation Studies}
213	@@ -98,8 +99,8 @@ BCE + Gumbel + Penalty (no KL) & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangi
214	 Rep
…[truncated 26750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-18T12:42:01.076666+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -c \"\\\\\\\\cite{\" paper/*.tex | awk -F: '{s+=$2} END {print \"Total citation commands:\", s}'",
  "description": "Count total citation commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -c \"\\\\\\\\cite{\" paper/*.tex | awk -F: '{s+=$2} END {print \"Total citation commands:\", s}'",
    "description": "Count total citation commands"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-18T12:42:01.528852+00:00_

Total citation commands: 46
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-18T12:42:01.679874+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -c \"bibitem\" paper/main.bbl",
  "description": "Count references in bbl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && grep -c \"bibitem\" paper/main.bbl",
    "description": "Count references in bbl"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-18T12:42:01.780726+00:00_

39
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-18T12:45:46.987590+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # === Round 1-2 resolved issues (compact) ===\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"desk-reject 条件\"}]\n    action_items: [{round: 1, action: \"拆为独立 section*\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit 7018701\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2 提出\"}]\n    action_items: [{round: 1, action: \"确认页数\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"8p main + 2p appendix\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1 critical\"}]\n    action_items: [{round: 1, action: \"C4 validation PPL\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"C4: Dense=9.21, KL=18.40, TEAL=38.75\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Structural failure 证据不足\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"两位独立指出\"}]\n    action_items: [{round: 1, action: \"BCE+Gumbel ×3 LR 对照\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"BCE best=38.02 vs KL=11.79\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融缺关键维度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"全维度 sweep\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Appendix B-C 全覆盖\"\n    resolution_round: 1\n\n  - id: \"R1-W1-Rd2\"\n    summary: \"Lagrangian 术语误用\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items:\n      - {round: 2, action: \"全文术语替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 2, action: \"启发式 schedule 说明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commits fe7c034 + e00d270\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"λ/sparsity 时序曲线缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"遗留修复\"}]\n    action_items: [{round: 2, action: \"Figure 生成+集成\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"lagrangian_dynamics.pdf in Appendix C\"\n    resolution_round: 2\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"需报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"添加 KL/Dense ratio\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"加 scale qualifier\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"30% MMLU 异常缺 per-layer 分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items: [{round: 2, action: \"Retention 分析+叙事修正\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"Late-layer starvation mechanism (commits f22d330 + 377ed61)\"\n    resolution_round: 2\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"引用偏低\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 7\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W4: 32篇仍偏低(typical 40-60), 遗漏 MiniLLM/GKD 等\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-W4: 遗漏 SparseInfer (DATE 2025) 和 SVD-CSP (arXiv 2026). R1 部分同意.\"}\n      - {round: 7, reviewers: [1, 2], note: \"39 refs, 接近 typical range. SparseInfer + SVD-CSP 已补充.\"}\n    action_items:\n      - {round: 2, action: \"补到 30+\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"补 MiniLLM, GKD, SparseLoRA, Mixture-of-Depths, D2DMoE 至 36\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"补充 SparseInfer (arXiv:2411.12692) 和 SVD-CSP (arXiv:2603.14110) 到 Related Work\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"39 refs. SparseInfer + SVD-CSP 已在 Related Work 讨论.\"\n    resolution_round: 7\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"Em-dash AI 写作信号\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 7\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"降为 info\"}\n      - {round: 6, reviewers: [2], note: \"本轮确认无 AI 写作痕迹 (S6)\"}\n      - {round: 7, reviewers: [1, 2], note: \"grep 确认无 em-dash/en-dash. 写作干净.\"}\n    action_items: [{round: 2, action: \"全文清理\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034. Round 6+7 确认已清理干净.\"\n    resolution_round: 2\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"SNR 缺数学定义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"降为 info\"}]\n    action_items: [{round: 2, action: \"§3.5 加公式\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit cb05c11\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 informal\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W4\"}]\n    action_items: [{round: 1, action: \"弱化+SNR\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Gradient-Based Motivation + SNR 5.76×\"\n    resolution_round: 2\n\n  - id: \"R1-W2\"\n    summary: \"Cross-arch 仅 1 点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W2\"}]\n    action_items: [{round: 1, action: \"6-point table\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Cross-arch 6-point table\"\n    resolution_round: 2\n\n  - id: \"R2-N3\"\n    summary: \"与 SPON 区分度不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"per-token vs static\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2-W5 Round 1\"}]\n    action_items: [{round: 1, action: \"加 caveat\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  # === Round 3-4 issues ===\n\n  - id: \"R3-C1\"\n    summary: \"Responsible NLP Research Checklist + Ethics Statement 缺失\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE. ARR 强制要求。\"}\n      - {round: 4, reviewers: [], note: \"本轮未提及。ethics.tex 已包含 Ethics Statement + 完整 Checklist (A1-E1)。\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及，格式合规已确认。\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 添加 checklist + Ethics Statement\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"ethics.tex 包含完整 Ethics Statement + ARR Responsible NLP Research Checklist\"\n    resolution_round: 4\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect: KL global MMLU≈random, PPL framing 自相矛盾\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE. 最严重问题。\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N2 + R2-N3, 交叉全 AGREE. Narrative vs evidence 矛盾.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W3 + R2-W1, 交叉全 AGREE. 50% 主推区间 downstream 崩溃; 30% 推荐操作点改善温和.\"}\n      - {round: 7, reviewers: [1, 2], note: \"14B 数据加剧此问题: KL PPL=7.62(win) 但 MMLU=63.7 vs TEAL 71.8(lose by 8pp). Abstract 现在更平衡, 但 14B MMLU 反转进一步挑战 output-preservation 目标的实际价值. 降为 warning 因叙事已大幅改善.\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 重写\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"KL+uniform 为推荐配置; Abstract equal prominence; global 作分析对象\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract/Introduction 进一步突出 30% 为推荐操作点\", assigned_to: \"paper_agent\", status: done}\n      - {round: 7, action: \"14B MMLU 反转已诚实报告, 但应讨论 output-preservation objective 的 fundamental limitation\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C3\"\n    summary: \"无 wall-clock speedup, efficiency framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N2, R1-W2. Conclusion 提 wall-clock 与 understanding framing 矛盾.\"}\n      - {round: 6, reviewers: [2], note: \"M4: pipeline adds 6.4% overhead, unstructured masks 不加速.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Appendix A 明确说明 unstructured masks 不加速, Limitations 也有说明. Conclusion 已无 wall-clock claim.\"}\n    action_items:\n      - {round: 3, action: \"D047 reframe: understanding paper\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Conclusion 删除 wall-clock speedup future direction\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Efficiency framing 已修正. Appendix + Limitations 明确无 wall-clock 加速.\"\n    resolution_round: 7\n\n  - id: \"R3-C4\"\n    summary: \"Train-inference mask mismatch 未量化\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE with nuance.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W3, R2 AGREE. Gap decomposition 混合 discretization+allocation.\"}\n      - {round: 7, reviewers: [], note: \"Gap decomposition 保留(53% predictor / 47% allocation). 本轮未 raise.\"}\n    action_items:\n      - {round: 3, action: \"per-token hard eval\", assigned_to: \"main_agent\", status: done}\n      - {round: 4, action: \"Gap decomposition paragraph added\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Gap decomposition 53%/47% 已报告, 满足信息披露要求.\"\n    resolution_round: 7\n\n  - id: \"R3-S1\"\n    summary: \"MaskLLM 技术重叠讨论不足 → 核心新颖性与 MaskLLM 区分不足\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise critical, R1 REBUT → 降 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N1 升 critical, R1 AGREE. 建议重定位为 empirical analysis.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-N1 critical + R1 AGREE with nuance. 共识: 技术新颖性有限.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Contribution 1 改为 'Empirical observation'. Related Work MaskLLM 对比充分. 但核心问题不变: 方法是 Forward KL + Gumbel + Lagrangian 的直接组合, 无方法论创新. 降为 warning 因定位已修正, 但仍影响 Main vs Findings 判断.\"}\n    action_items:\n      - {round: 3, action: \"Related Work 添加 MaskLLM 深度对比\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"重定位为 empirical analysis contribution\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"进一步弱化方法论创新 claim\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S2\"\n    summary: \"BCE 对比是 pipeline 差异非仅 loss 差异 → coupling vs oracle confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N3 critical, R2 REBUT→warning.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W2 Must-Fix, R2 AGREE. coupling vs oracle quality confound.\"}\n      - {round: 7, reviewers: [1, 2], note: \"§4.2 现在明确承认 confound 并提出 KL-derived masks ablation. Limitations 也有讨论. 但仍无实验分离. 因语言修正到位(correlates vs causes), 从 critical 降为 warning.\"}\n    action_items:\n      - {round: 3, action: \"§4.3 明确说明 loss+infrastructure 组合\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"§4.3 添加 future work sentence\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"弱化 coupling 因果 claim 为相关性观察\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S4\"\n    summary: \"仅 7-8B 实验规模\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W5, R2 AGREE. Title 过于宽泛.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W10 Minor. 论文已有 '7-8B scale' qualifier.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Qwen-2.5-14B 数据已加入 (Table 8). Abstract/Intro 覆盖 7-14B. 虽然 14B MMLU 结果 mixed, 但规模覆盖问题已解决.\"}\n    action_items:\n      - {round: 3, action: \"已有 scale qualifiers\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Intro/Conclusion 明确 '7-8B scale tested here'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract 已包含 'at the 7--8B scale'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 7, action: \"14B table + narrative added\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Qwen-2.5-14B added (Table 8). 7-14B 覆盖. Mixed results 诚实报告.\"\n    resolution_round: 7\n\n  - id: \"R3-S5\"\n    summary: \"Regime 分析证据不足 (3 数据点)\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W1 + R2-W3. 每 regime 仅 1 数据点.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-W3: 仍仅 3 采样点(30/40/50%).\"}\n      - {round: 7, reviewers: [1, 2], note: \"措辞已弱化为 'three qualitative behaviors at the sampled sparsity levels'. 正文注明 'Denser sampling would be needed to precisely locate region boundaries'. 降为 info: 作为定性观察已足够, 不再要求额外数据点.\"}\n    action_items:\n      - {round: 3, action: \"降为 empirical observation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Wording changed to 'three operating regions'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"弱化为 'three qualitative behaviors at the sampled sparsity levels'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"措辞已充分弱化, 作为 empirical observation 可接受.\"\n    resolution_round: 7\n\n  - id: \"R3-S6\"\n    summary: \"'Parameter-free' penalty controller + 'converges' 不准确\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W6: 30%/70% λ hit cap ≠ convergence.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W7: 30% target 偏差 5%(实际 28.5%).\"}\n      - {round: 7, reviewers: [1, 2], note: \"Appendix D 现有 28.5% vs TEAL 对比(PPL差<0.3). 术语已修正.\"}\n    action_items:\n      - {round: 3, action: \"删除 parameter-free, 承认 λ_max\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"convergence→'reaches target for 40-50%, saturates at λ_max for 30%/70%'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Appendix D 补 TEAL@28.5% PPL≈10.7 对比讨论\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"术语修正 + 28.5% 影响分析已完成.\"\n    resolution_round: 7\n\n  - id: \"R3-S7\"\n    summary: \"D2DMoE 遗漏 + missing refs (MiniLLM/GKD/SparseLoRA)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"D2DMoE taxonomy 简化; MiniLLM/GKD/SparseLoRA 遗漏\"}\n    action_items:\n      - {round: 3, action: \"引用 + 更新 Table 1\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"D2DMoE added to taxonomy; MiniLLM/GKD/SparseLoRA cited\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"All cited. 39 refs total.\"\n    resolution_round: 7\n\n  - id: \"R3-S8\"\n    summary: \"Abstract PPL-centric 叙事\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"Abstract headline 是 PPL reduction 但 downstream collapse 未 equal prominence.\"}\n      - {round: 6, reviewers: [2], note: \"M1: Abstract 数字密度过高(7+ 个数字).\"}\n      - {round: 7, reviewers: [1, 2], note: \"Abstract 现在以 30% 推荐操作点开头, 加入 14B + MMLU gap. 数字仍较多(~6个)但每个服务于叙事. 较 Round 6 明显改善.\"}\n    action_items:\n      - {round: 3, action: \"精简到 3-4 核心数字\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Abstract rewritten\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract 精简至 ~4 关键数字\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Abstract 叙事平衡, 数字密度可接受.\"\n    resolution_round: 7\n\n  - id: \"R3-S9\"\n    summary: \"Taxonomy 5/9 cells 空, post-hoc 质疑\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 部分 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W2: post-hoc 无 predictive power.\"}\n    action_items:\n      - {round: 3, action: \"补 DejaVu/D2DMoE\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Taxonomy dropped from contribution list; kept as §3.6 organizational framework\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Taxonomy 作为组织框架保留, 不列为 contribution.\"\n    resolution_round: 4\n\n  - id: \"R3-M\"\n    summary: \"11 条 minor (AdamW wd, BCE threshold, ShadowLLM, bib years, GPU, Conclusion 过短等)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"混合来源\"}\n      - {round: 4, reviewers: [1, 2], note: \"部分复发\"}\n      - {round: 6, reviewers: [2], note: \"M2 术语不一致; M5 Table 2 BCE 行标注不清.\"}\n      - {round: 7, reviewers: [1, 2], note: \"术语已统一; Table 2 caption 已明确. 但 Conclusion 现在过短(仅 1 句), 缺 future directions.\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 批量修复\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"SPON year 2026→2025 fixed\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"术语统一; Table 2 BCE caption 明确\", assigned_to: \"paper_agent\", status: done}\n      - {round: 7, action: \"Conclusion 需扩展至 3-5 句(含 future directions)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"6.4% 延迟与效率叙事矛盾\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7 Round 1\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-C3 再次 raise\"}\n      - {round: 4, reviewers: [1, 2], note: \"合并入 R3-C3.\"}\n      - {round: 7, reviewers: [], note: \"已合并入 R3-C3, 该 issue 已 resolved.\"}\n    action_items:\n      - {round: 1, action: \"Reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 3, action: \"understanding paper reframe\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Merged with R3-C3. Efficiency framing 已修正.\"\n    resolution_round: 7\n\n  - id: \"R1-W3\"\n    summary: \"三 seed 统计效力弱 → 主表全部单 seed\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 7\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出, R2 REBUT\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-S3, 升为 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W4, R2 AGREE. Table 2 所有关键对比单 seed.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W5 + R2-W2, 交叉 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"显著改善: Table 2 现有 30% KL global 3-seed(8.96±0.02), 50% KL MMLU 3-seed, BCE 3-seed. 但 30% KL uniform PPL(8.82)仍为单 seed, 30% TEAL/downstream 部分单 seed. 40% 全部单 seed. 从持续 open 改为 in_progress.\"}\n    action_items:\n      - {round: 3, action: \"标注已有 4-seed mean±0.07\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"需 GPU 时间跑 multi-seed\", assigned_to: \"main_agent\", status: done}\n      - {round: 7, action: \"Table 2 多数关键行已有 3-seed. 剩余: 30% KL uniform PPL, 40% 行, 部分 30% downstream.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 4 issues ===\n\n  - id: \"R4-C1\"\n    summary: \"PPL 22.51 幽灵数字: '91% worse PPL' claim 无表格数据支撑\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R1-N1 raise, R2 强 AGREE.\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及. 数据已修正.\"}\n    action_items:\n      - {round: 4, action: \"22.51→27.97 全文替换\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit a7ae77b. 数据溯源链完整.\"\n    resolution_round: 6\n\n  - id: \"R4-W1\"\n    summary: \"d030 exp_id 暗示 regime analysis 使用了错误 sparsity target 的 predictor\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [2], note: \"交叉分享中发现.\"}]\n    action_items:\n      - {round: 4, action: \"确认 d030=batch prefix 非 predictor mismatch\", assigned_to: \"main_agent\", status: done}\n    resolution: \"d030 是 batch 编号前缀, 非 predictor training target.\"\n    resolution_round: 4\n\n  - id: \"R4-W2\"\n    summary: \"Structural mismatch 洞察新颖性: end-to-end > decomposed 是基本原则\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R2-W1, R1 AGREE.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-N2 critical, R1 REBUT→Should-Fix.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Contribution 1 改为 'Empirical observation and quantification'. 措辞到位. 但 §3.6 仍占较大篇幅对基本性质做 formalization, 与 'empirical observation' 定位有张力.\"}\n    action_items:\n      - {round: 4, action: \"Contributions rewritten as empirical validation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Contribution 1 改为 'Empirical observation and quantification'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"Training/eval domain overlap: WikiText-103 训练 + WikiText-2 评测, OOD 仅 50%\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R2-W6. OOD 仅 50% 一个 sparsity.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W8 + R2-W6. 30%(推荐操作点)缺 C4 OOD.\"}\n      - {round: 7, reviewers: [1, 2], note: \"C4 OOD 现覆盖 30%(PPL 16.03±0.01, 2-seed) + 50%(18.40). 推荐操作点已有 OOD 验证.\"}\n    action_items:\n      - {round: 4, action: \"30%/40% C4 OOD eval\", assigned_to: \"main_agent\", status: done}\n      - {round: 6, action: \"C4 OOD 30% PPL=16.05 已写入论文\", assigned_to: \"main_agent+paper_agent\", status: done}\n    resolution: \"C4 OOD 覆盖 30% + 50%. 推荐操作点验证完成.\"\n    resolution_round: 7\n\n  # === Round 6 issues ===\n\n  - id: \"R6-N1\"\n    summary: \"'Eliminates the need for compensation' claim 缺 KL+compensation 控制实验\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R2-N3 raise critical, R1 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"KL+compensation 实验完成: 30% 2-seed(PPL 8.97±0.01 vs 8.96±0.03) + 50%(5 指标完全一致). Compensation Convergence appendix 证明网络已收敛(step 700 plateau). Claim 升级为 'renders compensation redundant at both sparsity levels'. 证据充分.\"}\n    action_items:\n      - {round: 6, action: \"Claim 弱化 + KL+comp 实验\", assigned_to: \"paper_agent+main_agent\", status: done}\n      - {round: 7, action: \"验证完成, claim 恢复为 'renders compensation redundant'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"KL+compensation 实验完成, 两个 sparsity level 均无效. Appendix comp_convergence 证明训练收敛. Claim 有实验支撑.\"\n    resolution_round: 7\n\n  - id: \"R6-W1\"\n    summary: \"Iso-compute 术语误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W1 Must-Fix, R2 REBUT 计算+AGREE 术语.\"}\n      - {round: 7, reviewers: [1, 2], note: \"标题改为 'Extended Training Analysis'. Wall-clock 明确报告(~46 min BCE vs ~45 min KL). 已修复.\"}\n    action_items:\n      - {round: 6, action: \"§4.2 标题改名 + wall-clock 报告\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"标题修正 + wall-clock 数据已报告.\"\n    resolution_round: 7\n\n  - id: \"R6-W2\"\n    summary: \"Near-orthogonal 措辞过强\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W6, R2 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"改为 'weakly correlated ($R^2$=0.038)'. 已修复.\"}\n    action_items:\n      - {round: 6, action: \"'near-orthogonal' → 'weakly correlated'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"措辞已修正.\"\n    resolution_round: 7\n\n  - id: \"R6-W3\"\n    summary: \"SNR 实验统计力度不足\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W4. 80 步无 error bars.\"}\n      - {round: 7, reviewers: [1, 2], note: \"扩展至 300 步(7 checkpoints) + 95% bootstrap CI. 发现 non-monotonic trajectory(BCE mid-training > KL). 统计力度显著提升. 但仍无 BCE training loss curve 排除收敛假说. 降为 info: 主文已有足够 caveats.\"}\n    action_items:\n      - {round: 6, action: \"增加采样至 200+ steps 并报告 95% CI\", assigned_to: \"main_agent+paper_agent\", status: done}\n    resolution: \"300 steps + 95% CI. Non-monotonic trajectory 是有价值的新发现.\"\n    resolution_round: 7\n\n  - id: \"R6-W4\"\n    summary: \"30% target 实际 sparsity 28.5%\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W7, R2 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Appendix D 已有 TEAL@28.5% PPL≈10.7 对比, 差异<0.3 PPL. 影响可忽略.\"}\n    action_items:\n      - {round: 6, action: \"28.5% actual sparsity 标注 + TEAL 对比\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"影响分析完成, <0.3 PPL 差异可忽略.\"\n    resolution_round: 7\n\n  - id: \"R6-W5\"\n    summary: \"Mistral 跨架构 claim 仅 PPL 无 downstream\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R2-W5, R1 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Claim 已弱化为 'preliminary evidence of generality at the 7-8B scale'. Mistral downstream eval 未补, 但措辞已充分限定. 降为 info.\"}\n    action_items:\n      - {round: 6, action: \"'consistent' 弱化为 'preliminary evidence'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Claim 已充分限定.\"\n    resolution_round: 7\n\n  - id: \"R6-W6\"\n    summary: \"Table 2 BCE 行标注不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1], note: \"R1-W9 Minor.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Table 2 caption 已明确: 'BCE follows DejaVu predictor pipeline with FastForward-style compensation network; no TEAL allocation'.\"}\n    action_items:\n      - {round: 6, action: \"Table 2 caption 明确 BCE inference protocol\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Caption 已修正.\"\n    resolution_round: 7\n\n  - id: \"R6-M1\"\n    summary: \"Forward KL 方向选择论证分散\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W11 Minor.\"}\n      - {round: 7, reviewers: [1, 2], note: \"§3.4 加入交叉引用到 §4. 已修复.\"}\n    action_items:\n      - {round: 6, action: \"§3.4 增加交叉引用\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"交叉引用已加.\"\n    resolution_round: 7\n\n  # === Round 7 new issues ===\n\n  - id: \"R7-N1\"\n    summary: \"14B MMLU 反转: KL PPL 最优但 MMLU 输给 TEAL/BCE 8pp, 暴露 output-preservation 目标的根本局限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Table 8: KL PPL 7.62(best) 但 MMLU 63.7% vs TEAL 71.8%(-8.1pp). Uniform 仅恢复 +0.8pp. 这是 8B PPL-downstream disconnect 在更大规模的加剧版本. 论文诚实报告但对 fundamental limitation 的讨论不足.\"}\n    action_items:\n      - {round: 7, action: \"14B 段落应更深入讨论 output-preservation vs task-specific preservation 的 tradeoff, 而非仅归因于 'output-preservation objective may underweight task-specific features'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-W1\"\n    summary: \"Conclusion 过短(1 句), 缺 future directions 和 broader implications\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Conclusion 仅 1 句: 'A <1% predictor with KL distillation halves TEAL PPL across 7-14B; uniform allocation cuts cross-seed σ 7.5×.' 这对于一篇完整论文过于简短. 缺少: 核心 takeaway 的 broader implications, future work directions, 对 PPL-downstream disconnect 的反思.\"}\n    action_items:\n      - {round: 7, action: \"扩展 Conclusion 至 3-5 句: 加 broader implication (PPL vs downstream gap), future work (14B MMLU gap investigation, structured sparsity, task-aware objectives)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-W2\"\n    summary: \"\\\\enlargethispage{8\\\\baselineskip} 暗示页面预算紧张, 审稿人可能注意到格式不正常\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - {round: 7, reviewers: [1], note: \"experiments.tex 第 253 行使用 \\\\enlargethispage{8\\\\baselineskip}. 8 行的页面扩展是显著的, 可能导致实际内容超出 margin 或影响排版. 审稿人可能将其视为隐蔽的超页行为.\"}\n    action_items:\n      - {round: 7, action: \"检查 \\\\enlargethispage 是否导致实际超页; 如果页数仍在 8p 内则可保留, 否则需要精简内容\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-W3\"\n    summary: \"Table 2 多 seed 覆盖不一致: 30% KL global 3-seed 但 30% KL uniform PPL 单 seed\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Table 2 中 30% KL global(8.96±0.02, 3-seed) 和 30% KL uniform PPL(8.82, 单 seed). KL uniform 是推荐配置且 PPL 最优, 反而缺 multi-seed. 审稿人可能质疑 8.82 是否 cherry-picked. 同样 40% 行全部单 seed. 不影响核心 claim 但统计一致性有瑕疵.\"}\n    action_items:\n      - {round: 7, action: \"补 30% KL uniform PPL 3-seed (优先) + 40% 行 multi-seed (如资源允许)\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # === Round 1-2 resolved issues (compact) ===\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"desk-reject 条件\"}]\n    action_items: [{round: 1, action: \"拆为独立 section*\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit 7018701\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2 提出\"}]\n    action_items: [{round: 1, action: \"确认页数\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"8p main + 2p appendix\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1 critical\"}]\n    action_items: [{round: 1, action: \"C4 validation PPL\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"C4: Dense=9.21, KL=18.40, TEAL=38.75\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Structural failure 证据不足\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"两位独立指出\"}]\n    action_items: [{round: 1, action: \"BCE+Gumbel ×3 LR 对照\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"BCE best=38.02 vs KL=11.79\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融缺关键维度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"全维度 sweep\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Appendix B-C 全覆盖\"\n    resolution_round: 1\n\n  - id: \"R1-W1-Rd2\"\n    summary: \"Lagrangian 术语误用\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items:\n      - {round: 2, action: \"全文术语替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 2, action: \"启发式 schedule 说明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commits fe7c034 + e00d270\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"λ/sparsity 时序曲线缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"遗留修复\"}]\n    action_items: [{round: 2, action: \"Figure 生成+集成\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"lagrangian_dynamics.pdf in Appendix C\"\n    resolution_round: 2\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"需报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"添加 KL/Dense ratio\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}]\n    action_items: [{round: 2, action: \"加 scale qualifier\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"30% MMLU 异常缺 per-layer 分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}]\n    action_items: [{round: 2, action: \"Retention 分析+叙事修正\", assigned_to: \"main_agent+paper_agent\", status: done}]\n    resolution: \"Late-layer starvation mechanism (commits f22d330 + 377ed61)\"\n    resolution_round: 2\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"引用偏低\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 7\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W4: 32篇仍偏低(typical 40-60), 遗漏 MiniLLM/GKD 等\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-W4: 遗漏 SparseInfer (DATE 2025) 和 SVD-CSP (arXiv 2026). R1 部分同意.\"}\n      - {round: 7, reviewers: [1, 2], note: \"39 refs, 接近 typical range. SparseInfer + SVD-CSP 已补充.\"}\n    action_items:\n      - {round: 2, action: \"补到 30+\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"补 MiniLLM, GKD, SparseLoRA, Mixture-of-Depths, D2DMoE 至 36\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"补充 SparseInfer (arXiv:2411.12692) 和 SVD-CSP (arXiv:2603.14110) 到 Related Work\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"39 refs. SparseInfer + SVD-CSP 已在 Related Work 讨论.\"\n    resolution_round: 7\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"Em-dash AI 写作信号\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 7\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"降为 info\"}\n      - {round: 6, reviewers: [2], note: \"本轮确认无 AI 写作痕迹 (S6)\"}\n      - {round: 7, reviewers: [1, 2], note: \"grep 确认无 em-dash/en-dash. 写作干净.\"}\n    action_items: [{round: 2, action: \"全文清理\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit fe7c034. Round 6+7 确认已清理干净.\"\n    resolution_round: 2\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"SNR 缺数学定义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions: [{round: 2, reviewers: [1, 2], note: \"降为 info\"}]\n    action_items: [{round: 2, action: \"§3.5 加公式\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Commit cb05c11\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 informal\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W4\"}]\n    action_items: [{round: 1, action: \"弱化+SNR\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Gradient-Based Motivation + SNR 5.76×\"\n    resolution_round: 2\n\n  - id: \"R1-W2\"\n    summary: \"Cross-arch 仅 1 点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R1-W2\"}]\n    action_items: [{round: 1, action: \"6-point table\", assigned_to: \"main_agent\", status: done}]\n    resolution: \"Cross-arch 6-point table\"\n    resolution_round: 2\n\n  - id: \"R2-N3\"\n    summary: \"与 SPON 区分度不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"降 warning\"}]\n    action_items: [{round: 1, action: \"per-token vs static\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions: [{round: 1, reviewers: [1, 2], note: \"R2-W5 Round 1\"}]\n    action_items: [{round: 1, action: \"加 caveat\", assigned_to: \"paper_agent\", status: done}]\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  # === Round 3-4 issues ===\n\n  - id: \"R3-C1\"\n    summary: \"Responsible NLP Research Checklist + Ethics Statement 缺失\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE. ARR 强制要求。\"}\n      - {round: 4, reviewers: [], note: \"本轮未提及。ethics.tex 已包含 Ethics Statement + 完整 Checklist (A1-E1)。\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及，格式合规已确认。\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 添加 checklist + Ethics Statement\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"ethics.tex 包含完整 Ethics Statement + ARR Responsible NLP Research Checklist\"\n    resolution_round: 4\n\n  - id: \"R3-C2\"\n    summary: \"PPL-downstream disconnect: KL global MMLU≈random, PPL framing 自相矛盾\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE. 最严重问题。\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N2 + R2-N3, 交叉全 AGREE. Narrative vs evidence 矛盾.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W3 + R2-W1, 交叉全 AGREE. 50% 主推区间 downstream 崩溃; 30% 推荐操作点改善温和.\"}\n      - {round: 7, reviewers: [1, 2], note: \"14B 数据加剧此问题: KL PPL=7.62(win) 但 MMLU=63.7 vs TEAL 71.8(lose by 8pp). Abstract 现在更平衡, 但 14B MMLU 反转进一步挑战 output-preservation 目标的实际价值. 降为 warning 因叙事已大幅改善.\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 重写\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"KL+uniform 为推荐配置; Abstract equal prominence; global 作分析对象\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract/Introduction 进一步突出 30% 为推荐操作点\", assigned_to: \"paper_agent\", status: done}\n      - {round: 7, action: \"14B MMLU 反转已诚实报告, 但应讨论 output-preservation objective 的 fundamental limitation\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C3\"\n    summary: \"无 wall-clock speedup, efficiency framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise, 交叉强 AGREE.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N2, R1-W2. Conclusion 提 wall-clock 与 understanding framing 矛盾.\"}\n      - {round: 6, reviewers: [2], note: \"M4: pipeline adds 6.4% overhead, unstructured masks 不加速.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Appendix A 明确说明 unstructured masks 不加速, Limitations 也有说明. Conclusion 已无 wall-clock claim.\"}\n    action_items:\n      - {round: 3, action: \"D047 reframe: understanding paper\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Conclusion 删除 wall-clock speedup future direction\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Efficiency framing 已修正. Appendix + Limitations 明确无 wall-clock 加速.\"\n    resolution_round: 7\n\n  - id: \"R3-C4\"\n    summary: \"Train-inference mask mismatch 未量化\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE with nuance.\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W3, R2 AGREE. Gap decomposition 混合 discretization+allocation.\"}\n      - {round: 7, reviewers: [], note: \"Gap decomposition 保留(53% predictor / 47% allocation). 本轮未 raise.\"}\n    action_items:\n      - {round: 3, action: \"per-token hard eval\", assigned_to: \"main_agent\", status: done}\n      - {round: 4, action: \"Gap decomposition paragraph added\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Gap decomposition 53%/47% 已报告, 满足信息披露要求.\"\n    resolution_round: 7\n\n  - id: \"R3-S1\"\n    summary: \"MaskLLM 技术重叠讨论不足 → 核心新颖性与 MaskLLM 区分不足\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise critical, R1 REBUT → 降 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-N1 升 critical, R1 AGREE. 建议重定位为 empirical analysis.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-N1 critical + R1 AGREE with nuance. 共识: 技术新颖性有限.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Contribution 1 改为 'Empirical observation'. Related Work MaskLLM 对比充分. 但核心问题不变: 方法是 Forward KL + Gumbel + Lagrangian 的直接组合, 无方法论创新. 降为 warning 因定位已修正, 但仍影响 Main vs Findings 判断.\"}\n    action_items:\n      - {round: 3, action: \"Related Work 添加 MaskLLM 深度对比\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"重定位为 empirical analysis contribution\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"进一步弱化方法论创新 claim\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S2\"\n    summary: \"BCE 对比是 pipeline 差异非仅 loss 差异 → coupling vs oracle confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-N3 critical, R2 REBUT→warning.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W2 Must-Fix, R2 AGREE. coupling vs oracle quality confound.\"}\n      - {round: 7, reviewers: [1, 2], note: \"§4.2 现在明确承认 confound 并提出 KL-derived masks ablation. Limitations 也有讨论. 但仍无实验分离. 因语言修正到位(correlates vs causes), 从 critical 降为 warning.\"}\n    action_items:\n      - {round: 3, action: \"§4.3 明确说明 loss+infrastructure 组合\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"§4.3 添加 future work sentence\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"弱化 coupling 因果 claim 为相关性观察\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-S4\"\n    summary: \"仅 7-8B 实验规模\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W5, R2 AGREE. Title 过于宽泛.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W10 Minor. 论文已有 '7-8B scale' qualifier.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Qwen-2.5-14B 数据已加入 (Table 8). Abstract/Intro 覆盖 7-14B. 虽然 14B MMLU 结果 mixed, 但规模覆盖问题已解决.\"}\n    action_items:\n      - {round: 3, action: \"已有 scale qualifiers\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Intro/Conclusion 明确 '7-8B scale tested here'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract 已包含 'at the 7--8B scale'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 7, action: \"14B table + narrative added\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Qwen-2.5-14B added (Table 8). 7-14B 覆盖. Mixed results 诚实报告.\"\n    resolution_round: 7\n\n  - id: \"R3-S5\"\n    summary: \"Regime 分析证据不足 (3 数据点)\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W1 + R2-W3. 每 regime 仅 1 数据点.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-W3: 仍仅 3 采样点(30/40/50%).\"}\n      - {round: 7, reviewers: [1, 2], note: \"措辞已弱化为 'three qualitative behaviors at the sampled sparsity levels'. 正文注明 'Denser sampling would be needed to precisely locate region boundaries'. 降为 info: 作为定性观察已足够, 不再要求额外数据点.\"}\n    action_items:\n      - {round: 3, action: \"降为 empirical observation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Wording changed to 'three operating regions'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"弱化为 'three qualitative behaviors at the sampled sparsity levels'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"措辞已充分弱化, 作为 empirical observation 可接受.\"\n    resolution_round: 7\n\n  - id: \"R3-S6\"\n    summary: \"'Parameter-free' penalty controller + 'converges' 不准确\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise, R2 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W6: 30%/70% λ hit cap ≠ convergence.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W7: 30% target 偏差 5%(实际 28.5%).\"}\n      - {round: 7, reviewers: [1, 2], note: \"Appendix D 现有 28.5% vs TEAL 对比(PPL差<0.3). 术语已修正.\"}\n    action_items:\n      - {round: 3, action: \"删除 parameter-free, 承认 λ_max\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"convergence→'reaches target for 40-50%, saturates at λ_max for 30%/70%'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Appendix D 补 TEAL@28.5% PPL≈10.7 对比讨论\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"术语修正 + 28.5% 影响分析已完成.\"\n    resolution_round: 7\n\n  - id: \"R3-S7\"\n    summary: \"D2DMoE 遗漏 + missing refs (MiniLLM/GKD/SparseLoRA)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"D2DMoE taxonomy 简化; MiniLLM/GKD/SparseLoRA 遗漏\"}\n    action_items:\n      - {round: 3, action: \"引用 + 更新 Table 1\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"D2DMoE added to taxonomy; MiniLLM/GKD/SparseLoRA cited\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"All cited. 39 refs total.\"\n    resolution_round: 7\n\n  - id: \"R3-S8\"\n    summary: \"Abstract PPL-centric 叙事\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"Abstract headline 是 PPL reduction 但 downstream collapse 未 equal prominence.\"}\n      - {round: 6, reviewers: [2], note: \"M1: Abstract 数字密度过高(7+ 个数字).\"}\n      - {round: 7, reviewers: [1, 2], note: \"Abstract 现在以 30% 推荐操作点开头, 加入 14B + MMLU gap. 数字仍较多(~6个)但每个服务于叙事. 较 Round 6 明显改善.\"}\n    action_items:\n      - {round: 3, action: \"精简到 3-4 核心数字\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Abstract rewritten\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Abstract 精简至 ~4 关键数字\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Abstract 叙事平衡, 数字密度可接受.\"\n    resolution_round: 7\n\n  - id: \"R3-S9\"\n    summary: \"Taxonomy 5/9 cells 空, post-hoc 质疑\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise, R1 部分 AGREE\"}\n      - {round: 4, reviewers: [1, 2], note: \"R2-W2: post-hoc 无 predictive power.\"}\n    action_items:\n      - {round: 3, action: \"补 DejaVu/D2DMoE\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"Taxonomy dropped from contribution list; kept as §3.6 organizational framework\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Taxonomy 作为组织框架保留, 不列为 contribution.\"\n    resolution_round: 4\n\n  - id: \"R3-M\"\n    summary: \"11 条 minor (AdamW wd, BCE threshold, ShadowLLM, bib years, GPU, Conclusion 过短等)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 7\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"混合来源\"}\n      - {round: 4, reviewers: [1, 2], note: \"部分复发\"}\n      - {round: 6, reviewers: [2], note: \"M2 术语不一致; M5 Table 2 BCE 行标注不清.\"}\n      - {round: 7, reviewers: [1, 2], note: \"术语已统一; Table 2 caption 已明确. 但 Conclusion 现在过短(仅 1 句), 缺 future directions.\"}\n    action_items:\n      - {round: 3, action: \"Paper Agent 批量修复\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"SPON year 2026→2025 fixed\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"术语统一; Table 2 BCE caption 明确\", assigned_to: \"paper_agent\", status: done}\n      - {round: 7, action: \"Conclusion 需扩展至 3-5 句(含 future directions)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"6.4% 延迟与效率叙事矛盾\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7 Round 1\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-C3 再次 raise\"}\n      - {round: 4, reviewers: [1, 2], note: \"合并入 R3-C3.\"}\n      - {round: 7, reviewers: [], note: \"已合并入 R3-C3, 该 issue 已 resolved.\"}\n    action_items:\n      - {round: 1, action: \"Reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 3, action: \"understanding paper reframe\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Merged with R3-C3. Efficiency framing 已修正.\"\n    resolution_round: 7\n\n  - id: \"R1-W3\"\n    summary: \"三 seed 统计效力弱 → 主表全部单 seed\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 7\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出, R2 REBUT\"}\n      - {round: 3, reviewers: [1, 2], note: \"W-S3, 升为 warning\"}\n      - {round: 4, reviewers: [1, 2], note: \"R1-W4, R2 AGREE. Table 2 所有关键对比单 seed.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W5 + R2-W2, 交叉 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"显著改善: Table 2 现有 30% KL global 3-seed(8.96±0.02), 50% KL MMLU 3-seed, BCE 3-seed. 但 30% KL uniform PPL(8.82)仍为单 seed, 30% TEAL/downstream 部分单 seed. 40% 全部单 seed. 从持续 open 改为 in_progress.\"}\n    action_items:\n      - {round: 3, action: \"标注已有 4-seed mean±0.07\", assigned_to: \"paper_agent\", status: done}\n      - {round: 4, action: \"需 GPU 时间跑 multi-seed\", assigned_to: \"main_agent\", status: done}\n      - {round: 7, action: \"Table 2 多数关键行已有 3-seed. 剩余: 30% KL uniform PPL, 40% 行, 部分 30% downstream.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 4 issues ===\n\n  - id: \"R4-C1\"\n    summary: \"PPL 22.51 幽灵数字: '91% worse PPL' claim 无表格数据支撑\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R1-N1 raise, R2 强 AGREE.\"}\n      - {round: 6, reviewers: [], note: \"本轮未提及. 数据已修正.\"}\n    action_items:\n      - {round: 4, action: \"22.51→27.97 全文替换\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit a7ae77b. 数据溯源链完整.\"\n    resolution_round: 6\n\n  - id: \"R4-W1\"\n    summary: \"d030 exp_id 暗示 regime analysis 使用了错误 sparsity target 的 predictor\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions: [{round: 4, reviewers: [2], note: \"交叉分享中发现.\"}]\n    action_items:\n      - {round: 4, action: \"确认 d030=batch prefix 非 predictor mismatch\", assigned_to: \"main_agent\", status: done}\n    resolution: \"d030 是 batch 编号前缀, 非 predictor training target.\"\n    resolution_round: 4\n\n  - id: \"R4-W2\"\n    summary: \"Structural mismatch 洞察新颖性: end-to-end > decomposed 是基本原则\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R2-W1, R1 AGREE.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R2-N2 critical, R1 REBUT→Should-Fix.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Contribution 1 改为 'Empirical observation and quantification'. 措辞到位. 但 §3.6 仍占较大篇幅对基本性质做 formalization, 与 'empirical observation' 定位有张力.\"}\n    action_items:\n      - {round: 4, action: \"Contributions rewritten as empirical validation\", assigned_to: \"paper_agent\", status: done}\n      - {round: 6, action: \"Contribution 1 改为 'Empirical observation and quantification'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"Training/eval domain overlap: WikiText-103 训练 + WikiText-2 评测, OOD 仅 50%\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - {round: 4, reviewers: [1, 2], note: \"R2-W6. OOD 仅 50% 一个 sparsity.\"}\n      - {round: 6, reviewers: [1, 2], note: \"R1-W8 + R2-W6. 30%(推荐操作点)缺 C4 OOD.\"}\n      - {round: 7, reviewers: [1, 2], note: \"C4 OOD 现覆盖 30%(PPL 16.03±0.01, 2-seed) + 50%(18.40). 推荐操作点已有 OOD 验证.\"}\n    action_items:\n      - {round: 4, action: \"30%/40% C4 OOD eval\", assigned_to: \"main_agent\", status: done}\n      - {round: 6, action: \"C4 OOD 30% PPL=16.05 已写入论文\", assigned_to: \"main_agent+paper_agent\", status: done}\n    resolution: \"C4 OOD 覆盖 30% + 50%. 推荐操作点验证完成.\"\n    resolution_round: 7\n\n  # === Round 6 issues ===\n\n  - id: \"R6-N1\"\n    summary: \"'Eliminates the need for compensation' claim 缺 KL+compensation 控制实验\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R2-N3 raise critical, R1 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"KL+compensation 实验完成: 30% 2-seed(PPL 8.97±0.01 vs 8.96±0.03) + 50%(5 指标完全一致). Compensation Convergence appendix 证明网络已收敛(step 700 plateau). Claim 升级为 'renders compensation redundant at both sparsity levels'. 证据充分.\"}\n    action_items:\n      - {round: 6, action: \"Claim 弱化 + KL+comp 实验\", assigned_to: \"paper_agent+main_agent\", status: done}\n      - {round: 7, action: \"验证完成, claim 恢复为 'renders compensation redundant'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"KL+compensation 实验完成, 两个 sparsity level 均无效. Appendix comp_convergence 证明训练收敛. Claim 有实验支撑.\"\n    resolution_round: 7\n\n  - id: \"R6-W1\"\n    summary: \"Iso-compute 术语误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W1 Must-Fix, R2 REBUT 计算+AGREE 术语.\"}\n      - {round: 7, reviewers: [1, 2], note: \"标题改为 'Extended Training Analysis'. Wall-clock 明确报告(~46 min BCE vs ~45 min KL). 已修复.\"}\n    action_items:\n      - {round: 6, action: \"§4.2 标题改名 + wall-clock 报告\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"标题修正 + wall-clock 数据已报告.\"\n    resolution_round: 7\n\n  - id: \"R6-W2\"\n    summary: \"Near-orthogonal 措辞过强\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W6, R2 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"改为 'weakly correlated ($R^2$=0.038)'. 已修复.\"}\n    action_items:\n      - {round: 6, action: \"'near-orthogonal' → 'weakly correlated'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"措辞已修正.\"\n    resolution_round: 7\n\n  - id: \"R6-W3\"\n    summary: \"SNR 实验统计力度不足\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W4. 80 步无 error bars.\"}\n      - {round: 7, reviewers: [1, 2], note: \"扩展至 300 步(7 checkpoints) + 95% bootstrap CI. 发现 non-monotonic trajectory(BCE mid-training > KL). 统计力度显著提升. 但仍无 BCE training loss curve 排除收敛假说. 降为 info: 主文已有足够 caveats.\"}\n    action_items:\n      - {round: 6, action: \"增加采样至 200+ steps 并报告 95% CI\", assigned_to: \"main_agent+paper_agent\", status: done}\n    resolution: \"300 steps + 95% CI. Non-monotonic trajectory 是有价值的新发现.\"\n    resolution_round: 7\n\n  - id: \"R6-W4\"\n    summary: \"30% target 实际 sparsity 28.5%\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W7, R2 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Appendix D 已有 TEAL@28.5% PPL≈10.7 对比, 差异<0.3 PPL. 影响可忽略.\"}\n    action_items:\n      - {round: 6, action: \"28.5% actual sparsity 标注 + TEAL 对比\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"影响分析完成, <0.3 PPL 差异可忽略.\"\n    resolution_round: 7\n\n  - id: \"R6-W5\"\n    summary: \"Mistral 跨架构 claim 仅 PPL 无 downstream\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R2-W5, R1 AGREE.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Claim 已弱化为 'preliminary evidence of generality at the 7-8B scale'. Mistral downstream eval 未补, 但措辞已充分限定. 降为 info.\"}\n    action_items:\n      - {round: 6, action: \"'consistent' 弱化为 'preliminary evidence'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Claim 已充分限定.\"\n    resolution_round: 7\n\n  - id: \"R6-W6\"\n    summary: \"Table 2 BCE 行标注不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1], note: \"R1-W9 Minor.\"}\n      - {round: 7, reviewers: [1, 2], note: \"Table 2 caption 已明确: 'BCE follows DejaVu predictor pipeline with FastForward-style compensation network; no TEAL allocation'.\"}\n    action_items:\n      - {round: 6, action: \"Table 2 caption 明确 BCE inference protocol\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Caption 已修正.\"\n    resolution_round: 7\n\n  - id: \"R6-M1\"\n    summary: \"Forward KL 方向选择论证分散\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - {round: 6, reviewers: [1, 2], note: \"R1-W11 Minor.\"}\n      - {round: 7, reviewers: [1, 2], note: \"§3.4 加入交叉引用到 §4. 已修复.\"}\n    action_items:\n      - {round: 6, action: \"§3.4 增加交叉引用\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"交叉引用已加.\"\n    resolution_round: 7\n\n  # === Round 7 new issues ===\n\n  - id: \"R7-N1\"\n    summary: \"14B MMLU 反转: KL PPL 最优但 MMLU 输给 TEAL/BCE 8pp, 暴露 output-preservation 目标的根本局限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Table 8: KL PPL 7.62(best) 但 MMLU 63.7% vs TEAL 71.8%(-8.1pp). Uniform 仅恢复 +0.8pp. 这是 8B PPL-downstream disconnect 在更大规模的加剧版本. 论文诚实报告但对 fundamental limitation 的讨论不足.\"}\n    action_items:\n      - {round: 7, action: \"14B 段落应更深入讨论 output-preservation vs task-specific preservation 的 tradeoff, 而非仅归因于 'output-preservation objective may underweight task-specific features'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-W1\"\n    summary: \"Conclusion 过短(1 句), 缺 future directions 和 broader implications\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Conclusion 仅 1 句: 'A <1% predictor with KL distillation halves TEAL PPL across 7-14B; uniform allocation cuts cross-seed σ 7.5×.' 这对于一篇完整论文过于简短. 缺少: 核心 takeaway 的 broader implications, future work directions, 对 PPL-downstream disconnect 的反思.\"}\n    action_items:\n      - {round: 7, action: \"扩展 Conclusion 至 3-5 句: 加 broader implication (PPL vs downstream gap), future work (14B MMLU gap investigation, structured sparsity, task-aware objectives)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-W2\"\n    summary: \"\\\\enlargethispage{8\\\\baselineskip} 暗示页面预算紧张, 审稿人可能注意到格式不正常\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - {round: 7, reviewers: [1], note: \"experiments.tex 第 253 行使用 \\\\enlargethispage{8\\\\baselineskip}. 8 行的页面扩展是显著的, 可能导致实际内容超出 margin 或影响排版. 审稿人可能将其视为隐蔽的超页行为.\"}\n    action_items:\n      - {round: 7, action: \"检查 \\\\enlargethispage 是否导致实际超页; 如果页数仍在 8p 内则可保留, 否则需要精简内容\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R7-W3\"\n    summary: \"Table 2 多 seed 覆盖不一致: 30% KL global 3-seed 但 30% KL uniform PPL 单 seed\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - {round: 7, reviewers: [1, 2], note: \"Table 2 中 30% KL global(8.96±0.02, 3-seed) 和 30% KL uniform PPL(8.82, 单 seed). KL uniform 是推荐配置且 PPL 最优, 反而缺 multi-seed. 审稿人可能质疑 8.82 是否 cherry-picked. 同样 40% 行全部单 seed. 不影响核心 claim 但统计一致性有瑕疵.\"}\n    action_items:\n      - {round: 7, action: \"补 30% KL uniform PPL 3-seed (优先) + 40% 行 multi-seed (如资源允许)\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-18T12:45:47.089237+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 32179}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-18T12:47:57.978319+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 7 审稿报告（Continue 模式）— Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+相关工作+写作+完整性)\n**轮次**: Round 7 (Continue from Round 6), 修订评估\n\n---\n\n## Summary of Changes Since Round 6\n\n本轮有 20+ commits 的实质性修改，响应了 Round 6 报告中的绝大多数 issue：\n\n1. **Compensation redundancy 实验**（C1 resolved）：KL+compensation 在 30%（2-seed, PPL 8.97±0.01 vs KL-only 8.96±0.03）和 50%（5 指标完全一致）均无效。新增 Appendix 证明 compensation 网络已收敛（step 700 plateau）。Claim 升级为 \"renders compensation redundant at both tested sparsity levels\"，有实验支撑。\n\n2. **Multi-seed 大幅扩展**（W2 substantially improved）：Table 2 现有 30% KL global 3-seed（8.96±0.02）、50% KL MMLU 3-seed（28.1±0.2）、BCE 3-seed（28.13±0.20）。但 30% KL uniform PPL（8.82, 推荐配置）仍为单 seed。\n\n3. **14B 跨规模验证**（新增）：Qwen-2.5-14B 数据（Table 8）。KL PPL 优势保持（7.62 vs TEAL 8.73），但 MMLU 低于 TEAL/BCE 8pp（63.7 vs 71.8%）。诚实报告为 \"scale-dependent MMLU gap\"。\n\n4. **SNR 扩展分析**（W8 resolved）：从 80 步扩展至 300 步（7 checkpoints），加入 95% bootstrap CI。发现 non-monotonic trajectory（BCE mid-training > KL），是有信息量的新发现。\n\n5. **OOD 30%**（W4 resolved）：C4 PPL 16.03±0.01（2-seed），推荐操作点 OOD 验证完成。\n\n6. **Claim 校准**：near-orthogonal → weakly correlated; Iso-compute → Extended Training Analysis; Contribution 1 → \"Empirical observation\"; coupling 因果 → 相关性; cross-arch \"consistent\" → \"preliminary evidence\"。\n\n7. **新增 appendix**：Extended SNR Analysis、Extended Downstream Evaluation（HellaSwag/PIQA/BoolQ）、Compensation Training Convergence。\n\n---\n\n## Round 6 Issue Disposition\n\n### Resolved (10 issues)\n\n| Issue | Round 6 状态 | 修复评估 |\n|-------|-------------|---------|\n| C1: Compensation claim 缺实验 | Critical | **Resolved**. KL+comp 实验完成, 两个 sparsity 均无效, 附 convergence 证据 |\n| W3: Iso-compute 术语 | Warning | **Resolved**. 标题改名 + wall-clock 数据 |\n| W4: OOD 仅 50% | Warning | **Resolved**. 30% C4 PPL 16.03±0.01 (2-seed) |\n| W5: 三区域采样不足 | Warning | **Resolved**. 措辞弱化为 \"qualitative behaviors at sampled levels\" + caveat |\n| W6: Missing refs | Warning | **Resolved**. SparseInfer + SVD-CSP 已补 (39 refs total) |\n| W7: Mistral 缺 downstream | Warning | **Resolved**. Claim 弱化为 \"preliminary evidence\" |\n| W8: SNR 统计 | Warning | **Resolved**. 300 steps + 95% CI + non-monotonic 发现 |\n| W9: near-orthogonal | Warning | **Resolved**. weakly correlated ($R^2$=0.038) |\n| W10: 28.5% 偏差 | Warning | **Resolved**. TEAL@28.5% 对比, <0.3 PPL 差异 |\n| M4: Forward KL 论证分散 | Minor | **Resolved**. 交叉引用已加 |\n\n### Partially Addressed (3 issues, 降级)\n\n| Issue | Round 6 状态 | 本轮评估 | 新状态 |\n|-------|-------------|---------|--------|\n| C2: 技术新颖性有限 | Critical | Contribution 1 改为 \"Empirical observation\", MaskLLM 对比充分. 但方法本身（KL+Gumbel+Lagrangian 组合）未变. **定位修正到位, 核心局限不变.** | Warning (降级: framing 已改善) |\n| C3: Coupling vs oracle confound | Critical | §4.2 明确承认 confound, Limitations 讨论, 语言改为 \"correlates with\" 而非 \"causes\". **但仍无实验分离.** | Warning (降级: 坦诚承认+语言校正) |\n| W1: PPL-downstream disconnect | Warning | Abstract 更平衡, 30% 为推荐操作点. 但 14B 数据加剧此问题（KL PPL best 但 MMLU 输 8pp）. | Warning (持续) |\n\n### Insufficient Progress (1 issue)\n\n| Issue | Round 6 状态 | 本轮评估 |\n|-------|-------------|---------|\n| W2: Multi-seed 不完整 | Warning | 显著改善但推荐配置（30% uniform PPL 8.82）仍为单 seed |\n\n---\n\n## New Issues This Round\n\n**R7-N1. [Warning] 14B MMLU 反转暴露 output-preservation 目标的根本局限**\n- Table 8: KL PPL=7.62（best）但 MMLU=63.7% vs TEAL 71.8%（-8.1pp）。Uniform 仅恢复 +0.8pp。\n- 这不是简单的 allocation 问题：KL 的 output-preservation 目标在更高 knowledge density 模型上系统性地 underweight task-specific features。\n- 论文诚实报告（\"gap appears intrinsic to KL's output-preservation objective\"），但讨论过于简短。\n- 8B 的 PPL-downstream disconnect（W1）在 14B 被放大为 PPL-MMLU 反转，构成对 KL distillation 方法论的根本质疑。\n- **要求**：14B 段落应更深入讨论 output-preservation vs task-specific preservation 的 tradeoff。\n\n**R7-W1. [Warning] Conclusion 过短**\n- 仅 1 句话（\"A <1% predictor with KL distillation halves TEAL's PPL across 7-14B; uniform allocation cuts cross-seed σ 7.5×.\"），缺 future directions 和 broader implications。\n- 对于一篇完整论文，Conclusion 应至少 3-5 句：核心发现总结 + PPL-downstream disconnect 的反思 + 14B 发现的 implications + future work。\n\n**R7-W2. [Info] `\\enlargethispage{8\\baselineskip}` 格式 hack**\n- experiments.tex 第 253 行。8 行的扩展幅度较大。需确认未导致实际超页。\n\n**R7-W3. [Info] Multi-seed 覆盖不一致**\n- 推荐配置（30% KL uniform, PPL 8.82）是单 seed，而非推荐配置（30% KL global）反而有 3-seed。统计一致性有瑕疵。\n\n---\n\n## Strengths (本轮新增/强化)\n\n**S1. Compensation redundancy 证据链完整**（本轮新增）\nKL+compensation 实验 + convergence 证明 + 两个 sparsity level 交叉验证。这是本轮最重要的贡献：论文从 \"未验证的 claim\" 变为 \"有实验支撑的发现\"。\n\n**S2. 14B 跨规模验证的诚实报告**（本轮新增）\n多数论文会隐藏 mixed results；本文不仅报告 KL PPL 优势，还坦诚展示 MMLU gap 和 uniform 无法修复的事实。这增加了论文的可信度。\n\n**S3. SNR 扩展分析发现 non-monotonic trajectory**（本轮新增）\nBCE mid-training SNR > KL 是一个非 trivial 的发现，提供了新的 mechanistic insight。95% CI 增加了统计可信度。\n\n**S4. 消融设计全面且有信息量**（持续）\nTable 3 的 loss isolation 设计（特别是 BCE+Gumbel+Penalty=38.02 > vanilla BCE=27.97）仍然是论文最强的部分。\n\n**S5. 写作质量良好**（持续）\n无 AI 写作痕迹（grep 确认无 em-dash/en-dash）。Claims 校准到位（correlates, preliminary evidence, qualitative behaviors）。格式合规（8p main, [review] option, anonymous, Limitations/Ethics/Checklist）。\n\n---\n\n## Weaknesses (综合排序)\n\n### Warning (影响评分但不一票否决)\n\n**W1. 技术新颖性有限（持续 5 轮）**\n- 核心方法是 Forward KL (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + Adaptive Penalty（标准约束优化）的组合。MaskLLM 已使用相同原则。\n- 论文已正确重定位为 \"empirical analysis / mechanistic understanding\"，但 Contribution 1 的 gradient formalization 仍然是对 backpropagation 基本性质的重述。\n- 影响：更适合 Findings 而非 Main Conference。\n\n**W2. Coupling vs oracle confound 无实验分离（持续 5 轮）**\n- BCE 使用 magnitude oracles，KL 直接优化 output distribution。观察到的差距可能源于 oracle quality 而非 gradient coupling。\n- 论文现在坦诚承认（§4.2 + Limitations），语言校正为 \"correlates with\"。但 7 轮审稿仍未提供 KL-derived masks → BCE 的控制实验。\n- 影响：gradient analysis（Contribution 1）的因果解释力被削弱。\n\n**W3. PPL-downstream disconnect + 14B MMLU 反转（持续 5 轮 + 新加剧）**\n- 8B: 50% downstream 崩溃；30% MMLU +2pp（温和）。\n- 14B: KL PPL 最优但 MMLU 输 TEAL 8pp，uniform 仅 +0.8pp。\n- 这不是 presentation 问题（叙事已大幅改善），而是方法论的 fundamental limitation：output-distribution preservation ≠ task-relevant preservation。14B 数据表明此 gap 随规模扩大。\n- 影响：削弱 KL distillation 作为通用方法的 claim。\n\n**W4. Multi-seed 覆盖仍不完整（持续 7 轮）**\n- 推荐配置（30% KL uniform, PPL 8.82）仍为单 seed。Table 5 的 40% 行全部单 seed。\n- 较 Round 6 有显著改善（Table 2 多数关键行已有 3-seed），但统计一致性仍有瑕疵。\n\n**W5. Conclusion 过短**\n- 1 句话的 Conclusion 不足以承载 14 页论文的 takeaway。审稿人可能认为草率。\n\n---\n\n## Questions (需作者回应)\n\n**Q1.** 14B MMLU gap（KL 63.7 vs TEAL 71.8）的机制是什么？论文说 \"intrinsic to output-preservation objective\"，但 output preservation 和 task performance 之间的解耦为何在 14B 比 8B 更严重？是否与 Qwen-2.5-14B 的 knowledge density 或 SwiGLU gate distribution 有关？\n\n**Q2.** 30% KL uniform（推荐配置）的 PPL 8.82 为何缺 multi-seed？如果这是最终推荐配置，单 seed 的可靠性如何保证？\n\n**Q3.** BCE mid-training SNR > KL 的 non-monotonic 现象是否有更深层的解释？论文的 \"KL coupling becomes effective after coarse mask learning\" 假说是否可以通过 mask entropy trajectory 验证？\n\n---\n\n## Overall Assessment\n\n**评分: 3.0/5 — Findings**\n**置信度: High (4/5)**\n\n### 与 Round 6 的评分变化\n\nRound 6: 2.5 (Borderline Findings) → Round 7: 3.0 (Findings)\n\n**提升 0.5 分的原因：**\n1. Compensation redundancy 实验补齐了 Round 6 最大的 gap（C1），从 \"未验证 claim\" 变为 \"有实验支撑的发现\"\n2. 14B 跨规模数据，虽然 mixed，但增加了论文的深度和诚实度\n3. Multi-seed 覆盖大幅改善，Table 2 多数关键行有 3-seed\n4. SNR 扩展分析（300 steps + 95% CI + non-monotonic 发现）提供了新的 mechanistic insight\n5. Claims 校准全面到位，写作质量持续良好\n\n**不升至 3.5 的原因：**\n1. 技术新颖性有限——已有组件的直接组合，持续 5 轮未改变\n2. Coupling vs oracle confound 无实验分离——7 轮审稿后仍仅有语言修正\n3. 14B MMLU 反转加剧了 PPL-downstream disconnect，暗示 output-preservation 目标的 fundamental limitation\n4. Multi-seed 覆盖仍有盲区（推荐配置单 seed）\n\n### 定位建议\n\n论文作为 **EMNLP 2026 Findings** 论文是合适的：\n- **实验工作高于 Findings 平均水平**：消融设计全面（Table 3）、跨架构验证（LLaMA/Mistral/Qwen）、negative results 诚实报告、三区域分析有实用价值\n- **方法论贡献不足 Main Conference**：技术为已有组件组合，理论分析是 backprop 基本性质的形式化\n- **最有价值的贡献是 empirical insights**：compensation redundancy、PPL-downstream disconnect 的量化、allocation-dependent operating regions、14B scale-dependent effects\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- 叙事较 Round 6 显著改善：以 30% 推荐操作点开头，14B + MMLU gap 诚实披露\n- 仍有 ~6 个数字（139%, 18%, 7.5×, 49%, 7-14B），但每个服务于叙事，可接受\n- \"rendering post-hoc compensation redundant at both 30% and 50% sparsity\" 现在有实验支撑\n\n### Introduction\n- Contribution 1 \"Empirical observation and quantification\" 比之前的 \"Identification\" 更准确\n- Contribution 2 compensation redundancy claim 有实验支撑\n- Contribution 3 \"allocation-to-downstream interactions at 7-14B\" 准确反映了 mixed results\n\n### Method (§3)\n- 数学表述正确\n- §3.6 Gradient-Based Motivation：SNR 扩展分析（300 steps, non-monotonic trajectory）增加了信息量\n- Taxonomy (Table 1) 作为组织框架有价值\n\n### Experiments (§4)\n- §4.2 Extended Training Analysis（改名 ✓）：wall-clock 对比 ✓；confound acknowledgment ✓\n- §4.3 消融：Compensation Redundancy 段落是本轮最有价值的新增内容\n- §4.4 Regime Analysis：措辞弱化到位\n- §4.5 SPON：weakly correlated ✓\n- §4.6 Cross-arch + 14B：Mistral preliminary evidence ✓；14B 诚实但讨论偏短\n- Inference Efficiency + Training Stability 段落被削减/移入 appendix，正文更紧凑\n\n### Conclusion\n- 过短（1 句）。需要扩展。\n\n### Limitations\n- 全面：PPL as proxy、per-target training、14B MMLU gap、OOD coverage、coupling vs oracle confound、seed variance、no wall-clock speedup。\n- 14B limitation 讨论比 §4.6 更深入（\"output-preservation objective may underweight task-specific features at higher knowledge densities\"），建议将这一讨论也整合到正文。\n\n### Appendix\n- 内容扎实且信息密度高\n- 新增 SNR Extended、Extended Downstream、Compensation Convergence 三个 appendix，均有价值\n- Extended Downstream (HellaSwag/PIQA/BoolQ) 提供了 30% 操作点的正面证据\n\n### Format Compliance\n- 14 页 PDF（8p main + appendix + refs + limitations/ethics）\n- `[review]` option ✓, anonymous ✓, line numbers expected (需确认)\n- `\\enlargethispage{8\\baselineskip}` 需要检查是否导致实际超页\n- 39 references，接近 typical range\n\n---\n\n## Issue Tracker 同步\n\n本轮 resolved 10 个 Round 6 issues，降级 3 个 Critical→Warning，新增 4 个 issues（1 Warning + 1 Warning + 2 Info）。\n\n**跨轮持续未解决的核心问题：**\n- 技术新颖性（R3-S1）：持续 5 轮，已从 Critical 降为 Warning\n- Coupling vs oracle confound（R3-S2）：持续 5 轮，已从 Critical 降为 Warning\n- PPL-downstream disconnect（R3-C2）：持续 5 轮，Warning\n- Multi-seed 不完整（R1-W3）：持续 7 轮，in_progress\n\n**新增 issues：**\n- R7-N1: 14B MMLU 反转（Warning）\n- R7-W1: Conclusion 过短（Warning）\n- R7-W2: enlargethispage 格式（Info）\n- R7-W3: Multi-seed 覆盖不一致（Info）",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 7 审稿报告（Continue 模式）— Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+相关工作+写作+完整性)\n**轮次**: Round 7 (Continue from Round 6), 修订评估\n\n---\n\n## Summary of Changes Since Round 6\n\n本轮有 20+ commits 的实质性修改，响应了 Round 6 报告中的绝大多数 issue：\n\n1. **Compensation redundancy 实验**（C1 resolved）：KL+compensation 在 30%（2-seed, PPL 8.97±0.01 vs KL-only 8.96±0.03）和 50%（5 指标完全一致）均无效。新增 Appendix 证明 compensation 网络已收敛（step 700 plateau）。Claim 升级为 \"renders compensation redundant at both tested sparsity levels\"，有实验支撑。\n\n2. **Multi-seed 大幅扩展**（W2 substantially improved）：Table 2 现有 30% KL global 3-seed（8.96±0.02）、50% KL MMLU 3-seed（28.1±0.2）、BCE 3-seed（28.13±0.20）。但 30% KL uniform PPL（8.82, 推荐配置）仍为单 seed。\n\n3. **14B 跨规模验证**（新增）：Qwen-2.5-14B 数据（Table 8）。KL PPL 优势保持（7.62 vs TEAL 8.73），但 MMLU 低于 TEAL/BCE 8pp（63.7 vs 71.8%）。诚实报告为 \"scale-dependent MMLU gap\"。\n\n4. **SNR 扩展分析**（W8 resolved）：从 80 步扩展至 300 步（7 checkpoints），加入 95% bootstrap CI。发现 non-monotonic trajectory（BCE mid-training > KL），是有信息量的新发现。\n\n5. **OOD 30%**（W4 resolved）：C4 PPL 16.03±0.01（2-seed），推荐操作点 OOD 验证完成。\n\n6. **Claim 校准**：near-orthogonal → weakly correlated; Iso-compute → Extended Training Analysis; Contribution 1 → \"Empirical observation\"; coupling 因果 → 相关性; cross-arch \"consistent\" → \"preliminary evidence\"。\n\n7. **新增 appendix**：Extended SNR Analysis、Extended Downstream Evaluation（HellaSwag/PIQA/BoolQ）、Compensation Training Convergence。\n\n---\n\n## Round 6 Issue Disposition\n\n### Resolved (10 issues)\n\n| Issue | Round 6 状态 | 修复评估 |\n|-------|-------------|---------|\n| C1: Compensation claim 缺实验 | Critical | **Resolved**. KL+comp 实验完成, 两个 sparsity 均无效, 附 convergence 证据 |\n| W3: Iso-compute 术语 | Warning | **Resolved**. 标题改名 + wall-clock 数据 |\n| W4: OOD 仅 50% | Warning | **Resolved**. 30% C4 PPL 16.03±0.01 (2-seed) |\n| W5: 三区域采样不足 | Warning | **Resolved**. 措辞弱化为 \"qualitative behaviors at sampled levels\" + caveat |\n| W6: Missing refs | Warning | **Resolved**. SparseInfer + SVD-CSP 已补 (39 refs total) |\n| W7: Mistral 缺 downstream | Warning | **Resolved**. Claim 弱化为 \"preliminary evidence\" |\n| W8: SNR 统计 | Warning | **Resolved**. 300 steps + 95% CI + non-monotonic 发现 |\n| W9: near-orthogonal | Warning | **Resolved**. weakly correlated ($R^2$=0.038) |\n| W10: 28.5% 偏差 | Warning | **Resolved**. TEAL@28.5% 对比, <0.3 PPL 差异 |\n| M4: Forward KL 论证分散 | Minor | **Resolved**. 交叉引用已加 |\n\n### Partially Addressed (3 issues, 降级)\n\n| Issue | Round 6 状态 | 本轮评估 | 新状态 |\n|-------|-------------|---------|--------|\n| C2: 技术新颖性有限 | Critical | Contribution 1 改为 \"Empirical observation\", MaskLLM 对比充分. 但方法本身（KL+Gumbel+Lagrangian 组合）未变. **定位修正到位, 核心局限不变.** | Warning (降级: framing 已改善) |\n| C3: Coupling vs oracle confound | Critical | §4.2 明确承认 confound, Limitations 讨论, 语言改为 \"correlates with\" 而非 \"causes\". **但仍无实验分离.** | Warning (降级: 坦诚承认+语言校正) |\n| W1: PPL-downstream disconnect | Warning | Abstract 更平衡, 30% 为推荐操作点. 但 14B 数据加剧此问题（KL PPL best 但 MMLU 输 8pp）. | Warning (持续) |\n\n### Insufficient Progress (1 issue)\n\n| Issue | Round 6 状态 | 本轮评估 |\n|-------|-------------|---------|\n| W2: Multi-seed 不完整 | Warning | 显著改善但推荐配置（30% uniform PPL 8.82）仍为单 seed |\n\n---\n\n## New Issues This Round\n\n**R7-N1. [Warning] 14B MMLU 反转暴露 output-preservation 目标的根本局限**\n- Table 8: KL PPL=7.62（best）但 MMLU=63.7% vs TEAL 71.8%（-8.1pp）。Uniform 仅恢复 +0.8pp。\n- 这不是简单的 allocation 问题：KL 的 output-preservation 目标在更高 knowledge density 模型上系统性地 underweight task-specific features。\n- 论文诚实报告（\"gap appears intrinsic to KL's output-preservation objective\"），但讨论过于简短。\n- 8B 的 PPL-downstream disconnect（W1）在 14B 被放大为 PPL-MMLU 反转，构成对 KL distillation 方法论的根本质疑。\n- **要求**：14B 段落应更深入讨论 output-preservation vs task-specific preservation 的 tradeoff。\n\n**R7-W1. [Warning] Conclusion 过短**\n- 仅 1 句话（\"A <1% predictor with KL distillation halves TEAL's PPL across 7-14B; uniform allocation cuts cross-seed σ 7.5×.\"），缺 future directions 和 broader implications。\n- 对于一篇完整论文，Conclusion 应至少 3-5 句：核心发现总结 + PPL-downstream disconnect 的反思 + 14B 发现的 implications + future work。\n\n**R7-W2. [Info] `\\enlargethispage{8\\baselineskip}` 格式 hack**\n- experiments.tex 第 253 行。8 行的扩展幅度较大。需确认未导致实际超页。\n\n**R7-W3. [Info] Multi-seed 覆盖不一致**\n- 推荐配置（30% KL uniform, PPL 8.82）是单 seed，而非推荐配置（30% KL global）反而有 3-seed。统计一致性有瑕疵。\n\n---\n\n## Strengths (本轮新增/强化)\n\n**S1. Compensation redundancy 证据链完整**（本轮新增）\nKL+compensation 实验 + convergence 证明 + 两个 sparsity level 交叉验证。这是本轮最重要的贡献：论文从 \"未验证的 claim\" 变为 \"有实验支撑的发现\"。\n\n**S2. 14B 跨规模验证的诚实报告**（本轮新增）\n多数论文会隐藏 mixed results；本文不仅报告 KL PPL 优势，还坦诚展示 MMLU gap 和 uniform 无法修复的事实。这增加了论文的可信度。\n\n**S3. SNR 扩展分析发现 non-monotonic trajectory**（本轮新增）\nBCE mid-training SNR > KL 是一个非 trivial 的发现，提供了新的 mechanistic insight。95% CI 增加了统计可信度。\n\n**S4. 消融设计全面且有信息量**（持续）\nTable 3 的 loss isolation 设计（特别是 BCE+Gumbel+Penalty=38.02 > vanilla BCE=27.97）仍然是论文最强的部分。\n\n**S5. 写作质量良好**（持续）\n无 AI 写作痕迹（grep 确认无 em-dash/en-dash）。Claims 校准到位（correlates, preliminary evidence, qualitative behaviors）。格式合规（8p main, [review] option, anonymous, Limitations/Ethics/Checklist）。\n\n---\n\n## Weaknesses (综合排序)\n\n### Warning (影响评分但不一票否决)\n\n**W1. 技术新颖性有限（持续 5 轮）**\n- 核心方法是 Forward KL (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + Adaptive Penalty（标准约束优化）的组合。MaskLLM 已使用相同原则。\n- 论文已正确重定位为 \"empirical analysis / mechanistic understanding\"，但 Contribution 1 的 gradient formalization 仍然是对 backpropagation 基本性质的重述。\n- 影响：更适合 Findings 而非 Main Conference。\n\n**W2. Coupling vs oracle confound 无实验分离（持续 5 轮）**\n- BCE 使用 magnitude oracles，KL 直接优化 output distribution。观察到的差距可能源于 oracle quality 而非 gradient coupling。\n- 论文现在坦诚承认（§4.2 + Limitations），语言校正为 \"correlates with\"。但 7 轮审稿仍未提供 KL-derived masks → BCE 的控制实验。\n- 影响：gradient analysis（Contribution 1）的因果解释力被削弱。\n\n**W3. PPL-downstream disconnect + 14B MMLU 反转（持续 5 轮 + 新加剧）**\n- 8B: 50% downstream 崩溃；30% MMLU +2pp（温和）。\n- 14B: KL PPL 最优但 MMLU 输 TEAL 8pp，uniform 仅 +0.8pp。\n- 这不是 presentation 问题（叙事已大幅改善），而是方法论的 fundamental limitation：output-distribution preservation ≠ task-relevant preservation。14B 数据表明此 gap 随规模扩大。\n- 影响：削弱 KL distillation 作为通用方法的 claim。\n\n**W4. Multi-seed 覆盖仍不完整（持续 7 轮）**\n- 推荐配置（30% KL uniform, PPL 8.82）仍为单 seed。Table 5 的 40% 行全部单 seed。\n- 较 Round 6 有显著改善（Table 2 多数关键行已有 3-seed），但统计一致性仍有瑕疵。\n\n**W5. Conclusion 过短**\n- 1 句话的 Conclusion 不足以承载 14 页论文的 takeaway。审稿人可能认为草率。\n\n---\n\n## Questions (需作者回应)\n\n**Q1.** 14B MMLU gap（KL 63.7 vs TEAL 71.8）的机制是什么？论文说 \"intrinsic to output-preservation objective\"，但 output preservation 和 task performance 之间的解耦为何在 14B 比 8B 更严重？是否与 Qwen-2.5-14B 的 knowledge density 或 SwiGLU gate distribution 有关？\n\n**Q2.** 30% KL uniform（推荐配置）的 PPL 8.82 为何缺 multi-seed？如果这是最终推荐配置，单 seed 的可靠性如何保证？\n\n**Q3.** BCE mid-training SNR > KL 的 non-monotonic 现象是否有更深层的解释？论文的 \"KL coupling becomes effective after coarse mask learning\" 假说是否可以通过 mask entropy trajectory 验证？\n\n---\n\n## Overall Assessment\n\n**评分: 3.0/5 — Findings**\n**置信度: High (4/5)**\n\n### 与 Round 6 的评分变化\n\nRound 6: 2.5 (Borderline Findings) → Round 7: 3.0 (Findings)\n\n**提升 0.5 分的原因：**\n1. Compensation redundancy 实验补齐了 Round 6 最大的 gap（C1），从 \"未验证 claim\" 变为 \"有实验支撑的发现\"\n2. 14B 跨规模数据，虽然 mixed，但增加了论文的深度和诚实度\n3. Multi-seed 覆盖大幅改善，Table 2 多数关键行有 3-seed\n4. SNR 扩展分析（300 steps + 95% CI + non-monotonic 发现）提供了新的 mechanistic insight\n5. Claims 校准全面到位，写作质量持续良好\n\n**不升至 3.5 的原因：**\n1. 技术新颖性有限——已有组件的直接组合，持续 5 轮未改变\n2. Coupling vs oracle confound 无实验分离——7 轮审稿后仍仅有语言修正\n3. 14B MMLU 反转加剧了 PPL-downstream disconnect，暗示 output-preservation 目标的 fundamental limitation\n4. Multi-seed 覆盖仍有盲区（推荐配置单 seed）\n\n### 定位建议\n\n论文作为 **EMNLP 2026 Findings** 论文是合适的：\n- **实验工作高于 Findings 平均水平**：消融设计全面（Table 3）、跨架构验证（LLaMA/Mistral/Qwen）、negative results 诚实报告、三区域分析有实用价值\n- **方法论贡献不足 Main Conference**：技术为已有组件组合，理论分析是 backprop 基本性质的形式化\n- **最有价值的贡献是 empirical insights**：compensation redundancy、PPL-downstream disconnect 的量化、allocation-dependent operating regions、14B scale-dependent effects\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- 叙事较 Round 6 显著改善：以 30% 推荐操作点开头，14B + MMLU gap 诚实披露\n- 仍有 ~6 个数字（139%, 18%, 7.5×, 49%, 7-14B），但每个服务于叙事，可接受\n- \"rendering post-hoc compensation redundant at both 30% and 50% sparsity\" 现在有实验支撑\n\n### Introduction\n- Contribution 1 \"Empirical observation and quantification\" 比之前的 \"Identification\" 更准确\n- Contribution 2 compensation redundancy claim 有实验支撑\n- Contribution 3 \"allocation-to-downstream interactions at 7-14B\" 准确反映了 mixed results\n\n### Method (§3)\n- 数学表述正确\n- §3.6 Gradient-Based Motivation：SNR 扩展分析（300 steps, non-monotonic trajectory）增加了信息量\n- Taxonomy (Table 1) 作为组织框架有价值\n\n### Experiments (§4)\n- §4.2 Extended Training Analysis（改名 ✓）：wall-clock 对比 ✓；confound acknowledgment ✓\n- §4.3 消融：Compensation Redundancy 段落是本轮最有价值的新增内容\n- §4.4 Regime Analysis：措辞弱化到位\n- §4.5 SPON：weakly correlated ✓\n- §4.6 Cross-arch + 14B：Mistral preliminary evidence ✓；14B 诚实但讨论偏短\n- Inference Efficiency + Training Stability 段落被削减/移入 appendix，正文更紧凑\n\n### Conclusion\n- 过短（1 句）。需要扩展。\n\n### Limitations\n- 全面：PPL as proxy、per-target training、14B MMLU gap、OOD coverage、coupling vs oracle confound、seed variance、no wall-clock speedup。\n- 14B limitation 讨论比 §4.6 更深入（\"output-preservation objective may underweight task-specific features at higher knowledge densities\"），建议将这一讨论也整合到正文。\n\n### Appendix\n- 内容扎实且信息密度高\n- 新增 SNR Extended、Extended Downstream、Compensation Convergence 三个 appendix，均有价值\n- Extended Downstream (HellaSwag/PIQA/BoolQ) 提供了 30% 操作点的正面证据\n\n### Format Compliance\n- 14 页 PDF（8p main + appendix + refs + limitations/ethics）\n- `[review]` option ✓, anonymous ✓, line numbers expected (需确认)\n- `\\enlargethispage{8\\baselineskip}` 需要检查是否导致实际超页\n- 39 references，接近 typical range\n\n---\n\n## Issue Tracker 同步\n\n本轮 resolved 10 个 Round 6 issues，降级 3 个 Critical→Warning，新增 4 个 issues（1 Warning + 1 Warning + 2 Info）。\n\n**跨轮持续未解决的核心问题：**\n- 技术新颖性（R3-S1）：持续 5 轮，已从 Critical 降为 Warning\n- Coupling vs oracle confound（R3-S2）：持续 5 轮，已从 Critical 降为 Warning\n- PPL-downstream disconnect（R3-C2）：持续 5 轮，Warning\n- Multi-seed 不完整（R1-W3）：持续 7 轮，in_progress\n\n**新增 issues：**\n- R7-N1: 14B MMLU 反转（Warning）\n- R7-W1: Conclusion 过短（Warning）\n- R7-W2: enlargethispage 格式（Info）\n- R7-W3: Multi-seed 覆盖不一致（Info）",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-18T12:48:01.994886+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Assistant

_source line 592 · 2026-05-18T12:48:09.011307+00:00_

Round 7 审稿报告已提交。

**核心结论：3.0/5 — Findings（较 Round 6 的 2.5 提升 0.5 分）**

提升原因：
- Compensation redundancy 实验补齐了最大 gap（C1 resolved）
- 14B 跨规模数据增加深度（虽然 mixed results）
- Multi-seed 覆盖大幅改善
- SNR 扩展分析提供新 mechanistic insight
- Claims 校准全面到位

未升至 3.5 的原因：
- 技术新颖性有限（已有组件组合，持续 5 轮）
- Coupling vs oracle confound 无实验分离
- 14B MMLU 反转加剧 PPL-downstream disconnect
- Conclusion 过短，multi-seed 推荐配置仍单 seed

Issue Tracker 已同步更新（resolved 10, 降级 3, 新增 4）。外部审稿（Stanford Agentic Reviewer）状态仍为 pending。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 50

## Round 50

122 recorded events


### User

_source line 593 · 2026-05-18T14:07:04.097242+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-18T14:07:11.332480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-18T14:07:11.383336+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-18T14:07:15.499535+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch,TodoWrite",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch,TodoWrite",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-18T14:07:15.550220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-18T14:07:22.176177+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-18T14:07:22.226820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-18T14:07:29.973197+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'pending', 'activeForm': '检查并发起外部审稿'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 进行独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛或需要下一轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'pending', 'activeForm': '检查并发起外部审稿'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 进行独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛或需要下一轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-18T14:07:30.023863+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-18T14:07:34.340885+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-18T14:07:35.797368+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (181 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- kl30_s456_uniform_v3（准备中）\n- kl30_s123_uniform_v3（准备中）\n- c4_download（准备中）\n- wallclock_speedup_30_50: Sparse activation at 30% and 50% sparsity produces measurable wall-clock inference speedup over dense baseline when using sparse kernels, with 50% showing greater speedup than 30% proportional to compute reduction（准备中）\n- kl50_s456_train_eval（准备中）\n- mag_preservation_reg（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- mvp_kl_norm_s456（准备中）\n- …另有 4 项\n\n## 近期结论\n- **kl30_s456_uniform_v2** (success): KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.\n- **kl30_s123_uniform_v2** (success): KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.\n- **kl50_s42_global_eval** (success): KL-trained predictor at 50% sparsity with global_topk allocation preserves downstream task quality better than uniform allocation because i
…[truncated 1562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-18T14:07:35.797867+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-18T14:07:36.099223+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.blg
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.bbl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.out
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.fls
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.fdb_latexmk

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-18T14:07:36.099617+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-18T14:07:44.031782+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: NLP for Science Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/nlp-science"}]

I found information about EMNLP 2026, though the main call for papers itself wasn't in these results. Here's what I found:

## EMNLP 2026 Related Information

The search r
…[truncated 1426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7932
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-18T14:07:50.686503+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline page limit author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline page limit author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-18T14:07:51.640506+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines template page limit anonymous"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines template page limit anonymous"
  }
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-18T14:07:52.293288+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-18T14:07:58.227086+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline page limit author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here's the key information about EMNLP 2026 ARR submissions:

## Submission Deadline
The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Page Limits
The format uses a two-column layout with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Author Guidelines & Requirements
Key author guidelines include:

- Authors must explicitly declare which conference they intend to commit to at submission time (for the ARR 2026 May cycle aligned with both EMNLP and AACL).

- All authors must complete the author registration form by May 27, 2026 EoD AoE.

- All a
…[truncated 506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7540
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-18T14:07:59.633347+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines template page limit anonymous"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026 regarding templates, page limits, and anonymity:

## Page Limits

Short papers have a maximum of 4 content pages, and long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not c
…[truncated 1141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7992
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-18T14:07:59.633964+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml\", \"content\": \"# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction\\n# Last updated: 2026-05-15\\n# Survey scope: 2023-2026, 4 directions\\n\\n# =============================================================================\\n# Direction 1: KL distillation for structured/activation sparsity\\n# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.\\n# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for\\n# learnable bias correction, not predictor training. This is our novelty.\\n# =============================================================================\\n\\n- title: \\\"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\\\"\\n  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]\\n  venue: ICML 2026\\n  year: 2026\\n  arxiv_id: \\\"2512.12744\\\"\\n  category: direct-competitor\\n  role: \\\"最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor\\\"\\n  key_finding: \\\"SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销\\\"\\n  relevance_to_us: \\\"SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致\\\"\\n\\n- title: \\\"Compact Language Models via Pruning and Knowledge Distillation\\\"\\n  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv_id: \\\"2407.14679\\\"\\n  category: method-component\\n  role: \\\"KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching\\\"\\n  key_finding: \\
…[truncated 1510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7340
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-18T14:08:05.867786+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the complete submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, reference page limits, mandatory sections (limitations, ethics), review criteria, and any key dates/deadlines. Also note if papers go through ARR."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract the complete submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, reference page limits, mandatory sections (limitations, ethics), review criteria, and any key dates/deadlines. Also note if papers go through ARR."
  }
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-18T14:08:07.323940+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete ARR submission guidelines: page limits (long/short), template, anonymity requirements, appendix rules, reference pages, mandatory sections, formatting requirements. Include any desk-reject conditions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the complete ARR submission guidelines: page limits (long/short), template, anonymity requirements, appendix rules, reference pages, mandatory sections, formatting requirements. Include any desk-reject conditions."
  }
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-18T14:08:07.977626+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-18T14:08:12.445572+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long Papers:** 8 pages + 1 additional page in camera-ready version (9 pages max)
- **Short Papers:** 4 pages + 1 additional page in camera-ready version (5 pages max)

## ARR Process
Papers undergo "two-stage review": authors submit to ACL Rolling Review (ARR) for reviews and meta-reviews, then commit reviewed articles to EMNLP 2026 where final acceptance decisions are made.

## Key Anonymity Rules
- Double-blind review maintained throughout
- "Reviewers will not see authors, nor will authors see reviewers"
- Reviews remain non-public on ARR
- "No anonymity period requirement" per ACL/ARR policies
- Authors may optionally make anonymized submissions publicly visible

## Mandatory Sections & Requirements
- Limitations section required
- Ethics checklist (responsible NLP research) required
- Follow ACL Publication Ethics Policy and ARR Ethics Policy
- Disclosure Policy compliance required
- Two-way anonymized review instructions must be followed

## Critical Deadlines
- **ARR Submission:** May 25, 2026
- **Reviewer Registration:** May 27, 2026
- **Author Response Period:** July 7-13, 2026
- **EMNLP Commitment:** August 2, 2026
- **Acceptance Notification:** August 20, 2026

## Appendix & Supplementary Materials
The guidelines reference "optional supplementary materials, appendices, software and data" as permitted per ARR requirements.

## Key Policy Note
Papers with "hallucinated citations" or ethical violations face potential desk rejection and author ineligibility for EMNLP 2026-2027.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "elapsed_ms": 6577
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-18T14:08:13.853286+00:00_

# ARR Submission Guidelines Summary

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

## Template & Formatting

Submissions must use "the official ACL style template" available on GitHub and follow "*ACL" conference formatting guidelines. Authors cannot modify style files or use templates from other conferences. Papers failing to conform to required styles, including page size, margins, and fonts, face rejection without review.

## Anonymity Requirements

Papers must exclude author names and affiliations. Self-references revealing identity should be reframed—use "Author previously showed" rather than "We previously showed." References to documents unavailable to reviewers are prohibited. Supplementary materials and repository links must be anonymized; Dropbox and similar tracking services are disallowed.

## Appendix Rules

Appendices follow the main paper after references and don't count toward page limits. They must use double-column format per approved exceptions. Critical content for assessing novelty, technical correctness, or claims belongs in the main paper, not appendices.

## Mandatory Sections

- **Limitations section** (required, untitled variations rejected): Discusses constraints of presented work only
- **Responsible NLP Checklist**: Completion required; incorrect/incomplete entries trigger desk rejection

## Desk-Rejection Conditions

Papers face desk rejection for:
- Format/anonymity violations
- Dual submissions or self-plagiarism
- Missing limitations section
- Incorrect/incomplete responsible checklist
- Anonymity policy violations
- Length limit exceedances
- Appendices not following required format (as of July 2025)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "elapsed_ms": 6529
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-18T14:08:13.853891+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \\\"unfair comparison\\\" attacks. **Iso-compute evidence (eval_bce_v3_s42)**: with 2.71× more gradient updates, BCE TEAL PPL=27.97 vs KL=12.00 (2.33× gap persists), and BCE loss saturates (step 500→2700: Δ=-0.006). The advantage is structural: BCE optimizes per-neuron binary classification, but inference uses global top-k budget allocation — per-neuron scoring is suboptimal under global reallocation. KL directly optimizes output distribution, naturally compatible with any allocation strategy. (Headline claim)\\n\\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \\\"subsuming\\\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that K
…[truncated 3353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5876
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-18T14:08:21.984899+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-18T14:08:22.437402+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \\\"unfair comparison\\\" attacks. **Iso-compute evidence (eval_bce_v3_s42)**: with 2.71× more gradient updates, BCE TEAL PPL=27.97 vs KL=12.00 (2.33× gap persists), and BCE loss saturates (step 500→2700: Δ=-0.006). The advantage is structural: BCE optimizes per-neuron binary classification, but inference uses global top-k budget allocation — per-neuron scoring is suboptimal under global reallocation. KL directly optimizes output distribution, naturally compatible with any allocation strategy. (Headline claim)\\n\\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \\\"subsuming\\\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that K
…[truncated 8198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-18T14:08:22.437857+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-18T14:08:22.940333+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-18T14:08:23.543261+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-18T14:08:23.895001+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-18T14:08:24.096079+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-18T14:08:24.146805+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_7.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-18T14:08:38.814413+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-18T14:08:38.865116+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-18T14:08:42.178616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-18T14:08:42.630654+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions and achieves higher oracle F1 yet 139\% worse perplexity than a KL-trained predictor.
4	A lightweight predictor ($<$1\% of base parameters) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution, rendering post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
5	On LLaMA-3.1-8B at the recommended 30\% sparsity, KL reduces PPL degradation 18\% over TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$, eliminating seed-dependent instability.
6	At 50\% sparsity, the PPL advantage widens to 49\% but downstream tasks degrade regardless of allocation, revealing allocation-dependent operating regions at 7--8B scale.
7	Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though 14B reveals a scale-dependent MMLU gap not resolved by allocation strategy.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-18T14:08:42.681398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-18T14:08:42.681790+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	We provide this analysis.
9	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of $j$ alone, independent of every other neuron.
10	Under KL divergence, the gradient for neuron $j$ in layer $\ell$ factors as:
11	\begin{equation*}
12	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
13	\end{equation*}
14	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, coupling each neuron's gradient to every other neuron's mask state.
15	This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 139\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preser
…[truncated 1574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-18T14:08:43.133865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-18T14:08:43.586871+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
15	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups
…[truncated 2535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-18T14:08:43.587385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-18T14:08:44.089735+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden sta
…[truncated 14198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-18T14:08:44.090196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-18T14:08:44.542561+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}
…[truncated 16396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-18T14:08:44.542930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-18T14:08:45.446713+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-4pt}
4	
5	KL distillation replaces per-neuron BCE with output-distribution coupling: a predictor ($<$1\% of base) halves TEAL's perplexity across 7--14B, with compensation (+67.2M params) redundant at both tested sparsity levels.
6	At 30\%, uniform allocation delivers $7.5\times$ smaller cross-seed $\sigma$; allocation-aware evaluation is essential since perplexity alone is a poor downstream proxy.
7	At 14B, the PPL advantage persists but an MMLU gap emerges, a scale-dependent tradeoff warranting further investigation.
8	
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-18T14:08:45.447107+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-18T14:08:45.949218+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	Our recommended operating point (30\% sparsity, uniform allocation) is validated at 7--8B scale; at 14B, the MMLU gap persists regardless of allocation strategy (\S\ref{sec:14b}). Scaling to 70B remains untested.
6	Out-of-distribution evaluation (Appendix~\ref{app:ood}) covers 30\% and 50\% sparsity on C4; extending to 70\% is left to future work.
7	Our attribution of KL's advantage to gradient coupling (\S\ref{sec:method:gradient}) is supported by SNR measurements and the BCE isolation ablation, but does not fully disentangle coupling from oracle quality: BCE uses magnitude-based oracles while KL directly optimizes output preservation, and an ablation using KL-derived masks as BCE targets would more precisely isolate the coupling effect.
8	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.
9	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
10	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that
…[truncated 53 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-18T14:08:45.949628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-18T14:08:46.150663+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText a
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-18T14:08:46.151042+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-18T14:08:46.201665+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net ac
…[truncated 12466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-18T14:09:02.922866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-18T14:09:03.576839+00:00_

1	issues:
2	  # === Round 1-2 resolved issues (compact) ===
3	  - id: "R2-N1"
4	    summary: "Limitations section 格式不合规"
5	    category: format
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 1
10	    mentions: [{round: 1, reviewers: [1, 2], note: "desk-reject 条件"}]
11	    action_items: [{round: 1, action: "拆为独立 section*", assigned_to: "paper_agent", status: done}]
12	    resolution: "Commit 7018701"
13	    resolution_round: 1
14	
15	  - id: "R2-N2"
16	    summary: "页数超限"
17	    category: format
18	    severity: critical
19	    status: resolved
20	    first_raised_round: 1
21	    last_seen_round: 1
22	    mentions: [{round: 1, reviewers: [1, 2], note: "R2 提出"}]
23	    action_items: [{round: 1, action: "确认页数", assigned_to: "paper_agent", status: done}]
24	    resolution: "8p main + 2p appendix"
25	    resolution_round: 1
26	
27	  - id: "R1-N1"
28	    summary: "缺 OOD PPL 评估"
29	    category: experiment
30	    severity: critical
31	    status: resolved
32	    first_raised_round: 1
33	    last_seen_round: 1
34	    mentions: [{round: 1, reviewers: [1, 2], note: "R1 critical"}]
35	    action_items: [{round: 1, action: "C4 validation PPL", assigned_to: "main_agent", status: done}]
36	    resolution: "C4: Dense=9.21, KL=18.40, TEAL=38.75"
37	    resolution_round: 1
38	
39	  - id: "R1-N2"
40	    summary: "Structural failure 证据不足"
41	    category: experiment
42	    severity: critical
43	    status: resolved
44	    first_raised_round: 1
45	    last_seen_round: 1
46	    mentions: [{round: 1, reviewers: [1, 2], note: "两位独立指出"}]
47	    action_items: [{round: 1, action: "BCE+Gumbel ×3 LR 对照", assigned_to: "main_agent", status: done}]
48	    resolution: "BCE best=38.02 vs KL=11.79"
49	    resolution_round: 1
50	
51	  - id: "R1-N3"
52	    summary: "消融缺关键维度"
53	    category: experiment
54	    severity: warning
55	    status: resolved
56	    first_raised_round: 1
57	    last_seen_round: 1
58	    mentions: [{round: 1, reviewers: [1, 2]
…[truncated 33157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-18T14:09:03.577384+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-18T14:09:03.627914+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-18T14:09:25.836552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-18T14:09:25.887421+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 15271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-18T14:09:35.926169+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check external review config",
  "subagent_type": "Explore",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu, find any config file (YAML, JSON, TOML) that mentions \"external_review\" or \"paperreview\". Check common locations: config.yaml, project.yaml, .claude/config*, agent/config*, etc. Report the relevant setting (especially external_review.paperreview_ai.enabled). Quick search."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check external review config",
    "subagent_type": "Explore",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu, find any config file (YAML, JSON, TOML) that mentions \"external_review\" or \"paperreview\". Check common locations: config.yaml, project.yaml, .claude/config*, agent/config*, etc. Report the relevant setting (especially external_review.paperreview_ai.enabled). Quick search."
  }
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-18T14:09:38.135200+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.{yaml,yml,json,toml}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.{yaml,yml,json,toml}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-18T14:09:38.336474+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_ssh_env-probe_20260515T101035_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_code_mvp-training-pipeline_20260515T103054_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_research_spon-survey_20260515T103818_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_ssh_fix-model-path_20260515T104116_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_ssh_dry-run-training_20260515T111136_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_ssh_fix-blockers_20260515T113045_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/checkpoints/mvp_kl_s123_PREPARING_20260515T115100.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/checkpoints/mvp_kl_s456_PREPARING_20260515T115102.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/checkpoints/mvp_bce_s42_PREPARING_20260515T115105.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/checkpoints/mvp_bce_s123_PREPARING_20260515T115107.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/checkpoints/mvp_bce_s456_PREPARING_20260515T115108.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/checkpoints/mvp_kl_s123_PENDING_20260515T115114.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/checkpoints/mvp_kl_s456_PENDING_20260515T115115.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/checkpoints/mvp_bce_s42_PENDING_20260515T115116.json
/home/ubuntu/.agent-ml-research-idea_
…[truncated 11831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-18T14:09:38.638649+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-18T14:09:38.741380+00:00_

Found 12 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_9377f94f5f31e719154474b70f5c3d18_paper_agent.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/archive/feishu_group_oc_dbbf8d2c695f1e79e11713aebc107790_director_20260517T171027_960441.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/worker_util_copy_lagrangian_fig_20260517T070307.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_util_copy_lagrangian_fig_20260517T070307.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_analysis_kl_bce_f1_oracle_20260517T051453.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/archive/feishu_group_oc_dbbf8d2c695f1e79e11713aebc107790_director_20260516T193527_913366.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-18T14:09:41.050135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/CLAUDE.md"
  }
}
```

</details>

---


### Tool result

_source line 660 · 2026-05-18T14:09:41.352199+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 661 · 2026-05-18T14:09:41.402902+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -maxdepth 3 -type f \\( -name \"config*.yaml\" -o -name \"config*.yml\" -o -name \"project.yaml\" -o -name \"project.yml\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -maxdepth 3 -type f \\( -name \"config*.yaml\" -o -name \"config*.yml\" -o -name \"project.yaml\" -o -name \"project.yml\" \\) 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-18T14:09:41.553879+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-18T14:09:43.762507+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/ 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 664 · 2026-05-18T14:09:44.114310+00:00_

total 32
drwxr-xr-x  3 ubuntu ubuntu  4096 May 15 10:05 .
drwxr-xr-x 13 ubuntu ubuntu  4096 May 18 14:07 ..
-rw-r--r--  1 ubuntu ubuntu 17174 May 18 14:07 CLAUDE.md
drwxr-xr-x 54 ubuntu ubuntu  4096 May 18 01:21 sessions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 665 · 2026-05-18T14:09:44.114798+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -type f -name \"*.yaml\" -o -name \"*.yml\" | grep -v checkpoint | grep -v worker | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -type f -name \"*.yaml\" -o -name \"*.yml\" | grep -v checkpoint | grep -v worker | head -30"
  }
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-18T14:09:44.216193+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea
…[truncated 159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 667 · 2026-05-18T14:09:46.977198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/CLAUDE.md"
  }
}
```

</details>

---


### Tool result

_source line 668 · 2026-05-18T14:09:47.178484+00:00_

1	## 当前项目
2	当前绑定项目：**distill_sparse_swiglu**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("distill_sparse_swiglu")` 或 `load_project_config("distill_sparse_swiglu", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/`（写文件后用 `register_artifact` 注册）
9	
10	## 用户自定义规则（必须遵守）
11	### 审稿规则
12	
13	- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
14	
15	> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。
16	
17	## Worker 操作规范
18	
19	### paper-writing-norms
20	
21	# 论文写作风格规范
22	
23	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
24	
25	---
26	
27	## 一、总体写作哲学
28	
29	### 1.1 故事驱动，不是数据堆砌
30	
31	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
32	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
33	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
34	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
35	
36	### 1.2 主线统一性
37	
38	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
39	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
40	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
41	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
42	
43	### 1.3 专有名词必须有定义
44	
45	- 首次出现的专有名词/缩写必须给出完整定义和解释
46	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
47	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
48	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
49	
50	### 1.4 写作前必读同类优秀论文
51	
52	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
53	- 重点学：
54	  - Abstract 怎么用最少篇幅讲完故事
55	  - Introduction 怎么从大问题切入到具体贡献
56	  - Related Work 怎么 positioning 自己（不是 survey）
…[truncated 9008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 669 · 2026-05-18T14:09:47.178862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml"
  }
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-18T14:09:47.379849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-18T14:09:47.430458+00:00_

File content (292.1KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-18T14:09:47.682591+00:00_

1	- id: art_20260515_1938be
2	  name: report_mvp_bce_s42
3	  type: report
4	  description: mvp_bce_s42 实验分析报告：BCE loss 训练 1000 steps 完成，最终 loss 0.6430，sparsity
5	    0.551
6	  path: projects/distill_sparse_swiglu/artifacts/mvp_bce_s42/report/report_mvp_bce_s42.md
7	  url: null
8	  project: distill_sparse_swiglu
9	  exp_id: mvp_bce_s42
10	  skill: ''
11	  created_at: '2026-05-15T12:27:29.705745+00:00'
12	  tags:
13	  - training
14	  - bce
15	  - mvp
16	  - seed42
17	- id: art_20260515_caab5d
18	  name: mvp_kl_s42_eval_and_collapse_analysis
19	  type: report
20	  description: mvp_kl_s42 evaluation results and sparsity collapse root cause analysis
21	  path: projects/distill_sparse_swiglu/artifacts/mvp_kl_s42/report/mvp_kl_s42_eval_report.json
22	  url: null
23	  project: distill_sparse_swiglu
24	  exp_id: mvp_kl_s42
25	  skill: ''
26	  created_at: '2026-05-15T13:27:45.593569+00:00'
27	  tags:
28	  - eval
29	  - kl
30	  - sparsity-collapse
31	  - analysis
32	- id: art_20260515_adad23
33	  name: BCE MVP 3-Seed Analysis
34	  type: report
35	  description: 3-seed aggregated statistics for BCE sparsity predictor MVP (seeds
36	    42/123/456). Includes mean±std tables, per-layer sparsity analysis, seed stability
37	    assessment (CV), LaTeX snippets for paper, and KL baseline comparison.
38	  path: projects/distill_sparse_swiglu/artifacts/_project/report/bce_mvp_3seed_analysis.md
39	  url: null
40	  project: distill_sparse_swiglu
41	  exp_id: null
42	  skill: ''
43	  created_at: '2026-05-15T14:08:07.767370+00:00'
44	  tags:
45	  - bce
46	  - mvp
47	  - 3-seed
48	  - statistics
49	  - baseline
50	  - paper
51	- id: art_20260515_1a9d62
52	  name: eval_results_v2_true_dense
53	  type: data
54	  description: '统一重评结果(5 checkpoints x 3 PPL modes)。evaluate.py md5: f4086818bb55dc354ea4c6fe8ed8899a。修复将
55	    predictor hard mask 误标为 dense 的 bug。'
56	  path: null
57	  url: file:///root/distill_sparse_swiglu/artifacts/eval_results_v2.json
58	  project: distill_sparse_swiglu
59	  exp_
…[truncated 37527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 673 · 2026-05-18T14:09:50.494738+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "content",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "content",
    "context": "5"
  }
}
```

</details>

---


### Tool result

_source line 674 · 2026-05-18T14:09:50.645752+00:00_

&lt;persisted-output>
Output too large (65.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-director-e331551e/ec283e87-d70e-465e-9c8b-6f0b6564454e/tool-results/toolu_01DJ36FJ1qwPw4J3JNoZcR8n.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-183-
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-184----
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-185-
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-186-## External Review (Stanford Agentic Reviewer)
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-187-
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md:188:外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-189-
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-190----
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-191-
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-192-## Overall Assessment
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md-193-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_1.md-165-
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu
…[truncated 356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 675 · 2026-05-18T14:09:53.521975+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"config*\" \\) -newer /etc/hostname 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"config*\" \\) -newer /etc/hostname 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-18T14:09:53.623658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/CLAUDE.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/CLAUDE.md",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-18T14:09:53.624130+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.git/config
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 678 · 2026-05-18T14:09:53.624359+00:00_

1	## 当前项目
2	当前绑定项目：**distill_sparse_swiglu**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("distill_sparse_swiglu")` 或 `load_project_config("distill_sparse_swiglu", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/`（写文件后用 `register_artifact` 注册）
9	
10	## 用户自定义规则（必须遵守）
11	### 审稿规则
12	
13	- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
14	
15	> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。
16	
17	## Worker 操作规范
18	
19	### paper-writing-norms
20	
21	# 论文写作风格规范
22	
23	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
24	
25	---
26	
27	## 一、总体写作哲学
28	
29	### 1.1 故事驱动，不是数据堆砌
30	
31	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
32	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
33	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
34	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
35	
36	### 1.2 主线统一性
37	
38	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
39	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
40	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
41	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
42	
43	### 1.3 专有名词必须有定义
44	
45	- 首次出现的专有名词/缩写必须给出完整定义和解释
46	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
47	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
48	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
49	
50	### 1.4 写作前必读同类优秀论文
51	
52	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
53	- 重点学：
54	  - Abstract 怎么用最少篇幅讲完故事
55	  - Introduction 怎么从大问题切入到具体贡献
56	  - Related Work 怎么 positioning 自己（不是 survey）
…[truncated 1250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 679 · 2026-05-18T14:09:56.146252+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ | head -30"
  }
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-18T14:09:56.648621+00:00_

total 612
drwxr-xr-x 13 ubuntu ubuntu   4096 May 18 14:07 .
drwxrwxr-x  6 ubuntu ubuntu   4096 May 15 10:05 ..
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 10:05 .claude
drwxr-xr-x  7 ubuntu ubuntu   4096 May 18 13:58 .git
drwxr-xr-x  6 ubuntu ubuntu   4096 May 15 23:33 .venv
-rw-r--r--  1 ubuntu ubuntu  17174 May 18 14:07 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu      0 May 15 10:07 ROADMAP.lock
-rw-------  1 ubuntu ubuntu   4044 May 18 12:02 ROADMAP.md
drwxr-xr-x 23 ubuntu ubuntu   4096 May 18 13:48 artifacts
drwxr-xr-x  2 ubuntu ubuntu  77824 May 18 13:56 checkpoints
-rw-r--r--  1 ubuntu ubuntu      0 May 15 10:10 constraints.lock
-rw-------  1 ubuntu ubuntu   1063 May 17 15:15 constraints.yaml
-rw-r--r--  1 ubuntu ubuntu      0 May 15 10:07 decisions.lock
-rw-------  1 ubuntu ubuntu  47676 May 18 11:53 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 16 05:30 docs
-rwxr-xr-x  1 ubuntu ubuntu      0 May 15 16:49 dream_registry.lock
-rw-------  1 ubuntu ubuntu    919 May 15 17:59 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu    924 May 15 17:59 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu      0 May 15 17:19 experiment_plan.lock
-rw-------  1 ubuntu ubuntu   4912 May 16 05:10 experiment_plan.yaml
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 23:13 figures
-rw-r--r--  1 ubuntu ubuntu  27238 May 16 09:24 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 15 10:10 logs
-rw-r--r--  1 ubuntu ubuntu   2367 May 18 05:04 memory.md
-rw-r--r--  1 ubuntu ubuntu      0 May 16 22:00 mistakes.lock
-rw-------  1 ubuntu ubuntu  18517 May 18 11:59 mistakes.yaml
drwxr-xr-x  3 ubuntu ubuntu   4096 May 18 13:58 paper
-rw-r--r--  1 ubuntu ubuntu   9853 May 18 01:27 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu      0 May 16 13:27 paper_provenance.lock

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 681 · 2026-05-18T14:09:56.649226+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/*.yaml 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/*.yaml 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool result

_source line 682 · 2026-05-18T14:09:56.699781+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-18T14:09:59.109236+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -path \"*distill_sparse_swiglu*\" -name \"*config*\" -type f 2>/dev/null | grep -v \".git\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -path \"*distill_sparse_swiglu*\" -name \"*config*\" -type f 2>/dev/null | grep -v \".git\" | head -20"
  }
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-18T14:09:59.311328+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-18T14:09:59.412166+00:00_

total 32
drwxr-xr-x  3 ubuntu ubuntu  4096 May 15 10:05 .
drwxr-xr-x 13 ubuntu ubuntu  4096 May 18 14:07 ..
-rw-r--r--  1 ubuntu ubuntu 17174 May 18 14:07 CLAUDE.md
drwxr-xr-x 54 ubuntu ubuntu  4096 May 18 01:21 sessions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 686 · 2026-05-18T14:09:59.462902+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_code_bce-comp-training-config_20260515T172020_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_code_bce-comp-training-config_20260515T172020.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_code_kl-extra-seeds-config_20260515T172039_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_code_kl-extra-seeds-config_20260515T172039.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/bin/numpy-config
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy/__config__.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy/__config__.pyi
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy/typing/tests/data/fail/ufunc_config.pyi
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy/typing/tests/data/pass/__pycache__/ufunc_config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy/typing/tests/data/pass/ufunc_config.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy/typing/tests/data/reveal/ufunc_config.pyi
/home/ubuntu/.agent-ml-research-
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 687 · 2026-05-18T14:10:02.174061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md",
  "offset": "180",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md",
    "offset": "180",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-18T14:10:02.174563+00:00_

180	
181	1. **SparseInfer**: Jiho Shin, Hoeseok Yang, Youngmin Yi. "SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference." DATE 2025. arXiv:2411.12692. （R2 raise，R1 部分 AGREE。需验证真实性。）
182	2. **SVD Contextual Sparsity Predictors**: Georgii Serbin et al. "SVD Contextual Sparsity Predictors for Fast LLM Inference." March 2026. arXiv:2603.14110. （R2 raise，R1 部分 AGREE。需验证真实性。）
183	
184	---
185	
186	## External Review (Stanford Agentic Reviewer)
187	
188	外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。
189	
190	---
191	
192	## Overall Assessment
193	
194	**评分: Borderline (2.5/5) — Borderline Findings**
195	**置信度: High (4/5)**
196	
197	两位 Reviewer 独立给出一致评分（均 2.5/5），交叉回应后主要分歧在严重程度而非方向，整体收敛良好。
198	
199	### 核心判断
200	
201	本文在实验层面做了扎实的工作——消融设计全面（Table 3）、跨架构验证到位（Table 6）、三区域分析有实用价值（Table 5）、负面结果诚实报告。写作质量良好，格式完全合规。
202	
203	但三个 Critical 问题阻碍 Main Conference 接收：
204	
205	1. **核心 claim 未验证**（C1）：论文最突出的 claim "eliminates the need for compensation" 缺少 KL+compensation 控制实验。这是一个简单但关键的实验 gap。
206	
207	2. **技术新颖性有限**（C2）：方法是已有技术（KL + Gumbel + Lagrangian）的直接组合。MaskLLM 已展示了相同原则在 N:M sparsity 中的应用。Per-token × Coupled 的问题空间填充有价值，但单纯的组合应用不构成 EMNLP Main 级别的方法论贡献。
208	
209	3. **因果归因不足**（C3）：将 KL 优势归因于 "gradient coupling" 但未分离 coupling effect 和 oracle quality effect。梯度分析形式化了 backpropagation 的基本性质（R2 观点）/ 有增量价值但不构成 strong theory（R1 观点）。
210	
211	### 实际影响力的限制
212	
213	- 推荐操作点（30% sparsity）：MMLU 65→40%（-38%），GSM8K 48→7%（-85%），改善温和（PPL 19%, MMLU +2pp vs TEAL）
214	- 50% sparsity（最大 PPL 优势区间）：downstream 完全崩溃
215	- 6.4% 推理开销、无 wall-clock speedup
216	
217	### 建议
218	
219	1. **重新定位**：将论文定位为 empirical analysis / mechanistic understanding 论文，而非方法论论文。降低 "structural mismatch" 理论贡献的权重，强化经验分析的贡献（三区域发现、PPL-downstream disconnect 的量化、BCE 失败模式分析）。
220	2. **补充关键实验**：KL+compensation、KL-oracle BCE ablation、multi-seed、30% C4 OOD、Mistral downstream
221	3. **修正 claims**：弱化 "eliminates compensation"、修正 "near-orthogonal"、修正 "iso-compute" 术语
222	4. **考虑 Findings track**：论文的实验工作高于平均水平，
…[truncated 124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 689 · 2026-05-18T14:10:05.543539+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview_ai\\|external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/*.jsonl 2>/dev/null | head -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview_ai\\|external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/*.jsonl 2>/dev/null | head -3"
  }
}
```

</details>

---


### Tool result

_source line 690 · 2026-05-18T14:10:05.744813+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_9377f94f5f31e719154474b70f5c3d18_paper_agent.jsonl:{"ts": "2026-05-18T13:58:39.321875+00:00", "role": "tool_result", "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:paper_agent", "text": "On branch master\nChanges not staged for commit:\n  (use \"git add &lt;file>...\" to update what will be committed)\n  (use \"git restore &lt;file>...\" to discard changes in working directory)\n\tmodified:   paper/experiments.tex\n\nUntracked files:\n  (use \"git add &lt;file>...\" to include in what will be committed)\n\t.claude/\n\tAGENTS.md\n\tROADMAP.lock\n\tROADMAP.md\n\tartifacts/\n\tcheckpoints/\n\tconstraints.lock\n\tconstraints.yaml\n\tdecisions.lock\n\tdecisions.yaml\n\tdocs/\n\tdream_registry.lock\n\tdream_registry.yaml\n\tdream_registry.yaml.bak\n\texperiment_plan.lock\n\texperiment_plan.yaml\n\texternal_review_state.json\n\tfigures/\n\tliterature_map.yaml\n\tlogs/\n\tmemory.md\n\tmistakes.lock\n\tmistakes.yaml\n\tpaper/_pdf_images/\n\tpaper/acl.sty\n\tpaper/acl_natbib.bst\n\tpaper/main.aux\n\tpaper/main.blg\n\tpaper/main.fdb_latexmk\n\tpaper/main.fls\n\tpaper/main.log\n\tpaper/main.out\n\tpaper/main.pdf\n\tpaper_framing.md\n\tpaper_provenance.lock\n\tpaper_provenance.yaml\n\tregistry.lock\n\tregistry.yaml\n\treport.md\n\tresults/\n\tstudy_status.lock\n\ttask_context/\n\twriting_plan.yaml\n\nno changes added to commit (use \"git add\" and/or \"git commit -a\")\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/paper_agent_f4a39553", "tool": "Bash", "elapsed_ms": 502}
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:{"ts": "2026-05-16T18:52:47.709174+00:00", "role": "tool_result", "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director", "text": "1\t---\n2\tname: review-dire
…[truncated 2664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 691 · 2026-05-18T14:10:05.745501+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -name \"project.yaml\" -o -name \"config.yaml\" 2>/dev/null | grep agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -name \"project.yaml\" -o -name \"config.yaml\" 2>/dev/null | grep agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-18T14:10:06.097200+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 693 · 2026-05-18T14:10:11.820113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/external_review_state.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/external_review_state.json"
  }
}
```

</details>

---


### Tool result

_source line 694 · 2026-05-18T14:10:11.820455+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 695 · 2026-05-18T14:10:14.280594+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && git status --short | grep external"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu && git status --short | grep external"
  }
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-18T14:10:14.431699+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 697 · 2026-05-18T14:10:14.483246+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -name \"external_review_state.json\" -o -name \"*external*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -name \"external_review_state.json\" -o -name \"*external*\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 698 · 2026-05-18T14:10:14.533879+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/fonttools-4.63.0.dist-info/licenses/LICENSE.external

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 699 · 2026-05-18T14:10:17.347087+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -h \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/*.jsonl 2>/dev/null | grep -o '\"[^\"]*external[^\"]*\":\"[^\"]*\"' | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -h \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/*.jsonl 2>/dev/null | grep -o '\"[^\"]*external[^\"]*\":\"[^\"]*\"' | head -10"
  }
}
```

</details>

---


### Tool result

_source line 700 · 2026-05-18T14:10:17.397722+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 701 · 2026-05-18T14:10:19.756696+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "decisions.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "decisions.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 702 · 2026-05-18T14:10:19.757536+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml\", \"content\": \"_next_id: 58\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:07 UTC\\n  summary: 'MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perplexity 对比'\\n  rationale: '核心假设是 KL 训练通过端到端梯度捕获联合神经元交互，优于 BCE 的逐神经元独立目标。MVP 聚焦最基础的 A/B 对比（KL vs\\n    BCE），不涉及 SPON 组合或 compensation network，以最小成本验证核心假设是否成立。Pass criteria: KL ppl <\\n    BCE ppl 差距 ≥ 0.3。评审笔记中的 novelty ceiling 和 effect size 风险恰好需要 MVP 先确认效果量级。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:08 UTC\\n  summary: 校准数据从 SlimPajama-627B 改为 WikiText-103 train split\\n  rationale: SlimPajama-627B 在 AutoDL 代理环境下 HF datasets API 无法访问（DatasetNotFoundError）。WikiText-103\\n    (~100M tokens) 满足 MVP 1K steps 需求，KL/BCE 用同一数据保证公平性。偏离 IDEA_BRIEF 原始方案，full paper\\n    实验阶段可能需要切回更多样的校准数据。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  - exp_id: mvp_bce_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 13:16 UTC\\n  summary: KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_weight\\n  rationale: mvp_kl_s42 的 sparsity 从 0.328 单调降至 0.000。KL loss 天然在 0% sparsity 处最小，固定\\n    reg_weight=0.1 被 KL loss（66 倍量级差）完全压制。Lagrangian multiplier 通过 dual gradient ascent\\n    自动调整约束强度，是约束优化的标准方案。暂停 KL s123/s456 直到修复验证通过。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: evidence\\n    result: sparsity collapsed to 0%, KL=3.3 vs reg=0.05\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 13:34 UTC\\n  summary: KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯 KL 端到端训练\\n  rationale: Lagrangian quicktest 确认 lambda 爬升追不上 KL loss 量级（KL~418 vs constraint~1.2）。根因是\\n    KL 用 sum reduction 导致绝对值过大。归一化到 per-token per-dim 后 KL 应降至 ~0.003，与 constraint\\n    可比。选 C 而非 A（BCE warm-start）因为 C
…[truncated 39302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-18T14:10:27.181425+00:00_

Perfect! I found the information. Based on my search, here is the configuration status for the `distill_sparse_swiglu` project:

## Finding: External Review Configuration Status

**Location:** The project configuration is managed through the ML Research agent system and referenced in the Review Director workflow skill.

**Current Status of `external_review.paperreview_ai.enabled`:**

According to the review reports and workflow documentation I found:

- **Setting is NOT enabled** - The Round 6 review report explicitly states:
  ```
  外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。
  ```
  (Translation: "External review: Not configured (project external_review.paperreview_ai.enabled not enabled).")

**Configuration Details:**
- The setting `external_review.paperreview_ai.enabled` is referenced in the Review Director session initialization workflow (found in feishu chat logs at `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl`)
- The workflow Step 0.6 checks this setting and conditionally calls `request_external_review()` if enabled
- The configuration is part of the project's ML research agent setup (not in local YAML files, but managed by the agent framework)

**Key Files Referenced:**
- Round 6 Review Report: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md` (line 188)
- Review Director Workflow: Found in the feishu chat logs with the complete initialization procedure

The external_review setting is part of the centralized project configuration system used by the ML Research agent framework, not stored as a standalone config file in the project directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Agent",
  "elapsed_ms": 51255
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-18T14:10:45.706099+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 进行独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛或需要下一轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 进行独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛或需要下一轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-18T14:10:45.756866+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-18T14:11:01.591356+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 进行独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛或需要下一轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6: 外部审稿线', 'status': 'completed', 'activeForm': '外部审稿未启用，跳过'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 进行独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛或需要下一轮'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-18T14:11:01.642086+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-18T14:11:27.515464+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重：方法严谨性 + 实验有效性**\n\n### 投稿信息\n- 论文路径：`projects/distill_sparse_swiglu/paper/main.tex`（多文件结构，各章节为独立 .tex）\n- 目标 venue：**EMNLP 2026**（ACL Rolling Review May 2026 cycle）\n- 截止日期：2026-05-25\n- 页数限制：Long paper 8 页正文 + 无限引用/Limitations/Ethics\n- 模板：ACL 官方模板，`\\usepackage[review]{acl}`\n- 双盲评审\n- 强制 Limitations section + Responsible NLP Research Checklist\n\n### 论文概要\n标题：\"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n核心贡献：用 KL 散度（而非 BCE）训练 SwiGLU LLM 的稀疏性预测器，消除补偿网络需求。在 LLaMA-3.1-8B 上验证，跨架构到 Mistral-7B 和 Qwen-2.5-14B。\n\n### 你需要重点审查的方面\n\n1. **技术正确性**\n   - 梯度分析（§3.6 BCE vs KL gradient structure）是否数学正确？推导是否 rigorous？\n   - Gumbel-Sigmoid relaxation 的使用是否合理？温度退火策略是否有理论依据？\n   - Adaptive penalty controller（§3.5）的收敛保证？30% 目标偏差 5% 是否影响结论？\n\n2. **实验设计与统计**\n   - 主要 claim 的统计支撑是否充分？哪些关键对比有 multi-seed，哪些只有单 seed？\n   - Iso-compute 对比（§4.2）是否公平？BCE 2700 步 vs KL 1000 步的 wall-clock 对齐是否合理？\n   - Oracle F1 分析（F1 高但 PPL 差）的论证是否 sound？是否存在 confound？\n   - OOD 评估（C4）的覆盖是否充分？\n\n3. **消融完整性**\n   - Table 3 的消融是否覆盖所有关键设计选择？\n   - BCE+Gumbel+Penalty 消融是否公平隔离了 loss function 的贡献？\n   - 是否存在遗漏的关键消融（如 KL-derived masks 作为 BCE targets）？\n\n4. **可复现性**\n   - 超参数是否完整报告？\n   - 训练/评估 protocol 是否清晰可复现？\n   - GPU 硬件信息是否充分？\n\n5. **Claims 与 Evidence 对齐**\n   - \"renders compensation redundant\" 的 claim 是否有充分实验支撑？\n   - 三 regime 分析（30%/40%/50%）每个 regime 仅一个数据点，claim 强度是否匹配？\n   - 14B 结果（KL PPL 好但 MMLU 差 8pp）与整体叙事是否一致？\n\n请按 ARR reviewer guidelines 格式输出完整审稿意见：Summary → Strengths → Weaknesses (Critical/Major/Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）→ Detailed Comments。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重：方法严谨性 + 实验有效性**\n\n### 投稿信息\n- 论文路径：`projects/distill_sparse_swiglu/paper/main.tex`（多文件结构，各章节为独立 .tex）\n- 目标 venue：**EMNLP 2026**（ACL Rolling Review May 2026 cycle）\n- 截止日期：2026-05-25\n- 页数限制：Long paper 8 页正文 + 无限引用/Limitations/Ethics\n- 模板：ACL 官方模板，`\\usepackage[review]{acl}`\n- 双盲评审\n- 强制 Limitations section + Responsible NLP Research Checklist\n\n### 论文概要\n标题：\"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n核心贡献：用 KL 散度（而非 BCE）训练 SwiGLU LLM 的稀疏性预测器，消除补偿网络需求。在 LLaMA-3.1-8B 上验证，跨架构到 Mistral-7B 和 Qwen-2.5-14B。\n\n### 你需要重点审查的方面\n\n1. **技术正确性**\n   - 梯度分析（§3.6 BCE vs KL gradient structure）是否数学正确？推导是否 rigorous？\n   - Gumbel-Sigmoid relaxation 的使用是否合理？温度退火策略是否有理论依据？\n   - Adaptive penalty controller（§3.5）的收敛保证？30% 目标偏差 5% 是否影响结论？\n\n2. **实验设计与统计**\n   - 主要 claim 的统计支撑是否充分？哪些关键对比有 multi-seed，哪些只有单 seed？\n   - Iso-compute 对比（§4.2）是否公平？BCE 2700 步 vs KL 1000 步的 wall-clock 对齐是否合理？\n   - Oracle F1 分析（F1 高但 PPL 差）的论证是否 sound？是否存在 confound？\n   - OOD 评估（C4）的覆盖是否充分？\n\n3. **消融完整性**\n   - Table 3 的消融是否覆盖所有关键设计选择？\n   - BCE+Gumbel+Penalty 消融是否公平隔离了 loss function 的贡献？\n   - 是否存在遗漏的关键消融（如 KL-derived masks 作为 BCE targets）？\n\n4. **可复现性**\n   - 超参数是否完整报告？\n   - 训练/评估 protocol 是否清晰可复现？\n   - GPU 硬件信息是否充分？\n\n5. **Claims 与 Evidence 对齐**\n   - \"renders compensation redundant\" 的 claim 是否有充分实验支撑？\n   - 三 regime 分析（30%/40%/50%）每个 regime 仅一个数据点，claim 强度是否匹配？\n   - 14B 结果（KL PPL 好但 MMLU 差 8pp）与整体叙事是否一致？\n\n请按 ARR reviewer guidelines 格式输出完整审稿意见：Summary → Strengths → Weaknesses (Critical/Major/Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）→ Detailed Comments。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-18T14:11:49.060066+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21544
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-18T14:11:49.462202+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重：新颖性 + 完整性**\n\n### 投稿信息\n- 论文路径：`projects/distill_sparse_swiglu/paper/main.tex`（多文件结构，各章节为独立 .tex）\n- 目标 venue：**EMNLP 2026**（ACL Rolling Review May 2026 cycle）\n- 截止日期：2026-05-25\n- 页数限制：Long paper 8 页正文 + 无限引用/Limitations/Ethics\n- 模板：ACL 官方模板，`\\usepackage[review]{acl}`\n- 双盲评审\n- 强制 Limitations section + Responsible NLP Research Checklist\n\n### 论文概要\n标题：\"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n核心贡献：用 KL 散度训练 SwiGLU LLM 的稀疏性预测器（替代传统 BCE），消除补偿网络；发现 allocation-dependent 的 sparsity regime 转换。\n\n### 你需要重点审查的方面\n\n1. **新颖性评估**\n   - 核心方法（Forward KL + Gumbel-Sigmoid + Lagrangian penalty）是否为已有技术的直接组合？方法论创新在哪里？\n   - 与 MaskLLM（同样 frozen weights + learnable masks + KL）的区分是否充分？\n   - BCE vs KL 的梯度分析是 end-to-end > decomposed 的基本原则的重述，还是有实质性新洞察？\n   - Taxonomy（Table 1）的贡献是否被过度宣传？\n   - 整体贡献是否足够支撑 EMNLP Main，还是更适合 Findings？\n\n2. **Related Work 覆盖**\n   - 39 篇引用对于 EMNLP 长文是否充足（typical 40-60）？\n   - 是否遗漏关键相关工作？特别关注：近期 activation sparsity predictor、KL distillation for efficiency、structured pruning 方向\n   - 与 SPON、FastForward、DejaVu 的区分是否清晰准确？\n   - Related Work 是否做了有效的 positioning（不是 survey 而是 gap analysis）？\n\n3. **写作质量**\n   - Abstract 是否在 30 秒内传达问题、方法、贡献？数字密度是否合适？\n   - Introduction 叙事线是否连贯（问题→Gap→方法→结果→贡献）？\n   - 是否存在 AI 写作痕迹（em-dash、-ing 短语结尾、过度分段、\"Furthermore/Moreover\" 连用）？\n   - 专有名词首次出现是否有定义？\n   - Conclusion 长度和内容是否合适？\n\n4. **格式合规**\n   - 正文是否 ≤8 页？（检查是否使用 `\\enlargethispage` 等页面操控）\n   - Limitations 和 Ethics 是否合规？\n   - Responsible NLP Research Checklist 是否逐项认真填写？\n   - 匿名化是否彻底（无作者信息泄露、无匿名仓库链接等）？\n   - 引用格式是否符合 ACL 标准？\n\n5. **叙事一致性**\n   - Abstract → Introduction → Method → Results → Conclusion 是否形成一条主线？\n   - 14B 的 mixed result（PPL 好但 MMLU 差 8pp）是否与 output-distribution preservation 的叙事矛盾？\n   - 50% 下 downstream collapse 但标题/Abstract 仍推 50% 结果，framing 是否诚实？\n   - PPL-downstream disconnect 在叙事中的地位是否恰当？\n\n请按 ARR reviewer guidelines 格式输出完整审稿意见：Summary → Strengths → Weaknesses (Critical/Major/Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）→ Detailed Comments。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重：新颖性 + 完整性**\n\n### 投稿信息\n- 论文路径：`projects/distill_sparse_swiglu/paper/main.tex`（多文件结构，各章节为独立 .tex）\n- 目标 venue：**EMNLP 2026**（ACL Rolling Review May 2026 cycle）\n- 截止日期：2026-05-25\n- 页数限制：Long paper 8 页正文 + 无限引用/Limitations/Ethics\n- 模板：ACL 官方模板，`\\usepackage[review]{acl}`\n- 双盲评审\n- 强制 Limitations section + Responsible NLP Research Checklist\n\n### 论文概要\n标题：\"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n核心贡献：用 KL 散度训练 SwiGLU LLM 的稀疏性预测器（替代传统 BCE），消除补偿网络；发现 allocation-dependent 的 sparsity regime 转换。\n\n### 你需要重点审查的方面\n\n1. **新颖性评估**\n   - 核心方法（Forward KL + Gumbel-Sigmoid + Lagrangian penalty）是否为已有技术的直接组合？方法论创新在哪里？\n   - 与 MaskLLM（同样 frozen weights + learnable masks + KL）的区分是否充分？\n   - BCE vs KL 的梯度分析是 end-to-end > decomposed 的基本原则的重述，还是有实质性新洞察？\n   - Taxonomy（Table 1）的贡献是否被过度宣传？\n   - 整体贡献是否足够支撑 EMNLP Main，还是更适合 Findings？\n\n2. **Related Work 覆盖**\n   - 39 篇引用对于 EMNLP 长文是否充足（typical 40-60）？\n   - 是否遗漏关键相关工作？特别关注：近期 activation sparsity predictor、KL distillation for efficiency、structured pruning 方向\n   - 与 SPON、FastForward、DejaVu 的区分是否清晰准确？\n   - Related Work 是否做了有效的 positioning（不是 survey 而是 gap analysis）？\n\n3. **写作质量**\n   - Abstract 是否在 30 秒内传达问题、方法、贡献？数字密度是否合适？\n   - Introduction 叙事线是否连贯（问题→Gap→方法→结果→贡献）？\n   - 是否存在 AI 写作痕迹（em-dash、-ing 短语结尾、过度分段、\"Furthermore/Moreover\" 连用）？\n   - 专有名词首次出现是否有定义？\n   - Conclusion 长度和内容是否合适？\n\n4. **格式合规**\n   - 正文是否 ≤8 页？（检查是否使用 `\\enlargethispage` 等页面操控）\n   - Limitations 和 Ethics 是否合规？\n   - Responsible NLP Research Checklist 是否逐项认真填写？\n   - 匿名化是否彻底（无作者信息泄露、无匿名仓库链接等）？\n   - 引用格式是否符合 ACL 标准？\n\n5. **叙事一致性**\n   - Abstract → Introduction → Method → Results → Conclusion 是否形成一条主线？\n   - 14B 的 mixed result（PPL 好但 MMLU 差 8pp）是否与 output-distribution preservation 的叙事矛盾？\n   - 50% 下 downstream collapse 但标题/Abstract 仍推 50% 结果，framing 是否诚实？\n   - PPL-downstream disconnect 在叙事中的地位是否恰当？\n\n请按 ARR reviewer guidelines 格式输出完整审稿意见：Summary → Strengths → Weaknesses (Critical/Major/Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）→ Detailed Comments。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-18T14:11:50.887782+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1425
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-18T14:11:58.719624+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 独立审稿",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: distill_sparse_swiglu\n- 论文路径: projects/distill_sparse_swiglu/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 独立审稿",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: distill_sparse_swiglu\n- 论文路径: projects/distill_sparse_swiglu/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-18T14:11:58.770267+00:00_

Next wakeup scheduled for 14:16:00 (in 241s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---
