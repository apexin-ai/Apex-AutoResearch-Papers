# Director coordination — Part 2 of 7

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/0d/0d5b5d57f8a45f2c2330.json)

## Round 31

### Tool call

_source line 315 · 2026-05-19T08:39:23.669068+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "issues:\n# === Round 4 Critical Issues (fresh review) ===\n\n- id: \"R4-N1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正式论证和 sensitivity analysis\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 首次提出，R2 交叉 AGREE。±2pp 仅一句话论证，缺 ±1pp/±1.5pp/±3pp 下的 p 值梯度表和 smallest equivalence margin。直接动摇 Contribution #1。\"\n  action_items:\n    - round: 4\n      action: \"报告 TOST 在 ±1pp, ±1.5pp, ±2pp, ±3pp 下的 p 值；报告 smallest margin at which equivalence holds；增加 deployment cost model 论证\"\n      assigned_to: \"paper+agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N2\"\n  summary: \"'Controlled comparison' 声称与实际设计存在系统性裂隙（checkpoint/seq_length/preprocessing/TRAJ regime）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 首次逐项拆解，R2 交叉 AGREE 并补充定量证据。四项 confound: (a) CLS val-best vs CWM final epoch; (b) Qwen3 CWM eval 8192 vs DeepSeek 4096; (c) s42 drop vs s123 truncate preprocessing; (d) TRAJ lr/data/eval granularity 不同。R2 补充：preprocessing 对 CLS degradation 有 3× 影响。\"\n  action_items:\n    - round: 4\n      action: \"Title 从 'Controlled' 改为 'Systematic'；增加 'Threats to Internal Validity' 段落；尝试修复 CWM NaN validation loss 或报告 CWM 多 epoch checkpoint sensitivity\"\n      assigned_to: \"paper+agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N3\"\n  summary: \"Repo-level n=48 variant-level 统计效力严重不足，缺 CI 和 power analysis\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两人独立发现并交叉 AGREE。n=48 下 SE≈5.8pp, 95% CI 宽±11.3pp。CLS 两 seed 差 8.33pp（4 个 variant）。TRAJ 6-seed std=5pp。variant-level 结论对 seed 极度敏感。Contribution #2 的 framing 远强于证据。\"\n  action_items:\n    - round: 4\n      action: \"为所有 variant-level 比较增加 bootstrap CI；进行 power analysis；将 variant-level 结论标记为 preliminary；降低 Contribution #2 语气\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 4 Should-Fix Issues ===\n\n- id: \"R4-W1\"\n  summary: \"CWM baseline external validity 严重受限但仍做 formulation-level 归因\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W2 和 R2-W4 独立提出，交叉 mutual AGREE。4-8B LoRA ≠ 32B mid-trained CWM。正文用 'generation formulation' / 'output space complexity' 做归因，但 4B→8B 仅 2× scale。R2 补充：repo-level CWM format collapse 可能是 capacity 问题而非 formulation-inherent。\"\n  action_items:\n    - round: 4\n      action: \"全文 CWM 结论加 'at ≤8B LoRA scale' qualifier；Limitations 讨论 32B mid-training 可能改变结论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌（~250 words, 15+ 数字）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W1 首次提出，R1 交叉 AGREE 并清点：15+ 个数值。违反写作规范（最多 2-3 个关键数字）。\"\n  action_items:\n    - round: 4\n      action: \"精简至 150-180 词，保留 2-3 关键数字，其余用定性描述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 'validation' 措辞过强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W4 首次提出，R2 交叉 AGREE。n=2 model families 不构成 'validation'，至多 'consistency check' 或 'directional evidence'。\"\n  action_items:\n    - round: 4\n      action: \"将 'Cross-model validation' 改为 'Cross-model consistency' 或 'directional evidence'；降低 Contribution #2 中的语气\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"新颖性定位：'design space' 仅 3 个离散点，缺深层机制洞察\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-N1 首次提出，R1 交叉部分 AGREE（保留 failure mode taxonomy 增量价值）。标题 'Design Space' overselling；function-level equivalence 较预期；repo-level 分析归结为 '生成长输出更难'。与 process vs outcome supervision 文献增量不明确。R1 建议 novelty 定位为 'empirical methodology contribution'。\"\n  action_items:\n    - round: 4\n      action: \"调整标题（去掉 'Design Space' 或改为 'Formulation Comparison'）；在 Introduction 中更明确论证相对 PRM/ORM 文献的具体增量\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"多重比较问题未处理\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W1 首次提出，R2 交叉 AGREE。论文以统计严谨性为卖点但未做多重比较校正。\"\n  action_items:\n    - round: 4\n      action: \"区分 primary vs exploratory comparisons；对 primary comparisons 应用 Holm correction 或报告 adjusted p 值\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"合成数据（mutation-based）外部效度讨论不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W2 首次提出，R1 交叉 AGREE。Limitations 仅一句话。应讨论 mutation vs real bug 分布差异对 formulation ranking 的可能影响。\"\n  action_items:\n    - round: 4\n      action: \"Limitations 扩展 synthetic-to-real transfer 讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W7\"\n  summary: \"Error complementarity / ICC oracle analysis 的适用范围未限定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W5 首次提出，R2 交叉 AGREE 并补充：repo-level CWM format collapse 使错误互补性不成立。function-level ICC=0.191 用于 repo-level oracle analysis 的 transfer 未论证。\"\n  action_items:\n    - round: 4\n      action: \"Table 6 增加 repo-level ICC=0.3146 列；明确 error complementarity 仅适用于 function-level\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏近期直接相关工作（CodePRM, FunPRM 等）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W3 首次提出，R1 交叉部分 AGREE（CodePRM/FunPRM 应引用；CodeScaler/CodeRL+ 相关性需确认）。另缺 constrained decoding 方法论文献。\"\n  action_items:\n    - round: 4\n      action: \"补充 CodePRM, FunPRM 引用；验证 CodeScaler/CodeRL+ 相关性后酌情补充；补充 constrained decoding 引用\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 4 Minor Issues ===\n\n- id: \"R4-M1\"\n  summary: \"Table 3 格式不统一（'/' 分隔 vs 单值）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-M1 提出，R2 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M2\"\n  summary: \"CWM unparseable default-to-pass 的方向性影响应在正文讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-M3 提出，R2 AGREE。default-to-pass 使 CWM accuracy 包含大量'猜对'成分。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M3\"\n  summary: \"'Matched seeds' 实际 preprocessing 不匹配，措辞误导\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2 在交叉回应 R1-M4 时发现。s42 和 s123 preprocessing/checkpoint 不同，不应称 'matched seeds'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M4\"\n  summary: \"NF4 vs bf16 precision mixing 未在正文说明原因\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2-M3 提出，R1 AGREE。Appendix 有 robustness check 但应提升到正文。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M5\"\n  summary: \"Figure 2 信息密度（分歧点，R1 认为有叙事功能，R2 认为偏低）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-M2 提出，R1 REBUT（认为有叙事功能）。轻度分歧。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M6\"\n  summary: \"'CWM stagnation' 措辞偏强\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-M5 提出，R1 AGREE。建议改为 'plateau' 或 'flat scaling'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M7\"\n  summary: \"Table 1 caption LLM-as-judge vs TRAJ 概念关系需澄清\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Previous Rounds — Tracked Issues ===\n\n- id: \"R3-N1\"\n  summary: \"TRAJ 训练数据量差异 175×（~400 vs ~70K）破坏 controlled comparison 框架\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 首次提出。Abstract 'identical data' 构成 overclaim。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 AGREE。数据不对称是 formulation-inherent。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"本轮未作为独立 issue 提出但被 R4-N2(d) TRAJ regime 差异覆盖。Abstract 已改为 'same source data with formulation-appropriate label granularity'。Downsample ablation 已完成。TRAJ lr 差异仍未控制。\"\n  action_items:\n    - round: 3\n      action: \"写作: Abstract 'identical data' → 'same source data with formulation-appropriate granularity'\"\n      assigned_to: \"paper\"\n      status: in_progress\n    - round: 3\n      action: \"实验: Downsample CLS function-level 15290→8052 (匹配 TRAJ)，重训+eval TOST\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Repo-level 统计效力严重不足，多数配置仅 1-2 seeds\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现。seed variance 可达 7.68pp。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N3 再次独立提出。问题持续存在。R2 补充定量 SE 分析（≈5.8pp）。\"\n  action_items:\n    - round: 3\n      action: \"写作: 弱化 'formulation-inherent' → 'observed consistently across both model families'\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"NaN validation loss 导致 checkpoint 选择策略跨配置不一致\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"DeepSeek s123 + CWM runs 用 final epoch，其余用 val-best。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N2(a) 再次提出。R2 补充：NaN loss 本身反映 CWM 训练稳定性问题，应作为 CWM inherent weakness 讨论。\"\n  action_items:\n    - round: 3\n      action: \"实验: Eval Qwen3-8B CLS ckpt-6633 (final epoch) 做 val-best vs final ablation\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"CWM 4-8B LoRA 结论不能外推为 generation formulation 的普遍判断\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"4-8B LoRA ≠ 32B mid-trained CWM。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-W1 再次独立提出。问题持续存在。\"\n  action_items:\n    - round: 3\n      action: \"写作: 全文 CWM 结论加 'at 4-8B LoRA scale' qualifier\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"Limitations 不是独立 section，有 desk reject 风险\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"30秒 LaTeX 修复。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未被提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 3\n      action: \"\\\\paragraph → \\\\section*{Limitations}\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Abstract 数据密度过高\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"211 词，数字太多。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-W2 再次独立提出。R1 清点 15+ 数字。问题持续存在，可能更严重。\"\n  action_items:\n    - round: 3\n      action: \"精简至 150-180 词，保留 2-3 关键数字\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"'No single formulation dominates' framing 与证据不符\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"CLS ≥ 所有条件。framing 与证据不符。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未被直接提及。当前 framing 已调整为 'CLS achieves the highest...aggregation penalty makes advantage configuration-dependent'，但 R4-W4 (novelty) 建议进一步调整。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"CWM 跨模型 eval seq_length 不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen3 8192 vs DeepSeek 4096。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N2(b) 再次提出。问题持续。\"\n  action_items:\n    - round: 3\n      action: \"强化 caveat 位置; Qwen3-8B CWM @4096 eval 正在运行\"\n      assigned_to: \"paper+agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"TOST ±2pp margin sensitivity 主文披露不足\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"±1pp→不等价, ±2pp→等价。margin-sensitive。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N1 升级为 critical。问题持续且被强化。\"\n  action_items:\n    - round: 3\n      action: \"主文增加 sensitivity 结果 + margin 选择 rationale\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Previous Rounds — Resolved Issues (保持记录) ===\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CWM 8B 完成。Round 2 确认 resolved。\"\n  resolution_round: 2\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"rank-32 消融完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Title changed.\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正当性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"TOST sensitivity table 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Relaxed matching 反降准确率。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"人工突变 vs 真实 bug ecological validity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Limitations 增加讨论。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"遗漏 LEVER 和 CodeT\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已添加。\"\n  resolution_round: 1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "issues:\n# === Round 4 Critical Issues (fresh review) ===\n\n- id: \"R4-N1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正式论证和 sensitivity analysis\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 首次提出，R2 交叉 AGREE。±2pp 仅一句话论证，缺 ±1pp/±1.5pp/±3pp 下的 p 值梯度表和 smallest equivalence margin。直接动摇 Contribution #1。\"\n  action_items:\n    - round: 4\n      action: \"报告 TOST 在 ±1pp, ±1.5pp, ±2pp, ±3pp 下的 p 值；报告 smallest margin at which equivalence holds；增加 deployment cost model 论证\"\n      assigned_to: \"paper+agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N2\"\n  summary: \"'Controlled comparison' 声称与实际设计存在系统性裂隙（checkpoint/seq_length/preprocessing/TRAJ regime）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 首次逐项拆解，R2 交叉 AGREE 并补充定量证据。四项 confound: (a) CLS val-best vs CWM final epoch; (b) Qwen3 CWM eval 8192 vs DeepSeek 4096; (c) s42 drop vs s123 truncate preprocessing; (d) TRAJ lr/data/eval granularity 不同。R2 补充：preprocessing 对 CLS degradation 有 3× 影响。\"\n  action_items:\n    - round: 4\n      action: \"Title 从 'Controlled' 改为 'Systematic'；增加 'Threats to Internal Validity' 段落；尝试修复 CWM NaN validation loss 或报告 CWM 多 epoch checkpoint sensitivity\"\n      assigned_to: \"paper+agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N3\"\n  summary: \"Repo-level n=48 variant-level 统计效力严重不足，缺 CI 和 power analysis\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两人独立发现并交叉 AGREE。n=48 下 SE≈5.8pp, 95% CI 宽±11.3pp。CLS 两 seed 差 8.33pp（4 个 variant）。TRAJ 6-seed std=5pp。variant-level 结论对 seed 极度敏感。Contribution #2 的 framing 远强于证据。\"\n  action_items:\n    - round: 4\n      action: \"为所有 variant-level 比较增加 bootstrap CI；进行 power analysis；将 variant-level 结论标记为 preliminary；降低 Contribution #2 语气\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 4 Should-Fix Issues ===\n\n- id: \"R4-W1\"\n  summary: \"CWM baseline external validity 严重受限但仍做 formulation-level 归因\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W2 和 R2-W4 独立提出，交叉 mutual AGREE。4-8B LoRA ≠ 32B mid-trained CWM。正文用 'generation formulation' / 'output space complexity' 做归因，但 4B→8B 仅 2× scale。R2 补充：repo-level CWM format collapse 可能是 capacity 问题而非 formulation-inherent。\"\n  action_items:\n    - round: 4\n      action: \"全文 CWM 结论加 'at ≤8B LoRA scale' qualifier；Limitations 讨论 32B mid-training 可能改变结论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌（~250 words, 15+ 数字）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W1 首次提出，R1 交叉 AGREE 并清点：15+ 个数值。违反写作规范（最多 2-3 个关键数字）。\"\n  action_items:\n    - round: 4\n      action: \"精简至 150-180 词，保留 2-3 关键数字，其余用定性描述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 'validation' 措辞过强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W4 首次提出，R2 交叉 AGREE。n=2 model families 不构成 'validation'，至多 'consistency check' 或 'directional evidence'。\"\n  action_items:\n    - round: 4\n      action: \"将 'Cross-model validation' 改为 'Cross-model consistency' 或 'directional evidence'；降低 Contribution #2 中的语气\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"新颖性定位：'design space' 仅 3 个离散点，缺深层机制洞察\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-N1 首次提出，R1 交叉部分 AGREE（保留 failure mode taxonomy 增量价值）。标题 'Design Space' overselling；function-level equivalence 较预期；repo-level 分析归结为 '生成长输出更难'。与 process vs outcome supervision 文献增量不明确。R1 建议 novelty 定位为 'empirical methodology contribution'。\"\n  action_items:\n    - round: 4\n      action: \"调整标题（去掉 'Design Space' 或改为 'Formulation Comparison'）；在 Introduction 中更明确论证相对 PRM/ORM 文献的具体增量\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"多重比较问题未处理\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W1 首次提出，R2 交叉 AGREE。论文以统计严谨性为卖点但未做多重比较校正。\"\n  action_items:\n    - round: 4\n      action: \"区分 primary vs exploratory comparisons；对 primary comparisons 应用 Holm correction 或报告 adjusted p 值\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"合成数据（mutation-based）外部效度讨论不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W2 首次提出，R1 交叉 AGREE。Limitations 仅一句话。应讨论 mutation vs real bug 分布差异对 formulation ranking 的可能影响。\"\n  action_items:\n    - round: 4\n      action: \"Limitations 扩展 synthetic-to-real transfer 讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W7\"\n  summary: \"Error complementarity / ICC oracle analysis 的适用范围未限定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W5 首次提出，R2 交叉 AGREE 并补充：repo-level CWM format collapse 使错误互补性不成立。function-level ICC=0.191 用于 repo-level oracle analysis 的 transfer 未论证。\"\n  action_items:\n    - round: 4\n      action: \"Table 6 增加 repo-level ICC=0.3146 列；明确 error complementarity 仅适用于 function-level\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏近期直接相关工作（CodePRM, FunPRM 等）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W3 首次提出，R1 交叉部分 AGREE（CodePRM/FunPRM 应引用；CodeScaler/CodeRL+ 相关性需确认）。另缺 constrained decoding 方法论文献。\"\n  action_items:\n    - round: 4\n      action: \"补充 CodePRM, FunPRM 引用；验证 CodeScaler/CodeRL+ 相关性后酌情补充；补充 constrained decoding 引用\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 4 Minor Issues ===\n\n- id: \"R4-M1\"\n  summary: \"Table 3 格式不统一（'/' 分隔 vs 单值）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-M1 提出，R2 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M2\"\n  summary: \"CWM unparseable default-to-pass 的方向性影响应在正文讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-M3 提出，R2 AGREE。default-to-pass 使 CWM accuracy 包含大量'猜对'成分。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M3\"\n  summary: \"'Matched seeds' 实际 preprocessing 不匹配，措辞误导\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2 在交叉回应 R1-M4 时发现。s42 和 s123 preprocessing/checkpoint 不同，不应称 'matched seeds'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M4\"\n  summary: \"NF4 vs bf16 precision mixing 未在正文说明原因\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2-M3 提出，R1 AGREE。Appendix 有 robustness check 但应提升到正文。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M5\"\n  summary: \"Figure 2 信息密度（分歧点，R1 认为有叙事功能，R2 认为偏低）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-M2 提出，R1 REBUT（认为有叙事功能）。轻度分歧。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M6\"\n  summary: \"'CWM stagnation' 措辞偏强\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-M5 提出，R1 AGREE。建议改为 'plateau' 或 'flat scaling'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-M7\"\n  summary: \"Table 1 caption LLM-as-judge vs TRAJ 概念关系需澄清\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Previous Rounds — Tracked Issues ===\n\n- id: \"R3-N1\"\n  summary: \"TRAJ 训练数据量差异 175×（~400 vs ~70K）破坏 controlled comparison 框架\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 首次提出。Abstract 'identical data' 构成 overclaim。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 AGREE。数据不对称是 formulation-inherent。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"本轮未作为独立 issue 提出但被 R4-N2(d) TRAJ regime 差异覆盖。Abstract 已改为 'same source data with formulation-appropriate label granularity'。Downsample ablation 已完成。TRAJ lr 差异仍未控制。\"\n  action_items:\n    - round: 3\n      action: \"写作: Abstract 'identical data' → 'same source data with formulation-appropriate granularity'\"\n      assigned_to: \"paper\"\n      status: in_progress\n    - round: 3\n      action: \"实验: Downsample CLS function-level 15290→8052 (匹配 TRAJ)，重训+eval TOST\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Repo-level 统计效力严重不足，多数配置仅 1-2 seeds\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现。seed variance 可达 7.68pp。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N3 再次独立提出。问题持续存在。R2 补充定量 SE 分析（≈5.8pp）。\"\n  action_items:\n    - round: 3\n      action: \"写作: 弱化 'formulation-inherent' → 'observed consistently across both model families'\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"NaN validation loss 导致 checkpoint 选择策略跨配置不一致\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"DeepSeek s123 + CWM runs 用 final epoch，其余用 val-best。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N2(a) 再次提出。R2 补充：NaN loss 本身反映 CWM 训练稳定性问题，应作为 CWM inherent weakness 讨论。\"\n  action_items:\n    - round: 3\n      action: \"实验: Eval Qwen3-8B CLS ckpt-6633 (final epoch) 做 val-best vs final ablation\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"CWM 4-8B LoRA 结论不能外推为 generation formulation 的普遍判断\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"4-8B LoRA ≠ 32B mid-trained CWM。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-W1 再次独立提出。问题持续存在。\"\n  action_items:\n    - round: 3\n      action: \"写作: 全文 CWM 结论加 'at 4-8B LoRA scale' qualifier\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"Limitations 不是独立 section，有 desk reject 风险\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"30秒 LaTeX 修复。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未被提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 3\n      action: \"\\\\paragraph → \\\\section*{Limitations}\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Abstract 数据密度过高\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"211 词，数字太多。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-W2 再次独立提出。R1 清点 15+ 数字。问题持续存在，可能更严重。\"\n  action_items:\n    - round: 3\n      action: \"精简至 150-180 词，保留 2-3 关键数字\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"'No single formulation dominates' framing 与证据不符\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"CLS ≥ 所有条件。framing 与证据不符。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未被直接提及。当前 framing 已调整为 'CLS achieves the highest...aggregation penalty makes advantage configuration-dependent'，但 R4-W4 (novelty) 建议进一步调整。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"CWM 跨模型 eval seq_length 不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen3 8192 vs DeepSeek 4096。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N2(b) 再次提出。问题持续。\"\n  action_items:\n    - round: 3\n      action: \"强化 caveat 位置; Qwen3-8B CWM @4096 eval 正在运行\"\n      assigned_to: \"paper+agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"TOST ±2pp margin sensitivity 主文披露不足\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"±1pp→不等价, ±2pp→等价。margin-sensitive。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N1 升级为 critical。问题持续且被强化。\"\n  action_items:\n    - round: 3\n      action: \"主文增加 sensitivity 结果 + margin 选择 rationale\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Previous Rounds — Resolved Issues (保持记录) ===\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CWM 8B 完成。Round 2 确认 resolved。\"\n  resolution_round: 2\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"rank-32 消融完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Title changed.\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正当性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"TOST sensitivity table 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Relaxed matching 反降准确率。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"人工突变 vs 真实 bug ecological validity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Limitations 增加讨论。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"遗漏 LEVER 和 CodeT\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已添加。\"\n  resolution_round: 1"
  }
}
```

</details>

---


### Tool result

_source line 316 · 2026-05-19T08:39:23.770574+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 16154}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 317 · 2026-05-19T08:41:32.415123+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\"\n**目标 Venue**: EMNLP 2026 via ARR (deadline: 2026-05-25)\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n**圆桌轮次**: 1 轮（Round 1 + 交叉分享后达成共识）\n\n---\n\n## Summary\n\n本文对 execution-free code verification 的三种 formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹级评分）进行了系统比较，覆盖两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（function-level、repo-level）和多 seed。核心发现：function-level 三者统计等价（TOST p=0.007, ±2pp）；repo-level CLS 大幅优于 CWM（19–26pp gap）；error complementarity 支持 ensemble。研究设计有野心，统计方法（TOST、clustered bootstrap、ICC）在 NLP 经验论文中属于高水平；但 \"controlled comparison\" 的执行在 repo-level 有多个系统性缺陷，新颖性定位偏高于实际贡献深度。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且清晰。** 验证 pipeline 中的 formulation 选择是实际工程决策，无先前工作提供 head-to-head 比较。论文填补了一个真实空白。[R1, R2 共识]\n\n**S2. 多维度实验设计。** 覆盖 formulation(3) × model family(2) × model size(2) × complexity(2) × seeds(up to 5)，比该领域典型论文更系统。[R1, R2 共识]\n\n**S3. 统计方法规范。** TOST 用于 null-result claim（而非仅 \"无显著差异\"）、clustered bootstrap 处理 within-problem 依赖、ICC 量化相关结构——方法选择均正确。[R1, R2 共识]\n\n**S4. Failure mode taxonomy 有洞察力。** Table 4 区分 format collapse / decision collapse / aggregation penalty，且展示同一模型在不同 configuration 下触发不同模式（DeepSeek s42 vs s123），是非平凡发现。[R1 强调, R2 认同]\n\n**S5. 消融设计全面。** LoRA rank、序列长度 matched-context、训练数据 downsampling、few-shot baselines、relaxed matching——系统性地排除了常见替代解释。[R1, R2 共识]\n\n**S6. Limitations 诚实。** 论文在正文和 Appendix 中主动披露了几乎所有方法论弱点（单 seed、NaN loss、eval seq_length 不一致等）。[R1 特别提及]\n\n---\n\n## Weaknesses\n\n### Critical（Must-Fix，影响接收决定）\n\n**C1. TOST ±2pp equivalence margin 缺乏正式论证和 sensitivity analysis** [R1-N1, R2 AGREE]\n\n§4.4 的 ±2pp margin 仅以一句话论证（\"unlikely to affect deployment decisions\"）。缺乏：(1) margin sensitivity 分析（±1pp/±1.5pp/±2pp/±3pp 下的 p 值梯度表）；(2) smallest equivalence margin 报告；(3) 基于 deployment cost model 的实质性论证。在 85–88% 的准确率范围内，2pp 不是小差异。如果 ±1pp 下 TOST 不成立，\"equivalence\" 需降级为 \"near-equivalence\"。直接动摇 Contribution #1 的基础。\n\n**C2. \"Controlled comparison\" 声称与实际设计存在系统性裂隙** [R1-N2, R2 AGREE]\n\n标题 \"Controlled Empirical Study\" 暗示所有变量被控制，实际仅控制了模型大小和训练数据来源。四项未控制的关键 confound：\n- (a) **Checkpoint selection**: CLS 使用 val-best；CWM/DeepSeek-s123 因 NaN validation loss 使用 final epoch。CLS 系统性获得更优 checkpoint。\n- (b) **Eval seq_length**: Qwen3 CWM 8192 vs DeepSeek CWM 4096。论文自己报告 ~9pp 的 seq_length variation，但 cross-model comparison 是核心论证策略。\n- (c) **Preprocessing**: s42 drop vs s123 truncate。Preprocessing 对 CLS degradation 有 ~3× 影响（4pp vs 12pp）。\n- (d) **TRAJ regime**: 不同 lr (2e-4 vs 5e-5)、不同训练集大小 (~400 vs ~70K)、不同评估粒度 (n=48 vs n=9784)。\n\n这些 confound 单独不致命（repo-level 19–26pp gap 足够大），但合在一起削弱 \"formulation-driven\" 的因果归因，且部分 confound 方向系统性偏向 CLS。\n\n**C3. Repo-level n=48 variant-level 统计效力严重不足** [R1-N3, R2-N2, mutual AGREE]\n\nn=48 下 SE ≈ 5.8pp，95% CI 宽 ±11.3pp。CLS Qwen3-8B 两 seed 差 8.33pp（72.92% vs 81.25%，仅 4 个 variant 翻转）。TRAJ DeepSeek 6-seed std = 5.00pp。variant-level 结论对 seed 极度敏感。论文混用 per-test (n=9784) 和 variant-level (n=48) 结果且未充分区分统计可靠性。Contribution #2 的 framing 远强于 variant-level 证据支撑。缺少 bootstrap CI 和 power analysis。\n\n### Warning（Should-Fix，影响评分）\n\n**W1. CWM baseline external validity 严重受限但仍做 formulation-level 归因** [R1-W2, R2-W4, mutual AGREE]\n\n4–8B LoRA fine-tuned CWM ≠ 32B execution-trace mid-trained CWM。正文使用 \"generation formulation\" / \"output space complexity\" 做归因，但 4B→8B 仅 2× scale，不足以推断 formulation-level 天花板。Repo-level CWM format collapse 可能是 capacity 问题而非 formulation-inherent。\n\n**W2. Abstract 数据堆砌** [R2-W1, R1 AGREE]\n\n~250 words 内 15+ 个数值，读起来像实验结果压缩而非叙事。违反写作规范（最多 2–3 关键数字）。\n\n**W3. Cross-model \"validation\" 措辞过强** [R1-W4, R2 AGREE]\n\nn=2 model families 不构成 \"validation\"，至多 \"consistency check\" 或 \"directional evidence\"。单 seed DeepSeek 数据高度不稳定（CLS 7.68pp spread）。\n\n**W4. 新颖性定位：\"design space\" 仅 3 个离散点** [R2-N1, R1 部分 AGREE]\n\n标题 \"Formulation Design Space\" overselling——3 个离散 formulation 不构成连续 space。Function-level equivalence 较预期；repo-level 分析归结为 \"生成长输出更难\"。与 process vs outcome supervision 文献增量不够明确。R1 认为 failure mode taxonomy 有增量价值（轻度分歧）。\n\n**W5. 多重比较问题未处理** [R1-W1, R2 AGREE]\n\n论文以统计严谨性为卖点但未区分 primary/exploratory comparisons，未应用任何多重比较校正。\n\n**W6. 合成数据外部效度讨论不足** [R2-W2, R1 AGREE]\n\nLimitations 仅一句话提及 synthetic-to-real transfer gap。对 formulation ranking 可能因训练数据来源而变化的风险未讨论。\n\n**W7. Error complementarity / ICC oracle analysis 适用范围未限定** [R1-W5, R2 AGREE]\n\nFunction-level ICC=0.191 用于 repo-level oracle analysis 的 transfer 未论证。Repo-level CWM format collapse 使错误互补性不成立（CWM variant-level 低于 majority baseline）。结论应限定为 function-level。\n\n**W8. Related Work 遗漏近期直接相关工作** [R2-W3, R1 部分 AGREE]\n\n缺失：CodePRM (ACL 2025 Findings)、FunPRM (2601.22249)。R1 另指出缺 constrained decoding 方法论文献。CodeScaler 和 CodeRL+ 的相关性需确认。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **TOST margin sensitivity**: ±2pp 论证不足，需 gradient table 和 smallest margin [C1]\n2. **\"Controlled\" framing gap**: 四项 confound 削弱因果归因，建议改 \"systematic\" [C2]\n3. **Repo-level statistical power**: n=48, single-seed, 缺 CI/power analysis [C3]\n4. **CWM external validity**: 4–8B LoRA 结论不可推广为 formulation-level [W1]\n5. **Abstract overloaded**: 15+ 数字，需精简至 2–3 [W2]\n6. **Cross-model \"validation\"**: 措辞过强，应降为 \"consistency check\" [W3]\n7. **Overall score**: 3.0 (Findings) [两人独立一致]\n\n## Reviewer Divergence [REBUT]\n\n仅有两项轻度分歧，均不影响结论：\n\n1. **Re-repair pilot 定位** — R1 认为不应暗示为 contribution；R2 指出它已正确放置在 Appendix 作为负面 pilot，定位恰当。**结论：R2 的 REBUT 成立，论文已正确处理。**\n\n2. **Novelty/Excitement 评分** — R1 给 3.5/5（认为 failure mode taxonomy 有增量价值），R2 给 2.5/5（认为深层机制洞察不足）。**结论：轻度分歧，不影响总分。novelty 定位为 \"empirical methodology contribution\" 比 \"design space exploration\" 更准确。**\n\n---\n\n## Questions（需作者回答）\n\n**Q1.** TOST 在 ±1pp margin 下是否仍然成立？请提供 ±1pp/±1.5pp/±2pp/±3pp 下的 p 值。[R1, R2 一致提问]\n\n**Q2.** 是否尝试过修复 CWM 的 NaN validation loss（如 gradient clipping、loss masking、更小 lr）？如果未尝试，是技术限制还是时间限制？[R1]\n\n**Q3.** CLS Qwen3-8B 两 seed variant-level 差异 8.33pp（72.92% vs 81.25%）。如何在同一 formulation 内如此大的 seed variance 下，仍将 formulation 间差异归因于 formulation choice？[R1, R2 一致关注]\n\n**Q4.** CWM parseable outputs 是否系统性偏向 harder instances？即 unparseable outputs 是否集中在简单 instances？[R1 独特提问]\n\n**Q5.** Oracle ensemble 90.63% 在其他 seeds 下是否稳定？repo-level 的 error complementarity 是否成立（考虑 CWM variant-level < majority baseline）？[R1, R2 一致关注]\n\n**Q6.** 如果改用 real bug data（非 mutation），formulation ranking 是否可能改变？[R2]\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 确认应补充：\n\n1. **CodePRM** (ACL 2025 Findings) — process-level verification in code generation [R2 提出, R1 AGREE]\n2. **FunPRM** (arxiv 2601.22249, 2026) — function-as-step PRM，与 TRAJ 直接相关 [R2 提出, R1 AGREE]\n3. **Constrained decoding 方法论** (如 Willard & Louf 2023) — §4.5 讨论了 constrained decoding 但未引用 [R1 提出]\n\n以下引用需确认相关性后酌情补充：\n4. **CodeScaler** (arxiv 2602.17684, 2026) [R2 提出, R1 要求确认相关性]\n5. **CodeRL+** (arxiv 2510.18471, 2025) [R2 提出, R1 要求确认相关性]\n6. **近年 mutation-real fault coupling meta-analysis** [R1 提出]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置）。跳过。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n**EMNLP 2026 ARR 评分标准**: 3 = Findings（可被 Findings 接收）\n\n**维度评分汇总**:\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Overall | 3.0 | 3.0 | 3.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合判断**:\n\n研究问题重要且实用，实验设计有野心（多 formulation × 多模型 × 多 seed × 多复杂度），统计方法在 NLP 经验论文中属于高水平。Function-level 分析扎实（5 seeds, proper TOST, bootstrap CI），failure mode taxonomy 有诊断价值。\n\n但承载最重要结论的 repo-level 分析在统计支撑上最薄弱：n=48 variant-level evaluation, 1–2 seeds, checkpoint selection asymmetry, eval protocol inconsistency。\"Controlled comparison\" 的 framing 与实际控制程度不匹配。新颖性受限于 3 个离散 formulation 点和较浅的机制分析（\"生成长输出更难\"）。论文的 Limitations 诚实地覆盖了大部分问题，但 Abstract/Contributions 的措辞未反映这些 caveats 的严重程度。\n\n**升级至 Conference (3.5+) 的路径**:\n1. 解决 C1：提供 TOST margin sensitivity gradient table\n2. 解决 C2：将 \"Controlled\" 改为 \"Systematic\"，增加 threats to validity 段落\n3. 解决 C3：为 variant-level 比较增加 bootstrap CI 和 power analysis，降低 claims 语气\n4. 解决 W1：全文 CWM 结论限定为 \"at ≤8B LoRA scale\"\n5. 解决 W2：Abstract 精简至 2–3 关键数字\n6. 解决 W4：调整标题，深化机制分析\n\n以上修改在截止日（2026-05-25）前技术上可行，但需要实质性的重写和可能的补充实验。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 15+ 数字，数据堆砌严重。应保留 function-level equivalence 和 repo-level gap 两个核心数字，其余定性描述。\n- \"same source data with formulation-appropriate label granularity\" 已改善了 Round 3 的 \"identical data\" overclaim，但仍需进一步精简。\n\n### Introduction\n- 叙事线清晰（背景→问题→不足→方法→贡献）。\n- Contribution #2 语气远强于 repo-level 证据。\"Complexity-dependent divergence with formulation × model interaction\" 应加 \"preliminary evidence suggests\" 或 \"initial results indicate\"。\n- 需更明确论证相对 process vs outcome supervision 文献的具体增量。\n\n### Method\n- Formulation 定义清晰、数学符号恰当。\n- Oracle Accuracy-Utility Framework (§3.3) 论证完整。\n- CWM unparseable default-to-pass 策略应在此处讨论方向性影响（当前仅在 Appendix）。\n\n### Experiments\n- Function-level (§4.2): 扎实，5 seeds, proper statistics。\n- Scaling (§4.3): \"matched seeds\" 措辞误导（s42 和 s123 preprocessing 不同）。\"CWM stagnation\" 应改为 \"plateau\" 或 \"flat scaling\"。\n- Per-test vs TRAJ equivalence (§4.4): 核心问题是 margin sensitivity。NF4 vs bf16 mixing 原因应在正文说明。\n- Repo-level (§4.5): 论文最重要也最薄弱的部分。CWM default-to-pass artifact 应在正文讨论。\"Cross-model validation\" → \"Cross-model consistency\"。CWM eval seq_length 差异的 caveat 应更突出。Table 3 建议拆分 per-test 和 variant-level。\n- Analysis (§4.6): Aggregation penalty 分析有价值。Checkpoint selection confound 是好发现。\n\n### Related Work\n- 结构合理（3 段按主题），但偏压缩。缺 CodePRM、FunPRM、constrained decoding 引用。对 PRM/ORM 文献的增量定位不够深入。\n\n### Conclusion\n- 基本准确但应反映 variant-level 结论的 preliminary 性质。\n- Limitations 段落内容全面但格式需确认是否为独立 section（ARR 要求）。\n\n### Appendix\n- 内容充实（A–I），ablation 设计合理。\n- Re-repair pilot (j) 作为负面结果正确放置。\n- Extended Limitations (F) 是 responsible 做法。\n\n### References\n- 38 篇引用，密度中等偏低。需补充 3–6 篇近期直接相关工作。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\"\n**目标 Venue**: EMNLP 2026 via ARR (deadline: 2026-05-25)\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n**圆桌轮次**: 1 轮（Round 1 + 交叉分享后达成共识）\n\n---\n\n## Summary\n\n本文对 execution-free code verification 的三种 formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹级评分）进行了系统比较，覆盖两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（function-level、repo-level）和多 seed。核心发现：function-level 三者统计等价（TOST p=0.007, ±2pp）；repo-level CLS 大幅优于 CWM（19–26pp gap）；error complementarity 支持 ensemble。研究设计有野心，统计方法（TOST、clustered bootstrap、ICC）在 NLP 经验论文中属于高水平；但 \"controlled comparison\" 的执行在 repo-level 有多个系统性缺陷，新颖性定位偏高于实际贡献深度。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且清晰。** 验证 pipeline 中的 formulation 选择是实际工程决策，无先前工作提供 head-to-head 比较。论文填补了一个真实空白。[R1, R2 共识]\n\n**S2. 多维度实验设计。** 覆盖 formulation(3) × model family(2) × model size(2) × complexity(2) × seeds(up to 5)，比该领域典型论文更系统。[R1, R2 共识]\n\n**S3. 统计方法规范。** TOST 用于 null-result claim（而非仅 \"无显著差异\"）、clustered bootstrap 处理 within-problem 依赖、ICC 量化相关结构——方法选择均正确。[R1, R2 共识]\n\n**S4. Failure mode taxonomy 有洞察力。** Table 4 区分 format collapse / decision collapse / aggregation penalty，且展示同一模型在不同 configuration 下触发不同模式（DeepSeek s42 vs s123），是非平凡发现。[R1 强调, R2 认同]\n\n**S5. 消融设计全面。** LoRA rank、序列长度 matched-context、训练数据 downsampling、few-shot baselines、relaxed matching——系统性地排除了常见替代解释。[R1, R2 共识]\n\n**S6. Limitations 诚实。** 论文在正文和 Appendix 中主动披露了几乎所有方法论弱点（单 seed、NaN loss、eval seq_length 不一致等）。[R1 特别提及]\n\n---\n\n## Weaknesses\n\n### Critical（Must-Fix，影响接收决定）\n\n**C1. TOST ±2pp equivalence margin 缺乏正式论证和 sensitivity analysis** [R1-N1, R2 AGREE]\n\n§4.4 的 ±2pp margin 仅以一句话论证（\"unlikely to affect deployment decisions\"）。缺乏：(1) margin sensitivity 分析（±1pp/±1.5pp/±2pp/±3pp 下的 p 值梯度表）；(2) smallest equivalence margin 报告；(3) 基于 deployment cost model 的实质性论证。在 85–88% 的准确率范围内，2pp 不是小差异。如果 ±1pp 下 TOST 不成立，\"equivalence\" 需降级为 \"near-equivalence\"。直接动摇 Contribution #1 的基础。\n\n**C2. \"Controlled comparison\" 声称与实际设计存在系统性裂隙** [R1-N2, R2 AGREE]\n\n标题 \"Controlled Empirical Study\" 暗示所有变量被控制，实际仅控制了模型大小和训练数据来源。四项未控制的关键 confound：\n- (a) **Checkpoint selection**: CLS 使用 val-best；CWM/DeepSeek-s123 因 NaN validation loss 使用 final epoch。CLS 系统性获得更优 checkpoint。\n- (b) **Eval seq_length**: Qwen3 CWM 8192 vs DeepSeek CWM 4096。论文自己报告 ~9pp 的 seq_length variation，但 cross-model comparison 是核心论证策略。\n- (c) **Preprocessing**: s42 drop vs s123 truncate。Preprocessing 对 CLS degradation 有 ~3× 影响（4pp vs 12pp）。\n- (d) **TRAJ regime**: 不同 lr (2e-4 vs 5e-5)、不同训练集大小 (~400 vs ~70K)、不同评估粒度 (n=48 vs n=9784)。\n\n这些 confound 单独不致命（repo-level 19–26pp gap 足够大），但合在一起削弱 \"formulation-driven\" 的因果归因，且部分 confound 方向系统性偏向 CLS。\n\n**C3. Repo-level n=48 variant-level 统计效力严重不足** [R1-N3, R2-N2, mutual AGREE]\n\nn=48 下 SE ≈ 5.8pp，95% CI 宽 ±11.3pp。CLS Qwen3-8B 两 seed 差 8.33pp（72.92% vs 81.25%，仅 4 个 variant 翻转）。TRAJ DeepSeek 6-seed std = 5.00pp。variant-level 结论对 seed 极度敏感。论文混用 per-test (n=9784) 和 variant-level (n=48) 结果且未充分区分统计可靠性。Contribution #2 的 framing 远强于 variant-level 证据支撑。缺少 bootstrap CI 和 power analysis。\n\n### Warning（Should-Fix，影响评分）\n\n**W1. CWM baseline external validity 严重受限但仍做 formulation-level 归因** [R1-W2, R2-W4, mutual AGREE]\n\n4–8B LoRA fine-tuned CWM ≠ 32B execution-trace mid-trained CWM。正文使用 \"generation formulation\" / \"output space complexity\" 做归因，但 4B→8B 仅 2× scale，不足以推断 formulation-level 天花板。Repo-level CWM format collapse 可能是 capacity 问题而非 formulation-inherent。\n\n**W2. Abstract 数据堆砌** [R2-W1, R1 AGREE]\n\n~250 words 内 15+ 个数值，读起来像实验结果压缩而非叙事。违反写作规范（最多 2–3 关键数字）。\n\n**W3. Cross-model \"validation\" 措辞过强** [R1-W4, R2 AGREE]\n\nn=2 model families 不构成 \"validation\"，至多 \"consistency check\" 或 \"directional evidence\"。单 seed DeepSeek 数据高度不稳定（CLS 7.68pp spread）。\n\n**W4. 新颖性定位：\"design space\" 仅 3 个离散点** [R2-N1, R1 部分 AGREE]\n\n标题 \"Formulation Design Space\" overselling——3 个离散 formulation 不构成连续 space。Function-level equivalence 较预期；repo-level 分析归结为 \"生成长输出更难\"。与 process vs outcome supervision 文献增量不够明确。R1 认为 failure mode taxonomy 有增量价值（轻度分歧）。\n\n**W5. 多重比较问题未处理** [R1-W1, R2 AGREE]\n\n论文以统计严谨性为卖点但未区分 primary/exploratory comparisons，未应用任何多重比较校正。\n\n**W6. 合成数据外部效度讨论不足** [R2-W2, R1 AGREE]\n\nLimitations 仅一句话提及 synthetic-to-real transfer gap。对 formulation ranking 可能因训练数据来源而变化的风险未讨论。\n\n**W7. Error complementarity / ICC oracle analysis 适用范围未限定** [R1-W5, R2 AGREE]\n\nFunction-level ICC=0.191 用于 repo-level oracle analysis 的 transfer 未论证。Repo-level CWM format collapse 使错误互补性不成立（CWM variant-level 低于 majority baseline）。结论应限定为 function-level。\n\n**W8. Related Work 遗漏近期直接相关工作** [R2-W3, R1 部分 AGREE]\n\n缺失：CodePRM (ACL 2025 Findings)、FunPRM (2601.22249)。R1 另指出缺 constrained decoding 方法论文献。CodeScaler 和 CodeRL+ 的相关性需确认。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **TOST margin sensitivity**: ±2pp 论证不足，需 gradient table 和 smallest margin [C1]\n2. **\"Controlled\" framing gap**: 四项 confound 削弱因果归因，建议改 \"systematic\" [C2]\n3. **Repo-level statistical power**: n=48, single-seed, 缺 CI/power analysis [C3]\n4. **CWM external validity**: 4–8B LoRA 结论不可推广为 formulation-level [W1]\n5. **Abstract overloaded**: 15+ 数字，需精简至 2–3 [W2]\n6. **Cross-model \"validation\"**: 措辞过强，应降为 \"consistency check\" [W3]\n7. **Overall score**: 3.0 (Findings) [两人独立一致]\n\n## Reviewer Divergence [REBUT]\n\n仅有两项轻度分歧，均不影响结论：\n\n1. **Re-repair pilot 定位** — R1 认为不应暗示为 contribution；R2 指出它已正确放置在 Appendix 作为负面 pilot，定位恰当。**结论：R2 的 REBUT 成立，论文已正确处理。**\n\n2. **Novelty/Excitement 评分** — R1 给 3.5/5（认为 failure mode taxonomy 有增量价值），R2 给 2.5/5（认为深层机制洞察不足）。**结论：轻度分歧，不影响总分。novelty 定位为 \"empirical methodology contribution\" 比 \"design space exploration\" 更准确。**\n\n---\n\n## Questions（需作者回答）\n\n**Q1.** TOST 在 ±1pp margin 下是否仍然成立？请提供 ±1pp/±1.5pp/±2pp/±3pp 下的 p 值。[R1, R2 一致提问]\n\n**Q2.** 是否尝试过修复 CWM 的 NaN validation loss（如 gradient clipping、loss masking、更小 lr）？如果未尝试，是技术限制还是时间限制？[R1]\n\n**Q3.** CLS Qwen3-8B 两 seed variant-level 差异 8.33pp（72.92% vs 81.25%）。如何在同一 formulation 内如此大的 seed variance 下，仍将 formulation 间差异归因于 formulation choice？[R1, R2 一致关注]\n\n**Q4.** CWM parseable outputs 是否系统性偏向 harder instances？即 unparseable outputs 是否集中在简单 instances？[R1 独特提问]\n\n**Q5.** Oracle ensemble 90.63% 在其他 seeds 下是否稳定？repo-level 的 error complementarity 是否成立（考虑 CWM variant-level < majority baseline）？[R1, R2 一致关注]\n\n**Q6.** 如果改用 real bug data（非 mutation），formulation ranking 是否可能改变？[R2]\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 确认应补充：\n\n1. **CodePRM** (ACL 2025 Findings) — process-level verification in code generation [R2 提出, R1 AGREE]\n2. **FunPRM** (arxiv 2601.22249, 2026) — function-as-step PRM，与 TRAJ 直接相关 [R2 提出, R1 AGREE]\n3. **Constrained decoding 方法论** (如 Willard & Louf 2023) — §4.5 讨论了 constrained decoding 但未引用 [R1 提出]\n\n以下引用需确认相关性后酌情补充：\n4. **CodeScaler** (arxiv 2602.17684, 2026) [R2 提出, R1 要求确认相关性]\n5. **CodeRL+** (arxiv 2510.18471, 2025) [R2 提出, R1 要求确认相关性]\n6. **近年 mutation-real fault coupling meta-analysis** [R1 提出]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置）。跳过。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n**EMNLP 2026 ARR 评分标准**: 3 = Findings（可被 Findings 接收）\n\n**维度评分汇总**:\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Overall | 3.0 | 3.0 | 3.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合判断**:\n\n研究问题重要且实用，实验设计有野心（多 formulation × 多模型 × 多 seed × 多复杂度），统计方法在 NLP 经验论文中属于高水平。Function-level 分析扎实（5 seeds, proper TOST, bootstrap CI），failure mode taxonomy 有诊断价值。\n\n但承载最重要结论的 repo-level 分析在统计支撑上最薄弱：n=48 variant-level evaluation, 1–2 seeds, checkpoint selection asymmetry, eval protocol inconsistency。\"Controlled comparison\" 的 framing 与实际控制程度不匹配。新颖性受限于 3 个离散 formulation 点和较浅的机制分析（\"生成长输出更难\"）。论文的 Limitations 诚实地覆盖了大部分问题，但 Abstract/Contributions 的措辞未反映这些 caveats 的严重程度。\n\n**升级至 Conference (3.5+) 的路径**:\n1. 解决 C1：提供 TOST margin sensitivity gradient table\n2. 解决 C2：将 \"Controlled\" 改为 \"Systematic\"，增加 threats to validity 段落\n3. 解决 C3：为 variant-level 比较增加 bootstrap CI 和 power analysis，降低 claims 语气\n4. 解决 W1：全文 CWM 结论限定为 \"at ≤8B LoRA scale\"\n5. 解决 W2：Abstract 精简至 2–3 关键数字\n6. 解决 W4：调整标题，深化机制分析\n\n以上修改在截止日（2026-05-25）前技术上可行，但需要实质性的重写和可能的补充实验。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 15+ 数字，数据堆砌严重。应保留 function-level equivalence 和 repo-level gap 两个核心数字，其余定性描述。\n- \"same source data with formulation-appropriate label granularity\" 已改善了 Round 3 的 \"identical data\" overclaim，但仍需进一步精简。\n\n### Introduction\n- 叙事线清晰（背景→问题→不足→方法→贡献）。\n- Contribution #2 语气远强于 repo-level 证据。\"Complexity-dependent divergence with formulation × model interaction\" 应加 \"preliminary evidence suggests\" 或 \"initial results indicate\"。\n- 需更明确论证相对 process vs outcome supervision 文献的具体增量。\n\n### Method\n- Formulation 定义清晰、数学符号恰当。\n- Oracle Accuracy-Utility Framework (§3.3) 论证完整。\n- CWM unparseable default-to-pass 策略应在此处讨论方向性影响（当前仅在 Appendix）。\n\n### Experiments\n- Function-level (§4.2): 扎实，5 seeds, proper statistics。\n- Scaling (§4.3): \"matched seeds\" 措辞误导（s42 和 s123 preprocessing 不同）。\"CWM stagnation\" 应改为 \"plateau\" 或 \"flat scaling\"。\n- Per-test vs TRAJ equivalence (§4.4): 核心问题是 margin sensitivity。NF4 vs bf16 mixing 原因应在正文说明。\n- Repo-level (§4.5): 论文最重要也最薄弱的部分。CWM default-to-pass artifact 应在正文讨论。\"Cross-model validation\" → \"Cross-model consistency\"。CWM eval seq_length 差异的 caveat 应更突出。Table 3 建议拆分 per-test 和 variant-level。\n- Analysis (§4.6): Aggregation penalty 分析有价值。Checkpoint selection confound 是好发现。\n\n### Related Work\n- 结构合理（3 段按主题），但偏压缩。缺 CodePRM、FunPRM、constrained decoding 引用。对 PRM/ORM 文献的增量定位不够深入。\n\n### Conclusion\n- 基本准确但应反映 variant-level 结论的 preliminary 性质。\n- Limitations 段落内容全面但格式需确认是否为独立 section（ARR 要求）。\n\n### Appendix\n- 内容充实（A–I），ablation 设计合理。\n- Re-repair pilot (j) 作为负面结果正确放置。\n- Extended Limitations (F) 是 responsible 做法。\n\n### References\n- 38 篇引用，密度中等偏低。需补充 3–6 篇近期直接相关工作。"
  }
}
```

</details>

---


### Tool result

_source line 318 · 2026-05-19T08:41:37.168886+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4753
}
```

</details>

---


### Tool call

_source line 319 · 2026-05-19T08:41:47.983159+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'completed', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'completed', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 320 · 2026-05-19T08:41:47.983705+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 321 · 2026-05-19T08:41:57.972891+00:00_

**圆桌审稿完成。**

审稿报告已投递至 Research Director。

**结论：Overall 3.0 — Findings**

两位 Reviewer 独立评分一致（R1: 3.0, R2: 3.0），交叉分享后在所有关键问题上达成共识，1 轮即收敛。

**3 个 Critical 问题**：
1. TOST ±2pp margin 缺 sensitivity analysis，动摇 Contribution #1
2. "Controlled comparison" 与实际设计存在 4 项系统性裂隙（checkpoint/seq_length/preprocessing/TRAJ regime）
3. Repo-level n=48 variant-level 统计效力不足，缺 CI 和 power analysis

**8 个 Warning 问题**：CWM external validity 归因过强、Abstract 数据堆砌、cross-model "validation" 措辞过强、novelty 定位偏高、多重比较未校正、合成数据外部效度、error complementarity 适用范围未限定、Related Work 遗漏近期工作。

**升级路径存在**：如果解决 C1–C3 + W1–W2 + W4，可达 3.5 (Borderline Conference)。技术上在截止日前可行但需实质性重写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 32

## Round 32

2 recorded events


### User

_source line 322 · 2026-05-19T08:42:00.748209+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

逐条对 R1 的 16 个 Weakness/Minor 做了判断：**13 条 AGREE、2 条 REBUT、1 条部分 AGREE**。

两条 REBUT：
- **W3**（re-repair pilot）：它仅在 Appendix 中作为负面 pilot 呈现，未列入 contribution，定位合理
- **M5**（2026 引用 ARR 政策）：ARR 允许引用公开 arXiv 预印本，不构成合规问题

与 R1 的核心共识：Overall 3.0 (Findings)，但维度分配不同——R1 对 soundness 更严（方法论 confound 拆解更细），我对 excitement 更严（design space 仅 3 点、新颖性不足）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 323 · 2026-05-19T08:42:14.517154+00:00_

圆桌审稿已完成。

**审稿报告已投递至 Research Director。**

汇总如下：

**Overall: 3.0 — Findings**（两位 Reviewer 独立一致）

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**3 个 Critical 问题**（共识）：
1. **C1** TOST ±2pp margin 缺 sensitivity analysis，动摇 Contribution #1
2. **C2** "Controlled comparison" 与实际设计存在 4 项系统性 confound（checkpoint/seq_length/preprocessing/TRAJ regime）
3. **C3** Repo-level n=48 variant-level 统计效力不足，缺 CI 和 power analysis

**8 个 Warning 问题**（共识或轻度分歧）：
CWM external validity、Abstract 数据堆砌、cross-model "validation" 措辞过强、novelty 定位偏高、多重比较未处理、合成数据外部效度、error complementarity 适用范围、Related Work 遗漏

**Issue Tracker 已同步更新**：`artifacts/review_issues.yaml`（19 个 open/in_progress issues + 7 个 resolved）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 33

## Round 33

86 recorded events


### User

_source line 324 · 2026-05-19T09:30:09.315857+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 325 · 2026-05-19T09:30:15.731185+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 326 · 2026-05-19T09:30:15.782279+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 327 · 2026-05-19T09:30:49.282610+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 328 · 2026-05-19T09:30:49.484131+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 329 · 2026-05-19T09:31:02.663339+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 330 · 2026-05-19T09:31:02.715037+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-19T09:31:06.593367+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 332 · 2026-05-19T09:31:06.593971+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 333 · 2026-05-19T09:31:11.476737+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-19T09:31:11.778412+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-19T09:31:12.182418+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (216 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T07:07:07Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 216 个实验 — ALLOCATED 1, DONE 200, PREPARING 14, RUNNING 1\n**DONE 分布**: failed 47, killed 26, negative 7, success 120\n\n### GPU 占用\n- **实际运行**: 1 张 — seetacloud-westd-4x5090:cuda:0(qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval)\n\n### 💾 磁盘余量\n- **seetacloud-westd-4x5090**:\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 436G/879G 可用（已用 48%）\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval` | seetacloud-westd-4x5090 | cuda:0 | 778328 | `…air-verifier/qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval.log` |\n\n### 📌 最近完成 (top 5)\n- `exp-downsample-cls-func-v3-eval` [failed] — 2026-05-19T07:07:03 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `exp-downsample-cls-func-v3` [success] — 2026-05-19T06:57:21\n- `deepseek-cwm-repo-s123` [failed] — 2026-05-19T04:38:19 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `repo-level-3shot-baseline` [success] — 2026-05-19T04:36:55 — CORRECTED: initial
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 705
}
```

</details>

---


### Tool result

_source line 336 · 2026-05-19T09:31:21.348226+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 using ARR:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. In addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Important Dates

The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026. Author response and author-reviewer discussion runs from July 7-13, 2026, and the meta review is r
…[truncated 919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 9569
}
```

</details>

---


### Tool call

_source line 337 · 2026-05-19T09:31:25.982000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template anonymization guidelines site:2026.emnlp.org OR site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template anonymization guidelines site:2026.emnlp.org OR site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-19T09:31:28.745001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-19T09:31:29.247946+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Math
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	
10	% Tables
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{tabularx}
14	
15	% Graphics
16	\usepackage{graphicx}
17	\graphicspath{{../../artifacts/}}
18	
19	% Lists
20	\usepackage{enumitem}
21	
22	% Custom commands
23	\newcommand{\cls}{\textsc{Cls}}
24	\newcommand{\cwm}{\textsc{Cwm}}
25	\newcommand{\traj}{\textsc{Traj}}
26	\newcommand{\fone}{F\textsubscript{1}}
27	\newcommand{\pp}{\,\text{pp}}
28	
29	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Systematic Empirical Study}
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{abstract}
36	
37	\input{introduction}
38	
39	\begin{figure*}[t]
40	\centering
41	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
42	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
43	\label{fig:reformulation}
44	\end{figure*}
45	
46	\input{method}
47	
48	\input{experiments}
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
53	\caption{Gap amplification from function-level to repo-level complexity. Function-level: \cls{}--\cwm{} gap is 1.32\pp{} at 4B, widening to 2.62\pp{} at 8B (2 matched seeds, bootstrap $p{<}.01$). Repo-level same-size 4B: the gap explodes to 25.59\pp{}, with \cwm{} falling below the majority baseline (72.96\%).}
54	\label{fig:scaling_gap}
55	\end{figure}
56	
57	
58	\input{related_work}
59	
60	\input{con
…[truncated 116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-19T09:31:29.650255+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-19T09:31:32.955384+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template anonymization guidelines site:2026.emnlp.org OR site:aclrollingreview.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Submission Form Fields","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsibleNLPresearch/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices","url":"http://aclrollingreview.org/responsible-nlp-checklist-appendices"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"}]

I found relevant information from the EMNLP 2026 Industry Track and ACL Rolling Review (ARR) guidelines. Here are the key submission requirements:

## **Anonymization Guidelines**

Industry Track submissions must neither include the authors' names nor their affiliations. More broadly, papers must not include authors' names and affiliations, and self-references that reveal authors' identities must be avoided.

Submissions should avoid links to non-anonymised repositories; code should be submitted as a link to an anonymised repository (e.g., Anonymous GitHub or Anonym Share). Links to file hosting services that can track downloads, such as Dropbox, are not allowed.

## **Page Limits and Appendices**

Authors are required to discuss the limitations of their work in a dedicated section titled "Li
…[truncated 618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 6973
}
```

</details>

---


### Tool result

_source line 342 · 2026-05-19T09:31:33.006345+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/literature_map.yaml\", \"content\": \"papers:\\n  # === Execution Simulation (5/5) ===\\n  - bibtex_key: maimon2026selfexecution\\n    title: \\\"Self-Execution Simulation Improves Coding Models\\\"\\n    authors: \\\"Maimon et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv: \\\"2604.03253\\\"\\n    doi: \\\"\\\"\\n    category: \\\"Execution Simulation\\\"\\n    verified: true\\n    abstract_snippet: \\\"Train code LLMs to simulate program execution step-by-step; self-verification by filtering code solutions based on predicted output.\\\"\\n    relevance: \\\"Closest prior work — trains LLMs for execution prediction via generation, we reformulate as classification.\\\"\\n\\n  - bibtex_key: meta2025cwm\\n    title: \\\"CWM: An Open-Weights LLM for Research on Code Generation with World Models\\\"\\n    authors: \\\"Meta AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv: \\\"2510.02387\\\"\\n    doi: \\\"\\\"\\n    category: \\\"Execution Simulation\\\"\\n    verified: true\\n    abstract_snippet: \\\"32B open-weights LLM mid-trained on Python execution traces; 65.8% on SWE-bench Verified.\\\"\\n    relevance: \\\"Production-scale CWM approach; our CWM baseline follows their generation formulation at smaller scale.\\\"\\n\\n  - bibtex_key: liu2024codemind\\n    title: \\\"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv: \\\"2402.09664\\\"\\n    doi: \\\"\\\"\\n    category: \\\"Execution Simulation\\\"\\n    verified: true\\n    abstract_snippet: \\\"Framework for evaluating LLM code reasoning: IER, DER, SR, DSR tasks. Performance drops with higher complexity.\\\"\\n    relevance: \\\"Evaluates execution reasoning capabilities; our work proposes classification as more robust formulat
…[truncated 1732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3356
}
```

</details>

---


### Tool call

_source line 343 · 2026-05-19T09:31:41.451648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 long paper page limit short paper format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 long paper page limit short paper format requirements"
  }
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-19T09:31:43.813407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-19T09:31:44.316261+00:00_

1	\begin{abstract}
2	Execution-free verification for LLM-based code repair can be formulated as per-test binary classification (\cls{}), execution output generation (\cwm{}), or trajectory-level patch scoring. Despite active development along each axis, no prior work compares these formulations under matched conditions. We present a systematic comparison across two model families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds, all at 4--8B LoRA fine-tuning scale.
3	
4	At function level, all three formulations achieve near-equivalent accuracy; Two One-Sided Tests (TOST) confirm per-test and trajectory approaches are statistically equivalent ($p{=}0.007$, $\pm$2\pp{} margin, 5 seeds). At repository level under the same training protocol, divergence amplifies to 19--26\pp{}, with generation-based simulation falling below majority baseline. The pattern is consistent across model families but model-contingent in magnitude.
5	
6	Two findings generalize. Per-test classification provides diagnostic granularity (which tests fail) at comparable accuracy, with configuration-dependent aggregation cost at repository level. Formulations exhibit complementary errors at function level (oracle ensemble: 90.63\%), motivating complexity-aware routing over uniform formulation selection.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-19T09:31:44.316765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-19T09:31:44.619210+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	These three formulations represent discrete points in the verification design space, each imposing different output complexity, diagnostic granularity, and inference cost. We present the first systematic empirical comparison across two model families (Qwen3, DeepSeek-Co
…[truncated 4046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-19T09:31:44.669985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-19T09:31:44.720716+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation
…[truncated 3266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 350 · 2026-05-19T09:31:46.179111+00:00_

Web search results for query: "ACL Rolling Review 2026 long paper page limit short paper format requirements"

Links: [{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

Based on the search results, here is the information about ACL Rolling Review 2026 paper format requirements:

## Long Papers

Long papers may have up to eight (8) pages of content plus unlimited pages for references.

## Short Papers

Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

## Additional Format Information

If pseudo-code, derivations, or model specifications are important for reviewers to assess technical correctness, they should be part of the main paper and not in appendices. Reviewers are not required to consider material in appendices. Appendices should come after the references in the submitted PDF, but do not count towards the page limit.

Some kinds of short papers include: a small, focused contribution, a negative result, an opinion piece, or an interesting application nugget.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 4727
}
```

</details>

---


### Tool call

_source line 351 · 2026-05-19T09:32:02.343790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-19T09:32:03.310611+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two model families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, defaulting to the final epoch checkpoint (affects DeepSeek s123 and all \cwm{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-
…[truncated 23705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 966
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-19T09:32:03.311160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-19T09:32:03.413053+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Scratchpad-based execution trace generation~\cite{nye2021scratchpad} established that intermediate computation steps improve neural execution prediction. Code World Models~\cite{meta2025cwm} predict output strings via 32B mid-training on execution traces; extensions address step-by-step prediction~\cite{maimon2026selfexecution}, code reasoning~\cite{liu2024codemind}, pre-trained execution simulation~\cite{liu2023codeexecutor}, simulation-execution bridging~\cite{lee2026solidcoder}, failure mode analysis~\cite{abdollahi2025demystifying}, and execution-free error detection~\cite{li2024redo}. Alternative formulations include trajectory-level reward models~\cite{shum2025swerm}, execution-free reward scaling~\cite{zhu2026codescaler}, process-level verification with execution feedback~\cite{li2025codeprm}, chain-of-thought verification~\cite{xu2025patchreasoner}, per-test classifiers~\cite{ni2023lever,chen2023codet}, and learned quality metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} further demonstrate verification value. None compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	Lightman et al.~\cite{lightman2023letsverify} and Uesato et al.~\cite{uesato2022solving} show process reward models (PRMs) outperform outcome reward models (ORMs) for mathematical reasoning; Math-Shepherd~\cite{wang2024mathshepherd} and OmegaPRM~\cite{luo2024omegaprm} scale process supervision via automated annotation. DreamPRM-Code~\cite{dreamprm2025code}, PRL-Coder~\cite{ye2025prlcoder}, FunPRM~\cite{zhang2026funprm}, and CodeRL+~\cite{jiang2025coderlplus} apply process-level or execution-aligned supervision to code. In the PRM/ORM framing, our \cls{} provides per-step (per-test) supervision while \t
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 355 · 2026-05-19T09:32:03.414327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-19T09:32:03.465136+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). \cls{} achieves the highest per-test accuracy across all tested conditions; at variant level, aggregation penalty makes the advantage configuration-dependent, motivating complexity-aware routing.
5	
6	At function level, all three formulations achieve near-equivalent accuracy (TOST $p{=}0.007$, 5 seeds). At repository level under our training protocol, divergence amplifies to 19--26\pp{}; cross-model consistency checks confirms this is consistent across both families but model-contingent in magnitude (Qwen3: ${\sim}$5/22\pp{}; DeepSeek: 4--12/25--30\pp{} for \cls{}/\cwm{}). Seed variance and evaluation protocol add further sensitivity (${\sim}$9\pp{} for the same \cwm{} checkpoint).
7	
8	Two properties generalize across models. First, per-test classification provides diagnostic granularity at comparable or better accuracy at function level; at repo level, aggregation penalty is configuration-dependent (1.36--19\pp{}). Second, classification yields 217$\times$ throughput over generation. Error complementarity at function level (oracle ensemble: 90.63\%) further motivates instance-level routing; whether this complementarity holds at repository level, where \cwm{} accuracy falls below majority baseline, remains open.
9	
10	\paragraph{Practical recommendations.} At function level, all three formulations achieve equivalent accuracy; \cls{} is preferred for its 217$\times$ throughput advantage and per-test diagnostic signal. At repository level under standard LoRA fine-tuning (${\leq}$8B), \cls{} is strongly preferred: \cwm{} falls below majority baseline due to output space complexity (19--26\pp{} gap). Generation-based verification at repo level requires either larger models or execution-trace pretraining (\S\ref{sec:threats}). When per-test diagnostic granularity is not needed, trajectory-level sco
…[truncated 1421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-19T09:32:08.643285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-19T09:32:08.946024+00:00_

1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlat
…[truncated 31803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-19T09:32:08.946382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-19T09:32:08.997400+00:00_

1	% === Execution Simulation ===
2	
3	@article{maimon2026selfexecution,
4	  title={Self-Execution Simulation Improves Coding Models},
5	  author={Maimon, Gallil and Yoran, Ori and Kreuk, Felix and Hassid, Michael and Cohen, Gal and Chambon, Pierre and Adi, Yossi},
6	  journal={arXiv preprint arXiv:2604.03253},
7	  year={2026}
8	}
9	
10	@article{meta2025cwm,
11	  title={{CWM}: An Open-Weights {LLM} for Research on Code Generation with World Models},
12	  author={{FAIR CodeGen team} and Copet, Jade and Carbonneaux, Quentin and Cohen, Gal and Gehring, Jonas and Kahn, Jacob and Kossen, Jannik and Kreuk, Felix and McMilin, Emily and Meyer, Michel and Wei, Yuxiang and Zhang, David and Zheng, Kunhao and others},
13	  journal={arXiv preprint arXiv:2510.02387},
14	  year={2025}
15	}
16	
17	@article{liu2024codemind,
18	  title={{CodeMind}: A Framework to Challenge Large Language Models for Code Reasoning},
19	  author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh},
20	  journal={arXiv preprint arXiv:2402.09664},
21	  year={2024}
22	}
23	
24	@article{abdollahi2025demystifying,
25	  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},
26	  author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi},
27	  journal={arXiv preprint arXiv:2512.00215},
28	  year={2025}
29	}
30	
31	@article{lee2026solidcoder,
32	  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},
33	  author={Lee, Woojin and Huang, Jin-Xia},
34	  journal={arXiv preprint arXiv:2604.19825},
35	  year={2026}
36	}
37	
38	@article{nye2021scratchpad,
39	  title={Show Your Work: Scratchpads for Intermediate Computation with Language Models},
40	  author={Nye, Maxwell and Andreassen, Anders Johan and Gur-Ari, Guy and Michalewski, Henryk and Austin, Jacob and Biber, David and Dohan, David and Lewkowycz, Aito
…[truncated 16967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-19T09:32:15.269203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-19T09:32:15.773939+00:00_

1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: single-seed repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and single-seed constraints.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified unde
…[truncated 4224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 363 · 2026-05-19T09:32:15.875171+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 364 · 2026-05-19T09:32:15.926013+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-19T09:32:20.047172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-19T09:32:20.299388+00:00_

1	issues:
2	# === Round 4 Critical Issues (fresh review) ===
3	
4	- id: "R4-N1"
5	  summary: "TOST ±2pp equivalence margin 缺乏正式论证和 sensitivity analysis"
6	  category: method
7	  severity: critical
8	  status: in_progress
9	  first_raised_round: 4
10	  last_seen_round: 4
11	  mentions:
12	    - round: 4
13	      reviewers: [1, 2]
14	      note: "R1 首次提出，R2 交叉 AGREE。±2pp 仅一句话论证，缺 ±1pp/±1.5pp/±3pp 下的 p 值梯度表和 smallest equivalence margin。直接动摇 Contribution #1。"
15	  action_items:
16	    - round: 4
17	      action: "Agent 从 clustered bootstrap 原始数据独立重算 TOST margin sweep ±0.5~5.0pp"
18	      assigned_to: "agent"
19	      status: in_progress
20	    - round: 4
21	      action: "Paper Agent 将 sensitivity table 加入 Appendix + 正文 deployment-relevance 论证"
22	      assigned_to: "paper"
23	      status: open
24	  resolution: ""
25	  resolution_round: null
26	
27	- id: "R4-N2"
28	  summary: "'Controlled comparison' 声称与实际设计存在系统性裂隙（checkpoint/seq_length/preprocessing/TRAJ regime）"
29	  category: experiment
30	  severity: critical
31	  status: in_progress
32	  first_raised_round: 4
33	  last_seen_round: 4
34	  mentions:
35	    - round: 4
36	      reviewers: [1, 2]
37	      note: "R1 首次逐项拆解，R2 交叉 AGREE 并补充定量证据。四项 confound。"
38	  action_items:
39	    - round: 4
40	      action: "Paper Agent: Title 从 'Controlled' 改为 'Systematic' + 新增 Threats to Validity 段落"
41	      assigned_to: "paper"
42	      status: in_progress
43	  resolution: ""
44	  resolution_round: null
45	
46	- id: "R4-N3"
47	  summary: "Repo-level n=48 variant-level 统计效力严重不足，缺 CI 和 power analysis"
48	  category: experiment
49	  severity: critical
50	  status: in_progress
51	  first_raised_round: 4
52	  last_seen_round: 4
53	  mentions:
54	    - round: 4
55	      reviewers: [1, 2]
56	      note: "两人独立发现并交叉 AGREE。n=48 下 SE≈5.8pp, 95% CI 宽±11.3pp。"
57	  action_items:
58	    - round: 4
59	      action: "Agent 计算 variant-level bootstrap CI + power analysis"
60	      assigned_to: "agent"
61	      status: in_progress
62	    - round: 4

…[truncated 15744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 367 · 2026-05-19T09:32:20.299894+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 368 · 2026-05-19T09:32:20.400955+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml\", \"content\": \"_next_id: 153\\ndecisions:\\n- id: D001\\n  date: 2026-05-11 18:01 UTC\\n  summary: 'MVP 方案: Monte Carlo oracle 模拟 + 函数级 pilot，不依赖 Docker 基础设施'\\n  rationale: '完整 Part 1 需要 Docker 重新评估 8K 个 patch 获取 per-test labels（16-24h），基础设施搭建成本高。MVP\\n    改用 Monte Carlo 模拟参数化真实测试数分布验证理论信息增益，函数级 pilot (HumanEval/MBPP) 验证可学习性。两者均无需 Docker，2-3\\n    天可完成。Pass 标准: per-test 在 70-85% 精度下 resolve rate 比 trajectory-level 高 ≥5%; 函数级\\n    pilot 精度 >70%。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-11 19:07 UTC\\n  summary: MVP-A 有条件通过：F2P-only block-corr 10.88%>5%；需补跑 Total(F2P+P2P) 模拟确认全图\\n  rationale: 真实 SWE-bench F2P median=1（69% 实例仅 1 个 F2P 测试），但 P2P median=50.5。F2P-only\\n    下 per-test 优势收窄但仍过阈值（block-corr 10.88%）。P2P regression 检测是更大的信号源——Total 分布(median=52)下优势预期更强。研究方向需校准：per-test\\n    价值主要来自 P2P regression 检测 + F2P multi-test 精确定位，而非单纯的 F2P 粒度。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: F2P-only block-corr advantage 10.88%, i.i.d. 1.98%\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-11 19:38 UTC\\n  summary: P2P regression rate 是项目关键前提——≥10% per-test 有效，<5% 则有害；需实测\\n  rationale: Total 模拟(F2P+P2P)显示 per-test 优势强烈依赖 P2P regression rate：5% 时优势为负(-1%)，10%\\n    时 13.2%，20% 时 35.7%。这是从 F2P-only 分析未发现的关键变量。真实 regression rate 未知，需从 SWE-bench\\n    数据/文献中实测。此数据点决定项目是否可行及论文 story 如何构建。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: 'Total sim: reg=5% adv=-1%, reg=10% adv=13.2%, reg=20% adv=35.7%'\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-11 20:05 UTC\\n  summary: P2P 回归率 ~1%，原始 Total 优势前提不成立；项目 reframe 而非 kill\\n  rationale: P2P 回归率 ~1%（mean=1.04%, median=0%, 仅 22.6% 错误 patch 破坏任何 P2P 测试），远低于\\n    per-test 有效的 10% 阈值。Total(F2P+P2P) 模型下 per-test 实际有害（噪声>信号）。但项目核心价值不在信
…[truncated 1464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-19T09:32:40.112023+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-19T09:32:40.464203+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 371 · 2026-05-19T09:32:43.885846+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check external review config",
  "subagent_type": "Explore",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier, find any configuration file (YAML, JSON, or TOML) that mentions \"external_review\" or \"paperreview_ai\" or \"paperreview.ai\". Check agent/ directory, config files, or any .yaml/.json files. Report whether external_review is enabled or not. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check external review config",
    "subagent_type": "Explore",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier, find any configuration file (YAML, JSON, or TOML) that mentions \"external_review\" or \"paperreview_ai\" or \"paperreview.ai\". Check agent/ directory, config files, or any .yaml/.json files. Report whether external_review is enabled or not. Search breadth: medium."
  }
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-19T09:32:46.297199+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/**/*.{yaml,yml,json,toml}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/**/*.{yaml,yml,json,toml}"
  }
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-19T09:32:46.347953+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" \\) 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" \\) 2>/dev/null | head -30"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-19T09:32:46.398713+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_PREPARING_20260511T180203.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_PREPARING_20260511T180203.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_infra_env-check_20260511T180230_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_infra_gpu-cleanup_20260511T182535_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_QUEUED_20260511T183926.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_RUNNING_20260511T183930.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_RUNNING_20260511T183937.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_DONE_20260511T183941.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_mvp-a-oracle-sim_20260511T182340_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_PENDING_20260511T185932.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_QUEUED_20260511T185944.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_RUNNING_20260511T185948.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_RUNNING_20260511T185959.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_DONE_20260511T190003.json
/home/ubun
…[truncated 12900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-19T09:32:46.550090+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_eval-nan-fix-deepseek_20260517T035959_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_eval_home-seed123-ckpt800-then-v5-sweep_20260514T210725_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_fix-repo-level-sample-weight_20260512T112618_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_train_s42-8b-resume-immediate_20260514T204620_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_analysis_table2-seed-basis-check_20260518T185458_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_infra_read-pr-results_20260512T060822_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_collect_critical-ckpt600-test8192-result_20260514T220030_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_fix-repo-level-sample-weight_20260512T141229_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_eval_deepseek-cwm-repo-s123_20260517T161324_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_research_test-curve-compilation_20260515T140344_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_monitor_full-gpu-status_20260517T202038_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_rep
…[truncated 2775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-19T09:32:48.309835+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ | grep -E \"(yaml|yml|json|toml|config|agent)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ | grep -E \"(yaml|yml|json|toml|config|agent)\""
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-19T09:32:48.761935+00:00_

-rw-------  1 ubuntu ubuntu 142061 May 19 07:22 decisions.yaml
-rw-------  1 ubuntu ubuntu   8567 May 18 18:09 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu   8572 May 18 18:09 dream_registry.yaml.bak
-rw-------  1 ubuntu ubuntu   5679 May 14 00:57 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  14143 May 15 12:52 literature_map.yaml
-rw-------  1 ubuntu ubuntu  15425 May 19 09:06 mistakes.yaml
-rw-------  1 ubuntu ubuntu  43414 May 18 19:26 paper_provenance.yaml
-rw-------  1 ubuntu ubuntu 362318 May 19 07:10 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  16632 May 16 06:03 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-19T09:32:49.115065+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -maxdepth 3 -type f -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" 2>/dev/null | grep -v checkpoints | grep -v logs | grep -v artifacts | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -maxdepth 3 -type f -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" 2>/dev/null | grep -v checkpoints | grep -v logs | grep -v artifacts | head -20"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-19T09:32:49.215965+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-19T09:32:51.078008+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai|paperreview\\.ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai|paperreview\\.ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-19T09:32:51.329488+00:00_

Found 13 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/chats/feishu_group_oc_0ae20ec1ce60f9c0589d629648584eff_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/chats/archive/feishu_group_oc_b2cf3b1eba4db851529b6a1a7a34c4e8_reviewer_20260519T084752_309618.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/chats/archive/feishu_group_oc_061c4b1115e483e8fdad01cae91c873a_director_20260519T084400_847680.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/chats/worker_infra_home-cwm-s42-e2-setup-launch_20260518T144853.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_infra_home-cwm-s42-e2-setup-launch_20260518T144853.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260517T034206/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_eval_cls-v5-urgent_20260513T155329.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_best.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-19T09:32:51.329999+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/ 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-19T09:32:51.430782+00:00_

total 36
drwxr-xr-x  4 ubuntu ubuntu  4096 May 18 18:02 .
drwxr-xr-x 11 ubuntu ubuntu  4096 May 19 09:14 ..
-rw-r--r--  1 ubuntu ubuntu 17206 May 19 09:31 CLAUDE.md
drwxr-xr-x 87 ubuntu ubuntu  4096 May 19 07:07 sessions
drwxr-xr-x  2 ubuntu ubuntu  4096 May 18 18:04 worktrees

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-19T09:32:52.988518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/CLAUDE.md"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-19T09:32:53.492376+00:00_

1	## 当前项目
2	当前绑定项目：**exec-sim-repair-verifier**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("exec-sim-repair-verifier")` 或 `load_project_config("exec-sim-repair-verifier", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/`（写文件后用 `register_artifact` 注册）
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
56	  - Related Work 怎么 positioning 自
…[truncated 9026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-19T09:32:53.644828+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -name \"AGENTS.md\" -o -name \"config.yaml\" -o -name \"config.yml\" -o -name \"config.json\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -name \"AGENTS.md\" -o -name \"config.yaml\" -o -name \"config.yml\" -o -name \"config.json\" 2>/dev/null"
  }
}
```

</details>

---


### Tool call

_source line 387 · 2026-05-19T09:32:53.697054+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/ | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/ | head -20"
  }
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-19T09:32:53.747857+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_8401d4e4/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_c50c6655/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_2c8595e9/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_015d731a/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_reviewer_2_ac5405e9/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_73218637/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_c38df6bb/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_afc9591d/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_51e42182/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_2281d02c/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_9a2f7ea5/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_bc5a0163/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_7a6138da/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/briefer_f20040f0/AGENTS.md
/home/ub
…[truncated 8765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 103
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-19T09:32:53.798652+00:00_

total 348
drwxr-xr-x 87 ubuntu ubuntu 4096 May 19 07:07 .
drwxr-xr-x  4 ubuntu ubuntu 4096 May 18 18:02 ..
drwxr-xr-x  2 ubuntu ubuntu 4096 May 12 09:21 agent_015d731a
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 10:30 agent_02faa6ba
drwxr-xr-x  2 ubuntu ubuntu 4096 May 12 10:59 agent_03a78f6d
drwxr-xr-x  2 ubuntu ubuntu 4096 May 16 18:27 agent_04b3d77b
drwxr-xr-x  2 ubuntu ubuntu 4096 May 12 13:14 agent_06f25cb5
drwxr-xr-x  2 ubuntu ubuntu 4096 May 12 08:19 agent_0de7aaa7
drwxr-xr-x  2 ubuntu ubuntu 4096 May 16 13:46 agent_1aebf38c
drwxr-xr-x  2 ubuntu ubuntu 4096 May 14 01:06 agent_1aed9aa8
drwxr-xr-x  2 ubuntu ubuntu 4096 May 12 17:55 agent_1ba9e99e
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 18:37 agent_2257bcc1
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 10:43 agent_2281d02c
drwxr-xr-x  2 ubuntu ubuntu 4096 May 12 09:26 agent_2406d87f
drwxr-xr-x  2 ubuntu ubuntu 4096 May 12 15:25 agent_25b6c083
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 06:24 agent_27e5fdba
drwxr-xr-x  2 ubuntu ubuntu 4096 May 14 01:17 agent_28bebe1c
drwxr-xr-x  2 ubuntu ubuntu 4096 May 12 12:48 agent_292b6004
drwxr-xr-x  2 ubuntu ubuntu 4096 May 16 00:27 agent_2c8595e9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-19T09:32:55.957503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/AGENTS.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/AGENTS.md",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-19T09:32:56.359683+00:00_

1	## 当前项目
2	当前绑定项目：**exec-sim-repair-verifier**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("exec-sim-repair-verifier")` 或 `load_project_config("exec-sim-repair-verifier", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/`（写文件后用 `register_artifact` 注册）
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
56	  - Related Work 怎么 positioning 自
…[truncated 1262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-19T09:32:56.510949+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/*.yaml 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/*.yaml 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-19T09:32:56.561969+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-19T09:32:58.771434+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-19T09:32:58.923340+00:00_

Exit code 123

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-19T09:32:58.923785+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/ 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/ 2>/dev/null | head -30"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-19T09:32:58.924093+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(find /home/ubuntu/.agent-ml-research-ide…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-19T09:33:01.025998+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai|paperreview\\.ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai|paperreview\\.ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-19T09:33:01.227417+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_3.md:156:外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置）。跳过。
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_2.md:157:**状态：已跳过**（用户未提交至 paperreview.ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/chats/worker_infra_home-cwm-s42-e2-setup-launch_20260518T144853.jsonl:81:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260517T034206/logs/review_worst.log:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_best.log:40:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_best.log:74:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_best.log:78:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_best.log:87:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_median.log:25:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_median.log:31:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/logs/review_median.log:70:[Omitted long matching line]
/home/ub
…[truncated 15634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-19T09:33:03.142356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_3.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_3.md",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-19T09:33:03.245607+00:00_

1	---
2	round: 3
3	review_mode: fresh
4	overall_score: 3.0 — Findings
5	timestamp: 2026-05-19T08:41:32.446070+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 4 (Fresh Review)
12	
13	**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study"
14	**目标 Venue**: EMNLP 2026 via ARR (deadline: 2026-05-25)
15	**审稿模式**: Fresh（重新审稿，无上轮记忆）
16	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
17	**圆桌轮次**: 1 轮（Round 1 + 交叉分享后达成共识）
18	
19	---
20	
21	## Summary
22	
23	本文对 execution-free code verification 的三种 formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹级评分）进行了系统比较，覆盖两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（function-level、repo-level）和多 seed。核心发现：function-level 三者统计等价（TOST p=0.007, ±2pp）；repo-level CLS 大幅优于 CWM（19–26pp gap）；error complementarity 支持 ensemble。研究设计有野心，统计方法（TOST、clustered bootstrap、ICC）在 NLP 经验论文中属于高水平；但 "controlled comparison" 的执行在 repo-level 有多个系统性缺陷，新颖性定位偏高于实际贡献深度。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 研究问题重要且清晰。** 验证 pipeline 中的 formulation 选择是实际工程决策，无先前工作提供 head-to-head 比较。论文填补了一个真实空白。[R1, R2 共识]
30	
31	**S2. 多维度实验设计。** 覆盖 formulation(3) × model family(2) × model size(2) × complexity(2) × seeds(up to 5)，比该领域典型论文更系统。[R1, R2 共识]
32	
33	**S3. 统计方法规范。** TOST 用于 null-result claim（而非仅 "无显著差异"）、clustered bootstrap 处理 within-problem 依赖、ICC 量化相关结构——方法选择均正确。[R1, R2 共识]
34	
35	**S4. Failure mode taxonomy 有洞察力。** Table 4 区分 format collapse / decision collapse / aggregation penalty，且展示同一模型在不同 configuration 下触发不同模式（DeepSeek s42 vs s123），是非平凡发现。[R1 强调, R2 认同]
36	
37	**S5. 消融设计全面。** LoRA rank、序列长度 matched-context、训练数据 downsampling、few-shot baselines、relaxed matching——系统性地排除了常见替代解释。[R1, R2 共识]
38	
39	**S6. Limitations 诚实。** 论文在正文和 Appendix 中主动披露了几乎所有方法论弱点（单 seed、NaN loss、eval seq_length 不一致等）。[R1 特别提及]
40	
41	---
42	
43	## Weaknesses
44	
45	### Critical（Must-Fix，影响接收决定）
46	
47	**C1. TOST ±2pp equivalence margin 缺乏正式论证和 sensitivity analysis** [R1-N1, R2 AGREE]
48	
49	§
…[truncated 7255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-19T09:33:03.297362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_2.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_2.md",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-19T09:33:03.348486+00:00_

1	---
2	round: 2
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-19T03:04:14.298259+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# Round 3 审稿报告（Fresh Review）
12	
13	**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study
14	**Venue**: EMNLP 2026 (ACL Rolling Review)
15	**审稿模式**: Fresh（重新审稿，无上轮记忆）
16	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作质量+格式合规）
17	**外部审稿**: 已跳过（用户未提交）
18	
19	---
20	
21	## Summary
22	
23	本文对三种 execution-free code verification formulation（per-test classification CLS、execution output generation CWM、trajectory-level patch scoring TRAJ）进行了系统对比，使用两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别（function-level, repo-level）、多个随机种子。核心发现：function-level 三种 formulation 准确率等价（TOST $p=0.007$）；repo-level CLS 显著优于 CWM（19-26pp）；CWM 在 repo-level 因 format collapse 失效（51-74% 不可解析输出）；CLS 和 CWM 存在互补错误模式（oracle ensemble 90.63%）。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 研究问题重要且定义清晰。** 三种 execution-free verification formulation 之间缺乏系统比较，论文将工程选择问题提升为科学问题，对 LLM-based repair pipeline 从业者有直接实用价值。[R1-S1, R2 共识]
30	
31	**S2. 统计方法论水准高。** 使用 TOST 等价性检验（非仅 NHST）、clustered bootstrap（尊重 problem-level 相关结构）、ICC 量化 within-problem correlation、margin sensitivity analysis。这在 NLP 实证研究中属于高标准。[R1-S2, R2 优势 #1]
32	
33	**S3. Function-level 结果稳健。** 5 seeds × 2 model families × 3 formulations 的 function-level 比较有充分统计效力，TOST 等价性结论和 clustered bootstrap CI 互相印证。[R1-S3]
34	
35	**S4. Failure mode taxonomy 有实用价值。** Table 4 的三种 failure mode 分类（format collapse, decision collapse, aggregation penalty）和 Appendix G 的 qualitative error analysis 为从业者选择 formulation 提供了实用参考。[R1-S4, R2 优势 #3]
36	
37	**S5. 对自身局限的透明度。** 论文明确讨论了 NaN validation loss、单种子限制、val-test distribution mismatch、eval seq_length sensitivity 等问题。这种坦诚在投稿论文中不常见。[R2 优势 #2]
38	
39	**S6. 消融实验覆盖面广。** LoRA rank ablation、majority voting、sequence-length ablation、relaxed matching、constrained decoding 讨论，涵盖了审稿人可能提出的多数 "what 
…[truncated 8550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-19T09:33:11.558252+00:00_

Perfect! I have found the key information about external review configuration. Let me verify the exact status one more time by checking the most recent status call:

Based on my comprehensive search of the project directory, here are my findings:

## Configuration File Search Results

**External Review Status: DISABLED / NOT ENABLED**

### Key Findings:

1. **Configuration Status**
   - Line 156 of Round 3 review report (`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_3.md`):
     > "外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置）。跳过。"
     > (External review not configured (`external_review.paperreview_ai.enabled` not set). Skipped.)

   - Line 157 of Round 2 review report (`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_2.md`):
     > "**状态：已跳过**（用户未提交至 paperreview.ai）"
     > (Status: Skipped (user did not submit to paperreview.ai))

2. **MCP Tool Status Logs**
   - The project logs show that `mcp__agent-ml-research__get_external_review_status` was called and returned:
     ```
     "status": "not_requested"
     "message": "No external review requested."
     ```
   - This indicates external review has never been requested for this project.

3. **Configuration Pattern**
   - The expected configuration key would be `external_review.paperreview_ai.enabled` (as referenced in the review reports)
   - This appears to be part of a larger MCP-based research project configuration system
   - No actual YAML/JSON/TOML configuration file in the project directory contains this setting

### Conclusion

**External review is NOT enabled** for the `exec-sim-repair-verifier` project. The configuration key `external_review.paperreview_ai.enabled` is either not set or defaults to disabled. The project uses an internal review system with Review Directors and Reviewers, but Stanford's Agentic Reviewer (paperreview.ai) integration was explicitly 
…[truncated 30 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Agent",
  "elapsed_ms": 27672
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-19T09:33:48.234213+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计方法**。\n\n## 论文信息\n- 标题: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n- 路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（各 section 分文件：abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n- 目标 venue: **EMNLP 2026**（ARR May 2026 cycle）\n- 截止日期: 2026-05-25\n- 格式要求: ACL style [review]，double-blind，Long paper 8 页正文 + unlimited references，Limitations 必须是独立 section（不是 paragraph），ARR Responsible NLP Checklist\n\n## 论文概述\n比较三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行系统比较。\n\n## 你的审查侧重\n1. **实验设计严谨性**：controlled comparison 的实际控制程度（checkpoint 选择、preprocessing、sequence length 等 confound 是否充分披露和量化）\n2. **统计方法**：TOST equivalence test 的 margin 选择正当性、clustered bootstrap 使用是否正确、多重比较校正、power analysis\n3. **Claims 与 evidence 的匹配度**：每个 contribution 是否有充分的实验证据支撑，是否存在 overclaim\n4. **内部一致性**：数据在不同 table/figure/text 之间是否一致\n5. **可复现性**：hyperparameters、seeds、evaluation protocol 的披露是否充分\n\n## 输出格式\n按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条，标记 S1/S2/...）\n- **Weaknesses**（逐条，标记 W1/W2/...，按严重程度排序：Must-Fix > Should-Fix > Minor）\n- **Questions**（需作者澄清的问题，标记 Q1/Q2/...）\n- **Missing References**（如有）\n- **Overall Assessment**（评分 + 置信度，参考 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n- **Detailed Comments**（逐节评论）",
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计方法**。\n\n## 论文信息\n- 标题: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n- 路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（各 section 分文件：abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n- 目标 venue: **EMNLP 2026**（ARR May 2026 cycle）\n- 截止日期: 2026-05-25\n- 格式要求: ACL style [review]，double-blind，Long paper 8 页正文 + unlimited references，Limitations 必须是独立 section（不是 paragraph），ARR Responsible NLP Checklist\n\n## 论文概述\n比较三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行系统比较。\n\n## 你的审查侧重\n1. **实验设计严谨性**：controlled comparison 的实际控制程度（checkpoint 选择、preprocessing、sequence length 等 confound 是否充分披露和量化）\n2. **统计方法**：TOST equivalence test 的 margin 选择正当性、clustered bootstrap 使用是否正确、多重比较校正、power analysis\n3. **Claims 与 evidence 的匹配度**：每个 contribution 是否有充分的实验证据支撑，是否存在 overclaim\n4. **内部一致性**：数据在不同 table/figure/text 之间是否一致\n5. **可复现性**：hyperparameters、seeds、evaluation protocol 的披露是否充分\n\n## 输出格式\n按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条，标记 S1/S2/...）\n- **Weaknesses**（逐条，标记 W1/W2/...，按严重程度排序：Must-Fix > Should-Fix > Minor）\n- **Questions**（需作者澄清的问题，标记 Q1/Q2/...）\n- **Missing References**（如有）\n- **Overall Assessment**（评分 + 置信度，参考 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n- **Detailed Comments**（逐节评论）",
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 406 · 2026-05-19T09:34:00.916876+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12682
}
```

</details>

---


### Tool call

_source line 407 · 2026-05-19T09:34:01.203310+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 写作质量 + 相关工作覆盖 + 格式合规**。\n\n## 论文信息\n- 标题: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n- 路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（各 section 分文件：abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n- 目标 venue: **EMNLP 2026**（ARR May 2026 cycle）\n- 截止日期: 2026-05-25\n- 格式要求: ACL style [review]，double-blind，Long paper 8 页正文 + unlimited references，Limitations 必须是独立 section（不是 paragraph），ARR Responsible NLP Checklist\n\n## 论文概述\n比较三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行系统比较。\n\n## 你的审查侧重\n1. **新颖性评估**：核心 contribution 的增量价值——是否超越了\"在相同设置下比较三种方法\"的基本实验报告？是否有可迁移的 insight/methodology？\n2. **写作质量**：\n   - 叙事线是否清晰连贯（问题→洞察→方法→验证）\n   - Abstract 是否在 30 秒内传达核心价值\n   - AI 写作痕迹检查（dash 使用、-ing phrases、过度分段、黑名单用词）\n   - 专有名词是否有定义\n3. **Related Work 覆盖**：\n   - 是否遗漏直接相关的近期工作\n   - 是否做了有效的 positioning（而非 survey 式堆砌）\n   - 引用数量是否达到目标会议水平\n4. **格式合规**：\n   - Limitations 是否为独立 section（ARR 要求）\n   - Checklist 是否认真填写\n   - 页数是否符合要求\n   - 匿名化是否完整（无自引泄露）\n5. **图表质量**：信息密度、可读性、caption 自包含性\n\n## 输出格式\n按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条，标记 S1/S2/...）\n- **Weaknesses**（逐条，标记 W1/W2/...，按严重程度排序：Must-Fix > Should-Fix > Minor）\n- **Questions**（需作者澄清的问题，标记 Q1/Q2/...）\n- **Missing References**（如有）\n- **Overall Assessment**（评分 + 置信度，参考 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n- **Detailed Comments**（逐节评论）",
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 写作质量 + 相关工作覆盖 + 格式合规**。\n\n## 论文信息\n- 标题: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n- 路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（各 section 分文件：abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n- 目标 venue: **EMNLP 2026**（ARR May 2026 cycle）\n- 截止日期: 2026-05-25\n- 格式要求: ACL style [review]，double-blind，Long paper 8 页正文 + unlimited references，Limitations 必须是独立 section（不是 paragraph），ARR Responsible NLP Checklist\n\n## 论文概述\n比较三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行系统比较。\n\n## 你的审查侧重\n1. **新颖性评估**：核心 contribution 的增量价值——是否超越了\"在相同设置下比较三种方法\"的基本实验报告？是否有可迁移的 insight/methodology？\n2. **写作质量**：\n   - 叙事线是否清晰连贯（问题→洞察→方法→验证）\n   - Abstract 是否在 30 秒内传达核心价值\n   - AI 写作痕迹检查（dash 使用、-ing phrases、过度分段、黑名单用词）\n   - 专有名词是否有定义\n3. **Related Work 覆盖**：\n   - 是否遗漏直接相关的近期工作\n   - 是否做了有效的 positioning（而非 survey 式堆砌）\n   - 引用数量是否达到目标会议水平\n4. **格式合规**：\n   - Limitations 是否为独立 section（ARR 要求）\n   - Checklist 是否认真填写\n   - 页数是否符合要求\n   - 匿名化是否完整（无自引泄露）\n5. **图表质量**：信息密度、可读性、caption 自包含性\n\n## 输出格式\n按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条，标记 S1/S2/...）\n- **Weaknesses**（逐条，标记 W1/W2/...，按严重程度排序：Must-Fix > Should-Fix > Minor）\n- **Questions**（需作者澄清的问题，标记 Q1/Q2/...）\n- **Missing References**（如有）\n- **Overall Assessment**（评分 + 置信度，参考 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n- **Detailed Comments**（逐节评论）",
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-19T09:34:02.930121+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1726
}
```

</details>

---


### Assistant

_source line 409 · 2026-05-19T09:34:18.425371+00:00_

两名 Reviewer 已部署，等待独立审稿结果返回。

- **Reviewer 1**（方法严谨性 + 实验设计 + 统计方法）— 已触发
- **Reviewer 2**（新颖性 + 写作质量 + 相关工作 + 格式）— 已触发

收到两人审稿后将进行交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 410 · 2026-05-19T09:39:31.774172+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性 + 实验设计 + 统计方法

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study"
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)

---

## Summary

本文系统比较了三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行实验。Function-level 三种方法近等效（TOST 验证）；repo-level CLS 大幅领先 CWM（19-26pp）。论文统计方法整体规范（clustered bootstrap、TOST、ICC），对 confounds 的透明度值得肯定，但 repo-level 的多重 confounds 累积以及若干方法论选择的合理性问题削弱了核心 claim 的因果归因力度。

---

## Strengths

**S1. 研究问题重要且适时。** Execution-free verification 的 formulation 选择是实际工程决策，目前缺乏 matched comparison。论文填补了这一空白，对从业者有直接指导价值。

**S2. Function-level 实验设计严谨。** 5 seeds、两个模型家族、TOST equivalence test + clustered bootstrap + ICC，统计工具链完整且正确使用。Qwen3 5-seed 数据充分支撑 function-level equivalence 结论。

**S3. 对 confounds 和 limitations 的透明度极高。** Section 5 (Threats to Validity) 和 Limitations section 系统性地列出了 checkpoint selection、eval sequence length、preprocessing、training regime 差异等 confounds，并量化了每个 confound 的 observed effect。这种诚实性在 empirical study 中难得。

**S4. Default assignment artifact 分析精彩。** Section 4.5 对 CWM 4B→8B "伪改善"的解构（unparseable rate 上升 → 更多 majority-class default → accuracy 虚增，parseable-only accuracy 实际下降）是本文最有洞察力的发现之一，展示了评估指标可以如何误导。

**S5. 消融设计充分。** LoRA rank ablation、matched-context ablation、training data downsample、majority voting ablation 系统排除了多个替代解释。Matched-context ablation 确认 input disparity 仅解释 <3% 的 CLS-CWM gap，是强有力的证据。

**S6. Failure mode taxonomy（Table 3）概念清晰。** 将 repo-level 退化分为 format collapse、decision collapse、aggregation penalty 三类，且展示同一模型家族在不同 configuration 下表现出不同 failure mode，这对理解 formulation × configuration 交互有实质贡献。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [Critical] TRAJ checkpoint selection 不一致，存在 cherry-picking 嫌疑。**
- 具体位置：Table 4 footnote (♦)，Section 4.5
- 问题：论文声明 NaN validation loss 时默认使用 final epoch checkpoint（Section 4.1："runs using truncate preprocessing produce NaN validation loss...defaulting to the final epoch checkpoint"）。CWM 所有 repo-level runs 均遵循此规则使用 final epoch。但 Qwen3-8B TRAJ 例外：明确选择了 epoch 2（72.92%）而非 Trainer 默认的 epoch 3（70.83%）。这一选择使 TRAJ 看起来与 CLS variant-level（72.92%）完全持平，但如果一致使用 final epoch，TRAJ 应为 70.83%。
- 为什么影响接收：选择性地为 TRAJ 破例选择更优 checkpoint 而不给 CWM 同等处理，违反了 controlled comparison 的核心原则。如果允许 TRAJ 选择非 default checkpoint，CWM 也应允许在多个 epoch 中选择最优。这个不一致直接影响 CLS-TRAJ 比较的 validity。
- 建议：(1) 所有 NaN val loss runs 统一使用同一 checkpoint 选择规则（final epoch 或 best-of-all-epochs）；(2) 如果要 report epoch 2 结果，必须同时 report CWM 的 epoch 2 结果作为对照；(3) 明确说明 epoch 2 选择的 a priori 理由。

**W2. [Critical] Table 4 混合不同粒度指标且视觉区分不足，容易误导。**
- 具体位置：Table 4
- 问题：Table 4 在同一行中并排报告 CLS/CWM 的 per-test accuracy（n=9,784）和 TRAJ 的 variant-level accuracy（n=48）。尽管有 footnote (‡) 说明，但表格主体视觉上暗示这些数字可比。实际上 CLS variant-level accuracy 远低于其 per-test accuracy（e.g., Qwen3-4B: 83.63% per-test vs 64.58% variant-level），如果读者将 CLS per-test (83.63%) 与 TRAJ variant-level (72.92%) 直接比较，会严重高估 CLS 相对 TRAJ 的优势。
- 为什么影响接收：Table 4 是论文最核心的结果表，粒度混淆会导致读者对 formulation 相对优劣的判断产生根本性误解。
- 建议：(1) 在 Table 4 中增加 CLS variant-level 列，或 (2) 将 TRAJ 移至单独的 variant-level comparison table，或 (3) 至少在 TRAJ 列标题中加粗标注 "variant-level"。

**W3. [Critical] TOST equivalence margin 缺乏 a priori 正当性。**
- 具体位置：Section 4.4，Appendix E (Table 7)
- 问题：±2pp margin 的选择被事后合理化为"30% headroom above the minimum equivalence margin (±1.52pp)"和"~15 additional errors per 900 predictions"。但 equivalence testing 的标准做法是 a priori 根据 practical significance 确定 margin，而非先看数据再选能通过检验的 margin。Table 7 (sensitivity analysis) 显示 ±1.5pp 时 p=0.054（borderline fail），表明 equivalence 结论对 margin 选择非常敏感。
- 为什么影响接收：TOST 是支撑 Contribution 1（formulation equivalence）和 Contribution 4（diagnostic granularity at no cost）的核心统计证据。如果 margin 选择不充分 justified，这两个 contribution 的可信度受损。
- 建议：(1) 提供 a priori margin justification（如：基于 deployment scenario，2pp 以下的差异在实际 pipeline 中不影响决策）；(2) 明确承认 margin sensitivity：equivalence 在 ±1.5pp 处 borderline fail；(3) 引用 equivalence testing 文献中关于 margin selection 的 best practice（如 Lakens 2017）。

### Should-Fix（影响评分但不一票否决）

**W4. [Major] Repo-level confounds 累积效应未讨论，削弱因果归因。**
- 具体位置：Section 5，Section 4.5
- 问题：论文正确识别了 5 个 confounds（checkpoint selection、eval seq_length、preprocessing、TRAJ training regime、CWM scale），并声称 "the repo-level CLS-CWM gap (19-26pp) exceeds any individual confound's observed effect by an order of magnitude"（Section 5 最后一段）。但这个论证假设 confounds 独立作用且不 compound。实际上这些 confounds 可能交互：例如 truncate preprocessing 导致 NaN val loss → 不同 checkpoint selection → 不同 effective training set，形成 cascading confound chain。论文未分析 confounds 的联合效应。
- 建议：(1) 明确承认 confounds 可能 compound；(2) 提供 worst-case bounding（如：所有 confounds 同向叠加时，最多能解释多少 pp 的 gap）；(3) 或者将 repo-level 结论的措辞从 "formulation-driven" 弱化为 "consistent with a formulation-driven explanation under the tested conditions"。

**W5. [Major] 未进行多重比较校正。**
- 具体位置：全文
- 问题：论文进行了大量统计检验：CLS vs CWM scaling gap (p=0.0066)、TOST equivalence (p=0.007)、parseable bias χ² (p=5.9×10⁻¹⁰, p=3.3×10⁻¹⁸)、variant-level bootstrap (Table 8 多个 p 值)、ICC significance (p<0.0001) 等。没有讨论任何 family-wise error rate 或 false discovery rate 控制。虽然最核心的 p 值（TOST p=0.007、scaling p=0.0066）在 Bonferroni correction for ~10 tests 后仍显著（threshold 0.005），但论文应明确讨论这一点。
- 建议：(1) 列举论文中所有 inferential tests；(2) 报告 Holm-Bonferroni 或 BH adjusted p 值；(3) 或至少讨论为什么不需要 correction（如：每个 test 回答不同的 research question，correction 过于保守）。

**W6. [Major] Post-hoc power analysis 方法论不当。**
- 具体位置：Appendix F (Table 8)
- 问题：论文报告 post-hoc observed power（CLS-CWM mean power=0.87，CLS-TRAJ mean power=0.08）。Post-hoc power analysis 在统计方法论文献中被广泛批评为无信息量：observed power 是 p 值的单调函数，不提供 p 值以外的额外信息（Hoenig & Heisey 2001, "The Abuse of Power"）。对于显著结果（CLS-CWM），power 自然高；对于非显著结果（CLS-TRAJ），power 自然低——这是 tautological 的。
- 建议：(1) 删除 post-hoc power 或明确标注为 "retrospective" 并承认其局限性；(2) 替换为 a priori power analysis：给定 n=48，能检测到的最小效应量是多少？这已部分包含在 "minimum detectable effect at n=48: 25.0pp" 中，但应更突出；(3) 对 CLS-TRAJ 比较，报告 equivalence bound width 作为替代信息。

**W7. [Moderate] NF4 与 bf16 精度混合分析的合理性不充分。**
- 具体位置：Section 4.1, 4.2, 4.4
- 问题：5-seed 分析中 3 seeds (42/123/456) 用 bf16，2 seeds (789/0) 用 NF4。论文声称 "function-level accuracy remains within seed noise across both precisions"（Section 4.1），但未提供直接的精度对照（如 bf16 mean vs NF4 mean、precision × formulation 交互检验）。Table 2 限制为 bf16 seeds 以隔离 size effect，说明作者自己也认为 precision 是需要控制的变量，但在 TOST equivalence test（Section 4.4）和 Table 1 中却将两种精度混合。
- 建议：(1) 报告 bf16-only (3 seeds) 和 NF4-only (2 seeds) 的分别均值和标准差；(2) 验证 TOST 结论在 bf16-only subset 上仍成立；(3) 或提供 precision × formulation interaction test 以排除混杂。

**W8. [Moderate] Cross-model CWM 比较因 eval seq_length 不同而无效。**
- 具体位置：Table 4 footnote，Section 4.5 最后一段
- 问题：Qwen3 CWM 使用 eval seq_length 8192，DeepSeek CWM 使用 4096。论文自身展示 eval seq_length 导致 ~9pp variation（Section 5）。Table 4 footnote 承认 "cross-model CWM values are not directly comparable"，但正文的 "Cross-model consistency" 段落仍将两个模型的 CWM 结果作为 "consistent with a formulation-driven explanation" 的证据。
- 建议：(1) 在正文 "Cross-model consistency" 段落中更明确地限定：CWM cross-model consistency 不可评估（因 eval seq_length 不同）；(2) 只将 CLS cross-model consistency 作为证据；(3) 或提供 matched seq_length 的 DeepSeek CWM 结果。

### Minor（不影响接收）

**W9.** Prompt templates 未展示（CLS 的 pass/fail prompt、CWM 的 output generation prompt、TRAJ 的 resolved/unresolved prompt）。Prompt 措辞可能影响 formulation performance，这对 reproducibility 和 "formulation-driven" 归因均有影响。建议在 Appendix 中完整展示。

**W10.** Table 1 的 TRAJ 在不同 test set 上评估（1,032-sample subset vs CLS/CWM 的 1,890-sample full set），这一差异仅在 caption 中提及。建议更突出标注，或报告 CLS/CWM 在相同 1,032-sample subset 上的 accuracy 作为 sanity check。

**W11.** Mutation operators（operator_swap、off_by_one、return_value、boundary_removal）的选择和实现未充分描述。不同 mutation operators 的难度差异显著（Table 9 和 Table 10），但 operator 选择的理由和 operator 实现细节缺失。

**W12.** Re-repair pilot（Appendix A.7(j)，n=44，p=0.42）的 sample size 太小（power ~0.3 for medium effect）。建议要么扩大样本量，要么删除此 pilot——当前结论（"per-test diagnostic information does not automatically translate to repair improvements"）基于严重 underpowered 的检验，不具信息量。

**W13.** Oracle ensemble result (90.63%) 仅报告 seed 42 单种子。如果 error complementarity 是一个贡献点，应报告多 seed 的 oracle accuracy 及其变异。

---

## Questions

**Q1.** Qwen3-8B TRAJ 为什么选择 epoch 2 而非 final epoch？是 a priori 的决定还是在看到 epoch 3 结果后做出的？如果是后者，CWM 是否也检查了多个 epoch？

**Q2.** Function-level TOST equivalence 限制为 bf16 seeds（排除 NF4 seeds 789/0）后，p 值和结论是否仍然成立？

**Q3.** CLS 和 CWM 的 prompt template 是否经过优化？如果 CWM prompt 指导模型 "predict the exact output string" 而 CLS prompt 指导 "predict pass or fail"，prompt 设计本身是否可能是差异来源之一？

**Q4.** Variant-level evaluation 仅 n=48。是否考虑过使用更多 SWE-bench instances 来增加 variant-level power？48 个 variants 的选择标准是什么？

**Q5.** Table 3 的 fail recall range 跨 configuration 变化极大（~14% to ~57%）。这种变异中有多少可归因于 formulation，多少归因于 preprocessing / checkpoint selection？是否有 controlled comparison 能分离这两个因素？

**Q6.** DeepSeek-Coder 的 learning rate（2×10⁻⁴）比 Qwen3（5×10⁻⁵）高 4 倍。这一差异的 tuning 过程是怎样的？是否在相同的 validation split 上 tuned？Learning rate 差异是否可能是 cross-model 差异的来源之一？

---

## Missing References

1. **Lakens (2017)**, "Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses" — TOST margin selection 的 standard reference，应在讨论 margin justification 时引用。
2. **Hoenig & Heisey (2001)**, "The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis" — 如果保留 post-hoc power analysis，应引用此文并讨论其局限性。
3. **Constrained decoding 文献**: 论文仅引用 Willard & Louf (2023) 的 Outlines，但 grammar-constrained decoding 领域有更多近期工作（如 guidance, lm-format-enforcer）。鉴于论文将 constrained decoding 作为 CWM 可能的改善方向讨论，引用应更充分。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | Function-level 统计方法规范（clustered bootstrap、TOST、ICC 正确使用）；repo-level 多重 uncontrolled confounds 累积削弱因果归因；TRAJ checkpoint selection 不一致（W1）；TOST margin 缺乏 a priori justification（W3）；无多重比较校正（W5）。整体 methodology 框架合理但执行中的不一致性影响可信度。|
| **Excitement** | 3/5 | 研究问题实用且适时，对从业者有直接指导价值。Function-level equivalence 虽有统计支撑但略 expected。Repo-level divergence 发现有趣但结论高度 conditioned on 具体实验配置。Error complementarity 和 failure mode taxonomy 有启发性但不够 deep。整体为 solid empirical work，非 groundbreaking。|
| **Reproducibility** | 3/5 | Hyperparameters 详尽（Appendix Table 5）；seeds 明确报告。但 prompt templates 缺失（W9）、mutation operator 实现细节不足（W11）、CWM output parsing 逻辑未描述、software versions 缺失（Checklist C4 自认）。当前无法完全复现实验。|
| **Reviewer Confidence** | 4/5 | 熟悉 equivalence testing、bootstrap methods、LoRA fine-tuning 和 code verification 领域。对 SWE-bench 具体实现细节了解有限。|

---

## Overall Assessment

**Overall: 3.0 (Findings)**

**Confidence: 4/5**

**一句话总结**: 研究问题重要，function-level 实验设计严谨，但 repo-level 多重 confounds 的累积效应、TRAJ checkpoint selection 不一致（W1）、以及核心统计检验（TOST）的 margin 缺乏 a priori 正当性（W3）共同限制了论文最核心 claim 的因果归因力度，定位为 Findings 水平。

**判断理由**:
- Function-level equivalence 结论 well-supported，是 solid contribution，但 somewhat expected（formulation 在简单 task 上趋同不令人意外）。
- Repo-level divergence（19-26pp）效应量很大，即使考虑 confounds 也可能部分真实，但论文自身列出的 5 个 confounds + checkpoint selection 不一致使得"formulation-driven"归因只能是 tentative 的。
- Error complementarity 仅限 function-level 单 seed，preliminary。
- 论文对 limitations 的透明度值得肯定，但透明地列出问题不等于解决了问题。
- 整体贡献是 useful empirical evidence，但 generalizability（仅 2 model families、≤8B、LoRA regime）和 causal inference 力度不足以支撑 main conference acceptance。

---

## Detailed Comments（逐节）

### Abstract
- 措辞准确，未 overclaim。"consistent across model families but model-contingent in magnitude" 是恰当的 hedging。
- "configuration-dependent aggregation cost at repository level" 准确反映了数据。

### Introduction
- Contribution list 每条都有对应 section/table 支撑。
- Contribution 2 的措辞（"Evidence for complexity-dependent divergence with identified confounds"）诚实地承认了 confounds，这比 overclaim 好。
- 但 Contribution 3（error complementarity）仅基于 function-level 单 seed，contribution claim 的 weight 与 evidence 不对称。

### Method (Section 3)
- Formulation 定义清晰，notation 一致。
- Section 3.2 failure mode 分析是合理的 a priori prediction，后续实验验证了大部分预测。
- Section 3.3 oracle framework：使用 function-level ICC（0.191）估算 repo-level oracle advantage 是 conservative 的（repo-level ICC=0.3146 更高），论文正确标注了这一点。

### Experiments (Section 4)
- Section 4.1 Setup: 数据集描述清楚，split 和 baseline 完整。"zero problem overlap" 是重要的正面设计。
- Section 4.2 Function-level: 最 solid 的部分，5-seed、两个模型家族、appropriate statistical tests。
- Section 4.3 Scaling: 仅 2 seeds（42/123），bf16 only。CWM flat scaling 的解释（"may reflect suboptimal hyperparameter transfer"）是合理的 hedging。但 clustered bootstrap 的 "3-seed superset" 是否包含 seed 456？如果是，为什么 Table 2 只用 2 seeds 但统计检验用 3 seeds？这需要澄清（可能 seed 456 没有 8B 数据，仅用于 4B 的 CLS/CWM 对比）。
- Section 4.4 TOST: 统计方法本身正确，但 margin justification 问题（W3）。
- Section 4.5 Repo-level: 最大的 confound 集中区。Table 4 混合指标问题（W2）。Default assignment artifact 分析是亮点。
- Section 4.6 Analysis: Aggregation penalty 分析深入且有实际价值。Checkpoint selection confound（val-best 优化 per-test accuracy 但 penalize variant-level）是重要观察。
- Section 5 Threats: 全面且诚实。唯一缺失是 confound 累积效应（W4）。

### Related Work
- 覆盖充分，归类合理。PRM/ORM 类比恰当。
- 未涉及 constrained decoding 的更广泛文献（minor）。

### Conclusion
- 未 overclaim，recommendation 条件化于 "under standard LoRA fine-tuning (≤8B)"。
- Limitations section 是独立 section（符合 ARR 要求），内容充实。

### Appendix
- Ablation studies 系统且有价值。
- Variant-level accuracy table（Table 6）应在正文中更突出（目前是理解 Table 4 的必要补充）。
- Qualitative error analysis（Appendix C）有助于理解 failure mode 的具体机制。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 411 · 2026-05-19T09:39:38.096328+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成独立审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 412 · 2026-05-19T09:39:43.262191+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。

主要发现：
- **Function-level** 实验设计严谨（5 seeds、TOST + clustered bootstrap + ICC），结论可信
- **Repo-level** 存在三个 critical 问题：(1) TRAJ checkpoint 选择不一致——CWM 被迫用 final epoch 但 TRAJ 特选了 epoch 2，有 cherry-picking 嫌疑；(2) Table 4 混合 per-test 与 variant-level 指标易误导读者；(3) TOST ±2pp margin 缺乏 a priori 正当性，sensitivity analysis 显示 ±1.5pp 处 borderline fail
- **统计方法**层面：无多重比较校正、post-hoc power analysis 方法论不当、NF4/bf16 混合分析未充分验证
- 论文对 limitations 的透明度是显著优点，但 confounds 的 cumulative effect 未被讨论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 413 · 2026-05-19T09:39:49.529106+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 36

## Round 36

6 recorded events


### User

_source line 414 · 2026-05-19T09:44:40.810969+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿报告

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性 + 写作质量 + 相关工作覆盖 + 格式合规 + 图表质量

---

## Summary

本文系统比较了三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），在两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（function-level、repo-level）上进行了多种子实验。核心发现：function-level 三种方法准确率等价；repo-level 下 CLS 以 19-26pp 的优势大幅超越 CWM。论文的统计方法论（TOST 等价检验、clustered bootstrap、ICC）在 function-level 上很扎实，但 repo-level 的核心发现主要依赖单种子实验，且 CWM baseline 与原始 32B CWM 存在本质差距。

---

## 总体评分

**Overall**: **3.0 (Findings)**
**一句话总结**: 方法论扎实的实验比较研究，但超出页数限制、CWM baseline 过弱、repo-level 单种子这三个问题共同削弱了论文的核心贡献。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | Function-level 统计方法论优秀（5 seeds, TOST, bootstrap）；repo-level 最核心的发现受单种子、CWM baseline 过弱、TRAJ 训练不对称等混淆因素限制，论文诚实地承认了这些问题但未解决 |
| Excitement | 3/5 (Interesting) | 填补了 matched comparison 的空白，failure mode taxonomy 和 error complementarity 有实用价值；但无新方法提出，核心发现（分类在长输出场景优于生成）从 autoregressive error compounding 原理可预期 |
| Reproducibility | 3/5 | 超参数详尽报告（Appendix Table 7），但未提及代码/数据发布计划；数据构建过程（mutation pipeline）描述不够详细以完整复现 |
| Confidence | 4/5 | 仔细阅读了全文和附录，技术细节在我的专业范围内 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文超出 ARR Long Paper 8 页限制
- 具体位置：PDF 全文
- 问题：通过 PDF 渲染验证，正文内容（Abstract 至 Conclusion + Limitations）约占 11 页，References 从第 11 页下半开始。ARR Long Paper 限制为 8 页正文 + unlimited references/appendix。超出约 2-3 页。
- 为什么影响接收：超页数是 ARR 的硬约束，可能直接 desk reject。
- 建议修改方向：Experiments §5 极长（Setup + 6 个子节含 Threats to Validity），建议：(1) 将 Threats to Validity 移入 Appendix 并在正文简要概括；(2) 压缩 §5.4 Repo-Level 中 Default assignment artifact / Constrained decoding / Training and evaluation sensitivity 段落，将细节移入 Appendix；(3) 缩减 Introduction 贡献列表的详细数字。

**N2** [critical] CWM baseline 与原始 CWM 存在本质差距，削弱核心 claim
- 具体位置：§5.4, §5.6 Threats to Validity (CWM scale paragraph), Limitations
- 问题：本文使用 4-8B LoRA fine-tuned CWM，而原始 Code World Model (Meta, 2025) 使用 32B 参数 + execution trace mid-training。这不是同一个 formulation 的 fair comparison，而是一个严重 under-resourced 的 generation baseline。论文的核心 claim "formulation-dependent divergence" 同样可以被解释为 "generation formulation 需要更多 capacity/数据才能正常工作"。
- 为什么影响接收：这是论文最核心的结论（repo-level CLS >> CWM）的替代解释，且论文无法排除。Threats to Validity 承认了这一点（"at larger scale or with execution-trace pretraining, the generation bottleneck may diminish"），但这个 caveat 本质上 invalidates 了 repo-level 的 formulation-level 结论。
- 建议修改方向：(1) 在 framing 上更审慎：将结论限定为 "at ≤8B LoRA scale without execution-trace pretraining"，而非暗示 formulation 本身劣势；(2) 如果条件允许，增加一个中等规模的 CWM baseline（如 14B 或 with execution trace pretraining 的 smaller model）；(3) 至少引用 CWM 原文在更大规模下的性能数据作为上界参考。

**N3** [critical] Repo-level 核心发现主要依赖单种子
- 具体位置：Table 3 (repo_level), §5.4
- 问题：Qwen3 repo-level CLS vs CWM 比较为单种子 (s42)；Qwen3-8B 的两个配置 (s42/s123) 混淆了 seed、preprocessing、checkpoint selection。DeepSeek 虽有 2 seeds 但跨模型比较进一步引入 eval seq_length 不一致（Qwen3: 8192, DeepSeek: 4096）。repo-level variant 评估只有 n=48，power analysis 显示 CLS-TRAJ 比较 power 仅 0.08。
- 为什么影响接收：论文在 function-level 使用了 5 seeds + TOST 等严格统计标准，但 repo-level（论文最有价值的部分）退化到了单种子观察。这种方法论不对称使得最重要的结论也最不可靠。
- 建议修改方向：(1) 至少补充 Qwen3 repo-level 的第二个种子实验（CLS 和 CWM 各一个）；(2) 在 abstract 和 introduction 中更审慎地表述 repo-level 发现的确信度。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Related Work 以枚举代替定位
- 具体位置：§6 Related Work, 第一段（Execution Simulation and Verification）
- 问题：第一段本质是 "A proposed X, B proposed Y, C proposed Z ... None compare formulations at matched capacity" 的列表式写法。该段在约 8 行内堆砌了 18 个引用，缺乏对已有工作的系统归纳和本文在其中的定位分析。第二段（Process vs. Outcome Supervision）较好地将本文与 PRM/ORM 框架关联。第三段同样偏列表化。
- 建议：将第一段按 formulation 类型（generation-based、classification-based、trajectory/reward-based）重新组织，每类提炼共同点和局限性，再自然引出本文的 matched comparison motivation。

**W2** [warning] Abstract 数字密度过高
- 具体位置：abstract.tex
- 问题：Abstract（约 170 words）中包含 TOST p-value、pp margin、oracle ensemble 百分比、3 组准确率数字、种子数等大量数据。读起来像 results 摘要而非 compelling narrative。审稿人在 30 秒内难以从中判断核心价值。
- 建议：保留 1-2 个最关键的数字（如 function-level equivalence 和 repo-level 19-26pp gap），其余用定性描述替代。

**W3** [warning] TRAJ 比较存在严重混淆因素
- 具体位置：§5.6 Threats to Validity (TRAJ training regime), §5.3 (Equivalence)
- 问题：TRAJ 训练使用 ~400 variant-level instances（vs CLS/CWM 的 ~70K per-test instances），不同 learning rate（2e-4 vs 5e-5），variant-level evaluation（n=48 vs per-test n=9,784）。downsample ablation (80.74% vs 72.92%) 部分缓解了数据量问题，但 LR 和 evaluation 粒度的差异仍未控制。
- 建议：明确标注 CLS-TRAJ 比较为 preliminary/suggestive rather than conclusive，并在 contribution list 中相应降级。

**W4** [warning] Introduction 贡献列表过长
- 具体位置：§1, 贡献列表（4 条，每条含多个子点和具体数字）
- 问题：贡献列表总计约 350 words，接近一整段。每条贡献都包含了具体实验数据（百分比、pp gap、p-value），信息过密。第二条贡献（complexity-dependent divergence）单条就有 ~120 words，包含 Qwen3 和 DeepSeek 的具体退化数据和三种 failure mode 名称。
- 建议：贡献列表每条控制在 1-2 句话，具体数据留给 Results section。

**W5** [warning] "pp" 缩写未定义
- 具体位置：首次出现于 abstract.tex line 4（$\pm$2\pp{} margin）
- 问题：\pp{} 宏在全文广泛使用但从未定义为 "percentage points"。虽然 ML 领域读者多能理解，但首次出现应标注。

---

## 小问题（不影响接收）

- **M1**: 少量 trailing -ing phrases（"motivating complexity-aware routing over uniform formulation selection", abstract & conclusion），符合 AI 写作模式。建议改写。
- **M2**: Checklist C4 回答 "Partially"（package version numbers），建议提交前补全。
- **M3**: Table 3 脚注密度极高（$\dagger$, $\ddagger$, $\diamond$ 三个注释），影响可读性。考虑将部分说明移入正文。
- **M4**: Figure 1 caption 末句 "Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost" 属于一般性陈述，不如替换为具体的 tradeoff 量化。

---

## 主要优势

- **S1**: 首个在 matched conditions 下比较三种 verification formulation 的系统研究，填补了确实存在的文献空白（§1 correctly identifies this gap）。
- **S2**: Function-level 统计方法论极为扎实：5 seeds, TOST equivalence test ($p=0.007$, ±2pp margin), clustered bootstrap (114 clusters, 10K resamples), ICC + design effect 报告。这在 ML 实验论文中属于上游水准。
- **S3**: Threats to Validity (§5.6) 的诚实度和系统性罕见——逐一识别 5 个 confound 并定量评估其影响范围。多数论文不会主动暴露如此深度的局限性。
- **S4**: Failure mode taxonomy (Table 4: format collapse, decision collapse, aggregation penalty) 提供了可操作的诊断框架，对 practitioners 有直接价值。
- **S5**: 217× throughput advantage 的量化（§5.5 Analysis (i)）在实际部署中有重要参考意义。
- **S6**: 写作质量在 AI 风格检测维度良好：无 em-dash/en-dash，无黑名单用词（delve/leverage/utilize），无 transition word 滥用。
- **S7**: 引用完整，58 篇全部 cite-bib 对齐，OpenAlex 验证 46 篇确认真实，无幻觉引用。

---

## Questions（需作者澄清）

- **Q1**: 为什么不在更接近原始 CWM 规模的模型上测试（如 14B 或 32B）？如果是资源限制，请在论文中更明确地说明这一约束。
- **Q2**: 5 种 mutation types 如何选择？它们对真实 bug 的代表性如何？Synthetic-to-real transfer gap 是否有任何 pilot study？
- **Q3**: 论文声称 "execution-free verification"，但训练标签来自 execution。在实际部署中，获取大量 execution labels 用于 fine-tuning 的成本与直接执行验证相比如何？
- **Q4**: CWM 的 unparseable default-to-pass 策略是否公平？如果 default-to-fail，CWM 的 accuracy 会如何变化？这个选择显著影响了报告的 gap 大小。

---

## Missing References

引用覆盖总体充分（58 篇），以下方向可考虑补充：
- Chain-of-thought code verification：PatchReasoner 已引用但仅一笔带过；CoT-based verification 作为 CLS 和 CWM 之间的中间地带（multi-token output with reasoning trace），值得更深入讨论。
- 更多 grammar-constrained decoding for code 的工作（论文只引用了 Outlines），以支撑 §5.4 关于 constrained decoding 的论证。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度极高但叙事性不足。TOST $p$-value 和 oracle ensemble 百分比可留给正文。
- "motivating complexity-aware routing over uniform formulation selection" 是典型 trailing -ing phrase。

### Introduction
- §1 para 1-2 的问题定义和 gap identification 清晰有效。
- 贡献列表过于冗长（前述 W4），削弱了 Introduction 的 "hook" 效果。
- "The results reveal a three-layer structure" 的表述很有概括力，但随后展开的细节过多，应移至 §5。

### Method
- §2 的形式化定义清晰。failure mode 的先验分析（§2.2）是论文的亮点之一，为后续实验提供了 testable predictions。
- Oracle accuracy-utility framework (§2.3) 很好地连接了 per-test 和 trajectory-level 的理论优劣。

### Experiments
- 整体过长（占全文约 5-6 页），是超页数的主要原因。
- §5.1 Setup 条理清晰，train/val/test split 和 majority baseline 报告完整。
- §5.4 Repo-Level 包含了 7 个 \paragraph 级子节，信息密度高但读者难以跟踪主线。建议精简为 3 个核心点（divergence → failure modes → artifacts），将 sensitivity analysis 移入 Appendix。
- §5.5 Analysis 的 (k) aggregation penalty 分析深入，checkpoint selection confound 的发现有实际价值。
- §5.6 Threats to Validity 是论文最诚实的部分。

### Related Work
- 前述 W1。第一段需要从 enumeration 重写为 synthesis。
- PRM/ORM 的类比（第二段）处理得当。

### Conclusion
- 简洁有效，practical recommendations 段落有实用价值。

### Limitations
- 作为独立 \section* 存在，符合 ARR 要求。内容诚实全面。

### Checklist
- 总体认真填写。C4 的 "Partially" 需要在提交前补全 version numbers。

### Appendix
- 内容丰富（oracle analysis, ablations, variant-level, hyperparams, mutation breakdown, qualitative errors, extended analysis, TOST sensitivity, power analysis, parseable bias, extended limitations），共约 6 页。
- 与正文的交叉引用完整。
- 建议将部分当前正文内容（Threats to Validity, sensitivity analysis details）移入 Appendix 以解决超页问题。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 415 · 2026-05-19T09:45:35.217021+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Summary\n本文系统比较了三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行实验。Function-level 三种方法近等效（TOST 验证）；repo-level CLS 大幅领先 CWM（19-26pp）。论文统计方法整体规范（clustered bootstrap、TOST、ICC），对 confounds 的透明度值得肯定，但 repo-level 的多重 confounds 累积以及若干方法论选择的合理性问题削弱了核心 claim 的因果归因力度。\n\n## Strengths\nS1. 研究问题重要且适时。\nS2. Function-level 实验设计严谨。5 seeds、两个模型家族、TOST equivalence test + clustered bootstrap + ICC。\nS3. 对 confounds 和 limitations 的透明度极高。\nS4. Default assignment artifact 分析精彩。\nS5. 消融设计充分。\nS6. Failure mode taxonomy 概念清晰。\n\n## Weaknesses\n\n### Must-Fix\n\n**W1. [Critical] TRAJ checkpoint selection 不一致，存在 cherry-picking 嫌疑。**\nQwen3-8B TRAJ 选择了 epoch 2（72.92%）而非 Trainer 默认的 epoch 3（70.83%）。CWM 所有 repo-level runs 均使用 final epoch。这一选择使 TRAJ 看起来与 CLS variant-level 完全持平，但如果一致使用 final epoch，TRAJ 应为 70.83%。违反 controlled comparison 原则。\n\n**W2. [Critical] Table 4 混合不同粒度指标且视觉区分不足，容易误导。**\nTable 4 并排报告 CLS/CWM 的 per-test accuracy（n=9,784）和 TRAJ 的 variant-level accuracy（n=48）。粒度混淆会导致读者误判 formulation 相对优劣。\n\n**W3. [Critical] TOST equivalence margin 缺乏 a priori 正当性。**\n±2pp margin 被事后合理化。Table 7 (sensitivity analysis) 显示 ±1.5pp 时 p=0.054（borderline fail），表明 equivalence 结论对 margin 选择非常敏感。\n\n### Should-Fix\n\n**W4. [Major] Repo-level confounds 累积效应未讨论。**\n论文声称 gap 超过任何单个 confound，但假设了 confounds 独立作用。实际可能 compound。\n\n**W5. [Major] 未进行多重比较校正。**\n大量统计检验但无 family-wise error rate 或 FDR 控制。\n\n**W6. [Major] Post-hoc power analysis 方法论不当。**\nObserved power 是 p 值的单调函数，不提供额外信息（Hoenig & Heisey 2001）。\n\n**W7. [Moderate] NF4 与 bf16 精度混合分析的合理性不充分。**\n5-seed 中 3 用 bf16、2 用 NF4，但未报告分别均值和交互检验。\n\n**W8. [Moderate] Cross-model CWM 比较因 eval seq_length 不同而无效。**\nQwen3 CWM eval 8192 vs DeepSeek 4096，但正文仍作为 consistency 证据使用。\n\n### Minor\n**W9.** Prompt templates 未展示。\n**W10.** TRAJ 在不同 test set 上评估（1,032 vs 1,890）。\n**W11.** Mutation operators 选择和实现描述不足。\n**W12.** Re-repair pilot n=44 太小。\n**W13.** Oracle ensemble 仅报告单 seed。\n\n## Questions\nQ1. TRAJ epoch 2 选择是 a priori 还是 post-hoc？\nQ2. TOST 限制为 bf16 seeds 后结论是否成立？\nQ3. Prompt templates 是否经过优化？\nQ4. n=48 variants 的选择标准是什么？\nQ5. Fail recall 变异中多少可归因于 formulation vs configuration？\nQ6. DeepSeek LR 4x 差异的 tuning 过程？\n\n## Missing References\n1. Lakens (2017) — TOST margin selection\n2. Hoenig & Heisey (2001) — post-hoc power criticism\n3. 更多 constrained decoding 文献\n\n## Overall Assessment\n**3.0 (Findings)**, Confidence 4/5",
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Summary\n本文系统比较了三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行实验。Function-level 三种方法近等效（TOST 验证）；repo-level CLS 大幅领先 CWM（19-26pp）。论文统计方法整体规范（clustered bootstrap、TOST、ICC），对 confounds 的透明度值得肯定，但 repo-level 的多重 confounds 累积以及若干方法论选择的合理性问题削弱了核心 claim 的因果归因力度。\n\n## Strengths\nS1. 研究问题重要且适时。\nS2. Function-level 实验设计严谨。5 seeds、两个模型家族、TOST equivalence test + clustered bootstrap + ICC。\nS3. 对 confounds 和 limitations 的透明度极高。\nS4. Default assignment artifact 分析精彩。\nS5. 消融设计充分。\nS6. Failure mode taxonomy 概念清晰。\n\n## Weaknesses\n\n### Must-Fix\n\n**W1. [Critical] TRAJ checkpoint selection 不一致，存在 cherry-picking 嫌疑。**\nQwen3-8B TRAJ 选择了 epoch 2（72.92%）而非 Trainer 默认的 epoch 3（70.83%）。CWM 所有 repo-level runs 均使用 final epoch。这一选择使 TRAJ 看起来与 CLS variant-level 完全持平，但如果一致使用 final epoch，TRAJ 应为 70.83%。违反 controlled comparison 原则。\n\n**W2. [Critical] Table 4 混合不同粒度指标且视觉区分不足，容易误导。**\nTable 4 并排报告 CLS/CWM 的 per-test accuracy（n=9,784）和 TRAJ 的 variant-level accuracy（n=48）。粒度混淆会导致读者误判 formulation 相对优劣。\n\n**W3. [Critical] TOST equivalence margin 缺乏 a priori 正当性。**\n±2pp margin 被事后合理化。Table 7 (sensitivity analysis) 显示 ±1.5pp 时 p=0.054（borderline fail），表明 equivalence 结论对 margin 选择非常敏感。\n\n### Should-Fix\n\n**W4. [Major] Repo-level confounds 累积效应未讨论。**\n论文声称 gap 超过任何单个 confound，但假设了 confounds 独立作用。实际可能 compound。\n\n**W5. [Major] 未进行多重比较校正。**\n大量统计检验但无 family-wise error rate 或 FDR 控制。\n\n**W6. [Major] Post-hoc power analysis 方法论不当。**\nObserved power 是 p 值的单调函数，不提供额外信息（Hoenig & Heisey 2001）。\n\n**W7. [Moderate] NF4 与 bf16 精度混合分析的合理性不充分。**\n5-seed 中 3 用 bf16、2 用 NF4，但未报告分别均值和交互检验。\n\n**W8. [Moderate] Cross-model CWM 比较因 eval seq_length 不同而无效。**\nQwen3 CWM eval 8192 vs DeepSeek 4096，但正文仍作为 consistency 证据使用。\n\n### Minor\n**W9.** Prompt templates 未展示。\n**W10.** TRAJ 在不同 test set 上评估（1,032 vs 1,890）。\n**W11.** Mutation operators 选择和实现描述不足。\n**W12.** Re-repair pilot n=44 太小。\n**W13.** Oracle ensemble 仅报告单 seed。\n\n## Questions\nQ1. TRAJ epoch 2 选择是 a priori 还是 post-hoc？\nQ2. TOST 限制为 bf16 seeds 后结论是否成立？\nQ3. Prompt templates 是否经过优化？\nQ4. n=48 variants 的选择标准是什么？\nQ5. Fail recall 变异中多少可归因于 formulation vs configuration？\nQ6. DeepSeek LR 4x 差异的 tuning 过程？\n\n## Missing References\n1. Lakens (2017) — TOST margin selection\n2. Hoenig & Heisey (2001) — post-hoc power criticism\n3. 更多 constrained decoding 文献\n\n## Overall Assessment\n**3.0 (Findings)**, Confidence 4/5",
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 416 · 2026-05-19T09:46:02.857618+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27640
}
```

</details>

---


### Tool call

_source line 417 · 2026-05-19T09:46:03.011052+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Summary\n本文系统比较了三种 execution-free code verification formulation（CLS、CWM、TRAJ），在两个模型家族、两个复杂度级别上进行了多种子实验。核心发现：function-level 等价；repo-level CLS 大幅超越 CWM（19-26pp）。统计方法在 function-level 扎实，但 repo-level 核心发现主要依赖单种子实验，且 CWM baseline 与原始 32B CWM 存在本质差距。\n\n## Strengths\nS1. 首个 matched comparison，填补文献空白。\nS2. Function-level 统计方法论极为扎实。\nS3. Threats to Validity 诚实度和系统性罕见。\nS4. Failure mode taxonomy 有实操价值。\nS5. 217× throughput 量化有部署参考意义。\nS6. 写作无 AI 风格痕迹（无 em-dash、黑名单用词等）。\nS7. 引用完整，58 篇全部验证无幻觉引用。\n\n## Must-Fix\n\n**N1 [critical] 正文超出 ARR Long Paper 8 页限制**\n通过 PDF 渲染验证，正文内容约占 11 页。超出约 2-3 页。ARR 的硬约束，可能直接 desk reject。建议将 Threats to Validity 移入 Appendix，压缩 Repo-Level 细节。\n\n**N2 [critical] CWM baseline 与原始 CWM 存在本质差距**\n4-8B LoRA ≠ 32B mid-trained CWM。核心 claim \"formulation-dependent divergence\" 可被解释为 \"generation 需要更多 capacity/数据\"。Threats to Validity 承认了这一点但本质上 invalidates repo-level 的 formulation-level 结论。\n\n**N3 [critical] Repo-level 核心发现主要依赖单种子**\nQwen3 repo-level CLS vs CWM 为单种子 (s42)；variant 评估只有 n=48。方法论不对称使最重要的结论也最不可靠。\n\n## Should-Fix\n\n**W1 [warning] Related Work 以枚举代替定位**\n第一段 8 行内堆砌 18 个引用，缺乏系统归纳和定位分析。\n\n**W2 [warning] Abstract 数字密度过高**\n约 170 words 中包含大量数据，读起来像 results 摘要而非 compelling narrative。\n\n**W3 [warning] TRAJ 比较存在严重混淆因素**\n训练数据量 ~400 vs ~70K，不同 LR，不同 evaluation 粒度。downsample ablation 部分缓解但 LR 和 evaluation 差异未控制。\n\n**W4 [warning] Introduction 贡献列表过长**\n4 条共约 350 words，每条含具体数字，信息过密。\n\n**W5 [warning] \"pp\" 缩写未定义**\n\\pp{} 全文广泛使用但从未定义。\n\n## Minor\nM1. 少量 trailing -ing phrases。\nM2. Checklist C4 \"Partially\"。\nM3. Table 3 脚注密度极高。\nM4. Figure 1 caption 末句过于一般性。\n\n## Questions\nQ1. 为什么不在更接近原始 CWM 规模的模型上测试？\nQ2. Mutation types 选择标准？Synthetic-to-real transfer gap？\nQ3. 训练标签来自 execution，获取 execution labels 的成本 vs 直接执行验证？\nQ4. CWM unparseable default-to-pass 策略是否公平？default-to-fail 会如何？\n\n## Missing References\n- Chain-of-thought code verification 更深入讨论\n- 更多 grammar-constrained decoding 文献\n\n## Overall Assessment\n**3.0 (Findings)**, Confidence 4/5",
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Summary\n本文系统比较了三种 execution-free code verification formulation（CLS、CWM、TRAJ），在两个模型家族、两个复杂度级别上进行了多种子实验。核心发现：function-level 等价；repo-level CLS 大幅超越 CWM（19-26pp）。统计方法在 function-level 扎实，但 repo-level 核心发现主要依赖单种子实验，且 CWM baseline 与原始 32B CWM 存在本质差距。\n\n## Strengths\nS1. 首个 matched comparison，填补文献空白。\nS2. Function-level 统计方法论极为扎实。\nS3. Threats to Validity 诚实度和系统性罕见。\nS4. Failure mode taxonomy 有实操价值。\nS5. 217× throughput 量化有部署参考意义。\nS6. 写作无 AI 风格痕迹（无 em-dash、黑名单用词等）。\nS7. 引用完整，58 篇全部验证无幻觉引用。\n\n## Must-Fix\n\n**N1 [critical] 正文超出 ARR Long Paper 8 页限制**\n通过 PDF 渲染验证，正文内容约占 11 页。超出约 2-3 页。ARR 的硬约束，可能直接 desk reject。建议将 Threats to Validity 移入 Appendix，压缩 Repo-Level 细节。\n\n**N2 [critical] CWM baseline 与原始 CWM 存在本质差距**\n4-8B LoRA ≠ 32B mid-trained CWM。核心 claim \"formulation-dependent divergence\" 可被解释为 \"generation 需要更多 capacity/数据\"。Threats to Validity 承认了这一点但本质上 invalidates repo-level 的 formulation-level 结论。\n\n**N3 [critical] Repo-level 核心发现主要依赖单种子**\nQwen3 repo-level CLS vs CWM 为单种子 (s42)；variant 评估只有 n=48。方法论不对称使最重要的结论也最不可靠。\n\n## Should-Fix\n\n**W1 [warning] Related Work 以枚举代替定位**\n第一段 8 行内堆砌 18 个引用，缺乏系统归纳和定位分析。\n\n**W2 [warning] Abstract 数字密度过高**\n约 170 words 中包含大量数据，读起来像 results 摘要而非 compelling narrative。\n\n**W3 [warning] TRAJ 比较存在严重混淆因素**\n训练数据量 ~400 vs ~70K，不同 LR，不同 evaluation 粒度。downsample ablation 部分缓解但 LR 和 evaluation 差异未控制。\n\n**W4 [warning] Introduction 贡献列表过长**\n4 条共约 350 words，每条含具体数字，信息过密。\n\n**W5 [warning] \"pp\" 缩写未定义**\n\\pp{} 全文广泛使用但从未定义。\n\n## Minor\nM1. 少量 trailing -ing phrases。\nM2. Checklist C4 \"Partially\"。\nM3. Table 3 脚注密度极高。\nM4. Figure 1 caption 末句过于一般性。\n\n## Questions\nQ1. 为什么不在更接近原始 CWM 规模的模型上测试？\nQ2. Mutation types 选择标准？Synthetic-to-real transfer gap？\nQ3. 训练标签来自 execution，获取 execution labels 的成本 vs 直接执行验证？\nQ4. CWM unparseable default-to-pass 策略是否公平？default-to-fail 会如何？\n\n## Missing References\n- Chain-of-thought code verification 更深入讨论\n- 更多 grammar-constrained decoding 文献\n\n## Overall Assessment\n**3.0 (Findings)**, Confidence 4/5",
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 418 · 2026-05-19T09:46:04.648325+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1637
}
```

</details>

---


### Assistant

_source line 419 · 2026-05-19T09:46:07.289472+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 37

## Round 37

2 recorded events


### User

_source line 420 · 2026-05-19T09:46:09.961347+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**，三个 Must-Fix 问题：

1. **正文超页**（~11 页，ARR 限制 8 页）——可能直接 desk reject
2. **CWM baseline 过弱**（4-8B LoRA vs 原始 32B + execution trace mid-training），无法排除 "capacity 不足" 的替代解释
3. **Repo-level 核心发现依赖单种子**，与 function-level 的 5-seed 严格标准形成方法论不对称

优势方面：function-level 统计方法论扎实（TOST、clustered bootstrap、ICC），failure mode taxonomy 有实用价值，Threats to Validity 的诚实度罕见，写作无 AI 风格痕迹，引用完整无幻觉。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 421 · 2026-05-19T09:46:14.989185+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 422 · 2026-05-19T09:48:13.434127+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix

**[AGREE] R2-N1: 正文超出 ARR Long Paper 8 页限制**
同意这是 critical issue。ARR Long Paper 硬约束 8 页正文 + unlimited references/appendix，超出可能导致 desk reject。论文 experiments section 含 5 个 subsection + 5 张 table + 2 张 figure，加上 Method 和 Threats to Validity section，页数超标几乎可以确定。建议：(1) Section 5 (Threats to Validity) 整体移入 Appendix，正文保留一段概述；(2) Section 4.5 (Repo-Level) 的 "Default assignment artifact"、"Constrained decoding"、"Training and evaluation sensitivity" 段落移入 Appendix；(3) Section 4.6 (Analysis) 的 aggregation penalty 详细数据移入 Appendix。这是提交前必须修复的格式硬伤。

**[REBUT] R2-N2: CWM baseline 与原始 CWM 存在本质差距 → "invalidates repo-level formulation-level conclusions"**
R2 的 concern 合理但 "invalidates" 过强。三点反驳：

(1) **论文从未声称无条件 formulation 优势**。Conclusion 明确写道 "At repository level under standard LoRA fine-tuning (≤8B), CLS is strongly preferred"（Section 6），Threats to Validity 写道 "all repo-level CWM conclusions are conditional on the ≤8B LoRA regime"（Section 5 最后一段）。论文的 claim 是 **conditioned on the tested regime** 的，不是 universal 的。

(2) **Matched comparison 的价值在于 formulation isolation，不在于 SOTA 复现**。论文 Introduction 明确说 "Our CWM baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model"（Section 4.1）。如果用 32B CWM 对比 4B CLS，那才是真正不公平的比较——模型容量差异会 confound formulation 效应。

(3) **即使 generation 在更大 scale 可能改善，论文的发现对 4-8B 实践者仍有直接价值**。很多部署场景受限于 ≤8B 模型（边缘推理、成本约束），在这个 regime 下 CLS > CWM 的结论是 actionable 的。

但我同意 R2 的隐含建议：论文应更突出这一条件限制（不仅在 Threats 中提及，也应在 Abstract 和 Introduction contribution list 中加入 conditioning），避免读者误读为 universal claim。

**[AGREE with nuance] R2-N3: Repo-level 核心发现主要依赖单种子**
同意这是 significant limitation。补充我的 R1 审稿中相关观察：

- Repo-level CLS-CWM 对比确实主要为 Qwen3 single seed (s42)。DeepSeek 作为 cross-model check 也是 single seed per formulation。
- n=48 variant-level evaluation 的 minimum detectable effect = 25.0pp（Appendix F, Table 8），意味着只有极大效应才能被检测到。

但我认为 R2 将此标为 "最重要的结论也最不可靠" 略有过度：
- 效应量极大（19-26pp），远超 function-level seed noise（<2pp，Table 1/2）。即使 repo-level seed variance 是 function-level 的 3-5 倍（约 4-10pp），效应仍远超噪声。
- Cross-model 方向一致（两个模型家族均 CLS > CWM），虽然各自 single-seed，但 independent replication 的概率论意义是真实的。
- CLS-CWM variant-level bootstrap 95% CI lower bound = 10.42pp（Table 8），即使在最保守估计下 gap 仍 substantial。

**综合判断**：single-seed 确实是 limitation，但对于 19-26pp 的效应，单种子的 risk 远低于对 2pp 效应的单种子 risk。论文应增加 multi-seed repo-level 实验，或在无法增加时将 repo-level 结论的 claim strength 进一步降级（从 "evidence for divergence" 到 "preliminary evidence for divergence"）。

---

## Should-Fix

**[AGREE] R2-W1: Related Work 以枚举代替定位**
同意。Section 6 (Related Work) 第一段在约 8 行内堆砌了 ~21 个引用，形式上更接近 survey list 而非 positioning analysis。论文应更强调自身与 direct competitors 的具体差异（如：CWM paper 的 32B mid-training vs 本文的 matched LoRA comparison；SWE-RM 的 trajectory-level 设计 vs 本文的 per-test decomposition），减少每个工作仅占一个 phrase 的 listing。

**[AGREE] R2-W2: Abstract 数字密度过高**
同意。Abstract 约 170 words 中包含 p=0.007、±2pp、5 seeds、19-26pp、90.63%、+3.12pp、217× 等密集数据。EMNLP 审稿人在 30 秒内判断论文价值，当前 Abstract 读起来更像 compressed results section 而非 compelling narrative。建议保留核心效应量（function-level equivalence、repo-level 19-26pp gap），删减次要数字（p 值、oracle accuracy）。

**[AGREE] R2-W3: TRAJ 比较存在严重混淆因素**
同意，且与我的 R1-W1（TRAJ checkpoint selection 不一致）互为补充。TRAJ 与 CLS/CWM 之间的 confound 链比 R2 列出的还长：

1. 训练数据量：~400 variants vs ~70K instances（R2 已指出）
2. Learning rate：2×10⁻⁴ vs 5×10⁻⁵（R2 已指出）
3. Evaluation 粒度：variant-level (n=48) vs per-test (n=9,784)（R2 已指出）
4. Checkpoint selection：TRAJ Qwen3-8B 选择了 epoch 2 而非 Trainer 默认的 final epoch，但 CWM 遵循 final epoch default（我的 R1-W1）
5. Label granularity：variant-level binary labels vs per-test labels

Downsample ablation 仅控制了 #1，其余 4 个 confounds 均未控制。CLS-TRAJ 的 repo-level 比较严格来说是 uninterpretable 的。

**[AGREE] R2-W4: Introduction 贡献列表过长**
同意。4 条 contribution 共 ~350 words，每条含括号内具体数字（seeds 数、pp 值、CI）。这些数字在 Introduction 阶段是过度的——reader 尚未看到实验设计，无法评判这些数字的意义。建议：每条 contribution 压缩至 1-2 句，具体数字移至实验章节引用。

**[AGREE] R2-W5: "pp" 缩写未定义**
同意。\pp{} 在 Abstract 首次出现（"±2pp margin"）时未定义。"pp" = percentage points 是相对常见的缩写，但 ARR 审稿人来自多语言背景，不应假设所有人熟悉。建议首次使用时加注 "(percentage points, pp)"。

---

## Minor

**[AGREE] R2-M1:** Trailing -ing phrases。与我的审稿侧重不直接相关，但 AI 风格检查维度上 R2 的观察合理。

**[AGREE] R2-M2:** Checklist C4 "Partially" 确认，与我 R1-W9（reproducibility）一致。

**[AGREE] R2-M3:** Table 3/4 脚注密度确实极高，尤其 Table 4 的 4 个不同 footnote markers (†, ‡, ♦, 加上 a) 增加阅读负担。

**[AGREE] R2-M4:** Figure 1 caption 末句 ("Each formulation makes different tradeoffs...") 较为 generic，可以更具体。

---

## Questions 回应

**R2-Q1 (为什么不在更接近原始 CWM 规模的模型上测试):**
与 N2 相关。论文在 Threats to Validity 中承认了 scale limitation（Section 5 最后一段）。我认为这是合理的 compute constraint——32B mid-training 需要的资源量级与 4B LoRA 完全不同。但论文应更明确地将这一 compute constraint 列为 scope decision 而非 afterthought。

**R2-Q2 (Mutation types 选择标准):**
与我 R1-W11 一致。论文未充分说明 5 种 mutation operators 的选择理由。Table 9/10 显示 mutation types 间难度差异巨大（boundary_removal ~47% vs gold ~98%），选择不同的 mutation set 可能改变 overall accuracy ranking。

**R2-Q3 (训练标签来自 execution，获取成本 vs 直接执行):**
这是一个重要的 framing question，论文未充分 address。Execution-free verification 的价值前提是推理时不需要执行，但训练数据构建需要执行。论文 Introduction 提到执行成本 "$1-3 per candidate at repository scale"，但未量化训练数据构建的一次性成本 vs 推理时执行的重复成本。建议在 Introduction 或 Discussion 中加入简短的 cost-benefit 分析。

**[REBUT] R2-Q4 (CWM unparseable default-to-pass 策略是否公平):**
反驳。Default-to-pass 是**对 CWM 最有利**的策略选择：
- Majority class 是 pass (72.96%)，default-to-pass = default-to-majority，这是 CWM 的 best-case default（Section 4.5）。
- 论文 Appendix A.7(c) 明确证明 relaxed matching（尝试从 unparseable outputs 中提取更多信息）**反而降低** CWM accuracy（58.04%→56.98%），因为 unparseable predictions 的 majority-class default 比 model 自身的 parseable predictions 更准确。
- Default-to-fail 会使 CWM accuracy 进一步下降（unparseable rate 53-74% 的样本全部判 fail → 远低于 majority baseline）。
- 论文 Section 4.5 的 parseable bias analysis 进一步证实："correcting for this artifact would widen the CLS-CWM gap beyond the 19-26pp reported."

因此，当前 default-to-pass 策略是对 CWM 最 charitable 的处理，实际 gap 只会更大。R2 的 concern 方向反了。

---

## Missing References 回应

**[AGREE]** Chain-of-thought code verification 和 grammar-constrained decoding 文献确实可以补充。但这些是 depth of coverage 问题，不影响核心 contribution 的 validity。

---

## Overall Assessment 对齐

R2 给出 **3.0 (Findings)**，与我的 R1 评分一致。

两位 reviewer 的核心 concern 高度一致：
1. Repo-level confounds 累积（R1-W4, R2-N3）
2. CWM baseline scale limitation（R2-N2, 我在 R1 中作为 context 提及但未单独列为 weakness）
3. TRAJ 比较 confounds（R1-W1, R2-W3）
4. 页数超限（R2-N1, 我未检查 PDF 渲染故未提及但同意）

两位 reviewer 的主要分歧：
- R2-N2 认为 CWM scale gap "essentially invalidates" repo-level conclusions → 我认为 "invalidates" 过强，论文的 conditioned claim 是合理的
- R2-Q4 暗示 default-to-pass 可能不公平 → 我认为 default-to-pass 已是 CWM 最有利选择，方向相反


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 423 · 2026-05-19T09:48:34.607751+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 39

## Round 39

14 recorded events


### User

_source line 424 · 2026-05-19T09:48:35.969436+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 的逐条交叉回应，已提交给 Review Director。

核心结论：
- 与 R2 的 Overall 3.0 (Findings) 评分一致
- 大部分 Weaknesses 我 AGREE（页数超限、Related Work 枚举、TRAJ confounds、Abstract 数字密度等）
- 两处 REBUT：(1) R2-N2 说 CWM scale gap "invalidates" repo-level conclusions 过强，论文的 conditioned claim 合理；(2) R2-Q4 暗示 default-to-pass 对 CWM 不公平，实际上这是对 CWM 最 charitable 的策略

---

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的逐条回应

---

## Must-Fix

**[AGREE] R1-W1: TRAJ checkpoint selection 不一致**
同意这是一个有效的方法论问题。Table 3 脚注明确记录："Qwen3-8B TRAJ uses epoch 2 checkpoint (72.92%); NaN validation loss caused Trainer default to epoch 3 final (70.83%)"。论文的协议是：当 val loss 为 NaN 时使用 final epoch（所有 CWM repo-level runs 和 DeepSeek CLS s123 均遵循此协议，§5.1）。但 TRAJ 在同样条件下却手动选择了 epoch 2 而非 Trainer 默认的 epoch 3，构成协议不一致。

补充我的判断：实际影响有限（72.92% vs 70.83%，仅 2pp），且即使使用 70.83%，TRAJ 仍远高于 CWM（52-65%），不改变 CLS > CWM 的核心结论。但作为 controlled comparison 的方法论缺陷，确实需要修复。建议：(1) 统一使用 final epoch 作为 NaN val loss 的默认策略并报告两组数字；(2) 在正文中明确标注 epoch 2 选择是 post-hoc 的。

---

**[AGREE] R1-W2: Table 4 混合粒度指标**
同意。Table 3（论文中为 Table `repo_level`）的脚注 $\ddagger$ 标注了 TRAJ 为 variant-level (n=48) 而 CLS/CWM 为 per-test (n=9,784)，但这个标注在视觉上容易被忽略。补充：我在自己的审稿意见 W3 中也指出了 TRAJ 比较的严重混淆因素。建议将 Table 3 拆为两部分（per-test 比较 + variant-level 比较），或在表头用独立列明确区分评估粒度。

---

**[REBUT] R1-W3: TOST margin 缺乏 a priori 正当性**
部分不同意。R1 称 margin 是"事后合理化"，但论文在 §5.3 给出了实质性论证："a 2pp gap corresponds to ~15 additional errors per 900 predictions"，这是一个基于实际部署影响的实用标准，不是纯统计意义上的 a priori 但属于 domain-justified margin。TOST 的标准实践（Lakens 2017, 我同意 R1 建议补充此引用）允许基于 smallest effect size of interest (SESOI) 来设定 margin，±2pp 作为 SESOI 在代码验证场景中是合理的。

关键证据：Table `tost_sensitivity`（Appendix）显示最小等价 margin 为 ±1.52pp（p~0.05），±2pp 提供 ~30% headroom。在 ±1.5pp 时 p=0.054 确实 borderline，但这恰恰说明实际 gap 非常小（观测 gap 仅 -0.45pp）。如果 gap 本身 < 0.5pp，讨论 ±1.5pp vs ±2pp 的区别对实际决策几乎没有影响。

补充建议：作者应在 §5.3 中引用 Lakens (2017) 的 SESOI 框架，正式论证 ±2pp 的选择依据，并明确声明这是 a priori 设定还是基于 domain reasoning 的事后选择。

---

## Should-Fix

**[AGREE] R1-W4: Confounds 累积效应**
同意。§5.6 末段声称 "the repo-level CLS-CWM gap (19-26pp) exceeds any individual confound's observed effect by an order of magnitude"，但确实假设了 confounds 独立作用。Checkpoint selection (~2pp) + eval seq_length (~9pp for CWM) + preprocessing (~7.68pp) 理论上可以 compound。不过我补充一点：这些 confounds 大部分对 CWM 不利方向一致（都使 CWM 看起来更差），所以即使 compound，也不太可能反转 CLS > CWM 的方向——只是 gap 的精确大小不可靠。建议在 §5.6 增加一段讨论 worst-case compound scenario。

---

**[REBUT] R1-W5: 未进行多重比较校正**
这一点事实上不成立。论文 §5.1 Statistics 段明确说明："Holm-Bonferroni correction [Holm 1979] controls family-wise error rate across the four primary comparisons (Table holm)"。§5.6 末段报告了校正后结果：CLS-CWM gap adjusted p=0.012, function-level equivalence adjusted p=0.021, repo-level CWM-TRAJ adjusted p=0.078（未通过校正）。论文不仅做了多重比较校正，还诚实地报告了其中一个比较未能通过校正。R1 可能遗漏了这些段落。

---

**[AGREE] R1-W6: Post-hoc power analysis 方法论不当**
部分同意。Hoenig & Heisey (2001) 的批评在严格统计意义上是正确的：observed power 是 p 值的单调变换，不提供独立信息。但我认为论文的使用方式有所不同——它用 power 作为诊断工具来解释为什么 CLS-TRAJ 比较不具结论性（mean power = 0.08，Table `variant_power`），而非用来验证显著结果。这种"解释性"用法在实践中比"确认性"用法更可接受。

建议：(1) 引用 Hoenig & Heisey (2001) 并承认方法论局限；(2) 将 power 分析重新表述为 sample size planning：at n=48, the minimum detectable effect is 25pp（这是同样的信息但表述更规范）。

---

**[AGREE] R1-W7: NF4 vs bf16 混合分析**
同意需要更严格的处理。论文在 Extended Limitations（Appendix）中提到 "Restricting to three bfloat16 seeds yields a comparable mean gap with wider confidence interval (df=2); the NF4 seeds do not systematically shift the equivalence result"，但缺乏正式的 precision × formulation 交互检验。补充：Table `scaling`（§5.2）明确排除了 NF4 seeds（"seeds 42/123, full bfloat16 precision"），说明作者意识到精度差异可能影响结果。建议在 §5.3 中报告 bf16-only 和 NF4-only 的分别 TOST 结果。

---

**[AGREE] R1-W8: Cross-model CWM eval seq_length 不同**
同意。论文在 Table 3 脚注和 §5.4 Training and evaluation sensitivity 段中明确标注了这一问题（"CWM eval seq_length: Qwen3 8192, DeepSeek 4096; cross-model CWM values are not directly comparable"），也在 §5.6 Threats to Validity 中详细讨论。但正文仍在 §5.4 Cross-model consistency 段中将 DeepSeek 作为 "consistent with a formulation-driven explanation" 的证据使用，这与自己标注的 "not directly comparable" 存在张力。

我在自己的审稿中未单独列此点（因论文已标注），但同意 R1 的判断：既然承认不可比，就不应在正文叙事中作为支撑证据使用。建议弱化 cross-model consistency 的措辞。

---

## Minor

**[AGREE] R1-W9**: Prompt templates 应展示。至少在 Appendix 中给出 CLS、CWM、TRAJ 各一个 example prompt。这对 reproducibility 很重要。

**[AGREE] R1-W10**: TRAJ 在不同 test set 上评估确实是一个混淆因素。Table 1 caption 明确标注了 "TRAJ is evaluated on a 1,032-sample subset covering the same 447 (problem, mutation) variants"。虽然 variant coverage 相同，sample 数量差异（1,032 vs 1,890）意味着 per-test accuracy 不可直接比较。好在论文的 TOST 等价检验使用 variant-level（523 instances across 5 seeds），回避了这个问题。

**[AGREE] R1-W11**: Mutation operators 描述不足。论文只列出了 5 种类型名称（gold, operator_swap, off_by_one, return_value, boundary_removal），未给出具体实现定义和 mutation rule 示例。Table `mutation_distribution` (Appendix) 给出了分布但没有定义。

**[AGREE] R1-W12**: Re-repair pilot n=44 确实太小。论文自己承认 "statistical power is ~0.3 for a medium effect size"（Appendix §(j)）。我在自己的审稿中未单独列此项因为论文对此非常坦诚。

**[REBUT] R1-W13**: Oracle ensemble 单种子。论文在 Appendix §(a) 报告 oracle ensemble 90.63% (+3.12pp)，确实是 seed 42 单种子。但 5-seed 的 CLS/CWM 各自 accuracy 都报告了（Table 1），且 error complementarity 是一个 qualitative pattern（CLS 偏 false negative 75.5%, CWM 偏 false positive 83.1%），这种 directional pattern 不太可能因种子变化而反转。建议补充 5 种子的 oracle 范围即可，不需要所有种子的详细 breakdown。

---

## Questions

**Q1**: 同意需要澄清。Table 3 脚注暗示 epoch 2 是手动选择的（"NaN validation loss caused Trainer default to epoch 3 final"），作者应明确说明这是 a priori 还是 post-hoc。

**Q2**: 论文在 Extended Limitations 中部分回答了这个问题（"Restricting to three bfloat16 seeds yields a comparable mean gap with wider confidence interval"），但正式的 bf16-only TOST 结果应该展示。

**Q3**: 同意。Prompt template 可能是一个重要的 confound，尤其是 CWM 的 output format 高度依赖 prompt 设计。

**Q4**: 论文 §5.1 说明 n=48 variants 来自 SWE-bench Verified 的 test split（48 个 problem × mutation 组合），但选择标准（如何从 500 个 SWE-bench Verified instances 中选出 48 个）未明确。

**Q5**: 好问题。Table `taxonomy` 中 DeepSeek 同一模型在不同 configuration 下展现了不同 failure modes（decision collapse vs aggregation penalty），说明 fail recall 变异中相当部分可归因于 configuration 而非 formulation。这实际上支持了论文 "formulation × model × configuration × complexity" 交互作用的 framing。

**Q6**: 论文 Appendix Table `hyperparams` 注明 DeepSeek lr=2e-4 "tuned on a held-out validation split"。但 tuning 细节（搜索范围、选择标准）未报告。

---

## Missing References

同意补充 Lakens (2017) 和 Hoenig & Heisey (2001)。对 Holm-Bonferroni 的遗漏指控不成立（论文已引用 Holm 1979 并使用）。constrained decoding 文献的覆盖确实可以更广。

---

## 总结

R1 的审稿整体严谨，大部分技术问题有据可查。最有价值的贡献是 W1（TRAJ checkpoint 不一致）和 W4（confounds 累积效应）。W5（多重比较校正）为事实性错误——论文明确使用了 Holm-Bonferroni 校正。W3（TOST margin）的批评有一定道理但过度严厉：±2pp 在 code verification 部署场景中是一个 defensible SESOI，且观测 gap 本身仅 -0.45pp。

R1 的评分 3.0 (Findings) 与我的评分一致。但 R1 和我的关注点有所不同：R1 更侧重统计方法论的严格性，我更侧重新颖性和 CWM baseline 的公平性问题。两者结合，核心问题是：(1) 论文最有价值的 repo-level 发现依赖最薄弱的证据基础；(2) CWM baseline 与原始 CWM 的巨大差距削弱了 formulation-level 结论的普适性。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 425 · 2026-05-19T09:49:27.169156+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Holm|holm|bonferroni|family-wise|FWER|FDR",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Holm|holm|bonferroni|family-wise|FWER|FDR",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-19T09:49:27.219871+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:17:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:194:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.bbl:96:\bibitem[{Holm(1979)}]{holm1979}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.bbl:97:Sture Holm. 1979.
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.bbl:129:\bibitem[{Just et~al.(2014)Just, Jalali, Inozemtseva, Ernst, Holmes, and
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.bbl:132:  Holmes, and Gordon Fraser. 2014.
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.log:1325:\OT1/cmr/m/n/10.95 Table [][]15[][] ap-plies Holm-Bonferroni cor-rec-
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib:305:  author={Just, Ren{\'e} and Jalali, Darioush and Inozemtseva, Laura and Ernst, Michael D and Holmes, Reid and Fraser, Gordon},
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib:350:@article{holm1979,
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib:352:  author={Holm, Sture},
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.aux:292:\citation{holm1979}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.aux:1026:\bibcite{holm1979}{{14}{1979}{{Holm}}{{}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.aux:1031:\bibcite{just2014mutants}{{19}{2014}{{Just et~al.}}{{Jus
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-19T09:49:33.995982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "offset": "368",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "offset": "368",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-19T09:49:34.498214+00:00_

368	
369	\section{Multiple Comparison Correction}
370	\label{app:holm}
371	
372	Table~\ref{tab:holm} applies Holm-Bonferroni correction~\cite{holm1979} to the four primary statistical comparisons across this study ($k{=}4$, family-wise $\alpha{=}0.05$).
373	
374	\begin{table}[h]
375	\centering
376	\small
377	\caption{Holm-Bonferroni correction for primary comparisons ($k{=}4$). Comparisons ranked by raw $p$-value; each tested against $\alpha / (k - \text{rank} + 1)$.}
378	\label{tab:holm}
379	\setlength{\tabcolsep}{3pt}
380	\begin{tabular}{clcccc}
381	\toprule
382	\textbf{Rank} & \textbf{Comparison} & \textbf{Raw $p$} & \textbf{Factor} & \textbf{Adj $p$} & \textbf{Sig.?} \\
383	\midrule
384	1 & Repo: \cls{} vs \cwm{} & 0.003 & $\times$4 & 0.012 & \checkmark \\
385	2 & Func: \cls{} vs \traj{} (TOST $\pm$2\pp{}) & 0.0071 & $\times$3 & 0.021 & \checkmark \\
386	3 & Repo: \cwm{} vs \traj{} & 0.039 & $\times$2 & 0.078 & --- \\
387	4 & Repo: \cls{} vs \traj{} & 0.385 & $\times$1 & 0.385 & --- \\
388	\bottomrule
389	\end{tabular}
390	\end{table}
391	
392	The two core claims survive correction: the repo-level \cls{}--\cwm{} gap (adjusted $p{=}0.012$) and function-level \cls{}--\traj{} equivalence (adjusted $p{=}0.021$). The repo-level \cwm{}--\traj{} comparison does not survive correction (adjusted $p{=}0.078$); we interpret this difference as directionally consistent but not confirmatory.
393	
394	\section{CWM Parseable Bias Analysis}
395	\label{app:parseable_bias}
396	
397	The default-to-pass assignment for unparseable \cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\% vs.\ 68.3\%, $\chi^2$ $p = 5.9 \times 10^{-10}$), and \cls{} models achieve higher accuracy on unparseable instances (86.4\% vs.\ 79.1\%, $p = 3.3 \times 10^{-18}$). This indicates that \cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be corr
…[truncated 2133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-19T09:49:34.649323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "offset": "14",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "offset": "14",
    "limit": "6"
  }
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-19T09:49:34.649817+00:00_

14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\ref{app:hyperparams}.
15	
16	\paragraph{Statistics.}
17	Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); per-test vs.\ trajectory-level equivalence uses Two One-Sided Tests (TOST)~\cite{schuirmann1987tost} with $\pm$2\pp{} margin. Holm-Bonferroni correction~\cite{holm1979} controls family-wise error rate across the four primary comparisons (Table~\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 431 · 2026-05-19T09:50:57.173003+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 432 · 2026-05-19T09:50:57.223713+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 433 · 2026-05-19T09:54:14.409288+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "issues:\n# === Round 5 Critical Issues (fresh review) ===\n\n- id: \"R5-N1\"\n  summary: \"正文超出 ARR Long Paper 8 页限制（~11 页），可能 desk reject\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2 首次提出，R1 交叉 AGREE。PDF 渲染约 11 页正文，超出 2-3 页。Experiments section 过长（5 subsection + 5 table + 2 figure）是主因。\"\n  action_items:\n    - round: 5\n      action: \"Threats to Validity 移入 Appendix，压缩 Repo-Level 细节段落，精简 Contribution list 数字\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"TRAJ checkpoint selection 协议不一致：CWM 用 final epoch 但 TRAJ 手选 epoch 2\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 首次提出，R2 交叉 AGREE（但 impact limited ~2pp）。Table 4 脚注♦显示 TRAJ 选 epoch 2 (72.92%) 而非 Trainer default epoch 3 (70.83%)，与 CWM 全部使用 final epoch 的协议不一致。构成 cherry-picking 嫌疑。\"\n  action_items:\n    - round: 5\n      action: \"统一 NaN val loss checkpoint 策略，report 两组数字（epoch 2 和 epoch 3），明确标注选择是 post-hoc 的\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N3\"\n  summary: \"Table 4 混合 per-test (n=9784) 和 variant-level (n=48) 指标，视觉区分不足\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 首次提出，R2 交叉 AGREE。CLS/CWM per-test accuracy 与 TRAJ variant-level accuracy 并排展示，脚注‡标注容易被忽略，误导读者高估 CLS 相对 TRAJ 优势。\"\n  action_items:\n    - round: 5\n      action: \"拆分 Table 4 为 per-test 和 variant-level 两部分，或增加 CLS variant-level 列\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 5 Should-Fix Issues ===\n\n- id: \"R5-W1\"\n  summary: \"CWM baseline ≤8B LoRA 的条件限制在 Abstract/Introduction 中不够突出\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"首次提出：4-8B LoRA ≠ 32B mid-trained CWM。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-W1 再次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 列为 critical (N2)，R1 REBUT 'invalidates' 过强但 AGREE 需更突出条件限制。Conclusion/Threats 已有 conditioning（'at ≤8B LoRA scale'），但 Abstract 和 Introduction contribution list 未体现。轻度分歧：R2 认为本质上 invalidate repo-level 结论；R1 认为 conditioned claim 合理。Director 判断 R1 论证更有说服力——matched comparison 正是论文的设计目的。\"\n  action_items:\n    - round: 5\n      action: \"Abstract 和 Introduction contribution list 中加入 'under ≤8B LoRA fine-tuning' 条件限定\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"Repo-level 核心发现主要依赖单种子，与 function-level 5-seed 标准形成方法论不对称\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"首次提出。seed variance 可达 7.68pp。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N3 再次提出。bootstrap CI + power analysis 已完成。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 列为 critical (N3)，R1 AGREE with nuance（效应量 19-26pp 远超 function-level seed noise <2pp；CI lower bound 10.42pp 仍 substantial）。两人共识：limitation 真实但效应量大到不太可能被 seed noise 反转。建议将 repo-level 结论措辞从 'evidence' 降级为 'preliminary evidence'。\"\n  action_items:\n    - round: 5\n      action: \"如可行补充第二个 repo-level seed；否则在 Abstract/Introduction 中弱化 repo-level 结论措辞\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"TOST ±2pp margin 需改善 a priori 正当性论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N1 首次提出为 critical。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 列为 critical (W3)；R2 部分 REBUT：domain-justified SESOI 可接受（观测 gap 仅 -0.45pp），但同意应引用 Lakens (2017) 正式论证。sensitivity table (Appendix E) 已有但正文 presentation 不够。轻度分歧已收敛：两人均同意需改善论证，但不再视为 critical。\"\n  action_items:\n    - round: 5\n      action: \"§4.4 引用 Lakens (2017) SESOI 框架，正式论证 ±2pp 选择依据，明确是 domain-justified 而非 a priori\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"Repo-level confounds 累积效应未讨论（假设独立作用不成立）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 首次提出 (W4)，R2 交叉 AGREE 并补充：confounds 大部分对 CWM 不利方向一致，不太可能反转 CLS>CWM 方向，但 gap 精确大小不可靠。§5.6 声称 gap 超过任何单个 confound 'by an order of magnitude' 但未讨论 compound effect。\"\n  action_items:\n    - round: 5\n      action: \"§5.6 增加 worst-case compound scenario 讨论段落\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"Post-hoc power analysis 方法论不当（Hoenig & Heisey 2001 批评）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 首次提出 (W6)，R2 部分 AGREE：observed power 是 p 值单调函数，但用作诊断工具解释 CLS-TRAJ 不具结论性比 confirmatory 用法更可接受。两人共识：重新表述为 sample size planning + 引用 Hoenig & Heisey。\"\n  action_items:\n    - round: 5\n      action: \"Appendix F 引用 Hoenig & Heisey (2001)，重新表述为 minimum detectable effect（已部分有），弱化 observed power 的 confirmatory 含义\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W6\"\n  summary: \"NF4 vs bf16 混合 5-seed 分析缺乏正式交互检验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R4-M4 首次提出为 minor。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W7)，R2 交叉 AGREE。Table 2 排除 NF4 seeds（说明作者认为 precision 是需控制变量），但 TOST 和 Table 1 混合两种精度。Extended Limitations 提到 bf16-only 结果 comparable 但未正式展示。\"\n  action_items:\n    - round: 5\n      action: \"§4.4 报告 bf16-only TOST 结果，或提供 precision × formulation 交互检验\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"Cross-model CWM eval seq_length 不一致（Qwen3:8192 vs DeepSeek:4096），但仍作为 consistency 证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R3-W4 首次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W8)，R2 交叉 AGREE。论文自标 'not directly comparable' 但 §4.5 仍用作 'consistent with formulation-driven explanation' 证据，存在矛盾。\"\n  action_items:\n    - round: 5\n      action: \"弱化 cross-model CWM consistency 措辞，仅将 CLS cross-model consistency 作为证据\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W8\"\n  summary: \"Related Work 第一段以枚举代替定位（8 行内堆砌 ~18 引用）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 首次提出 (W1)，R1 交叉 AGREE。第一段 'A proposed X, B proposed Y' 列表式写法，缺乏按 formulation 类型的归纳和本文定位分析。第二段（PRM/ORM）较好。\"\n  action_items:\n    - round: 5\n      action: \"Related Work 第一段按 formulation 类型重组（generation-based, classification-based, trajectory/reward-based），提炼共性和局限性\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W9\"\n  summary: \"Abstract 数字密度过高，读起来像 results 摘要而非 compelling narrative\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R3-W2 首次提出。211 词。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-W2 再次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出 (W2)，R1 交叉 AGREE。约 170 words 含 p-value、pp margin、oracle%、多组准确率等。跨 3 轮未解决。\"\n  action_items:\n    - round: 5\n      action: \"保留 1-2 个关键数字（function equivalence, repo 19-26pp gap），其余定性描述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W10\"\n  summary: \"TRAJ 比较存在多重未控制混淆因素（数据量、LR、评估粒度、checkpoint、label 粒度）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R3-N1 首次提出。downsample ablation 部分缓解。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出 (W3)，R1 交叉 AGREE 并列出 5 个 confound chain（数据量、LR、评估粒度、checkpoint、label 粒度），downsample 仅控制第 1 个。CLS-TRAJ repo-level 比较严格来说 uninterpretable。\"\n  action_items:\n    - round: 5\n      action: \"明确标注 CLS-TRAJ repo-level 比较为 preliminary/suggestive，在 contribution list 中相应降级\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W11\"\n  summary: \"Introduction 贡献列表过长（4 条共 ~350 words，每条含具体数字）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出 (W4)，R1 交叉 AGREE。第二条 contribution 单条 ~120 words 含 Qwen3/DeepSeek 退化数据和 3 种 failure mode 名称。信息过密，reader 尚未看到实验设计无法评判数字意义。\"\n  action_items:\n    - round: 5\n      action: \"每条 contribution 压缩至 1-2 句，具体数字移至 Results section\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 5 Minor Issues ===\n\n- id: \"R5-M1\"\n  summary: \"'pp' (percentage points) 缩写全文未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2 提出 (W5)，R1 交叉 AGREE。首次出现于 Abstract。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"Prompt templates（CLS/CWM/TRAJ）未在论文或 Appendix 中展示\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W9)，R2 交叉 AGREE。Prompt 措辞可能影响 formulation performance，对 reproducibility 和 formulation 归因有影响。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M3\"\n  summary: \"Mutation operators 选择理由和实现细节缺失\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W11)，R2 交叉 AGREE。5 种 mutation types 仅列名称，未给出具体实现定义和 mutation rule 示例。Table 9/10 显示类型间难度差异巨大。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"Table 4 脚注密度极高（†, ‡, ♦, a 四个标记）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-M1 首次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 AGREE R2 的观察（M3）。仍然存在。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Checklist C4 回答 'Partially'（package version numbers），提交前需补全\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出 (M2)，R1 的 W9 也涉及 reproducibility。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M6\"\n  summary: \"少量 trailing -ing phrases（AI 写作痕迹）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2 提出 (M1)：'motivating complexity-aware routing over uniform formulation selection'（abstract, conclusion）。R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M7\"\n  summary: \"TRAJ function-level 在不同 test set 上评估（1,032 vs 1,890 samples）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W10)，R2 AGREE。Table 1 caption 标注但不够突出。TOST 使用 variant-level 回避了此问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M8\"\n  summary: \"Oracle ensemble (90.63%) 仅报告单 seed，应报告多 seed 范围\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"R1 提出 (W13)。R2 REBUT：directional pattern（CLS 偏 FN 75.5%，CWM 偏 FP 83.1%）不太可能因种子反转，补充 5 种子范围即可。共识：降级为 minor。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 4 Issues — Status Update ===\n\n- id: \"R4-N1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正式论证和 sensitivity analysis\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 首次提出，R2 交叉 AGREE。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Sensitivity table 已加入 Appendix E (Table 7)。正文 §4.4 有 deployment-relevance 论证但仍缺 SESOI 框架引用。被 R5-W3 覆盖。\"\n  action_items:\n    - round: 4\n      action: \"Agent 从 clustered bootstrap 原始数据独立重算 TOST margin sweep ±0.5~5.0pp\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 4\n      action: \"Paper Agent 将 sensitivity table 加入 Appendix + 正文 deployment-relevance 论证\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Sensitivity table 完成，但 a priori 正当性论证仍需改善（R5-W3）\"\n  resolution_round: null\n\n- id: \"R4-N2\"\n  summary: \"'Controlled comparison' 声称与实际设计存在系统性裂隙\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 首次逐项拆解。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Title 已改为 'Systematic'。Threats to Validity 已有。但 TRAJ checkpoint 不一致新增（R5-N2）。部分解决。\"\n  action_items:\n    - round: 4\n      action: \"Paper Agent: Title 从 'Controlled' 改为 'Systematic' + 新增 Threats to Validity 段落\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Title 和 Threats to Validity 已修复。TRAJ checkpoint 不一致作为新 issue R5-N2 跟踪。\"\n  resolution_round: 5\n\n- id: \"R4-N3\"\n  summary: \"Repo-level n=48 variant-level 统计效力严重不足，缺 CI 和 power analysis\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两人独立发现。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Appendix F (Table 8) 已有 bootstrap CI + power analysis。但 post-hoc power 方法论不当（R5-W5）。R5-W2 作为持续 issue 跟踪。\"\n  action_items:\n    - round: 4\n      action: \"Agent 计算 variant-level bootstrap CI + power analysis\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 4\n      action: \"Paper Agent 加 hedging 到 Contribution #2 和 repo-level 结论\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"Power analysis 已完成。Hedging 有改善但仍不充分（R5-W2）。\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"CWM baseline external validity 严重受限但仍做 formulation-level 归因\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"4-8B LoRA ≠ 32B mid-trained CWM。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Conclusion 和 Threats 已有 'at ≤8B LoRA scale' conditioning。但 Abstract/Introduction 未体现。R5-W1 跟踪。\"\n  action_items:\n    - round: 4\n      action: \"Paper Agent: 全文 CWM 结论加 'at ≤8B LoRA scale' + Limitations 讨论\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"Conclusion/Threats 已加 conditioning。Abstract/Introduction 仍需补充（R5-W1）。\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"15+ 个数值。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍然存在。R5-W9 跟踪。跨 3 轮未解决。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 'validation' 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"n=2 model families 不构成 'validation'。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未被提及。正文已改为 'cross-model consistency check'。\"\n  action_items: []\n  resolution: \"全文替换 'cross-model validation' → 'cross-model consistency check' 已完成。\"\n  resolution_round: 5\n\n- id: \"R4-W4\"\n  summary: \"新颖性定位：'design space' 仅 3 个离散点，缺深层机制洞察\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"标题 'Design Space' overselling。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未被直接提及。标题保留 'Formulation Design Space'。R2 Excitement 评 3/5 但未单列此问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"多重比较问题未处理\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"论文以统计严谨性为卖点但未做多重比较校正。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 再次提出 (W5) 但 R2 REBUT 指出论文已有 Holm-Bonferroni（§4.1 Statistics + Appendix K Table 15）。R1 遗漏此段落。事实性错误——论文已解决。\"\n  action_items: []\n  resolution: \"Holm-Bonferroni correction 已在 §4.1 和 Appendix K 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W6\"\n  summary: \"合成数据（mutation-based）外部效度讨论不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Limitations 仅一句话。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Limitations section 已扩展讨论 synthetic-to-real transfer gap。两位 reviewer 均提出 mutation types 描述不足（R5-M3）。改善但未完全解决。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W7\"\n  summary: \"Error complementarity / ICC oracle analysis 的适用范围未限定\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"oracle 结论应限定为 function-level。\"\n    - round: 5\n      reviewers: []\n      note: \"Abstract 现在写 'Formulations exhibit complementary errors at function level'，Introduction contribution 3 也标注 function-level。改善明显。R5-M8 跟踪单 seed 问题。\"\n  action_items: []\n  resolution: \"function-level 限定已加入。基本解决。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏近期直接相关工作（CodePRM, FunPRM 等）\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"缺 CodePRM/FunPRM/constrained decoding 引用。\"\n    - round: 5\n      reviewers: []\n      note: \"CodePRM、FunPRM、DreamPRM-Code、CodeScaler、CodeRL+、PRL-Coder 均已在 references.bib 和 Related Work 中引用。本轮未被提及。\"\n  action_items: []\n  resolution: \"相关引用已补充完整。\"\n  resolution_round: 5\n\n- id: \"R4-M2\"\n  summary: \"CWM unparseable default-to-pass 的方向性影响应在正文讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"default-to-pass 使 CWM accuracy 包含大量'猜对'成分。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"§4.5 现有 'Default assignment artifact' 段落，详细讨论 parseable bias、χ² 检验、方向性影响。R1 交叉回应中引用此段证明 default-to-pass 是对 CWM 最 charitable 的策略。已充分解决。\"\n  action_items: []\n  resolution: \"§4.5 Default assignment artifact 段落已充分讨论。\"\n  resolution_round: 5\n\n- id: \"R4-M6\"\n  summary: \"'CWM stagnation' 措辞偏强\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"建议改为 'plateau' 或 'flat scaling'。\"\n    - round: 5\n      reviewers: []\n      note: \"正文已改为 'flat scaling'（§4.3）。\"\n  action_items: []\n  resolution: \"已改为 'flat scaling'。\"\n  resolution_round: 5\n\n# === Earlier Rounds — Resolved Issues (保留记录) ===\n\n- id: \"R3-W1\"\n  summary: \"Limitations 不是独立 section，有 desk reject 风险\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"30秒 LaTeX 修复。\"\n    - round: 5\n      reviewers: []\n      note: \"已改为 \\\\section*{Limitations}，R2 确认格式合规。\"\n  resolution: \"已修复为独立 section。\"\n  resolution_round: 5\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CWM 8B 完成。Round 2 确认 resolved。\"\n  resolution_round: 2\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"rank-32 消融完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Title changed.\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Relaxed matching 反降准确率。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"遗漏 LEVER 和 CodeT\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已添加。\"\n  resolution_round: 1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "issues:\n# === Round 5 Critical Issues (fresh review) ===\n\n- id: \"R5-N1\"\n  summary: \"正文超出 ARR Long Paper 8 页限制（~11 页），可能 desk reject\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2 首次提出，R1 交叉 AGREE。PDF 渲染约 11 页正文，超出 2-3 页。Experiments section 过长（5 subsection + 5 table + 2 figure）是主因。\"\n  action_items:\n    - round: 5\n      action: \"Threats to Validity 移入 Appendix，压缩 Repo-Level 细节段落，精简 Contribution list 数字\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"TRAJ checkpoint selection 协议不一致：CWM 用 final epoch 但 TRAJ 手选 epoch 2\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 首次提出，R2 交叉 AGREE（但 impact limited ~2pp）。Table 4 脚注♦显示 TRAJ 选 epoch 2 (72.92%) 而非 Trainer default epoch 3 (70.83%)，与 CWM 全部使用 final epoch 的协议不一致。构成 cherry-picking 嫌疑。\"\n  action_items:\n    - round: 5\n      action: \"统一 NaN val loss checkpoint 策略，report 两组数字（epoch 2 和 epoch 3），明确标注选择是 post-hoc 的\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N3\"\n  summary: \"Table 4 混合 per-test (n=9784) 和 variant-level (n=48) 指标，视觉区分不足\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 首次提出，R2 交叉 AGREE。CLS/CWM per-test accuracy 与 TRAJ variant-level accuracy 并排展示，脚注‡标注容易被忽略，误导读者高估 CLS 相对 TRAJ 优势。\"\n  action_items:\n    - round: 5\n      action: \"拆分 Table 4 为 per-test 和 variant-level 两部分，或增加 CLS variant-level 列\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 5 Should-Fix Issues ===\n\n- id: \"R5-W1\"\n  summary: \"CWM baseline ≤8B LoRA 的条件限制在 Abstract/Introduction 中不够突出\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"首次提出：4-8B LoRA ≠ 32B mid-trained CWM。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-W1 再次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 列为 critical (N2)，R1 REBUT 'invalidates' 过强但 AGREE 需更突出条件限制。Conclusion/Threats 已有 conditioning（'at ≤8B LoRA scale'），但 Abstract 和 Introduction contribution list 未体现。轻度分歧：R2 认为本质上 invalidate repo-level 结论；R1 认为 conditioned claim 合理。Director 判断 R1 论证更有说服力——matched comparison 正是论文的设计目的。\"\n  action_items:\n    - round: 5\n      action: \"Abstract 和 Introduction contribution list 中加入 'under ≤8B LoRA fine-tuning' 条件限定\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"Repo-level 核心发现主要依赖单种子，与 function-level 5-seed 标准形成方法论不对称\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"首次提出。seed variance 可达 7.68pp。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N3 再次提出。bootstrap CI + power analysis 已完成。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 列为 critical (N3)，R1 AGREE with nuance（效应量 19-26pp 远超 function-level seed noise <2pp；CI lower bound 10.42pp 仍 substantial）。两人共识：limitation 真实但效应量大到不太可能被 seed noise 反转。建议将 repo-level 结论措辞从 'evidence' 降级为 'preliminary evidence'。\"\n  action_items:\n    - round: 5\n      action: \"如可行补充第二个 repo-level seed；否则在 Abstract/Introduction 中弱化 repo-level 结论措辞\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"TOST ±2pp margin 需改善 a priori 正当性论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-N1 首次提出为 critical。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 列为 critical (W3)；R2 部分 REBUT：domain-justified SESOI 可接受（观测 gap 仅 -0.45pp），但同意应引用 Lakens (2017) 正式论证。sensitivity table (Appendix E) 已有但正文 presentation 不够。轻度分歧已收敛：两人均同意需改善论证，但不再视为 critical。\"\n  action_items:\n    - round: 5\n      action: \"§4.4 引用 Lakens (2017) SESOI 框架，正式论证 ±2pp 选择依据，明确是 domain-justified 而非 a priori\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"Repo-level confounds 累积效应未讨论（假设独立作用不成立）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 首次提出 (W4)，R2 交叉 AGREE 并补充：confounds 大部分对 CWM 不利方向一致，不太可能反转 CLS>CWM 方向，但 gap 精确大小不可靠。§5.6 声称 gap 超过任何单个 confound 'by an order of magnitude' 但未讨论 compound effect。\"\n  action_items:\n    - round: 5\n      action: \"§5.6 增加 worst-case compound scenario 讨论段落\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"Post-hoc power analysis 方法论不当（Hoenig & Heisey 2001 批评）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 首次提出 (W6)，R2 部分 AGREE：observed power 是 p 值单调函数，但用作诊断工具解释 CLS-TRAJ 不具结论性比 confirmatory 用法更可接受。两人共识：重新表述为 sample size planning + 引用 Hoenig & Heisey。\"\n  action_items:\n    - round: 5\n      action: \"Appendix F 引用 Hoenig & Heisey (2001)，重新表述为 minimum detectable effect（已部分有），弱化 observed power 的 confirmatory 含义\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W6\"\n  summary: \"NF4 vs bf16 混合 5-seed 分析缺乏正式交互检验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R4-M4 首次提出为 minor。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W7)，R2 交叉 AGREE。Table 2 排除 NF4 seeds（说明作者认为 precision 是需控制变量），但 TOST 和 Table 1 混合两种精度。Extended Limitations 提到 bf16-only 结果 comparable 但未正式展示。\"\n  action_items:\n    - round: 5\n      action: \"§4.4 报告 bf16-only TOST 结果，或提供 precision × formulation 交互检验\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"Cross-model CWM eval seq_length 不一致（Qwen3:8192 vs DeepSeek:4096），但仍作为 consistency 证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R3-W4 首次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W8)，R2 交叉 AGREE。论文自标 'not directly comparable' 但 §4.5 仍用作 'consistent with formulation-driven explanation' 证据，存在矛盾。\"\n  action_items:\n    - round: 5\n      action: \"弱化 cross-model CWM consistency 措辞，仅将 CLS cross-model consistency 作为证据\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W8\"\n  summary: \"Related Work 第一段以枚举代替定位（8 行内堆砌 ~18 引用）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 首次提出 (W1)，R1 交叉 AGREE。第一段 'A proposed X, B proposed Y' 列表式写法，缺乏按 formulation 类型的归纳和本文定位分析。第二段（PRM/ORM）较好。\"\n  action_items:\n    - round: 5\n      action: \"Related Work 第一段按 formulation 类型重组（generation-based, classification-based, trajectory/reward-based），提炼共性和局限性\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W9\"\n  summary: \"Abstract 数字密度过高，读起来像 results 摘要而非 compelling narrative\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R3-W2 首次提出。211 词。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-W2 再次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出 (W2)，R1 交叉 AGREE。约 170 words 含 p-value、pp margin、oracle%、多组准确率等。跨 3 轮未解决。\"\n  action_items:\n    - round: 5\n      action: \"保留 1-2 个关键数字（function equivalence, repo 19-26pp gap），其余定性描述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W10\"\n  summary: \"TRAJ 比较存在多重未控制混淆因素（数据量、LR、评估粒度、checkpoint、label 粒度）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R3-N1 首次提出。downsample ablation 部分缓解。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出 (W3)，R1 交叉 AGREE 并列出 5 个 confound chain（数据量、LR、评估粒度、checkpoint、label 粒度），downsample 仅控制第 1 个。CLS-TRAJ repo-level 比较严格来说 uninterpretable。\"\n  action_items:\n    - round: 5\n      action: \"明确标注 CLS-TRAJ repo-level 比较为 preliminary/suggestive，在 contribution list 中相应降级\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W11\"\n  summary: \"Introduction 贡献列表过长（4 条共 ~350 words，每条含具体数字）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出 (W4)，R1 交叉 AGREE。第二条 contribution 单条 ~120 words 含 Qwen3/DeepSeek 退化数据和 3 种 failure mode 名称。信息过密，reader 尚未看到实验设计无法评判数字意义。\"\n  action_items:\n    - round: 5\n      action: \"每条 contribution 压缩至 1-2 句，具体数字移至 Results section\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 5 Minor Issues ===\n\n- id: \"R5-M1\"\n  summary: \"'pp' (percentage points) 缩写全文未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2 提出 (W5)，R1 交叉 AGREE。首次出现于 Abstract。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M2\"\n  summary: \"Prompt templates（CLS/CWM/TRAJ）未在论文或 Appendix 中展示\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W9)，R2 交叉 AGREE。Prompt 措辞可能影响 formulation performance，对 reproducibility 和 formulation 归因有影响。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M3\"\n  summary: \"Mutation operators 选择理由和实现细节缺失\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W11)，R2 交叉 AGREE。5 种 mutation types 仅列名称，未给出具体实现定义和 mutation rule 示例。Table 9/10 显示类型间难度差异巨大。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"Table 4 脚注密度极高（†, ‡, ♦, a 四个标记）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R4-M1 首次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 AGREE R2 的观察（M3）。仍然存在。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Checklist C4 回答 'Partially'（package version numbers），提交前需补全\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 提出 (M2)，R1 的 W9 也涉及 reproducibility。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M6\"\n  summary: \"少量 trailing -ing phrases（AI 写作痕迹）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"R2 提出 (M1)：'motivating complexity-aware routing over uniform formulation selection'（abstract, conclusion）。R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M7\"\n  summary: \"TRAJ function-level 在不同 test set 上评估（1,032 vs 1,890 samples）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 提出 (W10)，R2 AGREE。Table 1 caption 标注但不够突出。TOST 使用 variant-level 回避了此问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M8\"\n  summary: \"Oracle ensemble (90.63%) 仅报告单 seed，应报告多 seed 范围\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"R1 提出 (W13)。R2 REBUT：directional pattern（CLS 偏 FN 75.5%，CWM 偏 FP 83.1%）不太可能因种子反转，补充 5 种子范围即可。共识：降级为 minor。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 4 Issues — Status Update ===\n\n- id: \"R4-N1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正式论证和 sensitivity analysis\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 首次提出，R2 交叉 AGREE。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Sensitivity table 已加入 Appendix E (Table 7)。正文 §4.4 有 deployment-relevance 论证但仍缺 SESOI 框架引用。被 R5-W3 覆盖。\"\n  action_items:\n    - round: 4\n      action: \"Agent 从 clustered bootstrap 原始数据独立重算 TOST margin sweep ±0.5~5.0pp\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 4\n      action: \"Paper Agent 将 sensitivity table 加入 Appendix + 正文 deployment-relevance 论证\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Sensitivity table 完成，但 a priori 正当性论证仍需改善（R5-W3）\"\n  resolution_round: null\n\n- id: \"R4-N2\"\n  summary: \"'Controlled comparison' 声称与实际设计存在系统性裂隙\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 首次逐项拆解。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Title 已改为 'Systematic'。Threats to Validity 已有。但 TRAJ checkpoint 不一致新增（R5-N2）。部分解决。\"\n  action_items:\n    - round: 4\n      action: \"Paper Agent: Title 从 'Controlled' 改为 'Systematic' + 新增 Threats to Validity 段落\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Title 和 Threats to Validity 已修复。TRAJ checkpoint 不一致作为新 issue R5-N2 跟踪。\"\n  resolution_round: 5\n\n- id: \"R4-N3\"\n  summary: \"Repo-level n=48 variant-level 统计效力严重不足，缺 CI 和 power analysis\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两人独立发现。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Appendix F (Table 8) 已有 bootstrap CI + power analysis。但 post-hoc power 方法论不当（R5-W5）。R5-W2 作为持续 issue 跟踪。\"\n  action_items:\n    - round: 4\n      action: \"Agent 计算 variant-level bootstrap CI + power analysis\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 4\n      action: \"Paper Agent 加 hedging 到 Contribution #2 和 repo-level 结论\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"Power analysis 已完成。Hedging 有改善但仍不充分（R5-W2）。\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"CWM baseline external validity 严重受限但仍做 formulation-level 归因\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"4-8B LoRA ≠ 32B mid-trained CWM。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Conclusion 和 Threats 已有 'at ≤8B LoRA scale' conditioning。但 Abstract/Introduction 未体现。R5-W1 跟踪。\"\n  action_items:\n    - round: 4\n      action: \"Paper Agent: 全文 CWM 结论加 'at ≤8B LoRA scale' + Limitations 讨论\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"Conclusion/Threats 已加 conditioning。Abstract/Introduction 仍需补充（R5-W1）。\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"15+ 个数值。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍然存在。R5-W9 跟踪。跨 3 轮未解决。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 'validation' 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"n=2 model families 不构成 'validation'。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未被提及。正文已改为 'cross-model consistency check'。\"\n  action_items: []\n  resolution: \"全文替换 'cross-model validation' → 'cross-model consistency check' 已完成。\"\n  resolution_round: 5\n\n- id: \"R4-W4\"\n  summary: \"新颖性定位：'design space' 仅 3 个离散点，缺深层机制洞察\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"标题 'Design Space' overselling。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未被直接提及。标题保留 'Formulation Design Space'。R2 Excitement 评 3/5 但未单列此问题。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"多重比较问题未处理\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"论文以统计严谨性为卖点但未做多重比较校正。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 再次提出 (W5) 但 R2 REBUT 指出论文已有 Holm-Bonferroni（§4.1 Statistics + Appendix K Table 15）。R1 遗漏此段落。事实性错误——论文已解决。\"\n  action_items: []\n  resolution: \"Holm-Bonferroni correction 已在 §4.1 和 Appendix K 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W6\"\n  summary: \"合成数据（mutation-based）外部效度讨论不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Limitations 仅一句话。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Limitations section 已扩展讨论 synthetic-to-real transfer gap。两位 reviewer 均提出 mutation types 描述不足（R5-M3）。改善但未完全解决。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W7\"\n  summary: \"Error complementarity / ICC oracle analysis 的适用范围未限定\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"oracle 结论应限定为 function-level。\"\n    - round: 5\n      reviewers: []\n      note: \"Abstract 现在写 'Formulations exhibit complementary errors at function level'，Introduction contribution 3 也标注 function-level。改善明显。R5-M8 跟踪单 seed 问题。\"\n  action_items: []\n  resolution: \"function-level 限定已加入。基本解决。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏近期直接相关工作（CodePRM, FunPRM 等）\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"缺 CodePRM/FunPRM/constrained decoding 引用。\"\n    - round: 5\n      reviewers: []\n      note: \"CodePRM、FunPRM、DreamPRM-Code、CodeScaler、CodeRL+、PRL-Coder 均已在 references.bib 和 Related Work 中引用。本轮未被提及。\"\n  action_items: []\n  resolution: \"相关引用已补充完整。\"\n  resolution_round: 5\n\n- id: \"R4-M2\"\n  summary: \"CWM unparseable default-to-pass 的方向性影响应在正文讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"default-to-pass 使 CWM accuracy 包含大量'猜对'成分。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"§4.5 现有 'Default assignment artifact' 段落，详细讨论 parseable bias、χ² 检验、方向性影响。R1 交叉回应中引用此段证明 default-to-pass 是对 CWM 最 charitable 的策略。已充分解决。\"\n  action_items: []\n  resolution: \"§4.5 Default assignment artifact 段落已充分讨论。\"\n  resolution_round: 5\n\n- id: \"R4-M6\"\n  summary: \"'CWM stagnation' 措辞偏强\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"建议改为 'plateau' 或 'flat scaling'。\"\n    - round: 5\n      reviewers: []\n      note: \"正文已改为 'flat scaling'（§4.3）。\"\n  action_items: []\n  resolution: \"已改为 'flat scaling'。\"\n  resolution_round: 5\n\n# === Earlier Rounds — Resolved Issues (保留记录) ===\n\n- id: \"R3-W1\"\n  summary: \"Limitations 不是独立 section，有 desk reject 风险\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"30秒 LaTeX 修复。\"\n    - round: 5\n      reviewers: []\n      note: \"已改为 \\\\section*{Limitations}，R2 确认格式合规。\"\n  resolution: \"已修复为独立 section。\"\n  resolution_round: 5\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CWM 8B 完成。Round 2 确认 resolved。\"\n  resolution_round: 2\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"rank-32 消融完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Title changed.\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Relaxed matching 反降准确率。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"遗漏 LEVER 和 CodeT\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已添加。\"\n  resolution_round: 1"
  }
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-19T09:54:14.511123+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 21351}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 435 · 2026-05-19T09:57:29.068112+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 5 (Fresh Review)\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计方法; R2: 新颖性+写作质量+相关工作+格式合规）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行实验。Function-level 三种方法近等效（TOST p=0.007, 5 seeds）；repo-level CLS 以 19-26pp 大幅领先 CWM。论文统计方法论在 function-level 达到上游水准，但 repo-level 核心发现受单种子、CWM baseline 规模限制、以及多重 confound 累积的制约。**正文约 11 页，超出 ARR Long Paper 8 页硬限制，是最紧迫的格式问题。**\n\n---\n\n## Strengths\n\n**S1.** 首个在 matched conditions 下比较三种 verification formulation 的系统研究，填补了确实存在的文献空白。[R1 S1, R2 S1, 共识]\n\n**S2.** Function-level 统计方法论极为扎实：5 seeds、两个模型家族、TOST equivalence test + clustered bootstrap (114 clusters, 10K resamples) + ICC + Holm-Bonferroni 多重比较校正。在 ML 实验论文中属于上游水准。[R1 S2, R2 S2, 共识]\n\n**S3.** 对 confounds 和 limitations 的透明度罕见。Section 5 (Threats to Validity) 系统性列出 5 个 confounds 并量化每个 confound 的 observed effect。多数论文不会主动暴露如此深度的局限性。[R1 S3, R2 S3, 共识]\n\n**S4.** Default assignment artifact 分析（§4.5）精彩：CWM 4B→8B \"伪改善\"的解构（unparseable rate 上升 → majority-class default → accuracy 虚增，parseable-only accuracy 实际下降）展示了评估指标如何误导。[R1 S4, 共识]\n\n**S5.** Failure mode taxonomy (Table 3: format collapse, decision collapse, aggregation penalty) 提供了可操作的诊断框架。同一模型家族在不同 configuration 下表现出不同 failure mode 的发现对理解 formulation × configuration 交互有实质贡献。[R1 S6, R2 S4, 共识]\n\n**S6.** 消融设计充分：LoRA rank ablation、matched-context ablation（确认 input disparity 仅解释 <3% gap）、training data downsample（控制数据量差异）、majority voting ablation、relaxed matching ablation。[R1 S5]\n\n**S7.** 217× throughput advantage 的量化有实际部署参考意义。[R2 S5]\n\n**S8.** 写作无明显 AI 风格痕迹（无 em-dash/en-dash、无黑名单用词），引用完整（58 篇验证无幻觉引用）。[R2 S6, S7]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [Critical] 正文超出 ARR Long Paper 8 页限制（~11 页）。** [R2-N1, R1 AGREE]\nPDF 渲染约 11 页正文，超出 2-3 页。ARR 硬约束，可能直接 desk reject。Experiments section 含 5 个 subsection + 5 张 table + 2 张 figure 是主因。\n→ **修复方向**: Threats to Validity 移入 Appendix 并在正文保留一段概述；压缩 Repo-Level 的 Default assignment artifact / Constrained decoding / Training and evaluation sensitivity 段落至 Appendix；精简 Introduction 贡献列表。\n\n**W2. [Critical] TRAJ checkpoint selection 协议不一致。** [R1-W1, R2 AGREE]\n论文协议：NaN validation loss 时使用 final epoch。CWM 所有 repo-level runs 遵循此协议。但 Qwen3-8B TRAJ 手动选择了 epoch 2 (72.92%) 而非 Trainer 默认 epoch 3 (70.83%)。Table 4 脚注 ♦ 记录了此选择。虽然绝对影响有限（~2pp），但构成协议不一致和 cherry-picking 嫌疑。\n→ **修复方向**: 统一 checkpoint 策略，report 两组数字，明确标注 epoch 2 选择是 post-hoc 的。\n\n**W3. [Critical] Table 4 混合 per-test (n=9,784) 和 variant-level (n=48) 指标。** [R1-W2, R2 AGREE]\nCLS/CWM per-test accuracy 与 TRAJ variant-level accuracy 并排展示，脚注 ‡ 标注容易被忽略。CLS variant-level accuracy 远低于其 per-test accuracy（如 Qwen3-4B: 83.63% → 64.58%），读者若将 CLS per-test 与 TRAJ variant-level 直接比较会严重误判优劣。\n→ **修复方向**: 拆分为 per-test 和 variant-level 两个表，或增加 CLS variant-level 列。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4. CWM baseline ≤8B LoRA 的条件限制在 Abstract/Introduction 不够突出。** [R2-N2 提出, R1 部分 REBUT]\n4-8B LoRA CWM ≠ 32B mid-trained CWM。论文 Conclusion/Threats 已有 \"at ≤8B LoRA scale\" conditioning，但 Abstract 和 Introduction contribution list 未体现。R2 认为此差距 \"essentially invalidates\" repo-level 结论；R1 反驳 \"invalidates\" 过强——matched comparison 正是论文设计目的，conditioned claim 合理。**Director 判断**：R1 论证更有说服力，但 conditioning 确需更突出。\n→ **修复方向**: Abstract 和 Introduction contribution list 中加入 \"under ≤8B LoRA fine-tuning\" 条件限定。\n\n**W5. Repo-level 核心发现依赖单种子。** [R2-N3, R1 AGREE with nuance]\nQwen3 repo-level CLS vs CWM 为单种子 (s42)；variant 评估 n=48。与 function-level 5-seed 标准形成方法论不对称。R1 补充：效应量 19-26pp 远超 function-level seed noise (<2pp)，CI lower bound 10.42pp 仍 substantial，cross-model 方向一致。两人共识：limitation 真实但效应量大到不太可能被 seed noise 反转。\n→ **修复方向**: 如可行补充第二个 repo-level seed；否则将措辞从 \"evidence\" 降级为 \"preliminary evidence\"。\n\n**W6. TOST ±2pp margin 需改善正当性论证。** [R1-W3 提出, R2 部分 REBUT]\nR1 认为缺乏 a priori justification；R2 反驳 ±2pp 是 code verification 场景中 defensible SESOI，观测 gap 仅 -0.45pp，讨论 ±1.5pp vs ±2pp 对实际决策几乎无影响。两人共识：需引用 Lakens (2017) SESOI 框架正式论证。Sensitivity table (Appendix E) 已有。\n→ **修复方向**: §4.4 引用 Lakens (2017)，正式论证 ±2pp 选择依据。\n\n**W7. Confounds 累积效应未讨论。** [R1-W4, R2 AGREE]\n§5.6 声称 gap \"exceeds any individual confound's observed effect by an order of magnitude\"，假设 confounds 独立作用。Checkpoint (~2pp) + eval seq_length (~9pp) + preprocessing (~7.68pp) 可能 compound。R2 补充：confounds 大部分对 CWM 不利方向一致，不太可能反转方向，但 gap 精确大小不可靠。\n→ **修复方向**: §5.6 增加 worst-case compound scenario 讨论。\n\n**W8. TRAJ 比较存在 5 重未控制混淆因素。** [R2-W3, R1 扩展]\n训练数据量 (~400 vs ~70K)、LR (2e-4 vs 5e-5)、评估粒度 (variant vs per-test)、checkpoint 策略 (W2)、label 粒度。Downsample ablation 仅控制第 1 个。CLS-TRAJ repo-level 比较严格来说 uninterpretable。\n→ **修复方向**: 明确标注 CLS-TRAJ repo-level 为 preliminary/suggestive，contribution list 相应降级。\n\n**W9. Abstract 数字密度过高。** [R2-W2, R1 AGREE; 跨 3 轮未解决]\n约 170 words 含 p=0.007、±2pp、5 seeds、19-26pp、90.63%、+3.12pp、217× 等密集数据。审稿人 30 秒内难以判断核心价值。\n→ **修复方向**: 保留 1-2 个关键数字，其余定性描述。\n\n**W10. Related Work 第一段以枚举代替定位。** [R2-W1, R1 AGREE]\n8 行内堆砌 ~18 引用，\"A proposed X, B proposed Y\" 列表式写法。缺乏按 formulation 类型的归纳和本文定位分析。\n→ **修复方向**: 按 formulation 类型重组，提炼共性和局限性。\n\n**W11. Introduction 贡献列表过长（~350 words，含大量具体数字）。** [R2-W4, R1 AGREE]\n→ **修复方向**: 每条 1-2 句，具体数字移至 Results。\n\n**W12. Post-hoc power analysis 方法论不当。** [R1-W6, R2 部分 AGREE]\nObserved power 是 p 值单调函数（Hoenig & Heisey 2001）。R2 认为用作诊断工具解释 CLS-TRAJ 不具结论性比 confirmatory 用法更可接受。\n→ **修复方向**: 引用 Hoenig & Heisey，重新表述为 minimum detectable effect。\n\n**W13. NF4 vs bf16 混合 5-seed 分析缺乏正式交互检验。** [R1-W7, R2 AGREE]\n→ **修复方向**: 报告 bf16-only TOST 结果。\n\n**W14. Cross-model CWM eval seq_length 不一致但仍作为 consistency 证据。** [R1-W8, R2 AGREE]\n→ **修复方向**: 弱化 cross-model CWM consistency 措辞。\n\n### Minor\n\n**M1.** \"pp\" (percentage points) 缩写全文未定义。[R2-W5, R1 AGREE]\n**M2.** Prompt templates（CLS/CWM/TRAJ）未在论文或 Appendix 中展示。[R1-W9, R2 AGREE]\n**M3.** Mutation operators 选择理由和实现细节缺失。[R1-W11, R2 AGREE]\n**M4.** Table 4 脚注密度极高（4 个不同标记）。[R2-M3, R1 AGREE]\n**M5.** Checklist C4 回答 \"Partially\"（package version numbers），提交前需补全。[R2-M2]\n**M6.** 少量 trailing -ing phrases（如 \"motivating complexity-aware routing...\"）。[R2-M1]\n**M7.** Oracle ensemble (90.63%) 仅报告单 seed，应报告多 seed 范围。[R1-W13, R2 降级]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成共识：\n\n1. **页数超限是最紧迫问题** — 可能 desk reject [R1 AGREE, R2 首提]\n2. **Repo-level 单种子是核心 limitation** — 效应量大到不太可能反转，但与 function-level 标准形成不对称 [共识]\n3. **TRAJ checkpoint 不一致** — 需统一协议 [共识]\n4. **Table 4 混合粒度** — 需拆分或增加 variant-level 列 [共识]\n5. **Abstract 数字密度过高** — 跨 3 轮未解决 [共识]\n6. **Related Work 枚举式** — 需 positioning 重写 [共识]\n7. **CLS-TRAJ 比较 uninterpretable** — 5 重 confound 仅控制 1 个 [共识]\n8. **Overall 3.0 (Findings)** — 两人独立给出完全一致的评分 [共识]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**分歧 1: CWM baseline 规模问题的严重性**\n- R2: \"essentially invalidates repo-level formulation-level conclusions\" [critical]\n- R1 REBUT: 论文 claim 已 conditioned on \"≤8B LoRA regime\"；matched comparison 正是论文设计目的；4-8B 实践者仍获得 actionable 指导\n- **Director 判断**: R1 论证更有说服力。论文明确 conditions 结论但需在 Abstract/Introduction 更突出\n\n**分歧 2: TOST margin a priori justification**\n- R1: 事后合理化，±1.5pp 处 borderline fail，\"结论对 margin 敏感\" [critical]\n- R2 REBUT: ±2pp 是 domain-justified SESOI；观测 gap 仅 -0.45pp；讨论 ±1.5pp vs ±2pp 对实际决策无影响\n- **Director 判断**: 均有道理。margin 应通过 SESOI 框架正式论证（R2 建议），但仍应承认 sensitivity（R1 观察）。降级为 should-fix。\n\n**分歧 3: 多重比较校正**\n- R1: 未进行多重比较校正 [major]\n- R2 REBUT: 事实性错误——论文 §4.1 Statistics 段和 Appendix K (Table 15) 明确有 Holm-Bonferroni 校正\n- **Director 验证**: 确认论文包含 Holm-Bonferroni。R1 遗漏。**此 weakness 撤回。**\n\n**分歧 4: Default-to-pass 策略公平性**\n- R2 Q4: CWM unparseable default-to-pass 是否公平？\n- R1 REBUT: default-to-pass = default-to-majority (72.96%) 是对 CWM 最 charitable 的策略；relaxed matching 反降准确率；default-to-fail 会使 CWM 更差\n- **Director 判断**: R1 论证正确。Default-to-pass 有利于 CWM，实际 gap 只会更大。此 concern 方向反了。**撤回。**\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Qwen3-8B TRAJ epoch 2 的选择是 a priori 还是 post-hoc？如果是后者，CWM 是否也检查了多个 epoch？[R1-Q1, 共识]\n\n**Q2.** Function-level TOST 限制为 bf16 seeds（排除 NF4 seeds 789/0）后，p 值和结论是否成立？[R1-Q2, R2 AGREE]\n\n**Q3.** CLS/CWM/TRAJ 的 prompt template 是什么？prompt 设计是否经过优化？[R1-Q3, R2 AGREE]\n\n**Q4.** 48 个 repo-level variants 的选择标准是什么？如何从 SWE-bench Verified 500 instances 中选出？[R1-Q4]\n\n**Q5.** Table 3 fail recall 跨 configuration 变化极大（~14% to ~57%）。有多少可归因于 formulation vs configuration？[R1-Q5]\n\n**Q6.** Execution-free verification 的训练标签来自 execution。获取 execution labels 的一次性成本 vs 推理时执行的重复成本的 cost-benefit 分析？[R2-Q3]\n\n**Q7.** 5 种 mutation types 如何选择？synthetic-to-real transfer gap 是否有任何 pilot study？[R2-Q2]\n\n---\n\n## Missing References\n\n1. **Lakens (2017)**, \"Equivalence Tests: A Practical Primer...\" — TOST margin 的 SESOI 框架标准参考 [R1, R2 均建议]\n2. **Hoenig & Heisey (2001)**, \"The Abuse of Power...\" — 如保留 post-hoc power analysis [R1]\n3. **更多 grammar-constrained decoding 文献** — 论文仅引用 Outlines (Willard & Louf 2023)，但讨论了 constrained decoding 作为 CWM 改善方向 [R1, R2]\n4. **Chain-of-thought code verification** — PatchReasoner 已引用但仅一笔带过；CoT 作为 CLS-CWM 中间地带值得更深入讨论 [R2]\n\n---\n\n## 外部审稿 (Stanford Agentic Reviewer)\n\n**状态：未配置**（`external_review.paperreview_ai.enabled` 未设置）。跳过。\n\n---\n\n## Overall Assessment\n\n### 评分: **3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 3/5 | **3.0/5** |\n| Excitement | 3/5 | 3/5 | **3.0/5** |\n| Reproducibility | 3/5 | 3/5 | **3.0/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 综合判断\n\n论文填补了一个确实存在的文献空白（matched formulation comparison），function-level 方法论严谨且结论可信。但以下因素共同将论文定位在 Findings 而非 Conference 水平：\n\n1. **格式硬伤**：正文超 8 页限制 ~3 页，提交前必须修复，否则 desk reject。\n2. **方法论不对称**：论文最有价值的发现（repo-level divergence）恰好依赖最薄弱的证据基础（单种子、多重 confound、CWM baseline 规模限制）。Function-level equivalence（最 robust 的结论）在直觉上 somewhat expected。\n3. **新颖性有限**：无新方法提出；核心发现（分类在长输出场景优于生成）从 autoregressive error compounding 原理可预期；\"design space\" 仅 3 个离散点。\n4. **Generalizable insight 不足**：所有 repo-level 结论 conditioned on ≤8B LoRA regime，CWM baseline 与原始 32B CWM 本质不同。论文对此足够诚实，但 conditioned 的结论天然限制了 impact。\n\n**积极因素**：透明度罕见（Threats to Validity 自省式暴露 5 个 confounds）；failure mode taxonomy 和 error complementarity 有实操价值；统计方法论在 function-level 达到高标准。论文是一篇 solid empirical study，适合 Findings。\n\n### 对 Research Director 的信号\n\n- **W1（页数超限）** 和 **W9（Abstract 数字密度）** 是纯写作/格式问题，不涉及新实验，可在截止日期前修复。\n- **W2（TRAJ checkpoint）** 和 **W3（Table 4 混合粒度）** 需要重新组织呈现方式，工作量中等。\n- **W5（repo-level 单种子）** 需要新实验（如可行）或措辞降级。\n- 其余 should-fix 项多为措辞和呈现优化。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 数字密度过高（跨 3 轮反复指出），需大幅精简。保留 function-level equivalence 和 repo-level 19-26pp gap，删减 p 值、oracle accuracy、具体百分比组。\n- \"motivating complexity-aware routing over uniform formulation selection\" 是 trailing -ing phrase（M6）。\n- \"pp\" 首次出现未定义（M1）。\n\n### Introduction\n- 问题定义和 gap identification 清晰有效。\n- Contribution list 过长（~350 words），具体数字应移至 Results。第二条 contribution 单条 ~120 words。\n- \"The results reveal a three-layer structure\" 概括有力，但后续展开过于详细。\n- 每条 contribution 有对应 section/table 支撑。Contribution 2 的 hedging（\"Evidence for...with identified confounds\"）诚实。\n- Contribution 3（error complementarity）仅基于 function-level 单 seed，claim weight 与 evidence 不对称。\n\n### Method\n- Formulation 定义清晰，notation 一致。\n- §3.2 failure mode 先验分析是亮点——为后续实验提供了 testable predictions，大部分被验证。\n- §3.3 oracle framework 使用 function-level ICC (0.191) 估算 repo-level oracle advantage 是 conservative 的，论文正确标注。\n\n### Experiments\n- **过长**（占全文 5-6 页），是超页数的主因。\n- §4.1 Setup: 数据集描述清楚，split 和 baseline 完整。\"zero problem overlap\" 是正面设计。Holm-Bonferroni 在 Statistics 段提及。\n- §4.2 Function-level: 最 solid 的部分。5-seed、两个模型家族、appropriate statistical tests。\n- §4.3 Scaling: 仅 2 seeds (bf16 only)。CWM flat scaling 的 hedging 合理。\n- §4.4 TOST: 统计方法本身正确。Sensitivity table 在 Appendix。但 SESOI 框架引用缺失。\n- §4.5 Repo-level: 最大 confound 集中区。Default assignment artifact 分析是亮点。Constrained decoding 段和 Training/evaluation sensitivity 段可移入 Appendix。\n- §4.6 Analysis: Aggregation penalty 分析深入。Checkpoint selection confound 是重要观察。\n- §5 Threats: 全面诚实，缺 compound effect 讨论。\n- TRAJ checkpoint 不一致（W2）需修复。\n\n### Related Work\n- 第一段需从 enumeration 重写为 synthesis。PRM/ORM 类比（第二段）处理得当。\n- 引用量充分（58 篇），近期工作补充基本到位。缺 constrained decoding 更广文献和 CoT verification 深入讨论。\n\n### Conclusion\n- 简洁有效，practical recommendations 有实用价值。\n- 措辞审慎（\"under standard LoRA fine-tuning (≤8B)\"）。\n\n### Limitations\n- 独立 \\section*，符合 ARR 要求。内容诚实全面。\n\n### Checklist\n- 认真填写。C4 \"Partially\" 需补全 version numbers。\n\n### Appendix\n- 内容丰富且与正文交叉引用完整。\n- Variant-level accuracy table (Table 6) 是理解 Table 4 的必要补充，建议在正文中更突出引用。\n- Holm-Bonferroni (Appendix K) 是方法论亮点。\n- 部分正文内容（Threats to Validity, sensitivity details）应移入以解决超页。\n\n---\n\n## 与历史 Issue Tracker 对比\n\n### Round 4 → Round 5 进展\n- **已解决 (6 项)**: R4-W3 (cross-model wording → 'consistency check')、R4-W5 (多重比较 → Holm-Bonferroni 完成)、R4-W8 (遗漏 CodePRM/FunPRM → 已引用)、R4-M2 (default-to-pass 讨论 → §4.5 完成)、R4-M6 (stagnation → flat scaling)、R3-W1 (Limitations section → 独立 section)\n- **部分改善 (5 项)**: R4-N1 (TOST sensitivity → table 完成但需 SESOI 框架)、R4-N2 (Controlled → Systematic title)、R4-N3 (power analysis → 完成但方法论需改善)、R4-W1 (CWM conditioning → Conclusion/Threats 有但 Abstract 缺)、R4-W7 (oracle scope → function-level 限定已加)\n- **未解决 (2 项)**: R4-W2/R3-W2 (Abstract 数字密度 → 跨 3 轮未解决)、R4-W4 (novelty positioning)\n- **新增 (7 项)**: R5-N1 (页数超限)、R5-N2 (TRAJ checkpoint)、R5-N3 (Table 4 混合粒度)、R5-W4 (confound 累积)、R5-W5 (post-hoc power)、R5-W8 (Related Work 枚举)、R5-W11 (贡献列表过长)",
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 5 (Fresh Review)\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计方法; R2: 新颖性+写作质量+相关工作+格式合规）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free code verification formulation（CLS 分类、CWM 生成、TRAJ 轨迹级），使用 Qwen3-4B/8B 和 DeepSeek-Coder-6.7B + LoRA 在 function-level 和 repo-level 上进行实验。Function-level 三种方法近等效（TOST p=0.007, 5 seeds）；repo-level CLS 以 19-26pp 大幅领先 CWM。论文统计方法论在 function-level 达到上游水准，但 repo-level 核心发现受单种子、CWM baseline 规模限制、以及多重 confound 累积的制约。**正文约 11 页，超出 ARR Long Paper 8 页硬限制，是最紧迫的格式问题。**\n\n---\n\n## Strengths\n\n**S1.** 首个在 matched conditions 下比较三种 verification formulation 的系统研究，填补了确实存在的文献空白。[R1 S1, R2 S1, 共识]\n\n**S2.** Function-level 统计方法论极为扎实：5 seeds、两个模型家族、TOST equivalence test + clustered bootstrap (114 clusters, 10K resamples) + ICC + Holm-Bonferroni 多重比较校正。在 ML 实验论文中属于上游水准。[R1 S2, R2 S2, 共识]\n\n**S3.** 对 confounds 和 limitations 的透明度罕见。Section 5 (Threats to Validity) 系统性列出 5 个 confounds 并量化每个 confound 的 observed effect。多数论文不会主动暴露如此深度的局限性。[R1 S3, R2 S3, 共识]\n\n**S4.** Default assignment artifact 分析（§4.5）精彩：CWM 4B→8B \"伪改善\"的解构（unparseable rate 上升 → majority-class default → accuracy 虚增，parseable-only accuracy 实际下降）展示了评估指标如何误导。[R1 S4, 共识]\n\n**S5.** Failure mode taxonomy (Table 3: format collapse, decision collapse, aggregation penalty) 提供了可操作的诊断框架。同一模型家族在不同 configuration 下表现出不同 failure mode 的发现对理解 formulation × configuration 交互有实质贡献。[R1 S6, R2 S4, 共识]\n\n**S6.** 消融设计充分：LoRA rank ablation、matched-context ablation（确认 input disparity 仅解释 <3% gap）、training data downsample（控制数据量差异）、majority voting ablation、relaxed matching ablation。[R1 S5]\n\n**S7.** 217× throughput advantage 的量化有实际部署参考意义。[R2 S5]\n\n**S8.** 写作无明显 AI 风格痕迹（无 em-dash/en-dash、无黑名单用词），引用完整（58 篇验证无幻觉引用）。[R2 S6, S7]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [Critical] 正文超出 ARR Long Paper 8 页限制（~11 页）。** [R2-N1, R1 AGREE]\nPDF 渲染约 11 页正文，超出 2-3 页。ARR 硬约束，可能直接 desk reject。Experiments section 含 5 个 subsection + 5 张 table + 2 张 figure 是主因。\n→ **修复方向**: Threats to Validity 移入 Appendix 并在正文保留一段概述；压缩 Repo-Level 的 Default assignment artifact / Constrained decoding / Training and evaluation sensitivity 段落至 Appendix；精简 Introduction 贡献列表。\n\n**W2. [Critical] TRAJ checkpoint selection 协议不一致。** [R1-W1, R2 AGREE]\n论文协议：NaN validation loss 时使用 final epoch。CWM 所有 repo-level runs 遵循此协议。但 Qwen3-8B TRAJ 手动选择了 epoch 2 (72.92%) 而非 Trainer 默认 epoch 3 (70.83%)。Table 4 脚注 ♦ 记录了此选择。虽然绝对影响有限（~2pp），但构成协议不一致和 cherry-picking 嫌疑。\n→ **修复方向**: 统一 checkpoint 策略，report 两组数字，明确标注 epoch 2 选择是 post-hoc 的。\n\n**W3. [Critical] Table 4 混合 per-test (n=9,784) 和 variant-level (n=48) 指标。** [R1-W2, R2 AGREE]\nCLS/CWM per-test accuracy 与 TRAJ variant-level accuracy 并排展示，脚注 ‡ 标注容易被忽略。CLS variant-level accuracy 远低于其 per-test accuracy（如 Qwen3-4B: 83.63% → 64.58%），读者若将 CLS per-test 与 TRAJ variant-level 直接比较会严重误判优劣。\n→ **修复方向**: 拆分为 per-test 和 variant-level 两个表，或增加 CLS variant-level 列。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4. CWM baseline ≤8B LoRA 的条件限制在 Abstract/Introduction 不够突出。** [R2-N2 提出, R1 部分 REBUT]\n4-8B LoRA CWM ≠ 32B mid-trained CWM。论文 Conclusion/Threats 已有 \"at ≤8B LoRA scale\" conditioning，但 Abstract 和 Introduction contribution list 未体现。R2 认为此差距 \"essentially invalidates\" repo-level 结论；R1 反驳 \"invalidates\" 过强——matched comparison 正是论文设计目的，conditioned claim 合理。**Director 判断**：R1 论证更有说服力，但 conditioning 确需更突出。\n→ **修复方向**: Abstract 和 Introduction contribution list 中加入 \"under ≤8B LoRA fine-tuning\" 条件限定。\n\n**W5. Repo-level 核心发现依赖单种子。** [R2-N3, R1 AGREE with nuance]\nQwen3 repo-level CLS vs CWM 为单种子 (s42)；variant 评估 n=48。与 function-level 5-seed 标准形成方法论不对称。R1 补充：效应量 19-26pp 远超 function-level seed noise (<2pp)，CI lower bound 10.42pp 仍 substantial，cross-model 方向一致。两人共识：limitation 真实但效应量大到不太可能被 seed noise 反转。\n→ **修复方向**: 如可行补充第二个 repo-level seed；否则将措辞从 \"evidence\" 降级为 \"preliminary evidence\"。\n\n**W6. TOST ±2pp margin 需改善正当性论证。** [R1-W3 提出, R2 部分 REBUT]\nR1 认为缺乏 a priori justification；R2 反驳 ±2pp 是 code verification 场景中 defensible SESOI，观测 gap 仅 -0.45pp，讨论 ±1.5pp vs ±2pp 对实际决策几乎无影响。两人共识：需引用 Lakens (2017) SESOI 框架正式论证。Sensitivity table (Appendix E) 已有。\n→ **修复方向**: §4.4 引用 Lakens (2017)，正式论证 ±2pp 选择依据。\n\n**W7. Confounds 累积效应未讨论。** [R1-W4, R2 AGREE]\n§5.6 声称 gap \"exceeds any individual confound's observed effect by an order of magnitude\"，假设 confounds 独立作用。Checkpoint (~2pp) + eval seq_length (~9pp) + preprocessing (~7.68pp) 可能 compound。R2 补充：confounds 大部分对 CWM 不利方向一致，不太可能反转方向，但 gap 精确大小不可靠。\n→ **修复方向**: §5.6 增加 worst-case compound scenario 讨论。\n\n**W8. TRAJ 比较存在 5 重未控制混淆因素。** [R2-W3, R1 扩展]\n训练数据量 (~400 vs ~70K)、LR (2e-4 vs 5e-5)、评估粒度 (variant vs per-test)、checkpoint 策略 (W2)、label 粒度。Downsample ablation 仅控制第 1 个。CLS-TRAJ repo-level 比较严格来说 uninterpretable。\n→ **修复方向**: 明确标注 CLS-TRAJ repo-level 为 preliminary/suggestive，contribution list 相应降级。\n\n**W9. Abstract 数字密度过高。** [R2-W2, R1 AGREE; 跨 3 轮未解决]\n约 170 words 含 p=0.007、±2pp、5 seeds、19-26pp、90.63%、+3.12pp、217× 等密集数据。审稿人 30 秒内难以判断核心价值。\n→ **修复方向**: 保留 1-2 个关键数字，其余定性描述。\n\n**W10. Related Work 第一段以枚举代替定位。** [R2-W1, R1 AGREE]\n8 行内堆砌 ~18 引用，\"A proposed X, B proposed Y\" 列表式写法。缺乏按 formulation 类型的归纳和本文定位分析。\n→ **修复方向**: 按 formulation 类型重组，提炼共性和局限性。\n\n**W11. Introduction 贡献列表过长（~350 words，含大量具体数字）。** [R2-W4, R1 AGREE]\n→ **修复方向**: 每条 1-2 句，具体数字移至 Results。\n\n**W12. Post-hoc power analysis 方法论不当。** [R1-W6, R2 部分 AGREE]\nObserved power 是 p 值单调函数（Hoenig & Heisey 2001）。R2 认为用作诊断工具解释 CLS-TRAJ 不具结论性比 confirmatory 用法更可接受。\n→ **修复方向**: 引用 Hoenig & Heisey，重新表述为 minimum detectable effect。\n\n**W13. NF4 vs bf16 混合 5-seed 分析缺乏正式交互检验。** [R1-W7, R2 AGREE]\n→ **修复方向**: 报告 bf16-only TOST 结果。\n\n**W14. Cross-model CWM eval seq_length 不一致但仍作为 consistency 证据。** [R1-W8, R2 AGREE]\n→ **修复方向**: 弱化 cross-model CWM consistency 措辞。\n\n### Minor\n\n**M1.** \"pp\" (percentage points) 缩写全文未定义。[R2-W5, R1 AGREE]\n**M2.** Prompt templates（CLS/CWM/TRAJ）未在论文或 Appendix 中展示。[R1-W9, R2 AGREE]\n**M3.** Mutation operators 选择理由和实现细节缺失。[R1-W11, R2 AGREE]\n**M4.** Table 4 脚注密度极高（4 个不同标记）。[R2-M3, R1 AGREE]\n**M5.** Checklist C4 回答 \"Partially\"（package version numbers），提交前需补全。[R2-M2]\n**M6.** 少量 trailing -ing phrases（如 \"motivating complexity-aware routing...\"）。[R2-M1]\n**M7.** Oracle ensemble (90.63%) 仅报告单 seed，应报告多 seed 范围。[R1-W13, R2 降级]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成共识：\n\n1. **页数超限是最紧迫问题** — 可能 desk reject [R1 AGREE, R2 首提]\n2. **Repo-level 单种子是核心 limitation** — 效应量大到不太可能反转，但与 function-level 标准形成不对称 [共识]\n3. **TRAJ checkpoint 不一致** — 需统一协议 [共识]\n4. **Table 4 混合粒度** — 需拆分或增加 variant-level 列 [共识]\n5. **Abstract 数字密度过高** — 跨 3 轮未解决 [共识]\n6. **Related Work 枚举式** — 需 positioning 重写 [共识]\n7. **CLS-TRAJ 比较 uninterpretable** — 5 重 confound 仅控制 1 个 [共识]\n8. **Overall 3.0 (Findings)** — 两人独立给出完全一致的评分 [共识]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**分歧 1: CWM baseline 规模问题的严重性**\n- R2: \"essentially invalidates repo-level formulation-level conclusions\" [critical]\n- R1 REBUT: 论文 claim 已 conditioned on \"≤8B LoRA regime\"；matched comparison 正是论文设计目的；4-8B 实践者仍获得 actionable 指导\n- **Director 判断**: R1 论证更有说服力。论文明确 conditions 结论但需在 Abstract/Introduction 更突出\n\n**分歧 2: TOST margin a priori justification**\n- R1: 事后合理化，±1.5pp 处 borderline fail，\"结论对 margin 敏感\" [critical]\n- R2 REBUT: ±2pp 是 domain-justified SESOI；观测 gap 仅 -0.45pp；讨论 ±1.5pp vs ±2pp 对实际决策无影响\n- **Director 判断**: 均有道理。margin 应通过 SESOI 框架正式论证（R2 建议），但仍应承认 sensitivity（R1 观察）。降级为 should-fix。\n\n**分歧 3: 多重比较校正**\n- R1: 未进行多重比较校正 [major]\n- R2 REBUT: 事实性错误——论文 §4.1 Statistics 段和 Appendix K (Table 15) 明确有 Holm-Bonferroni 校正\n- **Director 验证**: 确认论文包含 Holm-Bonferroni。R1 遗漏。**此 weakness 撤回。**\n\n**分歧 4: Default-to-pass 策略公平性**\n- R2 Q4: CWM unparseable default-to-pass 是否公平？\n- R1 REBUT: default-to-pass = default-to-majority (72.96%) 是对 CWM 最 charitable 的策略；relaxed matching 反降准确率；default-to-fail 会使 CWM 更差\n- **Director 判断**: R1 论证正确。Default-to-pass 有利于 CWM，实际 gap 只会更大。此 concern 方向反了。**撤回。**\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Qwen3-8B TRAJ epoch 2 的选择是 a priori 还是 post-hoc？如果是后者，CWM 是否也检查了多个 epoch？[R1-Q1, 共识]\n\n**Q2.** Function-level TOST 限制为 bf16 seeds（排除 NF4 seeds 789/0）后，p 值和结论是否成立？[R1-Q2, R2 AGREE]\n\n**Q3.** CLS/CWM/TRAJ 的 prompt template 是什么？prompt 设计是否经过优化？[R1-Q3, R2 AGREE]\n\n**Q4.** 48 个 repo-level variants 的选择标准是什么？如何从 SWE-bench Verified 500 instances 中选出？[R1-Q4]\n\n**Q5.** Table 3 fail recall 跨 configuration 变化极大（~14% to ~57%）。有多少可归因于 formulation vs configuration？[R1-Q5]\n\n**Q6.** Execution-free verification 的训练标签来自 execution。获取 execution labels 的一次性成本 vs 推理时执行的重复成本的 cost-benefit 分析？[R2-Q3]\n\n**Q7.** 5 种 mutation types 如何选择？synthetic-to-real transfer gap 是否有任何 pilot study？[R2-Q2]\n\n---\n\n## Missing References\n\n1. **Lakens (2017)**, \"Equivalence Tests: A Practical Primer...\" — TOST margin 的 SESOI 框架标准参考 [R1, R2 均建议]\n2. **Hoenig & Heisey (2001)**, \"The Abuse of Power...\" — 如保留 post-hoc power analysis [R1]\n3. **更多 grammar-constrained decoding 文献** — 论文仅引用 Outlines (Willard & Louf 2023)，但讨论了 constrained decoding 作为 CWM 改善方向 [R1, R2]\n4. **Chain-of-thought code verification** — PatchReasoner 已引用但仅一笔带过；CoT 作为 CLS-CWM 中间地带值得更深入讨论 [R2]\n\n---\n\n## 外部审稿 (Stanford Agentic Reviewer)\n\n**状态：未配置**（`external_review.paperreview_ai.enabled` 未设置）。跳过。\n\n---\n\n## Overall Assessment\n\n### 评分: **3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 3/5 | **3.0/5** |\n| Excitement | 3/5 | 3/5 | **3.0/5** |\n| Reproducibility | 3/5 | 3/5 | **3.0/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 综合判断\n\n论文填补了一个确实存在的文献空白（matched formulation comparison），function-level 方法论严谨且结论可信。但以下因素共同将论文定位在 Findings 而非 Conference 水平：\n\n1. **格式硬伤**：正文超 8 页限制 ~3 页，提交前必须修复，否则 desk reject。\n2. **方法论不对称**：论文最有价值的发现（repo-level divergence）恰好依赖最薄弱的证据基础（单种子、多重 confound、CWM baseline 规模限制）。Function-level equivalence（最 robust 的结论）在直觉上 somewhat expected。\n3. **新颖性有限**：无新方法提出；核心发现（分类在长输出场景优于生成）从 autoregressive error compounding 原理可预期；\"design space\" 仅 3 个离散点。\n4. **Generalizable insight 不足**：所有 repo-level 结论 conditioned on ≤8B LoRA regime，CWM baseline 与原始 32B CWM 本质不同。论文对此足够诚实，但 conditioned 的结论天然限制了 impact。\n\n**积极因素**：透明度罕见（Threats to Validity 自省式暴露 5 个 confounds）；failure mode taxonomy 和 error complementarity 有实操价值；统计方法论在 function-level 达到高标准。论文是一篇 solid empirical study，适合 Findings。\n\n### 对 Research Director 的信号\n\n- **W1（页数超限）** 和 **W9（Abstract 数字密度）** 是纯写作/格式问题，不涉及新实验，可在截止日期前修复。\n- **W2（TRAJ checkpoint）** 和 **W3（Table 4 混合粒度）** 需要重新组织呈现方式，工作量中等。\n- **W5（repo-level 单种子）** 需要新实验（如可行）或措辞降级。\n- 其余 should-fix 项多为措辞和呈现优化。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 数字密度过高（跨 3 轮反复指出），需大幅精简。保留 function-level equivalence 和 repo-level 19-26pp gap，删减 p 值、oracle accuracy、具体百分比组。\n- \"motivating complexity-aware routing over uniform formulation selection\" 是 trailing -ing phrase（M6）。\n- \"pp\" 首次出现未定义（M1）。\n\n### Introduction\n- 问题定义和 gap identification 清晰有效。\n- Contribution list 过长（~350 words），具体数字应移至 Results。第二条 contribution 单条 ~120 words。\n- \"The results reveal a three-layer structure\" 概括有力，但后续展开过于详细。\n- 每条 contribution 有对应 section/table 支撑。Contribution 2 的 hedging（\"Evidence for...with identified confounds\"）诚实。\n- Contribution 3（error complementarity）仅基于 function-level 单 seed，claim weight 与 evidence 不对称。\n\n### Method\n- Formulation 定义清晰，notation 一致。\n- §3.2 failure mode 先验分析是亮点——为后续实验提供了 testable predictions，大部分被验证。\n- §3.3 oracle framework 使用 function-level ICC (0.191) 估算 repo-level oracle advantage 是 conservative 的，论文正确标注。\n\n### Experiments\n- **过长**（占全文 5-6 页），是超页数的主因。\n- §4.1 Setup: 数据集描述清楚，split 和 baseline 完整。\"zero problem overlap\" 是正面设计。Holm-Bonferroni 在 Statistics 段提及。\n- §4.2 Function-level: 最 solid 的部分。5-seed、两个模型家族、appropriate statistical tests。\n- §4.3 Scaling: 仅 2 seeds (bf16 only)。CWM flat scaling 的 hedging 合理。\n- §4.4 TOST: 统计方法本身正确。Sensitivity table 在 Appendix。但 SESOI 框架引用缺失。\n- §4.5 Repo-level: 最大 confound 集中区。Default assignment artifact 分析是亮点。Constrained decoding 段和 Training/evaluation sensitivity 段可移入 Appendix。\n- §4.6 Analysis: Aggregation penalty 分析深入。Checkpoint selection confound 是重要观察。\n- §5 Threats: 全面诚实，缺 compound effect 讨论。\n- TRAJ checkpoint 不一致（W2）需修复。\n\n### Related Work\n- 第一段需从 enumeration 重写为 synthesis。PRM/ORM 类比（第二段）处理得当。\n- 引用量充分（58 篇），近期工作补充基本到位。缺 constrained decoding 更广文献和 CoT verification 深入讨论。\n\n### Conclusion\n- 简洁有效，practical recommendations 有实用价值。\n- 措辞审慎（\"under standard LoRA fine-tuning (≤8B)\"）。\n\n### Limitations\n- 独立 \\section*，符合 ARR 要求。内容诚实全面。\n\n### Checklist\n- 认真填写。C4 \"Partially\" 需补全 version numbers。\n\n### Appendix\n- 内容丰富且与正文交叉引用完整。\n- Variant-level accuracy table (Table 6) 是理解 Table 4 的必要补充，建议在正文中更突出引用。\n- Holm-Bonferroni (Appendix K) 是方法论亮点。\n- 部分正文内容（Threats to Validity, sensitivity details）应移入以解决超页。\n\n---\n\n## 与历史 Issue Tracker 对比\n\n### Round 4 → Round 5 进展\n- **已解决 (6 项)**: R4-W3 (cross-model wording → 'consistency check')、R4-W5 (多重比较 → Holm-Bonferroni 完成)、R4-W8 (遗漏 CodePRM/FunPRM → 已引用)、R4-M2 (default-to-pass 讨论 → §4.5 完成)、R4-M6 (stagnation → flat scaling)、R3-W1 (Limitations section → 独立 section)\n- **部分改善 (5 项)**: R4-N1 (TOST sensitivity → table 完成但需 SESOI 框架)、R4-N2 (Controlled → Systematic title)、R4-N3 (power analysis → 完成但方法论需改善)、R4-W1 (CWM conditioning → Conclusion/Threats 有但 Abstract 缺)、R4-W7 (oracle scope → function-level 限定已加)\n- **未解决 (2 项)**: R4-W2/R3-W2 (Abstract 数字密度 → 跨 3 轮未解决)、R4-W4 (novelty positioning)\n- **新增 (7 项)**: R5-N1 (页数超限)、R5-N2 (TRAJ checkpoint)、R5-N3 (Table 4 混合粒度)、R5-W4 (confound 累积)、R5-W5 (post-hoc power)、R5-W8 (Related Work 枚举)、R5-W11 (贡献列表过长)",
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 436 · 2026-05-19T09:57:33.390994+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4322
}
```

</details>

---


### Assistant

_source line 437 · 2026-05-19T09:57:48.672830+00:00_

审稿报告已投递至 Research Director。

**Round 5 审稿完成。**

核心结论：**Overall 3.0 (Findings)**，两位 Reviewer 独立给出完全一致的评分。

关键发现汇总：

| 优先级 | 问题 | 共识状态 |
|--------|------|----------|
| **Must-Fix** | 正文超 8 页限制（~11 页），desk reject 风险 | 两人 AGREE |
| **Must-Fix** | TRAJ checkpoint 选择协议不一致 | 两人 AGREE |
| **Must-Fix** | Table 4 混合 per-test / variant-level 指标 | 两人 AGREE |
| Should-Fix | CWM ≤8B 条件限制在 Abstract/Intro 不够突出 | 轻度分歧，R1 论证更有说服力 |
| Should-Fix | Repo-level 单种子 | 共识（效应量大缓解风险） |
| Should-Fix | Abstract 数字密度过高 | 共识（跨 3 轮未解决） |

**积极进展**：Round 4 的 6 项 issue 已解决（Holm-Bonferroni、cross-model wording、CodePRM/FunPRM 引用等），5 项部分改善。

**最紧迫行动**：页数压缩（Threats to Validity 移入 Appendix + Repo-Level 细节段落压缩）和 Abstract 精简，均为纯写作任务，可在截止日期前完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 438 · 2026-05-19T09:57:50.182962+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 的逐条交叉回应，主要结论：

- **REBUT 2 条**：W5（多重比较校正）事实性错误，论文明确使用了 Holm-Bonferroni；W13（oracle 单种子）影响有限
- **AGREE 11 条**：W1（TRAJ checkpoint 不一致）、W2（Table 混合粒度）、W4（confounds 累积）、W6-W12 等
- **部分 REBUT 1 条**：W3（TOST margin），论文的 ±2pp 在部署场景中是 defensible 的 SESOI

两位 Reviewer 评分一致（3.0 Findings），但侧重点互补：R1 关注统计方法论严格性，我关注新颖性和 CWM baseline 公平性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 439 · 2026-05-19T09:58:07.183613+00:00_

审稿流程已完成。

**Round 5 汇总报告已投递至 Research Director。**

最终结论：**Overall 3.0 (Findings)**，两位 Reviewer 独立评分完全一致。

关键发现摘要：
- **Must-Fix 3 项**：正文超 8 页限制（~11 页，desk reject 风险）、TRAJ checkpoint 选择不一致、Table 4 混合粒度指标
- **Should-Fix 11 项**：CWM baseline conditioning 不够突出、repo-level 单种子、TOST margin 论证、confound 累积效应、TRAJ 5 重 confound、Abstract 数字密度（跨 3 轮未解决）、Related Work 枚举式、贡献列表过长等
- **已解决（Round 4→5 改善）6 项**：Holm-Bonferroni 校正已完成、cross-model wording 已修正、缺失引用已补充、default-to-pass 讨论已加入、Limitations 已改为独立 section、CWM stagnation 措辞已修正

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 41

## Round 41

78 recorded events


### User

_source line 440 · 2026-05-19T10:55:45.957219+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 441 · 2026-05-19T10:55:53.623575+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-19T10:55:53.624522+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-19T10:55:58.597487+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-19T10:55:58.698254+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 445 · 2026-05-19T10:56:05.328158+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 446 · 2026-05-19T10:56:05.328500+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-19T10:56:09.736391+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+mcp__agent-ml-research director reviewer",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+mcp__agent-ml-research director reviewer",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-19T10:56:09.825599+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 89
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-19T10:56:14.308409+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-19T10:56:14.409464+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-19T10:56:23.358989+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-19T10:56:23.359333+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-19T10:56:31.145656+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 454 · 2026-05-19T10:56:32.099776+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (216 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T07:07:07Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 216 个实验 — ALLOCATED 1, DONE 200, PREPARING 14, RUNNING 1\n**DONE 分布**: failed 47, killed 26, negative 7, success 120\n\n### GPU 占用\n- **实际运行**: 1 张 — seetacloud-westd-4x5090:cuda:0(qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval)\n\n### 💾 磁盘余量\n- **seetacloud-westd-4x5090**:\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 436G/879G 可用（已用 48%）\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval` | seetacloud-westd-4x5090 | cuda:0 | 778328 | `…air-verifier/qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval.log` |\n\n### 📌 最近完成 (top 5)\n- `exp-downsample-cls-func-v3-eval` [failed] — 2026-05-19T07:07:03 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `exp-downsample-cls-func-v3` [success] — 2026-05-19T06:57:21\n- `deepseek-cwm-repo-s123` [failed] — 2026-05-19T04:38:19 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `repo-level-3shot-baseline` [success] — 2026-05-19T04:36:55 — CORRECTED: initial
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-19T10:56:32.100190+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-19T10:56:32.502184+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/literature_map.yaml\", \"content\": \"papers:\\n  # === Execution Simulation (5/5) ===\\n  - bibtex_key: maimon2026selfexecution\\n    title: \\\"Self-Execution Simulation Improves Coding Models\\\"\\n    authors: \\\"Maimon et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv: \\\"2604.03253\\\"\\n    doi: \\\"\\\"\\n    category: \\\"Execution Simulation\\\"\\n    verified: true\\n    abstract_snippet: \\\"Train code LLMs to simulate program execution step-by-step; self-verification by filtering code solutions based on predicted output.\\\"\\n    relevance: \\\"Closest prior work — trains LLMs for execution prediction via generation, we reformulate as classification.\\\"\\n\\n  - bibtex_key: meta2025cwm\\n    title: \\\"CWM: An Open-Weights LLM for Research on Code Generation with World Models\\\"\\n    authors: \\\"Meta AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv: \\\"2510.02387\\\"\\n    doi: \\\"\\\"\\n    category: \\\"Execution Simulation\\\"\\n    verified: true\\n    abstract_snippet: \\\"32B open-weights LLM mid-trained on Python execution traces; 65.8% on SWE-bench Verified.\\\"\\n    relevance: \\\"Production-scale CWM approach; our CWM baseline follows their generation formulation at smaller scale.\\\"\\n\\n  - bibtex_key: liu2024codemind\\n    title: \\\"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv: \\\"2402.09664\\\"\\n    doi: \\\"\\\"\\n    category: \\\"Execution Simulation\\\"\\n    verified: true\\n    abstract_snippet: \\\"Framework for evaluating LLM code reasoning: IER, DER, SR, DSR tasks. Performance drops with higher complexity.\\\"\\n    relevance: \\\"Evaluates execution reasoning capabilities; our work proposes classification as more robust formulat
…[truncated 4019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-19T10:56:32.502567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-19T10:56:38.329100+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the web search results, I found information about paper submission guidelines for major
…[truncated 1397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 5826
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-19T10:56:45.663582+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-19T10:56:45.764432+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines page limit template"
  }
}
```

</details>

---


### Tool call

_source line 461 · 2026-05-19T10:56:45.764884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 462 · 2026-05-19T10:56:45.915888+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Math
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	
10	% Tables
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{tabularx}
14	
15	% Graphics
16	\usepackage{graphicx}
17	\graphicspath{{../../artifacts/}}
18	
19	% Lists
20	\usepackage{enumitem}
21	
22	% Custom commands
23	\newcommand{\cls}{\textsc{Cls}}
24	\newcommand{\cwm}{\textsc{Cwm}}
25	\newcommand{\traj}{\textsc{Traj}}
26	\newcommand{\fone}{F\textsubscript{1}}
27	\newcommand{\pp}{\,\text{pp}}
28	
29	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Systematic Empirical Study}
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{abstract}
36	
37	\input{introduction}
38	
39	\begin{figure*}[t]
40	\centering
41	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
42	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
43	\label{fig:reformulation}
44	\end{figure*}
45	
46	\input{method}
47	
48	\input{experiments}
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
53	\caption{Gap amplification from function to repo level. At function level, the \cls{}--\cwm{} gap is 1--3\pp{}; at repo level, it widens to 19--26\pp{} with \cwm{} falling below majority baseline.}
54	\label{fig:scaling_gap}
55	\end{figure}
56	
57	
58	\input{related_work}
59	
60	\input{conclusion}
61	
62	\bibliography{references}
63	
64	\input{checklist}
65	
66	\input{appendix}
67	
68	\end{document}
69
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-19T10:56:51.347449+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the key information about EMNLP 2026 call for papers submission deadline:

## ARR Submission Deadline

The ARR Submission Deadline for EMNLP 2026 is May 25, 2026.
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 5683
}
```

</details>

---


### Tool result

_source line 464 · 2026-05-19T10:56:52.401695+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit template"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 author guidelines:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Template

There is an official Overleaf template. Note that this template has a [review] setting that must be on for the submission. Additionally, ARR abandons the MS Word Template for conference submissions. The submissions based on the Word template will be desk-rejected starting from March 2026.

## Key Requir
…[truncated 579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 6637
}
```

</details>

---


### Tool call

_source line 465 · 2026-05-19T10:57:04.162728+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" call for papers page limit appendix anonymity responsible NLP checklist site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" call for papers page limit appendix anonymity responsible NLP checklist site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-19T10:57:04.263696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-19T10:57:04.716928+00:00_

1	\begin{abstract}
2	Execution-free verification for LLM-based code repair can be formulated as per-test binary classification (\cls{}), execution output generation (\cwm{}), or trajectory-level patch scoring. No prior work compares these formulations under matched conditions. We present a systematic comparison across two model families, two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning.
3	
4	At function level, all three formulations achieve near-equivalent accuracy (TOST equivalence within $\pm$2\pp{}, 5 seeds). At repository level, divergence amplifies to 19--26\pp{}, with generation-based simulation falling below majority baseline. The pattern is consistent across model families but model-contingent in magnitude.
5	
6	Per-test classification provides diagnostic granularity at comparable accuracy, with configuration-dependent aggregation cost at repository level. Formulations exhibit complementary errors at function level, motivating complexity-aware routing over uniform formulation selection.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-19T10:57:04.767523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-19T10:57:05.120154+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	These three formulations represent discrete points in the verification design space, each imposing different output complexity, diagnostic granularity, and inference cost. We present the first systematic empirical comparison across two model families (Qwen3, DeepSeek-Co
…[truncated 2657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-19T10:57:05.171178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-19T10:57:05.221878+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation
…[truncated 3266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 472 · 2026-05-19T10:57:09.842587+00:00_

Web search results for query: ""EMNLP 2026" call for papers page limit appendix anonymity responsible NLP checklist site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Just What do You Think You're Doing, Dave?' A Checklist for Responsible   Data Use in NLP","url":"https://arxiv.org/pdf/2109.06598"},{"title":"Reproducibility in NLP: What Have We Learned from the Checklist?","url":"https://arxiv.org/pdf/2306.09562"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"ConfReady: A RAG based Assistant and Dataset for Conference Checklist Responses","url":"https://arxiv.org/pdf/2408.04675"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

Based on the search results for EMNLP 2026, here's what I found regarding your query about the call for papers:

**Anonymity:** Following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing process will continue to be double-blind, with reviewers not seeing authors, nor will authors see reviewers and reviews.

**Responsible NLP Checklist:** Both long and short paper submissions should follow all of the ARR submission requirements, including ACL's Publication Ethics Policy, and ARR's Ethics Policy including the responsible NLP research checklist.

**Appendix:** Regarding unlimited appendices, authors are asked not to abuse the option of an unlimited appendix and only to include material that supports the primary messages and content of the paper.

**Page Limits:** The search results did not
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 5679
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-19T10:57:14.975313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 474 · 2026-05-19T10:57:15.427747+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two model families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, which defaults to the final epoch checkpoint (affects DeepSeek s123 and all \cwm{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use 
…[truncated 16449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-19T10:57:15.428332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 476 · 2026-05-19T10:57:15.880486+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves neural code reasoning~\cite{nye2021scratchpad}, with recent work extending to full output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and execution-free error detection~\cite{li2024redo}. Verification formulations span trajectory-level reward~\cite{shum2025swerm,zhu2026codescaler}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, and learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value. None compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	Lightman et al.~\cite{lightman2023letsverify} and Uesato et al.~\cite{uesato2022solving} show process reward models (PRMs) outperform outcome reward models (ORMs) for mathematical reasoning; Math-Shepherd~\cite{wang2024mathshepherd} and OmegaPRM~\cite{luo2024omegaprm} scale process supervision via automated annotation. DreamPRM-Code~\cite{dreamprm2025code}, PRL-Coder~\cite{ye2025prlcoder}, FunPRM~\cite{zhang2026funprm}, and CodeRL+~\cite{jiang2025coderlplus} apply process-level or execution-aligned supervision to code. In the PRM/ORM framing, our \cls{} provides per-step (per-test) supervision while \traj{} provides outcome-level supervision. TOST confirms per-test and trajectory equivalence at function level ($p = 0.007$); per-test classification matches trajectory-level accuracy with additional diagnostic value. The PRM literature primarily compares supervision granularity given a fixed output format; our study additionally varies the output format itself (\cwm{} generation v
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-19T10:57:15.880938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-19T10:57:16.435050+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, all three achieve near-equivalent accuracy (TOST $p{=}0.007$, 5 seeds). At repository level under ${\leq}$8B LoRA fine-tuning, divergence amplifies to 19--26\pp{}, consistent across model families but model-contingent in magnitude (based on limited seed coverage). Per-test classification provides diagnostic granularity at comparable accuracy with 217$\times$ throughput over generation; error complementarity at function level (oracle ensemble: 90.63\%) motivates instance-level routing.
5	
6	\paragraph{Practical recommendations.} At function level, \cls{} is preferred for throughput and diagnostic signal. At repository level (${\leq}$8B), \cls{} is strongly preferred: \cwm{} falls below majority baseline (19--26\pp{} gap). Generation-based verification at repo level requires larger models or execution-trace pretraining (\S\ref{sec:threats}). When per-test diagnostics are not needed, trajectory-level scoring offers a competitive alternative with no aggregation penalty.
7	
8	\section*{Limitations}
9	
10	Most repo-level comparisons use a single seed; the gap magnitude (19--26\pp{}) exceeds any individual confound (\S\ref{sec:threats}), but definitive causal attribution requires multi-seed replication. Our \cwm{} baseline uses ${\leq}$8B LoRA fine-tuning, not the original 32B CWM with execution trace mid-training~\cite{meta2025cwm}; at larger scale, the generation bottleneck may diminish. Training data comprises synthetic mutations~\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap remains untested. \traj{} training uses variant-level labels (386 instances vs.\ ${\sim}$70K for \cls{}/\cwm{}), which limits direct comparison. A re-repair pilot ($n{=}44$, $p{=}0.42$; Appendix~\ref{app:extended_analysis}(j)) found no benefit from per-test diagnostics. Extend
…[truncated 46 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 479 · 2026-05-19T10:57:16.485749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 480 · 2026-05-19T10:57:16.788039+00:00_

1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlat
…[truncated 39104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 481 · 2026-05-19T10:57:24.062334+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 482 · 2026-05-19T10:57:25.518610+00:00_

1	% === Execution Simulation ===
2	
3	@article{maimon2026selfexecution,
4	  title={Self-Execution Simulation Improves Coding Models},
5	  author={Maimon, Gallil and Yoran, Ori and Kreuk, Felix and Hassid, Michael and Cohen, Gal and Chambon, Pierre and Adi, Yossi},
6	  journal={arXiv preprint arXiv:2604.03253},
7	  year={2026}
8	}
9	
10	@article{meta2025cwm,
11	  title={{CWM}: An Open-Weights {LLM} for Research on Code Generation with World Models},
12	  author={{FAIR CodeGen team} and Copet, Jade and Carbonneaux, Quentin and Cohen, Gal and Gehring, Jonas and Kahn, Jacob and Kossen, Jannik and Kreuk, Felix and McMilin, Emily and Meyer, Michel and Wei, Yuxiang and Zhang, David and Zheng, Kunhao and others},
13	  journal={arXiv preprint arXiv:2510.02387},
14	  year={2025}
15	}
16	
17	@article{liu2024codemind,
18	  title={{CodeMind}: A Framework to Challenge Large Language Models for Code Reasoning},
19	  author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh},
20	  journal={arXiv preprint arXiv:2402.09664},
21	  year={2024}
22	}
23	
24	@article{abdollahi2025demystifying,
25	  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},
26	  author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi},
27	  journal={arXiv preprint arXiv:2512.00215},
28	  year={2025}
29	}
30	
31	@article{lee2026solidcoder,
32	  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},
33	  author={Lee, Woojin and Huang, Jin-Xia},
34	  journal={arXiv preprint arXiv:2604.19825},
35	  year={2026}
36	}
37	
38	@article{nye2021scratchpad,
39	  title={Show Your Work: Scratchpads for Intermediate Computation with Language Models},
40	  author={Nye, Maxwell and Andreassen, Anders Johan and Gur-Ari, Guy and Michalewski, Henryk and Austin, Jacob and Biber, David and Dohan, David and Lewkowycz, Aito
…[truncated 2554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 483 · 2026-05-19T10:57:25.519116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 484 · 2026-05-19T10:57:25.619888+00:00_

1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: single-seed repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and single-seed constraints.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified unde
…[truncated 4297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-19T10:57:26.071946+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 486 · 2026-05-19T10:57:26.173026+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_framing.md\", \"content\": \"# Paper Framing — exec-sim-repair-verifier\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Extended fallback: ICSE 2027 (Jun 23 abstract, Jun 30 paper)\\n- Deadline: ARR May 25, 2026 (9 days remaining)\\n\\n## D116 Framing Pivot (2026-05-16)\\n\\n**前 framing**: \\\"CLS scales where generation fails\\\" (CLS advocacy)\\n**新 framing**: \\\"The Formulation Design Space for Neural Code Verification\\\" (empirical characterization)\\n\\n核心转变：不再主张任何 formulation 普遍更好，而是 characterize 何时用什么。\\n最强贡献重新定位：\\n1. CWM 失败模式是 **tokenizer/model-specific** 而非 formulation-inherent（Qwen 93% unparseable vs DeepSeek 11.8%）\\n2. Error complementarity: CLS/CWM 有系统性互补错误模式，oracle ensemble +2-3pp\\n3. 复杂度是 formulation 选择的关键维度（func-level 等价，repo-level 分化）\\n\\n## Core Claims (revised per D116)\\n\\n1. **Formulation Equivalence at Low Complexity**: At function-level, CLS, CWM, and TRAJ achieve statistically equivalent accuracy across two model families (Qwen3: 88.4/87.2/86.3%; DeepSeek: 86.9/86.8/84.2%). Formulation choice does not matter when execution outputs are short and structured.\\n\\n2. **Complexity-Dependent Divergence (Model-Contingent)**: At repo-level, formulation effectiveness depends on model/tokenizer properties:\\n   - Qwen3: CLS dominates CWM by 19-26pp due to 54-93% unparseable rate (tokenizer-specific CWM collapse)\\n   - DeepSeek: ⏳ **PENDING** — results determine narrative direction:\\n     - If CLS > CWM: \\\"complexity-dependent advantage is consistent across model families\\\"\\n     - If CWM ≥ CLS: \\\"advantage is model/tokenizer-contingent; CWM works when tokenizer supports structured generation\\\"\\n   - Either outcome supports the design space characterization framing\\n\\n3. **Diagnostic Granularity Without Accuracy Cost**: Per-test CLS a
…[truncated 3484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-19T10:57:34.457826+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org \"call for\" main conference papers page limit appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org \"call for\" main conference papers page limit appendix"
  }
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-19T10:57:34.960481+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 489 · 2026-05-19T10:57:36.014828+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 490 · 2026-05-19T10:57:40.433039+00:00_

Web search results for query: "site:2026.emnlp.org "call for" main conference papers page limit appendix"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Ten Simple Rules for writing algorithmic bioinformatics conference papers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7117650/"}]

Based on the search results, I found information about the main conference papers submission guidelines for EMNLP 2026. Here's what the Call for Main Conference Papers page contains:

The search returned the EMNLP 2026 Call for Main Conference Papers page. From the available content, final versions of accepted papers will be given one additional page of content (up to 9 pages), though the complete page limit specifications for initial submissions and detailed appendix guidelines for the main conference track were not fully captured in the search results excerpt.

For comparison, the Industry Track guidelines (from a related call on the same site) specify that Industry Track papers cannot exceed 6 pages in length (excluding ethical considerations and references), and references and limitations sections do not count toward the page limit, nor do the following optional sections: acknowledgements (only in the final version), ethical considerations, and appendices.

To get the complete page limit and appendix requirements for the main conference papers track specifically, you may want to visit the full page directly at: https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 5975
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-19T10:57:40.485040+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 5524
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-19T10:57:40.638605+00:00_

issues:
# === Round 5 New Critical Issues ===

- id: "R5-W1"
  summary: "正文超出 ARR Long Paper 8 页限制（~11 页），desk reject 风险"
  category: format
  severity: critical
  status: in_progress
  first_raised_round: 5
  last_seen_round: 5
  mentions:
    - round: 5
      reviewers: [1, 2]
      note: "两人共识最紧迫问题。需砍 ~3 页。"
  action_items:
    - round: 5
      action: "Paper Agent: Threats→Appendix, §4.5 details→Appendix, Intro 压缩, Table caption 压缩"
      assigned_to: "paper"
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R5-W2"
  summary: "TRAJ Qwen3-8B checkpoint 选择不一致（epoch 2 post-hoc vs epoch 3 default）"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 5
  last_seen_round: 5
  mentions:
    - round: 5
      reviewers: [1, 2]
      note: "协议不一致 + cherry-picking 嫌疑。~2pp 差距有限但需透明报告。"
  action_items:
    - round: 5
      action: "Paper Agent: Table 4 报告两组数字，标注 post-hoc"
      assigned_to: "paper"
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R5-W3"
  summary: "Table 4 混合 per-test (n=9784) 和 variant-level (n=48) 指标"
  category: format
  severity: critical
  status: in_progress
  first_raised_round: 5
  last_seen_round: 5
  mentions:
    - round: 5
      reviewers: [1, 2]
      note: "CLS per-test vs TRAJ variant-level 直接比较会误判优劣。"
  action_items:
    - round: 5
      action: "Paper Agent: Table 4 加 Variant Acc 列"
      assigned_to: "paper"
      status: in_progress
  resolution: ""
  resolution_round: null

# === Round 5 New Should-Fix Issues ===

- id: "R5-W7"
  summary: "Confounds 累积效应未讨论（独立性假设）"
  category: method
  severity: warning
  status: in_progress
  first_raised_round: 5
  last_seen_round: 5
  mentions:
    - round: 5
      reviewers: [1, 2]
      note: "Worst-case compound ~11.5pp vs 19-26pp gap。方向一致减轻风险。"
  action_items:
    - round: 5
      action: "Paper Agent: Appendix Threats 加 worst-case compound scenario"
      assigned_to: "paper"
      status: in_progress
  resolu
…[truncated 9335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 4623
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-19T10:57:47.968626+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 494 · 2026-05-19T10:57:48.019411+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 495 · 2026-05-19T10:57:57.695261+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the following specific details from this EMNLP 2026 Call for Papers page: 1) Page limits for long and short papers (submission vs camera-ready), 2) Appendix rules (allowed? page limits? reviewed?), 3) Anonymity policy (double-blind? anonymity period?), 4) Template requirements (which template/style file), 5) Key deadlines (ARR submission, commitment, notification), 6) Any special requirements about checklist, limitations section, ethics statement. Return all details verbatim as found on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract the following specific details from this EMNLP 2026 Call for Papers page: 1) Page limits for long and short papers (submission vs camera-ready), 2) Appendix rules (allowed? page limits? reviewed?), 3) Anonymity policy (double-blind? anonymity period?), 4) Template requirements (which template/style file), 5) Key deadlines (ARR submission, commitment, notification), 6) Any special requirements about checklist, limitations section, ethics statement. Return all details verbatim as found on the page."
  }
}
```

</details>

---


### Tool result

_source line 496 · 2026-05-19T10:58:02.014624+00:00_

# EMNLP 2026 Paper Submission Details

**1) Page Limits:**
- Submission: "Long Papers (8 pages) and Short Papers (4 pages)"
- Camera-ready: "one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers)"

**2) Appendix Rules:**
The page states authors should "follow all of the ARR submission requirements" and references "Optional Supplementary Materials (Appendices, Software and Data)" but provides no specific limits or review details on this page.

**3) Anonymity Policy:**
- Review process: "double-blind. Reviewers will not see authors, nor will authors see reviewers"
- Anonymity period: "Following the ACL and ARR policies, there is no anonymity period requirement"

**4) Template Requirements:**
The page directs authors to consult ARR's "Paper Submission and Templates" section but does not specify template names or style files directly.

**5) Key Deadlines:**
- ARR submission: "May 25, 2026"
- EMNLP commitment: "August 2, 2026"
- Acceptance notification: "August 20, 2026"

**6) Special Requirements:**
References required sections include "Limitations," "responsible NLP research checklist," and compliance with "ACL's Publication Ethics Policy" and "ARR's Ethics Policy," though specific checklist content isn't detailed here.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebFetch",
  "elapsed_ms": 4319
}
```

</details>

---


### Tool call

_source line 497 · 2026-05-19T10:58:09.254392+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-19T10:58:09.757057+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml\", \"content\": \"_next_id: 153\\ndecisions:\\n- id: D001\\n  date: 2026-05-11 18:01 UTC\\n  summary: 'MVP 方案: Monte Carlo oracle 模拟 + 函数级 pilot，不依赖 Docker 基础设施'\\n  rationale: '完整 Part 1 需要 Docker 重新评估 8K 个 patch 获取 per-test labels（16-24h），基础设施搭建成本高。MVP\\n    改用 Monte Carlo 模拟参数化真实测试数分布验证理论信息增益，函数级 pilot (HumanEval/MBPP) 验证可学习性。两者均无需 Docker，2-3\\n    天可完成。Pass 标准: per-test 在 70-85% 精度下 resolve rate 比 trajectory-level 高 ≥5%; 函数级\\n    pilot 精度 >70%。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-11 19:07 UTC\\n  summary: MVP-A 有条件通过：F2P-only block-corr 10.88%>5%；需补跑 Total(F2P+P2P) 模拟确认全图\\n  rationale: 真实 SWE-bench F2P median=1（69% 实例仅 1 个 F2P 测试），但 P2P median=50.5。F2P-only\\n    下 per-test 优势收窄但仍过阈值（block-corr 10.88%）。P2P regression 检测是更大的信号源——Total 分布(median=52)下优势预期更强。研究方向需校准：per-test\\n    价值主要来自 P2P regression 检测 + F2P multi-test 精确定位，而非单纯的 F2P 粒度。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: F2P-only block-corr advantage 10.88%, i.i.d. 1.98%\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-11 19:38 UTC\\n  summary: P2P regression rate 是项目关键前提——≥10% per-test 有效，<5% 则有害；需实测\\n  rationale: Total 模拟(F2P+P2P)显示 per-test 优势强烈依赖 P2P regression rate：5% 时优势为负(-1%)，10%\\n    时 13.2%，20% 时 35.7%。这是从 F2P-only 分析未发现的关键变量。真实 regression rate 未知，需从 SWE-bench\\n    数据/文献中实测。此数据点决定项目是否可行及论文 story 如何构建。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: 'Total sim: reg=5% adv=-1%, reg=10% adv=13.2%, reg=20% adv=35.7%'\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-11 20:05 UTC\\n  summary: P2P 回归率 ~1%，原始 Total 优势前提不成立；项目 reframe 而非 kill\\n  rationale: P2P 回归率 ~1%（mean=1.04%, median=0%, 仅 22.6% 错误 patch 破坏任何 P2P 测试），远低于\\n    per-test 有效的 10% 阈值。Total(F2P+P2P) 模型下 per-test 实际有害（噪声>信号）。但项目核心价值不在信
…[truncated 1464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-19T10:58:11.413917+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract: 1) Page limits for long/short papers including what counts toward the limit (references? appendix? ethics? limitations?), 2) Template name and where to get it, 3) Formatting requirements (font size, anonymization), 4) Any rules about supplementary materials or appendix. Return all details verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract: 1) Page limits for long/short papers including what counts toward the limit (references? appendix? ethics? limitations?), 2) Template name and where to get it, 3) Formatting requirements (font size, anonymization), 4) Any rules about supplementary materials or appendix. Return all details verbatim."
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-19T10:58:16.837910+00:00_

# ARR Submission Requirements Summary

## 1) Page Limits

**Long Papers:**
- "up to eight (8) pages of content"
- References: unlimited pages
- Limitations section: unlimited space after conclusion (required, doesn't count toward limit)
- Ethical considerations section: unlimited space (optional, doesn't count toward limit)

**Short Papers:**
- "up to four (4) pages of content"
- References: unlimited pages
- Limitations section: unlimited space after conclusion (required, doesn't count toward limit)
- Ethical considerations section: unlimited space (optional, doesn't count toward limit)

Note: Submissions exceeding length requirements or lacking a limitations section face desk rejection.

## 2) Template

The official formatting resource is the "ACL style template, which is available [here](https://github.com/acl-org/acl-style-files)." Authors must also consult the "\*ACL" conference formatting guidelines at [acl-org.github.io/ACLPUB/formatting.html](https://acl-org.github.io/ACLPUB/formatting.html).

## 3) Formatting Requirements

- Follow official ACL style files without modification
- Adhere to specifications for "paper size, margin width, and font size"
- Papers non-compliant with required styles "will be rejected without review"
- All text must be "addressed exclusively to the human readers and be clearly visible"

## 4) Supplementary Materials

Permitted materials include appendices, software, and data archives. Key constraints:

- Appendices follow double-column format with approved exceptions
- Must be "fully anonymized"
- Software/data submitted as single ".tgz or .zip archive"
- Cloud storage links (Dropbox, Google Drive) are prohibited
- Reviewers are not obligated to review appendix content
- Critical methodological details belong in the main paper, not appendices

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebFetch",
  "elapsed_ms": 5423
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-19T10:59:06.467017+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-19T10:59:06.568673+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-19T10:59:14.400167+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5; grep -rl \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ 2>/dev/null | head -5",
  "description": "Find project config files with external_review setting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5; grep -rl \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ 2>/dev/null | head -5",
    "description": "Find project config files with external_review setting"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-19T10:59:15.004176+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_eval_cls-v5-urgent_20260513T155329.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_infra_home-cwm-s42-e2-setup-launch_20260518T144853.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/chats/feishu_group_oc_061c4b1115e483e8fdad01cae91c873a_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/chats/feishu_group_oc_0ae20ec1ce60f9c0589d629648584eff_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/chats/archive/feishu_group_oc_061c4b1115e483e8fdad01cae91c873a_director_20260519T084400_847680.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-19T10:59:27.418467+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"NO PDF\"",
  "description": "Check if compiled PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"NO PDF\"",
    "description": "Check if compiled PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-19T10:59:27.469274+00:00_

-rw-r--r-- 1 ubuntu ubuntu 529078 May 19 10:35 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf
PDF EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-19T10:59:32.339982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-19T10:59:32.842094+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf (516.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-19T10:59:38.729691+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf",
  "pages": "9-14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf",
    "pages": "9-14"
  }
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-19T10:59:39.082912+00:00_

PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf (516.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-19T10:59:44.668988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf",
  "pages": "15-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf",
    "pages": "15-20"
  }
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-19T10:59:45.071973+00:00_

PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf (516.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-19T11:00:39.830763+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **EMNLP 2026**，ARR May cycle，截止 2026-05-25\n- Long Paper: 8 页正文（References/Limitations/Ethics 不计入）\n- ACL style template with `[review]` option\n- Double-blind，无匿名期\n- 评分标准（ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（编译 PDF: `main.pdf`）\n\n### 论文概述\n比较三种 execution-free code verification formulation（CLS per-test classification, CWM output generation, TRAJ trajectory-level scoring），在两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别（function-level, repo-level）、多种 seed 下进行系统实验。核心发现：function-level 三者等价（TOST p=0.007），repo-level CLS 领先 CWM 19-26pp。\n\n### 你的审查侧重\n\n**1. 统计方法论**\n- TOST equivalence test（±2pp margin）的 SESOI 论证是否充分？sensitivity analysis（Table 13, min ±1.52pp）是否说服力足够？\n- Holm-Bonferroni correction（k=4）的选择和实施是否正确？\n- Clustered bootstrap（114 clusters, 10K resamples）是否适合这个数据结构？ICC=0.191 的 design effect 处理是否得当？\n- MDE 分析（~25pp at n=48）的方法论是否恰当？\n\n**2. 实验 confound 控制**\n- Repo-level 比较多为 single-seed：19-26pp 的 gap 是否足以排除 seed noise？\n- CWM baseline 用 ≤8B LoRA vs 原始 32B CWM with mid-training：这个比较的公平性如何？论文 conditioning 是否足够明确？\n- Checkpoint selection 不一致（val-selected vs final epoch due to NaN val loss）：是否系统性偏向某个 formulation？\n- TRAJ 训练数据量差异（~400 vs ~70K）：downsample ablation 是否充分控制了这个 confound？\n- 评估 sequence length 跨模型不一致（Qwen3: 8192, DeepSeek: 4096）\n\n**3. Claim-Evidence 对齐**\n- 每个 contribution 是否有充分的统计证据支撑？\n- \"Error complementarity\" claim（oracle 90.63%）是单 seed 估计——这个 claim 的强度与证据是否匹配？\n- Re-repair pilot（n=44, p=0.42）的 negative result 如何影响论文的 practical value narrative？\n- \"Formulation × model × complexity interaction\" 是否被实验设计充分支撑？\n\n**4. 数据与评估**\n- 合成突变（mutation operators）vs 真实 bug 的 validity threat\n- Val-test mutation type distribution mismatch（operator_swap: 19.1%→34.3%）\n- Variant-level n=48 的统计效力是否足以支撑 repo-level claims？\n\n请输出完整审稿意见，包含：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，按 severity 排序: Must-Fix / Should-Fix / Minor), Questions, Missing References, 以及 Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **EMNLP 2026**，ARR May cycle，截止 2026-05-25\n- Long Paper: 8 页正文（References/Limitations/Ethics 不计入）\n- ACL style template with `[review]` option\n- Double-blind，无匿名期\n- 评分标准（ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（编译 PDF: `main.pdf`）\n\n### 论文概述\n比较三种 execution-free code verification formulation（CLS per-test classification, CWM output generation, TRAJ trajectory-level scoring），在两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别（function-level, repo-level）、多种 seed 下进行系统实验。核心发现：function-level 三者等价（TOST p=0.007），repo-level CLS 领先 CWM 19-26pp。\n\n### 你的审查侧重\n\n**1. 统计方法论**\n- TOST equivalence test（±2pp margin）的 SESOI 论证是否充分？sensitivity analysis（Table 13, min ±1.52pp）是否说服力足够？\n- Holm-Bonferroni correction（k=4）的选择和实施是否正确？\n- Clustered bootstrap（114 clusters, 10K resamples）是否适合这个数据结构？ICC=0.191 的 design effect 处理是否得当？\n- MDE 分析（~25pp at n=48）的方法论是否恰当？\n\n**2. 实验 confound 控制**\n- Repo-level 比较多为 single-seed：19-26pp 的 gap 是否足以排除 seed noise？\n- CWM baseline 用 ≤8B LoRA vs 原始 32B CWM with mid-training：这个比较的公平性如何？论文 conditioning 是否足够明确？\n- Checkpoint selection 不一致（val-selected vs final epoch due to NaN val loss）：是否系统性偏向某个 formulation？\n- TRAJ 训练数据量差异（~400 vs ~70K）：downsample ablation 是否充分控制了这个 confound？\n- 评估 sequence length 跨模型不一致（Qwen3: 8192, DeepSeek: 4096）\n\n**3. Claim-Evidence 对齐**\n- 每个 contribution 是否有充分的统计证据支撑？\n- \"Error complementarity\" claim（oracle 90.63%）是单 seed 估计——这个 claim 的强度与证据是否匹配？\n- Re-repair pilot（n=44, p=0.42）的 negative result 如何影响论文的 practical value narrative？\n- \"Formulation × model × complexity interaction\" 是否被实验设计充分支撑？\n\n**4. 数据与评估**\n- 合成突变（mutation operators）vs 真实 bug 的 validity threat\n- Val-test mutation type distribution mismatch（operator_swap: 19.1%→34.3%）\n- Variant-level n=48 的统计效力是否足以支撑 repo-level claims？\n\n请输出完整审稿意见，包含：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，按 severity 排序: Must-Fix / Should-Fix / Minor), Questions, Missing References, 以及 Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-19T11:01:03.048317+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23217
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-19T11:01:03.350140+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 写作完整性 + 格式合规）\n\n### Venue 信息\n- **EMNLP 2026**，ARR May cycle，截止 2026-05-25\n- Long Paper: 8 页正文（References/Limitations/Ethics 不计入）\n- ACL style template with `[review]` option\n- Double-blind，无匿名期\n- 评分标准（ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（编译 PDF: `main.pdf`）\n\n### 论文概述\n比较三种 execution-free code verification formulation（CLS per-test classification, CWM output generation, TRAJ trajectory-level scoring），在两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别（function-level, repo-level）、多种 seed 下进行系统实验。核心发现：function-level 三者等价（TOST p=0.007），repo-level CLS 领先 CWM 19-26pp。\n\n### 你的审查侧重\n\n**1. 新颖性评估**\n- \"Classification > generation when outputs are complex\" 是否一个可预测的结论？论文的 novelty 到底在哪里？\n- 论文声称是 \"the first systematic comparison\"——这个 gap 是否真实存在？是否有遗漏的先前工作做了类似比较？\n- 方法论贡献（matched experimental framework）vs 经验发现——哪个更有价值？对 EMNLP venue 来说是否足够？\n- Error complementarity / failure mode taxonomy 的 novelty 和 insight depth\n\n**2. 写作质量**\n- Abstract：是否在 30 秒内传达了核心价值？是否有数据堆砌？字数是否合适（ARR 推荐 150-250 words）？\n- Introduction：5 段叙事结构是否完整？贡献列表是否清晰、简洁、每条有 section 支撑？\n- Related Work：是否做到了归纳和定位而非论文堆砌？引用覆盖是否充分（直接相关方法、baseline、benchmark、理论基础）？\n- 全文主线统一性：Abstract → Intro → Method → Results → Conclusion 是否一条连贯主线？\n- **AI 写作痕迹检查**（硬规则）：\n  - em-dash（—）和解释性 en-dash（ – ）：必须全部清零\n  - -ing 短语结尾（\", highlighting...\"、\", demonstrating...\"）\n  - 过度分段（每 2-3 句就换段）\n  - \"Furthermore\" / \"Moreover\" / \"Additionally\" 连续使用\n  - 用词黑名单：delve into / leverage / utilize / facilitate / a myriad of / a plethora of\n\n**3. 格式合规**\n- 页数限制：正文是否 ≤8 页？\n- 模板：`\\usepackage[review]{acl}` 是否正确？\n- 匿名化：正文/附录中是否有 de-anonymization 风险？\n- Responsible NLP Checklist：每项是否认真填写（非全写 N/A）？\n- Limitations section：是否存在且充分？\n- 图表格式：caption 自包含？小数精度一致？最优加粗？字体大小可读？\n- 引用格式：是否使用 natbib？格式一致？\n\n**4. Venue Fit（EMNLP 2026）**\n- 这是一篇 SE/NLP 交叉的实证论文——EMNLP 的审稿人是否认为这属于 EMNLP scope？\n- 论文是否连接了足够的 NLP 理论框架（如 process vs outcome supervision）使其对 NLP audience 有价值？\n- 与 SE venue（ICSE/FSE/ASE）相比，投 EMNLP 的优势在哪里？\n\n请输出完整审稿意见，包含：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，按 severity 排序: Must-Fix / Should-Fix / Minor), Questions, Missing References, 以及 Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 写作完整性 + 格式合规）\n\n### Venue 信息\n- **EMNLP 2026**，ARR May cycle，截止 2026-05-25\n- Long Paper: 8 页正文（References/Limitations/Ethics 不计入）\n- ACL style template with `[review]` option\n- Double-blind，无匿名期\n- 评分标准（ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（编译 PDF: `main.pdf`）\n\n### 论文概述\n比较三种 execution-free code verification formulation（CLS per-test classification, CWM output generation, TRAJ trajectory-level scoring），在两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别（function-level, repo-level）、多种 seed 下进行系统实验。核心发现：function-level 三者等价（TOST p=0.007），repo-level CLS 领先 CWM 19-26pp。\n\n### 你的审查侧重\n\n**1. 新颖性评估**\n- \"Classification > generation when outputs are complex\" 是否一个可预测的结论？论文的 novelty 到底在哪里？\n- 论文声称是 \"the first systematic comparison\"——这个 gap 是否真实存在？是否有遗漏的先前工作做了类似比较？\n- 方法论贡献（matched experimental framework）vs 经验发现——哪个更有价值？对 EMNLP venue 来说是否足够？\n- Error complementarity / failure mode taxonomy 的 novelty 和 insight depth\n\n**2. 写作质量**\n- Abstract：是否在 30 秒内传达了核心价值？是否有数据堆砌？字数是否合适（ARR 推荐 150-250 words）？\n- Introduction：5 段叙事结构是否完整？贡献列表是否清晰、简洁、每条有 section 支撑？\n- Related Work：是否做到了归纳和定位而非论文堆砌？引用覆盖是否充分（直接相关方法、baseline、benchmark、理论基础）？\n- 全文主线统一性：Abstract → Intro → Method → Results → Conclusion 是否一条连贯主线？\n- **AI 写作痕迹检查**（硬规则）：\n  - em-dash（—）和解释性 en-dash（ – ）：必须全部清零\n  - -ing 短语结尾（\", highlighting...\"、\", demonstrating...\"）\n  - 过度分段（每 2-3 句就换段）\n  - \"Furthermore\" / \"Moreover\" / \"Additionally\" 连续使用\n  - 用词黑名单：delve into / leverage / utilize / facilitate / a myriad of / a plethora of\n\n**3. 格式合规**\n- 页数限制：正文是否 ≤8 页？\n- 模板：`\\usepackage[review]{acl}` 是否正确？\n- 匿名化：正文/附录中是否有 de-anonymization 风险？\n- Responsible NLP Checklist：每项是否认真填写（非全写 N/A）？\n- Limitations section：是否存在且充分？\n- 图表格式：caption 自包含？小数精度一致？最优加粗？字体大小可读？\n- 引用格式：是否使用 natbib？格式一致？\n\n**4. Venue Fit（EMNLP 2026）**\n- 这是一篇 SE/NLP 交叉的实证论文——EMNLP 的审稿人是否认为这属于 EMNLP scope？\n- 论文是否连接了足够的 NLP 理论框架（如 process vs outcome supervision）使其对 NLP audience 有价值？\n- 与 SE venue（ICSE/FSE/ASE）相比，投 EMNLP 的优势在哪里？\n\n请输出完整审稿意见，包含：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，按 severity 排序: Must-Fix / Should-Fix / Minor), Questions, Missing References, 以及 Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 516 · 2026-05-19T11:01:04.912998+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1562
}
```

</details>

---


### Assistant

_source line 517 · 2026-05-19T11:01:12.942375+00:00_

Round 1 审稿任务已分派给两名 Reviewer。等待独立初审结果返回。

- **Reviewer 1**：方法严谨性 + 实验设计（统计方法、confound 控制、claim-evidence）
- **Reviewer 2**：新颖性 + 写作完整性 + 格式合规（novelty、AI 痕迹、venue fit）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 518 · 2026-05-19T11:08:30.999181+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

### Summary

本文系统比较了三种 execution-free code verification formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹评分），在两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度层级（function-level、repo-level）、多 seed 条件下进行匹配实验。核心发现：function-level 三者等价（TOST p=0.007），repo-level CLS 领先 CWM 19-26pp。论文还提供了 failure mode taxonomy 和 error complementarity 分析。

---

## 总体评分

**Overall**: 3.0 / 5（Findings）
**Confidence**: 4 / 5
**一句话总结**: 实验框架设计严谨、统计方法规范，但核心发现的 novelty 有限——"classification 在复杂输出场景优于 generation"是一个可预期的结论，且 repo-level 结果依赖 single-seed，削弱了论文最有价值的 claim。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 匹配实验框架、TOST 等价检验、ICC、bootstrap CI 等统计方法使用规范。但 repo-level 仅 single-seed（Extended Limitations, p18 承认），合成数据未验证真实 bug 迁移性。 |
| Excitement | 2.5/5 | 填补了一个真实但狭窄的文献空白。核心发现（CLS>CWM at repo-level）可预期；function-level 等价结论更有趣但叙事占比不足。failure mode taxonomy 有一定 insight 但深度有限。 |
| Reproducibility | 4/5 | 训练超参（Appendix E, Table 11）、数据统计（Section 3.1）、统计检验细节均有报告。但未提及代码/数据开源计划（checklist C4 回答 "Partially"）。 |
| Overall Assessment | 3.0/5 | 方法论贡献（matched framework）扎实，经验发现有实用价值，但 novelty 不足以支撑主会议。适合 Findings。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Novelty 有限：核心发现可预期**
- 具体位置：Abstract, Section 1 (Contributions), Section 3.2-3.5
- 问题：论文的核心 claim 是 "classification > generation when outputs are complex"（repo-level CLS 领先 CWM 19-26pp）。但这一结论在概念上是可预期的：CWM 需要精确生成长序列输出（repo-level 平均 ~477 tokens, Section 3.5 p6），错误会乘法累积（format collapse + truncation + surface form errors, Table 4）；而 CLS 只需输出 1 token。CodeScaler (Zhu et al., 2026) 已经将 reward model 区分为 "sequence classifiers" 和 "generative models" 两类，这说明 community 已经意识到了这一概念区分。论文声称是 "the first systematic comparison"（Section 1, p1），这个 gap 是真实的，但填补这个 gap 所获得的 insight 深度有限——主要是确认了一个直觉上合理的预期。function-level 的等价结论（TOST p=0.007）实际上更有趣且更出乎意料，但在叙事中没有得到足够突出。
- 为什么影响接收：EMNLP 主会议期望 "noteworthy contribution"（Excitement ≥ 4），而本文的 novelty 主要在于 methodology（matched framework）而非 insight。
- 建议修改方向：(1) 重新平衡叙事，将 function-level 等价的 surprising finding 作为核心故事而非 repo-level 的 predictable divergence；(2) 深化 failure mode taxonomy 的分析——目前 Table 4 的分类较为表面，可以加入 per-mutation-type 或 per-error-category 的定量分析来增强 insight depth；(3) 更明确地论证 "为什么 matched comparison 本身是一个方法论贡献"——目前论文倾向于把它当作理所当然。

**N2** [critical] **Repo-level 核心结果依赖 single-seed**
- 具体位置：Extended Limitations (p18), Section 3.3 (Table 2-3)
- 问题：论文最核心的发现——repo-level CLS 领先 CWM 19-26pp——基于 single-seed 实验（p18 明确承认 "All repo-level results use val-selected checkpoints"，CWM 8B comparison 也是 single-seed）。论文在 function-level 使用了 3-5 seeds 并配合 TOST 检验，展示了良好的统计方法论意识，但在最重要的 repo-level claim 上却没有贯彻同样的标准。Table 3 没有 ±std 或 CI，也没有 TOST 检验。这构成了论文内部的方法论不一致。
- 为什么影响接收：论文的叙事重心在于 "complexity-dependent divergence"，但支撑这一 claim 的 repo-level 数据统计效力不足。审稿人无法判断 19-26pp gap 的哪部分是系统性差异、哪部分是 seed variance。
- 建议修改方向：至少补充 2-3 个 seed 的 repo-level 实验并报告 CI，或者将 repo-level 结论明确降级为 "preliminary observation"，在叙事中给予相应的 hedging。

**N3** [critical] **合成数据的外部效度未验证**
- 具体位置：Section 3.1, Conclusion (p8), Extended Limitations (p18)
- 问题：所有训练数据均基于 mutation-based 合成 bug（Section 3.1: "five mutation types"）。论文在 Conclusion 引用了 Andrews et al. (2005) 和 Just et al. (2014) 来支持 mutation adequacy，但这些经典工作讨论的是 mutation testing 在测试评估中的有效性，并非 mutation-based training data 对 LLM verification 任务的迁移性。Extended Limitations (p18) 承认 "the synthetic-to-real transfer gap remains untested"。对于一篇声称要指导 "formulation selection" 的实用导向论文来说，完全缺乏真实 bug 数据的验证（哪怕是 held-out evaluation）是一个重要缺陷。
- 为什么影响接收：如果 formulation 之间的相对优劣在真实 bug 上发生逆转，论文的 practical recommendations 就失效了。
- 建议修改方向：在 SWE-bench Verified 的 gold patches 上做一个 zero-shot 或 few-shot evaluation，验证 formulation ranking 是否保持一致。即使不做 fine-tuning，也可以用预训练模型的 prompting 来获得初步证据。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Abstract 字数不足**
- 具体位置：abstract.tex
- 问题：Abstract 约 120-130 词，低于 ARR 推荐的 150-250 词范围。当前 abstract 缺少对 "为什么这个问题重要" 的充分论述（仅一句 "No prior work compares these formulations under matched conditions"），也缺少对 failure mode taxonomy / error complementarity 这些次要贡献的提及。
- 建议：扩展到 ~180 词，补充 (1) 问题重要性（execution-free verification 在 test-time scaling 中的角色），(2) failure mode taxonomy 的核心发现。

**W2** [warning] **模型规模受限，泛化性存疑**
- 具体位置：Section 3.1, Table 11 (Appendix E)
- 问题：所有实验使用 ≤8B 模型 + LoRA/QLoRA fine-tuning。Limitations (p8) 提到 "Generation-based verification at repo level requires larger models or execution-trace pretraining (§3.7)"，但论文没有验证这一假设。CWM 在 repo-level 的劣势可能是模型容量不足导致的 artifact，而非 formulation 本身的固有限制。如果使用 32B+ 模型或 full fine-tuning，CWM 可能缩小甚至消除与 CLS 的差距。
- 建议：至少讨论一下 CWM 原始论文 (Meta FAIR, 32B, full fine-tuning) 的 repo-level 表现，与本文 ≤8B LoRA 结果做 qualitative comparison。

**W3** [warning] **遗漏相关工作**
- 具体位置：Section 4 (Related Work)
- 问题：以下近期工作与本文直接相关但未被讨论：
  - **Aletheia** (Venkatkrishna et al., 2026, arXiv:2601.12186): 系统研究 code verifier 的 RLVR 训练配方，提供了 execution-grounded evaluation testbed，发现最优训练策略是 scale-dependent——与本文的 "complexity-dependent formulation choice" 形成直接对话。
  - **VeRPO** (2026, arXiv:2601.03525): Verifiable Dense Reward Policy Optimization，提出了将 execution outcome 锚定到 dense reward 的方法，与本文的 process vs outcome supervision 框架直接相关。
  - **ExecVerify** (2026, arXiv:2603.11226): White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning，讨论了 step-level verification 的训练方法。
- 建议：在 Related Work 中加入这些工作的讨论，特别是 Aletheia 的 scale-dependent finding。

**W4** [warning] **表格缺少次优下划线标记**
- 具体位置：Table 1, 2, 3
- 问题：Best results 用粗体标记（符合规范），但 second-best 未使用下划线标记。这是 NLP/ML 顶会论文的常见格式惯例，有助于读者快速识别方法间的排名。
- 建议：为 second-best 结果添加下划线。

**W5** [warning] **Venue fit 存在张力**
- 具体位置：全文
- 问题：论文位于 SE 和 NLP 的交叉地带。虽然论文使用了 NLP 理论框架（process vs outcome supervision, Section 4 第二段），但所有 benchmark 完全是代码相关的（HumanEval, MBPP, SWE-bench），核心贡献是关于 code verification formulation 的实证发现。EMNLP 审稿人可能会质疑这些 findings 是否对更广泛的 NLP community 有价值——例如，formulation choice 的 complexity-dependence 是否 generalize 到非代码领域（如 math reasoning verification）？论文没有讨论这一点。
- 建议：在 Discussion/Conclusion 中明确论述这些发现对 broader NLP verification 的 implications（例如，CLS vs generation tradeoff 在 math PRM 中是否也存在？）。

---

## 小问题（不影响接收）

- **M1**: experiments.tex line 98 存在一个 "-ing phrase"（", providing approximately 30% headroom"），虽然不严重但建议改写为独立句。
- **M2**: Figure 2（gap amplification bar chart）信息密度偏低——可以考虑合并更多信息（如加入 confidence intervals 或 per-model breakdown）。
- **M3**: Checklist C4 回答 "Partially" 关于 version numbers——camera-ready 前应补全。
- **M4**: 引用验证显示 8 条 bib entry 未被 OpenAlex 索引（liu2024codemind, xu2025patchreasoner, li2025sstar 等），均为较新的 preprint，不影响引用真实性，但建议检查是否有更新的正式发表版本。

---

## 主要优势

1. **实验设计严谨**：matched experimental framework 消除了模型、数据、训练配置等混淆变量，这在 formulation comparison 中是非常必要的，也是本文相对于 prior work 的真实增量。
2. **统计方法规范**：TOST 等价检验（而非仅用 p-value 证明差异不显著）、bootstrap CI、ICC 的使用体现了良好的统计素养，在 NLP 实证论文中较为少见。
3. **Failure mode taxonomy 有实用价值**：Table 4 和 Section H 的 error analysis 虽然深度有限，但 format collapse / truncation / surface form errors 的分类对 practitioners 选择 formulation 有直接指导意义。
4. **写作质量良好**：全文主线清晰（formulation choice is complexity-dependent），无 AI 写作痕迹（无 em-dash、无黑名单词汇、段落长度自然），Introduction 的 5 段结构完整。
5. **格式基本合规**：`\usepackage[review]{acl}` 正确、匿名化完整、Limitations section 存在且较充分、Responsible NLP Checklist 逐项填写。

---

## Missing References

- Aletheia (Venkatkrishna et al., 2026, arXiv:2601.12186)
- VeRPO (arXiv:2601.03525, 2026)
- ExecVerify (arXiv:2603.11226, 2026)
- Pareto Optimal Code Generation (arXiv:2506.10056) — 讨论了 ORM accuracy vs throughput 的 Pareto frontier，与本文 formulation tradeoff 相关

---

## Questions for Authors

1. Repo-level 结果（Table 3）是否有额外 seed 的数据？如果有，19-26pp gap 的 variance 是多少？
2. CWM 原始论文 (Meta FAIR) 使用 32B full fine-tuning 在 repo-level 上的表现如何？是否有证据支持 CWM 的 repo-level 劣势是 capacity-limited 而非 formulation-inherent？
3. 论文声称 error complementarity motivates "complexity-aware routing"（Abstract 最后一句）。是否有 preliminary 实验验证了这种 routing 策略的实际收益？
4. Function-level TOST 等价使用了 ±2pp margin——这个阈值是如何选取的？是否做了 sensitivity analysis？（注：Section 3.4 和 Appendix A 有 TOST sensitivity 讨论，但 margin 选择的 justification 不够 explicit。）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 519 · 2026-05-19T11:08:46.034110+00:00_

Reviewer 2 初审意见已收到（Overall: 3.0 Findings）。等待 Reviewer 1 提交后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 520 · 2026-05-19T11:08:48.659629+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论：Overall 3.0/5（Findings），Confidence 4/5。**

核心判断：
- 实验框架设计和统计方法是论文的真正亮点（TOST 等价检验、matched comparison）
- 但 novelty 有限——"classification > generation for complex outputs" 可预期，且最关键的 repo-level 结论基于 single-seed
- 三个 Must-Fix：(1) novelty 不足需重新平衡叙事，(2) repo-level 需补充多 seed，(3) 合成数据需验证真实 bug 迁移性
- 五个 Should-Fix：Abstract 字数不足、模型规模受限、遗漏相关工作（Aletheia 等）、表格格式、venue fit 张力

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 521 · 2026-05-19T11:08:55.501070+00:00_

已记录。继续等待 Reviewer 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 44

## Round 44

6 recorded events


### User

_source line 522 · 2026-05-19T11:13:19.457566+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 完整审稿意见

**论文**: The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 统计方法论 + 实验 confound 控制 + Claim-Evidence 对齐 + 数据与评估

---

## 总体评分

**Overall**: 3.0 (Findings)
**Confidence**: 4/5
**一句话总结**: Function-level 等价性结论有充分多 seed 支撑，统计框架值得肯定；但 repo-level 核心 claims 受 single-seed 设计、checkpoint 选择系统性偏差、within-formulation 高方差严重制约，需要补充实验或大幅降调 claims。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 统计框架整体合理（TOST、clustered bootstrap、ICC），但 repo-level claims 缺乏多 seed 支撑，CWM checkpoint 选择系统性不 matched |
| Excitement | 2.5/5 | 填补 formulation 系统比较的空白，但 function-level 等价性直觉上不意外，repo-level 结论受限于实验条件 |
| Reproducibility | 3.5/5 | 超参数文档化充分，统计方法透明，但无代码/数据释出，关键 repo-level 实验为 single-seed |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Repo-level claims 的 single-seed 基础与 within-formulation 高方差矛盾

- 具体位置：§3.5, Table 3, Table 10, Appendix I
- 问题：论文核心 repo-level claim（CLS-CWM gap 19–26pp）几乎全部基于 seed 42 的单次实验。然而 Table 10 揭示了 within-formulation 的巨大 seed 方差：DeepSeek CLS per-test accuracy 从 82.51%（s42, drop preprocessing）到 63.51%（s123），波动达 **19pp**；variant-level 从 81.25% 到 39.17%，波动 **42pp**。Qwen3-4B CLS variant-level 也从 64.58%（s42）到 81.25%（s123），波动 **17pp**。Within-formulation seed 方差（~19pp per-test）与 between-formulation gap（19–26pp）量级相当。
- 论文 §3.7 声称 "the observed 19–26 pp gap exceeds any individual confound by an order of magnitude"，但 Table 10 中 within-CLS seed variance 数据直接反驳此 claim——confound 与 effect 处于同一量级，而非差一个数量级。
- 为什么影响接收：无法排除 repo-level CLS-CWM gap 主要反映 seed/checkpoint/preprocessing 的偶然选择而非 formulation 内在差异。这是一篇以 matched comparison 为核心贡献的论文，但其最重要的比较使用了 unmatched seeds。
- 建议修改方向：(1) 补充至少 3 seeds 的 repo-level 实验，报告 seed-level 方差和 paired comparison；(2) 如果资源不允许，将所有 repo-level conclusions 明确标注为 "preliminary/suggestive under single-seed design"，并修正 §3.7 中 "order of magnitude" 的表述。

**N2** [critical] Checkpoint 选择策略系统性偏向 CLS，全部 CWM 运行受影响

- 具体位置：§3.1 ("runs using training perplexity/loss produce NaN validation loss...defaults to the final epoch checkpoint (affects DeepSeek ×123 and all CWM runs)")
- 问题：论文承认所有 CWM 运行因 NaN val loss 而被迫使用 final-epoch checkpoint，而 CLS 运行（部分）使用 val-selected checkpoint。在 3 epoch 训练中，val-best checkpoint 可能出现在任意 epoch；final-epoch ≠ best-epoch。这引入系统性 confound：CLS 有 checkpoint selection 优势而 CWM 没有。论文估计 checkpoint 效应 ~2pp（§3.7），但这是基于 CLS 数据的估计。Generation 任务的 overfitting dynamics 与 classification 不同（generation 更容易在后期 overfit 到训练数据的 surface form），CWM 的 checkpoint 效应可能更大。
- 更严重的是：这不是个别 run 的问题，而是影响 **全部 CWM 运行** 的系统性偏差。对于一篇强调 "matched conditions" 的论文，checkpoint selection 不 matched 是核心方法论缺陷。
- 为什么影响接收：直接影响论文最重要的比较（CLS vs CWM），且 confound 方向与 observed effect 方向一致（CWM 被系统性低估）。
- 建议修改方向：(1) 修复 CWM val loss 计算使所有 formulations 使用相同的 checkpoint selection；(2) 如不可修复，提供 CLS final-epoch vs val-selected 的消融以量化 CLS 端的 checkpoint selection benefit；(3) 将此从脚注级 caveat 升级为 §3.7 中的 prominent confound 讨论。

**N3** [critical] SESOI (±2pp) 的 domain justification 循环论证

- 具体位置：§3.4
- 问题：TOST 的结论完全取决于 SESOI 的选择。论文的 justification 是 "±2 pp corresponds to ~15 additional errors per 500 predictions, the smallest difference we consider practically meaningful"。这是循环论证——将 ±2pp 转换为绝对错误数并不构成 domain-grounded justification，只是 restated 了 ±2pp 的含义。在 code verification 的实际部署中，verifier accuracy 的边际价值取决于下游 pipeline（如 best-of-n selection 的 success rate 对 verifier accuracy 的敏感度）。
- 另外，"approximately 307% headroom" 的表述有误导性。如果 TOST 在 ±1.52pp 处仍然 reject，"headroom" 在等价性检验中通常指 margin 可以收紧多少（(2.0−1.52)/2.0 = 24%），而非 margin/observed_gap 的比值（1.52/0.45 ≈ 338%）。后者衡量的是 observed gap 相对于 tightest margin 的冗余度，不是 SESOI 的 robustness。
- 为什么影响接收：SESOI 选择是 equivalence testing 的核心假设。Lakens (2017)（论文自己引用的方法学参考）明确要求 SESOI 基于 domain knowledge 或 existing literature，而非研究者主观判断。
- 建议修改方向：(1) 从下游应用（如 best-of-n pipeline）角度给出 ±2pp 的 functional justification；(2) 报告 SESOI sensitivity 曲线（不同 margin 下的 TOST p-value，Table 13 已有但应在正文中更 prominent）；(3) 修正 "307% headroom" 为更准确的表述。

**N4** [critical] Oracle ensemble accuracy 数值自相矛盾

- 具体位置：§3.6 vs Appendix H(a) vs §5 Conclusion
- 问题：§3.6 报告 "an oracle combination achieves 90.6%"；Conclusion 报告 "oracle ensemble: 90.63%"。但 Appendix H(a) 报告 "An oracle combination achieves **96.03%** accuracy, **+3.12pp** over the best single formulation (87.51%)"。数学验证：87.51 + 3.12 = 90.63 ≠ 96.03。正文和结论的 90.63% 与 +3.12pp 吻合，但附录中的 96.03% 与两者矛盾。
- Error complementarity 是论文三个核心 contributions 之一（§1 第三条 contribution），核心数字不一致直接损害可信度。
- 为什么影响接收：Reviewer 和 AC 会立即注意到正文与附录的数字矛盾，质疑整体数据可靠性。
- 建议修改方向：核实并统一所有 oracle accuracy 数字，确保正文、附录、结论一致。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] TRAJ 训练配置差异过大，downsample ablation 不充分控制 confound

- 具体位置：§3.1, Appendix B, Appendix I
- 问题：TRAJ 使用 ~400 个 repo-level 实例（variant-level labels），CLS/CWM 使用 ~70K 个 per-test 实例，相差 175×。Learning rate 也不同（2×10⁻⁴ vs 5×10⁻⁵）。Downsample ablation（Appendix B）将 CLS 数据减少到 match TRAJ 的 **volume**，但未 match **granularity**：downsampled CLS 仍使用 per-test 级别的学习信号（每个 test 一个 label），而 TRAJ 只有 variant-level 信号（整个 patch 一个 label）。Per-test labels 的信息量远大于 variant-level labels（n×binary vs 1×binary），所以 volume-matched 不等于 information-matched。
- 建议：(1) 明确讨论 volume vs granularity 的区别；(2) 如果可行，在 variant-level aggregated labels 上训练 CLS 作为 ablation。

**W2** [warning] "Formulation × model × complexity interaction" 未做形式化统计检验

- 具体位置：§1, §3.5, §5
- 问题：论文在 Introduction 就 claim 了三阶交互（"the results reveal a three-layer structure"），在 §3.5 和 Conclusion 中反复使用 "formulation × model × complexity interaction" 表述。但这个交互从未通过 factorial ANOVA、mixed-effects model 或任何形式化统计方法检验。所有证据是描述性的（function-level 等价 + repo-level 分化）。在 single-seed repo-level 数据下，三阶交互的统计检验甚至不可行。
- 建议：将 "interaction" 降级为 "observed pattern"，或在至少有多 seed 数据的条件下做 two-way interaction 检验。

**W3** [warning] CWM 结论的 regime qualifier 在 Abstract/Conclusion 中不充分

- 具体位置：Abstract, §5 Conclusion
- 问题：§3.1 明确声明 CWM baseline 是 "LoRA fine-tuned variant for matched comparison, not a reproduction of the 2.8B Code World Model"，Limitations 也提到 "at larger scale, the generation bottleneck may diminish"。但 Abstract 写 "generation-based simulation falling below majority baseline"——无任何 regime qualifier。Conclusion 有 "under <8B LoRA fine-tuning" 的限定，但随后的 practical recommendations 中 "CWM falls below majority baseline (19–26 pp gap)" 再次缺乏限定。读者（尤其是只看 Abstract 的）可能得出 generation formulation 本身有问题的一般性结论，而实际上可能是 model scale/pretraining 的问题。
- 建议：Abstract 中加 "under ≤8B LoRA fine-tuning" 限定；practical recommendations 中每处 CWM 劣势 claim 都加 regime qualifier。

**W4** [warning] Re-repair negative result 与 diagnostic value narrative 的张力未充分讨论

- 具体位置：§3.6, Appendix H(j)
- 问题：论文反复强调 CLS 的 "diagnostic granularity" 作为核心卖点（§1 第四条 contribution, §5 practical recommendations）。但唯一测试 diagnostic value 是否 translates to downstream benefit 的实验（re-repair pilot, Appendix H(j)）得到了 **negative result**（Δ_A = −32.5%, p = 0.42, effect size δ = 0）。论文以 "insufficient sample size (power ~0.3)" dismiss 这个结果，但 effect size δ = 0 表明这不是 underpowered type II error——效应本身就是零。这与 diagnostic value narrative 形成实质性张力。
- 另外，主文 §3.6 提到的样本量（需核实是 n=14 还是 n=44）与 Appendix H(j) 中的 n=44 可能存在不一致。
- 建议：(1) 在讨论 diagnostic value 时更平衡地呈现 negative result；(2) 考虑将 "diagnostic granularity" 从 core contribution 降级为 "potential advantage, pending downstream validation"。

**W5** [warning] Synthetic mutation validity gap 未有实证评估

- 具体位置：§3.1, §5 Limitations, Table 12
- 问题：训练和测试数据全部基于 synthetic mutation operators。Andrews 2005 和 Just 2014 的引用仅提供间接支持——这些经典研究在传统 mutation testing 语境下，不能直接推广到 LLM 训练数据的 distribution matching。Val-test mutation type distribution 的显著偏移（operator_swap: 19.1%→34.3%, +15.2pp shift）进一步暴露 synthetic data 分布的脆弱性。
- 建议：(1) 在 SWE-bench Verified 的真实 bug（非 mutation）上评估至少一种 formulation 的性能作为 transfer sanity check；(2) 更详细讨论 mutation distribution shift 对结论泛化性的影响。

---

## 小问题（不影响接收）

- Table 2 中 TRAJ Δ 4B→8B 为 "+0.09"（function-level），但正文 §3.3 写 "TRAJ also shows no scaling benefit (72.92% at both 4B and 8B)" 指的是 repo-level。两个 level 的数据在同一段落中交叉引用，容易造成混淆。
- Table 3 格式不清晰（CLS 出现两次，部分 cell 为空），建议重新组织为更直观的 layout。
- §2.3 中 κ = r/(1 + (1−r)/n) 的 n 未明确定义（是 test count 还是 sample size？），与后续 ICC ρ 的关系也不清楚。
- Appendix 编号不连续（A-I 存在，但 §3.6 引用 "Appendix M" 和 "Appendix N"，未在转录范围内确认）。
- 引用验证：60 条 bib entries 全部被引用（无 orphan），8 条 OpenAlex 未查到（liu2024codemind, xu2025patchreasoner, li2025sstar, lightman2023letsverify 等为已知论文但未被 API 索引），4 条 first_author 格式微小差异——整体引用可靠。

---

## Questions

1. Table 10 中 DeepSeek s42 与 s123 的 per-test accuracy 差距达 19pp（82.51% vs 63.51%）。论文 §3.5 说 "preprocessing and checkpoint selection differences...confirms impact directly explains <3% of this gap"——但这个 <3% 是关于 CLS-CWM gap 的，不是关于 within-CLS seed variance 的。对于 DeepSeek CLS 内部 19pp 的 seed variance，preprocessing vs checkpoint vs random seed 各贡献多少？

2. TOST 将 5 个 seed（3 bf16 + 2 NF4）pooled 在一起。Appendix I 提到 "Restricting to three bfloat16 seeds yields a comparable mean gap with wider confidence interval"——具体的 bf16-only TOST p-value 是多少？如果 p > 0.05，equivalence claim 需要重新 qualify。

3. Repo-level ICC = 0.3146 对应 DEFF = 114.4（Appendix A），意味着 effective sample size 极小。Repo-level per-test 比较（n=9,784）的 effective n ≈ 9784/114.4 ≈ 86。在这么小的 effective n 下，repo-level 的 CLS-CWM 差异的 clustered bootstrap 95% CI 是多少？论文似乎没有报告 repo-level 比较的 CI。

4. CWM unparseable outputs 默认为 majority class (PASS)。如果默认为 FAIL 或 random 50/50，CWM accuracy 如何变化？这个设计决策对 CLS-CWM gap 的影响是放大还是缩小？

---

## Missing References

- 原始 CWM 论文（FAIR CodeGen team et al., 2025）在 32B scale 的 benchmark 结果应在 Related Work 中更详细对比讨论，帮助读者理解 ≤8B LoRA regime 的局限性上下文。当前 Related Work 仅在一般性段落中提及 CWM，未对比其 32B 结果与本文 ≤8B 结果的差异。
- 建议补充近期 execution-free reward model 的工作（如有遗漏的同期工作），确保 Related Work 覆盖完整。

---

## 主要优势

1. **填补实证空白**：首个在 matched conditions 下系统比较三种 execution-free verification formulations 的工作，研究问题的定义清晰且有实际价值。
2. **统计框架超越 NLP 常见标准**：TOST equivalence testing + clustered bootstrap + ICC + Holm-Bonferroni 的组合在 NLP 论文中罕见，显示了方法论意识。即使 SESOI justification 需加强，框架本身值得肯定。
3. **Function-level 等价性结论可信**：5 seeds × 2 model families 的充分支撑，TOST 在 ±1.52pp 仍 reject，这个结论是 robust 的。
4. **极高的透明度**：~10 页附录包含 rank ablation、majority voting、sequence-length ablation、few-shot baseline、per-mutation breakdown、error analysis 等，几乎所有可预见的 reviewer 问题都有对应的消融实验。Limitations 的讨论在 NLP 论文中属于异常详尽。
5. **Failure mode taxonomy 有实际价值**：§2.2 和 Table 4 的 failure mode 分析（format collapse、aggregation penalty、token exhaustion）为 practitioners 提供了可操作的 diagnostic framework。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 523 · 2026-05-19T11:14:01.387884+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 评分: Overall 3.0 (Findings), Confidence 4/5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] **Novelty 有限：核心发现可预期**\n- \"classification > generation when outputs are complex\" 在概念上可预期。CodeScaler (Zhu et al., 2026) 已区分 \"sequence classifiers\" vs \"generative models\"。论文声称 \"the first systematic comparison\" 这个 gap 真实但 insight 深度有限。function-level 等价结论更有趣但叙事占比不足。\n- 建议重新平衡叙事，将 function-level 等价的 surprising finding 作为核心故事。\n\n**R2-N2** [critical] **Repo-level 核心结果依赖 single-seed**\n- Table 3 无 ±std 或 CI。Table 10 显示 within-formulation seed variance 巨大。论文在 function-level 使用了 3-5 seeds 配合 TOST，但 repo-level 没有贯彻同标准。\n- 建议至少补充 2-3 seeds 或将 repo-level 结论降级为 preliminary observation。\n\n**R2-N3** [critical] **合成数据外部效度未验证**\n- 所有训练数据基于 mutation-based 合成 bug。Andrews 2005 和 Just 2014 讨论的是 mutation testing 在测试评估中的有效性，非 LLM verification 的迁移性。\"the synthetic-to-real transfer gap remains untested\"。\n- 建议在 SWE-bench Verified 的 gold patches 上做 zero-shot evaluation 验证 formulation ranking 一致性。\n\n### Should-Fix 问题\n\n**R2-W1** Abstract ~120-130 词，低于 ARR 推荐 150-250 词。缺少问题重要性论述和次要贡献提及。\n\n**R2-W2** 所有实验 ≤8B + LoRA/QLoRA。CWM 劣势可能是 capacity artifact 而非 formulation 固有限制。\n\n**R2-W3** 遗漏相关工作：Aletheia (2601.12186), VeRPO (2601.03525), ExecVerify (2603.11226)。\n\n**R2-W4** Tables 缺少次优下划线标记。\n\n**R2-W5** Venue fit 张力——SE/NLP 交叉论文，EMNLP 审稿人可能质疑 scope。建议讨论 findings 对 broader NLP verification 的 implications。\n\n### Minor\n- M1: -ing phrase in §3.4\n- M2: Figure 2 信息密度偏低\n- M3: Checklist C4 \"Partially\" 需补全\n- M4: 8 条 bib entry 未被 OpenAlex 索引（较新 preprint，不影响真实性）\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 评分: Overall 3.0 (Findings), Confidence 4/5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] **Novelty 有限：核心发现可预期**\n- \"classification > generation when outputs are complex\" 在概念上可预期。CodeScaler (Zhu et al., 2026) 已区分 \"sequence classifiers\" vs \"generative models\"。论文声称 \"the first systematic comparison\" 这个 gap 真实但 insight 深度有限。function-level 等价结论更有趣但叙事占比不足。\n- 建议重新平衡叙事，将 function-level 等价的 surprising finding 作为核心故事。\n\n**R2-N2** [critical] **Repo-level 核心结果依赖 single-seed**\n- Table 3 无 ±std 或 CI。Table 10 显示 within-formulation seed variance 巨大。论文在 function-level 使用了 3-5 seeds 配合 TOST，但 repo-level 没有贯彻同标准。\n- 建议至少补充 2-3 seeds 或将 repo-level 结论降级为 preliminary observation。\n\n**R2-N3** [critical] **合成数据外部效度未验证**\n- 所有训练数据基于 mutation-based 合成 bug。Andrews 2005 和 Just 2014 讨论的是 mutation testing 在测试评估中的有效性，非 LLM verification 的迁移性。\"the synthetic-to-real transfer gap remains untested\"。\n- 建议在 SWE-bench Verified 的 gold patches 上做 zero-shot evaluation 验证 formulation ranking 一致性。\n\n### Should-Fix 问题\n\n**R2-W1** Abstract ~120-130 词，低于 ARR 推荐 150-250 词。缺少问题重要性论述和次要贡献提及。\n\n**R2-W2** 所有实验 ≤8B + LoRA/QLoRA。CWM 劣势可能是 capacity artifact 而非 formulation 固有限制。\n\n**R2-W3** 遗漏相关工作：Aletheia (2601.12186), VeRPO (2601.03525), ExecVerify (2603.11226)。\n\n**R2-W4** Tables 缺少次优下划线标记。\n\n**R2-W5** Venue fit 张力——SE/NLP 交叉论文，EMNLP 审稿人可能质疑 scope。建议讨论 findings 对 broader NLP verification 的 implications。\n\n### Minor\n- M1: -ing phrase in §3.4\n- M2: Figure 2 信息密度偏低\n- M3: Checklist C4 \"Partially\" 需补全\n- M4: 8 条 bib entry 未被 OpenAlex 索引（较新 preprint，不影响真实性）\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 524 · 2026-05-19T11:14:25.573724+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24185
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-19T11:14:25.826044+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 评分: Overall 3.0 (Findings), Confidence 4/5\n\n### Must-Fix 问题\n\n**R1-N1** [critical] **Repo-level claims 的 single-seed 基础与 within-formulation 高方差矛盾**\n- Table 10: DeepSeek CLS per-test 82.51% (s42) vs 63.51% (s123)，波动 19pp；variant-level 81.25% vs 39.17%，波动 42pp。Within-formulation seed variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当。\n- §3.7 声称 gap \"exceeds any individual confound by an order of magnitude\"——Table 10 直接反驳此 claim。\n- 建议补充至少 3 seeds 或将 repo-level 明确标注为 preliminary。\n\n**R1-N2** [critical] **Checkpoint 选择系统性偏向 CLS**\n- 所有 CWM 运行因 NaN val loss 使用 final-epoch checkpoint，而 CLS 部分使用 val-selected。这不是个别 run 的问题，而是影响全部 CWM 运行的系统性偏差。对 \"matched conditions\" 论文来说，checkpoint selection 不 matched 是核心方法论缺陷。\n- Generation 任务的 overfitting dynamics 与 classification 不同，CWM checkpoint 效应可能 > 估计的 2pp。\n- 建议修复 CWM val loss 计算，或提供 CLS final-epoch vs val-selected 消融。\n\n**R1-N3** [critical] **SESOI (±2pp) 循环论证**\n- \"±2 pp corresponds to ~15 additional errors per 500 predictions\" 是 restated 含义而非 domain justification。Lakens 2017 要求 SESOI 基于 domain knowledge 或 existing literature。\n- \"approximately 30% headroom\" 表述误导：headroom 应指 (2.0−1.52)/2.0 = 24%，非 margin/observed_gap 比值。\n- 建议从下游应用角度（如 best-of-n pipeline）给出 functional justification。\n\n**R1-N4** [critical] **Oracle ensemble accuracy 数值自相矛盾**\n- §3.6: \"oracle combination achieves 90.63%\"；Appendix H(a): \"achieves 96.03% accuracy, +3.12pp over 87.51%\"。87.51 + 3.12 = 90.63 ≠ 96.03。正文与附录数字矛盾。\n- Error complementarity 是核心 contribution 之一，数字不一致直接损害可信度。\n\n### Should-Fix 问题\n\n**R1-W1** TRAJ 训练配置差异过大（~400 vs ~70K 实例, 不同 lr），downsample ablation 未控制 label granularity（per-test vs variant-level），volume-matched ≠ information-matched。\n\n**R1-W2** \"Formulation × model × complexity interaction\" 从未做形式化统计检验（factorial ANOVA 或 mixed-effects model），所有证据是描述性的。建议降级为 \"observed pattern\"。\n\n**R1-W3** CWM regime qualifier 在 Abstract/Conclusion 不充分。Abstract \"generation-based simulation falling below majority baseline\" 无 regime qualifier。\n\n**R1-W4** Re-repair negative result (effect size δ=0) 与 diagnostic value narrative 形成实质性张力。\"insufficient sample size\" 的 dismiss 不成立——effect size 本身为零。建议将 diagnostic granularity 从 core contribution 降级。\n\n**R1-W5** Synthetic mutation validity gap 同 R2-N3。\n\n### Minor\n- Table 2/3 中 function-level 和 repo-level 数据在同段交叉引用易混淆\n- Table 3 格式不清晰\n- §2.3 中 κ 的 n 未明确定义\n- Appendix 编号引用与实际可能不连续\n\n### Questions\n1. DeepSeek CLS 内部 19pp seed variance 中 preprocessing vs checkpoint vs random seed 各贡献多少？\n2. bf16-only TOST p-value 是多少？如果 p>0.05 需重新 qualify。\n3. Repo-level ICC=0.3146 对应 DEFF=114.4，effective n ≈ 86。repo-level CLS-CWM 的 clustered bootstrap CI？\n4. CWM unparseable 默认改为 FAIL 或 random 50/50 时 accuracy 如何变化？\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 评分: Overall 3.0 (Findings), Confidence 4/5\n\n### Must-Fix 问题\n\n**R1-N1** [critical] **Repo-level claims 的 single-seed 基础与 within-formulation 高方差矛盾**\n- Table 10: DeepSeek CLS per-test 82.51% (s42) vs 63.51% (s123)，波动 19pp；variant-level 81.25% vs 39.17%，波动 42pp。Within-formulation seed variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当。\n- §3.7 声称 gap \"exceeds any individual confound by an order of magnitude\"——Table 10 直接反驳此 claim。\n- 建议补充至少 3 seeds 或将 repo-level 明确标注为 preliminary。\n\n**R1-N2** [critical] **Checkpoint 选择系统性偏向 CLS**\n- 所有 CWM 运行因 NaN val loss 使用 final-epoch checkpoint，而 CLS 部分使用 val-selected。这不是个别 run 的问题，而是影响全部 CWM 运行的系统性偏差。对 \"matched conditions\" 论文来说，checkpoint selection 不 matched 是核心方法论缺陷。\n- Generation 任务的 overfitting dynamics 与 classification 不同，CWM checkpoint 效应可能 > 估计的 2pp。\n- 建议修复 CWM val loss 计算，或提供 CLS final-epoch vs val-selected 消融。\n\n**R1-N3** [critical] **SESOI (±2pp) 循环论证**\n- \"±2 pp corresponds to ~15 additional errors per 500 predictions\" 是 restated 含义而非 domain justification。Lakens 2017 要求 SESOI 基于 domain knowledge 或 existing literature。\n- \"approximately 30% headroom\" 表述误导：headroom 应指 (2.0−1.52)/2.0 = 24%，非 margin/observed_gap 比值。\n- 建议从下游应用角度（如 best-of-n pipeline）给出 functional justification。\n\n**R1-N4** [critical] **Oracle ensemble accuracy 数值自相矛盾**\n- §3.6: \"oracle combination achieves 90.63%\"；Appendix H(a): \"achieves 96.03% accuracy, +3.12pp over 87.51%\"。87.51 + 3.12 = 90.63 ≠ 96.03。正文与附录数字矛盾。\n- Error complementarity 是核心 contribution 之一，数字不一致直接损害可信度。\n\n### Should-Fix 问题\n\n**R1-W1** TRAJ 训练配置差异过大（~400 vs ~70K 实例, 不同 lr），downsample ablation 未控制 label granularity（per-test vs variant-level），volume-matched ≠ information-matched。\n\n**R1-W2** \"Formulation × model × complexity interaction\" 从未做形式化统计检验（factorial ANOVA 或 mixed-effects model），所有证据是描述性的。建议降级为 \"observed pattern\"。\n\n**R1-W3** CWM regime qualifier 在 Abstract/Conclusion 不充分。Abstract \"generation-based simulation falling below majority baseline\" 无 regime qualifier。\n\n**R1-W4** Re-repair negative result (effect size δ=0) 与 diagnostic value narrative 形成实质性张力。\"insufficient sample size\" 的 dismiss 不成立——effect size 本身为零。建议将 diagnostic granularity 从 core contribution 降级。\n\n**R1-W5** Synthetic mutation validity gap 同 R2-N3。\n\n### Minor\n- Table 2/3 中 function-level 和 repo-level 数据在同段交叉引用易混淆\n- Table 3 格式不清晰\n- §2.3 中 κ 的 n 未明确定义\n- Appendix 编号引用与实际可能不连续\n\n### Questions\n1. DeepSeek CLS 内部 19pp seed variance 中 preprocessing vs checkpoint vs random seed 各贡献多少？\n2. bf16-only TOST p-value 是多少？如果 p>0.05 需重新 qualify。\n3. Repo-level ICC=0.3146 对应 DEFF=114.4，effective n ≈ 86。repo-level CLS-CWM 的 clustered bootstrap CI？\n4. CWM unparseable 默认改为 FAIL 或 random 50/50 时 accuracy 如何变化？\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-19T11:14:27.290378+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1464
}
```

</details>

---


### Assistant

_source line 527 · 2026-05-19T11:14:31.651128+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 528 · 2026-05-19T11:14:34.247089+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)，Confidence 4/5。

四个 Must-Fix 问题：
1. Repo-level 核心 claims 基于 single seed，但 within-CLS seed variance (~19pp) 与 CLS-CWM gap (~19-26pp) 量级相当，§3.7 中 "exceeds confounds by an order of magnitude" 的表述被 Table 10 数据直接反驳
2. 所有 CWM 运行因 NaN val loss 使用 final-epoch checkpoint（非 val-selected），系统性低估 CWM，对 "matched comparison" 定位构成核心方法论缺陷
3. TOST 的 ±2pp SESOI 缺乏 domain-grounded justification（循环论证），"307% headroom" 表述误导
4. Oracle ensemble accuracy 在正文 (90.63%) 与附录 (96.03%) 之间数值矛盾（87.51 + 3.12 = 90.63 ≠ 96.03）

五个 Should-Fix：TRAJ 训练配置差异未充分控制、三阶交互未做形式化检验、CWM 结论缺 regime qualifier、re-repair negative result 与 diagnostic value narrative 矛盾（δ=0 不是 power 问题）、synthetic mutation validity gap。

主要优势：首个 matched comparison、统计框架超越 NLP 标准、function-level equivalence 可信、附录透明度极高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 529 · 2026-05-19T11:14:39.764270+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 530 · 2026-05-19T11:15:36.396536+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — Reviewer 2 意见

---

### Must-Fix 回应

**[AGREE] R2-N1: Novelty 有限，核心发现可预期**

同意方向，但对 severity 和具体建议有补充。

R2 指出 "classification > generation when outputs are complex" 在概念上可预期——这一判断是合理的。从 sequence modeling 角度看，CLS 只需要输出一个 binary label（几个 token），CWM 需要精确重建完整输出序列（数百 token），后者在长序列下更容易出错是直觉可预期的。论文 §2.2 的 failure mode taxonomy（format collapse、token exhaustion）本质上是在形式化这个直觉，而非挑战它。

但我与 R2 的侧重略有不同：**问题不仅是 novelty，更是 claim-evidence 的权重分配。** 论文将 repo-level divergence（19-26pp）作为 headline result 置于 Abstract 和 §1，但这个结论：(a) 直觉上可预期，(b) 统计上依赖 single seed（我的 N1），(c) 受 checkpoint confound 影响（我的 N2）。相比之下，function-level equivalence 是一个 **非显然的、统计上 robust 的发现**（5 seeds × 2 model families, TOST p=0.007）——"CWM 在 function-level 并不比 CLS 差"这一结论是违反直觉的，因为 CWM 的 task difficulty 明显更高。

R2 建议重新平衡叙事——我支持，但补充一点：function-level equivalence 的叙事如果成为 headline，需要加强 SESOI justification（我的 N3），否则 "equivalence" claim 的基础仍有问题。

**[AGREE] R2-N2: Repo-level 核心结果依赖 single-seed**

完全同意，这与我的 N1 高度重叠。

我补充一个 R2 未提及但加强此 concern 的证据点：**Table 10 中 DeepSeek CLS 的 within-formulation seed variance**。DeepSeek CLS per-test accuracy 从 82.51%（s42）到 63.51%（s123），差距 19pp——与 CLS-CWM gap（19-26pp）量级相当。论文 §3.7 声称 gap "exceeds any individual confound by an order of magnitude"，但 Table 10 的数据直接反驳此表述。

R2 的建议（2-3 seeds 或降级为 preliminary）与我的建议一致。两位 reviewer 独立提出相同 concern，应视为 high-consensus Must-Fix。

**[REBUT] R2-N3: 合成数据外部效度未验证 → 应为 Should-Fix 而非 Must-Fix**

反驳 severity level，部分同意 substance。

R2 将此定为 Must-Fix，我认为应为 **Should-Fix**，理由如下：

1. **论文的核心 claim 是 formulation 之间的相对排序，不是绝对性能。** 如果 synthetic mutation 与 real bugs 的 distribution shift 对所有 formulations 影响相近（即 shift 是 formulation-agnostic 的），那么在 synthetic data 上建立的 relative ranking 仍然有效。要否定论文结论，需要论证 shift 对 CLS 和 CWM 的影响不同——R2 未提供此论证。

2. **Zero-shot evaluation on SWE-bench gold patches 的建议有操作问题。** SWE-bench Verified 的 "gold patches" 是 real bug fixes，不是 real bugs + tests 的 pass/fail labels。要在 gold patches 上评估 verifier，需要已知哪些 tests 应该 pass/fail，这正是 mutation 提供的。直接在 SWE-bench 上做 zero-shot（无 fine-tuning）评估的是 base model 能力，不是 formulation 的相对优势。

3. **我在 W5 中已经以 Should-Fix 标注了此问题**，建议在真实 bug 上做 sanity check。我维持 Should-Fix 的 severity 判断。

但 R2 正确指出 Andrews 2005 和 Just 2014 的引用不能直接支持 LLM verification 中的迁移性——这些经典研究的语境是 test suite adequacy evaluation，不是 LLM training data distribution matching。论文应更明确说明这个 gap。

---

### Should-Fix 回应

**[AGREE] R2-W1: Abstract 偏短**

同意。~120-130 words 低于 ARR 推荐的 150-250 words。更重要的是，短 Abstract 导致论文缺少 "为什么重要" 的 motivating statement 和 function-level equivalence 这个更 surprising 的结论的空间。如果按 R2-N1 的建议重新平衡叙事，Abstract 自然需要扩展。

补充一个我注意到的问题：Abstract 中 "generation-based simulation falling below majority baseline" 缺乏 regime qualifier（≤8B LoRA），这与我的 W3 一致。扩写 Abstract 时应同时修复此问题。

**[AGREE] R2-W2: ≤8B + LoRA 可能是 capacity artifact**

同意，与我的 W3 高度一致。我在 W3 中指出论文在 §3.1 有 regime qualifier 但 Abstract/Conclusion 中经常省略。R2 从 capacity artifact 角度切入，补充了一个重要视角：CWM（generation task）对 model capacity 的需求可能高于 CLS（classification task），因此 capacity constraint 对 CWM 的影响不是 uniform 的，而是 disproportionately 惩罚 CWM。这进一步削弱了 "CWM 在 repo-level 本质上差" 的推论。

**[REBUT] R2-W3: 遗漏 Aletheia (2601.12186), VeRPO (2601.03525), ExecVerify (2603.11226)**

部分反驳。

我无法直接验证这三篇论文的存在和相关性（未在论文中搜索到引用，也无法独立确认 arXiv ID）。R2 有责任说明这些工作与本文的具体关系——"遗漏相关工作" 需要解释 **为什么** 遗漏这些论文会影响论文的 positioning 或 completeness。如果这三篇论文涉及 execution-free verification 的 formulation 比较，那确实是重要遗漏；如果只是 general code verification 工作，则论文已有 60 条引用（verify_references 确认 0 orphan, 0 missing），覆盖度可能已经足够。

建议 R2 在后续轮次中说明每篇遗漏论文与本文的具体关系（directly competing? different formulation? extends this work's setup?）。

**[AGREE] R2-W4: Tables 缺少次优下划线**

同意。这是 NLP 论文的标准做法（最优加粗、次优下划线），Table 1-3 均未遵循。Minor 但应该修复。

**[REBUT] R2-W5: Venue fit 张力**

不同意这是 Should-Fix 级别的问题。

1. **EMNLP 近年持续接收 code-related 论文。** CodeBERTScore (Zhou et al., 2023) 在 EMNLP 发表；PRLCoder (Ye et al., 2025) 在 EMNLP 发表；S* (Li et al., 2025) 在 Findings of EMNLP 发表——论文自己的 reference list 就包含多篇 EMNLP code 论文。EMNLP 的 scope 明确包含 "computational semantics" 和 "language models for code"。

2. **论文的统计方法论（TOST、clustered bootstrap、ICC）、formulation 设计空间的概念框架、以及 NLP-style verification（CLS as QA, CWM as conditional generation）都是 NLP 社区关心的问题。** 这不是一篇纯 SE 论文——它的核心是 LLM 训练策略的比较，只是应用在 code verification 领域。

3. R2 建议 "讨论 findings 对 broader NLP verification 的 implications"——这个建议本身合理（可以在 Conclusion 中加一段 generalization 讨论），但不构成 Should-Fix 级别的 venue fit 问题。

---

### Minor 回应

- **M1** (-ing phrase): 同意，但这是 cosmetic issue。
- **M2** (Figure 2 信息密度低): 同意。Figure 2 的概念图如果只传达三种 formulation 的 input/output 对比，可以压缩为半栏宽。
- **M3** (Checklist C4 "Partially"): 同意，应补全版本号。
- **M4** (8 条 bib 未被 OpenAlex 索引): 同意这不影响真实性。我的 verify_references 结果确认这 8 条均为较新 preprint 或 API 索引限制，非 fabricated citations。

---

### 两位 Reviewer 共识总结

**高共识 Must-Fix**（两人独立提出）：
- Repo-level single-seed 问题（R1-N1 = R2-N2）
- CWM regime qualifier 不足（R1-W3 ≈ R2-W2，R2 从 capacity artifact 角度，R1 从 framing 角度）

**R1 独有的 Must-Fix**（R2 未覆盖）：
- Checkpoint 选择系统性偏差（R1-N2）——R2 未注意到 NaN val loss 导致全部 CWM 使用 final-epoch checkpoint 这个 confound
- SESOI justification 不足（R1-N3）——R2 未质疑 TOST 方法论细节
- Oracle accuracy 数值矛盾（R1-N4）——R2 未注意到 §3.6 vs H(a) 的 90.63% vs 96.03% 不一致

**Severity 分歧**：
- 合成数据 validity（R2 视为 Must-Fix N3, R1 视为 Should-Fix W5）——我认为 Should-Fix 更合理，因为论文的核心是 relative ranking 而非 absolute performance

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 531 · 2026-05-19T11:15:44.389370+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 532 · 2026-05-19T11:15:47.037302+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：

- **R2-N2 (single-seed)**: 完全同意，补充了 Table 10 中 DeepSeek within-CLS 19pp variance 的证据，两位 reviewer 高共识
- **R2-N1 (novelty)**: 同意方向，但指出核心 novelty 应转向 function-level equivalence（违反直觉且统计 robust），而非 repo-level divergence（可预期且证据弱）
- **R2-N3 (synthetic validity)**: 反驳 severity level，应为 Should-Fix 而非 Must-Fix——论文关心的是 formulation 间相对排序，只要 distribution shift 是 formulation-agnostic 的，排序结论仍有效
- **R2-W3 (missing references)**: 部分反驳，要求 R2 说明三篇论文与本文的具体关系
- **R2-W5 (venue fit)**: 反驳，EMNLP 近年持续接收 code 论文，论文核心是 LLM 训练策略比较

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 533 · 2026-05-19T11:15:54.020480+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 48

## Round 48

10 recorded events


### User

_source line 534 · 2026-05-19T11:17:35.441948+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1

---

### Must-Fix

**[AGREE] R1-N1: Repo-level single-seed + 高 within-formulation variance**

完全同意，这是 R1 提出的最有力的技术问题。Table 10 显示 DeepSeek CLS per-test 82.51% vs 63.51%（约 19pp variance），variant-level 81.25% vs 29.17%（超过 50pp）。当 within-formulation seed variance 与 between-formulation gap（19-26pp）处于同一量级时，论文无法从统计上区分 "formulation effect" 和 "seed noise"。

Section 3.7 声称 gap "exceeds any individual confound by an order of magnitude" 被 Table 10 的数据直接反驳——R1 准确地指出了这一点。我在 R2-N2 中也独立提出了相同问题（single-seed repo-level），但 R1 给出了更精确的定量证据。

补充发现：Extended Limitations (p18) 进一步承认 "checkpoint selection variance could contribute to observed differences"，这与 R1-N2 形成联动。repo-level claims 的统计基础整体上是脆弱的。

---

**[AGREE] R1-N2: Checkpoint selection 系统性偏向 CLS**

同意这是一个重要的方法论缺陷。Section 3.1 (p4) 明确说明 "validation loss is computationally run using training preprocessor produce NaN validation loss due to length-mismatched sequences, which defaults to the final epoch checkpoint (affects DeepSeek s123 and all CWM runs)"。这意味着：

1. CLS 享有 val-based best checkpoint selection
2. CWM **全部**使用 final-epoch checkpoint（因为 NaN val loss）
3. 这是系统性偏差，不是随机噪声

对一篇以 "matched conditions" 为核心方法论贡献的论文来说，checkpoint selection 不 matched 确实构成核心矛盾。CWM 可能因为 overfitting（generation 任务 overfitting dynamics 不同于 classification）而在 final epoch 表现下降，而 CLS 通过 val selection 规避了这一问题。

R1 建议的 "CLS final-epoch vs val-selected ablation" 是最小成本的修复方案，可以量化 checkpoint selection 贡献了多少差距。

---

**[AGREE with nuance] R1-N3: SESOI ±2pp 循环论证**

部分同意。R1 的技术批评是准确的：

1. "~15 additional errors per 500 predictions" 确实是 ±2pp 的数学等价表述而非 domain justification。Lakens (2017) 要求 SESOI 基于 smallest effect size of interest from a practical standpoint（如 downstream task performance difference）。论文引用了 Lakens 但未遵循其方法论精神。
2. "30% headroom" 的表述：(2.0 − 1.52)/2.0 = 24%，R1 的计算正确。论文可能用的是 2.0/1.52 − 1 ≈ 31.6%，但这种表达方式（margin/gap ratio）确实容易误导。

**但我不认为这是 critical 级别。** TOST 等价检验是论文的辅助证据（supporting evidence），核心 claim（function-level 等价）也得到了 Table 1 中直接的 accuracy 比较和 overlap 的 CI 支持。即使 SESOI 设定有争议，function-level 三者差距确实小（CLS 88.43, CWM 87.19, TRAJ 86.30，最大差距仅 2.13pp），这一 pattern 不依赖 TOST 的 margin 选择。

建议保持为 should-fix：改写 SESOI justification 引入 downstream functional argument（如 best-of-n reranking 中 2pp verifier accuracy 差距的 practical impact），并修正 headroom 计算。

---

**[AGREE] R1-N4: Oracle ensemble 数值矛盾**

完全同意。Appendix H(a) (p16) 原文说 "An oracle combination achieves 96.03% accuracy, +3.12pp over the best single formulation (87.51%)"。但 87.51 + 3.12 = 90.63 ≠ 96.03。这两个数字中至少有一个是错误的：
- 如果 oracle 是 90.63%，则 "+3.12pp over 87.51%" 正确但 96.03% 是 typo
- 如果 oracle 是 96.03%，则增量应是 +8.52pp 而非 +3.12pp

Section 3.6 没有给出明确的 oracle accuracy 数字（我在正文中未找到 90.63% 的直接出现），但 Contribution bullet (p2) 提到 "an oracle ensemble improves over the best single formulation (§3.6)" 但未给数字。

Error complementarity 是论文的四条 contributions 之一，核心数据自相矛盾是不可接受的。R1 准确识别了这一问题。作者必须核查并统一所有 oracle 相关数字。

---

### Should-Fix

**[AGREE] R1-W1: TRAJ 训练配置差异过大**

同意。TRAJ 使用 ~400 variant-level instances（vs CLS/CWM ~70K per-test instances），学习率不同（5×10⁻⁶ vs 2×10⁻⁴），且 downsample ablation 只控制了数据量而未控制 label granularity。即使 volume-matched（将 CLS/CWM 下采样到 ~400），per-test label 包含的信息量仍然大于 variant-level label。这是一个 inherent confound，但论文应更明确地讨论它，而非将 downsample 结果作为 TRAJ 与 CLS/CWM 可比性的充分证据。

---

**[AGREE] R1-W2: 缺乏 formulation × model × complexity 交互效应的正式检验**

同意。论文大量使用 "consistent across model families" 和 "model-contingent in magnitude" 等表述（Abstract, Section 3.2-3.3），但从未用 factorial ANOVA 或 mixed-effects model 检验 formulation × model × complexity 的交互效应。所有证据都是描述性的（Table 1-3 的直接比较）。

对于一篇强调统计方法论严谨性（TOST, ICC, bootstrap CI）的论文，缺少这一关键检验是一个方法论上的不完整。建议要么补充正式检验，要么在措辞上降级为 "observed pattern"。

---

**[AGREE] R1-W3: CWM regime qualifier 在 Abstract/Conclusion 不充分**

同意。Abstract 说 "generation-based simulation falling below majority baseline"，但这只在 repo-level 的特定配置下成立。Conclusion 中 "CWM falls below majority baseline (19-26pp gap)" 同样缺少 regime qualifier。读者可能误解为 CWM 在所有场景下都低于 majority baseline，而实际上在 function-level CWM 与 CLS 等价。这是一个 framing 问题，修复成本低但影响读者印象。

---

**[AGREE] R1-W4: Re-repair negative result 与 diagnostic value narrative 的张力**

同意，且认为这一点比 R1 给予的 severity 更严重。Section 3.5 (p18 注脚或正文) 报告 re-repair pilot 的 effect size δ=0。论文用 "insufficient sample size (n=44, statistical power ≈ 0.3)" 来 dismiss 这个 negative result，但 R1 准确指出：当 effect size 本身为零时，增加 sample size 不会改变结论方向。Power 不足只意味着不能排除小效应的存在，但观测到的 point estimate 是零。

这与论文的第四条 contribution "Diagnostic granularity with configuration-dependent cost" 直接矛盾——如果 per-test diagnostics 无法改善 downstream re-repair，"diagnostic granularity" 的实际价值就缺乏证据支持。建议将 diagnostic granularity 从核心 contribution 降级为 "potential advantage requiring future validation"，或者补充更大规模的 re-repair 实验。

---

**[AGREE] R1-W5: Synthetic mutation validity gap**

同意，与我在 R2-N3 中的独立判断一致。两位 Reviewer 独立得出相同结论，增强了这一问题的 severity。

---

### R1 提问的补充意见

R1 的 4 个 Questions 均有价值，特别是：
- **Q2 (bf16-only TOST p-value)**: 这一点我未独立发现。如果仅限 bf16 precision 的 runs，TOST 可能不再显著，这会直接影响 function-level 等价的核心 claim。
- **Q4 (CWM unparseable 默认策略)**: Section 3.1 提到 unparseable 默认改为 pass（majority class default），但如果改为 FAIL 或 random 50/50，CWM accuracy 可能显著变化。这关系到 CWM 结果的 robustness。

---

### 综合判断

R1 和 R2 的审稿意见高度互补：
- **R1 在技术方法论上更深入**（checkpoint selection bias, SESOI 循环论证, TRAJ 训练配置, oracle 数值矛盾）
- **R2 在 novelty 和 venue fit 上更聚焦**（核心发现可预期性, 遗漏的 recent work, EMNLP scope 问题）
- **两者独立一致的发现**：single-seed repo-level (R1-N1 = R2-N2)、synthetic data gap (R1-W5 = R2-N3)

我维持 Overall 3.0 (Findings) 的评分。R1 发现的 oracle 数值矛盾 (R1-N4) 和 checkpoint selection bias (R1-N2) 是我遗漏的重要问题，但不改变整体判断——论文的核心问题仍然是 novelty 有限（R2-N1）加上 repo-level 统计效力不足（R1-N1/R2-N2 共识）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 535 · 2026-05-19T11:18:03.965765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-19T11:18:04.016392+00:00_

1	\begin{abstract}
2	Execution-free verification for LLM-based code repair can be formulated as per-test binary classification (\cls{}), execution output generation (\cwm{}), or trajectory-level patch scoring. No prior work compares these formulations under matched conditions. We present a systematic comparison across two model families, two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning.
3	
4	At function level, all three formulations achieve near-equivalent accuracy (TOST equivalence within $\pm$2\pp{}, 5 seeds). At repository level, divergence amplifies to 19--26\pp{}, with generation-based simulation falling below majority baseline. The pattern is consistent across model families but model-contingent in magnitude.
5	
6	Per-test classification provides diagnostic granularity at comparable accuracy, with configuration-dependent aggregation cost at repository level. Formulations exhibit complementary errors at function level, motivating complexity-aware routing over uniform formulation selection.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 537 · 2026-05-19T11:18:04.117284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 538 · 2026-05-19T11:18:04.117954+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	These three formulations represent discrete points in the verification design space, each imposing different output complexity, diagnostic granularity, and inference cost. We present the first systematic empirical comparison across two model families (Qwen3, DeepSeek-Co
…[truncated 2657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 539 · 2026-05-19T11:19:33.102148+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "# === Round 6 Issues ===\n# Fresh review (session reset); prior round issues preserved for continuity tracking\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。Table 10 DeepSeek CLS per-test 82.51% vs 63.51% (19pp); variant-level 81.25% vs 29.17% (52pp)。§3.7 'exceeds confounds by order of magnitude' 被 Table 10 直接反驳。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI，或将所有 repo-level conclusions 标注为 preliminary/suggestive + 修正 §3.7 措辞\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS：全部 CWM 运行因 NaN val loss 使用 final-epoch，CLS 使用 val-selected\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 交叉分享中完全同意。系统性偏差方向与 observed effect 一致（CWM 被低估）。对 'matched conditions' 定位构成核心矛盾。\"\n  action_items:\n    - round: 6\n      action: \"修复 CWM val loss 使 checkpoint selection 一致；或提供 CLS final-epoch vs val-selected 消融量化 bias；升级 §3.7 中的讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾：§3.6/Conclusion 90.63% vs Appendix H(a) 96.03%\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 发现，R2 交叉中确认。87.51 + 3.12 = 90.63 ≠ 96.03。Error complementarity 是核心 contribution 之一，数字不一致直接损害可信度。\"\n  action_items:\n    - round: 6\n      action: \"核实并统一所有 oracle accuracy 数字（正文、附录、结论）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：repo-level 核心发现 'classification > generation for complex outputs' 概念上可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意方向。R1 建议将 function-level equivalence（违反直觉且统计 robust）作为 headline 而非 repo-level divergence（可预期且 single-seed）。\"\n  action_items:\n    - round: 6\n      action: \"重新平衡叙事：function-level equivalence 升为核心故事，repo-level divergence 降为 supporting evidence with caveats\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 缺乏 domain-grounded justification（循环论证），headroom 表述误导\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 定为 critical，R2 降为 should-fix（TOST 是辅助证据，function-level equivalence 不依赖 TOST margin 选择）。分歧记录。\"\n  action_items:\n    - round: 6\n      action: \"从下游应用角度重写 SESOI justification（如 best-of-n pipeline impact）；修正 '30% headroom' 计算\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier (≤8B LoRA) 在 Abstract/Conclusion 不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出。Abstract 'generation-based simulation falling below majority baseline' 无 regime qualifier。Conclusion 同。\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Conclusion 中所有 CWM 劣势 claim 加 '≤8B LoRA' qualifier\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Re-repair negative result (δ=0) 与 diagnostic granularity narrative 实质性矛盾\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 提出 W4，R2 交叉同意并认为 severity 应更高。effect size=0 不是 underpowered type II error，是真零效应。与第四条 contribution 矛盾。\"\n  action_items:\n    - round: 6\n      action: \"Diagnostic granularity 从 core contribution 降级为 'potential advantage pending downstream validation'；或补充更大规模 re-repair 实验\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异过大 (~400 vs ~70K)，downsample ablation 未控制 label granularity\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。volume-matched ≠ information-matched (per-test vs variant-level labels)。\"\n  action_items:\n    - round: 6\n      action: \"明确讨论 volume vs granularity 区别；如可行在 variant-level aggregated labels 上训练 CLS 作为 ablation\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"'Formulation × model × complexity interaction' 未做形式化统计检验\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。所有证据是描述性的，未用 factorial ANOVA 或 mixed-effects model 检验。\"\n  action_items:\n    - round: 6\n      action: \"降级 'interaction' 措辞为 'observed pattern'，或在多 seed 数据下做 two-way interaction 检验\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 数据外部效度未验证（synthetic-to-real transfer gap）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 定为 Must-Fix，R1 反驳降为 Should-Fix：论文关心 relative ranking 非绝对性能，shift 若 formulation-agnostic 则排序有效。分歧记录，采纳 Should-Fix。\"\n  action_items:\n    - round: 6\n      action: \"更明确讨论 Andrews/Just 引用的适用范围；如可行在真实 bug 上做 transfer sanity check\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Abstract ~120-130 词偏短，低于 ARR 推荐 150-250 词\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意。缺少问题重要性论述和 function-level equivalence 这个更 surprising 结论。\"\n  action_items:\n    - round: 6\n      action: \"扩展至 ~180 词，补充 motivation 和 function-level equivalence\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作（Aletheia 等待验证）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 提出 Aletheia/VeRPO/ExecVerify。R1 部分反驳，要求说明具体关系。待验证。\"\n  action_items:\n    - round: 6\n      action: \"验证 R2 推荐的三篇论文存在性和相关性；如确实相关则补入 Related Work\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 1-3 缺少次优下划线标记\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意。NLP 论文标准做法。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers 需补全\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"当前回答 'Partially'，camera-ready 前需补全。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 bar chart 信息密度偏低\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"可考虑加入 CI 或 per-model breakdown。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (preserved for continuity) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超出 ARR Long Paper 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需砍 ~3 页。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"本轮未提及。PDF 确认正文 8 页合规。\"\n  resolution: \"正文已压缩至 8 页。Round 6 确认合规。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ Qwen3-8B checkpoint 选择不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"cherry-picking 嫌疑\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Table 3 已报告两组数字并标注 post-hoc。但 R6-N2 将 checkpoint 问题扩展到全部 CWM 运行。\"\n  resolution: \"TRAJ 已透明报告。CWM checkpoint 问题升级为 R6-N2。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合 per-test 和 variant-level 指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需加 Variant Acc 列\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。Table 3 已含 Variant Acc 列。\"\n  resolution: \"Table 3 (原 Table 4) 已包含 variant-level accuracy 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST ±2pp margin 缺乏 sensitivity analysis\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"缺 gradient table\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Sensitivity table 完成，但需 SESOI 框架\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Table 13 sensitivity + Lakens 2017 引用已有。但 R6-W1 指出 SESOI justification 仍循环论证，headroom 计算有误。\"\n  action_items:\n    - round: 6\n      action: \"见 R6-W1\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA conditioning 不够突出\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"全文加 qualifier\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Conclusion/Threats 有，Abstract/Intro 缺\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"仍未修复。Abstract 'generation-based simulation falling below majority baseline' 无 qualifier。见 R6-W2。\"\n  action_items:\n    - round: 6\n      action: \"见 R6-W2\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"211 词，数字太多\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"~170 words 仍含多个数字\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"~120-130 words 偏短但数据堆砌问题已缓解。新问题变为字数不足。见 R6-W7。\"\n  action_items:\n    - round: 6\n      action: \"见 R6-W7\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# Older resolved issues preserved\n- id: \"R4-W3\"\n  summary: \"Cross-model 'validation' 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"已改为 'consistency check'。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较问题未处理\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏近期工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"58 篇引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 不是独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"独立 section* 已有。\"\n  resolution_round: 5\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "# === Round 6 Issues ===\n# Fresh review (session reset); prior round issues preserved for continuity tracking\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。Table 10 DeepSeek CLS per-test 82.51% vs 63.51% (19pp); variant-level 81.25% vs 29.17% (52pp)。§3.7 'exceeds confounds by order of magnitude' 被 Table 10 直接反驳。\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI，或将所有 repo-level conclusions 标注为 preliminary/suggestive + 修正 §3.7 措辞\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS：全部 CWM 运行因 NaN val loss 使用 final-epoch，CLS 使用 val-selected\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 交叉分享中完全同意。系统性偏差方向与 observed effect 一致（CWM 被低估）。对 'matched conditions' 定位构成核心矛盾。\"\n  action_items:\n    - round: 6\n      action: \"修复 CWM val loss 使 checkpoint selection 一致；或提供 CLS final-epoch vs val-selected 消融量化 bias；升级 §3.7 中的讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾：§3.6/Conclusion 90.63% vs Appendix H(a) 96.03%\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 发现，R2 交叉中确认。87.51 + 3.12 = 90.63 ≠ 96.03。Error complementarity 是核心 contribution 之一，数字不一致直接损害可信度。\"\n  action_items:\n    - round: 6\n      action: \"核实并统一所有 oracle accuracy 数字（正文、附录、结论）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：repo-level 核心发现 'classification > generation for complex outputs' 概念上可预期\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意方向。R1 建议将 function-level equivalence（违反直觉且统计 robust）作为 headline 而非 repo-level divergence（可预期且 single-seed）。\"\n  action_items:\n    - round: 6\n      action: \"重新平衡叙事：function-level equivalence 升为核心故事，repo-level divergence 降为 supporting evidence with caveats\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 缺乏 domain-grounded justification（循环论证），headroom 表述误导\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 定为 critical，R2 降为 should-fix（TOST 是辅助证据，function-level equivalence 不依赖 TOST margin 选择）。分歧记录。\"\n  action_items:\n    - round: 6\n      action: \"从下游应用角度重写 SESOI justification（如 best-of-n pipeline impact）；修正 '30% headroom' 计算\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier (≤8B LoRA) 在 Abstract/Conclusion 不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出。Abstract 'generation-based simulation falling below majority baseline' 无 regime qualifier。Conclusion 同。\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Conclusion 中所有 CWM 劣势 claim 加 '≤8B LoRA' qualifier\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Re-repair negative result (δ=0) 与 diagnostic granularity narrative 实质性矛盾\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 提出 W4，R2 交叉同意并认为 severity 应更高。effect size=0 不是 underpowered type II error，是真零效应。与第四条 contribution 矛盾。\"\n  action_items:\n    - round: 6\n      action: \"Diagnostic granularity 从 core contribution 降级为 'potential advantage pending downstream validation'；或补充更大规模 re-repair 实验\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异过大 (~400 vs ~70K)，downsample ablation 未控制 label granularity\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。volume-matched ≠ information-matched (per-test vs variant-level labels)。\"\n  action_items:\n    - round: 6\n      action: \"明确讨论 volume vs granularity 区别；如可行在 variant-level aggregated labels 上训练 CLS 作为 ablation\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"'Formulation × model × complexity interaction' 未做形式化统计检验\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。所有证据是描述性的，未用 factorial ANOVA 或 mixed-effects model 检验。\"\n  action_items:\n    - round: 6\n      action: \"降级 'interaction' 措辞为 'observed pattern'，或在多 seed 数据下做 two-way interaction 检验\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 数据外部效度未验证（synthetic-to-real transfer gap）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 定为 Must-Fix，R1 反驳降为 Should-Fix：论文关心 relative ranking 非绝对性能，shift 若 formulation-agnostic 则排序有效。分歧记录，采纳 Should-Fix。\"\n  action_items:\n    - round: 6\n      action: \"更明确讨论 Andrews/Just 引用的适用范围；如可行在真实 bug 上做 transfer sanity check\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Abstract ~120-130 词偏短，低于 ARR 推荐 150-250 词\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意。缺少问题重要性论述和 function-level equivalence 这个更 surprising 结论。\"\n  action_items:\n    - round: 6\n      action: \"扩展至 ~180 词，补充 motivation 和 function-level equivalence\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作（Aletheia 等待验证）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 提出 Aletheia/VeRPO/ExecVerify。R1 部分反驳，要求说明具体关系。待验证。\"\n  action_items:\n    - round: 6\n      action: \"验证 R2 推荐的三篇论文存在性和相关性；如确实相关则补入 Related Work\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 1-3 缺少次优下划线标记\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 同意。NLP 论文标准做法。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers 需补全\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"当前回答 'Partially'，camera-ready 前需补全。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 bar chart 信息密度偏低\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"可考虑加入 CI 或 per-model breakdown。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (preserved for continuity) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超出 ARR Long Paper 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需砍 ~3 页。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"本轮未提及。PDF 确认正文 8 页合规。\"\n  resolution: \"正文已压缩至 8 页。Round 6 确认合规。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ Qwen3-8B checkpoint 选择不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"cherry-picking 嫌疑\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Table 3 已报告两组数字并标注 post-hoc。但 R6-N2 将 checkpoint 问题扩展到全部 CWM 运行。\"\n  resolution: \"TRAJ 已透明报告。CWM checkpoint 问题升级为 R6-N2。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合 per-test 和 variant-level 指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需加 Variant Acc 列\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。Table 3 已含 Variant Acc 列。\"\n  resolution: \"Table 3 (原 Table 4) 已包含 variant-level accuracy 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST ±2pp margin 缺乏 sensitivity analysis\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"缺 gradient table\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Sensitivity table 完成，但需 SESOI 框架\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Table 13 sensitivity + Lakens 2017 引用已有。但 R6-W1 指出 SESOI justification 仍循环论证，headroom 计算有误。\"\n  action_items:\n    - round: 6\n      action: \"见 R6-W1\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA conditioning 不够突出\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"全文加 qualifier\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Conclusion/Threats 有，Abstract/Intro 缺\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"仍未修复。Abstract 'generation-based simulation falling below majority baseline' 无 qualifier。见 R6-W2。\"\n  action_items:\n    - round: 6\n      action: \"见 R6-W2\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"211 词，数字太多\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"~170 words 仍含多个数字\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"~120-130 words 偏短但数据堆砌问题已缓解。新问题变为字数不足。见 R6-W7。\"\n  action_items:\n    - round: 6\n      action: \"见 R6-W7\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# Older resolved issues preserved\n- id: \"R4-W3\"\n  summary: \"Cross-model 'validation' 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"已改为 'consistency check'。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较问题未处理\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏近期工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"58 篇引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 不是独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"独立 section* 已有。\"\n  resolution_round: 5\n"
  }
}
```

</details>

---


### Tool result

_source line 540 · 2026-05-19T11:19:33.204134+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 11982}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 541 · 2026-05-19T11:21:53.508939+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "report": "# 审稿报告 — Round 6 (Fresh Review)\n\n**论文**: The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 写作完整性 + 格式合规）\n**Overall**: 3.0 / 5（Findings）— 两位 Reviewer 一致\n**Confidence**: 4 / 5 — 两位 Reviewer 一致\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free code verification formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹评分），在两个模型家族（Qwen3-4B/8B、DeepSeek-Coder-6.7B）、两个复杂度级别（function-level、repo-level）、多 seed 条件下进行匹配实验。核心发现：function-level 三者近等价（TOST p=0.007, 5 seeds），repo-level CLS 领先 CWM 19-26pp（≤8B LoRA regime）。论文还提供了 failure mode taxonomy、error complementarity 分析和 oracle framework。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **填补真实文献空白**：首个在 matched conditions 下系统比较三种 execution-free verification formulations 的工作，研究问题定义清晰且有实际价值。\n\n**S2** [R1+R2 共识] **统计方法论超越 NLP 常见标准**：TOST equivalence testing（而非仅用 p-value 证明差异不显著）、clustered bootstrap（114 clusters, 10K resamples）、ICC with design effect、Holm-Bonferroni correction (k=4) 的组合在 NLP 实证论文中罕见，体现了良好的方法论意识。\n\n**S3** [R1+R2 共识] **Function-level 等价结论可信且有价值**：5 seeds × 2 model families 的充分支撑，TOST 在 ±1.52pp 仍 reject。\"CWM 在 function-level 并不比 CLS 差\"是一个违反直觉的发现（CWM task difficulty 明显更高），这实际上是论文最有力的结果。\n\n**S4** [R1+R2 共识] **极高的实验透明度**：~8 页附录包含 rank ablation、majority voting、sequence-length ablation、few-shot baseline、per-mutation breakdown、error analysis、TOST sensitivity、variant-level effect sizes、parseable bias analysis 等。几乎所有可预见的 reviewer 问题都有对应的消融实验。Limitations 讨论异常详尽。\n\n**S5** [R1] **Failure mode taxonomy 有实用价值**：§2.2 和 Table 4 的三类 failure mode（format collapse、decision collapse、aggregation penalty）为 practitioners 提供了可操作的 diagnostic framework。\n\n**S6** [R2] **写作质量良好**：全文主线清晰，无 AI 写作痕迹（无 em-dash、无黑名单词汇、段落长度自然），Introduction 5 段叙事结构完整。格式基本合规（8 页正文、`[review]` option、匿名完整、Limitations section 存在、Checklist 逐项填写）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [R1-N1 + R2-N2, CONSENSUS] **Repo-level 核心 claims 基于 single-seed，within-formulation variance 与 between-formulation gap 量级相当**\n\n论文最核心的 repo-level claim（CLS-CWM gap 19-26pp）几乎全部基于 seed 42 的单次实验。Table 10 揭示了 within-formulation 的巨大 seed 方差：DeepSeek CLS per-test accuracy 82.51% (s42) vs 63.51% (s123)，波动 ~19pp；variant-level 81.25% vs 29.17%，波动 >50pp。Within-formulation seed variance (~19pp per-test) 与 between-formulation gap (19-26pp) 量级相当。\n\n§3.7 声称 \"the observed 19-26pp gap exceeds any individual confound by an order of magnitude\"，但 Table 10 数据直接反驳此 claim。论文在 function-level 使用了 3-5 seeds 配合 TOST，展示了良好的统计方法论意识，但在最重要的 repo-level claim 上没有贯彻同标准。Table 3 没有 ±std 或 CI。\n\n**修复方向**：(1) 补充至少 2-3 seeds 的 repo-level 实验并报告 CI；(2) 如资源不允许，将所有 repo-level conclusions 明确标注为 \"preliminary/suggestive under single-seed design\"，修正 §3.7 \"order of magnitude\" 措辞。\n\n**N2** [R1-N2, R2 AGREE] **Checkpoint selection 系统性偏向 CLS**\n\n§3.1 明确说明所有 CWM 运行因 NaN val loss 使用 final-epoch checkpoint，而 CLS 部分使用 val-selected checkpoint。这是影响全部 CWM 运行的系统性偏差，非随机噪声。对一篇以 \"matched conditions\" 为核心方法论贡献的论文，checkpoint selection 不 matched 是核心矛盾。Generation 任务的 overfitting dynamics 与 classification 不同，CWM checkpoint 效应可能 > 论文估计的 ~2pp。偏差方向与 observed effect 一致（CWM 被系统性低估）。\n\n**修复方向**：(1) 修复 CWM val loss 计算使 checkpoint selection 一致；(2) 提供 CLS final-epoch vs val-selected 消融量化 bias；(3) 将此从脚注级 caveat 升级为 §3.7 中的 prominent confound。\n\n**N3** [R1-N4, R2 AGREE] **Oracle ensemble accuracy 数值自相矛盾**\n\n§3.6 报告 \"oracle combination achieves 90.63%\"，Conclusion 报告 \"oracle ensemble: 90.63%\"。但 Appendix H(a) 报告 \"achieves 96.03% accuracy, +3.12pp over 87.51%\"。验证：87.51 + 3.12 = 90.63 ≠ 96.03。正文与附录数字矛盾。Error complementarity 是核心 contribution 之一，数字不一致直接损害可信度。\n\n**修复方向**：核实并统一所有 oracle accuracy 数字。\n\n**N4** [R2-N1, R1 AGREE] **Novelty 有限：核心发现可预期，叙事权重错配**\n\n\"Classification > generation when outputs are complex\"（repo-level CLS 领先 CWM 19-26pp）在概念上可预期：CWM 需精确生成长序列（~477 tokens），错误乘法累积；CLS 只需 1 token。论文的 failure mode taxonomy（format collapse, token exhaustion）本质上是形式化这个直觉，而非挑战它。\n\n更重要的是 claim-evidence 权重错配：论文将 repo-level divergence（可预期 + single-seed + checkpoint confound）作为 headline，而 function-level equivalence（违反直觉 + 统计 robust）在叙事中处于从属地位。\"CWM 在 function-level 并不比 CLS 差\"这一结论实际上更有趣，因为 CWM 的 task difficulty 明显更高。\n\n**修复方向**：重新平衡叙事，将 function-level equivalence 升为核心故事，repo-level divergence 降为 supporting evidence with explicit caveats。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R1-N3, R2 AGREE WITH NUANCE; severity 分歧：R1 critical, R2 should-fix] **SESOI ±2pp 缺乏 domain-grounded justification**\n\n\"±2pp corresponds to ~15 additional errors per 500 predictions\" 是循环论证（restated 含义而非 domain justification）。Lakens (2017) 要求 SESOI 基于 domain knowledge。\"approximately 30% headroom\" 计算有误：(2.0−1.52)/2.0 = 24%。R2 认为 TOST 是辅助证据，function-level equivalence 不依赖 margin 选择，故降为 should-fix。\n\n**修复方向**：从下游应用角度重写 SESOI justification（如 best-of-n pipeline impact）；修正 headroom 计算。\n\n**W2** [R1-W3 + R2-W2, CONSENSUS] **CWM regime qualifier (≤8B LoRA) 在 Abstract/Conclusion 不充分**\n\nAbstract \"generation-based simulation falling below majority baseline\" 无 regime qualifier。Conclusion practical recommendations 同样缺失。读者可能误解为 CWM 在所有场景下都低于 majority baseline。CWM 劣势可能是 capacity artifact（≤8B）而非 formulation 固有限制。\n\n**修复方向**：Abstract/Conclusion 中所有 CWM 劣势 claim 加 \"under ≤8B LoRA fine-tuning\" 限定。\n\n**W3** [R1-W4, R2 AGREE+] **Re-repair negative result (δ=0) 与 diagnostic granularity narrative 矛盾**\n\nRe-repair pilot (Appendix H(j), n=44, p=0.42, effect size δ=0) 是唯一测试 diagnostic value 是否 translates to downstream benefit 的实验，得到 negative result。论文以 \"insufficient sample size (power ~0.3)\" dismiss，但 effect size 本身为零——增加 sample size 不会改变结论方向。这与第四条 contribution \"Diagnostic granularity with configuration-dependent cost\" 直接矛盾。R2 认为此问题 severity 应更高。\n\n**修复方向**：将 diagnostic granularity 从 core contribution 降级为 \"potential advantage pending downstream validation\"。\n\n**W4** [R1-W1, R2 AGREE] **TRAJ 训练配置差异过大，downsample ablation 未控制 label granularity**\n\nTRAJ ~400 instances vs CLS/CWM ~70K，lr 不同，且 downsample ablation 只控制 volume 未控制 granularity（per-test vs variant-level labels），volume-matched ≠ information-matched。\n\n**修复方向**：明确讨论 volume vs granularity 区别。\n\n**W5** [R1-W2, R2 AGREE] **\"Formulation × model × complexity interaction\" 未做形式化统计检验**\n\n论文反复使用此三阶交互表述（Abstract, §1, §3.5, §5），但从未通过 factorial ANOVA 或 mixed-effects model 检验。所有证据是描述性的。在 single-seed repo-level 数据下，三阶交互统计检验甚至不可行。\n\n**修复方向**：降级 \"interaction\" 措辞为 \"observed pattern\"。\n\n**W6** [R2-N3 → R1 rebut to should-fix; severity 分歧] **合成 mutation 数据外部效度未验证**\n\n所有训练/测试数据基于 synthetic mutation operators。R1 认为论文关心 relative ranking 而非 absolute performance，若 distribution shift 是 formulation-agnostic 的则排序有效，故定为 should-fix。R2 认为应为 must-fix。采纳 should-fix，但记录分歧。\n\n**修复方向**：更明确讨论 Andrews/Just 引用的适用范围；如可行在真实 bug 上做 transfer sanity check。\n\n**W7** [R2-W1, R1 AGREE] **Abstract ~120-130 词偏短**\n\n低于 ARR 推荐 150-250 词。缺少问题重要性论述和 function-level equivalence 这个更 surprising 结论。\n\n**修复方向**：扩展至 ~180 词。\n\n**W8** [R2-W3, R1 PARTIAL REBUT] **可能遗漏近期相关工作**\n\nR2 指出 Aletheia (2601.12186), VeRPO (2601.03525), ExecVerify (2603.11226)。R1 要求 R2 说明具体关系——若涉及 formulation comparison 则为重要遗漏，若仅为 general code verification 则已有 60 条引用覆盖度可能足够。待验证。\n\n---\n\n### Minor（不影响接收）\n\n- **M1**: Tables 1-3 缺少次优下划线标记（NLP 标准做法）\n- **M2**: Checklist C4 version numbers 需补全（当前 \"Partially\"）\n- **M3**: Figure 2 bar chart 信息密度偏低，可加 CI 或 per-model breakdown\n- **M4**: 8 条 bib entry 未被 OpenAlex 索引（较新 preprint，不影响引用真实性）\n- **M5**: §3.3 中 function-level 和 repo-level 数据在同段交叉引用易混淆\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 独立提出并在交叉分享中确认：\n\n| Issue | R1 | R2 | Cross-share |\n|-------|----|----|-------------|\n| Single-seed repo-level | N1 (critical) | N2 (critical) | [AGREE] 最高共识 |\n| Checkpoint selection bias | N2 (critical) | — | R2 [AGREE] |\n| Oracle number contradiction | N4 (critical) | — | R2 [AGREE] |\n| Novelty / claim-evidence rebalancing | — | N1 (critical) | R1 [AGREE] direction |\n| CWM regime qualifier | W3 (warning) | W2 (warning) | [AGREE] 独立一致 |\n| Re-repair vs diagnostic value | W4 (warning) | — | R2 [AGREE+] severity 更高 |\n| TRAJ training confound | W1 (warning) | — | R2 [AGREE] |\n| Interaction not formally tested | W2 (warning) | — | R2 [AGREE] |\n| Synthetic data validity | W5 (warning) | N3 (critical) | 分歧：R1 should-fix, R2 must-fix |\n| Abstract 偏短 | — | W1 (warning) | R1 [AGREE] |\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | 分歧性质 |\n|-------|----|----|----------|\n| SESOI justification severity | N3 (critical) | AGREE with nuance → should-fix | R2 认为 TOST 是辅助证据 |\n| Synthetic data severity | W5 (should-fix) | N3 (must-fix) | R1 认为 relative ranking 不受影响 |\n| Missing references (Aletheia etc.) | PARTIAL REBUT | W3 (should-fix) | R1 要求说明具体关系 |\n| Venue fit | REBUT | W5 (should-fix) | R1 引用 EMNLP 近年 code 论文 |\n\n---\n\n## Questions for Authors\n\n1. [R1-Q1] Table 10 中 DeepSeek CLS 19pp seed variance 中 preprocessing vs checkpoint vs random seed 各贡献多少？\n2. [R1-Q2] bf16-only TOST p-value 是多少？如果 p>0.05，equivalence claim 需重新 qualify。\n3. [R1-Q3] Repo-level ICC=0.3146 对应 DEFF=114.4，effective n≈86。Repo-level CLS-CWM 的 clustered bootstrap 95% CI？\n4. [R1-Q4] CWM unparseable 默认改为 FAIL 或 random 50/50 时 accuracy 如何变化？\n5. [R2-Q1] CWM 原始论文 (Meta FAIR, 32B) 在 repo-level 的表现如何？是否有证据支持 CWM 劣势是 capacity-limited？\n6. [R2-Q2] 论文声称 error complementarity motivates \"complexity-aware routing\"——是否有 preliminary 验证？\n\n---\n\n## Missing References\n\n- CWM 原始论文 (FAIR, 32B) 的 benchmark 结果需在 Related Work 中更详细对比（R1）\n- Aletheia (2601.12186), VeRPO (2601.03525), ExecVerify (2603.11226) — 待验证相关性（R2，R1 部分反驳）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，无外部审稿结果。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5（Findings）— 两位 Reviewer 一致**\n\n**EMNLP 2026 ARR 评分对应**：3.0 = Findings（可被 Findings 接收）\n\n**核心判断**：\n\n论文填补了一个真实的文献空白（execution-free verification formulation 的系统比较），统计方法论和实验透明度超越 NLP 常见标准。Function-level equivalence 结论有 5 seeds × 2 model families 的充分支撑，是论文最 robust 的发现。\n\n但论文存在四个互相关联的核心问题：(1) repo-level claims 基于 single-seed，within-formulation variance 与 between-formulation gap 量级相当；(2) checkpoint selection 系统性偏向 CLS；(3) 核心发现（classification > generation at repo-level）在概念上可预期，novelty 主要在 methodology 而非 insight；(4) oracle ensemble 数字矛盾。这些问题共同将论文定位在 Findings 而非主会议。\n\n**如果修复**：补充多 seed repo-level 实验（N1）、修复 checkpoint 一致性或量化 bias（N2）、统一 oracle 数字（N3）、重新平衡叙事以 function-level equivalence 为核心（N4），论文有潜力提升到 3.5 (Borderline Conference)。但补充 repo-level 多 seed 实验需要额外计算资源和时间，在 ARR May deadline (5/25) 前可能不可行。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- ~120-130 词偏短（ARR 推荐 150-250）\n- \"generation-based simulation falling below majority baseline\" 缺 regime qualifier (≤8B LoRA)\n- 缺少问题重要性动机和 function-level equivalence 的突出\n- 建议扩展至 ~180 词\n\n### Introduction\n- 5 段叙事结构完整，逻辑清晰\n- \"formulation × model × complexity interaction\" 未经统计检验，建议降级为 \"observed pattern\"\n- 第四条 contribution (diagnostic granularity) 与 re-repair negative result (δ=0) 矛盾，需降级或加 caveat\n\n### Method (§2)\n- Formulation 定义清晰，§2.2 failure mode taxonomy 有价值\n- §2.3 Oracle framework 的 κ 中 n 定义不明确\n\n### Experiments (§3)\n- §3.1 Setup 文档化充分\n- §3.2 Function-level 结论 robust（5 seeds, TOST, 2 model families）\n- §3.3 Scaling 结论受限于 2 seeds（42, 123），但 direction 一致\n- §3.4 TOST equivalence: SESOI justification 需加强，headroom 计算有误\n- §3.5 Repo-level: **最弱环节**——single-seed, checkpoint confound, high within-formulation variance\n- §3.6 Analysis: oracle 数字矛盾必须修复；re-repair negative result 需更平衡呈现\n- §3.7 Threats: \"order of magnitude\" 表述被 Table 10 反驳\n\n### Related Work (§4)\n- 三段结构清晰，归纳优于列举\n- Process vs outcome supervision 的 NLP 框架连接有价值\n- 引用覆盖基本充分（60 条），但可能遗漏若干近期工作（待验证）\n\n### Conclusion (§5)\n- CWM 劣势 claim 需加 regime qualifier\n- Practical recommendations 过于 definitive given single-seed repo-level evidence\n\n### Appendices\n- 极其详尽（A-N, ~8 页），覆盖几乎所有 reviewer 可能的疑问\n- Appendix H(a) oracle 数字需修正\n- Appendix M Threats 讨论 \"order of magnitude\" 需修正\n\n### Checklist\n- 逐项认真填写，C4 需补全 version numbers\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "report": "# 审稿报告 — Round 6 (Fresh Review)\n\n**论文**: The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 写作完整性 + 格式合规）\n**Overall**: 3.0 / 5（Findings）— 两位 Reviewer 一致\n**Confidence**: 4 / 5 — 两位 Reviewer 一致\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free code verification formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹评分），在两个模型家族（Qwen3-4B/8B、DeepSeek-Coder-6.7B）、两个复杂度级别（function-level、repo-level）、多 seed 条件下进行匹配实验。核心发现：function-level 三者近等价（TOST p=0.007, 5 seeds），repo-level CLS 领先 CWM 19-26pp（≤8B LoRA regime）。论文还提供了 failure mode taxonomy、error complementarity 分析和 oracle framework。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **填补真实文献空白**：首个在 matched conditions 下系统比较三种 execution-free verification formulations 的工作，研究问题定义清晰且有实际价值。\n\n**S2** [R1+R2 共识] **统计方法论超越 NLP 常见标准**：TOST equivalence testing（而非仅用 p-value 证明差异不显著）、clustered bootstrap（114 clusters, 10K resamples）、ICC with design effect、Holm-Bonferroni correction (k=4) 的组合在 NLP 实证论文中罕见，体现了良好的方法论意识。\n\n**S3** [R1+R2 共识] **Function-level 等价结论可信且有价值**：5 seeds × 2 model families 的充分支撑，TOST 在 ±1.52pp 仍 reject。\"CWM 在 function-level 并不比 CLS 差\"是一个违反直觉的发现（CWM task difficulty 明显更高），这实际上是论文最有力的结果。\n\n**S4** [R1+R2 共识] **极高的实验透明度**：~8 页附录包含 rank ablation、majority voting、sequence-length ablation、few-shot baseline、per-mutation breakdown、error analysis、TOST sensitivity、variant-level effect sizes、parseable bias analysis 等。几乎所有可预见的 reviewer 问题都有对应的消融实验。Limitations 讨论异常详尽。\n\n**S5** [R1] **Failure mode taxonomy 有实用价值**：§2.2 和 Table 4 的三类 failure mode（format collapse、decision collapse、aggregation penalty）为 practitioners 提供了可操作的 diagnostic framework。\n\n**S6** [R2] **写作质量良好**：全文主线清晰，无 AI 写作痕迹（无 em-dash、无黑名单词汇、段落长度自然），Introduction 5 段叙事结构完整。格式基本合规（8 页正文、`[review]` option、匿名完整、Limitations section 存在、Checklist 逐项填写）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [R1-N1 + R2-N2, CONSENSUS] **Repo-level 核心 claims 基于 single-seed，within-formulation variance 与 between-formulation gap 量级相当**\n\n论文最核心的 repo-level claim（CLS-CWM gap 19-26pp）几乎全部基于 seed 42 的单次实验。Table 10 揭示了 within-formulation 的巨大 seed 方差：DeepSeek CLS per-test accuracy 82.51% (s42) vs 63.51% (s123)，波动 ~19pp；variant-level 81.25% vs 29.17%，波动 >50pp。Within-formulation seed variance (~19pp per-test) 与 between-formulation gap (19-26pp) 量级相当。\n\n§3.7 声称 \"the observed 19-26pp gap exceeds any individual confound by an order of magnitude\"，但 Table 10 数据直接反驳此 claim。论文在 function-level 使用了 3-5 seeds 配合 TOST，展示了良好的统计方法论意识，但在最重要的 repo-level claim 上没有贯彻同标准。Table 3 没有 ±std 或 CI。\n\n**修复方向**：(1) 补充至少 2-3 seeds 的 repo-level 实验并报告 CI；(2) 如资源不允许，将所有 repo-level conclusions 明确标注为 \"preliminary/suggestive under single-seed design\"，修正 §3.7 \"order of magnitude\" 措辞。\n\n**N2** [R1-N2, R2 AGREE] **Checkpoint selection 系统性偏向 CLS**\n\n§3.1 明确说明所有 CWM 运行因 NaN val loss 使用 final-epoch checkpoint，而 CLS 部分使用 val-selected checkpoint。这是影响全部 CWM 运行的系统性偏差，非随机噪声。对一篇以 \"matched conditions\" 为核心方法论贡献的论文，checkpoint selection 不 matched 是核心矛盾。Generation 任务的 overfitting dynamics 与 classification 不同，CWM checkpoint 效应可能 > 论文估计的 ~2pp。偏差方向与 observed effect 一致（CWM 被系统性低估）。\n\n**修复方向**：(1) 修复 CWM val loss 计算使 checkpoint selection 一致；(2) 提供 CLS final-epoch vs val-selected 消融量化 bias；(3) 将此从脚注级 caveat 升级为 §3.7 中的 prominent confound。\n\n**N3** [R1-N4, R2 AGREE] **Oracle ensemble accuracy 数值自相矛盾**\n\n§3.6 报告 \"oracle combination achieves 90.63%\"，Conclusion 报告 \"oracle ensemble: 90.63%\"。但 Appendix H(a) 报告 \"achieves 96.03% accuracy, +3.12pp over 87.51%\"。验证：87.51 + 3.12 = 90.63 ≠ 96.03。正文与附录数字矛盾。Error complementarity 是核心 contribution 之一，数字不一致直接损害可信度。\n\n**修复方向**：核实并统一所有 oracle accuracy 数字。\n\n**N4** [R2-N1, R1 AGREE] **Novelty 有限：核心发现可预期，叙事权重错配**\n\n\"Classification > generation when outputs are complex\"（repo-level CLS 领先 CWM 19-26pp）在概念上可预期：CWM 需精确生成长序列（~477 tokens），错误乘法累积；CLS 只需 1 token。论文的 failure mode taxonomy（format collapse, token exhaustion）本质上是形式化这个直觉，而非挑战它。\n\n更重要的是 claim-evidence 权重错配：论文将 repo-level divergence（可预期 + single-seed + checkpoint confound）作为 headline，而 function-level equivalence（违反直觉 + 统计 robust）在叙事中处于从属地位。\"CWM 在 function-level 并不比 CLS 差\"这一结论实际上更有趣，因为 CWM 的 task difficulty 明显更高。\n\n**修复方向**：重新平衡叙事，将 function-level equivalence 升为核心故事，repo-level divergence 降为 supporting evidence with explicit caveats。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R1-N3, R2 AGREE WITH NUANCE; severity 分歧：R1 critical, R2 should-fix] **SESOI ±2pp 缺乏 domain-grounded justification**\n\n\"±2pp corresponds to ~15 additional errors per 500 predictions\" 是循环论证（restated 含义而非 domain justification）。Lakens (2017) 要求 SESOI 基于 domain knowledge。\"approximately 30% headroom\" 计算有误：(2.0−1.52)/2.0 = 24%。R2 认为 TOST 是辅助证据，function-level equivalence 不依赖 margin 选择，故降为 should-fix。\n\n**修复方向**：从下游应用角度重写 SESOI justification（如 best-of-n pipeline impact）；修正 headroom 计算。\n\n**W2** [R1-W3 + R2-W2, CONSENSUS] **CWM regime qualifier (≤8B LoRA) 在 Abstract/Conclusion 不充分**\n\nAbstract \"generation-based simulation falling below majority baseline\" 无 regime qualifier。Conclusion practical recommendations 同样缺失。读者可能误解为 CWM 在所有场景下都低于 majority baseline。CWM 劣势可能是 capacity artifact（≤8B）而非 formulation 固有限制。\n\n**修复方向**：Abstract/Conclusion 中所有 CWM 劣势 claim 加 \"under ≤8B LoRA fine-tuning\" 限定。\n\n**W3** [R1-W4, R2 AGREE+] **Re-repair negative result (δ=0) 与 diagnostic granularity narrative 矛盾**\n\nRe-repair pilot (Appendix H(j), n=44, p=0.42, effect size δ=0) 是唯一测试 diagnostic value 是否 translates to downstream benefit 的实验，得到 negative result。论文以 \"insufficient sample size (power ~0.3)\" dismiss，但 effect size 本身为零——增加 sample size 不会改变结论方向。这与第四条 contribution \"Diagnostic granularity with configuration-dependent cost\" 直接矛盾。R2 认为此问题 severity 应更高。\n\n**修复方向**：将 diagnostic granularity 从 core contribution 降级为 \"potential advantage pending downstream validation\"。\n\n**W4** [R1-W1, R2 AGREE] **TRAJ 训练配置差异过大，downsample ablation 未控制 label granularity**\n\nTRAJ ~400 instances vs CLS/CWM ~70K，lr 不同，且 downsample ablation 只控制 volume 未控制 granularity（per-test vs variant-level labels），volume-matched ≠ information-matched。\n\n**修复方向**：明确讨论 volume vs granularity 区别。\n\n**W5** [R1-W2, R2 AGREE] **\"Formulation × model × complexity interaction\" 未做形式化统计检验**\n\n论文反复使用此三阶交互表述（Abstract, §1, §3.5, §5），但从未通过 factorial ANOVA 或 mixed-effects model 检验。所有证据是描述性的。在 single-seed repo-level 数据下，三阶交互统计检验甚至不可行。\n\n**修复方向**：降级 \"interaction\" 措辞为 \"observed pattern\"。\n\n**W6** [R2-N3 → R1 rebut to should-fix; severity 分歧] **合成 mutation 数据外部效度未验证**\n\n所有训练/测试数据基于 synthetic mutation operators。R1 认为论文关心 relative ranking 而非 absolute performance，若 distribution shift 是 formulation-agnostic 的则排序有效，故定为 should-fix。R2 认为应为 must-fix。采纳 should-fix，但记录分歧。\n\n**修复方向**：更明确讨论 Andrews/Just 引用的适用范围；如可行在真实 bug 上做 transfer sanity check。\n\n**W7** [R2-W1, R1 AGREE] **Abstract ~120-130 词偏短**\n\n低于 ARR 推荐 150-250 词。缺少问题重要性论述和 function-level equivalence 这个更 surprising 结论。\n\n**修复方向**：扩展至 ~180 词。\n\n**W8** [R2-W3, R1 PARTIAL REBUT] **可能遗漏近期相关工作**\n\nR2 指出 Aletheia (2601.12186), VeRPO (2601.03525), ExecVerify (2603.11226)。R1 要求 R2 说明具体关系——若涉及 formulation comparison 则为重要遗漏，若仅为 general code verification 则已有 60 条引用覆盖度可能足够。待验证。\n\n---\n\n### Minor（不影响接收）\n\n- **M1**: Tables 1-3 缺少次优下划线标记（NLP 标准做法）\n- **M2**: Checklist C4 version numbers 需补全（当前 \"Partially\"）\n- **M3**: Figure 2 bar chart 信息密度偏低，可加 CI 或 per-model breakdown\n- **M4**: 8 条 bib entry 未被 OpenAlex 索引（较新 preprint，不影响引用真实性）\n- **M5**: §3.3 中 function-level 和 repo-level 数据在同段交叉引用易混淆\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 独立提出并在交叉分享中确认：\n\n| Issue | R1 | R2 | Cross-share |\n|-------|----|----|-------------|\n| Single-seed repo-level | N1 (critical) | N2 (critical) | [AGREE] 最高共识 |\n| Checkpoint selection bias | N2 (critical) | — | R2 [AGREE] |\n| Oracle number contradiction | N4 (critical) | — | R2 [AGREE] |\n| Novelty / claim-evidence rebalancing | — | N1 (critical) | R1 [AGREE] direction |\n| CWM regime qualifier | W3 (warning) | W2 (warning) | [AGREE] 独立一致 |\n| Re-repair vs diagnostic value | W4 (warning) | — | R2 [AGREE+] severity 更高 |\n| TRAJ training confound | W1 (warning) | — | R2 [AGREE] |\n| Interaction not formally tested | W2 (warning) | — | R2 [AGREE] |\n| Synthetic data validity | W5 (warning) | N3 (critical) | 分歧：R1 should-fix, R2 must-fix |\n| Abstract 偏短 | — | W1 (warning) | R1 [AGREE] |\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | 分歧性质 |\n|-------|----|----|----------|\n| SESOI justification severity | N3 (critical) | AGREE with nuance → should-fix | R2 认为 TOST 是辅助证据 |\n| Synthetic data severity | W5 (should-fix) | N3 (must-fix) | R1 认为 relative ranking 不受影响 |\n| Missing references (Aletheia etc.) | PARTIAL REBUT | W3 (should-fix) | R1 要求说明具体关系 |\n| Venue fit | REBUT | W5 (should-fix) | R1 引用 EMNLP 近年 code 论文 |\n\n---\n\n## Questions for Authors\n\n1. [R1-Q1] Table 10 中 DeepSeek CLS 19pp seed variance 中 preprocessing vs checkpoint vs random seed 各贡献多少？\n2. [R1-Q2] bf16-only TOST p-value 是多少？如果 p>0.05，equivalence claim 需重新 qualify。\n3. [R1-Q3] Repo-level ICC=0.3146 对应 DEFF=114.4，effective n≈86。Repo-level CLS-CWM 的 clustered bootstrap 95% CI？\n4. [R1-Q4] CWM unparseable 默认改为 FAIL 或 random 50/50 时 accuracy 如何变化？\n5. [R2-Q1] CWM 原始论文 (Meta FAIR, 32B) 在 repo-level 的表现如何？是否有证据支持 CWM 劣势是 capacity-limited？\n6. [R2-Q2] 论文声称 error complementarity motivates \"complexity-aware routing\"——是否有 preliminary 验证？\n\n---\n\n## Missing References\n\n- CWM 原始论文 (FAIR, 32B) 的 benchmark 结果需在 Related Work 中更详细对比（R1）\n- Aletheia (2601.12186), VeRPO (2601.03525), ExecVerify (2603.11226) — 待验证相关性（R2，R1 部分反驳）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，无外部审稿结果。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5（Findings）— 两位 Reviewer 一致**\n\n**EMNLP 2026 ARR 评分对应**：3.0 = Findings（可被 Findings 接收）\n\n**核心判断**：\n\n论文填补了一个真实的文献空白（execution-free verification formulation 的系统比较），统计方法论和实验透明度超越 NLP 常见标准。Function-level equivalence 结论有 5 seeds × 2 model families 的充分支撑，是论文最 robust 的发现。\n\n但论文存在四个互相关联的核心问题：(1) repo-level claims 基于 single-seed，within-formulation variance 与 between-formulation gap 量级相当；(2) checkpoint selection 系统性偏向 CLS；(3) 核心发现（classification > generation at repo-level）在概念上可预期，novelty 主要在 methodology 而非 insight；(4) oracle ensemble 数字矛盾。这些问题共同将论文定位在 Findings 而非主会议。\n\n**如果修复**：补充多 seed repo-level 实验（N1）、修复 checkpoint 一致性或量化 bias（N2）、统一 oracle 数字（N3）、重新平衡叙事以 function-level equivalence 为核心（N4），论文有潜力提升到 3.5 (Borderline Conference)。但补充 repo-level 多 seed 实验需要额外计算资源和时间，在 ARR May deadline (5/25) 前可能不可行。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- ~120-130 词偏短（ARR 推荐 150-250）\n- \"generation-based simulation falling below majority baseline\" 缺 regime qualifier (≤8B LoRA)\n- 缺少问题重要性动机和 function-level equivalence 的突出\n- 建议扩展至 ~180 词\n\n### Introduction\n- 5 段叙事结构完整，逻辑清晰\n- \"formulation × model × complexity interaction\" 未经统计检验，建议降级为 \"observed pattern\"\n- 第四条 contribution (diagnostic granularity) 与 re-repair negative result (δ=0) 矛盾，需降级或加 caveat\n\n### Method (§2)\n- Formulation 定义清晰，§2.2 failure mode taxonomy 有价值\n- §2.3 Oracle framework 的 κ 中 n 定义不明确\n\n### Experiments (§3)\n- §3.1 Setup 文档化充分\n- §3.2 Function-level 结论 robust（5 seeds, TOST, 2 model families）\n- §3.3 Scaling 结论受限于 2 seeds（42, 123），但 direction 一致\n- §3.4 TOST equivalence: SESOI justification 需加强，headroom 计算有误\n- §3.5 Repo-level: **最弱环节**——single-seed, checkpoint confound, high within-formulation variance\n- §3.6 Analysis: oracle 数字矛盾必须修复；re-repair negative result 需更平衡呈现\n- §3.7 Threats: \"order of magnitude\" 表述被 Table 10 反驳\n\n### Related Work (§4)\n- 三段结构清晰，归纳优于列举\n- Process vs outcome supervision 的 NLP 框架连接有价值\n- 引用覆盖基本充分（60 条），但可能遗漏若干近期工作（待验证）\n\n### Conclusion (§5)\n- CWM 劣势 claim 需加 regime qualifier\n- Practical recommendations 过于 definitive given single-seed repo-level evidence\n\n### Appendices\n- 极其详尽（A-N, ~8 页），覆盖几乎所有 reviewer 可能的疑问\n- Appendix H(a) oracle 数字需修正\n- Appendix M Threats 讨论 \"order of magnitude\" 需修正\n\n### Checklist\n- 逐项认真填写，C4 需补全 version numbers\n"
  }
}
```

</details>

---


### Tool result

_source line 542 · 2026-05-19T11:21:57.829997+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4321
}
```

</details>

---


### Assistant

_source line 543 · 2026-05-19T11:22:10.922716+00:00_

审稿报告已投递至 Research Director。

**Round 6 审稿结果汇总**：

**Overall: 3.0 / 5 (Findings)** — 两位 Reviewer 一致，Confidence 4/5。

**4 个 Must-Fix（共识）**：
1. **Single-seed repo-level** — within-CLS seed variance (~19pp) 与 CLS-CWM gap (19-26pp) 量级相当，§3.7 "order of magnitude" 被 Table 10 反驳
2. **Checkpoint selection bias** — 全部 CWM 使用 final-epoch（NaN val loss），CLS 使用 val-selected，系统性偏向 CLS
3. **Oracle 数字矛盾** — §3.6 报 90.63%，Appendix H(a) 报 96.03%，87.51+3.12=90.63≠96.03
4. **Novelty/叙事错配** — repo-level 核心发现可预期，应将 function-level equivalence（违反直觉且 robust）升为 headline

**8 个 Should-Fix**：SESOI 循环论证、CWM regime qualifier 缺失、re-repair δ=0 与 diagnostic value 矛盾、TRAJ 训练配置不可比、交互未形式检验、合成数据效度、Abstract 偏短、可能遗漏相关工作

**主要优势**：matched comparison framework、统计方法论超越 NLP 标准、function-level equivalence 可信、附录透明度极高、写作质量良好无 AI 痕迹

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 544 · 2026-05-19T11:22:13.478497+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

逐条总结：
- **R1-N1 (single-seed variance)**: [AGREE] — Table 10 的 within-formulation 19pp variance 与 between-formulation 19-26pp gap 同量级，直接反驳 §3.7 的 claim
- **R1-N2 (checkpoint bias)**: [AGREE] — CWM 全部使用 final-epoch checkpoint vs CLS val-selected，系统性偏差
- **R1-N3 (SESOI 循环)**: [AGREE with nuance] — 技术批评准确但不应升至 critical，因 function-level 等价不依赖 TOST margin 选择
- **R1-N4 (oracle 数值矛盾)**: [AGREE] — 87.51 + 3.12 = 90.63 ≠ 96.03，确凿的数据错误
- **R1-W1 到 R1-W5**: 全部 [AGREE]，其中 R1-W4 (re-repair δ=0) 我认为比 R1 给予的 severity 更高

两位 Reviewer 在 single-seed repo-level 和 synthetic data gap 上独立达成一致。我维持 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 545 · 2026-05-19T11:22:27.816414+00:00_

审稿报告已提交至 Research Director。R2 的交叉回应与报告中的共识判断完全一致，无需补充修订。

**Round 6 审稿完成。**

核心结论：
- **Overall: 3.0 (Findings)**，两人一致，Confidence 4/5
- **4 个 Must-Fix**：(1) single-seed repo-level + within-formulation variance 同量级（最高共识），(2) checkpoint selection 系统性偏向 CLS，(3) oracle 数字矛盾 90.63% vs 96.03%，(4) novelty 有限 + 叙事权重错配
- **8 个 Should-Fix**：SESOI 循环论证、CWM regime qualifier 缺失、re-repair δ=0 vs diagnostic value 矛盾、TRAJ 训练配置差异、交互效应未检验、合成数据外部效度、Abstract 偏短、可能遗漏相关工作
- **提升路径**：补充多 seed repo-level 实验 + 修复 checkpoint 一致性 + 统一 oracle 数字 + 重新平衡叙事以 function-level equivalence 为核心 → 有潜力升至 3.5 (Borderline Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 50

## Round 50

48 recorded events


### User

_source line 546 · 2026-05-22T13:38:45.220247+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings unified)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 547 · 2026-05-22T13:38:50.792538+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 548 · 2026-05-22T13:38:50.843590+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 549 · 2026-05-22T13:38:57.117500+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 550 · 2026-05-22T13:38:57.117971+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 551 · 2026-05-22T13:39:00.029427+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-22T13:39:00.531565+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 553 · 2026-05-22T13:39:00.732812+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (252 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s123-eval-1epoch | Eval DeepSeek CWM repo-level s123 1-epoch checkpoint (checkpoint-4209)。验证 appendix cwm_convergence 中引用的 early-stopping 数据 (75.45% acc / 66.4% unparseable) 是否在干净 eval 下可复现。 | — | — | — |\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- 
…[truncated 1818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 703
}
```

</details>

---


### Tool result

_source line 554 · 2026-05-22T13:39:00.733185+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 555 · 2026-05-22T13:39:06.638382+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines",
  "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines",
    "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-22T13:39:08.550453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-22T13:39:09.052694+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\graphicspath{{../../artifacts/}}
21	
22	% Lists
23	\usepackage{enumitem}
24	
25	% Custom commands
26	\newcommand{\cls}{\textsc{Cls}}
27	\newcommand{\cwm}{\textsc{Cwm}}
28	\newcommand{\traj}{\textsc{Traj}}
29	\newcommand{\fone}{F\textsubscript{1}}
30	\newcommand{\pp}{\,\text{pp}}
31	\newcommand{\tbd}{\textsc{tbd}}
32	
33	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Systematic Empirical Study}
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\input{abstract}
40	
41	\input{introduction}
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
46	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
47	\label{fig:reformulation}
48	\end{figure*}
49	
50	\input{method}
51	
52	\input{experiments}
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
57	\caption{Gap amplification from function to repo level. At function level, the \cls{}--\cwm{} gap is 1--3\pp{}; at repo level, it widens to 18--26\pp{} with \cwm{} falling below majority baseline.}
58	\label{fig:scaling_gap}
59	\end{figure}
60	
61	
62	\input{related_work}
63	
64	\input{c
…[truncated 118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-22T13:39:09.555041+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "report.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 559 · 2026-05-22T13:39:10.057138+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 560 · 2026-05-22T13:39:17.987045+00:00_

Web search results for query: "EMNLP 2026 ACL Rolling Review call for papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026's submission guidelines using ACL Rolling Review:

## Review Process

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference.

## Two-Step Sub
…[truncated 1071 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 11348
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-22T13:39:17.987681+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| deepseek-cwm-repo-s123-eval-1epoch | Eval DeepSeek CWM repo-level s123 1-epoch checkpoint (checkpoint-4209)。验证 appendix cwm_convergence 中引用的 early-stopping 数据 (75.45% acc / 66.4% unparseable) 是否在干净 eval 下可复现。 | — | — | — |\\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\\n\\n## 待处理\\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\\n- qwen_cwm_s456_resume2（准备中）\\n- qwen_cwm_s456_resume（准备中）\\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\\n- D131-cwm-s42-epoch3-seq2048（准备中）\\n- D133-cwm-s42-e2-seq2048-home-resume（准备中）\\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\\n- deepseek-cls-repo-resume-v3: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633. Fixed: removed unrecognized --save_steps arg.（准备中）\\n- …另有 8 项\\n\\n## 近期结论\\n- **qwen3-8b-cwm-repo-s456-eval** (success): Eval Qwen3-8B CWM repo-level s456 checkpoint-6633。与 s42/s123 对比验证 CWM repo-level 跨 seed 一致性，组成 3-seed coverage 用于论文 Table 3。 ← 基于 qwen3
…[truncated 1405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8432
}
```

</details>

---


### Tool result

_source line 562 · 2026-05-22T13:39:18.038267+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 7981
}
```

</details>

---


### Tool call

_source line 563 · 2026-05-22T13:39:26.119153+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers page limit format requirements ARR submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers page limit format requirements ARR submission"
  }
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-22T13:39:26.119576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-22T13:39:26.571647+00:00_

1	# === Round 6 Issues ===
2	
3	# --- Round 6 Must-Fix (Consensus Critical) ---
4	
5	- id: "R6-N1"
6	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
7	  category: experiment
8	  severity: critical
9	  status: in_progress
10	  first_raised_round: 6
11	  last_seen_round: 7
12	  mentions:
13	    - round: 6
14	      reviewers: [1, 2]
15	      note: "两人独立提出，最高共识。"
16	    - round: 7
17	      reviewers: [pre-review]
18	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress. Blocked on CWM data (~May 22-23)."
19	  action_items:
20	    - round: 6
21	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
22	      assigned_to: "paper"
23	      status: in_progress
24	  resolution: "CLS 3-seed ✅, TRAJ 3-seed ✅. CWM training: DeepSeek s123-v2 ~May 21 09:30, Qwen s123+s456 ~May 22 22:00."
25	  resolution_round: null
26	
27	- id: "R6-N2"
28	  summary: "Checkpoint selection 系统性偏向 CLS"
29	  category: method
30	  severity: critical
31	  status: resolved
32	  first_raised_round: 6
33	  last_seen_round: 7
34	  mentions:
35	    - round: 6
36	      reviewers: [1, 2]
37	      note: "系统性偏差方向与 observed effect 一致。"
38	    - round: 7
39	      reviewers: [pre-review]
40	      note: "Reviewer 确认修复充分。"
41	  action_items:
42	    - round: 6
43	      action: "CLS epoch ablation + matched epoch-3 解释"
44	      assigned_to: "paper"
45	      status: resolved
46	  resolution: "CLS epoch ablation <1pp range. Matched epoch-3 cross-model gap ~2pp. Written in §4.4."
47	  resolution_round: 7
48	
49	- id: "R6-N3"
50	  summary: "Oracle ensemble accuracy 数值矛盾"
51	  category: experiment
52	  severity: critical
53	  status: resolved
54	  first_raised_round: 6
55	  last_seen_round: 6
56	  action_items:
57	    - round: 6
58	      action: "核实并统一数字"
59	      assigned_to: "paper"
60	      status: resolved
61	  resolution: "Oracle 90.63% 验证正确。96.03% 已删除。Error direction 6 处修正。"
62	  resolution_round: 7
63	
64	- id: "R6-
…[truncated 7713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-22T13:39:26.622308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-22T13:39:26.773290+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly relies on generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is model-dependent. At repository level, a significant interaction ($z{=}-23.7$) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 18--26\pp{} across 3 seeds per model in variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-22T13:39:26.773739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-22T13:39:26.824330+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimenta
…[truncated 2613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-22T13:39:32.646629+00:00_

Web search results for query: "EMNLP 2026 call for papers page limit format requirements ARR submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here is the information about EMNLP 2026 call for papers page limit and format requirements for ARR submissions:

## Page Limit

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Format Requirements

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

The mandatory Limitations section 
…[truncated 739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 6527
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-22T13:39:38.520463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 572 · 2026-05-22T13:39:39.323730+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation
…[truncated 3353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 573 · 2026-05-22T13:39:39.474754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 574 · 2026-05-22T13:39:39.826766+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, which defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Mo
…[truncated 20895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-22T13:39:39.827313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-22T13:39:40.078653+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; our work extends this direction to repo-level repair verification. Verification formulations span trajectory-level reward~\cite{shum2025swerm,zhu2026codescaler}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. Our \cls{} provides per-test (process) supervision while \traj{} provides outcome-level; the PRM literature compares supervision granularity given a fixed output format, while we additionally vary the output format (\cwm{} generation vs.\ \cls{} classification).
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{li2022alphacode,alphacode2023team}, and Reflexion~\cite{shinn2023
…[truncated 1050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-22T13:39:40.079067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-22T13:39:40.129594+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} reaches parity on Qwen3 but not DeepSeek-Coder (2.69\pp{}). Per-test classification achieves 217$\times$ higher throughput while providing diagnostic signal whose downstream utility remains unconfirmed ($n{=}44$, $p{=}0.42$). Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA fine-tuning, a significant interaction ($z{=}-23.7$) confirms divergence (18--26\pp{}, confirmed across 3 seeds per model, variant-level), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). Variant-level analysis reveals three distinct failure modes (format collapse, decision collapse, aggregation penalty) consistent across model families. At function level, formulation choice is immaterial; at repository level under ${\leq}$8B LoRA, \cls{} is recommended for both accuracy and throughput.
5	
6	Three directions follow. First, oracle gains (90.63\%/95.83\%) motivate complexity-aware routing among formulations; the failure mode taxonomy (\S\ref{sec:repo}) provides candidate routing features. Second, the generation bottleneck is semantic---four syntactic interventions fail (Appendix~\ref{app:extended_analysis}(g))---suggesting that closing the gap requires capacity scaling or execution trace pretraining~\cite{meta2025cwm}; testing at 32B+ scale would resolve the primary open question. Third, larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether the 217$\times$ throughput advantage of \cls{} extends beyond verification to repair pipelines.
7	
8	\section*{Limitations}
9	
10	Repo-level \cwm{} uses 3 seeds p
…[truncated 850 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 579 · 2026-05-22T13:39:45.049402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 580 · 2026-05-22T13:39:45.100163+00:00_

1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: limited seed coverage for repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and seed coverage.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified 
…[truncated 4347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-22T13:39:45.100647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-22T13:39:45.402519+00:00_

1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlat
…[truncated 48824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-22T13:39:53.886167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 584 · 2026-05-22T13:39:55.041728+00:00_

1	% === Execution Simulation ===
2	
3	@inproceedings{gu2024cruxeval,
4	  title={{CRUXEval}: A Benchmark for Code Reasoning, Understanding and Execution},
5	  author={Gu, Alex and Rozi{\`e}re, Baptiste and Leather, Hugh and Solar-Lezama, Armando and Synnaeve, Gabriel and Wang, Sida I.},
6	  booktitle={Proceedings of the 41st International Conference on Machine Learning},
7	  pages={16568--16621},
8	  year={2024}
9	}
10	
11	@article{maimon2026selfexecution,
12	  title={Self-Execution Simulation Improves Coding Models},
13	  author={Maimon, Gallil and Yoran, Ori and Kreuk, Felix and Hassid, Michael and Cohen, Gal and Chambon, Pierre and Adi, Yossi},
14	  journal={arXiv preprint arXiv:2604.03253},
15	  year={2026}
16	}
17	
18	@article{meta2025cwm,
19	  title={{CWM}: An Open-Weights {LLM} for Research on Code Generation with World Models},
20	  author={{FAIR CodeGen team} and Copet, Jade and Carbonneaux, Quentin and Cohen, Gal and Gehring, Jonas and Kahn, Jacob and Kossen, Jannik and Kreuk, Felix and McMilin, Emily and Meyer, Michel and Wei, Yuxiang and Zhang, David and Zheng, Kunhao and others},
21	  journal={arXiv preprint arXiv:2510.02387},
22	  year={2025}
23	}
24	
25	@article{liu2024codemind,
26	  title={{CodeMind}: A Framework to Challenge Large Language Models for Code Reasoning},
27	  author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh},
28	  journal={arXiv preprint arXiv:2402.09664},
29	  year={2024}
30	}
31	
32	@article{abdollahi2025demystifying,
33	  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},
34	  author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi},
35	  journal={arXiv preprint arXiv:2512.00215},
36	  year={2025}
37	}
38	
39	@article{venkatkrishna2026aletheia,
40	  title={Aletheia: What Makes {RLVR} For Code Verifiers Tick?},
41	  author={Venkatkrishna, Vatsal and Paul, Indranei
…[truncated 18797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-22T13:39:55.042249+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_6/submitted.pdf 2>/dev/null; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf 2>/dev/null",
  "description": "Check PDF file existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_6/submitted.pdf 2>/dev/null; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf 2>/dev/null",
    "description": "Check PDF file existence"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-22T13:39:55.243278+00:00_

-rw-r--r-- 1 ubuntu ubuntu 419746 May 22 13:35 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_6/submitted.pdf
-rw-r--r-- 1 ubuntu ubuntu 419746 May 22 13:35 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-22T13:40:22.160655+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 588 · 2026-05-22T13:40:40.163220+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18002
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-22T13:40:40.365320+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n- 路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（各 section 为独立 .tex 文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_6/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR May cycle)\n- Deadline: 2026-05-25\n- 正文限制: Long paper 8 页（不含 references 和 limitations）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind（作者匿名）\n- Limitations section: mandatory，不计入页数\n- Appendix: 允许，参与审稿\n- Overall Assessment 评分标准: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**重点审查以下维度（必须逐项给出判断）**：\n\n1. **统计方法论**: TOST 等价检验（±2pp margin 是否合理）、clustered bootstrap 设计（114 clusters, 10K resamples）、mixed-effects LPM（vs logistic regression 的选择）、Holm-Bonferroni 校正（k=4 是否覆盖所有关键比较）、ICC 和 DEFF 的使用\n2. **实验设计**: seed 覆盖是否充分（function: 5 seeds, repo: 3 seeds）、cross-model consistency check 设计（DeepSeek 作为 secondary family）、checkpoint selection 策略（val-based vs final epoch 混用）、confound 控制（preprocessing, seq_length, training data volume）\n3. **Claims vs Evidence 对齐**: 每个 contribution 是否有充分统计证据支持、Abstract/Conclusion 中的 claims 是否过强或过弱、Limitations 是否充分覆盖已知局限\n4. **可重复性**: 超参数报告完整性、数据构建流程清晰度、compute budget 报告\n\n请以 ARR 审稿格式输出：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor) → Questions → Missing References → Suggested Overall Assessment (用 EMNLP 2026 评分标准)。\n\n严格、客观、不留情面。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n- 路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（各 section 为独立 .tex 文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_6/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR May cycle)\n- Deadline: 2026-05-25\n- 正文限制: Long paper 8 页（不含 references 和 limitations）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind（作者匿名）\n- Limitations section: mandatory，不计入页数\n- Appendix: 允许，参与审稿\n- Overall Assessment 评分标准: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**重点审查以下维度（必须逐项给出判断）**：\n\n1. **统计方法论**: TOST 等价检验（±2pp margin 是否合理）、clustered bootstrap 设计（114 clusters, 10K resamples）、mixed-effects LPM（vs logistic regression 的选择）、Holm-Bonferroni 校正（k=4 是否覆盖所有关键比较）、ICC 和 DEFF 的使用\n2. **实验设计**: seed 覆盖是否充分（function: 5 seeds, repo: 3 seeds）、cross-model consistency check 设计（DeepSeek 作为 secondary family）、checkpoint selection 策略（val-based vs final epoch 混用）、confound 控制（preprocessing, seq_length, training data volume）\n3. **Claims vs Evidence 对齐**: 每个 contribution 是否有充分统计证据支持、Abstract/Conclusion 中的 claims 是否过强或过弱、Limitations 是否充分覆盖已知局限\n4. **可重复性**: 超参数报告完整性、数据构建流程清晰度、compute budget 报告\n\n请以 ARR 审稿格式输出：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor) → Questions → Missing References → Suggested Overall Assessment (用 EMNLP 2026 评分标准)。\n\n严格、客观、不留情面。"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-22T13:40:51.521654+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11156
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-22T13:40:51.623004+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n- 路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（各 section 为独立 .tex 文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_6/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR May cycle)\n- Deadline: 2026-05-25\n- 正文限制: Long paper 8 页（不含 references 和 limitations）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind（作者匿名）\n- Limitations section: mandatory，不计入页数\n- Appendix: 允许，参与审稿\n- Overall Assessment 评分标准: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**重点审查以下维度（必须逐项给出判断）**：\n\n1. **Novelty / Contribution 意义**: 对 NLP/SE 社区的贡献程度——\"比较三种已有 formulation\" 是否构成足够的学术贡献？结论是否提供 actionable insights 还是仅确认直觉？formulation equivalence at function level 是否是 trivial finding？\n2. **Related Work 覆盖**: 是否遗漏重要相关工作（特别是 2025-2026 年的 execution simulation / code verification / process reward model 领域）？positioning 是否准确？\n3. **论文结构与可读性**: narrative arc 是否清晰？Section 之间过渡是否流畅？Table/Figure 是否有效传达关键信息？信息密度是否均匀（有无过度压缩或冗余）？\n4. **写作质量**: 术语一致性、符号系统清晰度、claim 的 hedging 是否恰当、是否有 AI 痕迹（过度使用 \"Furthermore\" / \"Moreover\" / \"Notably\" 等）\n5. **格式合规**: 8 页正文限制、匿名性（无 deanonymizing 信息）、checklist 完整性、Limitations 章节质量\n\n请以 ARR 审稿格式输出：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor) → Questions → Missing References → Suggested Overall Assessment (用 EMNLP 2026 评分标准)。\n\n严格、客观、不留情面。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n- 路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（各 section 为独立 .tex 文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_6/submitted.pdf`\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR May cycle)\n- Deadline: 2026-05-25\n- 正文限制: Long paper 8 页（不含 references 和 limitations）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind（作者匿名）\n- Limitations section: mandatory，不计入页数\n- Appendix: 允许，参与审稿\n- Overall Assessment 评分标准: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**重点审查以下维度（必须逐项给出判断）**：\n\n1. **Novelty / Contribution 意义**: 对 NLP/SE 社区的贡献程度——\"比较三种已有 formulation\" 是否构成足够的学术贡献？结论是否提供 actionable insights 还是仅确认直觉？formulation equivalence at function level 是否是 trivial finding？\n2. **Related Work 覆盖**: 是否遗漏重要相关工作（特别是 2025-2026 年的 execution simulation / code verification / process reward model 领域）？positioning 是否准确？\n3. **论文结构与可读性**: narrative arc 是否清晰？Section 之间过渡是否流畅？Table/Figure 是否有效传达关键信息？信息密度是否均匀（有无过度压缩或冗余）？\n4. **写作质量**: 术语一致性、符号系统清晰度、claim 的 hedging 是否恰当、是否有 AI 痕迹（过度使用 \"Furthermore\" / \"Moreover\" / \"Notably\" 等）\n5. **格式合规**: 8 页正文限制、匿名性（无 deanonymizing 信息）、checklist 完整性、Limitations 章节质量\n\n请以 ARR 审稿格式输出：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Must-Fix / Should-Fix / Minor) → Questions → Missing References → Suggested Overall Assessment (用 EMNLP 2026 评分标准)。\n\n严格、客观、不留情面。"
  }
}
```

</details>

---


### Tool result

_source line 592 · 2026-05-22T13:40:53.204809+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1581
}
```

</details>

---


### Assistant

_source line 593 · 2026-05-22T13:40:57.059062+00:00_

已完成 Round 1 派发：
- 视觉审查 Agent：已启动（fire-and-forget）
- Reviewer 1（方法严谨性 + 实验设计）：已分配
- Reviewer 2（新颖性 + 完整性 + 写作质量）：已分配

等待两名 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 51

## Round 51

38 recorded events


### User

_source line 594 · 2026-05-22T13:46:52.617061+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性 + 实验设计

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## Summary

本文系统比较了三种 execution-free 代码验证 formulation（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分），在 matched conditions 下使用两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（函数级/仓库级）、多种随机种子进行 ≤8B LoRA 微调。主要发现：(1) 函数级 CLS 和 CWM 近乎等价；(2) 仓库级 CLS 显著优于 CWM（18–26pp），主要因 format collapse；(3) 错误互补性暗示集成潜力。论文统计方法论全面（TOST、clustered bootstrap、mixed-effects LPM、Holm-Bonferroni），并附有大量消融实验和 threats-to-validity 分析。

---

## Strengths

**S1.** 实验框架设计严谨，真正做到了 matched comparison：固定模型容量、训练数据、compute，仅改变 formulation。这在该领域是首次，填补了重要空白。（§1, §3.1）

**S2.** 统计方法论选择恰当且多层次：(a) clustered bootstrap（114 clusters, 10K resamples）正确处理了 within-problem correlation（ICC = 0.191, DEFF = 3.97）；(b) TOST 等价检验搭配 SESOI 框架，先于观测数据设定 margin；(c) mixed-effects LPM 正式检验 formulation×complexity 交互效应（z = −23.7）；(d) Holm-Bonferroni 校正控制 family-wise error。四层统计工具形成了完整的证据链。（§3.2–3.5, Appendix K）

**S3.** Failure mode taxonomy（Table 4: format collapse / decision collapse / aggregation penalty）不仅是描述性的，而且为每种 formulation 的适用边界提供了可操作的诊断标准。这比单纯报告准确率数字更有价值。（§3.5, Table 4）

**S4.** 对 CWM 退化的诊断极为彻底：四种干预（rank 32、majority voting、relaxed matching、model scaling）全部失败，加上意外训练 artifact（CWM 模型在 CLS 格式数据上恢复 86.05%）、convergence analysis（eval loss 在 5% training 后单调增加），共同排除了多种替代解释，锁定了 formulation-level bottleneck。（Appendix H(c)(g), Table 16）

**S5.** Threats to Validity 分析（§3.7 + Appendix N）对五个 confound 逐一量化，包括 checkpoint selection（<1pp）、eval sequence length（~1.5pp）、preprocessing（~8pp）等，并计算了 worst-case compounding（~11.5pp），显示 18–26pp gap 仍有 ≥7.5pp margin。这种量化式的 threats 分析在实证论文中很少见。

**S6.** Oracle accuracy-utility framework（§2.3, Appendix A）从理论上推导了 per-test advantage 集中在 multi-F2P 实例的预测，并用 SWE-bench Verified 数据验证（T=2 贡献 55.3% 的总 advantage），理论与实验吻合。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] **TOST 检验结果被错误归属于 CLS–CWM 比较**

- **具体位置**: Abstract（第1段）、Conclusion §5（第1段）
- **问题**: Abstract 声称 "CLS and CWM are statistically equivalent across both families (TOST, 5 seeds)"；Conclusion 进一步给出 "CLS and CWM are statistically equivalent (TOST p=0.007, 5 seeds)"。然而，§3.4 标题为 "Per-Test vs. Trajectory-Level Equivalence"，明确执行的 TOST 检验对象是 **CLS vs TRAJ**（"We compare CLS (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds"），得到 p=0.007。Table 15（Holm-Bonferroni）中 Rank 2 也标注为 "Func: CLS vs TRAJ (TOST ±2pp)"。全文没有任何位置报告对 CLS–CWM 的正式 TOST 检验。
- **为什么影响接收**: 这是论文第一条 contribution 的核心统计证据。将 CLS–TRAJ 的 p 值错误标注为 CLS–CWM 的结果，构成了 abstract 和 conclusion 中的事实性错误。审稿人无法区分这是 (a) 笔误（将 TRAJ 写成了 CWM），还是 (b) CLS–CWM 等价从未被正式检验。两种情况都需要修正。
- **建议修改方向**: (1) 对 CLS–CWM 补做正式 TOST 检验并报告 p 值（考虑到 gap 仅 0.02–1.24pp，预期会通过 ±2pp margin）；(2) 在 abstract/conclusion 中准确标注哪个比较产生了 p=0.007；(3) 在 Holm-Bonferroni 表中加入 CLS–CWM TOST，相应更新 k 值。

**N2** [critical] **CWM formulation 的实验条件对其系统性不利，但结论却以 formulation-general 的方式表述**

- **具体位置**: Title、Abstract、§5 Conclusion
- **问题**: 论文标题 "The Formulation Design Space" 暗示对 formulation 的一般性比较，conclusion 推荐 "at repository level under ≤8B LoRA, CLS is recommended"。然而 CWM formulation 面临多重系统性劣势：(a) 所有 CWM repo-level runs 产生 NaN validation loss，被迫使用 final epoch checkpoint，而 convergence analysis（Table 16）显示此时 eval loss 已达最优值的 1.8 倍；(b) CWM 的 max_new_tokens=512 限制了有效输入上下文至 ~1,536 tokens，而 CLS 使用 5,120–8,192 tokens；(c) 原始 CWM（Meta, 2025）使用 32B 参数 + execution trace mid-training，与本文的 ≤8B LoRA 微调条件根本不同。虽然 §3.7 和 Limitations 有提及，但 abstract/conclusion 的 hedging 不够充分——读者可能误以为 "CWM as a formulation" 在 repo level 天生不行，而实际上是 "CWM under ≤8B LoRA without execution-trace pretraining" 不行。
- **为什么影响接收**: ARR soundness 要求 claims 与 evidence 对齐。当前的 framing 在 abstract 级别可能误导读者对 CWM formulation 本身能力的判断。
- **建议修改方向**: (1) 在 abstract 中明确 "under our ≤8B LoRA protocol" 限定所有 repo-level CWM 结论（当前 conclusion 有此 qualifier 但 abstract 更模糊）；(2) 在 §3.5 的 formulation divergence 段落中，增加一段讨论：如果 CWM 使用 early-stopped checkpoint（如 DeepSeek epoch 1 的 75.45%），gap 如何变化——当前 75.45% 仍落后于 CLS 的 ~84%，但 gap 从 ~26pp 缩至 ~9pp，这改变了 effect size 的定性解读；(3) 明确区分 "formulation-level conclusion"（generation 面临 output complexity 瓶颈）和 "regime-specific conclusion"（18–26pp gap 的具体数值）。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Repo-level variant 样本量 n=48 导致多个关键比较严重欠 power**

- **具体位置**: §3.5（Table 3）、§3.6（Analysis）、Appendix J（Table 14）
- **问题**: 所有 repo-level variant-level 分析基于 n=48（48 个 SWE-bench Verified variants）。论文自报 MDE ≈ 25pp（Appendix J），意味着只有 >25pp 的效应才能被检测到。CLS–TRAJ 在 repo level 的 gap（<10pp）完全落在 MDE 以下，论文却在 §5 conclusion 中推荐 CLS "for both accuracy and throughput"——这个推荐隐含了 CLS ≥ TRAJ 的假设，但该假设在当前样本量下无法被检验。
- **建议**: (1) 在 conclusion 的推荐中明确 CLS–TRAJ 比较在 variant level 是 underpowered 的，当前推荐主要基于 CLS 的 throughput 优势和 per-test 诊断能力，而非 accuracy 优势；(2) 报告 repo-level variant-level 分析所需的样本量（power analysis），给后续研究提供参考。

**W2** [warning] **Oracle 互补性估计均为单种子、无置信区间**

- **具体位置**: §3.6（"oracle routing reaches 95.83% variant accuracy"）、Abstract/§5
- **问题**: Contribution 3（error complementarity）的核心数字——函数级 oracle 90.63%（+2.80pp）和 repo 级 95.83%（+14.58pp）——均来自单一种子（seed 42）。在 n=48 repo variants 上，95.83% 意味着 46/48 正确，仅 2 个错误。这个估计的 binomial 95% CI 大约为 [85.7%, 99.5%]，非常宽。论文将这些数字作为 "the strongest practical argument for exploring the formulation design space"（§1）和 conclusion 中的核心方向，但没有提供任何不确定性量化。
- **建议**: (1) 在 repo-level oracle 数字旁加上 bootstrap/binomial CI；(2) 在 abstract/conclusion 中标注 "single-seed estimate"（conclusion 已有，abstract 没有）；(3) 多种子 oracle 分析（至少 function level 可以做，有 5 个种子）。

**W3** [warning] **TOST 种子池中混合 bfloat16 和 NF4 量化精度**

- **具体位置**: §3.4（"Seeds 789 and 0 use NF4 quantized inference"）
- **问题**: 5 个种子中 3 个使用 bfloat16、2 个使用 NF4 量化。论文将它们合并计算 TOST。虽然脚注指出 "Restricting to bfloat16 seeds only yields p=0.128: consistent in direction but underpowered"，但这恰恰说明 NF4 种子对 p 值的贡献是决定性的（从 0.128 降至 0.007）。问题在于：NF4 种子的加入不仅增加了样本量（提供 power），还可能系统性地缩小 CLS–TRAJ gap（如果 NF4 对两种 formulation 的影响不同）。论文未检验 precision × formulation 交互效应。
- **建议**: (1) 报告 NF4-only 子集的 CLS–TRAJ gap（2 种子）与 bfloat16-only 子集（3 种子）的对比；(2) 或在 mixed-effects 模型中加入 precision 作为固定效应，检验其是否显著调节 formulation 效应。

**W4** [warning] **CWM 的 checkpoint selection 没有与 CLS 对等的消融**

- **具体位置**: §3.7 Threats、Appendix N
- **问题**: CLS 有 checkpoint 消融（epoch 1/val-selected/final，range <1pp）。CWM 因所有 runs 产生 NaN val loss，全部使用 final epoch checkpoint。Convergence analysis（Table 16）显示 CWM eval loss 在 step 300–400 达到最小值，此后单调增加至 1.8× 最优。DeepSeek epoch-1 CWM 达到 75.45%（vs epoch-3 的 57.31%），这是 +18.14pp 的差异。但论文没有对 Qwen3 CWM 做同样的 early-stopping 消融，而 Qwen3 是 primary model family。如果 Qwen3 CWM early-stopped 也能达到 ~75%，则 CLS–CWM gap 从 ~18pp 缩至 ~10pp，显著改变结论的力度。
- **建议**: (1) 对 Qwen3-8B CWM 补做 epoch-1 checkpoint 的评估（至少一个种子）；(2) 在 §3.7 中量化 CWM checkpoint selection confound 的 upper bound（当前只量化了 CLS 的）。

---

### Minor 问题（不影响接收）

- **M1**: Mixed-effects LPM（§3.5, Appendix L）使用二元因变量但未提及是否使用了 robust standard errors（如 HC1/HC3）。在 n=56K 下影响可能很小，但 Angrist & Pischke (2009) 自己也建议对 LPM 使用 robust SEs。建议在 Appendix L 中添加一句说明。

- **M2**: Prompt templates 仅定性描述（Appendix E："CLS uses a binary classification template"），具体 template 文本指向 code repository。对于 reproducibility，建议在 appendix 中至少展示每种 formulation 的一个完整 prompt 示例。

- **M3**: Figure 2 的 y 轴截断起始于 ~55%，视觉上放大了 CLS–CWM 差异。建议标注 y 轴起点或在 caption 中提醒。

- **M4**: §3.3 scaling analysis 仅使用 2 个种子（42, 123）比较 4B→8B。CWM 的 -0.03pp 变化被解读为 "flat scaling"，但 2 个种子的 power 极低。建议避免做定性推断（如 "CWM flat scaling may reflect suboptimal hyperparameter transfer"）或明确标注这是 exploratory observation。

- **M5**: References 中 Xia et al. (2024) Agentless 标注 year=2025 但引用中写 2024。应统一。

---

## Questions to Authors

**Q1**: TOST p=0.007 是否确实是 CLS–CWM 的结果（如 abstract/conclusion 所述），还是 CLS–TRAJ 的结果（如 §3.4 和 Table 15 所示）？如果是后者，CLS–CWM 是否有单独的 TOST 检验？

**Q2**: 是否可以提供 Qwen3-8B CWM 在 epoch 1 或 step 400 附近 checkpoint 的 repo-level 评估结果？这对理解 CWM 的 "真实" 性能非常关键。

**Q3**: Oracle 互补性分析是否可以扩展到多种子？至少 function-level 有 5 个种子的数据。

**Q4**: 对于 mixed-effects LPM，是否检验过 logistic regression 的结果是否一致（即便 Angrist & Pischke 理论上保证了一致性，实际验证能增强可信度）？

---

## Missing References

- Ding et al. (2024) "RepoExec: Evaluate Code Generation with a Repository-Level Executable Benchmark" — 与本文的 repo-level verification 高度相关但未引用
- Chen et al. (2024) "Benchmarking the Role of LLM-based Verifiers in Code Generation" — 直接比较不同 verifier formulations

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 统计框架整体严谨（TOST+bootstrap+LPM+Holm），但 TOST 误归属是 critical error，CWM 比较条件不对等削弱了 formulation-level claims。修复后可达 4+。|
| **Excitement** | 3/5 | 研究问题实际且填补空白（首次 matched comparison），failure mode taxonomy 有洞察力，但核心发现（generation 在长输出时退化）相对直觉，且结论受限于 ≤8B regime。|
| **Reproducibility** | 4/5 | 超参数完整（Table 11）、compute budget 明确（~370 GPU-hrs）、承诺 release all code/data/checkpoints。扣分：prompt templates 未在论文中给出；NaN val loss 的处理策略虽有记录但增加了复现难度。|

---

## 总体评分

**Overall**: **3.0 — Findings**

**一句话总结**: 实验框架设计优秀、统计方法论全面，但核心 TOST 检验的归属错误（CLS–CWM vs CLS–TRAJ）和 CWM 比较条件的系统性不对等（checkpoint selection、scale、pretraining）使得两个主要 claim 的证据基础存在裂缝。修复 N1（TOST 误归属）和加强 N2（CWM 条件对等性的讨论和 hedging）后，本文有 3.5（Borderline Conference）的潜力——failure mode taxonomy、交互效应分析和 oracle framework 是有价值的 methodological contribution。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 595 · 2026-05-22T13:47:04.578753+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 596 · 2026-05-22T13:47:06.784957+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 2206
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-22T13:47:06.802094+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status,director_post_to_reviewer,dispatch_visual_check,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status,director_post_to_reviewer,dispatch_visual_check,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-22T13:47:06.926235+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 124
}
```

</details>

---


### Tool call

_source line 599 · 2026-05-22T13:47:09.790679+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 600 · 2026-05-22T13:47:09.791069+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-22T13:47:10.242426+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_external_review_status",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_external_review_status",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 602 · 2026-05-22T13:47:10.242831+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-22T13:47:10.744395+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_visual_check_status",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_visual_check_status",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-22T13:47:10.744825+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 605 · 2026-05-22T13:47:11.246512+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 606 · 2026-05-22T13:47:11.297213+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-22T13:47:11.698916+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-22T13:47:11.699446+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-22T13:47:12.205365+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-22T13:47:12.205768+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-22T13:47:12.659188+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:dispatch_visual_check",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:dispatch_visual_check",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-22T13:47:12.659614+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-22T13:47:13.111458+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:request_external_review",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:request_external_review",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-22T13:47:13.111914+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-22T13:47:13.312925+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-22T13:47:13.363918+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-22T13:47:17.783221+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "mcp agent-ml-research director",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "mcp agent-ml-research director",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-22T13:47:17.884128+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 619 · 2026-05-22T13:47:23.773430+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-22T13:47:24.327951+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-22T13:47:24.780069+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (252 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s123-eval-1epoch | Eval DeepSeek CWM repo-level s123 1-epoch checkpoint (checkpoint-4209)。验证 appendix cwm_convergence 中引用的 early-stopping 数据 (75.45% acc / 66.4% unparseable) 是否在干净 eval 下可复现。 | — | — | — |\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- 
…[truncated 1818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-22T13:47:24.780540+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 623 · 2026-05-22T13:47:24.831041+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 624 · 2026-05-22T13:47:24.831548+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T13:40:25.660899+00:00\", \"completed_at\": \"2026-05-22T13:43:08.661444+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 22\", \"message\": \"附录最后一页仅 ~10% 填充（17 行文本），剩余 ~90% 空白。建议将 Appendix O (Extended Limitations) 内容合并到前一页，或调整附录顺序消除尾页大面积空白\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-2\", \"message\": \"连续 2 页纯文本无任何 display item（Abstract + Introduction）。Figure 1 在 page 3 出现。对于 ACL 格式论文属常见模式，但若能在 page 2 底部或 Introduction 中嵌入一个小型概览图/表，可加速审稿人锚定\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 柱状图的 axis labels 和 bar labels 在打印尺寸下偏小（约正文字号 65-70%），建议稍微放大字号或增加图的宽度\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Tables 1 和 2 紧密排布在同一页，信息密度高。目前可读但较紧凑——如果后续修订有空间余裕，可考虑增加表间距\"}, {\"severity\": \"info\", \"dimension\": \"pages 13-14\", \"message\": \"附录 Tables 5-9 集中在 2 页内（5 个表），密度极高但均在 column width 内，无溢出\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-22T13:47:25.333492+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 626 · 2026-05-22T13:47:25.384063+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 627 · 2026-05-22T13:47:29.498665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 628 · 2026-05-22T13:47:29.850705+00:00_

1	# === Round 6 Issues ===
2	
3	# --- Round 6 Must-Fix (Consensus Critical) ---
4	
5	- id: "R6-N1"
6	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
7	  category: experiment
8	  severity: critical
9	  status: in_progress
10	  first_raised_round: 6
11	  last_seen_round: 7
12	  mentions:
13	    - round: 6
14	      reviewers: [1, 2]
15	      note: "两人独立提出，最高共识。"
16	    - round: 7
17	      reviewers: [pre-review]
18	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress. Blocked on CWM data (~May 22-23)."
19	  action_items:
20	    - round: 6
21	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
22	      assigned_to: "paper"
23	      status: in_progress
24	  resolution: "CLS 3-seed ✅, TRAJ 3-seed ✅. CWM training: DeepSeek s123-v2 ~May 21 09:30, Qwen s123+s456 ~May 22 22:00."
25	  resolution_round: null
26	
27	- id: "R6-N2"
28	  summary: "Checkpoint selection 系统性偏向 CLS"
29	  category: method
30	  severity: critical
31	  status: resolved
32	  first_raised_round: 6
33	  last_seen_round: 7
34	  mentions:
35	    - round: 6
36	      reviewers: [1, 2]
37	      note: "系统性偏差方向与 observed effect 一致。"
38	    - round: 7
39	      reviewers: [pre-review]
40	      note: "Reviewer 确认修复充分。"
41	  action_items:
42	    - round: 6
43	      action: "CLS epoch ablation + matched epoch-3 解释"
44	      assigned_to: "paper"
45	      status: resolved
46	  resolution: "CLS epoch ablation <1pp range. Matched epoch-3 cross-model gap ~2pp. Written in §4.4."
47	  resolution_round: 7
48	
49	- id: "R6-N3"
50	  summary: "Oracle ensemble accuracy 数值矛盾"
51	  category: experiment
52	  severity: critical
53	  status: resolved
54	  first_raised_round: 6
55	  last_seen_round: 6
56	  action_items:
57	    - round: 6
58	      action: "核实并统一数字"
59	      assigned_to: "paper"
60	      status: resolved
61	  resolution: "Oracle 90.63% 验证正确。96.03% 已删除。Error direction 6 处修正。"
62	  resolution_round: 7
63	
64	- id: "R6-
…[truncated 7713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 629 · 2026-05-22T13:47:30.152343+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 630 · 2026-05-22T13:47:30.203030+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_5.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 631 · 2026-05-22T13:48:25.137864+00:00_

上下文恢复完毕。状态摘要：

**当前 Round**：Round 6（fresh 模式）
**投稿目标**：EMNLP 2026 via ARR
**论文**："The Formulation Design Space for Execution-Free Code Verification"
**PDF**：`artifacts/review_round_6/submitted.pdf`

**已完成**：
- 视觉审查：✅ done（1 warning: 附录尾页 90% 空白；4 info）
- 外部审稿：未请求
- Reviewer 1：✅ 已返回（方法严谨性 + 实验设计）
- Reviewer 2：⏳ 待返回（新颖性 + 完整性）

---

**Reviewer 1 报告收悉。** 关键发现概括：

| 类别 | ID | 严重性 | 核心问题 |
|------|-----|--------|---------|
| Must-Fix | N1 | critical | TOST p=0.007 被错误归属于 CLS–CWM，实际检验对象是 CLS–TRAJ |
| Must-Fix | N2 | critical | CWM 实验条件系统性不利（NaN checkpoint / 短上下文 / 缺 pretrain），但结论以 formulation-general 表述 |
| Should-Fix | W1 | warning | Repo-level n=48，MDE≈25pp，CLS–TRAJ 比较 underpowered |
| Should-Fix | W2 | warning | Oracle 互补性为单种子、无 CI |
| Should-Fix | W3 | warning | TOST 5 种子混合 bfloat16 + NF4，precision×formulation 交互未检验 |
| Should-Fix | W4 | warning | CWM checkpoint ablation 只有 DeepSeek，缺 Qwen3 |
| Minor | M1-M5 | info | LPM robust SEs、prompt templates、Figure 2 y轴截断、scaling 2-seed、Xia year |

**Soundness 3.5 / Excitement 3 / Reproducibility 4 → Overall 3.0 (Findings)**

N1 是全新发现（TOST 归属错误），此前各轮未出现。N2 与历史 issue R6-W2（CWM regime qualifier）相关但更深入——R1 要求量化 early-stop 对 gap 的影响。

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 52

## Round 52

6 recorded events


### User

_source line 632 · 2026-05-22T13:48:26.264852+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心发现：

1. **TOST 误归属（Must-Fix）**：Abstract/Conclusion 声称 CLS–CWM 等价（TOST p=0.007），但 §3.4 和 Table 15 表明该 p 值来自 CLS–TRAJ 比较。CLS–CWM 从未做过正式 TOST 检验。

2. **CWM 比较条件不对等（Must-Fix）**：所有 CWM repo-level runs 被迫使用 final epoch checkpoint（NaN val loss），而此时 eval loss 已达最优值 1.8 倍。DeepSeek early-stopped CWM 从 57% 跳到 75%，但 Qwen3 没有做同样的消融。论文标题暗示 formulation-general 结论，但实际是 regime-specific 的。

3. 另外四个 Should-Fix：n=48 variant 样本量导致 CLS–TRAJ 比较欠 power、oracle 估计无 CI 且单种子、TOST 种子池混合精度、CWM checkpoint 消融缺失。

Overall: 3.0（Findings），修复核心问题后有 3.5 潜力。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（Novelty + Completeness + Writing Quality）

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## Summary

本文系统比较了三种 execution-free 代码验证 formulation：per-test classification (CLS)、execution output generation (CWM)、trajectory-level scoring (TRAJ)。实验在两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（function-level、repo-level）上进行，使用 ≤8B LoRA fine-tuning。主要发现：(1) function level 三种 formulation 统计等价；(2) repo level CLS 大幅优于 CWM（18–26pp gap），主因是 CWM 的 format collapse；(3) 错误互补性暗示 formulation routing 的潜力。论文还提出了一个 failure mode taxonomy（format collapse, decision collapse, aggregation penalty）。

---

## Strengths（逐条）

**S1. 实验方法论严谨。** 使用 TOST 等价检验、clustered bootstrap（按 problem 聚类）、ICC、Holm-Bonferroni 多重比较校正、SESOI framework 设定等价阈值——统计方法论远超同类 empirical study 的平均水平。这是论文最突出的优势。

**S2. Matched experimental design。** 控制变量设计合理：相同训练数据、相同 LoRA 配置、相同模型家族，只改变 formulation。这使得 formulation 效果的归因具有较高可信度（虽然仍有 confound，见 W2）。

**S3. Failure mode taxonomy 有实用价值。** Table 4 的三类 failure mode（format collapse / decision collapse / aggregation penalty）对 practitioner 选择 formulation 有直接指导意义，比单纯报告准确率差异更有信息量。

**S4. 透明的 limitations 讨论。** §3.7 Threats to Validity 和 Limitations 对几乎所有 confound 进行了系统讨论（checkpoint selection、preprocessing、eval sequence length、CWM scale 限制等），hedging 恰当，没有过度声称因果关系。

**S5. 丰富的 appendix。** 10+ 页附录覆盖 ablation、sensitivity analysis、qualitative examples、power analysis，审稿过程中几乎所有追问都能在附录找到答案。

**S6. 写作整体干净。** 主文几乎没有 AI 痕迹（"Furthermore"/"Moreover"/"Notably" 仅出现在 appendix 中 3 次），术语体系（CLS/CWM/TRAJ）一致，claim 的 hedging 恰当（大量使用 "under our protocol"、"conditional on the ≤8B LoRA regime" 等限定语）。

---

## Weaknesses（逐条，标注 severity）

**W1. [Must-Fix] CWM baseline 严重偏弱，削弱了核心结论的说服力。**

- **具体位置**：§3.1 (Models and training), §3.5 (Repo-Level), Limitations
- **问题**：论文的 CWM 是 ≤8B LoRA fine-tuned model，而非原始 CWM（Meta, 32B, execution trace mid-training）。这两个设置的差距是根本性的：原始 CWM 专门在 execution trace 数据上做了 mid-training 来学习输出格式，而本文的 CWM 只是普通 LLM + LoRA，从未见过 execution trace。repo-level 的 18–26pp gap 和 format collapse（53–74% unparseable）很可能主要归因于 pretraining 数据差异而非 formulation 本身的固有缺陷。
- **为什么影响接收**：论文的核心 claim 是 "formulation choice is governed by code complexity"，但如果 CWM 的失败主要是因为 baseline 不充分（缺少 execution trace pretraining），那这个 claim 变成 "inadequately pretrained generation models fail at repo level"——这是 trivial 的。论文虽然承认了这个 limitation，但 abstract 和 introduction 的措辞（"the CLS–CWM gap widens to 18–26pp"）没有充分限定这一点。
- **建议修改方向**：(1) Abstract 和 Introduction 中所有提到 CWM 18–26pp gap 的地方必须加上 "under ≤8B LoRA fine-tuning without execution trace pretraining" 限定；(2) 讨论 GenRM（Zhang et al., 2024, ICLR 2025）等工作中 generative verifier 在数学推理领域优于 discriminative verifier 的发现，分析为什么代码验证可能呈现相反模式（或承认 scale 不足以下定论）；(3) 理想情况下补充一个 32B 规模的实验（即使只有 1 seed）来检验 format collapse 是否是 scale-dependent。

**W2. [Must-Fix] Novelty 不足以达到 Conference 水平——对已有 formulation 的比较缺少新方法论或新洞见。**

- **问题**：论文不提出任何新方法，而是比较三种已有 formulation。这本身不是问题（systematic empirical study 有其价值），但前提是比较的结论必须超越直觉、提供 surprising 或 actionable 的 insight。让我逐一审视三个核心发现：
  - **Finding 1（function-level equivalence）**：当输出是 1 个 token（integer/boolean）时，generation ≈ classification——这基本是 trivial 的。输出空间极小时，generation 不会比 classification 差，这不需要实验验证。
  - **Finding 2（repo-level divergence via format collapse）**：长输出的 generation 模型容易产生格式错误——这也是广泛已知的。任何使用过 LLM 生成结构化输出的 practitioner 都经历过这个问题。
  - **Finding 3（error complementarity）**：oracle routing 达到 95.83%，但 (a) 这是 single-seed estimate（n=48 variants），(b) re-repair pilot（n=44, p=0.42）显示 per-test diagnostics 没有下游收益，直接削弱了 complementarity 的实用价值。
- **为什么影响接收**：这三个发现都没有超越一个有经验的 practitioner 的直觉。Failure mode taxonomy（S3）是相对新颖的贡献，但它是 descriptive 的，没有 prescriptive 价值（论文没有提出如何利用 taxonomy 来改进 verification）。
- **建议修改方向**：(1) 在 taxonomy 基础上提出 complexity-aware routing algorithm 并验证其效果（哪怕是 oracle analysis 之外的 heuristic）；(2) 深入分析 WHY CLS 和 CWM 在 function level 等价——是因为 function-level 代码语义简单，还是因为输出空间小？一个 ablation 可以用 CWM 预测 short structured output（如 JSON {pass: true/false}）vs. full execution trace，以区分两个假设；(3) 如果无法增加新贡献，需要更诚实地将论文定位为 "benchmark/replication study" 而非 "systematic empirical study with actionable insights"。

**W3. [Should-Fix] z=−23.7 interaction statistic 仅基于 DeepSeek-Coder，但在 abstract/intro 中被作为核心发现呈现。**

- **具体位置**：Abstract（"a significant interaction (z=−23.7)"），§1 Introduction（同），§3.5（"A mixed-effects linear probability model... DeepSeek-Coder"）
- **问题**：§3.5 明确说明 interaction 分析只用了 DeepSeek-Coder（"the only family with both function- and repo-level CWM evaluations under matched conditions"），但 abstract 和 introduction 没有提及这个限制。读者会自然认为这是跨模型的结论。
- **建议**：Abstract 中改为 "a significant interaction (z=−23.7, DeepSeek-Coder)" 或至少在 introduction 中明确标注。

**W4. [Should-Fix] Oracle routing 结果（90.63%/95.83%）均为 single-seed estimate，统计可靠性不足。**

- **具体位置**：§1 contribution 3、§3.6 Error complementarity、§5 Conclusion
- **问题**：Function-level oracle 90.63% 是 single-seed estimate；repo-level 95.83% 基于 n=48 variants。这些数字被反复在 abstract、introduction、conclusion 中引用，但没有 confidence interval 或多 seed 验证。given function-level per-seed accuracy 的 std 为 0.37–0.97pp，oracle combination 的 variance 可能更大。
- **建议**：提供 oracle 结果的 bootstrap CI，或至少在引用时明确标注 "(single-seed estimate)"。

**W5. [Should-Fix] 遗漏关键相关工作：GenRM（Zhang et al., 2024）。**

- **具体位置**：§4 Related Work
- **问题**：GenRM / "Generative Verifiers: Reward Modeling as Next-Token Prediction"（Zhang et al., ICLR 2025）直接研究了 discriminative vs. generative formulation 在 verification/reward modeling 中的效果，发现 generative verifier 在数学推理任务上显著优于 discriminative verifier（GSM8K 上 73%→93.4%）。这与本文在 repo-level 代码验证上的发现形成直接对比/矛盾。论文的 §4 "Process vs. Outcome Supervision" 段讨论了 PRM/ORM，但完全没有提到 GenRM 这个最直接的相关工作。
- **为什么重要**：GenRM 的发现暗示 generative formulation 在 sufficient scale 下可能优于 classification——这恰好支持本文 CWM 失败可能是 scale 问题而非 formulation 固有缺陷的假设。不讨论这个工作是 related work 的显著遗漏。
- **额外遗漏**：CVeDRL（2026, arXiv 2601.22803）——difficulty-aware RL for code verification，与本文的 per-test difficulty 分析相关。

**W6. [Should-Fix] TRAJ 的实验设置不公平，削弱了 TRAJ 相关结论的可信度。**

- **具体位置**：§3.1 (Datasets), Appendix §N (TRAJ training regime)
- **问题**：TRAJ 使用 ~400 repo-level variants 训练，而 CLS 和 CWM 使用 ~70K per-test instances。虽然这是 formulation 固有的（trajectory-level labels 只有 variant 粒度），但训练数据量相差 175×，这使得 TRAJ 的 repo-level 表现（72.91–77.08%）可能主要受限于数据量而非 formulation。Downsample ablation（80.74% vs 72.92%）控制了 CLS 的数据量但没有控制 label granularity。
- **建议**：讨论 data augmentation for TRAJ（如对每个 variant 生成多个 prompt 变体）是否可能缩小差距。

**W7. [Minor] 信息密度不均匀：§3.5 过度压缩，§3.3 Scaling Behavior 价值有限。**

- §3.5 (Repo-Level) 在不到 1.5 页内塞入了 formulation divergence、cross-model consistency、failure mode taxonomy、default assignment artifact、complexity as moderator、formulation×complexity interaction——每个都值得更多讨论空间。
- §3.3 (Scaling Behavior) 仅比较 4B vs 8B 两个 size，n=2 seeds，结论有限（"CLS and TRAJ scale, CWM doesn't"），可以压缩为一段，腾出空间给 §3.5。

**W8. [Minor] Figure 2 信息冗余。**

- Figure 2 展示的信息（function→repo gap amplification）已经在 Table 1、Table 3 和正文中充分表达。作为唯一的 figure（除 Figure 1 架构图），这个位置可以更好地用于展示 failure mode taxonomy 的可视化或 error complementarity 的 Venn diagram。

**W9. [Minor] Limitations 段过于简短。**

- Limitations 只有一小段（约 10 行），仅覆盖 3 个点。鉴于本文有大量 confound（W1-W6），建议至少增加：(a) synthetic mutation 与 real bug 的 gap 讨论；(b) 仅 2 个模型家族的 generalizability 限制。虽然 §3.7 讨论了 threats，但 Limitations section 本身应该是 self-contained 的。

---

## Questions for Authors

**Q1.** GenRM (Zhang et al., ICLR 2025) 发现 generative verifier 在数学推理上优于 discriminative verifier。你们如何解释代码验证领域呈现相反趋势？是 domain difference、scale difference、还是 pretraining difference？

**Q2.** 如果将 CWM 的输出改为 short structured format（如 JSON `{"result": "PASS", "output": "42"}`）而非 free-form execution trace，format collapse 是否会显著减少？这个 ablation 可以区分 "输出长度" 和 "generation formulation" 两个因素的贡献。

**Q3.** Re-repair pilot (n=44, p=0.42) 显示 per-test diagnostics 没有下游收益。这是否意味着 CLS 的 diagnostic advantage 是 theoretical 的而非 practical 的？如果是，"error complementarity" 作为核心贡献之一的地位是否需要降低？

**Q4.** 论文在 Appendix 中提到 accidental training artifact（CWM model trained on classification-format data, 86.05% accuracy with 0% unparseable）。这个发现是否暗示 format 是唯一瓶颈，只要解决 format compliance 就能恢复 CWM 的性能？如果是，constrained decoding 为什么没有被尝试？

---

## Missing References

1. **Zhang et al. (2024/2025)**, "Generative Verifiers: Reward Modeling as Next-Token Prediction," ICLR 2025. 直接比较 discriminative vs. generative formulation for verification。
2. **CVeDRL** (2026, arXiv 2601.22803), difficulty-aware RL for code verification。
3. **GenPRM** (2025, arXiv 2504.00891), "Process Reward Models That Think" — generative PRM with CoT。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.0/5 | 统计方法论优秀，但 CWM baseline 严重偏弱（≤8B LoRA vs. 原始 32B+mid-training），TRAJ 训练数据量不对等（175×），oracle results 为 single-seed。核心比较的公平性存疑。 |
| **Excitement** | 2.5/5 | 研究问题相关，但三个核心发现均未超越 practitioner 直觉。没有新方法、新 formulation、或 surprising insight。Failure mode taxonomy 有增量价值。 |
| **Reproducibility** | 4.0/5 | 详细报告了 hyperparameters、seeds、统计方法；承诺 release code/data/checkpoints。唯一扣分：部分 repo-level 结果的 seed 数不足。 |

---

## 总体评分

**Overall**: **3.0** (Findings)

**一句话总结**: 方法论严谨的 empirical study，但核心贡献受限于 (1) CWM baseline 不充分导致主要发现（formulation divergence）的归因不清，(2) 三个核心 finding 均未超越有经验 practitioner 的直觉，(3) 纯比较性工作没有提出新方法或 actionable 的改进方案。适合 Findings track，但 novelty 和 insight depth 不足以支撑 main conference。

---

**Reviewer Confidence**: 4/5 — 熟悉 code generation/verification 和 reward modeling 领域，仔细阅读了全文含 appendix。

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**：Overall 3.0（Findings track）。

主要问题：
1. **CWM baseline 严重偏弱**（≤8B LoRA vs. 原始 32B+execution trace mid-training），导致 18–26pp 的 formulation divergence 结论归因不清——可能是 scale/pretraining 问题而非 formulation 固有缺陷
2. **Novelty 不足**——三个核心 finding（function-level equivalence、repo-level format collapse、error complementarity）均未超越 practitioner 直觉，且没有提出新方法
3. **遗漏 GenRM**（Zhang et al., ICLR 2025）这个最直接的相关工作——该工作发现 generative verifier 优于 discriminative，与本文结论形成有趣对比但未被讨论

优势方面：统计方法论（TOST/clustered bootstrap/Holm-Bonferroni）、matched experimental design、failure mode taxonomy、透明的 threats 讨论，以及写作质量（几乎无 AI 痕迹）均为显著亮点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 633 · 2026-05-22T13:50:48.163132+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条 Weakness/Question，使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 也请简要标注是否同意。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 代码验证 formulation（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分），在 matched conditions 下使用两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（函数级/仓库级）、多种随机种子进行 ≤8B LoRA 微调。主要发现：(1) 函数级 CLS 和 CWM 近乎等价；(2) 仓库级 CLS 显著优于 CWM（18–26pp），主要因 format collapse；(3) 错误互补性暗示集成潜力。论文统计方法论全面（TOST、clustered bootstrap、mixed-effects LPM、Holm-Bonferroni），并附有大量消融实验和 threats-to-validity 分析。\n\n---\n\n## Strengths\n\n**S1.** 实验框架设计严谨，真正做到了 matched comparison：固定模型容量、训练数据、compute，仅改变 formulation。这在该领域是首次，填补了重要空白。（§1, §3.1）\n\n**S2.** 统计方法论选择恰当且多层次：(a) clustered bootstrap（114 clusters, 10K resamples）正确处理了 within-problem correlation（ICC = 0.191, DEFF = 3.97）；(b) TOST 等价检验搭配 SESOI 框架，先于观测数据设定 margin；(c) mixed-effects LPM 正式检验 formulation×complexity 交互效应（z = −23.7）；(d) Holm-Bonferroni 校正控制 family-wise error。四层统计工具形成了完整的证据链。（§3.2–3.5, Appendix K）\n\n**S3.** Failure mode taxonomy（Table 4: format collapse / decision collapse / aggregation penalty）不仅是描述性的，而且为每种 formulation 的适用边界提供了可操作的诊断标准。这比单纯报告准确率数字更有价值。（§3.5, Table 4）\n\n**S4.** 对 CWM 退化的诊断极为彻底：四种干预（rank 32、majority voting、relaxed matching、model scaling）全部失败，加上意外训练 artifact（CWM 模型在 CLS 格式数据上恢复 86.05%）、convergence analysis（eval loss 在 5% training 后单调增加），共同排除了多种替代解释，锁定了 formulation-level bottleneck。（Appendix H(c)(g), Table 16）\n\n**S5.** Threats to Validity 分析（§3.7 + Appendix N）对五个 confound 逐一量化，包括 checkpoint selection（<1pp）、eval sequence length（~1.5pp）、preprocessing（~8pp）等，并计算了 worst-case compounding（~11.5pp），显示 18–26pp gap 仍有 ≥7.5pp margin。这种量化式的 threats 分析在实证论文中很少见。\n\n**S6.** Oracle accuracy-utility framework（§2.3, Appendix A）从理论上推导了 per-test advantage 集中在 multi-F2P 实例的预测，并用 SWE-bench Verified 数据验证（T=2 贡献 55.3% 的总 advantage），理论与实验吻合。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **TOST 检验结果被错误归属于 CLS–CWM 比较**\n\n- **具体位置**: Abstract（第1段）、Conclusion §5（第1段）\n- **问题**: Abstract 声称 \"CLS and CWM are statistically equivalent across both families (TOST, 5 seeds)\"；Conclusion 进一步给出 \"CLS and CWM are statistically equivalent (TOST p=0.007, 5 seeds)\"。然而，§3.4 标题为 \"Per-Test vs. Trajectory-Level Equivalence\"，明确执行的 TOST 检验对象是 **CLS vs TRAJ**（\"We compare CLS (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds\"），得到 p=0.007。Table 15（Holm-Bonferroni）中 Rank 2 也标注为 \"Func: CLS vs TRAJ (TOST ±2pp)\"。全文没有任何位置报告对 CLS–CWM 的正式 TOST 检验。\n- **为什么影响接收**: 这是论文第一条 contribution 的核心统计证据。将 CLS–TRAJ 的 p 值错误标注为 CLS–CWM 的结果，构成了 abstract 和 conclusion 中的事实性错误。审稿人无法区分这是 (a) 笔误（将 TRAJ 写成了 CWM），还是 (b) CLS–CWM 等价从未被正式检验。两种情况都需要修正。\n- **建议修改方向**: (1) 对 CLS–CWM 补做正式 TOST 检验并报告 p 值（考虑到 gap 仅 0.02–1.24pp，预期会通过 ±2pp margin）；(2) 在 abstract/conclusion 中准确标注哪个比较产生了 p=0.007；(3) 在 Holm-Bonferroni 表中加入 CLS–CWM TOST，相应更新 k 值。\n\n**N2** [critical] **CWM formulation 的实验条件对其系统性不利，但结论却以 formulation-general 的方式表述**\n\n- **具体位置**: Title、Abstract、§5 Conclusion\n- **问题**: 论文标题 \"The Formulation Design Space\" 暗示对 formulation 的一般性比较，conclusion 推荐 \"at repository level under ≤8B LoRA, CLS is recommended\"。然而 CWM formulation 面临多重系统性劣势：(a) 所有 CWM repo-level runs 产生 NaN validation loss，被迫使用 final epoch checkpoint，而 convergence analysis（Table 16）显示此时 eval loss 已达最优值的 1.8 倍；(b) CWM 的 max_new_tokens=512 限制了有效输入上下文至 ~1,536 tokens，而 CLS 使用 5,120–8,192 tokens；(c) 原始 CWM（Meta, 2025）使用 32B 参数 + execution trace mid-training，与本文的 ≤8B LoRA 微调条件根本不同。虽然 §3.7 和 Limitations 有提及，但 abstract/conclusion 的 hedging 不够充分——读者可能误以为 \"CWM as a formulation\" 在 repo level 天生不行，而实际上是 \"CWM under ≤8B LoRA without execution-trace pretraining\" 不行。\n- **为什么影响接收**: ARR soundness 要求 claims 与 evidence 对齐。当前的 framing 在 abstract 级别可能误导读者对 CWM formulation 本身能力的判断。\n- **建议修改方向**: (1) 在 abstract 中明确 \"under our ≤8B LoRA protocol\" 限定所有 repo-level CWM 结论（当前 conclusion 有此 qualifier 但 abstract 更模糊）；(2) 在 §3.5 的 formulation divergence 段落中，增加一段讨论：如果 CWM 使用 early-stopped checkpoint（如 DeepSeek epoch 1 的 75.45%），gap 如何变化——当前 75.45% 仍落后于 CLS 的 ~84%，但 gap 从 ~26pp 缩至 ~9pp，这改变了 effect size 的定性解读；(3) 明确区分 \"formulation-level conclusion\"（generation 面临 output complexity 瓶颈）和 \"regime-specific conclusion\"（18–26pp gap 的具体数值）。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Repo-level variant 样本量 n=48 导致多个关键比较严重欠 power**\n\n- **具体位置**: §3.5（Table 3）、§3.6（Analysis）、Appendix J（Table 14）\n- **问题**: 所有 repo-level variant-level 分析基于 n=48（48 个 SWE-bench Verified variants）。论文自报 MDE ≈ 25pp（Appendix J），意味着只有 >25pp 的效应才能被检测到。CLS–TRAJ 在 repo level 的 gap（<10pp）完全落在 MDE 以下，论文却在 §5 conclusion 中推荐 CLS \"for both accuracy and throughput\"——这个推荐隐含了 CLS ≥ TRAJ 的假设，但该假设在当前样本量下无法被检验。\n- **建议**: (1) 在 conclusion 的推荐中明确 CLS–TRAJ 比较在 variant level 是 underpowered 的，当前推荐主要基于 CLS 的 throughput 优势和 per-test 诊断能力，而非 accuracy 优势；(2) 报告 repo-level variant-level 分析所需的样本量（power analysis），给后续研究提供参考。\n\n**W2** [warning] **Oracle 互补性估计均为单种子、无置信区间**\n\n- **具体位置**: §3.6（\"oracle routing reaches 95.83% variant accuracy\"）、Abstract/§5\n- **问题**: Contribution 3（error complementarity）的核心数字——函数级 oracle 90.63%（+2.80pp）和 repo 级 95.83%（+14.58pp）——均来自单一种子（seed 42）。在 n=48 repo variants 上，95.83% 意味着 46/48 正确，仅 2 个错误。这个估计的 binomial 95% CI 大约为 [85.7%, 99.5%]，非常宽。论文将这些数字作为 \"the strongest practical argument for exploring the formulation design space\"（§1）和 conclusion 中的核心方向，但没有提供任何不确定性量化。\n- **建议**: (1) 在 repo-level oracle 数字旁加上 bootstrap/binomial CI；(2) 在 abstract/conclusion 中标注 \"single-seed estimate\"（conclusion 已有，abstract 没有）；(3) 多种子 oracle 分析（至少 function level 可以做，有 5 个种子）。\n\n**W3** [warning] **TOST 种子池中混合 bfloat16 和 NF4 量化精度**\n\n- **具体位置**: §3.4（\"Seeds 789 and 0 use NF4 quantized inference\"）\n- **问题**: 5 个种子中 3 个使用 bfloat16、2 个使用 NF4 量化。论文将它们合并计算 TOST。虽然脚注指出 \"Restricting to bfloat16 seeds only yields p=0.128: consistent in direction but underpowered\"，但这恰恰说明 NF4 种子对 p 值的贡献是决定性的（从 0.128 降至 0.007）。问题在于：NF4 种子的加入不仅增加了样本量（提供 power），还可能系统性地缩小 CLS–TRAJ gap（如果 NF4 对两种 formulation 的影响不同）。论文未检验 precision × formulation 交互效应。\n- **建议**: (1) 报告 NF4-only 子集的 CLS–TRAJ gap（2 种子）与 bfloat16-only 子集（3 种子）的对比；(2) 或在 mixed-effects 模型中加入 precision 作为固定效应，检验其是否显著调节 formulation 效应。\n\n**W4** [warning] **CWM 的 checkpoint selection 没有与 CLS 对等的消融**\n\n- **具体位置**: §3.7 Threats、Appendix N\n- **问题**: CLS 有 checkpoint 消融（epoch 1/val-selected/final，range <1pp）。CWM 因所有 runs 产生 NaN val loss，全部使用 final epoch checkpoint。Convergence analysis（Table 16）显示 CWM eval loss 在 step 300–400 达到最小值，此后单调增加至 1.8× 最优。DeepSeek epoch-1 CWM 达到 75.45%（vs epoch-3 的 57.31%），这是 +18.14pp 的差异。但论文没有对 Qwen3 CWM 做同样的 early-stopping 消融，而 Qwen3 是 primary model family。如果 Qwen3 CWM early-stopped 也能达到 ~75%，则 CLS–CWM gap 从 ~18pp 缩至 ~10pp，显著改变结论的力度。\n- **建议**: (1) 对 Qwen3-8B CWM 补做 epoch-1 checkpoint 的评估（至少一个种子）；(2) 在 §3.7 中量化 CWM checkpoint selection confound 的 upper bound（当前只量化了 CLS 的）。\n\n---\n\n### Minor 问题（不影响接收）\n\n- **M1**: Mixed-effects LPM（§3.5, Appendix L）使用二元因变量但未提及是否使用了 robust standard errors（如 HC1/HC3）。在 n=56K 下影响可能很小，但 Angrist & Pischke (2009) 自己也建议对 LPM 使用 robust SEs。建议在 Appendix L 中添加一句说明。\n\n- **M2**: Prompt templates 仅定性描述（Appendix E：\"CLS uses a binary classification template\"），具体 template 文本指向 code repository。对于 reproducibility，建议在 appendix 中至少展示每种 formulation 的一个完整 prompt 示例。\n\n- **M3**: Figure 2 的 y 轴截断起始于 ~55%，视觉上放大了 CLS–CWM 差异。建议标注 y 轴起点或在 caption 中提醒。\n\n- **M4**: §3.3 scaling analysis 仅使用 2 个种子（42, 123）比较 4B→8B。CWM 的 -0.03pp 变化被解读为 \"flat scaling\"，但 2 个种子的 power 极低。建议避免做定性推断（如 \"CWM flat scaling may reflect suboptimal hyperparameter transfer\"）或明确标注这是 exploratory observation。\n\n- **M5**: References 中 Xia et al. (2024) Agentless 标注 year=2025 但引用中写 2024。应统一。\n\n---\n\n## Questions to Authors\n\n**Q1**: TOST p=0.007 是否确实是 CLS–CWM 的结果（如 abstract/conclusion 所述），还是 CLS–TRAJ 的结果（如 §3.4 和 Table 15 所示）？如果是后者，CLS–CWM 是否有单独的 TOST 检验？\n\n**Q2**: 是否可以提供 Qwen3-8B CWM 在 epoch 1 或 step 400 附近 checkpoint 的 repo-level 评估结果？这对理解 CWM 的 \"真实\" 性能非常关键。\n\n**Q3**: Oracle 互补性分析是否可以扩展到多种子？至少 function-level 有 5 个种子的数据。\n\n**Q4**: 对于 mixed-effects LPM，是否检验过 logistic regression 的结果是否一致（即便 Angrist & Pischke 理论上保证了一致性，实际验证能增强可信度）？\n\n---\n\n## Missing References\n\n- Ding et al. (2024) \"RepoExec: Evaluate Code Generation with a Repository-Level Executable Benchmark\" — 与本文的 repo-level verification 高度相关但未引用\n- Chen et al. (2024) \"Benchmarking the Role of LLM-based Verifiers in Code Generation\" — 直接比较不同 verifier formulations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条 Weakness/Question，使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 也请简要标注是否同意。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 代码验证 formulation（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分），在 matched conditions 下使用两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（函数级/仓库级）、多种随机种子进行 ≤8B LoRA 微调。主要发现：(1) 函数级 CLS 和 CWM 近乎等价；(2) 仓库级 CLS 显著优于 CWM（18–26pp），主要因 format collapse；(3) 错误互补性暗示集成潜力。论文统计方法论全面（TOST、clustered bootstrap、mixed-effects LPM、Holm-Bonferroni），并附有大量消融实验和 threats-to-validity 分析。\n\n---\n\n## Strengths\n\n**S1.** 实验框架设计严谨，真正做到了 matched comparison：固定模型容量、训练数据、compute，仅改变 formulation。这在该领域是首次，填补了重要空白。（§1, §3.1）\n\n**S2.** 统计方法论选择恰当且多层次：(a) clustered bootstrap（114 clusters, 10K resamples）正确处理了 within-problem correlation（ICC = 0.191, DEFF = 3.97）；(b) TOST 等价检验搭配 SESOI 框架，先于观测数据设定 margin；(c) mixed-effects LPM 正式检验 formulation×complexity 交互效应（z = −23.7）；(d) Holm-Bonferroni 校正控制 family-wise error。四层统计工具形成了完整的证据链。（§3.2–3.5, Appendix K）\n\n**S3.** Failure mode taxonomy（Table 4: format collapse / decision collapse / aggregation penalty）不仅是描述性的，而且为每种 formulation 的适用边界提供了可操作的诊断标准。这比单纯报告准确率数字更有价值。（§3.5, Table 4）\n\n**S4.** 对 CWM 退化的诊断极为彻底：四种干预（rank 32、majority voting、relaxed matching、model scaling）全部失败，加上意外训练 artifact（CWM 模型在 CLS 格式数据上恢复 86.05%）、convergence analysis（eval loss 在 5% training 后单调增加），共同排除了多种替代解释，锁定了 formulation-level bottleneck。（Appendix H(c)(g), Table 16）\n\n**S5.** Threats to Validity 分析（§3.7 + Appendix N）对五个 confound 逐一量化，包括 checkpoint selection（<1pp）、eval sequence length（~1.5pp）、preprocessing（~8pp）等，并计算了 worst-case compounding（~11.5pp），显示 18–26pp gap 仍有 ≥7.5pp margin。这种量化式的 threats 分析在实证论文中很少见。\n\n**S6.** Oracle accuracy-utility framework（§2.3, Appendix A）从理论上推导了 per-test advantage 集中在 multi-F2P 实例的预测，并用 SWE-bench Verified 数据验证（T=2 贡献 55.3% 的总 advantage），理论与实验吻合。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **TOST 检验结果被错误归属于 CLS–CWM 比较**\n\n- **具体位置**: Abstract（第1段）、Conclusion §5（第1段）\n- **问题**: Abstract 声称 \"CLS and CWM are statistically equivalent across both families (TOST, 5 seeds)\"；Conclusion 进一步给出 \"CLS and CWM are statistically equivalent (TOST p=0.007, 5 seeds)\"。然而，§3.4 标题为 \"Per-Test vs. Trajectory-Level Equivalence\"，明确执行的 TOST 检验对象是 **CLS vs TRAJ**（\"We compare CLS (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds\"），得到 p=0.007。Table 15（Holm-Bonferroni）中 Rank 2 也标注为 \"Func: CLS vs TRAJ (TOST ±2pp)\"。全文没有任何位置报告对 CLS–CWM 的正式 TOST 检验。\n- **为什么影响接收**: 这是论文第一条 contribution 的核心统计证据。将 CLS–TRAJ 的 p 值错误标注为 CLS–CWM 的结果，构成了 abstract 和 conclusion 中的事实性错误。审稿人无法区分这是 (a) 笔误（将 TRAJ 写成了 CWM），还是 (b) CLS–CWM 等价从未被正式检验。两种情况都需要修正。\n- **建议修改方向**: (1) 对 CLS–CWM 补做正式 TOST 检验并报告 p 值（考虑到 gap 仅 0.02–1.24pp，预期会通过 ±2pp margin）；(2) 在 abstract/conclusion 中准确标注哪个比较产生了 p=0.007；(3) 在 Holm-Bonferroni 表中加入 CLS–CWM TOST，相应更新 k 值。\n\n**N2** [critical] **CWM formulation 的实验条件对其系统性不利，但结论却以 formulation-general 的方式表述**\n\n- **具体位置**: Title、Abstract、§5 Conclusion\n- **问题**: 论文标题 \"The Formulation Design Space\" 暗示对 formulation 的一般性比较，conclusion 推荐 \"at repository level under ≤8B LoRA, CLS is recommended\"。然而 CWM formulation 面临多重系统性劣势：(a) 所有 CWM repo-level runs 产生 NaN validation loss，被迫使用 final epoch checkpoint，而 convergence analysis（Table 16）显示此时 eval loss 已达最优值的 1.8 倍；(b) CWM 的 max_new_tokens=512 限制了有效输入上下文至 ~1,536 tokens，而 CLS 使用 5,120–8,192 tokens；(c) 原始 CWM（Meta, 2025）使用 32B 参数 + execution trace mid-training，与本文的 ≤8B LoRA 微调条件根本不同。虽然 §3.7 和 Limitations 有提及，但 abstract/conclusion 的 hedging 不够充分——读者可能误以为 \"CWM as a formulation\" 在 repo level 天生不行，而实际上是 \"CWM under ≤8B LoRA without execution-trace pretraining\" 不行。\n- **为什么影响接收**: ARR soundness 要求 claims 与 evidence 对齐。当前的 framing 在 abstract 级别可能误导读者对 CWM formulation 本身能力的判断。\n- **建议修改方向**: (1) 在 abstract 中明确 \"under our ≤8B LoRA protocol\" 限定所有 repo-level CWM 结论（当前 conclusion 有此 qualifier 但 abstract 更模糊）；(2) 在 §3.5 的 formulation divergence 段落中，增加一段讨论：如果 CWM 使用 early-stopped checkpoint（如 DeepSeek epoch 1 的 75.45%），gap 如何变化——当前 75.45% 仍落后于 CLS 的 ~84%，但 gap 从 ~26pp 缩至 ~9pp，这改变了 effect size 的定性解读；(3) 明确区分 \"formulation-level conclusion\"（generation 面临 output complexity 瓶颈）和 \"regime-specific conclusion\"（18–26pp gap 的具体数值）。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Repo-level variant 样本量 n=48 导致多个关键比较严重欠 power**\n\n- **具体位置**: §3.5（Table 3）、§3.6（Analysis）、Appendix J（Table 14）\n- **问题**: 所有 repo-level variant-level 分析基于 n=48（48 个 SWE-bench Verified variants）。论文自报 MDE ≈ 25pp（Appendix J），意味着只有 >25pp 的效应才能被检测到。CLS–TRAJ 在 repo level 的 gap（<10pp）完全落在 MDE 以下，论文却在 §5 conclusion 中推荐 CLS \"for both accuracy and throughput\"——这个推荐隐含了 CLS ≥ TRAJ 的假设，但该假设在当前样本量下无法被检验。\n- **建议**: (1) 在 conclusion 的推荐中明确 CLS–TRAJ 比较在 variant level 是 underpowered 的，当前推荐主要基于 CLS 的 throughput 优势和 per-test 诊断能力，而非 accuracy 优势；(2) 报告 repo-level variant-level 分析所需的样本量（power analysis），给后续研究提供参考。\n\n**W2** [warning] **Oracle 互补性估计均为单种子、无置信区间**\n\n- **具体位置**: §3.6（\"oracle routing reaches 95.83% variant accuracy\"）、Abstract/§5\n- **问题**: Contribution 3（error complementarity）的核心数字——函数级 oracle 90.63%（+2.80pp）和 repo 级 95.83%（+14.58pp）——均来自单一种子（seed 42）。在 n=48 repo variants 上，95.83% 意味着 46/48 正确，仅 2 个错误。这个估计的 binomial 95% CI 大约为 [85.7%, 99.5%]，非常宽。论文将这些数字作为 \"the strongest practical argument for exploring the formulation design space\"（§1）和 conclusion 中的核心方向，但没有提供任何不确定性量化。\n- **建议**: (1) 在 repo-level oracle 数字旁加上 bootstrap/binomial CI；(2) 在 abstract/conclusion 中标注 \"single-seed estimate\"（conclusion 已有，abstract 没有）；(3) 多种子 oracle 分析（至少 function level 可以做，有 5 个种子）。\n\n**W3** [warning] **TOST 种子池中混合 bfloat16 和 NF4 量化精度**\n\n- **具体位置**: §3.4（\"Seeds 789 and 0 use NF4 quantized inference\"）\n- **问题**: 5 个种子中 3 个使用 bfloat16、2 个使用 NF4 量化。论文将它们合并计算 TOST。虽然脚注指出 \"Restricting to bfloat16 seeds only yields p=0.128: consistent in direction but underpowered\"，但这恰恰说明 NF4 种子对 p 值的贡献是决定性的（从 0.128 降至 0.007）。问题在于：NF4 种子的加入不仅增加了样本量（提供 power），还可能系统性地缩小 CLS–TRAJ gap（如果 NF4 对两种 formulation 的影响不同）。论文未检验 precision × formulation 交互效应。\n- **建议**: (1) 报告 NF4-only 子集的 CLS–TRAJ gap（2 种子）与 bfloat16-only 子集（3 种子）的对比；(2) 或在 mixed-effects 模型中加入 precision 作为固定效应，检验其是否显著调节 formulation 效应。\n\n**W4** [warning] **CWM 的 checkpoint selection 没有与 CLS 对等的消融**\n\n- **具体位置**: §3.7 Threats、Appendix N\n- **问题**: CLS 有 checkpoint 消融（epoch 1/val-selected/final，range <1pp）。CWM 因所有 runs 产生 NaN val loss，全部使用 final epoch checkpoint。Convergence analysis（Table 16）显示 CWM eval loss 在 step 300–400 达到最小值，此后单调增加至 1.8× 最优。DeepSeek epoch-1 CWM 达到 75.45%（vs epoch-3 的 57.31%），这是 +18.14pp 的差异。但论文没有对 Qwen3 CWM 做同样的 early-stopping 消融，而 Qwen3 是 primary model family。如果 Qwen3 CWM early-stopped 也能达到 ~75%，则 CLS–CWM gap 从 ~18pp 缩至 ~10pp，显著改变结论的力度。\n- **建议**: (1) 对 Qwen3-8B CWM 补做 epoch-1 checkpoint 的评估（至少一个种子）；(2) 在 §3.7 中量化 CWM checkpoint selection confound 的 upper bound（当前只量化了 CLS 的）。\n\n---\n\n### Minor 问题（不影响接收）\n\n- **M1**: Mixed-effects LPM（§3.5, Appendix L）使用二元因变量但未提及是否使用了 robust standard errors（如 HC1/HC3）。在 n=56K 下影响可能很小，但 Angrist & Pischke (2009) 自己也建议对 LPM 使用 robust SEs。建议在 Appendix L 中添加一句说明。\n\n- **M2**: Prompt templates 仅定性描述（Appendix E：\"CLS uses a binary classification template\"），具体 template 文本指向 code repository。对于 reproducibility，建议在 appendix 中至少展示每种 formulation 的一个完整 prompt 示例。\n\n- **M3**: Figure 2 的 y 轴截断起始于 ~55%，视觉上放大了 CLS–CWM 差异。建议标注 y 轴起点或在 caption 中提醒。\n\n- **M4**: §3.3 scaling analysis 仅使用 2 个种子（42, 123）比较 4B→8B。CWM 的 -0.03pp 变化被解读为 \"flat scaling\"，但 2 个种子的 power 极低。建议避免做定性推断（如 \"CWM flat scaling may reflect suboptimal hyperparameter transfer\"）或明确标注这是 exploratory observation。\n\n- **M5**: References 中 Xia et al. (2024) Agentless 标注 year=2025 但引用中写 2024。应统一。\n\n---\n\n## Questions to Authors\n\n**Q1**: TOST p=0.007 是否确实是 CLS–CWM 的结果（如 abstract/conclusion 所述），还是 CLS–TRAJ 的结果（如 §3.4 和 Table 15 所示）？如果是后者，CLS–CWM 是否有单独的 TOST 检验？\n\n**Q2**: 是否可以提供 Qwen3-8B CWM 在 epoch 1 或 step 400 附近 checkpoint 的 repo-level 评估结果？这对理解 CWM 的 \"真实\" 性能非常关键。\n\n**Q3**: Oracle 互补性分析是否可以扩展到多种子？至少 function-level 有 5 个种子的数据。\n\n**Q4**: 对于 mixed-effects LPM，是否检验过 logistic regression 的结果是否一致（即便 Angrist & Pischke 理论上保证了一致性，实际验证能增强可信度）？\n\n---\n\n## Missing References\n\n- Ding et al. (2024) \"RepoExec: Evaluate Code Generation with a Repository-Level Executable Benchmark\" — 与本文的 repo-level verification 高度相关但未引用\n- Chen et al. (2024) \"Benchmarking the Role of LLM-based Verifiers in Code Generation\" — 直接比较不同 verifier formulations"
  }
}
```

</details>

---


### Tool result

_source line 634 · 2026-05-22T13:52:24.030164+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 95867
}
```

</details>

---
