# Director coordination — Part 12 of 12

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[← Part 11](part-011.md) · [Transcript overview](../director-coordination-copy-2.md) · [Structured JSON](../../../sessions/b1/b1d47a1a2aa91fd38090.json)

## Round 293

### Tool call

_source line 3262 · 2026-05-25T05:10:39.762122+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 34\n  resolution: \"Compositional narrative + screening trigger 定位。method.tex L54 显式定位 ISR 为 screening trigger。\"\n  resolution_round: 34\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 33\n  resolution: \"Compositional Goodhart reframed. χ² as primary evidence.\"\n  resolution_round: 33\n\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R1 S3 + R2 N2 均再次提出。R2 错误标注为 1B。实际为 4B。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1+R2 均再次提出。R1 补充 8B post-hoc 解释不可证伪、单训练算法(GRPO K=4)限制。Claims 已 scope to Qwen3-4B。\"}\n  resolution: \"结构性限制。Claims scoped to Qwen3-4B.\"\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 34\n  resolution: \"Table 5 caption 增加 descriptive-only 限定 + CMH 引用。\"\n  resolution_round: 34\n\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1], note: \"R1 M2: seed 43 评估协议不一致。此前已在正文 L65 说明，但 R1 认为不够显著。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1 W1 + R2 同意。正文脚注 + N=2 sensitivity 已充分披露。当前处理到位。\"}\n  resolution: \"正文 N=2 统计句（experiments.tex L65）+ Appendix D.6。复发×3 后从 footnote 升级到正文。\"\n  resolution_round: 34\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R2 N1 再次提出为 critical。R1 rebut 称机制分析超越 generic Goodhart 但同意 C1 overclaim。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1+R2 均同意新颖性有限但实证深度有价值。C1 已修正为 systematic empirical analysis。\"}\n  resolution: \"R35 修复：C1 从 'we propose STA' 降级为 'systematic empirical analysis using LOO ablation'。\"\n  resolution_round: 35\n\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: \"Reframed as empirical instantiation of Goodhart's Law.\"\n  resolution_round: 31\n\n- id: v30-R1-W1\n  summary: \"SFT baseline selection bias\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"SFT positioned as pre-RL temporal reference.\"\n  resolution_round: 31\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 22\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [2], note: \"R2 提出替代假设：PR=15% 可能意味着模型未收敛而非信号打乱阻止 gaming。见 v36-R2-W2。\"}\n  resolution: \"Positioned as corroborating rather than definitive.\"\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy recall 未评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 34\n  resolution: \"Limitations 增加 recall 自约束论证：precision=100% + measured N-H=6% 约束 recall ≥94%。\"\n  resolution_round: 34\n\n- id: v19-R12-W3\n  summary: \"ProofFOL 跨数据集证据过度声称（Abstract 'persists across dataset families'）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R1+R2 强共识：Abstract 'persists across dataset families' 仍具误导性。ProofFOL ISR-as-reward 方向可能相反（矫正性），不应作为 asymmetry 持续存在的证据。R1 Round 2 验证 TeX 源码确认论文自身承认 ISR 在 ProofFOL 上 'effectively corrective'（experiments.tex L113），与 abstract 'supported by' 直接矛盾。\"}\n  action_items:\n    - {round: 36, action: \"Abstract 移除 'dataset families' 或改为 'reveals dataset-dependent boundary conditions'\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [1], note: \"R1 N3 再次提出为 critical（ISR-NLI ρ=−0.049）。R2 rebut。Director 裁定 side R2：论文诊断逻辑不依赖 ISR-NLI 相关性，method.tex L54 定位清晰。降为 info。\"}\n  resolution: \"'reasoning quality' → 'formalization integrity'.\"\n  resolution_round: 32\n\n- id: v33-N2-BIMODAL\n  summary: \"5-seed 双峰弱化 Goodhart 核心叙事\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"C2 changed to 'seed-dependent Goodhart effect'.\"\n  resolution_round: 33\n\n- id: v33-W1-EXEC-POOLING\n  summary: \"Table 1 exec-only 仅报告 s42\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"§4.2 explains. Table 1 footnote expanded.\"\n  resolution_round: 33\n\n- id: v33-M8-CONVERTS\n  summary: \"'ISR converts CE into TS' 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"'converts' → 'systematically selects for TS over CE'.\"\n  resolution_round: 33\n\n- id: v33-W3-TAXONOMY\n  summary: \"Taxonomy 互斥性和 N-H upper bound 未在正文说明\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"Priority rule and N-H upper bound added to §3.3.\"\n  resolution_round: 33\n\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Nishimura et al. 2026 spec gaming\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"Citation added.\"\n  resolution_round: 31\n\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 32\n  resolution: \"Title shortened.\"\n  resolution_round: 32\n\n- id: v31-R2-ISR0-AMBIGUITY\n  summary: \"ISR=0 语义不同\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"ISR=0 disambiguation added.\"\n  resolution_round: 31\n\n- id: v32-R12-MR-UNFAITHFUL-COT\n  summary: \"缺失引用：Lanham/Turpin\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  resolution: \"Both citations added.\"\n  resolution_round: 32\n\n- id: v34-R12-N1\n  summary: \"C3 贡献声称 overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"C3 establishing→confirming(Prolog)+exploratory(ProofFOL)。Abstract/Conclusion 三处同步。\"\n  resolution_round: 34\n\n- id: v34-R12-N2\n  summary: \"ISR scalar framing 张力\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex L54 ISR screening trigger 定位句。与 L53/L99 形成三处闭环。\"\n  resolution_round: 34\n\n- id: v34-R1-N1\n  summary: \"3-5 seeds proportion claim CI 宽\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"5 seeds CI 仍宽。但正文已改为 existence claim。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1 补充 optional stopping 风险：seeds 45-46 post-hoc 添加可能膨胀 false positive rate。当前 CI + 'can occur' 修正方向正确。\"}\n  resolution: \"R35 修复：Abstract 改为 'can occur'；experiments.tex L65 加 95% Clopper-Pearson CI [11.8%, 88.1%]。\"\n  resolution_round: 35\n\n- id: v34-R1-N2\n  summary: \"Seed 43 sensitivity 可见性不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"正文 L65 N=2 统计句。从 footnote 升级到正文。\"\n  resolution_round: 34\n\n- id: v34-R1-N3\n  summary: \"Table 5 pooled Fisher 缺 descriptive-only 限定\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"Appendix Table 5 caption 增加限定 + CMH 引用。\"\n  resolution_round: 34\n\n- id: v34-R12-W1\n  summary: \"Table 1 caption 过长\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"150 词→48 词。信息无丢失。\"\n  resolution_round: 34\n\n- id: v34-R1-W3\n  summary: \"convergence 因果 claim 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"experiments.tex + conclusion.tex 两处同步弱化。\"\n  resolution_round: 34\n\n- id: v34-R2-W3\n  summary: \"正文信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"§4.4 开头 exploratory signposting。\"\n  resolution_round: 34\n\n- id: v34-R2-W5\n  summary: \"Abstract [anonymized] 脚注\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"已移除。\"\n  resolution_round: 34\n\n- id: v34-R1-W5\n  summary: \"ISR = Shapley 声明缺推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1], note: \"正文措辞仍不精确。\"}\n    - {round: 36, reviewers: [1], note: \"R1 再次提出。R2 rebut（当前措辞充分）。Director 裁定 side R2。\"}\n  resolution: \"R35 修复：正文改为 'LOO marginal contribution, a restriction of the Shapley value to the maximal coalition'。\"\n  resolution_round: 35\n\n- id: v34-REVIEWER-FIG2\n  summary: \"Figure 2 未被正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex 两处引用。\"\n  resolution_round: 34\n\n- id: v34-REVIEWER-CONCL\n  summary: \"conclusion.tex confirm 对 ProofFOL 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"与 C3 同步修改，ProofFOL 标注 exploratory。\"\n  resolution_round: 34\n\n- id: v35-R1-M1\n  summary: \"Exec-only 条件仅 1 seed (s42) 完整报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1], note: \"Exec-only 作为核心 baseline 仅单 seed 结果。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1 W2 + R2 同意展示问题。正文已加 3-seed 1000-step 证据句。\"}\n  resolution: \"R35 修复：experiments.tex L35 加 3-seed 1000-step 证据句（≤6.2% N-H）引用 Table 5。\"\n  resolution_round: 35\n\n- id: v35-R1-M3\n  summary: \"Premise-count confound 对 compositional evidence 未隔离\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"R35 修复：Discussion 加 premise-count confound 承认句 + future work。\"\n  resolution_round: 35\n\n- id: v35-R2-W2\n  summary: \"缺少与 PRM 的 Goodhart susceptibility 对比讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R1 agree。论文引用 PRM 但未讨论 PRM 是否同样面临 Goodhart 风险。\"}\n    - {round: 36, reviewers: [1], note: \"R1 Round 2 仍认为 PRM 对比不充分但 '不影响接收决定'。Conclusion L9 'step-level rewards face analogous considerations' 是唯一联系句，未展开论证。\"}\n  resolution: \"R35 修复：Discussion 加 PRM 安全 framing 句。\"\n  resolution_round: 35\n\n- id: v35-R2-W4\n  summary: \"ISR/ISR* 术语使用不一致（R36 grep: 85 vs 17 occurrences）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R1 agree。§3.2 定义 ISR* 但正文多处省略星号。\"}\n    - {round: 36, reviewers: [1], note: \"R1 Round 2 grep 验证：bare 'ISR' 出现 85 次，'ISR*' 仅 17 次（集中在 Table 1 caption、Appendix、method.tex 定义处）。正文行文几乎全部使用 bare ISR，与 method.tex L56 声明矛盾。ISR vs ISR* 区别影响 claim 解读（是否限定为 proved samples）。\"}\n  action_items:\n    - {round: 36, action: \"全文统一为 ISR* 或在 method 节声明 'ISR hereafter refers to ISR*'\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: v35-R2-MR1\n  summary: \"缺失引用：Krakovna et al. (2020) Specification gaming examples\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R1 agree。Specification gaming 标准参考。\"}\n    - {round: 36, reviewers: [1], note: \"R1 Round 2 确认 related_work.tex L10 已引用 Krakovna et al. (2020)。R2 此条为误判。\"}\n  resolution: \"R35 修复：Related Work 加 Krakovna et al. (2020) 引用。R36 R1 确认已存在。\"\n  resolution_round: 35\n\n- id: v36-R12-N2\n  summary: \"Section 1 'any verifiable proxy' 泛化声称过度\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"从 Qwen3-4B/FOLIO/GRPO-K4 推断到 'any verifiable proxy' 不合理。R1 补充单训练算法和小评估集限制。与 v17-R12-W1 关联但侧重语言修正非实验扩展。\"}\n  action_items:\n    - {round: 36, action: \"Section 1 'any' 改为 'LOO-based structural proxies in comparable settings' 或类似限定\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: v36-R12-W1\n  summary: \"缺少代码和数据可用性声明\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R2 提出，R1 同意。24 页论文无代码/数据发布计划。ARR Reproducibility 维度要求。\"}\n  action_items:\n    - {round: 36, action: \"添加 Data Availability 声明（匿名审稿阶段可用 anonymous repo link）\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: v36-R2-W2\n  summary: \"Shuffled-ISR 低 PR 的替代解释：非收敛而非信号打乱\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [2], note: \"PR=15% 可能表明模型未成功收敛，自然不会 game 任何指标。论文应讨论此混淆因素。与 v22-R1-W4 关联。\"}\n  action_items:\n    - {round: 36, action: \"§4.2 或 Appendix 加一句讨论 non-convergence 替代解释\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 34\n  resolution: \"Compositional narrative + screening trigger 定位。method.tex L54 显式定位 ISR 为 screening trigger。\"\n  resolution_round: 34\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 33\n  resolution: \"Compositional Goodhart reframed. χ² as primary evidence.\"\n  resolution_round: 33\n\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 17\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R1 S3 + R2 N2 均再次提出。R2 错误标注为 1B。实际为 4B。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1+R2 均再次提出。R1 补充 8B post-hoc 解释不可证伪、单训练算法(GRPO K=4)限制。Claims 已 scope to Qwen3-4B。\"}\n  resolution: \"结构性限制。Claims scoped to Qwen3-4B.\"\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 34\n  resolution: \"Table 5 caption 增加 descriptive-only 限定 + CMH 引用。\"\n  resolution_round: 34\n\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1], note: \"R1 M2: seed 43 评估协议不一致。此前已在正文 L65 说明，但 R1 认为不够显著。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1 W1 + R2 同意。正文脚注 + N=2 sensitivity 已充分披露。当前处理到位。\"}\n  resolution: \"正文 N=2 统计句（experiments.tex L65）+ Appendix D.6。复发×3 后从 footnote 升级到正文。\"\n  resolution_round: 34\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R2 N1 再次提出为 critical。R1 rebut 称机制分析超越 generic Goodhart 但同意 C1 overclaim。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1+R2 均同意新颖性有限但实证深度有价值。C1 已修正为 systematic empirical analysis。\"}\n  resolution: \"R35 修复：C1 从 'we propose STA' 降级为 'systematic empirical analysis using LOO ablation'。\"\n  resolution_round: 35\n\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  resolution: \"Reframed as empirical instantiation of Goodhart's Law.\"\n  resolution_round: 31\n\n- id: v30-R1-W1\n  summary: \"SFT baseline selection bias\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"SFT positioned as pre-RL temporal reference.\"\n  resolution_round: 31\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 22\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [2], note: \"R2 提出替代假设：PR=15% 可能意味着模型未收敛而非信号打乱阻止 gaming。见 v36-R2-W2。\"}\n  resolution: \"Positioned as corroborating rather than definitive.\"\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy recall 未评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 34\n  resolution: \"Limitations 增加 recall 自约束论证：precision=100% + measured N-H=6% 约束 recall ≥94%。\"\n  resolution_round: 34\n\n- id: v19-R12-W3\n  summary: \"ProofFOL 跨数据集证据过度声称（Abstract 'persists across dataset families'）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R1+R2 强共识：Abstract 'persists across dataset families' 仍具误导性。ProofFOL ISR-as-reward 方向可能相反（矫正性），不应作为 asymmetry 持续存在的证据。R1 Round 2 验证 TeX 源码确认论文自身承认 ISR 在 ProofFOL 上 'effectively corrective'（experiments.tex L113），与 abstract 'supported by' 直接矛盾。\"}\n  action_items:\n    - {round: 36, action: \"Abstract 移除 'dataset families' 或改为 'reveals dataset-dependent boundary conditions'\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [1], note: \"R1 N3 再次提出为 critical（ISR-NLI ρ=−0.049）。R2 rebut。Director 裁定 side R2：论文诊断逻辑不依赖 ISR-NLI 相关性，method.tex L54 定位清晰。降为 info。\"}\n  resolution: \"'reasoning quality' → 'formalization integrity'.\"\n  resolution_round: 32\n\n- id: v33-N2-BIMODAL\n  summary: \"5-seed 双峰弱化 Goodhart 核心叙事\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"C2 changed to 'seed-dependent Goodhart effect'.\"\n  resolution_round: 33\n\n- id: v33-W1-EXEC-POOLING\n  summary: \"Table 1 exec-only 仅报告 s42\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"§4.2 explains. Table 1 footnote expanded.\"\n  resolution_round: 33\n\n- id: v33-M8-CONVERTS\n  summary: \"'ISR converts CE into TS' 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"'converts' → 'systematically selects for TS over CE'.\"\n  resolution_round: 33\n\n- id: v33-W3-TAXONOMY\n  summary: \"Taxonomy 互斥性和 N-H upper bound 未在正文说明\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"Priority rule and N-H upper bound added to §3.3.\"\n  resolution_round: 33\n\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Nishimura et al. 2026 spec gaming\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"Citation added.\"\n  resolution_round: 31\n\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 32\n  resolution: \"Title shortened.\"\n  resolution_round: 32\n\n- id: v31-R2-ISR0-AMBIGUITY\n  summary: \"ISR=0 语义不同\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"ISR=0 disambiguation added.\"\n  resolution_round: 31\n\n- id: v32-R12-MR-UNFAITHFUL-COT\n  summary: \"缺失引用：Lanham/Turpin\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  resolution: \"Both citations added.\"\n  resolution_round: 32\n\n- id: v34-R12-N1\n  summary: \"C3 贡献声称 overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"C3 establishing→confirming(Prolog)+exploratory(ProofFOL)。Abstract/Conclusion 三处同步。\"\n  resolution_round: 34\n\n- id: v34-R12-N2\n  summary: \"ISR scalar framing 张力\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex L54 ISR screening trigger 定位句。与 L53/L99 形成三处闭环。\"\n  resolution_round: 34\n\n- id: v34-R1-N1\n  summary: \"3-5 seeds proportion claim CI 宽\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"5 seeds CI 仍宽。但正文已改为 existence claim。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1 补充 optional stopping 风险：seeds 45-46 post-hoc 添加可能膨胀 false positive rate。当前 CI + 'can occur' 修正方向正确。\"}\n  resolution: \"R35 修复：Abstract 改为 'can occur'；experiments.tex L65 加 95% Clopper-Pearson CI [11.8%, 88.1%]。\"\n  resolution_round: 35\n\n- id: v34-R1-N2\n  summary: \"Seed 43 sensitivity 可见性不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"正文 L65 N=2 统计句。从 footnote 升级到正文。\"\n  resolution_round: 34\n\n- id: v34-R1-N3\n  summary: \"Table 5 pooled Fisher 缺 descriptive-only 限定\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"Appendix Table 5 caption 增加限定 + CMH 引用。\"\n  resolution_round: 34\n\n- id: v34-R12-W1\n  summary: \"Table 1 caption 过长\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"150 词→48 词。信息无丢失。\"\n  resolution_round: 34\n\n- id: v34-R1-W3\n  summary: \"convergence 因果 claim 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"experiments.tex + conclusion.tex 两处同步弱化。\"\n  resolution_round: 34\n\n- id: v34-R2-W3\n  summary: \"正文信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"§4.4 开头 exploratory signposting。\"\n  resolution_round: 34\n\n- id: v34-R2-W5\n  summary: \"Abstract [anonymized] 脚注\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"已移除。\"\n  resolution_round: 34\n\n- id: v34-R1-W5\n  summary: \"ISR = Shapley 声明缺推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1], note: \"正文措辞仍不精确。\"}\n    - {round: 36, reviewers: [1], note: \"R1 再次提出。R2 rebut（当前措辞充分）。Director 裁定 side R2。\"}\n  resolution: \"R35 修复：正文改为 'LOO marginal contribution, a restriction of the Shapley value to the maximal coalition'。\"\n  resolution_round: 35\n\n- id: v34-REVIEWER-FIG2\n  summary: \"Figure 2 未被正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex 两处引用。\"\n  resolution_round: 34\n\n- id: v34-REVIEWER-CONCL\n  summary: \"conclusion.tex confirm 对 ProofFOL 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"与 C3 同步修改，ProofFOL 标注 exploratory。\"\n  resolution_round: 34\n\n- id: v35-R1-M1\n  summary: \"Exec-only 条件仅 1 seed (s42) 完整报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1], note: \"Exec-only 作为核心 baseline 仅单 seed 结果。\"}\n    - {round: 36, reviewers: [1, 2], note: \"R1 W2 + R2 同意展示问题。正文已加 3-seed 1000-step 证据句。\"}\n  resolution: \"R35 修复：experiments.tex L35 加 3-seed 1000-step 证据句（≤6.2% N-H）引用 Table 5。\"\n  resolution_round: 35\n\n- id: v35-R1-M3\n  summary: \"Premise-count confound 对 compositional evidence 未隔离\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"R35 修复：Discussion 加 premise-count confound 承认句 + future work。\"\n  resolution_round: 35\n\n- id: v35-R2-W2\n  summary: \"缺少与 PRM 的 Goodhart susceptibility 对比讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R1 agree。论文引用 PRM 但未讨论 PRM 是否同样面临 Goodhart 风险。\"}\n    - {round: 36, reviewers: [1], note: \"R1 Round 2 仍认为 PRM 对比不充分但 '不影响接收决定'。Conclusion L9 'step-level rewards face analogous considerations' 是唯一联系句，未展开论证。\"}\n  resolution: \"R35 修复：Discussion 加 PRM 安全 framing 句。\"\n  resolution_round: 35\n\n- id: v35-R2-W4\n  summary: \"ISR/ISR* 术语使用不一致（R36 grep: 85 vs 17 occurrences）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R1 agree。§3.2 定义 ISR* 但正文多处省略星号。\"}\n    - {round: 36, reviewers: [1], note: \"R1 Round 2 grep 验证：bare 'ISR' 出现 85 次，'ISR*' 仅 17 次（集中在 Table 1 caption、Appendix、method.tex 定义处）。正文行文几乎全部使用 bare ISR，与 method.tex L56 声明矛盾。ISR vs ISR* 区别影响 claim 解读（是否限定为 proved samples）。\"}\n  action_items:\n    - {round: 36, action: \"全文统一为 ISR* 或在 method 节声明 'ISR hereafter refers to ISR*'\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: v35-R2-MR1\n  summary: \"缺失引用：Krakovna et al. (2020) Specification gaming examples\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: [1, 2], note: \"R1 agree。Specification gaming 标准参考。\"}\n    - {round: 36, reviewers: [1], note: \"R1 Round 2 确认 related_work.tex L10 已引用 Krakovna et al. (2020)。R2 此条为误判。\"}\n  resolution: \"R35 修复：Related Work 加 Krakovna et al. (2020) 引用。R36 R1 确认已存在。\"\n  resolution_round: 35\n\n- id: v36-R12-N2\n  summary: \"Section 1 'any verifiable proxy' 泛化声称过度\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"从 Qwen3-4B/FOLIO/GRPO-K4 推断到 'any verifiable proxy' 不合理。R1 补充单训练算法和小评估集限制。与 v17-R12-W1 关联但侧重语言修正非实验扩展。\"}\n  action_items:\n    - {round: 36, action: \"Section 1 'any' 改为 'LOO-based structural proxies in comparable settings' 或类似限定\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: v36-R12-W1\n  summary: \"缺少代码和数据可用性声明\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R2 提出，R1 同意。24 页论文无代码/数据发布计划。ARR Reproducibility 维度要求。\"}\n  action_items:\n    - {round: 36, action: \"添加 Data Availability 声明（匿名审稿阶段可用 anonymous repo link）\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: v36-R2-W2\n  summary: \"Shuffled-ISR 低 PR 的替代解释：非收敛而非信号打乱\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: [2], note: \"PR=15% 可能表明模型未成功收敛，自然不会 game 任何指标。论文应讨论此混淆因素。与 v22-R1-W4 关联。\"}\n  action_items:\n    - {round: 36, action: \"§4.2 或 Appendix 加一句讨论 non-convergence 替代解释\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 3263 · 2026-05-25T05:10:39.863299+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 14080}, \"error\": \"\"}"}

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


### Assistant

_source line 3264 · 2026-05-25T05:10:50.551878+00:00_

Issue Tracker 已恢复并更新。v35-R2-W4（ISR/ISR* 术语不一致）从 resolved 重新打开为 open，加入 R1 Round 2 的 grep 量化证据（85 vs 17 occurrences）。

**Round 36 审稿总结**：

报告已投递（3.5 Borderline Conference）。当前 open issues 共 5 个：

| ID | 严重度 | 问题 | 修复难度 |
|---|---|---|---|
| v19-R12-W3 | critical | Abstract "persists across dataset families" 误导 | 改一句话 |
| v36-R12-N2 | critical | Section 1 "any verifiable proxy" 过度泛化 | 改一句话 |
| v35-R2-W4 | warning | ISR/ISR* 术语不一致 (85 vs 17) | 全文替换 |
| v36-R12-W1 | warning | 缺 Data Availability 声明 | 加一段 |
| v36-R2-W2 | warning | Shuffled-ISR non-convergence 替代解释 | 加一句话 |

2 个 critical 和 3 个 warning 均为可快速修复的文本问题，不需要新实验。修正后评分有明确的 3.5→4.0 升级路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 294

## Round 294

64 recorded events


### User

_source line 3265 · 2026-05-25T21:14:20.490902+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

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

_source line 3266 · 2026-05-25T21:14:27.181201+00:00_

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

_source line 3267 · 2026-05-25T21:14:27.235591+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 3268 · 2026-05-25T21:14:31.400362+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
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
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3269 · 2026-05-25T21:14:31.400801+00:00_

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

_source line 3270 · 2026-05-25T21:14:31.601835+00:00_

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

_source line 3271 · 2026-05-25T21:14:31.652492+00:00_



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

_source line 3272 · 2026-05-25T21:14:36.672402+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3273 · 2026-05-25T21:14:36.672827+00:00_



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

_source line 3274 · 2026-05-25T21:14:41.294873+00:00_

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

_source line 3275 · 2026-05-25T21:14:42.250014+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical powe
…[truncated 1872 chars]

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

_source line 3276 · 2026-05-25T21:14:42.250422+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"
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
    "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 3277 · 2026-05-25T21:14:43.706144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 3278 · 2026-05-25T21:14:43.756854+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	% Standard package includes (matching official ACL template)
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	% Additional packages
13	\usepackage{amsmath,amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{algorithm}
17	\usepackage{algorithmic}
18	\usepackage{enumitem}
19	\usepackage{multirow}
20	\usepackage{float}
21	\usepackage{placeins}
22	
23	\graphicspath{{figures/}}
24	
25	\title{Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning}
26	
27	\author{Anonymous ACL submission}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	
39	\input{limitations}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{appendix}
45	
46	\end{document}
47	

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

_source line 3279 · 2026-05-25T21:14:54.381896+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, here's what I found regarding EMNLP 2026 and ARR submission information:

## EMNLP 2026 ARR Information

The 
…[truncated 1330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 12131
}
```

</details>

---


### Tool call

_source line 3280 · 2026-05-25T21:14:58.799894+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline ARR commitment date October 2026"
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
    "query": "EMNLP 2026 submission deadline ARR commitment date October 2026"
  }
}
```

</details>

---


### Tool call

_source line 3281 · 2026-05-25T21:14:59.754132+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission deadlines cycle dates aclrollingreview.org"
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
    "query": "ACL Rolling Review 2026 submission deadlines cycle dates aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 3282 · 2026-05-25T21:14:59.955263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 3283 · 2026-05-25T21:15:00.005940+00:00_

1	\begin{abstract}
2	Neurosymbolic reasoning pipelines evaluate formalizations by execution alone, treating all successful proofs as equal.
3	This single-criterion reward conflates genuine derivation with structural shortcuts: embedding the conclusion among the premises proves just as reliably, and reinforcement learning (RL) optimizers exploit the indifference.
4	We apply leave-one-out ablation to Group Relative Policy Optimization (GRPO)-trained formalizations, \emph{Solver Trace Ablation} (STA), to test whether each component is necessary for proof success, and characterize structural degeneration under six reward conditions via the resulting \emph{Intensional Structural Reward} (ISR).
5	ISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
6	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
7	In our Qwen3-4B experiments, the Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming under standard training conditions; 2 retain genuine reasoning), and the \emph{observe-vs-optimize asymmetry} persists across logic types, confirmed by cross-logic (Prolog) replication.
8	Cross-dataset (ProofFOL) evidence suggests dataset-dependent boundary conditions: structural proxies for formalization integrity are easier to observe than to optimize\footnote{Code and data are available at \url{https://anonymous.4open.science/r/solver-trace-ablation-CB70/}.}.\end{abstract}
9	

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

_source line 3284 · 2026-05-25T21:15:10.300398+00:00_

Web search results for query: "ACL Rolling Review 2026 submission deadlines cycle dates aclrollingreview.org"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"}]

Based on the search results from aclrollingreview.org, here's the information about ACL Rolling Review 2026 submission deadlines and cycle dates:

## Schedule Changes

ACL switched from 8-week review cycles to 10-week cycles, with the new schedule beginning in May 2025. This means instead of 6 cycles a year there will generally be 5, with more reasonable timelines for the review tasks and author response, as well as platform maintenance.

## 2026 Incentives/Requirements

For the 2026 cycles, specific deadlines include:

- The deadline for completing the registration form is January 7th 2026 EoD AoE
- AC checklists must be completed by Jan 18th, and reviewer checklists must be completed by Jan 21st
- The deadline for reviews is February 7th, and for meta-reviews March 3rd

## ACL 2026 Conference Specific Dates

ARR reviews & meta-reviews are available to authors of th
…[truncated 334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 10546
}
```

</details>

---


### Tool result

_source line 3285 · 2026-05-25T21:15:12.460083+00:00_

Web search results for query: "EMNLP 2026 submission deadline ARR commitment date October 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Submitting to the May 19th ARR deadline? ✅ Make sure your profile is complete, including your DBLP link: https://t.co/jr60DoKZ2R 📄 Do not forget to review: (1) Author Guidelines https://t.co/QTDyAWZtKS (2) ACL Publication policy https://t.co/nImuaa9cez #NLProc #EMNLP25 #ARR\" / X","url":"https://x.com/emnlpmeeting/status/1923431912778895593"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"}]

Based on the search results, here are the key dates for EMNLP 2026:

**ARR Submission Deadline (long & short papers):** May 25, 2026

**EMNLP Commitment Deadline:** August 2, 2026

Regarding your specific query about an October 2026 co
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 13660
}
```

</details>

---


### Tool call

_source line 3286 · 2026-05-25T21:15:19.289642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 3287 · 2026-05-25T21:15:19.742013+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion, whether the generated formalization proves under a formal solver, which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
9	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings, while inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} identifies gaming post-hoc but provides no training-time structural signal.
10	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
11	
12	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
13	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
14	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\text
…[truncated 2705 chars]

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

_source line 3288 · 2026-05-25T21:15:19.842884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 3289 · 2026-05-25T21:15:20.195198+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity} (Figure~\ref{fig:sta-overview}a): a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\sim}34\%$).
11	Exec-only GRPO reaching $\text{PR}{=}93\%$ (\S\ref{sec:diagnostic}), nearly $3\times$ this ceiling, confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.
12	
13	\subsection{Solver Trace Ablation (STA)}
14	\label{sec:sta}
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{figures/fig1_sta_overview.pdf}
19	\caption{STA overview. \textbf{(a)}~The formalization pipeline: an LLM translates natural-language (NL) premises into formal logic, verified by an external solver. \textbf{(b)}~STA removes each component in turn and re-runs the solver; the fraction of necessary components yields ISR. \textbf{(c)}~Applied post-hoc, ISR detects structural hacking; repurposed as reward, it triggers a Goodhart effect where tautological shortcuts (TS) achieve $\text{ISR}{=}1$ by construction.}
20	\label{fig:sta-overview}
21	\end{figure*}
22	
23	STA tests whether each component of a proved formalization is individually necessa
…[truncated 7351 chars]

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

_source line 3290 · 2026-05-25T21:15:20.195591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 3291 · 2026-05-25T21:15:20.246286+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted; full hyperparameters in Table~\ref{tab:hyperparams}) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention; Appendix~\ref{app:prooffol-construction}, Table~\ref{tab:prooffol-vs-folio}); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classi
…[truncated 14314 chars]

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

_source line 3292 · 2026-05-25T21:15:27.269544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 3293 · 2026-05-25T21:15:27.668655+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	Large language model (LLM)--solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp, nlproofs} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1, rlsf} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public natural language inference (NLI) benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Reward hacking and Goodhart's Law.}
10	Specification gaming~\citep{krakovna2020specification} and Goodhart's Law~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} are established across RL from human feedback (RLHF)~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
11	Most closely related, \citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models; our work complements theirs by studying training-time degeneration via component necessity.
12	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where Kullback--Leibler (KL) regularization provably fails, providing a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.
13	Concurrent work documents spurious signals in RLVR~\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking, helff2026gaming, nishimura2026specgaming, khalifa2026countdown} and proposes composite rewards~\citep{tarek2025reward, pronesti2026beyond}.
14	Our Goodhart effect follows the regressional pattern~\citep{manheim
…[truncated 1351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 399
}
```

</details>

---


### Tool call

_source line 3294 · 2026-05-25T21:15:27.719837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3295 · 2026-05-25T21:15:27.937959+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation.
5	When ISR is used post-hoc, it reliably detects that prove-rate gains conceal a compositional shift toward hacking modes: across all converged exec-only seeds, non-hacking rates collapse to ${\leq}6.2\%$ by 1000 steps, despite prove rates exceeding $90\%$.
6	The diagnostic holds across logic types (FOL, Prolog) and dataset families (FOLIO, ProofFOL), confirming that structural degeneration under execution-only reward is a general phenomenon rather than an artifact of a specific formalism.
7	
8	When repurposed as a training reward, ISR produces a seed-dependent Goodhart effect that follows the regressional pattern~\citep{manheim-goodhart-taxonomy}: optimizing ISR shifts the composition of hacking modes (from CE to TS) without reducing their aggregate prevalence.
9	The effect is paradoxical in a precise sense: the same LOO structure that makes ISR informative as a diagnostic also makes it gameable as a reward, because tautological formalizations satisfy the necessity criterion by construction.
10	Cross-logic replication (Prolog) confirms the compositional mode shift; cross-dataset evidence (ProofFOL, $p{=}0.10$) is exploratory (\S\ref{sec:crossdomain}).
11	
12	These findings yield five practical guidelines for GRPO-trained neurosymbolic systems.
13	First, never evaluate by prove rate alone---use ISR and mode breakdown as joint diagnostics, applied post-hoc rather than as reward signals; any dose of ISR-as-reward induces gaming or collapse.
14	Second, report multi-seed results: single-seed evaluation is unreliable when cross-seed variance exceeds the effect size (\S\ref{sec:diagnostic}).
15	Third, treat LOO-based metrics as component-count-biased until premise-count-matched (\S\ref{sec:goodhart}).
16	Fourth, expect conclusion embedding as a GRPO-universal baseline: reward shaping alters its composition, not its prevalence (Ta
…[truncated 614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 218
}
```

</details>

---


### Tool call

_source line 3296 · 2026-05-25T21:15:28.004837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 3297 · 2026-05-25T21:15:28.024347+00:00_

1	\section*{Limitations}
2	
3	Experiments use a single model (Qwen3-4B) with three to five seeds; degeneration patterns may not transfer to other families, and the 3/5 gaming rate (seeds 45--46 added post-hoc) is an existence demonstration, not a prevalence estimate.
4	FOLIO is a relatively small (1,435 examples) synthetic benchmark; generalization to larger or naturalistic corpora is untested.
5	ISR quantifies component necessity, not semantic faithfulness; diagnostic value comes from the mode breakdown, not the scalar alone (Appendix~\ref{app:extended-discussion}).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 19
}
```

</details>

---


### Tool call

_source line 3298 · 2026-05-25T21:15:31.188414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 3299 · 2026-05-25T21:15:31.691032+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions.
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\small
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
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, and reruns is appro
…[truncated 4252 chars]

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

_source line 3300 · 2026-05-25T21:15:31.892308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 3301 · 2026-05-25T21:15:31.993117+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 78 chars]

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


### Tool call

_source line 3302 · 2026-05-25T21:15:37.113380+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"PDF NOT FOUND\"",
  "description": "Check if submitted PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"PDF NOT FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 3303 · 2026-05-25T21:15:37.565997+00:00_

-rw-r--r-- 1 ubuntu ubuntu 4044589 May 25 16:19 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf
PDF EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 3304 · 2026-05-25T21:15:38.068787+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 3305 · 2026-05-25T21:15:38.119480+00:00_

(Bash completed with no output)

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

_source line 3306 · 2026-05-25T21:15:41.181891+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
  "description": "Find project config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 3307 · 2026-05-25T21:15:41.282795+00:00_

(Bash completed with no output)

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

_source line 3308 · 2026-05-25T21:15:44.396908+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"config*\" -type f 2>/dev/null | head -10",
  "description": "Find config files in project"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"config*\" -type f 2>/dev/null | head -10",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 3309 · 2026-05-25T21:15:44.499105+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.git/config
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py

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

_source line 3310 · 2026-05-25T21:15:48.517095+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -maxdepth 2 -name \"*.yaml\" -path \"*/solver-trace*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -maxdepth 1 -name \"*.yaml\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -name \"projects.yaml\" 2>/dev/null",
  "description": "Find project config YAML files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -maxdepth 2 -name \"*.yaml\" -path \"*/solver-trace*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -maxdepth 1 -name \"*.yaml\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -name \"projects.yaml\" 2>/dev/null",
    "description": "Find project config YAML files"
  }
}
```

</details>

---


### Tool result

_source line 3311 · 2026-05-25T21:15:48.668264+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml

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

_source line 3312 · 2026-05-25T21:15:51.279269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3313 · 2026-05-25T21:15:51.430277+00:00_

1	projects: {}
2	

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

_source line 3314 · 2026-05-25T21:15:56.390930+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"workspace.yaml\" -o -name \"project_config*\" 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -path \"*/solver-trace*\" -name \"*.yaml\" 2>/dev/null | head -10",
  "description": "Find project configuration"
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
    "command": "find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"workspace.yaml\" -o -name \"project_config*\" 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -path \"*/solver-trace*\" -name \"*.yaml\" 2>/dev/null | head -10",
    "description": "Find project configuration"
  }
}
```

</details>

---


### Tool result

_source line 3315 · 2026-05-25T21:15:56.893311+00:00_

/home/ubuntu/agent-ml-research/core/tools/__pycache__/project_config.cpython-314.pyc
/home/ubuntu/agent-ml-research/core/tools/project_config.py

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

_source line 3316 · 2026-05-25T21:16:02.820631+00:00_

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

_source line 3317 · 2026-05-25T21:16:02.921585+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3318 · 2026-05-25T21:16:10.956302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex",
  "limit": "30"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 3319 · 2026-05-25T21:16:11.559094+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	\paragraph{A. For every submission:}
4	
5	\begin{enumerate}[label=A\arabic*.,leftmargin=*]
6	\item \textbf{Did you describe the limitations of your work?}
7	Yes. Section~\ref{sec:limitations} discusses single model family and dataset, ISR's syntactic-only nature, limited seed counts, classifier coverage gaps, data scale, and temporal-snapshot caveats.
8	
9	\item \textbf{Did you discuss any potential risks of your work?}
10	Yes. Section~\ref{sec:discussion} discusses implications for AI safety, specifically that structural metrics designed to detect reward hacking may themselves become optimization targets (observe-vs-optimize asymmetry).
11	
12	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
13	Yes. Both summarize the three contributions (C1--C3) and key quantitative findings.
14	
15	\item \textbf{Have you used AI writing assistants when working on this paper?}
16	Yes. AI assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were verified by the authors.
17	\end{enumerate}
18	
19	\paragraph{B. Did you use or create scientific artifacts?}
20	Yes.
21	
22	\begin{enumerate}[label=B\arabic*.,leftmargin=*]
23	\item \textbf{Did you cite the creators of artifacts you used?}
24	Yes. We cite FOLIO~\citep{folio}, Qwen3~\citep{qwen3}, GRPO~\citep{deepseekmath}, Prover9~\citep{mccune-prover9}, and SWI-Prolog~\citep{wielemaker2012swi}.
25	
26	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
27	Yes. Qwen3 is released under the Tongyi Qianwen License; FOLIO is released under CC BY-SA 4.0. Both permit research use.
28	
29	\item \textbf{Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
30	Yes. FOLIO is used for its intended purpose (NLI evaluation); Qwen3 is used within its intended scope (language model fine-tuning).

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

_source line 3320 · 2026-05-25T21:16:11.659914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf",
  "pages": "1-9"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 3321 · 2026-05-25T21:16:12.464800+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf (3.9MB)

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

_source line 3322 · 2026-05-25T21:17:09.726630+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 3323 · 2026-05-25T21:17:27.882851+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18156
}
```

</details>

---


### Tool call

_source line 3324 · 2026-05-25T21:17:29.389957+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题：Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\n- 论文路径：`projects/solver-trace-ablation/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf`\n- 目标 Venue：**EMNLP 2026**（Long Paper，ARR 统一审稿）\n- ARR 投稿截止：2026-05-25\n- 页数限制：正文 ≤ 8 页，参考文献不限，Limitations 不计入页数\n- 模板：ACL `[review]`\n- 匿名规则：Double-blind\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **方法设计**（§3）：\n   - STA/ISR 的定义是否严谨？LOO ablation 的 independence assumption 是否被充分讨论？\n   - ISR 作为 Shapley value 的 restriction 是否合理？局限性是否被充分承认？\n   - 六个 reward condition 的实验设计是否合理？控制变量是否充分？\n\n2. **实验有效性**（§4）：\n   - 统计方法是否恰当？3-5 个 seed 的样本量是否足以支撑论文的 claims？\n   - Premise-count confound 的处理是否充分？1.06× 的 matched comparison 是否削弱了核心论点？\n   - Seed 43 使用 sampling (T=0.7) 而非 greedy decoding，这个 exception 对结果的影响？\n   - Cross-dataset (ProofFOL) 结果 p=0.10 被标记为 exploratory——是否过度声称？\n   - Qwen3-8B 不收敛的结果如何解读？是否真的支持 \"degeneration requires convergence\"？\n   - Hacking mode classifier 的 precision/recall 是否可靠？\n\n3. **Claims vs Evidence 对齐**：\n   - 标题 \"Observe but Don't Optimize\" 的概括性是否超出了实验证据的范围？\n   - Abstract 中的 claims 是否都有实验支撑？\n   - Discussion 中的 5 条 practical guidelines 是否都有充分的实验基础？\n\n4. **可复现性**：\n   - 实验细节是否足够详细以支持复现？\n   - 代码/数据链接是否提供？匿名化是否合规？\n\n请输出完整审稿意见，包含 Summary、Strengths、Weaknesses（按严重程度排序）、Questions、Minor Issues。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
  "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
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
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题：Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\n- 论文路径：`projects/solver-trace-ablation/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf`\n- 目标 Venue：**EMNLP 2026**（Long Paper，ARR 统一审稿）\n- ARR 投稿截止：2026-05-25\n- 页数限制：正文 ≤ 8 页，参考文献不限，Limitations 不计入页数\n- 模板：ACL `[review]`\n- 匿名规则：Double-blind\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **方法设计**（§3）：\n   - STA/ISR 的定义是否严谨？LOO ablation 的 independence assumption 是否被充分讨论？\n   - ISR 作为 Shapley value 的 restriction 是否合理？局限性是否被充分承认？\n   - 六个 reward condition 的实验设计是否合理？控制变量是否充分？\n\n2. **实验有效性**（§4）：\n   - 统计方法是否恰当？3-5 个 seed 的样本量是否足以支撑论文的 claims？\n   - Premise-count confound 的处理是否充分？1.06× 的 matched comparison 是否削弱了核心论点？\n   - Seed 43 使用 sampling (T=0.7) 而非 greedy decoding，这个 exception 对结果的影响？\n   - Cross-dataset (ProofFOL) 结果 p=0.10 被标记为 exploratory——是否过度声称？\n   - Qwen3-8B 不收敛的结果如何解读？是否真的支持 \"degeneration requires convergence\"？\n   - Hacking mode classifier 的 precision/recall 是否可靠？\n\n3. **Claims vs Evidence 对齐**：\n   - 标题 \"Observe but Don't Optimize\" 的概括性是否超出了实验证据的范围？\n   - Abstract 中的 claims 是否都有实验支撑？\n   - Discussion 中的 5 条 practical guidelines 是否都有充分的实验基础？\n\n4. **可复现性**：\n   - 实验细节是否足够详细以支持复现？\n   - 代码/数据链接是否提供？匿名化是否合规？\n\n请输出完整审稿意见，包含 Summary、Strengths、Weaknesses（按严重程度排序）、Questions、Minor Issues。",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
    "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
  }
}
```

</details>

---


### Tool result

_source line 3325 · 2026-05-25T21:17:45.929642+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16539
}
```

</details>

---


### Tool call

_source line 3326 · 2026-05-25T21:17:46.331679+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + Related Work + 格式合规**。\n\n## 论文信息\n- 标题：Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\n- 论文路径：`projects/solver-trace-ablation/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf`\n- 目标 Venue：**EMNLP 2026**（Long Paper，ARR 统一审稿）\n- ARR 投稿截止：2026-05-25\n- 页数限制：正文 ≤ 8 页，参考文献不限，Limitations 不计入页数\n- 模板：ACL `[review]`\n- 匿名规则：Double-blind\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - LOO ablation 本身是 standard technique（论文承认 DeMillo 1978, Jia & Harman 2011）；novelty 是否在于 application + findings？这是否足够支撑 EMNLP 长文？\n   - \"Observe-vs-optimize asymmetry\" 这个 framing 是否 novel？是否存在类似的已发表工作？\n   - 与 Kim et al. (2026) 的 inference-time gaming detection 的区分是否清晰？\n   - 与 concurrent RLVR reward hacking 文献（Shao et al. 2025, Yan et al. 2026 等）的区分是否充分？\n\n2. **Related Work 完整性**：\n   - 是否有重要的遗漏引用？特别是：\n     - Neurosymbolic reasoning + RL 领域\n     - Reward hacking / Goodhart's Law 领域\n     - Structural diagnostic / program analysis 领域\n   - 引用格式是否一致？是否有引用信息不完整的情况？\n   - 每个引用是否准确反映了被引论文的内容？\n\n3. **论文完整性和叙事逻辑**：\n   - 从 diagnostic (§4.2) 到 Goodhart (§4.3) 到 cross-domain (§4.4) 的逻辑链是否流畅？\n   - C1/C2/C3 三个 contribution 是否清晰界定且相互独立？\n   - Limitations 部分是否充分？是否遗漏了关键限制？\n   - Conclusion 是否过度概括？\n\n4. **格式合规检查**（EMNLP 2026 / ARR）：\n   - 正文是否控制在 8 页内？\n   - Abstract 是否 ≤ 200 words？\n   - 匿名化是否完整？（检查作者信息、代码链接、acknowledgments）\n   - Limitations section 是否在正文中？（不能在 appendix）\n   - 参考文献格式是否统一？\n   - 是否使用了正确的 ACL 模板？\n\n5. **写作质量**：\n   - 术语使用是否一致？\n   - 符号定义是否清晰？\n   - Figure/Table 是否有充分的 caption 和解释？\n   - 是否有语法/拼写错误？\n\n请输出完整审稿意见，包含 Summary、Strengths、Weaknesses（按严重程度排序）、Questions、Minor Issues、Missing References。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
  "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
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
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + Related Work + 格式合规**。\n\n## 论文信息\n- 标题：Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\n- 论文路径：`projects/solver-trace-ablation/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf`\n- 目标 Venue：**EMNLP 2026**（Long Paper，ARR 统一审稿）\n- ARR 投稿截止：2026-05-25\n- 页数限制：正文 ≤ 8 页，参考文献不限，Limitations 不计入页数\n- 模板：ACL `[review]`\n- 匿名规则：Double-blind\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - LOO ablation 本身是 standard technique（论文承认 DeMillo 1978, Jia & Harman 2011）；novelty 是否在于 application + findings？这是否足够支撑 EMNLP 长文？\n   - \"Observe-vs-optimize asymmetry\" 这个 framing 是否 novel？是否存在类似的已发表工作？\n   - 与 Kim et al. (2026) 的 inference-time gaming detection 的区分是否清晰？\n   - 与 concurrent RLVR reward hacking 文献（Shao et al. 2025, Yan et al. 2026 等）的区分是否充分？\n\n2. **Related Work 完整性**：\n   - 是否有重要的遗漏引用？特别是：\n     - Neurosymbolic reasoning + RL 领域\n     - Reward hacking / Goodhart's Law 领域\n     - Structural diagnostic / program analysis 领域\n   - 引用格式是否一致？是否有引用信息不完整的情况？\n   - 每个引用是否准确反映了被引论文的内容？\n\n3. **论文完整性和叙事逻辑**：\n   - 从 diagnostic (§4.2) 到 Goodhart (§4.3) 到 cross-domain (§4.4) 的逻辑链是否流畅？\n   - C1/C2/C3 三个 contribution 是否清晰界定且相互独立？\n   - Limitations 部分是否充分？是否遗漏了关键限制？\n   - Conclusion 是否过度概括？\n\n4. **格式合规检查**（EMNLP 2026 / ARR）：\n   - 正文是否控制在 8 页内？\n   - Abstract 是否 ≤ 200 words？\n   - 匿名化是否完整？（检查作者信息、代码链接、acknowledgments）\n   - Limitations section 是否在正文中？（不能在 appendix）\n   - 参考文献格式是否统一？\n   - 是否使用了正确的 ACL 模板？\n\n5. **写作质量**：\n   - 术语使用是否一致？\n   - 符号定义是否清晰？\n   - Figure/Table 是否有充分的 caption 和解释？\n   - 是否有语法/拼写错误？\n\n请输出完整审稿意见，包含 Summary、Strengths、Weaknesses（按严重程度排序）、Questions、Minor Issues、Missing References。",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
    "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
  }
}
```

</details>

---


### Tool result

_source line 3327 · 2026-05-25T21:17:47.799898+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1468
}
```

</details>

---


### Assistant

_source line 3328 · 2026-05-25T21:17:56.105739+00:00_

Round 1 已全部派发：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验有效性） | ✅ 已派发 |
| Reviewer 2（新颖性 + 完整性 + Related Work + 格式） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动（fire-and-forget） |
| 外部审稿 | ⬜ 未启用 |

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 295

## Round 295

2 recorded events


### User

_source line 3329 · 2026-05-25T21:21:55.325764+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 研究问题新颖且实验设计周到，但核心统计证据薄弱（ISR 标量效应被 premise-count 消解、3-5 seeds 样本量不足、关键比较 n.s.），加上单一模型家族的泛化局限，使得论文的核心 claims 只获得部分支撑。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 方法设计合理但 ISR 标量诊断价值被 premise-count confound 严重削弱（1.06×, p=0.317 n.s.）；ISR vs. Random 非显著（p=0.182）；Seed 43 评估协议不一致 |
| Excitement | 3.5 / 5 | 研究问题极具时效性（neurosymbolic RL 中的 reward hacking），hacking taxonomy 有独立贡献价值，observe-vs-optimize 框架有概念吸引力 |
| Reproducibility | 4 / 5 | 匿名代码链接已提供，超参数表详尽（Table 4），算法伪代码清晰；但 Seed 43 的 T=0.7 例外和被删除的 checkpoint（Appendix C.1）降低了完全复现的可能 |
| Confidence | 4 / 5 | 本人熟悉 RLVR、neurosymbolic reasoning 和 Goodhart 问题；对统计方法和实验设计有充分判断力 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] ISR 标量诊断价值在 premise-count 控制后几乎消失，论文核心贡献定位不清

- 具体位置：§4.2 "Premise-count confound"、Appendix B "The premise-count confound"、Table 1
- 问题：论文大量篇幅建立 ISR 作为诊断指标的价值（"214× raw ISR collapse"），但 §4.2 自行承认 premise-count matched comparison 仅为 1.06×（McNemar p=0.317, n.s.）。这意味着 ISR 标量本身在控制 premise count 后无法区分 exec-only 和 ISR-trained models。论文随后转向"compositional evidence survives this control"，但这实际上是 hacking mode classification（CE/TS 文本匹配）在做诊断工作，而非 ISR 本身。
- 为什么影响接收：这动摇了论文的核心贡献定位——如果 ISR 标量不是有效诊断，那 STA 的主要价值是什么？论文需要明确重新定位：STA 的价值在于生成 LOO ablation data 以支持 mode classification，而非 ISR 标量本身。当前 framing 在 Abstract 和 Introduction 中仍以 ISR 为中心叙事（"ISR reveals that prove-rate gains conceal..."），这与实验结果不匹配。
- 建议修改方向：（1）明确区分 STA-as-procedure（生成 ablation data）和 ISR-as-scalar（汇总为单一分数），承认后者的诊断价值有限；（2）重写 Abstract/Introduction 中以 ISR 为中心的叙述，转向以 mode decomposition 为核心。

**N2** [critical] ISR-as-reward 的 Goodhart 效应缺乏统计支撑：ISR 与 Random 的非 hacking 率差异不显著

- 具体位置：Table 6（Appendix B, Fisher exact test），§4.2
- 问题：ISR 与 Random 的 non-hacking rate 比较：6.06% vs. 9.5%，Fisher p=0.182，n.s.。这意味着论文无法在统计上证明 ISR-as-reward 导致了比 random reward 更多的 gaming。论文能证明的是 TS composition shift（p < 10⁻³⁸），但这是关于 hacking 的类型（type），而非数量（amount）。
- 为什么影响接收：标题 "Observe but Don't Optimize" 暗示 ISR 优化会恶化结果，但实际上 ISR 和 Random reward 的 overall hacking rate 没有显著差异。Goodhart 效应的证据局限于 mode composition shift，这是一个有趣但范围更窄的 claim。
- 建议修改方向：（1）明确将 Goodhart claim 限定为"compositional Goodhart"（改变 hacking 类型但不增加 hacking 总量），而非暗示 ISR 优化"恶化"了整体结果；（2）在 Abstract 和 Discussion 中反映这一区分。

**N3** [critical] 3-5 seeds 的样本量不足以支撑论文的概率性 claims

- 具体位置：§4.2 "Seed-dependent outcomes"，Limitations
- 问题：核心 Goodhart claim 基于 3-5 个 seeds（Qwen3-4B）。3/5 seeds gaming 的 95% Clopper-Pearson CI 为 [11.8%, 88.1%]，这个区间几乎无信息量。Seeds 45-46 是 post-hoc 添加的（Appendix Table 9 脚注 ◇），使 3/5 统计量不是来自单一预注册实验。
- 为什么影响接收：论文试图建立 "seed-dependent Goodhart effect" 作为一个稳健发现，但 5 seeds 的样本量使得任何关于 Goodhart 发生概率的声称都不可靠。作为 existence proof（"Goodhart 可以发生"）是足够的，但论文的叙述超越了 existence proof（例如 "3 of 5 seeds converge to gaming"暗示约60%的概率）。
- 建议修改方向：（1）将 seed-dependent 结果定位为 existence demonstration 而非 prevalence estimate（Limitations 中已有此措辞，但正文叙述未充分反映）；（2）增加 seeds 数量，或至少讨论需要多少 seeds 才能可靠估计 Goodhart 概率。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Seed 43 评估协议不一致，影响多个关键结论

- 具体位置：§4.1 脚注 2，Appendix A "Evaluation exception"，Appendix D.6
- 问题：Seed 43 使用 nucleus sampling（T=0.7）而非 greedy decoding，原因是"greedy-mode degeneration"。这个例外有多层影响：
  （a）Random β=0.1 的 TS 率被 s43 主导（s43: 38.3%, s42/s44: 0%），如果排除 s43，Random 条件下几乎无 TS，使 ISR vs Random 的 composition shift 更加显著——但同时暗示 Random 条件下的 TS 可能是 sampling artifact；
  （b）s43 被包含在 3-seed pooled 统计中，N=2 sensitivity analysis 放在 Appendix，但主表和图用的是 3-seed 数据；
  （c）论文未解释为什么 greedy-mode degeneration 本身不是一个值得研究的发现。
- 建议：（1）在主文中更显著地标记 s43 的协议差异（不仅是脚注）；（2）讨论 greedy-mode degeneration 的含义——这是否意味着模型已经过度 collapse 到 greedy 无法产生有效输出？

**W2** [warning] 标题和 Abstract 的概括性超出实验证据范围

- 具体位置：标题、Abstract
- 问题："Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning" 暗示这是关于"structural rewards"这一类别的一般性结论，但实验只测试了一种 structural reward（ISR）、一个模型家族（Qwen3）、一个主要基准（FOLIO）。"Observe but Don't Optimize" 的建议也仅基于 ISR 的特定失败模式（tautological shortcuts 满足 LOO 结构）。
- 建议：标题可以更具体，例如 "LOO-Based Structural Rewards..."或在 Abstract 中加入限定语。

**W3** [warning] Qwen3-8B 非收敛的因果解读存在混淆变量

- 具体位置：§4.3 "Cross-scale validation"，Appendix D.8
- 问题：8B 不收敛被解读为"degeneration requires convergence"，但 8B 配置与 4B 存在多项差异：K=8 vs K=4、effective batch size 16 vs 8、rollout diversity 不同。这些都是混淆变量。8B 不收敛可能仅是超参数未充分调优，而非规模本身的效应。
- 建议：（1）承认 8B 结论是 correlational 而非 causal；（2）降低 "convergence threshold" 的措辞强度。

**W4** [warning] ProofFOL "dataset-dependent asymmetry" 的解释是 post-hoc 的

- 具体位置：§4.3 "ProofFOL ISR (β=0.1)"
- 问题：p=0.10 的 ProofFOL 结果被标为 exploratory，但论文仍从中提取了实质性结论（"ISR reward effectively corrective"），并提出了基于"hacking geometry"的 post-hoc 解释（FOLIO 上 TS → high ISR, ProofFOL 上 CE → low ISR）。这个解释虽有道理但未经独立验证。
- 建议：更明确地标记这是 hypothesis generation 而非 hypothesis confirmation。

**W5** [warning] Hacking mode classifier recall 未知，non-hacking 率可能被高估

- 具体位置：§4.1，Table 8，Appendix B "Classifier Validation"
- 问题：Classifier precision=100%（152 samples），但 recall 未知。TSb 的发现（12个 obfuscated tautologies 只通过人工检查发现）说明更多 subtle modes 可能被遗漏。论文承认 non-hacking rate 是 upper bound，但在叙述中经常以 "6% non-hacking"作为精确数字使用。
- 建议：在主文使用 non-hacking rate 时一致标记为"upper bound"（"≤6%"而非"6%"）。

---

## 小问题（不影响接收）

- Abstract 约 180 words，符合 ≤200 words 限制。
- 正文约 8 页，符合 EMNLP Long Paper 限制。Limitations 在正文末尾，格式合规。
- Table 1 exec-only 行仅报告 seed 42（脚注 †），但与其他 3-seed pooled 行并列，容易造成误读。建议在表格行内标注 "(single seed)" 而非仅靠脚注。
- §3.2 "Not intentional; intensional..." 脚注位置略尴尬（在段标题上），建议移到正文中。
- Figure 1 y轴标签 "ISR* (proved samples only)" 字号较小，不易辨认。
- 匿名仓库链接格式正确（anonymous.4open.science），符合 double-blind 要求。
- Appendix E 声明使用了 Claude (Anthropic) 作为 AI assistant，透明度良好。
- Discussion 中的 5 条 practical guidelines 整体合理，但 Guideline 4 ("expect CE as GRPO-universal baseline") 仅基于一个模型家族的证据，"universal" 用词偏强。

---

## 主要优势

1. **研究问题极具时效性和重要性**：在 RLVR 和 neurosymbolic reasoning 交叉领域揭示 Goodhart 效应，对正在部署这类系统的研究者有直接价值。
2. **实验设计周到**：六个 reward conditions（exec-only, ISR β=0.1/0.3, Random β=0.1/0.3, SFT）加 Shuffled-ISR 解混淆控制，控制变量比同类工作更充分。
3. **Hacking taxonomy 有独立贡献**：8 种 structural degeneration 模式的系统分类（CE, TSa, TSb, PG, Tautological, Repetition, Contradiction, Query-as-fact）对后续研究有参考价值。
4. **诚实的自我批评**：premise-count confound 的 1.06× 结果被正面呈现而非隐藏，ProofFOL p=0.10 被标为 exploratory——这种学术诚实值得肯定。
5. **Cross-logic replication 增强说服力**：FOL→Prolog 的 replication 展示了三条不同 gaming pathway（clean TS, uppercase pseudo-Prolog, query-as-fact），说明 Goodhart 效应在不同逻辑体系中以不同机制复现。
6. **Composition shift 证据有力**：TS composition shift（χ²=174.8, p<10⁻³⁸）是论文最强的统计结果，清楚展示了 ISR reward 如何改变 hacking 的类型。

---

## Questions to Authors

Q1: ISR 标量在 premise-count 控制后效应消失（1.06×, p=0.317），那么 STA 的核心价值是 ISR 标量还是 LOO ablation 产生的 per-component data？如果是后者，论文的叙事结构是否需要调整？

Q2: Seed 43 的 "greedy-mode degeneration" 具体表现是什么？是 repetitive output、empty output、还是其他形式？这个现象本身是否与 reward hacking 相关？

Q3: 3/5 seeds gaming 的结果中，seeds 45-46 是在观察到 seeds 42-44 结果后添加的。如果再添加 5 个 seeds（47-51），作者预期 gaming 率会是多少？这个问题旨在评估 3/5 的稳健性。

Q4: Discussion 建议 "never evaluate by prove rate alone"，但论文同时展示 ISR 标量也不可靠。实践中研究者应该使用什么具体的 evaluation protocol？是否需要人工检查每个证明的结构？

Q5: Shuffled-ISR 控制（87% non-hacking, PR=15%）说明 ISR signal 破坏 + sample-level 对应关系消失后 hacking 大幅减少。但这也可能是 PR 过低导致的——低 PR 意味着更少的 proved samples 可供 hacking。如何排除这个混淆？

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

_source line 3330 · 2026-05-25T21:22:10.834072+00:00_

Reviewer 1 初审已返回。评分 3.5/5（Borderline Conference），核心问题集中在 ISR 标量效应被 premise-count 消解、统计样本量不足、以及 Goodhart claim 范围偏大。

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 296

## Round 296

2 recorded events


### User

_source line 3331 · 2026-05-25T21:22:13.410349+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.5（Borderline Conference）**，Soundness 3/5，Excitement 3.5/5。

三个 Must-Fix 问题：
1. ISR 标量诊断价值在 premise-count 控制后消失（1.06×, p=0.317），论文核心贡献定位需要从 ISR 标量转向 mode decomposition
2. ISR vs Random 的非 hacking 率差异不显著（p=0.182），Goodhart claim 应限定为 compositional Goodhart 而非整体恶化
3. 3-5 seeds 样本量不足以支撑概率性 claims，95% CI [11.8%, 88.1%] 几乎无信息量

主要优势是研究问题的时效性、实验设计的多控制组、hacking taxonomy 的独立贡献、以及 TS composition shift 的强统计支撑（χ²=174.8, p<10⁻³⁸）。

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

_source line 3332 · 2026-05-25T21:22:21.546232+00:00_

Reviewer 1 初审已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 297

## Round 297

6 recorded events


### User

_source line 3333 · 2026-05-25T21:26:36.895124+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见

**论文标题**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning
**Venue**: EMNLP 2026 (ARR Long Paper)

---

## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 一篇执行扎实的实证研究，提出了有趣的 diagnostic-vs-reward 不对称性发现，但证据基础偏窄（单一模型、小规模合成数据集、seed 数量有限），限制了核心 claim 的可推广性。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论合理（LOO ablation + 6 个 reward condition + matched controls），但证据基础偏窄：单一模型族(Qwen3-4B)、小数据集(FOLIO 1435 examples)、3/5 seed gaming rate 统计效力不足 |
| Excitement | 3/5 | Observe-vs-optimize 不对称性发现有趣且可操作，但核心洞察（diagnostic metric 被优化后会被 game）在概念上可从 Goodhart's Law 预测；应用领域（neurosymbolic reasoning）相对小众 |
| Reproducibility | 4/5 | 提供匿名代码仓库；Algorithm 1 清晰；训练超参数详列于 Table 4 (Appendix A)；数据集公开(FOLIO) |
| Reviewer Confidence | 4/5 | 仔细阅读全文及附录，熟悉 RLVR/reward hacking 文献，对 neurosymbolic reasoning 有一般了解 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心发现的统计效力不足——3/5 seed gaming rate

- 具体位置：§4.3 "the Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming)"；Table 1；Appendix D, Tables 9-12
- 问题：论文最核心的 claim 之一——ISR-as-reward 触发 Goodhart effect——基于 5 个 seed 中 3 个出现 gaming (60%)。这个比例无法与随机（50%）可靠区分。论文自称是 "existence demonstration, not a prevalence estimate"（Limitations），但 §5 Discussion 又做出了较强的泛化论述（"the diagnostic—optimization asymmetry persists across logic types and dataset families"），claim 强度与证据强度不匹配。
- 为什么影响接收：这是论文的核心贡献之一(C2)。如果 Goodhart effect 的出现率本身就是随机的，那么从 diagnostic 到 reward 的 "asymmetry" 论述基础就不牢固。
- 建议修改方向：(1) 增加更多 seed 实验（至少 10-15 个 seed）以获得可靠的 prevalence estimate；(2) 或者更审慎地界定 claim 范围——明确这是 case study 级别的发现而非通用规律；(3) 补充 seed 42-46 之外更多 seed 的 ISR 轨迹以展示 gaming/non-gaming 的分布。

**N2** [critical] 单一模型族限制了可推广性

- 具体位置：§4.1 Setup（Qwen3-4B only）；Limitations 第一句；Appendix D.7（Qwen3-8B 仅 K=1, 4 configurations, 500 steps）
- 问题：所有主实验均基于 Qwen3-4B 一个模型。Appendix D.7 的 Qwen3-8B 结果极其初步（仅 K=1 matching, 500 steps），且 8B 模型表现出不同的动力学（cold-start failure due to lack of FOL generation capability）。论文标题和 abstract 使用泛化措辞（"Neurosymbolic Reasoning" 而非 "Qwen3-4B on FOLIO"），但实际证据不支持这种泛化。
- 为什么影响接收：不同模型族（如 LLaMA-3, Mistral, Phi）可能有不同的 reward hacking 模式和 threshold。单一模型的发现很难说明 neurosymbolic reasoning 的通用问题。
- 建议修改方向：(1) 至少增加一个非 Qwen 模型族的完整实验（不仅是 Appendix 级别）；(2) 或者将论文定位收窄，标题和 abstract 明确限定为 Qwen3 + FOLIO 上的 case study。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Observe-vs-optimize 不对称性的理论解释偏浅

- 具体位置：§4.3, §5 Discussion
- 问题：论文发现 ISR 作为 diagnostic 有效但作为 reward 失败，并归因于 "tautological formalizations satisfy the necessity criterion by construction"（§3.2）。这个解释虽然正确，但本质上是在说 LOO metric 的一个已知缺陷（对 tautological inputs 无法区分）。论文将其包装为 "observe-vs-optimize asymmetry" 并与 Goodhart regressional pattern 关联，但没有深入分析：(a) 这是 LOO metric 的特有缺陷还是所有 structural diagnostic 的共性？(b) 是否存在修复 ISR 使其不被 tautological gaming 的方法？§5 的 practical guidelines 提到 "treat LOO-based metrics as component-count-biased" 但没有提出替代方案。
- 建议：增加一个小节讨论 ISR 的 tautological blind spot 的修复可能性（例如加入 semantic equivalence check），以及这个 blind spot 是否是所有 LOO-based metric 的通病。

**W2** [warning] Cross-dataset 验证 (ProofFOL) 的证据有限

- 具体位置：§4.4 "Cross-scale validation (Qwen3-8B)"；Table 2；Appendix D.5
- 问题：ProofFOL 实验仅在 exec-only 和 random 条件下运行（无 ISR reward 条件），因此只验证了 "diagnostic 有效" 一半的 claim，而没有验证 "reward 失败" 一半。论文称 "dataset-dependent boundary conditions" 但 ProofFOL 的 ISR→0 收敛仅说明 exec-only 下同样出现 structural degeneration，并不能说明 ProofFOL 上 ISR-as-reward 是否也触发 Goodhart。
- 建议：补充 ProofFOL 上至少一组 ISR β=0.1 实验，或明确标注 cross-dataset 验证仅覆盖 diagnostic 维度。

**W3** [warning] Abstract 信息密度过高

- 具体位置：Abstract（~187 words，符合 ≤200 限制但信息过载）
- 问题：Abstract 在 187 词内塞入了 STA、ISR、GRPO、6 reward conditions、3/5 seed rate、Prolog replication、ProofFOL evidence 等大量细节。论文最有记忆点的贡献——observe-vs-optimize asymmetry——被淹没在技术细节中。第 4-7 句连续引入概念，读者需要反复阅读才能理解主线。
- 建议：简化 abstract，前半部分聚焦 problem + method 的直觉（为什么 prove rate 不够？STA 如何诊断？），后半部分聚焦核心发现（asymmetry + 实践含义）。具体数字（3/5 seeds、6 conditions）可省略。

**W4** [warning] Contribution C1-C3 的独立性值得商榷

- 具体位置：§1 Introduction, 第一段末尾的 contribution 列表
- 问题：C1（STA/ISR 作为 diagnostic tool）和 C2（Goodhart effect characterization）是紧密耦合的——Goodhart 发现依赖于 C1 的 metric，而 C1 的价值很大程度上通过 C2 体现。C3（cross-domain evidence）是 C2 的扩展。将这三点列为独立 contribution 有拼凑之嫌。更诚实的表述是：一个核心 contribution（STA 诊断 + Goodhart 发现），辅以 cross-domain 验证。
- 建议：重新组织为 2 个核心 contribution，或者更清晰地阐述 C1 作为独立 diagnostic tool 的价值（即使没有 Goodhart 发现，STA/ISR 是否仍然有用？如果是，增加更多 diagnostic-only 的使用场景）。

---

## 新颖性评估（审查侧重 #1）

**方法层面**：LOO ablation 本身是 standard technique，论文坦诚承认（§3.2, citing DeMillo 1978, Jia & Harman 2011）。ISR metric 的定义（necessary component fraction）是 LOO 的直接应用。方法论层面的新颖性有限。

**应用层面**：将 LOO ablation 系统性地应用于 GRPO-trained neurosymbolic outputs 是新的（据 web search 未发现先行工作）。

**发现层面**：Observe-vs-optimize asymmetry 是论文最有价值的发现。虽然从 Goodhart's Law 理论可以预测 "any metric optimized against will be gamed"，但论文展示了这在 neurosymbolic reasoning 中的具体机制（tautological formalizations, 8 hacking modes）和 seed-dependent dynamics，这是 non-trivial 的实证贡献。

**与 Kim et al. (2026) 的区分**：清晰——Kim 研究 inference-time gaming on FOLIO with frontier models，本文研究 training-time degeneration via component necessity。§2 Related Work 第 11 行明确区分。✓

**与 concurrent RLVR 文献的区分**：基本清晰——Helff et al. (2026) 引入 IPT 但聚焦 inductive reasoning；本文聚焦 formal logic formalization。Shao et al. (2025), Yan et al. (2026) 聚焦 math/code domains。但论文可以更清晰地说明 STA 相比 IPT 的优劣势。

**总体新颖性判断**：中等偏上。Application novelty + empirical findings 足以支撑一篇 focused empirical paper，但作为 EMNLP 长文，novelty depth 是borderline。

---

## Related Work 完整性（审查侧重 #2）

**覆盖面**：Related Work (§2) 分三段覆盖 Neurosymbolic reasoning、Reward hacking/Goodhart's Law、Reward design/structural diagnostics。引用约 57 篇，覆盖全面。

**可能遗漏的引用**：

1. **Metamorphic testing 文献**（Chen et al., 2018 "Metamorphic Testing: A Review of Challenges and Opportunities"）——LOO ablation 与 metamorphic testing 的 source-test-case mutation 有概念上的相似性，但论文仅引用了 software engineering 的 mutation testing (DeMillo, Jia & Harman)。这是一个 minor gap。

2. **Reward model interpretability**——论文引用了 Lundberg & Lee (2017) 的 Shapley value 连接，但没有引用 reward model interpretability 的近期工作（如 reward model probing, reward decomposition），这与 ISR 作为 diagnostic tool 的定位有关。

3. **Wang et al. (2026) "Reward Hacking in the Era of Large Models"** (arXiv:2604.13602)——这是一篇综述，论文已在 references.bib 中列为 `reward-hacking-survey` 但我未在正文中看到显式引用。如果已引用则无问题，否则建议补充。

**引用格式一致性**：
- 大部分 arXiv preprint 使用 `@article` 类型，conference 论文使用 `@inproceedings`——一致 ✓
- McCune Prover9 引用使用 `year = {2005--2010}`，格式稍有不寻常但可接受
- `coste2023reward` 引用中 year=2023 但 booktitle 标注 ICLR 2024，可能有年份不一致
- 部分引用使用 `and others` 缩略（如 LLaMA, DeepSeek），部分列出完整作者——不影响审稿但建议统一

**引用准确性**：抽查了几个关键引用，内容描述准确——Kim et al. (2026) 确为 inference-time gaming on FOLIO (§2, line 11)；Kwa et al. (2024) 确为 catastrophic Goodhart with KL divergence (§2, line 12)；Helff et al. (2026) 确为 RLVR gaming verifiers (§2, line 13)。✓

---

## 论文完整性和叙事逻辑（审查侧重 #3）

**逻辑链**：§4.2 (ISR as Diagnostic) → §4.3 (Goodhart Effects) → §4.4 (Cross-Domain) 的叙事结构清晰。先建立 ISR 的 diagnostic 价值（exec-only 下 ISR→0 揭示 structural degeneration），再展示 ISR-as-reward 的 Goodhart 失败，最后 cross-domain 验证。逻辑连贯。✓

**C1/C2/C3 界定**：如 W4 所述，三个 contribution 的独立性有重叠，但叙事上仍然流畅。

**Limitations**：覆盖了 3 个点（单模型、小数据集、ISR ≠ semantic faithfulness），符合 EMNLP 2026 要求（简短、~3 个点）。但遗漏了以下关键限制：
- STA 的计算开销：每个样本需要 n+1 次 solver call (Appendix B 提到 "n+1 solver calls per sample")，对大规模应用是瓶颈
- Hacking taxonomy 的完整性：8 种模式是从单一模型+数据集观察到的，可能不穷尽

**Conclusion 是否过度概括**：§5 Discussion 总体审慎，使用了 "existence demonstration" 和 "seed-dependent" 等 hedging 语言。但 "the diagnostic—optimization asymmetry persists across logic types (FOL, Prolog) and dataset families (FOLIO, ProofFOL)" 这句稍有过强——如 W2 所述，ProofFOL 上并未验证 optimization 失败。建议修改为 "the diagnostic value persists across... while the optimization failure is confirmed on FOL/Prolog"。

---

## 格式合规检查（审查侧重 #4，EMNLP 2026 / ARR）

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✓ | §1-§5 + Limitations 在 page 1-8 内；Limitations 不计入页数限制 |
| Abstract ≤ 200 words | ✓ | 实测 ~187 words |
| ACL 模板 | ✓ | `\usepackage[review]{acl}`，使用 `times` 字体 |
| 匿名化 | ✓ | 作者行 "Anonymous ACL submission"；代码链接使用 anonymous.4open.science |
| Limitations 在正文 | ✓ | page 8，References 之前 |
| Limitations 不在 Appendix | ✓ | Appendix 无单独 Limitations section |
| 参考文献格式 | ✓ | natbib, `\citep`/`\citet` 使用正确 |
| AI assistants 声明 | ✓ | Appendix E "Use of AI Assistants" 声明使用 Claude |
| Acknowledgments | ✓ | 匿名审稿期间无 acknowledgments section（正确） |
| Double-blind | ✓ | 未发现去匿名化信息 |

**格式问题**：无违规。

---

## 写作质量（审查侧重 #5）

**术语一致性**：STA (Solver Trace Ablation) 和 ISR (Intensional Structural Reward) 在全文中使用一致。✓

**符号定义**：
- β 在 §3.3 中定义为 ISR reward weight，但在不同 condition 中的取值表述分散（Table 1 caption vs §3.3 正文），可以更集中。
- ISR(r) 的数学定义（§3.2, Equation 1）清晰。✓
- "Intensional" 一词的 footnote 2 解释得当（"Not intentional; intensional contrasts with extensional evaluation"）。✓

**Figure/Table quality**：
- Figure 1: 训练轨迹图，caption 充分，但 5 条线在黑白打印下可能难以区分
- Figure 2: STA pipeline overview，设计清晰，(a)(b)(c) 三部分逻辑递进 ✓
- Figure 3: seed-dependent Goodhart，stacked bar + line combination 有效 ✓
- Figure 4: hacking composition，grouped bar chart，caption 解释充分 ✓
- Table 1: Goodhart landscape，信息密集但可读 ✓
- 所有 Figure/Table 均在正文中被引用 ✓

**语法/拼写**：未发现明显错误。写作质量在 EMNLP submission 中属中上水平。

---

## 小问题（不影响接收）

- §3.2 "ISR is thus a component-necessity diagnostic, not a semantic quality metric"——这个限制非常重要，建议提前到 §1 Introduction 中就明确提示读者，避免读者误解 ISR 的含义。
- §4.1 "All experiments draw from FOLIO"——footnote 或正文中可以简要说明为什么选择 FOLIO 而非其他 NLI 数据集（§2 提到 "the only public NLI benchmark with both FOL and Prolog annotations" 但 §4.1 没有重复这个理由）。
- Appendix D.7 Qwen3-8B 的 cross-scale 实验只有 K=1（matching 4B config），建议增加 K=4 或更多 rollout 的实验以充分利用 8B 的容量。
- Figure 6 caption 中 "small-sample artifact, n=21" 应在正文中更显著地讨论，因为这么小的 sample 对 Prolog 结果的可靠性有影响。

---

## 主要优势

1. **实验设计系统且严谨**：6 种 reward conditions (exec-only, ISR 3-seed, ISR 1-seed, Random, Shuffled-ISR, SFT) 形成了 well-controlled 的对比框架；matched random controls 和 shuffled-ISR 提供了良好的 ablation。
2. **Observe-vs-optimize asymmetry 是有实践价值的发现**：即使概念上可预测，具体机制的揭示（tautological gaming, seed-dependent dynamics, 8 hacking modes taxonomy）为 RLVR 社区提供了可操作的诊断工具和实践指南。
3. **诚实的 self-critique**：论文坦承 ISR 的 paradoxical position（§3.2 "ISR occupies a paradoxical position"）、seed-dependent nature、existence-vs-prevalence 区分。这种科学诚实值得肯定。
4. **Cross-logic replication (Prolog)**：虽然 sample 小，但 FOL→Prolog 的复制增加了 structural degeneration 是通用现象的证据。
5. **Hacking taxonomy (Appendix C)**：8 种模式的定义、示例和 ISR interaction 分析为后续研究提供了有价值的分类框架。
6. **Reproducibility**：匿名代码仓库、完整超参数表(Table 4)、per-seed 详细结果(Tables 9-12)。

---

## Missing References（建议补充）

1. Chen, T.Y., Kuo, F.C., Liu, H., et al. (2018). "Metamorphic Testing: A Review of Challenges and Opportunities." *ACM Computing Surveys* 51(1). — LOO ablation 与 metamorphic testing 的概念联系。
2. 如 `reward-hacking-survey` (Wang et al., 2026, arXiv:2604.13602) 已在 bib 中但未在正文引用，建议在 §2 显式引用这篇综述。
3. 考虑引用 Pan et al. (2023) "Logic-LM" 的后续工作中是否有关于 formalization quality 的讨论。

---

## Questions for Authors

1. 如果将 seed 数量增加到 15-20 个，你预期 gaming rate 会稳定在什么水平？是否有初步结果？
2. 是否尝试过在 ISR reward 中加入 tautological detection filter（即检测 conclusion embedding 后排除 ISR=1 的 tautological case），以修复 ISR 的 gameable blind spot？
3. STA 的 n+1 solver call overhead 在实际部署中是否 prohibitive？是否有近似版本（如 sampling-based LOO）能降低成本？
4. Qwen3-8B 的 cold-start failure (Appendix D.7) 是否暗示 Goodhart effect 是 model-capacity-dependent 的？如果是，这对论文的泛化 claim 意味着什么？

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

_source line 3334 · 2026-05-25T21:27:40.057840+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意（并简要说明理由），或用 **[REBUT]** 表示反驳（并引用具体 Section/Table/Figure 提供证据）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3 / 5 |\n| Excitement | 3.5 / 5 |\n| Reproducibility | 4 / 5 |\n| Confidence | 4 / 5 |\n\n### Must-Fix 问题\n\n**N1** [critical] ISR 标量诊断价值在 premise-count 控制后几乎消失，论文核心贡献定位不清\n\n- §4.2 \"Premise-count confound\"、Appendix B、Table 1\n- 214× raw ISR collapse 在 premise-count matched comparison 后仅为 1.06×（McNemar p=0.317, n.s.）。ISR 标量本身在控制 premise count 后无法区分 exec-only 和 ISR-trained models。论文转向 \"compositional evidence survives this control\"，但实际是 hacking mode classification（CE/TS 文本匹配）在做诊断工作，而非 ISR 本身。\n- 核心贡献定位需从 ISR 标量转向 STA-as-procedure（生成 LOO ablation data 以支持 mode classification）。\n\n**N2** [critical] ISR-as-reward 的 Goodhart 效应缺乏统计支撑：ISR 与 Random 的非 hacking 率差异不显著\n\n- Table 6（Appendix B），§4.2\n- ISR vs Random non-hacking rate: 6.06% vs. 9.5%，Fisher p=0.182，n.s.。论文无法在统计上证明 ISR-as-reward 导致了比 random reward 更多的 gaming。\n- TS composition shift（p < 10⁻³⁸）是成立的，但这是 type 而非 amount 的差异。\n- Goodhart claim 应限定为 \"compositional Goodhart\"。\n\n**N3** [critical] 3-5 seeds 的样本量不足以支撑论文的概率性 claims\n\n- §4.2 \"Seed-dependent outcomes\"\n- 3/5 seeds gaming 的 95% CI 为 [11.8%, 88.1%]。Seeds 45-46 是 post-hoc 添加的。\n- 作为 existence proof 足够，但论文叙述超越了 existence proof。\n\n### Should-Fix 问题\n\n**W1** [warning] Seed 43 评估协议不一致，影响多个关键结论\n- s43 使用 nucleus sampling（T=0.7）而非 greedy decoding\n- Random β=0.1 的 TS 率被 s43 主导（s43: 38.3%, s42/s44: 0%）\n- N=2 sensitivity analysis 放在 Appendix，但主表用 3-seed 数据\n\n**W2** [warning] 标题和 Abstract 的概括性超出实验证据范围\n- 仅测试一种 structural reward（ISR）、一个模型家族（Qwen3）、一个主要基准（FOLIO）\n\n**W3** [warning] Qwen3-8B 非收敛的因果解读存在混淆变量\n- 8B 配置与 4B 存在多项差异（K=8 vs K=4、effective batch size 16 vs 8）\n\n**W4** [warning] ProofFOL \"dataset-dependent asymmetry\" 的解释是 post-hoc 的\n- p=0.10 的结果仍提取了 \"ISR reward effectively corrective\" 的实质性结论\n\n**W5** [warning] Hacking mode classifier recall 未知，non-hacking 率可能被高估\n- Precision=100%（152 samples），但 recall 未知。TSb 的发现说明 subtle modes 可能被遗漏。\n\n### Questions\nQ1: STA 的核心价值是 ISR 标量还是 LOO ablation 产生的 per-component data？\nQ2: Seed 43 的 \"greedy-mode degeneration\" 具体表现？\nQ3: 再添加 5 个 seeds 预期 gaming 率？\nQ4: 实践中应用什么具体的 evaluation protocol？\nQ5: Shuffled-ISR 的低 PR (15%) 是否是 hacking 减少的混淆因素？\n\n---\n\n请对每个 N1-N3、W1-W5 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
  "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
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
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意（并简要说明理由），或用 **[REBUT]** 表示反驳（并引用具体 Section/Table/Figure 提供证据）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3 / 5 |\n| Excitement | 3.5 / 5 |\n| Reproducibility | 4 / 5 |\n| Confidence | 4 / 5 |\n\n### Must-Fix 问题\n\n**N1** [critical] ISR 标量诊断价值在 premise-count 控制后几乎消失，论文核心贡献定位不清\n\n- §4.2 \"Premise-count confound\"、Appendix B、Table 1\n- 214× raw ISR collapse 在 premise-count matched comparison 后仅为 1.06×（McNemar p=0.317, n.s.）。ISR 标量本身在控制 premise count 后无法区分 exec-only 和 ISR-trained models。论文转向 \"compositional evidence survives this control\"，但实际是 hacking mode classification（CE/TS 文本匹配）在做诊断工作，而非 ISR 本身。\n- 核心贡献定位需从 ISR 标量转向 STA-as-procedure（生成 LOO ablation data 以支持 mode classification）。\n\n**N2** [critical] ISR-as-reward 的 Goodhart 效应缺乏统计支撑：ISR 与 Random 的非 hacking 率差异不显著\n\n- Table 6（Appendix B），§4.2\n- ISR vs Random non-hacking rate: 6.06% vs. 9.5%，Fisher p=0.182，n.s.。论文无法在统计上证明 ISR-as-reward 导致了比 random reward 更多的 gaming。\n- TS composition shift（p < 10⁻³⁸）是成立的，但这是 type 而非 amount 的差异。\n- Goodhart claim 应限定为 \"compositional Goodhart\"。\n\n**N3** [critical] 3-5 seeds 的样本量不足以支撑论文的概率性 claims\n\n- §4.2 \"Seed-dependent outcomes\"\n- 3/5 seeds gaming 的 95% CI 为 [11.8%, 88.1%]。Seeds 45-46 是 post-hoc 添加的。\n- 作为 existence proof 足够，但论文叙述超越了 existence proof。\n\n### Should-Fix 问题\n\n**W1** [warning] Seed 43 评估协议不一致，影响多个关键结论\n- s43 使用 nucleus sampling（T=0.7）而非 greedy decoding\n- Random β=0.1 的 TS 率被 s43 主导（s43: 38.3%, s42/s44: 0%）\n- N=2 sensitivity analysis 放在 Appendix，但主表用 3-seed 数据\n\n**W2** [warning] 标题和 Abstract 的概括性超出实验证据范围\n- 仅测试一种 structural reward（ISR）、一个模型家族（Qwen3）、一个主要基准（FOLIO）\n\n**W3** [warning] Qwen3-8B 非收敛的因果解读存在混淆变量\n- 8B 配置与 4B 存在多项差异（K=8 vs K=4、effective batch size 16 vs 8）\n\n**W4** [warning] ProofFOL \"dataset-dependent asymmetry\" 的解释是 post-hoc 的\n- p=0.10 的结果仍提取了 \"ISR reward effectively corrective\" 的实质性结论\n\n**W5** [warning] Hacking mode classifier recall 未知，non-hacking 率可能被高估\n- Precision=100%（152 samples），但 recall 未知。TSb 的发现说明 subtle modes 可能被遗漏。\n\n### Questions\nQ1: STA 的核心价值是 ISR 标量还是 LOO ablation 产生的 per-component data？\nQ2: Seed 43 的 \"greedy-mode degeneration\" 具体表现？\nQ3: 再添加 5 个 seeds 预期 gaming 率？\nQ4: 实践中应用什么具体的 evaluation protocol？\nQ5: Shuffled-ISR 的低 PR (15%) 是否是 hacking 减少的混淆因素？\n\n---\n\n请对每个 N1-N3、W1-W5 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
    "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
  }
}
```

</details>

---


### Tool result

_source line 3335 · 2026-05-25T21:28:01.535261+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21477
}
```

</details>

---


### Tool call

_source line 3336 · 2026-05-25T21:28:02.339893+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意（并简要说明理由），或用 **[REBUT]** 表示反驳（并引用具体 Section/Table/Figure 提供证据）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5 / 5 |\n| Excitement | 3 / 5 |\n| Reproducibility | 4 / 5 |\n| Confidence | 4 / 5 |\n\n### Must-Fix 问题\n\n**N1** [critical] 核心发现的统计效力不足——3/5 seed gaming rate\n- 5 个 seed 中 3 个出现 gaming (60%)，无法与随机（50%）可靠区分\n- Limitations 自称 \"existence demonstration\" 但 §5 Discussion 做出较强泛化论述\n- Claim 强度与证据强度不匹配\n- 建议增加至少 10-15 个 seed，或界定为 case study 级别发现\n\n**N2** [critical] 单一模型族限制了可推广性\n- 所有主实验基于 Qwen3-4B\n- 8B 结果极初步且不同动力学（cold-start failure）\n- 标题使用泛化措辞但证据不支持\n- 建议增加至少一个非 Qwen 模型族的完整实验\n\n### Should-Fix 问题\n\n**W1** [warning] Observe-vs-optimize 不对称性的理论解释偏浅\n- 归因于 \"tautological formalizations satisfy necessity criterion by construction\"，本质上是 LOO metric 的已知缺陷\n- 没有讨论：(a) 这是 LOO 特有还是所有 structural diagnostic 的共性？(b) 是否存在修复 ISR 的方法？\n- 建议增加讨论 tautological blind spot 的修复可能性\n\n**W2** [warning] Cross-dataset 验证 (ProofFOL) 的证据有限\n- ProofFOL 仅在 exec-only 和 random 条件下运行，无 ISR reward 条件\n- 只验证了 \"diagnostic 有效\" 一半，未验证 \"reward 失败\" 一半\n- 建议补充 ProofFOL 上 ISR β=0.1 实验\n\n**W3** [warning] Abstract 信息密度过高\n- ~187 words 内塞入大量技术细节\n- observe-vs-optimize asymmetry 被淹没\n- 建议简化，聚焦 problem + core finding\n\n**W4** [warning] Contribution C1-C3 的独立性值得商榷\n- C1 和 C2 紧密耦合（Goodhart 依赖 ISR，ISR 价值通过 Goodhart 体现）\n- C3 是 C2 的扩展\n- 建议重组为 2 个核心 contribution\n\n### 新颖性判断\n- 方法新颖性有限（LOO ablation 是 standard technique）\n- 应用新颖性中等（GRPO-trained neurosymbolic outputs）\n- 发现新颖性中等偏上（observe-vs-optimize asymmetry 的具体机制）\n- 总体：中等偏上，作为 EMNLP 长文 borderline\n\n### Missing References\n1. Chen et al. (2018) \"Metamorphic Testing\" — LOO ablation 与 metamorphic testing 的概念联系\n2. reward-hacking-survey (Wang et al., 2026) 可能在 bib 中但未在正文引用\n3. Pan et al. (2023) \"Logic-LM\" 后续关于 formalization quality 的讨论\n\n### Questions\nQ1: 增加到 15-20 seeds 预期 gaming rate 稳定在什么水平？\nQ2: 是否尝试过 tautological detection filter 修复 ISR？\nQ3: STA 的 n+1 solver call overhead 在实际部署中是否 prohibitive？\nQ4: Qwen3-8B cold-start failure 是否暗示 Goodhart effect 是 capacity-dependent 的？\n\n---\n\n请对每个 N1-N2、W1-W4 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "solver-trace-ablation",
  "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
  "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
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
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意（并简要说明理由），或用 **[REBUT]** 表示反驳（并引用具体 Section/Table/Figure 提供证据）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5 / 5 |\n| Excitement | 3 / 5 |\n| Reproducibility | 4 / 5 |\n| Confidence | 4 / 5 |\n\n### Must-Fix 问题\n\n**N1** [critical] 核心发现的统计效力不足——3/5 seed gaming rate\n- 5 个 seed 中 3 个出现 gaming (60%)，无法与随机（50%）可靠区分\n- Limitations 自称 \"existence demonstration\" 但 §5 Discussion 做出较强泛化论述\n- Claim 强度与证据强度不匹配\n- 建议增加至少 10-15 个 seed，或界定为 case study 级别发现\n\n**N2** [critical] 单一模型族限制了可推广性\n- 所有主实验基于 Qwen3-4B\n- 8B 结果极初步且不同动力学（cold-start failure）\n- 标题使用泛化措辞但证据不支持\n- 建议增加至少一个非 Qwen 模型族的完整实验\n\n### Should-Fix 问题\n\n**W1** [warning] Observe-vs-optimize 不对称性的理论解释偏浅\n- 归因于 \"tautological formalizations satisfy necessity criterion by construction\"，本质上是 LOO metric 的已知缺陷\n- 没有讨论：(a) 这是 LOO 特有还是所有 structural diagnostic 的共性？(b) 是否存在修复 ISR 的方法？\n- 建议增加讨论 tautological blind spot 的修复可能性\n\n**W2** [warning] Cross-dataset 验证 (ProofFOL) 的证据有限\n- ProofFOL 仅在 exec-only 和 random 条件下运行，无 ISR reward 条件\n- 只验证了 \"diagnostic 有效\" 一半，未验证 \"reward 失败\" 一半\n- 建议补充 ProofFOL 上 ISR β=0.1 实验\n\n**W3** [warning] Abstract 信息密度过高\n- ~187 words 内塞入大量技术细节\n- observe-vs-optimize asymmetry 被淹没\n- 建议简化，聚焦 problem + core finding\n\n**W4** [warning] Contribution C1-C3 的独立性值得商榷\n- C1 和 C2 紧密耦合（Goodhart 依赖 ISR，ISR 价值通过 Goodhart 体现）\n- C3 是 C2 的扩展\n- 建议重组为 2 个核心 contribution\n\n### 新颖性判断\n- 方法新颖性有限（LOO ablation 是 standard technique）\n- 应用新颖性中等（GRPO-trained neurosymbolic outputs）\n- 发现新颖性中等偏上（observe-vs-optimize asymmetry 的具体机制）\n- 总体：中等偏上，作为 EMNLP 长文 borderline\n\n### Missing References\n1. Chen et al. (2018) \"Metamorphic Testing\" — LOO ablation 与 metamorphic testing 的概念联系\n2. reward-hacking-survey (Wang et al., 2026) 可能在 bib 中但未在正文引用\n3. Pan et al. (2023) \"Logic-LM\" 后续关于 formalization quality 的讨论\n\n### Questions\nQ1: 增加到 15-20 seeds 预期 gaming rate 稳定在什么水平？\nQ2: 是否尝试过 tautological detection filter 修复 ISR？\nQ3: STA 的 n+1 solver call overhead 在实际部署中是否 prohibitive？\nQ4: Qwen3-8B cold-start failure 是否暗示 Goodhart effect 是 capacity-dependent 的？\n\n---\n\n请对每个 N1-N2、W1-W4 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "solver-trace-ablation",
    "chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
    "director_session_key": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
  }
}
```

</details>

---


### Tool result

_source line 3337 · 2026-05-25T21:28:03.698906+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1359
}
```

</details>

---


### Assistant

_source line 3338 · 2026-05-25T21:28:08.914170+00:00_

交叉分享已派发。等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 298

## Round 298

2 recorded events


### User

_source line 3339 · 2026-05-25T21:28:11.488356+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**摘要**：给出 Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3。

两个 Must-Fix：
1. 3/5 seed gaming rate 统计效力不足，无法与随机区分，但论文在 Discussion 中做出了较强的泛化论述
2. 单一模型族 (Qwen3-4B)，标题和 abstract 的泛化措辞（"Neurosymbolic Reasoning"）与实际证据范围不匹配

四个 Should-Fix：observe-vs-optimize 理论解释偏浅、ProofFOL 仅验证 diagnostic 未验证 optimization 失败、abstract 信息过载、C1-C3 独立性值得商榷。

格式合规全部通过（页数、abstract 字数、匿名化、Limitations 位置等）。写作质量中上。

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

_source line 3340 · 2026-05-25T21:28:25.365143+00:00_

Reviewer 2 初审确认收到。交叉分享已于上一步同时派发给两位 Reviewer，等待双方的 [AGREE]/[REBUT] 交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 299

## Round 299

2 recorded events


### User

_source line 3341 · 2026-05-25T21:29:52.664296+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 3/5 seed gaming rate 统计效力不足**

同意核心判断。这与我自己的 N3 高度一致。5 seeds 的 95% Clopper-Pearson CI 为 [11.8%, 88.1%]（§4.2），无法与随机区分。补充两点：

1. R2 建议增加到 10-15 seeds，我认为仍可能不足。论文展示了 multi-attractor dynamics（§4.1 "Cross-seed instability"），不同 seeds 收敛到不同 hacking modes（s42→CE, s43→Repetition, s44→Tautological）。这种 qualitative divergence 意味着即使 30 seeds 也可能呈现高方差。论文应该明确讨论需要多少 seeds 才能可靠估计 Goodhart 概率，而不是简单增加数量。

2. 论文在 Limitations 中称 "existence demonstration"，但正文叙述（§4.2 "3 of 5 seeds converge to gaming"、§5 "the Goodhart effect is seed-dependent"）的措辞暗示了概率估计。这种 framing 不一致确实是问题。

**[REBUT] R2-N2: 单一模型族限制可推广性**

部分反驳。R2 的核心关切（仅 Qwen3 一个模型族）成立，但低估了论文已有的泛化证据：

1. **Cross-logic replication**（§4.3, Figure 6）：FOL→Prolog 的复制展示了三条独立的 gaming pathway（clean TS, uppercase pseudo-Prolog, query-as-fact），跨越了完全不同的逻辑体系和 solver（Prover9 vs. SWI-Prolog）。这不是模型泛化，但证明了 Goodhart 效应在不同 symbolic backend 中复现。

2. **Cross-dataset replication**（§4.3, Table 12）：FOLIO→ProofFOL 展示了不同 dataset structure（3.4× more premises, simpler predicates; Table 2）下的 diagnostic 有效性。

3. **LLaMA-3.2-3B cold-start**（Appendix D.3）和 **non-converging seeds**（Appendix D.5, s45/s52）提供了反面证据：不收敛时不退化。虽然不是完整实验，但支持了 "degeneration requires successful optimization" 的 claim。

4. R2 建议增加 "至少一个非 Qwen 模型族的完整实验"——我同意这会显著增强论文，但认为这更接近 **Should-Fix** 而非 **Must-Fix**。原因是论文的核心 claim 是关于 ISR/LOO metric 的结构性缺陷（tautological formalizations 满足 LOO necessity by construction, §3.2），这是 metric 层面的问题，不依赖于特定模型。标题措辞确实需要收窄（与我的 W2 一致），但增加模型族不是核心科学贡献成立的前提。

---

### Should-Fix 问题

**[AGREE] R2-W1: Observe-vs-optimize 理论解释偏浅**

同意。论文将 asymmetry 归因于 "tautological formalizations satisfy the necessity criterion by construction"（§3.2, §5），这是一个正确但表层的观察。缺失的讨论包括：

- 这是 LOO 特有的（因为 LOO 只检查 marginal contribution，对 P→P tautology 无法识别）还是所有 structural diagnostic 的共性？例如，full Shapley value（O(2^n) 评估）是否也会被游戏化？论文在 Appendix B 提到 ISR 是 Shapley value 的 (n-1)-coalition restriction，但未讨论 full Shapley 是否免疫。
- 是否存在修复 ISR 的方法？例如在 LOO 之前增加 tautology pre-filter（检查 premise ≡ conclusion），或结合 semantic faithfulness check。这些讨论对读者的 actionable takeaway 很重要。

**[REBUT] R2-W2: ProofFOL 缺少 ISR reward 条件**

R2 的事实判断有误。论文 **确实在 ProofFOL 上运行了 ISR β=0.1 实验**：

- §4.3 "ProofFOL ISR (β=0.1): dataset-dependent asymmetry" 明确报告了结果
- Table 12（Appendix D, p.20）给出了 ProofFOL ISR β=0.1 的三个 seed 详细数据：s42 (PR=0.35, Genuine=100%), s43 (PR≈0.47, Genuine=30.4%), s44 (PR=0.49, Genuine=100%)
- Aggregate genuine rate: 76.8% vs exec-only 17.4%（permutation test p=0.10, exploratory）

论文不仅验证了 "diagnostic 有效"，还验证了 "reward 在 ProofFOL 上的效果不同于 FOLIO"——ISR reward 在 ProofFOL 上表现为 corrective 而非 Goodhart，因为 CE（而非 TS）主导了 hacking geometry，使 ISR≈0 而非 ISR≥0.5。这恰恰展示了 "reward 失败" 的 dataset-dependent boundary conditions。

R2 可能因为 ProofFOL 的 ISR 结果未出现在 Table 1（主表）中而遗漏了这部分内容。

**[AGREE] R2-W3: Abstract 信息密度过高**

轻度同意。Abstract 约 180 words，技术上合规（≤200 words），但在有限空间内塞入了 STA 定义、ISR 定义、六种 reward conditions、3/5 seed 统计、cross-logic replication、cross-dataset evidence——导致核心 message（observe-vs-optimize asymmetry）被稀释。不过我认为这是 **写作优化** 问题而非 **学术严谨性** 问题，严重程度低于 R2 的定位。

**[REBUT] R2-W4: Contribution C1-C3 的独立性**

部分反驳。C1-C3 之间确有逻辑耦合，但我认为它们对不同读者群体有独立价值：

- **C1（STA/ISR 作为诊断）**：对部署 neurosymbolic RL 系统的从业者有直接价值，即使他们不关心 Goodhart 理论。§4.1 的 collapse trajectory（ISR 从 0.642 降到 0.003）和 mode breakdown 是独立可用的诊断工具。
- **C2（Goodhart 效应）**：对 reward design 研究者有价值，展示了 metric → reward 转换的风险。这个发现逻辑上依赖于 C1 的 ISR 定义，但科学贡献是独立的。
- **C3（Hacking taxonomy）**：8 种 modes 的分类体系（Table 3, Appendix C）有独立的参考价值，后续研究可以直接使用这个分类框架。

R2 建议重组为 2 个 contributions 的方案会损失粒度。当前的 3-contribution 结构与 Introduction §1 末尾的组织（"(C1) a systematic analysis...; (C2) empirical characterization...; (C3) cross-logic replication..."）一致且清晰。

---

### 对 R2 Missing References 的回应

1. **Chen et al. (2018) "Metamorphic Testing"**：有价值的概念联系。STA 的 LOO ablation 与 metamorphic testing 的 "变换后预期行为" 理念确有相似之处，但论文已引用 DeMillo et al. (1978) 和 Jia & Harman (2011) 建立了 mutation testing 的联系（§3.2），coverage 充分。
2. **reward-hacking-survey (Wang et al., 2026)**：如果确实存在但未引用，应补充。
3. **Pan et al. (2023) "Logic-LM"**：已在 Related Work §2 引用（"Ye et al., 2023; Pan et al., 2023; Olausson et al., 2023..."）。R2 可能是指 Logic-LM 的后续关于 formalization quality 的专门讨论，如果是特定后续论文则建议作者检查。

---

### 对 R2 Questions 的补充意见

**Q2（tautological detection filter 修复 ISR）**：这是一个重要方向。论文在 Appendix D.1 测试了 O(1) binary tautology check，结果表明它过于粗糙（所有 ProofFOL 样本都通过）。但未测试将 tautology filter 与 O(n) ISR 结合的方案（例如：先排除 P≡C 的 TS，再计算剩余的 ISR）。这个 gap 值得在 Discussion 中补充。

**Q4（Goodhart effect 是否 capacity-dependent）**：与我的 W3 相关。8B 结果（Appendix D.8）的因果解读被多个混淆变量（K=8 vs K=4, effective batch 16 vs 8）干扰，不能简单归因于 capacity。论文的 "convergence threshold" 表述需要降级为 correlational observation。

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

_source line 3342 · 2026-05-25T21:30:07.325081+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 300

## Round 300

2 recorded events


### User

_source line 3343 · 2026-05-25T21:30:09.886919+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **[AGREE] R2-N1**: 同意 seed 数量不足，补充指出 multi-attractor dynamics 使得即使增加到 10-15 seeds 仍可能不够
- **[REBUT] R2-N2**: 部分反驳，论文已有 cross-logic/cross-dataset 泛化证据，建议从 Must-Fix 降级为 Should-Fix
- **[AGREE] R2-W1**: 同意理论解释偏浅，应讨论 LOO 特异性和修复可能
- **[REBUT] R2-W2**: R2 事实有误——论文确实在 ProofFOL 上运行了 ISR β=0.1（§4.3, Table 12）
- **[AGREE] R2-W3**: 轻度同意 Abstract 密度过高，但属于写作优化而非学术问题
- **[REBUT] R2-W4**: 部分反驳 C1-C3 合并建议，三个 contribution 对不同读者群有独立价值

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

_source line 3344 · 2026-05-25T21:30:16.879287+00:00_

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


## Round 301

## Round 301

14 recorded events


### User

_source line 3345 · 2026-05-25T21:31:48.837908+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: ISR 标量诊断价值在 premise-count 控制后几乎消失**

同意 R1 的核心观察。§4.2 "Premise-count confound" 明确承认 214× raw ISR collapse 在 matched comparison 后仅为 1.06×（McNemar p=0.317, n.s.）。论文自己也在 Limitations 中写道 "diagnostic value comes from the mode breakdown, not the scalar alone (Appendix B)"。

但我认为 R1 将此定性为 "must-fix" 有一定 overstatement：论文并未声称 ISR *标量*是唯一诊断工具——§3.2 定义 ISR 后紧接着引入了 hacking mode classification (§3.3)，且 §4.2 的主要叙事线已经是 mode breakdown（Figure 4, Table 3），ISR 标量更多作为 overview metric。问题出在 **framing**：标题（"Structural Rewards"）、Abstract、和 C1 的表述让读者以为 ISR 标量本身是核心贡献。

**建议方向**：同意 R1——将核心贡献定位从 "ISR metric" 转向 "STA procedure + mode taxonomy"，ISR 标量降级为 summary statistic。这是 framing 问题而非 soundness 问题。

---

**[AGREE with nuance] R1-N2: ISR vs Random 非 hacking 率差异不显著**

R1 引用的数据准确——Table 6 (Appendix B) 显示 ISR vs Random non-hacking rate: 6.06% vs 9.5%，Fisher p=0.182 (n.s.)。这确实意味着从 *总量* 角度无法说 ISR-as-reward 比 random reward 产生了更多 gaming。

但我对 R1 的结论有一个补充：论文引用的 Goodhart 分类是 Manheim & Garrabrant (2019) 的 **regressional Goodhart pattern**（§2, §4.3）。Regressional Goodhart 的定义本身就是 proxy optimization 导致的 *compositional shift*——优化 proxy 不一定增加总 hacking 量，但会将 hacking 集中到 proxy 的 specific blind spots。论文的 TS composition shift (p < 10⁻³⁸) 恰好符合这个模式：ISR reward 将 gaming 系统性地导向 TS（tautological shortcut），因为 TS 满足 LOO necessity criterion by construction。因此，Goodhart claim 在 regressional 框架下**逻辑上成立**。

**但 R1 的建议完全正确**：论文应明确标注这是 "compositional/regressional Goodhart"，而非 "ISR 导致了比 random 更多的 gaming"。当前叙述（§4.3 第一段）确实容易让读者理解为后者。

---

**[AGREE] R1-N3: 3-5 seeds 样本量不足**

完全同意。这与我自己的 N1 一致。R1 提供的 95% CI [11.8%, 88.1%] 量化了问题严重程度——这个区间覆盖了从 "rare event" 到 "almost certain" 的全部范围，无法得出任何可靠的 prevalence 结论。

R1 还指出 seeds 45-46 是 post-hoc 添加的（§4.1 footnote 3: "Seed 43 uses nucleus sampling... seeds 45-46 added post-hoc"），这进一步削弱统计推断。

作为 existence proof 这些 seed 数够用，但论文叙述多处超越了 existence proof 的范围（特别是 §5 的泛化论述）。

---

### Should-Fix 问题

**[AGREE] R1-W1: Seed 43 评估协议不一致**

确认 Appendix D.6 记载 seed 43 使用 T=0.7 nucleus sampling 而非 greedy decoding。R1 正确指出这影响了 pooled analysis 的一致性——特别是 Random β=0.1 条件下 s43 贡献了 38.3% TS rate 而 s42/s44 为 0%（Table 9, Appendix D），说明 s43 的异常行为可能是 decoding strategy 导致而非 reward condition 导致。

**但我注意到论文已提供了 robustness check**：Table 13 (Appendix D.6) 报告了排除 s43 后（N=2, seeds 42/44 only）的 pooled statistics，"exec-only converges to ≤7.5% non-hacking; ISR 2→0.1 shifts composition toward tautological shortcut"。这说明主要定性结论在排除 s43 后仍然成立。

R1 的建议合理：main text 的 pooled 分析应基于 protocol-一致的 seeds（即排除 s43 或重新用 greedy decoding 评估 s43），sensitivity analysis 放 appendix 作为补充。

---

**[AGREE] R1-W2: 标题和 Abstract 概括性超出实验范围**

与我自己的 N2 和 W3 一致。标题说 "Neurosymbolic Reasoning"（泛化）而实验仅覆盖 Qwen3-4B + FOLIO（具体）。Abstract 塞入过多技术细节而核心 message 被淹没。

---

**[AGREE with minor reservation] R1-W3: Qwen3-8B 非收敛的因果解读存在混淆变量**

同意 8B 实验的因果推断不清晰。Appendix D.7 将 8B 的 "cold-start failure" 归因于 "lack of FOL generation capability" 和 "collateral diversity bottleneck"，但如 R1 所述，配置差异（如 effective batch size）可能是混淆因素。

**不过**，关于 R1 提出的具体数值 "K=8 vs K=4"——从 Table 4 (Appendix A) 看，4B 配置为 "Rollouts per prompt (K): 1"，Appendix D.7 也说 "We first tested K = 1 (matching the 4B configuration)"。所以 K 值实际上是 matched 的 (K=1=1)，R1 给出的 "K=8 vs K=4" 可能有误。但 R1 关于 effective batch size 差异和 per-device 配置差异的 broader concern 仍然有效——8B 和 4B 在相同 K 下可能有不同的 gradient dynamics。

---

**[AGREE] R1-W4: ProofFOL "dataset-dependent asymmetry" 解释是 post-hoc 的**

与我自己的 W2 一致。ProofFOL 仅运行了 exec-only 和 random 条件，没有 ISR-as-reward 实验。因此只验证了 "diagnostic 有效" 但未验证 "reward 失败"。p=0.10 的结果本身就 borderline，在此基础上提取 "ISR reward effectively corrective" 的实质性结论是 overinterpretation。

---

**[AGREE] R1-W5: Hacking mode classifier recall 未知**

同意。论文报告 precision=100%（152 samples manually verified），但 recall 未知。Appendix B (page 14) 自己也承认 "subtle semantic manipulations below our text-matching threshold would evade the strict classifier"。TSb 的发现（12 samples reclassified from non-hacking to TS, page 15）具体说明了 recall gap 的存在——text-match classifier 遗漏了 vacuous quantifier wrapping 和 structural simplification 两种 subtle TS variants。

这意味着论文报告的 non-hacking rate（Table 1 的 N-H% 列）是 **上界**——真实的 non-hacking rate 可能更低。如果 recall gap 在不同 conditions 间不均匀分布，可能会影响 condition 间的比较。

---

### 对 R1 Questions 的补充意见

**Q1 (STA 核心价值是 ISR 标量还是 LOO per-component data)**：同意 R1 的隐含观点——STA 的核心价值在于 LOO procedure 产生的 per-component necessity data（支持 mode classification），而非 ISR 标量本身。论文应据此调整 framing。

**Q5 (Shuffled-ISR 低 PR 是否混淆)**：这是一个好问题。Shuffled-ISR 的 PR=15% (Table 1) 远低于其他条件，低 PR 本身意味着 fewer proved samples 进入 hacking 分析，non-hacking 的"低率"可能是 sample selection artifact 而非 reward design 的效果。论文应讨论 PR 差异对 hacking rate 比较的影响。

---

### Reviewer 2 的综合判断

R1 的审稿质量很高，数据引用准确，统计检验运用恰当。我在 8 个问题中对 7 个给出 AGREE（含 2 个 with nuance），0 个给出 REBUT。

**两位 Reviewer 共识的核心问题**：
1. **Seed 数量不足** (R1-N3 = R2-N1)：最严重的问题，两位 Reviewer 一致认为 3/5 seeds 无法支撑论文的概率性 claims
2. **单一模型族** (R1-W2 部分 = R2-N2)：Qwen3-4B only + 初步的 8B 实验不足以支撑泛化论述
3. **ISR framing 需调整** (R1-N1 = R2-W4 部分)：核心贡献应从 ISR 标量转向 STA procedure + mode taxonomy
4. **Abstract/Title overclaim** (R1-W2 = R2-W3)

**R1 提出而 R2 初审未充分覆盖的有价值发现**：
- N1 的 premise-count confound 分析——R1 对 p=0.317 的引用非常 precise，我初审时注意到了这一点但没有给予足够权重
- N2 的 Table 6 Fisher test 引用——ISR vs Random non-hacking rate n.s.，我初审时没有单独拉出这个统计检验
- W5 的 classifier recall 问题——我初审提到了 TSb 但没有系统性地讨论 recall gap 对所有 condition 比较的影响

**维持我的总评**：3.5 / 5 (Borderline Conference)。R1 的分析强化了我对证据基础偏窄的担忧，但也确认了论文在实验设计和 scientific honesty 方面的优点。如果作者能增加 seed 数量、至少一个非 Qwen 模型、并按 R1-N1 调整 framing，这篇论文有潜力成为 solid conference paper。

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

_source line 3346 · 2026-05-25T21:32:54.859385+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

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
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 3347 · 2026-05-25T21:32:54.910076+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:17:13.266043+00:00\", \"completed_at\": \"2026-05-25T21:20:32.086957+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 18\", \"message\": \"附录 D.1 节内容仅占页面约 1/3，下方约 2/3 为空白。建议将 D.1 与 D.2 合并排版或调整 LaTeX float 位置以填充空间\"}, {\"severity\": \"warning\", \"dimension\": \"page 23\", \"message\": \"末页\\\"Use of AI Assistants\\\"部分内容极短，约 55% 页面为空白。建议将该声明紧接上一页内容排布\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 4 堆叠条形图中部分颜色段（绿色系各子类、红色系各子类）在小尺寸下区分度偏低，色盲读者可能受影响。建议增加 hatching pattern 或调整色阶间距\"}, {\"severity\": \"info\", \"dimension\": \"page 19-20\", \"message\": \"Tables 9-12 的 Notes 列字号偏小（目测 ~6-7pt），密集注释在打印时可能难以辨读。可考虑将长注释移至表格脚注\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"单页内含 Tables 6、7、8 三个表格，页面视觉密度偏高但内容均为附录详细数据，可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 主结果表格式规范：booktabs 风格、最优值加粗、脚注标记清晰。Figure 3 配色与全文一致\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"单页含 Figure 5 + Table 2 + Table 3，密度高但排版未溢出，间距合理\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 全宽概念图使用红/绿/蓝三色方案，与后续统计图配色语义一致，全文颜色体系统一\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3348 · 2026-05-25T21:32:54.960826+00:00_

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

_source line 3349 · 2026-05-25T21:32:55.011526+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3350 · 2026-05-25T21:32:55.012008+00:00_

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

_source line 3351 · 2026-05-25T21:32:55.112872+00:00_

No matching deferred tools found

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

_source line 3352 · 2026-05-25T21:33:00.736924+00:00_

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

_source line 3353 · 2026-05-25T21:33:00.939616+00:00_

issues:
- id: R1-W1
  summary: "统计效力严重不足：β=0.3 仅 single seed"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。"
  resolution_round: 2
- id: v22-R12-N3
  summary: "Premise-count confound 使 ISR scalar 诊断价值严重削弱"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 22
  last_seen_round: 34
  resolution: "Compositional narrative + screening trigger 定位。method.tex L54 显式定位 ISR 为 screening trigger。"
  resolution_round: 34
- id: v22-R12-N1
  summary: "ISR vs Random non-hacking rate p=0.182 不显著"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 22
  last_seen_round: 33
  resolution: "Compositional Goodhart reframed. χ² as primary evidence."
  resolution_round: 33
- id: v17-R12-W1
  summary: "单模型 (Qwen3-4B) 无法支撑通用性声明"
  category: experiment
  severity: critical
  status: wont_fix
  first_raised_round: 17
  last_seen_round: 35
  resolution: "结构性限制。Claims scoped to Qwen3-4B."
- id: v27-R1-N2
  summary: "CMH pseudo-replication：within-seed samples 非独立"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 27
  last_seen_round: 34
  resolution: "Table 5 caption 增加 descriptive-only 限定 + CMH 引用。"
  resolution_round: 34
- id: v17-R1-W9
  summary: "Seed 43 使用 T=0.7 sampling 评估而非 greedy"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 17
  last_seen_round: 36
  mentions:
    - {round: 36, reviewers: [1, 2], note: "R36 W5 确认已解决，无需进一步修改。"}
  resolution: "正文 N=2 统计句（experiments.tex L65）+ Appendix D.6。"
  resolution_round: 34
- id: v22-R2-N1
  summary: "方法论新颖性不足——LOO 是标准技术"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 22
  last_seen_round: 35
  resolution: "R35 修复：C1 从 'we propose STA' 降级为 'systematic empirical analysis using LOO ablation'。Reviewer 验证 PASS。"
  resolution_round: 35
- id: v29-R2-W5
  summary: "'Observe-vs-opti
…[truncated 9192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 3354 · 2026-05-25T21:35:41.365232+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 34, reviewers: [1, 2], note: \"Compositional narrative + screening trigger 定位。method.tex L54 显式定位 ISR 为 screening trigger。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-N1 重新提出。1.06× p=0.317 n.s. 仍是核心问题。Abstract/Intro 仍以 ISR 为中心叙事，framing 修复不充分。两位 Reviewer 共识：核心贡献应从 ISR 标量转向 STA procedure + mode taxonomy。\"}\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 33, reviewers: [1, 2], note: \"Compositional Goodhart reframed. χ² as primary evidence.\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-N2 重新提出。Fisher p=0.182 n.s. 仍在。R1 建议限定为 compositional Goodhart，R2 同意（with nuance）。当前叙述仍暗示 ISR 优化恶化了整体结果。\"}\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 35, reviewers: [2], note: \"Claims scoped to Qwen3-4B.\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R2-N2 Must-Fix。R1 反驳认为 Should-Fix（cross-logic/cross-dataset 已有泛化证据）。分歧：严重程度。标题 'Neurosymbolic Reasoning' 仍过于泛化。\"}\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 34\n  resolution: \"Table 5 caption 增加 descriptive-only 限定 + CMH 引用。\"\n  resolution_round: 34\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R36 W5 确认已解决，无需进一步修改。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-W1 重新提出。s43 对 Random β=0.1 TS rate 影响大（s43:38.3%, s42/s44:0%）。建议主文 pooled 分析基于 protocol 一致的 seeds。R2 同意但注意到 N=2 robustness check 存在。\"}\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 35\n  resolution: \"R35 修复：C1 从 'we propose STA' 降级为 'systematic empirical analysis using LOO ablation'。Reviewer 验证 PASS。\"\n  resolution_round: 35\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 31, reviewers: [2], note: \"Reframed as empirical instantiation of Goodhart's Law.\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R2-W1 提出理论解释偏浅。缺少讨论：(a) LOO 特有还是所有 structural diagnostic 共性？(b) 修复 ISR 的可能性？R1 同意，补充 full Shapley 免疫性讨论缺失。\"}\n- id: v30-R1-W1\n  summary: \"SFT baseline selection bias\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"SFT positioned as pre-RL temporal reference.\"\n  resolution_round: 31\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 22\n  last_seen_round: 31\n  resolution: \"Positioned as corroborating rather than definitive.\"\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy recall 未评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 34, reviewers: [2], note: \"Limitations 增加 recall 自约束论证。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-W5 重新提出。Precision=100% (152 samples) 但 recall 未知。TSb 发现说明 subtle modes 被遗漏。non-hacking rate 应一致标记为 upper bound（≤6% 而非 6%）。R2 同意。\"}\n- id: v19-R12-W3\n  summary: \"ProofFOL p=0.10 被过度引用 / 跨数据集 persistence claim 误导\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R36 修复：Abstract + Intro 同步改为 'boundary conditions'。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-W4 ProofFOL dataset-dependent asymmetry 解释仍被认为 post-hoc。'ISR reward effectively corrective' 是 overinterpretation。应标记为 hypothesis generation 而非 confirmation。\"}\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 33\n  resolution: \"'reasoning quality' → 'formalization integrity'.\"\n  resolution_round: 32\n- id: v33-N2-BIMODAL\n  summary: \"5-seed 双峰弱化 Goodhart 核心叙事\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 33\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 33, reviewers: [1, 2], note: \"C2 changed to 'seed-dependent Goodhart effect'.\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: 两位 Reviewer 一致认为 3/5 seeds 95% CI [11.8%, 88.1%] 无信息量。seeds 45-46 post-hoc 添加进一步削弱。Existence proof 定位在 Limitations 有但正文叙述超越。R1 补充：multi-attractor dynamics 使增加 seeds 仍可能高方差。\"}\n- id: v33-W1-EXEC-POOLING\n  summary: \"Table 1 exec-only 仅报告 s42\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 33, reviewers: [1], note: \"§4.2 explains. Table 1 footnote expanded.\"}\n    - {round: 37, reviewers: [1], note: \"R37 minor issue: Table 1 exec-only 行仅 seed 42（脚注 †）与 3-seed pooled 行并列，易造成误读。建议行内标注 (single seed)。\"}\n- id: v33-M8-CONVERTS\n  summary: \"'ISR converts CE into TS' 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"'converts' → 'systematically selects for TS over CE'.\"\n  resolution_round: 33\n- id: v33-W3-TAXONOMY\n  summary: \"Taxonomy 互斥性和 N-H upper bound 未在正文说明\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"Priority rule and N-H upper bound added to §3.3.\"\n  resolution_round: 33\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Nishimura et al. 2026 spec gaming\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"Citation added.\"\n  resolution_round: 31\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 32\n  resolution: \"Title shortened.\"\n  resolution_round: 32\n- id: v31-R2-ISR0-AMBIGUITY\n  summary: \"ISR=0 语义不同\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"ISR=0 disambiguation added.\"\n  resolution_round: 31\n- id: v32-R12-MR-UNFAITHFUL-COT\n  summary: \"缺失引用：Lanham/Turpin\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  resolution: \"Both citations added.\"\n  resolution_round: 32\n- id: v34-R12-N1\n  summary: \"C3 贡献声称 overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"C3 establishing→confirming(Prolog)+exploratory(ProofFOL)。\"\n  resolution_round: 34\n- id: v34-R12-N2\n  summary: \"ISR scalar framing 张力\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex L54 ISR screening trigger 定位句。\"\n  resolution_round: 34\n- id: v34-R1-N1\n  summary: \"3-5 seeds proportion claim CI 宽\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 37\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R36 W1: CI 已展示，'can occur' framing 正确。新增 optional stopping concern → limitations 加 post-hoc 声明。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: 两位 Reviewer 再次一致标记为 critical。根本问题（仅 5 seeds）未变，framing 修复不足以消解。\"}\n- id: v34-R1-N2\n  summary: \"Seed 43 sensitivity 可见性不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"正文 L65 N=2 统计句。\"\n  resolution_round: 34\n- id: v34-R1-N3\n  summary: \"Table 5 pooled Fisher 缺 descriptive-only 限定\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"Appendix Table 5 caption 增加限定 + CMH 引用。\"\n  resolution_round: 34\n- id: v34-R12-W1\n  summary: \"Table 1 caption 过长\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"150 词→48 词。\"\n  resolution_round: 34\n- id: v34-R1-W3\n  summary: \"convergence 因果 claim 过强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 34, reviewers: [1], note: \"experiments.tex + conclusion.tex 两处同步弱化。\"}\n    - {round: 37, reviewers: [1], note: \"R37 R1-W3: 8B 不收敛仍被解读为 'degeneration requires convergence'，但 8B 配置与 4B 存在混淆变量。应降级为 correlational observation。\"}\n- id: v34-R2-W3\n  summary: \"正文信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 34, reviewers: [2], note: \"§4.4 开头 exploratory signposting。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 R2-W3 + R1-W2: Abstract 信息过载（~187 words 内塞入过多细节），observe-vs-optimize asymmetry 被淹没。标题泛化措辞与实验范围不匹配。\"}\n- id: v34-R2-W5\n  summary: \"Abstract [anonymized] 脚注\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"已移除。\"\n  resolution_round: 34\n- id: v34-R1-W5\n  summary: \"ISR = Shapley 声称缺推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 35\n  resolution: \"R35: 正文改为 'maximal coalition restriction'。\"\n  resolution_round: 35\n- id: v34-REVIEWER-FIG2\n  summary: \"Figure 2 未被正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex 两处引用。\"\n  resolution_round: 34\n- id: v34-REVIEWER-CONCL\n  summary: \"conclusion.tex confirm 对 ProofFOL 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"ProofFOL 标注 exploratory。\"\n  resolution_round: 34\n- id: v35-R1-M1\n  summary: \"Exec-only 条件仅 1 seed (s42) 完整报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"R35: experiments.tex L35 加 3-seed 1000-step 证据句。\"\n  resolution_round: 35\n- id: v35-R1-M3\n  summary: \"Premise-count confound 对 compositional evidence 未隔离\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"R35: Discussion 加 confound 承认句。R36: 整合为 open question。\"\n  resolution_round: 35\n- id: v35-R2-W2\n  summary: \"缺少与 PRM 的 Goodhart susceptibility 对比讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"R35: Discussion 安全 framing。R36: 整合为 open question。\"\n  resolution_round: 35\n- id: v35-R2-W4\n  summary: \"ISR/ISR* 术语使用不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"功能性 PASS。method.tex L56 'throughout' 约定 + 数值处均用 ISR*。\"\n  resolution_round: 35\n- id: v35-R2-MR1\n  summary: \"缺失引用：Krakovna et al. (2020)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"Related Work 加引用。\"\n  resolution_round: 35\n- id: v36-R12-N2\n  summary: \"Section 1 'any verifiable proxy' 从极窄实验范围过度推广\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 36\n  resolution: \"R36 修复：intro L27 改为 'LOO-based structural proxies---and plausibly other component-necessity measures---face analogous exploitation risks in neurosymbolic settings'。三层限定 + hedge。Reviewer 验证 PASS。\"\n  resolution_round: 36\n- id: v36-R12-W1\n  summary: \"缺少代码和数据可用性声明\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 36\n  resolution: \"R36 修复：Limitations 末尾加 'Code, training scripts, and evaluation data will be released upon acceptance.' Reviewer 验证 PASS。\"\n  resolution_round: 36\n- id: v36-R2-W2\n  summary: \"Shuffled-ISR 非收敛替代解释未讨论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 36\n  resolution: \"R36 修复：experiments L56 'confirms' → 'consistent with' + 显式承认 non-convergence confound。Reviewer 验证 PASS。\"\n  resolution_round: 36\n- id: v36-R2-W4\n  summary: \"Hacking taxonomy 5/8 modes 可靠性存疑\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 36\n  resolution: \"R36 修复：method L97 'CE and TS are robust; remaining five modes are configuration-specific observations'。Reviewer 验证 PASS。\"\n  resolution_round: 36\n- id: v37-R2-W1\n  summary: \"Observe-vs-optimize 理论解释偏浅，缺 LOO 特异性讨论和修复方案\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - {round: 37, reviewers: [1, 2], note: \"R2 提出，R1 同意。缺少：(a) LOO 特有 vs 所有 structural diagnostic 共性？(b) full Shapley 是否免疫？(c) 修复 ISR（如 tautology pre-filter + ISR）的讨论。\"}\n- id: v37-R2-W4\n  summary: \"C1-C3 contribution 独立性值得商榷\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - {round: 37, reviewers: [1, 2], note: \"R2 建议合并为 2 个 contributions；R1 反驳，认为三个对不同读者群有独立价值。轻微分歧，不影响接收。\"}"
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
    "issues_yaml": "issues:\n- id: R1-W1\n  summary: \"统计效力严重不足：β=0.3 仅 single seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。\"\n  resolution_round: 2\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 34, reviewers: [1, 2], note: \"Compositional narrative + screening trigger 定位。method.tex L54 显式定位 ISR 为 screening trigger。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-N1 重新提出。1.06× p=0.317 n.s. 仍是核心问题。Abstract/Intro 仍以 ISR 为中心叙事，framing 修复不充分。两位 Reviewer 共识：核心贡献应从 ISR 标量转向 STA procedure + mode taxonomy。\"}\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 33, reviewers: [1, 2], note: \"Compositional Goodhart reframed. χ² as primary evidence.\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-N2 重新提出。Fisher p=0.182 n.s. 仍在。R1 建议限定为 compositional Goodhart，R2 同意（with nuance）。当前叙述仍暗示 ISR 优化恶化了整体结果。\"}\n- id: v17-R12-W1\n  summary: \"单模型 (Qwen3-4B) 无法支撑通用性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 35, reviewers: [2], note: \"Claims scoped to Qwen3-4B.\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R2-N2 Must-Fix。R1 反驳认为 Should-Fix（cross-logic/cross-dataset 已有泛化证据）。分歧：严重程度。标题 'Neurosymbolic Reasoning' 仍过于泛化。\"}\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 34\n  resolution: \"Table 5 caption 增加 descriptive-only 限定 + CMH 引用。\"\n  resolution_round: 34\n- id: v17-R1-W9\n  summary: \"Seed 43 使用 T=0.7 sampling 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R36 W5 确认已解决，无需进一步修改。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-W1 重新提出。s43 对 Random β=0.1 TS rate 影响大（s43:38.3%, s42/s44:0%）。建议主文 pooled 分析基于 protocol 一致的 seeds。R2 同意但注意到 N=2 robustness check 存在。\"}\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 35\n  resolution: \"R35 修复：C1 从 'we propose STA' 降级为 'systematic empirical analysis using LOO ablation'。Reviewer 验证 PASS。\"\n  resolution_round: 35\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 31, reviewers: [2], note: \"Reframed as empirical instantiation of Goodhart's Law.\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R2-W1 提出理论解释偏浅。缺少讨论：(a) LOO 特有还是所有 structural diagnostic 共性？(b) 修复 ISR 的可能性？R1 同意，补充 full Shapley 免疫性讨论缺失。\"}\n- id: v30-R1-W1\n  summary: \"SFT baseline selection bias\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 32\n  resolution: \"SFT positioned as pre-RL temporal reference.\"\n  resolution_round: 31\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 22\n  last_seen_round: 31\n  resolution: \"Positioned as corroborating rather than definitive.\"\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy recall 未评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 34, reviewers: [2], note: \"Limitations 增加 recall 自约束论证。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-W5 重新提出。Precision=100% (152 samples) 但 recall 未知。TSb 发现说明 subtle modes 被遗漏。non-hacking rate 应一致标记为 upper bound（≤6% 而非 6%）。R2 同意。\"}\n- id: v19-R12-W3\n  summary: \"ProofFOL p=0.10 被过度引用 / 跨数据集 persistence claim 误导\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R36 修复：Abstract + Intro 同步改为 'boundary conditions'。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: R1-W4 ProofFOL dataset-dependent asymmetry 解释仍被认为 post-hoc。'ISR reward effectively corrective' 是 overinterpretation。应标记为 hypothesis generation 而非 confirmation。\"}\n- id: v30-R2-W3\n  summary: \"ISR 与 NLI accuracy 不相关限制 actionability\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 30\n  last_seen_round: 33\n  resolution: \"'reasoning quality' → 'formalization integrity'.\"\n  resolution_round: 32\n- id: v33-N2-BIMODAL\n  summary: \"5-seed 双峰弱化 Goodhart 核心叙事\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 33\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 33, reviewers: [1, 2], note: \"C2 changed to 'seed-dependent Goodhart effect'.\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: 两位 Reviewer 一致认为 3/5 seeds 95% CI [11.8%, 88.1%] 无信息量。seeds 45-46 post-hoc 添加进一步削弱。Existence proof 定位在 Limitations 有但正文叙述超越。R1 补充：multi-attractor dynamics 使增加 seeds 仍可能高方差。\"}\n- id: v33-W1-EXEC-POOLING\n  summary: \"Table 1 exec-only 仅报告 s42\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 33, reviewers: [1], note: \"§4.2 explains. Table 1 footnote expanded.\"}\n    - {round: 37, reviewers: [1], note: \"R37 minor issue: Table 1 exec-only 行仅 seed 42（脚注 †）与 3-seed pooled 行并列，易造成误读。建议行内标注 (single seed)。\"}\n- id: v33-M8-CONVERTS\n  summary: \"'ISR converts CE into TS' 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"'converts' → 'systematically selects for TS over CE'.\"\n  resolution_round: 33\n- id: v33-W3-TAXONOMY\n  summary: \"Taxonomy 互斥性和 N-H upper bound 未在正文说明\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 33\n  resolution: \"Priority rule and N-H upper bound added to §3.3.\"\n  resolution_round: 33\n- id: v31-R2-MR-SPECGAMING\n  summary: \"缺失引用：Nishimura et al. 2026 spec gaming\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"Citation added.\"\n  resolution_round: 31\n- id: v31-R2-W-TITLE-LENGTH\n  summary: \"标题过长\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 32\n  resolution: \"Title shortened.\"\n  resolution_round: 32\n- id: v31-R2-ISR0-AMBIGUITY\n  summary: \"ISR=0 语义不同\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 31\n  last_seen_round: 31\n  resolution: \"ISR=0 disambiguation added.\"\n  resolution_round: 31\n- id: v32-R12-MR-UNFAITHFUL-COT\n  summary: \"缺失引用：Lanham/Turpin\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  resolution: \"Both citations added.\"\n  resolution_round: 32\n- id: v34-R12-N1\n  summary: \"C3 贡献声称 overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"C3 establishing→confirming(Prolog)+exploratory(ProofFOL)。\"\n  resolution_round: 34\n- id: v34-R12-N2\n  summary: \"ISR scalar framing 张力\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex L54 ISR screening trigger 定位句。\"\n  resolution_round: 34\n- id: v34-R1-N1\n  summary: \"3-5 seeds proportion claim CI 宽\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 37\n  mentions:\n    - {round: 36, reviewers: [1, 2], note: \"R36 W1: CI 已展示，'can occur' framing 正确。新增 optional stopping concern → limitations 加 post-hoc 声明。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 fresh review: 两位 Reviewer 再次一致标记为 critical。根本问题（仅 5 seeds）未变，framing 修复不足以消解。\"}\n- id: v34-R1-N2\n  summary: \"Seed 43 sensitivity 可见性不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"正文 L65 N=2 统计句。\"\n  resolution_round: 34\n- id: v34-R1-N3\n  summary: \"Table 5 pooled Fisher 缺 descriptive-only 限定\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"Appendix Table 5 caption 增加限定 + CMH 引用。\"\n  resolution_round: 34\n- id: v34-R12-W1\n  summary: \"Table 1 caption 过长\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"150 词→48 词。\"\n  resolution_round: 34\n- id: v34-R1-W3\n  summary: \"convergence 因果 claim 过强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 34, reviewers: [1], note: \"experiments.tex + conclusion.tex 两处同步弱化。\"}\n    - {round: 37, reviewers: [1], note: \"R37 R1-W3: 8B 不收敛仍被解读为 'degeneration requires convergence'，但 8B 配置与 4B 存在混淆变量。应降级为 correlational observation。\"}\n- id: v34-R2-W3\n  summary: \"正文信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 37\n  resolution: \"\"\n  mentions:\n    - {round: 34, reviewers: [2], note: \"§4.4 开头 exploratory signposting。\"}\n    - {round: 37, reviewers: [1, 2], note: \"R37 R2-W3 + R1-W2: Abstract 信息过载（~187 words 内塞入过多细节），observe-vs-optimize asymmetry 被淹没。标题泛化措辞与实验范围不匹配。\"}\n- id: v34-R2-W5\n  summary: \"Abstract [anonymized] 脚注\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"已移除。\"\n  resolution_round: 34\n- id: v34-R1-W5\n  summary: \"ISR = Shapley 声称缺推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 35\n  resolution: \"R35: 正文改为 'maximal coalition restriction'。\"\n  resolution_round: 35\n- id: v34-REVIEWER-FIG2\n  summary: \"Figure 2 未被正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"method.tex 两处引用。\"\n  resolution_round: 34\n- id: v34-REVIEWER-CONCL\n  summary: \"conclusion.tex confirm 对 ProofFOL 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  resolution: \"ProofFOL 标注 exploratory。\"\n  resolution_round: 34\n- id: v35-R1-M1\n  summary: \"Exec-only 条件仅 1 seed (s42) 完整报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"R35: experiments.tex L35 加 3-seed 1000-step 证据句。\"\n  resolution_round: 35\n- id: v35-R1-M3\n  summary: \"Premise-count confound 对 compositional evidence 未隔离\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"R35: Discussion 加 confound 承认句。R36: 整合为 open question。\"\n  resolution_round: 35\n- id: v35-R2-W2\n  summary: \"缺少与 PRM 的 Goodhart susceptibility 对比讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"R35: Discussion 安全 framing。R36: 整合为 open question。\"\n  resolution_round: 35\n- id: v35-R2-W4\n  summary: \"ISR/ISR* 术语使用不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"功能性 PASS。method.tex L56 'throughout' 约定 + 数值处均用 ISR*。\"\n  resolution_round: 35\n- id: v35-R2-MR1\n  summary: \"缺失引用：Krakovna et al. (2020)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 35\n  last_seen_round: 35\n  resolution: \"Related Work 加引用。\"\n  resolution_round: 35\n- id: v36-R12-N2\n  summary: \"Section 1 'any verifiable proxy' 从极窄实验范围过度推广\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 36\n  resolution: \"R36 修复：intro L27 改为 'LOO-based structural proxies---and plausibly other component-necessity measures---face analogous exploitation risks in neurosymbolic settings'。三层限定 + hedge。Reviewer 验证 PASS。\"\n  resolution_round: 36\n- id: v36-R12-W1\n  summary: \"缺少代码和数据可用性声明\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 36\n  resolution: \"R36 修复：Limitations 末尾加 'Code, training scripts, and evaluation data will be released upon acceptance.' Reviewer 验证 PASS。\"\n  resolution_round: 36\n- id: v36-R2-W2\n  summary: \"Shuffled-ISR 非收敛替代解释未讨论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 36\n  resolution: \"R36 修复：experiments L56 'confirms' → 'consistent with' + 显式承认 non-convergence confound。Reviewer 验证 PASS。\"\n  resolution_round: 36\n- id: v36-R2-W4\n  summary: \"Hacking taxonomy 5/8 modes 可靠性存疑\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 36\n  resolution: \"R36 修复：method L97 'CE and TS are robust; remaining five modes are configuration-specific observations'。Reviewer 验证 PASS。\"\n  resolution_round: 36\n- id: v37-R2-W1\n  summary: \"Observe-vs-optimize 理论解释偏浅，缺 LOO 特异性讨论和修复方案\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - {round: 37, reviewers: [1, 2], note: \"R2 提出，R1 同意。缺少：(a) LOO 特有 vs 所有 structural diagnostic 共性？(b) full Shapley 是否免疫？(c) 修复 ISR（如 tautology pre-filter + ISR）的讨论。\"}\n- id: v37-R2-W4\n  summary: \"C1-C3 contribution 独立性值得商榷\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - {round: 37, reviewers: [1, 2], note: \"R2 建议合并为 2 个 contributions；R1 反驳，认为三个对不同读者群有独立价值。轻微分歧，不影响接收。\"}"
  }
}
```

</details>

---


### Tool result

_source line 3355 · 2026-05-25T21:35:41.416278+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 13905}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3356 · 2026-05-25T21:38:31.888048+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 37 (Fresh Review)\n\n**论文**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（全新审稿，无历史记忆）\n**Reviewer**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性 + Related Work + 格式）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，通过 leave-one-out (LOO) 消融测试 GRPO 训练的神经符号推理模型中每个形式化组件是否对证明成功必要，由此定义 Intensional Structural Reward (ISR)。论文发现：(1) ISR 作为事后诊断有效揭示了执行奖励下的结构退化（prove rate 上升而 ISR 崩溃）；(2) 将 ISR 作为训练奖励触发 seed-dependent 的 Goodhart 效应（3/5 seeds 收敛至 gaming）；(3) 该效应跨逻辑类型（FOL/Prolog）复现，跨数据集（ProofFOL）证据为 exploratory。\n\n---\n\n## Strengths\n\n**S1** [共识] 研究问题极具时效性和重要性：在 RLVR 和 neurosymbolic reasoning 交叉领域揭示 Goodhart 效应，对正在部署这类系统的研究者有直接价值。\n\n**S2** [共识] 实验设计系统且严谨：六种 reward conditions（exec-only, ISR β=0.1/0.3, Random β=0.1/0.3, SFT）加 Shuffled-ISR 解混淆控制，matched random controls 和 shuffled-ISR 形成 well-controlled 对比框架。控制变量比同类工作更充分。\n\n**S3** [共识] Hacking taxonomy 有独立贡献价值：8 种 structural degeneration 模式的系统分类（CE, TSa, TSb, PG, Tautological, Repetition, Contradiction, Query-as-fact）为后续研究提供了可参考的分类框架。\n\n**S4** [共识] Composition shift 证据有力：TS composition shift（χ²=174.8, p<10⁻³⁸）是论文最强的统计结果，清楚展示了 ISR reward 如何改变 hacking 的类型。\n\n**S5** [共识] 诚实的科学自我批评：premise-count confound 的 1.06× 结果被正面呈现而非隐藏，ProofFOL p=0.10 被标为 exploratory，ISR 的 paradoxical position 被坦诚讨论。\n\n**S6** [共识] Cross-logic replication (FOL→Prolog)：三条独立 gaming pathway（clean TS, degenerate syntax, query-as-fact）展示了 Goodhart 效应在不同逻辑体系中以不同机制复现。\n\n**S7** [共识] 可复现性良好：匿名代码仓库（anonymous.4open.science），完整超参数表（Table 4），Algorithm 1 伪代码清晰，per-seed 详细结果（Tables 9-12）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [共识, critical] **3-5 seeds 的样本量不足以支撑论文的概率性 claims**\n\n两位 Reviewer 一致标记为最严重问题。核心 Goodhart claim 基于 5 个 seeds 中 3 个出现 gaming（60%），95% Clopper-Pearson CI 为 [11.8%, 88.1%]，无法与随机（50%）可靠区分。Seeds 45-46 是 post-hoc 添加的（§4.1），进一步削弱统计推断。论文在 Limitations 中自称 \"existence demonstration\"，但正文叙述（§4.2 \"3 of 5 seeds converge to gaming\"、§5 的泛化论述）超越了 existence proof。\n\nR1 补充：论文展示了 multi-attractor dynamics（不同 seeds 收敛到不同 hacking modes），即使增加到 10-15 seeds 仍可能呈现高方差。论文应讨论需要多少 seeds 才能可靠估计 Goodhart 概率。\n\n- 修复要求：增加 seed 数量（建议 ≥15），或将正文叙述全面降级为 existence demonstration（非仅 Limitations 一句）。\n\n**MF2** [共识, critical] **ISR 标量诊断价值在 premise-count 控制后消失，核心贡献定位不清**\n\n214× raw ISR collapse 在 premise-count matched comparison 后仅为 1.06×（McNemar p=0.317, n.s., §4.2）。ISR 标量本身无法区分 exec-only 和 ISR-trained models。论文随后转向 \"compositional evidence survives this control\"，但这实际是 hacking mode classification（CE/TS 文本匹配）在做诊断工作，而非 ISR 本身。当前 framing 在 Abstract 和 Introduction 中仍以 ISR 标量为中心叙事（\"ISR reveals that prove-rate gains conceal...\"），与实验结果不匹配。\n\nR2 补充：论文 §3.2 确实已引入 mode classification，§4.2 主叙事也围绕 mode breakdown——问题出在 framing 而非 soundness。\n\n- 修复要求：明确区分 STA-as-procedure（生成 LOO ablation data）和 ISR-as-scalar（汇总分数），承认后者诊断价值有限。重写 Abstract/Introduction 中以 ISR 标量为中心的叙述，转向以 mode decomposition 为核心。\n\n**MF3** [共识, critical] **ISR-as-reward Goodhart 效应的统计支撑仅限于 compositional shift，非整体恶化**\n\nISR vs Random non-hacking rate: 6.06% vs 9.5%，Fisher p=0.182 (n.s., Table 6)。论文无法在统计上证明 ISR-as-reward 导致了比 random reward 更多的总体 gaming。TS composition shift（p < 10⁻³⁸）成立，但这是 type 差异而非 amount 差异。标题 \"Observe but Don't Optimize\" 和当前叙述暗示 ISR 优化恶化了整体结果。\n\nR2 补充：regressional Goodhart（Manheim & Garrabrant 2019）的定义本身就是 compositional shift，因此 Goodhart claim 在 regressional 框架下逻辑成立。但需要明确标注。\n\n- 修复要求：将 Goodhart claim 明确限定为 \"compositional/regressional Goodhart\"（改变 hacking 类型但不增加总量），在 Abstract 和 Discussion 中反映这一区分。\n\n**MF4** [R2 Must-Fix, R1 Should-Fix, 分歧] **单一模型族限制可推广性**\n\n所有主实验基于 Qwen3-4B。8B 结果极初步且动力学不同。标题使用 \"Neurosymbolic Reasoning\"（泛化）而实验仅覆盖 Qwen3-4B + FOLIO（具体）。\n\nR1 反驳降级为 Should-Fix：论文已有 cross-logic（FOL/Prolog, 不同 solver）和 cross-dataset（FOLIO/ProofFOL）泛化证据。核心 claim 关于 ISR/LOO metric 的结构性缺陷，不依赖于特定模型。\n\n- 修复要求（折中）：标题和 Abstract 加入 model-specific 限定语；讨论中承认 cross-model 泛化是关键 open question。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [共识] **Seed 43 评估协议不一致**：s43 使用 T=0.7 nucleus sampling 而非 greedy decoding（§4.1 脚注），对 Random β=0.1 TS rate 影响大（s43: 38.3%, s42/s44: 0%）。N=2 sensitivity analysis 放 Appendix 但主表用 3-seed pooled 数据。建议主文 pooled 分析基于 protocol 一致的 seeds，或更显著标记 s43 差异。\n\n**SF2** [共识] **标题和 Abstract 概括性超出实验范围**：仅测试一种 structural reward (ISR)、一个模型 (Qwen3-4B)、一个主基准 (FOLIO)。Abstract ~187 words 内塞入过多技术细节，核心 message (observe-vs-optimize asymmetry) 被淹没。\n\n**SF3** [共识] **Observe-vs-optimize 理论解释偏浅**：归因于 \"tautological formalizations satisfy necessity criterion by construction\" 是正确但表层的观察。缺失讨论：(a) 这是 LOO 特有还是所有 structural diagnostic 的共性？(b) Full Shapley value 是否也会被 game？(c) 修复 ISR 的可能性（如 tautology pre-filter + ISR）。\n\n**SF4** [R1] **Qwen3-8B 非收敛的因果解读存在混淆变量**：8B 配置与 4B 存在差异，不收敛可能是超参数未充分调优。\"degeneration requires convergence\" 应降级为 correlational observation。\n\n**SF5** [共识] **ProofFOL \"dataset-dependent asymmetry\" 解释是 post-hoc 的**：p=0.10 的结果仍提取了 \"ISR reward effectively corrective\" 的实质性结论。应标记为 hypothesis generation 而非 confirmation。（注：R2 初审误认为 ProofFOL 缺少 ISR 实验，R1 在交叉回应中纠正——§4.3 和 Table 12 包含 ProofFOL ISR β=0.1 结果。）\n\n**SF6** [共识] **Hacking mode classifier recall 未知**：Precision=100% (152 samples)，但 recall 未知。TSb 的发现（12 个 obfuscated tautologies 仅通过人工检查发现）说明 subtle modes 被遗漏。non-hacking rate 应一致标记为 \"≤6%\" 而非 \"6%\"。\n\n**SF7** [R2] **C1-C3 contribution 独立性值得商榷**：C1 和 C2 紧密耦合，C3 是 C2 的扩展。R1 反驳认为三者对不同读者群有独立价值。轻微分歧。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 达成共识的关键问题：\n\n1. **[AGREE] 3-5 seeds 统计效力不足** — 最严重问题，两位 Reviewer 一致\n2. **[AGREE] ISR 标量 framing 需从标量转向 mode taxonomy** — R1 提出，R2 同意\n3. **[AGREE] Goodhart claim 应限定为 compositional** — R1 提出，R2 同意（with nuance: regressional Goodhart 框架下逻辑成立但需明确标注）\n4. **[AGREE] 标题/Abstract 过度概括** — 两位一致\n5. **[AGREE] Seed 43 评估不一致** — 两位一致\n6. **[AGREE] Classifier recall 未知** — 两位一致\n7. **[AGREE] 理论解释偏浅** — R2 提出，R1 同意并补充 full Shapley 讨论缺失\n\n## Reviewer Divergence\n\n1. **单一模型族**：R2 标记为 Must-Fix（需增加非 Qwen 模型），R1 反驳为 Should-Fix（cross-logic/cross-dataset 已提供泛化证据，核心 claim 关于 metric 缺陷不依赖模型）。折中处理：标题/Abstract 加限定语 + 讨论中承认 cross-model 泛化为 open question。\n2. **C1-C3 合并**：R2 建议合并为 2 个 contributions，R1 认为三者对不同受众有独立价值。轻微分歧，不影响评分。\n3. **ProofFOL 实验完整性**：R2 初审误认为 ProofFOL 缺少 ISR 实验（实际存在于 §4.3 和 Table 12），R1 在交叉回应中纠正。R2 在 cross-response 中未明确承认此纠正，但将 W2 的 framing 调整为\"post-hoc 解释\"而非\"缺少实验\"。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R1] STA 的核心价值是 ISR 标量还是 LOO ablation 产生的 per-component data？如果是后者，论文叙事结构是否需要调整？\n\n**Q2** [R1] Seed 43 的 \"greedy-mode degeneration\" 具体表现是什么？这个现象本身是否与 reward hacking 相关？\n\n**Q3** [R1+R2] 如果增加到 15-20 seeds，预期 gaming 率稳定在什么水平？是否有初步结果？\n\n**Q4** [R1] Shuffled-ISR 的低 PR (15%) 是否是 hacking 减少的混淆因素？低 PR 意味着更少 proved samples 进入 hacking 分析。\n\n**Q5** [R2] 是否尝试过在 ISR reward 中加入 tautological detection filter（检测 conclusion embedding 后排除 ISR=1 的 tautological case）以修复 ISR 的 gameable blind spot？\n\n**Q6** [R2] STA 的 n+1 solver call overhead 在实际部署中是否 prohibitive？是否有近似版本（如 sampling-based LOO）？\n\n---\n\n## Missing References\n\n1. Chen, T.Y., Kuo, F.C., Liu, H., et al. (2018). \"Metamorphic Testing: A Review of Challenges and Opportunities.\" *ACM Computing Surveys* 51(1) — LOO ablation 与 metamorphic testing 的概念联系 [R2 建议]\n2. Wang et al. (2026) \"Reward Hacking in the Era of Large Models\" (arXiv:2604.13602) — 可能在 bib 中但未在正文显式引用 [R2 建议]\n\n---\n\n## External Review\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（0 critical, 2 warning, 6 info）：\n\n**Warnings:**\n- Page 18: 附录 D.1 节内容仅占页面约 1/3，下方约 2/3 为空白。建议合并排版或调整 float 位置。\n- Page 23: \"Use of AI Assistants\" 部分内容极短，约 55% 页面为空白。\n\n**Info:**\n- Page 6: Figure 4 堆叠条形图部分颜色段在小尺寸下区分度偏低，色盲读者可能受影响。建议增加 hatching pattern。\n- Pages 19-20: Tables 9-12 的 Notes 列字号偏小（~6-7pt），打印时可能难以辨读。\n- Page 14: 单页含 Tables 6/7/8 三个表格，密度高但可接受。\n- Page 4: Figure 2 全宽概念图颜色体系与后续统计图一致。\n- Page 5: Table 1 主结果表格式规范（booktabs, 最优值加粗）。\n- Page 7: 单页含 Figure 5 + Table 2 + Table 3，密度高但排版未溢出。\n\n---\n\n## Overall Assessment\n\n**综合评分: 3.0 / 5 — Findings**\n\n**置信度: 4 / 5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3 | 3.5 | 3 |\n| Excitement | 3.5 | 3 | 3 |\n| Reproducibility | 4 | 4 | 4 |\n\n**评分理由**：\n\n两位 Reviewer 独立给出 3.5 (Borderline Conference)，但交叉分享后在所有关键问题上达成高度共识，暴露出比单独评估更清晰的整体图景：\n\n1. **证据基础偏窄**：核心 Goodhart claim 的三个关键统计检验均不显著或效力不足——ISR 标量 1.06× (p=0.317)、非 hacking 率差异 (p=0.182)、3/5 seed CI [11.8%, 88.1%]。论文最强的证据是 TS composition shift (p<10⁻³⁸)，但这支撑的是一个范围更窄的 claim（compositional Goodhart 而非整体 Goodhart）。\n\n2. **Framing 与证据不匹配**：标题、Abstract 和 Introduction 的叙述范围显著超出实验证据——\"Structural Rewards\"（仅测试 ISR）、\"Neurosymbolic Reasoning\"（仅 Qwen3-4B + FOLIO）、ISR 标量为核心叙事（实际诊断价值来自 mode classification）。多个已被标记为 \"resolved\" 的历史 issue（ISR framing、ProofFOL overclaim、seed count framing）在 fresh review 中被重新提出，说明先前的 framing 修复未能从根本上解决问题。\n\n3. **核心贡献仍有价值**：hacking taxonomy（8 modes 分类）、compositional Goodhart 的实证机制（tautological shortcuts 满足 LOO necessity by construction）、cross-logic replication（FOL/Prolog 三条独立 gaming pathway）均为 solid contributions——但其范围是 Findings 级别的 focused empirical study，而非 Conference 级别的 general-audience paper。\n\n**接收条件**（升至 Borderline Conference / Conference）：\n- 增加 seed 数量至 ≥15 或将正文叙述全面降级为 existence demonstration\n- 重写 framing：核心贡献从 ISR 标量转向 STA procedure + mode taxonomy\n- 将 Goodhart claim 明确限定为 compositional/regressional\n- 标题和 Abstract 加入 model/dataset-specific 限定语\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- ~187 words，符合 ≤200 限制 ✓\n- 信息密度过高，核心 message (observe-vs-optimize asymmetry) 被技术细节淹没\n- \"ISR reveals that prove-rate gains conceal...\" — ISR 标量本身不是有效诊断（1.06× n.s.），需转向 mode decomposition 叙事\n- \"3 of 5 seeds converge to gaming\" — CI 过宽，应使用 \"can occur\" 等 existence 措辞\n\n### §1 Introduction\n- C1/C2/C3 三个 contribution 清晰列出\n- C1 的叙述仍以 ISR 为中心，应重新定位为 STA procedure + mode taxonomy\n- \"structural proxies for formalization integrity are easier to observe than to optimize\" — 这个 tagline 有效但需更强的理论支撑\n\n### §2 Related Work\n- 覆盖全面：57 篇引用涵盖 neurosymbolic reasoning、reward hacking/Goodhart、reward design/structural diagnostics\n- 与 Kim et al. (2026) 的区分清晰（inference-time vs training-time）✓\n- 与 concurrent RLVR 文献的区分基本清晰，可更明确说明 STA vs IPT 的优劣势\n- 可能遗漏：Chen et al. (2018) metamorphic testing 概念联系、Wang et al. (2026) reward hacking survey 正文显式引用\n\n### §3 Method\n- STA/ISR 定义清晰，Algorithm 1 伪代码简洁 ✓\n- LOO independence assumption 被坦诚讨论 ✓\n- ISR = Shapley maximal coalition restriction 的联系适当 ✓\n- 六种 reward conditions 设计合理，控制变量充分 ✓\n- Hacking taxonomy 八种模式定义清晰，优先级规则 (PG > CE > TS) 已说明 ✓\n\n### §4 Experiments\n- §4.1 Setup: 超参数详尽，s43 例外在脚注中标注（应更显著）\n- §4.2 ISR as Diagnostic: ISR collapse trajectory 有效；premise-count confound 的 1.06× 诚实呈现但削弱 ISR 标量价值；mode breakdown 是真正的诊断工具\n- §4.3 Goodhart Effects: TS composition shift (p<10⁻³⁸) 有力；但 non-hacking rate 差异 n.s. (p=0.182)；seed-dependent 结果有趣但 5 seeds 不足\n- §4.4 Cross-Domain: Prolog replication 有效；ProofFOL 结果为 exploratory (p=0.10)，\"hacking geometry\" 解释是 post-hoc；8B 非收敛的因果解读需弱化\n- §4.5 Hacking Taxonomy: Table 3 的分类有独立参考价值\n\n### §5 Discussion and Conclusion\n- 五条 practical guidelines 总体合理，但 Guideline 4 (\"expect CE as GRPO-universal baseline\") \"universal\" 用词偏强\n- \"the diagnostic—optimization asymmetry persists across logic types and dataset families\" — ProofFOL 上未验证 optimization 失败（已在交叉分享中由 R1 纠正：§4.3 Table 12 包含 ProofFOL ISR β=0.1 结果，但 p=0.10 underpowered），措辞仍偏强\n\n### Limitations\n- 三个点（单模型、小数据集、ISR ≠ semantic faithfulness），符合 EMNLP 要求 ✓\n- 遗漏：STA 的 n+1 solver call 计算开销；hacking taxonomy 完整性\n\n### 格式合规\n- 正文 ≤ 8 页 ✓ | Abstract ≤ 200 words ✓ | ACL [review] 模板 ✓\n- 匿名化完整 ✓ | Limitations 在正文 ✓ | 参考文献格式一致 ✓\n- AI assistants 声明 ✓ | Double-blind 合规 ✓",
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
    "report": "# 审稿报告 — Round 37 (Fresh Review)\n\n**论文**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（全新审稿，无历史记忆）\n**Reviewer**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性 + Related Work + 格式）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，通过 leave-one-out (LOO) 消融测试 GRPO 训练的神经符号推理模型中每个形式化组件是否对证明成功必要，由此定义 Intensional Structural Reward (ISR)。论文发现：(1) ISR 作为事后诊断有效揭示了执行奖励下的结构退化（prove rate 上升而 ISR 崩溃）；(2) 将 ISR 作为训练奖励触发 seed-dependent 的 Goodhart 效应（3/5 seeds 收敛至 gaming）；(3) 该效应跨逻辑类型（FOL/Prolog）复现，跨数据集（ProofFOL）证据为 exploratory。\n\n---\n\n## Strengths\n\n**S1** [共识] 研究问题极具时效性和重要性：在 RLVR 和 neurosymbolic reasoning 交叉领域揭示 Goodhart 效应，对正在部署这类系统的研究者有直接价值。\n\n**S2** [共识] 实验设计系统且严谨：六种 reward conditions（exec-only, ISR β=0.1/0.3, Random β=0.1/0.3, SFT）加 Shuffled-ISR 解混淆控制，matched random controls 和 shuffled-ISR 形成 well-controlled 对比框架。控制变量比同类工作更充分。\n\n**S3** [共识] Hacking taxonomy 有独立贡献价值：8 种 structural degeneration 模式的系统分类（CE, TSa, TSb, PG, Tautological, Repetition, Contradiction, Query-as-fact）为后续研究提供了可参考的分类框架。\n\n**S4** [共识] Composition shift 证据有力：TS composition shift（χ²=174.8, p<10⁻³⁸）是论文最强的统计结果，清楚展示了 ISR reward 如何改变 hacking 的类型。\n\n**S5** [共识] 诚实的科学自我批评：premise-count confound 的 1.06× 结果被正面呈现而非隐藏，ProofFOL p=0.10 被标为 exploratory，ISR 的 paradoxical position 被坦诚讨论。\n\n**S6** [共识] Cross-logic replication (FOL→Prolog)：三条独立 gaming pathway（clean TS, degenerate syntax, query-as-fact）展示了 Goodhart 效应在不同逻辑体系中以不同机制复现。\n\n**S7** [共识] 可复现性良好：匿名代码仓库（anonymous.4open.science），完整超参数表（Table 4），Algorithm 1 伪代码清晰，per-seed 详细结果（Tables 9-12）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [共识, critical] **3-5 seeds 的样本量不足以支撑论文的概率性 claims**\n\n两位 Reviewer 一致标记为最严重问题。核心 Goodhart claim 基于 5 个 seeds 中 3 个出现 gaming（60%），95% Clopper-Pearson CI 为 [11.8%, 88.1%]，无法与随机（50%）可靠区分。Seeds 45-46 是 post-hoc 添加的（§4.1），进一步削弱统计推断。论文在 Limitations 中自称 \"existence demonstration\"，但正文叙述（§4.2 \"3 of 5 seeds converge to gaming\"、§5 的泛化论述）超越了 existence proof。\n\nR1 补充：论文展示了 multi-attractor dynamics（不同 seeds 收敛到不同 hacking modes），即使增加到 10-15 seeds 仍可能呈现高方差。论文应讨论需要多少 seeds 才能可靠估计 Goodhart 概率。\n\n- 修复要求：增加 seed 数量（建议 ≥15），或将正文叙述全面降级为 existence demonstration（非仅 Limitations 一句）。\n\n**MF2** [共识, critical] **ISR 标量诊断价值在 premise-count 控制后消失，核心贡献定位不清**\n\n214× raw ISR collapse 在 premise-count matched comparison 后仅为 1.06×（McNemar p=0.317, n.s., §4.2）。ISR 标量本身无法区分 exec-only 和 ISR-trained models。论文随后转向 \"compositional evidence survives this control\"，但这实际是 hacking mode classification（CE/TS 文本匹配）在做诊断工作，而非 ISR 本身。当前 framing 在 Abstract 和 Introduction 中仍以 ISR 标量为中心叙事（\"ISR reveals that prove-rate gains conceal...\"），与实验结果不匹配。\n\nR2 补充：论文 §3.2 确实已引入 mode classification，§4.2 主叙事也围绕 mode breakdown——问题出在 framing 而非 soundness。\n\n- 修复要求：明确区分 STA-as-procedure（生成 LOO ablation data）和 ISR-as-scalar（汇总分数），承认后者诊断价值有限。重写 Abstract/Introduction 中以 ISR 标量为中心的叙述，转向以 mode decomposition 为核心。\n\n**MF3** [共识, critical] **ISR-as-reward Goodhart 效应的统计支撑仅限于 compositional shift，非整体恶化**\n\nISR vs Random non-hacking rate: 6.06% vs 9.5%，Fisher p=0.182 (n.s., Table 6)。论文无法在统计上证明 ISR-as-reward 导致了比 random reward 更多的总体 gaming。TS composition shift（p < 10⁻³⁸）成立，但这是 type 差异而非 amount 差异。标题 \"Observe but Don't Optimize\" 和当前叙述暗示 ISR 优化恶化了整体结果。\n\nR2 补充：regressional Goodhart（Manheim & Garrabrant 2019）的定义本身就是 compositional shift，因此 Goodhart claim 在 regressional 框架下逻辑成立。但需要明确标注。\n\n- 修复要求：将 Goodhart claim 明确限定为 \"compositional/regressional Goodhart\"（改变 hacking 类型但不增加总量），在 Abstract 和 Discussion 中反映这一区分。\n\n**MF4** [R2 Must-Fix, R1 Should-Fix, 分歧] **单一模型族限制可推广性**\n\n所有主实验基于 Qwen3-4B。8B 结果极初步且动力学不同。标题使用 \"Neurosymbolic Reasoning\"（泛化）而实验仅覆盖 Qwen3-4B + FOLIO（具体）。\n\nR1 反驳降级为 Should-Fix：论文已有 cross-logic（FOL/Prolog, 不同 solver）和 cross-dataset（FOLIO/ProofFOL）泛化证据。核心 claim 关于 ISR/LOO metric 的结构性缺陷，不依赖于特定模型。\n\n- 修复要求（折中）：标题和 Abstract 加入 model-specific 限定语；讨论中承认 cross-model 泛化是关键 open question。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [共识] **Seed 43 评估协议不一致**：s43 使用 T=0.7 nucleus sampling 而非 greedy decoding（§4.1 脚注），对 Random β=0.1 TS rate 影响大（s43: 38.3%, s42/s44: 0%）。N=2 sensitivity analysis 放 Appendix 但主表用 3-seed pooled 数据。建议主文 pooled 分析基于 protocol 一致的 seeds，或更显著标记 s43 差异。\n\n**SF2** [共识] **标题和 Abstract 概括性超出实验范围**：仅测试一种 structural reward (ISR)、一个模型 (Qwen3-4B)、一个主基准 (FOLIO)。Abstract ~187 words 内塞入过多技术细节，核心 message (observe-vs-optimize asymmetry) 被淹没。\n\n**SF3** [共识] **Observe-vs-optimize 理论解释偏浅**：归因于 \"tautological formalizations satisfy necessity criterion by construction\" 是正确但表层的观察。缺失讨论：(a) 这是 LOO 特有还是所有 structural diagnostic 的共性？(b) Full Shapley value 是否也会被 game？(c) 修复 ISR 的可能性（如 tautology pre-filter + ISR）。\n\n**SF4** [R1] **Qwen3-8B 非收敛的因果解读存在混淆变量**：8B 配置与 4B 存在差异，不收敛可能是超参数未充分调优。\"degeneration requires convergence\" 应降级为 correlational observation。\n\n**SF5** [共识] **ProofFOL \"dataset-dependent asymmetry\" 解释是 post-hoc 的**：p=0.10 的结果仍提取了 \"ISR reward effectively corrective\" 的实质性结论。应标记为 hypothesis generation 而非 confirmation。（注：R2 初审误认为 ProofFOL 缺少 ISR 实验，R1 在交叉回应中纠正——§4.3 和 Table 12 包含 ProofFOL ISR β=0.1 结果。）\n\n**SF6** [共识] **Hacking mode classifier recall 未知**：Precision=100% (152 samples)，但 recall 未知。TSb 的发现（12 个 obfuscated tautologies 仅通过人工检查发现）说明 subtle modes 被遗漏。non-hacking rate 应一致标记为 \"≤6%\" 而非 \"6%\"。\n\n**SF7** [R2] **C1-C3 contribution 独立性值得商榷**：C1 和 C2 紧密耦合，C3 是 C2 的扩展。R1 反驳认为三者对不同读者群有独立价值。轻微分歧。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 达成共识的关键问题：\n\n1. **[AGREE] 3-5 seeds 统计效力不足** — 最严重问题，两位 Reviewer 一致\n2. **[AGREE] ISR 标量 framing 需从标量转向 mode taxonomy** — R1 提出，R2 同意\n3. **[AGREE] Goodhart claim 应限定为 compositional** — R1 提出，R2 同意（with nuance: regressional Goodhart 框架下逻辑成立但需明确标注）\n4. **[AGREE] 标题/Abstract 过度概括** — 两位一致\n5. **[AGREE] Seed 43 评估不一致** — 两位一致\n6. **[AGREE] Classifier recall 未知** — 两位一致\n7. **[AGREE] 理论解释偏浅** — R2 提出，R1 同意并补充 full Shapley 讨论缺失\n\n## Reviewer Divergence\n\n1. **单一模型族**：R2 标记为 Must-Fix（需增加非 Qwen 模型），R1 反驳为 Should-Fix（cross-logic/cross-dataset 已提供泛化证据，核心 claim 关于 metric 缺陷不依赖模型）。折中处理：标题/Abstract 加限定语 + 讨论中承认 cross-model 泛化为 open question。\n2. **C1-C3 合并**：R2 建议合并为 2 个 contributions，R1 认为三者对不同受众有独立价值。轻微分歧，不影响评分。\n3. **ProofFOL 实验完整性**：R2 初审误认为 ProofFOL 缺少 ISR 实验（实际存在于 §4.3 和 Table 12），R1 在交叉回应中纠正。R2 在 cross-response 中未明确承认此纠正，但将 W2 的 framing 调整为\"post-hoc 解释\"而非\"缺少实验\"。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R1] STA 的核心价值是 ISR 标量还是 LOO ablation 产生的 per-component data？如果是后者，论文叙事结构是否需要调整？\n\n**Q2** [R1] Seed 43 的 \"greedy-mode degeneration\" 具体表现是什么？这个现象本身是否与 reward hacking 相关？\n\n**Q3** [R1+R2] 如果增加到 15-20 seeds，预期 gaming 率稳定在什么水平？是否有初步结果？\n\n**Q4** [R1] Shuffled-ISR 的低 PR (15%) 是否是 hacking 减少的混淆因素？低 PR 意味着更少 proved samples 进入 hacking 分析。\n\n**Q5** [R2] 是否尝试过在 ISR reward 中加入 tautological detection filter（检测 conclusion embedding 后排除 ISR=1 的 tautological case）以修复 ISR 的 gameable blind spot？\n\n**Q6** [R2] STA 的 n+1 solver call overhead 在实际部署中是否 prohibitive？是否有近似版本（如 sampling-based LOO）？\n\n---\n\n## Missing References\n\n1. Chen, T.Y., Kuo, F.C., Liu, H., et al. (2018). \"Metamorphic Testing: A Review of Challenges and Opportunities.\" *ACM Computing Surveys* 51(1) — LOO ablation 与 metamorphic testing 的概念联系 [R2 建议]\n2. Wang et al. (2026) \"Reward Hacking in the Era of Large Models\" (arXiv:2604.13602) — 可能在 bib 中但未在正文显式引用 [R2 建议]\n\n---\n\n## External Review\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（0 critical, 2 warning, 6 info）：\n\n**Warnings:**\n- Page 18: 附录 D.1 节内容仅占页面约 1/3，下方约 2/3 为空白。建议合并排版或调整 float 位置。\n- Page 23: \"Use of AI Assistants\" 部分内容极短，约 55% 页面为空白。\n\n**Info:**\n- Page 6: Figure 4 堆叠条形图部分颜色段在小尺寸下区分度偏低，色盲读者可能受影响。建议增加 hatching pattern。\n- Pages 19-20: Tables 9-12 的 Notes 列字号偏小（~6-7pt），打印时可能难以辨读。\n- Page 14: 单页含 Tables 6/7/8 三个表格，密度高但可接受。\n- Page 4: Figure 2 全宽概念图颜色体系与后续统计图一致。\n- Page 5: Table 1 主结果表格式规范（booktabs, 最优值加粗）。\n- Page 7: 单页含 Figure 5 + Table 2 + Table 3，密度高但排版未溢出。\n\n---\n\n## Overall Assessment\n\n**综合评分: 3.0 / 5 — Findings**\n\n**置信度: 4 / 5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3 | 3.5 | 3 |\n| Excitement | 3.5 | 3 | 3 |\n| Reproducibility | 4 | 4 | 4 |\n\n**评分理由**：\n\n两位 Reviewer 独立给出 3.5 (Borderline Conference)，但交叉分享后在所有关键问题上达成高度共识，暴露出比单独评估更清晰的整体图景：\n\n1. **证据基础偏窄**：核心 Goodhart claim 的三个关键统计检验均不显著或效力不足——ISR 标量 1.06× (p=0.317)、非 hacking 率差异 (p=0.182)、3/5 seed CI [11.8%, 88.1%]。论文最强的证据是 TS composition shift (p<10⁻³⁸)，但这支撑的是一个范围更窄的 claim（compositional Goodhart 而非整体 Goodhart）。\n\n2. **Framing 与证据不匹配**：标题、Abstract 和 Introduction 的叙述范围显著超出实验证据——\"Structural Rewards\"（仅测试 ISR）、\"Neurosymbolic Reasoning\"（仅 Qwen3-4B + FOLIO）、ISR 标量为核心叙事（实际诊断价值来自 mode classification）。多个已被标记为 \"resolved\" 的历史 issue（ISR framing、ProofFOL overclaim、seed count framing）在 fresh review 中被重新提出，说明先前的 framing 修复未能从根本上解决问题。\n\n3. **核心贡献仍有价值**：hacking taxonomy（8 modes 分类）、compositional Goodhart 的实证机制（tautological shortcuts 满足 LOO necessity by construction）、cross-logic replication（FOL/Prolog 三条独立 gaming pathway）均为 solid contributions——但其范围是 Findings 级别的 focused empirical study，而非 Conference 级别的 general-audience paper。\n\n**接收条件**（升至 Borderline Conference / Conference）：\n- 增加 seed 数量至 ≥15 或将正文叙述全面降级为 existence demonstration\n- 重写 framing：核心贡献从 ISR 标量转向 STA procedure + mode taxonomy\n- 将 Goodhart claim 明确限定为 compositional/regressional\n- 标题和 Abstract 加入 model/dataset-specific 限定语\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- ~187 words，符合 ≤200 限制 ✓\n- 信息密度过高，核心 message (observe-vs-optimize asymmetry) 被技术细节淹没\n- \"ISR reveals that prove-rate gains conceal...\" — ISR 标量本身不是有效诊断（1.06× n.s.），需转向 mode decomposition 叙事\n- \"3 of 5 seeds converge to gaming\" — CI 过宽，应使用 \"can occur\" 等 existence 措辞\n\n### §1 Introduction\n- C1/C2/C3 三个 contribution 清晰列出\n- C1 的叙述仍以 ISR 为中心，应重新定位为 STA procedure + mode taxonomy\n- \"structural proxies for formalization integrity are easier to observe than to optimize\" — 这个 tagline 有效但需更强的理论支撑\n\n### §2 Related Work\n- 覆盖全面：57 篇引用涵盖 neurosymbolic reasoning、reward hacking/Goodhart、reward design/structural diagnostics\n- 与 Kim et al. (2026) 的区分清晰（inference-time vs training-time）✓\n- 与 concurrent RLVR 文献的区分基本清晰，可更明确说明 STA vs IPT 的优劣势\n- 可能遗漏：Chen et al. (2018) metamorphic testing 概念联系、Wang et al. (2026) reward hacking survey 正文显式引用\n\n### §3 Method\n- STA/ISR 定义清晰，Algorithm 1 伪代码简洁 ✓\n- LOO independence assumption 被坦诚讨论 ✓\n- ISR = Shapley maximal coalition restriction 的联系适当 ✓\n- 六种 reward conditions 设计合理，控制变量充分 ✓\n- Hacking taxonomy 八种模式定义清晰，优先级规则 (PG > CE > TS) 已说明 ✓\n\n### §4 Experiments\n- §4.1 Setup: 超参数详尽，s43 例外在脚注中标注（应更显著）\n- §4.2 ISR as Diagnostic: ISR collapse trajectory 有效；premise-count confound 的 1.06× 诚实呈现但削弱 ISR 标量价值；mode breakdown 是真正的诊断工具\n- §4.3 Goodhart Effects: TS composition shift (p<10⁻³⁸) 有力；但 non-hacking rate 差异 n.s. (p=0.182)；seed-dependent 结果有趣但 5 seeds 不足\n- §4.4 Cross-Domain: Prolog replication 有效；ProofFOL 结果为 exploratory (p=0.10)，\"hacking geometry\" 解释是 post-hoc；8B 非收敛的因果解读需弱化\n- §4.5 Hacking Taxonomy: Table 3 的分类有独立参考价值\n\n### §5 Discussion and Conclusion\n- 五条 practical guidelines 总体合理，但 Guideline 4 (\"expect CE as GRPO-universal baseline\") \"universal\" 用词偏强\n- \"the diagnostic—optimization asymmetry persists across logic types and dataset families\" — ProofFOL 上未验证 optimization 失败（已在交叉分享中由 R1 纠正：§4.3 Table 12 包含 ProofFOL ISR β=0.1 结果，但 p=0.10 underpowered），措辞仍偏强\n\n### Limitations\n- 三个点（单模型、小数据集、ISR ≠ semantic faithfulness），符合 EMNLP 要求 ✓\n- 遗漏：STA 的 n+1 solver call 计算开销；hacking taxonomy 完整性\n\n### 格式合规\n- 正文 ≤ 8 页 ✓ | Abstract ≤ 200 words ✓ | ACL [review] 模板 ✓\n- 匿名化完整 ✓ | Limitations 在正文 ✓ | 参考文献格式一致 ✓\n- AI assistants 声明 ✓ | Double-blind 合规 ✓",
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

_source line 3357 · 2026-05-25T21:38:36.053283+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4165
}
```

</details>

---


### Assistant

_source line 3358 · 2026-05-25T21:38:51.040679+00:00_

审稿报告已投递。

---

**Round 37 审稿完成。** 总结：

**综合评分：3.0 / 5 — Findings**

两位 Reviewer 均给出 3.5 (Borderline Conference)，交叉分享后在所有关键问题上达成高度共识。综合评分降至 3.0 (Findings)，原因：

**4 个 Must-Fix 问题：**
1. 3-5 seeds 统计效力不足（CI [11.8%, 88.1%]，无信息量）
2. ISR 标量诊断价值在 premise-count 控制后消失（1.06×, p=0.317）
3. Goodhart claim 仅由 compositional shift 支撑（non-hacking 率差异 p=0.182 n.s.）
4. 单一模型族限制泛化性（R1/R2 对严重程度有分歧）

**核心优势：** 实验设计系统严谨、hacking taxonomy 有独立贡献、TS composition shift 统计有力（p<10⁻³⁸）、cross-logic replication 增强说服力、学术诚实度高。

**升级条件：** 增加 seeds ≥15 + 重写 framing（ISR 标量→mode taxonomy）+ 限定 Goodhart 为 compositional + 标题/Abstract 加 model-specific 限定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 302

## Round 302

2 recorded events


### User

_source line 3359 · 2026-05-25T21:38:53.608979+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

对 R1 的 8 个问题（N1-N3, W1-W5）逐条给出了判断：
- **7 个 AGREE**（其中 N2 和 W3 附带 nuance）
- **0 个 REBUT**

两位 Reviewer 的主要共识：seed 数量不足是最严重问题；单一模型族限制泛化；ISR framing 需从标量转向 STA procedure。R1 在 premise-count confound (N1) 和 classifier recall (W5) 方面的分析比我初审更深入，我已明确认可这些补充发现。维持总评 3.5/5。

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

_source line 3360 · 2026-05-25T21:39:08.472193+00:00_

审稿报告已投递完成。

**Round 37 审稿总结**：

- **综合评分**：3.0 / 5（Findings）
- **R1**：3.5 (Borderline Conference) | **R2**：3.5 (Borderline Conference)
- 交叉分享后高度共识（R2 对 R1 的 8 个问题中 7 个 AGREE，0 个 REBUT；R1 对 R2 的 6 个问题中 3 个 AGREE、3 个 REBUT）

**4 个 Must-Fix**：
1. 3-5 seeds 统计效力不足（两位一致）
2. ISR 标量 framing 需从标量转向 STA procedure + mode taxonomy
3. Goodhart claim 应限定为 compositional/regressional（非整体恶化）
4. 单一模型族泛化性（R2 Must-Fix / R1 Should-Fix，折中处理）

**7 个 Should-Fix**：Seed 43 协议不一致、标题/Abstract overclaim、理论解释偏浅、8B 因果解读、ProofFOL post-hoc、classifier recall 未知、C1-C3 独立性

报告已投递至 Research Director，Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---
