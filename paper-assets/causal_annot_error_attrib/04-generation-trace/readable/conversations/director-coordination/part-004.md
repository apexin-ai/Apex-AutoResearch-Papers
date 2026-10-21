# Director coordination — Part 4 of 8

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/1d/1de11abfd142608a2277.json)

## Round 88

### Tool call

_source line 900 · 2026-05-23T04:10:21.847823+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。R1 指出缺少 commercial API 和 near-perfect accuracy regime。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 11\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。承认为 honest limitation + pipeline design 缓解。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补直觉解释。R1 新增具体批评：B.5 stress test 仅用随机扰动模型，未测试结构化违反（outcome-conditional prompting、文本难度-outcome 关联、label-specific LLM bias）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 11\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT。R1 完整审稿 Excitement 3.5/5 部分因此。建议 Section 3.3 增加显式 ASV-vs-E-value 对比段。\"\n    action_items:\n      - round: 8\n        action: \"ASV 措辞从 framework 降为 diagnostics\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Section 4.4 已解释。\"\n    resolution_round: 8\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"CRITICAL——要求降低声称。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Abstract 已改为 'concentrated in secondary coefficients'。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未直接提及。Abstract 现为 'exclusively in secondary coefficients with small effect sizes'。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"Abstract 进一步降级\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已降级为 'concentrated in secondary coefficients'。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未直接提及。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"与 R5-N3 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。EXP-4（23 真实矩阵 × 4 DGP）进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 完整审稿 W1 再次提出（适用范围未充分论证）。R2 交叉回应成功 REBUT severity（Table 15 97.3%）。Director 维持 should-fix。建议主文引用 Table 15。\"\n    action_items:\n      - round: 8\n        action: \"报告 general case 统计\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"EXP-4 用 23 真实矩阵评估 proportional effects\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。R11 R1 Excitement 3.5/5 部分因此。\"\n    action_items:\n      - round: 8\n        action: \"与 R4-W6 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加三级层次说明。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：三级层次清晰，被两位 Reviewer 赞为 strength。可能已修复。\"\n    action_items:\n      - round: 8\n        action: \"与 R8-C1 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1]\n        note: \"Collider脚注已添加。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。可能已修复。\"\n    action_items:\n      - round: 8\n        action: \"Table 1 caption 添加 Collider 脚注\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。可能已修复或优先级降低。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：exposure/IV 的 CI 跨界是拓扑特异问题，非框架缺陷。建议报告 CI 在何 N 下收敛。\"\n    action_items:\n      - round: 8\n        action: \"分 topology 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。可能已修复或优先级降低。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: critical\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识降级：两位 Reviewer 认为论文诚实处理。R1 完整审稿给 Soundness 4/5。Director 降级为 should-fix。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-C2\n    category: soundness\n    severity: critical\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续：要求 f/g 评估。EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 W1 再次提出但评为 should-fix。R2 成功 REBUT severity。Director 降为 should-fix。\"\n    action_items:\n      - round: 8\n        action: \"EXP-1 proportional effects breakdown\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"EXP-4 23 真实矩阵 × 4 DGP proportional effects 评估\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R8-W1\n    category: novelty\n    severity: major\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。R1 Excitement 3.5/5 部分因此。\"\n    action_items:\n      - round: 8\n        action: \"ASV 定位调整\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-W2\n    category: soundness\n    severity: major\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"均匀 ε 局限。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R1 完整审稿 W2 新增具体批评：stress test 仅用随机扰动，未测试结构化违反模式（outcome-conditional prompting, 文本难度-outcome 关联, label-specific LLM bias）。\"\n    action_items:\n      - round: 8\n        action: \"EXP-3 realistic ε\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-W3\n    category: method\n    severity: major\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：拓扑特异问题。建议报告 CI 收敛的 N 阈值。\"\n    action_items:\n      - round: 8\n        action: \"分 topology 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R2]\n        note: \"已添加。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。论文 Related Work 现引用 ding_vanderweele2016。可能已修复。\"\n    action_items:\n      - round: 8\n        action: \"引用 Ding & VanderWeele\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: critical\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。要求 f/g coefficient of variation 评估。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识降级：R2 成功 REBUT severity。Director 综合降为 should-fix。\"\n    action_items:\n      - round: 9\n        action: \"EXP-4 23 真实矩阵 × 4 DGP proportional effects 评估\"\n        assigned_to: agent\n        status: in_progress\n      - round: 9\n        action: \"method.tex 非差异性局限性讨论增强\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-C2\n    category: scope\n    severity: critical\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需 Section 3.1 加线性 SEM 动机 + Section 4 提升 logistic 结论。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：主文整合 logistic 结果不足。R1 Q4 新增具体问题：logistic 下 bias 量级解释（log-odds ratio vs additive effect）。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 9\n        action: \"Section 4 提升 logistic DGP 核心结论\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-M1\n    category: soundness\n    severity: major\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 已包含 proof obstacle 解释。两位 Reviewer 均认为处理诚实。R1 Soundness 4/5。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 proof obstacle 技术解释\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-M2\n    category: method\n    severity: major\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需在主文 Section 3.3 总结 Algorithm 1 核心逻辑。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Algorithm 1 被两位 Reviewer 赞为 S5/S6 strength。可能已修复。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.3 加 Algorithm 1 摘要 2-3 行\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R2, R1]\n        note: \"改为 'first unified analysis' + building on Brenner/Teblunthuis。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：措辞恰当。可能已修复。\"\n    action_items:\n      - round: 9\n        action: \"Introduction novelty claim 改写\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"改为 topology-specific。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。Abstract 已 topology-specific。可能已修复。\"\n    action_items:\n      - round: 9\n        action: \"Abstract sign reversal 改为 topology-specific range\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"DDL 前无法新增。Limitations 扩展。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。R11 共识：不影响核心贡献。\"\n    action_items:\n      - round: 9\n        action: \"Limitations 增加 LLM 多样性讨论\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-S4\n    category: presentation\n    severity: should-fix\n    summary: \"PPI++ 47.0% vs Table 4 17.0 数字不一致\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: \"数字实际一致（47.0%），Reviewer 误读。无需修改论文。\"\n    resolution_round: 9\n\n  # === Round 11 新发现 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增强论文对 EMNLP 应用导向读者的说服力。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增加 3-4 句直觉语言解释。\"\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1]\n        note: \"R1 完整审稿 W3：论文强调 K=2→K≥3 的结构性质变，但校正比较仅用 K=3。缺少 K∈{2,5,10} 的校正敏感性分析。建议至少对 2-3 种关键拓扑补充。\"\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1]\n        note: \"R1 完整审稿 W4：应在 Section 4.1 或 5 增加 2-3 句实践 guidance——如使用 IV 策略需要的最低 diagonal dominance。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现，含 R1 和 R2 共识）\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：(1) Prediction-Powered Causal Inferences 2025, (2) Variance-Aware LLM Annotation 2025, (3) Hidden Measurement Error in LLM Pipelines 2026, (4) Dawid & Skene 1979, (5) Rosenbaum 2002 + Mathur et al. 2018。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1]\n        note: \"M1: Eq.(2) wⱼₖ 依赖的 marginal distribution 未 clarify (真实 A vs A*); M2: Figure 2 y 轴标签不够 informative; M3: Section 4.4 'predictably' 主观用语; M4: Limitations 'outcome misclassification of A' 措辞歧义。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。R1 指出缺少 commercial API 和 near-perfect accuracy regime。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 11\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。承认为 honest limitation + pipeline design 缓解。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补直觉解释。R1 新增具体批评：B.5 stress test 仅用随机扰动模型，未测试结构化违反（outcome-conditional prompting、文本难度-outcome 关联、label-specific LLM bias）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 11\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT。R1 完整审稿 Excitement 3.5/5 部分因此。建议 Section 3.3 增加显式 ASV-vs-E-value 对比段。\"\n    action_items:\n      - round: 8\n        action: \"ASV 措辞从 framework 降为 diagnostics\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Section 4.4 已解释。\"\n    resolution_round: 8\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"CRITICAL——要求降低声称。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Abstract 已改为 'concentrated in secondary coefficients'。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未直接提及。Abstract 现为 'exclusively in secondary coefficients with small effect sizes'。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"Abstract 进一步降级\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已降级为 'concentrated in secondary coefficients'。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未直接提及。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"与 R5-N3 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。EXP-4（23 真实矩阵 × 4 DGP）进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 完整审稿 W1 再次提出（适用范围未充分论证）。R2 交叉回应成功 REBUT severity（Table 15 97.3%）。Director 维持 should-fix。建议主文引用 Table 15。\"\n    action_items:\n      - round: 8\n        action: \"报告 general case 统计\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"EXP-4 用 23 真实矩阵评估 proportional effects\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。R11 R1 Excitement 3.5/5 部分因此。\"\n    action_items:\n      - round: 8\n        action: \"与 R4-W6 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加三级层次说明。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：三级层次清晰，被两位 Reviewer 赞为 strength。可能已修复。\"\n    action_items:\n      - round: 8\n        action: \"与 R8-C1 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1]\n        note: \"Collider脚注已添加。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。可能已修复。\"\n    action_items:\n      - round: 8\n        action: \"Table 1 caption 添加 Collider 脚注\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。可能已修复或优先级降低。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：exposure/IV 的 CI 跨界是拓扑特异问题，非框架缺陷。建议报告 CI 在何 N 下收敛。\"\n    action_items:\n      - round: 8\n        action: \"分 topology 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。可能已修复或优先级降低。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: critical\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识降级：两位 Reviewer 认为论文诚实处理。R1 完整审稿给 Soundness 4/5。Director 降级为 should-fix。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-C2\n    category: soundness\n    severity: critical\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续：要求 f/g 评估。EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 W1 再次提出但评为 should-fix。R2 成功 REBUT severity。Director 降为 should-fix。\"\n    action_items:\n      - round: 8\n        action: \"EXP-1 proportional effects breakdown\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"EXP-4 23 真实矩阵 × 4 DGP proportional effects 评估\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R8-W1\n    category: novelty\n    severity: major\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。R1 Excitement 3.5/5 部分因此。\"\n    action_items:\n      - round: 8\n        action: \"ASV 定位调整\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-W2\n    category: soundness\n    severity: major\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"均匀 ε 局限。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R1 完整审稿 W2 新增具体批评：stress test 仅用随机扰动，未测试结构化违反模式（outcome-conditional prompting, 文本难度-outcome 关联, label-specific LLM bias）。\"\n    action_items:\n      - round: 8\n        action: \"EXP-3 realistic ε\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-W3\n    category: method\n    severity: major\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：拓扑特异问题。建议报告 CI 收敛的 N 阈值。\"\n    action_items:\n      - round: 8\n        action: \"分 topology 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R2]\n        note: \"已添加。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。论文 Related Work 现引用 ding_vanderweele2016。可能已修复。\"\n    action_items:\n      - round: 8\n        action: \"引用 Ding & VanderWeele\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: critical\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。要求 f/g coefficient of variation 评估。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识降级：R2 成功 REBUT severity。Director 综合降为 should-fix。\"\n    action_items:\n      - round: 9\n        action: \"EXP-4 23 真实矩阵 × 4 DGP proportional effects 评估\"\n        assigned_to: agent\n        status: in_progress\n      - round: 9\n        action: \"method.tex 非差异性局限性讨论增强\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-C2\n    category: scope\n    severity: critical\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需 Section 3.1 加线性 SEM 动机 + Section 4 提升 logistic 结论。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：主文整合 logistic 结果不足。R1 Q4 新增具体问题：logistic 下 bias 量级解释（log-odds ratio vs additive effect）。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 9\n        action: \"Section 4 提升 logistic DGP 核心结论\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-M1\n    category: soundness\n    severity: major\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 已包含 proof obstacle 解释。两位 Reviewer 均认为处理诚实。R1 Soundness 4/5。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 proof obstacle 技术解释\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-M2\n    category: method\n    severity: major\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需在主文 Section 3.3 总结 Algorithm 1 核心逻辑。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Algorithm 1 被两位 Reviewer 赞为 S5/S6 strength。可能已修复。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.3 加 Algorithm 1 摘要 2-3 行\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R2, R1]\n        note: \"改为 'first unified analysis' + building on Brenner/Teblunthuis。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：措辞恰当。可能已修复。\"\n    action_items:\n      - round: 9\n        action: \"Introduction novelty claim 改写\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"改为 topology-specific。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。Abstract 已 topology-specific。可能已修复。\"\n    action_items:\n      - round: 9\n        action: \"Abstract sign reversal 改为 topology-specific range\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"DDL 前无法新增。Limitations 扩展。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。R11 共识：不影响核心贡献。\"\n    action_items:\n      - round: 9\n        action: \"Limitations 增加 LLM 多样性讨论\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-S4\n    category: presentation\n    severity: should-fix\n    summary: \"PPI++ 47.0% vs Table 4 17.0 数字不一致\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: \"数字实际一致（47.0%），Reviewer 误读。无需修改论文。\"\n    resolution_round: 9\n\n  # === Round 11 新发现 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增强论文对 EMNLP 应用导向读者的说服力。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增加 3-4 句直觉语言解释。\"\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1]\n        note: \"R1 完整审稿 W3：论文强调 K=2→K≥3 的结构性质变，但校正比较仅用 K=3。缺少 K∈{2,5,10} 的校正敏感性分析。建议至少对 2-3 种关键拓扑补充。\"\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1]\n        note: \"R1 完整审稿 W4：应在 Section 4.1 或 5 增加 2-3 句实践 guidance——如使用 IV 策略需要的最低 diagonal dominance。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现，含 R1 和 R2 共识）\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：(1) Prediction-Powered Causal Inferences 2025, (2) Variance-Aware LLM Annotation 2025, (3) Hidden Measurement Error in LLM Pipelines 2026, (4) Dawid & Skene 1979, (5) Rosenbaum 2002 + Mathur et al. 2018。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1]\n        note: \"M1: Eq.(2) wⱼₖ 依赖的 marginal distribution 未 clarify (真实 A vs A*); M2: Figure 2 y 轴标签不够 informative; M3: Section 4.4 'predictably' 主观用语; M4: Limitations 'outcome misclassification of A' 措辞歧义。\""
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-23T04:10:21.949674+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 27622}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-23T04:12:41.381440+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 11 Consolidated Review Report (修正版)\n\n> **修正说明**：本版修正了先前提交中 Reviewer 1 评分的错误（3.5→4.0），并补充了 R1 完整审稿中新发现的 weaknesses（K 值敏感性、IV 实践指导、结构化违反测试）和 minor issues。\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**投稿类别**: Long Paper (8 页正文限制)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n**格式合规**: ✓ 正文 ≤ 8 页, ✓ Double-blind, ✓ ACL 引用格式, ✓ Limitations 节\n\n---\n\n## Reviewer 评分总览\n\n| 维度 | Reviewer 1 | Reviewer 2 |\n|------|-----------|-----------|\n| **Overall** | **4.0 (Conference)** | **3.5 (Borderline Conference)** |\n| Soundness | 4/5 | 4/5 |\n| Excitement | 3.5/5 | 3/5 |\n| Reproducibility | 4/5 | — |\n| Confidence | 4/5 | — |\n\n---\n\n## Summary\n\n本文分析 K≥3 多类别标注误差在七种典型 DAG 拓扑下如何传播到因果估计中。核心贡献：(1) 七种拓扑的 bias 闭式表达，证明/验证五种拓扑保持符号方向而 exposure 和 IV 可产生符号反转；(2) ASV 诊断工具揭示从 IV（最脆弱）到 M-bias（免疫）的脆弱性谱；(3) FWL 不变性负面结果证明基于矩阵的校正方法对四种拓扑无效。23 个真实 LLM 配置的 161 场景验证确认理论预测（MAPE 1.6%）。\n\n---\n\n## Strengths\n\n**S1 [共识]**: FWL 不变性是干净且重要的负面结果。对四种协变量拓扑，矩阵校正在线性 OLS 下精确实现 0% bias reduction，logistic 下偏差可忽略（< 0.01%, Table 5）。直接阻止实践者在这四种拓扑上浪费计算资源。\n\n**S2 [共识]**: 三级证据层次（Proved / Numerically Verified / Conjectured）是方法论典范。Theorem 1 → Observation 1 → Conjecture 1 清晰界定证明边界。R1 称\"在 NLP 理论工作中罕见且值得推广\"，R2 称\"应被 AC 特别注意\"。\n\n**S3 [共识]**: 首次系统覆盖 K≥3 × 7 种 DAG 拓扑。前作仅覆盖 K=2、4 种 DAG。每种拓扑的 bias 机制都有清晰的因果直觉支撑。\n\n**S4 [共识]**: 实证验证规模充分且全面。161 scenarios MAPE 1.6%，per-topology 从 0.5%（confounding）到 5.7%（IV）。100,000 随机矩阵符号保持验证。\n\n**S5 [共识]**: Proposition 1 的 sign preservation 条件结构清晰。四种拓扑分别用 Cauchy-Schwarz、Berkson attenuation、leakage boundedness 和结构性论证给出充分条件。\n\n**S6 [共识]**: Algorithm 1 + Table 4 校正方法比较覆盖 210 配置（5 方法 × 6 error structures × 7 拓扑），对实践者直接可用。\n\n---\n\n## Weaknesses\n\n### Major (3 项)\n\n**W1 [Major, 分歧]**: ASV 相对于 E-value 的新颖性定位。\n- R2: C(δ) 参数化与 E-value \"高度同构\"，三个 ASV 类型本质是同一 δ 在不同阈值。\n- R1 反驳：扰动对象不同（annotation error vs. unmeasured confounding），sign-flip ASV 无 E-value 对应物，拓扑依赖性是独特创新。R1 Excitement 3.5/5 部分因 ASV 贡献来自系统性而非方法论突破。\n- **Director 判定**：R1 技术正确，R2 的定位建议有价值。**建议 Section 3.3 增加 1 段显式 ASV-vs-E-value 对比**。\n\n**W2 [Major, 共识]**: K≥3 理论不完整。Theorem 1 仅覆盖 K=2；Conjecture 1 依赖 210,000 次数值验证。两位 Reviewer 均认为诚实处理——R1 Soundness 仍给 4/5。R2 建议补充 K=3 符号计算验证。不构成拒稿理由。\n\n**W3 [Major, 分歧→降级]**: Proportional effects (f=λg) 假设适用性。\n- R1 原评为 should-fix（W1）：适用范围未充分论证，未从 23 个 LLM 配置估计 f/g 比值。但也指出 \"B.15 non-proportional 下 97.3% 仍成立\"这个观察被淹没在附录。\n- R2 交叉回应 REBUT severity：Table 15 和 Proposition 4 提供充分 robustness。\n- **Director 判定**：维持 should-fix。主文应引用 Table 15 robustness 结果。\n\n### Should-Fix (8 项)\n\n**W4 [Should-Fix, 共识]**: Abstract 信息密度过高（~5 个数字）。建议保留 1-2 核心数字，其余移至 Introduction。\n\n**W5 [Should-Fix, R1 新增]**: Non-differential stress test 仅覆盖随机扰动模型。R1 指出 B.5 用 Uniform[-1,1] 随机 Δ，未测试结构化违反（outcome-conditional prompting、文本难度-outcome 关联、label-specific LLM bias）。建议补充至少一种结构化违反模型，或在 Limitations 中更明确讨论。\n\n**W6 [Should-Fix, 共识]**: Section 3 NLP 可达性不足。plim/FWL 假设计量经济学背景。建议 Section 3.1 增加 \"Notation roadmap\"（3-4 句）。\n\n**W7 [Should-Fix, 共识]**: LLM 配置多样性有限（四个 7-13B 开源模型，缺 commercial API、>70B、ordinal）。不影响核心贡献。Limitations 应更具体。\n\n**W8 [Should-Fix, R1 新增]**: 校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性。论文强调 K=2→K≥3 质变，但校正是否对此 robust 未验证。建议补充 K∈{2,5,10} 的校正比较（至少 2-3 种关键拓扑）。\n\n**W9 [Should-Fix, 共识]**: ASV Bootstrap CI 过宽（exposure/IV 特异）。Exposure δ*=0.94 [0.60,1.36], IV δ*=0.75 [0.44,1.29] 跨越分界线。其余 5 种拓扑 CI 在同一类别内——拓扑特异问题，非框架缺陷。\n\n**W10 [Should-Fix, 共识]**: 线性 SEM 结论的非线性推广整合不足。Appendix B.6/B.13 有 logistic 验证但主文未充分整合。R1 新增具体问题：logistic 下 bias 量级解释——log-odds ratio vs additive effect 量纲不同，\"approximate correctness\" 如何解释？\n\n**W11 [Should-Fix, 共识]**: ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 提及。展示 FWL 不变性实际意义。\n\n### Minor (2 项)\n\n**W12 [Minor, R1]**: IV 52.6% denominator sign change 缺乏 NLP 实践指导。应在 Section 4.1 增加 2-3 句——如 IV 策略需要的最低 diagonal dominance。\n\n**W13 [Minor, R1]**: 四个文本问题——(M1) Eq.(2) wⱼₖ 的 marginal distribution 来源未 clarify; (M2) Figure 2 y 轴标签不够 informative; (M3) Section 4.4 \"predictably\" 主观用语; (M4) Limitations \"outcome misclassification of A\" 措辞歧义。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. FWL 不变性是论文最强、最干净的贡献\n2. 三级证据层次是值得 AC 特别注意的方法论美德\n3. K≥3 gap 是真实局限但诚实处理——不构成拒稿理由\n4. Abstract 需减少数字密度；Section 3 需提高 NLP 可达性\n5. Non-differential 假设需更好的主文讨论\n6. 真实 LLM 验证对理论论文足够但多样性有限\n7. 所有主要 weaknesses 可在 camera-ready 阶段解决\n\n## Reviewer Divergence [REBUT]\n\n1. **ASV vs E-value 新颖性**：R2 认为高度同构 → R1 反驳扰动对象不同且拓扑依赖性独特。Director 支持 R1 技术判断。\n2. **Proportional effects 严重性**：R1 评 should-fix（evidence buried in appendix），R2 REBUT further downgrade（97.3% robustness）。Director 维持 should-fix。\n3. **Overall 评分分歧**：R1 给 4.0 (Conference)，R2 给 3.5 (Borderline Conference)。分歧主要来自 Excitement（R1: 3.5, R2: 3.0）——R2 对 ASV 新颖性更保守。\n\n---\n\n## Questions for Authors\n\n**Q1** [R1]: Theorem 1 中 V₀(δ) convexity 论证——当 f ≈ λg + small perturbation（near-proportional）时，monotonicity 是否以 Lipschitz 方式退化？Appendix B.12 暗示 worst-case deviation 0.01，但缺乏形式化。\n\n**Q2** [R1]: PPI++ 对 M-bias -88% RMSE 的机制——是否与 M-bias collider conditioning 结构导致 gold labels 引入额外 selection bias 有关？\n\n**Q3** [R1]: ASV bootstrap 不确定性仅在 N=1,500 测试。N > 100,000 时 sharp transition 是否更 sharp？N 增大主要影响 δ_sig 还是 δ_mag？\n\n**Q4** [R1]: Logistic 下 bias 表达式的 \"approximate correctness\" 如何解释？Bias 方向正确但量级不适用，还是两者都近似正确？\n\n**Q5** [R1]: Conjecture 1 的 per-topology ε（confounding 0.006, IV 0.112）——IV 的 11.2% 相对偏差在因果推断中是否可忽略？是否应讨论\"可接受 ε 阈值\"？\n\n**Q6** [R2]: ASV sharp phase transition 对 N < 1,000 的实践含义？ASV 是渐近量，有限样本行为未刻画。\n\n**Q7** [两位]: 23 个 LLM 配置的 non-differential departure ε 量级是多少？\n\n**Q8** [R1]: PPI++ 在不同 gold label 比例下的性能降解？\n\n**Q9** [R1]: ASV 在 DAG 不确定性下的 robustness？\n\n---\n\n## Missing References\n\n1. **Prediction-Powered Causal Inferences** (2025, arXiv:2502.06343) [共识]\n2. **Variance-Aware LLM Annotation** (2025, arXiv:2601.02370) [共识]\n3. **Hidden Measurement Error in LLM Pipelines** (2026, arXiv:2604.11581) [共识]\n4. **Dawid & Skene (1979)** [共识]\n5. **Rosenbaum (2002), Mathur et al. (2018)** [共识]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查仍在进行中（started at 2026-05-23T03:56:05Z）。本报告不等待，完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**评分拆解**：\n- R1: 4.0 (Conference) — 认为核心贡献（FWL 不变性 + 七拓扑 bias taxonomy + 三级证据层次）足以支撑主会议接收，所有 weaknesses 可 camera-ready 解决\n- R2: 3.5 (Borderline Conference) — 对 ASV 新颖性更保守（Excitement 3/5），认为 Conjecture 1 未证明和 NLP 可达性是拉低因素\n- Director: 3.5，倾向 3.5-4.0 区间上半部\n\n**评分理由**：\n\n论文针对一个重要且时机恰当的问题提供了系统性理论分析。核心贡献清晰：\n\n*支持接收的因素*（R1 4.0 的理由，Director 认可）：\n1. 七种拓扑 × K≥3 的完整 bias 分析在文献中确为首次\n2. 三级证据层次的方法论诚实度在 NLP 理论工作中罕见且值得推广\n3. FWL 不变性比 \"method X improves by Y%\" 的正面结果更有长期影响\n4. 实验验证超过理论论文的通常标准\n\n*阻碍完全接收的因素*（R2 3.5 的理由，Director 部分认可）：\n1. K≥3 monotonicity 停留在 conjecture，ASV 框架在主要使用场景下缺乏解析保证\n2. ASV 与 E-value 的技术区分可以更鲜明（虽然 R1 已论证两者不同构）\n3. 对 EMNLP 主流 NLP 读者门槛偏高\n4. 非差异性假设的 stress test 缺少结构化违反模型（R1 新增的重要批评）\n5. 校正方法比较缺少 K 值敏感性分析（R1 新增）\n\n论文可发表，增量贡献明确。通过针对性修改（提高可达性、补充结构化 stress test 或在 Limitations 讨论、增加 K 值敏感性、显式 ASV-vs-E-value 对比），可达到 Conference (4.0) 水平。当前状态为强 Findings 候选或 Borderline Conference。\n\n**Confidence: 4/5**\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 更早将 7 种拓扑分为 \"sign-preserving\"（5）和 \"sign-reversing\"（2）[R1]\n- \"first unified analysis\" 措辞恰当 [共识]\n\n### Section 3 (Method)\n- Section 3.1 开头增加 \"Notation roadmap\"（3-4 句话）[W6]\n- Definition 1 后增加 2-3 句直觉解释 non-differential 假设 [W5]\n- Eq.(2) clarify wⱼₖ 的 marginal distribution 来源 [R1 M1]\n- Section 3.3 增加 ASV-vs-E-value 显式对比段 [W1]\n- 主文引用 Table 15 robustness（97.3% under non-proportional）[W3]\n\n### Section 4 (Experiments)\n- 用 1-2 句话提升 logistic DGP 核心结论到主文，clarify bias 量级解释 [W10]\n- Section 4.1：IV 52.6% sign change 增加 NLP 实践 guidance [W12]\n- Section 4.5：简要提及 ClinicalBERT case study [W11]\n- Figure 2 y 轴标签更 informative [R1 M2]\n- Section 4.4 \"predictably\" → \"consistently with theoretical predictions\" [R1 M3]\n\n### Limitations\n- 更具体讨论 LLM 多样性缺口 [W7]\n- 增加有限样本 ASV 行为讨论 [Q6]\n- 修正 \"outcome misclassification of A\" 措辞歧义 [R1 M4]\n- 更明确讨论哪些 LLM 使用模式违反 non-differential 假设 [W5]\n\n### 事实纠正\n- R1 对 Appendix B.13 的描述有误（称\"一个数据集\"，实为 Monte Carlo 模拟）。已由 R2 纠正。\n- R2 称\"正文未讨论 PPI++ negative transfer\"，但 Section 4.5 已明确提及。已由 R1 纠正。\n- R1 交叉回应中引用了错误的表号（Table 13 是 logistic bias，不是 λ(C)）。已由 R2 纠正。",
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 11 Consolidated Review Report (修正版)\n\n> **修正说明**：本版修正了先前提交中 Reviewer 1 评分的错误（3.5→4.0），并补充了 R1 完整审稿中新发现的 weaknesses（K 值敏感性、IV 实践指导、结构化违反测试）和 minor issues。\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**投稿类别**: Long Paper (8 页正文限制)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n**格式合规**: ✓ 正文 ≤ 8 页, ✓ Double-blind, ✓ ACL 引用格式, ✓ Limitations 节\n\n---\n\n## Reviewer 评分总览\n\n| 维度 | Reviewer 1 | Reviewer 2 |\n|------|-----------|-----------|\n| **Overall** | **4.0 (Conference)** | **3.5 (Borderline Conference)** |\n| Soundness | 4/5 | 4/5 |\n| Excitement | 3.5/5 | 3/5 |\n| Reproducibility | 4/5 | — |\n| Confidence | 4/5 | — |\n\n---\n\n## Summary\n\n本文分析 K≥3 多类别标注误差在七种典型 DAG 拓扑下如何传播到因果估计中。核心贡献：(1) 七种拓扑的 bias 闭式表达，证明/验证五种拓扑保持符号方向而 exposure 和 IV 可产生符号反转；(2) ASV 诊断工具揭示从 IV（最脆弱）到 M-bias（免疫）的脆弱性谱；(3) FWL 不变性负面结果证明基于矩阵的校正方法对四种拓扑无效。23 个真实 LLM 配置的 161 场景验证确认理论预测（MAPE 1.6%）。\n\n---\n\n## Strengths\n\n**S1 [共识]**: FWL 不变性是干净且重要的负面结果。对四种协变量拓扑，矩阵校正在线性 OLS 下精确实现 0% bias reduction，logistic 下偏差可忽略（< 0.01%, Table 5）。直接阻止实践者在这四种拓扑上浪费计算资源。\n\n**S2 [共识]**: 三级证据层次（Proved / Numerically Verified / Conjectured）是方法论典范。Theorem 1 → Observation 1 → Conjecture 1 清晰界定证明边界。R1 称\"在 NLP 理论工作中罕见且值得推广\"，R2 称\"应被 AC 特别注意\"。\n\n**S3 [共识]**: 首次系统覆盖 K≥3 × 7 种 DAG 拓扑。前作仅覆盖 K=2、4 种 DAG。每种拓扑的 bias 机制都有清晰的因果直觉支撑。\n\n**S4 [共识]**: 实证验证规模充分且全面。161 scenarios MAPE 1.6%，per-topology 从 0.5%（confounding）到 5.7%（IV）。100,000 随机矩阵符号保持验证。\n\n**S5 [共识]**: Proposition 1 的 sign preservation 条件结构清晰。四种拓扑分别用 Cauchy-Schwarz、Berkson attenuation、leakage boundedness 和结构性论证给出充分条件。\n\n**S6 [共识]**: Algorithm 1 + Table 4 校正方法比较覆盖 210 配置（5 方法 × 6 error structures × 7 拓扑），对实践者直接可用。\n\n---\n\n## Weaknesses\n\n### Major (3 项)\n\n**W1 [Major, 分歧]**: ASV 相对于 E-value 的新颖性定位。\n- R2: C(δ) 参数化与 E-value \"高度同构\"，三个 ASV 类型本质是同一 δ 在不同阈值。\n- R1 反驳：扰动对象不同（annotation error vs. unmeasured confounding），sign-flip ASV 无 E-value 对应物，拓扑依赖性是独特创新。R1 Excitement 3.5/5 部分因 ASV 贡献来自系统性而非方法论突破。\n- **Director 判定**：R1 技术正确，R2 的定位建议有价值。**建议 Section 3.3 增加 1 段显式 ASV-vs-E-value 对比**。\n\n**W2 [Major, 共识]**: K≥3 理论不完整。Theorem 1 仅覆盖 K=2；Conjecture 1 依赖 210,000 次数值验证。两位 Reviewer 均认为诚实处理——R1 Soundness 仍给 4/5。R2 建议补充 K=3 符号计算验证。不构成拒稿理由。\n\n**W3 [Major, 分歧→降级]**: Proportional effects (f=λg) 假设适用性。\n- R1 原评为 should-fix（W1）：适用范围未充分论证，未从 23 个 LLM 配置估计 f/g 比值。但也指出 \"B.15 non-proportional 下 97.3% 仍成立\"这个观察被淹没在附录。\n- R2 交叉回应 REBUT severity：Table 15 和 Proposition 4 提供充分 robustness。\n- **Director 判定**：维持 should-fix。主文应引用 Table 15 robustness 结果。\n\n### Should-Fix (8 项)\n\n**W4 [Should-Fix, 共识]**: Abstract 信息密度过高（~5 个数字）。建议保留 1-2 核心数字，其余移至 Introduction。\n\n**W5 [Should-Fix, R1 新增]**: Non-differential stress test 仅覆盖随机扰动模型。R1 指出 B.5 用 Uniform[-1,1] 随机 Δ，未测试结构化违反（outcome-conditional prompting、文本难度-outcome 关联、label-specific LLM bias）。建议补充至少一种结构化违反模型，或在 Limitations 中更明确讨论。\n\n**W6 [Should-Fix, 共识]**: Section 3 NLP 可达性不足。plim/FWL 假设计量经济学背景。建议 Section 3.1 增加 \"Notation roadmap\"（3-4 句）。\n\n**W7 [Should-Fix, 共识]**: LLM 配置多样性有限（四个 7-13B 开源模型，缺 commercial API、>70B、ordinal）。不影响核心贡献。Limitations 应更具体。\n\n**W8 [Should-Fix, R1 新增]**: 校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性。论文强调 K=2→K≥3 质变，但校正是否对此 robust 未验证。建议补充 K∈{2,5,10} 的校正比较（至少 2-3 种关键拓扑）。\n\n**W9 [Should-Fix, 共识]**: ASV Bootstrap CI 过宽（exposure/IV 特异）。Exposure δ*=0.94 [0.60,1.36], IV δ*=0.75 [0.44,1.29] 跨越分界线。其余 5 种拓扑 CI 在同一类别内——拓扑特异问题，非框架缺陷。\n\n**W10 [Should-Fix, 共识]**: 线性 SEM 结论的非线性推广整合不足。Appendix B.6/B.13 有 logistic 验证但主文未充分整合。R1 新增具体问题：logistic 下 bias 量级解释——log-odds ratio vs additive effect 量纲不同，\"approximate correctness\" 如何解释？\n\n**W11 [Should-Fix, 共识]**: ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 提及。展示 FWL 不变性实际意义。\n\n### Minor (2 项)\n\n**W12 [Minor, R1]**: IV 52.6% denominator sign change 缺乏 NLP 实践指导。应在 Section 4.1 增加 2-3 句——如 IV 策略需要的最低 diagonal dominance。\n\n**W13 [Minor, R1]**: 四个文本问题——(M1) Eq.(2) wⱼₖ 的 marginal distribution 来源未 clarify; (M2) Figure 2 y 轴标签不够 informative; (M3) Section 4.4 \"predictably\" 主观用语; (M4) Limitations \"outcome misclassification of A\" 措辞歧义。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. FWL 不变性是论文最强、最干净的贡献\n2. 三级证据层次是值得 AC 特别注意的方法论美德\n3. K≥3 gap 是真实局限但诚实处理——不构成拒稿理由\n4. Abstract 需减少数字密度；Section 3 需提高 NLP 可达性\n5. Non-differential 假设需更好的主文讨论\n6. 真实 LLM 验证对理论论文足够但多样性有限\n7. 所有主要 weaknesses 可在 camera-ready 阶段解决\n\n## Reviewer Divergence [REBUT]\n\n1. **ASV vs E-value 新颖性**：R2 认为高度同构 → R1 反驳扰动对象不同且拓扑依赖性独特。Director 支持 R1 技术判断。\n2. **Proportional effects 严重性**：R1 评 should-fix（evidence buried in appendix），R2 REBUT further downgrade（97.3% robustness）。Director 维持 should-fix。\n3. **Overall 评分分歧**：R1 给 4.0 (Conference)，R2 给 3.5 (Borderline Conference)。分歧主要来自 Excitement（R1: 3.5, R2: 3.0）——R2 对 ASV 新颖性更保守。\n\n---\n\n## Questions for Authors\n\n**Q1** [R1]: Theorem 1 中 V₀(δ) convexity 论证——当 f ≈ λg + small perturbation（near-proportional）时，monotonicity 是否以 Lipschitz 方式退化？Appendix B.12 暗示 worst-case deviation 0.01，但缺乏形式化。\n\n**Q2** [R1]: PPI++ 对 M-bias -88% RMSE 的机制——是否与 M-bias collider conditioning 结构导致 gold labels 引入额外 selection bias 有关？\n\n**Q3** [R1]: ASV bootstrap 不确定性仅在 N=1,500 测试。N > 100,000 时 sharp transition 是否更 sharp？N 增大主要影响 δ_sig 还是 δ_mag？\n\n**Q4** [R1]: Logistic 下 bias 表达式的 \"approximate correctness\" 如何解释？Bias 方向正确但量级不适用，还是两者都近似正确？\n\n**Q5** [R1]: Conjecture 1 的 per-topology ε（confounding 0.006, IV 0.112）——IV 的 11.2% 相对偏差在因果推断中是否可忽略？是否应讨论\"可接受 ε 阈值\"？\n\n**Q6** [R2]: ASV sharp phase transition 对 N < 1,000 的实践含义？ASV 是渐近量，有限样本行为未刻画。\n\n**Q7** [两位]: 23 个 LLM 配置的 non-differential departure ε 量级是多少？\n\n**Q8** [R1]: PPI++ 在不同 gold label 比例下的性能降解？\n\n**Q9** [R1]: ASV 在 DAG 不确定性下的 robustness？\n\n---\n\n## Missing References\n\n1. **Prediction-Powered Causal Inferences** (2025, arXiv:2502.06343) [共识]\n2. **Variance-Aware LLM Annotation** (2025, arXiv:2601.02370) [共识]\n3. **Hidden Measurement Error in LLM Pipelines** (2026, arXiv:2604.11581) [共识]\n4. **Dawid & Skene (1979)** [共识]\n5. **Rosenbaum (2002), Mathur et al. (2018)** [共识]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查仍在进行中（started at 2026-05-23T03:56:05Z）。本报告不等待，完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**评分拆解**：\n- R1: 4.0 (Conference) — 认为核心贡献（FWL 不变性 + 七拓扑 bias taxonomy + 三级证据层次）足以支撑主会议接收，所有 weaknesses 可 camera-ready 解决\n- R2: 3.5 (Borderline Conference) — 对 ASV 新颖性更保守（Excitement 3/5），认为 Conjecture 1 未证明和 NLP 可达性是拉低因素\n- Director: 3.5，倾向 3.5-4.0 区间上半部\n\n**评分理由**：\n\n论文针对一个重要且时机恰当的问题提供了系统性理论分析。核心贡献清晰：\n\n*支持接收的因素*（R1 4.0 的理由，Director 认可）：\n1. 七种拓扑 × K≥3 的完整 bias 分析在文献中确为首次\n2. 三级证据层次的方法论诚实度在 NLP 理论工作中罕见且值得推广\n3. FWL 不变性比 \"method X improves by Y%\" 的正面结果更有长期影响\n4. 实验验证超过理论论文的通常标准\n\n*阻碍完全接收的因素*（R2 3.5 的理由，Director 部分认可）：\n1. K≥3 monotonicity 停留在 conjecture，ASV 框架在主要使用场景下缺乏解析保证\n2. ASV 与 E-value 的技术区分可以更鲜明（虽然 R1 已论证两者不同构）\n3. 对 EMNLP 主流 NLP 读者门槛偏高\n4. 非差异性假设的 stress test 缺少结构化违反模型（R1 新增的重要批评）\n5. 校正方法比较缺少 K 值敏感性分析（R1 新增）\n\n论文可发表，增量贡献明确。通过针对性修改（提高可达性、补充结构化 stress test 或在 Limitations 讨论、增加 K 值敏感性、显式 ASV-vs-E-value 对比），可达到 Conference (4.0) 水平。当前状态为强 Findings 候选或 Borderline Conference。\n\n**Confidence: 4/5**\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 更早将 7 种拓扑分为 \"sign-preserving\"（5）和 \"sign-reversing\"（2）[R1]\n- \"first unified analysis\" 措辞恰当 [共识]\n\n### Section 3 (Method)\n- Section 3.1 开头增加 \"Notation roadmap\"（3-4 句话）[W6]\n- Definition 1 后增加 2-3 句直觉解释 non-differential 假设 [W5]\n- Eq.(2) clarify wⱼₖ 的 marginal distribution 来源 [R1 M1]\n- Section 3.3 增加 ASV-vs-E-value 显式对比段 [W1]\n- 主文引用 Table 15 robustness（97.3% under non-proportional）[W3]\n\n### Section 4 (Experiments)\n- 用 1-2 句话提升 logistic DGP 核心结论到主文，clarify bias 量级解释 [W10]\n- Section 4.1：IV 52.6% sign change 增加 NLP 实践 guidance [W12]\n- Section 4.5：简要提及 ClinicalBERT case study [W11]\n- Figure 2 y 轴标签更 informative [R1 M2]\n- Section 4.4 \"predictably\" → \"consistently with theoretical predictions\" [R1 M3]\n\n### Limitations\n- 更具体讨论 LLM 多样性缺口 [W7]\n- 增加有限样本 ASV 行为讨论 [Q6]\n- 修正 \"outcome misclassification of A\" 措辞歧义 [R1 M4]\n- 更明确讨论哪些 LLM 使用模式违反 non-differential 假设 [W5]\n\n### 事实纠正\n- R1 对 Appendix B.13 的描述有误（称\"一个数据集\"，实为 Monte Carlo 模拟）。已由 R2 纠正。\n- R2 称\"正文未讨论 PPI++ negative transfer\"，但 Section 4.5 已明确提及。已由 R1 纠正。\n- R1 交叉回应中引用了错误的表号（Table 13 是 logistic bias，不是 λ(C)）。已由 R2 纠正。",
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-23T04:12:45.552759+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4171
}
```

</details>

---


### Assistant

_source line 904 · 2026-05-23T04:12:57.428238+00:00_

修正版审稿报告已提交。

**Round 11 审稿完成，汇总如下**：

- **R1**: 4.0 (Conference) — Soundness 4/5, Excitement 3.5/5。认为 FWL 不变性 + 七拓扑 taxonomy + 三级证据层次足以支撑主会议接收
- **R2**: 3.5 (Borderline Conference) — Soundness 4/5, Excitement 3/5。对 ASV 新颖性更保守
- **Director 综合**: 3.5 (Borderline Conference)，倾向 3.5-4.0 上半区间

**关键共识**：FWL 不变性是最强贡献；三级证据层次值得 AC 注意；K≥3 gap 诚实处理不构成拒稿理由；所有 weaknesses 可 camera-ready 解决。

**主要改进建议**（按优先级）：
1. Section 3.3 增加 ASV-vs-E-value 显式对比
2. 主文引用 Table 15 proportional effects robustness (97.3%)
3. Section 3.1 增加 Notation roadmap 提升 NLP 可达性
4. Non-differential stress test 补充结构化违反讨论
5. 校正方法补充 K 值敏感性分析
6. Section 4 提升 logistic DGP 核心结论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 89

## Round 89

56 recorded events


### User

_source line 905 · 2026-05-23T06:26:17.694111+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-23T06:26:23.088943+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-23T06:26:23.142955+00:00_

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
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-23T06:26:30.692218+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-23T06:26:30.692622+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-23T06:26:34.157950+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-23T06:26:34.209357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-23T06:26:37.328040+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-23T06:26:38.836846+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1508
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-23T06:26:38.987782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-23T06:26:39.439746+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	
20	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
24	\graphicspath{{../../figures/paper/}}
25	
26	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	
35	\input{introduction}
36	
37	\input{related_work}
38	
39	\input{method}
40	
41	% ── Figures ──
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
46	\vspace{-6pt}
47	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
48	\label{fig:dag_taxonomy}
49	\end{figure*}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
54	\vspace{-6pt}
55	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
56	\label{fig:bias_distribution}
57	\end{figure*}
58	
59	\input{experiments}
60	
61	\input{conclusion}
62	
63	\bibliography{references}
64	
65	\appendix
66	\input{appendix_proofs}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-23T06:26:39.791711+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-23T06:26:50.501445+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are key submission guidelines for EMNLP 2026 related to ARR (ACL Rolling Review):

## Main Conference Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Policy for EMNLP 2026

For the ARR 2026 May cycle aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EM
…[truncated 737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 10709
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-23T06:26:58.814626+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission guidelines including: 1) page limits for long and short papers (main text, references, appendix), 2) template requirements (ACL style), 3) anonymity/blind review rules, 4) submission deadlines (especially ARR May cycle), 5) appendix rules (does it count toward page limit? is it reviewed?), 6) citation/reference format requirements, 7) any special formatting rules, 8) commitment deadlines for EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission guidelines including: 1) page limits for long and short papers (main text, references, appendix), 2) template requirements (ACL style), 3) anonymity/blind review rules, 4) submission deadlines (especially ARR May cycle), 5) appendix rules (does it count toward page limit? is it reviewed?), 6) citation/reference format requirements, 7) any special formatting rules, 8) commitment deadlines for EMNLP 2026"
  }
}
```

</details>

---


### Tool call

_source line 919 · 2026-05-23T06:27:00.979466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 920 · 2026-05-23T06:27:01.333830+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy, sign reversal occurs in 2.1\% of exposure configurations, exclusively in secondary coefficients with small effect sizes; no sign reversals occur for the remaining six topologies including IV. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 921 · 2026-05-23T06:27:01.535304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 922 · 2026-05-23T06:27:01.586018+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, however, is never reversed in any t
…[truncated 2699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 923 · 2026-05-23T06:27:01.586545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 924 · 2026-05-23T06:27:01.637431+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This holds in standard annotation pipelines where the LLM receives only source text and classifies without observing the outcome or covariates---the typical setup in computational social science~\cite{ziems2024can}. Violations arise when pretraining data encodes $A$--$Y$ associations, outcome-conditional prompting is used, or retrieval pipelines surface $Y$-correlated documents. Our stress test (Appendix~\ref{sec:nondiff_stress}) shows uniform violations below $\varepsilon{=}0.05$ cause $<$3~pp degradation; outcome-conditional violations can exceed uniform predictions while label-specific violations are milder. For $K{\geq}3$ exposure, even $\varepsilon{=}0.01$ produces sign reversal in 14 of 16 empirical configurations (Appendix~\ref{sec:realistic_epsilon}).
15	
16	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Throughout, we d
…[truncated 13393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-23T06:27:04.356742+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long papers:** 8 pages main text; final accepted versions get 1 additional page (up to 9 pages)
- **Short papers:** 4 pages main text; final accepted versions get 1 additional page (up to 5 pages)
- References and appendices follow ARR requirements (details referenced but not specified in this document)

## Template Requirements
Papers must follow "all of the ARR submission requirements" including ACL style formatting. The document references the ARR CFP for specific template details rather than restating them.

## Anonymity/Blind Review
The review process maintains double-blind standards: "Reviewers will not see authors, nor will authors see reviewers." Reviews remain confidential on ARR. Authors may optionally make their anonymized submissions publicly visible. No anonymity period is required per ACL/ARR policy.

## Submission Deadlines
- **ARR May 2026 submission:** May 25, 2026 (11:59 PM UTC-12:00)
- **Reviewer registration:** May 27, 2026
- **EMNLP commitment deadline:** August 2, 2026
- **Acceptance notification:** August 20, 2026
- **Camera-ready deadline:** September 20, 2026

## Appendix Rules
The document references ARR's "Optional Supplementary Materials" policy but does not specify whether appendices count toward page limits or review scope.

## Citation/Reference Format
No specific citation format requirements are detailed; authors should "follow all of the ARR submission requirements."

## Special Formatting Rules
Papers must include a limitations section and address the "responsible NLP research checklist."

## Key Commitment Requirement
Authors cannot modify author lists during commitment, though author order changes are permitted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebFetch",
  "elapsed_ms": 5542
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-23T06:27:08.781409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-23T06:27:09.233970+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.3\% (confounding) to 3.7\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient. The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five of seven topologies exhibit zero sign-flip rate across all sampled matrices (Table~\ref{tab:taxonomy}). Confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse th
…[truncated 8162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-23T06:27:09.385468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-23T06:27:09.637277+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayya_sedoc2024} propose str
…[truncated 2179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-23T06:27:09.637702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 931 · 2026-05-23T06:27:10.290309+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology. The classical binary attenuation guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal, while five topologies maintain structural guarantees. ASVs reveal a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and matrix-based corrections are provably ineffective for four topologies due to FWL invariance. All structural patterns persist under logistic DGP. Code and data will be publicly released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information; a stress test (Appendix~\ref{sec:nondiff_stress}) shows that structured violation patterns can exceed or fall below uniform predictions. Closed-form expressions and correction rankings are derived under $K{=}3$ linear structural equations; extensions to arbitrary $K$, nonlinear models, and correction sensitivity to $K$ remain open (Appendix~\ref{sec:logistic_dgp}). Our 23 configurations span four 7--13B open-weight LLMs with diagonal accuracy 0.61--0.83; commercial models, larger architectures ($>$70B), and ordinal tasks remain untested.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-23T06:27:10.692415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 933 · 2026-05-23T06:27:10.943650+00:00_

File content (39226 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 934 · 2026-05-23T06:27:15.567023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-23T06:27:15.618053+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 8484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-23T06:27:16.572434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-23T06:27:17.627790+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@article{cinelli2020making,
5	  author    = {Cinelli, Carlos and Hazlett, Chad},
6	  title     = {Making Sense of Sensitivity: Extending Omitted Variable Bias},
7	  journal   = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
8	  year      = {2020},
9	  volume    = {82},
10	  number    = {1},
11	  pages     = {39--67},
12	  doi       = {10.1111/rssb.12348},
13	}
14	
15	@article{gilardi2023chatgpt,
16	  author    = {Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma\"{e}l},
17	  title     = {{ChatGPT} Outperforms Crowd Workers for Text-Annotation Tasks},
18	  journal   = {Proceedings of the National Academy of Sciences},
19	  year      = {2023},
20	  volume    = {120},
21	  number    = {30},
22	  pages     = {e2305016120},
23	  doi       = {10.1073/pnas.2305016120},
24	}
25	
26	@article{ziems2024can,
27	  author    = {Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},
28	  title     = {Can Large Language Models Transform Computational Social Science?},
29	  journal   = {Computational Linguistics},
30	  year      = {2024},
31	  volume    = {50},
32	  number    = {1},
33	  pages     = {237--291},
34	  doi       = {10.1162/coli\_a\_00502},
35	}
36	
37	@incollection{bound2001measurement,
38	  author    = {Bound, John and Brown, Charles and Mathiowetz, Nancy},
39	  title     = {Measurement Error in Survey Data},
40	  booktitle = {Handbook of Econometrics},
41	  editor    = {Heckman, James J. and Leamer, Edward E.},
42	  year      = {2001},
43	  volume    = {5},
44	  chapter   = {59},
45	  pages     = {3705--3843},
46	  publisher = {Elsevier},
47	}
48	
49	@article{richardson1993bayesian,
50	  author    = {Richardson, Sylvia and Gilks, Walter R.},
51	  title     = {A {Bayesian} Approach to Measurement Error Problems in Epidemiology Using Conditional Independence Models},
52	  journal   = {Amer
…[truncated 5820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-23T06:27:17.678813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_12/submitted.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"NO PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_12/submitted.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"NO PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-23T06:27:18.583654+00:00_

-rw-r--r-- 1 ubuntu ubuntu 921010 May 23 06:20 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_12/submitted.pdf
PDF EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-23T06:27:18.735367+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "description": "Count appendix lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "description": "Count appendix lines"
  }
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-23T06:27:18.787770+00:00_

1298 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-23T06:27:25.789511+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"; ls -la main.pdf 2>/dev/null",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"; ls -la main.pdf 2>/dev/null",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-23T06:27:26.141360+00:00_

Pages:           29
-rw-r--r-- 1 ubuntu ubuntu 921010 May 23 06:20 main.pdf
Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-23T06:27:27.198223+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-23T06:27:27.450101+00:00_

&lt;persisted-output>
Output too large (33.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib--claude-sessions-review-director-d2e6d7be/70e056b3-6822-496a-9749-e73a09ba09f2/tool-results/b44mqkxcw.txt

Preview (first 2KB):
issues:
  # === Round 1-7 历史 (resolved，保留摘要) ===

  - id: R1-N1
    category: soundness
    severity: must-fix
    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
    status: resolved
    first_raised_round: 1
    last_seen_round: 7
    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
    resolution_round: 7

  - id: R1-N2
    category: soundness
    severity: should-fix
    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    resolution: "Abstract 已准确区分 prove/verify。"
    resolution_round: 4

  - id: R1-N3
    category: soundness
    severity: must-fix
    summary: "ASV C(δ) 定义域错误"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Section 3.3 已引入 δ_max 约束。"
    resolution_round: 2

  - id: R2-N1
    category: presentation
    severity: must-fix
    summary: "83.4% sign reversal headline framing 过度声称"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Introduction 已重写。"
    resolution_round: 5

  - id: R2-N2
    category: novelty
    severity: should-fix
    summary: "'first systematic framework' 过度声明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R2-N3
    category: related_work
    severity: must-fix
    summary: "4 篇关键相关工作未引用"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R1-W2
    category: clarity
    severity: should-fix
    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
    status: resolved
  
…[truncated 324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-23T06:27:27.550981+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-23T06:27:27.601722+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_annot_error_attrib'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-23T06:27:33.881720+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib--claude-sessions-review-director-d2e6d7be/70e056b3-6822-496a-9749-e73a09ba09f2/tool-results/b44mqkxcw.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib--claude-sessions-review-director-d2e6d7be/70e056b3-6822-496a-9749-e73a09ba09f2/tool-results/b44mqkxcw.txt"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-23T06:27:34.183846+00:00_

1	issues:
2	  # === Round 1-7 历史 (resolved，保留摘要) ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 7
11	    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
12	    resolution_round: 7
13	
14	  - id: R1-N2
15	    category: soundness
16	    severity: should-fix
17	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
18	    status: resolved
19	    first_raised_round: 1
20	    last_seen_round: 3
21	    resolution: "Abstract 已准确区分 prove/verify。"
22	    resolution_round: 4
23	
24	  - id: R1-N3
25	    category: soundness
26	    severity: must-fix
27	    summary: "ASV C(δ) 定义域错误"
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 1
31	    resolution: "Section 3.3 已引入 δ_max 约束。"
32	    resolution_round: 2
33	
34	  - id: R2-N1
35	    category: presentation
36	    severity: must-fix
37	    summary: "83.4% sign reversal headline framing 过度声称"
38	    status: resolved
39	    first_raised_round: 1
40	    last_seen_round: 5
41	    resolution: "Introduction 已重写。"
42	    resolution_round: 5
43	
44	  - id: R2-N2
45	    category: novelty
46	    severity: should-fix
47	    summary: "'first systematic framework' 过度声明"
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1
51	    resolution: "已修复。"
52	    resolution_round: 2
53	
54	  - id: R2-N3
55	    category: related_work
56	    severity: must-fix
57	    summary: "4 篇关键相关工作未引用"
58	    status: resolved
59	    first_raised_round: 1
60	    last_seen_round: 1
61	    resolution: "已修复。"
62	    resolution_round: 2
63	
64	  - id: R1-W2
65	    category: clarity
66	    severity: should-fix
67	    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
68	    status: resolved
69	    first_raised_round: 1
70	    last_seen_round: 2
71	    resolution: "Section 3.2 已添加 ASV 替代讨论。"
72	    resolution_
…[truncated 31851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-23T06:27:56.468876+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 951 · 2026-05-23T06:27:56.569733+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 952 · 2026-05-23T06:28:00.540379+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4071
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-23T06:28:00.591040+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 4021
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-23T06:28:08.931032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-23T06:28:08.981908+00:00_

200	  &\leq \mathbb{E}\bigl[\sqrt{\operatorname{Var}(g\mid A^*)\,\operatorname{Var}(f\mid A^*)}\bigr]\\
201	  &\leq \sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*)]\;\mathbb{E}[\operatorname{Var}(f\mid A^*)]}\\
202	  &\leq \sqrt{\operatorname{Var}(g(A))\;\operatorname{Var}(f(A))},
203	\end{align*}
204	where the last step uses $\mathbb{E}[\operatorname{Var}(X\mid Y)]\leq\operatorname{Var}(X)$ (law of total variance).
205	
206	\emph{Step 2: Conclude.}
207	The bias satisfies
208	\[
209	  |B(C)| = \frac{|R(C)|}{D(C)} \leq \frac{\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(f)}}{\sigma_T^2} = \bar{B}.
210	\]
211	When $|\tau|>\bar{B}$, the bias cannot cancel $\tau$, so $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ for all $C$.
212	\end{proof}
213	
214	\paragraph{Relationship to the omitted-variable condition.}
215	A weaker (necessary) condition for sign preservation is $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ where $\tau_{\mathrm{OV}}=\tau+\operatorname{Cov}(g,f)/\operatorname{Var}(T)$.
216	If this fails, then $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform noise) already flips the sign.
217	The rigorous sufficient condition $|\tau|>\bar{B}$ implies the weaker condition, since $|B_{\mathrm{OV}}|=|\operatorname{Cov}(g,f)|/\operatorname{Var}(T)\leq\bar{B}$ by Cauchy--Schwarz and $\operatorname{Var}(T)\geq\sigma_T^2$.
218	
219	\paragraph{Verification for paper parameters ($K{=}3$).}
220	With $\tau{=}2.0$, $\boldsymbol{\alpha}{=}(1.5,{-}1.0)$, $\boldsymbol{\beta}^{(A)}{=}(1.0,{-}0.5)$, $\sigma_T{=}1.0$, $\mathbf{p}{=}(0.40,0.35,0.25)$:
221	\begin{align*}
222	  \operatorname{Var}(g) &= \sum_k p_k\alpha_k^2 - \bigl(\textstyle\sum_k p_k\alpha_k\bigr)^2 = 0.962,\\
223	  \operatorname{Var}(f) &= \sum_k p_k(\beta_k^{(A)})^2 - \bigl(\textstyle\sum_k p_k\beta_k^{(A)}\bigr)^2 = 0.362,\\
224	  \bar{B} &= \sqrt{0.962\times 0.362}\;/\;1.0^2 = 0.590.
225	\end{align*}
226	Since $|\tau|{=}2.0 > \bar{B}{=}0.590$, sign preservation 
…[truncated 22369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-23T06:28:47.621558+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- Long Paper：正文 8 页限制，参考文献不限，附录不计入页数\n- 模板：ACL style（`\\usepackage[review]{acl}`）\n- 匿名审稿（double-blind）\n- 必须包含 Limitations section\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 主文件：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_12/submitted.pdf`\n- 总页数：29 页（正文 + 参考文献 + 附录）\n\n## 你的审查侧重\n\n### 1. 理论严谨性\n- Proposition 1 (sign preservation) 的证明是否完整？条件 (a)(b)(c) 是否充分？\n- Theorem 1 (envelope monotonicity) 仅限 K=2——K≥3 依赖 Observation 1 和 Conjecture 1（数值验证）。这个证据层次（Proved/Verified/Conjectured）是否清晰且诚实？\n- λ(C) ∈ [0,1] 在 proportional effects 下成立，但 general case 15-17% 违反。这对 mediation 结论的影响？\n- Conjecture 1 的 ε-approximate monotonicity（ε<0.06）验证规模是否充分？\n\n### 2. 假设合理性\n- Non-differential misclassification (Definition 1)：在 LLM 场景下是否合理？stress test (Appendix B.5) 是否充分覆盖了结构化违反模式（outcome-conditional、label-specific）？\n- Proportional effects (f=λg)：在 NLP 应用中是否可验证？23 个 LLM 配置的经验验证是否充分？\n- 线性 SEM 假设：对 EMNLP 读者是否有足够的动机解释？logistic DGP 结果是否应更突出？\n\n### 3. 实验设计\n- Monte Carlo 验证（MAPE 1.6%）是否有统计量不足的 topology？\n- 23 个 LLM 配置（4 个 7-235B 模型 × 3 任务）是否充分？缺少商业 API 和 >70B 模型。\n- 校正方法比较（Table 4/Appendix）仅用 K=3——FWL invariance 与 K 无关，但 PPI++/MC-SIMEX 排名可能随 K 变化。\n- ASV bootstrap CI 过宽（exposure: [0.60, 1.36]，IV: [0.44, 1.29]）——实践可用性？\n\n### 4. 格式合规\n- 正文是否 ≤ 8 页？\n- 引用格式是否正确？\n- Limitations section 是否合规？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1: ...\nS2: ...\n\n## Weaknesses\nW1: [severity: must-fix/should-fix/minor] ...\nW2: ...\n\n## Questions\nQ1: ...\n\n## Missing References\nMR1: ...\n\n## Minor Issues\nM1: ...\n\n## Overall Assessment\n- Soundness: X/5\n- Excitement: X/5\n- Overall: X/5\n- Confidence: X/5\n- 推荐：strong reject / weak reject / borderline / weak accept / strong accept\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- Long Paper：正文 8 页限制，参考文献不限，附录不计入页数\n- 模板：ACL style（`\\usepackage[review]{acl}`）\n- 匿名审稿（double-blind）\n- 必须包含 Limitations section\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 主文件：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_12/submitted.pdf`\n- 总页数：29 页（正文 + 参考文献 + 附录）\n\n## 你的审查侧重\n\n### 1. 理论严谨性\n- Proposition 1 (sign preservation) 的证明是否完整？条件 (a)(b)(c) 是否充分？\n- Theorem 1 (envelope monotonicity) 仅限 K=2——K≥3 依赖 Observation 1 和 Conjecture 1（数值验证）。这个证据层次（Proved/Verified/Conjectured）是否清晰且诚实？\n- λ(C) ∈ [0,1] 在 proportional effects 下成立，但 general case 15-17% 违反。这对 mediation 结论的影响？\n- Conjecture 1 的 ε-approximate monotonicity（ε<0.06）验证规模是否充分？\n\n### 2. 假设合理性\n- Non-differential misclassification (Definition 1)：在 LLM 场景下是否合理？stress test (Appendix B.5) 是否充分覆盖了结构化违反模式（outcome-conditional、label-specific）？\n- Proportional effects (f=λg)：在 NLP 应用中是否可验证？23 个 LLM 配置的经验验证是否充分？\n- 线性 SEM 假设：对 EMNLP 读者是否有足够的动机解释？logistic DGP 结果是否应更突出？\n\n### 3. 实验设计\n- Monte Carlo 验证（MAPE 1.6%）是否有统计量不足的 topology？\n- 23 个 LLM 配置（4 个 7-235B 模型 × 3 任务）是否充分？缺少商业 API 和 >70B 模型。\n- 校正方法比较（Table 4/Appendix）仅用 K=3——FWL invariance 与 K 无关，但 PPI++/MC-SIMEX 排名可能随 K 变化。\n- ASV bootstrap CI 过宽（exposure: [0.60, 1.36]，IV: [0.44, 1.29]）——实践可用性？\n\n### 4. 格式合规\n- 正文是否 ≤ 8 页？\n- 引用格式是否正确？\n- Limitations section 是否合规？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1: ...\nS2: ...\n\n## Weaknesses\nW1: [severity: must-fix/should-fix/minor] ...\nW2: ...\n\n## Questions\nQ1: ...\n\n## Missing References\nMR1: ...\n\n## Minor Issues\nM1: ...\n\n## Overall Assessment\n- Soundness: X/5\n- Excitement: X/5\n- Overall: X/5\n- Confidence: X/5\n- 推荐：strong reject / weak reject / borderline / weak accept / strong accept\n```"
  }
}
````

</details>

---


### Tool result

_source line 957 · 2026-05-23T06:29:13.218068+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25596
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-23T06:29:15.429158+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- Long Paper：正文 8 页限制，参考文献不限，附录不计入页数\n- 模板：ACL style（`\\usepackage[review]{acl}`）\n- 匿名审稿（double-blind）\n- 必须包含 Limitations section\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 主文件：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_12/submitted.pdf`\n- 总页数：29 页\n\n## 你的审查侧重\n\n### 1. 贡献新颖性\n- 三个贡献（bias taxonomy / ASV / correction guidance）的新颖性程度？\n- ASV 与 E-value (VanderWeele & Ding 2017) 的方法论差异是否充分论证？论文声称 ASV 将 K²-维问题降为 1D，且 sign-flip ASV 无 E-value 对应——是否令人信服？\n- FWL invariance 结果（4 种 topology 下 matrix-based correction 0% bias reduction）是否足够 surprising？\n- 与 Teblunthuis (2024)（binary, 4 DAGs）和 Lee & Wood-Doughty (2024)（categorical, 1 DAG）相比，本文的增量贡献是否值得 EMNLP 长文？\n- \"first unified analysis\" 的声明是否准确且恰当？\n\n### 2. 相关工作完整性\n- 检查是否遗漏重要相关工作，特别是：\n  - Prediction-powered inference 系列（Angelopoulos 2023, Zrnic & Candes 2024, Demirel et al. 2024, Cadei et al. 2025）\n  - 测量误差文献（Carroll et al. 2006, Gustafson 2004, Buonaccorsi 2010）\n  - 敏感性分析（Rosenbaum 2002, Mathur et al. 2018, Cinelli & Hazlett 2020）\n  - LLM 标注质量（Baumann 2025, Kim & Garg 2025, Pangakis et al. 2023）\n  - 是否遗漏其他关键工作？\n\n### 3. 写作质量与呈现\n- Abstract 信息密度（包含多少个具体数字？是否过载？）\n- Introduction 的叙事结构——从问题到贡献的逻辑流是否清晰？\n- Method section 对 EMNLP 读者的可读性（plim/FWL 等计量经济学概念是否有足够解释？）\n- Experiments section 的结构（是否清晰区分理论验证和实证验证？）\n- Figure/Table 质量和信息量\n- Limitations section 是否充分但简洁？\n\n### 4. 对 EMNLP 社区的适配性\n- 论文的主要受众是 CL/NLP 研究者还是统计学家？是否对正确的读者群体发声？\n- 实践指导（Algorithm 1、correction guidance）对 NLP practitioners 的可用性？\n- 案例研究（ClinicalBERT、political ad tone）是否有效展示了实际应用？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1: ...\nS2: ...\n\n## Weaknesses\nW1: [severity: must-fix/should-fix/minor] ...\nW2: ...\n\n## Questions\nQ1: ...\n\n## Missing References\nMR1: ...\n\n## Minor Issues\nM1: ...\n\n## Overall Assessment\n- Soundness: X/5\n- Excitement: X/5\n- Overall: X/5（使用 EMNLP 2026 ARR 评分标准）\n- Confidence: X/5\n- 推荐：strong reject / weak reject / borderline / weak accept / strong accept\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- Long Paper：正文 8 页限制，参考文献不限，附录不计入页数\n- 模板：ACL style（`\\usepackage[review]{acl}`）\n- 匿名审稿（double-blind）\n- 必须包含 Limitations section\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 主文件：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_12/submitted.pdf`\n- 总页数：29 页\n\n## 你的审查侧重\n\n### 1. 贡献新颖性\n- 三个贡献（bias taxonomy / ASV / correction guidance）的新颖性程度？\n- ASV 与 E-value (VanderWeele & Ding 2017) 的方法论差异是否充分论证？论文声称 ASV 将 K²-维问题降为 1D，且 sign-flip ASV 无 E-value 对应——是否令人信服？\n- FWL invariance 结果（4 种 topology 下 matrix-based correction 0% bias reduction）是否足够 surprising？\n- 与 Teblunthuis (2024)（binary, 4 DAGs）和 Lee & Wood-Doughty (2024)（categorical, 1 DAG）相比，本文的增量贡献是否值得 EMNLP 长文？\n- \"first unified analysis\" 的声明是否准确且恰当？\n\n### 2. 相关工作完整性\n- 检查是否遗漏重要相关工作，特别是：\n  - Prediction-powered inference 系列（Angelopoulos 2023, Zrnic & Candes 2024, Demirel et al. 2024, Cadei et al. 2025）\n  - 测量误差文献（Carroll et al. 2006, Gustafson 2004, Buonaccorsi 2010）\n  - 敏感性分析（Rosenbaum 2002, Mathur et al. 2018, Cinelli & Hazlett 2020）\n  - LLM 标注质量（Baumann 2025, Kim & Garg 2025, Pangakis et al. 2023）\n  - 是否遗漏其他关键工作？\n\n### 3. 写作质量与呈现\n- Abstract 信息密度（包含多少个具体数字？是否过载？）\n- Introduction 的叙事结构——从问题到贡献的逻辑流是否清晰？\n- Method section 对 EMNLP 读者的可读性（plim/FWL 等计量经济学概念是否有足够解释？）\n- Experiments section 的结构（是否清晰区分理论验证和实证验证？）\n- Figure/Table 质量和信息量\n- Limitations section 是否充分但简洁？\n\n### 4. 对 EMNLP 社区的适配性\n- 论文的主要受众是 CL/NLP 研究者还是统计学家？是否对正确的读者群体发声？\n- 实践指导（Algorithm 1、correction guidance）对 NLP practitioners 的可用性？\n- 案例研究（ClinicalBERT、political ad tone）是否有效展示了实际应用？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1: ...\nS2: ...\n\n## Weaknesses\nW1: [severity: must-fix/should-fix/minor] ...\nW2: ...\n\n## Questions\nQ1: ...\n\n## Missing References\nMR1: ...\n\n## Minor Issues\nM1: ...\n\n## Overall Assessment\n- Soundness: X/5\n- Excitement: X/5\n- Overall: X/5（使用 EMNLP 2026 ARR 评分标准）\n- Confidence: X/5\n- 推荐：strong reject / weak reject / borderline / weak accept / strong accept\n```"
  }
}
````

</details>

---


### Tool result

_source line 959 · 2026-05-23T06:29:16.944386+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1515
}
```

</details>

---


### Assistant

_source line 960 · 2026-05-23T06:29:28.190551+00:00_

**Round 1 审稿已启动：**
- Reviewer 1（方法严谨性）：理论证明、假设合理性、实验设计
- Reviewer 2（新颖性与完整性）：贡献定位、相关工作、写作质量
- 视觉审查 Agent：已并行派发

等待两位 Reviewer 返回审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 90

## Round 90

2 recorded events


### User

_source line 961 · 2026-05-23T06:34:13.370377+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（方法严谨性）

---

## Summary

本文研究 K 类标注错误（以 LLM 标注为典型场景）在因果推断中的传播机制。作者推导了 7 种典型 DAG 拓扑下的闭式偏差表达式，建立了符号保持条件（Proposition 1）和包络单调性结果（Theorem 1, K=2），提出了 Annotation Sensitivity Values (ASV) 敏感性分析框架，并在 23 个 LLM 配置和 3 个 NLP 任务上进行了经验验证。论文还评估了 5 种校正方法（naive plug-in, MLA, DSL, MC-SIMEX, PPI++），证明了 FWL 不变性对协变量拓扑的精确 0% 偏差消减。

---

## Strengths

**S1: 拓扑依赖框架的系统性与新颖性。** 将混淆矩阵 C 与 DAG 拓扑的交互效应作为核心分析维度是本文最重要的贡献。先前工作（Bound et al., 2001; Gustafson, 2004; Lee and Wood-Doughty, 2024）通常只处理单一拓扑或 K=2 场景，本文系统覆盖 7 种拓扑并推导出闭式表达式，揭示了"同一混淆矩阵在不同拓扑下产生质的不同偏差"这一非平凡发现（Section 1, "topology, not annotator quality, determines downstream risk"）。

**S2: 证据层次的诚实标注。** 论文对 K=2 的 Theorem 1 提供完整证明（Appendix A.4），对 K≥3 明确区分了 "Proved"（Proposition 1-6）、"Numerically Verified"（Observation 1, 20,000+ 配置）和 "Conjectured"（Conjecture 1, ε<0.06）三个层次。Table 2 (p.5) 对每个拓扑的充分条件和验证状态做了清晰汇总。这种诚实的分层陈述在方法论上值得肯定。

**S3: 理论-模拟一致性极强。** 100,000 次 Dirichlet 随机矩阵的 Monte Carlo 验证与解析预测的 MAPE 为 1.6%，覆盖 161 个场景（Section 4.2, Table 1）。这为闭式表达式的正确性提供了强有力的数值支撑。

**S4: FWL 不变性的理论证明。** 证明矩阵校正对协变量拓扑（confounding, mediation, collider, M-bias）精确实现 0% 偏差消减（Appendix B.2, B.13），且将这一结论推广到逻辑回归（Table 5, Table 13），是一个 clean 且实用的理论贡献。

**S5: ASV 框架实用性。** 三种互补的 ASV 指标（magnitude, significance, sign-flip）提供了从不同角度量化标注敏感性的工具包，Figure 4 (p.7) 的可视化直观展示了跨拓扑的脆弱性排序。

---

## Weaknesses

**W1 [must-fix]: Theorem 1 仅适用于 K=2，核心多类结果停留在 Conjecture 层面。**

- 具体位置：Section 3.3, Theorem 1 (p.5); Conjecture 1 (p.5); Appendix B.11
- 问题：论文标题强调 "Multi-Class Annotation Errors"，但核心单调性定理 (Theorem 1) 仅对 K=2 成立。K≥3 的单调性完全依赖数值验证 (Observation 1) 和猜想 (Conjecture 1, ε-approximate monotonicity with ε<0.06)。虽然 Conjecture 1 在 30,000 随机矩阵 × K∈{3,5,7} × 7 拓扑下验证通过（Table 10, Appendix B.11, worst single-step deviation ≈0.01-0.017），但这仍是数值证据而非证明。
- 为什么影响接收：审稿人和读者会追问——如果 K≥3 的单调性只是 conjecture，那么基于 ASV 的实践指导（Algorithm 1, p.29）在 K≥3 时的理论保证是什么？论文对此未充分讨论。
- 建议修改方向：(i) 在正文中更明确地讨论 Conjecture 1 失效时对 ASV 实践指导的影响范围；(ii) 如果能提供 K=3 的部分解析结果（即使需要更强的条件），将显著加强论文；(iii) 至少应讨论为什么 K≥3 的证明困难——是纯粹的维度问题还是存在结构性障碍？

**W2 [must-fix]: 非差异性错分假设 (Definition 1) 在 LLM 场景下的合理性论证不足。**

- 具体位置：Section 3.1, Definition 1 (p.3); Appendix B.5 (p.23); Appendix B.15 (p.28)
- 问题：Definition 1 要求 P(A*|A,Y,Z) = P(A*|A)，即错分独立于 outcome 和协变量。但 LLM 标注场景中，错分几乎必然是差异性的：(a) 某些文本特征同时影响 LLM 标注质量和 outcome（例如，复杂语句更难分类且与特定 outcome 相关）；(b) LLM 在不同类别上的错误率通常不对称（label-specific bias）。Appendix B.5 的 stress test 在 ε=0.50 时违反率高达 54.6%（label-specific 模式），ε=0.10 时也达 7.6 pp。但 stress test 仅覆盖 K=3 和两种违反模式（outcome-conditional, label-specific），且违反结构较为程式化。
- 为什么影响接收：对于 EMNLP 读者，LLM 标注是核心应用场景。如果该假设在目标场景下系统性不成立，论文的实用价值将大打折扣。Appendix B.15 测量了 23 个经验混淆矩阵的差异性阈值（ε*），但仅报告了每个矩阵"在 sign reversal 前可容忍的最大 ε"，未直接估计实际 LLM 系统中 ε 的典型取值范围。
- 建议修改方向：(i) 从已有的 23 个 LLM 配置中，直接估计经验差异性程度（即衡量 P(A*|A,Y) vs P(A*|A) 的偏离），以此判断 stress test 的 ε 范围是否覆盖了实际场景；(ii) 讨论 Messing (2026) 或类似工作中提出的差异性错分校正方法是否可以嵌入本框架。

**W3 [should-fix]: 线性 SEM 假设对 NLP 应用的适用性缺乏动机论证。**

- 具体位置：Section 3.1 (p.3, "linear structural equation models"); Appendix B.6 (p.21, logistic DGP); Table 5 (p.22)
- 问题：全文理论框架基于线性 SEM（Y = τT + f(A) + εY），但 NLP 应用中变量关系通常高度非线性。虽然 Appendix B.6/B.13/Table 5/Table 13 验证了逻辑回归下的 FWL 不变性和校正有效性，但这些结果在正文中几乎没有讨论（仅 Section 4.5 一句 "structural patterns persist under logistic regression"）。Table 5 显示 collider 和 M-bias 在 N=10,000 时标准差高达 2.6 stl（论文称 "rare outlier replicates"），这一解释过于简略。
- 建议：(i) 在正文 Method 或 Experiments 部分用 1-2 段明确讨论线性假设的适用边界和非线性扩展方向；(ii) 将 Table 5 或 Table 13 的关键结果提升到正文或至少在正文中给出更详细的引用讨论。

**W4 [should-fix]: 校正方法比较仅在 K=3 下进行。**

- 具体位置：Table 4 (p.8); Appendix B.14 (p.27)
- 问题：Table 4 的校正方法 RMSE 对比仅覆盖 K=3, N=1,000。虽然 FWL 不变性与 K 无关（Appendix B.2 已证），但 PPI++ 和 MC-SIMEX 的相对性能可能随 K 变化。特别是 PPI++ 在 K>3 时需要更多 gold labels（Table 14 显示 gold label fraction 对 RMSE 的影响），MC-SIMEX 的外推精度也可能因 K 增大而下降。
- 建议：补充 K=5 或 K=7 的校正方法对比，至少在附录中验证排名稳定性。

**W5 [should-fix]: ASV bootstrap CI 过宽，实践可操作性存疑。**

- 具体位置：Section 4.3 (p.6-7); Appendix B.7 (p.21-22); Figure 4 (p.7)
- 问题：Exposure ASV bootstrap CI 为 [0.60, 1.36]，IV 为 [0.44, 1.29]（Section 4.3, p.7 注释）。以 magnitude ASV 为例，exposure 的 CI 跨越了 "safe"（<1）和 "amplifying"（>1）的分界线，使从业者无法据此做出明确决策。Appendix B.7 的 bootstrap 分析（D=1,000 resample, replacement D=1,000）确认了 CI 宽度，但未提供缩窄 CI 的具体方案。
- 建议：(i) 讨论样本量 N 或 gold label 比例对 CI 宽度的影响；(ii) 考虑 CI 是否可以通过 parametric bootstrap 或 profiling 方法缩窄；(iii) 在 Algorithm 1 (p.29) 的实践指导中增加 "CI 过宽时应如何决策" 的指导。

**W6 [should-fix]: LLM 配置覆盖度不足。**

- 具体位置：Section 4.4 (p.8); Appendix B.9 (p.25)
- 问题：23 个 LLM 配置来自 4 个模型（Llama-3-Maverick, Qwen2.5-3B, DeepSeek-Chat, Qwen2.5-7B-Instruct）× 3 个任务。缺少：(a) 商业 API 模型（GPT-4, Claude），这些是 NLP 实践中最常用的标注工具；(b) 参数量 >235B 的模型（虽然 235B 已较大，但 flagship 模型行为可能不同）；(c) 3 个任务均为分类任务，未覆盖 NER、relation extraction 等结构化标注场景。
- 建议：至少讨论为何排除商业 API 模型，以及是否有理由认为结论可泛化到这些场景。

---

## Questions

**Q1:** Theorem 1 证明使用了 perspective function convexity（Appendix A.4, "V_D(δ) is convex"）。能否提供 K≥3 证明困难的解析直觉？是否因为 K≥3 时 C 的 off-diagonal 自由度增加导致凸性不再全局成立？

**Q2:** Appendix B.15 (Table 15) 报告了 23 个经验混淆矩阵的差异性阈值 ε*，但这些阈值衡量的是"在 sign reversal 前可容忍的最大 ε"。能否直接从原始标注数据中估计实际差异性程度（即 P(A*|A,Y) 与 P(A*|A) 的经验偏离）？这将使 stress test 的参数选择更有实际依据。

**Q3:** ASV 案例研究（Appendix B.17, 政治广告分类, K=3）识别出 exposure 是最脆弱的拓扑。对于更细粒度的标注方案（K=5, K=10），ASV 排名是否稳定？Table 9 (Appendix B.10) 仅报告了 magnitude ASV 跨 DGP 的稳定性，未系统分析 K 的影响。

**Q4:** λ(C) 的 out-of-bounds 率在 general case 下为 15-17%（Table 12, Appendix B.12）。当 λ(C)∉[0,1] 时，mediation 拓扑的偏差表达式（Section 3.2, plim τ̂_direct(A*)）中 λ(C) 的物理含义是什么？论文是否应更明确地限定 mediation 结论的适用条件？

**Q5:** Proposition 3（Confounding sign preservation, general case）中 worst-case bound B̃ 使用了 Cauchy-Schwarz，这是一个 loose bound。在实际 LLM 混淆矩阵上，|R(C)| 与 B̃ 的比值分布如何？是否存在许多 "near-boundary" 情况导致实践中符号保持判定不确定？

---

## Missing References

**MR1:** Schennach (2020) 的 measurement error in nonlinear/semiparametric models 综述——论文假设线性 SEM 但声称对 NLP 应用有指导意义，应讨论非线性扩展的可能性和挑战。

**MR2:** Si et al. (2023, "Can ChatGPT Replace Traditional Annotation Pipelines?") 或类似的大规模 LLM 标注质量评估工作——可补充 LLM 差异性错分的经验证据。

---

## Minor Issues

**M1:** Figure 2 (p.7) 标注 "Red = sign reversal" 但 Figure 2 实际在 p.7 底部，与 Figure 1 (p.7 顶部) 的 DAG 图相邻。两图挤在同一页且 caption 字号较小，建议调整间距。

**M2:** Algorithm 1 (p.29) 使用硬编码的 RMSE 阈值（如 "RMSE red. ≥ 47.0%" 对应 MC-SIMEX），这些阈值来源于 Table 4 (K=3) 的具体数值。如果 K 改变，这些阈值是否仍然有效？应标注适用条件。

**M3:** Notation: Section 3.2 使用 f(A) 和 g(A) 表示 misclassification 对结构方程的效应（p.3），但 f 和 g 的精确定义分散在 Appendix A.1-A.3 的各拓扑推导中（例如 Appendix A.3 p.12 for confounding），正文中应提供更集中的符号定义。

**M4:** p.5 "ε < 0.06 at default DGP parameters" — "default DGP parameters" 在正文中未给出（需参照 Appendix B.11 Table 10 的脚注），建议正文给出简要说明或引用。

---

## Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2 结果严格证明，K≥3 有充分数值支持但核心单调性停留在 conjecture；非差异性假设 stress test 覆盖度可接受但不完整；线性 SEM 下的推导无误 |
| Excitement | 3.5/5 | 拓扑依赖框架是真正的新视角，连接了测量误差理论和 DAG 结构；ASV 有实用价值；但受线性假设和 K=2 限制约束了影响范围 |
| Reproducibility | 4/5 | 闭式表达式可直接验证；声明代码和数据将公开发布；Monte Carlo 验证流程清晰（100,000 Dirichlet matrices, 161 scenarios） |
| Overall | 3.5/5 | Borderline Conference — 理论贡献真实但不完整（conjecture vs proof），实践适用性受假设约束 |
| Confidence | 4/5 | 仔细检查了核心证明（Appendix A.2-A.4）、Monte Carlo 验证设计、stress test 方法论和经验验证设计 |

**推荐：Borderline Conference (3.5)**

**一句话总结：** 拓扑依赖的多类错分偏差分析框架具有新颖性和系统性，K=2 的理论结果严格且有强数值支撑，但核心 K≥3 单调性结论停留在 conjecture 层面、非差异性假设在 LLM 场景下的合理性论证不充分，限制了论文作为 Conference paper 的说服力。

---

**审稿人声明：** 本审稿仅基于投稿 PDF 材料，未参考任何内部文件或代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 962 · 2026-05-23T06:34:29.632457+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 91

## Round 91

2 recorded events


### User

_source line 963 · 2026-05-23T06:34:35.462969+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Borderline Conference (3.5/5)**。

两个 must-fix 问题：
1. **Theorem 1 仅限 K=2**，K≥3 多类场景的核心单调性停留在 Conjecture 层面（数值验证充分但无解析证明），与标题承诺存在落差
2. **非差异性错分假设在 LLM 场景下论证不足**，stress test 覆盖度可接受但未直接估计实际 LLM 系统的差异性程度

四个 should-fix 问题：线性 SEM 动机不足、校正方法仅比较 K=3、ASV bootstrap CI 过宽影响可操作性、LLM 配置缺少商业 API 模型。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 964 · 2026-05-23T06:34:40.661193+00:00_

等待 Reviewer 2 的审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 92

## Round 92

6 recorded events


### User

_source line 965 · 2026-05-23T06:36:19.196281+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性与完整性

---

## Summary

本文研究多类别（K≥3）LLM 标注误差在因果推断中的传播问题，覆盖 7 种 DAG 拓扑结构，推导出拓扑依赖的偏差表达式，提出 Annotation Sensitivity Values (ASV) 框架用于量化敏感性，并评估 5 种校正方法。核心发现包括：K≥3 引入 binary 不存在的符号反转（sign reversal）现象、基于矩阵的校正因 FWL 不变性在 4 种拓扑下完全无效、PPI++ 是最有效的校正方法。

---

## Strengths

**S1: 系统性覆盖填补了真实空白。** Teblunthuis (2024) 仅覆盖 binary×4 DAGs，Lee &amp; Wood-Doughty (2024) 仅覆盖 categorical×1 DAG（confounding）。本文将两个维度同时扩展至 K≥3×7 topologies，并在每个交叉点提供了解析偏差表达式（Section 3.2, Appendix A.3–A.8）。这不是简单的排列组合——K≥3 下 stochastic constraint 打破了 2×2 矩阵的结构保证（Section 3.2, Proposition 1(c)），使 sign reversal 成为可能，这是本文最重要的理论发现。83.4% 的 K≥3 exposure 混淆矩阵至少有一个 secondary coefficient 发生符号反转（Section 4.2），这一数字令人印象深刻。

**S2: ASV 框架设计合理且实用。** 三种 ASV 类型（magnitude, significance, sign-flip）对应不同的实践需求，K²→1D 降维通过 diagonal scaling δ 实现（Section 3.3）。Sign-flip ASV 识别临界样本量 N*——低于此阈值所有 rejection 被阻断——这在 E-value 框架中确实没有直接对应物（E-value 针对 unmeasured confounding 而非 measurement error）。Figure 4（p7）的 ASV 跨拓扑排名提供了清晰的 vulnerability spectrum。

**S3: FWL 不变性是一个干净且有实践价值的负面结果。** 证明基于 column-space equivalence（col(D*·M) = col(D*)，Appendix B.2），表明 matrix-based correction（MLA, DSL）在 confounding/mediation/collider/M-bias 下 0% bias reduction（Table 4, p8）。这直接驳斥了"有混淆矩阵估计就能校正"的朴素假设，对 NLP practitioners 有重要的实操指导意义。

**S4: 附录材料详实。** 19 页附录包含完整证明（Appendix A）、大量数值验证（Appendix B）、扩展实验（B.5 非差异性假设压力测试, B.13 FWL 非线性模型, B.14 PPI++ 金标敏感性）。Reproducibility 条件充分。

**S5: Algorithm 1 提供了可直接使用的决策流程。** 从拓扑识别→ASV 计算→校正方法选择的完整 pipeline（p29），对 NLP 从业者友好。

---

## Weaknesses

**W1 [severity: should-fix] Conjecture 1 未证明，削弱理论贡献的完整性。**
- 具体位置：Section 3.3, Conjecture 1（p5）；Appendix B.11
- 问题：Envelope monotonicity（非 IV 拓扑下 ε-approximate）是 ASV 框架的关键支撑——它保证 ASV 阈值有意义。但这一结果仅以 Conjecture 形式给出，通过 100,000 随机矩阵数值验证。对于一篇以理论分析为核心卖点的论文，关键结果停留在 conjecture 层面有些遗憾。
- 建议：(a) 尝试为特定拓扑（如 confounding）给出解析证明，即使 general case 保留 conjecture；(b) 至少更明确地说明 conjecture 失败的后果——如果 monotonicity 不成立，ASV 的实践建议具体会如何受影响？

**W2 [severity: should-fix] Abstract 信息密度过高，可读性受损。**
- 具体位置：Abstract（p1）
- 问题：单段 abstract 中塞入了至少 9 个具体数字/百分比（K², 1D, 83.4%, K≥3, 2×2, 0%, 47.0%, 1.65×, 161 scenarios）。对于不熟悉该领域的 EMNLP 读者，首次接触就被数字淹没，难以抓住核心 message。
- 建议：Abstract 聚焦 2-3 个最有冲击力的数字（如 sign reversal 的 83.4% 和 FWL 的 0%），其余移至 Introduction 或 Experiments。

**W3 [severity: should-fix] 计量经济学术语对 EMNLP 受众的可及性不足。**
- 具体位置：Section 3 整体，特别是 Section 3.1（plim）, Section 3.2（FWL decomposition）
- 问题：plim（probability limit）、Frisch-Waugh-Lovell (FWL) theorem、Bias decomposition 等是计量经济学标准工具，但对 CL/NLP 社区并非常识。Section 3.1 对 plim 仅一笔带过（"the probability limit of the OLS estimator"），未解释其直觉含义（大样本下估计量收敛到的值）。FWL 定理在 Section 4.5 首次使用时才引用，但早在 Appendix A 的证明中就大量依赖。
- 为什么影响评分：EMNLP reviewers 可能因无法跟上推导而低估论文贡献。
- 建议：在 Section 3.1 增加 1-2 句直觉解释（如 "plim identifies the systematic bias component that persists regardless of sample size"），并在首次使用 FWL 时简要说明其核心思想（"partialling out controls"）。

**W4 [severity: should-fix] 实证验证规模有限，与理论覆盖面不匹配。**
- 具体位置：Section 4.4（p8）；Appendix B.3, B.17
- 问题：论文理论覆盖 7 topologies × K≥3 × 多种混淆矩阵参数化，但实证验证仅用 23 个经验混淆矩阵（来自 3 个 NLP 任务：HumAID K=10, VAST K=5, CivilComments K=2）。其中 CivilComments 实际是 K=2（binary），与论文 K≥3 的核心贡献不完全对齐。ClinicalBERT 案例（Appendix B.3, p22）和 Political Ad Tone 案例（Appendix B.17, p28）虽然有意义，但均为回顾性应用（retrospective），未在真实因果推断流程中端到端验证。
- 建议：(a) 增加更多 K≥3 的真实混淆矩阵（如从 Baumann 2025 或其他 LLM annotation benchmarks 获取）；(b) 如果时间允许，做一个前瞻性（prospective）案例——在一个实际因果分析任务中，先用 ASV 预判风险，再观察实际偏差，验证 ASV 的预测准确性。

**W5 [severity: minor] "First unified analysis" 声明可以更精确。**
- 具体位置：Abstract ("first unified analysis"), Introduction（p2, "We address these gaps with three contributions"）
- 问题："First unified analysis" 在技术上可辩护（确实没有先前工作同时覆盖 K≥3 × 7 topologies × sensitivity × correction），但措辞略显 broad。读者可能质疑 "unified" 的边界——论文并未覆盖 differential misclassification、non-linear outcome models（仅附录 B.13 简要讨论 logistic DGP）、或连续误差变量。
- 建议：改为 "first systematic analysis of multi-class non-differential misclassification across multiple causal DAG topologies" 或类似表述，明确限定范围。

**W6 [severity: minor] Figure 2 视觉传达效率可提升。**
- 具体位置：Figure 2（p7）
- 问题：7 个拓扑的 bias distribution 用 violin/box plot 展示，但红色 "sign reversal" 标记的含义需要仔细阅读 caption 才能理解。Exposure 的 violin plot 视觉上与 Confounding 差异不大，但文本强调它们有本质区别。
- 建议：考虑用 dual-panel 设计——左 panel 显示 bias magnitude，右 panel 显示 sign reversal rate——使核心发现（topology determines sign reversal vulnerability）更直接可见。

---

## Questions

**Q1**: Proposition 1 的 sign preservation conditions（Table 2, p20）依赖于混淆矩阵 C 的 column-stochasticity 和对角优势条件。在实际 LLM 标注场景中，这些条件多常被满足？Table 15（p28）报告了 23 个经验矩阵的检验结果，但样本量太小无法得出可靠结论。作者是否有更大规模的经验证据？

**Q2**: ASV 的 diagonal parameterization（C(δ) = (1-δ)I + δC₀）隐含假设所有类别的误分类率以相同比例退化。这在实际中是否合理？如果某些类别的标注质量比其他类别差得多（如稀有类别），这种 1D 降维是否会遗漏关键信息？

**Q3**: FWL 不变性结果限于线性模型（OLS, logistic regression 在 Appendix B.13 有简要讨论）。对于现代 NLP 中更常见的非参数/半参数因果推断方法（如 doubly robust estimators, TMLE），这一不变性是否仍然成立？这关系到 Algorithm 1 对非线性管道的适用性。

**Q4**: PPI++ 需要 gold labels 用于子集。Appendix B.14（p27）显示 gold label 比例从 5% 到 50% 的 RMSE reduction 变化，但实际中获取 gold labels 的成本如何？Algorithm 1 中在什么条件下推荐 PPI++ vs 其他方法的决策边界是否需要 cost-aware？

---

## Missing References

**MR1**: 本文讨论 IV 拓扑下 Wald estimator 的脆弱性（Section 3.2, p4; Table 1, Figure 3），但未引用弱工具变量（weak instruments）文献。Stock &amp; Yogo (2005, "Testing for weak instruments in linear IV regression") 和 Andrews, Stock &amp; Sun (2019, "Weak instruments in IV regression") 直接相关——Wald estimator 在弱 IV 下的不稳定性是已知问题，论文应讨论 annotation error 与 weak IV 问题的交互作用。

**MR2**: Mediation topology 的讨论缺少对 VanderWeele (2015, "Explanation in Causal Inference") 的引用，这是因果中介分析的标准参考。论文的 mediation bias decomposition（Appendix A.5）与该书 Chapter 2 的框架有直接对应关系。

**MR3**: 在 Related Work 中，prediction-powered inference 部分可补充 Egami et al. (2024, "Using imperfect surrogates for downstream inference") 的讨论——该工作也 address surrogate-based estimation 但从不同角度。（注：检查后发现该文已被引用于 Section 2，此条撤回。）

**MR3 (revised)**: 考虑引用 Mozer et al. (2023) 或类似工作关于 LLM annotation 的 inter-annotator agreement 与 systematic bias 的区分——这与论文的 non-differential misclassification 假设直接相关。

---

## Minor Issues

**M1**: Footnote 1（p2）定义 "ratio of maximum to minimum bias" 但公式使用了绝对值比，可能与文本描述不完全一致——建议核实。

**M2**: Section 3.3（p5）parameterization 公式 C(δ) = (1-δ)I + δC₀ 在 δ=0 时给出 identity matrix（完美分类），δ=1 时给出 C₀。文中用 δ ∈ [0,1] 但图 4 的 x 轴标注不够清晰。

**M3**: Algorithm 1（p29）的 Step 2 中阈值 "RMSE red. ≥ 10%" 的来源不明——这是经验选择还是有理论依据？

**M4**: References 中 Brenner (1993) 出现两次（p9 和 p11），格式略有不同，确认是否为同一文献的重复引用。

**M5**: 论文正文（Sections 1-5, 不含 Limitations）结束于 page 9 上方——结论段从 page 8 延伸至 page 9 前几行。在严格 8 页限制解读下，这可能构成格式违规。建议压缩结论段使其完全落在 page 8 内。

---

## Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 理论推导严谨，附录证明完整，Monte Carlo 验证充分。主要扣分点：Conjecture 1 未证明；non-differential misclassification 假设的 stress test（Appendix B.5）显示 ε=0.10 时 violation rate 升至 7.6%，但论文对此讨论不够。 |
| Excitement | 3.5/5 | 问题重要且 timely（LLM annotation 广泛使用），sign reversal 发现和 FWL 不变性结果有实践价值。但对 EMNLP 受众的直接兴奋度受限于重度计量经济学形式——更多 NLP 社区读者可能觉得这是一篇"应该发在统计/因果推断 venue"的论文。 |
| Reproducibility | 4/5 | 详细的模拟参数（Appendix A.3 extension to K>3, Appendix B.1 binarization collapse），承诺代码公开，Algorithm 1 伪代码完整。扣分：empirical confusion matrices 的来源和预处理细节可更明确。 |
| Overall | 3.5/5 | **Borderline Conference。** 贡献实质性——将 binary/single-DAG 先前工作统一并扩展至 K≥3×7 topologies 是有意义的推进，ASV 框架和 FWL 不变性结果均有独立价值。主要顾虑：(1) 对 EMNLP 受众的可及性不足（W3），(2) 实证验证规模偏小（W4），(3) Conjecture 1 未证明（W1）。如果 W3 和 W4 能得到改善，论文可达到 4/5 水平。 |
| Confidence | 4/5 | 我对因果推断和测量误差文献有较好了解，仔细阅读了正文和附录。对 FWL 和 PPI++ 的技术细节有足够背景判断其正确性。 |

### 最终推荐
**Borderline Accept (weak accept)**。论文在一个重要且 timely 的问题上做出了系统性贡献，理论分析扎实，实践指导明确。主要瓶颈在于写作的可及性和实证验证的广度——这些是 camera-ready 阶段可以改善的，不构成根本性缺陷。如果是 Findings track，我会明确推荐接收；对于主会议，取决于其他 reviewer 对可及性问题的评价。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-23T06:37:03.450262+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\n本文研究 K 类标注错误在因果推断中的传播机制。作者推导了 7 种典型 DAG 拓扑下的闭式偏差表达式，建立了符号保持条件（Proposition 1）和包络单调性结果（Theorem 1, K=2），提出了 ASV 敏感性分析框架，并在 23 个 LLM 配置和 3 个 NLP 任务上进行了经验验证。还评估了 5 种校正方法，证明了 FWL 不变性对协变量拓扑的精确 0% 偏差消减。\n\n### Strengths\nS1: 拓扑依赖框架的系统性与新颖性——将混淆矩阵 C 与 DAG 拓扑的交互效应作为核心分析维度是最重要的贡献。\nS2: 证据层次的诚实标注——Proved/Verified/Conjectured 三级层次清晰。\nS3: 理论-模拟一致性极强——MAPE 1.6%，覆盖 161 个场景。\nS4: FWL 不变性的理论证明——clean 且实用。\nS5: ASV 框架实用性——三种互补指标。\n\n### Weaknesses\nW1 [must-fix]: Theorem 1 仅适用于 K=2，核心多类结果停留在 Conjecture 层面。K≥3 的单调性完全依赖数值验证和猜想。如果 K≥3 的单调性只是 conjecture，基于 ASV 的实践指导在 K≥3 时的理论保证是什么？\nW2 [must-fix]: 非差异性错分假设在 LLM 场景下的合理性论证不足。Appendix B.5 的 stress test 在 ε=0.50 时违反率高达 54.6%。未直接估计实际 LLM 系统中 ε 的典型取值范围。\nW3 [should-fix]: 线性 SEM 假设对 NLP 应用的适用性缺乏动机论证。logistic DGP 结果在正文中几乎没有讨论。\nW4 [should-fix]: 校正方法比较仅在 K=3 下进行。PPI++ 和 MC-SIMEX 的相对性能可能随 K 变化。\nW5 [should-fix]: ASV bootstrap CI 过宽，实践可操作性存疑。Exposure [0.60, 1.36]，IV [0.44, 1.29]。\nW6 [should-fix]: LLM 配置覆盖度不足。缺少商业 API 模型（GPT-4, Claude）、>235B 模型、NER 等任务。\n\n### Questions\nQ1: K≥3 证明困难的解析直觉？\nQ2: 能否直接从原始标注数据估计实际差异性程度？\nQ3: ASV 排名随 K 变化是否稳定？\nQ4: λ(C)∉[0,1] 时 mediation 偏差表达式的物理含义？\nQ5: Proposition 3 的 Cauchy-Schwarz bound 在实际 LLM 矩阵上的 tightness？\n\n### Missing References\nMR1: Schennach (2020) 非线性测量误差综述\nMR2: Si et al. (2023) LLM 标注质量评估\n\n### Minor Issues\nM1: Figure 2 两图挤在同一页\nM2: Algorithm 1 硬编码阈值来自 K=3\nM3: f/g 定义分散在附录中\nM4: \"default DGP parameters\" 正文未说明\n\n---\n\n请对 R1 的每个 Weakness 和 Question 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\n本文研究 K 类标注错误在因果推断中的传播机制。作者推导了 7 种典型 DAG 拓扑下的闭式偏差表达式，建立了符号保持条件（Proposition 1）和包络单调性结果（Theorem 1, K=2），提出了 ASV 敏感性分析框架，并在 23 个 LLM 配置和 3 个 NLP 任务上进行了经验验证。还评估了 5 种校正方法，证明了 FWL 不变性对协变量拓扑的精确 0% 偏差消减。\n\n### Strengths\nS1: 拓扑依赖框架的系统性与新颖性——将混淆矩阵 C 与 DAG 拓扑的交互效应作为核心分析维度是最重要的贡献。\nS2: 证据层次的诚实标注——Proved/Verified/Conjectured 三级层次清晰。\nS3: 理论-模拟一致性极强——MAPE 1.6%，覆盖 161 个场景。\nS4: FWL 不变性的理论证明——clean 且实用。\nS5: ASV 框架实用性——三种互补指标。\n\n### Weaknesses\nW1 [must-fix]: Theorem 1 仅适用于 K=2，核心多类结果停留在 Conjecture 层面。K≥3 的单调性完全依赖数值验证和猜想。如果 K≥3 的单调性只是 conjecture，基于 ASV 的实践指导在 K≥3 时的理论保证是什么？\nW2 [must-fix]: 非差异性错分假设在 LLM 场景下的合理性论证不足。Appendix B.5 的 stress test 在 ε=0.50 时违反率高达 54.6%。未直接估计实际 LLM 系统中 ε 的典型取值范围。\nW3 [should-fix]: 线性 SEM 假设对 NLP 应用的适用性缺乏动机论证。logistic DGP 结果在正文中几乎没有讨论。\nW4 [should-fix]: 校正方法比较仅在 K=3 下进行。PPI++ 和 MC-SIMEX 的相对性能可能随 K 变化。\nW5 [should-fix]: ASV bootstrap CI 过宽，实践可操作性存疑。Exposure [0.60, 1.36]，IV [0.44, 1.29]。\nW6 [should-fix]: LLM 配置覆盖度不足。缺少商业 API 模型（GPT-4, Claude）、>235B 模型、NER 等任务。\n\n### Questions\nQ1: K≥3 证明困难的解析直觉？\nQ2: 能否直接从原始标注数据估计实际差异性程度？\nQ3: ASV 排名随 K 变化是否稳定？\nQ4: λ(C)∉[0,1] 时 mediation 偏差表达式的物理含义？\nQ5: Proposition 3 的 Cauchy-Schwarz bound 在实际 LLM 矩阵上的 tightness？\n\n### Missing References\nMR1: Schennach (2020) 非线性测量误差综述\nMR2: Si et al. (2023) LLM 标注质量评估\n\n### Minor Issues\nM1: Figure 2 两图挤在同一页\nM2: Algorithm 1 硬编码阈值来自 K=3\nM3: f/g 定义分散在附录中\nM4: \"default DGP parameters\" 正文未说明\n\n---\n\n请对 R1 的每个 Weakness 和 Question 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-23T06:37:26.857083+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23406
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-23T06:37:27.009393+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Summary\n本文研究多类别（K≥3）LLM 标注误差在因果推断中的传播，覆盖 7 种 DAG 拓扑，推导拓扑依赖偏差表达式，提出 ASV 框架，评估 5 种校正方法。核心发现：K≥3 引入 binary 不存在的 sign reversal、FWL 不变性使 4 种拓扑下 matrix-based correction 完全无效、PPI++ 最有效但 topology-dependent。\n\n### Strengths\nS1: 系统性覆盖填补真实空白——K≥3×7 topologies 扩展 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024)。83.4% sign reversal 令人印象深刻。\nS2: ASV 框架设计合理且实用——Sign-flip ASV 识别 N* 在 E-value 中无对应物。\nS3: FWL 不变性是干净且有实践价值的负面结果。\nS4: 附录材料详实——19 页完整证明和数值验证。\nS5: Algorithm 1 提供可直接使用的决策流程。\n\n### Weaknesses\nW1 [should-fix]: Conjecture 1 未证明，削弱理论贡献完整性。建议为特定拓扑（如 confounding）给出解析证明。\nW2 [should-fix]: Abstract 信息密度过高，至少 9 个数字。建议聚焦 2-3 个核心数字。\nW3 [should-fix]: 计量经济学术语对 EMNLP 受众可及性不足。plim、FWL 等未充分解释。\nW4 [should-fix]: 实证验证规模有限——23 个经验混淆矩阵，CivilComments 实际 K=2。未在真实因果推断流程中端到端验证。\nW5 [minor]: \"First unified analysis\" 声明可更精确。\nW6 [minor]: Figure 2 视觉传达效率可提升。\n\n### Questions\nQ1: Proposition 1 的 sign preservation conditions 在实际 LLM 场景中多常被满足？\nQ2: ASV 的 diagonal parameterization 假设所有类别误分类率以相同比例退化，是否遗漏关键信息？\nQ3: FWL 不变性对非参数/半参数因果推断方法（doubly robust, TMLE）是否仍成立？\nQ4: PPI++ gold labels 成本，Algorithm 1 是否需要 cost-aware？\n\n### Missing References\nMR1: Stock & Yogo (2005) 弱工具变量检验——与 IV 拓扑直接相关\nMR2: VanderWeele (2015) 因果中介分析标准参考\nMR3: Mozer et al. (2023) LLM annotation inter-annotator agreement 与 systematic bias\n\n### Minor Issues\nM1: Footnote 1 绝对值比与文本描述可能不一致\nM2: Figure 4 x 轴标注不够清晰\nM3: Algorithm 1 Step 2 阈值 \"RMSE red. ≥ 10%\" 来源不明\nM4: Brenner (1993) 可能重复引用\nM5: 正文可能超 8 页（结论段延伸至 page 9）\n\n### Overall Assessment\nSoundness 4/5, Excitement 3.5/5, Overall 3.5/5 (Borderline Conference)\n推荐：Borderline Accept (weak accept)——贡献实质性，主要顾虑为可及性和实证验证广度。\n\n---\n\n请对 R2 的每个 Weakness 和 Question 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Summary\n本文研究多类别（K≥3）LLM 标注误差在因果推断中的传播，覆盖 7 种 DAG 拓扑，推导拓扑依赖偏差表达式，提出 ASV 框架，评估 5 种校正方法。核心发现：K≥3 引入 binary 不存在的 sign reversal、FWL 不变性使 4 种拓扑下 matrix-based correction 完全无效、PPI++ 最有效但 topology-dependent。\n\n### Strengths\nS1: 系统性覆盖填补真实空白——K≥3×7 topologies 扩展 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024)。83.4% sign reversal 令人印象深刻。\nS2: ASV 框架设计合理且实用——Sign-flip ASV 识别 N* 在 E-value 中无对应物。\nS3: FWL 不变性是干净且有实践价值的负面结果。\nS4: 附录材料详实——19 页完整证明和数值验证。\nS5: Algorithm 1 提供可直接使用的决策流程。\n\n### Weaknesses\nW1 [should-fix]: Conjecture 1 未证明，削弱理论贡献完整性。建议为特定拓扑（如 confounding）给出解析证明。\nW2 [should-fix]: Abstract 信息密度过高，至少 9 个数字。建议聚焦 2-3 个核心数字。\nW3 [should-fix]: 计量经济学术语对 EMNLP 受众可及性不足。plim、FWL 等未充分解释。\nW4 [should-fix]: 实证验证规模有限——23 个经验混淆矩阵，CivilComments 实际 K=2。未在真实因果推断流程中端到端验证。\nW5 [minor]: \"First unified analysis\" 声明可更精确。\nW6 [minor]: Figure 2 视觉传达效率可提升。\n\n### Questions\nQ1: Proposition 1 的 sign preservation conditions 在实际 LLM 场景中多常被满足？\nQ2: ASV 的 diagonal parameterization 假设所有类别误分类率以相同比例退化，是否遗漏关键信息？\nQ3: FWL 不变性对非参数/半参数因果推断方法（doubly robust, TMLE）是否仍成立？\nQ4: PPI++ gold labels 成本，Algorithm 1 是否需要 cost-aware？\n\n### Missing References\nMR1: Stock & Yogo (2005) 弱工具变量检验——与 IV 拓扑直接相关\nMR2: VanderWeele (2015) 因果中介分析标准参考\nMR3: Mozer et al. (2023) LLM annotation inter-annotator agreement 与 systematic bias\n\n### Minor Issues\nM1: Footnote 1 绝对值比与文本描述可能不一致\nM2: Figure 4 x 轴标注不够清晰\nM3: Algorithm 1 Step 2 阈值 \"RMSE red. ≥ 10%\" 来源不明\nM4: Brenner (1993) 可能重复引用\nM5: 正文可能超 8 页（结论段延伸至 page 9）\n\n### Overall Assessment\nSoundness 4/5, Excitement 3.5/5, Overall 3.5/5 (Borderline Conference)\n推荐：Borderline Accept (weak accept)——贡献实质性，主要顾虑为可及性和实证验证广度。\n\n---\n\n请对 R2 的每个 Weakness 和 Question 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-23T06:37:28.573398+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1563
}
```

</details>

---


### Assistant

_source line 970 · 2026-05-23T06:37:30.625236+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 93

## Round 93

2 recorded events


### User

_source line 971 · 2026-05-23T06:37:33.321116+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心结论：**Overall 3.5/5（Borderline Conference）**，推荐 weak accept。

主要发现：
- **优势**：K≥3 sign reversal 现象（83.4%）是真正的新发现；ASV 框架实用；FWL 不变性是干净的负面结果；附录材料详实
- **关键问题**：Conjecture 1 未证明（W1）、Abstract 数字过载（W2）、计量经济学术语对 EMNLP 受众可及性不足（W3）、实证验证仅 23 个经验矩阵规模偏小（W4）
- **缺失引用**：弱工具变量文献（Stock & Yogo 2005）、因果中介标准参考（VanderWeele 2015）
- **格式**：结论段从 p8 溢出至 p9 前几行，严格解读下可能违反 8 页限制

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 972 · 2026-05-23T06:37:38.255708+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 94

## Round 94

2 recorded events


### User

_source line 973 · 2026-05-23T06:40:45.924479+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Strengths 回应

**[AGREE] R1-S1**: 拓扑依赖框架的系统性确实是本文最重要的贡献。我在自己的审稿中也将此列为 S1（"系统性覆盖填补了真实空白"）。K≥3 下 stochastic constraint 打破 binary 的结构保证这一发现，是不同于简单排列组合的真正理论洞察。

**[AGREE] R1-S2**: 证据层次的 Proved/Verified/Conjectured 标注确实值得肯定。这种诚实性在学术论文中不常见，体现了作者的学术严谨性。Table 2（p19-20）的 Summary of Conditions 表清晰区分了各结果的证明状态。

**[AGREE] R1-S3**: 1.6% MAPE 覆盖 161 场景（Section 4.2, p6）的理论-模拟一致性令人印象深刻。这有效排除了推导中的代数错误，增强了对闭式表达式的信心。

**[AGREE] R1-S4**: FWL 不变性证明干净——column-space equivalence 论证（Appendix B.2, p20-21）简洁有力。我在自己的审稿 S3 中也强调了这一点。

**[AGREE] R1-S5**: ASV 三种互补指标的设计合理。补充一点：sign-flip ASV 识别临界 N*（低于此阈值所有 rejection 被阻断）在 E-value 框架中确实没有直接对应物，这是 ASV 相对于现有敏感性分析工具的独特价值（Section 3.3, p5）。

---

### Weaknesses 回应

**[AGREE] R1-W1**: Conjecture 1 未证明确实削弱理论完整性。我在自己的审稿 W1 中提出了相同问题。但我对严重性评估与 R1 略有不同——我认为这是 **should-fix 而非 must-fix**，理由如下：

1. **数值验证规模充分**：Appendix B.11（p25）报告了 10,000 random C_δ matrices × 4 step sizes × K ∈ {3,5,7}，violation magnitude 对非 IV 拓扑始终 negligible（≤10⁻¹²），即使 violation count 本身较高（60-97%）。这说明 monotonicity "几乎" 成立，偏离量极小。
2. **ASV 实践价值不完全依赖 monotonicity**：即使 envelope monotonicity 不严格成立，ASV 的三种指标（magnitude/significance/sign-flip）仍然可以在给定 δ 点上提供有意义的敏感性信息。Monotonicity 保证的是 ASV 阈值的 **单调搜索性质**（可以 binary search），而非 ASV 本身的信息量。
3. **但作者确实应该更明确说明**：如果 monotonicity 失败，实践后果是什么？Algorithm 1（p29）是否需要修改？这一点论文未讨论。

**[AGREE] R1-W2**: 非差异性假设的合理性论证不足，我与 R1 判断一致。但我要补充两点 nuance：

1. **ε=0.50 是极端场景**：ε=0.50 意味着一半的误分类是 differential 的——即 LLM 的标注质量系统性依赖于 outcome Y。在标准 text classification pipeline 中（LLM 仅看 source text，不看 outcome），这种程度的 differential error 需要通过 outcome-covariate 关联间接产生（例如 Y-correlated 文本风格影响 LLM 判断）。Appendix B.5（p23）在 ε=0.10 时 violation rate 仅升 7.6 个百分点，这更接近实际场景。
2. **但 R1 的核心点成立**：论文确实没有直接从真实 LLM 系统估计 ε 的典型值。Limitations（p9）承认 "when it accesses Y-correlated information" 假设可能被违反，但未量化。建议作者从 Section 4.4 的 23 个经验矩阵中，利用 gold label subset 估计实际 differential degree。

**[AGREE] R1-W3**: 线性 SEM 假设对 NLP 应用的适用性确实需要更好的动机论证。但我要补充：Appendix B.13（p27）的 logistic DGP 验证比 R1 描述的更充分——Table 13 显示所有 5 种 covariate topologies 下 logistic bias reduction 均保持近零（<0.005），Table 5（p22）进一步确认 OLS 与 logistic 的 sign-flip rate 差异 < 0.02。问题不在于结果缺失，而在于 **正文中几乎没有引用这些附录结果**。建议在 Section 4.5（p8）增加 1-2 句总结 logistic DGP 的发现，并显式引用 Appendix B.13。

**[AGREE] R1-W4**: 校正比较仅在 K=3 下进行是一个合理的担忧。Table 4（p8）的 RMSE reduction 确实只报告了 K=3 结果。PPI++ 和 MC-SIMEX 的性能可能随 K 增大而变化——特别是 PPI++ 依赖 gold label subset 的统计效率，而 MC-SIMEX 的模拟步骤在高维混淆矩阵下可能不稳定。Appendix B.14（p27）的 gold label sensitivity 分析也限于 K=3。建议至少在 K=5 和 K=10 下重复 Table 4 的核心比较。

**[REBUT] R1-W5**: ASV bootstrap CI 宽度的实践可操作性问题，我持不同意见。

1. **宽 CI 反映的是真实参数不确定性，而非框架缺陷**。ASV 是混淆矩阵 C 的函数，而 C 的估计需要 gold labels 或 calibration data。Bootstrap CI 宽度 [0.60, 1.36] for exposure（Table 9, Figure 8, p25）反映了在有限 bootstrap resamples 下 C 估计的不确定性。
2. **排名稳定性比绝对值更重要**。Table 9（p25）和 Figure 8 显示 ASV 排名在不同 DGP 配置下一致：confounding 最稳健，IV 最脆弱，M-bias 免疫。即使绝对 ASV 值有宽 CI，拓扑间的 **相对排序** 是稳定的——这才是 Algorithm 1 决策流程所依赖的信息。
3. **但 R1 的实操关切有道理**：如果 practitioner 需要判断 "我的 ASV 是否超过安全阈值"，宽 CI 确实使这个二元决策变得模糊。建议作者讨论 ASV 的 **推荐使用方式**——是作为排名工具还是作为阈值检测工具，前者对 CI 宽度更鲁棒。

**[AGREE] R1-W6**: LLM 配置覆盖度不足是合理关切，但我认为严重性低于 R1 的评估。

1. **理论结果与 LLM 无关**：论文的核心贡献（bias taxonomy, ASV, FWL invariance）完全取决于混淆矩阵 C 的性质，与具体 LLM 无关。LLM 配置只影响 Section 4.4 的经验验证。
2. **但经验覆盖确实可以更广**：缺少 GPT-4/Claude 等商业模型、>235B 参数模型、以及 NER/关系抽取等结构化标注任务。特别是 NER 任务中 entity boundary 错误引入的混淆矩阵结构可能与 text classification 不同——off-diagonal 元素的分布模式可能更 sparse。
3. **建议**：增加 2-3 个商业 API 模型的混淆矩阵（哪怕从现有文献如 Baumann 2025 或 Gilardi et al. 2023 中获取），以及至少一个序列标注任务。

---

### Questions 回应

**[AGREE] R1-Q1**: K≥3 证明困难的解析直觉——这是一个好问题。从 Appendix B.11（p25）和 Section 5（p5）可以推断，困难源于 K≥3 混淆矩阵的 K²-K 个额外自由度允许类别间 opposite-sign effects 的交叉污染（cross-contamination），而 K=2 的 2×2 stochastic matrix 只有 1 个自由度，结构高度受限。但论文确实应该在正文中更清晰地解释这一直觉。

**[AGREE] R1-Q2**: 从原始标注数据估计 differential degree 在原则上可行——如果有 gold label subset（如 PPI++ 设置中的子集），可以计算 P(A*|A,Y) vs P(A*|A) 来估计 ε。论文未讨论这个自然延伸，这是一个遗憾。

**[AGREE] R1-Q3**: ASV 排名随 K 变化的稳定性是关键实践问题。Appendix B.10（p25）报告了 K ∈ {3,5,7} 下 ASV across three scaling regimes（alternating-large, same-sign, alternating-small），但我在论文中未找到 K 对排名影响的显式讨论。如果 K=10 下排名反转，Algorithm 1 的建议就需要条件化于 K。

**[REBUT] R1-Q4**: λ(C)∉[0,1] 时 mediation 偏差表达式的物理含义——这个问题的前提可能需要修正。从 Section 3.2（p4）和 Appendix A.5（p15-16），λ(C) ∈ [0,1] under proportional effects（Proposition 4），这是由混淆矩阵的 column-stochasticity 保证的。λ(C)∉[0,1] 理论上需要混淆矩阵 C 的特定列结构使加权平均超出 [0,1]——但在 column-stochastic C 下，Appendix A.5 的推导表明 λ(C) 始终落在 [0,1]。如果 R1 发现了 λ(C)∉[0,1] 的具体例子，我会很有兴趣看到。

**[AGREE] R1-Q5**: Proposition 3（p13）的 Cauchy-Schwarz bound |R(C)| ≤ √(Var(g(A))·Var(f(A))) 的 tightness 是合理的技术问题。Cauchy-Schwarz bound 在 g 和 f 高度相关时是 tight 的，在不相关时非常 loose。论文提供了这个 bound 作为 "complementary assessment tool"（Section 5, p5），但未在经验数据上验证其 tightness。建议作者在 Section 4.4 的 23 个经验矩阵上报告 bound 与实际 |R(C)| 的比值。

---

### Missing References 回应

**[AGREE] R1-MR1**: Schennach (2020) 非线性测量误差综述确实相关——论文在 Limitations 中承认 non-differential 假设的局限性，但未引用非线性测量误差的通用框架。这对想要扩展本工作到非线性模型的读者是有价值的参考。

**[AGREE] R1-MR2**: Si et al. (2023) LLM 标注质量评估——如果该工作提供了系统性的 LLM confusion matrix 分析，确实应该在 Section 2 "Text classifiers and LLM annotation"（p2-3）中引用。补充：我在自己的审稿中也建议引用 weak instruments 文献（Stock & Yogo 2005）和因果中介分析标准参考（VanderWeele 2015）。

---

### Minor Issues 回应

**[AGREE] R1-M1**: Figure 2 两图挤在同一页（p7）——我在自己的审稿 W6 中也提出了 Figure 2 的视觉传达效率问题。

**[AGREE] R1-M2**: Algorithm 1 硬编码阈值来自 K=3——这与 W4（校正比较仅在 K=3）是同一问题的不同面向。如果 K 变化导致最优阈值变化，Algorithm 1 需要参数化。

**[AGREE] R1-M3**: f/g 定义分散在附录中——正文首次使用时应给出简短定义或显式引用附录位置。

**[AGREE] R1-M4**: "default DGP parameters" 正文未说明——Section 4.1（p6）提到 "compute the analytical probability limit...and validate against Monte Carlo simulation (N=10,000)"，但 DGP 的具体参数（β 值、误差分布）在正文中确实没有完整说明，需要翻到 Appendix A.3（p13）才能找到。建议在 Section 4.1 增加 1 句简要说明。

---

### 总体评估对比

R1 和我（R2）的评分基本一致：

| 维度 | R1 | R2（我） | 差异分析 |
|------|------|--------|----------|
| Soundness | 3.5/5 | 4/5 | R1 因 Conjecture 1 扣分更重；我认为数值验证规模（10,000 matrices × 多配置）部分弥补了缺乏解析证明的问题 |
| Excitement | 3.5/5 | 3.5/5 | 一致 |
| Overall | 3.5/5 | 3.5/5 | 一致：Borderline Conference |
| Confidence | 4/5 | 4/5 | 一致 |

**共识**：论文在重要问题上做出系统性贡献，理论扎实但有缺口（Conjecture 1），实证验证规模偏小，对 EMNLP 受众的可及性需要改善。

**分歧**：我对 W5（ASV CI 宽度）持更乐观态度——排名稳定性比绝对值的 CI 更重要；对 W1 的严重性我评为 should-fix 而非 must-fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 974 · 2026-05-23T06:40:53.349444+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 95

## Round 95

2 recorded events


### User

_source line 975 · 2026-05-23T06:41:05.021577+00:00_

[Reviewer 2 审稿结果]:
两轮审稿意见已提交给 Review Director：

1. **Round 1 初审**：完整审稿意见（Overall 3.5/5 Borderline Conference，5 个 Strengths，6 个 Weaknesses，4 个 Questions，3 个 Missing References）
2. **Round 1 交叉回应**：对 R1 的每个 Weakness/Question 逐条标注 [AGREE] 或 [REBUT]，附证据引用

关键共识与分歧：
- **共识**：R1 和 R2 在 Overall 3.5/5、Excitement 3.5/5 上完全一致；均认为 Conjecture 1 未证明和实证规模偏小是主要问题
- **分歧**：我对 W1 评为 should-fix（R1 评 must-fix），对 W5（ASV CI 宽度）持更乐观态度——排名稳定性比绝对值更重要；Soundness 我给 4/5（R1 给 3.5/5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 976 · 2026-05-23T06:41:12.441657+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 96

## Round 96

12 recorded events


### User

_source line 977 · 2026-05-23T06:41:46.552239+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths

[AGREE] R2-S1: 系统性覆盖确实是本文最核心的贡献。我在 S1 中做了相同判断。补充一点：83.4% sign reversal 数据来自 Table 1 (p.7) 的 exposure 拓扑下 K=3 Dirichlet(1,1,1) 随机矩阵，条件为 "under uniform Dirichlet prior"。这个数字在特定参数设定下成立，正文的呈现方式可能让读者以为是所有 K=3 配置的普遍比例。

[AGREE] R2-S2: ASV 框架的 sign-flip ASV 确实填补了 E-value 框架的空白。我在 S5 中同样肯定了这一点。

[AGREE] R2-S3: 与我的 S4 一致。FWL 不变性是一个 clean 的负面结果。

[AGREE] R2-S4: 附录材料确实详实。19 页附录覆盖了完整证明和大量数值验证。

[AGREE] R2-S5: Algorithm 1 的决策流程实用，但我在 M2 中指出其阈值硬编码自 K=3 结果，适用条件应明确标注。

---

### Weaknesses

[AGREE] R2-W1: Conjecture 1 未证明。我在 W1 中将此标为 **must-fix** 而非 should-fix，理由更强：论文标题核心承诺是 "Multi-Class"（K≥3），但 Theorem 1 仅覆盖 K=2。K≥3 的单调性是 ASV 框架实践指导（Algorithm 1, p.29）的理论基础——如果单调性不成立，ASV 的 δ 阈值判定可能给出误导性建议。R2 建议"为特定拓扑给出解析证明"是建设性的；我补充建议作者至少应在正文中讨论 Conjecture 1 失效时的 fallback 策略。

R2 评 should-fix，我评 must-fix。差异在于我认为这直接影响论文核心 claim 的可信度，而非仅削弱完整性。

[AGREE] R2-W2: Abstract 信息密度确实过高。重新检查 Abstract（p.1），我计数到至少 10 个定量信息点：K-class、K≥3、sign reversal、2.15×、83.4%、secondary coefficients、diagonal ≥ 0.7、2.1%、FWL invariance、four topologies。对于 EMNLP 读者，这种密度可能导致核心信息淹没。不过我倾向将此评为 **minor** 而非 should-fix——这是展示效率问题，不影响技术内容。

[AGREE] R2-W3: 计量经济学术语可及性不足。plim（probability limit）在 Section 3.2 (p.3-4) 频繁出现但未定义；FWL（Frisch-Waugh-Lovell）在 Section 4.5 (p.8) 引用了原始文献但未陈述定理内容。对于 EMNLP 读者，这些术语需要 1-2 句解释。我在原始审稿中未单独提出此问题，但 R2 的判断合理。建议在 Section 3.1 或 Section 3.2 首次使用 plim 时加脚注定义，FWL 可用一句话概述其含义（"partialling-out interpretation: the coefficient on T equals the coefficient from regressing T-residuals on Y-residuals"）。

[AGREE] R2-W4: 实证验证规模有限。我在 W6 中提出了类似关切。R2 正确指出 CivilComments 实际为 K=2（确认自 p.8: "CivilComments (K=2)"），这意味着 3 个任务中仅 HumAID (K=10) 和 VAST (K=5) 是真正的多类别验证。此外，R2 提出的"未在真实因果推断流程中端到端验证"是我原始审稿未充分强调的有效关切——论文验证了偏差表达式的准确性（Monte Carlo）和 LLM 混淆矩阵的预测一致性，但未展示从"LLM 标注 → 构建混淆矩阵 → 选择校正方法 → 恢复真实因果效应"的完整流水线在真实数据上的有效性。Appendix B.3 的 ClinicalBERT 案例最接近端到端验证，但使用的是代理 DAG 识别而非 ground-truth 因果效应。

[REBUT] R2-W5: "First unified analysis" 声明的准确性。论文在 Section 2 (p.2) 的实际表述是"the first unified analysis of K-class annotation error propagation across seven canonical DAG topologies, building on prior single-topology analyses (Brenner, 1993; Teblunthuis et al., 2024)"。这一声明是准确的：Teblunthuis et al. (2024) 覆盖 K≥3 但仅处理 confounding 拓扑；Lee & Wood-Doughty (2024) 覆盖多拓扑但限于 K=2 或特定方面；Bound et al. (2001) 讨论了 polytomous confounders 但未系统推导多拓扑闭式表达式。论文确实是首个在 7 种拓扑 × K≥3 下提供统一分析框架的工作。R2 建议"更精确"是合理的写作建议，但 claim 本身有事实支撑，不构成 weakness。

[AGREE] R2-W6: Figure 2 视觉传达效率可提升。我在 M1 中指出了相同问题——Figure 1 和 Figure 2 挤在同一页 (p.7)，caption 字号较小。

---

### Questions

[AGREE] R2-Q1: Proposition 1 的 sign preservation conditions 在实际 LLM 场景中多常被满足？这与我的 Q5 密切相关。我在 Q5 中追问了 |R(C)| 与 bound B̃ 的比值分布。论文在 Table 2 (p.5) 汇总了各拓扑的充分条件，Appendix B.15 (Table 15, p.28) 报告了 23 个经验矩阵的差异性阈值 ε*，但**未系统报告 sign preservation conditions 在这 23 个经验矩阵上的满足频率**。这一缺失使得理论条件的实践相关性难以评估。

[AGREE] R2-Q2: ASV 的 diagonal parameterization 确实遗漏了非对称退化模式。C(δ) = (1−δ)I + δC_k（Section 3.3, p.5）假设所有类别从完美分类均匀退化到参考混淆矩阵 C_k。实际中，稀有类别通常退化更快。然而我认为这是**可接受的简化**：任何一维敏感性参数化都必须牺牲某些信息以获得可解释性。关键问题是该参数化是否捕获了最具政策相关性的变化方向。建议作者在 Limitations 中明确讨论此假设，并指出多维 ASV 扩展的可能方向。

[AGREE] R2-Q3: FWL 不变性对非参数/半参数方法是否成立？这与我的 W3（线性 SEM 假设）直接相关。FWL 不变性依赖于线性投影的 partialling-out 性质（Appendix B.2, p.20）。对于 doubly robust estimators 或 TMLE，residualization 过程不同（通常涉及 nuisance function 的非参数估计），FWL 不变性几乎必然不成立。这意味着论文"matrix-based correction 对协变量拓扑无效"的结论可能仅适用于线性/逻辑回归估计器，而不适用于现代因果推断工具箱。论文应在 Limitations 或 Section 4.5 中明确标注此适用边界。

[AGREE] R2-Q4: PPI++ gold labels 成本。Algorithm 1 (p.29) 推荐 PPI++ 为 exposure/IV 拓扑的首选方法，但 Appendix B.14 (Table 14, p.27) 显示 PPI++ 需要 ≥20% gold labels 才能实现显著 RMSE 降低（在 low gold 场景下 RMSE 反而可能增加）。一个 cost-aware 版本的 Algorithm 1——至少讨论 gold label budget 对方法选择的影响——会显著提升实用性。

---

### Missing References

[REBUT] R2-MR1: Stock & Yogo (2005) 弱工具变量检验。论文的 IV 拓扑分析关注的是**错分类对工具变量系数的偏差效应**（Section 3.2, p.4, Wald estimator denominator），而非弱工具变量问题本身。N-sensitivity ASV（Section 4.3, p.7）衡量的是 first-stage coefficient 接近零时的 sign-flip 脆弱性，这与 weak IV 在概念上相邻但分析目标不同——Stock & Yogo 处理的是 instrument relevance，本文处理的是 instrument measurement error。引用该文献可以作为补充背景，但不构成必要引用。

[AGREE] R2-MR2: VanderWeele (2015) 因果中介分析标准参考。论文 mediation 拓扑分析（Section 3.2, p.4; Appendix A.5, p.15-16）大量使用中介分析概念（direct effect, indirect effect, λ(C) leakage coefficient），但仅引用了 VanderWeele & Ding (2017) 的敏感性分析文献，未引用中介分析方法论的标准参考。这一遗漏在方法论背景上是不完整的。

[AGREE] R2-MR3: Mozer et al. (2023) 或类似 LLM 标注质量评估工作。这将为非差异性假设讨论提供经验支撑——如果有工作直接测量了 LLM 标注中 P(A*|A,Y) 与 P(A*|A) 的偏离程度，将大幅加强 Appendix B.5 stress test 参数选择的实际依据。与我的 W2 建议一致。

---

### Minor Issues

[AGREE] R2-M2: Figure 4 (p.7 底部) 的 x 轴标注确实不够清晰。δ 参数的物理含义（从完美分类到参考混淆矩阵的插值比例）应在 caption 中直接说明。

[AGREE] R2-M3: Algorithm 1 阈值来源不明。与我的 M2 完全一致——这些阈值硬编码自 Table 4 (K=3, N=1,000) 的具体结果，应标注适用条件。

[AGREE] R2-M5: **正文可能超 8 页。** 重新检查后确认：Section 5 (Conclusion) 起始于 p.8 下方约 1/3 处，但结论文本延续至 p.9 顶部约 4-5 行（"structural guarantees. ASVs reveal a vulnerability spectrum from IV (maximally fragile) to M-bias (immune)..."），之后才是 Limitations section。这意味着 main text（Sections 1-5）技术上超出了 8 页限制。虽然溢出量极小（约 4-5 行），但 EMNLP 2026 的 8 页限制是硬约束。**我在原始审稿中未检出此格式问题，R2 的发现是正确的。** 建议将结论压缩约 4-5 行使其完全收入 p.8。

R2-M1（Footnote 1 一致性）和 R2-M4（Brenner 1993 重复引用）：我未独立验证这两点，无法确认或反驳。

---

### Overall Assessment 对比

| 维度 | R1 (我) | R2 | 差异分析 |
|------|--------|-----|--------|
| Soundness | 3.5/5 | 4/5 | 我更关注 Conjecture 1 对核心 claim 的影响和非差异性假设的经验依据不足 |
| Excitement | 3.5/5 | 3.5/5 | 一致 |
| Overall | 3.5/5 | 3.5/5 | 一致（Borderline Conference） |
| Confidence | 4/5 | — | — |

**关键分歧：Soundness。** R2 给 4/5（Strong），我给 3.5/5。分歧核心在于 Conjecture 1 的权重判定：R2 将其评为 should-fix（认为数值验证充分），我评为 must-fix（认为标题承诺 "Multi-Class" 但核心定理限于 K=2）。我维持 3.5/5 的 soundness 判断——K≥3 单调性作为 conjecture 而非 theorem 是一个真实的理论缺口，不仅削弱完整性，且影响基于 ASV 的实践指导的可靠性。

**共识：** 两位 reviewer 在 Overall 3.5/5（Borderline Conference）上达成一致。论文贡献真实且系统性强，但理论不完整性（conjecture）和实证覆盖度限制（K=2 任务占比、无端到端验证、线性假设边界）使其处于 Conference 门槛边缘。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-23T06:42:15.496716+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-23T06:42:15.647914+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T06:28:00.282943+00:00\", \"completed_at\": \"2026-05-23T06:31:33.172663+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 1-6\", \"message\": \"前 6 页连续纯文本无任何 figure/table，审稿人在形成第一印象时完全没有视觉锚点。Figure 1（DAG 拓扑图）是论文的核心概念图，应尽早出现（理想位置：P1-P2 的 Introduction 中）\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"三个 display items（Figure 1 + Figure 2 + Table 1）挤在同一页，每个图表被压缩得较小。Figure 2 的直方图细节在当前尺寸下勉强可读。建议将 Figure 1 前移至 Introduction，分散视觉密度\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-9\", \"message\": \"正文 8.5 页仅 4 个 display items（3 figure + 1 table），作为实证为主的论文偏少。主要实验结果表格（Table 3-4, RMSE reduction 等）全部在 Appendix（P20+），审稿人在正文中看不到核心定量结果的表格\"}, {\"severity\": \"warning\", \"dimension\": \"page 21\", \"message\": \"Appendix 中 Figure 4 + Figure 5 + Figure 6 三图挤一页，每个图尺寸很小。Figure 5（混淆矩阵热力图）在此尺寸下色块文字较难辨认\"}, {\"severity\": \"warning\", \"dimension\": \"page 22\", \"message\": \"Figure 7（ASV magnitude ranges）使用红色和绿色柱状图进行对比，对红绿色盲不友好。建议改用蓝/橙或 Okabe-Ito 色板\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（bias distributions）使用红色标记 sign reversal——建议除颜色外增加 marker shape 区分，提高打印和色盲场景下的可辨识度\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 3（topology determines bias 热力图）caption 较简短，建议增加\\\"如何阅读此图\\\"的说明（如\\\"颜色越深表示偏差越大\\\"）使 caption 更加自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 19\", \"message\": \"Table 2（Summary of Conditions）底部文字与页面下边距较近，排版略显拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Table 3 和 Table 4 格式规范（booktabs 风格、最优加粗），排版良好\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"References 排版正常，无 [?] 未解析引用，格式统一\"}, {\"severity\": \"info\", \"dimension\": \"page 11-18\", \"message\": \"Appendix 证明部分连续 8 页纯数学推导，无 display item，但数学证明密集属合理例外\"}, {\"severity\": \"info\", \"dimension\": \"page 29\", \"message\": \"Algorithm 1 伪代码
…[truncated 137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-23T06:42:15.648390+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-23T06:42:15.698866+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-23T06:42:45.369304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-23T06:42:45.369719+00:00_

1	issues:
2	  # === Round 1-7 历史 (resolved，保留摘要) ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 7
11	    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
12	    resolution_round: 7
13	
14	  - id: R1-N2
15	    category: soundness
16	    severity: should-fix
17	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
18	    status: resolved
19	    first_raised_round: 1
20	    last_seen_round: 3
21	    resolution: "Abstract 已准确区分 prove/verify。"
22	    resolution_round: 4
23	
24	  - id: R1-N3
25	    category: soundness
26	    severity: must-fix
27	    summary: "ASV C(δ) 定义域错误"
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 1
31	    resolution: "Section 3.3 已引入 δ_max 约束。"
32	    resolution_round: 2
33	
34	  - id: R2-N1
35	    category: presentation
36	    severity: must-fix
37	    summary: "83.4% sign reversal headline framing 过度声称"
38	    status: resolved
39	    first_raised_round: 1
40	    last_seen_round: 5
41	    resolution: "Introduction 已重写。"
42	    resolution_round: 5
43	
44	  - id: R2-N2
45	    category: novelty
46	    severity: should-fix
47	    summary: "'first systematic framework' 过度声明"
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-23T06:46:16.964912+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 12\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：23 个配置缺少商业 API（GPT-4/Claude）、>235B 模型、NER 等结构化任务。R1 评 should-fix，R2 同意。理论贡献与 LLM 无关，但经验验证覆盖度可更广。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 12\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补直觉解释。R1 新增批评：B.5 stress test 仅用随机扰动模型。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识 must-fix（R1）/should-fix（R2）：stress test 覆盖 ε=0.10-0.50 但未直接估计实际 LLM 系统的差异性程度。R2 补充 ε=0.50 是极端场景，ε=0.10 更接近实际。建议从 23 个经验矩阵的 gold label subset 估计实际 differential degree。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 4\n        reviewers: []\n        note: \"正文 ≤ 8 页已验证。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 复发：Conclusion（Section 5）从 p8 下方 1/3 处延伸至 p9 顶部约 4-5 行，之后才是 Limitations。严格解读下溢出 8 页限制。两位 Reviewer 共识确认。建议压缩结论约 4-5 行。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Abstract 至少 9-10 个定量信息点，信息密度过高。R2 评 should-fix，R1 评 minor。建议聚焦 2-3 个核心数字，其余移至 Introduction。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 12\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：两位 Reviewer 均认可 ASV 的 sign-flip ASV 和 N* 临界样本量在 E-value 中无对应物（S2/S5）。但 R2 仍认为与 E-value 同构度高。建议 Section 3.3 增加显式 ASV-vs-E-value 对比。\"\n    action_items:\n      - round: 8\n        action: \"ASV 措辞从 framework 降为 diagnostics\"\n        assigned_to: agent\n        status: done\n      - round: 11\n        action: \"Section 3.3 加 ASV-vs-E-value 显式对比段\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Section 4.4 已解释。\"\n    resolution_round: 8\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述（'exclusively in secondary coefficients with small effect sizes'）。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。Abstract 已移除 structural property 声称。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 W1 再次提出。R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R1 Q4 追问 λ(C)∉[0,1] 时物理含义。R2 REBUT——column-stochastic C 下 proportional case 保证 λ(C)∈[0,1]（Proposition 4）。General case 15-17% 违反仍是已知限制。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是真正的新贡献，但 magnitude ASV 与 E-value 同构度高。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被 R11 两位 Reviewer 赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加 Collider amplification 脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论 PPI++ 对 M-bias 有害。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：exposure/IV 的 CI 跨界是拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧：R1 评 should-fix（CI 过宽影响可操作性），R2 REBUT（排名稳定性比绝对值更重要）。Director 采纳 R2 观点——ASV 主要用作排名工具而非阈值检测，CI 宽度不构成框架缺陷。降为 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"R11 未再提及。Algorithm 1 整体被两位 Reviewer 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级为 should-fix。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出。R1 评 must-fix（标题承诺 Multi-Class 但 Theorem 限 K=2），R2 评 should-fix（数值验证规模充分）。Section 3.3 已包含 proof obstacle 解释。两位均认可三级层次诚实。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"正文讨论 Conjecture 1 失效时对 ASV 实践指导的影响\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R1 Q4 追问 λ(C)∉[0,1] 物理含义。R2 REBUT——proportional case 有保证。General case 15-17% violation 是已知限制。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"分歧：R2 认为与 E-value 同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是 E-value 无对应物的新贡献。但 magnitude ASV 与 E-value 同构度高。建议增加 ASV-vs-E-value 显式对比。\"\n    action_items:\n      - round: 8\n        action: \"ASV 定位调整\"\n        assigned_to: agent\n        status: done\n      - round: 11\n        action: \"Section 3.3 加 ASV-vs-E-value 显式对比段\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"均匀 ε 局限。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R1 新增：stress test 仅随机扰动，未测结构化违反。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 R1 评 must-fix，R2 评 should-fix。共识：未直接估计实际 LLM 系统的差异性程度。建议从 23 个经验矩阵的 gold label subset 估计实际 differential degree。R2 补充 ε=0.10 更接近实际。\"\n    action_items:\n      - round: 11\n        action: \"结构化违反实验：outcome-conditional + label-specific\"\n        assigned_to: agent\n        status: in_progress\n      - round: 12\n        action: \"从经验矩阵估计实际 differential degree\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧 → R2 REBUT 成功：排名稳定性比绝对值更重要。Director 降为 minor。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用 ding_vanderweele2016。R11 未再提及。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 NEW-1 和 R8-C2 讨论。核心问题未变：未从实际 LLM 数据估计假设违反程度。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需 Section 3.1 加线性 SEM 动机。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"主文整合 logistic 结果不足。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Appendix B.6/B.13 的 logistic DGP 验证充分但正文几乎未引用。R2 确认 Table 13 logistic bias reduction < 0.005。建议 Section 4.5 增加 1-2 句 + 显式引用 Appendix B.13。R2 新增 W3：plim/FWL 对 EMNLP 读者不友好，需 1-2 句直觉解释。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 12\n        action: \"Section 4.5 增加 logistic DGP 总结 + 引用 Appendix B.13\"\n        assigned_to: agent\n        status: open\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: open\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R1 Q1 追问解析直觉。R2 AGREE 并补充——K≥3 的 K²-K 额外自由度允许 cross-contamination。论文应在正文中更清晰解释。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被 R11 赞为 S5/S6 strength，可操作性获认可。\"\n    resolution_round: 11\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R2 提议进一步精确化（W5），R1 REBUT——'first unified analysis...building on prior single-topology analyses' 有事实支撑。Director 支持 R1，claim 准确。\"\n    resolution: \"R1 REBUT 成功。Introduction 措辞准确且有事实支撑。\"\n    resolution_round: 12\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。R11 未再提及。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 R1-W3。共识：不影响核心贡献。\"\n\n  - id: R9-S4\n    category: presentation\n    severity: should-fix\n    summary: \"PPI++ 47.0% vs Table 4 17.0 数字不一致\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: \"数字实际一致，Reviewer 误读。\"\n    resolution_round: 9\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增强论文对 EMNLP 应用导向读者的说服力。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R1 交叉回应中确认 ClinicalBERT 案例最接近端到端验证但使用代理 DAG。R2 W4 再次提出需要前瞻性验证。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增加 3-4 句直觉语言解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出（R2-W3）。R1 交叉回应 AGREE——plim 在 Section 3.2 未定义，FWL 在 Section 4.5 才引用但 Appendix 大量依赖。建议 Section 3.1 加 plim 脚注定义 + FWL 首次使用加内联解释。\"\n    action_items:\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: open\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1]\n        note: \"FWL invariance 与 K 无关，PPI++/MC-SIMEX 排名可能随 K 变化。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：R1 W4 + R2 交叉回应 AGREE。PPI++ 在 K>3 需更多 gold labels，MC-SIMEX 外推精度可能下降。建议至少 K=5/K=10 附录验证排名稳定性。\"\n    action_items:\n      - round: 12\n        action: \"补充 K=5/K=10 校正方法对比（至少附录）\"\n        assigned_to: agent\n        status: open\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R12 未单独提出但 R1 Q1 间接涉及。Section 4.2 已有 practitioners 指导句。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：5 篇引用。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 新增缺失引用：VanderWeele (2015) 因果中介标准参考（R2-MR2，R1 AGREE）、Schennach (2020) 非线性测量误差综述（R1-MR1，R2 AGREE）。Stock & Yogo (2005) R1 REBUT——分析目标不同。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 11\n\n  # === Round 12 新发现 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文 Section 5 (Conclusion) 溢出至 p9，违反 EMNLP 2026 的 8 页限制\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R2 首先发现（M5），R1 交叉回应确认。Conclusion 从 p8 下方 1/3 处延续至 p9 顶部约 4-5 行。溢出量极小但 8 页限制是硬约束。建议压缩结论约 4-5 行。\"\n    action_items:\n      - round: 12\n        action: \"压缩 Conclusion 使正文完全收入 8 页\"\n        assigned_to: agent\n        status: open\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语（plim/FWL）对 EMNLP 受众可及性不足\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R2 提出（W3），R1 交叉回应 AGREE。plim 在 Section 3.2 频繁出现但未定义；FWL 在 Section 4.5 引用但未陈述内容。建议 plim 首次使用加脚注 + FWL 首次使用加内联解释。\"\n    action_items:\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 脚注定义和 FWL 内联解释\"\n        assigned_to: agent\n        status: open\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 新发现的缺失引用\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"共识缺失：(1) VanderWeele (2015) 因果中介标准参考——mediation 分析大量使用但未引用（R2-MR2，R1 AGREE）；(2) Schennach (2020) 非线性测量误差综述——讨论非线性扩展可能性（R1-MR1，R2 AGREE）。分歧：Stock & Yogo (2005) 弱 IV——R2 提出，R1 REBUT（分析目标不同）。\"\n\n  - id: R12-MI1\n    category: presentation\n    severity: minor\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果，适用条件未标注\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R1-M2 和 R2-M3 共同提出。Algorithm 1 的 RMSE 阈值来源于 Table 4（K=3, N=1,000），如 K 变化阈值可能失效。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 和 Figure 7 视觉问题\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R1-M1 + R2-W6：Figure 1/2 挤在同一页，caption 字号小。R2 建议 dual-panel 设计。视觉审查补充：Figure 7 使用红绿色板对色盲不友好。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 12\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：23 个配置缺少商业 API（GPT-4/Claude）、>235B 模型、NER 等结构化任务。R1 评 should-fix，R2 同意。理论贡献与 LLM 无关，但经验验证覆盖度可更广。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 12\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补直觉解释。R1 新增批评：B.5 stress test 仅用随机扰动模型。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识 must-fix（R1）/should-fix（R2）：stress test 覆盖 ε=0.10-0.50 但未直接估计实际 LLM 系统的差异性程度。R2 补充 ε=0.50 是极端场景，ε=0.10 更接近实际。建议从 23 个经验矩阵的 gold label subset 估计实际 differential degree。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 4\n        reviewers: []\n        note: \"正文 ≤ 8 页已验证。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 复发：Conclusion（Section 5）从 p8 下方 1/3 处延伸至 p9 顶部约 4-5 行，之后才是 Limitations。严格解读下溢出 8 页限制。两位 Reviewer 共识确认。建议压缩结论约 4-5 行。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 12\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Abstract 至少 9-10 个定量信息点，信息密度过高。R2 评 should-fix，R1 评 minor。建议聚焦 2-3 个核心数字，其余移至 Introduction。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 12\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：两位 Reviewer 均认可 ASV 的 sign-flip ASV 和 N* 临界样本量在 E-value 中无对应物（S2/S5）。但 R2 仍认为与 E-value 同构度高。建议 Section 3.3 增加显式 ASV-vs-E-value 对比。\"\n    action_items:\n      - round: 8\n        action: \"ASV 措辞从 framework 降为 diagnostics\"\n        assigned_to: agent\n        status: done\n      - round: 11\n        action: \"Section 3.3 加 ASV-vs-E-value 显式对比段\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Section 4.4 已解释。\"\n    resolution_round: 8\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述（'exclusively in secondary coefficients with small effect sizes'）。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。Abstract 已移除 structural property 声称。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 W1 再次提出。R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R1 Q4 追问 λ(C)∉[0,1] 时物理含义。R2 REBUT——column-stochastic C 下 proportional case 保证 λ(C)∈[0,1]（Proposition 4）。General case 15-17% 违反仍是已知限制。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是真正的新贡献，但 magnitude ASV 与 E-value 同构度高。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被 R11 两位 Reviewer 赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加 Collider amplification 脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论 PPI++ 对 M-bias 有害。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：exposure/IV 的 CI 跨界是拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧：R1 评 should-fix（CI 过宽影响可操作性），R2 REBUT（排名稳定性比绝对值更重要）。Director 采纳 R2 观点——ASV 主要用作排名工具而非阈值检测，CI 宽度不构成框架缺陷。降为 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"R11 未再提及。Algorithm 1 整体被两位 Reviewer 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级为 should-fix。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出。R1 评 must-fix（标题承诺 Multi-Class 但 Theorem 限 K=2），R2 评 should-fix（数值验证规模充分）。Section 3.3 已包含 proof obstacle 解释。两位均认可三级层次诚实。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"正文讨论 Conjecture 1 失效时对 ASV 实践指导的影响\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R1 Q4 追问 λ(C)∉[0,1] 物理含义。R2 REBUT——proportional case 有保证。General case 15-17% violation 是已知限制。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"分歧：R2 认为与 E-value 同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是 E-value 无对应物的新贡献。但 magnitude ASV 与 E-value 同构度高。建议增加 ASV-vs-E-value 显式对比。\"\n    action_items:\n      - round: 8\n        action: \"ASV 定位调整\"\n        assigned_to: agent\n        status: done\n      - round: 11\n        action: \"Section 3.3 加 ASV-vs-E-value 显式对比段\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"均匀 ε 局限。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R1 新增：stress test 仅随机扰动，未测结构化违反。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 R1 评 must-fix，R2 评 should-fix。共识：未直接估计实际 LLM 系统的差异性程度。建议从 23 个经验矩阵的 gold label subset 估计实际 differential degree。R2 补充 ε=0.10 更接近实际。\"\n    action_items:\n      - round: 11\n        action: \"结构化违反实验：outcome-conditional + label-specific\"\n        assigned_to: agent\n        status: in_progress\n      - round: 12\n        action: \"从经验矩阵估计实际 differential degree\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧 → R2 REBUT 成功：排名稳定性比绝对值更重要。Director 降为 minor。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用 ding_vanderweele2016。R11 未再提及。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 NEW-1 和 R8-C2 讨论。核心问题未变：未从实际 LLM 数据估计假设违反程度。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需 Section 3.1 加线性 SEM 动机。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"主文整合 logistic 结果不足。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Appendix B.6/B.13 的 logistic DGP 验证充分但正文几乎未引用。R2 确认 Table 13 logistic bias reduction < 0.005。建议 Section 4.5 增加 1-2 句 + 显式引用 Appendix B.13。R2 新增 W3：plim/FWL 对 EMNLP 读者不友好，需 1-2 句直觉解释。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 12\n        action: \"Section 4.5 增加 logistic DGP 总结 + 引用 Appendix B.13\"\n        assigned_to: agent\n        status: open\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: open\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R1 Q1 追问解析直觉。R2 AGREE 并补充——K≥3 的 K²-K 额外自由度允许 cross-contamination。论文应在正文中更清晰解释。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被 R11 赞为 S5/S6 strength，可操作性获认可。\"\n    resolution_round: 11\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R2 提议进一步精确化（W5），R1 REBUT——'first unified analysis...building on prior single-topology analyses' 有事实支撑。Director 支持 R1，claim 准确。\"\n    resolution: \"R1 REBUT 成功。Introduction 措辞准确且有事实支撑。\"\n    resolution_round: 12\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。R11 未再提及。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 R1-W3。共识：不影响核心贡献。\"\n\n  - id: R9-S4\n    category: presentation\n    severity: should-fix\n    summary: \"PPI++ 47.0% vs Table 4 17.0 数字不一致\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    resolution: \"数字实际一致，Reviewer 误读。\"\n    resolution_round: 9\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增强论文对 EMNLP 应用导向读者的说服力。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：R1 交叉回应中确认 ClinicalBERT 案例最接近端到端验证但使用代理 DAG。R2 W4 再次提出需要前瞻性验证。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增加 3-4 句直觉语言解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出（R2-W3）。R1 交叉回应 AGREE——plim 在 Section 3.2 未定义，FWL 在 Section 4.5 才引用但 Appendix 大量依赖。建议 Section 3.1 加 plim 脚注定义 + FWL 首次使用加内联解释。\"\n    action_items:\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: open\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1]\n        note: \"FWL invariance 与 K 无关，PPI++/MC-SIMEX 排名可能随 K 变化。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：R1 W4 + R2 交叉回应 AGREE。PPI++ 在 K>3 需更多 gold labels，MC-SIMEX 外推精度可能下降。建议至少 K=5/K=10 附录验证排名稳定性。\"\n    action_items:\n      - round: 12\n        action: \"补充 K=5/K=10 校正方法对比（至少附录）\"\n        assigned_to: agent\n        status: open\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R12 未单独提出但 R1 Q1 间接涉及。Section 4.2 已有 practitioners 指导句。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：5 篇引用。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 新增缺失引用：VanderWeele (2015) 因果中介标准参考（R2-MR2，R1 AGREE）、Schennach (2020) 非线性测量误差综述（R1-MR1，R2 AGREE）。Stock & Yogo (2005) R1 REBUT——分析目标不同。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 11\n\n  # === Round 12 新发现 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文 Section 5 (Conclusion) 溢出至 p9，违反 EMNLP 2026 的 8 页限制\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R2 首先发现（M5），R1 交叉回应确认。Conclusion 从 p8 下方 1/3 处延续至 p9 顶部约 4-5 行。溢出量极小但 8 页限制是硬约束。建议压缩结论约 4-5 行。\"\n    action_items:\n      - round: 12\n        action: \"压缩 Conclusion 使正文完全收入 8 页\"\n        assigned_to: agent\n        status: open\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语（plim/FWL）对 EMNLP 受众可及性不足\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R2 提出（W3），R1 交叉回应 AGREE。plim 在 Section 3.2 频繁出现但未定义；FWL 在 Section 4.5 引用但未陈述内容。建议 plim 首次使用加脚注 + FWL 首次使用加内联解释。\"\n    action_items:\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 脚注定义和 FWL 内联解释\"\n        assigned_to: agent\n        status: open\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 新发现的缺失引用\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"共识缺失：(1) VanderWeele (2015) 因果中介标准参考——mediation 分析大量使用但未引用（R2-MR2，R1 AGREE）；(2) Schennach (2020) 非线性测量误差综述——讨论非线性扩展可能性（R1-MR1，R2 AGREE）。分歧：Stock & Yogo (2005) 弱 IV——R2 提出，R1 REBUT（分析目标不同）。\"\n\n  - id: R12-MI1\n    category: presentation\n    severity: minor\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果，适用条件未标注\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R1-M2 和 R2-M3 共同提出。Algorithm 1 的 RMSE 阈值来源于 Table 4（K=3, N=1,000），如 K 变化阈值可能失效。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 和 Figure 7 视觉问题\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R1-M1 + R2-W6：Figure 1/2 挤在同一页，caption 字号小。R2 建议 dual-panel 设计。视觉审查补充：Figure 7 使用红绿色板对色盲不友好。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-23T06:46:17.116451+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 29059}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-23T06:48:51.837519+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# Round 12 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**类型**: Long Paper (8 页限制)\n**Reviewer**: R1（方法严谨性）+ R2（新颖性与完整性）\n**轮次**: Round 12 (fresh mode)\n\n---\n\n## Summary\n\n本文研究 K 类（K≥3）LLM 标注误差在因果推断中的拓扑依赖传播机制。作者推导了 7 种 DAG 拓扑下的闭式偏差表达式，证明 K≥3 引入 binary 不存在的符号反转（sign reversal）——exposure 和 IV 拓扑可反转因果效应符号，而 5 种拓扑维持结构性保证。提出 Annotation Sensitivity Values (ASV) 敏感性分析框架，揭示从 IV（最脆弱）到 M-bias（免疫）的脆弱性谱。证明 FWL 不变性使矩阵校正在 4 种协变量拓扑下完全无效（0% bias reduction）。23 个 LLM 配置 × 3 NLP 任务的经验验证与理论预测一致（MAPE 1.6%）。\n\n---\n\n## Strengths\n\n**S1 [共识]: 拓扑依赖框架的系统性填补真实空白。** 将混淆矩阵 C 与 DAG 拓扑的交互效应作为核心分析维度是本文最重要的贡献。Teblunthuis (2024) 仅覆盖 binary×4 DAGs，Lee & Wood-Doughty (2024) 仅覆盖 categorical×1 DAG。本文首次在 K≥3×7 topologies 交叉点提供统一分析框架，发现\"同一混淆矩阵在不同拓扑下产生质的不同偏差\"（R1-S1, R2-S1 共识）。\n\n**S2 [共识]: 证据层次的诚实标注（Proved/Verified/Conjectured）。** 论文对 K=2 提供完整证明（Theorem 1），对 K≥3 明确区分三级证据层次。Table 2 汇总了各拓扑的充分条件和验证状态。这种自我约束在方法论论文中值得肯定（R1-S2, R2-S4 共识）。\n\n**S3 [共识]: 理论-模拟一致性极强。** MAPE 1.6% across 161 scenarios (23 LLM configs × 7 topologies)，有效排除推导中的代数错误，为闭式表达式提供强数值支撑（R1-S3, R2-S1 共识）。\n\n**S4 [共识]: FWL 不变性是干净且有实践价值的负面结果。** 证明矩阵校正（MLA, DSL）在 confounding/mediation/collider/M-bias 下精确 0% bias reduction，直接驳斥\"有混淆矩阵就能校正\"的朴素假设。逻辑回归下不变性经验性保持（<0.005, Table 13）（R1-S4, R2-S3 共识）。\n\n**S5 [共识]: ASV 框架实用性。** 三种互补 ASV 指标（magnitude, significance, sign-flip）覆盖不同实践需求。Sign-flip ASV 识别临界 N*（低于此阈值所有 rejection 被阻断）在 E-value 框架中无对应物。Algorithm 1 提供可直接使用的决策流程（R1-S5, R2-S2/S5 共识）。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**W1 [R1 must-fix / R2 should-fix → Director 判定 should-fix]: Theorem 1 仅限 K=2，K≥3 核心单调性停留在 Conjecture。**\n- 论文标题承诺 \"Multi-Class\" 但 Theorem 1 (envelope monotonicity) 仅对 K=2 成立。K≥3 完全依赖 Observation 1（20,000+ 配置数值验证）和 Conjecture 1（ε<0.06 approximate monotonicity）。\n- R1 评 must-fix（影响核心 claim 可信度），R2 评 should-fix（数值验证规模充分，ASV 实践价值不完全依赖 monotonicity）。\n- **Director 判定 should-fix**：论文已诚实标注三级证据层次，数值验证规模充分（30,000 matrices × K∈{3,5,7}），violation magnitude negligible（≤10⁻¹²）。但论文**应在正文中讨论 Conjecture 1 失效时对 Algorithm 1 实践指导的具体影响**——如果 monotonicity 不严格成立，δ 阈值判定是否仍可靠？\n\n**W2 [R1 must-fix / R2 agree → Director 判定 should-fix]: 非差异性错分假设在 LLM 场景下论证不足。**\n- Definition 1 要求 P(A*|A,Y,Z) = P(A*|A)。Appendix B.5 的 stress test 覆盖 ε=0.10-0.50，但未直接从 23 个 LLM 经验矩阵估计实际差异性程度。\n- R1 评 must-fix，R2 同意问题存在但补充 ε=0.10 更接近实际。\n- **Director 判定 should-fix**：假设在标准 text classification pipeline（LLM 仅看 source text）下合理，stress test 覆盖了有意义的 ε 范围。但论文应从现有 gold label subset 估计实际 differential degree，使参数选择有经验依据。\n\n**W3 [R2 M5, R1 交叉确认 → Director 判定 must-fix]: 正文可能超出 8 页限制。**\n- Section 5 (Conclusion) 从 p8 下方 1/3 处延续至 p9 顶部约 4-5 行。EMNLP 2026 的 8 页正文限制是硬约束（Limitations/ethical considerations 不计入）。\n- **Director 判定 must-fix**：格式违规是 desk reject 风险。必须压缩结论使正文完全收入 8 页。\n\n### Should-Fix\n\n**W4 [R1 W3, R2 W3 共识]: 计量经济学术语对 EMNLP 受众可及性不足。**\n- plim (probability limit) 在 Section 3.2 频繁出现但未定义其直觉含义。FWL (Frisch-Waugh-Lovell) 在 Section 4.5 引用但未陈述定理内容。对 CL/NLP 读者不友好。\n- 建议：Section 3.1 加 plim 脚注定义（\"大样本下估计量收敛到的值\"）；FWL 首次使用加内联解释（\"partialling out controls\"）。\n\n**W5 [R1 W3, R2 W3 共识]: 线性 SEM 假设的正文讨论不足。**\n- Appendix B.6/B.13 的 logistic DGP 验证充分（Table 5, Table 13: sign-flip rate 差异 <0.02, FWL bias reduction <0.005），但正文仅一句 \"structural patterns persist under logistic DGP\"。\n- 建议：Section 4.5 增加 1-2 句总结 logistic 发现 + 显式引用 Appendix B.13。\n\n**W6 [R1 W4, R2 交叉 AGREE]: 校正方法比较仅在 K=3 下进行。**\n- Table 4 的 RMSE reduction 仅覆盖 K=3。FWL 不变性与 K 无关（代数性质），但 PPI++ 和 MC-SIMEX 的相对性能可能随 K 变化——PPI++ 在 K>3 需更多 gold labels，MC-SIMEX 外推精度可能下降。\n- 建议：至少在附录中补充 K=5/K=10 校正方法排名稳定性验证。\n\n**W7 [R1 W6, R2 W4 共识]: 实证验证规模偏小。**\n- 23 个 LLM 配置来自 4 个模型 × 3 任务，缺少商业 API（GPT-4/Claude）、>235B 模型、NER 等结构化标注任务。CivilComments 实际为 K=2，与 K≥3 核心贡献不完全对齐。\n- 两位 Reviewer 共识：不影响核心贡献（理论结果与 LLM 无关），但限制泛化性声明。\n\n**W8 [R2 W2, R1 交叉降为 minor]: Abstract 信息密度过高。**\n- Abstract 包含至少 9-10 个定量信息点，对不熟悉该领域的 EMNLP 读者构成认知负担。\n- 建议：聚焦 2-3 个核心数字（83.4% sign reversal, FWL 0% bias reduction），其余移至 Introduction。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识：\n\n1. **[AGREE] 拓扑依赖框架是真正的新贡献**——K≥3 下 stochastic constraint 打破 binary 结构保证是非平凡理论发现\n2. **[AGREE] 三级证据层次（Proved/Verified/Conjectured）标注诚实**——Table 2 清晰区分各结果证明状态\n3. **[AGREE] FWL 不变性是干净的负面结果**——矩阵校正对 4 种协变量拓扑精确无效\n4. **[AGREE] Conjecture 1 未证明削弱理论完整性**（分歧仅在严重性：must-fix vs should-fix）\n5. **[AGREE] 非差异性假设论证不足**——未从实际 LLM 数据估计差异性程度\n6. **[AGREE] 正文可能超 8 页限制**——Conclusion 溢出至 p9\n7. **[AGREE] EMNLP 受众可及性不足**——plim/FWL 等术语需解释\n8. **[AGREE] 线性 SEM 正文讨论不足**——logistic 结果在附录但正文未引用\n9. **[AGREE] Algorithm 1 阈值硬编码自 K=3**——适用条件未标注\n10. **[AGREE] \"First unified analysis\" 声明准确**（R1 REBUT R2-W5 成功）\n11. **[AGREE] 缺失引用**：VanderWeele (2015) 因果中介标准参考、Schennach (2020) 非线性测量误差综述\n\n## Reviewer Divergence\n\n1. **Conjecture 1 严重性** [分歧保留]\n   - R1: must-fix（标题承诺 Multi-Class 但 Theorem 限 K=2，影响核心 claim 可信度）\n   - R2: should-fix（数值验证规模充分，ASV 实践价值不完全依赖 monotonicity）\n   - Director: 采纳 should-fix（论文已诚实标注，violation magnitude negligible）\n\n2. **ASV bootstrap CI 宽度** [R2 REBUT 成功]\n   - R1 W5: should-fix（CI 跨越安全/不安全分界，影响可操作性）\n   - R2 REBUT: 排名稳定性比绝对值更重要，CI 宽度反映真实参数不确定性而非框架缺陷\n   - Director: 采纳 R2 观点，降为 minor\n\n3. **Stock & Yogo (2005) 引用必要性** [R1 REBUT 成功]\n   - R2: 应引用弱 IV 文献\n   - R1 REBUT: 论文处理的是 instrument measurement error 而非 instrument relevance，分析目标不同\n   - Director: 采纳 R1 观点，可选引用但非必要\n\n---\n\n## Questions\n\n**Q1 [R1, R2 共识]:** K≥3 证明困难的解析直觉是什么？K≥3 的 K²-K 额外自由度允许 off-diagonal 交叉污染（cross-contamination），打破 K=2 的 1-自由度结构约束，使凸性论证不再全局成立。正文应更清晰解释此直觉。\n\n**Q2 [R1]:** 能否从 23 个 LLM 配置的 gold label subset 直接估计实际差异性程度（P(A*|A,Y) vs P(A*|A) 的经验偏离）？这将使 stress test 的 ε 参数选择更有实际依据。\n\n**Q3 [R2]:** ASV 的 diagonal parameterization C(δ) = (1-δ)I + δC₀ 假设所有类别均匀退化。实际中稀有类别退化更快——1D 降维是否遗漏关键信息？建议在 Limitations 讨论多维 ASV 扩展方向。\n\n**Q4 [R2]:** FWL 不变性对非参数/半参数因果推断方法（doubly robust estimators, TMLE）是否仍成立？这关系到 Algorithm 1 对现代因果推断工具箱的适用性。论文应在 Limitations 标注此适用边界。\n\n**Q5 [R2]:** PPI++ 需要 ≥20% gold labels（Table 14）。Algorithm 1 是否需要 cost-aware 版本——讨论 gold label budget 对方法选择的影响？\n\n---\n\n## Missing References\n\n**MR1 [R2 提出, R1 AGREE]:** VanderWeele (2015, \"Explanation in Causal Inference\")——因果中介分析标准参考。论文 mediation 拓扑分析大量使用中介概念但未引用此标准参考。\n\n**MR2 [R1 提出, R2 AGREE]:** Schennach (2020)——非线性/半参数测量误差综述。论文假设线性 SEM 但声称对 NLP 有指导意义，应讨论非线性扩展的可能性和挑战。\n\n**MR3 [R1 提出, R2 AGREE]:** Si et al. (2023, \"Can ChatGPT Replace Traditional Annotation Pipelines?\") 或类似 LLM 标注质量系统评估——补充 non-differential 假设的经验支撑。\n\n**MR4 [R2 提出, R1 REBUT → 可选]:** Stock & Yogo (2005, \"Testing for weak instruments in linear IV regression\")——与 IV 拓扑概念相关但分析目标不同。可作为补充背景。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 critical, 4 warnings, 7 info）。\n\n**Critical:**\n- 前 6 页连续纯文本无任何 figure/table，审稿人在形成第一印象时完全没有视觉锚点。Figure 1（DAG 拓扑图）是核心概念图，应前移至 Introduction（P1-P2）。\n\n**Warnings:**\n- P7 三个 display items（Figure 1 + Figure 2 + Table 1）挤在同一页，每个图表被压缩。Figure 2 直方图细节在当前尺寸下勉强可读。\n- 正文 8.5 页仅 4 个 display items（3 figures + 1 table），主要实验结果表格（Table 3-4）全在 Appendix，审稿人在正文中看不到核心定量结果表格。\n- Appendix P21 三图挤一页，Figure 5（混淆矩阵热力图）色块文字较难辨认。\n- Figure 7（ASV magnitude ranges）使用红绿色板对色盲不友好，建议改用蓝/橙或 Okabe-Ito 色板。\n\n**Info:**\n- Figure 2 建议除颜色外增加 marker shape 区分，提高打印和色盲场景可辨识度。\n- Figure 3 caption 较简短，建议增加\"如何阅读此图\"说明。\n- References 排版正常，无未解析引用。\n- Algorithm 1 伪代码框排版清晰。\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|-----|-----|-------------|\n| Soundness | 3.5/5 | 4/5 | **3.5/5** |\n| Excitement | 3.5/5 | 3.5/5 | **3.5/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### Overall Assessment: 3.5 — Borderline Conference\n\n**推荐：Borderline Conference (3.5)**\n\n论文在一个重要且 timely 的问题上做出了系统性贡献：\n- (+) 拓扑依赖的多类错分偏差分析是真正的新视角，将分散的单拓扑/binary 先前工作统一为 7 topology × K≥3 框架\n- (+) K≥3 sign reversal 发现（83.4% under Dirichlet, 2.1% under realistic accuracy）具有实践警示价值\n- (+) FWL 不变性负面结果干净且有实操指导意义\n- (+) 三级证据层次标注体现学术诚实\n- (+) Algorithm 1 提供可直接使用的决策流程\n\n但存在以下限制使其处于 Conference 门槛边缘：\n- (-) 核心 K≥3 单调性停留在 Conjecture（有充分数值支撑但无解析证明），与标题 \"Multi-Class\" 承诺存在落差\n- (-) 非差异性假设在 LLM 场景下的经验依据不足\n- (-) 对 EMNLP 受众的可及性不足（plim/FWL 未解释，logistic 结果未在正文引用）\n- (-) 实证验证仅 23 个配置，缺少商业 API 和端到端验证\n- (-) 正文可能超 8 页限制（格式风险）\n\n如果 W3（页数）、W4（术语可及性）、W5（logistic 正文讨论）能在 camera-ready 前修复，论文可达到 Conference 水平。如果这些改善无法实现，Findings track 是合理的去向。\n\n### 置信度: 4/5\n两位 Reviewer 仔细检查了核心证明、Monte Carlo 验证设计、stress test 方法论和经验验证设计，对因果推断和测量误差文献有足够背景。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 叙事结构清晰：从 LLM 标注趋势 → K≥3 结构性转变 → F1 不预测因果风险 → 三个贡献\n- \"first unified analysis...building on prior single-topology analyses\" 措辞准确（R1 REBUT R2-W5 确认）\n- 建议减少 Abstract 中的定量信息点至 2-3 个\n\n### Section 3 (Method)\n- Section 3.1: plim 未定义直觉含义，建议加脚注\n- Section 3.2: 7 种拓扑的偏差表达式推导清晰，Proposition 1 的 (a)(b)(c) 条件结构合理\n- Section 3.3: ASV 的 K²→1D 降维和三类指标设计合理；Theorem 1 限 K=2 已正确标注；proof obstacle 解释（perspective function convexity 在 K≥3 失效）应更清晰\n- **建议增加 ASV-vs-E-value 显式对比**：sign-flip ASV 和 N* 是 E-value 无对应物的新贡献\n\n### Section 4 (Experiments)\n- Section 4.2: Table 1 三级符号（✓/✓*/✗）清晰\n- Section 4.3: ASV ranking（IV 最脆弱 → M-bias 免疫）跨 DGP 稳定\n- Section 4.4: 经验验证（23 configs, 161 scenarios, MAPE 1.6%）充分但规模可更大\n- Section 4.5: 校正指导有实践价值，但 K=3 限制应明确标注；FWL 适用边界（仅线性/logistic）应标注\n\n### Section 5 (Conclusion) + Limitations\n- Conclusion 溢出至 p9，必须压缩\n- Limitations 覆盖了 non-differential 假设、线性 SEM、LLM 覆盖度——内容合理但可补充 ASV diagonal parameterization 假设\n- 建议补充：FWL 不变性对非参数方法不适用的显式声明\n\n### Appendix\n- 证明完整（A.1-A.8），数值验证详实（B.1-B.17）\n- ClinicalBERT 案例（B.3）和 Political Ad Tone 案例（B.17）有实践价值，建议在正文中引用\n- 附录材料是论文的重要支撑，Reproducibility 条件充分"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# Round 12 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**类型**: Long Paper (8 页限制)\n**Reviewer**: R1（方法严谨性）+ R2（新颖性与完整性）\n**轮次**: Round 12 (fresh mode)\n\n---\n\n## Summary\n\n本文研究 K 类（K≥3）LLM 标注误差在因果推断中的拓扑依赖传播机制。作者推导了 7 种 DAG 拓扑下的闭式偏差表达式，证明 K≥3 引入 binary 不存在的符号反转（sign reversal）——exposure 和 IV 拓扑可反转因果效应符号，而 5 种拓扑维持结构性保证。提出 Annotation Sensitivity Values (ASV) 敏感性分析框架，揭示从 IV（最脆弱）到 M-bias（免疫）的脆弱性谱。证明 FWL 不变性使矩阵校正在 4 种协变量拓扑下完全无效（0% bias reduction）。23 个 LLM 配置 × 3 NLP 任务的经验验证与理论预测一致（MAPE 1.6%）。\n\n---\n\n## Strengths\n\n**S1 [共识]: 拓扑依赖框架的系统性填补真实空白。** 将混淆矩阵 C 与 DAG 拓扑的交互效应作为核心分析维度是本文最重要的贡献。Teblunthuis (2024) 仅覆盖 binary×4 DAGs，Lee & Wood-Doughty (2024) 仅覆盖 categorical×1 DAG。本文首次在 K≥3×7 topologies 交叉点提供统一分析框架，发现\"同一混淆矩阵在不同拓扑下产生质的不同偏差\"（R1-S1, R2-S1 共识）。\n\n**S2 [共识]: 证据层次的诚实标注（Proved/Verified/Conjectured）。** 论文对 K=2 提供完整证明（Theorem 1），对 K≥3 明确区分三级证据层次。Table 2 汇总了各拓扑的充分条件和验证状态。这种自我约束在方法论论文中值得肯定（R1-S2, R2-S4 共识）。\n\n**S3 [共识]: 理论-模拟一致性极强。** MAPE 1.6% across 161 scenarios (23 LLM configs × 7 topologies)，有效排除推导中的代数错误，为闭式表达式提供强数值支撑（R1-S3, R2-S1 共识）。\n\n**S4 [共识]: FWL 不变性是干净且有实践价值的负面结果。** 证明矩阵校正（MLA, DSL）在 confounding/mediation/collider/M-bias 下精确 0% bias reduction，直接驳斥\"有混淆矩阵就能校正\"的朴素假设。逻辑回归下不变性经验性保持（<0.005, Table 13）（R1-S4, R2-S3 共识）。\n\n**S5 [共识]: ASV 框架实用性。** 三种互补 ASV 指标（magnitude, significance, sign-flip）覆盖不同实践需求。Sign-flip ASV 识别临界 N*（低于此阈值所有 rejection 被阻断）在 E-value 框架中无对应物。Algorithm 1 提供可直接使用的决策流程（R1-S5, R2-S2/S5 共识）。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**W1 [R1 must-fix / R2 should-fix → Director 判定 should-fix]: Theorem 1 仅限 K=2，K≥3 核心单调性停留在 Conjecture。**\n- 论文标题承诺 \"Multi-Class\" 但 Theorem 1 (envelope monotonicity) 仅对 K=2 成立。K≥3 完全依赖 Observation 1（20,000+ 配置数值验证）和 Conjecture 1（ε<0.06 approximate monotonicity）。\n- R1 评 must-fix（影响核心 claim 可信度），R2 评 should-fix（数值验证规模充分，ASV 实践价值不完全依赖 monotonicity）。\n- **Director 判定 should-fix**：论文已诚实标注三级证据层次，数值验证规模充分（30,000 matrices × K∈{3,5,7}），violation magnitude negligible（≤10⁻¹²）。但论文**应在正文中讨论 Conjecture 1 失效时对 Algorithm 1 实践指导的具体影响**——如果 monotonicity 不严格成立，δ 阈值判定是否仍可靠？\n\n**W2 [R1 must-fix / R2 agree → Director 判定 should-fix]: 非差异性错分假设在 LLM 场景下论证不足。**\n- Definition 1 要求 P(A*|A,Y,Z) = P(A*|A)。Appendix B.5 的 stress test 覆盖 ε=0.10-0.50，但未直接从 23 个 LLM 经验矩阵估计实际差异性程度。\n- R1 评 must-fix，R2 同意问题存在但补充 ε=0.10 更接近实际。\n- **Director 判定 should-fix**：假设在标准 text classification pipeline（LLM 仅看 source text）下合理，stress test 覆盖了有意义的 ε 范围。但论文应从现有 gold label subset 估计实际 differential degree，使参数选择有经验依据。\n\n**W3 [R2 M5, R1 交叉确认 → Director 判定 must-fix]: 正文可能超出 8 页限制。**\n- Section 5 (Conclusion) 从 p8 下方 1/3 处延续至 p9 顶部约 4-5 行。EMNLP 2026 的 8 页正文限制是硬约束（Limitations/ethical considerations 不计入）。\n- **Director 判定 must-fix**：格式违规是 desk reject 风险。必须压缩结论使正文完全收入 8 页。\n\n### Should-Fix\n\n**W4 [R1 W3, R2 W3 共识]: 计量经济学术语对 EMNLP 受众可及性不足。**\n- plim (probability limit) 在 Section 3.2 频繁出现但未定义其直觉含义。FWL (Frisch-Waugh-Lovell) 在 Section 4.5 引用但未陈述定理内容。对 CL/NLP 读者不友好。\n- 建议：Section 3.1 加 plim 脚注定义（\"大样本下估计量收敛到的值\"）；FWL 首次使用加内联解释（\"partialling out controls\"）。\n\n**W5 [R1 W3, R2 W3 共识]: 线性 SEM 假设的正文讨论不足。**\n- Appendix B.6/B.13 的 logistic DGP 验证充分（Table 5, Table 13: sign-flip rate 差异 <0.02, FWL bias reduction <0.005），但正文仅一句 \"structural patterns persist under logistic DGP\"。\n- 建议：Section 4.5 增加 1-2 句总结 logistic 发现 + 显式引用 Appendix B.13。\n\n**W6 [R1 W4, R2 交叉 AGREE]: 校正方法比较仅在 K=3 下进行。**\n- Table 4 的 RMSE reduction 仅覆盖 K=3。FWL 不变性与 K 无关（代数性质），但 PPI++ 和 MC-SIMEX 的相对性能可能随 K 变化——PPI++ 在 K>3 需更多 gold labels，MC-SIMEX 外推精度可能下降。\n- 建议：至少在附录中补充 K=5/K=10 校正方法排名稳定性验证。\n\n**W7 [R1 W6, R2 W4 共识]: 实证验证规模偏小。**\n- 23 个 LLM 配置来自 4 个模型 × 3 任务，缺少商业 API（GPT-4/Claude）、>235B 模型、NER 等结构化标注任务。CivilComments 实际为 K=2，与 K≥3 核心贡献不完全对齐。\n- 两位 Reviewer 共识：不影响核心贡献（理论结果与 LLM 无关），但限制泛化性声明。\n\n**W8 [R2 W2, R1 交叉降为 minor]: Abstract 信息密度过高。**\n- Abstract 包含至少 9-10 个定量信息点，对不熟悉该领域的 EMNLP 读者构成认知负担。\n- 建议：聚焦 2-3 个核心数字（83.4% sign reversal, FWL 0% bias reduction），其余移至 Introduction。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识：\n\n1. **[AGREE] 拓扑依赖框架是真正的新贡献**——K≥3 下 stochastic constraint 打破 binary 结构保证是非平凡理论发现\n2. **[AGREE] 三级证据层次（Proved/Verified/Conjectured）标注诚实**——Table 2 清晰区分各结果证明状态\n3. **[AGREE] FWL 不变性是干净的负面结果**——矩阵校正对 4 种协变量拓扑精确无效\n4. **[AGREE] Conjecture 1 未证明削弱理论完整性**（分歧仅在严重性：must-fix vs should-fix）\n5. **[AGREE] 非差异性假设论证不足**——未从实际 LLM 数据估计差异性程度\n6. **[AGREE] 正文可能超 8 页限制**——Conclusion 溢出至 p9\n7. **[AGREE] EMNLP 受众可及性不足**——plim/FWL 等术语需解释\n8. **[AGREE] 线性 SEM 正文讨论不足**——logistic 结果在附录但正文未引用\n9. **[AGREE] Algorithm 1 阈值硬编码自 K=3**——适用条件未标注\n10. **[AGREE] \"First unified analysis\" 声明准确**（R1 REBUT R2-W5 成功）\n11. **[AGREE] 缺失引用**：VanderWeele (2015) 因果中介标准参考、Schennach (2020) 非线性测量误差综述\n\n## Reviewer Divergence\n\n1. **Conjecture 1 严重性** [分歧保留]\n   - R1: must-fix（标题承诺 Multi-Class 但 Theorem 限 K=2，影响核心 claim 可信度）\n   - R2: should-fix（数值验证规模充分，ASV 实践价值不完全依赖 monotonicity）\n   - Director: 采纳 should-fix（论文已诚实标注，violation magnitude negligible）\n\n2. **ASV bootstrap CI 宽度** [R2 REBUT 成功]\n   - R1 W5: should-fix（CI 跨越安全/不安全分界，影响可操作性）\n   - R2 REBUT: 排名稳定性比绝对值更重要，CI 宽度反映真实参数不确定性而非框架缺陷\n   - Director: 采纳 R2 观点，降为 minor\n\n3. **Stock & Yogo (2005) 引用必要性** [R1 REBUT 成功]\n   - R2: 应引用弱 IV 文献\n   - R1 REBUT: 论文处理的是 instrument measurement error 而非 instrument relevance，分析目标不同\n   - Director: 采纳 R1 观点，可选引用但非必要\n\n---\n\n## Questions\n\n**Q1 [R1, R2 共识]:** K≥3 证明困难的解析直觉是什么？K≥3 的 K²-K 额外自由度允许 off-diagonal 交叉污染（cross-contamination），打破 K=2 的 1-自由度结构约束，使凸性论证不再全局成立。正文应更清晰解释此直觉。\n\n**Q2 [R1]:** 能否从 23 个 LLM 配置的 gold label subset 直接估计实际差异性程度（P(A*|A,Y) vs P(A*|A) 的经验偏离）？这将使 stress test 的 ε 参数选择更有实际依据。\n\n**Q3 [R2]:** ASV 的 diagonal parameterization C(δ) = (1-δ)I + δC₀ 假设所有类别均匀退化。实际中稀有类别退化更快——1D 降维是否遗漏关键信息？建议在 Limitations 讨论多维 ASV 扩展方向。\n\n**Q4 [R2]:** FWL 不变性对非参数/半参数因果推断方法（doubly robust estimators, TMLE）是否仍成立？这关系到 Algorithm 1 对现代因果推断工具箱的适用性。论文应在 Limitations 标注此适用边界。\n\n**Q5 [R2]:** PPI++ 需要 ≥20% gold labels（Table 14）。Algorithm 1 是否需要 cost-aware 版本——讨论 gold label budget 对方法选择的影响？\n\n---\n\n## Missing References\n\n**MR1 [R2 提出, R1 AGREE]:** VanderWeele (2015, \"Explanation in Causal Inference\")——因果中介分析标准参考。论文 mediation 拓扑分析大量使用中介概念但未引用此标准参考。\n\n**MR2 [R1 提出, R2 AGREE]:** Schennach (2020)——非线性/半参数测量误差综述。论文假设线性 SEM 但声称对 NLP 有指导意义，应讨论非线性扩展的可能性和挑战。\n\n**MR3 [R1 提出, R2 AGREE]:** Si et al. (2023, \"Can ChatGPT Replace Traditional Annotation Pipelines?\") 或类似 LLM 标注质量系统评估——补充 non-differential 假设的经验支撑。\n\n**MR4 [R2 提出, R1 REBUT → 可选]:** Stock & Yogo (2005, \"Testing for weak instruments in linear IV regression\")——与 IV 拓扑概念相关但分析目标不同。可作为补充背景。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 critical, 4 warnings, 7 info）。\n\n**Critical:**\n- 前 6 页连续纯文本无任何 figure/table，审稿人在形成第一印象时完全没有视觉锚点。Figure 1（DAG 拓扑图）是核心概念图，应前移至 Introduction（P1-P2）。\n\n**Warnings:**\n- P7 三个 display items（Figure 1 + Figure 2 + Table 1）挤在同一页，每个图表被压缩。Figure 2 直方图细节在当前尺寸下勉强可读。\n- 正文 8.5 页仅 4 个 display items（3 figures + 1 table），主要实验结果表格（Table 3-4）全在 Appendix，审稿人在正文中看不到核心定量结果表格。\n- Appendix P21 三图挤一页，Figure 5（混淆矩阵热力图）色块文字较难辨认。\n- Figure 7（ASV magnitude ranges）使用红绿色板对色盲不友好，建议改用蓝/橙或 Okabe-Ito 色板。\n\n**Info:**\n- Figure 2 建议除颜色外增加 marker shape 区分，提高打印和色盲场景可辨识度。\n- Figure 3 caption 较简短，建议增加\"如何阅读此图\"说明。\n- References 排版正常，无未解析引用。\n- Algorithm 1 伪代码框排版清晰。\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|-----|-----|-------------|\n| Soundness | 3.5/5 | 4/5 | **3.5/5** |\n| Excitement | 3.5/5 | 3.5/5 | **3.5/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### Overall Assessment: 3.5 — Borderline Conference\n\n**推荐：Borderline Conference (3.5)**\n\n论文在一个重要且 timely 的问题上做出了系统性贡献：\n- (+) 拓扑依赖的多类错分偏差分析是真正的新视角，将分散的单拓扑/binary 先前工作统一为 7 topology × K≥3 框架\n- (+) K≥3 sign reversal 发现（83.4% under Dirichlet, 2.1% under realistic accuracy）具有实践警示价值\n- (+) FWL 不变性负面结果干净且有实操指导意义\n- (+) 三级证据层次标注体现学术诚实\n- (+) Algorithm 1 提供可直接使用的决策流程\n\n但存在以下限制使其处于 Conference 门槛边缘：\n- (-) 核心 K≥3 单调性停留在 Conjecture（有充分数值支撑但无解析证明），与标题 \"Multi-Class\" 承诺存在落差\n- (-) 非差异性假设在 LLM 场景下的经验依据不足\n- (-) 对 EMNLP 受众的可及性不足（plim/FWL 未解释，logistic 结果未在正文引用）\n- (-) 实证验证仅 23 个配置，缺少商业 API 和端到端验证\n- (-) 正文可能超 8 页限制（格式风险）\n\n如果 W3（页数）、W4（术语可及性）、W5（logistic 正文讨论）能在 camera-ready 前修复，论文可达到 Conference 水平。如果这些改善无法实现，Findings track 是合理的去向。\n\n### 置信度: 4/5\n两位 Reviewer 仔细检查了核心证明、Monte Carlo 验证设计、stress test 方法论和经验验证设计，对因果推断和测量误差文献有足够背景。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 叙事结构清晰：从 LLM 标注趋势 → K≥3 结构性转变 → F1 不预测因果风险 → 三个贡献\n- \"first unified analysis...building on prior single-topology analyses\" 措辞准确（R1 REBUT R2-W5 确认）\n- 建议减少 Abstract 中的定量信息点至 2-3 个\n\n### Section 3 (Method)\n- Section 3.1: plim 未定义直觉含义，建议加脚注\n- Section 3.2: 7 种拓扑的偏差表达式推导清晰，Proposition 1 的 (a)(b)(c) 条件结构合理\n- Section 3.3: ASV 的 K²→1D 降维和三类指标设计合理；Theorem 1 限 K=2 已正确标注；proof obstacle 解释（perspective function convexity 在 K≥3 失效）应更清晰\n- **建议增加 ASV-vs-E-value 显式对比**：sign-flip ASV 和 N* 是 E-value 无对应物的新贡献\n\n### Section 4 (Experiments)\n- Section 4.2: Table 1 三级符号（✓/✓*/✗）清晰\n- Section 4.3: ASV ranking（IV 最脆弱 → M-bias 免疫）跨 DGP 稳定\n- Section 4.4: 经验验证（23 configs, 161 scenarios, MAPE 1.6%）充分但规模可更大\n- Section 4.5: 校正指导有实践价值，但 K=3 限制应明确标注；FWL 适用边界（仅线性/logistic）应标注\n\n### Section 5 (Conclusion) + Limitations\n- Conclusion 溢出至 p9，必须压缩\n- Limitations 覆盖了 non-differential 假设、线性 SEM、LLM 覆盖度——内容合理但可补充 ASV diagonal parameterization 假设\n- 建议补充：FWL 不变性对非参数方法不适用的显式声明\n\n### Appendix\n- 证明完整（A.1-A.8），数值验证详实（B.1-B.17）\n- ClinicalBERT 案例（B.3）和 Political Ad Tone 案例（B.17）有实践价值，建议在正文中引用\n- 附录材料是论文的重要支撑，Reproducibility 条件充分"
  }
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-23T06:48:56.159105+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4321
}
```

</details>

---


### Assistant

_source line 988 · 2026-05-23T06:49:10.424319+00:00_

审稿报告已投递。

**Round 12 审稿结果摘要**：

**Overall: 3.5/5 — Borderline Conference**

两位 Reviewer 评分一致（R1: 3.5, R2: 3.5），关键共识与分歧如下：

**核心优势**：
- 拓扑依赖框架系统性填补真实空白（K≥3 × 7 topologies）
- 83.4% sign reversal 发现和 FWL 不变性负面结果有实践价值
- 三级证据层次标注体现学术诚实
- Algorithm 1 提供可操作的决策流程

**待修复问题**：
- **must-fix**: 正文 Conclusion 溢出至 p9（~4-5 行），违反 8 页限制
- **should-fix**: Conjecture 1 未证明（R1/R2 分歧保留但 Director 判 should-fix）、非差异性假设经验依据不足、plim/FWL 术语可及性、logistic 结果正文未引用、校正方法仅 K=3、LLM 配置规模偏小、Abstract 数字过密
- **缺失引用**: VanderWeele (2015)、Schennach (2020)

**建议**：如果页数、术语可及性和 logistic 讨论能在 camera-ready 前修复，论文可达到 Conference 水平；否则 Findings 是合理去向。

Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 97

## Round 97

2 recorded events


### User

_source line 989 · 2026-05-23T06:49:13.109119+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 6 个 Weakness 中 5 个 AGREE（W1-W4, W6），1 个 REBUT（W5 "First unified analysis" 声明有事实支撑）；4 个 Question 全部 AGREE；Missing References 中 1 个 REBUT（MR1 Stock & Yogo 与本文分析目标不同）、2 个 AGREE（MR2, MR3）。核心分歧在 Soundness 评分：我维持 3.5/5（vs R2 的 4/5），理由是 Conjecture 1 的缺口直接影响论文核心 "Multi-Class" 承诺的可信度。两位 reviewer 在 Overall 3.5 (Borderline Conference) 上一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 990 · 2026-05-23T06:49:27.213602+00:00_

圆桌审稿已完成。

**最终结果：Overall 3.5/5 — Borderline Conference**

两位 Reviewer 在 Overall 3.5、Excitement 3.5 上完全一致。审稿报告已投递给 Research Director。

**核心发现摘要：**

| 类别 | 问题数 | 关键项 |
|------|--------|--------|
| Must-fix | 1 | 正文溢出 8 页限制（~4-5 行） |
| Should-fix | 7 | Conjecture 1 未证明、非差异性假设论证不足、术语可及性、线性 SEM 正文讨论、校正方法 K=3 限制、实证规模偏小、Abstract 过密 |
| Minor | 3 | ASV CI 宽度、Algorithm 1 硬编码阈值、Figure 视觉问题 |
| 缺失引用 | 3 | VanderWeele (2015)、Schennach (2020)、Si et al. (2023) |

**唯一未收敛分歧**：Conjecture 1 严重性（R1: must-fix vs R2: should-fix），Director 采纳 should-fix。

Issue Tracker 已同步更新至 `review_issues.yaml`。视觉审查结果（1 critical: 前 6 页无 figure）已纳入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 98

## Round 98

50 recorded events


### User

_source line 991 · 2026-05-23T09:19:12.167106+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-23T09:19:17.491368+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-23T09:19:17.592781+00:00_

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
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-23T09:19:26.680461+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-23T09:19:26.680826+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-23T09:19:30.997295+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-23T09:19:32.001848+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-23T09:19:32.052776+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-23T09:19:32.053149+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-23T09:19:33.358915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-23T09:19:33.409659+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	
20	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
24	\graphicspath{{../../figures/paper/}}
25	
26	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	
35	\input{introduction}
36	
37	\begin{figure*}[t]
38	\centering
39	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
40	\vspace{-6pt}
41	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
42	\label{fig:dag_taxonomy}
43	\end{figure*}
44	
45	\input{related_work}
46	
47	\input{method}
48	
49	% ── Figures ──
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
54	\vspace{-6pt}
55	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
56	\label{fig:bias_distribution}
57	\end{figure*}
58	
59	\input{experiments}
60	
61	\input{conclusion}
62	
63	\bibliography{references}
64	
65	\appendix
66	\input{appendix_proofs}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-23T09:19:38.781951+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 1003 · 2026-05-23T09:19:41.342780+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1004 · 2026-05-23T09:19:42.096319+00:00_

-rw-r--r-- 1 ubuntu ubuntu 926825 May 23 09:14 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1005 · 2026-05-23T09:19:42.247243+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 1006 · 2026-05-23T09:19:42.297848+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-23T09:19:46.319907+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 papers through ARR:

## General Paper Types
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR-Specific Policies
For the ARR 2026 May cycle, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026—ARR 2026 May submissions that do not select E
…[truncated 658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7537
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-23T09:19:57.364197+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit long paper short paper guidelines",
  "allowed_domains": "['2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit long paper short paper guidelines",
    "allowed_domains": "['2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 1009 · 2026-05-23T09:19:57.565503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1010 · 2026-05-23T09:19:57.566003+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy, sign reversal occurs in 2.1\% of exposure configurations, exclusively in secondary coefficients with small effect sizes; no sign reversals occur for all other topologies including IV. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1011 · 2026-05-23T09:19:57.617378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1012 · 2026-05-23T09:19:57.617982+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, however, is never reversed in any t
…[truncated 2874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1013 · 2026-05-23T09:19:57.618359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1014 · 2026-05-23T09:19:57.920658+00:00_

1	issues:
2	  # === Round 1-7 历史 (resolved，保留摘要) ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 7
11	    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
12	    resolution_round: 7
13	
14	  - id: R1-N2
15	    category: soundness
16	    severity: should-fix
17	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
18	    status: resolved
19	    first_raised_round: 1
20	    last_seen_round: 3
21	    resolution: "Abstract 已准确区分 prove/verify。"
22	    resolution_round: 4
23	
24	  - id: R1-N3
25	    category: soundness
26	    severity: must-fix
27	    summary: "ASV C(δ) 定义域错误"
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 1
31	    resolution: "Section 3.3 已引入 δ_max 约束。"
32	    resolution_round: 2
33	
34	  - id: R2-N1
35	    category: presentation
36	    severity: must-fix
37	    summary: "83.4% sign reversal headline framing 过度声称"
38	    status: resolved
39	    first_raised_round: 1
40	    last_seen_round: 5
41	    resolution: "Introduction 已重写。"
42	    resolution_round: 5
43	
44	  - id: R2-N2
45	    category: novelty
46	    severity: should-fix
47	    summary: "'first systematic framework' 过度声明"
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1
51	    resolution: "已修复。"
52	    resolution_round: 2
53	
54	  - id: R2-N3
55	    category: related_work
56	    severity: must-fix
57	    summary: "4 篇关键相关工作未引用"
58	    status: resolved
59	    first_raised_round: 1
60	    last_seen_round: 1
61	    resolution: "已修复。"
62	    resolution_round: 2
63	
64	  - id: R1-W2
65	    category: clarity
66	    severity: should-fix
67	    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
68	    status: resolved
69	    first_raised_round: 1
70	    last_seen_round: 2
71	    resolution: "Section 3.2 已添加 ASV 替代讨论。"
72	    resolution_
…[truncated 32345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-23T09:20:27.687886+00:00_

Web search results for query: "EMNLP 2026 submission format page limit long paper short paper guidelines"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

Let me search for more specific information about the main conference paper format guidelines, particularly for long and short papers.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Physician- and Large Language Model-Generated Hospit
…[truncated 4017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 30323
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-23T09:20:48.220075+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-23T09:20:48.973914+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This holds in standard annotation pipelines where the LLM receives only source text and classifies without observing the outcome or covariates---the typical setup in computational social science~\cite{ziems2024can}. Empirical verification using topic-stratified confusion matrices confirms cross-group stability (Appendix~\ref{sec:nondiff_verify}). Violations arise when pretraining data encodes $A$--$Y$ associations, outcome-conditional prompting is used, or retrieval pipelines surface $Y$-correlated documents. Our stress test (Appendix~\ref{sec:nondiff_stress}) shows uniform violations below $\varepsilon{=}0.05$ cause $<$3~pp degradation; outcome-conditional violations can exceed uniform predictions while label-specific violations are milder. When non-differential misclassification is violated for $K{\geq}3$ exposure, even $\varepsilon{=}0.01$ structured departure produces sign reversal in 14 of 16 empirical configurations (Appendix~\ref{sec:realistic_epsilon}).
15	
16	We study seven canonical DAG topologies (Figure~\ref{
…[truncated 13920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-23T09:20:49.125010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-23T09:20:49.527018+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.3\% (confounding) to 3.7\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient. The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five of seven topologies exhibit zero sign-flip rate across all sampled matrices (Table~\ref{tab:taxonomy}). Confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse th
…[truncated 7479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-23T09:20:49.527469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-23T09:20:49.678248+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: the binary attenuation guarantee breaks at $K \geq 3$, where exposure and IV produce sign reversal while five topologies preserve signs. ASVs reveal a vulnerability spectrum from IV (most fragile) to M-bias (immune); matrix-based corrections are provably ineffective for four covariate topologies due to FWL invariance, with all patterns persisting under logistic DGP. Code and data will be released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information; a stress test (Appendix~\ref{sec:nondiff_stress}) shows that structured violation patterns can exceed or fall below uniform predictions. Closed-form expressions are derived under $K{=}3$ linear structural equations; extensions to arbitrary $K$ and nonlinear models~\cite{schennach2020mismeasured} remain open (Appendix~\ref{sec:logistic_dgp}), though correction method rankings are stable across $K{=}3,5,10$ (Spearman $\rho \geq 0.80$, with PPI++ degrading at $K{=}10$; Appendix~\ref{sec:correction_k_sensitivity}). The ASV diagonal parameterization $C(\delta) = (1{-}\delta)I + \delta C_0$ assumes uniform degradation across categories; rare-class-specific degradation would require multi-dimensional extensions. FWL invariance holds under linear OLS and approximately under logistic regression; applicability to non-parametric methods (doubly robust estimators, TMLE) remains unverified. Our 23 configurations span four open-weight LLMs (7B--235B) with diagonal accuracy 0.61--0.83; commercial models and ordinal tasks remain untested.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-23T09:20:49.678613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-23T09:20:49.779236+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayya_sedoc2024} propose str
…[truncated 2179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-23T09:20:55.551892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-23T09:20:56.154877+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 1253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-23T09:20:56.205612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-23T09:20:57.009362+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@article{cinelli2020making,
5	  author    = {Cinelli, Carlos and Hazlett, Chad},
6	  title     = {Making Sense of Sensitivity: Extending Omitted Variable Bias},
7	  journal   = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
8	  year      = {2020},
9	  volume    = {82},
10	  number    = {1},
11	  pages     = {39--67},
12	  doi       = {10.1111/rssb.12348},
13	}
14	
15	@article{gilardi2023chatgpt,
16	  author    = {Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma\"{e}l},
17	  title     = {{ChatGPT} Outperforms Crowd Workers for Text-Annotation Tasks},
18	  journal   = {Proceedings of the National Academy of Sciences},
19	  year      = {2023},
20	  volume    = {120},
21	  number    = {30},
22	  pages     = {e2305016120},
23	  doi       = {10.1073/pnas.2305016120},
24	}
25	
26	@article{ziems2024can,
27	  author    = {Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},
28	  title     = {Can Large Language Models Transform Computational Social Science?},
29	  journal   = {Computational Linguistics},
30	  year      = {2024},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-23T09:20:57.059971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-23T09:20:57.110699+00:00_

This PDF has 30 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-23T09:21:02.080682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf",
  "pages": "7-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf",
    "pages": "7-10"
  }
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-23T09:21:02.382363+00:00_

PDF pages extracted: 4 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf (905.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-23T09:21:37.630924+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 1033 · 2026-05-23T09:21:38.134886+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1034 · 2026-05-23T09:22:12.153485+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 34522
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-23T09:22:12.153829+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 34018
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-23T09:22:12.354911+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性和实验验证**。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 投稿类别：Long Paper\n- 截止日期：2026-05-25\n- 正文限制：8 页（参考文献、Limitations、Ethical Considerations 不计入）\n- 模板：ACL（`\\usepackage[review]{acl}`）\n- 匿名规则：Double-blind\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 主文件：`docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf`（30页，含附录）\n\n## 你的审查侧重\n\n### 1. 理论证明的严谨性\n- **Theorem 1**（K=2 envelope monotonicity）：证明是否完整？条件（proportional effects, $(C_0)_{jj} \\geq 1/2$）是否充分？\n- **Proposition 1**（sign preservation）：confounding 和 collider 的解析证明是否严密？条件是否过强/过弱？\n- **Conjecture 1**（ε-approximate monotonicity for K≥3）：数值验证规模（30,000 matrices per topology）是否足够？ε=0.06 的 bound 是否有意义？标题承诺 \"Multi-Class\" 但核心 Theorem 限 K=2——是否有断裂？\n- **Observation 1**（K≥3 monotonicity）：20,000 triples 的验证是否充分建立了 claim？\n\n### 2. 核心假设的合理性\n- **Non-differential misclassification**（Definition 1）：在 LLM 标注场景下该假设何时成立、何时被违反？论文的 stress test（Appendix B.6）是否充分？特别关注：是否直接估计了实际 LLM 系统的 differential degree？\n- **Proportional effects**（f=λg）：在 NLP 应用中是否可验证？论文报告 15-17% failure rate——这对结论有何影响？λ(C)∉[0,1] 时物理含义是什么？\n- **线性 SEM**：对 EMNLP 社区是否过于局限？Appendix 中的 logistic DGP 验证是否在正文中充分引用？\n\n### 3. Bias Expressions 推导\n- 七种拓扑的 bias 表达式是否正确推导？\n- Exposure (Eq.2) 的权重 w_jk 是否正确描述？sign reversal 的条件是否清晰？\n- IV Wald estimator 的不稳定性分析是否完整？\n- FWL invariance 结论是否严格成立？证明是否完整？\n\n### 4. 实验设计和统计方法\n- Monte Carlo 验证（N=10,000, 100,000 Dirichlet matrices）：设计是否合理？MAPE 1.6% 的评估标准是否恰当？\n- ASV 的 Bootstrap CI 方法是否合理？CI 过宽是否影响可操作性？\n- 经验验证（23 LLM 配置, 161 scenarios）：覆盖范围是否充分？缺少商业 LLM（GPT-4/Claude）和 >235B 模型是否构成重大局限？\n- 校正方法比较（Table 4, K=3/5/10）：实验设计是否公平？PPI++ 在 K=10 退化的解释是否充分？\n- Cross-K robustness (K=3,5,7,10)：是否充分验证了结论的 K 无关性？\n\n### 5. 数值一致性\n- Abstract/Introduction 中的数字是否与 Experiments section 一致？\n- Table 1 的数字是否与正文描述一致？\n- Correction method ranking 在不同 section 的引用是否一致？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n（2-3句概述论文）\n\n## Strengths\nS1. ...\nS2. ...\n...\n\n## Weaknesses\nW1. [severity: must-fix/should-fix/minor] ...\nW2. ...\n...\n\n## Questions\nQ1. ...\nQ2. ...\n...\n\n## Missing References\nMR1. ...\n...\n\n## Minor Issues\nMI1. ...\n...\n\n## Overall Assessment\nScore: X.X\nConfidence: high/medium/low\n一句话总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性和实验验证**。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 投稿类别：Long Paper\n- 截止日期：2026-05-25\n- 正文限制：8 页（参考文献、Limitations、Ethical Considerations 不计入）\n- 模板：ACL（`\\usepackage[review]{acl}`）\n- 匿名规则：Double-blind\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 主文件：`docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf`（30页，含附录）\n\n## 你的审查侧重\n\n### 1. 理论证明的严谨性\n- **Theorem 1**（K=2 envelope monotonicity）：证明是否完整？条件（proportional effects, $(C_0)_{jj} \\geq 1/2$）是否充分？\n- **Proposition 1**（sign preservation）：confounding 和 collider 的解析证明是否严密？条件是否过强/过弱？\n- **Conjecture 1**（ε-approximate monotonicity for K≥3）：数值验证规模（30,000 matrices per topology）是否足够？ε=0.06 的 bound 是否有意义？标题承诺 \"Multi-Class\" 但核心 Theorem 限 K=2——是否有断裂？\n- **Observation 1**（K≥3 monotonicity）：20,000 triples 的验证是否充分建立了 claim？\n\n### 2. 核心假设的合理性\n- **Non-differential misclassification**（Definition 1）：在 LLM 标注场景下该假设何时成立、何时被违反？论文的 stress test（Appendix B.6）是否充分？特别关注：是否直接估计了实际 LLM 系统的 differential degree？\n- **Proportional effects**（f=λg）：在 NLP 应用中是否可验证？论文报告 15-17% failure rate——这对结论有何影响？λ(C)∉[0,1] 时物理含义是什么？\n- **线性 SEM**：对 EMNLP 社区是否过于局限？Appendix 中的 logistic DGP 验证是否在正文中充分引用？\n\n### 3. Bias Expressions 推导\n- 七种拓扑的 bias 表达式是否正确推导？\n- Exposure (Eq.2) 的权重 w_jk 是否正确描述？sign reversal 的条件是否清晰？\n- IV Wald estimator 的不稳定性分析是否完整？\n- FWL invariance 结论是否严格成立？证明是否完整？\n\n### 4. 实验设计和统计方法\n- Monte Carlo 验证（N=10,000, 100,000 Dirichlet matrices）：设计是否合理？MAPE 1.6% 的评估标准是否恰当？\n- ASV 的 Bootstrap CI 方法是否合理？CI 过宽是否影响可操作性？\n- 经验验证（23 LLM 配置, 161 scenarios）：覆盖范围是否充分？缺少商业 LLM（GPT-4/Claude）和 >235B 模型是否构成重大局限？\n- 校正方法比较（Table 4, K=3/5/10）：实验设计是否公平？PPI++ 在 K=10 退化的解释是否充分？\n- Cross-K robustness (K=3,5,7,10)：是否充分验证了结论的 K 无关性？\n\n### 5. 数值一致性\n- Abstract/Introduction 中的数字是否与 Experiments section 一致？\n- Table 1 的数字是否与正文描述一致？\n- Correction method ranking 在不同 section 的引用是否一致？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n（2-3句概述论文）\n\n## Strengths\nS1. ...\nS2. ...\n...\n\n## Weaknesses\nW1. [severity: must-fix/should-fix/minor] ...\nW2. ...\n...\n\n## Questions\nQ1. ...\nQ2. ...\n...\n\n## Missing References\nMR1. ...\n...\n\n## Minor Issues\nMI1. ...\n...\n\n## Overall Assessment\nScore: X.X\nConfidence: high/medium/low\n一句话总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 1037 · 2026-05-23T09:22:42.031806+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29676
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-23T09:22:42.182871+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性、完整性和表达质量**。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 投稿类别：Long Paper\n- 截止日期：2026-05-25\n- 正文限制：8 页（参考文献、Limitations、Ethical Considerations 不计入）\n- 模板：ACL（`\\usepackage[review]{acl}`）\n- 匿名规则：Double-blind\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 主文件：`docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf`（30页，含附录）\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **贡献 1（Multi-class bias taxonomy）**：相比 Brenner (1993), Dosemeci (1990), Veirod & Laake (2001), Teblunthuis (2024), Lee et al. (2024)——真正的增量贡献是什么？\"first unified analysis across seven topologies\" 是否有事实支撑？\n- **贡献 2（ASV framework）**：与 E-values (VanderWeele & Ding, 2017)、robustness values (Cinelli & Hazlett, 2020) 的方法论区别是什么？sign-flip ASV 和 N* 是否确实在 E-value 中无对应物？magnitude ASV 是否与 E-value 高度同构？Section 3.3 的 ASV-vs-E-value 对比是否充分？\n- **贡献 3（Correction guidance + FWL invariance）**：FWL invariance 作为负面结果是否有足够的 novelty？topology-aware correction guidance 是否超越了简单的方法排名？\n\n### 2. 相关工作完整性\n- 测量误差文献（Carroll et al., 2006; Gustafson, 2004）是否充分覆盖？\n- NLP+因果推断文献（Feder et al., 2022; Keith et al., 2020; Wood-Doughty, 2018）是否充分覆盖？\n- 敏感性分析文献（Rosenbaum, 2002; Ding & VanderWeele, 2016）是否充分覆盖？\n- 是否遗漏了重要的 mediation analysis 文献（如 VanderWeele, 2015）或非线性测量误差文献（如 Schennach, 2020）？\n- PPI++ 及其后续（Zrnic & Candes, 2024; Demirel et al., 2024; Cadei et al., 2025）是否充分讨论？\n\n### 3. 写作质量和可达性\n- **Abstract**：信息密度是否过高？定量信息点数量是否合理？是否应聚焦 2-3 个核心数字？\n- **Introduction**：叙事结构是否清晰？三个贡献是否准确反映论文内容？\n- **Method (Section 3)**：对 EMNLP 受众——计量经济学术语（plim, FWL, probability limit）是否有充分解释？是否有 notation roadmap？\n- **Experiments (Section 4)**：结果呈现是否逻辑流畅？Table 和 Figure 是否有效支撑 claim？\n- **Conclusion**：是否过度声称或遗漏重要限制？\n- **Limitations**：是否覆盖了关键限制（non-differential、线性 SEM、LLM 覆盖范围）？\n- **整体节奏**：8 页限制下是否有内容取舍失当？广度 vs 深度的平衡？\n\n### 4. 格式合规性\n- 正文是否在 8 页内？Section 5 (Conclusion) 是否完全在 page 8 内？\n- 匿名规则是否遵守？（作者署名、致谢、代码链接）\n- 引用格式是否符合 ACL/natbib 规范？\n- Appendix 是否合理使用（关键证明 vs 补充实验）？\n- Figure/Table 编号和引用是否一致？\n\n### 5. 论文的整体叙事\n- 论文的 \"story\" 是否连贯？从问题动机 → 理论分析 → 实验验证 → correction guidance 的逻辑链是否通顺？\n- 论文是否在 claim 与 evidence 之间保持了适当的对应？\n- 对 EMNLP 目标受众（NLP 研究者，可能不熟悉因果推断技术细节）的可及性如何？\n- 论文是否适合 EMNLP（而非统计/计量经济学会议）？NLP 社区的 takeaway 是什么？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n（2-3句概述论文）\n\n## Strengths\nS1. ...\nS2. ...\n...\n\n## Weaknesses\nW1. [severity: must-fix/should-fix/minor] ...\nW2. ...\n...\n\n## Questions\nQ1. ...\nQ2. ...\n...\n\n## Missing References\nMR1. ...\n...\n\n## Minor Issues\nMI1. ...\n...\n\n## Overall Assessment\nScore: X.X\nConfidence: high/medium/low\n一句话总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性、完整性和表达质量**。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 投稿类别：Long Paper\n- 截止日期：2026-05-25\n- 正文限制：8 页（参考文献、Limitations、Ethical Considerations 不计入）\n- 模板：ACL（`\\usepackage[review]{acl}`）\n- 匿名规则：Double-blind\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 主文件：`docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_13/submitted.pdf`（30页，含附录）\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **贡献 1（Multi-class bias taxonomy）**：相比 Brenner (1993), Dosemeci (1990), Veirod & Laake (2001), Teblunthuis (2024), Lee et al. (2024)——真正的增量贡献是什么？\"first unified analysis across seven topologies\" 是否有事实支撑？\n- **贡献 2（ASV framework）**：与 E-values (VanderWeele & Ding, 2017)、robustness values (Cinelli & Hazlett, 2020) 的方法论区别是什么？sign-flip ASV 和 N* 是否确实在 E-value 中无对应物？magnitude ASV 是否与 E-value 高度同构？Section 3.3 的 ASV-vs-E-value 对比是否充分？\n- **贡献 3（Correction guidance + FWL invariance）**：FWL invariance 作为负面结果是否有足够的 novelty？topology-aware correction guidance 是否超越了简单的方法排名？\n\n### 2. 相关工作完整性\n- 测量误差文献（Carroll et al., 2006; Gustafson, 2004）是否充分覆盖？\n- NLP+因果推断文献（Feder et al., 2022; Keith et al., 2020; Wood-Doughty, 2018）是否充分覆盖？\n- 敏感性分析文献（Rosenbaum, 2002; Ding & VanderWeele, 2016）是否充分覆盖？\n- 是否遗漏了重要的 mediation analysis 文献（如 VanderWeele, 2015）或非线性测量误差文献（如 Schennach, 2020）？\n- PPI++ 及其后续（Zrnic & Candes, 2024; Demirel et al., 2024; Cadei et al., 2025）是否充分讨论？\n\n### 3. 写作质量和可达性\n- **Abstract**：信息密度是否过高？定量信息点数量是否合理？是否应聚焦 2-3 个核心数字？\n- **Introduction**：叙事结构是否清晰？三个贡献是否准确反映论文内容？\n- **Method (Section 3)**：对 EMNLP 受众——计量经济学术语（plim, FWL, probability limit）是否有充分解释？是否有 notation roadmap？\n- **Experiments (Section 4)**：结果呈现是否逻辑流畅？Table 和 Figure 是否有效支撑 claim？\n- **Conclusion**：是否过度声称或遗漏重要限制？\n- **Limitations**：是否覆盖了关键限制（non-differential、线性 SEM、LLM 覆盖范围）？\n- **整体节奏**：8 页限制下是否有内容取舍失当？广度 vs 深度的平衡？\n\n### 4. 格式合规性\n- 正文是否在 8 页内？Section 5 (Conclusion) 是否完全在 page 8 内？\n- 匿名规则是否遵守？（作者署名、致谢、代码链接）\n- 引用格式是否符合 ACL/natbib 规范？\n- Appendix 是否合理使用（关键证明 vs 补充实验）？\n- Figure/Table 编号和引用是否一致？\n\n### 5. 论文的整体叙事\n- 论文的 \"story\" 是否连贯？从问题动机 → 理论分析 → 实验验证 → correction guidance 的逻辑链是否通顺？\n- 论文是否在 claim 与 evidence 之间保持了适当的对应？\n- 对 EMNLP 目标受众（NLP 研究者，可能不熟悉因果推断技术细节）的可及性如何？\n- 论文是否适合 EMNLP（而非统计/计量经济学会议）？NLP 社区的 takeaway 是什么？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n（2-3句概述论文）\n\n## Strengths\nS1. ...\nS2. ...\n...\n\n## Weaknesses\nW1. [severity: must-fix/should-fix/minor] ...\nW2. ...\n...\n\n## Questions\nQ1. ...\nQ2. ...\n...\n\n## Missing References\nMR1. ...\n...\n\n## Minor Issues\nMI1. ...\n...\n\n## Overall Assessment\nScore: X.X\nConfidence: high/medium/low\n一句话总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 1039 · 2026-05-23T09:22:43.691480+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1508
}
```

</details>

---


### Assistant

_source line 1040 · 2026-05-23T09:22:58.884070+00:00_

**Round 1 已启动。** 当前状态：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验验证） | ⏳ 审稿中 |
| Reviewer 2（新颖性 + 完整性 + 表达） | ⏳ 审稿中 |
| 视觉审查 Agent | ⏳ 已启动 |
| 外部审稿（Stanford Agentic Reviewer） | ❌ 未启用 |

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 1041 · 2026-05-23T09:29:33.540883+00:00_

[Reviewer 2 审稿意见]:
## Summary

本文分析了 LLM 多类标注误差如何在七种经典因果 DAG 拓扑下传播到因果效应估计中。在线性 SEM 和 K 类非差异误分类假设下，推导了各拓扑的闭合形式偏差表达式，提出了 Annotation Sensitivity Values (ASVs) 作为拓扑依赖的敏感性分析框架，并评估了五种校正方法。核心发现包括：K≥3 误分类可导致因果效应符号反转（二分类不会出现）；拓扑呈现从 IV（最脆弱）到 M-bias（最稳健）的脆弱性谱；FWL 不变性使矩阵校正方法对四种协变量拓扑无效。

## Strengths

**S1. 七种 DAG 拓扑的统一分析框架具有真正的新颖性。** 先前工作（Brenner 1993 处理多类混杂；Lee & Wood-Doughty 2024 处理 LLM 分类器但仅覆盖 confounding）均针对单一拓扑。本文的统一分析揭示了跨拓扑模式（符号保持层级、ASV 谱），这在单拓扑研究中不可见。"first unified analysis across seven topologies" 的声称有事实支撑。

**S2. K≥3 符号反转发现具有理论重要性和实践相关性。** 论文通过 Proposition 1、Figure 2、Table 1 清晰展示了多类误分类与二类误分类的本质差异：K=2 时非差异误分类必然向零衰减（Brenner 1993），而 K≥3 时 off-diagonal 权重可导致符号反转。对于使用多类 LLM 分类器（如 3+ 类情感/立场分类）的 NLP 因果推断实践者，这是一个直接相关的警告。

**S3. 实验验证扎实且透明。** 理论预测与 Monte Carlo 模拟高度吻合（100,000 矩阵，161 场景，MAPE 1.6%——Section 4.2）。使用三个 NLP 任务（HumAID、VAST、CivilComments）的真实 LLM 混淆矩阵进行经验验证（Section 4.4），且所有结构模式得到确认。

**S4. 实用性强。** Algorithm 1 和 Table 4 的校正方法排名按拓扑给出可操作指导。ClinicalBERT 案例研究（Appendix B.3）展示了从拓扑识别→ASV 诊断→校正方法选择的完整工作流。

**S5. 附录极为详尽。** 22 页附录包含完整证明、10+ 项鲁棒性检验（非线性 DGP B.7、差异误分类 B.6、逻辑回归 FWL B.14、Bootstrap CI B.8 等），展现了高度的学术严谨性。

## Weaknesses

**W1. [must-fix] EMNLP 受众的可达性障碍严重。**

论文大量使用计量经济学/流行病学术语而缺乏面向 NLP 读者的解释：
- "plim"（概率极限）从 Section 3.2 起贯穿全文，但仅在 page 4 脚注中以一句话解释（"The probability limit (plim) is the value to which an estimator converges as sample size N → ∞"），且未解释其与普通期望值的区别。
- FWL 定理是贡献 3 的核心（Section 4.5 标题即为 "FWL invariance"），但分解过程全部放在 Appendix A.2。正文中首次出现 "Frisch-Waugh-Lovell" 时（page 5, Section 3.2 Collider 段落）没有任何直觉解释。
- Equation (1) 的 $\tilde{Z}$ 和残差化概念对不熟悉 OLS 投影的读者不透明。
- 缺少 notation roadmap——Table 18（page 30 Notation 表）应该前置到 Section 3 开头或至少引用它。

**建议**：在 Section 3.1 开头加 1-2 段直觉性文字解释 plim、FWL 分解、残差化的含义；将 Table 18 移到正文或在 Section 3.1 加简化版。

**W2. [must-fix] Conjecture 1（包络单调性）未被证明，削弱了核心理论贡献。**

论文最显著的 claim 之一是拓扑形成从 IV → exposure → front-door → M-bias → confounding → mediation → collider 的严格脆弱性层级。但这在 K≥3 情况下标记为 "Conjecture"（page 6），仅有数值验证（Appendix B.12：210,000 total 配置，ε < 0.06）。对于一篇以理论分析为核心贡献的论文，中心排序结果停留在猜想阶段是显著弱点。

具体问题：
- K=2 的证明（Theorem 1）使用 perspective function 的凸性——论文未解释为何此方法不能推广到 K≥3。
- Appendix B.12 Table 10 显示 worst-case 违反为 "largest single-step deviation"，但未报告这些偏差的统计显著性。
- "ε-approximate monotonicity" 的定义（ε < 0.06）是否足够？对于 ASV 值本身较小的拓扑对（如 confounding vs. mediation），0.06 的偏差可能相对显著。

**建议**：要么证明 K≥3 情况（至少对 K=3），要么明确降低 claim 强度——例如将 "vulnerability spectrum" 从 strong ordering 降级为 "approximate ranking supported by extensive numerical evidence"。

**W3. [should-fix] ASV 与 E-value 的比较不够充分。**

Section 3.3 用约半栏篇幅对比 ASV 和 E-values，但未达到可以让读者判断 ASV 独立贡献的深度：
- Magnitude ASV 和 E-value 在结构上高度相似：两者都提供"结论翻转所需的最小扰动阈值"。论文声称 "ASV parameterizes a K×K confusion matrix error along a topology-specific path"（page 5），但未形式化展示这与 E-value 参数化的数学差异。
- Sign-flip ASV 被声称 "has no E-value counterpart"（page 6），但未解释为什么 E-value 框架不能被扩展来处理符号反转——仅仅是因为 E-value 文献没有讨论这个问题，还是因为存在结构性障碍？
- 与 Cinelli & Hazlett (2020) 的 partial R² 框架完全没有形式化对比，仅在 Related Work 中提及 "the robustness value of Cinelli and Hazlett (2020)"。

**建议**：添加一个表格或并列展示，形式化对比 ASV、E-value、robustness value 在参数空间、敏感性路径、适用场景上的异同。

**W4. [should-fix] Abstract 信息密度过高。**

Abstract 包含至少 7 个独立数字（seven topologies, K-class, K≥3, 14×, 83.4%, 52.6%, 2.1%, 1.6% MAPE）。对于可能不熟悉因果推断技术细节的 EMNLP 读者，这造成认知超载。核心信息（"LLM 多类标注误差在因果推断中的传播取决于 DAG 拓扑，且 K≥3 时可导致符号反转"）被数字淹没。

**建议**：聚焦 2-3 个最核心的定量发现（如 K≥3 sign reversal + topology-dependent vulnerability range），将其余数字移至 Introduction。

**W5. [should-fix] 七种拓扑中部分对 NLP 的实践相关性不足，缺乏动机说明。**

论文覆盖七种 DAG 拓扑，但未充分论证每种拓扑在 NLP 因果推断中何时出现：
- **M-bias**：论文未给出任何 NLP 场景实例。M-bias 结构要求两个未测量变量分别影响处理和结果——这在文本分析中何时成立？
- **Front-door criterion**：需要完整中介路径且无直接效应——NLP 因果推断中有哪些应用？
- **IV topology**：有效工具变量在 NLP 中极难找到（论文自己在 Appendix B.4 也称 IV 为 "the most fragile topology"）。

Section 4.4 经验验证仅使用 confounding 和 exposure 拓扑。如果其余五种拓扑缺少 NLP 用例，那么 "seven topologies" 的覆盖更多是理论完整性而非实践需求驱动。

**建议**：在 Introduction 或 Section 3 开头为每种拓扑给出至少一个简短的 NLP 因果推断应用场景，或者明确哪些拓扑主要是为理论完整性而包含。

**W6. [should-fix] FWL 不变性作为"贡献"的定位过高。**

FWL 不变性（Section 4.5, Appendix B.14）本质上是一个负面结果：矩阵校正对协变量拓扑无效，因为 FWL 投影消除了被校正的变量。这是一个有用的观察，但：
- 对四种（confounding, mediation, collider, M-bias）拓扑，校正指导实质上是"用 PPI++ 或不校正"——这更像工程建议而非方法论贡献。
- 论文未提出任何新的校正方法，仅评估了现有方法。
- Algorithm 1 是一个基于拓扑分类的决策树，而非方法论创新。

Introduction 将此列为三大贡献之一（"We evaluate five correction methods and prove a Frisch-Waugh-Lovell invariance result"），但 FWL 不变性本身是 FWL 定理的直接推论——标注变量作为协变量时的投影消除是意料之中的。

**W7. [minor] 非差异误分类假设可能被 LLM 系统性违反。**

Definition 1 假设 LLM 误差在给定真实标签后独立于结果和处理。但 LLM 误差已知与文本复杂度、领域、内容特征相关，这些可能同时与结果相关。Appendix B.6 的压力测试仅考虑温和扰动（ε 到 0.50），且结论是"主要发现在温和条件下成立但应谨慎使用"。正文 Limitations 中的讨论较为简短（~3 行），考虑到这是论文的核心假设，应在正文中更充分讨论。

**W8. [minor] 缺少 DAG 拓扑未知时的讨论。**

论文整个框架假设分析者知道因果 DAG 结构。但在 NLP 因果推断实践中，DAG 规范通常不确定。Algorithm 1 的第一步就是"确定 DAG 拓扑"，但没有讨论拓扑误判的后果或如何处理 DAG 不确定性。

## Questions

**Q1.** Conjecture 1 的证明障碍：K=2 证明使用 perspective function 凸性（Appendix A.4），为何此方法不能推广到 K≥3？是维度诅咒、非凸性、还是组合爆炸？如果能明确障碍所在，这将帮助读者评估猜想被证明的可能性。

**Q2.** 对于二元结果（NLP 中常见：情感、立场、毒性分类），逻辑回归下的结果是否会质性改变？Appendix B.14 显示偏差减少百分比"negligible"，但未验证符号保持条件（Propositions 1-7）在非线性模型下是否成立。Table 13 仅报告偏差方向一致性，未报告符号翻转率。

**Q3.** Sign-flip ASV 对 M-bias 为 ∞（page 7）——这是否意味着 M-bias 在 *任何* 误分类程度下都不会发生符号反转？如果是，这似乎是一个可以证明的定理而非仅靠数值验证。

**Q4.** Table 4（Section 4.5）RMSE 比较：PPI++ 在 confounding 下达到 85.3% 降低，但在 M-bias 下为负值（-88.0）。这个负值意味着什么？PPI++ 在 M-bias 下反而增大误差？如果是，这是否意味着 PPI++ 在某些拓扑下不安全？论文未讨论这一点。

**Q5.** 论文在 Section 4.4 经验验证中提到 "classification accuracy is not a reliable proxy for causal estimation quality (Spearman ρ = −0.10, p = 0.45)"——这是基于 56 个 HumAID 场景的相关性。但 56 个观测的 power 可能不足以检测中等相关性。这个 null result 的 power analysis 是什么？

## Missing References

**MR1.** Veitch, Wang & Blei (2020), "Adapting Text Embeddings for Causal Inference" — 直接相关的 NLP+因果推断工作，提出基于文本嵌入的因果效应估计，面临类似的标注质量问题。

**MR2.** Imai, Keele & Tingley (2010), "A General Approach to Causal Mediation Analysis" — 论文详细讨论 mediation 拓扑但未引用因果中介分析的基础框架。

**MR3.** Roberts, Stewart & Tingley (2020) 或 Pryzant et al. (2021) 关于基于文本的因果推断——Related Work 的 NLP+因果推断覆盖可进一步加强。

**MR4.** 论文引用 Cinelli & Hazlett (2020) 但未形式化对比其 partial R² sensitivity 框架与 ASV 的关系——这是加强 ASV 新颖性论证的关键缺失。

## Minor Issues

**MI1.** Table 1 列标题过于缩略（"Amplif."、"Sign Flip"），建议使用完整词或添加表注。

**MI2.** Figure 3 y 轴标签 "Downstream causal bias" 不够精确——是绝对偏差还是相对偏差？具体偏差度量未说明。

**MI3.** 论文在 "annotation error" 和 "misclassification" 之间交替使用，未明确建立同义关系。建议在首次使用时声明。

**MI4.** Footnote 2（page 4，关于 Brenner 1993 一致性）的内容对理解贡献增量至关重要，建议提升到正文。

**MI5.** Section 3.1 标题为 "Setup and Notation"，但缺少 notation summary——Table 18（page 30）应前置或在 Section 3.1 中引用。

**MI6.** Page 8 结尾 "Code and data will be released" 满足匿名要求，但建议添加 anonymous repository link（如已有的话）以提高 reproducibility 评分。

## Overall Assessment

**Score: 3.5** (Borderline Conference)

**Confidence: 4** (Quite sure; checked important points carefully, familiar with both measurement error and NLP+causal inference literature)

**官方维度打分（ACL ARR Review Form）：**

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claims 有充分支撑（bias 表达式+Monte Carlo 验证），但核心排序结果（Conjecture 1）未被证明，非差异假设的鲁棒性验证有限 |
| Excitement | 3.0/5 | K≥3 符号反转和拓扑脆弱性谱对 NLP+因果推断领域有价值，但高度计量经济学理论内容可能限制 EMNLP 社区共鸣 |
| Reproducibility | 4.0/5 | Monte Carlo 参数完整指定，真实 LLM 混淆矩阵可复现，代码承诺释放但尚未提供 |
| Overall | 3.5/5 | 理论贡献扎实，统一框架确有新颖性，但 EMNLP 可达性障碍和未证明的核心猜想是显著顾虑 |

**一句话总评**：论文在测量误差×因果推断的交叉领域做出了系统性的理论贡献（七拓扑统一分析、K≥3 符号反转、ASV 框架），实验验证扎实，但核心排序结果停留在猜想阶段、面向 EMNLP 受众的可达性不足、以及部分拓扑对 NLP 的实践相关性缺乏动机，使其处于主会议接收的边界。建议加强可达性、证明或降级 Conjecture 1、深化 ASV-vs-E-value 对比后重新提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1042 · 2026-05-23T09:29:44.072490+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1043 · 2026-05-23T09:29:48.797155+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结果摘要**：

- **Overall: 3.5**（Borderline Conference）
- **Soundness: 3.5** / **Excitement: 3.0** / **Reproducibility: 4.0**

**核心判断**：论文在测量误差×因果推断交叉领域做出了系统性理论贡献（七拓扑统一分析、K≥3 符号反转），实验验证扎实。但存在三个主要问题：

1. **Must-fix**：EMNLP 受众可达性障碍（plim/FWL 等计量经济学术语缺乏解释）
2. **Must-fix**：Conjecture 1（包络单调性）作为核心理论 claim 未被证明
3. **Should-fix**：ASV vs E-value 对比不充分、Abstract 信息过载、部分拓扑缺少 NLP 应用动机、FWL 不变性贡献定位过高

共提出 8 个 Weaknesses、5 个 Questions、4 个 Missing References、6 个 Minor Issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1044 · 2026-05-23T09:29:56.918007+00:00_

Reviewer 2 审稿完成（3.5 Borderline Conference）。等待 Reviewer 1 完成独立初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 101

## Round 101

6 recorded events


### User

_source line 1045 · 2026-05-23T09:33:16.702081+00:00_

[Reviewer 1 审稿意见]:
## Summary

本文系统分析了 K 类标注错误（如 LLM 分类器产生的错误）在线性 SEM 下如何沿七种典型 DAG 拓扑传播至因果估计。主要贡献包括：(1) 七种拓扑的闭式偏差表达式；(2) K=2 的单调性证明（Theorem 1）和一般 K 的符号保持命题（Propositions 1-6）；(3) Annotation Sensitivity Values (ASV) 敏感性分析框架；(4) 五种校正方法的拓扑感知比较和实践指导（Algorithm 1）。经验验证覆盖 23 个 LLM 配置和 161 个场景。

## Strengths

**S1. 系统性和全面性。** 首次对七种典型 DAG 拓扑进行 K 类错分类的统一分析，填补了以往文献只覆盖单一拓扑或二元错分类的空白。拓扑分类体系（Figure 1）清晰有用。

**S2. 诚实的理论层级体系。** 将理论贡献明确区分为"解析证明"（Propositions 1-6，适用于一般 K）、"数值验证"（Observation 1，20,000 triples per topology）和"ε-近似猜想"（Conjecture 1），避免了过度宣称。

**S3. FWL 不变性的实践洞见。** 证明在线性 OLS 下，四种协变量拓扑的矩阵校正方法本质上无效（Appendix B.2, B.14），因为 FWL 定理保证了 dummy 变量的列空间变换不改变处理效应估计。这一结论在 logistic 回归下也近似成立（偏差缩减可忽略，~0.003，Table 13）。为实践者提供了"不要在这些拓扑上浪费时间做 naive 校正"的清晰指导。

**S4. 实证验证规模充分。** Monte Carlo 验证覆盖 100,000 Dirichlet 矩阵 × 7 拓扑，MAPE 1.6%（Section 4.1）。经验验证使用 23 个真实 LLM 混淆矩阵、3 个 NLP 数据集、161 个场景（Section 4.4）。跨 K 稳健性检验覆盖 K=3,5,7,10。

**S5. 实践价值高。** Algorithm 1 提供了拓扑感知的校正方法选择指南，ASV 框架可量化标注敏感性。Fig 3 证明分类精度（F1）与因果偏差无显著相关（ρ = -0.10, p = 0.45），强有力地支持了"拓扑决定偏差"的核心论点。

**S6. Exposure 拓扑的 sign reversal 发现。** 明确识别出 K≥3 引入的结构性符号反转可能性（Proposition 7 提供了构造性反例），这是二元情形中不存在的现象。Eq.2 的权重 w_{jk} 机制解释清晰。

## Weaknesses

**W1. [should-fix] Theorem 1（单调性）限于 K=2，与论文多类别框架的关系需更清晰阐述。**
- Theorem 1（Section 3.3, p5）证明了 confounding 和 mediation 的 envelope monotonicity，但仅限 K=2 且需 proportional effects（f=λg）和 (C₀)_{jj} ≥ 1/2 两个条件。
- K≥3 的单调性依赖 Observation 1（20,000 triples per topology 的数值验证）和 Conjecture 1（ε < 0.06 的近似单调性猜想）。
- 问题不在于这个事实本身（论文已诚实披露），而在于 Abstract 和 Introduction 中对该限制的呈现不够突出。读者可能在深入 Section 3.3 之前误以为所有理论结果都适用于一般 K。
- **建议**：在 Abstract 中明确提及 Theorem 1 的 K=2 条件，例如将 "show that K≥3 introduces..." 之前加一句关于 K=2 formal guarantees 和 K≥3 numerical evidence 的区分。

**W2. [should-fix] Proportional effects 假设的失败率不可忽视。**
- Theorem 1 和 Proposition 2 需要 f=λg（处理对 T 和 Y 的效应成比例）。
- Appendix B.17（Table 16）报告在 23 个真实 LLM 混淆矩阵下，proportional effects 在 15-17% 的案例中被违反（"Sparse DGP (zero-effect categories) produces the highest violation rate (24.2%)"）。
- 当 f≠λg 时，论文退回到 Proposition 3（一般情形），但该命题要求 |τ| > B（worst-case bias bound），条件更难在实践中验证。
- **问题**：15-17% 的失败率是否集中在特定模型类型或 K 值？失败时偏差的实际幅度有多大？
- **建议**：在正文中更直接地讨论这一失败率的实践含义，而非仅在 Appendix B.17 中报告。

**W3. [should-fix] Section 4.2 中 IV 拓扑 sign reversal 的表述存在内部不一致。**
- Section 4.2（p7）写道："diagonal dominance C₀ ≥ 0.8 reduces but does not eliminate sign reversal risk"——暗示即使在高精度下，IV 的符号反转风险仍然存在。
- 然而 Appendix B.4（p23）写道："IV maintains 100% violation with pure amplification. IV sign reversal is entirely driven by pathological (near-random) confusion matrices where the Wald denominator crosses zero; diagonal dominance prevents this crossing."——明确说 diagonal dominance 消除了符号反转。
- Abstract 则说 "no sign reversal occurs for all other topologies including IV"——与 Appendix B.4 一致但与 Section 4.2 矛盾。
- 数值事实本身是一致的（真实 LLM 矩阵的 138 个非 exposure 场景中 0 次符号反转），但 Section 4.2 的措辞会误导读者。
- **建议**：修改 Section 4.2 的表述，明确区分"violation（偏差存在）"和"sign reversal（符号反转）"，使之与 Appendix B.4 和 Abstract 一致。

**W4. [should-fix] 线性 SEM 限制对 EMNLP 受众的适用性。**
- 所有闭式偏差表达式在线性 SEM 下推导。NLP 实践中的因果推断常涉及非线性模型（logistic regression, neural networks）。
- Appendix B.7 的 logistic DGP 验证显示 sign-flip patterns "virtually identical"，但 Appendix B.14 的 FWL invariance under logistic regression 显示 exposure 拓扑的偏差缩减达 ~22% 到 ~78%（Table 13），远非 "negligible"。
- 这意味着在 logistic 回归下，线性 SEM 的"矩阵校正无效"结论不再成立（至少对 exposure 不成立），但正文（Section 4.5）似乎将 FWL invariance 泛化到了 logistic 情形（"FWL invariance holds under linear OLS and approximately under logistic regression"）。
- **建议**：在正文中更精确地限定 FWL invariance 的适用范围，特别是 exposure 拓扑在 logistic 回归下的行为差异。

**W5. [should-fix] 经验验证缺少商业 LLM。**
- 仅使用 4 个开源模型族（Llama-4-Maverick, Qwen2.5-25B, DeepSeek-Chat, Qwen2.5-7B-Instruct），均 ≤25B 参数。
- 缺少 GPT-4, Claude, Gemini 等在标注流水线中广泛使用的商业模型。
- Limitations（p9）提及 "commercial models and ordinal tasks remain untested"，但未解释为什么未包含。
- 商业 LLM 的错误分布可能与开源模型显著不同（如 API-based models 常有不同的 calibration 特性），影响论文结论的普适性。

**W6. [minor] Conjecture 1 的数值验证在高维度下覆盖不足。**
- 对 K=7 的混淆矩阵（42 个自由参数），每拓扑仅 10,000 个样本（Appendix B.12）在高维空间中极度稀疏。
- ε < 0.06 的界对实践者的含义不够清晰——6% 的单调性偏差在什么场景下有实际影响？
- **建议**：讨论 ε 界的实践含义，或提供更多 K=10 的验证结果。

## Questions

**Q1.** Proportional effects 失败率（15-17%）是否与特定模型类型或 K 值相关？Appendix B.17 Table 16 的分层统计是否可以进一步拆解？失败时的偏差实际幅度是什么量级？

**Q2.** Section 4.2 中 IV sign reversal 的表述（"does not eliminate sign reversal risk"）与 Appendix B.4（"diagonal dominance prevents this crossing"）和 Abstract（"no sign reversal for IV"）三处不一致——请确认哪个说法是正确的，并统一措辞。

**Q3.** 对于 exposure 拓扑在 logistic DGP 下的行为：Appendix B.14 Table 13 显示 exposure 在 logistic 回归下有 ~22% 到 ~78% 的偏差缩减，这是否意味着 FWL invariance 对 exposure 拓扑在非线性情形下不成立？如果是，Algorithm 1 中对 exposure 的推荐（MLA）在 logistic 回归下是否仍有效？

**Q4.** ASV 框架的 δ* 阈值（Algorithm 1 使用 10% bias threshold）——该选择的敏感性如何？不同阈值是否会改变拓扑排序？

**Q5.** 为什么未包含商业 LLM 的混淆矩阵？这是 double-blind 限制还是数据可获得性问题？

## Missing References

未发现显著遗漏。论文的文献覆盖在测量误差理论（Carroll et al., 2006; Brenner, 1993）、LLM 标注（Gilardi et al., 2023; Ziems et al., 2024; Baumann et al., 2025）、PPI（Angelopoulos et al., 2023; Zrnic and Candès, 2024）和敏感性分析（VanderWeele and Ding, 2017; Cinelli and Hazlett, 2020）方面均较为充分。

## Minor Issues

**MI1.** Footnote 1（p1）提到 "varying 15×+ across topologies"，但该数字的计算基准不够清晰（是什么对什么的比率？应明确说明）。

**MI2.** Table 1（p7）的 "τ_adj=0%" 列含义需在 caption 中更明确解释——当前 caption 未解释各列含义。

**MI3.** Notation Table（Table 18, p30）非常有用但放置太晚。建议在主文第一次引入大量符号时交叉引用该表。

**MI4.** Section 4.2 将"Numerical Verification 1"和"Numerical Verification 2"作为行内引用，但这两个术语未在任何地方正式定义。建议使用更标准的引用方式或在首次使用时给出定义。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2 证明严谨，一般 K 的 sign preservation 命题覆盖充分。但 proportional effects 的 15-17% 失败率削弱了 Theorem 1 的实用性，IV sign reversal 表述存在内部不一致。整体而言，main claims 有充分支撑但需修正细节。 |
| Excitement | 3.5/5 | 选题具时效性（LLM 标注 × 因果推断），拓扑分类体系和 ASV 框架有实践价值。但核心技术贡献（K 类错分类的偏差表达式）是经典测量误差理论的延伸，创新性有限。FWL invariance 洞见是一个亮点。 |
| Reproducibility | 4/5 | Monte Carlo 参数明确（N=10,000, 100,000 Dirichlet），LLM 配置和数据集有具体名称，承诺释放代码和数据。但部分实验细节需从附录 20 页材料中提取。 |
| Confidence | 4/5 | 我仔细检查了理论证明的条件和结构、数值一致性、实验设计。对测量误差理论和因果推断有一定背景。可能遗漏了部分附录中的细节。 |

## Overall Assessment

**Score: 3.5 (Borderline Conference)**

**一句话总评：** 本文对 LLM 标注错误在因果推断中的传播进行了系统且深入的分析，理论框架（特别是 FWL invariance 和 sign preservation）和实践工具（ASV, Algorithm 1）有实质贡献，但 Theorem 1 的 K=2 限制、proportional effects 假设的非平凡失败率、IV 表述的内部不一致、以及线性 SEM 对 NLP 场景的局限性，使其处于主会议接收的边界线上。如果能在修订中（1）统一 IV sign reversal 表述，（2）更突出地讨论 proportional effects 的实践含义，（3）补充至少 1-2 个商业 LLM 的验证，则可上调至 Conference (4.0)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-23T09:34:19.594880+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条审阅 Reviewer 1 的意见，对每个 Weakness、Question 使用 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供证据，cite 具体 Section/Table/Figure）回应。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## Summary\n\n本文系统分析了 K 类标注错误（如 LLM 分类器产生的错误）在线性 SEM 下如何沿七种典型 DAG 拓扑传播至因果估计。主要贡献包括：(1) 七种拓扑的闭式偏差表达式；(2) K=2 的单调性证明（Theorem 1）和一般 K 的符号保持命题（Propositions 1-6）；(3) Annotation Sensitivity Values (ASV) 敏感性分析框架；(4) 五种校正方法的拓扑感知比较和实践指导（Algorithm 1）。经验验证覆盖 23 个 LLM 配置和 161 个场景。\n\n## Strengths\n\nS1. 系统性和全面性。首次对七种典型 DAG 拓扑进行 K 类错分类的统一分析，填补了以往文献只覆盖单一拓扑或二元错分类的空白。拓扑分类体系（Figure 1）清晰有用。\n\nS2. 诚实的理论层级体系。将理论贡献明确区分为\"解析证明\"（Propositions 1-6，适用于一般 K）、\"数值验证\"（Observation 1，20,000 triples per topology）和\"ε-近似猜想\"（Conjecture 1），避免了过度宣称。\n\nS3. FWL 不变性的实践洞见。证明在线性 OLS 下，四种协变量拓扑的矩阵校正方法本质上无效（Appendix B.2, B.14），因为 FWL 定理保证了 dummy 变量的列空间变换不改变处理效应估计。这一结论在 logistic 回归下也近似成立（偏差缩减可忽略，~0.003，Table 13）。\n\nS4. 实证验证规模充分。Monte Carlo 验证覆盖 100,000 Dirichlet 矩阵 × 7 拓扑，MAPE 1.6%（Section 4.1）。经验验证使用 23 个真实 LLM 混淆矩阵、3 个 NLP 数据集、161 个场景（Section 4.4）。跨 K 稳健性检验覆盖 K=3,5,7,10。\n\nS5. 实践价值高。Algorithm 1 提供了拓扑感知的校正方法选择指南，ASV 框架可量化标注敏感性。Fig 3 证明分类精度（F1）与因果偏差无显著相关（ρ = -0.10, p = 0.45），强有力地支持了\"拓扑决定偏差\"的核心论点。\n\nS6. Exposure 拓扑的 sign reversal 发现。明确识别出 K≥3 引入的结构性符号反转可能性（Proposition 7 提供了构造性反例），这是二元情形中不存在的现象。Eq.2 的权重 w_{jk} 机制解释清晰。\n\n## Weaknesses\n\nW1. [should-fix] Theorem 1（单调性）限于 K=2，与论文多类别框架的关系需更清晰阐述。\n- Theorem 1（Section 3.3, p5）证明了 confounding 和 mediation 的 envelope monotonicity，但仅限 K=2 且需 proportional effects（f=λg）和 (C₀)_{jj} ≥ 1/2 两个条件。\n- K≥3 的单调性依赖 Observation 1（20,000 triples per topology 的数值验证）和 Conjecture 1（ε < 0.06 的近似单调性猜想）。\n- 问题不在于这个事实本身（论文已诚实披露），而在于 Abstract 和 Introduction 中对该限制的呈现不够突出。\n- 建议：在 Abstract 中明确提及 Theorem 1 的 K=2 条件。\n\nW2. [should-fix] Proportional effects 假设的失败率不可忽视。\n- Theorem 1 和 Proposition 2 需要 f=λg。\n- Appendix B.17（Table 16）报告在 23 个真实 LLM 混淆矩阵下，proportional effects 在 15-17% 的案例中被违反（Sparse DGP 最高 24.2%）。\n- 当 f≠λg 时，论文退回到 Proposition 3（一般情形），但该命题要求 |τ| > B（worst-case bias bound），条件更难在实践中验证。\n- 建议：在正文中更直接地讨论这一失败率的实践含义。\n\nW3. [should-fix] Section 4.2 中 IV 拓扑 sign reversal 的表述存在内部不一致。\n- Section 4.2 写道 \"diagonal dominance C₀ ≥ 0.8 reduces but does not eliminate sign reversal risk\"\n- Appendix B.4 写道 \"diagonal dominance prevents this crossing\"\n- Abstract 说 \"no sign reversal occurs for all other topologies including IV\"\n- 建议：修改 Section 4.2 的表述，明确区分 violation 和 sign reversal。\n\nW4. [should-fix] 线性 SEM 限制对 EMNLP 受众的适用性。\n- Appendix B.14 Table 13 显示 exposure 拓扑在 logistic 回归下有 ~22% 到 ~78% 的偏差缩减，远非 \"negligible\"。\n- 正文 Section 4.5 似乎将 FWL invariance 泛化到了 logistic 情形。\n- 建议：更精确地限定 FWL invariance 的适用范围。\n\nW5. [should-fix] 经验验证缺少商业 LLM。\n- 仅使用 4 个开源模型族，均 ≤25B 参数（实际包含 Qwen3-235B）。\n- 缺少 GPT-4, Claude, Gemini 等。\n\nW6. [minor] Conjecture 1 的数值验证在高维度下覆盖不足。\n- K=7 的混淆矩阵（42 个自由参数）每拓扑仅 10,000 个样本。\n\n## Questions\n\nQ1. Proportional effects 失败率（15-17%）是否与特定模型类型或 K 值相关？失败时的偏差实际幅度是什么量级？\nQ2. Section 4.2 中 IV sign reversal 的表述与 Appendix B.4 和 Abstract 不一致——请确认哪个说法是正确的。\nQ3. Appendix B.14 Table 13 exposure 在 logistic 回归下有 ~22%-78% 偏差缩减，FWL invariance 对 exposure 在非线性情形下是否不成立？Algorithm 1 中对 exposure 的推荐在 logistic 回归下是否仍有效？\nQ4. ASV 框架的 δ* 阈值选择的敏感性如何？不同阈值是否会改变拓扑排序？\nQ5. 为什么未包含商业 LLM 的混淆矩阵？\n\n## Missing References\n未发现显著遗漏。\n\n## Minor Issues\nMI1. Footnote 1 \"varying 15×+\" 计算基准不清晰。\nMI2. Table 1 的 τ_adj=0% 列含义需更明确解释。\nMI3. Notation Table（Table 18, p30）应更早交叉引用。\nMI4. \"Numerical Verification 1/2\" 术语未正式定义。\n\n## Overall Assessment\nScore: 3.5 (Borderline Conference)\n\n---\n\n请对 Reviewer 1 的每个 Weakness (W1-W6) 和 Question (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条审阅 Reviewer 1 的意见，对每个 Weakness、Question 使用 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供证据，cite 具体 Section/Table/Figure）回应。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## Summary\n\n本文系统分析了 K 类标注错误（如 LLM 分类器产生的错误）在线性 SEM 下如何沿七种典型 DAG 拓扑传播至因果估计。主要贡献包括：(1) 七种拓扑的闭式偏差表达式；(2) K=2 的单调性证明（Theorem 1）和一般 K 的符号保持命题（Propositions 1-6）；(3) Annotation Sensitivity Values (ASV) 敏感性分析框架；(4) 五种校正方法的拓扑感知比较和实践指导（Algorithm 1）。经验验证覆盖 23 个 LLM 配置和 161 个场景。\n\n## Strengths\n\nS1. 系统性和全面性。首次对七种典型 DAG 拓扑进行 K 类错分类的统一分析，填补了以往文献只覆盖单一拓扑或二元错分类的空白。拓扑分类体系（Figure 1）清晰有用。\n\nS2. 诚实的理论层级体系。将理论贡献明确区分为\"解析证明\"（Propositions 1-6，适用于一般 K）、\"数值验证\"（Observation 1，20,000 triples per topology）和\"ε-近似猜想\"（Conjecture 1），避免了过度宣称。\n\nS3. FWL 不变性的实践洞见。证明在线性 OLS 下，四种协变量拓扑的矩阵校正方法本质上无效（Appendix B.2, B.14），因为 FWL 定理保证了 dummy 变量的列空间变换不改变处理效应估计。这一结论在 logistic 回归下也近似成立（偏差缩减可忽略，~0.003，Table 13）。\n\nS4. 实证验证规模充分。Monte Carlo 验证覆盖 100,000 Dirichlet 矩阵 × 7 拓扑，MAPE 1.6%（Section 4.1）。经验验证使用 23 个真实 LLM 混淆矩阵、3 个 NLP 数据集、161 个场景（Section 4.4）。跨 K 稳健性检验覆盖 K=3,5,7,10。\n\nS5. 实践价值高。Algorithm 1 提供了拓扑感知的校正方法选择指南，ASV 框架可量化标注敏感性。Fig 3 证明分类精度（F1）与因果偏差无显著相关（ρ = -0.10, p = 0.45），强有力地支持了\"拓扑决定偏差\"的核心论点。\n\nS6. Exposure 拓扑的 sign reversal 发现。明确识别出 K≥3 引入的结构性符号反转可能性（Proposition 7 提供了构造性反例），这是二元情形中不存在的现象。Eq.2 的权重 w_{jk} 机制解释清晰。\n\n## Weaknesses\n\nW1. [should-fix] Theorem 1（单调性）限于 K=2，与论文多类别框架的关系需更清晰阐述。\n- Theorem 1（Section 3.3, p5）证明了 confounding 和 mediation 的 envelope monotonicity，但仅限 K=2 且需 proportional effects（f=λg）和 (C₀)_{jj} ≥ 1/2 两个条件。\n- K≥3 的单调性依赖 Observation 1（20,000 triples per topology 的数值验证）和 Conjecture 1（ε < 0.06 的近似单调性猜想）。\n- 问题不在于这个事实本身（论文已诚实披露），而在于 Abstract 和 Introduction 中对该限制的呈现不够突出。\n- 建议：在 Abstract 中明确提及 Theorem 1 的 K=2 条件。\n\nW2. [should-fix] Proportional effects 假设的失败率不可忽视。\n- Theorem 1 和 Proposition 2 需要 f=λg。\n- Appendix B.17（Table 16）报告在 23 个真实 LLM 混淆矩阵下，proportional effects 在 15-17% 的案例中被违反（Sparse DGP 最高 24.2%）。\n- 当 f≠λg 时，论文退回到 Proposition 3（一般情形），但该命题要求 |τ| > B（worst-case bias bound），条件更难在实践中验证。\n- 建议：在正文中更直接地讨论这一失败率的实践含义。\n\nW3. [should-fix] Section 4.2 中 IV 拓扑 sign reversal 的表述存在内部不一致。\n- Section 4.2 写道 \"diagonal dominance C₀ ≥ 0.8 reduces but does not eliminate sign reversal risk\"\n- Appendix B.4 写道 \"diagonal dominance prevents this crossing\"\n- Abstract 说 \"no sign reversal occurs for all other topologies including IV\"\n- 建议：修改 Section 4.2 的表述，明确区分 violation 和 sign reversal。\n\nW4. [should-fix] 线性 SEM 限制对 EMNLP 受众的适用性。\n- Appendix B.14 Table 13 显示 exposure 拓扑在 logistic 回归下有 ~22% 到 ~78% 的偏差缩减，远非 \"negligible\"。\n- 正文 Section 4.5 似乎将 FWL invariance 泛化到了 logistic 情形。\n- 建议：更精确地限定 FWL invariance 的适用范围。\n\nW5. [should-fix] 经验验证缺少商业 LLM。\n- 仅使用 4 个开源模型族，均 ≤25B 参数（实际包含 Qwen3-235B）。\n- 缺少 GPT-4, Claude, Gemini 等。\n\nW6. [minor] Conjecture 1 的数值验证在高维度下覆盖不足。\n- K=7 的混淆矩阵（42 个自由参数）每拓扑仅 10,000 个样本。\n\n## Questions\n\nQ1. Proportional effects 失败率（15-17%）是否与特定模型类型或 K 值相关？失败时的偏差实际幅度是什么量级？\nQ2. Section 4.2 中 IV sign reversal 的表述与 Appendix B.4 和 Abstract 不一致——请确认哪个说法是正确的。\nQ3. Appendix B.14 Table 13 exposure 在 logistic 回归下有 ~22%-78% 偏差缩减，FWL invariance 对 exposure 在非线性情形下是否不成立？Algorithm 1 中对 exposure 的推荐在 logistic 回归下是否仍有效？\nQ4. ASV 框架的 δ* 阈值选择的敏感性如何？不同阈值是否会改变拓扑排序？\nQ5. 为什么未包含商业 LLM 的混淆矩阵？\n\n## Missing References\n未发现显著遗漏。\n\n## Minor Issues\nMI1. Footnote 1 \"varying 15×+\" 计算基准不清晰。\nMI2. Table 1 的 τ_adj=0% 列含义需更明确解释。\nMI3. Notation Table（Table 18, p30）应更早交叉引用。\nMI4. \"Numerical Verification 1/2\" 术语未正式定义。\n\n## Overall Assessment\nScore: 3.5 (Borderline Conference)\n\n---\n\n请对 Reviewer 1 的每个 Weakness (W1-W6) 和 Question (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-23T09:34:56.349122+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 36754
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-23T09:34:56.602403+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条审阅 Reviewer 2 的意见，对每个 Weakness、Question 使用 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供证据，cite 具体 Section/Table/Figure）回应。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## Summary\n\n本文分析了 LLM 多类标注误差如何在七种经典因果 DAG 拓扑下传播到因果效应估计中。在线性 SEM 和 K 类非差异误分类假设下，推导了各拓扑的闭合形式偏差表达式，提出了 ASVs 作为拓扑依赖的敏感性分析框架，并评估了五种校正方法。核心发现包括：K≥3 误分类可导致符号反转；拓扑呈现从 IV（最脆弱）到 M-bias（最稳健）的脆弱性谱；FWL 不变性使矩阵校正方法对四种协变量拓扑无效。\n\n## Strengths\n\nS1. 七种 DAG 拓扑的统一分析框架具有真正的新颖性。\nS2. K≥3 符号反转发现具有理论重要性和实践相关性。\nS3. 实验验证扎实且透明。\nS4. 实用性强（Algorithm 1, Table 4）。\nS5. 附录极为详尽（22 页，完整证明 + 10+ 鲁棒性检验）。\n\n## Weaknesses\n\nW1. [must-fix] EMNLP 受众的可达性障碍严重。\n- plim 从 Section 3.2 起贯穿全文，仅在 p4 脚注中一句话解释。\n- FWL 定理分解全部放在 Appendix A.2，正文首次出现时无直觉解释。\n- Eq.(1) 的残差化概念对不熟悉 OLS 投影的读者不透明。\n- 缺少 notation roadmap。\n- 建议：Section 3.1 开头加 1-2 段直觉性文字；将 Table 18 前置或引用。\n\nW2. [must-fix] Conjecture 1（包络单调性）未被证明，削弱了核心理论贡献。\n- 核心拓扑排序结果在 K≥3 下标记为 Conjecture。\n- K=2 证明使用 perspective function 凸性——未解释为何不能推广。\n- Appendix B.12 的违反偏差未报告统计显著性。\n- ε=0.06 对小 ASV 差值的拓扑对可能相对显著。\n- 建议：证明 K≥3 或降低 claim 强度。\n\nW3. [should-fix] ASV 与 E-value 的比较不够充分。\n- Magnitude ASV 和 E-value 结构高度相似，未形式化展示数学差异。\n- Sign-flip ASV \"has no E-value counterpart\" 未解释结构性障碍。\n- 与 Cinelli & Hazlett (2020) 的 partial R² 无形式化对比。\n- 建议：添加表格形式化对比 ASV、E-value、robustness value。\n\nW4. [should-fix] Abstract 信息密度过高。\n- 至少 7 个独立数字，造成认知超载。\n- 建议：聚焦 2-3 个核心定量发现。\n\nW5. [should-fix] 七种拓扑中部分对 NLP 的实践相关性不足。\n- M-bias、front-door、IV 未给出 NLP 场景实例。\n- Section 4.4 仅使用 confounding 和 exposure。\n- 建议：为每种拓扑给出至少一个 NLP 应用场景。\n\nW6. [should-fix] FWL 不变性作为\"贡献\"定位过高。\n- 本质是负面结果，是 FWL 定理的直接推论。\n- Algorithm 1 是决策树而非方法论创新。\n\nW7. [minor] 非差异误分类假设可能被 LLM 系统性违反。\n- Appendix B.6 stress test 仅考虑温和扰动。\n- Limitations 中讨论较简短。\n\nW8. [minor] 缺少 DAG 拓扑未知时的讨论。\n\n## Questions\n\nQ1. Conjecture 1 证明障碍——维度诅咒、非凸性、还是组合爆炸？\nQ2. 二元结果下 logistic 回归是否会质性改变符号保持条件？\nQ3. M-bias 的 Sign-flip ASV = ∞ 是否可以被证明？\nQ4. PPI++ 在 M-bias 下的负值（-88.0）意味着什么？\nQ5. 56 个 HumAID 场景的 null result (ρ=-0.10, p=0.45) 的 power analysis？\n\n## Missing References\n\nMR1. Veitch, Wang & Blei (2020) — NLP+因果推断。\nMR2. Imai, Keele & Tingley (2010) — 因果中介分析。\nMR3. Roberts, Stewart & Tingley (2020) 或 Pryzant et al. (2021) — 基于文本的因果推断。\nMR4. Cinelli & Hazlett (2020) 的形式化对比缺失。\n\n## Minor Issues\n\nMI1-MI6（略）。\n\n## Overall Assessment\nScore: 3.5 (Borderline Conference)\n\n---\n\n请对 Reviewer 2 的每个 Weakness (W1-W8) 和 Question (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条审阅 Reviewer 2 的意见，对每个 Weakness、Question 使用 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供证据，cite 具体 Section/Table/Figure）回应。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## Summary\n\n本文分析了 LLM 多类标注误差如何在七种经典因果 DAG 拓扑下传播到因果效应估计中。在线性 SEM 和 K 类非差异误分类假设下，推导了各拓扑的闭合形式偏差表达式，提出了 ASVs 作为拓扑依赖的敏感性分析框架，并评估了五种校正方法。核心发现包括：K≥3 误分类可导致符号反转；拓扑呈现从 IV（最脆弱）到 M-bias（最稳健）的脆弱性谱；FWL 不变性使矩阵校正方法对四种协变量拓扑无效。\n\n## Strengths\n\nS1. 七种 DAG 拓扑的统一分析框架具有真正的新颖性。\nS2. K≥3 符号反转发现具有理论重要性和实践相关性。\nS3. 实验验证扎实且透明。\nS4. 实用性强（Algorithm 1, Table 4）。\nS5. 附录极为详尽（22 页，完整证明 + 10+ 鲁棒性检验）。\n\n## Weaknesses\n\nW1. [must-fix] EMNLP 受众的可达性障碍严重。\n- plim 从 Section 3.2 起贯穿全文，仅在 p4 脚注中一句话解释。\n- FWL 定理分解全部放在 Appendix A.2，正文首次出现时无直觉解释。\n- Eq.(1) 的残差化概念对不熟悉 OLS 投影的读者不透明。\n- 缺少 notation roadmap。\n- 建议：Section 3.1 开头加 1-2 段直觉性文字；将 Table 18 前置或引用。\n\nW2. [must-fix] Conjecture 1（包络单调性）未被证明，削弱了核心理论贡献。\n- 核心拓扑排序结果在 K≥3 下标记为 Conjecture。\n- K=2 证明使用 perspective function 凸性——未解释为何不能推广。\n- Appendix B.12 的违反偏差未报告统计显著性。\n- ε=0.06 对小 ASV 差值的拓扑对可能相对显著。\n- 建议：证明 K≥3 或降低 claim 强度。\n\nW3. [should-fix] ASV 与 E-value 的比较不够充分。\n- Magnitude ASV 和 E-value 结构高度相似，未形式化展示数学差异。\n- Sign-flip ASV \"has no E-value counterpart\" 未解释结构性障碍。\n- 与 Cinelli & Hazlett (2020) 的 partial R² 无形式化对比。\n- 建议：添加表格形式化对比 ASV、E-value、robustness value。\n\nW4. [should-fix] Abstract 信息密度过高。\n- 至少 7 个独立数字，造成认知超载。\n- 建议：聚焦 2-3 个核心定量发现。\n\nW5. [should-fix] 七种拓扑中部分对 NLP 的实践相关性不足。\n- M-bias、front-door、IV 未给出 NLP 场景实例。\n- Section 4.4 仅使用 confounding 和 exposure。\n- 建议：为每种拓扑给出至少一个 NLP 应用场景。\n\nW6. [should-fix] FWL 不变性作为\"贡献\"定位过高。\n- 本质是负面结果，是 FWL 定理的直接推论。\n- Algorithm 1 是决策树而非方法论创新。\n\nW7. [minor] 非差异误分类假设可能被 LLM 系统性违反。\n- Appendix B.6 stress test 仅考虑温和扰动。\n- Limitations 中讨论较简短。\n\nW8. [minor] 缺少 DAG 拓扑未知时的讨论。\n\n## Questions\n\nQ1. Conjecture 1 证明障碍——维度诅咒、非凸性、还是组合爆炸？\nQ2. 二元结果下 logistic 回归是否会质性改变符号保持条件？\nQ3. M-bias 的 Sign-flip ASV = ∞ 是否可以被证明？\nQ4. PPI++ 在 M-bias 下的负值（-88.0）意味着什么？\nQ5. 56 个 HumAID 场景的 null result (ρ=-0.10, p=0.45) 的 power analysis？\n\n## Missing References\n\nMR1. Veitch, Wang & Blei (2020) — NLP+因果推断。\nMR2. Imai, Keele & Tingley (2010) — 因果中介分析。\nMR3. Roberts, Stewart & Tingley (2020) 或 Pryzant et al. (2021) — 基于文本的因果推断。\nMR4. Cinelli & Hazlett (2020) 的形式化对比缺失。\n\n## Minor Issues\n\nMI1-MI6（略）。\n\n## Overall Assessment\nScore: 3.5 (Borderline Conference)\n\n---\n\n请对 Reviewer 2 的每个 Weakness (W1-W8) 和 Question (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-23T09:34:58.114544+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1512
}
```

</details>

---


### Assistant

_source line 1050 · 2026-05-23T09:35:00.665460+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 102

## Round 102

2 recorded events


### User

_source line 1051 · 2026-05-23T09:35:03.369568+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要：**

- **Overall: 3.5（Borderline Conference）**
- **Soundness: 3.5** — K=2 证明严谨，但 proportional effects 15-17% 失败率和 IV 表述内部不一致
- **Excitement: 3.5** — 选题时效性强，FWL invariance 是亮点，但核心技术是经典理论延伸
- **Reproducibility: 4** — 实验设计清晰，代码/数据承诺释放

**主要问题：** W1（Theorem 1 限 K=2 的呈现不够突出）、W2（proportional effects 失败率）、W3（IV sign reversal 表述在 Section 4.2 vs Appendix B.4 vs Abstract 之间不一致）、W4（线性 SEM 下的 FWL invariance 在 logistic 回归中对 exposure 不成立但正文表述模糊）、W5（缺少商业 LLM 验证）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1052 · 2026-05-23T09:35:07.529991+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 103

## Round 103

2 recorded events


### User

_source line 1053 · 2026-05-23T09:37:16.454253+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Weaknesses 逐条回应

**[AGREE] R1-W1: Theorem 1 限于 K=2，Abstract/Intro 呈现不够突出**

同意。这与我自己 W2 的核心关切一致。论文 Abstract 第一段写 "We derive bias expressions for seven canonical topologies under K-class non-differential misclassification"，而 Theorem 1 实际只覆盖 K=2 + proportional effects + (C₀)ⱼⱼ ≥ 1/2 三个条件。K≥3 的排序依赖 Conjecture 1（ε-approximate，未证明）。Abstract 中应明确区分"K=2 已证明"和"K≥3 为数值验证"这两个层级。R1 的建议合理。

**[AGREE] R1-W2: Proportional effects 假设失败率 15-17% 不可忽视**

同意。Appendix B.17 Table 16 报告 proportional effects 违反率在 real LLM 矩阵下为 15-17%（Sparse DGP 高达 24.2%）。当 f≠λg 时，论文退回 Proposition 3（一般情形），其条件 |τ| > B 需要知道 worst-case bias bound——这在实践中通常不可知。正文对这一退化路径的讨论不足。

补充我的观察：这一问题与我 W7（非差异假设鲁棒性）相关联。如果 proportional effects 和非差异假设都可能被违反，论文的理论保证在实践中的覆盖率可能低于读者的直觉预期。建议论文给出一个综合的"coverage analysis"——在多少比例的现实 LLM 配置中，至少有一组理论保证成立。

**[AGREE] R1-W3: IV 拓扑 sign reversal 表述存在内部不一致**

强烈同意。这是我在首轮审稿中未捕获的一个重要问题。R1 正确识别了三处矛盾：

1. **Abstract**（page 1）："no sign reversal occurs for all other topologies including IV"
2. **Section 4.2**（page 7）："diagonal dominance C₀ > 0.8 reduces but does not eliminate sign reversal risk"
3. **Appendix B.4**（page 23）："diagonal dominance prevents this crossing"

(2) 和 (3) 直接矛盾——一个说 "does not eliminate"，另一个说 "prevents"。Abstract 的 "no sign reversal" 与 Section 4.2 的 "does not eliminate" 也矛盾。

进一步，Table 1（page 7）报告 IV 的 Sign Flip 为 52.6%（under Dirichlet(1,1,1) random matrices）。如果 Abstract 的 claim 是"在 realistic LLM accuracy 下无 sign reversal"，则需要明确"realistic"的操作定义（是 diagonal dominance > 某阈值？是真实 LLM 矩阵的 empirical 范围？），并解释为何 Section 4.2 的措辞暗示残留风险。

这是一个需要修复的 factual consistency 问题，属于 **must-fix** 级别，而非 R1 标记的 should-fix。

**[REBUT] R1-W4: 线性 SEM 限制对 EMNLP 受众的适用性**

部分反驳。R1 引用 Appendix B.14 Table 13 称 exposure 在 logistic 回归下有"~22% 到 ~78% 偏差缩减"，但需要区分两个不同的 claim：

1. **FWL 不变性**适用于四种**协变量拓扑**（confounding, mediation, collider, M-bias），不适用于 exposure。论文在 Appendix B.2 和 B.14 中明确区分了这一点。对协变量拓扑，Table 13 的 logistic bias reduction 均为 ~0.003%——确实 negligible。

2. **Exposure 不是协变量拓扑**——A 是 treatment variable，FWL 论证不适用。Exposure 下 logistic 回归的 bias reduction 不构成对 FWL invariance claim 的反驳，因为该 claim 本身不覆盖 exposure。

R1 的实质关切——"正文 Section 4.5 似乎将 FWL invariance 泛化到了 logistic 情形"——我同意措辞需要更精确。但 R1 将 exposure 的 logistic 结果作为反驳 FWL invariance 的证据，在逻辑上有错位：FWL invariance 只 claim 协变量拓扑，exposure 本就在 claim 之外。

**建议**：论文应在 Section 4.5 正文中更明确地限定"FWL invariance applies to covariate topologies only; exposure is excluded because A enters as treatment, not covariate."

**[REBUT] R1-W5: 经验验证缺少商业 LLM**

反驳。论文的核心贡献是**理论框架**（bias 表达式、ASV、FWL 不变性），经验验证是辅助性的。理论结果仅依赖混淆矩阵的数学性质（column-stochastic, diagonal dominance），不依赖生成该矩阵的 LLM 架构。

论文已使用了参数范围从 Llama-4-Maverick 到 Qwen3-235B 到 DeepSeek-Chat 的多种模型（Section 4.4），覆盖了从低精度到高精度的混淆矩阵。商业 LLM 的混淆矩阵不太可能展示超出现有开源 LLM 覆盖范围的结构性新模式——除非有证据表明商业 LLM 的误差结构质性不同。

此外，这是 EMNLP 投稿，而非 LLM benchmarking——缺少特定商业 API 不应被视为方法论缺陷。

**[AGREE] R1-W6: Conjecture 1 数值验证在高维度下覆盖不足**

部分同意。K=7 混淆矩阵有 42 个自由参数（7×7 矩阵 - 7 列和约束 = 42），每拓扑 10,000 个样本的覆盖密度确实远低于 K=3 的情况（K=3 有 6 个自由参数）。这不足以声称高维空间的全面扫描。

不过，如果 monotonicity 的违反是结构性的（而非罕见角落），10,000 样本应能捕获。论文 Appendix B.12 Table 10 报告 K=7 的 worst-case violation 与 K=3 可比，暗示违反模式是低维的。但这不能替代证明。

建议增加 K=7 的采样量至至少 100,000，或对采样密度做 power analysis。

---

### Questions 逐条回应

**[AGREE] R1-Q1: Proportional effects 失败率是否与模型类型或 K 相关？**

合理的追问。如果失败率集中在特定模型族（如低精度的小模型）或特定 K 值，那么对高质量 LLM 用户的实践影响更小。论文应给出按模型和 K 分层的违反率和偏差幅度。

**[AGREE] R1-Q2: IV sign reversal 表述不一致**

强烈同意，如上 W3 回应。这是 factual consistency 问题，必须修复。

**[AGREE] R1-Q3: FWL invariance 对 exposure 在非线性情形下的适用性**

同意这是一个重要问题，但需要重新框定。如 W4 回应所述，FWL invariance 本身不 claim 覆盖 exposure。真正的问题是：**Algorithm 1 对 exposure 的推荐（"Naive plug-in, MLA: best; gold-free alternatives exist"）在 logistic 回归下是否仍有效？** 如果 exposure 在非线性模型下的 bias reduction 结构不同，Algorithm 1 的推荐可能需要按模型类型条件化。这确实值得作者回应。

**[AGREE] R1-Q4: ASV δ* 阈值选择的敏感性**

同意。论文使用 δ* 阈值（如 magnitude ASV 的 10% bias threshold, Section 3.3 的 τ=0.05），但未系统展示阈值选择如何影响拓扑排序。如果排序在合理阈值范围内不稳定，ASV 框架的 practical guidance 价值会降低。Appendix B.11 的 cross-K robustness 检验展示了跨 K 的稳定性，但未展示跨阈值的稳定性。

**[REBUT] R1-Q5: 为什么未包含商业 LLM？**

如 W5 回应，商业 LLM 缺失不构成方法论缺陷。实际原因可能是成本和 API 访问限制（blind review 下不便说明），且不影响理论 claim 的有效性。

---

### 与我自身审稿的总结性交叉比较

R1 和我在以下核心关切上**高度一致**：
1. Conjecture 1 未被证明是理论贡献的显著弱点（我的 W2，R1 的 W1）
2. 论文对 EMNLP 受众的可达性存在问题（我的 W1 更强调术语解释，R1 更强调理论层级呈现——两者互补）
3. 附录与正文的一致性需要检查（R1 的 W3 是一个我未捕获的重要 factual 问题）

R1 新增的有价值发现：
- **W3（IV 表述不一致）**是一个重要的 factual consistency 问题，我认为应升级为 **must-fix**
- **W2（proportional effects 失败率）**与我的 W7（非差异假设鲁棒性）结合，形成对理论保证实际覆盖率的系统性关切

我不同意的点：
- **W4**：R1 将 exposure 的 logistic 结果作为反驳 FWL invariance 的证据存在逻辑错位
- **W5/Q5**：商业 LLM 缺失不是关键缺陷

**我维持 Overall 3.5（Borderline Conference）的评分**。R1 的 W3 发现加强了我对论文需要修订的判断，但 R1 的 S2（诚实的理论层级体系）也正确指出了论文的一个重要优点——作者对证明/验证/猜想的层级划分是透明的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1054 · 2026-05-23T09:37:24.327674+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 104

## Round 104

2 recorded events


### User

_source line 1055 · 2026-05-23T09:37:26.989573+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **W1-W3, W6, Q1-Q4**：[AGREE]，其中 W3（IV sign reversal 表述不一致）是 R1 发现的重要问题，我建议升级为 must-fix
- **W4**：[REBUT]——R1 将 exposure 的 logistic 结果用于反驳 FWL invariance 存在逻辑错位，FWL invariance 本就不 claim 覆盖 exposure
- **W5, Q5**：[REBUT]——商业 LLM 缺失不构成方法论缺陷
- 维持 Overall 3.5 评分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1056 · 2026-05-23T09:37:31.448664+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 105

## Round 105

10 recorded events


### User

_source line 1057 · 2026-05-23T09:37:39.542290+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Weaknesses

**[AGREE] R2-W1: EMNLP 受众的可达性障碍**
同意可达性是一个问题，但建议从 must-fix 降为 should-fix。理由：
1. plim 确实仅在 p4 脚注中定义，但这是计量经济学标准术语，EMNLP 因果推断方向的读者应当熟悉。
2. FWL 分解放在 Appendix A.2 是合理的篇幅安排——正文 8 页限制下不可能展开所有技术细节。
3. 但我同意 Section 3.1 开头加 1-2 段直觉性文字会显著改善可读性，特别是对 Eq.(1) 的残差化含义做简短解释。Table 18 的交叉引用也值得添加。
4. 总体而言，这是写作改进建议而非方法论问题，不应影响接收决定。

**[REBUT] R2-W2: Conjecture 1 未被证明是 must-fix**
不同意 must-fix 的严重性定级。理由：
1. R2 的表述暗示 Conjecture 1 是"核心理论贡献"——但实际上论文的核心理论贡献是**一般 K 的闭式偏差表达式**（Section 3.2, Eq.1-2 等）和 **sign preservation 命题**（Propositions 1-6），这些都是对一般 K 的解析证明，不依赖 Conjecture 1。
2. Conjecture 1 仅涉及 **envelope monotonicity**（偏差大小随误分类程度单调变化），这是 ASV 排序的支撑之一，但不是唯一支撑——经验证据（Table 3, Section 4.3 的 161 scenarios）独立验证了拓扑排序。
3. 论文诚实地将其标记为 "Conjecture" 而非 "Theorem"，并提供了 210,000 矩阵的数值验证（Appendix B.12），ε < 0.06 的偏差极小。
4. R2 说"未解释为何 K=2 perspective function 凸性不能推广"——Appendix A.4（p14）实际上解释了：K≥3 时 V₀(δ) 的结构从标量变为矩阵值函数，perspective function 的凸性论证不再直接适用。论文在 p14 末尾写道 "a strict monotonicity proof for the general case remains open"，已明确承认这一技术障碍。
5. 建议维持 should-fix：在正文中更显式地说明 K=2→K≥3 的推广障碍即可。

**[AGREE] R2-W3: ASV 与 E-value 的比较不够充分**
同意，但补充：
1. 论文确实在 Section 3.3 将 ASV 定位为 E-value 的离散测量误差对应物，并在 Section 2 引用了 VanderWeele and Ding (2017)。
2. 但 R2 的建议合理——一个形式化的对比表（ASV vs. E-value vs. partial R²）能帮助读者快速理解 ASV 的定位和边界。
3. 特别是 Sign-flip ASV "has no E-value counterpart" 这一说法（p5）需要更明确的解释——为什么 E-value 框架无法自然扩展到符号反转？核心区别在于 E-value 度量的是未观测混杂的强度（连续标量），而 Sign-flip ASV 度量的是离散误分类矩阵到符号反转边界的距离，两者的数学结构不同。论文应当阐明这一点。

**[REBUT] R2-W4: Abstract 信息密度过高**
不同意。
1. 学术论文的 Abstract 应当提供精确、可验证的定量声明。本文 Abstract 的数字（MAPE 1.6%, sign reversal 2.1%, 161 scenarios 等）均可在正文中直接验证，这是好的科学实践。
2. 对比 EMNLP 近年发表的方法论论文（如 Feder et al. 2022 的因果推断综述），类似密度的 Abstract 是常见的。
3. 删减定量信息反而会削弱 Abstract 的信息价值——审稿人和读者需要这些数字来快速判断论文的贡献规模。
4. 如果有具体的冗余数字可以删除，R2 应指出是哪些；泛泛地说"过多"不够具体。

**[AGREE] R2-W5: 部分拓扑缺少 NLP 场景示例**
部分同意。
1. 论文确实只为 confounding（Section 4.4 ClinicalBERT）和 exposure（隐含在框架中）提供了具体 NLP 应用。
2. 但我认为这不是 should-fix——论文的贡献是通用因果推断框架，不限于 NLP。七种拓扑中的每一种在社会科学因果推断中都有确立的用途。
3. 不过，为 M-bias 和 front-door 各给一个简短的 NLP 场景描述（1-2 句）确实能增强论文对 EMNLP 读者的相关性。例如：front-door 可类比于通过中间文本特征识别处理效应的场景；IV 可类比于使用外生事件作为工具变量的自然实验。
4. 建议从 should-fix 降为 minor。

**[REBUT] R2-W6: FWL 不变性作为"贡献"定位过高**
强烈不同意。
1. R2 称 FWL 不变性是"FWL 定理的直接推论"——这忽略了关键的非平凡性。FWL 定理本身是关于最小二乘回归的代数恒等式；**识别出它在误分类校正语境下的含义**（矩阵校正方法对四种协变量拓扑无效）是一个需要将 FWL 与混淆矩阵的列空间性质结合的洞见，而非"直接"可得。
2. 具体地：关键步骤是认识到如果 D̃ = D* × M（任意可逆线性变换），则 col(D̃) = col(D*)，因此 M_{D̃} = M_{D*}，处理效应 τ 的 FWL 残差不变。这需要理解(a) naive 校正是列空间变换，(b) 列空间不变性通过 FWL 传递到处理效应估计。对非计量经济学背景的读者，这绝非显然。
3. 更重要的是这一结果的**实践含义**：它直接告诉实践者不要在 confounding/mediation/collider/M-bias 拓扑下浪费时间做矩阵校正，转而使用 DSL 或 PPI++ 等绕过 FWL 的方法。Table 4 的经验结果（Naive MLA 对这四种拓扑的 RMSE 缩减为 0.0%）完全证实了这一理论预测。
4. Algorithm 1 虽然是"决策树"，但其中编码的拓扑-方法映射此前不存在于文献中。将其贬为"非方法论创新"忽略了系统性综合的价值。
5. 建议：此条 weakness 不成立，可删除。

**[AGREE] R2-W7: 非差异误分类假设可能被 LLM 系统性违反**
同意这是一个合理的 minor concern。我在自己的审稿中也提出了相同问题（my W3 关于 IV 表述不一致也间接涉及此点）。Appendix B.6 的 stress test 覆盖了温和扰动（ε ≤ 0.5），但仅考虑均匀扰动，未测试结构化违反（如 outcome-conditional misclassification）。不过论文在 Section 3.1 已识别出 LLM 标注中该假设成立的条件（"the LLM receives only source text and classifies without observing the outcome Y or covariates"），并在 Limitations 中承认了例外情形。作为 minor issue 处理恰当。

**[AGREE] R2-W8: 缺少 DAG 拓扑未知时的讨论**
部分同意，但认为这是 minor 而非 should-fix。
1. 几乎所有因果推断方法都假设 DAG 已知或调整集已确定——这是该领域的标准假设。
2. 论文的贡献是"给定 DAG，标注错误如何影响估计"，而非"如何发现 DAG"。
3. 但 R2 的建议合理——简要讨论 DAG 未知时的应对策略（如：对所有可能拓扑运行 ASV 并取最保守结果）会有实践价值。1-2 句即可。

---

### Questions

**[AGREE] R2-Q1: Conjecture 1 证明障碍**
好的问题。如上所述（R2-W2 回应），Appendix A.4 已部分回答：K≥3 时 V₀(δ) 从标量变为矩阵值函数，perspective function 凸性论证失效。我同意论文应在正文中更明确地说明具体障碍（维度诅咒 vs. 非凸性 vs. 组合爆炸——从 Appendix A.4 的分析看，主要是矩阵结构导致的非凸性）。

**[AGREE] R2-Q2: Logistic 回归下符号保持条件**
重要问题，与我的 W4 高度相关。Appendix B.7 显示 sign-flip patterns 在 logistic DGP 下"virtually identical"，但 Appendix B.14 Table 13 显示 exposure 拓扑的偏差缩减在 logistic 下达 ~22%-78%（远非 negligible）。论文需要更精确地限定哪些结论在非线性模型下成立（sign preservation: 是），哪些不成立（FWL invariance for exposure: 否）。

**[AGREE] R2-Q3: M-bias Sign-flip ASV = ∞ 是否可以被证明**
好的问题。从论文内容看：
- M-bias 的 sign preservation 目前仅有数值验证（Table 1: 0% sign flip across 100,000 matrices），未有解析证明。
- Proposition 1 覆盖了 confounding 和 collider 的解析证明，但 M-bias 仅标注为 "numerically verified"（Section 3.2, p5: "verify it numerically for mediation, M-bias, and front-door"）。
- 如果能将 M-bias sign preservation 提升为解析证明，则 Sign-flip ASV = ∞ 自然成立。否则它只是一个数值结论。
- 这确实是一个可以加强论文的方向。

**[AGREE] R2-Q4: PPI++ 在 M-bias 下的负值**
同意论文应解释 WHY PPI++ 对 M-bias 有害。Table 4 报告 -88.0% RMSE 但未解释机制。可能的原因：M-bias 下误分类是"保护性的"（|B(C)| ≤ |B(I)|, Collider/M-bias non-increasing per Conjecture 1），PPI++ 的校正反而移除了这种保护性衰减，放大了偏差。论文应当明确说明这一机制。

**[REBUT] R2-Q5: 56 个 HumAID 场景的 null result power analysis**
部分反驳。
1. R2 关心 ρ=-0.10 (p=0.45) 在 n=56 下的统计功效。对 |ρ|=0.10, n=56, α=0.05 的功效约为 0.12——确实很低。
2. 但 Fig 3 的论点**不是**证明相关性为零，而是展示"分类精度不是因果偏差的可靠预测器"。即使相关性非零但很弱（|ρ|=0.10），这一论点也成立。
3. 更关键的是 Fig 3 的定性模式：相同 F1 分数的不同拓扑产生截然不同的偏差幅度（0.001 到 0.690），这个变异性本身就足以支持"拓扑决定偏差"的论点，不需要依赖相关系数。
4. 不过，补充 power analysis 或报告 confidence interval for ρ 是合理的改进，可以 1 句话完成。

---

### Missing References

**[REBUT] R2-MR1 (Veitch, Wang & Blei, 2020)**
不同意这是显著遗漏。Veitch et al. (2020) 研究的是 text-as-treatment/confounder 的因果推断，关注的是如何利用文本表示来控制混杂——与本文研究的标注误差传播问题在研究问题上不同。本文的 Related Work (Section 2) 已覆盖了更直接相关的 NLP×因果推断文献（Feder et al. 2022, Keith et al. 2020, Egami et al. 2023）。

**[AGREE] R2-MR2 (Imai, Keele & Tingley, 2010)**
同意可以引用。论文涉及 mediation topology 的分析（Section 3.2, Appendix A.5），引用 Imai et al. (2010) 的因果中介分析框架作为背景文献是合理的，虽然不引用也不影响论文完整性。

**[AGREE] R2-MR3 (Roberts et al. 2020 / Pryzant et al. 2021)**
同意可以在 Related Work 中补充 1-2 个 text-based causal inference 的引用以加强 NLP 定位。

**[REBUT] R2-MR4 (Cinelli & Hazlett, 2020 形式化对比缺失)**
论文已引用 Cinelli & Hazlett (2020)——Section 2 (p3) 和 Section 3.3 均有引用。R2 要求的是"形式化对比"而非引用本身，这与 W3 重复（ASV vs. E-value/partial R² 的形式化比较），已在 W3 回应中处理。

---

### 综合评价

R2 的审稿整体质量高，但存在两个过度定级的问题：
1. **W2 (Conjecture 1) 不应为 must-fix**：论文的核心贡献是偏差表达式和 sign preservation（均有解析证明），不是 Conjecture 1。将未解决的单调性猜想视为"削弱核心理论贡献"是对论文贡献结构的误读。
2. **W6 (FWL 不变性) 不应为 weakness**：将 FWL 在误分类校正语境下的含义识别出来并实证验证，是有意义的贡献。

R2 的其他意见（W1 可达性、W3 ASV 对比、W5 NLP 场景、W7-W8 minor issues）均为合理的改进建议。

我维持自己的 Overall 3.5 评分，与 R2 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1058 · 2026-05-23T09:37:59.681370+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-23T09:37:59.932715+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T09:21:41.432837+00:00\", \"completed_at\": \"2026-05-23T09:21:45.091252+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-23T09:37:59.933063+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-23T09:37:59.983663+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-23T09:43:07.872300+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 13\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：23 个配置缺少商业 API（GPT-4/Claude）、>235B 模型、NER 等结构化任务。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 R1 再次提出(W5)。R2 REBUT——理论结论仅依赖混淆矩阵数学性质，不依赖 LLM 架构。Director 采纳 R2：降为 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 13\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补直觉解释。R1 新增批评：B.5 stress test 仅用随机扰动模型。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识 must-fix（R1）/should-fix（R2）。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W7 minor。Section 3.1 已有成立条件识别和 stress test（Appendix B.6）。R1 未单独提出。共识降为 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 13\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Abstract 至少 9-10 个定量信息点。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W4 再次提出（至少 7 个独立数字）。R1 REBUT——精确定量是好的实践，删减降低信息价值。Director 保留分歧。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 13\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献，但 magnitude ASV 与 E-value 同构度高。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-W3 再次提出：形式化对比不充分，需表格对比 ASV/E-value/partial R²。R1 AGREE 并补充应阐明 Sign-flip ASV 无法被 E-value 自然扩展的结构性原因。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 13\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"Section 4.4 已解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-Q4 追问机制。R1 AGREE 并给出可能解释（M-bias 误分类是保护性的，PPI++ 移除保护性衰减）。论文应明确说明。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 W1 再次提出。R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：General case 15-17% 违反仍是已知限制。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W2 再次提出：15-17% 失败率（Sparse DGP 24.2%）在正文中讨论不足。R2 AGREE 并建议给出综合 coverage analysis。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R4-W6 合并。R2-W3 + R1 AGREE：需形式化对比表。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被 R11 两位 Reviewer 赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加 Collider amplification 脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论 PPI++ 对 M-bias 有害。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：exposure/IV 的 CI 跨界是拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧→R2 REBUT 成功：排名稳定性比绝对值更重要。Director 降为 minor。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 R1-Q4 间接涉及：δ* 阈值选择敏感性，跨阈值排序稳定性未验证。R2 AGREE。minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"R11 未再提及。Algorithm 1 整体被两位 Reviewer 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级为 should-fix。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出。Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W1 + R2-W2 再次提出。R2 评 must-fix，R1 REBUT：核心贡献是 bias expressions + sign preservation（解析证明），非 Conjecture 1。Director 采纳 R1——Conjecture 1 仅支撑 ASV monotonicity，非核心理论贡献。维持 should-fix。共识：Abstract 应更突出区分 K=2 已证明 vs K≥3 数值验证。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"正文讨论 Conjecture 1 失效时对 ASV 实践指导的影响\"\n        assigned_to: agent\n        status: open\n      - round: 13\n        action: \"Abstract 明确区分 K=2 formal guarantees 和 K≥3 numerical evidence\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：General case 15-17% violation 是已知限制。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R6-M3 合并。R1-W2 再提。R2 AGREE + 建议综合 coverage analysis。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"分歧：R2 认为与 E-value 同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R4-W6 合并。形式化对比不足是共识。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"均匀 ε 局限。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R1 新增：stress test 仅随机扰动，未测结构化违反。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 R1 评 must-fix，R2 评 should-fix。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W7 minor。Section 3.1 已有条件讨论 + stress test。改善明显。降为 minor。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧 → R2 REBUT 成功。Director 降为 minor。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。可能已充分缓解。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用 ding_vanderweele2016。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 NEW-1 和 R8-C2 讨论。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 合并到 R6-M3 和 NEW-1。R2 建议综合 coverage analysis。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需 Section 3.1 加线性 SEM 动机。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"主文整合 logistic 结果不足。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Appendix B.6/B.13 logistic 验证充分但正文引用不足。已添加。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W4 + R2-W1 再次提出。plim 脚注和 FWL 内联定义已添加（R12 修复），但 R2 认为仍不充分——需 Section 3.1 开头加 1-2 段直觉性文字。R1 同意但建议降为 should-fix。FWL invariance 在 logistic 下对 exposure 不成立的措辞需精确化。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 12\n        action: \"Section 4.5 增加 logistic DGP 总结 + 引用 Appendix B.13\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 加 1-2 段直觉性文字解释 plim、FWL 分解、残差化\"\n        assigned_to: agent\n        status: open\n      - round: 13\n        action: \"Section 4.5 精确限定 FWL invariance 仅适用于 covariate topologies，exposure 在 logistic 下不成立\"\n        assigned_to: agent\n        status: open\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-Q1 追问具体障碍（维度/非凸/组合）。R1 AGREE 并指出 Appendix A.4 已部分回答（K≥3 V₀(δ) 从标量→矩阵值，perspective function 失效）。应在正文更明确说明。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"R1 REBUT 成功。Introduction 措辞准确且有事实支撑。\"\n    resolution_round: 12\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 R1-W3。共识：不影响核心贡献。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 合并到 R1-W3。R2 REBUT。Director 降为 minor。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被 R11 赞为 S5/S6 strength，可操作性获认可。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增强论文对 EMNLP 应用导向读者的说服力。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：ClinicalBERT 案例最接近端到端验证。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。Section 4.5 已包含 ClinicalBERT 提及。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增加 3-4 句直觉语言解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出（R2-W3）。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-W1 (must-fix) + R1 AGREE (suggest should-fix)。plim 脚注和 FWL 内联定义已添加（R12修复），但 R2 认为仍不充分。需 Section 3.1 开头 1-2 段直觉文字 + Table 18 交叉引用。与 R9-C2 合并。\"\n    action_items:\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 需更充分的直觉性解释段落\"\n        assigned_to: agent\n        status: open\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"EXP-2 完成：K=3/5/10 × 7 topologies。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R12 未单独提出。Section 4.2 已有 practitioners 指导句。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 已添加。\"\n    resolution_round: 13\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文 Section 5 (Conclusion) 溢出至 p9，违反 EMNLP 2026 的 8 页限制\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩，视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语（plim/FWL）对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"plim 首次使用加脚注 + FWL 首次使用加内联解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 修复已部分生效（plim 脚注 + FWL 内联定义可见），但 R2-W1 仍评 must-fix：需更深入的直觉解释，不仅仅是定义。与 R11-W2 合并。\"\n    action_items:\n      - round: 12\n        action: \"plim 脚注 + FWL 内联定义\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 加直觉段落（超越单纯定义）\"\n        assigned_to: agent\n        status: open\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 均已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: minor\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果，适用条件未标注\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"Algorithm 1 caption 已添加 K=3 calibration 注释。\"\n    resolution_round: 13\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 和 Figure 7 视觉问题\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n\n  # === Round 13 新发现 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract、Section 4.2、Appendix B.4 之间存在 factual 不一致\"\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R1-W3 首先发现。Abstract 说 'no sign reversal for IV'，Section 4.2 说 'does not eliminate sign reversal risk'，Appendix B.4 说 'diagonal dominance prevents this crossing'。三处相互矛盾。R2 交叉回应 AGREE 并升级为 must-fix。共识：必须统一措辞，明确区分 violation（偏差存在）和 sign reversal（符号反转），并定义 'realistic' 的操作边界。\"\n    action_items:\n      - round: 13\n        action: \"统一 Abstract/Section 4.2/Appendix B.4 关于 IV sign reversal 的措辞\"\n        assigned_to: agent\n        status: open\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑（M-bias, front-door, IV）缺少 NLP 应用场景示例\"\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [R2]\n        note: \"R2-W5 提出。R1 部分 AGREE 但建议降为 minor——论文贡献是通用因果推断框架，不限于 NLP。Director 采纳降级。但建议为 M-bias/front-door 各加 1-2 句 NLP 场景。\"\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 新发现的缺失引用\"\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [R2]\n        note: \"R2 提出 3 篇：(1) Imai, Keele & Tingley (2010) 因果中介分析——R1 AGREE；(2) Roberts/Pryzant et al. text-based causal inference——R1 AGREE；(3) Veitch, Wang & Blei (2020)——R1 REBUT，研究问题不同。Director：(1)(2) 建议引用，(3) 不强制。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 13\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：23 个配置缺少商业 API（GPT-4/Claude）、>235B 模型、NER 等结构化任务。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 R1 再次提出(W5)。R2 REBUT——理论结论仅依赖混淆矩阵数学性质，不依赖 LLM 架构。Director 采纳 R2：降为 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 13\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补直觉解释。R1 新增批评：B.5 stress test 仅用随机扰动模型。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识 must-fix（R1）/should-fix（R2）。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W7 minor。Section 3.1 已有成立条件识别和 stress test（Appendix B.6）。R1 未单独提出。共识降为 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 13\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Abstract 至少 9-10 个定量信息点。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W4 再次提出（至少 7 个独立数字）。R1 REBUT——精确定量是好的实践，删减降低信息价值。Director 保留分歧。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 13\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献，但 magnitude ASV 与 E-value 同构度高。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-W3 再次提出：形式化对比不充分，需表格对比 ASV/E-value/partial R²。R1 AGREE 并补充应阐明 Sign-flip ASV 无法被 E-value 自然扩展的结构性原因。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 13\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"Section 4.4 已解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-Q4 追问机制。R1 AGREE 并给出可能解释（M-bias 误分类是保护性的，PPI++ 移除保护性衰减）。论文应明确说明。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 W1 再次提出。R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：General case 15-17% 违反仍是已知限制。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W2 再次提出：15-17% 失败率（Sparse DGP 24.2%）在正文中讨论不足。R2 AGREE 并建议给出综合 coverage analysis。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R4-W6 合并。R2-W3 + R1 AGREE：需形式化对比表。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被 R11 两位 Reviewer 赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加 Collider amplification 脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论 PPI++ 对 M-bias 有害。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：exposure/IV 的 CI 跨界是拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧→R2 REBUT 成功：排名稳定性比绝对值更重要。Director 降为 minor。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 R1-Q4 间接涉及：δ* 阈值选择敏感性，跨阈值排序稳定性未验证。R2 AGREE。minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"R11 未再提及。Algorithm 1 整体被两位 Reviewer 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级为 should-fix。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出。Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W1 + R2-W2 再次提出。R2 评 must-fix，R1 REBUT：核心贡献是 bias expressions + sign preservation（解析证明），非 Conjecture 1。Director 采纳 R1——Conjecture 1 仅支撑 ASV monotonicity，非核心理论贡献。维持 should-fix。共识：Abstract 应更突出区分 K=2 已证明 vs K≥3 数值验证。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"正文讨论 Conjecture 1 失效时对 ASV 实践指导的影响\"\n        assigned_to: agent\n        status: open\n      - round: 13\n        action: \"Abstract 明确区分 K=2 formal guarantees 和 K≥3 numerical evidence\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：General case 15-17% violation 是已知限制。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R6-M3 合并。R1-W2 再提。R2 AGREE + 建议综合 coverage analysis。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"分歧：R2 认为与 E-value 同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R4-W6 合并。形式化对比不足是共识。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"均匀 ε 局限。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R1 新增：stress test 仅随机扰动，未测结构化违反。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 R1 评 must-fix，R2 评 should-fix。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W7 minor。Section 3.1 已有条件讨论 + stress test。改善明显。降为 minor。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧 → R2 REBUT 成功。Director 降为 minor。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。可能已充分缓解。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用 ding_vanderweele2016。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 NEW-1 和 R8-C2 讨论。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 合并到 R6-M3 和 NEW-1。R2 建议综合 coverage analysis。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需 Section 3.1 加线性 SEM 动机。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"主文整合 logistic 结果不足。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Appendix B.6/B.13 logistic 验证充分但正文引用不足。已添加。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W4 + R2-W1 再次提出。plim 脚注和 FWL 内联定义已添加（R12 修复），但 R2 认为仍不充分——需 Section 3.1 开头加 1-2 段直觉性文字。R1 同意但建议降为 should-fix。FWL invariance 在 logistic 下对 exposure 不成立的措辞需精确化。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 12\n        action: \"Section 4.5 增加 logistic DGP 总结 + 引用 Appendix B.13\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 加 1-2 段直觉性文字解释 plim、FWL 分解、残差化\"\n        assigned_to: agent\n        status: open\n      - round: 13\n        action: \"Section 4.5 精确限定 FWL invariance 仅适用于 covariate topologies，exposure 在 logistic 下不成立\"\n        assigned_to: agent\n        status: open\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-Q1 追问具体障碍（维度/非凸/组合）。R1 AGREE 并指出 Appendix A.4 已部分回答（K≥3 V₀(δ) 从标量→矩阵值，perspective function 失效）。应在正文更明确说明。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"R1 REBUT 成功。Introduction 措辞准确且有事实支撑。\"\n    resolution_round: 12\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 R1-W3。共识：不影响核心贡献。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 合并到 R1-W3。R2 REBUT。Director 降为 minor。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被 R11 赞为 S5/S6 strength，可操作性获认可。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增强论文对 EMNLP 应用导向读者的说服力。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：ClinicalBERT 案例最接近端到端验证。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。Section 4.5 已包含 ClinicalBERT 提及。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增加 3-4 句直觉语言解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出（R2-W3）。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-W1 (must-fix) + R1 AGREE (suggest should-fix)。plim 脚注和 FWL 内联定义已添加（R12修复），但 R2 认为仍不充分。需 Section 3.1 开头 1-2 段直觉文字 + Table 18 交叉引用。与 R9-C2 合并。\"\n    action_items:\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 需更充分的直觉性解释段落\"\n        assigned_to: agent\n        status: open\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"EXP-2 完成：K=3/5/10 × 7 topologies。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R12 未单独提出。Section 4.2 已有 practitioners 指导句。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 已添加。\"\n    resolution_round: 13\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文 Section 5 (Conclusion) 溢出至 p9，违反 EMNLP 2026 的 8 页限制\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩，视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语（plim/FWL）对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"plim 首次使用加脚注 + FWL 首次使用加内联解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 修复已部分生效（plim 脚注 + FWL 内联定义可见），但 R2-W1 仍评 must-fix：需更深入的直觉解释，不仅仅是定义。与 R11-W2 合并。\"\n    action_items:\n      - round: 12\n        action: \"plim 脚注 + FWL 内联定义\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 加直觉段落（超越单纯定义）\"\n        assigned_to: agent\n        status: open\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 均已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: minor\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果，适用条件未标注\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"Algorithm 1 caption 已添加 K=3 calibration 注释。\"\n    resolution_round: 13\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 和 Figure 7 视觉问题\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n\n  # === Round 13 新发现 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract、Section 4.2、Appendix B.4 之间存在 factual 不一致\"\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R1-W3 首先发现。Abstract 说 'no sign reversal for IV'，Section 4.2 说 'does not eliminate sign reversal risk'，Appendix B.4 说 'diagonal dominance prevents this crossing'。三处相互矛盾。R2 交叉回应 AGREE 并升级为 must-fix。共识：必须统一措辞，明确区分 violation（偏差存在）和 sign reversal（符号反转），并定义 'realistic' 的操作边界。\"\n    action_items:\n      - round: 13\n        action: \"统一 Abstract/Section 4.2/Appendix B.4 关于 IV sign reversal 的措辞\"\n        assigned_to: agent\n        status: open\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑（M-bias, front-door, IV）缺少 NLP 应用场景示例\"\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [R2]\n        note: \"R2-W5 提出。R1 部分 AGREE 但建议降为 minor——论文贡献是通用因果推断框架，不限于 NLP。Director 采纳降级。但建议为 M-bias/front-door 各加 1-2 句 NLP 场景。\"\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 新发现的缺失引用\"\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [R2]\n        note: \"R2 提出 3 篇：(1) Imai, Keele & Tingley (2010) 因果中介分析——R1 AGREE；(2) Roberts/Pryzant et al. text-based causal inference——R1 AGREE；(3) Veitch, Wang & Blei (2020)——R1 REBUT，研究问题不同。Director：(1)(2) 建议引用，(3) 不强制。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-23T09:43:08.075718+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 30381}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-23T09:45:59.023011+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Multi-Class Annotation Errors in Causal Inference\n\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 13 (Fresh Review)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验验证; R2: 新颖性+完整性+表达）\n\n---\n\n## Summary\n\n本文系统分析了 K 类 LLM 标注错误在线性 SEM 下沿七种经典 DAG 拓扑（confounding, exposure, mediation, collider, M-bias, front-door, IV）传播至因果效应估计的机制。主要贡献包括：(1) 七种拓扑的闭式偏差表达式，证明 K≥3 引入结构性符号反转可能（二分类不会出现）；(2) Annotation Sensitivity Values (ASVs) 敏感性框架，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑脆弱性谱；(3) 五种校正方法的拓扑感知评估，证明 FWL 不变性使矩阵校正对四种协变量拓扑无效。经验验证覆盖 23 个 LLM 配置、3 个 NLP 数据集、161 个场景。\n\n## Strengths\n\n**S1. 七种 DAG 拓扑的统一分析框架具有真正的新颖性（R1-S1, R2-S1 共识）。** 先前工作要么覆盖单一拓扑（Brenner 1993 多类混杂；Lee & Wood-Doughty 2024 LLM+confounding），要么限于二元错分类（Teblunthuis 2024，四种 DAG）。本文首次跨七种拓扑进行统一分析，揭示了跨拓扑模式（符号保持层级、ASV 谱），这在单拓扑研究中不可见。\"first unified analysis across seven topologies\" 的声称经两位 Reviewer 独立确认有事实支撑。\n\n**S2. 诚实的三级理论层级体系（R1-S2）。** 将理论贡献明确区分为\"解析证明\"（Proposition 1: confounding/collider sign preservation, Theorem 1: K=2 monotonicity）、\"数值验证\"（Observation 1: 20,000 triples/topology）和\"ε-近似猜想\"（Conjecture 1），避免了过度宣称。这一透明度是方法论美德。\n\n**S3. K≥3 符号反转发现（R2-S2, R1-S6）。** 通过 Proposition 1(c) 的构造性反例和 100,000 Dirichlet 矩阵验证，清晰展示了多类误分类与二类误分类的本质差异。对使用多类 LLM 分类器的 NLP 因果推断实践者有直接相关性。\n\n**S4. FWL 不变性洞见（R1-S3）。** 证明矩阵校正方法对四种协变量拓扑无效是一个有实践价值的负面结果。R2 认为这是 FWL 定理的\"直接推论\"，R1 强力反驳：识别 FWL 在误分类校正语境下的含义需要结合列空间性质，并非 trivially obvious。Director 采纳 R1 观点——该洞见具有独立贡献价值。\n\n**S5. 实验验证规模充分且透明（R1-S4, R2-S3）。** 100,000 Dirichlet 矩阵 × 7 拓扑，MAPE 1.6%（161 scenarios）。跨 K 稳健性检验覆盖 K=3,5,7,10。Algorithm 1 和 ASV 框架提供可操作的实践指导（R1-S5, R2-S4）。\n\n**S6. 附录极为详尽（R2-S5）。** 22 页附录覆盖完整证明和 10+ 项鲁棒性检验，展现高度学术严谨性。\n\n## Weaknesses\n\n### Must-Fix\n\n**M1. [must-fix] EMNLP 受众的可达性障碍（R2-W1, R1 AGREE）。**\n论文大量使用计量经济学/流行病学术语而面向 NLP 读者的解释不足：\n- \"plim\" 从 Section 3.2 起贯穿全文，仅在 p4 脚注中一句话定义——这是改善但仍不充分（R12 已添加脚注，但 R13 两位 Reviewer 均认为需要更深入的直觉解释）\n- FWL 定理是贡献 3 的核心，但分解全在 Appendix A.2；正文首次出现时缺乏直觉解释\n- Equation (1) 的残差化概念对不熟悉 OLS 投影的读者不透明\n- Notation Table (Table 18, p30) 应更早交叉引用\n- **建议**：Section 3.1 开头加 1-2 段直觉性文字，解释 plim、FWL 分解、残差化的含义和动机；Table 18 前置或引用\n\nR1 建议降为 should-fix（认为是写作改进而非方法论问题）。Director 维持 must-fix：EMNLP 是 NLP 会议，读者可达性直接影响论文的 venue fit 和 impact。\n\n**M2. [must-fix] IV sign reversal 表述在论文内部存在 factual 不一致（R1-W3, R2 AGREE 并升级）。**\n三处关键表述相互矛盾：\n1. **Abstract (p1)**: \"no sign reversal occurs for all other topologies including IV\"\n2. **Section 4.2 (p7)**: \"diagonal dominance C₀ > 0.8 reduces but does not eliminate sign reversal risk\"\n3. **Appendix B.4 (p23)**: \"diagonal dominance prevents this crossing\"\n\n(2) 说 \"does not eliminate\"，(3) 说 \"prevents\"——直接矛盾。Abstract 与 Section 4.2 也矛盾。数值事实本身可能是一致的（真实 LLM 矩阵下 138 个非 exposure 场景中 0 次 sign reversal），但措辞必须统一。需明确区分 \"violation（偏差存在）\" 和 \"sign reversal（符号反转）\"，并定义 \"realistic accuracy\" 的操作边界。\n\n### Should-Fix\n\n**S1. [should-fix] Conjecture 1（K≥3 包络单调性）未被证明，Abstract 呈现不够突出（R1-W1, R2-W2 共识）。**\n核心拓扑排序在 K≥3 下依赖 Conjecture 1（ε < 0.06 近似单调性），仅有 210,000 矩阵的数值验证（Appendix B.12）。K=2 证明使用 perspective function 凸性，K≥3 因 V₀(δ) 从标量变为矩阵值函数而无法推广（Appendix A.4 已解释）。\n\nR2 评 must-fix，R1 REBUT：核心贡献是偏差表达式（Eq.1-2, 解析推导）和 sign preservation（Propositions 1-6, 一般 K 的解析证明），非 Conjecture 1。Director 采纳 R1——Conjecture 1 仅支撑 ASV monotonicity 排序，不构成论文核心理论基础。经验证据（Table 3, 161 scenarios）独立验证了拓扑排序。\n\n**建议**：(1) Abstract 明确区分 \"K=2 formal guarantees\" 和 \"K≥3 numerical evidence\"；(2) 降低 \"vulnerability spectrum\" 的声称强度为 \"approximate ranking supported by extensive numerical evidence\"。\n\n**S2. [should-fix] ASV 与 E-value/partial R² 的形式化比较不足（R2-W3, R1 AGREE）。**\nSection 3.3 的 ASV-vs-E-value 对比已有改善（R12 修复），但仍缺乏形式化深度：\n- Magnitude ASV 与 E-value 结构高度相似（均提供\"结论翻转所需最小扰动阈值\"），未展示数学差异\n- Sign-flip ASV \"has no E-value counterpart\" 未解释结构性原因（R1 补充：E-value 度量连续标量的混杂强度，Sign-flip ASV 度量离散矩阵到符号反转边界的距离——数学结构不同）\n- 与 Cinelli & Hazlett (2020) partial R² 框架无形式化对比\n- **建议**：添加对比表，形式化展示 ASV/E-value/robustness value 在参数空间、敏感性路径、适用场景上的异同\n\n**S3. [should-fix] Proportional effects 假设失败率（15-17%）在正文中讨论不足（R1-W2, R2 AGREE）。**\nAppendix B.17 Table 16 报告 proportional effects 在真实 LLM 矩阵下违反率 15-17%（Sparse DGP 高达 24.2%）。当 f≠λg 时，论文退回 Proposition 3（一般情形），其条件 |τ| > B 在实践中通常不可知。R2 补充建议：给出综合 \"coverage analysis\"——在多少比例的现实 LLM 配置中，至少有一组理论保证成立。\n- **建议**：正文中更直接地讨论失败率的实践含义和退化路径\n\n**S4. [should-fix] Section 4.5 FWL invariance 的适用范围限定不够精确（R1-W4 经 R2 修正后）。**\nR1 引用 Appendix B.14 Table 13 称 exposure 在 logistic 下有 22-78% 偏差缩减，暗示 FWL invariance 不成立。R2 正确指出：FWL invariance 仅 claim 协变量拓扑（confounding, mediation, collider, M-bias），exposure 不在 claim 范围内（A 是 treatment 而非 covariate）。Table 13 对协变量拓扑的 logistic bias reduction 均为 ~0.003%——确实 negligible。\n\n但正文 Section 4.5 的表述（\"FWL invariance holds under linear OLS and approximately under logistic regression\"）可能误导读者以为 FWL invariance 覆盖所有拓扑。\n- **建议**：明确添加 \"FWL invariance applies to covariate topologies only; exposure is excluded because A enters as treatment, not covariate\"\n\n### Minor\n\n**m1. [minor] Abstract 信息密度（R2-W4, R1 REBUT）。** R2 认为 7+ 个独立数字造成认知超载，R1 反驳精确定量是好的实践。分歧保留——属风格偏好。\n\n**m2. [minor] 部分拓扑缺少 NLP 场景示例（R2-W5, R1 部分 AGREE）。** M-bias、front-door、IV 未给出 NLP 应用实例。R1 指出这是通用因果推断框架，不限于 NLP。建议为 M-bias/front-door 各加 1-2 句 NLP 场景描述。\n\n**m3. [minor] 商业 LLM 验证缺失（R1-W5, R2 REBUT）。** R2 成功论证：理论结论仅依赖混淆矩阵数学性质（column-stochastic, diagonal dominance），不依赖 LLM 架构。23 个配置已覆盖 7B-235B 参数范围。Limitations 已承认此局限。\n\n**m4. [minor] Non-differential 假设讨论（R2-W7, R1 AGREE minor）。** Section 3.1 已识别成立条件和 stress test（Appendix B.6）。历轮改善显著。\n\n**m5. [minor] DAG 未知时的讨论（R2-W8, R1 AGREE minor）。** 标准因果推断假设，建议 1-2 句讨论应对策略即可。\n\n**m6. [minor] PPI++ 在 M-bias 下有害 (-88%) 缺乏机制解释（R2-Q4, R1 AGREE）。** 可能原因：M-bias 误分类是保护性的，PPI++ 移除保护性衰减，放大偏差。应在正文说明。\n\n**m7. [minor] Conjecture 1 高维覆盖不足（R1-W6, R2 部分 AGREE）。** K=7 每拓扑仅 10,000 样本，42 自由参数空间稀疏。建议增加采样量或做 power analysis。\n\n**m8. [minor] 各项 minor issues（R1-MI1-4, R2-MI1-6）。** Table 1 caption 说明不足、Footnote 1 计算基准不清晰、\"Numerical Verification 1/2\" 未正式定义、\"annotation error\" 与 \"misclassification\" 交替使用未声明同义、Figure 3 y 轴标签不精确。\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键判断上达成共识：\n\n1. **[AGREE] 七拓扑统一分析的新颖性成立**（R1-S1, R2-S1）。\n2. **[AGREE] 三级理论层级体系（proved/verified/conjectured）是透明的方法论美德**（R1-S2, R2 交叉确认）。\n3. **[AGREE] IV sign reversal 表述存在必须修复的 factual 不一致**（R1-W3, R2 升级为 must-fix）。\n4. **[AGREE] EMNLP 可达性需要改善**（R2-W1, R1 AGREE 实质但建议降级）。\n5. **[AGREE] ASV vs E-value 形式化对比不足**（R2-W3, R1 AGREE）。\n6. **[AGREE] Proportional effects 15-17% 失败率需更充分讨论**（R1-W2, R2 AGREE）。\n7. **[AGREE] K≥3 理论限制应在 Abstract 更突出呈现**（R1-W1, R2-W2）。\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 裁决 |\n|------|---------|---------|--------------|\n| Conjecture 1 严重性 | should-fix（偏差表达式才是核心） | must-fix（核心排序依赖猜想） | **R1**——核心贡献是 bias expressions + sign preservation，Conjecture 1 仅支撑 ASV monotonicity |\n| Abstract 信息密度 | REBUT（精确定量是好实践） | should-fix（认知超载） | **保留分歧**——属风格偏好 |\n| FWL 贡献定位 | REBUT（非平凡洞见） | should-fix（直接推论） | **R1**——识别 FWL 在误分类校正中的含义需结合列空间性质 |\n| 商业 LLM | should-fix | REBUT（理论不依赖架构） | **R2**——降为 minor |\n| Logistic regression + FWL | should-fix（exposure 结果远非 negligible） | REBUT（FWL 不 claim 覆盖 exposure） | **R2 纠正了逻辑错位**，但 R1 对 Section 4.5 措辞模糊的关切有效 → should-fix 限于措辞精确化 |\n\n## Questions\n\n**Q1.** IV sign reversal 三处表述（Abstract/Section 4.2/Appendix B.4）中哪个是正确的？\"realistic accuracy\" 的操作定义是什么？（R1-Q2, R2 AGREE — must address）\n\n**Q2.** Proportional effects 15-17% 失败率是否与特定模型类型或 K 值相关？失败时偏差的实际幅度是什么量级？（R1-Q1, R2 AGREE）\n\n**Q3.** M-bias 的 Sign-flip ASV = ∞ 是否可被解析证明？目前仅有数值验证。（R2-Q3, R1 AGREE — 加强论文的方向）\n\n**Q4.** Algorithm 1 的 δ* 阈值选择敏感性如何？不同阈值是否改变拓扑排序？（R1-Q4, R2 AGREE）\n\n**Q5.** Logistic 回归下 Algorithm 1 对 exposure 的推荐是否仍有效？（R1-Q3, R2 重新框定）\n\n**Q6.** PPI++ 在 M-bias 下 RMSE 增大 88% 的机制是什么？（R2-Q4, R1 AGREE）\n\n**Q7.** F1-bias null result (ρ=-0.10, p=0.45, n=56) 的统计功效？R1 部分 REBUT：Fig 3 的论点不是 ρ=0 而是\"F1 不是 reliable proxy\"，图的定性模式（同 F1 不同拓扑偏差差 10×）已足够支撑。但报告 CI 或 power 是合理改进。\n\n## Missing References\n\n**共识缺失（R2 提出, R1 AGREE）**:\n- Imai, Keele & Tingley (2010), \"A General Approach to Causal Mediation Analysis\" — mediation 分析基础框架\n- Roberts, Stewart & Tingley (2020) 或 Pryzant et al. (2021) — text-based causal inference\n\n**分歧**:\n- Veitch, Wang & Blei (2020) — R2 提出, R1 REBUT（研究问题不同：text-as-treatment/confounder vs. 标注误差传播）。Director 不强制引用。\n\nR1 未发现显著遗漏，认为文献覆盖在测量误差理论、LLM 标注、PPI、敏感性分析方面均较充分。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：错误。** 视觉审查 Agent 因限额问题退出（\"You've hit your limit · resets 4pm (UTC)\"）。未产生排版审查结果。用户可在限额重置后重新触发。\n\n**手动页面检查**（Director 基于 PDF 阅读）：\n- Section 5 (Conclusion) 在 page 8 内结束 ✓\n- Limitations 从 page 9 顶部开始，不计入页数 ✓\n- References 从 page 9 开始 ✓\n- 正文符合 EMNLP 2026 的 8 页限制 ✓\n- 匿名：作者署名为 \"Anonymous\" ✓\n- 模板：`\\usepackage[review]{acl}` ✓\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n\n**Confidence: High**（两位 Reviewer 独立评分一致，交叉分享后核心判断收敛）\n\n**官方维度打分综合：**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**总评**：论文在测量误差×因果推断的交叉领域做出了系统性贡献：七拓扑统一分析的新颖性经两位 Reviewer 确认成立；K≥3 符号反转发现有理论和实践价值；FWL 不变性洞见具有独立贡献（R1 成功论证其非平凡性）；实验验证规模充分。\n\n但存在两个 must-fix：(1) EMNLP 受众的术语可达性不足——plim/FWL 的直觉解释仍需深化；(2) IV sign reversal 在 Abstract/Section 4.2/Appendix B.4 之间的 factual 不一致必须修复。此外，ASV vs E-value 形式化对比不足、proportional effects 失败率正文讨论不充分、K≥3 理论限制在 Abstract 中呈现不够突出，均为 should-fix。\n\n论文处于主会议接收的边界线上。如修订能解决上述 must-fix 并改善 should-fix 项，可上调至 Conference (4.0)。当前版本更适合 Findings。\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 叙事结构清晰，三个贡献准确反映论文内容。\n- \"first unified analysis across seven topologies, building on prior single-topology analyses\" 的措辞准确有事实支撑（R1 交叉回应确认）。\n- 建议：明确区分 K=2 formal guarantees 和 K≥3 numerical evidence 的理论层级。\n\n### Section 2 (Related Work)\n- 覆盖面广泛（测量误差、LLM 标注、敏感性分析、校正方法），两位 Reviewer 均认为较充分。\n- 建议补充：Imai et al. (2010) 因果中介分析基础框架；1-2 篇 text-based causal inference 文献。\n\n### Section 3 (Method)\n- **3.1**: plim 脚注已添加（R12 修复），但需进一步加直觉段落（1-2 段解释 plim/FWL/残差化的含义和动机）。Table 18 应在此处交叉引用。\n- **3.2**: Bias expressions (Eq.1-2) 推导正确，R1 未发现错误。Exposure 的 w_{jk} 权重机制解释清晰（R1-S6）。但 Section 4.2 中 IV sign reversal 的措辞与 Appendix B.4 矛盾，必须修复。\n- **3.3**: ASV 框架定义清晰。Theorem 1 (K=2 monotonicity) 证明严谨。ASV-vs-E-value 对比已有改善（R12 添加），但需更深入的形式化展示。\n\n### Section 4 (Experiments)\n- **4.1-4.2**: Monte Carlo 验证设计合理，MAPE 1.6% 可接受。Table 1 和 Figure 2 有效支撑 bias taxonomy。IV sign reversal 表述需统一。\n- **4.3**: ASV 验证充分。Bootstrap CI 方法合理。\n- **4.4**: 经验验证覆盖 23 配置 × 3 数据集。Fig 3 (F1 vs bias) 有效支撑核心论点。建议补充 CI for ρ。\n- **4.5**: FWL invariance 措辞需精确限定为 covariate topologies only。K=3/5/10 校正方法对比是 R12 后的显著改善。PPI++ 对 M-bias 有害的机制需解释。\n\n### Section 5 (Conclusion)\n- 简洁准确，符合页面限制。\n\n### Limitations\n- 覆盖了主要限制（non-differential、线性 SEM、LLM 覆盖）。可进一步加 DAG 未知时的应对策略（1-2 句）。\n\n### Appendix\n- 极为详尽（22 页），完整证明和 10+ 鲁棒性检验。两位 Reviewer 均赞扬学术严谨性。\n",
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：Multi-Class Annotation Errors in Causal Inference\n\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 13 (Fresh Review)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验验证; R2: 新颖性+完整性+表达）\n\n---\n\n## Summary\n\n本文系统分析了 K 类 LLM 标注错误在线性 SEM 下沿七种经典 DAG 拓扑（confounding, exposure, mediation, collider, M-bias, front-door, IV）传播至因果效应估计的机制。主要贡献包括：(1) 七种拓扑的闭式偏差表达式，证明 K≥3 引入结构性符号反转可能（二分类不会出现）；(2) Annotation Sensitivity Values (ASVs) 敏感性框架，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑脆弱性谱；(3) 五种校正方法的拓扑感知评估，证明 FWL 不变性使矩阵校正对四种协变量拓扑无效。经验验证覆盖 23 个 LLM 配置、3 个 NLP 数据集、161 个场景。\n\n## Strengths\n\n**S1. 七种 DAG 拓扑的统一分析框架具有真正的新颖性（R1-S1, R2-S1 共识）。** 先前工作要么覆盖单一拓扑（Brenner 1993 多类混杂；Lee & Wood-Doughty 2024 LLM+confounding），要么限于二元错分类（Teblunthuis 2024，四种 DAG）。本文首次跨七种拓扑进行统一分析，揭示了跨拓扑模式（符号保持层级、ASV 谱），这在单拓扑研究中不可见。\"first unified analysis across seven topologies\" 的声称经两位 Reviewer 独立确认有事实支撑。\n\n**S2. 诚实的三级理论层级体系（R1-S2）。** 将理论贡献明确区分为\"解析证明\"（Proposition 1: confounding/collider sign preservation, Theorem 1: K=2 monotonicity）、\"数值验证\"（Observation 1: 20,000 triples/topology）和\"ε-近似猜想\"（Conjecture 1），避免了过度宣称。这一透明度是方法论美德。\n\n**S3. K≥3 符号反转发现（R2-S2, R1-S6）。** 通过 Proposition 1(c) 的构造性反例和 100,000 Dirichlet 矩阵验证，清晰展示了多类误分类与二类误分类的本质差异。对使用多类 LLM 分类器的 NLP 因果推断实践者有直接相关性。\n\n**S4. FWL 不变性洞见（R1-S3）。** 证明矩阵校正方法对四种协变量拓扑无效是一个有实践价值的负面结果。R2 认为这是 FWL 定理的\"直接推论\"，R1 强力反驳：识别 FWL 在误分类校正语境下的含义需要结合列空间性质，并非 trivially obvious。Director 采纳 R1 观点——该洞见具有独立贡献价值。\n\n**S5. 实验验证规模充分且透明（R1-S4, R2-S3）。** 100,000 Dirichlet 矩阵 × 7 拓扑，MAPE 1.6%（161 scenarios）。跨 K 稳健性检验覆盖 K=3,5,7,10。Algorithm 1 和 ASV 框架提供可操作的实践指导（R1-S5, R2-S4）。\n\n**S6. 附录极为详尽（R2-S5）。** 22 页附录覆盖完整证明和 10+ 项鲁棒性检验，展现高度学术严谨性。\n\n## Weaknesses\n\n### Must-Fix\n\n**M1. [must-fix] EMNLP 受众的可达性障碍（R2-W1, R1 AGREE）。**\n论文大量使用计量经济学/流行病学术语而面向 NLP 读者的解释不足：\n- \"plim\" 从 Section 3.2 起贯穿全文，仅在 p4 脚注中一句话定义——这是改善但仍不充分（R12 已添加脚注，但 R13 两位 Reviewer 均认为需要更深入的直觉解释）\n- FWL 定理是贡献 3 的核心，但分解全在 Appendix A.2；正文首次出现时缺乏直觉解释\n- Equation (1) 的残差化概念对不熟悉 OLS 投影的读者不透明\n- Notation Table (Table 18, p30) 应更早交叉引用\n- **建议**：Section 3.1 开头加 1-2 段直觉性文字，解释 plim、FWL 分解、残差化的含义和动机；Table 18 前置或引用\n\nR1 建议降为 should-fix（认为是写作改进而非方法论问题）。Director 维持 must-fix：EMNLP 是 NLP 会议，读者可达性直接影响论文的 venue fit 和 impact。\n\n**M2. [must-fix] IV sign reversal 表述在论文内部存在 factual 不一致（R1-W3, R2 AGREE 并升级）。**\n三处关键表述相互矛盾：\n1. **Abstract (p1)**: \"no sign reversal occurs for all other topologies including IV\"\n2. **Section 4.2 (p7)**: \"diagonal dominance C₀ > 0.8 reduces but does not eliminate sign reversal risk\"\n3. **Appendix B.4 (p23)**: \"diagonal dominance prevents this crossing\"\n\n(2) 说 \"does not eliminate\"，(3) 说 \"prevents\"——直接矛盾。Abstract 与 Section 4.2 也矛盾。数值事实本身可能是一致的（真实 LLM 矩阵下 138 个非 exposure 场景中 0 次 sign reversal），但措辞必须统一。需明确区分 \"violation（偏差存在）\" 和 \"sign reversal（符号反转）\"，并定义 \"realistic accuracy\" 的操作边界。\n\n### Should-Fix\n\n**S1. [should-fix] Conjecture 1（K≥3 包络单调性）未被证明，Abstract 呈现不够突出（R1-W1, R2-W2 共识）。**\n核心拓扑排序在 K≥3 下依赖 Conjecture 1（ε < 0.06 近似单调性），仅有 210,000 矩阵的数值验证（Appendix B.12）。K=2 证明使用 perspective function 凸性，K≥3 因 V₀(δ) 从标量变为矩阵值函数而无法推广（Appendix A.4 已解释）。\n\nR2 评 must-fix，R1 REBUT：核心贡献是偏差表达式（Eq.1-2, 解析推导）和 sign preservation（Propositions 1-6, 一般 K 的解析证明），非 Conjecture 1。Director 采纳 R1——Conjecture 1 仅支撑 ASV monotonicity 排序，不构成论文核心理论基础。经验证据（Table 3, 161 scenarios）独立验证了拓扑排序。\n\n**建议**：(1) Abstract 明确区分 \"K=2 formal guarantees\" 和 \"K≥3 numerical evidence\"；(2) 降低 \"vulnerability spectrum\" 的声称强度为 \"approximate ranking supported by extensive numerical evidence\"。\n\n**S2. [should-fix] ASV 与 E-value/partial R² 的形式化比较不足（R2-W3, R1 AGREE）。**\nSection 3.3 的 ASV-vs-E-value 对比已有改善（R12 修复），但仍缺乏形式化深度：\n- Magnitude ASV 与 E-value 结构高度相似（均提供\"结论翻转所需最小扰动阈值\"），未展示数学差异\n- Sign-flip ASV \"has no E-value counterpart\" 未解释结构性原因（R1 补充：E-value 度量连续标量的混杂强度，Sign-flip ASV 度量离散矩阵到符号反转边界的距离——数学结构不同）\n- 与 Cinelli & Hazlett (2020) partial R² 框架无形式化对比\n- **建议**：添加对比表，形式化展示 ASV/E-value/robustness value 在参数空间、敏感性路径、适用场景上的异同\n\n**S3. [should-fix] Proportional effects 假设失败率（15-17%）在正文中讨论不足（R1-W2, R2 AGREE）。**\nAppendix B.17 Table 16 报告 proportional effects 在真实 LLM 矩阵下违反率 15-17%（Sparse DGP 高达 24.2%）。当 f≠λg 时，论文退回 Proposition 3（一般情形），其条件 |τ| > B 在实践中通常不可知。R2 补充建议：给出综合 \"coverage analysis\"——在多少比例的现实 LLM 配置中，至少有一组理论保证成立。\n- **建议**：正文中更直接地讨论失败率的实践含义和退化路径\n\n**S4. [should-fix] Section 4.5 FWL invariance 的适用范围限定不够精确（R1-W4 经 R2 修正后）。**\nR1 引用 Appendix B.14 Table 13 称 exposure 在 logistic 下有 22-78% 偏差缩减，暗示 FWL invariance 不成立。R2 正确指出：FWL invariance 仅 claim 协变量拓扑（confounding, mediation, collider, M-bias），exposure 不在 claim 范围内（A 是 treatment 而非 covariate）。Table 13 对协变量拓扑的 logistic bias reduction 均为 ~0.003%——确实 negligible。\n\n但正文 Section 4.5 的表述（\"FWL invariance holds under linear OLS and approximately under logistic regression\"）可能误导读者以为 FWL invariance 覆盖所有拓扑。\n- **建议**：明确添加 \"FWL invariance applies to covariate topologies only; exposure is excluded because A enters as treatment, not covariate\"\n\n### Minor\n\n**m1. [minor] Abstract 信息密度（R2-W4, R1 REBUT）。** R2 认为 7+ 个独立数字造成认知超载，R1 反驳精确定量是好的实践。分歧保留——属风格偏好。\n\n**m2. [minor] 部分拓扑缺少 NLP 场景示例（R2-W5, R1 部分 AGREE）。** M-bias、front-door、IV 未给出 NLP 应用实例。R1 指出这是通用因果推断框架，不限于 NLP。建议为 M-bias/front-door 各加 1-2 句 NLP 场景描述。\n\n**m3. [minor] 商业 LLM 验证缺失（R1-W5, R2 REBUT）。** R2 成功论证：理论结论仅依赖混淆矩阵数学性质（column-stochastic, diagonal dominance），不依赖 LLM 架构。23 个配置已覆盖 7B-235B 参数范围。Limitations 已承认此局限。\n\n**m4. [minor] Non-differential 假设讨论（R2-W7, R1 AGREE minor）。** Section 3.1 已识别成立条件和 stress test（Appendix B.6）。历轮改善显著。\n\n**m5. [minor] DAG 未知时的讨论（R2-W8, R1 AGREE minor）。** 标准因果推断假设，建议 1-2 句讨论应对策略即可。\n\n**m6. [minor] PPI++ 在 M-bias 下有害 (-88%) 缺乏机制解释（R2-Q4, R1 AGREE）。** 可能原因：M-bias 误分类是保护性的，PPI++ 移除保护性衰减，放大偏差。应在正文说明。\n\n**m7. [minor] Conjecture 1 高维覆盖不足（R1-W6, R2 部分 AGREE）。** K=7 每拓扑仅 10,000 样本，42 自由参数空间稀疏。建议增加采样量或做 power analysis。\n\n**m8. [minor] 各项 minor issues（R1-MI1-4, R2-MI1-6）。** Table 1 caption 说明不足、Footnote 1 计算基准不清晰、\"Numerical Verification 1/2\" 未正式定义、\"annotation error\" 与 \"misclassification\" 交替使用未声明同义、Figure 3 y 轴标签不精确。\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键判断上达成共识：\n\n1. **[AGREE] 七拓扑统一分析的新颖性成立**（R1-S1, R2-S1）。\n2. **[AGREE] 三级理论层级体系（proved/verified/conjectured）是透明的方法论美德**（R1-S2, R2 交叉确认）。\n3. **[AGREE] IV sign reversal 表述存在必须修复的 factual 不一致**（R1-W3, R2 升级为 must-fix）。\n4. **[AGREE] EMNLP 可达性需要改善**（R2-W1, R1 AGREE 实质但建议降级）。\n5. **[AGREE] ASV vs E-value 形式化对比不足**（R2-W3, R1 AGREE）。\n6. **[AGREE] Proportional effects 15-17% 失败率需更充分讨论**（R1-W2, R2 AGREE）。\n7. **[AGREE] K≥3 理论限制应在 Abstract 更突出呈现**（R1-W1, R2-W2）。\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 裁决 |\n|------|---------|---------|--------------|\n| Conjecture 1 严重性 | should-fix（偏差表达式才是核心） | must-fix（核心排序依赖猜想） | **R1**——核心贡献是 bias expressions + sign preservation，Conjecture 1 仅支撑 ASV monotonicity |\n| Abstract 信息密度 | REBUT（精确定量是好实践） | should-fix（认知超载） | **保留分歧**——属风格偏好 |\n| FWL 贡献定位 | REBUT（非平凡洞见） | should-fix（直接推论） | **R1**——识别 FWL 在误分类校正中的含义需结合列空间性质 |\n| 商业 LLM | should-fix | REBUT（理论不依赖架构） | **R2**——降为 minor |\n| Logistic regression + FWL | should-fix（exposure 结果远非 negligible） | REBUT（FWL 不 claim 覆盖 exposure） | **R2 纠正了逻辑错位**，但 R1 对 Section 4.5 措辞模糊的关切有效 → should-fix 限于措辞精确化 |\n\n## Questions\n\n**Q1.** IV sign reversal 三处表述（Abstract/Section 4.2/Appendix B.4）中哪个是正确的？\"realistic accuracy\" 的操作定义是什么？（R1-Q2, R2 AGREE — must address）\n\n**Q2.** Proportional effects 15-17% 失败率是否与特定模型类型或 K 值相关？失败时偏差的实际幅度是什么量级？（R1-Q1, R2 AGREE）\n\n**Q3.** M-bias 的 Sign-flip ASV = ∞ 是否可被解析证明？目前仅有数值验证。（R2-Q3, R1 AGREE — 加强论文的方向）\n\n**Q4.** Algorithm 1 的 δ* 阈值选择敏感性如何？不同阈值是否改变拓扑排序？（R1-Q4, R2 AGREE）\n\n**Q5.** Logistic 回归下 Algorithm 1 对 exposure 的推荐是否仍有效？（R1-Q3, R2 重新框定）\n\n**Q6.** PPI++ 在 M-bias 下 RMSE 增大 88% 的机制是什么？（R2-Q4, R1 AGREE）\n\n**Q7.** F1-bias null result (ρ=-0.10, p=0.45, n=56) 的统计功效？R1 部分 REBUT：Fig 3 的论点不是 ρ=0 而是\"F1 不是 reliable proxy\"，图的定性模式（同 F1 不同拓扑偏差差 10×）已足够支撑。但报告 CI 或 power 是合理改进。\n\n## Missing References\n\n**共识缺失（R2 提出, R1 AGREE）**:\n- Imai, Keele & Tingley (2010), \"A General Approach to Causal Mediation Analysis\" — mediation 分析基础框架\n- Roberts, Stewart & Tingley (2020) 或 Pryzant et al. (2021) — text-based causal inference\n\n**分歧**:\n- Veitch, Wang & Blei (2020) — R2 提出, R1 REBUT（研究问题不同：text-as-treatment/confounder vs. 标注误差传播）。Director 不强制引用。\n\nR1 未发现显著遗漏，认为文献覆盖在测量误差理论、LLM 标注、PPI、敏感性分析方面均较充分。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：错误。** 视觉审查 Agent 因限额问题退出（\"You've hit your limit · resets 4pm (UTC)\"）。未产生排版审查结果。用户可在限额重置后重新触发。\n\n**手动页面检查**（Director 基于 PDF 阅读）：\n- Section 5 (Conclusion) 在 page 8 内结束 ✓\n- Limitations 从 page 9 顶部开始，不计入页数 ✓\n- References 从 page 9 开始 ✓\n- 正文符合 EMNLP 2026 的 8 页限制 ✓\n- 匿名：作者署名为 \"Anonymous\" ✓\n- 模板：`\\usepackage[review]{acl}` ✓\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n\n**Confidence: High**（两位 Reviewer 独立评分一致，交叉分享后核心判断收敛）\n\n**官方维度打分综合：**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**总评**：论文在测量误差×因果推断的交叉领域做出了系统性贡献：七拓扑统一分析的新颖性经两位 Reviewer 确认成立；K≥3 符号反转发现有理论和实践价值；FWL 不变性洞见具有独立贡献（R1 成功论证其非平凡性）；实验验证规模充分。\n\n但存在两个 must-fix：(1) EMNLP 受众的术语可达性不足——plim/FWL 的直觉解释仍需深化；(2) IV sign reversal 在 Abstract/Section 4.2/Appendix B.4 之间的 factual 不一致必须修复。此外，ASV vs E-value 形式化对比不足、proportional effects 失败率正文讨论不充分、K≥3 理论限制在 Abstract 中呈现不够突出，均为 should-fix。\n\n论文处于主会议接收的边界线上。如修订能解决上述 must-fix 并改善 should-fix 项，可上调至 Conference (4.0)。当前版本更适合 Findings。\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 叙事结构清晰，三个贡献准确反映论文内容。\n- \"first unified analysis across seven topologies, building on prior single-topology analyses\" 的措辞准确有事实支撑（R1 交叉回应确认）。\n- 建议：明确区分 K=2 formal guarantees 和 K≥3 numerical evidence 的理论层级。\n\n### Section 2 (Related Work)\n- 覆盖面广泛（测量误差、LLM 标注、敏感性分析、校正方法），两位 Reviewer 均认为较充分。\n- 建议补充：Imai et al. (2010) 因果中介分析基础框架；1-2 篇 text-based causal inference 文献。\n\n### Section 3 (Method)\n- **3.1**: plim 脚注已添加（R12 修复），但需进一步加直觉段落（1-2 段解释 plim/FWL/残差化的含义和动机）。Table 18 应在此处交叉引用。\n- **3.2**: Bias expressions (Eq.1-2) 推导正确，R1 未发现错误。Exposure 的 w_{jk} 权重机制解释清晰（R1-S6）。但 Section 4.2 中 IV sign reversal 的措辞与 Appendix B.4 矛盾，必须修复。\n- **3.3**: ASV 框架定义清晰。Theorem 1 (K=2 monotonicity) 证明严谨。ASV-vs-E-value 对比已有改善（R12 添加），但需更深入的形式化展示。\n\n### Section 4 (Experiments)\n- **4.1-4.2**: Monte Carlo 验证设计合理，MAPE 1.6% 可接受。Table 1 和 Figure 2 有效支撑 bias taxonomy。IV sign reversal 表述需统一。\n- **4.3**: ASV 验证充分。Bootstrap CI 方法合理。\n- **4.4**: 经验验证覆盖 23 配置 × 3 数据集。Fig 3 (F1 vs bias) 有效支撑核心论点。建议补充 CI for ρ。\n- **4.5**: FWL invariance 措辞需精确限定为 covariate topologies only。K=3/5/10 校正方法对比是 R12 后的显著改善。PPI++ 对 M-bias 有害的机制需解释。\n\n### Section 5 (Conclusion)\n- 简洁准确，符合页面限制。\n\n### Limitations\n- 覆盖了主要限制（non-differential、线性 SEM、LLM 覆盖）。可进一步加 DAG 未知时的应对策略（1-2 句）。\n\n### Appendix\n- 极为详尽（22 页），完整证明和 10+ 鲁棒性检验。两位 Reviewer 均赞扬学术严谨性。\n",
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-23T09:46:03.241319+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4218
}
```

</details>

---


### Assistant

_source line 1066 · 2026-05-23T09:46:17.242430+00:00_

审稿报告已投递至 Research Director。

**Round 13 审稿总结**：

- **Overall: 3.5 (Borderline Conference)**
- R1 和 R2 独立评分一致，交叉分享后核心判断收敛

**2 个 Must-Fix**：
1. EMNLP 受众可达性——plim/FWL 术语直觉解释仍不充分
2. IV sign reversal 表述在 Abstract/Section 4.2/Appendix B.4 之间存在 factual 不一致

**4 个 Should-Fix**：
1. K≥3 理论限制在 Abstract 中呈现不够突出
2. ASV vs E-value 形式化对比不足
3. Proportional effects 15-17% 失败率正文讨论不充分
4. Section 4.5 FWL invariance 适用范围需精确限定为 covariate topologies

**关键分歧裁决**：
- Conjecture 1 严重性：采纳 R1（should-fix，核心贡献是 bias expressions 非 Conjecture）
- FWL 贡献定位：采纳 R1（非平凡洞见，不是 weakness）
- 商业 LLM：采纳 R2（降为 minor，理论不依赖 LLM 架构）

Issue Tracker 已同步更新（新增 R13-W1/W2/MR1，更新 15 个历史 issue 的 R13 mentions）。视觉审查因限额错误未完成，外部审稿未请求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 106

## Round 106

2 recorded events


### User

_source line 1067 · 2026-05-23T09:46:19.904761+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部 Weaknesses (W1-W8) 和 Questions (Q1-Q5) 的逐条回应。

核心判断摘要：
- **4 条 REBUT**：W2（Conjecture 1 不应 must-fix）、W4（Abstract 信息密度合理）、W6（FWL 不变性是有意义的贡献）、MR4/MR1（引用已覆盖或不直接相关）
- **8 条 AGREE**（含部分同意）：W1（可达性，降为 should-fix）、W3（ASV 对比）、W5（NLP 场景，降为 minor）、W7-W8（minor 合理）、Q1-Q4
- **1 条部分 REBUT**：Q5（power analysis 有用但 Fig 3 论点不依赖于它）

两位 Reviewer 的 Overall 评分一致：**3.5 (Borderline Conference)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1068 · 2026-05-23T09:46:35.014631+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿完成总结：**

- **Overall: 3.5 (Borderline Conference)**
- **Soundness: 3.5 | Excitement: 3.25 | Reproducibility: 4.0**
- 2 名 Reviewer 独立评分一致（均 3.5），交叉分享后核心判断收敛

**Must-Fix (2)**:
1. EMNLP 受众可达性——plim/FWL 等术语需更深入的直觉解释
2. IV sign reversal 在 Abstract/Section 4.2/Appendix B.4 之间存在 factual 不一致

**Should-Fix (4)**:
1. K≥3 理论限制在 Abstract 中呈现不够突出（Conjecture 1 vs Theorem 1）
2. ASV vs E-value/partial R² 形式化对比不足
3. Proportional effects 15-17% 失败率正文讨论不充分
4. Section 4.5 FWL invariance 适用范围需精确限定为 covariate topologies

**Minor (8)**:
Abstract 信息密度（分歧保留）、NLP 场景示例、商业 LLM、non-differential 假设、DAG 未知讨论、PPI++ M-bias 机制、Conjecture 1 高维覆盖、各项格式细节

Issue Tracker 已同步更新（`review_issues.yaml`）。视觉审查因限额未完成，限额重置后可重新触发。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 107

## Round 107

64 recorded events


### User

_source line 1069 · 2026-05-23T10:31:36.715641+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-23T10:31:42.217329+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-23T10:31:42.268554+00:00_

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
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-23T10:31:49.703422+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-23T10:31:49.703760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-23T10:31:52.063516+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-23T10:31:52.164276+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-23T10:31:55.225964+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-23T10:31:55.276656+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1078 · 2026-05-23T10:31:58.038337+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1079 · 2026-05-23T10:31:58.139291+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-23T10:32:02.809111+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-23T10:32:06.370454+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 3561
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-23T10:32:06.471375+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1083 · 2026-05-23T10:32:06.622350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1084 · 2026-05-23T10:32:06.622806+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	
20	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
24	\graphicspath{{../../figures/paper/}}
25	
26	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	
35	\input{introduction}
36	
37	\begin{figure*}[t]
38	\centering
39	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
40	\vspace{-6pt}
41	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
42	\label{fig:dag_taxonomy}
43	\end{figure*}
44	
45	\input{related_work}
46	
47	\input{method}
48	
49	% ── Figures ──
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
54	\vspace{-6pt}
55	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
56	\label{fig:bias_distribution}
57	\end{figure*}
58	
59	\input{experiments}
60	
61	\input{conclusion}
62	
63	\bibliography{references}
64	
65	\appendix
66	\input{appendix_proofs}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1085 · 2026-05-23T10:32:06.824547+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1086 · 2026-05-23T10:32:07.025792+00:00_

-rw-r--r-- 1 ubuntu ubuntu 37500 May 23 10:30 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-23T10:32:16.913781+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found relevant information from ACL
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 10442
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-23T10:32:22.134557+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 1089 · 2026-05-23T10:32:22.636754+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers Budapest submission deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers Budapest submission deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-23T10:32:24.294367+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-23T10:32:24.646280+00:00_

-rw-r--r-- 1 ubuntu ubuntu 919983 May 23 10:21 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-23T10:32:24.797367+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-23T10:32:24.848008+00:00_

1	issues:
2	  # === Round 1-7 历史 (resolved，保留摘要) ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 7
11	    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
12	    resolution_round: 7
13	
14	  - id: R1-N2
15	    category: soundness
16	    severity: should-fix
17	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
18	    status: resolved
19	    first_raised_round: 1
20	    last_seen_round: 3
21	    resolution: "Abstract 已准确区分 prove/verify。"
22	    resolution_round: 4
23	
24	  - id: R1-N3
25	    category: soundness
26	    severity: must-fix
27	    summary: "ASV C(δ) 定义域错误"
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 1
31	    resolution: "Section 3.3 已引入 δ_max 约束。"
32	    resolution_round: 2
33	
34	  - id: R2-N1
35	    category: presentation
36	    severity: must-fix
37	    summary: "83.4% sign reversal headline framing 过度声称"
38	    status: resolved
39	    first_raised_round: 1
40	    last_seen_round: 5
41	    resolution: "Introduction 已重写。"
42	    resolution_round: 5
43	
44	  - id: R2-N2
45	    category: novelty
46	    severity: should-fix
47	    summary: "'first systematic framework' 过度声明"
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1
51	    resolution: "已修复。"
52	    resolution_round: 2
53	
54	  - id: R2-N3
55	    category: related_work
56	    severity: must-fix
57	    summary: "4 篇关键相关工作未引用"
58	    status: resolved
59	    first_raised_round: 1
60	    last_seen_round: 1
61	    resolution: "已修复。"
62	    resolution_round: 2
63	
64	  - id: R1-W2
65	    category: clarity
66	    severity: should-fix
67	    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
68	    status: resolved
69	    first_raised_round: 1
70	    last_seen_round: 2
71	    resolution: "Section 3.2 已添加 ASV 替代讨论。"
72	    resolution_
…[truncated 939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1094 · 2026-05-23T10:32:28.664320+00:00_

Web search results for query: "EMNLP 2026 call for papers Budapest submission deadline commitment"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the search results, here's the information about EMNLP 2026:

## Conference Location and Dates
EMNLP 2026 will be held in Budapest, Hungary, October 24 - 29, 2026.

## Main Conference Paper Submission Deadline
The EMNLP 2026 paper submission deadline is May 25, 2026 at 23:59:59 (UTC-12).

## Commitment Process
Papers that have received reviews and a meta-review from ARR (whether fro
…[truncated 652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6027
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-23T10:32:30.324244+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results from aclrollingreview.org, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unl
…[truncated 1209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 8189
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-23T10:32:35.999145+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-23T10:32:36.502246+00:00_

100	    resolution: ""
101	    resolution_round: null
102	
103	  - id: R2-W2
104	    category: presentation
105	    severity: should-fix
106	    summary: "98 场景 zero sign reversals 与 sign reversal narrative 的 tension"
107	    status: resolved
108	    first_raised_round: 1
109	    last_seen_round: 1
110	    resolution: "已解决。"
111	    resolution_round: 2
112	
113	  - id: R2-W3
114	    category: method
115	    severity: should-fix
116	    summary: "ASV 对 C₀ 估计不确定性的敏感性"
117	    status: resolved
118	    first_raised_round: 1
119	    last_seen_round: 2
120	    resolution: "Bootstrap ASV 分析已完成。"
121	    resolution_round: 3
122	
123	  - id: R2-W4
124	    category: scope
125	    severity: should-fix
126	    summary: "线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat"
127	    status: resolved
128	    first_raised_round: 1
129	    last_seen_round: 5
130	    resolution: "Section 4.5 FWL 段加 'Under linear OLS' 限定。"
131	    resolution_round: 5
132	
133	  - id: R1-W4
134	    category: experiments
135	    severity: should-fix
136	    summary: "MC MAPE 报告不充分"
137	    status: resolved
138	    first_raised_round: 1
139	    last_seen_round: 1
140	    resolution: "已修复。"
141	    resolution_round: 2
142	
143	  - id: MISC-1
144	    category: presentation
145	    severity: minor
146	    summary: "符号不统一（τ vs β_T）、Proposition 编号不一致"
147	    status: resolved
148	    first_raised_round: 1
149	    last_seen_round: 5
150	    resolution: "method.tex 添加 τ 在各拓扑下含义的明确说明。"
151	    resolution_round: 5
152	
153	  - id: NEW-1
154	    category: soundness
155	    severity: should-fix
156	    summary: "Non-differential misclassification 假设讨论不足"
157	    status: in_progress
158	    first_raised_round: 2
159	    last_seen_round: 13
160	    mentions:
161	      - round: 5
162	        reviewers: []
163	        note: "method.tex 添加完整的讨论。"
164	      - round: 8
165	        reviewers: [R1, R2]
166	        note: "R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。"
167	      - round: 9
168	        reviewers: [R1, R2]
169	        no
…[truncated 3942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-23T10:32:36.502824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1099 · 2026-05-23T10:32:36.954925+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy, sign reversal occurs in 2.1\% of exposure configurations, exclusively in secondary coefficients with small effect sizes; across all 23 empirical LLM configurations (mean diagonal 0.45--0.81), sign reversal is confined exclusively to exposure, though IV reaches 52.6\% under uniform Dirichlet priors. We introduce Annotation Sensitivity Values (ASVs), with proved monotonicity ($K{=}2$; Theorem~1) and approximate monotonicity supported by 210{,}000-matrix numerical evidence ($K{\geq}3$; Conjecture~1), yielding an approximate vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1100 · 2026-05-23T10:32:37.005595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-23T10:32:37.056286+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors (equivalently, misclassification) from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, h
…[truncated 2908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-23T10:32:41.675816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "offset": "298",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "offset": "298",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-23T10:32:42.228532+00:00_

298	  - id: R4-W3
299	    category: soundness
300	    severity: should-fix
301	    summary: "Eq.(3) 中 λ(C) ∈ [0,1] 未证明"
302	    status: resolved
303	    first_raised_round: 4
304	    last_seen_round: 4
305	    resolution: "Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。"
306	    resolution_round: 5
307	
308	  - id: R4-W4
309	    category: presentation
310	    severity: should-fix
311	    summary: "'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次"
312	    status: resolved
313	    first_raised_round: 4
314	    last_seen_round: 5
315	    resolution: "论文已建立三级层次。"
316	    resolution_round: 5
317	
318	  - id: R4-W6
319	    category: novelty
320	    severity: should-fix
321	    summary: "ASV 方法论创新有限——E-value 直接移植质疑"
322	    status: in_progress
323	    first_raised_round: 4
324	    last_seen_round: 13
325	    mentions:
326	      - round: 7
327	        reviewers: [R1, R2]
328	        note: "共识：聚焦 monotonicity 非平凡性。"
329	      - round: 8
330	        reviewers: [R1, R2]
331	        note: "已调整 framework→diagnostics + K²→1D 降维。"
332	      - round: 11
333	        reviewers: [R1, R2]
334	        note: "R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT。"
335	      - round: 12
336	        reviewers: [R1, R2]
337	        note: "R12 共识：sign-flip ASV 和 N* 是新贡献，但 magnitude ASV 与 E-value 同构度高。"
338	      - round: 13
339	        reviewers: [R1, R2]
340	        note: "R13 R2-W3 再次提出：形式化对比不充分，需表格对比 ASV/E-value/partial R²。R1 AGREE 并补充应阐明 Sign-flip ASV 无法被 E-value 自然扩展的结构性原因。共识 should-fix。"
341	    action_items:
342	      - round: 13
343	        action: "Appendix 新增 ASV vs E-value/Partial R² 对比表（含 Topology dependence 行）"
344	        assigned_to: agent
345	        status: in_progress
346	    resolution: ""
347	    resolution_round: null
348	
349	  - id: R4-W7
350	    category: presentation
351	    severity: should-fix
352	    summary: "论文广度有余深度不足"
353	    status: resolved
354	    first_raised_round: 4
355	    last_seen_round: 7
356	    resolution: "Appendix pointer 已添加，R8
…[truncated 4349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-23T10:32:42.429730+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-23T10:32:42.430353+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes systematic bias---the value an estimator converges to as $N \to \infty$ (the probability limit, or plim)---rather than finite-sample variance. The Frisch--Waugh--Lovell (FWL) theorem guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables; this is why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}): replacing the mismeasured variable with a corrected version does not change the residualized relationship. Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}) collects all notation.
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	This holds in standard annotation pipelines where the LLM receives only source text and classifies without observing the outcome or covariates---the typical setup in computational social science~\cite{ziems2024can}. Empirical verification using topic-stratified confusion matrices confirms cross-group stability (Appendix~\ref{sec:nondiff_verify}). Violations
…[truncated 13202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-23T10:32:46.696246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-23T10:32:47.098305+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.3\% (confounding) to 3.7\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient. The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C
…[truncated 6951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-23T10:32:47.098740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-23T10:32:47.651218+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{imai_keele_tingley2010, valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayy
…[truncated 2268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-23T10:32:47.651726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-23T10:32:48.555346+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: the binary attenuation guarantee breaks at $K \geq 3$, where exposure and IV can reverse signs while five topologies preserve them. ASVs yield a vulnerability ranking from IV (most fragile) to M-bias (immune); matrix-based corrections are provably ineffective for four covariate topologies due to FWL invariance. Code and data will be released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information; a stress test (Appendix~\ref{sec:nondiff_stress}) shows that structured violation patterns can exceed or fall below uniform predictions. Closed-form expressions are derived under $K{=}3$ linear structural equations; extensions to arbitrary $K$ and nonlinear models~\cite{schennach2020mismeasured} remain open (Appendix~\ref{sec:logistic_dgp}), though correction method rankings are stable across $K{=}3,5,10$ (Spearman $\rho \geq 0.80$, with PPI++ degrading at $K{=}10$; Appendix~\ref{sec:correction_k_sensitivity}). The ASV diagonal parameterization $C(\delta) = (1{-}\delta)I + \delta C_0$ assumes uniform degradation across categories; rare-class-specific degradation would require multi-dimensional extensions. When the true DAG is uncertain, practitioners can apply Algorithm~1 under each candidate topology and report the range of conclusions as a form of specification sensitivity analysis. FWL invariance holds under linear OLS and approximately under logistic regression; applicability to non-parametric methods (doubly robust estimators, TMLE) remains unverified. Our 23 configurations span four open-weight LLMs (7B--235B) with diagonal accuracy 0.45--0.81; commercial models and ordinal tasks remain untested.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-23T10:32:48.706368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "offset": "496",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "offset": "496",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-23T10:32:48.757501+00:00_

496	    status: resolved
497	    first_raised_round: 6
498	    last_seen_round: 7
499	    resolution: "Abstract 和 Section 4.2 现均使用 2.1%。"
500	    resolution_round: 7
501	
502	  - id: R6-W1
503	    category: scope
504	    severity: should-fix
505	    summary: "线性模型假设与 NLP 实践的 scope mismatch"
506	    status: resolved
507	    first_raised_round: 6
508	    last_seen_round: 7
509	    resolution: "EXP-2 FWL N-scaling 完成。R8 未再提及。"
510	    resolution_round: 9
511	
512	  - id: R6-W2
513	    category: novelty
514	    severity: should-fix
515	    summary: "ASV 与 E-value 的方法论创新边界不清晰"
516	    status: in_progress
517	    first_raised_round: 6
518	    last_seen_round: 13
519	    mentions:
520	      - round: 8
521	        reviewers: [R1, R2]
522	        note: "已调整措辞。"
523	      - round: 11
524	        reviewers: [R1, R2]
525	        note: "与 R4-W6 合并。"
526	      - round: 12
527	        reviewers: [R1, R2]
528	        note: "R12 共识：sign-flip ASV 和 N* 是新贡献。"
529	      - round: 13
530	        reviewers: [R1, R2]
531	        note: "R13 与 R4-W6 合并。R2-W3 + R1 AGREE：需形式化对比表。"
532	    resolution: ""
533	    resolution_round: null
534	
535	  - id: R6-W3
536	    category: related_work
537	    severity: minor
538	    summary: "缺失引用"
539	    status: resolved
540	    first_raised_round: 6
541	    last_seen_round: 7
542	    resolution: "全部已引用。"
543	    resolution_round: 7
544	
545	  - id: R6-W4
546	    category: soundness
547	    severity: minor
548	    summary: "Conjecture 1 与 Theorem 1 覆盖范围关系"
549	    status: resolved
550	    first_raised_round: 6
551	    last_seen_round: 11
552	    resolution: "三级证据层次被 R11 两位 Reviewer 赞为方法论美德。"
553	    resolution_round: 11
554	
555	  - id: R6-W5
556	    category: experiments
557	    severity: should-fix
558	    summary: "Non-differential stress test 覆盖不足"
559	    status: resolved
560	    first_raised_round: 6
561	    last_seen_round: 7
562	    resolution: "Stress test 已覆盖 ε up to 0.50。"
563	    resolution_round: 8
564	
565	  - id: R6-D1
566	    category: pres
…[truncated 7042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-23T10:32:53.475375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "offset": "795",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "offset": "795",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-23T10:32:53.930658+00:00_

795	    status: resolved
796	    first_raised_round: 8
797	    last_seen_round: 11
798	    resolution: "已引用 ding_vanderweele2016。"
799	    resolution_round: 11
800	
801	  # === Round 9 ===
802	
803	  - id: R9-C1
804	    category: soundness
805	    severity: should-fix
806	    summary: "核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证"
807	    status: in_progress
808	    first_raised_round: 9
809	    last_seen_round: 13
810	    mentions:
811	      - round: 9
812	        reviewers: [R1, R2]
813	        note: "延续 R8-C2。"
814	      - round: 11
815	        reviewers: [R1, R2]
816	        note: "共识降级。"
817	      - round: 12
818	        reviewers: [R1, R2]
819	        note: "R12 合并到 NEW-1 和 R8-C2 讨论。"
820	      - round: 13
821	        reviewers: [R1, R2]
822	        note: "R13 合并到 R6-M3 和 NEW-1。R2 建议综合 coverage analysis。"
823	
824	  - id: R9-C2
825	    category: scope
826	    severity: should-fix
827	    summary: "线性 SEM 假设对 EMNLP 读者可达性和泛化性不足"
828	    status: in_progress
829	    first_raised_round: 9
830	    last_seen_round: 13
831	    mentions:
832	      - round: 9
833	        reviewers: [R1, R2]
834	        note: "需 Section 3.1 加线性 SEM 动机。"
835	      - round: 11
836	        reviewers: [R1, R2]
837	        note: "主文整合 logistic 结果不足。"
838	      - round: 12
839	        reviewers: [R1, R2]
840	        note: "R12 共识：Appendix B.6/B.13 logistic 验证充分但正文引用不足。已添加。"
841	      - round: 13
842	        reviewers: [R1, R2]
843	        note: "R13 R1-W4 + R2-W1 再次提出。plim 脚注和 FWL 内联定义已添加（R12 修复），但 R2 认为仍不充分——需 Section 3.1 开头加 1-2 段直觉性文字。R1 同意但建议降为 should-fix。FWL invariance 在 logistic 下对 exposure 不成立的措辞需精确化。"
844	    action_items:
845	      - round: 9
846	        action: "Section 3.1 加线性 SEM 动机句"
847	        assigned_to: agent
848	        status: in_progress
849	      - round: 12
850	        action: "Section 4.5 增加 logistic DGP 总结 + 引用 Appendix B.13"
851	        assigned_to: agent
852	        status: done
853	      - round: 12
854	        action: "Section 3.1/3.2 增加 plim 和 FWL 直
…[truncated 7582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-23T10:32:54.131839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-23T10:32:54.182534+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 3331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-23T10:32:59.953020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "offset": "1093",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "offset": "1093",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-23T10:33:00.003863+00:00_

1093	      - round: 13
1094	        reviewers: []
1095	        note: "R13 未单独提出。"
1096	
1097	  # === Round 13 新发现 ===
1098	
1099	  - id: R13-W1
1100	    category: soundness
1101	    severity: must-fix
1102	    summary: "IV sign reversal 表述在 Abstract、Section 4.2、Appendix B.4 之间存在 factual 不一致"
1103	    status: resolved
1104	    first_raised_round: 13
1105	    last_seen_round: 13
1106	    mentions:
1107	      - round: 13
1108	        reviewers: [R1, R2]
1109	        note: "R1-W3 首先发现。Abstract 说 'no sign reversal for IV'，Section 4.2 说 'does not eliminate sign reversal risk'，Appendix B.4 说 'diagonal dominance prevents this crossing'。三处相互矛盾。R2 交叉回应 AGREE 并升级为 must-fix。共识：必须统一措辞，明确区分 violation（偏差存在）和 sign reversal（符号反转），并定义 'realistic' 的操作边界。"
1110	    action_items:
1111	      - round: 13
1112	        action: "统一 Abstract/Section 4.2/Appendix B.4 关于 IV sign reversal 的措辞"
1113	        assigned_to: agent
1114	        status: done
1115	    resolution: "三处统一：Abstract用empirical configs限定，Section 4.2用mean diagonal as low as 0.45限定，Appendix B.4用near-zero under empirical conditions。Reviewer PASS。"
1116	    resolution_round: 14
1117	
1118	  - id: R13-W2
1119	    category: presentation
1120	    severity: minor
1121	    summary: "部分拓扑（M-bias, front-door, IV）缺少 NLP 应用场景示例"
1122	    status: in_progress
1123	    first_raised_round: 13
1124	    last_seen_round: 13
1125	    mentions:
1126	      - round: 13
1127	        reviewers: [R2]
1128	        note: "R2-W5 提出。R1 部分 AGREE 但建议降为 minor——论文贡献是通用因果推断框架，不限于 NLP。Director 采纳降级。但建议为 M-bias/front-door 各加 1-2 句 NLP 场景。"
1129	
1130	  - id: R13-MR1
1131	    category: related_work
1132	    severity: minor
1133	    summary: "R13 新发现的缺失引用"
1134	    status: in_progress
1135	    first_raised_round: 13
1136	    last_seen_round: 13
1137	    mentions:
1138	      - round: 13
1139	        reviewers: [R2]
1140	        note: "R2 提出 3 篇：(1) Imai, Keele & Tingley (2010) 因果中介分析——R1 AGREE；(2) Roberts/Pryzant et al. text-based causal inference——R1 AGREE；(3) Veitch
…[truncated 1030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-23T10:33:27.129262+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "ROADMAP.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "ROADMAP.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-23T10:33:28.495389+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ROADMAP.md\", \"content\": \"# causal_annot_error_attrib — Research Dashboard\\n\\n> 最后更新: 2026-05-22 19:12 UTC | 更新原因: 清理阻塞项（plan003搁置、Re-dream跳过、GPU释放通知），聚焦 Round 7 审稿\\n\\n> 详见 paper_framing.md（story/claims）、experiment_plan.yaml（实验列表）\\n\\n## 核心方向\\n多分类 LLM 标注误差在因果推断中的偏差传播：K×K 混淆矩阵 × 7 DAG 拓扑偏差分类 + ASV 灵敏度框架 + 校正指导。\\n\\n## 当前阶段：最终审稿打磨\\n\\n### Target Venue\\n- **EMNLP 2026**（ARR rolling review，8 页 main text + unlimited refs）\\n- DDL: 2026-05-25\\n\\n### Core Claims 覆盖率\\n| Claim | 完成/总计 | 状态 |\\n|-------|-----------|------|\\n| 1. Multi-class bias taxonomy | **5/6 (83%)** | plan_001✅ plan_002✅ plan_008✅ plan_009✅ plan_010✅ plan_003⚠️(API 402, 搁置) |\\n| 2. ASV framework | **3/3 (100%)** | plan_004✅ plan_005✅ plan_006✅ |\\n| 3. Correction guidance | **1/1 (100%)** | plan_007✅ |\\n\\n### 论文状态\\n- ✅ Main text 8 页（Conclusion + Limitations 在 page 8）\\n- ✅ 0 undefined references, 0 critical warnings\\n- ✅ 6 轮审稿修复完成（W6 same-sign→magnitude dominance, FWL scope, missing refs, ASV vs E-value, bootstrap restored, Theorem 1 xref fixed）\\n- ⏳ Round 7 审稿已提交，等待审批\\n\\n## 近期任务\\n- [ ] 等待 Round 7 审稿结果 → 修复发现的问题\\n- [x] GPU 空闲确认（Reviewer 正式确认，已通知 Manager 可释放）(D020)\\n- [x] plan003 frontier annotations → 搁置（API key 耗尽 + 论文空间不足）(D020)\\n- [x] Re-dream → 跳过（Claude API rate limit + 无方向性变化需求）(D020)\\n- [x] Reviewer warnings 全部修复（bootstrap 恢复、Theorem 1 xref、Conjecture 压缩确认）\\n\\n## GPU 预算\\nhome-1x5090: 1× RTX 5090（已通知 Manager 可释放，本项目不再需要 GPU）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D020 | 2026-05-22 | 搁置 plan003 frontier annotations 和 Re-dream；GPU 通知  | plan003_empirical_confusion_matrices, plan006_asv_empirical |\\n| D019 | 2026-05-22 | Sign flip 检查扩展为全系数检查，论文叙事从 \\\"zero sign flips\\\" 改为 \\\"5 | plan006_asv_empirical, plan011 |\\n| D018 | 2026-05-22 | Round 1 审稿 3.5→4.0 修复计划：proof 降级 + δ_max 约束 + fram | — |\\n| D
…[truncated 936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-23T10:33:28.611599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 1123 · 2026-05-23T10:33:29.717517+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf (898.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-23T10:34:06.907563+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 1125 · 2026-05-23T10:34:07.683053+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-23T10:34:37.298858+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 30391
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-23T10:34:37.299317+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 29616
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-23T10:34:37.450212+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "text": "你负责 **方法严谨性（Soundness）** 审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限 references；Limitations 不计入页数\n- **模板**: ACL [review] 模板\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf`\n\n## 论文概述\n标题: \"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n\n研究 K-class LLM 标注误差在 7 种 DAG 拓扑下的因果推断偏差传播。三个贡献：(1) 多分类偏差分类法——推导 7 种拓扑的偏差表达式，证明 confounding/collider 的符号保持，数值验证 mediation/M-bias/front-door；(2) ASV 灵敏度框架——证明 K=2 的 envelope monotonicity (Theorem 1)，K≥3 数值验证 (Conjecture 1)；(3) 校正指导——证明 FWL invariance 导致矩阵校正对 4 种拓扑无效。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 理论推导正确性\n- Proposition 1 (sign preservation) 的三个部分：(a) confounding Cauchy-Schwarz 论证、(b) collider Berkson attenuation 论证、(c) exposure 反例\n- Theorem 1 (K=2 envelope monotonicity)：perspective function convexity 论证是否严密？proportional effects 条件 (f=λg) 是否充分？\n- Conjecture 1 (K≥3 ε-approximate monotonicity)：数值验证规模（30,000 matrices × K∈{3,5,7} × 5 个 τ 值）是否充分？ε=0.06 的实际含义？\n- FWL invariance 证明：是否正确？linear OLS → logistic 的扩展是否合理？\n\n### 2. 核心假设\n- Non-differential misclassification (Definition 1)：在 LLM 标注场景中是否合理？stress test (Appendix B.6/B.16) 是否充分？\n- Proportional effects (f=λg)：15-17% failure rate 意味着什么？对核心结论（sign preservation）的影响？\n- Linear SEM：对 EMNLP 读者是否过于restrictive？logistic DGP 验证是否充分？\n\n### 3. 实验方法论\n- MC 验证：1.6% MAPE across 161 scenarios 是否充分？IV 的 3.7% 是否有系统性原因？\n- 实证验证：23 个 LLM 配置（4 个 open-weight 模型，7B-235B）是否足够？缺少商业模型和 ordinal 任务是否是重大限制？\n- ASV 验证：bootstrap CI、N-sensitivity、ranking stability\n\n### 4. 内部一致性\n- Abstract 中的数字与正文/表格是否一致\n- 各 Section 之间的交叉引用是否正确\n- 三级证据层次（proved/verified/conjectured）的使用是否一致\n\n请按以下格式输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条 S1, S2, ...)\n3. Weaknesses (逐条 W1, W2, ... 标注 must-fix/should-fix/minor)\n4. Questions (逐条 Q1, Q2, ...)\n5. Missing References (如有)\n6. Overall Assessment (评分 + 置信度)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "text": "你负责 **方法严谨性（Soundness）** 审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限 references；Limitations 不计入页数\n- **模板**: ACL [review] 模板\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf`\n\n## 论文概述\n标题: \"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n\n研究 K-class LLM 标注误差在 7 种 DAG 拓扑下的因果推断偏差传播。三个贡献：(1) 多分类偏差分类法——推导 7 种拓扑的偏差表达式，证明 confounding/collider 的符号保持，数值验证 mediation/M-bias/front-door；(2) ASV 灵敏度框架——证明 K=2 的 envelope monotonicity (Theorem 1)，K≥3 数值验证 (Conjecture 1)；(3) 校正指导——证明 FWL invariance 导致矩阵校正对 4 种拓扑无效。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 理论推导正确性\n- Proposition 1 (sign preservation) 的三个部分：(a) confounding Cauchy-Schwarz 论证、(b) collider Berkson attenuation 论证、(c) exposure 反例\n- Theorem 1 (K=2 envelope monotonicity)：perspective function convexity 论证是否严密？proportional effects 条件 (f=λg) 是否充分？\n- Conjecture 1 (K≥3 ε-approximate monotonicity)：数值验证规模（30,000 matrices × K∈{3,5,7} × 5 个 τ 值）是否充分？ε=0.06 的实际含义？\n- FWL invariance 证明：是否正确？linear OLS → logistic 的扩展是否合理？\n\n### 2. 核心假设\n- Non-differential misclassification (Definition 1)：在 LLM 标注场景中是否合理？stress test (Appendix B.6/B.16) 是否充分？\n- Proportional effects (f=λg)：15-17% failure rate 意味着什么？对核心结论（sign preservation）的影响？\n- Linear SEM：对 EMNLP 读者是否过于restrictive？logistic DGP 验证是否充分？\n\n### 3. 实验方法论\n- MC 验证：1.6% MAPE across 161 scenarios 是否充分？IV 的 3.7% 是否有系统性原因？\n- 实证验证：23 个 LLM 配置（4 个 open-weight 模型，7B-235B）是否足够？缺少商业模型和 ordinal 任务是否是重大限制？\n- ASV 验证：bootstrap CI、N-sensitivity、ranking stability\n\n### 4. 内部一致性\n- Abstract 中的数字与正文/表格是否一致\n- 各 Section 之间的交叉引用是否正确\n- 三级证据层次（proved/verified/conjectured）的使用是否一致\n\n请按以下格式输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条 S1, S2, ...)\n3. Weaknesses (逐条 W1, W2, ... 标注 must-fix/should-fix/minor)\n4. Questions (逐条 Q1, Q2, ...)\n5. Missing References (如有)\n6. Overall Assessment (评分 + 置信度)"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-23T10:35:03.477399+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26027
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-23T10:35:03.628399+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "text": "你负责 **新颖性 + 完整性（Novelty & Completeness）** 审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限 references；Limitations 不计入页数\n- **模板**: ACL [review] 模板\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf`\n\n## 论文概述\n标题: \"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n\n研究 K-class LLM 标注误差在 7 种 DAG 拓扑下的因果推断偏差传播。三个贡献：(1) 多分类偏差分类法——推导 7 种拓扑的偏差表达式，证明 confounding/collider 的符号保持；(2) ASV 灵敏度诊断框架——E-value 类似但针对 K×K 标注误差参数化；(3) 校正指导——FWL invariance 导致矩阵校正对 4 种拓扑无效。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性定位\n- 论文声称 \"first unified analysis of K-class annotation error propagation across seven canonical DAG topologies\"——是否成立？是否有先行工作已覆盖此领域？\n- ASV 与 E-value (VanderWeele & Ding, 2017) 的关系：是否为方法论创新还是直接移植？Sign-flip ASV 和 N* 是否是真正的新贡献？论文是否提供了充分的形式化对比？\n- FWL invariance 作为负面结果的贡献：在校正文献中是否真的被忽视？\n- 对 NLP/EMNLP 社区的贡献：这是一篇因果推断/计量经济学论文——对 EMNLP 读者的实用价值如何？\n\n### 2. 相关工作完整性\n- Related Work section 覆盖三个方向：measurement error in CI、text classifiers and LLM annotation、sensitivity analysis and correction\n- 检查是否有重要遗漏：\n  - 因果中介分析：Imai, Keele & Tingley (2010) 是否已引用？\n  - Text-based causal inference: Pryzant et al. (2021) 是否已引用？\n  - 其他可能遗漏的近期工作（2024-2026）\n- 引用格式是否符合 ACL 规范\n\n### 3. 展示质量\n- **Abstract 信息密度**: Abstract 包含大量数字（83.4%, 2.1%, 52.6%, 210,000, 0.45-0.81 等）——是否过载？\n- **Section 3.1 可及性**: plim、FWL 等计量经济学术语对 EMNLP 读者是否友好？是否有足够的直觉解释？\n- **Figure 质量**: Figure 1 (DAG taxonomy)、Figure 2 (bias distributions)、Figure 3 (F1 vs bias) 是否清晰、信息丰富？\n- **Table 1** 设计是否清晰？$\\tau_{sf}=0$? 列的三级标注 (Yes/Yes*/No) 是否容易理解？\n- **Algorithm 1** 是否可操作？是否有足够的说明？\n- **叙事流畅性**: Introduction → Related Work → Method → Experiments → Conclusion 的逻辑是否连贯？\n\n### 4. 格式合规\n- 正文是否不超过 8 页（Section 5 Conclusion + Limitations 必须在 p8 内）\n- References 格式是否一致\n- 匿名性：是否有任何 deanonymization 风险（代码链接、self-citation 措辞等）\n- Appendix 是否符合规范（不能有单独的 Limitations section）\n\n### 5. Limitations 完整性\n- 当前 Limitations 覆盖：non-differential 假设、K=3 linear SEM、ASV parameterization、DAG uncertainty、FWL under logistic、LLM 配置范围\n- 是否有重要遗漏？\n\n请按以下格式输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条 S1, S2, ...)\n3. Weaknesses (逐条 W1, W2, ... 标注 must-fix/should-fix/minor)\n4. Questions (逐条 Q1, Q2, ...)\n5. Missing References (如有)\n6. Overall Assessment (评分 + 置信度)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "text": "你负责 **新颖性 + 完整性（Novelty & Completeness）** 审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限 references；Limitations 不计入页数\n- **模板**: ACL [review] 模板\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_14/submitted.pdf`\n\n## 论文概述\n标题: \"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n\n研究 K-class LLM 标注误差在 7 种 DAG 拓扑下的因果推断偏差传播。三个贡献：(1) 多分类偏差分类法——推导 7 种拓扑的偏差表达式，证明 confounding/collider 的符号保持；(2) ASV 灵敏度诊断框架——E-value 类似但针对 K×K 标注误差参数化；(3) 校正指导——FWL invariance 导致矩阵校正对 4 种拓扑无效。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性定位\n- 论文声称 \"first unified analysis of K-class annotation error propagation across seven canonical DAG topologies\"——是否成立？是否有先行工作已覆盖此领域？\n- ASV 与 E-value (VanderWeele & Ding, 2017) 的关系：是否为方法论创新还是直接移植？Sign-flip ASV 和 N* 是否是真正的新贡献？论文是否提供了充分的形式化对比？\n- FWL invariance 作为负面结果的贡献：在校正文献中是否真的被忽视？\n- 对 NLP/EMNLP 社区的贡献：这是一篇因果推断/计量经济学论文——对 EMNLP 读者的实用价值如何？\n\n### 2. 相关工作完整性\n- Related Work section 覆盖三个方向：measurement error in CI、text classifiers and LLM annotation、sensitivity analysis and correction\n- 检查是否有重要遗漏：\n  - 因果中介分析：Imai, Keele & Tingley (2010) 是否已引用？\n  - Text-based causal inference: Pryzant et al. (2021) 是否已引用？\n  - 其他可能遗漏的近期工作（2024-2026）\n- 引用格式是否符合 ACL 规范\n\n### 3. 展示质量\n- **Abstract 信息密度**: Abstract 包含大量数字（83.4%, 2.1%, 52.6%, 210,000, 0.45-0.81 等）——是否过载？\n- **Section 3.1 可及性**: plim、FWL 等计量经济学术语对 EMNLP 读者是否友好？是否有足够的直觉解释？\n- **Figure 质量**: Figure 1 (DAG taxonomy)、Figure 2 (bias distributions)、Figure 3 (F1 vs bias) 是否清晰、信息丰富？\n- **Table 1** 设计是否清晰？$\\tau_{sf}=0$? 列的三级标注 (Yes/Yes*/No) 是否容易理解？\n- **Algorithm 1** 是否可操作？是否有足够的说明？\n- **叙事流畅性**: Introduction → Related Work → Method → Experiments → Conclusion 的逻辑是否连贯？\n\n### 4. 格式合规\n- 正文是否不超过 8 页（Section 5 Conclusion + Limitations 必须在 p8 内）\n- References 格式是否一致\n- 匿名性：是否有任何 deanonymization 风险（代码链接、self-citation 措辞等）\n- Appendix 是否符合规范（不能有单独的 Limitations section）\n\n### 5. Limitations 完整性\n- 当前 Limitations 覆盖：non-differential 假设、K=3 linear SEM、ASV parameterization、DAG uncertainty、FWL under logistic、LLM 配置范围\n- 是否有重要遗漏？\n\n请按以下格式输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条 S1, S2, ...)\n3. Weaknesses (逐条 W1, W2, ... 标注 must-fix/should-fix/minor)\n4. Questions (逐条 Q1, Q2, ...)\n5. Missing References (如有)\n6. Overall Assessment (评分 + 置信度)"
  }
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-23T10:35:05.144377+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1515
}
```

</details>

---


### Assistant

_source line 1132 · 2026-05-23T10:35:26.054611+00:00_

**Step 1 已启动**：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已派发，等待回复 |
| Reviewer 2（新颖性+完整性） | ✅ 已派发，等待回复 |
| 视觉审查 Agent | ✅ 已启动，与 Reviewer 并行 |
| 外部审稿（Stanford Agentic Reviewer） | ⏭️ 未配置，跳过 |

等待两位 Reviewer 的独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 108

## Round 108

2 recorded events


### User

_source line 1133 · 2026-05-23T10:42:11.914406+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）

---

### Summary

本文提出了一个统一框架，分析 K-class LLM 标注误差如何在 7 种 canonical DAG 拓扑下传播至因果估计偏差。三个贡献：(1) 多分类偏差分类法——推导 7 种拓扑的偏差表达式并证明 confounding/collider 的符号保持性质；(2) ASV 灵敏度诊断框架——三种互补度量（magnitude、significance、sign-flip）；(3) FWL invariance 负面结果——证明矩阵校正对 4 种协变量拓扑无效。通过 210,000 次 Monte Carlo 模拟和 3 个 NLP 数据集验证。

---

### Strengths

**S1.** 系统性范围覆盖前所未有。将标注误差分析从 K=2 二分类扩展到 K≥3，从单一拓扑扩展到 7 种 canonical DAG，是真正的范围创新。K≥3 揭示了定性新现象：exposure 下 83.4% 符号反转（Section 4.2），而 K=2 时 confounding/collider 的符号反转率为 0%（Table 1）。Prior work（Lee & Wood-Doughty 2024 仅覆盖 confounding；TelButhuis et al. 2023 限于二分类处理）均未达到此覆盖范围。

**S2.** 符号保持定理（Propositions 1–4）优雅且具实用价值。Proposition 2 证明 confounding 下比例效应保证 sign(plim τ̂) = sign(τ)，Proposition 3 给出一般情况的 worst-case bound B（Eq. 16），这些结构性保证直接告诉实践者"哪些拓扑下不用担心方向性错误"。

**S3.** FWL invariance 负面结果（Section 4.5, Appendix B.2, B.14）是真正新颖且非显而易见的发现。Table 4 和 Table 5 用 OLS 与 logistic 回归验证，Table 13 在 logistic 下展示了 mean bias reduction < 0.065% 的结果。这一发现有重要实践意义：阻止从业者在 confounding/mediation/collider/M-bias 拓扑上浪费精力于矩阵校正。

**S4.** 实验验证充分。210 种校正配置 × 6 种方法（Table 4），3 个 NLP 数据集（HumAID K=10, VAST K=5, CivilComments K=2），23 种 LLM 配置（Section 4.4, Figure 3），外加 ClinicalBERT 临床案例（Appendix B.18）。验证广度令人信服。

**S5.** Algorithm 1（page 31）将理论直接转化为可操作的决策流程。三步走（assess risk → select correction → FWL warning）为 NLP 从业者提供具体指导。

**S6.** Appendix 极为详尽（23 页），包含完整证据链（Propositions 1-4 的证明、20+ 补充实验、非微分假设压力测试 B.6、非线性 DGP 鲁棒性 B.7、differential misclassification 阈值 B.16）。

---

### Weaknesses

**W1** [should-fix] **ASV 与 E-value 的形式化对比缺失**
- 具体位置：Section 3.3, Section 2 (Related Work)
- 问题：论文将 ASV 定位为"analogous to E-values"（Section 3.3, p.5），Related Work 也提到"Our ASV framework draws on the sensitivity analysis tradition of Ding and VanderWeele (2016), E-values (VanderWeele and Ding, 2017)"。但全文没有任何 proposition 或 theorem 形式化说明：(a) ASV 在何种条件下退化为 E-value？(b) 两者在数学结构上的区别是什么？(c) ASV 的 K×K confusion matrix 参数化相比 E-value 的 risk-ratio 参数化有何优势？
- 为什么影响接收：E-value 是成熟的、被广泛使用的灵敏度分析工具。如果 ASV 仅仅是对 E-value 的 re-parameterization，则方法论贡献被显著削弱。Reviewer 需要明确区分才能评估 novelty。
- 建议：增加一个 Remark 或 Proposition，形式化说明"E-value bounds unmeasured confounding on the risk-ratio scale; ASV bounds annotation error via the K×K confusion matrix C. When K=2 and C has structure [1-ε, ε; ε, 1-ε], ASV reduces to [具体表达式]，which differs from E-value because [具体原因]." Appendix B.20（Comparison with Related Sensitivity Frameworks, p.30, Table 18）部分已列出对比表但过于简略——应在正文中展开核心区别。

**W2** [should-fix] **对 EMNLP 读者的可及性不足**
- 具体位置：Section 3.1–3.2 (pages 3–4)
- 问题：plim、FWL decomposition、structural equation models 等计量经济学术语对 EMNLP 读者不友好。Section 3.1 从 Definition 1（non-differential misclassification）直接跳到 Eq. 1–5 的偏差表达式，中间缺少直觉解释。例如，Eq. 1 中 plim τ̂(A*) 的含义需要读者理解 probability limit 和 OLS 残差化过程，但论文仅在脚注 2（p.4）简短提及。
- 为什么影响接收：EMNLP 审稿人和读者主要来自 NLP/CL 背景。如果核心方法部分只有计量经济学训练的读者能读懂，论文的影响力和引用潜力会大打折扣。
- 建议：在 Section 3.1 开头增加一个具体 NLP running example（如："Consider a sentiment classification pipeline where an LLM labels reviews as positive/negative/neutral for downstream causal analysis of review sentiment on sales..."），然后用这个例子串联偏差表达式的推导。这不需要额外空间——可以替换当前较为泛化的描述。

**W3** [should-fix] **Conjecture 1（envelope monotonicity K≥3）未证明但被实质性使用**
- 具体位置：Section 3.3 (p.6, Observation 1), Appendix B.12 (p.26), Algorithm 1 (p.31)
- 问题：Conjecture 1 声称 envelope monotonicity 对 K≥3 成立，但仅有数值验证（210,000 随机混淆矩阵，Appendix B.12）。该猜想在 Algorithm 1 中被实质性使用——ASV 作为有意义的脆弱性诊断工具依赖于 monotonicity（否则 ASV 排序可能不稳定）。Appendix B.12（Table 10）报告 worst-case deviation < 0.066，但这不等于数学保证。
- 为什么影响接收：如果 Conjecture 1 对某类混淆矩阵结构不成立，Algorithm 1 的 Step 1（ASV-based risk assessment）可能给出误导性建议。猜想与被证明的定理之间的间隙需要更明确地讨论。
- 建议：(a) 明确陈述"Algorithm 1 的有效性依赖于 Conjecture 1"；(b) 讨论如果猜想不成立会产生什么后果（ASV 排序可能在某些 C 下不可靠）；(c) 提供更强的数值证据或部分证明（例如对 K=3 的特殊矩阵族的解析证明）。

**W4** [should-fix] **EMNLP venue fit 的论证不够充分**
- 问题：论文的核心贡献（偏差分类法、ASV、FWL invariance）是纯因果推断/计量经济学方法论。NLP 连接主要通过应用域建立（LLM 标注 → 因果估计），而非方法论对 NLP 的贡献。Introduction 最后一段（p.1-2）提到"LLM-generated annotations"但未充分论证为什么 EMNLP 读者应该关心这个问题，以及这项工作相比直接发表在因果推断 venue（如 UAI、AISTATS、Journal of Causal Inference）有何额外价值。
- 建议：在 Introduction 中增加一段，明确论证 EMNLP 读者的 actionable takeaway，例如："NLP practitioners using LLM annotations for causal studies currently have no topology-aware diagnostic tool. Our framework fills this gap by providing Algorithm 1, which requires only the confusion matrix and DAG specification..."

**W5** [minor] **Abstract 数字密度过高**
- 具体位置：Abstract (p.1)
- 问题：Abstract 包含 10+ 个具体数字（83.4%, 2.1%, 52.6%, 210,000, 0.45-0.81, 15×, K=2, K=3 等）。每个数字都有意义，但聚合效果令人 overwhelmed。
- 建议：保留 3-4 个最具影响力的数字（如 83.4% sign reversal, FWL invariance, 210 configurations），其余改为定性描述。

**W6** [minor] **Table 1 的 Yes/Yes*/No 标注不够直观**
- 具体位置：Table 1 (p.7)
- 问题：τ_sf=0? 列的三级标注需要读脚注才能理解。Yes* 表示"under proportional effects"（脚注在 p.4），但读者在 p.7 看到 Table 1 时可能已忘记脚注。
- 建议：在 Table 1 下方直接添加 legend 或在 caption 中解释 Yes* 含义。

**W7** [minor] **Algorithm 1 的阈值过于具体化**
- 具体位置：Algorithm 1 (p.31)
- 问题：阈值如"RMSE red. ~99.65%"、"RMSE red. ~86.6%"看起来高度校准于本文实验设置。论文未讨论这些阈值是否应在新数据集/新任务上重新校准。
- 建议：明确说明这些阈值是基于本文实验得出的参考值，并建议实践者在自己的数据上验证。

---

### Questions

**Q1.** Section 4.2 和 Appendix B.6 讨论了非微分假设违背的 stress test，但 main text 对结果的总结过于简略。Table 7（Appendix B.6）显示 ε=0.10 时 sign-flip rate 从 baseline 3.5% 变化到多少？对 Propositions 1-4 的核心保证在假设轻微违背时是否仍然近似成立？

**Q2.** Observation 1 证明了 K=2 的 envelope monotonicity，但 Conjecture 1 推广到 K≥3。在 K=3 证明中，哪一步具体卡住了？是凸性论证（Appendix A.4）中的多元扩展，还是排列矩阵的组合复杂度？

**Q3.** ClinicalBERT 案例（Appendix B.18）使用的 K=3 混淆矩阵来自单一实验设置。如果换用不同的 clinical NLP 模型（例如不同 epoch 或不同预训练基础），ASV 值的稳定性如何？

**Q4.** Limitations 提到 "DAG uncertainty" 但未展开。在实践中 DAG 拓扑往往未知或有争议。当从业者不确定是 confounding 还是 mediation 时，Algorithm 1 应如何使用？是否应该对所有可能的拓扑运行 ASV 并取最保守的结果？

---

### Missing References

论文引用覆盖相当完整：
- Imai, Keele & Tingley (2010) ✓ — cited as reference on p.10
- Pryzant et al. (2021) ✓ — cited on p.11
- Feder et al. (2022) survey ✓
- Wood-Doughty et al. (2018) ✓
- VanderWeele & Ding (2017) ✓
- Keith et al. (2020) ✓

未发现关键遗漏。一篇可能相关的近期工作：
- "Causal Effect Estimation with Latent Textual Treatments" (2026, arXiv:2602.15730) — 讨论 text-as-treatment 的因果估计偏差，但聚焦于 latent treatment 而非标注误差传播，且可能在本文提交后发表，非关键遗漏。

---

### 格式合规检查

| 检查项 | 结果 |
|--------|------|
| 正文 ≤ 8 页 | ✅ Sections 1-5 + Limitations 在 p.1-8 |
| Limitations 在正文内 | ✅ 在 p.8，Section 5 之后 |
| Appendix 无单独 Limitations | ✅ |
| 匿名性 | ✅ "Anonymous ACL submission"，无代码链接，仅承诺 "Code and data will be released" |
| References 格式 | ✅ ACL 格式，一致 |
| Appendix 无过多实质内容占用 | ⚠️ 23 页 appendix 内容极为丰富，但这不违规——所有核心 claim 在正文中有支撑 |

---

### Limitations 完整性评估

当前 Limitations 覆盖 6 点：non-differential 假设、K=3 linear SEM、ASV parameterization、DAG uncertainty、FWL under logistic、LLM 配置范围。覆盖面合理。

可能的遗漏：
1. **混淆矩阵的可获得性问题**：整个框架假设 confusion matrix C 已知或可估计，但实践中获取准确的 C 需要 gold-standard 标签——这本身就是标注问题的核心瓶颈。Limitations 应提及这一 chicken-and-egg 问题。
2. **外部效度**：所有实验使用英语数据集，未讨论跨语言迁移性。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4.0/5 | 证明严谨（Propositions 1-4），Monte Carlo 验证充分。扣分项：Conjecture 1 未证明但被实质使用 |
| Excitement | 3.0/5 | FWL invariance 和符号保持定理有新意，但问题设定偏 niche，核心贡献属因果推断而非 NLP 方法论 |
| Reproducibility | 4.0/5 | 证明完整，实验描述详细，DGP 参数全部给出。代码未公开但方法论足够清晰 |
| Overall Assessment | 3.5/5 | Borderline Conference。技术贡献扎实（soundness 4.0），但 EMNLP venue fit 和可及性（W2, W4）制约了 excitement。若 W1-W3 解决，可上调至 4.0 |
| Confidence | 4/5 | 熟悉因果推断和 measurement error 文献，仔细检查了主要证明和实验 |

---

### 总体评分

**Overall**: 3.5 (Borderline Conference)

**一句话总结**: 技术上严谨且范围创新的因果推断工作（unified K-class × 7 topology framework + FWL invariance negative result），但 ASV vs E-value 的形式化对比缺失、对 EMNLP 读者的可及性不足、以及 venue fit 论证薄弱，使其停留在 Conference 和 Findings 的边界。

---

### 主要优势（总结）
1. 首个 K-class × 7 topology 的统一标注误差传播分析
2. 符号保持定理提供了结构性安全保证
3. FWL invariance 是真正新颖且有实践价值的负面结果
4. 实验验证广度令人信服（210 configs, 3 datasets, 23 LLM configs）
5. Algorithm 1 将理论直接转化为从业者决策工具

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1134 · 2026-05-23T10:42:19.020053+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 109

## Round 109

2 recorded events


### User

_source line 1135 · 2026-05-23T10:42:25.893977+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心评估：**Overall 3.5（Borderline Conference）**。

主要发现：
- **技术贡献扎实**：K-class × 7 topology 的统一分析框架、符号保持定理、FWL invariance 负面结果均为真正的新贡献，Soundness 4.0
- **三个 should-fix 问题**：(1) ASV 与 E-value 缺少形式化对比，novelty 边界不清；(2) 计量经济学术语对 EMNLP 读者不够友好；(3) Conjecture 1 未证明但被 Algorithm 1 实质性使用
- **venue fit 存疑**：核心贡献是因果推断/计量经济学方法论，NLP 连接主要通过应用域建立
- **相关工作完整**：Imai et al. 2010、Pryzant et al. 2021 等关键文献均已引用，无重大遗漏
- **格式合规**：8 页限制、匿名性、Limitations 位置均符合要求

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1136 · 2026-05-23T10:42:35.887214+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 110

## Round 110

6 recorded events


### User

_source line 1137 · 2026-05-23T10:43:43.796477+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性（Soundness）审查

## 论文信息
**标题**: "Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction"
**Venue**: EMNLP 2026 (ARR)
**审查侧重**: 理论推导正确性、核心假设合理性、实验方法论、内部一致性

---

## 1. Summary

本文研究 K-class LLM 标注误差在 7 种 DAG 拓扑下的因果推断偏差传播，贡献三部分：(1) 多分类偏差分类法，证明 confounding/collider 的符号保持（Proposition 1），构造 exposure 的符号反转反例；(2) ASV 灵敏度框架，证明 K=2 下的 envelope monotonicity（Theorem 1），K≥3 数值验证（Conjecture 1）；(3) 校正指导，证明 FWL invariance 导致矩阵校正对 4 种拓扑无效。理论结果通过 MC 模拟（161 scenarios, 1.6% MAPE）和 23 个实证 LLM 配置验证。论文在其所覆盖的范围内理论严谨，但核心结果的证明范围（K=2, 线性 SEM, 比例效应）窄于论文标题和动机所暗示的适用范围（multi-class, K≥3）。

---

## 2. Strengths

**S1: 系统性的拓扑覆盖。** 7 种 DAG 拓扑的统一分析是新颖的。先前工作（Lee and Wood-Doughty, 2024; TelBauthaus et al., 2023）仅覆盖 1–4 种拓扑。论文 Figure 1 清晰展示了拓扑结构，每个拓扑有独立的偏差推导和数值验证。

**S2: 三级证据层次的科学诚实性。** 论文明确区分 "proved"（Proposition 1, Theorem 1）、"numerically verified"（Observation 1, 各拓扑的数值验证）和 "conjectured"（Conjecture 1）。这种分层在同类论文中不常见，是科学严谨性的体现。

**S3: 符号保持证明的技术正确性。** 我逐步验证了以下关键推导：
- **Confounding (Appendix A.3, Proposition 2-3)**：Cauchy-Schwarz 论证链正确——先对条件协方差应用 C-S 不等式，再对期望再次应用 C-S，最后用全方差定律得到 |R(C)| ≤ B 的上界。从 |R(C)| ≤ B 到 sign(plim τ̂) = sign(τ) 的推导（当 |τ| > B 时）逻辑自洽。
- **Collider (Appendix A.6, Proposition 5-6)**：Berkson attenuation 论证正确——误分类将 collider-induced bias 向零衰减（B(C) = τ·B(C)），因此不会引入新的符号反转。
- **Exposure counterexample (Appendix A.8, Proposition 7)**：K=3 下的显式构造合法——选定 DGP 参数和混淆矩阵后，展示 plim β̂_1 < 0 而 β_1 > 0。论文正确指出 K=2 下符号反转结构上不可能（因为 2×2 正对角线随机矩阵不能反转单一系数的符号）。

**S4: 多层次验证流水线。** 解析推导 → MC 模拟（161 scenarios, N=10,000）→ 实证 LLM 混淆矩阵（23 配置 × 3 数据集）→ ClinicalBERT 案例研究（Appendix B.3）。这种多层验证是方法论上的最佳实践。

**S5: FWL invariance 结果的实用价值。** 证明矩阵校正对 4 种协变量拓扑无效（Section 4.5, Appendix B.2）直接帮助实践者避免无效操作。证明本身（列空间保持论证）简洁正确。

**S6: 问题的时效性和重要性。** LLM 标注日益替代人工标注用于 CSS 因果推断，理解标注误差的因果传播后果具有迫切实际意义。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**W1 [critical]: Theorem 1 仅证明 K=2，与 "Multi-Class" 标题/框架不匹配。**
- **具体位置**: Theorem 1 (Section 3.3, p.6), Conjecture 1 (Section 3.3, p.6), Appendix A.4 (p.14)
- **问题**: 论文的核心理论贡献——envelope monotonicity——仅在 K=2 + 比例效应条件下完成证明。对于 K≥3（论文标题强调 "Multi-Class"，Introduction 声称 "K=3–14 categories" 是常见场景），结果降级为 Conjecture 1，依赖 30,000 random matrices × K∈{3,5,7} × 5 个 τ 值的数值验证。ε<0.06 的界意味着允许最高 6% 的严格单调性违反——这一容差的实际含义未充分讨论。
- **为什么影响接收**: 论文的核心理论 claim 在其主要目标场景（multi-class）下未被证明。标题与证明范围之间的落差是主要 soundness 关切。
- **建议修改方向**: (a) 明确讨论 K=2 证明无法扩展到 K≥3 的数学障碍（是 perspective function 的维度问题，还是 K×K 随机矩阵结构的根本限制？）；(b) 讨论 ε=0.06 在实践中意味着什么——对治疗效应估计的具体影响有多大；(c) 考虑是否能对特定混淆矩阵结构（如近对角占优矩阵）证明 K≥3 的部分结果。

**W2 [critical]: 比例效应条件 (f=λg) 的限制性未充分探讨。**
- **具体位置**: Theorem 1 条件, Propositions 2/5, Appendix B.13 (p.27)
- **问题**: Theorem 1 和 sign preservation 的关键结果（Propositions 2, 5）要求混杂因素对治疗和结局的效应成比例（f=λg）。Appendix B.13 报告 λ OOB 率从精确比例时的 0% 上升到 f,g 独立时的约 23%。论文仅报告了随机抽样下的失败率统计，未刻画**何种结构条件**下比例效应成立或失败。NLP 实践者无法判断自己的 DGP 是否满足此条件。
- **为什么影响接收**: 如果 15-23% 的现实 DGP 不满足比例效应，核心理论结果的适用性大打折扣。论文需要提供可操作的诊断指导。
- **建议修改方向**: (a) 给出比例效应的直觉解释——何时混杂因素对 T 和 Y 的效应方向/比例自然一致？(b) 提供非比例效应下的最坏情况分析；(c) 讨论实践者如何用观测数据近似评估此条件。

### Should-Fix 问题（影响评分但不一票否决）

**W3 [warning]: 线性 SEM 假设对 EMNLP 读者的限制性。**
- **具体位置**: Section 3 全部理论推导, Appendix B.7 (Table 5, p.22), Limitations (p.8)
- **问题**: 全部证明假设线性结构方程。Appendix B.7 的 logistic DGP 验证（Table 5）显示 FWL invariance 在 logistic 下失效（≤7% bias reduction, N≥5,000 时 "correction worsens bias"）。但符号保持和单调性在非线性模型下未验证。EMNLP 读者的因果推断多用 logistic 或其他非线性模型。
- **建议**: 将线性 SEM 限制从 Limitations 的简短提及提升为更显著的讨论；或者在 Appendix B.7 中补充 logistic DGP 下 sign preservation 的数值验证。

**W4 [warning]: IV 拓扑系统性排除但缺少替代方案讨论。**
- **具体位置**: Conjecture 1 排除 IV (Section 3.3, p.6), Table 1 IV 行 (p.7), Section 4.3 (p.7)
- **问题**: IV 被排除于 Conjecture 1（"due to first-stage singularity"）、ASV 单调性分析之外，显示 52.6% sign reversal under Dirichlet priors，ASV=∞（immune）。但 IV 是 NLP 因果推断的重要策略。论文将 IV 标记为 "maximally fragile" 后未讨论替代估计方法。
- **建议**: 讨论在 IV 设计中应对标注误差的替代策略（如 bounds approach、two-sample IV、或 sensitivity analysis for first-stage misclassification）。

**W5 [warning]: 实证验证范围。**
- **具体位置**: Section 4.4 (p.7-8), Appendix B.3 (p.22)
- **问题**: 仅测试 4 个 open-weight 模型（7B-235B），无商业模型（GPT-4, Claude）。3 个数据集（HumAID K=10, VAST K=5, CivilComments K=2），无 ordinal 标注任务。论文声称对 "LLM-annotated causal inference" 的一般性可能过强。
- **建议**: 明确讨论 open-weight vs. commercial 模型的混淆矩阵结构是否可能存在系统差异；或降低一般性声明的力度。

**W6 [warning]: Non-differential misclassification 假设的实践合理性需加强。**
- **具体位置**: Definition 1 (Section 3.1, p.4), Appendix B.5 (p.23), Appendix B.6 (p.23-24)
- **问题**: Definition 1 要求 P(A*|A,Y,Z) = P(A*|A)。论文论证 "LLM 仅看文本，不观察 Y 或 Z"（Section 3.1）。但实际中：(a) 文本本身常包含 Y-predictive 信息，LLM 可能隐式利用；(b) chain-of-thought prompting 可能引入对 Y 的隐式条件化。Appendix B.6 的 stress test（Table 7-8）测试了结构化违反，结果表明 K≥3 exposure 对违反敏感（ε≥0.01 时 14/16 配置产生 sign reversal），但这些扰动是合成的，未针对 LLM 的实际失败模式设计。
- **建议**: 补充基于真实 LLM 失败模式（如 outcome-correlated text features 导致的差异性误分类）的 stress test。

---

## 4. Questions

**Q1**: Conjecture 1 的 K=2→K≥3 证明障碍的具体数学性质是什么？是 perspective function 在 K≥3 维度下的非凸性，还是 K×K 随机矩阵的某种结构特性使得 V_g(δ) 的凸性不再成立？

**Q2**: Appendix A.3 Proposition 3 定义的 worst-case bound B（方程 16）依赖于 DGP 参数。实践者通常不知道真实 DGP 参数——论文能否讨论如何从观测数据估计 B 的上界，以判断符号保持是否成立？

**Q3**: Table 5 (Appendix B.7) 显示 logistic regression 下矩阵校正产生小但非零的 bias reduction（~7%）。对于使用 logistic 的实践者，推荐的校正策略是什么？论文仅说 "negligible"，但对于 high-stakes 应用（如医疗因果推断），7% 可能不可忽略。

**Q4**: 非比例效应下的 15-17% 单调性失败率（Appendix B.13）——这些失败是否集中在特定拓扑或 DGP 参数区间？如果失败主要发生在 τ 接近零的情况（即真实效应本身很小），则实际影响可能有限。

**Q5**: ClinicalBERT 案例研究（Appendix B.3）得出 OR=0.89，结论是误分类不能反转保护性效应方向。这一结论对混淆矩阵的选择有多敏感？在不同合理混淆矩阵下的 OR 分布（bootstrap/sensitivity analysis）会增强此 claim 的可信度。

---

## 5. Missing References

未发现关键缺失引用。测量误差文献（Carroll et al., 2006; Gustafson, 2004; Brenner, 1993; Neuhaus, 1999; Ogburn and VanderWeele, 2012）和 NLP 因果推断文献（Feder et al., 2022; Keith et al., 2020; Wood-Doughty, 2024）覆盖充分。

---

## 6. Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 在其覆盖范围内（K=2, 线性 SEM, 比例效应）理论严谨。但核心结果的证明范围窄于论文声称的适用范围（Multi-Class K≥3）。Conjecture 1 有充分数值支撑但仍是猜想。 |
| **Excitement** | 3.5/5 | 问题重要且时效性强；7 拓扑统一分析新颖；符号保持/反转的拓扑依赖性结果令人惊讶且有实用价值。但线性 SEM 限制了即时实践影响。 |
| **Overall** | 3.5/5 (Borderline Conference) | 理论深度高于 EMNLP 平均水平，验证流水线完整，问题选择好。但 K=2 证明与 Multi-Class 标题/动机之间的落差、比例效应条件的限制性是主要 concern。若能补充 W1（至少讨论 K≥3 的证明障碍和 ε 的实际含义）和 W2（可操作的比例效应诊断），可达 4.0 (Conference)。 |
| **Reproducibility** | 4/5 | 附录提供完整推导、MC 参数、Algorithm 1；提及代码和数据将公开。唯一缺失：LLM 标注的具体 prompt 模板未在论文中提供。 |
| **Confidence** | 4/5 | 我仔细验证了核心证明（Propositions 1-7, Theorem 1 的 perspective function 论证, FWL invariance）。K≥3 的数值验证我无法独立重现但论证看起来合理。 |

### 一句话总结

论文在 K=2 线性 SEM 框架内的理论贡献严谨且有价值，但核心 monotonicity 证明的适用范围（K=2 + 比例效应）与论文标题/动机所强调的 Multi-Class 场景之间存在显著落差——这是 borderline conference vs. conference 的关键区别因素。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-23T10:44:36.428391+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "text": "以下是 Reviewer 2（新颖性 + 完整性）的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）\n\n### Summary\n本文提出了一个统一框架，分析 K-class LLM 标注误差如何在 7 种 canonical DAG 拓扑下传播至因果估计偏差。三个贡献：(1) 多分类偏差分类法；(2) ASV 灵敏度诊断框架；(3) FWL invariance 负面结果。通过 210,000 次 Monte Carlo 模拟和 3 个 NLP 数据集验证。\n\n### Strengths\nS1. 系统性范围覆盖前所未有。K≥3 揭示定性新现象：exposure 下 83.4% 符号反转。\nS2. 符号保持定理优雅且具实用价值。\nS3. FWL invariance 负面结果是真正新颖且非显而易见的发现。\nS4. 实验验证充分（210 配置 × 6 方法，3 个 NLP 数据集，23 种 LLM 配置）。\nS5. Algorithm 1 将理论直接转化为可操作的决策流程。\nS6. Appendix 极为详尽（23 页），包含完整证据链。\n\n### Weaknesses\n\nW1 [should-fix] ASV 与 E-value 的形式化对比缺失\n- Section 3.3 将 ASV 定位为 \"analogous to E-values\"，Related Work 也提到，但全文没有任何 proposition 或 theorem 形式化说明：(a) ASV 在何种条件下退化为 E-value？(b) 两者数学结构区别？(c) K×K confusion matrix 参数化相比 E-value 的 risk-ratio 参数化有何优势？\n- 如果 ASV 仅是 E-value 的 re-parameterization，方法论贡献被削弱。\n- 建议：增加 Remark 或 Proposition 形式化说明。Appendix B.20 Table 18 对比表过于简略——应在正文展开核心区别。\n\nW2 [should-fix] 对 EMNLP 读者的可及性不足\n- plim、FWL decomposition、SEM 等计量经济学术语对 EMNLP 读者不友好。Section 3.1 从 Definition 1 直接跳到 Eq. 1-5，缺少直觉解释。\n- 建议：增加 NLP running example 串联偏差表达式推导。\n\nW3 [should-fix] Conjecture 1 未证明但被实质性使用\n- Conjecture 1 在 Algorithm 1 中被实质性使用——ASV 诊断依赖 monotonicity。ε<0.06 不等于数学保证。\n- 建议：明确陈述 \"Algorithm 1 的有效性依赖于 Conjecture 1\"；讨论如果猜想不成立的后果。\n\nW4 [should-fix] EMNLP venue fit 论证不够充分\n- 核心贡献是纯因果推断方法论。NLP 连接主要通过应用域建立。未充分论证 EMNLP 读者的 actionable takeaway。\n\nW5 [minor] Abstract 数字密度过高（10+ 个具体数字）\nW6 [minor] Table 1 的 Yes/Yes*/No 标注不够直观\nW7 [minor] Algorithm 1 的阈值过于具体化\n\n### Questions\nQ1. ε=0.10 时 sign-flip rate 变化？Propositions 1-4 在假设轻微违背时是否近似成立？\nQ2. K=3 证明具体卡住哪一步？\nQ3. ClinicalBERT 换用不同模型时 ASV 值的稳定性？\nQ4. DAG 拓扑未知时 Algorithm 1 如何使用？\n\n### Missing References\n未发现关键遗漏。\n\n### Overall Assessment\n3.5 (Borderline Conference)。技术贡献扎实（soundness 4.0），但 EMNLP venue fit 和可及性制约了 excitement。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "text": "以下是 Reviewer 2（新颖性 + 完整性）的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）\n\n### Summary\n本文提出了一个统一框架，分析 K-class LLM 标注误差如何在 7 种 canonical DAG 拓扑下传播至因果估计偏差。三个贡献：(1) 多分类偏差分类法；(2) ASV 灵敏度诊断框架；(3) FWL invariance 负面结果。通过 210,000 次 Monte Carlo 模拟和 3 个 NLP 数据集验证。\n\n### Strengths\nS1. 系统性范围覆盖前所未有。K≥3 揭示定性新现象：exposure 下 83.4% 符号反转。\nS2. 符号保持定理优雅且具实用价值。\nS3. FWL invariance 负面结果是真正新颖且非显而易见的发现。\nS4. 实验验证充分（210 配置 × 6 方法，3 个 NLP 数据集，23 种 LLM 配置）。\nS5. Algorithm 1 将理论直接转化为可操作的决策流程。\nS6. Appendix 极为详尽（23 页），包含完整证据链。\n\n### Weaknesses\n\nW1 [should-fix] ASV 与 E-value 的形式化对比缺失\n- Section 3.3 将 ASV 定位为 \"analogous to E-values\"，Related Work 也提到，但全文没有任何 proposition 或 theorem 形式化说明：(a) ASV 在何种条件下退化为 E-value？(b) 两者数学结构区别？(c) K×K confusion matrix 参数化相比 E-value 的 risk-ratio 参数化有何优势？\n- 如果 ASV 仅是 E-value 的 re-parameterization，方法论贡献被削弱。\n- 建议：增加 Remark 或 Proposition 形式化说明。Appendix B.20 Table 18 对比表过于简略——应在正文展开核心区别。\n\nW2 [should-fix] 对 EMNLP 读者的可及性不足\n- plim、FWL decomposition、SEM 等计量经济学术语对 EMNLP 读者不友好。Section 3.1 从 Definition 1 直接跳到 Eq. 1-5，缺少直觉解释。\n- 建议：增加 NLP running example 串联偏差表达式推导。\n\nW3 [should-fix] Conjecture 1 未证明但被实质性使用\n- Conjecture 1 在 Algorithm 1 中被实质性使用——ASV 诊断依赖 monotonicity。ε<0.06 不等于数学保证。\n- 建议：明确陈述 \"Algorithm 1 的有效性依赖于 Conjecture 1\"；讨论如果猜想不成立的后果。\n\nW4 [should-fix] EMNLP venue fit 论证不够充分\n- 核心贡献是纯因果推断方法论。NLP 连接主要通过应用域建立。未充分论证 EMNLP 读者的 actionable takeaway。\n\nW5 [minor] Abstract 数字密度过高（10+ 个具体数字）\nW6 [minor] Table 1 的 Yes/Yes*/No 标注不够直观\nW7 [minor] Algorithm 1 的阈值过于具体化\n\n### Questions\nQ1. ε=0.10 时 sign-flip rate 变化？Propositions 1-4 在假设轻微违背时是否近似成立？\nQ2. K=3 证明具体卡住哪一步？\nQ3. ClinicalBERT 换用不同模型时 ASV 值的稳定性？\nQ4. DAG 拓扑未知时 Algorithm 1 如何使用？\n\n### Missing References\n未发现关键遗漏。\n\n### Overall Assessment\n3.5 (Borderline Conference)。技术贡献扎实（soundness 4.0），但 EMNLP venue fit 和可及性制约了 excitement。"
  }
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-23T10:45:10.959649+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34531
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-23T10:45:11.163012+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见（方法严谨性）\n\n### Summary\n论文在其覆盖范围内理论严谨，但核心结果的证明范围（K=2, 线性 SEM, 比例效应）窄于论文标题和动机所暗示的适用范围（multi-class, K≥3）。\n\n### Strengths\nS1. 7 种 DAG 拓扑的统一分析是新颖的。\nS2. 三级证据层次（proved/verified/conjectured）科学诚实。\nS3. 符号保持证明技术正确——Cauchy-Schwarz, Berkson attenuation, exposure counterexample 均验证通过。\nS4. 多层次验证流水线（解析 → MC → 实证 → ClinicalBERT）。\nS5. FWL invariance 列空间保持论证简洁正确。\nS6. 问题时效性和重要性。\n\n### Weaknesses\n\nW1 [critical] Theorem 1 仅证明 K=2，与 \"Multi-Class\" 标题/框架不匹配。\n- Theorem 1 (envelope monotonicity) 仅在 K=2 + 比例效应条件下完成证明。K≥3 降级为 Conjecture 1，依赖 30,000 random matrices 数值验证。ε<0.06 允许 6% 的严格单调性违反——实际含义未充分讨论。\n- 论文核心理论 claim 在主要目标场景（multi-class）下未被证明。标题与证明范围之间的落差是主要 soundness 关切。\n- 建议：(a) 讨论 K≥3 证明障碍的数学性质；(b) 讨论 ε=0.06 在实践中的具体影响；(c) 对特定矩阵族（如近对角占优）证明部分结果。\n\nW2 [critical] 比例效应条件 (f=λg) 的限制性未充分探讨。\n- Appendix B.13 报告 λ OOB 率从 0% 上升到约 23%。论文未刻画何种结构条件下比例效应成立或失败。NLP 实践者无法判断自己的 DGP 是否满足此条件。\n- 15-23% 的现实 DGP 不满足比例效应，核心理论结果的适用性大打折扣。\n- 建议：(a) 给出比例效应的直觉解释；(b) 提供非比例效应下的最坏情况分析；(c) 讨论实践者如何用观测数据近似评估此条件。\n\nW3 [warning] 线性 SEM 假设对 EMNLP 读者的限制性。\n- 全部证明假设线性结构方程。Appendix B.7 logistic DGP 验证显示 FWL invariance 在 logistic 下失效（≤7% bias reduction）。符号保持和单调性在非线性模型下未验证。\n- 建议：提升线性 SEM 限制的讨论显著性，或补充 logistic DGP 下 sign preservation 的数值验证。\n\nW4 [warning] IV 拓扑系统性排除但缺少替代方案讨论。\n- IV 被排除于 Conjecture 1、ASV 单调性分析之外，52.6% sign reversal。但 IV 是 NLP 因果推断的重要策略。标记 \"maximally fragile\" 后未讨论替代估计方法。\n- 建议：讨论 IV 设计中应对标注误差的替代策略。\n\nW5 [warning] 实证验证范围。\n- 仅 4 个 open-weight 模型，无商业模型（GPT-4, Claude），3 个数据集，无 ordinal 任务。\n- 建议：明确讨论 open-weight vs. commercial 模型的混淆矩阵结构差异；或降低一般性声明力度。\n\nW6 [warning] Non-differential misclassification 假设的实践合理性需加强。\n- 文本本身常包含 Y-predictive 信息，LLM 可能隐式利用；chain-of-thought prompting 可能引入对 Y 的隐式条件化。Appendix B.6 stress test 是合成的，未针对 LLM 实际失败模式设计。\n- 建议：补充基于真实 LLM 失败模式的 stress test。\n\n### Questions\nQ1. K=2→K≥3 证明障碍的具体数学性质？perspective function 在 K≥3 的非凸性，还是随机矩阵结构？\nQ2. Proposition 3 worst-case bound B 依赖 DGP 参数。如何从观测数据估计 B 的上界？\nQ3. Table 5 logistic 下 ~7% bias reduction。对 high-stakes 应用推荐的校正策略？\nQ4. 15-17% 单调性失败率是否集中在特定拓扑或 DGP 参数区间？\nQ5. ClinicalBERT 案例 OR=0.89 对混淆矩阵选择的敏感性？\n\n### Overall Assessment\n3.5 (Borderline Conference)。K=2 证明与 Multi-Class 标题/动机之间的落差、比例效应条件的限制性是主要 concern。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见（方法严谨性）\n\n### Summary\n论文在其覆盖范围内理论严谨，但核心结果的证明范围（K=2, 线性 SEM, 比例效应）窄于论文标题和动机所暗示的适用范围（multi-class, K≥3）。\n\n### Strengths\nS1. 7 种 DAG 拓扑的统一分析是新颖的。\nS2. 三级证据层次（proved/verified/conjectured）科学诚实。\nS3. 符号保持证明技术正确——Cauchy-Schwarz, Berkson attenuation, exposure counterexample 均验证通过。\nS4. 多层次验证流水线（解析 → MC → 实证 → ClinicalBERT）。\nS5. FWL invariance 列空间保持论证简洁正确。\nS6. 问题时效性和重要性。\n\n### Weaknesses\n\nW1 [critical] Theorem 1 仅证明 K=2，与 \"Multi-Class\" 标题/框架不匹配。\n- Theorem 1 (envelope monotonicity) 仅在 K=2 + 比例效应条件下完成证明。K≥3 降级为 Conjecture 1，依赖 30,000 random matrices 数值验证。ε<0.06 允许 6% 的严格单调性违反——实际含义未充分讨论。\n- 论文核心理论 claim 在主要目标场景（multi-class）下未被证明。标题与证明范围之间的落差是主要 soundness 关切。\n- 建议：(a) 讨论 K≥3 证明障碍的数学性质；(b) 讨论 ε=0.06 在实践中的具体影响；(c) 对特定矩阵族（如近对角占优）证明部分结果。\n\nW2 [critical] 比例效应条件 (f=λg) 的限制性未充分探讨。\n- Appendix B.13 报告 λ OOB 率从 0% 上升到约 23%。论文未刻画何种结构条件下比例效应成立或失败。NLP 实践者无法判断自己的 DGP 是否满足此条件。\n- 15-23% 的现实 DGP 不满足比例效应，核心理论结果的适用性大打折扣。\n- 建议：(a) 给出比例效应的直觉解释；(b) 提供非比例效应下的最坏情况分析；(c) 讨论实践者如何用观测数据近似评估此条件。\n\nW3 [warning] 线性 SEM 假设对 EMNLP 读者的限制性。\n- 全部证明假设线性结构方程。Appendix B.7 logistic DGP 验证显示 FWL invariance 在 logistic 下失效（≤7% bias reduction）。符号保持和单调性在非线性模型下未验证。\n- 建议：提升线性 SEM 限制的讨论显著性，或补充 logistic DGP 下 sign preservation 的数值验证。\n\nW4 [warning] IV 拓扑系统性排除但缺少替代方案讨论。\n- IV 被排除于 Conjecture 1、ASV 单调性分析之外，52.6% sign reversal。但 IV 是 NLP 因果推断的重要策略。标记 \"maximally fragile\" 后未讨论替代估计方法。\n- 建议：讨论 IV 设计中应对标注误差的替代策略。\n\nW5 [warning] 实证验证范围。\n- 仅 4 个 open-weight 模型，无商业模型（GPT-4, Claude），3 个数据集，无 ordinal 任务。\n- 建议：明确讨论 open-weight vs. commercial 模型的混淆矩阵结构差异；或降低一般性声明力度。\n\nW6 [warning] Non-differential misclassification 假设的实践合理性需加强。\n- 文本本身常包含 Y-predictive 信息，LLM 可能隐式利用；chain-of-thought prompting 可能引入对 Y 的隐式条件化。Appendix B.6 stress test 是合成的，未针对 LLM 实际失败模式设计。\n- 建议：补充基于真实 LLM 失败模式的 stress test。\n\n### Questions\nQ1. K=2→K≥3 证明障碍的具体数学性质？perspective function 在 K≥3 的非凸性，还是随机矩阵结构？\nQ2. Proposition 3 worst-case bound B 依赖 DGP 参数。如何从观测数据估计 B 的上界？\nQ3. Table 5 logistic 下 ~7% bias reduction。对 high-stakes 应用推荐的校正策略？\nQ4. 15-17% 单调性失败率是否集中在特定拓扑或 DGP 参数区间？\nQ5. ClinicalBERT 案例 OR=0.89 对混淆矩阵选择的敏感性？\n\n### Overall Assessment\n3.5 (Borderline Conference)。K=2 证明与 Multi-Class 标题/动机之间的落差、比例效应条件的限制性是主要 concern。"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-23T10:45:12.884765+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1721
}
```

</details>

---


### Assistant

_source line 1142 · 2026-05-23T10:45:15.920157+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 111

## Round 111

2 recorded events


### User

_source line 1143 · 2026-05-23T10:45:18.644733+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心发现总结：

**评分**: Overall 3.5/5 (Borderline Conference), Soundness 3.5/5, Excitement 3.5/5

**两个 Must-Fix 问题**：
1. **Theorem 1 仅证明 K=2，但论文标题/动机强调 Multi-Class (K≥3)**——核心 monotonicity 结果在主要目标场景下未被证明，仅为 Conjecture 1（数值验证 ε<0.06）
2. **比例效应条件 (f=λg) 的限制性**——15-23% 的 DGP 不满足此条件，论文未提供可操作的诊断指导

**三个 Should-Fix 问题**：线性 SEM 限制对 EMNLP 读者的适用性、IV 拓扑被排除但缺少替代方案、实证验证仅覆盖 open-weight 模型

**正面评价**：符号保持证明（Cauchy-Schwarz, Berkson attenuation）技术正确、三级证据层次科学诚实、MC 验证流水线完整（1.6% MAPE across 161 scenarios）、FWL invariance 结果实用价值高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1144 · 2026-05-23T10:45:25.607894+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 112

## Round 112

2 recorded events


### User

_source line 1145 · 2026-05-23T10:46:15.666707+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Weaknesses 回应

### [AGREE] R2-W1: ASV 与 E-value 的形式化对比缺失

同意这是一个合理的 should-fix。Section 3.3 将 ASV 定位为 "analogous to E-values (VanderWeele and Ding, 2017)"，Appendix B.20 Table 18 提供了对比表但确实过于简略（仅列名称对比，无数学结构分析）。ASV 的参数化基于 K×K confusion matrix 插值路径 C(δ)=(1−δ)I+δC₀，而 E-value 基于 risk-ratio 单参数。如果 ASV 在 K=2 下可以被证明退化为某种 E-value 的变体（或证明不能），这将极大澄清方法论贡献的独立性。当前论文未提供此形式化连接，确实削弱了 ASV 作为独立方法论贡献的论证力度。

### [REBUT] R2-W2: 对 EMNLP 读者的可及性不足

部分不同意。论文的目标读者是**使用 LLM 标注进行因果推断的 NLP 研究者**——这一群体对 plim、SEM、FWL 等概念应具备基本熟悉度，否则他们本身也不应在无此背景的情况下进行因果推断研究。具体证据：

- Section 3.1 的 Definition 1（non-differential misclassification）附有直觉解释："This holds in standard annotation pipelines where the LLM receives only source text and classifies without observing the outcome Y or covariates Z"（p.4）。
- Section 3.2 每个拓扑的偏差表达式之后都附有 verbal interpretation（如 confounding: "Misclassification produces residual confounding that monotonically approaches the omitted variable bias"；collider: "misclassification attenuates the collider-induced bias toward zero"）。
- Figure 1 提供了 7 种 DAG 拓扑的清晰可视化。

不过，我同意增加一个 NLP running example（如用情感分析标注作为 treatment variable 的具体场景）串联推导会有帮助，但这是 presentation 优化而非 soundness 缺陷。将此标为 should-fix 似乎略重——minor 更合适。

### [AGREE] R2-W3: Conjecture 1 未证明但被实质性使用

同意。这与我的 W1 (critical) 一致——Conjecture 1 是 Theorem 1 从 K=2 到 K≥3 的关键桥梁，Algorithm 1（p.31）的 Step 1 "Assess risk level" 中 ASV magnitude 诊断隐式假设 envelope monotonicity 成立。如果 Conjecture 1 不成立（即存在 δ 使得 ASV 非单调），则 Algorithm 1 的阈值判断可能给出错误的风险评级。

论文应在 Algorithm 1 处添加显式声明："Algorithm 1 的 ASV 阈值判断的有效性依赖于 Conjecture 1（K≥3 ε-approximate monotonicity）。当 Conjecture 1 不成立时，报告的 ASV magnitude 可能低估实际偏差严重程度，误差上界为 ε<0.06（即最多 6% 的最大偏差）。"

### [REBUT] R2-W4: EMNLP venue fit 论证不够充分

不同意。论文的 venue fit 远不止"通过应用域建立"：

1. **问题动机直接来自 NLP 实践**：LLM 标注替代人工标注用于 CSS 因果推断是 EMNLP 社区的活跃研究方向（Gilardi et al., 2023; Ziems et al., 2024; Baumman et al., 2025 均发表在 *ACL venues）。论文 Introduction（p.1）引用的 7 篇文献中 5 篇来自 *ACL。

2. **实证验证使用 NLP 数据和模型**：Section 4.4 使用 HumAID（灾害推文分类）、VAST（立场检测）、CivilComments（毒性评论分类）三个 NLP 数据集，23 个 LLM 配置来自 NLP 模型（Llama, Qwen, Mistral）。ClinicalBERT 案例研究（Appendix B.3）同样是 NLP 模型应用。

3. **实践指导直接针对 NLP 研究者**：Algorithm 1 的输入是 DAG topology 和 gold-label availability——这正是 NLP 研究者在使用 LLM 标注时面临的决策。FWL invariance 结果直接告诉 NLP 实践者"矩阵校正方法对 4 种拓扑无效，不要浪费时间"。

4. **先例**：Feder et al. (2022) "Causal inference in natural language processing" 发表在 TACL；Keith et al. (2020) "Text and causal inference" 发表在 ACL。本文的理论深度与这些工作处于同一层次，且更直接面向当前 LLM 标注的实践问题。

Venue fit 不应因论文使用了因果推断的技术工具就被质疑——关键是**问题是否来自 NLP 社区、结果是否对 NLP 实践者有价值**，两者答案均为是。

### [AGREE] R2-W5: Abstract 数字密度过高

同意，minor 级别。Abstract 中包含 "1.6%"、"161"、"2.1%"、"52.6%"、"0.45-0.81"、"32.6%"（或 52.6%）、"K∈{3,5,7}"、"ε=0.06" 等 10+ 个具体数字，信息密度过高。建议保留 3-4 个最关键数字，其余移至 Introduction。

### [AGREE] R2-W6: Table 1 的 Yes/Yes*/No 标注不够直观

同意，minor 级别。"Yes*" 的含义（"Yes, conditional on specific DGP parameters"）需要查看脚注才能理解。可以改用更直观的标注如 "Conditional" 或用颜色编码。

### [AGREE] R2-W7: Algorithm 1 的阈值过于具体化

同意，minor 级别。Algorithm 1 中的 "0.5%"、"65%"、"τ threshold" 等具体数字来自论文的特定 MC 设置，可能不适用于其他 DGP。建议改为参数化阈值或标明"本文推荐值，使用者应根据具体场景校准"。

---

## Questions 回应

### [REBUT] R2-Q1: ε=0.10 时 sign-flip rate 变化？

论文已提供相关证据。Appendix B.6 Table 7 直接测试了 non-differential 假设违反对 sign-flip 的影响：ε=0.10 时，K=2 下所有拓扑 sign-flip rate 为 0%（符号保持完全成立）；K=3 下 confounding/mediation/collider/M-bias sign-flip rate 仍为 0%，仅 exposure 在结构化违反下产生 sign reversal。Table 8 进一步展示 ε 从 0.00 到 0.50 的连续变化，sign-flip rate 的增长模式清晰。Propositions 1-4 在假设轻微违背时确实近似成立——这正是 stress test 的结论（Section B.6, p.24: "the main conclusions hold under mild violations but should be interpreted cautiously when outcome-conditional annotation is suspected"）。

### [AGREE] R2-Q2: K=3 证明具体卡住哪一步？

同意这是一个重要问题。论文未明确说明 K≥3 证明的具体数学障碍。从 Appendix A.4 的证明结构推断，K=2 下 V_g(δ) 的凸性依赖于 perspective function (x,t)→x²/t 的显式代数展开——在 K=2 下混淆矩阵仅有 1 个自由参数（off-diagonal entry），使得 V_g(δ) 可以写成 δ 的显式有理函数并直接验证凸性。K≥3 下混淆矩阵有 K(K-1) 个自由参数，V_g(δ) 成为多变量有理函数的复合，凸性不再能通过逐项 perspective function 分解证明（因为交叉项的符号不确定）。这一障碍应在论文中明确陈述。

### [REBUT] R2-Q3: ClinicalBERT 换用不同模型时 ASV 值的稳定性？

Appendix B.11 Table 9 ("ASV stability across DGP parameters") 已部分回答此问题：在不同 DGP 参数（β 和 effect sizes）下，ASV ranking 跨拓扑是稳定的（confounding 最 robust，exposure 最 fragile，IV 从未达到 10% threshold）。虽然 Table 9 测试的是 DGP 参数变化而非模型变化，但 Section 4.4（p.7-8）报告 "across all 23 empirical LLM configurations including low-accuracy annotators (mean diagonal as low as 0.45), IV exhibits zero sign reversal"——这暗示 ASV 的定性结论（拓扑排序）对模型选择是稳定的。不过，直接报告不同模型下的 ASV 数值变化确实会更有说服力。

### [AGREE] R2-Q4: DAG 拓扑未知时 Algorithm 1 如何使用？

同意这是一个重要的实践问题。Algorithm 1 的输入要求明确的 DAG topology，但实践中 DAG 通常是假设性的。论文在 Limitations（p.8-9）简要提及 "When the true DAG is uncertain, practitioners can apply Algorithm 1 under each candidate topology and report the range of conclusions as a form of specification sensitivity analysis"，但这一重要指导应更突出——可以在 Algorithm 1 的描述中直接集成 DAG uncertainty 的处理步骤（如 Step 0: DAG identification → topology-specific guarantees → correction method selection）。

---

## 总体评估

Reviewer 2 的审稿质量高，问题定位准确。核心关切——Conjecture 1 的未证明性（W3）、ASV 与 E-value 的关系（W1）——与我的独立评估一致。主要分歧在 venue fit（W4）：我认为论文的 NLP 动机、数据、实践指导充分支撑 EMNLP venue fit，不应因使用因果推断技术工具就降低 venue fit 评价。W2（可及性）我认为应降级为 minor。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1146 · 2026-05-23T10:46:21.785561+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 113

## Round 113

2 recorded events


### User

_source line 1147 · 2026-05-23T10:46:26.149763+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心判断：

- **W1 (ASV vs E-value)**: AGREE — 缺少形式化对比确实削弱方法论贡献
- **W2 (可及性)**: REBUT — 论文已有足够直觉解释，目标读者应具备因果推断基础；建议降级为 minor
- **W3 (Conjecture 1 被实质使用)**: AGREE — 与我的 W1 (critical) 一致，Algorithm 1 应显式声明对 Conjecture 1 的依赖
- **W4 (venue fit)**: REBUT — 问题来自 NLP 社区、数据/模型均为 NLP、实践指导针对 NLP 研究者，有充分先例
- **W5-W7**: 全部 AGREE，均为合理 minor 问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1148 · 2026-05-23T10:46:31.486888+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 114

## Round 114

12 recorded events


### User

_source line 1149 · 2026-05-23T10:48:32.662035+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### W1 [critical] Theorem 1 仅证明 K=2，与 "Multi-Class" 标题不匹配

**[REBUT]** R1 将问题描述为"核心理论 claim 在 multi-class 下未被证明"，这一表述过度概括。需要区分论文的三层理论结构：

1. **偏差表达式（Section 3.2, Eqs 1–5）**：对一般 K 推导，不依赖 K=2。这是 "Multi-Class" 标题的首要支撑。
2. **符号保持（Propositions 1–6）**：对一般 K 证明。Proposition 2 证明 confounding 下比例效应的符号保持对所有 column-stochastic C 成立；Proposition 3 给出一般 f 的 worst-case bound B（Eq. 16），均不限于 K=2。Proposition 5–6（Appendix A.6, p.17–18）对 collider 也给出一般 K 的证明。Table 2（p.20）明确汇总了各拓扑的充分条件——"Proved" 栏适用于一般 K。
3. **Envelope monotonicity（Theorem 1）**：确实仅 K=2 + 比例效应。Conjecture 1 将其推广到 K≥3，依赖数值验证。

因此，"Multi-Class" 标题由偏差表达式 + 符号保持证明支撑，而非仅由 Theorem 1 支撑。R1 将全部理论贡献等同于 Theorem 1 的做法不准确。

**但我同意** Conjecture 1 的未证明状态确实是一个 soundness concern——它影响 ASV 作为诊断工具的可靠性（与我自己的 W3 一致）。建议(a)-(c) 有价值，特别是对 K=3 近对角占优矩阵的部分证明。

---

### W2 [critical] 比例效应条件 (f=λg) 的限制性

**[AGREE]** R1-W2: 比例效应条件确实限制性强，论文未充分帮助实践者判断自身 DGP 是否满足此条件。

但需要补充一个 R1 未提及的细节：Appendix B.13 Table 12（p.28）中 **NLP-realistic DGP** 的 sign failure rate 仅 0.07%，远低于 R1 强调的 15–23%。后者出现在 independent/near-proportional 设置下。这说明比例效应在 NLP 实际场景中可能比 R1 暗示的更常满足。

尽管如此，我同意 R1 的建议：论文应给出比例效应的直觉解释（即"处理效应的方向和相对大小在所有类别间保持一致"），并提供实践者用观测数据近似评估此条件的指南。

---

### W3 [warning] 线性 SEM 假设对 EMNLP 读者的限制性

**[REBUT]** R1-W3: R1 声称"符号保持和单调性在非线性模型下未验证"，这与 Appendix B.7（p.24）的内容不符。

Table 8（p.24）明确对比了 linear 和 logistic DGP 下的 sign-flip rates。论文原文写道：

> "Linear and logistic DGPs produce virtually identical sign-flip patterns across all seven topologies (|ΔSF_r| < 0.02)."

具体数据：Confounding SF_r = 0.000 (linear) vs 0.000 (logistic)；Exposure SF_r 在两者间差异 < 0.02；IV 在两种 DGP 下均表现高 sign-flip。符号保持**已经在 logistic DGP 下数值验证**。

R1 准确指出 FWL invariance 在 logistic 下失效（Table 5, p.22: mean bias reduction < 0.065%），但这是关于**校正方法**的限制，而非**符号保持**的限制。两者不应混为一谈。

我同意线性 SEM 假设是一个应更显著讨论的 limitation，但 R1 的具体 claim 需修正。

---

### W4 [warning] IV 拓扑系统性排除但缺少替代方案讨论

**[AGREE]** R1-W4: IV 被标记为"maximally fragile"（Section 3.2, p.5: 52.6% sign reversal）后，论文确实未讨论 NLP 中使用 IV 策略时应如何应对标注误差。这对 EMNLP 读者是实际的指导空白。

补充观点：Algorithm 1（p.31）在 Step 1 中将 IV 标记为 "Heist"（最高风险），Step 2 对 IV 给出 "M ← Heist: Exposure, IV: expt bias red. ~99.65%; no correction preferred"。但这仅是消极建议（"不要校正"），未提供积极替代方案（如 robust IV estimators、bounds approaches）。

---

### W5 [warning] 实证验证范围

**[AGREE]** R1-W5: 仅使用 open-weight 模型（Llama 系列）、3 个数据集、无 ordinal 任务，确实限制了经验发现的一般性。

但有两点补充：
1. 论文的**核心贡献是理论性的**（偏差表达式 + 符号保持 + FWL invariance），不依赖于特定模型。实验验证是支持性的，不是唯一证据。
2. Section 4.4 Figure 3（p.8）使用 23 种 LLM 配置（包括不同 prompt 策略、few-shot settings），覆盖了 F₁ 从 0.614 到 0.690 的范围。这比"仅 4 个模型"的描述更全面。

R1 关于 open-weight vs commercial 模型混淆矩阵结构差异的建议是合理的——至少应在 Limitations 中讨论。

---

### W6 [warning] Non-differential misclassification 假设

**[AGREE]** R1-W6: LLM 可能通过 chain-of-thought 隐式利用 Y-predictive 信息的担忧是合理的。

但论文在此方面的工作比 R1 描述的更充分：
- Appendix B.5（p.23）提供了基于 topic-stratified confusion matrices 的 proxy-based test，论文承认"this proxy-based test is necessarily limited"
- Appendix B.6（p.23–24）Table 7 展示了 structured differential misclassification stress test，在 ε=0.10 时所有拓扑的 sign-flip rate 变化低于 3 个百分点
- Appendix B.16（p.28–29）Table 15 展示了 differential misclassification 阈值——K=2 时所有配置均对 differential error 免疫（ε_diff=0.50），K≥3 时多数配置在 ε < 0.10 内保持稳健

我同意 R1 的建议——基于真实 LLM 失败模式（而非合成扰动）的 stress test 会更有说服力。但当前证据已提供了合理的保障水平。

---

### Q1. K=2→K≥3 证明障碍的数学性质

**[AGREE]** 这是一个重要的澄清问题。从 Appendix A.4（p.14）的证明结构看，K=2 证明依赖于 perspective function 的凸性（N²f/g 是凸的）和单变量参数化（δ ∈ [0,1]）。K≥3 时，混淆矩阵 C 有 K(K-1) 个自由参数，参数空间从一维变为多维，凸性论证不再直接适用。论文应在正文或 Appendix 中明确说明这一障碍。

---

### Q2. Proposition 3 worst-case bound B 的可估计性

**[AGREE]** 有价值的实践问题。Eq. 16 中 B 依赖 Var(g(A)), Var(f(A))，这些是 DGP 参数而非观测量。论文未讨论如何从数据估计 B 的上界。这对 Algorithm 1 的可操作性有直接影响——如果实践者无法计算 B，Proposition 3 的保证就只是理论上的。

---

### Q3. Table 5 logistic 下 ~7% bias reduction 的应对策略

**[AGREE]** 实践问题重要。Table 5（p.22）显示 logistic 下所有拓扑的 bias reduction 均 < 0.065%，这意味着在 high-stakes logistic regression 应用中，论文的矩阵校正方法实质上无效。论文在 Appendix B.14 承认这一点但 main text 中 Section 4.5 对此轻描淡写——仅说 "Under logistic regression the invariance breaks but empirically by < 0.065%"。对高风险应用，应推荐 non-matrix-based 替代方案（如 EM imputation、Bayesian methods）。

---

### Q4. 15-17% 单调性失败率的分布

**[AGREE]** 有价值。Table 10（Appendix B.12, p.26）按拓扑报告了 envelope violation rates，但未按 DGP 参数区间细分。如果失败集中在特定 confusion matrix 结构（如高度非对角占优），实践者可以提前排除这些情况。

---

### Q5. ClinicalBERT OR=0.89 的稳定性

**[AGREE]** 这与我自己的 Q3 一致。Appendix B.18 的 K=3 混淆矩阵来自单一模型配置，ASV 值在不同 confusion matrices 下的稳定性未被测试。

---

### 总结

R1 的 6 个 Weaknesses 中，我对 3 个 AGREE（W2, W4, W5），2 个部分 REBUT（W1, W6），1 个 REBUT（W3）。

**核心分歧**：
1. **W1**：R1 将论文描述为"仅证明 K=2"过于笼统。偏差表达式和符号保持定理（Propositions 1-6）均对一般 K 成立。仅 Theorem 1（envelope monotonicity）限于 K=2。
2. **W3**：R1 称符号保持在非线性模型下"未验证"，但 Appendix B.7 Table 8 已明确验证——|ΔSF_r| < 0.02 across all topologies。

**共识**：
- Conjecture 1 未证明是 soundness concern（W1 部分 + 我的 W3）
- 比例效应限制性需更好论证（W2）
- IV 替代方案缺失（W4）
- 实验范围可扩展（W5）

**建议的 Overall Assessment 维持**：3.5 (Borderline Conference)。R1 的 critical issues（W1, W2）在我看来应降级为 should-fix——因为偏差表达式和符号保持在一般 K 下已证明，且 NLP-realistic 场景下比例效应失败率仅 0.07%。核心理论比 R1 的评估更 sound。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-23T10:49:17.219361+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool call

_source line 1151 · 2026-05-23T10:49:17.219788+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1152 · 2026-05-23T10:49:18.374420+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T10:34:11.355960+00:00\", \"completed_at\": \"2026-05-23T10:34:15.476831+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-23T10:49:18.374948+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-23T10:49:18.375264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-23T10:49:18.425829+00:00_

1	issues:
2	  # === Round 1-7 历史 (resolved，保留摘要) ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 7
11	    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
12	    resolution_round: 7
13	
14	  - id: R1-N2
15	    category: soundness
16	    severity: should-fix
17	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
18	    status: resolved
19	    first_raised_round: 1
20	    last_seen_round: 3
21	    resolution: "Abstract 已准确区分 prove/verify。"
22	    resolution_round: 4
23	
24	  - id: R1-N3
25	    category: soundness
26	    severity: must-fix
27	    summary: "ASV C(δ) 定义域错误"
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---
