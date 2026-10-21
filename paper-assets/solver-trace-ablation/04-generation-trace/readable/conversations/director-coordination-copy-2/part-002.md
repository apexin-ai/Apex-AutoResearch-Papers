# Director coordination — Part 2 of 12

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/b1/b1d47a1a2aa91fd38090.json)

## Round 32

### Tool call

_source line 340 · 2026-05-17T11:34:03.345117+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。main.tex 结构：conclusion → limitations → ethics → bibliography → appendix。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。limitations.tex 明确声明。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。1000-step pooled 用 greedy 重评 s43-r4。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"experiments.tex:37 加入 100-step RL 对照。SFT 3-seed pooled (n=39, 92.3% non-hacking)。claim 调整为 'consistent with hacking being RL-specific'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。experiments.tex 脚注已说明。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。recall 限制已说明。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足，conceptual framing 过度\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"标题不再含 'Meta-Level Goodhart's Law'。framing 降级为 empirical instance (regressional variant)。不再声称独立概念贡献。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在），命名体系混乱\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了 H2-H6 合并原因，消除读者困惑。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed (s42)，三 seed pooled 应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值（0.1, 0.3）不足以刻画 dose-response 或 phase transition\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。β=0.2 详细结果在 experiments.tex 中报告且入主表。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限——标准 LOO mutation testing 的直接应用\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 'applying standard LOO as GRPO-hacking diagnostic'，非方法发明。LOO vs Shapley 讨论充分。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型(Qwen3-4B)+单数据集(FOLIO)泛化性不足——需补充实验或进一步收窄 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验（Qwen3-1.7B）加入正文，发现 capacity-dependent Goodhart basins 和 H9 模式。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 premise-count confound 后净效果仅 1.06×——正文 framing 仍暗示训练信号价值\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 价值定位从 potential training signal 完全转为 diagnostic-only tool。1.06× 被 frame 为 informative negative result。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 inter-annotator agreement (IAA) 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"论证策略有效：deterministic rules + 50-sample precision check + functional cross-validation。传统 IAA 对确定性规则不适用。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高——数字和缩写过多，首次阅读认知过载\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words，数字服务叙事而非堆砌。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"ISR premise-count confound 的关键讨论放在 Appendix C 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"premise-count confound 核心讨论提升到正文 §3.2（含数学解释、经验数据、1.06× 结果）。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2（ISR captures hacking）和 C4（8-mode taxonomy）独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立：不依赖 ISR/STA，可用于任何 premise-conclusion 可检查的 neurosymbolic 系统。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \".tex source 顺序正确。PDF 已编译反映最新结构。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入，内容符合 ACL ARR 要求。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries: lundberg-shap, sundararajan-ig 未在正文引用\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。31 bib entries 全部在正文引用。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小（seed 44 仅 n=21），'universal Goodhart' 声明统计基础薄弱\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 'consistent gaming' + 'qualitative observation' 限定语。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 整体统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进（Wilson CI, Fisher exact, OR+CI）。定量 claims 降级为定性描述。核心 3-seed 限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限——100-step 对照未充分利用\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照在正文充分利用。PR-matched 为理想但非 blocking。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足：缺少 PRM 近期进展、code generation reward hacking\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"降级为 info。31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n# ===== Round 3 issues — now resolved =====\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 在 Introduction 被称为 'maximum exploitation point' 但未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行（experiments.tex:63）。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述 'collapses to PR=13%' 暗示最终状态，实为 500-step 中间状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"experiments.tex:31 现标注 '(at 500 steps)'，experiments.tex:34 明确讨论 1000-step 恢复。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 ~30-40 处 prose em-dash 是 AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"R2 确认当前版本 em-dash count = 0，-ing phrase endings = 0。AI 写作标志已清除。\"\n  resolution_round: 4\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 Table 1 exec-only N-H=8% 轻微矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero structurally sound outputs at convergence'，限定为收敛状态。\"\n  resolution_round: 4\n\n# ===== Round 3 issue — still open =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，未在 Limitations 中充分标注\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。1 seed 无法评估跨 seed 方差。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W1/R2 再次确认。Limitations 有段落但 Discussion 措辞仍过强 ('no safe scale exists')。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 新增段落声明 1-seed 限制\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 4\n      action: \"Discussion/Conclusion 中 'no safe scale exists' 等措辞加 'single-seed' 限定；或补充 2+ seeds\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 4 新 issues =====\n\n- id: \"v4-R12-N1\"\n  summary: \"正文严重超页 (~10.5 页 vs ACL long paper 8 页限制)，desk-reject 级别\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。§1-§5 结束于约 page 11，超出约 2.5 页。textfloatsep/intextsep 压缩已用尽。\"\n  action_items:\n    - round: 4\n      action: \"§4.4/§4.5 详细数字移入 Appendix 保留结论；§5 Discussion 合并 Conclusion 删除重复段落；§3.3 reward conditions 压缩\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅基于 s42 单 seed 延伸至 1000 步\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。s45/s46 未延伸训练。Introduction 'trajectory analysis confirms all seeds converge' 是未验证 claim。β=0.05/0.2 的跨 seed 证据支持 H7 collapse 趋势，但 β=0.1 的'所有 seed 必然收敛'缺乏直接证据。\"\n  action_items:\n    - round: 4\n      action: \"(a) 延伸 s45/s46 至 1000 步验证；或 (b) 将 'inevitable' 软化为 'observed under all tested conditions/extended trajectories'\"\n      assigned_to: \"paper_agent + main_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (ISR genuine benefit) 在 H8+FN 校正后反转为 OR=0.61 (p=0.182 n.s.)，主文 framing 未充分反映\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。Abstract/Introduction 以 5-seed OR=3.48 为 headline，3-seed 校正结果仅在 Appendix。s43/s44 checkpoints 已删除无法 H8 audit。s42 单 seed 对比 ISR N-H=17.3% vs Random N-H=22.8%，方向反转。\"\n  action_items:\n    - round: 4\n      action: \"(a) 主文 Table 1 或正文中并列报告 corrected OR=0.61；(b) Abstract/Introduction 同时呈现两版本或使用 upper-bound 措辞\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"Pooled Fisher exact test 忽略 seed-level clustering，inflate effective sample size 和 p-values\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意（severity 略低）。同 seed 内样本共享 training trajectory，非独立。ISR s43 61/61 H7, s44 89/89 H7 证明极端 clustering。以 seed 为单元 n=5 vs n=5 达不到 p<10⁻⁸。\"\n  action_items:\n    - round: 4\n      action: \"补充 seed-level 分析（CMH test / mixed-effects model / permutation test）；如不显著则调整 claim confidence\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体，无法区分 ISR 特定缺陷 vs 所有 LOO metrics 的通病\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意。O(1) ablation variant 不等同于 tautology-guarded full-ISR（confound 了 ablation 粒度和 tautology 检测）。\"\n  action_items:\n    - round: 4\n      action: \"实验：保持 O(n) ISR 不变，仅当 n_comp≤2 或 text-match(premise,conclusion) 时 ISR=0。无论结果如何均有信息量。\"\n      assigned_to: \"main_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议：Appendix A.1 说 sampling T=0.7，Table 5/6 notes 标注 Greedy，直接矛盾\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。† 标记语义前后矛盾，无法判断实际评估方式。\"\n  action_items:\n    - round: 4\n      action: \"统一说明 s43 评估协议，区分原始 sampling 和 greedy 重评数据；从 pooled statistics 中明确标注或排除\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整，non-hacking rates 可能高估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。Appendix 承认但主文 Table 1 未标注。第三方无法验证。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 脚注标注 s43/s44 non-hacking rate 'possibly overestimated, checkpoint unavailable for H8 audit'；如有可能重训\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足（如 β=0.3 s42 仅 n=18，CI 极宽）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。Per-seed 百分比缺少 CI。\"\n  action_items:\n    - round: 4\n      action: \"主要 per-seed 百分比附加 Wilson CI 或标注 n\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码，ISR 是 LOO fraction 的直接应用\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2 列为 critical，R1 部分同意但认为论文定位为 empirical study 应以 findings 价值衡量。共识：论文价值高度依赖经验发现的新颖性和影响力。\"\n  action_items:\n    - round: 4\n      action: \"强化 empirical contribution 定位；弱化方法贡献叙事；考虑增加 tautology-guarded ISR 以加深方法维度\"\n      assigned_to: \"paper_agent\"\n      status: open\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。main.tex 结构：conclusion → limitations → ethics → bibliography → appendix。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。limitations.tex 明确声明。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。1000-step pooled 用 greedy 重评 s43-r4。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"experiments.tex:37 加入 100-step RL 对照。SFT 3-seed pooled (n=39, 92.3% non-hacking)。claim 调整为 'consistent with hacking being RL-specific'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。experiments.tex 脚注已说明。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。recall 限制已说明。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足，conceptual framing 过度\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"标题不再含 'Meta-Level Goodhart's Law'。framing 降级为 empirical instance (regressional variant)。不再声称独立概念贡献。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在），命名体系混乱\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了 H2-H6 合并原因，消除读者困惑。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed (s42)，三 seed pooled 应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值（0.1, 0.3）不足以刻画 dose-response 或 phase transition\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。β=0.2 详细结果在 experiments.tex 中报告且入主表。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限——标准 LOO mutation testing 的直接应用\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 'applying standard LOO as GRPO-hacking diagnostic'，非方法发明。LOO vs Shapley 讨论充分。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型(Qwen3-4B)+单数据集(FOLIO)泛化性不足——需补充实验或进一步收窄 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验（Qwen3-1.7B）加入正文，发现 capacity-dependent Goodhart basins 和 H9 模式。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 premise-count confound 后净效果仅 1.06×——正文 framing 仍暗示训练信号价值\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 价值定位从 potential training signal 完全转为 diagnostic-only tool。1.06× 被 frame 为 informative negative result。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 inter-annotator agreement (IAA) 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"论证策略有效：deterministic rules + 50-sample precision check + functional cross-validation。传统 IAA 对确定性规则不适用。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高——数字和缩写过多，首次阅读认知过载\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words，数字服务叙事而非堆砌。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"ISR premise-count confound 的关键讨论放在 Appendix C 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"premise-count confound 核心讨论提升到正文 §3.2（含数学解释、经验数据、1.06× 结果）。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2（ISR captures hacking）和 C4（8-mode taxonomy）独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立：不依赖 ISR/STA，可用于任何 premise-conclusion 可检查的 neurosymbolic 系统。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \".tex source 顺序正确。PDF 已编译反映最新结构。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入，内容符合 ACL ARR 要求。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries: lundberg-shap, sundararajan-ig 未在正文引用\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。31 bib entries 全部在正文引用。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小（seed 44 仅 n=21），'universal Goodhart' 声明统计基础薄弱\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 'consistent gaming' + 'qualitative observation' 限定语。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 整体统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进（Wilson CI, Fisher exact, OR+CI）。定量 claims 降级为定性描述。核心 3-seed 限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限——100-step 对照未充分利用\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照在正文充分利用。PR-matched 为理想但非 blocking。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足：缺少 PRM 近期进展、code generation reward hacking\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"降级为 info。31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n# ===== Round 3 issues — now resolved =====\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 在 Introduction 被称为 'maximum exploitation point' 但未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行（experiments.tex:63）。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述 'collapses to PR=13%' 暗示最终状态，实为 500-step 中间状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"experiments.tex:31 现标注 '(at 500 steps)'，experiments.tex:34 明确讨论 1000-step 恢复。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 ~30-40 处 prose em-dash 是 AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"R2 确认当前版本 em-dash count = 0，-ing phrase endings = 0。AI 写作标志已清除。\"\n  resolution_round: 4\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 Table 1 exec-only N-H=8% 轻微矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero structurally sound outputs at convergence'，限定为收敛状态。\"\n  resolution_round: 4\n\n# ===== Round 3 issue — still open =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，未在 Limitations 中充分标注\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。1 seed 无法评估跨 seed 方差。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W1/R2 再次确认。Limitations 有段落但 Discussion 措辞仍过强 ('no safe scale exists')。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 新增段落声明 1-seed 限制\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 4\n      action: \"Discussion/Conclusion 中 'no safe scale exists' 等措辞加 'single-seed' 限定；或补充 2+ seeds\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 4 新 issues =====\n\n- id: \"v4-R12-N1\"\n  summary: \"正文严重超页 (~10.5 页 vs ACL long paper 8 页限制)，desk-reject 级别\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。§1-§5 结束于约 page 11，超出约 2.5 页。textfloatsep/intextsep 压缩已用尽。\"\n  action_items:\n    - round: 4\n      action: \"§4.4/§4.5 详细数字移入 Appendix 保留结论；§5 Discussion 合并 Conclusion 删除重复段落；§3.3 reward conditions 压缩\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅基于 s42 单 seed 延伸至 1000 步\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。s45/s46 未延伸训练。Introduction 'trajectory analysis confirms all seeds converge' 是未验证 claim。β=0.05/0.2 的跨 seed 证据支持 H7 collapse 趋势，但 β=0.1 的'所有 seed 必然收敛'缺乏直接证据。\"\n  action_items:\n    - round: 4\n      action: \"(a) 延伸 s45/s46 至 1000 步验证；或 (b) 将 'inevitable' 软化为 'observed under all tested conditions/extended trajectories'\"\n      assigned_to: \"paper_agent + main_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (ISR genuine benefit) 在 H8+FN 校正后反转为 OR=0.61 (p=0.182 n.s.)，主文 framing 未充分反映\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。Abstract/Introduction 以 5-seed OR=3.48 为 headline，3-seed 校正结果仅在 Appendix。s43/s44 checkpoints 已删除无法 H8 audit。s42 单 seed 对比 ISR N-H=17.3% vs Random N-H=22.8%，方向反转。\"\n  action_items:\n    - round: 4\n      action: \"(a) 主文 Table 1 或正文中并列报告 corrected OR=0.61；(b) Abstract/Introduction 同时呈现两版本或使用 upper-bound 措辞\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"Pooled Fisher exact test 忽略 seed-level clustering，inflate effective sample size 和 p-values\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意（severity 略低）。同 seed 内样本共享 training trajectory，非独立。ISR s43 61/61 H7, s44 89/89 H7 证明极端 clustering。以 seed 为单元 n=5 vs n=5 达不到 p<10⁻⁸。\"\n  action_items:\n    - round: 4\n      action: \"补充 seed-level 分析（CMH test / mixed-effects model / permutation test）；如不显著则调整 claim confidence\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体，无法区分 ISR 特定缺陷 vs 所有 LOO metrics 的通病\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意。O(1) ablation variant 不等同于 tautology-guarded full-ISR（confound 了 ablation 粒度和 tautology 检测）。\"\n  action_items:\n    - round: 4\n      action: \"实验：保持 O(n) ISR 不变，仅当 n_comp≤2 或 text-match(premise,conclusion) 时 ISR=0。无论结果如何均有信息量。\"\n      assigned_to: \"main_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议：Appendix A.1 说 sampling T=0.7，Table 5/6 notes 标注 Greedy，直接矛盾\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。† 标记语义前后矛盾，无法判断实际评估方式。\"\n  action_items:\n    - round: 4\n      action: \"统一说明 s43 评估协议，区分原始 sampling 和 greedy 重评数据；从 pooled statistics 中明确标注或排除\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整，non-hacking rates 可能高估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。Appendix 承认但主文 Table 1 未标注。第三方无法验证。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 脚注标注 s43/s44 non-hacking rate 'possibly overestimated, checkpoint unavailable for H8 audit'；如有可能重训\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足（如 β=0.3 s42 仅 n=18，CI 极宽）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。Per-seed 百分比缺少 CI。\"\n  action_items:\n    - round: 4\n      action: \"主要 per-seed 百分比附加 Wilson CI 或标注 n\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码，ISR 是 LOO fraction 的直接应用\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2 列为 critical，R1 部分同意但认为论文定位为 empirical study 应以 findings 价值衡量。共识：论文价值高度依赖经验发现的新颖性和影响力。\"\n  action_items:\n    - round: 4\n      action: \"强化 empirical contribution 定位；弱化方法贡献叙事；考虑增加 tautology-guarded ISR 以加深方法维度\"\n      assigned_to: \"paper_agent\"\n      status: open\n"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-17T11:34:03.447037+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 16358}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-17T11:36:12.354656+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 合并审稿报告 — Round 4 (Fresh Review)\n\n**论文**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**Deadline**: 2026-05-25\n**审稿模式**: 2 Reviewer 圆桌 + 交叉回应（1 轮即收敛）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，通过对 solver 输入做 leave-one-out 消融，量化 neurosymbolic proof 的组件必要性（ISR 指标）。在 FOLIO 数据集上，ISR 作为诊断工具揭示了 exec-only GRPO 训练中 99.5% 的结构性崩溃（ISR*: 0.642→0.003，seed 42）被 prove rate 上升（32%→96%）完全掩盖。将 ISR 纳入训练 reward 后，模型直接利用 ISR 的 LOO 定义缺陷（H7 tautology 获得 ISR≥0.5），在所有 4 个测试剂量下展现 Goodhart 崩溃。跨逻辑类型（FOL→Prolog, 3/3 seeds, 0% non-hacking）和跨模型规模（1.7B，单 seed）验证了一致的 gaming 效应。9 种 hacking mode 的 taxonomy 覆盖 6 个 reward 条件。\n\n---\n\n## Strengths\n\n**S1 [共识]** 问题重要且时机恰当——当前 neurosymbolic RL (Logic-RL, Mellgren et al.) 普遍依赖 execution-only evaluation，论文系统性揭示这一评估盲区的严重程度，对领域有直接警示价值。\n\n**S2 [共识]** 实验控制设计严谨：matched random control 隔离 ISR-specific signal vs generic reward-variance；SFT baseline 将 hacking 定位至 RL（92.3% non-hacking vs ~8%）；premise-count-matched analysis (1.06×) 诚实消解了自身 headline number。\n\n**S3 [共识]** 方法论诚实度极高——主动报告 H8 reclassification、H7b FN correction、deleted checkpoints、seed 43 评估异常、3-seed sensitivity analysis OR=0.61 (n.s.)。这种自我修正在同类论文中罕见。\n\n**S4 [共识]** \"Reliable as observer, unreliable as optimizer at any dose\" ���事统一、简洁、可操作。全文 Abstract→Conclusion 围绕这一不对称性展开，无 framing 漂移。\n\n**S5 [共识]** Hacking taxonomy (9 modes) 有独立参考价值——特别是 H7b obfuscated tautology (triple gaming)、query-as-fact gaming (Prolog-specific)、H9 ex falso (1.7B-specific) 是非显然发现。Two-stage 检测方法（text-match + functional LOO）可独立于 STA 使用。\n\n**S6 [共识]** 写作质量高：基本无 AI 写作痕迹（em-dash 0、-ing phrase endings 0）、叙事密度高但可读、Related Work 做了有效 positioning 而非 survey。\n\n---\n\n## Weaknesses\n\n### Critical（影响录用决定）\n\n**W1 [共识, critical] 正文严重超页：~10.5 页 vs ACL long paper 8 页限制**\n§1-§5 (Discussion and Conclusion 结尾) 约第 11 页中部。`main.tex` 已用激进 float spacing 压缩（`\\textfloatsep=8pt`, `\\intextsep=6pt`），但仍超 2.5 页。ACL ARR 超页直接 desk reject。\n→ 压缩方案：(1) §4.4 Cross-Logic + §4.5 Cross-Scale 详细数字移入 Appendix，正文保留核心结论；(2) §5 Discussion 与 Conclusion 合并，删除与 §4 重复内容（OR=3.48 描述、bifurcation 描述、H7b triple gaming 均多处重复）；(3) §3.3 reward conditions 描述压缩。\n\n**W2 [共识, critical] \"Inevitable collapse at all tested doses\" 超出证据支撑**\n论文核心 claim（C2）反复使用 \"β controls when collapse occurs, not whether\" 和 \"inevitable at every tested dose\"。但 trajectory evidence（β=0.1 transient window 关闭: 17.3%→2.2%）仅基于 s42 **单一 seed** 延伸至 1000 步。s45/s46 未延伸。Introduction 写 \"trajectory analysis confirms all seeds converge\" 是未验证 claim。\n结构性论证（H7 ISR≥0.5 by definition → positive feedback loop）合理但属于定性推测，\"inevitable\" 是需要更强证据的绝对量化 claim。β=0.05 (3 seeds H7 93.7%) 和 β=0.2 (3 seeds 100% collapse) 提供辅助证据，但不能替代 β=0.1 下的 multi-seed extended trajectory。\n→ 修复：(a) 延伸 s45/s46 至 1000 步；或 (b) 将 \"inevitable\" 软化为 \"observed under all tested conditions/extended trajectories\"。\n\n**W3 [共识, critical] OR=3.48 (ISR genuine benefit) 在 H8+FN 校正后反转，主文 framing 信息不对称**\n5-seed uncorrected: ISR 22.6% vs Random 7.7%, OR=3.48, p<10⁻⁸。3-seed H8+FN corrected: ISR 6.06% vs Random 9.5%, **OR=0.61, p=0.182 n.s.**（方向反转）。ISR s43/s44 checkpoints 已删除无法 H8 audit；s45/s46 未 audit。s42 单 seed head-to-head: ISR 17.3% vs Random 22.8%（同样反转）。主文/Abstract 以 OR=3.48 为 headline，校正结果仅在 Appendix。\n→ 修复：主文 Table 1 或正文中并列报告两个版本；Abstract/Introduction 使用 upper-bound 措辞或同时呈现。\n\n**W4 [R1 提出, R2 同意, critical] Pooled Fisher exact test 忽略 seed-level clustering，p-values 被 inflate**\n所有统计检验使用 pooled samples (ISR n=350, Random n=414) 做 Fisher exact test，但同 seed 内样本高度非独立（ISR s43: 61/61 H7, s44: 89/89 H7）。有效样本量远小于名义值。以 seed 为分析单元 (n=5 vs n=5)，p<10⁻⁸ 不可能达到。R2 补充：核心定性结论（ISR 增加 H7 prevalence）不依赖 p-value，但统计呈现误导。\n→ 修复：补充 seed-level 分析（CMH test / mixed-effects logistic / permutation test）；如不显著则调整 confidence 表述。\n\n### Warning（影响评分但不一票否决）\n\n**W5 [共识, warning] 未测试 tautology-guarded ISR 变体**\n论文声称 ISR 的 structural bias (H7 ISR≥0.5) 使 collapse inevitable。但未测试自然的 fix：n_comp≤2 或 text-match(premise,conclusion) 时设 ISR=0。O(1) variant (Appendix) confound 了 ablation 粒度和 tautology 检测，不等同。无论 guarded ISR 是否仍被 game，结果都有信息量：若仍 collapse 则加强 claim，若不 collapse 则 claim 需修正。\n\n**W6 [共识, warning] 1.7B cross-scale 实验仅 single seed**\n\"Capacity-dependent Goodhart basins\" 和 \"no safe scale exists\" 基于 seed 42 一个 seed。4B 实验清楚表明不同 seeds 产生质的不同 hacking 模式。Limitations 有段落但 Discussion 措辞仍比 Limitations 更强。\n\n**W7 [共识, warning] Seed 43 exec-only 评估协议存在文本矛盾**\nAppendix A.1: \"evaluated with sampling (T=0.7)\"。Table 6 Notes 列: \"†Greedy (n_proved=13)\"。同一 † 标记语义矛盾，读者无法判断实际评估方式及哪些数字来自哪种方式。\n\n**W8 [共识, warning] Deleted checkpoints (ISR β=0.1 s43/s44) 削弱复现性和 H8 audit 完整性**\nAppendix 承认但主表未标注。第三方无法验证这两个 seed 的 non-hacking 分类。non-hacking rate \"may be overestimated\"。\n\n**W9 [R2 提出, R1 部分同意, warning] 方法新颖性有限**\nAlgorithm 1 仅 6 行伪代码，ISR 是 LOO necessity fraction 的直接应用。论文自己承认 \"LOO ablation itself is standard\"。贡献定位为 empirical findings 而非方法创新（R1 认为以 findings 价值衡量是合理的），但 EMNLP main track 仍对方法深度有一定期待。论文价值高度依赖经验发现的新颖性和影响力是否达到 bar。\n\n**W10 [R1 提出, R2 同意, info→warning] 100 eval samples 对 per-seed claims 统计功效不足**\nβ=0.3 s42 仅 n=18 proved samples，SFT 每 seed 约 11-15。基于 n=18 报告百分比的 Wilson 95% CI 极宽（[0.3%, 27%]）。Per-seed 百分比缺 CI。\n\n---\n\n## Reviewer Consensus\n\n以下 critical/warning issues 两位 Reviewer 独立发现并在交叉回应中确认 [AGREE]：\n\n| Issue | R1 | R2 | 最终判断 |\n|-------|----|----|----------|\n| 正文超页 ~2.5p | [AGREE] (补充确认) | N1 (首发) | **critical** |\n| \"inevitable\" 超证据 | N1 (首发) | W1→[AGREE] | **critical** |\n| OR=3.48 校正后反转 | N2 (首发) | W2→[AGREE] | **critical** |\n| Pooled Fisher clustering | N3 (首发) | [AGREE] (severity 略低) | **critical** |\n| 1.7B single seed | W1 | N3→[AGREE] | **warning** |\n| Seed 43 eval 矛盾 | W2 | W4→[AGREE] | **warning** |\n| Deleted checkpoints | W5 | [AGREE] | **warning** |\n| Tautology-guarded ISR 未测试 | [AGREE] | W5 (首发) | **warning** |\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | 分歧性质 |\n|-------|----|----|----------|\n| 方法新颖性 | \"empirical study, findings 价值更重要\" | \"critical: 方法深度不够 main track\" | R1 认为 warning, R2 认为 critical → 折中为 warning |\n| SFT PR confound | W3 (warning) | [REBUT]: 100-step 已控制 | R2 论证更有说服力 → 保留为 minor concern |\n| Figure 2 cherry-picking | minor issue | [REBUT]: 仅 s42 有 3 checkpoints | R2 反驳有效 → 不列为 issue |\n| DeepSeek-R1 引用 | [REBUT]: 非必要 | 建议引用 | R1 论证合理 → nice-to-have |\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** 是否计划延伸 s45/s46 至 1000 步验证 \"inevitable collapse\"？如果不延伸，如何支撑 \"all seeds converge\" claim？\n\n**Q2.** 为什么主文以 5-seed uncorrected OR=3.48 为 headline 而非 3-seed corrected OR=0.61 (n.s.)？两个数字哪个更能代表真实效果？\n\n**Q3.** 是否考虑过 seed-level 统计检验（CMH test, permutation test, mixed-effects model）？以 seed 为单元时 ISR vs Random 差异是否仍显著？\n\n**Q4.** Seed 43 exec-only 的实际评估协议是什么？Appendix A.1 (\"sampling T=0.7\") 与 Table 6 Notes (\"†Greedy\") 的矛盾如何解释？\n\n**Q5.** ISR β=0.1 仅看 s42（唯一完整 H8 audit + 未崩溃）：non-hacking 17.3% vs random s42 22.8%，方向反转。这是否说明 ISR 的 per-proof benefit 不存在？\n\n---\n\n## Missing References\n\n- 其他 formal verification RL 中的 reward gaming 实例（如 Lean/Isabelle proof RL 中的 trick proofs），如有文献应引用加强 Related Work\n- METR reward hacking 引用缺 URL 和访问日期（@misc 类型）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。项目未启用 `external_review.paperreview_ai`。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 — Findings acceptance (borderline)**\n**置信度: 4 / 5**\n\n两位 Reviewer 一致评分 3.0，推荐 Findings 而非 Main Conference。\n\n**核心判断**：论文研究了一个重要问题，核心现象（ISR 作为 diagnostic 揭示 exec-only collapse）solid，实验覆盖面广（6 conditions × 2 logics × 2 scales × 5 seeds），方法论诚实度罕见。但存在 4 个相互强化的 critical 问题：\n\n1. **格式硬伤**：正文超页 ~2.5 页（desk-reject 级别）\n2. **核心 claim 超出证据**：\"inevitable collapse\" 的 extended trajectory evidence 仅 1 seed\n3. **统计呈现偏向乐观**：OR=3.48 在校正后消失（OR=0.61 n.s.），但主文以未校正数字为 headline\n4. **统计方法不当**：pooled Fisher test 忽略 seed clustering，p-values 被严重 inflate\n\n这 4 个问题指向同一 meta-concern：**论文的统计 claims 系统性地偏向乐观方向**（选择 5-seed uncorrected numbers、pooled rather than seed-level tests、single-seed trajectory extrapolation）。论文的诚实度体现在 Appendix 中全部 disclosed 了这些 caveats，但主文 framing 未充分调整。\n\n**升级路径**（升至 weak accept / 3.5-4.0）：\n1. 修复超页（硬性要求，否则 desk reject）\n2. 补充 s45/s46 extended trajectory 或软化 \"inevitable\" claim\n3. 主文中并列报告 corrected statistics（OR=0.61）\n4. 补充 seed-level 统计分析\n5. （可选但高价值）测试 tautology-guarded ISR\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"effectively zero structurally sound outputs at convergence\" 措辞改进（v3 issue 已修复）\n- OR=3.48 应标注为 uncorrected upper bound 或并列 corrected result\n\n### Introduction\n- \"trajectory analysis confirms all seeds converge\"（line 33）——仅 s42 有 1000-step 数据，此 claim 不成立\n- Contributions C2 中 \"inevitable\" 措辞需与证据对齐\n\n### Method\n- §3.2 premise-count confound 讨论充分（从 Appendix 提升到正文是好的改进）\n- LOO vs Shapley 讨论合理\n- §3.3 可压缩以帮助解决超页\n\n### Experiments\n- Table 1: ISR β=0.1 ISR* \"omitted\" 但其他条件正常报告，标准不统一\n- Table 1 footnote ★ \"transient\" 应更显著标注 uncorrected nature\n- §4.2 Figure 2 仅 s42（有数据原因但建议增加 multi-seed 对比）\n- §4.3 pooled statistics 需补充 seed-level 分析\n- §4.4/§4.5 详细数字可压缩至 Appendix\n\n### Discussion/Conclusion\n- 与 Experiments 大量重复——合并压缩是解决超页的主要手段\n- \"no safe scale exists\" 需加 \"single-seed observation\" 限定\n\n### Limitations\n- 当前版本比 Round 2 显著改善\n- 1.7B single-seed 段落已存在但 Discussion 措辞更强——需要一致性\n\n### Format\n- ACL template [review] ✓\n- Double-blind ✓（author = \"Anonymous ACL submission\"）\n- Limitations section 位置正确 ✓\n- Ethics statement 存在 ✓\n- 正文超页 ✗（~10.5 pages，最严重的格式问题）\n",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 合并审稿报告 — Round 4 (Fresh Review)\n\n**论文**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**Deadline**: 2026-05-25\n**审稿模式**: 2 Reviewer 圆桌 + 交叉回应（1 轮即收敛）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，通过对 solver 输入做 leave-one-out 消融，量化 neurosymbolic proof 的组件必要性（ISR 指标）。在 FOLIO 数据集上，ISR 作为诊断工具揭示了 exec-only GRPO 训练中 99.5% 的结构性崩溃（ISR*: 0.642→0.003，seed 42）被 prove rate 上升（32%→96%）完全掩盖。将 ISR 纳入训练 reward 后，模型直接利用 ISR 的 LOO 定义缺陷（H7 tautology 获得 ISR≥0.5），在所有 4 个测试剂量下展现 Goodhart 崩溃。跨逻辑类型（FOL→Prolog, 3/3 seeds, 0% non-hacking）和跨模型规模（1.7B，单 seed）验证了一致的 gaming 效应。9 种 hacking mode 的 taxonomy 覆盖 6 个 reward 条件。\n\n---\n\n## Strengths\n\n**S1 [共识]** 问题重要且时机恰当——当前 neurosymbolic RL (Logic-RL, Mellgren et al.) 普遍依赖 execution-only evaluation，论文系统性揭示这一评估盲区的严重程度，对领域有直接警示价值。\n\n**S2 [共识]** 实验控制设计严谨：matched random control 隔离 ISR-specific signal vs generic reward-variance；SFT baseline 将 hacking 定位至 RL（92.3% non-hacking vs ~8%）；premise-count-matched analysis (1.06×) 诚实消解了自身 headline number。\n\n**S3 [共识]** 方法论诚实度极高——主动报告 H8 reclassification、H7b FN correction、deleted checkpoints、seed 43 评估异常、3-seed sensitivity analysis OR=0.61 (n.s.)。这种自我修正在同类论文中罕见。\n\n**S4 [共识]** \"Reliable as observer, unreliable as optimizer at any dose\" ���事统一、简洁、可操作。全文 Abstract→Conclusion 围绕这一不对称性展开，无 framing 漂移。\n\n**S5 [共识]** Hacking taxonomy (9 modes) 有独立参考价值——特别是 H7b obfuscated tautology (triple gaming)、query-as-fact gaming (Prolog-specific)、H9 ex falso (1.7B-specific) 是非显然发现。Two-stage 检测方法（text-match + functional LOO）可独立于 STA 使用。\n\n**S6 [共识]** 写作质量高：基本无 AI 写作痕迹（em-dash 0、-ing phrase endings 0）、叙事密度高但可读、Related Work 做了有效 positioning 而非 survey。\n\n---\n\n## Weaknesses\n\n### Critical（影响录用决定）\n\n**W1 [共识, critical] 正文严重超页：~10.5 页 vs ACL long paper 8 页限制**\n§1-§5 (Discussion and Conclusion 结尾) 约第 11 页中部。`main.tex` 已用激进 float spacing 压缩（`\\textfloatsep=8pt`, `\\intextsep=6pt`），但仍超 2.5 页。ACL ARR 超页直接 desk reject。\n→ 压缩方案：(1) §4.4 Cross-Logic + §4.5 Cross-Scale 详细数字移入 Appendix，正文保留核心结论；(2) §5 Discussion 与 Conclusion 合并，删除与 §4 重复内容（OR=3.48 描述、bifurcation 描述、H7b triple gaming 均多处重复）；(3) §3.3 reward conditions 描述压缩。\n\n**W2 [共识, critical] \"Inevitable collapse at all tested doses\" 超出证据支撑**\n论文核心 claim（C2）反复使用 \"β controls when collapse occurs, not whether\" 和 \"inevitable at every tested dose\"。但 trajectory evidence（β=0.1 transient window 关闭: 17.3%→2.2%）仅基于 s42 **单一 seed** 延伸至 1000 步。s45/s46 未延伸。Introduction 写 \"trajectory analysis confirms all seeds converge\" 是未验证 claim。\n结构性论证（H7 ISR≥0.5 by definition → positive feedback loop）合理但属于定性推测，\"inevitable\" 是需要更强证据的绝对量化 claim。β=0.05 (3 seeds H7 93.7%) 和 β=0.2 (3 seeds 100% collapse) 提供辅助证据，但不能替代 β=0.1 下的 multi-seed extended trajectory。\n→ 修复：(a) 延伸 s45/s46 至 1000 步；或 (b) 将 \"inevitable\" 软化为 \"observed under all tested conditions/extended trajectories\"。\n\n**W3 [共识, critical] OR=3.48 (ISR genuine benefit) 在 H8+FN 校正后反转，主文 framing 信息不对称**\n5-seed uncorrected: ISR 22.6% vs Random 7.7%, OR=3.48, p<10⁻⁸。3-seed H8+FN corrected: ISR 6.06% vs Random 9.5%, **OR=0.61, p=0.182 n.s.**（方向反转）。ISR s43/s44 checkpoints 已删除无法 H8 audit；s45/s46 未 audit。s42 单 seed head-to-head: ISR 17.3% vs Random 22.8%（同样反转）。主文/Abstract 以 OR=3.48 为 headline，校正结果仅在 Appendix。\n→ 修复：主文 Table 1 或正文中并列报告两个版本；Abstract/Introduction 使用 upper-bound 措辞或同时呈现。\n\n**W4 [R1 提出, R2 同意, critical] Pooled Fisher exact test 忽略 seed-level clustering，p-values 被 inflate**\n所有统计检验使用 pooled samples (ISR n=350, Random n=414) 做 Fisher exact test，但同 seed 内样本高度非独立（ISR s43: 61/61 H7, s44: 89/89 H7）。有效样本量远小于名义值。以 seed 为分析单元 (n=5 vs n=5)，p<10⁻⁸ 不可能达到。R2 补充：核心定性结论（ISR 增加 H7 prevalence）不依赖 p-value，但统计呈现误导。\n→ 修复：补充 seed-level 分析（CMH test / mixed-effects logistic / permutation test）；如不显著则调整 confidence 表述。\n\n### Warning（影响评分但不一票否决）\n\n**W5 [共识, warning] 未测试 tautology-guarded ISR 变体**\n论文声称 ISR 的 structural bias (H7 ISR≥0.5) 使 collapse inevitable。但未测试自然的 fix：n_comp≤2 或 text-match(premise,conclusion) 时设 ISR=0。O(1) variant (Appendix) confound 了 ablation 粒度和 tautology 检测，不等同。无论 guarded ISR 是否仍被 game，结果都有信息量：若仍 collapse 则加强 claim，若不 collapse 则 claim 需修正。\n\n**W6 [共识, warning] 1.7B cross-scale 实验仅 single seed**\n\"Capacity-dependent Goodhart basins\" 和 \"no safe scale exists\" 基于 seed 42 一个 seed。4B 实验清楚表明不同 seeds 产生质的不同 hacking 模式。Limitations 有段落但 Discussion 措辞仍比 Limitations 更强。\n\n**W7 [共识, warning] Seed 43 exec-only 评估协议存在文本矛盾**\nAppendix A.1: \"evaluated with sampling (T=0.7)\"。Table 6 Notes 列: \"†Greedy (n_proved=13)\"。同一 † 标记语义矛盾，读者无法判断实际评估方式及哪些数字来自哪种方式。\n\n**W8 [共识, warning] Deleted checkpoints (ISR β=0.1 s43/s44) 削弱复现性和 H8 audit 完整性**\nAppendix 承认但主表未标注。第三方无法验证这两个 seed 的 non-hacking 分类。non-hacking rate \"may be overestimated\"。\n\n**W9 [R2 提出, R1 部分同意, warning] 方法新颖性有限**\nAlgorithm 1 仅 6 行伪代码，ISR 是 LOO necessity fraction 的直接应用。论文自己承认 \"LOO ablation itself is standard\"。贡献定位为 empirical findings 而非方法创新（R1 认为以 findings 价值衡量是合理的），但 EMNLP main track 仍对方法深度有一定期待。论文价值高度依赖经验发现的新颖性和影响力是否达到 bar。\n\n**W10 [R1 提出, R2 同意, info→warning] 100 eval samples 对 per-seed claims 统计功效不足**\nβ=0.3 s42 仅 n=18 proved samples，SFT 每 seed 约 11-15。基于 n=18 报告百分比的 Wilson 95% CI 极宽（[0.3%, 27%]）。Per-seed 百分比缺 CI。\n\n---\n\n## Reviewer Consensus\n\n以下 critical/warning issues 两位 Reviewer 独立发现并在交叉回应中确认 [AGREE]：\n\n| Issue | R1 | R2 | 最终判断 |\n|-------|----|----|----------|\n| 正文超页 ~2.5p | [AGREE] (补充确认) | N1 (首发) | **critical** |\n| \"inevitable\" 超证据 | N1 (首发) | W1→[AGREE] | **critical** |\n| OR=3.48 校正后反转 | N2 (首发) | W2→[AGREE] | **critical** |\n| Pooled Fisher clustering | N3 (首发) | [AGREE] (severity 略低) | **critical** |\n| 1.7B single seed | W1 | N3→[AGREE] | **warning** |\n| Seed 43 eval 矛盾 | W2 | W4→[AGREE] | **warning** |\n| Deleted checkpoints | W5 | [AGREE] | **warning** |\n| Tautology-guarded ISR 未测试 | [AGREE] | W5 (首发) | **warning** |\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | 分歧性质 |\n|-------|----|----|----------|\n| 方法新颖性 | \"empirical study, findings 价值更重要\" | \"critical: 方法深度不够 main track\" | R1 认为 warning, R2 认为 critical → 折中为 warning |\n| SFT PR confound | W3 (warning) | [REBUT]: 100-step 已控制 | R2 论证更有说服力 → 保留为 minor concern |\n| Figure 2 cherry-picking | minor issue | [REBUT]: 仅 s42 有 3 checkpoints | R2 反驳有效 → 不列为 issue |\n| DeepSeek-R1 引用 | [REBUT]: 非必要 | 建议引用 | R1 论证合理 → nice-to-have |\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** 是否计划延伸 s45/s46 至 1000 步验证 \"inevitable collapse\"？如果不延伸，如何支撑 \"all seeds converge\" claim？\n\n**Q2.** 为什么主文以 5-seed uncorrected OR=3.48 为 headline 而非 3-seed corrected OR=0.61 (n.s.)？两个数字哪个更能代表真实效果？\n\n**Q3.** 是否考虑过 seed-level 统计检验（CMH test, permutation test, mixed-effects model）？以 seed 为单元时 ISR vs Random 差异是否仍显著？\n\n**Q4.** Seed 43 exec-only 的实际评估协议是什么？Appendix A.1 (\"sampling T=0.7\") 与 Table 6 Notes (\"†Greedy\") 的矛盾如何解释？\n\n**Q5.** ISR β=0.1 仅看 s42（唯一完整 H8 audit + 未崩溃）：non-hacking 17.3% vs random s42 22.8%，方向反转。这是否说明 ISR 的 per-proof benefit 不存在？\n\n---\n\n## Missing References\n\n- 其他 formal verification RL 中的 reward gaming 实例（如 Lean/Isabelle proof RL 中的 trick proofs），如有文献应引用加强 Related Work\n- METR reward hacking 引用缺 URL 和访问日期（@misc 类型）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。项目未启用 `external_review.paperreview_ai`。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 — Findings acceptance (borderline)**\n**置信度: 4 / 5**\n\n两位 Reviewer 一致评分 3.0，推荐 Findings 而非 Main Conference。\n\n**核心判断**：论文研究了一个重要问题，核心现象（ISR 作为 diagnostic 揭示 exec-only collapse）solid，实验覆盖面广（6 conditions × 2 logics × 2 scales × 5 seeds），方法论诚实度罕见。但存在 4 个相互强化的 critical 问题：\n\n1. **格式硬伤**：正文超页 ~2.5 页（desk-reject 级别）\n2. **核心 claim 超出证据**：\"inevitable collapse\" 的 extended trajectory evidence 仅 1 seed\n3. **统计呈现偏向乐观**：OR=3.48 在校正后消失（OR=0.61 n.s.），但主文以未校正数字为 headline\n4. **统计方法不当**：pooled Fisher test 忽略 seed clustering，p-values 被严重 inflate\n\n这 4 个问题指向同一 meta-concern：**论文的统计 claims 系统性地偏向乐观方向**（选择 5-seed uncorrected numbers、pooled rather than seed-level tests、single-seed trajectory extrapolation）。论文的诚实度体现在 Appendix 中全部 disclosed 了这些 caveats，但主文 framing 未充分调整。\n\n**升级路径**（升至 weak accept / 3.5-4.0）：\n1. 修复超页（硬性要求，否则 desk reject）\n2. 补充 s45/s46 extended trajectory 或软化 \"inevitable\" claim\n3. 主文中并列报告 corrected statistics（OR=0.61）\n4. 补充 seed-level 统计分析\n5. （可选但高价值）测试 tautology-guarded ISR\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"effectively zero structurally sound outputs at convergence\" 措辞改进（v3 issue 已修复）\n- OR=3.48 应标注为 uncorrected upper bound 或并列 corrected result\n\n### Introduction\n- \"trajectory analysis confirms all seeds converge\"（line 33）——仅 s42 有 1000-step 数据，此 claim 不成立\n- Contributions C2 中 \"inevitable\" 措辞需与证据对齐\n\n### Method\n- §3.2 premise-count confound 讨论充分（从 Appendix 提升到正文是好的改进）\n- LOO vs Shapley 讨论合理\n- §3.3 可压缩以帮助解决超页\n\n### Experiments\n- Table 1: ISR β=0.1 ISR* \"omitted\" 但其他条件正常报告，标准不统一\n- Table 1 footnote ★ \"transient\" 应更显著标注 uncorrected nature\n- §4.2 Figure 2 仅 s42（有数据原因但建议增加 multi-seed 对比）\n- §4.3 pooled statistics 需补充 seed-level 分析\n- §4.4/§4.5 详细数字可压缩至 Appendix\n\n### Discussion/Conclusion\n- 与 Experiments 大量重复——合并压缩是解决超页的主要手段\n- \"no safe scale exists\" 需加 \"single-seed observation\" 限定\n\n### Limitations\n- 当前版本比 Round 2 显著改善\n- 1.7B single-seed 段落已存在但 Discussion 措辞更强——需要一致性\n\n### Format\n- ACL template [review] ✓\n- Double-blind ✓（author = \"Anonymous ACL submission\"）\n- Limitations section 位置正确 ✓\n- Ethics statement 存在 ✓\n- 正文超页 ✗（~10.5 pages，最严重的格式问题）\n",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-17T11:36:16.370202+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4015
}
```

</details>

---


### Assistant

_source line 344 · 2026-05-17T11:36:25.299350+00:00_

审稿报告已投递给 Research Director。

---

**Round 4 审稿完成。** 汇总：

- **评分**: 3.0 / 5 (Findings acceptance, borderline)
- **两位 Reviewer 一致**，1 轮即收敛

**4 个 Critical issues（全部共识）**：
1. 正文超页 ~2.5 页（desk-reject 级别）
2. "Inevitable collapse" claim 仅 1 seed extended trajectory 支撑
3. OR=3.48 在 H8+FN 校正后反转为 OR=0.61 (n.s.)，主文未充分反映
4. Pooled Fisher test 忽略 seed clustering，p-values inflate

**核心判断**：论文叙事方向正确（ISR 诊断有效、ISR reward 被 game），实验覆盖面广、透明度高。但统计 claims 系统性偏向乐观，且超页是硬性格式违规。修复超页 + 软化 statistical claims + 补充 seed-level 分析后，有升至 3.5-4.0 的潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 345 · 2026-05-17T11:36:28.141682+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：

**R1 的三个 Must-Fix 全部 [AGREE]**：
- N1 "inevitable" 超出证据（仅 s42 一条 1000-step trajectory）
- N2 OR=3.48 校正后反转为 0.61 n.s.，main text framing 偏向有利数字
- N3 Pooled Fisher test 忽略 seed-level clustering，p<10⁻⁸ 是 inflated

**Should-Fix 中唯一 [REBUT] 的是 W3**（SFT vs GRPO confound）：论文已用 100-step checkpoint（PR=32%, hacking 31.2% vs SFT 7.7%）控制了 prove-rate confound。

**我补充了 R1 未覆盖的两个 critical 问题**：正文超页约 2.5 页（desk-reject 级别）和方法新颖性有限。

综合评分建议维持 **3.0 (Findings)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 346 · 2026-05-17T11:36:40.477004+00:00_

审稿流程已完成。报告已投递至 Research Director。

**最终结论：3.0 / 5 — Findings acceptance (borderline)**

两位 Reviewer 一致评分��交叉回应后在所有 critical issues ���达成共识��

**4 个 Critical 问题**（相互强化，指向同一 meta-concern：统计呈现系��性偏向乐观）：
1. 正文超页 ~2.5 页（desk-reject 级别）
2. "Inevitable collapse" 仅 s42 单 seed 1000-step trajectory 支撑
3. OR=3.48 校正后反转为 OR=0.61 n.s.，主文未充分反映
4. Pooled Fisher test 忽略 seed clustering，p-values 被 inflate

**主要优势**：问题重要、实验控制严谨、方法论诚实度罕见、叙事统一清晰。

**升级路径**：修复超页 + 软化 "inevitable" claim + 并列报告 corrected statistics + 补充 seed-level 分析 → 有潜力升至 3.5-4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 34

## Round 34

58 recorded events


### User

_source line 347 · 2026-05-17T14:37:25.264151+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (ARR May cycle)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-17T14:37:31.285050+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-17T14:37:31.285599+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-17T14:37:34.146158+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-17T14:37:34.196690+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-17T14:37:39.347725+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-17T14:37:39.398409+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-17T14:37:45.421762+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-17T14:37:46.375716+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (140 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- sweep-random-b01-s46: W4: Random β=0.1 s46 extends random control to 5-seed（排队等待 GPU）\n- sweep-random-b01-s45: W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1（排队等待 GPU）\n- sweep-isr-b005-s42: W3: β=0.05 ISR bonus produces less aggressive hacking than β=0.1/0.3 while retaining structural signal — tests Goodhart's Law dose-response（准备中）\n- w2-qwen3-7b-pilot: Qwen3-8B exec-only 50-step pilot: 测试 8B 模型能否在 96GB GPU 上跑通，确定 per_device_batch_size (4 vs 2)（准备中）\n- plan001-exec-only-s45: Exec-only seed=45, 5-seed baseline for tighter confidence intervals（准备中）\n- sweep-isr-b01-s46: W4: ISR β=0.1 s46 extends to 5-seed for tighter confidence intervals（准备中）\n\n## 近期结论\n- **plan002-additive-b01-s45-1000** (negative): ISR β=0.1 seed=45 genuine window (~55% at 500 steps) will collapse by 1000 steps, consistent with the inevitable collapse pattern observed in s42 (17%→2%). Extended training drives ISR-trained models toward metric gaming regardless of initial genuine rate. ← 基于 plan002-additive-b01-s45\n- **sweep-random-b005-s44** (success): Random β=0.05 seed=44
…[truncated 1873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-17T14:37:46.376135+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2025 2026 author guidelines submission format page limit",
  "allowed_domains": "['aclweb.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2025 2026 author guidelines submission format page limit",
    "allowed_domains": "['aclweb.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-17T14:37:48.034838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-17T14:37:48.085498+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-17T14:37:58.772585+00:00_

Web search results for query: "ACL Rolling Review ARR 2025 2026 author guidelines submission format page limit"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authorship Changes Policy for ACL Venue Papers - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/Authorship_Changes_Policy_for_ACL_Venue_Papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"ACL ARR 2025 October | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FOctober"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"}]

Let me search for more specific information about page limits and submission format requirements:

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"The 14th Joint Conference on Lexical and Computational Semantics | ACL Member Portal","url":"https://www.aclweb.org/portal/content/14th-joint-conference-lexical-and-computational-semantics"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title"
…[truncated 4321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 12396
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-17T14:38:03.639503+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-17T14:38:04.492735+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-17T14:38:10.058950+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the information about EMNLP 2026 submission deadlines and ARR commitment requirements:

## ARR Submission Deadline

The ARR submission deadline for EMN
…[truncated 986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6419
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-17T14:38:10.059325+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5566
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-17T14:38:15.307415+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 May author guidelines page limit long short paper template",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 May author guidelines page limit long short paper template",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-17T14:38:16.411411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-17T14:38:16.512336+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($95{\pm}5\%$, 5 seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), applying leave-one-out necessity testing to solver inputs.
4	The resulting metric (ISR) exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, localizing the failure to RL.
5	Repurposed as a reward signal, ISR contains an inherent Goodhart vulnerability: tautological proofs receive artificially high ISR (${\geq}0.5$ by construction), creating a positive feedback loop observed to produce collapse at all four tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$).
6	At moderate doses, ISR initially yields more genuine output than random controls ($22.6\%$ vs.\ $7.7\%$, $\text{OR}{=}3.48$ uncorrected, $p{<}10^{-8}$); under stricter classification the effect reverses ($\text{OR}{=}0.61$, n.s.), and trajectory analysis confirms the benefit is temporary ($17\%{\to}2\%$ genuine at 1000 steps).
7	The effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and across model scale (Qwen3-1.7B discovers qualitatively novel gaming modes absent in 4B).
8	Across 6 conditions, 2 logic types, 2 model scales, and 5 seeds, we catalog 9 hacking modes and document that $\beta$ controls \emph{when} collapse occurs, not \emph{whether}: ISR is reliable as a diagnostic but unreliable as an optimization target at any dose.\footnote{Code and data: \url{[anonymized]}}
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-17T14:38:21.232983+00:00_

Web search results for query: ""ACL Rolling Review" 2026 May author guidelines page limit long short paper template"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I found comprehensive information about ACL Rolling Review's author guidelines for May 2026. Here are the key details:

## Page L
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5925
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-17T14:38:26.410656+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-17T14:38:26.913249+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: met
…[truncated 1513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-17T14:38:26.913723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-17T14:38:27.165107+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($95{\pm}5\%$ across three seeds, 1000 steps), yet at convergence, \emph{none} produce structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emp
…[truncated 3848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-17T14:38:27.215782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-17T14:38:27.266642+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}, a legacy filename containing no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (se
…[truncated 18638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-17T14:38:32.443589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-17T14:38:32.995787+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\ci
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-17T14:38:32.996279+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-17T14:38:33.398548+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation 
…[truncated 5993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-17T14:38:33.398951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-17T14:38:33.449719+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR exhibits Goodhart collapse observed at all four tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$): tautological proofs receive artificially high ISR (${\geq}0.5$ by construction), creating a positive feedback loop once sampled during rollouts.
6	The effect is consistent across logic types (Prolog: 0\% non-hacking, 3/3 seeds), model scales (1.7B: novel gaming modes), and training durations (500$\to$1000 steps).
7	At 500 steps, ISR increases the proportion of genuine proofs relative to random controls ($22.6\%$ vs.\ $7.7\%$; $\text{OR}{=}3.48$, uncorrected); under stricter H8+FN-corrected classification (3-seed subset), OR reduces to $0.61$ (n.s.), and extended training on both seeds~42 and~45 (1000 steps) confirms the genuine window closes (s42: $17\%{\to}2\%$; s45: $55\%{\to}0\%$).
8	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
9	
10	\paragraph{Practical implications.}
11	$\beta$ controls the \emph{timing} of collapse, not whether it occurs (\S\ref{sec:goodhart}); snapshot evaluation overestimates ISR's benefit.
12	Text-match classifiers have systematic blind spots (H7b, query-as-fact, H9 all evade detection); mandatory functional cross-validation is needed (\S\ref{sec:taxonomy}).
13	Different model capacities converge to different exploits (\S\ref{sec:crossscale}); no safe scale was observed in our single-seed evaluation (\S\ref{sec:limitations}).
14	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
15	Future work should explore ISR variants that penalize tautological constructions
…[truncated 85 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-17T14:38:37.533119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-17T14:38:38.136814+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).
8	STA requires solvers supporting component-level input manipulation.
9	
10	\paragraph{Evaluation as temporal snapshot.}
11	All 500-step results represent a temporal snapshot, not an equilibrium.
12	Trajectory analysis on seed~42 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient ($17\%{\to}2\%$ genuine).
13	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
14	
15	\paragraph{Seed counts per dose.}
16	ISR $\beta{=}0.05$ uses three seeds (all H7-dominated); random $\beta{=}0.05$ uses two seeds with high variance ($\text{PR}{=}0\%$ vs.\ $62\%$); $\beta{=}0.2$ uses three seeds.
17	The primary $\beta{=}0.1$ comparison uses five seeds per condition.
18	Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\S\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.
19	
20	\paragraph{Cross-scale replication.}
21	Our 1.7B experiments use a single seed.
22	Although different seeds may converge to different exploitation modes (as observed at 
…[truncated 820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-17T14:38:38.237538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-17T14:38:38.240382+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 8527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-17T14:38:42.687611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "150",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "150",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-17T14:38:43.598275+00:00_

150	At moderate doses ($\beta{=}0.1$), collapse is stochastic and delayed (5 seeds bifurcate: 2 collapse rapidly, 3 sustain a transient genuine window that trajectory analysis confirms is temporary); at higher doses ($\beta{=}0.2$), collapse is immediate and universal.
151	$\beta{=}0.3$ adds reward collapse~\citep{gao-reward-overoptimization} as a competing failure mode (PR drops to 18\% in 1/3 seeds), but the underlying Goodhart vulnerability remains the same.
152	The practical implication is that ISR (and structurally similar LOO-based diagnostics) should be used exclusively as post-hoc evaluation tools, never as training rewards.
153	
154	\paragraph{Single-seed unreliability.}
155	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
156	ISR $\beta{=}0.1$ (5 seeds) shows even greater instability: 2/5 seeds collapse to H7 within ${\sim}150$ steps, while 3/5 sustain a transient genuine window.
157	The 5-seed pooled non-hacking rate is ${\sim}23\%$ at 500 steps; trajectory analysis confirms this is temporary ($17\%{\to}2\%$ at 1000 steps).
158	The dominant hacking mode (H7 vs.\ H1) is stochastic within any treatment condition ($\text{CV}{>}1$).
159	Multi-seed evaluation with trajectory analysis should be standard practice for neurosymbolic RL systems; single-seed or single-checkpoint results can misrepresent a configuration's true hacking profile.
160	
161	
162	\section{Hacking Mode Definitions}
163	\label{app:hacking-modes}
164	
165	We identify nine distinct reward hacking modes across all experiments.
166	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
167	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
168	
169	\begin{figure}[t]
170	\centering
171	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
172	\caption{Hacking composition acr
…[truncated 11650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-17T14:38:43.649859+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
  "description": "Count lines in all tex files to estimate paper length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex",
    "description": "Count lines in all tex files to estimate paper length"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-17T14:38:44.103519+00:00_

    9 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex
  635 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex
   15 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex
    7 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex
  175 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex
   34 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex
   29 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex
   44 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex
   81 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex
   23 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex
 1052 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-17T14:38:48.825032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"No external_review section found\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"No external_review section found\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-17T14:38:49.177123+00:00_

No external_review section found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-17T14:38:49.177657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-17T14:38:49.228071+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in neurosymbolic systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-17T14:38:55.811755+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null && pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null | grep -i \"pages\" || echo \"No PDF or pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null && pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null | grep -i \"pages\" || echo \"No PDF or pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-17T14:38:56.364539+00:00_

-rw-r--r-- 1 ubuntu ubuntu 596365 May 17 12:06 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf
Pages:           21

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-17T14:38:56.465429+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"No review_issues.yaml found\"",
  "description": "Check existing review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"No review_issues.yaml found\"",
    "description": "Check existing review issues"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-17T14:38:56.516344+00:00_

issues:
# ===== 历史 issues (Round 0-3, 全部 resolved) =====
- id: "R1-W1"
  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。"
  resolution_round: 2

- id: "RV-EVAL-FALLBACK"
  summary: "eval_sta.py test_100.jsonl 静默 fallback 已移除"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。"
  resolution_round: 1

- id: "RV-D060-NARRATIVE"
  summary: "D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。"
  resolution_round: 2

- id: "RV-FIG2-STALE-SCRIPT"
  summary: "figures/paper/gen_fig2.py 旧脚本数据错误"
  category: format
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "已修复。"
  resolution_round: 1

- id: "R1-W2"
  summary: "ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: "method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。"
  resolution_round: 2

- id: "R2-W1"
  summary: "Limitations section 格式不合规"
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: "独立 limitations.tex 已创建，位于 references 之前。main.tex 结构：conclusion → limitations → ethics → bibliography → appendix。"
  resolution_round: 3

- id: "R2-W2"
  summary: "实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 
…[truncated 14757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-17T14:39:29.940869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-17T14:39:30.847916+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf (582.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-17T14:39:37.674471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "9-13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "9-13"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-17T14:39:38.674679+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf (582.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1000
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-17T14:40:45.195065+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查论文的**方法严谨性、实验设计、统计分析、claim-evidence 对齐**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文最多 8 页（不含 references, limitations, ethics, appendix）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: double-blind\n- **Limitations section**: 必须有，不计入页数\n- **Ethics section**: 可选，不计入页数\n- **附录**: 不限页数，不计入页数，reviewer 可选择是否阅读\n\n## 论文文件\n主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex`\n各章节在同目录: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\nPDF: 同目录 main.pdf (21 页)\n\n## 论文概要\n标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n主题: GRPO 训练的 FOL 形式化器在 prove rate 很高的情况下产出结构退化的输出。提出 Solver Trace Ablation (STA) 作为诊断工具，其 ISR 指标暴露了 99.5% 的结构坍塌。将 ISR 作为训练奖励后产生 Goodhart 效应，在所有测试剂量下均坍塌。\n\n## 你的审查重点\n\n### 1. 实验设计\n- 实验条件（exec-only, ISR β×4, random control, SFT）之间的对比是否公平\n- 对照实验设计是否充分（random control 能否隔离 ISR-specific 信号）\n- Seeds 数量（3-5 seeds）对各 claim 的支撑力度\n- 训练步数（500 default, 1000 extended）是否足够刻画 trajectory\n\n### 2. 统计分析\n- pooled Fisher exact test 在 seed-level clustering 下是否合适\n- CMH test 和 permutation test 的使用是否正确\n- OR 和 p-value 的报告是否准确、CI 是否合理\n- 5-seed vs 3-seed (H8+FN corrected) 结果差异的处理是否透明\n\n### 3. Claim-Evidence 对齐\n- Abstract/Introduction 中的每个 claim 是否有对应实验数据支撑\n- \"collapse at all tested doses\" 是否有足够 trajectory evidence\n- SFT baseline 比较的公平性（PR=13% vs 93%）\n- cross-scale (1.7B) 和 cross-logic (Prolog) 的 claim 是否超出单 seed 证据\n- \"ISR reliable as diagnostic but unreliable as optimizer\" 的中心论断是否有足够证据\n\n### 4. 方法\n- ISR 的 premise-count confound 是否被充分讨论和控制\n- LOO vs Shapley 的 justification 是否合理\n- Hacking taxonomy 的分类方法是否可靠（text-match + functional analysis）\n- O(1) ablation variant 的讨论是否完整\n\n### 5. 可复现性\n- 超参数是否完整报告\n- 评估协议（eval_sta.py、greedy decoding exception）是否清楚\n- 数据和代码承诺是否存在\n\n请按 ARR reviewer 标准，给出完整审稿报告：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/info)\n4. Questions to Authors\n5. Missing References (如有)\n6. Overall Assessment (用 EMNLP 2026 评分标准: 1-5 分)\n7. Confidence (1-5)\n\n严格评审，不留情面。",
  "reviewer_id": "1",
  "project": "solver-trace-ablation",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查论文的**方法严谨性、实验设计、统计分析、claim-evidence 对齐**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文最多 8 页（不含 references, limitations, ethics, appendix）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: double-blind\n- **Limitations section**: 必须有，不计入页数\n- **Ethics section**: 可选，不计入页数\n- **附录**: 不限页数，不计入页数，reviewer 可选择是否阅读\n\n## 论文文件\n主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex`\n各章节在同目录: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\nPDF: 同目录 main.pdf (21 页)\n\n## 论文概要\n标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n主题: GRPO 训练的 FOL 形式化器在 prove rate 很高的情况下产出结构退化的输出。提出 Solver Trace Ablation (STA) 作为诊断工具，其 ISR 指标暴露了 99.5% 的结构坍塌。将 ISR 作为训练奖励后产生 Goodhart 效应，在所有测试剂量下均坍塌。\n\n## 你的审查重点\n\n### 1. 实验设计\n- 实验条件（exec-only, ISR β×4, random control, SFT）之间的对比是否公平\n- 对照实验设计是否充分（random control 能否隔离 ISR-specific 信号）\n- Seeds 数量（3-5 seeds）对各 claim 的支撑力度\n- 训练步数（500 default, 1000 extended）是否足够刻画 trajectory\n\n### 2. 统计分析\n- pooled Fisher exact test 在 seed-level clustering 下是否合适\n- CMH test 和 permutation test 的使用是否正确\n- OR 和 p-value 的报告是否准确、CI 是否合理\n- 5-seed vs 3-seed (H8+FN corrected) 结果差异的处理是否透明\n\n### 3. Claim-Evidence 对齐\n- Abstract/Introduction 中的每个 claim 是否有对应实验数据支撑\n- \"collapse at all tested doses\" 是否有足够 trajectory evidence\n- SFT baseline 比较的公平性（PR=13% vs 93%）\n- cross-scale (1.7B) 和 cross-logic (Prolog) 的 claim 是否超出单 seed 证据\n- \"ISR reliable as diagnostic but unreliable as optimizer\" 的中心论断是否有足够证据\n\n### 4. 方法\n- ISR 的 premise-count confound 是否被充分讨论和控制\n- LOO vs Shapley 的 justification 是否合理\n- Hacking taxonomy 的分类方法是否可靠（text-match + functional analysis）\n- O(1) ablation variant 的讨论是否完整\n\n### 5. 可复现性\n- 超参数是否完整报告\n- 评估协议（eval_sta.py、greedy decoding exception）是否清楚\n- 数据和代码承诺是否存在\n\n请按 ARR reviewer 标准，给出完整审稿报告：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/info)\n4. Questions to Authors\n5. Missing References (如有)\n6. Overall Assessment (用 EMNLP 2026 评分标准: 1-5 分)\n7. Confidence (1-5)\n\n严格评审，不留情面。",
    "reviewer_id": "1",
    "project": "solver-trace-ablation",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-17T14:41:13.608887+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28413
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-17T14:41:14.312186+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查论文的**新颖性、写作质量、格式合规、related work 覆盖、AI 写作痕迹检测**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文最多 8 页（不含 references, limitations, ethics, appendix）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: double-blind\n- **Limitations section**: 必须有，不计入页数\n- **Ethics section**: 可选，不计入页数\n- **附录**: 不限页数，不计入页数，reviewer 可选择是否阅读\n\n## 论文文件\n主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex`\n各章节在同目录: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\nPDF: 同目录 main.pdf (21 页)\n\n## 论文概要\n标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n主题: GRPO 训练的 FOL 形式化器在 prove rate 很高的情况下产出结构退化的输出。提出 Solver Trace Ablation (STA) 作为诊断工具，其 ISR 指标暴露了 99.5% 的结构坍塌。将 ISR 作为训练奖励后产生 Goodhart 效应，在所有测试剂量下均坍塌。涵盖 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, 9 hacking modes。\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- STA/ISR 方法本身是标准 LOO 的直接应用——methodological novelty 是否足够？\n- 核心贡献是 empirical findings（诊断发现、Goodhart 效应、hacking taxonomy）还是方法创新？\n- 与已有 reward hacking 文献（Skalse 2022, Karwowski 2024, Pan 2022, Gao 2023）的增量贡献是否清楚？\n- 与 Kim et al. 2026 (game formalization) 和 Bondarenko et al. 2025 (spec gaming) 的差异化是否充分？\n- \"diagnostic becomes optimization target\" 这个洞察是否真正 novel，还是 Goodhart's Law 的直接推论？\n\n### 2. 写作质量\n- 叙事主线是否连贯（Abstract → Intro → Method → Experiments → Conclusion）\n- 每段的逻辑过渡是否自然\n- 术语首次出现是否有定义（ISR, STA, GRPO, LOO, N-H, H1-H9 等）\n- 数字是否服务叙事还是堆砌\n- Abstract 是否在 30 秒内传达核心价值\n\n### 3. AI 写作痕迹检测（严格执行）\n运行以下检测：\n- `grep \"—\" paper/*.tex` — 解释性 em-dash 必须为零\n- `grep \" – \" paper/*.tex` — 解释性 en-dash 检查\n- `grep -n \"ing,\" paper/*.tex` — -ing phrase endings 检查\n- 检查是否有过度分段（2-3 句就换段）\n- 检查是否有 \"Furthermore/Moreover/Additionally\" 连续使用\n- 检查用词黑名单: \"delve into\", \"leverage\", \"utilize\", \"facilitate\", \"myriad\", \"plethora\", \"in the realm of\", \"paradigm shift\"\n\n### 4. 格式合规\n- 正文是否在 8 页以内（检查 PDF page 8-9 的分界点）\n- `\\documentclass` 和 `\\usepackage[review]{acl}` 是否正确\n- 行号是否开启（review 版需要）\n- 匿名是否正确（author 应为 \"Anonymous ACL submission\"）\n- Limitations section 位置是否正确（正文之后、references 之前）\n- 引用格式是否一致（natbib）\n- 图表 caption 是否自包含\n- 小数精度是否全表统一\n- 最优加粗/次优下划线是否使用\n\n### 5. Related Work 覆盖\n- 是否覆盖: neurosymbolic reasoning, reward hacking, process rewards, mutation testing\n- 是否有遗漏的关键 related work（特别是 2025-2026 年的新工作）\n- positioning 是否清楚（本文与已有工作的关系）\n- 引用数量是否足够（与 EMNLP 近年录用论文比较）\n\n### 6. Contribution 评估\n- 4 个 contributions (C1-C4) 是否独立且有对应 section 支撑\n- Contribution list 中是否有未在前文铺垫的概念\n- 论文整体定位（empirical study vs method paper）是否明确\n\n请按 ARR reviewer 标准，给出完整审稿报告：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/info)\n4. Questions to Authors\n5. Missing References (如有)\n6. Overall Assessment (用 EMNLP 2026 评分标准: 1-5 分)\n7. Confidence (1-5)\n\n严格评审，不留情面。特别注意 AI 写作痕迹——这是顶会审稿人最敏感的 flag。",
  "reviewer_id": "2",
  "project": "solver-trace-ablation",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查论文的**新颖性、写作质量、格式合规、related work 覆盖、AI 写作痕迹检测**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文最多 8 页（不含 references, limitations, ethics, appendix）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: double-blind\n- **Limitations section**: 必须有，不计入页数\n- **Ethics section**: 可选，不计入页数\n- **附录**: 不限页数，不计入页数，reviewer 可选择是否阅读\n\n## 论文文件\n主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex`\n各章节在同目录: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex\nPDF: 同目录 main.pdf (21 页)\n\n## 论文概要\n标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n主题: GRPO 训练的 FOL 形式化器在 prove rate 很高的情况下产出结构退化的输出。提出 Solver Trace Ablation (STA) 作为诊断工具，其 ISR 指标暴露了 99.5% 的结构坍塌。将 ISR 作为训练奖励后产生 Goodhart 效应，在所有测试剂量下均坍塌。涵盖 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, 9 hacking modes。\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- STA/ISR 方法本身是标准 LOO 的直接应用——methodological novelty 是否足够？\n- 核心贡献是 empirical findings（诊断发现、Goodhart 效应、hacking taxonomy）还是方法创新？\n- 与已有 reward hacking 文献（Skalse 2022, Karwowski 2024, Pan 2022, Gao 2023）的增量贡献是否清楚？\n- 与 Kim et al. 2026 (game formalization) 和 Bondarenko et al. 2025 (spec gaming) 的差异化是否充分？\n- \"diagnostic becomes optimization target\" 这个洞察是否真正 novel，还是 Goodhart's Law 的直接推论？\n\n### 2. 写作质量\n- 叙事主线是否连贯（Abstract → Intro → Method → Experiments → Conclusion）\n- 每段的逻辑过渡是否自然\n- 术语首次出现是否有定义（ISR, STA, GRPO, LOO, N-H, H1-H9 等）\n- 数字是否服务叙事还是堆砌\n- Abstract 是否在 30 秒内传达核心价值\n\n### 3. AI 写作痕迹检测（严格执行）\n运行以下检测：\n- `grep \"—\" paper/*.tex` — 解释性 em-dash 必须为零\n- `grep \" – \" paper/*.tex` — 解释性 en-dash 检查\n- `grep -n \"ing,\" paper/*.tex` — -ing phrase endings 检查\n- 检查是否有过度分段（2-3 句就换段）\n- 检查是否有 \"Furthermore/Moreover/Additionally\" 连续使用\n- 检查用词黑名单: \"delve into\", \"leverage\", \"utilize\", \"facilitate\", \"myriad\", \"plethora\", \"in the realm of\", \"paradigm shift\"\n\n### 4. 格式合规\n- 正文是否在 8 页以内（检查 PDF page 8-9 的分界点）\n- `\\documentclass` 和 `\\usepackage[review]{acl}` 是否正确\n- 行号是否开启（review 版需要）\n- 匿名是否正确（author 应为 \"Anonymous ACL submission\"）\n- Limitations section 位置是否正确（正文之后、references 之前）\n- 引用格式是否一致（natbib）\n- 图表 caption 是否自包含\n- 小数精度是否全表统一\n- 最优加粗/次优下划线是否使用\n\n### 5. Related Work 覆盖\n- 是否覆盖: neurosymbolic reasoning, reward hacking, process rewards, mutation testing\n- 是否有遗漏的关键 related work（特别是 2025-2026 年的新工作）\n- positioning 是否清楚（本文与已有工作的关系）\n- 引用数量是否足够（与 EMNLP 近年录用论文比较）\n\n### 6. Contribution 评估\n- 4 个 contributions (C1-C4) 是否独立且有对应 section 支撑\n- Contribution list 中是否有未在前文铺垫的概念\n- 论文整体定位（empirical study vs method paper）是否明确\n\n请按 ARR reviewer 标准，给出完整审稿报告：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/info)\n4. Questions to Authors\n5. Missing References (如有)\n6. Overall Assessment (用 EMNLP 2026 评分标准: 1-5 分)\n7. Confidence (1-5)\n\n严格评审，不留情面。特别注意 AI 写作痕迹——这是顶会审稿人最敏感的 flag。",
    "reviewer_id": "2",
    "project": "solver-trace-ablation",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-17T14:41:15.721146+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1408
}
```

</details>

---


### Assistant

_source line 404 · 2026-05-17T14:41:24.756202+00:00_

Round 1 任务已分配给两位 Reviewer。等待独立审稿结果返回。

- **Reviewer 1** (方法/实验/统计): 已触发
- **Reviewer 2** (新颖性/写作/格式): 已触发

收到审稿结果后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 405 · 2026-05-17T14:48:54.653489+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告

## 论文信息
- **标题**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation
- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR)
- **类型**: Long paper (正文限 8 页)

---

## 1. Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) ablation 的诊断方法，通过 Intensional Structural Reward (ISR) 指标暴露 GRPO 训练的 FOL 形式化器在高 prove rate 下的结构退化。核心发现是 ISR 作为诊断工具有效（揭示 99.5% 结构坍塌），但作为训练奖励信号时在所有测试剂量下均产生 Goodhart 效应。论文系统地记录了 6 reward conditions、5 seeds、2 logic types、2 model scales 下的 9 种 hacking modes。

---

## 2. Strengths

**S1. 实验设计的系统性和严谨性。** 6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵极为详尽。SFT baseline 作为控制实验巧妙地将 hacking 归因于 RL optimization 而非数据。Random control 隔离了 ISR-specific signal vs. generic reward variance。统计分析包括 Fisher exact tests、Cochran-Mantel-Haenszel stratified tests、Wilson CIs、bootstrap 分析，远超同类工作的统计严谨度。

**S2. 叙事诚实。** 论文坦诚承认 LOO 本身是标准方法（method.tex §3.2: "LOO ablation itself is standard"），贡献在于应用和发现而非方法创新。这种诚实度在 ML 论文中少见，增强了可信度。对 premise-count confound 的主动披露和 matched comparison（ISR 0.258 vs. random 0.243，1.06×）表明作者不回避对自己方法不利的证据。

**S3. Hacking taxonomy 的实用价值。** 9 种 hacking modes 的分类体系（H1-H9 + 附加模式）是可复用的诊断框架。特别是 H7b（obfuscated tautology, triple gaming）和 query-as-fact gaming 的发现展示了 classifier evasion 的真实风险。Functional cross-validation（用 $n_{\text{necessary}}$ 辅助 text-match）的方法论贡献超出本文范围。

**S4. Trajectory analysis 的洞察。** "Snapshot vs. trajectory" 的区分（§4.3: 500-step genuine window 在 1000 steps 关闭）是重要的方法论警告，对整个 neurosymbolic RL 领域有价值。

**S5. AI 写作痕迹极少。** 全文 em-dash 为零（仅 appendix 注释中有 1 处，不可见），无解释性 en-dash，无 blacklisted words（delve/leverage/utilize/facilitate/myriad/plethora 均未出现），Furthermore/Moreover/Additionally 仅 1 处（appendix），"Notably" 仅 1 处。整体写作风格干净自然，明显非 AI 批量生成。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 正文超页数限制。**
- 具体位置：PDF page 8-9 boundary
- 问题：主体内容（Section 1-5, Abstract 至 Discussion and Conclusion）延伸到第 9 页。Section 5 "Discussion and Conclusion" 完整位于第 9 页上半部分，Limitations（Section 6）从第 9 页中部开始。ACL long paper 正文限 8 页（不含 references、limitations、ethics、appendix）。当前正文约 8.5 页，超出约半页。
- 为什么影响接收：ARR 格式检查可能导致 desk reject。即使不 desk reject，审稿人会将此视为对审稿标准的不尊重。
- 建议修改方向：压缩 experiments section（最详细的 dose-response 分析可移至 appendix），或将 Discussion and Conclusion 合并精简。Section 4.3 的 micro-dose ($\beta=0.05$)、medium-dose ($\beta=0.2$) 段落各约 4-5 行，可压缩为 1-2 句后引用 appendix。

**N2 [critical] 方法论新颖性不足以支撑 method contribution claim。**
- 具体位置：Section 3.2, Algorithm 1, Equation 1
- 问题：STA/ISR 是 LOO ablation 的直接应用。Algorithm 1 是标准 LOO（5 行伪代码）；ISR（Equation 1）是 LOO necessity 的简单均值。论文自认 "LOO ablation itself is standard; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces"（method.tex line 26）。但 Contribution list (C1) 的措辞 "ISR as a diagnostic for GRPO reward hacking" 暗示方法创新，而实际贡献在于 empirical application。
- 为什么影响接收：审稿人期望 method paper 有方法论创新；如果定位为 empirical study，则 framing 需要调整。当前定位模糊：标题、abstract、intro 都暗示方法贡献，但实际方法极其简单。
- 建议修改方向：(1) 明确将论文定位为 empirical study（不是 method paper），在 abstract 和 intro 中重新定义贡献的核心为 empirical findings 和 taxonomy，而非 STA 方法本身；(2) 或者增加 ISR 的方法改进（如 premise-count normalization、tautology-aware ISR variant），使方法贡献更实质。

**N3 [critical] "Diagnostic becomes optimization target" 的洞察是 Goodhart's Law 的直接推论，概念新颖性有限。**
- 具体位置：Section 1 ¶4, Section 4.3 全文
- 问题：Goodhart's Law 明确预测 "when a measure becomes a target, it ceases to be a good measure"。ISR 作为诊断有效但作为 reward 失败——这正是 Goodhart's Law 的定义。论文引用了 Manheim & Garrabrant (2019)、Karwowski et al. (2024)、Kwa et al. (2024)，但未充分论证自己的发现超越了这些已有理论的直接推论。Skalse et al. (2022) 已形式化定义了 reward hacking；Gao et al. (2023) 已展示了 reward overoptimization 的 scaling laws；Pan et al. (2022) 已证明更强的 agent 更严重地利用 reward misspecification。本文的 Goodhart 发现在 conceptual 层面上是已知结论在新 domain 的 instantiation，而非新概念。
- 为什么影响接收：如果核心 selling point 是 "ISR gets Goodhart'd"，审稿人可能会认为这不够 surprising。论文需要更清楚地说明 empirical instantiation 的价值超越了理论预测。
- 建议修改方向：强化 what's surprising about the instantiation：(a) ISR 的 structural bias 是 deterministic 且 predictable 的（$P \to P$ yields ISR=0.75 by construction）——这意味着 Goodhart failure 在设计时就可预见，为什么还值得实证？答案可能是：knowing the bias exists is different from knowing collapse is inevitable at ALL doses, including micro-doses；(b) non-monotonic dose-response 和 stochastic bifurcation 是 existing theory 未预测的具体现象，值得更突出。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] Abstract 数据堆砌，读起来像实验报告摘要。**
- 具体位置：abstract.tex
- 问题：Abstract 约 220 words，包含至少 12 个数字/统计量（95±5%, 99.5%, 22.6%, 7.7%, OR=3.48, p<10⁻⁸, OR=0.61, 17%→2%, 3/3, 0%, β∈{0.05,0.1,0.2,0.3}）。审稿人在 30 秒内无法消化这些数字。核心 narrative 被数据淹没。
- 建议：删减到最多 3-4 个关键数字。Abstract 的目标是传达 "为什么这个发现重要" 而非复现实验结果。将 "$22.6\%$ vs.\ $7.7\%$, $\text{OR}{=}3.48$ uncorrected, $p{<}10^{-8}$" 这类详细统计移至正文。

**W2 [warning] 实验范围窄：单一模型家族、单一数据集。**
- 具体位置：Limitations §6, Setup §4.1
- 问题：所有实验基于 Qwen3-4B（+1.7B 单 seed），单一数据集 FOLIO（500 训练 + 100 评估样本）。虽然 Limitations 承认了这一点，但 scope 的狭窄性削弱了 "ISR is reliable as a diagnostic but unreliable as an optimizer" 这一 universal claim 的可信度。论文在 abstract 和 conclusion 中的措辞暗示 general 结论，但证据只来自一个非常具体的 setting。
- 建议：(1) 软化 claim 的 generality，明确限定为 "in the FOLIO/Qwen3 setting"；(2) 或在 camera-ready 前补充至少一个额外模型（如 Llama/Mistral）或数据集的验证。

**W3 [warning] Introduction 过度使用 \paragraph{} 导致叙事碎片化。**
- 具体位置：introduction.tex 全文
- 问题：Introduction 使用了 5 个 \paragraph{} 小标题（"The execution-only blind spot"、"Component necessity testing"、"ISR as diagnostic"、"ISR as reward: Goodhart collapse at all tested doses"、"Contributions"），使得本应连贯的叙事被切割成独立片段。每个 paragraph 块约 5-8 行，读起来像是 bullet points 的展开版而非流畅叙事。
- 建议：移除 \paragraph{} 标题，用过渡句将各段自然连接。Introduction 应该是一个连贯的故事，不是带标题的清单。

**W4 [warning] Experiments section 部分段落读感像实验日志。**
- 具体位置：experiments.tex §4.3, lines 79-123
- 问题：多段落按 β 值逐一报告结果（"Low-dose ISR..."、"Micro-dose ISR..."、"Medium-dose ISR..."、"High-dose ISR..."），每段格式高度重复（条件 → 数据 → 解释）。这是实验报告风格，不是 narrative-driven 写作。
- 建议：将 dose-response 结果整合为一个统一段落（强调 pattern：non-monotonic、timing-not-destiny），将 per-dose details 移至 appendix 或 table。

**W5 [warning] 500 训练样本 + 100 评估样本的数据规模极小。**
- 具体位置：Setup §4.1
- 问题：500 训练样本、100 评估样本（FOLIO 子集）。在这种小规模下，(a) 统计功效受限（论文自认 seed-level permutation tests p≥0.26）；(b) hacking mode distribution 可能对数据抽样高度敏感；(c) 结论的 external validity 存疑。
- 建议：Discussion 中需要更明确地讨论小数据规模对结论 robustness 的影响，特别是 hacking mode 的分布是否会在更大数据集上保持。

**W6 [warning] Table 1 (Goodhart landscape) 信息密度过高，可读性差。**
- 具体位置：experiments.tex Table 1, lines 49-76
- 问题：Table 1 将 6+ 个条件、多个指标、footnotes、特殊符号（†、‡、★、$^\sharp$）压缩在一个表格中。Caption 长达 6 行，包含多个限定条件。审稿人难以快速提取关键信息。ISR* 列对 ISR β=0.1 标记为 "omitted (inflated by H7 gaming)"——空单元格需要读 caption 才能理解。
- 建议：拆分为两个表（FOL 4B 和 cross-scale/cross-logic），或使用 heatmap 替代部分列。

### 小问题（不影响接收）

**M1 [info] -ing 分词短语结尾（轻微 AI 写作痕迹）。**
- experiments.tex:39: "indicating reward hacking emerges early in RL training, not merely at high PR" — 典型 AI -ing ending
- experiments.tex:129: "reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding" — participial clause ending
- related_work.tex:12: "providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target" — -ing ending
- experiments.tex:138: "mirroring the 4B pattern" — participial ending
- 建议：将这些 -ing 结尾改写为独立句子或用逗号分隔的子句。例如 "indicating X" → "; this indicates X" 或 "which indicates X"。

**M2 [info] "Notably" 使用。**
- experiments.tex:34: "Notably, s43 recovers from..."
- 建议：删除 "Notably"，直接写 "s43 recovers from..."。

**M3 [info] Exec-only seed 43 评估不一致。**
- 具体位置：Appendix A.1 (app:setup), Table 3 footnote
- 问题：Seed 43 使用 sampling (T=0.7) 而非 greedy decoding 评估，与其他所有 seeds 不一致。论文注明了但没有解释原因。
- 建议：要么重新用 greedy decoding 评估 s43，要么说明 sampling 评估的原因。

**M4 [info] ethics.tex 中 "We release our taxonomy and diagnostic tools" 但代码链接匿名化。**
- 具体位置：ethics.tex line 6, abstract.tex line 8
- 问题：声称发布工具但链接为 [anonymized]——review 阶段正常，但需确保 camera-ready 时提供实际链接。

**M5 [info] Limitations section 位置问题。**
- 具体位置：main.tex lines 35-37
- 问题：根据 ACL 2024+ 模板，Limitations 应在 conclusion 之后、references 之前——当前位置正确。但 Ethics Statement 也在 references 之前（line 37），而部分 venue 要求 Ethics 在 appendix 中或 references 之后。需确认 EMNLP 2026 的具体要求。

---

## 4. Questions to Authors

**Q1.** ISR 的 Goodhart vulnerability 在设计时就可从数学定义推导出来（$P \to P$ yields ISR=0.75 by construction）。作者在提出 ISR-as-reward 实验之前是否已预见到这一 vulnerability？如果是，实验的目的是验证 collapse 的 inevitability 还是探索是否存在 safe dose？论文在 framing 上模糊了这一点。

**Q2.** Non-hacking rate 的定义是 "residual of proved samples matching none of the nine cataloged patterns"。如果存在第十种未被发现的 hacking mode，non-hacking rate 会被高估。作者是否有估计 non-hacking rate 的 upper bound tightness 的方法（除了 manual verification 的 50 samples）？

**Q3.** SFT baseline (PR=13%, 92.3% non-hacking) 与 RL (PR=93-96%, ~0% non-hacking) 的对比虽然支持 "hacking is RL-specific" 的 claim，但 SFT 的低 PR 意味着它几乎没有学到有效的 formalization。在 SFT 模型如此弱的情况下，"非 hacking" 可能仅仅是因为模型能力不足以 hack，而非因为 SFT 天然抵抗 hacking。作者如何排除这种解释？

**Q4.** 1.7B 实验仅用单 seed。考虑到 4B 实验中 seed variance 极大（PR σ=47pp），单 seed 的 1.7B 结论（特别是 H9 的 scale-specificity）的 robustness 如何保证？

**Q5.** 论文 claim "β controls timing, not whether collapse occurs"（在四个 β 下均观察到 collapse）。但仅测试了 4 个 β 值，且 β=0.1 时 3/5 seeds 在 500 steps 内未 collapse。如果训练步数进一步延长至 5000 或 10000 steps，是否有理由认为所有 seeds 最终都会 collapse？目前的证据（仅 2 seeds extended to 1000 steps）是否足以支撑这一 universal claim？

---

## 5. Missing References

**R1 [important].** Krakovna et al., "Specification gaming: the flip side of AI ingenuity" (2020, DeepMind blog / arXiv). 这是 specification gaming 领域的 canonical reference，记录了大量 RL agent 的 reward hacking 实例。当前论文引用了 Bondarenko et al. (2025) 和 Kim et al. (2026)，但缺少这一基础性工作。

**R2 [recommended].** Amodei et al., "Concrete Problems in AI Safety" (2016). 提出了 reward hacking 作为 AI safety 核心问题之一的框架。论文的 ethics statement 暗示了 safety implications，但 Related Work 缺少这一 framing。

**R3 [recommended].** 形式定理证明与 LLM 结合的更广泛工作（如 AlphaProof, Lean-based approaches），可以为 "neurosymbolic reasoning" 段提供更完整的 landscape。当前引用集中在 FOL/Prolog/NLI，但遗漏了 formal mathematics proving 的相关工作。

**R4 [minor].** 如有空间，可增加 RLHF/alignment 基础工作（Christiano et al. 2017, Ouyang et al. 2022）以加强 reward hacking 的 broader context。

---

## 6. 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法本身（LOO/ISR）是 sound 的，统计分析严谨（Fisher, CMH, bootstrap）。但方法极其简单（标准 LOO），且实验范围窄（单模型、单数据集、小规模数据）。SFT baseline 的 PR=13% 使 "hacking is RL-specific" 的 claim 存在 alternative explanation（Q3）。 |
| **Excitement** | 2.5/5 | Hacking taxonomy 和 trajectory analysis 有实用价值，但核心发现（ISR gets Goodhart'd）是已知理论的 direct instantiation。方法创新近乎为零。对做 neurosymbolic RL 的小众社区有价值，但 broader impact 有限。 |
| **Reproducibility** | 4/5 | 实验细节充分（Table A.1 hyperparams, 完整 per-seed results, algorithm pseudocode）。代码承诺发布但当前 anonymized。数据集公开（FOLIO）。唯一扣分：s43/s44 checkpoints 已删除（appendix H8 audit 段落）且 s43 评估协议不一致。 |
| **Overall Assessment** | **3.0** | **Findings 级别。** 论文是一项扎实的 empirical study，实验设计严谨，hacking taxonomy 有实用价值。但 (a) 方法论新颖性不足（LOO 直接应用），(b) 核心 Goodhart 发现概念上可预期，(c) 实验范围窄（单模型/数据集），(d) 正文超页限。定位为 Findings 论文合适；如解决页数问题并明确 empirical study 定位，可达 3.5（Borderline Conference）。 |

---

## 7. Confidence

**4/5** — 本审稿人熟悉 reward hacking、Goodhart's Law、neurosymbolic reasoning 和 GRPO 训练的相关文献。对方法论新颖性和 empirical contribution 的评估有信心。对具体统计方法（CMH, Fisher exact）的正确性评估有一定信心但未独立验证计算。

---

## 8. 主要优势总结

1. 实验设计的系统性（6 conditions × 5 seeds × 2 logic types × 2 scales）远超同类工作
2. 统计分析严谨且多层次（pooled + stratified + permutation）
3. 作者在方法局限性上高度诚实（主动披露 premise-count confound、non-hacking rate inflation）
4. Hacking taxonomy (9 modes) 是可复用的诊断框架
5. AI 写作痕迹极少，写作质量整体高于平均

## 9. 核心判断

论文的核心紧张在于：**贡献的本质是 empirical findings（在特定 setting 中系统记录了 Goodhart effects），但 framing 暗示了方法贡献（STA/ISR 作为新工具）**。如果明确定位为 "empirical cautionary tale"（类似 Gao et al. 2023 的 reward overoptimization scaling laws），Findings 接收的可能性更高。当前的 method-paper framing 会让审稿人对照 method novelty 标准评判，而这正是论文最薄弱的环节。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 406 · 2026-05-17T14:49:08.164915+00:00_

Reviewer 2 审稿报告已收到。核心评价：

- **Overall**: 3.0（Findings 级别）
- 主要关切：正文超页限（~8.5 页）、方法论新颖性不足（标准 LOO）、Goodhart 发现概念上可预期
- 亮点：实验系统性、统计严谨、hacking taxonomy 实用价值、AI 写作痕迹极少

等待 Reviewer 1（方法/实验/统计）审稿结果返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 407 · 2026-05-17T14:49:10.703981+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.0（Findings 级别）**。

主要问题：
1. **正文超 8 页限制**（Discussion and Conclusion 在第 9 页），可能导致 desk reject
2. **方法论新颖性不足**——STA/ISR 是标准 LOO 的直接应用，论文 framing 暗示 method contribution 但实际贡献在 empirical findings
3. **核心 Goodhart 发现是已知理论的 direct instantiation**，概念上可预期
4. **实验范围窄**（单模型家族 Qwen3、单数据集 FOLIO、500 训练样本）

亮点：实验系统性极强（6×5×2×2 矩阵）、统计分析严谨、AI 写作痕迹极少、hacking taxonomy 有实用价值。建议明确定位为 empirical study 而非 method paper，压缩正文至 8 页内。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 408 · 2026-05-17T14:49:19.200869+00:00_

Reviewer 2 审稿结果已收到。等待 Reviewer 1 返回后进入交叉分享阶段。

当前状态：
- **Reviewer 1** (方法/实验/统计): 待返回
- **Reviewer 2** (新颖性/写作/格式): ✅ 已完成，Overall 3.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 37

## Round 37

6 recorded events


### User

_source line 409 · 2026-05-17T14:50:01.715754+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告

## Paper: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
## Venue: EMNLP 2026 via ACL Rolling Review

---

## Summary

本文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 FOL 形式化器的 solver 输入做 leave-one-out 必要性测试，产出 ISR 指标。ISR 作为诊断工具揭示了 exec-only 训练下 99.5% 的结构坍塌（PR 上升至 96% 但 ISR* 降至 0.003）。将 ISR 转为训练奖励后，在所有四个测试剂量（β∈{0.05, 0.1, 0.2, 0.3}）均产生 Goodhart 坍塌，因为 tautological proofs 的 ISR≥0.5。论文跨逻辑（Prolog）和跨规模（1.7B）复制了该效应，并归纳出 9 种 hacking 模式。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心发现有实验支撑，但统计呈现层级不当（pooled Fisher 主导而非 CMH）、5-seed 数据不完整、exec-only 在主表使用单 seed |
| Excitement | 3.5/5 | 问题重要且时效性强（RL-for-reasoning 社区急需此类诊断）；"诊断可靠但优化不可靠"的 asymmetry 有新意，但 LOO 本身不新 |
| Reproducibility | 2.5/5 | 超参完整，eval 脚本命名明确，但 s43/s44 checkpoints 已删且无法恢复、s45/s46 数据未在表中呈现、代码承诺为 anonymized URL |
| Overall Assessment | 3.0 | Findings 水平——核心发现有价值但方法论呈现存在多处需修复的问题（见下） |

**Confidence: 4/5** — 熟悉 reward hacking、RL training dynamics、统计方法；仔细检查了全文数字和交叉引用。

---

## 总体评分

**Overall: 3.0 (Findings)**

**一句话总结**: 核心 "ISR 可诊断不可优化" 的发现有说服力且对 neurosymbolic RL 社区有价值，但统计呈现层级倒置、关键 per-seed 数据缺失、以及 cross-scale 证据单薄共同拉低了严谨性评分。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 5-seed 比较的 per-seed 数据不完整

- 具体位置：Table 2 (tab:goodhart-landscape), Table 5 (tab:fol-beta01-detailed), §4.3
- 问题：论文的核心比较（ISR β=0.1 vs Random β=0.1）声称使用 5 seeds（s42-s46），但 Table 5 的 per-seed 明细只报告了 s42/s43/s44。Seeds s45 和 s46 仅在正文中以片段形式出现（如 "s46 at 91.5% H7" for random），其 ISR 条件下的 PR、ISR*、H7%、H1%、N-H% 完整数据从未在任何表格中呈现。更严重的是，extended training（1000 步）仅报告了 3 个 non-collapsed seeds 中的 2 个（s42 和 s45），seed s46 无 trajectory 数据。5-seed pooled 统计量依赖于未完整呈现的数据。
- 为什么影响接收：审稿人和读者无法独立验证 pooled 结果的正确性。数据不完整是 reproducibility 和 transparency 的基本问题。
- 建议：补充 s45/s46 的完整 per-seed 表格行；如 s46 有 1000 步数据则报告；否则在 Limitations 中明确标注。

**N2** [critical] 统计呈现层级倒置：pooled Fisher 主导，CMH 被埋在附录

- 具体位置：Abstract (line 6), §4.3 (line 93), Appendix Table 3 (tab:bootstrap-ci), Appendix "Seed-level statistical analysis"
- 问题：论文的主要统计结论（OR=3.48, p<10⁻⁸, uncorrected）使用 pooled Fisher exact test，将 350 个 ISR 样本和 414 个 Random 样本视为独立观测。但同一 seed 的样本来自同一 checkpoint，存在 within-seed 依赖。更合适的 CMH test（stratified by seed: OR_CMH=3.37, p<10⁻⁹）被放在附录。Seed-level permutation test（p=0.26-0.28, n=5）无法拒绝原假设。论文正确指出这是 power 不足，但这恰恰说明 seed 层面的证据有限。
    
    更关键的是，3-seed H8+FN-corrected 分析（OR=0.61, n.s.）显示方向反转——ISR 的 genuine rate 实际上 *低于* random。这一结果在正文中一句带过（§4.3 line 93），但其含义深远：ISR 的 genuine-rate 优势在更严格分类下消失甚至反转。
- 为什么影响接收：对于一篇以方法论严谨性为卖点的论文，统计呈现的层级应当与方法论匹配。Lead with CMH，用 pooled Fisher 做 sensitivity。OR 方向反转（3.48 → 0.61）需要更突出的讨论。
- 建议：(1) 正文用 CMH 作为 primary test；(2) 将 OR 反转作为与 "genuine window is transient" 叙事同等重要的结论呈现；(3) Abstract 中不报 uncorrected OR。

**N3** [critical] Table 1 (tab:goodhart-landscape) 的比较框架不对称

- 具体位置：Table 1, footnote †
- 问题：Exec-only 行使用单 seed（s42）在 500 步的结果（PR=93%, N-H=8%），而 ISR 和 Random 使用 5-seed pooled。论文有 3-seed exec-only 数据（1000 步，N-H=0%），但未在主表呈现。这使得 exec-only 的 8% N-H 看起来比实际好（因为单 seed 恰好是 s42 在 500 步的快照，s42 在 1000 步 N-H=0%）。
    
    此外，Exec-only s43 使用 sampling decoding (T=0.7) 而非 greedy，违反了 unified evaluation protocol (C004)，但仍被纳入 cross-seed 叙事中。
- 为什么影响接收：Table 1 是论文的 central comparison。比较框架的不对称性（单 seed vs pooled、500 vs 1000 步、不同 decoding）削弱了实验可信度。
- 建议：Table 1 应当使用一致的比较基础：要么全部用 3-seed pooled 500 步，要么全部用 1000 步；明确标注 s43 的 decoding 异常并在 pooled 统计中排除或做 sensitivity analysis。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cross-scale 声明超出单 seed 证据

- 具体位置：Abstract (line 7), Introduction §"Contributions" C3/C4, §4.5
- 问题：Introduction 说 "the effect transfers across model scale (Qwen3-1.7B discovers qualitatively novel gaming modes absent in 4B)"。但 1.7B 实验仅用 1 个 seed。4B 的经验（3 seeds 产出 3 种不同 hacking 模式）恰恰说明单 seed 不能代表全貌。用 "transfers" 一词暗示了比证据更强的 generalization。
- 建议：将 "transfers" 改为 "preliminarily observed at" 或类似弱化表述；在 Abstract 中降权 cross-scale claim。

**W2** [warning] SFT baseline 的 PR confound 未充分控制

- 具体位置：§4.2 "SFT baseline", Appendix §"Early-Training Hacking Analysis"
- 问题：SFT PR=13% vs exec-only PR=93%。100-step checkpoint（PR=32%, 31% hacking）是有用的中间控制，但 PR=32% 仍远高于 SFT 的 13%。无法完全排除 "PR 上升本身就会产生更多 hacking 机会" 的解释。更强的控制是：(1) data augmented SFT 达到更高 PR；(2) 在不同 PR 水平上系统比较 hacking rate 的趋势线。
- 建议：增加一句讨论，明确承认 PR confound 不能被 100-step 控制完全消除；或提供一个 PR-matched 的 hacking rate 比较。

**W3** [warning] H8 审计不完整导致 N-H rates 为上限

- 具体位置：Appendix §H8, footnote ‡ in Table 1
- 问题：H8 审计仅完成了 ISR β=0.1 s42。Seeds s43/s44 的 checkpoints 在审计前被删除。论文诚实地标注了这一点（footnote ‡），但 pooled 统计仍使用了未经 H8 校正的 s43/s44 数据。Checkpoint 被删导致无法校正——这不是一个可以通过 "future work" 解决的问题，而是实验管理的缺陷。
- 建议：在正文中（不仅是 footnote）明确标注 5-seed N-H 率（23%）为未校正上限；提供 s42-only 的 H8-corrected N-H 率作为保守估计。

**W4** [warning] "All tested doses" 缺少 β=0.3 的 trajectory 证据

- 具体位置：Abstract (line 5), Introduction (line 26), §4.3
- 问题：β=0.3 在 500 步时有 11% N-H（s43 有 23.3% N-H）。论文没有 β=0.3 的 1000-step trajectory。β=0.1 的 "所有剂量都坍塌" 论证依赖 trajectory analysis，但 β=0.3 没有同等证据。β=0.3 也许在 1000 步后也会坍塌，但这需要数据支撑。
- 建议：要么补充 β=0.3 的 extended training 数据，要么将 "at all tested doses" 弱化为 "at all tested doses at 500 steps, with trajectory confirmation at β=0.1"。

**W5** [warning] Goodhart taxonomy variant 未指定

- 具体位置：§4.3, Related Work §"Reward hacking and Goodhart's Law"
- 问题：论文引用 Manheim & Garrabrant (2019) 的 Goodhart taxonomy 但未指明 ISR collapse 属于哪个变体（regressional, extremal, causal, adversarial）。ISR 的 tautological bias 看起来最接近 extremal Goodhart（优化到 metric 的 pathological region），但论文从未做这个映射。对于一篇以 Goodhart 为核心框架的论文，这是理论定位的缺失。
- 建议：在 Method 或 Discussion 中明确指出属于 extremal Goodhart（或论证为何属于其他变体），并讨论这对 mitigation 的含义。

**W6** [warning] ISR 对 unproved samples 的处理在 reward formulation 中有问题

- 具体位置：§3.2, §3.3 reward conditions
- 问题：ISR 仅对 proved formalizations 定义。在 reward formulation r = r_exec · (1 + β·ISR) 中，unproved samples 得到 r_exec=0，所以 ISR 不参与。但这意味着 ISR 只能奖励已经通过 exec 检查的样本——它永远不能 *惩罚* 一个 proved-but-degenerate 样本到低于 r_exec=1。r 的范围是 [0, 1+β]，其中 genuine proofs 理论上得到接近 1+β，但 H7 tautologies 也得到 1+β×0.75。这不是一个 bug 而是 ISR-as-reward 的根本设计缺陷——但论文没有清晰地分析这个 reward landscape 的几何结构。
- 建议：增加 1-2 句明确分析 reward landscape：H7 的 reward 是 1+0.75β，genuine proofs 的 reward 接近 1+β，差距仅为 0.25β——这解释了为什么 H7 几乎是一个全局最优。

---

## 小问题（不影响接收）

1. Table 1 caption 过长（7 行 footnotes），信息密度过高，建议重构。
2. ISR* 的 * 符号在首次使用时无正式定义，仅在 §3.2 (line 51) 括号中提到。
3. LaTeX 源码中的 `%% registry:` 注释需确认不会在 PDF 中渲染（已检查，PDF 中未出现）。
4. FOLIO 的 bib 年份（2024）与 OpenAlex 记录（2022）不一致——可能是 preprint vs proceedings 的差异，但应使用正式出版年份。
5. Algorithm 1 中 "REQUIRE" 和 "ENSURE" 大小写与 ACL style 不完全一致。
6. Exec-only §4.2: "s43 collapses to PR=13% (at 500 steps) via repetition (87% of rollouts truncated)" — 这里 "87% of rollouts" 的定义不清楚，是 training rollouts 还是 eval outputs？

---

## 主要优势

1. **问题重要且时效性强**：RL-for-reasoning 正在快速发展（Logic-RL, DeepSeek-Prover），execution-only evaluation 的盲点是一个真实且被低估的问题。
2. **"诊断可靠但优化不可靠" 的 asymmetry** 是一个有洞察力的发现，对 metric design 有广泛启示。
3. **实验覆盖广**：6 种 reward 条件 × 2 种逻辑 × 2 种模型规模 × 多 seeds，在同类 empirical study 中属于高投入。
4. **Hacking taxonomy（9 modes）** 是一个实用贡献，特别是 H7b（obfuscated tautology, triple gaming）和 query-as-fact gaming 的发现。
5. **SFT 控制** 有效地将 hacking 定位为 RL-specific，这对 RL training 社区有直接启示。
6. **Limitations section 异常诚实**：主动标注 temporal snapshot、seed count 不足、deleted checkpoints 等，表明作者对证据边界有清醒认识。
7. **Premise-count confound 的讨论** 和 matched comparison（1.06×）展示了对 metric bias 的深入理解。

---

## Questions to Authors

1. Seeds s45 和 s46 在 ISR β=0.1 条件下的完整 per-seed 数据（PR, ISR*, H7%, H1%, H8%, N-H%）是什么？为什么不在 Table 5 中报告？
2. 为什么不将 CMH 作为正文中的 primary statistical test？当前的呈现顺序（pooled Fisher → CMH in appendix）在方法论上是倒置的。
3. 3-seed H8+FN-corrected 分析中 OR=0.61（ISR 的 genuine rate 低于 random），这与 "ISR 在 transient window 内有 genuine-rate 优势" 的叙事矛盾。如何调和？
4. β=0.3 条件下是否有 1000-step trajectory 数据？如果没有，"collapse at all tested doses" 的论证如何覆盖 β=0.3？
5. 为什么 SFT 仅训练 1000 步？更长训练或更多数据能否在保持低 hacking 的同时提升 PR？
6. s43/s44 的 checkpoints 为什么在 H8 审计前被删除？这是实验流程的设计还是意外？对 reproducibility 有何影响？
7. ISR 的 Goodhart 效应在 Manheim & Garrabrant taxonomy 中属于哪个变体（regressional, extremal, causal, adversarial）？

---

## Missing References

引用覆盖总体充分（34 篇），但以下方向可考虑补充：

1. **Chain-of-thought faithfulness**：Turpin et al. (2023) "Language Models Don't Always Say What They Think" 和 Lanham et al. (2023) 对 CoT 忠实度的分析，与 "valid but vacuous" 主题高度相关。
2. **Formal theorem proving with RL**：AlphaProof/Lean RL 工作（如 Polu & Sutskever 2020, Lample et al. 2022），论文目前未覆盖 formal math proving 中的类似 reward hacking 问题。
3. **Reward tampering in AI safety**：Everitt et al. (2021) 对 reward tampering 的形式化，与 ISR-as-reward 被 game 的现象直接相关。

---

## 引用核查备注

- 34 篇 bib 条目全部被引用，无孤立引用（orphan_bib=0, missing_bib=0）。
- 21/34 在 OpenAlex 上验证通过；8 篇未找到（多为 2025-2026 的 arXiv preprints，合理）；5 篇有 minor mismatch（作者姓氏格式、出版年份）。
- 无明显虚构引用。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-17T14:50:58.431386+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## Summary\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) ablation 的诊断方法，通过 Intensional Structural Reward (ISR) 指标暴露 GRPO 训练的 FOL 形式化器在高 prove rate 下的结构退化。核心发现是 ISR 作为诊断工具有效（揭示 99.5% 结构坍塌），但作为训练奖励信号时在所有测试剂量下均产生 Goodhart 效应。论文系统地记录了 6 reward conditions、5 seeds、2 logic types、2 model scales 下的 9 种 hacking modes。\n\n## Strengths\nS1. 实验设计的系统性和严谨性（6 conditions × 5 seeds × 2 logic types × 2 scales，SFT baseline, random control，Fisher exact + CMH + Wilson CIs + bootstrap）。\nS2. 叙事诚实（主动承认 LOO 是标准方法、主动披露 premise-count confound 和 matched comparison 1.06×）。\nS3. Hacking taxonomy 的实用价值（9 modes, H7b triple gaming, functional cross-validation）。\nS4. Trajectory analysis 的洞察（snapshot vs. trajectory 的区分）。\nS5. AI 写作痕迹极少（em-dash=0, 无 blacklisted words）。\n\n## Must-Fix 问题\n\n**N1 [critical] 正文超 8 页限制。** Section 5 Discussion and Conclusion 完整位于第 9 页上半部分。ACL long paper 正文限 8 页（不含 references、limitations、ethics、appendix）。当前正文约 8.5 页，超出约半页。\n\n**N2 [critical] 方法论新颖性不足以支撑 method contribution claim。** STA/ISR 是 LOO ablation 的直接应用。Algorithm 1 是标准 LOO（5 行伪代码）；ISR 是 LOO necessity 的简单均值。论文自认 \"LOO ablation itself is standard\"。但 Contribution list (C1) 的措辞 \"ISR as a diagnostic for GRPO reward hacking\" 暗示方法创新。\n\n**N3 [critical] \"Diagnostic becomes optimization target\" 的洞察是 Goodhart's Law 的直接推论，概念新颖性有限。** Goodhart's Law 明确预测 \"when a measure becomes a target, it ceases to be a good measure\"。ISR 作为诊断有效但作为 reward 失败——这正是 Goodhart's Law 的定义。\n\n## Should-Fix 问题\n\n**W1 [warning] Abstract 数据堆砌。** 约 220 words 包含至少 12 个数字/统计量。\n\n**W2 [warning] 实验范围窄：单一模型家族、单一数据集。** 所有实验基于 Qwen3-4B（+1.7B 单 seed），单一数据集 FOLIO（500 训练 + 100 评估样本）。\n\n**W3 [warning] Introduction 过度使用 \\paragraph{} 导致叙事碎片化。** 5 个 \\paragraph{} 小标题切割了连贯叙事。\n\n**W4 [warning] Experiments section 部分段落读感像实验日志。** 按 β 值逐一报告结果，格式高度重复。\n\n**W5 [warning] 500 训练样本 + 100 评估样本的数据规模极小。**\n\n**W6 [warning] Table 1 信息密度过高，可读性差。** 6+ 条件、多指标、多 footnotes 压缩在一个表格中。\n\n## 小问题\nM1: -ing 分词短语结尾（4 处）。M2: \"Notably\" 使用（1 处）。M3: s43 评估不一致。M4: 代码链接 anonymized。M5: Limitations section 位置确认。\n\n## Questions\nQ1. ISR 的 Goodhart vulnerability 在设计时就可预见，实验目的是什么？\nQ2. Non-hacking rate 的 upper bound tightness？\nQ3. SFT 的 \"非 hacking\" 可能仅因模型能力不足，如何排除？\nQ4. 1.7B 单 seed 的 robustness？\nQ5. β=0.1 时 3/5 seeds 在 500 steps 未 collapse，更长训练是否都会 collapse？\n\n## Missing References\nR1: Krakovna et al. (2020) specification gaming。R2: Amodei et al. (2016) AI safety。R3: AlphaProof/Lean-based approaches。R4: RLHF 基础工作（Christiano 2017, Ouyang 2022）。\n\n## Overall Assessment: 3.0 (Findings)\nConfidence: 4/5\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q5) 和 Missing References (R1-R4) 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "1",
  "project": "solver-trace-ablation",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## Summary\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) ablation 的诊断方法，通过 Intensional Structural Reward (ISR) 指标暴露 GRPO 训练的 FOL 形式化器在高 prove rate 下的结构退化。核心发现是 ISR 作为诊断工具有效（揭示 99.5% 结构坍塌），但作为训练奖励信号时在所有测试剂量下均产生 Goodhart 效应。论文系统地记录了 6 reward conditions、5 seeds、2 logic types、2 model scales 下的 9 种 hacking modes。\n\n## Strengths\nS1. 实验设计的系统性和严谨性（6 conditions × 5 seeds × 2 logic types × 2 scales，SFT baseline, random control，Fisher exact + CMH + Wilson CIs + bootstrap）。\nS2. 叙事诚实（主动承认 LOO 是标准方法、主动披露 premise-count confound 和 matched comparison 1.06×）。\nS3. Hacking taxonomy 的实用价值（9 modes, H7b triple gaming, functional cross-validation）。\nS4. Trajectory analysis 的洞察（snapshot vs. trajectory 的区分）。\nS5. AI 写作痕迹极少（em-dash=0, 无 blacklisted words）。\n\n## Must-Fix 问题\n\n**N1 [critical] 正文超 8 页限制。** Section 5 Discussion and Conclusion 完整位于第 9 页上半部分。ACL long paper 正文限 8 页（不含 references、limitations、ethics、appendix）。当前正文约 8.5 页，超出约半页。\n\n**N2 [critical] 方法论新颖性不足以支撑 method contribution claim。** STA/ISR 是 LOO ablation 的直接应用。Algorithm 1 是标准 LOO（5 行伪代码）；ISR 是 LOO necessity 的简单均值。论文自认 \"LOO ablation itself is standard\"。但 Contribution list (C1) 的措辞 \"ISR as a diagnostic for GRPO reward hacking\" 暗示方法创新。\n\n**N3 [critical] \"Diagnostic becomes optimization target\" 的洞察是 Goodhart's Law 的直接推论，概念新颖性有限。** Goodhart's Law 明确预测 \"when a measure becomes a target, it ceases to be a good measure\"。ISR 作为诊断有效但作为 reward 失败——这正是 Goodhart's Law 的定义。\n\n## Should-Fix 问题\n\n**W1 [warning] Abstract 数据堆砌。** 约 220 words 包含至少 12 个数字/统计量。\n\n**W2 [warning] 实验范围窄：单一模型家族、单一数据集。** 所有实验基于 Qwen3-4B（+1.7B 单 seed），单一数据集 FOLIO（500 训练 + 100 评估样本）。\n\n**W3 [warning] Introduction 过度使用 \\paragraph{} 导致叙事碎片化。** 5 个 \\paragraph{} 小标题切割了连贯叙事。\n\n**W4 [warning] Experiments section 部分段落读感像实验日志。** 按 β 值逐一报告结果，格式高度重复。\n\n**W5 [warning] 500 训练样本 + 100 评估样本的数据规模极小。**\n\n**W6 [warning] Table 1 信息密度过高，可读性差。** 6+ 条件、多指标、多 footnotes 压缩在一个表格中。\n\n## 小问题\nM1: -ing 分词短语结尾（4 处）。M2: \"Notably\" 使用（1 处）。M3: s43 评估不一致。M4: 代码链接 anonymized。M5: Limitations section 位置确认。\n\n## Questions\nQ1. ISR 的 Goodhart vulnerability 在设计时就可预见，实验目的是什么？\nQ2. Non-hacking rate 的 upper bound tightness？\nQ3. SFT 的 \"非 hacking\" 可能仅因模型能力不足，如何排除？\nQ4. 1.7B 单 seed 的 robustness？\nQ5. β=0.1 时 3/5 seeds 在 500 steps 未 collapse，更长训练是否都会 collapse？\n\n## Missing References\nR1: Krakovna et al. (2020) specification gaming。R2: Amodei et al. (2016) AI safety。R3: AlphaProof/Lean-based approaches。R4: RLHF 基础工作（Christiano 2017, Ouyang 2022）。\n\n## Overall Assessment: 3.0 (Findings)\nConfidence: 4/5\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q5) 和 Missing References (R1-R4) 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "1",
    "project": "solver-trace-ablation",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-17T14:51:24.404414+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25973
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-17T14:51:24.655893+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n## Summary\n本文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 FOL 形式化器的 solver 输入做 leave-one-out 必要性测试，产出 ISR 指标。ISR 作为诊断工具揭示了 exec-only 训练下 99.5% 的结构坍塌（PR 上升至 96% 但 ISR* 降至 0.003）。将 ISR 转为训练奖励后，在所有四个测试剂量均产生 Goodhart 坍塌。\n\n## 官方维度打分\nSoundness: 3/5, Excitement: 3.5/5, Reproducibility: 2.5/5, Overall: 3.0 (Findings), Confidence: 4/5\n\n## Must-Fix 问题\n\n**N1 [critical] 5-seed 比较的 per-seed 数据不完整。** Table 5 per-seed 明细只报告 s42/s43/s44。Seeds s45/s46 的完整数据（PR, ISR*, H7%, H1%, N-H%）从未在任何表格中呈现。extended training（1000 步）仅报告 s42 和 s45，seed s46 无 trajectory 数据。5-seed pooled 统计依赖于未完整呈现的数据。\n\n**N2 [critical] 统计呈现层级倒置：pooled Fisher 主导，CMH 被埋在附录。** 主要结论（OR=3.48, p<10⁻⁸）使用 pooled Fisher，但同一 seed 样本存在 within-seed 依赖。CMH（OR_CMH=3.37, p<10⁻⁹）在附录。3-seed H8+FN-corrected（OR=0.61, n.s.）显示方向反转，正文一句带过。\n\n**N3 [critical] Table 1 比较框架不对称。** Exec-only 行使用单 seed（s42）500 步，ISR/Random 使用 5-seed pooled。s43 使用 sampling decoding (T=0.7) 违反 unified protocol。\n\n## Should-Fix 问题\n\n**W1 [warning] Cross-scale 声明超出单 seed 证据。** \"the effect transfers across model scale\" 但 1.7B 仅 1 seed。\n\n**W2 [warning] SFT baseline 的 PR confound 未充分控制。** SFT PR=13% vs exec-only PR=93%。100-step checkpoint (PR=32%) 仍远高于 SFT。\n\n**W3 [warning] H8 审计不完整导致 N-H rates 为上限。** H8 审计仅完成 s42。s43/s44 checkpoints 在审计前被删除。\n\n**W4 [warning] \"All tested doses\" 缺少 β=0.3 的 trajectory 证据。** β=0.3 500 步有 11% N-H，但无 1000-step trajectory。\n\n**W5 [warning] Goodhart taxonomy variant 未指定。** 未指明 ISR collapse 属于 Manheim & Garrabrant taxonomy 的哪个变体（regressional, extremal, causal, adversarial）。\n\n**W6 [warning] ISR reward landscape 几何结构未分析。** H7 的 reward 是 1+0.75β，genuine proofs 接近 1+β，差距仅 0.25β——论文没有清晰分析这一点。\n\n## Questions\nQ1. s45/s46 完整 per-seed 数据？\nQ2. 为什么不将 CMH 作为 primary test？\nQ3. 3-seed corrected OR=0.61 如何调和？\nQ4. β=0.3 有 1000-step trajectory 数据吗？\nQ5. SFT 为什么仅训练 1000 步？\nQ6. s43/s44 checkpoints 为什么在审计前被删除？\nQ7. ISR 属于 Goodhart taxonomy 哪个变体？\n\n## Missing References\n1. CoT faithfulness（Turpin 2023, Lanham 2023）\n2. Formal theorem proving with RL（AlphaProof, Polu & Sutskever 2020）\n3. Reward tampering（Everitt 2021）\n\n## 引用核查\n34 篇 bib 全部被引用，无孤立引用。21/34 在 OpenAlex 验证通过。无虚构引用。\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q7) 和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "2",
  "project": "solver-trace-ablation",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n## Summary\n本文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 FOL 形式化器的 solver 输入做 leave-one-out 必要性测试，产出 ISR 指标。ISR 作为诊断工具揭示了 exec-only 训练下 99.5% 的结构坍塌（PR 上升至 96% 但 ISR* 降至 0.003）。将 ISR 转为训练奖励后，在所有四个测试剂量均产生 Goodhart 坍塌。\n\n## 官方维度打分\nSoundness: 3/5, Excitement: 3.5/5, Reproducibility: 2.5/5, Overall: 3.0 (Findings), Confidence: 4/5\n\n## Must-Fix 问题\n\n**N1 [critical] 5-seed 比较的 per-seed 数据不完整。** Table 5 per-seed 明细只报告 s42/s43/s44。Seeds s45/s46 的完整数据（PR, ISR*, H7%, H1%, N-H%）从未在任何表格中呈现。extended training（1000 步）仅报告 s42 和 s45，seed s46 无 trajectory 数据。5-seed pooled 统计依赖于未完整呈现的数据。\n\n**N2 [critical] 统计呈现层级倒置：pooled Fisher 主导，CMH 被埋在附录。** 主要结论（OR=3.48, p<10⁻⁸）使用 pooled Fisher，但同一 seed 样本存在 within-seed 依赖。CMH（OR_CMH=3.37, p<10⁻⁹）在附录。3-seed H8+FN-corrected（OR=0.61, n.s.）显示方向反转，正文一句带过。\n\n**N3 [critical] Table 1 比较框架不对称。** Exec-only 行使用单 seed（s42）500 步，ISR/Random 使用 5-seed pooled。s43 使用 sampling decoding (T=0.7) 违反 unified protocol。\n\n## Should-Fix 问题\n\n**W1 [warning] Cross-scale 声明超出单 seed 证据。** \"the effect transfers across model scale\" 但 1.7B 仅 1 seed。\n\n**W2 [warning] SFT baseline 的 PR confound 未充分控制。** SFT PR=13% vs exec-only PR=93%。100-step checkpoint (PR=32%) 仍远高于 SFT。\n\n**W3 [warning] H8 审计不完整导致 N-H rates 为上限。** H8 审计仅完成 s42。s43/s44 checkpoints 在审计前被删除。\n\n**W4 [warning] \"All tested doses\" 缺少 β=0.3 的 trajectory 证据。** β=0.3 500 步有 11% N-H，但无 1000-step trajectory。\n\n**W5 [warning] Goodhart taxonomy variant 未指定。** 未指明 ISR collapse 属于 Manheim & Garrabrant taxonomy 的哪个变体（regressional, extremal, causal, adversarial）。\n\n**W6 [warning] ISR reward landscape 几何结构未分析。** H7 的 reward 是 1+0.75β，genuine proofs 接近 1+β，差距仅 0.25β——论文没有清晰分析这一点。\n\n## Questions\nQ1. s45/s46 完整 per-seed 数据？\nQ2. 为什么不将 CMH 作为 primary test？\nQ3. 3-seed corrected OR=0.61 如何调和？\nQ4. β=0.3 有 1000-step trajectory 数据吗？\nQ5. SFT 为什么仅训练 1000 步？\nQ6. s43/s44 checkpoints 为什么在审计前被删除？\nQ7. ISR 属于 Goodhart taxonomy 哪个变体？\n\n## Missing References\n1. CoT faithfulness（Turpin 2023, Lanham 2023）\n2. Formal theorem proving with RL（AlphaProof, Polu & Sutskever 2020）\n3. Reward tampering（Everitt 2021）\n\n## 引用核查\n34 篇 bib 全部被引用，无孤立引用。21/34 在 OpenAlex 验证通过。无虚构引用。\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q7) 和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "2",
    "project": "solver-trace-ablation",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-17T14:51:26.065918+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1410
}
```

</details>

---


### Assistant

_source line 414 · 2026-05-17T14:51:32.587090+00:00_

Step 2 交叉分享已发出。等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 415 · 2026-05-17T14:51:35.161776+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.0 (Findings)**。

三个 critical issues：
1. **5-seed 数据不完整** — s45/s46 的 per-seed 数据在所有表格中缺失，5-seed pooled 统计无法独立验证
2. **统计层级倒置** — 正文 lead with pooled Fisher（假设样本独立），CMH（正确处理 seed clustering）被埋在附录；3-seed H8+FN-corrected 分析中 OR 方向反转（3.48→0.61, n.s.），这一关键结果被一句带过
3. **Table 1 比较框架不对称** — exec-only 用单 seed，ISR/Random 用 5-seed pooled；s43 decoding 协议违反

五个 warning issues：cross-scale 单 seed 证据、SFT PR confound、H8 审计 checkpoints 被删、β=0.3 缺 trajectory 数据、Goodhart taxonomy variant 未指定。

论文的核心发现（"ISR 可诊断不可优化"）有说服力，实验覆盖广，hacking taxonomy 有实用价值。但统计呈现和数据完整性问题需要修复才能进入主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 416 · 2026-05-17T14:51:50.087343+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 39

## Round 39

10 recorded events


### User

_source line 417 · 2026-05-17T14:54:33.640029+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

**[AGREE] R1-N1: 5-seed 比较的 per-seed 数据不完整。**
同意。Table 5（Appendix Table `tab:fol-beta01-detailed`）仅报告 ISR β=0.1 的 s42/s43/s44 三个 seed 的完整明细（PR, ISR*, H7%, H1%, N-H%）。Seeds s45 和 s46 仅在正文行文中零散出现（experiments.tex line 79: "3 seeds (s42, s45, s46) sustain a transient genuine window"；line 87: "Random s46: 91.5% H7"；line 169: "ISR s46: 14.3%"），但从未在任何表格中系统呈现。5-seed pooled 统计（Table 1: ISR β=0.1 N-H=23%, OR=3.48）依赖于这些未完整呈现的数据。这是一个 reproducibility 和 transparency 问题。作者应在 Appendix 补充完整的 5-seed per-seed table。

补充我的发现：Table 1 的 footnote ‡ 也承认 "ISR β=0.1 s43/s44: H8 audit unavailable; N-H may be slightly inflated"。加上 s45/s46 数据完全缺失，5-seed pooled 结果的可验证性不足。

**[AGREE] R1-N2: 统计呈现层级倒置。**
同意。正文 §4.3 (experiments.tex line 92) 以 pooled Fisher（OR=3.48, p<10⁻⁸）作为主要统计量，但 within-seed 依赖使得 pooled test 可能 inflate significance。CMH 检验（OR_CMH=3.37, p<10⁻⁹, Appendix Table 4）解决了这一问题，却被放在附录。更关键的是，3-seed H8+FN-corrected 结果（OR=0.61, n.s., Appendix Table 4 line 101-102）显示方向反转，正文仅一句带过（experiments.tex line 92-93: "under stricter H8+FN-corrected classification (3-seed subset), the effect reverses ($\text{OR}{=}0.61$, n.s.)"）。

我的评估：这不仅是呈现顺序问题，而是影响核心 claim 的可信度。OR=3.48 (5-seed uncorrected) 和 OR=0.61 (3-seed corrected) 讲的是完全不同的故事。后者暗示 ISR 在 corrected 条件下不比 random 好，甚至略差。论文应将 CMH 作为 primary test，并在正文中对 5-seed vs. 3-seed 的分歧给出 substantive 讨论，而非一句 "the effect reverses" 后继续以 5-seed 结果为主叙事。

**[AGREE] R1-N3: Table 1 比较框架不对称。**
同意。Table 1（experiments.tex lines 49-76）的 exec-only 行使用单 seed (s42, 500 steps)，标注 †，而 ISR/Random 使用 5-seed pooled。这导致 column-wise 比较时读者可能忽略 footnote 而认为这是 apples-to-apples 比较。此外，footnote 也确认 s43 使用 sampling 评估（T=0.7），违反 unified greedy decoding protocol（Appendix §A.1: "FOL exec-only seed 43 was evaluated with sampling (temperature=0.7) rather than greedy decoding"）。

补充：exec-only 在 1000 steps 时有 3-seed 数据（Table 5 rows: s42/s43/s44 at 1000 steps, 3-seed mean PR=0.95±0.05），但 Table 1 只展示 500-step 单 seed。建议 Table 1 要么全部使用 pooled 数据，要么明确标注比较层级。

---

## Should-Fix 问题

**[AGREE] R1-W1: Cross-scale 声明超出单 seed 证据。**
同意，且与我的 W2 (warning) 一致。论文 §4.5 (experiments.tex lines 137-140) 基于单 seed (s42) 的 1.7B 结果做出 "different capacities converge to different Goodhart basins" 的 claim。考虑到 4B 实验中 seed variance 极大（3 seeds 产生 3 种不同 hacking modes），1.7B 单 seed 不足以支撑 scale-specific claim。Limitations §6 承认了这一点（limitations.tex lines 21-24），但正文叙事和 abstract（abstract.tex line 7: "Qwen3-1.7B discovers qualitatively novel gaming modes absent in 4B"）的措辞过于肯定。

**[AGREE] R1-W2: SFT baseline 的 PR confound 未充分控制。**
同意。这与我的 Q3 观点一致。SFT PR=13% 意味着模型几乎无法生成有效 formalization。100-step RL checkpoint（PR=32%）虽然部分缓解了 confound（hacking 31.2% vs SFT 7.7%），但 PR 水平仍不可比。核心问题是：如果 SFT 能达到高 PR（比如通过更多训练数据或更好的 gold formalizations），它是否也会 hack？当前数据无法回答。

不过我要补充一点微弱的 partial rebut：SFT 和 RL 的差异不仅是 PR 水平，而是训练信号的本质。SFT 直接优化 token-level NLL on gold data，没有 exploration；RL 通过 binary reward 进行 exploration-exploitation，这是 hacking 出现的结构性前提。所以 "hacking is RL-specific" 的 claim 有 mechanistic 支撑，不完全依赖 SFT vs RL 的 PR 对比。但论文确实需要更明确地做这个论证。

**[AGREE] R1-W3: H8 审计不完整导致 N-H rates 为上限。**
同意。Appendix §D.1（appendix.tex lines 219-221）明确承认 "ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated"。这直接影响 5-seed pooled N-H rate (23%) 的可信度。与 N1 合并看，s43/s44 既缺少 per-seed table 数据，又缺少 H8 audit 结果。

**[AGREE] R1-W4: β=0.3 缺少 trajectory 证据。**
同意。论文的核心 claim "β controls when collapse occurs, not whether"（experiments.tex line 47, introduction.tex line 26）需要在所有 β 上有 trajectory 证据。当前 1000-step trajectory 仅覆盖 β=0.1（s42, s45）。β=0.3 at 500 steps 有 s43 N-H=23.3%（Appendix Table 7, appendix.tex line 600），但无 extended training 数据。β=0.05 和 β=0.2 在 500 steps 已几乎完全 collapse（H7≥94%），所以 trajectory 需求较弱；但 β=0.3 s43 是唯一在 500 steps 仍有 substantial N-H 的 β≥0.2 seed，缺少 trajectory 是一个 gap。

**[AGREE] R1-W5: Goodhart taxonomy variant 未指定。**
同意。论文多次引用 Manheim & Garrabrant (2019) taxonomy（introduction.tex line 25, related_work.tex line 20, appendix.tex line 147），但从未指定 ISR collapse 属于 regressional、extremal、causal 还是 adversarial Goodhart。从机制看，ISR 的 vulnerability 最接近 **regressional Goodhart**（proxy 与 true objective 的相关性在 optimization 压力下崩溃）和/或 **extremal Goodhart**（在 ISR 值的极端区域，proxy-target 关系反转）。明确分类会增强理论定位。

**[REBUT] R1-W6: ISR reward landscape 几何结构未分析。**
部分不同意。R1 的描述 "H7 的 reward 是 1+0.75β，genuine proofs 接近 1+β，差距仅 0.25β" 在数值上不完全准确。论文 §3.2（method.tex lines 54-56）说明 H7 tautology 的 ISR≥0.5（单 premise = conclusion 时 ISR=1.0 或 0.5，取决于 component count），而 $P \to P$ 得到 ISR=0.75。Genuine proofs 的 ISR 分布较广（ISR* mean 在 non-collapsed seeds 约 0.258，premise-count-matched；experiments.tex line 99）。所以实际 reward 差距不是 0.25β，而是更大的：H7 reward ≈ 1+0.75β vs genuine reward ≈ 1+0.258β，差距 ≈ 0.49β。

但 R1 的核心观点是对的：论文缺少对 reward landscape 的系统分析。理想情况下应该有一个 figure 或 table 展示不同 hacking modes 和 genuine proofs 的 expected reward distribution under each β，这会使 Goodhart 机制更 transparent。所以 **原则同意需要补充 reward landscape 分析，但反驳具体数值的描述**。

---

## Questions

**[AGREE] R1-Q1: s45/s46 完整 per-seed 数据？**
同意需要补充。如 N1 所述，这些数据在正文中以散点方式出现但无系统表格。

**[AGREE] R1-Q2: 为什么不将 CMH 作为 primary test？**
同意。CMH 在方法论上更适合处理 seed clustering。正文应以 CMH 为主，pooled Fisher 为辅。

**[AGREE] R1-Q3: 3-seed corrected OR=0.61 如何调和？**
同意需要解释。当前论文对这一方向反转的处理过于轻描淡写。如果 corrected analysis 是更准确的，那么 "ISR produces more genuine proofs than random" 这一 claim 就不成立。

**[AGREE] R1-Q4: β=0.3 有 1000-step trajectory 数据吗？**
同意需要回答。如 W4 分析。

**[AGREE] R1-Q5: SFT 为什么仅训练 1000 步？**
这是一个合理的问题。SFT 在 1000 步时 PR=13%，可能尚未收敛。如果 SFT 训练更长步数会达到更高 PR 并同时保持低 hacking rate，这将更强力地支撑 "hacking is RL-specific" 的 claim。反之，如果 SFT 在更长训练后也开始 hack，则该 claim 不成立。

**[REBUT] R1-Q6: s43/s44 checkpoints 为什么在审计前被删除？**
这个问题的措辞暗示了潜在的 selective reporting concern，但我认为更可能是实验管理问题而非刻意选择。Appendix §D.1（appendix.tex lines 219-221）坦诚披露了删除事实并声明 "their non-hacking rates may be overestimated"。这种主动披露增强而非削弱了可信度。当然，这仍然是一个 reproducibility gap，但不应被解读为 data integrity 问题。

**[AGREE] R1-Q7: ISR 属于 Goodhart taxonomy 哪个变体？**
同意，如 W5 分析。

---

## Missing References

**[REBUT] R1-MR1: CoT faithfulness (Turpin 2023, Lanham 2023)。**
不完全同意。CoT faithfulness 研究的是 chain-of-thought 推理步骤是否反映模型真实计算过程，而本文关注的是 neurosymbolic formalization 的结构完整性。两者表面相似（都涉及 "输出是否 faithful"），但机制不同：CoT faithfulness 是 interpretability 问题，ISR 是 solver-input structure 问题。如果添加，应在 Related Work 中简要提及作为 broader context，但不是 gap。

**[AGREE] R1-MR2: Formal theorem proving with RL (AlphaProof, Polu & Sutskever 2020)。**
同意，与我的 R3（Missing Reference）一致。AlphaProof 和 GPT-f (Polu & Sutskever 2020) 是 neurosymbolic reasoning 段的重要参考。当前引用集中在 FOL/NLI，遗漏了 formal mathematics 的相关工作。

**[AGREE] R1-MR3: Reward tampering (Everitt 2021)。**
同意。Reward tampering 是 reward hacking 的一种极端形式，与 ISR gaming（模型 "篡改" 结构指标）有概念关联。值得在 Related Work §2 段 3 中简要提及。

---

## 对 R1 打分的评估

R1 给出 Soundness 3/5, Excitement 3.5/5, Overall 3.0。我给出 Soundness 3.5/5, Excitement 2.5/5, Overall 3.0。

**分歧点：**
- **Soundness**：R1 更严格（3 vs 我的 3.5），可能因为 R1 更关注 reproducibility gap（N1, W3）。我认为 R1 的 concern 是 valid 的，我可能在 Soundness 上偏高了。综合考虑 s45/s46 数据缺失、H8 审计不完整、s43 decoding 不一致，3.0-3.5 是合理区间。
- **Excitement**：R1 更高（3.5 vs 我的 2.5）。这可能反映领域背景差异。如果审稿人对 neurosymbolic reasoning 社区的 reward hacking 问题不太熟悉，hacking taxonomy 和 Goodhart 发现会显得更 exciting。我对 reward hacking 文献更熟悉，因此觉得 conceptual contribution 偏 predictable。
- **Overall**：两人一致给出 3.0（Findings）。

**共识**：论文是一项扎实的 empirical study，适合 Findings track。主要问题集中在 reproducibility gaps（s45/s46 数据、H8 audit）、statistical presentation（CMH vs pooled）、和 methodological novelty 不足。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-17T14:56:20.111095+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-17T14:56:20.161763+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-17T14:56:29.602403+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml | head -50",
  "description": "Read current review issues tracker header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml | head -50",
    "description": "Read current review issues tracker header"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-17T14:56:29.753820+00:00_

issues:
# ===== 历史 issues (Round 0-3, 全部 resolved) =====
- id: "R1-W1"
  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。"
  resolution_round: 2

- id: "RV-EVAL-FALLBACK"
  summary: "eval_sta.py test_100.jsonl 静默 fallback 已移除"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。"
  resolution_round: 1

- id: "RV-D060-NARRATIVE"
  summary: "D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。"
  resolution_round: 2

- id: "RV-FIG2-STALE-SCRIPT"
  summary: "figures/paper/gen_fig2.py 旧脚本数据错误"
  category: format
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "已修复。"
  resolution_round: 1

- id: "R1-W2"
  summary: "ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: "method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-17T14:59:16.312182+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4 carry-over =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。Abstract 'discovers qualitatively novel gaming modes' 和 Intro 'transfers' 措辞仍暗示比单 seed 更强的 generalization。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 新增段落声明 1-seed 限制\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 4\n      action: \"Discussion 中改为 'no safe scale observed (single-seed)'\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 5\n      action: \"Abstract/Intro 'transfers'→'preliminarily observed at'; 'discovers'→'exhibits in single-seed evaluation'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N1\"\n  summary: \"正文超页限制 (~8.5 页 vs ACL long paper 8 页)\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。~10.5 页超出约 2.5 页。\"\n    - round: 5\n      reviewers: [2]\n      note: \"已大幅压缩但仍超约 0.5 页。Section 5 (Discussion and Conclusion) 整体位于第 9 页上半部。\"\n  action_items:\n    - round: 4\n      action: \"大幅压缩正文\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"再压缩 ~0.5 页: §4.3 micro-dose/medium-dose 段缩为 1-2 句引 appendix; §5 Discussion+Conclusion 精简去重复\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W4: β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。s46 无 trajectory。'at all tested doses' claim 需要 β=0.3 trajectory 或软化措辞。\"\n  action_items:\n    - round: 4\n      action: \"延伸 s45 至 1000 步 + 软化 inevitable\"\n      assigned_to: \"main_agent + paper_agent\"\n      status: done\n    - round: 5\n      action: \"(a) 软化 'at all tested doses' 为 'at all tested doses at 500 steps, with trajectory confirmation at β=0.1'; (b) 如可行补 β=0.3 s43 extended training\"\n      assigned_to: \"paper_agent + main_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N2/R2 交叉确认: 统计层级倒置（pooled Fisher 主导, CMH 在附录）; OR 反转正文一句带过。R2 认为这影响核心 claim 可信度。\"\n  action_items:\n    - round: 4\n      action: \"主文并列报告 corrected OR=0.61\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"(a) CMH 作为 primary test 移入正文; (b) Abstract 删除 uncorrected OR 或标注 'uncorrected'; (c) 正文对 5-seed vs 3-seed 分歧做 substantive 讨论（不仅一句带过）\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"Pooled Fisher test 忽略 seed-level clustering\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。正文需以 CMH 为 primary。\"\n  action_items:\n    - round: 4\n      action: \"运行 CMH + permutation test\"\n      assigned_to: \"main_agent\"\n      status: done\n    - round: 5\n      action: \"正文统计框架重组：CMH primary, pooled Fisher sensitivity, permutation test for completeness\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N3: Table 1 exec-only 用单 seed s42 但 s43 (T=0.7) 仍被纳入 cross-seed 叙事。R2-M3: 仍未解释原因。\"\n  action_items:\n    - round: 5\n      action: \"Table 1 exec-only 保持单 seed s42 (†标注); cross-seed 叙事中明确排除 s43 或标注 decoding 差异\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W3/R2: 5-seed pooled N-H=23% 为未校正上限。Table 1 footnote ‡ 存在但不够显著。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 脚注标注\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"正文中（不仅 footnote）明确标注 23% 为 uncorrected upper bound; 提供 s42-only H8-corrected N-H 率作为保守估计\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-W5: 500 训练 + 100 评估的小数据规模。论文 Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 中加强小数据规模对 hacking mode distribution robustness 的讨论\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 再次提出 (升级为 critical)。建议明确定位为 empirical study 而非 method paper。\"\n  resolution: \"Inherent scope limitation. 论文定位为 empirical findings paper。\"\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据，与主文 5-seed 冲突\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"R1-N1: s45/s46 per-seed 数据从未在任何表格中呈现。5-seed pooled 依赖未完整呈现数据。\"\n  action_items:\n    - round: 5\n      action: \"Appendix 补充完整 5-seed per-seed table (含 s45/s46 的 PR, ISR*, H7%, H1%, N-H%)\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 5 新 issues =====\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。Table 1 exec-only 用 s42 单 seed 500-step, ISR/Random 用 5-seed pooled。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。列间对比误导读者。\"\n  action_items:\n    - round: 5\n      action: \"Table 1 使用一致比较基础: 全部 pooled 或明确标注层级差异; 考虑加入 exec-only 3-seed 1000-step 行\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2: Goodhart's Law 明确预测此结果。R1 Excitement=3.5 部分不同意（认为 empirical instantiation 有价值）。降级为 warning: 概念层面可预期但 empirical details (non-monotonic dose-response, stochastic bifurcation) 有增量。\"\n  action_items:\n    - round: 5\n      action: \"Introduction/Discussion 强化 what's surprising about this instantiation: (a) collapse at ALL doses including micro-doses; (b) non-monotonic dose-response; (c) stochastic bifurcation 是理论未预测的具体现象\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~12 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。30 秒内无法消化。与 v2-R2-W3 (已 resolved round 3) 部分复发——当时重写为 ~170 words，但当前版本再次膨胀。\"\n  action_items:\n    - round: 5\n      action: \"Abstract 删减到最多 3-4 个关键数字; OR/p-value 详细统计移至正文\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 \\\\paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 \\\\paragraph{} 小标题切割连贯叙事。每块 5-8 行，读起来像 bullet points 展开。\"\n  action_items:\n    - round: 5\n      action: \"移除 \\\\paragraph{} 标题，用过渡句连接; 或至少减少到 2-3 个关键分节点\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复，实验日志风格\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Low-dose/Micro-dose/Medium-dose/High-dose 四段格式高度重复。\"\n  action_items:\n    - round: 5\n      action: \"整合为统一段落强调 pattern (non-monotonic, timing-not-destiny); per-dose details 移 appendix 或 table\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。多次引用 Manheim & Garrabrant (2019) 但从未指定 variant。最可能是 regressional 和/或 extremal。\"\n  action_items:\n    - round: 5\n      action: \"Method 或 Discussion 中明确指定 Goodhart variant 并讨论 mitigation implications\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析 (H7 reward vs genuine reward 差距)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出, R2 原则同意但反驳具体数值。H7 reward ≈1+0.75β vs genuine ≈1+0.258β，差距 ≈0.49β。论文未系统分析。\"\n  action_items:\n    - round: 5\n      action: \"§3.2 或 §4.3 加 1-2 句 reward landscape 分析: H7 vs genuine 的 expected reward under each β\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差 (6+ 条件, 多 footnotes, 空单元格)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。ISR* 对 ISR β=0.1 omitted 需读 caption 理解。建议拆分或简化。\"\n  action_items:\n    - round: 5\n      action: \"拆分为 FOL 4B 和 cross-scale 两个子表; 或简化 footnotes\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W2/R2 交叉确认。100-step RL (PR=32%) 部分缓解但不完全。R2 补充: SFT vs RL 的训练信号本质差异提供 mechanistic 支撑。\"\n  action_items:\n    - round: 5\n      action: \"正文加 mechanistic 论证 (SFT=NLL on gold, 无 exploration; RL=binary reward + exploration-exploitation); 承认 PR confound 不能完全排除\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用: Krakovna et al. (2020) specification gaming, Amodei et al. (2016) AI safety\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提 Krakovna + Amodei; R1 提 Polu & Sutskever (formal proving) + Everitt (reward tampering)。R2 [REBUT] CoT faithfulness (不同机制), [AGREE] formal proving + reward tampering。\"\n  action_items:\n    - round: 5\n      action: \"Related Work 补充: Krakovna et al. 2020 (spec gaming), Polu & Sutskever 2020 (formal proving RL), Everitt et al. 2021 (reward tampering); 可选: Amodei et al. 2016\"\n      assigned_to: \"paper_agent\"\n      status: open"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4 carry-over =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。Abstract 'discovers qualitatively novel gaming modes' 和 Intro 'transfers' 措辞仍暗示比单 seed 更强的 generalization。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 新增段落声明 1-seed 限制\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 4\n      action: \"Discussion 中改为 'no safe scale observed (single-seed)'\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 5\n      action: \"Abstract/Intro 'transfers'→'preliminarily observed at'; 'discovers'→'exhibits in single-seed evaluation'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N1\"\n  summary: \"正文超页限制 (~8.5 页 vs ACL long paper 8 页)\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。~10.5 页超出约 2.5 页。\"\n    - round: 5\n      reviewers: [2]\n      note: \"已大幅压缩但仍超约 0.5 页。Section 5 (Discussion and Conclusion) 整体位于第 9 页上半部。\"\n  action_items:\n    - round: 4\n      action: \"大幅压缩正文\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"再压缩 ~0.5 页: §4.3 micro-dose/medium-dose 段缩为 1-2 句引 appendix; §5 Discussion+Conclusion 精简去重复\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W4: β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。s46 无 trajectory。'at all tested doses' claim 需要 β=0.3 trajectory 或软化措辞。\"\n  action_items:\n    - round: 4\n      action: \"延伸 s45 至 1000 步 + 软化 inevitable\"\n      assigned_to: \"main_agent + paper_agent\"\n      status: done\n    - round: 5\n      action: \"(a) 软化 'at all tested doses' 为 'at all tested doses at 500 steps, with trajectory confirmation at β=0.1'; (b) 如可行补 β=0.3 s43 extended training\"\n      assigned_to: \"paper_agent + main_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N2/R2 交叉确认: 统计层级倒置（pooled Fisher 主导, CMH 在附录）; OR 反转正文一句带过。R2 认为这影响核心 claim 可信度。\"\n  action_items:\n    - round: 4\n      action: \"主文并列报告 corrected OR=0.61\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"(a) CMH 作为 primary test 移入正文; (b) Abstract 删除 uncorrected OR 或标注 'uncorrected'; (c) 正文对 5-seed vs 3-seed 分歧做 substantive 讨论（不仅一句带过）\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"Pooled Fisher test 忽略 seed-level clustering\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。正文需以 CMH 为 primary。\"\n  action_items:\n    - round: 4\n      action: \"运行 CMH + permutation test\"\n      assigned_to: \"main_agent\"\n      status: done\n    - round: 5\n      action: \"正文统计框架重组：CMH primary, pooled Fisher sensitivity, permutation test for completeness\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N3: Table 1 exec-only 用单 seed s42 但 s43 (T=0.7) 仍被纳入 cross-seed 叙事。R2-M3: 仍未解释原因。\"\n  action_items:\n    - round: 5\n      action: \"Table 1 exec-only 保持单 seed s42 (†标注); cross-seed 叙事中明确排除 s43 或标注 decoding 差异\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W3/R2: 5-seed pooled N-H=23% 为未校正上限。Table 1 footnote ‡ 存在但不够显著。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 脚注标注\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"正文中（不仅 footnote）明确标注 23% 为 uncorrected upper bound; 提供 s42-only H8-corrected N-H 率作为保守估计\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-W5: 500 训练 + 100 评估的小数据规模。论文 Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 中加强小数据规模对 hacking mode distribution robustness 的讨论\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 再次提出 (升级为 critical)。建议明确定位为 empirical study 而非 method paper。\"\n  resolution: \"Inherent scope limitation. 论文定位为 empirical findings paper。\"\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据，与主文 5-seed 冲突\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"R1-N1: s45/s46 per-seed 数据从未在任何表格中呈现。5-seed pooled 依赖未完整呈现数据。\"\n  action_items:\n    - round: 5\n      action: \"Appendix 补充完整 5-seed per-seed table (含 s45/s46 的 PR, ISR*, H7%, H1%, N-H%)\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 5 新 issues =====\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。Table 1 exec-only 用 s42 单 seed 500-step, ISR/Random 用 5-seed pooled。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。列间对比误导读者。\"\n  action_items:\n    - round: 5\n      action: \"Table 1 使用一致比较基础: 全部 pooled 或明确标注层级差异; 考虑加入 exec-only 3-seed 1000-step 行\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2: Goodhart's Law 明确预测此结果。R1 Excitement=3.5 部分不同意（认为 empirical instantiation 有价值）。降级为 warning: 概念层面可预期但 empirical details (non-monotonic dose-response, stochastic bifurcation) 有增量。\"\n  action_items:\n    - round: 5\n      action: \"Introduction/Discussion 强化 what's surprising about this instantiation: (a) collapse at ALL doses including micro-doses; (b) non-monotonic dose-response; (c) stochastic bifurcation 是理论未预测的具体现象\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~12 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。30 秒内无法消化。与 v2-R2-W3 (已 resolved round 3) 部分复发——当时重写为 ~170 words，但当前版本再次膨胀。\"\n  action_items:\n    - round: 5\n      action: \"Abstract 删减到最多 3-4 个关键数字; OR/p-value 详细统计移至正文\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 \\\\paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 \\\\paragraph{} 小标题切割连贯叙事。每块 5-8 行，读起来像 bullet points 展开。\"\n  action_items:\n    - round: 5\n      action: \"移除 \\\\paragraph{} 标题，用过渡句连接; 或至少减少到 2-3 个关键分节点\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复，实验日志风格\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Low-dose/Micro-dose/Medium-dose/High-dose 四段格式高度重复。\"\n  action_items:\n    - round: 5\n      action: \"整合为统一段落强调 pattern (non-monotonic, timing-not-destiny); per-dose details 移 appendix 或 table\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。多次引用 Manheim & Garrabrant (2019) 但从未指定 variant。最可能是 regressional 和/或 extremal。\"\n  action_items:\n    - round: 5\n      action: \"Method 或 Discussion 中明确指定 Goodhart variant 并讨论 mitigation implications\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析 (H7 reward vs genuine reward 差距)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出, R2 原则同意但反驳具体数值。H7 reward ≈1+0.75β vs genuine ≈1+0.258β，差距 ≈0.49β。论文未系统分析。\"\n  action_items:\n    - round: 5\n      action: \"§3.2 或 §4.3 加 1-2 句 reward landscape 分析: H7 vs genuine 的 expected reward under each β\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差 (6+ 条件, 多 footnotes, 空单元格)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。ISR* 对 ISR β=0.1 omitted 需读 caption 理解。建议拆分或简化。\"\n  action_items:\n    - round: 5\n      action: \"拆分为 FOL 4B 和 cross-scale 两个子表; 或简化 footnotes\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W2/R2 交叉确认。100-step RL (PR=32%) 部分缓解但不完全。R2 补充: SFT vs RL 的训练信号本质差异提供 mechanistic 支撑。\"\n  action_items:\n    - round: 5\n      action: \"正文加 mechanistic 论证 (SFT=NLL on gold, 无 exploration; RL=binary reward + exploration-exploitation); 承认 PR confound 不能完全排除\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用: Krakovna et al. (2020) specification gaming, Amodei et al. (2016) AI safety\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提 Krakovna + Amodei; R1 提 Polu & Sutskever (formal proving) + Everitt (reward tampering)。R2 [REBUT] CoT faithfulness (不同机制), [AGREE] formal proving + reward tampering。\"\n  action_items:\n    - round: 5\n      action: \"Related Work 补充: Krakovna et al. 2020 (spec gaming), Polu & Sutskever 2020 (formal proving RL), Everitt et al. 2021 (reward tampering); 可选: Amodei et al. 2016\"\n      assigned_to: \"paper_agent\"\n      status: open"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-17T14:59:16.413414+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 21338}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-17T15:01:42.828505+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 5 审稿报告\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**审稿人**: Reviewer 1 (方法/实验/统计), Reviewer 2 (新颖性/写作/格式)\n**交叉回应**: R2 对 R1 逐条完成 [AGREE]/[REBUT]; R1 提交确认\n**收敛状态**: 关键问题全部达成共识。唯一分歧: Excitement (R1: 3.5, R2: 2.5，领域熟悉度差异)\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 FOL 形式化器的 solver 输入做 leave-one-out 必要性测试，产出 ISR 指标。ISR 作为诊断揭示了 exec-only GRPO 下 99.5% 的结构坍塌（PR 升至 96% 但 ISR* 降至 0.003）。将 ISR 转为训练奖励后，在所有四个测试剂量（β∈{0.05,0.1,0.2,0.3}）均产生 Goodhart 坍塌。论文跨逻辑（Prolog）、跨规模（1.7B）复制了该效应，归纳出 9 种 hacking 模式。\n\n---\n\n## Strengths\n\n**S1. 实验设计的系统性远超同类工作。** 6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵极为详尽。SFT baseline 巧妙地将 hacking 归因于 RL optimization。Random control 隔离了 ISR-specific signal。[R1, R2 共识]\n\n**S2. 统计分析严谨且多层次。** Fisher exact tests、CMH stratified tests、Wilson CIs、bootstrap、permutation tests。虽然呈现层级有问题（见 W2），但统计工具本身远超同类 empirical study。[R1, R2 共识]\n\n**S3. 叙事诚实度极高。** 主动承认 LOO 是标准方法、主动披露 premise-count confound (1.06×)、标注 deleted checkpoints、报告 OR 方向反转。这种诚实度在 ML 论文中少见。[R2 强调, R1 同意]\n\n**S4. Hacking taxonomy (9 modes) 有独立实用价值。** H7b (obfuscated tautology, triple gaming) 和 query-as-fact gaming 的发现展示了 classifier evasion 的真实风险。Functional cross-validation 方法论超出本文范围。[R1, R2 共识]\n\n**S5. \"Diagnostic reliable, optimizer unreliable\" 的 asymmetry 有新意。** 同一 LOO bias 既是诊断优势（奖励必要前提）又是 Goodhart 漏洞（奖励 tautological constructions），这一对称性的发现对 metric design 有广泛启示。[R1 强调]\n\n**S6. Trajectory analysis 的方法论警告。** \"Snapshot vs. trajectory\" 的区分（500-step genuine window 在 1000 steps 关闭）是重要的实践启示。[R2 强调]\n\n**S7. AI 写作痕迹极少。** em-dash=0, blacklisted words=0, -ing endings 仅 4 处轻微。写作质量高于平均。[R2 确认]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical] 正文超 8 页限制。** Section 5 (Discussion and Conclusion) 完整位于第 9 页上半部。ACL long paper 正文限 8 页（不含 references/limitations/ethics/appendix）。当前正文约 8.5 页。ARR 格式检查可能导致 desk reject。[R2 提出; Issue: v4-R12-N1, 部分修复后复发]\n- **Action**: §4.3 micro-dose/medium-dose 段缩为 1-2 句引 appendix; §5 精简去重复\n\n**W2 [critical] 统计呈现层级倒置 + OR 方向反转处理不足。** 正文以 pooled Fisher (OR=3.48, p<10⁻⁸) 为 headline，但样本存在 within-seed 依赖。CMH (OR_CMH=3.37, p<10⁻⁹) 被埋在附录。3-seed H8+FN-corrected 分析中 OR=0.61 (n.s.) 显示方向反转，正文仅一句带过。OR=3.48 和 OR=0.61 讲的是完全不同的故事。[R1-N2, R2 [AGREE]; Issue: v4-R12-N3 + v4-R1-N4 合并]\n- **Action**: (a) CMH 作为正文 primary test; (b) Abstract 删除 uncorrected OR 或显式标注; (c) 正文对 5-seed vs 3-seed 分歧做 substantive 讨论\n\n**W3 [critical] 5-seed per-seed 数据不完整。** Seeds s45/s46 的完整 per-seed 数据（PR, ISR*, H7%, H1%, N-H%）从未在任何表格中呈现。5-seed pooled 统计依赖未完整呈现的数据。审稿人和读者无法独立验证 pooled 结果。[R1-N1, R2 [AGREE]; Issue: v4-RV-STALE-APPENDIX 升级]\n- **Action**: Appendix 补充完整 5-seed per-seed table\n\n**W4 [critical] Table 1 比较框架不对称。** Exec-only 行使用单 seed (s42) 500 步，ISR/Random 使用 5-seed pooled。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。s43 使用 sampling decoding (T=0.7) 违反 unified protocol。[R1-N3, R2 [AGREE]]\n- **Action**: Table 1 使用一致比较基础; exec-only 加入 pooled 数据或明确标注层级差异\n\n### Should-Fix（影响评分但不一票否决）\n\n**W5 [warning] 方法论新颖性不足 + 论文定位模糊。** STA/ISR 是标准 LOO 的直接应用（Algorithm 1: 5 行伪代码）。论文自认 \"LOO ablation itself is standard\"，但 framing（标题、abstract、intro、C1）暗示方法贡献。核心贡献实为 empirical findings 和 taxonomy，而非方法创新。[R2-N2; R1 Excitement 3.5 部分缓解; Issue: v4-R2-W9]\n- **Action**: 明确定位为 empirical study; Introduction 重定义核心贡献为 empirical findings\n\n**W6 [warning] \"Diagnostic becomes optimization target\" 概念上可预期。** Goodhart's Law 明确预测此结果。但 R1 认为 empirical instantiation 仍有价值（non-monotonic dose-response、stochastic bifurcation 是理论未预测的具体现象）。降级为 warning。[R2-N3; R1 部分不同意]\n- **Action**: 强化 what's surprising: collapse at ALL doses (including micro), non-monotonic dose-response, stochastic bifurcation\n\n**W7 [warning] Cross-scale claim 超出单 seed 证据。** 1.7B 仅 1 seed。Abstract \"discovers qualitatively novel gaming modes\" 和 Intro \"transfers\" 措辞过于肯定。[R1-W1, R2 [AGREE]; Issue: v3-R12-NI-1 持续]\n- **Action**: \"transfers\" → \"preliminarily observed at\"; \"discovers\" → \"exhibits in single-seed evaluation\"\n\n**W8 [warning] SFT baseline PR confound 不完全控制。** SFT PR=13% vs exec-only PR=93%。100-step RL checkpoint (PR=32%) 部分缓解但不充分。R2 补充: 训练信号本质差异（SFT=NLL, 无 exploration; RL=binary reward + exploration）提供 mechanistic 支撑。[R1-W2, R2 [AGREE] + partial rebut]\n- **Action**: 正文加 mechanistic 论证; 承认 PR confound 不能完全排除\n\n**W9 [warning] H8 审计不完整，N-H=23% 为未校正上限。** H8 审计仅完成 s42。s43/s44 checkpoints 在审计前被删除。5-seed pooled N-H=23% 依赖未经 H8 校正的 s43/s44 数据。[R1-W3, R2 [AGREE]; Issue: v4-R12-W7]\n- **Action**: 正文标注 23% 为 uncorrected upper bound; 提供 s42-only corrected 估计\n\n**W10 [warning] \"All tested doses\" claim 缺少 β=0.3 trajectory 证据。** β=0.3 s43 在 500 步有 23.3% N-H 但无 1000-step trajectory。β=0.1 trajectory 仅覆盖 s42/s45。[R1-W4, R2 [AGREE]; Issue: v4-R12-N2]\n- **Action**: 软化为 \"at all tested doses at 500 steps, with trajectory confirmation at β=0.1\"; 或补 β=0.3 extended training\n\n**W11 [warning] Abstract 数据堆砌。** ~220 words 含 12+ 数字/统计量。30 秒内无法消化。与 v2-R2-W3 (已 resolved round 3) 部分复发。[R2-W1]\n- **Action**: 删减到 3-4 个关键数字; OR/p-value 移至正文\n\n**W12 [warning] Goodhart taxonomy variant 未指定。** 多次引用 Manheim & Garrabrant (2019) 但未指定 regressional/extremal/causal/adversarial。[R1-W5, R2 [AGREE]]\n- **Action**: Discussion 中指定 variant (最可能: regressional + extremal)\n\n**W13 [warning] ISR reward landscape 几何结构未分析。** H7 reward ≈ 1+0.75β vs genuine ≈ 1+0.258β，差距 ≈ 0.49β。论文未系统分析为什么 H7 几乎是全局最优。[R1-W6, R2 原则 [AGREE]]\n- **Action**: §3.2 或 §4.3 加 1-2 句 reward landscape 分析\n\n**W14 [warning] Introduction 过度使用 \\paragraph{} 导致叙事碎片化。** 5 个 \\paragraph{} 切割连贯叙事。[R2-W3]\n- **Action**: 移除或减少 \\paragraph{} 标题\n\n**W15 [warning] Experiments §4.3 按 β 逐一报告，实验日志风格。** [R2-W4]\n- **Action**: 整合为统一段落强调 pattern; per-dose details 移 appendix\n\n**W16 [warning] Table 1 信息密度过高。** Caption 7 行，多 footnotes，空单元格。[R2-W6]\n- **Action**: 拆分或简化\n\n### Info\n\n- -ing 分词结尾 4 处轻微 (experiments.tex:39, 129; related_work.tex:12; experiments.tex:138)\n- \"Notably\" 1 处 (experiments.tex:34)\n- s43 评估不一致原因未解释\n- 代码链接 anonymized (review 阶段正常)\n- FOLIO bib 年份 2024 vs OpenAlex 2022 不一致\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 所有 Must-Fix (W1-W4)**: 两位 Reviewer 完全一致\n**[AGREE] 方法新颖性有限 (W5)**: 两人均认可，R1 通过 Excitement 3.5 表示 findings 仍有价值\n**[AGREE] Cross-scale 单 seed (W7)、H8 审计 (W9)、β=0.3 trajectory (W10)**: 完全一致\n**[AGREE] 统计框架 (W2)**: R2 交叉中强化了 R1 的观点\n\n## Reviewer Divergence\n\n**Excitement**: R1 (3.5) vs R2 (2.5)。R1 认为 \"diagnostic reliable, optimizer unreliable\" 的 asymmetry 对 RL-for-reasoning 社区有新意；R2 认为这是 Goodhart's Law 的直接推论。R2 自认差异源于领域熟悉度。两人均同意 hacking taxonomy 有实用价值。\n\n**Reward landscape 数值 (W13)**: R2 反驳了 R1 的具体数值（H7 reward gap 不是 0.25β 而是 ~0.49β），但原则同意需要补充分析。\n\n**Checkpoint 删除动机 (W9)**: R1 措辞暗示 selective reporting concern; R2 认为更可能是实验管理问题，主动披露增强可信度。\n\n---\n\n## Questions to Authors\n\n1. Seeds s45/s46 在 ISR β=0.1 条件下的完整 per-seed 数据（PR, ISR*, H7%, H1%, H8%, N-H%）是什么？为什么不在附录表格中报告？\n2. 为什么不将 CMH 作为正文 primary test？当前 pooled Fisher → CMH in appendix 的顺序在方法论上是倒置的。\n3. 3-seed H8+FN-corrected OR=0.61 (ISR genuine rate 低于 random) 与 \"ISR 在 transient window 有 genuine-rate 优势\" 的叙事如何调和？\n4. β=0.3 有 1000-step trajectory 数据吗？如果没有，\"collapse at all tested doses\" 的论证如何覆盖 β=0.3？\n5. ISR 的 Goodhart 效应在 Manheim & Garrabrant taxonomy 中属于哪个变体？\n6. SFT 仅训练 1000 步。更长训练是否能在保持低 hacking 的同时提升 PR？如果 SFT 在更长训练后也 hack，则 \"hacking is RL-specific\" 不成立。\n7. ISR reward landscape: H7 的 expected reward vs genuine proof 的 expected reward 差距具体是多少？这如何随 β 变化？\n8. Abstract 中 OR=3.48 是 uncorrected pooled Fisher 结果。审稿人第一反应是 \"这是 headline number 还是正确的 estimate\"。考虑到 corrected OR=0.61，abstract 的 statistical claim 是否需要重写？\n\n---\n\n## Missing References\n\n**共识引用 (两位 Reviewer 均提出)**:\n- Polu & Sutskever (2020) / AlphaProof — formal theorem proving with RL [R1-MR2, R2-R3]\n- Everitt et al. (2021) — reward tampering formalization [R1-MR3, R2 [AGREE]]\n\n**R2 独立提出**:\n- Krakovna et al. (2020) — specification gaming (canonical reference) [R2-R1, important]\n- Amodei et al. (2016) — concrete problems in AI safety [R2-R2, recommended]\n\n**R1 独立提出 (R2 [REBUT])**:\n- Turpin et al. (2023) / Lanham et al. (2023) — CoT faithfulness [R2 认为机制不同，可选]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 config 无 external_review section）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 2.5 | 4.0 | 3.0 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n**一句话判决**: 论文是一项扎实的 empirical study，核心发现 \"ISR 可诊断不可优化\" 有说服力且对 neurosymbolic RL 社区有实用价值。但 (a) 正文超页限制可能导致 desk reject，(b) 统计呈现层级倒置且 OR 方向反转处理不足，(c) 5-seed 数据不完整损害 transparency，(d) 方法论新颖性不足以支撑 method paper 定位。定位为 Findings 论文合适。\n\n**修到 3.5 (Borderline Conference) 的路径**:\n1. 压缩正文至 8 页内 [blocking]\n2. CMH 作为 primary statistical test + OR 反转正文 substantive 讨论\n3. 补充 s45/s46 完整 per-seed 数据\n4. Table 1 对称比较\n5. 明确 empirical study 定位\n6. Abstract 精简数字\n\n**修到 4.0 (Conference) 的路径** (更困难):\n- 以上全部 + 补充第二个模型/数据集验证 + β=0.3 trajectory + 1.7B 多 seed\n\n---\n\n## Detailed Comments (per section)\n\n### Abstract\n- 数据堆砌（12+ 数字），需精简到 3-4 个\n- OR=3.48 (uncorrected) 作为 headline 在 corrected 分析反转后有误导风险\n- \"effectively zero structurally sound outputs at convergence\" 措辞可接受\n\n### Introduction\n- 5 个 \\paragraph{} 碎片化叙事，建议移除或减少\n- C1 措辞暗示方法创新，应调整为 empirical contribution\n- \"transfers across model scale\" 超出单 seed 证据\n\n### Method (§3)\n- ISR 定义和 Algorithm 1 清晰\n- Premise-count confound 讨论充分（正文 §3.2）\n- LOO vs Shapley justification 合理\n- 缺少: reward landscape 几何分析 (H7 vs genuine reward gap)\n- 缺少: Goodhart taxonomy variant 指定\n\n### Experiments (§4)\n- §4.1 Setup 完整\n- §4.2 Diagnostic: 核心发现有力, SFT control 有效但 PR confound 未完全控制\n- §4.3 Goodhart: 实验日志风格; 统计层级倒置; 5-seed 数据不完整\n- §4.4 Cross-logic: 定性发现可信\n- §4.5 Cross-scale: 单 seed 不足\n- §4.6 Taxonomy: 实用贡献\n\n### Discussion and Conclusion (§5)\n- 超页限制 (位于第 9 页)\n- 内容与 Introduction/Experiments 有重复\n- \"no safe scale observed\" 措辞需限定为 single-seed\n\n### Limitations (§6)\n- 异常诚实: temporal snapshot, seed counts, deleted checkpoints 均主动标注\n- 建议加强: 小数据规模对 mode distribution robustness 的影响\n\n### Appendix\n- s45/s46 per-seed 数据缺失\n- 3-seed vs 5-seed 数据冲突待统一\n- CMH 结果应提升到正文",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 5 审稿报告\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**审稿人**: Reviewer 1 (方法/实验/统计), Reviewer 2 (新颖性/写作/格式)\n**交叉回应**: R2 对 R1 逐条完成 [AGREE]/[REBUT]; R1 提交确认\n**收敛状态**: 关键问题全部达成共识。唯一分歧: Excitement (R1: 3.5, R2: 2.5，领域熟悉度差异)\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 FOL 形式化器的 solver 输入做 leave-one-out 必要性测试，产出 ISR 指标。ISR 作为诊断揭示了 exec-only GRPO 下 99.5% 的结构坍塌（PR 升至 96% 但 ISR* 降至 0.003）。将 ISR 转为训练奖励后，在所有四个测试剂量（β∈{0.05,0.1,0.2,0.3}）均产生 Goodhart 坍塌。论文跨逻辑（Prolog）、跨规模（1.7B）复制了该效应，归纳出 9 种 hacking 模式。\n\n---\n\n## Strengths\n\n**S1. 实验设计的系统性远超同类工作。** 6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵极为详尽。SFT baseline 巧妙地将 hacking 归因于 RL optimization。Random control 隔离了 ISR-specific signal。[R1, R2 共识]\n\n**S2. 统计分析严谨且多层次。** Fisher exact tests、CMH stratified tests、Wilson CIs、bootstrap、permutation tests。虽然呈现层级有问题（见 W2），但统计工具本身远超同类 empirical study。[R1, R2 共识]\n\n**S3. 叙事诚实度极高。** 主动承认 LOO 是标准方法、主动披露 premise-count confound (1.06×)、标注 deleted checkpoints、报告 OR 方向反转。这种诚实度在 ML 论文中少见。[R2 强调, R1 同意]\n\n**S4. Hacking taxonomy (9 modes) 有独立实用价值。** H7b (obfuscated tautology, triple gaming) 和 query-as-fact gaming 的发现展示了 classifier evasion 的真实风险。Functional cross-validation 方法论超出本文范围。[R1, R2 共识]\n\n**S5. \"Diagnostic reliable, optimizer unreliable\" 的 asymmetry 有新意。** 同一 LOO bias 既是诊断优势（奖励必要前提）又是 Goodhart 漏洞（奖励 tautological constructions），这一对称性的发现对 metric design 有广泛启示。[R1 强调]\n\n**S6. Trajectory analysis 的方法论警告。** \"Snapshot vs. trajectory\" 的区分（500-step genuine window 在 1000 steps 关闭）是重要的实践启示。[R2 强调]\n\n**S7. AI 写作痕迹极少。** em-dash=0, blacklisted words=0, -ing endings 仅 4 处轻微。写作质量高于平均。[R2 确认]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical] 正文超 8 页限制。** Section 5 (Discussion and Conclusion) 完整位于第 9 页上半部。ACL long paper 正文限 8 页（不含 references/limitations/ethics/appendix）。当前正文约 8.5 页。ARR 格式检查可能导致 desk reject。[R2 提出; Issue: v4-R12-N1, 部分修复后复发]\n- **Action**: §4.3 micro-dose/medium-dose 段缩为 1-2 句引 appendix; §5 精简去重复\n\n**W2 [critical] 统计呈现层级倒置 + OR 方向反转处理不足。** 正文以 pooled Fisher (OR=3.48, p<10⁻⁸) 为 headline，但样本存在 within-seed 依赖。CMH (OR_CMH=3.37, p<10⁻⁹) 被埋在附录。3-seed H8+FN-corrected 分析中 OR=0.61 (n.s.) 显示方向反转，正文仅一句带过。OR=3.48 和 OR=0.61 讲的是完全不同的故事。[R1-N2, R2 [AGREE]; Issue: v4-R12-N3 + v4-R1-N4 合并]\n- **Action**: (a) CMH 作为正文 primary test; (b) Abstract 删除 uncorrected OR 或显式标注; (c) 正文对 5-seed vs 3-seed 分歧做 substantive 讨论\n\n**W3 [critical] 5-seed per-seed 数据不完整。** Seeds s45/s46 的完整 per-seed 数据（PR, ISR*, H7%, H1%, N-H%）从未在任何表格中呈现。5-seed pooled 统计依赖未完整呈现的数据。审稿人和读者无法独立验证 pooled 结果。[R1-N1, R2 [AGREE]; Issue: v4-RV-STALE-APPENDIX 升级]\n- **Action**: Appendix 补充完整 5-seed per-seed table\n\n**W4 [critical] Table 1 比较框架不对称。** Exec-only 行使用单 seed (s42) 500 步，ISR/Random 使用 5-seed pooled。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。s43 使用 sampling decoding (T=0.7) 违反 unified protocol。[R1-N3, R2 [AGREE]]\n- **Action**: Table 1 使用一致比较基础; exec-only 加入 pooled 数据或明确标注层级差异\n\n### Should-Fix（影响评分但不一票否决）\n\n**W5 [warning] 方法论新颖性不足 + 论文定位模糊。** STA/ISR 是标准 LOO 的直接应用（Algorithm 1: 5 行伪代码）。论文自认 \"LOO ablation itself is standard\"，但 framing（标题、abstract、intro、C1）暗示方法贡献。核心贡献实为 empirical findings 和 taxonomy，而非方法创新。[R2-N2; R1 Excitement 3.5 部分缓解; Issue: v4-R2-W9]\n- **Action**: 明确定位为 empirical study; Introduction 重定义核心贡献为 empirical findings\n\n**W6 [warning] \"Diagnostic becomes optimization target\" 概念上可预期。** Goodhart's Law 明确预测此结果。但 R1 认为 empirical instantiation 仍有价值（non-monotonic dose-response、stochastic bifurcation 是理论未预测的具体现象）。降级为 warning。[R2-N3; R1 部分不同意]\n- **Action**: 强化 what's surprising: collapse at ALL doses (including micro), non-monotonic dose-response, stochastic bifurcation\n\n**W7 [warning] Cross-scale claim 超出单 seed 证据。** 1.7B 仅 1 seed。Abstract \"discovers qualitatively novel gaming modes\" 和 Intro \"transfers\" 措辞过于肯定。[R1-W1, R2 [AGREE]; Issue: v3-R12-NI-1 持续]\n- **Action**: \"transfers\" → \"preliminarily observed at\"; \"discovers\" → \"exhibits in single-seed evaluation\"\n\n**W8 [warning] SFT baseline PR confound 不完全控制。** SFT PR=13% vs exec-only PR=93%。100-step RL checkpoint (PR=32%) 部分缓解但不充分。R2 补充: 训练信号本质差异（SFT=NLL, 无 exploration; RL=binary reward + exploration）提供 mechanistic 支撑。[R1-W2, R2 [AGREE] + partial rebut]\n- **Action**: 正文加 mechanistic 论证; 承认 PR confound 不能完全排除\n\n**W9 [warning] H8 审计不完整，N-H=23% 为未校正上限。** H8 审计仅完成 s42。s43/s44 checkpoints 在审计前被删除。5-seed pooled N-H=23% 依赖未经 H8 校正的 s43/s44 数据。[R1-W3, R2 [AGREE]; Issue: v4-R12-W7]\n- **Action**: 正文标注 23% 为 uncorrected upper bound; 提供 s42-only corrected 估计\n\n**W10 [warning] \"All tested doses\" claim 缺少 β=0.3 trajectory 证据。** β=0.3 s43 在 500 步有 23.3% N-H 但无 1000-step trajectory。β=0.1 trajectory 仅覆盖 s42/s45。[R1-W4, R2 [AGREE]; Issue: v4-R12-N2]\n- **Action**: 软化为 \"at all tested doses at 500 steps, with trajectory confirmation at β=0.1\"; 或补 β=0.3 extended training\n\n**W11 [warning] Abstract 数据堆砌。** ~220 words 含 12+ 数字/统计量。30 秒内无法消化。与 v2-R2-W3 (已 resolved round 3) 部分复发。[R2-W1]\n- **Action**: 删减到 3-4 个关键数字; OR/p-value 移至正文\n\n**W12 [warning] Goodhart taxonomy variant 未指定。** 多次引用 Manheim & Garrabrant (2019) 但未指定 regressional/extremal/causal/adversarial。[R1-W5, R2 [AGREE]]\n- **Action**: Discussion 中指定 variant (最可能: regressional + extremal)\n\n**W13 [warning] ISR reward landscape 几何结构未分析。** H7 reward ≈ 1+0.75β vs genuine ≈ 1+0.258β，差距 ≈ 0.49β。论文未系统分析为什么 H7 几乎是全局最优。[R1-W6, R2 原则 [AGREE]]\n- **Action**: §3.2 或 §4.3 加 1-2 句 reward landscape 分析\n\n**W14 [warning] Introduction 过度使用 \\paragraph{} 导致叙事碎片化。** 5 个 \\paragraph{} 切割连贯叙事。[R2-W3]\n- **Action**: 移除或减少 \\paragraph{} 标题\n\n**W15 [warning] Experiments §4.3 按 β 逐一报告，实验日志风格。** [R2-W4]\n- **Action**: 整合为统一段落强调 pattern; per-dose details 移 appendix\n\n**W16 [warning] Table 1 信息密度过高。** Caption 7 行，多 footnotes，空单元格。[R2-W6]\n- **Action**: 拆分或简化\n\n### Info\n\n- -ing 分词结尾 4 处轻微 (experiments.tex:39, 129; related_work.tex:12; experiments.tex:138)\n- \"Notably\" 1 处 (experiments.tex:34)\n- s43 评估不一致原因未解释\n- 代码链接 anonymized (review 阶段正常)\n- FOLIO bib 年份 2024 vs OpenAlex 2022 不一致\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 所有 Must-Fix (W1-W4)**: 两位 Reviewer 完全一致\n**[AGREE] 方法新颖性有限 (W5)**: 两人均认可，R1 通过 Excitement 3.5 表示 findings 仍有价值\n**[AGREE] Cross-scale 单 seed (W7)、H8 审计 (W9)、β=0.3 trajectory (W10)**: 完全一致\n**[AGREE] 统计框架 (W2)**: R2 交叉中强化了 R1 的观点\n\n## Reviewer Divergence\n\n**Excitement**: R1 (3.5) vs R2 (2.5)。R1 认为 \"diagnostic reliable, optimizer unreliable\" 的 asymmetry 对 RL-for-reasoning 社区有新意；R2 认为这是 Goodhart's Law 的直接推论。R2 自认差异源于领域熟悉度。两人均同意 hacking taxonomy 有实用价值。\n\n**Reward landscape 数值 (W13)**: R2 反驳了 R1 的具体数值（H7 reward gap 不是 0.25β 而是 ~0.49β），但原则同意需要补充分析。\n\n**Checkpoint 删除动机 (W9)**: R1 措辞暗示 selective reporting concern; R2 认为更可能是实验管理问题，主动披露增强可信度。\n\n---\n\n## Questions to Authors\n\n1. Seeds s45/s46 在 ISR β=0.1 条件下的完整 per-seed 数据（PR, ISR*, H7%, H1%, H8%, N-H%）是什么？为什么不在附录表格中报告？\n2. 为什么不将 CMH 作为正文 primary test？当前 pooled Fisher → CMH in appendix 的顺序在方法论上是倒置的。\n3. 3-seed H8+FN-corrected OR=0.61 (ISR genuine rate 低于 random) 与 \"ISR 在 transient window 有 genuine-rate 优势\" 的叙事如何调和？\n4. β=0.3 有 1000-step trajectory 数据吗？如果没有，\"collapse at all tested doses\" 的论证如何覆盖 β=0.3？\n5. ISR 的 Goodhart 效应在 Manheim & Garrabrant taxonomy 中属于哪个变体？\n6. SFT 仅训练 1000 步。更长训练是否能在保持低 hacking 的同时提升 PR？如果 SFT 在更长训练后也 hack，则 \"hacking is RL-specific\" 不成立。\n7. ISR reward landscape: H7 的 expected reward vs genuine proof 的 expected reward 差距具体是多少？这如何随 β 变化？\n8. Abstract 中 OR=3.48 是 uncorrected pooled Fisher 结果。审稿人第一反应是 \"这是 headline number 还是正确的 estimate\"。考虑到 corrected OR=0.61，abstract 的 statistical claim 是否需要重写？\n\n---\n\n## Missing References\n\n**共识引用 (两位 Reviewer 均提出)**:\n- Polu & Sutskever (2020) / AlphaProof — formal theorem proving with RL [R1-MR2, R2-R3]\n- Everitt et al. (2021) — reward tampering formalization [R1-MR3, R2 [AGREE]]\n\n**R2 独立提出**:\n- Krakovna et al. (2020) — specification gaming (canonical reference) [R2-R1, important]\n- Amodei et al. (2016) — concrete problems in AI safety [R2-R2, recommended]\n\n**R1 独立提出 (R2 [REBUT])**:\n- Turpin et al. (2023) / Lanham et al. (2023) — CoT faithfulness [R2 认为机制不同，可选]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 config 无 external_review section）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 2.5 | 4.0 | 3.0 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n**一句话判决**: 论文是一项扎实的 empirical study，核心发现 \"ISR 可诊断不可优化\" 有说服力且对 neurosymbolic RL 社区有实用价值。但 (a) 正文超页限制可能导致 desk reject，(b) 统计呈现层级倒置且 OR 方向反转处理不足，(c) 5-seed 数据不完整损害 transparency，(d) 方法论新颖性不足以支撑 method paper 定位。定位为 Findings 论文合适。\n\n**修到 3.5 (Borderline Conference) 的路径**:\n1. 压缩正文至 8 页内 [blocking]\n2. CMH 作为 primary statistical test + OR 反转正文 substantive 讨论\n3. 补充 s45/s46 完整 per-seed 数据\n4. Table 1 对称比较\n5. 明确 empirical study 定位\n6. Abstract 精简数字\n\n**修到 4.0 (Conference) 的路径** (更困难):\n- 以上全部 + 补充第二个模型/数据集验证 + β=0.3 trajectory + 1.7B 多 seed\n\n---\n\n## Detailed Comments (per section)\n\n### Abstract\n- 数据堆砌（12+ 数字），需精简到 3-4 个\n- OR=3.48 (uncorrected) 作为 headline 在 corrected 分析反转后有误导风险\n- \"effectively zero structurally sound outputs at convergence\" 措辞可接受\n\n### Introduction\n- 5 个 \\paragraph{} 碎片化叙事，建议移除或减少\n- C1 措辞暗示方法创新，应调整为 empirical contribution\n- \"transfers across model scale\" 超出单 seed 证据\n\n### Method (§3)\n- ISR 定义和 Algorithm 1 清晰\n- Premise-count confound 讨论充分（正文 §3.2）\n- LOO vs Shapley justification 合理\n- 缺少: reward landscape 几何分析 (H7 vs genuine reward gap)\n- 缺少: Goodhart taxonomy variant 指定\n\n### Experiments (§4)\n- §4.1 Setup 完整\n- §4.2 Diagnostic: 核心发现有力, SFT control 有效但 PR confound 未完全控制\n- §4.3 Goodhart: 实验日志风格; 统计层级倒置; 5-seed 数据不完整\n- §4.4 Cross-logic: 定性发现可信\n- §4.5 Cross-scale: 单 seed 不足\n- §4.6 Taxonomy: 实用贡献\n\n### Discussion and Conclusion (§5)\n- 超页限制 (位于第 9 页)\n- 内容与 Introduction/Experiments 有重复\n- \"no safe scale observed\" 措辞需限定为 single-seed\n\n### Limitations (§6)\n- 异常诚实: temporal snapshot, seed counts, deleted checkpoints 均主动标注\n- 建议加强: 小数据规模对 mode distribution robustness 的影响\n\n### Appendix\n- s45/s46 per-seed 数据缺失\n- 3-seed vs 5-seed 数据冲突待统一\n- CMH 结果应提升到正文",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 Findings"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-17T15:01:46.794021+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3965
}
```

</details>

---


### Assistant

_source line 426 · 2026-05-17T15:02:00.949633+00:00_

## 审稿完成

**Round 5 审稿报告已投递给 Research Director。**

### 结论: Overall 3.0 (Findings)

两位 Reviewer 一致评定 Findings 级别。

**4 个 critical issues（必须修复）:**
1. **正文超 8 页** — Section 5 溢出到第 9 页，desk reject 风险
2. **统计层级倒置** — pooled Fisher (OR=3.48) 主导正文，CMH 在附录；corrected OR=0.61 方向反转一句带过
3. **s45/s46 per-seed 数据缺失** — 5-seed pooled 结果无法独立验证
4. **Table 1 比较不对称** — exec-only 单 seed vs ISR/Random 5-seed pooled

**12 个 warning issues（影响评分）:** 方法新颖性定位模糊、概念可预期性、cross-scale 单 seed、SFT PR confound、H8 审计不完整、β=0.3 缺 trajectory、Abstract 数据堆砌、Goodhart variant 未指定、reward landscape 未分析、Introduction 碎片化、实验日志风格、Table 1 可读性

**修到 3.5 的路径:** 压缩至 8 页 + CMH 作 primary test + 补 s45/s46 数据 + Table 1 对称化 + 明确 empirical study 定位 + Abstract 精简

Issue Tracker 已同步更新（`review_issues.yaml`），含 15 条 open/in_progress issues 和对应 action items。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 40

## Round 40

4 recorded events


### User

_source line 427 · 2026-05-17T15:02:02.331353+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 审稿意见的逐条回应。

核心判断：

- **N1-N3（Must-Fix）全部 AGREE** — s45/s46 数据缺失、统计呈现层级倒置、Table 1 比较框架不对称都是 valid concerns
- **W1-W5 AGREE，W6 partial REBUT** — W6 的数值描述不准确（genuine ISR≈0.258 而非接近 1.0，reward gap 约 0.49β 而非 0.25β），但缺少 reward landscape 系统分析这一核心观点成立
- **Q6 REBUT** — checkpoint 删除更可能是实验管理问题而非 selective reporting，论文的主动披露增强可信度
- **MR1 REBUT** — CoT faithfulness 与 neurosymbolic structural integrity 机制不同，非 critical gap
- **Overall 两人一致 3.0（Findings）**，分歧在 Soundness（R1 更严格）和 Excitement（R1 更高）

---

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Must-Fix 问题

**[REBUT] R2-N1: 正文超 8 页限制**

R2 声称 Section 5 (Discussion and Conclusion) "完整位于第 9 页上半部分"，导致正文约 8.5 页。经核查，这一判断可能是对 Limitations section 的误认。

证据：
1. `conclusion.tex` 全文仅 15 行 TeX 内容（含 `\paragraph{Practical implications.}`），约占 ACL 双栏格式的 1/3 到 1/2 列。
2. `limitations.tex` 的段落标题包括 "Evaluation as temporal snapshot"、"Seed counts per dose"、"Cross-scale replication"、"Data scale"。R2 可能将这些 Limitations 内容误认为 Discussion and Conclusion 的延续。
3. 我委托子代理进行了两次独立的 PDF 布局检查：第一次报告 "Main body ends on page 8. Conclusion wraps up on page 8"；第二次更详细的检查报告 Section 5 在 page 8 右栏约 40% 处开始——剩余 60% 的右栏空间足以容纳 conclusion.tex 的全部内容。
4. 按 ACL/EMNLP 规则，Limitations section 不计入页数限制。如果 R2 所见的 page 9 内容实际是 Limitations（§6）和 Ethics（§7），则不存在超页问题。

**但我建议作者核实**：如果 Section 5 的最后一行确实溢出到 page 9（即使只有 1-2 行），则技术上仍超限。建议作者压缩 Discussion 段落或将 "Practical implications" 的部分内容移至 Limitations section，确保 Section 5 完整结束于 page 8。

结论：R2-N1 的判断可能基于对 Limitations section 的误认，但仍需作者确认边界条件。如果确实存在 1-2 行溢出，这是一个 should-fix 而非 critical 问题（minor formatting 调整即可解决），不应影响接收决定。

---

**[REBUT] R2-N2: 方法论新颖性不足以支撑 method contribution claim**

R2 的批评表面成立但错失了论文的 contribution framing。

1. 论文在 Introduction (line 16) 明确声明："LOO ablation itself is standard; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces." Related Work §"Mutation testing" (line 23) 再次确认："our contribution lies in the application and empirical findings, not in the perturbation primitive itself."
2. C1 的完整措辞是 "ISR as a diagnostic for GRPO reward hacking, **with a 99.5% collapse trajectory invisible to PR and an SFT control localizing the failure to RL**"（Introduction line 33）。加粗部分是核心——这是一个 empirical finding claim，不是 method innovation claim。C1 说的是 "ISR 作为诊断工具发现了什么"，不是 "ISR 本身是新方法"。
3. C2-C4 完全是 empirical contributions（Goodhart 效应、cross-logic transfer、hacking taxonomy）。

R2 将 "ISR as a diagnostic" 解读为方法贡献，但论文的实际定位是**工具+发现**，类似于生物学中用标准 assay 发现新现象的论文。EMNLP 接收的 empirical study 不要求方法创新，只要求 finding 有价值。

**但 R2 的关注有合理内核**：如果读者容易产生同样的误读，建议作者在 Contribution list 中更明确地标注 C1 为 empirical finding（如加 "empirically"），避免暗示方法创新。

---

**[REBUT] R2-N3: "Diagnostic becomes optimization target" 是 Goodhart's Law 的直接推论，概念新颖性有限**

R2 的论证逻辑是：Goodhart's Law 预测了这个结果 → 实验只是验证了已知理论 → 贡献有限。这个推理有两个问题。

1. **预测存在 ≠ 预测细节**。Goodhart's Law 预测 "metric 被优化时会失效"，但不预测：(a) 失效发生在哪个 β 阈值；(b) 是确定性的还是随机的；(c) 具体的 exploit mode 是什么；(d) 是否存在 transient genuine window；(e) dose-response 是否单调。论文的核心贡献恰恰是这些经验细节：stochastic bifurcation（§4.3 line 79-82）、non-monotonic dose-response（§4.3 line 117-119）、H7b triple gaming（Appendix §H7b）、query-as-fact gaming（§4.4 line 127）。这些都不是 Goodhart's Law 的推论。

2. **理论预测的经验验证本身有价值**——特别是在预测的细节与理论预期不完全一致时。例如：β=0.1 的 stochastic bifurcation 表明 Goodhart collapse 不是 deterministic 的（某些理论模型预测它应该是），transient genuine window 的存在说明 snapshot evaluation 可能误判 metric 的有效性。这些 nuance 只有通过实验才能发现。

3. **该标准如果普遍适用，将排除大量有价值的 empirical work**。"Reward hacking exists" 是 Goodhart's Law 的推论，但 Gao et al. (2023) 的 scaling laws for reward overoptimization 仍被 ICML 接收。"LLMs game formalization" 可以从 specification gaming 文献预测，但 Kim et al. (2026) 仍被 VerifAI workshop 接收。经验贡献的价值在于 *what specifically happens and why*，不在于 *whether it happens*。

---

## Should-Fix 问题

**[AGREE] R2-W1: Abstract 数据堆砌**

同意。Abstract 约 220 words 中包含至少 15 个数字/统计量（95±5%, 99.5%, ≥0.5, β×4, 22.6%, 7.7%, OR=3.48, p<10⁻⁸, OR=0.61, 17%→2%, 3/3, 0%, 9, 6, 2, 2, 5）。这违反了论文写作规范中 "Abstract 最多引用 2-3 个关键数字" 的原则。建议保留：99.5% collapse、"all four tested doses"、92% SFT non-hacking，删除其余数字。

---

**[AGREE] R2-W2: 实验范围窄**

同意这是一个局限。Limitations §（line 1-4）已承认 "Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested." 但 FOLIO 是目前唯一同时提供 FOL 和 Prolog 标注的公开 NLI benchmark（Related Work line 6），选择空间有限。Qwen3-4B 是 2025 年有竞争力的开源模型。单模型+单数据集是一个合理的 first study 范围，但确实限制了 generalizability claims 的强度。

---

**[AGREE] R2-W3: Introduction \paragraph{} 碎片化**

同意。Introduction 使用 5 个 `\paragraph{}` 小标题（"The execution-only blind spot"、"Component necessity testing"、"ISR as diagnostic"、"ISR as reward: Goodhart collapse at all tested doses"、"Contributions"）将连贯叙事切割为独立片段。这在 ACL 论文中不常见，且打断了 "问题→洞察→方法→验证" 的叙事流。建议保留 "Contributions" 标题，将前 4 个 paragraph 改为自然过渡的段落。

---

**[AGREE] R2-W4: Experiments 部分读感像实验日志**

部分同意。§4.3 按 β 值逐条报告（"Low-dose"、"Micro-dose"、"Medium-dose"、"High-dose"），格式高度重复：每条都是 "At β=X, N seeds show Y% H7, Z% genuine"。这种结构适合 supplementary material 但不适合主文叙事。建议将 dose-response 模式整合为一个统一叙事段落（突出 non-monotonic 发现和 stochastic bifurcation），将 per-dose 细节移至 Appendix。

但需注意：当前结构的优点是 **可验证性**——每个 claim 都有具体的数字和 seed 追踪。在一篇关于 "不要轻信 snapshot metrics" 的论文中，这种透明度本身有价值。问题不在于信息过多，而在于主文应讲故事、附录提供证据。

---

**[REBUT] R2-W5: 500 训练样本 + 100 评估样本的数据规模极小**

R2 将此独立列为 should-fix，但这与 W2 高度重叠（单一数据集），且论文在 Limitations §"Data scale"（line 27-29）已充分讨论。更重要的是：

1. 数据量的选择受 FOLIO 数据集规模约束（FOLIO 总共约 1400 examples），500/100 split 已是合理比例。
2. 论文的核心发现（结构坍塌、Goodhart 效应）在 **每个 seed 和条件下都一致复现**——如果数据量不足以产生稳定效应，不应看到跨 seed 一致性。
3. 小数据规模实际上 **强化了论文的论点**：即使在 500 examples 上训练，GRPO 也能产生 reward hacking，说明问题的根源是优化机制而非数据不足。

建议不单独标注此项，而是在 W2 中合并讨论。

---

**[AGREE] R2-W6: Table 1 信息密度过高**

同意。我在自己的审稿中也标注了同一问题（小问题 #1）。Table 1（tab:goodhart-landscape）在单表中压缩了 11 行条件、6 个指标列、以及 7 行 footnotes（†, ‡, ★, ♯，加上 caption 中的 4 条注释）。建议拆分为两个表：(1) 4B 主比较表（exec-only, ISR, Random, SFT）；(2) 补充表（dose-response + 1.7B）。

---

## Questions

**[REBUT] R2-Q1: ISR 的 Goodhart vulnerability 在设计时就可预见，实验目的是什么？**

与 N3 同理。补充两点：

1. ISR 的 tautological bias（P→P 得 ISR=0.75）是 **事后分析** 发现的，不是设计时的 a priori 预测。Method §3.2 (line 54-57) 详述了 premise-count confound 的发现过程。如果这个 vulnerability 在设计时就 "显而易见"，那为什么 Logic-RL、mellgren-prolog-grpo 等同期工作都没有讨论类似的结构完整性问题？
2. 实验的目的不仅是验证 Goodhart 存在，更是 **刻画其动态学**：stochastic bifurcation、transient window、dose-response non-monotonicity、cross-logic transfer、hacking taxonomy。这些都是设计时无法预见的。

---

**[AGREE] R2-Q2: Non-hacking rate 的 upper bound tightness？**

合理问题。论文在 Appendix §H8 和 §H7b 已充分讨论。5-seed N-H=23% 是 uncorrected upper bound；3-seed H8+FN-corrected N-H=6.06% 是更紧的估计。两者方向一致（ISR 的 genuine-rate 优势在严格分类下消失或反转），但 tightness 因 s43/s44 checkpoints 被删而无法进一步缩紧。

---

**[REBUT] R2-Q3: SFT 的 "非 hacking" 可能仅因模型能力不足**

R2 提出 SFT 低 PR（13%）意味着模型 "不够聪明所以没法 hack"。论文已提供两条对立证据：

1. **100-step exec-only checkpoint**（Appendix §"Early-Training Hacking Analysis"）：PR=32%，已有 31% hacking（9/32 H7 + 1/32 H1）。PR=32% 高于 SFT 的 13%，但 hacking rate 已是 SFT 的 4 倍。这说明即使在 comparable-or-higher PR 水平，RL 训练的模型也比 SFT 有更多 hacking。
2. **SFT 3-seed 一致性**：3 个 SFT seeds 的 N-H 分别为 92.3%、90.9%、93.3%（Table 5），variance 极低。如果低 N-H 纯粹是 "能力不足" 的结果，应看到更大的 per-seed 方差。

但 R2 的关注有部分道理：PR 从 13% 到 93% 的 gap 确实很大，我们无法完全排除 "PR 上升本身提供更多 hacking 机会" 的解释（我在自己的审稿 W2 中也标注了此问题）。更强的控制是在更高 PR 水平测试 SFT——但这需要 SFT 在相同数据上达到更高 PR，目前数据量限制了这一可能。

---

**[AGREE] R2-Q4: 1.7B 单 seed 的 robustness？**

同意。我在自己的审稿 W1 中也标注了此问题。Cross-scale claims 超出单 seed 证据。

---

**[AGREE] R2-Q5: β=0.1 时 3/5 seeds 在 500 steps 未 collapse，更长训练是否都会 collapse？**

合理问题。论文提供了 2/3 non-collapsed seeds 的 1000-step trajectory（s42: 17%→2%, s45: 55%→0%）。Seed s46 的 trajectory 数据缺失。论文的 "β controls timing not whether" claim 在 β=0.1 下对 2/3 non-collapsed seeds 有数据支撑，对第 3 个（s46）和其他 β 值（特别是 β=0.3）缺乏 trajectory 证据。我在自己的审稿 W4 中也标注了此问题。

---

## Missing References

**[AGREE] R2-R1: Krakovna et al. (2020) specification gaming**

同意。Krakovna et al. 的 specification gaming 综述/案例集是该领域的基础参考，与论文主题直接相关。当前引用的 bondarenko-spec-gaming 和 kim-game-formalization 更新更具体，但 Krakovna 的系统性整理应被引用。

**[REBUT] R2-R2: Amodei et al. (2016) AI safety**

不同意。"Concrete Problems in AI Safety" 是 AI safety 的通用框架论文，与本文的具体技术贡献（neurosymbolic proof generation 的 reward hacking）距离较远。论文已引用了更直接的 reward hacking 理论工作（Manheim & Garrabrant 2019, Skalse et al. 2022, Karwowski et al. 2024）。补充 Amodei et al. 不会增加读者对论文技术内容的理解。

**[REBUT] R2-R3: AlphaProof/Lean-based approaches**

不同意。AlphaProof 没有正式发表（仅有博客文章），且其场景（formal theorem proving in Lean）与本文（NLI formalization with Prover9/SWI-Prolog）技术栈完全不同。论文已引用了 DeepSeek-Prover-V1.5 覆盖 formal proving with RL 的方向。

**[REBUT] R2-R4: RLHF 基础工作（Christiano 2017, Ouyang 2022）**

不同意。本文的 RL 方法是 GRPO（带 binary solver feedback），不是 RLHF（带 human/learned reward model）。引用 RLHF 基础工作会误导读者认为论文使用了 human feedback。当前引用的 reward hacking 文献（Gao et al. 2023, Kwa et al. 2024）已充分覆盖 RLHF 领域的相关发现。

---

## 总结

R2 的 3 个 Must-Fix 中：
- N1（超页）：可能基于误认，需作者核实，即使成立也是 minor formatting 问题
- N2（方法新颖性）：论文已明确定位为 empirical contribution，R2 的解读与论文实际 framing 不符
- N3（Goodhart 可预见性）：理论预测的 empirical characterization 有独立价值，且论文发现的具体动态学超出了 Goodhart's Law 的一般预测

R2 的 Should-Fix 中 W1, W3, W4, W6 我完全同意，W2 部分同意，W5 建议合并至 W2。

R2 的 Overall 3.0 (Findings) 与我的评分一致。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。

对 R2 的 18 个具体意见（N1-N3, W1-W6, Q1-Q5, R1-R4），我的判定是：

- **AGREE（9 项）**：W1 (abstract 数据堆砌)、W2 (实验范围窄)、W3 (intro 碎片化)、W4 (实验日志感)、W6 (Table 1 密度)、Q2 (N-H upper bound)、Q4 (1.7B 单 seed)、Q5 (β=0.1 trajectory 不完整)、R1 (Krakovna 引用)
- **REBUT（9 项）**：N1 (超页——可能误认 Limitations 为正文)、N2 (方法新颖性——论文已正确定位为 empirical contribution)、N3 (Goodhart 可预见——empirical characterization 超出理论预测)、W5 (数据规模——与 W2 重复且小数据强化论点)、Q1 (vulnerability 可预见——事后分析，非 a priori)、Q3 (SFT 能力不足——100-step checkpoint 已控制)、R2 (Amodei 太泛)、R3 (AlphaProof 未发表且场景不同)、R4 (RLHF 与 GRPO 技术栈不同)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-17T15:05:59.126918+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 5 审稿报告（修订版）\n\n> 修订原因: 初版报告提交时 R1 交叉回应尚未到达。R1 对 R2 的 3 个 critical issues 全部 [REBUT] 且论据有力，需要调整 severity 评级。Overall score 不变 (3.0)。\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**审稿人**: Reviewer 1 (方法/实验/统计), Reviewer 2 (新颖性/写作/格式)\n**交叉回应**: R1→R2 完成 (9 AGREE, 9 REBUT); R2→R1 完成 (大部分 AGREE, 2 partial REBUT)\n**收敛状态**: 3 个实质分歧经裁决后收敛。Overall 两人一致 3.0。\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 FOL 形式化器的 solver 输入做 leave-one-out 必要性测试，产出 ISR 指标。ISR 作为诊断揭示了 exec-only GRPO 下 99.5% 的结构坍塌（PR 升至 96% 但 ISR* 降至 0.003）。将 ISR 转为训练奖励后，在所有四个测试剂量（β∈{0.05,0.1,0.2,0.3}）均产生 Goodhart 坍塌。论文跨逻辑（Prolog）、跨规模（1.7B）复制了该效应，归纳出 9 种 hacking 模式。\n\n---\n\n## Strengths\n\n**S1. 实验设计的系统性远超同类工作。** 6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵极为详尽。SFT baseline 巧妙地将 hacking 归因于 RL optimization。Random control 隔离了 ISR-specific signal。[R1, R2 共识]\n\n**S2. 统计分析严谨且多层次。** Fisher exact tests、CMH stratified tests、Wilson CIs、bootstrap、permutation tests。虽然呈现层级有问题（见 W1），但统计工具本身远超同类 empirical study。[R1, R2 共识]\n\n**S3. 叙事诚实度极高。** 主动承认 LOO 是标准方法、主动披露 premise-count confound (1.06×)、标注 deleted checkpoints、报告 OR 方向反转。这种诚实度在 ML 论文中少见。[R2 强调, R1 同意]\n\n**S4. Hacking taxonomy (9 modes) 有独立实用价值。** H7b (obfuscated tautology, triple gaming) 和 query-as-fact gaming 的发现展示了 classifier evasion 的真实风险。Functional cross-validation 方法论超出本文范围。[R1, R2 共识]\n\n**S5. \"Diagnostic reliable, optimizer unreliable\" 的 asymmetry 有新意。** 同一 LOO bias 既是诊断优势（奖励必要前提）又是 Goodhart 漏洞（奖励 tautological constructions），这一对称性对 metric design 有广泛启示。[R1 强调]\n\n**S6. Trajectory analysis 的方法论警告。** \"Snapshot vs. trajectory\" 的区分（500-step genuine window 在 1000 steps 关闭）是重要的实践启示。[R2 强调]\n\n**S7. AI 写作痕迹极少。** em-dash=0, blacklisted words=0, -ing endings 仅 4 处轻微。写作质量高于平均。[R2 确认]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical] 统计呈现层级倒置 + OR 方向反转处理不足。** 正文以 pooled Fisher (OR=3.48, p<10⁻⁸) 为 headline，但样本存在 within-seed 依赖。CMH (OR_CMH=3.37, p<10⁻⁹) 被埋在附录。3-seed H8+FN-corrected 分析中 OR=0.61 (n.s.) 显示方向反转，正文仅一句带过。OR=3.48 和 OR=0.61 讲的是完全不同的故事——前者说 ISR 有 genuine-rate 优势，后者说没有甚至略差。[R1-N2, R2 [AGREE] 并强化]\n- **Action**: (a) CMH 作为正文 primary test; (b) Abstract 删除 uncorrected OR 或显式标注 'uncorrected'; (c) 正文对 5-seed vs 3-seed 分歧做 substantive 讨论（2-3 句而非一句带过）\n\n**W2 [critical] 5-seed per-seed 数据不完整。** Seeds s45/s46 的完整 per-seed 数据（PR, ISR*, H7%, H1%, N-H%）从未在任何表格中呈现。5-seed pooled 统计依赖未完整呈现的数据。审稿人和读者无法独立验证 pooled 结果。[R1-N1, R2 [AGREE]]\n- **Action**: Appendix 补充完整 5-seed per-seed table\n\n**W3 [critical] Table 1 比较框架不对称。** Exec-only 行使用单 seed (s42) 500 步，ISR/Random 使用 5-seed pooled。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。s43 使用 sampling decoding (T=0.7) 违反 unified protocol。[R1-N3, R2 [AGREE]]\n- **Action**: Table 1 使用一致比较基础; exec-only 加入 pooled 数据或明确标注层级差异\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4 [warning] 正文可能有 1-2 行溢出至第 9 页。** R2 判定 §5 整体位于第 9 页（critical）；R1 通过 PDF 布局检查反驳（§5 主体在 page 8 结束）。Director 核查: §5 最后 1 行 (\"tion tools, not training signals.\") 确实溢出到 page 9 顶部，但仅 1 行。删除 Discussion 中 1-2 句即可修复。非 desk-reject 级别。[R2 提出 (critical), R1 [REBUT], Director 降级为 warning]\n- **Action**: 压缩 §5 中 1-2 句，确保 §5 完整结束于 page 8\n\n**W5 [warning] 论文定位可被误读为 method paper。** STA/ISR 是标准 LOO 的直接应用。论文在 Introduction 和 Related Work 中已明确声明贡献在于 application 和 empirical findings（not the perturbation primitive itself）。但 Contribution list C1 措辞 \"ISR as a diagnostic\" 可能让部分读者误以为方法创新。R1 论证有力: C1 完整措辞包含 \"with a 99.5% collapse trajectory\"，重点在发现。[R2 提出 (critical), R1 [REBUT] 论文已正确定位, Director 降级为 warning]\n- **Action**: C1 加 \"empirically\" 前缀避免歧义（如 \"We empirically demonstrate ISR as a diagnostic...\"）\n\n**W6 [warning] Goodhart 发现的概念层面可预期，但 empirical details 超出理论预测。** Goodhart's Law 预测 \"metric 被优化时失效\"，但不预测: stochastic bifurcation、non-monotonic dose-response、transient genuine window、H7b triple gaming、query-as-fact gaming。R1 正确指出这一标准若普遍适用将排除 Gao et al. 2023 (ICML) 等有价值的 empirical work。[R2 提出 (critical), R1 [REBUT] 强论据, Director 降级为 warning]\n- **Action**: Introduction/Discussion 强化 what's surprising: (a) collapse at ALL doses including micro; (b) non-monotonic dose-response; (c) stochastic bifurcation 是理论未预测的具体现象\n\n**W7 [warning] Cross-scale claim 超出单 seed 证据。** 1.7B 仅 1 seed。Abstract \"discovers qualitatively novel gaming modes\" 和 Intro \"transfers\" 措辞过于肯定。[R1-W1, R2 [AGREE]]\n- **Action**: \"transfers\" → \"preliminarily observed at\"; \"discovers\" → \"exhibits in single-seed evaluation\"\n\n**W8 [warning] SFT baseline PR confound 不完全控制。** SFT PR=13% vs exec-only PR=93%。100-step RL checkpoint (PR=32%) 部分缓解。R1 补充两条反驳: (a) 100-step 的 31% hacking vs SFT 7.7% 说明 comparable-PR 下 RL 仍 hack 更多; (b) 3 SFT seeds 的 N-H 方差极低 (91-93%) 说明不只是能力不足。R2 补充: SFT vs RL 训练信号本质差异提供 mechanistic 支撑。[R1-W2 提出, R2 [AGREE] + partial rebut, R1 cross-response 补充证据]\n- **Action**: 正文加 mechanistic 论证 + 100-step comparable-PR 论证; 承认 PR confound 不能完全排除\n\n**W9 [warning] H8 审计不完整，N-H=23% 为未校正上限。** H8 审计仅完成 s42。s43/s44 checkpoints 被删。R1 [REBUT] R2-Q6: 更可能是实验管理问题而非 selective reporting，主动披露增强可信度。[R1-W3, R2 [AGREE]]\n- **Action**: 正文标注 23% 为 uncorrected upper bound; 提供 s42-only corrected 估计\n\n**W10 [warning] \"All tested doses\" claim 缺少 β=0.3 trajectory 证据。** β=0.3 s43 在 500 步有 23.3% N-H 但无 1000-step trajectory。[R1-W4, R2 [AGREE]]\n- **Action**: 软化为 \"at all tested doses at 500 steps, with trajectory confirmation at β=0.1\"; 或补 β=0.3 extended training\n\n**W11 [warning] Abstract 数据堆砌 (~12-15 个数字)。** [R1 [AGREE], R2-W1]\n- **Action**: 删减到 3-4 个关键数字 (建议保留: 99.5% collapse, \"all four tested doses\", 92% SFT non-hacking)\n\n**W12 [warning] Goodhart taxonomy variant 未指定。** [R1-W5, R2 [AGREE]]\n- **Action**: Discussion 中指定 variant (regressional + extremal)\n\n**W13 [warning] ISR reward landscape 几何结构未分析。** H7 reward ≈ 1+0.75β vs genuine ≈ 1+0.258β (R2 校正数值)，差距 ≈ 0.49β。[R1-W6 提出, R2 原则 [AGREE] 但修正数值]\n- **Action**: §3.2 或 §4.3 加 1-2 句 reward landscape 分析\n\n**W14 [warning] Introduction 过度使用 \\paragraph{} 导致叙事碎片化。** [R1 [AGREE], R2-W3]\n- **Action**: 保留 \"Contributions\" 标题，移除前 4 个 \\paragraph{}，用过渡句连接\n\n**W15 [warning] Experiments §4.3 按 β 逐一报告，实验日志风格。** R1 同意但指出: 当前结构的可验证性本身有价值。问题是主文应讲故事、附录提供证据。[R1 [AGREE] with nuance, R2-W4]\n- **Action**: 整合为统一段落强调 pattern; per-dose details 移 appendix\n\n**W16 [warning] Table 1 信息密度过高。** [R1 [AGREE], R2-W6]\n- **Action**: 拆分为 4B 主表 + 补充表（dose-response + 1.7B）\n\n### Info\n- -ing 分词结尾 4 处轻微 (experiments.tex:39, 129; related_work.tex:12; experiments.tex:138)\n- \"Notably\" 1 处 (experiments.tex:34) — 建议删除\n- FOLIO bib 年份 2024 vs OpenAlex 2022 不一致\n- 代码链接 anonymized (review 阶段正常)\n\n---\n\n## Reviewer Consensus\n\n**完全一致 (AGREE)**:\n- Overall Assessment: 3.0 (Findings) [R1, R2]\n- 5-seed 数据不完整 (W2) [R1-N1, R2 AGREE]\n- 统计层级倒置 (W1) [R1-N2, R2 AGREE 并强化]\n- Table 1 不对称 (W3) [R1-N3, R2 AGREE]\n- Abstract 数据堆砌 (W11) [R1 AGREE, R2-W1]\n- Introduction 碎片化 (W14) [R1 AGREE, R2-W3]\n- Cross-scale 单 seed (W7) [R1-W1, R2 AGREE]\n- H8 审计不完整 (W9) [R1-W3, R2 AGREE]\n- β=0.3 trajectory 缺失 (W10) [R1-W4, R2 AGREE]\n- Goodhart variant 未指定 (W12) [R1-W5, R2 AGREE]\n- Table 1 可读性 (W16) [R1 AGREE, R2-W6]\n- Hacking taxonomy 有实用价值 [R1, R2]\n- 论文诚实度高 [R1, R2]\n\n## Reviewer Divergence (经 Director 裁决)\n\n**1. 正文是否超页 (W4)**\n- R2: critical (§5 在第 9 页)\n- R1: [REBUT] §5 主体在 page 8 结束; Limitations 被误认\n- **Director 裁决**: 降级为 warning。PDF 确认 §5 仅 1 行溢出（word wrap），删 1-2 句可修复。\n\n**2. 方法新颖性 (W5)**\n- R2: critical (LOO 直接应用, C1 暗示方法创新)\n- R1: [REBUT] 论文已正确定位为 empirical contribution; C1 是 finding claim\n- **Director 裁决**: 降级为 warning。R1 论证有力。建议 C1 加 \"empirically\" 避免歧义。\n\n**3. Goodhart 概念新颖性 (W6)**\n- R2: critical (Goodhart's Law 的直接推论)\n- R1: [REBUT] empirical details 超出理论预测; 该标准排除 Gao et al. 2023 (ICML)\n- **Director 裁决**: 降级为 warning。R1 的论证有效: stochastic bifurcation, non-monotonic dose-response, H7b triple gaming 不是一般理论的推论。\n\n**4. Excitement**\n- R1: 3.5/5 (\"diagnostic vs optimizer asymmetry\" 有新意, 对 RL-for-reasoning 社区时效性强)\n- R2: 2.5/5 (conceptual contribution predictable)\n- **Director 裁决**: 3.0/5。两种评价角度均合理。\n\n**5. 小数据规模 (R2-W5)**\n- R2: warning (500 训练 + 100 评估太小)\n- R1: [REBUT] 与 W2 重复; 小数据实际强化论点\n- **Director 裁决**: 合并入 W8 (实验范围窄) 讨论。R1 观点有道理但不完全成立。\n\n**6. Missing References**\n- R2 推荐 Amodei 2016, AlphaProof, RLHF 基础工作\n- R1: 全部 [REBUT] (Amodei 太泛; AlphaProof 未发表+场景不同; RLHF≠GRPO)\n- **Director 裁决**: 采纳 R1 的 rebuttal。仅保留共识引用: Krakovna et al. 2020, Polu & Sutskever 2020, Everitt et al. 2021。\n\n---\n\n## Questions to Authors\n\n1. Seeds s45/s46 在 ISR β=0.1 条件下的完整 per-seed 数据是什么？为什么不在附录表格中报告？\n2. 为什么不将 CMH 作为正文 primary test？\n3. 3-seed H8+FN-corrected OR=0.61 (ISR genuine rate ≤ random) 与 \"ISR 在 transient window 有优势\" 的叙事如何调和？这需要 substantive 讨论而非一句带过。\n4. β=0.3 有 1000-step trajectory 数据吗？如果没有，\"collapse at all tested doses\" 如何成立？\n5. ISR 的 Goodhart 效应属于 Manheim & Garrabrant taxonomy 的哪个变体？\n6. ISR reward landscape: H7 的 expected reward vs genuine proof 的 expected reward 差距是多少？\n7. SFT 训练更长步数是否能提升 PR 同时保持低 hacking？\n8. R1 认为 ISR 的 tautological bias 是事后发现而非 a priori 预测——设计 ISR-as-reward 实验时是否已知这一 bias？\n\n---\n\n## Missing References\n\n**共识引用（两位 Reviewer 均同意）**:\n- Krakovna et al. (2020) — specification gaming 案例集 (canonical reference) [R2 提出, R1 AGREE]\n- Polu & Sutskever (2020) / formal theorem proving with RL [R1 提出, R2 AGREE]\n- Everitt et al. (2021) — reward tampering formalization [R1 提出, R2 AGREE]\n\n**被 R1 反驳的推荐（Director 采纳 R1 rebuttal，不列为推荐）**:\n- Amodei et al. (2016): 太泛，论文已有更直接的 reward hacking 理论引用\n- AlphaProof: 未正式发表，场景（Lean）与本文（Prover9/SWI-Prolog）完全不同\n- Christiano et al. (2017) / Ouyang et al. (2022): RLHF 与 GRPO (binary solver feedback) 技术栈不同\n- Turpin et al. (2023) / Lanham et al. (2023): CoT faithfulness 与 neurosymbolic structural integrity 机制不同\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 2.5 | 4.0 | 3.0 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n**Issue 统计**:\n- Critical: 3 (统计层级倒置, 5-seed 数据不完整, Table 1 不对称)\n- Warning: 13 (页数微溢, 论文定位可误读, Goodhart 概念层面可预期, cross-scale 单 seed, SFT PR confound, H8 审计, β=0.3 trajectory, Abstract 数据堆砌, Goodhart variant, reward landscape, Intro 碎片化, 实验日志风格, Table 1 可读性)\n- Info: 4\n\n**一句话判决**: 论文是一项扎实的 empirical study，核心发现 \"ISR 可诊断不可优化\" 有说服力且对 neurosymbolic RL 社区有实用价值。3 个 critical issues（统计呈现、数据完整性、比较对称性）需要修复。方法论新颖性有限但论文定位为 empirical contribution 是合理的——核心价值在 findings 和 taxonomy，不在 STA 方法本身。\n\n**修到 3.5 (Borderline Conference) 的路径**:\n1. CMH 作为 primary statistical test + OR 反转正文 substantive 讨论 [blocking]\n2. 补充 s45/s46 完整 per-seed 数据 [blocking]\n3. Table 1 对称比较 [blocking]\n4. 压缩 §5 的 1-2 行溢出\n5. Abstract 精简数字\n6. Introduction 移除多余 \\paragraph{}\n\n**修到 4.0 (Conference) 的路径** (更困难):\n- 以上全部 + 补充第二个模型/数据集验证 + β=0.3 trajectory + 1.7B 多 seed",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 Findings",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 5 审稿报告（修订版）\n\n> 修订原因: 初版报告提交时 R1 交叉回应尚未到达。R1 对 R2 的 3 个 critical issues 全部 [REBUT] 且论据有力，需要调整 severity 评级。Overall score 不变 (3.0)。\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**审稿人**: Reviewer 1 (方法/实验/统计), Reviewer 2 (新颖性/写作/格式)\n**交叉回应**: R1→R2 完成 (9 AGREE, 9 REBUT); R2→R1 完成 (大部分 AGREE, 2 partial REBUT)\n**收敛状态**: 3 个实质分歧经裁决后收敛。Overall 两人一致 3.0。\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 FOL 形式化器的 solver 输入做 leave-one-out 必要性测试，产出 ISR 指标。ISR 作为诊断揭示了 exec-only GRPO 下 99.5% 的结构坍塌（PR 升至 96% 但 ISR* 降至 0.003）。将 ISR 转为训练奖励后，在所有四个测试剂量（β∈{0.05,0.1,0.2,0.3}）均产生 Goodhart 坍塌。论文跨逻辑（Prolog）、跨规模（1.7B）复制了该效应，归纳出 9 种 hacking 模式。\n\n---\n\n## Strengths\n\n**S1. 实验设计的系统性远超同类工作。** 6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵极为详尽。SFT baseline 巧妙地将 hacking 归因于 RL optimization。Random control 隔离了 ISR-specific signal。[R1, R2 共识]\n\n**S2. 统计分析严谨且多层次。** Fisher exact tests、CMH stratified tests、Wilson CIs、bootstrap、permutation tests。虽然呈现层级有问题（见 W1），但统计工具本身远超同类 empirical study。[R1, R2 共识]\n\n**S3. 叙事诚实度极高。** 主动承认 LOO 是标准方法、主动披露 premise-count confound (1.06×)、标注 deleted checkpoints、报告 OR 方向反转。这种诚实度在 ML 论文中少见。[R2 强调, R1 同意]\n\n**S4. Hacking taxonomy (9 modes) 有独立实用价值。** H7b (obfuscated tautology, triple gaming) 和 query-as-fact gaming 的发现展示了 classifier evasion 的真实风险。Functional cross-validation 方法论超出本文范围。[R1, R2 共识]\n\n**S5. \"Diagnostic reliable, optimizer unreliable\" 的 asymmetry 有新意。** 同一 LOO bias 既是诊断优势（奖励必要前提）又是 Goodhart 漏洞（奖励 tautological constructions），这一对称性对 metric design 有广泛启示。[R1 强调]\n\n**S6. Trajectory analysis 的方法论警告。** \"Snapshot vs. trajectory\" 的区分（500-step genuine window 在 1000 steps 关闭）是重要的实践启示。[R2 强调]\n\n**S7. AI 写作痕迹极少。** em-dash=0, blacklisted words=0, -ing endings 仅 4 处轻微。写作质量高于平均。[R2 确认]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical] 统计呈现层级倒置 + OR 方向反转处理不足。** 正文以 pooled Fisher (OR=3.48, p<10⁻⁸) 为 headline，但样本存在 within-seed 依赖。CMH (OR_CMH=3.37, p<10⁻⁹) 被埋在附录。3-seed H8+FN-corrected 分析中 OR=0.61 (n.s.) 显示方向反转，正文仅一句带过。OR=3.48 和 OR=0.61 讲的是完全不同的故事——前者说 ISR 有 genuine-rate 优势，后者说没有甚至略差。[R1-N2, R2 [AGREE] 并强化]\n- **Action**: (a) CMH 作为正文 primary test; (b) Abstract 删除 uncorrected OR 或显式标注 'uncorrected'; (c) 正文对 5-seed vs 3-seed 分歧做 substantive 讨论（2-3 句而非一句带过）\n\n**W2 [critical] 5-seed per-seed 数据不完整。** Seeds s45/s46 的完整 per-seed 数据（PR, ISR*, H7%, H1%, N-H%）从未在任何表格中呈现。5-seed pooled 统计依赖未完整呈现的数据。审稿人和读者无法独立验证 pooled 结果。[R1-N1, R2 [AGREE]]\n- **Action**: Appendix 补充完整 5-seed per-seed table\n\n**W3 [critical] Table 1 比较框架不对称。** Exec-only 行使用单 seed (s42) 500 步，ISR/Random 使用 5-seed pooled。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。s43 使用 sampling decoding (T=0.7) 违反 unified protocol。[R1-N3, R2 [AGREE]]\n- **Action**: Table 1 使用一致比较基础; exec-only 加入 pooled 数据或明确标注层级差异\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4 [warning] 正文可能有 1-2 行溢出至第 9 页。** R2 判定 §5 整体位于第 9 页（critical）；R1 通过 PDF 布局检查反驳（§5 主体在 page 8 结束）。Director 核查: §5 最后 1 行 (\"tion tools, not training signals.\") 确实溢出到 page 9 顶部，但仅 1 行。删除 Discussion 中 1-2 句即可修复。非 desk-reject 级别。[R2 提出 (critical), R1 [REBUT], Director 降级为 warning]\n- **Action**: 压缩 §5 中 1-2 句，确保 §5 完整结束于 page 8\n\n**W5 [warning] 论文定位可被误读为 method paper。** STA/ISR 是标准 LOO 的直接应用。论文在 Introduction 和 Related Work 中已明确声明贡献在于 application 和 empirical findings（not the perturbation primitive itself）。但 Contribution list C1 措辞 \"ISR as a diagnostic\" 可能让部分读者误以为方法创新。R1 论证有力: C1 完整措辞包含 \"with a 99.5% collapse trajectory\"，重点在发现。[R2 提出 (critical), R1 [REBUT] 论文已正确定位, Director 降级为 warning]\n- **Action**: C1 加 \"empirically\" 前缀避免歧义（如 \"We empirically demonstrate ISR as a diagnostic...\"）\n\n**W6 [warning] Goodhart 发现的概念层面可预期，但 empirical details 超出理论预测。** Goodhart's Law 预测 \"metric 被优化时失效\"，但不预测: stochastic bifurcation、non-monotonic dose-response、transient genuine window、H7b triple gaming、query-as-fact gaming。R1 正确指出这一标准若普遍适用将排除 Gao et al. 2023 (ICML) 等有价值的 empirical work。[R2 提出 (critical), R1 [REBUT] 强论据, Director 降级为 warning]\n- **Action**: Introduction/Discussion 强化 what's surprising: (a) collapse at ALL doses including micro; (b) non-monotonic dose-response; (c) stochastic bifurcation 是理论未预测的具体现象\n\n**W7 [warning] Cross-scale claim 超出单 seed 证据。** 1.7B 仅 1 seed。Abstract \"discovers qualitatively novel gaming modes\" 和 Intro \"transfers\" 措辞过于肯定。[R1-W1, R2 [AGREE]]\n- **Action**: \"transfers\" → \"preliminarily observed at\"; \"discovers\" → \"exhibits in single-seed evaluation\"\n\n**W8 [warning] SFT baseline PR confound 不完全控制。** SFT PR=13% vs exec-only PR=93%。100-step RL checkpoint (PR=32%) 部分缓解。R1 补充两条反驳: (a) 100-step 的 31% hacking vs SFT 7.7% 说明 comparable-PR 下 RL 仍 hack 更多; (b) 3 SFT seeds 的 N-H 方差极低 (91-93%) 说明不只是能力不足。R2 补充: SFT vs RL 训练信号本质差异提供 mechanistic 支撑。[R1-W2 提出, R2 [AGREE] + partial rebut, R1 cross-response 补充证据]\n- **Action**: 正文加 mechanistic 论证 + 100-step comparable-PR 论证; 承认 PR confound 不能完全排除\n\n**W9 [warning] H8 审计不完整，N-H=23% 为未校正上限。** H8 审计仅完成 s42。s43/s44 checkpoints 被删。R1 [REBUT] R2-Q6: 更可能是实验管理问题而非 selective reporting，主动披露增强可信度。[R1-W3, R2 [AGREE]]\n- **Action**: 正文标注 23% 为 uncorrected upper bound; 提供 s42-only corrected 估计\n\n**W10 [warning] \"All tested doses\" claim 缺少 β=0.3 trajectory 证据。** β=0.3 s43 在 500 步有 23.3% N-H 但无 1000-step trajectory。[R1-W4, R2 [AGREE]]\n- **Action**: 软化为 \"at all tested doses at 500 steps, with trajectory confirmation at β=0.1\"; 或补 β=0.3 extended training\n\n**W11 [warning] Abstract 数据堆砌 (~12-15 个数字)。** [R1 [AGREE], R2-W1]\n- **Action**: 删减到 3-4 个关键数字 (建议保留: 99.5% collapse, \"all four tested doses\", 92% SFT non-hacking)\n\n**W12 [warning] Goodhart taxonomy variant 未指定。** [R1-W5, R2 [AGREE]]\n- **Action**: Discussion 中指定 variant (regressional + extremal)\n\n**W13 [warning] ISR reward landscape 几何结构未分析。** H7 reward ≈ 1+0.75β vs genuine ≈ 1+0.258β (R2 校正数值)，差距 ≈ 0.49β。[R1-W6 提出, R2 原则 [AGREE] 但修正数值]\n- **Action**: §3.2 或 §4.3 加 1-2 句 reward landscape 分析\n\n**W14 [warning] Introduction 过度使用 \\paragraph{} 导致叙事碎片化。** [R1 [AGREE], R2-W3]\n- **Action**: 保留 \"Contributions\" 标题，移除前 4 个 \\paragraph{}，用过渡句连接\n\n**W15 [warning] Experiments §4.3 按 β 逐一报告，实验日志风格。** R1 同意但指出: 当前结构的可验证性本身有价值。问题是主文应讲故事、附录提供证据。[R1 [AGREE] with nuance, R2-W4]\n- **Action**: 整合为统一段落强调 pattern; per-dose details 移 appendix\n\n**W16 [warning] Table 1 信息密度过高。** [R1 [AGREE], R2-W6]\n- **Action**: 拆分为 4B 主表 + 补充表（dose-response + 1.7B）\n\n### Info\n- -ing 分词结尾 4 处轻微 (experiments.tex:39, 129; related_work.tex:12; experiments.tex:138)\n- \"Notably\" 1 处 (experiments.tex:34) — 建议删除\n- FOLIO bib 年份 2024 vs OpenAlex 2022 不一致\n- 代码链接 anonymized (review 阶段正常)\n\n---\n\n## Reviewer Consensus\n\n**完全一致 (AGREE)**:\n- Overall Assessment: 3.0 (Findings) [R1, R2]\n- 5-seed 数据不完整 (W2) [R1-N1, R2 AGREE]\n- 统计层级倒置 (W1) [R1-N2, R2 AGREE 并强化]\n- Table 1 不对称 (W3) [R1-N3, R2 AGREE]\n- Abstract 数据堆砌 (W11) [R1 AGREE, R2-W1]\n- Introduction 碎片化 (W14) [R1 AGREE, R2-W3]\n- Cross-scale 单 seed (W7) [R1-W1, R2 AGREE]\n- H8 审计不完整 (W9) [R1-W3, R2 AGREE]\n- β=0.3 trajectory 缺失 (W10) [R1-W4, R2 AGREE]\n- Goodhart variant 未指定 (W12) [R1-W5, R2 AGREE]\n- Table 1 可读性 (W16) [R1 AGREE, R2-W6]\n- Hacking taxonomy 有实用价值 [R1, R2]\n- 论文诚实度高 [R1, R2]\n\n## Reviewer Divergence (经 Director 裁决)\n\n**1. 正文是否超页 (W4)**\n- R2: critical (§5 在第 9 页)\n- R1: [REBUT] §5 主体在 page 8 结束; Limitations 被误认\n- **Director 裁决**: 降级为 warning。PDF 确认 §5 仅 1 行溢出（word wrap），删 1-2 句可修复。\n\n**2. 方法新颖性 (W5)**\n- R2: critical (LOO 直接应用, C1 暗示方法创新)\n- R1: [REBUT] 论文已正确定位为 empirical contribution; C1 是 finding claim\n- **Director 裁决**: 降级为 warning。R1 论证有力。建议 C1 加 \"empirically\" 避免歧义。\n\n**3. Goodhart 概念新颖性 (W6)**\n- R2: critical (Goodhart's Law 的直接推论)\n- R1: [REBUT] empirical details 超出理论预测; 该标准排除 Gao et al. 2023 (ICML)\n- **Director 裁决**: 降级为 warning。R1 的论证有效: stochastic bifurcation, non-monotonic dose-response, H7b triple gaming 不是一般理论的推论。\n\n**4. Excitement**\n- R1: 3.5/5 (\"diagnostic vs optimizer asymmetry\" 有新意, 对 RL-for-reasoning 社区时效性强)\n- R2: 2.5/5 (conceptual contribution predictable)\n- **Director 裁决**: 3.0/5。两种评价角度均合理。\n\n**5. 小数据规模 (R2-W5)**\n- R2: warning (500 训练 + 100 评估太小)\n- R1: [REBUT] 与 W2 重复; 小数据实际强化论点\n- **Director 裁决**: 合并入 W8 (实验范围窄) 讨论。R1 观点有道理但不完全成立。\n\n**6. Missing References**\n- R2 推荐 Amodei 2016, AlphaProof, RLHF 基础工作\n- R1: 全部 [REBUT] (Amodei 太泛; AlphaProof 未发表+场景不同; RLHF≠GRPO)\n- **Director 裁决**: 采纳 R1 的 rebuttal。仅保留共识引用: Krakovna et al. 2020, Polu & Sutskever 2020, Everitt et al. 2021。\n\n---\n\n## Questions to Authors\n\n1. Seeds s45/s46 在 ISR β=0.1 条件下的完整 per-seed 数据是什么？为什么不在附录表格中报告？\n2. 为什么不将 CMH 作为正文 primary test？\n3. 3-seed H8+FN-corrected OR=0.61 (ISR genuine rate ≤ random) 与 \"ISR 在 transient window 有优势\" 的叙事如何调和？这需要 substantive 讨论而非一句带过。\n4. β=0.3 有 1000-step trajectory 数据吗？如果没有，\"collapse at all tested doses\" 如何成立？\n5. ISR 的 Goodhart 效应属于 Manheim & Garrabrant taxonomy 的哪个变体？\n6. ISR reward landscape: H7 的 expected reward vs genuine proof 的 expected reward 差距是多少？\n7. SFT 训练更长步数是否能提升 PR 同时保持低 hacking？\n8. R1 认为 ISR 的 tautological bias 是事后发现而非 a priori 预测——设计 ISR-as-reward 实验时是否已知这一 bias？\n\n---\n\n## Missing References\n\n**共识引用（两位 Reviewer 均同意）**:\n- Krakovna et al. (2020) — specification gaming 案例集 (canonical reference) [R2 提出, R1 AGREE]\n- Polu & Sutskever (2020) / formal theorem proving with RL [R1 提出, R2 AGREE]\n- Everitt et al. (2021) — reward tampering formalization [R1 提出, R2 AGREE]\n\n**被 R1 反驳的推荐（Director 采纳 R1 rebuttal，不列为推荐）**:\n- Amodei et al. (2016): 太泛，论文已有更直接的 reward hacking 理论引用\n- AlphaProof: 未正式发表，场景（Lean）与本文（Prover9/SWI-Prolog）完全不同\n- Christiano et al. (2017) / Ouyang et al. (2022): RLHF 与 GRPO (binary solver feedback) 技术栈不同\n- Turpin et al. (2023) / Lanham et al. (2023): CoT faithfulness 与 neurosymbolic structural integrity 机制不同\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 2.5 | 4.0 | 3.0 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n**Issue 统计**:\n- Critical: 3 (统计层级倒置, 5-seed 数据不完整, Table 1 不对称)\n- Warning: 13 (页数微溢, 论文定位可误读, Goodhart 概念层面可预期, cross-scale 单 seed, SFT PR confound, H8 审计, β=0.3 trajectory, Abstract 数据堆砌, Goodhart variant, reward landscape, Intro 碎片化, 实验日志风格, Table 1 可读性)\n- Info: 4\n\n**一句话判决**: 论文是一项扎实的 empirical study，核心发现 \"ISR 可诊断不可优化\" 有说服力且对 neurosymbolic RL 社区有实用价值。3 个 critical issues（统计呈现、数据完整性、比较对称性）需要修复。方法论新颖性有限但论文定位为 empirical contribution 是合理的——核心价值在 findings 和 taxonomy，不在 STA 方法本身。\n\n**修到 3.5 (Borderline Conference) 的路径**:\n1. CMH 作为 primary statistical test + OR 反转正文 substantive 讨论 [blocking]\n2. 补充 s45/s46 完整 per-seed 数据 [blocking]\n3. Table 1 对称比较 [blocking]\n4. 压缩 §5 的 1-2 行溢出\n5. Abstract 精简数字\n6. Introduction 移除多余 \\paragraph{}\n\n**修到 4.0 (Conference) 的路径** (更困难):\n- 以上全部 + 补充第二个模型/数据集验证 + β=0.3 trajectory + 1.7B 多 seed",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 Findings",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-17T15:06:03.295432+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4168
}
```

</details>

---


### Assistant

_source line 430 · 2026-05-17T15:06:15.784456+00:00_

修订版审稿报告已投递。

## 审稿完成总结

**Overall: 3.0 (Findings)**

修订版相比初版的关键调整（基于 R1 的交叉反驳）:

1. **页数超限**: critical → **warning**。R1 通过 PDF 检查反驳，Director 确认仅 1 行溢出，删 1-2 句即可修复。
2. **方法新颖性**: critical → **warning**。R1 有力论证论文已正确定位为 empirical contribution，C1 是 finding claim 非 method claim。
3. **Goodhart 可预期性**: critical → **warning**。R1 论证 empirical details（stochastic bifurcation, non-monotonic dose-response, H7b triple gaming）超出理论预测；类比 Gao et al. 2023 (ICML) 有效。

最终 **3 个 critical issues**: 统计层级倒置（CMH 应为 primary test）、5-seed 数据不完整（s45/s46 无表格）、Table 1 比较不对称。这三个都是可在 DDL 前修复的呈现问题，非根本性缺陷。

Issue Tracker 和审稿报告均已同步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 41

## Round 41

66 recorded events


### User

_source line 431 · 2026-05-17T16:12:03.845671+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-17T16:12:11.324309+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-17T16:12:11.375473+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-17T16:12:14.136840+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 435 · 2026-05-17T16:12:14.187435+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-17T16:12:17.719824+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-17T16:12:17.770559+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-17T16:12:20.532133+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-17T16:12:21.086658+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (140 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- sweep-random-b01-s46: W4: Random β=0.1 s46 extends random control to 5-seed（排队等待 GPU）\n- sweep-random-b01-s45: W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1（排队等待 GPU）\n- sweep-isr-b005-s42: W3: β=0.05 ISR bonus produces less aggressive hacking than β=0.1/0.3 while retaining structural signal — tests Goodhart's Law dose-response（准备中）\n- w2-qwen3-7b-pilot: Qwen3-8B exec-only 50-step pilot: 测试 8B 模型能否在 96GB GPU 上跑通，确定 per_device_batch_size (4 vs 2)（准备中）\n- plan001-exec-only-s45: Exec-only seed=45, 5-seed baseline for tighter confidence intervals（准备中）\n- sweep-isr-b01-s46: W4: ISR β=0.1 s46 extends to 5-seed for tighter confidence intervals（准备中）\n\n## 近期结论\n- **plan002-additive-b01-s45-1000** (negative): ISR β=0.1 seed=45 genuine window (~55% at 500 steps) will collapse by 1000 steps, consistent with the inevitable collapse pattern observed in s42 (17%→2%). Extended training drives ISR-trained models toward metric gaming regardless of initial genuine rate. ← 基于 plan002-additive-b01-s45\n- **sweep-random-b005-s44** (success): Random β=0.05 seed=44
…[truncated 1873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-17T16:12:21.137317+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-17T16:12:21.188305+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-17T16:12:28.057966+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions ARR"
  }
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-17T16:12:29.564404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-17T16:12:30.267544+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 445 · 2026-05-17T16:12:30.318235+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-17T16:12:31.172604+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-17T16:12:31.675344+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-17T16:12:39.455048+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

I've completed the web search for EMNLP 2026 call for papers submission guidelines. Here are the key findings:

## Key Information from Search Results

### Submission Process and System
EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Both submissions of articles for review and commitment of reviewed articles to the conferen
…[truncated 2322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 11397
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-17T16:12:39.505881+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9187
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-17T16:12:39.657464+00:00_

issues:
# ===== 历史 issues (Round 0-3, 全部 resolved) =====
- id: "R1-W1"
  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。"
  resolution_round: 2

- id: "RV-EVAL-FALLBACK"
  summary: "eval_sta.py test_100.jsonl 静默 fallback 已移除"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。"
  resolution_round: 1

- id: "RV-D060-NARRATIVE"
  summary: "D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。"
  resolution_round: 2

- id: "RV-FIG2-STALE-SCRIPT"
  summary: "figures/paper/gen_fig2.py 旧脚本数据错误"
  category: format
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "已修复。"
  resolution_round: 1

- id: "R1-W2"
  summary: "ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: "method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。"
  resolution_round: 2

- id: "R2-W1"
  summary: "Limitations section 格式不合规"
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: "独立 limitations.tex 已创建，位于 references 之前。"
  resolution_round: 3

- id: "R2-W2"
  summary: "实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: "标题改为单数。Qwen3-1.7B cross-scale 实验已加
…[truncated 19556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 7982
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-17T16:12:39.657887+00:00_

_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
conclusion.tex
ethics.tex
experiments.md
experiments.tex
figures
introduction.tex
limitations.tex
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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 8485
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-17T16:12:48.547397+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 long paper page limit formatting requirements template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 long paper page limit formatting requirements template"
  }
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-17T16:12:52.312893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 454 · 2026-05-17T16:12:52.363634+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\pm}2\%$, three seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), applying leave-one-out necessity testing to solver inputs.
4	The resulting metric, Irreducible Solver Rate (ISR), exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, localizing the failure to RL.
5	Repurposed as a reward signal, ISR contains an inherent Goodhart vulnerability: tautological proofs receive artificially high scores by construction, creating a positive feedback loop at all four tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$).
6	At moderate doses, ISR initially yields more genuine output than random controls, but this benefit reverses under stricter classification and disappears under extended training.
7	The effect transfers to Prolog (3/3 seeds, 0\% non-hacking) and exhibits qualitatively distinct gaming modes in single-seed 1.7B evaluation.
8	Across 6 conditions, 2 logic types, 2 model scales, and 5 seeds, we catalog 9 hacking modes and document that $\beta$ controls \emph{when} collapse occurs, not \emph{whether}: ISR is reliable as a diagnostic but unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-17T16:12:52.514587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-17T16:12:52.515100+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\pm}2\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the 
…[truncated 3866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-17T16:12:52.665882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-17T16:12:52.716733+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation 
…[truncated 5566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-17T16:12:56.732753+00:00_

Web search results for query: "ACL Rolling Review 2026 long paper page limit formatting requirements template"

Links: [{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"}]

Based on the search results, here is the information about ACL Rolling Review 2026 long paper requirements:

## Page Limit and Formatting

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page -- up to nine (9) pages of content plus unlimited pages for acknowledgements and references.

## Key Formatting Requirements

ACL provides style files for LaTeX and Microsoft Word that meet these
…[truncated 1023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 8185
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-17T16:13:01.449557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-17T16:13:01.500465+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}) with greedy decoding (Appendix~\ref{app:setup}).
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples ha
…[truncated 18423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-17T16:13:01.952437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-17T16:13:02.304145+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{polu2020generative, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward} and empi
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-17T16:13:02.304515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-17T16:13:02.806423+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses with consistent effects across logic types and model scales (\S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR increases genuine proofs relative to random controls ($\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification (3-seed subset), the effect reverses ($\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.
6	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
7	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-17T16:13:02.957387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-17T16:13:03.108393+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).
8	STA requires solvers supporting component-level input manipulation.
9	
10	\paragraph{Evaluation as temporal snapshot.}
11	All 500-step results represent a temporal snapshot, not an equilibrium.
12	Trajectory analysis on seeds~42 and~45 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient (s42: $17\%{\to}2\%$; s45: $55\%{\to}0\%$ genuine).
13	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
14	
15	\paragraph{Seed counts per dose.}
16	ISR $\beta{=}0.05$ uses three seeds (all H7-dominated); random $\beta{=}0.05$ uses three seeds with high variance ($\text{PR}{=}0\%$, $7\%$, $62\%$); $\beta{=}0.2$ uses three seeds.
17	The primary $\beta{=}0.1$ comparison uses five seeds per condition.
18	Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\S\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.
19	
20	\paragraph{Cross-scale replication.}
21	Our 1.7B experiments use a single seed.
22	Although different seeds may converge to differ
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-17T16:13:03.159081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-17T16:13:03.209747+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in neurosymbolic systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-17T16:13:07.876365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-17T16:13:08.329729+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation protocol.}
53	All cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so that training-log ISR is never compared across runs.
54	The evaluation file \texttt{proofwriter\_fol\_100.jsonl} is a legacy filename cont
…[truncated 43265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-17T16:13:08.330212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-17T16:13:08.382170+00:00_

1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	% ============================================================
43	% Category 2: Reward shaping for code/formal verification
44	% ============================================================
45	
46	@inproceedings{lightman-verify-step,
47	  author 
…[truncated 2576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-17T16:13:13.151578+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-17T16:13:14.758758+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1607
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-17T16:13:15.110625+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && pdfinfo main.pdf 2>/dev/null | grep Pages || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && pdfinfo main.pdf 2>/dev/null | grep Pages || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-17T16:13:16.516892+00:00_

Pages:           22
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-17T16:13:16.668914+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/registry.yaml 2>/dev/null; grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/registry.yaml 2>/dev/null || echo \"Not found in registry\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/registry.yaml 2>/dev/null; grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/registry.yaml 2>/dev/null || echo \"Not found in registry\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-17T16:13:17.933652+00:00_

Not found in registry

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1264
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-17T16:13:18.185117+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*.yaml\" -path \"*/config*\" 2>/dev/null | head -5; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | grep -A5 \"external\" || echo \"Config not found\"",
  "description": "Find project config for external review setting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*.yaml\" -path \"*/config*\" 2>/dev/null | head -5; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | grep -A5 \"external\" || echo \"Config not found\"",
    "description": "Find project config for external review setting"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-17T16:13:18.287121+00:00_

Config not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-17T16:13:21.551385+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -maxdepth 3 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -maxdepth 3 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-17T16:13:21.602150+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/min_necessary_circuit_css.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-17T16:13:25.250466+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml 2>/dev/null",
  "description": "Check external review config in project yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml 2>/dev/null",
    "description": "Check external review config in project yaml"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-17T16:13:25.401526+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-17T16:13:25.402012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-17T16:13:25.452930+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  writing: []
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-17T16:13:30.323793+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml 2>/dev/null || echo \"No external review config found\"",
  "description": "Check for external review setting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml 2>/dev/null || echo \"No external review config found\"",
    "description": "Check for external review setting"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-17T16:13:33.035689+00:00_

No external review config found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 2711
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-17T16:13:33.186936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1-13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "pages": "1-13"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-17T16:13:33.941073+00:00_

PDF pages extracted: 13 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf (589.5KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-17T16:15:05.175449+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息（EMNLP 2026 via ARR）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页 + 无限 references（Limitations 不计入页限，附录不计入页限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/solver-trace-ablation/paper/main.tex`\n- 各 section 在同目录下的独立 .tex 文件中\n- PDF: `projects/solver-trace-ablation/paper/main.pdf`（22 页）\n\n### 审查侧重（你的重点）\n\n请从以下维度严格评审：\n\n1. **方法设计 (Method)**\n   - STA/ISR 方法本身是否有技术贡献？LOO ablation 在这里的应用是否 trivial？\n   - Algorithm 1 仅 6 行伪代码，方法新颖性如何？\n   - ISR 的 premise-count confound 是否被充分处理？\n   - Reward formulation $r = r_{exec} \\cdot (1 + \\beta \\cdot ISR)$ 的设计选择是否充分 justified？\n\n2. **实验设计 (Experimental Design)**\n   - Seed 数量（3-5 seeds）对 claims 的统计支撑是否充分？\n   - Exec-only baseline 用单 seed (s42) 500-step vs ISR/Random 用 5-seed pooled，比较框架是否对称？\n   - SFT baseline（PR=13% vs RL PR=93%）的 PR confound 是否被充分控制？\n   - 1.7B cross-scale 实验仅单 seed，claims 措辞是否过强？\n   - 4 个 β 值是否足以支撑 dose-response claims？\n   - ISR β=0.1 s43/s44 checkpoints 已删除导致 H8 audit 不完整，对结论有何影响？\n\n3. **统计分析 (Statistical Rigor)**\n   - Pooled Fisher test 忽略 seed-level clustering 的问题是否被充分处理？\n   - CMH test 是否应该是 primary 而非 sensitivity？\n   - 5-seed uncorrected OR=3.48 vs 3-seed H8-corrected OR=0.61 的方向反转如何解读？论文的 framing 是否诚实？\n   - 100 eval samples 对 per-seed claims 的统计效力？\n   - \"at all tested doses\" claim 的证据支撑：β=0.3 有无 1000-step trajectory？\n\n4. **可复现性**\n   - 实验细节是否足以复现？\n   - Seed 43 使用 sampling (T=0.7) 而非 greedy decoding 的不一致性\n\n请输出完整审稿意见，包括 Strengths, Weaknesses (must-fix / should-fix / nice-to-have), Questions, 和你对整体质量的初步评分。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息（EMNLP 2026 via ARR）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页 + 无限 references（Limitations 不计入页限，附录不计入页限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/solver-trace-ablation/paper/main.tex`\n- 各 section 在同目录下的独立 .tex 文件中\n- PDF: `projects/solver-trace-ablation/paper/main.pdf`（22 页）\n\n### 审查侧重（你的重点）\n\n请从以下维度严格评审：\n\n1. **方法设计 (Method)**\n   - STA/ISR 方法本身是否有技术贡献？LOO ablation 在这里的应用是否 trivial？\n   - Algorithm 1 仅 6 行伪代码，方法新颖性如何？\n   - ISR 的 premise-count confound 是否被充分处理？\n   - Reward formulation $r = r_{exec} \\cdot (1 + \\beta \\cdot ISR)$ 的设计选择是否充分 justified？\n\n2. **实验设计 (Experimental Design)**\n   - Seed 数量（3-5 seeds）对 claims 的统计支撑是否充分？\n   - Exec-only baseline 用单 seed (s42) 500-step vs ISR/Random 用 5-seed pooled，比较框架是否对称？\n   - SFT baseline（PR=13% vs RL PR=93%）的 PR confound 是否被充分控制？\n   - 1.7B cross-scale 实验仅单 seed，claims 措辞是否过强？\n   - 4 个 β 值是否足以支撑 dose-response claims？\n   - ISR β=0.1 s43/s44 checkpoints 已删除导致 H8 audit 不完整，对结论有何影响？\n\n3. **统计分析 (Statistical Rigor)**\n   - Pooled Fisher test 忽略 seed-level clustering 的问题是否被充分处理？\n   - CMH test 是否应该是 primary 而非 sensitivity？\n   - 5-seed uncorrected OR=3.48 vs 3-seed H8-corrected OR=0.61 的方向反转如何解读？论文的 framing 是否诚实？\n   - 100 eval samples 对 per-seed claims 的统计效力？\n   - \"at all tested doses\" claim 的证据支撑：β=0.3 有无 1000-step trajectory？\n\n4. **可复现性**\n   - 实验细节是否足以复现？\n   - Seed 43 使用 sampling (T=0.7) 而非 greedy decoding 的不一致性\n\n请输出完整审稿意见，包括 Strengths, Weaknesses (must-fix / should-fix / nice-to-have), Questions, 和你对整体质量的初步评分。"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-17T16:15:28.433871+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23258
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-17T16:15:28.584867+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**: 新颖性 + 写作质量 + 格式合规 + 完整性\n\n### Venue 信息（EMNLP 2026 via ARR）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页 + 无限 references（Limitations 不计入页限，附录不计入页限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/solver-trace-ablation/paper/main.tex`\n- 各 section 在同目录下的独立 .tex 文件中\n- PDF: `projects/solver-trace-ablation/paper/main.pdf`（22 页）\n\n### 审查侧重（你的重点）\n\n请从以下维度严格评审：\n\n1. **新颖性 (Novelty)**\n   - \"Diagnostic becomes optimization target\" 这个 insight 是否只是 Goodhart's Law 的直接推论？empirical contribution 的增量在哪里？\n   - LOO ablation 本身是标准方法（mutation testing），应用到 solver inputs 的贡献程度？\n   - 9-mode hacking taxonomy 的分类学贡献是否足够？分类标准是否 principled？\n   - 与 Kim et al. (2026)、Bondarenko et al. (2025) 等直接相关工作的差异化是否清晰？\n\n2. **写作质量 (Writing)**\n   - Abstract 数据密度：当前 abstract (~220 words) 包含多少个数字/统计量？读感如何？30 秒内能否消化核心贡献？\n   - Introduction 结构：使用了多个 \\paragraph{} 小标题，是否导致叙事碎片化？\n   - §4.3 (Goodhart Effects) 的实验报告按 β 值逐一描述（Low-dose/Micro-dose/Medium-dose/High-dose），是否过于重复？\n   - AI 写作痕迹检查：em-dash (—)、解释性 en-dash (–)、-ing phrase endings、过度分段、blacklisted words (delve/leverage/utilize/facilitate/myriad/plethora)\n   - 专有名词首次出现是否有定义？\n   - Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 引用了 Manheim & Garrabrant (2019) 多次但是否指定了具体 variant？\n\n3. **格式合规 (Format)**\n   - 正文是否在 8 页内？（检查 §5 Discussion and Conclusion 是否完整结束于第 8 页）\n   - Limitations section 位置是否正确（conclusion 之后、references 之前）？\n   - Ethics Statement 是否存在？\n   - 匿名化是否到位（author = \"Anonymous ACL submission\"）？\n   - Table 1 的 caption 长度和可读性\n   - Table 2 (hacking taxonomy) 的信息密度和可读性\n   - Figure 字体大小是否 ≥ 7pt？\n\n4. **引用完整性 (Reference Coverage)**\n   - 引用数量是否达到 EMNLP 级别？（当前 ~30 条）\n   - 是否覆盖：直接相关方法、baseline 论文、评测 benchmark、理论基础？\n   - 是否缺少重要引用？特别检查：\n     - Reward hacking / specification gaming 领域\n     - Formal verification with RL 领域\n     - Reward tampering 领域\n   - 引用格式是否一致（arXiv preprint vs. conference proceedings）？\n\n5. **完整性 (Completeness)**\n   - Contribution claims (C1-C4) 是否都有对应的 section/table 支撑？\n   - Appendix 内容是否在正文中被引用？\n   - 是否有 orphan 引用或未引用的 bib entries？\n\n请输出完整审稿意见，包括 Strengths, Weaknesses (must-fix / should-fix / nice-to-have), Missing References, 和你对整体质量的初步评分。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**: 新颖性 + 写作质量 + 格式合规 + 完整性\n\n### Venue 信息（EMNLP 2026 via ARR）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页 + 无限 references（Limitations 不计入页限，附录不计入页限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/solver-trace-ablation/paper/main.tex`\n- 各 section 在同目录下的独立 .tex 文件中\n- PDF: `projects/solver-trace-ablation/paper/main.pdf`（22 页）\n\n### 审查侧重（你的重点）\n\n请从以下维度严格评审：\n\n1. **新颖性 (Novelty)**\n   - \"Diagnostic becomes optimization target\" 这个 insight 是否只是 Goodhart's Law 的直接推论？empirical contribution 的增量在哪里？\n   - LOO ablation 本身是标准方法（mutation testing），应用到 solver inputs 的贡献程度？\n   - 9-mode hacking taxonomy 的分类学贡献是否足够？分类标准是否 principled？\n   - 与 Kim et al. (2026)、Bondarenko et al. (2025) 等直接相关工作的差异化是否清晰？\n\n2. **写作质量 (Writing)**\n   - Abstract 数据密度：当前 abstract (~220 words) 包含多少个数字/统计量？读感如何？30 秒内能否消化核心贡献？\n   - Introduction 结构：使用了多个 \\paragraph{} 小标题，是否导致叙事碎片化？\n   - §4.3 (Goodhart Effects) 的实验报告按 β 值逐一描述（Low-dose/Micro-dose/Medium-dose/High-dose），是否过于重复？\n   - AI 写作痕迹检查：em-dash (—)、解释性 en-dash (–)、-ing phrase endings、过度分段、blacklisted words (delve/leverage/utilize/facilitate/myriad/plethora)\n   - 专有名词首次出现是否有定义？\n   - Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 引用了 Manheim & Garrabrant (2019) 多次但是否指定了具体 variant？\n\n3. **格式合规 (Format)**\n   - 正文是否在 8 页内？（检查 §5 Discussion and Conclusion 是否完整结束于第 8 页）\n   - Limitations section 位置是否正确（conclusion 之后、references 之前）？\n   - Ethics Statement 是否存在？\n   - 匿名化是否到位（author = \"Anonymous ACL submission\"）？\n   - Table 1 的 caption 长度和可读性\n   - Table 2 (hacking taxonomy) 的信息密度和可读性\n   - Figure 字体大小是否 ≥ 7pt？\n\n4. **引用完整性 (Reference Coverage)**\n   - 引用数量是否达到 EMNLP 级别？（当前 ~30 条）\n   - 是否覆盖：直接相关方法、baseline 论文、评测 benchmark、理论基础？\n   - 是否缺少重要引用？特别检查：\n     - Reward hacking / specification gaming 领域\n     - Formal verification with RL 领域\n     - Reward tampering 领域\n   - 引用格式是否一致（arXiv preprint vs. conference proceedings）？\n\n5. **完整性 (Completeness)**\n   - Contribution claims (C1-C4) 是否都有对应的 section/table 支撑？\n   - Appendix 内容是否在正文中被引用？\n   - 是否有 orphan 引用或未引用的 bib entries？\n\n请输出完整审稿意见，包括 Strengths, Weaknesses (must-fix / should-fix / nice-to-have), Missing References, 和你对整体质量的初步评分。"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-17T16:15:29.891881+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1307
}
```

</details>

---


### Assistant

_source line 496 · 2026-05-17T16:15:35.354079+00:00_

Round 1 任务已分配给两位 Reviewer。等待审稿结果返回。

- **Reviewer 1** (方法/实验/统计): 已触发
- **Reviewer 2** (新颖性/写作/格式/完整性): 已触发

收到审稿结果后进入 Step 2 交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 497 · 2026-05-17T16:21:57.940674+00:00_

[Reviewer 1 审稿意见]:
## Round 1 审稿意见 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）

### 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 问题重要且叙事清晰，但实验设计中的多处不对称比较、被删除的关键 checkpoint 导致核心 claim 的统计支撑不足，方法贡献偏薄。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心比较框架存在多处不对称（exec-only 单 seed vs ISR 5-seed pooled；SFT PR=13% vs RL PR=93%）；OR 方向反转的 framing 偏乐观；s43/s44 checkpoint 丢失导致 primary analysis 不完整 |
| Excitement | 3.5/5 | "诊断工具自身被 Goodhart 化" 的叙事有新意，hacking taxonomy 有实用价值，与 AI safety 社区高度相关 |
| Reproducibility | 3/5 | 超参完整，算法清晰，但 s43/s44 checkpoint 已删且无法恢复，s43 eval 使用 sampling 而非 greedy，部分关键实验无法独立验证 |
| Confidence | 4/5 | 仔细阅读了全文和附录，熟悉 reward hacking / GRPO / neurosymbolic reasoning 文献 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] Exec-only baseline 在 Table 1 中的不对称比较
- 具体位置：Table 1 (§4.2)，脚注 †
- 问题：Table 1 的 exec-only 行使用**单 seed (s42)、500-step、greedy decoding**，而 ISR/Random β=0.1 使用**5-seed pooled**。这不是同类比较。3-seed 1000-step exec-only 数据（Appendix Table 9: 所有 seed 收敛至 ≥94% PR + near-zero genuine）被放在附录而非主表。读者看 Table 1 会自然地将 exec-only 的 N-H=8% 与 ISR 的 N-H=23% 相比较，但一个是单 seed 一个是 5-seed pooled，一个是 500-step 一个有 1000-step 数据可用。
- 为什么影响接收：主表是审稿人最先看的实验证据，不对称的比较框架会让审稿人质疑所有下游 claim 的可信度。
- 建议修改方向：Table 1 中 exec-only 行应改为 3-seed pooled 1000-step 数据（与 SFT 对齐），或在主表中同时呈现 500-step 和 1000-step 结果。

**N2** [critical] 5-seed uncorrected OR=3.48 vs 3-seed corrected OR=0.61 的方向反转：framing 不够诚实
- 具体位置：§4.2 "The transient genuine window" 段落；Table 4 (Appendix)；§5
- 问题：论文的核心 claim 之一是 "ISR initially yields more genuine output than random controls"（Abstract L5-6）。主文首先报告 5-seed pooled Fisher OR=3.48（ISR 显著优于 random），然后提到 3-seed H8+FN-corrected OR=0.61（方向反转，n.s.）。论文将二者 frame 为 "bound the true effect from above and below"。但 3-seed corrected 分析使用了更完整的审计数据（包含 H8 reclassification 和 H7b false-negative correction），是**更可信**的估计。5-seed 分析包含两个 checkpoint 已删除、H8 audit 未完成的 seed（s43、s44），其 N-H 率是 uncorrected upper bound（Table 1 脚注 ‡）。
- 为什么影响接收：这是论文最核心的定量比较之一。如果 corrected 分析才是更可靠的估计，那么 ISR 在 transient window 内的 genuine 优势可能根本不存在。论文应将 corrected 分析作为 primary，uncorrected 作为 sensitivity/upper bound，而非反过来。
- 建议修改方向：（1）明确说明 3-seed corrected 是 primary analysis，5-seed uncorrected 是 upper bound；（2）Abstract 和 Introduction 中关于 "ISR initially yields more genuine output" 的措辞需要弱化；（3）Discussion 应直接讨论 "transient benefit 是否真实存在的不确定性"。

**N3** [critical] ISR β=0.1 s43/s44 checkpoint 丢失，削弱了核心分析的完整性
- 具体位置：Appendix D.1；Table 1 脚注 ‡；Table 5 (Appendix)
- 问题：ISR β=0.1 的 s43 和 s44 checkpoint 在 H8 audit 之前被删除，无法恢复。这意味着：（1）5-seed pooled N-H rate (23%) 是不完整的上界；（2）H8 模式在这两个 seed 上的发生率未知；（3）核心 CMH test 的分层估计可能偏高。
- 为什么影响接收：关键数据的不可恢复缺失是严重的可复现性问题。脚注确实标注了，但应该更突出。
- 建议修改方向：（1）Limitations 中明确列出 checkpoint 丢失的影响；（2）所有引用 5-seed pooled N-H 的地方标注 "(uncorrected upper bound)"；（3）考虑在主表中将 ISR β=0.1 的 N-H 列报告为区间 [6%, 23%]。

**N4** [critical] SFT vs RL 比较中 PR 严重混淆
- 具体位置：§4.1 "SFT baseline"；Appendix E.3
- 问题：SFT 达到 PR=13%（n=39 proved），而 RL 各条件达到 PR=66-97%。论文声称 "near-absence of hacking under identical data exposure is consistent with hacking being RL-specific"。但 SFT 和 RL 的 PR 差距巨大（13% vs 93%），SFT 只有 39 个 proved sample。100-step exec-only checkpoint（PR=32%，hacking=31.2%）部分控制了这个混淆，但 32% 仍远低于收敛时的 93%+。**核心问题是：我们无法知道 SFT 在高 PR 时是否也会 hack**，因为 SFT 根本达不到高 PR。
- 为什么影响接收：C1（"localizing the failure to RL"）是四个 contribution 之一，证据链有 PR confound。
- 建议修改方向：将 claim 弱化为 "SFT does not produce hacking at its achievable PR range; whether hacking would emerge at higher PR under a different SFT setup remains unknown"。

**N5** [critical] 统计分析层级倒置：pooled Fisher 不应作为 primary analysis
- 具体位置：§4.2；Table 4 (Appendix)；§4.5
- 问题：论文在主文中首先报告 pooled Fisher exact test（OR=3.48），将 CMH test 作为 sensitivity 放在附录。但实验存在明显的 within-seed clustering（同一 seed 的 proved samples 高度相关），pooled Fisher 忽略这一结构会膨胀 Type I error。CMH 天然应该是 primary analysis。Seed-level permutation test（p=0.26/0.28）与 Fisher（p<10⁻⁸）的巨大差距恰恰说明 clustering 的严重性。
- 为什么影响接收：统计分析的层级选择直接影响所有定量 claim 的可信度。
- 建议修改方向：（1）主文中将 CMH 结果前置为 primary；（2）Fisher 作为 sensitivity；（3）讨论 seed-level permutation test 的 power analysis。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 方法贡献偏薄
- 具体位置：§3 Method；Algorithm 1
- 问题：论文坦诚承认 "LOO ablation itself is standard; our contribution lies in applying it"。Algorithm 1 只有 6 行伪代码，ISR 是简单的必要组件比例。这更像 empirical study 而非 method paper。
- 建议：在 Introduction 中更明确地 position 为 empirical study，或补充方法层面的探索。

**W2** [warning] Dose-response claim 基于 4 个 β 值、不均匀的 seed 数
- 具体位置：§4.2 "Non-monotonic dose-response"
- 问题：β∈{0.05, 0.1, 0.2, 0.3} 只有 4 个点，β=0.1 用 5 seeds 而其余用 3 seeds。"Non-monotonic dose-response" 的 claim 在统计上无法支撑。
- 建议：弱化为 "the pattern across four tested doses suggests..."。

**W3** [warning] 1.7B cross-scale claims 仅基于单 seed
- 具体位置：§4.4；Table 1 下半部分
- 问题：在 4B scale，3 个 seed 产生了 3 种截然不同的 hacking mode，说明单 seed 几乎不具备代表性。"H9 never appears at 4B scale" 可能只是 seed 不够多。
- 建议：主文 §4.4 弱化因果性措辞，明确标记为 "preliminary single-seed observation"。

**W4** [warning] "at all tested doses" claim 缺少 β=0.3/0.05 的 trajectory 数据
- 具体位置：Abstract L5-6；§1 ¶4；§4.2
- 问题：1000-step trajectory 分析仅对 β=0.1 的 2 个 seed 进行了。β=0.3 和 β=0.05 只有 500-step snapshot。论文自身方法论认为 "snapshot evaluation would overestimate ISR's benefit"，但对自己的 β=0.3/0.05 claim 却使用了 snapshot。
- 建议：弱化 claim 或补充 trajectory 数据。

**W5** [warning] 100 个 eval examples 对 per-seed claims 的统计效力不足
- 具体位置：§4 Setup
- 问题：一些 per-seed proved sample 数极小（ISR β=0.3 s42 仅 n=18；Prolog exec-only s44 仅 n=21），百分比信息量极低。
- 建议：对小 n seed 报告 CI 而非点估计。

**W6** [warning] Seed 43 exec-only 使用 sampling (T=0.7) 而非 greedy decoding
- 具体位置：Appendix A (L55-56)；Table 8
- 问题：违反 unified evaluation protocol (C004)，s43 与其他 seed 不可直接比较，但 s43 数据仍用于主文 §4.1 claims。
- 建议：主文引用 s43 时标注 eval 不一致性。

---

### 小问题
- Table 1 caption 脚注过多（6 个标记），建议拆分为表下注释
- §3.2 "mean n=5.58 vs. 8.46 for random" 缺少 CI/SE
- References: `folio` 年份 mismatch（bib=2024 vs OpenAlex=2022），应确认 venue 一致性
- `metr-reward-hacking` 引用类型为 misc，缺少 venue/URL
- Discussion (§5) 仅 7 行，对实验发现丰富的论文来说讨论不够充分

---

### 主要优势
1. **问题定义和叙事质量高**："诊断工具自身被 Goodhart 化"的叙事简洁有力
2. **实验覆盖面广**：6 conditions × 5 seeds × 2 logic types × 2 scales，附录极其详尽
3. **诚实的 self-disclosure**：premise-count confound、OR reversal、checkpoint 丢失、eval 不一致均被主动披露
4. **Hacking taxonomy 有独立价值**：9 种模式可直接应用于其他 neurosymbolic 系统
5. **Control design 方向正确**：SFT control 和 random control 分离 RL-specific 和 generic variance effect 的思路好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 498 · 2026-05-17T16:22:06.383036+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 499 · 2026-05-17T16:22:08.938417+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

**评分总结**: Overall 3.5 (Borderline Conference), Soundness 2.5, Excitement 3.5, Reproducibility 3。

**核心问题**：5 个 must-fix（Table 1 不对称比较、OR 反转 framing、checkpoint 丢失、SFT PR confound、统计层级倒置）+ 6 个 should-fix（方法贡献薄、dose-response 仅 4 点、1.7B 单 seed、β=0.3 缺 trajectory、100 eval samples、s43 eval 协议不一致）。

**主要优势**：叙事质量高、实验覆盖广、self-disclosure 诚实、hacking taxonomy 有独立价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 500 · 2026-05-17T16:22:14.646335+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 44

## Round 44

6 recorded events


### User

_source line 501 · 2026-05-17T16:22:52.650113+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 完整审稿意见

**论文**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation
**Venue**: EMNLP 2026 via ACL Rolling Review
**审查侧重**: 新颖性 + 写作质量 + 格式合规 + 完整性

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 实验彻底但新颖性有限——核心发现（Goodhart's Law 的经验实例）在理论上可预测，写作过度数据密集导致叙事被淹没，且核心指标存在命名不一致的严重错误。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨（多 seed、统计检验、CMH 分层、多 dose），但实验范围窄（单一模型族 Qwen3 + 单一数据集 FOLIO）限制了 claim 的可推广性 |
| Excitement | 2/5 | "诊断指标被优化时会被 game" 本质上是 Goodhart's Law 的直接推论；经验贡献在理论预测框架内，缺少意料之外的发现 |
| Overall Assessment | 3.0 | Findings 水平：实验工作扎实但 insight 增量有限，适合作为经验案例记录发表 |
| Confidence | 4/5 | 熟悉 reward hacking、neurosymbolic reasoning、RL for reasoning 相关文献 |
| Reproducibility | 4/5 | 超参数表完整，数据集公开，算法伪代码清晰；eval protocol 有详细说明 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] ISR 核心指标命名不一致
- 具体位置：Abstract (abstract.tex:4) vs. Introduction (introduction.tex:15) vs. Method (method.tex:44)
- 问题：Abstract 将 ISR 定义为 **"Irreducible Solver Rate"**，Introduction 和 Method 将其定义为 **"Intensional Structural Reward"**。这是论文最核心概念的名称冲突。
- 为什么影响接收：审稿人会认为这是草率写作或版本合并遗留错误，严重损害可信度。核心指标连名字都不统一，reader 无法确定作者是否对自己的贡献有清晰理解。
- 建议修改方向：统一为一个名称。建议保留 "Intensional Structural Reward" (与 Method §3 一致)，同时修改 Abstract。

**N2** [critical] 新颖性 framing 不足——论文核心发现是 Goodhart's Law 的已知推论
- 具体位置：Introduction ¶4 (introduction.tex:24-28), §4.3 全节, Related Work (related_work.tex:14-20)
- 问题：论文核心 claim 是 "diagnostic becomes optimization target"，但这恰恰是 Goodhart's Law 的定义。论文自己承认这一点（introduction.tex:26 引用 manheim-goodhart-taxonomy），但没有说服 reader 这个经验实例为什么值得一篇论文。
  - LOO ablation 是标准方法（mutation testing），应用到 solver inputs 是工程适配，不是方法论贡献（论文自己在 method.tex:26 和 related_work.tex:23 承认）。
  - 9-mode taxonomy 是 post-hoc 分类，缺少 principled 的分类标准（为什么是这 9 种而不是其他？有没有理论完备性论证？）。
  - Goodhart collapse at all tested doses 是实验观察，但理论上可从 ISR 的数学定义直接推导（method.tex:55-56 已经给出了 H7 tautology 获得 ISR≥0.5 的构造性论证）。
- 为什么影响接收：Excitement 维度是 ARR 最关键的评分维度之一。论文需要说服 reader 为什么一个可从定义推导的结果值得经验验证——目前的 framing 没有做到。
- 建议修改方向：
  (1) 强调 **意料之外** 的经验发现（如 stochastic bifurcation、non-monotonic dose-response、cross-scale mode divergence），这些是理论无法预测的；
  (2) 将 taxonomy 的贡献定位为 "operational toolkit for practitioners" 而非 "intellectual contribution"；
  (3) 明确区分 "predictable that Goodhart effects exist" vs. "unpredictable which modes emerge and how they interact"。

**N3** [critical] Abstract 数据过载——30 秒内无法消化核心贡献
- 具体位置：Abstract (abstract.tex:1-9, ~220 words)
- 问题：Abstract 包含至少 15 个独立数字/统计量：97±2%, 99.5%, 92%, β∈{0.05, 0.1, 0.2, 0.3}, 3/3 seeds, 0%, 6 conditions, 2 logic types, 2 model scales, 5 seeds, 9 hacking modes, ρ=−0.049 (implicit via "structural collapse")。这是实验报告风格，不是故事。
- 为什么影响接收：审稿人在 30 秒内判断论文价值。当前 Abstract 读起来像一个压缩的 results table，核心 insight 被数字淹没。
- 建议修改方向：保留 3-4 个最关键数字（ISR collapse 幅度、non-hacking rate 对比、dose-response 结论），其余细节移到 Introduction 或 Results。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Introduction 叙事碎片化
- 具体位置：Introduction (introduction.tex), 5 个 \paragraph{} 子标题
- 问题：Introduction 被 5 个 \paragraph{} 打断（"The execution-only blind spot", "Component necessity testing", "ISR as diagnostic", "ISR as reward: Goodhart collapse at all tested doses", "Contributions"），导致叙事碎片化。读者在 disconnected 的 mini-sections 之间跳跃，而不是跟随一个连贯的故事。
- 建议：减少到 2-3 个 \paragraph{}，或者完全去掉、改用自然段过渡。当前结构更像一个 extended abstract 而不是 introduction。

**W2** [warning] §4.3 Goodhart Effects 的 β 值呈现顺序混乱
- 具体位置：experiments.tex:79-124
- 问题：四个 dose 按 β=0.1→0.05→0.2→0.3 顺序呈现，不是升序。β=0.1 被标为 "Low-dose" 而 β=0.05 被标为 "Micro-dose"。这个非单调的呈现顺序增加了 reader 的认知负荷。
- 建议：按 β 升序呈现（0.05→0.1→0.2→0.3），或至少在开头给出一句解释为什么选择当前顺序（如 "we begin with β=0.1 as the primary comparison point"）。

**W3** [warning] 实验范围窄：单一模型族 + 单一数据集
- 具体位置：Limitations (limitations.tex:1-4), Experiments §4.1 (experiments.tex:10)
- 问题：所有实验使用 Qwen3-4B（1.7B 只有 single seed），FOLIO 是唯一数据集（500 训练 / 100 评估）。论文标题暗示是关于 "neurosymbolic proof generation" 的一般性发现，但实验只支持 "Qwen3 on FOLIO" 的结论。
- 建议：标题或 claim 中增加限定语（如 "a case study"），或在 Limitations 中更突出地讨论 generalization risk。

**W4** [warning] 1.7B 跨尺度实验太薄
- 具体位置：§4.5 (experiments.tex:138-141), Table 1 bottom rows
- 问题：1.7B 实验仅 single seed，但论文从中得出了 "different capacities converge to different Goodhart basins" 的 claim。Single seed 不支持任何关于 scale-dependent 行为的一般性结论。
- 建议：要么增加 seed（理想），要么将 claim 弱化为 "preliminary observation"（当前文字已部分做到，但 Table 1 中 1.7B 行的呈现方式暗示了与 4B 的对称比较）。

**W5** [warning] ISR 名称本身具有误导性
- 具体位置：method.tex:44, 论文全文
- 问题：无论最终统一到哪个名称，"Intensional Structural **Reward**" 的名字暗示它应该被用作 reward，但论文的核心结论恰恰是它不应该被用作 reward。这个命名自相矛盾。"Irreducible Solver Rate" 作为名称更中性，但与方法章节不一致。
- 建议：考虑将名称统一为不含 "Reward" 的版本，避免读者困惑。

**W6** [warning] LOO 缩写未在首次使用时定义
- 具体位置：introduction.tex:16 首次使用 "LOO ablation"
- 问题："LOO" 作为 "Leave-One-Out" 的缩写在正文中频繁使用（>15 次），但首次出现时未以 "(LOO)" 形式正式定义。Introduction 中使用了 "leave-one-out ablation" 全称，但 LOO 缩写直接出现在 introduction.tex:16 而无括号展开。
- 建议：在首次使用处添加 "leave-one-out (LOO) ablation"。

**W7** [warning] Table 1 caption 过长
- 具体位置：experiments.tex:74 (Table 1 caption)
- 问题：Caption 包含约 120 words 的注释和脚注说明，几乎是一个独立段落。读者需要反复参照 caption 才能理解表格，信息密度过高。
- 建议：将条件说明移到正文或 Appendix，caption 仅保留表格内容的简要描述。

**W8** [warning] Hacking taxonomy 的分类标准不够 principled
- 具体位置：§4.6 (experiments.tex:147-176), Appendix §B (appendix.tex:192-480)
- 问题：9 种 hacking mode 是 post-hoc 从实验中归纳的，没有理论完备性论证（即"为什么恰好是这 9 种"）。部分 mode 之间存在语义重叠（H7a "conclusion duplication" 和 "tautological collapse" 的区别仅在 component count；H1 和 H7 是 gradient 关系）。
- 建议：讨论 taxonomy 是否 exhaustive，是否存在理论框架可以统一这些 mode（如按 proof-theoretic properties 分类）。

---

## 小问题（不影响接收）

- appendix.tex:1 注释中包含 em-dash (`% Appendix — solver-trace-ablation`)，虽然不渲染但应清理。
- experiments.tex:176 和 appendix.tex:55, 130 等处有少量 "-ing" trailing clauses ("indicating that the associations are robust...")，可适度改写。
- bib 条目 `folio` year mismatch: bib 标注 2024，OpenAlex 记录 2022（可能是 conference vs. arXiv 版本差异）。
- bib 条目 `jia-harman-survey` 标注 2011，OpenAlex 显示 2010。
- bib 条目 `deepseek-prover-v15` 等的 author 字段不规范（"DeepSeek AI" 而非实际第一作者）。
- Figure 1 部分标签字体可能接近 7pt 下限（视觉审查存疑，建议作者自查）。
- experiments.tex:56 中 eval protocol 差异（s43 用 sampling 而非 greedy）在 Appendix 提到但正文 Table 1 未标注。

---

## 引用完整性

**当前状态**：37 条引用，全部被 cite，无 orphan 无 missing。覆盖面：
- ✅ Reward hacking / specification gaming: Skalse 2022, Krakovna 2020, Bondarenko 2025, Kim 2026, METR 2025, Wang et al. 2026 survey
- ✅ Neurosymbolic reasoning: SatLM, Logic-LM, LINC, FoVer, LoRP
- ✅ Process rewards: Lightman 2024, Math-Shepherd, VersaPRM, ThinkPRM
- ✅ Goodhart theory: Manheim & Garrabrant 2019, Karwowski 2024, Kwa 2024, Gao 2023
- ✅ Mutation testing: DeMillo 1978, Jia & Harman 2011

**可能缺失的引用**（非强制，但会增强 coverage）：
1. **Amodei et al. (2016), "Concrete Problems in AI Safety"** — reward hacking 讨论的 foundational reference
2. **Christiano et al. (2017), "Deep RL from Human Preferences"** — RLHF 奠基工作，讨论 reward misspecification
3. **DeepSeek-R1 (2025)** — 使用 GRPO 的代表性工作，直接相关
4. **Shortcut learning 综述 (Geirhos et al. 2020)** — 论文讨论的 "degenerate shortcuts" 与 shortcut learning 文献有天然联系
5. **Formal verification/theorem proving**: AlphaProof 或 LEGO-Prover 等较新工作

37 条引用在 EMNLP 中偏少（典型 long paper 40-60 条），但不是 critical issue。

---

## Contribution 完整性检查

| Contribution | 对应支撑 | 状态 |
|---|---|---|
| C1: ISR as diagnostic | §4.2, Figure 2, Table 1 (exec-only) | ✅ 完整 |
| C2: Goodhart collapse at 4 doses | §4.3, Table 1, Appendix Tables | ✅ 完整 |
| C3: Prolog transfer | §4.4, Appendix Table 5, Figure 4 | ✅ 完整 |
| C4: 9-mode taxonomy | §4.6, Table 2, Appendix §B | ✅ 完整 |

所有 Appendix 内容均在正文中被引用。无 orphan appendix sections。

---

## 主要优势

1. **实验设计严谨**：多 seed（3-5 per condition）、matched random controls、CMH 分层统计检验、1000-step trajectory analysis、premise-count-matched comparison。这是该领域少见的统计严谨度。
2. **透明度高**：论文坦诚承认 ISR 的局限（premise-count confound, method.tex:53-58），坦诚报告 negative results（ISR 作为 reward 不 work），坦诚报告数据缺失（s43/s44 checkpoints deleted before audit, appendix.tex:250）。
3. **Cross-validation 思维**：text-match classifier + functional LOO analysis 的双重验证发现了 H7b obfuscated tautology 和 query-as-fact gaming，体现了 careful empirical work。
4. **Cautionary value**：对 neurosymbolic RL 社区有实际警示价值——execution-only evaluation 不足以判断 formalization quality。
5. **Hacking taxonomy 有操作价值**：虽然分类标准不够 principled，但 9 种 mode 的具体定义和示例对从业者有直接参考价值。

---

## 审稿人总结

这是一篇实验认真、报告透明的经验性论文。核心发现（ISR 作为 diagnostic 有效但作为 reward 失败）有实用价值，但理论上是 Goodhart's Law 的直接推论，缺少意料之外的 insight。实验范围局限于 Qwen3 + FOLIO，且 ISR 命名不一致是严重的写作错误。建议修复命名问题、压缩 Abstract 数据密度、强化 novelty framing（突出理论无法预测的经验发现），方可达到 Conference 水平。当前以 Findings 推荐。

Sources:
- [ACL Rolling Review Form](https://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-17T16:23:30.897645+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分\nOverall: 3.5 (Borderline Conference), Soundness 2.5/5, Excitement 3.5/5, Reproducibility 3/5\n\n### Must-Fix 问题\n\n**R1-N1** [critical] Exec-only baseline 在 Table 1 中的不对称比较\n- Table 1 的 exec-only 行使用单 seed (s42)、500-step、greedy decoding，而 ISR/Random β=0.1 使用 5-seed pooled。3-seed 1000-step exec-only 数据在附录但不在主表。\n\n**R1-N2** [critical] 5-seed uncorrected OR=3.48 vs 3-seed corrected OR=0.61 的方向反转：framing 不够诚实\n- 论文将二者 frame 为 \"bound the true effect from above and below\"，但 3-seed corrected 分析使用了更完整的审计数据，应作为 primary。5-seed 分析包含 checkpoint 已删除的 seed。\n\n**R1-N3** [critical] ISR β=0.1 s43/s44 checkpoint 丢失，削弱了核心分析的完整性\n- 5-seed pooled N-H rate (23%) 是不完整的上界。建议报告区间 [6%, 23%]。\n\n**R1-N4** [critical] SFT vs RL 比较中 PR 严重混淆\n- SFT PR=13% (n=39) vs RL PR=93%+。核心问题：无法知道 SFT 在高 PR 时是否也会 hack。C1 \"localizing the failure to RL\" 证据链有 PR confound。\n\n**R1-N5** [critical] 统计分析层级倒置：pooled Fisher 不应作为 primary analysis\n- 实验存在 within-seed clustering，pooled Fisher 忽略这一结构会膨胀 Type I error。CMH 应该是 primary。Seed-level permutation test (p=0.26/0.28) 与 Fisher (p<10⁻⁸) 的巨大差距说明 clustering 严重。\n\n### Should-Fix 问题\n\n**R1-W1** 方法贡献偏薄（Algorithm 1 仅 6 行伪代码）\n**R1-W2** Dose-response claim 基于 4 个 β 值、不均匀的 seed 数\n**R1-W3** 1.7B cross-scale claims 仅基于单 seed\n**R1-W4** \"at all tested doses\" claim 缺少 β=0.3/0.05 的 trajectory 数据\n**R1-W5** 100 个 eval examples 对 per-seed claims 的统计效力不足\n**R1-W6** Seed 43 exec-only 使用 sampling (T=0.7) 而非 greedy decoding\n\n### 主要优势\n1. 叙事质量高\n2. 实验覆盖面广\n3. Self-disclosure 诚实\n4. Hacking taxonomy 有独立价值\n5. Control design 方向正确\n\n---\n\n请对每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，附上你的理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分\nOverall: 3.5 (Borderline Conference), Soundness 2.5/5, Excitement 3.5/5, Reproducibility 3/5\n\n### Must-Fix 问题\n\n**R1-N1** [critical] Exec-only baseline 在 Table 1 中的不对称比较\n- Table 1 的 exec-only 行使用单 seed (s42)、500-step、greedy decoding，而 ISR/Random β=0.1 使用 5-seed pooled。3-seed 1000-step exec-only 数据在附录但不在主表。\n\n**R1-N2** [critical] 5-seed uncorrected OR=3.48 vs 3-seed corrected OR=0.61 的方向反转：framing 不够诚实\n- 论文将二者 frame 为 \"bound the true effect from above and below\"，但 3-seed corrected 分析使用了更完整的审计数据，应作为 primary。5-seed 分析包含 checkpoint 已删除的 seed。\n\n**R1-N3** [critical] ISR β=0.1 s43/s44 checkpoint 丢失，削弱了核心分析的完整性\n- 5-seed pooled N-H rate (23%) 是不完整的上界。建议报告区间 [6%, 23%]。\n\n**R1-N4** [critical] SFT vs RL 比较中 PR 严重混淆\n- SFT PR=13% (n=39) vs RL PR=93%+。核心问题：无法知道 SFT 在高 PR 时是否也会 hack。C1 \"localizing the failure to RL\" 证据链有 PR confound。\n\n**R1-N5** [critical] 统计分析层级倒置：pooled Fisher 不应作为 primary analysis\n- 实验存在 within-seed clustering，pooled Fisher 忽略这一结构会膨胀 Type I error。CMH 应该是 primary。Seed-level permutation test (p=0.26/0.28) 与 Fisher (p<10⁻⁸) 的巨大差距说明 clustering 严重。\n\n### Should-Fix 问题\n\n**R1-W1** 方法贡献偏薄（Algorithm 1 仅 6 行伪代码）\n**R1-W2** Dose-response claim 基于 4 个 β 值、不均匀的 seed 数\n**R1-W3** 1.7B cross-scale claims 仅基于单 seed\n**R1-W4** \"at all tested doses\" claim 缺少 β=0.3/0.05 的 trajectory 数据\n**R1-W5** 100 个 eval examples 对 per-seed claims 的统计效力不足\n**R1-W6** Seed 43 exec-only 使用 sampling (T=0.7) 而非 greedy decoding\n\n### 主要优势\n1. 叙事质量高\n2. 实验覆盖面广\n3. Self-disclosure 诚实\n4. Hacking taxonomy 有独立价值\n5. Control design 方向正确\n\n---\n\n请对每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，附上你的理由。"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-17T16:23:42.656046+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11758
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-17T16:23:42.756852+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分\nOverall: 3.0 (Findings), Soundness 4/5, Excitement 2/5, Reproducibility 4/5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] ISR 核心指标命名不一致\n- Abstract 将 ISR 定义为 \"Irreducible Solver Rate\"，Introduction/Method 定义为 \"Intensional Structural Reward\"。核心概念的名称冲突。\n\n**R2-N2** [critical] 新颖性 framing 不足——论文核心发现是 Goodhart's Law 的已知推论\n- \"Diagnostic becomes optimization target\" 是 Goodhart's Law 的定义。论文没有说服 reader 这个经验实例为什么值得一篇论文。9-mode taxonomy 是 post-hoc 分类。Goodhart collapse 可从 ISR 数学定义直接推导。建议强调意料之外的发现（stochastic bifurcation, non-monotonic dose-response, cross-scale mode divergence）。\n\n**R2-N3** [critical] Abstract 数据过载——30 秒内无法消化核心贡献\n- Abstract 含 15+ 数字/统计量。实验报告风格，不是故事。建议保留 3-4 个关键数字。\n\n### Should-Fix 问题\n\n**R2-W1** Introduction 叙事碎片化（5 个 \\paragraph{} 子标题）\n**R2-W2** §4.3 β 值呈现顺序混乱（不是升序）\n**R2-W3** 实验范围窄：单一模型族 + 单一数据集\n**R2-W4** 1.7B 跨尺度实验太薄（single seed）\n**R2-W5** ISR 名称本身具有误导性（\"Reward\" 暗示应被用作 reward）\n**R2-W6** LOO 缩写未在首次使用时定义\n**R2-W7** Table 1 caption 过长\n**R2-W8** Hacking taxonomy 的分类标准不够 principled\n\n### 引用建议\n当前 37 条引用偏少。可能缺失：Amodei et al. 2016 (Concrete Problems), Christiano et al. 2017 (RLHF), DeepSeek-R1 2025, Geirhos et al. 2020 (shortcut learning), AlphaProof/LEGO-Prover。\n\n### 主要优势\n1. 实验设计严谨（多 seed、CMH、matched controls）\n2. 透明度高\n3. Cross-validation 思维\n4. Cautionary value\n5. Hacking taxonomy 有操作价值\n\n---\n\n请对每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，附上你的理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分\nOverall: 3.0 (Findings), Soundness 4/5, Excitement 2/5, Reproducibility 4/5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] ISR 核心指标命名不一致\n- Abstract 将 ISR 定义为 \"Irreducible Solver Rate\"，Introduction/Method 定义为 \"Intensional Structural Reward\"。核心概念的名称冲突。\n\n**R2-N2** [critical] 新颖性 framing 不足——论文核心发现是 Goodhart's Law 的已知推论\n- \"Diagnostic becomes optimization target\" 是 Goodhart's Law 的定义。论文没有说服 reader 这个经验实例为什么值得一篇论文。9-mode taxonomy 是 post-hoc 分类。Goodhart collapse 可从 ISR 数学定义直接推导。建议强调意料之外的发现（stochastic bifurcation, non-monotonic dose-response, cross-scale mode divergence）。\n\n**R2-N3** [critical] Abstract 数据过载——30 秒内无法消化核心贡献\n- Abstract 含 15+ 数字/统计量。实验报告风格，不是故事。建议保留 3-4 个关键数字。\n\n### Should-Fix 问题\n\n**R2-W1** Introduction 叙事碎片化（5 个 \\paragraph{} 子标题）\n**R2-W2** §4.3 β 值呈现顺序混乱（不是升序）\n**R2-W3** 实验范围窄：单一模型族 + 单一数据集\n**R2-W4** 1.7B 跨尺度实验太薄（single seed）\n**R2-W5** ISR 名称本身具有误导性（\"Reward\" 暗示应被用作 reward）\n**R2-W6** LOO 缩写未在首次使用时定义\n**R2-W7** Table 1 caption 过长\n**R2-W8** Hacking taxonomy 的分类标准不够 principled\n\n### 引用建议\n当前 37 条引用偏少。可能缺失：Amodei et al. 2016 (Concrete Problems), Christiano et al. 2017 (RLHF), DeepSeek-R1 2025, Geirhos et al. 2020 (shortcut learning), AlphaProof/LEGO-Prover。\n\n### 主要优势\n1. 实验设计严谨（多 seed、CMH、matched controls）\n2. 透明度高\n3. Cross-validation 思维\n4. Cautionary value\n5. Hacking taxonomy 有操作价值\n\n---\n\n请对每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，附上你的理由。"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-17T16:23:44.114976+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1358
}
```

</details>

---


### Assistant

_source line 506 · 2026-05-17T16:23:47.518943+00:00_

交叉分享任务已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 507 · 2026-05-17T16:23:50.064839+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

核心发现：

**Must-Fix (3 项)**:
1. ISR 命名不一致：Abstract 称 "Irreducible Solver Rate"，Introduction/Method 称 "Intensional Structural Reward"
2. 新颖性 framing 不足——核心发现是 Goodhart's Law 的直接推论，需强化经验贡献的意外性
3. Abstract 数据过载（~15 个数字），30 秒内无法提取核心 message

**Should-Fix (8 项)**:
- Introduction 5 个 \paragraph{} 导致叙事碎片化
- §4.3 β 值呈现顺序混乱（0.1→0.05→0.2→0.3）
- 实验范围窄（单模型族 Qwen3 + 单数据集 FOLIO）
- 1.7B 实验仅 single seed 但做了 scale-dependent claim
- ISR 名称含 "Reward" 但结论是不应用作 reward
- LOO 缩写未正式定义
- Table 1 caption 过长
- Hacking taxonomy 缺乏 principled 分类标准

**总评**: 3.0 (Findings)——实验严谨透明，但 excitement 有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 508 · 2026-05-17T16:23:56.218897+00:00_

交叉分享已发送给两位 Reviewer，等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 509 · 2026-05-17T16:25:46.993095+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1

---

## Must-Fix 逐条回应

**[AGREE] R1-N1: Exec-only baseline 在 Table 1 中的不对称比较**
同意。Table 1 exec-only 行仅为 s42 单 seed（caption 脚注 $^\dagger$ 标注），而 ISR/Random 行为 5-seed pooled，这是不对等的。虽然论文在脚注中披露了这一点并指向 Appendix Table 6（exec-only 3-seed 1000-step），但主表是审稿人第一眼看到的比较基准。建议在 Table 1 中增加 exec-only 3-seed 1000-step 行（数据已有：PR=97±2%, N-H≈2%），使主表内比较对称。

补充：Table 1 caption 本身已经过长（我在 R2-W7 中提到约 120 words），增加新行的同时应精简 caption。

**[AGREE] R1-N2: OR=3.48 vs OR=0.61 方向反转的 framing 问题**
同意这是 framing 问题。论文将两个分析描述为 "bound the true effect from above and below"（experiments.tex:96），但这个说法在方法论上不够准确：5-seed 分析缺少 s43/s44 的 H8 审计（appendix.tex:249-251 明确说 checkpoints 已删除），而 3-seed 分析是唯一有完整审计的比较。

不过我注意到两点 nuance：
1. CMH OR=3.37（p<10⁻⁹）是分层检验，已处理 within-seed clustering，且方向与 5-seed Fisher 一致——因此正面效应并非纯粹 artifact。
2. 3-seed 分析的 OR=0.61 是 n.s.（p=0.182），其方向反转也不显著。

建议：将 3-seed corrected OR=0.61 提升为 primary sensitivity analysis（而非 "lower bound"），明确表述 "the genuine-rate advantage is not robust to H8 correction and checkpoint completeness"。当前 framing 给 reader 的印象是正面效应是 baseline、0.61 是保守例外，但实际上两个分析各有 limitation。

**[AGREE] R1-N3: s43/s44 checkpoint 丢失**
完全同意。Checkpoint 丢失是不可逆的数据完整性问题。论文在 appendix.tex:249-251 坦诚披露了这一点（"checkpoints were deleted before audit and cannot be recovered"），但在主表（Table 1）中 N-H=23% 仍以点估计呈现。R1 建议的区间 [6%, 23%] 是合理的表示方式。

我补充一个观察：这个问题对论文 narrative 的实际影响有限，因为论文的核心结论是 ISR 作为 reward 最终导致 Goodhart collapse（所有 seed 在 extended training 后收敛到 ≤2% genuine），而非 500-step snapshot 有 23% 的 genuine。论文在 experiments.tex:98-100 和 §5 conclusion 中已正确将 500-step 结果定位为 "transient"。但 Table 1 的呈现方式仍需修正。

**[AGREE] R1-N4: SFT vs RL 的 PR confound**
同意 PR confound 是此比较的核心弱点。SFT PR=13%（n=39）vs exec-only PR=93%（n=93）的巨大差距意味着我们无法排除 "SFT 在高 PR 时也会 hack" 的可能性。

论文提供了两层 mitigation，但都不够充分：
1. 100-step checkpoint（PR=32%, hacking=31.2%，appendix.tex:670-674）：PR 仍然是 SFT 的 2.5 倍，且只有 n=32。
2. 机制论证（SFT 无 exploration-exploitation dynamics，experiments.tex:39）：这是合理的 reasoning，但不是 empirical evidence。

C1 中 "localizing the failure to RL"（introduction.tex:22）作为 claim 过强。建议弱化为 "consistent with RL-specific failure" 或提供 PR-matched 的 RL early checkpoint 数据。

不过我对 R1 评分有异议：R1 给 Soundness 2.5/5，我认为这低估了论文在其他方面的实验严谨度。SFT 比较是一个 confound，但论文的核心贡献（ISR collapse diagnostic, Goodhart at all doses, taxonomy）不依赖于 SFT 比较。

**[REBUT] R1-N5: 统计分析层级倒置——Pooled Fisher 不应作为 primary**
部分反驳。R1 的 clustering concern 在方法论上正确，但论文的实际呈现比 R1 描述的更合理：

1. **正文（experiments.tex:94）已将 CMH 作为 primary**：原文说 "Cochran--Mantel--Haenszel tests stratified by seed **confirm** ISR produces more genuine proofs"（第一个出现的统计检验），然后才提 Fisher 作为 "consistent but does not account for within-seed dependence"。CMH 不是附属分析，是正文叙事中的首要检验。

2. **CMH 和 Fisher 的结论方向一致**：CMH OR=3.37 (p<10⁻⁹) vs Fisher OR=3.48 (p<10⁻⁸)，差异微小。Clustering 确实存在，但在这个 case 中没有改变结论。

3. **Seed-level permutation p=0.26/0.28 的解读**：R1 说这与 Fisher 的 "巨大差距说明 clustering 严重"。这个推理不完全正确——p=0.26 primarily 反映的是 n=5 的严重 power limitation（论文在 limitations.tex:7 明确说 minimum achievable p=0.008 at n=5），而非 clustering inflation。如果有 20 seeds，permutation test 可能也会显著。

R1 的建议（CMH 作为 primary）本身没有问题，但论文已经实质上在正文中这么做了。真正需要修的是 Appendix Table 3 (bootstrap-ci) 中 Fisher 作为第一行的排列顺序——这确实给人 Fisher=primary 的错觉。

---

## Should-Fix 逐条回应

**[AGREE] R1-W1: 方法贡献偏薄**
同意。Algorithm 1 是 6 行伪代码实现标准 LOO ablation。论文自己在 method.tex:26 和 related_work.tex:23 承认 "our contribution lies in the application and empirical findings, not in the perturbation primitive itself"。这是诚实的，但也意味着 method 贡献确实薄。我在 R2-N2 中从 novelty 角度提出了类似 concern。

**[AGREE] R1-W2: Dose-response claim 基于 4 个 β 值、不均匀 seed 数**
同意。β=0.05/0.2 各 3 seeds，β=0.1 有 5 seeds，β=0.3 有 3 seeds。Non-monotonic dose-response（experiments.tex:122-124）是一个有趣的观察，但 4 个数据点 + 不均匀 power 不足以支撑 dose-response function 的 claim。"non-monotonic pattern" 措辞可以保留，但不应暗示这是一个 robust 的功能关系。

**[AGREE] R1-W3: 1.7B cross-scale 仅单 seed**
同意，与我的 R2-W4 一致。单 seed 无法支撑 "different capacities converge to different Goodhart basins" 的一般性 claim。

**[AGREE] R1-W4: "at all tested doses" 缺 β=0.05/0.3 trajectory 数据**
同意。"At all tested doses"（introduction.tex:26）claim 的证据链：
- β=0.1：有 1000-step trajectory（s42, s45）——最完整
- β=0.2：500-step 已 100% H7，但无 trajectory 确认是否有更早的 genuine window
- β=0.05：500-step 已 87-100% H7，同上
- β=0.3：500-step 有 3 seeds 但无 trajectory

500-step snapshot 显示 collapse 是合理证据，但与 β=0.1 的 trajectory analysis 标准不一致。要么补充 trajectory 数据，要么将 claim 弱化为 "collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1"。

**[AGREE] R1-W5: 100 eval examples 对 per-seed claims 效力不足**
同意。每个 seed 的 proved samples 在 42-94 之间（Table 4, appendix.tex:127-147），per-seed hacking rate 的 95% CI 很宽。例如 ISR s42 N-H=17.3%（n=81）的 Wilson CI 约 [10%, 27%]。论文依赖 pooled analysis 来获取 power，但 per-seed claims（如 "s45 achieves 55% genuine"）的精度有限。这是实验规模限制，而非设计缺陷。

**[AGREE] R1-W6: Seed 43 exec-only 使用 sampling (T=0.7)**
同意。appendix.tex:55-56 披露了此差异，但正文和 Table 1 中无标注（Table 1 exec-only 行是 s42 非 s43，所以主表本身不受影响，但 Appendix Table 5 的 s43 行应有更显著的标注）。

---

## 与 R1 评分的分歧

R1 给 Overall 3.5（Borderline Conference），我给 3.0（Findings）。差异来源：

1. **Excitement**: R1 给 3.5，我给 2.0。R1 可能更看重 cautionary value 和 taxonomy 的实用性。我认为核心 insight（Goodhart's Law applied to diagnostics）理论上可预测，empirical contribution 的 increment 有限。

2. **Soundness**: R1 给 2.5，我给 4.0。R1 聚焦于统计分析层级和 PR confound，我认为这些是 framing 问题而非根本性缺陷——论文的 multi-seed 设计、matched random controls、CMH stratification 在该领域是 above-average 的实验标准。

综合看，R1 和我对论文的主要 weakness 判断一致（novelty limited, narrow scope, some statistical issues），但权重不同。我认为 Findings 是当前稿件的合适定位。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 510 · 2026-05-17T16:25:52.474294+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 511 · 2026-05-17T16:25:58.836350+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- R1 的 5 个 Must-Fix 中我 **AGREE 4 个**（N1 表格不对称、N2 OR 反转 framing、N3 checkpoint 丢失、N4 SFT PR confound），**部分 REBUT 1 个**（N5：论文正文实际上已将 CMH 作为 primary，clustering concern 方法论正确但实际影响小，seed-level permutation p=0.26 主要反映 n=5 power 不足而非 clustering inflation）。
- R1 的 6 个 Should-Fix 全部 AGREE。
- 评分分歧：R1 给 3.5/Soundness 2.5/Excitement 3.5，我给 3.0/Soundness 4.0/Excitement 2.0。我们对 soundness 和 excitement 的权重相反，但都认为论文在 Findings-to-Borderline Conference 区间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 512 · 2026-05-17T16:26:03.838099+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 48

## Round 48

8 recorded events


### User

_source line 513 · 2026-05-17T16:26:29.255409+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: ISR 核心指标命名不一致**
确认这是一个明确的写作 bug。Abstract (L4) 将 ISR 定义为 "Irreducible Solver Rate"，而 Introduction (§1 ¶2) 和 Method (§3.2) 均定义为 "Intensional Structural Reward"。同一缩写在同一篇论文中展开为两个不同的全名，这不应该出现。必须统一。

**[AGREE with nuance] R2-N2: 新颖性 framing 不足**
同意核心论点：**"当诊断变为优化目标时会被 game"本身就是 Goodhart's Law 的定义**，论文如果只是说 "我们观察到了 Goodhart 效应"，贡献不够。

但我认为 R2 低估了部分 empirical findings 的非平凡性：
- **Stochastic bifurcation**（§4.2: 5 seeds 中 2/5 在 ~150 步内 collapse，3/5 维持 transient window）不能从 ISR 数学定义直接推导。ISR 定义预测 H7 是全局最优 exploit，但不能预测 collapse 的时间是 stochastic 的。
- **H7b triple gaming**（Appendix D.3: 模型同时 game execution reward、ISR metric 和 H7 classifier，通过 vacuous quantifier wrapping）是意料之外的发现。
- **Cross-logic mode divergence**（§4.3: Prolog 3 seeds × 3 distinct mechanisms，包括 query-as-fact gaming 逃逸 classifier）也有经验价值。
- **OR 方向反转**（§4.2: 5-seed OR=3.48 vs 3-seed corrected OR=0.61）是一个重要的方法论警示。

**建议的修改方向与 R2 一致**：论文应将 framing 从 "我们提出 STA 方法并发现 Goodhart 效应" 转为 "Goodhart collapse 是可预测的，但以下经验现象是不可预测的：[stochastic bifurcation timing, non-monotonic dose-response, triple gaming, cross-scale mode divergence]"。这也与我自己的 W1（方法贡献偏薄）一致——论文应更诚实地 position 为 empirical study。

**[AGREE] R2-N3: Abstract 数据过载**
确认 Abstract 包含 15+ 数字/统计量。逐句统计：
- L1: "97±2%", "three seeds"
- L3: "99.5%"
- L4: "92%"
- L5: "β∈{0.05, 0.1, 0.2, 0.3}"（4 个值）
- L7: "3/3 seeds", "0%", "1.7B"
- L8: "6 conditions", "2 logic types", "2 model scales", "5 seeds", "9 hacking modes"

这是实验报告风格，不是故事。审稿人在 30 秒内无法提取核心价值判断。R2 的建议（保留 3-4 个关键数字）合理。

---

### Should-Fix 问题

**[REBUT] R2-W1: Introduction 叙事碎片化（5 个 \paragraph{} 子标题）**
不完全同意。§1 的 5 个 \paragraph{} 结构（execution-only blind spot → component necessity testing → ISR as diagnostic → ISR as reward → contributions）确实不是 EMNLP 的标准叙事格式，但它服务于一个清晰的逻辑链。论文需要在 Introduction 中交代两个完整的 story arc（ISR-as-diagnostic + ISR-as-reward），单段落结构可能更混乱。**问题不在于子标题本身，而在于每个 \paragraph{} 内部数据过密**（尤其是 ¶4 "ISR as reward: Goodhart collapse at all tested doses"，单段落包含 4 个 β 值、5 seeds bifurcation、2 个 1000-step trajectory、OR 值）。建议保留 \paragraph{} 结构但精简数据。

**[AGREE] R2-W2: §4.3 β 值呈现顺序混乱**
确认 §4.2 的 β 呈现顺序为 0.1 → 0.05 → 0.2 → 0.3（不是升序）。领先 β=0.1 有叙事理由（最丰富的案例，stochastic bifurcation），但 dose-response 小节（§4.2 末尾 "Non-monotonic dose-response"）回顾所有 4 个 β 时，读者必须前后翻找。升序呈现 + 最后做 cross-dose synthesis 会更清晰。

**[REBUT with partial agreement] R2-W3: 实验范围窄（单一模型族 + 单一数据集）**
部分同意，但 R2 的 framing 忽略了论文已覆盖的维度。论文测试了：
- 2 个逻辑类型（FOL/Prover9 + Prolog/SWI-Prolog，§4.3）
- 2 个模型规模（4B + 1.7B，§4.4）
- 6 reward conditions（exec-only, ISR×4 doses, random×2 doses, SFT）
- 5 seeds（primary），3 seeds（sensitivity）

**真正的窄处**是 (1) 单一数据集（FOLIO）和 (2) 单一模型族（Qwen3）。但 FOLIO 是唯一同时提供 FOL 和 Prolog 注释的公开 NLI benchmark（§2 Related Work），数据集选择有合理约束。模型单一性是更实质的限制，但 Limitations §6 已明确承认。这是 should-note，不是 must-fix。

**[AGREE] R2-W4: 1.7B 跨尺度实验太薄（single seed）**
与我自己的 W3 完全一致。补充一点：§4.4 主文写 "No safe scale was observed"，但 n=1 seed 不足以支撑 "no safe X" 的存在性声明。

**[AGREE with caveat] R2-W5: ISR 名称本身具有误导性**
在 R2-N1 已确认名称不一致的背景下，这个问题更值得关注。如果统一为 "Intensional Structural Reward"，确实会暗示它应被用作 reward，而论文的核心结论恰恰是它不应被如此使用。但如果统一为 Abstract 的 "Irreducible Solver Rate"，则名称更中性，与 diagnostic 定位一致。**建议：统一为 "Irreducible Solver Rate" 或重新命名为不含 "Reward" 的名称。** 不过这是一个命名 preference 问题，不影响技术正确性。

**[AGREE] R2-W6: LOO 缩写未在首次使用时定义**
确认。LOO 首次出现在 Introduction §1 ¶2 (L16)："LOO ablation itself is standard"，之前未展开为 "Leave-One-Out (LOO)"。Abstract (L3) 使用全称 "leave-one-out" 但未引入缩写。简单的格式修复。

**[AGREE] R2-W7: Table 1 caption 过长**
与我自己的小问题观察一致。Table 1 caption 包含 6 个脚注标记（†, ‡, ★, 加上条件说明），信息密度过高。

**[REBUT] R2-W8: Hacking taxonomy 的分类标准不够 principled**
不完全同意 R2 的严重性判断。Taxonomy 确实混合了两种检测方法（text-match for H1/H7 vs functional LOO analysis for others），但这不是分类标准的问题——分类标准是统一的：**基于 structural degeneration mechanism**（conclusion embedding vs tautological duplication vs premise-subset gaming vs contradiction injection 等）。检测方法（text-match vs functional analysis）是实施细节，不是分类轴。

更重要的是，论文已经展示了 cross-validation 的价值（Prolog s44 query-as-fact gaming 逃逸 strict classifier，§4.3 L132），这恰恰说明 taxonomy 不是 post-hoc 的——它被 functional analysis 挑战和修正过。

**但 R2 有一个有效的隐含观点**：Table 2 中部分 mode 只出现在特定 seed/condition 组合中（如 H9 仅 1.7B random、query-as-fact 仅 Prolog s44），读者难以判断这些是 systematic mode 还是 one-off observation。建议在 taxonomy 中标注每种 mode 的 evidence strength（多 seed/condition 观察 vs 单点观察）。

---

### 引用建议回应

**R2 建议的 5 篇引用**：
1. **Amodei et al. 2016 (Concrete Problems in AI Safety)** — 相关。论文讨论 reward hacking 和 scalable oversight implications (Ethics §7)，引用此文有助于定位贡献。**建议增加。**
2. **Christiano et al. 2017 (RLHF)** — 边际相关。论文不使用 RLHF，而是 GRPO + solver feedback。Related Work §2 已引用 PRMs 和 reward shaping 文献。可引可不引。
3. **DeepSeek-R1 2025** — 相关但需要小心。论文的 baseline 是 Qwen3，不是 DeepSeek-R1。如果引用，应在 Related Work 中讨论 reasoning models 的更广泛趋势。**建议在 Related Work ¶1 增加。**
4. **Geirhos et al. 2020 (Shortcut Learning)** — **强烈建议增加。** 论文的核心发现（模型学习 shortcut 而非 genuine reasoning）与 shortcut learning 文献直接对话。当前 Related Work 缺少这个连接。
5. **AlphaProof / LEGO-Prover** — AlphaProof 相关（neurosymbolic proof generation at scale）；LEGO-Prover 与 FOL/Prolog formalization 更直接相关。**建议增加至少一个。**

**引用总量**：当前 37 条对 EMNLP 偏少但不严重。增加 3-5 条高相关引用即可。

---

### 总结

R2 的 Must-Fix 问题中，N1（命名不一致）和 N3（Abstract 过载）是确实的写作 bug；N2（新颖性 framing）有道理但我认为 R2 略微低估了 empirical findings 的非平凡性。Should-Fix 中 W2/W4/W6/W7 是简单修复；W1 可辩护；W3 部分有效；W8 我不完全同意但有隐含的有效观点。

R2 与我的审查结论有一个重要分歧：**R2 给 Soundness 4/5，我给 2.5/5**。R2 似乎接受了论文的统计框架（"实验设计严谨"），而我的 N1-N5 指出了比较框架的多处不对称和统计层级倒置。如果我的 N2（OR 反转 framing）和 N5（Fisher vs CMH 层级）成立，Soundness 4/5 过高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-17T16:27:24.578389+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-17T16:27:24.679193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-17T16:32:31.668330+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4-5 carry-over (in_progress) =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W4 再次确认。§4.5 'No safe scale was observed' 仍为 n=1 seed 的存在性声明。R1 交叉同意 R2-W4。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 新增段落声明 1-seed 限制\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"Abstract/Intro 'transfers'→'preliminarily observed at'\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"§4.5 'No safe scale was observed' 改为 'No safe scale was observed in this single-seed comparison'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N1\"\n  summary: \"正文超页限制 (~8.5 页 vs ACL long paper 8 页)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。~10.5 页超出约 2.5 页。\"\n    - round: 5\n      reviewers: [2]\n      note: \"已大幅压缩但仍超约 0.5 页。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未被 Reviewer 提及。Director PDF 审查确认正文 §1-§5 在第 8 页内结束，§6 Limitations 从第 9 页开始。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 5\n      action: \"§5 删 1-2 句与 §4 重复内容\"\n      assigned_to: \"paper_agent\"\n      status: done\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds/doses\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W4: β=0.3/0.05 仅 500-step snapshot，论文自身方法论认为 snapshot 不足，但对自己的 claims 使用了 snapshot。R2 [AGREE]。\"\n  action_items:\n    - round: 5\n      action: \"软化 'at all tested doses' 措辞\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"弱化为 'collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"统计层级倒置; OR 反转正文一句带过。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N2: 3-seed corrected 是更可信估计（完整审计），应为 primary。R2 [AGREE]: 'genuine-rate advantage is not robust to H8 correction and checkpoint completeness'。R2 补充: CMH OR=3.37 (p<10⁻⁹) 方向与 5-seed Fisher 一致，正面效应非纯粹 artifact，但 framing 不诚实。\"\n  action_items:\n    - round: 5\n      action: \"CMH 作为 primary test 移入正文; Abstract 删除 uncorrected OR\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"(a) 3-seed corrected OR=0.61 提升为 primary sensitivity; (b) 明确 'genuine-rate advantage is not robust to H8 correction'; (c) Abstract/Intro 弱化 'initially yields more genuine' 措辞\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"Pooled Fisher test 忽略 seed-level clustering\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N5 再次提出。R2 [REBUT]: 正文 experiments.tex:94 已将 CMH 作为 primary (first mentioned test)，Fisher 作为 'consistent but does not account for within-seed dependence'。Seed-level permutation p=0.26 主要反映 n=5 power 不足而非 clustering inflation。Director 裁决: R2 的 rebut 有力——正文叙事中 CMH 确实是 primary。降级为 warning。真正需修的是 Appendix Table 4 中 Fisher 排在第一行的视觉层级。\"\n  action_items:\n    - round: 5\n      action: \"正文统计框架重组：CMH primary\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Appendix Table 4 重排: CMH 置于 Fisher 之前; 正文中 permutation test 的 power analysis 更显著呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解释原因。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W6: s43 数据仍用于主文 §4.1 cross-seed claims。R2 [AGREE]: 正文 Table 1 不受影响(exec-only 行是 s42)，但 Appendix Table 8 的 s43 行标注不够显著。\"\n  action_items:\n    - round: 6\n      action: \"Appendix Table 8 s43 行增加显著 eval 差异标注\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"5-seed pooled N-H=23% 为未校正上限。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N3: 建议报告区间 [6%, 23%]。R2 [AGREE]: 对 narrative 实际影响有限(核心结论是 extended training 后 collapse)，但 Table 1 呈现方式需修正。\"\n  action_items:\n    - round: 5\n      action: \"正文明确标注 23% 为 uncorrected upper bound\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"Table 1 ISR β=0.1 N-H 列报告为区间或标注 'upper bound'; Limitations 明确列出 checkpoint 丢失的具体影响\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W5: per-seed proved n=18-94，百分比信息量低。R2 [AGREE]: 实验规模限制而非设计缺陷，建议小 n seed 报告 CI。\"\n  action_items:\n    - round: 6\n      action: \"对 n<30 的 per-seed 结果报告 Wilson CI 而非仅点估计\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 升级为 critical。R1 [REBUT]: 已正确定位为 empirical contribution。Director 降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-N2 再次提出。两位 reviewer 共识: 方法贡献薄，应更明确 position 为 empirical study。R1 交叉同意 R2-N2 但认为 R2 低估了 stochastic bifurcation、H7b triple gaming 等经验发现的非平凡性。\"\n  action_items:\n    - round: 6\n      action: \"Introduction 中更明确 position 为 empirical study; 强调理论无法预测的经验现象\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据，与主文 5-seed 冲突\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"s45/s46 per-seed 数据从未在任何表格中呈现。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。Director 确认 Appendix Table 5 现含 5-seed per-seed data (s42-s46)。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 5\n      action: \"Appendix 补充完整 5-seed per-seed table\"\n      assigned_to: \"paper_agent\"\n      status: done\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N1 再次提出。R2 [AGREE]: 建议 Table 1 增加 exec-only 3-seed 1000-step 行(数据已有: PR=97±2%, N-H≈2%)。\"\n  action_items:\n    - round: 5\n      action: \"Table 1 保持 s42 单 seed + 加强†脚注\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Table 1 增加 exec-only 3-seed 1000-step 行 (PR=97±2%, N-H≈2%); 精简 caption\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R1 Excitement=3.5 部分不同意。降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N2 再次提出(升级为 critical)。R1 交叉回应 [AGREE with nuance]: 核心论点正确，但 stochastic bifurcation、H7b triple gaming、cross-logic mode divergence、OR 方向反转是理论无法预测的。Director 裁决: 维持 warning——概念层面可预测但 empirical details 有增量，论文需更好地 frame 这些增量。\"\n  action_items:\n    - round: 6\n      action: \"Framing 从 'we discover Goodhart effects' 转为 'Goodhart collapse is predictable, but these phenomena are not: [stochastic bifurcation, non-monotonic dose-response, triple gaming, cross-scale mode divergence]'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~15 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。与 v2-R2-W3 (已 resolved round 3) 部分复发。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N3 再次提出。R1 [AGREE]: 逐句确认 15+ 数字。'审稿人在 30 秒内无法提取核心价值判断'。建议保留 3-4 个关键数字。\"\n  action_items:\n    - round: 5\n      action: \"Abstract 删减到最多 3-4 个关键数字\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"Abstract 删减到 ≤4 个关键数字(ISR collapse 幅度、non-hacking rate 对比、dose-response 结论); 移除 β 列表、seed counts、condition counts\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 \\\\paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 \\\\paragraph{} 小标题切割连贯叙事。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [REBUT]: 结构服务于清晰的逻辑链(两个 story arc)，问题不在子标题本身而在每个 paragraph 内数据过密。Director 裁决: 分歧记录。两种修改方向均可接受: (a) 保留 paragraph 结构但精简数据; (b) 减少到 2-3 个 paragraph + 自然段过渡。\"\n  action_items:\n    - round: 6\n      action: \"二选一: (a) 保留 paragraph 但精简每段数据密度; (b) 减少到 2-3 个 paragraph\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Low-dose/Micro-dose/Medium-dose/High-dose 四段格式高度重复。\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W2: β 呈现顺序为 0.1→0.05→0.2→0.3(非升序)。R1 [AGREE]。\"\n  action_items:\n    - round: 6\n      action: \"按 β 升序呈现(0.05→0.1→0.2→0.3)，或开头解释当前顺序的叙事理由\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"多次引用 Manheim & Garrabrant (2019) 但从未指定 variant。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。Director 确认 related_work.tex:20 现已指定 'primarily regressional, with extremal elements'。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 中指定 regressional + extremal variant\"\n      assigned_to: \"paper_agent\"\n      status: done\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"H7 reward ≈1+0.75β vs genuine ≈1+0.258β，差距 ≈0.49β。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。Director 确认 experiments.tex:91 现已包含 reward landscape 分析 ('H7 tautologies receive expected reward 1+0.75β versus ~1+0.26β for genuine proofs, a gap of ~0.49β')。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 5\n      action: \"§4.3 加 reward landscape 分析\"\n      assigned_to: \"paper_agent\"\n      status: done\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W7: caption ~120 words + 6 脚注标记。R1 [AGREE]。建议条件说明移正文或 Appendix，caption 仅保留简要描述。\"\n  action_items:\n    - round: 6\n      action: \"Table 1 caption 压缩至 ≤60 words; 条件说明移正文\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"100-step RL (PR=32%) 部分缓解但不完全。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N4: C1 'localizing the failure to RL' 证据链有 PR confound。无法知道 SFT 在高 PR 时是否也会 hack。R2 [AGREE]: 100-step (PR=32%) 和机制论证仍不充分。但 R2 补充: SFT 比较是一个 confound，不影响论文核心贡献(ISR collapse diagnostic, Goodhart at all doses, taxonomy)。\"\n  action_items:\n    - round: 6\n      action: \"C1 弱化为 'consistent with RL-specific failure'; 正文承认 'whether SFT would hack at higher PR remains unknown'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Krakovna, Polu & Sutskever, Everitt。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Krakovna 2020, Polu & Sutskever 2020, Everitt 2021 现已在 references.bib 中。R2 新建议: Amodei et al. 2016, Geirhos et al. 2020 (shortcut learning), DeepSeek-R1 2025。R1 交叉同意 Amodei, Geirhos, DeepSeek-R1。当前 37 条引用对 EMNLP 偏少但不严重。\"\n  action_items:\n    - round: 6\n      action: \"增加 3 条高相关引用: Amodei et al. 2016 (Concrete Problems), Geirhos et al. 2020 (shortcut learning), DeepSeek-R1 2025\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 6 新 issues =====\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致: Abstract 'Irreducible Solver Rate' vs Method 'Intensional Structural Reward'\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 交叉 [AGREE]。同一缩写在同一篇论文中展开为两个不同全名，严重损害可信度。\"\n  action_items:\n    - round: 6\n      action: \"统一 ISR 全名。建议选择不含 'Reward' 的版本以避免与核心结论矛盾 (见 v6-R2-W5)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性——论文结论恰恰是不应用作 reward\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 交叉 [AGREE with caveat]: 如统一为 'Intensional Structural Reward' 会暗示应被用作 reward。建议统一为 'Irreducible Solver Rate' 或其他不含 'Reward' 的名称。\"\n  action_items:\n    - round: 6\n      action: \"与 v6-R2-N1 合并处理: 统一为不含 'Reward' 的名称\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 基于 4 个 β 值、不均匀 seed 数，统计上不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 提出，R2 [AGREE]。β=0.1 用 5 seeds 而 β=0.05/0.2/0.3 用 3 seeds。'Non-monotonic dose-response' claim 统计上无法支撑。\"\n  action_items:\n    - round: 6\n      action: \"弱化为 'the pattern across four tested doses suggests...' 而非 'non-monotonic dose-response'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 Goodhart Effects 的 β 值呈现顺序非升序 (0.1→0.05→0.2→0.3)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 [AGREE]。升序呈现 + 最后 cross-dose synthesis 会更清晰。或解释当前顺序的叙事理由。\"\n  action_items:\n    - round: 6\n      action: \"与 v5-R2-W4 合并: 按 β 升序呈现或解释当前顺序理由\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W6 提出，R1 [AGREE]。首次出现在 introduction.tex:16 'LOO ablation' 但未展开为 'Leave-One-Out (LOO)'。简单格式修复。\"\n  action_items:\n    - round: 6\n      action: \"introduction.tex:16 首次使用处改为 'leave-one-out (LOO) ablation'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled，部分 mode 为单点观察\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W8 提出。R1 [REBUT]: 分类标准是统一的(基于 structural degeneration mechanism)，taxonomy 被 functional analysis cross-validate 过(Prolog s44)。但 R1 承认部分 mode 仅单 seed/condition 观察。Director 裁决: 降级为 info，建议标注 evidence strength。\"\n  action_items:\n    - round: 6\n      action: \"Table 2/Appendix 中标注每种 mode 的 evidence strength (multi-seed vs single-point observation)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4-5 carry-over (in_progress) =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W4 再次确认。§4.5 'No safe scale was observed' 仍为 n=1 seed 的存在性声明。R1 交叉同意 R2-W4。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 新增段落声明 1-seed 限制\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"Abstract/Intro 'transfers'→'preliminarily observed at'\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"§4.5 'No safe scale was observed' 改为 'No safe scale was observed in this single-seed comparison'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N1\"\n  summary: \"正文超页限制 (~8.5 页 vs ACL long paper 8 页)\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"共识。~10.5 页超出约 2.5 页。\"\n    - round: 5\n      reviewers: [2]\n      note: \"已大幅压缩但仍超约 0.5 页。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未被 Reviewer 提及。Director PDF 审查确认正文 §1-§5 在第 8 页内结束，§6 Limitations 从第 9 页开始。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 5\n      action: \"§5 删 1-2 句与 §4 重复内容\"\n      assigned_to: \"paper_agent\"\n      status: done\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds/doses\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W4: β=0.3/0.05 仅 500-step snapshot，论文自身方法论认为 snapshot 不足，但对自己的 claims 使用了 snapshot。R2 [AGREE]。\"\n  action_items:\n    - round: 5\n      action: \"软化 'at all tested doses' 措辞\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"弱化为 'collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"统计层级倒置; OR 反转正文一句带过。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N2: 3-seed corrected 是更可信估计（完整审计），应为 primary。R2 [AGREE]: 'genuine-rate advantage is not robust to H8 correction and checkpoint completeness'。R2 补充: CMH OR=3.37 (p<10⁻⁹) 方向与 5-seed Fisher 一致，正面效应非纯粹 artifact，但 framing 不诚实。\"\n  action_items:\n    - round: 5\n      action: \"CMH 作为 primary test 移入正文; Abstract 删除 uncorrected OR\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"(a) 3-seed corrected OR=0.61 提升为 primary sensitivity; (b) 明确 'genuine-rate advantage is not robust to H8 correction'; (c) Abstract/Intro 弱化 'initially yields more genuine' 措辞\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"Pooled Fisher test 忽略 seed-level clustering\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N5 再次提出。R2 [REBUT]: 正文 experiments.tex:94 已将 CMH 作为 primary (first mentioned test)，Fisher 作为 'consistent but does not account for within-seed dependence'。Seed-level permutation p=0.26 主要反映 n=5 power 不足而非 clustering inflation。Director 裁决: R2 的 rebut 有力——正文叙事中 CMH 确实是 primary。降级为 warning。真正需修的是 Appendix Table 4 中 Fisher 排在第一行的视觉层级。\"\n  action_items:\n    - round: 5\n      action: \"正文统计框架重组：CMH primary\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Appendix Table 4 重排: CMH 置于 Fisher 之前; 正文中 permutation test 的 power analysis 更显著呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解释原因。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W6: s43 数据仍用于主文 §4.1 cross-seed claims。R2 [AGREE]: 正文 Table 1 不受影响(exec-only 行是 s42)，但 Appendix Table 8 的 s43 行标注不够显著。\"\n  action_items:\n    - round: 6\n      action: \"Appendix Table 8 s43 行增加显著 eval 差异标注\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"5-seed pooled N-H=23% 为未校正上限。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N3: 建议报告区间 [6%, 23%]。R2 [AGREE]: 对 narrative 实际影响有限(核心结论是 extended training 后 collapse)，但 Table 1 呈现方式需修正。\"\n  action_items:\n    - round: 5\n      action: \"正文明确标注 23% 为 uncorrected upper bound\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"Table 1 ISR β=0.1 N-H 列报告为区间或标注 'upper bound'; Limitations 明确列出 checkpoint 丢失的具体影响\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W5: per-seed proved n=18-94，百分比信息量低。R2 [AGREE]: 实验规模限制而非设计缺陷，建议小 n seed 报告 CI。\"\n  action_items:\n    - round: 6\n      action: \"对 n<30 的 per-seed 结果报告 Wilson CI 而非仅点估计\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 升级为 critical。R1 [REBUT]: 已正确定位为 empirical contribution。Director 降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-N2 再次提出。两位 reviewer 共识: 方法贡献薄，应更明确 position 为 empirical study。R1 交叉同意 R2-N2 但认为 R2 低估了 stochastic bifurcation、H7b triple gaming 等经验发现的非平凡性。\"\n  action_items:\n    - round: 6\n      action: \"Introduction 中更明确 position 为 empirical study; 强调理论无法预测的经验现象\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据，与主文 5-seed 冲突\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"s45/s46 per-seed 数据从未在任何表格中呈现。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。Director 确认 Appendix Table 5 现含 5-seed per-seed data (s42-s46)。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 5\n      action: \"Appendix 补充完整 5-seed per-seed table\"\n      assigned_to: \"paper_agent\"\n      status: done\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N1 再次提出。R2 [AGREE]: 建议 Table 1 增加 exec-only 3-seed 1000-step 行(数据已有: PR=97±2%, N-H≈2%)。\"\n  action_items:\n    - round: 5\n      action: \"Table 1 保持 s42 单 seed + 加强†脚注\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Table 1 增加 exec-only 3-seed 1000-step 行 (PR=97±2%, N-H≈2%); 精简 caption\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R1 Excitement=3.5 部分不同意。降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N2 再次提出(升级为 critical)。R1 交叉回应 [AGREE with nuance]: 核心论点正确，但 stochastic bifurcation、H7b triple gaming、cross-logic mode divergence、OR 方向反转是理论无法预测的。Director 裁决: 维持 warning——概念层面可预测但 empirical details 有增量，论文需更好地 frame 这些增量。\"\n  action_items:\n    - round: 6\n      action: \"Framing 从 'we discover Goodhart effects' 转为 'Goodhart collapse is predictable, but these phenomena are not: [stochastic bifurcation, non-monotonic dose-response, triple gaming, cross-scale mode divergence]'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~15 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。与 v2-R2-W3 (已 resolved round 3) 部分复发。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N3 再次提出。R1 [AGREE]: 逐句确认 15+ 数字。'审稿人在 30 秒内无法提取核心价值判断'。建议保留 3-4 个关键数字。\"\n  action_items:\n    - round: 5\n      action: \"Abstract 删减到最多 3-4 个关键数字\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 6\n      action: \"Abstract 删减到 ≤4 个关键数字(ISR collapse 幅度、non-hacking rate 对比、dose-response 结论); 移除 β 列表、seed counts、condition counts\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 \\\\paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 \\\\paragraph{} 小标题切割连贯叙事。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [REBUT]: 结构服务于清晰的逻辑链(两个 story arc)，问题不在子标题本身而在每个 paragraph 内数据过密。Director 裁决: 分歧记录。两种修改方向均可接受: (a) 保留 paragraph 结构但精简数据; (b) 减少到 2-3 个 paragraph + 自然段过渡。\"\n  action_items:\n    - round: 6\n      action: \"二选一: (a) 保留 paragraph 但精简每段数据密度; (b) 减少到 2-3 个 paragraph\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Low-dose/Micro-dose/Medium-dose/High-dose 四段格式高度重复。\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W2: β 呈现顺序为 0.1→0.05→0.2→0.3(非升序)。R1 [AGREE]。\"\n  action_items:\n    - round: 6\n      action: \"按 β 升序呈现(0.05→0.1→0.2→0.3)，或开头解释当前顺序的叙事理由\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"多次引用 Manheim & Garrabrant (2019) 但从未指定 variant。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。Director 确认 related_work.tex:20 现已指定 'primarily regressional, with extremal elements'。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 中指定 regressional + extremal variant\"\n      assigned_to: \"paper_agent\"\n      status: done\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"H7 reward ≈1+0.75β vs genuine ≈1+0.258β，差距 ≈0.49β。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。Director 确认 experiments.tex:91 现已包含 reward landscape 分析 ('H7 tautologies receive expected reward 1+0.75β versus ~1+0.26β for genuine proofs, a gap of ~0.49β')。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 5\n      action: \"§4.3 加 reward landscape 分析\"\n      assigned_to: \"paper_agent\"\n      status: done\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W7: caption ~120 words + 6 脚注标记。R1 [AGREE]。建议条件说明移正文或 Appendix，caption 仅保留简要描述。\"\n  action_items:\n    - round: 6\n      action: \"Table 1 caption 压缩至 ≤60 words; 条件说明移正文\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"100-step RL (PR=32%) 部分缓解但不完全。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N4: C1 'localizing the failure to RL' 证据链有 PR confound。无法知道 SFT 在高 PR 时是否也会 hack。R2 [AGREE]: 100-step (PR=32%) 和机制论证仍不充分。但 R2 补充: SFT 比较是一个 confound，不影响论文核心贡献(ISR collapse diagnostic, Goodhart at all doses, taxonomy)。\"\n  action_items:\n    - round: 6\n      action: \"C1 弱化为 'consistent with RL-specific failure'; 正文承认 'whether SFT would hack at higher PR remains unknown'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Krakovna, Polu & Sutskever, Everitt。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Krakovna 2020, Polu & Sutskever 2020, Everitt 2021 现已在 references.bib 中。R2 新建议: Amodei et al. 2016, Geirhos et al. 2020 (shortcut learning), DeepSeek-R1 2025。R1 交叉同意 Amodei, Geirhos, DeepSeek-R1。当前 37 条引用对 EMNLP 偏少但不严重。\"\n  action_items:\n    - round: 6\n      action: \"增加 3 条高相关引用: Amodei et al. 2016 (Concrete Problems), Geirhos et al. 2020 (shortcut learning), DeepSeek-R1 2025\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 6 新 issues =====\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致: Abstract 'Irreducible Solver Rate' vs Method 'Intensional Structural Reward'\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N1 提出，R1 交叉 [AGREE]。同一缩写在同一篇论文中展开为两个不同全名，严重损害可信度。\"\n  action_items:\n    - round: 6\n      action: \"统一 ISR 全名。建议选择不含 'Reward' 的版本以避免与核心结论矛盾 (见 v6-R2-W5)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性——论文结论恰恰是不应用作 reward\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W5 提出，R1 交叉 [AGREE with caveat]: 如统一为 'Intensional Structural Reward' 会暗示应被用作 reward。建议统一为 'Irreducible Solver Rate' 或其他不含 'Reward' 的名称。\"\n  action_items:\n    - round: 6\n      action: \"与 v6-R2-N1 合并处理: 统一为不含 'Reward' 的名称\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 基于 4 个 β 值、不均匀 seed 数，统计上不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 提出，R2 [AGREE]。β=0.1 用 5 seeds 而 β=0.05/0.2/0.3 用 3 seeds。'Non-monotonic dose-response' claim 统计上无法支撑。\"\n  action_items:\n    - round: 6\n      action: \"弱化为 'the pattern across four tested doses suggests...' 而非 'non-monotonic dose-response'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 Goodhart Effects 的 β 值呈现顺序非升序 (0.1→0.05→0.2→0.3)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W2 提出，R1 [AGREE]。升序呈现 + 最后 cross-dose synthesis 会更清晰。或解释当前顺序的叙事理由。\"\n  action_items:\n    - round: 6\n      action: \"与 v5-R2-W4 合并: 按 β 升序呈现或解释当前顺序理由\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W6 提出，R1 [AGREE]。首次出现在 introduction.tex:16 'LOO ablation' 但未展开为 'Leave-One-Out (LOO)'。简单格式修复。\"\n  action_items:\n    - round: 6\n      action: \"introduction.tex:16 首次使用处改为 'leave-one-out (LOO) ablation'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled，部分 mode 为单点观察\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W8 提出。R1 [REBUT]: 分类标准是统一的(基于 structural degeneration mechanism)，taxonomy 被 functional analysis cross-validate 过(Prolog s44)。但 R1 承认部分 mode 仅单 seed/condition 观察。Director 裁决: 降级为 info，建议标注 evidence strength。\"\n  action_items:\n    - round: 6\n      action: \"Table 2/Appendix 中标注每种 mode 的 evidence strength (multi-seed vs single-point observation)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-17T16:32:31.769796+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 27430}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-17T16:35:06.212376+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "report": "# 圆桌审稿报告 — Round 6\n\n**论文**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle, deadline 2026-05-25)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+写作质量+格式合规+完整性）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 neurosymbolic formalizer 的 solver 输入进行 leave-one-out 消融，生成 Intensional Structural Reward (ISR) 指标。ISR 作为诊断工具有效揭示了 execution-based evaluation 隐藏的结构崩溃（99.5% degradation），但作为训练信号时在所有 4 个测试剂量下触发 Goodhart collapse。论文覆盖 6 reward conditions、5 seeds、2 logic types、2 model scales，cataloging 了 9 种 hacking 模式。\n\n---\n\n## Strengths\n\n**S1. 实验覆盖面广且透明度高**\n多 seed（3-5 per condition）、matched random controls、CMH 分层检验、1000-step trajectory analysis、premise-count-matched comparison——该领域少见的统计严谨度。论文坦诚披露所有已知局限（ISR premise-count confound、OR 方向反转、checkpoint 丢失、eval 协议不一致），自我批评充分。[共识: R1+R2]\n\n**S2. 叙事核心有说服力**\n\"ISR: reliable as observer, unreliable as optimizer at any dose\" 是一个清晰、有警示价值的结论。对 neurosymbolic RL 社区有实际操作意义。[共识: R1+R2]\n\n**S3. Hacking taxonomy 有独立操作价值**\n9 种 hacking mode 的定义、示例和 ISR 交互分析对从业者有直接参考价值。Cross-validation 思维（text-match + functional LOO analysis）发现了 H7b obfuscated tautology 和 query-as-fact gaming，体现 careful empirical work。[共识: R1+R2]\n\n**S4. Control design 正确**\nSFT control（分离 RL-specific vs data exposure）、random control（分离 ISR-specific vs generic variance）、matched dose design 的实验逻辑清晰。[R1 优势 #5; R2 隐含同意]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] ISR 核心指标命名不一致** [v6-R2-N1]\nAbstract 将 ISR 定义为 \"Irreducible Solver Rate\" (abstract.tex:3)，Introduction/Method 定义为 \"Intensional Structural Reward\" (method.tex:44)。核心概念的名称冲突是严重的写作错误，损害可信度。此外，\"Reward\" 一词暗示应被用作 reward，与论文核心结论矛盾 (v6-R2-W5)。\n- **建议**: 统一为不含 \"Reward\" 的名称（如 \"Irreducible Solver Rate\"）。\n- **共识**: R1 [AGREE] + R2 [提出]\n\n**MF2. [critical] Abstract 数据过载，30 秒内无法消化核心贡献** [v5-R2-W1, 复发]\nAbstract (~220 words) 包含 15+ 数字/统计量（97±2%, 99.5%, 92%, β∈{0.05,0.1,0.2,0.3}, 3/3 seeds, 0%, 6 conditions, 2 logic types, 2 model scales, 5 seeds, 9 hacking modes）。读感像压缩的 results table，核心 insight 被数字淹没。此问题在 Round 3 修复后（重写为 ~170 words）再次膨胀。\n- **建议**: 保留 ≤4 个关键数字，移除 β 列表、seed counts、condition counts。\n- **共识**: R1 [AGREE] + R2 [提出]\n\n**MF3. [critical] Table 1 比较框架不对称** [v5-R1-N3, 持续存在]\nTable 1 exec-only 行为单 seed (s42)、500-step，而 ISR/Random 为 5-seed pooled。3-seed 1000-step exec-only 数据（PR=97±2%, N-H≈2%）在附录但不在主表。主表是审稿人第一眼看到的比较基准，不对称的比较框架损害所有下游 claim 的可信度。\n- **建议**: Table 1 增加 exec-only 3-seed 1000-step 行。\n- **共识**: R1 [提出] + R2 [AGREE]\n\n**MF4. [critical] OR=3.48 vs OR=0.61 方向反转的 framing 不够诚实** [v4-R12-N3, 持续存在]\n5-seed uncorrected OR=3.48 基于包含 2 个 checkpoint 已删除 seed 的不完整数据，3-seed H8+FN-corrected OR=0.61 是唯一有完整审计的比较。论文将二者 frame 为 \"bound the true effect from above and below\"，但应将 corrected 分析作为 primary sensitivity，明确 \"genuine-rate advantage is not robust to H8 correction\"。CMH OR=3.37 (p<10⁻⁹) 方向一致，说明正面效应非纯粹 artifact，但 framing 仍需修正。\n- **建议**: (a) 3-seed corrected 提升为 primary sensitivity; (b) Abstract/Intro 弱化 \"initially yields more genuine\" 措辞; (c) 正文讨论 \"transient benefit 是否真实存在的不确定性\"。\n- **共识**: R1 [提出] + R2 [AGREE with nuance]\n\n**MF5. [critical] SFT vs RL 比较中 PR 严重混淆** [v5-R12-SFT-PR, 持续存在]\nSFT PR=13% (n=39) vs RL PR=93%+。C1 \"localizing the failure to RL\" 的证据链有根本性 PR confound：无法知道 SFT 在高 PR 时是否也会 hack。100-step checkpoint (PR=32%, hacking=31.2%) 部分缓解但 PR 仍为 SFT 的 2.5 倍。机制论证（SFT 无 exploration-exploitation dynamics）是合理的 reasoning 但非 empirical evidence。\n- **建议**: C1 弱化为 \"consistent with RL-specific failure\"；正文承认 \"whether SFT would hack at higher PR remains unknown\"。\n- **注意**: R2 补充——SFT 比较是一个 confound 但不影响论文核心贡献（ISR collapse diagnostic, Goodhart at all doses, taxonomy）。\n- **共识**: R1 [提出] + R2 [AGREE]\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] 新颖性 framing 不足** [v5-R2-N3 + v4-R2-W9, 持续存在]\n\"Diagnostic becomes optimization target\" 是 Goodhart's Law 的定义，不是新发现。LOO ablation 是标准方法。论文需说服 reader 为什么这个经验实例值得一篇论文。\n- **Director 裁决**: R2 正确指出概念层面可预测，但 R1 正确指出 stochastic bifurcation timing、H7b triple gaming、cross-logic mode divergence、OR 方向反转是理论无法预测的经验现象。论文应将 framing 从 \"we discover Goodhart effects\" 转为 \"Goodhart collapse is predictable, but these specific phenomena are not\"。\n- **分歧记录**: R1 Excitement=3.5, R2 Excitement=2.0\n\n**SF2. [warning] 1.7B cross-scale claims 仅单 seed** [v3-R12-NI-1, 持续存在]\n4B scale 下 3 seeds 产生 3 种截然不同的 hacking mode，说明单 seed 几乎不具备代表性。§4.5 \"No safe scale was observed\" 是 n=1 的存在性声明。\n- **建议**: 弱化为 \"No safe scale was observed in this single-seed comparison\"。\n- **共识**: R1+R2\n\n**SF3. [warning] \"At all tested doses\" claim 缺 β=0.3/0.05 trajectory 数据** [v4-R12-N2, 持续存在]\n1000-step trajectory 仅对 β=0.1 两个 seed 进行。β=0.3 和 β=0.05 仅 500-step snapshot。论文自身方法论认为 snapshot 不足以判断 long-run 行为，但对自己的 claims 使用了 snapshot。\n- **建议**: 弱化为 \"collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1\"。\n- **共识**: R1+R2\n\n**SF4. [warning] Deleted checkpoints 导致 N-H rate 不完整** [v4-R12-W7, 持续存在]\nISR β=0.1 s43/s44 checkpoint 丢失，5-seed pooled N-H=23% 是 uncorrected upper bound。\n- **建议**: Table 1 报告为区间或标注 \"upper bound\"；Limitations 明确列出影响。\n- **共识**: R1+R2\n\n**SF5. [warning] Dose-response claim 基于 4 β、不均匀 seed 数** [v6-R1-W2, 新]\nβ=0.1 用 5 seeds，其余用 3 seeds。\"Non-monotonic dose-response\" 统计上无法支撑。\n- **建议**: 弱化为 \"the pattern across four tested doses suggests...\"。\n- **共识**: R1+R2\n\n**SF6. [warning] §4.3 β 值呈现顺序非升序** [v6-R2-W2, 新]\n0.1→0.05→0.2→0.3 增加认知负荷。\n- **建议**: 升序呈现或解释当前顺序的叙事理由。\n- **共识**: R1 [AGREE] + R2 [提出]\n\n**SF7. [warning] Table 1 caption 过长 (~120 words + 6 脚注)** [v5-R2-W6, 持续存在]\n- **建议**: Caption 压缩至 ≤60 words，条件说明移正文。\n- **共识**: R1+R2\n\n**SF8. [warning] Introduction \\paragraph{} 结构争议** [v5-R2-W3, 持续存在]\n- **分歧**: R2 认为 5 个 \\paragraph{} 碎片化叙事; R1 认为结构服务于逻辑链，问题在于段内数据密度。\n- **Director 裁决**: 两种修改方向均可接受。\n\n### Nice-to-Have（info 级别）\n\n- **NF1.** Pooled Fisher vs CMH 在 Appendix Table 4 中的排列顺序应调整（CMH 置于 Fisher 前）[v4-R1-N4, R2 部分 REBUT 后降级]\n- **NF2.** LOO 缩写未在首次使用时定义 [v6-R2-W6-LOO]\n- **NF3.** 100 eval samples 对 per-seed claims 效力有限；小 n seed 应报告 CI [v4-R1-W8]\n- **NF4.** Seed 43 exec-only eval 协议不一致（T=0.7），Appendix 标注不够显著 [v4-R12-W6]\n- **NF5.** Hacking taxonomy 部分 mode 为单点观察，建议标注 evidence strength [v6-R2-W8]\n- **NF6.** 引用偏少（37 条），建议增加 Amodei 2016, Geirhos 2020 (shortcut learning), DeepSeek-R1 2025 [v5-R2-MR]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| ISR 命名不一致 | AGREE | 提出 | 必须统一 |\n| Abstract 数据过载 | AGREE | 提出 | 必须精简 |\n| Table 1 不对称比较 | 提出 | AGREE | 必须修正 |\n| OR 反转 framing | 提出 | AGREE | 必须修正 framing |\n| SFT PR confound | 提出 | AGREE | C1 claim 弱化 |\n| Checkpoint 丢失影响 | 提出 | AGREE | 标注 upper bound |\n| 1.7B 单 seed | AGREE | AGREE | 弱化 claims |\n| β=0.3/0.05 缺 trajectory | AGREE | AGREE | 弱化 \"at all doses\" |\n| Dose-response 4 点不足 | 提出 | AGREE | 弱化 claim |\n| Table 1 caption 过长 | AGREE | 提出 | 精简 |\n| β 呈现顺序 | AGREE | 提出 | 升序或解释 |\n| LOO 缩写未定义 | AGREE | 提出 | 简单修复 |\n\n---\n\n## Reviewer Divergence\n\n**D1. Soundness 评分: R1=2.5/5, R2=4.0/5**\n- R1 聚焦于比较框架不对称（Table 1 exec-only 单 seed vs ISR 5-seed pooled）、OR 反转 framing、SFT PR confound、统计层级倒置，认为这些是根本性缺陷。\n- R2 认为论文的 multi-seed 设计、matched controls、CMH stratification 在该领域是 above-average 标准，上述问题是 framing issues 而非根本性缺陷。\n- **Director 裁决**: Soundness 约 3.0-3.5。R1 的具体指摘均有效，但多数可通过 framing 修正解决，不需要新实验。R2 对 SFT confound 的补充（不影响核心贡献）有道理。\n\n**D2. Excitement 评分: R1=3.5/5, R2=2.0/5**\n- R1 认为 cautionary value 高，taxonomy 有实用性，stochastic bifurcation 等现象非平凡。\n- R2 认为核心 insight 是 Goodhart's Law 的直接推论，empirical increment 有限。\n- **Director 裁决**: Excitement 约 2.5-3.0。概念层面确实可预测（R2 正确），但 empirical details 有增量（R1 正确）。论文的 framing 需要更好地突出理论无法预测的具体现象。\n\n**D3. Introduction \\paragraph{} 结构: R1 REBUT, R2 提出**\n- R1 认为 5 个 \\paragraph{} 服务于两个 story arc 的逻辑链，问题在段内数据密度。\n- R2 认为 \\paragraph{} 碎片化叙事，建议减少到 2-3 个或去掉。\n- **Director 裁决**: 不裁决，两种方向均可接受。\n\n**D4. Taxonomy principled-ness: R1 REBUT, R2 提出**\n- R1 认为分类标准统一（基于 mechanism），cross-validation 证明非 post-hoc。\n- R2 认为 9 种 mode 缺乏理论完备性论证。\n- **Director 裁决**: 降级为 info。标注 evidence strength 即可。\n\n---\n\n## Questions（需作者澄清）\n\n1. ISR 应统一为哪个名称？如果 \"Irreducible Solver Rate\"，Method §3 需要大幅修改描述语言。\n2. 是否有可能补跑 1-2 个 β=0.3 1000-step trajectory 以支撑 \"at all doses\" claim？\n3. s43/s44 checkpoint 丢失是技术事故还是存储策略？是否有防止未来类似丢失的措施？\n4. 如果 3-seed corrected OR=0.61 是更可靠的估计，是否考虑将 ISR β=0.1 的 transient genuine window 完全从核心叙事中降级？\n\n---\n\n## Missing References\n\n两位 Reviewer 共识的缺失引用：\n1. **Amodei et al. (2016)**, \"Concrete Problems in AI Safety\" — reward hacking 讨论的基础性引用\n2. **Geirhos et al. (2020)**, shortcut learning 综述 — 与 \"degenerate shortcuts\" 直接对话\n3. **DeepSeek-R1 (2025)** — 使用 GRPO 的代表性工作\n\n可选增加：\n4. Christiano et al. (2017), RLHF — 边际相关\n5. AlphaProof 或 LEGO-Prover — neurosymbolic proof generation at scale\n\n当前 37 条引用对 EMNLP 偏少（典型 40-60 条），增加 3-5 条即可。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5**\n\n**理由**:\n论文是一篇实验认真、报告透明的经验性研究。核心发现（ISR 作为 diagnostic 有效但作为 reward 在所有测试剂量下触发 Goodhart collapse）对 neurosymbolic RL 社区有实际警示价值。实验覆盖面广（6 conditions × 5 seeds × 2 logics × 2 scales），统计分析（CMH + matched controls + trajectory analysis）在该领域属 above-average。\n\n主要扣分因素：\n1. **新颖性有限** (Excitement 约 2.5): 核心 insight 是 Goodhart's Law 的直接推论；LOO ablation 是标准方法；论文坦诚承认 \"our contribution lies in applying it\"。论文需更好地 frame 理论无法预测的经验现象。\n2. **写作问题多** (MF1+MF2): ISR 命名不一致是不应出现的错误；Abstract 数据过载是复发问题（Round 3 修复后再次膨胀）。\n3. **比较框架不对称** (MF3+MF4+MF5): Table 1 exec-only 单 seed vs ISR 5-seed pooled；OR 反转 framing 不够诚实；SFT PR confound 未充分控制。\n4. **实验范围窄**: 单一模型族 (Qwen3) + 单一数据集 (FOLIO)；1.7B 仅单 seed。\n\n**修改后潜力**: 多数 Must-Fix 是 framing/写作问题，可在一轮修改中解决，无需新实验（除可能的 β=0.3 trajectory 补跑）。修复后有望达到 3.5 (Borderline Conference)。是否达到 4.0 (Conference) 取决于 novelty framing 能否让审稿人信服 empirical contribution 的增量足够。\n\n---\n\n## Detailed Comments\n\n### §Abstract (abstract.tex)\n- **[MF1]** L3 \"Irreducible Solver Rate\" 与 Method §3 \"Intensional Structural Reward\" 冲突。统一名称。\n- **[MF2]** 15+ 数字过载。建议结构: (1) 问题+方法 2 句; (2) ISR-as-diagnostic 核心数字 1 个; (3) ISR-as-reward 核心结论 1 句; (4) breadth statement 1 句。目标 ≤4 数字。\n- L7 \"exhibits qualitatively distinct gaming modes in single-seed 1.7B evaluation\" — 措辞暗示比单 seed 更强的 generalization。\n\n### §1 Introduction (introduction.tex)\n- **[SF8]** 5 个 \\paragraph{} 争议。至少精简 ¶4 \"ISR as reward\" 段内数据密度（当前含 4 β 值、5 seeds bifurcation、2 trajectory、OR 值）。\n- L22 C1 \"localizing the failure to RL\" — **[MF5]** 弱化为 \"consistent with RL-specific failure\"。\n- L27 \"ISR initially yields more genuine output than random controls, but this benefit reverses under stricter classification\" — **[MF4]** framing 应将 stricter classification 的反转放在更显著位置。\n- L29 \"preliminarily observed at 1.7B scale\" — 好的限定语，但 \"exhibits qualitatively distinct gaming modes\" 仍暗示 robust finding。\n\n### §2 Related Work (related_work.tex)\n- L20 \"primarily regressional, with extremal elements\" — Goodhart variant 已指定，v5-R1-W5 可能已解决。\n- 建议增加 Amodei 2016, Geirhos 2020 (shortcut learning), DeepSeek-R1 2025。\n\n### §3 Method (method.tex)\n- **[MF1]** L44 \"Intensional Structural Reward\" — 与 Abstract 不一致。\n- L56 premise-count confound 讨论完整且诚实，是论文的一个亮点。\n- Algorithm 1 仅 6 行 — 方法贡献薄，但论文已诚实定位为 empirical study。\n\n### §4 Experiments (experiments.tex)\n- **[MF3]** Table 1 exec-only 行应增加 3-seed 1000-step 数据。Caption 需精简。\n- **[SF6]** §4.3 β 呈现顺序应改为升序。\n- L91 reward landscape 分析（H7=1+0.75β vs genuine≈1+0.26β）— v5-R1-W6 可能已解决。\n- L94 CMH 确实是正文中 first-mentioned test — v4-R1-N4 的严重性在交叉后降级。\n- L96 \"bound the true effect from above and below\" — **[MF4]** 不够准确，需修正。\n- §4.5 L141 \"No safe scale was observed\" — **[SF2]** 改为 \"...in this single-seed comparison\"。\n\n### §5 Discussion and Conclusion (conclusion.tex)\n- 仅 7 行，对实验发现丰富的论文来说讨论不够充分。建议增加 2-3 句讨论：(a) 理论无法预测的经验现象; (b) 对 neurosymbolic RL 的操作建议。\n\n### §6 Limitations (limitations.tex)\n- 内容充实，涵盖 temporal snapshot、seed counts、cross-scale、data scale。\n- 建议增加 checkpoint 丢失的影响讨论。\n\n### §7 Ethics (ethics.tex)\n- 存在且合理。\n\n### Format Compliance\n- ✅ 正文 §1-§5 在 8 页内（§5 在 page 8 结束，§6 Limitations 从 page 9 开始）\n- ✅ Limitations 位于 Conclusion 之后、References 之前\n- ✅ Ethics Statement 存在\n- ✅ Double-blind 匿名化（\"Anonymous ACL submission\"）\n- ✅ ACL template with review option\n- ⚠️ Table 1 caption 过长\n- ⚠️ LOO 缩写未正式定义\n\n---\n\n**报告结束。**\n\nReviewer 1 评分: 3.5 (Borderline Conference) | Soundness 2.5 | Excitement 3.5\nReviewer 2 评分: 3.0 (Findings) | Soundness 4.0 | Excitement 2.0\nDirector 综合评分: **3.0 (Findings)** | Soundness ~3.0 | Excitement ~2.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "report": "# 圆桌审稿报告 — Round 6\n\n**论文**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\n**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle, deadline 2026-05-25)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+写作质量+格式合规+完整性）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 neurosymbolic formalizer 的 solver 输入进行 leave-one-out 消融，生成 Intensional Structural Reward (ISR) 指标。ISR 作为诊断工具有效揭示了 execution-based evaluation 隐藏的结构崩溃（99.5% degradation），但作为训练信号时在所有 4 个测试剂量下触发 Goodhart collapse。论文覆盖 6 reward conditions、5 seeds、2 logic types、2 model scales，cataloging 了 9 种 hacking 模式。\n\n---\n\n## Strengths\n\n**S1. 实验覆盖面广且透明度高**\n多 seed（3-5 per condition）、matched random controls、CMH 分层检验、1000-step trajectory analysis、premise-count-matched comparison——该领域少见的统计严谨度。论文坦诚披露所有已知局限（ISR premise-count confound、OR 方向反转、checkpoint 丢失、eval 协议不一致），自我批评充分。[共识: R1+R2]\n\n**S2. 叙事核心有说服力**\n\"ISR: reliable as observer, unreliable as optimizer at any dose\" 是一个清晰、有警示价值的结论。对 neurosymbolic RL 社区有实际操作意义。[共识: R1+R2]\n\n**S3. Hacking taxonomy 有独立操作价值**\n9 种 hacking mode 的定义、示例和 ISR 交互分析对从业者有直接参考价值。Cross-validation 思维（text-match + functional LOO analysis）发现了 H7b obfuscated tautology 和 query-as-fact gaming，体现 careful empirical work。[共识: R1+R2]\n\n**S4. Control design 正确**\nSFT control（分离 RL-specific vs data exposure）、random control（分离 ISR-specific vs generic variance）、matched dose design 的实验逻辑清晰。[R1 优势 #5; R2 隐含同意]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] ISR 核心指标命名不一致** [v6-R2-N1]\nAbstract 将 ISR 定义为 \"Irreducible Solver Rate\" (abstract.tex:3)，Introduction/Method 定义为 \"Intensional Structural Reward\" (method.tex:44)。核心概念的名称冲突是严重的写作错误，损害可信度。此外，\"Reward\" 一词暗示应被用作 reward，与论文核心结论矛盾 (v6-R2-W5)。\n- **建议**: 统一为不含 \"Reward\" 的名称（如 \"Irreducible Solver Rate\"）。\n- **共识**: R1 [AGREE] + R2 [提出]\n\n**MF2. [critical] Abstract 数据过载，30 秒内无法消化核心贡献** [v5-R2-W1, 复发]\nAbstract (~220 words) 包含 15+ 数字/统计量（97±2%, 99.5%, 92%, β∈{0.05,0.1,0.2,0.3}, 3/3 seeds, 0%, 6 conditions, 2 logic types, 2 model scales, 5 seeds, 9 hacking modes）。读感像压缩的 results table，核心 insight 被数字淹没。此问题在 Round 3 修复后（重写为 ~170 words）再次膨胀。\n- **建议**: 保留 ≤4 个关键数字，移除 β 列表、seed counts、condition counts。\n- **共识**: R1 [AGREE] + R2 [提出]\n\n**MF3. [critical] Table 1 比较框架不对称** [v5-R1-N3, 持续存在]\nTable 1 exec-only 行为单 seed (s42)、500-step，而 ISR/Random 为 5-seed pooled。3-seed 1000-step exec-only 数据（PR=97±2%, N-H≈2%）在附录但不在主表。主表是审稿人第一眼看到的比较基准，不对称的比较框架损害所有下游 claim 的可信度。\n- **建议**: Table 1 增加 exec-only 3-seed 1000-step 行。\n- **共识**: R1 [提出] + R2 [AGREE]\n\n**MF4. [critical] OR=3.48 vs OR=0.61 方向反转的 framing 不够诚实** [v4-R12-N3, 持续存在]\n5-seed uncorrected OR=3.48 基于包含 2 个 checkpoint 已删除 seed 的不完整数据，3-seed H8+FN-corrected OR=0.61 是唯一有完整审计的比较。论文将二者 frame 为 \"bound the true effect from above and below\"，但应将 corrected 分析作为 primary sensitivity，明确 \"genuine-rate advantage is not robust to H8 correction\"。CMH OR=3.37 (p<10⁻⁹) 方向一致，说明正面效应非纯粹 artifact，但 framing 仍需修正。\n- **建议**: (a) 3-seed corrected 提升为 primary sensitivity; (b) Abstract/Intro 弱化 \"initially yields more genuine\" 措辞; (c) 正文讨论 \"transient benefit 是否真实存在的不确定性\"。\n- **共识**: R1 [提出] + R2 [AGREE with nuance]\n\n**MF5. [critical] SFT vs RL 比较中 PR 严重混淆** [v5-R12-SFT-PR, 持续存在]\nSFT PR=13% (n=39) vs RL PR=93%+。C1 \"localizing the failure to RL\" 的证据链有根本性 PR confound：无法知道 SFT 在高 PR 时是否也会 hack。100-step checkpoint (PR=32%, hacking=31.2%) 部分缓解但 PR 仍为 SFT 的 2.5 倍。机制论证（SFT 无 exploration-exploitation dynamics）是合理的 reasoning 但非 empirical evidence。\n- **建议**: C1 弱化为 \"consistent with RL-specific failure\"；正文承认 \"whether SFT would hack at higher PR remains unknown\"。\n- **注意**: R2 补充——SFT 比较是一个 confound 但不影响论文核心贡献（ISR collapse diagnostic, Goodhart at all doses, taxonomy）。\n- **共识**: R1 [提出] + R2 [AGREE]\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] 新颖性 framing 不足** [v5-R2-N3 + v4-R2-W9, 持续存在]\n\"Diagnostic becomes optimization target\" 是 Goodhart's Law 的定义，不是新发现。LOO ablation 是标准方法。论文需说服 reader 为什么这个经验实例值得一篇论文。\n- **Director 裁决**: R2 正确指出概念层面可预测，但 R1 正确指出 stochastic bifurcation timing、H7b triple gaming、cross-logic mode divergence、OR 方向反转是理论无法预测的经验现象。论文应将 framing 从 \"we discover Goodhart effects\" 转为 \"Goodhart collapse is predictable, but these specific phenomena are not\"。\n- **分歧记录**: R1 Excitement=3.5, R2 Excitement=2.0\n\n**SF2. [warning] 1.7B cross-scale claims 仅单 seed** [v3-R12-NI-1, 持续存在]\n4B scale 下 3 seeds 产生 3 种截然不同的 hacking mode，说明单 seed 几乎不具备代表性。§4.5 \"No safe scale was observed\" 是 n=1 的存在性声明。\n- **建议**: 弱化为 \"No safe scale was observed in this single-seed comparison\"。\n- **共识**: R1+R2\n\n**SF3. [warning] \"At all tested doses\" claim 缺 β=0.3/0.05 trajectory 数据** [v4-R12-N2, 持续存在]\n1000-step trajectory 仅对 β=0.1 两个 seed 进行。β=0.3 和 β=0.05 仅 500-step snapshot。论文自身方法论认为 snapshot 不足以判断 long-run 行为，但对自己的 claims 使用了 snapshot。\n- **建议**: 弱化为 \"collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1\"。\n- **共识**: R1+R2\n\n**SF4. [warning] Deleted checkpoints 导致 N-H rate 不完整** [v4-R12-W7, 持续存在]\nISR β=0.1 s43/s44 checkpoint 丢失，5-seed pooled N-H=23% 是 uncorrected upper bound。\n- **建议**: Table 1 报告为区间或标注 \"upper bound\"；Limitations 明确列出影响。\n- **共识**: R1+R2\n\n**SF5. [warning] Dose-response claim 基于 4 β、不均匀 seed 数** [v6-R1-W2, 新]\nβ=0.1 用 5 seeds，其余用 3 seeds。\"Non-monotonic dose-response\" 统计上无法支撑。\n- **建议**: 弱化为 \"the pattern across four tested doses suggests...\"。\n- **共识**: R1+R2\n\n**SF6. [warning] §4.3 β 值呈现顺序非升序** [v6-R2-W2, 新]\n0.1→0.05→0.2→0.3 增加认知负荷。\n- **建议**: 升序呈现或解释当前顺序的叙事理由。\n- **共识**: R1 [AGREE] + R2 [提出]\n\n**SF7. [warning] Table 1 caption 过长 (~120 words + 6 脚注)** [v5-R2-W6, 持续存在]\n- **建议**: Caption 压缩至 ≤60 words，条件说明移正文。\n- **共识**: R1+R2\n\n**SF8. [warning] Introduction \\paragraph{} 结构争议** [v5-R2-W3, 持续存在]\n- **分歧**: R2 认为 5 个 \\paragraph{} 碎片化叙事; R1 认为结构服务于逻辑链，问题在于段内数据密度。\n- **Director 裁决**: 两种修改方向均可接受。\n\n### Nice-to-Have（info 级别）\n\n- **NF1.** Pooled Fisher vs CMH 在 Appendix Table 4 中的排列顺序应调整（CMH 置于 Fisher 前）[v4-R1-N4, R2 部分 REBUT 后降级]\n- **NF2.** LOO 缩写未在首次使用时定义 [v6-R2-W6-LOO]\n- **NF3.** 100 eval samples 对 per-seed claims 效力有限；小 n seed 应报告 CI [v4-R1-W8]\n- **NF4.** Seed 43 exec-only eval 协议不一致（T=0.7），Appendix 标注不够显著 [v4-R12-W6]\n- **NF5.** Hacking taxonomy 部分 mode 为单点观察，建议标注 evidence strength [v6-R2-W8]\n- **NF6.** 引用偏少（37 条），建议增加 Amodei 2016, Geirhos 2020 (shortcut learning), DeepSeek-R1 2025 [v5-R2-MR]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| ISR 命名不一致 | AGREE | 提出 | 必须统一 |\n| Abstract 数据过载 | AGREE | 提出 | 必须精简 |\n| Table 1 不对称比较 | 提出 | AGREE | 必须修正 |\n| OR 反转 framing | 提出 | AGREE | 必须修正 framing |\n| SFT PR confound | 提出 | AGREE | C1 claim 弱化 |\n| Checkpoint 丢失影响 | 提出 | AGREE | 标注 upper bound |\n| 1.7B 单 seed | AGREE | AGREE | 弱化 claims |\n| β=0.3/0.05 缺 trajectory | AGREE | AGREE | 弱化 \"at all doses\" |\n| Dose-response 4 点不足 | 提出 | AGREE | 弱化 claim |\n| Table 1 caption 过长 | AGREE | 提出 | 精简 |\n| β 呈现顺序 | AGREE | 提出 | 升序或解释 |\n| LOO 缩写未定义 | AGREE | 提出 | 简单修复 |\n\n---\n\n## Reviewer Divergence\n\n**D1. Soundness 评分: R1=2.5/5, R2=4.0/5**\n- R1 聚焦于比较框架不对称（Table 1 exec-only 单 seed vs ISR 5-seed pooled）、OR 反转 framing、SFT PR confound、统计层级倒置，认为这些是根本性缺陷。\n- R2 认为论文的 multi-seed 设计、matched controls、CMH stratification 在该领域是 above-average 标准，上述问题是 framing issues 而非根本性缺陷。\n- **Director 裁决**: Soundness 约 3.0-3.5。R1 的具体指摘均有效，但多数可通过 framing 修正解决，不需要新实验。R2 对 SFT confound 的补充（不影响核心贡献）有道理。\n\n**D2. Excitement 评分: R1=3.5/5, R2=2.0/5**\n- R1 认为 cautionary value 高，taxonomy 有实用性，stochastic bifurcation 等现象非平凡。\n- R2 认为核心 insight 是 Goodhart's Law 的直接推论，empirical increment 有限。\n- **Director 裁决**: Excitement 约 2.5-3.0。概念层面确实可预测（R2 正确），但 empirical details 有增量（R1 正确）。论文的 framing 需要更好地突出理论无法预测的具体现象。\n\n**D3. Introduction \\paragraph{} 结构: R1 REBUT, R2 提出**\n- R1 认为 5 个 \\paragraph{} 服务于两个 story arc 的逻辑链，问题在段内数据密度。\n- R2 认为 \\paragraph{} 碎片化叙事，建议减少到 2-3 个或去掉。\n- **Director 裁决**: 不裁决，两种方向均可接受。\n\n**D4. Taxonomy principled-ness: R1 REBUT, R2 提出**\n- R1 认为分类标准统一（基于 mechanism），cross-validation 证明非 post-hoc。\n- R2 认为 9 种 mode 缺乏理论完备性论证。\n- **Director 裁决**: 降级为 info。标注 evidence strength 即可。\n\n---\n\n## Questions（需作者澄清）\n\n1. ISR 应统一为哪个名称？如果 \"Irreducible Solver Rate\"，Method §3 需要大幅修改描述语言。\n2. 是否有可能补跑 1-2 个 β=0.3 1000-step trajectory 以支撑 \"at all doses\" claim？\n3. s43/s44 checkpoint 丢失是技术事故还是存储策略？是否有防止未来类似丢失的措施？\n4. 如果 3-seed corrected OR=0.61 是更可靠的估计，是否考虑将 ISR β=0.1 的 transient genuine window 完全从核心叙事中降级？\n\n---\n\n## Missing References\n\n两位 Reviewer 共识的缺失引用：\n1. **Amodei et al. (2016)**, \"Concrete Problems in AI Safety\" — reward hacking 讨论的基础性引用\n2. **Geirhos et al. (2020)**, shortcut learning 综述 — 与 \"degenerate shortcuts\" 直接对话\n3. **DeepSeek-R1 (2025)** — 使用 GRPO 的代表性工作\n\n可选增加：\n4. Christiano et al. (2017), RLHF — 边际相关\n5. AlphaProof 或 LEGO-Prover — neurosymbolic proof generation at scale\n\n当前 37 条引用对 EMNLP 偏少（典型 40-60 条），增加 3-5 条即可。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5**\n\n**理由**:\n论文是一篇实验认真、报告透明的经验性研究。核心发现（ISR 作为 diagnostic 有效但作为 reward 在所有测试剂量下触发 Goodhart collapse）对 neurosymbolic RL 社区有实际警示价值。实验覆盖面广（6 conditions × 5 seeds × 2 logics × 2 scales），统计分析（CMH + matched controls + trajectory analysis）在该领域属 above-average。\n\n主要扣分因素：\n1. **新颖性有限** (Excitement 约 2.5): 核心 insight 是 Goodhart's Law 的直接推论；LOO ablation 是标准方法；论文坦诚承认 \"our contribution lies in applying it\"。论文需更好地 frame 理论无法预测的经验现象。\n2. **写作问题多** (MF1+MF2): ISR 命名不一致是不应出现的错误；Abstract 数据过载是复发问题（Round 3 修复后再次膨胀）。\n3. **比较框架不对称** (MF3+MF4+MF5): Table 1 exec-only 单 seed vs ISR 5-seed pooled；OR 反转 framing 不够诚实；SFT PR confound 未充分控制。\n4. **实验范围窄**: 单一模型族 (Qwen3) + 单一数据集 (FOLIO)；1.7B 仅单 seed。\n\n**修改后潜力**: 多数 Must-Fix 是 framing/写作问题，可在一轮修改中解决，无需新实验（除可能的 β=0.3 trajectory 补跑）。修复后有望达到 3.5 (Borderline Conference)。是否达到 4.0 (Conference) 取决于 novelty framing 能否让审稿人信服 empirical contribution 的增量足够。\n\n---\n\n## Detailed Comments\n\n### §Abstract (abstract.tex)\n- **[MF1]** L3 \"Irreducible Solver Rate\" 与 Method §3 \"Intensional Structural Reward\" 冲突。统一名称。\n- **[MF2]** 15+ 数字过载。建议结构: (1) 问题+方法 2 句; (2) ISR-as-diagnostic 核心数字 1 个; (3) ISR-as-reward 核心结论 1 句; (4) breadth statement 1 句。目标 ≤4 数字。\n- L7 \"exhibits qualitatively distinct gaming modes in single-seed 1.7B evaluation\" — 措辞暗示比单 seed 更强的 generalization。\n\n### §1 Introduction (introduction.tex)\n- **[SF8]** 5 个 \\paragraph{} 争议。至少精简 ¶4 \"ISR as reward\" 段内数据密度（当前含 4 β 值、5 seeds bifurcation、2 trajectory、OR 值）。\n- L22 C1 \"localizing the failure to RL\" — **[MF5]** 弱化为 \"consistent with RL-specific failure\"。\n- L27 \"ISR initially yields more genuine output than random controls, but this benefit reverses under stricter classification\" — **[MF4]** framing 应将 stricter classification 的反转放在更显著位置。\n- L29 \"preliminarily observed at 1.7B scale\" — 好的限定语，但 \"exhibits qualitatively distinct gaming modes\" 仍暗示 robust finding。\n\n### §2 Related Work (related_work.tex)\n- L20 \"primarily regressional, with extremal elements\" — Goodhart variant 已指定，v5-R1-W5 可能已解决。\n- 建议增加 Amodei 2016, Geirhos 2020 (shortcut learning), DeepSeek-R1 2025。\n\n### §3 Method (method.tex)\n- **[MF1]** L44 \"Intensional Structural Reward\" — 与 Abstract 不一致。\n- L56 premise-count confound 讨论完整且诚实，是论文的一个亮点。\n- Algorithm 1 仅 6 行 — 方法贡献薄，但论文已诚实定位为 empirical study。\n\n### §4 Experiments (experiments.tex)\n- **[MF3]** Table 1 exec-only 行应增加 3-seed 1000-step 数据。Caption 需精简。\n- **[SF6]** §4.3 β 呈现顺序应改为升序。\n- L91 reward landscape 分析（H7=1+0.75β vs genuine≈1+0.26β）— v5-R1-W6 可能已解决。\n- L94 CMH 确实是正文中 first-mentioned test — v4-R1-N4 的严重性在交叉后降级。\n- L96 \"bound the true effect from above and below\" — **[MF4]** 不够准确，需修正。\n- §4.5 L141 \"No safe scale was observed\" — **[SF2]** 改为 \"...in this single-seed comparison\"。\n\n### §5 Discussion and Conclusion (conclusion.tex)\n- 仅 7 行，对实验发现丰富的论文来说讨论不够充分。建议增加 2-3 句讨论：(a) 理论无法预测的经验现象; (b) 对 neurosymbolic RL 的操作建议。\n\n### §6 Limitations (limitations.tex)\n- 内容充实，涵盖 temporal snapshot、seed counts、cross-scale、data scale。\n- 建议增加 checkpoint 丢失的影响讨论。\n\n### §7 Ethics (ethics.tex)\n- 存在且合理。\n\n### Format Compliance\n- ✅ 正文 §1-§5 在 8 页内（§5 在 page 8 结束，§6 Limitations 从 page 9 开始）\n- ✅ Limitations 位于 Conclusion 之后、References 之前\n- ✅ Ethics Statement 存在\n- ✅ Double-blind 匿名化（\"Anonymous ACL submission\"）\n- ✅ ACL template with review option\n- ⚠️ Table 1 caption 过长\n- ⚠️ LOO 缩写未正式定义\n\n---\n\n**报告结束。**\n\nReviewer 1 评分: 3.5 (Borderline Conference) | Soundness 2.5 | Excitement 3.5\nReviewer 2 评分: 3.0 (Findings) | Soundness 4.0 | Excitement 2.0\nDirector 综合评分: **3.0 (Findings)** | Soundness ~3.0 | Excitement ~2.5"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-17T16:35:10.227902+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4015
}
```

</details>

---


### Assistant

_source line 520 · 2026-05-17T16:35:19.441803+00:00_

审稿报告已投递至 Research Director。

**Round 6 圆桌审稿完成。**

总结：
- **综合评分**: 3.0 (Findings)
- **5 个 Must-Fix**: ISR 命名不一致、Abstract 数据过载、Table 1 不对称比较、OR 反转 framing 不诚实、SFT PR confound
- **8 个 Should-Fix**: 新颖性 framing 不足、1.7B 单 seed、β=0.3/0.05 缺 trajectory、checkpoint 丢失标注、dose-response 4 点不足、β 呈现顺序、Table 1 caption 过长、Introduction 结构争议
- **6 个 Nice-to-Have**: Appendix 统计表排序、LOO 缩写、小 n CI、s43 eval 标注、taxonomy evidence strength、引用补充
- **修改后潜力**: 多数 Must-Fix 为 framing/写作问题，修复后有望达 3.5 (Borderline Conference)
- **Issue Tracker**: 已同步更新至 `review_issues.yaml`（含 Round 6 新发现 6 项 + 历史 in_progress 更新 15 项）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 521 · 2026-05-17T16:35:22.254139+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

**Must-Fix**:
- R2-N1 (命名不一致): **[AGREE]** — 确认 Abstract="Irreducible Solver Rate" vs Method="Intensional Structural Reward"，明确的写作 bug
- R2-N2 (新颖性): **[AGREE with nuance]** — Goodhart 本身可预测，但 stochastic bifurcation timing、H7b triple gaming、query-as-fact gaming 是非平凡的经验发现；建议重新 frame 为 empirical study
- R2-N3 (Abstract 过载): **[AGREE]** — 15+ 数字/统计量，实验报告风格

**Should-Fix**:
- W1 (Introduction 碎片化): **[REBUT]** — 5 段结构服务于双 story arc，问题在数据密度非结构
- W2/W4/W5/W6/W7: **[AGREE]**
- W3 (范围窄): **[REBUT partial]** — 已覆盖 2 logic × 2 scale × 6 conditions，FOLIO 是唯一可用 benchmark
- W8 (Taxonomy 不 principled): **[REBUT]** — 分类轴是 mechanism 非检测方法，但单点观察 mode 应标注证据强度

**关键分歧**: R2 给 Soundness 4/5，与我的 2.5/5 差距大。如果我的 N2 (OR 反转 framing) 和 N5 (Fisher vs CMH 层级) 成立，R2 对实验严谨性的评价偏高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 522 · 2026-05-17T16:35:34.727348+00:00_

审稿报告已投递完毕。

**审稿流程总结**:

- **Round 1**: 两位 Reviewer 独立审稿 → 交叉分享 → 1 轮达成共识
- **最终评分**: **3.0 (Findings)**
  - R1: 3.5 (Borderline Conference), R2: 3.0 (Findings)
  - Director 综合: 3.0，Soundness ~3.0, Excitement ~2.5

**核心问题汇总**:
- 5 个 Must-Fix（ISR 命名不一致、Abstract 过载、Table 1 不对称、OR 反转 framing、SFT PR confound）
- 8 个 Should-Fix（新颖性 framing、1.7B 单 seed、trajectory 缺失、checkpoint 丢失、dose-response 4 点、β 呈现顺序、Table 1 caption、Introduction 结构）
- 6 个 Nice-to-Have

**修改后潜力**: 多数 Must-Fix 是 framing/写作问题，可在一轮修改中解决。修复后有望达到 3.5 (Borderline Conference)。

Issue tracker 已同步更新至 `review_issues.yaml`（Round 6 新增 6 个 issue，更新 15 个 in_progress issue 的 mentions）。报告已通过 `submit_review_report_to_research_director` 投递。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 50

## Round 50

58 recorded events


### User

_source line 523 · 2026-05-17T17:03:06.499118+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-17T17:03:14.088352+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-17T17:03:14.162204+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 73
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-17T17:03:18.557130+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-17T17:03:18.607674+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-17T17:03:25.733447+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-17T17:03:25.784113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-17T17:03:31.450868+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-17T17:03:32.406193+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (140 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- sweep-random-b01-s46: W4: Random β=0.1 s46 extends random control to 5-seed（排队等待 GPU）\n- sweep-random-b01-s45: W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1（排队等待 GPU）\n- sweep-isr-b005-s42: W3: β=0.05 ISR bonus produces less aggressive hacking than β=0.1/0.3 while retaining structural signal — tests Goodhart's Law dose-response（准备中）\n- w2-qwen3-7b-pilot: Qwen3-8B exec-only 50-step pilot: 测试 8B 模型能否在 96GB GPU 上跑通，确定 per_device_batch_size (4 vs 2)（准备中）\n- plan001-exec-only-s45: Exec-only seed=45, 5-seed baseline for tighter confidence intervals（准备中）\n- sweep-isr-b01-s46: W4: ISR β=0.1 s46 extends to 5-seed for tighter confidence intervals（准备中）\n\n## 近期结论\n- **plan002-additive-b01-s45-1000** (negative): ISR β=0.1 seed=45 genuine window (~55% at 500 steps) will collapse by 1000 steps, consistent with the inevitable collapse pattern observed in s42 (17%→2%). Extended training drives ISR-trained models toward metric gaming regardless of initial genuine rate. ← 基于 plan002-additive-b01-s45\n- **sweep-random-b005-s44** (success): Random β=0.05 seed=44
…[truncated 1873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-17T17:03:32.406570+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 533 · 2026-05-17T17:03:33.962853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 534 · 2026-05-17T17:03:34.013466+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-17T17:03:44.153997+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 main conference papers:

## Paper Types and Scope

EMNLP 2026 invites s
…[truncated 1656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 11747
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-17T17:03:56.353201+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit long paper short paper template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit long paper short paper template"
  }
}
```

</details>

---


### Tool call

_source line 537 · 2026-05-17T17:03:57.357171+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-17T17:03:57.709032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-17T17:04:02.192201+00:00_

Web search results for query: "EMNLP 2026 submission format page limit long paper short paper template"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/about/submissions"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

Based on the search results, here's the submission format information for EMNLP 2026:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Format and Template

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Requirements

The mandatory Limitations section is required, placed after the conclusion.

##
…[truncated 512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5838
}
```

</details>

---


### Tool result

_source line 540 · 2026-05-17T17:04:02.192816+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: met
…[truncated 3661 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4835
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-17T17:04:02.243304+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\pm}2\%$, three seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, suggesting the failure is RL-specific.
4	Repurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.
5	Across 6 conditions, 2 logic types, and 2 model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
6	\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 4534
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-17T17:04:12.031607+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission requirements anonymity checklist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle submission requirements anonymity checklist"
  }
}
```

</details>

---


### Tool call

_source line 543 · 2026-05-17T17:04:12.383400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-17T17:04:12.383893+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-17T17:04:12.434489+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\pm}2\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yield
…[truncated 3732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 546 · 2026-05-17T17:04:22.974977+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission requirements anonymity checklist"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the web search results, here is information about ACL Rolling Review 2026 May cycle submission requirements and anonymity checklist:

## Submission Requirements

ARR provides authors with a checklist to assist with avoiding common issues (the list is not exhaustive), and starting from December 2024, ARR enforces desk rejections for incorrect, incomplete or misleading filing of the responsible NLP checklist, and
…[truncated 991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 10943
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-17T17:04:23.025748+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 10641
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-17T17:04:28.900841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-17T17:04:29.453602+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation 
…[truncated 5560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-17T17:04:29.454135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-17T17:04:29.906818+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}) with greedy decoding (Appendix~\ref{app:setup}).
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples ha
…[truncated 17864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-17T17:04:29.907301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-17T17:04:30.258872+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{polu2020generative, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1-2025} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt20
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-17T17:04:30.259231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-17T17:04:30.309673+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$; \S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR increases genuine proofs over random controls ($\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification the effect reverses ($\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.
6	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
7	While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\S\ref{sec:goodhart}), non-monotonic dose-response across four $\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\S\ref{sec:crosslogic}).
8	These details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \emph{that} a metric will be gamed and predicting \emph{how}.
9	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-17T17:04:38.194759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-17T17:04:38.697219+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).
8	STA requires solvers supporting component-level input manipulation.
9	
10	\paragraph{Evaluation as temporal snapshot.}
11	All 500-step results represent a temporal snapshot, not an equilibrium.
12	Trajectory analysis on seeds~42 and~45 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient (s42: $17\%{\to}2\%$; s45: $55\%{\to}0\%$ genuine).
13	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
14	
15	\paragraph{Seed counts per dose.}
16	ISR $\beta{=}0.05$ uses three seeds (all H7-dominated); random $\beta{=}0.05$ uses three seeds with high variance ($\text{PR}{=}0\%$, $7\%$, $62\%$); $\beta{=}0.2$ uses three seeds.
17	The primary $\beta{=}0.1$ comparison uses five seeds per condition.
18	Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\S\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.
19	ISR $\beta{=}0.1$ s43 and s44 checkpoints were lost during disk cleanup, preventing retrospective H8 audit on these seeds; the reporte
…[truncated 1067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-17T17:04:38.697569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-17T17:04:39.249898+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in neurosymbolic systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-17T17:04:39.250373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-17T17:04:39.702899+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation protocol.}
53	All cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so that training-log ISR is never compared across runs.
54	The evaluation file \texttt{proofwriter\_fol\_100.jsonl} is a legacy filename cont
…[truncated 43398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-17T17:04:39.853913+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-17T17:04:39.904686+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-17T17:04:45.629182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-17T17:04:46.433857+00:00_

1	issues:
2	# ===== 历史 issues (Round 0-3, 全部 resolved) =====
3	- id: "R1-W1"
4	  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。"
11	  resolution_round: 2
12	
13	- id: "RV-EVAL-FALLBACK"
14	  summary: "eval_sta.py test_100.jsonl 静默 fallback 已移除"
15	  category: experiment
16	  severity: critical
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 1
20	  resolution: "第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。"
21	  resolution_round: 1
22	
23	- id: "RV-D060-NARRATIVE"
24	  summary: "D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立"
25	  category: experiment
26	  severity: warning
27	  status: resolved
28	  first_raised_round: 1
29	  last_seen_round: 1
30	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。"
31	  resolution_round: 2
32	
33	- id: "RV-FIG2-STALE-SCRIPT"
34	  summary: "figures/paper/gen_fig2.py 旧脚本数据错误"
35	  category: format
36	  severity: warning
37	  status: resolved
38	  first_raised_round: 1
39	  last_seen_round: 1
40	  resolution: "已修复。"
41	  resolution_round: 1
42	
43	- id: "R1-W2"
44	  summary: "ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量"
45	  category: framing
46	  severity: critical
47	  status: resolved
48	  first_raised_round: 0
49	  last_seen_round: 0
50	  resolution: "method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。"
51	  resolution_round: 2
52	
53	- id: "R2-W1"
54	  summary: "Limitations section 格式不合规"
55	  category: format
56	  severity: critical
57	  status: resolved
58	  first_raised_round: 0
59	  last_seen_round: 2
60	  resolution: "独立 limitations.tex 已创建，位于 references 之前。"
61	  resolution_round: 3
62	
63	- id: "R2-W2"
64	  summary: "实验仅用单一模型 (Qwen3-4B) 
…[truncated 29142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-17T17:04:46.434406+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-17T17:04:46.485022+00:00_

1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	% ============================================================
43	% Category 2: Reward shaping for code/formal verification
44	% ============================================================
45	
46	@inproceedings{lightman-verify-step,
47	  author 
…[truncated 2576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-17T17:05:16.823332+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-17T17:05:16.895954+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 72
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-17T17:05:25.577086+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-17T17:05:25.778482+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-17T17:05:30.549042+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/registry.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/registry.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-17T17:05:30.599762+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-17T17:05:39.914921+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A3 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml 2>/dev/null || echo \"NOT FOUND\"",
  "description": "Check external review config in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A3 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml 2>/dev/null || echo \"NOT FOUND\"",
    "description": "Check external review config in registry"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-17T17:05:40.065881+00:00_

NOT FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-17T17:06:52.180051+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: projects/solver-trace-ablation/paper/main.tex (及同目录下各 .tex 文件)\n- 目标 venue: EMNLP 2026 (通过 ACL Rolling Review)\n- 格式: ACL 模板 review 模式, Long paper 8 页正文限制, double-blind\n- ARR deadline: 2026-05-25\n\n## 你的审查侧重\n\n1. **实验设计严谨性**：\n   - 实验条件是否充分控制 confounds？\n   - Seed 数量和统计方法是否支撑 claims？\n   - SFT baseline 比较是否公平（PR 差距问题）？\n   - 评估集大小（100 例）对结论可靠性的影响？\n\n2. **统计分析**：\n   - 报告的统计检验是否正确使用？\n   - CMH test、Fisher exact test、permutation test 的使用是否恰当？\n   - OR=3.37 (CMH, uncorrected) vs OR=0.61 (3-seed corrected) 方向反转——论文如何处理？\n   - Per-seed 样本量对百分比估计的影响？\n\n3. **Claims 与证据匹配**：\n   - \"Goodhart collapse at all tested doses\" 是否有充分 trajectory evidence？\n   - Cross-scale claims（1.7B, single seed）的强度是否合理？\n   - \"β controls timing, not whether\" 是否仅 β=0.1 有 1000-step 确认？\n   - ISR diagnostic 的 sensitivity/specificity 论证是否充分？\n\n4. **方法论**：\n   - ISR 的 premise-count confound 是否充分讨论？\n   - LOO vs Shapley 的 justification 是否令人信服？\n   - Hacking taxonomy 的分类标准是否 principled？\n\n## 已知历史问题（供参考，但请独立审查）\n\n以下是此前审稿轮次中仍 open/in_progress 的关键问题。请在审查中独立验证这些问题是否已充分解决：\n\n- [CRITICAL] OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，正文 framing 是否诚实？\n- [CRITICAL] Table 1 exec-only 行为单 seed (s42) vs ISR/Random 5-seed pooled，比较框架不对称\n- [WARNING] 'Inevitable collapse at all doses' 但 trajectory 仅 β=0.1 有 1000-step\n- [WARNING] Cross-scale 1.7B 仅 single seed\n- [WARNING] Deleted checkpoints 导致 ISR β=0.1 s43/s44 H8 audit 不完整，23% N-H 为 upper bound\n- [WARNING] SFT PR=13% vs exec-only PR=93%，低 PR 本身减少 hacking 机会\n\n请按以下格式输出：\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 severity: critical/warning/info)\n## Questions (需要作者回答)\n## Missing References\n## Overall Assessment (评分 1-5, 参照 EMNLP 2026 ARR 评分标准)\n## Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: projects/solver-trace-ablation/paper/main.tex (及同目录下各 .tex 文件)\n- 目标 venue: EMNLP 2026 (通过 ACL Rolling Review)\n- 格式: ACL 模板 review 模式, Long paper 8 页正文限制, double-blind\n- ARR deadline: 2026-05-25\n\n## 你的审查侧重\n\n1. **实验设计严谨性**：\n   - 实验条件是否充分控制 confounds？\n   - Seed 数量和统计方法是否支撑 claims？\n   - SFT baseline 比较是否公平（PR 差距问题）？\n   - 评估集大小（100 例）对结论可靠性的影响？\n\n2. **统计分析**：\n   - 报告的统计检验是否正确使用？\n   - CMH test、Fisher exact test、permutation test 的使用是否恰当？\n   - OR=3.37 (CMH, uncorrected) vs OR=0.61 (3-seed corrected) 方向反转——论文如何处理？\n   - Per-seed 样本量对百分比估计的影响？\n\n3. **Claims 与证据匹配**：\n   - \"Goodhart collapse at all tested doses\" 是否有充分 trajectory evidence？\n   - Cross-scale claims（1.7B, single seed）的强度是否合理？\n   - \"β controls timing, not whether\" 是否仅 β=0.1 有 1000-step 确认？\n   - ISR diagnostic 的 sensitivity/specificity 论证是否充分？\n\n4. **方法论**：\n   - ISR 的 premise-count confound 是否充分讨论？\n   - LOO vs Shapley 的 justification 是否令人信服？\n   - Hacking taxonomy 的分类标准是否 principled？\n\n## 已知历史问题（供参考，但请独立审查）\n\n以下是此前审稿轮次中仍 open/in_progress 的关键问题。请在审查中独立验证这些问题是否已充分解决：\n\n- [CRITICAL] OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，正文 framing 是否诚实？\n- [CRITICAL] Table 1 exec-only 行为单 seed (s42) vs ISR/Random 5-seed pooled，比较框架不对称\n- [WARNING] 'Inevitable collapse at all doses' 但 trajectory 仅 β=0.1 有 1000-step\n- [WARNING] Cross-scale 1.7B 仅 single seed\n- [WARNING] Deleted checkpoints 导致 ISR β=0.1 s43/s44 H8 audit 不完整，23% N-H 为 upper bound\n- [WARNING] SFT PR=13% vs exec-only PR=93%，低 PR 本身减少 hacking 机会\n\n请按以下格式输出：\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 severity: critical/warning/info)\n## Questions (需要作者回答)\n## Missing References\n## Overall Assessment (评分 1-5, 参照 EMNLP 2026 ARR 评分标准)\n## Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-17T17:07:11.804586+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19624
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-17T17:07:12.056068+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 2，负责**新颖性/贡献定位 + 写作质量 + 格式合规**。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: projects/solver-trace-ablation/paper/main.tex (及同目录下各 .tex 文件)\n- 目标 venue: EMNLP 2026 (通过 ACL Rolling Review)\n- 格式: ACL 模板 review 模式, Long paper 8 页正文限制, double-blind\n- ARR deadline: 2026-05-25\n\n## 你的审查侧重\n\n1. **新颖性与贡献评估**：\n   - STA/ISR 方法本身新颖性如何？（Algorithm 1 仅 6 行 LOO 伪代码）\n   - \"Diagnostic becomes optimization target\" 是否只是 Goodhart's Law 的直接推论？\n   - 经验贡献（stochastic bifurcation, nine hacking modes, cross-logic transfer）的增量价值？\n   - 论文是否正确定位为 empirical study 而非 method paper？\n\n2. **写作质量**：\n   - Abstract 是否数据堆砌（计算其中的数字/统计量数量）？\n   - Introduction 的叙事结构是否连贯？\\paragraph{} 使用是否过度？\n   - Experiments §4.3 按 β 值逐一报告是否格式重复？β 呈现顺序是否合理？\n   - 全文是否有 AI 写作痕迹（em-dash、-ing phrase、过度分段、blacklisted words）？\n   - ISR 全名是否在全文中一致？（检查 Abstract 和 Method 是否用同一展开形式）\n\n3. **格式合规**：\n   - 正文是否在 8 页限制内（§1-§5 + References 之前的内容）？\n   - Limitations 和 Ethics Statement 位置是否正确？\n   - Table/Figure caption 是否自包含？Table 1 caption 长度是否合理？\n   - 缩写首次使用是否有定义？（检查 LOO, ISR, GRPO, STA, FOL, PR 等）\n   - 引用格式和数量是否合规？\n\n4. **叙事一致性**：\n   - Abstract → Introduction → Method → Experiments → Discussion 是否形成一条连贯主线？\n   - C1-C4 贡献列表是否均有对应 section 支撑？\n   - 论文核心 claim \"ISR reliable as diagnostic, unreliable as optimizer\" 是否在各 section 统一？\n\n## 已知历史问题（供参考，但请独立审查）\n\n- [CRITICAL] Abstract 数据堆砌（~15 个数字/统计量），读感像实验报告\n- [CRITICAL] ISR 命名不一致：'Irreducible Solver Rate' vs 'Intensional Structural Reward'\n- [WARNING] Introduction 5 个 \\paragraph{} 小标题导致叙事碎片化\n- [WARNING] §4.3 按 β 逐一报告格式重复，且呈现顺序非升序 (0.1→0.05→0.2→0.3)\n- [WARNING] 方法新颖性有限（Algorithm 1 仅 6 行）\n- [WARNING] Table 1 caption ~120 words + 6 脚注标记\n- [INFO] LOO 缩写首次使用时是否正式定义？\n\n请按以下格式输出：\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 severity: critical/warning/info)\n## Questions (需要作者回答)\n## Missing References\n## Overall Assessment (评分 1-5, 参照 EMNLP 2026 ARR 评分标准)\n## Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 2，负责**新颖性/贡献定位 + 写作质量 + 格式合规**。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: projects/solver-trace-ablation/paper/main.tex (及同目录下各 .tex 文件)\n- 目标 venue: EMNLP 2026 (通过 ACL Rolling Review)\n- 格式: ACL 模板 review 模式, Long paper 8 页正文限制, double-blind\n- ARR deadline: 2026-05-25\n\n## 你的审查侧重\n\n1. **新颖性与贡献评估**：\n   - STA/ISR 方法本身新颖性如何？（Algorithm 1 仅 6 行 LOO 伪代码）\n   - \"Diagnostic becomes optimization target\" 是否只是 Goodhart's Law 的直接推论？\n   - 经验贡献（stochastic bifurcation, nine hacking modes, cross-logic transfer）的增量价值？\n   - 论文是否正确定位为 empirical study 而非 method paper？\n\n2. **写作质量**：\n   - Abstract 是否数据堆砌（计算其中的数字/统计量数量）？\n   - Introduction 的叙事结构是否连贯？\\paragraph{} 使用是否过度？\n   - Experiments §4.3 按 β 值逐一报告是否格式重复？β 呈现顺序是否合理？\n   - 全文是否有 AI 写作痕迹（em-dash、-ing phrase、过度分段、blacklisted words）？\n   - ISR 全名是否在全文中一致？（检查 Abstract 和 Method 是否用同一展开形式）\n\n3. **格式合规**：\n   - 正文是否在 8 页限制内（§1-§5 + References 之前的内容）？\n   - Limitations 和 Ethics Statement 位置是否正确？\n   - Table/Figure caption 是否自包含？Table 1 caption 长度是否合理？\n   - 缩写首次使用是否有定义？（检查 LOO, ISR, GRPO, STA, FOL, PR 等）\n   - 引用格式和数量是否合规？\n\n4. **叙事一致性**：\n   - Abstract → Introduction → Method → Experiments → Discussion 是否形成一条连贯主线？\n   - C1-C4 贡献列表是否均有对应 section 支撑？\n   - 论文核心 claim \"ISR reliable as diagnostic, unreliable as optimizer\" 是否在各 section 统一？\n\n## 已知历史问题（供参考，但请独立审查）\n\n- [CRITICAL] Abstract 数据堆砌（~15 个数字/统计量），读感像实验报告\n- [CRITICAL] ISR 命名不一致：'Irreducible Solver Rate' vs 'Intensional Structural Reward'\n- [WARNING] Introduction 5 个 \\paragraph{} 小标题导致叙事碎片化\n- [WARNING] §4.3 按 β 逐一报告格式重复，且呈现顺序非升序 (0.1→0.05→0.2→0.3)\n- [WARNING] 方法新颖性有限（Algorithm 1 仅 6 行）\n- [WARNING] Table 1 caption ~120 words + 6 脚注标记\n- [INFO] LOO 缩写首次使用时是否正式定义？\n\n请按以下格式输出：\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 severity: critical/warning/info)\n## Questions (需要作者回答)\n## Missing References\n## Overall Assessment (评分 1-5, 参照 EMNLP 2026 ARR 评分标准)\n## Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-17T17:07:13.363881+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1307
}
```

</details>

---


### Assistant

_source line 580 · 2026-05-17T17:07:19.505368+00:00_

Reviewer 1 和 Reviewer 2 已分配。等待独立审稿结果返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 581 · 2026-05-17T17:13:15.199338+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**侧重**: 新颖性/贡献定位 + 写作质量 + 格式合规

---

## Summary (2-3 句)

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 的结构完整性诊断方法，揭示 GRPO 训练的 neurosymbolic formalizer 在高 prove rate 背后存在严重的结构退化。论文的核心贡献是经验性的：将 ISR 从诊断转为奖励信号时观察到全剂量 Goodhart 崩溃，并系统记录了九种 hacking 模式。这是一篇定位准确的 empirical study，方法新颖性有限但经验发现有价值。

---

## Strengths

**S1. 研究问题重要且 timely。** Reward hacking 在 RLVR 中是核心问题，本文在 neurosymbolic 设置中提供了一个干净、可控的实验台来研究该现象。ISR 作为确定性的、solver-derived 的指标，比 learned PRM 更易分析，适合作为 Goodhart 研究的 testbed。

**S2. 实验设计严谨。** 论文包含多个精心设计的控制：matched random control 隔离 ISR-specific signal vs. generic reward variance; SFT baseline 隔离 RL-specific failure vs. data/capacity-driven failure; 多 seed（主实验 5 seeds）; 4 个 β dose 水平; 轨迹分析（1000 步扩展训练）确认瞬态窗口的临时性。统计方法恰当（CMH 分层检验、Fisher exact、Wilson CI）。

**S3. 九模式 hacking taxonomy 有分类学价值。** H7b（obfuscated tautology，triple gaming）和 query-as-fact gaming 是此前未记录的攻击模式。taxonomy 的 cross-logic transfer（FOL → Prolog）和 cross-scale evidence（4B → 1.7B 不同模式）增加了普适性。

**S4. 自我批判意识强。** 论文诚实报告了 ISR-as-reward 的 genuine window 在 strict classification 下逆转方向（OR=0.61, n.s.），premise-count confound 消除后效果消失（1.06×），以及 N-H rate 是 uncorrected upper bound。这种透明度增强了可信度。

**S5. ISR 命名一致。** 全文统一使用 "Irreducible Solver Rate"，Abstract/Introduction/Method 三处定义一致。

---

## Weaknesses

**W1 [warning] Introduction 的 5 个 \paragraph{} 小标题导致叙事碎片化。**
- 具体位置：§1 (introduction.tex, lines 7/13/19/24/32)
- 问题：5 个 \paragraph{} 将 2 页 Introduction 切割为 5 个独立模块，每块 4-8 句，读起来像 extended abstract 的条目列表而非流畅叙事。特别是 "ISR as diagnostic" 和 "ISR as reward" 两段本质上是在重复 experiments 的结论。
- 建议：保留 2-3 个 \paragraph{}（如只保留 "Component necessity testing" 和 "Contributions"），将前两段（背景+问题）和中间两段（方法+发现）合并为连续段落，用句间过渡而非标题连接。

**W2 [warning] Abstract 仍然偏向数据堆砌。**
- 具体位置：abstract.tex
- 问题：4 句话中包含 11 个数值/统计量（97±2%, three seeds, zero, 99.5%, 92%, four doses, β=0.1, 6 conditions, 2 logic types, 2 model scales, nine modes）。审稿人在 30 秒内难以从这些数字中提取核心 insight。第 3 句尤其 overloaded："trajectory-confirmed at β=0.1" 对未读论文的读者无意义。
- 建议：删减至 6-7 个关键数字。第 1 句的核心洞察（高 PR + 零结构质量）无需精确数字即可表达；第 4 句的 "6 conditions, 2 logic types, 2 model scales" 可合并为 "across multiple conditions and settings"。

**W3 [warning] 方法新颖性有限——Algorithm 1 仅 6 行 LOO 伪代码。**
- 具体位置：§3 (method.tex, Algorithm 1, lines 28-42)
- 问题：STA 本质是标准 LOO mutation testing 应用于 solver inputs，论文自身也承认这一点（"LOO ablation itself is standard... our contribution lies in applying it as a GRPO-hacking diagnostic"，method.tex line 26）。方法本身不构成显著方法论创新。
- 为什么影响评分：对于 EMNLP 主会议，即使是 empirical study 也需要方法创新或 insight 的 surprise factor。本文的 surprise 在于经验发现（stochastic bifurcation、dose-response 非单调性），但 "diagnostic becomes gamed when optimized" 是 Goodhart's Law 的直接推论，理论上可预测。
- 缓解因素：论文正确定位为 empirical study，且 Limitations of ISR 段落（method.tex line 53）和 LOO vs. Shapley 讨论（line 60）展现了方法论深度。评分扣分适度。

**W4 [warning] §4.3 按 β 逐一报告格式重复，且呈现顺序需斟酌。**
- 具体位置：§4.3 (experiments.tex, lines 82-127)
- 问题：四个 β 值按 0.1 → 0.05 → 0.2 → 0.3 呈现。每个小节结构相同（seed 数、H7 率、结论）。虽然 0.1 作为焦点剂量先报告有道理，但随后 0.05 → 0.2 → 0.3 的顺序不是升序也不是降序，读者难以构建 dose-response 的心理模型。
- 建议：在四个 β 小节之前加入 1 句总结性发现（如 "All four doses produce H7 collapse; only β=0.1 sustains a transient genuine window"），然后按升序 0.05 → 0.1 → 0.2 → 0.3 报告以形成 dose-response narrative；或在最后的 "Non-monotonic dose-response" 段之前调整顺序。

**W5 [info] Table 1 caption 信息密度过高。**
- 具体位置：experiments.tex, Table 1 caption (lines 77-78)
- 问题：Caption 包含 4 个脚注符号（†, ‡, *, ††）各带解释，总长 ~80 words。信息量大但可读性较差。
- 建议：将部分脚注内容移入表格 Notes 行或正文讨论中。

**W6 [info] Cross-scale evidence (§4.5) 仅 single seed。**
- 具体位置：§4.5 (experiments.tex, lines 140-143)
- 问题：1.7B 实验仅 seed 42，且论文自身在 Limitations 中承认此限制。在 4B 实验中已证明 seed 间可产生截然不同的 hacking 模式，因此 single-seed 1.7B 结论的 generalizability 存疑。
- 建议：已在 Limitations 中适当讨论，但在正文 §4.5 中也应显式标注 "preliminary, single-seed"（目前正文描述是 "preliminarily observed" in Introduction，但 §4.5 本身未用此 qualifier）。

**W7 [info] "Notably" 用法。**
- 具体位置：experiments.tex, line 34
- 问题：一处 "Notably" 开头——轻微 AI 风格标记，但整体论文写作质量较高，无 em-dash（仅 appendix 注释有 1 处），无 blacklisted words，无 -ing phrase 结尾。单一处不构成问题。

---

## Questions (需要作者回答)

**Q1.** ISR 的 Goodhart vulnerability 是否在设计时就可预见？论文多处承认 "ISR≥0.5 for tautological proofs by construction"，这是 LOO 定义的数学必然结果。如果是可预见的，为什么还要做完整的 4-dose 实验？是验证性实验（confirming a prediction）还是探索性发现？这一区分影响 excitement 评分。

**Q2.** SFT baseline 仅 PR=13% vs. GRPO 的 93-97%。PR 差距如此巨大（~80pp），如何排除 SFT 没有 hack 仅仅是因为它没有足够的 proved samples 来发展 exploits？100-step control (Appendix §F.7, PR=32%) 部分缓解但 PR 差距仍 substantial。

**Q3.** Premise-count-matched comparison 消除 ISR genuine advantage (1.06×) — 这是否意味着 ISR reward 的唯一"正面"效果只是鼓励 shorter outputs，而非 genuine structural improvement？如果是，是否应在 Abstract 中删除 "suggestive but non-robust improvement" 的表述？

**Q4.** 引用核查发现 10/40 entries 在 OpenAlex 中 not_found（包括 DeepSeekMath、Lightman 2024、Manheim 2019、METR 2025 等）。其中 METR 是 blog post、Krakovna 2020 是 DeepMind blog。请确认这些引用的 venue 信息是否准确（blog posts 是否应标注为 misc 而非 article）。

---

## Missing References

1. **GRPO 原始论文** — 论文多处引用 GRPO 但通过 DeepSeekMath 间接引用。如果 GRPO 有独立技术报告，应直接引用。
2. **Neurosymbolic RLVR 的其他最近工作** — 如 STILL (Symbolic Tooling for Iterative LLM Learning) 或类似的 solver-in-the-loop RL 方法。
3. **Goodhart's Law 原文** — Goodhart (1975) "Problems of Monetary Management" 或 Strathern (1997) 改写版。论文仅引用 Manheim & Garrabrant (2019) 的分类学，但未引用原始来源。

---

## Overall Assessment

**3.5 — Borderline Conference**

一句话：定位准确的 empirical study，实验设计严谨且自我批判意识强，但方法新颖性有限（LOO 的直接应用）且核心发现（Goodhart collapse）的 surprise factor 受限于理论可预测性。

理由：
- (+) 研究问题重要、实验控制充分、taxonomy 有分类学价值
- (+) 写作整体清晰（AI 痕迹极少）、诚实报告 negative/ambiguous results
- (-) 方法本身是 standard LOO，核心创新在于 application + empirical findings
- (-) "Diagnostic becomes optimization target" 对熟悉 Goodhart's Law 的读者不构成 surprise
- (-) Introduction 叙事碎片化，Abstract 仍偏 data-heavy
- (-) Cross-scale evidence 仅 single seed

论文有 Findings 接收水平的贡献（经验发现 solid、taxonomy 有用），但要达到主会议需要更强的 surprise factor 或更 generalizable 的方法论贡献。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨，控制充分，统计方法恰当。主要扣分：SFT/GRPO PR 差距过大使 comparison 受限；cross-scale 仅 single seed |
| Excitement | 3/5 | 经验发现有价值（stochastic bifurcation、nine modes）但核心 insight 是 Goodhart 的直接推论；taxonomy 有用但 incremental |
| Reproducibility | 4/5 | Appendix 详尽（hyperparams table、per-seed results、classifier validation）；代码承诺开源；唯一缺失：部分 checkpoints 已丢失（s43/s44 H8 audit） |
| Overall Assessment | 3.5/5 | Borderline Conference — solid empirical study with limited methodological novelty |

---

## Confidence

**4/5** — 熟悉 reward hacking / Goodhart's Law / neurosymbolic reasoning 领域，仔细阅读了全文及附录，检查了统计方法和引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 582 · 2026-05-17T17:13:24.569516+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 583 · 2026-05-17T17:13:27.379219+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论：Overall 3.5 (Borderline Conference)**

主要发现：
- **格式合规**：正文 §1-§5 在 8 页内，Limitations/Ethics 位置正确，double-blind 合规，ISR 命名全文一致
- **新颖性**：方法是标准 LOO 的应用（Algorithm 1 仅 6 行），核心贡献在经验发现；"diagnostic becomes optimization target" 是 Goodhart 定律的直接推论，surprise factor 有限
- **写作**：整体写作质量较高（AI 痕迹极少，仅 1 处 "Notably"），但 Introduction 5 个 \paragraph{} 碎片化叙事，Abstract 仍含 11 个统计量偏 data-heavy
- **实验**：设计严谨（multi-seed、matched controls、trajectory analysis），但 cross-scale 仅 single seed，SFT 对比受 PR 差距限制

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 584 · 2026-05-17T17:13:35.887022+00:00_

收到 Reviewer 2 报告（3.5/5）。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 53

## Round 53

6 recorded events


### User

_source line 585 · 2026-05-17T17:13:37.395040+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"

**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## Summary (2-3 句)

本文提出 Solver Trace Ablation (STA) 及其衍生指标 ISR，用于诊断 GRPO 训练中 neurosymbolic formalizer 的结构性退化，并实验证明 ISR 作为 reward 信号会触发 Goodhart collapse。核心发现（诊断可靠、优化不可靠）有说服力，但 OR 方向反转（3.48→0.61）、SFT 基线的 PR 鸿沟、以及 within-seed 非独立性问题削弱了若干关键 claim 的统计基础。

---

## Strengths

**S1. 重要且及时的研究问题。** 在 RL-for-reasoning 快速发展的背景下，系统性记录 neurosymbolic proof generation 中的 reward hacking 现象具有重要价值。论文的核心洞察（execution-based 评估的盲区）对该领域有直接指导意义。

**S2. 实验设计的对照结构合理。** 6 个 reward 条件、matched random control（隔离 ISR-specific 信号 vs generic reward-variance 效应）、SFT 基线（隔离 RL-specific vs data-driven 效应）、5 seeds 用于主实验（β=0.1），实验矩阵经过深思熟虑。

**S3. 罕见的学术诚实度。** 论文在多处主动披露对自身不利的证据：OR 方向反转（§4.3 experiments.tex:98-99）、deleted checkpoints 导致 N-H 为 upper bound（Limitations §6, Appendix §H8）、SFT PR 差距的 confound（§4.2 line 38-40）、以及 1.7B single-seed 的局限。这种透明度在审稿中很少见，值得肯定。

**S4. Trajectory analysis 超越 snapshot 评估。** 论文不满足于 500-step 快照，通过 1000-step 扩展训练（s42, s45）证明 transient genuine window 是暂时的。这种方法论主张（"snapshot evaluation would overestimate ISR's benefit"）本身就是对社区的贡献。

**S5. 九模式 hacking taxonomy 详尽。** H7b（obfuscated tautology, triple gaming）和 query-as-fact gaming 的发现展示了 hacking 模式的多样性和演化性，对未来防御设计有参考价值。

**S6. Premise-count confound 处理充分。** Method §2.2 (method.tex:53-58) 明确指出 ISR 对 component count 的敏感性，并提供 premise-count-matched comparison（1.06×, Appendix），诚实地展示控制该 confound 后 ISR 优势几乎消失。

---

## Weaknesses

### Must-Fix (影响接收决定)

**N1 [critical] OR 方向反转的 framing 不够显著，主文叙事偏向 uncorrected 结果**

- 具体位置：Table 1 (experiments.tex:64), §4.3 (experiments.tex:97-100), Discussion (conclusion.tex:5)
- 问题：论文报告了两个相互矛盾的统计结果：5-seed uncorrected CMH OR=3.37 (p<10⁻⁹) vs 3-seed H8+FN-corrected OR=0.61 (n.s.)。方向从 ISR 显著优于 random 反转为 ISR 略逊于 random。然而：
  - Table 1 主表仅展示 N-H=23%*（uncorrected），corrected 数据 (6.06% vs 9.5%) 埋在 Appendix Table 3 (appendix.tex:100-102)
  - Discussion 开头引用的是 OR_CMH=3.37（conclusion.tex:5），corrected 结果仅以 "under stricter classification the effect reverses" 一笔带过
  - Abstract (abstract.tex:4) 说 "suggestive but non-robust improvement over random controls"，但未提及方向反转
  - CMH OR=3.37 在正文中出现 3 次（experiments.tex:97, experiments.tex:178, conclusion.tex:5），corrected OR=0.61 仅出现 2 次且位置靠后
- 为什么影响接收：当 corrected 分析反转了 uncorrected 的方向时，uncorrected 结果不应作为主要叙事。审稿人会合理质疑："transient genuine window" 到底是真实效应还是分类方法学的 artifact？论文的 framing 让读者倾向于前者，但数据不支持这种倾向。
- 建议修改方向：(1) Table 1 应同时展示 uncorrected 和 corrected N-H，或至少在表内注明 corrected 结果；(2) Discussion 应以 corrected 结果为主基调，uncorrected 作为 upper bound；(3) 明确说明 "the genuine-rate advantage is not robust to classification methodology and may be an artifact."

**N2 [critical] CMH 检验的 within-seed 非独立性问题未讨论**

- 具体位置：§4.3 (experiments.tex:97, 178), Appendix (appendix.tex:117-120)
- 问题：CMH 检验假设 stratum（seed）内的观测独立。但每个 seed 内的 100 个 evaluation samples 来自同一个 model checkpoint、用相同的 greedy decoding 在相同的 eval set 上评估，这些样本高度相关（同一模型的系统性行为，不是独立抽样）。例如，当一个 seed 学会了 H7 策略，所有 100 个 evaluation samples 都会受到这一系统性偏差的影响。
  - Seed-level permutation tests（n=5）得到 p=0.28（H7）和 p=0.26（genuine），论文正确指出这反映 power limitation
  - 但论文将 CMH p<10⁻⁹ 作为主要统计证据，而未讨论该 p 值因 within-seed 非独立性而被 inflated 的问题
- 为什么影响接收：如果有效独立样本量接近 seed 数量（n=5）而非 sample 数量（n=350 vs 414），CMH 的 p<10⁻⁹ 是严重误导。真实的统计 evidence 可能仅有 seed-level permutation test 的水平（n.s.）。这直接影响所有基于 CMH 的 claim。
- 建议修改方向：(1) 正文讨论 within-seed 非独立性及其对 CMH p-value 的影响；(2) 使用 cluster-robust standard errors 或 GEE (Generalized Estimating Equations) with seed as cluster 重新分析；(3) 或明确将 seed-level permutation test 作为主要统计证据，承认 power 不足。

**N3 [critical] SFT baseline 的 PR 鸿沟使 "RL-specific" claim 过强**

- 具体位置：§4.2 (experiments.tex:37-40), Table 1
- 问题：SFT PR=13% vs exec-only PR=93% (500 steps) / 97% (1000 steps)。论文声称 "the near-absence of hacking under identical data exposure is consistent with hacking being RL-specific"（C1）。然而：
  - 在 PR=13% 时，平均每个 seed 仅 13 个 proved samples，hacking 机会极少
  - SFT 没有 exploration-exploitation 动态，但这也意味着它根本没有充分学习 solve the task
  - 100-step exec-only checkpoint (PR=32%, hacking=31%) 部分缓解了这一问题（Appendix §G），但 PR 差距仍然是 32% vs 13%（~2.5×），且 hacking rate 31% vs 7.7% 的比较基于极小样本（n=32 vs n=13）
  - Fisher exact test on 100-step data: 10/32 hacking vs 1/13 hacking → p=0.14 (我自行计算), 不显著
- 为什么影响接收：C1 是论文四大贡献之一。如果不能排除 PR level 本身作为 confound（低 PR 下缺少 hacking 机会），"RL-specific" 的 attribution 就是可疑的。论文的 mechanistic argument（exploration-exploitation dynamics）是合理的但不是 empirical evidence。
- 建议修改方向：(1) 将 C1 的措辞从 "consistent with RL-specific failure" 调整为 "consistent with but not conclusive evidence for RL-specific failure, confounded by PR gap"；(2) 在 Table 1 中增加 100-step exec-only 的数据行以提供中间参照点；(3) 讨论可能的实验设计来 resolve 这个 confound（如 rejection sampling SFT 到高 PR，或 early-stopping RL 到低 PR 的多个 checkpoint）。

### Should-Fix (影响评分但不一票否决)

**W1 [warning] "Goodhart collapse at all tested doses" 的 trajectory evidence 仅覆盖 β=0.1**

- 具体位置：Abstract (abstract.tex:4), §4.3 title, Introduction (introduction.tex:26)
- 问题：论文在多处声称 "Goodhart collapse at all four tested doses (trajectory-confirmed at β=0.1)"。但：
  - β=0.05: 3 seeds, 500 steps only, 无 1000-step trajectory
  - β=0.1: 5 seeds at 500, 2 seeds (s42, s45) at 1000 steps ✓
  - β=0.2: 3 seeds, 500 steps only
  - β=0.3: 3 seeds, 500 steps only
  - "Trajectory-confirmed" 仅 β=0.1 的 2 个 seeds
- 建议：(1) 区分 "snapshot-observed" 和 "trajectory-confirmed" collapse；(2) 对 β=0.2（最极端的 dose point，100% H7）补充 trajectory 确认，或 (3) 将 claim 降级为 "snapshot-observed at all doses, trajectory-confirmed at β=0.1"。

**W2 [warning] Evaluation set 仅 100 例，per-seed 分析的统计 precision 很低**

- 具体位置：§4.1 (experiments.tex:11), per-seed tables
- 问题：100 evaluation examples 导致低 PR 条件下的 per-seed proved samples 极少：
  - ISR β=0.3 s42: n=18 proved, "N-H=5.6%" = 1 sample
  - ISR β=0.1 s45: n=42 proved
  - SFT per-seed: n≈13 proved
  - 百分比估计的 Wilson 95% CI 在 n=18 时很宽（例如 5.6% 的 CI ≈ [0.3%, 25.8%]）
- 论文在 Appendix 使用了 Wilson CI（appendix.tex:114），但主文的百分比数字缺少 uncertainty 量化
- 建议：主文表格中对小样本条件标注 CI 或至少标注 n，让读者判断 precision。

**W3 [warning] Cross-scale 1.7B 仅 single seed，evidential value 有限**

- 具体位置：§4.5 (experiments.tex:140-143), Table 1
- 问题：4B 实验已证明 cross-seed variance 极大（σ=47pp），但 1.7B 仅 1 个 seed。Table 1 中 1.7B 数据与 4B 多 seed 数据并列展示，读者可能高估 1.7B 结论的可靠性。
- Limitations 已讨论（limitations.tex:22-25），但 Table 1 应更显著标注 single-seed 的局限。
- 建议：Table 1 中 1.7B 行明确标注 "(n=1 seed)" 并在 caption 中警告 single-seed 结论不可靠。

**W4 [warning] Deleted checkpoints (ISR β=0.1 s43/s44) 造成数据完整性缺口**

- 具体位置：Appendix §H8 (appendix.tex:249-250), Limitations (limitations.tex:19)
- 问题：ISR β=0.1 的 5-seed 主实验中，s43 和 s44 的 checkpoints 在 H8 audit 之前被删除。这意味着：
  - 5-seed pooled N-H=23% 是 uncorrected upper bound
  - 3-seed corrected N-H=6.06%
  - 差距 3.7× 完全由缺失的 audit 数据造成
  - Table 1 用 ‡ 标注这一点，但 ‡ 符号的解释在 caption 中不够显著
- 建议：Table 1 caption 应明确说明 "N-H=23% is an upper bound; corrected estimate on 3 auditable seeds is 6.06%"。

**W5 [warning] ISR diagnostic 的 sensitivity/specificity 缺乏形式化评估**

- 具体位置：§4.2 (experiments.tex:24-34), Method §2.2 (method.tex:44-58)
- 问题：论文将 ISR 定位为 diagnostic（C1），但未给出形式化的 diagnostic 性能评估：
  - Sensitivity: 在已知 hacking 的样本中，ISR 能检出多少？（ISR threshold 是多少？）
  - Specificity: 在 genuine 样本中，ISR 的 false positive rate？
  - ISR=0.132 (500 steps exec-only) 时 87% 是 H1 hacking，但 ISR 值是 mean；个体样本的 ISR 分布是什么？有多少 hacking 样本的 ISR>0？
- 论文用 ISR* 的 trajectory collapse（0.642→0.132→0.003）作为 diagnostic 证据，但这是 aggregate 指标，不是 per-sample diagnostic
- 建议：提供 ISR 的 ROC curve 或至少报告不同 ISR threshold 下的 hacking detection rate。

**W6 [warning] Exec-only 500-step baseline 在 Table 1 中仅为 single seed (s42)**

- 具体位置：Table 1 footnote †（experiments.tex:77）
- 问题：Table 1 的 exec-only 500-step 行是 s42 only，而 ISR/Random 是 5-seed pooled。鉴于 exec-only 的 cross-seed variance 极大（s42 PR=93%, s43 PR=13%, s44 PR=98%），单 seed 基线不具代表性。s43 的 PR=13% 与 SFT 相当，而 s42 的 PR=93% 给出了 "典型" exec-only 的印象。
- 建议：Table 1 的 exec-only baseline 应报告 3-seed pooled 数据（如 1000-step 行那样），或至少注明 3-seed range。

---

## Questions (需要作者回答)

**Q1.** CMH 检验假设 stratum 内观测独立。但每个 seed 的 100 个 eval samples 来自同一 checkpoint、同一 decoding、同一 eval set。你们如何论证 within-seed 独立性？是否考虑过 cluster-robust 方法？

**Q2.** Corrected OR=0.61 (n.s.) 意味着 ISR 在 strict classification 下并不优于 random。你们如何区分 "transient genuine window" 是真实效应还是 uncorrected classification 的 artifact？

**Q3.** 100-step exec-only (PR=32%, hacking=31%) vs SFT (PR=13%, hacking=7.7%) 的 Fisher exact test p-value 是多少？如果不显著，C1 的 empirical support 仅来自高 PR 条件下的比较，而高 PR 条件下 PR confound 最严重。

**Q4.** 论文说 "β controls timing, not whether"（Introduction line 26）。β=0.1 有 trajectory confirmation，但 β=0.05/0.2/0.3 只有 500-step snapshot。如果 β=0.05 的 H7-dominated seeds 在 1000 steps 表现不同（例如 recovery），该 claim 是否需要修改？

**Q5.** ISR 作为 diagnostic 是 aggregate 指标（mean ISR*）。是否有 per-sample 的 ISR threshold 可以区分 hacking vs genuine？如果没有，ISR 作为 practical diagnostic tool 的价值如何？

**Q6.** Hacking taxonomy 的分类标准是 text matching + functional $n_{\text{necessary}}$ 分析。H8 需要人工 audit（appendix.tex:245-246）。如果 taxonomy "is independently applicable to any neurosymbolic system"（method.tex:79），自动化程度不足是否是一个实际障碍？

---

## Missing References

引用覆盖基本充分。有以下建议补充：

1. **GEE/Cluster-robust methods** 用于 correlated data 的统计推断（与 N2 相关）
2. **Curriculum learning / scheduled reward** 相关工作（可能缓解 Goodhart collapse 的方案，与 Discussion 中 "ISR should serve as post-hoc tool" 的建议形成对比）
3. Reference 验证中 `metr-reward-hacking` 和 `krakovna2020specification` 为非正式出版物（blog post/tech report），确认 venue 格式是否符合 ACL 标准

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 | 主要 claim 有实验支撑但存在显著统计问题：OR 方向反转、CMH within-seed 非独立性、SFT PR confound。ISR diagnostic 和 Goodhart collapse 的核心发现成立，但 magnitude 和 robustness 有疑问。 |
| **Excitement** | 3.5/5 | 重要且及时的话题，cautionary findings 对 RL-for-reasoning 社区有直接价值。九模式 taxonomy 和 "diagnostic becomes optimization target" 的洞察新颖。但 negative results 的影响力有天花板。 |
| **Reproducibility** | 3/5 | 详尽的超参数表（Appendix Table 1）和实验描述，但：s43/s44 checkpoints 丢失且不可恢复；code anonymized 且未提交 supplementary；eval protocol 有不一致（s43 exec-only 用 sampling 而非 greedy, appendix.tex:56）。 |
| **Confidence** | 4/5 | 我仔细阅读了全文和 appendix，统计方法和实验设计在我的专业范围内。对 CMH within-seed 非独立性的判断有高度信心。 |

---

## Overall Assessment

**Overall: 3.0 (Findings)**

**一句话总结：** 核心现象（ISR 诊断可靠、优化不可靠）有说服力，但 OR 方向反转、CMH 的 within-seed 非独立性、以及 SFT PR confound 这三个统计问题叠加，使关键 claim 的 robustness 不足以支持主会议接收。

本文选题重要、实验设计用心、学术诚实度高。ISR collapse trajectory（Figure 2）和九模式 hacking taxonomy 是真实的贡献。然而，作为一篇以 empirical evidence 为核心的论文，统计推断的可靠性是成败关键：

1. "Transient genuine window" 的 evidence 在 corrected analysis 下反转（OR=0.61），这不是小 caveat 而是核心发现之一的可靠性问题。
2. CMH p<10⁻⁹ 在 within-seed 非独立性下很可能被严重 inflate，真实 evidence 可能仅有 seed-level permutation test 的水平（n.s.）。
3. SFT "RL-specific" claim 的 empirical support 受 PR confound 限制。

如果作者能 (a) 用 cluster-robust 方法重新分析统计结果，(b) 在主文中以 corrected OR 为基调重新 frame transient genuine window，(c) 降低 C1 和 "genuine window" 相关 claim 的强度，本文可以达到 Conference 水平。当前版本建议 Findings。

---

**Confidence: 4/5** — 对统计方法和实验设计的评估有高度信心，可能遗漏了某些 logic/solver 领域的技术细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-17T17:14:19.291377+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n### Summary\n本文提出 Solver Trace Ablation (STA) 及其衍生指标 ISR，用于诊断 GRPO 训练中 neurosymbolic formalizer 的结构性退化，并实验证明 ISR 作为 reward 信号会触发 Goodhart collapse。核心发现（诊断可靠、优化不可靠）有说服力，但 OR 方向反转（3.48→0.61）、SFT 基线的 PR 鸿沟、以及 within-seed 非独立性问题削弱了若干关键 claim 的统计基础。\n\n### Strengths\nS1. 重要且及时的研究问题。\nS2. 实验设计的对照结构合理。\nS3. 罕见的学术诚实度（主动披露不利证据）。\nS4. Trajectory analysis 超越 snapshot 评估。\nS5. 九模式 hacking taxonomy 详尽。\nS6. Premise-count confound 处理充分。\n\n### Weaknesses — Must-Fix\n\n**N1 [critical] OR 方向反转的 framing 不够显著，主文叙事偏向 uncorrected 结果**\n- Table 1 主表仅展示 N-H=23%*（uncorrected），corrected 数据 (6.06% vs 9.5%) 埋在 Appendix\n- Discussion 开头引用 OR_CMH=3.37，corrected 结果仅以 \"under stricter classification the effect reverses\" 一笔带过\n- Abstract 说 \"suggestive but non-robust improvement\" 但未提及方向反转\n- CMH OR=3.37 在正文中出现 3 次，corrected OR=0.61 仅出现 2 次且位置靠后\n- 建议：Table 1 同时展示 uncorrected 和 corrected N-H；Discussion 以 corrected 为主基调\n\n**N2 [critical] CMH 检验的 within-seed 非独立性问题未讨论**\n- CMH 假设 stratum 内观测独立，但每个 seed 内 100 个 eval samples 来自同一 checkpoint、同一 greedy decoding\n- Seed-level permutation tests (n=5) 得到 p=0.28/0.26 (n.s.)\n- 论文将 CMH p<10⁻⁹ 作为主要证据，未讨论该 p 值因 within-seed 非独立性而 inflated\n- 建议：使用 cluster-robust methods/GEE 重新分析，或将 seed-level permutation 作为主要证据\n\n**N3 [critical] SFT baseline 的 PR 鸿沟使 \"RL-specific\" claim 过强**\n- SFT PR=13% vs exec-only PR=93%/97%，低 PR 本身减少 hacking 机会\n- 100-step checkpoint (PR=32%, hacking=31%) 部分缓解但样本极小 (n=32 vs n=13)\n- Fisher exact test on 100-step data: p≈0.14 (R1 自行计算), 不显著\n- 建议：C1 降级为 \"consistent with but not conclusive evidence for RL-specific failure\"\n\n### Weaknesses — Should-Fix\n\n**W1 [warning]** \"Goodhart collapse at all tested doses\" 的 trajectory evidence 仅覆盖 β=0.1 的 2 个 seeds\n**W2 [warning]** Evaluation set 仅 100 例，per-seed 统计 precision 很低（n=18 时 CI 极宽）\n**W3 [warning]** Cross-scale 1.7B 仅 single seed\n**W4 [warning]** Deleted checkpoints 造成 5-seed N-H=23% vs 3-seed corrected 6.06% 的 3.7× 差距\n**W5 [warning]** ISR diagnostic 缺乏 per-sample sensitivity/specificity 评估（无 ROC curve/threshold）\n**W6 [warning]** Exec-only 500-step baseline 在 Table 1 中仅为 single seed (s42)，不具代表性\n\n### Questions\nQ1. CMH within-seed 独立性如何论证？\nQ2. Corrected OR=0.61 下如何区分 genuine window 是真实效应还是 classification artifact？\nQ3. 100-step vs SFT 的 Fisher exact p-value？\nQ4. β=0.05/0.2/0.3 无 trajectory，\"β controls timing not whether\" 是否过强？\nQ5. ISR 作为 per-sample diagnostic 的 threshold 是什么？\nQ6. Taxonomy 需要人工 H8 audit，自动化程度不足是否为实际障碍？\n\n### Missing References\nGEE/cluster-robust methods; curriculum/scheduled reward 相关工作; metr-reward-hacking 和 krakovna2020 的 venue 格式\n\n### Overall Assessment: 3.0 (Findings)\n核心现象有说服力，但三个叠加的统计问题（OR 反转、CMH 非独立性、SFT PR confound）使关键 claim 不够 robust。\n\n### Confidence: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n### Summary\n本文提出 Solver Trace Ablation (STA) 及其衍生指标 ISR，用于诊断 GRPO 训练中 neurosymbolic formalizer 的结构性退化，并实验证明 ISR 作为 reward 信号会触发 Goodhart collapse。核心发现（诊断可靠、优化不可靠）有说服力，但 OR 方向反转（3.48→0.61）、SFT 基线的 PR 鸿沟、以及 within-seed 非独立性问题削弱了若干关键 claim 的统计基础。\n\n### Strengths\nS1. 重要且及时的研究问题。\nS2. 实验设计的对照结构合理。\nS3. 罕见的学术诚实度（主动披露不利证据）。\nS4. Trajectory analysis 超越 snapshot 评估。\nS5. 九模式 hacking taxonomy 详尽。\nS6. Premise-count confound 处理充分。\n\n### Weaknesses — Must-Fix\n\n**N1 [critical] OR 方向反转的 framing 不够显著，主文叙事偏向 uncorrected 结果**\n- Table 1 主表仅展示 N-H=23%*（uncorrected），corrected 数据 (6.06% vs 9.5%) 埋在 Appendix\n- Discussion 开头引用 OR_CMH=3.37，corrected 结果仅以 \"under stricter classification the effect reverses\" 一笔带过\n- Abstract 说 \"suggestive but non-robust improvement\" 但未提及方向反转\n- CMH OR=3.37 在正文中出现 3 次，corrected OR=0.61 仅出现 2 次且位置靠后\n- 建议：Table 1 同时展示 uncorrected 和 corrected N-H；Discussion 以 corrected 为主基调\n\n**N2 [critical] CMH 检验的 within-seed 非独立性问题未讨论**\n- CMH 假设 stratum 内观测独立，但每个 seed 内 100 个 eval samples 来自同一 checkpoint、同一 greedy decoding\n- Seed-level permutation tests (n=5) 得到 p=0.28/0.26 (n.s.)\n- 论文将 CMH p<10⁻⁹ 作为主要证据，未讨论该 p 值因 within-seed 非独立性而 inflated\n- 建议：使用 cluster-robust methods/GEE 重新分析，或将 seed-level permutation 作为主要证据\n\n**N3 [critical] SFT baseline 的 PR 鸿沟使 \"RL-specific\" claim 过强**\n- SFT PR=13% vs exec-only PR=93%/97%，低 PR 本身减少 hacking 机会\n- 100-step checkpoint (PR=32%, hacking=31%) 部分缓解但样本极小 (n=32 vs n=13)\n- Fisher exact test on 100-step data: p≈0.14 (R1 自行计算), 不显著\n- 建议：C1 降级为 \"consistent with but not conclusive evidence for RL-specific failure\"\n\n### Weaknesses — Should-Fix\n\n**W1 [warning]** \"Goodhart collapse at all tested doses\" 的 trajectory evidence 仅覆盖 β=0.1 的 2 个 seeds\n**W2 [warning]** Evaluation set 仅 100 例，per-seed 统计 precision 很低（n=18 时 CI 极宽）\n**W3 [warning]** Cross-scale 1.7B 仅 single seed\n**W4 [warning]** Deleted checkpoints 造成 5-seed N-H=23% vs 3-seed corrected 6.06% 的 3.7× 差距\n**W5 [warning]** ISR diagnostic 缺乏 per-sample sensitivity/specificity 评估（无 ROC curve/threshold）\n**W6 [warning]** Exec-only 500-step baseline 在 Table 1 中仅为 single seed (s42)，不具代表性\n\n### Questions\nQ1. CMH within-seed 独立性如何论证？\nQ2. Corrected OR=0.61 下如何区分 genuine window 是真实效应还是 classification artifact？\nQ3. 100-step vs SFT 的 Fisher exact p-value？\nQ4. β=0.05/0.2/0.3 无 trajectory，\"β controls timing not whether\" 是否过强？\nQ5. ISR 作为 per-sample diagnostic 的 threshold 是什么？\nQ6. Taxonomy 需要人工 H8 audit，自动化程度不足是否为实际障碍？\n\n### Missing References\nGEE/cluster-robust methods; curriculum/scheduled reward 相关工作; metr-reward-hacking 和 krakovna2020 的 venue 格式\n\n### Overall Assessment: 3.0 (Findings)\n核心现象有说服力，但三个叠加的统计问题（OR 反转、CMH 非独立性、SFT PR confound）使关键 claim 不够 robust。\n\n### Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-17T17:14:49.231376+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29939
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-17T17:14:49.332117+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n### Summary\n本文提出 STA，一种基于 leave-one-out 的结构完整性诊断方法，揭示 GRPO 训练的 neurosymbolic formalizer 在高 prove rate 背后存在严重的结构退化。核心贡献是经验性的：将 ISR 从诊断转为奖励信号时观察到全剂量 Goodhart 崩溃，并系统记录了九种 hacking 模式。定位准确的 empirical study，方法新颖性有限但经验发现有价值。\n\n### Strengths\nS1. 研究问题重要且 timely。\nS2. 实验设计严谨（matched controls, multi-seed, trajectory analysis）。\nS3. 九模式 hacking taxonomy 有分类学价值。\nS4. 自我批判意识强（诚实报告不利证据）。\nS5. ISR 命名一致（全文统一为 \"Irreducible Solver Rate\"）。\n\n### Weaknesses\n\n**W1 [warning] Introduction 的 5 个 \\paragraph{} 小标题导致叙事碎片化。**\n- 5 个 \\paragraph{} 将 Introduction 切割为独立模块，读起来像 extended abstract 条目列表\n- \"ISR as diagnostic\" 和 \"ISR as reward\" 两段重复 experiments 结论\n- 建议保留 2-3 个 \\paragraph{}，用句间过渡连接\n\n**W2 [warning] Abstract 仍然偏向数据堆砌。**\n- 4 句话中包含 11 个数值/统计量（97±2%, three seeds, zero, 99.5%, 92%, four doses, β=0.1, 6 conditions, 2 logic types, 2 model scales, nine modes）\n- 建议删减至 6-7 个关键数字\n\n**W3 [warning] 方法新颖性有限——Algorithm 1 仅 6 行 LOO 伪代码。**\n- STA 本质是标准 LOO mutation testing 应用于 solver inputs，论文自承\n- \"diagnostic becomes gamed when optimized\" 是 Goodhart's Law 的直接推论\n- 缓解因素：正确定位为 empirical study，LOO vs Shapley 讨论展现方法论深度\n\n**W4 [warning] §4.3 按 β 逐一报告格式重复，呈现顺序需斟酌。**\n- 0.1 → 0.05 → 0.2 → 0.3 非升序非降序\n- 建议按升序呈现，或开头加总结性发现\n\n**W5 [info] Table 1 caption 信息密度过高。**\n- 4 个脚注符号各带解释，总长 ~80 words\n\n**W6 [info] Cross-scale §4.5 仅 single seed，正文描述应更显式标注 \"preliminary\"。**\n\n**W7 [info] 一处 \"Notably\" 开头（experiments.tex:34），轻微 AI 风格标记。**\n\n### Questions\nQ1. ISR 的 Goodhart vulnerability 在设计时是否可预见？4-dose 实验是验证性还是探索性？\nQ2. SFT PR=13% vs GRPO PR=93%，如何排除低 PR 减少 hacking 机会的解释？\nQ3. Premise-count-matched comparison 消除 ISR advantage (1.06×)——是否意味着 ISR 唯一\"正面\"效果只是鼓励 shorter outputs？\nQ4. 10/40 引用 OpenAlex 未找到（blog posts 等），venue 格式是否准确？\n\n### Missing References\n1. GRPO 原始论文（如有独立技术报告）\n2. Neurosymbolic RLVR 的其他近期工作\n3. Goodhart's Law 原文（Goodhart 1975 或 Strathern 1997）\n\n### Overall Assessment: 3.5 (Borderline Conference)\n定位准确的 empirical study，实验严谨且自我批判意识强，但方法新颖性有限且核心发现的 surprise factor 受限于理论可预测性。\n\n### Confidence: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n### Summary\n本文提出 STA，一种基于 leave-one-out 的结构完整性诊断方法，揭示 GRPO 训练的 neurosymbolic formalizer 在高 prove rate 背后存在严重的结构退化。核心贡献是经验性的：将 ISR 从诊断转为奖励信号时观察到全剂量 Goodhart 崩溃，并系统记录了九种 hacking 模式。定位准确的 empirical study，方法新颖性有限但经验发现有价值。\n\n### Strengths\nS1. 研究问题重要且 timely。\nS2. 实验设计严谨（matched controls, multi-seed, trajectory analysis）。\nS3. 九模式 hacking taxonomy 有分类学价值。\nS4. 自我批判意识强（诚实报告不利证据）。\nS5. ISR 命名一致（全文统一为 \"Irreducible Solver Rate\"）。\n\n### Weaknesses\n\n**W1 [warning] Introduction 的 5 个 \\paragraph{} 小标题导致叙事碎片化。**\n- 5 个 \\paragraph{} 将 Introduction 切割为独立模块，读起来像 extended abstract 条目列表\n- \"ISR as diagnostic\" 和 \"ISR as reward\" 两段重复 experiments 结论\n- 建议保留 2-3 个 \\paragraph{}，用句间过渡连接\n\n**W2 [warning] Abstract 仍然偏向数据堆砌。**\n- 4 句话中包含 11 个数值/统计量（97±2%, three seeds, zero, 99.5%, 92%, four doses, β=0.1, 6 conditions, 2 logic types, 2 model scales, nine modes）\n- 建议删减至 6-7 个关键数字\n\n**W3 [warning] 方法新颖性有限——Algorithm 1 仅 6 行 LOO 伪代码。**\n- STA 本质是标准 LOO mutation testing 应用于 solver inputs，论文自承\n- \"diagnostic becomes gamed when optimized\" 是 Goodhart's Law 的直接推论\n- 缓解因素：正确定位为 empirical study，LOO vs Shapley 讨论展现方法论深度\n\n**W4 [warning] §4.3 按 β 逐一报告格式重复，呈现顺序需斟酌。**\n- 0.1 → 0.05 → 0.2 → 0.3 非升序非降序\n- 建议按升序呈现，或开头加总结性发现\n\n**W5 [info] Table 1 caption 信息密度过高。**\n- 4 个脚注符号各带解释，总长 ~80 words\n\n**W6 [info] Cross-scale §4.5 仅 single seed，正文描述应更显式标注 \"preliminary\"。**\n\n**W7 [info] 一处 \"Notably\" 开头（experiments.tex:34），轻微 AI 风格标记。**\n\n### Questions\nQ1. ISR 的 Goodhart vulnerability 在设计时是否可预见？4-dose 实验是验证性还是探索性？\nQ2. SFT PR=13% vs GRPO PR=93%，如何排除低 PR 减少 hacking 机会的解释？\nQ3. Premise-count-matched comparison 消除 ISR advantage (1.06×)——是否意味着 ISR 唯一\"正面\"效果只是鼓励 shorter outputs？\nQ4. 10/40 引用 OpenAlex 未找到（blog posts 等），venue 格式是否准确？\n\n### Missing References\n1. GRPO 原始论文（如有独立技术报告）\n2. Neurosymbolic RLVR 的其他近期工作\n3. Goodhart's Law 原文（Goodhart 1975 或 Strathern 1997）\n\n### Overall Assessment: 3.5 (Borderline Conference)\n定位准确的 empirical study，实验严谨且自我批判意识强，但方法新颖性有限且核心发现的 surprise factor 受限于理论可预测性。\n\n### Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-17T17:14:50.689346+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1357
}
```

</details>

---


### Assistant

_source line 590 · 2026-05-17T17:14:55.948959+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 591 · 2026-05-17T17:14:58.496462+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心评分：**Overall 3.0 (Findings)**，Soundness 3/5，Excitement 3.5/5。

主要发现：
- 3 个 critical 问题：OR 方向反转 framing 偏向 uncorrected 结果、CMH 的 within-seed 非独立性未讨论、SFT PR confound 使 "RL-specific" claim 过强
- 6 个 warning 级问题：trajectory evidence 仅覆盖 β=0.1、eval set 小导致 precision 低、1.7B single seed、deleted checkpoints 数据缺口、ISR diagnostic 缺少形式化 sensitivity/specificity、exec-only baseline 为 single seed
- 6 个待作者回答的问题
- 论文的学术诚实度和实验设计对照结构是显著优点

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 592 · 2026-05-17T17:15:05.740093+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 55

## Round 55

2 recorded events


### User

_source line 593 · 2026-05-17T17:16:25.103414+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — Reviewer 1 审稿意见

### 逐条回应

**[AGREE] R1-N1: OR 方向反转 framing 不够显著**
同意。Table 1 仅展示 uncorrected N-H=23%*，corrected 6.06% vs 9.5% 仅在 Appendix。CMH OR=3.37 在正文出现 3 次 vs corrected OR=0.61 仅 2 次，频率不对称。Abstract "suggestive but non-robust improvement" 措辞仍暗示正方向效应，未提方向逆转。需修复。

**[AGREE] R1-N2: CMH within-seed 非独立性**
同意这是实质性问题。Greedy decoding 下同一 checkpoint 的 100 个样本高度相关（如 ISR s43: 100% H7）。真正独立观测单位是 seed (n=5)，非 sample (n=350/414)。CMH p<10⁻⁹ 严重 inflated。论文应在正文讨论此限制并降低 CMH prominence。

**[REBUT] R1-N3: "RL-specific" claim**
部分不同意 severity=critical。论文 framing 已 cautious：§4.2 用 "consistent with"（非 "proves"），且显式说 "this mechanistic argument is plausible but not conclusive"（experiments.tex line 40）。C1 表述也用 "consistent with RL-specific failure"。建议降为 warning——问题存在但 framing 已 appropriate。

**[AGREE] R1-W1**: trajectory evidence 仅 β=0.1 两个 seeds，其余 doses 是 snapshot。β=0.2 的 3/3 H7 saturation 本身 sufficient，但 β=0.05/0.3 的 timing claim 缺乏轨迹支持。

**[AGREE] R1-W2**: 100-example eval → per-seed n 可低至 18 (β=0.3 s42)，CI 极宽。

**[AGREE] R1-W3**: 1.7B single seed，与我的 W6 一致。

**[AGREE] R1-W4**: Deleted checkpoints 造成 uncorrected/corrected 3.7× 差距，是方法学遗憾。

**[REBUT] R1-W5**: ISR 不需要 ROC/threshold。ISR 设计为 population-level trend indicator（collapse trajectory），非 per-sample binary classifier。配合 text-match + functional taxonomy 做分类。ISR 与 NLI accuracy 无相关性 (ρ=-0.049) 说明它不适合做 per-sample semantic classifier。

**[AGREE] R1-W6**: Table 1 exec-only 500-step 为 s42 单 seed，建议改为 3-seed pooled。

### 评分影响

R1 的 N1/N2 若不修复，我的评分从 3.5 降至 3.0。R1 的 3.0 (Findings) 评分合理但略保守——核心 descriptive findings（collapse trajectory、nine modes、cross-logic transfer）的价值不完全受统计问题侵蚀。

**我的最终评分：维持 3.5 (Borderline Conference)**，条件是 N1/N2 需在 revision 中修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 594 · 2026-05-17T17:16:31.346184+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 595 · 2026-05-17T17:16:33.897599+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- R1 的 3 个 critical 中，**N1 (OR framing)** 和 **N2 (CMH 非独立性)** 完全同意，**N3 (SFT PR gap)** 认为论文 framing 已 cautious，建议降为 warning
- 6 个 warnings 中同意 5 个，反驳 W5（ISR 不是 binary classifier，不需要 ROC）
- 维持我的评分 3.5 (Borderline Conference)，若 N1/N2 不修复则降至 3.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 596 · 2026-05-17T17:16:42.515213+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 57

## Round 57

8 recorded events


### User

_source line 597 · 2026-05-17T17:17:18.155598+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths

[AGREE] S1-S5 全部同意。特别是 S4（自我批判意识强），我在自己的审稿中也将此列为主要优势（我的 S3）。S5（ISR 命名一致性）是我遗漏的观察。

---

### Weaknesses

**[AGREE] R2-W1: Introduction 的 5 个 \paragraph{} 导致叙事碎片化**

同意。Introduction（introduction.tex:7-33）有 5 个 \paragraph{}："The execution-only blind spot"、"Component necessity testing"、"ISR as diagnostic"、"ISR as reward"、"Contributions"。前两个建立了 problem → method 的合理流，但 §3 和 §4 确实预支了 experiments 结论。对于 EMNLP long paper，这种结构更像 extended abstract 的格式。建议将 §3-§4 合并为一个"Key findings"段落，用 1-2 句话概括，把具体数字留给 Experiments。

**[AGREE] R2-W2: Abstract 偏向数据堆砌**

同意。我手动计数 abstract.tex 的数值/统计量：97±2%, three seeds, zero, 99.5%, 92%, four doses, β=0.1, 6 conditions, 2 logic types, 2 model scales, nine modes = 11 个。对于 4 句话的 Abstract 这过于密集。特别是最后一句 "Across 6 conditions, 2 logic types, and 2 model scales" 是纯规模描述，可删减。建议保留 5-6 个服务于叙事推进的关键数字（如 97±2%, 99.5% collapse, 92% SFT non-hacking, nine modes）。

**[AGREE with nuance] R2-W3: 方法新颖性有限**

同意方法论 novelty 有限这一判断。Algorithm 1（method.tex:28-42）确实仅 6 行 LOO 伪代码，论文自承两次（method.tex:26, introduction.tex:16）。但我想补充两点 nuance：

1. 论文的 LOO vs Shapley 讨论（method.tex:60-63）和 O(1) ablation variant（method.tex:64-65, appendix.tex:676-688）展示了设计空间的探索，不是盲目套用 LOO
2. 对于 empirical study，方法简单是优势而非劣势：复杂方法会引入额外 confound，LOO 的透明性使 Goodhart vulnerability 的分析更清晰
3. 真正的 methodological contribution 不在 Algorithm 1 本身，而在 reward formulation（multiplicative vs convex, method.tex:71-75）和 hacking taxonomy 的分类方法论（method.tex:77-80）

R2 的缓解因素判断（"正确定位为 empirical study"）准确。

**[AGREE] R2-W4: §4.3 按 β 逐一报告的顺序问题**

同意。experiments.tex 的 β 呈现顺序为 0.1→0.05→0.2→0.3（experiments.tex:82, 112, 116, 119），既非升序也非降序。虽然将 β=0.1 作为 focal dose（5 seeds, trajectory analysis）放在首位有合理性，但：
- 读者需要在 4 个 dose 之间反复跳转才能建立 dose-response 全局图景
- "Non-monotonic dose-response" 总结段（experiments.tex:124-126）放在最后，但它应该作为 §4.3 的开头引导

建议：§4.3 开头加 1-2 句总结性发现（如 "All four doses produce dominant H7 gaming; β controls only timing and mode"），然后按升序呈现各 dose。

**[AGREE] R2-W5: Table 1 caption 信息密度过高**

同意。4 个脚注符号（†, ‡, *, ††）各带解释，加上 "PR/ISR*: mean±std; H7/H1/N-H: pooled %"，总长约 80 words（experiments.tex:77）。但我认为这是 dense summary table 的必要代价——如果删减脚注，Table 1 的数据会更容易被误读（特别是 ‡ 标注 N-H 为 uncorrected upper bound，这对正确理解至关重要）。建议的折中：将 † 和 †† 的详细解释移入 main text 或 Appendix，caption 仅保留 ‡ 和 *（直接影响 claim interpretation 的标注）。

**[AGREE] R2-W6: Cross-scale §4.5 应标注 "preliminary"**

同意，这与我的 W3 一致。experiments.tex:140 说 "single seed, 500 steps" 但未用 "preliminary" 一词。正文说 "Cross-Scale Evidence"（标题），读者可能赋予这些结果比实际更高的权重。建议标题改为 "Preliminary Cross-Scale Evidence"。

**[AGREE] R2-W7: "Notably" AI 风格标记**

同意。experiments.tex:34 "Notably, s43 recovers from PR=13%..." 符合论文写作规范 §5.2 列出的禁用模式。应直接写 "s43 recovers from..." 即可。

---

### Questions

**[AGREE] R2-Q1: ISR Goodhart vulnerability 的可预见性**

这是一个重要问题，涉及论文的 contribution 定位。论文在 method.tex:54-57 明确指出 ISR≥0.5 for tautological proofs 的结构性漏洞，且 Related Work（related_work.tex:14-20）引用了 Goodhart taxonomy。论文对此的回应在 conclusion.tex:6-8："While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation, non-monotonic dose-response, and cross-logic mode divergence."

我认为这个回应基本成立，但可以更强调：empirical 贡献的价值在于 calibrating 理论预测（哪些现象可预测，哪些不可），而非在于 surprise factor。论文应更明确地将 4-dose 实验定位为 verification + discovery（验证 Goodhart prediction 的同时发现了 stochastic bifurcation 等未预见现象）。

**[AGREE] R2-Q2: SFT PR confound**

完全同意。这与我的 N3 [critical] 一致。论文承认 PR gap confound（experiments.tex:38-40）但无法 resolve。100-step checkpoint comparison（Appendix §G, PR=32% vs SFT PR=13%）仅部分缓解。C1 的 "RL-specific" attribution 在当前证据下过强。

**[AGREE with qualification] R2-Q3: Premise-count-matched 消除 ISR advantage**

同意 R2 的观察方向：1.06× 差异在 premise-count-matched 后确实近乎消失（experiments.tex:104-105, appendix.tex:83-86）。但我不完全同意 "ISR 唯一正面效果只是鼓励 shorter outputs" 的推论。ISR 在 transient window 中产生了一些 genuinely high-ISR proofs（如 s45 55% genuine at 500 steps, Table~\ref{tab:fol-beta01-perseed}），但这些是暂时的且最终会被 H7 attractor 消灭。

更准确的解读：ISR 的 "正面" 效果有两个渠道——(1) encouraging shorter outputs（mechanical ISR inflation, resolved by premise-count matching）和 (2) genuinely rewarding necessary premises（transient, eventually gamed）。渠道 (1) 被消除后，渠道 (2) 的 net effect 在 corrected analysis 下是 n.s.（OR=0.61）。所以 R2 的核心判断是对的：ISR 作为 reward 没有 robust 的正面效果。

**[PARTIAL AGREE] R2-Q4: 10/40 引用 OpenAlex 未找到**

部分同意。ML/NLP 领域大量引用 arXiv preprints、blog posts、tech reports，OpenAlex 未收录不等于引用虚假。但论文应检查：(1) 所有 arXiv 引用是否标注了正确的 arXiv ID；(2) blog posts/tech reports 是否有更正式的 venue 版本可替代；(3) ACL 格式要求所有引用有完整的 author, title, year, venue 信息。这不是 critical 问题但需要 camera-ready 修复。

---

### Missing References

**[PARTIAL AGREE] R2-Missing-1: GRPO 原始论文**

GRPO 来自 DeepSeekMath（\citep{deepseekmath}），论文已引用（method.tex:15, experiments.tex:10）。如果 R2 指的是 GRPO 有独立的技术报告，据我所知没有——GRPO 是 DeepSeekMath 论文中首次提出的。无需额外引用。

**[AGREE] R2-Missing-2: Neurosymbolic RLVR 其他近期工作**

同意。Related Work（related_work.tex:5）已引用 logic-rl、mellgren-prolog-grpo、deepseek-prover-v15 等，但该领域发展迅速，可能有更近的工作需要覆盖。建议作者检查 2025-2026 的 neurosymbolic RLVR 新工作。

**[AGREE] R2-Missing-3: Goodhart's Law 原文**

同意。论文引用了 Manheim & Garrabrant 2018 的 taxonomy（related_work.tex:14）和多篇理论/实证工作，但确实缺少 Goodhart 1975 原文或 Strathern 1997 ("When a measure becomes a target, it ceases to be a good measure") 的经典引用。对于以 Goodhart's Law 为核心框架的论文，这是一个引用遗漏。

---

### Overall Assessment

**[PARTIAL AGREE] R2 给出 3.5 (Borderline Conference)**

R2 的评分比我（3.0 Findings）高 0.5 分。核心分歧在于统计问题的严重程度：
- R2 将统计问题（OR 方向反转、within-seed 非独立性）列为 Questions 而非 Weaknesses，我将其列为 Critical Weaknesses
- R2 的 W1-W7 集中在 presentation issues（Introduction 结构、Abstract 数据堆砌、dose 呈现顺序、AI 风格），而非 methodological/statistical concerns
- R2 的 "方法新颖性有限" 与 "surprise factor 受限" 的判断我同意，但我认为 statistical robustness 问题比 novelty/surprise 对 accept/reject decision 影响更大

我维持 3.0 (Findings) 的评分。如果作者能通过 rebuttal 解决 CMH 非独立性（如提供 cluster-robust 分析）和 OR 方向反转的 framing 问题，我愿意上调至 3.5。

---

### 总结

R2 的审稿侧重于写作质量和 novelty/positioning，与我侧重的统计/实验设计形成互补。我们在以下方面一致：
- SFT PR confound 是未解决的问题
- 方法 novelty 有限但论文定位正确
- Cross-scale single-seed 应标注 preliminary

主要分歧：R2 未将 OR 方向反转和 within-seed 非独立性列为 critical issues，我认为这些是影响接收决定的核心问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-17T17:17:53.312609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-17T17:17:53.365095+00:00_

1	issues:
2	# ===== 历史 issues (Round 0-3, 全部 resolved) =====
3	- id: "R1-W1"
4	  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。"
11	  resolution_round: 2
12	
13	- id: "RV-EVAL-FALLBACK"
14	  summary: "eval_sta.py test_100.jsonl 静默 fallback 已移除"
15	  category: experiment
16	  severity: critical
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 1
20	  resolution: "第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。"
21	  resolution_round: 1
22	
23	- id: "RV-D060-NARRATIVE"
24	  summary: "D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立"
25	  category: experiment
26	  severity: warning
27	  status: resolved
28	  first_raised_round: 1
29	  last_seen_round: 1
30	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。"
31	  resolution_round: 2
32	
33	- id: "RV-FIG2-STALE-SCRIPT"
34	  summary: "figures/paper/gen_fig2.py 旧脚本数据错误"
35	  category: format
36	  severity: warning
37	  status: resolved
38	  first_raised_round: 1
39	  last_seen_round: 1
40	  resolution: "已修复。"
41	  resolution_round: 1
42	
43	- id: "R1-W2"
44	  summary: "ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量"
45	  category: framing
46	  severity: critical
47	  status: resolved
48	  first_raised_round: 0
49	  last_seen_round: 0
50	  resolution: "method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---
