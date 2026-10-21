# Director coordination — Part 7 of 8

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../director-coordination.md) · [Part 8 →](part-008.md) · [Structured JSON](../../../sessions/1d/1de11abfd142608a2277.json)

## Round 164

### Tool call

_source line 1666 · 2026-05-23T18:48:23.037867+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 20\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix（低优先级）。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 再提 Dirichlet 采样代表性。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Limitations 已覆盖。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。Limitations 已覆盖。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 20\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出，R18 修复充分。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 两位 Reviewer 再次提出（R1-W3, R2-W4）：主文 Section 3.1 仅简短提及，B.25 的 content-dependent proxy 违反结果（12/12 rejections for topic）未在主文讨论。要求在主文增加 2-3 句讨论实践合理性和验证策略。共识 should-fix。\"\n    resolution: \"R18 三管齐下修复（architectural invariant + Y-stratified test + stress test）。R20 要求进一步前置到主文。\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 19\n    resolution: \"R18 压缩后编译验证 main text ≤8 pages。R19 PDF 确认合规。连续两轮无复发。\"\n    resolution_round: 19\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: minor\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1 联合。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提（Abstract 187 words 合规，但 7+ 数字密度高）。R1 未单独提出。共识 minor。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。R2 仅在 minor M1 提及 abstract 字数边界。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: must-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据——缺少端到端因果应用验证\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。Limitations 中已承认。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 升级为 critical。R2 列为唯一 Must-Fix（N1）：声称对 practitioner 有指导意义但无端到端 demo（annotate→estimate→correct）。R1 列为 W2（should-fix）：缺乏 ground-truth causal effect 的端到端验��。共识：对 EMNLP 应用导向 venue 影响接收。建议至少一个 text-as-treatment 数据集走完全流程。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: Remark 1 重写为 complementary tools。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提：ASV 与 E-value 范式相似，方法论新颖性有限。R1 认为 ASV 有实用价值但同意理论创新不高。共识 should-fix。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W5 再提：ASV 与 E-values 区分度论证不够锐利，建议增加 'Why not E-values?' 讨论。R1 未单独提出但在优势中肯定 ASV 设计合理。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加��关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: must-fix\n    summary: \"Proportional effects 假设在 NLP 中是强限制，且 Limitations 中完全缺失\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 增加 stance detection/sentiment analysis 场景讨论 + 97.3% empirical compliance。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位 Reviewer 再提。R1: f,g 不可观测，97.3% 检验方法和标准不透明，OOB 率 23%。R2: 同意。共识 should-fix（高优先级）。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 升级为 critical（N1）：Proportional effects 是两个核心定理的关键前提，但 Limitations 中完全缺失。B.13 Table 14 显示 non-proportional 下 OOB rate 84.6%、sign preservation 降至 75.5%。建议：(1) Limitations 明确列出；(2) Section 3.2 加 scope caveat；(3) 引用 Table 14 数据。R2 未单独列出但在 W1 中间接触及（单调性假设条件过强）。\"\n    action_items:\n      - round: 19\n        action: \"SF-2 fix: 97.3% wording corrected to distinguish proportional vs non-proportional sign preservation rate\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem/Conjecture 边界在主文中模糊\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 must-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 2 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位再次列为 critical。MF-1a/1b/1c actions completed（adversarial test + Theorem 2 + framing chain）。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 再次提出。R1-N2（critical）：Theorem 1→Theorem 2→Conjecture 1 连续呈现，'已证明'与'数值猜测'边界不清。adversarial search 结构类型手动选择，无法排除未覆盖病态结构。R2-W1（should-fix）：Abstract 语气过于确定（'yielding a vulnerability ranking'），读者可能误以为已证结论。共识：need clearer delineation of proof vs conjecture boundary。\"\n    action_items:\n      - round: 19\n        action: \"MF-1a: Adversarial monotonicity test — 545,945 curves, max ε=0.016\"\n        assigned_to: agent\n        status: done\n      - round: 19\n        action: \"MF-1b: Theorem 2 (K=3 symmetric monotonicity) proof added\"\n        assigned_to: agent\n        status: done\n      - round: 19\n        action: \"MF-1c: Framing chain in method.tex\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。SF-2 fix applied。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"与 R6-M3 合并。R20 R1-N1 升级为 critical。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"与 R4-W6 合并。R2-W5 再提 ASV 与 E-values 区分度。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 NEW-1。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 NEW-1。R19 ���单独提出。连续两轮未提出，R18 修复充分。\"\n    resolution: \"随 NEW-1 一同解决。\"\n    resolution_round: 19\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 18\n    resolution: \"连续五轮（R14-R18）未被任何 Reviewer 提出，视为已解决。\"\n    resolution_round: 18\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: §4.5 扩展 logistic 讨论。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: Abstract + Conclusion linear SEM qualifier added。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W2 再提：FWL 不变性在 logistic 下部分失效意味着矩阵校正方法在非线性场景可能有效——论文对此讨论不足。建议在 Limitations 增加线性→非线性推广段。R1 未单独提出但间接认可。共识 should-fix。\"\n    action_items:\n      - round: 19\n        action: \"Abstract + Conclusion linear SEM qualifier added\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 确认 'first unified analysis' 在当前文献范围内成立。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 限定词简化。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 fix: 改为 'first multi-class (K≥3) topology-specific analysis'。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W3 再提：Brenner (1993) 已有 polytomous confounder 分析���Lee & Wood-Doughty (2024) 有 K≥3 confounding。建议改为 'first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies'。R1 未单独提出。共识 should-fix（低优先级）。\"\n    action_items:\n      - round: 19\n        action: \"SF-5 fix: introduction.tex 改为 'first multi-class (K≥3) topology-specific analysis'\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 R1-W3。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 R1-W3。R19 未单独提出。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: minor\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: column-stochastic 括号说明已加入。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: FWL, Wald inline explanations added。共识 minor。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 小问题 #2：notation density 高（p.3-4 一页内引入大量符号），Table 26 出现太晚。���议主文早期引用。R2 小问题 M5 提术语一致性。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 minor。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 R1 提 x 轴 scale 差异大。minor。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 R1 小问题 #1 caption 颜色含义不明确；R2 M3 信息密度过高建议仅保留 3 个拓扑在主文。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"两位共识。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。连续三轮未提出。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: 随 R9-C2 一同修复。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出��R19 fix 生效。\"\n    action_items:\n      - round: 19\n        action: \"随 R9-C2 一同修复：Abstract + Conclusion linear SEM qualifier\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 fix: primary coefficient hedge + sampling method note added。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。R19 fix 生效。\"\n    action_items:\n      - round: 19\n        action: \"Q5 fix: primary coefficient hedge + sampling note added\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 3 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: FWL 降为 Observation，Contribution 3 重聚焦于 correction routing 实证发现。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1-W4 再提 Algorithm 1 阈值缺乏理论依据：决策阈值来自特定模拟设置的经验平均，未验证跨 K/DGP 参数稳定性。建议报告不同 K 下性能或明确定位为启发式指南。R2 Q1 间接提及（DAG 不确定性下 Algorithm 1 的 sensitivity）。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words by 3 counting methods. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。Theorem 2 现为 collider 提供 K=3 symmetric 理论证明。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。连续三轮未提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"dawid1979, rosenbaum2002 未引用。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: 3 orphans removed。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 fix: 5 new orphans removed。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。连续一轮未提出。\"\n\n  # === Round 20 新发现 ===\n\n  - id: R20-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中很少成立——缺少合理性讨论和经验量化\"\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [R1]\n        note: \"R1-W1：真实 LLM confusion matrix 通常高度不对称（如 positive-neutral 混淆远多于 positive-negative）。论文未报告 23 个经验矩阵中有多少满足或近似满足对称性，也未讨论 Theorem 2 对轻微不对称的鲁棒性。建议量化对称性偏离程度（Frobenius distance to nearest symmetric matrix）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R20-N2\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 决策阈值缺乏理论依据和跨设置稳定性验证\"\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R1-W4: 阈值来自特定模拟设置（K=3, Dirichlet），未验证对不同 K/DGP/N 的稳定性。R2-Q1: DAG 不确定性下 Algorithm 1 的 sensitivity 未讨论。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n"
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
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 20\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix（低优先级）。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 再提 Dirichlet 采样代表性。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Limitations 已覆盖。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。Limitations 已覆盖。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 20\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出，R18 修复充分。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 两位 Reviewer 再次提出（R1-W3, R2-W4）：主文 Section 3.1 仅简短提及，B.25 的 content-dependent proxy 违反结果（12/12 rejections for topic）未在主文讨论。要求在主文增加 2-3 句讨论实践合理性和验证策略。共识 should-fix。\"\n    resolution: \"R18 三管齐下修复（architectural invariant + Y-stratified test + stress test）。R20 要求进一步前置到主文。\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 19\n    resolution: \"R18 压缩后编译验证 main text ≤8 pages。R19 PDF 确认合规。连续两轮无复发。\"\n    resolution_round: 19\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: minor\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1 联合。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提（Abstract 187 words 合规，但 7+ 数字密度高）。R1 未单独提出。共识 minor。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。R2 仅在 minor M1 提及 abstract 字数边界。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: must-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据——缺少端到端因果应用验证\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。Limitations 中已承认。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 升级为 critical。R2 列为唯一 Must-Fix（N1）：声称对 practitioner 有指导意义但无端到端 demo（annotate→estimate→correct）。R1 列为 W2（should-fix）：缺乏 ground-truth causal effect 的端到端验��。共识：对 EMNLP 应用导向 venue 影响接收。建议至少一个 text-as-treatment 数据集走完全流程。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: Remark 1 重写为 complementary tools。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提：ASV 与 E-value 范式相似，方法论新颖性有限。R1 认为 ASV 有实用价值但同意理论创新不高。共识 should-fix。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W5 再提：ASV 与 E-values 区分度论证不够锐利，建议增加 'Why not E-values?' 讨论。R1 未单独提出但在优势中肯定 ASV 设计合理。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加��关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: must-fix\n    summary: \"Proportional effects 假设在 NLP 中是强限制，且 Limitations 中完全缺失\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 增加 stance detection/sentiment analysis 场景讨论 + 97.3% empirical compliance。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位 Reviewer 再提。R1: f,g 不可观测，97.3% 检验方法和标准不透明，OOB 率 23%。R2: 同意。共识 should-fix（高优先级）。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 升级为 critical（N1）：Proportional effects 是两个核心定理的关键前提，但 Limitations 中完全缺失。B.13 Table 14 显示 non-proportional 下 OOB rate 84.6%、sign preservation 降至 75.5%。建议：(1) Limitations 明确列出；(2) Section 3.2 加 scope caveat；(3) 引用 Table 14 数据。R2 未单独列出但在 W1 中间接触及（单调性假设条件过强）。\"\n    action_items:\n      - round: 19\n        action: \"SF-2 fix: 97.3% wording corrected to distinguish proportional vs non-proportional sign preservation rate\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem/Conjecture 边界在主文中模糊\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 must-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 2 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位再次列为 critical。MF-1a/1b/1c actions completed（adversarial test + Theorem 2 + framing chain）。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 再次提出。R1-N2（critical）：Theorem 1→Theorem 2→Conjecture 1 连续呈现，'已证明'与'数值猜测'边界不清。adversarial search 结构类型手动选择，无法排除未覆盖病态结构。R2-W1（should-fix）：Abstract 语气过于确定（'yielding a vulnerability ranking'），读者可能误以为已证结论。共识：need clearer delineation of proof vs conjecture boundary。\"\n    action_items:\n      - round: 19\n        action: \"MF-1a: Adversarial monotonicity test — 545,945 curves, max ε=0.016\"\n        assigned_to: agent\n        status: done\n      - round: 19\n        action: \"MF-1b: Theorem 2 (K=3 symmetric monotonicity) proof added\"\n        assigned_to: agent\n        status: done\n      - round: 19\n        action: \"MF-1c: Framing chain in method.tex\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。SF-2 fix applied。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"与 R6-M3 合并。R20 R1-N1 升级为 critical。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"与 R4-W6 合并。R2-W5 再提 ASV 与 E-values 区分度。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 NEW-1。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 NEW-1。R19 ���单独提出。连续两轮未提出，R18 修复充分。\"\n    resolution: \"随 NEW-1 一同解决。\"\n    resolution_round: 19\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 18\n    resolution: \"连续五轮（R14-R18）未被任何 Reviewer 提出，视为已解决。\"\n    resolution_round: 18\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: §4.5 扩展 logistic 讨论。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: Abstract + Conclusion linear SEM qualifier added。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W2 再提：FWL 不变性在 logistic 下部分失效意味着矩阵校正方法在非线性场景可能有效——论文对此讨论不足。建议在 Limitations 增加线性→非线性推广段。R1 未单独提出但间接认可。共识 should-fix。\"\n    action_items:\n      - round: 19\n        action: \"Abstract + Conclusion linear SEM qualifier added\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 确认 'first unified analysis' 在当前文献范围内成立。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 限定词简化。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 fix: 改为 'first multi-class (K≥3) topology-specific analysis'。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W3 再提：Brenner (1993) 已有 polytomous confounder 分析���Lee & Wood-Doughty (2024) 有 K≥3 confounding。建议改为 'first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies'。R1 未单独提出。共识 should-fix（低优先级）。\"\n    action_items:\n      - round: 19\n        action: \"SF-5 fix: introduction.tex 改为 'first multi-class (K≥3) topology-specific analysis'\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 R1-W3。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 R1-W3。R19 未单独提出。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: minor\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: column-stochastic 括号说明已加入。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: FWL, Wald inline explanations added。共识 minor。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 小问题 #2：notation density 高（p.3-4 一页内引入大量符号），Table 26 出现太晚。���议主文早期引用。R2 小问题 M5 提术语一致性。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 minor。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 R1 提 x 轴 scale 差异大。minor。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 R1 小问题 #1 caption 颜色含义不明确；R2 M3 信息密度过高建议仅保留 3 个拓扑在主文。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"两位共识。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。连续三轮未提出。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: 随 R9-C2 一同修复。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出��R19 fix 生效。\"\n    action_items:\n      - round: 19\n        action: \"随 R9-C2 一同修复：Abstract + Conclusion linear SEM qualifier\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 fix: primary coefficient hedge + sampling method note added。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。R19 fix 生效。\"\n    action_items:\n      - round: 19\n        action: \"Q5 fix: primary coefficient hedge + sampling note added\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 3 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: FWL 降为 Observation，Contribution 3 重聚焦于 correction routing 实证发现。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1-W4 再提 Algorithm 1 阈值缺乏理论依据：决策阈值来自特定模拟设置的经验平均，未验证跨 K/DGP 参数稳定性。建议报告不同 K 下性能或明确定位为启发式指南。R2 Q1 间接提及（DAG 不确定性下 Algorithm 1 的 sensitivity）。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words by 3 counting methods. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 20\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。Theorem 2 现为 collider 提供 K=3 symmetric 理论证明。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。连续三轮未提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"dawid1979, rosenbaum2002 未引用。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: 3 orphans removed。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 fix: 5 new orphans removed。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。连续一轮未提出。\"\n\n  # === Round 20 新发现 ===\n\n  - id: R20-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中很少成立——缺少合理性讨论和经验量化\"\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [R1]\n        note: \"R1-W1：真实 LLM confusion matrix 通常高度不对称（如 positive-neutral 混淆远多于 positive-negative）。论文未报告 23 个经验矩阵中有多少满足或近似满足对称性，也未讨论 Theorem 2 对轻微不对称的鲁棒性。建议量化对称性偏离程度（Frobenius distance to nearest symmetric matrix）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R20-N2\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 决策阈值缺乏理论依据和跨设置稳定性验证\"\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R1-W4: 阈值来自特定模拟设置（K=3, Dirichlet），未验证对不同 K/DGP/N 的稳定性。R2-Q1: DAG 不确定性下 Algorithm 1 的 sensitivity 未讨论。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1667 · 2026-05-23T18:48:23.139017+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 24228}, \"error\": \"\"}"}

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

_source line 1668 · 2026-05-23T18:50:35.065153+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "report": "# 审稿报告 — Round 20 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（重新审稿，无历史记忆）\n**Reviewer 配置**: 2人（R1: 方法严谨性; R2: 新颖性/完整性）\n\n---\n\n## Summary\n\n本文分析了 K≥3 多类别非差异性误分类在 7 种因果 DAG 拓扑下的偏差传播，证明 5 种拓扑保持符号而 exposure 和 IV 可发生符号反转。提出 Annotation Sensitivity Values (ASV) 框架量化拓扑依赖的脆弱性，并证明矩阵校正方法对 4 种协变量拓扑因 FWL 不变性而无效。理论在限定条件下正确，100,000 次 Monte Carlo 验证与 545,945 条对抗曲线支撑。\n\n---\n\n## Strengths\n\n**S1. 系统性覆盖填补文献空白。** 将 K≥3 多类别误分类与 7 种 DAG 拓扑的交叉分析做到前所未有的完整度。Teblunthuis (2024) 仅 K=2/4 拓扑；Lee & Wood-Doughty (2024) 仅单一 confounding。同时推广两个维度并发现质性新现象（sign reversal），非简单笛卡尔积。\n\n**S2. K≥3 sign reversal 发现有实际价值。** 经典 \"toward the null\" 保证在 K≥3 下被系统性打破（exposure 83.4% sign reversal under uniform Dirichlet; 2.1% under realistic diagonal ≥ 0.7）。对使用 LLM 标注进行因果推断的研究者是重要警示。\n\n**S3. FWL 不变性负结果优雅且有实践指导意义。** 证明 naive plug-in/MLA 对 4 种协变量拓扑下 bias reduction = 0%。直接改变 practitioner 的方法选择策略。\n\n**S4. 理论-数值三层协同验证模式优秀。** 每个定理配有 analytic proof + Monte Carlo verification (MAPE 1.6%) + adversarial testing (545,945 curves)。这种验证深度在方法论论文中罕见。\n\n**S5. 26 页 Appendix 验证充分。** 完整证明（A.1-A.9）、对抗验证（A.11）、非差异性压力测试（B.6）、非线性鲁棒性（B.7）、混淆矩阵估计鲁棒性（B.23）等形成完整的可信度链条。\n\n**S6. 实证锚定。** 23 组真实 LLM 混淆矩阵（HumAID K=10, VAST K=3, CivilComments K=2）将理论预测与实际 LLM 配置对接，F₁ disconnect (Spearman ρ=-0.10, p=0.45) 论证有力。\n\n**S7. 校正方法对比全面。** 5 方法 × 7 拓扑 × 210 配置，附带 Algorithm 1 决策流程。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [Critical, 共识] 缺少端到端因果应用验证。**\n- R2 列为唯一 Must-Fix; R1 列为 Should-Fix\n- 论文声称 \"Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations\"（Abstract 末句），但没有任何实验真正回答一个因果问题。Section 4.4 仅验证理论 violation rate 与真实混淆矩阵匹配；B.18 ClinicalBERT case study 仅回顾性分析已有混淆矩阵。缺少前瞻性的 annotate → estimate → correct 全流程 demonstration。\n- **影响**：对 EMNLP 这样的应用导向 venue，声称\"对 practitioner 有指导意义\"的框架需要至少一个端到端 demo。\n- **建议**：选择一个 text-as-treatment 数据集走完全流程，即使结果简单也比纯理论推导更有说服力。\n\n**W2. [Critical, R1] Proportional effects 假设在 Limitations 中完全缺失。**\n- Theorem 1（K=2）和 Theorem 2（K=3 symmetric）均要求 f = λg（proportional effects）\n- Limitations 提到了 non-differential misclassification、linear SEMs、symmetric matrices、general K 开放性——唯独未提及 proportional effects\n- B.13 Table 14 显示：non-proportional effects 下 OOB rate 达 84.6%，sign preservation 降至 75.5%\n- **影响**：读者可能高估定理的一般性。这是论文理论贡献的核心假设。\n- **建议**：(1) Limitations 明确列出 proportional effects 及其限制性；(2) Section 3.2 引入定理时加 scope caveat；(3) 引用 Table 14 数据说明退化行为。\n\n**W3. [Critical, R1; Should-Fix, R2] Theorem → Conjecture 理论缺口在主文中表述不清。**\n- Theorem 1（K=2）→ Theorem 2（K=3 symmetric）→ Conjecture 1（general K≥3, ε-approximate）连续呈现，\"已证明\"与\"数值猜测\"的边界模糊\n- Conjecture 1 依赖 545,945 adversarial curves，但 adversarial search 结构类型为手动选择，无法排除未覆盖的病态结构\n- **影响**：读者容易将 Conjecture 1 误读为已证明定理。\n- **建议**：(1) 明确标注 \"analytic proofs end here; the following is supported by numerical evidence only\"；(2) 讨论 adversarial search 覆盖范围限制。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4. [共识] Theorem 2 的 symmetric C₀ 假设在实际 LLM 场景中很少成立。**\n- 真实 LLM 混淆矩阵通常高度不对称\n- 论文未报告 23 个经验矩阵中有多少满足或近似满足对称性\n- **建议**：量化经验矩阵的对称性偏离程度（Frobenius distance to nearest symmetric matrix），讨论 Theorem 2 对轻微不对称的鲁棒性。\n\n**W5. [共识] 线性 SEM 推广讨论不足。**\n- 所有定理建立在线性 SEM 上。B.7 logistic 回归 sign-flip 率为零（积极），但 B.15 FWL breakdown 显示 logistic 下矩阵校正方法可能有效。\n- **影响**：核心负结果（矩阵校正无效）在非线性模型下可能不适用，论文对此讨论不充分。\n- **建议**：Limitations 增加线性→非线性推广讨论。\n\n**W6. [共识] Non-differential misclassification 假设讨论应更前置。**\n- B.25 Y-stratified 验证显示 content-dependent proxies 违反假设（12/12 rejections for topic）\n- 主文仅 Limitations 一句带过\n- **建议**：Section 3.1 增加 2-3 句讨论实践合理性和验证策略，引导读者到 B.5-B.6。\n\n**W7. [R2] ASV 与 E-values 区分度论证不够锐利。**\n- 两者都将\"扰动强度\"映射到\"效果是否翻转\"的阈值。Remark 1 称 \"analogous to E-values\" 但未深入解释增量价值。\n- **建议**：增加 \"Why not E-values?\" 讨论，明确 ASV 回答的问题（标注误差强度阈值）与 E-values 回答的问题（未观测混淆强度阈值）的本质区别。\n\n**W8. [R1] Algorithm 1 决策阈值缺乏理论依据。**\n- 阈值来自特定模拟设置（K=3, Dirichlet, 7 topologies）的经验平均\n- 未验证对不同 K、DGP 参数、样本量的稳定性\n- **建议**：报告跨 K 性能，或明确定位为启发式指南而非普适算法。\n\n**W9. [R2] \"first multi-class topology-specific analysis\" 声称需更精确界定。**\n- Brenner (1993) 已有 polytomous confounder；Lee & Wood-Doughty (2024) 有 K≥3 confounding。\n- **建议**：改为 \"first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **评分一致**：两位 Reviewer 独立给出 3.5/5（Borderline Conference）。\n2. **端到端验证缺失是核心短板**：对 EMNLP 应用导向 venue，声称 practitioner guidance 但无实际因果问题 demo 是显著弱点。\n3. **Theorem/Conjecture 边界需更清晰**：K≥3 一般情况下 ASV 排序仅有数值支撑，主文语气应更谨慎。\n4. **Non-differential 假设讨论应前置到主文**。\n5. **理论贡献的条件（proportional effects, symmetric C₀, linear SEM）在实践中限制性强**，论文未充分告知读者。\n6. **核心发现（sign reversal, FWL invariance, ASV ranking）有实际价值**，对 NLP 社区有警示意义。\n7. **验证深度（MAPE 1.6%, 545,945 curves, 23 LLM configs）令人信服**。\n\n## Reviewer Divergence [REBUT]\n\n1. **端到端验证的严重程度**：R2 视为唯一 Must-Fix（critical）；R1 视为 Should-Fix（认为论文的理论贡献自身有价值，端到端 demo 是 nice-to-have）。\n2. **Proportional effects 缺失**：R1 视为 Critical（核心假设未在 Limitations 中披露）；R2 未单独列出（在 W1 ASV 单调性下间接触及，但未升级为 critical）。\n\n---\n\n## Questions for Authors\n\nQ1. Algorithm 1 假设 DAG topology 已知。当 topology 不确定时，是否考虑过在多个候选 DAG 上运行 ASV 并报告 sensitivity 范围？\n\nQ2. MC-SIMEX 需要已知/估计的混淆矩阵，PPI++ 只需 gold labels。在 gold labels 昂贵时（如 K=10），两者的 trade-off 如何？\n\nQ3. 非线性 DGP（logistic）下 bias magnitude 如何变化？线性 ASV 能否作为保守近似？\n\nQ4. K=10 时混淆矩阵有 100 个参数。B.23 bootstrap 分析在 n_gold=500 时 ASV 排序稳定（Spearman ρ≥0.99），但对 K=10 是否也成立？\n\nQ5. 23 个经验 LLM 混淆矩阵中有多少满足或近似满足 Theorem 2 的对称性条件？\n\n---\n\n## Missing References\n\n未发现重大遗漏。Related Work 覆盖了 measurement error (Carroll 2006, Gustafson 2004)、binary misclassification (Brenner 1993, Bross 1954)、LLM annotation (Gilardi 2023, Ziems 2024, Baumann 2025)、sensitivity analysis (VanderWeele & Ding 2017, Cinelli 2020) 等主要方向。引用中未发现明显虚构或年份错误。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成** (2026-05-23 18:34 → 18:39, ~5min)\n\n主要发现：\n- **[Warning]** 前两页纯文本（Title + Abstract + Introduction），无 display item。Figure 1 到第 3 页才出现。审稿人前 2 分钟只看到密集文字，无视觉锚点。建议将 Figure 1 提前到第 2 页。\n- **[Warning]** 页 4-6 理论密度高但视觉节奏略显单调（3 页中仅 1 个 display item）。考虑到是理论核心区域，属可接受例外。\n- **[Info]** 正文恰好 8 页，符合 EMNLP 2026 Long Paper 限制。\n- **[Info]** 主文 4 个 display items (3 figures + 1 table) across 8 页 = 0.5/页。对理论+实证混合型论文偏低端但可接受。\n- **[Info]** References 无 [?] 未解析引用，格式一致。\n- 0 critical / 2 warning / 16 info。总体排版专业、格式合规。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 — Borderline Conference (介于 Conference 和 Findings 之间)**\n\n**置信度：4 / 5**\n\n**判断依据**：\n- 理论贡献在限定条件下正确且有新颖性（sign reversal dichotomy, ASV framework, FWL invariance insight）\n- 验证深度优秀（三层协同：analytic + MC + adversarial）\n- 但核心定理的实际适用范围受 proportional effects + symmetric C₀ + linear SEM 三重限制，且 Limitations 未充分披露\n- 对 EMNLP 应用导向 venue 而言，缺少端到端 NLP 因果应用 demo 是显著短板\n- Conjecture 1 的理论缺口（K≥3 一般情况未证明）使 ASV 排序的理论保障不完整\n\n**升级条件（→ 4.0 Conference）**：\n1. 增加一个端到端因果应用 demo（即使简单）\n2. Limitations 补充 proportional effects 假设讨论\n3. 主文明确标注 Theorem/Conjecture 边界\n\n**降级风险（→ 3.0 Findings）**：\n- 如果 Reviewer 认为 proportional effects 下 OOB rate 84.6% 意味着定理在实践中基本无用\n- 如果 EMNLP AC 倾向惩罚纯方法论贡献（无 NLP 应用 demo）\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"first multi-class (K≥3) topology-specific analysis\" 需更精确限定（Brenner 1993, Lee & Wood-Doughty 2024 部分覆盖）\n- 83.4% headline 后续有 realistic regime 数字（2.1%），叙事节奏合理\n\n### Section 3.1 (Setup)\n- Non-differential 假设的实践合理性讨论应从 Appendix 部分前置到此处\n- Notation density 高（p.3-4 一页内引入大量符号），Table 26 出现太晚\n\n### Section 3.2 (Bias Expressions + Theorems)\n- Theorem 1/2 → Conjecture 1 的递进需更显式标注证明终点\n- Proportional effects 假设需在定理引入时加 caveat\n- Theorem 2 symmetric 假设的实际合理性需讨论\n\n### Section 4.2 (Bias Taxonomy Results)\n- \"grand MAPE\" 非标准术语，建议改为 \"mean absolute percentage error averaged across\"\n- Dirichlet(1,1,1) 83.4% 是最坏情况，Figure 2 caption 建议注明 realistic-accuracy 对比\n\n### Section 4.4 (Empirical Validation)\n- 使用真实混淆矩阵但在模拟 DGP 上运行——最接近但仍非端到端验证\n- F₁ disconnect 论证有力（Spearman ρ=-0.10, p=0.45）\n\n### Section 4.5 (Correction)\n- Algorithm 1 阈值为启发式，应明确标注\n- FWL invariance 描述应加 \"matrix-based\" 修饰，避免误导\n\n### Section 5 (Limitations)\n- 缺 proportional effects（最关键遗漏）\n- \"experiments lack end-to-end causal benchmarks\" 一笔带过，应展开\n- 三个限制覆盖合适，但深度不足\n\n### Format Compliance\n- 正文 ≤ 8 页 ✅\n- Abstract ≈ 190 words（边界合规）⚠️\n- Limitations 存在且适当 ✅\n- 匿名性 ✅（无 self-citation leak）\n- 单一 Limitations section ✅\n- AI 辅助声明 ✅（Section D, p.34）\n",
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
    "project": "causal_annot_error_attrib",
    "report": "# 审稿报告 — Round 20 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（重新审稿，无历史记忆）\n**Reviewer 配置**: 2人（R1: 方法严谨性; R2: 新颖性/完整性）\n\n---\n\n## Summary\n\n本文分析了 K≥3 多类别非差异性误分类在 7 种因果 DAG 拓扑下的偏差传播，证明 5 种拓扑保持符号而 exposure 和 IV 可发生符号反转。提出 Annotation Sensitivity Values (ASV) 框架量化拓扑依赖的脆弱性，并证明矩阵校正方法对 4 种协变量拓扑因 FWL 不变性而无效。理论在限定条件下正确，100,000 次 Monte Carlo 验证与 545,945 条对抗曲线支撑。\n\n---\n\n## Strengths\n\n**S1. 系统性覆盖填补文献空白。** 将 K≥3 多类别误分类与 7 种 DAG 拓扑的交叉分析做到前所未有的完整度。Teblunthuis (2024) 仅 K=2/4 拓扑；Lee & Wood-Doughty (2024) 仅单一 confounding。同时推广两个维度并发现质性新现象（sign reversal），非简单笛卡尔积。\n\n**S2. K≥3 sign reversal 发现有实际价值。** 经典 \"toward the null\" 保证在 K≥3 下被系统性打破（exposure 83.4% sign reversal under uniform Dirichlet; 2.1% under realistic diagonal ≥ 0.7）。对使用 LLM 标注进行因果推断的研究者是重要警示。\n\n**S3. FWL 不变性负结果优雅且有实践指导意义。** 证明 naive plug-in/MLA 对 4 种协变量拓扑下 bias reduction = 0%。直接改变 practitioner 的方法选择策略。\n\n**S4. 理论-数值三层协同验证模式优秀。** 每个定理配有 analytic proof + Monte Carlo verification (MAPE 1.6%) + adversarial testing (545,945 curves)。这种验证深度在方法论论文中罕见。\n\n**S5. 26 页 Appendix 验证充分。** 完整证明（A.1-A.9）、对抗验证（A.11）、非差异性压力测试（B.6）、非线性鲁棒性（B.7）、混淆矩阵估计鲁棒性（B.23）等形成完整的可信度链条。\n\n**S6. 实证锚定。** 23 组真实 LLM 混淆矩阵（HumAID K=10, VAST K=3, CivilComments K=2）将理论预测与实际 LLM 配置对接，F₁ disconnect (Spearman ρ=-0.10, p=0.45) 论证有力。\n\n**S7. 校正方法对比全面。** 5 方法 × 7 拓扑 × 210 配置，附带 Algorithm 1 决策流程。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [Critical, 共识] 缺少端到端因果应用验证。**\n- R2 列为唯一 Must-Fix; R1 列为 Should-Fix\n- 论文声称 \"Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations\"（Abstract 末句），但没有任何实验真正回答一个因果问题。Section 4.4 仅验证理论 violation rate 与真实混淆矩阵匹配；B.18 ClinicalBERT case study 仅回顾性分析已有混淆矩阵。缺少前瞻性的 annotate → estimate → correct 全流程 demonstration。\n- **影响**：对 EMNLP 这样的应用导向 venue，声称\"对 practitioner 有指导意义\"的框架需要至少一个端到端 demo。\n- **建议**：选择一个 text-as-treatment 数据集走完全流程，即使结果简单也比纯理论推导更有说服力。\n\n**W2. [Critical, R1] Proportional effects 假设在 Limitations 中完全缺失。**\n- Theorem 1（K=2）和 Theorem 2（K=3 symmetric）均要求 f = λg（proportional effects）\n- Limitations 提到了 non-differential misclassification、linear SEMs、symmetric matrices、general K 开放性——唯独未提及 proportional effects\n- B.13 Table 14 显示：non-proportional effects 下 OOB rate 达 84.6%，sign preservation 降至 75.5%\n- **影响**：读者可能高估定理的一般性。这是论文理论贡献的核心假设。\n- **建议**：(1) Limitations 明确列出 proportional effects 及其限制性；(2) Section 3.2 引入定理时加 scope caveat；(3) 引用 Table 14 数据说明退化行为。\n\n**W3. [Critical, R1; Should-Fix, R2] Theorem → Conjecture 理论缺口在主文中表述不清。**\n- Theorem 1（K=2）→ Theorem 2（K=3 symmetric）→ Conjecture 1（general K≥3, ε-approximate）连续呈现，\"已证明\"与\"数值猜测\"的边界模糊\n- Conjecture 1 依赖 545,945 adversarial curves，但 adversarial search 结构类型为手动选择，无法排除未覆盖的病态结构\n- **影响**：读者容易将 Conjecture 1 误读为已证明定理。\n- **建议**：(1) 明确标注 \"analytic proofs end here; the following is supported by numerical evidence only\"；(2) 讨论 adversarial search 覆盖范围限制。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4. [共识] Theorem 2 的 symmetric C₀ 假设在实际 LLM 场景中很少成立。**\n- 真实 LLM 混淆矩阵通常高度不对称\n- 论文未报告 23 个经验矩阵中有多少满足或近似满足对称性\n- **建议**：量化经验矩阵的对称性偏离程度（Frobenius distance to nearest symmetric matrix），讨论 Theorem 2 对轻微不对称的鲁棒性。\n\n**W5. [共识] 线性 SEM 推广讨论不足。**\n- 所有定理建立在线性 SEM 上。B.7 logistic 回归 sign-flip 率为零（积极），但 B.15 FWL breakdown 显示 logistic 下矩阵校正方法可能有效。\n- **影响**：核心负结果（矩阵校正无效）在非线性模型下可能不适用，论文对此讨论不充分。\n- **建议**：Limitations 增加线性→非线性推广讨论。\n\n**W6. [共识] Non-differential misclassification 假设讨论应更前置。**\n- B.25 Y-stratified 验证显示 content-dependent proxies 违反假设（12/12 rejections for topic）\n- 主文仅 Limitations 一句带过\n- **建议**：Section 3.1 增加 2-3 句讨论实践合理性和验证策略，引导读者到 B.5-B.6。\n\n**W7. [R2] ASV 与 E-values 区分度论证不够锐利。**\n- 两者都将\"扰动强度\"映射到\"效果是否翻转\"的阈值。Remark 1 称 \"analogous to E-values\" 但未深入解释增量价值。\n- **建议**：增加 \"Why not E-values?\" 讨论，明确 ASV 回答的问题（标注误差强度阈值）与 E-values 回答的问题（未观测混淆强度阈值）的本质区别。\n\n**W8. [R1] Algorithm 1 决策阈值缺乏理论依据。**\n- 阈值来自特定模拟设置（K=3, Dirichlet, 7 topologies）的经验平均\n- 未验证对不同 K、DGP 参数、样本量的稳定性\n- **建议**：报告跨 K 性能，或明确定位为启发式指南而非普适算法。\n\n**W9. [R2] \"first multi-class topology-specific analysis\" 声称需更精确界定。**\n- Brenner (1993) 已有 polytomous confounder；Lee & Wood-Doughty (2024) 有 K≥3 confounding。\n- **建议**：改为 \"first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **评分一致**：两位 Reviewer 独立给出 3.5/5（Borderline Conference）。\n2. **端到端验证缺失是核心短板**：对 EMNLP 应用导向 venue，声称 practitioner guidance 但无实际因果问题 demo 是显著弱点。\n3. **Theorem/Conjecture 边界需更清晰**：K≥3 一般情况下 ASV 排序仅有数值支撑，主文语气应更谨慎。\n4. **Non-differential 假设讨论应前置到主文**。\n5. **理论贡献的条件（proportional effects, symmetric C₀, linear SEM）在实践中限制性强**，论文未充分告知读者。\n6. **核心发现（sign reversal, FWL invariance, ASV ranking）有实际价值**，对 NLP 社区有警示意义。\n7. **验证深度（MAPE 1.6%, 545,945 curves, 23 LLM configs）令人信服**。\n\n## Reviewer Divergence [REBUT]\n\n1. **端到端验证的严重程度**：R2 视为唯一 Must-Fix（critical）；R1 视为 Should-Fix（认为论文的理论贡献自身有价值，端到端 demo 是 nice-to-have）。\n2. **Proportional effects 缺失**：R1 视为 Critical（核心假设未在 Limitations 中披露）；R2 未单独列出（在 W1 ASV 单调性下间接触及，但未升级为 critical）。\n\n---\n\n## Questions for Authors\n\nQ1. Algorithm 1 假设 DAG topology 已知。当 topology 不确定时，是否考虑过在多个候选 DAG 上运行 ASV 并报告 sensitivity 范围？\n\nQ2. MC-SIMEX 需要已知/估计的混淆矩阵，PPI++ 只需 gold labels。在 gold labels 昂贵时（如 K=10），两者的 trade-off 如何？\n\nQ3. 非线性 DGP（logistic）下 bias magnitude 如何变化？线性 ASV 能否作为保守近似？\n\nQ4. K=10 时混淆矩阵有 100 个参数。B.23 bootstrap 分析在 n_gold=500 时 ASV 排序稳定（Spearman ρ≥0.99），但对 K=10 是否也成立？\n\nQ5. 23 个经验 LLM 混淆矩阵中有多少满足或近似满足 Theorem 2 的对称性条件？\n\n---\n\n## Missing References\n\n未发现重大遗漏。Related Work 覆盖了 measurement error (Carroll 2006, Gustafson 2004)、binary misclassification (Brenner 1993, Bross 1954)、LLM annotation (Gilardi 2023, Ziems 2024, Baumann 2025)、sensitivity analysis (VanderWeele & Ding 2017, Cinelli 2020) 等主要方向。引用中未发现明显虚构或年份错误。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成** (2026-05-23 18:34 → 18:39, ~5min)\n\n主要发现：\n- **[Warning]** 前两页纯文本（Title + Abstract + Introduction），无 display item。Figure 1 到第 3 页才出现。审稿人前 2 分钟只看到密集文字，无视觉锚点。建议将 Figure 1 提前到第 2 页。\n- **[Warning]** 页 4-6 理论密度高但视觉节奏略显单调（3 页中仅 1 个 display item）。考虑到是理论核心区域，属可接受例外。\n- **[Info]** 正文恰好 8 页，符合 EMNLP 2026 Long Paper 限制。\n- **[Info]** 主文 4 个 display items (3 figures + 1 table) across 8 页 = 0.5/页。对理论+实证混合型论文偏低端但可接受。\n- **[Info]** References 无 [?] 未解析引用，格式一致。\n- 0 critical / 2 warning / 16 info。总体排版专业、格式合规。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 — Borderline Conference (介于 Conference 和 Findings 之间)**\n\n**置信度：4 / 5**\n\n**判断依据**：\n- 理论贡献在限定条件下正确且有新颖性（sign reversal dichotomy, ASV framework, FWL invariance insight）\n- 验证深度优秀（三层协同：analytic + MC + adversarial）\n- 但核心定理的实际适用范围受 proportional effects + symmetric C₀ + linear SEM 三重限制，且 Limitations 未充分披露\n- 对 EMNLP 应用导向 venue 而言，缺少端到端 NLP 因果应用 demo 是显著短板\n- Conjecture 1 的理论缺口（K≥3 一般情况未证明）使 ASV 排序的理论保障不完整\n\n**升级条件（→ 4.0 Conference）**：\n1. 增加一个端到端因果应用 demo（即使简单）\n2. Limitations 补充 proportional effects 假设讨论\n3. 主文明确标注 Theorem/Conjecture 边界\n\n**降级风险（→ 3.0 Findings）**：\n- 如果 Reviewer 认为 proportional effects 下 OOB rate 84.6% 意味着定理在实践中基本无用\n- 如果 EMNLP AC 倾向惩罚纯方法论贡献（无 NLP 应用 demo）\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"first multi-class (K≥3) topology-specific analysis\" 需更精确限定（Brenner 1993, Lee & Wood-Doughty 2024 部分覆盖）\n- 83.4% headline 后续有 realistic regime 数字（2.1%），叙事节奏合理\n\n### Section 3.1 (Setup)\n- Non-differential 假设的实践合理性讨论应从 Appendix 部分前置到此处\n- Notation density 高（p.3-4 一页内引入大量符号），Table 26 出现太晚\n\n### Section 3.2 (Bias Expressions + Theorems)\n- Theorem 1/2 → Conjecture 1 的递进需更显式标注证明终点\n- Proportional effects 假设需在定理引入时加 caveat\n- Theorem 2 symmetric 假设的实际合理性需讨论\n\n### Section 4.2 (Bias Taxonomy Results)\n- \"grand MAPE\" 非标准术语，建议改为 \"mean absolute percentage error averaged across\"\n- Dirichlet(1,1,1) 83.4% 是最坏情况，Figure 2 caption 建议注明 realistic-accuracy 对比\n\n### Section 4.4 (Empirical Validation)\n- 使用真实混淆矩阵但在模拟 DGP 上运行——最接近但仍非端到端验证\n- F₁ disconnect 论证有力（Spearman ρ=-0.10, p=0.45）\n\n### Section 4.5 (Correction)\n- Algorithm 1 阈值为启发式，应明确标注\n- FWL invariance 描述应加 \"matrix-based\" 修饰，避免误导\n\n### Section 5 (Limitations)\n- 缺 proportional effects（最关键遗漏）\n- \"experiments lack end-to-end causal benchmarks\" 一笔带过，应展开\n- 三个限制覆盖合适，但深度不足\n\n### Format Compliance\n- 正文 ≤ 8 页 ✅\n- Abstract ≈ 190 words（边界合规）⚠️\n- Limitations 存在且适当 ✅\n- 匿名性 ✅（无 self-citation leak）\n- 单一 Limitations section ✅\n- AI 辅助声明 ✅（Section D, p.34）\n",
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

_source line 1669 · 2026-05-23T18:50:38.679604+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Assistant

_source line 1670 · 2026-05-23T18:50:46.101551+00:00_

审稿完成。

**Round 20 审稿结果：3.5 / 5（Borderline Conference）**

核心发现：
- **3 个 Must-Fix**：(1) 缺少端到端因果应用 demo；(2) Proportional effects 假设未在 Limitations 披露；(3) Theorem/Conjecture 边界在主文中模糊
- **6 个 Should-Fix**：Theorem 2 对称假设实际合理性、线性 SEM 推广讨论、非差异性假设前置、ASV vs E-values 区分度、Algorithm 1 阈值稳定性、"first" 声称精度
- **升级条件（→ 4.0）**：增加端到端 demo + 补充 Limitations + 明确理论边界

报告已投递 Research Director，Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 165

## Round 165

2 recorded events


### User

_source line 1671 · 2026-05-23T18:50:46.105387+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R2-N1: 缺少端到端因果应用验证 — 同意方向但反对 Must-Fix 定级**

R2 的关切本身合理：论文没有从一个真实因果问题出发走完 annotate → estimate → correct 全流程。但我认为应降级为 Should-Fix，理由：

1. **论文的核心贡献是理论/方法论，不是应用**。Theorem 1/2、Proposition 1、ASV 框架的价值不依赖于某个特定端到端 demo。这类似于 E-values（VanderWeele and Ding, 2017）首发论文也没有端到端因果实验，而是提供了 sensitivity analysis 工具并用模拟验证。

2. **现有实验已提供合理的实践验证链**：(a) Section 4.4 用 23 个真实 LLM 混淆矩阵（HumAID K=10, VAST K=3, CivilComments K=2）验证理论 violation rate 预测；(b) Appendix B.18 的 ClinicalBERT case study 在真实 CSS 场景（political ad tone → voter outcomes）上演示了完整的 ASV 诊断 + 校正推荐流程；(c) Appendix B.19/B.20 测试了校正方法在 K=3,5,10 下的稳定性。

3. **R2 建议的 Egami et al. (2022) 数据集也不提供 ground-truth causal effect**，因此即使使用该数据集，也无法验证校正后的估计更接近真值——只能展示流程可执行性，这与 B.18 的演示本质相同。

综上：建议作者增加端到端 demo 以增强 practical appeal（特别是面向 EMNLP 受众），但不应以此作为拒稿理由。

---

### Should-Fix

**[AGREE] R2-W1: ASV 单调性对一般 K 是猜想而非定理**

完全同意。这与我自己的 N2 发现一致。主文 Section 3.2-3.3 将 Theorem 1 → Theorem 2 → Conjecture 1 连续呈现，proof 与 numerical evidence 的边界不够清晰。建议在 Conjecture 1 引入处明确标注 "empirically robust conjecture supported by 545,945 adversarial curves, not a proven result"。Abstract 中 "K≥3 introduces a structural possibility of sign reversal" 的表述是准确的，但 Section 3.3 中 ASV 排序的稳定性声称应注明依赖 Conjecture 1。

**[REBUT] R2-W2: 理论限于线性 SEM，推广讨论不足**

论文在 Limitations（p.8）已明确提到 "Closed-form expressions assume linear SEMs (logistic robustness: Appendix B.11)"。更重要的是，论文提供了系统的非线性鲁棒性验证：
- Appendix B.7（p.25, Table 15）：logistic 回归下所有 5 个 guaranteed topology 的 sign-flip rate 为零，treatment-effect sign-flip rate 也为零，涵盖 K=3 和 6 种 error level × 6 种拓扑 × 100 MC replications。
- Appendix B.15（p.29, Table 15）：FWL breakdown 下 logistic bias reduction 在所有 covariate topology 上均 < 0.001（essentially zero），确认 FWL invariance 的近似成立。
- Appendix B.7 的 Table 13 还显示 mean logistic bias reduction 在所有拓扑上接近零（positive = correction works）。

这些已经构成了充分的线性→非线性鲁棒性证据。当然，在 Limitations 中可以增加一两句讨论 logistic 近似的局限（如在 treatment effect 极大时可能失效），但当前状态并非缺失。

**[AGREE] R2-W3: "first multi-class topology-specific analysis" 声称需更精确**

同意。论文 Introduction（p.2）已引用 Brenner (1993) 和 Lee & Wood-Doughty (2024) 作为 prior work，但 "first" 声称仍可能引起异议。R2 建议的改写——"first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies"——更精确地界定了贡献范围，明确了 novelty 在于 "systematic + multiple topologies" 的组合，而非 multi-class 或 topology-specific 的单独首次性。建议采纳。

**[AGREE] R2-W4: 非差异性误分类假设讨论应更前置**

同意，与我的 W3 发现一致。Appendix B.25（Table 25）的 Y-stratified 验证显示 content-dependent proxies（topic, sentiment）产生显著违反（topic: 12/12 rejections），这对论文核心假设的适用范围有实质影响。至少应在主文 Section 3.1 的 Definition 1 之后加一段简短讨论：(1) 为什么 LLM 标注 pipeline 通常满足此假设（text independently classified）；(2) 已知例外情况（content-dependent 特征与 Y 相关时）；(3) 指向 B.25 的详细验证。

**[AGREE] R2-W5: ASV 与 E-values 的区分度论证不够锐利**

同意。当前主文（p.5-6）仅说 ASV "analogous to E-values"，但没有解释为什么不能直接复用 E-values。关键区别至少包括：
1. **扰动维度不同**：E-values 量化 unmeasured confounding 的强度阈值（risk ratio 尺度）；ASV 量化 annotation error 的强度阈值（confusion matrix interpolation 路径）。
2. **拓扑依赖性**：E-values 对所有 DAG 结构给出相同的 bound（因为 confounding 的影响不依赖其他路径）；ASV 的值高度依赖 DAG 拓扑（这正是论文的核心洞见）。
3. **多维诊断**：ASV 分解为 magnitude/significance/sign-flip 三个维度，E-values 是单一标量。
建议增加一段 "Why not E-values?" 的简要讨论。

---

### 小问题

- **M1 (Abstract 字数)**：同意应检查，EMNLP 2026 限制 200 words。
- **M2 ("grand MAPE")**：同意不是标准术语，建议改为 "overall MAPE" 或 "mean MAPE across configurations"。
- **M3 (Figure 2 信息密度)**：与我的小问题一致，Figure 2 包含 7 个子图 + 颜色编码，确实密度偏高。但考虑到 8 页的空间约束，这种密度是可接受的折衷。
- **M5 (topology vs DAG topology)**：合理的一致性建议，统一用 "DAG topology" 更精确。
- **M6 (Limitations 中端到端缺失一笔带过)**：同意，Limitations 说 "experiments lack end-to-end causal benchmarks" 但没有解释为什么以及如何弥补。

---

### Questions 回应

**Q1: 是否考虑在多个候选 DAG 上运行 ASV 并报告 sensitivity 范围？**
好问题。论文 Section 4.3 的 ASV 计算假设已知拓扑。在实际中拓扑不确定时，跨多个候选 DAG 报告 ASV 范围是自然的扩展。但我注意到 Algorithm 1（p.34）Step 1 已考虑了 "DAG uncertainty"（"if T is uncertain, return Step 1.1 model each candidate topology"），虽然没有展开。这可作为 future work 或增加一个简短讨论。

**Q2: MC-SIMEX vs PPI++ 在 gold labels 昂贵时的 trade-off？**
Table 5（p.23）和 Algorithm 1 已部分回答：MC-SIMEX 是 gold-free 方法（不需要 gold labels），PPI++ 需要。Algorithm 1 Step 2 按 gold label availability 分流。但论文没有量化 gold label 数量与 PPI++ 性能的关系（如 5%, 10%, 20% gold labels 下的 RMSE reduction 曲线）。这是一个合理的 future work 方向。

**Q3: 非线性 DGP 下 bias magnitude 如何变化？线性 ASV 能否作为近似？**
Appendix B.7（p.25）提供了 logistic regression 的 sign-flip 率（均为零），B.15（Table 15, p.29）显示 logistic bias reduction 在 covariate topologies 上接近零。这支持线性 ASV 作为近似的合理性——至少在 sign preservation 和 topology ranking 维度上。但 bias magnitude 的绝对精度确实可能在强非线性下退化，论文没有量化这一点。

**Q4: K=10 时 100 参数的混淆矩阵如何可靠估计？**
重要的实操问题。K=10 的混淆矩阵有 K×(K-1)=90 个独立参数。论文在 Section 4.4 使用 HumAID（K=10）但没有讨论估计所需的最小 gold-label 样本量。Appendix B.23（p.32, Table 23）显示 ASV ranking stability 在 n_gold=50 时已达 Spearman ρ≥0.99，这部分回答了问题——但仅针对 K≤3 的经验混淆矩阵。K=10 下的 bootstrap stability 没有专门报告。建议补充。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2-N1（端到端验证）**：[REBUT] 同意方向但反对 Must-Fix 定级。论文核心贡献是理论框架，B.18 已提供 ClinicalBERT case study，且 R2 建议的 Egami et al. 数据集也无 ground-truth causal effect。建议降为 Should-Fix。
- **R2-W1（Conjecture 1 标注）**：[AGREE]，与我的 N2 一致。
- **R2-W2（线性 SEM）**：[REBUT]，Limitations 已提及，B.7/B.15 提供了系统的 logistic 鲁棒性验证。
- **R2-W3（novelty 声称）**：[AGREE]，R2 的改写建议更精确。
- **R2-W4（non-differential 前置）**：[AGREE]，与我的 W3 一致。
- **R2-W5（ASV vs E-values）**：[AGREE]，应增加区分讨论。

---

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### [AGREE] R1-N1: Proportional effects 假设在 Limitations 中缺失

同意这是一个实质性遗漏。我逐项验证了 R1 的论据：

1. **定理依赖确认**：Theorem 1 (p6) 明确要求 "proportional effects (f = λg for some scalar λ)"；Theorem 2 (p6) 同样要求 "proportional effects (f=λg)"。这是两个核心单调性定理的必要条件。

2. **Limitations 缺失确认**：p8 Limitations 段落仅列出四点限制——non-differential misclassification、linear SEMs、symmetric matrices (Theorem 2)、general K open。确实没有提及 proportional effects。

3. **实证影响确认**：Appendix B.13 Table 14 (p29) 的数据支持 R1 的担忧——non-proportional effects 下 A(C) OOB rate 从 exact proportional 的 0% 升至 near-proportional 的 ~10%，fully independent (f ⊥ g) 时升至 ~15%，sign preservation 从 100% 降至 75.5%。这不是可忽略的边界情况。

**补充发现**：主文 p6 确实讨论了 non-proportional effects（"under non-proportional effects, approximate monotonicity holds (ε < 0.004; Appendix A.6, Remark 2)"），且 Appendix A.6 Remark 2 (p14) 提供了详细分析。所以信息存在于论文中，但 Limitations 段落作为读者最常检查的"假设清单"，遗漏了这一条确实有问题。建议在 Limitations 增加一句即可修复。

---

### [REBUT] R1-N2: Theorem → Conjecture 过渡表述不清

部分不同意将此列为 Must-Fix/critical。理由：

1. **标注已足够清晰**：Conjecture 1 在 p6 明确标注为 "Conjecture 1 (ε-approximate envelope monotonicity)"——使用了 "Conjecture" 而非 "Theorem"。紧随其后的文字用 "is supported by" 而非 "is proved by"（"Conjecture 1 is supported by 100,000 Dirichlet-sampled matrices and 545,945 adversarial curves"）。

2. **证明边界有标注**：p6 的叙事结构是 "Theorem 1 proves exact monotonicity for K=2. Theorem 2 extends to K=3 symmetric matrices. For general K≥3, Conjecture 1 is supported by..."——从 "proves" → "extends" → "supported by" 的措辞变化已经传递了证明状态的降级。

3. **数值验证规模可观**：545,945 adversarial curves（Appendix A.11, p21-22）覆盖 near-permutation, block-diagonal, sparse, near-uniform 四种结构，maximum violation ε_adv ≤ 0.016。虽然 adversarial search 结构是手动选择的（R1 正确指出），但这些结构覆盖了confusion matrix space的典型极端情况。

**但我同意 R1 建议的方向**：在 Theorem 2 和 Conjecture 1 之间增加一句过渡性说明（如 "The following result is empirically supported but unproven"）是低成本高收益的改进，可以从 Must-Fix 降为 Should-Fix。R1 将此列为 critical 似乎过重——Conjecture 在数学论文中是标准术语，ACL/EMNLP 审稿人应能理解其含义。

---

## Should-Fix 问题

### [AGREE] R1-W1: Theorem 2 的 symmetric C₀ 假设在实际中很少成立

同意 R1 的关切。真实 LLM 混淆矩阵通常高度不对称（如 sentiment 分类中 positive→neutral 的误分类率远高于 neutral→positive），论文未量化 23 个经验矩阵的对称性偏离程度。

**但需补充上下文**：Theorem 2 的对称性假设仅限制了该定理的适用范围，不影响论文的实际使用场景。Conjecture 1 适用于一般 column-stochastic C（无对称性要求），这才是 practitioner 使用的结果。Appendix B.12 (p27) 的 extended conjecture verification 使用了非对称矩阵。所以对称性限制是理论完整性问题（K=3 证明仅覆盖对称情况），而非实用性问题（ASV ranking 在非对称矩阵上仍然稳定）。

建议：量化 23 个经验矩阵的 Frobenius norm ||C - C^T||_F 作为对称性偏离度，并报告非对称矩阵上的 ASV ranking 一致性。

---

### [AGREE] R1-W2: 缺乏已知因果效应的端到端验证

完全同意。这与我自己审稿意见中的 N1 一致。论文的 empirical validation（Section 4.4, p7-8）验证了 theory-MC agreement 和 bias taxonomy predictions，但没有在任何真实因果问题上走完 annotate → estimate → correct 全流程。Appendix B.18 (p31) 的 ClinicalBERT case study 最接近，但仍是回顾性分析，不是前瞻性应用。

这是两位 reviewer 共同识别的最大实践缺陷。

---

### [AGREE] R1-W3: Non-differential 假设脆弱性未在主文充分讨论

同意总体方向，但需补充论文已有的讨论：

1. **主文 p4 已有论证**：Section 3.1 第二段专门讨论了为什么 LLM 标注是 architecturally non-differential——"the LLM processes each text independently without access to Y, making non-differentiality an architectural invariant rather than an empirical approximation"。这个论证有一定说服力。

2. **但 R1 引用 B.25 的发现确实值得主文讨论**：p33 B.25 的 Y-stratified verification 显示 content-dependent proxies (topic, sentiment) 导致 12/12 rejections。这意味着虽然 LLM 不直接看到 Y，但当文本内容同时与 Y 和 A 相关时，misclassification 可以变得 effectively differential。这个 nuance 只在 Appendix 中讨论，主文确实不够。

建议：在 Section 3.1 的 non-differential 论证段落末尾增加 2-3 句，承认 content-dependent proxies 可能违反该假设，并引导读者到 B.25。

---

### [REBUT] R1-W4: Algorithm 1 阈值缺乏理论依据

部分不同意。

1. **K-stability 已有验证**：Appendix B.20 (p31-32) "Correction Method Sensitivity to K" 专门测试了 K=3,5,10 下校正方法的排序稳定性。Table 20 (p32) 显示所有7种拓扑的最优方法（Bold标注）在 K=3 和 K=5 之间保持一致（如 confounding 始终 PPI++, exposure 始终 SIMEX, M-bias 始终 SIMEX）。Grand ranking stability (p31) 报告 Spearman ρ 从 K=3 的 0.80 上升到 K=10 的 0.93。

2. **但 R1 关于"阈值"本身的关切有部分道理**：Algorithm 1 (p34) 中的具体数值阈值（如 Step 1 的 R ≤ 0.04、Step 12 的 RMSE reduction 47.0%/36.0%）确实来自 K=3 Dirichlet 的特定设置。Table 20 显示方法*排序*稳定，但 RMSE reduction 的具体数值在 K=10 时可能不同（如 PPI++ 在 K=10, confounding 下 reduction 从 85.6% 变为 -88%）。

**结论**：Algorithm 1 的*路由逻辑*（哪种拓扑用哪种方法）是 K-robust 的，但具体*阈值数值*可能需要 K-dependent calibration。建议在 Algorithm 1 caption 或 Section 4.5 中说明阈值是 K=3 参考值，并建议 practitioner 根据自己的 K 调整。这是 Should-Fix 而非 critical issue。

---

## 小问题

### [AGREE] R1-M1: Figure 2 caption 颜色含义
Figure 2 caption (p5) 写了 "Red = sign reversal"，但子图中红色的具体定义（是超过某个阈值还是 exact reversal？）不够精确。同意补充更明确的说明。

### [AGREE] R1-M2: Notation density
同意论文 notation 较重。Table 26 (p33) 的 notation table 放在 Appendix 最后才出现，如果移到 Section 3.1 之后或作为 footnote 提供会更友好。

### [REBUT] R1-M3: Dirichlet(1,1,1) 83.4% 过于悲观
不完全同意 R1 的措辞"容易给人过于悲观印象"。论文在报告 83.4% 之后，紧接着在 Section 4.2 (p7) 给出了 realistic LLM accuracy 下的结果："Under realistic LLM accuracy, sign reversal is confined to exposure"，并在 Table 1 (p7) 明确显示只有 exposure (83.4%) 和 IV (52.6%) 有 sign reversal。正文的叙事结构是"worst case → realistic case"，这是标准的 sensitivity analysis 呈现方式。但 Abstract 中的表述确实可以更明确地区分 uniform prior 和 realistic accuracy 两个场景。

### [AGREE] R1-M4: ASV 是渐近量，finite-sample 讨论不足
同意。Appendix B.8 (p27) 提供了 bootstrap confidence intervals 来处理 finite-sample uncertainty，B.23 (p32) 的 confusion matrix estimation robustness 测试了 n_gold = 50-500 的 stability（Spearman ρ ≥ 0.99 at n=500）。但主文未讨论 ASV 作为 plim-based quantity 的 finite-sample 修正。建议在 Section 3.3 增加一句引导到 B.8。

### [AGREE] R1-M5: "provably ineffective" 限定语
同意。"matrix-based corrections are provably ineffective" 应加上 "under linear OLS" 的限定。p8 Section 4.4 的上下文中有 "under linear OLS, FWL invariance implies..."，但 Abstract 和 Section 1 的表述可以更精确。Appendix B.15 Table 6 (p23) 明确显示 logistic 回归下 bias reduction 非零（虽然很小），这进一步说明限定语的重要性。

---

## 总体评价

R1 的审稿质量高，方法论关切大多准确。两位 reviewer 在以下问题上高度一致：
1. **端到端验证缺失**（R1-W2 = R2-N1）——这是最大的共同关切
2. **Conjecture 1 的理论开放性**（R1-N2 ≈ R2-W1）——严重程度判断略有差异
3. **Non-differential 假设讨论不足**（R1-W3 ≈ R2-W4）

唯一的实质分歧在 N2 的严重程度：R1 列为 Must-Fix/critical，我认为 Conjecture 标注已足够清晰，降为 Should-Fix 更合适。N1（proportional effects 遗漏）我完全同意 R1，但认为这是一个低成本修复——在 Limitations 中增加一句话即可。

**我维持 Overall 3.5 / 5 (Borderline Conference)**，与 R1 一致。


---

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

要点总结：
- **R1-N1 (proportional effects 遗漏)**：[AGREE]，Limitations 确实缺少该假设，B.13 Table 14 数据支持其重要性
- **R1-N2 (Conjecture 过渡不清)**：[REBUT]，Conjecture 标注和措辞已足够清晰，建议降为 Should-Fix
- **R1-W1 (symmetric C₀)**：[AGREE]，但补充 Conjecture 1 不要求对称性，实用性不受影响
- **R1-W2 (端到端验证)**：[AGREE]，与我的 N1 一致，是两位 reviewer 的共同最大关切
- **R1-W3 (non-differential 讨论不足)**：[AGREE]，B.25 的 content-dependent proxy 违反值得主文讨论
- **R1-W4 (Algorithm 1 阈值)**：[REBUT]，B.20 Table 20 已验证方法排序的 K-stability，但具体阈值数值可能需 K-dependent calibration

两位 reviewer 在端到端验证缺失、Conjecture 开放性、non-differential 假设三个问题上高度一致。

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

_source line 1672 · 2026-05-23T18:51:17.995853+00:00_

交叉回应已收回。两位 Reviewer 的逐条回应确认了已提交报告中的共识与分歧判断：

**收敛确认：**
- 端到端验证缺失 = 共同最大关切（虽然严重程度有分歧）
- Proportional effects 应补入 Limitations（R2 AGREE R1-N1）
- Non-differential 假设讨论应前置（双方 AGREE）
- ASV vs E-values 区分需强化（双方 AGREE）
- "first" 声称需精确化（双方 AGREE）

**分歧确认（严重程度而非实质）：**
- 端到端验证：R2 列 Must-Fix / R1 REBUT 为 Should-Fix（认为理论贡献自身有价值）
- Theorem→Conjecture 边界：R1 列 Must-Fix / R2 REBUT 为 Should-Fix（认为 "Conjecture" 标注已足够清晰）
- 线性 SEM：R1 REBUT R2-W2（认为 B.7/B.15 已提供充分非线性鲁棒性验证）

报告已于交叉回应前提交（3.5 Borderline Conference），当前交叉回应的细节与报告结论一致，无需修订。圆桌审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 166

## Round 166

2 recorded events


### User

_source line 1673 · 2026-05-23T19:43:26.263133+00:00_

[RESET REQUEST] Research Reviewer 达到硬限
  触发原因：运行时长 16h3m
  本轮累计 39 条消息 / 16h 3min

⚠️ 你自己的 context 状态：已 39 条消息 / 16h 3min

请回复：
  [RESET AGENT]     只重置 Research Reviewer，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 1674 · 2026-05-23T19:43:39.548633+00:00_

[RESET BOTH]

审稿已完成：报告已通过 `submit_review_report_to_research_director` 投递（Overall 3.5 — Borderline Conference），Issue Tracker 已同步更新至 Round 20。本轮所有 Reviewer 交叉回应已收集、共识已达成，无待处理工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 167

## Round 167

62 recorded events


### User

_source line 1675 · 2026-05-23T19:47:17.420064+00:00_

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

_source line 1676 · 2026-05-23T19:47:26.756766+00:00_

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

_source line 1677 · 2026-05-23T19:47:26.858107+00:00_

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

_source line 1678 · 2026-05-23T19:47:36.149949+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1679 · 2026-05-23T19:47:36.251059+00:00_



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

_source line 1680 · 2026-05-23T19:47:38.309799+00:00_

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

_source line 1681 · 2026-05-23T19:47:38.360342+00:00_



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

_source line 1682 · 2026-05-23T19:47:43.335584+00:00_

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

_source line 1683 · 2026-05-23T19:47:44.191146+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1684 · 2026-05-23T19:47:44.191662+00:00_

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

_source line 1685 · 2026-05-23T19:47:46.407311+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex 2>/dev/null && echo \"MAIN_TEX_EXISTS\" || echo \"MAIN_TEX_MISSING\"",
  "description": "Check if main.tex exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex 2>/dev/null && echo \"MAIN_TEX_EXISTS\" || echo \"MAIN_TEX_MISSING\"",
    "description": "Check if main.tex exists"
  }
}
```

</details>

---


### Tool result

_source line 1686 · 2026-05-23T19:47:47.060742+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1551 May 23 13:23 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
MAIN_TEX_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 1687 · 2026-05-23T19:47:47.161759+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_21/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_21/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1688 · 2026-05-23T19:47:47.262623+00:00_

-rw-r--r-- 1 ubuntu ubuntu 955061 May 23 19:45 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_21/submitted.pdf
PDF_EXISTS

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


### Tool result

_source line 1689 · 2026-05-23T19:47:49.975876+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found several results related to EM
…[truncated 1313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 5784
}
```

</details>

---


### Tool call

_source line 1690 · 2026-05-23T19:47:53.445105+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
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
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 1691 · 2026-05-23T19:47:53.746929+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity policy"
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
    "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity policy"
  }
}
```

</details>

---


### Tool result

_source line 1692 · 2026-05-23T19:47:59.673382+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"}]

Based on the search results, here's the information about EMNLP 2026 call for papers submission deadline and ARR commitment:

## Submission De
…[truncated 1234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6228
}
```

</details>

---


### Tool result

_source line 1693 · 2026-05-23T19:48:01.129726+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit anonymity policy"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results, here are the key guidelines for ACL Rolling Review 2026 submissions regarding page limits and anonymity policy:

## Page Limits

The page limit is 4 pages for short papers and 8 pages for long papers, excluding ethical considerations and limitations.

## Anonymity Policy

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identitie
…[truncated 944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7382
}
```

</details>

---


### Tool call

_source line 1694 · 2026-05-23T19:48:16.543942+00:00_

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

_source line 1695 · 2026-05-23T19:48:16.946402+00:00_

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
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1696 · 2026-05-23T19:48:17.449135+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1697 · 2026-05-23T19:48:18.605045+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_annot_error_attrib'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1698 · 2026-05-23T19:48:18.655594+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1699 · 2026-05-23T19:48:19.711402+00:00_

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
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Section 3.2 已添加 ASV 替代讨论。"
    resolution_round: 3

  - id: R1-W3
    category: experiments
    severity: should-fix
    summary: "实证验证不完整：缺少商业 LLM"
    status: in_progress
    first_raised_round: 1
    last_seen_round: 20
    mentions:
      - roun
…[truncated 22227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 1700 · 2026-05-23T19:48:19.761966+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1701 · 2026-05-23T19:48:19.812772+00:00_

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

_source line 1702 · 2026-05-23T19:48:27.457970+00:00_

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

_source line 1703 · 2026-05-23T19:48:27.508814+00:00_

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

_source line 1704 · 2026-05-23T19:48:28.916470+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config header"
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config header"
  }
}
```

</details>

---


### Tool result

_source line 1705 · 2026-05-23T19:48:29.017261+00:00_

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

_source line 1706 · 2026-05-23T19:48:31.680934+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 1707 · 2026-05-23T19:48:31.731578+00:00_

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

_source line 1708 · 2026-05-23T19:48:34.143670+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510 -maxdepth 2 -name \"config.yaml\" -o -name \"projects.yaml\" 2>/dev/null | head -5",
  "description": "Find project config"
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
    "command": "find /home/ubuntu/.agent-ml-research-prod_0510 -maxdepth 2 -name \"config.yaml\" -o -name \"projects.yaml\" 2>/dev/null | head -5",
    "description": "Find project config"
  }
}
```

</details>

---


### Tool result

_source line 1709 · 2026-05-23T19:48:34.194325+00:00_

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

_source line 1710 · 2026-05-23T19:48:36.658070+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/*.yaml /home/ubuntu/.agent-ml-research-prod_0510/*.yml /home/ubuntu/.agent-ml-research-prod_0510/config/ 2>/dev/null",
  "description": "Find config location"
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
    "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/*.yaml /home/ubuntu/.agent-ml-research-prod_0510/*.yml /home/ubuntu/.agent-ml-research-prod_0510/config/ 2>/dev/null",
    "description": "Find config location"
  }
}
```

</details>

---


### Tool result

_source line 1711 · 2026-05-23T19:48:36.759147+00:00_

Exit code 2
/home/ubuntu/.agent-ml-research-prod_0510/workspace.yaml

/home/ubuntu/.agent-ml-research-prod_0510/config/:
approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
email_tokens.json
email_tokens.json.bak.20260521T061054Z
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_director.json
mcp_config_distiller.json
mcp_config_dream_review_director.json
mcp_config_idea_reviewer.json
mcp_config_no_project.json
mcp_config_paper_agent.json
mcp_config_paper_audit_content.json
mcp_config_paper_audit_review_visual.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
mcp_config_worker_29834432f6498e7996daf9a6d4e8eda9.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
mcp_config_worker_3683e51e3c097c93488562d683342ec7.json
mcp_config_worker_421decd2032b14f2ef6566c2172240c1.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_91888988436c01dfc0d65cc645a31cd1.json
mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
mcp_config_worker_af98c2743afa33d94f043b9d3e70ed88.json
mcp_config_worker_ddf919c12f9233b9c1be7884efc37bb6.json
mcp_config_worker_e2d981ca8df69fe85b404249e1ed8253.json
mcp_config_worker_e660d20289ab9bbb488d128f5d99bf46.json
mcp_config_worker_ec7b7c2246633b015619e121164ce6bf.json
mcp_config_worker_f265de7a9796688b878083fef59f9d4c.json
mcp_config_worker_f40e094d561eafca7f3a1e02207f47a0.json
pending_approval_notifications.yaml
pool.json
projects
resources.yaml
secrets
session_state.json
tum_pending_tum_20260521_083500_openrouter.json
venue_registry.yaml
venue_rules

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


### Tool call

_source line 1712 · 2026-05-23T19:48:40.031252+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/config/projects/causal_annot_error_attrib.yaml 2>/dev/null | grep -A10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_SECTION\"",
  "description": "Check external review config in project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/config/projects/causal_annot_error_attrib.yaml 2>/dev/null | grep -A10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_SECTION\"",
    "description": "Check external review config in project config"
  }
}
```

</details>

---


### Tool result

_source line 1713 · 2026-05-23T19:48:40.081946+00:00_

NO_EXTERNAL_REVIEW_SECTION

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

_source line 1714 · 2026-05-23T19:48:49.134897+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/*.tex",
  "description": "List all tex files"
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
    "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/*.tex",
    "description": "List all tex files"
  }
}
```

</details>

---


### Tool result

_source line 1715 · 2026-05-23T19:48:49.185528+00:00_

/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conjecture_dgp_sensitivity_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_demo_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/exp_a_stress_test_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/exp_e_asv_stability_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/k3_symmetric_proof.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex

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

_source line 1716 · 2026-05-23T19:48:54.211069+00:00_

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

_source line 1717 · 2026-05-23T19:48:54.663699+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification in linear structural equation models and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy, sign reversal of non-dominant coefficients occurs under exposure; under empirical LLM matrices (diagonal 0.45--0.81), sign reversal is confined to exposure; IV is fragile under uniform Dirichlet priors but exhibits zero reversals under empirical LLM matrices. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$) and numerically verified ($K{\geq}3$) monotonicity, yielding a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
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

_source line 1718 · 2026-05-23T19:48:54.664360+00:00_

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

_source line 1719 · 2026-05-23T19:48:55.116856+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors (equivalently, misclassification) from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient is
…[truncated 3194 chars]

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

_source line 1720 · 2026-05-23T19:48:55.167804+00:00_

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

_source line 1721 · 2026-05-23T19:48:55.520038+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes probability limits (plim, $N \to \infty$) rather than finite-sample variance. The FWL theorem~\cite{frisch1933partial} guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables---this is why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}). Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}) collects all notation.
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	In batch annotation pipelines, the LLM processes each text independently without access to $Y$, making non-differentiality an architectural invariant~\cite{ziems2024can}. Y-stratified permutation tests across 12 configurations confirm this (1/12 rejection at $\alpha{=}0.05$; Appendix~\ref{sec:y_stratified_test},~\ref{sec:nondiff_verify}): only content-dependent proxy variables (topic, sentiment) show significant Y-stratificati
…[truncated 14289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1722 · 2026-05-23T19:48:55.570760+00:00_

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

_source line 1723 · 2026-05-23T19:48:55.621578+00:00_

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
15	Analytical probability limits match Monte Carlo estimates with MAPE of 1.6\%, averaged across 161 scenarios (23 LLM configurations $\times$ 7 topologies; per-topology range: 0.3\%--3.7\%).
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; at diagonal $\geq 0.9$, violation persists at 11.9\% (Appendix~\ref{sec:iv_dirichlet_subspace}). Under the full Dirichlet prior, 85\% of matrices violate the binary ``toward-null'' guarantee and 83.4\% cause sign reversal; $\min_k C_{kk} < 0.55$ predicts sign reversal with 91\% accuracy (Appendix~\ref{sec:sign_determinants}). The $K{=}2$ control confirms classical attenuation~\cite{brenner1993}, establishing the multi-class failure as structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\ref{conj:monotone}); M-bias shows weakest sensitivity (53.2\% violation). All patterns persist at $K{=}5,7$ (Appendix~\ref{sec:cross_k_robustness}).
22	
23	\paragraph{IV: W
…[truncated 6137 chars]

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

_source line 1724 · 2026-05-23T19:49:00.152338+00:00_

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

_source line 1725 · 2026-05-23T19:49:00.704379+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: at $K{\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs yield a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four covariate topologies (FWL invariance). Practitioners should identify their topology and compute ASV before selecting corrections.
5	
6	\section*{Limitations}
7	
8	We assume non-differential misclassification (Appendix~\ref{sec:nondiff_stress}). Closed-form results (Theorems~1--2) assume linear SEMs with proportional effects ($f{=}\lambda g$); logistic robustness is verified in Appendix~\ref{sec:fwl_nonlinear}, and sign preservation holds at 97.3\% under non-proportional effects (Table~\ref{tab:proportional_empirical}), though $\lambda(C)$ falls outside $[0,1]$ in 15\% of configurations; under nonlinear models, FWL invariance may break, enabling matrix-based corrections. Proving general $K{\geq}3$ envelope monotonicity beyond symmetric matrices remains open~\cite{schennach2020mismeasured}.
9	

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

_source line 1726 · 2026-05-23T19:49:00.704673+00:00_

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

_source line 1727 · 2026-05-23T19:49:01.256991+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	Foundations appear in \citet{carroll2006, gustafson2004, buonaccorsi2010, bound2001measurement}, with DAG-based formalization by \citet{hernan_cole2009} and \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{bross1954misclassification, brenner1993, ogburn_vanderweele2012}, but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. Extensions address differential measurement error~\cite{edwards_lessler_naimi2021, imai_yamamoto2010}, endogenous misreporting~\cite{nguimkeu_denteh_tchernis2019}, mismeasured covariates under IPW~\cite{shu_yi2019a, shu_yi2019b}, mediation with mismeasured mediators~\cite{valeri_vanderweele2013}, nonclassical error~\cite{schennach2020mismeasured}, and multiply robust estimation~\cite{wei2025multiply}. All analyze a single DAG topology; ours characterizes how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document rapid LLM annotator adoption (surveyed by \citealt{tan2024llm}), \citet{baumann2025} found 31\% incorrect conclusions, and \citet{kim_garg2025} showed 60\% error correlation across models~\cite{pangakis_wolken_fasching2023, cheng_mayya_sedoc2024, variance_aware_llm2026, hidden_measurement_error2026}. \citet{audinet2025} benchmark debiasing; \citet{keith_jensen_oconnor2020} survey the landsca
…[truncated 1088 chars]

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

_source line 1728 · 2026-05-23T19:49:01.257494+00:00_

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

_source line 1729 · 2026-05-23T19:49:01.558812+00:00_

File content (45824 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

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

_source line 1730 · 2026-05-23T19:49:42.085587+00:00_

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

_source line 1731 · 2026-05-23T19:50:04.311952+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22226
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-23T19:50:04.363237+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **投稿类别**: ARR Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（不含 limitations、ethical considerations、references）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不要求必须阅读\n\n## 论文文件\n- LaTeX 源码: `projects/causal_annot_error_attrib/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, related_work.tex, appendix_proofs.tex）\n- PDF: `projects/causal_annot_error_attrib/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **理论正确性**：\n   - Theorem 1（K=2 envelope monotonicity）和 Theorem 2（K=3 symmetric monotonicity）的证明是否完整、正确？\n   - Proposition 1（sign preservation）的条件是否充分？\n   - Conjecture 1 的数值验证是否充分？adversarial search 是否有遗漏的病态结构？\n   - 各拓扑的 bias expression 推导是否正确？\n\n2. **假设合理性**：\n   - Non-differential misclassification 假设在 LLM annotation 场景下是否合理？论文的论证（architectural invariant + Y-stratified test）是否充分？\n   - Proportional effects 假设（f=λg）在 NLP 应用中是否合理？97.3% 的经验验证是否足够？论文是否充分讨论了该假设失败时的后果？\n   - Linear SEM 假设对 EMNLP 读者是否可达？logistic robustness 验证是否充分？\n   - Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中的适用性如何？\n\n3. **实验有效性**：\n   - Monte Carlo 验证的 1.6% MAPE 是否可靠？161 scenarios 覆盖是否充分？\n   - 23 个 LLM configurations 是否足够代表性？缺少商业 LLM 是否构成重大局限？\n   - Dirichlet 采样是否能充分覆盖真实 LLM 混淆矩阵的分布？\n   - 端到端因果应用验证是否缺失？对 EMNLP 应用导向 venue 的影响如何？\n\n4. **数学规范性**：\n   - 符号使用是否一致？定义是否完整？\n   - plim 推导的严谨性\n   - ASV 定义域和单调性论证的完备性\n\n请按以下格式输出审稿意见：\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[S1] ...\n[S2] ...\n\n## Weaknesses\n[W1] [severity: must-fix/should-fix/minor] ...\n[W2] ...\n\n## Questions\n[Q1] ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\n[评分（参考 ARR 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit）+ 置信度 + 简要理由]\n```"
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
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **投稿类别**: ARR Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（不含 limitations、ethical considerations、references）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不要求必须阅读\n\n## 论文文件\n- LaTeX 源码: `projects/causal_annot_error_attrib/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, related_work.tex, appendix_proofs.tex）\n- PDF: `projects/causal_annot_error_attrib/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **理论正确性**：\n   - Theorem 1（K=2 envelope monotonicity）和 Theorem 2（K=3 symmetric monotonicity）的证明是否完整、正确？\n   - Proposition 1（sign preservation）的条件是否充分？\n   - Conjecture 1 的数值验证是否充分？adversarial search 是否有遗漏的病态结构？\n   - 各拓扑的 bias expression 推导是否正确？\n\n2. **假设合理性**：\n   - Non-differential misclassification 假设在 LLM annotation 场景下是否合理？论文的论证（architectural invariant + Y-stratified test）是否充分？\n   - Proportional effects 假设（f=λg）在 NLP 应用中是否合理？97.3% 的经验验证是否足够？论文是否充分讨论了该假设失败时的后果？\n   - Linear SEM 假设对 EMNLP 读者是否可达？logistic robustness 验证是否充分？\n   - Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中的适用性如何？\n\n3. **实验有效性**：\n   - Monte Carlo 验证的 1.6% MAPE 是否可靠？161 scenarios 覆盖是否充分？\n   - 23 个 LLM configurations 是否足够代表性？缺少商业 LLM 是否构成重大局限？\n   - Dirichlet 采样是否能充分覆盖真实 LLM 混淆矩阵的分布？\n   - 端到端因果应用验证是否缺失？对 EMNLP 应用导向 venue 的影响如何？\n\n4. **数学规范性**：\n   - 符号使用是否一致？定义是否完整？\n   - plim 推导的严谨性\n   - ASV 定义域和单调性论证的完备性\n\n请按以下格式输出审稿意见：\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[S1] ...\n[S2] ...\n\n## Weaknesses\n[W1] [severity: must-fix/should-fix/minor] ...\n[W2] ...\n\n## Questions\n[Q1] ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\n[评分（参考 ARR 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit）+ 置信度 + 简要理由]\n```"
  }
}
````

</details>

---


### Tool result

_source line 1733 · 2026-05-23T19:50:21.353278+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16990
}
```

</details>

---


### Tool call

_source line 1734 · 2026-05-23T19:50:21.455055+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **投稿类别**: ARR Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（不含 limitations、ethical considerations、references）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不要求必须阅读\n\n## 论文文件\n- LaTeX 源码: `projects/causal_annot_error_attrib/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, related_work.tex, appendix_proofs.tex）\n- PDF: `projects/causal_annot_error_attrib/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与贡献定位**：\n   - \"first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies\" 这一声明是否成立？与 Brenner (1993)、Dosemeci (1990)、Teblunthuis (2024)、Lee & Wood-Doughty (2024) 的区分是否清晰？\n   - ASV 框架相对于 E-values、partial R² 等已有 sensitivity analysis 工具的增量创新在哪里？Remark 1 对 ASV vs E-values 的区分是否令人信服？\n   - 三个贡献（bias taxonomy + ASV + correction routing）的相对权重是否合理？correction routing 作为贡献之一是否实质性够强？\n   - 对 EMNLP venue 而言，这种偏数理统计的工作是否有足够的 NLP 连接？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作？特别是：measurement error 文献、NLP causal inference 文献、sensitivity analysis 文献\n   - 引用是否真实？是否有虚构引用的迹象？\n   - 对已有工作的定位（positioning）是否公平？\n\n3. **写作质量**：\n   - Abstract 是否符合 200 words 限制？内容是否过于技术化？\n   - Introduction 的叙事逻辑是否清晰？数字密度是否过高？\n   - Section 3（Method）对 NLP 读者的可达性如何？plim、FWL 等计量概念是否有足够解释？\n   - Conclusion 和 Limitations 是否充分？\n\n4. **格式合规**：\n   - 正文是否不超过 8 页？\n   - 匿名性是否保持（无自我引用暴露）？\n   - 引用格式是否正确（natbib）？\n   - Limitations section 是否存在且位置正确（正文内，非附录）？\n\n请按以下格式输出审稿意见：\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[S1] ...\n[S2] ...\n\n## Weaknesses\n[W1] [severity: must-fix/should-fix/minor] ...\n[W2] ...\n\n## Questions\n[Q1] ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\n[评分（参考 ARR 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit）+ 置信度 + 简要理由]\n```"
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
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **投稿类别**: ARR Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（不含 limitations、ethical considerations、references）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不要求必须阅读\n\n## 论文文件\n- LaTeX 源码: `projects/causal_annot_error_attrib/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, related_work.tex, appendix_proofs.tex）\n- PDF: `projects/causal_annot_error_attrib/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与贡献定位**：\n   - \"first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies\" 这一声明是否成立？与 Brenner (1993)、Dosemeci (1990)、Teblunthuis (2024)、Lee & Wood-Doughty (2024) 的区分是否清晰？\n   - ASV 框架相对于 E-values、partial R² 等已有 sensitivity analysis 工具的增量创新在哪里？Remark 1 对 ASV vs E-values 的区分是否令人信服？\n   - 三个贡献（bias taxonomy + ASV + correction routing）的相对权重是否合理？correction routing 作为贡献之一是否实质性够强？\n   - 对 EMNLP venue 而言，这种偏数理统计的工作是否有足够的 NLP 连接？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作？特别是：measurement error 文献、NLP causal inference 文献、sensitivity analysis 文献\n   - 引用是否真实？是否有虚构引用的迹象？\n   - 对已有工作的定位（positioning）是否公平？\n\n3. **写作质量**：\n   - Abstract 是否符合 200 words 限制？内容是否过于技术化？\n   - Introduction 的叙事逻辑是否清晰？数字密度是否过高？\n   - Section 3（Method）对 NLP 读者的可达性如何？plim、FWL 等计量概念是否有足够解释？\n   - Conclusion 和 Limitations 是否充分？\n\n4. **格式合规**：\n   - 正文是否不超过 8 页？\n   - 匿名性是否保持（无自我引用暴露）？\n   - 引用格式是否正确（natbib）？\n   - Limitations section 是否存在且位置正确（正文内，非附录）？\n\n请按以下格式输出审稿意见：\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[S1] ...\n[S2] ...\n\n## Weaknesses\n[W1] [severity: must-fix/should-fix/minor] ...\n[W2] ...\n\n## Questions\n[Q1] ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\n[评分（参考 ARR 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit）+ 置信度 + 简要理由]\n```"
  }
}
````

</details>

---


### Tool result

_source line 1735 · 2026-05-23T19:50:22.813038+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1357
}
```

</details>

---


### Assistant

_source line 1736 · 2026-05-23T19:50:30.787539+00:00_

已派发：
- 视觉审查 Agent：已启动（fire-and-forget）
- Reviewer 1（方法严谨性）：已派发
- Reviewer 2（新颖性/完整性）：已派发

等待两位 Reviewer 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 168

## Round 168

2 recorded events


### User

_source line 1737 · 2026-05-23T19:50:32.292187+00:00_

[SYSTEM] Research Reviewer 刚完成 context rotation (Loop 5)，已读取 handoff 并就绪。如有待办任务请立即分配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 1738 · 2026-05-23T19:50:38.390305+00:00_

Reviewer 1 和 Reviewer 2 的审稿任务已在上一轮分配，等待返回结果。无新任务需要分配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 169

## Round 169

2 recorded events


### User

_source line 1739 · 2026-05-23T19:56:25.342995+00:00_

[Reviewer 1 审稿意见]:

## Summary

本文研究多类别（K≥3）LLM 标注误差如何在因果推断中传播，覆盖 7 种典型 DAG 拓扑。作者推导了每种拓扑下的 bias 表达式，证明了 K=2（Theorem 1）和 K=3 对称混淆矩阵（Theorem 2）下的 envelope monotonicity，定义了 Annotation Sensitivity Values (ASV) 作为诊断工具，并提出了 topology-aware 校正路由算法（Algorithm 1）。理论结果通过 161 scenarios 的 Monte Carlo 验证（MAPE 1.6%）和 23 个 LLM 配置的经验验证支撑。

## Strengths

[S1] **系统性的拓扑分类学**：对 7 种 DAG 拓扑逐一推导 bias 表达式（Section 3.2, Appendix A.3-A.9），揭示了拓扑结构决定 bias 方向和幅度的核心洞见。特别是 sign reversal 只在 exposure (IV) 拓扑下发生的发现（Table 1, Appendix A.9），对实践者有直接指导意义。这是一个真正的、此前文献中缺失的贡献。

[S2] **证明的严谨性**：我逐步检查了 Theorem 1（Appendix A.4）和 Theorem 2（Appendix A.6）的证明。Theorem 1 通过 perspective function 的凸性论证 B(C(δ)) 的单调性，推导链条完整。Theorem 2 将问题归约为 V_b(x) 在 [0,1] 上严格递减，利用 C₀ 的对称分解 C₀ = (1-3c)I + c·11ᵀ 得到干净的因式分解形式（公式 23），sign analysis 正确。Proposition 1-3 的 Cauchy-Schwarz 论证也是标准且正确的。

[S3] **诚实的理论边界声明**：论文没有过度宣称。Theorem 2 的对称 C₀ 限制在 Remark 4（p.18）中被坦诚讨论为"a theoretical anchor rather than a universal guarantee"；Conjecture 1 被正确标注为 conjecture 而非 theorem；proportional effects 假设的违反率（Table 14, ~23% for independent f,g）被量化报告。这种学术诚实度值得肯定。

[S4] **充分的数值验证体系**：100,000 Dirichlet 矩阵采样 + 545,945 条 adversarial 曲线验证 Conjecture 1（max violation 0.016 < 0.02）；23 个真实 LLM 混淆矩阵验证 sign preservation（97.3%）；Monte Carlo 验证解析表达式（MAPE 1.6%）。多层验证体系为理论结果提供了强有力的经验支撑。

[S5] **实用的诊断框架**：ASV 的三维度设计（magnitude/significance/sign-flip）和 Algorithm 1 的校正路由为实践者提供了可操作的工具。Table 4 的 topology-specific vulnerability ranking 和 Figure 3 的可视化直观有效。

## Weaknesses

[W1] [severity: must-fix] **Theorem 2 的对称 C₀ 假设与实际 LLM 混淆矩阵严重脱节**
- 具体位置：Theorem 2 (Section 3.1, p.6), Remark 4 (Appendix A.6, p.18)
- 问题：Theorem 2 要求 K=3 混淆矩阵 C₀ 完全对称（所有 off-diagonal 元素相等：a=b=c）。但 Remark 4 自己报告，10 个 VAST 配置的真实 LLM 混淆矩阵中位相对 Frobenius 距离 d_rel = 0.33（范围 0.29-0.38），即实际矩阵与对称矩阵偏差约 33%。这意味着 Theorem 2 的理论保证在实际场景中基本不适用。论文试图用 Conjecture 1 的数值验证弥合这一缺口，但这实质上将 K≥3 的核心理论贡献降格为一个经验观察。
- 为什么影响接收：论文的核心 claim 之一是提供"closed-form"和"provable"的 monotonicity 结果。如果主要适用场景（K≥3，非对称矩阵）只能依赖 conjecture，理论贡献的强度显著削弱。
- 建议修改方向：(a) 尝试证明一个更弱但更实用的结果，例如"near-symmetric"矩阵（d_rel < ε）下的近似单调性保证；(b) 或者在正文中更明确地重新定位 Theorem 2 的角色——不是作为实用工具，而是作为精确案例研究，证明单调性结构在特定条件下是精确成立的，从而为 Conjecture 1 提供结构性支撑。当前的处理方式（正文 p.6 表述为 Theorem，附录才承认局限）可能误导读者。

[W2] [severity: must-fix] **缺少端到端的真实 NLP 因果推断应用**
- 具体位置：Section 4 (Experiments), Appendix B.3 (ClinicalBERT), B.19 (End-to-End Demo)
- 问题：对于 EMNLP 这个应用导向的 venue，论文的实验验证主要是"验证理论正确性"（Monte Carlo vs. 解析解）和"验证假设成立"（non-differential test, proportional effects test），缺少一个完整的场景：在真实 NLP 任务中，使用 LLM 标注数据进行因果推断，展示本文框架如何改变实质性的因果结论。ClinicalBERT 案例（Appendix B.3）使用了真实 LLM 混淆矩阵，但 ground truth 因果效应是合成的。End-to-End Demo（B.19）同样基于合成 DGP。
- 为什么影响接收：ARR reviewer guidelines 强调 "a paper only needs to present sufficient evidence for the claim that the authors are making"。论文 claim 这个框架对使用 LLM 标注的 NLP 研究者有实践价值（Introduction: "practitioners should identify their topology and compute ASV before selecting corrections"），但没有展示一个真实研究者会遇到的场景。
- 建议修改方向：增加一个真实 NLP 因果推断案例，例如：(a) 使用 LLM 标注的政治立场检测数据，估计社交媒体曝光对政治态度的因果效应，比较 naive/corrected 估计；(b) 使用 HumAID 的灾害推文，估计灾害类型对公众响应的因果效应。关键是展示校正前后的因果结论差异，而不仅是 bias 数值变化。

[W3] [severity: should-fix] **Proportional effects 假设的违反后果讨论不充分**
- 具体位置：Section 3.2 (p.4, footnote), Appendix B.13 (Table 14), Appendix B.17 (Table 18)
- 问题：Proportional effects (f = λg) 是 Theorems 1-2 单调性证明的核心假设。Table 14 显示，当 f 和 g 完全独立时，out-of-bounds 率达 23%；Table 18 显示 97.3% 的配置在 non-proportional 下仍保持 sign preservation，但这混合了 proportional 和 non-proportional 情况。关键问题是：在 NLP 因果推断的典型场景中，proportional effects 有多合理？例如，在混淆拓扑中，confounder 对 treatment 和 outcome 的效应有什么理由是成比例的？论文没有提供足够的实质性论证。
- 建议：在正文中增加 1-2 句讨论 proportional effects 在典型 NLP 因果场景中的合理性（或不合理性），而不仅仅是报告违反率。如果该假设在实践中经常不成立，需要明确说明 monotonicity 结果在什么条件下可以被信赖。

[W4] [severity: should-fix] **Linear SEM 假设的适用范围在正文中讨论不足**
- 具体位置：Section 3.1 (Setup), Limitations (p.8), Appendix B.7 (Table 6)
- 问题：整个框架建立在线性 SEM 上。Table 6（Appendix B.7）的 logistic regression 鲁棒性测试显示，对于 covariate 拓扑，FWL 不变性保持（bias reduction negligible），但对 exposure 拓扑，logistic regression 下的校正实际上恶化了 bias（-78%）。这意味着对于 EMNLP 读者常用的非线性模型，本文的校正建议可能是有害的。Limitations section 提及了这一点但过于简略（"FWL-based routing may not apply under nonlinear models"）。
- 建议：在 Limitations 或 Section 4.5 中更突出地讨论：(a) 哪些拓扑的结论在非线性模型下仍然成立（covariate 拓扑）；(b) 哪些不成立且校正可能反向（exposure）；(c) 实践者在使用非线性模型时应如何调整策略。

[W5] [severity: should-fix] **Conjecture 1 的验证覆盖范围可能不足**
- 具体位置：Conjecture 1 (Section 3.1, p.6), Appendix A.11 (p.21-22)
- 问题：Adversarial search 覆盖了 4 种结构族（near-permutation, block-diagonal, sparse, near-uniform），但这些族的选择似乎是基于直觉而非系统性的参数空间覆盖。100,000 Dirichlet 采样均匀覆盖了 simplex，但可能遗漏了高维空间中的稀疏病态区域。特别是，论文报告 near-permutation 矩阵是"最具挑战性"的（max violation 0.016），但没有解释为什么不存在更病态的结构。
- 建议：增加 adversarial search 的系统性说明——为什么这 4 种结构族足以覆盖潜在的 counterexample 空间？是否尝试过基于梯度的 adversarial optimization 来寻找最大违反？

[W6] [severity: minor] **符号负担较重，对 EMNLP 读者不够友好**
- 具体位置：全文，特别是 Section 3.1-3.3
- 问题：论文大量使用计量经济学/测量误差文献的符号（plim, FWL, δ-interpolation, Vb/Vw 分解等），对于 EMNLP 的主要读者群（NLP/ML 背景）可能较难跟随。虽然 notation table（Table 26, p.34）在附录中提供了参考，但正文中缺少足够的直觉解释来帮助非计量背景的读者。
- 建议：在 Section 3.1 中增加一个简短的"intuition"段落，用非技术语言解释 bias 传播的核心机制，再进入形式化推导。

## Questions

[Q1] Theorem 1 的证明（Appendix A.4, Step 4）提到 general case（non-proportional f）的严格单调性证明"remains open"。这对 K=2 的实际应用有什么影响？是否意味着即使在 K=2 下，非比例效应也可能导致 envelope 非单调？数值验证（p.17 底部）显示 proportional 和 non-proportional 两种情况下 λ(C) 的行为——能否更明确地量化 non-proportional case 的 monotonicity violation 范围？

[Q2] Table 1 报告 sign-flip guarantee 对所有非 exposure 拓扑成立（sign(plim τ̂) = sign(τ)），条件是 C₁₄ > 0。但在实际 LLM 混淆矩阵中，某些 off-diagonal 元素是否可能为 0（例如某些类别之间完全不会混淆）？如果 C₁₄ = 0 对某些 (j,k) 成立，sign preservation 是否仍然成立？

[Q3] Algorithm 1 中的阈值（e.g., "risk level" 分类，PPI++ vs DSL 的选择条件）是如何确定的？这些是否可以从理论或数据驱动的方式得出，还是纯粹基于启发式？Table 5 的校正方法比较中，不同方法的选择标准是否应该取决于 sample size 或其他实验条件？

[Q4] Non-differential misclassification 的验证（Appendix B.25）显示"content-dependent"proxy variables 产生了显著的 Y-stratification。在 stance detection 等任务中，标注变量与文本内容高度耦合——这是否意味着 non-differential 假设在这类核心 NLP 任务中系统性地不成立？论文如何建议实践者在这种情况下使用本框架？

## Missing References

无明显遗漏。论文引用覆盖了测量误差（Bound et al., Carroll et al.）、因果推断（Pearl, VanderWeele）、LLM 标注（Gilardi et al., Tan et al., Baumann et al.）和校正方法（Angelopoulos et al., Egami et al.）等核心文献。

## Overall Assessment

**Overall**: 3.5 (Borderline Conference)
**Confidence**: 4/5 (Quite sure — 我逐步验证了核心证明并熟悉测量误差和因果推断文献)

**理由**：

本文在一个重要且日益相关的问题（LLM 标注误差的因果传播）上做出了系统性的理论贡献。7 种拓扑的 bias 分类学是新颖且有用的，证明在其假设范围内是正确的，ASV 诊断工具有实践价值。

阻碍评分达到 4.0 (Conference) 的主要原因：

1. **理论覆盖与实际需求的错位**：Theorem 2 的对称假设在实际 LLM 场景中偏差约 33%（作者自己的数据），意味着 K≥3 的理论保证主要依赖未证明的 Conjecture 1。这不是一个错误，但它减弱了理论贡献的力度。

2. **应用验证的缺失**：对于 EMNLP venue，缺少一个真实 NLP 因果推断应用是显著短板。当前所有实验都是"验证理论"而非"展示影响"。

3. **假设的 NLP 适用性论证不足**：Non-differential misclassification、proportional effects、linear SEM 这三个核心假设在 NLP 场景中的合理性讨论分散在附录各处，缺少整合性的讨论。

如果作者能：(a) 增加一个真实 NLP 因果推断案例展示框架的实际价值；(b) 将 Theorem 2 在正文中更准确地定位为"theoretical anchor + numerical evidence for general case"的组合贡献；(c) 在正文中整合讨论三个核心假设的 NLP 适用性——这篇论文可以达到 Conference 水平。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 证明在假设范围内正确；但 K≥3 主要结论依赖 conjecture，Theorem 2 实际适用性有限 |
| Excitement | 3/5 | 问题重要且日益相关；bias taxonomy 新颖；但缺少令人信服的应用演示，实际影响待验证 |
| Reproducibility | 4/5 | 所有参数、采样方案、验证步骤详细记录；代码路径在附录中提及；符合 reproducibility 标准 |
| Overall Assessment | 3.5/5 | Borderline Conference — 理论贡献扎实但假设窄、应用展示不足 |
| Confidence | 4/5 | 逐步验证了核心证明，熟悉相关文献 |


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

_source line 1740 · 2026-05-23T19:56:31.678643+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 170

## Round 170

2 recorded events


### User

_source line 1741 · 2026-05-23T19:56:50.392051+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评审摘要**：Overall 3.5 (Borderline Conference)，Soundness 3.5/5，Excitement 3/5。

**核心发现**：
- 证明在其假设范围内正确（Theorem 1/2, Proposition 1-3 均经逐步验证）
- 7 种拓扑的 bias 分类学是新颖且有用的贡献
- 两个 must-fix 问题：(1) Theorem 2 的对称 C₀ 假设与实际 LLM 混淆矩阵偏差约 33%，K≥3 的理论保证实质上依赖未证明的 Conjecture 1；(2) 缺少端到端的真实 NLP 因果推断应用
- 三个 should-fix：proportional effects 假设的 NLP 适用性论证不足、linear SEM 限制在正文讨论不够、Conjecture 1 的 adversarial search 覆盖系统性不明
- 一个 minor：符号负担对 EMNLP 读者偏重

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

_source line 1742 · 2026-05-23T19:56:54.526210+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 171

## Round 171

6 recorded events


### User

_source line 1743 · 2026-05-23T19:58:05.481737+00:00_

[Reviewer 2 审稿意见]:
## Summary

本文研究 LLM 生成的多分类标注误差如何在不同因果 DAG 拓扑下传播到下游因果估计中。作者推导了 7 种典型 DAG 拓扑下 K 类非差异性误分类的偏差表达式，证明 K≥3 时存在二分类所不具有的符号反转可能性，并提出 Annotation Sensitivity Values (ASV) 作为脆弱性诊断工具。此外，作者基于 Frisch-Waugh-Lovell 不变性指出矩阵校正方法在四种拓扑下无效，并提供拓扑感知的校正路由指南。

## Strengths

**[S1] 系统性覆盖多拓扑 × 多分类的真空地带。** Brenner (1993) 仅覆盖多分类混杂变量，Dosemeci (1990) 仅覆盖多分类暴露变量，Wood-Doughty et al. (2018)/Lee & Wood-Doughty (2024) 仅处理二分类或单一拓扑。本文将 7 种 DAG 拓扑 × K≥3 类别统一分析，确实填补了文献空白。"first systematic analysis" 的声明在合理范围内（Section 1, page 2）。

**[S2] K≥3 符号反转结果是有意义的负面发现。** Proposition 1 (page 5) 和 Theorem 1 (page 6) 证明多分类情形下即使非差异性误分类也可以反转因果效应方向。Figure 2 (page 5) 直观展示了各拓扑的符号反转概率，IV 拓扑高达 52.6%，这对依赖 LLM 标注做因果推断的实践者有直接警示意义。

**[S3] ASV 框架提供可操作的诊断工具。** 三个互补度量（magnitude、significance、sign-flip）从不同维度刻画脆弱性，Figure 3 (page 7) 展示的拓扑排序（IV 最脆弱，M-bias 免疫）具有实际指导价值。ASV 与 E-values 的区分（Remark 1, page 6）在 topology dependence 和 sign-flip 维度上有说服力。

**[S4] 极其详尽的数值验证。** 34 页论文中 24 页为附录，包含完整证明、100,000 次 Dirichlet 抽样验证、545,945 条对抗性曲线搜索（Appendix A.11）、真实 LLM 混淆矩阵实证（HumAID K=10, CivilComments K=2）。Conjecture 1 的验证（ε_false < 0.017, Table 3）虽为猜想但数值证据充分。

**[S5] FWL 不变性结果对实践者有直接价值。** Table 6 (Appendix B.2) 证明矩阵校正在 confounding、mediation、collider、M-bias 四种拓扑下无效（RMSE 减少 0%），这一"负面结果"阻止了盲目应用校正方法造成的资源浪费。

**[S6] Related Work 覆盖全面。** 引用涵盖经典计量（Carroll et al., 2006; Buonaccorsi, 2010; Gustafson, 2004）、流行病学（Brenner, 1993; Dosemeci, 1990; Jurek et al., 2005）、NLP 因果（Feder et al., 2022; Wood-Doughty et al., 2018; Egami et al., 2024）、sensitivity analysis（VanderWeele & Ding, 2017; Cinelli & Hazlett, 2020）和最新 LLM 标注（Baumann et al., 2025; Messing, 2025; Kim et al., 2025）。经验证，关键引用（Brenner 1993, Dosemeci 1990, Angelopoulos et al. 2023, Lee & Wood-Doughty 2024, Baumann et al. 2025）均为真实文献。

## Weaknesses

**[W1] [should-fix] 核心实用结果停留在猜想（Conjecture），理论贡献的"已证"部分适用范围有限。**
- 具体位置：Theorem 1 (page 6), Theorem 2 (page 6), Conjecture 1 (page 6)
- 问题：已证明的结果中，Theorem 1（confounding 单调性）仅对 K=2 完全成立（"Not guaranteed for K≥3"，Table 2, page 21）；Theorem 2（K=3 对称单调性）要求对称混淆矩阵，而 Remark (page 21) 自承"empirical K=3 confusion matrices deviate substantially from symmetry (median d_rel=0.33)"。实践中最需要的一般性 K≥3 单调性结果（Conjecture 1）仅有数值支持，未获证明。Extended Conjecture (Appendix B.12) 同样未证。论文的核心理论贡献呈现"已证但不实用 vs 实用但未证"的尴尬局面。
- 建议：明确讨论从 Conjecture 到 Theorem 的证明障碍在哪里。如果是技术障碍而非根本障碍，应说明；如果确实无法证明，应在正文（而非仅在附录 Remark 中）更坦诚地讨论这一限制。

**[W2] [should-fix] 非差异性误分类假设对 LLM 标注场景可能过强，主文讨论不足。**
- 具体位置：Definition 1 (page 3), Limitations (page 8)
- 问题：非差异性假设要求 P(A*=j|A=k,Y,Z) = P(A*=j|A=k)，即误分类独立于结果和协变量。但 LLM 分类器的错误往往与文本特征（如长度、复杂度、领域）相关，而这些特征可能同时预测结果变量。例如情感分类器在不同主题上的表现差异可能与待估因果效应相关。虽然附录 B.5-B.6 通过 Y-分层检验和压力测试部分缓解了这一担忧（12/12 配置中 1/12 拒绝），但主文仅在 Limitations 中一句带过（"non-differential misclassification (Appendix B.6)"），没有讨论违反此假设时偏差表达式会如何变化。
- 建议：在 Section 3.1 或 Limitations 中增加 1-2 句讨论差异性误分类的后果，并引导读者到附录中的实证检验。

**[W3] [should-fix] 实证验证全部基于模拟数据+真实混淆矩阵，缺乏端到端真实因果分析。**
- 具体位置：Section 4 (pages 7-8), Appendix B.3 (page 24)
- 问题：Section 4.4 使用 HumAID 和 CivilComments 的真实 LLM 混淆矩阵，但下游因果分析仍在模拟数据上进行。Appendix B.3 的 ClinicalBERT 案例研究最接近端到端应用，但其"ground truth"来自已知医学研究而非 NLP 管道自身。论文未展示在真实观测数据集上（已知或可估ground truth 因果效应）完整运行该框架（标注→ASV 诊断→校正→因果估计）的案例。对于一篇面向 NLP 实践者的论文，这是一个显著缺口。
- 建议：增加一个端到端案例，使用现有 NLP 因果推断数据集（如 Egami et al. 2024 的政治广告数据，或 Keith et al. 2020 的 benchmark），完整展示框架从 LLM 标注到因果估计校正的全流程。

**[W4] [minor] 对 EMNLP 读者的可达性有待提升。**
- 具体位置：Section 3 (pages 3-6)
- 问题：plim（概率极限）在脚注 1 (page 4) 简要定义但后续频繁使用；FWL (Frisch-Waugh-Lovell) 定理虽在 Appendix A.1 证明但主文假设读者熟悉；column-stochastic 矩阵的概念未解释。这些计量经济学/统计学概念对典型 EMNLP 读者（偏机器学习/NLP 背景）可能不够直观。Section 3.2 的偏差推导（Equations 1-2）虽然正确但信息密度极高。
- 建议：在 Section 3.1 增加一个 "Reader's Guide" 段落（2-3 句），明确告知读者需要哪些背景知识以及哪些附录可补充。

**[W5] [minor] Correction routing（Algorithm 1）作为三大贡献之一，实质性偏弱。**
- 具体位置：Section 4.5 (page 8), Algorithm 1 (page 34), Introduction (page 2)
- 问题：Algorithm 1 本质上是一个基于已有校正方法（PPI++, DSL, MC-SIMEX, Naive/MLA）和本文拓扑分析结果的决策树。各校正方法本身均非本文贡献。虽然"哪种方法在哪种拓扑下有效"这一知识有价值（Table 5, page 23），但将此与 bias taxonomy 和 ASV 框架并列为三大贡献可能膨胀了贡献声明。
- 建议：在 Introduction 中降低 correction routing 的贡献权重，将其定位为"practical implication"而非"contribution"；或者强化 FWL 不变性结果作为核心贡献（这确实是新结果）。

**[W6] [minor] Venue 适配度处于边界。**
- 问题：本文的核心贡献在于统计/计量经济学层面的测量误差理论，NLP 的连接主要通过"LLM 产生误分类标签"这一应用背景。理论结果（偏差表达式、符号反转定理、ASV）对任何多分类误分类场景通用，不特定于 NLP。EMNLP 读者可能期望更多 NLP 方法创新（如改进 LLM 标注质量的新方法）而非纯测量理论。但本文确实解决了 NLP 社区当前面临的紧迫问题（LLM-as-annotator 的可靠性），且 NLP 因果推断是 EMNLP 的一个活跃子领域。
- 这不是一个需要修改的问题，而是一个需要 AC 做价值判断的定位问题。

## Questions

**[Q1]** Conjecture 1 的证明障碍具体是什么？是 K≥3 列随机矩阵的组合复杂性，还是特定拓扑（如 exposure）存在结构性困难？作者是否尝试过对特定拓扑子集或特定 C 矩阵结构（如 near-diagonal）证明该猜想？

**[Q2]** 在 DAG 拓扑不确定的情况下（这在实际 NLP 因果推断中很常见），实践者应如何使用本框架？是否应对所有 7 种拓扑计算 ASV 并取最坏情况？

**[Q3]** ASV 的 bootstrap CI（Section 3.3）需要参考混淆矩阵 C₀。gold-standard 标签样本量对 ASV 估计精度的影响如何？是否有最低样本量的经验规则？

**[Q4]** 附录 B.7 (page 25) 测试了逻辑回归下的鲁棒性。是否测试过其他非线性模型（如随机森林、神经网络）？线性 SEM 假设的实际边界在哪里？

## Missing References

未发现重大遗漏。以下为可选补充：
- Kuroki & Pearl (2014) "Measurement bias and effect restoration in causal inference" — 已引用（page 10）✓
- 近期 proximal causal inference with text data 文献（如 Mozer et al. 或 Tchetgen Tchetgen 系列）——与本文的 measurement error 视角互补，但不属于必须引用。

## Overall Assessment

**Overall**: 3.5 (Borderline Conference)
**Soundness**: 4/5
**Excitement**: 3/5
**Confidence**: 4/5（熟悉因果推断和测量误差文献，对 NLP 应用场景有一定了解）

**一句话总结**：这是一篇技术上严谨、问题定义清晰的测量误差理论论文，系统覆盖了多分类×多拓扑的真空地带（S1-S2），ASV 框架有诊断价值（S3），但核心实用结果停留在猜想而非定理（W1），且缺乏端到端真实数据验证（W3），NLP venue 适配度处于边界（W6）。

**接收理由**：填补 K≥3 × 多拓扑文献空白，符号反转结果对实践有警示价值，ASV 提供可操作诊断。
**犹豫理由**：已证定理的适用范围有限（K=2 或对称矩阵），Conjecture 1 未证，实证验证停留在模拟层面，NLP 方法贡献薄弱。

如能在 camera-ready 中（1）增加端到端案例，（2）更坦诚讨论 Conjecture 1 的证明前景，（3）强化非差异性假设的讨论，可提升至 4/5。

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

_source line 1744 · 2026-05-23T19:59:05.753339+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Strength 和 Weakness：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 的审稿意见\n\n### Summary\n本文研究 LLM 生成的多分类标注误差如何在不同因果 DAG 拓扑下传播到下游因果估计中。作者推导了 7 种典型 DAG 拓扑下 K 类非差异性误分类的偏差表达式，证明 K≥3 时存在二分类所不具有的符号反转可能性，并提出 Annotation Sensitivity Values (ASV) 作为脆弱性诊断工具。此外，作者基于 Frisch-Waugh-Lovell 不变性指出矩阵校正方法在四种拓扑下无效，并提供拓扑感知的校正路由指南。\n\n### Strengths\n\n**[S1] 系统性覆盖多拓扑 × 多分类的真空地带。** Brenner (1993) 仅覆盖多分类混杂变量，Dosemeci (1990) 仅覆盖多分类暴露变量，Wood-Doughty et al. (2018)/Lee & Wood-Doughty (2024) 仅处理二分类或单一拓扑。本文将 7 种 DAG 拓扑 × K≥3 类别统一分析，确实填补了文献空白。\"first systematic analysis\" 的声明在合理范围内（Section 1, page 2）。\n\n**[S2] K≥3 符号反转结果是有意义的负面发现。** Proposition 1 (page 5) 和 Theorem 1 (page 6) 证明多分类情形下即使非差异性误分类也可以反转因果效应方向。Figure 2 (page 5) 直观展示了各拓扑的符号反转概率，IV 拓扑高达 52.6%，这对依赖 LLM 标注做因果推断的实践者有直接警示意义。\n\n**[S3] ASV 框架提供可操作的诊断工具。** 三个互补度量（magnitude、significance、sign-flip）从不同维度刻画脆弱性，Figure 3 (page 7) 展示的拓扑排序（IV 最脆弱，M-bias 免疫）具有实际指导价值。ASV 与 E-values 的区分（Remark 1, page 6）在 topology dependence 和 sign-flip 维度上有说服力。\n\n**[S4] 极其详尽的数值验证。** 34 页论文中 24 页为附录，包含完整证明、100,000 次 Dirichlet 抽样验证、545,945 条对抗性曲线搜索（Appendix A.11）、真实 LLM 混淆矩阵实证（HumAID K=10, CivilComments K=2）。Conjecture 1 的验证（ε_false < 0.017, Table 3）虽为猜想但数值证据充分。\n\n**[S5] FWL 不变性结果对实践者有直接价值。** Table 6 (Appendix B.2) 证明矩阵校正在 confounding、mediation、collider、M-bias 四种拓扑下无效（RMSE 减少 0%），这一\"负面结果\"阻止了盲目应用校正方法造成的资源浪费。\n\n**[S6] Related Work 覆盖全面。** 引用涵盖经典计量（Carroll et al., 2006; Buonaccorsi, 2010; Gustafson, 2004）、流行病学（Brenner, 1993; Dosemeci, 1990; Jurek et al., 2005）、NLP 因果（Feder et al., 2022; Wood-Doughty et al., 2018; Egami et al., 2024）、sensitivity analysis（VanderWeele & Ding, 2017; Cinelli & Hazlett, 2020）和最新 LLM 标注（Baumann et al., 2025; Messing, 2025; Kim et al., 2025）。经验证，关键引用均为真实文献。\n\n### Weaknesses\n\n**[W1] [should-fix] 核心实用结果停留在猜想（Conjecture），理论贡献的\"已证\"部分适用范围有限。**\n- Theorem 1 仅对 K=2 完全成立；Theorem 2 要求对称混淆矩阵，而实际偏差约 33%。最需要的一般性 K≥3 单调性结果（Conjecture 1）仅有数值支持。论文呈现\"已证但不实用 vs 实用但未证\"的局面。\n- 建议：明确讨论从 Conjecture 到 Theorem 的证明障碍在哪里。\n\n**[W2] [should-fix] 非差异性误分类假设对 LLM 标注场景可能过强，主文讨论不足。**\n- LLM 分类器的错误往往与文本特征（如长度、复杂度、领域）相关，而这些特征可能同时预测结果变量。附录 B.5-B.6 通过 Y-分层检验部分缓解了担忧（12/12 中 1/12 拒绝），但主文仅在 Limitations 中一句带过。\n- 建议：在 Section 3.1 或 Limitations 中增加讨论。\n\n**[W3] [should-fix] 实证验证全部基于模拟数据+真实混淆矩阵，缺乏端到端真实因果分析。**\n- Section 4.4 使用 HumAID 和 CivilComments 的真实 LLM 混淆矩阵，但下游因果分析仍在模拟数据上进行。Appendix B.3 的 ClinicalBERT 最接近端到端但 ground truth 来自已知医学研究而非 NLP 管道。\n\n**[W4] [minor] 对 EMNLP 读者的可达性有待提升。**\n- plim、FWL、column-stochastic 等概念对 NLP 背景读者可能不够直观。建议增加 \"Reader's Guide\" 段落。\n\n**[W5] [minor] Correction routing（Algorithm 1）作为三大贡献之一，实质性偏弱。**\n- Algorithm 1 本质上是已有校正方法和本文拓扑分析的决策树。建议降低贡献权重或强化 FWL 不变性作为核心贡献。\n\n**[W6] [minor] Venue 适配度处于边界。**\n- 核心贡献在统计/计量层面，NLP 连接主要通过应用背景。不需修改，但需 AC 做价值判断。\n\n### Questions\n[Q1] Conjecture 1 的证明障碍具体是什么？\n[Q2] DAG 拓扑不确定时如何使用本框架？\n[Q3] ASV bootstrap CI 的 gold-standard 样本量要求？\n[Q4] 是否测试过其他非线性模型？\n\n---\n\n**请逐条回应以上所有 Strengths 和 Weaknesses。**"
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
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Strength 和 Weakness：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 的审稿意见\n\n### Summary\n本文研究 LLM 生成的多分类标注误差如何在不同因果 DAG 拓扑下传播到下游因果估计中。作者推导了 7 种典型 DAG 拓扑下 K 类非差异性误分类的偏差表达式，证明 K≥3 时存在二分类所不具有的符号反转可能性，并提出 Annotation Sensitivity Values (ASV) 作为脆弱性诊断工具。此外，作者基于 Frisch-Waugh-Lovell 不变性指出矩阵校正方法在四种拓扑下无效，并提供拓扑感知的校正路由指南。\n\n### Strengths\n\n**[S1] 系统性覆盖多拓扑 × 多分类的真空地带。** Brenner (1993) 仅覆盖多分类混杂变量，Dosemeci (1990) 仅覆盖多分类暴露变量，Wood-Doughty et al. (2018)/Lee & Wood-Doughty (2024) 仅处理二分类或单一拓扑。本文将 7 种 DAG 拓扑 × K≥3 类别统一分析，确实填补了文献空白。\"first systematic analysis\" 的声明在合理范围内（Section 1, page 2）。\n\n**[S2] K≥3 符号反转结果是有意义的负面发现。** Proposition 1 (page 5) 和 Theorem 1 (page 6) 证明多分类情形下即使非差异性误分类也可以反转因果效应方向。Figure 2 (page 5) 直观展示了各拓扑的符号反转概率，IV 拓扑高达 52.6%，这对依赖 LLM 标注做因果推断的实践者有直接警示意义。\n\n**[S3] ASV 框架提供可操作的诊断工具。** 三个互补度量（magnitude、significance、sign-flip）从不同维度刻画脆弱性，Figure 3 (page 7) 展示的拓扑排序（IV 最脆弱，M-bias 免疫）具有实际指导价值。ASV 与 E-values 的区分（Remark 1, page 6）在 topology dependence 和 sign-flip 维度上有说服力。\n\n**[S4] 极其详尽的数值验证。** 34 页论文中 24 页为附录，包含完整证明、100,000 次 Dirichlet 抽样验证、545,945 条对抗性曲线搜索（Appendix A.11）、真实 LLM 混淆矩阵实证（HumAID K=10, CivilComments K=2）。Conjecture 1 的验证（ε_false < 0.017, Table 3）虽为猜想但数值证据充分。\n\n**[S5] FWL 不变性结果对实践者有直接价值。** Table 6 (Appendix B.2) 证明矩阵校正在 confounding、mediation、collider、M-bias 四种拓扑下无效（RMSE 减少 0%），这一\"负面结果\"阻止了盲目应用校正方法造成的资源浪费。\n\n**[S6] Related Work 覆盖全面。** 引用涵盖经典计量（Carroll et al., 2006; Buonaccorsi, 2010; Gustafson, 2004）、流行病学（Brenner, 1993; Dosemeci, 1990; Jurek et al., 2005）、NLP 因果（Feder et al., 2022; Wood-Doughty et al., 2018; Egami et al., 2024）、sensitivity analysis（VanderWeele & Ding, 2017; Cinelli & Hazlett, 2020）和最新 LLM 标注（Baumann et al., 2025; Messing, 2025; Kim et al., 2025）。经验证，关键引用均为真实文献。\n\n### Weaknesses\n\n**[W1] [should-fix] 核心实用结果停留在猜想（Conjecture），理论贡献的\"已证\"部分适用范围有限。**\n- Theorem 1 仅对 K=2 完全成立；Theorem 2 要求对称混淆矩阵，而实际偏差约 33%。最需要的一般性 K≥3 单调性结果（Conjecture 1）仅有数值支持。论文呈现\"已证但不实用 vs 实用但未证\"的局面。\n- 建议：明确讨论从 Conjecture 到 Theorem 的证明障碍在哪里。\n\n**[W2] [should-fix] 非差异性误分类假设对 LLM 标注场景可能过强，主文讨论不足。**\n- LLM 分类器的错误往往与文本特征（如长度、复杂度、领域）相关，而这些特征可能同时预测结果变量。附录 B.5-B.6 通过 Y-分层检验部分缓解了担忧（12/12 中 1/12 拒绝），但主文仅在 Limitations 中一句带过。\n- 建议：在 Section 3.1 或 Limitations 中增加讨论。\n\n**[W3] [should-fix] 实证验证全部基于模拟数据+真实混淆矩阵，缺乏端到端真实因果分析。**\n- Section 4.4 使用 HumAID 和 CivilComments 的真实 LLM 混淆矩阵，但下游因果分析仍在模拟数据上进行。Appendix B.3 的 ClinicalBERT 最接近端到端但 ground truth 来自已知医学研究而非 NLP 管道。\n\n**[W4] [minor] 对 EMNLP 读者的可达性有待提升。**\n- plim、FWL、column-stochastic 等概念对 NLP 背景读者可能不够直观。建议增加 \"Reader's Guide\" 段落。\n\n**[W5] [minor] Correction routing（Algorithm 1）作为三大贡献之一，实质性偏弱。**\n- Algorithm 1 本质上是已有校正方法和本文拓扑分析的决策树。建议降低贡献权重或强化 FWL 不变性作为核心贡献。\n\n**[W6] [minor] Venue 适配度处于边界。**\n- 核心贡献在统计/计量层面，NLP 连接主要通过应用背景。不需修改，但需 AC 做价值判断。\n\n### Questions\n[Q1] Conjecture 1 的证明障碍具体是什么？\n[Q2] DAG 拓扑不确定时如何使用本框架？\n[Q3] ASV bootstrap CI 的 gold-standard 样本量要求？\n[Q4] 是否测试过其他非线性模型？\n\n---\n\n**请逐条回应以上所有 Strengths 和 Weaknesses。**"
  }
}
```

</details>

---


### Tool result

_source line 1745 · 2026-05-23T19:59:45.602897+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 39849
}
```

</details>

---


### Tool call

_source line 1746 · 2026-05-23T19:59:45.754364+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Strength 和 Weakness：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 的审稿意见\n\n### Summary\n本文研究多类别（K≥3）LLM 标注误差如何在因果推断中传播，覆盖 7 种典型 DAG 拓扑。作者推导了每种拓扑下的 bias 表达式，证明了 K=2（Theorem 1）和 K=3 对称混淆矩阵（Theorem 2）下的 envelope monotonicity，定义了 ASV 作为诊断工具，并提出了 topology-aware 校正路由算法。\n\n### Strengths\n\n**[S1] 系统性的拓扑分类学：** 对 7 种 DAG 拓扑逐一推导 bias 表达式（Section 3.2, Appendix A.3-A.9），揭示了拓扑结构决定 bias 方向和幅度的核心洞见。特别是 sign reversal 只在 exposure (IV) 拓扑下发生的发现（Table 1, Appendix A.9），对实践者有直接指导意义。\n\n**[S2] 证明的严谨性：** Theorem 1 通过 perspective function 的凸性论证 B(C(δ)) 的单调性，推导链条完整。Theorem 2 将问题归约为 V_b(x) 在 [0,1] 上严格递减，利用对称分解得到干净的因式分解形式（公式 23），sign analysis 正确。Proposition 1-3 的 Cauchy-Schwarz 论证标准且正确。\n\n**[S3] 诚实的理论边界声明：** Theorem 2 的局限在 Remark 4 中被坦诚讨论；Conjecture 1 被正确标注；proportional effects 违反率（Table 14, ~23%）被量化报告。\n\n**[S4] 充分的数值验证体系：** 100,000 Dirichlet 矩阵 + 545,945 adversarial 曲线 + 23 真实 LLM 配置 + Monte Carlo 验证（MAPE 1.6%）。\n\n**[S5] 实用的诊断框架：** ASV 三维度设计和 Algorithm 1 校正路由。\n\n### Weaknesses\n\n**[W1] [must-fix] Theorem 2 的对称 C₀ 假设与实际 LLM 混淆矩阵严重脱节**\n- Theorem 2 要求 K=3 混淆矩阵 C₀ 完全对称（所有 off-diagonal 元素相等）。但 Remark 4 自己报告，10 个 VAST 配置的真实 LLM 混淆矩阵中位相对 Frobenius 距离 d_rel = 0.33（范围 0.29-0.38），即实际矩阵与对称矩阵偏差约 33%。\n- 论文的核心 claim 之一是提供\"closed-form\"和\"provable\"的 monotonicity 结果。如果主要适用场景只能依赖 conjecture，理论贡献强度显著削弱。\n- 建议：(a) 尝试证明 \"near-symmetric\" 矩阵下的近似单调性；(b) 或在正文中更明确重新定位 Theorem 2 为 \"theoretical anchor\"。\n\n**[W2] [must-fix] 缺少端到端的真实 NLP 因果推断应用**\n- 对于 EMNLP 应用导向 venue，实验验证主要是\"验证理论正确性\"和\"验证假设成立\"，缺少完整场景：在真实 NLP 任务中使用 LLM 标注数据进行因果推断，展示框架如何改变实质性结论。\n- 建议：增加真实 NLP 因果推断案例（如政治立场检测、灾害推文分析）。\n\n**[W3] [should-fix] Proportional effects 假设的违反后果讨论不充分**\n- Table 14 显示独立 f,g 下 out-of-bounds 率达 23%。论文缺少对 NLP 因果场景中 proportional effects 合理性的实质论证。\n- 建议：增加 1-2 句讨论 NLP 场景中的合理性。\n\n**[W4] [should-fix] Linear SEM 假设的适用范围在正文中讨论不足**\n- Table 6 的 logistic regression 测试显示，exposure 拓扑下校正实际恶化了 bias（-78%）。Limitations 过于简略。\n- 建议：更突出讨论哪些拓扑在非线性下仍成立、哪些不成立。\n\n**[W5] [should-fix] Conjecture 1 的验证覆盖范围可能不足**\n- 4 种 adversarial 结构族的选择基于直觉而非系统性参数空间覆盖。未解释为什么不存在更病态的结构。\n- 建议：解释为何这 4 种族足以覆盖？是否尝试过基于梯度的 adversarial optimization？\n\n**[W6] [minor] 符号负担较重，对 EMNLP 读者不够友好**\n- 大量计量经济学符号对 NLP/ML 背景读者较难跟随。建议增加 intuition 段落。\n\n### Questions\n[Q1] Theorem 1 非比例效应下的 monotonicity violation 范围？\n[Q2] 实际 LLM 混淆矩阵中某些 off-diagonal 为 0 时 sign preservation 是否仍成立？\n[Q3] Algorithm 1 阈值如何确定？是否应依赖 sample size？\n[Q4] content-dependent proxy 导致 Y-stratification 显著时，如何使用本框架？\n\n### Overall Assessment\n**Overall**: 3.5 (Borderline Conference), **Soundness**: 3.5/5, **Excitement**: 3/5, **Confidence**: 4/5\n\n---\n\n**请逐条回应以上所有 Strengths 和 Weaknesses。**"
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
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Strength 和 Weakness：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 的审稿意见\n\n### Summary\n本文研究多类别（K≥3）LLM 标注误差如何在因果推断中传播，覆盖 7 种典型 DAG 拓扑。作者推导了每种拓扑下的 bias 表达式，证明了 K=2（Theorem 1）和 K=3 对称混淆矩阵（Theorem 2）下的 envelope monotonicity，定义了 ASV 作为诊断工具，并提出了 topology-aware 校正路由算法。\n\n### Strengths\n\n**[S1] 系统性的拓扑分类学：** 对 7 种 DAG 拓扑逐一推导 bias 表达式（Section 3.2, Appendix A.3-A.9），揭示了拓扑结构决定 bias 方向和幅度的核心洞见。特别是 sign reversal 只在 exposure (IV) 拓扑下发生的发现（Table 1, Appendix A.9），对实践者有直接指导意义。\n\n**[S2] 证明的严谨性：** Theorem 1 通过 perspective function 的凸性论证 B(C(δ)) 的单调性，推导链条完整。Theorem 2 将问题归约为 V_b(x) 在 [0,1] 上严格递减，利用对称分解得到干净的因式分解形式（公式 23），sign analysis 正确。Proposition 1-3 的 Cauchy-Schwarz 论证标准且正确。\n\n**[S3] 诚实的理论边界声明：** Theorem 2 的局限在 Remark 4 中被坦诚讨论；Conjecture 1 被正确标注；proportional effects 违反率（Table 14, ~23%）被量化报告。\n\n**[S4] 充分的数值验证体系：** 100,000 Dirichlet 矩阵 + 545,945 adversarial 曲线 + 23 真实 LLM 配置 + Monte Carlo 验证（MAPE 1.6%）。\n\n**[S5] 实用的诊断框架：** ASV 三维度设计和 Algorithm 1 校正路由。\n\n### Weaknesses\n\n**[W1] [must-fix] Theorem 2 的对称 C₀ 假设与实际 LLM 混淆矩阵严重脱节**\n- Theorem 2 要求 K=3 混淆矩阵 C₀ 完全对称（所有 off-diagonal 元素相等）。但 Remark 4 自己报告，10 个 VAST 配置的真实 LLM 混淆矩阵中位相对 Frobenius 距离 d_rel = 0.33（范围 0.29-0.38），即实际矩阵与对称矩阵偏差约 33%。\n- 论文的核心 claim 之一是提供\"closed-form\"和\"provable\"的 monotonicity 结果。如果主要适用场景只能依赖 conjecture，理论贡献强度显著削弱。\n- 建议：(a) 尝试证明 \"near-symmetric\" 矩阵下的近似单调性；(b) 或在正文中更明确重新定位 Theorem 2 为 \"theoretical anchor\"。\n\n**[W2] [must-fix] 缺少端到端的真实 NLP 因果推断应用**\n- 对于 EMNLP 应用导向 venue，实验验证主要是\"验证理论正确性\"和\"验证假设成立\"，缺少完整场景：在真实 NLP 任务中使用 LLM 标注数据进行因果推断，展示框架如何改变实质性结论。\n- 建议：增加真实 NLP 因果推断案例（如政治立场检测、灾害推文分析）。\n\n**[W3] [should-fix] Proportional effects 假设的违反后果讨论不充分**\n- Table 14 显示独立 f,g 下 out-of-bounds 率达 23%。论文缺少对 NLP 因果场景中 proportional effects 合理性的实质论证。\n- 建议：增加 1-2 句讨论 NLP 场景中的合理性。\n\n**[W4] [should-fix] Linear SEM 假设的适用范围在正文中讨论不足**\n- Table 6 的 logistic regression 测试显示，exposure 拓扑下校正实际恶化了 bias（-78%）。Limitations 过于简略。\n- 建议：更突出讨论哪些拓扑在非线性下仍成立、哪些不成立。\n\n**[W5] [should-fix] Conjecture 1 的验证覆盖范围可能不足**\n- 4 种 adversarial 结构族的选择基于直觉而非系统性参数空间覆盖。未解释为什么不存在更病态的结构。\n- 建议：解释为何这 4 种族足以覆盖？是否尝试过基于梯度的 adversarial optimization？\n\n**[W6] [minor] 符号负担较重，对 EMNLP 读者不够友好**\n- 大量计量经济学符号对 NLP/ML 背景读者较难跟随。建议增加 intuition 段落。\n\n### Questions\n[Q1] Theorem 1 非比例效应下的 monotonicity violation 范围？\n[Q2] 实际 LLM 混淆矩阵中某些 off-diagonal 为 0 时 sign preservation 是否仍成立？\n[Q3] Algorithm 1 阈值如何确定？是否应依赖 sample size？\n[Q4] content-dependent proxy 导致 Y-stratification 显著时，如何使用本框架？\n\n### Overall Assessment\n**Overall**: 3.5 (Borderline Conference), **Soundness**: 3.5/5, **Excitement**: 3/5, **Confidence**: 4/5\n\n---\n\n**请逐条回应以上所有 Strengths 和 Weaknesses。**"
  }
}
```

</details>

---


### Tool result

_source line 1747 · 2026-05-23T19:59:47.163852+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 1748 · 2026-05-23T19:59:49.564212+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 172

## Round 172

2 recorded events


### User

_source line 1749 · 2026-05-23T19:59:52.221607+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论：Overall 3.5 (Borderline Conference)**

核心判断：
- **技术严谨**，系统覆盖 7 种 DAG 拓扑 × K≥3 多分类误分类的偏差分析，填补文献空白
- **ASV 框架**有诊断价值，符号反转结果（K≥3 特有）对实践者有警示意义
- **主要顾虑**：已证定理适用范围有限（Theorem 1 仅 K=2 完整，Theorem 2 要求对称矩阵），核心实用结果 Conjecture 1 未获证明；实证验证全部基于模拟而非端到端真实因果分析；NLP venue 适配度处于边界

提出 3 个 should-fix（Conjecture 讨论不足、非差异性假设主文讨论不足、缺端到端案例）和 3 个 minor 问题。引用验证通过，未发现虚构引用。格式合规（8 页正文、Limitations 在正文内、abstract ≈185 words、双盲匿名）。

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

_source line 1750 · 2026-05-23T19:59:55.900449+00:00_

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


## Round 173

## Round 173

2 recorded events


### User

_source line 1751 · 2026-05-23T20:00:34.716700+00:00_

[Reviewer 1 审稿意见]:

## 交叉回应：Reviewer 2 审稿意见

---

### Strengths 回应

**[AGREE] R2-S1: 系统性覆盖多拓扑 × 多分类的真空地带。**
完全同意。我在 R1-S1 中也独立指出了这一点。7 种拓扑的 bias 分类学确实是此前文献中缺失的贡献，"first systematic analysis" 的声明有据可查。

**[AGREE] R2-S2: K≥3 符号反转结果是有意义的负面发现。**
同意。Figure 2 (p.5) 的 IV 拓扑 52.6% sign reversal 率是一个重要的实践警示。我补充一点：Table 1 (p.7) 中 sign-flip guarantee 的拓扑分化（5 种拓扑 zero sign-flip vs. IV 52.6%）进一步强化了这个发现的价值——实践者可以通过识别拓扑来判断是否需要担心符号反转。

**[AGREE] R2-S3: ASV 框架提供可操作的诊断工具。**
同意。我在 R1-S5 中也肯定了 ASV 的实用价值。Remark 1 (p.6) 区分 ASV 与 E-values 的论证（topology dependence + sign-flip 维度）是有说服力的。

**[AGREE] R2-S4: 极其详尽的数值验证。**
同意。多层验证体系（Dirichlet 采样 + adversarial search + 真实 LLM 矩阵 + Monte Carlo）是本文的显著优势。我在 R1-S4 中也独立肯定了这一点。

**[AGREE] R2-S5: FWL 不变性结果对实践者有直接价值。**
同意。Table 6 (Appendix B.2) 的"负面结果"（4 种拓扑下矩阵校正无效）确实有实践指导意义。我补充：这个结果的价值在于它与 Table 5 (p.8) 的校正路由建议形成了完整的决策框架——不仅告诉实践者"该用什么"，也告诉他们"什么不用做"。

**[AGREE] R2-S6: Related Work 覆盖全面。**
同意。我在审稿中未发现明显的引用遗漏。

---

### Weaknesses 回应

**[AGREE] R2-W1: 核心实用结果停留在猜想，"已证但不实用 vs 实用但未证"的局面。**
强烈同意，这与我的 R1-W1 高度一致。R2 的概括更精炼——"已证但不实用 vs 实用但未证"准确捕捉了核心矛盾。

我补充两点证据：
1. Remark 4 (p.18) 报告的 d_rel = 0.33 意味着 Theorem 2 的对称假设在实践中偏差约三分之一，这不是"近似成立"而是"显著偏离"。
2. R2 建议"明确讨论从 Conjecture 到 Theorem 的证明障碍"——我同意这比我提的"尝试证明 near-symmetric 结果"更务实。论文应至少解释：是技术上缺少关键引理，还是存在已知的反例结构阻止一般性证明？Appendix A.4 Step 4 提到 general case 的严格单调性 "remains open"，但没有说明为什么 open。

**[AGREE] R2-W2: 非差异性误分类假设对 LLM 标注场景可能过强。**
同意，这与我的 R1-Q4 一致。我在 Q4 中特别追问了"content-dependent proxy variables 产生显著 Y-stratification"（Appendix B.25）的含义——当标注变量与文本内容高度耦合（如 stance detection），non-differential 假设可能系统性地不成立。

不过我对 R2 的措辞有一个细微补充：R2 说"LLM 分类器的错误往往与文本特征相关"——这是对的，但 non-differential 要求的是 P(A*|A,Y,Z) = P(A*|A)，即误分类不依赖于 Y *在给定 A 的条件下*。如果文本特征通过 A 完全中介了对 Y 的影响（即 A 是 text features 和 Y 之间的中介变量），那么 non-differential 仍然可以成立。论文的 architectural invariant 论证（LLM 只看 text，不看 Y）在 Y 不直接影响 text 的场景下是成立的。关键问题是：在 NLP 中，Y 和 text 的关系通常更复杂（Y 可能是 text 的结果，也可能是 text 的原因），论文应该更明确地讨论哪些 NLP 任务满足这个条件。

**[AGREE] R2-W3: 缺乏端到端真实因果分析。**
强烈同意，这与我的 R1-W2 完全一致。两位 reviewer 独立指出同一问题，加强了其严重性。R2 的观察"ground truth 来自已知医学研究而非 NLP 管道"精确地指出了 ClinicalBERT 案例的局限。

**[AGREE] R2-W4: 对 EMNLP 读者的可达性有待提升。**
同意，与我的 R1-W6 一致。R2 建议的 "Reader's Guide" 段落比我建议的 "intuition 段落" 更具体、更可操作。

**[REBUT] R2-W5: Correction routing（Algorithm 1）作为三大贡献之一，实质性偏弱。**
部分不同意。R2 认为 Algorithm 1 "本质上是已有校正方法和本文拓扑分析的决策树"——这在形式上是对的，但忽略了其实质贡献：

1. **FWL 不变性的发现本身就是 Algorithm 1 的核心理论基础**。在此之前，实践者没有理由知道 PPI++/DSL/MC-SIMEX 在 confounding/mediation/collider/M-bias 四种拓扑下是无效的（Table 5, p.8；Table 6, Appendix B.2）。这不是"已知方法的简单组合"，而是基于本文新发现（FWL 不变性 → 矩阵校正无效）的决策逻辑。

2. **决策树的价值在于 topology-dependent routing 这个概念本身**。现有校正文献（Angelopoulos et al., 2023; Egami et al., 2024）都是 topology-agnostic 的——它们假设校正方法普适。Algorithm 1 首次将"先识别拓扑，再选校正方法"系统化。

3. 不过，我同意 R2 说 Algorithm 1 的阈值设定（risk level 分类等）偏启发式（我在 R1-Q3 中也追问了这一点）。如果作者能提供阈值的理论或数据驱动依据，Algorithm 1 的贡献会更扎实。

综上，我认为 Algorithm 1 的贡献不应被降低，但其呈现方式可以改进——强调 FWL 不变性发现作为独立贡献，将 Algorithm 1 定位为该发现的实践推论。

**[AGREE] R2-W6: Venue 适配度处于边界。**
部分同意。论文的核心贡献确实在统计/计量层面，NLP 连接主要通过应用背景建立。但我认为这不构成拒稿理由——ARR reviewer guidelines 明确指出 "NLP is an interdisciplinary field" 且不应因方法类型歧视论文。问题不在于方法是统计性的，而在于论文没有充分展示这些统计结果对 NLP 实践者的具体影响（回到 W3/R1-W2 的端到端应用缺失）。如果补充了真实 NLP 因果应用案例，venue 适配度问题会自然解决。

---

### 总结：两位 Reviewer 的共识与分歧

**高度共识（3 个核心问题）：**
1. K≥3 理论贡献依赖 conjecture，已证结果适用范围窄（R1-W1 ≈ R2-W1）
2. 缺少端到端真实 NLP 因果应用（R1-W2 ≈ R2-W3）
3. Non-differential 假设在 NLP 中可能过强，讨论不足（R1-Q4 ≈ R2-W2）

**分歧：**
- Algorithm 1 的贡献权重（R2-W5 认为偏弱，R1 认为有实质价值但阈值需要论证）
- 严重性分级：R2 将大多数问题标为 should-fix/minor，R1 将 W1（Theorem 2 脱节）和 W2（缺少应用）标为 must-fix

**我的最终判断：**
维持 Overall 3.5 (Borderline Conference)。两位 reviewer 的共识问题（conjecture gap + 缺少应用）是阻碍评分达到 4.0 的主要原因。如果作者在 revision 中能补充一个真实 NLP 因果案例并更好地定位 Theorem 2 的角色，评分可上调至 4.0。


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

_source line 1752 · 2026-05-23T20:00:38.401485+00:00_

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


## Round 174

## Round 174

2 recorded events


### User

_source line 1753 · 2026-05-23T20:00:42.112314+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心结论：

- **与 R2 高度一致的 3 个问题**：Conjecture gap、缺少真实 NLP 因果应用、non-differential 假设讨论不足
- **唯一分歧**：Algorithm 1 的贡献权重——我认为 FWL 不变性发现赋予了它实质性内容，不应简单降级为"决策树"
- **维持 3.5 评分**，两位 reviewer 的共识强化了 borderline conference 的判断

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

_source line 1754 · 2026-05-23T20:00:47.552350+00:00_

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


## Round 175

## Round 175

10 recorded events


### User

_source line 1755 · 2026-05-23T20:02:05.015829+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Strengths 回应

**[AGREE] R1-S1: 系统性的拓扑分类学。** 同意这是本文最核心的贡献。补充一点精确化：sign reversal 发生在 Exposure 和 IV 两个独立拓扑（Table 1, page 7; Figure 2, page 5），R1 表述为"exposure (IV)"可能给人二者为同一拓扑的印象——实际上 Exposure 的 sign reversal 率为 83.4%，IV 为 52.6%，机制也不同（Exposure 通过 off-diagonal dominance，IV 通过 first-stage coefficient 归零）。

**[AGREE] R1-S2: 证明的严谨性。** 同意。Theorem 1 的 perspective function 论证和 Theorem 2 的对称分解（Equation 23, Appendix A.6）在我的独立审查中也验证为正确。Proposition 1-3 的 Cauchy-Schwarz 应用标准且无误。

**[AGREE] R1-S3: 诚实的理论边界声明。** 同意，且认为这是本文值得肯定的学术态度。Remark (page 21) 中关于 Theorem 2 对称假设的局限讨论、Conjecture 1 的显式标注，以及 Table 14 (Appendix B.13) 中 proportional effects 违反率的量化报告，均体现了负责任的学术写作。

**[AGREE] R1-S4: 充分的数值验证体系。** 同意。我在自己的审稿中也将此列为 S4。100,000 Dirichlet 抽样 + adversarial 搜索 + 23 真实 LLM 配置的三层验证体系超出了同类工作的常见标准。Monte Carlo 与解析结果的 MAPE 1.6%（Section 4.2）进一步增强了可信度。

**[AGREE] R1-S5: 实用的诊断框架。** 部分同意。ASV 三维度设计（magnitude, significance, sign-flip）确实有诊断价值（Figure 3, page 7）。但我在自己的 W5 中指出 Algorithm 1 作为三大贡献之一的权重可能过高——它本质上是对已有方法（PPI++, DSL, MC-SIMEX）的拓扑适配，而非方法创新。R1 将其列为 Strength 无异议，但作为"contribution"的定位值得商榷。

---

### Weaknesses 回应

**[AGREE] R1-W1: Theorem 2 对称假设与实际 LLM 矩阵脱节。**
同意这是一个显著局限，我在自己的 W1 中也提出了本质相同的批评。d_rel=0.33（Remark, page 21）意味着 Theorem 2 在实际中几乎不直接适用。我的补充观察：这个问题与 Conjecture 1 的未证状态叠加后更加严重——论文的理论体系呈现出一个尴尬的结构：

- Theorem 1（K=2 完全成立）→ 对 NLP 场景最不相关（多数 NLP 分类任务 K≥3）
- Theorem 2（K=3 对称矩阵）→ 实际 LLM 矩阵不满足
- Conjecture 1（一般 K≥3）→ 未证明

同意 R1 的建议 (b)：在正文中将 Theorem 2 更明确地定位为"theoretical anchor"比尝试证明 near-symmetric 情况更务实。

**[AGREE] R1-W2: 缺少端到端真实 NLP 因果推断应用。**
强烈同意，这与我的 W3 完全一致。Appendix B.3 的 ClinicalBERT 案例是论文中最接近端到端应用的部分，但其因果效应 ground truth 来自文献中已知的医学发现，而非通过 NLP pipeline 独立验证。对 EMNLP venue 而言，展示框架在真实 NLP 因果推断场景中如何改变实质性结论（而非仅验证理论预测的正确性）是关键缺口。

补充：R1 建议"政治立场检测、灾害推文分析"作为案例来源。我认为论文已经使用了 HumAID（灾害推文，K=10）的混淆矩阵，增加对应的端到端因果分析（如：灾害推文情感→公众行为的因果效应估计）不需要大量额外工作，可行性较高。

**[AGREE] R1-W3: Proportional effects 假设讨论不充分。**
同意。Table 14（Appendix B.13）中独立 f,g 下 ~23% out-of-bounds 率是一个不可忽视的数字。论文在 Appendix B.17 对真实 LLM 混淆矩阵验证了 proportional effects 的近似成立（sign preservation 97.3%），但主文对这一关键假设几乎未讨论。

补充：从 NLP 视角看，proportional effects 要求混杂/处理效应与误分类"比例传递"，即 f(A) = λg(A)。在 NLP 因果场景中（如：主题分类器错误→情感估计偏差），不同类别的效应方向和幅度可能差异很大，proportional effects 的合理性需要 domain-specific 论证。R1 的建议（增加 1-2 句 NLP 场景论证）合理且易行。

**[REBUT] R1-W4: Linear SEM 假设的适用范围讨论不足。**
部分反驳。R1 指出 Table 6 中 exposure 拓扑下 logistic regression 校正恶化 bias（-78%），但这需要更完整的语境：

1. Appendix B.7（page 25, Table 9）实际上测试了两种非线性模型：logistic regression 和 nonlinear DGP。对于 logistic regression，五种 covariate 拓扑（confounding, mediation, collider, M-bias, front-door）的 sign-flip 率均为 0%，FWL invariance 在这些拓扑下保持。Exposure 的 -78% 恶化是因为 FWL-covariate 拓扑本身就不应做矩阵校正（Table 5, page 23 已明确标注 "no correction (FWL)"），而非 linear SEM 假设失败。

2. Appendix B.14 (Table 15) 进一步测试了 FWL invariance under nonlinear models（logistic 和 linear），在 N={1000, 5000, 10000, 50000} 和三种 error level 下均确认 covariate 拓扑的 mean logistic bias reduction ≤5%。

3. 我同意 Limitations 段落过于简略（仅"assume linear SEMs"一句），但论文在附录中已提供了比 R1 评估更充分的非线性鲁棒性证据。建议将附录的关键结论（如"FWL invariance holds under logistic regression for all covariate topologies"）在 Limitations 中明确引用。

**[AGREE] R1-W5: Conjecture 1 的 adversarial 验证覆盖范围。**
同意这是一个合理的担忧。4 种 adversarial 结构族（near-permutation, block-diagonal, sparse, near-uniform; Appendix A.11）的选择确实基于直觉而非系统性覆盖。

但我想提供一个平衡视角：
- 545,945 条 adversarial 曲线的最大单步 monotonicity 违反为 ε_false < 0.017（Table 3, page 22），这是一个极小的数字
- Conjecture 1 的声明本身已经留有 ε < 0.02 的余地
- 从实践角度看，即使存在未覆盖的 adversarial 结构，只要违反幅度保持在 ε < 0.02 的量级，对 ASV ranking 的实际影响可忽略

R1 建议的"基于梯度的 adversarial optimization"是一个很好的方向。如果 C(δ) 是连续参数化的，可以对 |d|B(C(δ))|/dδ| 做梯度上升来寻找最大违反。这比随机采样更有效但计算量更大。

**[AGREE] R1-W6: 符号负担较重。**
同意，这与我的 W4 一致。plim、FWL、column-stochastic 等概念对 EMNLP 读者确实不够友好。R1 建议增加 intuition 段落，我在自己的审稿中建议增加 "Reader's Guide" 段落，本质相同。

---

### 对 R1 Questions 的补充

**R1-Q1（non-proportional monotonicity violation 范围）**: 这是一个好问题。Appendix B.13 Table 14 报告了 OOB 率，但未报告 violation 的 magnitude。如果 violation 幅度很小（如 ε < 0.01），则 proportional effects 假设的实际影响有限。

**R1-Q2（off-diagonal 为 0 时的 sign preservation）**: 从理论上看，off-diagonal 元素为 0 意味着某些类别间无混淆，C 矩阵退化为 block-diagonal 形式。Proposition 1 的 Cauchy-Schwarz 论证应仍然成立（分子变小但不改变符号），但值得作者确认。

**R1-Q3（Algorithm 1 阈值确定）**: 同意这是一个实践上重要的问题。Algorithm 1 (page 34) 中 ASV > 0.05 等阈值看起来是基于经验（Table 4, page 22 的数值分布），但缺少 sensitivity analysis 说明阈值选择如何影响路由决策。

**R1-Q4（content-dependent proxy 的 Y-stratification）**: 论文在 Appendix B.25/B.5 中报告 content-dependent proxy 变量（topic, sentiment）显示显著 Y-stratification，这表明对这类变量非差异性假设可能不成立。这与我的 W2 直接相关——论文需要更充分讨论此假设违反时的后果。

---

### 综合评估比较

R1 给出 Overall 3.5, Soundness 3.5, Excitement 3.0。
我给出 Overall 3.5, Soundness 4.0, Excitement 3.0。

主要分歧在 Soundness：我认为 R1 的 3.5 稍偏低。虽然 Theorem 2 的对称假设和 Conjecture 1 的未证状态是真实局限（我也标注了），但论文在其理论框架内的推导是严格的，且数值验证极其充分。Soundness 评估的是"论文的 claims 是否被充分支撑"，而非"是否证明了最强结果"。Conjecture 1 作为猜想被正确标注，且有充分数值证据——这本身就是 sound 的做法。

两位 reviewer 的核心共识：
1. 缺少端到端真实 NLP 因果推断案例（R1-W2, R2-W3）
2. Theorem 2 实用性有限 / Conjecture 1 未证（R1-W1, R2-W1）
3. 对 EMNLP 读者可达性不足（R1-W6, R2-W4）
4. Venue 适配度处于边界（R2-W6, R1 未显式提出但 Excitement 3.0 反映了类似判断）

这些共识点应作为作者修改的优先方向。

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

_source line 1756 · 2026-05-23T20:02:35.317315+00:00_

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

_source line 1757 · 2026-05-23T20:02:35.368079+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T19:49:45.272610+00:00\", \"completed_at\": \"2026-05-23T19:53:32.683609+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前两页为连续纯文本（Title/Abstract/Introduction/Related Work），无任何 display item。第一个视觉锚点（Figure 1 DAG拓扑图）直到第3页才出现。审稿人在前2分钟内看到的全是文字，缺少视觉锚定。建议考虑将 Figure 1 提前至第2页（如通过压缩 Introduction 或将 Related Work 后移）\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Author/Abstract 排版整洁，符合 ACL 双栏模板规范。Abstract 长度适中\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（七种 DAG 拓扑）清晰可读，caption 自包含，DAG 节点标注明确。作为首个 display item 能有效传达核心框架，但位置偏后\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2（bias distribution 直方图）4 个子图布局合理，红色区域标注 sign reversal 直观。但子图内轴标签和图例文字偏小（估计 ~7pt），接近可读性下限\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Figure 2 的 \\\"Red = sign reversal\\\" 图例文字非常小，灰度打印时红色填充区域与背景的对比度可能不足\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"整页为定理/命题/Remark 密集数学内容，无 display item。对理论部分可接受，但与 page 1-2 的纯文本形成连续 3+ 页视觉单调段（pages 1-2 纯文本 → page 3 Figure 1 → pages 4 有公式 → page 5 有 Figure 2 → page 6 纯定理）——整体节奏尚可\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 + Figure 3 同页出现，display item 密度高，视觉节奏好。Table 1 使用 booktabs 风格，最优结果加粗标注，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（ASV vulnerability ranking）三种 ASV 类型用不同颜色区分，bar chart 清晰。颜色区分度良好\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4 + Conclusion + Limitations + References 起始，页面内容充实（≥95% 填充），空间利用率高\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 段落简洁（约 3 个点），符合 EMNLP 规范\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"References 页排版正常，格式统一（author 缩写、venue、年份一致），未发现 [?] 未解析引用\"}, {\"severity\": \"info\", \"dimension
…[truncated 1543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1758 · 2026-05-23T20:02:35.368507+00:00_

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

_source line 1759 · 2026-05-23T20:02:35.519574+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1760 · 2026-05-23T20:06:03.217668+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 21\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix（低优先级）。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 再提 Dirichlet 采样代表性。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Limitations 已覆盖。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。Limitations 已覆盖。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续三轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 21\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出，R18 修复充分。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 两位 Reviewer 再次提出。要求在主文增加讨论。共识 should-fix。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位 Reviewer 再次提出（R1-Q4, R2-W2）。主文仅在 Limitations 一句带过，Section 3.1 的 architectural invariant 论证不充分——content-dependent proxy（topic, sentiment）的 Y-stratification 显著（B.25），但未在主文讨论违反时后果。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 19\n    resolution: \"R18 压缩后编译验证 main text ≤8 pages。R19 PDF 确认合规。连续两轮无复发。\"\n    resolution_round: 19\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: minor\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1 联合。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提。共识 minor。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续两轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: must-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据——缺少端到端因果应用验证\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 升级为 critical。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位 Reviewer 再次独立提出（R1-W2 must-fix, R2-W3 should-fix）。共识：对 EMNLP 应用导向 venue，缺少在真实 NLP 任务中走完 annotate→estimate→correct 全流程的案例是显著缺口。ClinicalBERT (B.3) 和 End-to-End Demo (B.19) 均使用合成 ground truth。建议使用已有 HumAID 混淆矩阵增加端到端因果分析。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: Remark 1 重写为 complementary tools。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提。共识 should-fix。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W5 再提。共识 should-fix。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出为 weakness。R2-S3 反而肯定了 ASV 与 E-values 的区分（Remark 1 的 topology dependence + sign-flip 维度'有说服力'）。可能已修复至可接受水平。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: must-fix\n    summary: \"Proportional effects 假设在 NLP 中是强限制，且 Limitations 中完全缺失\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 增加 stance detection/sentiment analysis 场景讨论 + 97.3% empirical compliance。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位再提。共识 should-fix（高优先级）。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 升级为 critical。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 R1-W3 (should-fix) 再提：Table 14 显示独立 f,g 下 OOB 率 23%，主文缺少对 NLP 场景中 proportional effects 合理性的实质论证。R2 在交叉回应中 AGREE。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem/Conjecture 边界在主文中模糊\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 must-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 2 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位再次列为 critical。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 再次提出。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位独立再提（R1-W1 must-fix, R2-W1 should-fix）。核心矛盾不变：Theorem 1 仅 K=2，Theorem 2 要求对称 C₀（实际偏差 d_rel=0.33），Conjecture 1 未证。R2 精炼总结为'已证但不实用 vs 实用但未证'。R1 在交叉回应中强烈 AGREE。共识：需更明确定位 Theorem 2 为 theoretical anchor，并讨论 Conjecture→Theorem 的证明障碍。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"与 R6-M3 合并。\"\n      - round: 21\n        reviewers: [R1]\n        note: \"与 R6-M3 合并。R21 R1-W3。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 21\n        reviewers: []\n        note: \"与 R4-W6 合并。R21 未单独提出，R2-S3 反而肯定 ASV 区分度。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 19\n    resolution: \"随 NEW-1 一同解决。\"\n    resolution_round: 19\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 18\n    resolution: \"连续五轮未被提出。\"\n    resolution_round: 18\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: §4.5 扩展 logistic 讨论。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: Abstract + Conclusion linear SEM qualifier added。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W2 再提。共识 should-fix。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 R1-W4 (should-fix) 提出 exposure 下 logistic 校正恶化 -78%，Limitations 过于简略。R2 在交叉回应中 partial REBUT：附录 B.7/B.14 已提供更充分的非线性验证（covariate 拓扑 FWL invariance 保持），R1 的批评主要针对 Limitations 呈现方式而非证据缺失。共识：附录证据充分但需在 Limitations 中更突出引用。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 确认 'first unified analysis' 在当前文献范围内成立。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 限定词简化。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 fix: 改为 'first multi-class (K≥3) topology-specific analysis'。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W3 再提。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。R2-S1 反而确认 'first systematic analysis 的声明在合理范围内'。可能已修复至可接受水平。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 R1-W3。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 R1-W3。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续三轮未提出。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: minor\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: column-stochastic 括号说明已加入。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: FWL, Wald inline explanations added。共识 minor。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 minor。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位再提（R1-W6 minor, R2-W4 minor）。plim/FWL/column-stochastic 仍对 NLP 读者不够直观。R2 建议增加 Reader's Guide 段落，R1 建议增加 intuition 段落。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 minor。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 R1 提 x 轴 scale 差异大。minor。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 minor。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 Reviewers 未单独提出。视觉审查 Agent 发现 Figure 2 legend 文字偏小（~7pt）、灰度打印对比度可能不足。minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"两位共识。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续四轮未提出，可能已修复。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 21\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: 随 R9-C2 一同修复。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。R19 fix 生效。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续两轮未提出。\"\n    action_items:\n      - round: 19\n        action: \"随 R9-C2 一同修复：Abstract + Conclusion linear SEM qualifier\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 fix: primary coefficient hedge + sampling method note added。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续两轮未提出，R19 fix 生效。\"\n    action_items:\n      - round: 19\n        action: \"Q5 fix: primary coefficient hedge + sampling note added\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 3 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: FWL 降为 Observation，Contribution 3 重聚焦。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1-W4 再提 Algorithm 1 阈值。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 R2-W5 (minor) 认为 Algorithm 1 作为三大贡献之一实质性偏弱，建议降级为 practical implication。R1 在交叉回应中 REBUT：FWL 不变性是 Algorithm 1 的核心理论基础，topology-dependent routing 概念本身有贡献。分歧缩小为定位方式。共识 should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words by 3 counting methods. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Theorem 2 现为 collider 提供 K=3 symmetric 理论证明。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。连续三轮未提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续四轮未提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"dawid1979, rosenbaum2002 未引用。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: 3 orphans removed。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 fix: 5 new orphans removed。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 R2 引用验证通过，未提出 bib 问题。连续两轮未提出。\"\n\n  # === Round 20 发现 ===\n\n  - id: R20-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中很少成立——缺少合理性讨论和经验量化\"\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 20\n        reviewers: [R1]\n        note: \"R1-W1：真实 LLM confusion matrix 通常高度不对称。未报告经验矩阵中有多少满足对称性。建议量化 Frobenius distance。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位独立再提。与 R8-C1 高度重叠——R1-W1 (must-fix) 指出 d_rel=0.33 意味着 Theorem 2 '不是近似成立而是显著偏离'；R2-W1 (should-fix) 同意。共识：Theorem 2 应在正文中重新定位为 theoretical anchor 而非实用工具。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R20-N2\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 决策阈值缺乏理论依据和跨设置稳定性验证\"\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R1-W4: 阈值来自特定模拟设置，未验证跨 K/DGP/N 稳定性。R2-Q1: DAG 不确定性下 sensitivity。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 R1-Q3 和 R2-Q2 间接触及（DAG 不确定性下如何使用框架？阈值是否应依赖 sample size？）。R2 交叉回应中 AGREE 需要 sensitivity analysis。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 21 新发现 ===\n\n  - id: R21-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 adversarial search 覆盖系统性不明——4 种结构族基于直觉选择，未尝试梯度优化\"\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R1-W5 (should-fix): 4 种 adversarial 结构族选择缺少系统性论证，未解释为何不存在更病态结构。R2 交叉回应 AGREE 但提供平衡视角：max violation 0.017 极小，实践影响可忽略。共识 should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R21-W2\n    category: presentation\n    severity: minor\n    summary: \"Correction routing (Algorithm 1) 作为三大贡献之一权重可能过高\"\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [R2]\n        note: \"R2-W5 (minor): Algorithm 1 本质是已有方法的拓扑适配决策树，建议降为 practical implication。R1 REBUT: FWL 不变性发现是核心理论基础，topology-dependent routing 概念本身有贡献。分歧存在但非重大。\"\n    resolution: \"\"\n    resolution_round: null"
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
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 21\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix（低优先级）。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 再提 Dirichlet 采样代表性。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Limitations 已覆盖。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。Limitations 已覆盖。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续三轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 21\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出，R18 修复充分。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 两位 Reviewer 再次提出。要求在主文增加讨论。共识 should-fix。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位 Reviewer 再次提出（R1-Q4, R2-W2）。主文仅在 Limitations 一句带过，Section 3.1 的 architectural invariant 论证不充分——content-dependent proxy（topic, sentiment）的 Y-stratification 显著（B.25），但未在主文讨论违反时后果。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 19\n    resolution: \"R18 压缩后编译验证 main text ≤8 pages。R19 PDF 确认合规。连续两轮无复发。\"\n    resolution_round: 19\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: minor\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1 联合。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提。共识 minor。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续两轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: must-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据——缺少端到端因果应用验证\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 升级为 critical。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位 Reviewer 再次独立提出（R1-W2 must-fix, R2-W3 should-fix）。共识：对 EMNLP 应用导向 venue，缺少在真实 NLP 任务中走完 annotate→estimate→correct 全流程的案例是显著缺口。ClinicalBERT (B.3) 和 End-to-End Demo (B.19) 均使用合成 ground truth。建议使用已有 HumAID 混淆矩阵增加端到端因果分析。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: Remark 1 重写为 complementary tools。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提。共识 should-fix。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W5 再提。共识 should-fix。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出为 weakness。R2-S3 反而肯定了 ASV 与 E-values 的区分（Remark 1 的 topology dependence + sign-flip 维度'有说服力'）。可能已修复至可接受水平。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: must-fix\n    summary: \"Proportional effects 假设在 NLP 中是强限制，且 Limitations 中完全缺失\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 增加 stance detection/sentiment analysis 场景讨论 + 97.3% empirical compliance。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位再提。共识 should-fix（高优先级）。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 升级为 critical。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 R1-W3 (should-fix) 再提：Table 14 显示独立 f,g 下 OOB 率 23%，主文缺少对 NLP 场景中 proportional effects 合理性的实质论证。R2 在交叉回应中 AGREE。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem/Conjecture 边界在主文中模糊\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 must-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 2 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位再次列为 critical。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 再次提出。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位独立再提（R1-W1 must-fix, R2-W1 should-fix）。核心矛盾不变：Theorem 1 仅 K=2，Theorem 2 要求对称 C₀（实际偏差 d_rel=0.33），Conjecture 1 未证。R2 精炼总结为'已证但不实用 vs 实用但未证'。R1 在交叉回应中强烈 AGREE。共识：需更明确定位 Theorem 2 为 theoretical anchor，并讨论 Conjecture→Theorem 的证明障碍。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"与 R6-M3 合并。\"\n      - round: 21\n        reviewers: [R1]\n        note: \"与 R6-M3 合并。R21 R1-W3。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 21\n        reviewers: []\n        note: \"与 R4-W6 合并。R21 未单独提出，R2-S3 反而肯定 ASV 区分度。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 19\n    resolution: \"随 NEW-1 一同解决。\"\n    resolution_round: 19\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 18\n    resolution: \"连续五轮未被提出。\"\n    resolution_round: 18\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: §4.5 扩展 logistic 讨论。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: Abstract + Conclusion linear SEM qualifier added。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W2 再提。共识 should-fix。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 R1-W4 (should-fix) 提出 exposure 下 logistic 校正恶化 -78%，Limitations 过于简略。R2 在交叉回应中 partial REBUT：附录 B.7/B.14 已提供更充分的非线性验证（covariate 拓扑 FWL invariance 保持），R1 的批评主要针对 Limitations 呈现方式而非证据缺失。共识：附录证据充分但需在 Limitations 中更突出引用。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 确认 'first unified analysis' 在当前文献范围内成立。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 限定词简化。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 fix: 改为 'first multi-class (K≥3) topology-specific analysis'。\"\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W3 再提。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。R2-S1 反而确认 'first systematic analysis 的声明在合理范围内'。可能已修复至可接受水平。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 R1-W3。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 R1-W3。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续三轮未提出。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: minor\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: column-stochastic 括号说明已加入。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: FWL, Wald inline explanations added。共识 minor。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 minor。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位再提（R1-W6 minor, R2-W4 minor）。plim/FWL/column-stochastic 仍对 NLP 读者不够直观。R2 建议增加 Reader's Guide 段落，R1 建议增加 intuition 段落。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 minor。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 R1 提 x 轴 scale 差异大。minor。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 minor。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 Reviewers 未单独提出。视觉审查 Agent 发现 Figure 2 legend 文字偏小（~7pt）、灰度打印对比度可能不足。minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"两位共识。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续四轮未提出，可能已修复。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 21\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: 随 R9-C2 一同修复。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。R19 fix 生效。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续两轮未提出。\"\n    action_items:\n      - round: 19\n        action: \"随 R9-C2 一同修复：Abstract + Conclusion linear SEM qualifier\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 fix: primary coefficient hedge + sampling method note added。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续两轮未提出，R19 fix 生效。\"\n    action_items:\n      - round: 19\n        action: \"Q5 fix: primary coefficient hedge + sampling note added\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 3 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 fix: FWL 降为 Observation，Contribution 3 重聚焦。\"\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1-W4 再提 Algorithm 1 阈值。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 R2-W5 (minor) 认为 Algorithm 1 作为三大贡献之一实质性偏弱，建议降级为 practical implication。R1 在交叉回应中 REBUT：FWL 不变性是 Algorithm 1 的核心理论基础，topology-dependent routing 概念本身有贡献。分歧缩小为定位方式。共识 should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words by 3 counting methods. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Theorem 2 现为 collider 提供 K=3 symmetric 理论证明。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。连续三轮未提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。连续四轮未提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"dawid1979, rosenbaum2002 未引用。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: 3 orphans removed。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 fix: 5 new orphans removed。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 R2 引用验证通过，未提出 bib 问题。连续两轮未提出。\"\n\n  # === Round 20 发现 ===\n\n  - id: R20-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中很少成立——缺少合理性讨论和经验量化\"\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 20\n        reviewers: [R1]\n        note: \"R1-W1：真实 LLM confusion matrix 通常高度不对称。未报告经验矩阵中有多少满足对称性。建议量化 Frobenius distance。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 两位独立再提。与 R8-C1 高度重叠——R1-W1 (must-fix) 指出 d_rel=0.33 意味着 Theorem 2 '不是近似成立而是显著偏离'；R2-W1 (should-fix) 同意。共识：Theorem 2 应在正文中重新定位为 theoretical anchor 而非实用工具。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R20-N2\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 决策阈值缺乏理论依据和跨设置稳定性验证\"\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R1-W4: 阈值来自特定模拟设置，未验证跨 K/DGP/N 稳定性。R2-Q1: DAG 不确定性下 sensitivity。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 R1-Q3 和 R2-Q2 间接触及（DAG 不确定性下如何使用框架？阈值是否应依赖 sample size？）。R2 交叉回应中 AGREE 需要 sensitivity analysis。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 21 新发现 ===\n\n  - id: R21-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 adversarial search 覆盖系统性不明——4 种结构族基于直觉选择，未尝试梯度优化\"\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R1-W5 (should-fix): 4 种 adversarial 结构族选择缺少系统性论证，未解释为何不存在更病态结构。R2 交叉回应 AGREE 但提供平衡视角：max violation 0.017 极小，实践影响可忽略。共识 should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R21-W2\n    category: presentation\n    severity: minor\n    summary: \"Correction routing (Algorithm 1) 作为三大贡献之一权重可能过高\"\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [R2]\n        note: \"R2-W5 (minor): Algorithm 1 本质是已有方法的拓扑适配决策树，建议降为 practical implication。R1 REBUT: FWL 不变性发现是核心理论基础，topology-dependent routing 概念本身有贡献。分歧存在但非重大。\"\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1761 · 2026-05-23T20:06:03.319016+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 25187}, \"error\": \"\"}"}

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

_source line 1762 · 2026-05-23T20:08:38.775488+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "report": "# 审稿报告 — Round 21 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**目标 Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人 — R1 方法严谨性 / R2 新颖性与完整性\n**轮次**: 1 轮达成共识（无需第二轮）\n\n---\n\n## Summary\n\n本文研究 LLM 生成的 K 类标注误差如何在 7 种典型 DAG 拓扑（confounding, exposure, mediation, collider, M-bias, front-door, IV）下传播到下游因果估计。作者推导了每种拓扑的 bias 表达式，证明 K≥3 时 exposure 和 IV 拓扑可发生符号反转（二分类情况下不可能），提出 Annotation Sensitivity Values (ASV) 诊断工具，并基于 FWL 不变性给出 topology-aware 校正路由。理论结果通过 100,000 Dirichlet 矩阵采样、545,945 adversarial 曲线、23 个真实 LLM 配置和 Monte Carlo 验证（MAPE 1.6%）支撑。\n\n---\n\n## Strengths\n\n**[S1] 系统性填补文献空白（R1-S1, R2-S1, 双方 AGREE）。** 7 种 DAG 拓扑 × K≥3 多分类的统一分析是此前文献中缺失的。Brenner (1993) 仅覆盖多分类混杂变量，Dosemeci (1990) 仅覆盖多分类暴露，Teblunthuis (2024) 限于二分类，Lee & Wood-Doughty (2024) 限于单一拓扑。\"first systematic analysis\" 声明在合理范围内。\n\n**[S2] K≥3 符号反转结果具有实践警示价值（R1-S1, R2-S2, 双方 AGREE）。** Figure 2 展示的拓扑分化（exposure 83.4% sign reversal, IV 52.6%, 其余 5 种拓扑 0%）是一个有意义的负面发现，直接告知实践者哪些拓扑需要额外警惕。\n\n**[S3] 证明严谨（R1-S2, R2 交叉 AGREE）。** R1 逐步验证了 Theorem 1（perspective function 凸性论证）、Theorem 2（对称分解 + 因式分解）和 Proposition 1-3（Cauchy-Schwarz），均正确。R2 独立确认。\n\n**[S4] 诚实的理论边界声明（R1-S3, R2 交叉 AGREE）。** Theorem 2 对称假设在 Remark 4 中被坦诚讨论为 \"theoretical anchor\"；Conjecture 1 被正确标注；proportional effects 违反率（23%）被量化报告。\n\n**[S5] 多层数值验证体系超出同类工作标准（R1-S4, R2-S4, 双方 AGREE）。** 100,000 Dirichlet + 545,945 adversarial + 23 真实 LLM 配置 + Monte Carlo (MAPE 1.6%)。\n\n**[S6] FWL 不变性的\"负面结果\"有实践指导价值（R1-S5, R2-S5, 双方 AGREE）。** 矩阵校正在 4 种 covariate 拓扑下无效（RMSE 减少 0%），阻止了盲目应用校正方法。\n\n**[S7] Related Work 覆盖全面，引用验证通过（R2-S6）。** R2 验证了关键引用的真实性（Brenner 1993, Dosemeci 1990, Angelopoulos et al. 2023, Lee & Wood-Doughty 2024, Baumann et al. 2025）。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**[MF-1] K≥3 理论贡献呈现\"已证但不实用 vs 实用但未证\"的尴尬结构（R1-W1 must-fix, R2-W1 should-fix, 共识）。**\n- Theorem 1 仅对 K=2 完全成立——对 NLP 场景最不相关（多数任务 K≥3）\n- Theorem 2 要求 K=3 对称混淆矩阵——10 个 VAST 配置的实际偏差 d_rel=0.33（Remark 4, p.18），不是\"近似成立\"而是\"显著偏离\"\n- Conjecture 1（一般 K≥3）有充分数值支持（ε < 0.017）但未获证明\n- 论文在正文 p.6 将 Theorem 2 呈现为主要理论结果，附录才承认局限，可能误导读者\n- **建议**：在正文中将 Theorem 2 明确定位为 theoretical anchor（证明单调性结构在特定条件下精确成立，为 Conjecture 1 提供结构性支撑），而非实用保证；讨论 Conjecture→Theorem 的证明障碍（是 K≥3 列随机矩阵的组合复杂性，还是存在根本困难？）\n\n**[MF-2] 缺少端到端的真实 NLP 因果推断应用（R1-W2 must-fix, R2-W3 should-fix, 强共识）。**\n- 对 EMNLP 应用导向 venue，当前所有实验均为\"验证理论正确性\"（Monte Carlo vs 解析解）或\"验证假设成立\"（non-differential test），缺少完整场景：在真实 NLP 任务中使用 LLM 标注→ASV 诊断→校正→因果估计，展示框架如何改变实质性因果结论\n- ClinicalBERT (Appendix B.3) 使用真实混淆矩阵但合成 ground truth；End-to-End Demo (B.19) 同样基于合成 DGP\n- 论文已有 HumAID (K=10) 的混淆矩阵，增加对应的端到端因果分析（如灾害类型→公众响应的因果效应估计）可行性较高\n- **建议**：增加至少一个真实 NLP 因果推断案例，完整展示 annotate→estimate→correct 全流程\n\n### Should-Fix\n\n**[SF-1] Non-differential misclassification 假设在 NLP 中可能过强，主文讨论不足（R1-W3/Q4, R2-W2, 共识）。**\n- 主文 Section 3.1 以\"architectural invariant\"（LLM 只看 text，不看 Y）为由论证 non-differential 成立，但 Appendix B.25 的 content-dependent proxy 测试（topic, sentiment）显示显著 Y-stratification（12/12 中仅 1/12 拒绝是因为 content-independent proxy 占多数）\n- R1 指出关键细微之处：如果 A 完全中介 text features→Y，non-differential 仍可成立；但 NLP 中 Y 和 text 的关系通常更复杂\n- **建议**：在 Section 3.1 或 Limitations 中增加 2-3 句讨论：(a) 哪些 NLP 任务满足 non-differential（content-independent proxy）；(b) 违反时偏差表达式如何变化；(c) 引导到附录 B.25 的实证检验\n\n**[SF-2] Proportional effects 假设的 NLP 适用性缺少实质论证（R1-W3, R2 交叉 AGREE, 共识）。**\n- 该假设（f=λg）是 Theorems 1-2 的核心前提\n- Table 14 (B.13) 显示独立 f,g 下 OOB 率达 23%；Table 18 报告 97.3% sign preservation，但混合了 proportional/non-proportional\n- 主文几乎未讨论 NLP 因果场景中 f=λg 的实质合理性\n- **建议**：增加 1-2 句 domain-specific 论证，说明哪些 NLP 场景 proportional effects 合理（如单一质量维度驱动两条路径），哪些不合理\n\n**[SF-3] Linear SEM 适用范围在 Limitations 中讨论过于简略（R1-W4 should-fix, R2 partial REBUT, 部分共识）。**\n- R1 指出 exposure 下 logistic 校正恶化 -78%，Limitations 仅\"assume linear SEMs\"一句\n- R2 partial REBUT：附录 B.7/B.14 已提供充分非线性验证（covariate 拓扑 FWL invariance 保持，mean logistic bias reduction ≤5%），R1 的批评主要针对呈现方式\n- **建议**：在 Limitations 中明确引用附录结论——哪些拓扑在非线性下仍成立（covariate），哪些不成立（exposure），实践者应如何调整\n\n**[SF-4] Conjecture 1 的 adversarial search 系统性不明（R1-W5, R2 交叉 AGREE with balance, 共识但低优先级）。**\n- 4 种结构族基于直觉选择，未解释为何足以覆盖潜在 counterexample 空间\n- R2 提供平衡：max violation 0.017 极小，实践影响可忽略\n- **建议**：增加一段说明为何这 4 种族具有代表性，或是否尝试过梯度优化寻找最大违反\n\n### Minor\n\n**[MI-1] 对 EMNLP 读者可达性有待提升（R1-W6, R2-W4, 双方 AGREE）。**\n- plim, FWL, column-stochastic 等计量经济学概念对 NLP/ML 读者不够直观\n- **建议**：Section 3.1 增加 2-3 句\"Reader's Guide\"，用非技术语言解释 bias 传播核心机制\n\n**[MI-2] Correction routing (Algorithm 1) 作为三大贡献之一的权重定位（R2-W5 minor, R1 REBUT, 分歧存在）。**\n- R2 认为 Algorithm 1 本质是已有方法的拓扑适配决策树\n- R1 REBUT：FWL 不变性发现是核心理论基础，topology-dependent routing 概念本身有贡献\n- 分歧已缩小为定位方式问题\n- **建议**：强调 FWL 不变性发现作为独立贡献，将 Algorithm 1 定位为该发现的实践推论\n\n**[MI-3] Venue 适配度处于边界（R2-W6, R1 隐含同意）。**\n- 核心贡献在统计/计量层面，NLP 连接主要通过应用背景\n- 不构成拒稿理由——ARR guidelines 允许跨学科方法\n- 如补充真实 NLP 因果应用（MF-2），此问题自然消解\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致（交叉回应中均 [AGREE]）：\n\n| # | 问题 | R1 定级 | R2 定级 | 共识定级 |\n|---|------|---------|---------|----------|\n| 1 | K≥3 理论贡献依赖 conjecture | must-fix | should-fix | **must-fix** |\n| 2 | 缺少端到端真实 NLP 因果应用 | must-fix | should-fix | **must-fix** |\n| 3 | Non-differential 假设主文讨论不足 | should-fix (Q4) | should-fix | **should-fix** |\n| 4 | Proportional effects NLP 适用性 | should-fix | should-fix (交叉 AGREE) | **should-fix** |\n| 5 | EMNLP 读者可达性 | minor | minor | **minor** |\n\n---\n\n## Reviewer Divergence\n\n| # | 问题 | R1 立场 | R2 立场 | 解决状态 |\n|---|------|---------|---------|----------|\n| 1 | Algorithm 1 贡献权重 | REBUT：FWL 不变性赋予实质价值 | minor：本质是决策树 | 分歧缩小为定位方式，非根本矛盾 |\n| 2 | Linear SEM 讨论 | should-fix：Limitations 过于简略 | partial REBUT：附录证据充分 | R2 论证有力（B.7/B.14），共识为改善 Limitations 呈现 |\n| 3 | Soundness 评分 | 3.5/5 | 4.0/5 | R2 论证合理（claims 在 stated assumptions 内被充分支撑），取均值 3.75 |\n\n---\n\n## Questions（需作者澄清）\n\n**[Q1]** Conjecture 1 的证明障碍具体是什么？是 K≥3 列随机矩阵的组合复杂性，还是特定拓扑存在结构性困难？是否有证据表明该 conjecture 可能为假？（R1-Q1, R2-Q1 共同追问）\n\n**[Q2]** DAG 拓扑不确定时（NLP 因果推断中常见），实践者应如何使用本框架？是否对所有 7 种拓扑计算 ASV 并取最坏情况？（R2-Q2）\n\n**[Q3]** ASV bootstrap CI 的 gold-standard 标签样本量对估计精度的影响？是否有最低样本量的经验规则？（R2-Q3）\n\n**[Q4]** Algorithm 1 的阈值（risk level 分类）如何确定？是否应取决于 sample size 或其他条件？是否有 sensitivity analysis？（R1-Q3, R2 交叉 AGREE）\n\n**[Q5]** Content-dependent proxy 导致 Y-stratification 显著时（如 stance detection），实践者应如何使用本框架？non-differential 假设在这类核心 NLP 任务中是否系统性地不成立？（R1-Q4）\n\n**[Q6]** 非比例效应 (non-proportional f,g) 下 Theorem 1 的 monotonicity violation magnitude 有多大？Table 14 报告 OOB 率但未报告 violation 幅度。（R1-Q1, R2 交叉补充）\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现重大引用遗漏。R2 验证了关键引用的真实性。可选补充：proximal causal inference with text data 文献（Mozer et al., Tchetgen Tchetgen 系列）——与本文 measurement error 视角互补但非必须。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未启用。项目配置中 `external_review.paperreview_ai.enabled` 未设置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（3 warnings, 0 critical, 19 info）\n\n关键发现：\n- **[Warning]** Pages 1-2 为连续纯文本（Title/Abstract/Introduction/Related Work），第一个 display item（Figure 1 DAG 拓扑图）直到 page 3 才出现。审稿人前 2 页看到的全是文字，缺少视觉锚定。建议考虑将 Figure 1 提前。\n- **[Warning]** Figure 2 的 \"Red = sign reversal\" 图例文字非常小（~7pt），灰度打印时红色填充对比度可能不足。\n- **[Warning]** Table 9（Appendix B.6, pp.25-26）跨两页，数值密度极高，建议在 caption 中标注关键行/列。\n- **[Info]** 正文 8 页含 4 figures + 1 table = 5 个 display items，密度合理。所有表格使用 booktabs 风格。无 margin 溢出、引用未解析等排版问题。格式合规（8 页正文，Limitations 在正文内，双盲匿名）。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 3.75 / 5 (R1: 3.5, R2: 4.0)\n**Excitement**: 3.0 / 5 (R1: 3.0, R2: 3.0)\n**Reproducibility**: 4.0 / 5\n**Confidence**: 4.0 / 5\n\n### 评分理由\n\n本文在一个重要且日益相关的问题（LLM 标注误差的因果传播）上做出了系统性贡献。7 种拓扑的 bias 分类学填补了文献空白（S1），K≥3 符号反转结果对实践者有直接警示价值（S2），证明在其假设范围内严格正确（S3），数值验证体系超出同类工作标准（S5）。\n\n阻碍达到 4.0 (Conference) 的原因：\n\n1. **理论覆盖与实际需求的错位（MF-1）**：Theorem 2 对称假设偏差约 33%，K≥3 核心结论依赖未证 Conjecture 1。论文的理论贡献呈现\"已证但不实用 vs 实用但未证\"的结构性矛盾。\n\n2. **应用验证的缺失（MF-2）**：对 EMNLP 应用导向 venue，缺少一个真实 NLP 因果推断端到端案例是显著短板。所有实验均为\"验证理论\"而非\"展示影响\"。\n\n3. **核心假设的 NLP 适用性论证不足（SF-1, SF-2）**：Non-differential misclassification 和 proportional effects 两个核心假设在 NLP 场景中的合理性讨论分散在附录，主文几乎未触及。\n\n### 修改建议优先级\n\n| 优先级 | 问题 | 预估工作量 |\n|--------|------|-----------|\n| P0 | 增加端到端真实 NLP 因果案例 | 中（已有 HumAID 混淆矩阵） |\n| P0 | 正文重新定位 Theorem 2（theoretical anchor + Conjecture 证明障碍讨论） | 小 |\n| P1 | Non-differential 假设的 NLP 适用性讨论前置到主文 | 小 |\n| P1 | Proportional effects 的 NLP 场景论证 | 小 |\n| P2 | Limitations 中引用附录非线性验证结论 | 小 |\n| P2 | Section 3.1 增加 Reader's Guide | 小 |\n| P3 | Conjecture 1 adversarial search 系统性说明 | 小 |\n\n如 P0 问题得到解决，评分可上调至 **4.0 (Conference)**。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 叙事逻辑清晰，K=2→K≥3 的 structural transition 论证有力\n- 三个贡献的陈述可微调：Contribution 3 (correction routing) 的 FWL 不变性发现值得更突出\n- 数字密度尚可接受（相比早期版本已显著改善）\n\n### Section 2 (Related Work)\n- 三段覆盖（measurement error / text classifiers / sensitivity analysis）结构合理\n- 引用验证通过，无虚构引用\n- 与已有工作的定位公平——既不过度贬低也不过度夸大自身贡献\n\n### Section 3 (Method)\n- Definition 1 (non-differential) 简洁但主文讨论不足——需增加 NLP 适用性论证（SF-1）\n- Equations 1-2 (confounding/exposure bias) 推导正确\n- Theorem 1-2 证明严格但适用范围窄——需正文重新定位（MF-1）\n- Conjecture 1 表述诚实，数值证据充分，但证明障碍未讨论\n- Remark 1 (ASV vs E-values) 区分有说服力（topology dependence + sign-flip 维度）\n- 符号负担较重——Reader's Guide 段落可显著改善可达性\n\n### Section 4 (Experiments)\n- 4.2 Bias Taxonomy：Monte Carlo 验证 (MAPE 1.6%) 可靠\n- 4.3 ASV Framework：Figure 3 vulnerability ranking 直观有效\n- 4.4 Empirical Validation：HumAID/VAST/CivilComments 真实混淆矩阵验证了理论预测，但缺少端到端因果应用（MF-2）\n- 4.5 Correction Guidance：FWL invariance observation 有价值；Algorithm 1 阈值需要 sensitivity analysis\n\n### Conclusion / Limitations\n- Conclusion 简洁到位\n- Limitations 段落过短——需增加 non-differential、proportional effects、linear SEM 的整合讨论\n- 当前 Limitations 仅 3 个点，符合 EMNLP 规范但不够充分\n\n### Appendix\n- 证明完整（A.4-A.6），R1 逐步验证通过\n- 数值验证附录极其详尽（24 页），超出审稿期望\n- Table 9 (B.6) 跨页密集，建议标注关键行列"
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
    "overall_score": "borderline",
    "report": "# 审稿报告 — Round 21 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**目标 Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人 — R1 方法严谨性 / R2 新颖性与完整性\n**轮次**: 1 轮达成共识（无需第二轮）\n\n---\n\n## Summary\n\n本文研究 LLM 生成的 K 类标注误差如何在 7 种典型 DAG 拓扑（confounding, exposure, mediation, collider, M-bias, front-door, IV）下传播到下游因果估计。作者推导了每种拓扑的 bias 表达式，证明 K≥3 时 exposure 和 IV 拓扑可发生符号反转（二分类情况下不可能），提出 Annotation Sensitivity Values (ASV) 诊断工具，并基于 FWL 不变性给出 topology-aware 校正路由。理论结果通过 100,000 Dirichlet 矩阵采样、545,945 adversarial 曲线、23 个真实 LLM 配置和 Monte Carlo 验证（MAPE 1.6%）支撑。\n\n---\n\n## Strengths\n\n**[S1] 系统性填补文献空白（R1-S1, R2-S1, 双方 AGREE）。** 7 种 DAG 拓扑 × K≥3 多分类的统一分析是此前文献中缺失的。Brenner (1993) 仅覆盖多分类混杂变量，Dosemeci (1990) 仅覆盖多分类暴露，Teblunthuis (2024) 限于二分类，Lee & Wood-Doughty (2024) 限于单一拓扑。\"first systematic analysis\" 声明在合理范围内。\n\n**[S2] K≥3 符号反转结果具有实践警示价值（R1-S1, R2-S2, 双方 AGREE）。** Figure 2 展示的拓扑分化（exposure 83.4% sign reversal, IV 52.6%, 其余 5 种拓扑 0%）是一个有意义的负面发现，直接告知实践者哪些拓扑需要额外警惕。\n\n**[S3] 证明严谨（R1-S2, R2 交叉 AGREE）。** R1 逐步验证了 Theorem 1（perspective function 凸性论证）、Theorem 2（对称分解 + 因式分解）和 Proposition 1-3（Cauchy-Schwarz），均正确。R2 独立确认。\n\n**[S4] 诚实的理论边界声明（R1-S3, R2 交叉 AGREE）。** Theorem 2 对称假设在 Remark 4 中被坦诚讨论为 \"theoretical anchor\"；Conjecture 1 被正确标注；proportional effects 违反率（23%）被量化报告。\n\n**[S5] 多层数值验证体系超出同类工作标准（R1-S4, R2-S4, 双方 AGREE）。** 100,000 Dirichlet + 545,945 adversarial + 23 真实 LLM 配置 + Monte Carlo (MAPE 1.6%)。\n\n**[S6] FWL 不变性的\"负面结果\"有实践指导价值（R1-S5, R2-S5, 双方 AGREE）。** 矩阵校正在 4 种 covariate 拓扑下无效（RMSE 减少 0%），阻止了盲目应用校正方法。\n\n**[S7] Related Work 覆盖全面，引用验证通过（R2-S6）。** R2 验证了关键引用的真实性（Brenner 1993, Dosemeci 1990, Angelopoulos et al. 2023, Lee & Wood-Doughty 2024, Baumann et al. 2025）。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**[MF-1] K≥3 理论贡献呈现\"已证但不实用 vs 实用但未证\"的尴尬结构（R1-W1 must-fix, R2-W1 should-fix, 共识）。**\n- Theorem 1 仅对 K=2 完全成立——对 NLP 场景最不相关（多数任务 K≥3）\n- Theorem 2 要求 K=3 对称混淆矩阵——10 个 VAST 配置的实际偏差 d_rel=0.33（Remark 4, p.18），不是\"近似成立\"而是\"显著偏离\"\n- Conjecture 1（一般 K≥3）有充分数值支持（ε < 0.017）但未获证明\n- 论文在正文 p.6 将 Theorem 2 呈现为主要理论结果，附录才承认局限，可能误导读者\n- **建议**：在正文中将 Theorem 2 明确定位为 theoretical anchor（证明单调性结构在特定条件下精确成立，为 Conjecture 1 提供结构性支撑），而非实用保证；讨论 Conjecture→Theorem 的证明障碍（是 K≥3 列随机矩阵的组合复杂性，还是存在根本困难？）\n\n**[MF-2] 缺少端到端的真实 NLP 因果推断应用（R1-W2 must-fix, R2-W3 should-fix, 强共识）。**\n- 对 EMNLP 应用导向 venue，当前所有实验均为\"验证理论正确性\"（Monte Carlo vs 解析解）或\"验证假设成立\"（non-differential test），缺少完整场景：在真实 NLP 任务中使用 LLM 标注→ASV 诊断→校正→因果估计，展示框架如何改变实质性因果结论\n- ClinicalBERT (Appendix B.3) 使用真实混淆矩阵但合成 ground truth；End-to-End Demo (B.19) 同样基于合成 DGP\n- 论文已有 HumAID (K=10) 的混淆矩阵，增加对应的端到端因果分析（如灾害类型→公众响应的因果效应估计）可行性较高\n- **建议**：增加至少一个真实 NLP 因果推断案例，完整展示 annotate→estimate→correct 全流程\n\n### Should-Fix\n\n**[SF-1] Non-differential misclassification 假设在 NLP 中可能过强，主文讨论不足（R1-W3/Q4, R2-W2, 共识）。**\n- 主文 Section 3.1 以\"architectural invariant\"（LLM 只看 text，不看 Y）为由论证 non-differential 成立，但 Appendix B.25 的 content-dependent proxy 测试（topic, sentiment）显示显著 Y-stratification（12/12 中仅 1/12 拒绝是因为 content-independent proxy 占多数）\n- R1 指出关键细微之处：如果 A 完全中介 text features→Y，non-differential 仍可成立；但 NLP 中 Y 和 text 的关系通常更复杂\n- **建议**：在 Section 3.1 或 Limitations 中增加 2-3 句讨论：(a) 哪些 NLP 任务满足 non-differential（content-independent proxy）；(b) 违反时偏差表达式如何变化；(c) 引导到附录 B.25 的实证检验\n\n**[SF-2] Proportional effects 假设的 NLP 适用性缺少实质论证（R1-W3, R2 交叉 AGREE, 共识）。**\n- 该假设（f=λg）是 Theorems 1-2 的核心前提\n- Table 14 (B.13) 显示独立 f,g 下 OOB 率达 23%；Table 18 报告 97.3% sign preservation，但混合了 proportional/non-proportional\n- 主文几乎未讨论 NLP 因果场景中 f=λg 的实质合理性\n- **建议**：增加 1-2 句 domain-specific 论证，说明哪些 NLP 场景 proportional effects 合理（如单一质量维度驱动两条路径），哪些不合理\n\n**[SF-3] Linear SEM 适用范围在 Limitations 中讨论过于简略（R1-W4 should-fix, R2 partial REBUT, 部分共识）。**\n- R1 指出 exposure 下 logistic 校正恶化 -78%，Limitations 仅\"assume linear SEMs\"一句\n- R2 partial REBUT：附录 B.7/B.14 已提供充分非线性验证（covariate 拓扑 FWL invariance 保持，mean logistic bias reduction ≤5%），R1 的批评主要针对呈现方式\n- **建议**：在 Limitations 中明确引用附录结论——哪些拓扑在非线性下仍成立（covariate），哪些不成立（exposure），实践者应如何调整\n\n**[SF-4] Conjecture 1 的 adversarial search 系统性不明（R1-W5, R2 交叉 AGREE with balance, 共识但低优先级）。**\n- 4 种结构族基于直觉选择，未解释为何足以覆盖潜在 counterexample 空间\n- R2 提供平衡：max violation 0.017 极小，实践影响可忽略\n- **建议**：增加一段说明为何这 4 种族具有代表性，或是否尝试过梯度优化寻找最大违反\n\n### Minor\n\n**[MI-1] 对 EMNLP 读者可达性有待提升（R1-W6, R2-W4, 双方 AGREE）。**\n- plim, FWL, column-stochastic 等计量经济学概念对 NLP/ML 读者不够直观\n- **建议**：Section 3.1 增加 2-3 句\"Reader's Guide\"，用非技术语言解释 bias 传播核心机制\n\n**[MI-2] Correction routing (Algorithm 1) 作为三大贡献之一的权重定位（R2-W5 minor, R1 REBUT, 分歧存在）。**\n- R2 认为 Algorithm 1 本质是已有方法的拓扑适配决策树\n- R1 REBUT：FWL 不变性发现是核心理论基础，topology-dependent routing 概念本身有贡献\n- 分歧已缩小为定位方式问题\n- **建议**：强调 FWL 不变性发现作为独立贡献，将 Algorithm 1 定位为该发现的实践推论\n\n**[MI-3] Venue 适配度处于边界（R2-W6, R1 隐含同意）。**\n- 核心贡献在统计/计量层面，NLP 连接主要通过应用背景\n- 不构成拒稿理由——ARR guidelines 允许跨学科方法\n- 如补充真实 NLP 因果应用（MF-2），此问题自然消解\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致（交叉回应中均 [AGREE]）：\n\n| # | 问题 | R1 定级 | R2 定级 | 共识定级 |\n|---|------|---------|---------|----------|\n| 1 | K≥3 理论贡献依赖 conjecture | must-fix | should-fix | **must-fix** |\n| 2 | 缺少端到端真实 NLP 因果应用 | must-fix | should-fix | **must-fix** |\n| 3 | Non-differential 假设主文讨论不足 | should-fix (Q4) | should-fix | **should-fix** |\n| 4 | Proportional effects NLP 适用性 | should-fix | should-fix (交叉 AGREE) | **should-fix** |\n| 5 | EMNLP 读者可达性 | minor | minor | **minor** |\n\n---\n\n## Reviewer Divergence\n\n| # | 问题 | R1 立场 | R2 立场 | 解决状态 |\n|---|------|---------|---------|----------|\n| 1 | Algorithm 1 贡献权重 | REBUT：FWL 不变性赋予实质价值 | minor：本质是决策树 | 分歧缩小为定位方式，非根本矛盾 |\n| 2 | Linear SEM 讨论 | should-fix：Limitations 过于简略 | partial REBUT：附录证据充分 | R2 论证有力（B.7/B.14），共识为改善 Limitations 呈现 |\n| 3 | Soundness 评分 | 3.5/5 | 4.0/5 | R2 论证合理（claims 在 stated assumptions 内被充分支撑），取均值 3.75 |\n\n---\n\n## Questions（需作者澄清）\n\n**[Q1]** Conjecture 1 的证明障碍具体是什么？是 K≥3 列随机矩阵的组合复杂性，还是特定拓扑存在结构性困难？是否有证据表明该 conjecture 可能为假？（R1-Q1, R2-Q1 共同追问）\n\n**[Q2]** DAG 拓扑不确定时（NLP 因果推断中常见），实践者应如何使用本框架？是否对所有 7 种拓扑计算 ASV 并取最坏情况？（R2-Q2）\n\n**[Q3]** ASV bootstrap CI 的 gold-standard 标签样本量对估计精度的影响？是否有最低样本量的经验规则？（R2-Q3）\n\n**[Q4]** Algorithm 1 的阈值（risk level 分类）如何确定？是否应取决于 sample size 或其他条件？是否有 sensitivity analysis？（R1-Q3, R2 交叉 AGREE）\n\n**[Q5]** Content-dependent proxy 导致 Y-stratification 显著时（如 stance detection），实践者应如何使用本框架？non-differential 假设在这类核心 NLP 任务中是否系统性地不成立？（R1-Q4）\n\n**[Q6]** 非比例效应 (non-proportional f,g) 下 Theorem 1 的 monotonicity violation magnitude 有多大？Table 14 报告 OOB 率但未报告 violation 幅度。（R1-Q1, R2 交叉补充）\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现重大引用遗漏。R2 验证了关键引用的真实性。可选补充：proximal causal inference with text data 文献（Mozer et al., Tchetgen Tchetgen 系列）——与本文 measurement error 视角互补但非必须。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未启用。项目配置中 `external_review.paperreview_ai.enabled` 未设置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（3 warnings, 0 critical, 19 info）\n\n关键发现：\n- **[Warning]** Pages 1-2 为连续纯文本（Title/Abstract/Introduction/Related Work），第一个 display item（Figure 1 DAG 拓扑图）直到 page 3 才出现。审稿人前 2 页看到的全是文字，缺少视觉锚定。建议考虑将 Figure 1 提前。\n- **[Warning]** Figure 2 的 \"Red = sign reversal\" 图例文字非常小（~7pt），灰度打印时红色填充对比度可能不足。\n- **[Warning]** Table 9（Appendix B.6, pp.25-26）跨两页，数值密度极高，建议在 caption 中标注关键行/列。\n- **[Info]** 正文 8 页含 4 figures + 1 table = 5 个 display items，密度合理。所有表格使用 booktabs 风格。无 margin 溢出、引用未解析等排版问题。格式合规（8 页正文，Limitations 在正文内，双盲匿名）。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 3.75 / 5 (R1: 3.5, R2: 4.0)\n**Excitement**: 3.0 / 5 (R1: 3.0, R2: 3.0)\n**Reproducibility**: 4.0 / 5\n**Confidence**: 4.0 / 5\n\n### 评分理由\n\n本文在一个重要且日益相关的问题（LLM 标注误差的因果传播）上做出了系统性贡献。7 种拓扑的 bias 分类学填补了文献空白（S1），K≥3 符号反转结果对实践者有直接警示价值（S2），证明在其假设范围内严格正确（S3），数值验证体系超出同类工作标准（S5）。\n\n阻碍达到 4.0 (Conference) 的原因：\n\n1. **理论覆盖与实际需求的错位（MF-1）**：Theorem 2 对称假设偏差约 33%，K≥3 核心结论依赖未证 Conjecture 1。论文的理论贡献呈现\"已证但不实用 vs 实用但未证\"的结构性矛盾。\n\n2. **应用验证的缺失（MF-2）**：对 EMNLP 应用导向 venue，缺少一个真实 NLP 因果推断端到端案例是显著短板。所有实验均为\"验证理论\"而非\"展示影响\"。\n\n3. **核心假设的 NLP 适用性论证不足（SF-1, SF-2）**：Non-differential misclassification 和 proportional effects 两个核心假设在 NLP 场景中的合理性讨论分散在附录，主文几乎未触及。\n\n### 修改建议优先级\n\n| 优先级 | 问题 | 预估工作量 |\n|--------|------|-----------|\n| P0 | 增加端到端真实 NLP 因果案例 | 中（已有 HumAID 混淆矩阵） |\n| P0 | 正文重新定位 Theorem 2（theoretical anchor + Conjecture 证明障碍讨论） | 小 |\n| P1 | Non-differential 假设的 NLP 适用性讨论前置到主文 | 小 |\n| P1 | Proportional effects 的 NLP 场景论证 | 小 |\n| P2 | Limitations 中引用附录非线性验证结论 | 小 |\n| P2 | Section 3.1 增加 Reader's Guide | 小 |\n| P3 | Conjecture 1 adversarial search 系统性说明 | 小 |\n\n如 P0 问题得到解决，评分可上调至 **4.0 (Conference)**。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 叙事逻辑清晰，K=2→K≥3 的 structural transition 论证有力\n- 三个贡献的陈述可微调：Contribution 3 (correction routing) 的 FWL 不变性发现值得更突出\n- 数字密度尚可接受（相比早期版本已显著改善）\n\n### Section 2 (Related Work)\n- 三段覆盖（measurement error / text classifiers / sensitivity analysis）结构合理\n- 引用验证通过，无虚构引用\n- 与已有工作的定位公平——既不过度贬低也不过度夸大自身贡献\n\n### Section 3 (Method)\n- Definition 1 (non-differential) 简洁但主文讨论不足——需增加 NLP 适用性论证（SF-1）\n- Equations 1-2 (confounding/exposure bias) 推导正确\n- Theorem 1-2 证明严格但适用范围窄——需正文重新定位（MF-1）\n- Conjecture 1 表述诚实，数值证据充分，但证明障碍未讨论\n- Remark 1 (ASV vs E-values) 区分有说服力（topology dependence + sign-flip 维度）\n- 符号负担较重——Reader's Guide 段落可显著改善可达性\n\n### Section 4 (Experiments)\n- 4.2 Bias Taxonomy：Monte Carlo 验证 (MAPE 1.6%) 可靠\n- 4.3 ASV Framework：Figure 3 vulnerability ranking 直观有效\n- 4.4 Empirical Validation：HumAID/VAST/CivilComments 真实混淆矩阵验证了理论预测，但缺少端到端因果应用（MF-2）\n- 4.5 Correction Guidance：FWL invariance observation 有价值；Algorithm 1 阈值需要 sensitivity analysis\n\n### Conclusion / Limitations\n- Conclusion 简洁到位\n- Limitations 段落过短——需增加 non-differential、proportional effects、linear SEM 的整合讨论\n- 当前 Limitations 仅 3 个点，符合 EMNLP 规范但不够充分\n\n### Appendix\n- 证明完整（A.4-A.6），R1 逐步验证通过\n- 数值验证附录极其详尽（24 页），超出审稿期望\n- Table 9 (B.6) 跨页密集，建议标注关键行列"
  }
}
```

</details>

---


### Tool result

_source line 1763 · 2026-05-23T20:08:42.492310+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3716
}
```

</details>

---


### Assistant

_source line 1764 · 2026-05-23T20:08:52.581226+00:00_

审稿报告已投递至 Research Director。

**Round 21 审稿完成。** 汇总：

- **Overall**: 3.5 / 5 (Borderline Conference)
- **两位 Reviewer 独立给出 3.5，交叉讨论后维持**
- **2 个 Must-Fix**：(1) K≥3 理论贡献依赖未证 Conjecture，Theorem 2 对称假设实际偏差 33%；(2) 缺少端到端真实 NLP 因果推断应用
- **4 个 Should-Fix**：non-differential 假设讨论、proportional effects NLP 论证、Limitations 整合、adversarial search 系统性
- **3 个 Minor**：读者可达性、Algorithm 1 贡献定位、venue 适配度
- **如 P0 问题解决，评分可上调至 4.0 (Conference)**

Issue tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 176

## Round 176

2 recorded events


### User

_source line 1765 · 2026-05-23T20:08:55.142315+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：

- **5 项 Strengths 全部 AGREE**（S5 附带对 Algorithm 1 贡献权重的保留意见）
- **5 项 Weaknesses 中 4 项 AGREE、1 项 REBUT**（W4 关于 linear SEM——论文附录 B.7/B.14 实际提供了比 R1 评估更充分的非线性鲁棒性证据，exposure 的 -78% 恶化是 FWL-covariate 拓扑不应做矩阵校正的预期行为，非假设失败）
- 两位 Reviewer 的核心共识集中在：缺少端到端真实案例、Conjecture 1 未证、EMNLP 读者可达性不足

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

_source line 1766 · 2026-05-23T20:09:09.292405+00:00_

审稿报告已提交完毕。

**Round 21 审稿总结**：

- **评分**：3.5 / 5 (Borderline Conference)，两位 Reviewer 独立给出一致评分
- **核心共识**（2 个 Must-Fix）：
  1. K≥3 理论贡献"已证但不实用 vs 实用但未证"——Theorem 2 对称假设偏差 33%，核心结论依赖未证 Conjecture
  2. 缺少端到端真实 NLP 因果应用——所有实验均为验证理论而非展示实际影响
- **3 个 Should-Fix**：non-differential 假设 NLP 讨论不足、proportional effects 适用性论证缺失、Linear SEM Limitations 呈现待改善
- **唯一分歧**：Algorithm 1 贡献权重（R1 认为 FWL 不变性赋予实质价值，R2 认为本质是决策树）——已缩小为定位方式问题
- **Issue Tracker** 已同步更新（`review_issues.yaml`）
- **视觉审查**：3 warnings（Figure 1 位置偏后、Figure 2 图例偏小、Table 9 跨页密集），无 critical

报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 177

## Round 177

30 recorded events


### User

_source line 1767 · 2026-05-24T01:24:26.078655+00:00_

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

_source line 1768 · 2026-05-24T01:24:31.737133+00:00_

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

_source line 1769 · 2026-05-24T01:24:31.737976+00:00_

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

_source line 1770 · 2026-05-24T01:24:43.295302+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1771 · 2026-05-24T01:24:43.345887+00:00_



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

_source line 1772 · 2026-05-24T01:24:46.160053+00:00_

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

_source line 1773 · 2026-05-24T01:24:46.763241+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1774 · 2026-05-24T01:24:46.763730+00:00_

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

_source line 1775 · 2026-05-24T01:24:46.814387+00:00_



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

_source line 1776 · 2026-05-24T01:24:51.336106+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
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
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1777 · 2026-05-24T01:24:53.245676+00:00_

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

_source line 1778 · 2026-05-24T01:24:54.703308+00:00_

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
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 1779 · 2026-05-24T01:24:54.854330+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_22/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_22/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1780 · 2026-05-24T01:24:55.608229+00:00_

-rw-r--r-- 1 ubuntu ubuntu 968396 May 23 23:21 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_22/submitted.pdf
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

_source line 1781 · 2026-05-24T01:24:55.760353+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1782 · 2026-05-24T01:24:55.811595+00:00_

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
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Section 3.2 已添加 ASV 替代讨论。"
    resolution_round: 3

  - id: R1-W3
    category: experiments
    severity: should-fix
    summary: "实证验证不完整：缺少商业 LLM"
    status: in_progress
    first_raised_round: 1
    last_seen_round: 21
    mentions:
      - roun
…[truncated 21671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1783 · 2026-05-24T01:25:00.689342+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"}]

Based on the search results, here's a comprehensive overview of the EMNLP 2026 call for papers and ARR submission guidelines:

## Key Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Important Dates

The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026. Author response and author-reviewer discussion runs July 7-13, 2026, and meta-reviews are released on July 30, 2026.

## Submission Process via ARR

Papers that have received reviews and 
…[truncated 1329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 9353
}
```

</details>

---


### Tool call

_source line 1784 · 2026-05-24T01:25:14.923808+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May formatting guidelines page limit template anonymous"
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
    "query": "ACL Rolling Review 2026 May formatting guidelines page limit template anonymous"
  }
}
```

</details>

---


### Tool call

_source line 1785 · 2026-05-24T01:25:15.928502+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "report.md",
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
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1786 · 2026-05-24T01:25:22.055814+00:00_

Web search results for query: "ACL Rolling Review 2026 May formatting guidelines page limit template anonymous"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Association for Computational Linguistics (ACL) conference - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj"},{"title":"Student Research Workshop - ACL 2026","url":"https://2026.aclweb.org/calls/student_research_workshop/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"GitHub - acl-org/acl-style-files: Official style files for papers submitted to venues of the Association for Computational Linguistics · GitHub","url":"https://github.com/acl-org/acl-style-files"}]

Based on the search results, here's information about ACL Rolling Review 2026 May formatting guidelines:

## Page Limits

For ARR submissions, the page limit is 4 pages for short papers and 8 pages for long papers, excluding the ethical conside
…[truncated 1211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7132
}
```

</details>

---


### Tool result

_source line 1787 · 2026-05-24T01:25:22.106570+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\\n\\n## 趋势\\n成功 13 / 负向 0 / 失败 1 / 共 14\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nhome-1x5090: 无 GPU 信息\\n\\n## 告警\\n- plan003_empirical_confusion_matrices: 训练失败 — unknown\\n\", \"total_chars\": 1083, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6178
}
```

</details>

---


### Tool call

_source line 1788 · 2026-05-24T01:25:51.549148+00:00_

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

_source line 1789 · 2026-05-24T01:25:51.700018+00:00_

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

_source line 1790 · 2026-05-24T01:25:55.069436+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3520
}
```

</details>

---


### Tool result

_source line 1791 · 2026-05-24T01:25:55.069858+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3369
}
```

</details>

---


### Tool call

_source line 1792 · 2026-05-24T01:26:24.867096+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 1，负责审查这篇投稿到 EMNLP 2026 (ARR Long Paper) 的论文。\n\n## 你的审查侧重：方法严谨性 + 理论/实验验证\n\n重点关注：\n1. **理论正确性**：定理、命题、引理的证明是否严格？假设是否合理且明确声明？K=2 证明 vs K≥3 猜想的边界是否清晰？\n2. **实验设计**：实验是否充分验证理论预测？模拟设置是否合理？是否有端到端验证？统计显著性是否充分？\n3. **方法论**：ASV 灵敏度框架是否 well-defined？校正方法的适用条件是否明确？Algorithm 1 的阈值是否有依据？\n4. **假设合理性**：Non-differential misclassification、线性 SEM、proportional effects 等假设在 NLP 场景中是否合理？讨论是否充分？\n5. **格式合规**：正文是否 ≤8 页？Abstract 是否 ≤200 words？是否 double-blind 匿名？\n\n## Venue 信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **类别**: Long Paper（正文 ≤8 页，参考文献不限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind，不得包含作者信息，self-reference 需用第三人称\n- **Limitations**: 必须包含，不计入页数限制\n- **截止日期**: 2026-05-25\n\n## 论文文件\n- TeX: `projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_22/submitted.pdf`\n\n请按 ACL/ARR 审稿标准完成独立审稿，输出 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。Weaknesses 要严格——像顶会最严格的审稿人一样评估。"
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
    "text": "你是 Reviewer 1，负责审查这篇投稿到 EMNLP 2026 (ARR Long Paper) 的论文。\n\n## 你的审查侧重：方法严谨性 + 理论/实验验证\n\n重点关注：\n1. **理论正确性**：定理、命题、引理的证明是否严格？假设是否合理且明确声明？K=2 证明 vs K≥3 猜想的边界是否清晰？\n2. **实验设计**：实验是否充分验证理论预测？模拟设置是否合理？是否有端到端验证？统计显著性是否充分？\n3. **方法论**：ASV 灵敏度框架是否 well-defined？校正方法的适用条件是否明确？Algorithm 1 的阈值是否有依据？\n4. **假设合理性**：Non-differential misclassification、线性 SEM、proportional effects 等假设在 NLP 场景中是否合理？讨论是否充分？\n5. **格式合规**：正文是否 ≤8 页？Abstract 是否 ≤200 words？是否 double-blind 匿名？\n\n## Venue 信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **类别**: Long Paper（正文 ≤8 页，参考文献不限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind，不得包含作者信息，self-reference 需用第三人称\n- **Limitations**: 必须包含，不计入页数限制\n- **截止日期**: 2026-05-25\n\n## 论文文件\n- TeX: `projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_22/submitted.pdf`\n\n请按 ACL/ARR 审稿标准完成独立审稿，输出 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。Weaknesses 要严格——像顶会最严格的审稿人一样评估。"
  }
}
```

</details>

---


### Tool result

_source line 1793 · 2026-05-24T01:26:34.876498+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10009
}
```

</details>

---


### Tool call

_source line 1794 · 2026-05-24T01:26:35.027433+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 2，负责审查这篇投稿到 EMNLP 2026 (ARR Long Paper) 的论文。\n\n## 你的审查侧重：新颖性 + 完整性 + 相关工作\n\n重点关注：\n1. **新颖性**：相对于 measurement error 文献（epi/econometrics）和 NLP annotation quality 文献，本文的增量贡献是否足够？声称的\"首次\"是否站得住脚？ASV 相对于 E-values 的创新度？\n2. **相关工作覆盖度**：是否遗漏重要相关工作？measurement error、causal inference with noisy labels、LLM annotation quality、sensitivity analysis 等领域的核心文献是否充分引用？\n3. **论文完整性**：Introduction 的动机是否清晰？叙事是否连贯？Contribution 与实际内容是否匹配？Limitations 是否充分？\n4. **写作质量**：论文的可读性、notation 一致性、图表质量、信息密度是否适当？对 NLP 社区读者是否友好？\n5. **Venue 适配度**：这篇偏统计/计量的论文是否适合 EMNLP？NLP 社区读者能从中获得什么？\n\n## Venue 信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **类别**: Long Paper（正文 ≤8 页，参考文献不限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind，不得包含作者信息，self-reference 需用第三人称\n- **Limitations**: 必须包含，不计入页数限制\n- **截止日期**: 2026-05-25\n\n## 论文文件\n- TeX: `projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_22/submitted.pdf`\n\n请按 ACL/ARR 审稿标准完成独立审稿，输出 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。Weaknesses 要严格——像顶会最严格的审稿人一样评估。"
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
    "text": "你是 Reviewer 2，负责审查这篇投稿到 EMNLP 2026 (ARR Long Paper) 的论文。\n\n## 你的审查侧重：新颖性 + 完整性 + 相关工作\n\n重点关注：\n1. **新颖性**：相对于 measurement error 文献（epi/econometrics）和 NLP annotation quality 文献，本文的增量贡献是否足够？声称的\"首次\"是否站得住脚？ASV 相对于 E-values 的创新度？\n2. **相关工作覆盖度**：是否遗漏重要相关工作？measurement error、causal inference with noisy labels、LLM annotation quality、sensitivity analysis 等领域的核心文献是否充分引用？\n3. **论文完整性**：Introduction 的动机是否清晰？叙事是否连贯？Contribution 与实际内容是否匹配？Limitations 是否充分？\n4. **写作质量**：论文的可读性、notation 一致性、图表质量、信息密度是否适当？对 NLP 社区读者是否友好？\n5. **Venue 适配度**：这篇偏统计/计量的论文是否适合 EMNLP？NLP 社区读者能从中获得什么？\n\n## Venue 信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **类别**: Long Paper（正文 ≤8 页，参考文献不限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind，不得包含作者信息，self-reference 需用第三人称\n- **Limitations**: 必须包含，不计入页数限制\n- **截止日期**: 2026-05-25\n\n## 论文文件\n- TeX: `projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_22/submitted.pdf`\n\n请按 ACL/ARR 审稿标准完成独立审稿，输出 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。Weaknesses 要严格——像顶会最严格的审稿人一样评估。"
  }
}
```

</details>

---


### Tool result

_source line 1795 · 2026-05-24T01:26:36.486719+00:00_

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

_source line 1796 · 2026-05-24T01:26:49.992256+00:00_

**Round 1 已启动。** 两名 Reviewer 正在独立审稿：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 理论/实验验证 | 审稿中 |
| R2 | 新颖性 + 完整性 + 相关工作 | 审稿中 |
| 视觉审查 | 排版/布局质量 | 已派发（非评分项） |
| 外部审稿 | Stanford Agentic Reviewer | 未配置，跳过 |

等待 Reviewer 返回审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 178

## Round 178

2 recorded events


### User

_source line 1797 · 2026-05-24T01:33:04.847377+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（Round 1 — Fresh Review）

**论文**: "Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction"
**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)
**审查侧重**: 新颖性 + 完整性 + 相关工作 + 写作质量 + Venue 适配度

---

## 总体评分

**Overall Assessment**: 3.5 / 5（Borderline Conference）

**一句话总结**: 扎实的系统性工作，将经典测量误差理论推广到 K≥3 多类误分类×7 种 DAG 拓扑，实用价值明确，但相对于已有文献的增量创新有限，核心 ASV 性质依赖未证明的猜想。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 理论推导正确（附录证明完整），MC 验证充分，但 Conjecture 1 未证明，非差异性误分类假设对 LLM 可能不成立 |
| Excitement | 3/5 | 问题重要且时效性强，但方法上更接近"已知理论的系统工程化"而非概念创新 |
| Overall Assessment | 3.5/5 | 实用贡献（Algorithm 1、PPI++ routing）对 NLP 社区有价值，但理论新颖性不足以稳进主会 |
| Reproducibility | 4/5 | 附录详尽，DGP 参数完整，MC 设置清晰；但代码/数据未提供 |
| Reviewer Confidence | 4/5 | 熟悉测量误差文献和因果推断方法论 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心新颖性存疑：相对于测量误差文献的增量贡献有限

- 具体位置：Section 1 (Contributions), Section 3.2, Theorems 1–2
- 问题：论文的核心贡献——将二值测量误差结果推广到 K≥3 多类误分类——在技术上是正确的，但主要依赖标准的线性代数工具（混淆矩阵乘积、FWL 分解）。误分类效应因 DAG 拓扑而异这一基本洞察在流行病学和计量经济学中已有充分讨论（Carroll et al., 2006; Brenner, 1993 已证明多值误分类可导致符号反转; Buonaccorsi, 2010 系统覆盖多种模型）。论文声称的 "first systematic analysis" (Section 1, p2) 在"K≥2 × 7 topologies × linear SEM"这个特定组合上站得住，但这更多是一个覆盖度的贡献而非方法论的创新。
- 为什么影响接收：EMNLP 主会要求 "exciting" 或有显著概念创新。作为 Findings 论文完全足够，但要进主会需要更强的新颖性论证。
- 建议修改方向：(1) 更清晰地区分本文的增量部分（K≥3 扩展）和真正新颖的部分（如 K≥3 对称结构导致的 sign reversal 是 K=2 不会出现的质变现象，p1 abstract 有提及但主文论述不充分）；(2) 强化 ASV 相对于 E-values 的差异化论证——目前 Section 3.3 说 ASV 是 "analogous to E-values" 但这恰恰削弱了新颖性；(3) 突出 topology-dependent 这一层的不可替代性。

**N2** [critical] Conjecture 1（包络单调性）未证明，但 ASV 的实用可靠性依赖于此

- 具体位置：Section 3.3 (Conjecture 1, p6), Appendix B.12 (Table 11)
- 问题：Conjecture 1 声称对于一般 K≥3、非 IV 拓扑，ASV 沿 C(δ) 近似单调。这是 ASV 作为诊断工具的核心性质——如果 ASV 不单调，practitioner 就无法通过比较 ASV 值来排序脆弱性。论文提供了大量数值验证（100,000 个矩阵、4 种对抗性结构，最大违反 ε < 0.017, Table 11），但这不是证明。对于一篇方法论论文，核心性质是猜想而非定理是一个重要的理论缺口。
- 为什么影响接收：如果读者不信任单调性，ASV 框架的可靠性就成问题。这与论文将 ASV 定位为 "practical diagnostic tool" 的目标相矛盾。
- 建议修改方向：(1) 至少证明特殊情况（如 K=3 对称矩阵的 Theorem 2 已经做到了），明确标注一般情况是 open problem；(2) 加强对 near-violation 区域的刻画——在什么条件下违反最大？(3) 讨论即使单调性近似违反，对实际 ASV ranking 决策的影响有多大（robustness analysis）。

**N3** [critical] 非差异性误分类假设在 LLM 注释场景下的现实性不足

- 具体位置：Definition 1 (p3), Appendix B.6 (stress test), Limitations (p8)
- 问题：Definition 1 假设混淆矩阵 C 不依赖于结果 Y 和协变量 Z。但 LLM 注释器的错误模式高度依赖于上下文特征：(a) 情感分类器在政治 vs. 产品文本上准确率不同；(b) stance detection 在争议性 vs. 非争议性话题上表现各异；(c) LLM 的 in-context learning 使错误模式与 prompt 中的示例相关，而示例选择可能与 Y 相关。Appendix B.6 的 stress test 确认了这一问题（sign-flip 率在 ε=0.20 时达到 13.9%），但主文几乎没有讨论这一关键假设的合理性边界。对于声称面向 "LLM-generated annotations" 的论文，这是一个严重的实践相关性问题。
- 为什么影响接收：论文的应用叙事（"When LLM-generated annotations feed into causal inference..."，abstract 第一句）与理论假设之间存在张力。如果非差异性假设在主要应用场景中不成立，论文的实用价值会大打折扣。
- 建议修改方向：(1) 在主文 Section 3.1 讨论非差异性假设在 LLM 场景中何时合理、何时不合理（给出具体的 NLP 应用例子）；(2) 将 B.6 的 stress test 关键结果移入主文或至少提供一段摘要；(3) 讨论如何从观测数据中验证或近似验证这一假设（如 Y-stratified permutation test, Appendix B.26 有提到但需更突出）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] PPI++ 校正（Contribution 3）的创新度有限，作为独立 contribution 列出不合适

- 具体位置：Section 4.5, Algorithm 1 (p35), Table 5 (Appendix B.2)
- 问题：PPI++ 校正本质上是将 Angelopoulos et al. (2023) 的框架应用于本文的拓扑识别设置。Algorithm 1 是有用的实践指南（路由逻辑），但不是方法论创新。Table 5 的校正结果表明 PPI++ 在 covariate topologies 上效果好（47.0% RMSE 降低），而 FWL-invariant topologies 上无效（0%），这是理论的直接推论，不是新发现。
- 建议：将 PPI++ 定位为 "practical application" 而非与 bias taxonomy 和 ASV 并列的 "contribution"，或者增加一些对 PPI++ 在本设置中的非平凡改进（如 topology-aware stratification 的技术细节）。

**W2** [warning] 正文信息密度过高，核心技术细节被迫推入附录

- 具体位置：整篇论文结构（8 页正文 + 27 页附录）
- 问题：正文试图在 8 页内覆盖：7 拓扑的 bias taxonomy、2 个定理、1 个猜想、ASV 框架（3 种度量）、PPI++ 校正、MC 验证、真实 LLM 验证、case study、校正指南。结果是正文读起来像一份 executive summary，关键技术洞察（如 Theorem 1 的证明思路、K≥3 sign reversal 的直觉机制、ASV 的计算流程）全部在附录中。正文与附录的 1:3.4 比例意味着 reviewer 必须阅读附录才能完整评估论文，这对审稿负担很大。
- 建议：考虑缩减覆盖范围——例如将 case study (Section 4.4) 或 correction guidance (Section 4.5) 移入附录，腾出空间将至少一个定理的证明 sketch 和 ASV 的完整计算流程放入正文。

**W3** [warning] Abstract 数字堆砌，主信息被稀释

- 具体位置：Abstract (p1)
- 问题：Abstract 中出现了大量具体数字："31% of hypotheses yield incorrect conclusions"、"60% agreement"、"F₁ range of 0.61–0.69"、"1.6% MAPE"、"4.1% to 42.1%"、"K≥3 introduces a structural possibility of sign reversal"、"ε < 0.017"、"0.006 to 0.926"、"88%"、"139%"、"83.8%"、"0.30–0.38"、"93.6%"。如此密集的数字使得读者在首次阅读时很难抓住核心信息。
- 建议：Abstract 保留 3-4 个最关键的数字，其余移入正文。核心信息应该是：(1) topology matters, (2) K≥3 qualitatively different from K=2, (3) ASV diagnoses vulnerability, (4) topology-aware correction helps。

**W4** [warning] Venue 适配度存疑：偏统计/计量的方法论论文在 EMNLP 的受众

- 具体位置：整篇论文
- 问题：论文的核心贡献是测量误差理论在多类设置下的推广，使用标准的统计/计量工具（FWL 分解、线性 SEM、混淆矩阵代数）。NLP 元素（LLM 注释、VAST/HumAID 数据集）作为应用场景出现，但不是方法论的核心。EMNLP 的读者群体主要是 NLP 研究者，他们可能：(a) 对测量误差理论的技术细节不感兴趣，(b) 更关心如何提高 LLM 注释质量而非如何在注释有错的情况下做因果推断。类似的方法论论文（如 Egami et al., 2022 TACL; Feder et al., 2022 TACL）通常发在 TACL 而非 EMNLP/ACL。
- 建议：(1) 强化 NLP 社区特有的洞察——例如 LLM 混淆矩阵的结构特征（是否接近对称？对角占优程度如何？）与传统测量误差文献假设的差异；(2) 增加更多 NLP-native 的实验（如在真实的因果 NLP pipeline 中端到端验证，Section B.19 有但只是 toy demo）。

**W5** [warning] K=2（二值）情况的处理不够精确

- 具体位置：Section 3.2, Section 1 (p1-2)
- 问题：论文反复强调 "K≥3 introduces a structural possibility of sign reversal absent in the binary case"（abstract, p1），但实际上二值非差异性误分类可以在特定条件下产生 sign reversal——当混淆矩阵的非对角元素超过 0.5 时（即分类器系统性地反转类别）。论文在 Proposition 7 (Appendix A.9, p20) 和 Table 1 footnote 中隐式承认了这一点（IV topology: "Not guaranteed (denominator instability)"），但主文的叙事给人一种 K=2 总是安全的印象。
- 建议：在 Section 3.2 明确说明 K=2 的 sign preservation 在什么条件下成立（C₁₁ > 0.5，即对角占优），并讨论这一条件在实践中是否总是满足（LLM 分类器 accuracy > 50% 通常成立，但在 fine-grained 或 adversarial 设置下可能不成立）。

---

## 小问题（不影响接收）

- **m1**: Figure 2 (p5) 的 y 轴标签 "Density" 在不同 topology 子图间量级差异很大，不便比较。建议统一或标注不同 scale。
- **m2**: Section 3.3 "We adopt the sensitivity analysis paradigm—E-values (VanderWeele and Ding, 2017), partial-R² bounds (Cinelli and Hazlett, 2020), coefficient stability (Oster, 2019)" 列了三个参照物但只详细比较了 E-values，partial-R² 和 Oster 的关系语焉不详。
- **m3**: Notation 密度较高：C, C₀, C_ij, δ, τ, β, γ, w_ij, π_k, M(·) 等符号在短短几页内大量引入。建议在正文提供一个 notation table 或将部分符号推迟到附录。
- **m4**: Section 4.4 "semi-real case study"（10 个 VAST 混淆矩阵 + 合成 DGP）的描述很简略，读者难以判断结果的可靠性。"Median improvement 93.6%" 的基线是什么？absolute RMSE 从多少降到多少？
- **m5**: Algorithm 1 (p35, Appendix) 是重要的实用贡献但被埋在附录最后一页，建议至少在正文提及其位置和核心逻辑。实际上正文 Section 4.5 确实引用了它，但 Algorithm 的完整版在附录太靠后。
- **m6**: References 中 Baumann et al. (2025) 标注为 "Preprint"，需确认是否已正式发表。

---

## 可能遗漏的相关工作

1. **Mahajan (2006)** "Identification and estimation of regression models with misclassification" — 计量经济学中多值误分类的非参数识别，与本文 K≥3 的识别条件讨论相关
2. **Hu (2008)** "Identification and estimation of nonlinear models with misclassification" — 非线性模型下的误分类处理，与本文 Appendix B.14 的扩展相关
3. **Plank (2022)** "The 'Problem' of Human Label Variation: On Ground Truth in Data, Disagreement, and Model Performance" — 虽然关注 disagreement 而非 error，但对 NLP 社区讨论注释质量的框架很重要
4. **Törnberg (2024)** "ChatGPT-4 Outperforms Experts..." — LLM 注释质量的重要实证工作
5. 论文引用了 VanderWeele and Ding (2017) 的 E-values 但未引用 **Cornfield et al. (1959)** 的开创性工作，后者是 sensitivity analysis 的源头

---

## 主要优势

- **S1**: 问题定义精准且时效性强——LLM 注释在 NLP 因果推断中越来越普遍，理解误分类的拓扑依赖性是一个真实需求
- **S2**: 理论覆盖度全面——7 种 DAG 拓扑 × K≥3 类 × 多种 DGP 参数，附录证明详尽
- **S3**: 实验验证多层次——MC simulation (100,000 矩阵) → cross-K robustness → real LLM confusion matrices (23 个) → semi-real case study (10 VAST configs)
- **S4**: Table 1 的 bias taxonomy 是一个有价值的速查工具，将复杂的拓扑依赖性压缩为可操作的信息
- **S5**: "topology-agnostic correction can harm" (PPI++ harms M-bias by 88%, IV correction amplifies by 139%) 是一个反直觉且实践重要的发现
- **S6**: Appendix B.19 的 end-to-end demo 和 B.18 的 political ad case study 展示了实际工作流

---

## 总结

这是一篇在测量误差理论框架下系统分析 LLM 多类注释误差如何影响因果推断的论文。工作量大、技术正确、实验充分。核心问题是：(1) 相对于 epi/econometrics 文献中已有的二值结果，K≥3 推广的理论新颖性有限；(2) ASV 的关键性质（单调性）是猜想而非定理；(3) 非差异性误分类假设在 LLM 注释场景下的合理性需要更充分的讨论。如果作者能更好地论证 K≥3 与 K=2 的质变差异（而非仅仅是量变），并加强 ASV 的理论基础，这篇论文有望进入 Conference 接收线。以当前形态，Findings 接收是有把握的。

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

_source line 1798 · 2026-05-24T01:33:12.547764+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 完成独立审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 179

## Round 179

2 recorded events


### User

_source line 1799 · 2026-05-24T01:33:39.658732+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论：Overall 3.5/5（Borderline Conference）**

核心判断：
- **3 个 Must-Fix**：(N1) K≥3 推广相对于已有测量误差文献的增量创新有限；(N2) Conjecture 1 未证明但 ASV 实用性依赖于此；(N3) 非差异性误分类假设对 LLM 注释器的现实性不足
- **5 个 Should-Fix**：PPI++ 创新度有限、正文信息密度过高、abstract 数字堆砌、venue 适配度存疑、K=2 叙述不够精确
- **主要优势**：问题定义精准、理论覆盖全面、实验验证多层次、Table 1 taxonomy 实用价值高、"topology-agnostic correction can harm" 是重要发现

当前形态适合 Findings 接收，若能加强 K≥3 vs K=2 的质变论证和 ASV 理论基础，有望进入主会。

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

_source line 1800 · 2026-05-24T01:33:47.157655+00:00_

收到 Reviewer 2 的报告。等待 Reviewer 1 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 180

## Round 180

6 recorded events


### User

_source line 1801 · 2026-05-24T01:35:08.936568+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告

**论文标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 论文对一个重要且尚未系统研究的问题（LLM 多分类标注误差在因果推断中的传播）提供了严格的理论框架，但核心理论贡献仅覆盖 K=2 和 K=3 对称情形，对论文标题声称的"Multi-Class"一般情形（K≥3 非对称）仅有猜想和数值支撑，加上非差异误分类和线性 SEM 两个强假设的联合约束，削弱了实际适用性。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | K=2 和 K=3 对称的证明严格，但 K≥3 一般情形（论文主要声称的覆盖范围）仅有 Conjecture 1 + 数值验证；非差异误分类假设脆弱（论文自身的压力测试 Appendix B.6 显示 ε=0.01 即导致 14/16 配置符号翻转）；多项关键结论依赖 proportional effects 假设 |
| Excitement | 3/5 | 问题重要且实际；拓扑分类法和 ASV 框架有创新；但线性 SEM + 非差异误分类的联合约束使得可直接应用于真实 NLP 因果研究的场景有限 |
| Reproducibility | 4/5 | DGP 参数、Algorithm 1 伪代码、Monte Carlo 设置详尽；附录 25 页提供了完整证明和补充实验；但未提及代码/数据开源 |
| Confidence | 4/5 | 仔细阅读全文及全部附录证明，熟悉因果推断和测量误差文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] K≥3 一般情形仅有猜想，论文标题和摘要的声称过强

- 具体位置：Title, Abstract, Section 3.2 (Theorem 1 vs Conjecture 1), Appendix A.4, A.6, A.11
- 问题：论文标题为"Multi-Class Annotation Errors"，摘要声称"We derive bias expressions for seven canonical topologies under K-class non-differential misclassification"，给读者的印象是 K≥3 的结果是已证明的。然而：
  - **Theorem 1**（envelope monotonicity）仅对 K=2 成立
  - **Theorem 2**（K=3 symmetric monotonicity）要求**对称混淆矩阵**（所有 off-diagonal 相等 C_jk = c），这在实际 LLM 中几乎不成立（论文自己的 Remark 4 承认 VAST 的 Frobenius 距离 d_rel = 0.30–0.38，远非对称）
  - **Conjecture 1**（一般 K≥3 envelope monotonicity）仅有数值支撑（100,000 Dirichlet 矩阵，最大违反 < 0.017），没有证明
- 为什么影响接收：对于一篇以"multi-class"为核心卖点的理论贡献论文，K=2 已有成熟文献（Brenner 1993, Hernán & Cole 2009），真正的增量贡献在于 K≥3 的形式化结果。该结果停留在猜想阶段，显著削弱了理论贡献的力度。
- 建议修改方向：(1) 在 Abstract 和 Section 3 中更明确区分"proved (K=2, K=3 symmetric)"和"conjectured (general K≥3)"，避免模糊表述；(2) 要么证明 Conjecture 1，要么将论文定位为"K=2 理论框架 + K≥3 数值延伸"，调整标题和 claims 的强度。

**N2** [critical] 非差异误分类假设（Definition 1）在 NLP 场景中过强且脆弱

- 具体位置：Definition 1 (Section 3.1, page 3), Appendix B.6, Appendix B.26, Limitations (page 8)
- 问题：Definition 1 假设混淆矩阵 C 与结果变量 Y 独立（P(A*|A) 不依赖 Y 和 covariates Z）。这是整个理论框架的基石。然而：
  1. **NLP 中标注误差几乎必然是差异性的**：LLM 对不同 outcome 群体的标注精度不同（例如，情感分类器对中性文本的误判率远高于极端情感文本；stance detection 对模糊立场的标注质量更差）。
  2. **论文自己的压力测试否定了该假设的鲁棒性**：Appendix B.6 显示，在 exposure 拓扑下，仅 ε=0.01 的结构性偏离即导致 14/16 K≥3 配置产生符号翻转（Section 3.1, page 3 引用）。这意味着非差异假设的微小违反就能推翻论文的核心正面结论。
  3. **Y-stratified 检验 (Appendix B.26) 统计功效不明**：论文用置换检验在 α=0.05 下拒绝了 1/12 配置，但未报告检验功效——低功效下"不拒绝"不等于"假设成立"。
- 为什么影响接收：论文声称"Five topologies provably preserve the treatment effect sign"，但这完全依赖于 Definition 1。如果非差异假设在实际 NLP 管道中不成立（这是高度可能的），则五个拓扑的符号保持保证不再适用，论文的核心实践价值大幅下降。
- 建议修改方向：(1) 在正文中明确讨论差异误分类的后果（不仅在 Limitations 中一句带过）；(2) 对差异误分类提供理论边界或敏感度分析（不限于 Appendix B.6 的单一拓扑 stress test）；(3) 报告 Y-stratified 检验的统计功效。

**N3** [critical] Proportional Effects 假设的验证存在循环论证风险

- 具体位置：Theorem 1 (page 4), Appendix B.17 (page 31), Section 8 Limitations
- 问题：Theorem 1 的符号保持对 confounding 拓扑要求 f(A) = λg(A)（proportional effects）。Appendix B.17 用 23 个真实 LLM 混淆矩阵验证该假设，报告"97.3% sign preservation"。然而：
  1. 验证使用的是**人工合成的 DGP**（而非真实观测数据），DGP 本身被设置为满足 proportional effects（"Proportional (f = λg)"条件下的结果）。这使验证部分循环：假设 proportional → 用满足 proportional 的 DGP 验证 → 得到高符号保持率。
  2. 对**非 proportional effects** 的验证显示 "sparse DGP (zero-effect categorical)" 的违反率高达 **24.2%**（Appendix B.17 最后一段），但此数据在正文中被忽略。
  3. 论文未讨论在什么实际 NLP 因果研究场景下 proportional effects 是合理的。这不是一个可以被 data-driven 验证的假设（因为需要知道真实的 treatment effects）。
- 为什么影响接收：Theorem 1 是论文最核心的形式化结果之一。如果 proportional effects 在实践中不成立，confounding 拓扑的符号保持保证不适用——而 confounding 恰恰是因果推断中最常见的拓扑。
- 建议修改方向：(1) 在正文中显著讨论 proportional effects 何时成立/何时不成立；(2) 报告 non-proportional DGP 下的完整结果（包括 24.2% 违反率），不要只放在 Appendix 末尾；(3) 提供 non-proportional 情形下的退化界（relaxed bounds）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 线性 SEM 假设限制实际适用性

- 具体位置：Section 3.1 (page 3), Appendix B.14, Limitations (page 8)
- 问题：全部偏差推导基于线性 SEM。Appendix B.14 测试了 logistic regression 下的 FWL 不变性，发现"logistic bias reduction is negligible (|mean| < 0.05%)"——但这只验证了 FWL 不变性，没有验证偏差公式本身在非线性模型下是否成立。Appendix B.7 进一步显示在 logistic regression 下，treatment-effect sign-flip rates 对所有拓扑保持为零，但 mean sign-flip rate 的测量精度 (mean ≤ 0.007%) 取决于 N=10,000 的 Monte Carlo 规模，可能掩盖了小概率但严重的违反。
- 建议：在正文中明确声明偏差公式的适用范围，并讨论在 GLM（logistic/Poisson）下偏差结构可能的定性变化。

**W2** [warning] ASV 框架的实际可操作性不足

- 具体位置：Section 3.3 (page 5), Algorithm 1 (page 35), Section 4.5
- 问题：ASV 的三个度量（magnitude, significance, sign-flip）都需要已知或可估计的混淆矩阵 C₀。在实际中，估计 C₀ 需要 gold labels。如果研究者已有足够 gold labels 来可靠估计 C₀，他们可能已有足够数据直接做因果分析，不需要 LLM 标注。论文的 bootstrap 方法（Section 3.3, "We recommend bootstrapping C₀"）进一步假设 gold labels 可用。这个"鸡生蛋"问题在论文中未被充分讨论。
- 建议：讨论 gold-label 预算的实际约束；考虑在 C₀ 部分已知或仅有 proxy 估计时 ASV 的鲁棒性。

**W3** [warning] 端到端验证不够真实

- 具体位置：Section 4.4 (page 7-8), Appendix B.19 (End-to-End Demo), Appendix B.18 (Case Study)
- 问题：
  1. Section 4.4 的"empirical validation"使用真实 LLM 混淆矩阵，但因果效应来自合成 DGP（K=3, N=10,000, Dirichlet confusion matrices）——这是 semi-synthetic 而非真实因果研究。
  2. Appendix B.19 的 "end-to-end demo" 也是合成 DGP + 真实混淆矩阵，Appendix B.20 的 VAST case study 使用 10 个生产混淆矩阵但偏差计算仍基于线性 SEM 的理论公式。
  3. Appendix B.3 的 ClinicalBERT case study 是最接近真实场景的，但仅是回顾性分析（retrospective application），没有与 ground truth 因果效应对比。
- 为什么影响评分：论文声称提供"practical implications"和"correction guidance"，但没有在真正的端到端 NLP 因果推断任务上验证这些建议是否有效。
- 建议：至少提供一个完整的端到端验证——用 LLM 标注的真实数据估计因果效应，与 gold-label 估计对比，展示 topology-aware correction 的改进。

**W4** [warning] Algorithm 1 的阈值缺乏形式化依据

- 具体位置：Algorithm 1 (page 35, Appendix B), Section 4.5 (page 8)
- 问题：Algorithm 1 中的决策阈值（如 Step 1 "C₁₄ > 0.5 → sign reversal risk"；Step 2 "RMSE_red > 40.0% → PPI++"等）看起来是从 Monte Carlo 实验中经验性地选取的，而非从理论分析推导。论文未说明这些阈值对 DGP 参数的敏感度，也未讨论阈值泛化到论文实验范围之外的 DGP 时是否仍然有效。
- 建议：明确声明阈值的经验来源；提供阈值敏感性分析。

**W5** [warning] "provably" 一词在摘要和正文中使用过度

- 具体位置：Abstract（两处 "provably"）, Section 1 contributions（多处）, Section 4.5
- 问题：摘要中 "Five topologies provably preserve the treatment effect sign" 和 "topology-blind corrections are provably futile" 给人以完全已证明的印象。然而：
  - "provably preserve" 仅对 K=2（Theorem 1）和 K=3 symmetric（Theorem 2）成立；对一般 K≥3 是 conjecture
  - 所有 "provably" 都隐含 non-differential misclassification + linear SEM + proportional effects 三个假设
- 建议：在使用 "provably" 时附加限定条件（如 "provably for K=2 under..."），或改用 "under our assumptions, five topologies preserve..."。

---

## 小问题（不影响接收）

1. **Figure 2 (page 5)** 的直方图密度较高，建议添加 median 标线辅助阅读。
2. **符号一致性**：正文中混淆矩阵有时用 C，有时用 C₀（参考矩阵），有时用 C(δ)（插值），三者的区分在首次引入时不够清晰。
3. **Remark 4 (page 18) 与正文脱节**：Remark 4 指出 VAST 混淆矩阵远非对称（d_rel = 0.30–0.38），但正文 Section 3 的叙述给人印象 Theorem 2 涵盖了 K=3 的主要情形。建议在正文中提及 Theorem 2 的对称性假设在实证中不成立这一事实。
4. **Appendix D 关于 AI 辅助的披露**：合规，但建议明确哪些证明是人工完成、哪些由 AI 辅助检查。
5. **Minor: "LLM" 术语使用**：Appendix B.3 使用 ClinicalBERT（fine-tuned BERT），Appendix B.18 使用 Egami et al. 的 classifiers——这些是 task-specific classifiers 而非严格意义的 "LLM"。建议在 Section 4 首次提及时说明 "LLM classifiers" 的定义范围。

---

## 主要优势

1. **问题重要且时机恰当**：LLM 标注在 NLP 因果推断中的使用正在快速增长（Gilardi et al. 2023, Ziems et al. 2024），但标注误差的因果后果缺乏系统研究。本文填补了这一空白。

2. **拓扑分类法（Taxonomy）是原创且有价值的贡献**：将 7 种 DAG 拓扑的偏差行为系统分类（Figure 1, Table 1），揭示了 topology-dependent vulnerability 的全景图。这是超越 Hernán & Cole (2009) 二分类框架的有意义扩展。

3. **FWL 不变性结果 (Section 4.5, Appendix B.2) 是最有实践冲击力的发现**：证明 matrix-based corrections（MLA, DSL, MC-SIMEX）对 4 个 covariate 拓扑无效——这直接挑战了"有混淆矩阵就能修正"的朴素直觉，对实践者有明确的行动指导价值。

4. **K=2 证明严格完整**：Theorem 1 + Propositions 1-6 覆盖了全部 7 个拓扑在 K=2 下的符号保持条件，附录证明（Appendix A.1–A.8）逻辑清晰，步骤完整。

5. **数值验证规模令人印象深刻**：100,000 Dirichlet 矩阵、adversarial monotonicity testing（Appendix A.11, 545,945 matrices）、cross-K robustness（Appendix B.9）、bootstrap convergence（Appendix B.8）——验证的广度和深度在同类论文中少见。

6. **Appendix 的组织和完整性**：25 页附录覆盖了从完整证明到 DGP 敏感性、非线性模型验证、differential misclassification stress test 等方方面面，显示了作者对潜在质疑的预判和回应能力。

---

## Questions to Authors

Q1. Conjecture 1 的数值支撑中，最大违反值 < 0.017（Appendix A.11）。在因果推断中，0.017 的 monotonicity 违反在实践中是否真的可以忽略？能否给出一个关于"可接受违反阈值"的理论或实践论证？

Q2. Appendix B.17 报告 non-proportional "sparse DGP" 的符号保持违反率为 24.2%。在实际 NLP 因果研究中（如 sentiment → policy outcome），treatment effects 更可能是 proportional 还是 non-proportional？能否提供来自真实研究的证据？

Q3. 如果非差异误分类假设不成立（论文自己的 stress test 显示这很容易发生），论文的框架是否提供任何退化保证（degradation guarantee）？或者是否完全失效？

Q4. ASV bootstrap（Section 3.3）需要 gold labels 来估计 C₀。在 gold-label budget 极少的情况下（如仅 50-100 samples），ASV 估计的方差和偏差如何？Appendix B.8 的 convergence analysis 使用了 N=1,500 个 gold labels，这在实际中是否现实？

Q5. Algorithm 1 中 "M ← PPI++" 的推荐前提是 gold labels 可用。如果将 PPI++ 替换为 MC-SIMEX（不需要 gold labels），correction performance 的退化幅度是多少？Table 5 给出了平均数据，但不同拓扑的退化差异如何？

---

## Missing References

1. **Kuroki & Pearl (2014)** — 论文引用了但未充分对比其 K≥3 结果与本文 Conjecture 1 的关系。
2. **Shu & Yi (2019a)** — 关于 misclassification 在 mediation analysis 中的传播，论文引用了但可以更深入对比 ASV 与其 sensitivity analysis 方法的异同。
3. 缺少对 **Lash et al. (2009/2014)** probabilistic bias analysis framework 的对比——该方法提供了一种不依赖 non-differential 假设的通用框架。
4. 缺少对 **Gustafson (2003) "Measurement Error and Misclassification in Statistics and Epidemiology"** 的引用——这是 multi-class misclassification bias 的经典教科书处理，与本文 Section 3.2 的 bias derivation 高度相关。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文 ≤8 页 | ✅ 合规 | 正文到 page 8（含 Limitations），References 从 page 9 |
| Abstract ≤200 words | ✅ 合规 | 估计约 165-175 words |
| Double-blind 匿名 | ✅ 合规 | "Anonymous ACL submission"，未发现破坏匿名的自引 |
| Limitations section | ✅ 合规 | Page 8，覆盖 non-differential 假设、linear SEM、proportional effects |
| ACL style template | ✅ 合规 | 使用 `\usepackage[review]{acl}` |
| AI 使用披露 | ✅ 合规 | Appendix D 披露使用 Claude (Anthropic) |

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

_source line 1802 · 2026-05-24T01:36:04.043428+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5/5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 核心新颖性存疑：相对于测量误差文献的增量贡献有限\n- 论文的核心贡献——将二值测量误差结果推广到 K≥3 多类误分类——在技术上是正确的，但主要依赖标准的线性代数工具（混淆矩阵乘积、FWL 分解）。误分类效应因 DAG 拓扑而异这一基本洞察在流行病学和计量经济学中已有充分讨论（Carroll et al., 2006; Brenner, 1993; Buonaccorsi, 2010）。论文声称的 \"first systematic analysis\" 在\"K≥2 × 7 topologies × linear SEM\"这个特定组合上站得住，但这更多是一个覆盖度的贡献而非方法论的创新。EMNLP 主会要求 \"exciting\" 或有显著概念创新，作为 Findings 足够但进主会需要更强的新颖性论证。\n\n**N2** [critical] Conjecture 1（包络单调性）未证明，但 ASV 的实用可靠性依赖于此\n- Conjecture 1 声称对于一般 K≥3、非 IV 拓扑，ASV 沿 C(δ) 近似单调。这是 ASV 作为诊断工具的核心性质。论文提供了大量数值验证（100,000 矩阵、4 种对抗性结构，最大违反 ε < 0.017），但这不是证明。对于方法论论文，核心性质是猜想而非定理是一个重要的理论缺口。\n\n**N3** [critical] 非差异性误分类假设在 LLM 注释场景下的现实性不足\n- Definition 1 假设 C 不依赖于 Y 和 Z。但 LLM 注释器的错误模式高度依赖上下文特征。Appendix B.6 的 stress test 确认了这一问题（sign-flip 率在 ε=0.20 时达 13.9%），但主文几乎没有讨论。对于声称面向 \"LLM-generated annotations\" 的论文，这是严重的实践相关性问题。\n\n### Should-Fix 问题\n\n**W1** PPI++ 校正（Contribution 3）创新度有限，作为独立 contribution 列出不合适\n- PPI++ 本质上是 Angelopoulos et al. (2023) 的框架应用。Algorithm 1 是实践指南但不是方法论创新。\n\n**W2** 正文信息密度过高，核心技术细节被迫推入附录\n- 8 页正文 + 27 页附录，正文与附录 1:3.4 比例，reviewer 必须阅读附录才能完整评估。\n\n**W3** Abstract 数字堆砌，主信息被稀释\n- Abstract 中出现大量具体数字，读者首次阅读时难以抓住核心信息。\n\n**W4** Venue 适配度存疑：偏统计/计量的方法论论文在 EMNLP 的受众\n- 核心贡献是测量误差理论推广，NLP 元素作为应用场景出现但不是方法论核心。类似论文（Egami et al., 2022; Feder et al., 2022）通常发在 TACL。\n\n**W5** K=2（二值）情况的处理不够精确\n- 论文反复强调 K≥3 引入 sign reversal 可能性，但二值非差异误分类在特定条件下也可产生 sign reversal（非对角元素超过 0.5 时）。主文叙事给人 K=2 总是安全的印象。\n\n### 小问题\n- m1: Figure 2 y轴标签 \"Density\" 在不同拓扑子图间量级差异大\n- m2: Section 3.3 列了三个参照物但只详细比较了 E-values\n- m3: Notation 密度高，建议 notation table\n- m4: Section 4.4 \"semi-real case study\" 描述简略\n- m5: Algorithm 1 被埋在附录最后一页\n- m6: Baumann et al. (2025) 标注为 \"Preprint\"\n\n### 可能遗漏的相关工作\n1. Mahajan (2006) — 多值误分类的非参数识别\n2. Hu (2008) — 非线性模型下的误分类处理\n3. Plank (2022) — Human Label Variation\n4. Törnberg (2024) — ChatGPT-4 Outperforms Experts\n5. Cornfield et al. (1959) — sensitivity analysis 源头\n\n### 主要优势\n- S1: 问题定义精准且时效性强\n- S2: 理论覆盖度全面\n- S3: 实验验证多层次\n- S4: Table 1 taxonomy 实用价值高\n- S5: \"topology-agnostic correction can harm\" 是反直觉且实践重要的发现\n- S6: End-to-end demo 和 case study 展示了工作流\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和主要优势 (S1-S6) 逐条给出 [AGREE] 或 [REBUT] 回应。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5/5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 核心新颖性存疑：相对于测量误差文献的增量贡献有限\n- 论文的核心贡献——将二值测量误差结果推广到 K≥3 多类误分类——在技术上是正确的，但主要依赖标准的线性代数工具（混淆矩阵乘积、FWL 分解）。误分类效应因 DAG 拓扑而异这一基本洞察在流行病学和计量经济学中已有充分讨论（Carroll et al., 2006; Brenner, 1993; Buonaccorsi, 2010）。论文声称的 \"first systematic analysis\" 在\"K≥2 × 7 topologies × linear SEM\"这个特定组合上站得住，但这更多是一个覆盖度的贡献而非方法论的创新。EMNLP 主会要求 \"exciting\" 或有显著概念创新，作为 Findings 足够但进主会需要更强的新颖性论证。\n\n**N2** [critical] Conjecture 1（包络单调性）未证明，但 ASV 的实用可靠性依赖于此\n- Conjecture 1 声称对于一般 K≥3、非 IV 拓扑，ASV 沿 C(δ) 近似单调。这是 ASV 作为诊断工具的核心性质。论文提供了大量数值验证（100,000 矩阵、4 种对抗性结构，最大违反 ε < 0.017），但这不是证明。对于方法论论文，核心性质是猜想而非定理是一个重要的理论缺口。\n\n**N3** [critical] 非差异性误分类假设在 LLM 注释场景下的现实性不足\n- Definition 1 假设 C 不依赖于 Y 和 Z。但 LLM 注释器的错误模式高度依赖上下文特征。Appendix B.6 的 stress test 确认了这一问题（sign-flip 率在 ε=0.20 时达 13.9%），但主文几乎没有讨论。对于声称面向 \"LLM-generated annotations\" 的论文，这是严重的实践相关性问题。\n\n### Should-Fix 问题\n\n**W1** PPI++ 校正（Contribution 3）创新度有限，作为独立 contribution 列出不合适\n- PPI++ 本质上是 Angelopoulos et al. (2023) 的框架应用。Algorithm 1 是实践指南但不是方法论创新。\n\n**W2** 正文信息密度过高，核心技术细节被迫推入附录\n- 8 页正文 + 27 页附录，正文与附录 1:3.4 比例，reviewer 必须阅读附录才能完整评估。\n\n**W3** Abstract 数字堆砌，主信息被稀释\n- Abstract 中出现大量具体数字，读者首次阅读时难以抓住核心信息。\n\n**W4** Venue 适配度存疑：偏统计/计量的方法论论文在 EMNLP 的受众\n- 核心贡献是测量误差理论推广，NLP 元素作为应用场景出现但不是方法论核心。类似论文（Egami et al., 2022; Feder et al., 2022）通常发在 TACL。\n\n**W5** K=2（二值）情况的处理不够精确\n- 论文反复强调 K≥3 引入 sign reversal 可能性，但二值非差异误分类在特定条件下也可产生 sign reversal（非对角元素超过 0.5 时）。主文叙事给人 K=2 总是安全的印象。\n\n### 小问题\n- m1: Figure 2 y轴标签 \"Density\" 在不同拓扑子图间量级差异大\n- m2: Section 3.3 列了三个参照物但只详细比较了 E-values\n- m3: Notation 密度高，建议 notation table\n- m4: Section 4.4 \"semi-real case study\" 描述简略\n- m5: Algorithm 1 被埋在附录最后一页\n- m6: Baumann et al. (2025) 标注为 \"Preprint\"\n\n### 可能遗漏的相关工作\n1. Mahajan (2006) — 多值误分类的非参数识别\n2. Hu (2008) — 非线性模型下的误分类处理\n3. Plank (2022) — Human Label Variation\n4. Törnberg (2024) — ChatGPT-4 Outperforms Experts\n5. Cornfield et al. (1959) — sensitivity analysis 源头\n\n### 主要优势\n- S1: 问题定义精准且时效性强\n- S2: 理论覆盖度全面\n- S3: 实验验证多层次\n- S4: Table 1 taxonomy 实用价值高\n- S5: \"topology-agnostic correction can harm\" 是反直觉且实践重要的发现\n- S6: End-to-end demo 和 case study 展示了工作流\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和主要优势 (S1-S6) 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1803 · 2026-05-24T01:36:35.115380+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31071
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-24T01:36:35.266365+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5/5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] K≥3 一般情形仅有猜想，论文标题和摘要的声称过强\n- 论文标题为\"Multi-Class Annotation Errors\"，给读者印象 K≥3 结果已证明。然而：Theorem 1 仅对 K=2；Theorem 2 要求对称混淆矩阵（VAST 的 d_rel = 0.30–0.38 远非对称）；Conjecture 1 仅有数值支撑。对于以\"multi-class\"为核心卖点的理论贡献论文，K=2 已有成熟文献，真正增量在于 K≥3 形式化结果停留在猜想阶段。\n\n**N2** [critical] 非差异误分类假设（Definition 1）在 NLP 场景中过强且脆弱\n- NLP 中标注误差几乎必然是差异性的。论文自己的 stress test（Appendix B.6）显示 ε=0.01 即导致 14/16 K≥3 配置符号翻转。Y-stratified 检验（Appendix B.26）统计功效不明。如果非差异假设不成立，五个拓扑的符号保持保证不再适用。\n\n**N3** [critical] Proportional Effects 假设的验证存在循环论证风险\n- Theorem 1 对 confounding 拓扑要求 proportional effects。Appendix B.17 用合成 DGP 验证，但 DGP 本身被设置为满足 proportional effects（循环论证）。Non-proportional \"sparse DGP\" 的违反率高达 24.2%（Appendix B.17），但正文忽略。论文未讨论实际 NLP 因果研究中 proportional effects 何时合理。\n\n### Should-Fix 问题\n\n**W1** 线性 SEM 假设限制实际适用性\n- 全部偏差推导基于线性 SEM。Appendix B.14 只验证 FWL 不变性，没验证偏差公式在非线性模型下是否成立。\n\n**W2** ASV 框架的实际可操作性不足\n- ASV 需要已知或可估计的 C₀，而估计 C₀ 需要 gold labels。存在\"鸡生蛋\"问题。\n\n**W3** 端到端验证不够真实\n- Section 4.4 使用真实混淆矩阵但因果效应来自合成 DGP。没有在真正的端到端 NLP 因果推断任务上验证。\n\n**W4** Algorithm 1 的阈值缺乏形式化依据\n- 决策阈值从 Monte Carlo 实验经验选取，未说明对 DGP 参数的敏感度。\n\n**W5** \"provably\" 一词使用过度\n- \"provably preserve\" 仅对 K=2 和 K=3 symmetric 成立，对一般 K≥3 是 conjecture。所有 \"provably\" 隐含三个强假设。\n\n### 小问题\n1. Figure 2 建议添加 median 标线\n2. C/C₀/C(δ) 三者区分首次引入时不够清晰\n3. Remark 4 与正文脱节（VAST 远非对称但正文暗示 Theorem 2 涵盖 K=3 主要情形）\n4. Appendix D AI 辅助披露建议更明确\n5. \"LLM\" 术语范围（ClinicalBERT 等非严格 LLM）\n\n### 主要优势\n1. 问题重要且时机恰当\n2. 拓扑分类法（Taxonomy）原创且有价值\n3. FWL 不变性结果最有实践冲击力\n4. K=2 证明严格完整\n5. 数值验证规模令人印象深刻\n6. Appendix 组织和完整性\n\n### Questions to Authors\nQ1. Conjecture 1 最大违反值 0.017 在因果推断中是否真的可忽略？\nQ2. Non-proportional \"sparse DGP\" 的 24.2% 违反率——实际 NLP 中 treatment effects 更可能是 proportional 还是 non-proportional？\nQ3. 如果非差异误分类不成立，框架是否提供任何退化保证？\nQ4. Gold-label budget 极少时（50-100 samples）ASV 估计的方差和偏差如何？\nQ5. 将 PPI++ 替换为 MC-SIMEX，correction performance 退化幅度和拓扑差异如何？\n\n### Missing References\n1. Kuroki & Pearl (2014) — 与 Conjecture 1 的关系\n2. Shu & Yi (2019a) — 与 ASV 的异同\n3. Lash et al. (2009/2014) — 不依赖 non-differential 假设的通用框架\n4. Gustafson (2003) — multi-class misclassification bias 经典教科书\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和主要优势 (1-6) 逐条给出 [AGREE] 或 [REBUT] 回应。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5/5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] K≥3 一般情形仅有猜想，论文标题和摘要的声称过强\n- 论文标题为\"Multi-Class Annotation Errors\"，给读者印象 K≥3 结果已证明。然而：Theorem 1 仅对 K=2；Theorem 2 要求对称混淆矩阵（VAST 的 d_rel = 0.30–0.38 远非对称）；Conjecture 1 仅有数值支撑。对于以\"multi-class\"为核心卖点的理论贡献论文，K=2 已有成熟文献，真正增量在于 K≥3 形式化结果停留在猜想阶段。\n\n**N2** [critical] 非差异误分类假设（Definition 1）在 NLP 场景中过强且脆弱\n- NLP 中标注误差几乎必然是差异性的。论文自己的 stress test（Appendix B.6）显示 ε=0.01 即导致 14/16 K≥3 配置符号翻转。Y-stratified 检验（Appendix B.26）统计功效不明。如果非差异假设不成立，五个拓扑的符号保持保证不再适用。\n\n**N3** [critical] Proportional Effects 假设的验证存在循环论证风险\n- Theorem 1 对 confounding 拓扑要求 proportional effects。Appendix B.17 用合成 DGP 验证，但 DGP 本身被设置为满足 proportional effects（循环论证）。Non-proportional \"sparse DGP\" 的违反率高达 24.2%（Appendix B.17），但正文忽略。论文未讨论实际 NLP 因果研究中 proportional effects 何时合理。\n\n### Should-Fix 问题\n\n**W1** 线性 SEM 假设限制实际适用性\n- 全部偏差推导基于线性 SEM。Appendix B.14 只验证 FWL 不变性，没验证偏差公式在非线性模型下是否成立。\n\n**W2** ASV 框架的实际可操作性不足\n- ASV 需要已知或可估计的 C₀，而估计 C₀ 需要 gold labels。存在\"鸡生蛋\"问题。\n\n**W3** 端到端验证不够真实\n- Section 4.4 使用真实混淆矩阵但因果效应来自合成 DGP。没有在真正的端到端 NLP 因果推断任务上验证。\n\n**W4** Algorithm 1 的阈值缺乏形式化依据\n- 决策阈值从 Monte Carlo 实验经验选取，未说明对 DGP 参数的敏感度。\n\n**W5** \"provably\" 一词使用过度\n- \"provably preserve\" 仅对 K=2 和 K=3 symmetric 成立，对一般 K≥3 是 conjecture。所有 \"provably\" 隐含三个强假设。\n\n### 小问题\n1. Figure 2 建议添加 median 标线\n2. C/C₀/C(δ) 三者区分首次引入时不够清晰\n3. Remark 4 与正文脱节（VAST 远非对称但正文暗示 Theorem 2 涵盖 K=3 主要情形）\n4. Appendix D AI 辅助披露建议更明确\n5. \"LLM\" 术语范围（ClinicalBERT 等非严格 LLM）\n\n### 主要优势\n1. 问题重要且时机恰当\n2. 拓扑分类法（Taxonomy）原创且有价值\n3. FWL 不变性结果最有实践冲击力\n4. K=2 证明严格完整\n5. 数值验证规模令人印象深刻\n6. Appendix 组织和完整性\n\n### Questions to Authors\nQ1. Conjecture 1 最大违反值 0.017 在因果推断中是否真的可忽略？\nQ2. Non-proportional \"sparse DGP\" 的 24.2% 违反率——实际 NLP 中 treatment effects 更可能是 proportional 还是 non-proportional？\nQ3. 如果非差异误分类不成立，框架是否提供任何退化保证？\nQ4. Gold-label budget 极少时（50-100 samples）ASV 估计的方差和偏差如何？\nQ5. 将 PPI++ 替换为 MC-SIMEX，correction performance 退化幅度和拓扑差异如何？\n\n### Missing References\n1. Kuroki & Pearl (2014) — 与 Conjecture 1 的关系\n2. Shu & Yi (2019a) — 与 ASV 的异同\n3. Lash et al. (2009/2014) — 不依赖 non-differential 假设的通用框架\n4. Gustafson (2003) — multi-class misclassification bias 经典教科书\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和主要优势 (1-6) 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-24T01:36:36.724117+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1457
}
```

</details>

---


### Assistant

_source line 1806 · 2026-05-24T01:36:39.865411+00:00_

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


## Round 181

## Round 181

2 recorded events


### User

_source line 1807 · 2026-05-24T01:36:42.514773+00:00_

[Reviewer 1 审稿结果]:
审稿完成。报告已提交至 Review Director。

**审稿核心判断：Overall 3.5 (Borderline Conference)**

三个 Must-Fix 问题：
1. **K≥3 理论缺口**：标题声称 "Multi-Class" 但形式化保证仅覆盖 K=2 和 K=3 对称，一般 K≥3 仅有 Conjecture 1
2. **非差异误分类假设脆弱**：论文自身的 stress test 显示 ε=0.01 即导致 14/16 配置符号翻转，NLP 中该假设几乎必然被违反
3. **Proportional effects 验证循环**：用满足 proportional 假设的合成 DGP 验证 proportional 假设下的定理，non-proportional 情形下 24.2% 违反率被低调处理

主要优势：问题重要、拓扑分类法原创、FWL 不变性结果有实践冲击力、K=2 证明严格完整、数值验证规模大。

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

_source line 1808 · 2026-05-24T01:36:46.251979+00:00_

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


## Round 182

## Round 182

2 recorded events


### User

_source line 1809 · 2026-05-24T01:38:31.137526+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 核心新颖性存疑**

同意 R2 的基本判断，但程度上有细微分歧。

R2 认为"误分类效应因 DAG 拓扑而异"这一洞察在 Carroll et al. (2006) 和 Brenner (1993) 中已充分讨论。这是对的——拓扑依赖性本身不新。但我认为本文仍有两个非平凡的增量贡献：

1. **FWL 不变性结果**（Section 4.5, Appendix B.2）：证明 matrix-based corrections（MLA, DSL, MC-SIMEX）对 4 个 covariate 拓扑无效——这在已有文献中未被明确指出。这不是简单的"覆盖度"扩展，而是一个有实践冲击力的负面结果。
2. **ASV 框架**（Section 3.3）：将敏感性分析从定性（"小心误分类"）推进到定量（给出 δ-threshold），这在 NLP 因果推断场景下是新的工具。

然而，R2 说得对：技术手段（线性代数、FWL 分解）是标准的。总体而言，本文是"系统性应用 + 实用工具"型贡献，不是"方法论突破"型贡献。对 Findings 足够，进主会需要 Conjecture 1 被证明或有更强的 NLP-specific insight。

**[AGREE] R2-N2: Conjecture 1 未证明削弱 ASV 可靠性**

完全同意。这与我自己的 N1 一致。补充一个 R2 没有提到的角度：

Conjecture 1 的数值验证（Appendix A.11）报告最大违反 ε < 0.017。但论文没有讨论 0.017 在因果推断实践中的含义。如果 ASV 的 monotonicity 违反了 0.017，对应的因果效应估计偏差是多少？是否影响显著性判断？缺少这个"so what"分析，单纯报告 ε < 0.017 不足以让读者判断 Conjecture 1 是否"足够好"。

此外，Appendix A.11 的 adversarial testing 使用了 4 种特定结构（near-permutation, block-diagonal, sparse, near-uniform），但这些结构是否覆盖了 adversarial worst case 并不清楚——论文没有论证为什么这 4 种结构就是最难的。

**[AGREE] R2-N3: 非差异性假设现实性不足**

完全同意。这与我自己的 N2 一致。

补充 R2 遗漏的一个关键细节：论文的 Appendix B.26 进行了 Y-stratified non-differential test，结果在 α=0.05 下仅拒绝了 1/12 配置。但论文**未报告该检验的统计功效（power）**。在小样本 Y-strata 中，置换检验的 power 可能极低，"不拒绝"不等于"假设成立"。这使得 Appendix B.26 的"验证"不具说服力。

R2 引用了 Appendix B.6 的 ε=0.20 时 sign-flip 率 13.9%。我在自己的审稿中注意到了更极端的数据：ε=0.01（极小的非差异性偏离）就导致 14/16 K≥3 exposure 配置产生符号翻转（Section 3.1, page 3 引用）。这比 R2 引用的数据更令人担忧。

---

### Should-Fix 问题

**[REBUT] R2-W1: PPI++ 作为独立 contribution 不合适**

R2 认为 PPI++ 仅是 Angelopoulos et al. (2023) 的应用。我认为这低估了本文在 correction 方面的贡献。

1. **本文的真正 correction 贡献不是 PPI++ 本身，而是"何时不该校正"**：FWL 不变性结果（Section 4.5, Appendix B.2）证明了 4/7 拓扑下 matrix-based corrections 完全无效。这个负面结果比"用 PPI++ 校正"更有价值——它告诉实践者**不要浪费精力在无效的校正上**。
2. **Algorithm 1 虽然是实践指南，但整合了论文的全部理论结果**（topology identification → risk assessment → method selection → FWL check）。这种端到端的决策流程在已有文献中不存在。
3. 我同意 Algorithm 1 的阈值缺乏形式化依据（我自己的 W4），但这不等于它作为 contribution 不合适——它是理论到实践的桥梁。

综上，我认为 Contribution 3 的措辞可以调整（从"PPI++ correction"改为"topology-aware correction guidance including FWL futility result"），但将其完全降级为"仅仅是应用"不公平。

**[AGREE] R2-W2: 正文信息密度过高**

同意。8 页正文试图覆盖 bias derivation + ASV framework + 3 theorems + correction guidance + empirical validation + case study，确实过度压缩。Reviewer 必须阅读 Appendix A 才能评估 Theorem 1 的证明正确性，阅读 Appendix B.2 才能理解 FWL invariance 结果的细节。

不过，我注意到这在 *ACL 长文中是常见现象——8 页限制本身就导致理论论文向附录转移内容。这不应成为 reject 的独立理由，但确实影响了审稿体验。建议作者在正文中加入更清晰的附录导航（如"Appendix A provides all proofs; Appendix B.1-B.7 cover robustness checks"）。

**[REBUT] R2-W3: Abstract 数字堆砌**

部分不同意。Abstract 中的具体数字（如"61% to <1%"、"five topologies"、"four topologies"）恰恰让 claims 可验证和具体。对比一个只有定性描述的 abstract（"we show significant bias reduction"），具体数字更符合 *ACL 的写作规范。

但 R2 有一定道理：某些数字可以精简（如不需要同时出现"five topologies preserve"和"exposure and IV can reverse"——后者已经隐含了前者）。主信息应更突出。

**[REBUT] R2-W4: Venue 适配度存疑**

不同意。本文的 venue 适配性是充分的：

1. **NLP 动机是核心而非装饰**：论文研究的是 LLM 标注误差（NLP 特有问题），验证用的是 NLP 数据集（HumAID, VAST, CivilComments），case study 来自 NLP 因果推断文献（Egami et al. 2023 政治广告、Lee & Wood-Doughty 2024 patient smoking）。
2. **先例充分**：Keith et al. (2020) "Text and Causal Inference" 发表在 ACL 2020；Feder et al. (2022) "Causal Inference in NLP" 发表在 TACL 但被 R2 自己引用为同类工作；Egami et al. (2022) 是 TACL。这些论文的方法论核心同样来自统计学/计量经济学，但因为 NLP 应用场景而被 *ACL 社区接受。
3. **EMNLP 的 Findings track 明确接受方法论应用论文**。

R2 建议 TACL 可能更合适——这是合理的建议，但不构成 EMNLP 的拒稿理由。

**[AGREE] R2-W5: K=2 叙事过于简化**

同意。这是一个我自己审稿时没有充分强调的技术细节。

论文 Abstract 声称"K≥3 introduces a structural possibility of sign reversal absent in the binary case"。但严格来说：
- **K=2 exposure topology 也能产生 sign reversal**——当对角线元素 < 0.5（accuracy < 50%）时。Proposition 1(c) 实际上暗示了这一点（C₁₄ > 0.5 是符号保持的条件），但正文叙事给人的印象是 K=2 总是安全的。
- 论文真正想说的是：**对 confounding 拓扑**，K=2 下 non-differential misclassification 保证 attenuation（经典 Brenner 1993 结果），而 K≥3 打破了这个保证。但 "absent in the binary case" 这个表述没有限定到 confounding，造成了过度概括。

建议作者修改为"K≥3 introduces sign reversal possibilities for confounding and mediation topologies where K=2 guarantees attenuation"或类似限定表述。

---

### 小问题

**[AGREE] m1**: Figure 2 各拓扑 y 轴量级差异大，影响跨拓扑比较。合理建议。

**[AGREE] m2**: Section 3.3 提到与 E-values 等的比较，但未展开，内容不对称。

**[AGREE] m3**: Notation 密度高。Notation table 对读者友好，尤其是 C, C₀, C(δ), A, A* 等符号需要集中定义。

**[AGREE] m4**: Section 4.4 "semi-real case study" 确实过于简略，关键细节在 Appendix B.18-B.20，正文应至少提供更多上下文。

**[AGREE] m5**: Algorithm 1 在 Appendix 最后一页（page 35）。考虑到它是论文声称的 Contribution 3 的核心，这个位置不合理。至少应在正文中给出简化版本或决策树。

**[REBUT] m6**: Baumann et al. (2025) 标注为 "Preprint" 是合理的引用实践——论文使用了该工作的结果但该工作尚未经同行评审，标注"Preprint"是透明度体现而非缺陷。*ACL 格式允许引用 arXiv preprints。

---

### 可能遗漏的相关工作

**[AGREE]** Mahajan (2006) — 多值误分类的非参数识别，与本文 K≥3 的 identifiability 讨论直接相关。确实缺失。

**[AGREE]** Hu (2008) — 非线性模型误分类，与 Appendix B.14 (logistic regression) 的讨论相关。

**[REBUT]** Plank (2022) Human Label Variation — 该工作关注标注者间分歧和 label variation 的建模，与本文关注的"标注误差对因果估计的传播"是不同问题。引用会有价值但不构成"遗漏"。

**[AGREE]** Törnberg (2024) ChatGPT-4 — 作为 LLM 标注质量的实证参考，在 Section 1 motivation 中引用是恰当的。Gilardi et al. (2023) 已被引用但 Törnberg 提供了不同角度。

**[AGREE]** Cornfield et al. (1959) — sensitivity analysis 的奠基性工作，考虑到 ASV 框架的 sensitivity analysis 性质，引用该工作是应当的。论文引用了 E-values (VanderWeele & Ding 2017) 但缺少这个更早的源头。

补充一个 R2 也没提到但我认为重要的遗漏：**Gustafson (2003) "Measurement Error and Misclassification in Statistics and Epidemiology"** — 该教科书对 multi-class misclassification bias 有系统处理，与本文 Section 3.2 的 bias derivation 高度相关。

---

### 主要优势

**[AGREE] S1**: 问题定义精准且时效性强。同意。LLM 标注在 NLP 因果推断中的使用正快速增长，本文填补了"标注误差 → 因果估计偏差"的系统分析空白。

**[AGREE] S2**: 理论覆盖度全面。同意，但附加一个 caveat：覆盖度仅在"K=2 证明 + K≥3 猜想/数值"意义上全面。如果只看已证明的结果，覆盖度是 K=2 的 7 拓扑 + K=3 对称的 3 拓扑。

**[AGREE] S3**: 实验验证多层次。同意。100,000 Dirichlet 矩阵 + adversarial testing + 23 真实 LLM 配置 + bootstrap convergence + cross-K robustness 的验证层次确实在同类论文中少见。

**[AGREE] S4**: Table 1 taxonomy 实用价值高。强烈同意。这是论文最直接可用的产出——实践者可以根据自己的 DAG 拓扑快速判断误分类风险等级。

**[AGREE] S5**: "topology-agnostic correction can harm" 是反直觉且重要的发现。强烈同意。这是我自己审稿中识别的论文最强优势。FWL invariance 意味着对 4 个 covariate 拓扑，无论混淆矩阵多精确，plug-in/MLA 校正的 RMSE reduction 都是 0%。这直接挑战了"有混淆矩阵就能修正"的朴素直觉。

**[AGREE] S6**: End-to-end demo 展示了工作流。部分同意。Demo 确实展示了从 topology identification 到 correction 的完整流程（Appendix B.19, Table 19）。但如我自己审稿 W3 所述，这是 semi-synthetic（合成 DGP + 真实混淆矩阵），不是真正的端到端实证验证。

---

### 综合评估

R2 的审稿与我的评估高度一致：Overall 3.5, 核心关切集中在 K≥3 猜想未证明、非差异假设脆弱、novelty 是"覆盖度"而非"方法论突破"。

两处分歧：
1. **PPI++ 贡献度** (W1)：R2 将其降级为"仅应用"，我认为 FWL 负面结果 + topology-aware decision procedure 构成了超越单纯应用的贡献。
2. **Venue 适配** (W4)：R2 认为偏统计/计量论文不适合 EMNLP，我认为 NLP 动机和验证场景使其适配 EMNLP Findings。

总体而言，R2 的审稿质量高，技术判断准确，建议合理。

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

_source line 1810 · 2026-05-24T01:38:47.071903+00:00_

收到 Reviewer 1 对 Reviewer 2 的交叉回应。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 183

## Round 183

2 recorded events


### User

_source line 1811 · 2026-05-24T01:38:49.659522+00:00_

[Reviewer 1 审稿结果]:
对 Reviewer 2 全部意见的逐条回应已提交给 Review Director。

总结：在 N1-N3 三个 Must-Fix 上全部 [AGREE]（与我自己的审稿高度一致），在 Should-Fix 上有两处 [REBUT]（W1 PPI++ 贡献度被低估、W4 venue 适配性充分），W3 部分反驳，W2/W5 同意。小问题中 m6 反驳（preprint 标注合规），其余同意。

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

_source line 1812 · 2026-05-24T01:38:53.781436+00:00_

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


## Round 184

## Round 184

16 recorded events


### User

_source line 1813 · 2026-05-24T01:41:09.666868+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R1-N1: "Theorem 1 仅对 K=2" — 事实性判断有误，但 broader concern 部分成立**

R1 称 "Theorem 1 仅对 K=2"，这一表述需要澄清。Theorem 1（p6）确实标题为 "Envelope monotonicity — K=2"，但这说的是 *单调性* 结果限于 K=2。论文中关于 *符号保持*（sign preservation）的结果——Proposition 1（p5, Appendix A.4–A.5）和 Proposition 2（p13, Appendix A.3）——明确覆盖一般 K，条件是 proportional effects 和 C_A > 0（对角占优）。因此 "K≥3 形式化结果停留在猜想阶段" 过于笼统：K≥3 的符号保持已被证明（under proportional effects），未证明的是 *包络单调性*（Conjecture 1）。

不过，R1 的核心关切——论文标题和 abstract 给人 K≥3 结果已全面证明的印象——我部分同意。Abstract 说 "Five topologies provably preserve the treatment effect sign"，这对 K≥3 在 proportional effects 下是成立的（Proposition 1），但 "provably" 的隐含条件（proportional effects）在 abstract 中没有提及。建议作者在 abstract 加入限定词或脚注。

**[AGREE] R1-N2: 非差异性误分类假设在 NLP 场景中过强**

同意方向，与我的 R2-N3 一致。LLM 注释器的错误模式确实高度上下文依赖，非差异性假设在 NLP 中是一个值得质疑的简化。

但 R1 引用的具体数据有误：R1 称 "ε=0.01 即导致 14/16 K≥3 配置符号翻转"。查阅 Table 9（p26, Appendix B.6），在 ε=0.01 时，confounding K=3 的 sign-flip 率全部为 0.00，mediation K=3 也是 0.00，exposure K=3 的 SF 也接近 0。只有 IV 在基线（ε=0）就有较高的 sign-flip。"14/16 配置" 这个数字我在 Table 8 和 Table 9 中均无法对应找到。Table 8（p25）在 ε=0.01 时 exposure 的 sign-flip 仅 2.0%，与 ε=0.00 相同。R1 可能混淆了 "any violation"（包含 amplification）和 "sign flip"，或者误读了表格数据。

这不影响 R1-N2 的核心论点——非差异性假设确实是论文最大的实践性弱点——但具体证据需要修正。

**[REBUT] R1-N3: "循环论证" 定性过重，但实践相关性讨论确实缺失**

R1 称 Appendix B.17 的验证是"循环论证"，因为 DGP 本身满足 proportional effects。这个批评不太公平：验证定理在其假设条件下成立（in-assumption verification）不是循环论证，而是标准的正确性检查。循环论证是指用结论来证明前提，但这里的逻辑是：定理说"如果 proportional effects 成立，则 sign preservation 成立"→ 用满足 proportional effects 的 DGP 验证 → 确认定理成立。这是标准的数值验证流程。

真正重要的是 *out-of-assumption* 测试：论文确实报告了 non-proportional sparse DGP 的 24.2% 违反率（Table 16, p31），以及 non-proportional effects 下 sign preservation 从 97.8% 降到 75.8%。这说明论文并没有回避假设失效的后果。

我同意 R1 的一个子关切：论文缺少对"实际 NLP 因果研究中 proportional effects 何时合理"的讨论。这是一个有价值的改进方向——例如，当 treatment 对所有 outcome categories 的效应方向一致时（如正面情感分类器的所有误判都倾向于同一方向），proportional effects 更可能成立。论文应在 Limitations 或 Section 3.2 加入这一讨论。

---

### Should-Fix 问题

**[AGREE] R1-W1: 线性 SEM 假设限制实际适用性**

同意。Appendix B.14 的 FWL 不变性验证仅扩展到 logistic regression（bias < 0.05% across topologies），但 NLP 中的因果模型越来越多使用非参数方法（matching, doubly-robust estimators, deep learning）。偏差公式在这些模型下是否成立是一个开放问题。这与我的 R2-W4（venue 适配度）相关——NLP 读者更关心的是他们实际使用的模型，而非线性 SEM。

**[AGREE] R1-W2: ASV 的 "鸡生蛋" 问题**

部分同意。ASV 需要估计 C₀（参考混淆矩阵），而估计 C₀ 需要 gold labels。这确实是一个实践障碍。但我认为这个问题没有 R1 暗示的那么严重：(a) PPI++ 校正本身也需要 gold labels，所以 ASV 和 correction 在同一个 gold-label budget 内操作；(b) Appendix B.8 的 bootstrap 收敛分析表明 ~500 个 gold labels 即可获得稳定的 ASV 估计（95% CI width < 0.2）。真正的 gap 是论文没有讨论 gold-label budget 极少时（R1-Q4 的 50-100 samples）的 ASV reliability。

**[AGREE] R1-W3: 端到端验证不够真实**

同意，与我的 R2-W2（信息密度）间接相关。Section 4.4 的 "semi-real case study" 使用真实 VAST 混淆矩阵但合成 DGP，Appendix B.18 的 political ad case study 和 B.19 的 end-to-end demo 也是构造的因果问题。论文缺少一个从头到尾使用真实数据（真实注释、真实因果问题、真实 outcome）的验证。这在当前形态下是可以理解的（获取同时有 gold labels 和已知因果效应的真实数据很困难），但应作为 limitation 明确说明。

**[AGREE] R1-W4: Algorithm 1 阈值缺乏形式化依据**

同意。Algorithm 1（p35）的决策阈值（如 ASV 的 risk level 分界点、PPI++ vs. MC-SIMEX 选择条件）来自 Monte Carlo 经验而非理论推导。论文在 Appendix B.10（ASV Diagnostic Results）和 B.11（ASV Stability Across DGPs）中展示了阈值的稳定性，但没有正式讨论阈值对 DGP 参数变化的敏感度。对于声称提供 "correction decision procedure" 的论文，阈值的鲁棒性论证应更充分。

**[REBUT] R1-W5: "provably" 使用——部分合理但需区分**

R1 称 "'provably' 仅对 K=2 和 K=3 symmetric 成立"。这不完全准确。论文中 "provably preserve" 的用法（p2, p8）对应的是 Proposition 1（p5），该命题覆盖一般 K 下的 sign preservation（under proportional effects + C_A > 0）。对于 confounding、mediation、collider、M-bias、front-door 五种拓扑，sign preservation 在这些条件下确实是 "provably" 的。Conjecture 1 是关于 *单调性*（monotonicity），不是 sign preservation。

不过，R1 有一个有效的子观点："provably" 的使用隐含了三个假设（non-differential, proportional effects, C_A > 0），而这些假设在正文 narrative 中不总是被提及。建议作者在使用 "provably" 时附注条件，或将 "provably" 替换为 "under [assumptions], we prove that..."。

---

### 小问题

1. **[AGREE]** Figure 2 添加 median 标线——合理建议，提升可读性。
2. **[AGREE]** C/C₀/C(δ) 区分不够清晰——同意，我在 R2-m3 也提到了 notation 密度问题。
3. **[AGREE]** Remark 4 与正文脱节——好观察。Theorem 2 要求对称 C，但 VAST 的 d_rel = 0.30–0.38 远非对称。论文应更明确地说明 Theorem 2 的实际适用范围。
4. **[AGREE]** Appendix D AI 辅助披露——minor，但应更具体。
5. **[AGREE]** "LLM" 术语范围——ClinicalBERT 不是严格意义上的 LLM。论文应使用 "text classifiers" 或 "NLP classifiers" 作为上位概念，将 "LLM" 限于真正的大模型。

---

### 主要优势

1. **[AGREE]** 问题重要且时机恰当——与我的 R2-S1 一致。
2. **[AGREE]** 拓扑分类法原创且有价值——Table 1 是论文最有impact的单一贡献，与我的 R2-S4 一致。
3. **[AGREE]** FWL 不变性结果最有实践冲击力——同意。这可能是论文对 NLP 社区最重要的实用信息：对于 covariate topologies（confounding, mediation, collider, M-bias），矩阵校正无效，FWL 已经吸收了误分类偏差。这反直觉且重要。
4. **[AGREE]** K=2 证明严格完整——同意，Theorems 1-2 和 Propositions 1-6 的证明详尽。
5. **[AGREE]** 数值验证规模令人印象深刻——100,000 矩阵、545,945 adversarial 矩阵、23 empirical LLM 矩阵。
6. **[AGREE]** Appendix 组织和完整性——同意，27 页附录虽然量大但组织有序（B.1-B.25 编号清晰）。

---

### R1 Questions 评价

- **Q1**（Conjecture 1 的 0.017 违反是否可忽略）：好问题。在因果推断中，如果真实效应本身很小（如 τ ≈ 0.05），0.017 的单调性违反可能导致 ASV ranking 翻转。论文应讨论 violation 与效应量的相对大小。
- **Q2**（NLP 中 proportional vs non-proportional）：非常好的问题。这是 R1-N3 的核心延伸——如果 NLP 中的 treatment effects 通常是 non-proportional（不同类别受影响程度不同），那么 24.2% 的违反率是一个严重问题。
- **Q3**（非差异假设不成立时的退化保证）：关键问题。论文目前没有提供退化保证。
- **Q4**（50-100 gold labels 时 ASV 估计质量）：实践相关，论文的 bootstrap 分析起步于 N*=6,000（Appendix B.8），远高于 50-100。
- **Q5**（MC-SIMEX vs PPI++ 替换）：有价值的对比，Table 21（p32）部分回答了这个问题——MC-SIMEX 在 IV topology 上是最佳方法，但其他拓扑上 PPI++ 更优。

---

### R1 Missing References — 全部已引

**[REBUT] 全部四条 "missing references" 均已在论文中引用：**

1. **Kuroki & Pearl (2014)**: 已引用——p10 references: "Masatoshi Kuroki and Judea Pearl. 2014. Measurement bias and effect estimation in causal inference. Biometrika, 101(2):423–437."
2. **Shu & Yi (2019a)**: 已引用——p11 references: "Di Shu and Grace Y. Yi. 2019a. Causal inference with measurement error in outcomes..." 以及 p5 正文 "misclassified outcomes under IPW (Shu and Yi, 2019a,b)"
3. **Lash et al. (2009)**: 已引用——p10 references: "Timothy L. Lash, Matthew P. Fox, and Aliza K. Fink. 2009. Applying Quantitative Bias Analysis."
4. **Gustafson (2003/2004)**: 已引用——p10 references: "Paul Gustafson. 2004. Measurement Error and Misclassification in Statistics and Epidemiology."

R1 可能在快速检索时遗漏了这些引用。建议 R1 重新核实。

---

### 总结

R1 的审查整体质量高，对 proportional effects 假设的质疑（N3 的核心关切）和 ASV 可操作性（W2）是有价值的洞察。但存在三个事实性问题需要修正：(1) Theorem 1 的适用范围不仅限 K=2，Proposition 1 覆盖一般 K 的 sign preservation; (2) ε=0.01 导致 14/16 配置 sign flip 的具体数据不被 Table 8-9 支持; (3) 四个 "missing references" 全部已引。

我与 R1 在总体评分上一致（3.5, Borderline Conference），且在核心关切上有重叠：Conjecture 1 未证明、非差异假设过强、实践验证不足。主要分歧在于对新颖性的判断——我认为 R1 低估了 Table 1 taxonomy 和 FWL invariance 结果的实用价值。

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

_source line 1814 · 2026-05-24T01:41:38.649853+00:00_

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

_source line 1815 · 2026-05-24T01:41:38.750734+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T01:25:54.830431+00:00\", \"completed_at\": \"2026-05-24T01:30:55.008371+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent timed out after 300s\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1816 · 2026-05-24T01:41:38.751023+00:00_

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

_source line 1817 · 2026-05-24T01:41:38.901793+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1818 · 2026-05-24T01:41:45.183058+00:00_

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

_source line 1819 · 2026-05-24T01:41:46.087648+00:00_

1	\begin{abstract}
2	When LLM-generated annotations feed into causal inference, annotation quality is the wrong thing to worry about---the causal DAG topology determines whether errors attenuate, amplify, or reverse the treatment effect estimate. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification in linear structural equation models and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. Five topologies provably preserve the treatment effect sign; exposure and IV can reverse it. Under empirical LLM confusion matrices, sign reversal is confined to exposure topology. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$, $K{=}3$ symmetric) and extensively validated (general $K{\geq}3$) monotonicity, yielding a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. A case study with 10 production LLM confusion matrices confirms: topology-aware correction reduces exposure bias from 61\% to $<$1\%, while topology-blind corrections are provably futile for four topologies.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1820 · 2026-05-24T01:41:46.238738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 1821 · 2026-05-24T01:41:46.239248+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors (equivalently, misclassification) from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference. Standard classification metrics do not capture this risk: within an $F_1$ range of 0.61--0.69 across three frontier LLMs, causal bias varies by an order of magnitude across topologies.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ expo
…[truncated 3450 chars]

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

_source line 1822 · 2026-05-24T01:41:46.290285+00:00_

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

_source line 1823 · 2026-05-24T01:41:46.391446+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: at $K{\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs yield a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four covariate topologies (FWL invariance). The practical implication is direct: identify the topology first---for four topologies, no matrix-based correction helps; for exposure, PPI++ with gold labels reduces bias by 93.6\%.
5	
6	\section*{Limitations}
7	
8	We assume non-differential misclassification (Appendix~\ref{sec:nondiff_stress}). Closed-form results (Theorems~1--2) assume linear SEMs with proportional effects ($f{=}\lambda g$); FWL invariance extends to logistic models for covariate topologies (Appendix~\ref{app:fwl_proof}), but for exposure, logistic specification can increase bias (Appendix~\ref{sec:fwl_nonlinear}), and practitioners should verify linearity assumptions. Sign preservation holds at 97.3\% under non-proportional effects (Table~\ref{tab:proportional_empirical}). Proving general $K{\geq}3$ envelope monotonicity beyond symmetric matrices remains open~\cite{schennach2020mismeasured}.
9	

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

_source line 1824 · 2026-05-24T01:45:05.547347+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 22\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。Limitations 已覆盖。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续多轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 22\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出，R18 修复充分。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 再提，要求主文前置讨论。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 SF-1: 主文讨论不足，要求 NLP task mapping。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 再次升级为 critical。两位 Reviewer 强共识：NLP 中标注误差几乎必然是差异性的；B.6 stress test 显示假设脆弱；Y-stratified test 功效不明。要求主文充分讨论假设合理性边界+差异误分类下的退化保证。\"\n    action_items:\n      - round: 20\n        action: \"W6 fix: Section 3.1 expanded non-differential discussion\"\n        assigned_to: paper_agent\n        status: done\n      - round: 21\n        action: \"SF-1 fix: NLP task mapping added\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 19\n    resolution: \"R18 压缩后编译验证 main text ≤8 pages。连续多轮无复发。\"\n    resolution_round: 19\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: minor\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-W3 再提：Abstract 中 10+ 具体数字稀释主信息。R1 部分反驳（具体数字符合 *ACL 规范），共识降为 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: must-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据——缺少端到端因果应用验证\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 升级为 critical。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 MF-2: 仍为 must-fix。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方 AGREE：Section 4.4 使用真实混淆矩阵但合成 DGP，Appendix B.19/B.20 也是构造的因果问题。缺少从头到尾使用真实数据的验证。R2 承认获取同时有 gold labels 和已知因果效应的真实数据很困难。降级为 should-fix（可理解的局限）。\"\n    action_items:\n      - round: 21\n        action: \"MF-2 fix: Semi-real case study with 10 VAST K=3 production LLM confusion matrices\"\n        assigned_to: agent + paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W5 再提 ASV 与 E-values 区分度。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-N1 合并讨论：ASV 'analogous to E-values' 的措辞削弱新颖性。R1 认为 ASV 将敏感性分析从定性推进到定量是新工具。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: must-fix\n    summary: \"Proportional effects 假设在 NLP 中是强限制，且 Limitations 中完全缺失\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 升级为 critical。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 SF-2: NLP 适用性缺少实质论证。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 R1-N3: proportional effects 验证用满足假设的 DGP，non-proportional sparse DGP 违反率 24.2% 被正文忽略。R2 rebut '循环论证'定性（in-assumption verification 是标准做法），但同意缺少 NLP 中何时合理的讨论。共识：不是循环论证，但实践讨论严重缺失。\"\n    action_items:\n      - round: 21\n        action: \"SF-2 fix: NLP domain-specific argument added\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem/Conjecture 边界在主文中模糊\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 再提。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 MF-1: 结构性矛盾。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方强共识 critical：(1) Theorem 1 仅 K=2 单调性；(2) Theorem 2 K=3 对称但 VAST d_rel=0.30-0.38 远非对称；(3) Conjecture 1 仅数值支撑。ASV 核心性质是猜想而非定理，削弱作为诊断工具的可靠性。R2 补充：adversarial 4 种结构是否覆盖 worst case 不清楚；0.017 违反对因果估计的实际影响未讨论。\"\n    action_items:\n      - round: 21\n        action: \"MF-1 fix: Main text Theorem 2 repositioned as theoretical anchor\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R1]\n        note: \"与 R6-M3 合并。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。R22 继续活跃。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-N1 合并：ASV 新颖性有限。R1 部分同意但认为定量化是增量贡献。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 19\n    resolution: \"随 NEW-1 一同解决。\"\n    resolution_round: 19\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 18\n    resolution: \"连续五轮未被提出，视为已解决。\"\n    resolution_round: 18\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W2 再提。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 SF-3。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方 AGREE：偏差公式在非线性模型（matching, doubly-robust, deep learning）下是否成立是开放问题。NLP 读者更关心实际使用的模型。\"\n    action_items:\n      - round: 21\n        action: \"SF-3 fix: Limitations references B.7 and B.14\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W3 再提。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-N1: 'first systematic analysis' 在特定组合上站得住但更多是覆盖度贡献。R1 AGREE 但认为 FWL+ASV 超越单纯覆盖度。\"\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续多轮未提出。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: minor\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 MI-1: Existing footnote covers。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方 AGREE notation 密度高。R2-m3 建议 notation table。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 R1-minor-1 + R2-m1：y轴量级差异大，建议统一 scale 或加 median 标线。\"\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续四轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续五轮未提出。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续三轮未提出。\"\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续三轮未提出。\"\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R2]\n        note: \"R21 MI-2: R1 rebut（FWL invariance 赋予价值）。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 分歧：R2-W1 认为 PPI++ 作为独立 contribution 不合适；R1 rebut（FWL 负面结果+topology-aware decision procedure 超越单纯应用）。R1 建议调整措辞为 'topology-aware correction guidance including FWL futility result'。\"\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续四轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续五轮未提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续三轮未提出。\"\n\n  - id: R20-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中很少成立——缺少合理性讨论和经验量化\"\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 MF-1 合并。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 与 R8-C1 合并。R1-minor-3: Remark 4 与正文脱节（VAST d_rel=0.30-0.38 远非对称，但正文暗示 Theorem 2 涵盖 K=3 主要情形）。双方 AGREE。\"\n\n  - id: R20-N2\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 决策阈值缺乏理论依据和跨设置稳定性验证\"\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 Q4: 已 addressed。MI-2 分歧。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方 AGREE：阈值从 MC 经验选取，缺乏形式化依据和对 DGP 参数变化的敏感度讨论。\"\n\n  - id: R21-SF4\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 adversarial search 4 种结构族基于直觉选择，系统性不明\"\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 SF-4: 低优先级。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-N2 合并：adversarial 4 种结构是否覆盖 worst case 不清楚。\"\n\n  - id: R21-MI3\n    category: scope\n    severity: minor\n    summary: \"Venue 适配度处于边界——核心贡献在统计/计量层面\"\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R2]\n        note: \"R2-W6: ARR 允许跨学科。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 分歧：R2-W4 认为偏统计/计量；R1 REBUT（NLP 动机核心、先例充分、Findings 明确接受）。共识：不构成拒稿理由。\"\n\n  - id: R21-Q2\n    category: method\n    severity: should-fix\n    summary: \"DAG 不确定时实践者应如何使用框架——缺少 worst-case guidance\"\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。\"\n\n  # === Round 22 新发现 ===\n\n  - id: R22-N1\n    category: novelty\n    severity: must-fix\n    summary: \"相对于测量误差文献（Carroll 2006, Brenner 1993, Buonaccorsi 2010）的增量创新有限——'系统性覆盖'而非'方法论突破'\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"双方 AGREE：技术手段标准（线性代数、FWL 分解），K≥3 推广更多是覆盖度贡献。R1 补充 FWL invariance 和 ASV 定量化是非平凡增量。共识：Findings 足够，进主会需要更强论证。\"\n\n  - id: R22-W1\n    category: soundness\n    severity: should-fix\n    summary: \"ASV 需要 gold labels 估计 C₀ 存在 '鸡生蛋' 问题——gold-label budget 极少时 ASV 可靠性未讨论\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R1-W2 提出，R2 部分 AGREE：PPI++ 也需要 gold labels 所以在同一 budget 内；B.8 bootstrap 收敛需 ~500 gold labels。但 50-100 samples 时的 ASV reliability 未讨论。\"\n\n  - id: R22-W2\n    category: presentation\n    severity: should-fix\n    summary: \"'provably' 在 abstract/正文中使用隐含三个强假设（non-differential + proportional effects + C_A > 0），应附加限定条件\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R1-W5 提出，R2 部分 REBUT：sign preservation（Proposition 1）覆盖一般 K，'provably' 技术上成立。但 R2 同意隐含条件应在 narrative 中提及。共识：建议将 'provably' 附注条件或改为 'under [assumptions], we prove that...'。\"\n\n  - id: R22-W3\n    category: presentation\n    severity: should-fix\n    summary: \"K=2 sign preservation 叙事过于简化——exposure topology 在对角元素 <0.5 时也可 sign reversal\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R2-W5 提出，R1 AGREE：'absent in the binary case' 未限定到 confounding，造成过度概括。建议修改为 'K≥3 introduces sign reversal possibilities for confounding and mediation topologies where K=2 guarantees attenuation'。\"\n\n  - id: R22-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Mahajan (2006), Hu (2008) — 多值误分类非参数识别和非线性模型处理\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R2 提出，R1 AGREE。与本文 K≥3 identifiability 和 Appendix B.14 直接相关。\"\n\n  - id: R22-MR2\n    category: related_work\n    severity: minor\n    summary: \"建议引用 Cornfield et al. (1959) sensitivity analysis 源头、Törnberg (2024) LLM 注释质量实证\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R2 提出。R1 AGREE Cornfield 和 Törnberg。R1 REBUT Plank (2022)——不同问题（disagreement vs error propagation）。\""
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
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 22\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。Limitations 已覆盖。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续多轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 22\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出，R18 修复充分。\"\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 再提，要求主文前置讨论。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 SF-1: 主文讨论不足，要求 NLP task mapping。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 再次升级为 critical。两位 Reviewer 强共识：NLP 中标注误差几乎必然是差异性的；B.6 stress test 显示假设脆弱；Y-stratified test 功效不明。要求主文充分讨论假设合理性边界+差异误分类下的退化保证。\"\n    action_items:\n      - round: 20\n        action: \"W6 fix: Section 3.1 expanded non-differential discussion\"\n        assigned_to: paper_agent\n        status: done\n      - round: 21\n        action: \"SF-1 fix: NLP task mapping added\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 19\n    resolution: \"R18 压缩后编译验证 main text ≤8 pages。连续多轮无复发。\"\n    resolution_round: 19\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: minor\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-W3 再提：Abstract 中 10+ 具体数字稀释主信息。R1 部分反驳（具体数字符合 *ACL 规范），共识降为 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: must-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据——缺少端到端因果应用验证\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 升级为 critical。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 MF-2: 仍为 must-fix。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方 AGREE：Section 4.4 使用真实混淆矩阵但合成 DGP，Appendix B.19/B.20 也是构造的因果问题。缺少从头到尾使用真实数据的验证。R2 承认获取同时有 gold labels 和已知因果效应的真实数据很困难。降级为 should-fix（可理解的局限）。\"\n    action_items:\n      - round: 21\n        action: \"MF-2 fix: Semi-real case study with 10 VAST K=3 production LLM confusion matrices\"\n        assigned_to: agent + paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W5 再提 ASV 与 E-values 区分度。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-N1 合并讨论：ASV 'analogous to E-values' 的措辞削弱新颖性。R1 认为 ASV 将敏感性分析从定性推进到定量是新工具。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: must-fix\n    summary: \"Proportional effects 假设在 NLP 中是强限制，且 Limitations 中完全缺失\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R1]\n        note: \"R20 R1 升级为 critical。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 SF-2: NLP 适用性缺少实质论证。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 R1-N3: proportional effects 验证用满足假设的 DGP，non-proportional sparse DGP 违反率 24.2% 被正文忽略。R2 rebut '循环论证'定性（in-assumption verification 是标准做法），但同意缺少 NLP 中何时合理的讨论。共识：不是循环论证，但实践讨论严重缺失。\"\n    action_items:\n      - round: 21\n        action: \"SF-2 fix: NLP domain-specific argument added\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem/Conjecture 边界在主文中模糊\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R1, R2]\n        note: \"R20 再提。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 MF-1: 结构性矛盾。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方强共识 critical：(1) Theorem 1 仅 K=2 单调性；(2) Theorem 2 K=3 对称但 VAST d_rel=0.30-0.38 远非对称；(3) Conjecture 1 仅数值支撑。ASV 核心性质是猜想而非定理，削弱作为诊断工具的可靠性。R2 补充：adversarial 4 种结构是否覆盖 worst case 不清楚；0.017 违反对因果估计的实际影响未讨论。\"\n    action_items:\n      - round: 21\n        action: \"MF-1 fix: Main text Theorem 2 repositioned as theoretical anchor\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R1]\n        note: \"与 R6-M3 合并。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。R22 继续活跃。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-N1 合并：ASV 新颖性有限。R1 部分同意但认为定量化是增量贡献。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 19\n    resolution: \"随 NEW-1 一同解决。\"\n    resolution_round: 19\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 18\n    resolution: \"连续五轮未被提出，视为已解决。\"\n    resolution_round: 18\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W2 再提。\"\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 SF-3。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方 AGREE：偏差公式在非线性模型（matching, doubly-robust, deep learning）下是否成立是开放问题。NLP 读者更关心实际使用的模型。\"\n    action_items:\n      - round: 21\n        action: \"SF-3 fix: Limitations references B.7 and B.14\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [R2]\n        note: \"R20 R2-W3 再提。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-N1: 'first systematic analysis' 在特定组合上站得住但更多是覆盖度贡献。R1 AGREE 但认为 FWL+ASV 超越单纯覆盖度。\"\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: []\n        note: \"R20 未单独提出。\"\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续多轮未提出。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: minor\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 MI-1: Existing footnote covers。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方 AGREE notation 密度高。R2-m3 建议 notation table。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: minor\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提出。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 R1-minor-1 + R2-m1：y轴量级差异大，建议统一 scale 或加 median 标线。\"\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续四轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续五轮未提出。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续三轮未提出。\"\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续三轮未提出。\"\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R2]\n        note: \"R21 MI-2: R1 rebut（FWL invariance 赋予价值）。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 分歧：R2-W1 认为 PPI++ 作为独立 contribution 不合适；R1 rebut（FWL 负面结果+topology-aware decision procedure 超越单纯应用）。R1 建议调整措辞为 'topology-aware correction guidance including FWL futility result'。\"\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续四轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续五轮未提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。连续三轮未提出。\"\n\n  - id: R20-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中很少成立——缺少合理性讨论和经验量化\"\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 MF-1 合并。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 与 R8-C1 合并。R1-minor-3: Remark 4 与正文脱节（VAST d_rel=0.30-0.38 远非对称，但正文暗示 Theorem 2 涵盖 K=3 主要情形）。双方 AGREE。\"\n\n  - id: R20-N2\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 决策阈值缺乏理论依据和跨设置稳定性验证\"\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 Q4: 已 addressed。MI-2 分歧。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 双方 AGREE：阈值从 MC 经验选取，缺乏形式化依据和对 DGP 参数变化的敏感度讨论。\"\n\n  - id: R21-SF4\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 adversarial search 4 种结构族基于直觉选择，系统性不明\"\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R1, R2]\n        note: \"R21 SF-4: 低优先级。\"\n      - round: 22\n        reviewers: [R2]\n        note: \"R22 R2-N2 合并：adversarial 4 种结构是否覆盖 worst case 不清楚。\"\n\n  - id: R21-MI3\n    category: scope\n    severity: minor\n    summary: \"Venue 适配度处于边界——核心贡献在统计/计量层面\"\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [R2]\n        note: \"R2-W6: ARR 允许跨学科。\"\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R22 分歧：R2-W4 认为偏统计/计量；R1 REBUT（NLP 动机核心、先例充分、Findings 明确接受）。共识：不构成拒稿理由。\"\n\n  - id: R21-Q2\n    category: method\n    severity: should-fix\n    summary: \"DAG 不确定时实践者应如何使用框架——缺少 worst-case guidance\"\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未单独提出。\"\n\n  # === Round 22 新发现 ===\n\n  - id: R22-N1\n    category: novelty\n    severity: must-fix\n    summary: \"相对于测量误差文献（Carroll 2006, Brenner 1993, Buonaccorsi 2010）的增量创新有限——'系统性覆盖'而非'方法论突破'\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"双方 AGREE：技术手段标准（线性代数、FWL 分解），K≥3 推广更多是覆盖度贡献。R1 补充 FWL invariance 和 ASV 定量化是非平凡增量。共识：Findings 足够，进主会需要更强论证。\"\n\n  - id: R22-W1\n    category: soundness\n    severity: should-fix\n    summary: \"ASV 需要 gold labels 估计 C₀ 存在 '鸡生蛋' 问题——gold-label budget 极少时 ASV 可靠性未讨论\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R1-W2 提出，R2 部分 AGREE：PPI++ 也需要 gold labels 所以在同一 budget 内；B.8 bootstrap 收敛需 ~500 gold labels。但 50-100 samples 时的 ASV reliability 未讨论。\"\n\n  - id: R22-W2\n    category: presentation\n    severity: should-fix\n    summary: \"'provably' 在 abstract/正文中使用隐含三个强假设（non-differential + proportional effects + C_A > 0），应附加限定条件\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R1-W5 提出，R2 部分 REBUT：sign preservation（Proposition 1）覆盖一般 K，'provably' 技术上成立。但 R2 同意隐含条件应在 narrative 中提及。共识：建议将 'provably' 附注条件或改为 'under [assumptions], we prove that...'。\"\n\n  - id: R22-W3\n    category: presentation\n    severity: should-fix\n    summary: \"K=2 sign preservation 叙事过于简化——exposure topology 在对角元素 <0.5 时也可 sign reversal\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R2-W5 提出，R1 AGREE：'absent in the binary case' 未限定到 confounding，造成过度概括。建议修改为 'K≥3 introduces sign reversal possibilities for confounding and mediation topologies where K=2 guarantees attenuation'。\"\n\n  - id: R22-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Mahajan (2006), Hu (2008) — 多值误分类非参数识别和非线性模型处理\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R2 提出，R1 AGREE。与本文 K≥3 identifiability 和 Appendix B.14 直接相关。\"\n\n  - id: R22-MR2\n    category: related_work\n    severity: minor\n    summary: \"建议引用 Cornfield et al. (1959) sensitivity analysis 源头、Törnberg (2024) LLM 注释质量实证\"\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [R1, R2]\n        note: \"R2 提出。R1 AGREE Cornfield 和 Törnberg。R1 REBUT Plank (2022)——不同问题（disagreement vs error propagation）。\""
  }
}
```

</details>

---


### Tool result

_source line 1825 · 2026-05-24T01:45:05.648623+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 23491}, \"error\": \"\"}"}

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

_source line 1826 · 2026-05-24T01:47:23.074614+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# 审稿报告 — Round 22 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**审稿模式**: Fresh（重新审稿，无历史记忆）\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+理论/实验验证; R2: 新颖性+完整性+相关工作）\n**轮次**: 1 轮（关键问题达成共识，无需第 2 轮）\n\n---\n\n## Summary\n\n论文研究 LLM 多类标注误差（K≥3 non-differential misclassification）在因果推断中沿 7 种 DAG 拓扑的传播行为。三个核心贡献：(1) 多类偏差分类法，证明 5 种拓扑保持符号、exposure 和 IV 可反转；(2) Annotation Sensitivity Values (ASV)，提供拓扑依赖的脆弱性排序；(3) 拓扑感知校正路由，证明 FWL 不变性使 4 种拓扑的矩阵校正无效。工作量大、技术正确、验证充分，但核心理论贡献仅覆盖 K=2 和 K=3 对称情形，一般 K≥3 依赖未证明的猜想，且三个强假设（非差异误分类、线性 SEM、proportional effects）的联合约束限制了 NLP 场景下的实际适用性。\n\n---\n\n## Strengths\n\n**S1** [强共识] **问题定义精准且时效性强。** LLM 标注在 NLP 因果推断中快速增长（Gilardi et al. 2023, Ziems et al. 2024），但标注误差的因果后果缺乏系统研究。论文填补了这一空白。\n\n**S2** [强共识] **拓扑分类法（Table 1）是原创且高价值的贡献。** 将 7 种 DAG 拓扑的偏差行为系统分类，揭示 topology-dependent vulnerability 全景图。这是超越 Hernán & Cole (2009) 二分类框架的有意义扩展。实践者可根据自己的 DAG 快速判断误分类风险等级。\n\n**S3** [强共识] **FWL 不变性是论文最有实践冲击力的发现。** 证明 matrix-based corrections（MLA, DSL, MC-SIMEX）对 4 个 covariate 拓扑无效——直接挑战了\"有混淆矩阵就能修正\"的朴素直觉。这是一个反直觉且重要的负面结果，对实践者有明确行动指导价值。\n\n**S4** [强共识] **数值验证规模令人印象深刻。** 100,000 Dirichlet 矩阵、545,945 adversarial 矩阵、23 empirical LLM 配置、bootstrap convergence、cross-K robustness——验证的广度和深度在同类论文中少见。\n\n**S5** [强共识] **K=2 证明严格完整。** Theorem 1 + Propositions 1-6 覆盖全部 7 拓扑在 K=2 下的符号保持条件，附录证明逻辑清晰、步骤完整。\n\n**S6** [共识] **Appendix 组织和完整性。** 27 页附录覆盖从完整证明到 DGP 敏感性、非线性模型验证、stress test 等，显示对潜在质疑的预判和回应能力。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [强共识, critical] **K≥3 一般情形仅有猜想，ASV 核心性质未证明。**\n\nTheorem 1（envelope monotonicity）仅对 K=2 成立；Theorem 2 要求对称混淆矩阵，但论文自身的 Remark 4 承认 VAST 实际混淆矩阵的 Frobenius distance d_rel = 0.30–0.38，远非对称；一般 K≥3 的 envelope monotonicity 仅有 Conjecture 1（100,000 矩阵数值验证，最大违反 ε < 0.017）。对于以 \"Multi-Class\" 为核心卖点的论文，K=2 已有成熟文献（Brenner 1993, Hernán & Cole 2009），真正的增量贡献在 K≥3，但该部分停留在猜想阶段。\n\n补充：(1) adversarial testing 的 4 种结构族是否覆盖 worst case 不清楚；(2) ε=0.017 在因果推断中的实际含义未讨论——如果真实效应量很小（τ ≈ 0.05），0.017 的违反可能影响 ASV ranking。\n\n*注：R2 在交叉回应中澄清了一个重要区分——sign preservation（Proposition 1）已被证明覆盖一般 K（under proportional effects），未证明的是 envelope monotonicity。论文正文对这一区分不够清晰。*\n\n**MF-2** [强共识, critical] **非差异误分类假设在 NLP 场景中过强且脆弱。**\n\nDefinition 1 假设 P(A*|A) 不依赖 Y 和 Z，但 LLM 注释器的错误模式高度上下文依赖（情感分类器对中性文本误判率更高；stance detection 对模糊立场质量更差；in-context learning 使误差与 prompt 示例相关）。论文自身的 Appendix B.6 stress test 确认了假设的脆弱性（sign-flip 率在 ε=0.20 时达 13.9%）。Appendix B.26 的 Y-stratified 检验仅拒绝 1/12 配置，但未报告统计功效——低功效下\"不拒绝\"不等于\"假设成立\"。\n\n如果非差异假设不成立，5 个拓扑的符号保持保证不再适用，论文的核心实践价值大幅下降。论文目前不提供差异误分类下的退化保证。\n\n**MF-3** [共识, critical] **相对于测量误差文献的增量创新有限。**\n\n误分类效应因 DAG 拓扑而异的基本洞察在 Carroll et al. (2006)、Brenner (1993)、Buonaccorsi (2010) 中已有充分讨论。技术手段（混淆矩阵乘积、FWL 分解）是标准工具。论文声称的 \"first systematic analysis\" 在 \"K≥2 × 7 topologies × linear SEM\" 这个特定组合上成立，但更多是覆盖度贡献而非方法论创新。R1 补充：FWL invariance 结果和 ASV 定量化是非平凡增量，但不足以构成 EMNLP 主会要求的 \"exciting\" 贡献。\n\n当前形态适合 Findings 接收，进主会需要更强的 K≥3 质变论证或 Conjecture 1 被证明。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [强共识] **Proportional effects 假设的 NLP 适用性讨论严重缺失。** Theorem 1 对 confounding 拓扑要求 proportional effects。Non-proportional sparse DGP 的符号保持违反率达 24.2%（Appendix B.17），但正文对此数据的呈现不足。论文未讨论在实际 NLP 因果研究中 proportional effects 何时合理。（注：R2 澄清 in-assumption verification 不构成\"循环论证\"，但实践相关性讨论确实缺失。）\n\n**SF-2** [强共识] **端到端验证不够真实。** Section 4.4 使用真实混淆矩阵但合成 DGP（semi-synthetic）。缺少从头到尾使用真实数据（真实注释、真实因果问题、真实 outcome）的验证。（R2 承认获取此类数据很困难，建议作为 limitation 明确说明。）\n\n**SF-3** [共识] **线性 SEM 假设限制实际适用性。** NLP 因果推断越来越多使用非参数方法（matching, doubly-robust estimators）。偏差公式在这些模型下是否成立是开放问题。Appendix B.14 仅验证了 logistic 下的 FWL 不变性，未验证偏差公式本身。\n\n**SF-4** [共识] **ASV 的 gold-label \"鸡生蛋\" 问题。** ASV 和 PPI++ 都需要 gold labels 估计 C₀。Bootstrap 收敛分析（Appendix B.8）需 ~500 gold labels，但极少 gold labels（50-100 samples）时 ASV 估计的可靠性未讨论。\n\n**SF-5** [共识] **Algorithm 1 阈值缺乏形式化依据。** 决策阈值从 Monte Carlo 经验选取，未讨论对 DGP 参数变化的敏感度和泛化性。\n\n**SF-6** [共识] **\"provably\" 在 abstract/正文中使用隐含三个强假设。** 建议附注条件或改为 \"under [assumptions], we prove that...\"。\n\n**SF-7** [共识] **K=2 sign reversal 叙事过于简化。** \"Absent in the binary case\" 未限定到 confounding/mediation，exposure topology 在对角元素 <0.5 时也可 sign reversal。建议修改为限定表述。\n\n### Minor（不影响接收）\n\n- Figure 2 各拓扑 y 轴量级差异大，建议统一 scale 或加 median 标线\n- C/C₀/C(δ) 三者区分首次引入时不够清晰，建议 notation table\n- Remark 4（VAST d_rel=0.30-0.38）与正文脱节，应在正文提及 Theorem 2 对称假设的实证局限\n- Abstract 数字密度高（10+ 具体数字），核心信息被稀释（R1 部分反驳：具体数字符合 *ACL 规范）\n- Section 3.3 列了三个 sensitivity analysis 参照物但只详细比较了 E-values\n- \"LLM\" 术语范围：ClinicalBERT 等 task-specific classifiers 非严格 LLM\n- Section 4.4 semi-real case study 描述过于简略\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成强共识 [AGREE]：\n\n1. **Conjecture 1 未证明是核心理论缺口**——削弱 ASV 作为诊断工具的可靠性\n2. **非差异误分类假设在 NLP 中过强**——论文自身的 stress test 确认了假设脆弱性\n3. **端到端验证不够真实**——缺少使用真实因果数据的完整验证\n4. **总体评分 3.5 (Borderline Conference)**——适合 Findings 但进主会需更强论证\n5. **Table 1 taxonomy 和 FWL invariance 是论文最有价值的贡献**\n6. **K=2 证明严格完整**，数值验证规模令人印象深刻\n\n---\n\n## Reviewer Divergence\n\n1. **PPI++ 贡献度**: R2 认为仅是 Angelopoulos et al. (2023) 的应用，不应作为独立 contribution；R1 反驳——FWL 负面结果 + topology-aware decision procedure 超越单纯应用。**Director 判断**: R1 论据更有说服力，FWL futility 是独立贡献。\n\n2. **Venue 适配度**: R2 认为偏统计/计量论文在 EMNLP 受众有限，类似论文通常发 TACL；R1 反驳——NLP 动机核心，先例充分（Keith et al. 2020 ACL, Feder et al. 2022 TACL），Findings 明确接受。**Director 判断**: 不构成拒稿理由。\n\n3. **Abstract 数字密度**: R2 认为堆砌稀释主信息；R1 认为具体数字使 claims 可验证，符合 *ACL 规范。**Director 判断**: 可精简但非关键问题。\n\n---\n\n## Questions\n\n1. Conjecture 1 最大违反值 0.017——在因果推断中（尤其效应量小时），这对 ASV ranking 决策的实际影响有多大？能否给出\"可接受违反阈值\"的理论或实践论证？\n2. 非差异误分类假设不成立时，论文框架是否提供任何退化保证（degradation guarantee）？或者完全失效？\n3. Non-proportional sparse DGP 的 24.2% 符号保持违反率——在实际 NLP 因果研究中（如 sentiment → policy outcome），treatment effects 更可能是 proportional 还是 non-proportional？\n4. Gold-label budget 极少时（50-100 samples），ASV 估计的方差和偏差如何？Appendix B.8 的起步 N*=6,000 是否反映了实际需求？\n5. Algorithm 1 中将 PPI++ 替换为 MC-SIMEX（不需要 gold labels），correction performance 退化幅度和拓扑差异如何？\n\n---\n\n## Missing References\n\n**确认缺失（双方共识）：**\n- Mahajan (2006) \"Identification and estimation of regression models with misclassification\" — 多值误分类非参数识别\n- Hu (2008) \"Identification and estimation of nonlinear models with misclassification\" — 非线性模型误分类\n- Cornfield et al. (1959) — sensitivity analysis 奠基性工作\n- Törnberg (2024) \"ChatGPT-4 Outperforms Experts...\" — LLM 注释质量实证\n\n**R1 提出但已引用（R2 核实确认）：**\n- Kuroki & Pearl (2014) — 已引用 p10\n- Shu & Yi (2019a) — 已引用 p11\n- Lash et al. (2009) — 已引用 p10\n- Gustafson (2003/2004) — 已引用 p10\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已派发但执行超时（300s）。未产出有效 findings。用户可选择重新触发。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 — Borderline Conference**\n**置信度: 4/5**\n\n**评分理由：**\n\n论文解决了一个重要且时效性强的问题（LLM 多类标注误差在因果推断中的传播），提供了有价值的实用工具（Table 1 taxonomy, ASV diagnostics, FWL futility result）。技术执行扎实，K=2 证明严格完整，数值验证规模令人印象深刻。\n\n然而，三个结构性问题限制了论文的评分：(1) 核心理论贡献仅覆盖 K=2 和 K=3 对称，一般 K≥3 依赖未证明的 Conjecture 1——对于以 \"Multi-Class\" 为卖点的论文，这是重要的理论缺口；(2) 非差异误分类假设在 NLP 场景中几乎必然被违反，论文不提供退化保证；(3) 相对于测量误差文献的方法论创新有限，更多是\"系统性覆盖+实用工具\"型贡献。\n\n**定位判断：** 当前形态适合 **Findings 接收**（3.0-3.5 区间），贡献清晰但进主会需要更强的理论支撑或实践验证。如果作者能 (a) 证明 Conjecture 1 或提供更紧的理论界，(b) 提供差异误分类下的退化分析，(c) 更充分论证 K≥3 相对于 K=2 的质变性质，则有望提升至 4.0（Conference 接收）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"first systematic analysis that jointly addresses\" (p2) — 在 \"K≥2 × 7 topologies × linear SEM\" 组合上成立，但应更谨慎定位相对于 Carroll et al. (2006), Buonaccorsi (2010) 的增量\n- Contribution 3 的措辞建议从 \"PPI++ correction\" 调整为 \"topology-aware correction guidance including FWL futility result\"\n- \"absent in the binary case\" 应限定为 \"for confounding and mediation topologies where K=2 guarantees attenuation\"\n\n### Section 3.1 (Non-differential Misclassification)\n- Definition 1 后应在正文充分讨论该假设在 NLP 中何时合理、何时不合理（给出具体 NLP 任务例子）\n- 应引用 Appendix B.6 stress test 的关键结果（至少一段摘要）\n- Y-stratified 检验（B.26）应报告统计功效\n\n### Section 3.2 (Bias Expressions)\n- 应明确区分 \"sign preservation (proved for general K under proportional effects, Proposition 1)\" 和 \"envelope monotonicity (proved for K=2 Theorem 1, K=3 symmetric Theorem 2, conjectured for general K≥3)\"\n- Non-proportional sparse DGP 的 24.2% 违反率应在正文呈现或至少提及\n\n### Section 3.3 (ASV)\n- \"analogous to E-values\" 的措辞削弱新颖性，建议更明确地论证 ASV 的差异化（topology-specific, multi-class specific）\n- 应讨论 Conjecture 1 的 0.017 违反在因果推断实践中的含义（与效应量的相对大小）\n- Gold-label budget 约束应在此处讨论\n\n### Section 4 (Experiments)\n- Section 4.4 semi-real case study 需更多细节（baseline RMSE、improvement 的绝对值）\n- 建议增加一个真正使用真实因果数据的端到端验证（或在 Limitations 中明确说明缺失原因）\n\n### Limitations\n- Proportional effects 何时在 NLP 中合理的讨论应更具体\n- 应明确线性 SEM 在非参数方法下的局限\n\n### Format Compliance\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤8 页 | ✅ |\n| Abstract ≤200 words | ✅ (~170 words) |\n| Double-blind 匿名 | ✅ |\n| Limitations section | ✅ |\n| ACL style template | ✅ |\n| AI 使用披露 | ✅ (Appendix D) |"
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
    "report": "# 审稿报告 — Round 22 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**审稿模式**: Fresh（重新审稿，无历史记忆）\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+理论/实验验证; R2: 新颖性+完整性+相关工作）\n**轮次**: 1 轮（关键问题达成共识，无需第 2 轮）\n\n---\n\n## Summary\n\n论文研究 LLM 多类标注误差（K≥3 non-differential misclassification）在因果推断中沿 7 种 DAG 拓扑的传播行为。三个核心贡献：(1) 多类偏差分类法，证明 5 种拓扑保持符号、exposure 和 IV 可反转；(2) Annotation Sensitivity Values (ASV)，提供拓扑依赖的脆弱性排序；(3) 拓扑感知校正路由，证明 FWL 不变性使 4 种拓扑的矩阵校正无效。工作量大、技术正确、验证充分，但核心理论贡献仅覆盖 K=2 和 K=3 对称情形，一般 K≥3 依赖未证明的猜想，且三个强假设（非差异误分类、线性 SEM、proportional effects）的联合约束限制了 NLP 场景下的实际适用性。\n\n---\n\n## Strengths\n\n**S1** [强共识] **问题定义精准且时效性强。** LLM 标注在 NLP 因果推断中快速增长（Gilardi et al. 2023, Ziems et al. 2024），但标注误差的因果后果缺乏系统研究。论文填补了这一空白。\n\n**S2** [强共识] **拓扑分类法（Table 1）是原创且高价值的贡献。** 将 7 种 DAG 拓扑的偏差行为系统分类，揭示 topology-dependent vulnerability 全景图。这是超越 Hernán & Cole (2009) 二分类框架的有意义扩展。实践者可根据自己的 DAG 快速判断误分类风险等级。\n\n**S3** [强共识] **FWL 不变性是论文最有实践冲击力的发现。** 证明 matrix-based corrections（MLA, DSL, MC-SIMEX）对 4 个 covariate 拓扑无效——直接挑战了\"有混淆矩阵就能修正\"的朴素直觉。这是一个反直觉且重要的负面结果，对实践者有明确行动指导价值。\n\n**S4** [强共识] **数值验证规模令人印象深刻。** 100,000 Dirichlet 矩阵、545,945 adversarial 矩阵、23 empirical LLM 配置、bootstrap convergence、cross-K robustness——验证的广度和深度在同类论文中少见。\n\n**S5** [强共识] **K=2 证明严格完整。** Theorem 1 + Propositions 1-6 覆盖全部 7 拓扑在 K=2 下的符号保持条件，附录证明逻辑清晰、步骤完整。\n\n**S6** [共识] **Appendix 组织和完整性。** 27 页附录覆盖从完整证明到 DGP 敏感性、非线性模型验证、stress test 等，显示对潜在质疑的预判和回应能力。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [强共识, critical] **K≥3 一般情形仅有猜想，ASV 核心性质未证明。**\n\nTheorem 1（envelope monotonicity）仅对 K=2 成立；Theorem 2 要求对称混淆矩阵，但论文自身的 Remark 4 承认 VAST 实际混淆矩阵的 Frobenius distance d_rel = 0.30–0.38，远非对称；一般 K≥3 的 envelope monotonicity 仅有 Conjecture 1（100,000 矩阵数值验证，最大违反 ε < 0.017）。对于以 \"Multi-Class\" 为核心卖点的论文，K=2 已有成熟文献（Brenner 1993, Hernán & Cole 2009），真正的增量贡献在 K≥3，但该部分停留在猜想阶段。\n\n补充：(1) adversarial testing 的 4 种结构族是否覆盖 worst case 不清楚；(2) ε=0.017 在因果推断中的实际含义未讨论——如果真实效应量很小（τ ≈ 0.05），0.017 的违反可能影响 ASV ranking。\n\n*注：R2 在交叉回应中澄清了一个重要区分——sign preservation（Proposition 1）已被证明覆盖一般 K（under proportional effects），未证明的是 envelope monotonicity。论文正文对这一区分不够清晰。*\n\n**MF-2** [强共识, critical] **非差异误分类假设在 NLP 场景中过强且脆弱。**\n\nDefinition 1 假设 P(A*|A) 不依赖 Y 和 Z，但 LLM 注释器的错误模式高度上下文依赖（情感分类器对中性文本误判率更高；stance detection 对模糊立场质量更差；in-context learning 使误差与 prompt 示例相关）。论文自身的 Appendix B.6 stress test 确认了假设的脆弱性（sign-flip 率在 ε=0.20 时达 13.9%）。Appendix B.26 的 Y-stratified 检验仅拒绝 1/12 配置，但未报告统计功效——低功效下\"不拒绝\"不等于\"假设成立\"。\n\n如果非差异假设不成立，5 个拓扑的符号保持保证不再适用，论文的核心实践价值大幅下降。论文目前不提供差异误分类下的退化保证。\n\n**MF-3** [共识, critical] **相对于测量误差文献的增量创新有限。**\n\n误分类效应因 DAG 拓扑而异的基本洞察在 Carroll et al. (2006)、Brenner (1993)、Buonaccorsi (2010) 中已有充分讨论。技术手段（混淆矩阵乘积、FWL 分解）是标准工具。论文声称的 \"first systematic analysis\" 在 \"K≥2 × 7 topologies × linear SEM\" 这个特定组合上成立，但更多是覆盖度贡献而非方法论创新。R1 补充：FWL invariance 结果和 ASV 定量化是非平凡增量，但不足以构成 EMNLP 主会要求的 \"exciting\" 贡献。\n\n当前形态适合 Findings 接收，进主会需要更强的 K≥3 质变论证或 Conjecture 1 被证明。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [强共识] **Proportional effects 假设的 NLP 适用性讨论严重缺失。** Theorem 1 对 confounding 拓扑要求 proportional effects。Non-proportional sparse DGP 的符号保持违反率达 24.2%（Appendix B.17），但正文对此数据的呈现不足。论文未讨论在实际 NLP 因果研究中 proportional effects 何时合理。（注：R2 澄清 in-assumption verification 不构成\"循环论证\"，但实践相关性讨论确实缺失。）\n\n**SF-2** [强共识] **端到端验证不够真实。** Section 4.4 使用真实混淆矩阵但合成 DGP（semi-synthetic）。缺少从头到尾使用真实数据（真实注释、真实因果问题、真实 outcome）的验证。（R2 承认获取此类数据很困难，建议作为 limitation 明确说明。）\n\n**SF-3** [共识] **线性 SEM 假设限制实际适用性。** NLP 因果推断越来越多使用非参数方法（matching, doubly-robust estimators）。偏差公式在这些模型下是否成立是开放问题。Appendix B.14 仅验证了 logistic 下的 FWL 不变性，未验证偏差公式本身。\n\n**SF-4** [共识] **ASV 的 gold-label \"鸡生蛋\" 问题。** ASV 和 PPI++ 都需要 gold labels 估计 C₀。Bootstrap 收敛分析（Appendix B.8）需 ~500 gold labels，但极少 gold labels（50-100 samples）时 ASV 估计的可靠性未讨论。\n\n**SF-5** [共识] **Algorithm 1 阈值缺乏形式化依据。** 决策阈值从 Monte Carlo 经验选取，未讨论对 DGP 参数变化的敏感度和泛化性。\n\n**SF-6** [共识] **\"provably\" 在 abstract/正文中使用隐含三个强假设。** 建议附注条件或改为 \"under [assumptions], we prove that...\"。\n\n**SF-7** [共识] **K=2 sign reversal 叙事过于简化。** \"Absent in the binary case\" 未限定到 confounding/mediation，exposure topology 在对角元素 <0.5 时也可 sign reversal。建议修改为限定表述。\n\n### Minor（不影响接收）\n\n- Figure 2 各拓扑 y 轴量级差异大，建议统一 scale 或加 median 标线\n- C/C₀/C(δ) 三者区分首次引入时不够清晰，建议 notation table\n- Remark 4（VAST d_rel=0.30-0.38）与正文脱节，应在正文提及 Theorem 2 对称假设的实证局限\n- Abstract 数字密度高（10+ 具体数字），核心信息被稀释（R1 部分反驳：具体数字符合 *ACL 规范）\n- Section 3.3 列了三个 sensitivity analysis 参照物但只详细比较了 E-values\n- \"LLM\" 术语范围：ClinicalBERT 等 task-specific classifiers 非严格 LLM\n- Section 4.4 semi-real case study 描述过于简略\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成强共识 [AGREE]：\n\n1. **Conjecture 1 未证明是核心理论缺口**——削弱 ASV 作为诊断工具的可靠性\n2. **非差异误分类假设在 NLP 中过强**——论文自身的 stress test 确认了假设脆弱性\n3. **端到端验证不够真实**——缺少使用真实因果数据的完整验证\n4. **总体评分 3.5 (Borderline Conference)**——适合 Findings 但进主会需更强论证\n5. **Table 1 taxonomy 和 FWL invariance 是论文最有价值的贡献**\n6. **K=2 证明严格完整**，数值验证规模令人印象深刻\n\n---\n\n## Reviewer Divergence\n\n1. **PPI++ 贡献度**: R2 认为仅是 Angelopoulos et al. (2023) 的应用，不应作为独立 contribution；R1 反驳——FWL 负面结果 + topology-aware decision procedure 超越单纯应用。**Director 判断**: R1 论据更有说服力，FWL futility 是独立贡献。\n\n2. **Venue 适配度**: R2 认为偏统计/计量论文在 EMNLP 受众有限，类似论文通常发 TACL；R1 反驳——NLP 动机核心，先例充分（Keith et al. 2020 ACL, Feder et al. 2022 TACL），Findings 明确接受。**Director 判断**: 不构成拒稿理由。\n\n3. **Abstract 数字密度**: R2 认为堆砌稀释主信息；R1 认为具体数字使 claims 可验证，符合 *ACL 规范。**Director 判断**: 可精简但非关键问题。\n\n---\n\n## Questions\n\n1. Conjecture 1 最大违反值 0.017——在因果推断中（尤其效应量小时），这对 ASV ranking 决策的实际影响有多大？能否给出\"可接受违反阈值\"的理论或实践论证？\n2. 非差异误分类假设不成立时，论文框架是否提供任何退化保证（degradation guarantee）？或者完全失效？\n3. Non-proportional sparse DGP 的 24.2% 符号保持违反率——在实际 NLP 因果研究中（如 sentiment → policy outcome），treatment effects 更可能是 proportional 还是 non-proportional？\n4. Gold-label budget 极少时（50-100 samples），ASV 估计的方差和偏差如何？Appendix B.8 的起步 N*=6,000 是否反映了实际需求？\n5. Algorithm 1 中将 PPI++ 替换为 MC-SIMEX（不需要 gold labels），correction performance 退化幅度和拓扑差异如何？\n\n---\n\n## Missing References\n\n**确认缺失（双方共识）：**\n- Mahajan (2006) \"Identification and estimation of regression models with misclassification\" — 多值误分类非参数识别\n- Hu (2008) \"Identification and estimation of nonlinear models with misclassification\" — 非线性模型误分类\n- Cornfield et al. (1959) — sensitivity analysis 奠基性工作\n- Törnberg (2024) \"ChatGPT-4 Outperforms Experts...\" — LLM 注释质量实证\n\n**R1 提出但已引用（R2 核实确认）：**\n- Kuroki & Pearl (2014) — 已引用 p10\n- Shu & Yi (2019a) — 已引用 p11\n- Lash et al. (2009) — 已引用 p10\n- Gustafson (2003/2004) — 已引用 p10\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已派发但执行超时（300s）。未产出有效 findings。用户可选择重新触发。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 — Borderline Conference**\n**置信度: 4/5**\n\n**评分理由：**\n\n论文解决了一个重要且时效性强的问题（LLM 多类标注误差在因果推断中的传播），提供了有价值的实用工具（Table 1 taxonomy, ASV diagnostics, FWL futility result）。技术执行扎实，K=2 证明严格完整，数值验证规模令人印象深刻。\n\n然而，三个结构性问题限制了论文的评分：(1) 核心理论贡献仅覆盖 K=2 和 K=3 对称，一般 K≥3 依赖未证明的 Conjecture 1——对于以 \"Multi-Class\" 为卖点的论文，这是重要的理论缺口；(2) 非差异误分类假设在 NLP 场景中几乎必然被违反，论文不提供退化保证；(3) 相对于测量误差文献的方法论创新有限，更多是\"系统性覆盖+实用工具\"型贡献。\n\n**定位判断：** 当前形态适合 **Findings 接收**（3.0-3.5 区间），贡献清晰但进主会需要更强的理论支撑或实践验证。如果作者能 (a) 证明 Conjecture 1 或提供更紧的理论界，(b) 提供差异误分类下的退化分析，(c) 更充分论证 K≥3 相对于 K=2 的质变性质，则有望提升至 4.0（Conference 接收）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"first systematic analysis that jointly addresses\" (p2) — 在 \"K≥2 × 7 topologies × linear SEM\" 组合上成立，但应更谨慎定位相对于 Carroll et al. (2006), Buonaccorsi (2010) 的增量\n- Contribution 3 的措辞建议从 \"PPI++ correction\" 调整为 \"topology-aware correction guidance including FWL futility result\"\n- \"absent in the binary case\" 应限定为 \"for confounding and mediation topologies where K=2 guarantees attenuation\"\n\n### Section 3.1 (Non-differential Misclassification)\n- Definition 1 后应在正文充分讨论该假设在 NLP 中何时合理、何时不合理（给出具体 NLP 任务例子）\n- 应引用 Appendix B.6 stress test 的关键结果（至少一段摘要）\n- Y-stratified 检验（B.26）应报告统计功效\n\n### Section 3.2 (Bias Expressions)\n- 应明确区分 \"sign preservation (proved for general K under proportional effects, Proposition 1)\" 和 \"envelope monotonicity (proved for K=2 Theorem 1, K=3 symmetric Theorem 2, conjectured for general K≥3)\"\n- Non-proportional sparse DGP 的 24.2% 违反率应在正文呈现或至少提及\n\n### Section 3.3 (ASV)\n- \"analogous to E-values\" 的措辞削弱新颖性，建议更明确地论证 ASV 的差异化（topology-specific, multi-class specific）\n- 应讨论 Conjecture 1 的 0.017 违反在因果推断实践中的含义（与效应量的相对大小）\n- Gold-label budget 约束应在此处讨论\n\n### Section 4 (Experiments)\n- Section 4.4 semi-real case study 需更多细节（baseline RMSE、improvement 的绝对值）\n- 建议增加一个真正使用真实因果数据的端到端验证（或在 Limitations 中明确说明缺失原因）\n\n### Limitations\n- Proportional effects 何时在 NLP 中合理的讨论应更具体\n- 应明确线性 SEM 在非参数方法下的局限\n\n### Format Compliance\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤8 页 | ✅ |\n| Abstract ≤200 words | ✅ (~170 words) |\n| Double-blind 匿名 | ✅ |\n| Limitations section | ✅ |\n| ACL style template | ✅ |\n| AI 使用披露 | ✅ (Appendix D) |"
  }
}
```

</details>

---


### Tool result

_source line 1827 · 2026-05-24T01:47:26.742359+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3667
}
```

</details>

---


### Assistant

_source line 1828 · 2026-05-24T01:47:38.079261+00:00_

审稿报告已投递至 Research Director。

---

**Round 22 审稿完成。** 两位 Reviewer 独立初审 + 交叉回应，1 轮达成共识。

**最终评分：3.5 / 5 (Borderline Conference)**

核心判断：
- **3 个 Must-Fix**：(1) K≥3 envelope monotonicity 仅有 Conjecture 1，ASV 核心性质未证明；(2) 非差异误分类假设在 NLP 中过强且脆弱；(3) 相对于测量误差文献增量创新有限
- **7 个 Should-Fix**：proportional effects 讨论缺失、端到端验证不够真实、线性 SEM 限制、ASV gold-label 问题、Algorithm 1 阈值、"provably" 限定、K=2 叙事简化
- **主要优势**：问题重要、Table 1 taxonomy 实用价值高、FWL invariance 是最有冲击力的发现、K=2 证明严格、数值验证规模大

**定位**：当前形态适合 Findings 接收。进主会需要证明 Conjecture 1 或提供差异误分类退化分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 185

## Round 185

2 recorded events


### User

_source line 1829 · 2026-05-24T01:47:40.973661+00:00_

[Reviewer 2 审稿结果]:
交叉审查已提交。核心结论：

- 与 R1 在总体评分（3.5）和三个核心关切（Conjecture 未证明、非差异假设过强、实践验证不足）上一致
- 修正了 R1 的三个事实性问题：Theorem 1 的 K 适用范围、ε=0.01 sign flip 数据、四个"遗漏引用"实际均已引用
- 对 R1 的"循环论证"批评（N3）给出了 REBUT——验证定理在其假设条件下成立不是循环论证，但同意缺少 proportional effects 在 NLP 中何时合理的讨论

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

_source line 1830 · 2026-05-24T01:47:53.193609+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **Overall: 3.5 / 5（Borderline Conference）**，两位 Reviewer 评分一致
- **3 个 Must-Fix**：(1) K≥3 envelope monotonicity 仅有 Conjecture 未证明；(2) 非差异误分类假设在 NLP 中过强且脆弱；(3) 相对于测量误差文献的增量创新有限
- **7 个 Should-Fix**：proportional effects NLP 讨论缺失、端到端验证不够真实、线性 SEM 局限、ASV gold-label 问题、Algorithm 1 阈值依据、"provably" 限定条件、K=2 叙事简化
- **定位判断**：当前适合 Findings 接收，进主会需证明 Conjecture 1 或提供差异误分类退化分析
- **Issue Tracker** 已同步更新（`review_issues.yaml`，含 Round 22 全部新发现）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 186

## Round 186

66 recorded events


### User

_source line 1831 · 2026-05-24T03:58:20.630678+00:00_

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

_source line 1832 · 2026-05-24T03:58:28.911247+00:00_

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

_source line 1833 · 2026-05-24T03:58:28.912114+00:00_

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

_source line 1834 · 2026-05-24T03:58:36.497938+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
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
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1835 · 2026-05-24T03:58:36.548486+00:00_



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

_source line 1836 · 2026-05-24T03:58:40.015084+00:00_

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

_source line 1837 · 2026-05-24T03:58:40.517873+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-24T03:58:40.518266+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1839 · 2026-05-24T03:58:41.925020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1840 · 2026-05-24T03:58:42.026096+00:00_

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
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1841 · 2026-05-24T03:58:45.844396+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

The search results do not contain a specific "EMNLP 2026 call for papers submission guidelines" document. However, the results 
…[truncated 1247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 5326
}
```

</details>

---


### Tool call

_source line 1842 · 2026-05-24T03:58:49.060670+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 official website call for papers"
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
    "query": "EMNLP 2026 official website call for papers"
  }
}
```

</details>

---


### Tool call

_source line 1843 · 2026-05-24T03:58:50.015107+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit formatting"
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
    "query": "ACL Rolling Review 2026 submission guidelines page limit formatting"
  }
}
```

</details>

---


### Tool call

_source line 1844 · 2026-05-24T03:58:51.622311+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/",
  "description": "List paper directory contents"
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
    "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 1845 · 2026-05-24T03:58:51.783465+00:00_

_pdf_images
aaai2026.bst
aaai2026.sty
abstract.tex
acl.sty
acl_natbib.bst
appendix_proofs.tex
conclusion.tex
conjecture_dgp_sensitivity_table.tex
e2e_demo_table.tex
e2e_real_cm_table.tex
exp_a_stress_test_table.tex
exp_c_bootstrap_figure.pdf
exp_e_asv_stability_table.tex
experiments.tex
fig2_bias_distribution.pdf
fig3_asv_ranking.pdf
introduction.tex
k3_symmetric_proof.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 161
}
```

</details>

---


### Tool result

_source line 1846 · 2026-05-24T03:58:55.564646+00:00_

Web search results for query: "EMNLP 2026 official website call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on my web se
…[truncated 1519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6503
}
```

</details>

---


### Tool result

_source line 1847 · 2026-05-24T03:58:59.082287+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit formatting"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.02279v1"}]

Based on the search results, here is information about ACL Rolling Review 2026 submission guidelines regarding page limits and formatting:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

## Formatting Guidelines

All long and short papers must follow
…[truncated 1066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 9067
}
```

</details>

---


### Tool call

_source line 1848 · 2026-05-24T03:59:13.451342+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_23/ 2>/dev/null || echo \"NO_DIR\"; ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"; ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES\"",
  "description": "Check review artifacts"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_23/ 2>/dev/null || echo \"NO_DIR\"; ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"; ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES\"",
    "description": "Check review artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1849 · 2026-05-24T03:59:14.406413+00:00_

total 968
drwxr-xr-x  2 ubuntu ubuntu   4096 May 24 03:58 .
drwxr-xr-x 44 ubuntu ubuntu  12288 May 24 03:58 ..
-rw-r--r--  1 ubuntu ubuntu 971710 May 24 03:46 submitted.pdf
round_1.md
round_11.md
round_12.md
round_13.md
round_14.md
round_15.md
round_16.md
round_17.md
round_18.md
round_19.md
round_2.md
round_20.md
round_21.md
round_22.md
round_3.md
round_4.md
round_5.md
round_6.md
round_7.md
round_8.md
round_9.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1850 · 2026-05-24T03:59:14.406809+00:00_

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

_source line 1851 · 2026-05-24T03:59:14.858861+00:00_

1	\begin{abstract}
2	When LLM-generated annotations feed into causal inference, annotation quality is the wrong thing to worry about---the causal DAG topology determines whether errors attenuate, amplify, or reverse the treatment effect estimate. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification in linear structural equation models and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. Under proportional effects, five topologies provably preserve the treatment effect sign; exposure and IV can reverse it. Under empirical LLM confusion matrices, sign reversal is confined to exposure topology. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$, $K{=}3$ symmetric) and extensively validated (general $K{\geq}3$) monotonicity, yielding a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. A case study with 10 production LLM confusion matrices confirms: topology-aware correction reduces exposure bias from 61\% to $<$1\%, while topology-blind corrections are provably futile under linear regression for four topologies.
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

_source line 1852 · 2026-05-24T03:59:14.859325+00:00_

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

_source line 1853 · 2026-05-24T03:59:15.211529+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors (equivalently, misclassification) from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference. Standard classification metrics do not capture this risk: within an $F_1$ range of 0.61--0.69 across three frontier LLMs, causal bias varies by an order of magnitude across topologies.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ expo
…[truncated 3500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1854 · 2026-05-24T03:59:15.212037+00:00_

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

_source line 1855 · 2026-05-24T03:59:15.363151+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	Foundations appear in \citet{carroll2006, gustafson2004, buonaccorsi2010, bound2001measurement}, with DAG-based formalization by \citet{hernan_cole2009} and \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{bross1954misclassification, brenner1993, ogburn_vanderweele2012}, but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. Extensions address differential measurement error~\cite{edwards_lessler_naimi2021, imai_yamamoto2010}, endogenous misreporting~\cite{nguimkeu_denteh_tchernis2019}, mismeasured covariates under IPW~\cite{shu_yi2019a, shu_yi2019b}, mediation with mismeasured mediators~\cite{valeri_vanderweele2013}, nonclassical error~\cite{schennach2020mismeasured}, and multiply robust estimation~\cite{wei2025multiply}. All analyze a single DAG topology; ours characterizes how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document rapid LLM annotator adoption (surveyed by \citealt{tan2024llm}), \citet{baumann2025} found 31\% incorrect conclusions, and \citet{kim_garg2025} showed 60\% error correlation across models~\cite{pangakis_wolken_fasching2023, cheng_mayya_sedoc2024, variance_aware_llm2026, hidden_measurement_error2026}. \citet{audinet2025} benchmark debiasing; \citet{keith_jensen_oconnor2020} survey the landsca
…[truncated 1207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1856 · 2026-05-24T03:59:24.513794+00:00_

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

_source line 1857 · 2026-05-24T03:59:24.564946+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes probability limits (plim, $N \to \infty$) rather than finite-sample variance. The FWL theorem~\cite{frisch1933partial} guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables---this is why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}). Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}) collects all notation.
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	In batch annotation pipelines, the LLM processes each text independently without access to $Y$, making non-differentiality an architectural invariant~\cite{ziems2024can}; Y-stratified permutation tests confirm this (1/12 rejection at $\alpha{=}0.05$; Appendix~\ref{sec:y_stratified_test}). Non-differentiality holds when error is label-intrinsic (e.g., vague category boundaries); it may be violated when error depends on features
…[truncated 14219 chars]

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

_source line 1858 · 2026-05-24T03:59:25.017461+00:00_

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

_source line 1859 · 2026-05-24T03:59:25.520459+00:00_

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
15	Analytical probability limits match Monte Carlo estimates with MAPE of 1.6\%, averaged across 161 scenarios (23 LLM configurations $\times$ 7 topologies; per-topology range: 0.3\%--3.7\%).
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; at diagonal $\geq 0.9$, violation persists at 11.9\% (Appendix~\ref{sec:iv_dirichlet_subspace}). Under the full Dirichlet prior, 85\% of matrices violate the binary ``toward-null'' guarantee and 83.4\% cause sign reversal; $\min_k C_{kk} < 0.55$ predicts sign reversal with 91\% accuracy (Appendix~\ref{sec:sign_determinants}). The $K{=}2$ control confirms classical attenuation~\cite{brenner1993}, establishing the multi-class failure as structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\ref{conj:monotone}); M-bias shows weakest sensitivity (53.2\% violation). All patterns persist at $K{=}5,7$ (Appendix~\ref{sec:cross_k_robustness}).
22	
23	\paragraph{IV: W
…[truncated 6365 chars]

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

_source line 1860 · 2026-05-24T03:59:25.520784+00:00_

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

_source line 1861 · 2026-05-24T03:59:25.772326+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: at $K{\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs yield a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective under linear regression for four covariate topologies (FWL invariance). The practical implication is direct: identify the topology first---for four topologies, no matrix-based correction helps; for exposure, PPI++ with gold labels reduces bias by 93.6\%.
5	
6	\section*{Limitations}
7	
8	We assume non-differential misclassification (Appendix~\ref{sec:nondiff_stress}). Closed-form results (Theorems~1--2) assume linear SEMs with proportional effects ($f{=}\lambda g$); FWL invariance extends to logistic models for covariate topologies (Appendix~\ref{app:fwl_proof}), but for exposure, logistic specification can increase bias (Appendix~\ref{sec:fwl_nonlinear}), and practitioners should verify linearity assumptions. Sign preservation holds at 97.3\% under non-proportional effects (Table~\ref{tab:proportional_empirical}). Proving general $K{\geq}3$ envelope monotonicity beyond symmetric matrices remains open~\cite{schennach2020mismeasured}.
9	

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

_source line 1862 · 2026-05-24T03:59:25.772713+00:00_

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

_source line 1863 · 2026-05-24T03:59:26.074381+00:00_

File content (46676 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

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

_source line 1864 · 2026-05-24T03:59:35.879373+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"pdfinfo not available\"; texcount -sum -1 main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex 2>/dev/null | tail -5 || echo \"texcount not available\"",
  "description": "Check paper page count and word count"
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
    "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"pdfinfo not available\"; texcount -sum -1 main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex 2>/dev/null | tail -5 || echo \"texcount not available\"",
    "description": "Check paper page count and word count"
  }
}
```

</details>

---


### Tool result

_source line 1865 · 2026-05-24T03:59:36.735867+00:00_

Pages:           35
Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1866 · 2026-05-24T03:59:36.786774+00:00_

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

_source line 1867 · 2026-05-24T03:59:37.239460+00:00_

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
…[truncated 770 chars]

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

_source line 1868 · 2026-05-24T03:59:37.239801+00:00_

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

_source line 1869 · 2026-05-24T03:59:37.290340+00:00_

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

_source line 1870 · 2026-05-24T03:59:49.917240+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/  */ /g' | wc -w",
  "description": "Count abstract words"
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
    "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/  */ /g' | wc -w",
    "description": "Count abstract words"
  }
}
```

</details>

---


### Tool result

_source line 1871 · 2026-05-24T03:59:50.622373+00:00_

170
Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1872 · 2026-05-24T03:59:50.825068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_23/submitted.pdf",
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
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_23/submitted.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 1873 · 2026-05-24T03:59:51.277521+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_23/submitted.pdf (948.9KB)

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

_source line 1874 · 2026-05-24T04:00:10.851330+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
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
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1875 · 2026-05-24T04:00:10.901840+00:00_

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

_source line 1876 · 2026-05-24T04:00:14.813075+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "config.yaml"
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
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1877 · 2026-05-24T04:00:14.863621+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

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

_source line 1878 · 2026-05-24T04:00:19.177710+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 external_review || echo \"NO_CONFIG\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 external_review || echo \"NO_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1879 · 2026-05-24T04:00:19.228296+00:00_

NO_CONFIG

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

_source line 1880 · 2026-05-24T04:00:25.500238+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10; find /home/ubuntu/.agent-ml-research-prod_0510 -name \"config.yaml\" -maxdepth 3 2>/dev/null | head -5",
  "description": "Find config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10; find /home/ubuntu/.agent-ml-research-prod_0510 -name \"config.yaml\" -maxdepth 3 2>/dev/null | head -5",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 1881 · 2026-05-24T04:00:25.600993+00:00_

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

_source line 1882 · 2026-05-24T04:00:30.819334+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510 -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -10; cat /home/ubuntu/.agent-ml-research-prod_0510/config.yaml 2>/dev/null | head -30 || echo \"no root config\"",
  "description": "Find project config"
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
    "command": "find /home/ubuntu/.agent-ml-research-prod_0510 -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -10; cat /home/ubuntu/.agent-ml-research-prod_0510/config.yaml 2>/dev/null | head -30 || echo \"no root config\"",
    "description": "Find project config"
  }
}
```

</details>

---


### Tool result

_source line 1883 · 2026-05-24T04:00:30.971270+00:00_

/home/ubuntu/.agent-ml-research-prod_0510/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-prod_0510/global/approvals.yaml
/home/ubuntu/.agent-ml-research-prod_0510/config/crons.yaml
/home/ubuntu/.agent-ml-research-prod_0510/config/approvals.yaml
/home/ubuntu/.agent-ml-research-prod_0510/config/backend.yaml
/home/ubuntu/.agent-ml-research-prod_0510/config/feishu.yaml
/home/ubuntu/.agent-ml-research-prod_0510/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-prod_0510/config/resources.yaml
/home/ubuntu/.agent-ml-research-prod_0510/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-prod_0510/workspace.yaml

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

_source line 1884 · 2026-05-24T04:00:35.541037+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/workspace.yaml 2>/dev/null | grep -A10 \"causal_annot\" | head -20; cat /home/ubuntu/.agent-ml-research-prod_0510/config/venue_registry.yaml 2>/dev/null | grep -A10 \"EMNLP\" | head -20",
  "description": "Check workspace and venue config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/workspace.yaml 2>/dev/null | grep -A10 \"causal_annot\" | head -20; cat /home/ubuntu/.agent-ml-research-prod_0510/config/venue_registry.yaml 2>/dev/null | grep -A10 \"EMNLP\" | head -20",
    "description": "Check workspace and venue config"
  }
}
```

</details>

---


### Tool result

_source line 1885 · 2026-05-24T04:00:35.592018+00:00_

    display_name: EMNLP 2026

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

_source line 1886 · 2026-05-24T04:00:39.409844+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/workspace.yaml 2>/dev/null | grep -B5 -A30 \"causal_annot\"",
  "description": "Read project workspace config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/workspace.yaml 2>/dev/null | grep -B5 -A30 \"causal_annot\"",
    "description": "Read project workspace config"
  }
}
```

</details>

---


### Tool result

_source line 1887 · 2026-05-24T04:00:39.510895+00:00_

(Bash completed with no output)

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


### Tool call

_source line 1888 · 2026-05-24T04:00:42.372894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/workspace.yaml",
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
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/workspace.yaml",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1889 · 2026-05-24T04:00:42.423551+00:00_

1	projects: {}
2	

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

_source line 1890 · 2026-05-24T04:01:07.807475+00:00_

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

_source line 1891 · 2026-05-24T04:01:28.650214+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20842
}
```

</details>

---


### Tool call

_source line 1892 · 2026-05-24T04:01:31.511591+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页 + 无限参考文献\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，供审稿人参考但不强制阅读\n- **Limitations**: 必须有，不计入页数限制\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`（入口文件，通过 \\input 引用 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**，重点关注：\n\n1. **证明正确性**：Theorem 1（K=2 envelope monotonicity）、Theorem 2（K=3 symmetric monotonicity）、Proposition 1（sign preservation）的证明是否完整、正确？假设条件是否合理且明确陈述？\n2. **Bias expressions 推导**：7 个 topology 的 bias 表达式是否正确？FWL decomposition 的使用是否得当？\"FWL invariance renders matrix-based corrections provably ineffective\" 这一 futility result 的论证是否严谨？\n3. **ASV 框架**：C(δ) 参数化是否合理？三种 ASV 类型的定义是否清晰无歧义？Conjecture 1 的数值验证是否充分（545,945 adversarial curves）？\n4. **假设合理性**：Non-differential misclassification 假设在 LLM annotation 场景下是否现实？Linear SEM 假设的限制是否被充分讨论？Proportional effects 假设的适用范围？\n5. **实验设计**：Monte Carlo 验证的设置是否合理（N=10,000, 100,000 Dirichlet matrices）？实证验证（HumAID K=10, VAST K=3, CivilComments K=2）是否足够？Correction methods 的对比是否公平？\n6. **数学符号和记号**：是否一致？是否存在符号滥用或定义不清的地方？\n\n请按 ARR/EMNLP 的审稿标准，给出完整审稿意见，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。\n\nOverall Assessment 评分标准：5 = Consider for Award，4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit。"
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
    "project": "causal_annot_error_attrib",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页 + 无限参考文献\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，供审稿人参考但不强制阅读\n- **Limitations**: 必须有，不计入页数限制\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`（入口文件，通过 \\input 引用 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**，重点关注：\n\n1. **证明正确性**：Theorem 1（K=2 envelope monotonicity）、Theorem 2（K=3 symmetric monotonicity）、Proposition 1（sign preservation）的证明是否完整、正确？假设条件是否合理且明确陈述？\n2. **Bias expressions 推导**：7 个 topology 的 bias 表达式是否正确？FWL decomposition 的使用是否得当？\"FWL invariance renders matrix-based corrections provably ineffective\" 这一 futility result 的论证是否严谨？\n3. **ASV 框架**：C(δ) 参数化是否合理？三种 ASV 类型的定义是否清晰无歧义？Conjecture 1 的数值验证是否充分（545,945 adversarial curves）？\n4. **假设合理性**：Non-differential misclassification 假设在 LLM annotation 场景下是否现实？Linear SEM 假设的限制是否被充分讨论？Proportional effects 假设的适用范围？\n5. **实验设计**：Monte Carlo 验证的设置是否合理（N=10,000, 100,000 Dirichlet matrices）？实证验证（HumAID K=10, VAST K=3, CivilComments K=2）是否足够？Correction methods 的对比是否公平？\n6. **数学符号和记号**：是否一致？是否存在符号滥用或定义不清的地方？\n\n请按 ARR/EMNLP 的审稿标准，给出完整审稿意见，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。\n\nOverall Assessment 评分标准：5 = Consider for Award，4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit。"
  }
}
```

</details>

---


### Tool result

_source line 1893 · 2026-05-24T04:01:42.895730+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11384
}
```

</details>

---


### Tool call

_source line 1894 · 2026-05-24T04:01:43.050331+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页 + 无限参考文献\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，供审稿人参考但不强制阅读\n- **Limitations**: 必须有，不计入页数限制\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`（入口文件，通过 \\input 引用 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点关注：\n\n1. **创新贡献评估**：三个贡献（multi-class bias taxonomy、ASV framework、topology-aware correction routing）的新颖性如何？与现有工作（Brenner 1993, TeBlunthuis 2024, Lee & Wood-Doughty 2024）的增量贡献是否足够？\n2. **相关工作覆盖**：是否遗漏重要相关工作？measurement error 文献（Carroll 2006, Buonaccorsi 2010）、LLM annotation 文献（Gilardi 2023, Baumann 2025）、sensitivity analysis 文献（VanderWeele & Ding 2017, Cinelli 2020）的覆盖是否全面？\n3. **写作质量**：论文结构是否清晰？论证逻辑是否连贯？Abstract 是否准确反映内容？Introduction 的 motivation 是否有说服力？\n4. **Claim 与 evidence 匹配**：Abstract/Introduction 中的声明是否都有实验或理论支撑？是否存在过度声称（overclaiming）？\n5. **实际影响力**：研究成果对 NLP 社区的实际价值？practitioner 能否直接使用这些结果？toolkit（plan010）的可用性如何？\n6. **Presentation 细节**：图表质量、表格设计、符号一致性、可读性。Appendix 的组织是否合理？\n7. **EMNLP 适配度**：这篇论文是否适合 EMNLP？empirical methods 的成分是否足够？\n\n请按 ARR/EMNLP 的审稿标准，给出完整审稿意见，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。\n\nOverall Assessment 评分标准：5 = Consider for Award，4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit。"
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
    "project": "causal_annot_error_attrib",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页 + 无限参考文献\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，供审稿人参考但不强制阅读\n- **Limitations**: 必须有，不计入页数限制\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`（入口文件，通过 \\input 引用 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点关注：\n\n1. **创新贡献评估**：三个贡献（multi-class bias taxonomy、ASV framework、topology-aware correction routing）的新颖性如何？与现有工作（Brenner 1993, TeBlunthuis 2024, Lee & Wood-Doughty 2024）的增量贡献是否足够？\n2. **相关工作覆盖**：是否遗漏重要相关工作？measurement error 文献（Carroll 2006, Buonaccorsi 2010）、LLM annotation 文献（Gilardi 2023, Baumann 2025）、sensitivity analysis 文献（VanderWeele & Ding 2017, Cinelli 2020）的覆盖是否全面？\n3. **写作质量**：论文结构是否清晰？论证逻辑是否连贯？Abstract 是否准确反映内容？Introduction 的 motivation 是否有说服力？\n4. **Claim 与 evidence 匹配**：Abstract/Introduction 中的声明是否都有实验或理论支撑？是否存在过度声称（overclaiming）？\n5. **实际影响力**：研究成果对 NLP 社区的实际价值？practitioner 能否直接使用这些结果？toolkit（plan010）的可用性如何？\n6. **Presentation 细节**：图表质量、表格设计、符号一致性、可读性。Appendix 的组织是否合理？\n7. **EMNLP 适配度**：这篇论文是否适合 EMNLP？empirical methods 的成分是否足够？\n\n请按 ARR/EMNLP 的审稿标准，给出完整审稿意见，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。\n\nOverall Assessment 评分标准：5 = Consider for Award，4.5 = Borderline Award，4 = Conference，3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit。"
  }
}
```

</details>

---


### Tool result

_source line 1895 · 2026-05-24T04:01:44.833065+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1782
}
```

</details>

---


### Assistant

_source line 1896 · 2026-05-24T04:02:07.950698+00:00_

Round 1 审稿任务已全部派发：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法严谨性（证明、bias expressions、ASV 框架、假设） |
| Reviewer 2 | ✅ 已派发 | 新颖性/完整性（创新贡献、相关工作、写作、影响力） |
| 视觉审查 | ✅ 已启动 | 排版质量（并行，不阻塞） |

等待 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 187

## Round 187

2 recorded events


### User

_source line 1897 · 2026-05-24T04:07:05.321322+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：新颖性与完整性

## Paper Summary

本文研究 LLM 标注的多分类误差如何在因果推断中传播。在线性结构方程模型（SEM）+ starred-node DAG 框架下，作者：(1) 为 7 种典型 DAG 拓扑推导了 K-class 非差异性误分类的偏差表达式，证明 K≥3 时存在二分类中不存在的符号反转可能性；(2) 提出 Annotation Sensitivity Values (ASV) 框架，给出拓扑脆弱性排序；(3) 证明矩阵校正方法在线性回归下对 4 种拓扑无效（FWL 不变性），并提出拓扑感知的校正路由算法。

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 理论框架扎实且问题重要，但三个核心贡献的新颖性在不同程度上属于已有方法的系统性延伸，real-world empirical validation 相对薄弱，distance to acceptance 在于 novelty bar 和 empirical depth。

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 理论推导严谨，25 页 appendix 含完整证明和 Monte Carlo 验证；但 Conjecture 1 未证明，非差异性假设验证有限 |
| Excitement | 3/5 | 问题定位好（NLP×因果推断交叉），但核心技术手段（FWL + starred-node DAG + Brenner 1993 延伸）增量性较强 |
| Reproducibility | 4/5 | Monte Carlo 设置详细（Appendix B），参数完整；但未提供代码/数据 release 承诺 |
| Reviewer Confidence | 4/5 | 熟悉因果推断、measurement error 和 NLP annotation 文献 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心贡献的增量性问题——三个贡献与 prior work 的边界不够清晰

- 具体位置：Section 1 (contributions list), Section 2 (Related Work)
- 问题：
  - **贡献 1（multi-class bias taxonomy）**：Brenner (1993) 已对 polytomous confounder 建立了偏差放大理论；TeBlunthuis (2024) 对 binary misclassification 覆盖了 4 种 DAG 拓扑。本文将二者从 K=2 / 单一拓扑 推广到 K≥3 / 7 种拓扑，核心技术手段仍是 FWL 定理 + probability limit 推导，属于 systematic extension 而非 methodological breakthrough。论文未充分讨论这种延伸的技术难度——读者可能会问"为什么不能直接对每个拓扑机械地套用 Brenner 的方法？"
  - **贡献 2（ASV framework）**：ASV 本质上是"使偏差 sign flip 所需的最小混淆矩阵扰动"，是一个有用的 diagnostic 工具，但方法论深度有限。与 E-values (VanderWeele & Ding, 2017) 的类比在 Abstract 和 Section 3.3 中被频繁使用，但 E-values 解决的是 unmeasured confounding 的 sensitivity analysis，ASV 解决的是 measurement error 的 sensitivity，二者在 problem structure 上有本质差异。这个类比可能误导读者高估 ASV 的方法论贡献。
  - **贡献 3（topology-aware correction routing）**：Algorithm 1 (page 35) 本质上是一个 if-else 决策树：根据拓扑选择 FWL/PPI++/DSL/MC-SIMEX。这更像是 practical guideline 而非 algorithmic contribution。
- 为什么影响接收：EMNLP main conference 对 novelty 有较高要求。三个贡献中没有一个达到"让审稿人感到 surprising methodology"的水平。综合来看，贡献是 real 但 incremental。
- 建议修改方向：(a) 在 Introduction 中明确讨论从 K=2 到 K≥3 的延伸涉及的 non-trivial 技术挑战（如 alternating-sign coefficients 导致的 sign cancellation 在高维 confusion matrix 中的复杂交互），而不只是列结果；(b) 对 ASV 与 E-values 的类比加注 caveat，或换一种 framing；(c) 将 Algorithm 1 降格为 practical contribution，不与理论贡献并列。

**N2** [critical] Conjecture 1 未证明削弱理论贡献的完整性

- 具体位置：Section 3.3, page 6; Appendix A.4 (Conjecture 1 verification), page 14
- 问题：ASV 框架的核心性质——envelope monotonicity for general K≥3——停留在 Conjecture 状态（"We therefore state a conjecture supported by numerical evidence"）。虽然有 100,000 Dirichlet-sampled matrices 和 545,945 adversarial curves 的数值验证（Appendix A.11），且 K=2 和 K=3 symmetric 的 exact monotonicity 已证明（Theorems 1-2），但对于一篇理论导向的论文，核心性质留为 conjecture 是明显的完整性缺陷。
- 为什么影响接收：如果 monotonicity 不成立（即存在未发现的反例），ASV 的 vulnerability ranking 就不可靠。虽然数值验证覆盖面广，但不能替代证明。
- 建议修改方向：(a) 尝试完成一般 K 的证明，或至少将 gap 缩小到一个明确的 technical lemma；(b) 如果无法证明，则在正文中更诚实地讨论这个 limitation，而非仅在 appendix 中提及"analytic proof for general K remain open"。

**N3** [critical] Real-world empirical validation 不充分

- 具体位置：Section 4.4 (Empirical Validation, page 7-8), Section B.18-B.21 (appendix case studies)
- 问题：论文的 empirical validation 主要是"理论预测 vs. Monte Carlo 模拟的一致性验证"（Section 4.2-4.3），而非在真实因果推断问题上验证框架的实用性。Section 4.4 使用 3 个 NLP 数据集（HumAID K=10, VAST K=3, CivilComments K=2）的 23 个 LLM 配置，但仅验证了 bias ranking 与理论预测的一致性，并未展示在实际因果效应估计中使用该框架能改善多少决策质量。ClinicalBERT case study（Appendix B.18）更接近实际应用，但放在了 appendix 中且只是 retrospective application。
  
  对于一篇投向 EMNLP（"Empirical Methods"）的论文，"empirical" 成分的权重偏低。主要实验是 Monte Carlo 模拟，不是在真实数据上的因果推断实验。
- 为什么影响接收：EMNLP 审稿人可能期待更强的 empirical grounding：(a) 至少一个完整的端到端因果推断 pipeline，从 LLM annotation → causal estimation → correction，在真实数据上展示；(b) 与现有 sensitivity analysis 工具（如 E-values, sensemakr）的定量对比。
- 建议修改方向：将 ClinicalBERT case study 提升到正文（可能替代部分 Monte Carlo 内容），或增加一个更完整的 end-to-end 实证。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 非差异性误分类假设（Definition 1）的实际合理性讨论不足

- 具体位置：Section 3.1 (Definition 1, page 3-4), Section B.5-B.6 (appendix), Limitations (page 8)
- 问题：非差异性假设要求 P(A*=j | A=k, Y, Z) = P(A*=j | A=k)——混淆矩阵不依赖于 outcome Y。对于 LLM 标注，这个假设可能系统性地被违反：LLM 在不同 outcome value 下的标注准确率可能不同（例如，极端情感更容易被正确标注）。Section B.5-B.6 讨论了 non-differential 验证（VAST 数据 Y-stratified test），但覆盖范围有限（1 个数据集，12 个 LLM 配置）。Limitations 部分提到了这个问题但只有一句话。
- 建议：在正文 Section 3.1 中加一段讨论该假设在 LLM annotation 场景下何时成立/何时可能被违反，并引用 differential misclassification 文献（如 Bross 1954, Dosemeci et al. 1990 中的相关讨论）。

**W2** [warning] 线性 SEM 限制与 NLP 实际应用的 gap

- 具体位置：Limitations (page 8-9), Appendix B.7 (Robustness to Nonlinear DGP), B.14 (FWL under Nonlinear Models)
- 问题：整个理论框架假设线性 SEM。Appendix B.7 测试了 logistic regression，发现 matrix-based correction 的 bias reduction ≈ 0（"the OLS gap — so the invariance falls formally"），承认"matrix-based corrections remain practically useless under logistic regression"。对于 NLP 任务中常见的非线性关系（logistic/softmax outcome models），框架的适用性受到根本限制。论文在 Limitations 中承认但正文从未正面讨论这个 gap。
- 建议：正文 Section 5 (Conclusion) 或 Section 3 (Method) 中应明确框架的适用边界，而非将此完全留给 Limitations + Appendix。

**W3** [warning] 相关工作覆盖存在缺口

- 具体位置：Section 2 (Related Work, page 2-3)
- 问题：
  - **Sensitivity analysis 文献**：论文将 ASV 类比于 E-values 但未实质性地对比 Cinelli & Hazlett (2020) "Making Sense of Sensitivity" 中的 partial R² sensitivity framework。Cinelli 的框架同样提供 topology-dependent sensitivity 分析，且有成熟的 R 包（sensemakr）。应讨论 ASV 与 sensemakr 的互补性。
  - **Multiple imputation for measurement error**：Carroll et al. (2006) 中 SIMEX 以外的方法（如 regression calibration, multiple imputation）未被讨论或排除。
  - **Prediction-powered inference**：PPI++ (Angelopoulos et al., 2023) 被用作校正方法之一，但论文未充分 engage 这一文献线——特别是 PPI++ 的 theoretical guarantees 在 misclassification 场景下是否仍然成立。
  - **Causal inference under covariate measurement error**：Shi & Miao (2023) "Multiply robust causal inference"、Webb et al. (2019) "To adjust or not to adjust" 等处理 covariate measurement error 的近年文献未被引用。
- 建议：补充上述文献的讨论，特别是说明 ASV 与 partial R² sensitivity analysis 的关系。

**W4** [warning] Abstract 中 "annotation quality is the wrong thing to worry about" 的 overclaiming

- 具体位置：Abstract, line 1-2
- 问题：这个 counterintuitive hook 在修辞上很有效，但存在 overclaiming 风险。论文的结果是"在已知 DAG 拓扑和线性 SEM 下，拓扑比标注质量更能决定偏差方向"。但在实际应用中，(a) DAG 拓扑通常未知或有争议；(b) 标注质量仍然通过 confusion matrix 决定偏差大小。说"annotation quality is the wrong thing to worry about"过于绝对。
- 建议：改为更 nuanced 的表述，如 "topology, not just annotation quality, determines whether errors attenuate or reverse the treatment effect"。

**W5** [warning] Figure 2 信息密度过高

- 具体位置：Figure 2, page 5
- 问题：Figure 2 在一个 figure 中塞入了 7 种拓扑的 bias 分布和 sign reversal 率。子图太小，密度标签难以辨认。红色 sign reversal 标记在小尺寸下不够醒目。对于论文的核心可视化，这影响了 readability。
- 建议：考虑只在 Figure 2 中展示最有代表性的 3-4 种拓扑（如 confounding, exposure, IV, M-bias），将完整版放入 appendix。

## 小问题（不影响接收）

- Section 3.1, page 4: "Throughout, τ denotes the causal estimand of interest, whose definition varies by topology" — 在后续各拓扑推导中 τ 的定义切换（OLS coefficient / direct effect / Wald ratio）可能造成读者混淆。建议在首次引入时用表格统一各拓扑下 τ 的定义。
- Table 1 (page 7): 表格设计紧凑但列头 "Violation" "Sign Flip" "Amplif." 的含义需要查阅正文才能理解，缺少自解释性。
- Appendix C (Notation, page 34): 符号表放在 appendix 最后不够便于查阅，建议移至 appendix 开头或正文开头。
- Remark 5 (page 19, Appendix A.7): "Empirical K≥3 confusion matrices from LLM stance detection depart substantially from symmetry" — 这个观察很重要但被埋在了 appendix 深处。建议在正文中简要提及。
- Section D (Use of AI Assistants, page 34): 披露了 Claude 的使用，符合 ACL 政策。

## 主要优势

1. **问题定位精准且 timely**：随着 LLM annotation 在 CSS/NLP 研究中的普及，理解标注误差在因果推断中的传播是一个切实的需求。论文是第一个系统性地覆盖 K≥3 + 7 种 DAG 拓扑的工作。
2. **理论框架严谨**：25 页 appendix 包含完整的数学证明、Monte Carlo 验证、和 adversarial testing。Propositions 1-3 和 Theorems 1-2 的推导清晰可验证。
3. **实用价值明确**：sign-flip guarantee（5 种拓扑在 proportional effects 下保号）、vulnerability ranking（IV fragile → M-bias immune）、FWL invariance result（4 种拓扑下矩阵校正无效）——这些结果直接可被 practitioner 使用。
4. **写作质量高**：正文结构清晰，density 高但叙事流畅。Abstract 的 counterintuitive hook 有效（尽管稍有 overclaim）。从 bias taxonomy → ASV → correction routing 的叙事线性逻辑连贯。
5. **Semi-real case study 接地气**：使用 10 个 production LLM confusion matrices（Section B.20）和 VAST 真实数据（Section B.18-B.19），将理论与实践连接。

## Missing References

- Cinelli, C. & Hazlett, C. (2020). "Making Sense of Sensitivity: Extending Omitted Variable Bias." JRSS-B. — 论文引用了但未充分对比 ASV 与 partial R² framework
- Shi, X. & Miao, W. (2023). "Multiply robust causal inference in the presence of an error-prone treatment." Statistical Methods in Medical Research. — 处理 treatment measurement error 的近年重要工作（注：论文实际已引用此文，记为 Ba Wei et al.）
- Ogburn, E.L. & VanderWeele, T.J. (2012). "On the nondifferential misclassification of a binary confounder." Epidemiology. — 已引用
- Grüger, J., Kay, R., & Schumacher, M. (1991). "The validity of inferences based on incomplete observations in disease state models." Biometrics. — 关于 misclassification 下的推断有效性
- Lash, T.L. et al. (2009). "Applying Quantitative Bias Analysis to Epidemiologic Data." Springer. — quantitative bias analysis 的标准教材，论文已引用
- Edwards, J.K. et al. (2021). "An underappreciated source of measurement error." — 已引用

## EMNLP 适配度评估

论文在 topic 上适合 EMNLP（NLP annotation × causal inference），但在 method 偏好上存在张力：这是一篇以理论推导为主的方法论论文，"empirical methods" 的成分主要是 Monte Carlo 模拟而非在真实数据上的大规模实证。在 ACL/EMNLP 的审稿文化中，这类理论导向论文通常需要 (a) 更强的实证验证 或 (b) 真正 surprising 的理论结果 来达到 main conference 的 bar。本文介于 Conference 和 Findings 之间。

## 最终判断

Overall: **3.5 (Borderline Conference)**

理论扎实、问题重要、写作好。但 (1) 三个贡献的增量性、(2) Conjecture 1 未证明、(3) real-world empirical validation 不足，使论文距离 main conference acceptance 有一定 gap。如果 authors 能在 rebuttal 中 (a) 证明或显著缩小 Conjecture 1 的 gap，(b) 展示一个 end-to-end 的真实因果推断案例，(c) 更好地 articulate K≥3 延伸的 non-trivial 技术挑战，评分有望提升到 4.0。当前状态下，推荐 Findings。


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

_source line 1898 · 2026-05-24T04:07:18.647564+00:00_

Reviewer 2 审稿意见已收到（3.5 Borderline Conference）。核心问题：贡献增量性、Conjecture 1 未证明、real-world 实证不足。

等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 188

## Round 188

2 recorded events


### User

_source line 1899 · 2026-05-24T04:07:41.585427+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成，已提交至 Review Director。

核心判断：**Overall 3.5 (Borderline Conference)**，推荐 Findings。

关键发现：
- 3 个 Must-Fix：(N1) 三个贡献相对 Brenner 1993/TeBlunthuis 2024 增量性较强，novelty bar 不够；(N2) Conjecture 1（ASV envelope monotonicity for general K≥3）未证明，核心理论不完整；(N3) Real-world empirical validation 薄弱，主要靠 Monte Carlo 模拟而非真实因果推断端到端验证
- 5 个 Should-Fix：非差异性假设讨论不足、线性 SEM 限制未在正文正面讨论、相关工作缺 Cinelli 2020 partial R² 对比、Abstract overclaiming、Figure 2 信息过载
- 主要优势：问题定位精准且 timely、理论推导严谨（25 页 appendix）、实用价值明确（sign-flip guarantee + vulnerability ranking + FWL invariance）、写作质量高

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

_source line 1900 · 2026-05-24T04:07:50.379735+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 189

## Round 189

6 recorded events


### User

_source line 1901 · 2026-05-24T04:08:12.788743+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性审查

## Summary

本文系统分析了多类别（K-class）LLM 标注误差在 7 种 canonical DAG topology 下对因果推断的传播机制。在线性 SEM + non-differential misclassification 假设下，作者推导了各 topology 的 bias 闭合表达式，证明了 K=2（proportional effects）和 K=3（symmetric confusion matrix）下的 envelope monotonicity（Theorems 1-2），提出了 Annotation Sensitivity Values (ASV) 框架用于量化标注脆弱性，并建立了 FWL invariance 下 matrix-based correction 对 covariate topologies 无效的 futility result。论文通过 Monte Carlo 模拟（100,000 Dirichlet 矩阵）和三个 NLP 数据集（HumAID K=10, VAST K=3, CivilComments K=2）进行了广泛验证。

---

## 总体评分

**Overall**: 3.5 / 5 (Borderline Conference)

**一句话总结**: 理论框架严谨且全面，但核心定理限于特殊情形（proportional effects / symmetric matrices），且 non-differential misclassification 假设在论文自身的 stress test 中被违反，实际适用性存在显著不确定性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 在已声明假设范围内，证明完整正确；但关键定理的适用范围受限（proportional effects, symmetric C），general-K monotonicity 仅为 conjecture |
| Excitement | 3.5 / 5 | 系统性 topology 分析和 ASV 框架有新意，但 linear SEM 限制了对 NLP 社区的实际影响；更接近计量经济学/流行病学贡献 |
| Reproducibility | 4 / 5 | Algorithm 1 伪代码完整，Monte Carlo 参数详尽，附录提供了具体 DGP 参数；但代码/数据似未公开 |
| Confidence | 4 / 5 | 仔细检查了主要证明推导和实验设置 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Theorem 1 仅对 proportional effects 成立，一般情形缺少证明

- 具体位置：Section 3.3 (p.6), Appendix A.4 (p.14)
- 问题：Theorem 1 的 envelope monotonicity 严格限于 proportional effects (f = λg)。对于 non-proportional effects，论文仅依赖 20,000 random (C_δ, p, g) triples 的数值验证（Appendix A.4, "sufficient in practice but not universal"）。然而 proportional effects 假设要求 confounder 对 treatment 和 outcome 的效应成严格比例关系，这在 NLP 因果推断场景中几乎不可验证，也很少成立（e.g., 情感标签对因变量的效应形态通常与对处理变量的效应形态不同）。
- 为什么影响接收：这是论文两个核心定理之一。如果主要理论结果仅在高度受限的特殊情形下成立，论文的理论贡献范围会显著缩小。读者可能误以为 monotonicity 是一般性结论。
- 建议修改方向：(a) 在正文中明确讨论 proportional effects 假设的实际合理性，给出 NLP 场景中何时可能成立的具体例子；(b) 对 non-proportional case 给出明确的 counterexample 或 sufficient conditions；(c) 如果一般性证明不可行，将 Appendix A.4 中的数值验证提升到正文并量化 violation 的严重程度。

**N2** [critical] Non-differential misclassification假设与论文自身 stress test 结果矛盾

- 具体位置：Definition 1 (p.3), Section B.6 (p.25), Table 9 (p.27)
- 问题：Definition 1 假设 P(A*=j | A=k, Y, Z) = P(A*=j | A=k)，即 confusion matrix 不依赖于 outcome Y 或 covariates Z。但论文自身的 stress test (Appendix B.6) 在 K≥3 的 exposure topology 下发现 13.3% 的 baseline violation rate（Table 9）。更关键的是，正文 p.4 承认 "under stress testing, sign reversal recurs in 14/16 K≥3 exposure configurations at α=0.01 structured departures"，sign-flip rate 从 2.6% 上升到 9.67%（α=0.20）。这说明 non-differential 假设在 LLM annotation 实践中是可以被违反的，而论文的全部理论结果都建立在这一假设之上。
- 为什么影响接收：如果核心假设在目标场景中系统性地被违反，理论结果的实际指导价值大打折扣。论文应更诚实地讨论这一 tension，而不是将 stress test 结果放在附录。
- 建议修改方向：(a) 在正文 Method 部分讨论当假设被违反时各定理的 graceful degradation 程度（e.g., monotonicity 在多大程度的 differential misclassification 下仍近似成立？）；(b) 提供 robustness bound：如果 |P(A*|A,Y) - P(A*|A)| < ε，bias expressions 的误差上界是多少？

**N3** [critical] Conjecture 1 未被证明但在实践框架中承担关键角色

- 具体位置：Section 3.3 (p.6), Appendix B.12 (p.28)
- 问题：Conjecture 1（general K≥3 的 approximate envelope monotonicity）仅有数值验证（545,945 adversarial curves，maximum step deviation < 0.04），但论文的 ASV 框架（Section 3.3）和 Algorithm 1 (p.35) 的 practical recommendations 隐含依赖此 conjecture。如果 monotonicity 不成立，ASV 的 safe/fragile partition 可能不正确，导致错误的 correction 建议。
- 为什么影响接收：论文将 Conjecture 1 作为 ASV 框架的理论支撑，但 conjecture 不是 theorem。数值验证虽然广泛，但无法排除 corner cases（尤其在 adversarial/pathological confusion matrices 下）。
- 建议修改方向：(a) 明确标注 ASV 框架的哪些结论不依赖 Conjecture 1（e.g., sign preservation 有独立证明）；(b) 讨论如果 Conjecture 1 失败，Algorithm 1 的输出如何 degrade。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Linear SEM 假设对 NLP 场景的适用性讨论不足

- 具体位置：Section 3.1 (p.3), Limitations (p.8-9)
- 问题：论文在 Limitations 中提到 "closed-form results (Theorems 1-2) assume linear SEMs with proportional effects"，但未充分讨论这对 NLP 实践意味着什么。NLP 中常见的因果推断任务（e.g., text classification → downstream decision）往往涉及高度非线性关系。论文的 Appendix B.7 测试了 nonlinear DGP 下的 robustness，结果显示 sign-flip rates 对六种 confusion matrix structures 在 structured model 下仍保持 0%（Table 8），但 nonlinear bias magnitudes 与 linear bias expressions 的对应关系未被建立。
- 建议：在正文中增加一段讨论，明确 linear SEM 结果可以作为 nonlinear settings 的 first-order approximation 的条件和局限。

**W2** [warning] FWL futility result 的 novelty 和 framing 需要更精确

- 具体位置：Section 3 (p.3), Appendix B.2 (p.23-24)
- 问题：论文声称 "FWL invariance renders matrix-based corrections provably ineffective"（Abstract, p.1）。但这本质上是 FWL 定理的直接推论：对 covariate topologies，treatment coefficient 的估计只依赖于 residualized treatment（控制 A 或 A* 后），而 matrix-based correction 改变的是 A 的编码但不改变 residualized treatment 的结构。这在理解 FWL 定理的读者看来并不令人惊讶。论文的贡献在于将这一观察与 correction method 文献（PP++, DSL, MC-SIMEX 等）联系起来，但 "provably ineffective" 的 framing 可能夸大了 novelty。此外，Table 6 (Appendix B.2) 显示在 logistic regression 下 matrix-based correction 的 bias reduction 也接近 0%，但这是经验结果而非 "provable"。
- 建议：(a) 区分 "provably ineffective under OLS" 和 "empirically ineffective under logistic regression"；(b) 讨论对于 nonlinear models（e.g., logistic, neural）correction 可能有效的条件。

**W3** [warning] C(δ) = (1-δ)I + δC₀ 参数化的局限性

- 具体位置：Section 3.3 (p.5)
- 问题：ASV 框架使用 C(δ) = (1-δ)I + δC₀ 的线性插值参数化。这假设 confusion matrix 的 "形状" 由 C₀ 固定，只有 "严重程度" 随 δ 变化。但实际 LLM annotation 中，不同类别的误分类模式可能随整体质量变化而定性改变（e.g., 低质量时易混淆类别的 pattern 可能与高质量时不同）。论文在 Appendix B.11 中测试了 ASV stability across DGP parameters，但未讨论 C(δ) 参数化本身的 misspecification 风险。
- 建议：讨论 C(δ) 参数化失效的情形，或提供 alternative parameterizations 的 robustness check。

**W4** [warning] 实证验证的数据集多样性不足

- 具体位置：Section 4.4 (p.7-8)
- 问题：三个实证数据集（HumAID, VAST, CivilComments）均为文本分类任务，且均使用 LLM 作为 annotator。论文未验证框架在以下场景下的适用性：(a) 非文本模态（e.g., 图像分类中的 annotation error）；(b) human annotator error（而非 LLM error，尽管 LLM error 是论文的主要 motivation）；(c) 更大的 K 值（K=10 是最大的，但实际 NLP 任务中 K>10 很常见，如 NER、fine-grained sentiment）。
- 建议：至少讨论框架在 K 较大时的 computational scalability 和 theoretical behavior（e.g., Conjecture 1 在 K=20 时是否仍有合理的 numerical evidence？）。

**W5** [warning] Theorem 2 的 symmetric confusion matrix 假设过强

- 具体位置：Section 3.3 (p.6), Appendix A.6 (p.17-18)
- 问题：Theorem 2 的 exact monotonicity 结果要求 K=3 symmetric confusion matrix。但 Remark 5 (Appendix, p.19) 指出 "empirical K=3 confusion matrices from LLM stance detection deviate substantially from symmetry (median relative Frobenius distance d_rel=0.33; range 0.30-0.38)"。这意味着 Theorem 2 的精确结论在实际 LLM confusion matrices 上可能不适用。论文通过 Remark 5 转向数值验证，但这削弱了 "exact monotonicity" claim 的实际价值。
- 建议：对 asymmetric K=3 matrices 给出 monotonicity 的 deviation bound（e.g., 当 d_rel < threshold 时 approximate monotonicity 以什么 tolerance 成立）。

---

## Questions for Authors

**Q1**: Proposition 1(a) 的 sign preservation condition (sign(τ) = sign(τ+B_OV)) 在实践中如何验证？B_OV 依赖于未观测的真实 A 的分布，而实际中我们只有 A*。作者是否有基于 observable quantities 的可行检验方法？

**Q2**: Algorithm 1 (p.35) 的 Step 2 使用 "DAG uncertainty" 分支（"If T uncertain, compute ASV under candidate topologies"）。在实践中，DAG 结构通常是未知的，researcher 需要对 topology 做假设。作者如何建议处理 DAG misspecification？如果真实 topology 是 exposure 但 researcher 误认为是 confounding，Algorithm 1 的输出会有什么后果？

**Q3**: Table 1 (p.7) 报告 IV topology 的 sign flip rate 为 52.6%，远高于其他 topologies。但 IV topology 在 NLP 因果推断中的实际使用频率如何？作者能否给出 NLP 中使用 annotated variable 作为 instrument 的具体应用场景？

**Q4**: Appendix B.3 (p.24) 的 ClinicalBERT Case Study 使用了 retrospective application 到 Lee and Wood-Doughty (2021) 的数据。但该 case study 中 confusion matrix 的估计方法是什么？是来自 gold-labeled subset 还是假设的？如果是假设的，这如何证明框架的 "empirical" validation？

**Q5**: 论文在 Appendix D (p.34) 提到使用了 AI (Claude) 作为 coding and writing assistant。这是否包括定理证明的辅助？如果是，如何确保证明的正确性不依赖于 AI 的错误？

---

## Missing References

1. **Differential misclassification in causal inference**: Hernán and Cole (2009) 的工作在引用列表中出现，但论文未充分引用 **Lash et al. (2009, "Applying Quantitative Bias Analysis to Epidemiologic Data")** 中关于 probabilistic bias analysis 在 differential misclassification下的系统方法。这与论文的 sensitivity analysis 框架直接相关。

2. **Sensitivity analysis for measurement error**: **Imai and Yamamoto (2010)** 关于 mediation analysis 中 measurement error 的 sensitivity analysis 方法在 Related Work 中被引用（p.3, "endogenous misspecification"），但未讨论其方法与 ASV 框架的异同。

3. **Recent NLP causal inference**: 论文引用了 Keith et al. (2020) 和 Feder et al. (2022) 的 survey，但缺少 **Pryzant et al. (2021)** 关于 text as treatment 的具体 correction 方法的讨论（尽管在 Related Work 中简略提及 "parametric sensitivity"）。

---

## 小问题（不影响接收）

- p.3, Definition 1: "misclassification of A is non-differential with respect to outcome Y and covariates Z" — 建议在 Definition 后立即给出一个 LLM annotation pipeline 中该假设成立的具体条件（e.g., "the LLM processes each text independently without access to Y"），而不是延迟到 p.4。
- p.5, Figure 2 caption: "Ref = sign reversal" — 这个缩写不直观，建议改为 "Rev" 或直接用全称。
- p.6, Remark 1: "ASV is topology-dependent (same C has different consequences across topologies)" — 这是论文的核心 insight 之一，但 Remark 的形式使其不够突出，建议在正文中用更 prominent 的方式呈现。
- p.8, Algorithm 1 仅在附录 p.35 给出，但在正文中被引用多次。考虑将简化版 Algorithm 放入正文。
- Table 1 (p.7): "Cond." 列的含义（Conditional sign-flip guarantee）需要在 caption 或脚注中解释，当前标注不够清晰。

---

## 主要优势

1. **系统性和完整性**：7 种 DAG topologies 的统一分析框架在 misclassification 文献中属首次，远超先前限于 binary 或单一 topology 的工作（Brenner 1993, Ogburn and VanderWeele 2012）。
2. **理论深度**：在已声明假设范围内，证明严谨完整（特别是 Appendix A.3-A.8 的逐 topology 推导、A.4/A.6 的 monotonicity 证明、以及 A.10 的 sign preservation conditions 汇总）。
3. **实践导向**：ASV 框架和 Algorithm 1 提供了可操作的 correction decision procedure，从理论到实践的 bridge 比大多数 measurement error 理论论文做得好。
4. **诚实的局限性讨论**：论文明确区分了 proven results（Theorems 1-2）和 conjectured results（Conjecture 1），标注了 proportional effects / symmetric 的限制条件，这种透明性值得肯定。
5. **广泛的数值验证**：100,000+ Dirichlet confusion matrices、545,945 adversarial curves、23 real LLM configurations、以及附录中的多种 robustness checks（non-differential stress test, nonlinear DGP, bootstrap uncertainty, FWL breakdown under logistic regression 等）。


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

_source line 1902 · 2026-05-24T04:09:07.832806+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 项，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## Paper Summary\n\n本文研究 LLM 标注的多分类误差如何在因果推断中传播。在线性结构方程模型（SEM）+ starred-node DAG 框架下，作者：(1) 为 7 种典型 DAG 拓扑推导了 K-class 非差异性误分类的偏差表达式，证明 K≥3 时存在二分类中不存在的符号反转可能性；(2) 提出 Annotation Sensitivity Values (ASV) 框架，给出拓扑脆弱性排序；(3) 证明矩阵校正方法在线性回归下对 4 种拓扑无效（FWL 不变性），并提出拓扑感知的校正路由算法。\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] 核心贡献的增量性问题——三个贡献与 prior work 的边界不够清晰\n- 贡献 1（multi-class bias taxonomy）：Brenner (1993) 已对 polytomous confounder 建立了偏差放大理论；TeBlunthuis (2024) 对 binary misclassification 覆盖了 4 种 DAG 拓扑。本文将二者从 K=2 / 单一拓扑推广到 K≥3 / 7 种拓扑，核心技术手段仍是 FWL 定理 + probability limit 推导，属于 systematic extension 而非 methodological breakthrough。\n- 贡献 2（ASV framework）：ASV 本质上是\"使偏差 sign flip 所需的最小混淆矩阵扰动\"，方法论深度有限。与 E-values 的类比可能误导读者高估 ASV 的方法论贡献。\n- 贡献 3（topology-aware correction routing）：Algorithm 1 本质上是一个 if-else 决策树，更像 practical guideline 而非 algorithmic contribution。\n\n**N2** [critical] Conjecture 1 未证明削弱理论贡献的完整性\n- ASV 框架的核心性质——envelope monotonicity for general K≥3——停留在 Conjecture 状态。虽有 100,000 Dirichlet-sampled matrices 和 545,945 adversarial curves 的数值验证，但对于理论导向论文，核心性质留为 conjecture 是完整性缺陷。\n\n**N3** [critical] Real-world empirical validation 不充分\n- Empirical validation 主要是\"理论预测 vs. Monte Carlo 模拟的一致性验证\"，而非在真实因果推断问题上验证框架的实用性。对于投向 EMNLP 的论文，\"empirical\" 成分偏低。\n\n## Should-Fix 问题\n\n**W1** 非差异性误分类假设的实际合理性讨论不足\n**W2** 线性 SEM 限制与 NLP 实际应用的 gap\n**W3** 相关工作覆盖存在缺口（Cinelli 2020 partial R² 对比、regression calibration、PPI++ theoretical guarantees）\n**W4** Abstract 中 \"annotation quality is the wrong thing to worry about\" 的 overclaiming\n**W5** Figure 2 信息密度过高\n\n## 主要优势\n\n1. 问题定位精准且 timely\n2. 理论框架严谨（25 页 appendix）\n3. 实用价值明确（sign-flip guarantee + vulnerability ranking + FWL invariance）\n4. 写作质量高\n5. Semi-real case study 接地气"
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
    "project": "causal_annot_error_attrib",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 项，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## Paper Summary\n\n本文研究 LLM 标注的多分类误差如何在因果推断中传播。在线性结构方程模型（SEM）+ starred-node DAG 框架下，作者：(1) 为 7 种典型 DAG 拓扑推导了 K-class 非差异性误分类的偏差表达式，证明 K≥3 时存在二分类中不存在的符号反转可能性；(2) 提出 Annotation Sensitivity Values (ASV) 框架，给出拓扑脆弱性排序；(3) 证明矩阵校正方法在线性回归下对 4 种拓扑无效（FWL 不变性），并提出拓扑感知的校正路由算法。\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] 核心贡献的增量性问题——三个贡献与 prior work 的边界不够清晰\n- 贡献 1（multi-class bias taxonomy）：Brenner (1993) 已对 polytomous confounder 建立了偏差放大理论；TeBlunthuis (2024) 对 binary misclassification 覆盖了 4 种 DAG 拓扑。本文将二者从 K=2 / 单一拓扑推广到 K≥3 / 7 种拓扑，核心技术手段仍是 FWL 定理 + probability limit 推导，属于 systematic extension 而非 methodological breakthrough。\n- 贡献 2（ASV framework）：ASV 本质上是\"使偏差 sign flip 所需的最小混淆矩阵扰动\"，方法论深度有限。与 E-values 的类比可能误导读者高估 ASV 的方法论贡献。\n- 贡献 3（topology-aware correction routing）：Algorithm 1 本质上是一个 if-else 决策树，更像 practical guideline 而非 algorithmic contribution。\n\n**N2** [critical] Conjecture 1 未证明削弱理论贡献的完整性\n- ASV 框架的核心性质——envelope monotonicity for general K≥3——停留在 Conjecture 状态。虽有 100,000 Dirichlet-sampled matrices 和 545,945 adversarial curves 的数值验证，但对于理论导向论文，核心性质留为 conjecture 是完整性缺陷。\n\n**N3** [critical] Real-world empirical validation 不充分\n- Empirical validation 主要是\"理论预测 vs. Monte Carlo 模拟的一致性验证\"，而非在真实因果推断问题上验证框架的实用性。对于投向 EMNLP 的论文，\"empirical\" 成分偏低。\n\n## Should-Fix 问题\n\n**W1** 非差异性误分类假设的实际合理性讨论不足\n**W2** 线性 SEM 限制与 NLP 实际应用的 gap\n**W3** 相关工作覆盖存在缺口（Cinelli 2020 partial R² 对比、regression calibration、PPI++ theoretical guarantees）\n**W4** Abstract 中 \"annotation quality is the wrong thing to worry about\" 的 overclaiming\n**W5** Figure 2 信息密度过高\n\n## 主要优势\n\n1. 问题定位精准且 timely\n2. 理论框架严谨（25 页 appendix）\n3. 实用价值明确（sign-flip guarantee + vulnerability ranking + FWL invariance）\n4. 写作质量高\n5. Semi-real case study 接地气"
  }
}
```

</details>

---


### Tool result

_source line 1903 · 2026-05-24T04:09:29.051065+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21218
}
```

</details>

---


### Tool call

_source line 1904 · 2026-05-24T04:09:29.152157+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 项，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性审查\n\n## 总体评分\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] Theorem 1 仅对 proportional effects 成立，一般情形缺少证明\n- Theorem 1 的 envelope monotonicity 严格限于 proportional effects (f = λg)。对于 non-proportional effects，论文仅依赖 20,000 random triples 的数值验证。proportional effects 假设在 NLP 因果推断场景中几乎不可验证也很少成立。\n\n**N2** [critical] Non-differential misclassification 假设与论文自身 stress test 结果矛盾\n- 论文自身 stress test (Appendix B.6) 在 K≥3 exposure topology 下发现 13.3% baseline violation rate。正文 p.4 承认 \"sign reversal recurs in 14/16 K≥3 exposure configurations at α=0.01 structured departures\"，sign-flip rate 从 2.6% 上升到 9.67%（α=0.20）。核心假设在目标场景中系统性被违反。\n\n**N3** [critical] Conjecture 1 未被证明但在实践框架中承担关键角色\n- Conjecture 1 仅有数值验证（545,945 adversarial curves），但 ASV 框架和 Algorithm 1 的 practical recommendations 隐含依赖此 conjecture。\n\n## Should-Fix 问题\n\n**W1** Linear SEM 假设对 NLP 场景的适用性讨论不足\n**W2** FWL futility result 的 novelty 和 framing 需要更精确——本质是 FWL 定理的直接推论，\"provably ineffective\" framing 可能夸大 novelty\n**W3** C(δ) = (1-δ)I + δC₀ 参数化的局限性——实际 LLM annotation 中误分类模式可能随整体质量变化而定性改变\n**W4** 实证验证的数据集多样性不足——仅文本分类、仅 LLM annotator、K 最大 10\n**W5** Theorem 2 的 symmetric confusion matrix 假设过强——Remark 5 指出实际 LLM confusion matrices 偏离对称性显著（median d_rel=0.33）\n\n## Questions\n\nQ1: Proposition 1(a) 的 B_OV 依赖于未观测 A，如何基于 observable quantities 验证？\nQ2: DAG misspecification 下 Algorithm 1 的后果？\nQ3: IV topology 在 NLP 中的实际使用频率？\nQ4: ClinicalBERT Case Study 中 confusion matrix 的估计方法？\nQ5: AI (Claude) 是否辅助了定理证明？\n\n## 主要优势\n\n1. 系统性和完整性：7 种 DAG topologies 的统一分析框架属首次\n2. 理论深度：在已声明假设范围内证明严谨完整\n3. 实践导向：ASV 框架和 Algorithm 1 提供可操作的 correction decision procedure\n4. 诚实的局限性讨论\n5. 广泛的数值验证"
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
    "project": "causal_annot_error_attrib",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 项，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性审查\n\n## 总体评分\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] Theorem 1 仅对 proportional effects 成立，一般情形缺少证明\n- Theorem 1 的 envelope monotonicity 严格限于 proportional effects (f = λg)。对于 non-proportional effects，论文仅依赖 20,000 random triples 的数值验证。proportional effects 假设在 NLP 因果推断场景中几乎不可验证也很少成立。\n\n**N2** [critical] Non-differential misclassification 假设与论文自身 stress test 结果矛盾\n- 论文自身 stress test (Appendix B.6) 在 K≥3 exposure topology 下发现 13.3% baseline violation rate。正文 p.4 承认 \"sign reversal recurs in 14/16 K≥3 exposure configurations at α=0.01 structured departures\"，sign-flip rate 从 2.6% 上升到 9.67%（α=0.20）。核心假设在目标场景中系统性被违反。\n\n**N3** [critical] Conjecture 1 未被证明但在实践框架中承担关键角色\n- Conjecture 1 仅有数值验证（545,945 adversarial curves），但 ASV 框架和 Algorithm 1 的 practical recommendations 隐含依赖此 conjecture。\n\n## Should-Fix 问题\n\n**W1** Linear SEM 假设对 NLP 场景的适用性讨论不足\n**W2** FWL futility result 的 novelty 和 framing 需要更精确——本质是 FWL 定理的直接推论，\"provably ineffective\" framing 可能夸大 novelty\n**W3** C(δ) = (1-δ)I + δC₀ 参数化的局限性——实际 LLM annotation 中误分类模式可能随整体质量变化而定性改变\n**W4** 实证验证的数据集多样性不足——仅文本分类、仅 LLM annotator、K 最大 10\n**W5** Theorem 2 的 symmetric confusion matrix 假设过强——Remark 5 指出实际 LLM confusion matrices 偏离对称性显著（median d_rel=0.33）\n\n## Questions\n\nQ1: Proposition 1(a) 的 B_OV 依赖于未观测 A，如何基于 observable quantities 验证？\nQ2: DAG misspecification 下 Algorithm 1 的后果？\nQ3: IV topology 在 NLP 中的实际使用频率？\nQ4: ClinicalBERT Case Study 中 confusion matrix 的估计方法？\nQ5: AI (Claude) 是否辅助了定理证明？\n\n## 主要优势\n\n1. 系统性和完整性：7 种 DAG topologies 的统一分析框架属首次\n2. 理论深度：在已声明假设范围内证明严谨完整\n3. 实践导向：ASV 框架和 Algorithm 1 提供可操作的 correction decision procedure\n4. 诚实的局限性讨论\n5. 广泛的数值验证"
  }
}
```

</details>

---


### Tool result

_source line 1905 · 2026-05-24T04:09:30.564293+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1412
}
```

</details>

---


### Assistant

_source line 1906 · 2026-05-24T04:09:34.465396+00:00_

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


## Round 190

## Round 190

2 recorded events


### User

_source line 1907 · 2026-05-24T04:09:37.104138+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审查完成摘要**：

- **Overall**: 3.5 / 5 (Borderline Conference)
- **Soundness**: 4/5 — 证明在已声明假设内完整正确
- **Excitement**: 3.5/5 — 系统性 taxonomy 和 ASV 框架有价值，但 linear SEM 限制了实际影响
- **Reproducibility**: 4/5

**3 个 Must-Fix 问题**：
1. Theorem 1 仅对 proportional effects 成立，一般情形缺少证明
2. Non-differential misclassification 假设与论文自身 stress test 矛盾（14/16 K≥3 配置在 α=0.01 下违反）
3. Conjecture 1 未证明但在 ASV 框架和 Algorithm 1 中承担关键角色

**5 个 Should-Fix 问题**：Linear SEM 适用性讨论不足、FWL futility framing 夸大、C(δ) 参数化局限、数据集多样性不足、Theorem 2 symmetric 假设过强。

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

_source line 1908 · 2026-05-24T04:09:42.743408+00:00_

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


## Round 191

## Round 191

2 recorded events


### User

_source line 1909 · 2026-05-24T04:10:56.211872+00:00_

[Reviewer 1 审稿结果]:
以下是我（Reviewer 1）对 Reviewer 2 各条意见的逐条回应：

---

## Must-Fix 回应

**[PARTIALLY AGREE] R2-N1: 核心贡献的增量性**

同意部分：R2 正确指出 ASV 在方法论深度上有限（本质上是 one-parameter sweep 找 sign-flip threshold），Algorithm 1 确实更像 practical guideline 而非 algorithmic contribution。将 ASV 与 E-values 类比（Section 3.3, p.5-6）确实可能误导读者高估其方法论创新。

反驳部分：R2 低估了从 K=2 到 K≥3 推广的理论意义。关键区别不仅是"更多类别"，而是 **K≥3 引入了质性新现象**：
- **Structural dichotomy**（Section 4.2, p.7, Table 1）：K=2 时所有 non-exposure topologies 都保证 0% sign-flip rate，但 K≥3 时 exposure topology 的 sign-flip rate 达到 83.6%（Table 1），confounding/mediation 的 violation rate 也非零（13.7% under realistic accuracy, p.7）。这不是 Brenner (1993) 的简单推广——Brenner 只处理了 polytomous confounder 的偏差放大，未覆盖 7 种 topology 的差异化行为。
- **FWL futility result**（Section 3, p.3; Appendix B.2）：TeBlunthuis (2024) 仅覆盖 4 种 binary DAG，未建立 correction method 的 topology-dependent effectiveness 分析。论文的 FWL invariance observation 虽然在理解 FWL 的读者看来不惊讶（我在自己的审稿中也指出了这点，见我的 W2），但将其系统化并与 PP++/DSL/MC-SIMEX 五种校正方法的实证对比联系起来，是对文献的实质贡献。

总结：贡献 1 的核心价值在于 K≥3 的质性新现象而非量的推广；贡献 2-3 的方法论深度确实有限。建议将此定性为 "solid systematic contribution with novel qualitative insights" 而非 "methodological breakthrough"。

---

**[AGREE] R2-N2: Conjecture 1 未证明削弱理论完整性**

完全同意。我在自己的审稿中将此列为 N3 (critical)。Conjecture 1（general K≥3 approximate envelope monotonicity）是 ASV 框架的理论基础之一，留为 conjecture 确实是完整性缺陷。数值验证虽然广泛（545,945 adversarial curves, maximum step deviation < 0.04, Appendix B.12 p.28），但不能替代证明。

补充我自己的发现：Appendix B.12 Table 11 显示 K=7 时 worst-case magnitude deviation 为 0.060*（non-monotone direction），这比 K=3 的 0.003 大一个数量级。这暗示随 K 增大，approximate monotonicity 的 approximation quality 可能恶化，进一步削弱 conjecture 在 large-K settings（如 HumAID K=10）下的可靠性。

---

**[PARTIALLY AGREE] R2-N3: Real-world empirical validation 不充分**

同意部分：R2 正确指出论文的 "empirical validation"（Section 4）主要是 theory-MC consistency check（Table 1: analytical predictions match MC estimates, MAPE 1.6%），而非在真实因果推断问题上的 end-to-end 验证。对投向 EMNLP 的论文，这确实偏理论。

反驳部分：
- 论文确实包含了超越 pure simulation 的实证成分：Section 4.4 (p.7-8) 使用 23 real LLM confusion matrices 验证 bias ranking 和 sign-flip predictions；Appendix B.18 (p.31) 的 Political Ad Tone Classification case study 使用 ASV 诊断真实 annotated variable 的脆弱性；Appendix B.19-B.20 (p.32) 的 end-to-end demonstration 和 semi-real case study 使用 production LLM confusion matrices。
- 但 R2 的核心批评成立：这些 case studies 仍然是 **retrospective analysis**（已知 ground truth 或 simulated outcomes），而非在一个 researcher 不知道 ground truth 的真实因果推断场景中展示框架的 decision-making value。一个理想的 validation 应该是：对一个有 gold-standard causal effect 的 NLP 任务，展示使用 Algorithm 1 routing 后的 corrected estimate 比 naive estimate 更接近 ground truth。

总结：论文的实证成分比 R2 描述的更丰富，但 end-to-end real-world validation 的缺失确实是一个合理的 weakness。我在自己的审稿中将此列为 W4 (should-fix) 而非 critical，因为对理论导向的论文，simulation + real confusion matrices 的验证已经达到了合理的 evidence bar。

---

## Should-Fix 回应

**[AGREE] R2-W1: 非差异性误分类假设讨论不足**

完全同意，且我认为这个问题比 R2 的 "should-fix" 分级更严重。我在自己的审稿中将此列为 **N2 (critical)**，因为论文自身的 stress test (Appendix B.6, Table 9, p.27) 显示 13.3% baseline violation rate 和 14/16 K≥3 configurations 在 α=0.01 下出现 structured departures（正文 p.4）。假设在目标场景中被系统性违反，理论结果的实际指导价值需要更诚实的讨论。

---

**[AGREE] R2-W2: Linear SEM 限制**

同意。我将此列为 W1 (should-fix)。论文 Appendix B.7 (p.26) 的 nonlinear DGP 测试提供了部分 robustness evidence（structured violation models 下 sign-flip rate 仍为 0%），但 linear bias expressions 与 nonlinear bias magnitudes 的对应关系未被建立。

---

**[PARTIALLY AGREE] R2-W3: 相关工作缺口**

- **Cinelli & Hazlett (2020) partial R² 对比**：同意。论文在 Section 2 (p.3) 引用了 Cinelli and Hazlett (2020) 的 "partial-R² bounds"，但未对比 ASV 与 partial R² sensitivity analysis 的方法论异同。这是一个合理的相关工作缺口。
- **Regression calibration**：同意。这是 measurement error 文献中的经典方法（Carroll et al., 2006），论文在 Section 4.5 (p.8) 讨论了 5 种 correction methods（Naive plug-in, MLA, DSL, MC-SIMEX, PP++）但未提及 regression calibration。虽然 regression calibration 主要适用于 continuous measurement error，但讨论其不适用于 categorical misclassification 的原因也是有价值的。
- **PPI++ theoretical guarantees**：部分不同意。论文在 Section 4.5 和 Table 5 (p.8) 对 PPI++ 进行了相当详细的实证对比，且在 Appendix B.15 (p.30) 分析了 PPI++ 在不同 gold label fractions 下的 RMSE sensitivity。PPI++ 的理论 guarantees（Angelopoulos et al., 2023）确实值得在 Related Work 中讨论，但这不是重大遗漏。

---

**[REBUT] R2-W4: Abstract "annotation quality is the wrong thing to worry about" overclaiming**

不同意这是 overclaiming。原文完整句子是（Abstract, p.1）："When LLM-generated annotations feed into causal inference, annotation quality is the wrong thing to worry about—what matters is whether errors attenuate, amplify, or reverse the treatment effect estimate." 这是一个 **framing statement**，意思是"关注 accuracy 不如关注 error structure"，而非"annotation quality 不重要"。论文的全部内容恰恰支持这一 framing：Table 1 (p.7) 显示同一 confusion matrix 在不同 topologies 下效果截然不同（confounding: 100% sign preservation vs. IV: 52.6% sign flip），这确实说明 aggregate accuracy 不是正确的 metric。

此外，这种 counterintuitive hook 是合理的写作策略，符合 NLP 顶会论文的叙事惯例（先提出 provocative claim，再用论文内容支撑）。只要正文不 overclaim（而正文确实给出了 nuanced discussion），abstract 中的 framing 是可接受的。

---

**[REBUT] R2-W5: Figure 2 信息密度过高**

不同意。Figure 2 (p.5) 展示了 100,000 random K=3 confusion matrices 下 7 种 topologies 的 bias distribution，通过并排 histogram 高效传达了 structural dichotomy 的核心 insight（exposure: 83.6% sign reversal vs. 其他 topologies: 0-2.1%）。替代方案（如拆分为多个 sub-figures）会占用更多版面但不增加信息量。在 8 页正文限制下，Figure 2 的密度是合理的。

---

## 总结

R2 的 3 个 Must-Fix 中，N2（Conjecture 1）我完全同意，N1（增量性）和 N3（实证不足）我部分同意。R2 的 Should-Fix 中，W1-W3 我基本同意，W4-W5 我不同意。

我与 R2 的主要分歧在于：(1) 我认为 K≥3 sign reversal 是质性新现象而非纯增量推广，这赋予贡献 1 独立的理论价值；(2) 我认为 non-differential 假设被违反（我的 N2）比 R2 给出的 W1 分级更严重——这是影响接收决定的 critical issue，而非 should-fix。

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

_source line 1910 · 2026-05-24T04:11:54.871308+00:00_

收到 Reviewer 1 的交叉回应。分析收敛状态前，需要确认 Reviewer 2 对 Reviewer 1 的交叉回应是否已到。

**Reviewer 1 交叉回应摘要：**

| R2 意见 | R1 判定 | 关键分歧 |
|---------|---------|---------|
| N1 增量性 | PARTIALLY AGREE | R1 认为 K≥3 sign reversal 是质性新现象，非纯量推广 |
| N2 Conjecture 1 | **AGREE** | 完全一致，R1 补充 K=7 deviation 恶化证据 |
| N3 实证不足 | PARTIALLY AGREE | R1 认为实证成分比 R2 描述的更丰富，但同意缺 end-to-end validation |
| W1 非差异性假设 | **AGREE + 升级** | R1 认为应为 critical 而非 should-fix |
| W2 Linear SEM | AGREE | 一致 |
| W3 相关工作 | PARTIALLY AGREE | Cinelli & Hazlett 同意，PPI++ 部分不同意 |
| W4 Abstract overclaim | **REBUT** | R1 认为是合理 framing，非 overclaiming |
| W5 Figure 2 密度 | **REBUT** | R1 认为在 8 页限制下密度合理 |

**初步收敛判断：**
- **已达共识**（5 项）：Conjecture 1 未证明、非差异性假设问题、Linear SEM 限制、部分相关工作缺口、end-to-end validation 缺失
- **待调和分歧**（3 项）：增量性程度、Abstract framing、Figure 2 密度
- **严重度分歧**（1 项）：R1 将 W1（非差异性假设）升级为 critical，R2 仅列为 should-fix

等待 Reviewer 2 的交叉回应到达后进行最终收敛判断。如果两份交叉回应在核心问题上分歧有限，可直接进入报告合成阶段（无需第三轮）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 192

## Round 192

16 recorded events


### User

_source line 1911 · 2026-05-24T04:11:54.874798+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

## Must-Fix 问题

**[AGREE] R1-N1: Theorem 1 仅对 proportional effects 成立**

同意这是一个重要的理论完整性缺陷。我在自己的 N2 中也独立提出了 Conjecture 1 未证明的问题。补充两点：

1. 论文的理论贡献结构是分层的：K=2 exact（所有 effects, Theorem 1 的 proportional case 之外还有 Appendix A.5 的一般 K=2 证明）→ K=3 symmetric exact（Theorem 2）→ general K≥3 conjecture。前两层是完整的，但最重要的一般情形留为 conjecture。
2. 不过，数值验证的覆盖面值得肯定：100,000 Dirichlet-sampled matrices + 545,945 adversarial curves（Appendix A.11）+ 20,000 random triples for non-proportional effects。在计算数学中，这种规模的数值验证通常被视为 strong evidence，尽管不能替代证明。

R1 说 "proportional effects 假设在 NLP 因果推断场景中几乎不可验证也很少成立"——这个判断我认为稍有过强。proportional effects 意味着所有类别的 treatment effect 按同一比例缩放，这在某些场景下是合理的近似（如 ordinal 分类变量的单调效应）。但确实不能假设它普遍成立。

**[AGREE] R1-N2: Non-differential 假设与 stress test 结果的张力**

同意这个发现值得关注。我在自己的 W1 中也提出了类似问题，但 R1 的论证更尖锐——直接用论文自身的数值来构成内部矛盾：

- 正文 p.4 承认 14/16 K≥3 exposure configurations 在 α=0.01 下出现 sign reversal
- Appendix B.6 Table 8 显示 sign-flip rate 随结构偏离增大
- Appendix B.26 的 Y-stratified permutation test 在 VAST 数据上 13.3% violation rate

这构成了一个内部一致性问题：论文的理论框架依赖 non-differential 假设，但论文自己的实证检验显示该假设在目标场景中存在非平凡的违反率。

不过，有一个 nuance 需要补充：B.26 的结果显示 violation 主要是 "content-dependent"（topic/sentiment driven）而非纯粹的 outcome-dependent。论文区分了这两类偏离——content-dependent violation 在某些因果推断 design 下（如控制了 topic 后）可能不构成 non-differential 假设的违反。但这个论点在论文中没有被充分发展。

**[AGREE] R1-N3: Conjecture 1 在实践框架中的关键角色**

完全同意。与我的 N2 一致。补充一个具体的依赖链：

Conjecture 1（envelope monotonicity）→ ASV 的 vulnerability ranking 有序性 → Algorithm 1 Step 1 的 risk level 判断 → 整个 correction routing 的正确性。

如果 Conjecture 1 存在反例（即某些 confusion matrix 下 ASV 的 topology ordering 反转），Algorithm 1 可能给出错误的 correction 建议。虽然 545,945 adversarial curves 未发现反例，但 "absence of evidence is not evidence of absence"。

论文应至少讨论：如果 Conjecture 1 的 approximate monotonicity 在实践中偶尔被违反（ε < 0.017, Appendix A.11），Algorithm 1 的 robustness 如何？这种小幅违反是否会导致 correction routing 的质变？

## Should-Fix 问题

**[AGREE] R1-W1: Linear SEM 假设对 NLP 场景的适用性**

同意。与我的 W2 一致。Appendix B.7 和 B.14 的 logistic regression 测试结果实际上更 damaging than the paper acknowledges：matrix-based correction 的 bias reduction 在 logistic regression 下 ≈ 0%，且 FWL invariance 在形式上不再成立但实际上 correction 仍然无效。这意味着论文的 practical recommendations 对非线性模型几乎完全不适用。

**[REBUT] R1-W2: FWL futility result 的 novelty**

部分不同意 R1 的判断。

R1 认为 FWL invariance result "本质是 FWL 定理的直接推论"。从纯数学角度看，proof 确实只需 3-4 步（见 Appendix B.2, page 23-24）。但我认为这个 result 的价值不在证明技巧而在 observation：

1. **实践意义显著**：NLP 社区中很多研究者在使用 LLM annotation 做因果推断时，直觉上会认为"先用 confusion matrix 校正标注再跑回归"是正确的 pipeline。FWL futility result 明确地告诉他们：对于 4 种 covariate topology（confounding, mediation, collider, M-bias），这个 pipeline 在 OLS 下是 provably useless。这个 negative result 本身就有传播价值。
2. **非显然性**：虽然对熟悉 FWL 的统计学家来说这个结果"not surprising"，但 (a) 之前没有人在 annotation error 的语境下明确指出这一点；(b) Table 6 (Appendix B.2) 的数值验证表明 correction 确实不改变 OLS 估计——这对 NLP practitioner 来说是 counterintuitive 的。

但我同意 R1 的 framing 建议：论文应将此定位为 "a practically important observation that follows from FWL" 而非暗示这是一个 deep theoretical contribution。"Provably ineffective" 的措辞是准确的，但论文在 contribution list 中将其与 bias taxonomy 和 ASV 并列，可能给人过高的 novelty 印象。

**[AGREE] R1-W3: C(δ) 参数化的局限性**

同意。C(δ) = (1-δ)I + δC₀ 假设误分类模式在质量变化时保持结构不变（只是 intensity 变化），但实际上 LLM 在不同 prompt / temperature / few-shot 设置下的 confusion matrix 结构可能发生定性变化（例如：某些类别对的混淆可能在高质量设置下消失而新的混淆出现）。这使得 ASV 的 "minimum perturbation to sign flip" 解释可能不准确——实际路径上的 confusion matrix 变化可能不沿 C(δ) 的线性插值路径。

不过，这是 sensitivity analysis 中常见的单参数 parameterization 问题（E-values 也有类似局限——用单一 risk ratio 参数化 unmeasured confounding），不是本文特有的缺陷。论文应 acknowledge 这个 limitation 但不必彻底改变方法。

**[AGREE] R1-W4: 数据集多样性不足**

同意。与我的 N3 一致。仅 3 个文本分类数据集（HumAID, VAST, CivilComments），最大 K=10，全部是英文，全部用 LLM annotator。缺少：
- 非文本模态（如 image classification + VLM annotator）
- 更大 K（如 K=20+）
- 非英文数据
- 非 LLM annotator（如 crowdsourcing）

不过，考虑到论文的理论导向性质和页数限制，要求全面的 empirical 覆盖可能不合理。但至少应在 limitations 中明确 acknowledge 这些缺口。

**[REBUT] R1-W5: Theorem 2 的 symmetric assumption 过强**

部分不同意。

R1 引用 Remark 5 (Appendix A.7) 指出实际 LLM confusion matrices 偏离对称性显著（median relative Frobenius distance d_rel = 0.30-0.38）。但论文对此有清晰的 awareness：

1. Theorem 2 的定位是 **theoretical anchor**，不是对实际 confusion matrices 的直接建模。论文明确说："Theorem 2 serves as a theoretical anchor: exact monotonicity is achievable at K=3 under symmetric C_s"（page 6）。
2. 对一般非对称 matrices，论文提供了 Conjecture 1 + 数值验证。Remark 5 本身就是作者用来论证"需要从 symmetric 推广到 general case"的 motivation。
3. Appendix A.11 的 adversarial monotonicity verification 不依赖对称性假设——它在 general column-stochastic matrices 上测试。

所以 Theorem 2 的对称假设不是一个"应该被修复"的问题，而是理论推导中的一个 stepping stone，论文对此处理得当。真正的问题仍是 Conjecture 1 未证明（R1-N3 / 我的 N2）。

## Questions 回应

**Q1（B_OV 可观测性）**: 好问题。Proposition 1(a) 中 B_OV = Cov(g(A), f(A)) / Var(f(A))，涉及真实 A 而非 observed A*。论文在 Section 3.3 用 bootstrap（从 A* 通过 C⁻¹ 估计 A 的分布）来近似这个量，但未明确讨论这个 "间接可观测" 问题的 estimation error propagation。这确实是 ASV 实用性的一个潜在瓶颈。

**Q2（DAG misspecification）**: 论文假设 DAG 已知，但 DAG discovery 本身在有 measurement error 下也会受影响。这是一个 important practical concern，应在 limitations 中讨论。

**Q3（IV topology 在 NLP 中的频率）**: 我同意 IV 在 NLP 中很少使用。但论文将 IV 列为理论上最脆弱的拓扑（vulnerability ranking 最高），这个结果对少数使用 IV 的研究者来说仍有重要警示价值。IV 在社会科学因果推断中有广泛使用，NLP 标注可能进入这些 pipeline。

**Q5（AI 辅助定理证明）**: Section D 的披露是"coding, designing and refactoring" + "drafting and revising paper sections"。是否辅助了定理证明未明确说明。ACL 2025/2026 的 AI assistance policy 要求"describe the use in sufficient detail"，如果 AI 确实参与了 proof development，应明确披露。这是一个 ethics concern 而非 technical concern。

## 总结

R1 和我（R2）的审稿意见在多个关键问题上 converge：
1. **Conjecture 1 未证明**（R1-N3 / R2-N2）——双方一致认为是 critical
2. **Non-differential 假设的实际合理性**（R1-N2 / R2-W1）——R1 用论文自身数据构成了更尖锐的论证
3. **Linear SEM 限制**（R1-W1 / R2-W2）——双方一致
4. **Empirical validation 深度**（R1-W4 / R2-N3）——双方一致

我和 R1 的主要分歧在：
- **FWL futility result**（R1-W2）：R1 认为 novelty 不足，我认为 observation 的实践价值大于证明技巧的深度
- **Theorem 2 symmetric assumption**（R1-W5）：R1 认为过强，我认为作为 theoretical stepping stone 定位合理
- **增量性的严重程度**：R1 侧重方法严谨性（对已有结论的信心），我侧重新颖性（贡献边界的清晰度），但结论相近

总体判断不变：**3.5 (Borderline Conference)**，推荐 Findings。


---

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条交叉回应。

核心共识：R1 和 R2 在 Conjecture 1 未证明、non-differential 假设合理性、linear SEM 限制、empirical validation 深度四个问题上独立收敛。主要分歧在 FWL futility result 的 novelty 判断和 Theorem 2 symmetric assumption 的严重程度。两位 reviewer 均给出 3.5 (Borderline Conference)，推荐 Findings。

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

_source line 1912 · 2026-05-24T04:12:09.520197+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
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
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1913 · 2026-05-24T04:12:09.570848+00:00_



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

_source line 1914 · 2026-05-24T04:12:12.284239+00:00_

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

_source line 1915 · 2026-05-24T04:12:12.284577+00:00_

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

_source line 1916 · 2026-05-24T04:12:12.385225+00:00_

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

_source line 1917 · 2026-05-24T04:12:12.385533+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T04:01:11.083606+00:00\", \"completed_at\": \"2026-05-24T04:06:03.765082+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本（title + intro + related work），无 display item。ACL 格式下属常规布局，但若能在 page 2 加入一个 teaser figure 或 motivating example 会增强审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 的 2×4 小面板中轴标签和拓扑名称字号偏小（估计 ~7pt），建议适当增大子图或减少面板数量以提升可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"纯文本页（Theorem 1-2 + Conjecture + Remark），无 display item。内容为数学定理密集段落，属理论推导例外，不影响评分\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4 尺寸较小（约占单栏宽度的 80%，高度约 1/4 页），数据点标签紧凑。作为正文最后一张图，适当放大可增强视觉冲击力\"}, {\"severity\": \"warning\", \"dimension\": \"page 23\", \"message\": \"附录单页堆叠 4 个 display items（Figure 5 + Figure 6 + Table 5 + Figure 7），版面极度拥挤，每个图表都偏小。建议将 Figure 5-6 或 Figure 7 移至下一页以改善可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 28-29\", \"message\": \"Tables 12-13 列数多（6-8 列），字号较小，数字密度高。审稿人快速扫阅时可能跳过细节。建议考虑合并或精简列数\"}, {\"severity\": \"info\", \"dimension\": \"page 35\", \"message\": \"Algorithm 1 占页面约 60%，底部约 40% 空白。附录末页不影响评分，但如有待补充内容可利用此空间\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1918 · 2026-05-24T04:12:21.680271+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1919 · 2026-05-24T04:12:21.781772+00:00_

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
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Section 3.2 已添加 ASV 替代讨论。"
    resolution_round: 3

  - id: R1-W3
    category: experiments
    severity: should-fix
    summary: "实证验证不完整：缺少商业 LLM"
    status: in_progress
    first_raised_round: 1
    last_seen_round: 22
    mentions:
      - roun
…[truncated 22383 chars]

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


### Tool call

_source line 1920 · 2026-05-24T04:12:42.186134+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
  "offset": "0",
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
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1921 · 2026-05-24T04:12:42.187009+00:00_

0	---
1	name: review-director-session-start
2	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
3	priority: 9
4	scope: global
5	tags:
6	- workflow
7	- review
8	- session
9	version: 3
10	roles:
11	- review_director
12	---
13	
14	# Review Director Session 启动流程（圆桌会议模式）
15	
16	## 初始化
17	
18	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
19	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
20	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
21	4. 向用户简要汇报：
22	   - **投稿目标**：venue 和 deadline
23	   - **论文状态**：当前草稿位置和版本
24	   - **资料完整性**：提交的材料是否齐全
25	   - **下一步**：即将开始的圆桌审稿流程
26	
27	## 评审流程（收到论文提交后执行）
28	
29	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
30	
31	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
32	2. 确认目标投稿 venue（从提交消息中获取）
33	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
34	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
35	   - `"&lt;venue name> 2026 submission deadline"`
36	   - `"&lt;venue name> 2026 author guidelines"`
37	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
38	5. 提取当前版本的格式要求：
39	   - 页数限制（正文 / 附录 / 参考文献）
40	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
41	   - 匿名规则（double-blind / single-blind / open）
42	   - 附录规则（是否允许、是否参与审稿）
43	   - 引用格式（natbib / biblatex / 特定 .bst）
44	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
45	
46	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
47	
48	### Step 0.5 — 决定 Reviewer 编排
49	
50	根据 venue 类型和论文特点，决定：
51	- 需要几个 Reviewer（1-5 人）
52	- 每个 Reviewer 的审查侧重
53	
54	参考：
55	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
56	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
57	- **Workshop / 短文**：1 人（全面审查）
58	
59	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
60	
61	### Step 0.6 — 外部审稿线（与 Step 1 并行）
62	
63	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
64	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
65	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
66	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
67	- 如果到 Step
…[truncated 3284 chars]

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
