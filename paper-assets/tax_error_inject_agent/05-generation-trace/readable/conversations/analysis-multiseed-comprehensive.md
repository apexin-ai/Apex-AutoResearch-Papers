# analysis multiseed comprehensive

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_multiseed-comprehensive_20260514T210150.jsonl`
- **Structured JSON:** [`0a57a24aaad872fc8771.json`](../../sessions/0a/0a57a24aaad872fc8771.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-14T21:05:08.020276+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-comprehensive_20260514T210150",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:05:08.020562+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-comprehensive_20260514T210150",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:05:08.020752+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/ 2>/dev/null | head -20",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-comprehensive_20260514T210150",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/ 2>/dev/null | head -20",
    "description": "List existing artifacts"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T21:05:08.020887+00:00_

_project
alfworld_data_survey.md
configs
data
diag_v4_taxei_recovery_eval.md
eval
injection
manifest.yaml
recovery.py
running_pids.md
v4-recovery-eval-dev
verl_agent_survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-comprehensive_20260514T210150",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T21:05:08.021037+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/d010_multiseed_analysis.md",
  "content": "# D010 Multi-Seed Validation & Recovery Eval 综合分析报告\n\n**日期**: 2025-05-14\n**实验**: D010 Phase 1 (Clean eval 多种子) + Phase 2 (Recovery eval)\n**评估集**: 47 tasks (ALFWorld)\n\n---\n\n## 1. 数据总览\n\n| 方法 | 训练数据量 | seed=42 | seed=0 | seed=123 | 均值 | SD | Range |\n|------|-----------|---------|--------|----------|------|-----|-------|\n| Vanilla SFT | 4,358 | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3 pp | 6.4 pp |\n| TaxEI SFT | 9,029 | 61.7% (29/47) | 46.8% (22/47) | — | **54.3%** | 10.5 pp | 14.9 pp |\n| Random SFT | 9,029 | 66.0% (31/47) | 55.3% (26/47) | — | **60.7%** | 7.6 pp | 10.7 pp |\n| Zero-shot | — | 42.6% (20/47) | — | — | **42.6%** | — | — |\n\n**注**: TaxEI/Random 仅有 2 个 seed，SD 基于 n-1=1 自由度，估计极不稳定。\n\n---\n\n## 2. 多种子稳定性分析\n\n### 2.1 跨 seed 波动\n\n| 方法 | SD (pp) | Range (pp) | CV (%) | 种子数 |\n|------|---------|------------|--------|--------|\n| Vanilla | 3.3 | 6.4 | 5.0% | 3 |\n| Random | 7.6 | 10.7 | 12.5% | 2 |\n| TaxEI | 10.5 | 14.9 | 19.4% | 2 |\n\n**观察**:\n- Vanilla 跨 seed 最稳定（SD=3.3 pp），三个 seed 均落在 61.7%–68.1% 的窄带内。\n- 注入训练方法（TaxEI/Random）的波动显著更大：TaxEI 的 range 达 14.9 pp，是 Vanilla 的 2.3 倍。\n- **但**: 2-seed SD 本质上就是 |x₁−x₂|/√2，自由度仅 1，不能可靠估计总体方差。Vanilla 有 3 seed 的 SD 也仅基于 df=2。这些 SD 的置信区间本身极宽。\n\n### 2.2 注入训练波动是否系统性更大？\n\n逐 seed 配对比较揭示了一个关键模式：\n\n| Seed | Vanilla | TaxEI | Random | Vanilla−TaxEI | Vanilla−Random |\n|------|---------|-------|--------|---------------|----------------|\n| 42 | 61.7% | 61.7% | 66.0% | **0.0 pp** | **−4.3 pp** |\n| 0 | 68.1% | 46.8% | 55.3% | **+21.3 pp** | **+12.8 pp** |\n\nSeed=42 时三种方法几乎无差异（甚至 Random > Vanilla）；seed=0 时注入方法大幅落后。这意味着 **方法差异与 seed 选择高度交互** — 不是一个稳定的主效应。\n\n**可能解释**:\n1. 注入数据放大了训练不稳定性：额外的 ~4,700 条注入样本引入了更多噪声，使模型对随机种子更敏感。\n2. Seed=0 碰巧是一个\"不利种子\"，对注入方法的影响不成比例地大。\n3. 样本量太小（n=47 eval tasks），评估本身的噪声掩盖了真实效应。\n\n---\n\n## 3. 方法间对比\n\n### 3.1 均值比较\n\n| 对比 | Δ均值 (pp) | Cohen's h | 效应大小 |\n|------|-----------|-----------|---------|\n| Vanilla vs Zero-shot | +22.7 | 0.46 | 接近中等 |\n| Vanilla vs TaxEI | +11.0 | 0.22 | 小 |\n| Vanilla vs Random | +4.6 | 0.09 | 可忽略 |\n| Random vs TaxEI | +6.4 | 0.13 | 可忽略 |\n| TaxEI vs Zero-shot | +11.7 | 0.23 | 小 |\n| Random vs Zero-shot | +18.1 | 0.37 | 小-中等 |\n\n### 3.2 个体运行的 95% 二项式置信区间 (Wilson)\n\n| 运行 | 点估计 | 95% CI |\n|------|--------|--------|\n| Vanilla seed=42 | 61.7% | [46.4%, 75.5%] |\n| Vanilla seed=0 | 68.1% | [52.9%, 80.5%] |\n| Vanilla seed=123 | 66.0% | [50.7%, 78.8%] |\n| TaxEI seed=42 | 61.7% | [46.4%, 75.5%] |\n| TaxEI seed=0 | 46.8% | [32.1%, 61.9%] |\n| Random seed=42 | 66.0% | [50.7%, 78.8%] |\n| Random seed=0 | 55.3% | [40.1%, 69.8%] |\n| Zero-shot | 42.6% | [28.3%, 57.8%] |\n\n**关键**: 每个 CI 宽度约 ±14 pp。大部分 CI 相互重叠。即使是 Vanilla 最好的 seed=0 (68.1%) 与 TaxEI 最差的 seed=0 (46.8%)，其 CI 仍有边缘重叠。\n\n### 3.3 均值的简易置信区间\n\n由于种子数极少（2-3），无法做 bootstrap。用 t 分布构造 CI：\n\n| 方法 | 均值 | SE | 95% CI (t-based) | df |\n|------|------|-----|------------------|----|\n| Vanilla | 65.3% | 1.9 pp | [57.1%, 73.4%] | 2 |\n| TaxEI | 54.3% | 7.5 pp | [−41.0%, 149.5%]* | 1 |\n| Random | 60.7% | 5.4 pp | [−7.8%, 129.1%]* | 1 |\n\n*df=1 时 t₀.₀₂₅=12.71，CI 完全没有意义。这证实 2-seed 设计对均值估计的统计功效为零。\n\n---\n\n## 4. D012 结论验证\n\n### D012 原始结论\n> \"注入训练系统性损害 clean performance\"\n\n### 新证据评估\n\n**支持 D012 的证据**:\n- TaxEI seed=0 (46.8%) 大幅低于 Vanilla seed=0 (68.1%)，差距 21.3 pp\n- Random seed=0 (55.3%) 也低于 Vanilla seed=0 (68.1%)，差距 12.8 pp\n- 两种注入方法在 seed=0 下均出现性能下降\n\n**反对 D012 的证据**:\n- TaxEI seed=42 (61.7%) = Vanilla seed=42 (61.7%)，差距 0.0 pp\n- Random seed=42 (66.0%) > Vanilla seed=42 (61.7%)，Random 反而更好 4.3 pp\n- Seed=42 下注入训练完全无害，甚至有益\n\n### 修正结论\n\n**D012 的\"系统性损害\"结论 premature（过早）**。更准确的描述是：\n\n> 注入训练增加了训练不稳定性，在某些 seed 下严重损害 clean performance（TaxEI seed=0 下降 21.3 pp），但在其他 seed 下无影响或轻微有益。\"系统性损害\"需要更多 seed 才能确认。\n\n### TaxEI seed=0 的 46.8% 是异常值还是趋势？\n\n**无法判定**。只有 2 个数据点：\n- 如果它是异常值 → TaxEI 真实均值接近 61.7%，与 Vanilla 无差异\n- 如果它是趋势 → TaxEI 真实均值约 54%，注入确实有害\n- 需要至少 3-5 个额外 seed 才能区分这两种情况\n\n类似地，Random seed=0 的 55.3% 同样面临相同的不确定性。\n\n---\n\n## 5. Recovery Eval 初步解读\n\n### 5.1 Vanilla Recovery 结果\n\n| 指标 | 值 | 含义 |\n|------|-----|------|\n| recovery_rate | 0.617 (29/47) | 61.7% 的错误注入 episode 中，模型成功纠正了注入的错误并完成任务 |\n| detection_rate | 0.0 (0/47) | 模型从未显式检测到/标记出注入的错误 |\n\n**解读**:\n- **Recovery without detection**: 模型通过通用问题解决能力（重试、换策略）恢复，而非通过识别错误类型。这是一种\"盲恢复\"——模型遇到失败后尝试替代路径，碰巧绕过了注入的错误。\n- recovery_rate=0.617 与 clean eval 的 seed=42 结果 (61.7%) 完全一致。这暗示 Vanilla 模型的 recovery 可能只是\"重新做一遍\"的 baseline 能力，而非真正的错误修复能力。\n\n### 5.2 对 TaxEI Recovery Eval 的预期\n\nTaxEI recovery eval 仍在运行 (17/47)。可能的结果及其含义：\n\n| TaxEI Recovery 结果 | TaxEI Detection 结果 | 解读 |\n|---------------------|---------------------|------|\n| recovery > 0.617 | detection > 0 | **正面**: taxonomy 训练同时提升了检测和恢复能力 |\n| recovery > 0.617 | detection = 0 | **部分正面**: taxonomy 提升了隐式恢复但未学会显式检测 |\n| recovery ≈ 0.617 | any | **中性**: taxonomy 训练对 recovery 无影响 |\n| recovery < 0.617 | any | **负面**: taxonomy 训练不仅损害 clean performance，还损害 recovery |\n\n**关键阈值**: TaxEI recovery_rate 需要 > 0.617 才能声称 taxonomy 在错误恢复上有价值。考虑到 TaxEI 的 clean eval 均值已低于 Vanilla（54.3% vs 65.3%），如果 recovery 也不优于 Vanilla，则 TaxEI 方案全面 negative。\n\n### 5.3 detection_rate=0 的深层含义\n\n所有方法 detection=0 意味着：\n1. 当前的 eval protocol 可能对\"检测\"的定义过于严格（需要显式输出特定标记？）\n2. 或者 SFT 训练根本不足以教会模型\"元认知\"——识别自己（或环境）的错误类型\n3. 如果 TaxEI 也是 detection=0，则 taxonomy-aware 训练在元认知层面完全失败\n\n---\n\n## 6. 统计功效讨论\n\n### 6.1 McNemar Test 的检测能力 (n=47)\n\nMcNemar test 基于 discordant pairs（两种方法结果不同的 task）。\n\n假设 discordant 比例为 30%（~14 tasks），80% power, α=0.05：\n- 需要 |b−c|² / (b+c) ≥ 3.84\n- 14 个 discordant pairs 中需要至少 11 vs 3 的分裂\n- 对应 accuracy 差异约 **17 pp** (8/47)\n\n假设 discordant 比例为 40%（~19 tasks）：\n- 需要至少 14 vs 5 的分裂\n- 对应约 **19 pp** 差异\n\n| 假设 discordant 率 | 可检测最小差异 (80% power) |\n|-------------------|-------------------------|\n| 20% (~9 pairs) | ~15 pp |\n| 30% (~14 pairs) | ~17 pp |\n| 40% (~19 pairs) | ~19 pp |\n\n### 6.2 当前观察效应 vs 检测阈值\n\n| 对比 | 观察 Δ (均值) | 逐 seed Δ 范围 | 可检测？ |\n|------|-------------|---------------|---------|\n| Vanilla vs TaxEI | 11.0 pp | 0.0 – 21.3 pp | **边缘**: seed=0 的 21.3 pp 可能可检测，seed=42 的 0 pp 不可能 |\n| Vanilla vs Random | 4.6 pp | −4.3 – 12.8 pp | **不可检测**: 远低于阈值 |\n\n### 6.3 多种子波动暗示的问题\n\n跨 seed 波动达 10-15 pp，这与方法间差异的量级相当。这意味着：\n\n1. **当前实验设计 underpowered**: 单个 seed 的结果包含约 ±7-10 pp 的训练随机性噪声（加上 ±7 pp 的评估噪声），总噪声可达 ±12-15 pp。方法间的真实差异需要远大于此才能被可靠检测。\n2. **最少需要 5+ seeds**: 要将均值的 SE 降到 3 pp 以下（使 10 pp 差异可检测），需要 SD²/n < 9，即 n > SD²/9 ≈ 110/9 ≈ 12 seeds（对 TaxEI）。即使是 Vanilla 的 SD=3.3，也需要 n≥3 seeds。\n3. **评估集太小**: n=47 tasks 本身就带来约 ±7 pp 的二项式噪声。扩大评估集到 100+ tasks 可将此噪声降到 ±5 pp。\n\n---\n\n## 7. 总结与建议\n\n### 7.1 可以确认的结论\n\n1. **所有 SFT 方法 > Zero-shot**: 全部 7 个 SFT 运行均超过 42.6% baseline，最低也有 46.8%。SFT 训练有效。\n2. **注入训练增加不稳定性**: TaxEI/Random 的跨 seed 波动（10-15 pp）明显大于 Vanilla（6 pp），尽管 2-seed 估计不够精确。\n3. **Vanilla recovery 是\"盲恢复\"**: detection_rate=0 表明恢复不依赖错误识别。\n\n### 7.2 不能确认的结论\n\n1. **\"注入训练系统性损害 clean performance\"**: Seed=42 下无损害，seed=0 下严重损害。证据不足以判定\"系统性\"。\n2. **TaxEI vs Random 的优劣**: 均值差 6.4 pp，但每种方法只有 2 个 seed，完全无法区分。\n3. **任何方法间的统计显著差异**: n=47 tasks × 2-3 seeds 的设计对 <15 pp 的效应完全 underpowered。\n\n### 7.3 如果要继续本方向\n\n| 改进 | 预期收益 | 成本 |\n|------|---------|------|\n| 为 TaxEI/Random 各补 3 个 seed (共 5 seeds) | 均值 SE 降到 ~4-5 pp | 6 次训练 + eval |\n| 扩大评估集到 134 tasks (ALFWorld 全集) | 二项式 SE 从 7pp 降到 4pp | 评估时间 ×3 |\n| 两者同时 | 总 SE < 4 pp，可检测 10 pp 差异 | 高 |\n\n### 7.4 当前证据的最诚实总结\n\n> 在 n=47, 2-3 seeds 的实验规模下，我们观察到注入训练 **可能** 损害 clean performance（均值下降 5-11 pp）并增加训练不稳定性，但效应大小与实验噪声（跨 seed 波动 10-15 pp）在同一量级，无法排除零效应的可能。Recovery eval 显示 Vanilla 模型已具备 61.7% 的盲恢复能力，TaxEI 的 recovery eval 结果将决定 taxonomy 方案是否有任何正面价值。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-comprehensive_20260514T210150",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/d010_multiseed_analysis.md",
    "content": "# D010 Multi-Seed Validation & Recovery Eval 综合分析报告\n\n**日期**: 2025-05-14\n**实验**: D010 Phase 1 (Clean eval 多种子) + Phase 2 (Recovery eval)\n**评估集**: 47 tasks (ALFWorld)\n\n---\n\n## 1. 数据总览\n\n| 方法 | 训练数据量 | seed=42 | seed=0 | seed=123 | 均值 | SD | Range |\n|------|-----------|---------|--------|----------|------|-----|-------|\n| Vanilla SFT | 4,358 | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3 pp | 6.4 pp |\n| TaxEI SFT | 9,029 | 61.7% (29/47) | 46.8% (22/47) | — | **54.3%** | 10.5 pp | 14.9 pp |\n| Random SFT | 9,029 | 66.0% (31/47) | 55.3% (26/47) | — | **60.7%** | 7.6 pp | 10.7 pp |\n| Zero-shot | — | 42.6% (20/47) | — | — | **42.6%** | — | — |\n\n**注**: TaxEI/Random 仅有 2 个 seed，SD 基于 n-1=1 自由度，估计极不稳定。\n\n---\n\n## 2. 多种子稳定性分析\n\n### 2.1 跨 seed 波动\n\n| 方法 | SD (pp) | Range (pp) | CV (%) | 种子数 |\n|------|---------|------------|--------|--------|\n| Vanilla | 3.3 | 6.4 | 5.0% | 3 |\n| Random | 7.6 | 10.7 | 12.5% | 2 |\n| TaxEI | 10.5 | 14.9 | 19.4% | 2 |\n\n**观察**:\n- Vanilla 跨 seed 最稳定（SD=3.3 pp），三个 seed 均落在 61.7%–68.1% 的窄带内。\n- 注入训练方法（TaxEI/Random）的波动显著更大：TaxEI 的 range 达 14.9 pp，是 Vanilla 的 2.3 倍。\n- **但**: 2-seed SD 本质上就是 |x₁−x₂|/√2，自由度仅 1，不能可靠估计总体方差。Vanilla 有 3 seed 的 SD 也仅基于 df=2。这些 SD 的置信区间本身极宽。\n\n### 2.2 注入训练波动是否系统性更大？\n\n逐 seed 配对比较揭示了一个关键模式：\n\n| Seed | Vanilla | TaxEI | Random | Vanilla−TaxEI | Vanilla−Random |\n|------|---------|-------|--------|---------------|----------------|\n| 42 | 61.7% | 61.7% | 66.0% | **0.0 pp** | **−4.3 pp** |\n| 0 | 68.1% | 46.8% | 55.3% | **+21.3 pp** | **+12.8 pp** |\n\nSeed=42 时三种方法几乎无差异（甚至 Random > Vanilla）；seed=0 时注入方法大幅落后。这意味着 **方法差异与 seed 选择高度交互** — 不是一个稳定的主效应。\n\n**可能解释**:\n1. 注入数据放大了训练不稳定性：额外的 ~4,700 条注入样本引入了更多噪声，使模型对随机种子更敏感。\n2. Seed=0 碰巧是一个\"不利种子\"，对注入方法的影响不成比例地大。\n3. 样本量太小（n=47 eval tasks），评估本身的噪声掩盖了真实效应。\n\n---\n\n## 3. 方法间对比\n\n### 3.1 均值比较\n\n| 对比 | Δ均值 (pp) | Cohen's h | 效应大小 |\n|------|-----------|-----------|---------|\n| Vanilla vs Zero-shot | +22.7 | 0.46 | 接近中等 |\n| Vanilla vs TaxEI | +11.0 | 0.22 | 小 |\n| Vanilla vs Random | +4.6 | 0.09 | 可忽略 |\n| Random vs TaxEI | +6.4 | 0.13 | 可忽略 |\n| TaxEI vs Zero-shot | +11.7 | 0.23 | 小 |\n| Random vs Zero-shot | +18.1 | 0.37 | 小-中等 |\n\n### 3.2 个体运行的 95% 二项式置信区间 (Wilson)\n\n| 运行 | 点估计 | 95% CI |\n|------|--------|--------|\n| Vanilla seed=42 | 61.7% | [46.4%, 75.5%] |\n| Vanilla seed=0 | 68.1% | [52.9%, 80.5%] |\n| Vanilla seed=123 | 66.0% | [50.7%, 78.8%] |\n| TaxEI seed=42 | 61.7% | [46.4%, 75.5%] |\n| TaxEI seed=0 | 46.8% | [32.1%, 61.9%] |\n| Random seed=42 | 66.0% | [50.7%, 78.8%] |\n| Random seed=0 | 55.3% | [40.1%, 69.8%] |\n| Zero-shot | 42.6% | [28.3%, 57.8%] |\n\n**关键**: 每个 CI 宽度约 ±14 pp。大部分 CI 相互重叠。即使是 Vanilla 最好的 seed=0 (68.1%) 与 TaxEI 最差的 seed=0 (46.8%)，其 CI 仍有边缘重叠。\n\n### 3.3 均值的简易置信区间\n\n由于种子数极少（2-3），无法做 bootstrap。用 t 分布构造 CI：\n\n| 方法 | 均值 | SE | 95% CI (t-based) | df |\n|------|------|-----|------------------|----|\n| Vanilla | 65.3% | 1.9 pp | [57.1%, 73.4%] | 2 |\n| TaxEI | 54.3% | 7.5 pp | [−41.0%, 149.5%]* | 1 |\n| Random | 60.7% | 5.4 pp | [−7.8%, 129.1%]* | 1 |\n\n*df=1 时 t₀.₀₂₅=12.71，CI 完全没有意义。这证实 2-seed 设计对均值估计的统计功效为零。\n\n---\n\n## 4. D012 结论验证\n\n### D012 原始结论\n> \"注入训练系统性损害 clean performance\"\n\n### 新证据评估\n\n**支持 D012 的证据**:\n- TaxEI seed=0 (46.8%) 大幅低于 Vanilla seed=0 (68.1%)，差距 21.3 pp\n- Random seed=0 (55.3%) 也低于 Vanilla seed=0 (68.1%)，差距 12.8 pp\n- 两种注入方法在 seed=0 下均出现性能下降\n\n**反对 D012 的证据**:\n- TaxEI seed=42 (61.7%) = Vanilla seed=42 (61.7%)，差距 0.0 pp\n- Random seed=42 (66.0%) > Vanilla seed=42 (61.7%)，Random 反而更好 4.3 pp\n- Seed=42 下注入训练完全无害，甚至有益\n\n### 修正结论\n\n**D012 的\"系统性损害\"结论 premature（过早）**。更准确的描述是：\n\n> 注入训练增加了训练不稳定性，在某些 seed 下严重损害 clean performance（TaxEI seed=0 下降 21.3 pp），但在其他 seed 下无影响或轻微有益。\"系统性损害\"需要更多 seed 才能确认。\n\n### TaxEI seed=0 的 46.8% 是异常值还是趋势？\n\n**无法判定**。只有 2 个数据点：\n- 如果它是异常值 → TaxEI 真实均值接近 61.7%，与 Vanilla 无差异\n- 如果它是趋势 → TaxEI 真实均值约 54%，注入确实有害\n- 需要至少 3-5 个额外 seed 才能区分这两种情况\n\n类似地，Random seed=0 的 55.3% 同样面临相同的不确定性。\n\n---\n\n## 5. Recovery Eval 初步解读\n\n### 5.1 Vanilla Recovery 结果\n\n| 指标 | 值 | 含义 |\n|------|-----|------|\n| recovery_rate | 0.617 (29/47) | 61.7% 的错误注入 episode 中，模型成功纠正了注入的错误并完成任务 |\n| detection_rate | 0.0 (0/47) | 模型从未显式检测到/标记出注入的错误 |\n\n**解读**:\n- **Recovery without detection**: 模型通过通用问题解决能力（重试、换策略）恢复，而非通过识别错误类型。这是一种\"盲恢复\"——模型遇到失败后尝试替代路径，碰巧绕过了注入的错误。\n- recovery_rate=0.617 与 clean eval 的 seed=42 结果 (61.7%) 完全一致。这暗示 Vanilla 模型的 recovery 可能只是\"重新做一遍\"的 baseline 能力，而非真正的错误修复能力。\n\n### 5.2 对 TaxEI Recovery Eval 的预期\n\nTaxEI recovery eval 仍在运行 (17/47)。可能的结果及其含义：\n\n| TaxEI Recovery 结果 | TaxEI Detection 结果 | 解读 |\n|---------------------|---------------------|------|\n| recovery > 0.617 | detection > 0 | **正面**: taxonomy 训练同时提升了检测和恢复能力 |\n| recovery > 0.617 | detection = 0 | **部分正面**: taxonomy 提升了隐式恢复但未学会显式检测 |\n| recovery ≈ 0.617 | any | **中性**: taxonomy 训练对 recovery 无影响 |\n| recovery < 0.617 | any | **负面**: taxonomy 训练不仅损害 clean performance，还损害 recovery |\n\n**关键阈值**: TaxEI recovery_rate 需要 > 0.617 才能声称 taxonomy 在错误恢复上有价值。考虑到 TaxEI 的 clean eval 均值已低于 Vanilla（54.3% vs 65.3%），如果 recovery 也不优于 Vanilla，则 TaxEI 方案全面 negative。\n\n### 5.3 detection_rate=0 的深层含义\n\n所有方法 detection=0 意味着：\n1. 当前的 eval protocol 可能对\"检测\"的定义过于严格（需要显式输出特定标记？）\n2. 或者 SFT 训练根本不足以教会模型\"元认知\"——识别自己（或环境）的错误类型\n3. 如果 TaxEI 也是 detection=0，则 taxonomy-aware 训练在元认知层面完全失败\n\n---\n\n## 6. 统计功效讨论\n\n### 6.1 McNemar Test 的检测能力 (n=47)\n\nMcNemar test 基于 discordant pairs（两种方法结果不同的 task）。\n\n假设 discordant 比例为 30%（~14 tasks），80% power, α=0.05：\n- 需要 |b−c|² / (b+c) ≥ 3.84\n- 14 个 discordant pairs 中需要至少 11 vs 3 的分裂\n- 对应 accuracy 差异约 **17 pp** (8/47)\n\n假设 discordant 比例为 40%（~19 tasks）：\n- 需要至少 14 vs 5 的分裂\n- 对应约 **19 pp** 差异\n\n| 假设 discordant 率 | 可检测最小差异 (80% power) |\n|-------------------|-------------------------|\n| 20% (~9 pairs) | ~15 pp |\n| 30% (~14 pairs) | ~17 pp |\n| 40% (~19 pairs) | ~19 pp |\n\n### 6.2 当前观察效应 vs 检测阈值\n\n| 对比 | 观察 Δ (均值) | 逐 seed Δ 范围 | 可检测？ |\n|------|-------------|---------------|---------|\n| Vanilla vs TaxEI | 11.0 pp | 0.0 – 21.3 pp | **边缘**: seed=0 的 21.3 pp 可能可检测，seed=42 的 0 pp 不可能 |\n| Vanilla vs Random | 4.6 pp | −4.3 – 12.8 pp | **不可检测**: 远低于阈值 |\n\n### 6.3 多种子波动暗示的问题\n\n跨 seed 波动达 10-15 pp，这与方法间差异的量级相当。这意味着：\n\n1. **当前实验设计 underpowered**: 单个 seed 的结果包含约 ±7-10 pp 的训练随机性噪声（加上 ±7 pp 的评估噪声），总噪声可达 ±12-15 pp。方法间的真实差异需要远大于此才能被可靠检测。\n2. **最少需要 5+ seeds**: 要将均值的 SE 降到 3 pp 以下（使 10 pp 差异可检测），需要 SD²/n < 9，即 n > SD²/9 ≈ 110/9 ≈ 12 seeds（对 TaxEI）。即使是 Vanilla 的 SD=3.3，也需要 n≥3 seeds。\n3. **评估集太小**: n=47 tasks 本身就带来约 ±7 pp 的二项式噪声。扩大评估集到 100+ tasks 可将此噪声降到 ±5 pp。\n\n---\n\n## 7. 总结与建议\n\n### 7.1 可以确认的结论\n\n1. **所有 SFT 方法 > Zero-shot**: 全部 7 个 SFT 运行均超过 42.6% baseline，最低也有 46.8%。SFT 训练有效。\n2. **注入训练增加不稳定性**: TaxEI/Random 的跨 seed 波动（10-15 pp）明显大于 Vanilla（6 pp），尽管 2-seed 估计不够精确。\n3. **Vanilla recovery 是\"盲恢复\"**: detection_rate=0 表明恢复不依赖错误识别。\n\n### 7.2 不能确认的结论\n\n1. **\"注入训练系统性损害 clean performance\"**: Seed=42 下无损害，seed=0 下严重损害。证据不足以判定\"系统性\"。\n2. **TaxEI vs Random 的优劣**: 均值差 6.4 pp，但每种方法只有 2 个 seed，完全无法区分。\n3. **任何方法间的统计显著差异**: n=47 tasks × 2-3 seeds 的设计对 <15 pp 的效应完全 underpowered。\n\n### 7.3 如果要继续本方向\n\n| 改进 | 预期收益 | 成本 |\n|------|---------|------|\n| 为 TaxEI/Random 各补 3 个 seed (共 5 seeds) | 均值 SE 降到 ~4-5 pp | 6 次训练 + eval |\n| 扩大评估集到 134 tasks (ALFWorld 全集) | 二项式 SE 从 7pp 降到 4pp | 评估时间 ×3 |\n| 两者同时 | 总 SE < 4 pp，可检测 10 pp 差异 | 高 |\n\n### 7.4 当前证据的最诚实总结\n\n> 在 n=47, 2-3 seeds 的实验规模下，我们观察到注入训练 **可能** 损害 clean performance（均值下降 5-11 pp）并增加训练不稳定性，但效应大小与实验噪声（跨 seed 波动 10-15 pp）在同一量级，无法排除零效应的可能。Recovery eval 显示 Vanilla 模型已具备 61.7% 的盲恢复能力，TaxEI 的 recovery eval 结果将决定 taxonomy 方案是否有任何正面价值。\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T21:05:08.021282+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/d010_multiseed_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-comprehensive_20260514T210150",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T21:05:08.021419+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "D010 Multi-Seed & Recovery Eval 综合分析",
  "type": "report",
  "description": "D010 Phase 1 多种子验证(Vanilla 3 seeds, TaxEI/Random 2 seeds)和 Phase 2 Recovery eval 的综合统计分析。包含稳定性分析、方法间对比(Cohen's h)、D012结论验证、recovery eval解读、统计功效讨论。核心发现：注入训练增加不稳定性(SD 10-15pp vs 3pp)，但\"系统性损害\"结论premature；n=47×2-3 seeds设计对<15pp效应underpowered。",
  "project": "tax_error_inject_agent",
  "exp_id": "D010",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/d010_multiseed_analysis.md",
  "tags": "['multi-seed', 'statistical-analysis', 'recovery-eval', 'D012-verification']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_multiseed-comprehensive_20260514T210150",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "D010 Multi-Seed & Recovery Eval 综合分析",
    "type": "report",
    "description": "D010 Phase 1 多种子验证(Vanilla 3 seeds, TaxEI/Random 2 seeds)和 Phase 2 Recovery eval 的综合统计分析。包含稳定性分析、方法间对比(Cohen's h)、D012结论验证、recovery eval解读、统计功效讨论。核心发现：注入训练增加不稳定性(SD 10-15pp vs 3pp)，但\"系统性损害\"结论premature；n=47×2-3 seeds设计对<15pp效应underpowered。",
    "project": "tax_error_inject_agent",
    "exp_id": "D010",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/d010_multiseed_analysis.md",
    "tags": "['multi-seed', 'statistical-analysis', 'recovery-eval', 'D012-verification']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T21:05:08.021618+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_c0db6f\", \"name\": \"D010 Multi-Seed & Recovery Eval 综合分析\", \"type\": \"report\", \"description\": \"D010 Phase 1 多种子验证(Vanilla 3 seeds, TaxEI/Random 2 seeds)和 Phase 2 Recovery eval 的综合统计分析。包含稳定性分析、方法间对比(Cohen's h)、D012结论验证、recovery eval解读、统计功效讨论。核心发现：注入训练增加不稳定性(SD 10-15pp vs 3pp)，但\\\"系统性损害\\\"结论premature；n=47×2-3 seeds设计对<15pp效应underpowered。\", \"path\": \"projects/tax_error_inject_agent/artifacts/D010/report/d010_multiseed_analysis.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": \"D010\", \"skill\": \"\", \"created_at\": \"2026-05-14T21:04:58.400163+00:00\", \"tags\": [\"multi-seed\", \"statistical-analysis\", \"recovery-eval\", \"D012-verification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_multiseed-comprehensive_20260514T210150",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-14T21:05:08.021802+00:00_

报告已写入并注册。核心发现：

1. **Vanilla 最稳定** (SD=3.3 pp)，注入方法波动 2-3 倍大 (TaxEI SD=10.5, Random SD=7.6)
2. **D012 "系统性损害" 结论 premature** — seed=42 下注入方法与 Vanilla 无差异甚至更好，seed=0 下才出现大幅下降。方法差异与 seed 高度交互，不是稳定主效应
3. **统计功效严重不足** — n=47 的 McNemar 需要 ~17 pp 才有 power，而观察效应 (11 pp 均值差) 与噪声 (10-15 pp 跨 seed 波动) 在同一量级
4. **Recovery eval**: Vanilla 61.7% 盲恢复 (detection=0)，TaxEI 结果将决定 taxonomy 是否有正面价值——如果 recovery ≤ 0.617 则全面 negative

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_multiseed-comprehensive_20260514T210150"
}
```

</details>

---
