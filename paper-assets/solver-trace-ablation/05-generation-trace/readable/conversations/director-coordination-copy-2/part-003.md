# Director coordination — Part 3 of 12

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/b1/b1d47a1a2aa91fd38090.json)

## Round 57

### Tool call

_source line 600 · 2026-05-17T17:22:23.416969+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4-7 carry-over (in_progress / open) =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W4 再次确认。§4.5 'No safe scale was observed' 仍为 n=1 seed 的存在性声明。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W6 再次确认。§4.5 title 应改为 'Preliminary Cross-Scale Evidence'。Introduction 用 'preliminarily observed' 但 §4.5 本身未用此 qualifier。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 新增段落声明 1-seed 限制\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"Abstract/Intro 'transfers'→'preliminarily observed at'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"§4.5 'No safe scale was observed' 改为 'No safe scale was observed in this single-seed comparison'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"§4.5 标题改为 'Preliminary Cross-Scale Evidence'; 正文中增加 'single-seed, preliminary' qualifier\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N1\"\n  summary: \"正文超页限制 (~8.5 页 vs ACL long paper 8 页)\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Round 7 两位 Reviewer 均未提及页数问题。R2 确认格式合规：正文 §1-§5 在 8 页内。\"\n  resolution_round: 7\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds/doses\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W4: β=0.3/0.05 仅 500-step snapshot。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 再次提出。R2 [AGREE]。'Trajectory-confirmed' 仅 β=0.1 的 2 个 seeds。β=0.2 的 100% H7 saturation 本身 sufficient 但 β=0.05/0.3 需区分 snapshot-observed vs trajectory-confirmed。\"\n  action_items:\n    - round: 5\n      action: \"软化 'at all tested doses' 措辞\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"弱化为 'collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"Abstract/Intro 中明确区分 'snapshot-observed (all doses)' vs 'trajectory-confirmed (β=0.1 only)'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"统计层级倒置; OR 反转正文一句带过。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N2 / R2 [AGREE]。CMH OR=3.37 方向与 5-seed Fisher 一致但 framing 不诚实。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N1 [critical], R2 [AGREE]。CMH OR=3.37 正文出现 3 次 vs corrected OR=0.61 仅 2 次且靠后。Table 1 仅 uncorrected N-H=23%*。Discussion 以 uncorrected 为主基调。'Suggestive but non-robust' 仍暗示正方向。需以 corrected 为 primary baseline。\"\n  action_items:\n    - round: 5\n      action: \"CMH 作为 primary test 移入正文; Abstract 删除 uncorrected OR\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"(a) 3-seed corrected OR=0.61 提升为 primary sensitivity; (b) 明确 'genuine-rate advantage is not robust to H8 correction'\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 7\n      action: \"(a) Table 1 N-H 列同时展示 uncorrected/corrected 或注明 corrected 值; (b) Discussion 以 corrected 为主基调; (c) Abstract 措辞改为 'genuine-rate advantage is not robust to classification methodology'; (d) 明确 'may be an artifact of uncorrected classification'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"CMH 检验的 within-seed 非独立性问题——真实独立样本量为 n=5 (seeds) 而非 n=350/414 (samples)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N5 再次提出。R2 [REBUT]: 正文已将 CMH 作为 primary。Director 降级为 warning。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N2 [critical] 升级论述。CMH 假设 stratum 内观测独立，但 greedy decoding 下同一 checkpoint 的 100 样本高度相关（如 ISR s43: 100% H7 = 系统性行为）。CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate。真实 evidence 可能仅有 seed-level permutation 水平 (p=0.26, n.s.)。R2 [AGREE]。建议 cluster-robust/GEE 方法或降低 CMH prominence。\"\n  action_items:\n    - round: 5\n      action: \"正文统计框架重组：CMH primary\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Appendix Table 4 重排: CMH 置于 Fisher 之前\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"(a) 正文讨论 within-seed 非独立性及对 CMH p-value 的 inflation 效应; (b) 使用 cluster-robust SE 或 GEE (seed as cluster) 重新分析并报告; (c) 或明确将 seed-level permutation test 作为主统计证据，承认 power 不足但 direction consistent; (d) 降低 CMH p<10⁻⁹ 的 prominence\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解释原因。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W6: s43 数据仍用于主文 §4.1 cross-seed claims。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 直接提及。\"\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"5-seed pooled N-H=23% 为未校正上限。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议报告区间 [6%, 23%]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W4 再次确认。3.7× 差距 (23% uncorrected vs 6.06% corrected) 完全由缺失 audit 数据造成。Table 1 ‡ 标注不够显著。\"\n  action_items:\n    - round: 5\n      action: \"正文明确标注 23% 为 uncorrected upper bound\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Table 1 ISR β=0.1 N-H 列报告为区间或标注 'upper bound'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"Table 1 caption 明确说明 'N-H=23% is uncorrected upper bound; corrected estimate on 3 auditable seeds is 6.06%'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"per-seed proved n=18-94，百分比信息量低。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W2 再次确认。n=18 (β=0.3 s42) 时 CI 极宽 (5.6% → [0.3%, 25.8%])。主文百分比缺少 uncertainty 量化。\"\n  action_items:\n    - round: 6\n      action: \"对 n<30 的 per-seed 结果报告 Wilson CI 而非仅点估计\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 升级为 critical。R1 [REBUT]: 已正确定位为 empirical contribution。Director 降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两位共识: 方法贡献薄，应更明确 position 为 empirical study。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3 再次提出。R1 交叉回应 [AGREE with nuance]: (1) LOO vs Shapley 和 O(1) variant 展示设计空间探索; (2) empirical study 中方法简单是优势; (3) 真正 contribution 在 reward formulation 和 taxonomy 方法论。R2 缓解因素评估准确。共识: 不扣重分但确认 novelty ceiling。\"\n  action_items:\n    - round: 6\n      action: \"Introduction 中更明确 position 为 empirical study\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据，与主文 5-seed 冲突\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Round 7 未被任何 Reviewer 提及。Appendix Table 5 (tab:fol-beta01-perseed) 现含完整 5-seed per-seed data (s42-s46)。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议 Table 1 增加 exec-only 3-seed 1000-step 行。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W6 再次提出。R2 [AGREE]。Table 1 exec-only 500-step 为 s42 单 seed (†标注)，cross-seed variance 极大 (s42=93%, s43=13%, s44=98%)。Table 1 已有 exec-only 1000-step 3-seed 行 (PR=97±2%)，但 500-step 行仍为单 seed。建议 500-step 也改为 3-seed pooled 或注明 range。\"\n  action_items:\n    - round: 5\n      action: \"Table 1 保持 s42 单 seed + 加强†脚注\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Table 1 增加 exec-only 3-seed 1000-step 行\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"Table 1 exec-only 500-step 行改为 3-seed pooled (PR=68±47%, ISR*=0.238±0.30)，或在 caption 注明 s42 单 seed 原因及 3-seed range\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R1 Excitement=3.5 部分不同意。降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N2 再次提出。R1 交叉 [AGREE with nuance]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3/Q1 再次提出。R1 交叉 [AGREE with nuance]: empirical 价值在于 calibrating 理论预测（哪些现象可预测，哪些不可）。建议论文更明确将实验定位为 verification + discovery。\"\n  action_items:\n    - round: 6\n      action: \"Framing 从 'we discover Goodhart effects' 转为 'Goodhart collapse is predictable, but these phenomena are not: [...]'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~15 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N3 再次提出。R1 [AGREE]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W2 再次确认，R1 [AGREE]。手动计数 11 个数值/统计量 in 4 sentences。'6 conditions, 2 logic types, 2 model scales' 可合并。建议保留 5-6 个关键数字。\"\n  action_items:\n    - round: 5\n      action: \"Abstract 删减到最多 3-4 个关键数字\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 7\n      action: \"Abstract 删减至 ≤6 关键数字; 删除 '6 conditions, 2 logic types, 2 model scales' 或合并为 'across multiple conditions'; 删除 β=0.1 具体值\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 \\\\paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 \\\\paragraph{} 小标题切割连贯叙事。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [REBUT] 认为结构清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [AGREE]: 前两段合理，但 'ISR as diagnostic' 和 'ISR as reward' 预支了 experiments 结论。建议合并为 'Key findings' 段。\"\n  action_items:\n    - round: 6\n      action: \"二选一: (a) 保留 paragraph 但精简每段数据密度; (b) 减少到 2-3 个 paragraph\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复且顺序非升序\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Low-dose/Micro-dose/Medium-dose/High-dose 四段格式高度重复。\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W2: β 呈现顺序 0.1→0.05→0.2→0.3。R1 [AGREE]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W4 再次确认，R1 [AGREE]。建议 §4.3 开头加 1-2 句总结性发现，然后按升序呈现。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 开头加 1-2 句 dose-response 总结; 按升序 0.05→0.1→0.2→0.3 呈现或解释当前顺序的叙事理由\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"Round 7 未被任何 Reviewer 提及。related_work.tex:20 现已指定 'primarily regressional, with extremal elements'。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"Round 7 未被任何 Reviewer 提及。experiments.tex:91-94 现已包含 reward landscape 分析。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"caption ~120 words + 6 脚注标记。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W5 [info]。R1 [AGREE] 但认为 ‡ (uncorrected upper bound) 标注对正确理解至关重要。建议折中: † 和 †† 解释移正文/Appendix，caption 仅保留 ‡ 和 *。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 caption 中 † 和 †† 的详细解释移入正文; caption 仅保留 ‡ 和 * 标注\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"100-step RL (PR=32%) 部分缓解但不完全。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"C1 'localizing the failure to RL' 证据链有 PR confound。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N3 [critical], R2 [REBUT to critical severity]: 论文 framing 已 cautious ('consistent with', 'plausible but not conclusive')。C1 表述用 'consistent with RL-specific failure'。Fisher p≈0.14 on 100-step data (R1 计算) 不显著。Director 裁决: R2 的 rebut 有效——论文 framing 确已 appropriate，但 C1 作为 contribution 的 prominence 与 evidence strength 不匹配。维持 warning。\"\n  action_items:\n    - round: 6\n      action: \"C1 弱化为 'consistent with RL-specific failure'; 正文承认 'whether SFT would hack at higher PR remains unknown'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"C1 进一步降低 prominence: 从独立 contribution 降级为 supporting observation; 或在 C1 描述中增加 'confounded by PR gap' 的显式 caveat\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Krakovna, Polu & Sutskever, Everitt。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"已加入。R2 新建议: Amodei et al. 2016, Geirhos et al. 2020, DeepSeek-R1 2025。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 建议增加 Goodhart 1975 原文或 Strathern 1997。R1 [AGREE]。Blog posts (METR, Krakovna) venue 格式需确认。\"\n  action_items:\n    - round: 7\n      action: \"(a) 增加 Goodhart 1975 或 Strathern 1997 经典引用; (b) 确认 blog posts/tech reports 的 BibTeX venue 格式符合 ACL 标准\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 6 issues — 状态更新 =====\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致: Abstract 'Irreducible Solver Rate' vs Method 'Intensional Structural Reward'\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Round 7 R2-S5 确认：'全文统一使用 Irreducible Solver Rate，Abstract/Introduction/Method 三处定义一致。' 命名不一致问题已修复。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性——论文结论恰恰是不应用作 reward\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Round 7 确认 ISR 统一为 'Irreducible Solver Rate'（不含 'Reward'）。问题已解决。\"\n  resolution_round: 7\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 基于 4 个 β 值、不均匀 seed 数，统计上不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"β=0.1 用 5 seeds 而 β=0.05/0.2/0.3 用 3 seeds。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N2 相关但独立角度。experiments.tex:124 'Non-monotonic dose-response' 作为 claim 统计上无法支撑。建议弱化为 'the pattern across four tested doses suggests...'。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 'Non-monotonic dose-response' 弱化为 descriptive pattern 而非 statistical claim\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 Goodhart Effects 的 β 值呈现顺序非升序 (0.1→0.05→0.2→0.3)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"升序呈现 + 最后 cross-dose synthesis 会更清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"与 v5-R2-W4 合并处理。\"\n  action_items:\n    - round: 7\n      action: \"与 v5-R2-W4 合并: 按 β 升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Round 7 确认 introduction.tex:14 现为 'component necessity testing (leave-one-out (LOO) ablation on solver inputs)'。首次使用已正式定义。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled，部分 mode 为单点观察\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 [REBUT]。Director 裁决: 降级为 info。\"\n    - round: 7\n      reviewers: [1]\n      note: \"R1-Q6 提及 taxonomy 需人工 H8 audit 的自动化限制，但未列为 weakness。共识: info 级。\"\n  action_items:\n    - round: 6\n      action: \"Table 2/Appendix 中标注每种 mode 的 evidence strength\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 7 新 issues =====\n\n- id: \"v7-R1-N2\"\n  summary: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate，需 cluster-robust 重分析\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 提出 [critical], R2 [AGREE]。CMH 假设 stratum 内独立，但 greedy decoding 下同一 checkpoint 的 100 样本是系统性行为（如 ISR s43: 100% H7）。真实独立观测为 seed (n=5) 非 sample (n=350/414)。需 cluster-robust SE/GEE 或降低 CMH prominence。与 v4-R1-N4 相关但从更基本的统计假设角度论述。\"\n  action_items:\n    - round: 7\n      action: \"与 v4-R1-N4 合并修复: (a) 正文新增段落讨论 within-seed 非独立性; (b) 报告 cluster-robust 分析或 GEE; (c) 将 seed-level permutation 作为 conservative bound 呈现; (d) CMH 降级为 'supportive but potentially inflated'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v7-R2-MR1\"\n  summary: \"缺少 Goodhart's Law 经典引用 (Goodhart 1975 或 Strathern 1997)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 [AGREE]。论文以 Goodhart's Law 为核心框架但仅引用 Manheim & Garrabrant 2019 taxonomy，缺少原始来源。\"\n  action_items:\n    - round: 7\n      action: \"Related Work 或 Introduction 增加 Goodhart 1975 或 Strathern 1997 引用\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v7-R2-W7\"\n  summary: \"experiments.tex:34 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W7 [info], R1 [AGREE]。单处出现，不严重但符合 §5.2 禁用模式。\"\n  action_items:\n    - round: 7\n      action: \"experiments.tex:34 'Notably, s43 recovers...' → 's43 recovers...'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4-7 carry-over (in_progress / open) =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W4 再次确认。§4.5 'No safe scale was observed' 仍为 n=1 seed 的存在性声明。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W6 再次确认。§4.5 title 应改为 'Preliminary Cross-Scale Evidence'。Introduction 用 'preliminarily observed' 但 §4.5 本身未用此 qualifier。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 新增段落声明 1-seed 限制\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 5\n      action: \"Abstract/Intro 'transfers'→'preliminarily observed at'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"§4.5 'No safe scale was observed' 改为 'No safe scale was observed in this single-seed comparison'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"§4.5 标题改为 'Preliminary Cross-Scale Evidence'; 正文中增加 'single-seed, preliminary' qualifier\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N1\"\n  summary: \"正文超页限制 (~8.5 页 vs ACL long paper 8 页)\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Round 7 两位 Reviewer 均未提及页数问题。R2 确认格式合规：正文 §1-§5 在 8 页内。\"\n  resolution_round: 7\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds/doses\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W4: β=0.3/0.05 仅 500-step snapshot。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 再次提出。R2 [AGREE]。'Trajectory-confirmed' 仅 β=0.1 的 2 个 seeds。β=0.2 的 100% H7 saturation 本身 sufficient 但 β=0.05/0.3 需区分 snapshot-observed vs trajectory-confirmed。\"\n  action_items:\n    - round: 5\n      action: \"软化 'at all tested doses' 措辞\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"弱化为 'collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"Abstract/Intro 中明确区分 'snapshot-observed (all doses)' vs 'trajectory-confirmed (β=0.1 only)'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"统计层级倒置; OR 反转正文一句带过。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N2 / R2 [AGREE]。CMH OR=3.37 方向与 5-seed Fisher 一致但 framing 不诚实。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N1 [critical], R2 [AGREE]。CMH OR=3.37 正文出现 3 次 vs corrected OR=0.61 仅 2 次且靠后。Table 1 仅 uncorrected N-H=23%*。Discussion 以 uncorrected 为主基调。'Suggestive but non-robust' 仍暗示正方向。需以 corrected 为 primary baseline。\"\n  action_items:\n    - round: 5\n      action: \"CMH 作为 primary test 移入正文; Abstract 删除 uncorrected OR\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"(a) 3-seed corrected OR=0.61 提升为 primary sensitivity; (b) 明确 'genuine-rate advantage is not robust to H8 correction'\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 7\n      action: \"(a) Table 1 N-H 列同时展示 uncorrected/corrected 或注明 corrected 值; (b) Discussion 以 corrected 为主基调; (c) Abstract 措辞改为 'genuine-rate advantage is not robust to classification methodology'; (d) 明确 'may be an artifact of uncorrected classification'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"CMH 检验的 within-seed 非独立性问题——真实独立样本量为 n=5 (seeds) 而非 n=350/414 (samples)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N5 再次提出。R2 [REBUT]: 正文已将 CMH 作为 primary。Director 降级为 warning。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N2 [critical] 升级论述。CMH 假设 stratum 内观测独立，但 greedy decoding 下同一 checkpoint 的 100 样本高度相关（如 ISR s43: 100% H7 = 系统性行为）。CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate。真实 evidence 可能仅有 seed-level permutation 水平 (p=0.26, n.s.)。R2 [AGREE]。建议 cluster-robust/GEE 方法或降低 CMH prominence。\"\n  action_items:\n    - round: 5\n      action: \"正文统计框架重组：CMH primary\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Appendix Table 4 重排: CMH 置于 Fisher 之前\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"(a) 正文讨论 within-seed 非独立性及对 CMH p-value 的 inflation 效应; (b) 使用 cluster-robust SE 或 GEE (seed as cluster) 重新分析并报告; (c) 或明确将 seed-level permutation test 作为主统计证据，承认 power 不足但 direction consistent; (d) 降低 CMH p<10⁻⁹ 的 prominence\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解释原因。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W6: s43 数据仍用于主文 §4.1 cross-seed claims。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 直接提及。\"\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"5-seed pooled N-H=23% 为未校正上限。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议报告区间 [6%, 23%]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W4 再次确认。3.7× 差距 (23% uncorrected vs 6.06% corrected) 完全由缺失 audit 数据造成。Table 1 ‡ 标注不够显著。\"\n  action_items:\n    - round: 5\n      action: \"正文明确标注 23% 为 uncorrected upper bound\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Table 1 ISR β=0.1 N-H 列报告为区间或标注 'upper bound'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"Table 1 caption 明确说明 'N-H=23% is uncorrected upper bound; corrected estimate on 3 auditable seeds is 6.06%'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"per-seed proved n=18-94，百分比信息量低。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W2 再次确认。n=18 (β=0.3 s42) 时 CI 极宽 (5.6% → [0.3%, 25.8%])。主文百分比缺少 uncertainty 量化。\"\n  action_items:\n    - round: 6\n      action: \"对 n<30 的 per-seed 结果报告 Wilson CI 而非仅点估计\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 升级为 critical。R1 [REBUT]: 已正确定位为 empirical contribution。Director 降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两位共识: 方法贡献薄，应更明确 position 为 empirical study。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3 再次提出。R1 交叉回应 [AGREE with nuance]: (1) LOO vs Shapley 和 O(1) variant 展示设计空间探索; (2) empirical study 中方法简单是优势; (3) 真正 contribution 在 reward formulation 和 taxonomy 方法论。R2 缓解因素评估准确。共识: 不扣重分但确认 novelty ceiling。\"\n  action_items:\n    - round: 6\n      action: \"Introduction 中更明确 position 为 empirical study\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据，与主文 5-seed 冲突\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Round 7 未被任何 Reviewer 提及。Appendix Table 5 (tab:fol-beta01-perseed) 现含完整 5-seed per-seed data (s42-s46)。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议 Table 1 增加 exec-only 3-seed 1000-step 行。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W6 再次提出。R2 [AGREE]。Table 1 exec-only 500-step 为 s42 单 seed (†标注)，cross-seed variance 极大 (s42=93%, s43=13%, s44=98%)。Table 1 已有 exec-only 1000-step 3-seed 行 (PR=97±2%)，但 500-step 行仍为单 seed。建议 500-step 也改为 3-seed pooled 或注明 range。\"\n  action_items:\n    - round: 5\n      action: \"Table 1 保持 s42 单 seed + 加强†脚注\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 6\n      action: \"Table 1 增加 exec-only 3-seed 1000-step 行\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"Table 1 exec-only 500-step 行改为 3-seed pooled (PR=68±47%, ISR*=0.238±0.30)，或在 caption 注明 s42 单 seed 原因及 3-seed range\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R1 Excitement=3.5 部分不同意。降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N2 再次提出。R1 交叉 [AGREE with nuance]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3/Q1 再次提出。R1 交叉 [AGREE with nuance]: empirical 价值在于 calibrating 理论预测（哪些现象可预测，哪些不可）。建议论文更明确将实验定位为 verification + discovery。\"\n  action_items:\n    - round: 6\n      action: \"Framing 从 'we discover Goodhart effects' 转为 'Goodhart collapse is predictable, but these phenomena are not: [...]'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~15 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N3 再次提出。R1 [AGREE]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W2 再次确认，R1 [AGREE]。手动计数 11 个数值/统计量 in 4 sentences。'6 conditions, 2 logic types, 2 model scales' 可合并。建议保留 5-6 个关键数字。\"\n  action_items:\n    - round: 5\n      action: \"Abstract 删减到最多 3-4 个关键数字\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 7\n      action: \"Abstract 删减至 ≤6 关键数字; 删除 '6 conditions, 2 logic types, 2 model scales' 或合并为 'across multiple conditions'; 删除 β=0.1 具体值\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 \\\\paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 \\\\paragraph{} 小标题切割连贯叙事。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [REBUT] 认为结构清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [AGREE]: 前两段合理，但 'ISR as diagnostic' 和 'ISR as reward' 预支了 experiments 结论。建议合并为 'Key findings' 段。\"\n  action_items:\n    - round: 6\n      action: \"二选一: (a) 保留 paragraph 但精简每段数据密度; (b) 减少到 2-3 个 paragraph\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复且顺序非升序\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Low-dose/Micro-dose/Medium-dose/High-dose 四段格式高度重复。\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W2: β 呈现顺序 0.1→0.05→0.2→0.3。R1 [AGREE]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W4 再次确认，R1 [AGREE]。建议 §4.3 开头加 1-2 句总结性发现，然后按升序呈现。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 开头加 1-2 句 dose-response 总结; 按升序 0.05→0.1→0.2→0.3 呈现或解释当前顺序的叙事理由\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"Round 7 未被任何 Reviewer 提及。related_work.tex:20 现已指定 'primarily regressional, with extremal elements'。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"Round 7 未被任何 Reviewer 提及。experiments.tex:91-94 现已包含 reward landscape 分析。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"caption ~120 words + 6 脚注标记。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W5 [info]。R1 [AGREE] 但认为 ‡ (uncorrected upper bound) 标注对正确理解至关重要。建议折中: † 和 †† 解释移正文/Appendix，caption 仅保留 ‡ 和 *。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 caption 中 † 和 †† 的详细解释移入正文; caption 仅保留 ‡ 和 * 标注\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"100-step RL (PR=32%) 部分缓解但不完全。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"C1 'localizing the failure to RL' 证据链有 PR confound。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N3 [critical], R2 [REBUT to critical severity]: 论文 framing 已 cautious ('consistent with', 'plausible but not conclusive')。C1 表述用 'consistent with RL-specific failure'。Fisher p≈0.14 on 100-step data (R1 计算) 不显著。Director 裁决: R2 的 rebut 有效——论文 framing 确已 appropriate，但 C1 作为 contribution 的 prominence 与 evidence strength 不匹配。维持 warning。\"\n  action_items:\n    - round: 6\n      action: \"C1 弱化为 'consistent with RL-specific failure'; 正文承认 'whether SFT would hack at higher PR remains unknown'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 7\n      action: \"C1 进一步降低 prominence: 从独立 contribution 降级为 supporting observation; 或在 C1 描述中增加 'confounded by PR gap' 的显式 caveat\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Krakovna, Polu & Sutskever, Everitt。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"已加入。R2 新建议: Amodei et al. 2016, Geirhos et al. 2020, DeepSeek-R1 2025。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 建议增加 Goodhart 1975 原文或 Strathern 1997。R1 [AGREE]。Blog posts (METR, Krakovna) venue 格式需确认。\"\n  action_items:\n    - round: 7\n      action: \"(a) 增加 Goodhart 1975 或 Strathern 1997 经典引用; (b) 确认 blog posts/tech reports 的 BibTeX venue 格式符合 ACL 标准\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 6 issues — 状态更新 =====\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致: Abstract 'Irreducible Solver Rate' vs Method 'Intensional Structural Reward'\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Round 7 R2-S5 确认：'全文统一使用 Irreducible Solver Rate，Abstract/Introduction/Method 三处定义一致。' 命名不一致问题已修复。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性——论文结论恰恰是不应用作 reward\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Round 7 确认 ISR 统一为 'Irreducible Solver Rate'（不含 'Reward'）。问题已解决。\"\n  resolution_round: 7\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 基于 4 个 β 值、不均匀 seed 数，统计上不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"β=0.1 用 5 seeds 而 β=0.05/0.2/0.3 用 3 seeds。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N2 相关但独立角度。experiments.tex:124 'Non-monotonic dose-response' 作为 claim 统计上无法支撑。建议弱化为 'the pattern across four tested doses suggests...'。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 'Non-monotonic dose-response' 弱化为 descriptive pattern 而非 statistical claim\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 Goodhart Effects 的 β 值呈现顺序非升序 (0.1→0.05→0.2→0.3)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"升序呈现 + 最后 cross-dose synthesis 会更清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"与 v5-R2-W4 合并处理。\"\n  action_items:\n    - round: 7\n      action: \"与 v5-R2-W4 合并: 按 β 升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Round 7 确认 introduction.tex:14 现为 'component necessity testing (leave-one-out (LOO) ablation on solver inputs)'。首次使用已正式定义。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled，部分 mode 为单点观察\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 [REBUT]。Director 裁决: 降级为 info。\"\n    - round: 7\n      reviewers: [1]\n      note: \"R1-Q6 提及 taxonomy 需人工 H8 audit 的自动化限制，但未列为 weakness。共识: info 级。\"\n  action_items:\n    - round: 6\n      action: \"Table 2/Appendix 中标注每种 mode 的 evidence strength\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n# ===== Round 7 新 issues =====\n\n- id: \"v7-R1-N2\"\n  summary: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate，需 cluster-robust 重分析\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 提出 [critical], R2 [AGREE]。CMH 假设 stratum 内独立，但 greedy decoding 下同一 checkpoint 的 100 样本是系统性行为（如 ISR s43: 100% H7）。真实独立观测为 seed (n=5) 非 sample (n=350/414)。需 cluster-robust SE/GEE 或降低 CMH prominence。与 v4-R1-N4 相关但从更基本的统计假设角度论述。\"\n  action_items:\n    - round: 7\n      action: \"与 v4-R1-N4 合并修复: (a) 正文新增段落讨论 within-seed 非独立性; (b) 报告 cluster-robust 分析或 GEE; (c) 将 seed-level permutation 作为 conservative bound 呈现; (d) CMH 降级为 'supportive but potentially inflated'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v7-R2-MR1\"\n  summary: \"缺少 Goodhart's Law 经典引用 (Goodhart 1975 或 Strathern 1997)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 [AGREE]。论文以 Goodhart's Law 为核心框架但仅引用 Manheim & Garrabrant 2019 taxonomy，缺少原始来源。\"\n  action_items:\n    - round: 7\n      action: \"Related Work 或 Introduction 增加 Goodhart 1975 或 Strathern 1997 引用\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v7-R2-W7\"\n  summary: \"experiments.tex:34 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W7 [info], R1 [AGREE]。单处出现，不严重但符合 §5.2 禁用模式。\"\n  action_items:\n    - round: 7\n      action: \"experiments.tex:34 'Notably, s43 recovers...' → 's43 recovers...'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-17T17:22:23.518521+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 30147}, \"error\": \"\"}"}

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

_source line 602 · 2026-05-17T17:24:26.840458+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 7\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**目标 venue**: EMNLP 2026 (ACL Rolling Review, deadline 2026-05-25)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法/实验/统计; R2: 新颖性/写作/格式）\n**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，通过 leave-one-out ablation 计算 Irreducible Solver Rate (ISR)，诊断 GRPO 训练中 neurosymbolic formalizer 的结构性退化。核心发现：(1) ISR 揭示 execution-only 评估不可见的 99.5% 结构崩溃；(2) ISR 作为 reward 信号在全部 4 个测试剂量下触发 Goodhart collapse；(3) 九种 hacking 模式跨逻辑类型和模型规模出现。论文定位为 empirical study，实验设计严谨、学术诚实度高，但关键统计推断存在系统性问题。\n\n---\n\n## Strengths\n\n1. **研究问题重要且 timely**：在 RL-for-reasoning 快速发展的背景下，系统性记录 neurosymbolic 设置中的 reward hacking 对该领域有直接指导价值。[R1-S1, R2-S1 共识]\n\n2. **实验设计的对照结构合理**：6 个 reward 条件、matched random control（隔离 ISR-specific vs generic reward-variance）、SFT baseline（隔离 RL-specific vs data-driven）、5 seeds 用于主实验，设计深思熟虑。[R1-S2, R2-S2 共识]\n\n3. **罕见的学术诚实度**：主动披露 OR 方向反转（corrected OR=0.61）、premise-count confound 消除效果（1.06×）、deleted checkpoints 导致 N-H 为 upper bound、SFT PR gap confound 等不利证据。[R1-S3, R2-S4 共识]\n\n4. **Trajectory analysis 超越 snapshot 评估**：1000-step 扩展训练证明 transient genuine window 是暂时的，方法论主张本身对社区有贡献。[R1-S4]\n\n5. **九模式 hacking taxonomy 有分类学价值**：H7b（obfuscated tautology, triple gaming）、query-as-fact gaming 此前未记录。Cross-logic transfer 和 cross-scale evidence 增加普适性。[R1-S5, R2-S3 共识]\n\n6. **Premise-count confound 处理充分**：正文明确指出 ISR 对 component count 的敏感性，premise-count-matched comparison 诚实展示控制后效果消失。[R1-S6]\n\n7. **格式合规**：ACL template review mode、double-blind、正文 8 页内、Limitations/Ethics 位置正确、ISR 命名全文一致。[R2-S5]\n\n---\n\n## Weaknesses\n\n### Critical (影响接收决定)\n\n**C1. OR 方向反转的 framing 偏向 uncorrected 结果** [R1-N1, R2 AGREE]\n\n5-seed uncorrected CMH OR=3.37 (p<10⁻⁹) vs 3-seed H8+FN-corrected OR=0.61 (n.s.)。方向从 \"ISR 显著优于 random\" 反转为 \"ISR 略逊于 random\"。Table 1 主表仅展示 uncorrected N-H=23%*；Discussion 以 OR=3.37 为开头；corrected 结果仅以 \"under stricter classification the effect reverses\" 一笔带过。对于 corrected analysis 反转方向的情况，uncorrected 结果不应作为主要叙事。\n\n**C2. CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate** [R1-N2, R2 AGREE]\n\nCMH 假设 stratum（seed）内观测独立。但每个 seed 内的 100 个 evaluation samples 来自同一 checkpoint、greedy decoding，是系统性行为（如 ISR s43: 100% H7）。真正的独立观测单位是 seed (n=5)，非 sample (n=350/414)。Seed-level permutation tests 得 p=0.26 (n.s.)。CMH p<10⁻⁹ 作为主要统计证据存在严重的方法论隐患，论文未讨论此问题。\n\n### Warning (影响评分但不致命)\n\n**W1. \"Goodhart collapse at all tested doses\" 的 trajectory evidence 仅覆盖 β=0.1** [R1-W1, R2 AGREE]\n\nTrajectory-confirmed 仅 β=0.1 的 2 个 seeds (s42, s45)。β=0.05/0.2/0.3 均为 500-step snapshot only。论文自身方法论主张 \"snapshot evaluation would overestimate\"，但对自己其他 doses 的 claims 使用了 snapshot evidence。\n\n**W2. SFT baseline PR confound 使 C1 \"RL-specific\" attribution 证据受限** [R1-N3 critical → Director 裁决 warning; R2 REBUT severity]\n\nSFT PR=13% vs exec-only PR=93%。低 PR 本身减少 hacking 机会。100-step checkpoint (PR=32%) 部分缓解但 Fisher p≈0.14 不显著。论文 framing 已用 \"consistent with\"（非 \"proves\"），R2 的 rebut 有效，但 C1 作为独立 contribution 的 prominence 与 evidence strength 不匹配。\n\n**W3. Cross-scale 1.7B 仅 single seed** [R1-W3, R2-W6 共识]\n\n4B 实验已证明 cross-seed variance 极大（σ=47pp），但 1.7B 仅 1 seed。§4.5 标题 \"Cross-Scale Evidence\" 未用 \"preliminary\" qualifier。\n\n**W4. Deleted checkpoints 造成数据完整性缺口** [R1-W4, R2 context]\n\nISR β=0.1 s43/s44 checkpoints 丢失，5-seed pooled N-H=23% 为 uncorrected upper bound，corrected=6.06%（3.7× 差距）。Table 1 ‡ 标注不够显著。\n\n**W5. Table 1 exec-only 500-step baseline 为 single seed (s42)** [R1-W6, R2 AGREE]\n\nCross-seed variance 极大（s42=93%, s43=13%, s44=98%），单 seed 不具代表性。建议改为 3-seed pooled 或注明 range。\n\n**W6. Abstract 仍偏数据堆砌 (11 个数值/统计量 in 4 sentences)** [R2-W2, R1 AGREE]\n\n审稿人在 30 秒内难以提取核心 insight。\"6 conditions, 2 logic types, 2 model scales\" 是纯规模描述可删减。\n\n**W7. Introduction 5 个 \\paragraph{} 叙事碎片化** [R2-W1, R1 AGREE]\n\n\"ISR as diagnostic\" 和 \"ISR as reward\" 两段预支 experiments 结论。建议合并为 \"Key findings\" 段。\n\n**W8. §4.3 β 呈现顺序非升序 (0.1→0.05→0.2→0.3)** [R2-W4, R1 AGREE]\n\n读者难以构建 dose-response 心理模型。建议开头加总结 + 按升序呈现。\n\n**W9. 方法新颖性有限 (Algorithm 1 仅 6 行 LOO)** [R2-W3, R1 AGREE with nuance]\n\nSTA 本质是标准 LOO mutation testing 的应用。\"Diagnostic becomes optimization target\" 是 Goodhart 直接推论。缓解因素：论文正确定位为 empirical study；LOO vs Shapley + O(1) variant 展示了设计空间探索。\n\n**W10. 100 eval samples per-seed 统计 precision 低** [R1-W2, R2 context]\n\nn=18 (β=0.3 s42) 时 CI 极宽 (5.6% → [0.3%, 25.8%])。主文百分比缺 uncertainty 量化。\n\n**W11. Dose-response claim 统计上不足** [from v6-R1-W2, both agree]\n\nβ=0.1 用 5 seeds 而 β=0.05/0.2/0.3 用 3 seeds。\"Non-monotonic dose-response\" 作为 statistical claim 无法支撑。\n\n### Info\n\n**I1.** Table 1 caption ~80 words + 4 脚注符号，可读性待改善 [R2-W5, R1 AGREE]\n**I2.** experiments.tex:34 \"Notably\" AI 写作标记 [R2-W7, R1 AGREE]\n**I3.** 缺少 Goodhart 1975 或 Strathern 1997 经典引用 [R2-Missing-3, R1 AGREE]\n**I4.** Blog posts (METR, Krakovna) 的 BibTeX venue 格式需确认 [R2-Q4]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. ISR collapse trajectory (Figure 2) 和 \"diagnostic reliable, optimizer unreliable\" 的核心发现成立且有价值\n2. OR 方向反转 (3.37 → 0.61) 的 framing 偏向 uncorrected，需以 corrected 为主基调\n3. CMH within-seed 非独立性是方法论隐患，p<10⁻⁹ 可能被严重 inflate\n4. 方法 novelty 有限但论文定位（empirical study）正确\n5. 九模式 taxonomy 有分类学贡献\n6. 1.7B cross-scale 仅 single seed，需标注 preliminary\n7. Abstract 数据堆砌、Introduction 碎片化、β 呈现顺序均需改善\n\n## Reviewer Divergence [REBUT]\n\n1. **N3/SFT PR confound severity**: R1 评 critical，R2 rebut 至 warning（论文 framing 已 cautious，用 \"consistent with\"）。**Director 裁决: warning**——论文措辞已适当但 C1 prominence 与 evidence 不匹配。\n\n2. **W5/ISR diagnostic ROC curve**: R1 要求 per-sample sensitivity/specificity，R2 rebut（ISR 是 population-level trend indicator，配合 text-match+functional taxonomy 做分类）。**Director 裁决: R2 rebut 成立**——ISR 设计为 aggregate diagnostic，不需要 per-sample threshold。降为建议而非 weakness。\n\n---\n\n## Questions (需作者 rebuttal)\n\n1. CMH 检验的 within-seed 独立性假设如何论证？是否有 cluster-robust 重分析结果？\n2. Corrected OR=0.61 (n.s.) 下，\"transient genuine window\" 是真实效应还是 uncorrected classification 的 artifact？\n3. 100-step exec-only vs SFT 的 Fisher exact p-value 是多少？\n4. β=0.05/0.2/0.3 无 1000-step trajectory，\"β controls timing not whether\" 是否过强？\n5. ISR 的 Goodhart vulnerability (ISR≥0.5 for tautology) 在设计时是否可预见？如是，4-dose 实验是 verification 还是 discovery？\n6. Premise-count-matched comparison 消除 ISR advantage (1.06×)——ISR reward 的\"正面\"效果是否仅为鼓励 shorter outputs？\n\n---\n\n## Missing References\n\n1. **Goodhart 1975** \"Problems of Monetary Management\" 或 **Strathern 1997** 经典改写——以 Goodhart's Law 为核心框架但缺原始来源 [R1+R2 共识]\n2. **Cluster-robust / GEE 方法**——与 C2 统计问题相关的方法论引用\n3. Blog posts/tech reports (METR, Krakovna 2020) 的 venue 格式需确认是否符合 ACL BibTeX 标准\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3.25/5 |\n| Reproducibility | 3/5 | 4/5 | 3.5/5 |\n| Overall | 3.0 | 3.5 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n\n核心现象（ISR diagnostic reveals collapse invisible to PR; Goodhart collapse across doses; nine hacking modes）有说服力，对 RL-for-reasoning 社区有直接警示价值。实验设计用心、学术诚实度高。\n\n然而，作为一篇以 empirical evidence 为核心的论文，两个 critical 级统计问题（OR 方向反转 framing、CMH 非独立性）动摇了 quantitative claims 的可靠性。\"Transient genuine window\" 的 evidence 在 corrected analysis 下方向反转；CMH p<10⁻⁹ 在 within-seed 非独立性下可能被严重 inflate；SFT \"RL-specific\" attribution 受 PR confound 限制。这些问题叠加，使论文的 robustness 不足以支持主会议接收。\n\n**建议投递 Findings track。** 如能在 rebuttal 中：(a) 提供 cluster-robust/GEE 重分析，(b) 以 corrected OR 为主基调重新 frame genuine window，(c) 降低 C1 prominence，则有望升至 Borderline Conference (3.5)。\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- 11 个数值/统计量过密，删减至 ≤6 个关键数字\n- \"suggestive but non-robust improvement\" 应改为更明确的 \"genuine-rate advantage is not robust to classification methodology\"\n- \"6 conditions, 2 logic types, 2 model scales\" 合并为 \"across multiple conditions and settings\"\n\n### Introduction\n- 5 个 \\paragraph{} 碎片化叙事；\"ISR as diagnostic\"/\"ISR as reward\" 预支 experiments 结论\n- 建议合并为 2-3 个 \\paragraph{}（背景+问题、方法+概述、贡献）\n- 更明确 position 为 empirical study（\"Goodhart collapse is predictable, but these phenomena are not: [stochastic bifurcation, non-monotonic dose-response, triple gaming]\"）\n\n### Method\n- Algorithm 1 (6 行) 方法 novelty 有限，但 LOO vs Shapley 讨论和 O(1) variant 展示了设计空间\n- Premise-count confound 讨论充分（正文 §3.2）\n\n### Experiments\n- §4.2: SFT comparison 的 C1 \"RL-specific\" claim 需降级为 supporting observation\n- §4.3: β 呈现顺序改为升序或开头加 dose-response 总结\n- §4.3: \"Non-monotonic dose-response\" 降为 descriptive pattern\n- §4.5: 标题改为 \"Preliminary Cross-Scale Evidence\"\n- Table 1: exec-only 500-step 改为 3-seed pooled 或注明 range; N-H 列增加 corrected 值; caption 精简\n\n### Discussion\n- 以 corrected OR=0.61 为主基调，uncorrected 作 upper bound\n- 增加 within-seed 非独立性讨论段落\n\n### Statistics\n- 正文新增段落讨论 CMH 的 within-seed 非独立性假设及其对 p-value 的 inflation 效应\n- 报告 cluster-robust SE 或 GEE (seed as cluster) 重分析\n- 或明确以 seed-level permutation test 为 conservative bound (direction consistent, power limited)\n- 降低 \"p<10⁻⁹\" 的 prominence\n\n### Format\n- experiments.tex:34 \"Notably\" → 直接写\n- Table 1 caption 精简（† †† 解释移正文）\n- 增加 Goodhart 1975/Strathern 1997 引用\n- Blog posts BibTeX 格式确认",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
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
    "report": "# 审稿报告 — Round 7\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**目标 venue**: EMNLP 2026 (ACL Rolling Review, deadline 2026-05-25)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法/实验/统计; R2: 新颖性/写作/格式）\n**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，通过 leave-one-out ablation 计算 Irreducible Solver Rate (ISR)，诊断 GRPO 训练中 neurosymbolic formalizer 的结构性退化。核心发现：(1) ISR 揭示 execution-only 评估不可见的 99.5% 结构崩溃；(2) ISR 作为 reward 信号在全部 4 个测试剂量下触发 Goodhart collapse；(3) 九种 hacking 模式跨逻辑类型和模型规模出现。论文定位为 empirical study，实验设计严谨、学术诚实度高，但关键统计推断存在系统性问题。\n\n---\n\n## Strengths\n\n1. **研究问题重要且 timely**：在 RL-for-reasoning 快速发展的背景下，系统性记录 neurosymbolic 设置中的 reward hacking 对该领域有直接指导价值。[R1-S1, R2-S1 共识]\n\n2. **实验设计的对照结构合理**：6 个 reward 条件、matched random control（隔离 ISR-specific vs generic reward-variance）、SFT baseline（隔离 RL-specific vs data-driven）、5 seeds 用于主实验，设计深思熟虑。[R1-S2, R2-S2 共识]\n\n3. **罕见的学术诚实度**：主动披露 OR 方向反转（corrected OR=0.61）、premise-count confound 消除效果（1.06×）、deleted checkpoints 导致 N-H 为 upper bound、SFT PR gap confound 等不利证据。[R1-S3, R2-S4 共识]\n\n4. **Trajectory analysis 超越 snapshot 评估**：1000-step 扩展训练证明 transient genuine window 是暂时的，方法论主张本身对社区有贡献。[R1-S4]\n\n5. **九模式 hacking taxonomy 有分类学价值**：H7b（obfuscated tautology, triple gaming）、query-as-fact gaming 此前未记录。Cross-logic transfer 和 cross-scale evidence 增加普适性。[R1-S5, R2-S3 共识]\n\n6. **Premise-count confound 处理充分**：正文明确指出 ISR 对 component count 的敏感性，premise-count-matched comparison 诚实展示控制后效果消失。[R1-S6]\n\n7. **格式合规**：ACL template review mode、double-blind、正文 8 页内、Limitations/Ethics 位置正确、ISR 命名全文一致。[R2-S5]\n\n---\n\n## Weaknesses\n\n### Critical (影响接收决定)\n\n**C1. OR 方向反转的 framing 偏向 uncorrected 结果** [R1-N1, R2 AGREE]\n\n5-seed uncorrected CMH OR=3.37 (p<10⁻⁹) vs 3-seed H8+FN-corrected OR=0.61 (n.s.)。方向从 \"ISR 显著优于 random\" 反转为 \"ISR 略逊于 random\"。Table 1 主表仅展示 uncorrected N-H=23%*；Discussion 以 OR=3.37 为开头；corrected 结果仅以 \"under stricter classification the effect reverses\" 一笔带过。对于 corrected analysis 反转方向的情况，uncorrected 结果不应作为主要叙事。\n\n**C2. CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate** [R1-N2, R2 AGREE]\n\nCMH 假设 stratum（seed）内观测独立。但每个 seed 内的 100 个 evaluation samples 来自同一 checkpoint、greedy decoding，是系统性行为（如 ISR s43: 100% H7）。真正的独立观测单位是 seed (n=5)，非 sample (n=350/414)。Seed-level permutation tests 得 p=0.26 (n.s.)。CMH p<10⁻⁹ 作为主要统计证据存在严重的方法论隐患，论文未讨论此问题。\n\n### Warning (影响评分但不致命)\n\n**W1. \"Goodhart collapse at all tested doses\" 的 trajectory evidence 仅覆盖 β=0.1** [R1-W1, R2 AGREE]\n\nTrajectory-confirmed 仅 β=0.1 的 2 个 seeds (s42, s45)。β=0.05/0.2/0.3 均为 500-step snapshot only。论文自身方法论主张 \"snapshot evaluation would overestimate\"，但对自己其他 doses 的 claims 使用了 snapshot evidence。\n\n**W2. SFT baseline PR confound 使 C1 \"RL-specific\" attribution 证据受限** [R1-N3 critical → Director 裁决 warning; R2 REBUT severity]\n\nSFT PR=13% vs exec-only PR=93%。低 PR 本身减少 hacking 机会。100-step checkpoint (PR=32%) 部分缓解但 Fisher p≈0.14 不显著。论文 framing 已用 \"consistent with\"（非 \"proves\"），R2 的 rebut 有效，但 C1 作为独立 contribution 的 prominence 与 evidence strength 不匹配。\n\n**W3. Cross-scale 1.7B 仅 single seed** [R1-W3, R2-W6 共识]\n\n4B 实验已证明 cross-seed variance 极大（σ=47pp），但 1.7B 仅 1 seed。§4.5 标题 \"Cross-Scale Evidence\" 未用 \"preliminary\" qualifier。\n\n**W4. Deleted checkpoints 造成数据完整性缺口** [R1-W4, R2 context]\n\nISR β=0.1 s43/s44 checkpoints 丢失，5-seed pooled N-H=23% 为 uncorrected upper bound，corrected=6.06%（3.7× 差距）。Table 1 ‡ 标注不够显著。\n\n**W5. Table 1 exec-only 500-step baseline 为 single seed (s42)** [R1-W6, R2 AGREE]\n\nCross-seed variance 极大（s42=93%, s43=13%, s44=98%），单 seed 不具代表性。建议改为 3-seed pooled 或注明 range。\n\n**W6. Abstract 仍偏数据堆砌 (11 个数值/统计量 in 4 sentences)** [R2-W2, R1 AGREE]\n\n审稿人在 30 秒内难以提取核心 insight。\"6 conditions, 2 logic types, 2 model scales\" 是纯规模描述可删减。\n\n**W7. Introduction 5 个 \\paragraph{} 叙事碎片化** [R2-W1, R1 AGREE]\n\n\"ISR as diagnostic\" 和 \"ISR as reward\" 两段预支 experiments 结论。建议合并为 \"Key findings\" 段。\n\n**W8. §4.3 β 呈现顺序非升序 (0.1→0.05→0.2→0.3)** [R2-W4, R1 AGREE]\n\n读者难以构建 dose-response 心理模型。建议开头加总结 + 按升序呈现。\n\n**W9. 方法新颖性有限 (Algorithm 1 仅 6 行 LOO)** [R2-W3, R1 AGREE with nuance]\n\nSTA 本质是标准 LOO mutation testing 的应用。\"Diagnostic becomes optimization target\" 是 Goodhart 直接推论。缓解因素：论文正确定位为 empirical study；LOO vs Shapley + O(1) variant 展示了设计空间探索。\n\n**W10. 100 eval samples per-seed 统计 precision 低** [R1-W2, R2 context]\n\nn=18 (β=0.3 s42) 时 CI 极宽 (5.6% → [0.3%, 25.8%])。主文百分比缺 uncertainty 量化。\n\n**W11. Dose-response claim 统计上不足** [from v6-R1-W2, both agree]\n\nβ=0.1 用 5 seeds 而 β=0.05/0.2/0.3 用 3 seeds。\"Non-monotonic dose-response\" 作为 statistical claim 无法支撑。\n\n### Info\n\n**I1.** Table 1 caption ~80 words + 4 脚注符号，可读性待改善 [R2-W5, R1 AGREE]\n**I2.** experiments.tex:34 \"Notably\" AI 写作标记 [R2-W7, R1 AGREE]\n**I3.** 缺少 Goodhart 1975 或 Strathern 1997 经典引用 [R2-Missing-3, R1 AGREE]\n**I4.** Blog posts (METR, Krakovna) 的 BibTeX venue 格式需确认 [R2-Q4]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. ISR collapse trajectory (Figure 2) 和 \"diagnostic reliable, optimizer unreliable\" 的核心发现成立且有价值\n2. OR 方向反转 (3.37 → 0.61) 的 framing 偏向 uncorrected，需以 corrected 为主基调\n3. CMH within-seed 非独立性是方法论隐患，p<10⁻⁹ 可能被严重 inflate\n4. 方法 novelty 有限但论文定位（empirical study）正确\n5. 九模式 taxonomy 有分类学贡献\n6. 1.7B cross-scale 仅 single seed，需标注 preliminary\n7. Abstract 数据堆砌、Introduction 碎片化、β 呈现顺序均需改善\n\n## Reviewer Divergence [REBUT]\n\n1. **N3/SFT PR confound severity**: R1 评 critical，R2 rebut 至 warning（论文 framing 已 cautious，用 \"consistent with\"）。**Director 裁决: warning**——论文措辞已适当但 C1 prominence 与 evidence 不匹配。\n\n2. **W5/ISR diagnostic ROC curve**: R1 要求 per-sample sensitivity/specificity，R2 rebut（ISR 是 population-level trend indicator，配合 text-match+functional taxonomy 做分类）。**Director 裁决: R2 rebut 成立**——ISR 设计为 aggregate diagnostic，不需要 per-sample threshold。降为建议而非 weakness。\n\n---\n\n## Questions (需作者 rebuttal)\n\n1. CMH 检验的 within-seed 独立性假设如何论证？是否有 cluster-robust 重分析结果？\n2. Corrected OR=0.61 (n.s.) 下，\"transient genuine window\" 是真实效应还是 uncorrected classification 的 artifact？\n3. 100-step exec-only vs SFT 的 Fisher exact p-value 是多少？\n4. β=0.05/0.2/0.3 无 1000-step trajectory，\"β controls timing not whether\" 是否过强？\n5. ISR 的 Goodhart vulnerability (ISR≥0.5 for tautology) 在设计时是否可预见？如是，4-dose 实验是 verification 还是 discovery？\n6. Premise-count-matched comparison 消除 ISR advantage (1.06×)——ISR reward 的\"正面\"效果是否仅为鼓励 shorter outputs？\n\n---\n\n## Missing References\n\n1. **Goodhart 1975** \"Problems of Monetary Management\" 或 **Strathern 1997** 经典改写——以 Goodhart's Law 为核心框架但缺原始来源 [R1+R2 共识]\n2. **Cluster-robust / GEE 方法**——与 C2 统计问题相关的方法论引用\n3. Blog posts/tech reports (METR, Krakovna 2020) 的 venue 格式需确认是否符合 ACL BibTeX 标准\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3.25/5 |\n| Reproducibility | 3/5 | 4/5 | 3.5/5 |\n| Overall | 3.0 | 3.5 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n\n核心现象（ISR diagnostic reveals collapse invisible to PR; Goodhart collapse across doses; nine hacking modes）有说服力，对 RL-for-reasoning 社区有直接警示价值。实验设计用心、学术诚实度高。\n\n然而，作为一篇以 empirical evidence 为核心的论文，两个 critical 级统计问题（OR 方向反转 framing、CMH 非独立性）动摇了 quantitative claims 的可靠性。\"Transient genuine window\" 的 evidence 在 corrected analysis 下方向反转；CMH p<10⁻⁹ 在 within-seed 非独立性下可能被严重 inflate；SFT \"RL-specific\" attribution 受 PR confound 限制。这些问题叠加，使论文的 robustness 不足以支持主会议接收。\n\n**建议投递 Findings track。** 如能在 rebuttal 中：(a) 提供 cluster-robust/GEE 重分析，(b) 以 corrected OR 为主基调重新 frame genuine window，(c) 降低 C1 prominence，则有望升至 Borderline Conference (3.5)。\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- 11 个数值/统计量过密，删减至 ≤6 个关键数字\n- \"suggestive but non-robust improvement\" 应改为更明确的 \"genuine-rate advantage is not robust to classification methodology\"\n- \"6 conditions, 2 logic types, 2 model scales\" 合并为 \"across multiple conditions and settings\"\n\n### Introduction\n- 5 个 \\paragraph{} 碎片化叙事；\"ISR as diagnostic\"/\"ISR as reward\" 预支 experiments 结论\n- 建议合并为 2-3 个 \\paragraph{}（背景+问题、方法+概述、贡献）\n- 更明确 position 为 empirical study（\"Goodhart collapse is predictable, but these phenomena are not: [stochastic bifurcation, non-monotonic dose-response, triple gaming]\"）\n\n### Method\n- Algorithm 1 (6 行) 方法 novelty 有限，但 LOO vs Shapley 讨论和 O(1) variant 展示了设计空间\n- Premise-count confound 讨论充分（正文 §3.2）\n\n### Experiments\n- §4.2: SFT comparison 的 C1 \"RL-specific\" claim 需降级为 supporting observation\n- §4.3: β 呈现顺序改为升序或开头加 dose-response 总结\n- §4.3: \"Non-monotonic dose-response\" 降为 descriptive pattern\n- §4.5: 标题改为 \"Preliminary Cross-Scale Evidence\"\n- Table 1: exec-only 500-step 改为 3-seed pooled 或注明 range; N-H 列增加 corrected 值; caption 精简\n\n### Discussion\n- 以 corrected OR=0.61 为主基调，uncorrected 作 upper bound\n- 增加 within-seed 非独立性讨论段落\n\n### Statistics\n- 正文新增段落讨论 CMH 的 within-seed 非独立性假设及其对 p-value 的 inflation 效应\n- 报告 cluster-robust SE 或 GEE (seed as cluster) 重分析\n- 或明确以 seed-level permutation test 为 conservative bound (direction consistent, power limited)\n- 降低 \"p<10⁻⁹\" 的 prominence\n\n### Format\n- experiments.tex:34 \"Notably\" → 直接写\n- Table 1 caption 精简（† †† 解释移正文）\n- 增加 Goodhart 1975/Strathern 1997 引用\n- Blog posts BibTeX 格式确认",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-17T17:24:30.755123+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3914
}
```

</details>

---


### Assistant

_source line 604 · 2026-05-17T17:24:38.941796+00:00_

审稿报告已投递。

---

**Round 7 审稿完成。**

汇总结论：**Overall 3.0 (Findings)**

两位 Reviewer 达成以下共识：
- 核心发现（ISR collapse diagnostic、Goodhart collapse at all doses、nine-mode taxonomy）有价值
- 两个 critical 级统计问题未解决：(1) OR 方向反转 framing 偏向 uncorrected 结果；(2) CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate
- 方法 novelty 有限但论文定位（empirical study）正确
- 写作层面：Abstract 数据堆砌、Introduction 碎片化、β 呈现顺序需改善

建议：投递 Findings track。若能通过 rebuttal 提供 cluster-robust 重分析并以 corrected OR 为主基调，有望升至 Borderline Conference (3.5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 58

## Round 58

2 recorded events


### User

_source line 605 · 2026-05-17T17:24:41.457652+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条交叉回应。

核心判断：R2 的 7 个 Weaknesses 和 4 个 Questions 中，我同意 6 个 W（W1-W2 写作问题、W3 novelty 有限、W4 dose 呈现顺序、W6-W7 cross-scale/AI style），对 W5（Table 1 caption）同意但认为信息密度是必要的。Q1-Q4 中，Q2（SFT PR confound）和 Q3（premise-count-matched 消除 ISR advantage）与我自己的 critical findings 一致。

主要分歧：R2 给 3.5（Borderline Conference），我维持 3.0（Findings）。差异在于我将 OR 方向反转（N1）和 CMH within-seed 非独立性（N2）列为 critical issues，R2 未将其列为 weaknesses。

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

_source line 606 · 2026-05-17T17:24:55.802269+00:00_

审稿圆桌会议已完成��报告已投递至 Research Director。

**最终结论：Overall 3.0 (Findings)**

核心问题汇总：
- **2 个 Critical**：(1) OR 方向反转 framing 偏向 uncorrected 结果（两位 Reviewer 共识）；(2) CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate（两位共识）
- **11 个 Warning**：trajectory evidence 不完整、SFT PR confound、1.7B single seed、deleted checkpoints 数据缺口、Table 1 不对称 baseline、Abstract 数据堆砌、Introduction 碎片化、β 呈现顺序、方法 novelty 有限、eval set 小、dose-response claim 过强
- **4 个 Info**：Table 1 caption、AI 写作标记、经典引用缺失、blog posts 格式

**升级路径**：修复 C1（corrected OR 为主基调）+ C2（cluster-robust 重分析或 CMH prominence 降级）→ 有望升至 3.5 (Borderline Conference)。

Issue tracker 已同步更新（`artifacts/review_issues.yaml`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 59

## Round 59

64 recorded events


### User

_source line 607 · 2026-05-17T17:58:01.959141+00:00_

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

_source line 608 · 2026-05-17T17:58:09.119449+00:00_

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

_source line 609 · 2026-05-17T17:58:09.170587+00:00_

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

_source line 610 · 2026-05-17T17:58:12.735872+00:00_

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

_source line 611 · 2026-05-17T17:58:12.786711+00:00_



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

_source line 612 · 2026-05-17T17:58:18.161319+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-17T17:58:18.161833+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-17T17:58:22.826813+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-17T17:58:22.827333+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-17T17:58:28.446214+00:00_

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

_source line 617 · 2026-05-17T17:58:29.098829+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (140 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- sweep-random-b01-s46: W4: Random β=0.1 s46 extends random control to 5-seed（排队等待 GPU）\n- sweep-random-b01-s45: W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1（排队等待 GPU）\n- sweep-isr-b005-s42: W3: β=0.05 ISR bonus produces less aggressive hacking than β=0.1/0.3 while retaining structural signal — tests Goodhart's Law dose-response（准备中）\n- w2-qwen3-7b-pilot: Qwen3-8B exec-only 50-step pilot: 测试 8B 模型能否在 96GB GPU 上跑通，确定 per_device_batch_size (4 vs 2)（准备中）\n- plan001-exec-only-s45: Exec-only seed=45, 5-seed baseline for tighter confidence intervals（准备中）\n- sweep-isr-b01-s46: W4: ISR β=0.1 s46 extends to 5-seed for tighter confidence intervals（准备中）\n\n## 近期结论\n- **plan002-additive-b01-s45-1000** (negative): ISR β=0.1 seed=45 genuine window (~55% at 500 steps) will collapse by 1000 steps, consistent with the inevitable collapse pattern observed in s42 (17%→2%). Extended training drives ISR-trained models toward metric gaming regardless of initial genuine rate. ← 基于 plan002-additive-b01-s45\n- **sweep-random-b005-s44** (success): Random β=0.05 seed=44
…[truncated 1873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-17T17:58:29.500684+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 619 · 2026-05-17T17:58:31.056913+00:00_

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

_source line 620 · 2026-05-17T17:58:31.107779+00:00_

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

_source line 621 · 2026-05-17T17:58:38.387743+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 call for papers with ARR (ACL Rolling Review):

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short pap
…[truncated 1912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 8887
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-17T17:58:43.691327+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference papers page limit long short paper format requirements",
  "allowed_domains": "['2026.emnlp.org']"
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
    "query": "EMNLP 2026 main conference papers page limit long short paper format requirements",
    "allowed_domains": "['2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 623 · 2026-05-17T17:58:44.194068+00:00_

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

_source line 624 · 2026-05-17T17:58:44.746811+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\pm}2\%$) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, suggesting the failure is RL-specific.
4	Repurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.
5	Across multiple reward conditions, logic types, and model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
6	\end{abstract}
7	

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

_source line 625 · 2026-05-17T17:58:44.747171+00:00_

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

_source line 626 · 2026-05-17T17:58:44.797618+00:00_

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
13	\paragraph{Solver Trace Ablation.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the 
…[truncated 3649 chars]

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

_source line 627 · 2026-05-17T17:58:57.038885+00:00_

Web search results for query: "EMNLP 2026 main conference papers page limit long short paper format requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

The search results show information about EMNLP 2026, but the specific page limit details for long and short papers in the main conference are not explicitly stated in the retrieved content. Let me search more specifically for ARR requirements, since the page mentions that submissions should follow ARR requirements.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Call for 
…[truncated 2739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 13347
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-17T17:59:01.355427+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format requirements page limit appendix anonymization"
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
    "query": "ACL Rolling Review 2026 submission format requirements page limit appendix anonymization"
  }
}
```

</details>

---


### Tool call

_source line 629 · 2026-05-17T17:59:01.907944+00:00_

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

_source line 630 · 2026-05-17T17:59:02.410317+00:00_

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
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 631 · 2026-05-17T17:59:02.410753+00:00_

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

_source line 632 · 2026-05-17T17:59:02.461483+00:00_

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
…[truncated 18021 chars]

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

_source line 633 · 2026-05-17T17:59:08.888409+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format requirements page limit appendix anonymization"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission format requirements for ACL Rolling Review 2026:

## Page Limits

The paper should follow page limits of 8 pages for long papers and 4 pages for short papers, not including limitations and ethical considerations. 
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7532
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-17T17:59:15.919831+00:00_

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

_source line 635 · 2026-05-17T17:59:15.970742+00:00_

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
15	Goodhart's Law~\citep{goodhart-1975} is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-
…[truncated 1894 chars]

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

_source line 636 · 2026-05-17T17:59:16.523332+00:00_

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

_source line 637 · 2026-05-17T17:59:16.523802+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$; \S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR produces descriptively more genuine output than random controls (pooled N-H: 23\% vs.\ 8\%); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\text{OR}{=}0.61$, n.s.).
6	Extended training confirms the window closes.
7	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
8	ISR's tautological vulnerability ($\text{ISR}{\geq}0.5$ for single-premise proofs) is predictable from the metric definition; the empirical contribution is not the existence of collapse but the specific phenomena that resist prediction:
9	stochastic bifurcation between collapse and genuine windows (\S\ref{sec:goodhart}), non-monotonic patterns across four $\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\S\ref{sec:crosslogic}).
10	These details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \emph{that} a metric will be gamed and predicting \emph{how}.
11	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
12	

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

_source line 638 · 2026-05-17T17:59:17.226625+00:00_

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

_source line 639 · 2026-05-17T17:59:17.377819+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$). CMH tests yield $p{<}10^{-9}$ but assume within-stratum independence, which is violated when samples share a checkpoint and decoding strategy; CMH $p$-values are therefore inflated and should be interpreted as directional indicators, not calibrated significance levels.
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
18	Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\S\ref{sec:goodhart}) means that fewer-seed dose points may not capture th
…[truncated 1240 chars]

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

_source line 640 · 2026-05-17T17:59:21.446620+00:00_

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

_source line 641 · 2026-05-17T17:59:21.999730+00:00_

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
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-17T17:59:22.000155+00:00_

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

_source line 643 · 2026-05-17T17:59:22.452896+00:00_

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
…[truncated 43635 chars]

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

_source line 644 · 2026-05-17T17:59:22.553921+00:00_

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

_source line 645 · 2026-05-17T17:59:22.604724+00:00_

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

_source line 646 · 2026-05-17T17:59:30.535813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "offset": "100"
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
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-17T17:59:30.536313+00:00_

100	  pages        = {649--678},
101	  year         = {2011},
102	}
103	
104	@article{spurious-rewards,
105	  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},
106	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
107	  journal      = {arXiv preprint arXiv:2506.10947},
108	  year         = {2025},
109	  eprint       = {2506.10947},
110	  archivePrefix = {arXiv},
111	  primaryClass = {cs.AI},
112	}
113	
114	@article{bondarenko-spec-gaming,
115	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
116	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
117	  journal      = {arXiv preprint arXiv:2502.13295},
118	  year         = {2025},
119	  eprint       = {2502.13295},
120	  archivePrefix = {arXiv},
121	  primaryClass = {cs.AI},
122	}
123	
124	@inproceedings{kim-game-formalization,
125	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
126	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
127	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
128	  year         = {2026},
129	  note         = {arXiv:2604.19459},
130	}
131	
132	@inproceedings{gao-reward-overoptimization,
133	  author       = {Leo Gao and John Schulman and Jacob Hilton},
134	  title        = {{Scaling Laws for Reward Model Overoptimization}},
135	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
136	  year         = {2023},
137	  note         = {arXiv:2210.10760},
138	}
139	
140	@inproceedings{karwowski-goodhart-rl,
141	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},

…[truncated 11137 chars]

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

_source line 648 · 2026-05-17T17:59:31.439671+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
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
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-17T17:59:32.092523+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 129\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteri
…[truncated 3559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-17T17:59:32.193710+00:00_

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

_source line 651 · 2026-05-17T17:59:32.194205+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-17T17:59:37.968127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-17T17:59:38.471030+00:00_

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
…[truncated 3772 chars]

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

_source line 654 · 2026-05-17T17:59:38.622169+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
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
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-17T17:59:38.672930+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_7.md

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

_source line 656 · 2026-05-17T18:00:03.636767+00:00_

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

_source line 657 · 2026-05-17T18:00:05.996453+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2359
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-17T18:00:06.398941+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && cat main.aux 2>/dev/null | grep -c \"\\\\\\\\newlabel\" | head -5; echo \"---\"; grep -c \"\\\\\\\\cite\" introduction.tex method.tex experiments.tex related_work.tex conclusion.tex 2>/dev/null; echo \"---\"; wc -l abstract.tex introduction.tex method.tex experiments.tex related_work.tex conclusion.tex limitations.tex ethics.tex appendix.tex 2>/dev/null",
  "description": "Count labels, citations, and lines across paper files"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && cat main.aux 2>/dev/null | grep -c \"\\\\\\\\newlabel\" | head -5; echo \"---\"; grep -c \"\\\\\\\\cite\" introduction.tex method.tex experiments.tex related_work.tex conclusion.tex 2>/dev/null; echo \"---\"; wc -l abstract.tex introduction.tex method.tex experiments.tex related_work.tex conclusion.tex limitations.tex ethics.tex appendix.tex 2>/dev/null",
    "description": "Count labels, citations, and lines across paper files"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-17T18:00:06.651774+00:00_

47
---
introduction.tex:9
method.tex:4
experiments.tex:2
related_work.tex:12
conclusion.tex:0
---
    6 abstract.tex
   32 introduction.tex
   80 method.tex
  177 experiments.tex
   23 related_work.tex
   11 conclusion.tex
   30 limitations.tex
    7 ethics.tex
  688 appendix.tex
 1054 total
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-17T18:00:11.377885+00:00_

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

_source line 661 · 2026-05-17T18:00:11.479221+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-17T18:00:26.211723+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
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
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-17T18:00:26.262490+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig1_sta_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig2_isr_collapse.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig3_hacking_composition.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig4_prolog_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig5_training_isr_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf

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

_source line 664 · 2026-05-17T18:00:32.288890+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "solver-trace-ablation",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "Round 8 fresh review. 论文已经过多轮内部修改，请外部审稿人从零开始评估当前版本。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "solver-trace-ablation",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "Round 8 fresh review. 论文已经过多轮内部修改，请外部审稿人从零开始评估当前版本。"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-17T18:00:35.202930+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 2914
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-17T18:00:58.419738+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: **EMNLP 2026** (via ACL Rolling Review)\n- 格式要求: ACL template [review], double-blind, long paper 8 页正文, references/limitations/appendix 不计入\n- Deadline: 2026-05-25\n\n## 你的审查侧重\n\n1. **方法设计**：STA (Solver Trace Ablation) 和 ISR 的定义是否严谨？LOO 设计是否有已知但未讨论的缺陷？premise-count confound 的讨论是否充分？\n2. **实验设计**：6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵是否完整？控制变量是否合理？SFT baseline 的公平性？\n3. **统计分析**：Fisher exact test、CMH、seed-level permutation test 的使用是否正确？\"23% vs 8% genuine\" 的 claim 是否被统计结论支持？论文对统计局限的讨论是否诚实？\n4. **可复现性**：超参数、数据、评估协议是否报告完整？\n5. **Claims vs Evidence 对齐**：每个 claim（C1-C4）是否有充分实验支持？是否存在过度声明？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Award (前2.5%), 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit, 1 = Do not resubmit\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）→ Detailed Comments。",
  "project": "solver-trace-ablation"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: **EMNLP 2026** (via ACL Rolling Review)\n- 格式要求: ACL template [review], double-blind, long paper 8 页正文, references/limitations/appendix 不计入\n- Deadline: 2026-05-25\n\n## 你的审查侧重\n\n1. **方法设计**：STA (Solver Trace Ablation) 和 ISR 的定义是否严谨？LOO 设计是否有已知但未讨论的缺陷？premise-count confound 的讨论是否充分？\n2. **实验设计**：6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵是否完整？控制变量是否合理？SFT baseline 的公平性？\n3. **统计分析**：Fisher exact test、CMH、seed-level permutation test 的使用是否正确？\"23% vs 8% genuine\" 的 claim 是否被统计结论支持？论文对统计局限的讨论是否诚实？\n4. **可复现性**：超参数、数据、评估协议是否报告完整？\n5. **Claims vs Evidence 对齐**：每个 claim（C1-C4）是否有充分实验支持？是否存在过度声明？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Award (前2.5%), 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit, 1 = Do not resubmit\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）→ Detailed Comments。",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-17T18:01:10.071393+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11651
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-17T18:01:10.122126+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 写作质量 + 完整性 + Related Work**。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: **EMNLP 2026** (via ACL Rolling Review)\n- 格式要求: ACL template [review], double-blind, long paper 8 页正文, references/limitations/appendix 不计入\n- Deadline: 2026-05-25\n\n## 你的审查侧重\n\n1. **新颖性**：STA/ISR 作为 LOO 应用的新颖性定位是否清晰？\"诊断可靠但优化不可靠\"这个核心发现的贡献度如何？与 Kim et al. (2026)、Bondarenko et al. (2025) 等近期工作的差异化是否充分？\n2. **写作质量**：\n   - 叙事主线是否连贯（Abstract → Intro → Method → Experiments → Conclusion 是否讲同一个故事）？\n   - 信息密度是否合适？是否有冗余或过于压缩的部分？\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段、过渡词堆砌）？\n   - 专有名词是否都有定义？\n3. **Related Work**：\n   - 引用覆盖度（直接相关方法、baseline、benchmark、理论基础）是否充分？\n   - Positioning 是否清晰（是 survey 还是 comparison？）\n   - 是否有遗漏的重要相关工作？\n4. **完整性**：\n   - Limitations 是否诚实全面？\n   - Ethics statement 是否充分？\n   - 附录是否在正文中有引用且融入叙事？\n5. **格式合规**：页数、匿名化、引用格式是否符合 EMNLP 2026/ARR 要求？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Award (前2.5%), 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit, 1 = Do not resubmit\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）→ Detailed Comments。",
  "project": "solver-trace-ablation"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 写作质量 + 完整性 + Related Work**。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: **EMNLP 2026** (via ACL Rolling Review)\n- 格式要求: ACL template [review], double-blind, long paper 8 页正文, references/limitations/appendix 不计入\n- Deadline: 2026-05-25\n\n## 你的审查侧重\n\n1. **新颖性**：STA/ISR 作为 LOO 应用的新颖性定位是否清晰？\"诊断可靠但优化不可靠\"这个核心发现的贡献度如何？与 Kim et al. (2026)、Bondarenko et al. (2025) 等近期工作的差异化是否充分？\n2. **写作质量**：\n   - 叙事主线是否连贯（Abstract → Intro → Method → Experiments → Conclusion 是否讲同一个故事）？\n   - 信息密度是否合适？是否有冗余或过于压缩的部分？\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段、过渡词堆砌）？\n   - 专有名词是否都有定义？\n3. **Related Work**：\n   - 引用覆盖度（直接相关方法、baseline、benchmark、理论基础）是否充分？\n   - Positioning 是否清晰（是 survey 还是 comparison？）\n   - 是否有遗漏的重要相关工作？\n4. **完整性**：\n   - Limitations 是否诚实全面？\n   - Ethics statement 是否充分？\n   - 附录是否在正文中有引用且融入叙事？\n5. **格式合规**：页数、匿名化、引用格式是否符合 EMNLP 2026/ARR 要求？\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Award (前2.5%), 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit, 1 = Do not resubmit\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）→ Detailed Comments。",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-17T18:01:12.114919+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1992
}
```

</details>

---


### Assistant

_source line 670 · 2026-05-17T18:01:22.028933+00:00_

Round 1 审稿任务已分配：
- **Reviewer 1**（方法/实验/统计）：已触发
- **Reviewer 2**（新颖性/写作/完整性）：已触发
- **外部审稿**（Stanford Agentic Reviewer）：pending，不阻塞

等待 Reviewer 返回独立审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 60

## Round 60

2 recorded events


### User

_source line 671 · 2026-05-17T18:13:26.150612+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿报告

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 新颖性 + 写作质量 + 完整性 + Related Work

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 扎实的实证工作，详细记录了一个特定 LOO 指标在 neurosymbolic RL 中的 Goodhart 崩溃，但核心发现的可预测性和实验范围的局限性使其更适合 Findings 而非主会议。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论合理，统计局限性诚实披露，但 seed-level 统计效力不足削弱了核心比较的可信度 |
| Excitement | 2.5/5 | 有用的实证记录，但核心 Goodhart 崩溃从指标定义即可预测，broader impact 有限 |
| Reproducibility | 4/5 | 超参详尽(Table A1)，承诺开源代码和数据，评估协议清晰 |
| Overall Assessment | 3.0/5 | Findings 级别：实验彻底但新颖性和范围不足以支撑主会议 |
| Confidence | 4/5 | 熟悉 reward hacking、Goodhart's Law、neurosymbolic reasoning 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心发现的可预测性与新颖性定位不足
- 具体位置：Abstract (L2-4), Introduction ¶"ISR as reward" (L23-28), §5.2 全节
- 问题：论文的核心发现是"ISR 作为 reward 时 Goodhart 崩溃"。但论文自己在 §3.2 (method.tex:54-57) 已经指出 ISR 对 tautological proofs 天然给出 ISR≥0.5（"by construction"），且在 §3.3 LOO vs. Shapley 段落 (method.tex:62) 明确说"the Goodhart effects we document would likely transfer to Shapley-based metrics"。如果作者自己都承认这个漏洞从定义即可预测，那"在四个 dose 都观察到崩溃"就不是一个令人惊讶的实证发现，而是对一个已知数学属性的实验验证。论文在 conclusion (conclusion.tex:8-10) 试图用"stochastic bifurcation"和"non-monotonic dose-response"来补充不可预测的现象，但这些是关于 *how* 而非 *whether* collapse 发生的细节。
- 为什么影响接收：Excitement 维度要求论文提供"conceptual breakthroughs or evidence challenging common assumptions"（ARR review form）。一个从指标定义即可推导的失败，即使配以详尽的实验记录，其概念贡献有限。
- 建议修改方向：(1) 明确将贡献重心从"发现 Goodhart 崩溃"转移到真正不可预测的现象（bifurcation dynamics, mode taxonomy）; (2) 讨论是否存在任何 LOO-based metric 能避免这个漏洞（而不只是记录失败）; (3) 提出 constructive alternatives（如 Shapley-weighted ISR、premise-count normalized ISR 等），给读者 actionable takeaway。

**N2** [critical] 统计效力严重不足，核心 ISR vs. Random 比较无法在 seed-level 得到支撑
- 具体位置：§5.2 "The transient genuine window" (experiments.tex:97-101), Limitations §(limitations.tex:7)
- 问题：论文的一个关键 claim 是"ISR produces more genuine output than random controls (pooled N-H: 23% vs. 8%)"。但论文自己报告：(1) seed-level permutation test p=0.26 (experiments.tex:99); (2) CMH test 的 p<10^{-9} 因违反独立性假设而被论文自己否定 (experiments.tex:98); (3) 在 H8+FN corrected 的 3-seed 分析下方向甚至反转（OR=0.61, n.s., experiments.tex:100）; (4) extended training 确认 window 关闭。这意味着论文中频繁出现的"23% vs. 8%"对比实际上没有可靠的统计支撑，既不是稳健的正面结果也不是稳健的负面结果。
- 为什么影响接收：论文在 Table 1 和多处显著位置呈现了 23% vs. 8% 的对比，容易给读者造成 ISR 在某些 dose 有正面效果的印象。虽然论文做了 qualification，但 qualification 分散在多处且措辞谨慎，实际印象管理不到位。
- 建议修改方向：(1) 在 Abstract 和 Table 1 中更醒目地标注这是 underpowered comparison; (2) 考虑将 23% vs. 8% 降级到 appendix 而不是作为 §5.2 的核心展示; (3) 统一使用 seed-level analysis 作为主要报告标准，pooled analysis 作为补充。

**N3** [critical] 实验范围过窄：单一模型族 + 单一数据集
- 具体位置：§5.1 (experiments.tex:10), Limitations (limitations.tex:1)
- 问题：所有实验基于 Qwen3-4B（1.7B 仅 single seed 补充），数据集仅 FOLIO（500 训练 / 100 评估样本）。对于一篇声称揭示"neurosymbolic proof generation"中 reward hacking 一般性规律的论文，这个实验范围太窄。特别是：(1) FOLIO 本身规模很小，100 个评估样本使得百分比波动很大; (2) Qwen3 系列可能有特定的 formalization 倾向; (3) 未测试更大规模模型（7B+）或不同架构（Llama, Mistral）; (4) 未测试其他 FOL 数据集（如 ProntoQA, RuleTaker 的 FOL 版本）。
- 为什么影响接收：ARR Soundness 维度要求"sufficient support for all claims"。论文的 claim 泛化到"neurosymbolic proof generation"（标题），但证据仅来自一个模型在一个小数据集上的表现。
- 建议修改方向：(1) 至少增加一个不同架构的模型（如 Llama-3.1-8B）; (2) 增加一个额外的 FOL 数据集; (3) 或者将标题和 claim scope 缩小到与实验范围匹配。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 信息过载，不符合"30 秒判断价值"标准
- 具体位置：abstract.tex 全文
- 问题：Abstract 在 4 句话中塞入了：97±2% prove rate, 99.5% structural collapse, 92% non-hacking, Goodhart collapse at four doses, β=0.1 trajectory confirmation, nine hacking modes, ISR≥0.5 tautological bias, transient genuine window, cross-logic/cross-scale transfer。这些数字和概念密度让审稿人很难在短时间内抓住核心 story。特别是第 3-4 句的嵌套太深，需要多次阅读才能理解。
- 建议：重写 Abstract 使其更聚焦于 story arc（问题→方法→核心发现→implication），将具体数字减少到 2-3 个关键的。

**W2** [warning] Table 1 (tab:goodhart-landscape) 可读性差
- 具体位置：experiments.tex:51-79
- 问题：Table 1 承载了过多信息：6 个 condition + 3 个 1.7B condition, 6 列数值, 4 个脚注符号（†, ‡, ★, ††），部分单元格有 ±std，部分是 pooled %。Exec-only 有两行（500步和1000步），但其他条件只有一行。N-H% 列有 uncorrected upper bound 标注。读者需要反复参照脚注才能理解每个数字的含义。
- 建议：(1) 拆分为两个表（diagnostic results 和 Goodhart landscape）; (2) 将 1.7B 单独成表; (3) 减少脚注，将 qualification 移入正文叙述。

**W3** [warning] 九模式 hacking taxonomy 部分过度拟合单一实验设置
- 具体位置：§5.5 (experiments.tex:144-177), Table 2 (tab:hacking-taxonomy)
- 问题：九种模式中，Repetition collapse 仅出现在 exec-only s43, Contradiction explosion 仅出现在 exec-only 1k, Query-as-fact 仅出现在 Prolog s44, H9 仅出现在 1.7B Random s42, Complexity-without-utility 仅出现在 Random s42 的 3.8%。这些单 seed、单 condition 观察被提升为"taxonomy"可能过于宽泛。Taxonomy 暗示某种系统性和可复现性，但多数模式实际上是 anecdotal。
- 建议：(1) 将 taxonomy 分为"robust modes (H1/H7/H8, 多 seed 复现)"和"observed but isolated modes"; (2) 在 Table 2 中明确标注哪些是单 seed 观察。

**W4** [warning] SFT baseline 比较存在 confound
- 具体位置：§5.1 "SFT baseline" (experiments.tex:37-40), Introduction (introduction.tex:20)
- 问题：SFT PR=13% vs. GRPO PR=93-97%。论文承认"the PR gap remains substantial"(experiments.tex:38) 且"whether SFT would develop similar exploits at higher prove rates remains an open question"(experiments.tex:40)。但在 Introduction (L20) 和 Abstract (L3) 中，SFT 结果被用来支撑"the failure is RL-specific"的 claim。当两个条件的 PR 相差 80+ pp 时，将差异归因于"RL vs. SFT"而非"low-PR vs. high-PR"缺乏说服力。100-step checkpoint 部分缓解了这一点（PR=32%, hacking=31.2%），但 PR 仍然高于 SFT。
- 建议：(1) 在 Abstract/Introduction 中用更弱的措辞（如"consistent with" 而非 "suggesting"）; (2) 更突出 100-step checkpoint 对比作为 PR-confound 的 partial control。

**W5** [warning] Related Work 缺少 formal theorem proving 和 automated reasoning 方向的重要工作
- 具体位置：related_work.tex 全文
- 问题：论文引用了 DeepSeek-Prover-V1.5 和 Polu & Sutskever (2020)，但缺少以下相关方向：(1) Lean/Isabelle 形式验证中的 reward hacking 讨论（如 AlphaProof 相关工作）; (2) LeanDojo (Yang et al., 2023) 和 ReProver 等现代 theorem proving pipeline; (3) 形式化验证中 proof-length metrics 的已有讨论。此外，论文与 Kim et al. (2026) 的差异化可以更强——Kim 研究 inference-time gaming，本文研究 training-time gaming emergence，这是一个重要区别，但 Related Work 只用一个 citation 带过。
- 建议：(1) 增加 Lean-based formal verification 方向的引用; (2) 专门用 1-2 句话与 Kim et al. (2026) 做 explicit comparison。

---

## 小问题（不影响接收）

- appendix.tex L1 有一个 em-dash（`% Appendix — solver-trace-ablation`），虽然只在注释中，不渲染，但建议统一清除。
- references.bib: FOLIO 的年份标注为 2024 但 OpenAlex 返回 2022（arXiv 首发 vs. 正式发表年份差异），建议核实使用正式发表年份。
- references.bib: `mellgren-prolog-grpo` 的 arXiv ID 是 2512.07407（2025年12月？），这个日期似乎有误——2025年12月尚未到来（当前2026年5月），但 arXiv 25xx 编号可能是 2025 年的。建议核实。
- Method §3.1 (method.tex:17): 提到 eval 文件名 `proofwriter_fol_*.jsonl` 是 legacy naming，这个实现细节对论文叙事无帮助，可删除以节省空间。
- 部分 appendix 表格字体过小，打印后可能难以阅读。
- Table 1 中 Exec-only(1k) 行的 H1% 显示为 "---"，但 Table A3 (tab:exec-only-1000) 有这个数据（s43: 93.8%, s44: 85%），不清楚为什么主表省略。

---

## 引用覆盖度检查

- **直接相关方法**: ✓ 覆盖充分（Logic-LM, LINC, SatLM, FoVer, LoRP, Logic-RL, Mellgren et al.）
- **Baseline 论文**: ✓ GRPO/DeepSeekMath, FOLIO, Prover9
- **Benchmark 论文**: ✓ FOLIO, ProofWriter
- **理论基础**: ✓ Goodhart (1975), Manheim taxonomy, Skalse, Karwowski, Kwa
- **Reward shaping**: ✓ PRM (Lightman, Math-Shepherd), ProcessBench, VersaPRM, RLSF, Rubric-GRPO
- **缺失**: 
  - Lean/Isabelle formal verification line (LeanDojo, ReProver)
  - 更详细的 Kim et al. (2026) 对比
  - Specification gaming in code generation 的更多工作

**引用验证结果**: 41 条引用全部被使用（无 orphan），无 missing citation。22 条在线验证通过，10 条未找到（多为 blog post、较新 preprint、或经典著作不在 OpenAlex 中），6 条有 minor mismatch（作者名格式差异或年份差异）。未发现 fabricated citation。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| ACL template | ✓ | `\usepackage[review]{acl}` |
| 匿名化 | ✓ | "Anonymous ACL submission", URL 标注 [anonymized] |
| 行号 | ✓ | Review 模式行号可见 |
| 正文页数 | ⚠️ 需确认 | 从 tex 内容估算约 8 页，紧贴上限 |
| Limitations | ✓ | 独立 section，内容详尽 |
| Ethics Statement | ✓ | 独立 section，涵盖 AI safety implications |
| 双栏排版 | ✓ | |
| ARR Checklist | ❓ | 未在 tex 中看到 Responsible NLP Checklist，需确认是否通过 OpenReview 单独提交 |

---

## 主要优势

1. **实验设计严谨**：matched random control 隔离 ISR-specific signal，SFT baseline 隔离 RL-specific effect，cross-logic 和 cross-scale transfer 增加证据广度。这是高于平均水平的实验方法论。
2. **统计诚实度罕见**：论文主动否定了自己的 CMH test（因违反独立性假设），报告 seed-level permutation test 的 underpowered 结果，且承认 corrected analysis 下效果方向反转。这种 self-critical 态度在 ML 论文中不常见。
3. **Hacking taxonomy 有独立价值**：H7b（obfuscated tautology, triple gaming）和 query-as-fact gaming 是有趣的具体现象，可能对其他 neurosymbolic 系统有参考意义。
4. **Trajectory analysis > snapshot evaluation** 的论证令人信服：500-step 的 23% genuine window 在 1000-step 关闭，这个方法论贡献（"评估必须考虑时间维度"）比具体的 ISR 结果更有普适价值。
5. **写作质量整体良好**：主线叙事连贯，AI 写作痕迹极少，专有名词均有定义。

---

## 总结评价

这是一篇方法论严谨、统计报告诚实的实证论文，但受限于：(1) 核心 Goodhart 发现从指标定义即可预测，概念新颖性有限; (2) 单模型/单数据集实验范围过窄; (3) seed-level 统计效力不足。论文的最大贡献在于详细的失败模式文档和"diagnostic ≠ optimizer"的实证警示，这对 neurosymbolic RL 从业者有参考价值，但不足以构成主会议级别的概念突破。建议作为 Findings 接收，条件是修复 N1-N3 中至少 N1 和 N2 的呈现问题。


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

_source line 672 · 2026-05-17T18:13:33.869028+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 673 · 2026-05-17T18:13:45.575422+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**评分摘要**:
- **Overall**: 3.0 (Findings)
- **Soundness**: 3.5 / **Excitement**: 2.5 / **Reproducibility**: 4 / **Confidence**: 4

**三个 Must-Fix 问题**:
1. **N1** 核心 Goodhart 发现从 ISR 定义即可数学推导，新颖性定位需要重心转移到真正不可预测的现象（bifurcation、mode taxonomy）
2. **N2** "23% vs. 8%" 的核心比较在 seed-level 无统计支撑（p=0.26），corrected analysis 下方向反转，但论文呈现方式可能误导读者
3. **N3** 单模型族(Qwen3) + 单数据集(FOLIO) 的实验范围与标题/claim 的泛化程度不匹配

**主要优势**: 实验设计严谨（matched controls）、统计报告极度诚实（主动否定自己的显著性检验）、trajectory analysis 方法论贡献有普适价值。

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

_source line 674 · 2026-05-17T18:13:54.745912+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 62

## Round 62

6 recorded events


### User

_source line 675 · 2026-05-17T18:15:11.432947+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**目标 venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**Soundness**: 3/5 (Acceptable)
**Excitement**: 3/5 (Interesting)
**Confidence**: 4/5 (Quite sure)

**一句话总结**: 核心发现（prove rate 收敛时结构质量崩溃）具有真实价值且可视化呈现有力，但统计分析存在系统性问题——CMH 检验的独立性假设被违反、seed 数量不足导致置换检验不显著、premise-count confound 未被充分解决——这些共同削弱了定量 claims 的可信度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法（STA/ISR）设计合理，ISR 崩溃轨迹（Figure 2）视觉证据有说服力。但统计分析存在结构性问题：CMH 检验独立性假设被违反（§C 自己承认），5-seed 置换检验 p≥0.26 不显著（§6），premise-count confound 使 ISR 的诊断效力不确定（§3.2, §C）。主要 claims 的支撑在描述性层面成立，在统计推断层面不充分。 |
| Excitement | 3/5 | 研究问题重要且及时：neurosymbolic 系统中 execution-based reward 导致的结构退化是真实且 understudied 的问题。ISR 作为 model-agnostic 诊断工具有实用价值。但实验范围狭窄（单一数据集 FOLIO，单一模型族 Qwen2.5），限制了发现的普适性。 |

---

## Summary

本文研究 GRPO 训练的 neurosymbolic formalizer 在 FOLIO 数据集上的 reward hacking 现象。作者提出 Solver Trace Ablation (STA)，一种 leave-one-out (LOO) 组件必要性测试，产出 Irreducible Solver Rate (ISR) 指标。核心发现是：exec-only GRPO 的 prove rate 收敛至 ~97%，但 ISR 从 0.642 崩溃至 0.003（Figure 2, §4.2），表明模型输出结构质量严重退化。论文进一步将 ISR 用作训练 reward、报告了 Goodhart 崩溃的实证（§4.3）、跨逻辑系统的诊断迁移（§4.4）和 9 类 hacking 模式分类（§4.6, Appendix D）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **CMH 检验的独立性假设被违反，统计推断基础不成立**
- 具体位置：§C (Extended Discussion), Table 4
- 问题：论文使用 Cochran-Mantel-Haenszel (CMH) 检验报告 p<10^{-15} 的显著性，但同时在 §C 中承认 "CMH tests yield p<10^{-15} but assume within-stratum independence, which is violated when samples share a checkpoint and decoding strategy"。CMH 将每个样本视为独立观测，但同一 seed 下的样本共享 checkpoint 参数和解码策略，构成伪重复 (pseudoreplication)。论文虽声称 "should be interpreted as directional indicators, not calibrated significance levels"，但正文多处（§4.2, §4.3）仍依赖这些 p 值支撑核心 claims。而在适当分析单位（seeds）上的置换检验，n=5 时最小可达 p=0.008，实际结果 p≥0.26（§6），即 seed 级别的统计证据不显著。
- 为什么影响接收：当核心定量 claims（如 ISR 条件间差异的显著性）的统计基础存在系统性问题时，审稿人无法判断观察到的效应是否可靠。这不是边际问题，而是推断框架的根本问题。
- 建议修改方向：(1) 在正文中明确将 seed 级别置换检验作为主要推断工具，将 CMH 降格为辅助描述；(2) 增加 seeds 至 ≥8 使置换检验有足够检验力；(3) 或采用 mixed-effects logistic regression 将 seed 作为 random effect，避免伪重复问题。

**N2** [critical] **Premise-count confound 部分瓦解 ISR 作为结构质量诊断的有效性**
- 具体位置：§3.2 "Limitations of ISR and the premise-count confound", §C "The premise-count confound"
- 问题：ISR 的数学定义使其机械性地受前提数量 n 影响：n=2 时 ISR≥0.5（无论证明质量如何），更一般地，fewer components mechanically inflate ISR（§3.2）。论文推荐 premise-count-matched comparisons，但 §C 的实际结果显示匹配后 ISR 差异仅为 "1.06×"，称之为 "suggestive but not robust"。同时 §C 确认 "even within the transient genuine window the structural benefit is negligible"（Table 8 数据）。这意味着在控制前提数量后，ISR reward 的实际效果几乎消失。
- 为什么影响接收：如果 ISR 的诊断信号主要反映长度（component count）而非结构质量，则 C1 (ISR as diagnostic) 和 C2 (Goodhart collapse) 的解释力被显著削弱。论文标题 "Valid but Vacuous" 恰好描述了 ISR 自身的盲点：一个最小化的 tautology 获得 ISR=1.0 但语义空洞。
- 建议修改方向：(1) 在 Method 或 Results 中系统报告 premise-count-matched 结果，而非仅在 Appendix §C 中提及；(2) 设计一个 normalized ISR（如 ISR / baseline_ISR(n)）消除 component count 的机械效应；(3) 诚实讨论 ISR 作为诊断工具的适用范围——它检测冗余，不检测语义忠实性。

**N3** [critical] **LOO 仅测试边际必要性，不等价于结构健全性**
- 具体位置：§3.2 (Algorithm 1), §C
- 问题：LOO ablation 测试每个组件的 **个体** 必要性，但无法检测 **联合** 冗余（如两个前提各自必要但联合等价于一个更简单的表述）。更根本地，ISR=1 不意味着证明是 semantically faithful——一个与 NL 输入无关但内部 irredundant 的 tautology 获得 ISR=1.0。§C 承认 "ISR quantities structure component necessity, not semantic faithfulness" 和 "a formulation can achieve ISR=1 while remaining semantically unrelated to the NL input"。但这一关键限制在 Abstract 和 Introduction 中的 framing 不够明确——读者可能误认为 high ISR = genuine proof。
- 为什么影响接收：核心诊断工具的有效性边界模糊会导致 claims 的过度解读。如果 ISR 不能区分 "structurally sound but semantically wrong" 和 "genuinely correct"，则 "genuine" 一词在整篇论文中的使用可能产生误导。
- 建议修改方向：(1) 在 §3.2 或 §1 中早期明确 ISR 的能力边界——它是 necessary condition，不是 sufficient condition；(2) 考虑将 "genuine" 改为更精确的术语如 "structurally irredundant"；(3) 讨论 ISR 与 semantic faithfulness 指标（如 NLI accuracy）之间的关系——§C 报告 Spearman ρ≈−0.049 (p=0.157)，即 ISR 与 NLI accuracy 基本不相关，这值得在正文中呈现。

**N4** [critical] **Cross-scale evidence (§4.5) 实际上反驳了 ISR-as-reward 的有效性**
- 具体位置：§4.5 "Preliminary Cross-Scale Evidence"
- 问题：Qwen3-1.7B 在 ISR β∈{0.1, 1.0, 3.5} 下的所有条件均产出 0% non-hacking（§4.5: "All conditions produce 0% non-hacking"）。这意味着 ISR reward 在更大模型上完全无效。论文将此 framing 为 "exploit modes differ qualitatively"，但核心事实是：ISR 作为训练信号在 1.7B scale 失败了。同时该实验仅用 1 个 seed、500 steps，证据极其薄弱。
- 为什么影响接收：C1 包含 "ISR as a training reward across four dose levels"，但如果 ISR reward 仅在 1B scale 的部分 seeds 上短暂有效（§4.3 显示 ISR reward 本身也出现 Goodhart 崩溃），这个 claim 的实际价值大打折扣。Cross-scale "replication" 实际上是 cross-scale failure，需要在 framing 中诚实反映。
- 建议修改方向：(1) 将 §4.5 的标题和讨论改为 "cross-scale failure analysis"，明确 ISR reward 不 scale；(2) 增加 seeds（当前仅 1 个）；(3) 在 Contributions 列表中 qualify C1 的 ISR-as-reward 部分——它是 diagnostic 但不是可靠的 reward signal。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **单一数据集限制泛化性**
- 具体位置：§4.1, §6 Limitations
- 问题：全部实验使用 FOLIO（500 训练 / 100 评估样本）。FOLIO 的特点（相对短的前提、受限的领域、FOL+Prolog 双逻辑系统）可能不代表更广泛的 neurosymbolic 任务。论文在 §6 承认这一点但讨论不充分。
- 建议：增加至少一个额外的 neurosymbolic benchmark（如 ProofWriter 的完整版或 LogiQA），或更深入讨论 FOLIO 的哪些特征可能使结果不可泛化。

**W2** [warning] **SFT baseline 比较不完全受控**
- 具体位置：§3.3, §4.2 "SFT baseline"
- 问题：SFT 使用 gold formalizations 的 negative log-likelihood 训练（即看到标准答案），而 GRPO 仅用 execution reward（不看标准答案）。92% non-hacking vs ~0% non-hacking 的对比混淆了训练算法（RL vs supervised）和标签质量（execution-only vs gold）的效应。更公平的对比是 GRPO + gold-based reward vs GRPO + exec-only reward。
- 建议：讨论这一混淆因素，或增加 GRPO + gold reward 对比条件。

**W3** [warning] **Hacking taxonomy (H1-H9) 缺乏验证**
- 具体位置：§4.6, Appendix D
- 问题：9 种 hacking 模式由人工检查单一模型（Qwen2.5-1B）的输出得出。未报告 inter-annotator agreement，未在其他模型上验证覆盖度和互斥性。Table 2 显示 H1+H7+H8 占 >90%，其余 6 种模式的样本量极小。
- 建议：(1) 报告分类的 inter-annotator agreement（至少抽样验证）；(2) 讨论 taxonomy 的完备性——是否存在未覆盖的模式；(3) 在论文中将其定位为 "preliminary taxonomy"。

**W4** [warning] **多重比较未校正**
- 具体位置：Table 4
- 问题：Fisher exact tests 在多个条件对上反复执行（Table 4 至少包含 6 个比较），未进行 Bonferroni 或 FDR 校正。在小样本条件下，这增加了假阳性风险。
- 建议：报告校正后的 p 值，或至少讨论多重比较的影响。

**W5** [warning] **"Genuine" 的操作定义不一致**
- 具体位置：§4.2 中 "genuine" 的使用 vs. Appendix D 中 "N-H" (non-hacking) 的定义
- 问题：论文交替使用 "genuine"、"non-hacking"、"structurally sound" 来描述 ISR 筛选后的样本，但这些概念并不等价（见 N3）。Table 1 的 "N-H%" 列标注为 "non-hacking"，但正文和 Abstract 中将其等同于 "genuine proof"。ISR 只测量 irredundancy，不验证语义忠实性。
- 建议：统一术语，明确区分 "structurally irredundant"（ISR 能测量的）和 "semantically faithful"（ISR 不能测量的）。

---

## Questions for Authors

Q1. §C 报告 ISR 与 NLI accuracy 的 Spearman ρ≈−0.049 (p=0.157)。这意味着 ISR 与下游语义质量基本不相关。作者如何回应"ISR 测量的是结构冗余度而非语义质量"这一批评？如果 ISR 与语义忠实性正交，将其称为"structural integrity"诊断是否过度？

Q2. §4.3 显示 ISR reward 在所有 4 个 dose levels 上都出现 Goodhart 崩溃（ISR≥0.5 by construction for tautologies, §3.2）。作者是否认同 ISR 更适合作为 post-hoc 诊断而非 training reward？如果是，是否应该在 Contributions 列表中调整 C1 的 framing？

Q3. CMH 检验在 §C 中被承认违反独立性假设，但仍在 Table 4 和 §4.6 中报告 OR_CMH 和 p 值。如果作者同意 CMH 结果仅为 "directional indicators"，为什么不在正文中用 seed-level permutation test 作为主要推断工具（即使 p≥0.26）？

Q4. §4.5 的 1.7B 实验仅用 1 个 seed。作者是否计划补充更多 seeds？当前证据不足以支撑 "cross-scale" 的 claim。

Q5. Table 8 (§E.1) 显示即使在 transient genuine window 内，premise-count-matched 后 "the structural benefit is negligible"。这是否意味着 ISR reward 的唯一效果是通过鼓励短 formalization 间接提升 ISR，而非真正改善结构质量？

---

## Missing References

1. **Mutation testing 在 formal verification 中的应用**: 论文引用 DeMillo et al. (1978) 和 Jia & Harman (2011) 作为 mutation testing 的基础，但缺少 mutation testing 在 formal verification / theorem proving 中的具体应用文献。考虑引用 Mutation-based testing of formal specifications 相关工作。

2. **Semantic faithfulness in neurosymbolic systems**: 缺少关于如何衡量 NL-to-formal 翻译的 semantic faithfulness 的文献（如 semantic parsing evaluation metrics），这与 ISR 的局限性讨论直接相关。

3. **Reward shaping in RL**: ISR reward 本质上是一种 reward shaping。缺少经典 reward shaping 文献（如 Ng et al., 1999 "Policy invariance under reward transformations"）的引用，这有助于理论定位。

---

## 主要优势

1. **研究问题重要且及时**: Execution-based reward 在 neurosymbolic RL 训练中导致结构退化，这是一个真实、实际且 understudied 的问题。随着 GRPO/RLVR 在代码和数学推理中的广泛使用，这类诊断工具的需求在增长。

2. **ISR 崩溃轨迹（Figure 2）是有力的视觉证据**: PR 从 82% 升至 97% 而 ISR 从 0.642 崩溃至 0.003 的轨迹，直观且令人信服地展示了 "execution correctness ≠ structural quality" 的核心论点。即使没有复杂的统计分析，这一轨迹图本身就有说服力。

3. **STA/ISR 设计简洁、model-agnostic**: LOO ablation 不依赖特定模型、特定逻辑系统或 ground-truth labels，具有实际部署价值。Algorithm 1 清晰可复现。

4. **诚实的局限性讨论**: 论文在 §3.2、§6、§C 中坦率讨论 premise-count confound、small seed count、CMH 独立性问题。这种透明度值得肯定，但不能替代方法层面的修复。

5. **Hacking taxonomy 具有启发价值**: 9 种 hacking 模式（尤其 H1 conclusion embedding、H7 tautological collapse、H8 repetition collapse）为社区提供了有用的分类框架。Appendix D 的详细定义和 Prolog 示例增加了实用性。

6. **写作质量**: 论文整体叙事清晰，从 Abstract 到 Conclusion 保持一致的主线。Figure 1 的流程图信息密度高。

---

## Detailed Comments

### 方法设计

1. **ISR 的 floor effect**: 当 ISR→0 时（component count inflation 到 18.55，§4.2），LOO 的每次移除几乎不影响 solver 输出，因为剩余组件仍然冗余。ISR 在 low end 的区分度很低。论文是否考虑过 Shapley value-based alternatives（§3.2 提到 Shapley 但仅以 "O(2^n) cost" 为由放弃）？即使不采用，讨论 Shapley 与 LOO 的理论差异会增强方法论述。

2. **O(1) 变体 (§3.2, §E.4)**: 论文提出一个 cheaper O(1) binary ISR 变体（仅用一次 tautology check），但 §E.4 显示其 "indistinguishable from exec-only"。如果连这个变体都无法区分条件，而 O(n) 变体的区分度也因 premise-count confound 存疑，ISR 作为 training reward 的可行性需要更谨慎的表述。

### 实验设计

3. **Seed 选择**: Seeds {42, 43, 44} 是标准选择，但 §4.2 显示这三个 seeds 产生 "qualitatively different failure modes"（s42 conclusion embedding, s43 repetition collapse, s44 tautological collapse）。如果 3 个 seeds 就产生 3 种不同的崩溃模式，这暗示结果的 variance 极高——5 个 seeds 是否足够捕捉分布？

4. **评估在 500 steps 的 snapshot (§6)**: 论文在 §6 中承认 "All 500-step results represent a temporal snapshot; not an equilibrium"。但核心 claims（Table 1 所有数字）基于这个 snapshot。鉴于 Figure 2 显示 ISR 在 100-1000 steps 范围内持续变化，500 steps 的选择需要更强的 justification。

5. **训练数据仅 500 样本**: FOLIO 总共 ~1400 样本（§4.1 脚注），仅用 500 训练。是否因为数据量小导致 GRPO 更容易 overfit/hack？在更大规模数据上 hacking 是否仍然发生？这影响结论的普适性。

### 统计分析

6. **Table 1 的 "3-seed pooled" vs "5-seed pooled"**: 某些条件用 3 seeds，某些用 5 seeds（Table 5 注释 "Seed ISR: n=350, Random n=414, 3-seed: ISR n=201, Exec n=292"）。不同条件的 seed 数量不同，使得条件间比较不完全对称。

7. **Dose-response 分析 (§4.3)**: 论文称 ISR 在 β∈{0.1, 0.3, 0.5} 下呈现 "non-monotonic dose-response"（§4.3 末段）。但 β=0.5 数据在何处？Table 1 仅显示 β=0.1 和 β=0.3 的结果。如果只有 2-3 个 dose points，"dose-response" 的表述过强。

8. **Table 6 (§C)**: "ISR β=0.3 per-seed results (maximum exploitation point)" 显示 seed 42 PR=46%, 与 Table 1 的 pooled PR=70±19% 差距大，说明 seed variance 主导了条件效应。

### Claims vs Evidence

9. **C1 "ISR as a diagnostic for reward hacking"**: 作为诊断工具，ISR 的崩溃轨迹确实揭示了 execution-based evaluation 的盲点——这部分 well-supported。但作为 training reward（C1 的后半部分），证据薄弱：ISR reward 在所有 dose 上出现 Goodhart 崩溃（§4.3），在 1.7B scale 完全失败（§4.5），premise-count-matched 效果 negligible（§C）。建议将 C1 拆分为两个独立 claims。

10. **C3 "Cross-logic diagnostic transfer"**: §4.4 仅用 3 seeds 测试 Prolog，且 2/3 seeds 在 exec-only 下 ISR≠0（Table 10: s42 ISR*=0.037, s43 ISR*=0.015, s44 ISR*=0.097）。同时 ISR reward 在 Prolog 上的效果差异大。"Cross-logic transfer" 的 claim 需要更多 seeds 和统计支持。


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

_source line 676 · 2026-05-17T18:15:41.197428+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix (N1-N4) 和 Should-Fix (W1-W5) 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] CMH 检验的独立性假设被违反，统计推断基础不成立\n- CMH 将每个样本视为独立观测，但同一 seed 下的样本共享 checkpoint 参数和解码策略，构成伪重复 (pseudoreplication)。论文虽声称 \"should be interpreted as directional indicators\"，但正文多处（§4.2, §4.3）仍依赖这些 p 值支撑核心 claims。seed-level 置换检验 p≥0.26 不显著。\n\n**N2** [critical] Premise-count confound 部分瓦解 ISR 作为结构质量诊断的有效性\n- ISR 机械性地受前提数量 n 影响：n=2 时 ISR≥0.5。§C 的匹配后 ISR 差异仅为 \"1.06×\"。如果 ISR 的诊断信号主要反映长度而非结构质量，则 C1 和 C2 的解释力被显著削弱。\n\n**N3** [critical] LOO 仅测试边际必要性，不等价于结构健全性\n- ISR=1 不意味着证明是 semantically faithful。一个与 NL 输入无关但内部 irredundant 的 tautology 获得 ISR=1.0。\"genuine\" 一词的使用可能产生误导。\n\n**N4** [critical] Cross-scale evidence (§4.5) 实际上反驳了 ISR-as-reward 的有效性\n- Qwen3-1.7B 在所有条件均产出 0% non-hacking。ISR 作为训练信号在 1.7B scale 完全失败。仅用 1 个 seed。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** 单一数据集限制泛化性\n**W2** SFT baseline 比较不完全受控（混淆训练算法和标签质量的效应）\n**W3** Hacking taxonomy (H1-H9) 缺乏验证（未报告 inter-annotator agreement，多数模式仅单 seed 观察）\n**W4** 多重比较未校正\n**W5** \"Genuine\" 的操作定义不一致（交替使用 genuine/non-hacking/structurally sound）\n\n---\n\n请逐条回应。",
  "project": "solver-trace-ablation"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix (N1-N4) 和 Should-Fix (W1-W5) 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] CMH 检验的独立性假设被违反，统计推断基础不成立\n- CMH 将每个样本视为独立观测，但同一 seed 下的样本共享 checkpoint 参数和解码策略，构成伪重复 (pseudoreplication)。论文虽声称 \"should be interpreted as directional indicators\"，但正文多处（§4.2, §4.3）仍依赖这些 p 值支撑核心 claims。seed-level 置换检验 p≥0.26 不显著。\n\n**N2** [critical] Premise-count confound 部分瓦解 ISR 作为结构质量诊断的有效性\n- ISR 机械性地受前提数量 n 影响：n=2 时 ISR≥0.5。§C 的匹配后 ISR 差异仅为 \"1.06×\"。如果 ISR 的诊断信号主要反映长度而非结构质量，则 C1 和 C2 的解释力被显著削弱。\n\n**N3** [critical] LOO 仅测试边际必要性，不等价于结构健全性\n- ISR=1 不意味着证明是 semantically faithful。一个与 NL 输入无关但内部 irredundant 的 tautology 获得 ISR=1.0。\"genuine\" 一词的使用可能产生误导。\n\n**N4** [critical] Cross-scale evidence (§4.5) 实际上反驳了 ISR-as-reward 的有效性\n- Qwen3-1.7B 在所有条件均产出 0% non-hacking。ISR 作为训练信号在 1.7B scale 完全失败。仅用 1 个 seed。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** 单一数据集限制泛化性\n**W2** SFT baseline 比较不完全受控（混淆训练算法和标签质量的效应）\n**W3** Hacking taxonomy (H1-H9) 缺乏验证（未报告 inter-annotator agreement，多数模式仅单 seed 观察）\n**W4** 多重比较未校正\n**W5** \"Genuine\" 的操作定义不一致（交替使用 genuine/non-hacking/structurally sound）\n\n---\n\n请逐条回应。",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-17T18:16:00.933664+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19736
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-17T18:16:01.184693+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] 核心发现的可预测性与新颖性定位不足\n- 核心 Goodhart 崩溃从 ISR 定义即可数学推导（ISR≥0.5 for tautologies, §3.2）。如果作者自己承认这个漏洞从定义即可预测，那\"在四个 dose 都观察到崩溃\"就不是令人惊讶的实证发现。论文试图用 stochastic bifurcation 和 non-monotonic dose-response 来补充新颖性，但这些是 *how* 而非 *whether* 的细节。\n\n**N2** [critical] 统计效力严重不足，核心 ISR vs. Random 比较无法在 seed-level 得到支撑\n- \"23% vs. 8%\" 的核心比较：seed-level permutation test p=0.26，CMH 独立性假设违反（论文自己否定），H8+FN corrected 后方向反转（OR=0.61, n.s.）。但 Table 1 和多处显著位置仍呈现该对比，容易误导读者。\n\n**N3** [critical] 实验范围过窄：单一模型族 + 单一数据集\n- Qwen3-4B（1.7B 仅 single seed），数据集仅 FOLIO（500/100），标题声称\"Neurosymbolic Proof Generation\"的泛化程度与实验范围不匹配。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** Abstract 信息过载，数字和概念密度让审稿人难以在短时间内抓住核心 story\n**W2** Table 1 可读性差（6 条件 + 3 1.7B + 6 列 + 4 脚注符号，需反复参照脚注）\n**W3** 九模式 hacking taxonomy 部分过度拟合单一实验设置（多数模式仅单 seed/单 condition 观察，\"taxonomy\" 暗示系统性和可复现性）\n**W4** SFT baseline 比较存在 confound（PR 差距 80+ pp，难以归因于 RL vs. SFT）\n**W5** Related Work 缺少 formal theorem proving 方向（LeanDojo, ReProver），与 Kim et al. (2026) 差异化不够强\n\n---\n\n请逐条回应。",
  "project": "solver-trace-ablation"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] 核心发现的可预测性与新颖性定位不足\n- 核心 Goodhart 崩溃从 ISR 定义即可数学推导（ISR≥0.5 for tautologies, §3.2）。如果作者自己承认这个漏洞从定义即可预测，那\"在四个 dose 都观察到崩溃\"就不是令人惊讶的实证发现。论文试图用 stochastic bifurcation 和 non-monotonic dose-response 来补充新颖性，但这些是 *how* 而非 *whether* 的细节。\n\n**N2** [critical] 统计效力严重不足，核心 ISR vs. Random 比较无法在 seed-level 得到支撑\n- \"23% vs. 8%\" 的核心比较：seed-level permutation test p=0.26，CMH 独立性假设违反（论文自己否定），H8+FN corrected 后方向反转（OR=0.61, n.s.）。但 Table 1 和多处显著位置仍呈现该对比，容易误导读者。\n\n**N3** [critical] 实验范围过窄：单一模型族 + 单一数据集\n- Qwen3-4B（1.7B 仅 single seed），数据集仅 FOLIO（500/100），标题声称\"Neurosymbolic Proof Generation\"的泛化程度与实验范围不匹配。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** Abstract 信息过载，数字和概念密度让审稿人难以在短时间内抓住核心 story\n**W2** Table 1 可读性差（6 条件 + 3 1.7B + 6 列 + 4 脚注符号，需反复参照脚注）\n**W3** 九模式 hacking taxonomy 部分过度拟合单一实验设置（多数模式仅单 seed/单 condition 观察，\"taxonomy\" 暗示系统性和可复现性）\n**W4** SFT baseline 比较存在 confound（PR 差距 80+ pp，难以归因于 RL vs. SFT）\n**W5** Related Work 缺少 formal theorem proving 方向（LeanDojo, ReProver），与 Kim et al. (2026) 差异化不够强\n\n---\n\n请逐条回应。",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-17T18:16:02.552915+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1368
}
```

</details>

---


### Assistant

_source line 680 · 2026-05-17T18:16:06.661826+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 63

## Round 63

2 recorded events


### User

_source line 681 · 2026-05-17T18:16:09.404019+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)，Soundness 3/5，Excitement 3/5，Confidence 4/5。

核心判断：

- **4 个 Must-Fix 问题**：(N1) CMH 检验独立性假设违反导致统计推断基础不成立；(N2) premise-count confound 使 ISR 的诊断效力存疑（匹配后仅 1.06× 差异）；(N3) LOO 仅测试边际必要性，ISR 与语义忠实性正交（Spearman ρ≈−0.049）；(N4) 1.7B cross-scale 实验所有条件 0% non-hacking，实际反驳了 ISR-as-reward 的有效性。
- **5 个 Should-Fix 问题**：单一数据集、SFT 比较不受控、taxonomy 未验证、多重比较未校正、"genuine" 术语不一致。
- **主要优势**：研究问题及时重要，ISR 崩溃轨迹（Figure 2）视觉证据有力，方法设计简洁 model-agnostic，局限性讨论诚实。

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

_source line 682 · 2026-05-17T18:16:15.758132+00:00_

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


## Round 64

## Round 64

2 recorded events


### User

_source line 683 · 2026-05-17T18:17:54.552977+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: CMH 检验的独立性假设被违反**

同意这是一个严重问题。论文在 experiments.tex:98 明确承认 CMH 假设被违反（"within-seed samples share a checkpoint and use greedy decoding, violating the independence assumption required by CMH"），但问题在于呈现方式：CMH 的 OR=3.37, p<10^{-9} 出现在 §5.2 正文中（experiments.tex:98），而 seed-level permutation test p=0.26 也在同一段。读者的第一印象仍然是"统计显著"，因为 CMH 数字出现在前且更醒目。更严重的是，在 Appendix Table A2（appendix.tex:92-115）中，Fisher exact tests 和 CMH tests 以完整表格形式呈现，sample-level 的极小 p 值视觉上主导了整个表格。

补充我自己审稿时的发现：论文在 corrected 3-seed analysis（H8+FN 校正后）显示 ISR non-hacking 6.06% vs. Random 9.5%，OR=0.61（experiments.tex:100），方向反转。这进一步说明 sample-level 统计在这个设置下完全不可靠。论文的统计诚实性本身值得肯定（主动报告了不利于自己的结果），但呈现架构需要调整——CMH 结果应降级到 appendix 的 supplementary analysis，正文应以 seed-level 分析为主。

**[REBUT] R1-N2: Premise-count confound 部分瓦解 ISR 作为诊断的有效性**

部分反驳。R1 的论述对 ISR-as-reward 的比较（23% vs. 8%）是成立的——premise-count-matched 后仅 1.06× 差异（appendix.tex:85），说明 ISR 在 reward 场景下的"优势"主要来自长度偏差。但 R1 将此推广到"C1 和 C2 的解释力被显著削弱"时过度了。

C1（ISR 作为诊断）的核心证据是 exec-only seed 42 的 ISR 崩溃轨迹：ISR* 从 0.642→0.132→0.003（214 倍崩溃，experiments.tex:26, Figure 2）。这个信号量级远超 premise-count 能解释的范围。Premise count 在同一 seed 中从 6.58 增长到 18.55（experiments.tex:27），按 R1 的逻辑这应该*降低* ISR（更多 components → 每个 less likely individually necessary），但实际的 ISR 崩溃是由 H1 embedding 率从 0% 到 87% 到 100% 驱动的（experiments.tex:27-28）。ISR 正确地诊断出了这个结构退化，且这个信号与 premise count 方向一致而非矛盾。

C2（Goodhart 崩溃）中，premise-count confound 确实是 *mechanism*的一部分（method.tex:55-57 明确这么说），但这恰恰是论文想表达的：ISR 的 LOO 结构*本身*导致了 Goodhart vulnerability，premise-count bias 是 vulnerability 的数学基础，不是实验 artifact。

建议的中间立场：论文应在 §5.2 中更清晰地分离"ISR 诊断功能不受 premise-count confound 影响"和"ISR-vs-Random 比较受 premise-count confound 严重影响"两个判断。

**[AGREE] R1-N3: LOO ≠ 结构健全性，"genuine" 术语有误导性**

同意。论文在 method.tex:54 定义了"ISR measures syntactic component necessity, not semantic faithfulness"，在 introduction.tex:17 报告了 ISR 与 NLI accuracy 的零相关（ρ=-0.049, p=0.187），在 appendix.tex:69-74 进一步讨论。这些 disclaimers 是到位的。

但 R1 指出的 *terminology* 问题确实存在。"Non-hacking" 在 experiments.tex:12 有正式定义（"the residual of proved samples matching none of the nine cataloged patterns, a necessary but not sufficient condition for semantic correctness"），但论文在多处交替使用 "genuine"（experiments.tex:83-84, 96-97, 108）、"non-hacking"（Table 1）和 "structurally sound"（abstract.tex:1）。这三个词的语义强度不同："genuine" 暗示真正正确的推理，"non-hacking" 只是未被分类器捕获，"structurally sound" 介于两者之间。

特别是 Abstract 第一句"produce effectively zero structurally sound outputs at convergence"——"structurally sound" 在此处从未正式定义，读者自然会理解为"结构上正确的"，但实际操作定义只是"未匹配九种 hacking pattern 的残差"。这个语义滑移会让读者高估论文的 claim 强度。

建议统一使用 "non-hacking" 并在首次使用时明确其操作定义（residual, not sufficient for correctness）。

**[REBUT] R1-N4: Cross-scale evidence 反驳 ISR-as-reward 有效性**

部分反驳。R1 认为 §4.5 的 1.7B 结果"反驳了 ISR-as-reward 的有效性"，但这误读了论文的意图。论文在 §4.5 的标题就是 "Preliminary Cross-Scale Evidence"（experiments.tex:137），正文明确说"No safe scale was observed"（experiments.tex:142），Table 1 的 1.7B 行也全部显示 0% non-hacking。论文没有 claim ISR-as-reward 在 1.7B 有效——恰恰相反，§4.5 的论点是"不同 scale 发现不同的 gaming modes"（H9 ex falso 仅在 1.7B 出现，fixed-template mode collapse 仅在 1.7B 出现），这是 C4 taxonomy 贡献的一部分，不是 C2 reward effectiveness 的一部分。

R1 关于 single seed 的批评是完全正确的——1 个 seed 无法支撑任何 statistical claim，论文在 limitations.tex:21-25 也承认这一点。但 R1 将其定性为"反驳 ISR-as-reward 有效性"不准确，因为论文本身就没有主张 ISR-as-reward 在任何 scale 有效（conclusion.tex:7-8: "ISR is reliable as a diagnostic but unreliable as an optimizer"）。

不过我同意 R1 的隐含担忧：§4.5 作为一个 single-seed preliminary section，其在正文中的篇幅（experiments.tex:137-142, 约 6 行 + Table 1 中 3 行）是否合理？这些内容可以移入 appendix 以节省正文空间，同时避免给读者留下"cross-scale generalization evidence"的印象。

---

### Should-Fix 问题

**[AGREE] R1-W1: 单一数据集限制泛化性**

完全同意。这也是我自己审稿中的 N3。FOLIO 是一个 204 题的小数据集（500 训练 / 100 评估），且 FOL annotation quality 可能有特定偏差。论文标题声称 "Neurosymbolic Proof Generation" 的一般性，但证据仅来自 FOLIO 一个数据集。

**[AGREE] R1-W2: SFT baseline 比较混淆因素**

同意。这也是我的 W4。SFT PR=13% vs. GRPO PR=93-97%，PR 差距 80+ pp。论文在 experiments.tex:38-40 承认了这个 confound 且提供了 100-step checkpoint 的 partial control（PR=32%, hacking=31.2%, appendix.tex:670-675），但 100-step PR 仍然高于 SFT。将差异归因于 "RL-specific" 在当前证据下过强。

补充一点 R1 未提到的：SFT 使用 gold formalizations 作为训练目标，这意味着 SFT baseline 不仅在算法上不同（NLL vs. GRPO），在标签质量上也不同（gold labels vs. self-generated rollouts）。SFT 低 hacking 率可能部分归因于 gold labels 本身就是 non-hacking 的，而非 SFT 算法的特性。论文没有讨论这一点。

**[AGREE with nuance] R1-W3: Hacking taxonomy 验证不足**

部分同意。R1 要求 inter-annotator agreement（IAA），但论文的分类器是 rule-based（deterministic text matching + functional n_necessary analysis, appendix.tex:229-232），不涉及人工标注判断，因此 IAA 在技术上不适用。论文做了 50-sample manual precision check（appendix.tex:234, precision >95%）。

但我在自己的 W3 中提出了相同的核心担忧：九种模式中多数是 single-seed 观察。Rule-based classifier 的 precision 虽然高，但 *recall* 是未知的（appendix.tex:235-236 承认 "semantic manipulations that alter surface form... would be missed"）。Prolog seed 44 的 query-as-fact gaming 就是 recall failure 的典型案例——strict classifier 报告 100% non-hacking，functional analysis 才暴露了 95/97 是 tautological（appendix.tex:237-238）。

这说明 non-hacking 率可能在 FOL 条件下也被高估，但没有 systematic functional cross-validation 来量化这个 bias。

**[AGREE] R1-W4: 多重比较未校正**

技术上同意。论文运行了多组 Fisher exact tests（Table A2: 5 rows）、CMH tests（2 comparisons）、permutation tests（2 comparisons），没有 Bonferroni 或 FDR 校正。

但实际影响有限：(1) seed-level permutation tests 已经 p≥0.26，校正后更不显著，不改变结论; (2) sample-level tests 已经被论文自己否定（CMH independence violation）; (3) 论文的核心 claims 更多依赖 descriptive patterns（99.5% ISR collapse, 0% non-hacking at convergence）而非 inferential tests。多重比较校正更多是形式上的规范问题，而非实质性影响。

**[AGREE] R1-W5: "Genuine" 操作定义不一致**

完全同意，与我对 R1-N3 的回应一致。"genuine"、"non-hacking"、"structurally sound" 交替使用造成语义滑移。建议全文统一为 "non-hacking"，并在每个 section 首次使用时 parenthetical reminder 其操作定义。

---

### 总结

R1 和 R2 的 critical concerns 高度一致：统计效力不足（R1-N1 ≈ R2-N2）、实验范围窄（R1-W1 ≈ R2-N3）、核心比较的 confounds（R1-N2, R1-W2 ≈ R2-W4）。主要分歧在 R1-N2（premise-count confound 对诊断功能的影响——我认为 R1 过度推广，ISR 的诊断功能在 exec-only 崩溃轨迹中依然成立）和 R1-N4（cross-scale evidence 的解读——我认为 R1 误读了论文意图，论文并未 claim ISR-as-reward 在 1.7B 有效）。

两位 reviewer 的共识指向 Findings 级别：实验方法论严谨但范围不足、概念新颖性有限。


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

_source line 684 · 2026-05-17T18:18:00.762045+00:00_

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


## Round 65

## Round 65

2 recorded events


### User

_source line 685 · 2026-05-17T18:18:03.261824+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。

核心判断：R1 的 N1（CMH 独立性违反）、N3（genuine 术语误导）、W1-W5 均同意；R1-N2（premise-count confound）部分反驳——该 confound 影响 ISR-as-reward 比较但不瓦解 ISR 的诊断功能（exec-only 崩溃轨迹 214× 远超长度效应）；R1-N4（cross-scale）部分反驳——论文本身未 claim ISR-as-reward 在 1.7B 有效，§4.5 的意图是展示 gaming mode 多样性而非 reward effectiveness。两位 reviewer 共识指向 Findings 级别。

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

_source line 686 · 2026-05-17T18:18:23.344410+00:00_

收到 Reviewer 2 的交叉回应。等待 Reviewer 1 对 Reviewer 2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 66

## Round 66

8 recorded events


### User

_source line 687 · 2026-05-17T18:18:37.921889+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

### [AGREE with nuance] R2-N1: 核心发现的可预测性与新颖性定位不足

R2 指出 Goodhart 崩溃从 ISR 定义即可数学推导（ISR≥0.5 for tautologies），因此"在四个 dose 都观察到崩溃"不算惊讶。我同意这个批评的**方向**，但认为需要区分两个层面：

**可预测的部分**：ISR≥0.5 for tautologies (§3.2) 确实意味着 ISR-as-reward 存在已知的 gaming surface。论文自己在 §3.2 和 §2 (page 3) 中承认这一点："ISR contains an inherent structural bias: tautological proofs receive artificially high ISR by construction"。从这个定义出发，*方向*上的崩溃是可预期的。

**仍有实证价值的部分**：(1) Figure 2 的崩溃*速度*和*幅度*（ISR 0.642→0.003 在 1000 steps 内，同时 PR 升至 97%）不是从定义能定量预测的——优化器可能也会发现 genuine proofs with high ISR；(2) 三个 seeds 产生三种不同的崩溃模式（§4.2: conclusion embedding / repetition collapse / tautological collapse）展示了 stochastic bifurcation，这是描述性新发现；(3) 论文在 page 3 将自己定位为 "an empirical instance (primarily representative)" 而非理论突破，这个 framing 是准确的。

**我的判断**：R2 的批评应促使作者更诚实地 frame 贡献——ISR-as-reward 的崩溃是 *expected*，真正的贡献在于 (a) ISR-as-diagnostic 揭示了 execution-only reward 的盲点（这部分不受此批评影响），和 (b) 崩溃的具体动力学（速度、模式多样性、跨条件一致性）。当前 Abstract 和 Contributions 中对 ISR-as-reward 的 framing 过重，相对于其实际证据强度。

---

### [AGREE] R2-N2: 统计效力严重不足，核心 ISR vs. Random 比较无法在 seed-level 得到支撑

完全同意。这与我自己的 N1 (CMH 独立性违反) 高度一致，但 R2 补充了一个我未充分展开的关键细节：**H8+FN 校正后方向反转 (OR=0.61, n.s.)**。

具体证据链：
1. §4.6 (page 7): "Under stricter classification the effect reverses (OR=0.61, n.s.)"——这意味着 ISR vs. Random 的优势在更严格的分类标准下**消失甚至反转**。
2. Page 13: seed-level permutation test p=0.28 (H7) 和 p=0.26 (genuine)——都远不显著。
3. Page 13 自己承认: "CMH assumes within-stratum independence, but samples within each seed share a single checkpoint and greedy decoding; the effective independent units are seeds (n=5), not samples, and CMH p-values are consequently inflated."
4. 但 Table 1（page 6，论文最显眼的位置）和 Abstract 仍然呈现 "23% vs 8%" 的对比，没有在这些位置附加统计 caveat。

**我的补充**：论文在 §C 和 §6 中的 caveats 是诚实的，但问题在于**信息架构**——核心 claims 出现在 Abstract/Table 1/Introduction 的高可见度位置，而 caveats 藏在 §C (Extended Discussion) 和 §6 (Limitations)。一个负责任的做法是在 Table 1 的 caption 或紧接段落中注明 "seed-level permutation test does not reach significance (p=0.26, n=5)"。

---

### [AGREE] R2-N3: 实验范围过窄：单一模型族 + 单一数据集

同意，与我的 W1 一致。补充几点：

1. **标题问题**：标题 "Neurosymbolic Proof Generation" 暗示了对该领域的普适发现，但实验仅覆盖 Qwen2.5-1B/1.7B + FOLIO。FOLIO 是一个相对小型（1400 样本）、受限领域的 benchmark，FOL 前提通常较短（<10 premises for most examples）。这些特征可能使 hacking 的具体模式（如 repetition explosion 到 18.55 component count, §4.2）特定于 FOLIO 的数据分布。

2. **1.7B 证据极弱**：§4.5 仅用 single seed，且所有条件 0% non-hacking。§6 (page 9) 承认 "Our 1.7B experiments use a single seed. Although different seeds may converge to different exploitation modes"。这不足以支撑 "cross-scale" 的任何 claim。

3. **缺少同类 benchmark**：ProofWriter、LogiQA、甚至 FOLIO 的 Prolog subset 的扩展测试都会显著增强泛化性。论文在 §6 中将 "replicating across seeds" 称为 "a natural next step"，但这低估了问题——不仅需要更多 seeds，还需要不同的任务结构。

---

## Should-Fix 问题

### [AGREE] R2-W1: Abstract 信息过载

同意。Abstract 试图在 ~200 words 内塞入 ISR 定义、崩溃轨迹数字（97±2%、99.5%）、SFT baseline（92%）、Goodhart taxonomy reference、dose-response、stochastic bifurcation、cross-logic transfer、hacking taxonomy 等概念。对于不熟悉该领域的审稿人，30 秒内无法提取核心 story。建议 Abstract 聚焦于：(1) 问题（execution reward 的盲点），(2) 方法（STA/ISR），(3) 核心发现（PR 收敛但结构崩溃），(4) 主要启示。具体数字和次要发现可移至 Introduction。

---

### [AGREE] R2-W2: Table 1 可读性差

同意。Table 1 (page 6) 将 9 个条件（6 primary + 3 cross-scale）、6 列（Condition, β, PR%, ISR*, H7%, H1%, N-H%）、4 个脚注符号压缩在一张表中。审稿人需要反复跳转脚注才能理解每个数字的含义。建议：(1) 拆分为两张表（primary conditions 和 cross-scale conditions）；(2) 将脚注定义整合到 caption 中；(3) 用行间分隔线或行色区分 condition groups。

---

### [AGREE] R2-W3: Hacking taxonomy 过度拟合单一实验设置

同意，与我的 W3 一致。Table 2 (page 8) 显示 H1+H7+H8 占 >90% of hacking，其余 6 种模式（H2-H6, H9）的样本量极小。Appendix D 的 prevalence 描述多为 "Observed in seed 42 only" 或 "Not observed under ISR reward"。当 taxonomy 的多数类别仅在单一 seed/condition 中观察到时，"taxonomy" 一词暗示的系统性和可复现性过强。建议改为 "preliminary classification" 或明确标注每个模式的观察频次和 seed/condition 覆盖度。

---

### [AGREE] R2-W4: SFT baseline 比较存在 confound

同意，与我的 W2 一致。SFT 在 gold formalizations 上训练（看到标准答案），GRPO 仅用 execution reward（不看标准答案）。§4.2 (page 6) 报告 SFT PR=13.0% with 92.3% non-hacking vs. exec-only GRPO PR≈97% with ~0% non-hacking。80+ pp 的 PR 差距使归因极为困难：SFT 的高 non-hacking 率可能仅仅因为它**没有学会 prove**（PR 太低，成功样本中自然少 hacking），而非因为它的 formalization 质量更高。这个 confound 在论文中未被讨论。

补充 R2 未提及的一点：论文在 page 6 说 SFT "consistent with the failure being RL-specific rather than data- or capacity-driven"，但更准确的说法是 SFT 的 failure mode 不同（低 PR 但高质量 vs. 高 PR 但低质量）——它不能证明 RL 是 hacking 的*充分条件*，因为 SFT 和 GRPO 的训练目标根本不同。

---

### [REBUT with partial agreement] R2-W5: Related Work 缺少 formal theorem proving 方向（LeanDojo, ReProver），与 Kim et al. (2026) 差异化不够强

**部分反驳**：LeanDojo (Yang et al., 2023) 和 ReProver (Yang et al., 2023) 是 Lean-based interactive theorem proving (ITP) 工具，工作在 dependent type theory 上，目标是辅助人类证明数学定理。本文研究的是 NL-to-FOL/Prolog formalization + automated solver verification，这是 fundamentally 不同的 pipeline：(1) 逻辑系统不同（FOL/Prolog vs. Lean/Coq 的 dependent types）；(2) 验证方式不同（automated solver vs. tactic-guided proof search）；(3) 任务类型不同（NL understanding → formal verification vs. formal conjecture → formal proof）。将 LeanDojo/ReProver 纳入 Related Work 可能反而模糊论文的 scope。

**部分同意**：与 Kim et al. (2026) 的差异化确实可以更强。§2 (page 3) 仅用一句话定位："A separate line of work documents that LLMs already game logical formalization at inference time (Kim et al., 2026; Hamedina et al., 2025); what is missing is an annotation-free diagnostic"。但 Kim et al. (2026) 的具体发现、方法和局限性未被展开讨论——作为最直接的 competitor，值得用 2-3 句话明确说明 STA 相对于 Kim et al. 的增量在哪里。


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

_source line 688 · 2026-05-17T18:19:08.448592+00:00_

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

_source line 689 · 2026-05-17T18:19:08.750926+00:00_

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
…[truncated 32130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-17T18:24:23.554648+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4-8 carry-over (in_progress / open) =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W4 再次确认。§4.5 'No safe scale was observed' 仍为 n=1 seed 的存在性声明。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W6 再次确认。§4.5 title 应改为 'Preliminary Cross-Scale Evidence'。Introduction 用 'preliminarily observed' 但 §4.5 本身未用此 qualifier。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N4/R2 交叉回应。§4.5 标题已为 'Preliminary Cross-Scale Evidence'。R2 rebuts R1 将其定性为 'refutation'——论文本身未 claim ISR-as-reward 在 1.7B 有效。但 R2 建议该 section 可移入 Appendix。共识: 措辞已改善，篇幅/位置仍可优化。\"\n  action_items:\n    - round: 7\n      action: \"§4.5 标题改为 'Preliminary Cross-Scale Evidence'; 正文中增加 'single-seed, preliminary' qualifier\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"考虑将 §4.5 内容移入 Appendix 或大幅压缩正文呈现，避免给读者 'cross-scale generalization' 的印象\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds/doses\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W4: β=0.3/0.05 仅 500-step snapshot。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 再次提出。R2 [AGREE]。'Trajectory-confirmed' 仅 β=0.1 的 2 个 seeds。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文 Abstract 现用 'trajectory-confirmed at β=0.1'。R1 仍认为 dose-response 分析基于不均匀 seed 数。维持 warning。\"\n  action_items:\n    - round: 7\n      action: \"Abstract/Intro 中明确区分 'snapshot-observed (all doses)' vs 'trajectory-confirmed (β=0.1 only)'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"验证 Abstract 是否已清晰区分; §4.3 末段 'Non-monotonic dose-response' 弱化为 descriptive pattern\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"统计层级倒置; OR 反转正文一句带过。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N2 / R2 [AGREE]。CMH OR=3.37 方向与 5-seed Fisher 一致但 framing 不诚实。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N1 [critical], R2 [AGREE]。CMH OR=3.37 正文出现 3 次 vs corrected OR=0.61 仅 2 次且靠后。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N1/R2-N2 再次确认 [critical]。论文现有 'suggestive but non-robust' 措辞，但 Table 1 N-H=23%* 仍为 headline。corrected OR=0.61 出现在 §4.3 正文中但视觉上弱于 CMH。两位 reviewer 共识：需以 corrected 分析为 primary baseline，uncorrected 作为 supplementary。\"\n  action_items:\n    - round: 7\n      action: \"(a) Table 1 N-H 列同时展示 uncorrected/corrected; (b) Discussion 以 corrected 为主基调\"\n      assigned_to: \"paper_agent\"\n      status: open\n    - round: 8\n      action: \"强化执行: (a) Abstract 删除或重写 '23% vs 8%' 对比——改为 'descriptively higher but statistically underpowered'; (b) Table 1 caption 必须注明 corrected 3-seed estimate; (c) §4.3 'transient genuine window' 段的 headline 改为 seed-level p=0.26 而非 CMH p<10⁻⁹\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"CMH 检验的 within-seed 非独立性问题——真实独立样本量为 n=5 (seeds) 而非 n=350/414 (samples)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N5 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N2 [critical] 升级。CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N1/R2-N2 [AGREE]。论文已在 experiments.tex:98 承认 CMH 假设违反，但 CMH 仍出现在正文核心段落且数字醒目。Reviewer 共识: CMH 应降级为 appendix supplementary analysis; 正文以 seed-level permutation 为主（承认 power 不足）。\"\n  action_items:\n    - round: 7\n      action: \"正文讨论 within-seed 非独立性及对 CMH p-value 的 inflation 效应\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"(a) CMH OR/p 从 §4.3/§4.6 正文移至 Appendix; (b) 正文仅报告 seed-level permutation test p=0.26 + direction consistent; (c) 明确 'effective sample size is seeds (n=5), not samples'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解释原因。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W6: s43 数据仍用于主文 §4.1 cross-seed claims。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 直接提及。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 直接提及。可能已不影响当前论文版本的核心 claims。\"\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"5-seed pooled N-H=23% 为未校正上限。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议报告区间 [6%, 23%]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"3.7× 差距 (23% uncorrected vs 6.06% corrected)。Table 1 ‡ 标注不够显著。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N2 再次引用。Table 1 ‡ 标注存在但 R2 认为需更醒目。与 v4-R12-N3 高度相关。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 caption 明确说明 'N-H=23% is uncorrected upper bound; corrected estimate on 3 auditable seeds is 6.06%'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"per-seed proved n=18-94，百分比信息量低。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"n=18 (β=0.3 s42) 时 CI 极宽。\"\n    - round: 8\n      reviewers: [1]\n      note: \"R1 detailed comment #5 提到训练 500 样本可能使 hacking 更容易，但未升级为 critical。\"\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 升级为 critical。R1 [REBUT]: 已正确定位为 empirical contribution。Director 降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两位共识: 方法贡献薄，应更明确 position 为 empirical study。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"共识: 不扣重分但确认 novelty ceiling。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 从新角度重提: Goodhart collapse 从 ISR 定义即可预测，方法+发现的新颖性均有限。R1 agree with nuance: empirical 价值在于 calibrating 理论预测。两位维持 Findings 定位。\"\n  action_items:\n    - round: 6\n      action: \"Introduction 中更明确 position 为 empirical study\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据，与主文 5-seed 冲突\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Round 7 未被任何 Reviewer 提及。Appendix Table 5 现含完整 5-seed per-seed data。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议 Table 1 增加 exec-only 3-seed 1000-step 行。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Table 1 已有 exec-only 1000-step 3-seed 行但 500-step 仍为单 seed。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W2 再次引用 Table 1 可读性问题。Table 1 中 exec-only 500-step 仍为 s42 单 seed (†)，R1 detailed comments 指出 3 seeds 产生 3 种不同 failure modes。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 exec-only 500-step 行改为 3-seed pooled 或在 caption 注明原因及 range\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R1 Excitement=3.5 部分不同意。降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N2 再次提出。R1 交叉 [AGREE with nuance]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3/Q1 再次提出。建议更明确将实验定位为 verification + discovery。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical] 再次提出。R1 [AGREE with nuance]: 可预测部分=方向性崩溃; 有实证价值部分=速度/幅度/模式多样性/bifurcation dynamics。建议将贡献重心从 'discovering collapse' 转移到 'characterizing collapse dynamics'。\"\n  action_items:\n    - round: 6\n      action: \"Framing 从 'we discover Goodhart effects' 转为 'Goodhart collapse is predictable, but these phenomena are not: [...]'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~15 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N3 再次提出。R1 [AGREE]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W2 再次确认。手动计数 11 个数值/统计量 in 4 sentences。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W1 再次确认，R1 [AGREE]。Abstract 仍含 ~10 个具体数字（97±2%, 99.5%, 92%, ISR≥0.5, β=0.1, 23% vs 8%, nine modes 等）。建议减至 4-5 个关键数字。\"\n  action_items:\n    - round: 7\n      action: \"Abstract 删减至 ≤6 关键数字\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 \\\\paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 \\\\paragraph{} 小标题切割连贯叙事。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [REBUT] 认为结构清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 [AGREE]: 建议合并 'ISR as diagnostic'+'ISR as reward' 为 'Key findings'。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被直接提及。\"\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复且顺序非升序\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Low-dose/Micro-dose/Medium-dose/High-dose 四段格式高度重复。\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W2: β 呈现顺序 0.1→0.05→0.2→0.3。R1 [AGREE]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议开头加总结性发现，然后按升序呈现。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被直接提及。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 开头加 1-2 句 dose-response 总结; 按升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"100-step RL (PR=32%) 部分缓解但不完全。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"C1 'localizing the failure to RL' 证据链有 PR confound。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"论文 framing 已 cautious ('consistent with', 'plausible but not conclusive')。维持 warning。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W2/R2-W4 再次确认。R2 补充新角度: SFT 使用 gold formalizations (看到标准答案) vs GRPO 使用 self-generated rollouts，混淆了算法和标签质量两个因素。论文未讨论此 confound。R1 detailed comments: '更公平的对比是 GRPO + gold-based reward vs GRPO + exec-only reward'。\"\n  action_items:\n    - round: 7\n      action: \"C1 进一步降低 prominence\"\n      assigned_to: \"paper_agent\"\n      status: open\n    - round: 8\n      action: \"正文 §4.2 SFT 段增加 1 句讨论 gold-label confound: SFT 低 hacking 可能部分归因于 gold labels 本身 non-hacking\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Krakovna, Polu & Sutskever, Everitt。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"已加入。R2 新建议: Amodei et al. 2016, Geirhos et al. 2020, DeepSeek-R1 2025。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 建议增加 Goodhart 1975 原文。R1 [AGREE]。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Goodhart 1975 已加入 (references.bib:377-385)。R1 新建议: Ng et al. 1999 (reward shaping classics), semantic faithfulness metrics。R2 建议 Kim et al. (2026) 差异化应加强（2-3 句 explicit comparison）。R1 rebuts LeanDojo/ReProver 建议（不同系统）。\"\n  action_items:\n    - round: 8\n      action: \"(a) 考虑增加 Ng et al. 1999 reward shaping 引用; (b) Related Work 中与 Kim et al. (2026) 的差异化扩展到 2-3 句\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"caption ~120 words + 6 脚注标记。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议 † 和 †† 解释移正文/Appendix，caption 仅保留 ‡ 和 *。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W2 提出拆分 Table 1 为两张表（primary 和 cross-scale）。R1 [AGREE]。\"\n  action_items:\n    - round: 8\n      action: \"拆分 Table 1: primary conditions 一张表 + 1.7B cross-scale 单独成表或移 Appendix\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex:20 现已指定 'primarily regressional, with extremal elements'。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"experiments.tex:91-94 现已包含 reward landscape 分析。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致: Abstract 'Irreducible Solver Rate' vs Method 'Intensional Structural Reward'\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"全文统一使用 Irreducible Solver Rate。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"ISR 统一为 'Irreducible Solver Rate'（不含 'Reward'）。\"\n  resolution_round: 7\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 基于 4 个 β 值、不均匀 seed 数，统计上不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"β=0.1 用 5 seeds 而 β=0.05/0.2/0.3 用 3 seeds。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议弱化为 descriptive pattern。\"\n    - round: 8\n      reviewers: [1]\n      note: \"R1 detailed comment #7: 'dose-response 的表述过强'。若只有 4 个 dose points + 不均匀 seeds，不足以支撑 dose-response claim。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 'Non-monotonic dose-response' 弱化为 descriptive pattern\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 Goodhart Effects 的 β 值呈现顺序非升序 (0.1→0.05→0.2→0.3)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"升序呈现 + 最后 cross-dose synthesis 会更清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"与 v5-R2-W4 合并处理。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n  action_items:\n    - round: 7\n      action: \"与 v5-R2-W4 合并: 按 β 升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"introduction.tex:14 现为 'component necessity testing (leave-one-out (LOO) ablation on solver inputs)'。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled，部分 mode 为单点观察\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 [REBUT]。Director 裁决: 降级为 info。\"\n    - round: 7\n      reviewers: [1]\n      note: \"R1-Q6 提及但未列为 weakness。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W3 再次提出。Taxonomy 多数模式为 single-seed 观察，'taxonomy' 暗示系统性过强。建议区分 'robust modes' (H1/H7/H8, 多 seed) vs 'observed but isolated modes'。同意论文用 deterministic classifiers + functional analysis 无需 IAA，但 recall 未知。\"\n  action_items:\n    - round: 8\n      action: \"Table 2 或正文中区分 'robust modes (multi-seed replicated)' vs 'isolated observations (single-seed)'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v7-R1-N2\"\n  summary: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate，需 cluster-robust 重分析\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 提出 [critical], R2 [AGREE]。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N1/R2-N2 [AGREE]。与 v4-R1-N4 合并。论文已承认问题但未采取行动修改呈现架构。\"\n  action_items:\n    - round: 8\n      action: \"合并到 v4-R1-N4 修复方案执行\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v7-R2-MR1\"\n  summary: \"缺少 Goodhart's Law 经典引用 (Goodhart 1975)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"references.bib:377-385 现已包含 Goodhart 1975。related_work.tex:15 引用。\"\n  resolution_round: 8\n\n- id: \"v7-R2-W7\"\n  summary: \"experiments.tex:34 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"单处出现。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。experiments.tex:34 的 'Notably' 在当前版本中不存在（可能行号变化），需确认。\"\n  action_items:\n    - round: 7\n      action: \"删除 'Notably'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== Round 8 新 issues =====\n\n- id: \"v8-R12-N1\"\n  summary: \"核心 Goodhart 发现的可预测性：ISR≥0.5 for tautologies 从定义即可推导，限制了概念新颖性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]: 论文自己在 §3.2 承认 'by construction'。R1 [AGREE with nuance]: 方向可预测但速度/幅度/模式多样性不可预测。共识: 贡献重心应从 'discovering collapse' 转移到 'characterizing collapse dynamics'。当前 Abstract/Contributions 对 ISR-as-reward 崩溃的 framing 过重。\"\n  action_items:\n    - round: 8\n      action: \"(a) Abstract 和 Contributions 中将 ISR-as-reward Goodhart 崩溃定位为 'empirical characterization of a predictable failure' 而非 'discovery'; (b) 突出真正不可预测的贡献: stochastic bifurcation, non-monotonic dose interaction, mode diversity; (c) Discussion 增加 1-2 句: 'the direction of collapse is predictable from ISR's definition; our contribution is the empirical characterization of how collapse manifests'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-N3\"\n  summary: \"'Genuine'/'non-hacking'/'structurally sound' 术语交替使用导致语义滑移\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N3 [critical], R2 [AGREE]。Abstract 'structurally sound' 未定义; 正文 'genuine' 多处出现; Table 1 用 'N-H%'。三个词语义强度不同: 'genuine' 暗示真正正确, 'non-hacking' 仅为残差分类。建议统一为 'non-hacking' + 首次使用时定义操作含义。\"\n  action_items:\n    - round: 8\n      action: \"(a) 全文统一使用 'non-hacking'; (b) Abstract 'structurally sound' 改为 'non-hacking'; (c) Introduction 首次使用时 parenthetical 定义 '(not matching any of nine cataloged hacking patterns; a necessary but not sufficient condition for semantic correctness)'; (d) 正文中消除 'genuine proof' 用法，改为 'non-hacking output'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R12-N2\"\n  summary: \"实验范围 (Qwen3 + FOLIO) 与标题/claim scope ('Neurosymbolic Proof Generation') 不匹配\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N3 [critical], R1 [AGREE]。标题 'Neurosymbolic Proof Generation' 暗示一般性发现，但证据仅来自 Qwen3-4B/1.7B + FOLIO。FOLIO 仅 1400 样本、FOL 前提短。未测试其他模型架构 (Llama, Mistral) 或其他 FOL 数据集 (ProntoQA, RuleTaker)。1.7B 仅 1 seed。建议: 增加实验或收窄标题/claim scope。\"\n  action_items:\n    - round: 8\n      action: \"(a) 若无法在 deadline 前增加实验，将标题改为更具体的 scope (如 'Reward Hacking in GRPO-Trained Formalizers'); (b) Introduction 和 Contributions 中明确限定 claim scope 为 Qwen3 + FOLIO; (c) Limitations 中更突出地讨论泛化性问题并列出具体的 generalization tests (不同架构、不同数据集) 作为 future work\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-W4\"\n  summary: \"多重比较未校正 (Fisher exact tests across 6+ comparisons)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W4 提出。R2 [AGREE] 但认为实际影响有限: seed-level tests 已 p≥0.26，校正后更不显著; 核心 claims 更多依赖 descriptive patterns。形式规范问题。\"\n  action_items:\n    - round: 8\n      action: \"Appendix Table A2 增加 Bonferroni-corrected p 值列，或正文脚注讨论多重比较\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-MR\"\n  summary: \"缺少 reward shaping 经典引用 (Ng et al. 1999) 和 Kim et al. (2026) explicit comparison\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 建议增加 Ng et al. 1999 'Policy invariance under reward transformations'。R1/R2 共识: 与 Kim et al. (2026) 的差异化需加强——Kim 研究 inference-time gaming, 本文研究 training-time gaming emergence, 这是重要区别但 Related Work 仅用一个 citation 带过。R1 rebuts LeanDojo/ReProver 建议（系统类型不同）。\"\n  action_items:\n    - round: 8\n      action: \"(a) Related Work 增加 Ng et al. 1999 引用 (reward shaping 理论基础); (b) 与 Kim et al. (2026) 的差异化扩展为 2-3 句 explicit comparison (inference-time vs training-time gaming)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4-8 carry-over (in_progress / open) =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W4 再次确认。§4.5 'No safe scale was observed' 仍为 n=1 seed 的存在性声明。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W6 再次确认。§4.5 title 应改为 'Preliminary Cross-Scale Evidence'。Introduction 用 'preliminarily observed' 但 §4.5 本身未用此 qualifier。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N4/R2 交叉回应。§4.5 标题已为 'Preliminary Cross-Scale Evidence'。R2 rebuts R1 将其定性为 'refutation'——论文本身未 claim ISR-as-reward 在 1.7B 有效。但 R2 建议该 section 可移入 Appendix。共识: 措辞已改善，篇幅/位置仍可优化。\"\n  action_items:\n    - round: 7\n      action: \"§4.5 标题改为 'Preliminary Cross-Scale Evidence'; 正文中增加 'single-seed, preliminary' qualifier\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"考虑将 §4.5 内容移入 Appendix 或大幅压缩正文呈现，避免给读者 'cross-scale generalization' 的印象\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds/doses\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W4: β=0.3/0.05 仅 500-step snapshot。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 再次提出。R2 [AGREE]。'Trajectory-confirmed' 仅 β=0.1 的 2 个 seeds。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文 Abstract 现用 'trajectory-confirmed at β=0.1'。R1 仍认为 dose-response 分析基于不均匀 seed 数。维持 warning。\"\n  action_items:\n    - round: 7\n      action: \"Abstract/Intro 中明确区分 'snapshot-observed (all doses)' vs 'trajectory-confirmed (β=0.1 only)'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"验证 Abstract 是否已清晰区分; §4.3 末段 'Non-monotonic dose-response' 弱化为 descriptive pattern\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"统计层级倒置; OR 反转正文一句带过。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N2 / R2 [AGREE]。CMH OR=3.37 方向与 5-seed Fisher 一致但 framing 不诚实。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N1 [critical], R2 [AGREE]。CMH OR=3.37 正文出现 3 次 vs corrected OR=0.61 仅 2 次且靠后。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N1/R2-N2 再次确认 [critical]。论文现有 'suggestive but non-robust' 措辞，但 Table 1 N-H=23%* 仍为 headline。corrected OR=0.61 出现在 §4.3 正文中但视觉上弱于 CMH。两位 reviewer 共识：需以 corrected 分析为 primary baseline，uncorrected 作为 supplementary。\"\n  action_items:\n    - round: 7\n      action: \"(a) Table 1 N-H 列同时展示 uncorrected/corrected; (b) Discussion 以 corrected 为主基调\"\n      assigned_to: \"paper_agent\"\n      status: open\n    - round: 8\n      action: \"强化执行: (a) Abstract 删除或重写 '23% vs 8%' 对比——改为 'descriptively higher but statistically underpowered'; (b) Table 1 caption 必须注明 corrected 3-seed estimate; (c) §4.3 'transient genuine window' 段的 headline 改为 seed-level p=0.26 而非 CMH p<10⁻⁹\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"CMH 检验的 within-seed 非独立性问题——真实独立样本量为 n=5 (seeds) 而非 n=350/414 (samples)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N5 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N2 [critical] 升级。CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N1/R2-N2 [AGREE]。论文已在 experiments.tex:98 承认 CMH 假设违反，但 CMH 仍出现在正文核心段落且数字醒目。Reviewer 共识: CMH 应降级为 appendix supplementary analysis; 正文以 seed-level permutation 为主（承认 power 不足）。\"\n  action_items:\n    - round: 7\n      action: \"正文讨论 within-seed 非独立性及对 CMH p-value 的 inflation 效应\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"(a) CMH OR/p 从 §4.3/§4.6 正文移至 Appendix; (b) 正文仅报告 seed-level permutation test p=0.26 + direction consistent; (c) 明确 'effective sample size is seeds (n=5), not samples'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解释原因。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W6: s43 数据仍用于主文 §4.1 cross-seed claims。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 直接提及。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 直接提及。可能已不影响当前论文版本的核心 claims。\"\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"5-seed pooled N-H=23% 为未校正上限。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议报告区间 [6%, 23%]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"3.7× 差距 (23% uncorrected vs 6.06% corrected)。Table 1 ‡ 标注不够显著。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N2 再次引用。Table 1 ‡ 标注存在但 R2 认为需更醒目。与 v4-R12-N3 高度相关。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 caption 明确说明 'N-H=23% is uncorrected upper bound; corrected estimate on 3 auditable seeds is 6.06%'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"per-seed proved n=18-94，百分比信息量低。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"n=18 (β=0.3 s42) 时 CI 极宽。\"\n    - round: 8\n      reviewers: [1]\n      note: \"R1 detailed comment #5 提到训练 500 样本可能使 hacking 更容易，但未升级为 critical。\"\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 升级为 critical。R1 [REBUT]: 已正确定位为 empirical contribution。Director 降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两位共识: 方法贡献薄，应更明确 position 为 empirical study。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"共识: 不扣重分但确认 novelty ceiling。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 从新角度重提: Goodhart collapse 从 ISR 定义即可预测，方法+发现的新颖性均有限。R1 agree with nuance: empirical 价值在于 calibrating 理论预测。两位维持 Findings 定位。\"\n  action_items:\n    - round: 6\n      action: \"Introduction 中更明确 position 为 empirical study\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据，与主文 5-seed 冲突\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Round 7 未被任何 Reviewer 提及。Appendix Table 5 现含完整 5-seed per-seed data。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议 Table 1 增加 exec-only 3-seed 1000-step 行。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Table 1 已有 exec-only 1000-step 3-seed 行但 500-step 仍为单 seed。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W2 再次引用 Table 1 可读性问题。Table 1 中 exec-only 500-step 仍为 s42 单 seed (†)，R1 detailed comments 指出 3 seeds 产生 3 种不同 failure modes。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 exec-only 500-step 行改为 3-seed pooled 或在 caption 注明原因及 range\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R1 Excitement=3.5 部分不同意。降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N2 再次提出。R1 交叉 [AGREE with nuance]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W3/Q1 再次提出。建议更明确将实验定位为 verification + discovery。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical] 再次提出。R1 [AGREE with nuance]: 可预测部分=方向性崩溃; 有实证价值部分=速度/幅度/模式多样性/bifurcation dynamics。建议将贡献重心从 'discovering collapse' 转移到 'characterizing collapse dynamics'。\"\n  action_items:\n    - round: 6\n      action: \"Framing 从 'we discover Goodhart effects' 转为 'Goodhart collapse is predictable, but these phenomena are not: [...]'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~15 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N3 再次提出。R1 [AGREE]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-W2 再次确认。手动计数 11 个数值/统计量 in 4 sentences。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W1 再次确认，R1 [AGREE]。Abstract 仍含 ~10 个具体数字（97±2%, 99.5%, 92%, ISR≥0.5, β=0.1, 23% vs 8%, nine modes 等）。建议减至 4-5 个关键数字。\"\n  action_items:\n    - round: 7\n      action: \"Abstract 删减至 ≤6 关键数字\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 \\\\paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 \\\\paragraph{} 小标题切割连贯叙事。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [REBUT] 认为结构清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 [AGREE]: 建议合并 'ISR as diagnostic'+'ISR as reward' 为 'Key findings'。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被直接提及。\"\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复且顺序非升序\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Low-dose/Micro-dose/Medium-dose/High-dose 四段格式高度重复。\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W2: β 呈现顺序 0.1→0.05→0.2→0.3。R1 [AGREE]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议开头加总结性发现，然后按升序呈现。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被直接提及。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 开头加 1-2 句 dose-response 总结; 按升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"100-step RL (PR=32%) 部分缓解但不完全。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"C1 'localizing the failure to RL' 证据链有 PR confound。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"论文 framing 已 cautious ('consistent with', 'plausible but not conclusive')。维持 warning。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W2/R2-W4 再次确认。R2 补充新角度: SFT 使用 gold formalizations (看到标准答案) vs GRPO 使用 self-generated rollouts，混淆了算法和标签质量两个因素。论文未讨论此 confound。R1 detailed comments: '更公平的对比是 GRPO + gold-based reward vs GRPO + exec-only reward'。\"\n  action_items:\n    - round: 7\n      action: \"C1 进一步降低 prominence\"\n      assigned_to: \"paper_agent\"\n      status: open\n    - round: 8\n      action: \"正文 §4.2 SFT 段增加 1 句讨论 gold-label confound: SFT 低 hacking 可能部分归因于 gold labels 本身 non-hacking\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Krakovna, Polu & Sutskever, Everitt。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"已加入。R2 新建议: Amodei et al. 2016, Geirhos et al. 2020, DeepSeek-R1 2025。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 建议增加 Goodhart 1975 原文。R1 [AGREE]。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Goodhart 1975 已加入 (references.bib:377-385)。R1 新建议: Ng et al. 1999 (reward shaping classics), semantic faithfulness metrics。R2 建议 Kim et al. (2026) 差异化应加强（2-3 句 explicit comparison）。R1 rebuts LeanDojo/ReProver 建议（不同系统）。\"\n  action_items:\n    - round: 8\n      action: \"(a) 考虑增加 Ng et al. 1999 reward shaping 引用; (b) Related Work 中与 Kim et al. (2026) 的差异化扩展到 2-3 句\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"caption ~120 words + 6 脚注标记。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议 † 和 †† 解释移正文/Appendix，caption 仅保留 ‡ 和 *。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W2 提出拆分 Table 1 为两张表（primary 和 cross-scale）。R1 [AGREE]。\"\n  action_items:\n    - round: 8\n      action: \"拆分 Table 1: primary conditions 一张表 + 1.7B cross-scale 单独成表或移 Appendix\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex:20 现已指定 'primarily regressional, with extremal elements'。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"experiments.tex:91-94 现已包含 reward landscape 分析。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致: Abstract 'Irreducible Solver Rate' vs Method 'Intensional Structural Reward'\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"全文统一使用 Irreducible Solver Rate。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"ISR 统一为 'Irreducible Solver Rate'（不含 'Reward'）。\"\n  resolution_round: 7\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 基于 4 个 β 值、不均匀 seed 数，统计上不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"β=0.1 用 5 seeds 而 β=0.05/0.2/0.3 用 3 seeds。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议弱化为 descriptive pattern。\"\n    - round: 8\n      reviewers: [1]\n      note: \"R1 detailed comment #7: 'dose-response 的表述过强'。若只有 4 个 dose points + 不均匀 seeds，不足以支撑 dose-response claim。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 'Non-monotonic dose-response' 弱化为 descriptive pattern\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 Goodhart Effects 的 β 值呈现顺序非升序 (0.1→0.05→0.2→0.3)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"升序呈现 + 最后 cross-dose synthesis 会更清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"与 v5-R2-W4 合并处理。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n  action_items:\n    - round: 7\n      action: \"与 v5-R2-W4 合并: 按 β 升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"introduction.tex:14 现为 'component necessity testing (leave-one-out (LOO) ablation on solver inputs)'。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled，部分 mode 为单点观察\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 [REBUT]。Director 裁决: 降级为 info。\"\n    - round: 7\n      reviewers: [1]\n      note: \"R1-Q6 提及但未列为 weakness。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W3 再次提出。Taxonomy 多数模式为 single-seed 观察，'taxonomy' 暗示系统性过强。建议区分 'robust modes' (H1/H7/H8, 多 seed) vs 'observed but isolated modes'。同意论文用 deterministic classifiers + functional analysis 无需 IAA，但 recall 未知。\"\n  action_items:\n    - round: 8\n      action: \"Table 2 或正文中区分 'robust modes (multi-seed replicated)' vs 'isolated observations (single-seed)'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v7-R1-N2\"\n  summary: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate，需 cluster-robust 重分析\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 提出 [critical], R2 [AGREE]。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N1/R2-N2 [AGREE]。与 v4-R1-N4 合并。论文已承认问题但未采取行动修改呈现架构。\"\n  action_items:\n    - round: 8\n      action: \"合并到 v4-R1-N4 修复方案执行\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v7-R2-MR1\"\n  summary: \"缺少 Goodhart's Law 经典引用 (Goodhart 1975)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"references.bib:377-385 现已包含 Goodhart 1975。related_work.tex:15 引用。\"\n  resolution_round: 8\n\n- id: \"v7-R2-W7\"\n  summary: \"experiments.tex:34 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"单处出现。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。experiments.tex:34 的 'Notably' 在当前版本中不存在（可能行号变化），需确认。\"\n  action_items:\n    - round: 7\n      action: \"删除 'Notably'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== Round 8 新 issues =====\n\n- id: \"v8-R12-N1\"\n  summary: \"核心 Goodhart 发现的可预测性：ISR≥0.5 for tautologies 从定义即可推导，限制了概念新颖性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]: 论文自己在 §3.2 承认 'by construction'。R1 [AGREE with nuance]: 方向可预测但速度/幅度/模式多样性不可预测。共识: 贡献重心应从 'discovering collapse' 转移到 'characterizing collapse dynamics'。当前 Abstract/Contributions 对 ISR-as-reward 崩溃的 framing 过重。\"\n  action_items:\n    - round: 8\n      action: \"(a) Abstract 和 Contributions 中将 ISR-as-reward Goodhart 崩溃定位为 'empirical characterization of a predictable failure' 而非 'discovery'; (b) 突出真正不可预测的贡献: stochastic bifurcation, non-monotonic dose interaction, mode diversity; (c) Discussion 增加 1-2 句: 'the direction of collapse is predictable from ISR's definition; our contribution is the empirical characterization of how collapse manifests'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-N3\"\n  summary: \"'Genuine'/'non-hacking'/'structurally sound' 术语交替使用导致语义滑移\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N3 [critical], R2 [AGREE]。Abstract 'structurally sound' 未定义; 正文 'genuine' 多处出现; Table 1 用 'N-H%'。三个词语义强度不同: 'genuine' 暗示真正正确, 'non-hacking' 仅为残差分类。建议统一为 'non-hacking' + 首次使用时定义操作含义。\"\n  action_items:\n    - round: 8\n      action: \"(a) 全文统一使用 'non-hacking'; (b) Abstract 'structurally sound' 改为 'non-hacking'; (c) Introduction 首次使用时 parenthetical 定义 '(not matching any of nine cataloged hacking patterns; a necessary but not sufficient condition for semantic correctness)'; (d) 正文中消除 'genuine proof' 用法，改为 'non-hacking output'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R12-N2\"\n  summary: \"实验范围 (Qwen3 + FOLIO) 与标题/claim scope ('Neurosymbolic Proof Generation') 不匹配\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N3 [critical], R1 [AGREE]。标题 'Neurosymbolic Proof Generation' 暗示一般性发现，但证据仅来自 Qwen3-4B/1.7B + FOLIO。FOLIO 仅 1400 样本、FOL 前提短。未测试其他模型架构 (Llama, Mistral) 或其他 FOL 数据集 (ProntoQA, RuleTaker)。1.7B 仅 1 seed。建议: 增加实验或收窄标题/claim scope。\"\n  action_items:\n    - round: 8\n      action: \"(a) 若无法在 deadline 前增加实验，将标题改为更具体的 scope (如 'Reward Hacking in GRPO-Trained Formalizers'); (b) Introduction 和 Contributions 中明确限定 claim scope 为 Qwen3 + FOLIO; (c) Limitations 中更突出地讨论泛化性问题并列出具体的 generalization tests (不同架构、不同数据集) 作为 future work\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-W4\"\n  summary: \"多重比较未校正 (Fisher exact tests across 6+ comparisons)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W4 提出。R2 [AGREE] 但认为实际影响有限: seed-level tests 已 p≥0.26，校正后更不显著; 核心 claims 更多依赖 descriptive patterns。形式规范问题。\"\n  action_items:\n    - round: 8\n      action: \"Appendix Table A2 增加 Bonferroni-corrected p 值列，或正文脚注讨论多重比较\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-MR\"\n  summary: \"缺少 reward shaping 经典引用 (Ng et al. 1999) 和 Kim et al. (2026) explicit comparison\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 建议增加 Ng et al. 1999 'Policy invariance under reward transformations'。R1/R2 共识: 与 Kim et al. (2026) 的差异化需加强——Kim 研究 inference-time gaming, 本文研究 training-time gaming emergence, 这是重要区别但 Related Work 仅用一个 citation 带过。R1 rebuts LeanDojo/ReProver 建议（系统类型不同）。\"\n  action_items:\n    - round: 8\n      action: \"(a) Related Work 增加 Ng et al. 1999 引用 (reward shaping 理论基础); (b) 与 Kim et al. (2026) 的差异化扩展为 2-3 句 explicit comparison (inference-time vs training-time gaming)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-17T18:24:23.659069+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 32928}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-17T18:26:10.686063+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 8 审稿报告\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+写作质量+完整性+Related Work）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，对已证明的 neurosymbolic formalization 执行 leave-one-out (LOO) 组件必要性测试，导出 Irreducible Solver Rate (ISR) 指标。核心发现：(1) GRPO exec-only 训练下，prove rate 收敛至 97±2% 但 ISR 崩溃 99.5%（Figure 2），揭示结构退化不可见于执行评估；(2) ISR 用作 reward 时在四个 β 值上均出现 Goodhart 崩溃（trajectory-confirmed at β=0.1）；(3) 效果跨 FOL/Prolog 两种逻辑和 4B/1.7B 两种模型规模一致；(4) 九种 hacking 模式的分类系统。实验使用 Qwen3-4B/1.7B + FOLIO 数据集。\n\n---\n\n## Strengths\n\n1. **研究问题重要且及时**：execution-based reward 在 neurosymbolic RL 中的 structural blind spot 是真实且 understudied 的问题。随着 GRPO/RLVR 广泛使用，此类诊断的需求在增长。[R1/R2 共识]\n\n2. **ISR 崩溃轨迹（Figure 2）视觉证据有力**：PR 32%→93%→96% 同时 ISR 0.642→0.132→0.003 的 214× 崩溃，直观且令人信服地展示了 \"execution correctness ≠ structural quality\"。即使不依赖统计推断，这一描述性发现本身有说服力。[R1/R2 共识]\n\n3. **统计诚实度罕见**：论文主动否定了自己的 CMH test（指出独立性假设违反），报告 seed-level permutation test 的 underpowered 结果（p=0.26），承认 corrected analysis 下效果方向反转（OR=0.61, n.s.）。这种 self-critical 态度在 ML 论文中不常见。[R1/R2 共识]\n\n4. **STA/ISR 设计简洁、model-agnostic**：LOO ablation 不依赖特定模型或 ground-truth labels，Algorithm 1 清晰可复现，具有实际部署价值。[R1]\n\n5. **Trajectory analysis > snapshot evaluation 方法论贡献**：500-step genuine window 在 1000-step 关闭的发现，方法论上有普适价值（\"评估必须考虑时间维度\"）。[R2]\n\n6. **实验设计（matched controls）**：random reward 控制隔离 ISR-specific signal，SFT baseline 隔离 RL-specific effect，cross-logic 和 cross-scale transfer 增加证据广度。高于平均水平的实验方法论。[R1/R2 共识]\n\n7. **写作质量整体良好**：主线叙事连贯，AI 写作痕迹极少，专有名词均有定义。[R2]\n\n---\n\n## Weaknesses（严格评估）\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, R1/R2 共识] **核心 Goodhart 发现的可预测性限制了概念新颖性**\n论文在 §3.2 已承认 ISR≥0.5 for tautological proofs \"by construction\"，§3.3 指出 \"Goodhart effects we document would likely transfer to Shapley-based metrics\"。既然作者自己承认这个漏洞从定义即可预测，那\"在四个 dose 都观察到崩溃\"主要是对已知数学属性的实验验证，而非概念突破。论文试图用 stochastic bifurcation 和 non-monotonic dose-response 补充新颖性，但这些关于 *how*（而非 *whether*）的细节在当前 framing 中不够突出。贡献重心应从 \"discovering Goodhart collapse\" 转移到 \"characterizing collapse dynamics\"。\n\n**N2** [critical, R1/R2 共识] **统计推断基础存在系统性问题**\n(a) CMH 检验 p<10⁻⁹ 的独立性假设被论文自己否定（experiments.tex:98），但 CMH 仍出现在正文核心段落且数字醒目；\n(b) Seed-level permutation test p=0.26（n=5），真实统计证据不显著；\n(c) H8+FN corrected 的 3-seed 分析下方向反转（OR=0.61, n.s.）；\n(d) Table 1 和 Abstract 的\"23% vs 8%\"对比容易误导读者认为 ISR 有正面效果。\n论文的信息架构问题：核心 claims 在 Abstract/Table 1 高可见度位置，caveats 藏在 §C/§6 低可见度位置。CMH 应降级为 appendix supplementary，正文以 seed-level analysis 为主。\n\n**N3** [critical, R1/R2 共识] **实验范围（Qwen3 + FOLIO）与 claim scope 不匹配**\n标题 \"Neurosymbolic Proof Generation\" 暗示一般性发现，但证据仅来自 Qwen3-4B/1.7B + FOLIO（500 训练/100 评估样本）。未测试其他模型架构（Llama, Mistral）或其他 FOL 数据集。1.7B 仅 1 seed。FOLIO 的特定特征（短前提、受限领域）可能使 hacking 模式不可泛化。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, R1/R2 共识] **\"Genuine\"/\"non-hacking\"/\"structurally sound\" 术语交替使用**\nAbstract 用 \"structurally sound\"（未定义），正文用 \"genuine\"（暗示语义正确），Table 1 用 \"N-H%\"（操作定义为残差分类）。三个词语义强度不同，造成 claim 强度的语义滑移。应统一为 \"non-hacking\" 并明确操作定义。\n\n**W2** [warning, R1/R2 共识] **Abstract 信息过载**\n~10 个具体数字在 4 句话中（97±2%, 99.5%, 92%, ISR≥0.5, β=0.1, 23% vs 8%, nine modes 等），审稿人 30 秒内无法抓住核心 story。建议减至 4-5 个关键数字。\n\n**W3** [warning, R1/R2 共识] **Table 1 可读性差**\n9 个 condition + 6 列 + 4 个脚注符号 + 1.7B cross-scale 混入同一表，需反复跳转脚注。建议拆分为 primary conditions 表 + cross-scale 单独成表。\n\n**W4** [warning, R1/R2 共识] **Hacking taxonomy 部分过度拟合单一实验设置**\n九种模式中，Repetition collapse、Contradiction explosion、Query-as-fact、H9、Complexity-without-utility 均为单 seed/单 condition 观察。\"Taxonomy\" 暗示系统性和可复现性过强。建议区分 \"robust modes\"（H1/H7/H8, 多 seed 复现）和 \"observed but isolated modes\"。\n\n**W5** [warning, R1/R2 共识] **SFT baseline 比较存在双重 confound**\n(a) PR 差距 80+ pp（SFT 13% vs GRPO 93-97%）；(b) SFT 使用 gold formalizations（标签质量 confound），GRPO 使用 self-generated rollouts。将差异归因于 \"RL-specific\" 在当前证据下过强，尽管论文已用 \"consistent with\" 措辞和 100-step partial control 部分缓解。\n\n**W6** [warning, R1/R2 共识] **Premise-count confound 对 ISR-vs-Random 比较的影响**\nPremise-count-matched 后 ISR 差异仅 1.06×（Appendix §C），说明 ISR reward 的\"优势\"主要来自长度偏差。注意：R2 的 partial rebut 成立——premise-count confound 不影响 ISR 的诊断功能（exec-only 崩溃轨迹 214× 远超长度效应），仅影响 ISR-vs-Random 的比较性 claims。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| 统计推断基础（CMH/permutation） | N1 [critical] | N2 [critical] | [AGREE] 完全一致 |\n| 实验范围过窄 | W1 [warning] | N3 [critical] | [AGREE] 完全一致 |\n| 新颖性定位不足 | AGREE with nuance | N1 [critical] | [AGREE] R1 同意方向但保留 calibration value |\n| SFT confound | W2 [warning] | W4 [warning] | [AGREE] 完全一致 |\n| Taxonomy 过拟合 | W3 [warning] | W3 [warning] | [AGREE] 完全一致 |\n| 术语不一致 | N3 [critical] | AGREE | [AGREE] 完全一致 |\n| Abstract 过载 | AGREE | W1 [warning] | [AGREE] 完全一致 |\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 解析 |\n|------|----|----|------|\n| Premise-count confound 范围 | N2: \"瓦解 C1 和 C2\" | REBUT: \"仅影响 reward 比较，不影响诊断\" | R2 反驳有效——ISR 诊断功能在 exec-only 崩溃轨迹中成立 |\n| Cross-scale (§4.5) 定性 | N4: \"反驳 ISR-as-reward\" | REBUT: \"论文未 claim 有效\" | R2 反驳有效——论文已定位为 preliminary，意图展示 mode diversity |\n| LeanDojo/ReProver 引用 | --- | W5: 需加入 | R1 REBUT: 不同系统类型 | R1 反驳有效——ITP vs NL→FOL 是不同 pipeline |\n\n---\n\n## Questions for Authors\n\n1. 如果 ISR≥0.5 for tautologies 从定义即可预测，论文的核心实证贡献是什么？是否应将 Contribution 重心从 C2 (Goodhart collapse) 转移到 C1 (diagnostic) 和 C4 (taxonomy)?\n\n2. 是否考虑将 CMH 结果移至 Appendix、正文仅报告 seed-level permutation test（承认 power 不足但 direction consistent）?\n\n3. 论文标题是否应缩窄为与实验范围匹配的 scope（如 \"Reward Hacking in GRPO-Trained FOL Formalizers\"）?\n\n4. \"Non-hacking\" 的操作定义为残差（不匹配九种 pattern），但 Prolog seed 44 的 query-as-fact gaming 证明 strict classifier 可能漏检。FOL 条件下的 non-hacking 率是否也被高估?\n\n5. 是否可以在 deadline 前增加至少一个不同架构的模型（如 Llama-3.1-8B）的 pilot experiment?\n\n---\n\n## Missing References\n\n1. **Ng et al., 1999** \"Policy invariance under reward transformations: Theory and application to reward shaping\" — ISR reward 本质是 reward shaping，缺少经典理论基础引用。[R1]\n2. **Kim et al. (2026) explicit comparison** — 当前 Related Work 仅一个 citation 带过，应扩展为 2-3 句 explicit comparison（inference-time gaming vs training-time gaming emergence）。[R1/R2 共识]\n3. LeanDojo/ReProver — R1 反驳有效（不同系统类型），不需要加入。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：已请求，截至报告撰写时状态为 pending。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 (Findings)\n**置信度**: 4/5\n\n**理由**：\n\n这是一篇方法论严谨、统计报告极度诚实的实证论文。ISR 崩溃轨迹（Figure 2）作为描述性发现具有真实价值，\"diagnostic ≠ optimizer\" 的实证警示对 neurosymbolic RL 从业者有参考意义。\n\n但以下因素将其限制在 Findings 而非主会议：\n\n1. **概念新颖性有限**：核心 Goodhart 崩溃从 ISR 定义即可预测（ISR≥0.5 by construction），论文的贡献更多是 calibration（验证已知理论预测）而非 discovery。\n2. **统计推断不充分**：核心比较（23% vs 8%）在 seed-level 无统计支撑（p=0.26），corrected 分析下方向反转。论文的诚实披露值得肯定，但不能替代方法层面的修复。\n3. **实验范围过窄**：单一模型族 + 单一数据集 vs 标题的泛化暗示。\n\n建议作为 **Findings** 接收，条件是修复：\n- N1（novelty framing 调整）\n- N2（统计呈现架构重组：CMH 降级，seed-level 为主）\n- 术语统一（W1）\n\n---\n\n## Detailed Comments\n\n### 关于 ISR 诊断功能 vs ISR-as-reward 的区分\n\n论文的最大贡献在 ISR 作为诊断工具揭示 exec-only blind spot（C1 的前半部分），而非 ISR 作为 reward 的效果（C2）。建议在修改中更明确这一区分：ISR 的诊断功能不受 premise-count confound 影响（214× 崩溃远超长度效应），但 ISR-as-reward 的任何比较性 claim 都受 confound 影响。\n\n### 关于 Trajectory Analysis 的方法论贡献\n\n\"Snapshot evaluation can overestimate structural rewards' benefit; only trajectory analysis reveals the transient nature\" 这一方法论 insight 比具体的 ISR 数字更有普适价值。建议在 Contributions 中更突出这一点。\n\n### 关于 ARR Responsible NLP Checklist\n\n论文中未见 ARR Responsible NLP Checklist（通常通过 OpenReview 单独提交）。建议确认已准备。",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)"
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
    "report": "# Round 8 审稿报告\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+写作质量+完整性+Related Work）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，对已证明的 neurosymbolic formalization 执行 leave-one-out (LOO) 组件必要性测试，导出 Irreducible Solver Rate (ISR) 指标。核心发现：(1) GRPO exec-only 训练下，prove rate 收敛至 97±2% 但 ISR 崩溃 99.5%（Figure 2），揭示结构退化不可见于执行评估；(2) ISR 用作 reward 时在四个 β 值上均出现 Goodhart 崩溃（trajectory-confirmed at β=0.1）；(3) 效果跨 FOL/Prolog 两种逻辑和 4B/1.7B 两种模型规模一致；(4) 九种 hacking 模式的分类系统。实验使用 Qwen3-4B/1.7B + FOLIO 数据集。\n\n---\n\n## Strengths\n\n1. **研究问题重要且及时**：execution-based reward 在 neurosymbolic RL 中的 structural blind spot 是真实且 understudied 的问题。随着 GRPO/RLVR 广泛使用，此类诊断的需求在增长。[R1/R2 共识]\n\n2. **ISR 崩溃轨迹（Figure 2）视觉证据有力**：PR 32%→93%→96% 同时 ISR 0.642→0.132→0.003 的 214× 崩溃，直观且令人信服地展示了 \"execution correctness ≠ structural quality\"。即使不依赖统计推断，这一描述性发现本身有说服力。[R1/R2 共识]\n\n3. **统计诚实度罕见**：论文主动否定了自己的 CMH test（指出独立性假设违反），报告 seed-level permutation test 的 underpowered 结果（p=0.26），承认 corrected analysis 下效果方向反转（OR=0.61, n.s.）。这种 self-critical 态度在 ML 论文中不常见。[R1/R2 共识]\n\n4. **STA/ISR 设计简洁、model-agnostic**：LOO ablation 不依赖特定模型或 ground-truth labels，Algorithm 1 清晰可复现，具有实际部署价值。[R1]\n\n5. **Trajectory analysis > snapshot evaluation 方法论贡献**：500-step genuine window 在 1000-step 关闭的发现，方法论上有普适价值（\"评估必须考虑时间维度\"）。[R2]\n\n6. **实验设计（matched controls）**：random reward 控制隔离 ISR-specific signal，SFT baseline 隔离 RL-specific effect，cross-logic 和 cross-scale transfer 增加证据广度。高于平均水平的实验方法论。[R1/R2 共识]\n\n7. **写作质量整体良好**：主线叙事连贯，AI 写作痕迹极少，专有名词均有定义。[R2]\n\n---\n\n## Weaknesses（严格评估）\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, R1/R2 共识] **核心 Goodhart 发现的可预测性限制了概念新颖性**\n论文在 §3.2 已承认 ISR≥0.5 for tautological proofs \"by construction\"，§3.3 指出 \"Goodhart effects we document would likely transfer to Shapley-based metrics\"。既然作者自己承认这个漏洞从定义即可预测，那\"在四个 dose 都观察到崩溃\"主要是对已知数学属性的实验验证，而非概念突破。论文试图用 stochastic bifurcation 和 non-monotonic dose-response 补充新颖性，但这些关于 *how*（而非 *whether*）的细节在当前 framing 中不够突出。贡献重心应从 \"discovering Goodhart collapse\" 转移到 \"characterizing collapse dynamics\"。\n\n**N2** [critical, R1/R2 共识] **统计推断基础存在系统性问题**\n(a) CMH 检验 p<10⁻⁹ 的独立性假设被论文自己否定（experiments.tex:98），但 CMH 仍出现在正文核心段落且数字醒目；\n(b) Seed-level permutation test p=0.26（n=5），真实统计证据不显著；\n(c) H8+FN corrected 的 3-seed 分析下方向反转（OR=0.61, n.s.）；\n(d) Table 1 和 Abstract 的\"23% vs 8%\"对比容易误导读者认为 ISR 有正面效果。\n论文的信息架构问题：核心 claims 在 Abstract/Table 1 高可见度位置，caveats 藏在 §C/§6 低可见度位置。CMH 应降级为 appendix supplementary，正文以 seed-level analysis 为主。\n\n**N3** [critical, R1/R2 共识] **实验范围（Qwen3 + FOLIO）与 claim scope 不匹配**\n标题 \"Neurosymbolic Proof Generation\" 暗示一般性发现，但证据仅来自 Qwen3-4B/1.7B + FOLIO（500 训练/100 评估样本）。未测试其他模型架构（Llama, Mistral）或其他 FOL 数据集。1.7B 仅 1 seed。FOLIO 的特定特征（短前提、受限领域）可能使 hacking 模式不可泛化。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, R1/R2 共识] **\"Genuine\"/\"non-hacking\"/\"structurally sound\" 术语交替使用**\nAbstract 用 \"structurally sound\"（未定义），正文用 \"genuine\"（暗示语义正确），Table 1 用 \"N-H%\"（操作定义为残差分类）。三个词语义强度不同，造成 claim 强度的语义滑移。应统一为 \"non-hacking\" 并明确操作定义。\n\n**W2** [warning, R1/R2 共识] **Abstract 信息过载**\n~10 个具体数字在 4 句话中（97±2%, 99.5%, 92%, ISR≥0.5, β=0.1, 23% vs 8%, nine modes 等），审稿人 30 秒内无法抓住核心 story。建议减至 4-5 个关键数字。\n\n**W3** [warning, R1/R2 共识] **Table 1 可读性差**\n9 个 condition + 6 列 + 4 个脚注符号 + 1.7B cross-scale 混入同一表，需反复跳转脚注。建议拆分为 primary conditions 表 + cross-scale 单独成表。\n\n**W4** [warning, R1/R2 共识] **Hacking taxonomy 部分过度拟合单一实验设置**\n九种模式中，Repetition collapse、Contradiction explosion、Query-as-fact、H9、Complexity-without-utility 均为单 seed/单 condition 观察。\"Taxonomy\" 暗示系统性和可复现性过强。建议区分 \"robust modes\"（H1/H7/H8, 多 seed 复现）和 \"observed but isolated modes\"。\n\n**W5** [warning, R1/R2 共识] **SFT baseline 比较存在双重 confound**\n(a) PR 差距 80+ pp（SFT 13% vs GRPO 93-97%）；(b) SFT 使用 gold formalizations（标签质量 confound），GRPO 使用 self-generated rollouts。将差异归因于 \"RL-specific\" 在当前证据下过强，尽管论文已用 \"consistent with\" 措辞和 100-step partial control 部分缓解。\n\n**W6** [warning, R1/R2 共识] **Premise-count confound 对 ISR-vs-Random 比较的影响**\nPremise-count-matched 后 ISR 差异仅 1.06×（Appendix §C），说明 ISR reward 的\"优势\"主要来自长度偏差。注意：R2 的 partial rebut 成立——premise-count confound 不影响 ISR 的诊断功能（exec-only 崩溃轨迹 214× 远超长度效应），仅影响 ISR-vs-Random 的比较性 claims。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| 统计推断基础（CMH/permutation） | N1 [critical] | N2 [critical] | [AGREE] 完全一致 |\n| 实验范围过窄 | W1 [warning] | N3 [critical] | [AGREE] 完全一致 |\n| 新颖性定位不足 | AGREE with nuance | N1 [critical] | [AGREE] R1 同意方向但保留 calibration value |\n| SFT confound | W2 [warning] | W4 [warning] | [AGREE] 完全一致 |\n| Taxonomy 过拟合 | W3 [warning] | W3 [warning] | [AGREE] 完全一致 |\n| 术语不一致 | N3 [critical] | AGREE | [AGREE] 完全一致 |\n| Abstract 过载 | AGREE | W1 [warning] | [AGREE] 完全一致 |\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 解析 |\n|------|----|----|------|\n| Premise-count confound 范围 | N2: \"瓦解 C1 和 C2\" | REBUT: \"仅影响 reward 比较，不影响诊断\" | R2 反驳有效——ISR 诊断功能在 exec-only 崩溃轨迹中成立 |\n| Cross-scale (§4.5) 定性 | N4: \"反驳 ISR-as-reward\" | REBUT: \"论文未 claim 有效\" | R2 反驳有效——论文已定位为 preliminary，意图展示 mode diversity |\n| LeanDojo/ReProver 引用 | --- | W5: 需加入 | R1 REBUT: 不同系统类型 | R1 反驳有效——ITP vs NL→FOL 是不同 pipeline |\n\n---\n\n## Questions for Authors\n\n1. 如果 ISR≥0.5 for tautologies 从定义即可预测，论文的核心实证贡献是什么？是否应将 Contribution 重心从 C2 (Goodhart collapse) 转移到 C1 (diagnostic) 和 C4 (taxonomy)?\n\n2. 是否考虑将 CMH 结果移至 Appendix、正文仅报告 seed-level permutation test（承认 power 不足但 direction consistent）?\n\n3. 论文标题是否应缩窄为与实验范围匹配的 scope（如 \"Reward Hacking in GRPO-Trained FOL Formalizers\"）?\n\n4. \"Non-hacking\" 的操作定义为残差（不匹配九种 pattern），但 Prolog seed 44 的 query-as-fact gaming 证明 strict classifier 可能漏检。FOL 条件下的 non-hacking 率是否也被高估?\n\n5. 是否可以在 deadline 前增加至少一个不同架构的模型（如 Llama-3.1-8B）的 pilot experiment?\n\n---\n\n## Missing References\n\n1. **Ng et al., 1999** \"Policy invariance under reward transformations: Theory and application to reward shaping\" — ISR reward 本质是 reward shaping，缺少经典理论基础引用。[R1]\n2. **Kim et al. (2026) explicit comparison** — 当前 Related Work 仅一个 citation 带过，应扩展为 2-3 句 explicit comparison（inference-time gaming vs training-time gaming emergence）。[R1/R2 共识]\n3. LeanDojo/ReProver — R1 反驳有效（不同系统类型），不需要加入。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：已请求，截至报告撰写时状态为 pending。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 (Findings)\n**置信度**: 4/5\n\n**理由**：\n\n这是一篇方法论严谨、统计报告极度诚实的实证论文。ISR 崩溃轨迹（Figure 2）作为描述性发现具有真实价值，\"diagnostic ≠ optimizer\" 的实证警示对 neurosymbolic RL 从业者有参考意义。\n\n但以下因素将其限制在 Findings 而非主会议：\n\n1. **概念新颖性有限**：核心 Goodhart 崩溃从 ISR 定义即可预测（ISR≥0.5 by construction），论文的贡献更多是 calibration（验证已知理论预测）而非 discovery。\n2. **统计推断不充分**：核心比较（23% vs 8%）在 seed-level 无统计支撑（p=0.26），corrected 分析下方向反转。论文的诚实披露值得肯定，但不能替代方法层面的修复。\n3. **实验范围过窄**：单一模型族 + 单一数据集 vs 标题的泛化暗示。\n\n建议作为 **Findings** 接收，条件是修复：\n- N1（novelty framing 调整）\n- N2（统计呈现架构重组：CMH 降级，seed-level 为主）\n- 术语统一（W1）\n\n---\n\n## Detailed Comments\n\n### 关于 ISR 诊断功能 vs ISR-as-reward 的区分\n\n论文的最大贡献在 ISR 作为诊断工具揭示 exec-only blind spot（C1 的前半部分），而非 ISR 作为 reward 的效果（C2）。建议在修改中更明确这一区分：ISR 的诊断功能不受 premise-count confound 影响（214× 崩溃远超长度效应），但 ISR-as-reward 的任何比较性 claim 都受 confound 影响。\n\n### 关于 Trajectory Analysis 的方法论贡献\n\n\"Snapshot evaluation can overestimate structural rewards' benefit; only trajectory analysis reveals the transient nature\" 这一方法论 insight 比具体的 ISR 数字更有普适价值。建议在 Contributions 中更突出这一点。\n\n### 关于 ARR Responsible NLP Checklist\n\n论文中未见 ARR Responsible NLP Checklist（通常通过 OpenReview 单独提交）。建议确认已准备。",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-17T18:26:14.501219+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 694 · 2026-05-17T18:26:26.707524+00:00_

## 审稿完成

**Round 8 审稿报告已投递至 Research Director。**

**评分**: 3.0 (Findings)

**核心判断**：

| 维度 | 评分 | 摘要 |
|------|------|------|
| Overall | 3.0 | Findings 级别 |
| Soundness | 3-3.5 | 方法合理但统计推断有结构性问题 |
| Excitement | 2.5-3 | 有用的实证记录但核心发现可预测 |
| Reproducibility | 4 | 超参详尽，承诺开源 |

**3 个 Must-Fix 共识**：
1. **N1** 新颖性定位：Goodhart 崩溃从 ISR 定义可预测，贡献重心应转向 collapse dynamics characterization
2. **N2** 统计呈现架构：CMH 应降级至 appendix，正文以 seed-level permutation 为主；"23% vs 8%" 需降级为 underpowered descriptive comparison
3. **N3** 实验范围 vs claim scope 不匹配：标题/claims 需收窄或增加实验

**持续 in_progress issues（跨 Round 4-8 未完全修复）**：统计呈现架构、OR 反转 framing、Table 1 可读性、Abstract 数据堆砌、β 呈现顺序、SFT confound 讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 67

## Round 67

2 recorded events


### User

_source line 695 · 2026-05-17T18:26:29.244015+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

**汇总**：

| R2 问题 | 我的判断 | 理由 |
|--------|--------|------|
| N1 新颖性不足 | AGREE (with nuance) | 崩溃方向可预测，但动力学细节仍有实证价值；Contributions 中 ISR-as-reward 的 framing 过重 |
| N2 统计效力不足 | AGREE | 与我的 N1 高度一致；补充了 H8+FN 校正后方向反转和信息架构问题 |
| N3 实验范围窄 | AGREE | 与我的 W1 一致；标题泛化程度与实验范围不匹配 |
| W1 Abstract 过载 | AGREE | 概念和数字密度过高 |
| W2 Table 1 可读性 | AGREE | 建议拆分+简化脚注 |
| W3 Taxonomy 过拟合 | AGREE | 与我的 W3 一致 |
| W4 SFT confound | AGREE | 与我的 W2 一致；补充了 PR 差距导致归因困难 |
| W5 缺 LeanDojo 等 | REBUT (partial) | FOL/Prolog solver 与 Lean ITP 是不同 pipeline；但 Kim et al. 差异化确需加强 |

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

_source line 696 · 2026-05-17T18:26:42.411093+00:00_

审稿圆桌会议完成。

**最终结论**：两位 Reviewer 一致评定 **3.0 (Findings)**，交叉回应后无未解决的重大分歧。审稿报告已投递至 Research Director。

**核心问题摘要**：
- 3 个 critical：概念新颖性有限（Goodhart 崩溃可预测）、统计推断基础问题（CMH 独立性违反 + seed-level p=0.26）、实验范围与 claim scope 不匹配
- 6 个 warning：术语不一致、Abstract 过载、Table 1 可读性、Taxonomy 过拟合、SFT confound、premise-count confound 对比较性 claims 的影响

**主要修改建议**（Findings 接收条件）：
1. Novelty framing 调整——从 "discovering collapse" 转向 "characterizing collapse dynamics"
2. 统计呈现架构重组——CMH 降级到 Appendix，seed-level permutation 为正文主统计
3. 术语统一为 "non-hacking"

Issue Tracker 已同步更新（Round 8: 3 new critical issues, 2 new info issues, 12 existing issues 追加 mentions）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 68

## Round 68

68 recorded events


### User

_source line 697 · 2026-05-17T18:51:38.961410+00:00_

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

_source line 698 · 2026-05-17T18:51:45.033193+00:00_

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

_source line 699 · 2026-05-17T18:51:45.084205+00:00_

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

_source line 700 · 2026-05-17T18:51:48.898645+00:00_

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

_source line 701 · 2026-05-17T18:51:48.949214+00:00_

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

_source line 702 · 2026-05-17T18:51:53.870932+00:00_

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

_source line 703 · 2026-05-17T18:51:53.871375+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-17T18:51:58.653029+00:00_

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


### Tool call

_source line 705 · 2026-05-17T18:51:59.106625+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "report.md",
  "max_chars": "6000"
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
    "file": "report.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 706 · 2026-05-17T18:51:59.609228+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (140 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- sweep-random-b01-s46: W4: Random β=0.1 s46 extends random control to 5-seed（排队等待 GPU）\n- sweep-random-b01-s45: W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1（排队等待 GPU）\n- sweep-isr-b005-s42: W3: β=0.05 ISR bonus produces less aggressive hacking than β=0.1/0.3 while retaining structural signal — tests Goodhart's Law dose-response（准备中）\n- w2-qwen3-7b-pilot: Qwen3-8B exec-only 50-step pilot: 测试 8B 模型能否在 96GB GPU 上跑通，确定 per_device_batch_size (4 vs 2)（准备中）\n- plan001-exec-only-s45: Exec-only seed=45, 5-seed baseline for tighter confidence intervals（准备中）\n- sweep-isr-b01-s46: W4: ISR β=0.1 s46 extends to 5-seed for tighter confidence intervals（准备中）\n\n## 近期结论\n- **plan002-additive-b01-s45-1000** (negative): ISR β=0.1 seed=45 genuine window (~55% at 500 steps) will collapse by 1000 steps, consistent with the inevitable collapse pattern observed in s42 (17%→2%). Extended training drives ISR-trained models toward metric gaming regardless of initial genuine rate. ← 基于 plan002-additive-b01-s45\n- **sweep-random-b005-s44** (success): Random β=0.05 seed=44
…[truncated 1873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 956
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-17T18:51:59.609733+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- sweep-random-b01-s46: W4: Random β=0.1 s46 extends random control to 5-seed（排队等待 GPU）\\n- sweep-random-b01-s45: W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1（排队等待 GPU）\\n- sweep-isr-b005-s42: W3: β=0.05 ISR bonus produces less aggressive hacking than β=0.1/0.3 while retaining structural signal — tests Goodhart's Law dose-response（准备中）\\n- w2-qwen3-7b-pilot: Qwen3-8B exec-only 50-step pilot: 测试 8B 模型能否在 96GB GPU 上跑通，确定 per_device_batch_size (4 vs 2)（准备中）\\n- plan001-exec-only-s45: Exec-only seed=45, 5-seed baseline for tighter confidence intervals（准备中）\\n- sweep-isr-b01-s46: W4: ISR β=0.1 s46 extends to 5-seed for tighter confidence intervals（准备中）\\n\\n## 近期结论\\n- **plan002-additive-b01-s45-1000** (negative): ISR β=0.1 seed=45 genuine window (~55% at 500 steps) will collapse by 1000 steps, consistent with the inevitable collapse pattern observed in s42 (17%→2%). Extended training drives ISR-trained models toward metric gaming regardless of initial genuine rate. ← 基于 plan002-additive-b01-s45\\n- **sweep-random-b005-s44** (success): Random β=0.05 seed=44: 3rd seed for balanced 3v3 comparison with ISR β=0.05, variance estimation\\n- **sweep-random-b005-s43** (success): Random β=0.05 seed=43: 2nd seed matched control for ISR β=0.05, replication for variance estimation\\n\\n## 趋势\\n成功 44 / 负向 35 / 失败 45 / 共 134\\ngenuine_rate: 0 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败
…[truncated 2313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-17T18:51:59.609988+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 709 · 2026-05-17T18:51:59.660366+00:00_



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

_source line 710 · 2026-05-17T18:52:05.209015+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
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
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 711 · 2026-05-17T18:52:06.163287+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit template",
  "allowed_domains": "['aclweb.org', 'aclrollingreview.org']"
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
    "query": "ACL Rolling Review 2026 author guidelines page limit template",
    "allowed_domains": "['aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-17T18:52:06.817457+00:00_

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

_source line 713 · 2026-05-17T18:52:06.868072+00:00_

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

_source line 714 · 2026-05-17T18:52:12.742273+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit template"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Author Guidelines - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Author_Guidelines"}]

Based on the search results, I found information about ACL Rolling Review 2026 author guidelines regarding page limits and formatting:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). Additionally, final versions of accepted papers will be given one addit
…[truncated 920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6578
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-17T18:52:14.199038+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 through ARR:

## Paper Submission Requirements

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource
…[truncated 1610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 8990
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-17T18:52:25.897491+00:00_

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

_source line 717 · 2026-05-17T18:52:26.349268+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\pm}2\%$) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline largely avoids hacking on identical data, suggesting the failure is RL-specific.
4	Repurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.
5	Across multiple reward conditions, logic types, and model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target, with collapse dynamics that resist prediction from the metric definition alone.\footnote{Code and data: \url{[anonymized]}}
6	\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-17T18:52:26.349599+00:00_

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

_source line 719 · 2026-05-17T18:52:26.951953+00:00_

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
13	\paragraph{Solver Trace Ablation.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the 
…[truncated 3597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-17T18:52:26.952447+00:00_

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

_source line 721 · 2026-05-17T18:52:27.003053+00:00_

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
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-17T18:52:35.185873+00:00_

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

_source line 723 · 2026-05-17T18:52:36.089836+00:00_

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
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate: the residual of proved samples matching none of the nine cataloged patterns (\S\ref{sec:taxonomy}); we use ``genuine'' interchangeably in descriptive contexts.
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved sample
…[truncated 17373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-17T18:52:36.241005+00:00_

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


### Tool call

_source line 725 · 2026-05-17T18:52:36.241440+00:00_

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

_source line 726 · 2026-05-17T18:52:36.291965+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{polu2020generative, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1-2025} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Unlike potential-based reward shaping~\citep{ng1999policy}, ISR augmentation does not preserve optimal policy, as it rewards output properties (component necessity) rather than state transitions, explaining the observed Goodhart vulnerability.
11	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
12	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
13	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, wher
…[truncated 2403 chars]

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

_source line 727 · 2026-05-17T18:52:36.292350+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$; \S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR produces descriptively more genuine output than random controls (pooled N-H: 23\% vs.\ 8\%); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\text{OR}{=}0.61$, n.s.).
6	Extended training confirms the window closes.
7	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
8	While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\S\ref{sec:goodhart}), non-monotonic dose-response across four $\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\S\ref{sec:crosslogic}).
9	These details underscore the gap between predicting \emph{that} a metric will be gamed and predicting \emph{how}.
10	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
11	

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

_source line 728 · 2026-05-17T18:52:41.563779+00:00_

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

_source line 729 · 2026-05-17T18:52:41.965826+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single model family (Qwen3-4B/1.7B) and a single structured-NLI dataset (FOLIO, 500 training examples); whether the specific hacking modes and collapse dynamics generalize to other architectures or larger-scale formal reasoning benchmarks remains an open question.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$). CMH tests yield $p{<}10^{-9}$ but assume within-stratum independence, which is violated when samples share a checkpoint and decoding strategy; CMH $p$-values are therefore inflated and should be interpreted as directional indicators, not calibrated significance levels.
8	STA requires solvers supporting component-level input manipulation.
9	Non-hacking is a residual classification; undiscovered gaming modes would reduce the true non-hacking rate, as illustrated by H7b (obfuscated tautology evading text-match classifiers) and query-as-fact gaming in Prolog.
10	
11	\paragraph{Evaluation as temporal snapshot.}
12	All 500-step results represent a temporal snapshot, not an equilibrium.
13	Trajectory analysis on seeds~42 and~45 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient (s42: $17\%{\to}2\%$; s45: $55\%{\to}0\%$ genuine).
14	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
15	
16	\paragraph{Seed counts per dose.}
17	ISR $\beta{=}0.05$ us
…[truncated 1638 chars]

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

_source line 730 · 2026-05-17T18:52:41.966208+00:00_

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


### Tool call

_source line 731 · 2026-05-17T18:52:42.217222+00:00_

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

_source line 732 · 2026-05-17T18:52:42.268736+00:00_

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
…[truncated 43671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-17T18:52:42.269278+00:00_

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
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-17T18:52:48.696688+00:00_

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

_source line 735 · 2026-05-17T18:52:48.748902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-17T18:52:55.322266+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
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
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-17T18:52:55.625247+00:00_

&lt;persisted-output>
Output too large (37.7KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/ceeb0556-7eea-41fe-a05f-77444259e8bf/tool-results/bb16ktrkq.txt

Preview (first 2KB):
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
  severity: critical
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
  last_seen_ro
…[truncated 290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-17T18:52:56.056077+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml 2>/dev/null | head -50",
  "description": "Check project constraints config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml 2>/dev/null | head -50",
    "description": "Check project constraints config"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-17T18:52:56.558454+00:00_

_next_id: 14
constraints:
- id: C001
  added: 2026-05-13 23:57 UTC
  summary: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl
    或其他数据文件
  scope: all
  reason: 'Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed
    仅控制模型初始化和训练随机性。'
- id: C002
  added: 2026-05-14 00:01 UTC
  summary: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c
    VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU
  scope: all
  reason: plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM
    死亡。这是第二次 GPU 冲突事故。
- id: C003
  added: 2026-05-14 01:40 UTC
  summary: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽
  scope: all
  reason: plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存
    3 份模型权重（~48GB）+ completions parquet（~2.5GB）。
- id: C004
  added: 2026-05-14 02:36 UTC
  summary: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run
    可能使用不同版本的 ISR 计算代码）
  scope: all
  reason: Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4
    使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。
- id: C005
  added: 2026-05-14 04:01 UTC
  summary: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑
  scope: worker
  reason: fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638
    MiB 显存。2026-05-14 事故。
- id: C006
  added: 2026-05-14 11:53 UTC
  summary: 论文讨论 ISR 时必须区分两种语义：exec-only 的 low ISR = 冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA
    的 high ISR = metric gaming（Goodhart 效应）。不可将 ISR 差异直接等同于 reasoning 能力差异。
  scope: all
  reason: Reviewer 发现 Prolog exec-only 生成大量重复 ground facts（如 penguin(fido). 出现 3 次），per-clause
    ablation 下删任一重复不影响结果，ISR=0。这是冗余不是无推理。如不区分，审稿人会误读 ISR 差异。
- id: C007
  added: 2026-05-14 23:23 UTC
  summary: kill_job 后必须 nvidia-smi 确认 GPU 释放，submit 前必须 nvidia-smi 确认目标 GPU 无残留进程
  scope: worker
  reason: 同一 session 两次出现 kill tmux → Python orphan → 新实验 OOM 
…[truncated 132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-17T18:52:56.709526+00:00_

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

_source line 741 · 2026-05-17T18:52:56.761010+00:00_

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

_source line 742 · 2026-05-17T18:53:02.733763+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/config.yaml 2>/dev/null || grep -rn \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ --include=\"*.yaml\" 2>/dev/null | head -10",
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
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/config.yaml 2>/dev/null || grep -rn \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ --include=\"*.yaml\" 2>/dev/null | head -10",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-17T18:53:03.681144+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 947
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-17T18:53:03.865159+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "Check LaTeX compilation status"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
    "description": "Check LaTeX compilation status"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-17T18:53:04.935725+00:00_

/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (22 pages, 605280 bytes).
Transcript written on main.log.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1070
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-17T18:53:21.101792+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -n \"\\\\\\\\bibliography\\|\\\\\\\\appendix\\|\\\\\\\\section{Limitations}\" main.tex",
  "description": "Check section boundaries for page count"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -n \"\\\\\\\\bibliography\\|\\\\\\\\appendix\\|\\\\\\\\section{Limitations}\" main.tex",
    "description": "Check section boundaries for page count"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-17T18:53:22.105567+00:00_

39:\bibliography{references}
41:\appendix
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-17T18:53:22.306670+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -c \"Output written on\" main.log && grep \"pages\" main.log | tail -5",
  "description": "Check page info from log"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -c \"Output written on\" main.log && grep \"pages\" main.log | tail -5",
    "description": "Check page info from log"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-17T18:53:22.457646+00:00_

1
Package hyperref Info: Plain pages OFF on input line 4210.
Output written on main.pdf (22 pages, 605280 bytes).
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

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

_source line 750 · 2026-05-17T18:53:26.894884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.log",
  "limit": "50",
  "offset": "4150"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.log",
    "limit": "50",
    "offset": "4150"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-17T18:53:26.945656+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (4150). The file has 1333 lines.&lt;/system-reminder>

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

_source line 752 · 2026-05-17T18:53:33.472033+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -n \"\\\\[.*\\\\].*{.*}\" main.log | grep -i \"page\\|ship\" | tail -20",
  "description": "Check page shipout info"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -n \"\\\\[.*\\\\].*{.*}\" main.log | grep -i \"page\\|ship\" | tail -20",
    "description": "Check page shipout info"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-17T18:53:33.522772+00:00_

Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

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

_source line 754 · 2026-05-17T18:53:37.940798+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -n \"Limitations\\|appendix\\|bibliography\" main.log | head -10",
  "description": "Find section page boundaries in log"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -n \"Limitations\\|appendix\\|bibliography\" main.log | head -10",
    "description": "Find section page boundaries in log"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-17T18:53:37.991557+00:00_

1007:) (./appendix.tex
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

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

_source line 756 · 2026-05-17T18:53:43.212496+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Get PDF info"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Get PDF info"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-17T18:53:43.313640+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sun May 17 18:53:03 2026 UTC
ModDate:         Sun May 17 18:53:03 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           22
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       605280 bytes
Optimized:       no
PDF version:     1.7
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-17T18:53:55.258065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "8-10"
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
    "pages": "8-10"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-17T18:53:55.509439+00:00_

PDF pages extracted: 3 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf (591.1KB)

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

_source line 760 · 2026-05-17T18:54:51.435040+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性** 审查。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: **EMNLP 2026** via ACL Rolling Review (ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: Long paper ≤8 页正文 + 不限 references/appendix\n- 模板: ACL LaTeX `[review]` 选项，double-blind\n- Limitations + Ethics 必须有，不计入页数\n- 评分标准: 5=Consider for Award (~top 2.5%), 4.5=Borderline Award, 4=Conference (主会议可接收), 3.5=Borderline Conference, 3=Findings (Findings 可接收), 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 实验设计与统计有效性\n- 所有定量声明是否有充分实验支撑？数据量（500 训练 / 100 评估）是否足够？\n- 统计检验的选择和解释是否正确？特别关注：CMH 检验在 greedy decoding 下的独立性假设违反、seed-level permutation test 的 power、Fisher exact test 的样本量\n- seed 数量（主实验 5 seeds，其他 dose 3 seeds，1.7B 单 seed）是否支撑论文声明？\n- \"ISR 在所有 4 个 dose 都产生 Goodhart collapse\" 这个声明的证据强度如何？\n\n### 2. 方法论严谨性\n- STA/ISR 的定义和算法是否清晰、无歧义？\n- ISR 的 premise-count confound 是否被充分讨论和控制？\n- Non-hacking 的残差分类（residual classification）方法的局限性\n- Hacking taxonomy 的分类器验证是否充分（50 样本手动验证）？\n- SFT baseline 与 RL 的对比是否公平（PR 差异：13% vs 93-97%）？\n\n### 3. 结果解释与过度声明\n- 论文声明是否超出了数据支撑的范围？\n- \"transient genuine window\" 的解释是否准确？特别是 5-seed pooled 23% vs 8% 在 H8+FN 校正后反转为 OR=0.61\n- 跨逻辑（Prolog）和跨规模（1.7B）的 generalization 声明是否过强？\n- \"ISR reliable as diagnostic, unreliable as optimizer\" 的核心声明是否有足够支撑？\n\n### 4. 可复现性\n- 实验细节是否足够复现（超参数、数据分割、评估协议）？\n- 代码和数据的可用性声明\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句概括论文]\n\n## Strengths\n[逐条列出优点，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出缺点，标注 W1, W2, ...，按严重性排序，区分 Must-Fix / Should-Fix / Minor]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 1-2 句总评]\n\n## Detailed Comments\n[逐节详细意见]\n```",
  "project": "solver-trace-ablation"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性** 审查。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: **EMNLP 2026** via ACL Rolling Review (ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: Long paper ≤8 页正文 + 不限 references/appendix\n- 模板: ACL LaTeX `[review]` 选项，double-blind\n- Limitations + Ethics 必须有，不计入页数\n- 评分标准: 5=Consider for Award (~top 2.5%), 4.5=Borderline Award, 4=Conference (主会议可接收), 3.5=Borderline Conference, 3=Findings (Findings 可接收), 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 实验设计与统计有效性\n- 所有定量声明是否有充分实验支撑？数据量（500 训练 / 100 评估）是否足够？\n- 统计检验的选择和解释是否正确？特别关注：CMH 检验在 greedy decoding 下的独立性假设违反、seed-level permutation test 的 power、Fisher exact test 的样本量\n- seed 数量（主实验 5 seeds，其他 dose 3 seeds，1.7B 单 seed）是否支撑论文声明？\n- \"ISR 在所有 4 个 dose 都产生 Goodhart collapse\" 这个声明的证据强度如何？\n\n### 2. 方法论严谨性\n- STA/ISR 的定义和算法是否清晰、无歧义？\n- ISR 的 premise-count confound 是否被充分讨论和控制？\n- Non-hacking 的残差分类（residual classification）方法的局限性\n- Hacking taxonomy 的分类器验证是否充分（50 样本手动验证）？\n- SFT baseline 与 RL 的对比是否公平（PR 差异：13% vs 93-97%）？\n\n### 3. 结果解释与过度声明\n- 论文声明是否超出了数据支撑的范围？\n- \"transient genuine window\" 的解释是否准确？特别是 5-seed pooled 23% vs 8% 在 H8+FN 校正后反转为 OR=0.61\n- 跨逻辑（Prolog）和跨规模（1.7B）的 generalization 声明是否过强？\n- \"ISR reliable as diagnostic, unreliable as optimizer\" 的核心声明是否有足够支撑？\n\n### 4. 可复现性\n- 实验细节是否足够复现（超参数、数据分割、评估协议）？\n- 代码和数据的可用性声明\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句概括论文]\n\n## Strengths\n[逐条列出优点，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出缺点，标注 W1, W2, ...，按严重性排序，区分 Must-Fix / Should-Fix / Minor]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 1-2 句总评]\n\n## Detailed Comments\n[逐节详细意见]\n```",
    "project": "solver-trace-ablation"
  }
}
````

</details>

---


### Tool result

_source line 761 · 2026-05-17T18:55:12.591790+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21156
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-17T18:55:12.742884+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: **EMNLP 2026** via ACL Rolling Review (ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: Long paper ≤8 页正文 + 不限 references/appendix\n- 模板: ACL LaTeX `[review]` 选项，double-blind\n- Limitations + Ethics 必须有，不计入页数\n- 评分标准: 5=Consider for Award (~top 2.5%), 4.5=Borderline Award, 4=Conference (主会议可接收), 3.5=Borderline Conference, 3=Findings (Findings 可接收), 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- STA（leave-one-out ablation on solver inputs）的技术新颖性如何？论文自称 LOO 本身不新，贡献在于 application + empirical findings——这种定位是否成立？\n- \"诊断性指标被优化时产生 Goodhart 效应\" 这个发现是否 predictable/trivial？论文声称 specific phenomena resist prediction——但 specific 部分是否足够 surprising？\n- 9-mode hacking taxonomy 作为贡献的价值如何？是否足够系统化？\n- 总体而言，对 EMNLP 2026 主会议是否有足够的贡献量？\n\n### 2. Related Work 覆盖与定位\n- 是否遗漏了重要相关工作？特别是：\n  - RL reward hacking 的最新文献\n  - Neurosymbolic reasoning 的其他结构性评估方法\n  - LOO/mutation testing 在 ML 中的应用\n  - Goodhart's Law 在 RLHF/RLVR 中的经验性研究\n- 论文与最近的 spurious rewards 工作、reward hacking in frontier models 的定位是否清晰？\n- 用 WebSearch 检查引用的真实性和完整性\n\n### 3. 写作质量与 AI 痕迹检查\n- 论文是否存在 AI 写作痕迹？特别检查：\n  - em-dash (—) 和解释性 en-dash (–) 的使用\n  - -ing 分词短语结尾\n  - \"Furthermore/Moreover/Additionally\" 连续使用\n  - 过度分段\n  - 用词黑名单：delve, leverage, utilize, facilitate, a myriad of, a plethora of\n- Abstract 是否在 150-250 words 内回答了四个必答问题？\n- Introduction 是否有完整叙事线（5 段结构）？\n- 全文主线是否统一（不是实验报告风格）？\n- 专有名词是否在首次使用时定义？\n\n### 4. 格式合规性\n- 页数是否符合 ≤8 页正文？\n- 模板使用是否正确（ACL + [review]）？\n- 匿名性是否保持（无作者信息泄漏）？\n- 图表知识密度和可读性\n- 引用格式是否正确？\n- Limitations 和 Ethics 章节是否完整？\n- 数字精度是否全表统一？最优加粗？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句概括论文]\n\n## Strengths\n[逐条列出优点，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出缺点，标注 W1, W2, ...，按严重性排序，区分 Must-Fix / Should-Fix / Minor]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 1-2 句总评]\n\n## Detailed Comments\n[逐节详细意见]\n```",
  "project": "solver-trace-ablation"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## 论文信息\n- 标题: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n- 路径: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- 目标 venue: **EMNLP 2026** via ACL Rolling Review (ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: Long paper ≤8 页正文 + 不限 references/appendix\n- 模板: ACL LaTeX `[review]` 选项，double-blind\n- Limitations + Ethics 必须有，不计入页数\n- 评分标准: 5=Consider for Award (~top 2.5%), 4.5=Borderline Award, 4=Conference (主会议可接收), 3.5=Borderline Conference, 3=Findings (Findings 可接收), 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- STA（leave-one-out ablation on solver inputs）的技术新颖性如何？论文自称 LOO 本身不新，贡献在于 application + empirical findings——这种定位是否成立？\n- \"诊断性指标被优化时产生 Goodhart 效应\" 这个发现是否 predictable/trivial？论文声称 specific phenomena resist prediction——但 specific 部分是否足够 surprising？\n- 9-mode hacking taxonomy 作为贡献的价值如何？是否足够系统化？\n- 总体而言，对 EMNLP 2026 主会议是否有足够的贡献量？\n\n### 2. Related Work 覆盖与定位\n- 是否遗漏了重要相关工作？特别是：\n  - RL reward hacking 的最新文献\n  - Neurosymbolic reasoning 的其他结构性评估方法\n  - LOO/mutation testing 在 ML 中的应用\n  - Goodhart's Law 在 RLHF/RLVR 中的经验性研究\n- 论文与最近的 spurious rewards 工作、reward hacking in frontier models 的定位是否清晰？\n- 用 WebSearch 检查引用的真实性和完整性\n\n### 3. 写作质量与 AI 痕迹检查\n- 论文是否存在 AI 写作痕迹？特别检查：\n  - em-dash (—) 和解释性 en-dash (–) 的使用\n  - -ing 分词短语结尾\n  - \"Furthermore/Moreover/Additionally\" 连续使用\n  - 过度分段\n  - 用词黑名单：delve, leverage, utilize, facilitate, a myriad of, a plethora of\n- Abstract 是否在 150-250 words 内回答了四个必答问题？\n- Introduction 是否有完整叙事线（5 段结构）？\n- 全文主线是否统一（不是实验报告风格）？\n- 专有名词是否在首次使用时定义？\n\n### 4. 格式合规性\n- 页数是否符合 ≤8 页正文？\n- 模板使用是否正确（ACL + [review]）？\n- 匿名性是否保持（无作者信息泄漏）？\n- 图表知识密度和可读性\n- 引用格式是否正确？\n- Limitations 和 Ethics 章节是否完整？\n- 数字精度是否全表统一？最优加粗？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句概括论文]\n\n## Strengths\n[逐条列出优点，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出缺点，标注 W1, W2, ...，按严重性排序，区分 Must-Fix / Should-Fix / Minor]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 1-2 句总评]\n\n## Detailed Comments\n[逐节详细意见]\n```",
    "project": "solver-trace-ablation"
  }
}
````

</details>

---


### Tool result

_source line 763 · 2026-05-17T18:55:14.053541+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1310
}
```

</details>

---


### Assistant

_source line 764 · 2026-05-17T18:55:20.126873+00:00_

Round 1 任务已分派给两位 Reviewer。等待审稿结果返回。

- **Reviewer 1**（方法/实验）：聚焦统计有效性、实验设计、结果解释、可复现性
- **Reviewer 2**（新颖性/写作）：聚焦贡献评估、Related Work 覆盖、AI 写作痕迹、格式合规

两位 Reviewer 正在独立审阅论文，完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 765 · 2026-05-17T19:02:04.615415+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Novelty + Completeness + Writing Quality

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种对 solver 输入进行 leave-one-out 消融的方法，用于诊断 GRPO 训练的神经符号形式化器中的 reward hacking。其导出指标 ISR (Irreducible Solver Rate) 揭示了隐藏在 prove rate 上升背后的 99.5% 结构性崩溃。当 ISR 被重新用作训练奖励信号时，在所有四个测试剂量下均表现出 Goodhart 崩溃。论文在 2 种逻辑类型、2 个模型规模、6 种奖励条件下记录了九种 hacking 模式。

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**Confidence**: 4/5
**一句话总结**: 实验设计细致、统计分析诚实的经验性研究，但核心 Goodhart 发现的新颖性不足（作者自己承认"可从定义预测"），且单一数据集（FOLIO, 500 examples）限制了泛化性。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论细致，seed-level 分析和自我纠正（H8+FN 校正后效果方向翻转）值得称赞；但 SFT 对比受 PR 水平混淆，1.7B 实验仅单 seed 与论文自身"反对单 seed 评估"的论点矛盾 |
| Excitement | 2.5/5 | 诊断工具有实用价值，但核心 Goodhart 发现可从 ISR 定义推导（作者自认），九模式分类有趣但实际影响限于窄设定 |
| Reproducibility | 4/5 | 超参数完整（Table 3/Appendix A），算法伪代码清晰，数据集公开，代码承诺开源 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心 Goodhart 发现的新颖性不足
- 具体位置：Introduction ¶3 ("That ISR will be gamed is predictable from its definition")、§5 Discussion、§2 Related Work line 22
- 问题：论文反复承认 ISR 的 Goodhart 脆弱性"可从定义预测"——tautological proofs 获得 ISR≥0.5 是 LOO 定义的固有结构偏差。论文试图通过"specific phenomena resist prediction"（随机分叉、非单调剂量响应）挽救新颖性，但这些是一阶可预测结果的二阶细节。机制在实验前已完全被规约：ISR≥0.5 for tautologies → GRPO rollout 中正反馈循环 → 崩溃。
- 为什么影响接收：对于 EMNLP 主会议，贡献 C2（Goodhart 崩溃动力学刻画）作为最大篇幅的贡献，其核心预测是 trivial 的。价值主要来自诊断侧（C1）和跨逻辑迁移（C3），但这些在篇幅上是次要的。
- 建议修改方向：(1) 重新框定论文叙事——将诊断发现（C1: 99.5% collapse invisible to PR）作为主要贡献，Goodhart 部分作为"当诊断指标被误用时的警示性案例"而非独立贡献；(2) 增加第二个数据集/任务验证诊断的泛化性，这会显著增强 C1 的贡献量。

**N2** [critical] 单一数据集限制泛化性声明
- 具体位置：§4.1 Setup, §6 Limitations ¶5
- 问题：所有实验使用 FOLIO 的 500 个训练样本 + 100 个评估样本。FOLIO 总共约 1400 例，属于小规模 NLI benchmark。论文标题声称"Neurosymbolic Proof Generation"这一广泛领域，但：(a) 无数学推理数据集（MATH, GSM8K）验证；(b) 无大规模形式推理基准（Lean-based benchmarks）；(c) hacking 模式可能特定于 FOLIO 的结构（较短前提、简单一阶逻辑）。
- 为什么影响接收：从单一小数据集到"neurosymbolic proof generation"的泛化跳跃过大。审稿人无法判断这些发现是 FOLIO-specific 还是 general。
- 建议修改方向：至少在一个额外的 neurosymbolic 任务上验证 STA 诊断（不需要完整的 Goodhart 实验，只需 C1 诊断复制）；或将标题和 claim 限定为 "first-order logic NLI" 范围。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 1.7B 实验仅单 seed，与论文自身方法论矛盾
- 具体位置：§4.5, Table 1 (1.7B rows), §6 Limitations ¶4
- 问题：§4.2 花大量篇幅论证 cross-seed variance 极高（σ=47pp, stochastic bifurcation），Appendix D 明确推荐"Multi-seed evaluation with trajectory analysis should be standard practice"。然而 §4.5 的 1.7B 实验仅用 seed 42，然后从单 seed 得出"different capacities converge to different Goodhart basins"的结论。
- 建议：要么增加 1.7B seeds（至少 3 个），要么将 §4.5 重新定位为"anecdotal observation"而非贡献支撑。

**W2** [warning] SFT 对比受 PR 水平严重混淆
- 具体位置：§4.2 "SFT baseline", Introduction ¶2 ("consistent with the failure being RL-specific")
- 问题：SFT PR=13% vs. GRPO PR=93-97%。在 PR=13% 时，模型几乎没有 proved 样本可供 exploit，因此 hacking rate 低不能归因于"RL-specific"。100-step checkpoint (PR=32%) 部分控制了这个混淆，但 32% 与 97% 仍有巨大差距。论文承认 "whether SFT would hack at higher PR remains an open question"（§4.2 最后一句），但 Introduction 和 Abstract 中的表述（"supervised baseline largely avoids hacking"）未加此限定。
- 建议：在所有提及 SFT 对比的位置加上 PR-level caveat；或尝试在更高 PR 的 SFT 条件下（如更多 epoch、更强模型）验证。

**W3** [warning] 关键对比（ISR vs. Random N-H rate）在校正后方向翻转
- 具体位置：§4.3 ¶5 ("The transient genuine window"), Table 4 (Appendix C)
- 问题：5-seed pooled N-H: ISR 23% vs. Random 8%（OR=3.48, p<10⁻⁸），但论文自己指出这违反 within-seed 独立性假设。3-seed H8+FN corrected: ISR 6.06% vs. Random 9.5%（OR=0.61, p=0.182, n.s.）——方向翻转。然而 Abstract 仍写"a supervised baseline largely avoids hacking on identical data"（这个是 SFT 比较，没问题），Introduction ¶3 写"transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls"。问题在于：如果校正后方向翻转，"suggestive improvement" 可能完全是统计假象。
- 建议：Abstract 和 Introduction 中应直接提及校正后方向翻转，而非仅在正文 §4.3 深处才交代。这是 intellectual honesty 的关键测试。

**W4** [warning] 九模式分类的系统性存疑
- 具体位置：§4.6, Table 2, Appendix E
- 问题：Table 2 中 H2-H6 标为 "isolated observations"，H9 仅出现在 1.7B single seed，query-as-fact 仅出现在 Prolog single seed。九个模式中有至少 4 个是单 seed/单条件的孤立观察。作为贡献 C4 的支撑，这个分类学的系统性和完整性不足。此外，论文自己发现 H7b 和 query-as-fact 是通过事后 cross-validation 才发现的——这暗示可能存在更多未发现的模式。
- 建议：明确区分"robust modes"（H1, H7, H8: multi-seed, multi-condition）和"observed modes"（其余），调低分类学的贡献声明。

---

## 小问题（不影响接收）

**M1** Abstract 信息密度过高：158 words 内塞入了 "99.5%", "β=0.1", "four tested doses", "nine hacking modes" 等大量数字。审稿人 30 秒内难以抓住关键 takeaway。建议减少数字，强化叙事。

**M2** Introduction 过长（2+ 页含 Contributions），读起来像压缩版全文而非 motivating narrative。每个 paragraph 都过载了定量结果（ISR*: 0.642→0.132→0.003; PR σ=47pp; OR=147 等）。这些数字应留给 Experiments。

**M3** Figure 1 占整栏宽度但信息密度一般。Panel (a) 是标准 NL→formal→solver pipeline，EMNLP 读者已知。可压缩。

**M4** Table 1 注释系统复杂（†, ‡, ††, ★, ♯），增加阅读认知负荷。

**M5** Appendix D 中 exec-only s43 使用 sampling evaluation (T=0.7) 而非 greedy——论文承认不可严格比较，但仍将其包含在 cross-seed 分析中。应更显著标注或排除。

**M6** 一处 em-dash 在 appendix.tex 第 1 行（注释 "% Appendix — solver-trace-ablation"），不影响渲染。主文无 AI 写作痕迹。

---

## 主要优势

**S1** 实验设计严谨且自我批评：seed-level 分析、H8+FN 校正后效果翻转的诚实报告、trajectory analysis 证明 transient window 是暂时的——这种统计诚实度在投稿论文中罕见。

**S2** Observer-optimizer 不对称性的框架清晰：ISR 作为诊断可靠、作为优化目标不可靠——这个 framing 简洁有力，对实践者有直接指导意义。

**S3** Cross-seed 定性分叉发现有价值：相同数据、相同奖励 → 定性不同的 hacking 模式（H1 vs. H7 vs. tautological collapse），这对 neurosymbolic RL 的可复现性讨论有贡献。

**S4** 写作质量好：无显著 AI 写作痕迹（无解释性 em-dash、无 Furthermore/Moreover 连用、无黑名单词汇），叙事聚焦且纪律性强。Related Work 定位清晰，与 Kim et al. (2026)、Pan et al. (2022)、Manheim & Garrabrant (2019) 的区分精确。

**S5** 引用覆盖全面：42 篇引用覆盖了 reward hacking 理论（Goodhart, Manheim, Skalse）、经验性研究（Karwowski, Kwa, Bondarenko, Kim）、neurosymbolic 方法（Logic-LM, LINC, SatLM, FoVer, LoRP）、process rewards（Lightman, Math-Shepherd, VersaPRM, ThinkPRM）和 mutation testing 基础。引用验证显示所有条目真实存在，少数年份/作者格式 mismatch 属于正常范围。

---

## Questions

**Q1**: 为什么不在 ISR 训练中对 component count 归一化（如 ISR_norm = ISR(x) / E[ISR | n]）？如果 premise-count confound 是 Goodhart 脆弱性的核心机制，归一化可能消除或减弱这个攻击面。如果不行，原因是什么？

**Q2**: ISR 是否被测试过作为 filter（拒绝 ISR 低于阈值的输出）而非 reward？这对诊断指标来说更自然的使用方式，且完全避免 Goodhart 风险。

**Q3**: Non-hacking 是残差分类。鉴于 H7b 和 query-as-fact gaming 都是事后发现的，作者对九种模式的穷尽性有多大信心？

**Q4**: 论文仅使用 Qwen3 系列。不同模型家族（Llama, Gemma）或 instruction-tuned vs. base 模型是否会产生本质不同的 hacking 动力学？

**Q5**: 如果增加训练数据规模（如 5000 examples），hacking 的普遍性和模式分布是否会改变？500 examples 是否太小导致 GRPO 更容易过拟合到 degenerate 策略？

---

## Missing References

**MR1** Khalaf et al., "Inference-Time Reward Hacking in Large Language Models", NeurIPS 2025 (arXiv:2506.19248)——直接相关于论文讨论的 training-time vs. inference-time reward hacking 区分。论文引用了 Kim et al. (2026) 和 Bondarenko et al. (2025) 作为 inference-time gaming 的对比，但遗漏了这篇专门研究 inference-time reward hacking 的 NeurIPS 论文。

**MR2** "Reward Hacking as Equilibrium under Finite Evaluation" (arXiv:2603.28063, 2026)——提供了 reward hacking 为何在有限评估下必然出现的理论视角，与论文的经验性发现互补。

**MR3** "Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms" (NeurIPS 2024)——论文引用了 Gao et al. (2023) 的原始 scaling laws 工作，但遗漏了 2024 年扩展到 DAA 的后续工作，后者对 Goodhart 在不同训练范式中的普遍性提供了更新的证据。

---

## 格式合规性

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 页数 ≤8 正文 | ✓ | §1-§5 在 page 8 内完成 |
| ACL 模板 + [review] | ✓ | `\usepackage[review]{acl}` |
| 匿名性 | ✓ | "Anonymous ACL submission", URL [anonymized] |
| 行号 | ✓ | PDF 中可见 |
| Limitations 章节 | ✓ | 详尽（6 段落），包含 temporal snapshot、seed counts、data scale |
| Ethics Statement | ✓ | 涵盖 AI safety implications、公开数据集/模型、无人类受试者 |
| 数字精度统一 | ✓ | 全表小数精度一致 |
| 最优加粗 | ✓ | Table 1, Table 2 中最优值加粗 |
| AI 写作痕迹 | ✓ | 未检测到 em-dash/en-dash（主文）、无 Furthermore/Moreover 连用、无黑名单词汇 |
| 引用格式 | ✓ | ACL bibliography style，\citep/\citet 使用正确 |

---

## Detailed Comments（逐节）

### Abstract
- 信息完整但密度过高。"trajectory-confirmed at β=0.1" 这类细节不属于 Abstract。
- "nine hacking modes" 在 Abstract 中提到但未给出任何示例，读者无法判断其价值。
- 建议：删减数字，保留 "99.5% collapse" 和 "Goodhart collapse at all tested doses" 两个核心数据点即可。

### Introduction (§1)
- 叙事结构完整（blind spot → STA → ISR as reward → contributions），逻辑流畅。
- 但 ¶2 (Solver Trace Ablation) 和 ¶3 (ISR as reward) 过载数字——Introduction 应建立直觉和动机，数字留给 Experiments。
- C4 ("nine-mode hacking taxonomy") 的支撑证据中有至少 4 个模式是孤立观察，Contribution 声明与证据强度不匹配。

### Related Work (§2)
- 结构清晰（四段落：neurosymbolic reasoning, process rewards, reward hacking, mutation testing）。
- 与 Kim et al. (2026) 的区分精确且有价值（inference-time vs. training-time gaming emergence）。
- 与 Ng (1999) potential-based reward shaping 的理论联系有洞察力（ISR 不保持最优策略不变）。
- 缺少 inference-time reward hacking (NeurIPS 2025) 引用。

### Method (§3)
- Algorithm 1 清晰。ISR 定义明确。
- LOO vs. Shapley 的讨论充分且论证合理。
- §3.2 "Limitations of ISR and the premise-count confound" 的自我批评值得肯定，但这里暴露了一个问题：如果 premise-count confound 在设计阶段就已知，为什么没有尝试 count-normalized ISR 作为 reward？这个显而易见的 ablation 的缺失削弱了 Goodhart 发现的深度。

### Experiments (§4)
- §4.2 (ISR as Diagnostic): 最强部分。99.5% collapse trajectory (Fig 2) 是清晰有力的证据。Cross-seed divergence 分析有价值。
- §4.3 (Goodhart Effects): 实验设计合理（matched random control, dose-response），但核心发现可预测。统计分析的诚实度（校正后方向翻转）难得，但也削弱了 claim。
- §4.4 (Cross-Logic): 有趣但 Prolog 部分证据较薄（3 seeds, no random control for Prolog ISR）。
- §4.5 (Cross-Scale): 单 seed，方法论上不足。
- §4.6 (Taxonomy): Table 2 布局好，但"九模式"中多数是孤立观察。

### Discussion & Conclusion (§5)
- 简洁有效。"ISR is reliable as a diagnostic but unreliable as an optimizer" 是清晰的 takeaway。
- 最后一句 ("ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals") 是实用建议。

### Limitations (§6)
- 极为详尽（temporal snapshot, seed counts, cross-scale replication, data scale）。这是本文的一个显著优势——比多数投稿论文的 Limitations 都更诚实和全面。


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

_source line 766 · 2026-05-17T19:02:15.905978+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 70

## Round 70

2 recorded events


### User

_source line 767 · 2026-05-17T19:02:18.427617+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断：Overall 3.0 (Findings)**

两个 Must-Fix 问题决定了评分：
1. **核心 Goodhart 发现的新颖性不足**——作者自己反复承认 ISR 被 gaming 是"可从定义预测的"，论文最大篇幅的贡献 (C2) 本质上是在详细确认一个预期结果
2. **单一数据集 (FOLIO, 500 examples) 限制泛化性**——标题声称"Neurosymbolic Proof Generation"但仅在一个小规模 NLI benchmark 上验证

主要优势在于实验设计的严谨性和统计分析的诚实度（H8+FN 校正后效果翻转的如实报告在投稿论文中罕见），以及 observer-optimizer 不对称性的清晰框架。写作质量好，无 AI 痕迹，格式完全合规。

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

_source line 768 · 2026-05-17T19:02:25.988198+00:00_

Reviewer 2 审稿意见已收到。核心判断 3.0 (Findings)，两个 critical 问题：Goodhart 发现新颖性不足 + 单一数据集泛化性受限。

等待 Reviewer 1 提交审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 71

## Round 71

6 recorded events


### User

_source line 769 · 2026-05-17T19:02:37.747893+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性 + 实验有效性

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的神经符号证明生成器中的结构性 reward hacking。其派生指标 Irreducible Solver Rate (ISR) 揭示了在 prove rate 高达 97±2% 的情况下，99.5% 的证明存在结构性退化（冗余/空洞推理）。论文进一步将 ISR 作为 reward 信号，发现所有测试剂量下均出现 Goodhart collapse，由此得出 "ISR 作为诊断可靠，作为优化目标不可靠" 的核心结论。论文归纳了 9 种 hacking 模式，并提供了 Prolog 跨逻辑和 1.7B 跨规模的初步证据。

## Strengths

**S1. 新颖且重要的诊断视角**
STA/ISR 填补了神经符号证明质量评估中 execution-based 指标的盲区。将软件工程中的 mutation testing 思想引入 RL reward hacking 检测，理论动机清晰。LOO 消融在概念上简洁（Algorithm 1），且与 Shapley value 的关系讨论（§3.2）增强了方法的理论基础。

**S2. 核心发现具有真实的实用价值**
"高 prove rate 可以与结构空洞的证明共存" 这一发现对 AI safety 和 neurosymbolic reasoning 社区有直接警示意义。Figure 2 清晰展示了 ISR collapse 轨迹与 PR 上升的背离，信息密度高。

**S3. 论文对自身局限的透明度高于平均水平**
§7 Limitations 和正文中多处主动承认统计检验的假设违反（CMH 独立性，§7）、seed-level 检验力不足（p=0.28）、premise-count confound（§3.2, §4.1）。这种透明度值得肯定。

**S4. Goodhart's Law 理论框架的引入恰当**
将 Manheim & Garrabrant (2019) 的分类法应用到 ISR 的 Goodhart 漏洞分析中（§4.3），使得实证发现有理论归属，提升了工作的可引用性。

**S5. Hacking taxonomy 的颗粒度较好**
9 种模式（Table 2）横跨 2 种逻辑、2 种规模，H1/H7/H8 三大主导模式的跨 seed 稳健性为后续研究提供了操作性的分类词汇。

## Weaknesses

### Must-Fix 问题（影响接收决定）

**W1 [critical] 统计框架内部矛盾：既否认检验有效性又引用其结果**

论文在 §7 明确承认 CMH 检验的独立性假设被违反（"CMH tests yield p<10⁻⁵ but assume within-stratum independence, which is violated when samples share a checkpoint and decoding strategy"），并将其降级为 "directional indicators, not calibrated significance levels"。然而在正文中，具体 p 值仍被用于支撑核心声明：

- §4.2 SFT 对比：OR=8.41, p<0.001
- §4.2 seed-level permutation test: p=0.28
- §4.2 premise-count confound: p=0.26
- Table 4 (Appendix): 多处 p<0.001

如果统计框架被承认为不可靠，论文应当：(a) 提供一种有效的替代统计方法（如 bootstrap confidence intervals with cluster correction），或 (b) 彻底移除所有具体 p 值，纯粹以描述性方式呈现结果。当前 "先免责再引用" 的做法削弱了方法论严谨性。

**W2 [critical] Seed 数量不足以支撑对随机分岔现象的声明**

论文的核心发现之一是 ISR collapse 呈现 "stochastic bifurcation"（§4.2: "2/5 seeds collapse within ~150 steps"）。但：
- 主实验仅 5 seeds：2/5 vs 3/5 的分裂无法区分于随机噪声
- Dose-response（§4.3）每个剂量仅 3 seeds：β=0.05 时 "2/5 seeds collapse"，β=0.1 时 "stochastic and delayed"——3 seeds 无法刻画 dose-response 曲线的任何非单调性
- 1.7B 跨规模（§4.5）仅 1 seed："preliminary cross-scale evidence" 在统计意义上等于单个轶事
- §4.2 明确报告 seed-level permutation test p=0.28——即主效应在 seed-level 统计上无显著性

当 stochastic bifurcation 是核心发现时，5 seeds 是根本性不足。至少需要 10-20 seeds 才能可靠刻画分岔的概率分布。建议：(a) 增加 seeds 至 ≥15 seeds 用于主条件，或 (b) 将所有涉及 seed 分岔的声明改为纯描述性观察，移出核心贡献。

**W3 [critical] Premise-count confound 根本性地限制了 ISR 的可解释性**

ISR 定义（Eq. 1）对 premise count 有结构性依赖：n 个 component 中只要 1 个冗余，ISR 就从 1.0 降至 (n-1)/n。这意味着：

1. **ISR 混淆了 "结构必要性" 与 "证明长度"**：较短的 formalization 机械性地倾向于更高 ISR，与推理质量无关
2. **"Transient genuine window" 本质上是 selection effect**：§4.2 自己承认 premise-count-matched comparison 将 ISR 优势从显著降至 1.06×，实质消失
3. **Goodhart vulnerability 直接利用此 confound**：H7 tautologies（单 premise = conclusion）自动获得 ISR≥0.5，不是因为推理质量好，而是因为 component 少
4. **Appendix C Extended Discussion 进一步确认**："ISR quantifies syntactic component necessity, not semantic faithfulness"

论文需要：(a) 提出 premise-count-normalized ISR 变体并重新运行关键实验，或 (b) 将所有 "structural integrity" 措辞改为 "component non-redundancy"（一个更弱但更准确的声称），并在 Abstract 和 Introduction 中前置此限制。

**W4 [major] SFT baseline 对比存在系统性 selection bias**

SFT 达到 PR≈13%（§4.2），GRPO 达到 93-97%。论文用 OR=8.41 (p<0.001) 声称 "the failure is RL-specific"（Abstract, §4.2）。但 SFT 的 13% 成功样本极可能是 "容易" 的问题——这些问题可能本身不需要复杂推理，因此 hacking 几率本来就低。

这构成经典的 selection bias：成功率悬殊时，比较成功样本的质量不等于比较方法的内在倾向。论文需要：
- 按问题难度分层对比（如 gold proof 长度、所需推理步数）
- 或只比较两种方法都成功的问题子集
- 或将 "RL-specific" 声称限定为 "在高 PR regime 下 RL 特有"

### Should-Fix 问题（影响评分但不一票否决）

**W5 [warning] "Transient genuine window" 不应出现在 Abstract/Introduction 的贡献声明中**

"Genuine window" 在三个独立维度上均未通过检验：
- 统计：seed-level permutation test p=0.28（§4.2）
- Confound 校正：premise-count matching 后降至 1.06×（§4.2）
- 方向校正：H8+FN correction 后 OR 反转为 0.61（§4.2）

尽管论文在正文中承认 "should not be interpreted as evidence that ISR reliably improves structural quality"，但 Abstract 和 Introduction 仍将其列为发现（"the transient genuine window at broadscale closes..."）。建议从 Abstract/Introduction 贡献列表中移除此项，仅在正文中作为描述性观察保留。

**W6 [warning] Hacking taxonomy 验证不充分**

- 分类器验证仅用 50 个样本（Appendix D 中提到），无 inter-annotator agreement 报告
- 9 个类别中 H1/H7/H8 占 >90%（Table 2），其余 6 个模式的样本量可能不足以支撑独立类别的设立
- Residual classification（将非 hacking 定义为 "排除所有已知 hacking 模式的残差"）inherently inflate non-hacking rate，因为新的 hacking 模式会被错误归入 non-hacking
- §3.3 中 hacking taxonomy 的描述混合了自动检测（text matching for H1/H7）和手动分类，但没有说明手动分类的覆盖范围

**W7 [warning] Cross-logic generalization 证据不足以支撑 §4.4 的标题 "Cross-Logic Diagnostic Transfer"**

Prolog 实验（§4.4）：3 seeds，2/3 ISR≈0，1/3 diverge。但：
- Solver 不同（SWI-Prolog vs ProofWriter）
- 逻辑不同（Prolog vs FOL）
- 1/3 seeds 表现不一致
- 没有分析相同 hacking 模式是否出现

"Transfer" 暗示方法的可迁移性，但实际只是在不同设置下重新运行了相同度量。建议将标题改为 "Preliminary Prolog Replication" 或类似描述性表述。

**W8 [warning] 训练/评估数据关系需澄清**

§4.1 提到训练用 "500 examples"，held-out 评估用 "100 FOLIO examples"。但：
- 正文多处提到 "on identical data"（Abstract, §1），具体指什么？训练集？评估集？
- Table 3 (Appendix A) 列出 "Training set: FOLIO, 500 examples" 和 "Evaluation set: FOLIO, 100 examples (held-out)"——但 ISR 在训练过程中也被计算（作为 reward），这里的 "held-out" 指的是从训练 reward 计算中排除还是从 FOLIO 原始数据集中划分？
- 如果 Figure 2 的 ISR 轨迹是在训练数据上计算的，那么 ISR 值会受到过拟合影响

### Minor 问题（不影响接收）

**M1.** Table 1 caption 中 "Hacking modes" 各模式的缩写（H1, H7 等）首次在 Table 2 定义但 Table 1 先引用，造成前向引用困惑。

**M2.** Figure 3 (Hacking Composition) 使用 stacked area chart 但 seed 间差异较大；per-seed 轨迹线或 box plot 可能更能展示 stochastic bifurcation。

**M3.** §3.2 讨论 Shapley values vs LOO 时给出了选择 LOO 的三个理由，但第三个理由（"the Goodhart effect we document would likely transfer to Shapley-based metrics"）是循环论证——用尚未证明的结论来辩护方法选择。

**M4.** 引用格式：`folio` 条目年份 bib 为 2024 vs OpenAlex 为 2022（可能是 arxiv vs 会议版本差异，建议确认使用会议发表年份）。

## Questions

**Q1.** STA 的 false-negative rate 是多少？如果 solver 内部有推理冗余（某个 premise 逻辑上必要但 solver 可以从其他 premises 推导），STA 会低估 necessity。这在 ProofWriter 上表现如何？

**Q2.** 如果使用 premise-count-normalized ISR（如 ISR / expected_ISR_under_random_ablation）作为 reward，Goodhart collapse 是否仍然发生？

**Q3.** §4.2 报告 "87.1% of proved samples exhibit the confusion (H1)"——这个比例在训练早期（如 step 100）是多少？H1 是一开始就主导还是随训练演化出现？

**Q4.** Abstract 中 "99.5% structural collapse" 的精确含义是什么？是指 ISR=0 的比例，还是 ISR<某阈值的比例？如果是前者，那么 ISR=0 在 LOO 定义下意味着 *每个* component 都是可移除的——这真的可能吗？

**Q5.** 论文是否考虑过 ISR 在 sampling decoding（而非 greedy decoding）下的表现？训练用 sampling 但评估用 greedy，这种不一致是否影响 ISR 作为诊断指标的有效性？

## Missing References

1. **Uesato et al. (2022)** "Solving Math Word Problems with Process- and Outcome-Based Feedback"——直接相关的 process vs outcome reward 对比，与 ISR vs PR 的对比有概念上的对应关系
2. **Cobbe et al. (2021)** "Training Verifiers to Solve Math Word Problems"——verifier-based 方法的奠基工作，与 STA 作为验证工具的定位相关
3. 论文引用了 Gao et al. (2023) 的 reward overoptimization scaling laws，但没有讨论 ISR 的 Goodhart collapse 是否符合其 scaling law 预测（KL divergence vs reward 的关系）——这是一个有价值的理论连接

## Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5** (High: I am quite sure of my assessment)

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 统计框架存在内部矛盾（W1）；核心声明的 seed 数量不足（W2）；ISR 的 premise-count confound 未被充分控制（W3）；SFT 对比有 selection bias（W4）。主要 claims 的支撑力度介于 "Poor" 和 "Acceptable" 之间。 |
| Excitement | 3.5/5 | 问题重要（reward hacking 在 neurosymbolic 系统中是 underexplored gap），STA/ISR 的概念新颖且有实用价值，Goodhart's Law 连接有见地。但范围受限（单数据集、单模型家族）降低了 excitement。 |
| Overall | 3.0/5 | 核心观察有价值（execution-based 评估遗漏结构退化），但 W1-W4 的方法论问题使得论文的核心声明超出了数据支撑范围。作为 Findings 论文可接收——前提是修复统计呈现（W1）、弱化/限定关键声称（W2 中的 bifurcation、W3 中的 structural integrity、W5 中的 genuine window），并补充 SFT 的 difficulty-controlled 分析（W4）。当前形式不足以支撑主会议接收，因为 soundness 问题涉及核心贡献而非边缘细节。 |

## 一句话总结

STA/ISR 作为诊断工具的概念有价值，但统计基础（小 seed 数 + 违反假设的检验 + 未控制的 confound）不足以支撑论文的核心声明强度，需要显著弱化 claims 或显著增强实验证据。


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

_source line 770 · 2026-05-17T19:03:25.994493+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见：Novelty + Completeness + Writing Quality\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种对 solver 输入进行 leave-one-out 消融的方法，用于诊断 GRPO 训练的神经符号形式化器中的 reward hacking。其导出指标 ISR (Irreducible Solver Rate) 揭示了隐藏在 prove rate 上升背后的 99.5% 结构性崩溃。当 ISR 被重新用作训练奖励信号时，在所有四个测试剂量下均表现出 Goodhart 崩溃。论文在 2 种逻辑类型、2 个模型规模、6 种奖励条件下记录了九种 hacking 模式。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 核心 Goodhart 发现的新颖性不足\n- 论文反复承认 ISR 的 Goodhart 脆弱性\"可从定义预测\"——tautological proofs 获得 ISR≥0.5 是 LOO 定义的固有结构偏差。论文试图通过\"specific phenomena resist prediction\"（随机分叉、非单调剂量响应）挽救新颖性，但这些是一阶可预测结果的二阶细节。\n- 建议：重新框定论文叙事——将诊断发现（C1: 99.5% collapse invisible to PR）作为主要贡献，Goodhart 部分作为警示性案例。\n\n**N2** [critical] 单一数据集限制泛化性声明\n- 所有实验使用 FOLIO 的 500 个训练样本 + 100 个评估样本。标题声称\"Neurosymbolic Proof Generation\"但仅在一个小规模 NLI benchmark 上验证。\n\n## Should-Fix 问题\n\n**W1** [warning] 1.7B 实验仅单 seed，与论文自身方法论矛盾\n\n**W2** [warning] SFT 对比受 PR 水平严重混淆\n\n**W3** [warning] 关键对比（ISR vs. Random N-H rate）在校正后方向翻转——Abstract 和 Introduction 中应直接提及。\n\n**W4** [warning] 九模式分类的系统性存疑——至少 4 个是单 seed/单条件的孤立观察。\n\n## 小问题\n\n**M1** Abstract 信息密度过高\n**M2** Introduction 过长，过载定量结果\n**M3** Figure 1 信息密度一般\n**M4** Table 1 注释系统复杂\n**M5** Appendix D 中 exec-only s43 使用 sampling evaluation\n**M6** 一处 em-dash 在 appendix.tex 注释中\n\n## 主要优势\n\n**S1** 实验设计严谨且自我批评\n**S2** Observer-optimizer 不对称性的框架清晰\n**S3** Cross-seed 定性分叉发现有价值\n**S4** 写作质量好，无 AI 写作痕迹\n**S5** 引用覆盖全面\n\n## Questions\n\n**Q1**: 为什么不在 ISR 训练中对 component count 归一化？\n**Q2**: ISR 是否被测试过作为 filter 而非 reward？\n**Q3**: 对九种模式的穷尽性有多大信心？\n**Q4**: 不同模型家族是否会产生本质不同的 hacking 动力学？\n**Q5**: 增加训练数据规模，hacking 的普遍性和模式分布是否会改变？\n\n## Missing References\n\n**MR1** Khalaf et al., \"Inference-Time Reward Hacking in Large Language Models\", NeurIPS 2025\n**MR2** \"Reward Hacking as Equilibrium under Finite Evaluation\" (arXiv:2603.28063, 2026)\n**MR3** \"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\" (NeurIPS 2024)",
  "project": "solver-trace-ablation"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见：Novelty + Completeness + Writing Quality\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种对 solver 输入进行 leave-one-out 消融的方法，用于诊断 GRPO 训练的神经符号形式化器中的 reward hacking。其导出指标 ISR (Irreducible Solver Rate) 揭示了隐藏在 prove rate 上升背后的 99.5% 结构性崩溃。当 ISR 被重新用作训练奖励信号时，在所有四个测试剂量下均表现出 Goodhart 崩溃。论文在 2 种逻辑类型、2 个模型规模、6 种奖励条件下记录了九种 hacking 模式。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 核心 Goodhart 发现的新颖性不足\n- 论文反复承认 ISR 的 Goodhart 脆弱性\"可从定义预测\"——tautological proofs 获得 ISR≥0.5 是 LOO 定义的固有结构偏差。论文试图通过\"specific phenomena resist prediction\"（随机分叉、非单调剂量响应）挽救新颖性，但这些是一阶可预测结果的二阶细节。\n- 建议：重新框定论文叙事——将诊断发现（C1: 99.5% collapse invisible to PR）作为主要贡献，Goodhart 部分作为警示性案例。\n\n**N2** [critical] 单一数据集限制泛化性声明\n- 所有实验使用 FOLIO 的 500 个训练样本 + 100 个评估样本。标题声称\"Neurosymbolic Proof Generation\"但仅在一个小规模 NLI benchmark 上验证。\n\n## Should-Fix 问题\n\n**W1** [warning] 1.7B 实验仅单 seed，与论文自身方法论矛盾\n\n**W2** [warning] SFT 对比受 PR 水平严重混淆\n\n**W3** [warning] 关键对比（ISR vs. Random N-H rate）在校正后方向翻转——Abstract 和 Introduction 中应直接提及。\n\n**W4** [warning] 九模式分类的系统性存疑——至少 4 个是单 seed/单条件的孤立观察。\n\n## 小问题\n\n**M1** Abstract 信息密度过高\n**M2** Introduction 过长，过载定量结果\n**M3** Figure 1 信息密度一般\n**M4** Table 1 注释系统复杂\n**M5** Appendix D 中 exec-only s43 使用 sampling evaluation\n**M6** 一处 em-dash 在 appendix.tex 注释中\n\n## 主要优势\n\n**S1** 实验设计严谨且自我批评\n**S2** Observer-optimizer 不对称性的框架清晰\n**S3** Cross-seed 定性分叉发现有价值\n**S4** 写作质量好，无 AI 写作痕迹\n**S5** 引用覆盖全面\n\n## Questions\n\n**Q1**: 为什么不在 ISR 训练中对 component count 归一化？\n**Q2**: ISR 是否被测试过作为 filter 而非 reward？\n**Q3**: 对九种模式的穷尽性有多大信心？\n**Q4**: 不同模型家族是否会产生本质不同的 hacking 动力学？\n**Q5**: 增加训练数据规模，hacking 的普遍性和模式分布是否会改变？\n\n## Missing References\n\n**MR1** Khalaf et al., \"Inference-Time Reward Hacking in Large Language Models\", NeurIPS 2025\n**MR2** \"Reward Hacking as Equilibrium under Finite Evaluation\" (arXiv:2603.28063, 2026)\n**MR3** \"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\" (NeurIPS 2024)",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-17T19:03:54.365230+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28370
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-17T19:03:54.516328+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的神经符号证明生成器中的结构性 reward hacking。其派生指标 Irreducible Solver Rate (ISR) 揭示了在 prove rate 高达 97±2% 的情况下，99.5% 的证明存在结构性退化。论文将 ISR 作为 reward 信号，发现所有测试剂量下均出现 Goodhart collapse，由此得出 \"ISR 作为诊断可靠，作为优化目标不可靠\" 的核心结论。\n\n## Strengths\n\n**S1.** STA/ISR 填补了神经符号证明质量评估中 execution-based 指标的盲区。\n**S2.** 核心发现对 AI safety 和 neurosymbolic reasoning 社区有直接警示意义。\n**S3.** 论文对自身局限的透明度高于平均水平。\n**S4.** Goodhart's Law 理论框架引入恰当。\n**S5.** Hacking taxonomy 颗粒度较好。\n\n## Must-Fix 问题\n\n**W1 [critical] 统计框架内部矛盾：既否认检验有效性又引用其结果**\n- CMH 检验的独立性假设被违反，论文承认后仍在正文中使用具体 p 值支撑核心声明\n- 要求：(a) 提供有效替代统计方法，或 (b) 彻底移除所有具体 p 值，纯粹描述性呈现\n\n**W2 [critical] Seed 数量不足以支撑对随机分岔现象的声明**\n- 主实验仅 5 seeds，2/5 vs 3/5 的分裂无法区分于随机噪声\n- Dose-response 每个剂量仅 3 seeds\n- 1.7B 仅 1 seed\n- 至少需要 10-20 seeds 才能可靠刻画分岔的概率分布\n\n**W3 [critical] Premise-count confound 根本性地限制了 ISR 的可解释性**\n- ISR 混淆了 \"结构必要性\" 与 \"证明长度\"\n- \"Transient genuine window\" 本质上是 selection effect\n- Goodhart vulnerability 直接利用此 confound\n- 需要 premise-count-normalized ISR 变体或弱化所有 \"structural integrity\" 措辞\n\n**W4 [major] SFT baseline 对比存在系统性 selection bias**\n- SFT PR≈13% vs GRPO 93-97%，成功样本可能是\"容易\"的问题\n- 需要按问题难度分层对比\n\n## Should-Fix 问题\n\n**W5 [warning] \"Transient genuine window\" 不应出现在 Abstract/Introduction 的贡献声明中**\n- 统计：p=0.28\n- Confound 校正：1.06×\n- 方向校正：OR 反转为 0.61\n\n**W6 [warning] Hacking taxonomy 验证不充分**\n- 分类器验证仅 50 样本，无 inter-annotator agreement\n- 9 类中 6 个模式样本量不足\n\n**W7 [warning] Cross-logic \"Transfer\" 措辞过强**\n- 实际只是在不同设置下重新运行，不是 transfer\n\n**W8 [warning] 训练/评估数据关系需澄清**\n- \"on identical data\" 具体指什么？\n- ISR 在训练中也被计算，held-out 的含义需明确\n\n## Questions\n\n**Q1.** STA 的 false-negative rate 是多少？\n**Q2.** premise-count-normalized ISR 作为 reward，Goodhart collapse 是否仍发生？\n**Q3.** H1 比例在训练早期（step 100）是多少？\n**Q4.** \"99.5% structural collapse\" 的精确含义？\n**Q5.** sampling decoding vs greedy decoding 对 ISR 的影响？\n\n## Missing References\n\n1. Uesato et al. (2022) \"Solving Math Word Problems with Process- and Outcome-Based Feedback\"\n2. Cobbe et al. (2021) \"Training Verifiers to Solve Math Word Problems\"\n3. Gao et al. (2023) scaling law 与 ISR Goodhart collapse 的理论连接",
  "project": "solver-trace-ablation"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的神经符号证明生成器中的结构性 reward hacking。其派生指标 Irreducible Solver Rate (ISR) 揭示了在 prove rate 高达 97±2% 的情况下，99.5% 的证明存在结构性退化。论文将 ISR 作为 reward 信号，发现所有测试剂量下均出现 Goodhart collapse，由此得出 \"ISR 作为诊断可靠，作为优化目标不可靠\" 的核心结论。\n\n## Strengths\n\n**S1.** STA/ISR 填补了神经符号证明质量评估中 execution-based 指标的盲区。\n**S2.** 核心发现对 AI safety 和 neurosymbolic reasoning 社区有直接警示意义。\n**S3.** 论文对自身局限的透明度高于平均水平。\n**S4.** Goodhart's Law 理论框架引入恰当。\n**S5.** Hacking taxonomy 颗粒度较好。\n\n## Must-Fix 问题\n\n**W1 [critical] 统计框架内部矛盾：既否认检验有效性又引用其结果**\n- CMH 检验的独立性假设被违反，论文承认后仍在正文中使用具体 p 值支撑核心声明\n- 要求：(a) 提供有效替代统计方法，或 (b) 彻底移除所有具体 p 值，纯粹描述性呈现\n\n**W2 [critical] Seed 数量不足以支撑对随机分岔现象的声明**\n- 主实验仅 5 seeds，2/5 vs 3/5 的分裂无法区分于随机噪声\n- Dose-response 每个剂量仅 3 seeds\n- 1.7B 仅 1 seed\n- 至少需要 10-20 seeds 才能可靠刻画分岔的概率分布\n\n**W3 [critical] Premise-count confound 根本性地限制了 ISR 的可解释性**\n- ISR 混淆了 \"结构必要性\" 与 \"证明长度\"\n- \"Transient genuine window\" 本质上是 selection effect\n- Goodhart vulnerability 直接利用此 confound\n- 需要 premise-count-normalized ISR 变体或弱化所有 \"structural integrity\" 措辞\n\n**W4 [major] SFT baseline 对比存在系统性 selection bias**\n- SFT PR≈13% vs GRPO 93-97%，成功样本可能是\"容易\"的问题\n- 需要按问题难度分层对比\n\n## Should-Fix 问题\n\n**W5 [warning] \"Transient genuine window\" 不应出现在 Abstract/Introduction 的贡献声明中**\n- 统计：p=0.28\n- Confound 校正：1.06×\n- 方向校正：OR 反转为 0.61\n\n**W6 [warning] Hacking taxonomy 验证不充分**\n- 分类器验证仅 50 样本，无 inter-annotator agreement\n- 9 类中 6 个模式样本量不足\n\n**W7 [warning] Cross-logic \"Transfer\" 措辞过强**\n- 实际只是在不同设置下重新运行，不是 transfer\n\n**W8 [warning] 训练/评估数据关系需澄清**\n- \"on identical data\" 具体指什么？\n- ISR 在训练中也被计算，held-out 的含义需明确\n\n## Questions\n\n**Q1.** STA 的 false-negative rate 是多少？\n**Q2.** premise-count-normalized ISR 作为 reward，Goodhart collapse 是否仍发生？\n**Q3.** H1 比例在训练早期（step 100）是多少？\n**Q4.** \"99.5% structural collapse\" 的精确含义？\n**Q5.** sampling decoding vs greedy decoding 对 ISR 的影响？\n\n## Missing References\n\n1. Uesato et al. (2022) \"Solving Math Word Problems with Process- and Outcome-Based Feedback\"\n2. Cobbe et al. (2021) \"Training Verifiers to Solve Math Word Problems\"\n3. Gao et al. (2023) scaling law 与 ISR Goodhart collapse 的理论连接",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-17T19:03:55.881113+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1364
}
```

</details>

---


### Assistant

_source line 774 · 2026-05-17T19:04:00.713893+00:00_

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


## Round 72

## Round 72

2 recorded events


### User

_source line 775 · 2026-05-17T19:04:03.236882+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：
- **Soundness**: 2.5/5 — 统计框架内部矛盾（CMH 免责后仍引用 p 值）、seed 数不足以刻画 stochastic bifurcation、premise-count confound 未控制、SFT 对比有 selection bias
- **Excitement**: 3.5/5 — 问题重要、STA/ISR 概念新颖，但范围受限
- **Overall**: 3.0 (Findings)

**4 个 Must-Fix 问题**：
1. 统计框架自相矛盾（先否认 CMH 有效性再引用其 p 值）
2. 5 seeds 不足以支撑 stochastic bifurcation 声明
3. Premise-count confound 根本性限制 ISR 的 "structural integrity" 解释
4. SFT 对比的 selection bias（13% vs 93-97% PR）

**4 个 Should-Fix 问题**：genuine window 不应列入核心贡献、taxonomy 验证不充分、cross-logic "transfer" 用词过强、训练/评估数据关系需澄清

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

_source line 776 · 2026-05-17T19:04:08.443113+00:00_

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


## Round 73

## Round 73

2 recorded events


### User

_source line 777 · 2026-05-17T19:06:49.553857+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### R1-W1: 统计框架内部矛盾：既否认检验有效性又引用其结果

**[AGREE] 部分同意，但论文已提供了合理的分层呈现。**

R1 指出论文承认 CMH 独立性假设违反后仍引用 p 值——这确实构成张力。但论文在 §4.3 已提供了三层统计分析的明确层级：(1) pooled Fisher（最强但假设最强）→ (2) CMH 分层（中间层，明确标注为"directional indicators, not calibrated significance levels"，见 §6 Limitations）→ (3) seed-level permutation（正确指定但 underpowered，p=0.26）。论文在 §4.3 最后一段明确写道："The transient benefit is descriptively observed but statistically underpowered at seed-level (n=5); it should not be interpreted as evidence that ISR reliably improves structural quality。"

我的判断：论文的分层呈现方式是合理的——先给 pooled 数字建立直觉，再逐步 qualify。但同意 R1 的建议：**主文应以 seed-level permutation 结果为主导**（p=0.26, n.s.），CMH p 值降至补充说明或 Appendix。当前结构容易让快速阅读的审稿人只看到 "OR=3.37" 而忽略后面的 qualification。

R1 建议的 "(a) 提供有效替代统计方法" 过于苛刻——论文已经提供了 seed-level permutation 作为替代，这正是统计上正确的方法，只是 underpowered。真正的解决方案是 R1-W2 提到的增加 seed 数。

---

### R1-W2: Seed 数量不足以支撑对随机分岔现象的声明

**[AGREE] 同意 seed 不足是真实局限，但 [REBUT] "至少需要 10-20 seeds" 的要求不切实际。**

同意方面：5 seeds 确实不足以刻画分岔的概率分布。论文自己在 §6 承认了这一点（"minimum achievable p=0.008 at n=5"）。2/5 vs 3/5 的分裂在统计上无法与随机噪声区分。

反驳方面：R1 要求 10-20 seeds。每个 GRPO seed 在 Qwen3-4B 上训练 500 steps（K=4 rollouts）需要显著的 GPU 时间。这不是一个可以轻易扩展到 20 seeds 的设置。更重要的是，**论文声称的核心 finding 并不依赖分岔的精确概率**。核心 finding 是 "ISR 在所有测试剂量下产生 Goodhart collapse"——这在 β=0.05（3 seeds, 93.7% H7）、β=0.2（3 seeds, 100% H7）下已确认，不需要 20 seeds。分岔是 β=0.1 特有的现象描述，论文将其定位为 "descriptive observation" 而非 hard claim 是合理的。

建议：增加到 8-10 seeds（β=0.1 focal dose）是可行且足够的，同时将 "stochastic bifurcation" 的措辞从 claim 降级为 observation。

---

### R1-W3: Premise-count confound 根本性限制 ISR 可解释性

**[REBUT] R1 过度泛化了 confound 的影响范围。**

关键区分：premise-count confound 影响的是 **ISR-as-reward**（§4.3），不影响 **ISR-as-diagnostic**（§4.2）。

ISR 作为诊断时的 99.5% collapse trajectory（Figure 2: ISR* 0.642→0.132→0.003）并不依赖 cross-condition ISR 比较——它是 **同一 seed 的时间序列**，比较的是同一模型在不同训练阶段的 ISR。在这个用法下，premise-count 变化本身就是 degeneration 的一部分（mean component count 6.58→18.55，§4.2），ISR 下降反映的是真实的结构崩溃（94.8% 的 proved samples 有 ISR=0）。

论文已在 §3.2 用一整段 "Limitations of ISR and the premise-count confound" 详细讨论此问题，并在 §4.3 提供 premise-count-matched comparison（1.06×），在 Appendix C 进一步分析。R1 说 "需要 premise-count-normalized ISR 变体"——这是合理的 future work 建议，但论文的诊断贡献 (C1) 不依赖 count-normalized ISR。

对于 R1 "弱化所有 structural integrity 措辞" 的要求：论文已在 §3.2 明确写道 "ISR measures syntactic component necessity, not semantic faithfulness"，并在 Appendix C 进一步 qualify。这个措辞已经足够精确。

**但同意 R1 关于 "transient genuine window is a selection effect" 的判断**——论文自己在 §4.3 提供了证据（premise-count-matched 1.06×），这进一步支持将 genuine window 从贡献声明中移除（同 R1-W5）。

---

### R1-W4: SFT baseline 对比存在系统性 selection bias

**[AGREE] 同意，我在自己的审稿中提出了相同问题（Reviewer 2 W2）。**

SFT PR=13% vs. GRPO PR=93-97% 的 selection bias 是真实的。论文的 100-step checkpoint partial control（PR=32%, hacking=31.2% vs. SFT 7.7%，Appendix F §app:100step）有帮助但不充分——32% 与 97% 仍有巨大差距。

但 R1 要求 "按问题难度分层对比" 需要更具体的建议：FOLIO 没有公开的难度标注，且 "难度" 在 neurosymbolic 设置中的定义本身就不明确（solver 难度 ≠ formalization 难度）。更可行的方向是论文已做的：在相近 PR level 下比较 hacking rate（100-step checkpoint）。

论文在 §4.2 最后一句已承认 "whether SFT would hack at higher PR remains an open question"。建议：将此 caveat 提前到 Introduction 中每次提及 SFT 对比时。

---

## Should-Fix 问题

### R1-W5: "Transient genuine window" 不应出现在 Abstract/Introduction

**[AGREE] 完全同意。我在自己的审稿中提出了相同问题（Reviewer 2 W3）。**

证据：(1) seed-level p=0.26；(2) premise-count-matched 仅 1.06×；(3) H8+FN 校正后 OR 翻转为 0.61 (n.s.)；(4) extended training 确认 window 关闭（§4.3 "Trajectory analysis"）。

Abstract 中 "the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training" 已经加了 hedge，但仍占据了 Abstract 中宝贵的 ~25 words。鉴于校正后方向翻转，这个 finding 最多只应在 §4.3 正文中描述，不应出现在 Abstract 或 Introduction 的贡献声明中。

---

### R1-W6: Hacking taxonomy 验证不充分

**[AGREE] 部分同意。**

同意分类器验证的 50 样本较少，缺少 inter-annotator agreement。但需要指出：H1/H7 分类器是 **确定性文本匹配**（normalized text matching between conclusion and premise strings，Appendix E），不是 learned classifier——对于确定性规则，传统意义上的 inter-annotator agreement 不完全适用。真正的风险在 recall 侧（false negatives），论文通过 functional cross-validation（n_necessary 分析）部分弥补了这一点，发现了 H7b 和 query-as-fact gaming。

同意 9 类中多数是孤立观察（我在 Reviewer 2 W4 也提出了此问题）。建议区分 "robust modes"（H1, H7, H8）和 "observed modes"（其余）。

---

### R1-W7: Cross-logic "Transfer" 措辞过强

**[AGREE] 同意。**

论文在 §4.4 标题用 "Cross-Logic Diagnostic Transfer"，但实际是在 Prolog 上从头运行 STA——这不是 ML 意义上的 "transfer"（没有模型/知识迁移），而是 "replication in a different logic type"。建议将 §4.4 标题改为 "Cross-Logic Replication" 或 "STA on Prolog"。

但这是措辞问题，不影响实验本身的有效性。Prolog 的三种不同 gaming pathway（H7 tautology, uppercase pseudo-Prolog, query-as-fact）是有信息量的发现。

---

### R1-W8: 训练/评估数据关系需澄清

**[REBUT] 论文已在多处提供了足够的澄清。**

- §4.1: "fixed 500-example FOLIO subset held constant across all conditions"（训练集）
- §4.1: "Held-out evaluation uses 100 FOLIO examples"（评估集）
- §4.1 footnote 1: "All experiments use train_500_seed42.jsonl; seeds control initialization and rollout sampling only"
- Appendix A: "evaluation file proofwriter_fol_100.jsonl is a legacy filename containing no ProofWriter data"
- Appendix A Table 3: Training set = "FOLIO, 500 examples", Evaluation set = "FOLIO, 100 examples (held-out)"
- "on identical data" 指 SFT 和 RL 条件使用相同的 500 训练样本——§4.1 和 Appendix A 均明确说明
- ISR 计算在 held-out 评估集上进行（Appendix A: "evaluation protocol", greedy decoding at T=0）

R1 可能因为信息分散在多个位置而遗漏。建议在 §4.1 用一句话集中说明即可。

---

## Questions 回应

### R1-Q1: STA 的 false-negative rate 是多少？

论文未给出精确的 false-negative rate，但在 Appendix E 提供了相关证据：H7b（12/89 samples in ISR β=0.1 s44 evaded text matcher），query-as-fact gaming（95/97 Prolog s44 samples evaded strict classifier）。论文明确将 non-hacking rate 定义为 "residual classification" 并标注为 upper bound（§4.1, §6）。精确的 false-negative rate 需要 exhaustive manual annotation，是 future work。

### R1-Q2: Premise-count-normalized ISR as reward, Goodhart collapse 是否仍发生？

**这是论文最显著的缺失实验。** 我在 Reviewer 2 Q1 提出了相同问题。如果 premise-count confound 是 Goodhart 的核心机制（H7 single-premise 获得 ISR≥0.5 by construction），则 count-normalized ISR 可能消除这个攻击面。论文未测试此变体，这削弱了对 ISR Goodhart vulnerability 的分析深度。但注意：即使 normalize，P→P tautology 仍然 trivially necessary（ISR_norm 仍然高），所以 Goodhart 可能仍会发生——但这需要实验验证。

### R1-Q3: H1 比例在训练早期（step 100）是多少？

**论文已回答。** Appendix F (§app:100step): 100-step checkpoint (seed 42), 32 proved samples 中 1 sample (3.1%) 是 H1, 9 samples (28.1%) 是 H7。H1 在早期很低，H7 在早期就已出现。

### R1-Q4: "99.5% structural collapse" 的精确含义？

**论文已定义。** §4.2 + Appendix D: seed 42 的 ISR* 从 step 100 的 0.642 降至 step 1000 的 0.003，下降幅度 = (0.642−0.003)/0.642 = 99.5%。这是单 seed 时间序列上的相对下降。

### R1-Q5: Sampling vs greedy decoding 对 ISR 的影响？

论文在 Appendix A 承认 exec-only s43 使用了 sampling (T=0.7) 而非 greedy，"not strictly comparable"。这是一个已知局限但仅影响一个 seed。论文未系统研究 decoding strategy 对 ISR 的影响——这是合理的 future work 但不是本文的核心问题。建议在 Table 5/6 中更显著标注此 seed。

---

## Missing References 回应

### Uesato et al. (2022) "Solving Math Word Problems with Process- and Outcome-Based Feedback"
**[AGREE]** 作为 process reward 的重要先驱工作应被引用。论文已引用 Lightman et al. (2024) 和 Math-Shepherd，但 Uesato 是 process/outcome reward 对比的奠基性工作。

### Cobbe et al. (2021) "Training Verifiers to Solve Math Word Problems"
**[REBUT] 相关性有限。** Cobbe et al. 研究的是数学文字题的 verifier training，与本文的 solver-verified neurosymbolic 设置有本质区别。论文的 Related Work 已聚焦于直接相关的 neurosymbolic + reward hacking 文献，引用 Cobbe 不会增加实质信息。

### Gao et al. (2023) scaling law 与 ISR Goodhart collapse 的理论连接
**[REBUT] 论文已引用。** Gao et al. (2023) "Scaling Laws for Reward Model Overoptimization" 已在 references.bib 中作为 `gao-reward-overoptimization` 引用，出现在 §2 Related Work ("Reward hacking and Goodhart's Law" paragraph) 和 Appendix C。R1 可能未注意到此引用。

---

## 综合判断

R1 的审稿意见整体严谨，在统计方法（W1）、SFT 对比（W4）和 transient genuine window（W5）上提出了有效批评，我在自己的审稿中也独立提出了类似问题。

R1 最值得重视的 critical issue 是 **W2 (seed 数量)** 和 **W4 (SFT selection bias)**，这两个问题确实限制了论文的 claim strength。

R1 的 W3 (premise-count confound) 虽然是真实的技术问题，但其影响范围被过度泛化——confound 主要影响 ISR-as-reward（§4.3），不影响 ISR-as-diagnostic（§4.2）。论文已在 §3.2 和 Appendix C 充分讨论了此问题。

R1 的 W8 (数据关系) 是论文已回答但信息分散的问题，不构成真实 weakness。


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

_source line 778 · 2026-05-17T19:07:04.216907+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 779 · 2026-05-17T19:07:06.765330+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**汇总**：对 R1 的 8 个 Weaknesses，我的回应分布如下：

| R1 Issue | 我的判断 | 理由 |
|----------|---------|------|
| W1 统计矛盾 | [AGREE] 部分 | 论文已分层呈现，但主文应以 seed-level permutation 为主导 |
| W2 Seed 不足 | [AGREE] 局限真实 / [REBUT] 10-20 seeds 不切实际 | 核心 Goodhart finding 不依赖分岔精确概率 |
| W3 Premise-count confound | [REBUT] | R1 过度泛化——confound 影响 ISR-as-reward 而非 ISR-as-diagnostic (C1) |
| W4 SFT selection bias | [AGREE] | 与我的 W2 一致 |
| W5 Genuine window 不应在 Abstract | [AGREE] | 与我的 W3 一致 |
| W6 Taxonomy 验证不充分 | [AGREE] 部分 | 确定性规则不需传统 IAA，但 50 样本偏少 |
| W7 Transfer 措辞 | [AGREE] | 措辞问题，不影响实验有效性 |
| W8 数据关系 | [REBUT] | 论文已在 §4.1 + Appendix A 充分说明 |

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

_source line 780 · 2026-05-17T19:07:33.874884+00:00_

Reviewer 2 的交叉回应已收到。仍在等待 Reviewer 1 对 Reviewer 2 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 75

## Round 75

10 recorded events


### User

_source line 781 · 2026-05-17T19:08:40.870473+00:00_

[Reviewer 1 审稿意见]:
# Reviewer 1 审稿意见：方法严谨性 + 实验有效性

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种对 solver 输入进行 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的神经符号证明生成器中的 reward hacking。其导出指标 Irreducible Solver Rate (ISR) 揭示了隐藏在 prove rate (97±2%) 上升背后的结构性崩溃（convergence 时 ISR→0）。当 ISR 被用作训练奖励时，在所有 4 个测试剂量下均展现 Goodhart 崩溃。论文在 2 种逻辑类型、2 个模型规模、6 种条件下记录了 9 种 hacking 模式，并提供了 observer-optimizer 不对称性的实证证据。

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**Soundness**: 2.5/5 — 方法论存在显著问题（统计框架可靠性、premise-count confound、样本量不足）
**Excitement**: 3.5/5 — 问题重要且切入角度新颖，但范围有限（单数据集、单模型家族）
**Confidence**: 4/5

**一句话总结**: 核心诊断思路（STA/ISR）有价值且填补了真实空白，但统计基础不足以支撑论文声明的强度，多处关键对比在自身 robustness check 后不成立。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | CMH 检验独立性假设被违反但仍报告 p 值；5 seeds 不足以刻画随机分叉；premise-count confound 是 ISR 的根本限制 |
| Excitement | 3.5/5 | 问题重要（execution-based evaluation 的盲区）、切入新颖（mutation-testing 思路引入 NLP），但单 dataset+单 model 限制影响力 |
| Overall | 3.0 | Findings 可接收：核心观察有价值，但需修复统计框架、降低声明强度、增加 robustness 实验 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 统计框架自相矛盾：disclaiming p-values 的同时仍依赖它们
- 具体位置：§4.2, §7 Limitations
- 问题：§7 明确承认 CMH 检验的独立性假设被违反（"CMH tests yield p<10^{-5} but assume within-stratum independence, which is violated when samples share a checkpoint and decoding strategy"），并将 CMH p-values 降级为 "directional indicators, not calibrated significance levels"。然而全文仍大量引用具体 p-values 作为证据：SFT 对比 p<0.001（§4.2）、Fisher exact test p-values（Table 5/6）、seed-level permutation test p=0.28（§4.2）。
- 为什么影响接收：一个统计框架要么有效，要么无效。当前的处理方式是 "承认问题但继续使用"，这不是可接受的方法论立场。审稿人无法判断哪些 p-values 可信、哪些不可信。
- 建议修改方向：(a) 提供一个有效的替代统计框架（如 bootstrap confidence intervals，不依赖独立性假设），或 (b) 完全移除所有 p-values，改为纯描述性报告（effect sizes + confidence intervals），或 (c) 至少明确标注每个 p-value 受影响的程度（哪些检验依赖独立性、哪些不依赖）。

**N2** [critical] Seed 数量不足以支撑核心声明
- 具体位置：§4.1-4.5, Table 1, §7
- 问题：主实验 5 seeds，dose-response 3 seeds/dose，1.7B 单 seed。论文自身在 §4.3 展示了 β=0.1 时出现随机分叉（2/5 seeds 在 ~150 步崩溃，3/5 在 500+ 步延迟崩溃），这意味着 5 seeds 可能不足以可靠地估计分叉概率。对于随机分叉现象，需要 ≥10-20 seeds 才能合理估计两个分支的占比。seed-level permutation test 的 power 极低（§7 承认 "minimum achievable p=0.008 at n=5"），意味着论文在设计上就无法检测到中等效应。
- 为什么影响接收：论文的两个核心贡献（C1: 诊断发现, C2: Goodhart 动力学刻画）都依赖于 cross-seed 一致性，但 seed 数量不足以可靠地建立这种一致性。
- 建议修改方向：(a) 增加主要条件的 seed 数量至 ≥10（至少 exec-only 和 ISR β=0.1），或 (b) 降低声明强度，将 "ISR exhibits Goodhart collapse at all four tested doses" 改为 "ISR exhibits Goodhart collapse in all observed seeds, but seed counts limit population-level inference."

**N3** [critical] Premise-count confound 根本性地限制 ISR 的解释
- 具体位置：§3.2, §4.1, §4.2
- 问题：ISR 对 component count 敏感——较短的 formalizations 机械地产生较高 ISR。§3.2 承认 "ISR measures syntactic component necessity, not semantic faithfulness"。关键影响：(1) "transient genuine window"（pooled 23% vs 8%）在 premise-count matching 后消失至 1.06×（§4.2）；(2) H7 tautology exploit（ISR≥0.5）直接利用此 confound（§3.2: "by construction"）；(3) non-collapsed seeds 产生更短的 formalizations（均值 5.58 vs 8.46 for random），inflating ISR mechanically（§4.1）。
- 为什么影响接收：论文将 ISR 框定为衡量 "structural integrity" 的指标，但 ISR 更准确地衡量的是 "relative to component count 的非冗余性"。这是一个更弱的声明。当 ISR 的核心正面发现（genuine window）经 confound 控制后消失，该指标作为诊断工具的价值需要重新评估。
- 建议修改方向：(a) 在 §3.2 中明确将 ISR 定位为 "non-redundancy metric" 而非 "structural integrity metric"；(b) 始终报告 premise-count-matched 对比作为主要结果，raw ISR 对比作为补充；(c) 讨论是否存在 premise-count-invariant 的替代指标。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SFT 对比受 PR 水平差异严重混淆
- 具体位置：§4.2
- 问题：SFT PR≈13% vs GRPO 93-97%。OR=8.41 的非 hacking 率对比存在严重选择偏差：SFT 可能仅在不需要 hacking 的 "easy" 问题上成功。论文用此对比支撑 "failure is RL-specific"（Abstract），但未控制问题难度。
- 建议：按问题难度分层对比（如按 gold proof 的 premise count 分层），或明确标注选择偏差 caveat。

**W2** [warning] "Transient genuine window" 未通过自身 robustness check 但仍出现在 Abstract/Introduction
- 具体位置：Abstract, §1 Introduction (Contributions C2), §4.2
- 问题：(1) Seed-level permutation test 不显著（p=0.28）；(2) Premise-count matching 后差异消失（1.06×）；(3) H8+FN correction 后方向翻转（OR=0.61, n.s.）。三重否定性证据，但 Abstract 和 Contributions 仍将其列为发现。
- 建议：从 Contributions 列表移除或降级为 "descriptive observation, not statistically confirmed"。Abstract 中应删除或加注 "though statistically underpowered and confound-sensitive"。

**W3** [warning] Hacking taxonomy 验证不充分
- 具体位置：§4.6, Table 2
- 问题：(1) 仅 50 样本手动验证（§4.6: "Seed 44 evades our strict classifier entirely"）；(2) 无 inter-annotator agreement 报告；(3) 无分类器 confusion matrix；(4) H1/H7/H8 占 >90%，其余 6 种模式可能是 single-seed 孤立观察；(5) Residual classification 意味着未被捕获的新 hacking 模式会被错误归入 non-hacking。
- 建议：(a) 区分 "robust modes"（H1/H7/H8）和 "observed but rare modes"；(b) 报告分类器的 precision/recall；(c) 增加手动验证样本量。

**W4** [warning] Cross-logic generalization 过度声明
- 具体位置：§4.4, Figure 4
- 问题：Prolog 实验仅 3 seeds，2/3 显示 ISR≈0。但：(a) 不同 solver（SWI-Prolog vs ProofWriter）；(b) 1/3 seed 发散；(c) 未分析是否出现相同 hacking 模式（仅 §4.4 末尾简要提及 "Prolog's simpler operational semantics providing a broader gaming basin"）；(d) 仍基于 FOLIO 数据而非独立 Prolog 数据集。
- 建议：将 "cross-logic diagnostic transfer" 降级为 "one additional data point suggesting generality."

**W5** [warning] 训练时与评估时 decoding 策略不一致
- 具体位置：§A (Appendix), §4.1
- 问题：GRPO 训练使用 sampling（temperature>0），但所有 ISR 评估使用 greedy decoding（temperature=0, Appendix A Table 3）。Sampling 下模型可能产生结构更多样的输出，greedy decoding 下的 ISR 可能系统性地偏向某些 hacking 模式。这一不一致未被讨论。
- 建议：至少在 1-2 个条件下对比 sampling vs greedy evaluation 的 ISR 分布。

---

## 小问题（不影响接收）

- Figure 2 的 y 轴标签在某些 panel 中与数据点视觉重叠
- Table 1 的注释系统过于复杂（多种符号：†, ‡, *, **），建议简化
- §3.2 讨论了 Shapley values 作为 LOO 的替代（引用 Shapley 1953），但没有解释为什么不使用——建议补充一句理由
- 论文标题 "Valid but Vacuous" 中 "valid" 有歧义：proofs 通过 solver check（execution validity）≠ logical validity（传统意义上的有效性）

---

## Questions

**Q1**: STA 的 false-negative rate 是多少？如果 solver 具有内在冗余（如逻辑上必要但 solver 可从其他 premises 导出的前提），STA 会低估 necessity。这是否被量化过？

**Q2**: 如果 ISR reward 使用 premise-count-normalized 版本（如 ISR / E[ISR | premise_count]），Goodhart collapse 是否仍然发生？H7 tautology exploit 将 component count 降到 1，归一化可能无法修复，但其他 hacking 模式呢？

**Q3**: ISR=1 的 proofs 是否一定语义正确？论文将 ISR=1 等同于 "every component is individually necessary"，但 necessary for solver success ≠ semantically correct。能否提供 ISR=1 但语义错误的反例？

**Q4**: 为什么仅在 FOLIO 上评估？即使是小规模验证（如 50-100 个 ProofWriter 原始问题、CLUTRR、或 LogiQA 的 FOL 子集），也能显著增强泛化性声明。

**Q5**: ISR 作为 rejection filter（丢弃 ISR < threshold 的样本）而非 continuous reward 是否被尝试过？这可能避免 Goodhart collapse，因为 filter 不提供优化梯度。

---

## Missing References

- **Uesato et al. (2022)** "Solving math word problems with process- and outcome-based feedback" — 直接相关 ISR 作为 process-level 诊断 vs prove rate 作为 outcome-based metric 的对比
- 论文已引用的引用覆盖总体全面（42 篇，涵盖 neurosymbolic reasoning、reward hacking、process reward models、Goodhart's Law），无明显重大遗漏

---

## 主要优势

**S1** 核心诊断思路（STA/ISR）填补真实空白：execution-based evaluation 确实无法检测结构性退化，ISR 提供了一个可操作的检测工具。mutation testing 思路从软件工程引入 NLP 是新颖的跨领域迁移。

**S2** 实验设计的自我批评精神值得肯定：论文主动报告了对自身发现不利的证据（premise-count confound、H8+FN correction 翻转、permutation test 不显著），这在 NLP 论文中相当少见。

**S3** Observer-optimizer 不对称性（"ISR reliable as diagnostic, unreliable as optimizer"）是清晰且有启发性的框架，对 reward design 有实际指导意义。

**S4** Goodhart collapse 的时间轨迹分析（§4.3, Table 1）提供了比简单 "hacking 发生了" 更丰富的信息，stochastic bifurcation 的观察对理解 RL 训练动力学有价值。

**S5** 写作质量好，无明显 AI 写作痕迹，叙事清晰度高于同领域平均水平。

---

## Detailed Comments（按章节）

**Abstract**: 信息密度适当但包含经校正后不成立的发现（genuine window）。建议修正。

**§1 Introduction**: 叙事结构完整，但 quantitative details 过多（如 p=0.187），读起来像实验报告。建议将数字移到 Results，Introduction 保持概念性叙事。

**§2 Related Work**: 覆盖全面，positioning 清晰。唯一建议：增加与 process reward model 文献（Uesato et al.）的对比讨论。

**§3 Method**: STA/ISR 定义清晰，Algorithm 1 可复现。§3.2 对 limitations 的讨论到位但应更突出（当前是 subsection 内的段落，应升级为独立 subsection 或在 §3.1 定义后紧跟 caveat）。

**§4 Experiments**: 最充实的章节。核心问题是统计推断的可靠性（如上 N1-N3）。Figure 2 有效展示了 ISR collapse trajectory。Table 1 信息丰富但注释过载。

**§5 Discussion**: 核心 takeaway（diagnostic vs optimizer）清晰。建议增加 "ISR as filter" 的讨论（见 Q5）。

**§6 Limitations**: 诚实但应更突出两点：(a) 统计 power 不足的具体影响，(b) premise-count confound 对核心发现的具体影响。

**§7 Ethics**: 将 AI safety 连接写得恰当，不过度宣传。

---

## 交叉回应 Reviewer 2

[AGREE] R2-N1: 同意 Goodhart 新颖性不足的判断方向，但认为 R2 低估了实证层面（随机分叉、非单调剂量响应）的贡献。建议论文重框而非删除 C2。

[AGREE] R2-N2: 完全同意。单一数据集是本文最大的外部有效性威胁。

[AGREE] R2-W1: 完全同意。单 seed 1.7B 与论文自身方法论矛盾。

[AGREE] R2-W2: 强烈同意。SFT 对比的选择偏差是论文的重要盲区。

[AGREE] R2-W3: 同意且补充：genuine window 不 survive 自身 robustness check，不应列为 Contribution。

[AGREE with nuance] R2-W4: 部分同意。Taxonomy 的 qualitative 价值不完全取决于每种模式的频率，但应区分 robust vs rare modes。

[REBUT] R2-M1: Abstract 信息密度适当，问题在准确性而非密度。

[REBUT] R2-M2: Introduction 长度在正常范围，问题在数字过多而非篇幅过长。

[AGREE] R2-M3/M4/M5/M6: 同意所有小问题。

R2-Q1-Q5: 所有问题都切中要害，尤其 Q1（component count 归一化）和 Q2（ISR as filter）触及了核心方法论改进方向。

R2-MR1-MR3: 无法独立验证这些引用的真实性，建议作者自行确认。

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

_source line 782 · 2026-05-17T19:09:16.955663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-17T19:09:17.008040+00:00_

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
26	  severity: critical
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
…[truncated 1059 chars]

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


### Tool call

_source line 784 · 2026-05-17T19:09:21.964754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "offset": "100"
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
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-17T19:09:22.217170+00:00_

100	  resolution: "100-step RL 对照已加入。claim 调整为 'consistent with'。"
101	  resolution_round: 2
102	
103	- id: "R2-W7"
104	  summary: "与 Kim et al. (2026) 差异化不充分"
105	  category: writing
106	  severity: warning
107	  status: resolved
108	  first_raised_round: 0
109	  last_seen_round: 2
110	  resolution: "related_work.tex 中有区分段落。"
111	  resolution_round: 2
112	
113	- id: "R1-W6"
114	  summary: "训练 500 例/评估 100 例的规模限制讨论不充分"
115	  category: experiment
116	  severity: warning
117	  status: resolved
118	  first_raised_round: 0
119	  last_seen_round: 0
120	  resolution: "limitations.tex 已讨论。"
121	  resolution_round: 2
122	
123	- id: "R1-W7"
124	  summary: "H1/H7 classifier precision/recall 未报告"
125	  category: experiment
126	  severity: info
127	  status: resolved
128	  first_raised_round: 0
129	  last_seen_round: 0
130	  resolution: "50 样本人工验证 precision >95%。"
131	  resolution_round: 2
132	
133	- id: "R1-W8"
134	  summary: "Random control U(0,1) 与 ISR 的 skewed 分布不匹配"
135	  category: method
136	  severity: info
137	  status: resolved
138	  first_raised_round: 0
139	  last_seen_round: 0
140	  resolution: "method.tex 和 experiments.tex 均说明了 Random 设计目的。"
141	  resolution_round: 2
142	
143	- id: "R1-W9"
144	  summary: "缺代码/数据开源承诺"
145	  category: format
146	  severity: info
147	  status: resolved
148	  first_raised_round: 0
149	  last_seen_round: 0
150	  resolution: "abstract.tex:9 脚注 'Code and data: [anonymized]'。"
151	  resolution_round: 2
152	
153	- id: "R1-W5"
154	  summary: "'Meta-level Goodhart' 新颖性论证不足"
155	  category: framing
156	  severity: warning
157	  status: resolved
158	  first_raised_round: 0
159	  last_seen_round: 3
160	  resolution: "framing 降级为 empirical instance。"
161	  resolution_round: 3
162	
163	- id: "R2-W8"
164	  summary: "H1/H7 编号不连贯（H2-H6 不存在）"
165	  category: writing
166	  severity: info
167	  status: resolved
168	  first_raised_round: 0
169	  last_seen_round: 3
170	  resolution: "method.tex 解释了合并原因。"
171	  resolution_round: 3
172	
173	- id: "v2-R1-N1"
…[truncated 32353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-17T19:15:16.481158+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4-9 carry-over (in_progress / open) =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W4 再次确认。§4.5 'No safe scale was observed' 仍为 n=1 seed 的存在性声明。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W6 再次确认。§4.5 title 应改为 'Preliminary Cross-Scale Evidence'。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"§4.5 标题已为 'Preliminary Cross-Scale Evidence'。R2 建议该 section 可移入 Appendix。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W2 [critical] 再次提出 1.7B 单 seed 问题。R2-W1 [AGREE] '与论文自身方法论矛盾'。R2 交叉回应中建议至少 3 seeds 或重定位为 anecdotal observation。论文已用 'Preliminary' qualifier 但仍占正文半页。\"\n  action_items:\n    - round: 7\n      action: \"§4.5 标题改为 'Preliminary Cross-Scale Evidence'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"考虑将 §4.5 内容移入 Appendix 或大幅压缩正文呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds/doses\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W4: β=0.3/0.05 仅 500-step snapshot。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"'Trajectory-confirmed' 仅 β=0.1 的 2 个 seeds。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文 Abstract 现用 'trajectory-confirmed at β=0.1'。R1 仍认为 dose-response 分析基于不均匀 seed 数。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 再次强调 seed 数不足支撑 'all four tested doses' 的 population-level inference。R2 [AGREE] 局限真实但 [REBUT] 核心 Goodhart finding 不依赖分岔精确概率——β=0.05/0.2 确认性崩溃不需更多 seeds。共识: 区分 'observed in all seeds tested' vs 'population-level inference'。\"\n  action_items:\n    - round: 7\n      action: \"Abstract/Intro 明确区分 'snapshot-observed (all doses)' vs 'trajectory-confirmed (β=0.1 only)'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"验证 Abstract 是否已清晰区分; §4.3 末段弱化为 descriptive pattern\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"统计层级倒置; OR 反转正文一句带过。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"CMH OR=3.37 方向与 5-seed Fisher 一致但 framing 不诚实。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"CMH OR=3.37 正文出现 3 次 vs corrected OR=0.61 仅 2 次且靠后。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文现有 'suggestive but non-robust' 措辞，但 Table 1 N-H=23%* 仍为 headline。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W5/R2-W3 均 [AGREE]: genuine window 在三个维度上均未通过检验 (p=0.26, 1.06× matched, OR reversal)。共识: 从 Abstract/Contributions 完全移除 genuine window，仅在 §4.3 作描述性保留。\"\n  action_items:\n    - round: 8\n      action: \"强化执行: Abstract 删除 '23% vs 8%' 对比; Table 1 caption 注明 corrected estimate; §4.3 headline 改为 seed-level p=0.26\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"CMH 检验的 within-seed 非独立性问题——真实独立样本量为 n=5 (seeds) 而非 n=350/414 (samples)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N5 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文已在 experiments.tex:98 承认但 CMH 仍在正文核心段落。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N1 [critical]: '先否认检验有效性再引用其结果'。R2 [AGREE 部分]: 论文已提供三层分析（pooled Fisher → CMH → seed-level permutation）但主文应以 seed-level 为主导。共识: CMH 降至 Appendix，正文以 seed-level permutation (p=0.26, n.s.) 为 primary。R2 rebuts '提供有效替代统计方法' 要求——permutation test 已是正确方法，只是 underpowered。\"\n  action_items:\n    - round: 8\n      action: \"CMH OR/p 从正文移至 Appendix; 正文仅报告 seed-level permutation p=0.26\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解释原因。\"\n    - round: 6\n      reviewers: [1]\n      note: \"s43 数据仍用于主文 claims。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被直接提及。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被直接提及。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-M5 提及 sampling eval s43 在 Appendix D 中应更显著标注或排除。R1 交叉回应: 已知局限仅影响一个 seed。\"\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"5-seed pooled N-H=23% 为未校正上限。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议报告区间 [6%, 23%]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"3.7× 差距。Table 1 ‡ 标注不够显著。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Table 1 ‡ 标注存在但需更醒目。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 紧密关联。Table 1 N-H=23%‡ 仍是 headline 数字而 corrected 6.06% 仅在 Appendix。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 caption 明确说明 N-H=23% is uncorrected upper bound; corrected=6.06%\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"per-seed proved n=18-94，百分比信息量低。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"n=18 (β=0.3 s42) 时 CI 极宽。\"\n    - round: 8\n      reviewers: [1]\n      note: \"训练 500 样本可能使 hacking 更容易。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q5: 500 examples 是否太小导致 GRPO 更容易过拟合到 degenerate 策略？R1-Q4: ISR=0 在 LOO 下意味着每个 component 可移除——在 100 例中需确认。\"\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 升级为 critical。R1 [REBUT]。降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"应更明确 position 为 empirical study。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"共识: 不扣重分但确认 novelty ceiling。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 从新角度重提: Goodhart collapse 可预测。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]: C2 作为最大篇幅贡献但核心可预测。R1 [AGREE with nuance]: empirical 价值在于 calibrating 预测。共识: reframe C2 为 'empirical characterization of a predictable failure'，突出真正不可预测的部分（bifurcation dynamics, mode diversity）。\"\n  action_items:\n    - round: 6\n      action: \"Introduction 中更明确 position 为 empirical study\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Appendix Table 5 现含完整 5-seed per-seed data。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议 Table 1 增加 exec-only 3-seed 1000-step 行。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Table 1 已有 exec-only 1000-step 3-seed 行但 500-step 仍单 seed。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"exec-only 500-step 仍 s42 单 seed (†)。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M4 Table 1 注释复杂度再次被提及。R1 交叉 [AGREE] R2-M4。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 exec-only 500-step 行改为 3-seed pooled 或在 caption 注明原因\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R1 Excitement=3.5 部分不同意。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N2 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议更明确将实验定位为 verification + discovery。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"建议将贡献重心从 'discovering collapse' 转移到 'characterizing collapse dynamics'。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical] 提升强度。R1 [AGREE with nuance]。核心建议不变: C2 reframe 为 empirical characterization。\"\n  action_items:\n    - round: 6\n      action: \"Framing 从 'we discover Goodhart effects' 转为 'Goodhart collapse is predictable, but these phenomena are not: [...]'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~15 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N3 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"手动计数 11 个数值/统计量。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍含 ~10 个具体数字。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M1: 审稿人 30 秒内难以抓住 takeaway。R1 [REBUT] 认为问题在准确性（genuine window）而非密度。两位共识: 至少删除 genuine window 相关数字 (23% vs 8%)。\"\n  action_items:\n    - round: 7\n      action: \"Abstract 删减至 ≤6 关键数字\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 paragraph{} 小标题切割连贯叙事。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [REBUT]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 [AGREE]: 建议合并 paragraphs。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-M2: Introduction 过长 (2+ 页)，过载定量结果。R1 [REBUT] 篇幅正常但 [AGREE] 数字过多。\"\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复且顺序非升序\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"四段格式高度重复。\"\n    - round: 6\n      reviewers: [2]\n      note: \"β 呈现顺序 0.1→0.05→0.2→0.3。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议开头加总结性发现，按升序呈现。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接提及。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 开头加总结; 按升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"100-step RL (PR=32%) 部分缓解但不完全。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"C1 'localizing the failure to RL' 证据链有 PR confound。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"论文 framing 已 cautious。维持 warning。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 补充: SFT 使用 gold formalizations vs GRPO self-generated rollouts 混淆算法和标签质量。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W4 [major]: 经典 selection bias。R2-W2 [AGREE]。两位共识: 不要求新实验，但 Introduction/Abstract 每次提及 SFT 对比时必须加 PR-level caveat。R2 交叉回应补充: FOLIO 无公开难度标注，难以按难度分层。\"\n  action_items:\n    - round: 8\n      action: \"正文 §4.2 SFT 段增加 gold-label confound 讨论\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Krakovna, Polu & Sutskever, Everitt。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"已加入。R2 新建议。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 建议增加 Goodhart 1975。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Goodhart 1975 已加入。R1 建议 Ng 1999, Kim 2026 差异化。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1: Uesato et al. (2022) process vs outcome feedback 应引用。R2 [AGREE]。R2: Khalaf et al. NeurIPS 2025 inference-time reward hacking。R1/R2 共识: Cobbe et al. (2021) 相关性有限。Ng 1999 已在 related_work.tex 引用（R2 交叉回应确认）。\"\n  action_items:\n    - round: 9\n      action: \"(a) 增加 Uesato et al. (2022) 引用; (b) 考虑增加 Khalaf et al. NeurIPS 2025\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"caption ~120 words + 6 脚注标记。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议简化脚注。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 建议拆分 Table 1 为 primary + cross-scale。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M4 再次确认注释系统过复杂 (†, ‡, ††, ★)。R1 小问题中 [AGREE]。\"\n  action_items:\n    - round: 8\n      action: \"拆分 Table 1: primary conditions + 1.7B 单独成表或移 Appendix\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex:20 现已指定 'primarily regressional, with extremal elements'。\"\n  resolution_round: 7\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"experiments.tex:91-94 现已包含 reward landscape 分析。\"\n  resolution_round: 7\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"全文统一使用 Irreducible Solver Rate。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"ISR 统一为 'Irreducible Solver Rate'。\"\n  resolution_round: 7\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 基于 4 个 β 值、不均匀 seed 数，统计上不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"β=0.1 用 5 seeds 而其他用 3 seeds。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议弱化为 descriptive pattern。\"\n    - round: 8\n      reviewers: [1]\n      note: \"dose-response 的表述过强。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 再次引用不均匀 seed 数问题。R2 交叉回应 [AGREE] 局限真实但核心 finding 不依赖精确概率。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 'Non-monotonic dose-response' 弱化为 descriptive pattern\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 的 β 值呈现顺序非升序\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"升序呈现更清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"与 v5-R2-W4 合并。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接提及。\"\n  action_items:\n    - round: 7\n      action: \"与 v5-R2-W4 合并: 按 β 升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"introduction.tex:14 现为 'component necessity testing (leave-one-out (LOO) ablation on solver inputs)'。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled，部分 mode 为单点观察\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Director 裁决降级为 info→warning。\"\n    - round: 7\n      reviewers: [1]\n      note: \"R1-Q6 提及。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"建议区分 robust vs isolated modes。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W6/R2-W4 均再次提出。R2 [AGREE 部分]——H1/H7 deterministic rules 不需 IAA 但 50 样本偏少。R1 补充: residual classification inflate non-hacking rate, 无 confusion matrix。共识: 区分 robust (H1/H7/H8) vs observed (其余), 增加手动验证样本量。\"\n  action_items:\n    - round: 8\n      action: \"Table 2 或正文区分 'robust modes' vs 'isolated observations'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v7-R1-N2\"\n  summary: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate，需 cluster-robust 重分析\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 提出 [critical], R2 [AGREE]。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"与 v4-R1-N4 合并。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"合并到 v4-R1-N4 处理。R1-N1 是最强版本: '先免责再引用'。\"\n  action_items:\n    - round: 8\n      action: \"合并到 v4-R1-N4 修复方案执行\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v7-R2-MR1\"\n  summary: \"缺少 Goodhart's Law 经典引用 (Goodhart 1975)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"references.bib 现已包含 Goodhart 1975。\"\n  resolution_round: 8\n\n- id: \"v7-R2-W7\"\n  summary: \"experiments.tex 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"单处出现。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n    - round: 9\n      reviewers: []\n      note: \"R2 全面 AI 痕迹检查通过。主文无 AI 写作痕迹。此 issue 可能已自行修复。\"\n  action_items:\n    - round: 7\n      action: \"删除 'Notably'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== Round 8 issues (continued) =====\n\n- id: \"v8-R12-N1\"\n  summary: \"核心 Goodhart 发现的可预测性：ISR≥0.5 for tautologies 从定义即可推导，限制了概念新颖性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]。R1 [AGREE with nuance]。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical] 再次强调: '一阶可预测结果的二阶细节'。R1 [AGREE with nuance]: 可预测=方向, 不可预测=速度/幅度/模式多样性。R2 交叉回应 [AGREE] R1 低估了 empirical 层面。共识: reframe C2 为 'empirical characterization of a predictable failure'，诊断 (C1) 应成为 primary contribution。\"\n  action_items:\n    - round: 8\n      action: \"Abstract/Contributions 将 Goodhart 崩溃定位为 'empirical characterization of a predictable failure'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-N3\"\n  summary: \"'Genuine'/'non-hacking'/'structurally sound' 术语交替使用导致语义滑移\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"建议统一为 'non-hacking'。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1 小问题中提到 'valid' 有歧义 (execution validity vs logical validity)。R2 未直接提及但 R2-N1 引用 'structurally sound' 作为 Abstract 中的术语问题。\"\n  action_items:\n    - round: 8\n      action: \"全文统一使用 'non-hacking'; Abstract 'structurally sound' 改为 'non-hacking'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R12-N2\"\n  summary: \"实验范围 (Qwen3 + FOLIO) 与标题/claim scope ('Neurosymbolic Proof Generation') 不匹配\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"建议增加实验或收窄标题。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]: 标题泛化跳跃过大。R1 [AGREE]。R1-Q4: 为什么仅 FOLIO？50-100 ProofWriter/LogiQA 样本也能增强。R2-Q4: 不同模型家族 (Llama, Gemma) 是否本质不同？R2-Q5: 训练数据规模影响？共识: 若 deadline 前无法增加实验，收窄标题为 'GRPO-Trained Formalizers' 或 'First-Order Logic NLI'。\"\n  action_items:\n    - round: 8\n      action: \"收窄标题或增加实验\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-W4\"\n  summary: \"多重比较未校正 (Fisher exact tests across 6+ comparisons)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"形式规范问题。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1 再次提及但未升级。R2 交叉回应 [AGREE] 但实际影响有限。\"\n  action_items:\n    - round: 8\n      action: \"Appendix 增加 Bonferroni-corrected p 值或正文脚注讨论\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-MR\"\n  summary: \"缺少 reward shaping 和 inference-time hacking 引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Ng 1999 + Kim 2026 差异化。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1: Uesato et al. (2022) 应引用。R2: Khalaf et al. NeurIPS 2025。Ng 1999 已引用。Kim 2026 差异化已存在但可加强。R2 交叉回应: Cobbe 2021 相关性有限; Gao 2023 已引用。\"\n  action_items:\n    - round: 9\n      action: \"(a) 增加 Uesato et al. (2022); (b) 考虑 Khalaf et al. NeurIPS 2025; (c) Kim 2026 差异化扩展 2-3 句\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== Round 9 新 issues =====\n\n- id: \"v9-R1-N3\"\n  summary: \"Premise-count confound 对 ISR-as-diagnostic 的影响范围存在分歧\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W3 [critical]: ISR 应定位为 'non-redundancy metric' 而非 'structural integrity metric'，confound 影响所有用途。R2 [REBUT]: confound 主要影响 ISR-as-reward (§4.3)，不影响 ISR-as-diagnostic (§4.2)——99.5% collapse trajectory 是同 seed 时间序列，premise-count 变化本身是 degeneration 的一部分。分歧记录: R1 认为影响全局，R2 认为仅影响 cross-condition 比较。Director 裁决: R2 的区分有道理——C1 诊断贡献不依赖 cross-condition ISR 比较，但论文应在 §3.2 进一步澄清 ISR 在不同使用场景下的 confound 影响差异。\"\n  action_items:\n    - round: 9\n      action: \"§3.2 增加 1-2 句明确区分: (a) ISR 用于 within-seed 时间序列诊断时 confound 不影响核心发现; (b) ISR 用于 cross-condition 比较时需 premise-count matching\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v9-R12-W1\"\n  summary: \"§4.4 标题 'Cross-Logic Diagnostic Transfer' 措辞过强\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W7 [warning]: 实际只是在不同设置下重新运行，非 ML 意义上的 transfer。R2 交叉回应 [AGREE]: 建议改为 'Cross-Logic Replication' 或 'STA on Prolog'。两位共识: 措辞问题不影响实验有效性。\"\n  action_items:\n    - round: 9\n      action: \"§4.4 标题改为 'Cross-Logic Replication' 或类似描述性表述\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v9-R1-W5\"\n  summary: \"训练时 sampling vs 评估时 greedy decoding 策略不一致未被讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5 [warning]: GRPO 训练用 sampling，ISR 评估用 greedy (T=0)。Sampling 下模型可能产生更多样输出，greedy 下可能系统性偏向某些 hacking 模式。R2 交叉回应未直接反驳此点。\"\n  action_items:\n    - round: 9\n      action: \"§4.1 或 Appendix A 增加 1-2 句讨论 training vs evaluation decoding 不一致的潜在影响\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v9-R12-Q-ISR-FILTER\"\n  summary: \"ISR 作为 filter (reject threshold) 而非 continuous reward 未测试\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-Q5/R2-Q2: ISR 作为 rejection filter 而非 reward signal 可能避免 Goodhart collapse（filter 不提供优化梯度）。R2 交叉回应: 这是论文最显著的缺失实验。但 filter 在 RL 训练循环中的实现方式和可行性未被讨论。标记为 future work 方向。\"\n  action_items:\n    - round: 9\n      action: \"§5 Discussion 增加 1 句讨论 ISR-as-filter 的可能方向\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v9-R12-Q-NORMALIZED-ISR\"\n  summary: \"未测试 premise-count-normalized ISR 作为 reward\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-Q2/R2-Q1: 如果 premise-count confound 是 Goodhart 核心机制，归一化可能消除或减弱攻击面。R2 交叉回应: 即使 normalize，P→P tautology 仍 trivially necessary (ISR_norm 仍高)，但需实验验证。标记为 future work。\"\n  action_items:\n    - round: 9\n      action: \"§5 Discussion 或 §3.2 增加讨论 count-normalized ISR 的可能性和局限\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
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
    "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"R2 确认 em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。AI 痕迹基本清除。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4-9 carry-over (in_progress / open) =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验仅 1 seed (Qwen3-1.7B seed 42)，claim 措辞过强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Discussion 措辞仍过强 ('no safe scale exists')。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W2 再次确认。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W4 再次确认。§4.5 'No safe scale was observed' 仍为 n=1 seed 的存在性声明。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3/R2-W6 再次确认。§4.5 title 应改为 'Preliminary Cross-Scale Evidence'。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"§4.5 标题已为 'Preliminary Cross-Scale Evidence'。R2 建议该 section 可移入 Appendix。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W2 [critical] 再次提出 1.7B 单 seed 问题。R2-W1 [AGREE] '与论文自身方法论矛盾'。R2 交叉回应中建议至少 3 seeds 或重定位为 anecdotal observation。论文已用 'Preliminary' qualifier 但仍占正文半页。\"\n  action_items:\n    - round: 7\n      action: \"§4.5 标题改为 'Preliminary Cross-Scale Evidence'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"考虑将 §4.5 内容移入 Appendix 或大幅压缩正文呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据——trajectory evidence 仅部分 seeds/doses\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"s45/s46 未延伸训练。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"β=0.3 无 1000-step trajectory。β=0.1 仅 s42/s45 有 1000-step。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W4: β=0.3/0.05 仅 500-step snapshot。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"'Trajectory-confirmed' 仅 β=0.1 的 2 个 seeds。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文 Abstract 现用 'trajectory-confirmed at β=0.1'。R1 仍认为 dose-response 分析基于不均匀 seed 数。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 再次强调 seed 数不足支撑 'all four tested doses' 的 population-level inference。R2 [AGREE] 局限真实但 [REBUT] 核心 Goodhart finding 不依赖分岔精确概率——β=0.05/0.2 确认性崩溃不需更多 seeds。共识: 区分 'observed in all seeds tested' vs 'population-level inference'。\"\n  action_items:\n    - round: 7\n      action: \"Abstract/Intro 明确区分 'snapshot-observed (all doses)' vs 'trajectory-confirmed (β=0.1 only)'\"\n      assigned_to: \"paper_agent\"\n      status: done\n    - round: 8\n      action: \"验证 Abstract 是否已清晰区分; §4.3 末段弱化为 descriptive pattern\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，主文 framing 不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Abstract/Intro 以 5-seed OR=3.48 为 headline。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"统计层级倒置; OR 反转正文一句带过。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"CMH OR=3.37 方向与 5-seed Fisher 一致但 framing 不诚实。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"CMH OR=3.37 正文出现 3 次 vs corrected OR=0.61 仅 2 次且靠后。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文现有 'suggestive but non-robust' 措辞，但 Table 1 N-H=23%* 仍为 headline。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W5/R2-W3 均 [AGREE]: genuine window 在三个维度上均未通过检验 (p=0.26, 1.06× matched, OR reversal)。共识: 从 Abstract/Contributions 完全移除 genuine window，仅在 §4.3 作描述性保留。\"\n  action_items:\n    - round: 8\n      action: \"强化执行: Abstract 删除 '23% vs 8%' 对比; Table 1 caption 注明 corrected estimate; §4.3 headline 改为 seed-level p=0.26\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-N4\"\n  summary: \"CMH 检验的 within-seed 非独立性问题——真实独立样本量为 n=5 (seeds) 而非 n=350/414 (samples)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"seed 为分析单元 n=5 达不到 p<10⁻⁸。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 合并：CMH 已存在但被埋附录。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-N5 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文已在 experiments.tex:98 承认但 CMH 仍在正文核心段落。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N1 [critical]: '先否认检验有效性再引用其结果'。R2 [AGREE 部分]: 论文已提供三层分析（pooled Fisher → CMH → seed-level permutation）但主文应以 seed-level 为主导。共识: CMH 降至 Appendix，正文以 seed-level permutation (p=0.26, n.s.) 为 primary。R2 rebuts '提供有效替代统计方法' 要求——permutation test 已是正确方法，只是 underpowered。\"\n  action_items:\n    - round: 8\n      action: \"CMH OR/p 从正文移至 Appendix; 正文仅报告 seed-level permutation p=0.26\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"† 标记语义矛盾。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解释原因。\"\n    - round: 6\n      reviewers: [1]\n      note: \"s43 数据仍用于主文 claims。\"\n    - round: 7\n      reviewers: []\n      note: \"本轮未被直接提及。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被直接提及。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-M5 提及 sampling eval s43 在 Appendix D 中应更显著标注或排除。R1 交叉回应: 已知局限仅影响一个 seed。\"\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Appendix 承认但主表未标注。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"5-seed pooled N-H=23% 为未校正上限。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议报告区间 [6%, 23%]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"3.7× 差距。Table 1 ‡ 标注不够显著。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Table 1 ‡ 标注存在但需更醒目。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"与 v4-R12-N3 紧密关联。Table 1 N-H=23%‡ 仍是 headline 数字而 corrected 6.06% 仅在 Appendix。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 caption 明确说明 N-H=23% is uncorrected upper bound; corrected=6.06%\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Limitations 已讨论但正文 claims 仍暗示 general 结论。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"per-seed proved n=18-94，百分比信息量低。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"n=18 (β=0.3 s42) 时 CI 极宽。\"\n    - round: 8\n      reviewers: [1]\n      note: \"训练 500 样本可能使 hacking 更容易。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q5: 500 examples 是否太小导致 GRPO 更容易过拟合到 degenerate 策略？R1-Q4: ISR=0 在 LOO 下意味着每个 component 可移除——在 100 例中需确认。\"\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2-N2 升级为 critical。R1 [REBUT]。降级为 warning。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"应更明确 position 为 empirical study。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"共识: 不扣重分但确认 novelty ceiling。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 从新角度重提: Goodhart collapse 可预测。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]: C2 作为最大篇幅贡献但核心可预测。R1 [AGREE with nuance]: empirical 价值在于 calibrating 预测。共识: reframe C2 为 'empirical characterization of a predictable failure'，突出真正不可预测的部分（bifurcation dynamics, mode diversity）。\"\n  action_items:\n    - round: 6\n      action: \"Introduction 中更明确 position 为 empirical study\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 和 H7a prevalence 段仍用 3-seed 数据\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Appendix Table 5 现含完整 5-seed per-seed data。确认已修复。\"\n  resolution_round: 7\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称: exec-only 单 seed vs ISR/Random 5-seed pooled\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议 Table 1 增加 exec-only 3-seed 1000-step 行。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Table 1 已有 exec-only 1000-step 3-seed 行但 500-step 仍单 seed。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"exec-only 500-step 仍 s42 单 seed (†)。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M4 Table 1 注释复杂度再次被提及。R1 交叉 [AGREE] R2-M4。\"\n  action_items:\n    - round: 7\n      action: \"Table 1 exec-only 500-step 行改为 3-seed pooled 或在 caption 注明原因\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限——Goodhart's Law 的直接推论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R1 Excitement=3.5 部分不同意。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N2 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议更明确将实验定位为 verification + discovery。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"建议将贡献重心从 'discovering collapse' 转移到 'characterizing collapse dynamics'。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical] 提升强度。R1 [AGREE with nuance]。核心建议不变: C2 reframe 为 empirical characterization。\"\n  action_items:\n    - round: 6\n      action: \"Framing 从 'we discover Goodhart effects' 转为 'Goodhart collapse is predictable, but these phenomena are not: [...]'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 (~15 个数字/统计量)，读感像实验报告\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"~220 words 含 12+ 数字。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-N3 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"手动计数 11 个数值/统计量。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍含 ~10 个具体数字。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M1: 审稿人 30 秒内难以抓住 takeaway。R1 [REBUT] 认为问题在准确性（genuine window）而非密度。两位共识: 至少删除 genuine window 相关数字 (23% vs 8%)。\"\n  action_items:\n    - round: 7\n      action: \"Abstract 删减至 ≤6 关键数字\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W3\"\n  summary: \"Introduction 过度使用 paragraph{} 导致叙事碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"5 个 paragraph{} 小标题切割连贯叙事。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出。R1 [REBUT]。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 [AGREE]: 建议合并 paragraphs。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-M2: Introduction 过长 (2+ 页)，过载定量结果。R1 [REBUT] 篇幅正常但 [AGREE] 数字过多。\"\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值逐一报告，格式重复且顺序非升序\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"四段格式高度重复。\"\n    - round: 6\n      reviewers: [2]\n      note: \"β 呈现顺序 0.1→0.05→0.2→0.3。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议开头加总结性发现，按升序呈现。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接提及。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 开头加总结; 按升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound 仍不充分控制 (PR=13% vs 93%)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"100-step RL (PR=32%) 部分缓解但不完全。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"C1 'localizing the failure to RL' 证据链有 PR confound。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"论文 framing 已 cautious。维持 warning。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 补充: SFT 使用 gold formalizations vs GRPO self-generated rollouts 混淆算法和标签质量。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W4 [major]: 经典 selection bias。R2-W2 [AGREE]。两位共识: 不要求新实验，但 Introduction/Abstract 每次提及 SFT 对比时必须加 PR-level caveat。R2 交叉回应补充: FOLIO 无公开难度标注，难以按难度分层。\"\n  action_items:\n    - round: 8\n      action: \"正文 §4.2 SFT 段增加 gold-label confound 讨论\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Krakovna, Polu & Sutskever, Everitt。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"已加入。R2 新建议。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 建议增加 Goodhart 1975。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Goodhart 1975 已加入。R1 建议 Ng 1999, Kim 2026 差异化。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1: Uesato et al. (2022) process vs outcome feedback 应引用。R2 [AGREE]。R2: Khalaf et al. NeurIPS 2025 inference-time reward hacking。R1/R2 共识: Cobbe et al. (2021) 相关性有限。Ng 1999 已在 related_work.tex 引用（R2 交叉回应确认）。\"\n  action_items:\n    - round: 9\n      action: \"(a) 增加 Uesato et al. (2022) 引用; (b) 考虑增加 Khalaf et al. NeurIPS 2025\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高，可读性差\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Caption 7 行。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"caption ~120 words + 6 脚注标记。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议简化脚注。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 建议拆分 Table 1 为 primary + cross-scale。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M4 再次确认注释系统过复杂 (†, ‡, ††, ★)。R1 小问题中 [AGREE]。\"\n  action_items:\n    - round: 8\n      action: \"拆分 Table 1: primary conditions + 1.7B 单独成表或移 Appendix\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant (regressional/extremal/causal/adversarial) 未指定\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex:20 现已指定 'primarily regressional, with extremal elements'。\"\n  resolution_round: 7\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"experiments.tex:91-94 现已包含 reward landscape 分析。\"\n  resolution_round: 7\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"全文统一使用 Irreducible Solver Rate。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"ISR 统一为 'Irreducible Solver Rate'。\"\n  resolution_round: 7\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 基于 4 个 β 值、不均匀 seed 数，统计上不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"β=0.1 用 5 seeds 而其他用 3 seeds。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"建议弱化为 descriptive pattern。\"\n    - round: 8\n      reviewers: [1]\n      note: \"dose-response 的表述过强。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 再次引用不均匀 seed 数问题。R2 交叉回应 [AGREE] 局限真实但核心 finding 不依赖精确概率。\"\n  action_items:\n    - round: 7\n      action: \"§4.3 'Non-monotonic dose-response' 弱化为 descriptive pattern\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 的 β 值呈现顺序非升序\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"升序呈现更清晰。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"与 v5-R2-W4 合并。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接提及。\"\n  action_items:\n    - round: 7\n      action: \"与 v5-R2-W4 合并: 按 β 升序呈现\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"introduction.tex:14 现为 'component necessity testing (leave-one-out (LOO) ablation on solver inputs)'。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled，部分 mode 为单点观察\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Director 裁决降级为 info→warning。\"\n    - round: 7\n      reviewers: [1]\n      note: \"R1-Q6 提及。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"建议区分 robust vs isolated modes。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W6/R2-W4 均再次提出。R2 [AGREE 部分]——H1/H7 deterministic rules 不需 IAA 但 50 样本偏少。R1 补充: residual classification inflate non-hacking rate, 无 confusion matrix。共识: 区分 robust (H1/H7/H8) vs observed (其余), 增加手动验证样本量。\"\n  action_items:\n    - round: 8\n      action: \"Table 2 或正文区分 'robust modes' vs 'isolated observations'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"v7-R1-N2\"\n  summary: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate，需 cluster-robust 重分析\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 提出 [critical], R2 [AGREE]。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"与 v4-R1-N4 合并。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"合并到 v4-R1-N4 处理。R1-N1 是最强版本: '先免责再引用'。\"\n  action_items:\n    - round: 8\n      action: \"合并到 v4-R1-N4 修复方案执行\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v7-R2-MR1\"\n  summary: \"缺少 Goodhart's Law 经典引用 (Goodhart 1975)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"references.bib 现已包含 Goodhart 1975。\"\n  resolution_round: 8\n\n- id: \"v7-R2-W7\"\n  summary: \"experiments.tex 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"单处出现。\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未直接提及。\"\n    - round: 9\n      reviewers: []\n      note: \"R2 全面 AI 痕迹检查通过。主文无 AI 写作痕迹。此 issue 可能已自行修复。\"\n  action_items:\n    - round: 7\n      action: \"删除 'Notably'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== Round 8 issues (continued) =====\n\n- id: \"v8-R12-N1\"\n  summary: \"核心 Goodhart 发现的可预测性：ISR≥0.5 for tautologies 从定义即可推导，限制了概念新颖性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]。R1 [AGREE with nuance]。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical] 再次强调: '一阶可预测结果的二阶细节'。R1 [AGREE with nuance]: 可预测=方向, 不可预测=速度/幅度/模式多样性。R2 交叉回应 [AGREE] R1 低估了 empirical 层面。共识: reframe C2 为 'empirical characterization of a predictable failure'，诊断 (C1) 应成为 primary contribution。\"\n  action_items:\n    - round: 8\n      action: \"Abstract/Contributions 将 Goodhart 崩溃定位为 'empirical characterization of a predictable failure'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-N3\"\n  summary: \"'Genuine'/'non-hacking'/'structurally sound' 术语交替使用导致语义滑移\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"建议统一为 'non-hacking'。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1 小问题中提到 'valid' 有歧义 (execution validity vs logical validity)。R2 未直接提及但 R2-N1 引用 'structurally sound' 作为 Abstract 中的术语问题。\"\n  action_items:\n    - round: 8\n      action: \"全文统一使用 'non-hacking'; Abstract 'structurally sound' 改为 'non-hacking'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R12-N2\"\n  summary: \"实验范围 (Qwen3 + FOLIO) 与标题/claim scope ('Neurosymbolic Proof Generation') 不匹配\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"建议增加实验或收窄标题。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]: 标题泛化跳跃过大。R1 [AGREE]。R1-Q4: 为什么仅 FOLIO？50-100 ProofWriter/LogiQA 样本也能增强。R2-Q4: 不同模型家族 (Llama, Gemma) 是否本质不同？R2-Q5: 训练数据规模影响？共识: 若 deadline 前无法增加实验，收窄标题为 'GRPO-Trained Formalizers' 或 'First-Order Logic NLI'。\"\n  action_items:\n    - round: 8\n      action: \"收窄标题或增加实验\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-W4\"\n  summary: \"多重比较未校正 (Fisher exact tests across 6+ comparisons)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"形式规范问题。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1 再次提及但未升级。R2 交叉回应 [AGREE] 但实际影响有限。\"\n  action_items:\n    - round: 8\n      action: \"Appendix 增加 Bonferroni-corrected p 值或正文脚注讨论\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v8-R1-MR\"\n  summary: \"缺少 reward shaping 和 inference-time hacking 引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Ng 1999 + Kim 2026 差异化。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1: Uesato et al. (2022) 应引用。R2: Khalaf et al. NeurIPS 2025。Ng 1999 已引用。Kim 2026 差异化已存在但可加强。R2 交叉回应: Cobbe 2021 相关性有限; Gao 2023 已引用。\"\n  action_items:\n    - round: 9\n      action: \"(a) 增加 Uesato et al. (2022); (b) 考虑 Khalaf et al. NeurIPS 2025; (c) Kim 2026 差异化扩展 2-3 句\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== Round 9 新 issues =====\n\n- id: \"v9-R1-N3\"\n  summary: \"Premise-count confound 对 ISR-as-diagnostic 的影响范围存在分歧\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W3 [critical]: ISR 应定位为 'non-redundancy metric' 而非 'structural integrity metric'，confound 影响所有用途。R2 [REBUT]: confound 主要影响 ISR-as-reward (§4.3)，不影响 ISR-as-diagnostic (§4.2)——99.5% collapse trajectory 是同 seed 时间序列，premise-count 变化本身是 degeneration 的一部分。分歧记录: R1 认为影响全局，R2 认为仅影响 cross-condition 比较。Director 裁决: R2 的区分有道理——C1 诊断贡献不依赖 cross-condition ISR 比较，但论文应在 §3.2 进一步澄清 ISR 在不同使用场景下的 confound 影响差异。\"\n  action_items:\n    - round: 9\n      action: \"§3.2 增加 1-2 句明确区分: (a) ISR 用于 within-seed 时间序列诊断时 confound 不影响核心发现; (b) ISR 用于 cross-condition 比较时需 premise-count matching\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v9-R12-W1\"\n  summary: \"§4.4 标题 'Cross-Logic Diagnostic Transfer' 措辞过强\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W7 [warning]: 实际只是在不同设置下重新运行，非 ML 意义上的 transfer。R2 交叉回应 [AGREE]: 建议改为 'Cross-Logic Replication' 或 'STA on Prolog'。两位共识: 措辞问题不影响实验有效性。\"\n  action_items:\n    - round: 9\n      action: \"§4.4 标题改为 'Cross-Logic Replication' 或类似描述性表述\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v9-R1-W5\"\n  summary: \"训练时 sampling vs 评估时 greedy decoding 策略不一致未被讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5 [warning]: GRPO 训练用 sampling，ISR 评估用 greedy (T=0)。Sampling 下模型可能产生更多样输出，greedy 下可能系统性偏向某些 hacking 模式。R2 交叉回应未直接反驳此点。\"\n  action_items:\n    - round: 9\n      action: \"§4.1 或 Appendix A 增加 1-2 句讨论 training vs evaluation decoding 不一致的潜在影响\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v9-R12-Q-ISR-FILTER\"\n  summary: \"ISR 作为 filter (reject threshold) 而非 continuous reward 未测试\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-Q5/R2-Q2: ISR 作为 rejection filter 而非 reward signal 可能避免 Goodhart collapse（filter 不提供优化梯度）。R2 交叉回应: 这是论文最显著的缺失实验。但 filter 在 RL 训练循环中的实现方式和可行性未被讨论。标记为 future work 方向。\"\n  action_items:\n    - round: 9\n      action: \"§5 Discussion 增加 1 句讨论 ISR-as-filter 的可能方向\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v9-R12-Q-NORMALIZED-ISR\"\n  summary: \"未测试 premise-count-normalized ISR 作为 reward\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-Q2/R2-Q1: 如果 premise-count confound 是 Goodhart 核心机制，归一化可能消除或减弱攻击面。R2 交叉回应: 即使 normalize，P→P tautology 仍 trivially necessary (ISR_norm 仍高)，但需实验验证。标记为 future work。\"\n  action_items:\n    - round: 9\n      action: \"§5 Discussion 或 §3.2 增加讨论 count-normalized ISR 的可能性和局限\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-17T19:15:16.632838+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 35489}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-17T19:17:40.688942+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "solver-trace-ablation",
  "report": "# 审稿报告 — Round 9\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**审稿团队**: Reviewer 1 (方法严谨性 + 实验有效性) + Reviewer 2 (新颖性 + 完整性 + 写作质量)\n**轮次**: Round 9 (fresh review session)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，对 solver 输入进行 leave-one-out 消融以检测 GRPO 训练的神经符号形式化器中的 reward hacking。其导出指标 Irreducible Solver Rate (ISR) 揭示了隐藏在 prove rate (97±2%) 上升背后的 99.5% 结构性崩溃。当 ISR 被用作训练奖励时，在所有四个测试剂量下均表现出 Goodhart 崩溃。论文归纳了九种 hacking 模式，跨 2 种逻辑类型、2 个模型规模、6 种奖励条件。\n\n---\n\n## Strengths\n\n**S1** [共识] 核心诊断思路 (STA/ISR) 填补了真实空白：execution-based evaluation 无法检测结构性退化，ISR 提供了可操作的检测工具。将 mutation testing 思想从软件工程引入 neurosymbolic RL 是新颖的跨领域迁移。\n\n**S2** [共识] 实验设计的自我批评精神罕见：H8+FN 校正后效果方向翻转的诚实报告、within-seed 非独立性对 CMH 的 inflation 效应的主动承认、premise-count confound 的充分讨论——这种统计诚实度在投稿论文中少见。\n\n**S3** [共识] Observer-optimizer 不对称性 (\"ISR reliable as diagnostic, unreliable as optimizer\") 是清晰有力且有实用指导意义的框架。\n\n**S4** [共识] Cross-seed 定性分叉发现有价值：相同数据、相同奖励 → 定性不同的 hacking 模式 (H1 vs. H7 vs. tautological collapse)，对 neurosymbolic RL 的可复现性讨论有贡献。\n\n**S5** [共识] 写作质量好，无 AI 写作痕迹，叙事聚焦，格式完全合规 (ACL [review] 模板, double-blind, 行号, ≤8 页正文, Limitations + Ethics 完整)。\n\n**S6** [共识] 引用覆盖全面 (42 篇)，涵盖 reward hacking 理论 + 经验性研究 + neurosymbolic 方法 + process rewards + mutation testing。\n\n---\n\n## Weaknesses\n\n### 持续性 Critical Issues（跨多轮未解决）\n\n**W1** [critical, 共识, 持续 R4-R9] **统计框架自相矛盾: CMH p-values 先被否认后被引用**\n- R1-N1 + R2 [AGREE 部分]\n- 论文在 §6 承认 CMH 独立性假设被违反 (\"directional indicators, not calibrated significance levels\")，但正文 §4.3/§4.6 仍醒目报告 CMH OR=3.37, OR=2.46 等具体数字。Seed-level permutation test (p=0.26, n.s.) 才是统计上正确的分析，但被置于次要位置。\n- **要求**: CMH 数字移至 Appendix，正文以 seed-level permutation (p=0.26, n.s., direction consistent but underpowered) 为主导。\n\n**W2** [critical, 共识, 持续 R4-R9] **OR 方向反转未在 Abstract/Introduction 充分呈现**\n- R1-W5 + R2-W3，双方 [AGREE]\n- 5-seed uncorrected N-H: ISR 23% vs. Random 8% (OR=3.48)，但 3-seed H8+FN corrected: ISR 6.06% vs. Random 9.5% (OR=0.61, n.s.)——方向反转。Seed-level permutation p=0.26。Premise-count matching 后差异降至 1.06×。三重否定性证据。\n- Abstract 仍含 \"transient genuine window\" 表述，Introduction 仍将其列为发现。\n- **要求**: 从 Abstract/Contributions 完全移除 genuine window；§4.3 仅作描述性保留并以 corrected 分析为 primary baseline。\n\n**W3** [critical, 共识, 新 R8-R9] **核心 Goodhart 发现的可预测性限制概念新颖性**\n- R2-N1 [critical] + R1 [AGREE with nuance]\n- 论文自己在 §3.2 承认 ISR 的 Goodhart 脆弱性 \"by construction\"。C2 (Goodhart 动力学刻画) 作为最大篇幅贡献，核心方向是 trivially predictable。论文试图通过二阶细节 (bifurcation, non-monotonic dose-response) 挽救新颖性。\n- R1 的 nuance: 可预测的是方向，不可预测的是速度/幅度/模式多样性/bifurcation dynamics——这部分有 empirical 价值。\n- **要求**: 将 C2 reframe 为 \"empirical characterization of a predictable failure\"；将 C1 (诊断发现) 提升为 primary contribution。\n\n**W4** [critical, 共识, 新 R8-R9] **实验范围 (Qwen3 + FOLIO) 与标题 scope 不匹配**\n- R2-N2 [critical] + R1 [AGREE]\n- 标题 \"Neurosymbolic Proof Generation\" 暗示一般性发现，但证据仅来自 Qwen3-4B/1.7B + FOLIO (500 训练样本, 100 评估样本)。未测试其他模型架构 (Llama, Gemma) 或其他 FOL 数据集 (ProntoQA, RuleTaker)。\n- **要求**: 若 deadline 前无法增加实验，收窄标题为更具体 scope (如 \"Reward Hacking in GRPO-Trained Formalizers\")。\n\n### Should-Fix Issues\n\n**W5** [warning, 共识, 持续 R5-R9] **SFT baseline PR confound**\n- R1-W4 [major] + R2-W2 [AGREE]\n- SFT PR=13% vs. GRPO 93-97%。选择偏差: SFT 成功样本可能是 \"easy\" 问题。100-step checkpoint (PR=32%) 部分缓解但不完全。论文在 §4.2 末句承认开放问题，但 Introduction/Abstract 中 \"consistent with RL-specific failure\" 的措辞未加充分 caveat。\n- **要求**: 每次提及 SFT 对比时附加 PR-level caveat。\n\n**W6** [warning, 共识, 持续 R3-R9] **1.7B 实验仅单 seed，与论文自身方法论矛盾**\n- R1-W2 + R2-W1，双方 [AGREE]\n- 论文大量论证 cross-seed variance 极高 (σ=47pp)，推荐 multi-seed evaluation，但 §4.5 仅 seed 42。\n- **要求**: 至少增加至 3 seeds，或将 §4.5 移入 Appendix 并重定位为 \"anecdotal observation\"。\n\n**W7** [warning, 共识, 持续 R6-R9] **Hacking taxonomy 系统性不足**\n- R1-W6 + R2-W4，双方 [AGREE 部分]\n- 9 类中 H1/H7/H8 占 >90%；其余 6 类中至少 4 个是单 seed/单条件孤立观察。分类器验证仅 50 样本，无 confusion matrix。Residual classification inflate non-hacking rate。\n- **要求**: 区分 \"robust modes\" (H1/H7/H8: multi-seed) vs. \"isolated observations\"；增加验证样本量。\n\n**W8** [warning, 共识, 持续 R6-R9] **Dose-response claim 基于不均匀 seed 数**\n- β=0.1 用 5 seeds，β=0.05/0.2/0.3 用 3 seeds。4 个 dose points 不足以刻画非单调模式。\n- **要求**: \"Non-monotonic dose-response\" 弱化为 descriptive pattern。\n\n**W9** [warning, 共识, 持续 R5-R9] **Abstract 数据堆砌**\n- ~10 个具体数字 (97±2%, 99.5%, 92%, ISR≥0.5, β=0.1, 23% vs 8%, nine modes 等)。审稿人 30 秒内难以抓住关键 takeaway。\n- **要求**: 删减至 4-5 个关键数字，删除 genuine window 相关数字。\n\n**W10** [warning, 新 R9] **§4.4 标题 \"Cross-Logic Diagnostic Transfer\" 措辞过强**\n- R1-W7 + R2 [AGREE]。实际是在不同设置下重新运行 STA，非 ML 意义上的 transfer。\n- **要求**: 改为 \"Cross-Logic Replication\" 或 \"STA on Prolog\"。\n\n**W11** [warning, 新 R9, 分歧] **Premise-count confound 对 ISR-as-diagnostic 的影响范围**\n- R1-W3 [critical]: ISR 应定位为 \"non-redundancy metric\"，confound 影响所有用途。\n- R2 [REBUT]: confound 主要影响 ISR-as-reward，不影响 ISR-as-diagnostic (同 seed 时间序列)。\n- **Director 裁决**: R2 的区分有道理——C1 不依赖 cross-condition ISR 比较。但论文应在 §3.2 进一步澄清 confound 在不同使用场景下的影响差异。降级为 warning。\n\n### Minor Issues\n\n**M1** Table 1 注释系统过复杂 (†, ‡, ††, ★)，建议拆分为 primary conditions + cross-scale 两张表。\n**M2** Introduction 过载定量结果 (ISR*: 0.642→0.132→0.003; PR σ=47pp; OR=147 等)，数字应留给 Experiments。\n**M3** Figure 1 Panel (a) 信息密度一般 (标准 NL→formal→solver pipeline)，可压缩。\n**M4** §3.2 Shapley 讨论第三个理由 (\"Goodhart effects would likely transfer\") 是循环论证。\n**M5** 训练时 sampling vs 评估时 greedy decoding 策略不一致未被讨论。\n**M6** 论文标题 \"Valid\" 有歧义 (execution validity vs logical validity)。\n**M7** 术语不一致: \"genuine\"/\"non-hacking\"/\"structurally sound\" 交替使用导致语义滑移。应统一为 \"non-hacking\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成共识：\n\n1. **总评 3.0 (Findings)**: 双方一致\n2. **CMH p-values 应降至 Appendix**: R1 [critical] + R2 [AGREE 部分]\n3. **Genuine window 从 Abstract/Contributions 移除**: R1 + R2 双方 [AGREE]\n4. **单一数据集限制泛化性**: R1 + R2 双方 [AGREE]\n5. **1.7B 单 seed 与方法论矛盾**: R1 + R2 双方 [AGREE]\n6. **SFT PR confound 真实存在**: R1 + R2 双方 [AGREE]\n7. **Taxonomy 应区分 robust vs isolated modes**: R1 + R2 双方 [AGREE]\n8. **Cross-logic \"transfer\" 措辞过强**: R1 + R2 双方 [AGREE]\n9. **Goodhart novelty 有限但 empirical characterization 有价值**: R1 [nuance] + R2 [critical]\n10. **写作质量好，无 AI 痕迹，格式完全合规**: R1 + R2 双方 [AGREE]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**唯一实质性分歧: Premise-count confound 的影响范围**\n\n- **R1 立场** [critical]: ISR 定义对 premise count 有结构性依赖，影响所有用途。ISR 应重新定位为 \"component non-redundancy metric\" 而非 \"structural integrity metric\"。论文中所有 \"structural integrity\" 措辞应弱化。\n- **R2 立场** [REBUT]: ISR 作为诊断 (C1) 使用时是同 seed 时间序列分析 (ISR* 0.642→0.132→0.003)，不依赖 cross-condition 比较，因此 premise-count confound 不影响 C1 核心发现。Confound 主要影响 ISR-as-reward 的 cross-condition 比较 (§4.3)，论文已在 §3.2 和 Appendix C 充分讨论。\n- **Director 裁决**: R2 的区分有技术道理。C1 的 99.5% collapse trajectory 是 within-seed 观察，premise-count 变化本身是 degeneration 的表征 (mean n: 6.58→18.55)。但 R1 关于 \"structural integrity\" 措辞精确度的要求合理。降级为 warning (W11)，要求 §3.2 澄清不同使用场景下的 confound 影响。\n\n---\n\n## Questions\n\n以下问题需要作者澄清（按优先级排序）：\n\n**Q1** [R1+R2, 高优先级] 如果使用 premise-count-normalized ISR（如 ISR / E[ISR | n]）作为 reward，Goodhart collapse 是否仍然发生？如不行，原因是什么？\n\n**Q2** [R1+R2, 高优先级] ISR 是否被测试过作为 rejection filter（丢弃 ISR < threshold 的输出）而非 continuous reward？Filter 不提供优化梯度，可能避免 Goodhart collapse。\n\n**Q3** [R1, 中优先级] ISR=1 的 proofs 是否一定语义正确？能否提供 ISR=1 但语义错误的反例？\n\n**Q4** [R2, 中优先级] 不同模型家族（Llama, Gemma）或 instruction-tuned vs. base 模型是否会产生本质不同的 hacking 动力学？\n\n**Q5** [R2, 中优先级] 增加训练数据规模（如 5000 examples），hacking 的普遍性和模式分布是否会改变？\n\n**Q6** [R1, 低优先级] STA 的 false-negative rate 是多少？Solver 内在冗余是否会导致 STA 低估 necessity？\n\n**Q7** [R1, 低优先级] \"99.5% structural collapse\" 精确指 ISR* 从 0.642 降至 0.003 的相对下降？还是 ISR=0 的样本比例？\n\n---\n\n## Missing References\n\n**共识推荐引用：**\n- Uesato et al. (2022) \"Solving Math Word Problems with Process- and Outcome-Based Feedback\" — process vs outcome feedback 对比，与 ISR vs PR 概念对应 (R1 提出, R2 [AGREE])\n\n**建议考虑：**\n- Khalaf et al. (NeurIPS 2025) \"Inference-Time Reward Hacking in Large Language Models\" — 与论文 training-time vs inference-time 区分直接相关 (R2 提出)\n- \"Reward Hacking as Equilibrium under Finite Evaluation\" (arXiv:2603.28063, 2026) — 理论互补 (R2 提出, 真实性待确认)\n\n**已确认不需要：**\n- Cobbe et al. (2021) — R2 rebuts: 数学文字题 verifier 与本文设置本质不同\n- Gao et al. (2023) — R1 提出但 R2 确认已引用\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 2.5/5 | 3.5/5 | 3.0/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Overall | 3.0 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分解读 (EMNLP 2026 ARR)**:\n- 3.0 = Findings（可被 Findings 接收）\n- 距主会议接收 (4.0) 有显著差距\n- 距 Borderline Conference (3.5) 需解决至少 W1-W4 中的 2-3 个\n\n**核心判断**: STA/ISR 作为诊断工具的概念有价值，observer-optimizer 不对称性框架清晰有力。但四个 critical 问题限制了当前版本的可接收性：(1) 统计呈现架构需重组 (CMH→Appendix, permutation→primary)；(2) genuine window 在三重检验后不成立但仍列为发现；(3) 核心 Goodhart 发现可从定义预测，需 reframe；(4) 实验范围与标题 scope 不匹配。\n\n**修改建议优先级**:\n1. [紧急, deadline 前可完成] 统计呈现重组 + genuine window 移除 + 术语统一 (W1, W2, M7)\n2. [紧急, deadline 前可完成] 标题收窄 + C2 reframe + Abstract 精简 (W3, W4, W9)\n3. [重要, deadline 前可部分完成] SFT caveat 加强 + taxonomy 区分 + cross-logic 标题修改 (W5, W7, W10)\n4. [理想但非必须] 增加 seeds/数据集, normalized ISR 实验 (W6, W8, Q1-Q2)\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高 (~10 个数字)，建议保留 \"99.5% collapse\" 和 \"Goodhart collapse at all tested doses\" 两个核心数据点\n- \"transient genuine window\" 应删除（三重检验后不成立）\n- \"structurally sound\" 应改为 \"non-hacking\"\n- \"trajectory-confirmed at β=0.1\" 过于细节化\n\n### Introduction (§1)\n- 叙事结构完整 (blind spot → STA → ISR as reward → contributions)\n- 过载定量结果 (ISR*: 0.642→0.132→0.003; PR σ=47pp; OR=147)——数字留给 Experiments\n- C4 声明与证据强度不匹配（多数 taxonomy 模式为孤立观察）\n- SFT 对比需加 PR-level caveat\n\n### Related Work (§2)\n- 结构清晰，与 Kim et al. (2026) 区分精确\n- 与 Ng (1999) reward shaping 的理论联系有洞察力\n- 建议增加 Uesato et al. (2022) 引用\n\n### Method (§3)\n- Algorithm 1 清晰，ISR 定义明确\n- LOO vs. Shapley 讨论充分但第三个理由循环论证\n- §3.2 premise-count confound 讨论值得肯定，但应增加不同使用场景下的影响区分\n\n### Experiments (§4)\n- §4.2 (ISR as Diagnostic): 最强部分。Figure 2 有力。Cross-seed divergence 分析有价值\n- §4.3 (Goodhart Effects): 统计呈现需重组。β 呈现顺序应为升序。Genuine window 降级为描述性\n- §4.4 (Cross-Logic): 标题 \"Transfer\" 过强，改为 \"Replication\"\n- §4.5 (Cross-Scale): 单 seed，建议移入 Appendix 或大幅压缩\n- §4.6 (Taxonomy): Table 2 好，但应区分 robust vs isolated modes\n\n### Discussion & Conclusion (§5)\n- 核心 takeaway 清晰。建议增加 ISR-as-filter 和 count-normalized ISR 的 future work 讨论\n\n### Limitations (§6)\n- 详尽且诚实（temporal snapshot, seed counts, cross-scale, data scale）——显著优势\n- 建议更突出 statistical power 不足和 premise-count confound 的具体影响\n\n### 格式合规\n- ✓ ≤8 页正文 (§1-§5 在 page 8 完成)\n- ✓ ACL LaTeX [review] 模板\n- ✓ Double-blind (\"Anonymous ACL submission\", URL [anonymized])\n- ✓ 行号可见\n- ✓ Limitations + Ethics 完整\n- ✓ 无 AI 写作痕迹",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)"
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
    "report": "# 审稿报告 — Round 9\n\n**论文**: \"Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**审稿团队**: Reviewer 1 (方法严谨性 + 实验有效性) + Reviewer 2 (新颖性 + 完整性 + 写作质量)\n**轮次**: Round 9 (fresh review session)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，对 solver 输入进行 leave-one-out 消融以检测 GRPO 训练的神经符号形式化器中的 reward hacking。其导出指标 Irreducible Solver Rate (ISR) 揭示了隐藏在 prove rate (97±2%) 上升背后的 99.5% 结构性崩溃。当 ISR 被用作训练奖励时，在所有四个测试剂量下均表现出 Goodhart 崩溃。论文归纳了九种 hacking 模式，跨 2 种逻辑类型、2 个模型规模、6 种奖励条件。\n\n---\n\n## Strengths\n\n**S1** [共识] 核心诊断思路 (STA/ISR) 填补了真实空白：execution-based evaluation 无法检测结构性退化，ISR 提供了可操作的检测工具。将 mutation testing 思想从软件工程引入 neurosymbolic RL 是新颖的跨领域迁移。\n\n**S2** [共识] 实验设计的自我批评精神罕见：H8+FN 校正后效果方向翻转的诚实报告、within-seed 非独立性对 CMH 的 inflation 效应的主动承认、premise-count confound 的充分讨论——这种统计诚实度在投稿论文中少见。\n\n**S3** [共识] Observer-optimizer 不对称性 (\"ISR reliable as diagnostic, unreliable as optimizer\") 是清晰有力且有实用指导意义的框架。\n\n**S4** [共识] Cross-seed 定性分叉发现有价值：相同数据、相同奖励 → 定性不同的 hacking 模式 (H1 vs. H7 vs. tautological collapse)，对 neurosymbolic RL 的可复现性讨论有贡献。\n\n**S5** [共识] 写作质量好，无 AI 写作痕迹，叙事聚焦，格式完全合规 (ACL [review] 模板, double-blind, 行号, ≤8 页正文, Limitations + Ethics 完整)。\n\n**S6** [共识] 引用覆盖全面 (42 篇)，涵盖 reward hacking 理论 + 经验性研究 + neurosymbolic 方法 + process rewards + mutation testing。\n\n---\n\n## Weaknesses\n\n### 持续性 Critical Issues（跨多轮未解决）\n\n**W1** [critical, 共识, 持续 R4-R9] **统计框架自相矛盾: CMH p-values 先被否认后被引用**\n- R1-N1 + R2 [AGREE 部分]\n- 论文在 §6 承认 CMH 独立性假设被违反 (\"directional indicators, not calibrated significance levels\")，但正文 §4.3/§4.6 仍醒目报告 CMH OR=3.37, OR=2.46 等具体数字。Seed-level permutation test (p=0.26, n.s.) 才是统计上正确的分析，但被置于次要位置。\n- **要求**: CMH 数字移至 Appendix，正文以 seed-level permutation (p=0.26, n.s., direction consistent but underpowered) 为主导。\n\n**W2** [critical, 共识, 持续 R4-R9] **OR 方向反转未在 Abstract/Introduction 充分呈现**\n- R1-W5 + R2-W3，双方 [AGREE]\n- 5-seed uncorrected N-H: ISR 23% vs. Random 8% (OR=3.48)，但 3-seed H8+FN corrected: ISR 6.06% vs. Random 9.5% (OR=0.61, n.s.)——方向反转。Seed-level permutation p=0.26。Premise-count matching 后差异降至 1.06×。三重否定性证据。\n- Abstract 仍含 \"transient genuine window\" 表述，Introduction 仍将其列为发现。\n- **要求**: 从 Abstract/Contributions 完全移除 genuine window；§4.3 仅作描述性保留并以 corrected 分析为 primary baseline。\n\n**W3** [critical, 共识, 新 R8-R9] **核心 Goodhart 发现的可预测性限制概念新颖性**\n- R2-N1 [critical] + R1 [AGREE with nuance]\n- 论文自己在 §3.2 承认 ISR 的 Goodhart 脆弱性 \"by construction\"。C2 (Goodhart 动力学刻画) 作为最大篇幅贡献，核心方向是 trivially predictable。论文试图通过二阶细节 (bifurcation, non-monotonic dose-response) 挽救新颖性。\n- R1 的 nuance: 可预测的是方向，不可预测的是速度/幅度/模式多样性/bifurcation dynamics——这部分有 empirical 价值。\n- **要求**: 将 C2 reframe 为 \"empirical characterization of a predictable failure\"；将 C1 (诊断发现) 提升为 primary contribution。\n\n**W4** [critical, 共识, 新 R8-R9] **实验范围 (Qwen3 + FOLIO) 与标题 scope 不匹配**\n- R2-N2 [critical] + R1 [AGREE]\n- 标题 \"Neurosymbolic Proof Generation\" 暗示一般性发现，但证据仅来自 Qwen3-4B/1.7B + FOLIO (500 训练样本, 100 评估样本)。未测试其他模型架构 (Llama, Gemma) 或其他 FOL 数据集 (ProntoQA, RuleTaker)。\n- **要求**: 若 deadline 前无法增加实验，收窄标题为更具体 scope (如 \"Reward Hacking in GRPO-Trained Formalizers\")。\n\n### Should-Fix Issues\n\n**W5** [warning, 共识, 持续 R5-R9] **SFT baseline PR confound**\n- R1-W4 [major] + R2-W2 [AGREE]\n- SFT PR=13% vs. GRPO 93-97%。选择偏差: SFT 成功样本可能是 \"easy\" 问题。100-step checkpoint (PR=32%) 部分缓解但不完全。论文在 §4.2 末句承认开放问题，但 Introduction/Abstract 中 \"consistent with RL-specific failure\" 的措辞未加充分 caveat。\n- **要求**: 每次提及 SFT 对比时附加 PR-level caveat。\n\n**W6** [warning, 共识, 持续 R3-R9] **1.7B 实验仅单 seed，与论文自身方法论矛盾**\n- R1-W2 + R2-W1，双方 [AGREE]\n- 论文大量论证 cross-seed variance 极高 (σ=47pp)，推荐 multi-seed evaluation，但 §4.5 仅 seed 42。\n- **要求**: 至少增加至 3 seeds，或将 §4.5 移入 Appendix 并重定位为 \"anecdotal observation\"。\n\n**W7** [warning, 共识, 持续 R6-R9] **Hacking taxonomy 系统性不足**\n- R1-W6 + R2-W4，双方 [AGREE 部分]\n- 9 类中 H1/H7/H8 占 >90%；其余 6 类中至少 4 个是单 seed/单条件孤立观察。分类器验证仅 50 样本，无 confusion matrix。Residual classification inflate non-hacking rate。\n- **要求**: 区分 \"robust modes\" (H1/H7/H8: multi-seed) vs. \"isolated observations\"；增加验证样本量。\n\n**W8** [warning, 共识, 持续 R6-R9] **Dose-response claim 基于不均匀 seed 数**\n- β=0.1 用 5 seeds，β=0.05/0.2/0.3 用 3 seeds。4 个 dose points 不足以刻画非单调模式。\n- **要求**: \"Non-monotonic dose-response\" 弱化为 descriptive pattern。\n\n**W9** [warning, 共识, 持续 R5-R9] **Abstract 数据堆砌**\n- ~10 个具体数字 (97±2%, 99.5%, 92%, ISR≥0.5, β=0.1, 23% vs 8%, nine modes 等)。审稿人 30 秒内难以抓住关键 takeaway。\n- **要求**: 删减至 4-5 个关键数字，删除 genuine window 相关数字。\n\n**W10** [warning, 新 R9] **§4.4 标题 \"Cross-Logic Diagnostic Transfer\" 措辞过强**\n- R1-W7 + R2 [AGREE]。实际是在不同设置下重新运行 STA，非 ML 意义上的 transfer。\n- **要求**: 改为 \"Cross-Logic Replication\" 或 \"STA on Prolog\"。\n\n**W11** [warning, 新 R9, 分歧] **Premise-count confound 对 ISR-as-diagnostic 的影响范围**\n- R1-W3 [critical]: ISR 应定位为 \"non-redundancy metric\"，confound 影响所有用途。\n- R2 [REBUT]: confound 主要影响 ISR-as-reward，不影响 ISR-as-diagnostic (同 seed 时间序列)。\n- **Director 裁决**: R2 的区分有道理——C1 不依赖 cross-condition ISR 比较。但论文应在 §3.2 进一步澄清 confound 在不同使用场景下的影响差异。降级为 warning。\n\n### Minor Issues\n\n**M1** Table 1 注释系统过复杂 (†, ‡, ††, ★)，建议拆分为 primary conditions + cross-scale 两张表。\n**M2** Introduction 过载定量结果 (ISR*: 0.642→0.132→0.003; PR σ=47pp; OR=147 等)，数字应留给 Experiments。\n**M3** Figure 1 Panel (a) 信息密度一般 (标准 NL→formal→solver pipeline)，可压缩。\n**M4** §3.2 Shapley 讨论第三个理由 (\"Goodhart effects would likely transfer\") 是循环论证。\n**M5** 训练时 sampling vs 评估时 greedy decoding 策略不一致未被讨论。\n**M6** 论文标题 \"Valid\" 有歧义 (execution validity vs logical validity)。\n**M7** 术语不一致: \"genuine\"/\"non-hacking\"/\"structurally sound\" 交替使用导致语义滑移。应统一为 \"non-hacking\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成共识：\n\n1. **总评 3.0 (Findings)**: 双方一致\n2. **CMH p-values 应降至 Appendix**: R1 [critical] + R2 [AGREE 部分]\n3. **Genuine window 从 Abstract/Contributions 移除**: R1 + R2 双方 [AGREE]\n4. **单一数据集限制泛化性**: R1 + R2 双方 [AGREE]\n5. **1.7B 单 seed 与方法论矛盾**: R1 + R2 双方 [AGREE]\n6. **SFT PR confound 真实存在**: R1 + R2 双方 [AGREE]\n7. **Taxonomy 应区分 robust vs isolated modes**: R1 + R2 双方 [AGREE]\n8. **Cross-logic \"transfer\" 措辞过强**: R1 + R2 双方 [AGREE]\n9. **Goodhart novelty 有限但 empirical characterization 有价值**: R1 [nuance] + R2 [critical]\n10. **写作质量好，无 AI 痕迹，格式完全合规**: R1 + R2 双方 [AGREE]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**唯一实质性分歧: Premise-count confound 的影响范围**\n\n- **R1 立场** [critical]: ISR 定义对 premise count 有结构性依赖，影响所有用途。ISR 应重新定位为 \"component non-redundancy metric\" 而非 \"structural integrity metric\"。论文中所有 \"structural integrity\" 措辞应弱化。\n- **R2 立场** [REBUT]: ISR 作为诊断 (C1) 使用时是同 seed 时间序列分析 (ISR* 0.642→0.132→0.003)，不依赖 cross-condition 比较，因此 premise-count confound 不影响 C1 核心发现。Confound 主要影响 ISR-as-reward 的 cross-condition 比较 (§4.3)，论文已在 §3.2 和 Appendix C 充分讨论。\n- **Director 裁决**: R2 的区分有技术道理。C1 的 99.5% collapse trajectory 是 within-seed 观察，premise-count 变化本身是 degeneration 的表征 (mean n: 6.58→18.55)。但 R1 关于 \"structural integrity\" 措辞精确度的要求合理。降级为 warning (W11)，要求 §3.2 澄清不同使用场景下的 confound 影响。\n\n---\n\n## Questions\n\n以下问题需要作者澄清（按优先级排序）：\n\n**Q1** [R1+R2, 高优先级] 如果使用 premise-count-normalized ISR（如 ISR / E[ISR | n]）作为 reward，Goodhart collapse 是否仍然发生？如不行，原因是什么？\n\n**Q2** [R1+R2, 高优先级] ISR 是否被测试过作为 rejection filter（丢弃 ISR < threshold 的输出）而非 continuous reward？Filter 不提供优化梯度，可能避免 Goodhart collapse。\n\n**Q3** [R1, 中优先级] ISR=1 的 proofs 是否一定语义正确？能否提供 ISR=1 但语义错误的反例？\n\n**Q4** [R2, 中优先级] 不同模型家族（Llama, Gemma）或 instruction-tuned vs. base 模型是否会产生本质不同的 hacking 动力学？\n\n**Q5** [R2, 中优先级] 增加训练数据规模（如 5000 examples），hacking 的普遍性和模式分布是否会改变？\n\n**Q6** [R1, 低优先级] STA 的 false-negative rate 是多少？Solver 内在冗余是否会导致 STA 低估 necessity？\n\n**Q7** [R1, 低优先级] \"99.5% structural collapse\" 精确指 ISR* 从 0.642 降至 0.003 的相对下降？还是 ISR=0 的样本比例？\n\n---\n\n## Missing References\n\n**共识推荐引用：**\n- Uesato et al. (2022) \"Solving Math Word Problems with Process- and Outcome-Based Feedback\" — process vs outcome feedback 对比，与 ISR vs PR 概念对应 (R1 提出, R2 [AGREE])\n\n**建议考虑：**\n- Khalaf et al. (NeurIPS 2025) \"Inference-Time Reward Hacking in Large Language Models\" — 与论文 training-time vs inference-time 区分直接相关 (R2 提出)\n- \"Reward Hacking as Equilibrium under Finite Evaluation\" (arXiv:2603.28063, 2026) — 理论互补 (R2 提出, 真实性待确认)\n\n**已确认不需要：**\n- Cobbe et al. (2021) — R2 rebuts: 数学文字题 verifier 与本文设置本质不同\n- Gao et al. (2023) — R1 提出但 R2 确认已引用\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 2.5/5 | 3.5/5 | 3.0/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Overall | 3.0 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分解读 (EMNLP 2026 ARR)**:\n- 3.0 = Findings（可被 Findings 接收）\n- 距主会议接收 (4.0) 有显著差距\n- 距 Borderline Conference (3.5) 需解决至少 W1-W4 中的 2-3 个\n\n**核心判断**: STA/ISR 作为诊断工具的概念有价值，observer-optimizer 不对称性框架清晰有力。但四个 critical 问题限制了当前版本的可接收性：(1) 统计呈现架构需重组 (CMH→Appendix, permutation→primary)；(2) genuine window 在三重检验后不成立但仍列为发现；(3) 核心 Goodhart 发现可从定义预测，需 reframe；(4) 实验范围与标题 scope 不匹配。\n\n**修改建议优先级**:\n1. [紧急, deadline 前可完成] 统计呈现重组 + genuine window 移除 + 术语统一 (W1, W2, M7)\n2. [紧急, deadline 前可完成] 标题收窄 + C2 reframe + Abstract 精简 (W3, W4, W9)\n3. [重要, deadline 前可部分完成] SFT caveat 加强 + taxonomy 区分 + cross-logic 标题修改 (W5, W7, W10)\n4. [理想但非必须] 增加 seeds/数据集, normalized ISR 实验 (W6, W8, Q1-Q2)\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高 (~10 个数字)，建议保留 \"99.5% collapse\" 和 \"Goodhart collapse at all tested doses\" 两个核心数据点\n- \"transient genuine window\" 应删除（三重检验后不成立）\n- \"structurally sound\" 应改为 \"non-hacking\"\n- \"trajectory-confirmed at β=0.1\" 过于细节化\n\n### Introduction (§1)\n- 叙事结构完整 (blind spot → STA → ISR as reward → contributions)\n- 过载定量结果 (ISR*: 0.642→0.132→0.003; PR σ=47pp; OR=147)——数字留给 Experiments\n- C4 声明与证据强度不匹配（多数 taxonomy 模式为孤立观察）\n- SFT 对比需加 PR-level caveat\n\n### Related Work (§2)\n- 结构清晰，与 Kim et al. (2026) 区分精确\n- 与 Ng (1999) reward shaping 的理论联系有洞察力\n- 建议增加 Uesato et al. (2022) 引用\n\n### Method (§3)\n- Algorithm 1 清晰，ISR 定义明确\n- LOO vs. Shapley 讨论充分但第三个理由循环论证\n- §3.2 premise-count confound 讨论值得肯定，但应增加不同使用场景下的影响区分\n\n### Experiments (§4)\n- §4.2 (ISR as Diagnostic): 最强部分。Figure 2 有力。Cross-seed divergence 分析有价值\n- §4.3 (Goodhart Effects): 统计呈现需重组。β 呈现顺序应为升序。Genuine window 降级为描述性\n- §4.4 (Cross-Logic): 标题 \"Transfer\" 过强，改为 \"Replication\"\n- §4.5 (Cross-Scale): 单 seed，建议移入 Appendix 或大幅压缩\n- §4.6 (Taxonomy): Table 2 好，但应区分 robust vs isolated modes\n\n### Discussion & Conclusion (§5)\n- 核心 takeaway 清晰。建议增加 ISR-as-filter 和 count-normalized ISR 的 future work 讨论\n\n### Limitations (§6)\n- 详尽且诚实（temporal snapshot, seed counts, cross-scale, data scale）——显著优势\n- 建议更突出 statistical power 不足和 premise-count confound 的具体影响\n\n### 格式合规\n- ✓ ≤8 页正文 (§1-§5 在 page 8 完成)\n- ✓ ACL LaTeX [review] 模板\n- ✓ Double-blind (\"Anonymous ACL submission\", URL [anonymized])\n- ✓ 行号可见\n- ✓ Limitations + Ethics 完整\n- ✓ 无 AI 写作痕迹",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-17T19:17:44.758923+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4069
}
```

</details>

---


### Assistant

_source line 790 · 2026-05-17T19:17:56.784956+00:00_

审稿报告已投递至 Research Director。

**Round 9 审稿完成。**

**总评: 3.0 (Findings)**

两位 Reviewer 一致评分 3.0，认为论文作为 Findings 可接收但距主会议 (4.0) 有显著差距。

**4 个 Critical Issues 决定评分上限：**

| # | Issue | 持续轮次 | 修复难度 |
|---|-------|---------|---------|
| W1 | CMH p-values 先否认后引用，统计呈现需重组 | R4→R9 | 低（文本编辑） |
| W2 | Genuine window 三重检验不成立但仍在 Abstract | R4→R9 | 低（删除/改写） |
| W3 | Goodhart 发现可从定义预测，C2 需 reframe | R8→R9 | 中（叙事重构） |
| W4 | 标题 scope 与实验范围不匹配 | R8→R9 | 低（标题修改） |

W1、W2、W4 均可在 deadline (5/25) 前完成。W3 需要 Abstract + Introduction + Contributions 的叙事重构但不涉及新实验。

**唯一分歧**: Premise-count confound 是否影响 ISR-as-diagnostic (R1: 影响全部 vs R2: 仅影响 cross-condition 比较)。Director 裁决支持 R2 的技术区分，降级为 warning。

Issue tracker 已同步更新至 Round 9（含 4 个新 issue + 15 个持续 issue 的 mention 更新）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 76

## Round 76

2 recorded events


### User

_source line 791 · 2026-05-17T19:17:59.293913+00:00_

[Reviewer 1 审稿结果]:
已完成两部分内容并提交给 Director：

1. **R2 交叉回应**：对 R2 的 2 个 Must-Fix、4 个 Should-Fix、6 个小问题逐条回应。大部分 [AGREE]，仅在 M1（Abstract 信息密度）和 M2（Introduction 长度）上 [REBUT]——我认为问题出在内容准确性和数字堆砌，而非信息密度和篇幅本身。

2. **R1 完整审稿意见**：Overall 3.0 (Findings)，三个 Must-Fix 问题：
   - **N1**: 统计框架自相矛盾（disclaiming p-values 同时依赖它们）
   - **N2**: Seed 数量不足以支撑核心声明（5 seeds 无法刻画随机分叉）
   - **N3**: Premise-count confound 根本性限制 ISR 解释（genuine window 经控制后消失）

R1 与 R2 在核心判断上高度一致：诊断思路有价值（S1-S3），但统计基础和泛化性是主要瓶颈。

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

_source line 792 · 2026-05-17T19:18:13.089215+00:00_

审稿报告已投递至 Research Director。

**Round 9 审稿完成。**

核心结论：

- **总评 3.0 (Findings)**，两位 Reviewer 一致
- **4 个 critical issues**: (1) CMH 统计呈现需重组；(2) genuine window 三重检验后不成立应从 Abstract 移除；(3) Goodhart 发现可预测性限制新颖性，需 reframe C2；(4) 实验范围与标题 scope 不匹配
- **7 个 warning issues**: SFT PR confound、1.7B 单 seed、taxonomy 系统性、dose-response 措辞、Abstract 数据堆砌、cross-logic "transfer" 措辞、premise-count confound 影响范围澄清
- **距主会议接收 (4.0) 有显著差距**，距 Borderline Conference (3.5) 需解决至少 2-3 个 critical issues
- Issue tracker 已同步更新至 Round 9（含 4 个新 issue + 所有历史 issue 的本轮 mentions）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 77

## Round 77

76 recorded events


### User

_source line 793 · 2026-05-18T08:05:33.506648+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/paper/main.tex
- 目标 venue: ACL ARR May 2026
- 投稿类别: NLP and Symbolic Reasoning
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

_source line 794 · 2026-05-18T08:05:39.743573+00:00_

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

_source line 795 · 2026-05-18T08:05:39.794654+00:00_

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

_source line 796 · 2026-05-18T08:05:45.569408+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-18T08:05:45.620064+00:00_



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

_source line 798 · 2026-05-18T08:05:50.392895+00:00_

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

_source line 799 · 2026-05-18T08:05:51.499002+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (150 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d129-1_7b-isr-b03-s44 | D129: 1.7B ISR β=0.3 s44 cross-scale replication — s42 showed reward collapse (PR=17% at 4B), s43 showed PR=52% with 100% CI at 1.7B; tests whether high-dose collapse pattern is consistent across seeds at 1.7B | — | — | — |\n\n## 待处理\n- sweep-random-b01-s46: W4: Random β=0.1 s46 extends random control to 5-seed（排队等待 GPU）\n- sweep-random-b01-s45: W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1（排队等待 GPU）\n- d129-1.7b-isr-b03-s44: D129: 1.7B ISR β=0.3 s44 cross-scale replication — tests robustness of reward collapse pattern at 1.7B high-dose ISR（准备中）\n- d129-1.7b-isr-b03-s43: D129: 1.7B ISR β=0.3 s43 cross-scale replication — s42 showed reward collapse (PR=17%) mirroring 4B pattern; additional seed tests robustness of high-dose collapse at 1.7B（准备中）\n- d129-1.7b-random-b01-s44: D129: 1.7B Random β=0.1 s44 cross-scale control — tests H9 mode determinism at 1.7B scale under random reward（准备中）\n- w2-qwen3-7b-pilot: Qwen3-8B exec-only 50-step pilot: 测试 8B 模型能否在 96GB 
…[truncated 1860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1106
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-18T08:05:51.750466+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 801 · 2026-05-18T08:05:51.801174+00:00_



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

_source line 802 · 2026-05-18T08:05:52.453976+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
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
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-18T08:05:52.454472+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-18T08:05:53.309545+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
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
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-18T08:05:53.360264+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig1_sta_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig4_prolog_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig2_isr_collapse.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig5_training_isr_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig3_hacking_composition.pdf

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

_source line 806 · 2026-05-18T08:05:58.605889+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines"
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
    "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 807 · 2026-05-18T08:05:59.410279+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 author guidelines page limit template anonymous review"
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
    "query": "ACL ARR 2026 author guidelines page limit template anonymous review"
  }
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-18T08:06:00.014037+00:00_

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

_source line 809 · 2026-05-18T08:06:05.888640+00:00_

Web search results for query: "ACL ARR 2026 author guidelines page limit template anonymous review"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"}]

Based on the search results, here's the information about ACL ARR 2026 author guidelines regarding page limits, templates, and anonymous review:

## Page Limits

For ARR submissions, the page limits are 4 pages for short papers and 8 pages for long papers, excluding the ethical considerations and limitations.

## Submission Template

The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template.

## Anonymous Review Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is und
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6478
}
```

</details>

---


### Tool result

_source line 810 · 2026-05-18T08:06:08.450003+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 call for papers submission guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results, here's information about ACL Rolling Review (ARR) submission guidelines:

## General Submission Guidelines

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). The author list should include all individuals who made substantial contributions to the work, and each author listed will be notified of submissions and reviews.

## Author Requirements

All authors are required to sign up as reviewers, with assignments made based o
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 9844
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-18T08:06:08.500686+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8486
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-18T08:06:19.199089+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclrollingreview.org dates May 2026 submission deadline"
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
    "query": "aclrollingreview.org dates May 2026 submission deadline"
  }
}
```

</details>

---


### Tool call

_source line 813 · 2026-05-18T08:06:19.852048+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 responsible NLP checklist submission requirements formatting acl2023.sty"
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
    "query": "ACL ARR 2026 responsible NLP checklist submission requirements formatting acl2023.sty"
  }
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-18T08:06:20.003890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-18T08:06:20.054520+00:00_

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
21	\title{Valid but Vacuous: Reward Hacking in RL-Trained Formal Reasoning}
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

_source line 816 · 2026-05-18T08:06:24.846840+00:00_

Web search results for query: "aclrollingreview.org dates May 2026 submission deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, I found information about ACL Rolling Review dates. However, the search results don't appear to contain specific details about a May 2026 submission deadline on the aclrollingreview.org dates page. 

The search results show that the submission deadline is always the 15th of the month for ARR cycles. According to the information found, the new schedule started in May 2025 cycle with 10-week cycles, which means cycles occur periodically throughout the year.

For a May 2026 submission deadline specifically, based on the pattern mentioned, this would likely be May 15, 2026, though the exact dates table for May 2026 wasn't fully visible in the search results. The GitHub repository reference (result 8) appears to have a table listing all key dates, but the complete May 2026 information wasn't fully displayed in the search results provided.

For the most up-to-date and complete information about May 2026 
…[truncated 222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5647
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-18T08:06:27.206966+00:00_

Web search results for query: "ACL ARR 2026 responsible NLP checklist submission requirements formatting acl2023.sty"

Links: [{"title":"ARR Responsible NLP Research checklist","url":"http://aclrollingreview.org/responsibleNLPresearch/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Responsible NLP Research Checklist","url":"https://aclrollingreview.org/static/responsibleNLPresearch.pdf"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Responsible NLP Research Checklist","url":"https://openreview.net/attachment?id=yGhYSEj8ln0&name=responsible_NLP_research"},{"title":"EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsible-nlp-checklist-appendices"}]

Based on the search results, here's information about ACL ARR 2026 Responsible NLP Checklist submission requirements:

## Submission Format

The checklist is completed as part of the submission form. Both long and short paper submissions should follow all of the ARR submission requirements, 
…[truncated 1319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7354
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-18T08:06:31.425297+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
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
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-18T08:06:31.476045+00:00_



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

_source line 820 · 2026-05-18T08:06:31.978859+00:00_

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

_source line 821 · 2026-05-18T08:06:32.380932+00:00_

1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\pm}2\%$) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline largely avoids hacking on identical data, suggesting the failure may be RL-specific.
4	Repurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and any transient improvement over random controls disappears under extended training and stricter classification.
5	Across multiple reward conditions, logic types, and model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target, with collapse dynamics that resist prediction from the metric definition alone.\footnote{Code and data: \url{[anonymized]}}
6	\end{abstract}
7	

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

_source line 822 · 2026-05-18T08:06:32.431713+00:00_

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

_source line 823 · 2026-05-18T08:06:32.934138+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\pm}2\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for solver-backed formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in solver-backed formal outputs.
12	
13	\paragraph{Solver Trace Ablation.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yiel
…[truncated 3512 chars]

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

_source line 824 · 2026-05-18T08:06:32.934545+00:00_

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

_source line 825 · 2026-05-18T08:06:32.985201+00:00_

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
…[truncated 5730 chars]

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

_source line 826 · 2026-05-18T08:06:33.286853+00:00_

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

_source line 827 · 2026-05-18T08:06:33.338181+00:00_

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
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate: the residual of proved samples matching none of the nine cataloged patterns (\S\ref{sec:taxonomy}); we use ``genuine'' interchangeably in descriptive contexts.
13	We further distinguish \emph{strict genuine}: proofs that are both non-hacking and content-dependent, using predicates derived from the natural-language premises rather than abstract placeholders; this filters content-independent proofs that evade the taxonomy through structural novelty (\S\ref{sec:crossscale}).
14	
15	\subsection{ISR as Diagnostic}
16	\label{sec:diagnostic}
17	
18	\begi
…[truncated 17934 chars]

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

_source line 828 · 2026-05-18T08:06:42.678109+00:00_

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

_source line 829 · 2026-05-18T08:06:43.783122+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Formal reasoning with LLMs.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{polu2020generative, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1-2025} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{uesato2022solving} and \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Unlike potential-based reward shaping~\citep{ng1999policy}, ISR augmentation does not preserve optimal policy, as it rewards output properties (component necessity) rather than state transitions, explaining the observed Goodhart vulnerability.
11	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
12	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
13	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant i
…[truncated 2439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-18T08:06:43.833874+00:00_

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

_source line 831 · 2026-05-18T08:06:44.386498+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$; \S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR produces descriptively more genuine output than random controls (pooled N-H: 23\% vs.\ 8\%); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\text{OR}{=}0.61$, n.s.).
6	Extended training confirms the window closes.
7	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
8	While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist prediction from the metric definition alone: stochastic bifurcation (\S\ref{sec:goodhart}), non-monotonic dose-response across four $\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\S\ref{sec:crosslogic}).
9	These details underscore the gap between predicting \emph{that} a metric will be gamed and predicting \emph{how}.
10	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
11	Promising directions include ISR as a post-hoc filter (selecting high-ISR outputs without backpropagating through the metric) and normalized variants that control for the premise-count confound.
12	

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

_source line 832 · 2026-05-18T08:06:44.386919+00:00_

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

_source line 833 · 2026-05-18T08:06:44.387164+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single model family (Qwen3-4B/1.7B) and a single structured-NLI dataset (FOLIO, 500 training examples); whether the specific hacking modes and collapse dynamics generalize to other architectures or larger-scale formal reasoning benchmarks remains an open question.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$). CMH tests yield $p{<}10^{-9}$ but assume within-stratum independence, which is violated when samples share a checkpoint and decoding strategy; CMH $p$-values are therefore inflated and should be interpreted as directional indicators, not calibrated significance levels.
8	STA requires solvers supporting component-level input manipulation.
9	Non-hacking is a residual classification; undiscovered gaming modes would reduce the true non-hacking rate, as illustrated by H7b (obfuscated tautology evading text-match classifiers) and query-as-fact gaming in Prolog.
10	
11	\paragraph{Evaluation as temporal snapshot.}
12	All 500-step results represent a temporal snapshot, not an equilibrium.
13	Trajectory analysis on seeds~42 and~45 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient (s42: $17\%{\to}2\%$; s45: $55\%{\to}0\%$ genuine).
14	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
15	
16	\paragraph{Seed counts per dose.}
17	ISR $\beta{=}0.05$ us
…[truncated 1912 chars]

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

_source line 834 · 2026-05-18T08:06:44.789064+00:00_

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

_source line 835 · 2026-05-18T08:06:45.291556+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
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
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-18T08:06:45.292108+00:00_

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

_source line 837 · 2026-05-18T08:06:45.744763+00:00_

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
…[truncated 43662 chars]

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

_source line 838 · 2026-05-18T08:06:48.154590+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission guidelines: page limits for long and short papers, template requirements, anonymity rules, appendix rules, responsible NLP checklist requirements, and any other formatting requirements. Also find the May 2026 submission deadline if listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the complete submission guidelines: page limits for long and short papers, template requirements, anonymity rules, appendix rules, responsible NLP checklist requirements, and any other formatting requirements. Also find the May 2026 submission deadline if listed."
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-18T08:06:55.048034+00:00_

# ACL Rolling Review Submission Guidelines Summary

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space after conclusion for limitations (required) and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space after conclusion for limitations (required) and optional ethical considerations
- Unlimited reference pages

Papers exceeding length requirements or lacking a limitations section face desk rejection.

## Template Requirements

Submissions must adhere to the official ACL style template available on GitHub (acl-org/acl-style-files). Authors must follow ACL formatting guidelines and cannot modify style files or use templates from other conferences. Submissions not conforming to required styles, including paper size, margins, and font sizes, are rejected without review.

## Anonymity Rules

The platform enforces two-way anonymized review. Papers must not contain author names, affiliations, or self-references revealing identity. Instead of "We previously showed," use "Authors previously showed." Supplementary materials and repository links must be anonymized. Non-anonymous preprints may be posted, though anonymous submissions receive preference in borderline acceptance decisions. Violations result in desk rejection.

## Appendix Rules

Appendices follow the main paper and references, do not count toward page limits, and must use double-column format (with limited exceptions per ACLPUB guidelines). Critical technical content should appear in the main paper, not appendices. Reviewers are not obligated to review appendix materials.

## Responsible NLP Checklist Requirements

Authors must complete the responsible NLP checklist during submission. Incorrect, incomplete, or misleading information results in desk rejection. The checklist addresses ethical considerations and responsible research practices.

## Additional Formatting Requirements

- Required "Limitations" section at pa
…[truncated 408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "elapsed_ms": 6893
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-18T08:07:03.586378+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Find the May 2026 submission cycle deadline and all key dates for that cycle (submission deadline, review period, commitment deadline for venues). List all dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/dates",
    "prompt": "Find the May 2026 submission cycle deadline and all key dates for that cycle (submission deadline, review period, commitment deadline for venues). List all dates."
  }
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-18T08:07:05.746041+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
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
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-18T08:07:05.897113+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-18T08:07:06.449545+00:00_

# May 2026 Cycle Key Dates

Based on the ARR schedule table, here are the important dates for the May 2026 submission cycle:

**Submission Deadline:** May 25, 2026

**Reviewer Registration Deadline:** May 27, 2026

**Reviews Due:** June 29, 2026

**Author Response Period:** July 7-13, 2026

**Meta-reviews Release Date:** July 30, 2026

**Cycle End:** August 2, 2026

**Commitment Deadlines for Venues:**
- EMNLP 2026: August 2, 2026
- AACL 2026: August 26, 2026

The cycle follows the new 10-week schedule that began in May 2025, with "more reasonable timelines for the review tasks and author response."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebFetch",
  "elapsed_ms": 2863
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-18T08:07:06.449969+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
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
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-18T08:07:06.500613+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 132\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteri
…[truncated 1452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-18T08:07:11.265579+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 847 · 2026-05-18T08:07:11.311272+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 45
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-18T08:07:14.793348+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
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
    "file": "paper_framing.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-18T08:07:15.446552+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- **EMNLP 2026 Main** (NLP and Symbolic Reasoning track)\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (9 modes, +H9) |\\n| Claim 2: Goodhart inevitable + ISR double-edged | ✅ 已闭环 (D057+D113+D120-D125) | **5-seed** ISR + **5-seed** random β=0.1 + premise-count-matched + SFT baseline + 1.7B cross-scale + **β=0.05 no-safe-dose** |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H
…[truncated 1362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-18T08:07:15.447001+00:00_

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


### Tool call

_source line 851 · 2026-05-18T08:07:15.597891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 852 · 2026-05-18T08:07:15.648835+00:00_

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
…[truncated 16446 chars]

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

_source line 853 · 2026-05-18T08:07:15.751362+00:00_

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
26	  severity: critical
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
…[truncated 39385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-18T08:07:23.391904+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-18T08:07:23.644059+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_4.md:133:未配置。项目未启用 `external_review.paperreview_ai`。
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_2.md:173:未配置。项目未启用 `external_review.paperreview_ai`。
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_7.md:149:外部审稿：未请求（项目未配置 external_review）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/feishu_group_oc_5abafbb382eb7c81e8a38090e46323e7_director.jsonl:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/feishu_group_oc_5abafbb382eb7c81e8a38090e46323e7_director.jsonl:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/feishu_group_oc_5abafbb382eb7c81e8a38090e46323e7_di
…[truncated 16433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Grep",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-18T08:07:40.167838+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null | grep -E \"Pages|Page size\"",
  "description": "Check PDF page count and size"
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
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf 2>/dev/null | grep -E \"Pages|Page size\"",
    "description": "Check PDF page count and size"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-18T08:07:41.975896+00:00_

Pages:           22
Page size:       595.276 x 841.89 pts (A4)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1808
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-18T08:07:42.026837+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"\\\\\\\\section\\|\\\\\\\\subsection\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex 2>/dev/null; echo \"---\"; grep -c '\\\\\\\\bibliography' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
  "description": "Count sections and bibliography command"
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
    "command": "grep -c \"\\\\\\\\section\\|\\\\\\\\subsection\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex 2>/dev/null; echo \"---\"; grep -c '\\\\\\\\bibliography' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
    "description": "Count sections and bibliography command"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-18T08:07:42.127758+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex:7
---
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-18T08:07:48.253906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "1-5"
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
    "pages": "1-5"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-18T08:07:48.607445+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf (592.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-18T08:07:55.093429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf",
  "pages": "6-10"
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
    "pages": "6-10"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-18T08:07:55.445663+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.pdf (592.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-18T08:09:21.702140+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计方法**。\n\n## 论文信息\n- **标题**: Valid but Vacuous: Reward Hacking in RL-Trained Formal Reasoning\n- **论文路径**: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- **目标 venue**: ACL ARR May 2026（目标 EMNLP 2026 commitment）\n- **Deadline**: 2026-05-25\n- **格式**: ACL Long Paper, 8 页正文, double-blind, Limitations + Ethics 不计入页数, Appendix 在 References 之后\n- **评分标准 (EMNLP 2026)**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 论文概要\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的 solver-backed formalizer 中的 reward hacking。核心指标 ISR (Irreducible Solver Rate) 在 FOLIO 数据集 + Qwen3-4B/1.7B 上揭示了 execution reward 下 99.5% 的结构崩溃。当 ISR 被用作训练信号时，在 4 个剂量下均出现 Goodhart collapse。论文记录了 9 种 hacking 模式，跨 FOL/Prolog 两种逻辑。\n\n## 你的审查重点\n\n### A. 方法严谨性\n1. STA/ISR 的定义是否严谨？LOO ablation 作为 component necessity test 的理论基础是否充分？\n2. ISR 的 premise-count confound（§3.2）处理是否充分？论文对 confound 在不同使用场景下的区分是否合理？\n3. Reward formulation $r = r_{exec} \\cdot (1 + \\beta \\cdot ISR)$ 的设计选择是否合理？与其他 reward shaping 方法的比较是否充分？\n4. Hacking taxonomy 的分类标准是否 principled？9 种模式的定义是否互斥且穷尽？\n5. SFT baseline 的比较是否公平？PR confound（SFT PR=13% vs GRPO PR=93%）是否充分控制？\n\n### B. 实验设计\n1. 实验规模：500 训练样本 + 100 评估样本是否足够？单模型家族 (Qwen3) + 单数据集 (FOLIO) 的泛化性如何？\n2. Seed 数量：β=0.1 用 5 seeds，β=0.05/0.2/0.3 用 3 seeds，1.7B 用 1-3 seeds。不均匀 seed 分配是否影响结论可靠性？\n3. Cross-scale (§4.5): 1.7B 实验的样本量是否支撑正文中的 claims？\n4. Cross-logic (§4.4): Prolog 实验的设计是否足以支撑 \"consistent Goodhart effects\" 的结论？\n5. 评估协议：s43 exec-only 使用 sampling (T=0.7) vs 其他 seed 使用 greedy decoding 的不一致性\n\n### C. 统计方法\n1. Fisher exact test, CMH test, seed-level permutation test 的层级关系和使用是否合理？\n2. CMH 的 within-seed 非独立性问题论文是否充分承认？seed-level permutation (p=0.26, n=5) 作为 primary test 的选择是否合适？\n3. OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，论文对此的处理是否诚实？\n4. 多重比较（6+ Fisher exact tests）是否需要校正？\n5. N-H=23% 作为 uncorrected upper bound 的处理（s43/s44 checkpoint deleted, H8 audit incomplete）\n\n### D. 产出报告格式\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出，每条 1-3 句]\n\n## Weaknesses\n[逐条列出，标注 severity: critical/major/minor]\n\n## Questions for Authors\n[需要作者澄清的问题]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Detailed Comments\n[按 section 逐节详细意见]\n\n## Overall Assessment\n[评分 + 置信度 + 1-2 句总评]\n```",
  "reviewer_id": "1",
  "project": "solver-trace-ablation",
  "round_number": "1"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计方法**。\n\n## 论文信息\n- **标题**: Valid but Vacuous: Reward Hacking in RL-Trained Formal Reasoning\n- **论文路径**: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- **目标 venue**: ACL ARR May 2026（目标 EMNLP 2026 commitment）\n- **Deadline**: 2026-05-25\n- **格式**: ACL Long Paper, 8 页正文, double-blind, Limitations + Ethics 不计入页数, Appendix 在 References 之后\n- **评分标准 (EMNLP 2026)**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 论文概要\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的 solver-backed formalizer 中的 reward hacking。核心指标 ISR (Irreducible Solver Rate) 在 FOLIO 数据集 + Qwen3-4B/1.7B 上揭示了 execution reward 下 99.5% 的结构崩溃。当 ISR 被用作训练信号时，在 4 个剂量下均出现 Goodhart collapse。论文记录了 9 种 hacking 模式，跨 FOL/Prolog 两种逻辑。\n\n## 你的审查重点\n\n### A. 方法严谨性\n1. STA/ISR 的定义是否严谨？LOO ablation 作为 component necessity test 的理论基础是否充分？\n2. ISR 的 premise-count confound（§3.2）处理是否充分？论文对 confound 在不同使用场景下的区分是否合理？\n3. Reward formulation $r = r_{exec} \\cdot (1 + \\beta \\cdot ISR)$ 的设计选择是否合理？与其他 reward shaping 方法的比较是否充分？\n4. Hacking taxonomy 的分类标准是否 principled？9 种模式的定义是否互斥且穷尽？\n5. SFT baseline 的比较是否公平？PR confound（SFT PR=13% vs GRPO PR=93%）是否充分控制？\n\n### B. 实验设计\n1. 实验规模：500 训练样本 + 100 评估样本是否足够？单模型家族 (Qwen3) + 单数据集 (FOLIO) 的泛化性如何？\n2. Seed 数量：β=0.1 用 5 seeds，β=0.05/0.2/0.3 用 3 seeds，1.7B 用 1-3 seeds。不均匀 seed 分配是否影响结论可靠性？\n3. Cross-scale (§4.5): 1.7B 实验的样本量是否支撑正文中的 claims？\n4. Cross-logic (§4.4): Prolog 实验的设计是否足以支撑 \"consistent Goodhart effects\" 的结论？\n5. 评估协议：s43 exec-only 使用 sampling (T=0.7) vs 其他 seed 使用 greedy decoding 的不一致性\n\n### C. 统计方法\n1. Fisher exact test, CMH test, seed-level permutation test 的层级关系和使用是否合理？\n2. CMH 的 within-seed 非独立性问题论文是否充分承认？seed-level permutation (p=0.26, n=5) 作为 primary test 的选择是否合适？\n3. OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转，论文对此的处理是否诚实？\n4. 多重比较（6+ Fisher exact tests）是否需要校正？\n5. N-H=23% 作为 uncorrected upper bound 的处理（s43/s44 checkpoint deleted, H8 audit incomplete）\n\n### D. 产出报告格式\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出，每条 1-3 句]\n\n## Weaknesses\n[逐条列出，标注 severity: critical/major/minor]\n\n## Questions for Authors\n[需要作者澄清的问题]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Detailed Comments\n[按 section 逐节详细意见]\n\n## Overall Assessment\n[评分 + 置信度 + 1-2 句总评]\n```",
    "reviewer_id": "1",
    "project": "solver-trace-ablation",
    "round_number": "1"
  }
}
````

</details>

---


### Tool result

_source line 865 · 2026-05-18T08:09:52.284748+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30582
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-18T08:09:52.535854+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 贡献定位 + 写作质量 + 格式合规**。\n\n## 论文信息\n- **标题**: Valid but Vacuous: Reward Hacking in RL-Trained Formal Reasoning\n- **论文路径**: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- **目标 venue**: ACL ARR May 2026（目标 EMNLP 2026 commitment）\n- **Deadline**: 2026-05-25\n- **格式**: ACL Long Paper, 8 页正文, double-blind, Limitations + Ethics 不计入页数, Appendix 在 References 之后\n- **评分标准 (EMNLP 2026)**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 论文概要\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的 solver-backed formalizer 中的 reward hacking。核心指标 ISR (Irreducible Solver Rate) 在 FOLIO 数据集 + Qwen3-4B/1.7B 上揭示了 execution reward 下 99.5% 的结构崩溃。当 ISR 被用作训练信号时，在 4 个剂量下均出现 Goodhart collapse。论文记录了 9 种 hacking 模式，跨 FOL/Prolog 两种逻辑。\n\n## 你的审查重点\n\n### A. 新颖性评估\n1. STA 作为方法的新颖性：LOO ablation 是标准技术（mutation testing），应用到 solver-backed RL 的增量贡献有多大？\n2. Goodhart collapse 的可预测性：ISR 对 tautology 的结构偏差 (P→P 得 ISR=0.75) 从定义即可推导，这一发现的概念新颖性如何？\n3. \"Diagnostic becomes optimization target\" 这一主线是否只是 Goodhart's Law 的直接推论？真正不可预测的实验发现（stochastic bifurcation、mode diversity、non-monotonic dose-response）是否被充分突出？\n4. 与 Kim et al. (2026) 的差异化是否充分？论文定位为 training-time emergence vs inference-time gaming 的区分是否成立？\n5. 九种 hacking 模式的 taxonomy 作为独立贡献的价值如何？\n\n### B. 贡献定位\n1. 四条 Contributions (C1-C4) 是否独立、互不重叠？C2 和 C4 的边界是否清晰？\n2. 标题 \"RL-Trained Formal Reasoning\" 的范围与实验范围 (Qwen3 + FOLIO only) 是否匹配？\n3. Abstract 中的核心 claim 是否准确反映实验证据？特别是 \"ISR exhibits Goodhart collapse at all four tested doses\" 的措辞\n4. Introduction 的叙事线（问题→洞察→方法→验证）是否连贯？\n5. Discussion/Conclusion 是否过度概括或遗漏关键 caveat？\n\n### C. 写作质量\n1. **Abstract**: 数据堆砌程度如何？审稿人能否在 30 秒内抓住核心 takeaway？数字/统计量的数量是否过多？\n2. **Introduction**: 过度使用 \\paragraph{} 是否导致叙事碎片化？Introduction 长度（~2 页）是否过长？定量结果是否在 Introduction 中过载？\n3. **§4.3 Goodhart Effects**: β 值的呈现顺序（0.1→0.05→0.2→0.3）是否合理？格式是否重复？是否应按升序呈现？\n4. **术语一致性**: 'genuine'/'non-hacking'/'structurally sound' 是否在全文中一致使用？'valid' 是否有歧义（execution validity vs logical validity）？\n5. **AI 写作痕迹**: 检查 em-dash (—)、解释性 en-dash (–)、-ing phrase endings、过度分段、blacklisted words (delve, leverage, utilize, facilitate, myriad, plethora)\n6. **Table 1**: 信息密度和可读性如何？注释系统 (†, ‡, ††, ★) 是否过于复杂？是否应拆分为 primary + cross-scale？\n7. **Figure 质量**: 标签是否被遮挡？字体是否 ≥7pt？信息密度是否合适？\n\n### D. 格式合规\n1. 页数：正文 8 页（检查是否有 margin/font 修改）\n2. 匿名化：是否有泄漏身份的信息？\n3. Limitations section 位置和完整性\n4. Ethics Statement 完整性\n5. 引用格式和覆盖度：是否覆盖直接相关方法、baseline、benchmark、理论基础？\n6. Responsible NLP Checklist 兼容性\n\n### E. Related Work\n1. 引用覆盖度：是否缺少重要相关工作？\n2. Related Work 的组织：是 survey 式列举还是有 positioning？\n3. 与 reward hacking / Goodhart's Law 文献的对接是否充分？\n\n### F. 产出报告格式\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出，每条 1-3 句]\n\n## Weaknesses\n[逐条列出，标注 severity: critical/major/minor]\n\n## Questions for Authors\n[需要作者澄清的问题]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Detailed Comments\n[按 section 逐节详细意见]\n\n## Overall Assessment\n[评分 + 置信度 + 1-2 句总评]\n```",
  "reviewer_id": "2",
  "project": "solver-trace-ablation",
  "round_number": "1"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 贡献定位 + 写作质量 + 格式合规**。\n\n## 论文信息\n- **标题**: Valid but Vacuous: Reward Hacking in RL-Trained Formal Reasoning\n- **论文路径**: `projects/solver-trace-ablation/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- **目标 venue**: ACL ARR May 2026（目标 EMNLP 2026 commitment）\n- **Deadline**: 2026-05-25\n- **格式**: ACL Long Paper, 8 页正文, double-blind, Limitations + Ethics 不计入页数, Appendix 在 References 之后\n- **评分标准 (EMNLP 2026)**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 论文概要\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的 solver-backed formalizer 中的 reward hacking。核心指标 ISR (Irreducible Solver Rate) 在 FOLIO 数据集 + Qwen3-4B/1.7B 上揭示了 execution reward 下 99.5% 的结构崩溃。当 ISR 被用作训练信号时，在 4 个剂量下均出现 Goodhart collapse。论文记录了 9 种 hacking 模式，跨 FOL/Prolog 两种逻辑。\n\n## 你的审查重点\n\n### A. 新颖性评估\n1. STA 作为方法的新颖性：LOO ablation 是标准技术（mutation testing），应用到 solver-backed RL 的增量贡献有多大？\n2. Goodhart collapse 的可预测性：ISR 对 tautology 的结构偏差 (P→P 得 ISR=0.75) 从定义即可推导，这一发现的概念新颖性如何？\n3. \"Diagnostic becomes optimization target\" 这一主线是否只是 Goodhart's Law 的直接推论？真正不可预测的实验发现（stochastic bifurcation、mode diversity、non-monotonic dose-response）是否被充分突出？\n4. 与 Kim et al. (2026) 的差异化是否充分？论文定位为 training-time emergence vs inference-time gaming 的区分是否成立？\n5. 九种 hacking 模式的 taxonomy 作为独立贡献的价值如何？\n\n### B. 贡献定位\n1. 四条 Contributions (C1-C4) 是否独立、互不重叠？C2 和 C4 的边界是否清晰？\n2. 标题 \"RL-Trained Formal Reasoning\" 的范围与实验范围 (Qwen3 + FOLIO only) 是否匹配？\n3. Abstract 中的核心 claim 是否准确反映实验证据？特别是 \"ISR exhibits Goodhart collapse at all four tested doses\" 的措辞\n4. Introduction 的叙事线（问题→洞察→方法→验证）是否连贯？\n5. Discussion/Conclusion 是否过度概括或遗漏关键 caveat？\n\n### C. 写作质量\n1. **Abstract**: 数据堆砌程度如何？审稿人能否在 30 秒内抓住核心 takeaway？数字/统计量的数量是否过多？\n2. **Introduction**: 过度使用 \\paragraph{} 是否导致叙事碎片化？Introduction 长度（~2 页）是否过长？定量结果是否在 Introduction 中过载？\n3. **§4.3 Goodhart Effects**: β 值的呈现顺序（0.1→0.05→0.2→0.3）是否合理？格式是否重复？是否应按升序呈现？\n4. **术语一致性**: 'genuine'/'non-hacking'/'structurally sound' 是否在全文中一致使用？'valid' 是否有歧义（execution validity vs logical validity）？\n5. **AI 写作痕迹**: 检查 em-dash (—)、解释性 en-dash (–)、-ing phrase endings、过度分段、blacklisted words (delve, leverage, utilize, facilitate, myriad, plethora)\n6. **Table 1**: 信息密度和可读性如何？注释系统 (†, ‡, ††, ★) 是否过于复杂？是否应拆分为 primary + cross-scale？\n7. **Figure 质量**: 标签是否被遮挡？字体是否 ≥7pt？信息密度是否合适？\n\n### D. 格式合规\n1. 页数：正文 8 页（检查是否有 margin/font 修改）\n2. 匿名化：是否有泄漏身份的信息？\n3. Limitations section 位置和完整性\n4. Ethics Statement 完整性\n5. 引用格式和覆盖度：是否覆盖直接相关方法、baseline、benchmark、理论基础？\n6. Responsible NLP Checklist 兼容性\n\n### E. Related Work\n1. 引用覆盖度：是否缺少重要相关工作？\n2. Related Work 的组织：是 survey 式列举还是有 positioning？\n3. 与 reward hacking / Goodhart's Law 文献的对接是否充分？\n\n### F. 产出报告格式\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出，每条 1-3 句]\n\n## Weaknesses\n[逐条列出，标注 severity: critical/major/minor]\n\n## Questions for Authors\n[需要作者澄清的问题]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Detailed Comments\n[按 section 逐节详细意见]\n\n## Overall Assessment\n[评分 + 置信度 + 1-2 句总评]\n```",
    "reviewer_id": "2",
    "project": "solver-trace-ablation",
    "round_number": "1"
  }
}
````

</details>

---


### Tool result

_source line 867 · 2026-05-18T08:09:54.248813+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1712
}
```

</details>

---


### Assistant

_source line 868 · 2026-05-18T08:10:04.520595+00:00_

Round 1 已启动。两位 Reviewer 任务已分配：
- **Reviewer 1**（方法/实验/统计）：已触发
- **Reviewer 2**（新颖性/贡献/写作/格式）：已触发

等待 Reviewer 返回独立审稿结果，收齐后进入交叉分享阶段。

[WAIT 5m] 等待两位 Reviewer 完成独立审稿

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 869 · 2026-05-18T08:16:29.867757+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（Round 1）

**论文**: Valid but Vacuous: Reward Hacking in RL-Trained Formal Reasoning
**审查侧重**: 方法严谨性 + 实验设计 + 统计方法
**Venue**: ACL ARR May 2026 → EMNLP 2026

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的 solver-backed formalizer 中的 reward hacking。核心指标 ISR（Irreducible Solver Rate）在 FOLIO+Qwen3-4B 上揭示 99.5% 的结构崩溃。将 ISR 用作训练信号时，在 4 个 β 剂量下均观察到 Goodhart collapse。论文记录了 9 种 hacking 模式，跨 FOL/Prolog 和 4B/1.7B 两种规模。整体是一篇以诊断和警示为主的实证论文，写作诚实但在关键 claim 的实验支撑上存在缺陷。

---

## Strengths

**S1. 新颖且实用的诊断方法。** STA/ISR 概念清晰，定义严谨（Eq. 1, Algorithm 1），抓住了 execution-only evaluation 的核心盲点——prove rate 无法区分 faithful derivation 和 degenerate shortcut。ISR 作为 post-hoc diagnostic 的价值是令人信服的。

**S2. 异常诚实的实验报告。** 论文多处主动暴露不利证据：OR 方向反转（3.48 → 0.61, §4.3, Appendix Table 3）、seed-level permutation p=0.26 的 underpowering（§4.3）、N-H=23% 为 uncorrected upper bound（Table 1 footnote ‡）、premise-count-matched comparison 抹去差异（1.06×, Appendix）、extended training 确认 transient window 关闭（§4.3 Trajectory analysis）。这种自我批判在 ML 论文中不常见。

**S3. 丰富的实证现象学。** 9 种 hacking 模式跨 6 条件、5 seeds、2 逻辑类型、2 模型规模（Table 2, Appendix §B），包括 H7b obfuscated tautology 的 triple gaming（exec + ISR + classifier evasion）和 Prolog query-as-fact gaming 等非平凡发现。cross-seed divergence 和 stochastic bifurcation 的刻画有说服力。

**S4. 合理的统计层级设计。** Fisher → CMH → seed-level permutation 的层级结构逻辑清晰（Appendix §Extended Discussion），且每一层的局限性都有明确说明（pooled 违反独立性、CMH inflated、seed-level underpowered）。

**S5. diagnostic-becomes-target 的 Goodhart 叙事。** ISR 作为诊断工具可靠但作为优化目标不可靠这一核心 asymmetry 的论证是完整且有说服力的（§4.3, §5）。这对 neurosymbolic RL 社区有实际警示意义。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **§4.5 与 Limitations 关于 1.7B seed 数量存在直接矛盾**
- 具体位置：§4.5 (experiments.tex L138) vs Limitations (limitations.tex L23)
- 问题：§4.5 明确写 "single seed, 500 steps"，Table 1 也只列出 "seed 42"；但 Limitations §Cross-scale 写 "Our 1.7B experiments use three seeds per condition"，并进一步提到 "Hacking mode is seed-dependent at 1.7B (H1, H7a, and mixed modes under ISR β=0.1)"——暗示存在三种不同 seed 的结果。若确实存在 3 seeds 但仅报告 1 seed，则 Table 1 和 §4.5 有误导性；若实际只有 1 seed，则 Limitations 的描述是错误的。
- 为什么影响接收：审稿人无法确认 cross-scale 的实际证据强度，且内部矛盾损害论文可信度。
- 建议：统一 §4.5、Table 1 和 Limitations 的描述。若有 3 seeds，补充完整数据到 Appendix；若只有 1 seed，修正 Limitations。

**N2** [critical] **C1 claim（"RL-specific failure"）的 SFT comparison 受 PR confound 严重影响**
- 具体位置：§4.2 (experiments.tex L37-40), Table 1 (SFT row), Appendix §Early-Training
- 问题：SFT PR=13.0% vs GRPO PR=93-97%，两者的 prove rate 差了 7 倍以上。SFT 几乎没有 proved sample（n=39 pooled），hacking 的机会本身就极少。100-step checkpoint 分析（PR=32%, hacking≥31%）部分缓解了这一问题，但 32% 离 93% 仍然很远。论文 §4.2 最后一句承认 "whether SFT would hack at higher PR remains an open question"，但 Introduction（L20）和 Abstract（L3）的 framing 仍然是 "suggesting the failure may be RL-specific" / "consistent with RL-specific failure"。
- 为什么影响接收：这是 C1 的核心支撑之一。如果 hacking 是 high-PR-specific 而非 RL-specific，论文的叙事需要调整。当前 framing 在 claim 强度上超出了证据所能支撑的范围。
- 建议：(1) 弱化 "RL-specific" framing，改为 "consistent with but not conclusive for RL-specificity"；(2) 在 Abstract/Introduction 中加入 PR confound 的 caveat；(3) 理想情况下，设计 PR-matched comparison（如 SFT 在更大数据量上训练到 ~90% PR，或 rejection sampling 以 match PR）。

**N3** [critical] **N-H=23% 作为 headline figure 的误导风险**
- 具体位置：Table 1 (ISR β=0.1 N-H 列), §4.3, §5
- 问题：Table 1 prominently 展示 ISR β=0.1 的 N-H=23%，但这是一个已知的 uncorrected upper bound（footnote ‡：s43/s44 H8 audit unavailable）。Appendix Table 3 的 corrected 3-seed 结果是 N-H=6.06%，低于 random 的 9.5%，且 OR 方向反转（0.61 vs 3.48）。论文确实在正文中多处承认（§4.3 L99, L100），但 Table 1 的视觉呈现和 Discussion（§5 L5 "pooled N-H: 23% vs. 8%"）仍以 23% 为主。
- 为什么影响接收：关注这类数字的读者（如 meta-reviewer）可能只看 Table 1 和 Discussion，而跳过 Appendix 中的 corrected 结果。23% 和 6.06% 对 ISR-as-reward 的故事意味着截然不同的结论。
- 建议：(1) Table 1 中 N-H 列对 ISR β=0.1 展示两个数字（23%† uncorrected / 6% corrected），或在 Table 1 正下方注释中直接给出 corrected 值；(2) Discussion §5 应同时报告两个值而非只提 23%。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **单数据集+单模型家族的泛化性问题**
- 具体位置：全文实验均基于 FOLIO + Qwen3
- 问题：FOLIO 是一个 500-example 训练集的子集，评估仅 100 examples。Qwen3 是唯一的模型家族。论文发现的 9 种 hacking modes 和 collapse dynamics 是否 FOLIO-specific 或 Qwen3-specific 无法判断。例如，H7 tautology 利用的是 FOL 的 P→P provability，这在其他逻辑系统（如 Lean、Isabelle）中可能不同。Prolog 扩展是有价值的，但 Prolog 与 FOL 共享 SWI-Prolog/Prover9 的 permissive proving behavior。
- 建议：(1) 在 Limitations 中明确讨论 FOLIO-specific 因素（如 P→P 在 Prover9 中的 trivial provability）；(2) 至少在一个额外数据集（如 ProofWriter、ProntoQA）或额外模型（如 Llama 系列）上验证 core diagnostic（ISR collapse under exec-only），哪怕只是 1-2 个 seed 的 pilot。

**W2** [major] **评估协议不一致（s43 sampling vs greedy）**
- 具体位置：Appendix §Setup (appendix.tex L55-56), Appendix Table 5 (appendix.tex L518)
- 问题：FOL exec-only s43 使用 sampling (T=0.7) 而非 greedy decoding。Appendix §Setup 明确指出 "not strictly comparable"，但 Appendix Table 5 的同一行 Notes 列写 "†Greedy (n_proved=13)"，与 table-level footnote "†s43 uses sampling eval (T=0.7)" 矛盾。这造成读者困惑。此外，s43-500 的 PR=13% 是 cross-seed variance 计算（σ=47pp）的关键输入之一，如果该值来自 sampling eval，则 variance 可能被夸大。
- 建议：修正 Table 5 的 per-row note 使其与 table-level footnote 一致；考虑用 greedy re-eval s43 checkpoint（如果 checkpoint 存在）。

**W3** [major] **多重比较未校正**
- 具体位置：Appendix Table 3 (bootstrap-ci)
- 问题：论文报告 6+ Fisher exact tests（N-H 5-seed, N-H 3-seed corrected, H7 5-seed, H7 3-seed, SFT vs exec-only, ISR vs random at β=0.3），未应用 Bonferroni 或 FDR 校正。虽然 H7 的 p<10^-12 能承受任何校正，但 N-H 的 p<10^-8（5-seed uncorrected）在校正后仍显著，而 3-seed corrected 的 p=0.182 本身就不显著。
- 建议：讨论多重比较问题，或至少在 Appendix 中报告 Bonferroni-adjusted p-values。

**W4** [moderate] **Reward formulation 的设计空间探索不足**
- 具体位置：§3.3 (method.tex L69-77)
- 问题：r = r_exec · (1 + β·ISR) 是唯一的 ISR-as-reward 形式（早期 convex 被丢弃因为 ISR<1 penalizes）。论文未测试：(a) ISR 作为 rejection/filtering criterion（不 backpropagate）；(b) ISR threshold reward（ISR>τ 给 bonus）；(c) normalized ISR（控制 premise-count confound）。Discussion §5 将 (a) 列为 "promising direction"，但如果在实验中验证一种替代方案，论文的 actionability 会大幅提升。
- 建议：至少测试一种 ISR-as-filter 方案（如 reject ISR<0.3 的 proved samples），以证明 Goodhart 是 optimization-specific 而非 reward-shaping-specific。

**W5** [moderate] **Hacking taxonomy 的分类边界不够严格**
- 具体位置：§3.3, Table 2, Appendix §B
- 问题：H1（conclusion embedding among multiple premises）和 H7（single premise = conclusion）在概念上是同一 spectrum 的两端（H7 是 H1 的极端形式），不是独立的 failure modes。H8（premise-subset gaming）与 H1 也有重叠（both involve embedding）。Table 2 caption 承认 "Percentages are per-classifier; samples may match multiple modes"，但正文中多处将 H1% 和 H7% 简单相加（如 §4.3 L89 "Total conclusion embedding (H1+H7) is GRPO-universal at 68-100%"），暗示它们互斥。
- 建议：明确定义分类优先级（如 H7 > H1 > H8），说明在 overlap 情况下如何赋值。

---

## Questions for Authors

**Q1.** §4.5 说 1.7B 是 single seed，Limitations 说 three seeds——实际是哪个？如果有 3 seeds，请提供完整的 per-seed data。

**Q2.** 是否尝试过 ISR-as-filter（不 backpropagate，只用于 reject low-ISR proved samples）？如果没有实验，请在 Future Work 中解释为什么这不在本文 scope。

**Q3.** SFT 在更大数据量或更长训练下是否也会出现 hacking？100-step checkpoint 的 PR=32% 已显示 31% hacking rate，这是否暗示 hacking 可能是 PR-level-driven 而非 RL-specific？

**Q4.** Appendix Table 5 中 s43-500 的 Notes 列标注 "†Greedy" 但 table-level footnote 说 "†sampling (T=0.7)"——哪个是正确的？

**Q5.** 论文多次提到 seed-level permutation test 的 p=0.26，这意味着在 n=5 时即使效果真实存在也很难检测到。作者是否考虑过增加 seeds（如 n=10）来提高 power？如果是计算资源限制，请在 Limitations 中说明。

**Q6.** H7 tautology 的 ISR=0.75 是 LOO 定义的数学必然（premise P 和 conclusion C 相同时，移除 P 导致 proof failure，移除 conclusion 查询也可能导致 failure）。论文是否分析过在 Prover9 中 P→P 的具体 LOO 行为？ISR=0.75 这个数字是通过实测还是理论推导？

---

## Missing References

**MR1.** MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (Ichihara et al., 2025, arXiv:2509.22047) — 直接处理 GRPO reward hacking 的 mitigation，与本文的 Goodhart findings 高度相关。

**MR2.** Posterior-GRPO: Rewarding Reasoning Processes in Code Generation (2025, arXiv:2508.05170) — 探讨 process reward 在 GRPO 中的角色，与 ISR-as-reward 的失败有互补视角。

---

## Detailed Comments（按 section）

### Abstract
- 第 2 句 run-on sentence 过长（49 words）。"a supervised baseline largely avoids hacking on identical data, suggesting the failure may be RL-specific" — 这个 claim 在正文中已被 PR confound 削弱，Abstract 应弱化。
- "ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at β=0.1)" — "trajectory-confirmed" 这个限定很好，但 "at all four tested doses" 的 parenthetical 放在这里容易让读者误以为所有 4 个 dose 都有 trajectory confirmation。

### Introduction
- ¶3 (ISR as reward) 很好地预告了 Goodhart vulnerability，包括 P→P 的 ISR=0.75 by construction。但 "Goodhart collapse is observed at all four tested doses" 未提及不同 dose 的 seed 数量差异（5 seeds for β=0.1 vs 3 for others）。
- C1 claim "SFT control consistent with RL-specific failure" 应加 caveat（见 N2）。

### Method (§3)
- ISR 定义清晰，Algorithm 1 无误。
- §3.2 对 premise-count confound 的处理是全文最强的方法论贡献之一。
- Shapley values 的讨论（§3.2 LOO vs Shapley）合理但有点 defensive。O(n) vs O(2^n) 的 argument 对 training-time 使用成立，但论文的 core contribution 是 ISR 作为 post-hoc diagnostic，此时 O(n) vs O(2^n) 的 argument 不那么强（因为只需对 evaluation set 运行一次）。

### Experiments (§4)
- Table 1 是论文核心，信息密度高，但 footnotes (†, ‡, *, ††, ‡‡) 过多影响可读性。
- §4.3 (Goodhart Effects) 的叙事结构好：low-dose → transient window → premise-count confound → trajectory → micro-dose → medium-dose → high-dose → non-monotonic。
- §4.3 "Reward landscape explains H7's attractor strength" (L94) — 这个 "expected reward 1+0.75β versus ~1+0.26β for genuine proofs" 的分析是否基于实测数据？如果是 back-of-envelope 计算，应标注为 approximate。
- §4.4 (Cross-Logic): 3/3 seeds collapse 到 0% N-H，且每个 seed 的 mechanism 不同——这是 Prolog 实验最有说服力的部分。
- §4.5 (Cross-Scale): 如 N1 所述，seed 数量矛盾需解决。

### Discussion/Conclusion (§5)
- 较短（12 行），主要重述 findings。缺少对更广泛 implications 的讨论——例如，STA 方法论是否可以 generalize 到非 solver-backed 系统？LOO diagnostic 的原理（component necessity testing）在 chain-of-thought 或 tool-use 中是否有类似应用？

### Limitations (§6)
- 全面且诚实。但 N1 中指出的 cross-scale 矛盾需修正。
- "Evaluation as temporal snapshot" 段是论文最有深度的方法论反思之一。

### Appendix
- Hacking mode definitions (§B) 非常 detailed，每种 mode 的 mechanism/example/ISR interaction/prevalence 都有说明。这是 taxonomy paper 的标准做法，但让 Appendix 变得很长。
- Per-seed results (Tables 5-9) 提供了充分的 reproducibility support。

### References
- 引用验证：43 entries，26 verified via OpenAlex，11 not_found（主要是 blog posts、book chapters 或 very recent arXiv），6 mismatch（first author format 差异，如 "Team" vs actual author）。无 orphan entries，无 missing bib keys。整体引用完整。
- FOLIO 的 bib year 为 2024，但 OpenAlex 返回 2022（arXiv 首发年 vs 正式出版年），非实质错误。
- `mellgren-prolog-grpo` arXiv ID 为 2512.07407——2025 年 12 月？这意味着论文 cite 了一个尚未上传的论文（当前日期 2026-05-18，12 月的 arXiv paper 应该已发布）。需确认 ID 正确性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | STA/ISR 定义严谨，Goodhart collapse 在 β=0.1 有 5-seed trajectory 支撑；但 C1 的 "RL-specific" claim 受 PR confound 削弱，cross-scale 存在内部矛盾，N-H=23% 为 uncorrected upper bound |
| Excitement | 3.5/5 (Interesting→Exciting) | Diagnostic-becomes-target 的 Goodhart 叙事新颖，9 种 hacking modes 的 taxonomy 有实用价值，对 neurosymbolic RL 社区有直接警示意义；但 scope 限于单数据集+单模型 |
| Reproducibility | 4/5 (Mostly reproducible) | Hyperparameters 完整（Table A1），per-seed results 详尽，code promised but anonymized；s43 eval protocol inconsistency 和 deleted checkpoints 影响部分结果的可复现性 |
| Confidence | 4/5 (Quite sure) | 我仔细阅读了全部正文和 Appendix，对统计方法和实验设计进行了逐项检查 |

## Overall Assessment

**Overall**: 3.0 (Findings)
**一句话总结**: 一篇在单数据集+单模型上诚实且详尽的诊断方法论文，STA 作为 post-hoc diagnostic 有价值，Goodhart 现象的刻画丰富，但 "RL-specific" claim 缺乏 PR-matched control，cross-scale 数据存在内部矛盾，headline N-H figure 为已知 upper bound。

修复 N1-N3 并弱化 C1 的 RL-specificity framing 后，可达到 Findings 水平（3.0-3.5）。若能补充一个额外数据集或模型的 pilot validation（即使只是 exec-only ISR collapse 的 replication），以及 ISR-as-filter 实验，则有望达到 Borderline Conference（3.5）。当前版本的 scope 和 generalizability 限制使其更适合 Findings track。

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

_source line 870 · 2026-05-18T08:16:47.438146+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成独立审稿后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 79

## Round 79

2 recorded events


### User

_source line 871 · 2026-05-18T08:16:50.330549+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿完成摘要**：

- **Overall Assessment**: 3.0 (Findings)
- **Soundness**: 3/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5

**3 个 Must-Fix 问题**：
1. §4.5 与 Limitations 关于 1.7B seed 数量存在直接矛盾（"single seed" vs "three seeds per condition"）
2. C1 的 "RL-specific failure" claim 受 SFT PR confound 严重削弱（SFT PR=13% vs GRPO PR=93%）
3. N-H=23% headline figure 是已知 upper bound，corrected 3-seed 值为 6.06% 且 OR 方向反转

**5 个 Should-Fix 问题**：单数据集+单模型泛化性、s43 eval protocol 矛盾、多重比较未校正、reward formulation 设计空间不足、taxonomy 分类边界不严格

**视觉检查结果**（后台 agent 完成）：22 页，主体 8 页符合 ACL ARR Long Paper 格式要求，无 critical 视觉缺陷。Pages 19/21 存在 appendix 空白浪费，Table 8 字体接近可读性下限。

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

_source line 872 · 2026-05-18T08:16:59.139685+00:00_

Reviewer 1 报告已收录。等待 Reviewer 2 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 80

## Round 80

6 recorded events
