# Director coordination — Part 5 of 8

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/1d/1de11abfd142608a2277.json)

## Round 114

### Tool call

_source line 1156 · 2026-05-23T10:54:07.836595+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 14\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：23 个配置缺少商业 API（GPT-4/Claude）、>235B 模型、NER 等结构化任务。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 R1 再次提出(W5)。R2 REBUT——理论结论仅依赖混淆矩阵数学性质，不依赖 LLM 架构。Director 采纳 R2：降为 minor。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W5 再提。R2 AGREE 但强调核心贡献是理论性的。共识：Limitations 中讨论即可，minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 14\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补直觉解释。R1 新增批评：B.5 stress test 仅用随机扰动模型。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识 must-fix（R1）/should-fix（R2）。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W7 minor。Section 3.1 已有成立条件识别和 stress test（Appendix B.6）。R1 未单独提出。共识降为 minor。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W6 再提：LLM CoT 可能隐式条件化于 Y。R2 AGREE 但指出 Appendix B.5/B.6/B.16 已提供合理保障。共识：stress test 是合成的而非基于真实 LLM 失败模式，minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 14\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Abstract 至少 9-10 个定量信息点。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W4 再次提出（至少 7 个独立数字）。R1 REBUT——精确定量是好的实践，删减降低信息价值。Director 保留分歧。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2-W5 再提（10+ 数字）。R1 AGREE 建议保留 3-4 个。共识：minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 14\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献，但 magnitude ASV 与 E-value 同构度高。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-W3 再次提出：形式化对比不充分，需表格对比 ASV/E-value/partial R²。R1 AGREE 并补充应阐明 Sign-flip ASV 无法被 E-value 自然扩展的结构性原因。共识 should-fix。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2-W1 + R1 AGREE。全文无 proposition/theorem 形式化说明 ASV 与 E-value 的数学关系。Appendix B.20 Table 18 过于简略。共识 should-fix。\"\n    action_items:\n      - round: 13\n        action: \"Appendix 新增 ASV vs E-value/Partial R² 对比表（含 Topology dependence 行）\"\n        assigned_to: agent\n        status: in_progress\n      - round: 14\n        action: \"正文增加 Remark 或 Proposition 形式化说明 ASV 与 E-value 的数学结构区别\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 13\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"Section 4.4 已解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-Q4 追问机制。R1 AGREE 并给出可能解释（M-bias 误分类是保护性的，PPI++ 移除保护性衰减）。论文应明确说明。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 4.5 已包含机制解释（'misclassification attenuates the spurious M-bias path, and PPI++ removes this protective attenuation'）。可能已充分缓解。\"\n    action_items:\n      - round: 13\n        action: \"Section 4.5 明确解释 PPI++ 对 M-bias 有害的机制（移除保护性衰减）\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 W1 再次提出。R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：General case 15-17% 违反仍是已知限制。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W2 再次提出：15-17% 失败率（Sparse DGP 24.2%）在正文中讨论不足。R2 AGREE 并建议给出综合 coverage analysis。共识 should-fix。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W2 再提（critical）。R2 AGREE 但补充 NLP-realistic DGP 的 sign failure rate 仅 0.07%（Appendix B.13 Table 12），15-23% 出现在 independent/near-proportional 设置。Director 采纳 R2 降级为 should-fix。\"\n    action_items:\n      - round: 13\n        action: \"Method section 新增 15-17% 效应大小讨论 + ≥97% sign preservation + CSS 合理性论证\"\n        assigned_to: agent\n        status: in_progress\n      - round: 14\n        action: \"正文增加比例效应直觉解释 + 实践者如何用观测数据近似评估此条件\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R4-W6 合并。R2-W3 + R1 AGREE：需形式化对比表。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R4-W6 合并处理。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被 R11 两位 Reviewer 赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加 Collider amplification 脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论 PPI++ 对 M-bias 有害。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：exposure/IV 的 CI 跨界是拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧→R2 REBUT 成功：排名稳定性比绝对值更重要。Director 降为 minor。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 R1-Q4 间接涉及：δ* 阈值选择敏感性，跨阈值排序稳定性未验证。R2 AGREE。minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。ClinicalBERT ASV 稳定性被 R1-Q5 间接涉及，R2 指出 Appendix B.11 Table 9 已验证排名稳定性。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"R11 未再提及。Algorithm 1 整体被两位 Reviewer 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级为 should-fix。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出。Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W1 + R2-W2 再次提出。Director 维持 should-fix。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W1 (critical) + R2-W3 (should-fix)。R2 成功 REBUT R1 的 critical 评级：偏差表达式（Eqs 1-5）和符号保持（Props 1-6）均对一般 K 证明，仅 Theorem 1 限于 K=2。Director 采纳 R2 降级为 should-fix。共识：Algorithm 1 应显式声明对 Conjecture 1 的依赖。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"正文讨论 Conjecture 1 失效时对 ASV 实践指导的影响\"\n        assigned_to: agent\n        status: in_progress\n      - round: 13\n        action: \"Abstract 明确区分 K=2 formal guarantees 和 K≥3 numerical evidence\"\n        assigned_to: agent\n        status: in_progress\n      - round: 14\n        action: \"Algorithm 1 添加显式声明：ASV 阈值有效性依赖 Conjecture 1，失效时误差上界为 ε<0.06\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：General case 15-17% violation 是已知限制。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R6-M3 合并。R1-W2 再提。R2 AGREE + 建议综合 coverage analysis。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R6-M3 合并。R2 补充 NLP-realistic 0.07% sign failure rate。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"分歧：R2 认为与 E-value 同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R4-W6 合并。形式化对比不足是共识。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R4-W6 合并。共识 should-fix。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"均匀 ε 局限。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R1 新增：stress test 仅随机扰动，未测结构化违反。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 R1 评 must-fix，R2 评 should-fix。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W7 minor。Section 3.1 已有条件讨论 + stress test。改善明显。降为 minor。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W6 再提。R2 AGREE 但指出已有 B.5/B.6/B.16 三层验证。共识 minor。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧 → R2 REBUT 成功。Director 降为 minor。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。可能已充分缓解。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用 ding_vanderweele2016。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 NEW-1 和 R8-C2 讨论。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 合并到 R6-M3 和 NEW-1。R2 建议综合 coverage analysis。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 合并到 R6-M3 和 NEW-1。NLP-realistic 0.07% 是新数据点。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需 Section 3.1 加线性 SEM 动机。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"主文整合 logistic 结果不足。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Appendix B.6/B.13 logistic 验证充分但正文引用不足。已添加。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W4 + R2-W1 再次提出。plim 脚注和 FWL 内联定义已添加。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W3 再提。R2 REBUT：Appendix B.7 Table 8 已验证 logistic 下符号保持（|ΔSF_r|<0.02）。R1 混淆了 FWL invariance 失效（校正限制）与符号保持（理论结果）。Director 采纳 R2：符号保持已在 logistic 下验证，线性 SEM 限制降为 minor。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 12\n        action: \"Section 4.5 增加 logistic DGP 总结 + 引用 Appendix B.13\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 加 1-2 段直觉性文字解释 plim、FWL 分解、残差化\"\n        assigned_to: agent\n        status: in_progress\n      - round: 13\n        action: \"Section 4.5 精确限定 FWL invariance 仅适用于 covariate topologies，exposure 在 logistic 下不成立\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-Q1 追问具体障碍。R1 AGREE 指出 Appendix A.4 已部分回答。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-Q1 + R2 AGREE。K=2 依赖 perspective function 凸性 + 单变量参数化；K≥3 参数空间变多维，凸性不再直接适用。两位 Reviewer 共识应在正文更明确说明。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"R1 REBUT 成功。Introduction 措辞准确且有事实支撑。\"\n    resolution_round: 12\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 R1-W3。共识：不影响核心贡献。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 合并到 R1-W3。R2 REBUT。Director 降为 minor。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 合并到 R1-W3。共识 minor。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被 R11 赞为 S5/S6 strength，可操作性获认可。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增强论文对 EMNLP 应用导向读者的说服力。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：ClinicalBERT 案例最接近端到端验证。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。Section 4.5 已包含 ClinicalBERT 提及。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 4.5 已引用 ClinicalBERT（p.8: 'ClinicalBERT validation (Appendix B.3) confirms FWL invariance in clinical NLP'）。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 14\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增加 3-4 句直觉语言解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出（R2-W3）。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-W1 + R1 AGREE。plim 脚注和 FWL 内联定义已添加但 R2 认为仍不充分。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2-W2 再提。R1 REBUT——目标读者应具备 CI 基础，建议降为 minor。Director 判定：R1 有理（目标读者应知道 plim/FWL），但 EMNLP 受众广泛，保持 should-fix（低优先级）。\"\n    action_items:\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 需更充分的直觉性解释段落\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"EXP-2 完成：K=3/5/10 × 7 topologies。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 14\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R12 未单独提出。Section 4.2 已有 practitioners 指导句。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W4 再提（IV 替代方案缺失）。R2 AGREE。共识 should-fix：论文标记 IV 为 'maximally fragile' 后仅给消极建议（'不要校正'），未提供积极替代方案（bounds approach、robust IV）。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 已添加。\"\n    resolution_round: 13\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文 Section 5 (Conclusion) 溢出至 p9，违反 EMNLP 2026 的 8 页限制\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩，视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语（plim/FWL）对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"plim 首次使用加脚注 + FWL 首次使用加内联解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 修复已部分生效。R2-W1 仍评 must-fix。与 R11-W2 合并。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R11-W2 合并。R1 REBUT 建议降为 minor。Director 保持 should-fix（低优先级）。\"\n    action_items:\n      - round: 12\n        action: \"plim 脚注 + FWL 内联定义\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 加直觉段落（超越单纯定义）\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 均已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: minor\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果，适用条件未标注\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"Algorithm 1 caption 已添加 K=3 calibration 注释。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2-W7 再提。R1 AGREE。共识 minor：阈值应标明为参考值，实践者需根据场景校准。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 和 Figure 7 视觉问题\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n\n  # === Round 13 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract、Section 4.2、Appendix B.4 之间存在 factual 不一致\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"三处统一：Abstract用empirical configs限定，Section 4.2用mean diagonal as low as 0.45限定，Appendix B.4用near-zero under empirical conditions。\"\n    resolution_round: 14\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑（M-bias, front-door, IV）缺少 NLP 应用场景示例\"\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [R2]\n        note: \"R2-W5 提出。R1 部分 AGREE 但建议降为 minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 3.2 已为 M-bias 和 front-door 添加 NLP 场景（'annotator expertise and topic difficulty'、'sentiment labels affect user engagement'）。\"\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 新发现的缺失引用\"\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [R2]\n        note: \"R2 提出 3 篇。Director：Imai et al. (2010) 和 Pryzant et al. (2021) 建议引用。\"\n      - round: 14\n        reviewers: [R2]\n        note: \"R14 R2 确认 Imai et al. 2010 和 Pryzant et al. 2021 均已引用（Related Work p.3）。无关键遗漏。\"\n\n  - id: R13-CRIT1\n    category: soundness\n    severity: critical\n    summary: \"Limitations 中 diagonal accuracy 范围错误（0.61-0.83 → 应为 0.45-0.81）\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"0.45-0.81 与 updated_empirical_results.json 实际数据 (0.453-0.809) 一致。Abstract 同步。\"\n    resolution_round: 14\n\n  # === Round 14 新发现 ===\n\n  - id: R14-W1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 的 Yes/Yes*/No 三级标注不够直观，需查看脚注才能理解\"\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R2-W6 提出。R1 AGREE。共识 minor：可改用 'Conditional' 或在 Table 1 caption 中解释 Yes* 含义。\"\n\n  - id: R14-W2\n    category: method\n    severity: should-fix\n    summary: \"IV 拓扑被标记为 maximally fragile 后缺少积极替代方案讨论\"\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R1-W4 提出。R2 AGREE。Algorithm 1 仅给消极建议（不校正），未讨论 bounds approach、robust IV、two-sample IV 等替代策略。共识 should-fix。\"\n\n  - id: R14-W3\n    category: presentation\n    severity: should-fix\n    summary: \"混淆矩阵 C 的可获得性——整个框架假设 C 已知或可估计，但获取准确 C 需 gold-standard 标签\"\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [R2]\n        note: \"R2 在 Limitations 完整性评估中提出。C 的估计是 chicken-and-egg 问题——需 gold labels 来估计 C，但如果有足够 gold labels 则不需要 LLM 标注。Limitations 应提及。\"\n"
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
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 14\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：23 个配置缺少商业 API（GPT-4/Claude）、>235B 模型、NER 等结构化任务。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 R1 再次提出(W5)。R2 REBUT——理论结论仅依赖混淆矩阵数学性质，不依赖 LLM 架构。Director 采纳 R2：降为 minor。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W5 再提。R2 AGREE 但强调核心贡献是理论性的。共识：Limitations 中讨论即可，minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 14\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补直觉解释。R1 新增批评：B.5 stress test 仅用随机扰动模型。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识 must-fix（R1）/should-fix（R2）。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W7 minor。Section 3.1 已有成立条件识别和 stress test（Appendix B.6）。R1 未单独提出。共识降为 minor。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W6 再提：LLM CoT 可能隐式条件化于 Y。R2 AGREE 但指出 Appendix B.5/B.6/B.16 已提供合理保障。共识：stress test 是合成的而非基于真实 LLM 失败模式，minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 14\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Abstract 至少 9-10 个定量信息点。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W4 再次提出（至少 7 个独立数字）。R1 REBUT——精确定量是好的实践，删减降低信息价值。Director 保留分歧。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2-W5 再提（10+ 数字）。R1 AGREE 建议保留 3-4 个。共识：minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 14\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献，但 magnitude ASV 与 E-value 同构度高。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-W3 再次提出：形式化对比不充分，需表格对比 ASV/E-value/partial R²。R1 AGREE 并补充应阐明 Sign-flip ASV 无法被 E-value 自然扩展的结构性原因。共识 should-fix。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2-W1 + R1 AGREE。全文无 proposition/theorem 形式化说明 ASV 与 E-value 的数学关系。Appendix B.20 Table 18 过于简略。共识 should-fix。\"\n    action_items:\n      - round: 13\n        action: \"Appendix 新增 ASV vs E-value/Partial R² 对比表（含 Topology dependence 行）\"\n        assigned_to: agent\n        status: in_progress\n      - round: 14\n        action: \"正文增加 Remark 或 Proposition 形式化说明 ASV 与 E-value 的数学结构区别\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 13\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"Section 4.4 已解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-Q4 追问机制。R1 AGREE 并给出可能解释（M-bias 误分类是保护性的，PPI++ 移除保护性衰减）。论文应明确说明。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 4.5 已包含机制解释（'misclassification attenuates the spurious M-bias path, and PPI++ removes this protective attenuation'）。可能已充分缓解。\"\n    action_items:\n      - round: 13\n        action: \"Section 4.5 明确解释 PPI++ 对 M-bias 有害的机制（移除保护性衰减）\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11：R1 W1 再次提出。R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：General case 15-17% 违反仍是已知限制。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W2 再次提出：15-17% 失败率（Sparse DGP 24.2%）在正文中讨论不足。R2 AGREE 并建议给出综合 coverage analysis。共识 should-fix。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W2 再提（critical）。R2 AGREE 但补充 NLP-realistic DGP 的 sign failure rate 仅 0.07%（Appendix B.13 Table 12），15-23% 出现在 independent/near-proportional 设置。Director 采纳 R2 降级为 should-fix。\"\n    action_items:\n      - round: 13\n        action: \"Method section 新增 15-17% 效应大小讨论 + ≥97% sign preservation + CSS 合理性论证\"\n        assigned_to: agent\n        status: in_progress\n      - round: 14\n        action: \"正文增加比例效应直觉解释 + 实践者如何用观测数据近似评估此条件\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R4-W6 合并。R2-W3 + R1 AGREE：需形式化对比表。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R4-W6 合并处理。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被 R11 两位 Reviewer 赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加 Collider amplification 脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论 PPI++ 对 M-bias 有害。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：exposure/IV 的 CI 跨界是拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧→R2 REBUT 成功：排名稳定性比绝对值更重要。Director 降为 minor。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 R1-Q4 间接涉及：δ* 阈值选择敏感性，跨阈值排序稳定性未验证。R2 AGREE。minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。ClinicalBERT ASV 稳定性被 R1-Q5 间接涉及，R2 指出 Appendix B.11 Table 9 已验证排名稳定性。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"R11 未再提及。Algorithm 1 整体被两位 Reviewer 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级为 should-fix。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出。Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W1 + R2-W2 再次提出。Director 维持 should-fix。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W1 (critical) + R2-W3 (should-fix)。R2 成功 REBUT R1 的 critical 评级：偏差表达式（Eqs 1-5）和符号保持（Props 1-6）均对一般 K 证明，仅 Theorem 1 限于 K=2。Director 采纳 R2 降级为 should-fix。共识：Algorithm 1 应显式声明对 Conjecture 1 的依赖。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"正文讨论 Conjecture 1 失效时对 ASV 实践指导的影响\"\n        assigned_to: agent\n        status: in_progress\n      - round: 13\n        action: \"Abstract 明确区分 K=2 formal guarantees 和 K≥3 numerical evidence\"\n        assigned_to: agent\n        status: in_progress\n      - round: 14\n        action: \"Algorithm 1 添加显式声明：ASV 阈值有效性依赖 Conjecture 1，失效时误差上界为 ε<0.06\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R2 成功 REBUT severity。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：General case 15-17% violation 是已知限制。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R6-M3 合并。R1-W2 再提。R2 AGREE + 建议综合 coverage analysis。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R6-M3 合并。R2 补充 NLP-realistic 0.07% sign failure rate。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"分歧：R2 认为与 E-value 同构，R1 REBUT。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：sign-flip ASV 和 N* 是新贡献。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 与 R4-W6 合并。形式化对比不足是共识。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R4-W6 合并。共识 should-fix。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"均匀 ε 局限。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R1 新增：stress test 仅随机扰动，未测结构化违反。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 R1 评 must-fix，R2 评 should-fix。\"\n      - round: 13\n        reviewers: [R2]\n        note: \"R13 R2-W7 minor。Section 3.1 已有条件讨论 + stress test。改善明显。降为 minor。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W6 再提。R2 AGREE 但指出已有 B.5/B.6/B.16 三层验证。共识 minor。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 12\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：拓扑特异问题。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 分歧 → R2 REBUT 成功。Director 降为 minor。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。可能已充分缓解。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用 ding_vanderweele2016。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识降级。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 NEW-1 和 R8-C2 讨论。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 合并到 R6-M3 和 NEW-1。R2 建议综合 coverage analysis。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 合并到 R6-M3 和 NEW-1。NLP-realistic 0.07% 是新数据点。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"需 Section 3.1 加线性 SEM 动机。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"主文整合 logistic 结果不足。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识：Appendix B.6/B.13 logistic 验证充分但正文引用不足。已添加。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R1-W4 + R2-W1 再次提出。plim 脚注和 FWL 内联定义已添加。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W3 再提。R2 REBUT：Appendix B.7 Table 8 已验证 logistic 下符号保持（|ΔSF_r|<0.02）。R1 混淆了 FWL invariance 失效（校正限制）与符号保持（理论结果）。Director 采纳 R2：符号保持已在 logistic 下验证，线性 SEM 限制降为 minor。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 12\n        action: \"Section 4.5 增加 logistic DGP 总结 + 引用 Appendix B.13\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 加 1-2 段直觉性文字解释 plim、FWL 分解、残差化\"\n        assigned_to: agent\n        status: in_progress\n      - round: 13\n        action: \"Section 4.5 精确限定 FWL invariance 仅适用于 covariate topologies，exposure 在 logistic 下不成立\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 已包含 proof obstacle 解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 共识。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-Q1 追问具体障碍。R1 AGREE 指出 Appendix A.4 已部分回答。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-Q1 + R2 AGREE。K=2 依赖 perspective function 凸性 + 单变量参数化；K≥3 参数空间变多维，凸性不再直接适用。两位 Reviewer 共识应在正文更明确说明。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"R1 REBUT 成功。Introduction 措辞准确且有事实支撑。\"\n    resolution_round: 12\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 合并到 R1-W3。共识：不影响核心贡献。\"\n      - round: 13\n        reviewers: [R1]\n        note: \"R13 合并到 R1-W3。R2 REBUT。Director 降为 minor。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 合并到 R1-W3。共识 minor。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被 R11 赞为 S5/S6 strength，可操作性获认可。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增强论文对 EMNLP 应用导向读者的说服力。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12：ClinicalBERT 案例最接近端到端验证。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。Section 4.5 已包含 ClinicalBERT 提及。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 4.5 已引用 ClinicalBERT（p.8: 'ClinicalBERT validation (Appendix B.3) confirms FWL invariance in clinical NLP'）。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 14\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：增加 3-4 句直觉语言解释。\"\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再次提出（R2-W3）。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 R2-W1 + R1 AGREE。plim 脚注和 FWL 内联定义已添加但 R2 认为仍不充分。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2-W2 再提。R1 REBUT——目标读者应具备 CI 基础，建议降为 minor。Director 判定：R1 有理（目标读者应知道 plim/FWL），但 EMNLP 受众广泛，保持 should-fix（低优先级）。\"\n    action_items:\n      - round: 12\n        action: \"Section 3.1/3.2 增加 plim 和 FWL 直觉解释\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 需更充分的直觉性解释段落\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"EXP-2 完成：K=3/5/10 × 7 topologies。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 14\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R12 未单独提出。Section 4.2 已有 practitioners 指导句。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1-W4 再提（IV 替代方案缺失）。R2 AGREE。共识 should-fix：论文标记 IV 为 'maximally fragile' 后仅给消极建议（'不要校正'），未提供积极替代方案（bounds approach、robust IV）。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 已添加。\"\n    resolution_round: 13\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文 Section 5 (Conclusion) 溢出至 p9，违反 EMNLP 2026 的 8 页限制\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩，视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语（plim/FWL）对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"plim 首次使用加脚注 + FWL 首次使用加内联解释。\"\n      - round: 13\n        reviewers: [R1, R2]\n        note: \"R13 修复已部分生效。R2-W1 仍评 must-fix。与 R11-W2 合并。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R11-W2 合并。R1 REBUT 建议降为 minor。Director 保持 should-fix（低优先级）。\"\n    action_items:\n      - round: 12\n        action: \"plim 脚注 + FWL 内联定义\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"Section 3.1 加直觉段落（超越单纯定义）\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 均已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: minor\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果，适用条件未标注\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"Algorithm 1 caption 已添加 K=3 calibration 注释。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2-W7 再提。R1 AGREE。共识 minor：阈值应标明为参考值，实践者需根据场景校准。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 和 Figure 7 视觉问题\"\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n\n  # === Round 13 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract、Section 4.2、Appendix B.4 之间存在 factual 不一致\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"三处统一：Abstract用empirical configs限定，Section 4.2用mean diagonal as low as 0.45限定，Appendix B.4用near-zero under empirical conditions。\"\n    resolution_round: 14\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑（M-bias, front-door, IV）缺少 NLP 应用场景示例\"\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [R2]\n        note: \"R2-W5 提出。R1 部分 AGREE 但建议降为 minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 3.2 已为 M-bias 和 front-door 添加 NLP 场景（'annotator expertise and topic difficulty'、'sentiment labels affect user engagement'）。\"\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 新发现的缺失引用\"\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [R2]\n        note: \"R2 提出 3 篇。Director：Imai et al. (2010) 和 Pryzant et al. (2021) 建议引用。\"\n      - round: 14\n        reviewers: [R2]\n        note: \"R14 R2 确认 Imai et al. 2010 和 Pryzant et al. 2021 均已引用（Related Work p.3）。无关键遗漏。\"\n\n  - id: R13-CRIT1\n    category: soundness\n    severity: critical\n    summary: \"Limitations 中 diagonal accuracy 范围错误（0.61-0.83 → 应为 0.45-0.81）\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"0.45-0.81 与 updated_empirical_results.json 实际数据 (0.453-0.809) 一致。Abstract 同步。\"\n    resolution_round: 14\n\n  # === Round 14 新发现 ===\n\n  - id: R14-W1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 的 Yes/Yes*/No 三级标注不够直观，需查看脚注才能理解\"\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R2-W6 提出。R1 AGREE。共识 minor：可改用 'Conditional' 或在 Table 1 caption 中解释 Yes* 含义。\"\n\n  - id: R14-W2\n    category: method\n    severity: should-fix\n    summary: \"IV 拓扑被标记为 maximally fragile 后缺少积极替代方案讨论\"\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R1-W4 提出。R2 AGREE。Algorithm 1 仅给消极建议（不校正），未讨论 bounds approach、robust IV、two-sample IV 等替代策略。共识 should-fix。\"\n\n  - id: R14-W3\n    category: presentation\n    severity: should-fix\n    summary: \"混淆矩阵 C 的可获得性——整个框架假设 C 已知或可估计，但获取准确 C 需 gold-standard 标签\"\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [R2]\n        note: \"R2 在 Limitations 完整性评估中提出。C 的估计是 chicken-and-egg 问题——需 gold labels 来估计 C，但如果有足够 gold labels 则不需要 LLM 标注。Limitations 应提及。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-23T10:54:07.988565+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 35637}, \"error\": \"\"}"}

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

_source line 1158 · 2026-05-23T10:57:05.136462+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# Round 14 审稿报告\n\n**论文**: \"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性 + 完整性）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文研究 K-class LLM 标注误差在 7 种 canonical DAG 拓扑下的因果推断偏差传播。三个贡献：(1) 多分类偏差分类法——推导 7 种拓扑的偏差表达式（Eqs 1–5, 对一般 K），证明 confounding/collider 的符号保持（Propositions 1–6），构造 exposure/IV 的符号反转反例；(2) ASV 灵敏度诊断框架——证明 K=2 envelope monotonicity（Theorem 1），K≥3 数值验证（Conjecture 1, ε<0.06），定义三种互补 ASV 度量；(3) 校正指导——证明 FWL invariance 导致矩阵校正对 4 种协变量拓扑无效（负面结果）。通过 MC 模拟（161 scenarios, 1.6% MAPE）、3 个 NLP 数据集（23 个 LLM 配置）和 ClinicalBERT 案例验证。\n\n---\n\n## Strengths\n\n**S1. 系统性范围覆盖前所未有。** 首个 K-class × 7 topology 的统一标注误差传播分析。Prior work 仅覆盖 1–4 种拓扑（Lee & Wood-Doughty 2024 仅 confounding；TeBlunthuis et al. 2024 限于 K=2, 4 DAGs）。K≥3 揭示定性新现象：exposure 下 83.4% 符号反转，而 K=2 时结构上不可能。[R1 S1, R2 S1 共识]\n\n**S2. 三级证据层次的科学诚实性。** 论文明确区分 proved（Proposition 1, Theorem 1）、numerically verified（Observation 1, Numerical Verifications 1–2）和 conjectured（Conjecture 1）。这种分层在同类论文中不常见，是方法论美德。[R1 S2]\n\n**S3. 符号保持证明技术正确。** R1 逐步验证了核心推导：Confounding 的 Cauchy-Schwarz 论证链、Collider 的 Berkson attenuation、Exposure 的 K=3 反例构造。Propositions 1–6 对一般 K 成立（非仅 K=2）。[R1 S3]\n\n**S4. FWL invariance 负面结果新颖且有实践价值。** 证明矩阵校正对 4 种协变量拓扑无效（列空间保持论证简洁正确），直接帮助实践者避免无效操作。OLS 和 logistic 下均验证（Table 5, Table 13）。[R1 S5, R2 S3 共识]\n\n**S5. 多层次验证流水线完整。** 解析推导 → MC 模拟（161 scenarios, N=10,000）→ 实证 LLM 混淆矩阵（23 配置 × 3 数据集）→ ClinicalBERT 案例（Appendix B.3）。210 种校正配置 × 6 方法。[R1 S4, R2 S4 共识]\n\n**S6. Algorithm 1 具有可操作性。** 三步走决策流程（assess risk → select correction → FWL warning）将理论直接转化为 NLP 从业者工具。[R2 S5]\n\n---\n\n## Weaknesses\n\n### Should-Fix\n\n**W1. ASV 与 E-value 的形式化对比缺失。** [R2-W1, R1 AGREE]\n- Section 3.3 将 ASV 定位为 \"analogous to E-values\"，Appendix B.20 Table 18 提供对比表但过于简略。全文无 proposition 或 theorem 形式化说明：(a) ASV 在何种条件下退化为 E-value；(b) K×K confusion matrix 参数化与 risk-ratio 参数化的数学区别；(c) sign-flip ASV 无法被 E-value 自然扩展的结构性原因。\n- **影响**：如果 ASV 仅是 E-value 的 re-parameterization，方法论贡献被显著削弱。\n- **建议**：正文增加 Remark 或 Proposition 形式化说明核心区别。\n- **跨轮追踪**：R4-W6 → R6-W2 → R8-W1 → R11 → R12 → R13 → R14。连续 8 轮提出，论文虽调整了 ASV 定位（framework → diagnostics）并添加了 Table 18，但形式化对比仍缺失。\n\n**W2. Conjecture 1 未证明但被 Algorithm 1 实质性使用。** [R1-W1, R2-W3, 双方 AGREE]\n- Theorem 1（envelope monotonicity）仅在 K=2 + proportional effects 下证明。K≥3 降级为 Conjecture 1（30,000 matrices 数值验证, ε<0.06）。Algorithm 1 的 ASV 阈值判断隐式依赖 envelope monotonicity。\n- **重要澄清（R2 成功 REBUT R1 的 critical 评级）**：论文的 \"Multi-Class\" 标题由偏差表达式（Eqs 1–5, 一般 K）+ 符号保持定理（Propositions 1–6, 一般 K）支撑，非仅由 Theorem 1 支撑。因此此问题影响 ASV 工具的可靠性，但不动摇核心理论贡献。\n- **建议**：(a) Algorithm 1 添加显式声明\"ASV 阈值有效性依赖 Conjecture 1，失效时误差上界 ε<0.06\"；(b) 讨论 K≥3 证明的数学障碍（K=2 依赖 perspective function 凸性 + 单变量参数化；K≥3 参数空间变多维，凸性不再直接适用）；(c) 讨论 ε=0.06 在治疗效应估计中的具体含义。\n- **跨轮追踪**：R8-C1 → R9-M1 → R11 → R12 → R13 → R14。\n\n**W3. 比例效应条件 (f=λg) 限制性未充分探讨。** [R1-W2, R2 AGREE with nuance]\n- Appendix B.13 报告一般 DGP 下 15–17% failure rate（Sparse DGP 24.2%），但 NLP-realistic DGP 的 sign failure rate 仅 0.07%（R2 补充）。论文未刻画何种结构条件下比例效应成立/失败，实践者无法判断自身 DGP 是否满足。\n- **Director 判定**：R1 标记 critical 过重。NLP-realistic 场景 0.07% failure rate 表明该条件在目标应用中通常满足。降级为 should-fix。\n- **建议**：(a) 给出比例效应的直觉解释；(b) 讨论实践者如何用观测数据近似评估此条件；(c) 正文提及 NLP-realistic 0.07% vs general 15-17% 的对比。\n- **跨轮追踪**：R6-M3 → R8-C2 → R9-C1 → R11 → R12 → R13 → R14。\n\n**W4. 对 EMNLP 读者的可及性不足。** [R2-W2, R1 部分 REBUT]\n- Section 3.1–3.2 的 plim、FWL decomposition 等计量经济学术语对 EMNLP 广泛读者不友好。plim 脚注和 FWL 内联定义已添加（R12 修复），但缺少直觉性解释段落。\n- **Director 判定**：R1 有理——目标读者（使用 LLM 标注进行因果推断的 NLP 研究者）应具备基本 CI 背景。但 EMNLP 受众广泛，增加 NLP running example 会显著提升可及性。保持 should-fix（低优先级）。\n- **建议**：Section 3.1 增加 1 个具体 NLP 场景（如情感分类作为 treatment variable）串联偏差表达式推导。\n- **跨轮追踪**：R9-C2 → R11-W2 → R12-W1 → R13 → R14。\n\n**W5. IV 拓扑被标记为 maximally fragile 后缺少替代方案讨论。** [R1-W4, R2 AGREE]\n- IV 被排除于 Conjecture 1 和 ASV 单调性分析之外（52.6% sign reversal under Dirichlet prior）。Algorithm 1 仅给消极建议（\"不要校正\"），未提供积极替代方案。\n- **建议**：讨论 IV 设计中应对标注误差的替代策略（bounds approach、robust IV、two-sample IV）。\n- **新发现**（R14 首次作为独立 issue 提出）。\n\n### Minor\n\n**W6. Abstract 数字密度过高。** [R2-W5, R1 AGREE] 10+ 个具体数字，信息过载。建议保留 3–4 个最关键数字。跨轮追踪：R3-NEW-4 → R8 → R11 → R12 → R13 → R14。\n\n**W7. Table 1 的 Yes/Yes*/No 标注不够直观。** [R2-W6, R1 AGREE] 需查看脚注理解 Yes* 含义。建议改用 \"Conditional\" 或在 caption 中直接解释。\n\n**W8. Algorithm 1 阈值过于具体化。** [R2-W7, R1 AGREE] 来自特定 MC 设置的阈值可能不适用于其他 DGP。建议标明为参考值并建议实践者根据场景校准。\n\n**W9. 混淆矩阵 C 的可获得性是 chicken-and-egg 问题。** [R2 新发现] 框架假设 C 已知或可估计，但获取准确 C 需 gold-standard 标签。Limitations 应提及。\n\n**W10. 实证验证仅覆盖 open-weight 模型。** [R1-W5, R2 AGREE] 4 个模型（7B–235B），无商业模型（GPT-4, Claude），无 ordinal 任务。核心贡献是理论性的，不依赖特定模型，但一般性声明应降低力度。跨轮追踪：R1-W3 → R9-S3 → R11 → R12 → R13 → R14。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Conjecture 1 的未证明状态是 soundness concern**：两位 Reviewer 独立识别此问题（R1-W1, R2-W3），交叉回应中双方确认。Algorithm 1 应显式声明对 Conjecture 1 的依赖。\n2. **ASV vs E-value 形式化对比缺失削弱方法论贡献**：连续 8 轮提出，双方持续 AGREE。\n3. **FWL invariance 是真正新颖且有实践价值的负面结果**：双方作为 top strength 识别（R1-S5, R2-S3）。\n4. **三级证据层次（proved/verified/conjectured）是科学诚实的体现**：双方赞赏（R1-S2, R2 在交叉回应中 AGREE）。\n5. **格式合规**：8 页限制 ✅，匿名性 ✅，Limitations 位置 ✅，References 格式 ✅。\n6. **相关工作覆盖完整**：无关键遗漏。Imai et al. (2010), Pryzant et al. (2021), Feder et al. (2022) 等均已引用。\n\n## Reviewer Divergence [REBUT]\n\n1. **R1-W1 severity（Theorem 1 K=2 only = critical?）**\n   - R1：core claim 在 multi-class 下未证明，标题与证明范围落差是 critical。\n   - R2 REBUT：偏差表达式（Eqs 1–5）和符号保持（Props 1–6）均对一般 K 证明。仅 Theorem 1（monotonicity）限于 K=2。\"Multi-Class\" 标题由前两者支撑。\n   - **Director 裁定**：R2 rebuttal 成立。降级为 should-fix。\n\n2. **R1-W3（线性 SEM 下 sign preservation 未在非线性模型验证？）**\n   - R1：符号保持在非线性模型下未验证。\n   - R2 REBUT：Appendix B.7 Table 8 已验证 logistic 下 |ΔSF_r| < 0.02。R1 混淆了 FWL invariance 失效（校正方法限制）与符号保持（理论结果）。\n   - **Director 裁定**：R2 rebuttal 成立。R1 的具体 claim 被事实纠正。线性 SEM 限制降为 minor。\n\n3. **R2-W4（EMNLP venue fit 不足？）**\n   - R2：核心贡献是纯因果推断方法论，NLP 连接通过应用域建立。\n   - R1 REBUT：问题直接来自 NLP 实践（7 篇引用中 5 篇来自 *ACL），数据/模型均为 NLP，Algorithm 1 直接针对 NLP 研究者。先例：Feder et al. (2022) TACL, Keith et al. (2020) ACL。\n   - **Director 裁定**：R1 rebuttal 成立。Venue fit 不构成 weakness。\n\n4. **R2-W2（可及性 = should-fix?）**\n   - R2：plim/FWL 对 EMNLP 读者不友好，should-fix。\n   - R1 REBUT：目标读者应具备 CI 基础，建议降为 minor。\n   - **Director 裁定**：保持 should-fix 但降低优先级。EMNLP 受众广泛，增加 NLP running example 有价值。\n\n---\n\n## Questions\n\n**Q1** [R1-Q2, R2 AGREE]: Proposition 3 worst-case bound B（Eq. 16）依赖 DGP 参数（Var(g(A)), Var(f(A))）。实践者通常不知道真实 DGP 参数——如何从观测数据估计 B 的上界以判断符号保持是否成立？\n\n**Q2** [R1-Q3, R2 AGREE]: Table 5（Appendix B.7）logistic 下矩阵校正产生 ~7% bias reduction。对高风险应用（如医疗因果推断），推荐的 non-matrix-based 替代方案是什么？\n\n**Q3** [R1-Q4, R2 AGREE]: Appendix B.13 的 15–17% 单调性失败率是否集中在特定 confusion matrix 结构（如高度非对角占优）？如果失败集中在特定区间，实践者可提前排除。\n\n**Q4** [R2-Q4, R1 AGREE]: DAG 拓扑未知时 Algorithm 1 如何使用？Limitations 简述 \"apply under each candidate topology\"，但应更显著地集成到 Algorithm 1 中。\n\n**Q5** [R1-Q5, R2 AGREE]: ClinicalBERT 案例（Appendix B.18）OR=0.89 对混淆矩阵选择的敏感性如何？不同合理混淆矩阵下的 OR 分布（bootstrap/sensitivity analysis）会增强可信度。\n\n---\n\n## Missing References\n\n两位 Reviewer 均确认相关工作覆盖完整。Imai, Keele & Tingley (2010), Pryzant et al. (2021), Feder et al. (2022), Wood-Doughty et al. (2018), VanderWeele & Ding (2017), Keith et al. (2020) 等关键文献均已引用。\n\nR2 提到一篇可能相关的近期工作（arXiv:2602.15730, \"Causal Effect Estimation with Latent Textual Treatments\"），但聚焦 latent treatment 而非标注误差传播，非关键遗漏。\n\n无关键缺失引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。项目配置未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：Agent 错误——rate limit 导致视觉审查 Agent 退出（\"You've hit your limit · resets 4pm (UTC)\"）。未能完成 PDF 渲染和逐页检查。\n\n**替代检查（Director 手动）**：\n- PDF 共 9 页（p1–8 正文 + Limitations，p9 起 References）\n- Figure 1（p.3）：7 种 DAG 拓扑，清晰可读\n- Figure 2（p.7）：Bias distributions，7 panel，尺寸偏小但可辨\n- Figure 3（p.8）：F1 vs bias 散点图，标注清晰\n- Table 1（p.7）：排版整洁，与 Figure 2 共享 p.7\n- Appendix 23 页，排版规范\n\n**用户可重新触发视觉审查**：本报告不因视觉审查缺失而推迟。\n\n---\n\n## Overall Assessment\n\n### 评分（EMNLP 2026 ARR 标准）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | 3.5/5 | 在覆盖范围内（偏差表达式一般 K、符号保持一般 K、Theorem 1 限 K=2）理论严谨。Conjecture 1 的未证明性和比例效应限制是主要 concern，但 NLP-realistic 场景影响有限（0.07% sign failure）。R1 验证了核心证明的技术正确性。 |\n| **Excitement** | 3.5/5 | 问题重要且时效性强（LLM 标注替代人工标注用于 CSS 因果推断）。7 拓扑统一分析新颖；FWL invariance 负面结果实用价值高。但线性 SEM + K=2 证明范围限制了即时实践影响。 |\n| **Reproducibility** | 4.0/5 | Appendix 23 页提供完整推导、MC 参数、DGP 设置。Algorithm 1 可操作。承诺代码公开。唯一缺失：LLM 标注的 prompt 模板未提供。 |\n| **Overall** | **3.5/5 (Borderline Conference)** | 两位 Reviewer 独立评分一致。技术贡献扎实（统一框架 + FWL invariance + 符号保持证明），验证流水线完整。主要 concern：ASV vs E-value 形式化对比缺失（连续 8 轮）、Conjecture 1 未证明但被 Algorithm 1 使用、比例效应限制性需更好论证。若 W1–W3 解决，可达 4.0 (Conference)。 |\n| **Confidence** | 4/5 | R1 逐步验证了核心证明（Propositions 1–7, Theorem 1, FWL invariance）。R2 检查了格式合规、引用完整性、novelty 定位。交叉回应纠正了 R1 的两个 factual error（logistic sign preservation 已验证、Multi-Class 标题由偏差表达式 + 符号保持支撑）。 |\n\n### 一句话总结\n\n技术上严谨的因果推断工作（K-class × 7 topology 统一分析 + FWL invariance 负面结果 + 多层次验证），但 ASV 方法论贡献的独立性论证（vs E-value）和 K≥3 ASV 的理论基础（Conjecture 1）是 Borderline Conference 与 Conference 的关键区别因素。\n\n### 距 Conference (4.0) 的差距\n\n1. **ASV vs E-value 形式化对比**（W1）：增加 Remark/Proposition 说明数学结构区别 → 澄清方法论贡献独立性\n2. **Algorithm 1 对 Conjecture 1 的依赖声明**（W2）：显式说明 + 讨论失效后果 → 增强用户信任\n3. **比例效应的直觉解释和诊断指南**（W3）：正文提及 NLP-realistic 0.07% + 实践者评估指南 → 增强可操作性\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 第 2 段 \"The transition at K≥3 is not gradual but structural\" 的叙述有力且准确。\n- 第 3 段 F₁ vs bias 的论证（Spearman ρ=−0.10, p=0.45）有效地建立了 topology > annotator quality 的核心 insight。但 power=0.57 意味着检测 |ρ|≥0.3 的能力有限——如果真实 ρ 在 0.1–0.2 之间，当前样本量无法区分。\n\n### Section 3 (Method)\n- Definition 1 (non-differential misclassification) 清晰，附有 NLP 场景直觉解释（p.4）。\n- Section 3.1 \"Notation conventions\" 段（p.3-4）的 plim 脚注和 FWL 内联定义是 R12 修复的成果，有效但仍偏技术性。\n- Conjecture 1（p.6）的 ε=0.06 容差——建议明确说明\"这意味着在最坏情况下，ASV 可能低估实际偏差严重程度，但误差不超过 6% 的最大偏差量\"。\n- M-bias 和 front-door 已添加 NLP 场景示例（annotator expertise/topic difficulty, sentiment → engagement → revenue），有效增强可理解性。\n\n### Section 4 (Experiments)\n- Table 1（p.7）呈现 7 种拓扑的关键属性，设计紧凑有效。Yes* 标注需改进（W7）。\n- Figure 3（p.8）F₁ vs bias 散点图清晰展示 topology > F₁ 的 insight。\n- Section 4.5 FWL invariance 段已包含 \"Under linear OLS\" 限定和 logistic 下 < 0.065% 的结果——准确。\n- Section 4.5 已提及 ClinicalBERT 验证（\"Appendix B.3 confirms FWL invariance in clinical NLP\"），解决了 R11-W1。\n- PPI++ 对 M-bias 有害的机制解释（\"misclassification attenuates the spurious M-bias path, and PPI++ removes this protective attenuation\"）清晰。\n\n### Section 5 + Limitations (p.8)\n- Conclusion 简洁有效（4 句话）。\n- Limitations 覆盖 6 点（non-differential, linear SEM, ASV parameterization, DAG uncertainty, FWL under logistic, LLM 配置范围），合理但应增加混淆矩阵 C 的可获得性问题（W9）。\n- \"Code and data will be released\" 承诺 ✅。\n\n### Appendix\n- 23 页 appendix 详尽覆盖完整证明链、补充实验、stress tests。关键表格：Table 2（sign conditions summary, p.20）、Table 5（logistic FWL, p.22）、Table 7-8（stress test, p.23-24）、Table 10（envelope violations, p.26）、Table 12（proportional effects, p.28）、Table 18（ASV vs E-value, p.30）。\n- Table 18 是 ASV vs E-value 对比表但过于简略——这是 W1 的核心位置。\n\n### 格式\n- 正文 8 页 ✅（Section 5 + Limitations 完全在 p.8 内）\n- ACL [review] 模板 ✅\n- 匿名 \"Anonymous ACL submission\" ✅\n- 无代码链接或 deanonymization 风险 ✅\n- References 格式一致 ✅\n"
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
    "report": "# Round 14 审稿报告\n\n**论文**: \"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性 + 完整性）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文研究 K-class LLM 标注误差在 7 种 canonical DAG 拓扑下的因果推断偏差传播。三个贡献：(1) 多分类偏差分类法——推导 7 种拓扑的偏差表达式（Eqs 1–5, 对一般 K），证明 confounding/collider 的符号保持（Propositions 1–6），构造 exposure/IV 的符号反转反例；(2) ASV 灵敏度诊断框架——证明 K=2 envelope monotonicity（Theorem 1），K≥3 数值验证（Conjecture 1, ε<0.06），定义三种互补 ASV 度量；(3) 校正指导——证明 FWL invariance 导致矩阵校正对 4 种协变量拓扑无效（负面结果）。通过 MC 模拟（161 scenarios, 1.6% MAPE）、3 个 NLP 数据集（23 个 LLM 配置）和 ClinicalBERT 案例验证。\n\n---\n\n## Strengths\n\n**S1. 系统性范围覆盖前所未有。** 首个 K-class × 7 topology 的统一标注误差传播分析。Prior work 仅覆盖 1–4 种拓扑（Lee & Wood-Doughty 2024 仅 confounding；TeBlunthuis et al. 2024 限于 K=2, 4 DAGs）。K≥3 揭示定性新现象：exposure 下 83.4% 符号反转，而 K=2 时结构上不可能。[R1 S1, R2 S1 共识]\n\n**S2. 三级证据层次的科学诚实性。** 论文明确区分 proved（Proposition 1, Theorem 1）、numerically verified（Observation 1, Numerical Verifications 1–2）和 conjectured（Conjecture 1）。这种分层在同类论文中不常见，是方法论美德。[R1 S2]\n\n**S3. 符号保持证明技术正确。** R1 逐步验证了核心推导：Confounding 的 Cauchy-Schwarz 论证链、Collider 的 Berkson attenuation、Exposure 的 K=3 反例构造。Propositions 1–6 对一般 K 成立（非仅 K=2）。[R1 S3]\n\n**S4. FWL invariance 负面结果新颖且有实践价值。** 证明矩阵校正对 4 种协变量拓扑无效（列空间保持论证简洁正确），直接帮助实践者避免无效操作。OLS 和 logistic 下均验证（Table 5, Table 13）。[R1 S5, R2 S3 共识]\n\n**S5. 多层次验证流水线完整。** 解析推导 → MC 模拟（161 scenarios, N=10,000）→ 实证 LLM 混淆矩阵（23 配置 × 3 数据集）→ ClinicalBERT 案例（Appendix B.3）。210 种校正配置 × 6 方法。[R1 S4, R2 S4 共识]\n\n**S6. Algorithm 1 具有可操作性。** 三步走决策流程（assess risk → select correction → FWL warning）将理论直接转化为 NLP 从业者工具。[R2 S5]\n\n---\n\n## Weaknesses\n\n### Should-Fix\n\n**W1. ASV 与 E-value 的形式化对比缺失。** [R2-W1, R1 AGREE]\n- Section 3.3 将 ASV 定位为 \"analogous to E-values\"，Appendix B.20 Table 18 提供对比表但过于简略。全文无 proposition 或 theorem 形式化说明：(a) ASV 在何种条件下退化为 E-value；(b) K×K confusion matrix 参数化与 risk-ratio 参数化的数学区别；(c) sign-flip ASV 无法被 E-value 自然扩展的结构性原因。\n- **影响**：如果 ASV 仅是 E-value 的 re-parameterization，方法论贡献被显著削弱。\n- **建议**：正文增加 Remark 或 Proposition 形式化说明核心区别。\n- **跨轮追踪**：R4-W6 → R6-W2 → R8-W1 → R11 → R12 → R13 → R14。连续 8 轮提出，论文虽调整了 ASV 定位（framework → diagnostics）并添加了 Table 18，但形式化对比仍缺失。\n\n**W2. Conjecture 1 未证明但被 Algorithm 1 实质性使用。** [R1-W1, R2-W3, 双方 AGREE]\n- Theorem 1（envelope monotonicity）仅在 K=2 + proportional effects 下证明。K≥3 降级为 Conjecture 1（30,000 matrices 数值验证, ε<0.06）。Algorithm 1 的 ASV 阈值判断隐式依赖 envelope monotonicity。\n- **重要澄清（R2 成功 REBUT R1 的 critical 评级）**：论文的 \"Multi-Class\" 标题由偏差表达式（Eqs 1–5, 一般 K）+ 符号保持定理（Propositions 1–6, 一般 K）支撑，非仅由 Theorem 1 支撑。因此此问题影响 ASV 工具的可靠性，但不动摇核心理论贡献。\n- **建议**：(a) Algorithm 1 添加显式声明\"ASV 阈值有效性依赖 Conjecture 1，失效时误差上界 ε<0.06\"；(b) 讨论 K≥3 证明的数学障碍（K=2 依赖 perspective function 凸性 + 单变量参数化；K≥3 参数空间变多维，凸性不再直接适用）；(c) 讨论 ε=0.06 在治疗效应估计中的具体含义。\n- **跨轮追踪**：R8-C1 → R9-M1 → R11 → R12 → R13 → R14。\n\n**W3. 比例效应条件 (f=λg) 限制性未充分探讨。** [R1-W2, R2 AGREE with nuance]\n- Appendix B.13 报告一般 DGP 下 15–17% failure rate（Sparse DGP 24.2%），但 NLP-realistic DGP 的 sign failure rate 仅 0.07%（R2 补充）。论文未刻画何种结构条件下比例效应成立/失败，实践者无法判断自身 DGP 是否满足。\n- **Director 判定**：R1 标记 critical 过重。NLP-realistic 场景 0.07% failure rate 表明该条件在目标应用中通常满足。降级为 should-fix。\n- **建议**：(a) 给出比例效应的直觉解释；(b) 讨论实践者如何用观测数据近似评估此条件；(c) 正文提及 NLP-realistic 0.07% vs general 15-17% 的对比。\n- **跨轮追踪**：R6-M3 → R8-C2 → R9-C1 → R11 → R12 → R13 → R14。\n\n**W4. 对 EMNLP 读者的可及性不足。** [R2-W2, R1 部分 REBUT]\n- Section 3.1–3.2 的 plim、FWL decomposition 等计量经济学术语对 EMNLP 广泛读者不友好。plim 脚注和 FWL 内联定义已添加（R12 修复），但缺少直觉性解释段落。\n- **Director 判定**：R1 有理——目标读者（使用 LLM 标注进行因果推断的 NLP 研究者）应具备基本 CI 背景。但 EMNLP 受众广泛，增加 NLP running example 会显著提升可及性。保持 should-fix（低优先级）。\n- **建议**：Section 3.1 增加 1 个具体 NLP 场景（如情感分类作为 treatment variable）串联偏差表达式推导。\n- **跨轮追踪**：R9-C2 → R11-W2 → R12-W1 → R13 → R14。\n\n**W5. IV 拓扑被标记为 maximally fragile 后缺少替代方案讨论。** [R1-W4, R2 AGREE]\n- IV 被排除于 Conjecture 1 和 ASV 单调性分析之外（52.6% sign reversal under Dirichlet prior）。Algorithm 1 仅给消极建议（\"不要校正\"），未提供积极替代方案。\n- **建议**：讨论 IV 设计中应对标注误差的替代策略（bounds approach、robust IV、two-sample IV）。\n- **新发现**（R14 首次作为独立 issue 提出）。\n\n### Minor\n\n**W6. Abstract 数字密度过高。** [R2-W5, R1 AGREE] 10+ 个具体数字，信息过载。建议保留 3–4 个最关键数字。跨轮追踪：R3-NEW-4 → R8 → R11 → R12 → R13 → R14。\n\n**W7. Table 1 的 Yes/Yes*/No 标注不够直观。** [R2-W6, R1 AGREE] 需查看脚注理解 Yes* 含义。建议改用 \"Conditional\" 或在 caption 中直接解释。\n\n**W8. Algorithm 1 阈值过于具体化。** [R2-W7, R1 AGREE] 来自特定 MC 设置的阈值可能不适用于其他 DGP。建议标明为参考值并建议实践者根据场景校准。\n\n**W9. 混淆矩阵 C 的可获得性是 chicken-and-egg 问题。** [R2 新发现] 框架假设 C 已知或可估计，但获取准确 C 需 gold-standard 标签。Limitations 应提及。\n\n**W10. 实证验证仅覆盖 open-weight 模型。** [R1-W5, R2 AGREE] 4 个模型（7B–235B），无商业模型（GPT-4, Claude），无 ordinal 任务。核心贡献是理论性的，不依赖特定模型，但一般性声明应降低力度。跨轮追踪：R1-W3 → R9-S3 → R11 → R12 → R13 → R14。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Conjecture 1 的未证明状态是 soundness concern**：两位 Reviewer 独立识别此问题（R1-W1, R2-W3），交叉回应中双方确认。Algorithm 1 应显式声明对 Conjecture 1 的依赖。\n2. **ASV vs E-value 形式化对比缺失削弱方法论贡献**：连续 8 轮提出，双方持续 AGREE。\n3. **FWL invariance 是真正新颖且有实践价值的负面结果**：双方作为 top strength 识别（R1-S5, R2-S3）。\n4. **三级证据层次（proved/verified/conjectured）是科学诚实的体现**：双方赞赏（R1-S2, R2 在交叉回应中 AGREE）。\n5. **格式合规**：8 页限制 ✅，匿名性 ✅，Limitations 位置 ✅，References 格式 ✅。\n6. **相关工作覆盖完整**：无关键遗漏。Imai et al. (2010), Pryzant et al. (2021), Feder et al. (2022) 等均已引用。\n\n## Reviewer Divergence [REBUT]\n\n1. **R1-W1 severity（Theorem 1 K=2 only = critical?）**\n   - R1：core claim 在 multi-class 下未证明，标题与证明范围落差是 critical。\n   - R2 REBUT：偏差表达式（Eqs 1–5）和符号保持（Props 1–6）均对一般 K 证明。仅 Theorem 1（monotonicity）限于 K=2。\"Multi-Class\" 标题由前两者支撑。\n   - **Director 裁定**：R2 rebuttal 成立。降级为 should-fix。\n\n2. **R1-W3（线性 SEM 下 sign preservation 未在非线性模型验证？）**\n   - R1：符号保持在非线性模型下未验证。\n   - R2 REBUT：Appendix B.7 Table 8 已验证 logistic 下 |ΔSF_r| < 0.02。R1 混淆了 FWL invariance 失效（校正方法限制）与符号保持（理论结果）。\n   - **Director 裁定**：R2 rebuttal 成立。R1 的具体 claim 被事实纠正。线性 SEM 限制降为 minor。\n\n3. **R2-W4（EMNLP venue fit 不足？）**\n   - R2：核心贡献是纯因果推断方法论，NLP 连接通过应用域建立。\n   - R1 REBUT：问题直接来自 NLP 实践（7 篇引用中 5 篇来自 *ACL），数据/模型均为 NLP，Algorithm 1 直接针对 NLP 研究者。先例：Feder et al. (2022) TACL, Keith et al. (2020) ACL。\n   - **Director 裁定**：R1 rebuttal 成立。Venue fit 不构成 weakness。\n\n4. **R2-W2（可及性 = should-fix?）**\n   - R2：plim/FWL 对 EMNLP 读者不友好，should-fix。\n   - R1 REBUT：目标读者应具备 CI 基础，建议降为 minor。\n   - **Director 裁定**：保持 should-fix 但降低优先级。EMNLP 受众广泛，增加 NLP running example 有价值。\n\n---\n\n## Questions\n\n**Q1** [R1-Q2, R2 AGREE]: Proposition 3 worst-case bound B（Eq. 16）依赖 DGP 参数（Var(g(A)), Var(f(A))）。实践者通常不知道真实 DGP 参数——如何从观测数据估计 B 的上界以判断符号保持是否成立？\n\n**Q2** [R1-Q3, R2 AGREE]: Table 5（Appendix B.7）logistic 下矩阵校正产生 ~7% bias reduction。对高风险应用（如医疗因果推断），推荐的 non-matrix-based 替代方案是什么？\n\n**Q3** [R1-Q4, R2 AGREE]: Appendix B.13 的 15–17% 单调性失败率是否集中在特定 confusion matrix 结构（如高度非对角占优）？如果失败集中在特定区间，实践者可提前排除。\n\n**Q4** [R2-Q4, R1 AGREE]: DAG 拓扑未知时 Algorithm 1 如何使用？Limitations 简述 \"apply under each candidate topology\"，但应更显著地集成到 Algorithm 1 中。\n\n**Q5** [R1-Q5, R2 AGREE]: ClinicalBERT 案例（Appendix B.18）OR=0.89 对混淆矩阵选择的敏感性如何？不同合理混淆矩阵下的 OR 分布（bootstrap/sensitivity analysis）会增强可信度。\n\n---\n\n## Missing References\n\n两位 Reviewer 均确认相关工作覆盖完整。Imai, Keele & Tingley (2010), Pryzant et al. (2021), Feder et al. (2022), Wood-Doughty et al. (2018), VanderWeele & Ding (2017), Keith et al. (2020) 等关键文献均已引用。\n\nR2 提到一篇可能相关的近期工作（arXiv:2602.15730, \"Causal Effect Estimation with Latent Textual Treatments\"），但聚焦 latent treatment 而非标注误差传播，非关键遗漏。\n\n无关键缺失引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。项目配置未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：Agent 错误——rate limit 导致视觉审查 Agent 退出（\"You've hit your limit · resets 4pm (UTC)\"）。未能完成 PDF 渲染和逐页检查。\n\n**替代检查（Director 手动）**：\n- PDF 共 9 页（p1–8 正文 + Limitations，p9 起 References）\n- Figure 1（p.3）：7 种 DAG 拓扑，清晰可读\n- Figure 2（p.7）：Bias distributions，7 panel，尺寸偏小但可辨\n- Figure 3（p.8）：F1 vs bias 散点图，标注清晰\n- Table 1（p.7）：排版整洁，与 Figure 2 共享 p.7\n- Appendix 23 页，排版规范\n\n**用户可重新触发视觉审查**：本报告不因视觉审查缺失而推迟。\n\n---\n\n## Overall Assessment\n\n### 评分（EMNLP 2026 ARR 标准）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | 3.5/5 | 在覆盖范围内（偏差表达式一般 K、符号保持一般 K、Theorem 1 限 K=2）理论严谨。Conjecture 1 的未证明性和比例效应限制是主要 concern，但 NLP-realistic 场景影响有限（0.07% sign failure）。R1 验证了核心证明的技术正确性。 |\n| **Excitement** | 3.5/5 | 问题重要且时效性强（LLM 标注替代人工标注用于 CSS 因果推断）。7 拓扑统一分析新颖；FWL invariance 负面结果实用价值高。但线性 SEM + K=2 证明范围限制了即时实践影响。 |\n| **Reproducibility** | 4.0/5 | Appendix 23 页提供完整推导、MC 参数、DGP 设置。Algorithm 1 可操作。承诺代码公开。唯一缺失：LLM 标注的 prompt 模板未提供。 |\n| **Overall** | **3.5/5 (Borderline Conference)** | 两位 Reviewer 独立评分一致。技术贡献扎实（统一框架 + FWL invariance + 符号保持证明），验证流水线完整。主要 concern：ASV vs E-value 形式化对比缺失（连续 8 轮）、Conjecture 1 未证明但被 Algorithm 1 使用、比例效应限制性需更好论证。若 W1–W3 解决，可达 4.0 (Conference)。 |\n| **Confidence** | 4/5 | R1 逐步验证了核心证明（Propositions 1–7, Theorem 1, FWL invariance）。R2 检查了格式合规、引用完整性、novelty 定位。交叉回应纠正了 R1 的两个 factual error（logistic sign preservation 已验证、Multi-Class 标题由偏差表达式 + 符号保持支撑）。 |\n\n### 一句话总结\n\n技术上严谨的因果推断工作（K-class × 7 topology 统一分析 + FWL invariance 负面结果 + 多层次验证），但 ASV 方法论贡献的独立性论证（vs E-value）和 K≥3 ASV 的理论基础（Conjecture 1）是 Borderline Conference 与 Conference 的关键区别因素。\n\n### 距 Conference (4.0) 的差距\n\n1. **ASV vs E-value 形式化对比**（W1）：增加 Remark/Proposition 说明数学结构区别 → 澄清方法论贡献独立性\n2. **Algorithm 1 对 Conjecture 1 的依赖声明**（W2）：显式说明 + 讨论失效后果 → 增强用户信任\n3. **比例效应的直觉解释和诊断指南**（W3）：正文提及 NLP-realistic 0.07% + 实践者评估指南 → 增强可操作性\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 第 2 段 \"The transition at K≥3 is not gradual but structural\" 的叙述有力且准确。\n- 第 3 段 F₁ vs bias 的论证（Spearman ρ=−0.10, p=0.45）有效地建立了 topology > annotator quality 的核心 insight。但 power=0.57 意味着检测 |ρ|≥0.3 的能力有限——如果真实 ρ 在 0.1–0.2 之间，当前样本量无法区分。\n\n### Section 3 (Method)\n- Definition 1 (non-differential misclassification) 清晰，附有 NLP 场景直觉解释（p.4）。\n- Section 3.1 \"Notation conventions\" 段（p.3-4）的 plim 脚注和 FWL 内联定义是 R12 修复的成果，有效但仍偏技术性。\n- Conjecture 1（p.6）的 ε=0.06 容差——建议明确说明\"这意味着在最坏情况下，ASV 可能低估实际偏差严重程度，但误差不超过 6% 的最大偏差量\"。\n- M-bias 和 front-door 已添加 NLP 场景示例（annotator expertise/topic difficulty, sentiment → engagement → revenue），有效增强可理解性。\n\n### Section 4 (Experiments)\n- Table 1（p.7）呈现 7 种拓扑的关键属性，设计紧凑有效。Yes* 标注需改进（W7）。\n- Figure 3（p.8）F₁ vs bias 散点图清晰展示 topology > F₁ 的 insight。\n- Section 4.5 FWL invariance 段已包含 \"Under linear OLS\" 限定和 logistic 下 < 0.065% 的结果——准确。\n- Section 4.5 已提及 ClinicalBERT 验证（\"Appendix B.3 confirms FWL invariance in clinical NLP\"），解决了 R11-W1。\n- PPI++ 对 M-bias 有害的机制解释（\"misclassification attenuates the spurious M-bias path, and PPI++ removes this protective attenuation\"）清晰。\n\n### Section 5 + Limitations (p.8)\n- Conclusion 简洁有效（4 句话）。\n- Limitations 覆盖 6 点（non-differential, linear SEM, ASV parameterization, DAG uncertainty, FWL under logistic, LLM 配置范围），合理但应增加混淆矩阵 C 的可获得性问题（W9）。\n- \"Code and data will be released\" 承诺 ✅。\n\n### Appendix\n- 23 页 appendix 详尽覆盖完整证明链、补充实验、stress tests。关键表格：Table 2（sign conditions summary, p.20）、Table 5（logistic FWL, p.22）、Table 7-8（stress test, p.23-24）、Table 10（envelope violations, p.26）、Table 12（proportional effects, p.28）、Table 18（ASV vs E-value, p.30）。\n- Table 18 是 ASV vs E-value 对比表但过于简略——这是 W1 的核心位置。\n\n### 格式\n- 正文 8 页 ✅（Section 5 + Limitations 完全在 p.8 内）\n- ACL [review] 模板 ✅\n- 匿名 \"Anonymous ACL submission\" ✅\n- 无代码链接或 deanonymization 风险 ✅\n- References 格式一致 ✅\n"
  }
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-23T10:57:09.405048+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4268
}
```

</details>

---


### Assistant

_source line 1160 · 2026-05-23T10:57:25.717442+00:00_

**Round 14 审稿完成。**

**最终评分：3.5 (Borderline Conference)**，两位 Reviewer 独立评分一致。

**核心发现：**
- **5 个 should-fix**：(1) ASV vs E-value 形式化对比缺失（连续 8 轮）；(2) Conjecture 1 未证明但被 Algorithm 1 实质使用；(3) 比例效应限制性需更好论证；(4) EMNLP 读者可及性；(5) IV 替代方案缺失
- **5 个 minor**：Abstract 数字密度、Table 1 标注、Algorithm 1 阈值、混淆矩阵可获得性、实证范围
- **关键分歧已解决**：R2 成功 REBUT R1 的两个 critical 评级——偏差表达式和符号保持对一般 K 已证明（非仅 K=2），logistic 下符号保持已验证。R1 成功 REBUT R2 的 venue fit 质疑。

**距 Conference (4.0) 的差距**：解决 W1（ASV vs E-value Remark）、W2（Algorithm 1 Conjecture 1 声明）、W3（比例效应直觉 + NLP-realistic 0.07%）即可。

审稿报告和 Issue Tracker 均已更新并投递。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 115

## Round 115

2 recorded events


### User

_source line 1161 · 2026-05-23T10:57:28.357847+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心判断：R1 的 6 个 Weaknesses 中我 AGREE 3 个（W2/W4/W5），部分 REBUT 2 个（W1/W6），完全 REBUT 1 个（W3）。主要分歧在于：(1) R1 将论文描述为"仅证明 K=2"过于笼统——Propositions 1-6 的符号保持对一般 K 成立；(2) R1 称符号保持在非线性模型下未验证，但 Appendix B.7 Table 8 已明确验证。Overall Assessment 维持 3.5。

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

_source line 1162 · 2026-05-23T10:57:41.023677+00:00_

审稿报告已在上一步提交完毕。

**Round 14 审稿完成。**

最终结果：**3.5/5 (Borderline Conference)**，两位 Reviewer 评分一致。

核心发现摘要：
- **5 个 should-fix**：ASV vs E-value 形式化对比缺失（连续 8 轮）、Conjecture 1 未证明但被 Algorithm 1 使用、比例效应限制性需更好论证、EMNLP 读者可及性、IV 替代方案缺失
- **4 个 minor**：Abstract 数字密度、Table 1 标注、Algorithm 1 阈值、混淆矩阵可获得性
- **距 Conference (4.0) 的关键差距**：解决 W1（ASV vs E-value）+ W2（Conjecture 1 依赖声明）+ W3（比例效应诊断）即可上调

报告和 Issue Tracker 均已更新并投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 116

## Round 116

64 recorded events


### User

_source line 1163 · 2026-05-23T11:23:04.454416+00:00_

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

_source line 1164 · 2026-05-23T11:23:10.281642+00:00_

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

_source line 1165 · 2026-05-23T11:23:10.282457+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1166 · 2026-05-23T11:23:18.364929+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
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
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1167 · 2026-05-23T11:23:18.365455+00:00_

No matching deferred tools found

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

_source line 1168 · 2026-05-23T11:23:22.181334+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-23T11:23:22.181712+00:00_



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

_source line 1170 · 2026-05-23T11:23:26.248541+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "3"
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
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1171 · 2026-05-23T11:23:26.349588+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-23T11:23:29.111362+00:00_

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

_source line 1173 · 2026-05-23T11:23:29.212208+00:00_

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

_source line 1174 · 2026-05-23T11:23:31.972887+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
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
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-23T11:23:32.023527+00:00_



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

_source line 1176 · 2026-05-23T11:23:38.700321+00:00_

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

_source line 1177 · 2026-05-23T11:23:39.103392+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1178 · 2026-05-23T11:23:39.605812+00:00_

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

_source line 1179 · 2026-05-23T11:23:41.211807+00:00_

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

_source line 1180 · 2026-05-23T11:23:42.015578+00:00_

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
19	\newtheorem{remark}{Remark}
20	
21	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
24	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
25	\graphicspath{{../../figures/paper/}}
26	
27	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{abstract}
35	
36	\input{introduction}
37	
38	\begin{figure*}[t]
39	\centering
40	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
41	\vspace{-6pt}
42	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
43	\label{fig:dag_taxonomy}
44	\end{figure*}
45	
46	\input{related_work}
47	
48	\input{method}
49	
50	% ── Figures ──
51	
52	\begin{figure*}[t]
53	\centering
54	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
55	\vspace{-6pt}
56	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
57	\label{fig:bias_distribution}
58	\end{figure*}
59	
60	\input{experiments}
61	
62	\input{conclusion}
63	
64	\bibliography{references}
65	
66	\appendix
67	\input{appendix_proofs}
68	
69	\end{document}
70	

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

_source line 1181 · 2026-05-23T11:23:42.015954+00:00_

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

_source line 1182 · 2026-05-23T11:23:43.020221+00:00_

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
…[truncated 39457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1183 · 2026-05-23T11:23:43.071367+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1184 · 2026-05-23T11:23:43.272472+00:00_

-rw-r--r-- 1 ubuntu ubuntu 921454 May 23 11:17 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf
PDF_EXISTS

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

_source line 1185 · 2026-05-23T11:23:48.241338+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Presentation Requirements

All accepted papers must be presented at the conference to appear in the proceedings, with both in-person and virtual presentation options available. Papers without at least one presenting author registered by the early regis
…[truncated 793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 8635
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-23T11:24:10.685997+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission format page limit template requirements"
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
    "query": "EMNLP 2026 ARR submission format page limit template requirements"
  }
}
```

</details>

---


### Tool call

_source line 1187 · 2026-05-23T11:24:11.238773+00:00_

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


### Tool call

_source line 1188 · 2026-05-23T11:24:12.142846+00:00_

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


### Tool call

_source line 1189 · 2026-05-23T11:24:12.344030+00:00_

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

_source line 1190 · 2026-05-23T11:24:18.117559+00:00_

Web search results for query: "EMNLP 2026 ARR submission format page limit template requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's what I found about EMNLP 2026 ARR submission format requirements:

## Format and Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. A mandatory Limitations section is required, placed after the conclusion.

## Submission Process

Both submissions of articles for review and commitment of reviewed articles to the conference will be performed via the Open Review platform.

## Important Dates

The ARR submission deadline for long and short papers is May 25, 2026, with notification of acceptance on August 20, 2026.

## Template

The official EMNLP 2026 LaTeX template uses ACL style 
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7431
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-23T11:24:18.268730+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 7029
}
```

</details>

---


### Tool result

_source line 1192 · 2026-05-23T11:24:18.269126+00:00_

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
  "elapsed_ms": 6126
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-23T11:24:18.269463+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors (equivalently, misclassification) from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, h
…[truncated 2750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 5925
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-23T11:24:24.292301+00:00_

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

_source line 1195 · 2026-05-23T11:24:24.844686+00:00_

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

_source line 1196 · 2026-05-23T11:24:25.045929+00:00_

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

_source line 1197 · 2026-05-23T11:24:25.247386+00:00_

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
17	This holds when the LLM classifies without observing the outcome---the typical CSS setup~\cite{ziems2024can}; topic-stratified confusion matrices confirm cross-group stability (Appendix~\ref{sec:nondiff_verify}). Violations arise when pretraining data encodes $A$--$Y$ associations; our stress test (Appendix~\ref{sec:nondiff_stress}) shows $<$3~pp degradatio
…[truncated 13567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-23T11:24:25.247778+00:00_

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

_source line 1199 · 2026-05-23T11:24:25.599475+00:00_

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
…[truncated 7211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1200 · 2026-05-23T11:24:25.650096+00:00_

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

_source line 1201 · 2026-05-23T11:24:25.700759+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: the binary attenuation guarantee breaks at $K \geq 3$, where exposure and IV can reverse signs while five topologies preserve them. ASVs yield a vulnerability ranking from IV (most fragile) to M-bias (immune); matrix-based corrections are provably ineffective for four covariate topologies due to FWL invariance. Code and data will be released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information; a stress test (Appendix~\ref{sec:nondiff_stress}) shows that structured violation patterns can exceed or fall below uniform predictions. Closed-form expressions are derived under $K{=}3$ linear structural equations; extensions to arbitrary $K$ and nonlinear models~\cite{schennach2020mismeasured} remain open (Appendix~\ref{sec:logistic_dgp}), though correction method rankings are stable across $K{=}3,5,10$ (Spearman $\rho \geq 0.80$, with PPI++ degrading at $K{=}10$; Appendix~\ref{sec:correction_k_sensitivity}). The ASV diagonal parameterization $C(\delta) = (1{-}\delta)I + \delta C_0$ assumes uniform degradation across categories; rare-class-specific degradation would require multi-dimensional extensions. When the true DAG is uncertain, practitioners can apply Algorithm~1 under each candidate topology and report the range of conclusions as a form of specification sensitivity analysis. FWL invariance holds under linear OLS and approximately under logistic regression; applicability to non-parametric methods (doubly robust estimators, TMLE) remains unverified. Our framework assumes $C$ is known or estimable from held-out gold-standard labels; obtaining accurate $C$ itself requires gold annotations, a bootstrapping constraint mitigated by cross-validation or 
…[truncated 174 chars]

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

_source line 1202 · 2026-05-23T11:24:32.478512+00:00_

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

_source line 1203 · 2026-05-23T11:24:33.432885+00:00_

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
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-23T11:24:33.885376+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib && cat agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
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
    "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib && cat agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-23T11:24:34.338537+00:00_

Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-23T11:24:34.439536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib",
  "limit": "40"
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
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-23T11:24:34.490270+00:00_

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

_source line 1208 · 2026-05-23T11:24:38.406245+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -10",
  "description": "Find project config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-23T11:24:38.507107+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-23T11:24:41.569368+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project_config*\" 2>/dev/null | head -10",
  "description": "Find project config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-prod_0510 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project_config*\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-23T11:24:41.620024+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-23T11:24:44.382654+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ 2>/dev/null",
  "description": "List project directory"
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
    "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ 2>/dev/null",
    "description": "List project directory"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-23T11:24:44.433312+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
__pycache__
_last_visual_review.json
_paper_audit_result.json
annot_sensitivity
artifacts
checkpoints
decisions.lock
decisions.yaml
distill_tmp
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
patch_metrics.py
plan_001_collider_mbias_iv.py
plan_001_mediation_frontdoor.py
plan_002_k57_extension.py
plan_005_asv_extended.py
plan_006_asv_empirical.py
plan_007_correction_guidance.py
plan_008_binarization_collapse.py
plan_009_pathological_matrices.py
plan_010_ppi_empirical_validation.py
registry.lock
registry.yaml
report.md
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-23T11:24:52.013942+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/registry.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/registry.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-23T11:24:52.064940+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-23T11:24:55.079241+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -5",
  "description": "Search for external review config"
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
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-23T11:24:55.230344+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-23T11:25:01.009299+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Get PDF page count and info"
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
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Get PDF page count and info"
  }
}
```

</details>

---


### Tool result

_source line 1219 · 2026-05-23T11:25:01.160372+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sat May 23 11:17:32 2026 UTC
ModDate:         Sat May 23 11:17:32 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           31
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       921454 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-23T11:25:19.672876+00:00_

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


### Tool result

_source line 1221 · 2026-05-23T11:25:37.964380+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18291
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-23T11:25:39.370433+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验完整性**。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: projects/causal_annot_error_attrib/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n\n## Venue 要求\n- EMNLP 2026 通过 ARR 统一审稿\n- Long paper 正文限 8 页，参考文献不限\n- 必须有 Limitations section（不计入页数限制）\n- Double-blind 匿名审稿\n- ACL 模板\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n重点审查以下方面：\n\n1. **理论严谨性**：\n   - Proposition 1 (sign preservation) 的证明是否完整、正确\n   - Theorem 1 (envelope monotonicity, K=2) 的证明是否严密\n   - Conjecture 1 (ε-approximate monotonicity, K≥3) 的数值验证是否充分\n   - Observation 1 的数值验证规模和方法是否合理\n   - 三级证据层次（proved/verified/conjectured）的区分是否清晰\n\n2. **假设合理性**：\n   - Non-differential misclassification 假设在 LLM 场景下是否合理\n   - Proportional effects 假设的限制性和验证\n   - 线性 SEM 假设对 NLP 实践的适用性\n   - 各假设的讨论是否充分\n\n3. **实验设计与验证**：\n   - Monte Carlo 验证的设置是否恰当（N=10,000, 100,000 matrices）\n   - Theory-MC MAPE 1.6% 的可信度\n   - 23 个 LLM 配置的覆盖性是否足够\n   - ASV 框架验证的完整性\n   - 校正方法比较（5 methods × 7 topologies × 6 error structures）的公平性\n   - Bootstrap CI 的可靠性\n\n4. **数值声明一致性**：\n   - Abstract 与正文/附录中的数值是否一致\n   - 所有百分比、比率是否有明确来源\n\n请给出完整审稿意见，包含 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: must-fix / should-fix / minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
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
    "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验完整性**。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: projects/causal_annot_error_attrib/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n\n## Venue 要求\n- EMNLP 2026 通过 ARR 统一审稿\n- Long paper 正文限 8 页，参考文献不限\n- 必须有 Limitations section（不计入页数限制）\n- Double-blind 匿名审稿\n- ACL 模板\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n重点审查以下方面：\n\n1. **理论严谨性**：\n   - Proposition 1 (sign preservation) 的证明是否完整、正确\n   - Theorem 1 (envelope monotonicity, K=2) 的证明是否严密\n   - Conjecture 1 (ε-approximate monotonicity, K≥3) 的数值验证是否充分\n   - Observation 1 的数值验证规模和方法是否合理\n   - 三级证据层次（proved/verified/conjectured）的区分是否清晰\n\n2. **假设合理性**：\n   - Non-differential misclassification 假设在 LLM 场景下是否合理\n   - Proportional effects 假设的限制性和验证\n   - 线性 SEM 假设对 NLP 实践的适用性\n   - 各假设的讨论是否充分\n\n3. **实验设计与验证**：\n   - Monte Carlo 验证的设置是否恰当（N=10,000, 100,000 matrices）\n   - Theory-MC MAPE 1.6% 的可信度\n   - 23 个 LLM 配置的覆盖性是否足够\n   - ASV 框架验证的完整性\n   - 校正方法比较（5 methods × 7 topologies × 6 error structures）的公平性\n   - Bootstrap CI 的可靠性\n\n4. **数值声明一致性**：\n   - Abstract 与正文/附录中的数值是否一致\n   - 所有百分比、比率是否有明确来源\n\n请给出完整审稿意见，包含 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: must-fix / should-fix / minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-23T11:25:55.340929+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15970
}
```

</details>

---


### Tool call

_source line 1224 · 2026-05-23T11:25:55.844970+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性 + 完整性 + 表达**。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: projects/causal_annot_error_attrib/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n\n## Venue 要求\n- EMNLP 2026 通过 ARR 统一审稿\n- Long paper 正文限 8 页，参考文献不限\n- 必须有 Limitations section（不计入页数限制）\n- Double-blind 匿名审稿\n- ACL 模板\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n重点审查以下方面：\n\n1. **新颖性与贡献定位**：\n   - \"first unified analysis of K-class annotation error across seven topologies\" 这一 claim 是否成立\n   - ASV framework 与 E-value、partial R² 的创新边界是否清晰\n   - 三个贡献（bias taxonomy, ASV, correction guidance）的独立价值\n   - FWL invariance 负结果的新颖性\n   - 与 Teblunthuis (2024)、Lee et al. (2024) 的增量是否充分\n\n2. **相关工作覆盖**：\n   - 是否有重要遗漏的相关工作\n   - 对现有工作的定位是否准确公正\n   - 因果推断 + 测量误差文献的覆盖是否充分\n   - NLP + LLM 标注文献的覆盖是否充分\n\n3. **写作质量与可及性**：\n   - 对 EMNLP 受众（NLP 研究者，非计量经济学家）是否友好\n   - 计量经济学术语（plim, FWL, Wald estimator）的解释是否充分\n   - Abstract 和 Introduction 的信息密度是否合适\n   - 叙事结构是否清晰（problem → gap → contribution → evidence）\n   - 图表质量和信息传达效率\n\n4. **格式合规性**：\n   - 正文是否在 8 页以内\n   - Limitations section 是否存在且充分\n   - 匿名审稿要求是否满足（无身份信息泄露）\n   - 引用格式是否符合 ACL 规范\n   - 附录内容与正文的关系是否合理\n\n5. **Limitations section 评估**：\n   - 是否覆盖了论文的主要局限\n   - 是否诚实、完整\n   - 长度是否合适（不应过长）\n\n请给出完整审稿意见，包含 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: must-fix / should-fix / minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
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
    "text": "你是 Reviewer 2，负责审查**新颖性 + 完整性 + 表达**。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: projects/causal_annot_error_attrib/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_15/submitted.pdf\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n\n## Venue 要求\n- EMNLP 2026 通过 ARR 统一审稿\n- Long paper 正文限 8 页，参考文献不限\n- 必须有 Limitations section（不计入页数限制）\n- Double-blind 匿名审稿\n- ACL 模板\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n重点审查以下方面：\n\n1. **新颖性与贡献定位**：\n   - \"first unified analysis of K-class annotation error across seven topologies\" 这一 claim 是否成立\n   - ASV framework 与 E-value、partial R² 的创新边界是否清晰\n   - 三个贡献（bias taxonomy, ASV, correction guidance）的独立价值\n   - FWL invariance 负结果的新颖性\n   - 与 Teblunthuis (2024)、Lee et al. (2024) 的增量是否充分\n\n2. **相关工作覆盖**：\n   - 是否有重要遗漏的相关工作\n   - 对现有工作的定位是否准确公正\n   - 因果推断 + 测量误差文献的覆盖是否充分\n   - NLP + LLM 标注文献的覆盖是否充分\n\n3. **写作质量与可及性**：\n   - 对 EMNLP 受众（NLP 研究者，非计量经济学家）是否友好\n   - 计量经济学术语（plim, FWL, Wald estimator）的解释是否充分\n   - Abstract 和 Introduction 的信息密度是否合适\n   - 叙事结构是否清晰（problem → gap → contribution → evidence）\n   - 图表质量和信息传达效率\n\n4. **格式合规性**：\n   - 正文是否在 8 页以内\n   - Limitations section 是否存在且充分\n   - 匿名审稿要求是否满足（无身份信息泄露）\n   - 引用格式是否符合 ACL 规范\n   - 附录内容与正文的关系是否合理\n\n5. **Limitations section 评估**：\n   - 是否覆盖了论文的主要局限\n   - 是否诚实、完整\n   - 长度是否合适（不应过长）\n\n请给出完整审稿意见，包含 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: must-fix / should-fix / minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-23T11:25:57.304378+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 1226 · 2026-05-23T11:26:05.277855+00:00_

Round 1 已启动，三线并行：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验完整性） | ⏳ 审稿中 |
| Reviewer 2（新颖性 + 完整性 + 表达） | ⏳ 审稿中 |
| 视觉审查 Agent | ⏳ 渲染中 |

等待两位 Reviewer 返回审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 117

## Round 117

2 recorded events


### User

_source line 1227 · 2026-05-23T11:35:09.511153+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）

**论文标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 选题重要且系统性突出，七拓扑统一分析和 ASV 框架填补了真正的研究空白；但 K≥3 核心单调性结果停留在 Conjecture 层面，且论文对 EMNLP 主流受众的可及性不足。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2 Theorem 1 有完整证明，Propositions 1-6 证明充分；但 K≥3 的核心 ASV 单调性仅为 Conjecture 1，210,000 随机矩阵验证不等于证明。非差分误分类假设的 stress test 覆盖不足 |
| Excitement | 3.5/5 | 选题及时（LLM annotation 快速普及），ASV 框架有实用价值，Algorithm 1 提供可操作的实践指引；但重计量方法论和密集术语可能限制 NLP 社区的实际采用率 |
| Reproducibility | 4/5 | 方法论描述详细，Monte Carlo 设置清晰，承诺代码发布，23 个 LLM 配置来源明确 |
| Reviewer Confidence | 4/5 | 熟悉因果推断、测量误差、sensitivity analysis 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] K≥3 核心 ASV 单调性结果是 Conjecture 而非 Theorem

- 具体位置：Section 3.3, Conjecture 1 (p.6); Appendix B.12 (p.27)
- 问题：论文将 ASV 框架定位为三大贡献之一，而 ASV 在 K≥3 下的实用性依赖于 envelope monotonicity——即随着 misclassification 程度 δ 增大，bias 单调不减。K=2 下 Theorem 1 提供了严格证明，但 K≥3 下仅有 Conjecture 1，依靠 210,000 随机矩阵的数值验证（violation ε < 0.06）。论文坦诚标注为 conjecture，这是值得肯定的，但数值验证无法排除 corner case 反例的存在。Appendix B.12 报告 worst-case single-step deviation 为 0.011（confounding）到 >10⁷（IV），但 IV 已排除在 conjecture 范围外。
- 为什么影响接收：ARR reviewer guidelines 明确要求 "formal statements (theorems, propositions) should be supported by complete and correct proofs"。虽然 Conjecture 1 未标为 theorem，但它是 ASV 框架在多类场景（实际应用中的常见情形）下成立的理论基础。如果单调性在某些 confusion matrix 结构下失效，ASV 的 vulnerability ranking 可能不可靠。
- 建议修改方向：(a) 在特殊条件下给出部分证明（如对角占优度 ≥ θ 时严格单调），将 conjecture 范围缩小到更一般的条件；(b) 如无法证明，需量化 violation 发生的参数空间特征——ε < 0.06 的 violation 集中在什么类型的 confusion matrix？这些矩阵在 real LLM 中是否出现过？(c) 讨论当 monotonicity 被轻微违反时，ASV ranking 的实际鲁棒性（如 ranking 是否在 violation 区域内反转）。

**N2** [critical] 对 EMNLP 受众的可及性不足

- 具体位置：全文，尤其是 Abstract, Section 3.1-3.3
- 问题：论文大量使用计量经济学和流行病学术语，且解释不充分：
  - **plim**（probability limit）：在 Abstract 和 Introduction 中已多次隐含使用（"probability limit"出现于 p.4 正文，而 Abstract 提到 "systematically characterizes systematic bias"），但正式定义在 p.4 脚注 1。EMNLP 读者不一定熟悉这个概念。
  - **FWL 定理**（Frisch-Waugh-Lovell）：是论文的核心概念之一（FWL invariance 作为负结果是 Contribution 3 的基础），但仅在 p.3 用一句话解释（"the coefficient from a simple regression after residualizing all other variables"）。
  - **Wald estimator**（p.5）：引用 Angrist and Imbens (1995) 但未解释其直觉含义。
  - **E-value**（p.1, p.5-6）：虽引用了 VanderWeele and Ding (2017)，但未解释 E-value 的基本思想就直接与 ASV 对比。
  - **column-stochastic**：在 Conjecture 1 和附录中频繁使用，未显式定义。
  - Abstract 信息密度极高，在一个段落中包含了 7 个拓扑、sign reversal、ASV、monotonicity、Theorem/Conjecture、correction methods、FWL invariance 等概念。
- 为什么影响接收：EMNLP 的主流受众是 NLP 研究者和 CSS 研究者，而非计量经济学家。如果主要读者群无法 follow 方法论，论文的 impact 和 excitement 会大打折扣。ARR guidelines 的 H11 虽然说 "writing quality shouldn't trump content"，但可及性不同于写作质量——这里的问题不是语法或文风，而是目标读者能否理解核心贡献。
- 建议修改方向：(a) 在 Section 3.1（或之前）增加 "Preliminaries" 段落，用 NLP 友好的语言和例子解释 plim、FWL、column-stochastic 等核心概念——每个 2-3 句话即可；(b) 大幅精简 Abstract，突出 1-2 个最核心发现（如 "K≥3 sign reversal" 和 "topology-dependent vulnerability ranking"），将其余细节留给 Introduction；(c) 考虑增加一个 running example（如 sentiment analysis task 上的 stance classification）贯穿 Section 3，帮助读者将抽象公式与具体 NLP 场景关联。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 非差分误分类假设的实际适用性讨论与验证不够充分

- 具体位置：Definition 1 (p.4), Limitations (p.8-9), Appendix B.6 (p.24)
- 问题：全文建立在 Definition 1（non-differential misclassification）上：P(A*|A,X,Y,Z) = P(A*|A)，即 LLM 的分类准确率不依赖于 outcome Y 或其他协变量。这要求 LLM 在标注时不接触 Y 相关信息。但在实践中：(1) LLM 可能通过上下文间接获取 Y 的信号（如在 sentiment → purchase 因果链中，评论文本可能同时包含 sentiment 和 purchase 相关信息）；(2) few-shot prompting 时示例选择可能引入 differential bias。Appendix B.6 的 stress test 值得肯定，但仅在 exposure 拓扑下测试（Table 7），且在 mild violations（ε=0.01）下 violation 率升至 12.4%（amplification 为 2.4，从 baseline 13.3%），ε=0.05 时 amplification 升至 16.7。其他拓扑下的 robustness 未知。
- 建议：(a) 将 stress test 扩展到至少 confounding 和 mediation 拓扑；(b) 在 Limitations 中明确列举 2-3 个 NLP 场景说明何时假设可能被违反；(c) 提供定量指导——当 differential 程度超过什么阈值时，本文结论不再可靠。

**W2** [warning] 与核心 prior work 的增量区分不够清晰

- 具体位置：Section 2 (p.2-3), Section 1 (p.1-2)
- 问题：论文正确指出 Wood-Doughty et al. (2018) 覆盖 4 个 DAG 但限于 K=2，Teblunthuis et al. (2024) 覆盖有限拓扑，Lee and Wood-Doughty (2024) 仅覆盖 confounding。但在方法论层面的增量说明不够具体：
  - 对于 **confounding 拓扑**，本文的 K-class bias expression (Eq. 1) 与 Teblunthuis et al. (2024) 的结果是否本质不同，还是 K-class 推广？
  - **ASV** 与 E-value 的技术创新点：Remark 1 (p.6) 列出三个区别（topology dependence, sign-flip diagnostic, parametric structure），但每个仅一句话，未给出具体数学层面的对比。
  - **correction guidance** 与已有 correction 文献（如 Angelopoulos et al. 2023 PPI++, Egami et al. 2023 DSL）的增量是什么——是方法创新还是 benchmark 式的系统比较？
- 建议：在 Section 2 末尾增加一个结构化对比（可用表格），沿维度 {拓扑覆盖, K 值范围, sensitivity analysis, correction, 理论 vs 经验} 逐篇列出 prior work 与本文的差异。

**W3** [warning] 实证验证的 LLM 和任务覆盖有限

- 具体位置：Section 4.4 (p.8), Figure 5 & 7 (p.21)
- 问题：经验验证使用 HumAnD (K=10), VAST (K=3), CivilComments (K=2) 和 4 个 LLM（包括 zero-shot 和 few-shot），共 23 个配置 × 161 bias scenarios。任务类型限于 hate speech detection, stance detection, sentiment/toxicity 分类。但 NLP 中还有大量其他标注任务（NER, relation extraction, event detection, discourse parsing），其 confusion matrix 结构可能与 sentiment-type 任务截然不同（如 NER 中的 O-tag 主导的稀疏混淆矩阵）。
- 建议：(a) 明确讨论 23 个配置在 confusion matrix 结构上的多样性——对角占优度、off-diagonal 结构是否覆盖了 Figure 2 中 sign reversal 最可能发生的区域？(b) 在 Limitations 中指出对其他任务类型的验证是 future work。

**W4** [warning] Figure 2 和 Figure 3 的可读性

- 具体位置：Figure 2 (p.7), Figure 3 (p.8)
- 问题：Figure 2 包含 7 个拓扑的 bias 分布子图，在 single-column 打印尺寸下每个子图过小，x 轴标签和刻度难以辨认。红色（sign reversal）和灰色/蓝色的区分在灰度打印下可能丢失。Figure 3 的 y 轴标签 "Topology Determinism Bias, Vol F₁" 含义不够直观。
- 建议：(a) Figure 2 考虑拆分为两行四列或选取最有代表性的 3-4 个拓扑放在正文、其余移入附录；(b) 使用 marker shape（如 ○ vs △）辅助颜色区分；(c) Figure 3 的 y 轴标签增加解释或在 caption 中说明 Vol F₁ 的含义。

**W5** [warning] Algorithm 1 的阈值选择缺乏理论依据

- 具体位置：Algorithm 1 (p.31), Section 4.5 (p.8)
- 问题：Algorithm 1 是实践贡献的核心，提供拓扑感知的校正方法推荐。但其中的决策阈值似乎是经验性的：
  - 步骤 1 中 τ_conf > 0.7 的 "high accuracy" 阈值
  - 步骤 2 中 RMSE reduction > 90.6% 的 "correction pointless" 阈值
  - 步骤 2 中 C₁₄ ≥ 0.05 RMSE red., 50.6% 的具体数值
  这些阈值是从 Table 4 的实验结果中提取的，但论文未讨论它们对不同 DGP 参数的敏感性。如果 DGP 改变，这些阈值是否仍然适用？
- 建议：(a) 讨论阈值选择的依据和敏感性；(b) 考虑将 Algorithm 1 改为更鲁棒的定性指导（topology → method class），避免依赖具体数值阈值。

---

## 小问题（不影响接收）

- p.1 Abstract: "seven canonical DAG topologies" 的 "canonical" 选取标准未解释。建议简短说明为什么是这 7 个（如 "covering all single-variable misclassification positions in linear structural equation models"）。
- p.3 Figure 1 caption: "starred-node annotation" 的 "starred" 含义（= observed with error）应在 caption 内而非仅在正文解释。
- p.4 footnote 1: plim 的正式定义位于此，但 abstract 和 introduction 已多次使用该概念。建议前移至首次使用处。
- p.5 Proposition 1: sign-flip guarantee 的条件 "|τ| > √(Var(g)/Var(h))·E[Var(T|A)]" 缺少直觉解释——这个条件在什么实际情境下容易/不容易满足？
- p.6 Observation 1: "numerical evidence (Conjecture 1)" 中，Observation 和 Conjecture 的关系可以更清晰——Observation 是对数值结果的描述，Conjecture 是对该 pattern 的形式化猜想。
- p.8 Conclusion: "Code and data will be released" → 匿名审稿阶段建议提供 anonymous repository 链接（如 Anonymous GitHub）以供 reviewers 验证 reproducibility。
- 论文中 τ 符号重载较重（τ_conf, τ_sign, τ_total, τ_obs 等），建议整理符号表或使用更具区分度的符号系统。
- Table 1 (p.7): "τ_conf=0?" 列的 "0%" 和 "Cond." 标记的含义在 caption 中解释不够清晰。

---

## 主要优势

1. **选题重要且时机恰当**：LLM 作为 annotator 在 CSS 中快速普及，但 annotation error 对 causal inference 的影响从未被跨拓扑系统分析过。本文填补了一个真正的研究空白，且在 NLP 社区对 LLM annotation quality 关注度持续上升的背景下极具时效性。

2. **系统性和完整性突出**：单篇论文覆盖 7 个拓扑 × K-class 扩展 × 3 种 ASV 诊断 × 5 种校正方法，提供从理论分析到实践指引的完整框架。23 页附录的证明和补充实验表明工作量极大。Theory-MC MAPE < 1.65%（Section 4.2）显示 analytic predictions 精度高。

3. **K≥3 sign reversal 发现有重要实践意义**：在 K=2 下 non-differential misclassification 只能造成 attenuation（Brenner, 1993），但 K≥3 引入结构性的 sign reversal 可能——83.4% 的 K=3 confusion matrices 导致至少一个系数 sign reversal（p.1 abstract; Appendix B.1）。这一发现对在多类标注场景（sentiment 3+ 类、stance 4+ 类）中做因果推断的 CSS 实践者有直接警示价值。

4. **FWL invariance 负结果有独立方法论价值**：证明 matrix-based correction（naive plug-in, MLA）对 confounding/mediation/collider/M-bias 四种 FWL-invariant 拓扑 exactly 无效（0% RMSE reduction, Table 4 p.22），为实践者提供了 "不应该做什么" 的明确指引。这比单纯推荐某种校正方法更有决策价值。

5. **实验设计三层验证结构合理**：(a) analytic predictions 对照 (b) Monte Carlo 验证（100,000 随机矩阵，20,000+ 配置）对照 (c) real LLM confusion matrices（4 LLM × 23 配置 × 161 scenarios），三层证据相互印证。

6. **Proposition 1 sign preservation 的严格性**：为 confounding 和 collider 提供了解析条件（Cauchy-Schwarz 和 endpoint analysis），不依赖数值验证。Table 2 (p.20) 清晰列出每个拓扑的 sufficient conditions 和证明状态。

---

## Missing References

- **Imai, Keele, and Tingley (2010)**, "A General Approach to Causal Mediation Analysis" — 高度相关于 mediation 拓扑的讨论（Section 3.2, p.4-5），当前 mediation 部分未引用该 foundational work。
- 论文的引用列表总体覆盖充分，测量误差文献（Carroll et al. 2006, Buonaccorsi 2010, Bound et al. 2001）、NLP 标注文献（Gilardi et al. 2023, Ziems et al. 2024）、sensitivity analysis（VanderWeele and Ding 2017, Cinelli and Hazlett 2020）的核心工作均已引用。

---

## Questions for Authors

1. **Conjecture 1 的 violation 结构**：ε < 0.06 的 violations 在 confusion matrix 参数空间中的分布如何？是否集中在对角占优度极低的区域？这类矩阵在 real LLM 的 23 个配置中是否出现过？

2. **非差分假设违反的鲁棒性**：在 differential misclassification（如 ε=0.03-0.05 的 outcome-dependent 分类偏差）下，ASV vulnerability ranking（IV > front-door > exposure > mediation > confounding/collider > M-bias）是否仍然稳定？

3. **K 对实践建议的影响**：Table 4 (p.22) 的校正方法比较在 K=3 下进行。Appendix B.7 显示 K=5,7 下 method ranking 稳定，但 K=10 时 PPI++ 退化。这是否意味着 Algorithm 1 的推荐在 high-K 场景（如 fine-grained sentiment 10 级标注）下需要修改？

4. **Logistic regression 下的 FWL 等价性**：Table 5 (p.22) 显示 FWL invariance 在 logistic regression 下 "practically breaks" 但 bias 极小（|Δ| ~10⁻³）。这个 "practically negligible" 的判断是否依赖于 DGP 参数？是否存在参数配置使 deviation 变得 substantial？

---

## 格式合规性检查

| 项目 | 状态 | 说明 |
|------|------|------|
| 正文页数 | ✅ 合规 | 8 页（含 Conclusion + Limitations），在限制内 |
| Limitations section | ✅ 存在 | p.8-9，覆盖 3 个主要局限（非差分假设、线性结构方程、K-specific 结果），长度适当 |
| 匿名审稿 | ✅ 合规 | 标注 "Anonymous ACL submission"，未发现身份信息泄露 |
| 引用格式 | ✅ 合规 | ACL 标准格式 |
| 附录 | ✅ 合理 | 23 页，包含完整证明、补充实验、Algorithm 1 |

---

## 总结

本文解决了一个重要且未被系统研究的问题——K-class LLM annotation error 在因果推断中的 topology-dependent 传播。工作量大、实验验证三层结构合理、K≥3 sign reversal 和 FWL invariance 两个核心发现有实践价值。主要不足在于：(1) K≥3 ASV 单调性仅有 conjecture 而非 proof，削弱了理论贡献的可靠性；(2) 对 EMNLP 受众的可及性不足——密集的计量术语和高度压缩的 abstract 可能阻碍 impact。如果作者能在 (1) 上提供 partial proof 或更充分的 failure mode 分析，并在 (2) 上增加 Preliminaries 段落和精简 abstract，本文可达到 Conference 接收水准。

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

_source line 1228 · 2026-05-23T11:35:22.215701+00:00_

Reviewer 2 审稿意见已收到（3.5 Borderline Conference）。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1229 · 2026-05-23T11:35:29.866820+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成，已提交给 Review Director。

核心评价：**Overall 3.5 (Borderline Conference)**。两个 Must-Fix：(1) K≥3 ASV 单调性停留在 Conjecture 层面，需 partial proof 或更充分的 failure mode 分析；(2) 对 EMNLP 受众可及性不足，计量术语（plim、FWL、Wald estimator）解释不充分，Abstract 过于密集。五个 Should-Fix 涉及非差分假设 stress test 覆盖不足、与 prior work 增量区分不清晰、LLM/任务覆盖有限、Figure 可读性、Algorithm 1 阈值缺乏理论依据。主要优势：选题重要且时机好、系统性突出（7 拓扑 × K-class × 3 ASV × 5 校正方法）、K≥3 sign reversal 和 FWL invariance 两个核心发现有实践价值。

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

_source line 1230 · 2026-05-23T11:35:37.485459+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 119

## Round 119

6 recorded events


### User

_source line 1231 · 2026-05-23T11:38:05.480008+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性 + 实验完整性

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 首次系统研究 K≥3 标注误差在 7 种 DAG 拓扑下的因果推断偏差传播，理论贡献扎实（闭合形式偏差表达式、sign preservation 证明、FWL invariance 发现），但核心 ASV 单调性对 K≥3 仅为猜想未证明，且所有实验均在合成 DGP 上完成，缺乏真实观测数据的端到端因果估计验证。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2 证明完整正确（Theorem 1, Proposition 1）；K≥3 关键性质（ASV 单调性）仅有数值验证未证明；non-differential 假设较强且框架对其违反敏感 |
| Excitement | 3.0/5 | 问题重要且及时（LLM 标注越来越普遍），但理论性强、应用限于线性 SEM + 分类变量，对 NLP 社区的直接影响较间接 |
| Reproducibility | 4/5 | 实验参数详尽（DGP 设置、样本量、随机种子均明确），承诺开源代码和数据，附录提供完整推导 |
| Reviewer Confidence | 4/5 | 熟悉因果推断与测量误差文献，仔细审查了主要证明和数值声明 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] K≥3 ASV 单调性仅为猜想——论文最核心的实用贡献缺乏理论保证

- **具体位置**：Section 3.3 Conjecture 1 (p.6), Observation 1 (p.6), Appendix B.12 (Table 10, p.27)
- **问题**：Theorem 1 仅证明了 K=2 在 proportional effects (f=λg) 下的 envelope monotonicity。对于论文标题强调的 "Multi-Class" (K≥3) 情形，ASV 的拓扑脆弱性排序（IV > Exposure > Front-door > Mediation > Confounding > Collider > M-bias）完全依赖于 Conjecture 1（ε-approximate monotonicity, ε < 0.06）。该猜想仅有 210,000 个随机矩阵的数值支撑，随机采样无法排除特定对抗性矩阵结构导致单调性失效的可能。
- **附加疑问**：Observation 1 声称 "worst-case deviations < 0.005"，但 Table 10 中 confounding K=3 的 "Worst mag." 列显示 0.011，front-door 显示 0.031——这些数字之间存在表面不一致。如果 Table 10 的数字正确，Observation 1 的 "< 0.005" 陈述需要修正或澄清度量定义的差异。
- **为什么影响接收**：ASV 排序是 Algorithm 1（校正方法选择指南，p.31）的直接输入。如果 K≥3 单调性不成立，基于 ASV 的拓扑脆弱性排序和校正指导可能对特定混淆矩阵结构失效，削弱论文最具实践价值的贡献。
- **建议修改方向**：(a) 至少对一个拓扑（如 confounding）给出 K=3 的解析证明或更紧的界；(b) 补充对抗性搜索（如 gradient-based optimization over the space of column-stochastic C），而非仅依赖 Dirichlet 随机采样；(c) 更明确量化猜想失效时对 Algorithm 1 实践建议的影响范围。

**N2** [critical] 所有实验均为合成 DGP，缺乏真实观测数据的端到端因果分析验证

- **具体位置**：Section 4 整体 (pp.6-8)，特别是 Section 4.4 "Empirical Validation" (p.8)
- **问题**：论文的全部实验（bias taxonomy 验证、ASV 计算、correction method 比较）均使用合成线性 SEM + 注入真实 LLM 混淆矩阵的设置。Section 4.4 的 "Empirical Validation" 仅验证了理论预测与 MC 模拟的一致性，并未在任何真实观测数据上运行完整的因果分析流程（LLM 标注 → ASV 诊断 → 校正方法选择 → 最终因果估计评估）。论文 Abstract 最后一句声称 "topology-aware analysis is necessary for valid causal inference with LLM-generated annotations"，但该声明缺乏真实数据支撑。
- **部分缓解**：Appendix B.18 (ASV Diagnosis of Political Ad Tone, p.29) 提供了一个接近真实应用的案例，使用了 Egami et al. (2023) 的政治广告数据和真实 K=3 混淆矩阵。但该案例仅停留在 ASV 诊断层面，未展示校正后的因果估计质量。
- **为什么影响接收**：EMNLP 审稿人期望看到对 NLP 实践的直接影响。框架在合成环境中的表现不能完全代表真实 CSS 研究中的实用性——真实数据中可能存在非线性、异方差、differential misclassification 等合成数据未捕捉的复杂性。
- **建议修改方向**：在 Appendix B.18 的基础上扩展为完整的端到端演示——从 LLM 标注 → 拓扑识别 → ASV 诊断 → 校正方法选择 → 与人工标注基准的因果估计比较。即使只有一个数据集，完整流程的演示也会大幅提升说服力。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Non-differential misclassification 假设在 LLM 场景下可能系统性违反，且框架对违反高度敏感

- **具体位置**：Definition 1 (p.4), Appendix B.6 (p.24), Table 15 (p.29)
- **问题**：Definition 1 要求 P(A*|A,Y,Z) = P(A*|A)——LLM 的分类误差不依赖于结果 Y 或协变量 Z。但 LLM 对文本的分类准确率通常与文本语义内容相关，而语义内容可能与 Y 相关（如情感强烈的文本更易被正确分类，情感强度本身与结果变量相关）。Appendix B.16 Table 15 显示安全阈值极紧——大多数数据集要求 ε < 0.02 才能保证 sign preservation，意味着即使微小的 differential misclassification 也可能使框架失效。
- **建议**：(a) 在正文中增加对 non-differential 假设在实际 LLM 标注中可信度的讨论，最好配有一个实证检验（如检测 LLM 误差率与 Y 的条件独立性）；(b) 讨论当假设违反时，哪些结论仍然近似成立，哪些完全失效。

**W2** [warning] Table 1 列定义模糊——"Violation" vs "Sign Flip" 含义不清，导致数值解读困难

- **具体位置**：Table 1 (p.7)
- **问题**：Table 1 的 "Violation" 和 "Sign Flip" 两列未在 caption 或正文中清晰定义。对于 Exposure，Violation=83.4% 而 Sign Flip=14.1%；对于 IV，Violation=34.2% 而 Sign Flip=52.6%。IV 的 Sign Flip > Violation 看似反直觉——如果 Violation 是 sign preservation 条件的违反，那么 sign flip 率怎么会高于条件违反率？Abstract 中 "83.4% produce sign reversal of at least one secondary coefficient" 对应的是 Violation 列而非 Sign Flip 列，但 "sign reversal" 一词自然对应 "Sign Flip"。这种术语混用增加了读者理解的认知负担。
- **建议**：在 Table 1 caption 中明确定义：Violation = [具体条件] 的违反率；Sign Flip = [具体定义] 的发生率。

**W3** [warning] ASV 参数化假设类别间均匀退化，与 LLM 实际误差模式不符

- **具体位置**：Section 3.3 Parameterization (p.5-6)
- **问题**：C(δ) = (1-δ)I + δC₀ 的插值假设所有类别以相同速率退化。但 LLM 误差模式通常高度非均匀——稀有类别的误差率远高于频繁类别，易混淆的类别对之间存在系统性偏移。Appendix B.11 测试了不同的 β 设置（alternating-large, same, alternating-small），但这改变的是效应方向/大小，而非混淆矩阵的退化结构。论文正文也承认 "rare-class-specific degradation would require multi-dimensional extensions"，但未给出这类扩展的初步探索。
- **建议**：(a) 测试 class-specific δ_k 参数化下 ASV 排序的鲁棒性；(b) 至少定性讨论非均匀退化对 ASV 排序的潜在影响。

**W4** [warning] Abstract 中 FWL invariance 声明缺少线性 OLS 限定条件

- **具体位置**：Abstract (p.1) 最后一段
- **问题**：Abstract 说 "matrix-based corrections are provably ineffective for four topologies due to Frisch-Waugh-Lovell invariance"，但 FWL invariance 严格来说仅在线性 OLS 下成立。Section 4.5 (p.8) 正文指出 "under logistic regression the invariance breaks but empirically by < 0.005"，Appendix B.7 Table 5 也展示了逻辑回归下的偏差，但 Abstract 中缺少 "under linear OLS" 这一关键限定词。这可能误导不仔细阅读正文的读者。
- **建议**：Abstract 中加 "under linear regression" 或 "under OLS"。

**W5** [warning] Theorem 1 的 proportional effects 假设 (f=λg) 限制性较强，实践中难以验证

- **具体位置**：Theorem 1 (p.6), Appendix B.13 (p.28)
- **问题**：Theorem 1 要求 confounder 对 T 和 Y 的效应成比例 (f=λg)。Appendix B.13 显示当 f ⊥ g（完全独立）时 OOB 率达 25%，虽然 sign failure 率仍低（< 1%），但 OOB 本身意味着偏差界不再有效。更关键的是，实践者通常无法验证 proportional effects 是否成立，因为 confounder 是未观测或部分观测的。
- **建议**：在正文讨论中增加关于 proportional effects 可验证性的讨论，并更明确说明当假设违反时 Theorem 1 的退化行为。

---

## 小问题（不影响接收）

- **M1**: Section 3 符号密度高（Appendix Table 19 列出约 20 个符号），正文中可考虑增加 notation summary box 或将部分符号定义移至首次使用处
- **M2**: Algorithm 1（校正方法选择指南，p.31）是论文最具实践价值的输出之一，但被放在 Appendix 最后一页。建议至少在正文 Section 4.5 中放置简化版或引用更显眼
- **M3**: Figure 1 (p.3) 七个 DAG 拓扑图在双栏格式下较小，部分边的标签（如 starred-node 与 dashed edge 的区别）在打印时可能难以辨认
- **M4**: Limitations section 对线性假设的局限讨论可更充分，可引用 Appendix B.7 中 logistic regression DGP 的结果作为部分缓解

---

## 主要优势

- **S1**: 首次系统研究 K≥3 多类标注误差在 7 种 DAG 拓扑下的因果偏差传播，是对 binary-only 文献（Wood-Doughty 2018, 2024; Tsilidis et al. 2024）的实质性扩展
- **S2**: 三级证据层次（proved / numerically verified / conjectured）科学透明，避免了常见的过度声明问题
- **S3**: 7 种拓扑的闭合形式偏差表达式（Eqs. 1-3 及 Appendix A.3-A.8）为一般 K 推导，理论贡献扎实
- **S4**: FWL invariance 发现（Section 4.5）直接回答了 "为什么 MLA/Naive plug-in 对协变量拓扑无效" 的实践问题，具有明确的指导意义
- **S5**: Theory-MC 一致性 MAPE 1.6% across 161 scenarios (23 LLM configs × 7 topologies)，验证规模充分、精度高
- **S6**: 附录 23 页包含完整证明（7 个拓扑的 sign preservation 推导）、15+ 项鲁棒性检查（非线性 DGP、cross-K 验证、bootstrap CI、non-differential stress test 等），体现出色的学术严谨度
- **S7**: 23 个真实 LLM 配置（HumAID K=10, VAST K=3, CivilComments K=2; 4 LLMs; zero/few-shot）的经验验证增强了框架的实践相关性
- **S8**: F1 与 causal bias 无显著相关（Spearman ρ = −0.10, p = 0.45, Figure 3）的发现具有警示价值——标准分类指标不能替代拓扑感知的因果分析

---

## Questions for Authors

**Q1**: Observation 1 声称 "worst-case deviations < 0.005"，Conjecture 1 使用 ε < 0.06 阈值，而 Table 10 显示 front-door 的 worst magnitude 为 0.031。请澄清这三个数字之间的关系——它们使用的偏差度量是否相同？

**Q2**: 对于 non-differential 假设的实际可信度，是否有可能设计一个实证检验（如利用已有的 gold-labeled 数据子集，检验 LLM 分类误差率是否条件独立于 Y）？

**Q3**: ASV 在非均匀退化模式下（如某个稀有类别的误差率为 50%，其余类别为 5%）的排序是否仍与均匀退化模式下一致？

**Q4**: Section 4.4 中 23 个 LLM 配置的 mean diagonal 范围为 0.45-0.81。当前主流 LLM（如 GPT-4, Claude 3.5）在同类任务上的准确率是否已显著高于此范围？如果是，该框架的警示在多大程度上仍然适用？

---

## Missing References

未发现重大引用遗漏。引用列表覆盖了测量误差（Carroll et al. 2006, Gustafson 2004）、因果推断（Pearl 2009, VanderWeele 2015）、NLP 因果分析（Keith et al. 2020, Feder et al. 2022）、LLM 标注质量（Gilardi et al. 2023, Kim et al. 2025）等核心文献。可考虑补充近期 LLM calibration 与 annotation quality 交叉领域的工作。

---

## 格式合规检查

- ✅ 正文 8 页（Sections 1-5），符合 EMNLP 2026 Long Paper 限制
- ✅ Limitations section 存在（p.8 底部），覆盖线性假设、non-differential 假设、观测范围
- ✅ Double-blind 合规——标题页标注 "Anonymous ACL submission"，正文无作者识别信息
- ✅ 参考文献格式正确，使用 ACL 模板
- ✅ 附录内容充实（23 页），包含完整证明和补充实验


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

_source line 1232 · 2026-05-23T11:39:01.291920+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] K≥3 核心 ASV 单调性结果是 Conjecture 而非 Theorem\n- Section 3.3, Conjecture 1 (p.6); Appendix B.12 (p.27)\n- 210,000 随机矩阵的数值验证无法排除 corner case 反例\n- 建议：(a) 特殊条件下部分证明；(b) 量化 violation 参数空间特征；(c) 讨论 violation 时 ASV ranking 的鲁棒性\n\n**N2** [critical] 对 EMNLP 受众的可及性不足\n- plim 在 Abstract 和 Introduction 中已多次隐含使用，正式定义在 p.4 脚注 1\n- FWL 定理仅在 p.3 用一句话解释\n- Wald estimator (p.5) 未解释直觉含义\n- E-value (p.1, p.5-6) 未解释基本思想就直接与 ASV 对比\n- Abstract 信息密度极高（7 个拓扑、sign reversal、ASV、monotonicity、Theorem/Conjecture、correction methods、FWL invariance）\n- 建议：增加 Preliminaries 段落；精简 Abstract；增加 running example\n\n### Should-Fix\n\n**W1** [warning] 非差分误分类假设的实际适用性讨论与验证不够充分\n- Appendix B.6 stress test 仅在 exposure 拓扑下测试（Table 7）\n- ε=0.01 时 violation 率升至 12.4%（amplification 2.4）\n- 建议扩展到 confounding 和 mediation 拓扑\n\n**W2** [warning] 与核心 prior work 的增量区分不够清晰\n- confounding 拓扑的 K-class bias expression 与 Teblunthuis (2024) 是否本质不同？\n- ASV 与 E-value 的技术创新点 Remark 1 仅每个一句话\n- correction guidance 是方法创新还是 benchmark 式系统比较？\n- 建议增加结构化对比表\n\n**W3** [warning] 实证验证的 LLM 和任务覆盖有限\n- 任务限于 hate speech, stance, sentiment/toxicity\n- 缺少 NER, relation extraction, event detection 等任务\n- 23 个配置的 confusion matrix 结构多样性存疑\n\n**W4** [warning] Figure 2 和 Figure 3 的可读性\n- Figure 2 子图过小，x 轴标签难辨\n- 灰度打印下颜色区分困难\n- Figure 3 y 轴标签 \"Topology Determinism Bias, Vol F₁\" 含义不够直观\n\n**W5** [warning] Algorithm 1 的阈值选择缺乏理论依据\n- τ_conf > 0.7, RMSE reduction > 90.6% 等阈值是经验性的\n- 未讨论对不同 DGP 参数的敏感性\n\n### Missing References\n- Imai, Keele, and Tingley (2010) \"A General Approach to Causal Mediation Analysis\" — mediation 拓扑的 foundational work\n\n### Questions\n1. Conjecture 1 的 violation 在 confusion matrix 参数空间中的分布如何？\n2. differential misclassification 下 ASV vulnerability ranking 是否仍稳定？\n3. K=10 时 PPI++ 退化是否意味着 Algorithm 1 推荐需修改？\n4. Logistic regression 下 FWL 等价性的 \"practically negligible\" 判断是否依赖 DGP 参数？\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Questions 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] K≥3 核心 ASV 单调性结果是 Conjecture 而非 Theorem\n- Section 3.3, Conjecture 1 (p.6); Appendix B.12 (p.27)\n- 210,000 随机矩阵的数值验证无法排除 corner case 反例\n- 建议：(a) 特殊条件下部分证明；(b) 量化 violation 参数空间特征；(c) 讨论 violation 时 ASV ranking 的鲁棒性\n\n**N2** [critical] 对 EMNLP 受众的可及性不足\n- plim 在 Abstract 和 Introduction 中已多次隐含使用，正式定义在 p.4 脚注 1\n- FWL 定理仅在 p.3 用一句话解释\n- Wald estimator (p.5) 未解释直觉含义\n- E-value (p.1, p.5-6) 未解释基本思想就直接与 ASV 对比\n- Abstract 信息密度极高（7 个拓扑、sign reversal、ASV、monotonicity、Theorem/Conjecture、correction methods、FWL invariance）\n- 建议：增加 Preliminaries 段落；精简 Abstract；增加 running example\n\n### Should-Fix\n\n**W1** [warning] 非差分误分类假设的实际适用性讨论与验证不够充分\n- Appendix B.6 stress test 仅在 exposure 拓扑下测试（Table 7）\n- ε=0.01 时 violation 率升至 12.4%（amplification 2.4）\n- 建议扩展到 confounding 和 mediation 拓扑\n\n**W2** [warning] 与核心 prior work 的增量区分不够清晰\n- confounding 拓扑的 K-class bias expression 与 Teblunthuis (2024) 是否本质不同？\n- ASV 与 E-value 的技术创新点 Remark 1 仅每个一句话\n- correction guidance 是方法创新还是 benchmark 式系统比较？\n- 建议增加结构化对比表\n\n**W3** [warning] 实证验证的 LLM 和任务覆盖有限\n- 任务限于 hate speech, stance, sentiment/toxicity\n- 缺少 NER, relation extraction, event detection 等任务\n- 23 个配置的 confusion matrix 结构多样性存疑\n\n**W4** [warning] Figure 2 和 Figure 3 的可读性\n- Figure 2 子图过小，x 轴标签难辨\n- 灰度打印下颜色区分困难\n- Figure 3 y 轴标签 \"Topology Determinism Bias, Vol F₁\" 含义不够直观\n\n**W5** [warning] Algorithm 1 的阈值选择缺乏理论依据\n- τ_conf > 0.7, RMSE reduction > 90.6% 等阈值是经验性的\n- 未讨论对不同 DGP 参数的敏感性\n\n### Missing References\n- Imai, Keele, and Tingley (2010) \"A General Approach to Causal Mediation Analysis\" — mediation 拓扑的 foundational work\n\n### Questions\n1. Conjecture 1 的 violation 在 confusion matrix 参数空间中的分布如何？\n2. differential misclassification 下 ASV vulnerability ranking 是否仍稳定？\n3. K=10 时 PPI++ 退化是否意味着 Algorithm 1 推荐需修改？\n4. Logistic regression 下 FWL 等价性的 \"practically negligible\" 判断是否依赖 DGP 参数？\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Questions 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-23T11:39:31.300370+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30008
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-23T11:39:32.204154+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] K≥3 ASV 单调性仅为猜想——论文最核心的实用贡献缺乏理论保证\n- Theorem 1 仅证明 K=2 在 proportional effects 下的 envelope monotonicity\n- K≥3 的 ASV 排序完全依赖 Conjecture 1\n- Observation 1 声称 \"worst-case deviations < 0.005\"，但 Table 10 中 confounding K=3 \"Worst mag.\" = 0.011，front-door = 0.031——存在表面不一致\n- 建议：(a) 至少对一个拓扑给出 K=3 解析证明；(b) 补充对抗性搜索；(c) 量化猜想失效时对 Algorithm 1 的影响\n\n**N2** [critical] 所有实验均为合成 DGP，缺乏真实观测数据的端到端因果分析验证\n- Section 4.4 \"Empirical Validation\" 仅验证理论预测与 MC 模拟一致性\n- 未在任何真实观测数据上运行完整因果分析流程（LLM 标注 → ASV 诊断 → 校正 → 因果估计评估）\n- Appendix B.18 的政治广告案例仅停留在 ASV 诊断层面\n- Abstract 最后一句 \"topology-aware analysis is necessary\" 缺乏真实数据支撑\n- 建议扩展 B.18 为完整端到端演示\n\n### Should-Fix\n\n**W1** [warning] Non-differential misclassification 假设在 LLM 场景下可能系统性违反\n- Appendix B.16 Table 15 显示安全阈值极紧——大多数数据集要求 ε < 0.02\n- 即使微小 differential misclassification 也可能使框架失效\n- 建议增加实证检验（检测 LLM 误差率与 Y 的条件独立性）\n\n**W2** [warning] Table 1 列定义模糊——\"Violation\" vs \"Sign Flip\"\n- IV 的 Sign Flip=52.6% > Violation=34.2% 看似反直觉\n- Abstract \"83.4% produce sign reversal\" 对应 Violation 列而非 Sign Flip 列，术语混用\n- 建议明确定义\n\n**W3** [warning] ASV 参数化假设类别间均匀退化，与 LLM 实际误差模式不符\n- C(δ) = (1-δ)I + δC₀ 假设所有类别以相同速率退化\n- LLM 误差通常高度非均匀——稀有类别误差率远高于频繁类别\n- 建议测试 class-specific δ_k 参数化\n\n**W4** [warning] Abstract 中 FWL invariance 声明缺少线性 OLS 限定条件\n- Abstract 说 \"provably ineffective\" 但未加 \"under linear OLS\"\n- Section 4.5 正文指出 logistic 下 invariance breaks but empirically < 0.005\n\n**W5** [warning] Theorem 1 的 proportional effects 假设限制性较强\n- f ⊥ g 时 OOB 率达 25%（Appendix B.13）\n- 实践者通常无法验证 proportional effects 是否成立\n- 建议讨论可验证性和退化行为\n\n### Questions\n1. Observation 1 \"< 0.005\" vs Table 10 \"0.011/0.031\" 数值不一致？\n2. 是否可设计 non-differential 假设的实证检验？\n3. ASV 在非均匀退化模式下排序是否仍一致？\n4. 当前主流 LLM（GPT-4, Claude 3.5）准确率是否已显著高于 0.45-0.81 范围？\n\n### 主要优势\n- S1: 首次系统研究 K≥3 多类标注误差在 7 种 DAG 拓扑下的因果偏差传播\n- S2: 三级证据层次科学透明\n- S3: 闭合形式偏差表达式为一般 K 推导\n- S4: FWL invariance 发现有明确实践指导意义\n- S5: Theory-MC MAPE 1.6% across 161 scenarios\n- S6: 附录 23 页完整证明和 15+ 项鲁棒性检查\n- S7: 23 个真实 LLM 配置的经验验证\n- S8: F1 与 causal bias 无显著相关的警示发现\n\n### Missing References\n- 未发现重大遗漏。可考虑补充近期 LLM calibration 文献。\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Questions 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] K≥3 ASV 单调性仅为猜想——论文最核心的实用贡献缺乏理论保证\n- Theorem 1 仅证明 K=2 在 proportional effects 下的 envelope monotonicity\n- K≥3 的 ASV 排序完全依赖 Conjecture 1\n- Observation 1 声称 \"worst-case deviations < 0.005\"，但 Table 10 中 confounding K=3 \"Worst mag.\" = 0.011，front-door = 0.031——存在表面不一致\n- 建议：(a) 至少对一个拓扑给出 K=3 解析证明；(b) 补充对抗性搜索；(c) 量化猜想失效时对 Algorithm 1 的影响\n\n**N2** [critical] 所有实验均为合成 DGP，缺乏真实观测数据的端到端因果分析验证\n- Section 4.4 \"Empirical Validation\" 仅验证理论预测与 MC 模拟一致性\n- 未在任何真实观测数据上运行完整因果分析流程（LLM 标注 → ASV 诊断 → 校正 → 因果估计评估）\n- Appendix B.18 的政治广告案例仅停留在 ASV 诊断层面\n- Abstract 最后一句 \"topology-aware analysis is necessary\" 缺乏真实数据支撑\n- 建议扩展 B.18 为完整端到端演示\n\n### Should-Fix\n\n**W1** [warning] Non-differential misclassification 假设在 LLM 场景下可能系统性违反\n- Appendix B.16 Table 15 显示安全阈值极紧——大多数数据集要求 ε < 0.02\n- 即使微小 differential misclassification 也可能使框架失效\n- 建议增加实证检验（检测 LLM 误差率与 Y 的条件独立性）\n\n**W2** [warning] Table 1 列定义模糊——\"Violation\" vs \"Sign Flip\"\n- IV 的 Sign Flip=52.6% > Violation=34.2% 看似反直觉\n- Abstract \"83.4% produce sign reversal\" 对应 Violation 列而非 Sign Flip 列，术语混用\n- 建议明确定义\n\n**W3** [warning] ASV 参数化假设类别间均匀退化，与 LLM 实际误差模式不符\n- C(δ) = (1-δ)I + δC₀ 假设所有类别以相同速率退化\n- LLM 误差通常高度非均匀——稀有类别误差率远高于频繁类别\n- 建议测试 class-specific δ_k 参数化\n\n**W4** [warning] Abstract 中 FWL invariance 声明缺少线性 OLS 限定条件\n- Abstract 说 \"provably ineffective\" 但未加 \"under linear OLS\"\n- Section 4.5 正文指出 logistic 下 invariance breaks but empirically < 0.005\n\n**W5** [warning] Theorem 1 的 proportional effects 假设限制性较强\n- f ⊥ g 时 OOB 率达 25%（Appendix B.13）\n- 实践者通常无法验证 proportional effects 是否成立\n- 建议讨论可验证性和退化行为\n\n### Questions\n1. Observation 1 \"< 0.005\" vs Table 10 \"0.011/0.031\" 数值不一致？\n2. 是否可设计 non-differential 假设的实证检验？\n3. ASV 在非均匀退化模式下排序是否仍一致？\n4. 当前主流 LLM（GPT-4, Claude 3.5）准确率是否已显著高于 0.45-0.81 范围？\n\n### 主要优势\n- S1: 首次系统研究 K≥3 多类标注误差在 7 种 DAG 拓扑下的因果偏差传播\n- S2: 三级证据层次科学透明\n- S3: 闭合形式偏差表达式为一般 K 推导\n- S4: FWL invariance 发现有明确实践指导意义\n- S5: Theory-MC MAPE 1.6% across 161 scenarios\n- S6: 附录 23 页完整证明和 15+ 项鲁棒性检查\n- S7: 23 个真实 LLM 配置的经验验证\n- S8: F1 与 causal bias 无显著相关的警示发现\n\n### Missing References\n- 未发现重大遗漏。可考虑补充近期 LLM calibration 文献。\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Questions 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-23T11:39:33.665603+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1461
}
```

</details>

---


### Assistant

_source line 1236 · 2026-05-23T11:39:36.666517+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 120

## Round 120

2 recorded events


### User

_source line 1237 · 2026-05-23T11:39:39.273280+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference）。

两个 must-fix 问题：
1. K≥3 ASV 单调性仅为猜想（Conjecture 1），论文最具实践价值的拓扑脆弱性排序和 Algorithm 1 缺乏理论保证
2. 所有实验均为合成 DGP，缺乏真实观测数据的端到端因果估计验证

五个 should-fix 问题：non-differential 假设敏感性、Table 1 列定义模糊、ASV 均匀退化参数化、Abstract FWL 声明缺少 OLS 限定、Theorem 1 proportional effects 假设的可验证性。

主要优势：首次系统覆盖 7 种 DAG 拓扑下 K≥3 误差传播、三级证据层次透明、MAPE 1.6% 的强 theory-MC 一致性、FWL invariance 发现具有直接实践价值。

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

_source line 1238 · 2026-05-23T11:39:43.677708+00:00_

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


## Round 121

## Round 121

2 recorded events


### User

_source line 1239 · 2026-05-23T11:42:45.217891+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 回应

### R2-N1: K≥3 ASV 单调性是 Conjecture 而非 Theorem

[AGREE] R2-N1: 与我的 R1-N1 一致，这是论文最大的理论缺口。

补充 R2 未提到的一个细节：Observation 1 (p.6) 声称 "worst-case deviations < 0.005"，但 Appendix Table 10 (p.27) 显示 front-door 的 worst magnitude 为 0.031，confounding 为 0.011——这三个数字之间存在表面不一致（我在 R1-W4 中已标记）。如果作者要回应 R2 的建议 (b)（量化 violation 参数空间特征），需要同时澄清这些数值之间的关系。

R2 提出的三个修改方向合理，特别是 (b)——量化 violation 的参数空间特征比追求完整证明更现实，也能更直接回应 "corner case 反例" 的担忧。

---

### R2-N2: 对 EMNLP 受众的可及性不足

[AGREE] R2-N2: R2 指出了一个我在 R1 中未充分强调的重要问题。

逐项验证 R2 的具体观察：

1. **plim**：确认 Abstract 和 Introduction 中隐含使用了 probability limit 概念（如 p.1 "we derive bias expressions" 实际描述的是 plim 行为），正式定义在 p.4 脚注 1。对不熟悉计量经济学的 NLP 读者，这一核心概念出现过晚。

2. **FWL 定理**：p.3 Section 3.1 仅用一句话解释 "The Frisch-Waugh-Lovell (FWL) theorem guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables"。这对于理解 Section 4.5 FWL invariance 论证至关重要，但解释确实不够。

3. **Wald estimator**：p.5 引入 IV 拓扑时直接写 "The Wald estimator (Angrist and Imbens, 1995) = cov(Y,A*)/cov(T,A*) has C in the denominator"，未解释其直觉（工具变量比率估计量）。

4. **E-value**：p.1 Introduction 提到 "E-values (VanderWeele and Ding, 2017)"，Remark 1 (p.6) 与 ASV 对比，但从未解释 E-value 的基本思想（衡量未观测混淆需要多强才能解释掉观察到的效应）。

5. **Abstract 信息密度**：确认 Abstract 在约 250 词内覆盖了 7 个拓扑 × sign reversal 分析 × ASV 框架 × 单调性层次 × correction methods × FWL invariance × 具体数字（83.4%, 2.1%, 1.6% MAPE, 210,000 matrices 等）。这对任何背景的读者都是高认知负荷。

**但我认为严重程度应为 should-fix 而非 must-fix**。理由：(a) *ACL venue 接受理论性较强的跨学科论文（如 Feder et al. 2022 同样使用大量因果推断术语），(b) 增加 Preliminaries 段落在 8 页限制下可能需要压缩 Method 或 Experiments，可能引入新问题。建议作者在 camera-ready 中优先解决 Abstract 精简和 E-value/FWL 直觉解释，这两项改动空间效率最高。

---

## Should-Fix 回应

### R2-W1: Non-differential stress test 仅在 exposure 拓扑下测试

[AGREE] R2-W1: Table 7 (p.24) 确实仅展示 exposure 拓扑的详细 stress test 结果。

**但需补充**：p.24 底部存在一段 R2 可能未注意到的文字——"Extended stress test. An extended stress test across 96 configurations (4 topologies × 4 ε levels × 6 perturbation types) confirms these patterns null." 该扩展测试覆盖了 4 个拓扑（confounding、exposure、mediation、collider），但结果仅以文字摘要呈现，未给出完整表格。

R2 的建议本质上合理：如果 Appendix 已经做了 4 拓扑的 extended stress test，应该将完整结果以表格形式呈现，而非仅文字总结。这是一个低成本的改进，可以直接回应 "仅在 exposure 上测试" 的质疑。

---

### R2-W2: 与核心 prior work 的增量区分不够清晰

[AGREE] R2-W2: 部分同意。R2 的三个子问题都有一定道理：

1. **Teblunthuis (2024) 对比**：Related Work (p.3) 提到 Teblunthuis (2024) 研究 "misclassification in automated content analysis causes bias in regression"，但未明确说明本文的 K-class 多拓扑分析与其单拓扑 binary 分析的具体技术差异。增加一个对比表格（如 Binary vs K-class、单拓扑 vs 7 拓扑、有无 FWL invariance 分析等）是合理建议。

2. **ASV vs E-value**：Remark 1 (p.6) 提供了三点对比——(i) topology-dependent vs single scalar, (ii) E-value 针对未观测混淆 vs ASV 针对分类误差, (iii) ASV 结构随 K 变化。三点都准确但各仅一句话，对于论文提出的新框架来说确实不够充分。建议至少展开第 (iii) 点，说明为什么 K≥3 维度使得 E-value 范式不直接适用。

3. **Correction guidance 的定位**：同意 R2 的观察——Section 4.5 更接近 "benchmark 式系统比较" 而非 "方法创新"。论文的方法创新在于 bias expressions 和 ASV 框架；correction guidance 的贡献是基于理论分析（FWL invariance）提供拓扑感知的方法选择指南（Algorithm 1）。建议作者在 Introduction 中更明确区分这两类贡献的性质。

---

### R2-W3: 实证验证的 LLM 和任务覆盖有限

[REBUT] R2-W3: 部分反驳。

R2 建议增加 NER、relation extraction、event detection 等任务。但这些任务的误差结构与论文框架根本不同：

- **NER/relation extraction** 是 span-level 或 pair-level 任务，误差表现为 span 边界错误、实体类型混淆、关系遗漏等，不能简单用 K×K 混淆矩阵建模。
- 论文框架明确限定于 **categorical variable misclassification**（Section 3.1, Definition 1, p.4），即对每个观测单位分配一个类别标签。这天然对应文本分类任务（sentiment, stance, hate speech, topic classification 等）。

因此，任务覆盖的局限不是实验设计的疏忽，而是框架适用范围的固有边界。论文 Limitations (p.8) 也提到 "our scope is observational"，但可以更明确说明框架仅适用于分类型标注。

**但 R2 有一个有效的子观点**：即使限于分类任务，3 个数据集（HumAID, VAST, CivilComments）的任务多样性确实不够。可以考虑增加 topic classification（如 AG News）或 natural language inference（如 MNLI）等分类任务的 LLM 混淆矩阵，以增加泛化说服力。23 个配置主要来自 3 个数据集 × 4 个 LLM × zero/few-shot 变体，混淆矩阵的结构多样性（对角线分布、off-diagonal 模式）确实受限于这 3 个任务的特性。

---

### R2-W4: Figure 2 和 Figure 3 的可读性

[AGREE] R2-W4: 完全同意。我在 R1-M3 中也标记了类似问题（针对 Figure 1）。

Figure 2 (p.7) 有 7 个子图排列在单栏宽度内，每个子图约 1.5cm 宽，x 轴标签在打印版确实难以辨认。Figure 3 的 y 轴标签 "Topology Determinism Bias, Vol F₁" 的含义不够直观——需要仔细阅读 caption 才能理解纵轴是相对偏差而横轴是 F1。灰度打印下的颜色区分也是实际问题。

---

### R2-W5: Algorithm 1 的阈值选择缺乏理论依据

[AGREE] R2-W5: 同意。

查看 Algorithm 1 (p.31) 的具体阈值：
- Step 1: `F̂ < 50/bias` (line 5) 和 `F̂ ∈ {Conf, Med, Coll, Front-door}` (line 9) — 这些基于 Proposition 1 的理论结果，有理论支撑
- Step 2: `PPI++ RMSE red. > 90.6%` (line 16) — 这是从 Table 4 的实验结果中提取的经验阈值
- `τ_conf > 0.7` — 来自 Table 7 的 stress test 结果

R2 正确指出 90.6% 和 0.7 等阈值是经验性的，且论文未讨论这些阈值对 DGP 参数的敏感性。当 DGP 参数变化时（如不同的效应大小、样本量、K 值），最优阈值可能不同。建议作者至少讨论这一局限性。

---

## Missing References 回应

[AGREE] R2-Missing-Ref: Imai, Keele, and Tingley (2010) "A General Approach to Causal Mediation Analysis" 确实是因果中介分析的奠基性工作，对 mediation 拓扑的讨论有参考价值。但论文已引用 VanderWeele (2015) 和 VanderWeele and Valeri (2013) 等覆盖因果中介的综合性参考文献，因此遗漏程度有限。建议在 camera-ready 中补充。

---

## Questions 回应

**Q1** (Conjecture 1 violation 在参数空间的分布): [AGREE] 这与我的 R1-Q1 一致，是关于 Conjecture 1 可信度的核心问题。

**Q2** (Differential misclassification 下 ASV ranking 稳定性): [AGREE] 这与我的 R1-W1 一致。Appendix B.16 Table 15 显示安全阈值极紧（ε < 0.02），说明框架对 differential misclassification 敏感，ASV ranking 在此条件下的稳定性值得研究。

**Q3** (K=10 PPI++ 退化是否意味着 Algorithm 1 需修改): [REBUT] Algorithm 1 (p.31) line 22-23 已明确处理了这一情况："If K > 5 then: MC-SIMEX is the most K-robust method, maintaining the top rank for 6/7 topologies at K=10 (vs. 3/7 at K=3)." 因此 Algorithm 1 已包含 K-specific 调整逻辑，不需要额外修改。R2 可能未注意到 Algorithm 1 的这一分支。

**Q4** (Logistic regression 下 FWL 等价性的 "practically negligible" 判断): [AGREE] 与我的 R1-W4 相关。Section 4.5 (p.8) 说 "under logistic regression the invariance breaks but empirically by < 0.005"，Table 5 (Appendix B.2) 给出具体数据。但 "< 0.005" 是否在所有 DGP 参数下成立需要更系统的验证——特别是在强非线性或极端 class imbalance 下。

---

## 总结：R1 与 R2 的共识与分歧

**共识点**：
- K≥3 ASV 单调性未证明是最大理论缺口（R1-N1 = R2-N1）
- Non-differential 假设的实践可信度需更充分讨论（R1-W1 ≈ R2-W1）
- Figure 可读性有改进空间（R1-M3 ≈ R2-W4）

**分歧点**：
- **R2-N2 (可及性) 的严重性**：R2 列为 must-fix，我认为应为 should-fix。8 页限制下增加 Preliminaries 可能压缩核心内容。
- **R2-W3 (任务覆盖)**：R2 要求增加 NER/RE/event detection，我认为这些超出框架的适用范围（categorical classification vs span-level tasks）。但同意在分类任务范围内增加数据集多样性。
- **R2-Q3 (K=10 Algorithm 1)**：R2 认为需修改，但 Algorithm 1 已有 K>5 的分支逻辑。

**R1 独有的关注点**（R2 未提及）：
- 缺乏真实观测数据的端到端因果分析验证（R1-N2）
- Table 1 "Violation" vs "Sign Flip" 列定义模糊（R1-W2）
- Observation 1 数值与 Table 10 的表面不一致（R1-W4）
- ASV 均匀退化参数化的局限（R1-W3）
- Abstract 中 FWL invariance 缺少 "linear OLS" 限定（R1-W4→更正：R1-W5 对应此处应为 W4）


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

_source line 1240 · 2026-05-23T11:42:54.991025+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 122

## Round 122

2 recorded events


### User

_source line 1241 · 2026-05-23T11:42:57.608930+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：R1 与 R2 在最大问题上形成共识（K≥3 单调性未证明），在 3 个点上有分歧（可及性严重程度、任务覆盖范围、Algorithm 1 K=10 处理）。我补充了 R2 未覆盖的 4 个独有关注点（真实数据验证缺失、Table 1 定义模糊、数值不一致、ASV 参数化局限）。

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

_source line 1242 · 2026-05-23T11:43:04.230846+00:00_

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


## Round 123

## Round 123

10 recorded events


### User

_source line 1243 · 2026-05-23T11:44:44.628042+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: K≥3 ASV 单调性仅为猜想**

同意，且 R1 发现了一个我此前未注意到的具体问题——Observation 1 与 Table 10 的数值不一致：

- Observation 1 (p.6) 声称 "worst-case deviations < 0.005 from strict monotonicity"
- Table 10 (p.27) 明确列出 confounding K=3 worst magnitude = 0.011，front-door K=3 = 0.031

0.011 和 0.031 都 > 0.005，构成表面矛盾。两处使用不同的矩阵数量（Observation 1: 30,000 triples; Table 10: 10,000 matrices），但更多矩阵应发现更大（而非更小）的偏差，无法解释这一差异。Conjecture 1 使用 ε ≤ 0.06 与 Table 10 一致，但 Observation 1 的 "< 0.005" 明显过于乐观。

这与我自己的 N1 担忧一致：Conjecture 1 作为 ASV 在 K≥3 下的理论基础，缺乏证明已经是一个 gap；加上正文（Observation 1）与附录（Table 10）数值不一致，进一步削弱了可信度。建议作者：(a) 修正 Observation 1 的数值以与 Table 10 一致；(b) 在特殊条件下给出 partial proof 或至少缩小 conjecture 的适用范围。

---

**[REBUT] R1-N2: 缺乏真实观测数据的端到端验证——同意方向但不同意 severity**

R1 的观察是准确的：Section 4.4 验证的是 theory-MC 一致性而非真实因果分析，Appendix B.18 的政治广告案例止步于 ASV 诊断而未运行完整的校正→因果估计流程。这确实限制了 "topology-aware analysis is necessary" 这一实践性 claim 的说服力。

但我认为这应为 **should-fix 而非 must-fix**，理由如下：

1. **论文的核心贡献是理论性的**（bias taxonomy + ASV framework + FWL invariance），三层验证结构（analytic predictions → MC simulation → real LLM confusion matrices）对理论贡献已经是高标准的验证。Section 4.2 的 Theory-MC MAPE < 1.65% across 161 scenarios (p.6-7) 和 Section 4.4 的 23 个真实 LLM 配置验证 (p.8, Figure 5 p.21) 为理论预测提供了充分的经验支持。

2. **ARR reviewer guidelines H13** 明确指出 "extra experiments aren't mandatory"，H16 指出 "acknowledged limitations aren't weaknesses"。Limitations section (p.8-9) 已承认验证范围有限。

3. **端到端真实数据验证的困难是结构性的**：要做完整的 ground-truth 因果效应评估，需要既有 gold-label annotations 又有 known causal effects 的数据集——这在社会科学中极难获得。要求这一验证可能不切实际。

**建议**：将 B.18 扩展为 should-fix 而非 must-fix。扩展方向可以是：在 B.18 案例中运行 correction methods (Table 4 中的 PPI++ 或 MC-SIMEX) 并报告校正前后的 causal estimate 变化，即使没有 ground truth 也能展示完整流程。

---

### Should-Fix

**[AGREE] R1-W1: Non-differential misclassification 假设可能被 LLM 系统性违反**

完全同意。R1 补充的具体证据强化了这一担忧：Appendix B.16 Table 15 (p.29) 显示大多数数据集的安全 differential 阈值 ε*_min 极紧（VAST: ε*=0.02, HumAnD: ε*<0.06），意味着即使 LLM 的分类准确率与 outcome 之间存在微小的条件依赖，框架结论就可能失效。

这与我自己的 W1 一致。我进一步补充：Appendix B.6 的 stress test (Table 7, p.24-25) 仅在 exposure 拓扑下进行。在 confounding 拓扑下（ASV 显示为 "robust"），non-differential violation 的影响可能不同——如果 confounding 在 mild violations 下也变得脆弱，将直接影响 ASV vulnerability ranking 的可靠性。

---

**[AGREE] R1-W2: Table 1 "Violation" vs "Sign Flip" 定义模糊**

R1 发现了一个我在 Round 1 中未充分关注的问题。Table 1 (p.7) 中：

- IV: Sign Flip = 52.6% > Violation = 34.2%

如果 "Violation" 指 sign preservation 条件被违反，"Sign Flip" 指 sign 实际反转，那么在逻辑上 Sign Flip ⊆ Violation（sign 只能在条件被违反时反转），应有 Sign Flip ≤ Violation。但 IV 的数据显示相反关系。

可能的解释是两列衡量不同的条件（如 "Violation" 可能仅指 Proposition 1 的 sufficient conditions 不满足，而 IV 不适用 Proposition 1 所以 "Violation" 衡量的是 first-stage singularity），但 **Table 1 的 caption 未显式定义 "Violation" 和 "Sign Flip" 两列的确切含义**。Abstract (p.1) 中 "83.4% produce sign reversal" 对应的是 exposure 的 Sign Flip 列，但未标明来源列名。

建议作者在 Table 1 caption 中增加每列的精确定义。

---

**[REBUT] R1-W3: ASV 参数化假设均匀退化——部分反驳**

R1 指出 C(δ) = (1-δ)I + δC₀ 假设所有类别以相同速率退化，与 LLM 对稀有类别误差率更高的实际模式不符。这个观察方向正确，但需要澄清参数化的实际含义：

1. **C₀ 本身可以是高度非均匀的**。C(δ) 中的 C₀ 是 reference confusion matrix，可以捕获任意的类别间误差不对称性。例如，如果 LLM 对 rare class 2 的 recall 远低于 common class 1，这会反映在 C₀ 的结构中。δ 控制的是从完美分类（I）到这个非均匀 C₀ 的插值程度。

2. **δ 的均匀性是 sensitivity analysis 的标准做法**。E-value (VanderWeele and Ding, 2017) 和 partial R² (Cinelli and Hazlett, 2020) 也使用单参数扰动进行 sensitivity analysis，这是为了获得可解释的单调性和可视化。引入 class-specific δ_k 会将参数空间从 1D 扩展到 (K-1)D，使 sensitivity analysis 的直觉解释性大幅下降。

3. **但 R1 的核心关切有道理**：在实践中，LLM 的退化模式确实是非均匀的（如 accuracy 降低时 rare class 先崩溃）。Section 4.4 (p.8) 使用的 23 个真实 LLM 配置的 confusion matrices 可以被视为对非均匀退化模式的隐式测试——这些矩阵来自不同 LLM 和 prompting 策略，自然包含非均匀误差结构。但论文未明确分析 ASV ranking 在这些非均匀矩阵下是否稳定。

**建议**：补充一个实验，用 real LLM confusion matrices 作为 C₀（而非 Dirichlet 随机矩阵），检验 ASV ranking 是否一致。这比引入 class-specific δ_k 更务实，且更贴近真实使用场景。

---

**[AGREE] R1-W4: Abstract 中 FWL invariance 声明缺少 "linear OLS" 限定**

同意。Abstract (p.1) 说 "matrix-based corrections are provably ineffective for four topologies due to Frisch-Waugh-Lovell invariance" 但未标注 "under linear OLS"。Section 4.5 (p.8) 和 Table 5 (p.22) 明确指出 logistic regression 下 FWL invariance 在数值上 breaks（|ΔSF| < 0.02, Appendix B.7），虽然偏差极小但 "provably ineffective" 的表述在非线性模型下不严格成立。这是一个小但重要的精度问题，应在 abstract 中加入 "under linear regression" 或 "under OLS" 限定词。

---

**[AGREE] R1-W5: Theorem 1 的 proportional effects 假设限制性较强**

同意 R1 的关切方向。Theorem 1 (p.6) 要求 f = λg（proportional effects），Appendix B.13 (p.28) 的 Table 12 显示在 fully independent（f ⊥ g）条件下 OOB 率升至约 25%，NLP-realistic DGP 下为 0.07%。

关键问题不在于 OOB 率本身（NLP-realistic 条件下 0.07% 是可接受的），而在于 **实践者通常无法先验地判断 proportional effects 是否成立**。论文提供了 NLP-realistic 参数下的数值证据，但未给出可验证的诊断标准——何时可以安全假设 proportional effects？

不过我认为这是 minor-to-should-fix 而非 critical，因为：(a) Theorem 1 的 proportional effects 假设是 sufficient condition，不是 necessary condition——即使假设不满足，monotonicity 仍可能成立；(b) 论文在 Appendix B.13 中提供了对 non-proportional 情况的全面数值分析。

---

### Questions 回应

**Q1: Observation 1 "< 0.005" vs Table 10 "0.011/0.031"**

如上 N1 分析，这是一个真实的数值不一致。我同意 R1 的观察，并将此作为 Observation 1 需要修正的证据。

**Q2: 是否可设计 non-differential 假设的实证检验？**

合理的问题。原则上可以通过检验 P(A*|A,Y) ≈ P(A*|A) 来验证——但这需要同时获得 gold labels A 和 outcomes Y，而 gold labels 的获取成本正是使用 LLM 标注的动机。一种折中方案是使用 Appendix B.16 Table 15 中的 ε*_min 阈值作为 sensitivity 指标，但这仍是间接的。我不认为存在 elegant 的直接检验方案。

**Q3: ASV 在非均匀退化模式下排序是否一致？**

如上 W3 分析。Figure 7 (p.21) 的右侧面板显示了 real LLM 配置下的 ASV 分布，各拓扑的相对排序与理论预测基本一致（confounding/collider/M-bias 稳健，exposure/IV 脆弱）。但论文未系统性地报告 ranking 一致性统计。

**Q4: 当前主流 LLM 准确率是否高于论文中的 0.45-0.81 范围？**

有效的实践性问题。2025-2026 年的 frontier LLMs（GPT-4o, Claude 3.5/4）在许多分类任务上准确率已超过 0.85-0.90，这可能使论文中基于 0.45-0.81 范围的分析显得保守。但论文的理论结果（bias expressions, sign reversal conditions）不依赖于特定准确率范围——它们在任何 confusion matrix 下成立。更高的准确率只是意味着 ASV 阈值更容易被满足。Appendix B.16 Table 15 的 differential thresholds 分析在高准确率场景下仍然适用。

---

### 对 R1 主要优势的回应

R1 列出的 8 项优势（S1-S8）与我的评估高度一致，尤其是：
- S1（首次系统研究 7 种拓扑）和 S4（FWL invariance 实践指导）是我认为的两个最强贡献
- S5（Theory-MC MAPE 1.6%）和 S6（23 页附录完整证明）印证了论文的 thoroughness
- S8（F₁ 与 causal bias 无显著相关）是我在 Round 1 中未充分强调的重要发现——Figure 3 (p.8) 显示 F₁ 与偏差的 Spearman 相关仅 ρ ≈ -0.10 (p = 0.45)，这对 NLP 实践者具有重要警示意义

---

### 综合评估

R1 和我的审稿意见在核心关切上高度收敛：Conjecture 1 的理论 gap、non-differential assumption 的实际适用性、对 EMNLP 受众的可及性。主要分歧在于 R1-N2（端到端验证）的 severity level——我认为 should-fix 更合适。

如果将 R1 和 R2 的意见合并，最关键的修改项为：
1. 修正 Observation 1 与 Table 10 的数值不一致（factual correction）
2. Conjecture 1 补充 partial proof 或更充分的 failure mode 分析
3. 增加 Preliminaries 段落提升可及性
4. 精简 Abstract

做到这些后，论文可从 3.5 提升至 Conference 水准。

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

_source line 1244 · 2026-05-23T11:45:15.654892+00:00_

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

_source line 1245 · 2026-05-23T11:45:15.856926+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T11:25:23.224666+00:00\", \"completed_at\": \"2026-05-23T11:25:27.003351+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-23T11:45:15.857340+00:00_

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

_source line 1247 · 2026-05-23T11:45:15.909377+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-23T11:50:06.285685+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 15\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R2-W3 再提（任务类型限于 sentiment/stance/toxicity）。R1 REBUT：NER/RE 超出框架范围（span-level vs categorical），但同意分类任务内数据集多样性不足。共识：should-fix（低优先级），Limitations 已覆盖。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor：stress test 合成但已有 B.5/B.6/B.16 三层验证。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-W1 + R2-W1 再提。R1 强调 Table 15 安全阈值极紧（ε<0.02），R2 强调 stress test 仅 exposure 拓扑有完整表格（extended test 4 拓扑仅文字摘要）。共识 should-fix：补充 confounding/mediation stress test 表格，讨论 LLM CoT 可能引入 differential bias。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 R2-N2 再提为 must-fix：Abstract 约 250 词覆盖 7 拓扑 + sign reversal + ASV + monotonicity + correction + FWL，信息密度极高。R1 AGREE 方向但认为 should-fix。Director 采纳 R1：should-fix（高优先级），Abstract 精简可在 camera-ready 完成。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-N2 列为 must-fix（缺乏真实数据端到端验证）。R2 REBUT 降为 should-fix：(1) 核心贡献是理论性的，三层验证对理论贡献已是高标准；(2) ARR H13 不要求额外实验；(3) 端到端验证需同时有 gold labels 和 known causal effects，结构性困难。Director 采纳 R2：should-fix。建议扩展 Appendix B.18 政治广告案例为完整校正流程。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 R2-W2 再提：Remark 1 的三点对比每个仅一句话，不够充分。R1 AGREE 但认为 correction guidance 定位应更明确区分（benchmark 式比较 vs 方法创新）。共识 should-fix。\"\n    action_items:\n      - round: 14\n        action: \"正文增加 Remark 或 Proposition 形式化说明 ASV 与 E-value 的数学结构区别\"\n        assigned_to: agent\n        status: done\n    resolution: \"Remark 1 新增三点形式化对比 + Table 18。R15 仍认为不够充分但降为 should-fix。\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 4.5 已包含机制解释。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出。\"\n    resolution: \"Section 4.5 已包含完整机制解释（protective attenuation removal）。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2 补充 NLP-realistic 0.07% sign failure rate。Director 降为 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-W5 再提：实践者无法先验验证 proportional effects 是否成立。R2 AGREE 但指出 (a) sufficient condition not necessary, (b) Appendix B.13 数值分析全面。共识 should-fix（minor-to-should-fix）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 合并到 R4-W6。R2-W2 再提但为 should-fix。\"\n    resolution: \"与 R4-W6 合并。Remark 1 + Table 18 已添加。R15 认为仍可改善但不阻塞接收。\"\n    resolution_round: 15\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被 R11 两位 Reviewer 赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加 Collider amplification 脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论 PPI++ 对 M-bias 有害。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1]\n        note: \"R15 R1-W3 再提：C(δ) 假设均匀退化，与 LLM 实际误差模式（稀有类别先崩溃）不符。R2 部分 REBUT：C₀ 本身捕获非均匀性，δ 是标准 sensitivity analysis 做法（类比 E-value）。但 R2 同意应补充 real LLM C₀ 下的 ASV ranking 稳定性检验。共识：should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"R11 未再提及。Algorithm 1 整体被两位 Reviewer 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。R2 成功 REBUT R1 的 critical 评级。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-N1 + R2-N1 均列为 critical。210,000 随机矩阵验证无法排除 corner case。R1 额外发现 Observation 1 与 Table 10 数值不一致（见 R15-N1）。两位共识：论文最大的理论缺口。建议 partial proof 或更充分的 failure mode 分析 + 对抗性搜索。\"\n    action_items:\n      - round: 14\n        action: \"Algorithm 1 脚注声明 + Conjecture 1 ε<0.06 限定为 under default DGP\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R6-M3 合并。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 与 R6-M3 合并。共识 should-fix。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R4-W6 合并。共识 should-fix。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 与 R4-W6 合并。R2-W2 认为 Remark 1 三点对比不够充分。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 NEW-1。R1-W1 + R2-W1 共识 should-fix。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。连续两轮未被 Reviewer 提出。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用 ding_vanderweele2016。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 合并到 R6-M3 和 NEW-1。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R6-M3 和 NEW-1。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 Director 采纳 R2：符号保持已在 logistic 下验证，降为 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-W4 指出 Abstract FWL 声明缺 'linear OLS' 限定。R2 AGREE。共识 should-fix（修复成本极低：加两个词）。\"\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：正文应更明确说明 K=2 凸性 + 单变量参数化 vs K≥3 多维参数空间。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R8-C1。两位 Reviewer 均列为 critical。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"R1 REBUT 成功。Introduction 措辞准确且有事实支撑。\"\n    resolution_round: 12\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 合并到 R1-W3。共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R1-W3。R1 REBUT NER/RE 超出范围但同意分类任务内多样性不足。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被 R11 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 4.5 已引用 ClinicalBERT。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出。连续两轮未被 Reviewer 提出。\"\n    resolution: \"Section 4.5 已引用 ClinicalBERT。连续三轮未被提出。\"\n    resolution_round: 15\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1 REBUT 建议降为 minor（目标读者应具备 CI 基础）。Director 保持 should-fix（低优先级）。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R2-N2 将可及性列为 must-fix：plim/FWL/Wald/E-value 四个核心概念解释不充分。R1 AGREE 方向但认为 should-fix：(a) ACL 接受跨学科论文，(b) 8 页限制下增加 Preliminaries 会压缩核心内容。Director 采纳 R1 降为 should-fix（高优先级）。建议 Abstract 精简 + E-value/FWL 直觉解释，这两项改动空间效率最高。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"EXP-2 完成：K=3/5/10 × 7 topologies。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix：仅消极建议（不校正），缺积极替代方案（bounds/robust IV）。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。Section 4.2 已添加 bounds approach/robust IV/two-sample 建议。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 已添加。\"\n    resolution_round: 13\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文 Section 5 (Conclusion) 溢出至 p9，违反 EMNLP 2026 的 8 页限制\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩，视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语（plim/FWL）对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R11-W2 合并。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 与 R11-W2 合并。Director 判定 should-fix（高优先级）。\"\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 均已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: minor\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果，适用条件未标注\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R2-W5 再提为 should-fix（阈值缺乏理论依据）。R1 AGREE。共识：阈值是经验性的且未讨论 DGP 敏感性。should-fix。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 和 Figure 7 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R2-W4 + R1-M3 再提：Figure 2 子图过小（7 个子图 single-column），灰度打印颜色区分困难。共识 minor。\"\n\n  # === Round 13 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract、Section 4.2、Appendix B.4 之间存在 factual 不一致\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"三处统一。\"\n    resolution_round: 14\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑（M-bias, front-door, IV）缺少 NLP 应用场景示例\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 3.2 已添加 NLP 场景。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出。连续两轮未被 Reviewer 提出。\"\n    resolution: \"Section 3.2 已为 M-bias/front-door 添加 NLP 场景。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R2]\n        note: \"R14 确认 Imai et al. 2010 和 Pryzant et al. 2021 均已引用。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 R2 再次提出 Imai et al. (2010)。查证：references.bib 已包含 imai_keele_tingley2010 和 imai_keele_yamamoto2010。Related Work p.3 已引用。无遗漏。\"\n    resolution: \"Imai et al. 2010 已在 references.bib 和 Related Work 中引用。\"\n    resolution_round: 15\n\n  - id: R13-CRIT1\n    category: soundness\n    severity: critical\n    summary: \"Limitations 中 diagonal accuracy 范围错误（0.61-0.83 → 应为 0.45-0.81）\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"0.45-0.81 与实际数据一致。Abstract 同步。\"\n    resolution_round: 14\n\n  # === Round 14 ===\n\n  - id: R14-W1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 的 Yes/Yes*/No 三级标注不够直观\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"已改为 Cond./Yes/No。\"\n    resolution_round: 15\n\n  - id: R14-W2\n    category: method\n    severity: should-fix\n    summary: \"IV 拓扑被标记为 maximally fragile 后缺少积极替代方案讨论\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。Section 4.2 已添加 bounds approach/robust IV/two-sample 建议。\"\n    resolution: \"Section 4.2 已添加三种积极替代方案。连续一轮未被提出。\"\n    resolution_round: 15\n\n  - id: R14-W3\n    category: presentation\n    severity: should-fix\n    summary: \"混淆矩阵 C 的可获得性——整个框架假设 C 已知或可估计\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。Limitations 已包含 gold-label bootstrapping 约束和 cross-validation 缓解。\"\n    resolution: \"Limitations 已覆盖。连续一轮未被提出。\"\n    resolution_round: 15\n\n  # === Round 15 新发现 ===\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case deviation < 0.005 与 Table 10 数值不一致（confounding 0.011, front-door 0.031）\"\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R1 发现，R2 交叉回应中确认。两处使用不同矩阵数量（30,000 vs 10,000），但更多矩阵应发现更大偏差。Observation 1 的 < 0.005 明显过于乐观。需修正 Observation 1 数值或澄清度量定义差异。\"\n    action_items:\n      - round: 15\n        action: \"修正 Observation 1 数值以与 Table 10 一致，或明确说明度量差异\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊，caption 未显式定义含义\"\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R1-W2 提出。R2 交叉回应 AGREE。Violation 和 Sign Flip 的包含关系不直观，需在 caption 中精确定义。\"\n    action_items:\n      - round: 15\n        action: \"Table 1 caption 增加 Violation 和 Sign Flip 列的精确定义\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R1-W4 提出，R2 AGREE。Abstract 说 'provably ineffective' 但 FWL 严格仅在 linear OLS 下成立。修复成本极低（加两个词）。\"\n    action_items:\n      - round: 15\n        action: \"Abstract 加 'under linear regression' 限定\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W3\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 经验阈值（90.6%, 0.7 等）缺乏理论依据和 DGP 敏感性讨论\"\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R2-W5 提出，R1 AGREE。阈值从 Table 4 和 Table 7 经验提取，未讨论 DGP 参数变化时的适用性。\"\n    action_items:\n      - round: 15\n        action: \"讨论 Algorithm 1 阈值选择的依据和敏感性\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null"
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
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 15\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R2-W3 再提（任务类型限于 sentiment/stance/toxicity）。R1 REBUT：NER/RE 超出框架范围（span-level vs categorical），但同意分类任务内数据集多样性不足。共识：should-fix（低优先级），Limitations 已覆盖。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor：stress test 合成但已有 B.5/B.6/B.16 三层验证。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-W1 + R2-W1 再提。R1 强调 Table 15 安全阈值极紧（ε<0.02），R2 强调 stress test 仅 exposure 拓扑有完整表格（extended test 4 拓扑仅文字摘要）。共识 should-fix：补充 confounding/mediation stress test 表格，讨论 LLM CoT 可能引入 differential bias。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 R2-N2 再提为 must-fix：Abstract 约 250 词覆盖 7 拓扑 + sign reversal + ASV + monotonicity + correction + FWL，信息密度极高。R1 AGREE 方向但认为 should-fix。Director 采纳 R1：should-fix（高优先级），Abstract 精简可在 camera-ready 完成。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-N2 列为 must-fix（缺乏真实数据端到端验证）。R2 REBUT 降为 should-fix：(1) 核心贡献是理论性的，三层验证对理论贡献已是高标准；(2) ARR H13 不要求额外实验；(3) 端到端验证需同时有 gold labels 和 known causal effects，结构性困难。Director 采纳 R2：should-fix。建议扩展 Appendix B.18 政治广告案例为完整校正流程。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 R2-W2 再提：Remark 1 的三点对比每个仅一句话，不够充分。R1 AGREE 但认为 correction guidance 定位应更明确区分（benchmark 式比较 vs 方法创新）。共识 should-fix。\"\n    action_items:\n      - round: 14\n        action: \"正文增加 Remark 或 Proposition 形式化说明 ASV 与 E-value 的数学结构区别\"\n        assigned_to: agent\n        status: done\n    resolution: \"Remark 1 新增三点形式化对比 + Table 18。R15 仍认为不够充分但降为 should-fix。\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 4.5 已包含机制解释。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出。\"\n    resolution: \"Section 4.5 已包含完整机制解释（protective attenuation removal）。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R2 补充 NLP-realistic 0.07% sign failure rate。Director 降为 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-W5 再提：实践者无法先验验证 proportional effects 是否成立。R2 AGREE 但指出 (a) sufficient condition not necessary, (b) Appendix B.13 数值分析全面。共识 should-fix（minor-to-should-fix）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 合并到 R4-W6。R2-W2 再提但为 should-fix。\"\n    resolution: \"与 R4-W6 合并。Remark 1 + Table 18 已添加。R15 认为仍可改善但不阻塞接收。\"\n    resolution_round: 15\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被 R11 两位 Reviewer 赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加 Collider amplification 脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论 PPI++ 对 M-bias 有害。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1]\n        note: \"R15 R1-W3 再提：C(δ) 假设均匀退化，与 LLM 实际误差模式（稀有类别先崩溃）不符。R2 部分 REBUT：C₀ 本身捕获非均匀性，δ 是标准 sensitivity analysis 做法（类比 E-value）。但 R2 同意应补充 real LLM C₀ 下的 ASV ranking 稳定性检验。共识：should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"R11 未再提及。Algorithm 1 整体被两位 Reviewer 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。R2 成功 REBUT R1 的 critical 评级。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-N1 + R2-N1 均列为 critical。210,000 随机矩阵验证无法排除 corner case。R1 额外发现 Observation 1 与 Table 10 数值不一致（见 R15-N1）。两位共识：论文最大的理论缺口。建议 partial proof 或更充分的 failure mode 分析 + 对抗性搜索。\"\n    action_items:\n      - round: 14\n        action: \"Algorithm 1 脚注声明 + Conjecture 1 ε<0.06 限定为 under default DGP\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R6-M3 合并。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 与 R6-M3 合并。共识 should-fix。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R4-W6 合并。共识 should-fix。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 与 R4-W6 合并。R2-W2 认为 Remark 1 三点对比不够充分。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 NEW-1。R1-W1 + R2-W1 共识 should-fix。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。连续两轮未被 Reviewer 提出。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用 ding_vanderweele2016。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 合并到 R6-M3 和 NEW-1。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R6-M3 和 NEW-1。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 Director 采纳 R2：符号保持已在 logistic 下验证，降为 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R1-W4 指出 Abstract FWL 声明缺 'linear OLS' 限定。R2 AGREE。共识 should-fix（修复成本极低：加两个词）。\"\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：正文应更明确说明 K=2 凸性 + 单变量参数化 vs K≥3 多维参数空间。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R8-C1。两位 Reviewer 均列为 critical。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"R1 REBUT 成功。Introduction 措辞准确且有事实支撑。\"\n    resolution_round: 12\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 合并到 R1-W3。共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R1-W3。R1 REBUT NER/RE 超出范围但同意分类任务内多样性不足。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被 R11 赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 4.5 已引用 ClinicalBERT。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出。连续两轮未被 Reviewer 提出。\"\n    resolution: \"Section 4.5 已引用 ClinicalBERT。连续三轮未被提出。\"\n    resolution_round: 15\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 R1 REBUT 建议降为 minor（目标读者应具备 CI 基础）。Director 保持 should-fix（低优先级）。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R2-N2 将可及性列为 must-fix：plim/FWL/Wald/E-value 四个核心概念解释不充分。R1 AGREE 方向但认为 should-fix：(a) ACL 接受跨学科论文，(b) 8 页限制下增加 Preliminaries 会压缩核心内容。Director 采纳 R1 降为 should-fix（高优先级）。建议 Abstract 精简 + E-value/FWL 直觉解释，这两项改动空间效率最高。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"EXP-2 完成：K=3/5/10 × 7 topologies。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix：仅消极建议（不校正），缺积极替代方案（bounds/robust IV）。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。Section 4.2 已添加 bounds approach/robust IV/two-sample 建议。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 4 个 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 已添加。\"\n    resolution_round: 13\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文 Section 5 (Conclusion) 溢出至 p9，违反 EMNLP 2026 的 8 页限制\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩，视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语（plim/FWL）对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 与 R11-W2 合并。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 与 R11-W2 合并。Director 判定 should-fix（高优先级）。\"\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"VanderWeele (2015) 和 Schennach (2020) 均已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: minor\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果，适用条件未标注\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R2-W5 再提为 should-fix（阈值缺乏理论依据）。R1 AGREE。共识：阈值是经验性的且未讨论 DGP 敏感性。should-fix。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 和 Figure 7 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 R2-W4 + R1-M3 再提：Figure 2 子图过小（7 个子图 single-column），灰度打印颜色区分困难。共识 minor。\"\n\n  # === Round 13 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract、Section 4.2、Appendix B.4 之间存在 factual 不一致\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"三处统一。\"\n    resolution_round: 14\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑（M-bias, front-door, IV）缺少 NLP 应用场景示例\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。Section 3.2 已添加 NLP 场景。\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出。连续两轮未被 Reviewer 提出。\"\n    resolution: \"Section 3.2 已为 M-bias/front-door 添加 NLP 场景。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [R2]\n        note: \"R14 确认 Imai et al. 2010 和 Pryzant et al. 2021 均已引用。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 R2 再次提出 Imai et al. (2010)。查证：references.bib 已包含 imai_keele_tingley2010 和 imai_keele_yamamoto2010。Related Work p.3 已引用。无遗漏。\"\n    resolution: \"Imai et al. 2010 已在 references.bib 和 Related Work 中引用。\"\n    resolution_round: 15\n\n  - id: R13-CRIT1\n    category: soundness\n    severity: critical\n    summary: \"Limitations 中 diagonal accuracy 范围错误（0.61-0.83 → 应为 0.45-0.81）\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"0.45-0.81 与实际数据一致。Abstract 同步。\"\n    resolution_round: 14\n\n  # === Round 14 ===\n\n  - id: R14-W1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 的 Yes/Yes*/No 三级标注不够直观\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"已改为 Cond./Yes/No。\"\n    resolution_round: 15\n\n  - id: R14-W2\n    category: method\n    severity: should-fix\n    summary: \"IV 拓扑被标记为 maximally fragile 后缺少积极替代方案讨论\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。Section 4.2 已添加 bounds approach/robust IV/two-sample 建议。\"\n    resolution: \"Section 4.2 已添加三种积极替代方案。连续一轮未被提出。\"\n    resolution_round: 15\n\n  - id: R14-W3\n    category: presentation\n    severity: should-fix\n    summary: \"混淆矩阵 C 的可获得性——整个框架假设 C 已知或可估计\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"R15 未单独提出。Limitations 已包含 gold-label bootstrapping 约束和 cross-validation 缓解。\"\n    resolution: \"Limitations 已覆盖。连续一轮未被提出。\"\n    resolution_round: 15\n\n  # === Round 15 新发现 ===\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case deviation < 0.005 与 Table 10 数值不一致（confounding 0.011, front-door 0.031）\"\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R1 发现，R2 交叉回应中确认。两处使用不同矩阵数量（30,000 vs 10,000），但更多矩阵应发现更大偏差。Observation 1 的 < 0.005 明显过于乐观。需修正 Observation 1 数值或澄清度量定义差异。\"\n    action_items:\n      - round: 15\n        action: \"修正 Observation 1 数值以与 Table 10 一致，或明确说明度量差异\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊，caption 未显式定义含义\"\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R1-W2 提出。R2 交叉回应 AGREE。Violation 和 Sign Flip 的包含关系不直观，需在 caption 中精确定义。\"\n    action_items:\n      - round: 15\n        action: \"Table 1 caption 增加 Violation 和 Sign Flip 列的精确定义\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R1-W4 提出，R2 AGREE。Abstract 说 'provably ineffective' 但 FWL 严格仅在 linear OLS 下成立。修复成本极低（加两个词）。\"\n    action_items:\n      - round: 15\n        action: \"Abstract 加 'under linear regression' 限定\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W3\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 经验阈值（90.6%, 0.7 等）缺乏理论依据和 DGP 敏感性讨论\"\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R2-W5 提出，R1 AGREE。阈值从 Table 4 和 Table 7 经验提取，未讨论 DGP 参数变化时的适用性。\"\n    action_items:\n      - round: 15\n        action: \"讨论 Algorithm 1 阈值选择的依据和敏感性\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-23T11:50:06.386850+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 29859}, \"error\": \"\"}"}

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

_source line 1250 · 2026-05-23T11:53:01.440272+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Round 15（Fresh Review）\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: 重新审稿（fresh）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验完整性; R2: 新颖性+完整性+表达）\n**交叉分享**: 完成（1 轮即收敛）\n**日期**: 2026-05-23\n\n---\n\n## Summary\n\n本文研究 K-class LLM 标注误差（非差分误分类）在 7 种典型 DAG 拓扑下对因果估计的偏差传播。主要贡献：(1) 推导 7 种拓扑的闭合形式偏差表达式，证明 K≥3 引入结构性 sign reversal（二元情形不存在）；(2) 提出 Annotation Sensitivity Values (ASV) 框架，给出拓扑依赖的脆弱性排序（IV 最脆弱，M-bias 免疫）；(3) 证明 FWL invariance 使矩阵校正对 4 种协变量拓扑无效，提供拓扑感知的校正指南。K=2 的 ASV 单调性有严格证明（Theorem 1），K≥3 仅有数值验证支撑的 Conjecture 1。实验在合成 DGP + 23 个真实 LLM 混淆矩阵上验证，Theory-MC MAPE 1.6%。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] 首次系统研究 K≥3 多类标注误差在 7 种 DAG 拓扑下的因果偏差传播，对 binary-only 文献（Wood-Doughty 2018/2024, Teblunthuis 2024）是实质性扩展。选题重要且时机恰当——LLM 标注在 CSS 中快速普及。\n\n**S2** [R1+R2 共识] 三级证据层次（proved / numerically verified / conjectured）科学透明，避免常见的过度声明。两位 Reviewer 均赞为方法论美德。\n\n**S3** [R1] 7 种拓扑的闭合形式偏差表达式（Eqs. 1-3 及 Appendix A.3-A.8）为一般 K 推导，理论贡献扎实。\n\n**S4** [R1+R2 共识] FWL invariance 负结果（Section 4.5）——矩阵校正对 4 种协变量拓扑 exactly 0% bias reduction——具有直接实践指导意义，回答了\"不应该做什么\"。\n\n**S5** [R1] Theory-MC 一致性 MAPE 1.6% across 161 scenarios（23 LLM configs × 7 topologies），验证规模充分、精度高。\n\n**S6** [R1] 23 页附录包含完整证明、15+ 项鲁棒性检查（非线性 DGP、cross-K、bootstrap CI、non-differential stress test 等），学术严谨度出色。\n\n**S7** [R2] K≥3 sign reversal 发现（83.4% under uniform Dirichlet, 2.1% under realistic accuracy）对多类标注场景的 CSS 实践者有直接警示价值。\n\n**S8** [R1+R2 共识] F₁ 与 causal bias 无显著相关（Spearman ρ = −0.10, p = 0.45, Figure 5）——标准分类指标不能替代拓扑感知的因果分析，对 NLP 实践者有重要警示。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-MF1** [R1-N1 + R2-N1, 共识 critical] **K≥3 ASV 单调性仅为 Conjecture，论文最核心的实用贡献缺乏理论保证**\n\nTheorem 1 仅证明 K=2 在 proportional effects 下的 envelope monotonicity。对于论文标题强调的 \"Multi-Class\"（K≥3）情形，ASV 的拓扑脆弱性排序和 Algorithm 1 校正指南完全依赖 Conjecture 1（ε-approximate monotonicity, ε < 0.06），该猜想仅有 210,000 随机矩阵的数值支撑。随机采样无法排除特定对抗性矩阵结构导致单调性失效的可能。\n\n**附加事实性问题**（R1 发现，R2 确认）：Observation 1 (p.6) 声称 \"worst-case deviations < 0.005\"，但 Table 10 (Appendix, p.27) 显示 confounding K=3 worst magnitude = 0.011，front-door = 0.031——构成表面数值矛盾。两处使用不同矩阵数量（30,000 vs 10,000），但更多矩阵应发现更大偏差，无法解释差异。\n\n建议修改方向：(a) 修正 Observation 1 数值或澄清度量定义差异；(b) 补充对抗性搜索（gradient-based optimization over column-stochastic C），而非仅 Dirichlet 随机采样；(c) 量化 violation 的参数空间特征——ε < 0.06 集中在什么类型的矩阵？real LLM 中是否出现过？(d) 讨论 violation 时 ASV ranking 的实际鲁棒性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W-SF1** [R2-N2 提出 must-fix, R1 AGREE 但降为 should-fix; Director 采纳 should-fix（高优先级）] **对 EMNLP 受众的可及性不足**\n\n计量经济学术语（plim, FWL, Wald estimator, E-value, column-stochastic）解释不充分。plim 在 Abstract/Introduction 隐含使用但正式定义在 p.4 脚注 1；FWL 作为核心概念仅 p.3 一句话解释；E-value 未解释基本思想就与 ASV 对比。Abstract 在约 250 词内覆盖 7 拓扑 × sign reversal × ASV × monotonicity × correction × FWL + 大量具体数字，认知负荷极高。\n\nDirector 裁决：降为 should-fix，理由：(a) ACL venue 接受跨学科论文（如 Feder et al. 2022），(b) 8 页限制下增加 Preliminaries 可能压缩核心内容。建议优先：Abstract 精简（保留 1-2 核心发现）+ E-value/FWL 直觉解释（各 1-2 句），空间效率最高。\n\n**W-SF2** [R1-N2 提出 must-fix, R2 REBUT 降为 should-fix; Director 采纳 should-fix] **缺乏真实观测数据的端到端因果分析验证**\n\n所有实验均为合成线性 SEM + 注入真实 LLM 混淆矩阵。Section 4.4 \"Empirical Validation\" 验证的是 theory-MC 一致性，未在任何真实观测数据上运行完整因果分析流程（LLM 标注 → ASV 诊断 → 校正 → 因果估计评估）。Appendix B.18 政治广告案例仅停留在 ASV 诊断层面。\n\nDirector 裁决：降为 should-fix，理由：(a) 核心贡献是理论性的，三层验证已是高标准；(b) 端到端验证需同时有 gold labels 和 known causal effects，结构性困难；(c) ARR H13 不要求额外实验。建议将 B.18 扩展为完整校正流程演示。\n\n**W-SF3** [R1-W1 + R2-W1, 共识 should-fix] **Non-differential misclassification 假设的适用性讨论和验证不够充分**\n\nTable 15 (Appendix B.16) 显示安全阈值极紧——多数数据集要求 ε < 0.02。Stress test (Table 7, Appendix B.6) 仅 exposure 拓扑有完整表格，extended 4-topology test 仅文字摘要无表格。LLM 可能通过上下文间接获取 Y 信号，few-shot 示例可能引入 differential bias。\n\n建议：(a) 将 extended stress test 4 拓扑结果以表格呈现；(b) 讨论 LLM CoT/few-shot 可能引入的 differential patterns；(c) 给出定量指导——超过什么阈值时结论不可靠。\n\n**W-SF4** [R2-W2, R1 AGREE] **与核心 prior work 的增量区分不够清晰**\n\nRemark 1 (p.6) 的 ASV vs E-value 三点对比各仅一句话，不够充分。Correction guidance 的贡献性质（benchmark 式比较 vs 方法创新）定位不清。建议增加结构化对比表。\n\n**W-SF5** [R1-W5, R2 AGREE] **Theorem 1 的 proportional effects 假设限制性强且实践中难以验证**\n\nf ⊥ g 时 OOB 率达 25%（Appendix B.13），NLP-realistic 下 0.07%。但实践者无法先验验证 proportional effects 是否成立。R2 补充：sufficient condition not necessary，Appendix B.13 数值分析全面。共识 should-fix（偏 minor）。\n\n**W-SF6** [R1-W4, R2 AGREE] **Abstract FWL invariance 声明缺少 \"under linear OLS\" 限定**\n\nAbstract \"provably ineffective\" 未标注 FWL 严格仅在 linear OLS 下成立。Logistic 下 breaks（|ΔSF| < 0.02, Table 5）。修复成本极低。\n\n**W-SF7** [R2-W5, R1 AGREE] **Algorithm 1 经验阈值缺乏理论依据**\n\n90.6% RMSE reduction、τ_conf > 0.7 等阈值从 Table 4/7 经验提取，未讨论对不同 DGP 参数的敏感性。\n\n**W-SF8** [R1-W2, R2 AGREE] **Table 1 Violation vs Sign Flip 列定义模糊**\n\nCaption 未显式定义两列含义，Violation 和 Sign Flip 的包含关系不直观。\n\n### Minor\n\n**W-MI1** [R1-M3 + R2-W4, 共识] Figure 2 子图过小（7 个子图 single-column），灰度打印颜色区分困难。Figure 3 y 轴标签不够直观。\n\n**W-MI2** [R1-W3, R2 部分 REBUT] ASV 参数化 C(δ) 假设均匀退化。R2 澄清 C₀ 本身捕获非均匀性、δ 是标准做法；但同意应补充 real LLM C₀ 下的 ranking 稳定性检验。\n\n**W-MI3** [R1-M1] 符号密度高（约 20 个符号），可考虑正文增加 notation summary。\n\n**W-MI4** [R1-M2] Algorithm 1 是最具实践价值的输出之一，但被放在 Appendix 最后一页。建议正文 Section 4.5 中放置简化版。\n\n**W-MI5** [R2 minor] Abstract \"seven canonical\" 的 canonical 选取标准未解释。\n\n**W-MI6** [R2 minor] Figure 1 caption \"starred-node\" 含义应在 caption 内解释。\n\n**W-MI7** [R2 minor] 匿名审稿阶段建议提供 anonymous repository 链接供 reproducibility 验证。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 通过交叉分享达成的共识：\n\n1. **[AGREE] K≥3 ASV 单调性未证明是论文最大的理论缺口**（R1-N1 = R2-N1）。Observation 1 与 Table 10 的数值不一致进一步削弱可信度。\n2. **[AGREE] Non-differential 假设的实践可信度需更充分讨论和验证**（R1-W1 ≈ R2-W1）。Stress test 完整表格仅覆盖 exposure 拓扑。\n3. **[AGREE] Abstract 信息密度过高，计量术语解释不充分**（方向一致，severity 分歧见下）。\n4. **[AGREE] Figure 可读性有改进空间**（R1-M3 = R2-W4）。\n5. **[AGREE] Abstract FWL invariance 应加 \"under linear OLS\"**（R1-W4, R2 AGREE）。\n6. **[AGREE] Algorithm 1 阈值是经验性的**（R2-W5, R1 AGREE）。\n7. **[AGREE] Table 1 列定义需明确**（R1-W2, R2 AGREE）。\n8. **[AGREE] ASV vs E-value 对比不够充分**（R2-W2, R1 AGREE）。\n9. **[AGREE] 三级证据层次是方法论美德**（S2）。\n10. **[AGREE] FWL invariance 负结果有独立实践价值**（S4）。\n\n---\n\n## Reviewer Divergence\n\n1. **EMNLP 受众可及性的严重程度**：R2 列为 must-fix（EMNLP 主流读者无法 follow 方法论会限制 impact），R1 降为 should-fix（ACL 接受跨学科论文，8 页限制下增加 Preliminaries 会压缩核心内容）。**Director 裁决：should-fix（高优先级）**。R1 的页面约束论点成立，但 R2 对受众匹配的担忧合理。建议低空间成本的改进：Abstract 精简 + 关键术语直觉解释。\n\n2. **真实数据端到端验证的严重程度**：R1 列为 must-fix（Abstract \"topology-aware analysis is necessary\" 缺乏真实数据支撑），R2 降为 should-fix（核心贡献是理论性的，端到端验证存在结构性困难）。**Director 裁决：should-fix**。R2 的三个论点（理论贡献的验证标准、ARR H13、ground truth 获取困难）更有说服力。\n\n3. **任务覆盖范围**：R2 建议增加 NER/RE/event detection 任务。R1 REBUT——这些是 span-level 任务，超出 K×K 混淆矩阵框架的适用范围，但同意分类任务内数据集多样性不足。**Director 裁决：采纳 R1 的 REBUT**。NER/RE 确实超出框架范围。但在分类任务内增加数据集多样性（如 topic classification, NLI）是合理的低优先级建议。\n\n---\n\n## Questions\n\n以下为需要作者回应的关键问题（按优先级排序）：\n\n1. **[R1+R2] Observation 1 数值澄清**：Observation 1 \"< 0.005\"、Conjecture 1 \"ε < 0.06\"、Table 10 \"0.011/0.031\" 三者之间的关系？使用的偏差度量是否相同？\n\n2. **[R1+R2] Conjecture 1 violation 分布**：ε < 0.06 的 violations 在 confusion matrix 参数空间中的分布如何？集中在对角占优度极低的区域？这类矩阵在 23 个 LLM 配置中出现过吗？\n\n3. **[R1+R2] Differential misclassification 下 ASV ranking 稳定性**：在 outcome-dependent 分类偏差（ε = 0.03-0.05）下，ASV vulnerability ranking 是否仍稳定？\n\n4. **[R1] 当前主流 LLM 准确率**：GPT-4o/Claude 在同类任务上准确率是否已显著高于 0.45-0.81？如是，框架警示在多大程度上仍适用？\n\n5. **[R2] Logistic FWL 等价性**：Table 5 的 \"practically negligible\"（< 0.005）判断是否依赖 DGP 参数？是否存在使 deviation 变得 substantial 的参数配置？\n\n---\n\n## Missing References\n\n**R2 提出**：Imai, Keele, and Tingley (2010) \"A General Approach to Causal Mediation Analysis\"。R1 确认遗漏程度有限（VanderWeele 2015 等已覆盖因果中介）。**查证**：references.bib 已包含 imai_keele_tingley2010 和 imai_keele_yamamoto2010，Related Work p.3 已引用。实际未遗漏。\n\n**R1**：未发现重大引用遗漏。可考虑补充近期 LLM calibration 文献。\n\n**Director 结论**：无关键引用遗漏。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中未开启 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因配额限制未能完成实际页面检查（error: \"You've hit your limit · resets 4pm (UTC)\"）。格式合规性由两位 Reviewer 人工确认：\n- ✅ 正文 8 页（Sections 1-5 + Limitations），符合 EMNLP 2026 Long Paper 限制\n- ✅ Limitations section 存在（p.8-9），覆盖 3 个主要局限\n- ✅ Double-blind 合规——\"Anonymous ACL submission\"，无身份信息泄露\n- ✅ 引用格式正确，ACL 模板\n- ✅ 附录 23 页，包含完整证明和补充实验\n- ⚠️ Figure 2 子图过小（7 个子图 single-column），灰度打印颜色区分困难\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**置信度: 4/5**（两位 Reviewer 均给出 4/5 置信度，交叉分享后在核心问题上达成共识）\n\n**评分理由**：\n\n论文解决了一个重要且未被系统研究的问题——K-class LLM annotation error 在因果推断中的 topology-dependent 传播。工作量巨大（7 拓扑 × K-class × 3 ASV × 5 校正方法 × 23 页附录），三级证据层次和 FWL invariance 负结果均有独立方法论价值。\n\n然而，论文最核心的实用贡献——K≥3 下 ASV 的拓扑脆弱性排序——依赖未证明的 Conjecture 1，且正文（Observation 1）与附录（Table 10）存在数值不一致，削弱可信度。对 EMNLP 受众的可及性不足（计量术语解释不充分、Abstract 过于密集）可能限制实际 impact。\n\n**从 3.5 提升至 4.0 (Conference) 的关键路径**：\n1. 修正 Observation 1 与 Table 10 的数值矛盾（factual correction，最低成本）\n2. 为 Conjecture 1 补充 failure mode 分析（violation 集中区域、ranking 鲁棒性）或 partial proof\n3. Abstract 精简 + 关键术语（plim/FWL/E-value）增加直觉解释\n4. Abstract 加 \"under linear regression\" 限定 FWL 声明\n\n以上 4 项中，第 1 和第 4 项可在 rebuttal/camera-ready 中即时完成，第 3 项可在 camera-ready 中完成，第 2 项需要一定的技术工作但不需要新实验。\n\n---\n\n## Detailed Comments\n\n### Abstract (p.1)\n- 约 250 词，覆盖概念过多。建议精简至 3 个核心发现：(1) K≥3 sign reversal, (2) topology-dependent vulnerability ranking, (3) FWL invariance negative result。具体数字（83.4%, 2.1%, 52.6%, 210,000, 1.6% MAPE 等）保留 2-3 个最有冲击力的即可。\n- \"matrix-based corrections are provably ineffective\" 需加 \"under linear regression\"。\n\n### Section 1 Introduction (pp.1-2)\n- 叙事结构清晰（problem → gap → contribution → evidence）。\n- Contribution 3（correction guidance）的性质定位不清——是方法创新还是 benchmark 式比较？建议明确区分。\n\n### Section 2 Related Work (pp.2-3)\n- 引用覆盖充分，涵盖测量误差、因果推断、NLP 标注质量三条文献线。\n- 与 Teblunthuis (2024) 和 Lee et al. (2024) 的技术增量可更具体（如对比表）。\n\n### Section 3 Method (pp.3-6)\n- Bias expressions (Eqs. 1-3) 推导清晰，一般 K 下成立。\n- Proposition 1 (sign preservation)：confounding 和 collider 的解析证明完整正确。条件 \"|τ| > √...\" 缺少直觉解释。\n- Theorem 1 (K=2 monotonicity)：证明利用 perspective function 凸性，技术上正确。Proportional effects 假设的讨论可更充分（可验证性和退化行为）。\n- Observation 1 (K≥3 monotonicity)：\"< 0.005\" 与 Table 10 不一致，需修正。\n- Conjecture 1 (ε-approximate)：数值验证规模（210,000 矩阵）充分但缺乏对抗性搜索。\"under default DGP parameters\" 限定适当。\n- Remark 1 (ASV vs E-value)：三点对比每个仅一句话，不够充分。\n\n### Section 4 Experiments (pp.6-8)\n- Theory-MC MAPE 1.6% 精度高。\n- Table 1 Violation/Sign Flip 列定义需在 caption 中明确。\n- Figure 5 (F₁ vs bias)：信息传达有效。\n- Section 4.5 correction guidance：FWL invariance 论证清晰。PPI++ M-bias 有害的机制解释（protective attenuation removal）到位。\n- Algorithm 1 在 Appendix 最后一页，建议正文放简化版。\n\n### Section 5 Conclusion + Limitations (p.8-9)\n- Conclusion 简洁恰当。\n- Limitations 覆盖 3 个主要局限（non-differential 假设、线性 SEM、观测范围），长度适当。Gold-label bootstrapping 约束已提及。\n- 可补充：Algorithm 1 阈值的 DGP 依赖性。\n\n### Appendix (pp.9-31)\n- 完整证明（7 拓扑 sign preservation + Theorem 1 monotonicity），15+ 鲁棒性检查。\n- Table 10 与 Observation 1 数值需对齐。\n- B.18 政治广告案例可扩展为完整校正流程。",
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
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
    "report": "# 审稿报告：Round 15（Fresh Review）\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: 重新审稿（fresh）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验完整性; R2: 新颖性+完整性+表达）\n**交叉分享**: 完成（1 轮即收敛）\n**日期**: 2026-05-23\n\n---\n\n## Summary\n\n本文研究 K-class LLM 标注误差（非差分误分类）在 7 种典型 DAG 拓扑下对因果估计的偏差传播。主要贡献：(1) 推导 7 种拓扑的闭合形式偏差表达式，证明 K≥3 引入结构性 sign reversal（二元情形不存在）；(2) 提出 Annotation Sensitivity Values (ASV) 框架，给出拓扑依赖的脆弱性排序（IV 最脆弱，M-bias 免疫）；(3) 证明 FWL invariance 使矩阵校正对 4 种协变量拓扑无效，提供拓扑感知的校正指南。K=2 的 ASV 单调性有严格证明（Theorem 1），K≥3 仅有数值验证支撑的 Conjecture 1。实验在合成 DGP + 23 个真实 LLM 混淆矩阵上验证，Theory-MC MAPE 1.6%。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] 首次系统研究 K≥3 多类标注误差在 7 种 DAG 拓扑下的因果偏差传播，对 binary-only 文献（Wood-Doughty 2018/2024, Teblunthuis 2024）是实质性扩展。选题重要且时机恰当——LLM 标注在 CSS 中快速普及。\n\n**S2** [R1+R2 共识] 三级证据层次（proved / numerically verified / conjectured）科学透明，避免常见的过度声明。两位 Reviewer 均赞为方法论美德。\n\n**S3** [R1] 7 种拓扑的闭合形式偏差表达式（Eqs. 1-3 及 Appendix A.3-A.8）为一般 K 推导，理论贡献扎实。\n\n**S4** [R1+R2 共识] FWL invariance 负结果（Section 4.5）——矩阵校正对 4 种协变量拓扑 exactly 0% bias reduction——具有直接实践指导意义，回答了\"不应该做什么\"。\n\n**S5** [R1] Theory-MC 一致性 MAPE 1.6% across 161 scenarios（23 LLM configs × 7 topologies），验证规模充分、精度高。\n\n**S6** [R1] 23 页附录包含完整证明、15+ 项鲁棒性检查（非线性 DGP、cross-K、bootstrap CI、non-differential stress test 等），学术严谨度出色。\n\n**S7** [R2] K≥3 sign reversal 发现（83.4% under uniform Dirichlet, 2.1% under realistic accuracy）对多类标注场景的 CSS 实践者有直接警示价值。\n\n**S8** [R1+R2 共识] F₁ 与 causal bias 无显著相关（Spearman ρ = −0.10, p = 0.45, Figure 5）——标准分类指标不能替代拓扑感知的因果分析，对 NLP 实践者有重要警示。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-MF1** [R1-N1 + R2-N1, 共识 critical] **K≥3 ASV 单调性仅为 Conjecture，论文最核心的实用贡献缺乏理论保证**\n\nTheorem 1 仅证明 K=2 在 proportional effects 下的 envelope monotonicity。对于论文标题强调的 \"Multi-Class\"（K≥3）情形，ASV 的拓扑脆弱性排序和 Algorithm 1 校正指南完全依赖 Conjecture 1（ε-approximate monotonicity, ε < 0.06），该猜想仅有 210,000 随机矩阵的数值支撑。随机采样无法排除特定对抗性矩阵结构导致单调性失效的可能。\n\n**附加事实性问题**（R1 发现，R2 确认）：Observation 1 (p.6) 声称 \"worst-case deviations < 0.005\"，但 Table 10 (Appendix, p.27) 显示 confounding K=3 worst magnitude = 0.011，front-door = 0.031——构成表面数值矛盾。两处使用不同矩阵数量（30,000 vs 10,000），但更多矩阵应发现更大偏差，无法解释差异。\n\n建议修改方向：(a) 修正 Observation 1 数值或澄清度量定义差异；(b) 补充对抗性搜索（gradient-based optimization over column-stochastic C），而非仅 Dirichlet 随机采样；(c) 量化 violation 的参数空间特征——ε < 0.06 集中在什么类型的矩阵？real LLM 中是否出现过？(d) 讨论 violation 时 ASV ranking 的实际鲁棒性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W-SF1** [R2-N2 提出 must-fix, R1 AGREE 但降为 should-fix; Director 采纳 should-fix（高优先级）] **对 EMNLP 受众的可及性不足**\n\n计量经济学术语（plim, FWL, Wald estimator, E-value, column-stochastic）解释不充分。plim 在 Abstract/Introduction 隐含使用但正式定义在 p.4 脚注 1；FWL 作为核心概念仅 p.3 一句话解释；E-value 未解释基本思想就与 ASV 对比。Abstract 在约 250 词内覆盖 7 拓扑 × sign reversal × ASV × monotonicity × correction × FWL + 大量具体数字，认知负荷极高。\n\nDirector 裁决：降为 should-fix，理由：(a) ACL venue 接受跨学科论文（如 Feder et al. 2022），(b) 8 页限制下增加 Preliminaries 可能压缩核心内容。建议优先：Abstract 精简（保留 1-2 核心发现）+ E-value/FWL 直觉解释（各 1-2 句），空间效率最高。\n\n**W-SF2** [R1-N2 提出 must-fix, R2 REBUT 降为 should-fix; Director 采纳 should-fix] **缺乏真实观测数据的端到端因果分析验证**\n\n所有实验均为合成线性 SEM + 注入真实 LLM 混淆矩阵。Section 4.4 \"Empirical Validation\" 验证的是 theory-MC 一致性，未在任何真实观测数据上运行完整因果分析流程（LLM 标注 → ASV 诊断 → 校正 → 因果估计评估）。Appendix B.18 政治广告案例仅停留在 ASV 诊断层面。\n\nDirector 裁决：降为 should-fix，理由：(a) 核心贡献是理论性的，三层验证已是高标准；(b) 端到端验证需同时有 gold labels 和 known causal effects，结构性困难；(c) ARR H13 不要求额外实验。建议将 B.18 扩展为完整校正流程演示。\n\n**W-SF3** [R1-W1 + R2-W1, 共识 should-fix] **Non-differential misclassification 假设的适用性讨论和验证不够充分**\n\nTable 15 (Appendix B.16) 显示安全阈值极紧——多数数据集要求 ε < 0.02。Stress test (Table 7, Appendix B.6) 仅 exposure 拓扑有完整表格，extended 4-topology test 仅文字摘要无表格。LLM 可能通过上下文间接获取 Y 信号，few-shot 示例可能引入 differential bias。\n\n建议：(a) 将 extended stress test 4 拓扑结果以表格呈现；(b) 讨论 LLM CoT/few-shot 可能引入的 differential patterns；(c) 给出定量指导——超过什么阈值时结论不可靠。\n\n**W-SF4** [R2-W2, R1 AGREE] **与核心 prior work 的增量区分不够清晰**\n\nRemark 1 (p.6) 的 ASV vs E-value 三点对比各仅一句话，不够充分。Correction guidance 的贡献性质（benchmark 式比较 vs 方法创新）定位不清。建议增加结构化对比表。\n\n**W-SF5** [R1-W5, R2 AGREE] **Theorem 1 的 proportional effects 假设限制性强且实践中难以验证**\n\nf ⊥ g 时 OOB 率达 25%（Appendix B.13），NLP-realistic 下 0.07%。但实践者无法先验验证 proportional effects 是否成立。R2 补充：sufficient condition not necessary，Appendix B.13 数值分析全面。共识 should-fix（偏 minor）。\n\n**W-SF6** [R1-W4, R2 AGREE] **Abstract FWL invariance 声明缺少 \"under linear OLS\" 限定**\n\nAbstract \"provably ineffective\" 未标注 FWL 严格仅在 linear OLS 下成立。Logistic 下 breaks（|ΔSF| < 0.02, Table 5）。修复成本极低。\n\n**W-SF7** [R2-W5, R1 AGREE] **Algorithm 1 经验阈值缺乏理论依据**\n\n90.6% RMSE reduction、τ_conf > 0.7 等阈值从 Table 4/7 经验提取，未讨论对不同 DGP 参数的敏感性。\n\n**W-SF8** [R1-W2, R2 AGREE] **Table 1 Violation vs Sign Flip 列定义模糊**\n\nCaption 未显式定义两列含义，Violation 和 Sign Flip 的包含关系不直观。\n\n### Minor\n\n**W-MI1** [R1-M3 + R2-W4, 共识] Figure 2 子图过小（7 个子图 single-column），灰度打印颜色区分困难。Figure 3 y 轴标签不够直观。\n\n**W-MI2** [R1-W3, R2 部分 REBUT] ASV 参数化 C(δ) 假设均匀退化。R2 澄清 C₀ 本身捕获非均匀性、δ 是标准做法；但同意应补充 real LLM C₀ 下的 ranking 稳定性检验。\n\n**W-MI3** [R1-M1] 符号密度高（约 20 个符号），可考虑正文增加 notation summary。\n\n**W-MI4** [R1-M2] Algorithm 1 是最具实践价值的输出之一，但被放在 Appendix 最后一页。建议正文 Section 4.5 中放置简化版。\n\n**W-MI5** [R2 minor] Abstract \"seven canonical\" 的 canonical 选取标准未解释。\n\n**W-MI6** [R2 minor] Figure 1 caption \"starred-node\" 含义应在 caption 内解释。\n\n**W-MI7** [R2 minor] 匿名审稿阶段建议提供 anonymous repository 链接供 reproducibility 验证。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 通过交叉分享达成的共识：\n\n1. **[AGREE] K≥3 ASV 单调性未证明是论文最大的理论缺口**（R1-N1 = R2-N1）。Observation 1 与 Table 10 的数值不一致进一步削弱可信度。\n2. **[AGREE] Non-differential 假设的实践可信度需更充分讨论和验证**（R1-W1 ≈ R2-W1）。Stress test 完整表格仅覆盖 exposure 拓扑。\n3. **[AGREE] Abstract 信息密度过高，计量术语解释不充分**（方向一致，severity 分歧见下）。\n4. **[AGREE] Figure 可读性有改进空间**（R1-M3 = R2-W4）。\n5. **[AGREE] Abstract FWL invariance 应加 \"under linear OLS\"**（R1-W4, R2 AGREE）。\n6. **[AGREE] Algorithm 1 阈值是经验性的**（R2-W5, R1 AGREE）。\n7. **[AGREE] Table 1 列定义需明确**（R1-W2, R2 AGREE）。\n8. **[AGREE] ASV vs E-value 对比不够充分**（R2-W2, R1 AGREE）。\n9. **[AGREE] 三级证据层次是方法论美德**（S2）。\n10. **[AGREE] FWL invariance 负结果有独立实践价值**（S4）。\n\n---\n\n## Reviewer Divergence\n\n1. **EMNLP 受众可及性的严重程度**：R2 列为 must-fix（EMNLP 主流读者无法 follow 方法论会限制 impact），R1 降为 should-fix（ACL 接受跨学科论文，8 页限制下增加 Preliminaries 会压缩核心内容）。**Director 裁决：should-fix（高优先级）**。R1 的页面约束论点成立，但 R2 对受众匹配的担忧合理。建议低空间成本的改进：Abstract 精简 + 关键术语直觉解释。\n\n2. **真实数据端到端验证的严重程度**：R1 列为 must-fix（Abstract \"topology-aware analysis is necessary\" 缺乏真实数据支撑），R2 降为 should-fix（核心贡献是理论性的，端到端验证存在结构性困难）。**Director 裁决：should-fix**。R2 的三个论点（理论贡献的验证标准、ARR H13、ground truth 获取困难）更有说服力。\n\n3. **任务覆盖范围**：R2 建议增加 NER/RE/event detection 任务。R1 REBUT——这些是 span-level 任务，超出 K×K 混淆矩阵框架的适用范围，但同意分类任务内数据集多样性不足。**Director 裁决：采纳 R1 的 REBUT**。NER/RE 确实超出框架范围。但在分类任务内增加数据集多样性（如 topic classification, NLI）是合理的低优先级建议。\n\n---\n\n## Questions\n\n以下为需要作者回应的关键问题（按优先级排序）：\n\n1. **[R1+R2] Observation 1 数值澄清**：Observation 1 \"< 0.005\"、Conjecture 1 \"ε < 0.06\"、Table 10 \"0.011/0.031\" 三者之间的关系？使用的偏差度量是否相同？\n\n2. **[R1+R2] Conjecture 1 violation 分布**：ε < 0.06 的 violations 在 confusion matrix 参数空间中的分布如何？集中在对角占优度极低的区域？这类矩阵在 23 个 LLM 配置中出现过吗？\n\n3. **[R1+R2] Differential misclassification 下 ASV ranking 稳定性**：在 outcome-dependent 分类偏差（ε = 0.03-0.05）下，ASV vulnerability ranking 是否仍稳定？\n\n4. **[R1] 当前主流 LLM 准确率**：GPT-4o/Claude 在同类任务上准确率是否已显著高于 0.45-0.81？如是，框架警示在多大程度上仍适用？\n\n5. **[R2] Logistic FWL 等价性**：Table 5 的 \"practically negligible\"（< 0.005）判断是否依赖 DGP 参数？是否存在使 deviation 变得 substantial 的参数配置？\n\n---\n\n## Missing References\n\n**R2 提出**：Imai, Keele, and Tingley (2010) \"A General Approach to Causal Mediation Analysis\"。R1 确认遗漏程度有限（VanderWeele 2015 等已覆盖因果中介）。**查证**：references.bib 已包含 imai_keele_tingley2010 和 imai_keele_yamamoto2010，Related Work p.3 已引用。实际未遗漏。\n\n**R1**：未发现重大引用遗漏。可考虑补充近期 LLM calibration 文献。\n\n**Director 结论**：无关键引用遗漏。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中未开启 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因配额限制未能完成实际页面检查（error: \"You've hit your limit · resets 4pm (UTC)\"）。格式合规性由两位 Reviewer 人工确认：\n- ✅ 正文 8 页（Sections 1-5 + Limitations），符合 EMNLP 2026 Long Paper 限制\n- ✅ Limitations section 存在（p.8-9），覆盖 3 个主要局限\n- ✅ Double-blind 合规——\"Anonymous ACL submission\"，无身份信息泄露\n- ✅ 引用格式正确，ACL 模板\n- ✅ 附录 23 页，包含完整证明和补充实验\n- ⚠️ Figure 2 子图过小（7 个子图 single-column），灰度打印颜色区分困难\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**置信度: 4/5**（两位 Reviewer 均给出 4/5 置信度，交叉分享后在核心问题上达成共识）\n\n**评分理由**：\n\n论文解决了一个重要且未被系统研究的问题——K-class LLM annotation error 在因果推断中的 topology-dependent 传播。工作量巨大（7 拓扑 × K-class × 3 ASV × 5 校正方法 × 23 页附录），三级证据层次和 FWL invariance 负结果均有独立方法论价值。\n\n然而，论文最核心的实用贡献——K≥3 下 ASV 的拓扑脆弱性排序——依赖未证明的 Conjecture 1，且正文（Observation 1）与附录（Table 10）存在数值不一致，削弱可信度。对 EMNLP 受众的可及性不足（计量术语解释不充分、Abstract 过于密集）可能限制实际 impact。\n\n**从 3.5 提升至 4.0 (Conference) 的关键路径**：\n1. 修正 Observation 1 与 Table 10 的数值矛盾（factual correction，最低成本）\n2. 为 Conjecture 1 补充 failure mode 分析（violation 集中区域、ranking 鲁棒性）或 partial proof\n3. Abstract 精简 + 关键术语（plim/FWL/E-value）增加直觉解释\n4. Abstract 加 \"under linear regression\" 限定 FWL 声明\n\n以上 4 项中，第 1 和第 4 项可在 rebuttal/camera-ready 中即时完成，第 3 项可在 camera-ready 中完成，第 2 项需要一定的技术工作但不需要新实验。\n\n---\n\n## Detailed Comments\n\n### Abstract (p.1)\n- 约 250 词，覆盖概念过多。建议精简至 3 个核心发现：(1) K≥3 sign reversal, (2) topology-dependent vulnerability ranking, (3) FWL invariance negative result。具体数字（83.4%, 2.1%, 52.6%, 210,000, 1.6% MAPE 等）保留 2-3 个最有冲击力的即可。\n- \"matrix-based corrections are provably ineffective\" 需加 \"under linear regression\"。\n\n### Section 1 Introduction (pp.1-2)\n- 叙事结构清晰（problem → gap → contribution → evidence）。\n- Contribution 3（correction guidance）的性质定位不清——是方法创新还是 benchmark 式比较？建议明确区分。\n\n### Section 2 Related Work (pp.2-3)\n- 引用覆盖充分，涵盖测量误差、因果推断、NLP 标注质量三条文献线。\n- 与 Teblunthuis (2024) 和 Lee et al. (2024) 的技术增量可更具体（如对比表）。\n\n### Section 3 Method (pp.3-6)\n- Bias expressions (Eqs. 1-3) 推导清晰，一般 K 下成立。\n- Proposition 1 (sign preservation)：confounding 和 collider 的解析证明完整正确。条件 \"|τ| > √...\" 缺少直觉解释。\n- Theorem 1 (K=2 monotonicity)：证明利用 perspective function 凸性，技术上正确。Proportional effects 假设的讨论可更充分（可验证性和退化行为）。\n- Observation 1 (K≥3 monotonicity)：\"< 0.005\" 与 Table 10 不一致，需修正。\n- Conjecture 1 (ε-approximate)：数值验证规模（210,000 矩阵）充分但缺乏对抗性搜索。\"under default DGP parameters\" 限定适当。\n- Remark 1 (ASV vs E-value)：三点对比每个仅一句话，不够充分。\n\n### Section 4 Experiments (pp.6-8)\n- Theory-MC MAPE 1.6% 精度高。\n- Table 1 Violation/Sign Flip 列定义需在 caption 中明确。\n- Figure 5 (F₁ vs bias)：信息传达有效。\n- Section 4.5 correction guidance：FWL invariance 论证清晰。PPI++ M-bias 有害的机制解释（protective attenuation removal）到位。\n- Algorithm 1 在 Appendix 最后一页，建议正文放简化版。\n\n### Section 5 Conclusion + Limitations (p.8-9)\n- Conclusion 简洁恰当。\n- Limitations 覆盖 3 个主要局限（non-differential 假设、线性 SEM、观测范围），长度适当。Gold-label bootstrapping 约束已提及。\n- 可补充：Algorithm 1 阈值的 DGP 依赖性。\n\n### Appendix (pp.9-31)\n- 完整证明（7 拓扑 sign preservation + Theorem 1 monotonicity），15+ 鲁棒性检查。\n- Table 10 与 Observation 1 数值需对齐。\n- B.18 政治广告案例可扩展为完整校正流程。",
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-23T11:53:05.757005+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4316
}
```

</details>

---


### Assistant

_source line 1252 · 2026-05-23T11:53:16.684525+00:00_

审稿报告已投递至 Research Director。

**Round 15 审稿完成**，总结如下：

**Overall: 3.5 (Borderline Conference)**

核心发现：
- **唯一 must-fix**：K≥3 ASV 单调性仅为 Conjecture + Observation 1 与 Table 10 数值不一致
- **8 个 should-fix**：EMNLP 可及性（高优先级）、端到端验证、non-differential 假设、prior work 增量、proportional effects 可验证性、Abstract FWL 限定、Algorithm 1 阈值、Table 1 定义
- **7 个 minor**

**提升至 4.0 (Conference) 的关键路径**：修正 Observation 1 数值矛盾 → Conjecture 1 failure mode 分析 → Abstract 精简 + 术语解释 → FWL 加 "under linear regression"。前两项需技术工作，后两项可在 camera-ready 完成。

Issue Tracker 已同步更新（新增 R15-N1, R15-W1, R15-W2, R15-W3 四个新 issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 124

## Round 124

2 recorded events


### User

_source line 1253 · 2026-05-23T11:53:19.292762+00:00_

[Reviewer 2 审稿结果]:
逐条回应已提交给 Director。核心结论：

- **R1-N1 (Conjecture 1)**: [AGREE]，并补充了 Observation 1 ("< 0.005") 与 Table 10 (0.011/0.031) 的数值不一致作为额外证据
- **R1-N2 (端到端验证)**: [REBUT] severity——同意方向但建议降为 should-fix，理由是论文核心贡献是理论性的，三层验证结构已足够
- **R1-W1 ~ W5**: W1/W2/W4/W5 均 [AGREE]；W3 部分 [REBUT]——C₀ 已捕获非均匀误差模式，但建议用 real LLM 矩阵做 robustness check
- 两位 Reviewer 在核心关切上高度收敛（Conjecture 1 gap、non-differential assumption、可及性），分歧仅在 N2 的 severity level

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

_source line 1254 · 2026-05-23T11:53:32.848563+00:00_

审稿报告已投递给 Research Director。

**Round 15 审稿总结**：

- **Overall Score**: 3.5 (Borderline Conference)
- **Reviewer 编排**: 2 人，1 轮交叉分享即收敛
- **唯一 Must-Fix**: K≥3 ASV 单调性仅为 Conjecture + Observation 1 与 Table 10 数值不一致
- **8 个 Should-Fix**: 可及性（高优先级）、端到端验证、non-differential 假设、prior work 增量、proportional effects、Abstract FWL 限定、Algorithm 1 阈值、Table 1 列定义
- **7 个 Minor**: Figure 可读性、ASV 参数化、符号密度、Algorithm 1 位置等

**从 3.5 → 4.0 的关键路径**：修正 Observation 1 数值矛盾 + Conjecture 1 failure mode 分析 + Abstract 精简/术语解释 + FWL "under linear regression" 限定。前两项需技术工作，后两项可在 camera-ready 完成。

Issue Tracker 已同步更新（4 个新 issue，所有历史 issue 状态已刷新）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 125

## Round 125

42 recorded events


### User

_source line 1255 · 2026-05-23T12:21:01.606395+00:00_

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

_source line 1256 · 2026-05-23T12:21:07.489229+00:00_

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

_source line 1257 · 2026-05-23T12:21:07.540133+00:00_

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
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1258 · 2026-05-23T12:21:13.481469+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
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
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-23T12:21:13.542961+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 61
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-23T12:21:17.002921+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-23T12:21:17.053628+00:00_



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

_source line 1262 · 2026-05-23T12:21:22.073838+00:00_

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

_source line 1263 · 2026-05-23T12:21:23.984474+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1910
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-23T12:21:24.437375+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf 2>&1",
  "description": "Check paper files exist"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-23T12:21:24.939685+00:00_

-rw-r--r-- 1 ubuntu ubuntu 921694 May 23 12:11 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf
-rw-r--r-- 1 ubuntu ubuntu   1916 May 23 12:11 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-23T12:21:25.090739+00:00_

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

_source line 1267 · 2026-05-23T12:21:25.191602+00:00_



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

_source line 1268 · 2026-05-23T12:21:30.763333+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines page limit"
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
    "query": "EMNLP 2026 call for papers ARR submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 1269 · 2026-05-23T12:21:31.717741+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines formatting requirements anonymity"
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
    "query": "ACL Rolling Review 2026 author guidelines formatting requirements anonymity"
  }
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-23T12:21:32.823589+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-23T12:21:32.924668+00:00_

&lt;persisted-output>
Output too large (34.3KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib--claude-sessions-review-director-d2e6d7be/051a1642-45de-4f89-9cec-976a354b9de5/tool-results/bigjmw1w8.txt

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
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1272 · 2026-05-23T12:21:35.901719+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the web search results, here's the information about EMNLP 2026 call for papers regarding ARR submission guidelines and page limits:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

## ARR Submission Guidelines

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare
…[truncated 584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 5138
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-23T12:21:40.669719+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines formatting requirements anonymity"

Links: [{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, here are the key author guidelines for ACL Rolling Review 2026 regarding formatting requirements and anonymity:

## Anonymity Requirements

Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided. Supplementary materials should also be anonymized.

A paper can only be submitted to ARR if it has been anonymous for at least a month before the first submission, and it must remain anonymous while it is under review. However, beginning with the February 15, 2024 AR
…[truncated 1107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 8951
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-23T12:21:47.749634+00:00_

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

_source line 1275 · 2026-05-23T12:21:48.753757+00:00_

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
19	\newtheorem{remark}{Remark}
20	
21	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
24	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
25	\graphicspath{{../../figures/paper/}}
26	
27	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{abstract}
35	
36	\input{introduction}
37	
38	\begin{figure*}[t]
39	\centering
40	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
41	\vspace{-6pt}
42	\caption{Seven canonical DAG topologies with starred-node annotation~\cite{hernan_cole2009}. $A$ (latent) $\to$ $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies: treatment (exposure), covariate (confounding, mediation, M-bias, front-door), selection (collider), instrument (IV).}
43	\label{fig:dag_taxonomy}
44	\end{figure*}
45	
46	\input{related_work}
47	
48	\input{method}
49	
50	% ── Figures ──
51	
52	\begin{figure*}[t]
53	\centering
54	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
55	\vspace{-6pt}
56	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
57	\label{fig:bias_distribution}
58	\end{figure*}
59	
60	\input{experiments}
61	
62	\input{concl
…[truncated 109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-23T12:21:49.056947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf",
  "pages": "1-10"
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
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool call

_source line 1277 · 2026-05-23T12:21:49.408821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib--claude-sessions-review-director-d2e6d7be/051a1642-45de-4f89-9cec-976a354b9de5/tool-results/bigjmw1w8.txt"
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
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib--claude-sessions-review-director-d2e6d7be/051a1642-45de-4f89-9cec-976a354b9de5/tool-results/bigjmw1w8.txt"
  }
}
```

</details>

---


### Tool result

_source line 1278 · 2026-05-23T12:21:49.711231+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf (900.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-23T12:21:49.737895+00:00_

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
…[truncated 32322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 329
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-23T12:21:58.623597+00:00_

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

_source line 1281 · 2026-05-23T12:21:59.075666+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy, sign reversal occurs in 2.1\% of exposure configurations, in secondary coefficients with small effect sizes; across all 23 empirical LLM configurations (mean diagonal 0.45--0.81), sign reversal is confined exclusively to exposure, though IV reaches 52.6\% under uniform Dirichlet priors. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$) and numerically verified ($K{\geq}3$) monotonicity, yielding a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
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

_source line 1282 · 2026-05-23T12:21:59.076096+00:00_

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

_source line 1283 · 2026-05-23T12:21:59.778909+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: the binary attenuation guarantee breaks at $K \geq 3$, where exposure and IV can reverse signs while five topologies preserve them. ASVs yield a vulnerability ranking from IV (most fragile) to M-bias (immune); matrix-based corrections are provably ineffective for four covariate topologies due to FWL invariance. Code and data will be released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information; a stress test (Appendix~\ref{sec:nondiff_stress}) shows that structured violation patterns can exceed or fall below uniform predictions. Closed-form expressions are derived under $K{=}3$ linear structural equations; extensions to arbitrary $K$ and nonlinear models~\cite{schennach2020mismeasured} remain open (Appendix~\ref{sec:logistic_dgp}), though correction method rankings are stable across $K{=}3,5,10$ (Spearman $\rho \geq 0.80$, with PPI++ degrading at $K{=}10$; Appendix~\ref{sec:correction_k_sensitivity}). The ASV diagonal parameterization $C(\delta) = (1{-}\delta)I + \delta C_0$ assumes uniform degradation across categories; rare-class-specific degradation would require multi-dimensional extensions. Algorithm~1 thresholds are calibrated under our default DGP; practitioners should re-calibrate under domain-specific structural parameters. When the true DAG is uncertain, practitioners can apply Algorithm~1 under each candidate topology and report the range of conclusions as a form of specification sensitivity analysis. FWL invariance holds under linear OLS and approximately under logistic regression; applicability to non-parametric methods (doubly robust estimators, TMLE) remains unverified. Our framework assumes $C$ is known or estimable from held-out
…[truncated 314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-23T12:21:59.829714+00:00_

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

_source line 1285 · 2026-05-23T12:21:59.880683+00:00_

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
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-23T12:22:34.843905+00:00_

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

_source line 1287 · 2026-05-23T12:22:35.245851+00:00_

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


### Tool call

_source line 1288 · 2026-05-23T12:22:35.447230+00:00_

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

_source line 1289 · 2026-05-23T12:22:38.816343+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3972
}
```

</details>

---


### Tool result

_source line 1290 · 2026-05-23T12:22:38.816784+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3570
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-23T12:22:38.967637+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 3520
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-23T12:23:26.952457+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 目标论文\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 路径：`projects/causal_annot_error_attrib/docs/paper/main.tex`（各章节通过 \\input 引入：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf`\n- 目标 venue：**EMNLP 2026**（ARR Long Paper）\n\n## Venue 要求\n- ARR 统一审稿，通过 OpenReview 提交\n- Long paper 正文 **8 页限制**（不含 References 和 Limitations）\n- ACL 模板，必须使用 `[review]` 选项\n- **Double-blind**：论文不得包含作者信息\n- 必须包含 Limitations 章节\n- 截止日期：2026-05-25\n\n## 你的审查侧重\n\n### 1. 理论严谨性\n- Proposition 1（sign preservation for confounding/collider）的证明是否完整、逻辑是否严密？\n- Theorem 1（envelope monotonicity, K=2）的证明是否正确？条件是否充分？\n- Observation 1（K≥3 envelope monotonicity 数值验证）：声称 worst-case deviations ≤ 0.013——核查此数值是否有充分支撑，与 Appendix Table 10 是否一致\n- Conjecture 1（ε-approximate monotonicity）：210,000 矩阵验证是否足够？corner case 分析是否充分？\n- proportional effects 假设 (f = λg) 在 NLP/CSS 场景下是否合理？实践者能否先验验证？\n\n### 2. 假设合理性\n- Non-differential misclassification 假设：在 LLM 场景下何时成立、何时不成立？论文对此讨论是否充分？\n- 线性 SEM 假设：对 EMNLP 受众是否足够通用？FWL invariance 声明是否正确限定了适用范围（linear OLS）？\n- ASV 参数化 C(δ) = (1−δ)I + δC₀ 假设均匀退化——与 LLM 实际误差模式（稀有类别先崩溃）是否一致？\n\n### 3. 实验验证\n- Monte Carlo 验证（161 场景，MAPE 1.6%）是否充分？\n- 23 个 LLM 配置的经验验证是否代表性足够？（模型范围 7B-235B，任务类型 sentiment/stance/toxicity）\n- Table 1/Table 4 数值是否内部一致？\n- Abstract 中的数值声明是否与正文/附录一致？\n- 是否缺乏真实因果数据的端到端验证？\n\n### 4. 数学表述\n- 符号系统是否一致（τ vs β_T，plim 记号）？\n- 公式推导是否可复现？\n- Definition 1 (non-differential misclassification) 是否精确？\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句论文概述）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出，标注 [must-fix] / [should-fix] / [minor]）\n4. **Questions**（需要作者澄清的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
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
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 目标论文\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 路径：`projects/causal_annot_error_attrib/docs/paper/main.tex`（各章节通过 \\input 引入：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf`\n- 目标 venue：**EMNLP 2026**（ARR Long Paper）\n\n## Venue 要求\n- ARR 统一审稿，通过 OpenReview 提交\n- Long paper 正文 **8 页限制**（不含 References 和 Limitations）\n- ACL 模板，必须使用 `[review]` 选项\n- **Double-blind**：论文不得包含作者信息\n- 必须包含 Limitations 章节\n- 截止日期：2026-05-25\n\n## 你的审查侧重\n\n### 1. 理论严谨性\n- Proposition 1（sign preservation for confounding/collider）的证明是否完整、逻辑是否严密？\n- Theorem 1（envelope monotonicity, K=2）的证明是否正确？条件是否充分？\n- Observation 1（K≥3 envelope monotonicity 数值验证）：声称 worst-case deviations ≤ 0.013——核查此数值是否有充分支撑，与 Appendix Table 10 是否一致\n- Conjecture 1（ε-approximate monotonicity）：210,000 矩阵验证是否足够？corner case 分析是否充分？\n- proportional effects 假设 (f = λg) 在 NLP/CSS 场景下是否合理？实践者能否先验验证？\n\n### 2. 假设合理性\n- Non-differential misclassification 假设：在 LLM 场景下何时成立、何时不成立？论文对此讨论是否充分？\n- 线性 SEM 假设：对 EMNLP 受众是否足够通用？FWL invariance 声明是否正确限定了适用范围（linear OLS）？\n- ASV 参数化 C(δ) = (1−δ)I + δC₀ 假设均匀退化——与 LLM 实际误差模式（稀有类别先崩溃）是否一致？\n\n### 3. 实验验证\n- Monte Carlo 验证（161 场景，MAPE 1.6%）是否充分？\n- 23 个 LLM 配置的经验验证是否代表性足够？（模型范围 7B-235B，任务类型 sentiment/stance/toxicity）\n- Table 1/Table 4 数值是否内部一致？\n- Abstract 中的数值声明是否与正文/附录一致？\n- 是否缺乏真实因果数据的端到端验证？\n\n### 4. 数学表述\n- 符号系统是否一致（τ vs β_T，plim 记号）？\n- 公式推导是否可复现？\n- Definition 1 (non-differential misclassification) 是否精确？\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句论文概述）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出，标注 [must-fix] / [should-fix] / [minor]）\n4. **Questions**（需要作者澄清的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-23T12:23:51.059194+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24106
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-23T12:23:51.762224+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 目标论文\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 路径：`projects/causal_annot_error_attrib/docs/paper/main.tex`（各章节通过 \\input 引入：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf`\n- 目标 venue：**EMNLP 2026**（ARR Long Paper）\n\n## Venue 要求\n- ARR 统一审稿，通过 OpenReview 提交\n- Long paper 正文 **8 页限制**（不含 References 和 Limitations）\n- ACL 模板，必须使用 `[review]` 选项\n- **Double-blind**：论文不得包含作者信息\n- 必须包含 Limitations 章节\n- 截止日期：2026-05-25\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 三个贡献（bias taxonomy, ASV, correction guidance）的新颖性如何？是否为增量贡献？\n- 与 Brenner (1993)、TeBlunthuis et al. (2024)、Lee & Wood-Doughty (2024) 的差异化是否清晰？\n- ASV 与 E-value (VanderWeele & Ding, 2017) 的方法论创新边界是否清晰？是否仅为 E-value 的直接移植？\n- \"first unified analysis across seven topologies\" 的 novelty claim 是否准确、有事实支撑？\n- Correction guidance 定位是否清晰（benchmark 式比较 vs 方法创新）？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - Measurement error in causal inference 领域\n  - LLM annotation quality 领域\n  - Sensitivity analysis 领域\n  - Text-as-data / computational social science 领域\n- 引用是否真实存在（非幻觉）？格式是否符合 ACL natbib 规范？\n\n### 3. 呈现质量与可及性\n- Abstract 是否过长？（EMNLP 2026 限制 200 词）检查实际词数\n- Abstract 信息密度是否过高？（7 拓扑 + sign reversal + ASV + monotonicity + correction + FWL）\n- 对 EMNLP 受众（NLP 研究者，非计量经济学家）的可及性如何？plim/FWL/Wald/E-value 等术语是否有足够解释？\n- 论文叙事结构是否清晰？Section 之间的逻辑衔接是否流畅？\n- Figure 2 子图是否过小（7 个子图挤在一个 figure 中）？灰度打印是否可区分？\n- Table 1 各列（Violation, Sign Flip, Amplif., τ_sf=0?）定义是否清晰？\n\n### 4. 格式合规\n- 正文是否控制在 8 页内？Conclusion/Limitations 是否在正确位置？\n- 是否使用 ACL 模板的 `[review]` 选项？\n- 是否满足 double-blind 要求（无作者信息泄露）？\n- Limitations 章节是否存在、是否仅讨论局限性（不包含新实验/分析）？\n- 引用格式是否正确（括号引用 vs 文内引用）？\n\n### 5. 实验完整性（从整体视角）\n- 实验设计是否覆盖了论文的核心 claim？\n- 是否存在 cherry-picking 的嫌疑（如只展示对论文有利的结果）？\n- LLM 配置多样性（模型大小、任务类型）是否充分？\n- 是否缺少必要的消融实验或控制实验？\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句论文概述）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出，标注 [must-fix] / [should-fix] / [minor]）\n4. **Questions**（需要作者澄清的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
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
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 目标论文\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 路径：`projects/causal_annot_error_attrib/docs/paper/main.tex`（各章节通过 \\input 引入：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_16/submitted.pdf`\n- 目标 venue：**EMNLP 2026**（ARR Long Paper）\n\n## Venue 要求\n- ARR 统一审稿，通过 OpenReview 提交\n- Long paper 正文 **8 页限制**（不含 References 和 Limitations）\n- ACL 模板，必须使用 `[review]` 选项\n- **Double-blind**：论文不得包含作者信息\n- 必须包含 Limitations 章节\n- 截止日期：2026-05-25\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 三个贡献（bias taxonomy, ASV, correction guidance）的新颖性如何？是否为增量贡献？\n- 与 Brenner (1993)、TeBlunthuis et al. (2024)、Lee & Wood-Doughty (2024) 的差异化是否清晰？\n- ASV 与 E-value (VanderWeele & Ding, 2017) 的方法论创新边界是否清晰？是否仅为 E-value 的直接移植？\n- \"first unified analysis across seven topologies\" 的 novelty claim 是否准确、有事实支撑？\n- Correction guidance 定位是否清晰（benchmark 式比较 vs 方法创新）？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - Measurement error in causal inference 领域\n  - LLM annotation quality 领域\n  - Sensitivity analysis 领域\n  - Text-as-data / computational social science 领域\n- 引用是否真实存在（非幻觉）？格式是否符合 ACL natbib 规范？\n\n### 3. 呈现质量与可及性\n- Abstract 是否过长？（EMNLP 2026 限制 200 词）检查实际词数\n- Abstract 信息密度是否过高？（7 拓扑 + sign reversal + ASV + monotonicity + correction + FWL）\n- 对 EMNLP 受众（NLP 研究者，非计量经济学家）的可及性如何？plim/FWL/Wald/E-value 等术语是否有足够解释？\n- 论文叙事结构是否清晰？Section 之间的逻辑衔接是否流畅？\n- Figure 2 子图是否过小（7 个子图挤在一个 figure 中）？灰度打印是否可区分？\n- Table 1 各列（Violation, Sign Flip, Amplif., τ_sf=0?）定义是否清晰？\n\n### 4. 格式合规\n- 正文是否控制在 8 页内？Conclusion/Limitations 是否在正确位置？\n- 是否使用 ACL 模板的 `[review]` 选项？\n- 是否满足 double-blind 要求（无作者信息泄露）？\n- Limitations 章节是否存在、是否仅讨论局限性（不包含新实验/分析）？\n- 引用格式是否正确（括号引用 vs 文内引用）？\n\n### 5. 实验完整性（从整体视角）\n- 实验设计是否覆盖了论文的核心 claim？\n- 是否存在 cherry-picking 的嫌疑（如只展示对论文有利的结果）？\n- LLM 配置多样性（模型大小、任务类型）是否充分？\n- 是否缺少必要的消融实验或控制实验？\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句论文概述）\n2. **Strengths**（逐条列出优点）\n3. **Weaknesses**（逐条列出，标注 [must-fix] / [should-fix] / [minor]）\n4. **Questions**（需要作者澄清的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-23T12:23:53.224180+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1461
}
```

</details>

---


### Assistant

_source line 1296 · 2026-05-23T12:24:05.582294+00:00_

**Round 1 审稿已启动。**

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性（理论证明、假设、实验验证） | 已派发 |
| Reviewer 2 | 新颖性/完整性（贡献定位、相关工作、呈现、格式） | 已派发 |
| 视觉审查 Agent | PDF 排版质量（非评分项） | 已派发 |
| 外部审稿 | Stanford Agentic Reviewer | 未配置，跳过 |

等待两名 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 126

## Round 126

2 recorded events


### User

_source line 1297 · 2026-05-23T12:33:32.964366+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性与完整性

**论文标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction

---

## 1. Summary

本文系统分析了多类别（K≥3）LLM 标注误差在七种因果 DAG 拓扑下的传播机制，推导了每种拓扑的偏差表达式，证明了符号保持/反转条件，提出了 Annotation Sensitivity Values (ASVs) 诊断框架，并基于 FWL 不变性证明了矩阵校正方法在四种协变量拓扑下的无效性。实验涵盖 Monte Carlo 模拟、23 组真实 LLM 混淆矩阵验证以及五种校正方法的系统比较。

---

## 2. Strengths

**S1. 填补了重要的文献空白。** Brenner (1993) 仅处理二值混杂, TeBlunthuis et al. (2024) 分析二值 K=2 的四种拓扑, Lee & Wood-Doughty (2024) 仅覆盖 confounding。本文首次在 K≥3 条件下统一分析七种标准 DAG 拓扑，这个"系统性"本身是一个真正的贡献。

**S2. FWL 不变性结果具有高实用价值。** Section 4.5 和 Appendix B.2 证明 PPI++/MLA 等矩阵校正方法在四种协变量拓扑（confounding, mediation, collider, M-bias）下无法减少偏差（因为 FWL 投影消除了校正列），这个结果非平凡且对实践者有直接指导意义。这是本文最有影响力的发现。

**S3. 理论-实验相互印证设计良好。** 对每个理论 claim（sign preservation, monotonicity, FWL invariance），论文都提供了解析证明（K=2）+ 数值验证（K≥3, 100K 随机矩阵）+ 真实 LLM 混淆矩阵验证的三层证据结构。Table 2 的 Violation/Sign Flip 列和 Figure 2 的分布图有效支撑了理论结果。

**S4. Algorithm 1 提供了可操作的实践指南。** 将理论发现转化为实用的拓扑感知校正选择算法（page 31），包含了风险评估、方法选择和 FWL 检查三个步骤，降低了理论到实践的转化门槛。

**S5. Appendix 丰富且严谨。** 22 页 appendix 包含完整证明、消融分析（B.6 非微分假设压力测试, B.7 非线性 DGP, B.12 envelope monotonicity 扩展验证）、以及 ClinicalBERT 案例研究（B.3），展示了作者对潜在反对意见的充分预期。

---

## 3. Weaknesses

### Must-Fix 问题

**N1 [critical] ASV 与 E-value 的方法论创新边界不够清晰**
- 具体位置：Section 3.3 (page 5-6), 以及与 VanderWeele & Ding (2017) 的关系讨论
- 问题：ASV 核心思想是"将 E-value 的未观测混杂强度参数替换为标注误差严重性参数（τ = 偏离完美分类的程度）"。论文声称 ASV "adapt the sensitivity analysis paradigm" (page 5)，但未充分阐明这个 adaptation 在方法论上引入了什么新的技术挑战或解决了什么 E-value 框架无法直接解决的问题。具体而言：(a) E-value 参数化的是未观测混杂的 relative risk，ASV 参数化的是 τ（混淆矩阵偏离单位矩阵的程度），但两者都是 "minimum perturbation to nullify the effect" 的逻辑——这更像是 reparametrization 而非 methodological innovation；(b) 三个子指标（magnitude, significance, sign-flip）虽有实用价值，但本质是 E-value 在不同 threshold 下的实例化。
- 为什么影响接收：如果 ASV 被 reviewer 认定为 E-value 的直接移植，论文的三个贡献中有一个的新颖性将被大幅削弱。
- 建议修改方向：明确指出 E-value 不具备的特性：(1) topology-dependence——同一 confusion matrix 在不同拓扑下 ASV 值不同，E-value 无此概念；(2) sign-flip ASV 是 E-value 没有的对应物（E-value 只关心 nullification，不关心 sign reversal）；(3) 混淆矩阵的参数空间与 E-value 的 relative risk 空间有本质的几何差异（column-stochastic simplex vs. positive reals）。建议在 Section 3.3 增加一个 "Remark" 或 "Comparison with E-values" 段落，用 2-3 句话明确技术区别。

**N2 [critical] "First unified analysis across seven topologies" 的 novelty claim 需要更精确限定**
- 具体位置：Section 1 (page 2, "We present the first unified analysis...")
- 问题：这个 claim 目前的表述是 "first unified analysis of K-class annotator error propagation across seven canonical DAG topologies"。但这个 "first" 需要与 Carroll et al. (2006) Ch. 15（涵盖多种 measurement error 模型下的多拓扑分析）和 Schennach (2020, Handbook of Econometrics, 该条目出现在 .bib 中但未在正文引用）的综述工作明确区分。Carroll 的框架虽然不是针对 LLM annotation，但在结构上也涵盖了多拓扑的 measurement error 分析。
- 为什么影响接收：Reviewer 如果熟悉 measurement error 文献，可能会认为 "first" 这个 claim 不够准确，削弱论文可信度。
- 建议修改方向：将 claim 限定为 "first unified analysis *for LLM-generated multi-class annotations* across seven topologies" 或 "first analysis connecting confusion-matrix structure to topology-dependent bias *in the NLP pipeline context*"，与 measurement error 经典文献做显式区分。

### Should-Fix 问题

**W1 [warning] Abstract 信息密度过高，对 EMNLP 受众不友好**
- 具体位置：Abstract (page 1)
- 问题：188 词的 abstract 试图覆盖：七种拓扑、K≥3 的符号反转、符号保持证明、2.1% exposure 配置、23 组 LLM 配置、52.6% IV 反转率、ASV 的 monotonicity、FWL 不变性。对于 EMNLP 的主要受众（NLP 研究者，非计量经济学家），这是一个过于密集的信息负荷。特别是 "2.1% of exposure configurations" 和 "52.6% under uniform Dirichlet priors" 这两个数字在 abstract 中缺乏足够上下文来让读者理解其含义。
- 建议：精简 abstract 到 3-4 个核心信息点：(1) 问题（LLM 标注误差 + 因果推断），(2) 关键发现（拓扑决定偏差方向），(3) 工具贡献（ASV），(4) 实践启示（FWL 不变性 → 需拓扑感知校正）。移除中间的具体百分比数字。

**W2 [warning] 对 EMNLP 受众的可及性不足——核心术语解释薄弱**
- 具体位置：贯穿全文，特别是 Section 3 Method
- 问题：论文使用了大量计量经济学/统计学术语，部分未给出充分解释：
  - **plim**（probability limit）：首次出现在 Section 3.2 (page 4) equation (1)，仅有脚注 "The probability limit (plim) is the value to which an estimator converges as sample size N → ∞"——但未解释为什么这个概念对理解偏差很重要。
  - **Frisch-Waugh-Lovell (FWL) theorem**：Section 3.1 (page 4) 提到但未给出直观解释。EMNLP 读者可能不知道这个定理的含义和为什么它暗示校正无效。
  - **Wald estimator**：Section 3.2 exposure 拓扑部分提到，仅简短引用 Angrist & Imbens (1995)。
  - **Column-stochastic matrix**：频繁出现但对 NLP 读者而言并非显而易见的术语。
  - **Dirichlet prior/distribution**：Section 4.1 实验设置中使用，未做任何直觉性解释。
- 为什么影响评分：EMNLP reviewer 的统计背景差异大。如果 reviewer 不熟悉这些概念，会显著降低对论文的理解和评价。
- 建议：在 Section 3.1 增加 1-2 句 FWL 的直觉性解释（"FWL theorem states that in multiple regression, the coefficient on one variable can be obtained by first regressing out all other variables—this means replacing a mismeasured variable with its corrected version does not change the coefficient when..."）。类似地，给 column-stochastic 和 Dirichlet 加简短直觉说明。

**W3 [warning] 符号反转（sign reversal）的实际风险可能被高估**
- 具体位置：Abstract, Section 4.2 (page 7)
- 问题：论文在 abstract 和 introduction 中强调符号反转作为核心风险。但 Section 4.2 Table 1 和 Figure 2 的数据显示：在真实 LLM 精度下，符号反转仅发生在 exposure 拓扑的 2.1% 配置中，且仅影响"小效应量的次要系数"（page 1, "in secondary coefficients with small effect sizes"）。对五种拓扑（confounding, mediation, M-bias, front-door, collider），符号反转率为 0%。IV 的 52.6% 是在 uniform Dirichlet prior 下的理论极端情形，而非真实 LLM 条件。
  论文虽然在正文中承认了这些限定条件，但 abstract 和 introduction 的 framing 给人的印象是符号反转是一个普遍且严重的风险。这构成了一种 overclaiming：标题中的 "Topology-Dependent Bias" 暗示这是一个跨拓扑的严重问题，但实际上对大多数拓扑（5/7），偏差方向是保持的。
- 建议：在 abstract 中更明确地限定符号反转的范围（"sign reversal is confined to exposure topology under specific conditions"），避免给读者留下 "LLM 标注导致因果结论全面反转" 的错误印象。

**W4 [warning] Figure 2 子图过小，灰度打印无法区分**
- 具体位置：Figure 2 (page 7)
- 问题：七个子图挤在一个 figure 中（约半页宽度），每个子图的 y 轴标签和分布细节在标准打印尺寸下难以辨认。更关键的是，图例区分 "sign reversal" (红色) 和其他分布 (灰色) 依赖颜色——灰度打印时 reviewer 可能无法区分红灰。
- 建议：(a) 使用 hatching pattern 或不同线型区分符号反转和非反转分布；(b) 考虑将七个子图分成两行或拆分为两个 figure。

**W5 [warning] 实验仅基于模拟，缺少真实因果数据集验证**
- 具体位置：Section 4 全节
- 问题：所有实验都是基于模拟的——Monte Carlo 模拟用理论 DGP 生成数据，empirical validation 用真实 LLM 混淆矩阵但仍然是合成数据。ClinicalBERT 案例研究（Appendix B.3）也是半合成的（真实混淆矩阵 + 模拟 DGP）。论文没有在任何一个已知真实因果效应的数据集上验证其理论预测。这使得 "practical guidance" 的 claim 缺少最有说服力的证据层。
  虽然理解在 causal inference 领域获取 ground truth 的困难，但一些 benchmark 数据集（如 IHDP, LaLonde, ACIC）可以用来验证偏差预测与实际偏差的一致性。
- 建议：即使无法用真实数据，也应该在 Limitations 中更明确地讨论这一缺失，并说明为什么模拟足以支撑论文的 claim。

**W6 [warning] Correction guidance 的定位模糊**
- 具体位置：Section 4.5 (page 8)
- 问题：论文定位 correction guidance 为 "a systematic benchmark, not a new correction method" (page 2)。但 Section 4.5 只用了半页篇幅讨论五种校正方法，且 Table 4（Appendix B.1）的结果摘要非常简短。对于一个声称的 "three contributions" 之一（与 bias taxonomy 和 ASV 并列），这个部分的深度不足。特别是：(a) 五种方法的选择标准未说明（为什么这五种？遗漏了 Bayesian 方法，EM 方法在 Limitations 中被提及但未被测试）；(b) 没有讨论校正方法的计算成本和样本量需求；(c) FWL 不变性结论（四种拓扑校正无效）非常强但实验验证仅在 Appendix B.2 中。
- 建议：将 FWL 不变性结论提升到主文中更突出的位置（目前在 Section 4.5 中只有一句 "matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch-Waugh-Lovell invariance"），增加对 Table 4 结果的分析讨论。

### 小问题

**M1 [minor]** Table 1 列标题定义不够清晰。"Violation"、"Sign Flip"、"Amplif."、"τ_sf=0?" 需要在 table caption 或正文中给出明确定义。目前 caption 仅说 "Bias taxonomy"，未解释各列的含义。

**M2 [minor]** Section 3.2 (page 4) 中 Confounding 拓扑的 bias 表达式 equation (1): plim f(A*) = (Ẽ'Z̃'Z̃)⁻¹Ẽ'Z̃'X̃β。变量 Z̃, Ẽ 的定义分散在前后文中，第一次读到此式时缺乏完整的符号引导。Notation table (Table 19, page 30) 放在了 Appendix C，建议在 Section 3.1 开头引用该表。

**M3 [minor]** bib 文件中 Schennach (2020) 出现在 references.bib (line 586) 但未在正文中引用。如果有意引用应加入正文；如果无意引用应从 bib 中删除以保持整洁。

**M4 [minor]** Conjecture 1 (page 6) 的表述 "envelope monotonicity preserves approximately for non-IV topologies" 中的 "approximately" 需要量化。Appendix B.12 的验证给出了最大逆序步长（worst mag. = 0.008），但主文中应给出这个量级的提示。

**M5 [minor]** Section 4.1 (page 6): "ASV experiments use C(δ) = (1−δ)I + δC_0" 中 C_0 的选取方式（"a reference confusion matrix"）未在主文中说明。需要翻到 Appendix 才能理解实验设置的完整定义。

---

## 4. Questions

**Q1.** ASV 的 topology-dependent 特性是否可以反向使用——即已知某个 ASV 值后，能否推断出最可能的 DAG 拓扑？如果可以，这将大大增加 ASV 的实用价值。

**Q2.** 非微分误分类假设（Definition 1, page 4）在真实 LLM 标注场景中有多强？Section B.6 的 stress test 表明在 ε ≤ 0.05 时结果稳健，但真实 LLM（特别是在不同子群上）的 differential misclassification 程度是否可能远超 ε = 0.05？论文是否有关于这个假设在实际 LLM 部署中的经验估计？

**Q3.** FWL 不变性结论是否推广到广义线性模型（如 logistic regression）？Appendix B.14 简短讨论了 logistic 的情况但结论似乎有所不同——exposure 拓扑下偏差可达 ~78%。如果 FWL 不变性在非线性模型下不成立，这是否意味着矩阵校正方法在 logistic regression 下反而可用？这个讨论在主文中完全缺失。

**Q4.** 论文在 Section 4.4 提到验证用了 HumAID (K=10), VAST (K=3), CivilComments (K=2)。但 K=2 是二值情形，论文的核心 novelty 在于 K≥3。为什么选择 K=2 的 CivilComments 作为验证数据集？是否应该用更多 K≥3 的数据集来支撑核心 claim？

---

## 5. Missing References

**R1.** Miles, Valeri, and Coull (2024). "Measurement Error-Robust Causal Inference via Constructed Instrumental Variables." arXiv:2406.00940. 该工作提出了不需要外部数据即可处理 measurement error 的因果推断方法，与本文的校正方法讨论高度相关，应在 Section 2 sensitivity analysis 段落中引用。

**R2.** Wei, He, Li, and Geng (2025). "Multiply robust causal inference in the presence of an error-prone treatment." Statistical Methods in Medical Research. 该工作处理 treatment 的 misclassification，与本文 exposure 拓扑的分析直接相关。

**R3.** Schennach (2020) 已在 bib 中但未在正文中引用（如 M3 所述）。作为 Handbook of Econometrics 中关于 mismeasured variables 的权威综述，应在 Section 2 measurement error 段落中显式引用。

**R4.** 论文引用了 Manski (1990) 的 bounds approach (Limitations section, page 9)，但未在 Related Work 中讨论。如果 Manski bounds 是一个相关的替代方法学，应在 Section 2 中简要提及。

---

## 6. Overall Assessment

**Overall**: 3.5 (Borderline Conference)

**一句话总结**: 填补了 K≥3 多类别标注误差在多拓扑因果推断下传播机制的文献空白，FWL 不变性结果有实践价值，但 ASV 的方法论新颖性需更清晰阐述，且论文对 EMNLP 受众的可及性需要提升。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 核心理论结果（sign preservation, FWL invariance）有严格证明；K≥3 monotonicity 依赖数值验证但证据充分（100K 矩阵）；非微分假设的 stress test 增强了稳健性。扣 1 分因为部分 claim 依赖 Conjecture 而非证明。 |
| Excitement | 3/5 | 填补了重要空白但属于方法论改进型工作（非开创性新范式）；ASV 是 E-value 的 adaptation 而非全新框架；对 NLP 实践者的直接影响有限（多数 NLP 因果推断仍在 confounding 拓扑下，而此拓扑下符号保持）。 |
| Reproducibility | 4/5 | 承诺代码/数据公开；实验设置细节充分（DGP 参数、Monte Carlo 规模、LLM 配置列表）；扣 1 分因为 ClinicalBERT 案例研究的数据来源和处理细节不够完整。 |
| Clarity | 3/5 | 对 measurement error 领域专家清晰但对 EMNLP 一般受众偏难；术语密度高；Figure 2 过于拥挤；correction guidance 部分过于简略。 |

**Reviewer Confidence**: 4/5 — 熟悉因果推断、measurement error 文献和 NLP 标注质量研究，但对部分高维代数证明未逐行验证。

**Limitations Assessment**: Limitations 章节存在且合理，但遗漏了"仅模拟验证、无真实因果数据集"这一重要局限。

---

## 主要优势（总结）

1. 首次 K≥3 × 7 拓扑的系统分析，填补文献空白
2. FWL 不变性证明具有直接实践指导意义
3. 理论-数值-经验三层证据结构严谨
4. Algorithm 1 降低了理论到实践的转化门槛
5. 丰富的 appendix 预见并回应了潜在质疑

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

_source line 1298 · 2026-05-23T12:33:40.197501+00:00_

Reviewer 2 审稿意见已收到（评分 3.5 Borderline Conference）。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 127

## Round 127

2 recorded events


### User

_source line 1299 · 2026-05-23T12:33:53.289364+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿要点总结**：

- **Overall: 3.5 (Borderline Conference)**
- **2 个 Must-Fix**: (1) ASV 与 E-value 的方法论创新边界不清晰——需明确 topology-dependence 和 sign-flip 等 E-value 不具备的特性；(2) "first unified analysis" claim 需更精确限定，与 Carroll (2006) 等经典 measurement error 文献做显式区分
- **6 个 Should-Fix**: abstract 信息过载、EMNLP 受众可及性不足（FWL/plim/Wald 等术语解释薄弱）、sign reversal 风险可能被高估（仅 2.1% exposure 配置）、Figure 2 子图过小且灰度不可区分、缺少真实因果数据集验证、correction guidance 深度不足
- **5 个 Minor**: Table 1 列定义不清、符号引导分散、Schennach 2020 在 bib 未引用、Conjecture 1 的 "approximately" 未量化、C_0 选取方式仅在 appendix 说明
- **4 个 Missing References**: Miles et al. (2024)、Wei et al. (2025)、Schennach (2020) 正文引用、Manski (1990) Related Work 讨论

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

_source line 1300 · 2026-05-23T12:33:59.329507+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 128

## Round 128

6 recorded events


### User

_source line 1301 · 2026-05-23T12:34:00.835582+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性审查

---

## Summary

本文研究 K-class LLM 标注误差如何沿七种因果 DAG 拓扑传播到因果估计中。论文推导了每种拓扑下的闭式 bias 表达式、sign preservation 条件和 envelope monotonicity 结果，提出 Annotation Sensitivity Values (ASV) 诊断框架和 Algorithm 1 校正决策树。理论上区分了"安全"拓扑（confounding/collider: sign preserved）和"脆弱"拓扑（exposure/IV: sign reversal possible），并用 Monte Carlo 验证、23 个 LLM 经验配置和 ClinicalBERT 案例研究支撑。

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 理论新颖且框架设计优雅，但核心单调性结果对 K≥3 仅为 conjecture、缺乏真实因果数据端到端验证、关键假设对 NLP 场景的适用性讨论不足。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2 证明正确完整，但 K≥3 核心结论为 conjecture；线性 SEM 和 non-differential 假设较强 |
| Excitement | 3.5/5 | 问题重要且及时（LLM 标注×因果推断），但受众可能较窄（需同时懂因果推断和 NLP annotation） |
| Reproducibility | 4/5 | 公式推导清晰、MC 验证参数完整可复现；承诺开源代码和数据 |
| Confidence | 4/5 | 对测量误差×因果推断文献较熟悉，仔细核查了主要证明和数值一致性 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Theorem 1 (envelope monotonicity) 仅对 K=2 成立，K≥3 为 Conjecture——与论文标题和核心 narrative 不匹配

- 具体位置：Section 3.3 Theorem 1, Conjecture 1 (p.6), Appendix A.4 (p.14-15), Table 10 (p.27)
- 问题：论文标题强调 "Multi-Class"（K≥3），但核心单调性结果 Theorem 1 仅对二分类（K=2）有解析证明。K≥3 的 envelope monotonicity 仅有 Conjecture 1（ε-approximate, ε < 0.06）和 210,000 矩阵数值验证。具体问题：
  (1) **采样覆盖不足**：Dirichlet(1,…,1) 均匀采样在高维空间（K=7 时 confusion matrix 有 42 自由度）中 210,000 个样本覆盖率极低，可能遗漏 adversarial corner cases。
  (2) **违反普遍存在**：Table 10 显示 60-97% 的矩阵存在单调性违反，虽然 magnitude 微小（≤ 0.013），但这说明 exact monotonicity 在 K≥3 下系统性不成立。
  (3) **IV 拓扑最严重**：IV 在 K=7 时 79% 的矩阵违反，worst magnitude 0.009——虽然绝对值小，但 Conjecture 本身排除了 IV（"For non-IV topologies"），而 IV 恰恰是最脆弱的拓扑。
- 为什么影响接收：论文的核心 narrative 是 "K≥3 引入二分类不具备的结构性复杂度"（Abstract, Section 1），但最关键的单调性结论在论文主要聚焦的 K≥3 情形下没有理论保证。这使得 ASV 框架的理论基础——"bias 沿 degradation path 单调增长"——在 K≥3 下仅为经验观察。
- 建议修改方向：(1) 在 abstract 和 introduction 中精确区分 "K=2 proven" 和 "K≥3 conjectured with numerical support"，避免读者误以为 multi-class monotonicity 已被证明；(2) 补充 adversarial 搜索（如梯度优化寻找违反 monotonicity 的 confusion matrix）而非仅靠 Dirichlet 随机采样；(3) 讨论若 Conjecture 不成立时 ASV 的 graceful degradation 保证。

**N2** [critical] 缺乏真实因果数据的端到端验证——实验仅验证了公式正确性和 confusion matrix 属性

- 具体位置：Section 4 Experiments 整体, Appendix B.3 ClinicalBERT 案例
- 问题：实验验证有两层但缺少关键的第三层：
  - **Layer 1**: 解析公式 vs. Monte Carlo（161 scenarios = 23 LLM configs × 7 topologies, MAPE 1.6%）→ 仅验证推导公式的数值正确性
  - **Layer 2**: 23 个 LLM 配置的 confusion matrix 性质（Table 1, Section 4.2）→ 仅验证 confusion matrix 输入端的行为
  - **Layer 3 缺失**: 在已知 ground-truth 因果效应的真实/半合成数据上，完整演示 "估计 confusion matrix → ASV 诊断 → 选择校正方法 → 改善因果估计" 的端到端流程。
  ClinicalBERT case study（Appendix B.3, p.22-23）最接近但其 "ground truth" 仍来自模型估计（OLS on gold labels），不是真正的已知因果效应。
- 为什么影响接收：EMNLP 受众关注框架在实际 NLP pipeline 中的应用价值。Theory-MC 一致性只能证明数学推导正确，不能证明框架在实际复杂场景（如 confusion matrix 估计不准确、non-differential 假设近似成立时）中有效。
- 建议修改方向：(1) 构建一个半合成 CSS 数据集（如基于真实文本的 sentiment → voting behavior，注入已知 causal effect），使用 LLM 标注，对比 "无校正 → ASV 诊断 → 校正后" 的 treatment effect 估计精度；(2) 或在 ClinicalBERT 案例中划出人工标注 gold-label 子集作为真正的 ground truth 对照。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Non-differential misclassification 假设在 LLM 场景下的适用性——主文讨论不足

- 具体位置：Definition 1 (Section 3.1, p.4), Limitations (p.9), Appendix B.5-B.6 (p.23-25)
- 问题：Definition 1 要求 P(A*=j|A=k,Y,Z) = P(A*=j|A=k)——误分类与 outcome 和 covariates 独立。在 LLM 标注中，这是一个强假设：LLM 可能利用与 outcome 相关的上下文线索（如情感词密度、话题分布）来分类，导致 differential misclassification。
  - Appendix B.5（Table 15）验证了 23 个 LLM 的 non-differential 安全阈值
  - Appendix B.6（Table 7-8）stress test 显示 ε=0.10 时 IV 的 sign-flip rate 达 7%
  - 但**主文** Section 3.1 对此仅一句 "This holds when the LLM classifies without observing the outcome"，过于简略
- 建议：在 Section 3.1 增加 1-2 段：(a) 何时 non-differential 在 LLM 标注中成立（如 instruction-following 分类、LLM 无法访问 outcome 变量）；(b) 何时可能失败（如 LLM prompt 包含 outcome-correlated context、few-shot examples 引入 outcome 偏差）；(c) 如何用 held-out gold labels 交叉检验此假设。

**W2** [warning] Proportional effects 假设 (f = λg) 缺乏实践验证指导

- 具体位置：Theorem 1 条件 (p.6), Appendix A.4 proof (p.14), Appendix B.13 (p.28)
- 问题：Theorem 1 的解析证明依赖 proportional effects 假设——treatment effect coefficients 跨类别成比例（f = λg）。这要求不同类别的 treatment effect 方向一致且幅度按比例缩放。
  - Appendix B.13 Table 12 显示：proportional 时 OOB rate 0%，near-proportional 0.5%，但 fully independent (f ⊥ g) 时 sign failure rate 达 23%。
  - 论文没有给出实践者如何 **a priori 验证**此假设的方法——在因果推断中，treatment effect 是待估计的未知量，无法在估计前验证其成比例性。
- 建议：(1) 讨论此假设的 testable implications（如使用 pilot data 估计效应向量并检验比例性）；(2) 明确哪类 NLP/CSS 任务更可能满足此假设（如 ordinal categories 的 treatment effect 天然成比例 vs. nominal categories 更可能独立）。

**W3** [warning] ASV 参数化 C(δ) = (1−δ)I + δC₀ 假设均匀退化与 LLM 实际误差模式不符

- 具体位置：Section 3.3 Parameterization (p.5-6)
- 问题：ASV 的 sensitivity path 假设所有类别以相同速率 δ 退化（线性插值 I → C₀）。但 LLM 标注实践中，稀有类别通常先出错（class-imbalanced degradation），且不同类别对之间的混淆概率退化速率不一致。
  - Appendix B.11 在三种 β 设定下测试了 ASV 稳定性（Table 9），但仅改变了效应向量，未改变退化路径本身。
  - 若退化路径非均匀（如 C(δ) 中稀有类别的 off-diagonal 元素增长更快），topology vulnerability ranking 可能改变。
- 建议：增加一个实验，使用 class-frequency-weighted degradation path，测试 ASV ranking 稳定性。

**W4** [warning] Abstract/主文中 "2.1% sign reversal" 的限定不够清晰

- 具体位置：Abstract (p.1), Section 4.2 (p.7), Table 1 (p.7)
- 问题：Abstract 说 "sign reversal occurs in 2.1% of exposure configurations"，而 Table 1 显示 exposure 的 Sign Flip 为 **0%**。深入阅读后发现：
  - Table 1 的 0% 指 **primary coefficient**（largest |β_k|）在 full Dirichlet(1,1,1) 下不 flip
  - 2.1% 指 **secondary coefficient**（small effect sizes）在 diagonal ≥ 0.7 条件下 flip
  - Abstract 提到 "in secondary coefficients" 但不够醒目，易被读者误解为 treatment effect 本身逆转
- 为什么影响评分：这一表述差异可能导致读者对论文核心发现产生误判。2.1% treatment effect reversal vs. 2.1% minor coefficient reversal 的实践含义完全不同。
- 建议：(1) Table 1 增加注脚明确 "Sign Flip" 列指 primary coefficient；(2) Abstract 中改为 "secondary-coefficient sign reversal occurs in 2.1% of exposure configurations under realistic accuracy"。

**W5** [warning] IV 拓扑 52.6% vs. 0% sign reversal 差异缺乏充分解释

- 具体位置：Section 4.2 (p.7), Table 1 (p.7)
- 问题：Table 1 显示 IV 在 full Dirichlet(1,1,1) 下有 **52.6%** sign flip。但主文称 "across all 23 empirical LLM configurations, including low-accuracy annotators (mean diagonal as low as 0.45)—IV exhibits zero sign reversal"。从 52.6% 到 0% 的骤降需要比 "LLM confusion matrices have structural properties" 更具体的解释。
  - Dirichlet(1,1,1) 产生的矩阵平均 diagonal ≈ 1/K ≈ 0.33，大部分矩阵远低于实际 LLM 精度
  - 但即使 diagonal 低至 0.45，empirical LLM 仍为 0%——说明不仅是 diagonal dominance，还有其他结构性质（如 off-diagonal 对称性？near-permutation 结构？）阻止了 sign reversal
- 建议：分析 23 个 empirical LLM confusion matrix 的具体结构特征（如行间相关性、off-diagonal 对称度、eigenvalue 分布）与 sign reversal 的关系。

---

## 小问题（不影响接收）

- **M1** [minor] 线性 SEM 对 EMNLP 受众的适用性。NLP 中许多因果关系可能是非线性的。Appendix B.7（非线性 DGP robustness）和 B.14（logistic regression 下 FWL invariance 失效）提供了部分讨论，建议在主文 Section 4 或 Limitations 中更突出地引用这些结果，以便不读附录的 reviewer/读者了解适用范围。
- **M2** [minor] 23 个 LLM 配置的代表性有限。模型范围 7B-235B、三类任务（sentiment/stance/toxicity）——未覆盖 NER、QA、discourse parsing 等需要 multi-class annotation 的重要 NLP 任务。虽然理论结果不依赖具体任务，但 empirical validation 的 generalizability 受限。
- **M3** [minor] Conjecture 1 的 ε bound 可否 tighten。Table 10 实际 worst-case deviation 最大为 0.013，远低于 conjecture 的 ε < 0.06 bound（保守了约 4.6x）。如果能收紧 bound 会增强理论贡献的精度。
- **M4** [minor] 符号 τ vs. β_T 的含义。Section 3.1-3.2 同时使用 τ（true causal effect）和 β_T（SEM treatment coefficient），在 mediator 和 front-door 拓扑中 total effect ≠ direct effect，建议在首次出现时明确 τ 是 total、direct 还是 topology-specific causal estimand。

---

## 主要优势

- **S1** 问题定义新颖且重要：首次系统分析 K-class 标注误差在 7 种因果 DAG 拓扑下的传播模式，填补了 NLP annotation quality × causal inference 交叉领域的理论空白。将 Brenner (1993) 和 Carroll et al. (2006) 的经典测量误差理论扩展到 multi-class + multi-topology 设定。
- **S2** Sign preservation taxonomy 优雅且有实践价值：Proposition 1 将 7 种拓扑清晰分为 "sign-preserving"（confounding/collider：analytic proof）、"conditionally preserving"（mediation/M-bias/front-door：需额外条件）和 "sign-vulnerable"（exposure/IV），为实践者提供了直接可用的风险评估维度。
- **S3** FWL invariance impossibility 结果是重要的负面贡献：Section 4.5 + Appendix B.2 证明 matrix-based corrections（Naïve plug-in, MLA）在线性 OLS 下对四种 covariate 拓扑**无效**，避免实践者浪费精力在不可能有效的校正方法上。同时指出 logistic regression 下此约束解除，提供了理论指导的完整图景。
- **S4** ASV 三维度设计（magnitude/significance/sign-flip）比 E-values 更适合标注误差场景。Remark 1 (p.6) 对比 E-values 的三点差异——C 的 parametric structure、topology-specific sensitivity、sign-flip detection——论证有说服力。
- **S5** Algorithm 1 (p.31) 的校正决策树兼顾了 DAG uncertainty 和 topology-specific correction，从 "assess risk level" 到 "select correction method" 流程完整，具有工具价值。
- **S6** 附录详尽且系统：19 个 Appendix subsections (B.1-B.19) 覆盖了 binarization collapse、FWL invariance proof、ClinicalBERT case study、non-differential stress test、nonlinear DGP robustness、correction method sensitivity 等几乎所有可预见的 reviewer 质疑点，体现了严谨的研究态度。

---

## Questions

**Q1**: Theorem 1 的 proportional effects 条件在 K≥3 下如何影响 envelope 的形状？能否构造一个 non-proportional effects 下 monotonicity **完全失败**（不只是 ε-approximate 违反）的解析反例？Table 12 显示 independent effects 的 sign failure rate 为 23%，但这是 sign failure 而非 monotonicity failure——两者的关系是什么？

**Q2**: 23 个 LLM 配置在 IV 拓扑下**全部** 0% sign reversal（含 diagonal 低至 0.45 的低精度标注器），而 random Dirichlet 矩阵为 52.6%。请问：(a) 具体是 confusion matrix 的哪些结构属性阻止了 sign reversal？(b) 是否存在可以构造的 realistic-looking LLM confusion matrix（如通过 adversarial perturbation）使 IV sign reversal 发生？

**Q3**: ASV 的 uniform degradation path C(δ) = (1−δ)I + δC₀ 在 class-imbalanced 场景（如 3-class 中 rare class 占比 5%）下，ASV ranking 是否仍然可靠？Appendix B.11 仅改变了 β 但未改变 degradation path。

**Q4**: Abstract 中 "sign reversal occurs in 2.1% of exposure configurations" 具体指的是 primary 还是 secondary coefficient 的 reversal？如果仅为 secondary coefficient，这对实践者的含义（是否需要担忧）与 primary coefficient reversal 完全不同——请在论文中更明确地限定。

**Q5**: Non-differential misclassification 假设失败时（ε > 0.05, Appendix B.6），ASV 的 topology vulnerability **ranking**（不仅是 sign-flip rate）是否仍然保持 IV > Exposure > Collider > ... 的顺序？即 ASV 的 ranking 在 differential misclassification 下有多 robust？

---

## Missing References

1. **Hernán MA, Robins JM (2020). "Causal Inference: What If." Chapman & Hall/CRC.** —— 因果推断领域标准教材，论文讨论 DAG 拓扑和 identification 时应引用，尤其是 measurement error 对 identification 的影响（Chapter 9）。
2. **Veitch V, Sridhar D, Blei D (2020). "Adapting Text Embeddings for Causal Inference." AISTATS.** —— text-as-treatment 因果推断开创性工作，Related Work (Section 2) 中与 Keith et al. (2020) 和 Feder et al. (2022) 并列讨论更完整。

---

## Overall Assessment

**Overall**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5

**理由**：论文选题重要且及时，理论框架设计优雅，Proposition 1 的 sign preservation taxonomy 和 FWL invariance impossibility 是有价值的理论贡献，附录极其详尽。但两个核心问题制约了评分：

(1) **理论完整性**：论文标题和 narrative 聚焦 "Multi-Class"（K≥3），但最关键的 envelope monotonicity 结论（Theorem 1）仅对 K=2 有解析证明，K≥3 仅为数值验证的 conjecture。这使得 ASV 框架在 K≥3 下的理论基础不完整——从 reviewer 角度看，这是一个可以改善但目前存在的 gap。

(2) **实验验证深度**：Monte Carlo 一致性验证了数学公式，LLM empirical validation 验证了 confusion matrix 输入端，但缺少 outcome-level 端到端验证——在真实/半合成因果数据上展示 ASV 诊断→校正→改善估计的完整闭环。对于 EMNLP 受众，这一 gap 限制了对框架实际应用价值的判断。

此外，non-differential misclassification 和 proportional effects 两个关键假设的适用性讨论不足以让 NLP 研究者判断何时可以信任此框架。如果能 (a) 在 K≥3 的理论保证上取得进展（至少 partial proof 或更强的 adversarial verification），(b) 增加一个端到端案例研究，(c) 充实关键假设的适用性讨论，论文可达 Conference (4.0) 水平。

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

_source line 1302 · 2026-05-23T12:35:05.061887+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question/Missing Reference 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix\n\n**N1 [critical] ASV 与 E-value 的方法论创新边界不够清晰**\n- Section 3.3 (page 5-6)\n- ASV 核心思想是\"将 E-value 的未观测混杂强度参数替换为标注误差严重性参数\"。论文声称 ASV \"adapt the sensitivity analysis paradigm\"，但未充分阐明 adaptation 在方法论上引入了什么新的技术挑战。(a) E-value 参数化 relative risk，ASV 参数化 τ（混淆矩阵偏离单位矩阵的程度），但两者都是 \"minimum perturbation to nullify the effect\" 的逻辑——更像 reparametrization 而非 methodological innovation；(b) 三个子指标（magnitude, significance, sign-flip）本质是 E-value 在不同 threshold 下的实例化。\n- 建议：明确 E-value 不具备的特性：(1) topology-dependence，(2) sign-flip ASV 是 E-value 没有的对应物，(3) 混淆矩阵的参数空间与 E-value 的 relative risk 空间有本质几何差异。\n\n**N2 [critical] \"First unified analysis across seven topologies\" 的 novelty claim 需要更精确限定**\n- Section 1 (page 2)\n- \"first unified analysis of K-class annotator error propagation across seven canonical DAG topologies\" 需与 Carroll et al. (2006) Ch. 15 和 Schennach (2020) 的综述工作明确区分。Carroll 的框架虽非针对 LLM annotation，但在结构上也涵盖了多拓扑的 measurement error 分析。\n- 建议：限定为 \"first unified analysis *for LLM-generated multi-class annotations*\" 或 \"first analysis connecting confusion-matrix structure to topology-dependent bias *in the NLP pipeline context*\"。\n\n### Should-Fix\n\n**W1 [warning] Abstract 信息密度过高**\n- 188 词试图覆盖七种拓扑、K≥3 符号反转、符号保持证明、2.1% exposure、23 组 LLM 配置、52.6% IV、ASV monotonicity、FWL 不变性。建议精简到 3-4 个核心信息点，移除具体百分比。\n\n**W2 [warning] 对 EMNLP 受众可及性不足**\n- plim 首次出现在 Section 3.2 仅有脚注解释；FWL theorem 在 Section 3.1 未给直观解释；Wald estimator、column-stochastic matrix、Dirichlet prior 均缺乏直觉性说明。\n\n**W3 [warning] 符号反转实际风险可能被高估**\n- 真实 LLM 精度下符号反转仅发生在 exposure 2.1% 配置的次要系数。5/7 拓扑 sign reversal 为 0%。IV 52.6% 是 uniform Dirichlet 理论极端情形。Abstract/Introduction framing 给人\"符号反转是普遍严重风险\"的印象。\n\n**W4 [warning] Figure 2 子图过小，灰度打印无法区分**\n- 七个子图挤在半页宽度，红灰颜色区分依赖彩色打印。\n\n**W5 [warning] 实验仅基于模拟，缺少真实因果数据集验证**\n- Monte Carlo + LLM confusion matrix + ClinicalBERT 均为合成/半合成。缺少在 IHDP/LaLonde/ACIC 等已知因果效应数据集上的验证。\n\n**W6 [warning] Correction guidance 定位模糊**\n- 作为三大贡献之一，Section 4.5 仅半页讨论。五种方法选择标准未说明，缺少计算成本和样本量讨论，FWL 不变性验证仅在 Appendix B.2。\n\n### Minor\n\n**M1** Table 1 列标题定义不清（Violation/Sign Flip/Amplif./τ_sf=0?）。\n**M2** Section 3.2 equation (1) 符号引导分散，Notation table (Table 19) 放在 Appendix C。\n**M3** Schennach (2020) 在 bib 未在正文引用。\n**M4** Conjecture 1 \"approximately\" 未量化，主文应提示 worst-case 量级。\n**M5** C₀ 选取方式仅在 appendix 说明。\n\n### Questions\n\n**Q1** ASV 的 topology-dependent 特性能否反向推断 DAG 拓扑？\n**Q2** 非微分假设在 LLM 部署中的 differential misclassification 程度是否远超 ε=0.05？\n**Q3** FWL 不变性是否推广到 logistic regression？Appendix B.14 显示 exposure 偏差 ~78%。如果 FWL 在非线性下不成立，矩阵校正在 logistic 下反而可用？主文完全缺失此讨论。\n**Q4** K=2 的 CivilComments 为何被选为验证数据集？论文核心 novelty 在 K≥3。\n**Q5** Table 2 中 Violation 和 Sign Flip 列的包含关系不直观。\n\n### Missing References\n\n**R1** Miles, Valeri, and Coull (2024). \"Measurement Error-Robust Causal Inference via Constructed Instrumental Variables.\" arXiv:2406.00940.\n**R2** Wei, He, Li, and Geng (2025). \"Multiply robust causal inference in the presence of an error-prone treatment.\" Statistical Methods in Medical Research.\n**R3** Schennach (2020) 正文引用。\n**R4** Manski (1990) bounds approach 在 Related Work 中讨论。\n\n---\n\n请对以上每个 Weakness、Question 和 Missing Reference 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question/Missing Reference 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix\n\n**N1 [critical] ASV 与 E-value 的方法论创新边界不够清晰**\n- Section 3.3 (page 5-6)\n- ASV 核心思想是\"将 E-value 的未观测混杂强度参数替换为标注误差严重性参数\"。论文声称 ASV \"adapt the sensitivity analysis paradigm\"，但未充分阐明 adaptation 在方法论上引入了什么新的技术挑战。(a) E-value 参数化 relative risk，ASV 参数化 τ（混淆矩阵偏离单位矩阵的程度），但两者都是 \"minimum perturbation to nullify the effect\" 的逻辑——更像 reparametrization 而非 methodological innovation；(b) 三个子指标（magnitude, significance, sign-flip）本质是 E-value 在不同 threshold 下的实例化。\n- 建议：明确 E-value 不具备的特性：(1) topology-dependence，(2) sign-flip ASV 是 E-value 没有的对应物，(3) 混淆矩阵的参数空间与 E-value 的 relative risk 空间有本质几何差异。\n\n**N2 [critical] \"First unified analysis across seven topologies\" 的 novelty claim 需要更精确限定**\n- Section 1 (page 2)\n- \"first unified analysis of K-class annotator error propagation across seven canonical DAG topologies\" 需与 Carroll et al. (2006) Ch. 15 和 Schennach (2020) 的综述工作明确区分。Carroll 的框架虽非针对 LLM annotation，但在结构上也涵盖了多拓扑的 measurement error 分析。\n- 建议：限定为 \"first unified analysis *for LLM-generated multi-class annotations*\" 或 \"first analysis connecting confusion-matrix structure to topology-dependent bias *in the NLP pipeline context*\"。\n\n### Should-Fix\n\n**W1 [warning] Abstract 信息密度过高**\n- 188 词试图覆盖七种拓扑、K≥3 符号反转、符号保持证明、2.1% exposure、23 组 LLM 配置、52.6% IV、ASV monotonicity、FWL 不变性。建议精简到 3-4 个核心信息点，移除具体百分比。\n\n**W2 [warning] 对 EMNLP 受众可及性不足**\n- plim 首次出现在 Section 3.2 仅有脚注解释；FWL theorem 在 Section 3.1 未给直观解释；Wald estimator、column-stochastic matrix、Dirichlet prior 均缺乏直觉性说明。\n\n**W3 [warning] 符号反转实际风险可能被高估**\n- 真实 LLM 精度下符号反转仅发生在 exposure 2.1% 配置的次要系数。5/7 拓扑 sign reversal 为 0%。IV 52.6% 是 uniform Dirichlet 理论极端情形。Abstract/Introduction framing 给人\"符号反转是普遍严重风险\"的印象。\n\n**W4 [warning] Figure 2 子图过小，灰度打印无法区分**\n- 七个子图挤在半页宽度，红灰颜色区分依赖彩色打印。\n\n**W5 [warning] 实验仅基于模拟，缺少真实因果数据集验证**\n- Monte Carlo + LLM confusion matrix + ClinicalBERT 均为合成/半合成。缺少在 IHDP/LaLonde/ACIC 等已知因果效应数据集上的验证。\n\n**W6 [warning] Correction guidance 定位模糊**\n- 作为三大贡献之一，Section 4.5 仅半页讨论。五种方法选择标准未说明，缺少计算成本和样本量讨论，FWL 不变性验证仅在 Appendix B.2。\n\n### Minor\n\n**M1** Table 1 列标题定义不清（Violation/Sign Flip/Amplif./τ_sf=0?）。\n**M2** Section 3.2 equation (1) 符号引导分散，Notation table (Table 19) 放在 Appendix C。\n**M3** Schennach (2020) 在 bib 未在正文引用。\n**M4** Conjecture 1 \"approximately\" 未量化，主文应提示 worst-case 量级。\n**M5** C₀ 选取方式仅在 appendix 说明。\n\n### Questions\n\n**Q1** ASV 的 topology-dependent 特性能否反向推断 DAG 拓扑？\n**Q2** 非微分假设在 LLM 部署中的 differential misclassification 程度是否远超 ε=0.05？\n**Q3** FWL 不变性是否推广到 logistic regression？Appendix B.14 显示 exposure 偏差 ~78%。如果 FWL 在非线性下不成立，矩阵校正在 logistic 下反而可用？主文完全缺失此讨论。\n**Q4** K=2 的 CivilComments 为何被选为验证数据集？论文核心 novelty 在 K≥3。\n**Q5** Table 2 中 Violation 和 Sign Flip 列的包含关系不直观。\n\n### Missing References\n\n**R1** Miles, Valeri, and Coull (2024). \"Measurement Error-Robust Causal Inference via Constructed Instrumental Variables.\" arXiv:2406.00940.\n**R2** Wei, He, Li, and Geng (2025). \"Multiply robust causal inference in the presence of an error-prone treatment.\" Statistical Methods in Medical Research.\n**R3** Schennach (2020) 正文引用。\n**R4** Manski (1990) bounds approach 在 Related Work 中讨论。\n\n---\n\n请对以上每个 Weakness、Question 和 Missing Reference 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 1303 · 2026-05-23T12:35:47.746940+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 42685
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-23T12:35:48.048661+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question/Missing Reference 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix\n\n**N1 [critical] Theorem 1 (envelope monotonicity) 仅对 K=2 成立，K≥3 为 Conjecture——与论文标题和核心 narrative 不匹配**\n- Section 3.3 Theorem 1, Conjecture 1 (p.6), Appendix A.4 (p.14-15), Table 10 (p.27)\n- 问题：(1) Dirichlet(1,…,1) 采样在高维空间覆盖率极低（K=7 时 42 自由度），210,000 样本可能遗漏 adversarial corner cases；(2) Table 10 显示 60-97% 矩阵存在单调性违反（magnitude ≤ 0.013），exact monotonicity 在 K≥3 下系统性不成立；(3) IV 拓扑 79% 违反（K=7），worst magnitude 0.009。\n- 论文标题和 narrative 聚焦 \"Multi-Class\"（K≥3），但核心单调性结论仅为 conjecture，ASV 框架在 K≥3 下的理论基础不完整。\n- 建议：(1) abstract/intro 精确区分 \"K=2 proven\" vs \"K≥3 conjectured\"；(2) 补充 adversarial 搜索（梯度优化寻找违反矩阵）；(3) 讨论 Conjecture 不成立时 ASV 的 graceful degradation。\n\n**N2 [critical] 缺乏真实因果数据的端到端验证**\n- Section 4, Appendix B.3\n- 实验仅有两层：(1) 解析公式 vs MC（MAPE 1.6%）→ 验证公式正确性；(2) 23 个 LLM confusion matrix 性质 → 验证输入端行为。缺少第三层：在已知 ground-truth 因果效应的数据上完整演示 \"估计 C → ASV 诊断 → 校正 → 改善估计\" 的端到端流程。\n- ClinicalBERT case study 的 \"ground truth\" 来自 OLS on gold labels，不是真正已知因果效应。\n- 建议：构建半合成 CSS 数据集或在 ClinicalBERT 案例中划出 gold-label 子集作为 ground truth 对照。\n\n### Should-Fix\n\n**W1 [warning] Non-differential misclassification 假设在 LLM 场景下的适用性——主文讨论不足**\n- Definition 1 (Section 3.1, p.4)\n- P(A*=j|A=k,Y,Z) = P(A*=j|A=k) 在 LLM 标注中是强假设。LLM 可能利用与 outcome 相关的上下文线索。\n- 主文仅一句 \"This holds when the LLM classifies without observing the outcome\"，过于简略。\n- 建议：增加何时成立/何时失败/如何检验的讨论。\n\n**W2 [warning] Proportional effects 假设 (f=λg) 缺乏实践验证指导**\n- Theorem 1 条件 (p.6)\n- Treatment effect 是待估计的未知量，无法在估计前验证其成比例性。Appendix B.13 Table 12 显示 independent effects 下 sign failure rate 23%。\n- 建议：讨论 testable implications 和哪类 NLP 任务更可能满足此假设。\n\n**W3 [warning] ASV 参数化 C(δ) 假设均匀退化与 LLM 实际误差模式不符**\n- Section 3.3 (p.5-6)\n- 稀有类别通常先出错（class-imbalanced degradation），不同类别对混淆概率退化速率不一致。\n- 建议：增加 class-frequency-weighted degradation path 实验。\n\n**W4 [warning] \"2.1% sign reversal\" 限定不够清晰**\n- Abstract (p.1), Section 4.2 (p.7), Table 1 (p.7)\n- Table 1 exposure Sign Flip 为 0%（指 primary coefficient），2.1% 指 secondary coefficient——读者容易误解为 treatment effect 本身逆转。\n- 建议：Table 1 增注脚、Abstract 改为 \"secondary-coefficient sign reversal\"。\n\n**W5 [warning] IV 52.6% vs. 0% sign reversal 差异缺乏充分解释**\n- 从 Dirichlet 的 52.6% 到 empirical LLM 的 0% 骤降，需要比 \"structural properties\" 更具体的解释。\n- 建议：分析 23 个 LLM confusion matrix 的具体结构特征。\n\n### Minor\n\n**M1** 线性 SEM 对 EMNLP 受众的适用性，建议主文引用 Appendix B.7/B.14 结果。\n**M2** 23 个 LLM 配置代表性有限（7B-235B，三类任务）。\n**M3** Conjecture 1 ε bound 保守 4.6x（0.013 vs 0.06），能否 tighten。\n**M4** 符号 τ vs. β_T 含义在 mediator/front-door 拓扑下不清晰。\n\n### Questions\n\n**Q1** Non-proportional effects 下 monotonicity 能否完全失败（不只是 ε-approximate 违反）？Table 12 的 sign failure vs monotonicity failure 关系？\n**Q2** 23 个 LLM 在 IV 全部 0% sign reversal——具体哪些 confusion matrix 结构属性阻止了 sign reversal？能否构造 realistic-looking LLM confusion matrix 使 IV sign reversal 发生？\n**Q3** Class-imbalanced 场景（如 rare class 5%）下 ASV ranking 是否仍可靠？\n**Q4** \"2.1% sign reversal\" 指 primary 还是 secondary coefficient？\n**Q5** Non-differential 假设失败时 ASV topology vulnerability ranking 是否保持 IV > Exposure > Collider > ... 的顺序？\n\n### Missing References\n\n**MR1** Hernán MA, Robins JM (2020). \"Causal Inference: What If.\" Chapman & Hall/CRC. Chapter 9 关于 measurement error 对 identification 的影响。\n**MR2** Veitch V, Sridhar D, Blei D (2020). \"Adapting Text Embeddings for Causal Inference.\" AISTATS. text-as-treatment 开创性工作。\n\n---\n\n请对以上每个 Weakness、Question 和 Missing Reference 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question/Missing Reference 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix\n\n**N1 [critical] Theorem 1 (envelope monotonicity) 仅对 K=2 成立，K≥3 为 Conjecture——与论文标题和核心 narrative 不匹配**\n- Section 3.3 Theorem 1, Conjecture 1 (p.6), Appendix A.4 (p.14-15), Table 10 (p.27)\n- 问题：(1) Dirichlet(1,…,1) 采样在高维空间覆盖率极低（K=7 时 42 自由度），210,000 样本可能遗漏 adversarial corner cases；(2) Table 10 显示 60-97% 矩阵存在单调性违反（magnitude ≤ 0.013），exact monotonicity 在 K≥3 下系统性不成立；(3) IV 拓扑 79% 违反（K=7），worst magnitude 0.009。\n- 论文标题和 narrative 聚焦 \"Multi-Class\"（K≥3），但核心单调性结论仅为 conjecture，ASV 框架在 K≥3 下的理论基础不完整。\n- 建议：(1) abstract/intro 精确区分 \"K=2 proven\" vs \"K≥3 conjectured\"；(2) 补充 adversarial 搜索（梯度优化寻找违反矩阵）；(3) 讨论 Conjecture 不成立时 ASV 的 graceful degradation。\n\n**N2 [critical] 缺乏真实因果数据的端到端验证**\n- Section 4, Appendix B.3\n- 实验仅有两层：(1) 解析公式 vs MC（MAPE 1.6%）→ 验证公式正确性；(2) 23 个 LLM confusion matrix 性质 → 验证输入端行为。缺少第三层：在已知 ground-truth 因果效应的数据上完整演示 \"估计 C → ASV 诊断 → 校正 → 改善估计\" 的端到端流程。\n- ClinicalBERT case study 的 \"ground truth\" 来自 OLS on gold labels，不是真正已知因果效应。\n- 建议：构建半合成 CSS 数据集或在 ClinicalBERT 案例中划出 gold-label 子集作为 ground truth 对照。\n\n### Should-Fix\n\n**W1 [warning] Non-differential misclassification 假设在 LLM 场景下的适用性——主文讨论不足**\n- Definition 1 (Section 3.1, p.4)\n- P(A*=j|A=k,Y,Z) = P(A*=j|A=k) 在 LLM 标注中是强假设。LLM 可能利用与 outcome 相关的上下文线索。\n- 主文仅一句 \"This holds when the LLM classifies without observing the outcome\"，过于简略。\n- 建议：增加何时成立/何时失败/如何检验的讨论。\n\n**W2 [warning] Proportional effects 假设 (f=λg) 缺乏实践验证指导**\n- Theorem 1 条件 (p.6)\n- Treatment effect 是待估计的未知量，无法在估计前验证其成比例性。Appendix B.13 Table 12 显示 independent effects 下 sign failure rate 23%。\n- 建议：讨论 testable implications 和哪类 NLP 任务更可能满足此假设。\n\n**W3 [warning] ASV 参数化 C(δ) 假设均匀退化与 LLM 实际误差模式不符**\n- Section 3.3 (p.5-6)\n- 稀有类别通常先出错（class-imbalanced degradation），不同类别对混淆概率退化速率不一致。\n- 建议：增加 class-frequency-weighted degradation path 实验。\n\n**W4 [warning] \"2.1% sign reversal\" 限定不够清晰**\n- Abstract (p.1), Section 4.2 (p.7), Table 1 (p.7)\n- Table 1 exposure Sign Flip 为 0%（指 primary coefficient），2.1% 指 secondary coefficient——读者容易误解为 treatment effect 本身逆转。\n- 建议：Table 1 增注脚、Abstract 改为 \"secondary-coefficient sign reversal\"。\n\n**W5 [warning] IV 52.6% vs. 0% sign reversal 差异缺乏充分解释**\n- 从 Dirichlet 的 52.6% 到 empirical LLM 的 0% 骤降，需要比 \"structural properties\" 更具体的解释。\n- 建议：分析 23 个 LLM confusion matrix 的具体结构特征。\n\n### Minor\n\n**M1** 线性 SEM 对 EMNLP 受众的适用性，建议主文引用 Appendix B.7/B.14 结果。\n**M2** 23 个 LLM 配置代表性有限（7B-235B，三类任务）。\n**M3** Conjecture 1 ε bound 保守 4.6x（0.013 vs 0.06），能否 tighten。\n**M4** 符号 τ vs. β_T 含义在 mediator/front-door 拓扑下不清晰。\n\n### Questions\n\n**Q1** Non-proportional effects 下 monotonicity 能否完全失败（不只是 ε-approximate 违反）？Table 12 的 sign failure vs monotonicity failure 关系？\n**Q2** 23 个 LLM 在 IV 全部 0% sign reversal——具体哪些 confusion matrix 结构属性阻止了 sign reversal？能否构造 realistic-looking LLM confusion matrix 使 IV sign reversal 发生？\n**Q3** Class-imbalanced 场景（如 rare class 5%）下 ASV ranking 是否仍可靠？\n**Q4** \"2.1% sign reversal\" 指 primary 还是 secondary coefficient？\n**Q5** Non-differential 假设失败时 ASV topology vulnerability ranking 是否保持 IV > Exposure > Collider > ... 的顺序？\n\n### Missing References\n\n**MR1** Hernán MA, Robins JM (2020). \"Causal Inference: What If.\" Chapman & Hall/CRC. Chapter 9 关于 measurement error 对 identification 的影响。\n**MR2** Veitch V, Sridhar D, Blei D (2020). \"Adapting Text Embeddings for Causal Inference.\" AISTATS. text-as-treatment 开创性工作。\n\n---\n\n请对以上每个 Weakness、Question 和 Missing Reference 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-23T12:35:49.513295+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1464
}
```

</details>

---


### Assistant

_source line 1306 · 2026-05-23T12:35:57.334695+00:00_

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


## Round 129

## Round 129

2 recorded events


### User

_source line 1307 · 2026-05-23T12:35:59.971328+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿意见（约 3500 字），评分 **3.5/5 (Borderline Conference)**，置信度 4/5。

核心发现：
- **2 个 Must-Fix**：(1) Theorem 1 仅对 K=2 证明，K≥3 为 conjecture，与 "Multi-Class" 标题不匹配；(2) 缺乏真实因果数据端到端验证
- **5 个 Should-Fix**：non-differential 假设讨论不足、proportional effects 无法先验验证、ASV 均匀退化假设、abstract 中 2.1% sign reversal 限定不清、IV 的 52.6% vs 0% 差异未解释
- **6 个主要优势**：问题新颖、sign preservation taxonomy 优雅、FWL impossibility 有价值、ASV 设计合理、Algorithm 1 实用、附录详尽

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

_source line 1308 · 2026-05-23T12:36:04.388640+00:00_

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


## Round 130

## Round 130

2 recorded events


### User

_source line 1309 · 2026-05-23T12:38:09.546896+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: Theorem 1 monotonicity 仅对 K=2 成立，K≥3 为 Conjecture**

同意这是一个实质性问题。论文标题聚焦 "Multi-Class"（K≥3），但 ASV 框架的理论支柱——envelope monotonicity——在 K≥3 下仅为 Conjecture 1 (page 6)，依赖 210,000 随机矩阵的数值验证。

我补充两点强化 R1 的论点：

(1) **数值验证的覆盖率问题确实存在但可能被 R1 高估。** Table 10 (Appendix B.12) 显示 K=3 时 60-97% 的矩阵存在违反，但 worst magnitude 仅 0.008-0.013。这说明 exact monotonicity 系统性不成立，但偏差极小。问题在于：论文将此解释为 "approximately monotone"（Conjecture 1 的 ε-approximate 表述），但 0.013 的 bound 是否足以保证 ASV ranking 的实用稳定性？论文未给出 "多大的违反会导致 ranking 翻转" 的分析。

(2) **与我自己的 N1 (ASV vs E-value) 交叉关联。** 如果 ASV 的 monotonicity 在 K≥3 下仅为 approximate，那么 ASV 的 topology vulnerability ranking（IV > Exposure > ... > M-bias）的可靠性也变得依赖于 ε 的大小。论文应讨论在 ε = 0.013 的违反幅度下，ranking 是否可能翻转。

但我不同意 R1 的建议 (2)——"补充 adversarial 搜索（梯度优化寻找违反矩阵）"。Column-stochastic 矩阵的约束空间（每列和为 1，所有元素非负）使得梯度优化需要投影到 simplex 上，实现复杂且不一定比大规模随机采样更有说服力。更实用的方案是增加采样量到 10⁶ 并报告违反分布的尾部行为。

**[AGREE] R1-N2: 缺乏真实因果数据的端到端验证**

完全同意。这与我自己的 W5 一致。论文目前的验证结构是：

- Layer 1: 解析公式 vs Monte Carlo → 验证数学正确性 ✓
- Layer 2: 23 个 LLM confusion matrix 的性质 → 验证输入端行为 ✓
- Layer 3: 端到端因果效应恢复 → **缺失**

R1 正确指出 ClinicalBERT 案例 (Appendix B.3) 的 "ground truth" 来自 OLS on gold labels，不是真正已知的因果效应。这意味着论文的实际验证止步于 "公式算对了" 和 "LLM 矩阵的统计性质"，但从未展示过 "使用本文方法确实改善了因果估计"。

R1 的建议——半合成 CSS 数据集——是合理的。例如用 LaLonde (1986) 或 IHDP 数据集注入已知误分类，验证 ASV 诊断 → 校正选择 → 估计改善的完整流程。但我认为这对本文的 rebuttal 周期来说工作量偏大。作为替代，至少应在 Limitations 中明确承认这一缺失（目前的 Limitations section 未提及）。

---

### Should-Fix

**[AGREE] R1-W1: Non-differential misclassification 假设的适用性讨论不足**

同意。Definition 1 (Section 3.1, page 4) 要求 P(A*=j|A=k,Y,Z) = P(A*=j|A=k)，即误分类概率不依赖于 outcome 和其他变量。对 LLM 来说，如果输入文本同时包含与 outcome 相关的线索（例如灾害推文中的紧急程度词汇既影响分类又与 outcome 相关），这个假设可能被违反。

论文确实在 Appendix B.6 做了 non-differential assumption stress test（page 24, Table 7），显示 ε ≤ 0.10 时 sign-flip 率 ≤ 20.9%。但 R1 正确指出主文仅一句话讨论了这个假设（"This holds when the LLM classifies without observing the outcome"），而 Appendix B.6 的详细分析未被主文充分引用。

建议在 Section 3.1 增加 2-3 句话：(1) 什么条件下假设成立（LLM 分类时未观察 outcome，或 prompt 中不包含 outcome-correlated 信息），(2) 什么条件下可能失败（LLM 利用上下文线索），(3) 引用 Appendix B.6 的稳健性结果。

**[AGREE] R1-W2: Proportional effects 假设的实践验证指导不足**

同意。Theorem 1 (page 6) 的 sign preservation 依赖 f = λg（treatment effect 与 confounding bias 成比例）。R1 正确指出：treatment effect 是待估计的未知量，无法在估计前验证成比例性。

Appendix B.13 Table 12 是关键证据：在 independent effects (f ⊥ g) 下，sign failure rate 达到 23%。这意味着在比例效应假设不成立时，即使是 confounding 拓扑也可能出现符号反转——直接削弱了 "confounding preserves sign" 这一核心结论的适用范围。

论文应该在主文中更明确地讨论：(a) 哪类 NLP 任务更可能满足比例效应（例如 treatment 和 confounder 影响方向一致的情况），(b) 不满足时的 fallback 策略。

**[AGREE] R1-W3: ASV C(δ) 均匀退化假设**

同意，但认为影响程度比 R1 评估的稍低。C(δ) = (1-δ)I + δC₀ 的线性插值确实假设所有类别以相同速率退化。真实 LLM 中，稀有类别（如 K=10 时占 5% 的类别）通常先出错。

但我注意到论文的 empirical validation (Section 4.4) 使用的是真实 LLM confusion matrices（来自 HumAID K=10, VAST K=3），这些矩阵本身就包含了 class-imbalanced 退化模式。如果 ASV ranking 在这些真实矩阵上仍然稳定（Table 1 显示是的），那么 C(δ) 的均匀退化主要影响的是 ASV 的绝对值而非拓扑间的相对排序。

仍然建议增加 class-frequency-weighted degradation 实验作为稳健性检查。

**[AGREE] R1-W4: "2.1% sign reversal" 限定不够清晰**

完全同意。这与我自己的 W3 一致。Abstract 中 "sign reversal occurs in 2.1% of exposure configurations" 确实容易被理解为 primary treatment effect 的符号反转，但实际上（根据 Table 1 和 Section 4.2 的讨论）这是 secondary coefficient 的反转。

论文应在 abstract 中明确写 "secondary-coefficient sign reversal"，并在 Table 1 增加脚注说明 "Sign Flip" 列指的是哪个系数。

**[REBUT] R1-W5: IV 52.6% vs 0% sign reversal 差异缺乏充分解释**

部分不同意。R1 要求 "比 structural properties 更具体的解释"，但我认为论文实际上给出了合理的（虽然简短的）解释。

Section 4.2 (page 7) 和 Appendix B.10 (page 26) 提供了以下解释：(1) Dirichlet(1,...,1) 采样产生的 confusion matrices 包含大量 "极端" 矩阵（对角线元素很小，接近随机分类），这些矩阵在真实 LLM 中不会出现；(2) 23 个真实 LLM 的 mean diagonal 在 0.45-0.81 之间，远高于 Dirichlet 均匀分布的期望值 1/K；(3) IV 拓扑的 sign reversal 需要 Wald estimator 的分母（first-stage coefficient）符号翻转，这要求 confusion matrix 严重偏离对角占优——在真实 LLM 中不太可能发生。

Table 9 (Appendix B.11, page 26) 进一步展示了不同 DGP 参数下 ASV 的稳定性，包含了对 IV 行为的拓扑特异性分析。

但我同意论文可以在主文中增加 1-2 句更直觉的解释，例如 "The gap reflects that uniform Dirichlet priors generate confusion matrices far from the diagonal-dominant structure typical of real LLMs, making the 52.6% an upper bound rather than a realistic estimate."

---

### Minor

**[AGREE] R1-M1:** 同意。主文应引用 Appendix B.7 (nonlinear DGP) 和 B.14 (logistic regression) 的结果，让读者知道线性假设的局限性和非线性扩展的存在。这与我自己的 Q3 一致。

**[AGREE] R1-M2:** 同意。23 个 LLM 配置覆盖 3 类任务（灾害、立场、文明度），模型范围 7B-235B。缺少更多样化的任务类型（如情感分析 K=5、政治立场 K=4 等）。但考虑到获取真实 K≥3 LLM confusion matrices 的成本，现有覆盖是可以接受的。

**[AGREE] R1-M3:** 同意这是一个 minor 问题。ε bound 的保守性（4.6x）不影响主要结论，但 tightening 会增强 Conjecture 1 的说服力。

**[AGREE] R1-M4:** 同意。τ 在 Section 3 中时而指 treatment effect，时而指 sign-flip threshold（τ_sf），在 mediator 和 front-door 拓扑下 β_T 的含义（direct effect vs total effect vs 哪个 path 的系数）需要更清晰的定义。

---

### Questions

**[AGREE] R1-Q1:** 好问题。Appendix B.13 Table 12 显示 independent effects 下 sign failure rate 23%，但未报告对应的 monotonicity violation 程度。如果 non-proportional effects 导致 monotonicity 完全失败（而非 ε-approximate 违反），那么 ASV 在这种情况下的诊断价值将受到严重质疑。作者应补充 independent effects 下的 monotonicity 违反数据。

**[AGREE] R1-Q2:** 好问题，与 W5 相关。作者应分析 23 个 LLM confusion matrices 的具体结构属性（如 diagonal dominance 程度、off-diagonal 分散度），解释为什么它们都避免了 IV sign reversal。构造 "realistic-looking" 但导致 sign reversal 的矩阵是一个有价值的反事实分析。

**[AGREE] R1-Q3:** 与 W3 相关。Class-imbalanced 场景是论文未充分覆盖的实际问题。当 rare class 占 5% 时，confusion matrix 的对应行/列会有极高的 misclassification rate，可能改变 ASV ranking。

**[AGREE] R1-Q4:** 这与 W4 一致，答案应该是 secondary coefficient。论文需要在 abstract 和 Table 1 中明确这一点。

**[REBUT] R1-Q5:** 部分不同意这个问题的前提。论文的 topology vulnerability ranking（IV > Exposure > ... > M-bias）是在 non-differential 假设下推导的。如果假设失败，ranking 的含义本身就需要重新定义——因为 differential misclassification 下的 bias expression 完全不同（每个拓扑的 bias 都可能增大或减小，取决于 differential 的方向）。

Appendix B.6 Table 7 的 stress test 结果显示，在 ε ≤ 0.10 的弱违反下，基本排序仍然保持（confounding 最稳健，exposure 最脆弱）。但这是数值观察，不是理论保证。我认为更准确的回答是：ranking 在弱违反下大致保持，但在强 differential misclassification 下没有理论保证——这本身是合理的，因为强 differential 下整个分析框架都需要更换。

---

### Missing References

**[AGREE] R1-MR1:** Hernán & Robins (2020) "Causal Inference: What If" 是因果推断领域的标准教科书，Chapter 9 讨论 measurement error 对 identification 的影响。论文引用了 Hernán & Cole (2009) 但未引用这本更完整的教科书参考。应在 Section 2 measurement error 段落中加入。

**[REBUT] R1-MR2:** Veitch, Sridhar & Blei (2020) "Adapting Text Embeddings for Causal Inference" 主要处理 text-as-treatment/confounder 的 representation learning 问题，与本文的 measurement error propagation 主题关联较弱。论文已引用了 Feder et al. (2022) 和 Pryzant et al. (2021)，这两篇覆盖了 text-based causal inference 的核心方法论。Veitch et al. 的方法假设 treatment 是从文本中派生的连续表示，而非本文关注的离散多类别分类。不引用不构成重要遗漏。

---

### 总结

R1 的审稿意见整体质量高，抓住了论文的核心弱点。我对 R1 意见的同意率约 85%。

**最关键的共识**：
1. Conjecture vs Theorem 的差距确实是论文最大的理论弱点（R1-N1，与我的 N1 关于 ASV 创新边界的 concern 互补）
2. 缺乏端到端真实数据验证（R1-N2，与我的 W5 一致）
3. "2.1% sign reversal" 的 framing 有 overclaim 风险（R1-W4，与我的 W3 一致）

**主要分歧**：
1. IV 52.6% vs 0% 的解释（R1-W5）：我认为论文在 appendix 中提供了足够解释，主文可增加但不是 critical
2. MR2 (Veitch et al. 2020)：与论文主题关联较弱，不构成重要遗漏
3. R1-Q5 的前提：differential misclassification 下 ranking 的讨论应该定位为"框架局限性"而非"需要验证的额外 claim"

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

_source line 1310 · 2026-05-23T12:38:22.955501+00:00_

Reviewer 2 的交叉回应已收到（同意率约 85%）。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 131

## Round 131

2 recorded events


### User

_source line 1311 · 2026-05-23T12:38:25.676455+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。

核心结论：与 R1 的同意率约 85%。最大共识在 Conjecture vs Theorem 的理论弱点、缺乏端到端验证、以及 sign reversal framing 的 overclaim 风险。主要分歧在 IV 52.6% vs 0% 的解释充分性（我认为 appendix 已有合理解释）和 Veitch et al. (2020) 的引用必要性（我认为与本文主题关联较弱）。

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

_source line 1312 · 2026-05-23T12:38:29.978013+00:00_

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


## Round 132

## Round 132

12 recorded events


### User

_source line 1313 · 2026-05-23T12:38:46.259146+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R2-N1: ASV 与 E-value 的方法论创新边界不够清晰**

R2 认为 ASV 仅是 E-value 的 reparametrization，核心逻辑均为 "minimum perturbation to nullify the effect"。我认为这一判断低估了 ASV 的方法论差异，原因如下：

1. **Topology-dependence 是结构性创新而非参数替换**。E-value 给出单一标量 bound，不区分 DAG 结构。ASV 的核心贡献在于揭示同一 confusion matrix 在不同拓扑下产生截然不同的 bias 行为——Remark 1 (p.6) 明确指出 "Topology dependence: the same C preserves sign under confounding but can reverse it under exposure (Table 1)"。这不是 threshold 的实例化，而是 sensitivity analysis 的参数空间从一维（relative risk γ）变为拓扑-特定的 confusion matrix manifold。

2. **Sign-flip ASV 确实没有 E-value 对应物**。E-value 仅考虑 "effect → null" 方向的 robustness，不考虑 "effect → opposite sign"。Sign-flip ASV（Section 3.3, p.5-6）定义了一个 E-value 框架中不存在的诊断维度。R2 将三个子指标描述为 "E-value 在不同 threshold 下的实例化" 是不准确的——magnitude ASV 和 significance ASV 的 threshold 确实类似 E-value 逻辑，但 sign-flip ASV 检测的是 bias 方向反转，这在 E-value 的 relative risk 框架中没有自然对应。

3. **但 R2 的建议是建设性的**。论文确实可以在 Remark 1 中更明确地强调这些差异的 **技术挑战**来源（如 confusion matrix 的 Birkhoff polytope 几何 vs. relative risk 的 [1,∞) 半线），而不仅是列举差异。

**结论**：ASV 不仅仅是 reparametrization——topology-dependence 和 sign-flip 维度是 E-value 不具备的结构性创新。但论文可以更好地 articulate 技术挑战的新颖性。建议降级为 should-fix。

---

**[AGREE] R2-N2: "First unified analysis" novelty claim 需要更精确限定**

R2 的关切合理。Carroll et al. (2006) 的测量误差框架在结构上确实涵盖了多种回归设定下的 measurement error 分析，虽然不是针对 LLM annotation 或 DAG topology 的系统性分析。论文的真正创新在于：(a) 将 confusion matrix 结构与 DAG topology 的**交互作用**系统化（7 拓扑 × K-class），(b) 在 NLP annotation pipeline 语境下给出可操作的诊断。

建议改为 "first unified analysis connecting K-class confusion-matrix structure to topology-dependent bias across seven canonical DAG topologies in the context of LLM-generated annotations"，既保留 novelty 又避免与 Carroll et al. (2006) 的通用框架混淆。

---

### Should-Fix

**[AGREE] R2-W1: Abstract 信息密度过高**

同意。Abstract 试图覆盖七种拓扑、K≥3 sign reversal、sign preservation 证明、2.1%/52.6% 等具体数字、ASV monotonicity、FWL invariance 等全部内容。我在自己的 W4 中也指出 "2.1% sign reversal" 的限定不清晰，信息过载加剧了这一问题。建议精简到 3-4 个核心 message：(1) multi-class bias is topology-dependent, (2) sign preservation taxonomy, (3) ASV framework, (4) correction guidance。具体百分比移入 Section 4。

---

**[AGREE] R2-W2: 对 EMNLP 受众可及性不足**

同意。plim（p.4 仅脚注解释）、FWL theorem（Section 3.1/4.5 缺乏直觉说明）、Wald estimator、column-stochastic matrix 等概念对 NLP 研究者不友好。我在 M1 中也提到 "线性 SEM 对 EMNLP 受众的适用性" 问题。建议在 Section 3.1 开头增加一个 "Intuition" 段落，用 NLP 语境下的具体例子（如 "当 LLM 将某些 neutral tweets 错标为 positive 时，下游情感对投票行为的回归估计会如何偏移"）建立直觉，再引入形式化定义。

---

**[REBUT] R2-W3: 符号反转实际风险可能被高估**

R2 认为 5/7 拓扑 sign reversal 为 0%，因此论文高估了 sign reversal 风险。我认为这一批评误解了论文的 narrative 结构：

1. **论文的核心贡献不是 "sign reversal 很严重"，而是 "sign reversal 的风险是 topology-dependent 的"**。Section 3.2 (p.4-5) 系统分析了每种拓扑的 sign preservation 条件，明确指出 confounding/collider/mediation/M-bias/front-door 在特定条件下 sign 是 preserved 的。这一 taxonomy 本身——告诉实践者哪些拓扑安全、哪些危险——是论文的价值所在。

2. **Exposure 2.1% 虽然比例低但绝非无足轻重**。这 2.1% 对应的是 realistic LLM 精度（diagonal ≥ 0.7）下的 secondary coefficient reversal。在大规模 CSS 研究中（如 Gilardi et al. 2023 的 ChatGPT 标注），数千个回归分析中有 2.1% 产生 sign reversal 意味着可能有数十个结论被误导。

3. **但 R2 的 framing 关切部分成立**。Abstract/Introduction 确实偏向强调 sign reversal 的风险而非 sign preservation 的保证。建议在 Introduction 中增加一句平衡性表述，如 "Our analysis reveals that five of seven topologies provide structural sign protection under realistic annotation quality, while exposure and IV remain vulnerable."

---

**[AGREE] R2-W4: Figure 2 子图过小**

同意。Figure 2 (p.7) 七个子图挤在半页宽度，且红/灰色区分依赖彩色打印。建议将 Figure 2 改为全页宽度，或选择 3-4 个代表性拓扑在主文展示，其余放入 Appendix。

---

**[AGREE] R2-W5: 实验仅基于模拟，缺少真实因果数据集验证**

完全同意。这与我的 N2（must-fix）一致。但关于 R2 建议的 IHDP/LaLonde/ACIC 数据集，我有补充：这些数据集的 treatment 通常是二元变量（如 IHDP 的 treatment/control），不涉及 multi-class annotation。更合适的验证方案是构建一个 NLP-native 的半合成因果数据集——例如在 VAST stance 数据（K=3）上注入已知因果效应，用 LLM 重新标注后对比 "原始估计 vs. LLM 标注估计 vs. ASV 校正估计"。

---

**[AGREE] R2-W6: Correction guidance 定位模糊**

同意。Section 4.5（p.8）确实仅约半页讨论五种校正方法，而 Algorithm 1 放在 Appendix p.31。如果 correction guidance 是论文三大贡献之一（Introduction 第三段），主文需要更充实的讨论：(1) 五种方法的选择标准和适用条件，(2) 计算成本和样本量要求，(3) FWL invariance 对校正可行性的约束（目前在 Appendix B.2 详述但主文仅一段）。建议将 Algorithm 1 或其简化版移入主文。

---

### Minor

**[AGREE] R2-M1**: Table 1 列标题 (Violation/Sign Flip/Amplif./τ_sf=0?) 确实需要脚注定义。特别是 "Violation" 的定义（bias > 某个 threshold？还是任何非零 bias？）和 Sign Flip 与 Violation 的包含关系需明确说明。

**[AGREE] R2-M2**: Notation table (Table 19, Appendix C, p.30) 远离公式定义。建议至少在 Section 3.1 首次引入核心符号时增加简表或内联定义。

**[AGREE] R2-M3**: 如果 Schennach (2020) 在 bib 中但未在正文引用，应在 Related Work (Section 2) 中引用（作为 measurement error 综述文献），或从 bib 中移除。

**[REBUT] R2-M4**: Conjecture 1 (p.6) **已经量化**了 "approximately"——明确写出 "monotonically non-decreasing up to ε < 0.06 deviations"，并指向 "Table 10 in Appendix B.12" 给出 topology-specific worst-case magnitudes。R2 可能是在快速阅读时遗漏了 ε < 0.06 这个 bound。但我同意主文可以补充一句 worst-case 的实际量级（如 "empirically ≤ 0.013 across all tested configurations"），使读者无需翻阅 Appendix 就能判断 approximation 的精度。

**[AGREE] R2-M5**: C₀ 的选取方式（如何从 empirical LLM confusion matrix 设定参考矩阵）确实仅在 Appendix 说明，主文 Section 3.3 Parameterization 部分应至少简述选择原则。

---

### Questions

**[AGREE] R2-Q1**: ASV 的 topology-dependent 特性能否反向推断 DAG 拓扑——这是一个有趣的研究方向。Appendix B.11 Table 9 显示 ASV magnitude 在 confounding/exposure/IV 三种拓扑间是数学上相同的（δ*=0.203），说明 ASV 本身无法区分这三种拓扑。但不同拓扑的 sign-flip ASV 行为差异显著（confounding 永远不 flip，IV 总是 flip）。论文可以在 Discussion 中简短提及此可能性及其局限。

**[AGREE] R2-Q2**: 同意这一关切，与我的 W1 一致。LLM 部署中的 differential misclassification 可能远超论文测试的 ε=0.05 范围——例如当 LLM prompt 包含与 outcome 相关的上下文时（如 few-shot examples 中同时展示了 sentiment label 和 purchase behavior），ε 可能达到 0.1-0.3。Appendix B.6 Table 7-8 的 stress test 覆盖了 ε 到 0.30，但主文讨论不足。

**[AGREE] R2-Q3**: 这是一个重要的点，我在审稿中未充分关注。Appendix B.14（p.28）显示 FWL invariance 在 logistic regression 下失效——exposure bias 从 OLS 的 0% 变为 logistic 的 ~78%。**这意味着对于使用 logistic regression 的 NLP 研究者，matrix-based correction 反而可能有效**——这完全改变了 Section 4.5 的 correction guidance。主文确实缺失此讨论，这是比 R2 标注的 "question" 更严重的问题，应提升为 should-fix。论文应在 Section 4.5 增加一段讨论 "对于 logistic regression 用户，FWL invariance 不成立，matrix-based corrections 变为可行选项"。

**[REBUT] R2-Q4**: K=2 CivilComments 的选择是合理的。论文同时使用了 HumAID（K=10）、VAST（K=3）和 CivilComments（K=2），覆盖了 K=2,3,10 三个层级（Section 4.1, p.7-8）。CivilComments 的 K=2 数据用于验证 Theorem 1（K=2 的解析结果），与 K≥3 的数据互补。论文的贡献不仅是 K≥3——它建立了一个 K≥2 的统一框架，其中 K=2 是 Theorem 1 有解析证明的特殊情形。删除 K=2 验证反而会损失对 Theorem 1 的直接经验支撑。

**[AGREE] R2-Q5**: Table 1（非 Table 2）中 Violation 和 Sign Flip 列的包含关系确实不直观。Sign Flip ⊂ Violation（sign reversal 是 violation 的子集），但 Violation 也包括 non-sign-reversing bias（如 amplification、attenuation）。建议在 Table 1 脚注中明确："Violation = any bias-direction deviation from ground truth; Sign Flip = sign(estimate) ≠ sign(true effect); Sign Flip ⊆ Violation"。

---

### Missing References

**[AGREE] R2-R1**: Miles, Valeri, and Coull (2024) "Measurement Error-Robust Causal Inference via Constructed Instrumental Variables" 与论文的 IV 拓扑分析直接相关——提出了一种在存在 measurement error 时构造 instrumental variables 的方法。应在 Related Work Section 2 (Sensitivity analysis and correction methods) 中引用。

**[AGREE] R2-R2**: Wei et al. (2025) "Multiply robust causal inference in the presence of an error-prone treatment" 与论文的 exposure 拓扑分析直接相关。论文的 correction guidance (Section 4.5) 讨论了 exposure 校正但未引用此 multiply robust 方法。

**[AGREE] R2-R3**: Schennach (2020) 应在正文 Related Work 中引用，或从 bib 中移除。

**[REBUT] R2-R4**: Manski (1990) bounds approach **已在正文引用**——Section 4.2 (p.7) 在 IV 讨论中写道 "practitioners may consider bounds approaches (Manski, 1990), robust IV methods, or two-sample designs"。R2 可能是建议在 Related Work (Section 2) 中更系统地讨论 Manski 的 partial identification approach 与论文的 point estimation approach 的关系——这一建议有道理，但 Manski 并未被遗漏。

---

### 总结

R2 的审稿意见整体有建设性，与我的多个关切一致（abstract 密度、EMNLP 可及性、缺少真实数据验证、correction guidance 篇幅不足）。主要分歧在两点：

1. **ASV vs. E-value (N1)**：R2 认为 ASV 仅为 reparametrization，我认为 topology-dependence 和 sign-flip ASV 是结构性创新。但同意论文可以更好地 articulate 技术新颖性。建议降级为 should-fix。

2. **Sign reversal 风险高估 (W3)**：R2 认为风险被高估，我认为论文的价值恰在于给出 topology-dependent risk taxonomy，而非声称 sign reversal 普遍严重。但同意 abstract/intro framing 可以更平衡。

3. **R2-Q3（FWL under logistic regression）是一个我初审遗漏的重要问题**：Appendix B.14 的 logistic 结果对 Section 4.5 correction guidance 有重要含义，主文缺失此讨论。建议提升为 should-fix。

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

_source line 1314 · 2026-05-23T12:39:24.970917+00:00_

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

_source line 1315 · 2026-05-23T12:39:25.022042+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T12:22:38.541780+00:00\", \"completed_at\": \"2026-05-23T12:22:42.223316+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-23T12:39:25.022492+00:00_

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

_source line 1317 · 2026-05-23T12:39:25.022738+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1318 · 2026-05-23T12:39:33.357327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib--claude-sessions-review-director-d2e6d7be/051a1642-45de-4f89-9cec-976a354b9de5/tool-results/bigjmw1w8.txt",
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
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib--claude-sessions-review-director-d2e6d7be/051a1642-45de-4f89-9cec-976a354b9de5/tool-results/bigjmw1w8.txt",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1319 · 2026-05-23T12:39:33.408284+00:00_

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
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-23T12:43:31.849472+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 16\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 R1-M2 再提为 minor：23 配置覆盖 3 类任务（7B-235B），缺 NER/QA/discourse 等。R2 同意但认为考虑获取成本可接受。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor：stress test 合成但已有三层验证。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。主文仅一句话讨论此假设，Appendix B.6 stress test 未被主文充分引用。两位共识 should-fix：需增加何时成立/失败/检验的讨论。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 should-fix（高优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W1 再提，R1 交叉 AGREE。Abstract 188 词覆盖 7 拓扑+多项数值结果，建议精简到 3-4 核心信息点，移除具体百分比。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。建议扩展 Appendix B.18 政治广告案例。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-N2 列为 must-fix（缺第三层端到端验证：C估计→ASV诊断→校正→改善估计），R2 AGREE 但认为 rebuttal 周期内工作量偏大，至少应在 Limitations 明确承认。Director 采纳 must-fix 但接受 Limitations 承认作为最低修复。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 Remark 1 三点对比不够充分。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N1 列为 must-fix（ASV 仅为 E-value reparametrization）。R1 交叉 REBUT：topology-dependence 和 sign-flip ASV 是结构性创新，非简单参数替换，建议降为 should-fix。Director 采纳 R1 判断降为 should-fix：论文确有创新但需更好 articulate 技术新颖性（Birkhoff polytope vs [1,∞) 半线几何差异）。\"\n    action_items:\n      - round: 14\n        action: \"正文增加 Remark 形式化说明 ASV 与 E-value 的数学结构区别\"\n        assigned_to: agent\n        status: done\n      - round: 16\n        action: \"Remark 1 增加技术挑战来源说明（confusion matrix Birkhoff polytope 几何 vs E-value relative risk 半线），强化 topology-dependence 和 sign-flip 的方法论独立性\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 降为 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（minor-to-should-fix）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W2 再提：treatment effect 是待估计未知量，无法先验验证成比例性。Appendix B.13 Table 12 independent effects 下 sign failure 23%。R2 AGREE。共识 should-fix：需讨论 testable implications 和哪类 NLP 任务可能满足。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 15\n    resolution: \"与 R4-W6 合并。Remark 1 + Table 18 已添加。\"\n    resolution_round: 15\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性 / 均匀退化假设\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1]\n        note: \"R15 should-fix（低优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W3 再提：C(δ) 假设均匀退化，与 LLM 稀有类别先崩溃的实际模式不符。R2 AGREE 但认为影响程度较低（empirical LLM 矩阵本身包含 class-imbalanced 退化，ASV ranking 仍稳定）。共识 should-fix：增加 class-frequency-weighted degradation path 实验。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"Algorithm 1 整体被赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8+ ===\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem 1 仅 K=2，Conjecture 1 缺理论证明\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 两位均列为 critical。210K 矩阵验证无法排除 corner case。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-N1 列为 critical：(1) Dirichlet 采样在高维空间覆盖率极低；(2) Table 10 显示 60-97% 矩阵违反 exact monotonicity（magnitude ≤ 0.013）；(3) 论文标题聚焦 Multi-Class 但核心结论仅为 conjecture。R2 交叉 AGREE 并补充：违反幅度 0.013 是否足以保证 ASV ranking 稳定性？论文未给出 ranking 翻转的 threshold 分析。两位共识 critical：论文最大理论缺口。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R6-M3 合并。共识 should-fix。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 与 R4-W6 合并。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R4-W6 合并。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 NEW-1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 NEW-1。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。连续三轮未被 Reviewer 提出。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R6-M3 和 NEW-1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 R6-M3 和 NEW-1。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（加两个词）。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 R1-M1 降为 minor：建议主文引用 Appendix B.7/B.14 结果。R2 AGREE。\"\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R8-C1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 R8-C1。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R1 REBUT 成功。Introduction 措辞准确。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N2 再提为 must-fix：需与 Carroll et al. (2006) 显式区分。R1 交叉 AGREE。Director 采纳 should-fix：建议限定为 'first unified analysis for LLM-generated multi-class annotations across seven topologies'。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R1-W3。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 合并到 R1-W3。R1-M2 minor。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study 应在正文提及\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 15\n    resolution: \"Section 4.5 已引用 ClinicalBERT。连续三轮未被提出。\"\n    resolution_round: 15\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（高优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W2 再提：plim/FWL/Wald/column-stochastic/Dirichlet 五个核心概念解释不足。R1 交叉 AGREE，建议 Section 3.1 增加 Intuition 段落用 NLP 例子建立直觉。共识 should-fix（高优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"K=3/5/10 × 7 topologies 完成。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"Section 4.2 已添加替代方案。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"已添加。\"\n    resolution_round: 13\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文溢出至 p9\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"已压缩。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 与 R11-W2 合并。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R11-W2 合并。\"\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: should-fix\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出，但 R1-W2 的 proportional effects 讨论隐含覆盖。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 minor。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W4 再提，R1 交叉 AGREE。七子图挤在半页，红灰颜色依赖彩色打印。共识 should-fix：使用 hatching pattern 或拆分 figure。\"\n\n  # === Round 13 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract/Section 4.2/Appendix B.4 之间 factual 不一致\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"三处统一。\"\n    resolution_round: 14\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑缺少 NLP 应用场景示例\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: \"已添加。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 缺失引用\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: \"已在 references.bib 和 Related Work 中引用。\"\n    resolution_round: 15\n\n  - id: R13-CRIT1\n    category: soundness\n    severity: critical\n    summary: \"Limitations 中 diagonal accuracy 范围错误\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"0.45-0.81 与实际数据一致。\"\n    resolution_round: 14\n\n  # === Round 14 ===\n\n  - id: R14-W1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 Yes/Yes*/No 标注不直观\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"已改为 Cond./Yes/No。\"\n    resolution_round: 15\n\n  - id: R14-W2\n    category: method\n    severity: should-fix\n    summary: \"IV 拓扑 maximally fragile 后缺少积极替代方案\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: \"Section 4.2 已添加三种替代方案。\"\n    resolution_round: 15\n\n  - id: R14-W3\n    category: presentation\n    severity: should-fix\n    summary: \"混淆矩阵 C 的可获得性假设\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 15\n\n  # === Round 15 ===\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case < 0.005 与 Table 10 不一致（confounding 0.011, front-door 0.013）\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"需修正 Observation 1 数值。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。Conjecture 1 ε < 0.06 bound 被 R1-M3 认为保守（实际 ≤ 0.013），但未单独检查 Observation 1 与 Table 10 一致性。\"\n    action_items:\n      - round: 15\n        action: \"修正 Observation 1 数值\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"需在 caption 中精确定义。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-M1 + R1 交叉 AGREE。应明确 Sign Flip ⊆ Violation，脚注定义各列含义。\"\n    action_items:\n      - round: 15\n        action: \"Table 1 caption 增加列定义\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"修复成本极低（加两个词）。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。但 R1 交叉回应 R2-Q3 时发现 Appendix B.14 logistic 结果对 Section 4.5 有重要含义，提升为 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W3\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 经验阈值缺乏理论依据和 DGP 敏感性讨论\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"should-fix。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n\n  # === Round 16 新发现 ===\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？Abstract 表述易误解\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R1-W4 + R2-W3 共识。Abstract 'sign reversal occurs in 2.1% of exposure configurations' 易被理解为 primary treatment effect reversal，实际仅为 secondary coefficient。Table 1 的 Sign Flip 列为 0%（primary）vs 2.1%（secondary）差异需脚注说明。\"\n    action_items:\n      - round: 16\n        action: \"Abstract 改为 'secondary-coefficient sign reversal'；Table 1 增加脚注明确 Sign Flip 列指 primary coefficient\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R2-W6 提出，R1 交叉 AGREE。五种方法选择标准未说明，缺计算成本讨论，FWL invariance 验证仅在 Appendix B.2。建议将 Algorithm 1 简化版移入主文。\"\n    action_items:\n      - round: 16\n        action: \"Section 4.5 扩充：方法选择标准、FWL invariance 对校正可行性的约束、Algorithm 1 简化版入正文\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N3\n    category: scope\n    severity: should-fix\n    summary: \"FWL invariance 在 logistic regression 下失效的含义未在主文讨论\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R2-Q3 提出，R1 交叉回应提升为 should-fix。Appendix B.14 显示 logistic 下 exposure bias ~78%，FWL invariance 不成立意味着 matrix-based correction 在 logistic 下可能有效——完全改变 Section 4.5 的 correction guidance。主文应增加此讨论。\"\n    action_items:\n      - round: 16\n        action: \"Section 4.5 增加 logistic regression 下 FWL 失效的讨论，说明 matrix-based corrections 在非线性模型下可能有效\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N4\n    category: novelty\n    severity: should-fix\n    summary: \"'First unified analysis' claim 需与 Carroll et al. (2006) 和 Schennach (2020) 显式区分\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R2-N2 提出为 must-fix，R1 交叉 AGREE。Director 采纳 should-fix：限定为 'first unified analysis for LLM-generated multi-class annotations across seven topologies'。\"\n    action_items:\n      - round: 16\n        action: \"Introduction 限定 novelty claim，与 Carroll et al. (2006) / Schennach (2020) 做显式区分\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N5\n    category: presentation\n    severity: minor\n    summary: \"Notation table (Table 19) 放在 Appendix C，主文符号引导分散\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R2-M2 提出，R1 AGREE。Section 3.1 应至少简表或内联定义核心符号。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N6\n    category: presentation\n    severity: minor\n    summary: \"τ vs β_T 含义在 mediator/front-door 拓扑下不清晰（total vs direct effect）\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1]\n        note: \"R1-M4 提出，R2 AGREE。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用：Miles et al. (2024), Wei et al. (2025), Hernán & Robins (2020), Schennach (2020) 正文引用\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"Miles et al. (2024) measurement error-robust CI via constructed IV：R2 提出 R1 AGREE。Wei et al. (2025) multiply robust CI with error-prone treatment：R2 提出 R1 AGREE。Hernán & Robins (2020) Causal Inference What If：R1 提出 R2 AGREE。Schennach (2020) 已在 bib 未在正文引用：R2 提出 R1 AGREE。\"\n    resolution: \"\"\n    resolution_round: null"
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
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 16\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 R1-M2 再提为 minor：23 配置覆盖 3 类任务（7B-235B），缺 NER/QA/discourse 等。R2 同意但认为考虑获取成本可接受。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor：stress test 合成但已有三层验证。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。主文仅一句话讨论此假设，Appendix B.6 stress test 未被主文充分引用。两位共识 should-fix：需增加何时成立/失败/检验的讨论。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 should-fix（高优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W1 再提，R1 交叉 AGREE。Abstract 188 词覆盖 7 拓扑+多项数值结果，建议精简到 3-4 核心信息点，移除具体百分比。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。建议扩展 Appendix B.18 政治广告案例。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-N2 列为 must-fix（缺第三层端到端验证：C估计→ASV诊断→校正→改善估计），R2 AGREE 但认为 rebuttal 周期内工作量偏大，至少应在 Limitations 明确承认。Director 采纳 must-fix 但接受 Limitations 承认作为最低修复。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 Remark 1 三点对比不够充分。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N1 列为 must-fix（ASV 仅为 E-value reparametrization）。R1 交叉 REBUT：topology-dependence 和 sign-flip ASV 是结构性创新，非简单参数替换，建议降为 should-fix。Director 采纳 R1 判断降为 should-fix：论文确有创新但需更好 articulate 技术新颖性（Birkhoff polytope vs [1,∞) 半线几何差异）。\"\n    action_items:\n      - round: 14\n        action: \"正文增加 Remark 形式化说明 ASV 与 E-value 的数学结构区别\"\n        assigned_to: agent\n        status: done\n      - round: 16\n        action: \"Remark 1 增加技术挑战来源说明（confusion matrix Birkhoff polytope 几何 vs E-value relative risk 半线），强化 topology-dependence 和 sign-flip 的方法论独立性\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 降为 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（minor-to-should-fix）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W2 再提：treatment effect 是待估计未知量，无法先验验证成比例性。Appendix B.13 Table 12 independent effects 下 sign failure 23%。R2 AGREE。共识 should-fix：需讨论 testable implications 和哪类 NLP 任务可能满足。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 15\n    resolution: \"与 R4-W6 合并。Remark 1 + Table 18 已添加。\"\n    resolution_round: 15\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性 / 均匀退化假设\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1]\n        note: \"R15 should-fix（低优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W3 再提：C(δ) 假设均匀退化，与 LLM 稀有类别先崩溃的实际模式不符。R2 AGREE 但认为影响程度较低（empirical LLM 矩阵本身包含 class-imbalanced 退化，ASV ranking 仍稳定）。共识 should-fix：增加 class-frequency-weighted degradation path 实验。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"Algorithm 1 整体被赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8+ ===\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem 1 仅 K=2，Conjecture 1 缺理论证明\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 两位均列为 critical。210K 矩阵验证无法排除 corner case。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-N1 列为 critical：(1) Dirichlet 采样在高维空间覆盖率极低；(2) Table 10 显示 60-97% 矩阵违反 exact monotonicity（magnitude ≤ 0.013）；(3) 论文标题聚焦 Multi-Class 但核心结论仅为 conjecture。R2 交叉 AGREE 并补充：违反幅度 0.013 是否足以保证 ASV ranking 稳定性？论文未给出 ranking 翻转的 threshold 分析。两位共识 critical：论文最大理论缺口。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R6-M3 合并。共识 should-fix。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 与 R4-W6 合并。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R4-W6 合并。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 NEW-1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 NEW-1。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。连续三轮未被 Reviewer 提出。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R6-M3 和 NEW-1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 R6-M3 和 NEW-1。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（加两个词）。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 R1-M1 降为 minor：建议主文引用 Appendix B.7/B.14 结果。R2 AGREE。\"\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R8-C1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 R8-C1。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R1 REBUT 成功。Introduction 措辞准确。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N2 再提为 must-fix：需与 Carroll et al. (2006) 显式区分。R1 交叉 AGREE。Director 采纳 should-fix：建议限定为 'first unified analysis for LLM-generated multi-class annotations across seven topologies'。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R1-W3。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 合并到 R1-W3。R1-M2 minor。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study 应在正文提及\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 15\n    resolution: \"Section 4.5 已引用 ClinicalBERT。连续三轮未被提出。\"\n    resolution_round: 15\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（高优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W2 再提：plim/FWL/Wald/column-stochastic/Dirichlet 五个核心概念解释不足。R1 交叉 AGREE，建议 Section 3.1 增加 Intuition 段落用 NLP 例子建立直觉。共识 should-fix（高优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"K=3/5/10 × 7 topologies 完成。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"Section 4.2 已添加替代方案。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"已添加。\"\n    resolution_round: 13\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文溢出至 p9\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"已压缩。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 与 R11-W2 合并。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R11-W2 合并。\"\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: should-fix\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出，但 R1-W2 的 proportional effects 讨论隐含覆盖。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 minor。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W4 再提，R1 交叉 AGREE。七子图挤在半页，红灰颜色依赖彩色打印。共识 should-fix：使用 hatching pattern 或拆分 figure。\"\n\n  # === Round 13 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract/Section 4.2/Appendix B.4 之间 factual 不一致\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"三处统一。\"\n    resolution_round: 14\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑缺少 NLP 应用场景示例\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: \"已添加。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 缺失引用\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: \"已在 references.bib 和 Related Work 中引用。\"\n    resolution_round: 15\n\n  - id: R13-CRIT1\n    category: soundness\n    severity: critical\n    summary: \"Limitations 中 diagonal accuracy 范围错误\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"0.45-0.81 与实际数据一致。\"\n    resolution_round: 14\n\n  # === Round 14 ===\n\n  - id: R14-W1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 Yes/Yes*/No 标注不直观\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"已改为 Cond./Yes/No。\"\n    resolution_round: 15\n\n  - id: R14-W2\n    category: method\n    severity: should-fix\n    summary: \"IV 拓扑 maximally fragile 后缺少积极替代方案\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: \"Section 4.2 已添加三种替代方案。\"\n    resolution_round: 15\n\n  - id: R14-W3\n    category: presentation\n    severity: should-fix\n    summary: \"混淆矩阵 C 的可获得性假设\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 15\n\n  # === Round 15 ===\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case < 0.005 与 Table 10 不一致（confounding 0.011, front-door 0.013）\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"需修正 Observation 1 数值。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。Conjecture 1 ε < 0.06 bound 被 R1-M3 认为保守（实际 ≤ 0.013），但未单独检查 Observation 1 与 Table 10 一致性。\"\n    action_items:\n      - round: 15\n        action: \"修正 Observation 1 数值\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"需在 caption 中精确定义。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-M1 + R1 交叉 AGREE。应明确 Sign Flip ⊆ Violation，脚注定义各列含义。\"\n    action_items:\n      - round: 15\n        action: \"Table 1 caption 增加列定义\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"修复成本极低（加两个词）。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。但 R1 交叉回应 R2-Q3 时发现 Appendix B.14 logistic 结果对 Section 4.5 有重要含义，提升为 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W3\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 经验阈值缺乏理论依据和 DGP 敏感性讨论\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"should-fix。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n\n  # === Round 16 新发现 ===\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？Abstract 表述易误解\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R1-W4 + R2-W3 共识。Abstract 'sign reversal occurs in 2.1% of exposure configurations' 易被理解为 primary treatment effect reversal，实际仅为 secondary coefficient。Table 1 的 Sign Flip 列为 0%（primary）vs 2.1%（secondary）差异需脚注说明。\"\n    action_items:\n      - round: 16\n        action: \"Abstract 改为 'secondary-coefficient sign reversal'；Table 1 增加脚注明确 Sign Flip 列指 primary coefficient\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R2-W6 提出，R1 交叉 AGREE。五种方法选择标准未说明，缺计算成本讨论，FWL invariance 验证仅在 Appendix B.2。建议将 Algorithm 1 简化版移入主文。\"\n    action_items:\n      - round: 16\n        action: \"Section 4.5 扩充：方法选择标准、FWL invariance 对校正可行性的约束、Algorithm 1 简化版入正文\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N3\n    category: scope\n    severity: should-fix\n    summary: \"FWL invariance 在 logistic regression 下失效的含义未在主文讨论\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R2-Q3 提出，R1 交叉回应提升为 should-fix。Appendix B.14 显示 logistic 下 exposure bias ~78%，FWL invariance 不成立意味着 matrix-based correction 在 logistic 下可能有效——完全改变 Section 4.5 的 correction guidance。主文应增加此讨论。\"\n    action_items:\n      - round: 16\n        action: \"Section 4.5 增加 logistic regression 下 FWL 失效的讨论，说明 matrix-based corrections 在非线性模型下可能有效\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N4\n    category: novelty\n    severity: should-fix\n    summary: \"'First unified analysis' claim 需与 Carroll et al. (2006) 和 Schennach (2020) 显式区分\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R2-N2 提出为 must-fix，R1 交叉 AGREE。Director 采纳 should-fix：限定为 'first unified analysis for LLM-generated multi-class annotations across seven topologies'。\"\n    action_items:\n      - round: 16\n        action: \"Introduction 限定 novelty claim，与 Carroll et al. (2006) / Schennach (2020) 做显式区分\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N5\n    category: presentation\n    severity: minor\n    summary: \"Notation table (Table 19) 放在 Appendix C，主文符号引导分散\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R2-M2 提出，R1 AGREE。Section 3.1 应至少简表或内联定义核心符号。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N6\n    category: presentation\n    severity: minor\n    summary: \"τ vs β_T 含义在 mediator/front-door 拓扑下不清晰（total vs direct effect）\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1]\n        note: \"R1-M4 提出，R2 AGREE。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用：Miles et al. (2024), Wei et al. (2025), Hernán & Robins (2020), Schennach (2020) 正文引用\"\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"Miles et al. (2024) measurement error-robust CI via constructed IV：R2 提出 R1 AGREE。Wei et al. (2025) multiply robust CI with error-prone treatment：R2 提出 R1 AGREE。Hernán & Robins (2020) Causal Inference What If：R1 提出 R2 AGREE。Schennach (2020) 已在 bib 未在正文引用：R2 提出 R1 AGREE。\"\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-23T12:43:32.003312+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 32226}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-23T12:46:30.748159+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# 审稿报告：Multi-Class Annotation Errors in Causal Inference\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 16 (Fresh)\n**Reviewer 编排**: 2 人（R1 方法严谨性, R2 新颖性/完整性）\n**收敛状态**: 1 轮独立审稿 + 1 轮交叉分享后收敛\n\n---\n\n## Summary\n\n本文系统分析了 K-class（K≥3）LLM 标注误差在七种因果 DAG 拓扑下的传播机制。核心贡献包括：(1) 推导每种拓扑的闭式 bias 表达式并建立 sign preservation taxonomy（confounding/collider 证明 sign preserved, exposure/IV 可反转）；(2) 提出 Annotation Sensitivity Values (ASVs) 诊断框架，包含 magnitude/significance/sign-flip 三个维度；(3) 基于 FWL 不变性证明矩阵校正方法在四种协变量拓扑下无效，并给出拓扑感知校正指南。实验涵盖 Monte Carlo 模拟（161 场景 MAPE 1.6%）、23 组真实 LLM 混淆矩阵验证和五种校正方法的系统比较。\n\n---\n\n## Strengths\n\n**S1. 填补重要文献空白。** 首次在 K≥3 条件下统一分析七种标准 DAG 拓扑的标注误差传播。Brenner (1993) 仅处理二值混杂，TeBlunthuis et al. (2024) 覆盖二值四种拓扑，Lee & Wood-Doughty (2024) 仅 confounding。这一系统性本身是真正的贡献。[R1 S1, R2 S1 共识]\n\n**S2. FWL 不变性结果具有高实用价值。** Section 4.5 + Appendix B.2 证明 matrix-based corrections（Naïve plug-in, MLA）在线性 OLS 下对四种协变量拓扑无效。这个非平凡的负面贡献（impossibility result）对实践者有直接指导意义，避免了无效校正尝试。[R1 S3, R2 S2 共识]\n\n**S3. 理论-实验三层证据结构设计良好。** 每个理论 claim 都有解析证明（K=2）+ 数值验证（K≥3, 100K-210K 矩阵）+ 真实 LLM 混淆矩阵验证的三层支撑。[R1 S1, R2 S3 共识]\n\n**S4. Sign preservation taxonomy 优雅且实用。** Proposition 1 将七种拓扑清晰分为 sign-preserving（confounding/collider, 解析证明）、conditionally preserving（mediation/M-bias/front-door）和 sign-vulnerable（exposure/IV），为实践者提供直接可用的风险评估维度。[R1 S2]\n\n**S5. Algorithm 1 降低理论到实践的转化门槛。** 校正决策树覆盖风险评估、方法选择和 FWL 检查三步流程，具有工具价值。[R1 S5, R2 S4 共识]\n\n**S6. Appendix 极其详尽。** 22 页 19 个 subsection 覆盖了几乎所有可预见的 reviewer 质疑点（非微分 stress test、非线性 DGP、ClinicalBERT 案例、校正方法敏感性等），体现严谨研究态度。[R1 S6, R2 S5 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical] K≥3 envelope monotonicity 仅为 Conjecture，与 \"Multi-Class\" 标题和核心 narrative 不匹配**\n- 位置：Section 3.3 Theorem 1, Conjecture 1 (p.6), Table 10 (p.27)\n- Theorem 1（envelope monotonicity）仅对 K=2 有解析证明。K≥3 为 Conjecture 1（ε-approximate, ε < 0.06），依赖 210,000 矩阵数值验证。\n- 问题：(1) Dirichlet 均匀采样在高维空间覆盖率极低（K=7 时 42 自由度），210K 样本可能遗漏 adversarial corner cases；(2) Table 10 显示 60-97% 矩阵存在 exact monotonicity 违反（magnitude ≤ 0.013），说明 exact monotonicity 在 K≥3 下**系统性不成立**；(3) 论文未分析 \"多大的违反会导致 ASV ranking 翻转\"——0.013 的 bound 是否足以保证实用稳定性？\n- 论文标题聚焦 \"Multi-Class\" 但核心结论在 K≥3 下仅为经验观察，ASV 框架的理论基础不完整。\n- **建议**：(a) Abstract/Introduction 精确区分 \"K=2 proven\" vs \"K≥3 conjectured with numerical support\"；(b) 增加采样量到 10⁶ 并报告违反分布的尾部行为；(c) 分析 ε=0.013 下 ASV ranking 翻转的条件。\n- **共识**：R1 N1 提出, R2 交叉 AGREE 并补充 ranking 稳定性分析缺失。两位均评为 critical。\n\n**W2 [critical] 缺乏真实因果数据的端到端验证——实验仅验证公式正确性和 confusion matrix 属性**\n- 位置：Section 4 整体, Appendix B.3\n- 验证三层中缺第三层：Layer 1（解析 vs MC, MAPE 1.6%）验证数学正确性 ✓；Layer 2（23 LLM 配置性质）验证输入端行为 ✓；**Layer 3 缺失**：在已知 ground-truth 因果效应的数据上完整演示 \"估计 C → ASV 诊断 → 选择校正 → 改善估计\" 的端到端流程。\n- ClinicalBERT case study (Appendix B.3) 的 ground truth 来自 OLS on gold labels，不是真正已知因果效应。\n- **建议**：构建 NLP-native 半合成因果数据集（如 VAST stance K=3 + 注入已知因果效应 + LLM 重标注），对比无校正 vs ASV 校正的估计精度。或至少在 Limitations 明确承认此缺失（目前未提及）。\n- **共识**：R1 N2 提出, R2 W5 独立提出, 交叉 AGREE。两位一致。R2 补充 rebuttal 周期内完整验证工作量偏大，接受 Limitations 承认作为最低修复。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3. Non-differential misclassification 假设主文讨论不足**\n- 位置：Definition 1 (Section 3.1, p.4)\n- 主文仅一句 \"This holds when the LLM classifies without observing the outcome\"。需增加何时成立（LLM 未观察 outcome）、何时失败（prompt 含 outcome-correlated context）、如何检验的讨论，并引用 Appendix B.6 stress test 结果。\n- **共识**：R1 W1 提出, R2 AGREE。\n\n**W4. Proportional effects 假设 (f = λg) 缺乏实践验证指导**\n- 位置：Theorem 1 (p.6), Appendix B.13 Table 12\n- Treatment effect 是待估计未知量，无法先验验证成比例性。Independent effects 下 sign failure rate 达 23%——直接削弱 \"confounding preserves sign\" 的适用范围。需讨论 testable implications 和哪类 NLP 任务可能满足。\n- **共识**：R1 W2 提出, R2 AGREE。\n\n**W5. ASV 创新性阐述需加强（降级自 R2 must-fix）**\n- 位置：Section 3.3 (p.5-6), Remark 1\n- R2 认为 ASV 仅为 E-value 的 reparametrization（must-fix）。R1 REBUT：topology-dependence（同一 C 在不同拓扑下 ASV 不同）和 sign-flip ASV（E-value 无对应物）是结构性创新。Confusion matrix 的 Birkhoff polytope 参数空间 vs E-value 的 [1,∞) 半线有本质几何差异。\n- **Director 判定**：降为 should-fix。ASV 有真实创新但论文未充分 articulate 技术挑战的新颖性。Remark 1 需强化技术区别的深度。\n- **分歧记录**：R2 维持 must-fix, R1 认为 should-fix。\n\n**W6. Abstract 信息密度过高**\n- 188 词覆盖 7 拓扑 + sign reversal + ASV + monotonicity + correction + FWL。建议精简到 3-4 核心信息点，移除具体百分比（2.1%, 52.6%）到正文。\n- **共识**：R2 W1 提出, R1 AGREE。\n\n**W7. EMNLP 受众可及性不足——核心术语解释薄弱**\n- plim（仅脚注）、FWL theorem（无直觉解释）、Wald estimator、column-stochastic matrix、Dirichlet prior 均缺乏 NLP 语境下的直觉说明。建议 Section 3.1 增加 Intuition 段落用具体 NLP 例子建立直觉。\n- **共识**：R2 W2 提出, R1 AGREE。高优先级。\n\n**W8. \"2.1% sign reversal\" 限定不清晰——secondary vs primary coefficient**\n- Abstract \"sign reversal occurs in 2.1% of exposure configurations\" 易误解为 primary treatment effect reversal，实际为 secondary coefficient（小效应量）。Table 1 Sign Flip 列为 0%（primary）。需在 Abstract 明确 \"secondary-coefficient\" 并在 Table 1 增加脚注。\n- **共识**：R1 W4 提出, R2 W3 独立提出, 交叉 AGREE。\n\n**W9. Correction guidance 作为三大贡献之一深度不足**\n- Section 4.5 仅半页，五种方法选择标准未说明，缺计算成本讨论，Algorithm 1 放在 Appendix p.31。建议充实 Section 4.5 并将 Algorithm 1 简化版移入主文。\n- **共识**：R2 W6 提出, R1 AGREE。\n\n**W10. FWL invariance 在 logistic regression 下失效的含义未在主文讨论**\n- Appendix B.14 显示 FWL invariance 在 logistic regression 下不成立（exposure bias ~78%）。这意味着对使用 logistic regression 的 NLP 研究者，matrix-based corrections 可能有效——完全改变 Section 4.5 的 correction guidance。主文应增加此讨论。\n- **来源**：R2 Q3 提出, R1 交叉回应提升为 should-fix。\n\n**W11. ASV C(δ) 均匀退化假设与 LLM 实际误差模式不符**\n- C(δ) = (1−δ)I + δC₀ 假设所有类别以相同速率退化，但 LLM 中稀有类别通常先出错。需增加 class-frequency-weighted degradation path 稳健性实验。\n- **共识**：R1 W3 提出, R2 AGREE（但认为影响程度偏低，因 empirical LLM 矩阵本身包含不均匀退化且 ASV ranking 仍稳定）。\n\n**W12. \"First unified analysis\" novelty claim 需与经典文献区分**\n- 需与 Carroll et al. (2006) Ch.15 和 Schennach (2020) 做显式区分。建议限定为 \"first unified analysis for LLM-generated multi-class annotations across seven topologies\"。\n- **共识**：R2 N2 提出为 must-fix, R1 AGREE。Director 采纳 should-fix（限定修辞即可解决）。\n\n**W13. Figure 2 子图过小，灰度打印无法区分**\n- 七个子图挤在半页宽度，红/灰颜色区分依赖彩色打印。建议使用 hatching pattern 或拆分 figure。\n- **共识**：R2 W4 提出, R1 AGREE。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n\n1. K≥3 monotonicity 仅为 conjecture 是论文最大理论缺口\n2. 缺乏端到端真实因果数据验证\n3. Abstract 信息过载需精简\n4. EMNLP 受众可及性需提升（术语解释）\n5. \"2.1% sign reversal\" 限定不清（secondary coefficient）\n6. Non-differential 假设主文讨论不足\n7. Proportional effects 假设缺乏验证指导\n8. Correction guidance 深度不足\n9. Figure 2 视觉质量\n10. Table 1 列定义需明确\n11. FWL under logistic regression 主文缺讨论\n\n---\n\n## Reviewer Divergence\n\n**D1. ASV vs E-value 创新性（R2: must-fix → Director: should-fix）**\n- R2 认为 ASV 仅为 E-value reparametrization，核心逻辑均为 \"minimum perturbation to nullify effect\"。\n- R1 REBUT：topology-dependence 和 sign-flip ASV 是 E-value 不具备的结构性创新。Confusion matrix 参数空间（Birkhoff polytope）与 relative risk 空间（[1,∞) 半线）有本质几何差异。\n- **Director 采纳 R1**：ASV 有真实方法论创新，但论文需更好 articulate 技术新颖性。降为 should-fix。\n\n**D2. Sign reversal 风险是否被高估（R2: should-fix vs R1: REBUT）**\n- R2 认为 5/7 拓扑 sign reversal 为 0%，framing 暗示风险普遍严重。\n- R1 REBUT：论文价值在于 topology-dependent risk taxonomy，不在于声称 sign reversal 普遍——告诉实践者哪些拓扑安全、哪些危险本身就是贡献。但同意 Abstract/Introduction framing 可更平衡。\n- **Director 判定**：R1 论证更有说服力——taxonomy 是核心价值。但同意 framing 需平衡，作为 W8 的一部分处理。\n\n**D3. IV 52.6% vs 0% gap 解释充分性（R1: should-fix vs R2: REBUT）**\n- R1 认为需要比 \"structural properties\" 更具体的解释。\n- R2 REBUT：Appendix B.10 已解释 Dirichlet 产生极端矩阵、LLM diagonal dominant、IV sign reversal 需 first-stage 符号翻转（真实 LLM 不太可能），但同意主文可增加 1-2 句直觉解释。\n- **Director 判定**：R2 REBUT 有效——Appendix 已有合理解释。采纳 R2 建议在主文增加直觉说明即可，不额外列为 weakness。\n\n**D4. Veitch et al. (2020) 引用必要性（R1: AGREE vs R2: REBUT）**\n- R1 认为应引用。R2 REBUT：该工作处理 text-as-treatment 的连续表示学习，与本文离散多类别 measurement error 主题关联较弱。已引用的 Feder et al. (2022) 和 Pryzant et al. (2021) 覆盖了 text-based causal inference。\n- **Director 判定**：R2 REBUT 有效。不列为缺失引用。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Conjecture 1 在 non-proportional effects 下是否可能完全失败（而非 ε-approximate 违反）？Table 12 的 23% sign failure rate 与 monotonicity failure 的关系是什么？\n\n**Q2.** 23 个 LLM confusion matrices 在 IV 拓扑下全部 0% sign reversal——具体哪些结构属性（diagonal dominance? off-diagonal 对称性? eigenvalue 分布?）阻止了 sign reversal？能否构造 realistic-looking 的矩阵使 IV sign reversal 发生？\n\n**Q3.** Class-imbalanced 场景（如 K=10 中 rare class 占 5%）下 ASV ranking 是否仍可靠？C(δ) 的均匀退化与实际不均匀退化的差异会否改变 topology vulnerability ranking？\n\n**Q4.** Non-differential 假设失败时（ε > 0.10），ASV topology vulnerability ranking（IV > Exposure > ... > M-bias）是否仍保持？Appendix B.6 覆盖了弱违反但未报告 ranking 稳定性。\n\n**Q5.** ASV 的 topology-dependent 特性能否反向推断 DAG 拓扑？Appendix B.11 Table 9 暗示某些维度可区分拓扑（sign-flip behavior），但 magnitude ASV 跨拓扑可能相同——这个方向的可行性和局限性是什么？\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 交叉确认为应引用：\n\n1. **Miles, Valeri, and Coull (2024)**. \"Measurement Error-Robust Causal Inference via Constructed Instrumental Variables.\" arXiv:2406.00940. — 与 IV 拓扑分析直接相关。[R2 提出, R1 AGREE]\n2. **Wei, He, Li, and Geng (2025)**. \"Multiply robust causal inference in the presence of an error-prone treatment.\" Statistical Methods in Medical Research. — 与 exposure 拓扑分析直接相关。[R2 提出, R1 AGREE]\n3. **Hernán MA, Robins JM (2020)**. \"Causal Inference: What If.\" Chapman & Hall/CRC. Chapter 9 关于 measurement error 对 identification 的影响。— 因果推断标准教材。[R1 提出, R2 AGREE]\n4. **Schennach (2020)**. 已在 bib 中但未在正文引用。应在 Related Work 引用或从 bib 移除。[R2 提出, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因 API 限额耗尽（rate limit reset at 4pm UTC）而失败，未能完成 PDF 逐页检查。\n\n**状态**: error\n**原因**: Agent exited 1: You've hit your limit · resets 4pm (UTC)\n**建议**: 用户可在限额恢复后重新触发视觉审查。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n**评分分解**:\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Clarity | — | 3/5 | 3/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评价**:\n\n论文选题重要且及时——LLM 标注误差在因果推断中的传播是 NLP×CSS 交叉领域的新兴关键问题。Sign preservation taxonomy 和 FWL invariance impossibility 是有价值的理论贡献，附录极其详尽，三层证据结构设计良好。\n\n但两个核心问题制约了评分：\n\n**(1) 理论完整性 gap**：论文标题和 narrative 聚焦 \"Multi-Class\"（K≥3），但最关键的 envelope monotonicity 结论在 K≥3 下仅为数值验证的 conjecture（且 exact monotonicity 系统性不成立，60-97% 矩阵违反）。这使得 ASV 框架在论文主要聚焦的 K≥3 情形下缺乏理论保证——从 reviewer 角度看，这是可以改善但目前存在的 gap。\n\n**(2) 实验验证深度 gap**：Monte Carlo 验证了公式正确性，LLM empirical validation 验证了 confusion matrix 输入端，但从未在 outcome level 展示过 \"使用本文方法确实改善了因果估计\" 的端到端闭环。对 EMNLP 受众，这限制了对框架实际应用价值的判断。\n\n此外，对 EMNLP 受众的可及性（术语解释、信息密度）和 correction guidance 的深度也需要提升。\n\n**提升路径**：如果能 (a) 在 K≥3 理论保证上取得进展（至少 ranking 稳定性分析 + 增加验证规模），(b) 增加端到端案例研究或在 Limitations 明确承认此缺失，(c) 精简 Abstract + 增加术语直觉解释 + 充实 correction guidance，论文可达 Conference (4.0) 水平。\n\n**EMNLP 2026 ARR 评分映射**：3.5 = Borderline Conference。论文有 Findings 级别的贡献，如上述问题得到充分修复可达主会议水平。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"first unified analysis\" claim 需限定为 \"for LLM-generated multi-class annotations\"，与 Carroll et al. (2006) 区分 [W12]\n- Sign reversal framing 建议增加平衡性表述：\"five of seven topologies provide structural sign protection\" [W8]\n\n### Section 3.1 (Setup)\n- 增加 Intuition 段落用 NLP 例子建立直觉 [W7]\n- Non-differential 假设讨论扩充：何时成立/失败/检验 [W3]\n- 核心符号内联定义或引用 Table 19 [minor]\n- τ vs β_T 在不同拓扑下含义需首次出现时明确 [minor]\n\n### Section 3.2 (Bias Expressions)\n- Proportional effects 假设增加 testable implications 讨论 [W4]\n\n### Section 3.3 (ASV)\n- Remark 1 扩充技术挑战来源（Birkhoff polytope vs [1,∞) 几何差异）[W5]\n- Conjecture 1 主文补充 worst-case 实际量级（\"empirically ≤ 0.013\"）[minor]\n- C₀ 选取方式在主文简述 [minor]\n\n### Abstract\n- 精简到 3-4 核心信息点，移除 2.1%/52.6% 等具体数字 [W6]\n- \"sign reversal\" 改为 \"secondary-coefficient sign reversal\" [W8]\n- FWL invariance 声明加 \"under linear regression\" 限定 [existing issue R15-W2]\n\n### Section 4.2 (Sign Reversal Results)\n- Table 1 caption 增加 Violation/Sign Flip 列精确定义和脚注 [minor]\n\n### Section 4.5 (Correction Guidance)\n- 扩充：方法选择标准、FWL invariance 约束说明 [W9]\n- 增加 logistic regression 下 FWL 失效讨论 [W10]\n- Algorithm 1 简化版移入主文 [W9]\n\n### Figure 2\n- 改为全页宽度或拆分，增加 hatching pattern 替代颜色区分 [W13]\n\n### Limitations\n- 增加\"仅模拟验证、无真实因果数据集端到端验证\"的明确承认 [W2]\n\n### Related Work\n- 引用 Miles et al. (2024), Wei et al. (2025), Hernán & Robins (2020), Schennach (2020) [MR]"
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
    "overall_score": "3.5 - Borderline Conference",
    "report": "# 审稿报告：Multi-Class Annotation Errors in Causal Inference\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 16 (Fresh)\n**Reviewer 编排**: 2 人（R1 方法严谨性, R2 新颖性/完整性）\n**收敛状态**: 1 轮独立审稿 + 1 轮交叉分享后收敛\n\n---\n\n## Summary\n\n本文系统分析了 K-class（K≥3）LLM 标注误差在七种因果 DAG 拓扑下的传播机制。核心贡献包括：(1) 推导每种拓扑的闭式 bias 表达式并建立 sign preservation taxonomy（confounding/collider 证明 sign preserved, exposure/IV 可反转）；(2) 提出 Annotation Sensitivity Values (ASVs) 诊断框架，包含 magnitude/significance/sign-flip 三个维度；(3) 基于 FWL 不变性证明矩阵校正方法在四种协变量拓扑下无效，并给出拓扑感知校正指南。实验涵盖 Monte Carlo 模拟（161 场景 MAPE 1.6%）、23 组真实 LLM 混淆矩阵验证和五种校正方法的系统比较。\n\n---\n\n## Strengths\n\n**S1. 填补重要文献空白。** 首次在 K≥3 条件下统一分析七种标准 DAG 拓扑的标注误差传播。Brenner (1993) 仅处理二值混杂，TeBlunthuis et al. (2024) 覆盖二值四种拓扑，Lee & Wood-Doughty (2024) 仅 confounding。这一系统性本身是真正的贡献。[R1 S1, R2 S1 共识]\n\n**S2. FWL 不变性结果具有高实用价值。** Section 4.5 + Appendix B.2 证明 matrix-based corrections（Naïve plug-in, MLA）在线性 OLS 下对四种协变量拓扑无效。这个非平凡的负面贡献（impossibility result）对实践者有直接指导意义，避免了无效校正尝试。[R1 S3, R2 S2 共识]\n\n**S3. 理论-实验三层证据结构设计良好。** 每个理论 claim 都有解析证明（K=2）+ 数值验证（K≥3, 100K-210K 矩阵）+ 真实 LLM 混淆矩阵验证的三层支撑。[R1 S1, R2 S3 共识]\n\n**S4. Sign preservation taxonomy 优雅且实用。** Proposition 1 将七种拓扑清晰分为 sign-preserving（confounding/collider, 解析证明）、conditionally preserving（mediation/M-bias/front-door）和 sign-vulnerable（exposure/IV），为实践者提供直接可用的风险评估维度。[R1 S2]\n\n**S5. Algorithm 1 降低理论到实践的转化门槛。** 校正决策树覆盖风险评估、方法选择和 FWL 检查三步流程，具有工具价值。[R1 S5, R2 S4 共识]\n\n**S6. Appendix 极其详尽。** 22 页 19 个 subsection 覆盖了几乎所有可预见的 reviewer 质疑点（非微分 stress test、非线性 DGP、ClinicalBERT 案例、校正方法敏感性等），体现严谨研究态度。[R1 S6, R2 S5 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical] K≥3 envelope monotonicity 仅为 Conjecture，与 \"Multi-Class\" 标题和核心 narrative 不匹配**\n- 位置：Section 3.3 Theorem 1, Conjecture 1 (p.6), Table 10 (p.27)\n- Theorem 1（envelope monotonicity）仅对 K=2 有解析证明。K≥3 为 Conjecture 1（ε-approximate, ε < 0.06），依赖 210,000 矩阵数值验证。\n- 问题：(1) Dirichlet 均匀采样在高维空间覆盖率极低（K=7 时 42 自由度），210K 样本可能遗漏 adversarial corner cases；(2) Table 10 显示 60-97% 矩阵存在 exact monotonicity 违反（magnitude ≤ 0.013），说明 exact monotonicity 在 K≥3 下**系统性不成立**；(3) 论文未分析 \"多大的违反会导致 ASV ranking 翻转\"——0.013 的 bound 是否足以保证实用稳定性？\n- 论文标题聚焦 \"Multi-Class\" 但核心结论在 K≥3 下仅为经验观察，ASV 框架的理论基础不完整。\n- **建议**：(a) Abstract/Introduction 精确区分 \"K=2 proven\" vs \"K≥3 conjectured with numerical support\"；(b) 增加采样量到 10⁶ 并报告违反分布的尾部行为；(c) 分析 ε=0.013 下 ASV ranking 翻转的条件。\n- **共识**：R1 N1 提出, R2 交叉 AGREE 并补充 ranking 稳定性分析缺失。两位均评为 critical。\n\n**W2 [critical] 缺乏真实因果数据的端到端验证——实验仅验证公式正确性和 confusion matrix 属性**\n- 位置：Section 4 整体, Appendix B.3\n- 验证三层中缺第三层：Layer 1（解析 vs MC, MAPE 1.6%）验证数学正确性 ✓；Layer 2（23 LLM 配置性质）验证输入端行为 ✓；**Layer 3 缺失**：在已知 ground-truth 因果效应的数据上完整演示 \"估计 C → ASV 诊断 → 选择校正 → 改善估计\" 的端到端流程。\n- ClinicalBERT case study (Appendix B.3) 的 ground truth 来自 OLS on gold labels，不是真正已知因果效应。\n- **建议**：构建 NLP-native 半合成因果数据集（如 VAST stance K=3 + 注入已知因果效应 + LLM 重标注），对比无校正 vs ASV 校正的估计精度。或至少在 Limitations 明确承认此缺失（目前未提及）。\n- **共识**：R1 N2 提出, R2 W5 独立提出, 交叉 AGREE。两位一致。R2 补充 rebuttal 周期内完整验证工作量偏大，接受 Limitations 承认作为最低修复。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3. Non-differential misclassification 假设主文讨论不足**\n- 位置：Definition 1 (Section 3.1, p.4)\n- 主文仅一句 \"This holds when the LLM classifies without observing the outcome\"。需增加何时成立（LLM 未观察 outcome）、何时失败（prompt 含 outcome-correlated context）、如何检验的讨论，并引用 Appendix B.6 stress test 结果。\n- **共识**：R1 W1 提出, R2 AGREE。\n\n**W4. Proportional effects 假设 (f = λg) 缺乏实践验证指导**\n- 位置：Theorem 1 (p.6), Appendix B.13 Table 12\n- Treatment effect 是待估计未知量，无法先验验证成比例性。Independent effects 下 sign failure rate 达 23%——直接削弱 \"confounding preserves sign\" 的适用范围。需讨论 testable implications 和哪类 NLP 任务可能满足。\n- **共识**：R1 W2 提出, R2 AGREE。\n\n**W5. ASV 创新性阐述需加强（降级自 R2 must-fix）**\n- 位置：Section 3.3 (p.5-6), Remark 1\n- R2 认为 ASV 仅为 E-value 的 reparametrization（must-fix）。R1 REBUT：topology-dependence（同一 C 在不同拓扑下 ASV 不同）和 sign-flip ASV（E-value 无对应物）是结构性创新。Confusion matrix 的 Birkhoff polytope 参数空间 vs E-value 的 [1,∞) 半线有本质几何差异。\n- **Director 判定**：降为 should-fix。ASV 有真实创新但论文未充分 articulate 技术挑战的新颖性。Remark 1 需强化技术区别的深度。\n- **分歧记录**：R2 维持 must-fix, R1 认为 should-fix。\n\n**W6. Abstract 信息密度过高**\n- 188 词覆盖 7 拓扑 + sign reversal + ASV + monotonicity + correction + FWL。建议精简到 3-4 核心信息点，移除具体百分比（2.1%, 52.6%）到正文。\n- **共识**：R2 W1 提出, R1 AGREE。\n\n**W7. EMNLP 受众可及性不足——核心术语解释薄弱**\n- plim（仅脚注）、FWL theorem（无直觉解释）、Wald estimator、column-stochastic matrix、Dirichlet prior 均缺乏 NLP 语境下的直觉说明。建议 Section 3.1 增加 Intuition 段落用具体 NLP 例子建立直觉。\n- **共识**：R2 W2 提出, R1 AGREE。高优先级。\n\n**W8. \"2.1% sign reversal\" 限定不清晰——secondary vs primary coefficient**\n- Abstract \"sign reversal occurs in 2.1% of exposure configurations\" 易误解为 primary treatment effect reversal，实际为 secondary coefficient（小效应量）。Table 1 Sign Flip 列为 0%（primary）。需在 Abstract 明确 \"secondary-coefficient\" 并在 Table 1 增加脚注。\n- **共识**：R1 W4 提出, R2 W3 独立提出, 交叉 AGREE。\n\n**W9. Correction guidance 作为三大贡献之一深度不足**\n- Section 4.5 仅半页，五种方法选择标准未说明，缺计算成本讨论，Algorithm 1 放在 Appendix p.31。建议充实 Section 4.5 并将 Algorithm 1 简化版移入主文。\n- **共识**：R2 W6 提出, R1 AGREE。\n\n**W10. FWL invariance 在 logistic regression 下失效的含义未在主文讨论**\n- Appendix B.14 显示 FWL invariance 在 logistic regression 下不成立（exposure bias ~78%）。这意味着对使用 logistic regression 的 NLP 研究者，matrix-based corrections 可能有效——完全改变 Section 4.5 的 correction guidance。主文应增加此讨论。\n- **来源**：R2 Q3 提出, R1 交叉回应提升为 should-fix。\n\n**W11. ASV C(δ) 均匀退化假设与 LLM 实际误差模式不符**\n- C(δ) = (1−δ)I + δC₀ 假设所有类别以相同速率退化，但 LLM 中稀有类别通常先出错。需增加 class-frequency-weighted degradation path 稳健性实验。\n- **共识**：R1 W3 提出, R2 AGREE（但认为影响程度偏低，因 empirical LLM 矩阵本身包含不均匀退化且 ASV ranking 仍稳定）。\n\n**W12. \"First unified analysis\" novelty claim 需与经典文献区分**\n- 需与 Carroll et al. (2006) Ch.15 和 Schennach (2020) 做显式区分。建议限定为 \"first unified analysis for LLM-generated multi-class annotations across seven topologies\"。\n- **共识**：R2 N2 提出为 must-fix, R1 AGREE。Director 采纳 should-fix（限定修辞即可解决）。\n\n**W13. Figure 2 子图过小，灰度打印无法区分**\n- 七个子图挤在半页宽度，红/灰颜色区分依赖彩色打印。建议使用 hatching pattern 或拆分 figure。\n- **共识**：R2 W4 提出, R1 AGREE。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n\n1. K≥3 monotonicity 仅为 conjecture 是论文最大理论缺口\n2. 缺乏端到端真实因果数据验证\n3. Abstract 信息过载需精简\n4. EMNLP 受众可及性需提升（术语解释）\n5. \"2.1% sign reversal\" 限定不清（secondary coefficient）\n6. Non-differential 假设主文讨论不足\n7. Proportional effects 假设缺乏验证指导\n8. Correction guidance 深度不足\n9. Figure 2 视觉质量\n10. Table 1 列定义需明确\n11. FWL under logistic regression 主文缺讨论\n\n---\n\n## Reviewer Divergence\n\n**D1. ASV vs E-value 创新性（R2: must-fix → Director: should-fix）**\n- R2 认为 ASV 仅为 E-value reparametrization，核心逻辑均为 \"minimum perturbation to nullify effect\"。\n- R1 REBUT：topology-dependence 和 sign-flip ASV 是 E-value 不具备的结构性创新。Confusion matrix 参数空间（Birkhoff polytope）与 relative risk 空间（[1,∞) 半线）有本质几何差异。\n- **Director 采纳 R1**：ASV 有真实方法论创新，但论文需更好 articulate 技术新颖性。降为 should-fix。\n\n**D2. Sign reversal 风险是否被高估（R2: should-fix vs R1: REBUT）**\n- R2 认为 5/7 拓扑 sign reversal 为 0%，framing 暗示风险普遍严重。\n- R1 REBUT：论文价值在于 topology-dependent risk taxonomy，不在于声称 sign reversal 普遍——告诉实践者哪些拓扑安全、哪些危险本身就是贡献。但同意 Abstract/Introduction framing 可更平衡。\n- **Director 判定**：R1 论证更有说服力——taxonomy 是核心价值。但同意 framing 需平衡，作为 W8 的一部分处理。\n\n**D3. IV 52.6% vs 0% gap 解释充分性（R1: should-fix vs R2: REBUT）**\n- R1 认为需要比 \"structural properties\" 更具体的解释。\n- R2 REBUT：Appendix B.10 已解释 Dirichlet 产生极端矩阵、LLM diagonal dominant、IV sign reversal 需 first-stage 符号翻转（真实 LLM 不太可能），但同意主文可增加 1-2 句直觉解释。\n- **Director 判定**：R2 REBUT 有效——Appendix 已有合理解释。采纳 R2 建议在主文增加直觉说明即可，不额外列为 weakness。\n\n**D4. Veitch et al. (2020) 引用必要性（R1: AGREE vs R2: REBUT）**\n- R1 认为应引用。R2 REBUT：该工作处理 text-as-treatment 的连续表示学习，与本文离散多类别 measurement error 主题关联较弱。已引用的 Feder et al. (2022) 和 Pryzant et al. (2021) 覆盖了 text-based causal inference。\n- **Director 判定**：R2 REBUT 有效。不列为缺失引用。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Conjecture 1 在 non-proportional effects 下是否可能完全失败（而非 ε-approximate 违反）？Table 12 的 23% sign failure rate 与 monotonicity failure 的关系是什么？\n\n**Q2.** 23 个 LLM confusion matrices 在 IV 拓扑下全部 0% sign reversal——具体哪些结构属性（diagonal dominance? off-diagonal 对称性? eigenvalue 分布?）阻止了 sign reversal？能否构造 realistic-looking 的矩阵使 IV sign reversal 发生？\n\n**Q3.** Class-imbalanced 场景（如 K=10 中 rare class 占 5%）下 ASV ranking 是否仍可靠？C(δ) 的均匀退化与实际不均匀退化的差异会否改变 topology vulnerability ranking？\n\n**Q4.** Non-differential 假设失败时（ε > 0.10），ASV topology vulnerability ranking（IV > Exposure > ... > M-bias）是否仍保持？Appendix B.6 覆盖了弱违反但未报告 ranking 稳定性。\n\n**Q5.** ASV 的 topology-dependent 特性能否反向推断 DAG 拓扑？Appendix B.11 Table 9 暗示某些维度可区分拓扑（sign-flip behavior），但 magnitude ASV 跨拓扑可能相同——这个方向的可行性和局限性是什么？\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 交叉确认为应引用：\n\n1. **Miles, Valeri, and Coull (2024)**. \"Measurement Error-Robust Causal Inference via Constructed Instrumental Variables.\" arXiv:2406.00940. — 与 IV 拓扑分析直接相关。[R2 提出, R1 AGREE]\n2. **Wei, He, Li, and Geng (2025)**. \"Multiply robust causal inference in the presence of an error-prone treatment.\" Statistical Methods in Medical Research. — 与 exposure 拓扑分析直接相关。[R2 提出, R1 AGREE]\n3. **Hernán MA, Robins JM (2020)**. \"Causal Inference: What If.\" Chapman & Hall/CRC. Chapter 9 关于 measurement error 对 identification 的影响。— 因果推断标准教材。[R1 提出, R2 AGREE]\n4. **Schennach (2020)**. 已在 bib 中但未在正文引用。应在 Related Work 引用或从 bib 移除。[R2 提出, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因 API 限额耗尽（rate limit reset at 4pm UTC）而失败，未能完成 PDF 逐页检查。\n\n**状态**: error\n**原因**: Agent exited 1: You've hit your limit · resets 4pm (UTC)\n**建议**: 用户可在限额恢复后重新触发视觉审查。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n**评分分解**:\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Clarity | — | 3/5 | 3/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评价**:\n\n论文选题重要且及时——LLM 标注误差在因果推断中的传播是 NLP×CSS 交叉领域的新兴关键问题。Sign preservation taxonomy 和 FWL invariance impossibility 是有价值的理论贡献，附录极其详尽，三层证据结构设计良好。\n\n但两个核心问题制约了评分：\n\n**(1) 理论完整性 gap**：论文标题和 narrative 聚焦 \"Multi-Class\"（K≥3），但最关键的 envelope monotonicity 结论在 K≥3 下仅为数值验证的 conjecture（且 exact monotonicity 系统性不成立，60-97% 矩阵违反）。这使得 ASV 框架在论文主要聚焦的 K≥3 情形下缺乏理论保证——从 reviewer 角度看，这是可以改善但目前存在的 gap。\n\n**(2) 实验验证深度 gap**：Monte Carlo 验证了公式正确性，LLM empirical validation 验证了 confusion matrix 输入端，但从未在 outcome level 展示过 \"使用本文方法确实改善了因果估计\" 的端到端闭环。对 EMNLP 受众，这限制了对框架实际应用价值的判断。\n\n此外，对 EMNLP 受众的可及性（术语解释、信息密度）和 correction guidance 的深度也需要提升。\n\n**提升路径**：如果能 (a) 在 K≥3 理论保证上取得进展（至少 ranking 稳定性分析 + 增加验证规模），(b) 增加端到端案例研究或在 Limitations 明确承认此缺失，(c) 精简 Abstract + 增加术语直觉解释 + 充实 correction guidance，论文可达 Conference (4.0) 水平。\n\n**EMNLP 2026 ARR 评分映射**：3.5 = Borderline Conference。论文有 Findings 级别的贡献，如上述问题得到充分修复可达主会议水平。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"first unified analysis\" claim 需限定为 \"for LLM-generated multi-class annotations\"，与 Carroll et al. (2006) 区分 [W12]\n- Sign reversal framing 建议增加平衡性表述：\"five of seven topologies provide structural sign protection\" [W8]\n\n### Section 3.1 (Setup)\n- 增加 Intuition 段落用 NLP 例子建立直觉 [W7]\n- Non-differential 假设讨论扩充：何时成立/失败/检验 [W3]\n- 核心符号内联定义或引用 Table 19 [minor]\n- τ vs β_T 在不同拓扑下含义需首次出现时明确 [minor]\n\n### Section 3.2 (Bias Expressions)\n- Proportional effects 假设增加 testable implications 讨论 [W4]\n\n### Section 3.3 (ASV)\n- Remark 1 扩充技术挑战来源（Birkhoff polytope vs [1,∞) 几何差异）[W5]\n- Conjecture 1 主文补充 worst-case 实际量级（\"empirically ≤ 0.013\"）[minor]\n- C₀ 选取方式在主文简述 [minor]\n\n### Abstract\n- 精简到 3-4 核心信息点，移除 2.1%/52.6% 等具体数字 [W6]\n- \"sign reversal\" 改为 \"secondary-coefficient sign reversal\" [W8]\n- FWL invariance 声明加 \"under linear regression\" 限定 [existing issue R15-W2]\n\n### Section 4.2 (Sign Reversal Results)\n- Table 1 caption 增加 Violation/Sign Flip 列精确定义和脚注 [minor]\n\n### Section 4.5 (Correction Guidance)\n- 扩充：方法选择标准、FWL invariance 约束说明 [W9]\n- 增加 logistic regression 下 FWL 失效讨论 [W10]\n- Algorithm 1 简化版移入主文 [W9]\n\n### Figure 2\n- 改为全页宽度或拆分，增加 hatching pattern 替代颜色区分 [W13]\n\n### Limitations\n- 增加\"仅模拟验证、无真实因果数据集端到端验证\"的明确承认 [W2]\n\n### Related Work\n- 引用 Miles et al. (2024), Wei et al. (2025), Hernán & Robins (2020), Schennach (2020) [MR]"
  }
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-23T12:46:35.073707+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4325
}
```

</details>

---


### Assistant

_source line 1324 · 2026-05-23T12:46:43.516271+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall**: 3.5 / 5 (Borderline Conference)
- **2 个 Must-Fix**：(1) K≥3 monotonicity 仅为 conjecture，ASV 理论基础不完整；(2) 缺乏端到端真实因果数据验证
- **11 个 Should-Fix**：non-differential 假设讨论不足、proportional effects 验证指导、ASV 创新性阐述、Abstract 信息过载、EMNLP 可及性、2.1% sign reversal 限定、correction guidance 深度、FWL under logistic 缺讨论、ASV 均匀退化假设、novelty claim 限定、Figure 2 视觉质量
- **4 篇缺失引用**：Miles et al. (2024), Wei et al. (2025), Hernán & Robins (2020), Schennach (2020)
- **提升路径**：修复上述问题后可达 Conference (4.0) 水平

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 133

## Round 133

2 recorded events


### User

_source line 1325 · 2026-05-23T12:46:46.331457+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条交叉回应，共涵盖 2 个 Must-Fix、6 个 Should-Fix、5 个 Minor、5 个 Question、4 个 Missing Reference。

核心判断：
- **N1 (ASV vs E-value)**: [REBUT]——topology-dependence 和 sign-flip ASV 是结构性创新，非简单 reparametrization，建议降级为 should-fix
- **N2 (novelty claim 限定)**: [AGREE]——应限定为 "for LLM-generated multi-class annotations in NLP pipeline context"
- **W3 (sign reversal 高估)**: [REBUT]——论文价值在于 topology-dependent risk taxonomy，非声称 sign reversal 普遍严重
- **Q3 (FWL under logistic)**: [AGREE] 并建议提升为 should-fix——这对 NLP 实践者的 correction guidance 有重要含义
- **Q4 (K=2 CivilComments)**: [REBUT]——K=2 验证 Theorem 1 的解析结果，与 K≥3 互补
- **M4 (Conjecture 1 量化)**: [REBUT]——Conjecture 1 已明确写出 ε < 0.06

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

_source line 1326 · 2026-05-23T12:47:02.250152+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall: 3.5 (Borderline Conference)**
- **2 个 Must-Fix**：K≥3 monotonicity 仅为 conjecture（论文最大理论缺口）；缺乏端到端真实因果数据验证
- **11 个 Should-Fix**：non-differential 假设讨论不足、proportional effects 验证指导缺失、ASV 创新性阐述需加强、Abstract 信息过载、EMNLP 可及性不足、sign reversal 限定不清、correction guidance 深度不足、FWL under logistic 主文缺讨论、ASV 均匀退化假设、novelty claim 限定、Figure 2 视觉质量
- **4 篇缺失引用**：Miles et al. (2024)、Wei et al. (2025)、Hernán & Robins (2020)、Schennach (2020)
- **提升路径**：修复上述问题后可达 Conference (4.0) 水平
- **视觉审查**：因 API 限额失败，完成后会自动补发到 Group C
- **Issue Tracker**：已同步更新至 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 134

## Round 134

52 recorded events


### User

_source line 1327 · 2026-05-23T13:39:16.218430+00:00_

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

_source line 1328 · 2026-05-23T13:39:23.547330+00:00_

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

_source line 1329 · 2026-05-23T13:39:23.598371+00:00_

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

_source line 1330 · 2026-05-23T13:39:31.578098+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
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
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-23T13:39:31.628776+00:00_

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


### Tool call

_source line 1332 · 2026-05-23T13:39:35.545952+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-23T13:39:35.598381+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-23T13:39:40.267922+00:00_

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

_source line 1335 · 2026-05-23T13:39:40.318759+00:00_

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


### Tool call

_source line 1336 · 2026-05-23T13:39:47.048291+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
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
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-23T13:39:47.149191+00:00_



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

_source line 1338 · 2026-05-23T13:39:54.629349+00:00_

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

_source line 1339 · 2026-05-23T13:39:56.035546+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-23T13:39:56.086290+00:00_

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

_source line 1341 · 2026-05-23T13:39:56.137016+00:00_

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
19	\newtheorem{remark}{Remark}
20	
21	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
24	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
25	\graphicspath{{../../figures/paper/}}
26	
27	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{abstract}
35	
36	\input{introduction}
37	
38	\begin{figure*}[t]
39	\centering
40	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
41	\vspace{-6pt}
42	\caption{Seven canonical DAG topologies with starred-node annotation~\cite{hernan_cole2009}. $A$ (latent) $\to$ $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies: treatment (exposure), covariate (confounding, mediation, M-bias, front-door), selection (collider), instrument (IV).}
43	\label{fig:dag_taxonomy}
44	\end{figure*}
45	
46	\input{related_work}
47	
48	\input{method}
49	
50	\input{experiments}
51	
52	\input{conclusion}
53	
54	\bibliography{references}
55	
56	\appendix
57	\input{appendix_proofs}
58	
59	\end{document}
60	

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

_source line 1342 · 2026-05-23T13:39:56.187677+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 1343 · 2026-05-23T13:39:56.439005+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-23T13:40:06.291820+00:00_

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

_source line 1345 · 2026-05-23T13:40:06.844548+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy, sign reversal of secondary coefficients occurs under exposure; under empirical LLM matrices (diagonal 0.45--0.81), sign reversal is confined to exposure; IV is fragile under uniform Dirichlet priors but exhibits zero reversals under empirical LLM matrices. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$) and numerically verified ($K{\geq}3$) monotonicity, yielding a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

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

_source line 1346 · 2026-05-23T13:40:06.844921+00:00_

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

_source line 1347 · 2026-05-23T13:40:07.353792+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors (equivalently, misclassification) from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, h
…[truncated 3064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---


### Tool call

_source line 1348 · 2026-05-23T13:40:07.504876+00:00_

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

_source line 1349 · 2026-05-23T13:40:07.856567+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{imai_keele_tingley2010, valeri_vanderweele2013}. \citet{schennach2020mismeasured} addresses general nonclassical measurement error in regression; \citet{miles2024measurement} construct instrumental variables for measurement-error-robust estimation; \citet{wei2025multiply} develop multiply robust estimators under misclassified treatment. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation 
…[truncated 2558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-23T13:40:07.856936+00:00_

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

_source line 1351 · 2026-05-23T13:40:08.309288+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes systematic bias---the value an estimator converges to as $N \to \infty$ (the probability limit, or plim)---rather than finite-sample variance. The Frisch--Waugh--Lovell (FWL) theorem guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables; this is why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}): replacing the mismeasured variable with a corrected version does not change the residualized relationship. The Wald estimator (ratio of reduced-form to first-stage effects) diverges under weak instruments; Dirichlet priors over probability vectors represent uncertainty over misclassification patterns. Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}) collects all notation.
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	This holds when the LLM classifies without observing the outcome---the typical CSS setup~\cite{ziems2024can}; topic-stratified confusion matrices confirm cross-gro
…[truncated 13597 chars]

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

_source line 1352 · 2026-05-23T13:40:08.309878+00:00_

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

_source line 1353 · 2026-05-23T13:40:08.763658+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each topology, we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute analytical probability limits, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies). Per-topology MAPE: 0.3\% (confounding) to 3.7\% (IV, reflecting Wald estimator variance amplification).
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient. The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\ref{conj:monotone}); M-bias shows weakest sensitivity (53.2\% violation). All patterns persist at $K{=}5,7$ (Appendix~\ref{sec:cross_k_robustne
…[truncated 5719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-23T13:40:08.764088+00:00_

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

_source line 1355 · 2026-05-23T13:40:10.571398+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: the binary attenuation guarantee breaks at $K \geq 3$, where exposure and IV can reverse signs while five topologies preserve them. ASVs yield a vulnerability ranking from IV (most fragile) to M-bias (immune); matrix-based corrections are provably ineffective for four covariate topologies due to FWL invariance. Code and data will be released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification, which holds when the LLM classifies without observing $Y$ but may be violated when pretraining data encodes $A$--$Y$ associations (Appendix~\ref{sec:nondiff_stress}). Closed-form bias expressions assume $K{=}3$ linear SEMs; extensions to arbitrary $K$ and nonlinear models~\cite{schennach2020mismeasured} remain open, though rankings are stable across $K{=}3,5,10$. The framework assumes $C$ is known or estimable from held-out gold labels. Our experiments verify formulas via Monte Carlo simulation; end-to-end demonstration with ground-truth causal effects remains future work.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 1807
}
```

</details>

---


### Tool call

_source line 1356 · 2026-05-23T13:40:10.722538+00:00_

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


### Tool call

_source line 1357 · 2026-05-23T13:40:10.722962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
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
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1358 · 2026-05-23T13:40:10.924428+00:00_

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
…[truncated 21736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 1359 · 2026-05-23T13:40:11.276247+00:00_

File content (41546 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-23T13:40:11.326970+00:00_

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

_source line 1361 · 2026-05-23T13:40:12.682628+00:00_

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


### Tool call

_source line 1362 · 2026-05-23T13:40:12.683015+00:00_

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

_source line 1363 · 2026-05-23T13:40:12.935433+00:00_

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
…[truncated 35195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool result

_source line 1364 · 2026-05-23T13:40:18.706868+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines with ARR:

## EMNLP 2026 Paper Submission

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Key Submission Details

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Following the ACL and ARR policies, there is no anonymity period requirement.

## ARR-Specific Policy for EMNLP 2026

For the ARR 20
…[truncated 700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7379
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-23T13:40:18.858042+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 6175
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-23T13:40:48.272276+00:00_

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

_source line 1367 · 2026-05-23T13:40:49.175713+00:00_

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
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1368 · 2026-05-23T13:40:49.677698+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission guidelines page limits formatting",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net', 'aclrollingreview.org']"
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
    "query": "ACL Rolling Review 2026 May submission guidelines page limits formatting",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1369 · 2026-05-23T13:40:50.681786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_17/submitted.pdf",
  "pages": "1-8"
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
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_17/submitted.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 1370 · 2026-05-23T13:40:51.237051+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_17/submitted.pdf (897.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-23T13:40:58.812644+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission guidelines page limits formatting"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026 regarding page limits and formatting:

## Page Limits

Long papers follow a page limit of 8 pages, while short papers are limited to 4 pages, not including limitations and ethica
…[truncated 1033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 9134
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-23T13:41:40.121871+00:00_

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


### Tool result

_source line 1373 · 2026-05-23T13:42:02.744012+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22622
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-23T13:42:04.049510+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "text": "你是 Reviewer 1，负责审查本论文的**方法严谨性**。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: projects/causal_annot_error_attrib/docs/paper/main.tex\n- **PDF**: projects/causal_annot_error_attrib/artifacts/review_round_17/submitted.pdf\n\n## Venue 要求\n- **目标**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（不含 references 和 Limitations）\n- **模板**: ACL review 格式\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有，不计入页数，不可包含新实验/分析\n- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n## 你的审查侧重\n\n**核心任务：方法严谨性评估**\n\n请重点审查以下方面：\n\n1. **理论基础完整性**\n   - Theorem 1（K=2 envelope monotonicity）的证明是否正确完整？\n   - Observation 1 和 Conjecture 1 的数值验证是否充分？特别注意 Conjecture 1 覆盖范围（K≥3）的理论缺口\n   - Proposition 1 的 sign preservation 条件是否足够 precise？\n\n2. **假设合理性**\n   - Non-differential misclassification 假设在 LLM annotator 场景下是否合理？主文讨论是否充分？\n   - Proportional effects 假设（f=λg）在 NLP 任务中的适用性——是否可验证？违反时后果如何？\n   - Linear SEM 假设对 EMNLP 读者的适用性和泛化性\n\n3. **实验方法论**\n   - 161 scenarios 的 theory-MC agreement (MAPE 1.6%) 验证是否充分？\n   - 100,000 Dirichlet 矩阵在高维空间的覆盖率是否足以支撑 sign preservation 声称？\n   - 是否存在端到端实证验证（confusion matrix estimation → ASV diagnosis → correction → improved estimates）？\n   - 23 LLM configurations 的多样性是否足够？\n\n4. **数值声称一致性**\n   - Abstract/Introduction/Section 4.2/Appendix 之间的数值是否一致？\n   - Observation 1 声称的 worst-case deviation 与 Table 10 数据是否一致？\n   - Table 1 各列（Violation, Sign Flip, Amplif.）的定义是否清晰无歧义？\n\n5. **FWL Invariance 结论**\n   - 证明是否完整？\n   - 在 logistic regression 下 FWL 失效的含义是否在主文充分讨论？\n   - 对 correction guidance 的影响是否准确表述？\n\n请按 ARR 标准出具完整审稿报告，包括：Summary、Strengths（逐条）、Weaknesses（逐条，标注 must-fix/should-fix/minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
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
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
    "text": "你是 Reviewer 1，负责审查本论文的**方法严谨性**。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: projects/causal_annot_error_attrib/docs/paper/main.tex\n- **PDF**: projects/causal_annot_error_attrib/artifacts/review_round_17/submitted.pdf\n\n## Venue 要求\n- **目标**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（不含 references 和 Limitations）\n- **模板**: ACL review 格式\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有，不计入页数，不可包含新实验/分析\n- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n## 你的审查侧重\n\n**核心任务：方法严谨性评估**\n\n请重点审查以下方面：\n\n1. **理论基础完整性**\n   - Theorem 1（K=2 envelope monotonicity）的证明是否正确完整？\n   - Observation 1 和 Conjecture 1 的数值验证是否充分？特别注意 Conjecture 1 覆盖范围（K≥3）的理论缺口\n   - Proposition 1 的 sign preservation 条件是否足够 precise？\n\n2. **假设合理性**\n   - Non-differential misclassification 假设在 LLM annotator 场景下是否合理？主文讨论是否充分？\n   - Proportional effects 假设（f=λg）在 NLP 任务中的适用性——是否可验证？违反时后果如何？\n   - Linear SEM 假设对 EMNLP 读者的适用性和泛化性\n\n3. **实验方法论**\n   - 161 scenarios 的 theory-MC agreement (MAPE 1.6%) 验证是否充分？\n   - 100,000 Dirichlet 矩阵在高维空间的覆盖率是否足以支撑 sign preservation 声称？\n   - 是否存在端到端实证验证（confusion matrix estimation → ASV diagnosis → correction → improved estimates）？\n   - 23 LLM configurations 的多样性是否足够？\n\n4. **数值声称一致性**\n   - Abstract/Introduction/Section 4.2/Appendix 之间的数值是否一致？\n   - Observation 1 声称的 worst-case deviation 与 Table 10 数据是否一致？\n   - Table 1 各列（Violation, Sign Flip, Amplif.）的定义是否清晰无歧义？\n\n5. **FWL Invariance 结论**\n   - 证明是否完整？\n   - 在 logistic regression 下 FWL 失效的含义是否在主文充分讨论？\n   - 对 correction guidance 的影响是否准确表述？\n\n请按 ARR 标准出具完整审稿报告，包括：Summary、Strengths（逐条）、Weaknesses（逐条，标注 must-fix/should-fix/minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-23T13:42:26.624507+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22574
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-23T13:42:27.026981+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "text": "你是 Reviewer 2，负责审查本论文的**新颖性与完整性**。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: projects/causal_annot_error_attrib/docs/paper/main.tex\n- **PDF**: projects/causal_annot_error_attrib/artifacts/review_round_17/submitted.pdf\n\n## Venue 要求\n- **目标**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（不含 references 和 Limitations）\n- **模板**: ACL review 格式\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有，不计入页数，不可包含新实验/分析\n- **ARR 规则**: Limitations section 只能讨论局限性，不得包含额外实验、图表或分析\n- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n## 你的审查侧重\n\n**核心任务：新颖性与完整性评估**\n\n请重点审查以下方面：\n\n1. **新颖性定位**\n   - \"first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies\" 是否准确？与 Carroll et al. (2006)、Schennach (2020) 的区分是否清晰？\n   - ASV 框架相对于 E-values (VanderWeele & Ding, 2017) 和 partial-R² bounds (Cinelli & Hazlett, 2020) 的方法论创新在哪里？是 reparametrization 还是结构性创新？\n   - Remark 1 的三点区分是否充分？是否需要更深入的技术新颖性说明（如 Birkhoff polytope 几何 vs E-value 半线）？\n   - Correction guidance 作为三大贡献之一，深度是否匹配？（Section 4.5 仅半页）\n\n2. **Related Work 覆盖度**\n   - 是否有遗漏的关键相关工作？特别关注：\n     - Measurement error in causal inference 领域\n     - LLM annotation quality 领域\n     - Sensitivity analysis 领域\n     - Correction/debiasing 方法\n   - 正文引用 vs bib 文件是否一致（有 bib 条目未被正文引用的情况）？\n\n3. **表达清晰度与 EMNLP 受众可达性**\n   - 计量经济学/统计学术语（plim, FWL, Wald estimator, column-stochastic, Dirichlet prior）对 NLP 读者是否足够友好？\n   - Section 3.1 的 Notation 段落是否提供足够的直觉建设？\n   - Abstract 信息密度是否过高？（覆盖 7 拓扑+多项数值结果，是否应精简到 3-4 核心信息点？）\n   - Abstract 是否超过 200 words（EMNLP 2026 限制）？\n\n4. **格式合规**\n   - 正文是否在 8 页内？\n   - Limitations section 是否仅讨论局限性（不含新实验/图表）？\n   - 匿名规则是否遵守？（检查是否有 de-anonymizing 信息）\n   - 引用格式是否一致？\n\n5. **Presentation 质量**\n   - Figure 1 (DAG taxonomy) 信息传达是否清晰？\n   - Figure 2 (bias distribution) 七子图是否过于拥挤？颜色方案是否依赖彩色打印？\n   - Table 1 的列定义是否清晰？Sign Flip 列指 primary 还是 secondary coefficient？\n   - 2.1% sign reversal 在 Abstract 中的表述是否容易被误解？（是 secondary coefficient 还是 primary？）\n\n6. **Correction Guidance 深度**\n   - 五种方法的选择标准是否充分说明？\n   - 计算成本讨论是否存在？\n   - Algorithm 1 是否应在主文出现？\n\n请按 ARR 标准出具完整审稿报告，包括：Summary、Strengths（逐条）、Weaknesses（逐条，标注 must-fix/should-fix/minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
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
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
    "text": "你是 Reviewer 2，负责审查本论文的**新颖性与完整性**。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: projects/causal_annot_error_attrib/docs/paper/main.tex\n- **PDF**: projects/causal_annot_error_attrib/artifacts/review_round_17/submitted.pdf\n\n## Venue 要求\n- **目标**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（不含 references 和 Limitations）\n- **模板**: ACL review 格式\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有，不计入页数，不可包含新实验/分析\n- **ARR 规则**: Limitations section 只能讨论局限性，不得包含额外实验、图表或分析\n- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n## 你的审查侧重\n\n**核心任务：新颖性与完整性评估**\n\n请重点审查以下方面：\n\n1. **新颖性定位**\n   - \"first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies\" 是否准确？与 Carroll et al. (2006)、Schennach (2020) 的区分是否清晰？\n   - ASV 框架相对于 E-values (VanderWeele & Ding, 2017) 和 partial-R² bounds (Cinelli & Hazlett, 2020) 的方法论创新在哪里？是 reparametrization 还是结构性创新？\n   - Remark 1 的三点区分是否充分？是否需要更深入的技术新颖性说明（如 Birkhoff polytope 几何 vs E-value 半线）？\n   - Correction guidance 作为三大贡献之一，深度是否匹配？（Section 4.5 仅半页）\n\n2. **Related Work 覆盖度**\n   - 是否有遗漏的关键相关工作？特别关注：\n     - Measurement error in causal inference 领域\n     - LLM annotation quality 领域\n     - Sensitivity analysis 领域\n     - Correction/debiasing 方法\n   - 正文引用 vs bib 文件是否一致（有 bib 条目未被正文引用的情况）？\n\n3. **表达清晰度与 EMNLP 受众可达性**\n   - 计量经济学/统计学术语（plim, FWL, Wald estimator, column-stochastic, Dirichlet prior）对 NLP 读者是否足够友好？\n   - Section 3.1 的 Notation 段落是否提供足够的直觉建设？\n   - Abstract 信息密度是否过高？（覆盖 7 拓扑+多项数值结果，是否应精简到 3-4 核心信息点？）\n   - Abstract 是否超过 200 words（EMNLP 2026 限制）？\n\n4. **格式合规**\n   - 正文是否在 8 页内？\n   - Limitations section 是否仅讨论局限性（不含新实验/图表）？\n   - 匿名规则是否遵守？（检查是否有 de-anonymizing 信息）\n   - 引用格式是否一致？\n\n5. **Presentation 质量**\n   - Figure 1 (DAG taxonomy) 信息传达是否清晰？\n   - Figure 2 (bias distribution) 七子图是否过于拥挤？颜色方案是否依赖彩色打印？\n   - Table 1 的列定义是否清晰？Sign Flip 列指 primary 还是 secondary coefficient？\n   - 2.1% sign reversal 在 Abstract 中的表述是否容易被误解？（是 secondary coefficient 还是 primary？）\n\n6. **Correction Guidance 深度**\n   - 五种方法的选择标准是否充分说明？\n   - 计算成本讨论是否存在？\n   - Algorithm 1 是否应在主文出现？\n\n请按 ARR 标准出具完整审稿报告，包括：Summary、Strengths（逐条）、Weaknesses（逐条，标注 must-fix/should-fix/minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-23T13:42:28.603589+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1576
}
```

</details>

---


### Assistant

_source line 1378 · 2026-05-23T13:42:39.249493+00:00_

**Step 1 启动完成**：
- ✅ 视觉审查 Agent 已派发（fire-and-forget）
- ✅ Reviewer 1（方法严谨性）已分配
- ✅ Reviewer 2（新颖性与完整性）已分配

等待两位 Reviewer 返回初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 135

## Round 135

2 recorded events


### User

_source line 1379 · 2026-05-23T13:50:49.746403+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿报告：新颖性与完整性评估

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿维度**: 新颖性与完整性

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**Soundness**: 4 / 5 (Strong)
**Excitement**: 3 / 5 (Interesting)
**Confidence**: 4 / 5 (Quite sure)

**一句话总结**: 理论工作扎实、MC验证充分，但 abstract 超字数限制（245 vs 200 words）为硬伤格式违规，correction guidance 作为三大贡献之一深度不足，ASV 相对于 E-values 的结构性创新论证不够充分。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 解析推导严谨，MC验证 1.6% MAPE，经验LLM矩阵验证到位；Conjecture 1 对 general K>3 仅有数值验证而无证明是唯一缺口 |
| Excitement | 3/5 | 对 CSS+NLP 交叉领域有实际价值，K≥3 sign reversal 是非平凡发现；但理论密度高、应用场景窄，EMNLP 核心读者触达有限 |
| Overall | 3.5/5 | 理论贡献充实但存在格式违规和贡献深度不均衡问题 |
| Confidence | 4/5 | 熟悉 measurement error 和因果推断文献，仔细核查了证明和实验 |

---

## Summary

本文系统分析了 LLM 生成的 K-class（K≥3）标注误差在七种典型因果 DAG 拓扑下对因果估计的偏差传播。核心发现是 K≥3 的列随机混淆矩阵可以产生符号反转（sign reversal），这在 K=2 时因代数结构约束而不可能。论文提出 Annotation Sensitivity Values (ASV) 框架进行敏感性分析，建立了从 IV（最脆弱）到 M-bias（免疫）的脆弱性排序，并证明 Frisch-Waugh-Lovell 不变性使矩阵校正方法在四种拓扑下可证明无效。实验包括 100,000 组 Dirichlet 矩阵的 MC 模拟、23 个经验 LLM 混淆矩阵的验证、以及五种校正方法的对比。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract 超过 200 words 限制
- 具体位置：Abstract（第1页）
- 问题：当前 abstract 约 245 words，超出 EMNLP 2026 规定的 200 words 上限约 22.5%。逐字统计确认：从 "Large language models" 到 "LLM-generated annotations" 共 245 词。
- 为什么影响接收：这是 EMNLP 2026 的硬性格式要求，desk reject 风险。ARR submission form 明确限制 abstract 不超过 200 words。
- 建议修改方向：当前 abstract 试图覆盖全部七种拓扑结果和多项数值发现。建议精简到 3-4 个核心信息点：(1) K≥3 sign reversal 的结构性发现；(2) ASV 框架及脆弱性排序；(3) FWL 不变性对校正的启示。删除具体数值（如 "diagonal 0.45-0.81"）和次要拓扑的逐一列举，用高层概括替代。

**N2** [critical] Correction Guidance 深度与"三大贡献"定位不匹配
- 具体位置：Section 4.5（第8页，约半页）+ Appendix Table 4
- 问题：Introduction（Section 1, p.2）将 "topology-aware correction guidance" 列为三大贡献之一（与 bias taxonomy 和 ASV 并列）。但正文 Section 4.5 仅约半页，包含：(a) 五种方法的一句话描述；(b) FWL 不变性的结论引用；(c) 指向 Appendix Table 4 的指引。主文中没有任何方法选择标准的讨论、计算成本对比、或适用场景分析。Algorithm 1 只出现在附录第30页（Appendix C, Table 19/p.30）。
- 为什么影响接收：贡献声明与实际内容深度严重不对称。一个"主要贡献"只有半页正文，核心内容（Algorithm 1、Table 4 的详细结果）全部在附录，reviewer 有理由质疑这是否构成独立贡献。
- 建议修改方向：要么 (a) 将 Algorithm 1 移入正文、增加方法选择讨论和计算成本对比（可能需要压缩其他部分以符合8页限制），要么 (b) 降低 correction guidance 的贡献定位，从"三大贡献"降级为"附带讨论"，在 Introduction 中诚实表述为 "we additionally survey correction methods and find..."

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] ASV 相对于 E-values 的方法论创新论证不充分
- 具体位置：Section 3.3（第5-6页）, Remark 1（第6页）
- 问题：Remark 1 给出三点区分——(1) topology dependence, (2) E-value 统一处理 confounding 而 ASV 按拓扑分层, (3) sign-flip diagnostic 无 E-value 对应物, (4) K² 维度 vs 标量。但这些区分主要是**应用域差异**（annotation error vs unmeasured confounding）和**参数化差异**（Birkhoff polytope vs 半线），而非**方法论结构的创新**。核心数学操作——沿参数路径 C(δ)=(1-δ)I+δC₀ 计算 plim 达到阈值的最小 δ——本质上是敏感性分析的标准 "tipping point" 方法。论文没有展示 ASV 能得出 E-values 在同一问题上无法得出的定性结论。
- 建议：增加一个具体例子或命题，展示 ASV 的拓扑分层能力在 E-value 框架下无法自然实现（例如：同一个 C 在 confounding 下 ASV=∞ 但在 exposure 下 ASV<0.1，而 E-value 无法区分这两种场景）。这将把"reparametrization"提升为"structural innovation"。

**W2** [warning] Conjecture 1 对 K>3 的一般单调性缺少证明
- 具体位置：Section 3.3, Conjecture 1（第6页）; Appendix B.12（第26页）
- 问题：Theorem 1 仅证明了 K=2 的 envelope monotonicity。对 K≥3，论文声称 "verified across 10,000 random matrices per topology for each τ ∈ {0.1, 0.5, 1.0, 2.0, 5.0}"（Conjecture 1 statement）。10,000 个矩阵的数值验证无法替代证明——可能存在 measure-zero 的反例集合。论文承认这一点（"rests on numerical evidence"），但 ASV 的 "vulnerability ranking" 功能依赖于此单调性。
- 为什么影响评分：如果单调性对某个 K≥3 配置失败，ASV 排序的实用价值将受损。这不是致命缺陷（数值证据相当充分），但应更显著地标注为 open question。
- 建议：(a) 在正文中明确标注 Conjecture 1 为 open problem 而非 "verified" 结论；(b) 考虑增加反例搜索的描述（如是否尝试了 adversarial 方向的搜索）；(c) 讨论单调性失败对实际应用的影响范围。

**W3** [warning] EMNLP 受众可达性偏低
- 具体位置：全文，特别是 Section 3.1-3.3（第3-6页）
- 问题：论文大量使用计量经济学/统计学术语且 NLP 读者未必熟悉：
  - **plim**（probability limit）：仅在脚注2（第4页）简要定义，后续全文反复使用
  - **FWL theorem**：Section 2（第3页）首次提及时仅写 "Frisch-Waugh-Lovell"，没有一句话直觉解释它为什么重要
  - **Wald estimator**：第5页使用但未解释其在 IV 回归中的角色
  - **column-stochastic**：第4页定义但与 NLP 读者更熟悉的 "confusion matrix where columns sum to 1" 未建立直觉连接
  - **Birkhoff polytope**（Remark 1, 第6页）：完全未定义
  - **Dirichlet prior**：生成混淆矩阵的工具，但为何选择 Dirichlet(1,1,1) 而非其他 prior 没有直觉说明
- 为什么影响评分：EMNLP 2026 的 reviewer pool 以 NLP 研究者为主。如果3个 reviewer 中有2个因术语壁垒无法完全理解论文，excitement score 会受到显著影响。
- 建议：(a) 为 plim 和 FWL 各增加1-2句直觉解释；(b) 将 Birkhoff polytope 替换为更直观的描述（如 "the space of all doubly-stochastic matrices"）；(c) 在 Section 3.1 增加一个 "Intuition" 小段落，用非技术语言概括核心思想。

**W4** [warning] "Sign reversal" 的 primary vs secondary coefficient 区分在正文中不够清晰
- 具体位置：Abstract, Section 4.2（第7页）
- 问题：Abstract 说 "sign reversal of secondary coefficients occurs under exposure"——这里 "secondary" 指 K≥3 dummy 编码中非基准类别对应的第2、3...个回归系数。但这一术语在 abstract 中首次出现时没有定义。Section 4.2（第7页）说 "the violation rate is 13.7% with a 2.1% sign reversal"——这里的 "sign reversal" 是指任何一个系数还是主效应系数？进一步，正文说 "The primary treatment coefficient, however, is never reversed in any tested configuration"——这个关键信息对理解 sign reversal 的实际严重程度至关重要，但没有出现在 abstract 中。
- 建议：(a) 在 abstract 中明确 "secondary coefficients" 的含义或改用更直观的表述；(b) 将 "primary coefficient never reverses" 作为与 sign reversal 对称的信息纳入 abstract（如果字数允许——但当前 abstract 已超限，所以需要整体重写）。

**W5** [warning] Bib 存在 2 条未引用条目
- 具体位置：references.bib
- 问题：dawid1979（"Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm"）和 rosenbaum2002（"Observational Studies"）在 bib 文件中存在但正文未引用。两篇都与论文主题相关（Dawid-Skene 是标注聚合的经典方法，Rosenbaum 2002 是观察研究的标准参考），但如果不引用则不应出现在 bib 中。
- 建议：要么在正文中引用（Dawid & Skene 1979 可以在讨论标注质量估计时引用，Rosenbaum 2002 可以在 sensitivity analysis 背景中引用），要么从 bib 中移除。

---

## 小问题（不影响接收）

1. **Figure 2 信息密度**：7个子图在单栏内略显拥挤，但尚可辨识。建议标注每个子图的 sign reversal 百分比（目前只在 caption 中给出 Exposure 和 IV 的数字）。颜色方案（红色=sign reversal）在灰度打印下可能不易区分——考虑增加 hatching pattern。

2. **Figure 1 DAG 示意图**：7个 DAG 排列清晰，但 starred-node convention（A* vs A）的解释仅在 caption 中，首次阅读时容易错过。建议在 Section 3.1 正文中也提及此约定。

3. **Table 1 列定义**："Sign Flip" 列的具体含义（是任何系数反转还是主效应反转）在表题中未明确。参照 Section 4.2 正文，应指的是"至少一个系数反转"，建议在表题或脚注中澄清。

4. **Appendix 体量**：附录长达22页（第11-30页以及补充表格），与8页正文形成悬殊对比。虽然不违规，但 reviewer 可能质疑是否有核心内容被不当放入附录以规避页数限制。特别是 Algorithm 1（第30页）和 Table 4 correction results（第21页）arguably 属于正文内容。

5. **脚注1**（第4页）定义了 "four structural roles"（treatment, outcome-side covariate, selection variable, instrument）——这个分类与七种拓扑的对应关系可以更明确。

---

## 新颖性评估（核心任务）

### "First unified analysis" 声明评估
Introduction（第2页）声称 "We present the first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies in linear SEMs." 经核查：
- Carroll et al. (2006) 和 Gustafson (2004) 是 measurement error 的通用教科书，未专门分析 LLM 标注误差或多拓扑
- Brenner (1993) 处理 polytomous confounders 但仅限 confounding 拓扑
- Edwards et al. (2021) 讨论 misclassification 的双向偏差但未系统覆盖多拓扑
- Lee & Wood-Doughty (2024) 扩展到 categorical variables 和 LLM classifiers 但仅覆盖一种 DAG 拓扑
- Shi & Yin (2021b) 处理 misclassified covariates 但非多拓扑框架
- **结论**："first" 声明在当前文献范围内是成立的。将七种拓扑统一在同一分析框架下的确是新工作。但需注意这里的 "unified" 主要指"系统覆盖"而非"统一理论"——各拓扑的 bias expression 仍是逐一推导的。

### ASV 框架的创新层级
- ASV 本质上是 E-value 思想在 annotation error 参数空间的重新参数化（reparametrization），核心操作（沿参数路径寻找 tipping point）是敏感性分析的标准范式
- 拓扑依赖性是真正的新贡献：同一混淆矩阵在不同 DAG 下产生不同 ASV 值——这是 E-value 框架无法自然表达的
- Sign-flip ASV 作为新诊断量有独立价值
- **总体判断**：介于 reparametrization 和 structural innovation 之间。拓扑分层是实质贡献，但数学机制本身不是新的

### K≥3 Sign Reversal 的新颖性
- 这是论文最强的理论贡献。K=2 时 column-stochastic 矩阵不可能反转符号（代数约束），K≥3 时这一约束被打破——这是一个干净的、非平凡的数学洞察
- 83.4% 的 Dirichlet(1,1,1) 矩阵在 exposure 拓扑下产生 sign reversal 的数值结果令人印象深刻

### Correction Guidance 的新颖性
- 评估五种现有方法并非新方法提出
- FWL 不变性在四种拓扑下使矩阵校正无效——这是 FWL 定理的直接应用，新颖性在于"识别该定理在此场景的适用性"而非定理本身
- 作为"贡献"来说，更接近 empirical finding 而非 methodological contribution

---

## Related Work 覆盖度评估

### 已覆盖的关键领域
- ✅ Measurement error in causal inference: Carroll et al. (2006), Gustafson (2004), Bound et al. (2001), Schennach (2020)
- ✅ DAG-based misclassification: Hernán & Cole (2009), Brenner (1993), Edwards et al. (2021)
- ✅ LLM annotation quality: Gilardi et al. (2023), Ziems et al. (2024), Pangakis et al. (2023), Kim et al. (2025)
- ✅ Sensitivity analysis: VanderWeele & Ding (2017), Cinelli & Hazlett (2020), Ding & VanderWeele (2016)
- ✅ Correction methods: PPI++ (Angelopoulos et al. 2023), MC-SIMEX
- ✅ Causal NLP: Feder et al. (2022), Keith et al. (2020), Egami et al. (2022/2024), Pryzant et al. (2021)

### 可能遗漏的相关工作
1. **Jurek et al. (2005)** "Proper interpretation of non-differential misclassification effects: expectations vs observations" - 直接讨论 non-differential misclassification 的偏差方向问题，与本文 "beyond toward-null" 的核心主题高度相关
2. **Valeri & VanderWeele (2014)** 在 mediation analysis 中处理 measurement error 的方法论，与本文 mediation topology 相关
3. **Ogburn & VanderWeele (2012)** 关于 mediator misclassification 的偏差分析，对 mediation 和 front-door 拓扑有参考价值

这些遗漏不构成严重缺陷，但补充引用会加强 related work 的完整性，特别是 Jurek et al. (2005) 作为 "beyond toward-null" 议题的早期关键贡献。

---

## 格式合规检查

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 正文 ≤ 8页 | ✅ 通过 | 正文到第8页 Limitations 结束 |
| Abstract ≤ 200 words | ❌ 违规 | 245 words，超出 22.5% |
| Limitations section 合规 | ✅ 通过 | 仅讨论局限性，无新实验/图表 |
| 匿名规则 | ✅ 通过 | 标注 "Anonymous ACL submission"，未发现 de-anonymizing 信息 |
| 引用格式一致性 | ⚠️ 小问题 | 2条 bib 条目未被引用 (dawid1979, rosenbaum2002) |

---

## 主要优势

1. **理论贡献扎实且验证充分**：七种拓扑的 bias expression 推导清晰，MC 验证达到 1.6% MAPE（161个场景），解析-数值一致性令人信服（Section 4.2, Table 1）。

2. **K≥3 sign reversal 是非平凡且实用的发现**：证明了 K=2 的 "toward-null" 保证在 K≥3 时可以被打破，且在 exposure 和 IV 拓扑下确实发生——这对使用 LLM 标注进行因果研究的实践者有直接警示价值。

3. **经验验证有说服力**：使用 23 个真实 LLM 混淆矩阵（来自 HumAID、VAST、CivilComments）验证理论预测，Spearman rank correlation 和 MAPE 等多维度评估增强了可信度（Section 4.4）。

4. **拓扑脆弱性排序有实用价值**：IV（最脆弱）→ M-bias（免疫）的排序为研究设计提供了直接可操作的指导（Figure 3, Table 3）。

5. **FWL 不变性结果具有重要的负面贡献价值**：证明四种拓扑下矩阵校正方法在线性回归中可证明无效（Appendix B.2），引导实践者避免无效的校正策略。

6. **附录材料详尽**：22页附录包含完整证明、扩展实验、robustness checks、bootstrap CI 分析——reproducibility 和 transparency 表现优秀。


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

_source line 1380 · 2026-05-23T13:51:40.925590+00:00_

Reviewer 2 审稿报告已收到。记录关键发现：

**R2 核心问题**：
- **[N1 critical]** Abstract 245 words，超出 200 words 硬限——desk reject 风险
- **[N2 critical]** Correction Guidance 仅半页正文，与"三大贡献"定位不匹配
- **[W1]** ASV vs E-values 创新论证不充分
- **[W2]** Conjecture 1 K>3 单调性仅数值验证
- **[W3]** 计量经济学术语对 EMNLP 受众可达性偏低
- **[W4]** Sign reversal primary/secondary 区分不清
- **[W5]** 2 条 bib 未引用条目

**Overall**: 3.5/5 (Borderline Conference)

等待 Reviewer 1 报告返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 136

## Round 136

2 recorded events


### User

_source line 1381 · 2026-05-23T13:51:43.554106+00:00_

[Reviewer 2 审稿结果]:
审稿完成。报告已通过 `review_reviewer_post_to_director` 提交。

核心结论：**Overall 3.5（Borderline Conference）**。

主要发现：
- **Must-Fix**：Abstract 245 words 超出 200 上限（格式违规）；Correction Guidance 作为三大贡献之一仅半页正文，深度严重不足
- **Should-Fix**：ASV vs E-values 的创新论证偏弱（更像 reparametrization）；Conjecture 1 对 K>3 缺证明；术语密度对 EMNLP 读者不友好；sign reversal 的 primary/secondary coefficient 区分不清晰；2条 bib 孤立条目
- **优势**：K≥3 sign reversal 是非平凡发现、MC 验证充分（1.6% MAPE）、经验 LLM 矩阵验证有说服力、拓扑排序有实用价值

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

_source line 1382 · 2026-05-23T13:52:09.499888+00:00_

Reviewer 2 审稿报告已收到。关键发现已记录：

**R2 核心判断**：3.5/5（Borderline Conference）
- **2个 Must-Fix**：Abstract 超字数（245 vs 200 words）；Correction Guidance 深度不足
- **5个 Should-Fix**：ASV 创新论证不充分、Conjecture 1 缺证明、术语壁垒、sign reversal 表述歧义、bib 孤立条目
- **6项优势**：K≥3 sign reversal 非平凡、MC 验证充分、经验验证有说服力、拓扑排序实用、FWL 负面贡献有价值、附录详尽

等待 Reviewer 1 报告返回后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 137

## Round 137

6 recorded events


### User

_source line 1383 · 2026-05-23T13:52:16.648474+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性评估

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)

---

## Summary

本文研究 LLM 多类标注误差（K≥2）在七种典型 DAG 拓扑下如何传播到因果估计中。主要贡献包括：(1) 在线性 SEM 下推导了七种拓扑的 multi-class bias 解析表达式；(2) 证明了 K=2 时 bias envelope 的单调性（Theorem 1），并以数值验证将其推广为 K≥3 的 conjecture；(3) 定义了 Annotation Sensitivity Values (ASV) 作为诊断指标；(4) 提出了 topology-aware 的校正路由算法（Algorithm 1）。验证涵盖 161 个场景（23 LLM 配置 × 7 拓扑），MAPE 1.6%，以及 100,000 Dirichlet 混淆矩阵的 sign preservation 分析。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2 证明严谨；K≥3 仅为 conjecture，且 60-97% 矩阵违反严格单调性（虽然 magnitude ≤0.013）；线性 SEM 限制了泛化性 |
| Excitement | 3/5 | 问题重要且及时，但 NLP 实践者最需要的端到端实证验证缺失；框架偏理论化 |
| Reproducibility | 4/5 | 证明详尽，MC 参数明确，声称会发布代码；但部分验证（如 proportional effects 检验）依赖未公开的脚本 |
| Overall Assessment | 3.5 | Borderline Conference |
| Confidence | 4/5 | 熟悉因果推断与测量误差理论，仔细检查了主要证明 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] K≥3 理论缺口：Conjecture 1 的"ε-近似单调性"过于弱化

- 具体位置：Section 3.3 Conjecture 1, Table 10 (Appendix B.12)
- 问题：Theorem 1 仅证明 K=2 的 envelope monotonicity。对于 K≥3，论文退回到 Conjecture 1（ε-approximate monotonicity），但 Table 10 显示 **60-97% 的随机矩阵违反严格单调性**（confounding 90%，collider 97%，mediation 83%）。虽然 worst-case magnitude ≤0.013，但"几乎所有矩阵都违反单调性"与"单调性近似成立"之间存在表述上的张力。此外，验证仅在 **default DGP parameters** 下进行——改变 β、σ² 等参数后 conjecture 是否仍成立未知。10,000 个矩阵在 K=7 的 42 维自由参数空间中覆盖率极低。
- 为什么影响接收：ASV 框架的实用性（特别是 magnitude ASV 和 sign-flip ASV 的排序稳定性声称，Section 4.3）部分依赖 monotonicity。如果 K≥3 下单调性不可靠，ASV 的 topology vulnerability ranking 可能在特定 DGP 下失效。Reviewer 需要确认该 conjecture 对框架核心结论的影响边界。
- 建议修改方向：(1) 明确 Conjecture 1 失败时 ASV 结论的 robustness margin；(2) 在非 default DGP 参数下扩展验证（至少扫描 β 和 σ² 的典型范围）；(3) 考虑将 Conjecture 1 弱化为 "Empirical Observation"，避免暗示比实际更强的理论保证。

**N2** [critical] 缺乏端到端实证验证：confusion matrix estimation → ASV diagnosis → correction → improved estimates

- 具体位置：Section 4.4-4.5, Appendix B.3 (ClinicalBERT)
- 问题：论文的验证路径是：(a) 解析 bias 表达式 vs. MC 模拟（MAPE 1.6%）——这本质上是代数正确性自检；(b) 23 empirical LLM confusion matrices 的 bias ranking——验证了 topology 效应的定性模式；(c) 校正方法比较（Table 4）——仍是模拟数据。ClinicalBERT 案例（B.3）是最接近端到端验证的，但它是回溯性的（重新分析 Lee & Wood-Doughty 2022），且仅使用单一数据集、单一模型、单一拓扑（confounding）。**论文从未展示过完整链条**：在真实 NLP 任务上估计 C → 计算 ASV → 使用 Algorithm 1 选择校正方法 → 与 gold-label 因果估计对比 → 证明框架实际改善了估计质量。
- 为什么影响接收：EMNLP 读者需要实证证据表明该框架在 NLP 实践中有用，而非仅在模拟中正确。一个覆盖至少 2-3 种拓扑的端到端 case study 对论文的实际影响力至关重要。
- 建议修改方向：(1) 在 HumAID 或 VAST 上执行完整 pipeline：subsample gold labels → estimate C → run ASV → apply correction → compare corrected vs. gold-standard causal estimates；(2) 重点展示 Algorithm 1 的路由选择是否在实践中做出了正确的校正方法决策。

**N3** [critical] 线性 SEM 假设对 EMNLP 受众的适用性讨论不足

- 具体位置：Section 3.1, Appendix B.2 (FWL under logistic), Limitations
- 问题：整个理论框架建立在线性 SEM 之上。NLP 因果推断中最常用的模型是 logistic regression（二元结果）或 multinomial models。Table 5 (Appendix B.2) 显示逻辑回归下 FWL invariance 失效（|Δ_bias| < 0.02，最大 ~14 × 10⁻³），但论文仅验证了 FWL invariance 这一个维度——**bias 表达式本身在非线性模型下的有效性完全未检验**。主文仅在 Limitations 段用一句话提及 "linear SEMs"，Section 3.1 的开头也未充分说明该限制对 NLP 应用的含义。
- 为什么影响接收：如果 bias 表达式在 logistic regression 下大幅偏离，ASV 诊断和 Algorithm 1 的校正路由可能给出错误建议。EMNLP reviewer 会质疑该框架对 NLP 实践的相关性。
- 建议修改方向：(1) 在主文 Section 3.1 明确说明线性假设的范围和对 NLP 的含义；(2) 至少在一个拓扑下对比 linear vs. logistic regression 的 bias magnitude，量化非线性带来的偏差；(3) 在 Limitations 段更详细地讨论该限制。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Proportional effects 假设 (f = λg) 的可验证性和适用范围

- 具体位置：Theorem 1 条件, Appendix A.4, Appendix B.13
- 问题：Theorem 1 的核心条件 f = λg（误分类对 outcome 和 treatment 的效应成比例）在实践中不可直接验证。Appendix B.13 检查了 OOB 率随 departure from proportionality 的变化，发现 OOB 从 0%（δ=0.1）升至 ~40%（δ=1.0），sign failure < 1%。但论文未讨论：(a) 在什么 NLP 场景下 f ≈ λg 是合理的？(b) 研究者如何判断自己的数据是否满足该条件？(c) general case（非 proportional）下 Theorem 1 的退化行为——Observation 1 对 non-proportional effects 的覆盖是否充分？
- 建议：添加一个简短讨论段落说明 proportional effects 在典型 NLP 因果推断场景中的合理性（或不合理性），并提供检验该假设的经验指南。

**W2** [warning] Non-differential misclassification 假设的 stress test 局限性

- 具体位置：Definition 1 (Section 3.1), Appendix B.5-B.6
- 问题：Definition 1 要求 P(A*=j|A=k,Y,Z) = P(A*=j|A=k)——误分类不依赖于结局 Y。论文以"LLM 分类时不观察 Y"为由辩护，并在 B.5 用 VAST 的 topic-stratified CM 验证。但在 NLP 中，Y 经常嵌入在与 A 相同的文本中：例如分析 stance (A) 对政策影响 (Y) 的因果效应时，LLM 可能因文本中 Y 的信号而改变对 A 的分类准确度——产生隐性 differential misclassification。Stress test 仅用 5 个 VAST topics（≤29 per-topic samples），且只检查了 uniform perturbation，未考虑 Y-dependent 的系统性偏差模式。
- 建议：(1) 在主文讨论 NLP 场景中 differential misclassification 的潜在来源（text-mediated Y→classification 路径）；(2) 扩展 stress test 到 Y-correlated perturbation 模式。

**W3** [warning] 23 LLM 配置的代表性

- 具体位置：Section 4.2, 4.4
- 问题：经验验证仅使用 4 个 LLM × 3 数据集 = 23 配置。当前 LLM 标注实践涵盖 GPT-4、Claude、Llama、Gemma 等多样化模型，其 confusion matrix 结构可能差异显著（例如 GPT-4 vs. 开源小模型的 off-diagonal 分布模式）。23 配置是否足以支撑 "under realistic LLM accuracy" 的普适性声称？
- 建议：(1) 讨论 23 配置的 confusion matrix 多样性（对角优势度范围、off-diagonal 对称性等）；(2) 如有条件，补充更多模型或数据集的验证。

**W4** [warning] Proposition 1(b) collider sign preservation 仅有经验验证

- 具体位置：Proposition 1(b), Table 2 (Appendix A.9), Appendix A.6
- 问题：Table 2 总结 sign preservation conditions 时，collider 的验证状态标记为 "Empirical"（Cauchy-Schwarz bound 或 Berkson attenuation），而 confounding/mediation/M-bias/front-door 均有代数证明。对于 Proposition 1 宣称的统一 sign preservation 框架，collider 的理论缺口削弱了整体严谨性。
- 建议：要么补充 collider 的代数证明，要么在 Proposition 1 中明确标注哪些 sub-claims 是 proved vs. numerically verified。

---

## 小问题（不影响接收）

- **M1**: Abstract 第 200 词限制——当前 abstract 接近但似乎在限制内，建议作者自查确认。
- **M2**: Figure 2 (page 6) 的 histogram 标注 "Red = sign reversal" 但在灰度打印下难以区分。建议使用 hatching pattern 而非仅颜色区分。
- **M3**: Algorithm 1 (page 30) 中 Step 2 的 "RMSE red. < 0.02" 阈值来源未说明——这是经验选择还是理论导出？
- **M4**: Table 1 中 "Cond." 列的含义在 caption 中解释不够充分，首次出现时应展开说明 conditional guarantee 的具体条件。
- **M5**: Remark 1 (page 6) 区分 ASV 与 E-values 是重要澄清，但仅用一个 Remark 可能不够——建议在 Section 3.3 开头更明确地定位 ASV 与已有 sensitivity analysis 工具（E-values, Robustness values）的关系。

---

## Questions for Authors

1. **Conjecture 1 的 DGP 敏感性**：当 β 从 default 值显著偏离（如 |β| > 5 或接近 0）时，ε-approximate monotonicity 是否仍然成立？是否有反例？

2. **非线性扩展的可行性**：如果将 linear SEM 替换为 logistic regression，bias 表达式的解析推导是否可能？还是只能依赖 MC simulation？作者是否考虑过提供 logistic 下的数值 bias envelope？

3. **Algorithm 1 的实际使用场景**：在实践中，研究者如何确定自己的 DAG 拓扑？Algorithm 1 的 input 要求研究者已经知道正确的 DAG——这对 NLP 因果推断新手是否构成使用门槛？

4. **Correction 方法的 gold label 需求**：Table 4 和 Section 4.5 显示 PPI++ 是多数拓扑下的最优校正方法，但 PPI++ 需要 gold labels。在 gold labels 不可用的场景下（这恰恰是使用 LLM 标注的主要动机），框架推荐什么？MC-SIMEX 是否在所有拓扑下都足够好？

5. **关于 "secondary coefficient" 的 sign reversal**：Abstract 提到 "sign reversal of secondary coefficients"，但 primary treatment coefficient 在 exposure 下也可能 reverse？还是 sign reversal 仅限于 secondary coefficients？请澄清。

---

## Missing References

- **Logistic regression 下的测量误差**：Stefanski & Carroll (1985) "Covariate Measurement Error in Logistic Regression" 和 Küchenhoff et al. (2006) "General Regression Calibration" 等非线性测量误差经典文献可以帮助论证 linear assumption 的边界。
- **LLM annotation quality 综述**：Tan et al. (2024) 的 LLM annotation survey 可能提供更全面的 confusion matrix 多样性参考。
- **Sensitivity analysis 工具对比**：Cinelli & Hazlett (2020) 的 robustness value 已被引用，但 Oster (2019) "Unobservable Selection and Coefficient Stability" 也与 ASV 的 sensitivity 思路直接相关。

---

## 主要优势

1. **系统性贡献**：首次统一分析 multi-class annotation error 在 7 种 DAG 拓扑下的传播，填补了重要的理论空白（prior work 仅覆盖 1-2 种拓扑，且多限于 K=2）。

2. **K=2 理论严谨**：Theorem 1 的证明使用 perspective function convexity 方法，手法巧妙且正确。Proposition 2-6 的拓扑特定 sign preservation 证明详尽。

3. **实用诊断工具**：ASV 的三维分解（magnitude, significance, sign-flip）提供了直观且可操作的风险评估框架。Algorithm 1 的 topology-aware routing 是有价值的实践指南。

4. **验证覆盖度**：161 scenarios 的 theory-MC agreement（MAPE 1.6%）、100,000 Dirichlet 矩阵的 sign preservation 分析、以及 empirical LLM CM 验证构成了多层次的 internal validation。

5. **Presentation**：论文组织清晰，主文保持了可读性，将大量技术细节合理地移入附录。Figure 1 的 DAG taxonomy 和 Figure 3 的 ASV spectrum 是有效的可视化。

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)

**一句话总结**: 系统性地分析了 multi-class annotation error 在因果推断中的拓扑依赖性传播，K=2 理论严谨，但 K≥3 仅为数值 conjecture、线性 SEM 限制显著、且缺乏端到端实证验证，使其对 EMNLP 受众的实际影响力不确定。

**置信度**: 4/5（熟悉因果推断与测量误差理论，逐页检查了主要证明和附录）


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

_source line 1384 · 2026-05-23T13:53:27.819858+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉审阅任务\n\n以下是 **Reviewer 2（新颖性与完整性评估）** 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：反驳该观点，并提供具体证据（cite 具体 Section/Table/Figure/Appendix）\n\n请特别关注以下几个你和 Reviewer 2 可能有分歧的点：\n1. R2-N1：Abstract 245 words 超出 200 上限——你在 M1 中也提及但仅列为 minor，请重新评估严重程度\n2. R2-N2：Correction Guidance 深度不足——你是否同意这构成 must-fix？\n3. R2-W1：ASV vs E-values 的创新论证——你如何评估 ASV 的方法论新颖性？\n4. R2-W5：2条未引用 bib 条目——你是否在审阅中注意到同样的问题？\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 4 / 5 (Strong)\n**Excitement**: 3 / 5 (Interesting)\n**Confidence**: 4 / 5 (Quite sure)\n\n**一句话总结**: 理论工作扎实、MC验证充分，但 abstract 超字数限制（245 vs 200 words）为硬伤格式违规，correction guidance 作为三大贡献之一深度不足，ASV 相对于 E-values 的结构性创新论证不够充分。\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 超过 200 words 限制\n- 当前 abstract 约 245 words，超出 EMNLP 2026 规定的 200 words 上限约 22.5%。逐字统计确认：从 \"Large language models\" 到 \"LLM-generated annotations\" 共 245 词。\n- 为什么影响接收：这是 EMNLP 2026 的硬性格式要求，desk reject 风险。ARR submission form 明确限制 abstract 不超过 200 words。\n- 建议修改方向：精简到 3-4 核心信息点，删除具体数值和次要拓扑的逐一列举。\n\n**N2** [critical] Correction Guidance 深度与\"三大贡献\"定位不匹配\n- Introduction 将 \"topology-aware correction guidance\" 列为三大贡献之一，但正文 Section 4.5 仅约半页。Algorithm 1 只出现在附录第30页。五种方法选择标准未在主文讨论，缺计算成本对比。\n- 建议：要么将 Algorithm 1 移入正文、增加方法选择讨论，要么降低贡献定位。\n\n### Should-Fix 问题\n\n**W1** ASV 相对于 E-values 的方法论创新论证不充分\n- Remark 1 给出三点区分主要是应用域差异和参数化差异，而非方法论结构创新。核心数学操作——沿参数路径 C(δ) 计算 plim 达到阈值的最小 δ——本质上是敏感性分析的标准 \"tipping point\" 方法。\n- 建议：增加具体例子展示 ASV 的拓扑分层能力在 E-value 框架下无法自然实现。\n\n**W2** Conjecture 1 对 K>3 的一般单调性缺少证明\n- 10,000 个矩阵的数值验证无法替代证明——可能存在 measure-zero 的反例集合。ASV 的 vulnerability ranking 依赖于此单调性。\n- 建议：明确标注为 open problem，增加反例搜索描述，讨论失败对应用的影响。\n\n**W3** EMNLP 受众可达性偏低\n- plim、FWL theorem、Wald estimator、column-stochastic、Birkhoff polytope、Dirichlet prior 等术语对 NLP 读者壁垒过高。\n- 建议：增加直觉解释，将 Birkhoff polytope 替换为更直观描述。\n\n**W4** \"Sign reversal\" 的 primary vs secondary coefficient 区分不清晰\n- Abstract 中 \"secondary coefficients\" 首次出现时没有定义。\"primary coefficient never reverses\" 这一关键信息未出现在 abstract 中。\n- 建议：在 abstract 中明确 secondary 含义或改用更直观表述。\n\n**W5** Bib 存在 2 条未引用条目\n- dawid1979 和 rosenbaum2002 在 bib 中存在但正文未引用。\n- 建议：要么引用，要么移除。\n\n### 小问题\n1. Figure 2 信息密度：7子图略显拥挤，颜色方案灰度打印下难区分\n2. Figure 1 starred-node convention 仅在 caption 中解释\n3. Table 1 \"Sign Flip\" 列具体含义未在表题中明确\n4. Appendix 22页 vs 正文8页的悬殊比例\n5. 脚注1的 four structural roles 与七种拓扑对应关系可更明确\n\n### 新颖性评估\n- \"First unified analysis\" 声明在当前文献范围内成立，但 \"unified\" 主要指系统覆盖而非统一理论\n- ASV 介于 reparametrization 和 structural innovation 之间\n- K≥3 Sign Reversal 是论文最强理论贡献\n- Correction Guidance 更接近 empirical finding 而非 methodological contribution\n\n### Related Work 覆盖度\n- 可能遗漏：Jurek et al. (2005)（与 \"beyond toward-null\" 核心主题高度相关）、Valeri & VanderWeele (2014)、Ogburn & VanderWeele (2012)\n\n### 格式合规\n- 正文 ≤ 8页：✅ 通过\n- Abstract ≤ 200 words：❌ 违规（245 words）\n- Limitations section：✅ 合规\n- 匿名规则：✅ 通过\n\n### 主要优势\n1. 理论贡献扎实且验证充分（1.6% MAPE）\n2. K≥3 sign reversal 是非平凡实用发现\n3. 经验 LLM 矩阵验证有说服力\n4. 拓扑脆弱性排序有实用价值\n5. FWL 不变性负面结果有价值\n6. 附录材料详尽",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
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
    "text": "## 交叉审阅任务\n\n以下是 **Reviewer 2（新颖性与完整性评估）** 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：反驳该观点，并提供具体证据（cite 具体 Section/Table/Figure/Appendix）\n\n请特别关注以下几个你和 Reviewer 2 可能有分歧的点：\n1. R2-N1：Abstract 245 words 超出 200 上限——你在 M1 中也提及但仅列为 minor，请重新评估严重程度\n2. R2-N2：Correction Guidance 深度不足——你是否同意这构成 must-fix？\n3. R2-W1：ASV vs E-values 的创新论证——你如何评估 ASV 的方法论新颖性？\n4. R2-W5：2条未引用 bib 条目——你是否在审阅中注意到同样的问题？\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 4 / 5 (Strong)\n**Excitement**: 3 / 5 (Interesting)\n**Confidence**: 4 / 5 (Quite sure)\n\n**一句话总结**: 理论工作扎实、MC验证充分，但 abstract 超字数限制（245 vs 200 words）为硬伤格式违规，correction guidance 作为三大贡献之一深度不足，ASV 相对于 E-values 的结构性创新论证不够充分。\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 超过 200 words 限制\n- 当前 abstract 约 245 words，超出 EMNLP 2026 规定的 200 words 上限约 22.5%。逐字统计确认：从 \"Large language models\" 到 \"LLM-generated annotations\" 共 245 词。\n- 为什么影响接收：这是 EMNLP 2026 的硬性格式要求，desk reject 风险。ARR submission form 明确限制 abstract 不超过 200 words。\n- 建议修改方向：精简到 3-4 核心信息点，删除具体数值和次要拓扑的逐一列举。\n\n**N2** [critical] Correction Guidance 深度与\"三大贡献\"定位不匹配\n- Introduction 将 \"topology-aware correction guidance\" 列为三大贡献之一，但正文 Section 4.5 仅约半页。Algorithm 1 只出现在附录第30页。五种方法选择标准未在主文讨论，缺计算成本对比。\n- 建议：要么将 Algorithm 1 移入正文、增加方法选择讨论，要么降低贡献定位。\n\n### Should-Fix 问题\n\n**W1** ASV 相对于 E-values 的方法论创新论证不充分\n- Remark 1 给出三点区分主要是应用域差异和参数化差异，而非方法论结构创新。核心数学操作——沿参数路径 C(δ) 计算 plim 达到阈值的最小 δ——本质上是敏感性分析的标准 \"tipping point\" 方法。\n- 建议：增加具体例子展示 ASV 的拓扑分层能力在 E-value 框架下无法自然实现。\n\n**W2** Conjecture 1 对 K>3 的一般单调性缺少证明\n- 10,000 个矩阵的数值验证无法替代证明——可能存在 measure-zero 的反例集合。ASV 的 vulnerability ranking 依赖于此单调性。\n- 建议：明确标注为 open problem，增加反例搜索描述，讨论失败对应用的影响。\n\n**W3** EMNLP 受众可达性偏低\n- plim、FWL theorem、Wald estimator、column-stochastic、Birkhoff polytope、Dirichlet prior 等术语对 NLP 读者壁垒过高。\n- 建议：增加直觉解释，将 Birkhoff polytope 替换为更直观描述。\n\n**W4** \"Sign reversal\" 的 primary vs secondary coefficient 区分不清晰\n- Abstract 中 \"secondary coefficients\" 首次出现时没有定义。\"primary coefficient never reverses\" 这一关键信息未出现在 abstract 中。\n- 建议：在 abstract 中明确 secondary 含义或改用更直观表述。\n\n**W5** Bib 存在 2 条未引用条目\n- dawid1979 和 rosenbaum2002 在 bib 中存在但正文未引用。\n- 建议：要么引用，要么移除。\n\n### 小问题\n1. Figure 2 信息密度：7子图略显拥挤，颜色方案灰度打印下难区分\n2. Figure 1 starred-node convention 仅在 caption 中解释\n3. Table 1 \"Sign Flip\" 列具体含义未在表题中明确\n4. Appendix 22页 vs 正文8页的悬殊比例\n5. 脚注1的 four structural roles 与七种拓扑对应关系可更明确\n\n### 新颖性评估\n- \"First unified analysis\" 声明在当前文献范围内成立，但 \"unified\" 主要指系统覆盖而非统一理论\n- ASV 介于 reparametrization 和 structural innovation 之间\n- K≥3 Sign Reversal 是论文最强理论贡献\n- Correction Guidance 更接近 empirical finding 而非 methodological contribution\n\n### Related Work 覆盖度\n- 可能遗漏：Jurek et al. (2005)（与 \"beyond toward-null\" 核心主题高度相关）、Valeri & VanderWeele (2014)、Ogburn & VanderWeele (2012)\n\n### 格式合规\n- 正文 ≤ 8页：✅ 通过\n- Abstract ≤ 200 words：❌ 违规（245 words）\n- Limitations section：✅ 合规\n- 匿名规则：✅ 通过\n\n### 主要优势\n1. 理论贡献扎实且验证充分（1.6% MAPE）\n2. K≥3 sign reversal 是非平凡实用发现\n3. 经验 LLM 矩阵验证有说服力\n4. 拓扑脆弱性排序有实用价值\n5. FWL 不变性负面结果有价值\n6. 附录材料详尽",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-23T13:54:07.131129+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 39311
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-23T13:54:07.633834+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉审阅任务\n\n以下是 **Reviewer 1（方法严谨性评估）** 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：反驳该观点，并提供具体证据（cite 具体 Section/Table/Figure/Appendix）\n\n请特别关注以下几个你和 Reviewer 1 可能有分歧的点：\n1. R1-N2：缺乏端到端实证验证——你在初审中未将此列为独立 must-fix，请重新评估\n2. R1-N3：线性 SEM 假设讨论不足——你如何评估此问题对 EMNLP 受众的影响？\n3. R1-W1：Proportional effects 假设——你是否同意这比 ASV novelty 更重要？\n4. R1-W4：Collider sign preservation 仅有经验验证——你是否注意到此理论缺口？\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**Soundness**: 3.5/5\n**Excitement**: 3/5\n**Reproducibility**: 4/5\n**Confidence**: 4/5\n\n**一句话总结**: 系统性地分析了 multi-class annotation error 在因果推断中的拓扑依赖性传播，K=2 理论严谨，但 K≥3 仅为数值 conjecture、线性 SEM 限制显著、且缺乏端到端实证验证，使其对 EMNLP 受众的实际影响力不确定。\n\n### Must-Fix 问题\n\n**N1** [critical] K≥3 理论缺口：Conjecture 1 的\"ε-近似单调性\"过于弱化\n- Theorem 1 仅证明 K=2。Table 10 显示 60-97% 随机矩阵违反严格单调性（worst-case ≤0.013）。验证仅在 default DGP parameters 下进行。10,000 矩阵在 K=7 的 42 维空间覆盖率极低。\n- 建议：明确 Conjecture 1 失败时 ASV 结论的 robustness margin；在非 default DGP 参数下扩展验证；考虑弱化为 \"Empirical Observation\"。\n\n**N2** [critical] 缺乏端到端实证验证：C estimation → ASV diagnosis → correction → improved estimates\n- 验证路径本质上是代数正确性自检（theory vs MC）和定性模式验证（topology effects）。ClinicalBERT 案例仅覆盖单一拓扑。论文从未展示过完整链条：在真实 NLP 任务上估计 C → 计算 ASV → Algorithm 1 选择校正 → 对比 gold-label 因果估计。\n- 建议：在 HumAID/VAST 上执行完整 pipeline，展示 Algorithm 1 路由选择是否正确。\n\n**N3** [critical] 线性 SEM 假设对 EMNLP 受众的适用性讨论不足\n- NLP 因果推断最常用 logistic regression。Appendix B.2 仅验证 FWL invariance 维度，bias 表达式在非线性模型下有效性完全未检验。主文 Limitations 仅一句话提及。\n- 建议：在主文明确线性假设的范围；至少对比一个拓扑下 linear vs. logistic bias magnitude。\n\n### Should-Fix 问题\n\n**W1** Proportional effects 假设 (f = λg) 的可验证性和适用范围\n- Theorem 1 核心条件在实践中不可直接验证。论文未讨论在什么 NLP 场景下合理，研究者如何判断数据是否满足，general case 退化行为。\n- 建议：添加讨论段落说明 proportional effects 在 NLP 场景中的合理性。\n\n**W2** Non-differential misclassification 假设的 stress test 局限性\n- NLP 中 Y 经常嵌入在与 A 相同的文本中，可能产生隐性 differential misclassification。Stress test 仅5个 VAST topics（≤29 per-topic samples），只检查 uniform perturbation。\n- 建议：讨论 NLP 中 differential misclassification 潜在来源，扩展 stress test。\n\n**W3** 23 LLM 配置的代表性\n- 4 LLM × 3 数据集 = 23 配置。缺 GPT-4、Claude 等主流商业模型。\n- 建议：讨论配置多样性或补充验证。\n\n**W4** Proposition 1(b) collider sign preservation 仅有经验验证\n- Table 2 中 collider 标记为 \"Empirical\"，而其他拓扑有代数证明。削弱 Proposition 1 统一框架的严谨性。\n- 建议：补充代数证明或明确标注 proved vs. verified。\n\n### 小问题\n- M1: Abstract 接近 200 词限制，建议自查\n- M2: Figure 2 灰度打印下 sign reversal 标记难区分\n- M3: Algorithm 1 Step 2 \"RMSE red. < 0.02\" 阈值来源未说明\n- M4: Table 1 \"Cond.\" 列含义解释不够\n- M5: Remark 1 对 ASV vs E-values 定位可能不够\n\n### Questions for Authors\n1. Conjecture 1 的 DGP 敏感性（β 偏离 default 时）\n2. 非线性扩展的可行性（logistic 下是否有解析推导）\n3. Algorithm 1 使用门槛（研究者如何确定 DAG 拓扑）\n4. Gold labels 不可用时的推荐（PPI++ 的替代）\n5. Primary vs secondary coefficient sign reversal 的澄清\n\n### Missing References\n- Stefanski & Carroll (1985) logistic regression 测量误差\n- Tan et al. (2024) LLM annotation survey\n- Oster (2019) coefficient stability\n\n### 主要优势\n1. 首次统一分析 multi-class annotation error 在 7 种 DAG 拓扑下的传播\n2. K=2 理论严谨（perspective function convexity）\n3. ASV 三维分解提供可操作风险评估框架\n4. 161 scenarios 多层次验证（1.6% MAPE）\n5. 论文组织清晰，Figure 1 和 Figure 3 有效",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
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
    "text": "## 交叉审阅任务\n\n以下是 **Reviewer 1（方法严谨性评估）** 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：反驳该观点，并提供具体证据（cite 具体 Section/Table/Figure/Appendix）\n\n请特别关注以下几个你和 Reviewer 1 可能有分歧的点：\n1. R1-N2：缺乏端到端实证验证——你在初审中未将此列为独立 must-fix，请重新评估\n2. R1-N3：线性 SEM 假设讨论不足——你如何评估此问题对 EMNLP 受众的影响？\n3. R1-W1：Proportional effects 假设——你是否同意这比 ASV novelty 更重要？\n4. R1-W4：Collider sign preservation 仅有经验验证——你是否注意到此理论缺口？\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**Soundness**: 3.5/5\n**Excitement**: 3/5\n**Reproducibility**: 4/5\n**Confidence**: 4/5\n\n**一句话总结**: 系统性地分析了 multi-class annotation error 在因果推断中的拓扑依赖性传播，K=2 理论严谨，但 K≥3 仅为数值 conjecture、线性 SEM 限制显著、且缺乏端到端实证验证，使其对 EMNLP 受众的实际影响力不确定。\n\n### Must-Fix 问题\n\n**N1** [critical] K≥3 理论缺口：Conjecture 1 的\"ε-近似单调性\"过于弱化\n- Theorem 1 仅证明 K=2。Table 10 显示 60-97% 随机矩阵违反严格单调性（worst-case ≤0.013）。验证仅在 default DGP parameters 下进行。10,000 矩阵在 K=7 的 42 维空间覆盖率极低。\n- 建议：明确 Conjecture 1 失败时 ASV 结论的 robustness margin；在非 default DGP 参数下扩展验证；考虑弱化为 \"Empirical Observation\"。\n\n**N2** [critical] 缺乏端到端实证验证：C estimation → ASV diagnosis → correction → improved estimates\n- 验证路径本质上是代数正确性自检（theory vs MC）和定性模式验证（topology effects）。ClinicalBERT 案例仅覆盖单一拓扑。论文从未展示过完整链条：在真实 NLP 任务上估计 C → 计算 ASV → Algorithm 1 选择校正 → 对比 gold-label 因果估计。\n- 建议：在 HumAID/VAST 上执行完整 pipeline，展示 Algorithm 1 路由选择是否正确。\n\n**N3** [critical] 线性 SEM 假设对 EMNLP 受众的适用性讨论不足\n- NLP 因果推断最常用 logistic regression。Appendix B.2 仅验证 FWL invariance 维度，bias 表达式在非线性模型下有效性完全未检验。主文 Limitations 仅一句话提及。\n- 建议：在主文明确线性假设的范围；至少对比一个拓扑下 linear vs. logistic bias magnitude。\n\n### Should-Fix 问题\n\n**W1** Proportional effects 假设 (f = λg) 的可验证性和适用范围\n- Theorem 1 核心条件在实践中不可直接验证。论文未讨论在什么 NLP 场景下合理，研究者如何判断数据是否满足，general case 退化行为。\n- 建议：添加讨论段落说明 proportional effects 在 NLP 场景中的合理性。\n\n**W2** Non-differential misclassification 假设的 stress test 局限性\n- NLP 中 Y 经常嵌入在与 A 相同的文本中，可能产生隐性 differential misclassification。Stress test 仅5个 VAST topics（≤29 per-topic samples），只检查 uniform perturbation。\n- 建议：讨论 NLP 中 differential misclassification 潜在来源，扩展 stress test。\n\n**W3** 23 LLM 配置的代表性\n- 4 LLM × 3 数据集 = 23 配置。缺 GPT-4、Claude 等主流商业模型。\n- 建议：讨论配置多样性或补充验证。\n\n**W4** Proposition 1(b) collider sign preservation 仅有经验验证\n- Table 2 中 collider 标记为 \"Empirical\"，而其他拓扑有代数证明。削弱 Proposition 1 统一框架的严谨性。\n- 建议：补充代数证明或明确标注 proved vs. verified。\n\n### 小问题\n- M1: Abstract 接近 200 词限制，建议自查\n- M2: Figure 2 灰度打印下 sign reversal 标记难区分\n- M3: Algorithm 1 Step 2 \"RMSE red. < 0.02\" 阈值来源未说明\n- M4: Table 1 \"Cond.\" 列含义解释不够\n- M5: Remark 1 对 ASV vs E-values 定位可能不够\n\n### Questions for Authors\n1. Conjecture 1 的 DGP 敏感性（β 偏离 default 时）\n2. 非线性扩展的可行性（logistic 下是否有解析推导）\n3. Algorithm 1 使用门槛（研究者如何确定 DAG 拓扑）\n4. Gold labels 不可用时的推荐（PPI++ 的替代）\n5. Primary vs secondary coefficient sign reversal 的澄清\n\n### Missing References\n- Stefanski & Carroll (1985) logistic regression 测量误差\n- Tan et al. (2024) LLM annotation survey\n- Oster (2019) coefficient stability\n\n### 主要优势\n1. 首次统一分析 multi-class annotation error 在 7 种 DAG 拓扑下的传播\n2. K=2 理论严谨（perspective function convexity）\n3. ASV 三维分解提供可操作风险评估框架\n4. 161 scenarios 多层次验证（1.6% MAPE）\n5. 论文组织清晰，Figure 1 和 Figure 3 有效",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-23T13:54:09.142875+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1509
}
```

</details>

---


### Assistant

_source line 1388 · 2026-05-23T13:54:12.699536+00:00_

交叉分享已发送。两位 Reviewer 正在审阅对方的完整审稿意见并准备逐条回应。等待交叉回应返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 138

## Round 138

2 recorded events
