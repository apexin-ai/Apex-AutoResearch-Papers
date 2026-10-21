# Director coordination — Part 6 of 6

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination-copy-2.md) · [Structured JSON](../../../sessions/3d/3da1d06caead0f03c51d.json)

## Round 146

### Tool call

_source line 1592 · 2026-05-21T21:54:08.567774+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n# ============================================================\n# ROUND 18 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值——accumulation 场景无系统实验\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 列为 N1 critical, R2 原列 W2 后升级为 critical。两人共识：pilot accumulation 仅报 -14~-15pp 无 Table/per-cell/EDD/统计检验\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-W1 (framing) resolved via §6 段落，但实验数据缺口未填补\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识 critical。R2-N2 列为 critical，R1 交叉回应升级同意 critical。指出 Gerstgrasser et al. (2024) 已论证 accumulation 与 full-replacement 统计行为根本不同。§8 Limitations 仅一句话处理不充分。\"}\n  action_items:\n  - {round: 17, action: \"需用户确认是否做新 accumulation 实验。已有 accum_v3 (Pythia nucleus, mix25/mix50) DONE 数据已引用于论文。新增 cells 需新实验。\", assigned_to: research_director, status: open}\n  - {round: 18, action: \"至少一个模型在 25/50/75% accumulation 比例下提供系统性 EDD 结果\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染——无法分离规模效应 vs 参考模型切换\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 首次识别 confound（N2 critical），R2 完全认同。14B 用 self-reference 而主表用 Pythia-1.4B cross-reference\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识 critical。R1 自纠 Round 1 中 85.8% 错误数字（实为 50.8%），认为问题比原评估更严重。Self-ref 50.8% EDD=0 意味着连 d0/d1 都无法区分。Cross-ref 44.1% EDD=2。§6 Discussion 对 EDD=0 含义讨论不足。\"}\n  action_items:\n  - {round: 17, action: \"需用户确认。控制实验：Pythia-1.4B ref on 14B data（仅 feature extraction，~2-3h）\", assigned_to: research_director, status: open}\n  - {round: 18, action: \"使用同族不同规模模型（如 Pythia-6.9B）分离 self-reference vs scale effect\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%——策略未知时方法基本失效，与应用场景矛盾\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N3 + R2-N3 完全共识\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-N3 resolved via reframe，但 claim scope 仍超出\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识。R1 列为 N2 critical，R2 列为 W1 后交叉同意 critical。Two-stage pipeline 恢复 11.5pp 但最终仍仅 ~57%。论文动机暗示通用性但证据仅支持 within-strategy。\"}\n  action_items:\n  - {round: 17, action: \"Abstract 已加 'depth estimation claims hold most strongly within-strategy or when the decoding configuration is known'; §5.3 已有 scope 限定; §1 贡献3 改为 boundary condition\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"探索策略不变特征子集；更明确限定 claims 为 within-strategy 场景\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足——标准特征+标准分类器，不满足 Conference 门槛\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2-N1 critical; R1 REBUT 但同意 Conference 不足\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 R2-N1 再次列为 critical，R1 AGREE。19 特征均非首创（GLTR/DetectGPT/Ghostbuster），RF 无超参搜索。R1 认为 task formulation 提供 excitement (3.5/5)，R2 认为不够 (2.5/5)，但双方均认同方法论零创新。\"}\n  action_items:\n  - {round: 17, action: \"接受 Findings 定位。§1 已有 empirical contribution 自我定位。\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"考虑引入 learned feature 或 hybrid 方法提升方法层面贡献度；或更强力论证 interpretable features 是设计选择\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 18 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W1, R2 AGREE。2 个 seed 不足以建立 stability claim\"}\n  - {round: 18, reviewers: [1, 2], note: \"R1 列为 N1 critical，R2 REBUT 指出 B.16 已有 seed=43 cross-seed replication（+0.14 to +3.17pp，CI 重叠），建议降为 warning。R1 交叉回应中未反驳。共识：降为 warning，2 个种子初步排除 artifact 但统计功效不足。\"}\n  action_items:\n  - {round: 17, action: \"DDL 前不可行完整 5 seeds。Limitations 已标注 seed uncertainty。Rebuttal 材料准备。\", assigned_to: research_director, status: open}\n  - {round: 18, action: \"增加到至少 3-5 个种子以提供可靠方差估计\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W2, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"R1-W1 warning，R2 AGREE。Footnote 3 承认 exploratory 但主文多处做确定性声明。100+ 测试量级应至少报告 FDR-corrected p-values。\"}\n  action_items:\n  - {round: 17, action: \"Abstract 'revealing' → 'suggesting' 已改。进一步弱化待评估。\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"对关键结论涉及的测试应用 Bonferroni 或 BH 校正，至少做 sensitivity check\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 ≤125M backbone\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W3, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"R1-W3 warning，R2 部分 REBUT。R2 指出 B.5 中 DeBERTa-v3-large 因 DCOL 数值不稳定失败（非故意回避），但标准 fine-tuning 的 large 变体未尝试。R2 补充 RF 与 PLM 信息 access 不同（reference-model features vs raw text）。\"}\n  action_items:\n  - {round: 17, action: \"需用户确认是否做新实验。否则在 Limitations 讨论。\", assigned_to: research_director, status: open}\n  - {round: 18, action: \"至少尝试 DeBERTa-v3-large 标准 fine-tuning（非 DCOL），排除框架问题\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%, p>0.05），削弱独特价值\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"R1-W4 warning，R2 AGREE。已有方法 calibration 后即可匹敌。R2 补充计算效率差异（单模型 vs 双模型）未讨论。\"}\n  action_items:\n  - {round: 17, action: \"§5.1 已有透明讨论 Binoculars parity + pipeline 优势。可进一步强化。\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"主文中更显著讨论 Binoculars 等价性及计算效率差异\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R1-W5 warning，R2 AGREE。Pipeline 依赖固定参考模型，跨架构 4-11pp 下降（B.13），跨规模更大。未提供参考模型选择指南。\"}\n  action_items:\n  - {round: 18, action: \"Limitations 中增加参考模型依赖作为独立限制；提供选择指南或分析\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著（p>0.4）但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5(curation) + R2-W5 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"R2-W4 warning，R1 AGREE。B.22 PoC 过于 toy（Pythia-410M, 单种子, PPL 变化 0.03-0.12, 不显著）。§6 curation 主张需降低强度或扩大 PoC。\"}\n  action_items:\n  - {round: 17, action: \"§6 'deployment scenario' → 'potential application' + hedge (p>0.4 引用) 已完成\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"进一步降低 §6 curation claim 强度，或扩大 PoC 规模和指标\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 (estimation vs classification)\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 minor points\"}\n  - {round: 18, reviewers: [1, 2], note: \"R2-W3 warning，R1 AGREE。Title/Abstract 用 estimation（暗示连续值），§3.1 定义为 ordinal classification。应统一或首次出现时声明等价。\"}\n  action_items:\n  - {round: 17, action: \"orphan bib penedo2024_fineweb 已删除\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"统一术语为 ordinal classification 并在首次出现解释 estimation 作为通俗表述\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 18 — MINOR (Info)\n# ============================================================\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N4 critical; R2 agree with nuance——family-level 可靠，individual ranking 不可靠\"}\n  - {round: 15, reviewers: [1, 2], note: \"历史: R16-W3 resolved via group-level ablation\"}\n  - {round: 18, reviewers: [1], note: \"R1-M1: 14-16/19 features VIF>10，实际独立维度 ~4-5。建议主文更早提及（§3.3 而非 §4.2）。R17 写作弱化已被 R18 默认接受。\"}\n  action_items:\n  - {round: 17, action: \"§4.2 弱化 individual ranking → family-level + cautious interpretation caveat\", assigned_to: research_director, status: done}\n  - {round: 17, action: \"补充 conditional permutation importance 或 bootstrap rank stability（需用户确认是否做新计算）\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R2-M1，R1 AGREE。d0 应为同一 Wikipedia seed corpus 但未在主文显式声明。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: Table 2 有 CI 但部分表格没有——CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1], note: \"R1 minor point\"}\n  - {round: 18, reviewers: [1, 2], note: \"R2-M2，R1 AGREE。主表 Table 2 应统一报告 CI/std。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M3\n  summary: §3.5 Theoretical Grounding 标题过大——内容为 post-hoc motivation\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R2-M3，R1 AGREE。建议改为 Theoretical Motivation 或 Intuitive Grounding。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2: attractor cycles (2502.15208), Canary's Echo (2502.14921), Data Provenance Auditing (2510.09655). R1: Liang et al. (2023) GPT detector bias\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 共识推荐：Carlini et al. (2021) Extracting Training Data（R1 标注为最重要缺失）、Rothe et al. (2018) Deep ordinal regression。建议补充：Guo et al. (2025)、Li et al. (2024)。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens，短文本推广未讨论\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1], note: \"R1-M3: B.18 显示 128 tokens accuracy ~66%，512 token 假设适用范围应界定。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1], note: \"R1-M2: B.29 确认 200 trees 为默认值无超参搜索。RF 对超参相对鲁棒但引入不确定性。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (from Round 16-17, status carried forward)\n# ============================================================\n\n- id: R16-N1\n  summary: 14B 结果 (EDD=0) 从根本上削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 12, reviewers: [1, 2], note: \"R12-W4\"}\n  - {round: 16, reviewers: [1, 2], note: \"R1-N4 + R2-N1 一致 critical\"}\n  - {round: 17, reviewers: [1, 2], note: \"R16 writing fix resolved; R17 发现新 confound → R17-N2\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-N2 下追踪\"}\n  resolution: \"Abstract 加 scope 限定; §6 新增 scale dependence 段落。R17 confound → R17-N2\"\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足——标准特征+标准分类器\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-N2 critical, R1 REBUT\"}\n  - {round: 17, reviewers: [1, 2], note: \"R17 再次提出 → R17-N5\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-N5 下追踪\"}\n  resolution: \"§1 贡献重组。R17 novelty 批评结构性 → R17-N5\"\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R1-N3 critical\"}\n  - {round: 17, reviewers: [1, 2], note: \"R17 认为 claim 仍需限定 → R17-N3 (now in_progress)\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-N3 下追踪\"}\n  resolution: \"§5.3 reframed + R17 进一步 scope 限定\"\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-N3 critical, R1 AGREE\"}\n  - {round: 17, reviewers: [1, 2], note: \"framing 已解决，实验缺口 → R17-N1\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-N1 下追踪\"}\n  resolution: \"§6 新增 'From ceiling to floor' 段\"\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia †)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Reviewer 确认 † + ref-model ablation 67-79% 已充分\"\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N4 individual ranking 仍 overstated — 已在 R17-N4 中弱化\"}\n  - {round: 18, reviewers: [1], note: \"R18 R1-M1 提及 VIF>10，继续在 R17-N4 下追踪\"}\n  resolution: \"§4.2 group-level ablation + R17 弱化 individual ranking\"\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载 (12+ 数字)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"R18 未提及，视为已解决\"}\n  resolution: \"Abstract ~6 数字, 3 findings 结构。\"\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Abstract 和 §1 以 d1-d3 balanced accuracy 领头\"\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Sensitivity analysis 已覆盖\"\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W4 重新提出，R17 写作修复已加强 BOS caveat\"}\n  - {round: 18, reviewers: [], note: \"R18 未作为独立 issue 提出，视为已解决\"}\n  resolution: \"§3.2 BOS caveat 加强为独立句 + prompted -13.8pp + Limitations\"\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W6 要求 FPR-coverage tradeoff curve\"}\n  - {round: 18, reviewers: [], note: \"R18 未提及\"}\n  resolution: \"Thresholding 方案已覆盖。更详细 tradeoff 需新计算。\"\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W7 认为仍不足，R17 已加 Conclusion 段\"}\n  - {round: 18, reviewers: [], note: \"R18 未作为独立 issue 提出\"}\n  resolution: \"§6 扩展为 4 段（含 Conclusion）。8 页限制约束。\"\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"§6 含 depth-scored data curation scenario (R17 已 hedge)\"\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: \"Minor visual, acceptable for review\"\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"视觉审查再次指出 pp.1-2 连续纯文本无 display item\"}\n  resolution: \"Pipeline 太简单不需要图\"\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"R18 格式检查：主文 8 页 ✓\"}\n  resolution: \"编译验证通过\"\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致 depth estimation / classification\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 仍注意到残余混用 → R17-M5\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-M5/R18-W6 下追踪，升级为 warning\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"已加入\"\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Classifier convergence evidence sufficient\"\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"视觉审查指出 p.8 极度拥挤——4 display items + 4 章节\"}\n  resolution: \"Structural constraint\"\n  resolution_round: 16\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"项目收尾不再跑新实验\"\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W2 重新提出\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-W2 下追踪\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§2 已引用\"\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"R18 格式检查通过 ✓\"}\n  resolution: \"编译验证通过，主文 pp.1-8\"\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"用户指示不再跑新实验\"\n  resolution_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n# ============================================================\n# ROUND 18 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值——accumulation 场景无系统实验\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 列为 N1 critical, R2 原列 W2 后升级为 critical。两人共识：pilot accumulation 仅报 -14~-15pp 无 Table/per-cell/EDD/统计检验\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-W1 (framing) resolved via §6 段落，但实验数据缺口未填补\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识 critical。R2-N2 列为 critical，R1 交叉回应升级同意 critical。指出 Gerstgrasser et al. (2024) 已论证 accumulation 与 full-replacement 统计行为根本不同。§8 Limitations 仅一句话处理不充分。\"}\n  action_items:\n  - {round: 17, action: \"需用户确认是否做新 accumulation 实验。已有 accum_v3 (Pythia nucleus, mix25/mix50) DONE 数据已引用于论文。新增 cells 需新实验。\", assigned_to: research_director, status: open}\n  - {round: 18, action: \"至少一个模型在 25/50/75% accumulation 比例下提供系统性 EDD 结果\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染——无法分离规模效应 vs 参考模型切换\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 首次识别 confound（N2 critical），R2 完全认同。14B 用 self-reference 而主表用 Pythia-1.4B cross-reference\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识 critical。R1 自纠 Round 1 中 85.8% 错误数字（实为 50.8%），认为问题比原评估更严重。Self-ref 50.8% EDD=0 意味着连 d0/d1 都无法区分。Cross-ref 44.1% EDD=2。§6 Discussion 对 EDD=0 含义讨论不足。\"}\n  action_items:\n  - {round: 17, action: \"需用户确认。控制实验：Pythia-1.4B ref on 14B data（仅 feature extraction，~2-3h）\", assigned_to: research_director, status: open}\n  - {round: 18, action: \"使用同族不同规模模型（如 Pythia-6.9B）分离 self-reference vs scale effect\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%——策略未知时方法基本失效，与应用场景矛盾\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N3 + R2-N3 完全共识\"}\n  - {round: 12, reviewers: [1, 2], note: \"历史: R16-N3 resolved via reframe，但 claim scope 仍超出\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识。R1 列为 N2 critical，R2 列为 W1 后交叉同意 critical。Two-stage pipeline 恢复 11.5pp 但最终仍仅 ~57%。论文动机暗示通用性但证据仅支持 within-strategy。\"}\n  action_items:\n  - {round: 17, action: \"Abstract 已加 'depth estimation claims hold most strongly within-strategy or when the decoding configuration is known'; §5.3 已有 scope 限定; §1 贡献3 改为 boundary condition\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"探索策略不变特征子集；更明确限定 claims 为 within-strategy 场景\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足——标准特征+标准分类器，不满足 Conference 门槛\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2-N1 critical; R1 REBUT 但同意 Conference 不足\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 R2-N1 再次列为 critical，R1 AGREE。19 特征均非首创（GLTR/DetectGPT/Ghostbuster），RF 无超参搜索。R1 认为 task formulation 提供 excitement (3.5/5)，R2 认为不够 (2.5/5)，但双方均认同方法论零创新。\"}\n  action_items:\n  - {round: 17, action: \"接受 Findings 定位。§1 已有 empirical contribution 自我定位。\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"考虑引入 learned feature 或 hybrid 方法提升方法层面贡献度；或更强力论证 interpretable features 是设计选择\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 18 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W1, R2 AGREE。2 个 seed 不足以建立 stability claim\"}\n  - {round: 18, reviewers: [1, 2], note: \"R1 列为 N1 critical，R2 REBUT 指出 B.16 已有 seed=43 cross-seed replication（+0.14 to +3.17pp，CI 重叠），建议降为 warning。R1 交叉回应中未反驳。共识：降为 warning，2 个种子初步排除 artifact 但统计功效不足。\"}\n  action_items:\n  - {round: 17, action: \"DDL 前不可行完整 5 seeds。Limitations 已标注 seed uncertainty。Rebuttal 材料准备。\", assigned_to: research_director, status: open}\n  - {round: 18, action: \"增加到至少 3-5 个种子以提供可靠方差估计\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W2, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"R1-W1 warning，R2 AGREE。Footnote 3 承认 exploratory 但主文多处做确定性声明。100+ 测试量级应至少报告 FDR-corrected p-values。\"}\n  action_items:\n  - {round: 17, action: \"Abstract 'revealing' → 'suggesting' 已改。进一步弱化待评估。\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"对关键结论涉及的测试应用 Bonferroni 或 BH 校正，至少做 sensitivity check\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 ≤125M backbone\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W3, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"R1-W3 warning，R2 部分 REBUT。R2 指出 B.5 中 DeBERTa-v3-large 因 DCOL 数值不稳定失败（非故意回避），但标准 fine-tuning 的 large 变体未尝试。R2 补充 RF 与 PLM 信息 access 不同（reference-model features vs raw text）。\"}\n  action_items:\n  - {round: 17, action: \"需用户确认是否做新实验。否则在 Limitations 讨论。\", assigned_to: research_director, status: open}\n  - {round: 18, action: \"至少尝试 DeBERTa-v3-large 标准 fine-tuning（非 DCOL），排除框架问题\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%, p>0.05），削弱独特价值\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"R1-W4 warning，R2 AGREE。已有方法 calibration 后即可匹敌。R2 补充计算效率差异（单模型 vs 双模型）未讨论。\"}\n  action_items:\n  - {round: 17, action: \"§5.1 已有透明讨论 Binoculars parity + pipeline 优势。可进一步强化。\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"主文中更显著讨论 Binoculars 等价性及计算效率差异\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R1-W5 warning，R2 AGREE。Pipeline 依赖固定参考模型，跨架构 4-11pp 下降（B.13），跨规模更大。未提供参考模型选择指南。\"}\n  action_items:\n  - {round: 18, action: \"Limitations 中增加参考模型依赖作为独立限制；提供选择指南或分析\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著（p>0.4）但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5(curation) + R2-W5 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"R2-W4 warning，R1 AGREE。B.22 PoC 过于 toy（Pythia-410M, 单种子, PPL 变化 0.03-0.12, 不显著）。§6 curation 主张需降低强度或扩大 PoC。\"}\n  action_items:\n  - {round: 17, action: \"§6 'deployment scenario' → 'potential application' + hedge (p>0.4 引用) 已完成\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"进一步降低 §6 curation claim 强度，或扩大 PoC 规模和指标\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 (estimation vs classification)\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 minor points\"}\n  - {round: 18, reviewers: [1, 2], note: \"R2-W3 warning，R1 AGREE。Title/Abstract 用 estimation（暗示连续值），§3.1 定义为 ordinal classification。应统一或首次出现时声明等价。\"}\n  action_items:\n  - {round: 17, action: \"orphan bib penedo2024_fineweb 已删除\", assigned_to: research_director, status: done}\n  - {round: 18, action: \"统一术语为 ordinal classification 并在首次出现解释 estimation 作为通俗表述\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 18 — MINOR (Info)\n# ============================================================\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N4 critical; R2 agree with nuance——family-level 可靠，individual ranking 不可靠\"}\n  - {round: 15, reviewers: [1, 2], note: \"历史: R16-W3 resolved via group-level ablation\"}\n  - {round: 18, reviewers: [1], note: \"R1-M1: 14-16/19 features VIF>10，实际独立维度 ~4-5。建议主文更早提及（§3.3 而非 §4.2）。R17 写作弱化已被 R18 默认接受。\"}\n  action_items:\n  - {round: 17, action: \"§4.2 弱化 individual ranking → family-level + cautious interpretation caveat\", assigned_to: research_director, status: done}\n  - {round: 17, action: \"补充 conditional permutation importance 或 bootstrap rank stability（需用户确认是否做新计算）\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R2-M1，R1 AGREE。d0 应为同一 Wikipedia seed corpus 但未在主文显式声明。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: Table 2 有 CI 但部分表格没有——CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1], note: \"R1 minor point\"}\n  - {round: 18, reviewers: [1, 2], note: \"R2-M2，R1 AGREE。主表 Table 2 应统一报告 CI/std。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M3\n  summary: §3.5 Theoretical Grounding 标题过大——内容为 post-hoc motivation\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R2-M3，R1 AGREE。建议改为 Theoretical Motivation 或 Intuitive Grounding。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2: attractor cycles (2502.15208), Canary's Echo (2502.14921), Data Provenance Auditing (2510.09655). R1: Liang et al. (2023) GPT detector bias\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 共识推荐：Carlini et al. (2021) Extracting Training Data（R1 标注为最重要缺失）、Rothe et al. (2018) Deep ordinal regression。建议补充：Guo et al. (2025)、Li et al. (2024)。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens，短文本推广未讨论\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1], note: \"R1-M3: B.18 显示 128 tokens accuracy ~66%，512 token 假设适用范围应界定。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [1], note: \"R1-M2: B.29 确认 200 trees 为默认值无超参搜索。RF 对超参相对鲁棒但引入不确定性。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (from Round 16-17, status carried forward)\n# ============================================================\n\n- id: R16-N1\n  summary: 14B 结果 (EDD=0) 从根本上削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 12, reviewers: [1, 2], note: \"R12-W4\"}\n  - {round: 16, reviewers: [1, 2], note: \"R1-N4 + R2-N1 一致 critical\"}\n  - {round: 17, reviewers: [1, 2], note: \"R16 writing fix resolved; R17 发现新 confound → R17-N2\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-N2 下追踪\"}\n  resolution: \"Abstract 加 scope 限定; §6 新增 scale dependence 段落。R17 confound → R17-N2\"\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足——标准特征+标准分类器\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-N2 critical, R1 REBUT\"}\n  - {round: 17, reviewers: [1, 2], note: \"R17 再次提出 → R17-N5\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-N5 下追踪\"}\n  resolution: \"§1 贡献重组。R17 novelty 批评结构性 → R17-N5\"\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R1-N3 critical\"}\n  - {round: 17, reviewers: [1, 2], note: \"R17 认为 claim 仍需限定 → R17-N3 (now in_progress)\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-N3 下追踪\"}\n  resolution: \"§5.3 reframed + R17 进一步 scope 限定\"\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R2-N3 critical, R1 AGREE\"}\n  - {round: 17, reviewers: [1, 2], note: \"framing 已解决，实验缺口 → R17-N1\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-N1 下追踪\"}\n  resolution: \"§6 新增 'From ceiling to floor' 段\"\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia †)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Reviewer 确认 † + ref-model ablation 67-79% 已充分\"\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N4 individual ranking 仍 overstated — 已在 R17-N4 中弱化\"}\n  - {round: 18, reviewers: [1], note: \"R18 R1-M1 提及 VIF>10，继续在 R17-N4 下追踪\"}\n  resolution: \"§4.2 group-level ablation + R17 弱化 individual ranking\"\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载 (12+ 数字)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"R18 未提及，视为已解决\"}\n  resolution: \"Abstract ~6 数字, 3 findings 结构。\"\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Abstract 和 §1 以 d1-d3 balanced accuracy 领头\"\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Sensitivity analysis 已覆盖\"\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W4 重新提出，R17 写作修复已加强 BOS caveat\"}\n  - {round: 18, reviewers: [], note: \"R18 未作为独立 issue 提出，视为已解决\"}\n  resolution: \"§3.2 BOS caveat 加强为独立句 + prompted -13.8pp + Limitations\"\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W6 要求 FPR-coverage tradeoff curve\"}\n  - {round: 18, reviewers: [], note: \"R18 未提及\"}\n  resolution: \"Thresholding 方案已覆盖。更详细 tradeoff 需新计算。\"\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W7 认为仍不足，R17 已加 Conclusion 段\"}\n  - {round: 18, reviewers: [], note: \"R18 未作为独立 issue 提出\"}\n  resolution: \"§6 扩展为 4 段（含 Conclusion）。8 页限制约束。\"\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"§6 含 depth-scored data curation scenario (R17 已 hedge)\"\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: \"Minor visual, acceptable for review\"\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"视觉审查再次指出 pp.1-2 连续纯文本无 display item\"}\n  resolution: \"Pipeline 太简单不需要图\"\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"R18 格式检查：主文 8 页 ✓\"}\n  resolution: \"编译验证通过\"\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致 depth estimation / classification\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 仍注意到残余混用 → R17-M5\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-M5/R18-W6 下追踪，升级为 warning\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"已加入\"\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Classifier convergence evidence sufficient\"\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"视觉审查指出 p.8 极度拥挤——4 display items + 4 章节\"}\n  resolution: \"Structural constraint\"\n  resolution_round: 16\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"项目收尾不再跑新实验\"\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W2 重新提出\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续在 R17-W2 下追踪\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§2 已引用\"\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n  - {round: 18, reviewers: [], note: \"R18 格式检查通过 ✓\"}\n  resolution: \"编译验证通过，主文 pp.1-8\"\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"用户指示不再跑新实验\"\n  resolution_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-21T21:54:08.670200+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml\", \"bytes\": 19882}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1594 · 2026-05-21T21:56:56.728629+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Round**: 18 (fresh review)\n**Reviewers**: R1 (方法严谨性+实验充分性), R2 (新颖性+完整性+写作质量)\n\n---\n\n## Summary\n\n本文提出将递归生成深度估计形式化为序数分类，构建 3 模型×3 解码策略×4 深度的 180K 样本基准，使用 19 维统计特征（perplexity 尾部统计量为主）+ Random Forest 分类器进行深度估计，并提出 Effective Discriminable Depth (EDD) 度量。在 1-1.5B 规模 in-distribution 下表现出色（d1-d3: 59-82%），但方法论无创新（标准特征+标准分类器），full-replacement 假设脱离现实，14B 规模下 EDD=0（self-ref 50.8%），跨策略迁移 d1-d3 仅 45.9%。\n\n---\n\n## Strengths\n\n**S1. 任务定义新颖且有实际意义。** 将 AI 文本检测从二分类推进到有序深度估计，与 model collapse 文献直接对接。这一 framing 在现有文献中是新的。[共识]\n\n**S2. EDD 度量设计优雅且实用。** Definition 1 (§3.4) 提供可操作的单一数字量化\"深度信号能穿透多远\"，与 contraction factor α^d 的理论关联建立了与 model collapse 理论的桥梁。[共识]\n\n**S3. 实验设计系统。** 3×3×4 网格变量控制合理，180K 样本量充分，跨模型/跨策略/跨规模/跨域四个泛化轴全面覆盖。[共识]\n\n**S4. 特征重要性三重验证。** Gini/SHAP/permutation importance 三种方法一致确认 perplexity tail features 主导深度判别（Kendall's W=0.90, p<0.005），跨条件 Spearman ρ̄=0.868。[共识]\n\n**S5. 附录极其详尽。** 17 页 29 个子实验（B.1-B.29），几乎预先回答了所有可预见的 reviewer 问题。诚实报告负面结果（cross-strategy 45.9%、14B EDD=0、DCOL 训练失败）。[共识]\n\n**S6. 引用体系干净可靠。** 75 条 bib entries 验证通过，63 条在线确认，无假引用，4 条 author order mismatch 均为 API 差异。[共识]\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**C1. 方法论创新不足——标准特征+标准分类器** [R2-N1, R1 AGREE]\n19 个特征均非新提出（见于 GLTR/DetectGPT/Ghostbuster），分类器为标准 RF 且无超参搜索（B.29）。论文自我定位为 \"benchmark-driven empirical study\"（§1），但 EMNLP Excitement 维度要求 \"something interesting\"——方法层面贡献接近零。R1 认为任务定义本身提供 excitement（Excitement 3.5/5），R2 认为不够（2.5/5），但双方均认同方法论零创新。四个分类器在跨模型迁移下收敛至 0.8pp 以内（§5.1）虽然支持 \"feature-determined ceiling\" 论点，但也强化了\"方法不重要\"的印象。\n\n**C2. Full-replacement 假设严重限制生态效度** [R2-N2 critical, R1 升级同意 critical]\n整个实验基于 full-replacement chain——每代完全替换训练数据。现实中递归污染几乎都是 accumulation 模式（Gerstgrasser et al., 2024）。论文仅在 §8 Limitations 用一句话提及 pilot accumulation 结果（14-15pp 衰减），无系统实验。Full-replacement 是信号最强的设定，14-15pp 衰减意味着 accumulation 下方法性能可能大幅退化。这不仅是 limitation，而是对论文实际价值的根本性质疑。\n\n**C3. 14B EDD=0——方法在当代模型规模下已失效** [R2-N3, R1 AGREE 并自纠加重]\nSelf-reference 准确率仅 50.8%（2× chance），EDD=0：连 d0（人类）vs d1（首代生成）都无法区分（d0/d1 AUC=0.56-0.64，均低于 T=0.70；Appendix B.14 Table 17）。Cross-reference 下 EDD=2 但准确率仅 44.1%。14B 已非前沿规模（GPT-4/Claude 远超此量级），EDD=0 暗示方法在更大模型上可能彻底失效。§6 Discussion 对此语气过于轻描淡写，未讨论方法的有效边界在哪里。R1 Round 1 中错误引用 85.8%（实为 50.8%），自纠后认为问题比原先评估更严重。\n\n**C4. 跨策略迁移失败** [R1-N2, R2 AGREE]\nd1-d3 跨策略迁移平均 45.9%（Table 6, chance=33%），仅高于随机 13pp。Two-stage pipeline（Appendix B.28）恢复 11.5pp 但最终仍仅 ~57%，远未达到实用水平。实际应用中解码策略通常未知，方法部署场景极为有限。论文动机（Abstract: \"yet no method estimates...\"）暗示通用性，但证据仅支持 within-strategy 使用。\n\n### Warning (Should-Fix)\n\n**W1. LoRA 链种子不足** [R1-N1 critical → R2 REBUT → 共识降为 warning]\n每个 cell 仅一条 LoRA 链（seed=42）。R1 认为无法排除 idiosyncratic artifacts，列为 critical。R2 指出 Appendix B.16 已有 seed=43 的 cross-seed replication（+0.14 to +3.17pp，CI 重叠），初步排除 artifact 可能，建议降级为 warning。共识：2 个种子有限但已初步缓解 artifact 风险，应增加到 3-5 个种子。\n\n**W2. 未进行多重比较校正** [R1-W1, R2 AGREE]\nFootnote 3（§3.5）承认 p-values 为 exploratory 未做校正，但主文多处基于未校正 p-value 做确定性声明（如 §4.3 \"p<0.001\"、§5.1 \"p>0.05\"）。100+ 统计测试量级，应至少报告 FDR-corrected 结果或做 sensitivity check。\n\n**W3. Neural baseline 对比可能不公平** [R1-W3, R2 部分 REBUT]\n仅用 base-size PLMs（DeBERTa-v3-base ~184M, RoBERTa-base ~125M）。R2 指出 B.5 中 DeBERTa-v3-large 因 DCOL 框架数值不稳定而失败（非故意回避），但标准 fine-tuning 的 large 变体未尝试。此外 RF 与 PLM 的信息 access 不同（reference-model perplexity features vs raw text），对比的公平性存疑。\n\n**W4. Binoculars 统计等价削弱独特价值** [R1-W4, R2 AGREE]\nBinoculars 11-feature calibrated 达到 78.1% vs 19-feature RF 78.4%（§5.1, p>0.05）。已有方法 calibration 后即可匹敌，19-feature pipeline 的增量价值不清。计算效率差异（单模型 forward pass vs 双模型）未讨论。\n\n**W5. 参考模型依赖性未充分讨论为部署限制** [R1-W5, R2 AGREE]\nPipeline 依赖固定参考模型（Pythia-1.4B）提取特征。跨架构切换导致 4-11pp 下降（B.13），跨规模更大。部署时需选择合适参考模型但论文未提供选择指南。Limitations 未将其列为独立限制。\n\n**W6. 术语不一致** [R2-W3, R1 AGREE]\nTitle/Abstract 用 \"estimation\"（暗示连续值预测），§3.1 定义为 \"ordinal classification\"。全文交替使用两个术语。应统一或在首次出现时声明等价。\n\n**W7. Downstream curation PoC 不足** [R2-W4, R1 AGREE]\nAppendix B.22 的 PoC 过于 toy（Pythia-410M, 单种子, PPL 变化 0.03-0.12, 不显著 p>0.4）。§6 \"depth-aware curation\" 主张与 evidence 力度不匹配。\n\n### Minor\n\n**M1.** d0 样本是否跨 cell 共享未显式声明 [R2-M1, R1 AGREE]\n**M2.** Table 2 主表未报告 CI/std，仅在文字中零散提及 [R2-M2, R1 AGREE]\n**M3.** §3.5 \"Theoretical Grounding\" 标题过大，内容为 post-hoc motivation [R2-M3, R1 AGREE]\n**M4.** \\cite/\\citet 格式不一致 [R2-M4, R1 AGREE]\n**M5.** VIF>10 的 14-16/19 特征，实际独立维度 ~4-5，应在 §3.3 更早提及 [R1-M1, R2 AGREE]\n**M6.** 生成长度固定 512 tokens，B.18 显示 128 tokens 时 accuracy ~66%，短文本推广未讨论 [R1-M3]\n**M7.** RF 无超参搜索（B.29 确认），200 trees 为默认值 [R1-M2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全一致：\n1. **Overall 3.0 (Findings)** — 独立给出相同评分\n2. **任务定义是最重要的贡献** — EDD 度量有独立价值\n3. **14B EDD=0 构成核心叙事威胁** — self-ref 50.8% 无法区分 d0/d1\n4. **Cross-strategy 45.9% 是实用性的主要障碍** — 策略未知时方法接近失效\n5. **Accumulation 是最大实验缺口** — full-replacement 结论无法直接推广\n6. **方法论无创新** — 标准特征 + 标准分类器\n7. **引用体系干净** — 无假引用\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**1. LoRA 种子严重程度**：R1 列为 critical，R2 提供 B.16 证据 REBUT 并建议降为 warning。R1 未在交叉回应中直接反驳。**结论：降为 warning。B.16 初步排除 artifact 但 2 个种子统计功效不足。**\n\n**2. Excitement 评分**：R1 给 3.5/5（任务定义新颖性驱动），R2 给 2.5/5（方法零创新压制 excitement）。R1 REBUT R2-W2 指出 strategy > model effect 和 cross-ref 提升 EDD 是 non-trivial findings。**结论：分歧合理，反映 task novelty vs method novelty 的权重偏好。合并取 3.0/5。**\n\n**3. Soundness 评分**：R1 给 ~2.5-3.0/5（实验 gap），R2 给 3.5/5（受限条件下执行质量高）。**结论：两者视角互补。合并取 3.0/5。**\n\n**4. Benchmark study 定位**（R2-W2, R1 REBUT）：R2 认为三个 findings 不 surprising；R1 指出 strategy > model effect 和 cross-ref 提升 EDD 是 non-trivial findings，引用 EMNLP 接受 benchmark 论文先例。**结论：benchmark study 在 EMNLP 可接受但需更强的 surprising insight。不列入合并 weakness。**\n\n**5. Figure 1 信息密度**（R2-W5, R1 REBUT）：R2 认为偏低浪费空间，R1 认为任务定义图的信息密度适当。**结论：分歧不影响评分，不列入合并 weakness。**\n\n---\n\n## Questions for Authors\n\n**Q1.** [共识] Accumulation 模式下的系统性实验结果？至少一个模型在 25/50/75% 混合比例下的 EDD？\n**Q2.** [共识] 14B 能否用同族不同规模模型（如 Pythia-6.9B）分离 self-reference vs scale effect？\n**Q3.** [共识] Binoculars in-distribution 等价——19-feature pipeline 的具体优势场景？计算效率差异？\n**Q4.** [共识] 是否探索过策略不变特征子集以改善 cross-strategy transfer？\n**Q5.** [R2] 19 特征中有多少是本文首创的？\n**Q6.** [R1] 为什么不做多重比较校正？关键结论在 FDR 校正后是否仍显著？\n**Q7.** [R2] 两阶段 pipeline 的策略分类阶段准确率是多少？\n**Q8.** [R1] B.16 的 2 个 LoRA 种子是否足够？是否有更多种子的实验？\n\n---\n\n## Missing References\n\n**共识推荐：**\n- Carlini et al. (2021) \"Extracting Training Data from Large Language Models\" — data provenance motivation [R1 标注为最重要缺失]\n- Rothe et al. (2018) \"Deep ordinal regression\" — ordinal classification 方法论 [R2 推荐, R1 同意]\n\n**建议补充：**\n- Guo et al. (2025) \"Generative AI May Prefer to Present Scientific Uncertainties as Certainties\"\n- Li et al. (2024) \"Synthetic Data (Almost) from Scratch\"\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warning, 7 info, 0 critical）：\n\n**Warnings：**\n- pp.1-2 连续两页纯文本无 display item，审稿人第一印象 text-heavy。建议提前 Figure 1 或加 teaser\n- p.8 极度拥挤——4 个 display items（Table 4, Figure 4, Table 5, Table 6）+ 4 个章节（§5.2/5.3/5.4/6）。建议移部分表格至 Appendix\n- p.7 Figure 2 feature importance heatmap 内部字体偏小，打印可读性受影响\n\n**Info：**\n- Figure 3 仅用颜色区分线条，缺 line style/marker 辅助（灰度/色盲不友好）\n- Figure 4 混淆矩阵尺寸偏小\n- Tables 2/3 booktabs 格式规范 ✓\n- Table 1 排版清晰 ✓\n- References 格式统一无 [?] ✓\n- Appendix 表格格式与正文一致 ✓\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n**置信度: 4.5/5** — 两位 Reviewer 独立审稿后达成完全一致的评分，交叉讨论解决了主要分歧。\n\n**评分依据（EMNLP 2026 ARR 标准）：**\n\n| 维度 | 合并评分 | 理由 |\n|------|----------|------|\n| Soundness | 3.0/5 | 在受限条件下（1-1.5B, in-distribution）实验质量高，但 14B EDD=0、cross-strategy 45.9%、limited seed chain、无 accumulation 系统实验构成显著缺口 |\n| Excitement | 3.0/5 | 任务定义有价值（R1: 3.5），但方法论零创新压制（R2: 2.5），取中值 |\n| Reproducibility | 3.5/5 | 超参报告完整（B.29），特征定义清晰，承诺释放代码。LoRA 种子有限降低完全复现信心 |\n\n**总评：** 论文提出了有价值的新任务（递归深度估计）和实用度量（EDD），在 1-1.5B 规模 in-distribution 条件下提供了详尽的实证刻画。但四个 critical 问题——方法论无创新（标准特征+RF）、核心假设脱离现实（full-replacement）、方法在 14B 规模已失效（EDD=0）、跨策略迁移接近失效（45.9%）——叠加使论文达不到 Conference（4.0）门槛。作为 Findings（3.0）论文，任务定义的原创性、EDD 度量的价值、引用和实验的高质量执行支撑其发表。\n\n**达到 Conference (4.0) 所需：**\n1. 至少一组系统的 accumulation 实验（25/50/75% 混合比例下的 EDD）\n2. 14B 使用同族参考模型（如 Pythia-6.9B）分离 self-reference confound\n3. 引入一个 non-trivial 方法改进或 surprising finding 提升 Excitement\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 数字密度适中（~6 个关键数字），\"three findings\" 结构清晰\n- 14B 结果呈现准确（EDD=2, cross-reference 条件），但应更显著标注规模限制\n\n### §1 Introduction\n- 动机推进自然（model collapse → binary detection → depth estimation）\n- \"benchmark-driven empirical study\" 定位诚实但限制论文上限\n- 贡献 3 正确标注 cross-strategy 为 boundary condition\n\n### §2 Related Work\n- 覆盖全面，组织清晰\n- 缺 Carlini et al. (2021) 作为 data provenance 补充\n- 与 GLTR 的关系（同用统计特征，不同任务定义）应更明确讨论\n\n### §3 Method\n- Problem definition 和 EDD 定义（Definition 1）清晰\n- T=0.70 有 Hosmer &amp; Lemeshow (2000) justification\n- \"Theoretical Grounding\" 标题过大——改为 \"Theoretical Motivation\"\n- 19 特征的 VIF>10 多重共线性应在 §3.3（而非 §4.2）首次提及\n- LoRA 链单种子应在主文显式声明并讨论影响\n\n### §4 Depth Degradation Atlas\n- Table 2 主要结果清晰但缺 CI\n- §4.2 特征重要性分析扎实（三重验证）\n- §4.3 EDD 分析是论文最精彩部分——AUC decay curves 直观有力\n- Figure 2 heatmap 字体偏小，影响打印可读性\n\n### §5 Generalization and Robustness\n- §5.1 Binoculars 等价结果需在主文更充分讨论（计算效率差异、具体优势场景）\n- §5.3 Cross-strategy 45.9% 应更 prominently 讨论对实用性的影响\n- §5.4 \"Preliminary\" 定位适当，但 14B EDD=0 的含义（方法有效边界、是否存在参数量阈值使统计指纹方法不可行）讨论严重不足\n\n### §6 Discussion\n- 深度不足——缺乏 \"why does signal attenuate with scale?\" 的机制分析\n- Curation 主张过于 speculative（p>0.4 evidence, B.22 PoC 不显著）\n\n### Limitations\n- 覆盖了 full-replacement vs accumulation 和 scale boundaries\n- 遗漏：仅英文文本、仅 Wikipedia seed corpus、仅 LoRA fine-tuning、参考模型依赖作为独立限制\n\n### 格式合规\n- 主文 8 页 ✓\n- 匿名合规（\"Anonymous ACL submission\"）✓\n- 引用格式基本规范（natbib）✓\n- Ethics Statement 合规 ✓\n- Limitations 长度合适 ✓",
  "project": "recursive_gen_depth_est",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 Findings",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Round**: 18 (fresh review)\n**Reviewers**: R1 (方法严谨性+实验充分性), R2 (新颖性+完整性+写作质量)\n\n---\n\n## Summary\n\n本文提出将递归生成深度估计形式化为序数分类，构建 3 模型×3 解码策略×4 深度的 180K 样本基准，使用 19 维统计特征（perplexity 尾部统计量为主）+ Random Forest 分类器进行深度估计，并提出 Effective Discriminable Depth (EDD) 度量。在 1-1.5B 规模 in-distribution 下表现出色（d1-d3: 59-82%），但方法论无创新（标准特征+标准分类器），full-replacement 假设脱离现实，14B 规模下 EDD=0（self-ref 50.8%），跨策略迁移 d1-d3 仅 45.9%。\n\n---\n\n## Strengths\n\n**S1. 任务定义新颖且有实际意义。** 将 AI 文本检测从二分类推进到有序深度估计，与 model collapse 文献直接对接。这一 framing 在现有文献中是新的。[共识]\n\n**S2. EDD 度量设计优雅且实用。** Definition 1 (§3.4) 提供可操作的单一数字量化\"深度信号能穿透多远\"，与 contraction factor α^d 的理论关联建立了与 model collapse 理论的桥梁。[共识]\n\n**S3. 实验设计系统。** 3×3×4 网格变量控制合理，180K 样本量充分，跨模型/跨策略/跨规模/跨域四个泛化轴全面覆盖。[共识]\n\n**S4. 特征重要性三重验证。** Gini/SHAP/permutation importance 三种方法一致确认 perplexity tail features 主导深度判别（Kendall's W=0.90, p<0.005），跨条件 Spearman ρ̄=0.868。[共识]\n\n**S5. 附录极其详尽。** 17 页 29 个子实验（B.1-B.29），几乎预先回答了所有可预见的 reviewer 问题。诚实报告负面结果（cross-strategy 45.9%、14B EDD=0、DCOL 训练失败）。[共识]\n\n**S6. 引用体系干净可靠。** 75 条 bib entries 验证通过，63 条在线确认，无假引用，4 条 author order mismatch 均为 API 差异。[共识]\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**C1. 方法论创新不足——标准特征+标准分类器** [R2-N1, R1 AGREE]\n19 个特征均非新提出（见于 GLTR/DetectGPT/Ghostbuster），分类器为标准 RF 且无超参搜索（B.29）。论文自我定位为 \"benchmark-driven empirical study\"（§1），但 EMNLP Excitement 维度要求 \"something interesting\"——方法层面贡献接近零。R1 认为任务定义本身提供 excitement（Excitement 3.5/5），R2 认为不够（2.5/5），但双方均认同方法论零创新。四个分类器在跨模型迁移下收敛至 0.8pp 以内（§5.1）虽然支持 \"feature-determined ceiling\" 论点，但也强化了\"方法不重要\"的印象。\n\n**C2. Full-replacement 假设严重限制生态效度** [R2-N2 critical, R1 升级同意 critical]\n整个实验基于 full-replacement chain——每代完全替换训练数据。现实中递归污染几乎都是 accumulation 模式（Gerstgrasser et al., 2024）。论文仅在 §8 Limitations 用一句话提及 pilot accumulation 结果（14-15pp 衰减），无系统实验。Full-replacement 是信号最强的设定，14-15pp 衰减意味着 accumulation 下方法性能可能大幅退化。这不仅是 limitation，而是对论文实际价值的根本性质疑。\n\n**C3. 14B EDD=0——方法在当代模型规模下已失效** [R2-N3, R1 AGREE 并自纠加重]\nSelf-reference 准确率仅 50.8%（2× chance），EDD=0：连 d0（人类）vs d1（首代生成）都无法区分（d0/d1 AUC=0.56-0.64，均低于 T=0.70；Appendix B.14 Table 17）。Cross-reference 下 EDD=2 但准确率仅 44.1%。14B 已非前沿规模（GPT-4/Claude 远超此量级），EDD=0 暗示方法在更大模型上可能彻底失效。§6 Discussion 对此语气过于轻描淡写，未讨论方法的有效边界在哪里。R1 Round 1 中错误引用 85.8%（实为 50.8%），自纠后认为问题比原先评估更严重。\n\n**C4. 跨策略迁移失败** [R1-N2, R2 AGREE]\nd1-d3 跨策略迁移平均 45.9%（Table 6, chance=33%），仅高于随机 13pp。Two-stage pipeline（Appendix B.28）恢复 11.5pp 但最终仍仅 ~57%，远未达到实用水平。实际应用中解码策略通常未知，方法部署场景极为有限。论文动机（Abstract: \"yet no method estimates...\"）暗示通用性，但证据仅支持 within-strategy 使用。\n\n### Warning (Should-Fix)\n\n**W1. LoRA 链种子不足** [R1-N1 critical → R2 REBUT → 共识降为 warning]\n每个 cell 仅一条 LoRA 链（seed=42）。R1 认为无法排除 idiosyncratic artifacts，列为 critical。R2 指出 Appendix B.16 已有 seed=43 的 cross-seed replication（+0.14 to +3.17pp，CI 重叠），初步排除 artifact 可能，建议降级为 warning。共识：2 个种子有限但已初步缓解 artifact 风险，应增加到 3-5 个种子。\n\n**W2. 未进行多重比较校正** [R1-W1, R2 AGREE]\nFootnote 3（§3.5）承认 p-values 为 exploratory 未做校正，但主文多处基于未校正 p-value 做确定性声明（如 §4.3 \"p<0.001\"、§5.1 \"p>0.05\"）。100+ 统计测试量级，应至少报告 FDR-corrected 结果或做 sensitivity check。\n\n**W3. Neural baseline 对比可能不公平** [R1-W3, R2 部分 REBUT]\n仅用 base-size PLMs（DeBERTa-v3-base ~184M, RoBERTa-base ~125M）。R2 指出 B.5 中 DeBERTa-v3-large 因 DCOL 框架数值不稳定而失败（非故意回避），但标准 fine-tuning 的 large 变体未尝试。此外 RF 与 PLM 的信息 access 不同（reference-model perplexity features vs raw text），对比的公平性存疑。\n\n**W4. Binoculars 统计等价削弱独特价值** [R1-W4, R2 AGREE]\nBinoculars 11-feature calibrated 达到 78.1% vs 19-feature RF 78.4%（§5.1, p>0.05）。已有方法 calibration 后即可匹敌，19-feature pipeline 的增量价值不清。计算效率差异（单模型 forward pass vs 双模型）未讨论。\n\n**W5. 参考模型依赖性未充分讨论为部署限制** [R1-W5, R2 AGREE]\nPipeline 依赖固定参考模型（Pythia-1.4B）提取特征。跨架构切换导致 4-11pp 下降（B.13），跨规模更大。部署时需选择合适参考模型但论文未提供选择指南。Limitations 未将其列为独立限制。\n\n**W6. 术语不一致** [R2-W3, R1 AGREE]\nTitle/Abstract 用 \"estimation\"（暗示连续值预测），§3.1 定义为 \"ordinal classification\"。全文交替使用两个术语。应统一或在首次出现时声明等价。\n\n**W7. Downstream curation PoC 不足** [R2-W4, R1 AGREE]\nAppendix B.22 的 PoC 过于 toy（Pythia-410M, 单种子, PPL 变化 0.03-0.12, 不显著 p>0.4）。§6 \"depth-aware curation\" 主张与 evidence 力度不匹配。\n\n### Minor\n\n**M1.** d0 样本是否跨 cell 共享未显式声明 [R2-M1, R1 AGREE]\n**M2.** Table 2 主表未报告 CI/std，仅在文字中零散提及 [R2-M2, R1 AGREE]\n**M3.** §3.5 \"Theoretical Grounding\" 标题过大，内容为 post-hoc motivation [R2-M3, R1 AGREE]\n**M4.** \\cite/\\citet 格式不一致 [R2-M4, R1 AGREE]\n**M5.** VIF>10 的 14-16/19 特征，实际独立维度 ~4-5，应在 §3.3 更早提及 [R1-M1, R2 AGREE]\n**M6.** 生成长度固定 512 tokens，B.18 显示 128 tokens 时 accuracy ~66%，短文本推广未讨论 [R1-M3]\n**M7.** RF 无超参搜索（B.29 确认），200 trees 为默认值 [R1-M2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全一致：\n1. **Overall 3.0 (Findings)** — 独立给出相同评分\n2. **任务定义是最重要的贡献** — EDD 度量有独立价值\n3. **14B EDD=0 构成核心叙事威胁** — self-ref 50.8% 无法区分 d0/d1\n4. **Cross-strategy 45.9% 是实用性的主要障碍** — 策略未知时方法接近失效\n5. **Accumulation 是最大实验缺口** — full-replacement 结论无法直接推广\n6. **方法论无创新** — 标准特征 + 标准分类器\n7. **引用体系干净** — 无假引用\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**1. LoRA 种子严重程度**：R1 列为 critical，R2 提供 B.16 证据 REBUT 并建议降为 warning。R1 未在交叉回应中直接反驳。**结论：降为 warning。B.16 初步排除 artifact 但 2 个种子统计功效不足。**\n\n**2. Excitement 评分**：R1 给 3.5/5（任务定义新颖性驱动），R2 给 2.5/5（方法零创新压制 excitement）。R1 REBUT R2-W2 指出 strategy > model effect 和 cross-ref 提升 EDD 是 non-trivial findings。**结论：分歧合理，反映 task novelty vs method novelty 的权重偏好。合并取 3.0/5。**\n\n**3. Soundness 评分**：R1 给 ~2.5-3.0/5（实验 gap），R2 给 3.5/5（受限条件下执行质量高）。**结论：两者视角互补。合并取 3.0/5。**\n\n**4. Benchmark study 定位**（R2-W2, R1 REBUT）：R2 认为三个 findings 不 surprising；R1 指出 strategy > model effect 和 cross-ref 提升 EDD 是 non-trivial findings，引用 EMNLP 接受 benchmark 论文先例。**结论：benchmark study 在 EMNLP 可接受但需更强的 surprising insight。不列入合并 weakness。**\n\n**5. Figure 1 信息密度**（R2-W5, R1 REBUT）：R2 认为偏低浪费空间，R1 认为任务定义图的信息密度适当。**结论：分歧不影响评分，不列入合并 weakness。**\n\n---\n\n## Questions for Authors\n\n**Q1.** [共识] Accumulation 模式下的系统性实验结果？至少一个模型在 25/50/75% 混合比例下的 EDD？\n**Q2.** [共识] 14B 能否用同族不同规模模型（如 Pythia-6.9B）分离 self-reference vs scale effect？\n**Q3.** [共识] Binoculars in-distribution 等价——19-feature pipeline 的具体优势场景？计算效率差异？\n**Q4.** [共识] 是否探索过策略不变特征子集以改善 cross-strategy transfer？\n**Q5.** [R2] 19 特征中有多少是本文首创的？\n**Q6.** [R1] 为什么不做多重比较校正？关键结论在 FDR 校正后是否仍显著？\n**Q7.** [R2] 两阶段 pipeline 的策略分类阶段准确率是多少？\n**Q8.** [R1] B.16 的 2 个 LoRA 种子是否足够？是否有更多种子的实验？\n\n---\n\n## Missing References\n\n**共识推荐：**\n- Carlini et al. (2021) \"Extracting Training Data from Large Language Models\" — data provenance motivation [R1 标注为最重要缺失]\n- Rothe et al. (2018) \"Deep ordinal regression\" — ordinal classification 方法论 [R2 推荐, R1 同意]\n\n**建议补充：**\n- Guo et al. (2025) \"Generative AI May Prefer to Present Scientific Uncertainties as Certainties\"\n- Li et al. (2024) \"Synthetic Data (Almost) from Scratch\"\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warning, 7 info, 0 critical）：\n\n**Warnings：**\n- pp.1-2 连续两页纯文本无 display item，审稿人第一印象 text-heavy。建议提前 Figure 1 或加 teaser\n- p.8 极度拥挤——4 个 display items（Table 4, Figure 4, Table 5, Table 6）+ 4 个章节（§5.2/5.3/5.4/6）。建议移部分表格至 Appendix\n- p.7 Figure 2 feature importance heatmap 内部字体偏小，打印可读性受影响\n\n**Info：**\n- Figure 3 仅用颜色区分线条，缺 line style/marker 辅助（灰度/色盲不友好）\n- Figure 4 混淆矩阵尺寸偏小\n- Tables 2/3 booktabs 格式规范 ✓\n- Table 1 排版清晰 ✓\n- References 格式统一无 [?] ✓\n- Appendix 表格格式与正文一致 ✓\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n**置信度: 4.5/5** — 两位 Reviewer 独立审稿后达成完全一致的评分，交叉讨论解决了主要分歧。\n\n**评分依据（EMNLP 2026 ARR 标准）：**\n\n| 维度 | 合并评分 | 理由 |\n|------|----------|------|\n| Soundness | 3.0/5 | 在受限条件下（1-1.5B, in-distribution）实验质量高，但 14B EDD=0、cross-strategy 45.9%、limited seed chain、无 accumulation 系统实验构成显著缺口 |\n| Excitement | 3.0/5 | 任务定义有价值（R1: 3.5），但方法论零创新压制（R2: 2.5），取中值 |\n| Reproducibility | 3.5/5 | 超参报告完整（B.29），特征定义清晰，承诺释放代码。LoRA 种子有限降低完全复现信心 |\n\n**总评：** 论文提出了有价值的新任务（递归深度估计）和实用度量（EDD），在 1-1.5B 规模 in-distribution 条件下提供了详尽的实证刻画。但四个 critical 问题——方法论无创新（标准特征+RF）、核心假设脱离现实（full-replacement）、方法在 14B 规模已失效（EDD=0）、跨策略迁移接近失效（45.9%）——叠加使论文达不到 Conference（4.0）门槛。作为 Findings（3.0）论文，任务定义的原创性、EDD 度量的价值、引用和实验的高质量执行支撑其发表。\n\n**达到 Conference (4.0) 所需：**\n1. 至少一组系统的 accumulation 实验（25/50/75% 混合比例下的 EDD）\n2. 14B 使用同族参考模型（如 Pythia-6.9B）分离 self-reference confound\n3. 引入一个 non-trivial 方法改进或 surprising finding 提升 Excitement\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 数字密度适中（~6 个关键数字），\"three findings\" 结构清晰\n- 14B 结果呈现准确（EDD=2, cross-reference 条件），但应更显著标注规模限制\n\n### §1 Introduction\n- 动机推进自然（model collapse → binary detection → depth estimation）\n- \"benchmark-driven empirical study\" 定位诚实但限制论文上限\n- 贡献 3 正确标注 cross-strategy 为 boundary condition\n\n### §2 Related Work\n- 覆盖全面，组织清晰\n- 缺 Carlini et al. (2021) 作为 data provenance 补充\n- 与 GLTR 的关系（同用统计特征，不同任务定义）应更明确讨论\n\n### §3 Method\n- Problem definition 和 EDD 定义（Definition 1）清晰\n- T=0.70 有 Hosmer &amp; Lemeshow (2000) justification\n- \"Theoretical Grounding\" 标题过大——改为 \"Theoretical Motivation\"\n- 19 特征的 VIF>10 多重共线性应在 §3.3（而非 §4.2）首次提及\n- LoRA 链单种子应在主文显式声明并讨论影响\n\n### §4 Depth Degradation Atlas\n- Table 2 主要结果清晰但缺 CI\n- §4.2 特征重要性分析扎实（三重验证）\n- §4.3 EDD 分析是论文最精彩部分——AUC decay curves 直观有力\n- Figure 2 heatmap 字体偏小，影响打印可读性\n\n### §5 Generalization and Robustness\n- §5.1 Binoculars 等价结果需在主文更充分讨论（计算效率差异、具体优势场景）\n- §5.3 Cross-strategy 45.9% 应更 prominently 讨论对实用性的影响\n- §5.4 \"Preliminary\" 定位适当，但 14B EDD=0 的含义（方法有效边界、是否存在参数量阈值使统计指纹方法不可行）讨论严重不足\n\n### §6 Discussion\n- 深度不足——缺乏 \"why does signal attenuate with scale?\" 的机制分析\n- Curation 主张过于 speculative（p>0.4 evidence, B.22 PoC 不显著）\n\n### Limitations\n- 覆盖了 full-replacement vs accumulation 和 scale boundaries\n- 遗漏：仅英文文本、仅 Wikipedia seed corpus、仅 LoRA fine-tuning、参考模型依赖作为独立限制\n\n### 格式合规\n- 主文 8 页 ✓\n- 匿名合规（\"Anonymous ACL submission\"）✓\n- 引用格式基本规范（natbib）✓\n- Ethics Statement 合规 ✓\n- Limitations 长度合适 ✓",
    "project": "recursive_gen_depth_est",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 Findings",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1595 · 2026-05-21T21:57:00.964350+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4235
}
```

</details>

---


### Assistant

_source line 1596 · 2026-05-21T21:57:10.603036+00:00_

审稿报告已投递至 Research Director。

**审稿完成摘要：**

- **Overall: 3.0 (Findings)**，置信度 4.5/5
- 两位 Reviewer 独立给出相同评分，交叉讨论后共识强化
- **4 个 Critical 问题**：方法论零创新、full-replacement 假设脱离现实、14B EDD=0 方法失效、跨策略迁移 45.9% 接近失效
- **7 个 Warning**：LoRA 种子不足、无多重比较校正、neural baseline 不公平、Binoculars 等价、参考模型依赖、术语不一致、curation PoC 不足
- **视觉审查**：3 warning（pp.1-2 无视觉锚点、p.8 拥挤、Figure 2 字体小），无 critical
- **Issue Tracker** 已同步更新至 Round 18

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 147

## Round 147

2 recorded events


### User

_source line 1597 · 2026-05-21T21:57:13.162407+00:00_

[Reviewer 1 审稿结果]:
已完成对 R2 审稿意见的逐条回应并提交给 Director。

核心结论：
- **N1/N2/N3**：三个 critical 问题全部 [AGREE]，其中 N3（14B EDD=0）经核实比我 Round 1 评估更严重（我之前误引了 85.8% 的数字，实际为 50.8%）
- **W2/W5/M5**：三处 [REBUT]——benchmark 论文在 EMNLP 可接受、Figure 1 信息密度适当、长附录是优势
- 维持 Overall 3.0 (Findings)，两位 reviewer 独立达到相同分数

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1598 · 2026-05-21T21:57:25.239561+00:00_

审稿报告已投递给 Research Director。

**Round 18 审稿完成。** 两位 Reviewer 独立给出 **Overall 3.0 (Findings)**，交叉讨论后完全收敛。

核心结论：
- **4 个 critical**：方法论零创新、full-replacement 脱离现实、14B EDD=0 方法失效、跨策略迁移 45.9%
- **7 个 warning**：LoRA 种子不足、无多重比较校正、neural baseline 可能不公平、Binoculars 等价、参考模型依赖、术语不一致、curation PoC 不足
- **达到 Conference (4.0) 所需**：accumulation 系统实验 + 14B confound 分离 + 方法层面改进
- Issue Tracker 已同步更新至 Round 18

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 148

## Round 148

132 recorded events


### User

_source line 1599 · 2026-05-22T22:49:34.128565+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recursive_gen_depth_est
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1600 · 2026-05-22T22:49:39.853546+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1601 · 2026-05-22T22:49:39.904498+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1602 · 2026-05-22T22:49:46.178022+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1603 · 2026-05-22T22:49:46.178380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1604 · 2026-05-22T22:49:52.156079+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1605 · 2026-05-22T22:49:54.164096+00:00_

{"result":"# 项目 recursive_gen_depth_est 概况\n\n## 实验状态 (152 个)\n\n- **cross_model_olmo_temp09_001**: DONE (killed) — \n- **pythia_topk50_001**: DONE (success) — \n- **cross_model_gpt2xl_001**: DONE (success) — \n- **cross_model_olmo_002**: DONE (success) — \n- **pythia_temp09_001**: DONE (success) — \n- **mvp_pipeline_pythia_002**: DONE (success) — \n- **cross_model_olmo_001**: DONE (failed) — \n- **mvp_pipeline_qwen_base_004**: DONE (killed) — \n- **mvp_pipeline_pythia_001**: DONE (killed) — \n- **mvp_pipeline_base_002**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (killed) — \n- **mvp_pipeline_001**: DONE (killed) — \n- **mvp_pipeline_base_003**: DONE (killed) — \n- **mvp_pipeline_004**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| qwen25_7b_selfref_001 | Recursive generation depth signal (d0-d3) should persist in Qwen2.5-7B with self-reference feature extraction, similar to 14B scale results, supporting that the phenomenon is not model-scale-specific. | — | — | — |\n\n## 待处理\n- accum_v2_mix25（准备中）\n- accum_v2_mix50（准备中）\n\n## 近期结论\n- **plan_020_bootstrap_ci** (success): B=10,000 bootstrap resampling of per-sample 5-fold CV predictions provides stable 95% CIs for the 9 atlas cells, confirming that B=1,000 CIs had already converged.\n- **plan_018_ordinal_baseline_v2** (success): Binary detection methods (Binoculars, Fast-DetectGPT) produce continuous scores that primarily distinguish d0 vs d1+; their ordinal resolution across d1/d2/d3 is near-chance, lacking the depth gradient captured by our 19-feature statistical pipeline.\n- **accum_olmo_temp_mix50** (success): OLMo-1B temp0.9 accumulation at 50% human mix ratio shows further depth signal degradation vs mix25 (73.47%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%) and Pythia pattern, confirming cross-model consistency of a
…[truncated 1841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2008
}
```

</details>

---


### Tool call

_source line 1606 · 2026-05-22T22:49:54.164476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1607 · 2026-05-22T22:49:54.415686+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\setlength{\dbltextfloatsep}{4pt plus 2pt minus 2pt}
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{method}
38	
39	\input{theory}
40	
41	\input{atlas}
42	
43	\input{generalization}
44	
45	\input{discussion}
46	
47	\input{conclusion}
48	
49	\bibliography{references}
50	
51	\clearpage
52	\appendix
53	\input{section_appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1608 · 2026-05-22T22:49:54.466288+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "report.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "report.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 1609 · 2026-05-22T22:49:54.517021+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| qwen25_7b_selfref_001 | Recursive generation depth signal (d0-d3) should persist in Qwen2.5-7B with self-reference feature extraction, similar to 14B scale results, supporting that the phenomenon is not model-scale-specific. | — | — | — |\\n\\n## 待处理\\n- accum_v2_mix25（准备中）\\n- accum_v2_mix50（准备中）\\n\\n## 近期结论\\n- **plan_020_bootstrap_ci** (success): B=10,000 bootstrap resampling of per-sample 5-fold CV predictions provides stable 95% CIs for the 9 atlas cells, confirming that B=1,000 CIs had already converged.\\n- **plan_018_ordinal_baseline_v2** (success): Binary detection methods (Binoculars, Fast-DetectGPT) produce continuous scores that primarily distinguish d0 vs d1+; their ordinal resolution across d1/d2/d3 is near-chance, lacking the depth gradient captured by our 19-feature statistical pipeline.\\n- **accum_olmo_temp_mix50** (success): OLMo-1B temp0.9 accumulation at 50% human mix ratio shows further depth signal degradation vs mix25 (73.47%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%) and Pythia pattern, confirming cross-model consistency of accumulation mixing effects\\n\\n## 趋势\\n成功 94 / 负向 14 / 失败 17 / 共 149\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ngpu-6000pro-2: 无 GPU 信息\\n\\n## 告警\\n- mvp_pipeline_001: 已被终止 — unknown\\n- mvp_pipeline_002: 已被终止 — unknown\\n- mvp_pipeline_003: 已被终止 — unknown\\n- mvp_pipeline_004: 已被终止 — unknown\\n- mvp_pipeline_base_002: 已被终止 — unknown\\n- mvp_pipeline_base_003: 已被终止 — unknown\\n- mvp_pipeline_pythia_001: 已被终止 — unknown\\n- mvp_pipeline_qwen_base_004: 已被终止 — unknown\\n- cross_model_olmo_001: 训练失败 — unknown\\n- dcol_deberta_001: 训练失败 — unknown\\n- cross_model_olmo_temp09_001
…[truncated 1447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-22T22:50:06.022208+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1611 · 2026-05-22T22:50:06.424077+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1612 · 2026-05-22T22:50:06.424542+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1613 · 2026-05-22T22:50:06.475043+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1614 · 2026-05-22T22:50:07.078048+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1615 · 2026-05-22T22:50:07.128649+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1616 · 2026-05-22T22:50:10.541383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-22T22:50:11.144239+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K cell-instances (140K unique passages) spanning three model families, three decoding strategies, and four depths under controlled full-replacement chains at the 1--1.5B parameter scale.
4	A lightweight pipeline (19 statistical features classified by Random Forest) achieves d1--d3 balanced accuracy of 59--82\% across nine model--strategy cells, with $\mathrm{EDD}_{0.70} = 3$ in 8/9 cells.
5	Three findings emerge: (1)~depth signal concentrates in perplexity distribution tails, corroborated by classifier convergence and independent cross-perplexity features; (2)~decoding strategy affects cross-condition transfer more than model architecture, suggesting structurally distinct degradation trajectories; (3)~signal attenuates with scale (14B cross-reference accuracy ${\sim}44$\%, $\mathrm{EDD}_{0.70}{=}2$ for nucleus and temperature, 0 for top-$k$), with reference-model choice accounting for ${\sim}7$\,pp of the apparent degradation.
6	Our depth estimation claims hold most strongly within-strategy or when the decoding configuration is known; a two-stage routing pipeline recovers $+$11.5\,pp under cross-strategy transfer.
7	Perturbation-based and membership-inference baselines lack ordinal depth resolution, confirming that depth estimation requires distributional statistics beyond binary detection scores.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1618 · 2026-05-22T22:50:11.144643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1619 · 2026-05-22T22:50:11.646727+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	We focus on the 1--1.5B parameter regime under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination involves partial mixing at unknown proportions; full replacement provides an upper bound on depth signal strength (\S\ref{sec:discussion}).
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors \cite{binoculars2024,fast_detectgpt2024,diveye2026} collapse all depths $d \geq 1$ into a single category, a limitation we confirm empirically: their pairwise d1-vs-d2 AUC collapses to chance level (\S\ref{sec:gen:baselines}); watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone (Figure~\ref{fig:problem}).
13	
14	We find that 
…[truncated 3162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-22T22:50:11.697319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1621 · 2026-05-22T22:50:12.701542+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad} and Markovian generation chains \cite{geng2026_markovian}.
6	Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
7	Mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, data scaling under constraint \cite{muennighoff2023scaling}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence analysis \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026} are active areas.
8	\citet{kazdan2025_collapse_or_thrive} systematically compare training workflows and show that data accumulation avoids collapse while pure replacement does not; \citet{suresh2025_rate_collapse} characterize the rate of collapse for fundamental distributions under recursive maximum-likelihood estimation.
9	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier that reveals strategy-dependent trajectories and
…[truncated 3907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1622 · 2026-05-22T22:50:12.752315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-22T22:50:13.204504+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	We use \emph{depth estimation} as shorthand throughout; the underlying task is ordinal classification.
13	Depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
14	
15	\subsection{Multi-Generational Benchmark Construction}
16	\label{sec:method:benchmark}
17	
18	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
19	
20	\paragraph{Model families.}
21	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
22	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
23	
24	\paragraph{Decoding strategies.}
25	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
26	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
27	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
2
…[truncated 6294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-22T22:50:13.204835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 1625 · 2026-05-22T22:50:13.706683+00:00_

1	\subsection{Theoretical Motivation}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed jointly with surprisal variance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), predicting weaker per-step signal.
15	Qwen2.5-14B supports this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B; \S\ref{sec:gen:crossscale}); 7--8B results are mixed, suggesting additional confounds interact with the scale effect (Appendix~\ref{app:cross_scale_full}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-22T22:50:13.707068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-22T22:50:14.209146+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells at the 1--1.5B parameter scale, evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}10{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: mean absolute error (MAE)\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references (Appendix~\ref{app:r
…[truncated 9658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-22T22:50:14.209542+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-22T22:50:14.661451+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares methods across all 9 cells.
10	Four classifiers (RF, XGBoost, ordinal MLP, prototypical) converge within 0.8\,pp under cross-model transfer (Appendix~\ref{app:learned_estimator}), confirming a feature-determined accuracy ceiling.
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA, 53--61\%) and RoBERTa-DCOL (ordinal contrastive, 64.5\%) lag RF by 14--32\,pp per cell; implications are discussed in \S\ref{sec:discussion}.
14	
15	\paragraph{Binary detectors and membership inference.}
16	Perturbation-based (DetectGPT, 28.8\%) and membership-inference (Min-K\% Prob, 33.2\%) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); Binoculars d1v2 AUC\,=\,0.50--0.53 vs.\ RF 0.93 (Appendix~\ref{app:detector_baselines}). Binoculars convergence with our pipeline is discussed in \S\ref{sec:discussion}.
17	
18	\paragraph{Surface-text ablation.}
19	Single-feature regression on mean perplexity (25.1\%) and zero-shot LLMs (best 36.2\%; Appendix~\ref{app:zeroshot_prompt}) confirm depth signal is inaccessible from surface text.
20	
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Method comparison (RF mean across 9 cells, 5-fold CV). Chance = 25\% / 33.3\% (d1--d3). $^\dagger$Adapted from binary detection; Binoculars 11-feat: $p{>}0.05$ vs.\ 19-feat RF (paired permutation test).}
25	\label{tab:baselines}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{@{}llcc@{}}
28	\toprule
29	Method & Calibration & 4-Cl (\%) & d1--d3 (\%) \\
30	\midrule
31	RF 19-feature (ours) & RF & 78.4 & \textbf{71.6} \\
32	Binoculars$^\dagger$ \cite{binoculars2024} &
…[truncated 2736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1630 · 2026-05-22T22:50:14.661865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1631 · 2026-05-22T22:50:15.214286+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Multi-channel depth encoding.}
5	Four importance measures (Gini, SHAP, permutation, CPI; Kendall's $W{=}0.90$) converge on the same feature ranking, and Binoculars-derived features independently reach 78.1\% ($p{>}0.05$ vs.\ 78.4\%; merged: 82.6\%).
6	Depth signal is a distributional property encoded across multiple statistical channels, not a single exploitable artifact.
7	
8	\paragraph{Why neural methods underperform.}
9	End-to-end classifiers (DeBERTa, RoBERTa-DCOL) lag RF by 14--32\,pp (\S\ref{sec:gen:baselines}) despite full token-level context, confirming that depth is encoded in distributional tail statistics that pretrained representations do not capture (d2 recall as low as 8\%); targeted feature engineering is necessary, not merely convenient.
10	
11	\paragraph{Feature hierarchy across depths.}
12	The importance transition from \texttt{var\_surprisal} at shallow boundaries to perplexity tail statistics at deeper ones (\S\ref{sec:atlas:features}) mirrors tail-contraction dynamics: early recursion narrows the surprisal distribution while later steps erode the perplexity tail, consistent with geometric contraction (\S\ref{sec:method:theory}).
13	
14	\paragraph{Deployment considerations.}
15	The strategy effect (9.3\,pp) exceeding the model effect (7.2\,pp) requires auditing pipelines to condition on decoding configuration (\S\ref{sec:gen:crossstrategy}), echoing \citet{schaeffer2025}; scale attenuation at 14B (\S\ref{sec:gen:crossscale}) may be partially recoverable via scale-matched references.
16	
17	\paragraph{Accumulation and outlook.}
18	Depth estimation bridges binary detection and model collapse research by providing ordinal resolution \cite{drayson2025_detection_prevents_collapse}.
19	Accumulation experiments at 25--50\% synthetic mixing (Appendix~\ref{app:accumulation_auc}) partially validate depth estimation under realistic conditions: $\mathrm{EDD}_{0.70}{=}3$ is preserv
…[truncated 516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1632 · 2026-05-22T22:50:15.214668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1633 · 2026-05-22T22:50:16.268789+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	The primary benchmark uses full-replacement chains; real-world contamination involves accumulation at unknown mixing ratios \cite{gerstgrasser2024_accumulate}.
6	Accumulation experiments (Appendix~\ref{app:accumulation_auc}) show accuracy attenuation that increases with higher synthetic mixing ratios, and do not test cross-strategy accumulation; extension to larger models and higher mixing ratios remains future work.
7	
8	\paragraph{Scale, generalization, and reference model.}
9	Depth signal attenuates at larger scales (\S\ref{sec:gen:crossscale}), with reference-model mismatch contributing to the observed degradation.
10	Cross-strategy transfer can invert adjacent-depth predictions when the classifier's training strategy differs from the test data, requiring strategy-aware deployment.
11	The pipeline requires a fixed reference model; cross-architecture references degrade accuracy (Appendix~\ref{app:ref_ablation}).
12	Additional caveats (single LoRA seed, web-crawl false positive rates, passage length sensitivity) are detailed in the Appendix.
13	
14	\section*{Ethics Statement}
15	
16	This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
17	No human subjects were involved, no private or sensitive data were collected, and no new models were released.
18	Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
19	Code and data will be released upon acceptance.
20	AI assistants were used in an auxiliary role for coding support and language polishing.
21	All scientific decisions, experimental design, analysis, and core writing were conducted by the authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1634 · 2026-05-22T22:50:16.269219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-22T22:50:16.821430+00:00_

File content (27284 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1636 · 2026-05-22T22:50:16.821796+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1637 · 2026-05-22T22:50:23.202009+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the web search results, I fo
…[truncated 1325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6380
}
```

</details>

---


### Tool call

_source line 1638 · 2026-05-22T22:50:28.611706+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission deadline guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle submission deadline guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 1639 · 2026-05-22T22:50:31.421691+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1640 · 2026-05-22T22:50:31.422309+00:00_

1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale 7--8B experiments (Appendix~\ref{app:cross_scale_full}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$; the 14B model uses FP16 LoRA with the same rank and scaling.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuat
…[truncated 16393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1641 · 2026-05-22T22:50:31.924131+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1642 · 2026-05-22T22:50:42.160745+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission deadline guidelines page limit"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Let me search for more specific information about the May 2026 cycle submission deadline and page limits.

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclro
…[truncated 2339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 13549
}
```

</details>

---


### Tool result

_source line 1643 · 2026-05-22T22:50:42.162745+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/decisions.yaml\", \"content\": \"_next_id: 53\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 14:03 UTC\\n  summary: MVP PASS — 递归生成深度可从统计特征高精度区分，进入 research phase\\n  rationale: Pythia-1.4B 4-depth pipeline 验证核心假设：4-class acc 78.2% (>>40% threshold),\\n    d1v2 AUC 0.861 (>>0.6 threshold)。控制实验排除域混淆（过滤代码后 acc 提升至 81.6%）。Top 特征为 surprisal\\n    variance 和 perplexity percentiles，说明信号来自分布窄化而非内容差异。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_pythia_002\\n    role: primary\\n    result: 4-class acc 78.2%, d1v2 AUC 0.861, content-type control 81.6%\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:01 UTC\\n  summary: Dream 三档分析完成：6项结构性必修+framing重心从DCOL转向Atlas/EDD\\n  rationale: Dream dream_20260514T140607 full review 完成。三档(best=borderline accept\\n    3.0, median=Findings 3.0, worst=borderline Findings 2.5)一致指出6项结构性问题：(1)DCOL loss\\n    Eq.1缺repulsive term不可复现 (2)Atlas论文零图不可接受 (3)bibliography严重不足(3-10 refs,需25+) (4)d0\\n    confound膨胀headline metrics,需报d1-d5 acc (5)EDD threshold无sensitivity analysis (6)surprisal\\n    reference model未指定有circularity风险。三档均认为Atlas/EDD是primary contribution,DCOL incremental\\n    over CLOC——与我们的contingency plan方向一致。worst case下DCOL不显著(p=0.12),EDD=2,但任务formalization+Atlas仍可支撑Findings。关键风险：cross-model\\n    transfer在worst case降到33%。\\n  related_experiments:\\n  - exp_id: dream_20260514T140607\\n    role: dream_simulation\\n    result: best=3.0 median=3.0 worst=2.5\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 19:45 UTC\\n  summary: 要求 baselines 统一使用 DeBERTa-v3-large，消除与 DCOL 的模型规模混淆变量\\n  rationale: Reviewer 发现 DCOL 用 DeBERTa-v3-large (435M) 而 CE/CORAL baselines 用 DeBERTa-v3-base\\n    (184M)，参数量差 2.4×，审稿人必问改进来源。修改 baseline 脚本支持 large 版本实验成本极低（模型已在服务器上），可彻底解耦方法贡献与模型容量。\\n  related_experiments:\\n  - exp_id: dcol_deberta_001\\n    role: target\\n    result: pending\\n  depends_on: []\\n- id: D00
…[truncated 1450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10238
}
```

</details>

---


### Tool call

_source line 1644 · 2026-05-22T22:50:48.185103+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the following information for ARR 2026 submissions: 1) page limits for long and short papers, 2) template requirements, 3) anonymity rules, 4) appendix rules, 5) citation format requirements, 6) May 2026 submission deadline, 7) any specific formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the following information for ARR 2026 submissions: 1) page limits for long and short papers, 2) template requirements, 3) anonymity rules, 4) appendix rules, 5) citation format requirements, 6) May 2026 submission deadline, 7) any specific formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 1645 · 2026-05-22T22:50:49.490500+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract all ARR 2026 submission deadlines, especially the May 2026 cycle deadline date. List all commitment deadlines for EMNLP 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/dates",
    "prompt": "Extract all ARR 2026 submission deadlines, especially the May 2026 cycle deadline date. List all commitment deadlines for EMNLP 2026."
  }
}
```

</details>

---


### Tool call

_source line 1646 · 2026-05-22T22:50:51.598024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": "300",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "offset": "300",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1647 · 2026-05-22T22:50:51.648853+00:00_

300	\end{tabular}
301	\end{table}
302	
303	\subsection{Feature Overlap Analysis}
304	\label{app:feature_overlap}
305	
306	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
307	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \texttt{var\_surprisal} and \texttt{p90\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.
308	This confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\S\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
309	
310	\subsection{End-to-End Learning}
311	\label{app:e2e}
312	
313	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
314	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
315	
316	\begin{table}[h]
317	\centering
318	\small
319	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
320	\label{tab:e2e_detail}
321	\resizebox{\columnwidth}{!}{%
322	\begin{tabular}{@{}lccccc@{}}
323	\top
…[truncated 20428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1648 · 2026-05-22T22:50:52.452101+00:00_

# ARR 2026 Submission and Commitment Deadlines

## ARR 2026 Submission Deadlines

Based on the schedule provided, there are three submission cycles in 2026:

1. **March 2026 cycle**: "March 16" submission deadline
2. **May 2026 cycle**: "May 25" submission deadline
3. **August 2026 cycle**: "August 3" submission deadline
4. **October 2026 cycle**: "October 12" submission deadline

## EMNLP 2026 Commitment Deadlines

For authors wishing to commit papers to EMNLP 2026, the document specifies that the final ARR submission must occur by "May 25, 2026" with a commitment date of "August 2, 2026."

This means authors have until the May 2026 cycle to submit new papers to ARR if they want those reviews ready before the August commitment deadline for EMNLP 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "elapsed_ms": 2961
}
```

</details>

---


### Tool result

_source line 1649 · 2026-05-22T22:50:54.108514+00:00_

# ARR 2026 Submission Guidelines

## 1) Page Limits
- **Long papers:** "up to eight (8) pages of content" plus unlimited references and a required limitations section
- **Short papers:** "up to four (4) pages of content" plus unlimited references and a required limitations section

## 2) Template Requirements
Papers must follow the "official ACL style template" available on GitHub. Authors cannot modify these files or use templates from other conferences. Submissions must conform to specified styles including "paper size, margin width, and font size restrictions."

## 3) Anonymity Rules
Submissions require two-way anonymized review. Papers must exclude author names and affiliations. Self-citations should be rephrased (e.g., "Smith previously showed..." rather than "We previously showed..."). Supplementary materials and repository links must also be anonymized. Violations result in desk rejection.

## 4) Appendix Rules
Appendices follow the main paper and don't count toward page limits. They must use double-column formatting per ACLPUB guidelines (with approved exceptions). Reviewers aren't required to review appendices, so critical content belongs in the main paper. Materials must be fully anonymized.

## 5) Citation Format Requirements
For concurrent submissions with overlapping topics, anonymized versions should be uploaded as supplementary material with the citation format: "Anonymous (2026). Paper title. Under review."

## 6) May 2026 Submission Deadline
Not specified in the provided document. The page references May 2025 cycles but does not list May 2026 dates.

## 7) Specific Formatting Requirements
Use official ACL formatting guidelines. Papers exceeding length limits or lacking a required limitations section face desk rejection. All text must be "addressed exclusively to the human readers" with visibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "elapsed_ms": 5923
}
```

</details>

---


### Tool call

_source line 1650 · 2026-05-22T22:51:01.984575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": "600",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "offset": "600",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-22T22:51:02.486978+00:00_

600	Strategy & Self-ref (\%) & Cross-ref (\%) & $\Delta$ & $\mathrm{EDD}_{0.70}$ & d0v1 AUC \\
601	\midrule
602	nucleus & 54.1 & 45.0 & $-$9.1 & 2 & 0.702 \\
603	temp ($\tau{=}0.9$) & 50.5 & 46.3 & $-$4.2 & 2 & 0.739 \\
604	top-$k$ ($k{=}50$) & 47.9 & 40.9 & $-$7.1 & 0 & 0.699 \\
605	\cmidrule{2-6}
606	\textit{mean} & \textit{50.8} & \textit{44.1} & $-$\textit{6.8} & --- & --- \\
607	\bottomrule
608	\end{tabular}}
609	\end{table}
610	
611	Cross-reference accuracy drops by 6.8\,pp on average (range 4.2--9.1\,pp), but $\mathrm{EDD}_{0.70}$ \emph{rises} from 0 to 2 for nucleus and temperature: the consecutive d0v1 (0.70--0.74) and d1v2 (0.72--0.73) AUCs now exceed the 0.70 threshold, while d2v3 remains below (0.54--0.61).
612	Under self-reference, the first boundary d0v1 falls below $T{=}0.70$ in all strategies (0.56--0.64), breaking the contiguous prefix and yielding $\mathrm{EDD}_{0.70}{=}0$ even though some later pairs (e.g., nucleus d1v2\,=\,0.713, d2v3\,=\,0.728) exceed the threshold; the Pythia-1.4B reference model provides sharper distributional contrast at the cost of overall accuracy.
613	The ${\sim}$7\,pp accuracy gap between self- and cross-reference is therefore a reference-model artifact, not a depth-signal artifact: depth signal persists at 14B albeit attenuated relative to 1--1.5B.
614	
615	\paragraph{Caveats.}
616	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
617	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
618	
619	\paragraph{Confounds.}
620	\label{app:cross_scale_confounds}
621	Four confounds limit the 7--8B results: (1)~4-bit NF4 QLoRA quantizat
…[truncated 22886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-22T22:51:02.788479+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-22T22:51:02.839091+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1654 · 2026-05-22T22:51:11.774052+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check project config for external review",
  "subagent_type": "Explore",
  "prompt": "Find and read the project configuration file for \"recursive_gen_depth_est\" project. I need to check if external_review.paperreview_ai.enabled is set to true. Look in:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/ for any config/yaml/json files\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/ for global config\n\nReport: the value of external_review.paperreview_ai.enabled and any other external review settings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check project config for external review",
    "subagent_type": "Explore",
    "prompt": "Find and read the project configuration file for \"recursive_gen_depth_est\" project. I need to check if external_review.paperreview_ai.enabled is set to true. Look in:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/ for any config/yaml/json files\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/ for global config\n\nReport: the value of external_review.paperreview_ai.enabled and any other external review settings."
  }
}
```

</details>

---


### Tool call

_source line 1655 · 2026-05-22T22:51:12.727532+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1656 · 2026-05-22T22:51:13.130098+00:00_

issues:
# ============================================================
# ROUND 18 — CRITICAL (Must-Fix)
# ============================================================

- id: R17-N1
  summary: Full-replacement 假设从根本上限制实用价值——accumulation 场景无系统实验
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 17
  last_seen_round: 18
  mentions:
  - {round: 17, reviewers: [1, 2], note: "R1 列为 N1 critical, R2 原列 W2 后升级为 critical。两人共识：pilot accumulation 仅报 -14~-15pp 无 Table/per-cell/EDD/统计检验"}
  - {round: 12, reviewers: [1, 2], note: "历史: R16-W1 (framing) resolved via §6 段落，但实验数据缺口未填补"}
  - {round: 18, reviewers: [1, 2], note: "R18 两人再次共识 critical。R2-N2 列为 critical，R1 交叉回应升级同意 critical。指出 Gerstgrasser et al. (2024) 已论证 accumulation 与 full-replacement 统计行为根本不同。§8 Limitations 仅一句话处理不充分。"}
  action_items:
  - {round: 17, action: "需用户确认是否做新 accumulation 实验。已有 accum_v3 (Pythia nucleus, mix25/mix50) DONE 数据已引用于论文。新增 cells 需新实验。", assigned_to: research_director, status: done}
  - {round: 18, action: "至少一个模型在 25/50/75% accumulation 比例下提供系统性 EDD 结果", assigned_to: research_director, status: in_progress}
  - {round: 18, action: "3-cell mix25 accumulation EDD 计算完成：GPT-2 XL nucleus / OLMo temperature / Pythia nucleus 均 EDD_0.70=3（d2-vs-d3 AUC 0.73-0.76）。论文 §1/§6/§8 已更新。Mix50 实验进行中。", assigned_to: research_director, status: done}
  resolution: ""
  resolution_round: null

- id: R17-N2
  summary: 14B EDD=0 被 self-reference confound 污染——无法分离规模效应 vs 参考模型切换
  category: experiment
  severity: critical
  status: open
  first_raised_round: 17
  last_seen_round: 18
  mentions:
  - {round: 17, reviewers: [1, 2], note: "R1 首次识别 confound（N2 critical），R2 完全认同。14B 用 self-reference 而主表用 Pythia-1.4B cross-reference"}
  - {round: 18, reviewers: [1, 2], note: "R18 两人再次共识 critical。R1 自纠 Round 1 中 85.8% 错误数字（实为 50.8%），认为问题比原评估更严重。Self-ref 50.8% EDD=0 意味着连 d0/d1 都无法区分。Cross-ref 44.1% EDD=2。§6 Discussion 对 EDD=0 含义讨论不足。"}
  action_items:
  - {round: 17, action: "需用户确认。控制实验：Pythia-1
…[truncated 18909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1657 · 2026-05-22T22:51:13.281031+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1658 · 2026-05-22T22:51:13.381774+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1659 · 2026-05-22T22:51:13.582805+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/**/*.{yaml,yml,json,config}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/**/*.{yaml,yml,json,config}"
  }
}
```

</details>

---


### Tool result

_source line 1660 · 2026-05-22T22:51:13.733928+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_data_seed-prep_20260514T095557_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_code_recursive-gen-chain_20260514T095847_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_code_fix-scripts_20260514T100522_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_code_fix-and-launch-pipeline_20260514T100803_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_QUEUED_20260514T102444.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_ALLOCATED_20260514T102448.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_RUNNING_20260514T102454.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_infra_env-setup_20260514T095535_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_check_status-urgent_20260514T105857_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_RUNNING_20260514T110519.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_DONE_20260514T110526.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_infra_kill-instruct-download-base-restart_20260514T110510_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_base_003_QUEUED_20260514T112425.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_
…[truncated 12794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1661 · 2026-05-22T22:51:13.734422+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/*.{yaml,yml,json,config}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/*.{yaml,yml,json,config}"
  }
}
```

</details>

---


### Tool result

_source line 1662 · 2026-05-22T22:51:13.784958+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/workspace.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/pool.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_no_project.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_reviewer.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_8cc4c834a811ce97beb3d8ceb6324669.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/logs/workers/worker_research_kvtc-code-survey_20260514T042154_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_ec7b7c2246633b015619e121164ce6bf.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/secrets/distill_kv_rag_cache/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/logs/workers/worker_code_env-setup_20260514T044829_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/logs/workers/worker_research_prophetkv-code-survey_20260514T044305_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/logs/workers/worker_research_mepic-code-survey_20260514T044250_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/logs/workers/worker_research_prophetkv-survey-v2_20260514T045403_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_ra
…[truncated 11214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1663 · 2026-05-22T22:51:15.993080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1664 · 2026-05-22T22:51:16.445138+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1665 · 2026-05-22T22:51:16.446239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1666 · 2026-05-22T22:51:16.496725+00:00_

1	execution:
2	  gpu_ids:
3	  - 0
4	  project_path: /root/autodl-tmp/recursive_gen_depth_est
5	  servers:
6	  - gpu_ids:
7	    - 0
8	    server: gpu-6000pro-2
9	feishu:
10	  chat_id: oc_5d269fdb74af3f4ab8d78b82a993f5cf
11	  check_references: false
12	  operational_chat_id: oc_5434474971bcc3bc52c4774796ba7f3d
13	  review_mode: fresh
14	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
15	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_16/submitted.pdf
16	  review_round: 16
17	  review_supplementary_paths: ''
18	  submission_chat_id: oc_db3bd143165620ee6950e6ef0826eec8
19	project:
20	  created_at: '2026-05-14T09:51:34.204Z'
21	  description: How Deep Is Your Data? Estimating Recursive Generation Depth for Synthetic
22	    Text Quality Scoring
23	  name: recursive_gen_depth_est
24	  phase: research
25	  source_idea_id: idea_008
26	venue: emnlp-2026
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1667 · 2026-05-22T22:51:16.497238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1668 · 2026-05-22T22:51:16.547811+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-idea-gen-0513-2
5	  my_token: 88df7b82fe89666837a7c394be40395b99611bbf40aa913dc676879bf0a5cc0e
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1669 · 2026-05-22T22:51:18.707733+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "output_mode": "files_with_matches",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
    "output_mode": "files_with_matches",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1670 · 2026-05-22T22:51:18.959824+00:00_

Found 20 files limit: 20
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260522T181603_105908.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260519T103007_509656.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260517T115818_483164.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_6.md
/home/ubuntu/.
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1671 · 2026-05-22T22:51:20.877213+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" \\) | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" \\) | head -30"
  }
}
```

</details>

---


### Tool result

_source line 1672 · 2026-05-22T22:51:20.927866+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/compresslink_code/configs/mvp_config.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/error_type_pref_optim/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/qurating2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/li2024_mage.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/synthetic_eggs2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/loki2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/drayson2025_detection_prevents_collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/editlens2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/verma2024_ghostbuster.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/kirchenbauer2023_watermark.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/mitchell2023_detectgpt.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/penedo2024_fineweb.yaml
/hom
…[truncated 1312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1673 · 2026-05-22T22:51:22.985937+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"manifest*\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"manifest*\" \\) 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1674 · 2026-05-22T22:51:23.036685+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/qurating2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/li2024_mage.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/synthetic_eggs2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/loki2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/drayson2025_detection_prevents_collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/editlens2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/verma2024_ghostbuster.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/kirchenbauer2023_watermark.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/mitchell2023_detectgpt.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/penedo2024_fineweb.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2024_demystified.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/diveye2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/cloc2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/shi2025_closer_look.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2025_strong_collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/wu2025_detection_survey.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/alemohammad2024_mad.yaml
…[truncated 2085 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1675 · 2026-05-22T22:51:25.279398+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview|review.*enabled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "type": "yaml",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview|review.*enabled",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
    "type": "yaml",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1676 · 2026-05-22T22:51:25.330081+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1677 · 2026-05-22T22:51:27.915595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1678 · 2026-05-22T22:51:27.916049+00:00_

1	baseline: null
2	experiments:
3	  cross_model_olmo_002:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-14T18:19:10.507Z'
7	    updated_at: '2026-05-14T18:19:32.370Z'
8	    spec:
9	      command: bash scripts/run_pipeline_olmo.sh
10	      server: gpu-6000pro-2
11	      data_path: data/olmo/
12	      data_count: 20000
13	      model_name: olmo-1b-hf
14	      seed: 42
15	      checkpoint_path: checkpoints/olmo/
16	      log_path: /root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_olmo_002.log
17	    conclusion: success
18	    metrics:
19	      rf_4class_acc: 0.7877
20	      rf_4class_acc_ci:
21	      - 0.7758
22	      - 0.8003
23	      lr_4class_acc: 0.7508
24	      rf_auc_0v1: 0.9834
25	      rf_auc_0v2: 0.9949
26	      rf_auc_0v3: 0.9989
27	      rf_auc_1v2: 0.8673
28	      rf_auc_1v3: 0.9806
29	      rf_auc_2v3: 0.8124
30	      train_loss_depth0: 2.269
31	      train_loss_depth1: 1.65
32	      train_loss_depth2: 1.226
33	      top_features:
34	      - p90_ppl
35	      - var_surprisal
36	      - p75_ppl
37	      - mean_surprisal
38	      - type_token_ratio
39	    completed_at: '2026-05-14T18:19:32.370Z'
40	  cross_model_gpt2xl_001:
41	    status: DONE
42	    retry_count: 0
43	    created_at: '2026-05-14T18:28:37.468Z'
44	    updated_at: '2026-05-14T18:29:09.370Z'
45	    spec:
46	      command: scripts/run_pipeline_gpt2xl.sh + manual eval (filter_code, extract_features,
47	        train_classifier)
48	      server: gpu-6000pro-2
49	      data_path: data/gpt2xl/
50	      data_count: 20000
51	      model_name: gpt2-xl
52	      seed: 42
53	      checkpoint_source: checkpoints/gpt2xl/
54	      checkpoint_path: checkpoints/gpt2xl/
55	      log_path: results/gpt2xl/
56	    conclusion: success
57	    metrics:
58	      four_class_rf_acc: 0.8333
59	      four_class_rf_ci:
60	      - 0.8227
61	      - 0.8445
62	      four_class_lr_acc: 0.8127
63	      four_class_lr_ci:
64	      - 0.8013
65	      - 0.8257
66	      pairwise_auc_rf:
67	        d0v1: 0.994
…[truncated 9256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1679 · 2026-05-22T22:51:28.016717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1680 · 2026-05-22T22:51:28.268331+00:00_

1	approvals:
2	  apr_20260515T052615_yo5c:
3	    approval_id: apr_20260515T052615_yo5c
4	    context:
5	      file_scope: 0
6	      task_type: experiment:depth_extension_binary_pairwise_001
7	    created_at: '2026-05-15T05:26:15.131Z'
8	    feishu_card_message_id: om_x100b6f5ea953989cc450e6ed97925de
9	    project: recursive_gen_depth_est
10	    reject_reason: 审批超时（24h）
11	    resolved_at: '2026-05-16T05:26:32.125737+00:00'
12	    resolved_by: null
13	    risk_score:
14	      auto_approve: false
15	      dimensions:
16	      - label: 任务类型
17	        level: medium
18	        name: task_type
19	        value: experiment:depth_extension_binary_pairwise_001
20	      - label: 涉及文件数
21	        level: low
22	        name: file_scope
23	        value: 0
24	      overall: medium
25	      reason: 需要人工审批。维度：任务类型=experiment:depth_extension_binary_pairwise_001(medium),
26	        涉及文件数=0(low)
27	    status: expired
28	    subject_id: worker_experiment_depth_extension_binary_pairwise_001_20260515T052615
29	    type: worker
30	  apr_20260515T103851_pcew:
31	    approval_id: apr_20260515T103851_pcew
32	    context:
33	      chat_id: oc_5d269fdb74af3f4ab8d78b82a993f5cf
34	      deadline: ''
35	      has_prior_review: true
36	      mode_reason: 距上轮审稿有大量修改（z-score claim 整段重写、新增粒度消融段落、多处数字修正），fresh review 能更好评估整体论文质量。
37	      paper_path: projects/recursive_gen_depth_est/paper/main.tex
38	      paper_title: EMNLP 2026
39	      reason: Round 1 Reviewer 所有 CRITICAL/WARNING 修复完成：z-score LR claim 修正(D021)、DeepSeek
40	        40.0%、LoRA targets 三模型分列、粒度消融结果加入正文、EDD binary classifier 方法学澄清、confusion
41	        matrix caption 同步、atlas "comparably" 措辞修正。编译通过，主文 8 页。
42	      recommended_review_mode: fresh
43	      review_chat_id: oc_db3bd143165620ee6950e6ef0826eec8
44	      review_mode: fresh
45	      review_round: 0
46	      supplementary_paths: ''
47	      track: main conference
48	      venue: EMNLP 2026
49	    created_at: '2026-05-15T10:38:51.676Z'
50	    feishu_card_message_id: om_x100b6f5
…[truncated 32864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1681 · 2026-05-22T22:51:31.028689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/feishu.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/feishu.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1682 · 2026-05-22T22:51:31.079318+00:00_

1	app_id: cli_a97eefefcbf8dcce
2	app_secret: 3rvr5B0mVHeobED6BwU5YbtHkGQFFicz
3	bot_name: Auto Research Prod13
4	chats: {}
5	policy:
6	  require_mention: true
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1683 · 2026-05-22T22:51:32.986573+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1684 · 2026-05-22T22:51:33.038140+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1685 · 2026-05-22T22:51:35.145961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/registry.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/registry.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1686 · 2026-05-22T22:51:35.146412+00:00_

1	baseline: null
2	experiments:
3	  mvp_pipeline_001:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-14T10:14:38.727Z'
7	    updated_at: '2026-05-14T12:07:10.095Z'
8	    spec:
9	      command: N/A (orphan cleanup)
10	      server: gpu-6000pro-2
11	      gpu:
12	      - cuda:0
13	      pid: '87744'
14	      log_path: N/A
15	      submitted_at: '2026-05-14T10:14:38.726Z'
16	      submitted_via: submit_training_job
17	      backend: tmux
18	      account: root
19	      data_path: N/A
20	      data_count: 0
21	      model_name: N/A
22	      seed: 0
23	      checkpoint_path: N/A
24	      wall_clock_seconds: 6751.4
25	      gpu_hours: 1.88
26	    conclusion: killed
27	    completed_at: '2026-05-14T12:07:10.095Z'
28	  mvp_pipeline_002:
29	    status: DONE
30	    retry_count: 0
31	    created_at: '2026-05-14T10:21:10.897Z'
32	    updated_at: '2026-05-14T12:07:10.599Z'
33	    spec:
34	      command: N/A (orphan cleanup)
35	      server: gpu-6000pro-2
36	      gpu:
37	      - cuda:0
38	      pid: '89048'
39	      log_path: N/A
40	      submitted_at: '2026-05-14T10:21:10.894Z'
41	      submitted_via: submit_training_job
42	      backend: tmux
43	      account: root
44	      data_path: N/A
45	      data_count: 0
46	      model_name: N/A
47	      seed: 0
48	      checkpoint_path: N/A
49	      wall_clock_seconds: 6359.7
50	      gpu_hours: 1.77

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1687 · 2026-05-22T22:51:37.053568+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -type f -name \"*.yaml\" -o -name \"*.yml\" | xargs grep -l \"external\\|review\\|paperreview\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -type f -name \"*.yaml\" -o -name \"*.yml\" | xargs grep -l \"external\\|review\\|paperreview\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1688 · 2026-05-22T22:51:37.104336+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/li2024_mage.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/penedo2024_fineweb.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/shi2025_closer_look.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/yi2026_escaping_collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1689 · 2026-05-22T22:51:39.364094+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/ | grep -E \"\\.yaml|\\.yml|\\.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/ | grep -E \"\\.yaml|\\.yml|\\.json\""
  }
}
```

</details>

---


### Tool result

_source line 1690 · 2026-05-22T22:51:39.414820+00:00_

-rw-rw-r-- 1 ubuntu ubuntu  2901 May  9 09:00 approvals.yaml
-rw------- 1 ubuntu ubuntu   769 May 13 11:23 backend.yaml
-rw-r--r-- 1 ubuntu ubuntu  4233 May 22 22:49 claude_sessions.json
-rw------- 1 ubuntu ubuntu 21158 May 22 22:48 crons.yaml
-rw------- 1 ubuntu ubuntu   463 May 15 04:13 email_tokens.json
-rw------- 1 ubuntu ubuntu   147 May 13 11:23 feishu.yaml
-rw-r--r-- 1 ubuntu ubuntu  4174 May 22 22:17 keepalive.json
-rw-r--r-- 1 ubuntu ubuntu   341 May 13 11:23 mcp_config.json
-rw-r--r-- 1 ubuntu ubuntu   391 May 17 10:55 mcp_config_briefer.json
-rw-r--r-- 1 ubuntu ubuntu   393 May 14 04:18 mcp_config_director.json
-rw-r--r-- 1 ubuntu ubuntu   395 May 20 14:06 mcp_config_distiller.json
-rw-r--r-- 1 ubuntu ubuntu   419 May 14 14:39 mcp_config_dream_review_director.json
-rw-r--r-- 1 ubuntu ubuntu   397 May 14 03:43 mcp_config_no_project.json
-rw-r--r-- 1 ubuntu ubuntu   399 May 15 06:28 mcp_config_paper_agent.json
-rw-r--r-- 1 ubuntu ubuntu   415 May 21 06:37 mcp_config_paper_audit_content.json
-rw-r--r-- 1 ubuntu ubuntu   427 May 20 06:26 mcp_config_paper_audit_review_visual.json
-rw-r--r-- 1 ubuntu ubuntu   413 May 21 06:37 mcp_config_paper_audit_visual.json
-rw-r--r-- 1 ubuntu ubuntu   407 May 15 10:39 mcp_config_review_director.json
-rw-r--r-- 1 ubuntu ubuntu   435 May 15 10:41 mcp_config_review_reviewer_1.json
-rw-r--r-- 1 ubuntu ubuntu   435 May 15 10:42 mcp_config_review_reviewer_2.json
-rw-r--r-- 1 ubuntu ubuntu   393 May 14 04:20 mcp_config_reviewer.json
-rw-r--r-- 1 ubuntu ubuntu   528 May 15 05:57 mcp_config_worker_074936fc4b5d802648d5b9b7fe3a8a01.json
-rw-r--r-- 1 ubuntu ubuntu   523 May 16 05:20 mcp_config_worker_088d5a12df17e204770bc16289635e95.json
-rw-r--r-- 1 ubuntu ubuntu   474 May 17 18:54 mcp_config_worker_09731295942d3269e0517509703bed15.json
-rw-r--r-- 1 ubuntu ubuntu   416 May 14 04:48 mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
-rw-r--r-- 1 ubuntu ubuntu   464 May 14 06:12 mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.js
…[truncated 4514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1691 · 2026-05-22T22:51:41.422636+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/resources.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/resources.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1692 · 2026-05-22T22:51:41.422996+00:00_

1	default_model: claude-opus-4-6
2	default_model_claude_code: claude-opus-4-6
3	idea_model: claude-opus-4-6
4	servers:
5	  autodl-rtx6000:
6	    accounts:
7	    - env_activate: ''
8	      user: root
9	      work_dir: /root/autodl-tmp
10	    detected_image:
11	      detected: false
12	      image: ''
13	      status: unknown
14	      version: ''
15	    gpus:
16	    - available: true
17	      id: cuda:0
18	      vram_gb: 96
19	    - available: true
20	      id: cuda:1
21	      vram_gb: 96
22	    hardware:
23	      cpu_cores: 0
24	      disk_avail_gb: 0
25	      disk_total_gb: 0
26	      probed_at: '2026-05-14T04:46:04.830Z'
27	      ram_total_gb: 0
28	    host: connect.westb.seetacloud.com
29	    port: 52439
30	  gpu-6000pro-2:
31	    accounts:
32	    - gpus:
33	      - cuda:0
34	      - cuda:1
35	      name: root
36	      password_encrypted: gAAAAABqBVQbiKx2CK5mMeICcVLdRYgmN9nf3KjerSShVvGHZ0bMQCZ9gjOaXRp91w8tAKzniu9NCBJTpjfi2mR8Hl0jdGqtCg==
37	      user: root
38	      work_dir: /root
39	    detected_image:
40	      detected: false
41	      image: ''
42	      status: unknown
43	      version: ''
44	    env_activate: ''
45	    host: connect.westb.seetacloud.com
46	    port: 52439
47	    total_gpus:
48	    - cuda:0
49	    - cuda:1
50	    user_rules_excluded: []
51	    work_dir: /root
52	user_rules: []
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1693 · 2026-05-22T22:51:44.183191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/crons.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/crons.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1694 · 2026-05-22T22:51:44.183544+00:00_

1	active_crons:
2	- chat_id: null
3	  created_at: '2026-05-22T18:38:56.847Z'
4	  exp_id: qwen25_7b_selfref_001
5	  hooks: null
6	  interval_seconds: 300
7	  last_checked: '2026-05-22T22:48:19.954Z'
8	  log_path: ~/runs/recursive_gen_depth_est/qwen25_7b_selfref_001.log
9	  pid: '825140'
10	  project: recursive_gen_depth_est
11	  server: gpu-6000pro-2
12	  tracked_metrics: null
13	  wandb_run_id: null
14	completed_crons:
15	- chat_id: null
16	  completed_at: '2026-05-14T17:02:03Z'
17	  created_at: '2026-05-14T16:53:44.952Z'
18	  exp_id: cross_model_olmo_002
19	  hooks: null
20	  interval_seconds: 120
21	  last_checked: '2026-05-14T16:59:59.244Z'
22	  log_path: /root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_olmo_002.log
23	  pid: '150550'
24	  project: recursive_gen_depth_est
25	  server: westb-52439
26	  status: completed
27	  tracked_metrics: null
28	  wandb_run_id: null
29	- chat_id: null
30	  completed_at: '2026-05-14T18:19:23Z'
31	  created_at: '2026-05-14T14:44:22.674Z'
32	  exp_id: cross_model_gpt2xl_001
33	  hooks: null
34	  interval_seconds: 120
35	  last_checked: '2026-05-14T18:17:19.427Z'
36	  log_path: /root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_gpt2xl.log
37	  pid: '123650'
38	  project: recursive_gen_depth_est
39	  server: gpu-6000pro-2
40	  status: completed
41	  tracked_metrics: null
42	  wandb_run_id: null
43	- chat_id: null
44	  completed_at: '2026-05-14T18:19:28Z'
45	  created_at: '2026-05-14T17:08:20.210Z'
46	  exp_id: cross_model_olmo_002
47	  hooks: null
48	  interval_seconds: 120
49	  last_checked: '2026-05-14T18:17:21.836Z'
50	  log_path: /root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_olmo_002.log
51	  pid: '150550'
52	  project: recursive_gen_depth_est
53	  server: gpu-6000pro-2
54	  status: completed
55	  tracked_metrics: null
56	  wandb_run_id: null
57	- chat_id: null
58	  completed_at: '2026-05-14T20:15:03Z'
59	  created_at: '2026-05-14T20:14:31.874Z'
60	  exp_id: pythia_topk50_001
61	  hooks: null
62	  interval_se
…[truncated 1264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1695 · 2026-05-22T22:51:46.443257+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -maxdepth 2 -type f \\( -name \"settings*\" -o -name \"config*\" -o -name \"main*\" \\) 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -maxdepth 2 -type f \\( -name \"settings*\" -o -name \"config*\" -o -name \"main*\" \\) 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1696 · 2026-05-22T22:51:46.443709+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1697 · 2026-05-22T22:51:48.502252+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool result

_source line 1698 · 2026-05-22T22:51:48.553110+00:00_

&lt;persisted-output>
Output too large (93KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-director-79bccd15/8fe70560-f017-4028-acea-e055da425e86/tool-results/b7wloi2ut.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260519T103007_509656.jsonl:{"ts": "2026-05-19T03:13:24.123844+00:00", "role": "user", "session": "feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director", "text": "[审稿报告]\nOverall: 3.0 (Findings)\n\n# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 写作质量)\n**审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了一个 180K 样本基准（3 模型族 × 3 解码策略 × 4 深度），用 Random Forest 在 19 个统计特征上实现 69-86% 四分类准确率（chance=25%）。论文定义了 Effective Discriminable Depth (EDD) 度量，构建了 Depth Degradation Atlas，并在 8 个泛化维度上进行系统评估。这是一项问题定义新颖、实验执行严谨、报告透明诚实的实证研究，但在生态效度、跨策略部署和规模可扩展性方面存在结构性限制。\n\n---\n\n## Strengths\n\n**S1. 任务定义的原创性 [R1, R2 一致]。** 递归生成深度估计是一个真正未被研究过的问题，填补了 model collapse 理论（假设深度已知）和二分类检测（忽略深度信息）之间的空白。EDD 度量的形式化（Definition 1, Eq. 1）数学自洽且有概念价值。\n\n**S2. 系统性实验设计 [R1, R2 一致]。** 3×3 model-strategy grid × 4 depths = 180K 样本，加上 8 个泛化轴（cross-model, cross-strategy, cross-scale, cross-domain, cross-model chains, prompted generation, seed replication, depth extension），构成了非常全面的实验矩阵。基线覆盖四类方法且对比公平。\n\n**S3. 统计实践透明 [R1 主导, R2 认同]。** Bootstrap 95% CI 贯穿主要结果；domain bias 分析的三子实验设计严谨；初始 bug 透明报告并修复；RF seed robustness 验证（std=0.06pp）。\n\n**S4. 诚实的局限性讨论 [R1, R2 一致]。** d0 膨胀、cross-strategy 失败、14B EDD=0、5 个 cross-scale 混杂因素、单 LoRA 种子不确定性、curation PoC 非显著——均被如实报告。Limitations 覆盖 12+ 个具体限制。\n\n**S5. 理论-实证对应 [R1 主导]。** tail erosion 理论预测与 9/9 cell
…[truncated 339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1699 · 2026-05-22T22:51:51.371238+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml 2>/dev/null | head -50"
  }
}
```

</details>

---


### Tool result

_source line 1700 · 2026-05-22T22:51:51.421899+00:00_

execution:
  gpu_ids:
  - 0
  project_path: /root/autodl-tmp/recursive_gen_depth_est
  servers:
  - gpu_ids:
    - 0
    server: gpu-6000pro-2
feishu:
  chat_id: oc_5d269fdb74af3f4ab8d78b82a993f5cf
  check_references: false
  operational_chat_id: oc_5434474971bcc3bc52c4774796ba7f3d
  review_mode: fresh
  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_16/submitted.pdf
  review_round: 16
  review_supplementary_paths: ''
  submission_chat_id: oc_db3bd143165620ee6950e6ef0826eec8
project:
  created_at: '2026-05-14T09:51:34.204Z'
  description: How Deep Is Your Data? Estimating Recursive Generation Depth for Synthetic
    Text Quality Scoring
  name: recursive_gen_depth_est
  phase: research
  source_idea_id: idea_008
venue: emnlp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1701 · 2026-05-22T22:51:53.479844+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -type f -name \"*.json\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -type f -name \"*.json\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1702 · 2026-05-22T22:51:53.580708+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1703 · 2026-05-22T22:51:56.140489+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview_ai\\|enabled.*true\\|enabled.*false\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview_ai\\|enabled.*true\\|enabled.*false\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1704 · 2026-05-22T22:51:56.241367+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-15 10:39:08 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-15 16:03:49 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 12:01:54 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 17:13:34 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 19:27:28 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 20:03:20 INFO     [EXTERN] [external_review] reset state for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 20:03:21 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-17 06:17:59 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-18 14:07:05 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-19 02:55:38 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-19 06:32:00 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth
…[truncated 1102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1705 · 2026-05-22T22:51:58.203193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1706 · 2026-05-22T22:51:58.203818+00:00_

1	2026-05-13 11:23:04 INFO     [SESSION] [session_server] wrote /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config.json
2	2026-05-13 11:23:04 INFO     [SESSION] [session_server] started (loop=129902514533920)
3	2026-05-13 11:23:04 INFO     [__MAIN] [startup] watchdog started pid=2785 (bash=/usr/bin/bash)
4	2026-05-13 11:23:04 INFO     [FEISHU] Feishu WebSocket started in background thread
5	2026-05-13 11:23:04 INFO     [GPU_MO] GPU monitor daemon starting (interval=60s)
6	2026-05-13 11:23:04 INFO     [CRON] Polling loop started (default interval 120s)
7	2026-05-13 11:23:04 INFO     [DIRECT] [keepalive] Loaded 0 project states
8	2026-05-13 11:23:08 INFO     [POOL_S] pool_state_watcher scheduled
9	2026-05-13 11:23:08 INFO     [POOL_S] pool_state_watcher: no manager target in backend.yaml; watcher will not emit events
10	2026-05-13 11:23:13 INFO     [HTTP] HTTP Request: GET https://autoresearch.claude-code-manager.com/api/health "HTTP/1.1 502 Bad Gateway"
11	2026-05-13 11:23:13 WARNING  [__MAIN] Public URL check failed: https://autoresearch.claude-code-manager.com 返回 502
12	2026-05-13 11:23:18 INFO     [FEISHU] [WS-PATCH] Monkey-patched WSClient._handle_message for CARD frame support
13	2026-05-13 11:23:19 INFO     [LARK] connected to wss://msg-frontier.feishu.cn/ws/v2?fpid=493&aid=552564&device_id=7639335430039948482&access_key=[REDACTED] [conn_id=7639335430039948482]
14	2026-05-13 11:23:19 INFO     [SESSION] [session_server] cron_poller started
15	2026-05-13 11:23:27 INFO     [CRON] Polling loop cancelled
16	2026-05-13 11:23:34 INFO     [SESSION] [session_server] started (loop=130404213405552)
17	2026-05-13 11:23:34 INFO     [__MAIN] [startup] watchdog started pid=3394 (bash=/usr/bin/bash)
18	2026-05-13 11:23:34 INFO     [FEISHU] Feishu WebSocket started in background thread
19	2026-05-13 11:23:34 INFO     [GPU_MO] GPU monitor daemon starting (interval=60s)
20	2026-05
…[truncated 20123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1707 · 2026-05-22T22:52:08.138281+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"external_review_enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | head -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"external_review_enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | head -3"
  }
}
```

</details>

---


### Tool result

_source line 1708 · 2026-05-22T22:52:08.188929+00:00_

6947:2026-05-15 10:39:08 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
8320:2026-05-15 16:03:49 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
12618:2026-05-16 12:01:54 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1709 · 2026-05-22T22:52:10.146255+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"external_review_enabled\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | grep -E \"True|enabled.*true\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"external_review_enabled\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | grep -E \"True|enabled.*true\" | head -5"
  }
}
```

</details>

---


### Tool result

_source line 1710 · 2026-05-22T22:52:10.196871+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1711 · 2026-05-22T22:52:11.955091+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1712 · 2026-05-22T22:52:12.256640+00:00_

&lt;persisted-output>
Output too large (151.3KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-director-79bccd15/8fe70560-f017-4028-acea-e055da425e86/tool-results/bxqihwumn.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/archive/feishu_group_oc_5d269fdb74af3f4ab8d78b82a993f5cf_director_20260519T103007_509656.jsonl:{"ts": "2026-05-19T03:13:24.123844+00:00", "role": "user", "session": "feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director", "text": "[审稿报告]\nOverall: 3.0 (Findings)\n\n# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 写作质量)\n**审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了一个 180K 样本基准（3 模型族 × 3 解码策略 × 4 深度），用 Random Forest 在 19 个统计特征上实现 69-86% 四分类准确率（chance=25%）。论文定义了 Effective Discriminable Depth (EDD) 度量，构建了 Depth Degradation Atlas，并在 8 个泛化维度上进行系统评估。这是一项问题定义新颖、实验执行严谨、报告透明诚实的实证研究，但在生态效度、跨策略部署和规模可扩展性方面存在结构性限制。\n\n---\n\n## Strengths\n\n**S1. 任务定义的原创性 [R1, R2 一致]。** 递归生成深度估计是一个真正未被研究过的问题，填补了 model collapse 理论（假设深度已知）和二分类检测（忽略深度信息）之间的空白。EDD 度量的形式化（Definition 1, Eq. 1）数学自洽且有概念价值。\n\n**S2. 系统性实验设计 [R1, R2 一致]。** 3×3 model-strategy grid × 4 depths = 180K 样本，加上 8 个泛化轴（cross-model, cross-strategy, cross-scale, cross-domain, cross-model chains, prompted generation, seed replication, depth extension），构成了非常全面的实验矩阵。基线覆盖四类方法且对比公平。\n\n**S3. 统计实践透明 [R1 主导, R2 认同]。** Bootstrap 95% CI 贯穿主要结果；domain bias 分析的三子实验设计严谨；初始 bug 透明报告并修复；RF seed robustness 验证（std=0.06pp）。\n\n**S4. 诚实的局限性讨论 [R1, R2 一致]。** d0 膨胀、cross-strategy 失败、14B EDD=0、5 个 cross-scale 混杂因素、单 LoRA 种子不确定性、curation PoC 非显著——均被如实报告。Limitations 覆盖 12+ 个具体限制。\n\n**S5. 理论-实证对应 [R1 主导]。** tail erosion 理论预测与 9/9 c
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1713 · 2026-05-22T22:52:15.116585+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"external_review_enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | wc -l && grep \"external_review_enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | sort | uniq -c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"external_review_enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | wc -l && grep \"external_review_enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | sort | uniq -c"
  }
}
```

</details>

---


### Tool result

_source line 1714 · 2026-05-22T22:52:15.167472+00:00_

16
      1 2026-05-15 10:39:08 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-15 16:03:49 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-16 12:01:54 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-16 17:13:34 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-16 19:27:28 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-16 20:03:21 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-17 06:17:59 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-18 14:07:05 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-19 02:55:38 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-19 06:32:00 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-20 06:23:02 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-20 08:30:31 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-20 13:59:11 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-21 06:27:36 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-21 21:29:05 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
      1 2026-05-22 22:49:32 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1715 · 2026-05-22T22:52:17.125036+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"external_review.*status|get_external_review_status\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"external_review.*status|get_external_review_status\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1716 · 2026-05-22T22:52:17.175670+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1717 · 2026-05-22T22:52:24.410799+00:00_

Based on my comprehensive search of the project configuration files and system logs, here is my findings report:

## Configuration Report: External Review Settings for "recursive_gen_depth_est" Project

### Value of external_review.paperreview_ai.enabled
**Status: FALSE (Disabled)**

The external review feature is currently **disabled** for the recursive_gen_depth_est project.

### Evidence
System log entries at `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log` consistently show:
```
external_review_enabled=False for project=recursive_gen_depth_est
```

This log entry appears 16 times across the review process (from 2026-05-15 through 2026-05-22), with every single entry showing `False`.

### Location of Configuration
The setting is enforced through the review hooks system rather than a static configuration file. The check is logged in the `[HOOKS] [review]` subsystem whenever review submissions are processed.

### Project Configuration Files Examined
1. `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml` - No external_review settings found
2. `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/workspace.yaml` - Empty projects section
3. `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/backend.yaml` - Manager and API configuration only
4. `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/feishu.yaml` - Feishu integration config only
5. `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml` - Approval records (no external review settings)

### Other External Review Settings
The system log also shows:
- **External review reset event** on 2026-05-16: `[EXTERN] [external_review] reset state for project=recursive_gen_depth_est`

This indicates the external review system tracked state for this project but the enabled flag remained False throughout all review rounds.

### Conclusion
The `external_review.paperreview_ai.enabled` setting is **set to False**, meaning Stanford Agentic R
…[truncated 196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Agent",
  "elapsed_ms": 72636
}
```

</details>

---


### Tool call

_source line 1718 · 2026-05-22T22:52:30.123369+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1719 · 2026-05-22T22:52:30.173949+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1720 · 2026-05-22T22:52:40.721579+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'pending', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer 任务', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见并收集回应', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'pending', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer 任务', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见并收集回应', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1721 · 2026-05-22T22:52:40.772231+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1722 · 2026-05-22T22:53:16.977971+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查 + Step 1: 分配 Reviewer 任务', 'status': 'in_progress', 'activeForm': '派发视觉审查并分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见并收集回应', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查 + Step 1: 分配 Reviewer 任务', 'status': 'in_progress', 'activeForm': '派发视觉审查并分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见并收集回应', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1723 · 2026-05-22T22:53:16.978382+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1724 · 2026-05-22T22:53:18.835531+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1725 · 2026-05-22T22:53:40.107729+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21272
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-22T22:53:40.108159+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## 论文信息\n- 标题: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n- 路径: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`（多文件结构，各章节为独立 .tex 文件在同目录下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_16/submitted.pdf`\n- 目标 venue: **EMNLP 2026**（ARR May cycle，截止 2026-05-25）\n\n## Venue 要求\n- Long paper: **正文 ≤8 页**，参考文献不限，Limitations 必须有（不计入页数），Ethics 可选（不计入页数）\n- ACL 模板，**double-blind** 匿名审稿\n- 附录在正文后，不计入页数，reviewer 不要求阅读附录\n- Overall Assessment 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请以顶会最严格的标准审查以下维度：\n\n1. **实验设计与统计严谨性**\n   - Benchmark 构建是否合理？控制变量是否充分？\n   - 统计检验是否恰当？多重比较是否校正？CI 是否报告？\n   - EDD 定义和 T=0.70 阈值选择是否合理？\n   - 5-fold CV 是否有 data leakage 风险？\n\n2. **Feature 设计与分析**\n   - 19 个特征的选择是否有依据？\n   - VIF>10 的严重共线性如何影响特征重要性排名？\n   - Group-level ablation 是否充分？\n\n3. **Baselines 与对比**\n   - Neural baselines 是否公平？（backbone 规模、训练策略）\n   - Binary detector baselines 的适配是否合理？\n   - Binoculars 达到统计等价（78.1% vs 78.4%, p>0.05）如何评价？\n\n4. **泛化性实验**\n   - Cross-model、cross-strategy、cross-scale 实验设计是否充分？\n   - Full-replacement vs accumulation 的差距是否充分讨论？\n   - 14B self-reference confound 是否得到充分控制？\n   - Reference model 依赖性是否系统分析？\n\n5. **可复现性**\n   - 超参数、训练细节、数据规模是否充分报告？\n   - Single LoRA seed 的影响？\n\n请输出完整审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注严重程度 [Critical/Warning/Minor]）、Questions（需作者回答）、Missing References、Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## 论文信息\n- 标题: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n- 路径: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`（多文件结构，各章节为独立 .tex 文件在同目录下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_16/submitted.pdf`\n- 目标 venue: **EMNLP 2026**（ARR May cycle，截止 2026-05-25）\n\n## Venue 要求\n- Long paper: **正文 ≤8 页**，参考文献不限，Limitations 必须有（不计入页数），Ethics 可选（不计入页数）\n- ACL 模板，**double-blind** 匿名审稿\n- 附录在正文后，不计入页数，reviewer 不要求阅读附录\n- Overall Assessment 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请以顶会最严格的标准审查以下维度：\n\n1. **实验设计与统计严谨性**\n   - Benchmark 构建是否合理？控制变量是否充分？\n   - 统计检验是否恰当？多重比较是否校正？CI 是否报告？\n   - EDD 定义和 T=0.70 阈值选择是否合理？\n   - 5-fold CV 是否有 data leakage 风险？\n\n2. **Feature 设计与分析**\n   - 19 个特征的选择是否有依据？\n   - VIF>10 的严重共线性如何影响特征重要性排名？\n   - Group-level ablation 是否充分？\n\n3. **Baselines 与对比**\n   - Neural baselines 是否公平？（backbone 规模、训练策略）\n   - Binary detector baselines 的适配是否合理？\n   - Binoculars 达到统计等价（78.1% vs 78.4%, p>0.05）如何评价？\n\n4. **泛化性实验**\n   - Cross-model、cross-strategy、cross-scale 实验设计是否充分？\n   - Full-replacement vs accumulation 的差距是否充分讨论？\n   - 14B self-reference confound 是否得到充分控制？\n   - Reference model 依赖性是否系统分析？\n\n5. **可复现性**\n   - 超参数、训练细节、数据规模是否充分报告？\n   - Single LoRA seed 的影响？\n\n请输出完整审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注严重程度 [Critical/Warning/Minor]）、Questions（需作者回答）、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1727 · 2026-05-22T22:53:54.672421+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14564
}
```

</details>

---


### Tool call

_source line 1728 · 2026-05-22T22:53:54.923870+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性、完整性和写作质量**。\n\n## 论文信息\n- 标题: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n- 路径: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`（多文件结构，各章节为独立 .tex 文件在同目录下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_16/submitted.pdf`\n- 目标 venue: **EMNLP 2026**（ARR May cycle，截止 2026-05-25）\n\n## Venue 要求\n- Long paper: **正文 ≤8 页**，参考文献不限，Limitations 必须有（不计入页数），Ethics 可选（不计入页数）\n- ACL 模板，**double-blind** 匿名审稿\n- 附录在正文后，不计入页数，reviewer 不要求阅读附录\n- Overall Assessment 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请以顶会最严格的标准审查以下维度：\n\n1. **新颖性与贡献度**\n   - 任务定义（recursive generation depth estimation）是否是真正的新问题？\n   - EDD metric 是否有独立价值？\n   - 方法层面（19 个统计特征 + RF）是否有方法论创新？\n   - 与 model collapse 文献、AI text detection 文献的区分是否清晰？\n   - 贡献是否达到 EMNLP Conference/Findings 标准？\n\n2. **Related Work 完整性**\n   - 覆盖是否全面？是否有重要遗漏？\n   - 与 adjacent tasks 的定位是否准确？\n   - 是否有 2025-2026 年重要新工作被遗漏？\n\n3. **Framing 与叙事合理性**\n   - Introduction 的动机是否成立？\n   - Claim scope 是否与证据匹配？（注意 cross-strategy 45.9%、14B EDD=0 对通用性主张的影响）\n   - \"depth estimation\" vs \"ordinal classification\" 术语是否一致？\n   - Abstract 是否准确反映论文内容和局限？\n\n4. **写作质量**\n   - 逻辑流是否清晰？章节衔接是否自然？\n   - 表格/图表是否有效传达信息？\n   - 是否存在 AI 写作痕迹或套话？\n   - Discussion 是否充分？\n\n5. **格式合规**\n   - 正文是否在 8 页限制内？\n   - 匿名是否合规？（无作者信息泄露）\n   - Limitations 是否存在且充分？\n   - Ethics Statement 是否存在？\n   - 引用格式是否符合 ACL 标准？\n\n请输出完整审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注严重程度 [Critical/Warning/Minor]）、Questions（需作者回答）、Missing References、Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查**新颖性、完整性和写作质量**。\n\n## 论文信息\n- 标题: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n- 路径: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`（多文件结构，各章节为独立 .tex 文件在同目录下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_16/submitted.pdf`\n- 目标 venue: **EMNLP 2026**（ARR May cycle，截止 2026-05-25）\n\n## Venue 要求\n- Long paper: **正文 ≤8 页**，参考文献不限，Limitations 必须有（不计入页数），Ethics 可选（不计入页数）\n- ACL 模板，**double-blind** 匿名审稿\n- 附录在正文后，不计入页数，reviewer 不要求阅读附录\n- Overall Assessment 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请以顶会最严格的标准审查以下维度：\n\n1. **新颖性与贡献度**\n   - 任务定义（recursive generation depth estimation）是否是真正的新问题？\n   - EDD metric 是否有独立价值？\n   - 方法层面（19 个统计特征 + RF）是否有方法论创新？\n   - 与 model collapse 文献、AI text detection 文献的区分是否清晰？\n   - 贡献是否达到 EMNLP Conference/Findings 标准？\n\n2. **Related Work 完整性**\n   - 覆盖是否全面？是否有重要遗漏？\n   - 与 adjacent tasks 的定位是否准确？\n   - 是否有 2025-2026 年重要新工作被遗漏？\n\n3. **Framing 与叙事合理性**\n   - Introduction 的动机是否成立？\n   - Claim scope 是否与证据匹配？（注意 cross-strategy 45.9%、14B EDD=0 对通用性主张的影响）\n   - \"depth estimation\" vs \"ordinal classification\" 术语是否一致？\n   - Abstract 是否准确反映论文内容和局限？\n\n4. **写作质量**\n   - 逻辑流是否清晰？章节衔接是否自然？\n   - 表格/图表是否有效传达信息？\n   - 是否存在 AI 写作痕迹或套话？\n   - Discussion 是否充分？\n\n5. **格式合规**\n   - 正文是否在 8 页限制内？\n   - 匿名是否合规？（无作者信息泄露）\n   - Limitations 是否存在且充分？\n   - Ethics Statement 是否存在？\n   - 引用格式是否符合 ACL 标准？\n\n请输出完整审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注严重程度 [Critical/Warning/Minor]）、Questions（需作者回答）、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1729 · 2026-05-22T22:53:56.453209+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1529
}
```

</details>

---


### Assistant

_source line 1730 · 2026-05-22T22:54:00.894821+00:00_

已完成：
- 视觉审查 Agent 已派发（fire-and-forget，不等待）
- Reviewer 1（方法严谨性 + 实验设计）已触发
- Reviewer 2（新颖性 + 完整性 + 写作）已触发

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 149

## Round 149

4 recorded events


### User

_source line 1731 · 2026-05-22T23:00:37.667109+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性和实验设计）

### 总体评分
**Overall**: 3.5 (Borderline Conference)
**Confidence**: 4/5
**一句话总结**: 问题新颖、实验覆盖面广，但 reference model 依赖、full-replacement 与真实场景的 gap、以及多重比较未校正等方法论问题限制了其可信度和实用性。

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心 claims 有实验支撑但存在混淆变量（reference model confound）、多重比较未校正、生态效度不足 |
| Excitement | 3.5/5 | 递归生成深度估计作为序数分类是全新问题定义，Depth Degradation Atlas 有实用价值，但受限于 reference model 硬依赖 |
| Reproducibility | 4/5 | 超参数、数据规模、硬件环境报告充分，单 seed 有 replication（B.21）但主实验仍为单 seed |

### Must-Fix 问题（3个 Critical）

**N1 [Critical] Reference model 依赖是 pipeline 根本瓶颈，main text 讨论不足**
- Table 18: cross-architecture reference (GPT-2 XL) 准确率从 78.6% 降至 67.3%（-11.3pp）
- 19 个特征中 12 个依赖 Pythia-1.4B log-probabilities
- Main text 仅笼统提 "~7pp"，未充分讨论 generator-unknown 部署场景
- 建议：增加 reference-agnostic baseline 或 multi-reference ensemble 实验

**N2 [Critical] 多重比较未校正，但基于 p-values 做了实质性判断**
- Footnote 1 声明 uncorrected，但 Section 5.1 称 Binoculars "statistical equivalence"（p>0.05）
- 非显著性 ≠ 等价性，需 TOST equivalence test
- 以 "Statistical Fingerprints" 为卖点的论文，统计推断本身缺乏严谨性

**N3 [Critical] Full-replacement benchmark 与真实 accumulation 场景有根本性 gap**
- Primary benchmark 为 full-replacement chain，真实场景为 accumulation + unknown mixing ratios
- Appendix B.8 仅覆盖 6 个组合，GPT-2 XL 50% mixing 出现 boundary failure（AUC=0.695）
- Title "How Deep Is Your Data?" 暗示通用性，但受限于 full-replacement 假设

### Should-Fix 问题（6个 Warning）
- W1: Neural baselines 比较不公平——RF 有 reference model oracle，DeBERTa/RoBERTa 只看原文
- W2: EDD 阈值 T=0.70 从 binary ROC 标准迁移到 ordinal pairwise AUC 缺乏理论论证
- W3: Cross-model transfer 平均仅 64.8%，Pythia holdout 55.4%，泛化声明需更审慎
- W4: 14B self-reference confound 无法干净分离 scale effect 和 reference-model confound
- W5: BOS seeding vs prompted generation 差 13.8pp，主 benchmark 的 depth signal 可能部分是 artifact
- W6: 单 LoRA seed 主实验，仅 2-seed replication 不足以估计方差分布

### Questions（6个）
- Q1: Table 18 显示 -11.3pp，main text 说 "~7pp"，请澄清差异来源
- Q2: Generator-unknown 场景下的 reference model 选择策略？
- Q3: T=0.70 边界处 d2 的 per-class recall 是否低于 chance？
- Q4: 10% mixing ratio 下 pipeline 是否仍能工作？
- Q5: BOS vs prompted 的 13.8pp gap 是否意味着主 benchmark 有 artifact？
- Q6: QWK=0.89 对应什么 ordinal misclassification pattern？

### Missing References
- Lakens (2017) equivalence testing 方法论
- Gutiérrez et al. (2016) ordinal regression 综述
- Alemohammad et al. (2024) autophagous loops 理论分析

### 升分条件
如果 rebuttal 能提供 (a) reference-agnostic baseline/ensemble, (b) Bonferroni-corrected key claims, (c) 更全面的 accumulation 实验，愿意提高至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-22T23:00:57.863055+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 1', 'status': 'completed', 'activeForm': 'Reviewer 1 完成审稿'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 2', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 审稿返回'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见并收集回应', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 1', 'status': 'completed', 'activeForm': 'Reviewer 1 完成审稿'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 2', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 审稿返回'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见并收集回应', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-22T23:00:57.863623+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1734 · 2026-05-22T23:01:07.408398+00:00_

**Reviewer 1 审稿意见已接收**（3.5 Borderline Conference，置信度 4/5）。

关键发现摘要：
- 3 个 Critical：reference model 硬依赖、多重比较未校正、full-replacement vs accumulation gap
- 6 个 Warning：neural baseline 信息不对等、EDD 阈值迁移、cross-model 泛化弱、14B confound、BOS artifact、单 seed
- 评分条件：rebuttal 若补 reference-agnostic baseline + Bonferroni 校正 + accumulation 实验，可升至 4.0

等待 Reviewer 2 审稿返回后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 150

## Round 150

2 recorded events


### User

_source line 1735 · 2026-05-22T23:01:09.924935+00:00_

[Reviewer 1 审稿结果]:
审稿意见已完成并提交给 Review Director。

核心判断：**3.5 (Borderline Conference)**。论文提出了一个genuinely novel的问题（递归生成深度的序数估计），benchmark构建和ablation覆盖面都很强，但三个critical issue拉低了评分：

1. **Reference model依赖**——cross-architecture降幅达11.3pp，main text讨论不足
2. **统计推断缺陷**——以"Statistical Fingerprints"为卖点却多重比较未校正，且将非显著性误读为等价性
3. **生态效度gap**——full-replacement benchmark与真实accumulation场景差距大，accumulation实验覆盖不足

如果rebuttal能补上reference-agnostic实验、corrected统计检验和更全面的accumulation结果，可升至4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1736 · 2026-05-22T23:01:15.655754+00:00_

已收到 Reviewer 1 的完整意见，等待 Reviewer 2 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 151

## Round 151

8 recorded events


### User

_source line 1737 · 2026-05-22T23:01:18.154306+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Round 1（新颖性、完整性、写作质量）

**论文**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**Venue**: EMNLP 2026 (ARR May cycle)

---

## Paper Summary

本文定义了"递归生成深度估计"任务——给定一段文本，判断它经历了多少轮 model→data→model 循环（深度 d=0 为人类原文，d=1,2,... 为逐代 LLM 生成）。作者将其形式化为序数分类问题，构建了 180K 实例的基准数据集（3 个模型族 × 3 种解码策略 × 4 个深度），提出 19 个统计特征 + Random Forest 的轻量管线，引入 EDD（Effective Discriminable Depth）指标。主要发现：(1) 深度信号集中在困惑度分布尾部；(2) 解码策略比模型架构更影响跨条件迁移；(3) 信号随模型规模衰减（14B 时 EDD_75=0）。

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 任务定义新颖、实证分析扎实，但方法论创新不足，且关键泛化瓶颈（跨策略 45.9%、14B EDD=0）严重限制了实际影响力，达到 Findings 标准但距 Conference 有差距。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.0/5 | 实验在受控基准内设计严谨，但核心主张（"fingerprints are consistent in direction"）与跨策略/跨模型迁移的弱结果存在张力；Abstract 中 "14B cross-reference accuracy ≈19%" 与 Section 5.4 报告的 44.1% 存在明显不一致 |
| **Excitement** | 2.5/5 | 任务定义有学术价值，但管线在已知条件外无法部署（跨策略 45.9%），且在实际规模模型上信号消失（14B EDD=0），限制了 excitement |
| **Reproducibility** | 4.0/5 | 超参数、数据构建、训练细节在正文和附录中均有详细说明；硬件和软件版本记录完整（Appendix B.34）；代码/数据承诺释放但未提供匿名链接 |
| **Confidence** | 4/5 | 我对模型坍塌、AI 文本检测和序数分类文献有较好了解，仔细阅读了全部27页 |

---

## 主要优势（Strengths）

**S1. 任务定义的新颖性与动机合理性。** 将递归生成深度从二分类（human vs. AI）推广到序数估计是一个自然且有价值的形式化。与 model collapse 文献（研究迭代训练的分布漂移）和 AI text detection 文献（关注二分类检测）的区分在 Section 2 中阐述清晰。Introduction 的动机——"合成数据如果自身又被用于训练，质量如何衰退"——切中当前 LLM 数据生态的实际痛点。

**S2. 系统性实证分析的深度令人印象深刻。** 180K 实例、3×3 网格、4 个深度的基准设计覆盖了合理的变量空间。附录中 30+ 个消融实验（B.1–B.34）的密度在 EMNLP 投稿中少见。Depth Degradation Atlas（Section 4.5, Figure 2）提供了直观的跨模型跨策略退化全景图。诚实报告负面结果（跨策略迁移失败、14B 衰减）也值得肯定。

**S3. 特征重要性分析透彻。** 通过 Gini、SHAP、条件排列重要性（CPI）三种独立方法交叉验证特征排名（Section 4.2, Appendix B.2–B.3），发现 p90_ppl、var_surprisal 稳定居前。消融实验（Section 4.2, d2 ablation）确认困惑度尾部统计量 vs. 去除后的性能差异，佐证了 Section 3.5 的理论动机。

**S4. EDD 指标有操作价值。** 将"分类器在哪个深度失效"凝练为单一标量（Definition 1），便于跨条件对比。EDD 的几何衰减观察（Section 4.3）与 model collapse 文献中指数衰减的理论预期一致。

**S5. Limitations 和 Ethics Statement 存在且有实质内容。** Limitations 覆盖了 full-replacement assumption、规模限制、混合比例等关键局限（第9页）。

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] **Abstract/正文数据不一致："14B cross-reference accuracy ≈19%"**
- 具体位置：Abstract（第1页）vs. Section 5.4（第8页）
- 问题：Abstract 称 "14B cross-reference accuracy ≈19%"，但 Section 5.4 明确报告 "cross-reference (Pythia-1.4B) drops accuracy to 44.1%"。如果 ≈19% 指的是"超过随机基线的百分点"(44.1%−25%=19.1pp)，则表述极易误读为绝对准确率——一个低于随机猜测的数字。如果是其他含义（某个子集、某个深度类别的准确率），则需要澄清。
- 为什么影响接收：Abstract 中的核心数字与正文矛盾（或至少严重歧义）直接损害论文可信度。审稿人和读者首先读 Abstract——如果第一印象就是数字不对，后续所有 claim 都会被质疑。
- 建议修改方向：统一 Abstract 与 Section 5.4 的报告方式。如果要表达"超过随机基线"的增益，使用 "19pp above chance" 或 "44.1% (vs. 25% chance)" 等无歧义表述。

**N2** [Critical] **核心 claim 与证据的系统性失配：泛化性**
- 具体位置：Abstract ("fingerprints are consistent in direction but scale-dependent in magnitude"), Section 4.4 (cross-strategy transfer 45.9%), Section 5.2 (cross-model transfer 46.7%), Table 9, Table 5
- 问题：论文的核心叙事是"递归生成在文本中留下可检测的统计指纹"——这暗示了某种程度的通用性。但三组迁移实验全面否定了这一暗示：
  - 跨策略迁移：45.9% 4-class（chance=25%），仅略高于随机
  - 跨模型迁移（leave-one-out）：46.7%
  - 14B 跨参考模型：44.1%
  
  Abstract 中 "consistent in direction" 的措辞将方向一致性包装为正面结论，但实际上一个 45.9% 的分类器在部署场景中几乎不可用。论文标题中的 "Statistical Fingerprints" 暗示某种稳定的、可迁移的信号，但实证表明这些"指纹"高度依赖于已知的模型族和解码策略——这更接近于 dataset-specific 的过拟合特征，而非真正的 fingerprint。
- 为什么影响接收：如果 claim scope 不与证据对齐，soundness 受损。当前的 framing 让读者期待一个通用工具，但实际交付的是一个 within-cell 的诊断工具。
- 建议修改方向：在 Abstract 和 Introduction 中明确限定 claim scope 为 "within known model-strategy configurations"；将跨条件迁移失败作为核心发现之一前置（而非在 Section 4.4/5.2 作为附加分析报告）；讨论这对 "fingerprint" 这一术语的适用性意味着什么。

**N3** [Critical] **规模衰减问题对论文立论的根本威胁**
- 具体位置：Section 5.4（第8页），Appendix B.19（第19–20页）
- 问题：在 14B (Qwen2.5-14B) 上，即使使用 self-reference，EDD_75=0——这意味着没有任何相邻深度对可以被可靠区分。4-class 准确率 50.8% 虽然是随机的两倍，但序数结构已完全坍塌。考虑到当前主流 LLM 是 70B–405B 规模，1.4B 基准上的 95–82% 准确率在实际应用中的参考价值有限。论文在 Limitations 中承认了这一点，但 Introduction 和 Discussion 的叙事仍然以积极的语气讨论这个任务的前景，没有充分传达这是当前方法的根本瓶颈。
- 为什么影响接收：如果方法在目标应用场景的模型规模上根本不工作，则论文的 impact 主要是学术/诊断性的，而非实用性的。这本身并不否定论文价值，但需要在 framing 中诚实反映。
- 建议修改方向：在 Introduction 的 contribution 列表中增加一个显式声明："our method is currently effective at 1–1.5B scale but depth signal vanishes at 14B, indicating that scaling remains an open challenge"；Discussion 中需要分析为什么规模增大导致信号消失（是因为更大模型的生成更接近人类分布？还是因为参考模型的困惑度估计不够灵敏？）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Warning] **方法论创新不足**
- 具体位置：Section 3.3（Table 1），Section 3.4
- 问题：19 个统计特征（困惑度矩、惊奇度统计量、词汇比率、n-gram 重复率）均为标准 NLP 特征，无一是本文提出的。分类器使用 off-the-shelf Random Forest。论文将此定位为 "lightweight" 的优势，但从方法论贡献的角度，这本质上是"将已有特征应用于新分类任务"——接近于实证研究而非方法创新。与 PLM 表征的对比（Appendix B.12）表明统计特征优于 DeBERTa/RoBERTa 的预训练表征，但论文未深入分析为什么——如果困惑度尾部统计量捕获了 PLM 无法编码的分布漂移信号，这个 why 本身就是一个有趣的发现，值得在正文中展开讨论。
- 建议：在 Discussion 中增加一段分析：为什么浅层统计特征优于深度 PLM 表征？这对 NLP 特征工程有什么更广泛的启示？

**W2** [Warning] **序数分类框架与实际方法的脱节**
- 具体位置：Section 3.1（"the underlying task is ordinal classification"），Appendix B.25（CORAL/CLOC 结果）
- 问题：论文在 Section 3.1 明确将任务框架为序数分类，强调 "depths carry a natural ordering"，并引用 CORAL 和 CLOC 作为背景。然而主管线使用标准 RF（不利用序数结构），而 CORAL 的消融结果在 Appendix B.25 中才出现，显示仅有边际改善。这产生一个叙事断裂：如果序数结构是任务的核心特征，为什么主方法不利用它？如果序数方法没有帮助，为什么在 framing 中强调序数性质？
- 建议：在正文中简要讨论为什么序数分类方法在此任务中没有显著优势（例如，是否因为类别数少 K=4，序数约束的收益有限？）。

**W3** [Warning] **参考模型依赖性在正文中讨论不充分**
- 具体位置：Section 3.3（"All statistical features §3.3 use Pythia-1.4B as fixed reference model"），Appendix B.17（Table 18）
- 问题：整个管线的核心操作——计算 19 个统计特征——依赖于用 Pythia-1.4B 作为参考模型计算每个 passage 的 token-level 困惑度。这意味着部署时需要运行一个完整的语言模型做推理。Appendix B.17 显示跨架构参考模型（GPT-2 XL, GPT-Neo）导致 4–11pp 准确率下降。正文中仅在 Section 3.3 一句话提及，未讨论这一依赖的实际含义和局限性。
- 建议：在 Section 3.3 或 Discussion 中增加一段讨论参考模型选择对实际部署的影响。

**W4** [Warning] **受控基准与真实场景的差距**
- 具体位置：Section 3.2（Benchmark Construction），Limitations（第9页）
- 问题：基准使用完全受控的 full-replacement chain——每一代使用同一 LoRA 配置对同一模型微调，seed 全部来自 Wikipedia。真实世界的递归生成远比这复杂：(a) 部分替换和混合比例（Limitations 中提及但未实验）；(b) 不同代使用不同模型或不同微调配置；(c) 非 Wikipedia 领域（新闻、社交媒体、代码）。Appendix B.15 的 wild-data 实验仅限于 WikiText-103 和 C4，且仅测试 d0 分类（即判断是否为人类文本），未触及 d≥1 的真实递归生成数据。
- 建议：在 Discussion 中明确承认当前基准是 "proof-of-concept under idealized conditions"，并讨论向真实场景扩展需要解决的关键问题。

---

## 小问题（不影响接收）

**M1** [Minor] Abstract 信息密度过高。最后一个长括号 "(14B cross-reference accuracy ≈19%, EDD_{75}≈2 for nuclei and temperature, 0 for top-1, with reference-model observer accounting for ~7pp of the apparent degradation)" 在一个括号内塞入 4 个不同维度的数字，读者很难在第一遍阅读时解析。建议拆分为独立句子或精简。

**M2** [Minor] 标题中 "Statistical Fingerprints" 的术语选择。"Fingerprint" 暗示唯一性和可迁移性（如基因指纹），但论文的迁移实验表明这些信号高度依赖于特定模型族和解码策略。"Statistical Signatures" 或 "Statistical Indicators" 可能更准确。

**M3** [Minor] Figure 2（Depth Degradation Atlas heatmap）在打印尺寸下可读性有限。细胞内数字较小，颜色梯度在相邻值间区分度不足。建议增大字号或拆分为多个子图。

**M4** [Minor] 脚注 3（第5页）承认 "Statistical tests are not corrected for multiple comparisons; p-values should be interpreted as exploratory"。对于一篇在多个条件下进行大量比较的论文，这削弱了统计声明的力度。至少应报告哪些结论在 Bonferroni 校正后仍然显著。

**M5** [Minor] Section 3.5 标题为 "Theoretical Motivation" 但内容主要是经验观察（困惑度尾部单调递减、惊奇度方差递增），缺少正式的理论推导。"Empirical Motivation" 可能更准确。

---

## Questions（需作者回答）

**Q1.** Abstract 中 "14B cross-reference accuracy ≈19%" 具体指什么？Section 5.4 报告 Pythia-1.4B 作为跨参考模型在 Qwen2.5-14B 上的 4-class 准确率为 44.1%，与 19% 明显不一致。请澄清这个数字的来源和含义。

**Q2.** 为什么主管线不使用序数分类器（如 ordinal logistic regression 或 CORAL loss 的 RF 变体），而是使用标准多类 RF？Appendix B.25 显示 CORAL 仅有边际改善——是否有分析为什么序数结构在此任务中不重要？

**Q3.** 对于跨策略迁移失败（45.9%），是否考虑过两阶段方案——先识别解码策略，再做策略条件化的深度估计？这在部署中可能是一个实用的折中方案。

**Q4.** EDD_75=0 在 14B scale 上意味着没有相邻深度对可被区分。作者是否有关于更大模型（70B+）的预期？是否有理论依据认为更大模型的深度信号会进一步衰减，还是可能存在 U 型曲线（更大模型的生成多样性下降反而增强深度信号）？

**Q5.** Appendix B.12 表明统计特征优于 DeBERTa/RoBERTa 的预训练表征（20pp accuracy gap）。作者是否分析过为什么？直觉上，预训练的 PLM 应该能捕获分布漂移——如果不能，这对 NLP 表征学习有何启示？

---

## Missing References

1. **数据过滤/策展管线**：FineWeb (Penedo et al., 2024)、DCLM (Li et al., 2024) 等大规模数据策展工作中使用 AI 文本过滤作为质量控制手段。深度估计作为比二分类更细粒度的过滤信号，与这些工作有直接联系，但未被讨论。
2. **合成数据质量评估**：近期关于合成数据用于训练的质量评估框架（如 Sachdeva et al., 2024, "Training on the Test Task"等）可能与深度估计的数据策展应用相关。
3. 作者应确认 2025–2026 年是否有直接研究递归/迭代文本生成深度估计的新工作发表（我未检索到，但应由作者确认）。

---

## Overall Assessment

**评分：3.0 (Findings)**
**置信度：4/5**

本文在任务定义层面有清晰的新颖性——将递归生成深度从二分类推广到序数估计是自然且有价值的形式化。实证分析的深度和系统性（180K 基准、30+ 消融、多种特征重要性分析方法交叉验证）达到顶会标准。EDD 指标提供了有用的操作性摘要。

但三个因素限制了 Conference 评分：

(1) **方法论贡献不足**：管线由全部已有组件组成（标准特征 + 标准分类器），无方法创新。这更像是一个 well-executed empirical study。

(2) **泛化性瓶颈未在 framing 中充分反映**：跨策略/跨模型迁移的弱结果（45–47%）意味着该方法仅在已知配置下可用，但 Abstract 和 Introduction 的叙事暗示了更广泛的适用性。"Statistical Fingerprints" 的标题强化了这种过度预期。

(3) **规模衰减是根本性的**：14B EDD_75=0 对论文的实际影响力构成上限。在当前 LLM 生态中（70B+ 模型），1.4B 规模的成功更多是 proof-of-concept 而非可部署方案。

这些问题不否定论文的学术价值——对递归生成退化模式的系统性实证刻画、困惑度尾部信号的识别、以及 Depth Degradation Atlas 的概念，都是有意义的贡献。但 impact 和 scope 更适合 Findings 而非 Conference。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1738 · 2026-05-22T23:01:42.786150+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 初始化到独立审稿', 'status': 'completed', 'activeForm': '初始化和独立审稿已完成'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见并收集回应', 'status': 'in_progress', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-1: 初始化到独立审稿', 'status': 'completed', 'activeForm': '初始化和独立审稿已完成'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见并收集回应', 'status': 'in_progress', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1739 · 2026-05-22T23:01:42.786540+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1740 · 2026-05-22T23:02:11.560296+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（新颖性、完整性、写作质量）\n\n**Overall**: 3.0 (Findings) | **Confidence**: 4/5\n**一句话总结**: 任务定义新颖、实证分析扎实，但方法论创新不足，且关键泛化瓶颈（跨策略 45.9%、14B EDD=0）严重限制了实际影响力，达到 Findings 标准但距 Conference 有差距。\n\n**维度打分**: Soundness 3.0/5, Excitement 2.5/5, Reproducibility 4.0/5\n\n**Strengths**:\n- S1: 任务定义新颖，与 model collapse 和 AI text detection 文献区分清晰\n- S2: 系统性实证分析深度令人印象深刻（180K 实例、30+ 消融）\n- S3: 特征重要性分析透彻（Gini/SHAP/CPI 三方交叉验证）\n- S4: EDD 指标有操作价值\n- S5: Limitations 和 Ethics Statement 有实质内容\n\n**Must-Fix (Critical)**:\n- N1: Abstract 中 \"14B cross-reference accuracy ≈19%\" 与 Section 5.4 的 44.1% 不一致——如果是\"超过随机基线的 pp\"则表述极易误读为绝对准确率\n- N2: 核心 claim 与证据系统性失配——跨策略 45.9%、跨模型 46.7%、14B 44.1% 全面否定 \"fingerprints\" 的通用性暗示。\"consistent in direction\" 包装方向一致性为正面结论，但 45.9% 的分类器几乎不可用。标题中 \"Statistical Fingerprints\" 暗示可迁移信号，实证表明更接近 dataset-specific 过拟合\n- N3: 14B EDD_75=0 意味着没有任何相邻深度对可靠区分。当前主流 LLM 是 70B–405B，1.4B 成功更多是 proof-of-concept。Introduction/Discussion 叙事仍以积极语气讨论前景，未充分传达这是根本瓶颈\n\n**Should-Fix (Warning)**:\n- W1: 方法论创新不足——19 特征均为标准 NLP 特征，RF 为 off-the-shelf，本质是\"已有特征应用于新任务\"\n- W2: 序数分类框架与实际方法脱节——强调 ordinal 但主管线用标准 RF 不利用序数结构\n- W3: 参考模型依赖性正文讨论不充分\n- W4: 受控基准与真实场景差距大——full-replacement chain 远比真实递归生成简单\n\n**Minor**:\n- M1: Abstract 信息密度过高，最后长括号难解析\n- M2: \"Statistical Fingerprints\" 术语选择——\"Signatures\" 或 \"Indicators\" 可能更准确\n- M3: Figure 2 打印尺寸下可读性有限\n- M4: Footnote 3 承认未校正多重比较，削弱统计声明力度\n- M5: Section 3.5 \"Theoretical Motivation\" 内容主要是经验观察，\"Empirical Motivation\" 可能更准确\n\n**Questions**:\n- Q1: Abstract \"14B cross-reference accuracy ≈19%\" 具体指什么？\n- Q2: 为什么主管线不用序数分类器？\n- Q3: 跨策略迁移失败是否考虑两阶段方案（先识别策略再做深度估计）？\n- Q4: EDD_75=0 在 14B 上——更大模型（70B+）的预期？\n- Q5: 统计特征优于 PLM 表征 20pp 的原因分析？\n\n**Missing References**: FineWeb (Penedo et al., 2024), DCLM (Li et al., 2024), Sachdeva et al. (2024) Training on the Test Task"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（新颖性、完整性、写作质量）\n\n**Overall**: 3.0 (Findings) | **Confidence**: 4/5\n**一句话总结**: 任务定义新颖、实证分析扎实，但方法论创新不足，且关键泛化瓶颈（跨策略 45.9%、14B EDD=0）严重限制了实际影响力，达到 Findings 标准但距 Conference 有差距。\n\n**维度打分**: Soundness 3.0/5, Excitement 2.5/5, Reproducibility 4.0/5\n\n**Strengths**:\n- S1: 任务定义新颖，与 model collapse 和 AI text detection 文献区分清晰\n- S2: 系统性实证分析深度令人印象深刻（180K 实例、30+ 消融）\n- S3: 特征重要性分析透彻（Gini/SHAP/CPI 三方交叉验证）\n- S4: EDD 指标有操作价值\n- S5: Limitations 和 Ethics Statement 有实质内容\n\n**Must-Fix (Critical)**:\n- N1: Abstract 中 \"14B cross-reference accuracy ≈19%\" 与 Section 5.4 的 44.1% 不一致——如果是\"超过随机基线的 pp\"则表述极易误读为绝对准确率\n- N2: 核心 claim 与证据系统性失配——跨策略 45.9%、跨模型 46.7%、14B 44.1% 全面否定 \"fingerprints\" 的通用性暗示。\"consistent in direction\" 包装方向一致性为正面结论，但 45.9% 的分类器几乎不可用。标题中 \"Statistical Fingerprints\" 暗示可迁移信号，实证表明更接近 dataset-specific 过拟合\n- N3: 14B EDD_75=0 意味着没有任何相邻深度对可靠区分。当前主流 LLM 是 70B–405B，1.4B 成功更多是 proof-of-concept。Introduction/Discussion 叙事仍以积极语气讨论前景，未充分传达这是根本瓶颈\n\n**Should-Fix (Warning)**:\n- W1: 方法论创新不足——19 特征均为标准 NLP 特征，RF 为 off-the-shelf，本质是\"已有特征应用于新任务\"\n- W2: 序数分类框架与实际方法脱节——强调 ordinal 但主管线用标准 RF 不利用序数结构\n- W3: 参考模型依赖性正文讨论不充分\n- W4: 受控基准与真实场景差距大——full-replacement chain 远比真实递归生成简单\n\n**Minor**:\n- M1: Abstract 信息密度过高，最后长括号难解析\n- M2: \"Statistical Fingerprints\" 术语选择——\"Signatures\" 或 \"Indicators\" 可能更准确\n- M3: Figure 2 打印尺寸下可读性有限\n- M4: Footnote 3 承认未校正多重比较，削弱统计声明力度\n- M5: Section 3.5 \"Theoretical Motivation\" 内容主要是经验观察，\"Empirical Motivation\" 可能更准确\n\n**Questions**:\n- Q1: Abstract \"14B cross-reference accuracy ≈19%\" 具体指什么？\n- Q2: 为什么主管线不用序数分类器？\n- Q3: 跨策略迁移失败是否考虑两阶段方案（先识别策略再做深度估计）？\n- Q4: EDD_75=0 在 14B 上——更大模型（70B+）的预期？\n- Q5: 统计特征优于 PLM 表征 20pp 的原因分析？\n\n**Missing References**: FineWeb (Penedo et al., 2024), DCLM (Li et al., 2024), Sachdeva et al. (2024) Training on the Test Task"
  }
}
```

</details>

---


### Tool result

_source line 1741 · 2026-05-22T23:02:36.382046+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24821
}
```

</details>

---


### Tool call

_source line 1742 · 2026-05-22T23:02:36.603237+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（方法严谨性和实验设计）\n\n**Overall**: 3.5 (Borderline Conference) | **Confidence**: 4/5\n**一句话总结**: 问题新颖、实验覆盖面广，但 reference model 依赖、full-replacement 与真实场景的 gap、以及多重比较未校正等方法论问题限制了其可信度和实用性。\n\n**维度打分**: Soundness 3/5, Excitement 3.5/5, Reproducibility 4/5\n\n**Must-Fix (Critical)**:\n- N1: Reference model 依赖是 pipeline 根本瓶颈——Table 18 cross-architecture 从 78.6% 降至 67.3%（-11.3pp），19 特征中 12 个依赖 Pythia-1.4B log-probabilities，main text 仅笼统提 \"~7pp\" 讨论不足，建议增加 reference-agnostic baseline\n- N2: 多重比较未校正但做了实质性判断——Footnote 1 声明 uncorrected 但 Section 5.1 称 Binoculars \"statistical equivalence\"（p>0.05），非显著性 ≠ 等价性需 TOST equivalence test。以 \"Statistical Fingerprints\" 为卖点的论文统计推断本身缺乏严谨性\n- N3: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap——Appendix B.8 仅覆盖 6 个组合，GPT-2 XL 50% mixing 出现 boundary failure（AUC=0.695）\n\n**Should-Fix (Warning)**:\n- W1: Neural baselines 比较不公平——RF 有 reference model oracle，DeBERTa/RoBERTa 只看原文\n- W2: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺乏理论论证\n- W3: Cross-model transfer 平均仅 64.8%，Pythia holdout 55.4%，泛化声明需更审慎\n- W4: 14B self-reference confound 无法干净分离 scale effect 和 reference-model confound\n- W5: BOS seeding vs prompted generation 差 13.8pp，主 benchmark depth signal 可能部分是 artifact\n- W6: 单 LoRA seed 主实验，仅 2-seed replication 不足以估计方差分布\n\n**Questions**:\n- Q1: Table 18 显示 -11.3pp，main text 说 \"~7pp\"，请澄清差异来源\n- Q2: Generator-unknown 场景下的 reference model 选择策略？\n- Q3: T=0.70 边界处 d2 per-class recall 是否低于 chance？\n- Q4: 10% mixing ratio 下 pipeline 是否仍能工作？\n- Q5: BOS vs prompted 的 13.8pp gap 是否意味着主 benchmark 有 artifact？\n- Q6: QWK=0.89 对应什么 ordinal misclassification pattern？\n\n**Missing References**: Lakens (2017) equivalence testing, Gutiérrez et al. (2016) ordinal regression 综述, Alemohammad et al. (2024) autophagous loops\n\n**升分条件**: 如果 rebuttal 能提供 (a) reference-agnostic baseline/ensemble, (b) Bonferroni-corrected key claims, (c) 更全面的 accumulation 实验，愿意提高至 4.0。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（方法严谨性和实验设计）\n\n**Overall**: 3.5 (Borderline Conference) | **Confidence**: 4/5\n**一句话总结**: 问题新颖、实验覆盖面广，但 reference model 依赖、full-replacement 与真实场景的 gap、以及多重比较未校正等方法论问题限制了其可信度和实用性。\n\n**维度打分**: Soundness 3/5, Excitement 3.5/5, Reproducibility 4/5\n\n**Must-Fix (Critical)**:\n- N1: Reference model 依赖是 pipeline 根本瓶颈——Table 18 cross-architecture 从 78.6% 降至 67.3%（-11.3pp），19 特征中 12 个依赖 Pythia-1.4B log-probabilities，main text 仅笼统提 \"~7pp\" 讨论不足，建议增加 reference-agnostic baseline\n- N2: 多重比较未校正但做了实质性判断——Footnote 1 声明 uncorrected 但 Section 5.1 称 Binoculars \"statistical equivalence\"（p>0.05），非显著性 ≠ 等价性需 TOST equivalence test。以 \"Statistical Fingerprints\" 为卖点的论文统计推断本身缺乏严谨性\n- N3: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap——Appendix B.8 仅覆盖 6 个组合，GPT-2 XL 50% mixing 出现 boundary failure（AUC=0.695）\n\n**Should-Fix (Warning)**:\n- W1: Neural baselines 比较不公平——RF 有 reference model oracle，DeBERTa/RoBERTa 只看原文\n- W2: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺乏理论论证\n- W3: Cross-model transfer 平均仅 64.8%，Pythia holdout 55.4%，泛化声明需更审慎\n- W4: 14B self-reference confound 无法干净分离 scale effect 和 reference-model confound\n- W5: BOS seeding vs prompted generation 差 13.8pp，主 benchmark depth signal 可能部分是 artifact\n- W6: 单 LoRA seed 主实验，仅 2-seed replication 不足以估计方差分布\n\n**Questions**:\n- Q1: Table 18 显示 -11.3pp，main text 说 \"~7pp\"，请澄清差异来源\n- Q2: Generator-unknown 场景下的 reference model 选择策略？\n- Q3: T=0.70 边界处 d2 per-class recall 是否低于 chance？\n- Q4: 10% mixing ratio 下 pipeline 是否仍能工作？\n- Q5: BOS vs prompted 的 13.8pp gap 是否意味着主 benchmark 有 artifact？\n- Q6: QWK=0.89 对应什么 ordinal misclassification pattern？\n\n**Missing References**: Lakens (2017) equivalence testing, Gutiérrez et al. (2016) ordinal regression 综述, Alemohammad et al. (2024) autophagous loops\n\n**升分条件**: 如果 rebuttal 能提供 (a) reference-agnostic baseline/ensemble, (b) Bonferroni-corrected key claims, (c) 更全面的 accumulation 实验，愿意提高至 4.0。"
  }
}
```

</details>

---


### Tool result

_source line 1743 · 2026-05-22T23:02:37.929273+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1326
}
```

</details>

---


### Assistant

_source line 1744 · 2026-05-22T23:02:40.981163+00:00_

交叉分享已派发。两位 Reviewer 正在审阅对方意见并准备 [AGREE]/[REBUT] 回应，等待返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 152

## Round 152

2 recorded events


### User

_source line 1745 · 2026-05-22T23:02:43.524765+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成。已向 Review Director 提交完整审稿意见，评分 **Overall 3.0 (Findings)**。

核心判断：
- **3 个 Critical 问题**：Abstract 数字不一致（≈19% vs. 44.1%）、泛化性 claim 与证据失配（跨策略 45.9%）、14B 规模 EDD=0 对立论的根本威胁
- **4 个 Warning 问题**：方法论创新不足（全部已有组件）、序数分类框架与实际方法脱节、参考模型依赖性讨论不充分、受控基准与真实场景差距大
- **主要优势**：任务定义新颖、实证分析系统性极强（180K 基准 + 30+ 消融）、特征重要性分析透彻

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1746 · 2026-05-22T23:02:51.096298+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 153

## Round 153

4 recorded events


### User

_source line 1747 · 2026-05-22T23:06:15.982198+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的逐条交叉回应

---

## 对 Strengths 的回应

R1 给出 Excitement 3.5/5，高于我的 2.5/5。R1 对任务新颖性的评价更积极，我认可任务定义的价值，但我对 excitement 的评分更多考虑了方法层面几乎无创新以及实际部署前景极其有限这两个因素。任务新颖 ≠ 论文 exciting——如果任务定义了但解法在目标规模上不 work，excitement 应打折。

---

## Must-Fix 逐条回应

### R1-N1: Reference model 依赖是 pipeline 根本瓶颈

**[AGREE]** 我在自己的审稿中将此列为 W3（Should-Fix），但 R1 提供了更具体的证据：12/19 特征依赖 Pythia-1.4B log-probabilities，Table 18 最大跨架构下降为 -11.3pp（Pythia-1.4B self 78.6% → GPT-2 XL cross 67.3%）。R1 指出正文中仅笼统说 "~7pp" 是有道理的——但需要注意，正文 Section 5.4 的 "~7pp" 指的是 **14B 规模下** self-reference (50.8%) vs. cross-reference (44.1%) 的差距（6.7pp≈~7pp），而 Table 18 的 -11.3pp 是 **1–1.5B 规模下** 的跨架构参考模型下降。这两个数字描述的是不同实验设定，不能直接对比。但无论如何，R1 要求增加 reference-agnostic baseline 的建议是合理的——目前管线完全绑定参考模型，这对实际部署是硬约束。

**不过我认为这可能更适合 Should-Fix 而非 Must-Fix。** 参考模型依赖是系统设计选择的后果，在 proof-of-concept 研究中可以接受，但论文确实应在正文中更充分地讨论这一限制。

### R1-N2: 多重比较未校正但做了实质性判断

**[AGREE]** R1 关于"非显著性 ≠ 等价性"需要 TOST equivalence test 的方法论批评是正确的。我在自己的审稿中将此列为 M4（Minor），但 R1 提升到 Critical 级别。

**我同意问题存在但对严重程度有不同判断。** 理由：论文的核心结论（特征重要性排名、within-cell 准确率、EDD 衰减模式）不依赖于这些具体的 p 值判断。Section 5.1 的 Binoculars 对比不是论文的核心 claim。将此定为 Critical 似乎过重。但 R1 的论点——"以 'Statistical Fingerprints' 为卖点的论文统计推断本身缺乏严谨性"——这个 meta 批评有说服力。补充 Bonferroni 校正或 TOST 在 rebuttal 中应该是可行的低成本修改。

**补充一点**：实际上，论文在 AUC 收敛分析中确实做了部分 Bonferroni 校正——Section 7（page 7）提到 "Bonferroni-corrected for 4 comparisons, α=0.0167"，说明作者并非完全不了解多重比较问题，只是在其他分析中未统一应用。

### R1-N3: Full-replacement benchmark 与真实 accumulation 场景的 gap

**[AGREE]** 我在自己的审稿中也将此列为 W4（Should-Fix）。R1 进一步指出 Appendix B.8 仅覆盖 6 个组合且 GPT-2 XL 50% mixing 出现 boundary failure (AUC=0.695)，使批评更具体。

**但我认为这应为 Should-Fix 而非 Must-Fix。** 任何新任务的首篇论文都需要从受控设定起步。Full-replacement 是研究递归退化的合理简化——它隔离了深度变量，排除了混合比例等混淆因素。真实场景的 gap 是后续工作的自然方向，不应因此否定基础研究的价值。论文在 Limitations（第9页）中明确承认了这一局限。但我同意 Appendix B.8 的 accumulation 实验覆盖面不足，特别是 boundary failure 说明方法在更现实条件下的鲁棒性堪忧。

---

## Should-Fix 逐条回应

### R1-W1: Neural baselines 比较不公平

**[AGREE]** 这个批评切中要害。Appendix B.12 中 RF 使用 Pythia-1.4B 的 token-level log-probabilities 计算的 19 维特征向量，而 DeBERTa/RoBERTa 仅获得原文 [CLS] 表征——信息输入不对等。论文自己在 B.12 中也指出 "var_surprisal and p75_ppl yield negative R² under linear probing; these features are not linearly accessible in the pretrained representation space"——但这恰恰说明应该给 PLM 一个公平机会：例如将参考模型的 perplexity 序列作为额外输入通道馈送给 PLM。当前对比更像是在说明 "PLM 不能从原文中推断出困惑度分布统计量"（这并不意外），而非 "统计特征优于深度学习"。

### R1-W2: EDD 阈值 T=0.70 缺乏理论论证

**[AGREE]** 但程度较轻。论文引用 Hosmer & Lemeshow (2000) 的 binary ROC "acceptable discrimination" 阈值作为依据（Section 4.3, page 5），但 R1 正确指出从 binary ROC AUC 到 ordinal pairwise AUC 的迁移需要额外论证——两者的随机基线和语义含义不完全一致。不过 EDD 本质上是一个操作性摘要指标而非理论量，作者也报告了多个阈值下的 sensitivity（Section 4.3 提到 T=0.65 时 5-class extensions 达到 d4）。这个问题通过增加一段阈值选择的敏感性讨论即可解决，不构成严重缺陷。

### R1-W3: Cross-model transfer 泛化声明需更审慎

**[AGREE]** 与我自己的 N2 (Critical) 完全一致。Table 5 显示 leave-one-out 平均 64.8%（4-class），Pythia holdout 最低 55.4%（接近 d0-vs-rest 的 trivial baseline）。论文的跨模型泛化远未达到可部署水平。

### R1-W4: 14B self-reference confound

**[REBUT]** R1 认为无法干净分离 scale effect 和 reference-model confound。但论文在 Section 5.4 报告了 14B **self-reference** 结果（50.8%, EDD_75=0），这意味着即使使用 Qwen2.5-14B 自身作为参考模型（消除参考模型失配），深度信号仍然极弱。Self-reference 与 cross-reference 的差距仅 ~7pp（50.8% vs 44.1%），而与 1-1.5B 的差距是 30+pp。这已经足够证明 **scale 是主要驱动因素**，reference-model mismatch 是次要因素。confound 确实存在（self-reference 在 14B 上也不完美），但因果方向已基本可分离。

### R1-W5: BOS seeding vs prompted generation 13.8pp gap

**[AGREE]** 这是我在 Round 1 审稿中未充分关注的一个好问题。如果深度信号部分依赖于无条件生成（BOS seeding）的特定退化模式，而有条件生成（prompted）的退化模式不同且信号更弱（-13.8pp），则主基准的结论可能高估了深度信号在现实场景中的强度。Appendix B.16 将此标记为 "Inconclusive"，但一个 13.8pp 的差距值得在正文中讨论——它暗示深度信号的一部分可能来自 BOS seeding 的特异性 artifact 而非递归退化本身。

### R1-W6: 单 LoRA seed，2-seed replication 不足

**[AGREE]** 但程度较轻。Appendix B.21（Table 23）的 2-seed replication 显示方向一致性——seed-42 和 seed-43 的准确率差异在 1pp 以内，且 CIs 重叠。理想情况下应有 3-5 seeds，但考虑到每个 seed 需要对 180K 实例重新生成的计算成本，2-seed replication 作为 sanity check 可以接受。关键问题不是 seed 方差，而是 seed 数量不足以估计方差的 **分布**。

---

## Questions 回应

### R1-Q1: Table 18 的 -11.3pp vs main text 的 ~7pp

**[AGREE]** 需要作者澄清。如我上面分析，~7pp 指 14B scale 下 self vs cross reference 的差距（Section 5.4: 50.8% vs 44.1% = 6.7pp），而 -11.3pp 指 1-1.5B scale 下 Pythia self vs GPT-2 XL cross 架构的差距（Table 18）。这两个数字描述不同实验设定。但正文的呈现确实容易误解为同一个比较，需要更清晰的标注。

### R1-Q2: Generator-unknown 场景下的 reference model 选择

**[AGREE]** 这是一个关键的实用问题。论文未讨论在不知道生成器的部署场景中如何选择参考模型。

### R1-Q3: T=0.70 边界处 d2 per-class recall

**[AGREE]** 有价值的问题。从 Appendix B.5（Table 8），d2 是所有 cell 中 recall 最低的类别（lowest-recall class），这与 EDD 的 boundary 行为直接相关。

### R1-Q4: 10% mixing ratio 下 pipeline 是否工作

**[AGREE]** 重要问题。Appendix B.8 的 accumulation 实验覆盖了 25% 和 50% mixing，但未测试 10%。鉴于 50% mixing 已出现 boundary failure (AUC=0.695)，10% mixing 很可能完全失败。

### R1-Q5: BOS vs prompted artifact

**[AGREE]** 如 W5 所述。

### R1-Q6: QWK=0.89 对应什么 ordinal misclassification pattern

**[AGREE]** 有价值。QWK=0.89 是一个聚合指标，需要配合 confusion matrix（Appendix B.6, Figure 5）理解具体的误分类模式。从 Figure 5 可见主要误分类集中在 d2↔d3 边界。

---

## Missing References 回应

### Lakens (2017) equivalence testing
**[AGREE]** 如果接受 R1-N2 的 TOST 批评，此引用是必要的。

### Gutiérrez et al. (2016) ordinal regression 综述
**[AGREE]** 与我自己的 W2（序数框架与实际方法脱节）一致，这篇综述可以支持更充分的序数分类方法讨论。

### Alemohammad et al. (2024) autophagous loops
**[REBUT]** 此文**已被引用**。Section 2 第1段（第2页）明确写道 "extended to autophagous loops in the MAD framework (Alemohammad et al., 2024)"。R1 可能遗漏了这一引用。

---

## 对 R1 总体评分的回应

R1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。核心分歧在于：

1. **方法论创新的权重**：R1 的 Excitement 3.5 似乎主要基于任务新颖性，但我认为"用标准特征+标准分类器解决新任务"的方法论贡献不足以支撑 Conference 级别的 excitement。

2. **泛化失败的影响**：R1 将此列为 N3（Critical）但仍给 3.5，暗示 proof-of-concept 的价值可弥补泛化不足。我认为跨策略 45.9% + 14B EDD=0 这两个结果的组合已经从根本上限制了论文的 impact。

3. **R1 的升分条件合理**：如果 rebuttal 能提供 (a) reference-agnostic baseline、(b) Bonferroni-corrected claims、(c) 更全面的 accumulation 实验，我也愿意重新评估。但 (a) 和 (c) 可能需要额外实验，在 rebuttal 期间完成有难度。

**我维持 3.0 (Findings) 的评分。**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1748 · 2026-05-22T23:06:26.285379+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 初始化到独立审稿', 'status': 'completed', 'activeForm': '初始化和独立审稿已完成'}, {'content': 'Step 2: 交叉分享 — Reviewer 2 回应 R1', 'status': 'completed', 'activeForm': 'Reviewer 2 完成交叉回应'}, {'content': 'Step 2: 交叉分享 — Reviewer 1 回应 R2', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-1: 初始化到独立审稿', 'status': 'completed', 'activeForm': '初始化和独立审稿已完成'}, {'content': 'Step 2: 交叉分享 — Reviewer 2 回应 R1', 'status': 'completed', 'activeForm': 'Reviewer 2 完成交叉回应'}, {'content': 'Step 2: 交叉分享 — Reviewer 1 回应 R2', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1749 · 2026-05-22T23:06:26.285787+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1750 · 2026-05-22T23:06:28.033382+00:00_

Reviewer 2 交叉回应已收到，等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 154

## Round 154

2 recorded events


### User

_source line 1751 · 2026-05-22T23:06:35.264394+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。总结：

- 对 R1 的 3 个 Must-Fix 中，**N1（参考模型依赖）和 N3（full-replacement gap）实质同意但认为严重程度应降至 Should-Fix**；**N2（多重比较）同意问题存在但认为不构成 Critical**
- 对 6 个 Should-Fix 中，**W1–W3、W5–W6 同意**；**W4（14B confound）反驳**——self-reference 结果（50.8%, EDD=0）已足够分离 scale 与 reference-model 因素
- **反驳 R1 的 Missing Reference**：Alemohammad et al. (2024) 已在 Section 2 第1段明确引用
- **维持 3.0 (Findings) 评分**，与 R1 的 3.5 存在 0.5 分差距，核心分歧在方法论创新权重和泛化失败的影响评估

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1752 · 2026-05-22T23:06:39.576077+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 155

## Round 155

20 recorded events


### User

_source line 1753 · 2026-05-22T23:07:48.766224+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的逐条交叉回应

### 总体立场
R2 给 3.0 (Findings)，我给 3.5 (Borderline Conference)。分歧主要在 Excitement（R2: 2.5 vs 我: 3.5）。我认为问题定义新颖性本身有显著价值，R2 在此维度上偏严格。但 R2 对泛化瓶颈和表述问题的诊断整体准确。

### Must-Fix 回应

**[AGREE] R2-N1 (Abstract "≈19%" 不一致)**: 核实确认——Section 5.4 报告 44.1%，"≈19%" 几乎确定是 above-chance margin (44.1%-25%=19.1pp) 的误写，读者会理解为低于 chance 的绝对准确率。必须修复。另外 Abstract 的 EDD₇₅=2 与 Section 5.4 的 EDD₇₅=0 也需要澄清数据来源差异。

**[AGREE，有细化] R2-N2 (Claim-evidence 失配)**: 跨条件迁移弱（cross-strategy 45.9%）确实与 "fingerprints" 叙事矛盾。但 R2 引用 "跨模型 46.7%" 在论文中找不到对应数字（Section 5.2 明确报告 d1-d3: 55.4%）——建议 R2 核实。我不同意 "dataset-specific 过拟合" 的定性——top features 在所有 9 cells 一致排名 top-2（Table 3, B.2），且 two-stage pipeline 将 cross-strategy 恢复到 70.5%（Section 5.3），说明信号存在但需策略适配。

**[AGREE，有精确化] R2-N3 (14B EDD₇₅=0)**: 实质同意——这是 scalability 的严重警示。技术上 EDD₇₅=0 不等于 "无信号"（self-reference 仍 50.8%=2× chance），但不影响核心论点：1.4B 成功更多是 proof-of-concept，论文 Discussion 对此传达不足。

### Should-Fix 回应

**[REBUT 部分] R2-W1 (创新不足)**: EMNLP 接收系统性实证研究，不要求每篇有 novel architecture。但同意这限制了 Excitement。

**[AGREE] R2-W2 (Ordinal 框架脱节)**: 论文强调 ordinal 但主 pipeline 不利用序数结构，存在 framing 不一致。

**[AGREE] R2-W3, W4**: 与我的 N1、N3 完全一致。

### Minor 回应
M1/M3/M4/M5 全部同意。M2 轻微反驳——"fingerprint" 在 forensics 文献中常见，但鉴于弱迁移结果确实有 framing risk。

### Questions 关键回应
**[REBUT] R2-Q3**: R2 可能遗漏了——论文已在 Section 5.3/Appendix B.31 报告了 two-stage pipeline 实验，将 cross-strategy 从 45.9% 恢复到 70.5%。

### R2 提出的 Missing References
FineWeb/DCLM/Sachdeva 与核心方法关联较间接，nice-to-have。我建议的 Lakens (2017) equivalence testing 和 Gutiérrez (2016) ordinal regression 综述更关键。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1754 · 2026-05-22T23:08:18.500084+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-2: 初始化到交叉分享', 'status': 'completed', 'activeForm': '初始化到交叉分享已完成'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '分析交叉回应判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-2: 初始化到交叉分享', 'status': 'completed', 'activeForm': '初始化到交叉分享已完成'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '分析交叉回应判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1755 · 2026-05-22T23:08:18.500556+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1756 · 2026-05-22T23:08:34.694218+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1757 · 2026-05-22T23:08:34.845915+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T22:53:22.420288+00:00\", \"completed_at\": \"2026-05-22T22:58:18.942005+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本（Abstract + Introduction + Related Work），无任何 display item。审稿人前 2 页完全无视觉锚点，第一印象建立延迟至 page 3 的 Figure 1。建议：将 Figure 1 提升到 page 2（Introduction 末尾或 Related Work 之前），或在 page 1 右栏插入一个简化版概念示意图\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（Recursive Generation Chain）作为首个 display item 出现在 page 3，概念清晰、caption 自包含，能有效传达核心 idea（递归生成链 + 深度估计任务）。配色使用蓝/橙/绿，色盲友好性可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1（19 statistical features）格式整洁，使用 booktabs 风格。与 Section 3.3 紧密配合，位置合理\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Definition 1（EDD）公式渲染正确，排版无异常。页面以 text + equation 为主，节奏可接受（数学定义段落例外）\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2（全宽）+ Table 3（单栏）密度合理。Table 2 最优结果已加粗标注。Table 3 用 bold 标记 top-2 features\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（heatmap）+ Figure 3（AUC curves）同页双图，视觉节奏好。Figure 2 的 y 轴 feature name 和 cell 内数字字号偏小，打印后可能难以辨认；Figure 3 三面板挤在单栏内，axis label 和 legend 字号偏小（约正文 60%）\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 2 heatmap 中 cell 内数值文字偏小（估计 ~6pt），Figure 3 三面板的 axis tick labels 同样偏小。建议：Figure 2 改为 figure*（全宽）以增大字号；或 Figure 3 减少为 2 面板 / 改为全宽\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"主文最后一页极度拥挤：Table 4（全宽）+ Table 5 + Section 5（含 5.1-5.4 四个子节）+ 整个 Section 6 Discussion and Conclusion 全部压缩在一页。审稿人可能认为 Generalization（Section 5）和 Discussion（Section 6）是匆忙收尾。Section 6 的多个加粗子主题（Multi-channel depth encoding / Why neural methods underperform / Feature hierarchy / Deployment considerations / Accumulation and outlook）虽然信息密度高，但视觉上非常紧凑\"}, {\"severity\": \"info\", \"dimension\": \"page 
…[truncated 1544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1758 · 2026-05-22T23:08:34.896614+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1759 · 2026-05-22T23:08:34.897069+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1760 · 2026-05-22T23:12:13.998687+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '初始化到收敛判断已完成'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '初始化到收敛判断已完成'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1761 · 2026-05-22T23:12:14.049318+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1762 · 2026-05-22T23:12:19.921093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1763 · 2026-05-22T23:12:20.072109+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K cell-instances (140K unique passages) spanning three model families, three decoding strategies, and four depths under controlled full-replacement chains at the 1--1.5B parameter scale.
4	A lightweight pipeline (19 statistical features classified by Random Forest) achieves d1--d3 balanced accuracy of 59--82\% across nine model--strategy cells, with $\mathrm{EDD}_{0.70} = 3$ in 8/9 cells.
5	Three findings emerge: (1)~depth signal concentrates in perplexity distribution tails, corroborated by classifier convergence and independent cross-perplexity features; (2)~decoding strategy affects cross-condition transfer more than model architecture, suggesting structurally distinct degradation trajectories; (3)~signal attenuates with scale (14B cross-reference accuracy ${\sim}44$\%, $\mathrm{EDD}_{0.70}{=}2$ for nucleus and temperature, 0 for top-$k$), with reference-model choice accounting for ${\sim}7$\,pp of the apparent degradation.
6	Our depth estimation claims hold most strongly within-strategy or when the decoding configuration is known; a two-stage routing pipeline recovers $+$11.5\,pp under cross-strategy transfer.
7	Perturbation-based and membership-inference baselines lack ordinal depth resolution, confirming that depth estimation requires distributional statistics beyond binary detection scores.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1764 · 2026-05-22T23:15:32.603016+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n# ============================================================\n# ROUND 19 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R19-C1\n  summary: 泛化性 claim 与证据系统性失配——跨策略 45.9%、14B EDD=0 与 \"fingerprints\" 通用性暗示矛盾\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N3: 跨策略 d1-d3 仅 45.9%\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续追踪，Abstract 已加 within-strategy scope 声明\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1 AGREE R2-N2。两人共识：Abstract 'consistent in direction' 将方向一致性包装为正面结论，但 45.9% 分类器不可用。标题 'Statistical Fingerprints' 暗示可迁移性与实证矛盾。Two-stage 恢复到 70.5% 但仍远低于 within-cell。R1 纠正 R2 引用的 '46.7%' 数字（实为 cross-τ 而非 cross-model）。\"}\n  action_items:\n  - {round: 19, action: \"Abstract/Introduction 明确限定 claim scope 为 within known model-strategy configurations\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-C2\n  summary: 14B 规模衰减 EDD₇₀=0 对论文立论的根本威胁——Discussion 传达不足\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N2: 14B EDD=0 被 self-reference confound 污染\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续追踪\"}\n  - {round: 19, reviewers: [1, 2], note: \"R2-N3 Critical, R1 AGREE with precision: EDD₇₀=0 ≠ 无信号 (self-ref 50.8%=2×chance)，但序数结构已坍塌。R2 REBUT R1-W4 (14B confound)：self-ref 数据已足够分离 scale vs ref-model (50.8% vs 44.1% = ~7pp gap << 30+pp 与 1.4B 的差距)。共识：1.4B 成功是 proof-of-concept，Introduction 和 contribution list 需显式声明规模限制。\"}\n  action_items:\n  - {round: 19, action: \"Contribution list 增加规模限制声明；Discussion 分析信号消失机制\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-C3\n  summary: 参考模型依赖限制部署可行性——12/19 特征绑定 Pythia-1.4B，正文讨论不足\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R18-W5: 参考模型依赖性未充分讨论为部署限制\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-N1 Critical, R2-W3 Warning→AGREE。R1 要求 reference-agnostic baseline。R2 认为 proof-of-concept 可接受但同意正文讨论不足。R2 精确区分了两个 'gap' 数字：14B self-vs-cross ~7pp (Section 5.4) vs 1.5B cross-architecture -11.3pp (Table 18)。\"}\n  action_items:\n  - {round: 19, action: \"正文增加参考模型依赖的系统讨论（部署含义、选择策略、multi-reference 可能性）\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-C4\n  summary: 多重比较未校正但做实质性判断——Binoculars p>0.05 误读为等价性\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W2: 多重比较未校正\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 atlas.tex EDD bootstrap 已加 Bonferroni 校正\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-N2 Critical, R2 部分 AGREE (not Critical)。R1: 非显著性≠等价性需 TOST。R2: 核心结论不依赖这些 p 值，但 'Statistical Fingerprints' 为卖点的论文统计推断应严谨。R2 补充：Section 4.3 已做部分 Bonferroni 但未统一应用。Director 判定：降为 Warning（核心结论不依赖），但需修复 Binoculars 等价性声明。\"}\n  action_items:\n  - {round: 19, action: \"Section 5.1 Binoculars 对比改为正确的统计解读（非显著≠等价），或补充 TOST\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 19 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R19-W1\n  summary: 方法论创新不足——标准特征+标准分类器，不满足 Conference 门槛\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N5\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续追踪\"}\n  - {round: 19, reviewers: [1, 2], note: \"R2-W1 Warning, R1 部分 REBUT (EMNLP accepts empirical)。分歧：R1 认为不阻拦，R2 认为限制 Conference excitement。共识：未深入分析统计特征优于 PLM 表征 20pp 的原因——这个 'why' 有价值。\"}\n  action_items:\n  - {round: 19, action: \"Discussion 增加一段：为何浅层统计特征优于深度 PLM 表征\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W2\n  summary: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N1: accumulation 场景无系统实验\"}\n  - {round: 18, reviewers: [1, 2], note: \"3-cell mix25 accumulation EDD 完成\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-N3 Critical→R2 认为 Should-Fix。R1: GPT-2 XL 50% mixing boundary failure (AUC=0.695)。R2: proof-of-concept 首篇从受控设定起步合理。共识：问题存在但 severity 为 Warning。\"}\n  action_items:\n  - {round: 19, action: \"Discussion 明确承认当前基准是 idealized conditions 下的 proof-of-concept\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W3\n  summary: Neural baseline 比较信息不对等——RF 有 reference model oracle，PLM 仅看原文\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W3: Neural baselines 仅测试 ≤125M backbone\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-W1 Warning, R2 AGREE。信息输入不对等：RF 用 token-level perplexity，PLM 仅获得原文 [CLS]。当前对比更像 'PLM 不能从原文推断困惑度分布'（不意外）。应给 PLM 同等 perplexity 信息通道。\"}\n  action_items:\n  - {round: 19, action: \"Discussion 或 Limitations 明确标注信息不对等；或尝试给 PLM 喂参考模型 perplexity 序列\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W4\n  summary: BOS seeding artifact——与 prompted generation 差 13.8pp，深度信号可能部分为 artifact\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R16-W7: BOS-seeded generation 限制生态效度\"}\n  - {round: 17, reviewers: [1, 2], note: \"R17 写作修复已加强 BOS caveat\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-W5 Warning, R2 AGREE。13.8pp gap 暗示深度信号部分来自 BOS seeding 特异性 artifact。Appendix B.16 标记为 Inconclusive 但差距值得在正文讨论。\"}\n  action_items:\n  - {round: 19, action: \"正文或 Limitations 更显著地讨论 BOS vs prompted gap 的含义\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W5\n  summary: 序数分类框架与实际方法脱节——强调 ordinal 但主管线不利用序数结构\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R2-W2 Warning, R1 AGREE。论文 Section 3.1 强调 ordinal classification 但主管线用标准 RF。CORAL 仅有边际改善 (Appendix B.25) 但未在正文讨论原因。叙事断裂：如果序数结构是核心特征，为什么主方法不利用它？\"}\n  action_items:\n  - {round: 19, action: \"正文简要讨论序数分类方法在此任务中边际改善的原因（如 K=4 序数约束收益有限）\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W6\n  summary: 单 LoRA seed 主实验，2-seed replication 不足以估计方差分布\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W1\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-W6 Warning, R2 AGREE 程度较轻。2 seeds 方向一致 (+0.14 to +3.17pp) 但不足以估计方差分布。R2: 考虑到 180K 重新生成的计算成本，2-seed 作为 sanity check 可接受。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 19 — MINOR (Info)\n# ============================================================\n\n- id: R19-M1\n  summary: Abstract 信息密度过高，14B 结果的 cross-ref vs self-ref 条件混用可能误导\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R2-M1 + R2-N1。R2 报告 Abstract '≈19%' 与 Section 5.4 的 44.1% 矛盾——Director 核查发现 Abstract 实际写 '~44%'，R2 误读。但 Abstract 中 cross-reference EDD₇₀=2 与 self-reference EDD₇₀=0 混用仍需澄清条件。R1 也指出 EDD₇₅=2 vs EDD₇₅=0 需要澄清。\"}\n  action_items:\n  - {round: 19, action: \"Abstract 14B 结果拆分为独立句子，明确标注 cross-reference 条件\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M2\n  summary: \"Statistical Fingerprints\" 术语选择——弱迁移结果下 \"fingerprint\" 有 framing risk\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R2-M2, R1 轻微 REBUT（forensics 文献常用）。但鉴于跨策略 45.9%，'fingerprint' 暗示的唯一性和可迁移性与实证不符。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M3\n  summary: Figure 2/3 字号偏小，打印可读性受限\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R2-M3, R1 AGREE。视觉审查确认 heatmap cell 内 ~6pt，Figure 3 axis labels 约正文 60%。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M4\n  summary: Section 3.5 \"Theoretical Motivation\" 内容主要为经验观察\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [2], note: \"R2-M5: 'Empirical Motivation' 可能更准确。R1 未反驳。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M5\n  summary: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺理论论证\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R1-W2, R2 AGREE 程度较轻。EDD 是操作性指标，多阈值 sensitivity 已报告，通过增加一段讨论即可解决。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M6\n  summary: Appendix B.20 Qwen2.5-7B Self-Reference 有 PLACEHOLDER 未填充\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: \"Director 在阅读论文时发现 Section B.20 (line 643-645) 有 %% PLACEHOLDER 注释未填充。提交前必须补全或删除。\"}\n  action_items:\n  - {round: 19, action: \"B.20 PLACEHOLDER 必须在提交前补全（qwen25_7b_selfref_001 实验结果）或删除整个 subsection\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M7\n  summary: Missing references——Lakens (2017) TOST、Gutiérrez (2016) ordinal regression\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"两人共同推荐。R2 另推荐 FineWeb/DCLM（R1 认为间接关联）。R2 纠正 R1：Alemohammad (2024) 已引用。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (from Round 16-18, status carried forward)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值——accumulation 场景无系统实验\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 列为 N1 critical, R2 原列 W2 后升级为 critical\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识 critical\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-W2 下追踪，severity 降为 warning（两人共识 proof-of-concept 合理）\"}\n  action_items:\n  - {round: 18, action: \"3-cell mix25 accumulation EDD 计算完成\", assigned_to: research_director, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染——无法分离规模效应 vs 参考模型切换\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 首次识别 confound\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识 critical\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 R2 REBUT R1-W4：self-ref 50.8% 已足够分离（scale 30+pp >> ref-model ~7pp）。R19 继续在 R19-C2 下追踪。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%——策略未知时方法基本失效，与应用场景矛盾\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N3 + R2-N3 完全共识\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续追踪\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-C1 下追踪。R1 纠正 R2 引用的 cross-model 46.7%（应为 66.4%/55.4%）。\"}\n  action_items:\n  - {round: 17, action: \"Abstract 已加 within-strategy scope 声明\", assigned_to: research_director, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足——标准特征+标准分类器，不满足 Conference 门槛\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2-N1 critical; R1 REBUT 但同意 Conference 不足\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人均认同方法论零创新\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-W1 下追踪，severity 降为 warning（R1 部分 REBUT：EMNLP accepts empirical studies）\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W1, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"降为 warning\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-W6 下追踪\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W2, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"atlas.tex EDD bootstrap 已加 Bonferroni\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-C4 下追踪\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 ≤125M backbone\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W3, R2 部分 REBUT\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-W3 下追踪（信息不对等角度）\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%, p>0.05），削弱独特价值\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"Limitations 已加计算效率对比\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 未作为独立 issue 提出，但 R19-C4 中涉及 Binoculars p>0.05 误读\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R1-W5 warning，R2 AGREE\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-C3 下追踪，severity 升为 critical\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著（p>0.4）但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5(curation) + R2-W5 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"§6 curation claim 已弱化\"}\n  - {round: 19, reviewers: [], note: \"R19 未作为独立 issue 提出\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 (estimation vs classification)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 minor points\"}\n  - {round: 18, reviewers: [1, 2], note: \"§3.1 已加术语声明\"}\n  - {round: 19, reviewers: [], note: \"R19 未作为独立 issue 提出，Section 3.1 声明已存在\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N4 critical → R2 同意 family-level 可靠\"}\n  - {round: 18, reviewers: [1], note: \"R1-M1 提及 VIF>10\"}\n  - {round: 19, reviewers: [], note: \"R19 未作为独立 issue 提出。Section 4.2 已有 cautious interpretation caveat + CPI 分析 (Appendix B.3)。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R2-M1，R1 AGREE\"}\n  - {round: 19, reviewers: [], note: \"R19 未提及。Section 3.2 已加 'd0 samples are drawn from a shared Wikipedia seed corpus across all cells'。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: CI 报告不一致——Table 2 有 CI 但部分表格没有\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1], note: \"R1 minor point\"}\n  - {round: 18, reviewers: [1, 2], note: \"R2-M2，R1 AGREE\"}\n  - {round: 19, reviewers: [], note: \"R19 未提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"多篇缺失引用\"}\n  - {round: 18, reviewers: [1, 2], note: \"已加 Carlini et al. (2021)\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 推荐: Lakens (2017) TOST, Gutiérrez (2016) ordinal regression。R2 推荐 FineWeb/DCLM（R1 认为间接）。R2 纠正 R1：Alemohammad (2024) 已引用。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL RESOLVED/WONT_FIX (carried forward unchanged)\n# ============================================================\n\n- id: R16-N1\n  summary: 14B 结果 (EDD=0) 从根本上削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"Abstract 加 scope 限定; §6 新增 scale dependence 段落。R17 confound → R17-N2\"\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足——标准特征+标准分类器\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"§1 贡献重组。R17 novelty 批评结构性 → R17-N5\"\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"§5.3 reframed + R17 scope 限定\"\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"§6 新增 'From ceiling to floor' 段\"\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia †)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Reviewer 确认 † + ref-model ablation 67-79% 已充分\"\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: \"§4.2 group-level ablation + R17 弱化 individual ranking\"\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"Abstract ~6 数字, 3 findings 结构\"\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Abstract 和 §1 以 d1-d3 balanced accuracy 领头\"\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Sensitivity analysis 已覆盖\"\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R19 re-raised as R19-W4，侧重 -13.8pp gap 的 artifact 含义\"}\n  resolution: \"§3.2 BOS caveat 加强。R19 re-raised → R19-W4\"\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: \"Thresholding 方案已覆盖\"\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"§6 扩展为 4 段\"\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"§6 含 depth-scored data curation scenario\"\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: \"Minor visual, acceptable\"\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: \"Pipeline 太简单不需要图\"\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: \"主文 8 页 ✓\"\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"Structural constraint\"\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致 depth estimation / classification\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"已加入\"\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Classifier convergence evidence sufficient\"\n  resolution_round: 16\n\n- id: R18-M3\n  summary: §3.5 Theoretical Grounding 标题过大\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"已改为 Theoretical Motivation\"\n  resolution_round: 18\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens，短文本推广未讨论\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: \"R19 未提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: \"R19 未提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"项目收尾不再跑新实验\"\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-C4 下追踪\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§2 已引用\"\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: \"编译验证通过，主文 pp.1-8\"\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"用户指示不再跑新实验\"\n  resolution_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n# ============================================================\n# ROUND 19 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R19-C1\n  summary: 泛化性 claim 与证据系统性失配——跨策略 45.9%、14B EDD=0 与 \"fingerprints\" 通用性暗示矛盾\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N3: 跨策略 d1-d3 仅 45.9%\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续追踪，Abstract 已加 within-strategy scope 声明\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1 AGREE R2-N2。两人共识：Abstract 'consistent in direction' 将方向一致性包装为正面结论，但 45.9% 分类器不可用。标题 'Statistical Fingerprints' 暗示可迁移性与实证矛盾。Two-stage 恢复到 70.5% 但仍远低于 within-cell。R1 纠正 R2 引用的 '46.7%' 数字（实为 cross-τ 而非 cross-model）。\"}\n  action_items:\n  - {round: 19, action: \"Abstract/Introduction 明确限定 claim scope 为 within known model-strategy configurations\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-C2\n  summary: 14B 规模衰减 EDD₇₀=0 对论文立论的根本威胁——Discussion 传达不足\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N2: 14B EDD=0 被 self-reference confound 污染\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续追踪\"}\n  - {round: 19, reviewers: [1, 2], note: \"R2-N3 Critical, R1 AGREE with precision: EDD₇₀=0 ≠ 无信号 (self-ref 50.8%=2×chance)，但序数结构已坍塌。R2 REBUT R1-W4 (14B confound)：self-ref 数据已足够分离 scale vs ref-model (50.8% vs 44.1% = ~7pp gap << 30+pp 与 1.4B 的差距)。共识：1.4B 成功是 proof-of-concept，Introduction 和 contribution list 需显式声明规模限制。\"}\n  action_items:\n  - {round: 19, action: \"Contribution list 增加规模限制声明；Discussion 分析信号消失机制\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-C3\n  summary: 参考模型依赖限制部署可行性——12/19 特征绑定 Pythia-1.4B，正文讨论不足\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R18-W5: 参考模型依赖性未充分讨论为部署限制\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-N1 Critical, R2-W3 Warning→AGREE。R1 要求 reference-agnostic baseline。R2 认为 proof-of-concept 可接受但同意正文讨论不足。R2 精确区分了两个 'gap' 数字：14B self-vs-cross ~7pp (Section 5.4) vs 1.5B cross-architecture -11.3pp (Table 18)。\"}\n  action_items:\n  - {round: 19, action: \"正文增加参考模型依赖的系统讨论（部署含义、选择策略、multi-reference 可能性）\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-C4\n  summary: 多重比较未校正但做实质性判断——Binoculars p>0.05 误读为等价性\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W2: 多重比较未校正\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 atlas.tex EDD bootstrap 已加 Bonferroni 校正\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-N2 Critical, R2 部分 AGREE (not Critical)。R1: 非显著性≠等价性需 TOST。R2: 核心结论不依赖这些 p 值，但 'Statistical Fingerprints' 为卖点的论文统计推断应严谨。R2 补充：Section 4.3 已做部分 Bonferroni 但未统一应用。Director 判定：降为 Warning（核心结论不依赖），但需修复 Binoculars 等价性声明。\"}\n  action_items:\n  - {round: 19, action: \"Section 5.1 Binoculars 对比改为正确的统计解读（非显著≠等价），或补充 TOST\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 19 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R19-W1\n  summary: 方法论创新不足——标准特征+标准分类器，不满足 Conference 门槛\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N5\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续追踪\"}\n  - {round: 19, reviewers: [1, 2], note: \"R2-W1 Warning, R1 部分 REBUT (EMNLP accepts empirical)。分歧：R1 认为不阻拦，R2 认为限制 Conference excitement。共识：未深入分析统计特征优于 PLM 表征 20pp 的原因——这个 'why' 有价值。\"}\n  action_items:\n  - {round: 19, action: \"Discussion 增加一段：为何浅层统计特征优于深度 PLM 表征\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W2\n  summary: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-N1: accumulation 场景无系统实验\"}\n  - {round: 18, reviewers: [1, 2], note: \"3-cell mix25 accumulation EDD 完成\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-N3 Critical→R2 认为 Should-Fix。R1: GPT-2 XL 50% mixing boundary failure (AUC=0.695)。R2: proof-of-concept 首篇从受控设定起步合理。共识：问题存在但 severity 为 Warning。\"}\n  action_items:\n  - {round: 19, action: \"Discussion 明确承认当前基准是 idealized conditions 下的 proof-of-concept\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W3\n  summary: Neural baseline 比较信息不对等——RF 有 reference model oracle，PLM 仅看原文\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W3: Neural baselines 仅测试 ≤125M backbone\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-W1 Warning, R2 AGREE。信息输入不对等：RF 用 token-level perplexity，PLM 仅获得原文 [CLS]。当前对比更像 'PLM 不能从原文推断困惑度分布'（不意外）。应给 PLM 同等 perplexity 信息通道。\"}\n  action_items:\n  - {round: 19, action: \"Discussion 或 Limitations 明确标注信息不对等；或尝试给 PLM 喂参考模型 perplexity 序列\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W4\n  summary: BOS seeding artifact——与 prompted generation 差 13.8pp，深度信号可能部分为 artifact\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: \"R16-W7: BOS-seeded generation 限制生态效度\"}\n  - {round: 17, reviewers: [1, 2], note: \"R17 写作修复已加强 BOS caveat\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-W5 Warning, R2 AGREE。13.8pp gap 暗示深度信号部分来自 BOS seeding 特异性 artifact。Appendix B.16 标记为 Inconclusive 但差距值得在正文讨论。\"}\n  action_items:\n  - {round: 19, action: \"正文或 Limitations 更显著地讨论 BOS vs prompted gap 的含义\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W5\n  summary: 序数分类框架与实际方法脱节——强调 ordinal 但主管线不利用序数结构\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R2-W2 Warning, R1 AGREE。论文 Section 3.1 强调 ordinal classification 但主管线用标准 RF。CORAL 仅有边际改善 (Appendix B.25) 但未在正文讨论原因。叙事断裂：如果序数结构是核心特征，为什么主方法不利用它？\"}\n  action_items:\n  - {round: 19, action: \"正文简要讨论序数分类方法在此任务中边际改善的原因（如 K=4 序数约束收益有限）\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W6\n  summary: 单 LoRA seed 主实验，2-seed replication 不足以估计方差分布\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R17-W1\"}\n  - {round: 19, reviewers: [1, 2], note: \"R1-W6 Warning, R2 AGREE 程度较轻。2 seeds 方向一致 (+0.14 to +3.17pp) 但不足以估计方差分布。R2: 考虑到 180K 重新生成的计算成本，2-seed 作为 sanity check 可接受。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 19 — MINOR (Info)\n# ============================================================\n\n- id: R19-M1\n  summary: Abstract 信息密度过高，14B 结果的 cross-ref vs self-ref 条件混用可能误导\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R2-M1 + R2-N1。R2 报告 Abstract '≈19%' 与 Section 5.4 的 44.1% 矛盾——Director 核查发现 Abstract 实际写 '~44%'，R2 误读。但 Abstract 中 cross-reference EDD₇₀=2 与 self-reference EDD₇₀=0 混用仍需澄清条件。R1 也指出 EDD₇₅=2 vs EDD₇₅=0 需要澄清。\"}\n  action_items:\n  - {round: 19, action: \"Abstract 14B 结果拆分为独立句子，明确标注 cross-reference 条件\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M2\n  summary: \"Statistical Fingerprints\" 术语选择——弱迁移结果下 \"fingerprint\" 有 framing risk\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R2-M2, R1 轻微 REBUT（forensics 文献常用）。但鉴于跨策略 45.9%，'fingerprint' 暗示的唯一性和可迁移性与实证不符。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M3\n  summary: Figure 2/3 字号偏小，打印可读性受限\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R2-M3, R1 AGREE。视觉审查确认 heatmap cell 内 ~6pt，Figure 3 axis labels 约正文 60%。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M4\n  summary: Section 3.5 \"Theoretical Motivation\" 内容主要为经验观察\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [2], note: \"R2-M5: 'Empirical Motivation' 可能更准确。R1 未反驳。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M5\n  summary: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺理论论证\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R1-W2, R2 AGREE 程度较轻。EDD 是操作性指标，多阈值 sensitivity 已报告，通过增加一段讨论即可解决。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M6\n  summary: Appendix B.20 Qwen2.5-7B Self-Reference 有 PLACEHOLDER 未填充\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: \"Director 在阅读论文时发现 Section B.20 (line 643-645) 有 %% PLACEHOLDER 注释未填充。提交前必须补全或删除。\"}\n  action_items:\n  - {round: 19, action: \"B.20 PLACEHOLDER 必须在提交前补全（qwen25_7b_selfref_001 实验结果）或删除整个 subsection\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-M7\n  summary: Missing references——Lakens (2017) TOST、Gutiérrez (2016) ordinal regression\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"两人共同推荐。R2 另推荐 FineWeb/DCLM（R1 认为间接关联）。R2 纠正 R1：Alemohammad (2024) 已引用。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (from Round 16-18, status carried forward)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值——accumulation 场景无系统实验\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 列为 N1 critical, R2 原列 W2 后升级为 critical\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识 critical\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-W2 下追踪，severity 降为 warning（两人共识 proof-of-concept 合理）\"}\n  action_items:\n  - {round: 18, action: \"3-cell mix25 accumulation EDD 计算完成\", assigned_to: research_director, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染——无法分离规模效应 vs 参考模型切换\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1 首次识别 confound\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人再次共识 critical\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 R2 REBUT R1-W4：self-ref 50.8% 已足够分离（scale 30+pp >> ref-model ~7pp）。R19 继续在 R19-C2 下追踪。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%——策略未知时方法基本失效，与应用场景矛盾\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N3 + R2-N3 完全共识\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 继续追踪\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-C1 下追踪。R1 纠正 R2 引用的 cross-model 46.7%（应为 66.4%/55.4%）。\"}\n  action_items:\n  - {round: 17, action: \"Abstract 已加 within-strategy scope 声明\", assigned_to: research_director, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足——标准特征+标准分类器，不满足 Conference 门槛\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R2-N1 critical; R1 REBUT 但同意 Conference 不足\"}\n  - {round: 18, reviewers: [1, 2], note: \"R18 两人均认同方法论零创新\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-W1 下追踪，severity 降为 warning（R1 部分 REBUT：EMNLP accepts empirical studies）\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W1, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"降为 warning\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-W6 下追踪\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W2, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"atlas.tex EDD bootstrap 已加 Bonferroni\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-C4 下追踪\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 ≤125M backbone\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W3, R2 部分 REBUT\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-W3 下追踪（信息不对等角度）\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%, p>0.05），削弱独特价值\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5, R2 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"Limitations 已加计算效率对比\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 未作为独立 issue 提出，但 R19-C4 中涉及 Binoculars p>0.05 误读\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R1-W5 warning，R2 AGREE\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-C3 下追踪，severity 升为 critical\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著（p>0.4）但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-W5(curation) + R2-W5 AGREE\"}\n  - {round: 18, reviewers: [1, 2], note: \"§6 curation claim 已弱化\"}\n  - {round: 19, reviewers: [], note: \"R19 未作为独立 issue 提出\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 (estimation vs classification)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [2], note: \"R2 minor points\"}\n  - {round: 18, reviewers: [1, 2], note: \"§3.1 已加术语声明\"}\n  - {round: 19, reviewers: [], note: \"R19 未作为独立 issue 提出，Section 3.1 声明已存在\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"R1-N4 critical → R2 同意 family-level 可靠\"}\n  - {round: 18, reviewers: [1], note: \"R1-M1 提及 VIF>10\"}\n  - {round: 19, reviewers: [], note: \"R19 未作为独立 issue 提出。Section 4.2 已有 cautious interpretation caveat + CPI 分析 (Appendix B.3)。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: \"R2-M1，R1 AGREE\"}\n  - {round: 19, reviewers: [], note: \"R19 未提及。Section 3.2 已加 'd0 samples are drawn from a shared Wikipedia seed corpus across all cells'。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: CI 报告不一致——Table 2 有 CI 但部分表格没有\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1], note: \"R1 minor point\"}\n  - {round: 18, reviewers: [1, 2], note: \"R2-M2，R1 AGREE\"}\n  - {round: 19, reviewers: [], note: \"R19 未提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: \"多篇缺失引用\"}\n  - {round: 18, reviewers: [1, 2], note: \"已加 Carlini et al. (2021)\"}\n  - {round: 19, reviewers: [1, 2], note: \"R19 推荐: Lakens (2017) TOST, Gutiérrez (2016) ordinal regression。R2 推荐 FineWeb/DCLM（R1 认为间接）。R2 纠正 R1：Alemohammad (2024) 已引用。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL RESOLVED/WONT_FIX (carried forward unchanged)\n# ============================================================\n\n- id: R16-N1\n  summary: 14B 结果 (EDD=0) 从根本上削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"Abstract 加 scope 限定; §6 新增 scale dependence 段落。R17 confound → R17-N2\"\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足——标准特征+标准分类器\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"§1 贡献重组。R17 novelty 批评结构性 → R17-N5\"\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"§5.3 reframed + R17 scope 限定\"\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"§6 新增 'From ceiling to floor' 段\"\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia †)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Reviewer 确认 † + ref-model ablation 67-79% 已充分\"\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: \"§4.2 group-level ablation + R17 弱化 individual ranking\"\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"Abstract ~6 数字, 3 findings 结构\"\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: \"Abstract 和 §1 以 d1-d3 balanced accuracy 领头\"\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"Sensitivity analysis 已覆盖\"\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R19 re-raised as R19-W4，侧重 -13.8pp gap 的 artifact 含义\"}\n  resolution: \"§3.2 BOS caveat 加强。R19 re-raised → R19-W4\"\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: \"Thresholding 方案已覆盖\"\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"§6 扩展为 4 段\"\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"§6 含 depth-scored data curation scenario\"\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: \"Minor visual, acceptable\"\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: \"Pipeline 太简单不需要图\"\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: \"主文 8 页 ✓\"\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"Structural constraint\"\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致 depth estimation / classification\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"已加入\"\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: \"Classifier convergence evidence sufficient\"\n  resolution_round: 16\n\n- id: R18-M3\n  summary: §3.5 Theoretical Grounding 标题过大\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"已改为 Theoretical Motivation\"\n  resolution_round: 18\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens，短文本推广未讨论\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: \"R19 未提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: \"R19 未提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"项目收尾不再跑新实验\"\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: \"R19 继续在 R19-C4 下追踪\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"§2 已引用\"\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: \"编译验证通过，主文 pp.1-8\"\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"用户指示不再跑新实验\"\n  resolution_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1765 · 2026-05-22T23:15:32.672113+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"issues_yaml is not valid YAML: while parsing a block mapping\\n  in \\\"&lt;unicode string>\\\", line 182, column 3:\\n    - id: R19-M2\\n      ^\\nexpected &lt;block end>, but found '&lt;scalar>'\\n  in \\\"&lt;unicode string>\\\", line 183, column 39:\\n     ... ary: \\\"Statistical Fingerprints\\\" 术语选择——弱迁移结果下 \\\"fingerprint\\\" 有 fra ... \\n                                         ^\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 69
}
```

</details>

---


### Tool call

_source line 1766 · 2026-05-22T23:18:12.674529+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n# ============================================================\n# ROUND 19 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R19-C1\n  summary: 泛化性 claim 与证据系统性失配——跨策略 45.9%、14B EDD=0 与 fingerprints 通用性暗示矛盾\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N3: 跨策略 d1-d3 仅 45.9%'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪，Abstract 已加 within-strategy scope 声明'}\n  - {round: 19, reviewers: [1, 2], note: 'R1 AGREE R2-N2。两人共识：Abstract consistent in direction 将方向一致性包装为正面结论，但 45.9% 分类器不可用。标题 Statistical Fingerprints 暗示可迁移性与实证矛盾。Two-stage 恢复到 70.5% 但仍远低于 within-cell。R1 纠正 R2 引用的 46.7% 数字（实为 cross-tau 而非 cross-model）。'}\n  action_items:\n  - {round: 19, action: 'Abstract/Introduction 明确限定 claim scope 为 within known model-strategy configurations', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C2\n  summary: 14B 规模衰减 EDD_70=0 对论文立论的根本威胁——Discussion 传达不足\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N2: 14B EDD=0 被 self-reference confound 污染'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪'}\n  - {round: 19, reviewers: [1, 2], note: 'R2-N3 Critical, R1 AGREE with precision: EDD_70=0 不等于无信号 (self-ref 50.8%=2x chance)，但序数结构已坍塌。R2 REBUT R1-W4 (14B confound)：self-ref 数据已足够分离 scale vs ref-model (50.8% vs 44.1% = ~7pp gap 远小于 30+pp 与 1.4B 的差距)。共识：1.4B 成功是 proof-of-concept，contribution list 需显式声明规模限制。'}\n  action_items:\n  - {round: 19, action: 'Contribution list 增加规模限制声明；Discussion 分析信号消失机制', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C3\n  summary: 参考模型依赖限制部署可行性——12/19 特征绑定 Pythia-1.4B，正文讨论不足\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: 'R18-W5: 参考模型依赖性未充分讨论为部署限制'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N1 Critical, R2-W3 Warning 后 AGREE。R1 要求 reference-agnostic baseline。R2 认为 proof-of-concept 可接受但同意正文讨论不足。R2 精确区分了两个 gap 数字：14B self-vs-cross ~7pp (Section 5.4) vs 1.5B cross-architecture -11.3pp (Table 18)。'}\n  action_items:\n  - {round: 19, action: '正文增加参考模型依赖的系统讨论（部署含义、选择策略、multi-reference 可能性）', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C4\n  summary: 多重比较未校正但做实质性判断——Binoculars p>0.05 误读为等价性\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W2: 多重比较未校正'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 atlas.tex EDD bootstrap 已加 Bonferroni'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N2 Critical, R2 部分 AGREE (not Critical)。R1: 非显著性不等于等价性需 TOST。R2: 核心结论不依赖这些 p 值，但统计论文的统计推断应严谨。R2 补充：Section 4.3 已做部分 Bonferroni 但未统一应用。Director 判定：降为 Warning。'}\n  action_items:\n  - {round: 19, action: 'Section 5.1 Binoculars 对比改为正确的统计解读（非显著不等于等价），或补充 TOST', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# ROUND 19 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R19-W1\n  summary: 方法论创新不足——标准特征+标准分类器，未分析统计特征优于PLM的原因\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N5'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪'}\n  - {round: 19, reviewers: [1, 2], note: 'R2-W1 Warning, R1 部分 REBUT (EMNLP accepts empirical)。分歧：R1 不阻拦，R2 限制 Conference excitement。共识：未深入分析统计特征优于 PLM 表征 20pp 的原因。'}\n  action_items:\n  - {round: 19, action: 'Discussion 增加一段：为何浅层统计特征优于深度 PLM 表征', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W2\n  summary: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N1: accumulation 场景无系统实验'}\n  - {round: 18, reviewers: [1, 2], note: '3-cell mix25 accumulation EDD 完成'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N3 Critical 后 R2 认为 Should-Fix。R1: GPT-2 XL 50% mixing boundary failure (AUC=0.695)。R2: proof-of-concept 首篇从受控设定起步合理。共识：问题存在但 severity 为 Warning。'}\n  action_items:\n  - {round: 19, action: 'Discussion 明确承认当前基准是 idealized conditions 下的 proof-of-concept', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W3\n  summary: Neural baseline 比较信息不对等——RF 有 reference model oracle，PLM 仅看原文\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W3: Neural baselines 仅测试 <=125M backbone'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W1 Warning, R2 AGREE。信息输入不对等：RF 用 token-level perplexity，PLM 仅获得原文 CLS。当前对比更像 PLM 不能从原文推断困惑度分布（不意外）。'}\n  action_items:\n  - {round: 19, action: 'Discussion 或 Limitations 明确标注信息不对等', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W4\n  summary: BOS seeding artifact——与 prompted generation 差 13.8pp，深度信号可能部分为 artifact\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: 'R16-W7: BOS-seeded generation 限制生态效度'}\n  - {round: 17, reviewers: [1, 2], note: 'R17 写作修复已加强 BOS caveat'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W5 Warning, R2 AGREE。13.8pp gap 暗示深度信号部分来自 BOS seeding 特异性。'}\n  action_items:\n  - {round: 19, action: '正文或 Limitations 更显著地讨论 BOS vs prompted gap 的含义', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W5\n  summary: 序数分类框架与实际方法脱节——强调 ordinal 但主管线不利用序数结构\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-W2 Warning, R1 AGREE。论文 Section 3.1 强调 ordinal classification 但主管线用标准 RF。CORAL 仅有边际改善 (Appendix B.25) 但未在正文讨论原因。'}\n  action_items:\n  - {round: 19, action: '正文简要讨论序数分类方法在此任务中边际改善的原因', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W6\n  summary: 单 LoRA seed 主实验，2-seed replication 不足以估计方差分布\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W1'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W6 Warning, R2 AGREE 程度较轻。2 seeds 方向一致但不足以估计方差分布。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# ROUND 19 — MINOR (Info)\n# ============================================================\n\n- id: R19-M1\n  summary: Abstract 信息密度过高，14B 结果的 cross-ref vs self-ref 条件混用可能误导\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2 报告 Abstract 约19% 与 Section 5.4 的 44.1% 矛盾——Director 核查发现 Abstract 实际写 约44%，R2 误读。但 Abstract 中 cross-reference EDD_70=2 与 self-reference EDD_70=0 混用仍需澄清条件。'}\n  action_items:\n  - {round: 19, action: 'Abstract 14B 结果拆分为独立句子，明确标注 cross-reference 条件', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M2\n  summary: 标题 Statistical Fingerprints 术语选择——弱迁移结果下 fingerprint 有 framing risk\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-M2, R1 轻微 REBUT（forensics 文献常用）。但鉴于跨策略 45.9%，fingerprint 暗示的唯一性和可迁移性与实证不符。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M3\n  summary: Figure 2/3 字号偏小，打印可读性受限\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-M3, R1 AGREE。视觉审查确认 heatmap cell 内约6pt。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M4\n  summary: Section 3.5 Theoretical Motivation 内容主要为经验观察\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [2], note: 'R2-M5: Empirical Motivation 可能更准确。R1 未反驳。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M5\n  summary: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺理论论证\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R1-W2, R2 AGREE 程度较轻。EDD 是操作性指标，多阈值 sensitivity 已报告。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M6\n  summary: Appendix B.20 Qwen2.5-7B Self-Reference 有 PLACEHOLDER 未填充\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'Director 在阅读论文时发现 Section B.20 有 PLACEHOLDER 注释未填充。提交前必须补全或删除。'}\n  action_items:\n  - {round: 19, action: 'B.20 PLACEHOLDER 必须在提交前补全或删除整个 subsection', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M7\n  summary: Missing references——Lakens (2017) TOST、Gutierrez (2016) ordinal regression\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: '两人共同推荐。R2 另推荐 FineWeb/DCLM（R1 认为间接关联）。R2 纠正 R1：Alemohammad (2024) 已引用。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (carried forward)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W2 下追踪，severity 降为 warning'}\n  action_items:\n  - {round: 18, action: '3-cell mix25 accumulation EDD 计算完成', assigned_to: research_director, status: done}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 R2 REBUT R1-W4：self-ref 50.8% 已足够分离。继续在 R19-C2 下追踪。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C1 下追踪。R1 纠正 R2 引用的 cross-model 46.7%。'}\n  action_items:\n  - {round: 17, action: 'Abstract 已加 within-strategy scope 声明', assigned_to: research_director, status: done}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W1 下追踪，severity 降为 warning'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W6 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C4 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 <=125M backbone\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W3 下追踪（信息不对等角度）'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%），削弱独特价值\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出，但 R19-C4 中涉及 Binoculars p>0.05 误读'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C3 下追踪，severity 升为 critical'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 (estimation vs classification)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出，Section 3.1 声明已存在'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出。Section 4.2 已有 caveat + CPI 分析。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及。Section 3.2 已加声明。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M2\n  summary: CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 推荐 Lakens (2017) TOST, Gutierrez (2016) ordinal regression。R2 另推荐 FineWeb/DCLM。R2 纠正 R1 Alemohammad (2024) 已引用。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n# Historical resolved/wont_fix (abbreviated, unchanged)\n- id: R16-N1\n  summary: 14B 结果削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Abstract 加 scope 限定; Section 6 新增 scale dependence'\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 1 贡献重组'\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 5.3 reframed'\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 6 新增段落'\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia dagger)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: 'Reviewer 确认 dagger + ref-model ablation 67-79% 已充分'\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: 'Section 4.2 group-level ablation'\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Abstract 精简'\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: 'd1-d3 balanced accuracy 领头'\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: 'Sensitivity analysis 已覆盖'\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 'Section 3.2 BOS caveat 加强。R19 re-raised as R19-W4'\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: 'Thresholding 方案已覆盖'\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 6 扩展'\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 'Section 6 含 curation scenario'\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: 'Acceptable for review'\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 'Pipeline 太简单不需要图'\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: '主文 8 页'\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: 'Structural constraint'\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: ''\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: '已加入'\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 'Classifier convergence evidence sufficient'\n  resolution_round: 16\n\n- id: R18-M3\n  summary: Section 3.5 标题过大\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: '已改为 Theoretical Motivation'\n  resolution_round: 18\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: '项目收尾不再跑新实验'\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C4 下追踪'}\n  resolution: ''\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: 'Section 2 已引用'\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: '编译验证通过'\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: '用户指示不再跑新实验'\n  resolution_round: 14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n# ============================================================\n# ROUND 19 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R19-C1\n  summary: 泛化性 claim 与证据系统性失配——跨策略 45.9%、14B EDD=0 与 fingerprints 通用性暗示矛盾\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N3: 跨策略 d1-d3 仅 45.9%'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪，Abstract 已加 within-strategy scope 声明'}\n  - {round: 19, reviewers: [1, 2], note: 'R1 AGREE R2-N2。两人共识：Abstract consistent in direction 将方向一致性包装为正面结论，但 45.9% 分类器不可用。标题 Statistical Fingerprints 暗示可迁移性与实证矛盾。Two-stage 恢复到 70.5% 但仍远低于 within-cell。R1 纠正 R2 引用的 46.7% 数字（实为 cross-tau 而非 cross-model）。'}\n  action_items:\n  - {round: 19, action: 'Abstract/Introduction 明确限定 claim scope 为 within known model-strategy configurations', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C2\n  summary: 14B 规模衰减 EDD_70=0 对论文立论的根本威胁——Discussion 传达不足\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N2: 14B EDD=0 被 self-reference confound 污染'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪'}\n  - {round: 19, reviewers: [1, 2], note: 'R2-N3 Critical, R1 AGREE with precision: EDD_70=0 不等于无信号 (self-ref 50.8%=2x chance)，但序数结构已坍塌。R2 REBUT R1-W4 (14B confound)：self-ref 数据已足够分离 scale vs ref-model (50.8% vs 44.1% = ~7pp gap 远小于 30+pp 与 1.4B 的差距)。共识：1.4B 成功是 proof-of-concept，contribution list 需显式声明规模限制。'}\n  action_items:\n  - {round: 19, action: 'Contribution list 增加规模限制声明；Discussion 分析信号消失机制', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C3\n  summary: 参考模型依赖限制部署可行性——12/19 特征绑定 Pythia-1.4B，正文讨论不足\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: 'R18-W5: 参考模型依赖性未充分讨论为部署限制'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N1 Critical, R2-W3 Warning 后 AGREE。R1 要求 reference-agnostic baseline。R2 认为 proof-of-concept 可接受但同意正文讨论不足。R2 精确区分了两个 gap 数字：14B self-vs-cross ~7pp (Section 5.4) vs 1.5B cross-architecture -11.3pp (Table 18)。'}\n  action_items:\n  - {round: 19, action: '正文增加参考模型依赖的系统讨论（部署含义、选择策略、multi-reference 可能性）', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C4\n  summary: 多重比较未校正但做实质性判断——Binoculars p>0.05 误读为等价性\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W2: 多重比较未校正'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 atlas.tex EDD bootstrap 已加 Bonferroni'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N2 Critical, R2 部分 AGREE (not Critical)。R1: 非显著性不等于等价性需 TOST。R2: 核心结论不依赖这些 p 值，但统计论文的统计推断应严谨。R2 补充：Section 4.3 已做部分 Bonferroni 但未统一应用。Director 判定：降为 Warning。'}\n  action_items:\n  - {round: 19, action: 'Section 5.1 Binoculars 对比改为正确的统计解读（非显著不等于等价），或补充 TOST', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# ROUND 19 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R19-W1\n  summary: 方法论创新不足——标准特征+标准分类器，未分析统计特征优于PLM的原因\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N5'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪'}\n  - {round: 19, reviewers: [1, 2], note: 'R2-W1 Warning, R1 部分 REBUT (EMNLP accepts empirical)。分歧：R1 不阻拦，R2 限制 Conference excitement。共识：未深入分析统计特征优于 PLM 表征 20pp 的原因。'}\n  action_items:\n  - {round: 19, action: 'Discussion 增加一段：为何浅层统计特征优于深度 PLM 表征', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W2\n  summary: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N1: accumulation 场景无系统实验'}\n  - {round: 18, reviewers: [1, 2], note: '3-cell mix25 accumulation EDD 完成'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N3 Critical 后 R2 认为 Should-Fix。R1: GPT-2 XL 50% mixing boundary failure (AUC=0.695)。R2: proof-of-concept 首篇从受控设定起步合理。共识：问题存在但 severity 为 Warning。'}\n  action_items:\n  - {round: 19, action: 'Discussion 明确承认当前基准是 idealized conditions 下的 proof-of-concept', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W3\n  summary: Neural baseline 比较信息不对等——RF 有 reference model oracle，PLM 仅看原文\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W3: Neural baselines 仅测试 <=125M backbone'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W1 Warning, R2 AGREE。信息输入不对等：RF 用 token-level perplexity，PLM 仅获得原文 CLS。当前对比更像 PLM 不能从原文推断困惑度分布（不意外）。'}\n  action_items:\n  - {round: 19, action: 'Discussion 或 Limitations 明确标注信息不对等', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W4\n  summary: BOS seeding artifact——与 prompted generation 差 13.8pp，深度信号可能部分为 artifact\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: 'R16-W7: BOS-seeded generation 限制生态效度'}\n  - {round: 17, reviewers: [1, 2], note: 'R17 写作修复已加强 BOS caveat'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W5 Warning, R2 AGREE。13.8pp gap 暗示深度信号部分来自 BOS seeding 特异性。'}\n  action_items:\n  - {round: 19, action: '正文或 Limitations 更显著地讨论 BOS vs prompted gap 的含义', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W5\n  summary: 序数分类框架与实际方法脱节——强调 ordinal 但主管线不利用序数结构\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-W2 Warning, R1 AGREE。论文 Section 3.1 强调 ordinal classification 但主管线用标准 RF。CORAL 仅有边际改善 (Appendix B.25) 但未在正文讨论原因。'}\n  action_items:\n  - {round: 19, action: '正文简要讨论序数分类方法在此任务中边际改善的原因', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W6\n  summary: 单 LoRA seed 主实验，2-seed replication 不足以估计方差分布\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W1'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W6 Warning, R2 AGREE 程度较轻。2 seeds 方向一致但不足以估计方差分布。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# ROUND 19 — MINOR (Info)\n# ============================================================\n\n- id: R19-M1\n  summary: Abstract 信息密度过高，14B 结果的 cross-ref vs self-ref 条件混用可能误导\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2 报告 Abstract 约19% 与 Section 5.4 的 44.1% 矛盾——Director 核查发现 Abstract 实际写 约44%，R2 误读。但 Abstract 中 cross-reference EDD_70=2 与 self-reference EDD_70=0 混用仍需澄清条件。'}\n  action_items:\n  - {round: 19, action: 'Abstract 14B 结果拆分为独立句子，明确标注 cross-reference 条件', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M2\n  summary: 标题 Statistical Fingerprints 术语选择——弱迁移结果下 fingerprint 有 framing risk\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-M2, R1 轻微 REBUT（forensics 文献常用）。但鉴于跨策略 45.9%，fingerprint 暗示的唯一性和可迁移性与实证不符。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M3\n  summary: Figure 2/3 字号偏小，打印可读性受限\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-M3, R1 AGREE。视觉审查确认 heatmap cell 内约6pt。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M4\n  summary: Section 3.5 Theoretical Motivation 内容主要为经验观察\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [2], note: 'R2-M5: Empirical Motivation 可能更准确。R1 未反驳。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M5\n  summary: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺理论论证\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R1-W2, R2 AGREE 程度较轻。EDD 是操作性指标，多阈值 sensitivity 已报告。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M6\n  summary: Appendix B.20 Qwen2.5-7B Self-Reference 有 PLACEHOLDER 未填充\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'Director 在阅读论文时发现 Section B.20 有 PLACEHOLDER 注释未填充。提交前必须补全或删除。'}\n  action_items:\n  - {round: 19, action: 'B.20 PLACEHOLDER 必须在提交前补全或删除整个 subsection', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M7\n  summary: Missing references——Lakens (2017) TOST、Gutierrez (2016) ordinal regression\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: '两人共同推荐。R2 另推荐 FineWeb/DCLM（R1 认为间接关联）。R2 纠正 R1：Alemohammad (2024) 已引用。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (carried forward)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W2 下追踪，severity 降为 warning'}\n  action_items:\n  - {round: 18, action: '3-cell mix25 accumulation EDD 计算完成', assigned_to: research_director, status: done}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 R2 REBUT R1-W4：self-ref 50.8% 已足够分离。继续在 R19-C2 下追踪。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C1 下追踪。R1 纠正 R2 引用的 cross-model 46.7%。'}\n  action_items:\n  - {round: 17, action: 'Abstract 已加 within-strategy scope 声明', assigned_to: research_director, status: done}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W1 下追踪，severity 降为 warning'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W6 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C4 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 <=125M backbone\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W3 下追踪（信息不对等角度）'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%），削弱独特价值\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出，但 R19-C4 中涉及 Binoculars p>0.05 误读'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C3 下追踪，severity 升为 critical'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 (estimation vs classification)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出，Section 3.1 声明已存在'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出。Section 4.2 已有 caveat + CPI 分析。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及。Section 3.2 已加声明。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M2\n  summary: CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 推荐 Lakens (2017) TOST, Gutierrez (2016) ordinal regression。R2 另推荐 FineWeb/DCLM。R2 纠正 R1 Alemohammad (2024) 已引用。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n# Historical resolved/wont_fix (abbreviated, unchanged)\n- id: R16-N1\n  summary: 14B 结果削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Abstract 加 scope 限定; Section 6 新增 scale dependence'\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 1 贡献重组'\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 5.3 reframed'\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 6 新增段落'\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia dagger)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: 'Reviewer 确认 dagger + ref-model ablation 67-79% 已充分'\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: 'Section 4.2 group-level ablation'\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Abstract 精简'\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: 'd1-d3 balanced accuracy 领头'\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: 'Sensitivity analysis 已覆盖'\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 'Section 3.2 BOS caveat 加强。R19 re-raised as R19-W4'\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: 'Thresholding 方案已覆盖'\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 6 扩展'\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 'Section 6 含 curation scenario'\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: 'Acceptable for review'\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 'Pipeline 太简单不需要图'\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: '主文 8 页'\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: 'Structural constraint'\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: ''\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: '已加入'\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 'Classifier convergence evidence sufficient'\n  resolution_round: 16\n\n- id: R18-M3\n  summary: Section 3.5 标题过大\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: '已改为 Theoretical Motivation'\n  resolution_round: 18\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: '项目收尾不再跑新实验'\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C4 下追踪'}\n  resolution: ''\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: 'Section 2 已引用'\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: '编译验证通过'\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: '用户指示不再跑新实验'\n  resolution_round: 14"
  }
}
```

</details>

---


### Tool result

_source line 1767 · 2026-05-22T23:18:12.725683+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml\", \"bytes\": 21081}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1768 · 2026-05-22T23:20:33.737350+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 19\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文定义了\"递归生成深度估计\"任务，将其形式化为序数分类。构建了 180K 实例的基准数据集（3 模型族 × 3 解码策略 × 4 深度），提出 19 个统计特征 + Random Forest 的轻量管线，引入 Effective Discriminable Depth (EDD) 指标。主要发现：深度信号集中在困惑度分布尾部，解码策略比模型架构更影响迁移，信号随规模衰减（14B EDD₇₀=0）。论文实证工作系统全面，但方法论创新有限、泛化能力不足、且部分关键声明与证据不匹配。\n\n---\n\n## Strengths\n\n1. **任务形式化具有真正的新颖性** [R1 AGREE, R2 AGREE]：将递归生成深度从二分类推广到序数估计是自然且有价值的形式化。与 model collapse 和 AI text detection 文献的区分在 Section 2 清晰。EDD 指标提供了有操作价值的可区分深度摘要。\n\n2. **系统性实证分析深度出色** [R1 AGREE, R2 AGREE]：180K 实例、3×3 网格、30+ 消融实验（Appendix B.1–B.34）的密度在 EMNLP 投稿中少见。Depth Degradation Atlas 提供了直观的退化全景图。\n\n3. **特征一致性发现有理论价值** [R1 AGREE, R2 AGREE]：p90_ppl 和 var_surprisal 在 9/9 cells 稳居 top-2（Table 3），跨模型特征排名 Spearman ρ=0.868。Gini/SHAP/CPI 三种方法交叉验证特征排名（Kendall's W=0.90）。\n\n4. **诚实报告负面结果** [R1 AGREE, R2 AGREE]：跨策略迁移失败（45.9%）、14B 衰减（EDD=0）、curation PoC 不显著（p>0.4）均有透明报告。\n\n5. **可复现性良好** [R1: 4/5, R2: 4/5]：超参数、数据规模、训练细节在正文和附录中详细记录。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**C1. 泛化性 claim 与证据系统性失配** [R1 AGREE, R2 N2 Critical]\n- 跨策略迁移：d1–d3 仅 45.9%（Section 5.3），接近随机\n- 14B self-reference：EDD₇₀=0，4-class 仅 50.8%（Section 5.4）\n- 标题 \"Statistical Fingerprints\" 暗示可迁移信号，但实证表明信号高度依赖已知模型族和解码策略\n- Abstract \"consistent in direction but scale-dependent in magnitude\" 将方向一致性包装为正面结论，但 45.9% 的分类器在部署场景中几乎不可用\n- Two-stage pipeline 恢复到 70.5%（Section 5.3）是重要发现但仍远低于 within-cell 水平\n- **共识**：需在 Abstract 和 Introduction 明确限定 claim scope 为 \"within known model-strategy configurations\"\n\n**C2. 14B 规模衰减是根本性瓶颈** [R1 AGREE, R2 N3 Critical]\n- Self-reference 50.8%（2× chance）但 EDD₇₀=0 意味着序数结构已坍塌\n- 当前主流 LLM 70B–405B，1.4B 成功更多是 proof-of-concept\n- Introduction/Discussion 叙事以积极语气讨论前景，未充分传达这是当前方法的根本瓶颈\n- R2 REBUT R1-W4（14B confound）：self-ref 数据已足够分离 scale vs ref-model（50.8% vs 44.1% = ~7pp gap 远小于 30+pp 与 1.4B 的差距）——scale 是主要驱动因素\n- **共识**：Contribution list 需显式声明规模限制\n\n**C3. 参考模型依赖限制部署可行性** [R1 N1 Critical, R2 W3 Warning → AGREE]\n- 19 特征中 12 个依赖 Pythia-1.4B log-probabilities\n- Cross-architecture 下降 4–11pp（Appendix B.17 Table 18）\n- Generator-unknown 场景下无参考模型选择策略\n- 正文仅笼统提及，未系统讨论部署含义\n- **分歧**：R1 列为 Critical（pipeline 根本瓶颈），R2 认为 proof-of-concept 阶段可接受 Should-Fix。Director 判定：由于 12/19 特征绑定且缺乏选择策略讨论，维持 Critical。\n\n---\n\n### Should-Fix (Warning)\n\n**W1. 方法论创新不足** [R1 部分 REBUT, R2 W1 Warning]\n- 19 特征均为标准 NLP 特征（GLTR/DetectGPT/Ghostbuster 均有先例），RF 为 off-the-shelf\n- 本质是\"已有特征应用于新任务\"\n- R1 认为 EMNLP 接收系统性实证研究；R2 认为这限制了 Conference excitement\n- **未深入分析统计特征优于 PLM 表征 20pp 的根本原因**——这个 \"why\" 本身有价值\n\n**W2. Full-replacement benchmark 与真实 accumulation 场景 gap** [R1 N3 Critical → R2 认为 Should-Fix]\n- 真实场景涉及 accumulation + unknown mixing ratios + 异构模型\n- Appendix B.8 仅覆盖 6 组合，GPT-2 XL 50% mixing 出现 boundary failure（AUC=0.695）\n- **共识**：证据不足，但首篇论文从受控设定起步合理\n\n**W3. Neural baseline 比较信息不对等** [R1 W1 Warning, R2 AGREE]\n- RF 使用参考模型 oracle（token-level perplexity），DeBERTa/RoBERTa 仅获得原文\n- 当前对比更像 \"PLM 不能从原文推断困惑度分布\"（不意外）\n\n**W4. 多重比较未统一校正** [R1 N2 Critical → R2 认为非 Critical]\n- Section 5.1 将 Binoculars p>0.05 解读为 \"statistical equivalence\"，但非显著性 ≠ 等价性（需 TOST）\n- Section 4.3 已做部分 Bonferroni 但未统一应用\n- Director 判定：核心结论不依赖这些 p 值，降为 Warning，但 Binoculars 等价性声明必须修正\n\n**W5. BOS seeding artifact** [R1 W5, R2 AGREE]\n- BOS seeding vs prompted generation 差 13.8pp（Appendix B.16）\n- 深度信号可能部分来自无条件生成的特异性 artifact\n- 正文应更显著地讨论此差距的含义\n\n**W6. 序数分类框架与实际方法脱节** [R1 AGREE, R2 W2]\n- 强调 ordinal classification 但主管线用标准 RF 不利用序数结构\n- CORAL 仅有边际改善（Appendix B.25）但未在正文讨论原因\n\n**W7. 单 LoRA seed 统计功效** [R1 W6, R2 AGREE 程度较轻]\n- 主实验单 seed，2-seed replication 方向一致但不足以估计方差分布\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. 任务定义的新颖性和价值 ✓\n2. 实证分析的系统性和深度 ✓\n3. 泛化 claim 超出证据支撑范围 ✓\n4. 14B 规模衰减是根本性挑战 ✓\n5. 参考模型依赖需更充分讨论 ✓\n6. Neural baseline 比较信息不对等 ✓\n7. BOS seeding artifact 值得讨论 ✓\n8. 序数框架与方法脱节 ✓\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分歧实质 |\n|------|-----|-----|---------|\n| Excitement | 3.5/5 | 2.5/5 | R1 更重任务新颖性；R2 更重方法创新和部署前景 |\n| 参考模型依赖严重程度 | Critical | Warning | R1: pipeline 根本瓶颈；R2: proof-of-concept 可接受 |\n| 多重比较严重程度 | Critical | Minor→Warning | R1: 统计论文需统计严谨；R2: 核心结论不依赖 p 值 |\n| Full-replacement gap 严重程度 | Critical | Warning | R1: 生态效度不足；R2: 首篇论文合理起步 |\n| 方法论创新 | 不阻拦 | 限制 Conference | R1: EMNLP 接收实证研究；R2: 零创新限制 excitement |\n| 14B confound 分离 | W4 Warning | REBUT | R2: self-ref 50.8% 已足够分离 scale vs ref-model |\n\n---\n\n## Questions（需作者回答）\n\n1. Generator-unknown 部署场景下的参考模型选择策略？是否考虑 multi-reference ensemble？\n2. 为什么主管线不使用序数分类器？CORAL 在此任务中边际改善的原因分析？\n3. BOS seeding vs prompted generation 的 13.8pp gap——深度信号中有多大比例来自 BOS seeding artifact？\n4. 14B 以上规模的理论预期？是否存在 U 型曲线？\n5. 统计特征优于 PLM 表征 20pp 的根本原因？这对 NLP 表征学习有何启示？\n6. 10% mixing ratio 下 pipeline 是否仍能工作？\n7. QWK=0.89 对应的具体 ordinal misclassification pattern？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同推荐**：\n- Lakens (2017) equivalence testing 方法论（TOST）\n- Gutiérrez et al. (2016) ordinal regression 综述\n\n**R2 推荐**（R1 认为间接关联，nice-to-have）：\n- FineWeb (Penedo et al., 2024) — 数据策展管线\n- DCLM (Li et al., 2024) — 大规模数据策展\n- Sachdeva et al. (2024) Training on the Test Task\n\n**交叉纠正**：R1 推荐的 Alemohammad et al. (2024) 已在 Section 2 第1段引用（R2 确认）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warnings, 15 info）：\n\n**Warnings**:\n1. **pp.1-2 无 display item**：连续 2 页纯文本（Abstract + Introduction + Related Work），审稿人前 2 页无视觉锚点。建议将 Figure 1 提升到 page 2。\n2. **p.7 Figure 2/3 字号偏小**：heatmap cell 内数值约 6pt，Figure 3 三面板 axis labels 约正文 60%。建议 Figure 2 改为 figure*（全宽）。\n3. **p.8 极度拥挤**：Table 4 + Table 5 + Section 5（4 子节）+ Section 6 全压缩在一页，审稿人可能认为 Generalization 和 Discussion 匆忙收尾。\n\n**正面确认**：主文 8 页 ✓；所有表格 booktabs 统一、最优结果加粗一致；无 margin overflow、无 LaTeX 渲染错误、无 [?] 未解析引用；Limitations 覆盖 3 点 ✓；Ethics Statement 存在 ✓；Appendix 15 页详尽。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n**置信度：4/5**\n\n**R1: 3.5 (Borderline Conference) | R2: 3.0 (Findings)**\n\n本文的核心价值在于任务形式化——将递归生成深度估计定义为序数分类，引入 EDD 指标，构建系统性 180K 基准。这是 genuinely novel 的问题定义，且实证工作的深度和诚实度达到顶会水准。\n\n但以下因素将评分限制在 Findings：\n\n1. **方法论贡献有限**：管线完全由已有组件组成（标准统计特征 + 标准 RF），无方法创新。四种分类器在 0.8pp 内收敛（Appendix B.25）表明准确率上限由特征决定，但特征本身也非本文提出。\n\n2. **泛化性是结构性瓶颈**：跨策略 45.9%、14B EDD₇₀=0 表明方法仅在已知模型-策略配置下有效。标题 \"Statistical Fingerprints\" 暗示的可迁移性与实证结果存在系统性张力。\n\n3. **规模衰减是根本性的**：当前主流 LLM 70B–405B，1.4B 规模的成功定位为 proof-of-concept 更合适。\n\n4. **参考模型硬依赖**：12/19 特征绑定单一参考模型，跨架构下降 4–11pp，无选择策略讨论。\n\n**升分路径**：如果 rebuttal 能 (a) 明确限定 claim scope 到 within-configuration 并调整标题/Abstract 措辞, (b) 补充 TOST/Bonferroni 校正关键统计声明, (c) 在 Discussion 中深入分析统计特征优于 PLM 的原因, 则可重新评估至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n**Abstract**: 信息密度过高。最后长括号内混合了准确率、EDD、因素分解三个维度的数字，建议拆分。Director 核查：R2 报告的 \"≈19%\" 不一致问题为误读——当前 abstract.tex 实际写 \"~44%\"，与 Section 5.4 一致。但 cross-reference EDD₇₀=2 与 self-reference EDD₇₀=0 的混用仍需明确标注条件。\n\n**Introduction (Section 1)**: 动机合理，贡献列表结构清晰。但 \"consistent in direction\" 需弱化——方向一致性不等于跨条件可用性。建议在贡献列表增加显式规模限制声明。\n\n**Related Work (Section 2)**: 覆盖全面（model collapse、AI detection、membership inference、ordinal classification、decoding effects），定位清晰。建议补充 Lakens (2017) equivalence testing 方法论。\n\n**Method (Section 3)**: Benchmark 构建设计合理。EDD 定义形式化清晰。建议更早提及 VIF>10 共线性（当前 Section 4.2 才出现）。\"depth estimation\" vs \"ordinal classification\" 术语声明已存在（Section 3.1），但后续使用仍偶有混用。\n\n**Atlas (Section 4)**: 最强章节。特征重要性分析透彻，策略依赖轨迹发现有理论意义。Figure 2/3 字号需增大。\n\n**Generalization (Section 5)**: 内容密度过高，5 子节不到 2 页。Two-stage pipeline 恢复到 70.5% 是重要发现但仅一句话带过。Table 4/5 的 cross-model/cross-strategy 结果应给更多讨论空间。\n\n**Discussion (Section 6)**: 过于压缩。5 个加粗主题每个仅 2-3 句。\"Why neural methods underperform\" 是核心洞察值得展开——统计特征优于 PLM 表征 20pp 的原因分析有独立的学术价值。建议考虑将 Conclusion 独立成节。\n\n**Limitations**: 覆盖关键局限，但 BOS seeding artifact（-13.8pp）的讨论应更显著。\n\n**Appendix**: 内容极为详尽（15 页，B.1–B.34），远超同类投稿。**注意：Section B.20 (Qwen2.5-7B Self-Reference) 有 PLACEHOLDER 注释未填充——提交前必须补全或删除。**\n\n**格式合规**: 主文 8 页 ✓；double-blind 匿名 ✓（作者标注 \"Anonymous\"）；Limitations ✓；Ethics Statement ✓；ACL 模板 ✓；引用格式统一 ✓。",
  "project": "recursive_gen_depth_est",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 19\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文定义了\"递归生成深度估计\"任务，将其形式化为序数分类。构建了 180K 实例的基准数据集（3 模型族 × 3 解码策略 × 4 深度），提出 19 个统计特征 + Random Forest 的轻量管线，引入 Effective Discriminable Depth (EDD) 指标。主要发现：深度信号集中在困惑度分布尾部，解码策略比模型架构更影响迁移，信号随规模衰减（14B EDD₇₀=0）。论文实证工作系统全面，但方法论创新有限、泛化能力不足、且部分关键声明与证据不匹配。\n\n---\n\n## Strengths\n\n1. **任务形式化具有真正的新颖性** [R1 AGREE, R2 AGREE]：将递归生成深度从二分类推广到序数估计是自然且有价值的形式化。与 model collapse 和 AI text detection 文献的区分在 Section 2 清晰。EDD 指标提供了有操作价值的可区分深度摘要。\n\n2. **系统性实证分析深度出色** [R1 AGREE, R2 AGREE]：180K 实例、3×3 网格、30+ 消融实验（Appendix B.1–B.34）的密度在 EMNLP 投稿中少见。Depth Degradation Atlas 提供了直观的退化全景图。\n\n3. **特征一致性发现有理论价值** [R1 AGREE, R2 AGREE]：p90_ppl 和 var_surprisal 在 9/9 cells 稳居 top-2（Table 3），跨模型特征排名 Spearman ρ=0.868。Gini/SHAP/CPI 三种方法交叉验证特征排名（Kendall's W=0.90）。\n\n4. **诚实报告负面结果** [R1 AGREE, R2 AGREE]：跨策略迁移失败（45.9%）、14B 衰减（EDD=0）、curation PoC 不显著（p>0.4）均有透明报告。\n\n5. **可复现性良好** [R1: 4/5, R2: 4/5]：超参数、数据规模、训练细节在正文和附录中详细记录。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**C1. 泛化性 claim 与证据系统性失配** [R1 AGREE, R2 N2 Critical]\n- 跨策略迁移：d1–d3 仅 45.9%（Section 5.3），接近随机\n- 14B self-reference：EDD₇₀=0，4-class 仅 50.8%（Section 5.4）\n- 标题 \"Statistical Fingerprints\" 暗示可迁移信号，但实证表明信号高度依赖已知模型族和解码策略\n- Abstract \"consistent in direction but scale-dependent in magnitude\" 将方向一致性包装为正面结论，但 45.9% 的分类器在部署场景中几乎不可用\n- Two-stage pipeline 恢复到 70.5%（Section 5.3）是重要发现但仍远低于 within-cell 水平\n- **共识**：需在 Abstract 和 Introduction 明确限定 claim scope 为 \"within known model-strategy configurations\"\n\n**C2. 14B 规模衰减是根本性瓶颈** [R1 AGREE, R2 N3 Critical]\n- Self-reference 50.8%（2× chance）但 EDD₇₀=0 意味着序数结构已坍塌\n- 当前主流 LLM 70B–405B，1.4B 成功更多是 proof-of-concept\n- Introduction/Discussion 叙事以积极语气讨论前景，未充分传达这是当前方法的根本瓶颈\n- R2 REBUT R1-W4（14B confound）：self-ref 数据已足够分离 scale vs ref-model（50.8% vs 44.1% = ~7pp gap 远小于 30+pp 与 1.4B 的差距）——scale 是主要驱动因素\n- **共识**：Contribution list 需显式声明规模限制\n\n**C3. 参考模型依赖限制部署可行性** [R1 N1 Critical, R2 W3 Warning → AGREE]\n- 19 特征中 12 个依赖 Pythia-1.4B log-probabilities\n- Cross-architecture 下降 4–11pp（Appendix B.17 Table 18）\n- Generator-unknown 场景下无参考模型选择策略\n- 正文仅笼统提及，未系统讨论部署含义\n- **分歧**：R1 列为 Critical（pipeline 根本瓶颈），R2 认为 proof-of-concept 阶段可接受 Should-Fix。Director 判定：由于 12/19 特征绑定且缺乏选择策略讨论，维持 Critical。\n\n---\n\n### Should-Fix (Warning)\n\n**W1. 方法论创新不足** [R1 部分 REBUT, R2 W1 Warning]\n- 19 特征均为标准 NLP 特征（GLTR/DetectGPT/Ghostbuster 均有先例），RF 为 off-the-shelf\n- 本质是\"已有特征应用于新任务\"\n- R1 认为 EMNLP 接收系统性实证研究；R2 认为这限制了 Conference excitement\n- **未深入分析统计特征优于 PLM 表征 20pp 的根本原因**——这个 \"why\" 本身有价值\n\n**W2. Full-replacement benchmark 与真实 accumulation 场景 gap** [R1 N3 Critical → R2 认为 Should-Fix]\n- 真实场景涉及 accumulation + unknown mixing ratios + 异构模型\n- Appendix B.8 仅覆盖 6 组合，GPT-2 XL 50% mixing 出现 boundary failure（AUC=0.695）\n- **共识**：证据不足，但首篇论文从受控设定起步合理\n\n**W3. Neural baseline 比较信息不对等** [R1 W1 Warning, R2 AGREE]\n- RF 使用参考模型 oracle（token-level perplexity），DeBERTa/RoBERTa 仅获得原文\n- 当前对比更像 \"PLM 不能从原文推断困惑度分布\"（不意外）\n\n**W4. 多重比较未统一校正** [R1 N2 Critical → R2 认为非 Critical]\n- Section 5.1 将 Binoculars p>0.05 解读为 \"statistical equivalence\"，但非显著性 ≠ 等价性（需 TOST）\n- Section 4.3 已做部分 Bonferroni 但未统一应用\n- Director 判定：核心结论不依赖这些 p 值，降为 Warning，但 Binoculars 等价性声明必须修正\n\n**W5. BOS seeding artifact** [R1 W5, R2 AGREE]\n- BOS seeding vs prompted generation 差 13.8pp（Appendix B.16）\n- 深度信号可能部分来自无条件生成的特异性 artifact\n- 正文应更显著地讨论此差距的含义\n\n**W6. 序数分类框架与实际方法脱节** [R1 AGREE, R2 W2]\n- 强调 ordinal classification 但主管线用标准 RF 不利用序数结构\n- CORAL 仅有边际改善（Appendix B.25）但未在正文讨论原因\n\n**W7. 单 LoRA seed 统计功效** [R1 W6, R2 AGREE 程度较轻]\n- 主实验单 seed，2-seed replication 方向一致但不足以估计方差分布\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. 任务定义的新颖性和价值 ✓\n2. 实证分析的系统性和深度 ✓\n3. 泛化 claim 超出证据支撑范围 ✓\n4. 14B 规模衰减是根本性挑战 ✓\n5. 参考模型依赖需更充分讨论 ✓\n6. Neural baseline 比较信息不对等 ✓\n7. BOS seeding artifact 值得讨论 ✓\n8. 序数框架与方法脱节 ✓\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分歧实质 |\n|------|-----|-----|---------|\n| Excitement | 3.5/5 | 2.5/5 | R1 更重任务新颖性；R2 更重方法创新和部署前景 |\n| 参考模型依赖严重程度 | Critical | Warning | R1: pipeline 根本瓶颈；R2: proof-of-concept 可接受 |\n| 多重比较严重程度 | Critical | Minor→Warning | R1: 统计论文需统计严谨；R2: 核心结论不依赖 p 值 |\n| Full-replacement gap 严重程度 | Critical | Warning | R1: 生态效度不足；R2: 首篇论文合理起步 |\n| 方法论创新 | 不阻拦 | 限制 Conference | R1: EMNLP 接收实证研究；R2: 零创新限制 excitement |\n| 14B confound 分离 | W4 Warning | REBUT | R2: self-ref 50.8% 已足够分离 scale vs ref-model |\n\n---\n\n## Questions（需作者回答）\n\n1. Generator-unknown 部署场景下的参考模型选择策略？是否考虑 multi-reference ensemble？\n2. 为什么主管线不使用序数分类器？CORAL 在此任务中边际改善的原因分析？\n3. BOS seeding vs prompted generation 的 13.8pp gap——深度信号中有多大比例来自 BOS seeding artifact？\n4. 14B 以上规模的理论预期？是否存在 U 型曲线？\n5. 统计特征优于 PLM 表征 20pp 的根本原因？这对 NLP 表征学习有何启示？\n6. 10% mixing ratio 下 pipeline 是否仍能工作？\n7. QWK=0.89 对应的具体 ordinal misclassification pattern？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同推荐**：\n- Lakens (2017) equivalence testing 方法论（TOST）\n- Gutiérrez et al. (2016) ordinal regression 综述\n\n**R2 推荐**（R1 认为间接关联，nice-to-have）：\n- FineWeb (Penedo et al., 2024) — 数据策展管线\n- DCLM (Li et al., 2024) — 大规模数据策展\n- Sachdeva et al. (2024) Training on the Test Task\n\n**交叉纠正**：R1 推荐的 Alemohammad et al. (2024) 已在 Section 2 第1段引用（R2 确认）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warnings, 15 info）：\n\n**Warnings**:\n1. **pp.1-2 无 display item**：连续 2 页纯文本（Abstract + Introduction + Related Work），审稿人前 2 页无视觉锚点。建议将 Figure 1 提升到 page 2。\n2. **p.7 Figure 2/3 字号偏小**：heatmap cell 内数值约 6pt，Figure 3 三面板 axis labels 约正文 60%。建议 Figure 2 改为 figure*（全宽）。\n3. **p.8 极度拥挤**：Table 4 + Table 5 + Section 5（4 子节）+ Section 6 全压缩在一页，审稿人可能认为 Generalization 和 Discussion 匆忙收尾。\n\n**正面确认**：主文 8 页 ✓；所有表格 booktabs 统一、最优结果加粗一致；无 margin overflow、无 LaTeX 渲染错误、无 [?] 未解析引用；Limitations 覆盖 3 点 ✓；Ethics Statement 存在 ✓；Appendix 15 页详尽。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n**置信度：4/5**\n\n**R1: 3.5 (Borderline Conference) | R2: 3.0 (Findings)**\n\n本文的核心价值在于任务形式化——将递归生成深度估计定义为序数分类，引入 EDD 指标，构建系统性 180K 基准。这是 genuinely novel 的问题定义，且实证工作的深度和诚实度达到顶会水准。\n\n但以下因素将评分限制在 Findings：\n\n1. **方法论贡献有限**：管线完全由已有组件组成（标准统计特征 + 标准 RF），无方法创新。四种分类器在 0.8pp 内收敛（Appendix B.25）表明准确率上限由特征决定，但特征本身也非本文提出。\n\n2. **泛化性是结构性瓶颈**：跨策略 45.9%、14B EDD₇₀=0 表明方法仅在已知模型-策略配置下有效。标题 \"Statistical Fingerprints\" 暗示的可迁移性与实证结果存在系统性张力。\n\n3. **规模衰减是根本性的**：当前主流 LLM 70B–405B，1.4B 规模的成功定位为 proof-of-concept 更合适。\n\n4. **参考模型硬依赖**：12/19 特征绑定单一参考模型，跨架构下降 4–11pp，无选择策略讨论。\n\n**升分路径**：如果 rebuttal 能 (a) 明确限定 claim scope 到 within-configuration 并调整标题/Abstract 措辞, (b) 补充 TOST/Bonferroni 校正关键统计声明, (c) 在 Discussion 中深入分析统计特征优于 PLM 的原因, 则可重新评估至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n**Abstract**: 信息密度过高。最后长括号内混合了准确率、EDD、因素分解三个维度的数字，建议拆分。Director 核查：R2 报告的 \"≈19%\" 不一致问题为误读——当前 abstract.tex 实际写 \"~44%\"，与 Section 5.4 一致。但 cross-reference EDD₇₀=2 与 self-reference EDD₇₀=0 的混用仍需明确标注条件。\n\n**Introduction (Section 1)**: 动机合理，贡献列表结构清晰。但 \"consistent in direction\" 需弱化——方向一致性不等于跨条件可用性。建议在贡献列表增加显式规模限制声明。\n\n**Related Work (Section 2)**: 覆盖全面（model collapse、AI detection、membership inference、ordinal classification、decoding effects），定位清晰。建议补充 Lakens (2017) equivalence testing 方法论。\n\n**Method (Section 3)**: Benchmark 构建设计合理。EDD 定义形式化清晰。建议更早提及 VIF>10 共线性（当前 Section 4.2 才出现）。\"depth estimation\" vs \"ordinal classification\" 术语声明已存在（Section 3.1），但后续使用仍偶有混用。\n\n**Atlas (Section 4)**: 最强章节。特征重要性分析透彻，策略依赖轨迹发现有理论意义。Figure 2/3 字号需增大。\n\n**Generalization (Section 5)**: 内容密度过高，5 子节不到 2 页。Two-stage pipeline 恢复到 70.5% 是重要发现但仅一句话带过。Table 4/5 的 cross-model/cross-strategy 结果应给更多讨论空间。\n\n**Discussion (Section 6)**: 过于压缩。5 个加粗主题每个仅 2-3 句。\"Why neural methods underperform\" 是核心洞察值得展开——统计特征优于 PLM 表征 20pp 的原因分析有独立的学术价值。建议考虑将 Conclusion 独立成节。\n\n**Limitations**: 覆盖关键局限，但 BOS seeding artifact（-13.8pp）的讨论应更显著。\n\n**Appendix**: 内容极为详尽（15 页，B.1–B.34），远超同类投稿。**注意：Section B.20 (Qwen2.5-7B Self-Reference) 有 PLACEHOLDER 注释未填充——提交前必须补全或删除。**\n\n**格式合规**: 主文 8 页 ✓；double-blind 匿名 ✓（作者标注 \"Anonymous\"）；Limitations ✓；Ethics Statement ✓；ACL 模板 ✓；引用格式统一 ✓。",
    "project": "recursive_gen_depth_est",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1769 · 2026-05-22T23:20:37.635304+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3897
}
```

</details>

---


### Tool call

_source line 1770 · 2026-05-22T23:20:44.816790+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '初始化到收敛判断已完成'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '初始化到收敛判断已完成'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1771 · 2026-05-22T23:20:44.917595+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 1772 · 2026-05-22T23:20:56.547381+00:00_

---

**Round 19 审稿完成。**

**最终评分：3.0 (Findings)**（R1: 3.5 Borderline Conference, R2: 3.0 Findings）

报告已投递至 Research Director。核心结论：

- **3 个 Critical**：泛化 claim 超出证据（跨策略 45.9%）、14B 规模衰减（EDD₇₀=0）、参考模型硬依赖（12/19 特征绑定）
- **7 个 Warning**：方法论创新不足、full-replacement gap、neural baseline 信息不对等、多重比较未统一校正、BOS seeding artifact、序数框架脱节、单 LoRA seed
- **Director 核查纠正**：R2 报告的 Abstract "≈19%" 不一致为误读——实际写 "~44%"，与 Section 5.4 一致
- **Appendix B.20 有 PLACEHOLDER 未填充**——提交前必须处理
- Issue Tracker 已更新（`review_issues.yaml`），视觉审查结果已拼入报告

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 156

## Round 156

2 recorded events


### User

_source line 1773 · 2026-05-22T23:20:59.039331+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- R2 的 3 个 Critical 问题中，**N1（Abstract ≈19% 表述错误）和 N3（14B scalability）我完全同意**，**N2（claim-evidence 失配）实质同意但对 "过拟合" 定性有修正**（信号一致性证据存在，问题更多在 framing 而非方法）。
- R2 引用的 "跨模型 46.7%" 在论文中找不到对应（Section 5.2 报告 55.4%），已标注供 Director 参考。
- R2 的 Q3 提到两阶段方案——**论文已在 Section 5.3 / Appendix B.31 做了这个实验**，R2 可能遗漏。
- R2 给 3.0，我给 3.5，分歧主要在 Excitement 维度（问题定义新颖性的权重）。3.0–3.5 范围我认为都可辩护。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1774 · 2026-05-22T23:21:11.608277+00:00_

审稿流程全部完成。

**Round 19 审稿报告已投递至 Research Director。**

汇总：
- **R1**: 3.5 (Borderline Conference) | **R2**: 3.0 (Findings) | **综合**: **3.0 (Findings)**
- **3 个 Critical**：泛化 claim-evidence 失配、14B 规模衰减根本瓶颈、参考模型硬依赖
- **7 个 Warning**：方法论创新不足、full-replacement gap、neural baseline 信息不对等、多重比较未统一校正、BOS seeding artifact、序数框架脱节、单 LoRA seed
- **升分路径**：限定 claim scope + 修正统计声明 + 深入分析统计特征优于 PLM 原因 → 可至 3.5
- **紧急提醒**：Appendix B.20 有 PLACEHOLDER 未填充，提交前必须处理
- Issue Tracker 已同步更新至 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 157

## Round 157

66 recorded events


### User

_source line 1775 · 2026-05-25T21:13:45.182727+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recursive_gen_depth_est
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Long Paper)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1776 · 2026-05-25T21:13:52.226070+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1777 · 2026-05-25T21:13:52.377602+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1778 · 2026-05-25T21:13:57.223070+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1779 · 2026-05-25T21:13:57.324089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1780 · 2026-05-25T21:14:03.605493+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1781 · 2026-05-25T21:14:05.164020+00:00_

{"result":"# 项目 recursive_gen_depth_est 概况\n\n## 实验状态 (152 个)\n\n- **cross_model_olmo_temp09_001**: DONE (killed) — \n- **pythia_topk50_001**: DONE (success) — \n- **cross_model_gpt2xl_001**: DONE (success) — \n- **cross_model_olmo_002**: DONE (success) — \n- **pythia_temp09_001**: DONE (success) — \n- **mvp_pipeline_pythia_002**: DONE (success) — \n- **cross_model_olmo_001**: DONE (failed) — \n- **mvp_pipeline_qwen_base_004**: DONE (killed) — \n- **mvp_pipeline_pythia_001**: DONE (killed) — \n- **mvp_pipeline_base_002**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (killed) — \n- **mvp_pipeline_001**: DONE (killed) — \n- **mvp_pipeline_base_003**: DONE (killed) — \n- **mvp_pipeline_004**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- accum_v2_mix25（准备中）\n- accum_v2_mix50（准备中）\n\n## 近期结论\n- **qwen25_7b_selfref_001** (success): Recursive generation depth signal (d0-d3) should persist in Qwen2.5-7B with self-reference feature extraction, similar to 14B scale results, supporting that the phenomenon is not model-scale-specific. ← 基于 cross_scale_qwen7b_001\n- **plan_020_bootstrap_ci** (success): B=10,000 bootstrap resampling of per-sample 5-fold CV predictions provides stable 95% CIs for the 9 atlas cells, confirming that B=1,000 CIs had already converged.\n- **plan_018_ordinal_baseline_v2** (success): Binary detection methods (Binoculars, Fast-DetectGPT) produce continuous scores that primarily distinguish d0 vs d1+; their ordinal resolution across d1/d2/d3 is near-chance, lacking the depth gradient captured by our 19-feature statistical pipeline.\n\n## 趋势\n成功 95 / 负向 14 / 失败 17 / 共 150\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ngpu-6000pro-2: 无 GPU 信息\n\n## 告警\n- mvp_pipeline_001: 已被终止 — unknown\n- mvp_pipeline_002: 已被终止 — unknown\n- mvp_pipeline_003: 已被终止 — unknown\n- mvp_pipeline_004: 已被终止 — unknown\n- mvp_pipeline_base_002: 已被终止 — unknown\n- mv
…[truncated 1561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1558
}
```

</details>

---


### Tool call

_source line 1782 · 2026-05-25T21:14:05.265000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1783 · 2026-05-25T21:14:05.265447+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	
5	% Change "review" to "final" to generate the camera-ready version.
6	\usepackage[review]{acl}
7	
8	% Standard package includes (per official ACL template)
9	\usepackage{times}
10	\usepackage{latexsym}
11	\usepackage[T1]{fontenc}
12	\usepackage[utf8]{inputenc}
13	\usepackage{microtype}
14	% \usepackage{inconsolata}  % not available in this TeX installation
15	\usepackage{graphicx}
16	
17	% Additional packages for this paper
18	\usepackage{booktabs}
19	\usepackage{amsmath}
20	\usepackage{amssymb}
21	\usepackage{multirow}
22	\usepackage{subcaption}
23	\usepackage{enumitem}
24	\usepackage{amsthm}
25	
26	\theoremstyle{definition}
27	\newtheorem{definition}{Definition}
28	
29	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
30	
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	\input{abstract}
37	
38	\input{introduction}
39	
40	\input{related_work}
41	
42	\input{method}
43	
44	\input{theory}
45	
46	\input{atlas}
47	
48	\input{generalization}
49	
50	\input{discussion}
51	
52	\input{conclusion}
53	
54	\bibliography{references}
55	
56	\appendix
57	\input{section_appendix}
58	
59	\end{document}
60	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1784 · 2026-05-25T21:14:11.341998+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1785 · 2026-05-25T21:14:11.493160+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1786 · 2026-05-25T21:14:12.497508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1787 · 2026-05-25T21:14:12.498062+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1788 · 2026-05-25T21:14:12.498946+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K cell-instances (140K unique passages) spanning three model families, three decoding strategies, and four depths under full-replacement chains at 1--1.5B scale.
4	A lightweight pipeline (19 statistical features classified by Random Forest) achieves d1--d3 balanced accuracy of 59--82\% across nine model--strategy cells, with Effective Discriminable Depth $\mathrm{EDD}_{0.70} = 3$ in 8/9 cells.
5	Three findings emerge: (1)~depth signal concentrates in perplexity distribution tails, corroborated by classifier convergence and independent cross-perplexity features; (2)~decoding strategy affects cross-condition transfer more than model architecture, consistent with structurally distinct degradation trajectories; (3)~signal attenuates with scale (14B: $\mathrm{EDD}_{0.70}{=}2$ under nucleus and temperature, 0 under top-$k$), with reference-model choice as a major confound.
6	Our claims hold within-strategy or when decoding configuration is known; a two-stage routing pipeline recovers $+$11.5\,pp under cross-strategy transfer.
7	Perturbation-based and membership-inference baselines lack ordinal resolution; depth estimation requires distributional statistics beyond binary detection scores\footnote{Code and data are available at \url{https://anonymous.4open.science/r/recursive_gen_depth_est-1BD0/}.}.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool result

_source line 1789 · 2026-05-25T21:14:12.499360+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models (LLMs) are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	We focus on the 1--1.5B parameter regime under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination involves partial mixing at unknown proportions; full replacement provides an upper bound on depth signal strength (\S\ref{sec:discussion}).
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors \cite{binoculars2024,fast_detectgpt2024,diveye2026} collapse all depths $d \geq 1$ into a single category, a limitation we confirm empirically: their pairwise d1-vs-d2 AUC collapses to chance level (\S\ref{sec:gen:baselines}); watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone (Figure~\ref{fig:problem}).
13	
14	We fin
…[truncated 3227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1790 · 2026-05-25T21:14:16.725140+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1791 · 2026-05-25T21:14:17.579515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1792 · 2026-05-25T21:14:17.680434+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad} and Markovian generation chains \cite{geng2026_markovian}.
6	\citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (grounding our EDD ceiling, \S\ref{sec:method:theory}); refinements address generalization-to-memorization transitions \cite{shi2025_closer_look} and broader model classes \cite{dohmatob2025_strong_collapse}.
7	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena; we respond by operationalizing tail-erosion into a deployable ordinal classifier that reveals strategy-dependent trajectories the theory does not predict.
8	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
9	
10	\paragraph{AI Text Detection.}
11	The detection literature \cite{wu2025_detection_survey} spans statistical \cite{mitchell2023_detectgpt,fast_detectgpt2024,binoculars2024,gehrmann2019_gltr,verma2024_ghostbuster}, geometric \cite{tulchinskii2023_intrinsic_dim}, and watermarking \cite{kirchenbauer2023_watermark} methods, with known limits \cite{sadasivan2023_paraphrase,pudasaini2026_detection_fails}.
12	\citet{bevendorff2025_two_paradigms} distinguish attribution from verification; all remain binary, whereas our approach outputs ordinal depth labels along a third axis, recursive iteration.
13	
14	\paragraph{Adjacent Tasks and Methods.}
15	Training data extraction \cite{carlini2021_extracting} motivates provenance pipelines; Min-K\% Prob \cite{shi2024_minkprob}, Datamodels \cite{ilyas2022datamodels}, watermarks \cite{christ2024_undetectable}, and TROVE \cite{zhu2025_trove} address
…[truncated 748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1793 · 2026-05-25T21:14:17.731066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1794 · 2026-05-25T21:14:17.782242+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	We use \emph{depth estimation} as shorthand throughout; the underlying task is ordinal classification.
13	Depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
14	
15	\subsection{Multi-Generational Benchmark Construction}
16	\label{sec:method:benchmark}
17	
18	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
19	
20	\paragraph{Model families.}
21	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
22	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
23	
24	\paragraph{Decoding strategies.}
25	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
26	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
27	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
2
…[truncated 7246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1795 · 2026-05-25T21:14:26.992623+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's comprehensive information about EMNLP 2026 ARR call for papers, submission deadline, and author guidelines:

## ARR Submission Deadline

The ARR subm
…[truncated 2212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 10267
}
```

</details>

---


### Tool call

_source line 1796 · 2026-05-25T21:14:37.452144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 1797 · 2026-05-25T21:14:37.854469+00:00_

1	\subsection{Theoretical Motivation}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed jointly with surprisal variance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\gamma^k$ for a contraction factor $\gamma \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction ratios (0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5, averaged across three models under nucleus; \S\ref{sec:atlas:edd}) are consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--81\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\gamma$ closer to 1), predicting weaker per-step signal.
15	Qwen2.5-14B supports this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.98$ at 1--1.5B; \S\ref{sec:gen:crossscale}); 7--8B results are mixed, and additional confounds likely interact with the scale effect (Appendix~\ref{app:cross_scale_full}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\gamma$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ 
…[truncated 415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1798 · 2026-05-25T21:14:37.854897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 1799 · 2026-05-25T21:14:37.955766+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells at the 1--1.5B parameter scale, evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% confidence interval (CI; ${\pm}$half-width; $B{=}10{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: mean absolute error (MAE)\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references
…[truncated 8117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1800 · 2026-05-25T21:14:38.056817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 1801 · 2026-05-25T21:14:38.107680+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares methods across all 9 cells.
10	Four classifiers (RF, XGBoost, ordinal multilayer perceptron (MLP), prototypical) converge within 0.8\,pp under cross-model transfer (Appendix~\ref{app:learned_estimator}), which confirms a feature-determined accuracy ceiling.
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA, 53--61\%) and RoBERTa-DCOL (ordinal contrastive, 64.5\%) lag RF by 14--33\,pp; note that RF features access reference-model log-probabilities unavailable to end-to-end pretrained language model (PLM) baselines (\S\ref{sec:discussion}).
14	
15	\paragraph{Binary detectors and membership inference.}
16	Perturbation-based (DetectGPT, 28.8\%) and membership-inference (Min-K\% Prob, 33.2\%) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); Binoculars d1v2 AUC\,=\,0.50--0.53 vs.\ RF 0.93 (Appendix~\ref{app:detector_baselines}). Binoculars convergence with our pipeline is discussed in \S\ref{sec:discussion}.
17	
18	\paragraph{Surface-text ablation.}
19	Single-feature regression on mean perplexity (25.1\%) and zero-shot LLMs (best 36.2\%; Appendix~\ref{app:zeroshot_prompt}) confirm depth signal is inaccessible from surface text.
20	
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Method comparison (RF mean across 9 cells, 5-fold CV). Chance = 25\% / 33.3\% (d1--d3). $^\dagger$Adapted from binary detection; Binoculars 11-feat: $p{>}0.05$ vs.\ 19-feat RF (paired permutation test).}
25	\label{tab:baselines}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{@{}llcc@{}}
28	\toprule
29	Method & Calibration & 4-Cl (\%) & d1--d3 
…[truncated 4400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1802 · 2026-05-25T21:14:43.635048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1803 · 2026-05-25T21:14:43.786353+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	Four importance measures converge (Kendall's $W{=}0.90$); Binoculars cross-perplexity features independently reach 78.1\% (merged: 82.6\%; Appendix~\ref{app:feature_ablation_bino}); four classifiers converge within 0.8\,pp (\S\ref{sec:gen:baselines}; Appendix~\ref{app:learned_estimator}).
5	The accuracy ceiling resides in the feature space, not the classifier: future gains require richer distributional statistics rather than more expressive classifiers.
6	End-to-end classifiers lag by 14--33\,pp (d2 F1\,${\leq}$\,0.27; Appendix~\ref{app:e2e}, \ref{app:dcol_iterations}): depth manifests as a global distributional shift requiring explicit passage-level aggregation inaccessible to pretrained encoders (Appendix~\ref{app:feature_overlap}).
7	The strategy effect (9.3\,pp) exceeds the model effect (7.2\,pp), requiring decoding-conditioned deployment or two-stage routing (\S\ref{sec:gen:crossstrategy}; Appendix~\ref{app:extended_discussion}).
8	Reference-model mismatch costs 4--11\,pp (Appendix~\ref{app:ref_ablation}), and a 7B self-reference probe reveals a scale ceiling ($\mathrm{EDD}_{0.70}{=}0$; Appendix~\ref{app:qwen7b_selfref}).
9	Accumulation and cross-boundary experiments (84.8\%; Appendix~\ref{app:accumulation_auc},~\ref{app:cross_boundary}) confirm process-level depth fingerprints that persist under partial mixing and across model boundaries.
10	
11	\paragraph{Practical implications.}
12	Ordinal depth labels enable tiered curation, retaining $d{=}1$ text while filtering $d{\geq}2$; the lightweight pipeline (19 statistics, one 1.4B forward pass) supports inline deployment with ${\leq}$7\% calibrated false-positive rate (Appendix~\ref{app:calibration}).
13	Depth fingerprints are thus resolvable to $\mathrm{EDD}_{0.70}{=}3$ in 8/9 cells; scaling beyond 1.5B, paraphrase robustness, and curation remain open (Appendix~\ref{app:curation_poc}, \ref{app:downstream}).
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-25T21:14:43.786900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-25T21:14:43.839270+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our benchmark uses full-replacement chains at 1--1.5B parameters; real-world contamination involves accumulation at unknown mixing ratios (per-passage robustness in Appendix~\ref{app:mixed_depth}), and depth signal attenuates at larger scales (\S\ref{sec:gen:crossscale}), with reference-model mismatch contributing to the observed degradation (Appendix~\ref{app:cross_scale_full}).
5	Cross-strategy transfer can invert adjacent-depth predictions, requiring strategy-aware deployment (\S\ref{sec:gen:crossstrategy}).
6	On held-out web-crawl corpora, pooled-classifier raw false-positive rates range from 15\% to 34\%, reducible to ${\leq}$7\% via posterior-threshold calibration (Appendix~\ref{app:calibration}); robustness to post-hoc paraphrasing remains untested.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1806 · 2026-05-25T21:14:47.969507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1807 · 2026-05-25T21:14:48.271640+00:00_

1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale 7--8B experiments (Appendix~\ref{app:cross_scale_full}) use Quantized LoRA (QLoRA; 4-bit NF4) with $r{=}16$, $\alpha{=}32$; the 14B model uses FP16 LoRA with the same rank and scaling.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Feature trajectories for nucleus and temperature sampling appear in Figure~\ref{fig:feature_trajectory} (\S\ref{sec:atlas:edd}).
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the
…[truncated 5046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1808 · 2026-05-25T21:14:48.272338+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1809 · 2026-05-25T21:14:48.373408+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1810 · 2026-05-25T21:14:52.295558+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/recursive_gen_depth_est/docs/paper/references*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/recursive_gen_depth_est/docs/paper/references*"
  }
}
```

</details>

---


### Tool result

_source line 1811 · 2026-05-25T21:14:52.748387+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1812 · 2026-05-25T21:14:52.799009+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1813 · 2026-05-25T21:14:52.900331+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1814 · 2026-05-25T21:14:57.219833+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/recursive_gen_depth_est/docs/paper/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/recursive_gen_depth_est/docs/paper/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 1815 · 2026-05-25T21:14:57.220410+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1816 · 2026-05-25T21:14:57.220679+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/recursive_gen_depth_est/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/recursive_gen_depth_est/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1817 · 2026-05-25T21:14:57.271100+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1818 · 2026-05-25T21:15:00.790003+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/recursive_gen_depth_est/**/references*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/recursive_gen_depth_est/**/references*"
  }
}
```

</details>

---


### Tool result

_source line 1819 · 2026-05-25T21:15:01.292541+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1820 · 2026-05-25T21:15:01.343797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1821 · 2026-05-25T21:15:01.394602+00:00_

100	\paragraph{Consistency with Gini rankings.}
101	CPI and Gini rankings agree on the dominant feature (\texttt{var\_surprisal} or \texttt{p90\_ppl}) in 8/9 cells; the sole disagreement (GPT-2~XL top-$k$) involves a swap between rank-2 and rank-3 features.
102	Bootstrap rank CI widths $\leq 0.5$ for the top-2 features confirm that these rankings are not artifacts of collinearity or resampling variability.
103	Controlling for multicollinearity via conditional permutation corroborates the Gini- and SHAP-based importance hierarchy reported in the main text.
104	
105	\subsection{Per-Cell Gini Feature Rankings}
106	\label{app:gini_per_cell}
107	
108	\begin{table}[h]
109	\centering
110	\small
111	\caption{Top-5 features by Gini importance. \textbf{Bold}: top-2. \texttt{p90\_ppl} top-2 in 9/9; \texttt{var\_surprisal} 8/9 under SHAP (7/9 under Gini). Individual rankings are approximate due to multicollinearity (VIF${>}$10 for 14--16/19 features).}
112	\label{tab:feature_importance}
113	\resizebox{\columnwidth}{!}{%
114	\begin{tabular}{@{}l l@{}}
115	\toprule
116	Cell & Top-5 features (Gini importance, ranked) \\
117	\midrule
118	Pythia, nuc.       & \textbf{var\_surprisal\,(.17)}, \textbf{p90\_ppl\,(.15)}, mean\_ppl\,(.11), var\_ppl\,(.08), p75\_ppl\,(.07) \\
119	Pythia, $\tau$     & \textbf{var\_surprisal\,(.17)}, \textbf{p90\_ppl\,(.14)}, mean\_ppl\,(.11), p75\_ppl\,(.07), mean\_surprisal\,(.07) \\
120	Pythia, top-$k$    & \textbf{var\_surprisal\,(.16)}, \textbf{p90\_ppl\,(.12)}, mean\_ppl\,(.11), var\_ppl\,(.07), mean\_surprisal\,(.06) \\
121	GPT-2\,XL, nuc.    & \textbf{var\_surprisal\,(.21)}, \textbf{p90\_ppl\,(.21)}, p75\_ppl\,(.10), mean\_surprisal\,(.07), mean\_ppl\,(.06) \\
122	GPT-2\,XL, $\tau$  & \textbf{p90\_ppl\,(.25)}, \textbf{p75\_ppl\,(.15)}, mean\_surprisal\,(.13), var\_surprisal\,(.12), p50\_ppl\,(.05) \\
123	GPT-2\,XL, top-$k$ & \textbf{p90\_ppl\,(.24)}, \textbf{p75\_ppl\,(.12)}, var\_surprisal\,(.10), mean\_surprisal\,(.09), type\_token\_ratio\,(.04) \\
…[truncated 10449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1822 · 2026-05-25T21:15:07.473328+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1823 · 2026-05-25T21:15:07.929247+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/decisions.yaml\", \"content\": \"_next_id: 53\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 14:03 UTC\\n  summary: MVP PASS — 递归生成深度可从统计特征高精度区分，进入 research phase\\n  rationale: Pythia-1.4B 4-depth pipeline 验证核心假设：4-class acc 78.2% (>>40% threshold),\\n    d1v2 AUC 0.861 (>>0.6 threshold)。控制实验排除域混淆（过滤代码后 acc 提升至 81.6%）。Top 特征为 surprisal\\n    variance 和 perplexity percentiles，说明信号来自分布窄化而非内容差异。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_pythia_002\\n    role: primary\\n    result: 4-class acc 78.2%, d1v2 AUC 0.861, content-type control 81.6%\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:01 UTC\\n  summary: Dream 三档分析完成：6项结构性必修+framing重心从DCOL转向Atlas/EDD\\n  rationale: Dream dream_20260514T140607 full review 完成。三档(best=borderline accept\\n    3.0, median=Findings 3.0, worst=borderline Findings 2.5)一致指出6项结构性问题：(1)DCOL loss\\n    Eq.1缺repulsive term不可复现 (2)Atlas论文零图不可接受 (3)bibliography严重不足(3-10 refs,需25+) (4)d0\\n    confound膨胀headline metrics,需报d1-d5 acc (5)EDD threshold无sensitivity analysis (6)surprisal\\n    reference model未指定有circularity风险。三档均认为Atlas/EDD是primary contribution,DCOL incremental\\n    over CLOC——与我们的contingency plan方向一致。worst case下DCOL不显著(p=0.12),EDD=2,但任务formalization+Atlas仍可支撑Findings。关键风险：cross-model\\n    transfer在worst case降到33%。\\n  related_experiments:\\n  - exp_id: dream_20260514T140607\\n    role: dream_simulation\\n    result: best=3.0 median=3.0 worst=2.5\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 19:45 UTC\\n  summary: 要求 baselines 统一使用 DeBERTa-v3-large，消除与 DCOL 的模型规模混淆变量\\n  rationale: Reviewer 发现 DCOL 用 DeBERTa-v3-large (435M) 而 CE/CORAL baselines 用 DeBERTa-v3-base\\n    (184M)，参数量差 2.4×，审稿人必问改进来源。修改 baseline 脚本支持 large 版本实验成本极低（模型已在服务器上），可彻底解耦方法贡献与模型容量。\\n  related_experiments:\\n  - exp_id: dcol_deberta_001\\n    role: target\\n    result: pending\\n  depends_on: []\\n- id: D00
…[truncated 1450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 1824 · 2026-05-25T21:15:09.085049+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1825 · 2026-05-25T21:15:09.388282+00:00_

&lt;persisted-output>
Output too large (66.8KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-director-79bccd15/4acb560f-4f49-4666-8e98-2ac0c772301d/tool-results/toolu_01JBiKMfG1idW4EexTUZ4jEZ.txt

Preview (first 2KB):
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/feishu_group_oc_db3bd143165620ee6950e6ef0826eec8_director.jsonl
…[truncated 55 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-25T21:15:13.667792+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/agent",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/agent",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1827 · 2026-05-25T21:15:13.769147+00:00_

&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_director_79bccd15.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1828 · 2026-05-25T21:15:17.850946+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1829 · 2026-05-25T21:15:17.951795+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1830 · 2026-05-25T21:15:21.520684+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/recursive_gen_depth_est/**/config*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/recursive_gen_depth_est/**/config*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1831 · 2026-05-25T21:15:21.621768+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1832 · 2026-05-25T21:15:24.489349+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/recursive_gen_depth_est/config*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/recursive_gen_depth_est/config*"
  }
}
```

</details>

---


### Tool result

_source line 1833 · 2026-05-25T21:15:24.489925+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1834 · 2026-05-25T21:15:47.849610+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1835 · 2026-05-25T21:16:02.496236+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 14646
}
```

</details>

---


### Tool call

_source line 1836 · 2026-05-25T21:16:02.952057+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责**方法严谨性、实验设计、统计方法和可复现性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, 8 页正文限制, double-blind\n- **匿名规则**: Double-blind (作者信息已隐藏)\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_17/submitted.pdf`\n\n## 审查侧重\n\n请重点评估以下方面：\n\n1. **实验设计**：benchmark 构建是否有方法论缺陷（数据泄露、confounds、选择偏差）？full-replacement chain 设定与 real-world scenario 的 gap 是否被充分讨论？\n2. **统计方法**：RF 分类器选择是否合理？EDD 指标定义是否严谨？AUC 评估、bootstrap CI、多重比较校正是否恰当？\n3. **可复现性**：超参数、数据规模、随机种子是否充分报告？代码/数据匿名链接是否可用？\n4. **Reference model confound**：Pythia 同时作为 generator 和 reference model 的自引用优势（4-11pp）是否被充分控制和讨论？\n5. **Cross-scale validity**：14B 结果 EDD=0 (self-ref) / EDD=2 (cross-ref) 的矛盾如何解释？scale attenuation 的讨论是否充分？\n6. **Feature multicollinearity**：19 特征中 14-16 个 VIF>10，这对 feature importance 排名的可靠性有何影响？conditional permutation importance 是否充分缓解？\n\n请输出完整审稿意见，包含 Summary、Strengths、Weaknesses（逐条编号，标注严重程度 [Critical/Major/Minor]）、Questions to Authors。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责**方法严谨性、实验设计、统计方法和可复现性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, 8 页正文限制, double-blind\n- **匿名规则**: Double-blind (作者信息已隐藏)\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_17/submitted.pdf`\n\n## 审查侧重\n\n请重点评估以下方面：\n\n1. **实验设计**：benchmark 构建是否有方法论缺陷（数据泄露、confounds、选择偏差）？full-replacement chain 设定与 real-world scenario 的 gap 是否被充分讨论？\n2. **统计方法**：RF 分类器选择是否合理？EDD 指标定义是否严谨？AUC 评估、bootstrap CI、多重比较校正是否恰当？\n3. **可复现性**：超参数、数据规模、随机种子是否充分报告？代码/数据匿名链接是否可用？\n4. **Reference model confound**：Pythia 同时作为 generator 和 reference model 的自引用优势（4-11pp）是否被充分控制和讨论？\n5. **Cross-scale validity**：14B 结果 EDD=0 (self-ref) / EDD=2 (cross-ref) 的矛盾如何解释？scale attenuation 的讨论是否充分？\n6. **Feature multicollinearity**：19 特征中 14-16 个 VIF>10，这对 feature importance 排名的可靠性有何影响？conditional permutation importance 是否充分缓解？\n\n请输出完整审稿意见，包含 Summary、Strengths、Weaknesses（逐条编号，标注严重程度 [Critical/Major/Minor]）、Questions to Authors。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1837 · 2026-05-25T21:16:15.341204+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12389
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-25T21:16:15.493403+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责**新颖性、贡献完整性、相关工作覆盖和 claims 与证据匹配**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, 8 页正文限制, double-blind\n- **匿名规则**: Double-blind (作者信息已隐藏)\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_17/submitted.pdf`\n\n## 审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性**：recursive generation depth estimation 作为新任务的定义是否具有足够的学术贡献？EDD 指标相对于现有评估指标（如 AUC、accuracy）有何独特价值？与 model collapse 文献的区分是否清晰？\n2. **Claims vs Evidence**：\n   - \"perplexity tail features dominate\" — 是否有足够的 ablation 和 alternative explanation 排除？\n   - \"decoding strategy > model architecture\" (9.3pp vs 7.2pp) — 样本量（3×3 grid）是否足以支撑此 claim？\n   - \"EDD_0.70 = 3 in 8/9 cells\" — threshold 选择 (0.70) 的理由是否充分？\n   - \"signal attenuates with scale\" — 仅测了 14B 一个点，claim 的泛化性如何？\n3. **相关工作覆盖**：\n   - 是否遗漏重要的 model collapse / synthetic data detection 文献？\n   - 与 EditLens、TROVE、data provenance 方向的区分是否充分？\n   - 2025-2026 最新工作是否覆盖？\n4. **贡献完整性**：Discussion 和 Limitations 是否诚实地承认了方法的边界条件？partial-mixing 实验是否足以弥合 full-replacement 与 real-world 的鸿沟？\n5. **写作质量**：abstract 是否在 200 words 以内？结构是否清晰？notation 是否一致？\n\n请输出完整审稿意见，包含 Summary、Strengths、Weaknesses（逐条编号，标注严重程度 [Critical/Major/Minor]）、Questions to Authors、Missing References（如有）。",
  "reviewer_id": "2",
  "project": "recursive_gen_depth_est",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责**新颖性、贡献完整性、相关工作覆盖和 claims 与证据匹配**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, 8 页正文限制, double-blind\n- **匿名规则**: Double-blind (作者信息已隐藏)\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_round_17/submitted.pdf`\n\n## 审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性**：recursive generation depth estimation 作为新任务的定义是否具有足够的学术贡献？EDD 指标相对于现有评估指标（如 AUC、accuracy）有何独特价值？与 model collapse 文献的区分是否清晰？\n2. **Claims vs Evidence**：\n   - \"perplexity tail features dominate\" — 是否有足够的 ablation 和 alternative explanation 排除？\n   - \"decoding strategy > model architecture\" (9.3pp vs 7.2pp) — 样本量（3×3 grid）是否足以支撑此 claim？\n   - \"EDD_0.70 = 3 in 8/9 cells\" — threshold 选择 (0.70) 的理由是否充分？\n   - \"signal attenuates with scale\" — 仅测了 14B 一个点，claim 的泛化性如何？\n3. **相关工作覆盖**：\n   - 是否遗漏重要的 model collapse / synthetic data detection 文献？\n   - 与 EditLens、TROVE、data provenance 方向的区分是否充分？\n   - 2025-2026 最新工作是否覆盖？\n4. **贡献完整性**：Discussion 和 Limitations 是否诚实地承认了方法的边界条件？partial-mixing 实验是否足以弥合 full-replacement 与 real-world 的鸿沟？\n5. **写作质量**：abstract 是否在 200 words 以内？结构是否清晰？notation 是否一致？\n\n请输出完整审稿意见，包含 Summary、Strengths、Weaknesses（逐条编号，标注严重程度 [Critical/Major/Minor]）、Questions to Authors、Missing References（如有）。",
    "reviewer_id": "2",
    "project": "recursive_gen_depth_est",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1839 · 2026-05-25T21:16:17.048222+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1554
}
```

</details>

---


### Assistant

_source line 1840 · 2026-05-25T21:16:21.971175+00:00_

Round 1 已启动：

- 视觉审查 Agent：已派发（并行运行，不阻塞）
- Reviewer 1（方法严谨性）：已分配
- Reviewer 2（新颖性/完整性）：已分配

等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 158

## Round 158

2 recorded events


### User

_source line 1841 · 2026-05-25T21:23:47.530168+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Round 1

**论文标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 新颖性、贡献完整性、相关工作覆盖、Claims vs Evidence

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 任务定义新颖、实验覆盖面广，但多个核心 claim 的统计支撑不足以匹配其表述强度，且 full-replacement 实验设定与真实场景之间的鸿沟未被充分弥合。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主要贡献（任务定义 + benchmark + 特征有效性）有充分支撑；但 "decoding > architecture"、"signal attenuates with scale" 等比较性 claim 的统计证据不足 |
| Excitement | 3/5 (Interesting) | 任务定义有新意，但受限于 full-replacement 实验设定，实际应用前景不明朗；方法本身（RF + 手工特征）缺乏技术深度上的兴奋点 |
| Confidence | 4/5 | 仔细阅读全文含 26 页附录，熟悉 model collapse、AI text detection、ordinal classification 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] "Decoding strategy contributes at least as much as model architecture" — 9 个 cell 无法支撑此 claim

- 具体位置：Abstract 第 6 句、Section 4.1 第 3 段、Section 6 第 2 句
- 问题：该 claim 基于 3×3 grid 的均值比较（within-model strategy gap 9.3pp vs. within-strategy model gap 7.2pp），但仅有 9 个 cell，且未对 9.3 vs. 7.2 的差异进行任何统计检验（如 paired permutation test 或 bootstrap CI on the difference）。Abstract 中 "decoding strategy effects cross-condition transfer more than model architecture" 的措辞暗示了一个排序关系，而非仅仅是 "comparable"。在如此小的样本上，2.1pp 的差异完全可能是噪声。
- 为什么影响接收：这是论文三大 findings 之一（Finding 2），也是 abstract 的核心 claim。如果此 claim 不成立，论文的贡献叙事需要重构。
- 建议修改方向：(1) 对 9.3 vs. 7.2 的差异提供 bootstrap CI 或置换检验 p 值；(2) 如果不显著，将措辞改为 "decoding strategy and model architecture contribute comparably"，删除 "more than" 的排序暗示；(3) 考虑增加更多 model family 或 decoding strategy 以增加统计功效。

**N2** [Critical] Scale generalization claim 证据薄弱——"signal attenuates with scale" 基于极有限的数据点

- 具体位置：Abstract 第 7 句、Section 5.4、Appendix B.18–B.19
- 问题：主 benchmark 仅覆盖 1–1.5B（3 个模型）。7–8B 实验（Appendix B.18, Table 19）包含 Llama-3.1-8B 和 Qwen2.5-7B 两个模型，仅用 nucleus sampling，accuracy 从 ~80% 降至 ~70%。14B 实验（Appendix B.19）仅测了 Qwen2.5-14B 一个模型（且用 QLoRA 而非 full LoRA）。从 3 个 1.5B 模型 + 2 个 7–8B 模型 + 1 个 14B 模型推断 "signal attenuates with scale" 的单调趋势，数据点严重不足。更重要的是，reference model 始终固定为 Pythia-1.4B——当目标模型为 14B 时，reference model 比目标小一个数量级，perplexity 特征的语义可能已经改变。Appendix B.19 自己承认 "the U-shaped pattern at Qwen2.5-7B likely originates from the cross-reference setup"，说明 reference model confound 未解决。
- 为什么影响接收：Scale generalization 是论文的第三个核心 finding，也是 Limitations 和 Discussion 的重要支撑。如果 attenuation 部分来自 reference model mismatch 而非 scale 本身，则因果推断不成立。
- 建议修改方向：(1) 至少在 7B 尺度用匹配规模的 reference model（如 Llama-3.1-8B 做 reference）复现实验，分离 scale effect 和 reference mismatch effect；(2) 或将 "signal attenuates with scale" 从 finding 降级为 preliminary observation，在 abstract 中用更审慎的语言。

**N3** [Critical] Full-replacement 假设与真实场景的鸿沟未被充分弥合

- 具体位置：Section 3.2（benchmark 构造）、Section 5.3（partial-mixing）、Limitations
- 问题：整个 benchmark 基于 full-replacement chain（每代 100% 替换训练数据）。现实中的 recursive contamination 是 partial mixing（如 Common Crawl 中混入不同比例的 AI 生成文本）。论文的 partial-mixing 实验（Section 5.3）仅测了 3 个 model-strategy cell（不是全部 9 个）、2 个混合比例（25%、50%），且 Table 10 显示 50% mixing 下 GPT-2 XL 已经失败（EDD 降至 <3）。这意味着：(a) partial-mixing 的覆盖面太窄，无法得出鲁棒结论；(b) 即使在最简单的 partial-mixing 设定下（已知比例、仅两个比例点），部分 cell 已经 break down。
- 为什么影响接收：论文在 Introduction 中动机段（"real-world contamination involves partial mixing at unknown mixing ratios"）承诺了对真实场景的适用性，但实验未能交付。审稿人会质疑：如果连 50% mixing 的控制实验都有 cell 失败，该方法在未知比例的真实场景中能否工作？
- 建议修改方向：(1) 将 partial-mixing 实验扩展到全部 9 个 cell，增加更多比例点（10%, 25%, 50%, 75%）；(2) 或者在 Introduction 中降低对真实场景适用性的暗示，明确将 full-replacement 作为 scope boundary；(3) 讨论从 full-replacement 到 partial-mixing 的 accuracy degradation 曲线是否有规律可循。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] EDD 指标的新颖性和独特价值论证不充分

- 具体位置：Section 3.4（Definition 1）、Section 4.3
- 问题：EDD 本质上是对 pairwise AUC 曲线设定阈值 τ 后取最大连续深度——这在技术上是一个简单的阈值操作，而非独立的 metric contribution。论文未与其他可能的 "depth discriminability" 度量做比较（如：基于 accuracy 的版本、基于 effect size 的版本、基于 information-theoretic 的版本）。τ = 0.70 的选择虽然引用了 Hosmer & Lemeshow (2000) 的 "acceptable discrimination" 标准，但该标准原本用于 binary logistic regression 的 ROC 分析，直接移植到 ordinal depth estimation 的 pairwise AUC 场景是否合理未做论证。Section 3.4 的 sensitivity analysis（τ ∈ {0.65, 0.70, 0.80}）仅展示了 EDD 值的变化，未讨论哪个 τ 最适合深度估计的实际应用。
- 建议：(1) 更明确地论证为什么 EDD 优于直接报告 per-pair AUC 曲线或 4-class accuracy；(2) 讨论 τ 选择对下游决策的影响；(3) 至少比较一个替代 metric 定义。

**W2** [Major] PLM baseline 比较可能不公平

- 具体位置：Section 5.1、Appendix B.13–B.14
- 问题：论文声称 "statistical features outperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations"（Section 5.1）。但 PLM baseline 仅使用 frozen CLS representations + linear probing（DeBERTa-v3-base, RoBERTa-base），以及 DCOL（fine-tuned but ordinal MLP）。这些 baseline 的能力上限远低于 fine-tuned PLM。Appendix B.13 显示 DCOL fine-tuned 到 64.5%（vs. RF 的 ~80%），但 DCOL 使用的是 ordinal loss + 小 MLP，而非充分 fine-tuned 的 encoder。论文没有测试 full fine-tuning of DeBERTa/RoBERTa on the ordinal task。这使得 "statistical features > PLM representations" 的 claim 可能仅反映 baseline 设计的弱点，而非方法本身的优势。
- 建议：(1) 增加 full fine-tuned DeBERTa-v3 baseline；(2) 或将 claim 弱化为 "statistical features outperform frozen PLM representations"，明确限定比较范围。

**W3** [Major] Seed corpus 单一性可能夸大特征一致性

- 具体位置：Section 3.2 第 1 段、Section 5.2
- 问题：Benchmark 全部基于 Wikipedia seed corpus（共享 seed corpus across all cells）。虽然 Section 5.2 测试了 cross-domain transfer（WikiText-103 → 其他域），但核心 benchmark 的 domain 同质性可能导致 perplexity tail 特征的 consistency 被高估。Table 4 的 cross-domain 结果（mean accuracy 66.4%）显著低于 in-distribution（~80%），下降超 14pp，说明 domain 是重要变量。此外，Wikipedia 文本风格相对统一（百科全书体），可能不代表 AI 生成文本在对话、创意写作、代码等多样化场景中的行为。
- 建议：在主 benchmark 中加入至少一个非 Wikipedia domain（如 news、Reddit、arXiv abstracts）作为对照。

**W4** [Minor] LoRA fine-tuning 作为 recursive training 的代理可能引入系统性偏差

- 具体位置：Section 3.2（Generation pipeline）、Appendix A
- 问题：Recursive chain 的每一代使用 LoRA fine-tuning（r=16, α=32）而非 full fine-tuning。LoRA 的低秩约束限制了模型权重的变化幅度，可能导致相邻深度之间的 distributional shift 被人为压缩（因为 LoRA 只更新少量参数）。这意味着论文观察到的 "depth signal concentrates in perplexity tails" 可能部分是 LoRA 的 artifact——如果用 full fine-tuning，distributional shift 可能更显著或呈现不同模式。论文未讨论 LoRA rank 的选择对 depth signal 的影响。
- 建议：(1) 讨论 LoRA rank 选择的合理性和潜在影响；(2) 在至少一个 cell 上用 full fine-tuning 对比验证深度信号是否一致。

---

## 小问题（不影响接收）

- **M1**: Table 2 脚注 5（"Statistical tests are not corrected for multiple comparisons; p-values should be interpreted as exploratory"）——考虑到论文有 9 个 cell 的多重比较，建议应用 Bonferroni 或 FDR correction 并在正文中报告 corrected p-values，而非仅在脚注声明 exploratory。
- **M2**: Figure 2（feature importance heatmap）的颜色编码不够直观——星号标记的 top-7 features 与颜色深度之间的对应关系需要在 caption 中更清楚地说明。
- **M3**: Section 3.3 中 "effective independent dimensionality is ≈4–5" 的 VIF 分析结论很有价值，但正文中没有给出 VIF 的具体数值范围，仅在 Appendix 中提及 VIF>10 的标准。建议在正文中至少报告 top features 的 VIF 值。
- **M4**: Appendix B.14 提到 domain bias analysis 中发现了 initial implementation bug（"we discovered the issue during internal review, corrected to per-depth seed group assignment"）——这种诚实值得赞赏，但建议更明确地说明 bug 对已报告结果的影响范围。
- **M5**: Abstract 约 185 words，符合 200-word 限制。✓

---

## Questions to Authors

**Q1**: 对于 N1 中的 "decoding > architecture" claim——能否提供 9.3pp vs. 7.2pp 差异的 bootstrap 95% CI？如果 CI 包含 0，是否愿意将 claim 改为 "comparable"？

**Q2**: 对于 N2——如果使用 7B 模型（如 Llama-3.1-8B）作为 reference model 来评估 7B 目标模型，depth signal 的 attenuation 幅度是否会显著减小？这能否区分 "scale effect" 和 "reference mismatch effect"？

**Q3**: Partial-mixing 实验（Section 5.3, Table 10）中，GPT-2 XL 在 50% mixing 下 EDD 降至 <3。能否报告 25% mixing 下全部 9 个 cell 的 EDD 值，而非仅 3 个 cell？

**Q4**: 论文使用 LoRA (r=16) 作为 recursive fine-tuning 的代理。是否考虑过 LoRA rank 是 depth signal 强度的一个混淆变量？如果用 r=4 或 r=64，EDD 值是否会显著变化？

**Q5**: EDD metric 的实际应用场景是什么？在什么下游任务中，知道 "EDD = 3" 比知道 "4-class accuracy = 80%" 更有价值？

**Q6**: Section 5.1 的 PLM 比较中，为什么没有测试 full fine-tuned DeBERTa 或 RoBERTa？在参数量可比的前提下（RF 的 19 features vs. 110M DeBERTa），feature-based 方法的优势是否依然成立？

---

## Missing References（建议补充）

1. **Stylometric analysis 传统**：论文使用的 19 个统计特征与 stylometry / authorship attribution 文献中的特征高度重叠（如 n-gram 分布、perplexity、type-token ratio）。建议引用 stylometry 综述以定位贡献——如 Stamatatos (2009) "A Survey of Modern Authorship Attribution Methods" 或 Neal et al. (2017)。这能帮助读者理解为什么这些特征对 depth 有效：recursive generation 可能在 stylometric space 中产生可检测的轨迹。

2. **Ordinal classification 方法论**：论文使用 Random Forest 做 ordinal classification，但未引用 ordinal-specific ensemble 方法（如 Frank & Hall, 2001 "A Simple Approach to Ordinal Classification" 已引用 ✓）。不过 Appendix B.25 中对比的 learned estimator 方法较少——可以考虑引用更多 ordinal regression baselines。

3. **Iterative self-improvement / self-play 文献**：如 Chen et al. (2024) "Self-Play Fine-Tuning" 或 Yuan et al. (2024) "Self-Rewarding Language Models"——这些工作产生的 iterative training 与论文的 recursive generation chain 结构相似，但动机不同（improvement vs. degradation），可作为 related work 的对比。

---

## 主要优势

1. **任务定义的原创性**：将 recursive generation depth 从 model collapse 研究中抽离出来，独立定义为 ordinal classification 问题，填补了 binary detection 和 model collapse theory 之间的空白。这个定义是清晰的、可操作的、可复现的。

2. **实验覆盖面极为扎实**：26 页论文中 17 页为附录，涵盖了 feature ablation（B.1–B.4）、cross-model transfer（B.7）、accumulation AUC（B.8）、DCOL iteration（B.9）、zero-shot LLM（B.10）、temperature robustness（B.11）、PLM comparison（B.12–B.14）、domain bias（B.14）、wild-data calibration（B.15）、curation PoC（B.16）、reference model ablation（B.17）、7–14B scale（B.18–B.19）、cross-boundary（B.20）、cross-seed（B.21）、depth-4 extension（B.22）、mixed-depth corpus（B.24）、generation length（B.24）、learned estimator（B.25）、1.5B instruction-tuned（B.26）、fine-tuning probe（B.27）、feature group ablation（B.28）、RF seed robustness（B.29）、binary detector baseline（B.30）、Binoculars decomposition（B.31）、prompted generation（B.32）、extended discussion（B.33）。这种程度的实验覆盖远超多数 EMNLP submissions。

3. **Feature importance 分析的多角度验证**：permutation importance、Gini importance、CPI（conditional）、SHAP 四种方法的一致性增强了 "perplexity tail features dominate" 这一 claim 的可信度。

4. **诚实的 limitations 讨论**：论文在 Limitations 和 Appendix B.33 中坦承了 full-replacement assumption、scale limitation、reference model dependency 等问题，没有回避。Appendix B.14 甚至主动披露了 implementation bug 的发现和修正过程。

5. **Benchmark 构造的方法论规范**：shared seed corpus、cross-validation splits do not leak across depths、leave-one-group-out evaluation——这些设计选择表明作者对实验严谨性的关注。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1842 · 2026-05-25T21:23:58.970559+00:00_

Reviewer 2 审稿意见已收到。评分 3.5 (Borderline Conference)，提出 3 个 Critical issues（decoding > architecture claim 统计支撑不足、scale generalization 证据薄弱、full-replacement 与真实场景鸿沟）和 3 个 Major issues。

等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 159

## Round 159

2 recorded events


### User

_source line 1843 · 2026-05-25T21:24:12.968315+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论概要**：Overall 3.5（Borderline Conference），Soundness 3/5，Excitement 3/5。

三个 Critical 问题：
1. **"Decoding > architecture" claim 缺乏统计检验**——9 个 cell 上 9.3pp vs 7.2pp 的差异未做任何显著性检验，无法支撑 abstract 中的排序性 claim
2. **Scale generalization 证据薄弱**——仅 1–1.5B 充分测试，7–14B 只有 3 个模型且 reference model confound 未解决
3. **Full-replacement 与真实场景的鸿沟**——partial-mixing 实验仅覆盖 3/9 cells × 2 比例点，50% mixing 下已有 cell 失败

三个 Major 问题：EDD 指标新颖性论证不足、PLM baseline 比较可能不公平（仅测 frozen representation）、seed corpus 单一性可能夸大特征一致性。

主要优势：任务定义原创、实验覆盖面极广（17 页附录）、feature importance 多角度交叉验证、limitations 讨论诚实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1844 · 2026-05-25T21:24:22.200027+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 160

## Round 160

6 recorded events


### User

_source line 1845 · 2026-05-25T21:25:30.584366+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 方法严谨性、实验设计、统计方法、可复现性

---

## 总体评分
**Overall Assessment**: 3.0 / 5（Findings）
**一句话总结**: 问题形式化新颖且 atlas 设计系统，但 reference model confound 贯穿全部实验、full-replacement 假设远离真实场景、14B 规模信号消失——三个核心问题叠加后，方法的实际价值和可靠性存疑，尚不足以进入主会议。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | Reference model confound 系统性膨胀 Pythia cells 结果；full-replacement 链与现实 gap 大且仅测 25-50% mixing；多重比较未校正（脚注3承认）；VIF>10 的 14-16/19 特征使 feature importance 排名不可靠 |
| Excitement | 3.5 / 5 | 问题形式化（递归深度估计 vs. 二分检测）确实新颖；EDD 指标有设计感；atlas 概念系统。但 14B 信号消失和 full-replacement 假设严重限制实际影响力 |
| Reproducibility | 4.0 / 5 | 超参数、种子（42/43/45）、硬件（2×RTX PRO 6000, 200 GPU-hours）、匿名代码/数据链接均有报告；cross-seed replication（B.29）覆盖 3 个种子 |
| Confidence | 4 / 5 | 全文含 18 页 appendix 通读，熟悉 model collapse、统计检验、RF multicollinearity 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] **Reference Model Confound 贯穿全部实验设计**
- 具体位置：§3.3 (p.4)、Table 2 (p.5)、Appendix B.17 (Table 18)、B.19 (Table 22)
- 问题：Pythia-1.4B 同时作为 3 个 generator 之一和全部 19 个特征的固定 reference model。自引用优势 4-11 pp（B.17: self=78.5% vs. GPT-2 XL cross=67.3%）。12/19 特征依赖 reference model 的 log-probability，这不是边际偏差，而是系统性地膨胀了 Pythia cells 的所有指标。论文虽在 §3.3 用 † 标记并在 Limitations 提及，但 Pythia 结果仍被纳入 Table 2 全部聚合统计（atlas 均值、feature importance 排名、EDD 分布）。更关键的是，B.19 的 14B 实验揭示了一个根本矛盾：Qwen2.5-14B self-reference EDD₀.₇₀ = 0（d0v1 AUC 仅 0.56-0.64），而 cross-reference（Pythia-1.4B）EDD₀.₇₀ = 2（d0v1 AUC 升至 0.70-0.74）。同一文本、同一特征集，仅改变 reference model 就使 EDD 从 0 跳到 2——这说明 EDD 度量的不是文本的内在深度属性，而是 reference model 与 generator 的兼容性。
- 为什么影响接收：论文的核心 claim（"statistical fingerprints of recursive depth"）建立在特征能反映文本内在属性的假设上。Reference model confound 使这一假设不成立。
- 建议修改方向：(a) 在 atlas 聚合统计中排除 Pythia self-reference cells 或单独报告；(b) 至少对一个 non-Pythia generator 使用两个不同 reference model 做 cross-validation；(c) 在主文而非仅 appendix 讨论 14B EDD 悖论及其对 "intrinsic depth signal" claim 的影响；(d) 考虑在 model-free 特征（7个 lexical/repetition 特征）上单独报告性能下界。

**N2** [Critical] **Full-Replacement Chain 与现实场景的生态有效性 Gap 严重且讨论不足**
- 具体位置：§3.2 (p.3)、§5.3 (p.8)、Appendix B.8 (Table 10)、Limitations (p.9)
- 问题：Atlas 使用 100% 合成替换构建递归链——每一深度完全替换上一深度语料。真实 web 递归污染的混合比例远低于此（估计 5-30%）。§5.3 仅测试了 25% 和 50% 两个混合比例，结果已显示 8-15 pp 准确率衰减。50% mixing 下 GPT-2 XL d2v3 AUC=0.695 已低于 T=0.70 阈值（EDD 降级）。5-10% mixing 完全未测试——考虑到 25%→50% 的衰减趋势，信号可能在更低比例下消失。论文在 Limitations（p.9 第1段）仅用一句话提及 "real-world contamination involves accumulation at unknown mixing ratios"，未量化这一 gap 或讨论其对所有实验结论的影响。
- 为什么影响接收：如果方法在真实污染比例（<10%）下不工作，180K-cell atlas 的全部结论仅适用于一个人工设定，学术贡献受限。
- 建议修改方向：(a) 补充 5% 和 10% mixing ratio 实验；(b) 建立 mixing ratio vs. signal strength 的衰减曲线并外推下界；(c) 在主文明确讨论 full-replacement 设定的适用范围和局限。

**N3** [Major] **14B 规模信号消失与 Scale Attenuation 讨论不充分**
- 具体位置：§5.4 (p.8)、Appendix B.18 (Table 19)、B.19
- 问题：Qwen2.5-14B self-reference EDD₀.₇₀ = 0，四分类准确率 50.8%（仅 2× chance）。d0v1 AUC 在三种策略下均低于 0.70（nucleus: 0.643, temp: 0.632, top-k: 0.561）。7-8B 结果混合：Llama-3.1-8B 单调衰减（d0v1=0.949→d4v5=0.618），Qwen2.5-7B 呈 U 型恢复（d0v1=0.969, d2v3=0.709, d4v5=0.772）——两个模型在同一规模上行为完全不同，无法得出一般性结论。论文在 §3.5 用 model collapse theory 解释 scale attenuation（γ→1 时 per-step 信号变弱），但这一理论预测的是 monotonic 衰减，不能解释 Qwen-7B 的 U 型 AUC 曲线。更重要的是：当前主流 LLM（7B-70B+）正处于信号衰减区间，方法的实际部署价值需要正视。
- 为什么影响接收：scale limitation 是论文实际影响力的核心瓶颈。如果仅在 1-1.5B 工作，贡献范围有限。
- 建议修改方向：(a) 解释 Qwen-7B U 型曲线与 model collapse theory 预测不一致的原因；(b) 讨论是否可以通过更大/更小的 reference model 缓解 14B 信号消失；(c) 在 abstract/introduction 中明确方法的 scale 适用范围。

**N4** [Major] **Feature Multicollinearity 对 Importance 排名可靠性的影响**
- 具体位置：§4.2 (p.6)、Table 1 (p.4)、Appendix B.3 (Table 6-7)
- 问题：19 个特征中 14-16 个 VIF > 10，有效独立维度仅 4-5。在此极端多重共线性下：(a) Gini importance 已知会偏向高基数连续变量（Strobl et al., 2007, 2008 在论文中已引用但未充分讨论此 bias）；(b) CPI 通过 conditional permutation 部分缓解，但当 14-16/19 个特征都在一个相关簇中时，CPI 的 "within-group permutation" 的组定义本身就有问题；(c) Rank 4-5 的 bootstrap CI width 达 2.7-3.7（B.3 Table 6），确认 top-2 之外排名不稳定。Group-level ablation（§4.2：perplexity alone 76.6%）比个体排名更可靠，但论文中多处（§4.3 "p90_ppl dominates at deeper depths", §4.4 strategy-dependent trajectories）依赖个体特征排名做因果叙事。
- 为什么影响接收：Feature importance 叙事是论文三大发现之一（"depth signal concentrates in perplexity distribution tails"）。如果排名不可靠，这一发现的置信度下降。
- 建议修改方向：(a) 在主文报告 group-level ablation 作为 primary evidence，个体排名作为 secondary；(b) 对 rank 3+ 的特征明确标注 "unstable under multicollinearity"；(c) 考虑使用 elastic net 或 LASSO 做特征选择作为补充验证。

**N5** [Major] **多重比较未校正**
- 具体位置：脚注 3（§3.4, p.5）、B.15（p.16）
- 问题：论文明确承认 "Statistical tests are not corrected for multiple comparisons; p-values should be interpreted as exploratory"。但实际论文中有大量比较：9 cells × 3+ pairwise depth comparisons × multiple feature rankings × cross-condition transfers = 远超 50 次假设检验。仅在一个特定测试（d3v4 AUC, §4.3）应用了 Bonferroni 校正（α=0.0167, 3 comparisons）。B.15 downstream curation PoC 也承认 "multiple pairwise comparisons that were not corrected for multiplicity"。当大量比较未校正时，某些 "显著" 发现可能是假阳性。
- 为什么影响接收：ARR 的 Soundness 评分要求 claims 有充分 statistical support。批量未校正的 p-values 削弱了 claims 的可信度。
- 建议修改方向：(a) 对主要 claims 涉及的比较应用 FDR 或 Bonferroni 校正并报告校正后 p-values；(b) 或者将未校正的结论明确标注为 exploratory 而非 confirmatory；(c) 区分 confirmatory（预先计划的）和 exploratory（数据驱动的）分析。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Warning] **EDD 阈值 T=0.70 的理论依据可质疑**
- 具体位置：Definition 1 (§3.4, p.4-5)、§4.1 sensitivity analysis
- 问题：T=0.70 引用 Hosmer & Lemeshow (2000) 的 "acceptable discrimination" 阈值，但 H&L 的阈值设计用于二元 logistic regression 的 goodness-of-fit 评估，而非 pairwise ordinal AUC。将其移植到不同上下文缺乏理论依据。不过 §4.1 的 sensitivity analysis 显示 EDD 对 T ∈ {0.65, 0.70, 0.80} 在 8/9 cells 中稳定，部分缓解了此问题。
- 建议：明确说明 T=0.70 是 operational choice 而非理论推导的结果；报告多个 T 值下的完整结果表。

**W2** [Warning] **Generation Protocol 过于统一**
- 具体位置：§3.2 (p.3)、Table 5 (Appendix A)
- 问题：所有模型使用完全相同的 LoRA 超参数（r=16, α=32, dropout=0.05, 3 epochs）。真实递归污染中，不同迭代/模型会使用不同的微调方法和参数。BOS seeding 统一用于所有生成，可能放大 prior-depth 数据 artifacts。Table 5 确认三个模型和所有深度使用 identical 配置——这虽然提高了内部一致性，但降低了外部有效性。
- 建议：至少在一个模型上测试不同 LoRA rank 或 full fine-tuning 对深度信号的影响。

**W3** [Warning] **Cross-Strategy Transfer 效果较弱**
- 具体位置：§5.2 (p.8)、Table 9 (Appendix B.7)
- 问题：Leave-one-out cross-strategy 准确率仅 45.95%（4-class，chance=25%），仅 1.84× chance。Two-stage pipeline 恢复到 59.1% 但仍不理想。这意味着深度信号高度策略特异，实际部署时需先识别解码策略——但论文未讨论策略识别的准确率和误差传播。
- 建议：在 two-stage pipeline 中报告 Stage 1（strategy identification）的准确率及其对 Stage 2 的误差级联效应。

**W4** [Warning] **Ordinal Classification 使用 Non-Ordinal Classifier**
- 具体位置：§3.4 (p.5)、§5.1 (p.7)
- 问题：RF 不是固有有序分类器。论文在 §5.1 与 ordinal MLP (prototypical) 比较，差距仅 0.8 pp，且 QWK=0.89 表明 RF 经验上尊重有序结构。但 EDD 的二元分类器（500 棵树）与主分类器（200 棵树）之间存在评价体系不一致——主结果用四分类 RF，EDD 用 pairwise binary RF。
- 建议：统一报告主分类器和 EDD 分类器的关系，或在主文解释为什么两者可以共存。

---

## 小问题（不影响接收）

- §3.3 (p.4) "Pythia results in Table 2 are marked †" — 但 Table 2 (p.5) 中 † 标记在 PDF 中不够醒目，容易忽略。建议加粗或加脚注说明。
- Notation 不一致：EDD 下标有时用 T（Definition 1），有时用 τ=0.70（§3.5），有时用 0.70（Table 2 caption）。建议统一。
- §4.3 (p.6) "Bonferroni-corrected for 3 comparisons, α=0.0167 yields p = 0.001" — 应明确说明这 3 个比较是哪 3 个模型的 d3v4 AUC 测试。
- Figure 3 (p.7) Y 轴 "normalized to depth 0" 但具体归一化方法未在 caption 中说明。
- B.14 (p.15) 承认发现并修复了 seed-group 分配 bug，透明度好；但 initial buggy results 占用了篇幅，可以精简。

---

## Questions to Authors

1. **Reference model dependency**: 如果使用一个完全独立的 reference model（如 GPT-2 small 或 LLaMA-3.1-8B）替代 Pythia-1.4B 作为所有 cells 的 reference model，atlas 的均值准确率和 EDD 分布会如何变化？是否测试过？

2. **Low mixing ratios**: 5% 和 10% mixing ratio 下的 signal strength 是否有任何 pilot data？如果没有，作者对低比例下信号存活的预期是什么（基于 25%→50% 的衰减趋势）？

3. **14B EDD paradox**: Cross-reference 使 EDD 从 0 升到 2，但 overall accuracy 下降 6.8 pp。作者如何调和这两个方向相反的结果？这是否暗示 EDD 和 accuracy 在大规模下度量的是不同的东西？

4. **Qwen-7B U-shaped AUC**: d2v3=0.709 但 d4v5=0.772 的 U 型恢复在 model collapse theory 框架下如何解释？是否可能是 QLoRA 量化引入的 artifact？

5. **Model-free features only**: 仅使用 7 个 model-free 特征（TTR、hapax ratio、bigram/trigram entropy、repeated n-gram fractions）的分类性能如何？这将建立一个不受 reference model confound 影响的性能下界。

6. **Multiple comparisons**: 如果对 Table 2 全部 9 cells 的 depth-pair AUC 测试应用 FDR 校正（共 27 次比较：9 cells × 3 adjacent pairs），有多少会保持显著？

---

## 主要优势

1. **问题形式化新颖**：将递归生成深度估计形式化为 ordinal classification 是一个真正的概念贡献。EDD 指标从 binary detection 升级到"能可靠区分多深"，比简单 accuracy 更有信息量。
2. **Atlas 设计系统**：3 model families × 3 decoding strategies × 4 depths 的全因子设计提供了 comprehensive baseline，对后续研究有参考价值。
3. **可复现性好**：超参数完整报告（Table 5）、多种子验证（B.29, 3 seeds, σ≤1.06 pp）、硬件和计算量（B.34, 2×RTX PRO 6000, ~200 GPU-hours）、匿名代码/数据链接。
4. **消融充分**：34 个 appendix subsections 覆盖分类器（§5.1: RF vs. XGBoost vs. ordinal MLP）、特征（§4.2 group ablation）、reference model（B.17）、domain transfer（B.15 FineWeb/RedPajama）、calibration（B.15 threshold calibration）等。
5. **透明度高**：脚注 3 主动声明未做多重比较校正；B.14 主动报告并修复了 seed-group bug；Limitations section 覆盖了主要局限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1846 · 2026-05-25T21:26:13.036968+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并简述理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference), Soundness 3/5, Excitement 3/5\n\n### Must-Fix 问题\n\n**N1** [Critical] \"Decoding strategy contributes at least as much as model architecture\" — 9 个 cell 无法支撑此 claim\n- 基于 3×3 grid 的均值比较（within-model strategy gap 9.3pp vs. within-strategy model gap 7.2pp），但仅有 9 个 cell，且未对 9.3 vs. 7.2 的差异进行任何统计检验。2.1pp 的差异完全可能是噪声。这是论文三大 findings 之一。\n\n**N2** [Critical] Scale generalization claim 证据薄弱——\"signal attenuates with scale\" 基于极有限的数据点\n- 主 benchmark 仅覆盖 1–1.5B。7–8B 仅 2 个模型（仅 nucleus），14B 仅 1 个模型（QLoRA）。Reference model 始终固定为 Pythia-1.4B——当目标模型为 14B 时 reference model 比目标小一个数量级。Appendix B.19 承认 \"U-shaped pattern likely originates from cross-reference setup\"。\n\n**N3** [Critical] Full-replacement 假设与真实场景的鸿沟未被充分弥合\n- Partial-mixing 实验仅测 3/9 cells × 2 比例点（25%, 50%）。50% mixing 下 GPT-2 XL 已失败。5-10% mixing 完全未测试。\n\n### Should-Fix 问题\n\n**W1** [Major] EDD 指标的新颖性和独特价值论证不充分\n- 技术上仅是对 pairwise AUC 设定阈值取最大连续深度。τ=0.70 从 binary logistic regression 直接移植到 ordinal depth AUC 场景是否合理未论证。\n\n**W2** [Major] PLM baseline 比较可能不公平\n- PLM baseline 仅用 frozen CLS + linear probing / ordinal MLP。未测试 full fine-tuned DeBERTa。\"statistical features > PLM representations\" 的 claim 可能仅反映 baseline 设计弱点。\n\n**W3** [Major] Seed corpus 单一性可能夸大特征一致性\n- 全部基于 Wikipedia seed。Cross-domain 结果下降 14pp+。Wikipedia 百科全书体可能不代表对话、创意写作等多样场景。\n\n**W4** [Minor] LoRA fine-tuning 作为 recursive training 代理可能引入系统性偏差\n- LoRA 低秩约束可能人为压缩相邻深度 distributional shift。未讨论 LoRA rank 对 depth signal 的影响。\n\n### Missing References\n1. Stylometric analysis 传统（Stamatatos 2009, Neal et al. 2017）\n2. Ordinal classification ensemble 方法\n3. Iterative self-improvement / self-play 文献（Chen et al. 2024 Self-Play, Yuan et al. 2024 Self-Rewarding）\n\n---\n\n请逐条回应（[AGREE] 或 [REBUT]），引用具体论文内容作为证据。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并简述理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference), Soundness 3/5, Excitement 3/5\n\n### Must-Fix 问题\n\n**N1** [Critical] \"Decoding strategy contributes at least as much as model architecture\" — 9 个 cell 无法支撑此 claim\n- 基于 3×3 grid 的均值比较（within-model strategy gap 9.3pp vs. within-strategy model gap 7.2pp），但仅有 9 个 cell，且未对 9.3 vs. 7.2 的差异进行任何统计检验。2.1pp 的差异完全可能是噪声。这是论文三大 findings 之一。\n\n**N2** [Critical] Scale generalization claim 证据薄弱——\"signal attenuates with scale\" 基于极有限的数据点\n- 主 benchmark 仅覆盖 1–1.5B。7–8B 仅 2 个模型（仅 nucleus），14B 仅 1 个模型（QLoRA）。Reference model 始终固定为 Pythia-1.4B——当目标模型为 14B 时 reference model 比目标小一个数量级。Appendix B.19 承认 \"U-shaped pattern likely originates from cross-reference setup\"。\n\n**N3** [Critical] Full-replacement 假设与真实场景的鸿沟未被充分弥合\n- Partial-mixing 实验仅测 3/9 cells × 2 比例点（25%, 50%）。50% mixing 下 GPT-2 XL 已失败。5-10% mixing 完全未测试。\n\n### Should-Fix 问题\n\n**W1** [Major] EDD 指标的新颖性和独特价值论证不充分\n- 技术上仅是对 pairwise AUC 设定阈值取最大连续深度。τ=0.70 从 binary logistic regression 直接移植到 ordinal depth AUC 场景是否合理未论证。\n\n**W2** [Major] PLM baseline 比较可能不公平\n- PLM baseline 仅用 frozen CLS + linear probing / ordinal MLP。未测试 full fine-tuned DeBERTa。\"statistical features > PLM representations\" 的 claim 可能仅反映 baseline 设计弱点。\n\n**W3** [Major] Seed corpus 单一性可能夸大特征一致性\n- 全部基于 Wikipedia seed。Cross-domain 结果下降 14pp+。Wikipedia 百科全书体可能不代表对话、创意写作等多样场景。\n\n**W4** [Minor] LoRA fine-tuning 作为 recursive training 代理可能引入系统性偏差\n- LoRA 低秩约束可能人为压缩相邻深度 distributional shift。未讨论 LoRA rank 对 depth signal 的影响。\n\n### Missing References\n1. Stylometric analysis 传统（Stamatatos 2009, Neal et al. 2017）\n2. Ordinal classification ensemble 方法\n3. Iterative self-improvement / self-play 文献（Chen et al. 2024 Self-Play, Yuan et al. 2024 Self-Rewarding）\n\n---\n\n请逐条回应（[AGREE] 或 [REBUT]），引用具体论文内容作为证据。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1847 · 2026-05-25T21:26:36.051408+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23014
}
```

</details>

---


### Tool call

_source line 1848 · 2026-05-25T21:26:36.404499+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并简述理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.0 (Findings), Soundness 3.0/5, Excitement 3.5/5\n\n### Must-Fix 问题\n\n**N1** [Critical] Reference Model Confound 贯穿全部实验设计\n- Pythia-1.4B 同时作为 generator 和 reference model，自引用优势 4-11pp。12/19 特征依赖 reference model log-probability。14B 实验揭示根本矛盾：同一文本仅改变 reference model 使 EDD 从 0 跳到 2——说明 EDD 度量的可能不是文本内在深度属性，而是 reference model 与 generator 的兼容性。\n\n**N2** [Critical] Full-Replacement Chain 与现实场景的生态有效性 Gap 严重\n- 100% 合成替换 vs 真实 5-30% 混合比例。25%→50% 已显示 8-15pp 衰减且有 cell 失败。5-10% 完全未测。论文仅用一句话在 Limitations 提及。\n\n**N3** [Major] 14B 规模信号消失与 Scale Attenuation 讨论不充分\n- Self-reference EDD=0，仅 2× chance。7-8B 结果混合（Llama-8B 单调衰减，Qwen-7B U 型恢复）。Model collapse theory 无法解释 U 型曲线。主流 LLM（7B-70B+）在信号衰减区间。\n\n**N4** [Major] Feature Multicollinearity 对 Importance 排名可靠性的影响\n- 14-16/19 特征 VIF>10，有效独立维度仅 4-5。CPI 在极端多重共线性下组定义本身有问题。Rank 4-5 CI width 2.7-3.7。Group-level ablation 比个体排名更可靠，但论文多处依赖个体排名做因果叙事。\n\n**N5** [Major] 多重比较未校正\n- 全文 50+ 假设检验（9 cells × 3 depth pairs × feature rankings × cross-condition transfers），仅 d3v4 AUC 一处做了 Bonferroni。脚注 3 声明 exploratory 但实际行文当作 confirmatory 使用。\n\n### Should-Fix 问题\n\n**W1** EDD 阈值 T=0.70 理论依据可质疑\n- 从 binary logistic regression goodness-of-fit 移植到 pairwise ordinal AUC，缺乏理论基础。不过 sensitivity analysis 部分缓解。\n\n**W2** Generation Protocol 过于统一\n- 所有模型 identical LoRA 超参（r=16, α=32, 3 epochs）。真实递归污染不会如此一致。BOS seeding 可能放大 artifacts。\n\n**W3** Cross-Strategy Transfer 效果较弱\n- Leave-one-out 仅 45.95%（1.84× chance）。Two-stage pipeline 恢复到 59.1% 但未讨论策略识别误差传播。\n\n**W4** Ordinal Classification 使用 Non-Ordinal Classifier\n- RF 不是有序分类器。主结果用 4-class RF（200 trees）与 EDD 用 binary RF（500 trees）存在评价体系不一致。\n\n### Questions to Authors\n1. 独立 reference model（非 Pythia）对全部 cells 的影响？\n2. 5%/10% mixing 有无 pilot data？\n3. 14B EDD paradox（cross-ref 使 EDD↑ 但 accuracy↓）如何调和？\n4. Qwen-7B U 型 AUC 如何解释？\n5. 仅用 7 个 model-free 特征的性能下界？\n6. 27 次深度 AUC 测试 FDR 校正后有多少保持显著？\n\n---\n\n请逐条回应（[AGREE] 或 [REBUT]），引用具体论文内容作为证据。",
  "reviewer_id": "2",
  "project": "recursive_gen_depth_est",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并简述理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.0 (Findings), Soundness 3.0/5, Excitement 3.5/5\n\n### Must-Fix 问题\n\n**N1** [Critical] Reference Model Confound 贯穿全部实验设计\n- Pythia-1.4B 同时作为 generator 和 reference model，自引用优势 4-11pp。12/19 特征依赖 reference model log-probability。14B 实验揭示根本矛盾：同一文本仅改变 reference model 使 EDD 从 0 跳到 2——说明 EDD 度量的可能不是文本内在深度属性，而是 reference model 与 generator 的兼容性。\n\n**N2** [Critical] Full-Replacement Chain 与现实场景的生态有效性 Gap 严重\n- 100% 合成替换 vs 真实 5-30% 混合比例。25%→50% 已显示 8-15pp 衰减且有 cell 失败。5-10% 完全未测。论文仅用一句话在 Limitations 提及。\n\n**N3** [Major] 14B 规模信号消失与 Scale Attenuation 讨论不充分\n- Self-reference EDD=0，仅 2× chance。7-8B 结果混合（Llama-8B 单调衰减，Qwen-7B U 型恢复）。Model collapse theory 无法解释 U 型曲线。主流 LLM（7B-70B+）在信号衰减区间。\n\n**N4** [Major] Feature Multicollinearity 对 Importance 排名可靠性的影响\n- 14-16/19 特征 VIF>10，有效独立维度仅 4-5。CPI 在极端多重共线性下组定义本身有问题。Rank 4-5 CI width 2.7-3.7。Group-level ablation 比个体排名更可靠，但论文多处依赖个体排名做因果叙事。\n\n**N5** [Major] 多重比较未校正\n- 全文 50+ 假设检验（9 cells × 3 depth pairs × feature rankings × cross-condition transfers），仅 d3v4 AUC 一处做了 Bonferroni。脚注 3 声明 exploratory 但实际行文当作 confirmatory 使用。\n\n### Should-Fix 问题\n\n**W1** EDD 阈值 T=0.70 理论依据可质疑\n- 从 binary logistic regression goodness-of-fit 移植到 pairwise ordinal AUC，缺乏理论基础。不过 sensitivity analysis 部分缓解。\n\n**W2** Generation Protocol 过于统一\n- 所有模型 identical LoRA 超参（r=16, α=32, 3 epochs）。真实递归污染不会如此一致。BOS seeding 可能放大 artifacts。\n\n**W3** Cross-Strategy Transfer 效果较弱\n- Leave-one-out 仅 45.95%（1.84× chance）。Two-stage pipeline 恢复到 59.1% 但未讨论策略识别误差传播。\n\n**W4** Ordinal Classification 使用 Non-Ordinal Classifier\n- RF 不是有序分类器。主结果用 4-class RF（200 trees）与 EDD 用 binary RF（500 trees）存在评价体系不一致。\n\n### Questions to Authors\n1. 独立 reference model（非 Pythia）对全部 cells 的影响？\n2. 5%/10% mixing 有无 pilot data？\n3. 14B EDD paradox（cross-ref 使 EDD↑ 但 accuracy↓）如何调和？\n4. Qwen-7B U 型 AUC 如何解释？\n5. 仅用 7 个 model-free 特征的性能下界？\n6. 27 次深度 AUC 测试 FDR 校正后有多少保持显著？\n\n---\n\n请逐条回应（[AGREE] 或 [REBUT]），引用具体论文内容作为证据。",
    "reviewer_id": "2",
    "project": "recursive_gen_depth_est",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1849 · 2026-05-25T21:26:37.767456+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1362
}
```

</details>

---


### Assistant

_source line 1850 · 2026-05-25T21:26:40.976436+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 161

## Round 161

2 recorded events


### User

_source line 1851 · 2026-05-25T21:26:43.441975+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断**: Overall 3.0（Findings 水平）。

**5 个 Must-Fix 问题**：
1. **Reference model confound** [Critical]：Pythia-1.4B 同时做 generator 和 reference model，4-11pp 自引用优势贯穿全部实验；14B 的 EDD=0 (self) / EDD=2 (cross) 悖论证明 EDD 度量的不是文本内在属性而是 reference model 兼容性
2. **Full-replacement vs. 现实 gap** [Critical]：100% 替换链远离真实场景，仅测了 25/50% mixing，5-10% 未测试
3. **14B 信号消失** [Major]：当前主流规模（7B+）信号大幅衰减，方法部署价值受限
4. **Feature multicollinearity** [Major]：14-16/19 VIF>10，top-2 之外排名不稳定（CI width 2.7-3.7），feature importance 叙事可靠性存疑
5. **多重比较未校正** [Major]：50+ 次比较仅 1 处做了 Bonferroni

**主要优势**：问题形式化新颖、atlas 设计系统、可复现性好、消融充分、透明度高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1852 · 2026-05-25T21:26:51.927477+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 162

## Round 162

2 recorded events


### User

_source line 1853 · 2026-05-25T21:29:18.412583+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: "Decoding strategy contributes at least as much as model architecture" claim 缺乏统计支撑**

同意。§4.1 (p.5) 原文："mean within-model strategy gap is 9.3 pp, comparable to the 7.2 pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance"。这一 claim 基于 3×3=9 个 cell 的均值比较，2.1 pp 的差异在如此小的样本上完全没有统计效力。论文未对此差异进行 permutation test、bootstrap test 或任何假设检验。作为论文 Introduction (p.2) 列出的三大发现之一（"decoding strategy affects cross-condition transfer more than model architecture"），该 claim 的证据强度与其在论文中的突出程度严重不匹配。

补充发现：§5.2 (p.8) cross-strategy transfer 仅 45.95%（4-class）也从反面佐证了策略差异的重要性，但这并不等价于 "contributes at least as much" 的定量 claim。建议作者要么提供统计检验，要么将 claim 降级为 observation。

---

**[AGREE] R2-N2: Scale generalization 证据薄弱**

同意，且补充我自己审稿中的发现。R2 准确指出了数据点稀疏的问题：7–8B 仅 2 个模型（Llama-3.1-8B + Qwen2.5-7B），14B 仅 1 个模型（Qwen2.5-14B with QLoRA）。

我进一步发现了一个 R2 未充分展开的关键矛盾（B.19, Table 22）：14B self-reference EDD₀.₇₀ = 0（d0v1 AUC 仅 0.56–0.64），但 cross-reference（Pythia-1.4B）EDD₀.₇₀ = 2（d0v1 AUC 升至 0.70–0.74）。同一文本、同一特征集，仅更换 reference model 就使 EDD 从 0 跃升至 2。这说明在大规模下，EDD 度量的更多是 reference-generator 兼容性而非文本内在深度属性。

此外，Qwen2.5-7B 的 U 型 AUC 曲线（d0v1=0.969, d2v3=0.709, d4v5=0.772, Table 19/20）与 Llama-3.1-8B 的单调衰减模式完全矛盾，论文的 model collapse theory（§3.5, γ→1 per-step signal attenuation）仅能解释单调衰减。B.19 承认 "U-shaped pattern likely originates from cross-reference setup" 恰好证明了 R2 关于 reference model confound 的观点。

---

**[AGREE] R2-N3: Full-replacement 假设与真实场景的鸿沟**

同意。这与我自己审稿中的 N2 一致。补充具体数据：

- B.8 Table 10 显示 50% mixing 下 GPT-2 XL d2v3 AUC = 0.695，已低于 T=0.70 阈值
- 从 25% → 50% mixing，d2v3 AUC 的衰减幅度为 0.03–0.05（三个 cell 均值）
- 如果按此趋势线性外推到 10% mixing，AUC 可能仍在阈值以上，但 5% 就存疑了
- 论文完全未测试 <25% 的比例，而真实 web 递归污染的估计比例更可能在 5-15% 范围

关键的是：partial-mixing 仅覆盖了 3/9 cells（GPT-2 XL nucleus、Pythia nucleus、OLMo temperature），其余 6 个 cell 未测试。在已测试的 3 个 cell 中就有 1 个失败（33% failure rate at 50%），这一失败率在更多 cells 上可能更高。

---

### Should-Fix 问题

**[REBUT] R2-W1: EDD 指标的新颖性和独特价值**

部分不同意。R2 将 EDD 简化为 "pairwise AUC 设阈值取最大连续深度"，但忽略了两个关键设计决策：

1. **Contiguous prefix 约束**：EDD 要求从 (0,1) 到 (d-1,d) 的所有相邻对**连续**超过阈值，而非允许跳跃。这比简单取 max AUC 或 mean AUC 更保守但更有实际意义——如果 d1-d2 不可区分但 d2-d3 可区分，声称能区分到 d3 是误导的。Definition 1 (§3.4, p.4-5) 中 "longest contiguous discriminable prefix" 的形式化是对 ordinal depth 问题的恰当抽象。

2. **与 model collapse 理论的对接**：§3.5 (p.5) 将 EDD 与 model collapse 的 tail erosion 理论联系，指出 EDD 提供了 classifier resolution 上的 physical ceiling——当相邻深度的分布差异低于分类器分辨率时 EDD 饱和。这不仅仅是一个 metric，而是连接理论预测和实证测量的桥梁。

3. **Sensitivity analysis**：§4.1 (p.7) 报告 EDD 在 T ∈ {0.65, 0.70, 0.80} 下对 8/9 cells 稳定，Table 2 caption 和 §4.3 Figure 4 均佐证了 EDD 对阈值选择的鲁棒性。

但我同意 R2 关于 **T=0.70 移植缺乏理论依据** 的具体批评（这也是我自己审稿的 W1）。Hosmer & Lemeshow (2000) 的阈值设计用于 binary logistic regression goodness-of-fit，不是 pairwise ordinal AUC。论文应明确 T=0.70 是 operational choice 而非理论推导。

---

**[AGREE] R2-W2: PLM baseline 比较可能不公平**

同意。B.13 (p.14) 明确报告 PLM baseline 仅使用 "frozen CLS representation + linear probing / ordinal MLP"：
- DeBERTa-v3-base: 64.5% (±4.7%)
- RoBERTa-base: 59.5% (±3.2%)
- RF (statistical features): 78.5%

但 frozen CLS + linear probing 是已知最弱的 PLM adaptation 方式。Full fine-tuned DeBERTa-v3-large 在许多分类任务上性能远超 frozen probing。论文自身在 B.13 末尾承认 "whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question"，这隐含承认了 baseline 设计的局限。

"Statistical features > PLM representations" 这一 claim（§6 Discussion, p.8："end-to-end PLMs lag RF by 14–33 pp"）的可信度取决于 baseline 是否足够强。当前 baseline 设计不足以支撑此 claim。

---

**[AGREE] R2-W3: Seed corpus 单一性，但 R2 关于 14pp+ 下降的数字需要修正**

同意 seed corpus 单一性是一个有效的关切。全部 atlas 基于 Wikipedia seed，百科全书文体的 token 分布（规范、事实陈述为主）可能与对话、创意写作、代码等场景差异显著。

但 R2 称 "Cross-domain 结果下降 14pp+" 需要修正。论文实际报告的 cross-domain 数据：
- B.26 arXiv 抽象文迁移：74.1% ± 2.0%（vs. WikiText ~78%），下降约 **4 pp**，非 14 pp
- B.15 FineWeb/RedPajama：calibrated FPR remains ≤7%

R2 可能混淆了 cross-**domain** transfer（~4 pp drop）和 cross-**model** transfer（§5.2: 66.4% mean，~12 pp drop）。尽管如此，仅测试 arXiv（同属学术/百科文体）不足以验证对话/创意写作等 far-domain 场景。建议补充至少一个非学术 domain（如 Reddit 或 fiction）。

---

**[AGREE] R2-W4: LoRA 作为 recursive training 代理的系统性偏差**

同意。LoRA 的低秩约束（r=16, Table 5 Appendix A）在每次微调时仅更新一个低维子空间，这可能系统性地压缩相邻深度之间的分布偏移幅度。论文对此完全未讨论——Table 5 确认所有模型、所有深度使用 identical LoRA 配置。

如果 LoRA rank 较低导致 per-step distributional shift 被人为缩小，那么论文报告的 EDD 值可能是 LoRA 特异的，不适用于 full fine-tuning 或 different rank 的 LoRA 递归链。至少应测试 r=4 和 r=64 来评估 rank 对 depth signal 的影响。

---

### Missing References

**[AGREE]** 三个方向的缺失引用均合理：

1. **Stylometric analysis**：论文的 19 个统计特征本质上就是 stylometric features（TTR、hapax ratio、n-gram entropy 等）。Stamatatos (2009) 的 survey 和 authorship attribution 文献是直接的方法论先驱，不引用是一个显著遗漏。这也可能帮助论文更好地定位自身贡献——将 depth estimation 与 authorship attribution 的区别和联系讲清楚。

2. **Ordinal classification**：论文使用 RF 做 ordinal classification 但未引用 ordinal ensemble 方法文献。Frank & Hall (2001) 将 ordinal 分类分解为二元子任务的经典方法与论文的 EDD pairwise binary classifier 有直接关联。

3. **Self-play / self-improvement**：Chen et al. (2024) Self-Play 和 Yuan et al. (2024) Self-Rewarding 代表了另一种递归生成范式（刻意的、有目标的递归），与论文研究的 "意外" web 递归污染形成有趣对比。引用这些工作可以拓宽论文的 Related Work 视野。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1854 · 2026-05-25T21:29:59.573809+00:00_

收到 Reviewer 1 的交叉回应。高度共识：7 项 AGREE，1 项 partial REBUT（EDD 新颖性）。R1 还补充了关键发现——14B cross-reference EDD 跃升问题和 R2 数字修正（cross-domain 下降 ~4pp 而非 14pp）。

等待 Reviewer 2 的交叉回应。收到后判断收敛并合成报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 163

## Round 163

20 recorded events


### User

_source line 1855 · 2026-05-25T21:30:00.594287+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

## Must-Fix 问题

### [AGREE with caveat] R1-N1: Reference Model Confound

同意 reference model confound 是真实存在的问题，但不同意其严重程度——"贯穿全部实验设计"过于绝对。

**同意的部分**：
- Pythia-1.4B 自引用优势 4–11pp 是事实（Section 3.3, Appendix B.17, Table 18）
- 14B 实验中 EDD 随 reference model 改变而剧烈波动（Appendix B.19）确实说明 EDD 对 reference model 敏感
- 这与我自己提出的 N2 问题一致：无法分离 scale effect 和 reference mismatch effect

**反驳的部分**：
R1 称 "EDD 度量的可能不是文本内在深度属性，而是 reference model 与 generator 的兼容性"，这个推论过强。关键证据：**主 benchmark 9 个 cell 中有 6 个（OLMo × 3 + GPT-2 XL × 3）本身就是 cross-reference 设定**（Pythia-1.4B 做 reference，OLMo/GPT-2 XL 做 generator），这些 cell 仍然达到 62.4–85.9% accuracy（Table 2）、EDD ≥ 3 in 5/6 cells。如果 EDD 纯粹度量 "reference-generator 兼容性"，cross-reference cells 不应该有如此强的 depth discrimination。此外，Appendix B.22（cross-reference control, Table 22）专门比较了 Pythia-1.4B reference vs. self-reference on Qwen2.5-14B，cross-reference AUC 虽低于 self-reference，但 d0-vs-d1 仍达 0.697，说明 depth signal 是存在的，只是被 reference mismatch 削弱。

**结论**：reference model confound 在 14B scale 是 critical issue，但在 1–1.5B 主 benchmark 中，6/9 cross-reference cells 的成功表明 depth signal 有 intrinsic component。建议作者在 Discussion 中更明确地分离这两个效应。

---

### [AGREE] R1-N2: Full-Replacement Chain 与现实场景的 Gap

完全同意。这与我的 N3 高度一致。

补充论据：Section 5.3 的 partial-mixing 实验（Table 10）仅覆盖 3/9 cells × 2 mixing ratios，且 50% mixing 下 GPT-2 XL 已失败（EDD < 3）。更关键的是，**论文未测试 5–10% 这一最贴近真实场景的比例区间**。Introduction 第 1 段的动机——"web text containing their own outputs"——暗示了对真实 web-scale 混合场景的适用性，但实验未能交付。

R1 指出 "仅用一句话在 Limitations 提及" 是准确的。Limitations（p9）的措辞是 "real-world contamination involves accumulation at unknown mixing ratios"，但这应该是一个 prominent caveat in the main text，而非被轻描淡写。

---

### [AGREE] R1-N3: 14B 规模信号消失

同意，且这与我的 N2 互相印证。

关键问题：Appendix B.19 中 Qwen2.5-7B 出现的 **U 型 AUC 恢复**（d0-vs-d1 下降后 d2-vs-d3 反弹）是一个无法被当前 framework 解释的异常。论文自己承认 "the U-shaped pattern at Qwen2.5-7B likely originates from the cross-reference setup"（Appendix B.19），但如果归因于 cross-reference，则整个 7B+ scale 的结论都受到 reference model confound 的污染，无法得出任何关于 scale 本身的结论。

补充 R1 的观点：**论文在 abstract 中将 "signal attenuates with scale" 列为第三个 finding**，但支撑它的仅有：(1) 1.5B 主结果；(2) 2 个 7–8B 模型（行为不一致）；(3) 1 个 14B 模型（reference model confound 未分离）。这不构成 "finding"——最多是 "preliminary observation"。

---

### [REBUT with partial AGREE] R1-N4: Feature Multicollinearity 对 Importance 排名的影响

**同意的部分**：
- VIF > 10 for 14–16/19 features 确实意味着严重共线性（Section 3.3）
- 个体特征排名（如 rank 4–5 CI width 2.7–3.7）确实不可靠
- 论文在某些地方确实基于个体排名做叙事（如 Section 4.2 "p90_ppl and var_surprisal are consistently prominent"）

**反驳的部分**：
R1 将此升级为 Critical 级别过重。论文采取了多重缓解措施：
1. **Group-level ablation**（Section 4.2）：perplexity family 单独达到 76.85% vs. full 78.45%——这是 robust to multicollinearity 的分析，因为它不依赖个体排名
2. **CPI**（Appendix B.3）：Conditional Permutation Importance 专为处理 correlated features 设计——它 permute 每个 feature within its correlated partners，正是为了应对共线性。R1 质疑 "CPI 在极端多重共线性下组定义本身有问题"，但 CPI 的 conditioning set 是 model-defined（RF 的 split partners），不是人工指定的组
3. **四种 importance 方法一致收敛**：permutation importance、Gini importance、CPI、SHAP 均将 perplexity tail 特征（p90_ppl, var_surprisal, kurtosis_ppl）排入 top-3（Appendix B.2–B.4, B.12）。共线性会导致个体排名不稳定，但不太可能使四种方法的 top-group 结论同时失效
4. **论文的核心 claim 是 family-level**（"perplexity tail statistics family dominates"），不是 individual-level。即使 p90_ppl 和 kurtosis_ppl 的排名互换，family-level 结论不受影响

**结论**：将此从 Critical 降级为 Major 更合理。建议作者删除或弱化个体特征排名的因果叙事，强调 group-level 结论。

---

### [AGREE] R1-N5: 多重比较未校正

同意。这与我的 M1 一致，但 R1 将其升级为 Major 是合理的。

论文有 9 cells × 3 adjacent depth pairs = 27 次 AUC 测试，加上 feature ranking 的 permutation test、cross-condition transfer 的 accuracy 比较等，总量远超 50。脚注 5 的 "exploratory" 声明与正文中 "signal persists in all 9 cells"（Section 4.3）、"depth 0 recall exceeds 97% in all 9 cells"（Section 4.1）等措辞的 confirmatory 语气不匹配。

不过，我认为这个问题的实际影响有限：论文的核心 pattern（d0 easily separable, d2-d3 most confusable, perplexity tail features dominate）在 9/9 cells 中一致出现，不太可能是多重比较 artifact。**建议作者对 27 次 depth-pair AUC 测试应用 Benjamini-Hochberg FDR correction 并报告 corrected results**——这很可能不会改变结论，但会消除方法论上的质疑。

---

## Should-Fix 问题

### [AGREE] R1-W1: EDD 阈值 T=0.70 理论依据

同意。这与我的 W1 一致。Hosmer & Lemeshow (2000) 的 0.70 标准源自 binary logistic regression 的 model fit 评估，移植到 ordinal pairwise AUC 缺乏理论桥梁。不过正如 R1 所说，sensitivity analysis（τ ∈ {0.65, 0.70, 0.80}）部分缓解了对单一阈值的依赖。

---

### [AGREE] R1-W2: Generation Protocol 过于统一

同意。这与我的 W4 一致。LoRA r=16, α=32, 3 epochs 是一组特定超参。真实 recursive contamination 中，不同代的训练方法可能完全不同（有的用 full fine-tuning，有的用 RLHF，有的用 distillation）。BOS seeding 的潜在 artifact 也是一个合理的担忧。

补充：论文在 Appendix B.26 测试了 instruction-tuned model（Qwen2.5-1.5B-Instruct），但仅用一个模型、一个配置，不足以解决 protocol 统一性的根本问题。

---

### [REBUT with partial AGREE] R1-W3: Cross-Strategy Transfer 效果较弱

**同意的部分**：
- Leave-one-out 4-class accuracy 45.95%（1.84× chance）确实偏低
- R1 指出 "策略识别误差传播" 是合理的——two-stage pipeline 的第一阶段（策略识别）如果犯错，第二阶段的 depth estimation 必然出错

**反驳的部分**：
论文并未 claim cross-strategy transfer 是 solved problem。Section 5.3（或准确说是 Section 5.2 的 cross-strategy 部分和 Section 8 的 Discussion）明确承认这是 limitation："Our depth estimation claims hold within-strategy when decoding configuration is known"（Section 8/Discussion 或 similar）。此外，two-stage pipeline 将 accuracy 从 45.95% 提升到 59.1%（+13.15pp），这本身是一个 non-trivial engineering contribution——论文没有将 cross-strategy 作为主要贡献点。

R1 要求讨论 "策略识别误差传播" 是合理的建议，但将此列为 Should-Fix（而非 Must-Fix）是恰当的。

---

### [REBUT] R1-W4: Ordinal Classification 使用 Non-Ordinal Classifier

不同意。

**证据**：Appendix B.25（Table 25）对比了 RF 与三种 ordinal/learned methods：
- XGBoost: mean accuracy comparable to RF
- Ordinal MLP (Frank & Hall, 2001): mean accuracy comparable to RF
- Prototypical: mean accuracy comparable to RF

所有三种 learned/ordinal methods 均未显著优于 RF。这说明 **ordinal structure 在该任务中未提供额外增益**——depth signal 的主要来源是 feature representation，而非分类器的 ordinal inductive bias。

关于 "4-class RF (200 trees) vs binary RF (500 trees) 评价体系不一致"：这是两个不同任务——4-class 衡量整体分类性能，binary 衡量 pairwise discriminability（用于计算 EDD）。使用不同 RF 配置是合理的工程决策，因为 pairwise binary 任务更简单、样本更少，需要更多 trees 以稳定估计。论文在 Section 3.5 解释了 EDD 的 binary RF 使用 500 trees + 5-fold stratified CV。

---

## 对 R1 Questions 的补充意见

**Q1**（独立 reference model 影响）：我也提出了类似问题（我的 Q2）。这是关键实验——如果匹配规模的 reference model（如用 OLMo-1B 做 OLMo 的 reference、GPT-2 XL 做 GPT-2 XL 的 reference）能保持 accuracy，则说明 depth signal 是 intrinsic 的；否则支持 R1 的 "reference-generator compatibility" 假说。

**Q4**（Qwen-7B U 型 AUC）：我同意这是一个需要解释的异常。论文将其归因于 cross-reference setup，但如果所有 7B+ 实验都受 cross-reference confound 影响，则整个 scale analysis 的结论都悬空。

**Q5**（仅用 7 个 model-free 特征）：这是一个很好的问题。Table 1 中 lexical (4) + repetition (3) = 7 个特征不依赖 reference model。如果这 7 个特征能达到 reasonable accuracy（如 >50%），则部分回应了 R1-N1 的 reference model confound 问题。不过论文的 feature group ablation（Section 4.2）显示 lexical + repetition 仅贡献 2.5× chance improvement，远低于 perplexity family，暗示 model-free 特征单独不够用。

**Q6**（FDR 校正后显著性）：R1 问的是 27 次 depth-pair AUC 测试。按 Benjamini-Hochberg，如果原始 p < 0.001 的测试占多数（论文报告 d0-vs-d1 AUC > 0.98 in all cells），FDR correction 后应该大部分保持显著。但 d2-vs-d3 的 borderline cases（特别是 GPT-2 XL top-k, EDD < 3）可能在 correction 后失去显著性。这不会颠覆核心结论，但会影响 "8/9 cells" 的措辞。


---

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部 8 条意见（5 Must-Fix + 3 Should-Fix）+ Missing References 的逐条回应：

- **N1-N3 全部 AGREE**：9-cell claim 无统计检验、scale generalization 数据稀疏且 14B EDD 悖论加深了 reference model confound 的严重性、full-replacement 鸿沟与 R1 自己的 N2 一致
- **W1 REBUT**：EDD 的 contiguous prefix 约束和与 model collapse 理论的对接使其不仅仅是 "阈值+max"；但同意 T=0.70 移植缺乏理论依据
- **W2-W4 全部 AGREE**：PLM baseline 仅 frozen CLS + linear probing 过弱、seed corpus 单一性有效（但修正了 R2 的 14pp 数字——实际 cross-domain 仅降 4pp）、LoRA 低秩约束可能人为压缩 depth signal
- **Missing References AGREE**：stylometric analysis、ordinal ensemble、self-play 文献均为合理补充

---

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 全部意见的逐条交叉回应。

总结：
- **N1 (Reference Model Confound)**: 部分同意——14B scale 问题确实严重，但主 benchmark 6/9 cells 本身就是 cross-reference 且表现良好，R1 的 "贯穿全部实验" 措辞过强
- **N2 (Full-Replacement Gap)**: 完全同意，与我的 N3 一致
- **N3 (14B Signal)**: 完全同意，与我的 N2 一致
- **N4 (Multicollinearity)**: 部分反驳——论文有 group-level ablation + CPI + 四方法交叉验证作为缓解，建议降级为 Major
- **N5 (Multiple Comparisons)**: 同意，建议 FDR correction
- **W1–W2**: 同意
- **W3 (Cross-Strategy)**: 部分反驳——论文未将此作为主要贡献
- **W4 (Non-Ordinal Classifier)**: 反驳——Appendix B.25 已对比 ordinal methods，无显著增益

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1856 · 2026-05-25T21:30:31.024187+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1857 · 2026-05-25T21:30:31.075178+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1858 · 2026-05-25T21:30:35.195933+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1859 · 2026-05-25T21:30:35.648437+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1860 · 2026-05-25T21:30:35.649038+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1861 · 2026-05-25T21:30:36.202110+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:15:51.623812+00:00\", \"completed_at\": \"2026-05-25T21:19:19.997011+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本无任何 display item。首个视觉锚点（Figure 1）延迟到 page 3。审稿人前 2 分钟内只看到文字，缺少视觉锚定。建议：若版面允许，可考虑将 Figure 1 提前至 page 2 底部\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（特征重要性热力图）单元格内数字字号偏小（约 6pt），9×7 网格密集。在屏幕阅读或打印时可能需要放大才能辨认具体数值。建议：增大字号或简化为 top-5 特征子集\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 列数较多（9 个 model-strategy cells），单栏内紧凑但未溢出。精度统一（小数点后一位百分比），最优值加粗，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 三面板折线图，线条颜色可区分（蓝/橙/绿），但图例字号偏小。建议确认灰度打印时线型（solid/dashed/dotted）也能区分\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4 AUC 衰减曲线含 bootstrap 置信带，清晰可读。Table 4 与 Figure 4 同页，布局紧凑但无溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 简短（约 6 行），覆盖 3 个关键点（规模限制、real-world 混合比例未知、分类器 vs 特征空间），符合 EMNLP 要求\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 5 混淆矩阵（3×1 排列）整体偏小，单个矩阵约 3cm 宽。单元格数字可读但较紧凑\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"该页密度极高：Table 9 + Figure 6 + Table 10 + Table 11 + B.10 零样本提示模板文本，附录页面紧凑但不影响主文审稿体验\"}, {\"severity\": \"info\", \"dimension\": \"page 26\", \"message\": \"最后一页内容仅占约 35-40%，剩余为空白。该页为 AI Assistance 声明和计算资源尾部，非主文内容，不影响审稿印象\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"所有表格均使用 booktabs 风格（toprule/midrule/bottomrule），无竖线，最优结果加粗，格式专业统一\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"未发现 LaTeX 渲染错误、margin 溢出、[?] 未解析引用、section heading 孤悬页底等排版问题\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"参考文献格式统一（pp.9-10），编号连续，无异常截断\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 11}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1862 · 2026-05-25T21:30:36.202497+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1863 · 2026-05-25T21:30:36.253286+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1864 · 2026-05-25T21:30:42.888135+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1865 · 2026-05-25T21:30:42.939772+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1866 · 2026-05-25T21:30:44.900517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1867 · 2026-05-25T21:30:44.901580+00:00_

1	issues:
2	# ============================================================
3	# ROUND 19 — CRITICAL (Must-Fix)
4	# ============================================================
5	
6	- id: R19-C1
7	  summary: 泛化性 claim 与证据系统性失配——跨策略 45.9%、14B EDD=0 与 fingerprints 通用性暗示矛盾
8	  category: framing
9	  severity: critical
10	  status: in_progress
11	  first_raised_round: 17
12	  last_seen_round: 19
13	  mentions:
14	  - {round: 17, reviewers: [1, 2], note: 'R17-N3: 跨策略 d1-d3 仅 45.9%'}
15	  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪，Abstract 已加 within-strategy scope 声明'}
16	  - {round: 19, reviewers: [1, 2], note: 'R1 AGREE R2-N2。两人共识：Abstract consistent in direction 将方向一致性包装为正面结论，但 45.9% 分类器不可用。标题 Statistical Fingerprints 暗示可迁移性与实证矛盾。Two-stage 恢复到 70.5% 但仍远低于 within-cell。R1 纠正 R2 引用的 46.7% 数字（实为 cross-tau 而非 cross-model）。'}
17	  action_items:
18	  - {round: 19, action: 'Abstract/Introduction 明确限定 claim scope 为 within known model-strategy configurations', assigned_to: research_director, status: in_progress}
19	  resolution: 'Intro Contribution 4 加 "Within the tested 1--1.5B regime" scope 限定'
20	  resolution_round: null
21	
22	- id: R19-C2
23	  summary: 14B 规模衰减 EDD_70=0 对论文立论的根本威胁——Discussion 传达不足
24	  category: experiment
25	  severity: critical
26	  status: in_progress
27	  first_raised_round: 17
28	  last_seen_round: 19
29	  mentions:
30	  - {round: 17, reviewers: [1, 2], note: 'R17-N2: 14B EDD=0 被 self-reference confound 污染'}
31	  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪'}
32	  - {round: 19, reviewers: [1, 2], note: 'R2-N3 Critical, R1 AGREE with precision: EDD_70=0 不等于无信号 (self-ref 50.8%=2x chance)，但序数结构已坍塌。R2 REBUT R1-W4 (14B confound)：self-ref 数据已足够分离 scale vs ref-model (50.8% vs 44.1% = ~7pp gap 远小于 30+pp 与 1.4B 的差距)。共识：1.4B 成功是 proof-of-concept，contribution list 需显式声明规模限制。'}
33	  action_items:
34	  - {round: 19, action: 'Contribution list 增加规模限制声明；Discussion 分析信号消失机制', assigned_to: research_director, status: in_progress}
35	  resolution: 'Discussion "sca
…[truncated 22995 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1868 · 2026-05-25T21:39:26.050371+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n# ============================================================\n# ROUND 20 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R20-C1\n  summary: \"解码策略贡献至少与模型架构相当\" claim 基于 9-cell 均值比较无统计检验\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R2-N1 提出, R1 完全 AGREE。§4.1 strategy gap 9.3pp vs model gap 7.2pp 差异 2.1pp 在 9 cells 上无统计效力。Introduction 列为三大发现之一但无 permutation/bootstrap test。'}\n  action_items:\n  - {round: 20, action: '提供统计检验或将 claim 从 \"at least as much\" 降级为 \"both contribute meaningfully\"', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C1\n  summary: 泛化性 claim 与证据系统性失配——跨策略 45.9%、14B EDD=0 与 fingerprints 通用性暗示矛盾\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N3: 跨策略 d1-d3 仅 45.9%'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪，Abstract 已加 within-strategy scope 声明'}\n  - {round: 19, reviewers: [1, 2], note: 'R1 AGREE R2-N2。标题 Statistical Fingerprints 暗示可迁移性与实证矛盾。Two-stage 恢复到 70.5% 但仍远低于 within-cell。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-W3 + R2 部分 REBUT（论文未 claim cross-strategy solved）。共识：Should-Fix 级别，framing 需匹配证据。标题 fingerprints 暗示仍成问题。'}\n  action_items:\n  - {round: 19, action: 'Abstract/Introduction 明确限定 claim scope 为 within known model-strategy configurations', assigned_to: research_director, status: in_progress}\n  resolution: 'Intro Contribution 4 加 \"Within the tested 1--1.5B regime\" scope 限定'\n  resolution_round: null\n\n- id: R19-C2\n  summary: 14B 规模衰减 EDD_70=0 对论文立论的根本威胁——Discussion 传达不足\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N2: 14B EDD=0 被 self-reference confound 污染'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪'}\n  - {round: 19, reviewers: [1, 2], note: 'R2-N3 Critical, R1 AGREE: EDD_70=0 不等于无信号但序数结构已坍塌。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-N3 + R2-N3 完全 AGREE。补充：Qwen2.5-7B U 型 AUC 与 model collapse theory 矛盾，论文归因 cross-reference 等于承认 7B+ 结论全部受污染。Abstract \"signal attenuates with scale\" 最多为 preliminary observation。'}\n  action_items:\n  - {round: 19, action: 'Contribution list 增加规模限制声明；Discussion 分析信号消失机制', assigned_to: research_director, status: in_progress}\n  - {round: 20, action: 'Abstract 中 scale attenuation 降级为 preliminary observation 或删除', assigned_to: research_director, status: open}\n  resolution: 'Discussion \"scale attenuation\" → \"accuracy attenuation at 14B\"'\n  resolution_round: null\n\n- id: R19-C3\n  summary: 参考模型依赖限制部署可行性——12/19 特征绑定 Pythia-1.4B，正文讨论不足\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: 'R18-W5: 参考模型依赖性未充分讨论为部署限制'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N1 Critical, R2-W3 后 AGREE。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1 restate confound 贯穿全部实验。R2 部分 REBUT：主 benchmark 6/9 cells 为 cross-reference 且表现良好（62.4-85.9%），depth signal 有 intrinsic component。14B confound 不可忽视。Director 判定：14B critical, 1-1.5B mitigated but 正文讨论仍不足。'}\n  action_items:\n  - {round: 19, action: '正文增加参考模型依赖的系统讨论', assigned_to: research_director, status: in_progress}\n  resolution: 'Discussion Deployment 段加参考模型依赖句 + ref_ablation 引用'\n  resolution_round: null\n\n- id: R19-W2\n  summary: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N1: accumulation 场景无系统实验'}\n  - {round: 18, reviewers: [1, 2], note: '3-cell mix25 accumulation EDD 完成'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N3 Critical 后 R2 认为 Should-Fix。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1 补充：50% mixing 下 GPT-2 XL 失败（AUC=0.695），3 tested cells 33% failure rate。5-10% 比例未测试。R2 完全 AGREE。Director 升级为 Critical——Introduction 动机与实验交付之间鸿沟过大。'}\n  action_items:\n  - {round: 19, action: 'Discussion 明确承认当前基准是 idealized conditions 下的 proof-of-concept', assigned_to: research_director, status: in_progress}\n  - {round: 20, action: 'Limitations 将 full-replacement caveat 提升显著性，或 Discussion 单独讨论', assigned_to: research_director, status: open}\n  resolution: 'Discussion Accumulation 段已改写但仍需加强'\n  resolution_round: null\n\n# ============================================================\n# ROUND 20 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R20-W1\n  summary: Seed corpus 仅 Wikipedia——far-domain 泛化未验证\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R2-W3 提出, R1 AGREE 但修正 R2 数字（cross-domain 降 ~4pp 非 14pp，R2 混淆了 cross-domain 和 cross-model）。arXiv 仍属学术文体，需测试对话/创意写作等 far-domain。'}\n  action_items:\n  - {round: 20, action: 'Discussion 讨论 domain 限制，至少承认 far-domain 未验证', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R20-W2\n  summary: LoRA r=16 统一配置——低秩约束可能人为压缩 depth signal，无 rank ablation\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R2-W4 提出, R1 AGREE。所有深度使用 identical LoRA config (r=16, α=32, 3 epochs)。低秩约束系统性压缩分布偏移幅度，EDD 值可能 LoRA-specific。未测试 r=4/r=64。'}\n  action_items:\n  - {round: 20, action: 'Discussion 或 Limitations 讨论 LoRA rank 对 depth signal 的潜在影响', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R20-W3\n  summary: PLM baseline 仅 frozen CLS + linear probing，信息输入不对等导致比较不公平\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R2-W2 提出, R1 AGREE。RF 用 12 个 reference-model token-level perplexity 特征，PLM 仅看原文 CLS。frozen CLS 是最弱 PLM adaptation。§6 \"PLMs lag RF by 14-33pp\" claim 可信度依赖 baseline 强度。'}\n  action_items:\n  - {round: 20, action: '§6 PLM 比较加条件限定 \"under frozen CLS + linear probing\"', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出。Section 4.2 已有 caveat + CPI 分析。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-N4 升级为 Critical，R2 REBUT 降为 Major（group-level ablation + CPI + 4方法收敛是有效缓解）。Director 采纳 R2 论据，判定 Warning。个体排名叙事需弱化，group-level 结论成立。'}\n  action_items:\n  - {round: 20, action: '§4.2 弱化个体特征排名因果叙事，改为 group-level 叙述', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C4\n  summary: 多重比较未校正但做实质性判断——需统一 FDR correction\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W2: 多重比较未校正'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 atlas.tex EDD bootstrap 已加 Bonferroni'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N2 Critical, R2 部分 AGREE。Director 降为 Warning。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-N5 + R2 AGREE。27+ AUC tests 需 BH FDR correction。脚注 5 exploratory 与正文 confirmatory 语气不匹配。核心结论大概率不受影响但 d2-d3 borderline cases 可能需调整。'}\n  action_items:\n  - {round: 19, action: 'Binoculars 措辞改为 \"not statistically distinguishable\"', assigned_to: research_director, status: in_progress}\n  - {round: 20, action: '对 27 次 depth-pair AUC 测试应用 BH FDR correction 并报告校正后结果', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W4\n  summary: BOS seeding artifact——与 prompted generation 差 13.8pp\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: 'R16-W7: BOS-seeded generation 限制生态效度'}\n  - {round: 17, reviewers: [1, 2], note: 'R17 写作修复已加强 BOS caveat'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W5 Warning, R2 AGREE。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-W2 + R2 AGREE。13.8pp gap 暗示 depth signal 部分源于 BOS seeding 特异性。真实递归污染方法异质（full FT, RLHF, distillation）。'}\n  action_items:\n  - {round: 19, action: 'Limitations 已加 BOS-seeded generation 13.8pp 差异句', assigned_to: research_director, status: in_progress}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W3\n  summary: Neural baseline 比较信息不对等——RF 有 reference model oracle，PLM 仅看原文\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W3: Neural baselines 仅测试 <=125M backbone'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W1 Warning, R2 AGREE。'}\n  - {round: 20, reviewers: [1, 2], note: '继续在 R20-W3 下以 PLM baseline 信息不对等角度追踪。'}\n  action_items:\n  - {round: 19, action: 'Discussion 或 Limitations 明确标注信息不对等', assigned_to: research_director, status: in_progress}\n  resolution: '§5.1 已加 \"RF features access reference-model log-probabilities unavailable to end-to-end PLM baselines\"'\n  resolution_round: null\n\n- id: R19-M2\n  summary: 标题 Statistical Fingerprints 术语选择——弱迁移结果下 fingerprint 有 framing risk\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-M2, R1 轻微 REBUT（forensics 文献常用）。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1 cross-response 重申标题暗示的可迁移性与 45.95% 跨策略结果矛盾。升级为 Warning。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W5\n  summary: 序数分类框架与实际方法脱节——强调 ordinal 但主管线不利用序数结构\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-W2 Warning, R1 AGREE。'}\n  - {round: 20, reviewers: [1, 2], note: 'R2 REBUT R1-W4（Appendix B.25 对比 ordinal methods 无显著增益）。Director 采纳 R2 rebuttal——ordinal structure 在此任务中未提供额外增益是有效发现。保留为 info 级别建议：正文简述原因。'}\n  action_items:\n  - {round: 19, action: '正文简要讨论序数分类方法在此任务中边际改善的原因', assigned_to: research_director, status: in_progress}\n  resolution: 'Discussion 已整合 CORAL +0.3pp 句'\n  resolution_round: null\n\n- id: R19-W6\n  summary: 单 LoRA seed 主实验，2-seed replication 不足以估计方差分布\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W1'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W6 Warning, R2 AGREE 程度较轻。'}\n  - {round: 20, reviewers: [], note: 'R20 未独立提出，但 LoRA rank 问题（R20-W2）间接关联。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W1\n  summary: 方法论创新不足——标准特征+标准分类器，未分析统计特征优于PLM的原因\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N5'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪'}\n  - {round: 19, reviewers: [1, 2], note: 'R2-W1 Warning, R1 部分 REBUT (EMNLP accepts empirical)。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1 cross-response 对 R2-W1 REBUT：EDD contiguous prefix 和 model collapse 对接是贡献。R2 未强力反驳。Director：EDD 设计有价值，novelty 问题降级。'}\n  action_items:\n  - {round: 19, action: 'Discussion 增加一段分析原因', assigned_to: research_director, status: wont_fix}\n  resolution: '页面空间不足。EDD 设计本身有贡献。'\n  resolution_round: 19\n\n# ============================================================\n# ROUND 20 — MINOR (Info)\n# ============================================================\n\n- id: R19-M1\n  summary: Abstract 信息密度过高，14B 结果的 cross-ref vs self-ref 条件混用可能误导\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'Abstract 中 cross-reference EDD_70=2 与 self-reference EDD_70=0 混用需澄清条件。'}\n  - {round: 20, reviewers: [1, 2], note: '继续追踪。scale attenuation claim 降级同时需清理 Abstract 14B 叙事。'}\n  action_items:\n  - {round: 19, action: 'Abstract 14B 结果拆分为独立句子，明确标注 cross-reference 条件', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M3\n  summary: Figure 2/3 字号偏小，打印可读性受限\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-M3, R1 AGREE。'}\n  - {round: 20, reviewers: [], note: '视觉审查确认 Figure 2 heatmap cell 约 6pt，Figure 3 图例字号偏小。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M4\n  summary: Section 3.5 标题过大——Theoretical Motivation 实为经验观察\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [2], note: 'R2-M5: Empirical Motivation 可能更准确。'}\n  - {round: 20, reviewers: [2], note: 'R20 再次提出，R1 未反驳。建议改为 Empirical Motivation。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M5\n  summary: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺理论论证\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R1-W2, R2 AGREE。EDD 是操作性指标，多阈值 sensitivity 已报告。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-W1 + R2 AGREE。sensitivity analysis 部分缓解。建议正文明确为 operational choice。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M6\n  summary: Appendix B.20 Qwen2.5-7B Self-Reference 有 PLACEHOLDER 未填充\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [], note: 'Director 发现 B.20 有 PLACEHOLDER 注释未填充。'}\n  - {round: 20, reviewers: [], note: '未重新检查，继续追踪。'}\n  action_items:\n  - {round: 19, action: 'B.20 PLACEHOLDER 必须在提交前补全或删除', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M7\n  summary: Missing references——stylometric analysis, ordinal classification, self-play\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: '推荐 Lakens (2017), Gutierrez (2016)。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1+R2 共同推荐三个方向：(1) Stamatatos (2009) stylometric/authorship attribution survey; (2) Frank & Hall (2001) ordinal decomposition; (3) Chen et al. (2024) Self-Play + Yuan et al. (2024) Self-Rewarding。均 AGREE。'}\n  action_items: []\n  resolution: 'Lakens 2017 已加入 bib'\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (carried forward, unchanged)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W2 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-W2 下追踪，升级为 critical'}\n  action_items:\n  - {round: 18, action: '3-cell mix25 accumulation EDD 计算完成', assigned_to: research_director, status: done}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 R2 REBUT R1-W4。继续在 R19-C2 下追踪。'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C2 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C1 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C1 下追踪'}\n  action_items:\n  - {round: 17, action: 'Abstract 已加 within-strategy scope 声明', assigned_to: research_director, status: done}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W1 下追踪，severity 降为 warning'}\n  action_items: []\n  resolution: '页面空间不足。R1 认为 EMNLP 接受 empirical contribution。'\n  resolution_round: 19\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W6 下追踪'}\n  - {round: 20, reviewers: [], note: 'R20 继续在 R19-W6 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C4 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C4 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 <=125M backbone\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W3 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-W3 和 R20-W3 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%），削弱独特价值\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C3 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C3 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 (estimation vs classification)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及。Section 3.2 已加声明。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M2\n  summary: CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: '推荐 Lakens (2017) TOST, Gutierrez (2016)。'}\n  - {round: 20, reviewers: [1, 2], note: '新增 Stamatatos (2009), Frank & Hall (2001), Chen et al. (2024) Self-Play, Yuan et al. (2024) Self-Rewarding。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n# Historical resolved/wont_fix (unchanged)\n- id: R16-N1\n  summary: 14B 结果削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Abstract 加 scope 限定; Section 6 新增 scale dependence'\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 1 贡献重组'\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 5.3 reframed'\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 6 新增段落'\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia dagger)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: 'Reviewer 确认 dagger + ref-model ablation 67-79% 已充分'\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: 'Section 4.2 group-level ablation'\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Abstract 精简'\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: 'd1-d3 balanced accuracy 领头'\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: 'Sensitivity analysis 已覆盖'\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 'Section 3.2 BOS caveat 加强。R19 re-raised as R19-W4'\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: 'Thresholding 方案已覆盖'\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 6 扩展'\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 'Section 6 含 curation scenario'\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: 'Acceptable for review'\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 'Pipeline 太简单不需要图'\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: '主文 8 页'\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: 'Structural constraint'\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: ''\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: '已加入'\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 'Classifier convergence evidence sufficient'\n  resolution_round: 16\n\n- id: R18-M3\n  summary: Section 3.5 标题过大\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: '已改为 Theoretical Motivation'\n  resolution_round: 18\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R20-W2 重新从 LoRA rank 角度提出——低秩约束可能压缩 depth signal。'}\n  resolution: '项目收尾不再跑新实验'\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C4 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C4 下追踪'}\n  resolution: ''\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: 'Section 2 已引用'\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: '编译验证通过'\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: '用户指示不再跑新实验'\n  resolution_round: 14\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n# ============================================================\n# ROUND 20 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R20-C1\n  summary: \"解码策略贡献至少与模型架构相当\" claim 基于 9-cell 均值比较无统计检验\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R2-N1 提出, R1 完全 AGREE。§4.1 strategy gap 9.3pp vs model gap 7.2pp 差异 2.1pp 在 9 cells 上无统计效力。Introduction 列为三大发现之一但无 permutation/bootstrap test。'}\n  action_items:\n  - {round: 20, action: '提供统计检验或将 claim 从 \"at least as much\" 降级为 \"both contribute meaningfully\"', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C1\n  summary: 泛化性 claim 与证据系统性失配——跨策略 45.9%、14B EDD=0 与 fingerprints 通用性暗示矛盾\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N3: 跨策略 d1-d3 仅 45.9%'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪，Abstract 已加 within-strategy scope 声明'}\n  - {round: 19, reviewers: [1, 2], note: 'R1 AGREE R2-N2。标题 Statistical Fingerprints 暗示可迁移性与实证矛盾。Two-stage 恢复到 70.5% 但仍远低于 within-cell。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-W3 + R2 部分 REBUT（论文未 claim cross-strategy solved）。共识：Should-Fix 级别，framing 需匹配证据。标题 fingerprints 暗示仍成问题。'}\n  action_items:\n  - {round: 19, action: 'Abstract/Introduction 明确限定 claim scope 为 within known model-strategy configurations', assigned_to: research_director, status: in_progress}\n  resolution: 'Intro Contribution 4 加 \"Within the tested 1--1.5B regime\" scope 限定'\n  resolution_round: null\n\n- id: R19-C2\n  summary: 14B 规模衰减 EDD_70=0 对论文立论的根本威胁——Discussion 传达不足\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N2: 14B EDD=0 被 self-reference confound 污染'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪'}\n  - {round: 19, reviewers: [1, 2], note: 'R2-N3 Critical, R1 AGREE: EDD_70=0 不等于无信号但序数结构已坍塌。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-N3 + R2-N3 完全 AGREE。补充：Qwen2.5-7B U 型 AUC 与 model collapse theory 矛盾，论文归因 cross-reference 等于承认 7B+ 结论全部受污染。Abstract \"signal attenuates with scale\" 最多为 preliminary observation。'}\n  action_items:\n  - {round: 19, action: 'Contribution list 增加规模限制声明；Discussion 分析信号消失机制', assigned_to: research_director, status: in_progress}\n  - {round: 20, action: 'Abstract 中 scale attenuation 降级为 preliminary observation 或删除', assigned_to: research_director, status: open}\n  resolution: 'Discussion \"scale attenuation\" → \"accuracy attenuation at 14B\"'\n  resolution_round: null\n\n- id: R19-C3\n  summary: 参考模型依赖限制部署可行性——12/19 特征绑定 Pythia-1.4B，正文讨论不足\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 18, reviewers: [1, 2], note: 'R18-W5: 参考模型依赖性未充分讨论为部署限制'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N1 Critical, R2-W3 后 AGREE。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1 restate confound 贯穿全部实验。R2 部分 REBUT：主 benchmark 6/9 cells 为 cross-reference 且表现良好（62.4-85.9%），depth signal 有 intrinsic component。14B confound 不可忽视。Director 判定：14B critical, 1-1.5B mitigated but 正文讨论仍不足。'}\n  action_items:\n  - {round: 19, action: '正文增加参考模型依赖的系统讨论', assigned_to: research_director, status: in_progress}\n  resolution: 'Discussion Deployment 段加参考模型依赖句 + ref_ablation 引用'\n  resolution_round: null\n\n- id: R19-W2\n  summary: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N1: accumulation 场景无系统实验'}\n  - {round: 18, reviewers: [1, 2], note: '3-cell mix25 accumulation EDD 完成'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N3 Critical 后 R2 认为 Should-Fix。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1 补充：50% mixing 下 GPT-2 XL 失败（AUC=0.695），3 tested cells 33% failure rate。5-10% 比例未测试。R2 完全 AGREE。Director 升级为 Critical——Introduction 动机与实验交付之间鸿沟过大。'}\n  action_items:\n  - {round: 19, action: 'Discussion 明确承认当前基准是 idealized conditions 下的 proof-of-concept', assigned_to: research_director, status: in_progress}\n  - {round: 20, action: 'Limitations 将 full-replacement caveat 提升显著性，或 Discussion 单独讨论', assigned_to: research_director, status: open}\n  resolution: 'Discussion Accumulation 段已改写但仍需加强'\n  resolution_round: null\n\n# ============================================================\n# ROUND 20 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R20-W1\n  summary: Seed corpus 仅 Wikipedia——far-domain 泛化未验证\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R2-W3 提出, R1 AGREE 但修正 R2 数字（cross-domain 降 ~4pp 非 14pp，R2 混淆了 cross-domain 和 cross-model）。arXiv 仍属学术文体，需测试对话/创意写作等 far-domain。'}\n  action_items:\n  - {round: 20, action: 'Discussion 讨论 domain 限制，至少承认 far-domain 未验证', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R20-W2\n  summary: LoRA r=16 统一配置——低秩约束可能人为压缩 depth signal，无 rank ablation\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R2-W4 提出, R1 AGREE。所有深度使用 identical LoRA config (r=16, α=32, 3 epochs)。低秩约束系统性压缩分布偏移幅度，EDD 值可能 LoRA-specific。未测试 r=4/r=64。'}\n  action_items:\n  - {round: 20, action: 'Discussion 或 Limitations 讨论 LoRA rank 对 depth signal 的潜在影响', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R20-W3\n  summary: PLM baseline 仅 frozen CLS + linear probing，信息输入不对等导致比较不公平\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R2-W2 提出, R1 AGREE。RF 用 12 个 reference-model token-level perplexity 特征，PLM 仅看原文 CLS。frozen CLS 是最弱 PLM adaptation。§6 \"PLMs lag RF by 14-33pp\" claim 可信度依赖 baseline 强度。'}\n  action_items:\n  - {round: 20, action: '§6 PLM 比较加条件限定 \"under frozen CLS + linear probing\"', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF>10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出。Section 4.2 已有 caveat + CPI 分析。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-N4 升级为 Critical，R2 REBUT 降为 Major（group-level ablation + CPI + 4方法收敛是有效缓解）。Director 采纳 R2 论据，判定 Warning。个体排名叙事需弱化，group-level 结论成立。'}\n  action_items:\n  - {round: 20, action: '§4.2 弱化个体特征排名因果叙事，改为 group-level 叙述', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C4\n  summary: 多重比较未校正但做实质性判断——需统一 FDR correction\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W2: 多重比较未校正'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 atlas.tex EDD bootstrap 已加 Bonferroni'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-N2 Critical, R2 部分 AGREE。Director 降为 Warning。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-N5 + R2 AGREE。27+ AUC tests 需 BH FDR correction。脚注 5 exploratory 与正文 confirmatory 语气不匹配。核心结论大概率不受影响但 d2-d3 borderline cases 可能需调整。'}\n  action_items:\n  - {round: 19, action: 'Binoculars 措辞改为 \"not statistically distinguishable\"', assigned_to: research_director, status: in_progress}\n  - {round: 20, action: '对 27 次 depth-pair AUC 测试应用 BH FDR correction 并报告校正后结果', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W4\n  summary: BOS seeding artifact——与 prompted generation 差 13.8pp\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n  - {round: 16, reviewers: [1, 2], note: 'R16-W7: BOS-seeded generation 限制生态效度'}\n  - {round: 17, reviewers: [1, 2], note: 'R17 写作修复已加强 BOS caveat'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W5 Warning, R2 AGREE。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-W2 + R2 AGREE。13.8pp gap 暗示 depth signal 部分源于 BOS seeding 特异性。真实递归污染方法异质（full FT, RLHF, distillation）。'}\n  action_items:\n  - {round: 19, action: 'Limitations 已加 BOS-seeded generation 13.8pp 差异句', assigned_to: research_director, status: in_progress}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W3\n  summary: Neural baseline 比较信息不对等——RF 有 reference model oracle，PLM 仅看原文\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W3: Neural baselines 仅测试 <=125M backbone'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W1 Warning, R2 AGREE。'}\n  - {round: 20, reviewers: [1, 2], note: '继续在 R20-W3 下以 PLM baseline 信息不对等角度追踪。'}\n  action_items:\n  - {round: 19, action: 'Discussion 或 Limitations 明确标注信息不对等', assigned_to: research_director, status: in_progress}\n  resolution: '§5.1 已加 \"RF features access reference-model log-probabilities unavailable to end-to-end PLM baselines\"'\n  resolution_round: null\n\n- id: R19-M2\n  summary: 标题 Statistical Fingerprints 术语选择——弱迁移结果下 fingerprint 有 framing risk\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-M2, R1 轻微 REBUT（forensics 文献常用）。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1 cross-response 重申标题暗示的可迁移性与 45.95% 跨策略结果矛盾。升级为 Warning。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W5\n  summary: 序数分类框架与实际方法脱节——强调 ordinal 但主管线不利用序数结构\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-W2 Warning, R1 AGREE。'}\n  - {round: 20, reviewers: [1, 2], note: 'R2 REBUT R1-W4（Appendix B.25 对比 ordinal methods 无显著增益）。Director 采纳 R2 rebuttal——ordinal structure 在此任务中未提供额外增益是有效发现。保留为 info 级别建议：正文简述原因。'}\n  action_items:\n  - {round: 19, action: '正文简要讨论序数分类方法在此任务中边际改善的原因', assigned_to: research_director, status: in_progress}\n  resolution: 'Discussion 已整合 CORAL +0.3pp 句'\n  resolution_round: null\n\n- id: R19-W6\n  summary: 单 LoRA seed 主实验，2-seed replication 不足以估计方差分布\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-W1'}\n  - {round: 19, reviewers: [1, 2], note: 'R1-W6 Warning, R2 AGREE 程度较轻。'}\n  - {round: 20, reviewers: [], note: 'R20 未独立提出，但 LoRA rank 问题（R20-W2）间接关联。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W1\n  summary: 方法论创新不足——标准特征+标准分类器，未分析统计特征优于PLM的原因\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 17, reviewers: [1, 2], note: 'R17-N5'}\n  - {round: 18, reviewers: [1, 2], note: 'R18 继续追踪'}\n  - {round: 19, reviewers: [1, 2], note: 'R2-W1 Warning, R1 部分 REBUT (EMNLP accepts empirical)。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1 cross-response 对 R2-W1 REBUT：EDD contiguous prefix 和 model collapse 对接是贡献。R2 未强力反驳。Director：EDD 设计有价值，novelty 问题降级。'}\n  action_items:\n  - {round: 19, action: 'Discussion 增加一段分析原因', assigned_to: research_director, status: wont_fix}\n  resolution: '页面空间不足。EDD 设计本身有贡献。'\n  resolution_round: 19\n\n# ============================================================\n# ROUND 20 — MINOR (Info)\n# ============================================================\n\n- id: R19-M1\n  summary: Abstract 信息密度过高，14B 结果的 cross-ref vs self-ref 条件混用可能误导\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'Abstract 中 cross-reference EDD_70=2 与 self-reference EDD_70=0 混用需澄清条件。'}\n  - {round: 20, reviewers: [1, 2], note: '继续追踪。scale attenuation claim 降级同时需清理 Abstract 14B 叙事。'}\n  action_items:\n  - {round: 19, action: 'Abstract 14B 结果拆分为独立句子，明确标注 cross-reference 条件', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M3\n  summary: Figure 2/3 字号偏小，打印可读性受限\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R2-M3, R1 AGREE。'}\n  - {round: 20, reviewers: [], note: '视觉审查确认 Figure 2 heatmap cell 约 6pt，Figure 3 图例字号偏小。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M4\n  summary: Section 3.5 标题过大——Theoretical Motivation 实为经验观察\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [2], note: 'R2-M5: Empirical Motivation 可能更准确。'}\n  - {round: 20, reviewers: [2], note: 'R20 再次提出，R1 未反驳。建议改为 Empirical Motivation。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M5\n  summary: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺理论论证\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R1-W2, R2 AGREE。EDD 是操作性指标，多阈值 sensitivity 已报告。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1-W1 + R2 AGREE。sensitivity analysis 部分缓解。建议正文明确为 operational choice。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M6\n  summary: Appendix B.20 Qwen2.5-7B Self-Reference 有 PLACEHOLDER 未填充\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [], note: 'Director 发现 B.20 有 PLACEHOLDER 注释未填充。'}\n  - {round: 20, reviewers: [], note: '未重新检查，继续追踪。'}\n  action_items:\n  - {round: 19, action: 'B.20 PLACEHOLDER 必须在提交前补全或删除', assigned_to: research_director, status: open}\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M7\n  summary: Missing references——stylometric analysis, ordinal classification, self-play\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: '推荐 Lakens (2017), Gutierrez (2016)。'}\n  - {round: 20, reviewers: [1, 2], note: 'R1+R2 共同推荐三个方向：(1) Stamatatos (2009) stylometric/authorship attribution survey; (2) Frank & Hall (2001) ordinal decomposition; (3) Chen et al. (2024) Self-Play + Yuan et al. (2024) Self-Rewarding。均 AGREE。'}\n  action_items: []\n  resolution: 'Lakens 2017 已加入 bib'\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (carried forward, unchanged)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W2 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-W2 下追踪，升级为 critical'}\n  action_items:\n  - {round: 18, action: '3-cell mix25 accumulation EDD 计算完成', assigned_to: research_director, status: done}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 R2 REBUT R1-W4。继续在 R19-C2 下追踪。'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C2 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C1 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C1 下追踪'}\n  action_items:\n  - {round: 17, action: 'Abstract 已加 within-strategy scope 声明', assigned_to: research_director, status: done}\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W1 下追踪，severity 降为 warning'}\n  action_items: []\n  resolution: '页面空间不足。R1 认为 EMNLP 接受 empirical contribution。'\n  resolution_round: 19\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个，统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W6 下追踪'}\n  - {round: 20, reviewers: [], note: 'R20 继续在 R19-W6 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C4 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C4 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试 <=125M backbone\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-W3 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-W3 和 R20-W3 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能（78.1% vs 78.4%），削弱独特价值\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C3 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C3 下追踪'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 (estimation vs classification)\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未作为独立 issue 提出'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及。Section 3.2 已加声明。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M2\n  summary: CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: '推荐 Lakens (2017) TOST, Gutierrez (2016)。'}\n  - {round: 20, reviewers: [1, 2], note: '新增 Stamatatos (2009), Frank & Hall (2001), Chen et al. (2024) Self-Play, Yuan et al. (2024) Self-Rewarding。'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n# Historical resolved/wont_fix (unchanged)\n- id: R16-N1\n  summary: 14B 结果削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Abstract 加 scope 限定; Section 6 新增 scale dependence'\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 1 贡献重组'\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 5.3 reframed'\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 6 新增段落'\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound (Pythia dagger)\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: 'Reviewer 确认 dagger + ref-model ablation 67-79% 已充分'\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: 'Section 4.2 group-level ablation'\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Abstract 精简'\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: 'd1-d3 balanced accuracy 领头'\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: 'Sensitivity analysis 已覆盖'\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 'Section 3.2 BOS caveat 加强。R19 re-raised as R19-W4'\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: 'Thresholding 方案已覆盖'\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: 'Section 6 扩展'\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 'Section 6 含 curation scenario'\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: 'Acceptable for review'\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 'Pipeline 太简单不需要图'\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: '主文 8 页'\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: 'Structural constraint'\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: ''\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: '已加入'\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 'Classifier convergence evidence sufficient'\n  resolution_round: 16\n\n- id: R18-M3\n  summary: Section 3.5 标题过大\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: '已改为 Theoretical Motivation'\n  resolution_round: 18\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - {round: 19, reviewers: [], note: 'R19 未提及'}\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n  - {round: 20, reviewers: [1, 2], note: 'R20-W2 重新从 LoRA rank 角度提出——低秩约束可能压缩 depth signal。'}\n  resolution: '项目收尾不再跑新实验'\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n  - {round: 19, reviewers: [1, 2], note: 'R19 继续在 R19-C4 下追踪'}\n  - {round: 20, reviewers: [1, 2], note: 'R20 继续在 R19-C4 下追踪'}\n  resolution: ''\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: 'Section 2 已引用'\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: '编译验证通过'\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: '用户指示不再跑新实验'\n  resolution_round: 14\n"
  }
}
```

</details>

---


### Tool result

_source line 1869 · 2026-05-25T21:39:26.053066+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"issues_yaml is not valid YAML: while parsing a block mapping\\n  in \\\"&lt;unicode string>\\\", line 6, column 3:\\n    - id: R20-C1\\n      ^\\nexpected &lt;block end>, but found '&lt;scalar>'\\n  in \\\"&lt;unicode string>\\\", line 7, column 30:\\n      summary: \\\"解码策略贡献至少与模型架构相当\\\" claim 基于 9-cell 均值比较无统计检验\\n                                 ^\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 1870 · 2026-05-25T21:42:30.988569+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n# ============================================================\n# ROUND 20 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R20-C1\n  summary: 解码策略贡献至少与模型架构相当 claim 基于 9-cell 均值比较无统计检验\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R2-N1 提出 R1 完全 AGREE。4.1 strategy gap 9.3pp vs model gap 7.2pp 差异 2.1pp 在 9 cells 上无统计效力。Introduction 列为三大发现之一但无 permutation/bootstrap test。\n  action_items:\n  - round: 20\n    action: 提供统计检验或将 claim 降级为 both contribute meaningfully\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C1\n  summary: 泛化性 claim 与证据系统性失配——跨策略 45.9% 与 fingerprints 通用性暗示矛盾\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-N3 跨策略 d1-d3 仅 45.9%\n  - round: 18\n    reviewers: [1, 2]\n    note: R18 继续追踪 Abstract 已加 within-strategy scope 声明\n  - round: 19\n    reviewers: [1, 2]\n    note: R1 AGREE R2-N2。标题 Statistical Fingerprints 暗示可迁移性与实证矛盾。\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-W3 加 R2 部分 REBUT（论文未 claim cross-strategy solved）。共识 Should-Fix 级别 framing 需匹配证据。\n  action_items:\n  - round: 19\n    action: Abstract/Introduction 明确限定 claim scope 为 within known model-strategy configurations\n    assigned_to: research_director\n    status: in_progress\n  resolution: Intro Contribution 4 加 within the tested 1-1.5B regime scope 限定\n  resolution_round: null\n\n- id: R19-C2\n  summary: 14B 规模衰减 EDD_70=0 对论文立论的根本威胁——Discussion 传达不足\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-N2 14B EDD=0 被 self-reference confound 污染\n  - round: 18\n    reviewers: [1, 2]\n    note: R18 继续追踪\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-N3 Critical R1 AGREE EDD_70=0 不等于无信号但序数结构已坍塌\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-N3 加 R2-N3 完全 AGREE。Qwen2.5-7B U 型 AUC 与 model collapse theory 矛盾。Abstract signal attenuates with scale 最多为 preliminary observation。\n  action_items:\n  - round: 19\n    action: Contribution list 增加规模限制声明\n    assigned_to: research_director\n    status: in_progress\n  - round: 20\n    action: Abstract 中 scale attenuation 降级为 preliminary observation 或删除\n    assigned_to: research_director\n    status: open\n  resolution: Discussion scale attenuation 改为 accuracy attenuation at 14B\n  resolution_round: null\n\n- id: R19-C3\n  summary: 参考模型依赖限制部署可行性——12/19 特征绑定 Pythia-1.4B 正文讨论不足\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: R18-W5 参考模型依赖性未充分讨论为部署限制\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-N1 Critical R2-W3 后 AGREE\n  - round: 20\n    reviewers: [1, 2]\n    note: R1 restate confound 贯穿全部实验。R2 部分 REBUT 主 benchmark 6/9 cells 为 cross-reference 且表现良好。Director 判定 14B critical 1-1.5B mitigated 但正文讨论仍不足。\n  action_items:\n  - round: 19\n    action: 正文增加参考模型依赖的系统讨论\n    assigned_to: research_director\n    status: in_progress\n  resolution: Discussion Deployment 段加参考模型依赖句\n  resolution_round: null\n\n- id: R19-W2\n  summary: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-N1 accumulation 场景无系统实验\n  - round: 18\n    reviewers: [1, 2]\n    note: 3-cell mix25 accumulation EDD 完成\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-N3 Critical 后 R2 认为 Should-Fix\n  - round: 20\n    reviewers: [1, 2]\n    note: R1 补充 50% mixing 下 GPT-2 XL 失败 AUC=0.695 33% failure rate。5-10% 未测试。R2 完全 AGREE。Director 升级为 Critical。\n  action_items:\n  - round: 19\n    action: Discussion 明确承认当前基准是 idealized conditions 下的 proof-of-concept\n    assigned_to: research_director\n    status: in_progress\n  - round: 20\n    action: Limitations 将 full-replacement caveat 提升显著性\n    assigned_to: research_director\n    status: open\n  resolution: Discussion Accumulation 段已改写但仍需加强\n  resolution_round: null\n\n# ============================================================\n# ROUND 20 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R20-W1\n  summary: Seed corpus 仅 Wikipedia far-domain 泛化未验证\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R2-W3 提出 R1 AGREE 但修正数字 cross-domain 降约4pp非14pp。arXiv 仍属学术文体 需测试对话创意写作等 far-domain。\n  action_items:\n  - round: 20\n    action: Discussion 讨论 domain 限制 至少承认 far-domain 未验证\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R20-W2\n  summary: LoRA r=16 统一配置 低秩约束可能人为压缩 depth signal 无 rank ablation\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R2-W4 提出 R1 AGREE。所有深度使用 identical LoRA config r=16 alpha=32 3 epochs。低秩约束系统性压缩分布偏移幅度 EDD 值可能 LoRA-specific。\n  action_items:\n  - round: 20\n    action: Discussion 或 Limitations 讨论 LoRA rank 对 depth signal 的潜在影响\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R20-W3\n  summary: PLM baseline 仅 frozen CLS 加 linear probing 信息输入不对等导致比较不公平\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R2-W2 提出 R1 AGREE。RF 用 12 个 reference-model perplexity 特征 PLM 仅看原文 CLS。Section 6 PLMs lag RF by 14-33pp 可信度依赖 baseline 强度。\n  action_items:\n  - round: 20\n    action: Section 6 PLM 比较加条件限定 under frozen CLS plus linear probing\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF 大于 10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未作为独立 issue 提出 Section 4.2 已有 caveat 加 CPI 分析\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-N4 升级为 Critical R2 REBUT 降为 Major（group-level ablation 加 CPI 加 4方法收敛是有效缓解）。Director 采纳 R2 论据判定 Warning。个体排名叙事需弱化 group-level 结论成立。\n  action_items:\n  - round: 20\n    action: Section 4.2 弱化个体特征排名因果叙事改为 group-level 叙述\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C4\n  summary: 多重比较未校正但做实质性判断 需统一 FDR correction\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-W2 多重比较未校正\n  - round: 18\n    reviewers: [1, 2]\n    note: R18 atlas.tex EDD bootstrap 已加 Bonferroni\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-N2 Critical R2 部分 AGREE Director 降为 Warning\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-N5 加 R2 AGREE。27+ AUC tests 需 BH FDR correction。脚注 5 exploratory 与正文 confirmatory 语气不匹配。\n  action_items:\n  - round: 19\n    action: Binoculars 措辞改为 not statistically distinguishable\n    assigned_to: research_director\n    status: in_progress\n  - round: 20\n    action: 对 27 次 depth-pair AUC 测试应用 BH FDR correction\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W4\n  summary: BOS seeding artifact 与 prompted generation 差 13.8pp\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: R16-W7 BOS-seeded generation 限制生态效度\n  - round: 17\n    reviewers: [1, 2]\n    note: R17 写作修复已加强 BOS caveat\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-W5 Warning R2 AGREE\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-W2 加 R2 AGREE。13.8pp gap 暗示 depth signal 部分源于 BOS seeding 特异性。\n  action_items:\n  - round: 19\n    action: Limitations 已加 BOS-seeded generation 13.8pp 差异句\n    assigned_to: research_director\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W3\n  summary: Neural baseline 比较信息不对等 RF 有 reference model oracle PLM 仅看原文\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-W3 Neural baselines 仅测试小于等于125M backbone\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-W1 Warning R2 AGREE\n  - round: 20\n    reviewers: [1, 2]\n    note: 继续在 R20-W3 下以 PLM baseline 信息不对等角度追踪\n  action_items:\n  - round: 19\n    action: Discussion 或 Limitations 明确标注信息不对等\n    assigned_to: research_director\n    status: in_progress\n  resolution: Section 5.1 已加 RF features access reference-model log-probabilities 句\n  resolution_round: null\n\n- id: R19-M2\n  summary: 标题 Statistical Fingerprints 术语选择 弱迁移结果下 fingerprint 有 framing risk\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-M2 R1 轻微 REBUT forensics 文献常用\n  - round: 20\n    reviewers: [1, 2]\n    note: R1 cross-response 重申标题暗示的可迁移性与 45.95% 跨策略结果矛盾。升级为 Warning。\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W5\n  summary: 序数分类框架与实际方法脱节 强调 ordinal 但主管线不利用序数结构\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-W2 Warning R1 AGREE\n  - round: 20\n    reviewers: [1, 2]\n    note: R2 REBUT R1-W4 Appendix B.25 对比 ordinal methods 无显著增益。Director 采纳 R2 rebuttal 降级为 info。\n  action_items:\n  - round: 19\n    action: 正文简要讨论序数分类方法在此任务中边际改善的原因\n    assigned_to: research_director\n    status: in_progress\n  resolution: Discussion 已整合 CORAL +0.3pp 句\n  resolution_round: null\n\n- id: R19-W6\n  summary: 单 LoRA seed 主实验 2-seed replication 不足以估计方差分布\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-W1\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-W6 Warning R2 AGREE 程度较轻\n  - round: 20\n    reviewers: []\n    note: R20 未独立提出但 LoRA rank 问题 R20-W2 间接关联\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W1\n  summary: 方法论创新不足 标准特征加标准分类器\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-N5\n  - round: 18\n    reviewers: [1, 2]\n    note: R18 继续追踪\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-W1 Warning R1 部分 REBUT EMNLP accepts empirical\n  - round: 20\n    reviewers: [1, 2]\n    note: R1 cross-response 对 R2-W1 REBUT EDD contiguous prefix 和 model collapse 对接是贡献。R2 未强力反驳。\n  action_items:\n  - round: 19\n    action: Discussion 增加一段分析原因\n    assigned_to: research_director\n    status: wont_fix\n  resolution: 页面空间不足。EDD 设计本身有贡献。\n  resolution_round: 19\n\n# ============================================================\n# ROUND 20 — MINOR (Info)\n# ============================================================\n\n- id: R19-M1\n  summary: Abstract 信息密度过高 14B 结果的 cross-ref vs self-ref 条件混用可能误导\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: Abstract 中 cross-reference EDD_70=2 与 self-reference EDD_70=0 混用需澄清条件\n  - round: 20\n    reviewers: [1, 2]\n    note: 继续追踪 scale attenuation claim 降级同时需清理 Abstract 14B 叙事\n  action_items:\n  - round: 19\n    action: Abstract 14B 结果拆分为独立句子明确标注 cross-reference 条件\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M3\n  summary: Figure 2/3 字号偏小 打印可读性受限\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-M3 R1 AGREE\n  - round: 20\n    reviewers: []\n    note: 视觉审查确认 Figure 2 heatmap cell 约 6pt Figure 3 图例字号偏小\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M4\n  summary: Section 3.5 标题过大 Theoretical Motivation 实为经验观察\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [2]\n    note: R2-M5 Empirical Motivation 可能更准确\n  - round: 20\n    reviewers: [2]\n    note: R20 再次提出 R1 未反驳。建议改为 Empirical Motivation。\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M5\n  summary: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺理论论证\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-W2 R2 AGREE EDD 是操作性指标 多阈值 sensitivity 已报告\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-W1 加 R2 AGREE。sensitivity analysis 部分缓解。建议正文明确为 operational choice。\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M6\n  summary: Appendix B.20 Qwen2.5-7B Self-Reference 有 PLACEHOLDER 未填充\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: []\n    note: Director 发现 B.20 有 PLACEHOLDER 注释未填充\n  - round: 20\n    reviewers: []\n    note: 未重新检查 继续追踪\n  action_items:\n  - round: 19\n    action: B.20 PLACEHOLDER 必须在提交前补全或删除\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M7\n  summary: Missing references stylometric analysis ordinal classification self-play\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: 推荐 Lakens 2017 Gutierrez 2016\n  - round: 20\n    reviewers: [1, 2]\n    note: 新增 Stamatatos 2009 stylometric survey。Frank and Hall 2001 ordinal decomposition。Chen et al 2024 Self-Play。Yuan et al 2024 Self-Rewarding。均 AGREE。\n  action_items: []\n  resolution: Lakens 2017 已加入 bib\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (carried forward)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-W2 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-W2 下追踪 升级为 critical\n  action_items:\n  - round: 18\n    action: 3-cell mix25 accumulation EDD 计算完成\n    assigned_to: research_director\n    status: done\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C2 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C2 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C1 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C1 下追踪\n  action_items:\n  - round: 17\n    action: Abstract 已加 within-strategy scope 声明\n    assigned_to: research_director\n    status: done\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 19\n  resolution: 页面空间不足。R1 认为 EMNLP 接受 empirical contribution。\n  resolution_round: 19\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个 统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-W6 下追踪\n  - round: 20\n    reviewers: []\n    note: R20 继续在 R19-W6 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C4 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C4 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试小于等于125M backbone\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-W3 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-W3 和 R20-W3 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能 78.1% vs 78.4% 削弱独特价值\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未作为独立 issue 提出\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C3 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C3 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未作为独立 issue 提出\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 estimation vs classification\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未作为独立 issue 提出\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未提及 Section 3.2 已加声明\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M2\n  summary: CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: 推荐 Lakens 2017 Gutierrez 2016\n  - round: 20\n    reviewers: [1, 2]\n    note: 新增 Stamatatos 2009 Frank and Hall 2001 Chen et al 2024 Yuan et al 2024\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R16-N1\n  summary: 14B 结果削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Abstract 加 scope 限定 Section 6 新增 scale dependence\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Section 1 贡献重组\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Section 5.3 reframed\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Section 6 新增段落\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound Pythia dagger\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: Reviewer 确认 dagger 加 ref-model ablation 67-79% 已充分\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: Section 4.2 group-level ablation\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Abstract 精简\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: d1-d3 balanced accuracy 领头\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: Sensitivity analysis 已覆盖\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: Section 3.2 BOS caveat 加强 R19 re-raised as R19-W4\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: Thresholding 方案已覆盖\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Section 6 扩展\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: Section 6 含 curation scenario\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: Acceptable for review\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: Pipeline 太简单不需要图\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 主文 8 页\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: Structural constraint\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: ''\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 已加入\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: Classifier convergence evidence sufficient\n  resolution_round: 16\n\n- id: R18-M3\n  summary: Section 3.5 标题过大\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: 已改为 Theoretical Motivation\n  resolution_round: 18\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R20-W2 重新从 LoRA rank 角度提出低秩约束可能压缩 depth signal\n  resolution: 项目收尾不再跑新实验\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C4 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C4 下追踪\n  resolution: ''\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: Section 2 已引用\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: 编译验证通过\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: 用户指示不再跑新实验\n  resolution_round: 14\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n# ============================================================\n# ROUND 20 — CRITICAL (Must-Fix)\n# ============================================================\n\n- id: R20-C1\n  summary: 解码策略贡献至少与模型架构相当 claim 基于 9-cell 均值比较无统计检验\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R2-N1 提出 R1 完全 AGREE。4.1 strategy gap 9.3pp vs model gap 7.2pp 差异 2.1pp 在 9 cells 上无统计效力。Introduction 列为三大发现之一但无 permutation/bootstrap test。\n  action_items:\n  - round: 20\n    action: 提供统计检验或将 claim 降级为 both contribute meaningfully\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C1\n  summary: 泛化性 claim 与证据系统性失配——跨策略 45.9% 与 fingerprints 通用性暗示矛盾\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-N3 跨策略 d1-d3 仅 45.9%\n  - round: 18\n    reviewers: [1, 2]\n    note: R18 继续追踪 Abstract 已加 within-strategy scope 声明\n  - round: 19\n    reviewers: [1, 2]\n    note: R1 AGREE R2-N2。标题 Statistical Fingerprints 暗示可迁移性与实证矛盾。\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-W3 加 R2 部分 REBUT（论文未 claim cross-strategy solved）。共识 Should-Fix 级别 framing 需匹配证据。\n  action_items:\n  - round: 19\n    action: Abstract/Introduction 明确限定 claim scope 为 within known model-strategy configurations\n    assigned_to: research_director\n    status: in_progress\n  resolution: Intro Contribution 4 加 within the tested 1-1.5B regime scope 限定\n  resolution_round: null\n\n- id: R19-C2\n  summary: 14B 规模衰减 EDD_70=0 对论文立论的根本威胁——Discussion 传达不足\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-N2 14B EDD=0 被 self-reference confound 污染\n  - round: 18\n    reviewers: [1, 2]\n    note: R18 继续追踪\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-N3 Critical R1 AGREE EDD_70=0 不等于无信号但序数结构已坍塌\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-N3 加 R2-N3 完全 AGREE。Qwen2.5-7B U 型 AUC 与 model collapse theory 矛盾。Abstract signal attenuates with scale 最多为 preliminary observation。\n  action_items:\n  - round: 19\n    action: Contribution list 增加规模限制声明\n    assigned_to: research_director\n    status: in_progress\n  - round: 20\n    action: Abstract 中 scale attenuation 降级为 preliminary observation 或删除\n    assigned_to: research_director\n    status: open\n  resolution: Discussion scale attenuation 改为 accuracy attenuation at 14B\n  resolution_round: null\n\n- id: R19-C3\n  summary: 参考模型依赖限制部署可行性——12/19 特征绑定 Pythia-1.4B 正文讨论不足\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: R18-W5 参考模型依赖性未充分讨论为部署限制\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-N1 Critical R2-W3 后 AGREE\n  - round: 20\n    reviewers: [1, 2]\n    note: R1 restate confound 贯穿全部实验。R2 部分 REBUT 主 benchmark 6/9 cells 为 cross-reference 且表现良好。Director 判定 14B critical 1-1.5B mitigated 但正文讨论仍不足。\n  action_items:\n  - round: 19\n    action: 正文增加参考模型依赖的系统讨论\n    assigned_to: research_director\n    status: in_progress\n  resolution: Discussion Deployment 段加参考模型依赖句\n  resolution_round: null\n\n- id: R19-W2\n  summary: Full-replacement benchmark 与真实 accumulation 场景有根本性 gap\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-N1 accumulation 场景无系统实验\n  - round: 18\n    reviewers: [1, 2]\n    note: 3-cell mix25 accumulation EDD 完成\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-N3 Critical 后 R2 认为 Should-Fix\n  - round: 20\n    reviewers: [1, 2]\n    note: R1 补充 50% mixing 下 GPT-2 XL 失败 AUC=0.695 33% failure rate。5-10% 未测试。R2 完全 AGREE。Director 升级为 Critical。\n  action_items:\n  - round: 19\n    action: Discussion 明确承认当前基准是 idealized conditions 下的 proof-of-concept\n    assigned_to: research_director\n    status: in_progress\n  - round: 20\n    action: Limitations 将 full-replacement caveat 提升显著性\n    assigned_to: research_director\n    status: open\n  resolution: Discussion Accumulation 段已改写但仍需加强\n  resolution_round: null\n\n# ============================================================\n# ROUND 20 — WARNING (Should-Fix)\n# ============================================================\n\n- id: R20-W1\n  summary: Seed corpus 仅 Wikipedia far-domain 泛化未验证\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R2-W3 提出 R1 AGREE 但修正数字 cross-domain 降约4pp非14pp。arXiv 仍属学术文体 需测试对话创意写作等 far-domain。\n  action_items:\n  - round: 20\n    action: Discussion 讨论 domain 限制 至少承认 far-domain 未验证\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R20-W2\n  summary: LoRA r=16 统一配置 低秩约束可能人为压缩 depth signal 无 rank ablation\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R2-W4 提出 R1 AGREE。所有深度使用 identical LoRA config r=16 alpha=32 3 epochs。低秩约束系统性压缩分布偏移幅度 EDD 值可能 LoRA-specific。\n  action_items:\n  - round: 20\n    action: Discussion 或 Limitations 讨论 LoRA rank 对 depth signal 的潜在影响\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R20-W3\n  summary: PLM baseline 仅 frozen CLS 加 linear probing 信息输入不对等导致比较不公平\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R2-W2 提出 R1 AGREE。RF 用 12 个 reference-model perplexity 特征 PLM 仅看原文 CLS。Section 6 PLMs lag RF by 14-33pp 可信度依赖 baseline 强度。\n  action_items:\n  - round: 20\n    action: Section 6 PLM 比较加条件限定 under frozen CLS plus linear probing\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N4\n  summary: VIF 大于 10 严重共线性下个体特征排名不可靠\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未作为独立 issue 提出 Section 4.2 已有 caveat 加 CPI 分析\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-N4 升级为 Critical R2 REBUT 降为 Major（group-level ablation 加 CPI 加 4方法收敛是有效缓解）。Director 采纳 R2 论据判定 Warning。个体排名叙事需弱化 group-level 结论成立。\n  action_items:\n  - round: 20\n    action: Section 4.2 弱化个体特征排名因果叙事改为 group-level 叙述\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-C4\n  summary: 多重比较未校正但做实质性判断 需统一 FDR correction\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-W2 多重比较未校正\n  - round: 18\n    reviewers: [1, 2]\n    note: R18 atlas.tex EDD bootstrap 已加 Bonferroni\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-N2 Critical R2 部分 AGREE Director 降为 Warning\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-N5 加 R2 AGREE。27+ AUC tests 需 BH FDR correction。脚注 5 exploratory 与正文 confirmatory 语气不匹配。\n  action_items:\n  - round: 19\n    action: Binoculars 措辞改为 not statistically distinguishable\n    assigned_to: research_director\n    status: in_progress\n  - round: 20\n    action: 对 27 次 depth-pair AUC 测试应用 BH FDR correction\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W4\n  summary: BOS seeding artifact 与 prompted generation 差 13.8pp\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: R16-W7 BOS-seeded generation 限制生态效度\n  - round: 17\n    reviewers: [1, 2]\n    note: R17 写作修复已加强 BOS caveat\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-W5 Warning R2 AGREE\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-W2 加 R2 AGREE。13.8pp gap 暗示 depth signal 部分源于 BOS seeding 特异性。\n  action_items:\n  - round: 19\n    action: Limitations 已加 BOS-seeded generation 13.8pp 差异句\n    assigned_to: research_director\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W3\n  summary: Neural baseline 比较信息不对等 RF 有 reference model oracle PLM 仅看原文\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-W3 Neural baselines 仅测试小于等于125M backbone\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-W1 Warning R2 AGREE\n  - round: 20\n    reviewers: [1, 2]\n    note: 继续在 R20-W3 下以 PLM baseline 信息不对等角度追踪\n  action_items:\n  - round: 19\n    action: Discussion 或 Limitations 明确标注信息不对等\n    assigned_to: research_director\n    status: in_progress\n  resolution: Section 5.1 已加 RF features access reference-model log-probabilities 句\n  resolution_round: null\n\n- id: R19-M2\n  summary: 标题 Statistical Fingerprints 术语选择 弱迁移结果下 fingerprint 有 framing risk\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-M2 R1 轻微 REBUT forensics 文献常用\n  - round: 20\n    reviewers: [1, 2]\n    note: R1 cross-response 重申标题暗示的可迁移性与 45.95% 跨策略结果矛盾。升级为 Warning。\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W5\n  summary: 序数分类框架与实际方法脱节 强调 ordinal 但主管线不利用序数结构\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-W2 Warning R1 AGREE\n  - round: 20\n    reviewers: [1, 2]\n    note: R2 REBUT R1-W4 Appendix B.25 对比 ordinal methods 无显著增益。Director 采纳 R2 rebuttal 降级为 info。\n  action_items:\n  - round: 19\n    action: 正文简要讨论序数分类方法在此任务中边际改善的原因\n    assigned_to: research_director\n    status: in_progress\n  resolution: Discussion 已整合 CORAL +0.3pp 句\n  resolution_round: null\n\n- id: R19-W6\n  summary: 单 LoRA seed 主实验 2-seed replication 不足以估计方差分布\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-W1\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-W6 Warning R2 AGREE 程度较轻\n  - round: 20\n    reviewers: []\n    note: R20 未独立提出但 LoRA rank 问题 R20-W2 间接关联\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-W1\n  summary: 方法论创新不足 标准特征加标准分类器\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: R17-N5\n  - round: 18\n    reviewers: [1, 2]\n    note: R18 继续追踪\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-W1 Warning R1 部分 REBUT EMNLP accepts empirical\n  - round: 20\n    reviewers: [1, 2]\n    note: R1 cross-response 对 R2-W1 REBUT EDD contiguous prefix 和 model collapse 对接是贡献。R2 未强力反驳。\n  action_items:\n  - round: 19\n    action: Discussion 增加一段分析原因\n    assigned_to: research_director\n    status: wont_fix\n  resolution: 页面空间不足。EDD 设计本身有贡献。\n  resolution_round: 19\n\n# ============================================================\n# ROUND 20 — MINOR (Info)\n# ============================================================\n\n- id: R19-M1\n  summary: Abstract 信息密度过高 14B 结果的 cross-ref vs self-ref 条件混用可能误导\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: Abstract 中 cross-reference EDD_70=2 与 self-reference EDD_70=0 混用需澄清条件\n  - round: 20\n    reviewers: [1, 2]\n    note: 继续追踪 scale attenuation claim 降级同时需清理 Abstract 14B 叙事\n  action_items:\n  - round: 19\n    action: Abstract 14B 结果拆分为独立句子明确标注 cross-reference 条件\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M3\n  summary: Figure 2/3 字号偏小 打印可读性受限\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R2-M3 R1 AGREE\n  - round: 20\n    reviewers: []\n    note: 视觉审查确认 Figure 2 heatmap cell 约 6pt Figure 3 图例字号偏小\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M4\n  summary: Section 3.5 标题过大 Theoretical Motivation 实为经验观察\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [2]\n    note: R2-M5 Empirical Motivation 可能更准确\n  - round: 20\n    reviewers: [2]\n    note: R20 再次提出 R1 未反驳。建议改为 Empirical Motivation。\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M5\n  summary: EDD 阈值 T=0.70 从 binary ROC 迁移到 ordinal pairwise AUC 缺理论论证\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R1-W2 R2 AGREE EDD 是操作性指标 多阈值 sensitivity 已报告\n  - round: 20\n    reviewers: [1, 2]\n    note: R1-W1 加 R2 AGREE。sensitivity analysis 部分缓解。建议正文明确为 operational choice。\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M6\n  summary: Appendix B.20 Qwen2.5-7B Self-Reference 有 PLACEHOLDER 未填充\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: []\n    note: Director 发现 B.20 有 PLACEHOLDER 注释未填充\n  - round: 20\n    reviewers: []\n    note: 未重新检查 继续追踪\n  action_items:\n  - round: 19\n    action: B.20 PLACEHOLDER 必须在提交前补全或删除\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R19-M7\n  summary: Missing references stylometric analysis ordinal classification self-play\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: 推荐 Lakens 2017 Gutierrez 2016\n  - round: 20\n    reviewers: [1, 2]\n    note: 新增 Stamatatos 2009 stylometric survey。Frank and Hall 2001 ordinal decomposition。Chen et al 2024 Self-Play。Yuan et al 2024 Self-Rewarding。均 AGREE。\n  action_items: []\n  resolution: Lakens 2017 已加入 bib\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL ISSUES (carried forward)\n# ============================================================\n\n- id: R17-N1\n  summary: Full-replacement 假设从根本上限制实用价值\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-W2 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-W2 下追踪 升级为 critical\n  action_items:\n  - round: 18\n    action: 3-cell mix25 accumulation EDD 计算完成\n    assigned_to: research_director\n    status: done\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N2\n  summary: 14B EDD=0 被 self-reference confound 污染\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C2 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C2 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N3\n  summary: 跨策略迁移 d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C1 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C1 下追踪\n  action_items:\n  - round: 17\n    action: Abstract 已加 within-strategy scope 声明\n    assigned_to: research_director\n    status: done\n  resolution: ''\n  resolution_round: null\n\n- id: R17-N5\n  summary: 方法层面 novelty 不足\n  category: method\n  severity: critical\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 19\n  resolution: 页面空间不足。R1 认为 EMNLP 接受 empirical contribution。\n  resolution_round: 19\n\n- id: R17-W1\n  summary: LoRA seed 仅 2 个 统计功效不足\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-W6 下追踪\n  - round: 20\n    reviewers: []\n    note: R20 继续在 R19-W6 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W2\n  summary: 多重比较未校正但结论超出 exploratory 范畴\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C4 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C4 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W3\n  summary: Neural end-to-end baselines 仅测试小于等于125M backbone\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-W3 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-W3 和 R20-W3 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W5\n  summary: Binoculars 达到统计等价性能 78.1% vs 78.4% 削弱独特价值\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未作为独立 issue 提出\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-W5\n  summary: 参考模型依赖性未充分讨论为部署限制\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C3 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C3 下追踪\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-W8\n  summary: Downstream curation PoC 不显著但 Introduction 暗示实际应用\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未作为独立 issue 提出\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M5\n  summary: 术语不一致 estimation vs classification\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未作为独立 issue 提出\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M1\n  summary: d0 样本是否跨 cell 共享未显式声明\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n  - round: 19\n    reviewers: []\n    note: R19 未提及 Section 3.2 已加声明\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M2\n  summary: CI 报告不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R17-M4\n  summary: Missing references\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: 推荐 Lakens 2017 Gutierrez 2016\n  - round: 20\n    reviewers: [1, 2]\n    note: 新增 Stamatatos 2009 Frank and Hall 2001 Chen et al 2024 Yuan et al 2024\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R16-N1\n  summary: 14B 结果削弱核心叙事\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Abstract 加 scope 限定 Section 6 新增 scale dependence\n  resolution_round: 16\n\n- id: R16-N2\n  summary: 方法贡献不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Section 1 贡献重组\n  resolution_round: 16\n\n- id: R16-N3\n  summary: Cross-strategy transfer d1-d3 仅 45.9%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Section 5.3 reframed\n  resolution_round: 16\n\n- id: R16-W1\n  summary: Full-replacement vs accumulation 脱节\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Section 6 新增段落\n  resolution_round: 16\n\n- id: R16-W2\n  summary: Self-reference confound Pythia dagger\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: Reviewer 确认 dagger 加 ref-model ablation 67-79% 已充分\n  resolution_round: 16\n\n- id: R16-W3\n  summary: 多重共线性对 feature importance 的影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: Section 4.2 group-level ablation\n  resolution_round: 17\n\n- id: R16-W4\n  summary: Abstract 信息过载\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Abstract 精简\n  resolution_round: 16\n\n- id: R16-W5\n  summary: d0 膨胀 headline metrics\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 16\n  resolution: d1-d3 balanced accuracy 领头\n  resolution_round: 16\n\n- id: R16-W6\n  summary: EDD T=0.70 justification\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: Sensitivity analysis 已覆盖\n  resolution_round: 16\n\n- id: R16-W7\n  summary: BOS-seeded generation 限制生态效度\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: Section 3.2 BOS caveat 加强 R19 re-raised as R19-W4\n  resolution_round: 17\n\n- id: R16-W8\n  summary: Wild-data FPR 过高\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 18\n  resolution: Thresholding 方案已覆盖\n  resolution_round: 16\n\n- id: R16-W9\n  summary: Discussion 过于压缩\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: Section 6 扩展\n  resolution_round: 17\n\n- id: R16-W10\n  summary: 缺具体使用场景\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: Section 6 含 curation scenario\n  resolution_round: 16\n\n- id: R16-M1\n  summary: Figure 3 混淆矩阵数字极小\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: Acceptable for review\n  resolution_round: 16\n\n- id: R16-M2\n  summary: 前 3 页无视觉锚点\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: Pipeline 太简单不需要图\n  resolution_round: 16\n\n- id: R16-M3\n  summary: 页数合规性验证\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: 主文 8 页\n  resolution_round: 16\n\n- id: R16-M4\n  summary: Display items 分布不均\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: Structural constraint\n  resolution_round: 16\n\n- id: R16-M5\n  summary: 术语不一致\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: ''\n  resolution_round: null\n\n- id: R16-M6\n  summary: 遗漏引用 Strobl/Hooker\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: 已加入\n  resolution_round: 16\n\n- id: R16-M7\n  summary: DeBERTa/RoBERTa 失败原因分析不足\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 16\n  last_seen_round: 16\n  resolution: Classifier convergence evidence sufficient\n  resolution_round: 16\n\n- id: R18-M3\n  summary: Section 3.5 标题过大\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: 已改为 Theoretical Motivation\n  resolution_round: 18\n\n- id: R18-M6\n  summary: 生成长度固定 512 tokens\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R18-M7\n  summary: RF 无超参搜索\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R15-W5\n  summary: LoRA 超参无 ablation\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n  - round: 20\n    reviewers: [1, 2]\n    note: R20-W2 重新从 LoRA rank 角度提出低秩约束可能压缩 depth signal\n  resolution: 项目收尾不再跑新实验\n  resolution_round: 16\n\n- id: R15-W8\n  summary: 多重比较未做校正\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n  - round: 19\n    reviewers: [1, 2]\n    note: R19 继续在 R19-C4 下追踪\n  - round: 20\n    reviewers: [1, 2]\n    note: R20 继续在 R19-C4 下追踪\n  resolution: ''\n  resolution_round: null\n\n- id: R15-MR1\n  summary: 遗漏 Markovian Generation Chains\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: Section 2 已引用\n  resolution_round: 16\n\n- id: R14-C2\n  summary: 主文超出 8 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: 编译验证通过\n  resolution_round: 16\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: 用户指示不再跑新实验\n  resolution_round: 14\n"
  }
}
```

</details>

---


### Tool result

_source line 1871 · 2026-05-25T21:42:31.089938+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml\", \"bytes\": 25246}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1872 · 2026-05-25T21:45:34.025395+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 20 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR)\n**Reviewers**: R1, R2 | 交叉回应完成 | 2 轮（初审 + 交叉）收敛\n\n---\n\n## Summary\n\n本文研究递归生成文本的深度估计问题——判断一段文本经历了多少代 LLM 递归重写。作者构建了 3×3 atlas（3 个 1–1.5B 模型 × 3 种解码策略 × 6 个深度层），提取 19 个统计特征（含 12 个基于参考模型的困惑度类特征），使用随机森林分类器进行 4-class ordinal 分类，并提出 Effective Discriminable Depth (EDD) 指标量化可区分深度。主要发现：(1) 在已知模型-策略配置下，1–1.5B 规模深度估计达 78.5% 准确率，EDD₀.₇₀ ≥ 3 覆盖 8/9 cells；(2) 困惑度尾部统计量族主导分类性能；(3) d0（人类文本）高度可分（AUC > 0.98）。\n\n两位 Reviewer 独立初审后完成交叉回应，关键问题充分收敛。核心共识：**论文在 1–1.5B 受控设定下的实证工作扎实，但多处 claim 系统性地超出证据支撑范围。**\n\n---\n\n## Strengths\n\n**S1. 任务定义与问题建模**\n首次将递归生成深度估计形式化为序数分类问题（§3.1），从\"检测 AI 文本\"扩展到\"区分不同递归代数\"。问题定义具有前瞻性——随着 LLM 生成文本回流训练数据，web 文本的递归深度将成为数据质量的重要维度。\n\n**S2. 系统化 Benchmark 设计**\n3 模型 × 3 策略 × 6 深度的 atlas 设计（§3.2–3.3）覆盖了关键实验维度。每个 cell 独立训练递归链、独立提取特征、独立训练分类器，避免跨 cell 数据泄漏。\n\n**S3. EDD 指标的设计理念**\nEDD 的 contiguous prefix 约束（Definition 1, §3.4）要求从 (0,1) 到 (d−1,d) 连续超过阈值——比简单的 max AUC 或 mean AUC 更保守但更有信息量。与 model collapse 理论中 per-step signal attenuation 的对接（§3.5）为指标提供了理论锚点。\n\n**S4. 特征分析深度**\nGroup-level ablation（§4.2: perplexity family 单独 76.85% vs. full 78.45%）、CPI（B.3）、SHAP（B.4）、permutation importance 四种方法交叉验证，group-level 结论在所有方法下一致收敛。\n\n**S5. d0 分离鲁棒性**\nd0 vs. d1 在所有 9 cells 中 AUC > 0.98、recall > 97%（§4.1），在 cross-model（Table 18）和 cross-domain（B.26 arXiv ~74%）场景下保持强信号。对 AI 文本检测有直接实用价值。\n\n**S6. 附录实验的广度**\nAppendix 包含 cross-model（B.17–18）、cross-reference（B.19, B.22）、partial mixing（B.8）、prompted generation（B.23）、PLM baseline（B.13）、ordinal methods（B.25）、arXiv domain（B.26）等实验，展现系统性探索。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**W1. [Critical] \"解码策略贡献至少与模型架构相当\" 的 claim 无统计支撑**\n§4.1 (p.5) 声称 \"mean within-model strategy gap is 9.3 pp, comparable to the 7.2 pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance\"。此 claim 基于 3×3=9 cell 均值比较，2.1 pp 差异在如此小的样本上无任何统计效力。论文未进行 permutation test、bootstrap test 或任何假设检验。然而该 claim 在 Introduction (p.2) 被列为三大发现之一，证据强度与突出程度严重不匹配。\n[R1 AGREE R2-N1，完全共识]\n\n**W2. [Critical] Scale generalization 证据薄弱且自相矛盾**\n论文在 Abstract 将 \"signal attenuates with scale\" 列为第三个 finding，但支撑证据：\n- 7–8B 仅 2 个模型且行为矛盾（Llama-3.1-8B 单调衰减 vs. Qwen2.5-7B U 型恢复，B.19–20）\n- 14B 仅 1 个模型，EDD₀.₇₀ 在 self-reference 下为 0，cross-reference 下为 2（B.19, Table 22）——同一文本更换 reference model 即产生 EDD 从 0 到 2 的跃变\n- Qwen2.5-7B 的 U 型 AUC（d0v1=0.969, d2v3=0.709, d4v5=0.772）与 §3.5 per-step signal attenuation 理论矛盾，论文自行归因于 \"cross-reference setup\"（B.19），由此整个 7B+ scale 分析均受 reference model confound 污染\n此 \"finding\" 最多为 \"preliminary observation\"。\n[R1-N3 AGREE, R2-N2 AGREE, R2-N3 AGREE，完全共识]\n\n**W3. [Critical] Full-replacement 假设与真实场景的根本性鸿沟**\nIntroduction 以 \"web text containing their own outputs\" 为动机，暗示对真实 web-scale 递归污染的适用性。但实验采用 100% replacement chain，partial mixing 仅覆盖 3/9 cells × 2 比例（25%, 50%）。50% mixing 下 GPT-2 XL 已失败（d2v3 AUC=0.695 < T=0.70），已测 3 cells 中 33% failure rate。最贴近真实场景的 5–10% 比例区间完全未测试。Limitations (p.9) 仅一句话带过。\n[R1-N2 AGREE, R2-N3 AGREE，完全共识]\n\n**W4. [Critical] Reference model 依赖限制结论的内在有效性**\n19 个特征中 12 个依赖 Pythia-1.4B 作为 reference model。Pythia-1.4B 自引用优势 4–11 pp（B.17, Table 18）。14B 实验中 EDD 随 reference model 剧烈波动。\n\nR2 提出重要缓解论据：主 benchmark 6/9 cells 为 cross-reference 设定且表现良好（62.4–85.9%），表明 depth signal 存在 intrinsic component——B.22 cross-reference control 中 d0-vs-d1 AUC 仍达 0.697。R1 认为 confound 贯穿全部实验。\n\n**Director 判定**：14B scale 下 confound 不可忽视（Critical），1–1.5B 主 benchmark 中 cross-reference 的成功部分缓解了此问题。但论文未在正文充分讨论这一依赖的部署含义——12/19 特征绑定特定 reference model 对实际应用构成根本限制。\n[R1-N1, R2 部分 AGREE：14B critical, 1–1.5B mitigated]\n\n### Should-Fix\n\n**W5. [Major] 特征多重共线性下个体排名叙事过强**\nVIF > 10 覆盖 14–16/19 个特征（§3.3），个体排名 CI width 2.7–3.7。§4.2 叙事如 \"p90_ppl and var_surprisal are consistently prominent\" 基于不可靠的个体排名。\n\nR2 提出有力缓解论据：group-level ablation + CPI + SHAP + permutation importance 四方法交叉验证，group-level 结论（困惑度尾部族主导）在所有方法下一致收敛。CPI 专为处理 correlated features 设计。即使个体排名不稳定，四种方法 top-group 同时失效的概率极低。\n\n**Director 判定**：采纳 R2 论据，从 R1 的 Critical 降为 Warning。Group-level 结论成立，但个体特征的因果叙事应删除或弱化。\n[R1-N4 Critical → R2 REBUT → Director 降为 Warning]\n\n**W6. [Major] 多重比较未统一校正**\n9 cells × 3 相邻深度对 = 27 次 AUC 测试，加上 feature ranking permutation test 等总量远超 50。脚注 5 \"exploratory\" 声明与正文 \"signal persists in all 9 cells\"、\"depth 0 recall exceeds 97% in all 9 cells\" 的 confirmatory 语气不匹配。建议对 27 次 depth-pair AUC 应用 Benjamini-Hochberg FDR correction——核心结论大概率不受影响，但 d2-vs-d3 borderline cases（特别是 GPT-2 XL top-k, EDD < 3）可能在 correction 后需调整措辞。\n[R1-N5, R2 AGREE，完全共识]\n\n**W7. [Major] PLM baseline 比较信息不对等**\nB.13 PLM baseline 仅用 frozen CLS + linear probing（DeBERTa-v3-base 64.5%, RoBERTa-base 59.5%），这是已知最弱的 PLM adaptation 方式。RF 使用 12 个基于 reference model 的 token-level perplexity 特征，PLM 仅看原文 CLS embedding——二者信息输入不对等。§6 \"end-to-end PLMs lag RF by 14–33 pp\" 的 claim 可信度取决于 baseline 是否足够强。论文自身在 B.13 末尾承认 \"whether larger PLMs can close the gap remains an open question\"。\n[R1 AGREE R2-W2，完全共识]\n\n**W8. [Major] LoRA 作为递归训练代理的系统性偏差**\n所有递归链使用 identical LoRA 配置（r=16, α=32, 3 epochs, Table 5）。LoRA 低秩约束可能系统性压缩相邻深度间的分布偏移幅度，导致 EDD 值为 LoRA-specific。未测试 r=4/r=64 对 depth signal 的影响。真实递归污染中训练方法异质（full fine-tuning, RLHF, distillation 等）。\n[R1 AGREE R2-W4，完全共识]\n\n**W9. [Warning] Seed corpus 仅 Wikipedia**\n全部 atlas 基于 Wikipedia seed。arXiv 跨域下降约 4 pp（B.26: 74.1% vs. ~78%），但 arXiv 仍属学术/百科文体。未测试对话（Reddit）、创意写作（fiction）、代码等 far-domain 场景。\n（注：R1 修正了 R2 初审中 \"14 pp+\" 的说法——实际 cross-domain 降约 4 pp，R2 混淆了 cross-domain 和 cross-model transfer。）\n[R1 AGREE R2-W3，数字修正后共识]\n\n**W10. [Warning] BOS seeding artifact**\nBOS-seeded generation 与 prompted generation 差 13.8 pp（B.23），暗示深度信号部分源于 BOS seeding 特异性而非递归本身的分布偏移。\n[R1-W2, R2 AGREE]\n\n**W11. [Warning] 跨策略迁移有效性有限但 framing 过度**\nLeave-one-out 4-class accuracy 45.95%（1.84× chance, §5.2）。Two-stage pipeline 恢复至 59.1%（+13.15 pp）。R2 指出论文未将 cross-strategy 作为主要贡献，这是合理的。但标题 \"Statistical Fingerprints\" 暗示的可迁移性与实证矛盾——fingerprint 在 forensics 文献中蕴含唯一性和跨条件稳定性。\n[R1-W3, R2 部分 REBUT，分歧收窄为 framing 问题]\n\n### Minor\n\n**W12. [Info] EDD 阈值 T=0.70 迁移缺理论论证**\nHosmer & Lemeshow (2000) 的 0.70 标准源自 binary logistic regression，移植到 ordinal pairwise AUC 无理论桥梁。Sensitivity analysis（T ∈ {0.65, 0.70, 0.80}）部分缓解。建议正文明确 T=0.70 为 operational choice。\n[R1-W1, R2 AGREE]\n\n**W13. [Info] §3.5 \"Theoretical Motivation\" 内容为经验观察**\nSection 标题 \"Theoretical Motivation\" 但内容主要是经验层面的观察和启发式推理，非严格理论推导。\"Empirical Motivation\" 可能更准确。\n[R2-M5, R1 未反驳]\n\n---\n\n## Reviewer 分歧与 Director 裁定\n\n| 问题 | R1 立场 | R2 立场 | Director 裁定 |\n|------|---------|---------|---------------|\n| Reference model confound 严重程度 | Critical, 贯穿全部实验 | Critical at 14B, mitigated at 1–1.5B (6/9 cross-ref cells work) | 采纳 R2 分层判断：14B Critical, 1–1.5B 有 intrinsic signal 但正文讨论不足 |\n| Feature multicollinearity 严重程度 | Critical | Major (group-level analysis robust) | 降为 Warning——R2 的四方法收敛论据成立 |\n| EDD 新颖性 | 有贡献 (contiguous prefix + model collapse) | 低 (AUC + threshold + max) | 采纳 R1——contiguous prefix 约束是有价值的设计选择 |\n| Cross-strategy transfer 严重程度 | Should-Fix | 论文未 claim solved | Should-Fix (framing issue) |\n| Non-ordinal classifier | Should-Fix | REBUT (B.25 ordinal methods 无增益) | 采纳 R2 rebuttal, dropped |\n\n---\n\n## Questions\n\n**Q1.** 如果使用规模匹配的 reference model（如 OLMo-1B 做 OLMo 的 reference、GPT-2 XL 做 GPT-2 XL 的 reference），depth signal 是否保持？这是分离 reference model confound 与 intrinsic depth signal 的关键实验。\n\n**Q2.** Table 1 中 7 个 model-free 特征（lexical 4 + repetition 3）单独使用能达到什么准确率？如果 >50%（2× chance），则部分回应 reference model confound 问题。§4.2 group ablation 暗示 model-free 特征远弱于 perplexity family。\n\n**Q3.** 对 27 次 depth-pair AUC 测试应用 Benjamini-Hochberg FDR correction 后，哪些 cell 的 d2-vs-d3 判断会发生改变？\n\n**Q4.** Qwen2.5-7B 的 U 型 AUC 恢复（d0v1=0.969, d2v3=0.709, d4v5=0.772）如何解释？论文归因于 cross-reference setup，但如果归因成立，则所有 cross-reference 实验的 AUC 模式都不可信。\n\n**Q5.** 5–10% mixing ratio 下 depth estimation 的表现如何？这是 Introduction 动机与实验交付之间鸿沟的关键数据点。\n\n---\n\n## Missing References\n\n两位 Reviewer 共同指出以下缺失引用（均 AGREE）：\n\n1. **Stylometric analysis 文献**：论文的 19 个统计特征本质上是 stylometric features（TTR、hapax ratio、n-gram entropy 等）。Stamatatos (2009) 的 authorship attribution survey 是直接的方法论先驱。引用此文有助于定位 depth estimation 与 authorship attribution 的关系。\n\n2. **Ordinal classification 文献**：Frank & Hall (2001) 将 ordinal 分类分解为二元子任务的方法与 EDD 的 pairwise binary classifier 有直接关联。\n\n3. **Self-play / Self-improvement 文献**：Chen et al. (2024) Self-Play 和 Yuan et al. (2024) Self-Rewarding 代表刻意的递归生成范式，与本文\"意外\" web 递归污染形成有意义的对比。\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-25 21:15–21:19 UTC）。\n\n| 严重级别 | 数量 |\n|---------|------|\n| Critical | 0 |\n| Warning | 1 |\n| Info | 11 |\n\n**Warning**: Pages 1–2 连续纯文本无 display item，Figure 1 延迟至 page 3。建议将 Figure 1 提前至 page 2 底部（如版面允许）。\n\n**Info 摘要**: Figure 2 (p.6) 热力图 cell 内数字约 6pt 密集阅读需放大 | Table 2 (p.5) 9 列紧凑但未溢出格式规范 | Figure 3 (p.7) 图例字号偏小建议确认灰度可区分性 | Figure 4 (p.8) + Table 4 清晰可读 | Limitations (p.9) 简短合规约 6 行 3 点 | Figure 5 (p.12) 混淆矩阵偏小但可读 | Page 13 附录密度高但不影响主文 | 全文 booktabs 格式统一无 LaTeX 渲染错误无 margin 溢出无未解析引用 | 参考文献格式统一编号连续\n\n整体排版质量良好，无格式性问题影响审稿。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5.0 — Findings**\n\n本文在受控设定下（1–1.5B 模型、已知解码策略、100% replacement chain、Wikipedia seed）完成了系统化的递归生成深度估计实证研究。核心发现（d0 高度可分、困惑度尾部特征主导、相邻深度可区分深度约 3–5 代）在 9/9 cells 中一致复现，实证基础扎实。EDD 指标的 contiguous prefix 设计和与 model collapse 理论的对接是有价值的方法论贡献。\n\n然而，论文存在**系统性的 claim-evidence 失配**：\n- \"解码策略贡献至少与模型架构相当\"无统计检验（W1）\n- \"Signal attenuates with scale\" 仅有 3 个 7B+ 模型、行为矛盾、且受 reference model confound 污染（W2）\n- \"Statistical features > PLM\" 基于不公平的 frozen CLS baseline（W7）\n- Introduction 动机暗示真实 web 场景适用性，但 5–10% mixing 未测试、full-replacement chain 为唯一主实验（W3）\n\n此外，12/19 特征依赖特定 reference model（W4）、LoRA r=16 统一配置可能引入系统性偏差（W8）、seed corpus 仅限 Wikipedia（W9）——这些 scope 限制在正文中讨论不足。\n\n**达到 Findings 接收水平的条件**：将 Critical claims 降级为 observations 或提供统计检验，在正文明确限定 scope（1–1.5B, within-strategy, controlled replacement），Discussion 充分讨论 reference model 依赖的部署含义。\n\n**升级至 Conference (4.0) 需要**：(1) 至少一个 5–10% mixing ratio 实验；(2) 规模匹配的 reference model 对照实验（回答 Q1）；(3) 修正 PLM baseline 为 fine-tuned 设定。\n\n---\n\n## Detailed Comments\n\n**Abstract**: 信息密度高但合规（<200 words）。\"signal attenuates with scale\" 需降级为 preliminary observation 或删除。14B 结果的 cross-ref vs self-ref 条件需分句澄清。\n\n**§1 Introduction (p.1–2)**: Contribution 4（\"decoding strategy affects cross-condition transfer more than model architecture\"）在 §4.1 无统计检验支撑，建议改为 \"decoding strategy and model architecture both contribute meaningfully to performance variance\"。\n\n**§3.3 Feature Extraction (p.4)**: 未引用 stylometric analysis 文献。19 个特征本质是 stylometric + perplexity features，应在 Related Work 或此处定位与 authorship attribution 的关系。\n\n**§3.4 Definition 1 (p.4–5)**: EDD 形式化清晰。建议添加一句说明 T=0.70 为 operational choice（参照 sensitivity analysis），非理论推导。\n\n**§3.5 Theoretical Motivation (p.5)**: 标题建议改为 \"Empirical Motivation\"——内容为经验观察而非严格理论推导。\n\n**§4.1 (p.5)**: \"mean within-model strategy gap is 9.3 pp, comparable to the 7.2 pp mean within-strategy model gap\"——2.1 pp 差异在 9 cell 上无统计效力。要么补充 permutation test，要么将 \"at least as much\" 改为 \"both contribute meaningfully\"。\n\n**§4.2 (p.6)**: 个体特征排名叙事（\"p90_ppl and var_surprisal are consistently prominent\"）在 VIF>10 下不可靠。建议改为 group-level 叙事：\"perplexity tail statistics family (p90_ppl, var_surprisal, kurtosis_ppl) collectively dominates\"。\n\n**§5.2 (p.8)**: 跨策略 45.95% 与标题 \"Statistical Fingerprints\" 暗示的可迁移性矛盾。正文应明确：当前深度估计 claim 限定于 \"within known model-strategy configurations\"。\n\n**§6 Discussion (p.8)**: \"end-to-end PLMs lag RF by 14–33 pp\" 需加条件限定：\"under frozen CLS + linear probing\"。Reference model 依赖的部署含义需单独一段讨论。\n\n**Limitations (p.9)**: 覆盖 3 点，长度合规。建议将 full-replacement 假设的局限从 Limitations 提升到 Discussion 的显著位置。\n\n**Appendix B.19**: Qwen2.5-7B U 型 AUC 是关键异常，需要超出 \"likely originates from cross-reference setup\" 的解释。如果归因于 cross-reference，则需讨论所有 cross-reference 实验结果的可信度边界。\n\n**Appendix B.20**: 检查是否仍有 PLACEHOLDER 未填充（Round 19 发现）。",
  "project": "recursive_gen_depth_est",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 20 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR)\n**Reviewers**: R1, R2 | 交叉回应完成 | 2 轮（初审 + 交叉）收敛\n\n---\n\n## Summary\n\n本文研究递归生成文本的深度估计问题——判断一段文本经历了多少代 LLM 递归重写。作者构建了 3×3 atlas（3 个 1–1.5B 模型 × 3 种解码策略 × 6 个深度层），提取 19 个统计特征（含 12 个基于参考模型的困惑度类特征），使用随机森林分类器进行 4-class ordinal 分类，并提出 Effective Discriminable Depth (EDD) 指标量化可区分深度。主要发现：(1) 在已知模型-策略配置下，1–1.5B 规模深度估计达 78.5% 准确率，EDD₀.₇₀ ≥ 3 覆盖 8/9 cells；(2) 困惑度尾部统计量族主导分类性能；(3) d0（人类文本）高度可分（AUC > 0.98）。\n\n两位 Reviewer 独立初审后完成交叉回应，关键问题充分收敛。核心共识：**论文在 1–1.5B 受控设定下的实证工作扎实，但多处 claim 系统性地超出证据支撑范围。**\n\n---\n\n## Strengths\n\n**S1. 任务定义与问题建模**\n首次将递归生成深度估计形式化为序数分类问题（§3.1），从\"检测 AI 文本\"扩展到\"区分不同递归代数\"。问题定义具有前瞻性——随着 LLM 生成文本回流训练数据，web 文本的递归深度将成为数据质量的重要维度。\n\n**S2. 系统化 Benchmark 设计**\n3 模型 × 3 策略 × 6 深度的 atlas 设计（§3.2–3.3）覆盖了关键实验维度。每个 cell 独立训练递归链、独立提取特征、独立训练分类器，避免跨 cell 数据泄漏。\n\n**S3. EDD 指标的设计理念**\nEDD 的 contiguous prefix 约束（Definition 1, §3.4）要求从 (0,1) 到 (d−1,d) 连续超过阈值——比简单的 max AUC 或 mean AUC 更保守但更有信息量。与 model collapse 理论中 per-step signal attenuation 的对接（§3.5）为指标提供了理论锚点。\n\n**S4. 特征分析深度**\nGroup-level ablation（§4.2: perplexity family 单独 76.85% vs. full 78.45%）、CPI（B.3）、SHAP（B.4）、permutation importance 四种方法交叉验证，group-level 结论在所有方法下一致收敛。\n\n**S5. d0 分离鲁棒性**\nd0 vs. d1 在所有 9 cells 中 AUC > 0.98、recall > 97%（§4.1），在 cross-model（Table 18）和 cross-domain（B.26 arXiv ~74%）场景下保持强信号。对 AI 文本检测有直接实用价值。\n\n**S6. 附录实验的广度**\nAppendix 包含 cross-model（B.17–18）、cross-reference（B.19, B.22）、partial mixing（B.8）、prompted generation（B.23）、PLM baseline（B.13）、ordinal methods（B.25）、arXiv domain（B.26）等实验，展现系统性探索。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**W1. [Critical] \"解码策略贡献至少与模型架构相当\" 的 claim 无统计支撑**\n§4.1 (p.5) 声称 \"mean within-model strategy gap is 9.3 pp, comparable to the 7.2 pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance\"。此 claim 基于 3×3=9 cell 均值比较，2.1 pp 差异在如此小的样本上无任何统计效力。论文未进行 permutation test、bootstrap test 或任何假设检验。然而该 claim 在 Introduction (p.2) 被列为三大发现之一，证据强度与突出程度严重不匹配。\n[R1 AGREE R2-N1，完全共识]\n\n**W2. [Critical] Scale generalization 证据薄弱且自相矛盾**\n论文在 Abstract 将 \"signal attenuates with scale\" 列为第三个 finding，但支撑证据：\n- 7–8B 仅 2 个模型且行为矛盾（Llama-3.1-8B 单调衰减 vs. Qwen2.5-7B U 型恢复，B.19–20）\n- 14B 仅 1 个模型，EDD₀.₇₀ 在 self-reference 下为 0，cross-reference 下为 2（B.19, Table 22）——同一文本更换 reference model 即产生 EDD 从 0 到 2 的跃变\n- Qwen2.5-7B 的 U 型 AUC（d0v1=0.969, d2v3=0.709, d4v5=0.772）与 §3.5 per-step signal attenuation 理论矛盾，论文自行归因于 \"cross-reference setup\"（B.19），由此整个 7B+ scale 分析均受 reference model confound 污染\n此 \"finding\" 最多为 \"preliminary observation\"。\n[R1-N3 AGREE, R2-N2 AGREE, R2-N3 AGREE，完全共识]\n\n**W3. [Critical] Full-replacement 假设与真实场景的根本性鸿沟**\nIntroduction 以 \"web text containing their own outputs\" 为动机，暗示对真实 web-scale 递归污染的适用性。但实验采用 100% replacement chain，partial mixing 仅覆盖 3/9 cells × 2 比例（25%, 50%）。50% mixing 下 GPT-2 XL 已失败（d2v3 AUC=0.695 < T=0.70），已测 3 cells 中 33% failure rate。最贴近真实场景的 5–10% 比例区间完全未测试。Limitations (p.9) 仅一句话带过。\n[R1-N2 AGREE, R2-N3 AGREE，完全共识]\n\n**W4. [Critical] Reference model 依赖限制结论的内在有效性**\n19 个特征中 12 个依赖 Pythia-1.4B 作为 reference model。Pythia-1.4B 自引用优势 4–11 pp（B.17, Table 18）。14B 实验中 EDD 随 reference model 剧烈波动。\n\nR2 提出重要缓解论据：主 benchmark 6/9 cells 为 cross-reference 设定且表现良好（62.4–85.9%），表明 depth signal 存在 intrinsic component——B.22 cross-reference control 中 d0-vs-d1 AUC 仍达 0.697。R1 认为 confound 贯穿全部实验。\n\n**Director 判定**：14B scale 下 confound 不可忽视（Critical），1–1.5B 主 benchmark 中 cross-reference 的成功部分缓解了此问题。但论文未在正文充分讨论这一依赖的部署含义——12/19 特征绑定特定 reference model 对实际应用构成根本限制。\n[R1-N1, R2 部分 AGREE：14B critical, 1–1.5B mitigated]\n\n### Should-Fix\n\n**W5. [Major] 特征多重共线性下个体排名叙事过强**\nVIF > 10 覆盖 14–16/19 个特征（§3.3），个体排名 CI width 2.7–3.7。§4.2 叙事如 \"p90_ppl and var_surprisal are consistently prominent\" 基于不可靠的个体排名。\n\nR2 提出有力缓解论据：group-level ablation + CPI + SHAP + permutation importance 四方法交叉验证，group-level 结论（困惑度尾部族主导）在所有方法下一致收敛。CPI 专为处理 correlated features 设计。即使个体排名不稳定，四种方法 top-group 同时失效的概率极低。\n\n**Director 判定**：采纳 R2 论据，从 R1 的 Critical 降为 Warning。Group-level 结论成立，但个体特征的因果叙事应删除或弱化。\n[R1-N4 Critical → R2 REBUT → Director 降为 Warning]\n\n**W6. [Major] 多重比较未统一校正**\n9 cells × 3 相邻深度对 = 27 次 AUC 测试，加上 feature ranking permutation test 等总量远超 50。脚注 5 \"exploratory\" 声明与正文 \"signal persists in all 9 cells\"、\"depth 0 recall exceeds 97% in all 9 cells\" 的 confirmatory 语气不匹配。建议对 27 次 depth-pair AUC 应用 Benjamini-Hochberg FDR correction——核心结论大概率不受影响，但 d2-vs-d3 borderline cases（特别是 GPT-2 XL top-k, EDD < 3）可能在 correction 后需调整措辞。\n[R1-N5, R2 AGREE，完全共识]\n\n**W7. [Major] PLM baseline 比较信息不对等**\nB.13 PLM baseline 仅用 frozen CLS + linear probing（DeBERTa-v3-base 64.5%, RoBERTa-base 59.5%），这是已知最弱的 PLM adaptation 方式。RF 使用 12 个基于 reference model 的 token-level perplexity 特征，PLM 仅看原文 CLS embedding——二者信息输入不对等。§6 \"end-to-end PLMs lag RF by 14–33 pp\" 的 claim 可信度取决于 baseline 是否足够强。论文自身在 B.13 末尾承认 \"whether larger PLMs can close the gap remains an open question\"。\n[R1 AGREE R2-W2，完全共识]\n\n**W8. [Major] LoRA 作为递归训练代理的系统性偏差**\n所有递归链使用 identical LoRA 配置（r=16, α=32, 3 epochs, Table 5）。LoRA 低秩约束可能系统性压缩相邻深度间的分布偏移幅度，导致 EDD 值为 LoRA-specific。未测试 r=4/r=64 对 depth signal 的影响。真实递归污染中训练方法异质（full fine-tuning, RLHF, distillation 等）。\n[R1 AGREE R2-W4，完全共识]\n\n**W9. [Warning] Seed corpus 仅 Wikipedia**\n全部 atlas 基于 Wikipedia seed。arXiv 跨域下降约 4 pp（B.26: 74.1% vs. ~78%），但 arXiv 仍属学术/百科文体。未测试对话（Reddit）、创意写作（fiction）、代码等 far-domain 场景。\n（注：R1 修正了 R2 初审中 \"14 pp+\" 的说法——实际 cross-domain 降约 4 pp，R2 混淆了 cross-domain 和 cross-model transfer。）\n[R1 AGREE R2-W3，数字修正后共识]\n\n**W10. [Warning] BOS seeding artifact**\nBOS-seeded generation 与 prompted generation 差 13.8 pp（B.23），暗示深度信号部分源于 BOS seeding 特异性而非递归本身的分布偏移。\n[R1-W2, R2 AGREE]\n\n**W11. [Warning] 跨策略迁移有效性有限但 framing 过度**\nLeave-one-out 4-class accuracy 45.95%（1.84× chance, §5.2）。Two-stage pipeline 恢复至 59.1%（+13.15 pp）。R2 指出论文未将 cross-strategy 作为主要贡献，这是合理的。但标题 \"Statistical Fingerprints\" 暗示的可迁移性与实证矛盾——fingerprint 在 forensics 文献中蕴含唯一性和跨条件稳定性。\n[R1-W3, R2 部分 REBUT，分歧收窄为 framing 问题]\n\n### Minor\n\n**W12. [Info] EDD 阈值 T=0.70 迁移缺理论论证**\nHosmer & Lemeshow (2000) 的 0.70 标准源自 binary logistic regression，移植到 ordinal pairwise AUC 无理论桥梁。Sensitivity analysis（T ∈ {0.65, 0.70, 0.80}）部分缓解。建议正文明确 T=0.70 为 operational choice。\n[R1-W1, R2 AGREE]\n\n**W13. [Info] §3.5 \"Theoretical Motivation\" 内容为经验观察**\nSection 标题 \"Theoretical Motivation\" 但内容主要是经验层面的观察和启发式推理，非严格理论推导。\"Empirical Motivation\" 可能更准确。\n[R2-M5, R1 未反驳]\n\n---\n\n## Reviewer 分歧与 Director 裁定\n\n| 问题 | R1 立场 | R2 立场 | Director 裁定 |\n|------|---------|---------|---------------|\n| Reference model confound 严重程度 | Critical, 贯穿全部实验 | Critical at 14B, mitigated at 1–1.5B (6/9 cross-ref cells work) | 采纳 R2 分层判断：14B Critical, 1–1.5B 有 intrinsic signal 但正文讨论不足 |\n| Feature multicollinearity 严重程度 | Critical | Major (group-level analysis robust) | 降为 Warning——R2 的四方法收敛论据成立 |\n| EDD 新颖性 | 有贡献 (contiguous prefix + model collapse) | 低 (AUC + threshold + max) | 采纳 R1——contiguous prefix 约束是有价值的设计选择 |\n| Cross-strategy transfer 严重程度 | Should-Fix | 论文未 claim solved | Should-Fix (framing issue) |\n| Non-ordinal classifier | Should-Fix | REBUT (B.25 ordinal methods 无增益) | 采纳 R2 rebuttal, dropped |\n\n---\n\n## Questions\n\n**Q1.** 如果使用规模匹配的 reference model（如 OLMo-1B 做 OLMo 的 reference、GPT-2 XL 做 GPT-2 XL 的 reference），depth signal 是否保持？这是分离 reference model confound 与 intrinsic depth signal 的关键实验。\n\n**Q2.** Table 1 中 7 个 model-free 特征（lexical 4 + repetition 3）单独使用能达到什么准确率？如果 >50%（2× chance），则部分回应 reference model confound 问题。§4.2 group ablation 暗示 model-free 特征远弱于 perplexity family。\n\n**Q3.** 对 27 次 depth-pair AUC 测试应用 Benjamini-Hochberg FDR correction 后，哪些 cell 的 d2-vs-d3 判断会发生改变？\n\n**Q4.** Qwen2.5-7B 的 U 型 AUC 恢复（d0v1=0.969, d2v3=0.709, d4v5=0.772）如何解释？论文归因于 cross-reference setup，但如果归因成立，则所有 cross-reference 实验的 AUC 模式都不可信。\n\n**Q5.** 5–10% mixing ratio 下 depth estimation 的表现如何？这是 Introduction 动机与实验交付之间鸿沟的关键数据点。\n\n---\n\n## Missing References\n\n两位 Reviewer 共同指出以下缺失引用（均 AGREE）：\n\n1. **Stylometric analysis 文献**：论文的 19 个统计特征本质上是 stylometric features（TTR、hapax ratio、n-gram entropy 等）。Stamatatos (2009) 的 authorship attribution survey 是直接的方法论先驱。引用此文有助于定位 depth estimation 与 authorship attribution 的关系。\n\n2. **Ordinal classification 文献**：Frank & Hall (2001) 将 ordinal 分类分解为二元子任务的方法与 EDD 的 pairwise binary classifier 有直接关联。\n\n3. **Self-play / Self-improvement 文献**：Chen et al. (2024) Self-Play 和 Yuan et al. (2024) Self-Rewarding 代表刻意的递归生成范式，与本文\"意外\" web 递归污染形成有意义的对比。\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-25 21:15–21:19 UTC）。\n\n| 严重级别 | 数量 |\n|---------|------|\n| Critical | 0 |\n| Warning | 1 |\n| Info | 11 |\n\n**Warning**: Pages 1–2 连续纯文本无 display item，Figure 1 延迟至 page 3。建议将 Figure 1 提前至 page 2 底部（如版面允许）。\n\n**Info 摘要**: Figure 2 (p.6) 热力图 cell 内数字约 6pt 密集阅读需放大 | Table 2 (p.5) 9 列紧凑但未溢出格式规范 | Figure 3 (p.7) 图例字号偏小建议确认灰度可区分性 | Figure 4 (p.8) + Table 4 清晰可读 | Limitations (p.9) 简短合规约 6 行 3 点 | Figure 5 (p.12) 混淆矩阵偏小但可读 | Page 13 附录密度高但不影响主文 | 全文 booktabs 格式统一无 LaTeX 渲染错误无 margin 溢出无未解析引用 | 参考文献格式统一编号连续\n\n整体排版质量良好，无格式性问题影响审稿。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5.0 — Findings**\n\n本文在受控设定下（1–1.5B 模型、已知解码策略、100% replacement chain、Wikipedia seed）完成了系统化的递归生成深度估计实证研究。核心发现（d0 高度可分、困惑度尾部特征主导、相邻深度可区分深度约 3–5 代）在 9/9 cells 中一致复现，实证基础扎实。EDD 指标的 contiguous prefix 设计和与 model collapse 理论的对接是有价值的方法论贡献。\n\n然而，论文存在**系统性的 claim-evidence 失配**：\n- \"解码策略贡献至少与模型架构相当\"无统计检验（W1）\n- \"Signal attenuates with scale\" 仅有 3 个 7B+ 模型、行为矛盾、且受 reference model confound 污染（W2）\n- \"Statistical features > PLM\" 基于不公平的 frozen CLS baseline（W7）\n- Introduction 动机暗示真实 web 场景适用性，但 5–10% mixing 未测试、full-replacement chain 为唯一主实验（W3）\n\n此外，12/19 特征依赖特定 reference model（W4）、LoRA r=16 统一配置可能引入系统性偏差（W8）、seed corpus 仅限 Wikipedia（W9）——这些 scope 限制在正文中讨论不足。\n\n**达到 Findings 接收水平的条件**：将 Critical claims 降级为 observations 或提供统计检验，在正文明确限定 scope（1–1.5B, within-strategy, controlled replacement），Discussion 充分讨论 reference model 依赖的部署含义。\n\n**升级至 Conference (4.0) 需要**：(1) 至少一个 5–10% mixing ratio 实验；(2) 规模匹配的 reference model 对照实验（回答 Q1）；(3) 修正 PLM baseline 为 fine-tuned 设定。\n\n---\n\n## Detailed Comments\n\n**Abstract**: 信息密度高但合规（<200 words）。\"signal attenuates with scale\" 需降级为 preliminary observation 或删除。14B 结果的 cross-ref vs self-ref 条件需分句澄清。\n\n**§1 Introduction (p.1–2)**: Contribution 4（\"decoding strategy affects cross-condition transfer more than model architecture\"）在 §4.1 无统计检验支撑，建议改为 \"decoding strategy and model architecture both contribute meaningfully to performance variance\"。\n\n**§3.3 Feature Extraction (p.4)**: 未引用 stylometric analysis 文献。19 个特征本质是 stylometric + perplexity features，应在 Related Work 或此处定位与 authorship attribution 的关系。\n\n**§3.4 Definition 1 (p.4–5)**: EDD 形式化清晰。建议添加一句说明 T=0.70 为 operational choice（参照 sensitivity analysis），非理论推导。\n\n**§3.5 Theoretical Motivation (p.5)**: 标题建议改为 \"Empirical Motivation\"——内容为经验观察而非严格理论推导。\n\n**§4.1 (p.5)**: \"mean within-model strategy gap is 9.3 pp, comparable to the 7.2 pp mean within-strategy model gap\"——2.1 pp 差异在 9 cell 上无统计效力。要么补充 permutation test，要么将 \"at least as much\" 改为 \"both contribute meaningfully\"。\n\n**§4.2 (p.6)**: 个体特征排名叙事（\"p90_ppl and var_surprisal are consistently prominent\"）在 VIF>10 下不可靠。建议改为 group-level 叙事：\"perplexity tail statistics family (p90_ppl, var_surprisal, kurtosis_ppl) collectively dominates\"。\n\n**§5.2 (p.8)**: 跨策略 45.95% 与标题 \"Statistical Fingerprints\" 暗示的可迁移性矛盾。正文应明确：当前深度估计 claim 限定于 \"within known model-strategy configurations\"。\n\n**§6 Discussion (p.8)**: \"end-to-end PLMs lag RF by 14–33 pp\" 需加条件限定：\"under frozen CLS + linear probing\"。Reference model 依赖的部署含义需单独一段讨论。\n\n**Limitations (p.9)**: 覆盖 3 点，长度合规。建议将 full-replacement 假设的局限从 Limitations 提升到 Discussion 的显著位置。\n\n**Appendix B.19**: Qwen2.5-7B U 型 AUC 是关键异常，需要超出 \"likely originates from cross-reference setup\" 的解释。如果归因于 cross-reference，则需讨论所有 cross-reference 实验结果的可信度边界。\n\n**Appendix B.20**: 检查是否仍有 PLACEHOLDER 未填充（Round 19 发现）。",
    "project": "recursive_gen_depth_est",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1873 · 2026-05-25T21:45:38.702484+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4677
}
```

</details>

---


### Assistant

_source line 1874 · 2026-05-25T21:45:52.504750+00:00_

Round 20 审稿报告已投递。

**评分：3.0 / 5.0 — Findings**

核心发现：
- **5 个 Critical**：(1) 策略贡献 claim 无统计检验；(2) Scale generalization 证据自相矛盾（U 型 AUC + 14B EDD 随 reference model 波动）；(3) Full-replacement 与真实场景鸿沟（50% mixing 已有 33% failure rate）；(4) Reference model 依赖正文讨论不足；(5) 原有 R19-W2 升级
- **7 个 Warning**：特征共线性个体排名（R1 Critical → R2 REBUT → 降级）、多重比较需 FDR、PLM baseline 信息不对等、LoRA rank 无 ablation、单域 seed、BOS artifact、标题 framing
- **2 个 Info**：EDD 阈值理论论证、§3.5 标题

关键裁定：采纳 R2 对 reference model confound 的分层判断（14B critical / 1–1.5B mitigated）和对 multicollinearity 的降级论据；采纳 R2 对 non-ordinal classifier 的 rebuttal（B.25 ordinal methods 无增益），该 issue 不进入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---
