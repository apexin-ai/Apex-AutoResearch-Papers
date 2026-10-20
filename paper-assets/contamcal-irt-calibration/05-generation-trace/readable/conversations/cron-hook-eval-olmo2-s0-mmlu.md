# cron hook eval olmo2 s0 mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/cron_hook_eval_olmo2_s0_mmlu.jsonl`
- **Structured JSON:** [`ae61ecd8d76fc047faec.json`](../../sessions/ae/ae61ecd8d76fc047faec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-21T19:53:32.216763+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #25。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-29999 `[0,1,2,3]`，cqa1-21977 `[0]`。禁用白名单外 GPU
- 投稿截止 **EMNLP 2026 ARR May 25**（D+3），当前处于 Round 10 内审等待阶段，**不要启动新 GPU 实验**除非 Director 明确指示
- evaluate.py 版本：MMLU/ARC 用 cqa1 版 (37591 bytes, MD5 `001a9bc23f808c47d25ef9eaeecb81f1`)。GSM8K appendix 统一用 37775 版 + caveat
- 跨 benchmark 对比**必须用 bootstrap 均值**，不能用单 seed（D190 教训：OLMo-2 单 seed s123 产生伪方向反转）
- OLMo-2 d000 baseline 53.79% 已验证正确（D210），不要再质疑

### 2. 🖥️ 基础设施快照
- **westd-29999**: 4× RTX PRO 6000 Blackwell，工作目录 `/root/contamcal-irt-calibration`，全部空闲
- **cqa1-21977**: 1× RTX 4090 D，工作目录 `/root/contamcal-irt-calibration`，空闲
- eval 结果统一目录：`eval_results_v2/`（s0 数据已从 `results/` 复制归一化）
- 活跃进程：无。无 tmux session、无 cron 任务
- Registry: 0 RUNNING / 0 PENDING / 37 PREPARING（绝大多数为历史遗留/已被后续实验取代）

### 3. 📊 当前状态
- **Round 9 (3.5 Borderline Conference) Action Matrix 全部执行完毕**：3 Must-Fix + 6 Should-Fix 全部 resolved
- **Round 10 内审已提交**（continue mode），等待审批返回
- LLaMA-3.1-8B out-of-sample validation 完成：分类 Immune，6 family taxonomy 确立（Immune×2 / Collapse×1 / V-recovery×1 / Benefit×2）
- Bootstrap CI 分析全部完成并审计通过：5 家族 n=3 BCa，Dir-Con 4/5
- 新增 Appendix W（参数化 DR 建模）和 Appendix X（s_ij classification）
- 编译通过：19 页（main 8 页），0 critical warnings
- 总计：268 success / 10 negative / 63 failed / 357 experiments
- **无运行中 Worker**，无等待回调

### 4. 📋 待办（条件触发式）
- Round 10 内审返回 → 按 Action Matrix 处理反馈（参考 D213: P(γ<0) 差异根因分析等）
- Director 批准终稿 → May 24-25 提交
- 若 Round 10 要求 P(γ<0) 重跑 → 用 j16_qwen 池在 westd 执行（D214）
- 低优先级 time-permitting 项（R8-W1 术语统一 / R8-W2 skewed sim / R8-W3 heatmap / R8-M1 references / R3-N3 ARC PPP / R8-M2 Figure 1 error bars）→ 仅在 Director 明确要求时处理

### 5. 🎯 战略上下文
- **核心结论**：SFT-route contamination 产生 family-dependent dose-response，4-pattern taxonomy（Immune/Collapse/V-recovery/Benefit）在 6 families × 2 benchmarks × 3 seeds 上得到验证
- **决策链关键节点**：D149（dose-response profiling 为 primary contribution）→ D181（vulnerability gradient 替代 sharp threshold）→ D184（4-pattern 命名确定）→ D207（LLaMA-3 Immune 确认 6th family）→ D211/D213（Round 9/10 action matrix）
- **易错点 1**：37 个 PREPARING 实验绝大多数是早期 ≤3B 规模或历史重试，**不要试图提交它们**——当前论文 scope 是 7B-14.7B 五/六家族
- **易错点 2**：Gemma-2 ARC 数据有 s42 oscillation artifact（d005=77.82→d025=87.37→d050=71.08），论文中 Gemma-2 ARC s42 excluded，用 s0/s123 数据
- **易错点 3**：GSM8K 数据仅入 Appendix（单 seed + evaluate.py 版本差异），不入主表。Qwen-14B GSM8K 跨 seed 方差 15.85pp 不足以支撑主表 claim
- **距投稿 3 天**，当前唯一阻塞项是 Round 10 内审结果。GPU 全部空闲是正常的——实验阶段已结束，现在是 paper finalization 阶段

## 项目硬约束 (memory.md 节选)

## (c) C009 约束状态

**建议**：将 C009 参考 hash 统一为 cqa1 版本 `001a9bc23f808c47d25ef9eaeecb81f1` (37591 bytes)

---

# OLMo-2 Baseline 验证 (2026-05-21 全量 Rerun 完成)

## Rerun 结果（eval_olmo2_s42_rerun, GPU 3, 37775 版 evaluate.py, adapter 加载确认）

| Dosage | MMLU (rerun) | MMLU (paper) | Δ | ARC (rerun) | ARC (paper) | Δ |
|--------|-------------|-------------|-----|------------|------------|-----|
| d000 | 53.79 | 53.79 | 0.00 ✅ | 76.11 | 76.11 | 0.00 ✅ |
| d005 | 56.14 | 55.89 | +0.25 | 76.62 | 76.62 | 0.00 ✅ |
| d025 | 56.17 | 57.73 | -1.56 ⚠️ | 78.16 | 78.16 | 0.00 ✅ |
| d050 | 57.25 | 57.44 | -0.19 | 79.61 | 79.61 | 0.00 ✅ |
| d100 | 57.00 | 58.60 | -1.60 ⚠️ | 80.03 | 80.03 | 0.00 ✅ |

## 可查的历史
前 214 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T19:53:44.381840+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T19:53:44.432469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T19:53:47.396595+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T19:53:48.351815+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PENDING'}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PENDING'}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T19:53:48.352255+00:00_

called mcp__agent-ml-research__reconcile_crons

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons</summary>

```json
Arguments not recorded in this source.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T19:53:48.804494+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9431}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1407
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T19:53:48.804921+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T19:53:49.156138+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T19:53:49.460096+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.104}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1108
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T19:53:49.611614+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 1259
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T19:53:49.662617+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\n- sft_llama3_8b_s0_validation: Out-of-sample taxonomy validation: LLaMA-3.1-8B (base) as 6th family. 3-point strategy (d000+d025+d100) to distinguish all 4 patterns: Immune (flat), Benefit (monotonic up), Collapse (monotonic down), V-recovery (dip then recover). Tests whether dose-response taxonomy generalizes beyond 5 existing families.（准备中）\\n- eval_gemma2_gsm8k_d000_s0: Gemma-2 d000 s0 GSM8K: baseline dosage cross-benchmark eval. Establishes Gemma-2 GSM8K baseline for dose-response comparison.（准备中）\\n- eval_qwen14b_gsm8k_d050_s0: Qwen-14B d050 s0 GSM8K: intermediate dosage cross-benchmark eval. Completes Qwen-14B GSM8K dose-response table (d000=74.98, d005=71.19, d025=79.30, d050=?, d100=running).（准备中）\\n- eval_gemma2_arc_s0: Gemma-2 s0 ARC 25-shot eval for d000-d050 (partial); d100 pending retrain completion（准备中）\\n- sft_gemma2_s0_sweep_v2（准备中）\\n- gsm8k_phi4_s42_westd: GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.（准备中）\\n- phase2_eval_gpu3_gemma_olmo: Phase 2 eval batch: Gemma-2 d005-d100 + OLMo-2 d000-d100 with fixed evaluate.py on westd cuda:3（准备中）\\n- phase2_eval_gpu1_qwen14b: Phase 2 eval batch: Qwen2.5-14B d000-d100 with fixed evaluate.py on westd cuda:1（准备中）\\n- …另有 27 项\\n\\n## 近期结论\\n- **eval_olmo2_s42_rerun** (success): OLMo-2 d000
…[truncated 4421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 857
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T19:53:49.663281+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-21 17:03 UTC | 更新原因: Round 9 Action Matrix fully executed; Round 10 review submitted\\n\\n> 目标: EMNLP 2026 ARR May 25 | **D+3**\\n\\n## 核心方向\\nSFT-route benchmark contamination 产生 family-dependent dose-response profiles。**4-pattern empirical taxonomy**: Immune / Collapse / V-recovery / Benefit。详见 paper_framing.md。\\n\\n## 当前状态\\n- **Round 9 (3.5 Borderline Conference) Action Matrix 全部执行完毕**\\n- 3 Must-Fix ✅: 参数化 DR 建模 (Appendix W)、因果语言→family-level factors、N=5 preliminary taxonomy + §5.1 事实修正\\n- 6 Should-Fix ✅: LoRA r=16 Limitations、65-70% scoping、s_ij classification (Appendix X)、Schaeffer comparison (§6)、OLMo-2 GSM8K seed annotation、DiD power caveat\\n- 编译通过: 19 页 (main text 8 页), 0 critical warnings\\n- **Round 10 内审已提交** (continue mode, 待批准)\\n\\n## 已完成任务\\n- [x] Agent: 参数化 DR 模型选择 (Constant/Linear/Quadratic/Hill, AICc) → Appendix W\\n- [x] Agent: s_ij exposure score classification (S1 AUC 0.93-0.99) → Appendix X  \\n- [x] Paper Agent: 全部 14 项文本修订 (P0+P1+P2) + 2 新 appendix sections\\n- [x] review_issues.yaml 更新: R9-N1/N2/S1/S2 resolved; R8-N2 resolved; R2-W6 resolved\\n\\n## 剩余流程\\n- [ ] Round 10 内审返回 → 处理反馈\\n- [ ] 终稿提交 (May 24-25)\\n\\n## 低优先级待定 (time permitting)\\n- R8-W1: Bayesian/frequentist 术语统一\\n- R8-W2: right-skewed exposure simulation\\n- R8-W3: Algorithm 1 sensitivity heatmap\\n- R8-M1: Golchin/Sainz/Yang references\\n- R3-N3 R9 action: ARC PPP main text discussion\\n- R8-M2 R9 actions: Figure 1 error bars, Table 2 'Con.' column, holland year\\n\\n## Taxonomy (6 families)\\nImmune ×2 (Phi-4, LLaMA-3) | Collapse ×1 (Qwen-14B) | V-recovery ×1 (Qwen-7B) | Benefit ×2 (Gemma-2, OLMo-2)\\n\\n## GPU 预算\\n- westd: 4× RTX PRO 6000 Blackwell — 全部空闲（无新 GPU 实验）\\n- cqa1: 1× RTX 4090 D — 空闲\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 507
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T19:54:03.728693+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 0/5 在用 (westd 4×空闲, cqa1 1×空闲) | Worker 0 | 磁盘: 未检查（无活跃实验）\n\n**Loop #25 Session Start — D+3**\n\n状态确认：\n- 0 RUNNING / 0 PENDING / 0 active crons\n- Round 9 Action Matrix 全部 resolved\n- Round 10 内审等待返回\n- 编译通过 19 页 (main 8), 0 critical warnings\n\n**唯一阻塞项**: Round 10 内审结果。收到后立即按 Action Matrix 处理。\n\n待命中。",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 0/5 在用 (westd 4×空闲, cqa1 1×空闲) | Worker 0 | 磁盘: 未检查（无活跃实验）\n\n**Loop #25 Session Start — D+3**\n\n状态确认：\n- 0 RUNNING / 0 PENDING / 0 active crons\n- Round 9 Action Matrix 全部 resolved\n- Round 10 内审等待返回\n- 编译通过 19 页 (main 8), 0 critical warnings\n\n**唯一阻塞项**: Round 10 内审结果。收到后立即按 Action Matrix 处理。\n\n待命中。",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T19:54:07.801581+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_olmo2_s0_mmlu",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 4072
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T19:54:15.097706+00:00_

初始化完毕。状态：Round 10 内审等待中，D+3 投稿截止，无活跃实验/Worker/cron。已向 Director 汇报。待命等待 Round 10 反馈或 Director 指令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_olmo2_s0_mmlu"
}
```

</details>

---
