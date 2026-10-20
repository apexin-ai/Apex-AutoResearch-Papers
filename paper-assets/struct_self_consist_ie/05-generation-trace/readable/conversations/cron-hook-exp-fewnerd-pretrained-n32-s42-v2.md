# cron hook exp fewnerd pretrained n32 s42 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/cron_hook_exp_fewnerd_pretrained_n32_s42_v2.jsonl`
- **Structured JSON:** [`e5c7aef20996b6c0eacb.json`](../../sessions/e5/e5c7aef20996b6c0eacb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-24T03:59:24.923040+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #20。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 仅限 autodl-5090 cuda:0-3（config 也含 autodl-5090-c cuda:0-3，但当前 servers 只列 autodl-5090）
- D244 决策：DDL eve 不启动新实验，4×5090 保留给 rebuttal 期间使用
- SciERC construction 指标：+0.32pp n.s.（单种子 seed42），不可 overclaim
- 三张表的 F1 基线不同：tab:scale_comparison 用 entity-type-averaged macro-F1(.667)；tab:selection 用 macro-F1(.645)；tab:fewnerd 用 instance-averaged(.663）——各表内部一致但不可混用
- autodl-5090 上 vLLM Unicode surrogate bug 尚未修复（autodl-5090-c 已修复），在 5090 跑新实验前需先同步 `sampling.py:673` 的 `errors='replace'` 修复
- 论文 N-scaling 图表必须用统一 instance 集 + 统一 greedy baseline（非各自独立解码的 greedy）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（主），autodl-5090-c（备用）
- 工作目录：`/root/autodl-tmp/struct_self_consist_ie`
- Python：aml-train 镜像，`/root/miniconda3/bin/python`（conda base 环境）
- 模型：qwen3-8b-fewnerd-exp021-merged（finetuned），Qwen2.5-7B-Instruct（pretrained）
- 匿名 repo commit：`58d1be8`
- 活跃进程：无（0 RUNNING，0 cron）
- GPU：4×RTX 5090 全部空闲

### 3. 📊 当前状态
论文 **submission-ready**，EMNLP 2026 DDL 是 2026-05-25。编译通过（46 pages, 0 errors），ARR checklist 15/15，匿名 repo 就绪。

- 0 个 RUNNING 实验
- 18 个 PREPARING 实验（rebuttal 备用池：entity verifier B2 系列、cross-task A1、signal routing E1、diversity/budget 系列等）
- R41 审稿已提交，等用户确认结果
- 最新审稿分数：R39 Fresh mode R1=3.5 / R2=3.0，realistic target 3.5 (Borderline Conference)

全部待办 blocked on 用户：OpenReview 提交、R41 确认、Figure 1 最终版。

### 4. 📋 待办（条件触发式）
- 用户完成 OpenReview 提交 → 确认提交成功，进入 rebuttal 准备模式
- R41 审稿结果返回 → 分析 reviewer comments，规划 rebuttal 实验（从 18 个 PREPARING 池中选最相关的）
- 收到 reviewer 质疑 epoch confound → 5-epoch 数据已就绪（memory.md 有完整对比），可直接引用
- 收到 reviewer 质疑 cross-task generalizability → 启动 exp_a1_spider_sql_sc（SQL on Spider）
- 收到 reviewer 质疑 entity verifier → 启动 exp_b2 系列（已有 4 个变体 PREPARING）
- autodl-5090 需要跑新实验前 → 先同步 vLLM unicode bug fix

### 5. 🎯 战略上下文
- **核心结论**：Self-Consistency 在 NER 上存在 correlation-selection gap——agreement signals（SJ, κ）与 correctness 正相关，但 MV 聚合无法利用这一相关性。Finetuned MV 负向（3 datasets），pretrained MV 正向（3 datasets）。Gap 是 model-intrinsic。
- **Framing 演化链**：D235→D236→D237→D238→D239→D240，最终收敛为 "NER diagnostic framework + correlation-selection gap"
- **易错点 1**：SciERC finetuned MV Δ = -0.50±0.74pp，方向不一致（s42 负、s123 正、s456 负），属于 noise regime——不可 claim MV hurts SciERC，只能说 n.s.
- **易错点 2**：3-epoch degen(8.8%) < pretrained degen(11.7%)——fine-tuning 与 degeneracy 关系非单调，叙事需处理
- **易错点 3**：18 个 PREPARING 实验是 rebuttal 备用，不要在 DDL 前启动（D244 决策）
- **研究已收敛（D243）**，当前阶段纯粹是等用户提交 + 准备 rebuttal

## 可查的历史
前 49 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-24T03:59:34.042825+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-24T03:59:34.093424+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T03:59:38.057871+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T03:59:38.610028+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PREPARING'}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PREPARING'}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T03:59:39.112073+00:00_

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
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T03:59:39.112533+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8709}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1054
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T03:59:39.564315+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T03:59:39.564738+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T03:59:39.866686+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_fewnerd_mf4v2_s123_v4\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T21:44:24.500Z\", \"updated_at\": \"2026-05-21T23:52:23.871Z\", \"hypothesis\": \"FewNERD MF4v2 s123 v4: regenerate finetuned FewNERD seed=123 instance-level samples.jsonl on autodl-5090-c for v4 MV unified recompute. N=8, T=1.0, seed=123. Model: qwen3-8b-fewnerd-exp021-merged. Parent retries v2 (failed on 5090) and v3 (killed). Using confirmed-working 5090-c environment from s456_v3.\", \"parent\": \"exp_fewnerd_mf4v2_s123_v2\", \"conclusion\": \"killed\"}, \"exp_fewnerd_mf4v2_s42_v4\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T21:44:21.426Z\", \"updated_at\": \"2026-05-21T23:52:22.502Z\", \"hypothesis\": \"Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.\", \"parent\": \"exp_fewnerd_mf4v2_s42_v2\", \"conclusion\": \"killed\"}, \"exp_fewnerd_mf4v2_s123_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:22:39.175Z\", \"updated_at\": \"2026-05-21T23:52:20.833Z\", \"hypothesis\": \"FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.\", \"conclusion\": \"killed\"}, \"exp_fewnerd_mf4v2_s42_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:22:37.754Z\", \"updated_at\": \"2026-05-21T23:52:19.142Z\", \"hypothesis\": \"FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=42, N=8, T=1.0.\", \"conclusion\": \"killed\"}, \"eval_scd_fewnerd_fallback\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T19:11:25.544Z\", \"updated_at\": \"2026-05-21T23:52:13.602Z\", \"conclusion\": \"killed\"}, \"exp_a1_spider_sql_sc\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T18:15:12.865Z\", \"updated_at\": \"2026-05-21T23:52:12.126Z\",
…[truncated 14763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1256
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T03:59:39.917469+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 805
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T03:59:39.918019+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-23\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp_fewnerd_mf4v2_s123_v4: FewNERD MF4v2 s123 v4: regenerate finetuned FewNERD seed=123 instance-level samples.jsonl on autodl-5090-c for v4 MV unified recompute. N=8, T=1.0, seed=123. Model: qwen3-8b-fewnerd-exp021-merged. Parent retries v2 (failed on 5090) and v3 (killed). Using confirmed-working 5090-c environment from s456_v3.（准备中）\\n- exp_fewnerd_mf4v2_s42_v4: Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.（准备中）\\n- exp_fewnerd_mf4v2_s123_v2: FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.（准备中）\\n- exp_fewnerd_mf4v2_s42_v2: FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=42, N=8, T=1.0.（准备中）\\n- eval_scd_fewnerd_fallback（准备中）\\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.（准备中）\\n- exp_b2_v3_domain_invariant: Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improv
…[truncated 4377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 353
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T03:59:39.968634+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\", \"content\": \"# struct_self_consist_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-24 01:58 UTC | 更新原因: 全部修复完成，论文 submission-ready，待办全部 blocked on 用户\\n\\n## 核心方向\\n**Self-Consistency for NER: Correlation-Selection Gap 诊断与分析**。详见 paper_framing.md。\\n\\n## 当前阶段\\n**🔴 DDL Sprint — EMNLP 2026 DDL 2026-05-25 (明天)**\\n\\n## 目标校准\\n- **Realistic target: 3.5 (Borderline Conference)**\\n- 当前 Fresh mode 最高 R1=3.5 / R2=3.0 (R39)\\n\\n## 审稿历史\\n| Round | Mode | Score | 关键问题 |\\n|-------|------|-------|---------|\\n| R39 | Fresh | 3.0 (R1=3.5, R2=3.0) | 页数溢出+epoch confound+novelty |\\n| R41 | Continue | **submitted, 待用户确认** | 全部修复+n16/n32整合 |\\n\\n## 论文状态：✅ SUBMISSION-READY\\n- 编译：46 pages, 0 errors, 0 undefined refs, 主文 ≤ 8 pages\\n- 匿名 repo：commit `58d1be8`（补齐缺失文件 + response letter 修正 + caption 脚注）\\n- Reviewer 验证：所有数值一致，格式合规，匿名通过\\n- Response letter：过时数据已修正（SciERC +0.32pp, selective prediction 引用 appendix）\\n- ARR checklist：15/15\\n\\n## 待办（全部 blocked on 用户）\\n- [ ] 用户在 OpenReview 提交\\n- [ ] 用户确认 R41 审稿模式（可选）\\n- [ ] 用户确认 Figure 1 最终版（可选）\\n\\n## GPU 预算\\nautodl-5090: 4×RTX 5090，全部空闲。研究已收敛（D243），18 个 PREPARING 实验留作 rebuttal 备用。\\n\\n## 硬约束\\n- GPU 仅限 autodl-5090 cuda:0-3\\n- SciERC construction 保持 +0.32pp n.s.（单种子 seed42）\\n- tab:scale_comparison: entity-type-averaged macro-F1（.667）；tab:selection: macro-F1（.645）；tab:fewnerd: instance-averaged（.663）——各表内部一致\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D244 | 2026-05-24 | DDL eve GPU 决策：不启动新实验，4×5090 保留给 rebuttal 期间使用 | — |\\n| D243 | 2026-05-22 | 研究确认收敛，不追加主要实验；等 pretrained N16/N32 完成后提交 R41 | exp_fewnerd_pretrained_n16_s42_v2, exp_fewnerd_pretrained_n32_s42_v2 |\\n| D242 | 2026-05-22 | Table 4 指标透明度修复 + SciERC MV sign flip 排除 + FewNERD | exp_esj_qwen3_all, exp_scierc_n8_s2024, exp_scierc_n8_s3141 |\\n| D241 | 2026-05-22 | R40 Action Matrix 定稿：5
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T03:59:51.059792+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T03:59:51.110336+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T04:00:00.001609+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 0/4 使用 | Worker 0 (GPU 0 / CPU 0) | 磁盘: autodl-5090 / 未检查\n\nLoop #20 Session-start 状态确认：\n- 0 RUNNING，0 活跃 cron，18 PREPARING（rebuttal 备用池）\n- 论文 submission-ready，DDL 明天 (2026-05-25)\n- 4×5090 全部空闲，按 D244 保留给 rebuttal\n- 全部待办 blocked on 用户：OpenReview 提交、R41 确认、Figure 1 最终版\n\n无需决策，待命中。",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 0/4 使用 | Worker 0 (GPU 0 / CPU 0) | 磁盘: autodl-5090 / 未检查\n\nLoop #20 Session-start 状态确认：\n- 0 RUNNING，0 活跃 cron，18 PREPARING（rebuttal 备用池）\n- 论文 submission-ready，DDL 明天 (2026-05-25)\n- 4×5090 全部空闲，按 D244 保留给 rebuttal\n- 全部待办 blocked on 用户：OpenReview 提交、R41 确认、Figure 1 最终版\n\n无需决策，待命中。",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T04:00:04.264921+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 4263
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-24T04:00:10.094881+00:00_

初始化完成，已向 Director 汇报。当前状态：全部待命，等用户操作（OpenReview 提交 / R41 确认 / Figure 1）。无活跃实验，无需调度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:exp_fewnerd_pretrained_n32_s42_v2"
}
```

</details>

---
