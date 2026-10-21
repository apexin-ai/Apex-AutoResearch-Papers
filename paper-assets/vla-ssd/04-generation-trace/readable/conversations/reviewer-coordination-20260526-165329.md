# Reviewer coordination (archived snapshot)

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 298
- **Recorded user turns:** 9
- **Tool calls:** 140
- **Original source:** `logs/chats/archive/feishu_group_oc_9e9aef1687e6abd097aa0edaf0551ee3_reviewer_20260526T165329_743858.jsonl`
- **Structured JSON:** [`d987f64211226eb31647.json`](../../sessions/d9/d987f64211226eb31647.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-25T22:18:24.361528+00:00_

[HANDOFF] 你是 Research Reviewer，这是 Loop #13。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- 服务器 westd-19183，代码根目录 /root/vla-ssd
- Reviewer 角色只读——不执行实验、不修改文件、不 ssh_execute
- 唯一输出渠道：`reviewer_post_to_director`
- 论文 DDL：Abstract 5/26，Paper 5/29（CoRL 2026）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，工作目录 /root/vla-ssd
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/
- 论文源码：projects/vla-ssd/docs/paper/（main.tex + 分章节 .tex + appendix.tex ~1278行）
- 无活跃训练进程——所有 143 个实验已完成，项目处于论文写作/提交阶段
- 无 wandb 需要监控

### 3. 📊 当前状态
刚完成并已 post：两个新增 appendix 小节审查（§cross_arch_rationale + §convergent_evidence）。结论 WARNING——NORA vision encoder 写成 "InternViT"（错，应为 Qwen2.5-VL native ViT）、vision integration 写成 "Cross-attention (interleaved)"（错，应为 token concatenation）。§convergent_evidence 通过。

已完成的审查链：
- Figure 3 random-split CRITICAL → 已修复验证
- Figure 4 colorblind/caption → 已修复验证
- v12 全文一致性 pass（78项）→ 通过
- Rebuttal v2 Bonferroni 48→40 错误 → 已报 Director，**未确认修复**
- conclusion.tex 孤儿文件 → 已报（info级）

Registry: 全部 DONE，无 RUNNING/PREPARING。无等待中的 Worker 回调或 Cron。

### 4. 📋 待办
- Director 确认 NORA vision encoder/integration 修复 → 验证 appendix 对应行是否改正
- Rebuttal v2 最终版出来 → 检查 Bonferroni "48/63" 是否已改为 "40/45 (88.9%)"
- 若 Director 触发最终提交前审查 → 做 PDF 视觉审查（load paper-visual-review skill）
- 若收到新章节/大改 → 按模式 B 审查（load paper-quality-lessons skill）

### 5. 🎯 战略上下文
项目核心结论：VLM→VLA fine-tuning 产生 exit collapse（ΔR²=0.16-0.46），VLA→VLA 不产生（<0.10）；L1 instruction attention 继承自 backbone；counterfactual sensitivity d=0.45-1.52 跨架构一致。N=2 VLM→VLA transitions 是最大 limitation。

易错点：
- 论文中有两套 R² 数字体系：demo-split（正确，Table 1）和 random-split（历史残留，部分旧 artifact 可能还有）——永远以 demo-split 为准
- appendix 1278 行很长，需要指定 offset/limit 分段读
- conclusion.tex 是孤儿文件（main.tex 不 include 它），真正的结论在 discussion.tex 末尾
- Rebuttal artifact 在 projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md，其中 Bonferroni 数字仍有错

## 项目硬约束 (memory.md 节选)

## 服务器信息

- westd-19183: 2× RTX PRO 6000
- Bootstrap v3 输出: `/root/autodl-tmp/vla-ssd/results/bootstrap_v3/`
- JSON 文件名: `{trained,untrained}.json`

## 可查的历史
前 11 轮 handoff 在 `task_context/history/reviewer/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-25T22:18:36.001420+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reviewer_post_to_director,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_read_only",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reviewer_post_to_director,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_read_only",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-25T22:18:36.052207+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T22:18:40.166680+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "filters": "{'status': 'RUNNING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "filters": "{'status': 'RUNNING'}"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T22:18:40.217509+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "filters": "{'status': 'PREPARING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "filters": "{'status': 'PREPARING'}"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T22:18:40.670233+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4996}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 503
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T22:18:41.171420+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"bootstrap_v3_cuda1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-23T06:44:43.352Z\", \"updated_at\": \"2026-05-23T06:44:43.353Z\"}, \"bootstrap_v3_cuda0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-23T06:44:41.488Z\", \"updated_at\": \"2026-05-23T06:44:41.488Z\"}, \"behavioral_smoketest_diag\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T05:05:18.989Z\", \"updated_at\": \"2026-05-21T23:25:45.876Z\", \"parent\": \"behavioral_smoketest\", \"conclusion\": \"killed\", \"notes\": \"D074: C-2 closed-loop path formally abandoned. Diagnostic cancelled before completion.\"}, \"behavioral_pilot_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-18T11:40:18.951Z\", \"updated_at\": \"2026-05-21T23:25:45.108Z\", \"hypothesis\": \"Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.\", \"parent\": \"behavioral_pilot_w4\", \"conclusion\": \"killed\", \"notes\": \"Director 确认放弃 behavioral rollout（mujoco 版本不匹配）。Phase 1 SR=0/3，fine-tuned checkpoint 加载成功但 action[0] 锁定在 0.236，Blackwell GPU 需要 device_map 绕过 segfault，可能影响 inference。不再投入。\"}, \"behavioral_pilot\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-18T09:25:24.217Z\", \"updated_at\": \"2026-05-21T23:25:44.194Z\", \"hypothesis\": \"Ablating L1 instruction-dominant heads during VLA inference will measurably change task success rate, providing behavioral evidence that these heads serve a functional role beyond representational reorganization measured by probes.\", \"parent\": \"ablation_50demos_main\", \"conclusion\": \"killed\"}, \"tracvla_spatial_trained\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:11:21.748Z\", \"updated_at\": \"2026-05-21T02:11:21.748Z\"}, \"libero_finetuned_probe\": {\"status\": \"PREPARING\",
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 953
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T22:19:01.877544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T22:19:02.931831+00:00_

1	# Anticipated Reviewer Response Letter
2	
3	We thank the reviewers for their careful evaluation. Below we address nine anticipated questions, referencing specific sections, tables, and figures in the manuscript and appendix.
4	
5	---
6	
7	## Q1: Behavioral correlation underpowered (ρ=0.583, p=0.10, n=9)
8	
9	The sample size **n=9** is determined by the cross-architecture matrix design: 3 architectures × 4 LIBERO suites yields 12 cells, of which 10 are filled (NORA Object and Long-Horizon checkpoints are unavailable; §3.1, Table 1). One cell (NORA Goal) is excluded due to bootstrap CI instability from an exit-layer R² ≈ −0.006 artifact (Table 1, footnote b), leaving **9 usable cells**. Expanding n requires either additional VLA architectures with published LIBERO success rates or additional benchmark suites—both beyond the scope of this initial cross-architecture characterization.
10	
11	We attempted closed-loop evaluation but achieved **SR=0/3** across tested configurations, consistent with known reproducibility challenges in the VLA community (the OpenVLA authors report substantial variation across hardware setups; Fang et al. [2026] similarly document closed-loop difficulties on LIBERO). This negative result is reported in the Appendix (Extended Discussion, 'Closed-loop evaluation attempt' paragraph).
12	
13	Regarding statistical interpretation: **|ρ|=0.583 constitutes a large effect size** by conventional criteria (|ρ|>0.5; Cohen 1988). The p=0.10 reflects insufficient statistical power at n=9, not absence of effect. Within-suite comparisons are uniformly positive: on Goal (n=3 architectures), ΔR² and success rate are perfectly rank-correlated (ρ=1.0), and every remaining suite shows the same direction (Appendix, Extended Discussion). The paper explicitly qualifies this as "directionally consistent but underpowered" (§6) and frames it as observational evidence rather than a confirmed causal link.
14	
15	---
16	
17	## Q2: Only validated on LIBERO—how does this g
…[truncated 10603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T22:19:04.138147+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "InternViT|Qwen2\\.5-VL|vision encoder|Cross-attention|token concatenation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "InternViT|Qwen2\\.5-VL|vision encoder|Cross-attention|token concatenation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T22:19:04.240815+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:11:For reference VLMs (Phi-3-Vision, Qwen2.5-VL) that do not produce actions, sensitivity is measured via cosine distance on hidden representations; these metrics operate on different scales and are not directly comparable (\S\ref{sec:cf_sensitivity}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:57:To test whether exit collapse is specific to action-oriented training, we probe three chat-finetuned models that share backbones with our VLAs but lack action heads or robot data: Llama-2-7b-chat (OpenVLA), Phi-3-mini-4k-instruct (TracVLA), and Qwen2.5-3B-Instruct (NORA).\footnote{Qwen2.5-3B-Instruct shares the Qwen2.5 language backbone with NORA's Qwen2.5-VL-3B but lacks the vision encoder and cross-attention modules; see Appendix~\ref{sec:nlp_control_appendix}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:152:The NORA reference (Qwen2.5-VL) allocates 13--14 of its 16 L1 heads to instruction dominance (81--88\%), and training leaves this essentially unchanged at 12--13/16.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:16:\textbf{NORA}~\cite{hung2025nora} uses Qwen2.5-VL-3B ($\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:19:A critical asymmetry distinguishes the reference baselines: the OpenVLA reference is an OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while the TracVLA and NORA references are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/pape
…[truncated 1520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T22:19:13.166225+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "InternViT|cross_arch_rationale|Cross-attention \\(interleaved\\)|token concatenation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "InternViT|cross_arch_rationale|Cross-attention \\(interleaved\\)|token concatenation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T22:19:13.668431+00:00_

1219:\label{sec:cross_arch_rationale}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T22:19:14.321867+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Bonferroni|48/63|40/45|88\\.9",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Bonferroni|48/63|40/45|88\\.9",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T22:19:14.624170+00:00_

&lt;persisted-output>
Output too large (49.4KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-reviewer-7b0fefde/636cd266-4398-44cf-91b0-9b9a7debd68a/tool-results/toolu_019HDPcQ5fuNyfCVVyu7gm1d.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml:1547:  description: Global Bonferroni and Holm-Bonferroni FWER correction across all 63
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md:79:- **Bonferroni correction**: of 45 originally significant tests, 40 survive family-wise correction (88.9%); all 8 core tests survive at α_adj = 7.94×10⁻⁴ (Appendix, Bonferroni Correction)
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md:135:- **Bonferroni correction** (Appendix, Bonferroni Correction): 40/45 originally significant tests survive (88.9%); all 8 core tests remain significant
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v1.md:79:- **Bonferroni correction**: 63 tests total, 48/63 (76%) pass family-wise correction; all 8 core tests survive at α_adj = 7.94×10⁻⁴ (Appendix §A.18)
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v1.md:93:- **Bonferroni correction** (Appendix §A.18): 48/63 tests survive; all 8 core tests remain significant
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_3.md:73:**W2 [warning, 全票共识]** 缺乏多重比较校正。32 层 × 3 条件 × 多 metric 的逐层比较无 FDR/Bonferroni 校正。至少对 key claims（inverted-U peak significance、per-layer training effects）应报告 adjusted p-values。
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_15.md:30:**S2** [三位共识] 附录极其详尽（26 页、30+ 辅助分析），包括 probe sensitivity（5 seeds）、threshold stability（30%-70%）、random-sub
…[truncated 298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T22:19:20.245066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1215",
  "limit": "65"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1215",
    "limit": "65"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T22:19:20.295738+00:00_

1215	\label{fig:claim_evidence}
1216	\end{figure}
1217	
1218	\subsection{Cross-Architecture Design Rationale}
1219	\label{sec:cross_arch_rationale}
1220	
1221	The two VLM-to-VLA transitions (TracVLA and NORA) were selected to maximize structural diversity within the constraint of publicly available LIBERO-evaluated checkpoints.
1222	Table~\ref{tab:arch_diversity} summarizes the design-axis differences.
1223	
1224	\begin{table}[h]
1225	\centering
1226	\caption{\textbf{Structural diversity between the two VLM-to-VLA transitions.} The two architectures differ on nearly every major design axis, strengthening the generality of shared findings.}
1227	\label{tab:arch_diversity}
1228	\small
1229	\begin{tabular}{@{}lll@{}}
1230	\toprule
1231	Design Axis & TracVLA & NORA \\
1232	\midrule
1233	Language backbone & Phi-3-mini (3.8B) & Qwen2.5-VL (3B) \\
1234	Backbone family & Microsoft & Alibaba \\
1235	Attention mechanism & Multi-Head Attention & Grouped-Query Attention \\
1236	Number of layers & 32 & 36 \\
1237	Vision encoder & SigLIP (shared w/ base) & Native ViT (dynamic resolution) \\
1238	Vision integration & Projector (late fusion) & Token concatenation (native) \\
1239	Pretraining data & English-centric web & Multilingual web + code \\
1240	Action head design & Linear projection & MLP \\
1241	Training data & OXE + LIBERO & OXE + LIBERO + custom \\
1242	\bottomrule
1243	\end{tabular}
1244	\end{table}
1245	
1246	Despite these differences, both transitions exhibit the same exit-collapse pattern ($\Delta R^2 = 0.156$--$0.455$), while their respective reference VLMs show only small fluctuations ($\Delta R^2 \leq 0.097$).
1247	The probability of observing consistent collapse in two structurally divergent architectures under a null hypothesis of random association is low (permutation test $p = 0.008$; \S\ref{sec:delta_r2_threshold}).
1248	Structural diversity thus provides evidential weight beyond what the raw $N = 2$ count suggests.
1249	
1250	\subsection{Convergent Evidence S
…[truncated 2263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T22:19:31.300609+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Bonferroni|family-wise|FWER",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Bonferroni|family-wise|FWER",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-25T22:19:31.352109+00:00_

85:These effects survive Bonferroni correction across all 63 tests (\S\ref{sec:bonferroni_correction}).
1112:We apply a Bonferroni correction ($\alpha_{\text{adj}} = 0.05 / 63 = 7.94 \times 10^{-4}$) and the less conservative Holm--Bonferroni step-down procedure; both yield identical results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T22:19:40.385961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1108",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1108",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T22:19:40.436632+00:00_

1108	\subsection{Global Multiple Comparison Correction}
1109	\label{sec:bonferroni_correction}
1110	
1111	The paper reports 63 statistical tests spanning permutation tests, $t$-tests, bootstrap comparisons, TOST equivalence, and Spearman correlations.
1112	We apply a Bonferroni correction ($\alpha_{\text{adj}} = 0.05 / 63 = 7.94 \times 10^{-4}$) and the less conservative Holm--Bonferroni step-down procedure; both yield identical results.
1113	Of the 45 originally significant tests, 40 survive correction (88.9\%).
1114	
1115	All eight core tests supporting the paper's main claims remain significant:
1116	RSA permutation at L12 ($p < 0.0001$), trained vs.\ reference image geometry at L12 ($p = 3.9 \times 10^{-5}$), counterfactual wrong and empty instruction ($p < 10^{-100}$), TOST cross-architecture equivalence ($p < 0.0001$), dose-response top-24 ablation ($p < 10^{-100}$), trained vs.\ reference probe $R^2$ ($p < 0.0001$), and bottom-24 specificity ($p < 10^{-90}$).
1117	
1118	Five auxiliary tests lose significance under correction:
1119	(i)~RSA trained vs.\ reference preaction at L12 ($p = 0.005 \to p_{\text{adj}} = 0.284$),
1120	(ii)~DINOv2 vs.\ SigLIP RSA ($p = 0.032 \to p_{\text{adj}} = 1.0$),
1121	(iii)~fused backbone vs.\ SigLIP RSA ($p = 0.011 \to p_{\text{adj}} = 0.673$),
1122	(iv)~CV exact paired permutation ($p = 0.016 \to p_{\text{adj}} = 0.984$),
1123	and (v)~$R^2$ projector vs.\ VLA Spearman correlation ($p = 0.003 \to p_{\text{adj}} = 0.183$).
1124	These concern auxiliary comparisons (encoder ranking, coefficient-of-variation ordering) rather than the core redistribution, probing, or counterfactual findings; no main-text conclusion requires revision.
1125	
1126	\subsection{Mechanistic Interpretation}
1127	\label{sec:mechanistic_interpretation}
1128	
1129	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed atte
…[truncated 1324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T22:19:49.723280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "82",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "82",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T22:19:49.774080+00:00_

82	
83	\paragraph{$R^2$ localization.}
84	$R^2$ action probing localizes training effects: trained readout peaks at $R^2 = 0.678$ (L13), reference readout peaks at $0.609$ (L32), and the training effect concentrates at the readout ($+0.069$) rather than at image\_mean ($+0.015$; \S\ref{sec:action_r2_threecond}).
85	These effects survive Bonferroni correction across all 63 tests (\S\ref{sec:bonferroni_correction}).
86	
87	\subsection{Counterfactual Sensitivity Details}
88	\label{sec:cf_details_appendix}
89	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T22:20:00.568726+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Bonferroni|family-wise|FWER|multiple.comparison",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Bonferroni|family-wise|FWER|multiple.comparison",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-25T22:20:00.669527+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:13:Bonferroni correction details appear in Appendix~\ref{sec:bonferroni_correction}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:85:These effects survive Bonferroni correction across all 63 tests (\S\ref{sec:bonferroni_correction}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:1112:We apply a Bonferroni correction ($\alpha_{\text{adj}} = 0.05 / 63 = 7.94 \times 10^{-4}$) and the less conservative Holm--Bonferroni step-down procedure; both yield identical results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T22:20:24.204478+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\Delta R\\^2.*0\\.\\d+",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\Delta R\\^2.*0\\.\\d+",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-25T22:20:24.756717+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:20:\caption{\textbf{Cross-architecture evaluation matrix.} Each cell reports $\Delta R^2$ (peak$-$exit). OpenVLA: VLA-to-VLA; TracVLA and NORA: VLM-to-VLA. Gray cells: checkpoints not released by original authors. Red borders indicate $\Delta R^2 > 0.10$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:42:VLM-to-VLA fine-tuning is associated with substantial exit collapse across all tested conditions: TracVLA~\cite{zheng2024tracevla} $\Delta R^2 = 0.156$--$0.362$ across all four suites, and NORA~\cite{hung2025nora} $\Delta R^2 = 0.308$ (Spatial) and $0.455$ (Goal) (Figure~\ref{fig:r2_collapse}), all exceeding the $\Delta R^2 > 0.10$ threshold for substantive collapse (\S\ref{sec:cross_arch_analyses}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:43:Under VLA-to-VLA conditions, OpenVLA~\cite{kim2024_openvla} shows only small fluctuations across all four suites ($\Delta R^2 = 0.033$--$0.086$, all below $0.10$); reference baselines similarly show $\Delta R^2 \leq 0.097$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:51:\caption{\textbf{Layer-wise action-probe $R^2$ (LIBERO-Goal, readout token).} Solid: trained; dashed: reference. VLM-to-VLA transitions show pronounced peak-to-exit drops ($\Delta R^2 = 0.16$--$0.46$); VLA-to-VLA remains flat ($< 0.09$). Quantitative $\Delta R^2$ values use demo-level splitting (\S\ref{sec:cross_arch_analyses}); see Table~\ref{tab:cross_arch_matrix} for all cells.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:58:All three produce flat $R^2$ profiles ($\Delta R^2 = 0.000$; $R^2 = 0.155 \pm 0.001$, $0.155 \pm 0.000$, and $0.155 \pm 0.000$ respectively; Appendix~\ref{sec:nlp_control_appendix}), contrasting with VLM-to-VLA collapse ($\Delta R^2 = 0.156$--$0.455$).

…[truncated 6438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T22:20:25.710506+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "random.split|random split",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "random.split|random split",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-25T22:20:26.162593+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:52:Demo-level splitting reduces $R^2$ from $0.7$--$0.9$ to $0.4$--$0.6$ compared to random splitting, confirming that temporal correlations inflate aggregate estimates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T22:20:26.263405+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "report.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-25T22:20:26.314236+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/report.md\", \"content\": \"# Handover — 2026-05-24\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- tracvla_spatial_full_v2: TraceVLA (Phi-3-mini) on LIBERO-Spatial shows the convergent entry-exit routing pattern when fine-tuned, and the untrained base model (Phi-3-Vision) lacks this pattern. Cross-suite validation for second architecture.（已分配 ? GPU:?，等待提交）\\n- bootstrap_v3_cuda1（准备中）\\n- bootstrap_v3_cuda0（准备中）\\n- behavioral_smoketest_diag（准备中）\\n- behavioral_pilot_v2: Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.（准备中）\\n- behavioral_pilot: Ablating L1 instruction-dominant heads during VLA inference will measurably change task success rate, providing behavioral evidence that these heads serve a functional role beyond representational reorganization measured by probes.（准备中）\\n- tracvla_spatial_trained（准备中）\\n- libero_finetuned_probe（准备中）\\n- fulllayer_action_probe（准备中）\\n- l1_head_ablation_control8（准备中）\\n- …另有 1 项\\n\\n## 近期结论\\n- **qwen_nlp_control** (success): NLP instruction-tuning of Qwen2.5-3B backbone (Qwen2.5-3B-Instruct) produces flat R² action-probe profile with ΔR²≈0, confirming exit collapse is specific to VLA action training — extending NLP controls to the third backbone family (Qwen, shared with NORA), closing the stated limitation in discussion.tex:23\\n- **phi3_nlp_control** (success): NLP instruction-tuning of Phi-3-mini backbone (Phi-3-mini-instruct) produces flat R² action-probe profile with ΔR²≈0, confirming exit collapse is specific to VLA action training rather than generic finetuning — extending the Llama-2-chat control to a second backbone family shared with TracVLA\\n  [phi3_nlp_control_summary](/api/work
…[truncated 1365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T22:20:43.106525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-25T22:20:43.558214+00:00_

1	When vision-language models are fine-tuned for robotic action prediction, which representational changes reflect training and which are inherited from the pretrained backbone?
2	We conduct a cross-architecture representational analysis of three VLAs (OpenVLA, TracVLA, and NORA) across four LIBERO task suites, comparing trained and reference checkpoints.
3	Using layer-wise action probes, attention profiling, and counterfactual instruction perturbations, we find that the two tested VLM-to-VLA transitions exhibit pronounced peak-to-exit reductions in action-probe decodability, whereas the tested VLA-to-VLA transition shows only small fluctuations.
4	An NLP finetuning control on each of the three backbone families ($\Delta R^2 = 0.000$) is consistent with exit collapse being specific to action-oriented training rather than generic fine-tuning.
5	Trained action-producing VLAs show medium-to-large sensitivity to instruction perturbations ($d = 0.45$--$1.52$), while L1 instruction-dominant attention largely pre-exists in the pretrained backbones.
6	These results provide a cross-architecture characterization of instruction-related representations in action-finetuned VLAs and clarify which observed patterns are training-associated versus inherited from reference models.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T22:20:43.608783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-25T22:20:43.659425+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) fine-tune pretrained language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but which of the resulting representational changes reflect action training and which are inherited from the pretrained backbone?
5	In these decoder-only architectures, image tokens precede instruction tokens, and the causal attention mask restricts multimodal integration to a single readout token~\cite{wang2025seeing,pei2025rethinking}; how representations at this critical position are reshaped by action fine-tuning remains unknown.
6	
7	Behavioral studies show that VLAs exhibit visual dominance~\cite{grant2026} and underweight instructions~\cite{haon2025}, but existing representational analyses target single architectures.
8	No prior work tests whether instruction routing mechanisms are consistent across backbone families or decomposes training-associated effects from inherited base-model priors.
9	
10	We address this gap with a cross-architecture analysis of three VLAs (OpenVLA~\cite{kim2024_openvla}, TracVLA~\cite{zheng2024tracevla}, and NORA~\cite{hung2025nora}) across four LIBERO~\cite{liu2023_libero} task suites (\S\ref{sec:setup}).
11	TracVLA and NORA baselines are pure VLMs ($N = 2$ independent VLM-to-VLA transitions); OpenVLA's baseline is the OXE-pretrained~\cite{padalkar2023_oxe} VLA (VLA-to-VLA transition).
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=0.88\linewidth]{figures/fig_overview.pdf}
16	\vspace{-6pt}
17	\caption{\textbf{Analysis framework.} We analyze hidden states at image-token averages and the readout token via layer-wise action probes, counterfactual instruction perturbations, and L1 attention profiling to distinguish training-associated changes from inherited backbone priors.}
18	\label{fig:overview}
19	\vspace{-6pt}
20	\end{figure}
21	
22	Our analysis reveals 
…[truncated 1427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T22:20:53.362462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-25T22:20:53.413133+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Scope and limitations.}
5	All findings are correlational (confounded by data distribution and optimization; $N = 2$ VLM-to-VLA transitions; Appendix~\ref{sec:claim_evidence_appendix}); we analyze causal-decoder VLAs on LIBERO only (flow-matching~\cite{black2024_pi0} and diffusion~\cite{ghosh2024_octo} architectures may differ); all analyses are open-loop.
6	Trained $\Delta R^2$ correlates with published success rates ($\rho = 0.583$, $p = 0.10$; Appendix~\ref{sec:extended_discussion_appendix}) but is underpowered ($n = 9$; effect size is large, $|\rho| > 0.5$); tracing collapse onset remains for future work.
7	
8	\paragraph{Practical implications.}
9	$\Delta R^2$ provides a cheap diagnostic ($> 0.10$ signals reorganization); preserved VLA-to-VLA exit structure justifies staged pipelines; mid-layer probes outperform exit-layer probes where collapse is pronounced (Appendix~\ref{sec:extended_discussion_appendix}).
10	
11	\paragraph{Conclusion.}
12	Across three architectures and four LIBERO suites, VLM-to-VLA fine-tuning produces exit collapse ($\Delta R^2 = 0.16$--$0.46$) while VLA-to-VLA conditions remain flat ($< 0.10$).
13	All trained VLAs show graded counterfactual sensitivity ($d = 0.45$--$1.52$); L1 instruction attention is inherited from pretrained backbones; NLP controls ($\Delta R^2 = 0.000$) confirm transition-type specificity, providing reusable diagnostics for future VLA evaluation and training pipeline design.
14	Code and data will be released upon acceptance.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T22:21:09.724137+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/ | head -20",
  "description": "List recent artifacts by modification time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/ | head -20",
    "description": "List recent artifacts by modification time"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-25T22:21:10.126492+00:00_

total 19784
-rw-r--r-- 1 ubuntu ubuntu   86803 May 25 21:39 manifest.yaml
-rw-r--r-- 1 ubuntu ubuntu    1651 May 25 21:39 abstract_submission.md
-rw-r--r-- 1 ubuntu ubuntu 1073203 May 25 21:05 VLA-SSD_camera_ready_v13_20260525.pdf
-rw-r--r-- 1 ubuntu ubuntu   18651 May 25 20:27 anticipated_rebuttal_v2.md
-rw-r--r-- 1 ubuntu ubuntu 1072304 May 25 20:26 VLA-SSD_终版v12_figures_fixed_20260525.pdf
-rw-r--r-- 1 ubuntu ubuntu   14180 May 25 20:05 number_consistency_check_v1.md
-rw-r--r-- 1 ubuntu ubuntu   11946 May 25 19:52 anticipated_rebuttal_v1.md
-rw-r--r-- 1 ubuntu ubuntu 1070970 May 25 07:02 VLA-SSD_终版v11_20260525.pdf
-rw-r--r-- 1 ubuntu ubuntu 1070977 May 25 06:56 paper_body_8pages_20260525_0656.pdf
-rw-r--r-- 1 ubuntu ubuntu 1073770 May 25 05:19 paper_final_20260525v10.pdf
-rw-r--r-- 1 ubuntu ubuntu    6340 May 24 20:44 bootstrap_ci_delta_r2.py
-rw-r--r-- 1 ubuntu ubuntu    7171 May 24 18:06 seed_robustness_openvla.py
-rw-r--r-- 1 ubuntu ubuntu    8542 May 24 18:06 seed_robustness_tracvla.py
-rw-r--r-- 1 ubuntu ubuntu 1071623 May 24 17:29 paper_final_20260524v8.pdf
-rw-r--r-- 1 ubuntu ubuntu 1071655 May 24 16:54 paper_final_20260524v7.pdf
-rw-r--r-- 1 ubuntu ubuntu 1071619 May 24 15:26 paper_final_20260524v6.pdf
-rw-r--r-- 1 ubuntu ubuntu 1069097 May 24 15:17 paper_final_20260524v5.pdf
-rw-r--r-- 1 ubuntu ubuntu 1069236 May 24 15:11 paper_final_20260524v4.pdf
-rw-r--r-- 1 ubuntu ubuntu 1068688 May 24 14:17 paper_final_20260524v3.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-25T22:21:10.177219+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/ | head -20",
  "description": "List recent paper file modifications"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/ | head -20",
    "description": "List recent paper file modifications"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-25T22:21:10.227947+00:00_

total 1488
-rw-r--r-- 1 ubuntu ubuntu   18734 May 25 22:18 main.fdb_latexmk
-rw-r--r-- 1 ubuntu ubuntu 1076626 May 25 22:18 main.pdf
-rw-r--r-- 1 ubuntu ubuntu   37752 May 25 22:18 main.log
-rw-r--r-- 1 ubuntu ubuntu   22177 May 25 22:18 main.fls
-rw-r--r-- 1 ubuntu ubuntu   16168 May 25 22:18 main.out
-rw-r--r-- 1 ubuntu ubuntu   66702 May 25 22:18 main.aux
-rw-r--r-- 1 ubuntu ubuntu     933 May 25 22:18 main.blg
-rw-r--r-- 1 ubuntu ubuntu   19460 May 25 22:18 main.bbl
-rw-r--r-- 1 ubuntu ubuntu   86399 May 25 22:17 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu   14590 May 25 21:05 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu   20687 May 25 21:05 references.bib
-rw-r--r-- 1 ubuntu ubuntu    3346 May 25 20:27 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu    1541 May 25 20:27 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu    7327 May 25 06:30 method.tex
-rw-r--r-- 1 ubuntu ubuntu    1272 May 25 06:29 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu    4344 May 25 05:19 submission_fields.md
-rw-r--r-- 1 ubuntu ubuntu    3795 May 25 01:47 related_work.tex
drwxr-xr-x 3 ubuntu ubuntu    4096 May 24 05:34 _figure_backups
-rw-r--r-- 1 ubuntu ubuntu    1603 May 24 03:31 conclusion.tex.bak

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-25T22:21:21.987653+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/abstract_submission.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/abstract_submission.md"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-25T22:21:22.891202+00:00_

1	# CoRL 2026 Abstract Submission
2	
3	## Title
4	
5	Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis
6	
7	## Abstract
8	
9	When vision-language models are fine-tuned for robotic action prediction, which representational changes reflect training and which are inherited from the pretrained backbone? We conduct a cross-architecture representational analysis of three VLAs (OpenVLA, TracVLA, and NORA) across four LIBERO task suites, comparing trained and reference checkpoints. Using layer-wise action probes, attention profiling, and counterfactual instruction perturbations, we find that the two tested VLM-to-VLA transitions exhibit pronounced peak-to-exit reductions in action-probe decodability, whereas the tested VLA-to-VLA transition shows only small fluctuations. An NLP finetuning control on each of the three backbone families (Delta R-squared = 0.000) is consistent with exit collapse being specific to action-oriented training rather than generic fine-tuning. Trained action-producing VLAs show medium-to-large sensitivity to instruction perturbations (Cohen's d = 0.45-1.52), while L1 instruction-dominant attention largely pre-exists in the pretrained backbones. These results provide a cross-architecture characterization of instruction-related representations in action-finetuned VLAs and clarify which observed patterns are training-associated versus inherited from reference models.
10	
11	## Keywords
12	
13	1. Vision-Language-Action models
14	2. Representational analysis
15	3. Instruction routing
16	4. Cross-architecture comparison
17	5. Fine-tuning analysis
18	6. Attention profiling
19	7. Action probing
20	8. Robotic manipulation
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T22:21:22.891694+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "description": "Count lines in appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "description": "Count lines in appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-25T22:21:22.992385+00:00_

1277 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T22:21:59.609117+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: info] Loop #13 提交前最终核查——全部通过\n\n**待确认修复验证（全部 ✅）：**\n\n1. **NORA vision encoder**（appendix.tex L1237）：已从 \"InternViT\" 修正为 \"Native ViT (dynamic resolution)\"\n2. **NORA vision integration**（appendix.tex L1238）：已从 \"Cross-attention (interleaved)\" 修正为 \"Token concatenation (native)\"\n3. **Rebuttal v2 Bonferroni**（anticipated_rebuttal_v2.md L79/L135）：已统一为 \"40/45 (88.9%)\"，与 appendix.tex L1113 一致\n\n**Abstract 提交物审查（abstract_submission.md）：**\n- 标题、摘要文本与 abstract.tex 一致，LaTeX 符号正确转写为纯文本\n- 关键数字（ΔR²=0.000, d=0.45-1.52）保留完整\n\n**全文数字一致性（关键 claim 跨 5 个 .tex 文件交叉核对）：**\n- ΔR² 0.16-0.46 / <0.10 / 0.000：abstract ↔ intro ↔ experiments ↔ discussion ↔ appendix 全部一致 ✅\n- d = 0.45-1.52：一致 ✅\n- ρ=0.583, p=0.10, n=9：一致 ✅\n- Bonferroni 40/45 (88.9%)：appendix + rebuttal 一致 ✅\n- N=2 VLM-to-VLA transitions：正确贯穿全文 ✅\n- Random-split 数据仅在 method.tex 方法论对比中出现，未污染报告数字 ✅\n\n**状态：** 无 RUNNING 实验，无遗留 critical。论文 v13 camera-ready + abstract_submission.md 已就绪。appendix.tex 22:17 有编辑但 main.pdf 22:18 已重编译包含该改动。\n\n明天 Abstract DDL（5/26），无阻塞项。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: info] Loop #13 提交前最终核查——全部通过\n\n**待确认修复验证（全部 ✅）：**\n\n1. **NORA vision encoder**（appendix.tex L1237）：已从 \"InternViT\" 修正为 \"Native ViT (dynamic resolution)\"\n2. **NORA vision integration**（appendix.tex L1238）：已从 \"Cross-attention (interleaved)\" 修正为 \"Token concatenation (native)\"\n3. **Rebuttal v2 Bonferroni**（anticipated_rebuttal_v2.md L79/L135）：已统一为 \"40/45 (88.9%)\"，与 appendix.tex L1113 一致\n\n**Abstract 提交物审查（abstract_submission.md）：**\n- 标题、摘要文本与 abstract.tex 一致，LaTeX 符号正确转写为纯文本\n- 关键数字（ΔR²=0.000, d=0.45-1.52）保留完整\n\n**全文数字一致性（关键 claim 跨 5 个 .tex 文件交叉核对）：**\n- ΔR² 0.16-0.46 / <0.10 / 0.000：abstract ↔ intro ↔ experiments ↔ discussion ↔ appendix 全部一致 ✅\n- d = 0.45-1.52：一致 ✅\n- ρ=0.583, p=0.10, n=9：一致 ✅\n- Bonferroni 40/45 (88.9%)：appendix + rebuttal 一致 ✅\n- N=2 VLM-to-VLA transitions：正确贯穿全文 ✅\n- Random-split 数据仅在 method.tex 方法论对比中出现，未污染报告数字 ✅\n\n**状态：** 无 RUNNING 实验，无遗留 critical。论文 v13 camera-ready + abstract_submission.md 已就绪。appendix.tex 22:17 有编辑但 main.pdf 22:18 已重编译包含该改动。\n\n明天 Abstract DDL（5/26），无阻塞项。",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-25T22:22:03.274450+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 3665
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-25T22:22:17.078700+00:00_

Loop #13 审查完成：

- 3 项待确认修复全部验证通过（NORA vision encoder/integration + Bonferroni 数字）
- Abstract 提交物与论文一致
- 全文关键数字跨 5 个 .tex 文件交叉核对一致
- 无 RUNNING 实验，无遗留 critical
- 明天 Abstract DDL 无阻塞项

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---

## Round 2

56 recorded events

### User

_source line 49 · 2026-05-25T22:55:16.565959+00:00_

[System 触发审查]:
论文 v13 已通过核查，但距 Paper DDL (5/29) 还有 4 天。请做一次"天花板审查"而非"底线核查"：

1. **Rebuttal 弱点分析**：anticipated_rebuttal_v2.md 中 9 个问题，哪个回答最薄弱？有没有任何轻量实验（≤4 GPU·h，非 closed-loop）能补强？特别关注 Q8 (causal evidence) 和 Q1 (behavioral underpowered)。

2. **叙事打磨空间**：Related Work 覆盖度是否完整（近期 5-6 月有无遗漏的新竞品）？Intro 的 hook 是否足够强？Discussion 的 actionable insight 还能更具体吗？

3. **Appendix 补充机会**：有没有已有数据但未呈现的分析可以加入 appendix 加强证据链？（如：更多 visualization、额外统计视角）

目标：识别 1-3 个可在 Paper DDL 前完成的高 ROI 改进点。不需要再验证数字一致性（Loop 13 已确认）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T22:55:26.919387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md",
  "offset": "98"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md",
    "offset": "98"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-25T22:55:27.421696+00:00_

98	
99	## Q8: Probing measures decodability, not causal reliance—how do you know the model actually uses this information?
100	
101	The paper acknowledges this limitation directly in §4.6 (Synthesis): "These probes measure decodability, not causal reliance." We consider this distinction important to state but insufficient to dismiss the findings, for several reasons.
102	
103	**Characterization precedes causal intervention.** Even without causal proof, establishing *where* information resides and *how* training reorganizes it is a necessary first step toward understanding. The analogy to neuroscience is instructive: fMRI cannot establish causal necessity, yet functional imaging has been foundational for building models of brain organization that subsequently guided causal interventions (TMS, lesion studies). Our probing results serve the same cartographic function for VLA internals.
104	
105	**Complementary behavioral evidence.** The counterfactual perturbation analysis (§4.4) provides direct behavioral evidence that instruction content *does* influence action outputs: swapping instructions between task suites produces medium-to-large action divergence (Cohen's d = 0.45–1.52, Table 2). This does not prove that the specific layers identified by probing are causally necessary, but it establishes that instruction information is functionally utilized somewhere in the pipeline.
106	
107	**Intervention evidence from dose-response ablation.** The attention head ablation (Appendix, Extended Discussion) provides intervention-level evidence: progressively removing instruction-dominant L1 heads produces monotonic increases in action divergence (d = 0.48–0.64), confirming that the attention structures we identify carry functionally relevant signals.
108	
109	**Convergent triangulation.** Three methodologically distinct approaches point to the same conclusion: probing identifies *where* instruction information concentrates, perturbation confirms *whether* instruction content aff
…[truncated 4483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T22:55:27.572722+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-25T22:55:27.874194+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce actions from visual and language input~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora,xiao2025ava}.
5	NLP instruction tuning is well-characterized behaviorally~\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.
6	Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; recent VLA-specific work proposes representation-preserving strategies~\cite{grover2025preserving,hancock2025actions}. Existing analyses target single architectures and cannot separate training dynamics from backbone artifacts.
7	
8	\paragraph{Mechanistic and behavioral analysis.}
9	Mechanistic interpretability has revealed residual stream communication~\cite{elhage2021}, induction heads~\cite{olsson2022}, and task circuits~\cite{wang2023_ioi,conmy2023}; causal tracing localizes factual recall~\cite{meng2022_rome}; attention probing shows heads encode syntactic relations~\cite{clark2019} and most can be pruned~\cite{michel2019sixteen}.
10	In VLMs, recent work characterizes visual token redundancy~\cite{fan2026visual}, progressive visual-textual alignment~\cite{neo2025interpreting,long2026understanding}, and instruction tokens as shallow-layer modality arbitration anchors~\cite{zhang2026instruction}.
11	Behavioral evaluations of VLAs reveal visual dominance~\cite{grant2026,hou2026,fei2025}; mechanistic studies identify sparse semantic directions~\cite{haon2025}, interpretable features~\cite{swann2026,buurmeijer2026}, symbolic representations~\cite{lu2025,molinari2025}, comprehension-action trade-offs~\cite{fang2025}, and task-specific attention heads for selective fine-tuning~\cite{mitra2025mechanistic}.
12	Concurrent continual-learning
…[truncated 1861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T22:55:27.874667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-25T22:55:27.925361+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We apply all three analyses (\S\ref{sec:cross_arch_analyses}) to the $3 \times 4$ architecture-suite matrix described in \S\ref{sec:arch_data} (Table~\ref{tab:cross_arch_matrix}).
8	Of the 12 cells, 10 are filled; NORA Object and Long-Horizon lack available checkpoints.
9	For OpenVLA LIBERO-Goal, $N = 63{,}228$ observations; other cells are at comparable scale.
10	For trained models that produce action outputs, counterfactual sensitivity is measured via Cohen's $d$ on action MSE.
11	For reference VLMs (Phi-3-Vision, Qwen2.5-VL) that do not produce actions, sensitivity is measured via cosine distance on hidden representations; these metrics operate on different scales and are not directly comparable (\S\ref{sec:cf_sensitivity}).
12	OpenVLA's OXE-pretrained checkpoint produces actions, permitting same-metric (Cohen's $d$) comparison in that condition.
13	Bonferroni correction details appear in Appendix~\ref{sec:bonferroni_correction}.
14	Figure~\ref{fig:result_matrix} summarizes the $3 \times 4$ architecture-suite matrix.
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.82\textwidth]{figures/fig_matrix_heatmap.pdf}
19	\vspace{-6pt}
20	\caption{\textbf{Cross-architecture evaluation matrix.} Each cell reports $\Delta R^2$ (peak$-$exit). OpenVLA: VLA-to-VLA; TracVLA and NORA: VLM-to-VLA. Gray cells: checkpoints not released by original authors. Red borders indicate $\Delta R^2 > 0.10$.}
21	\label{fig:result_matrix}
22	\vspace{-10pt}
23	\end{figure}
24	
25	%------------------------------------------------------------------
26	\subsection{OpenVLA: Motivating Single-Architecture Analysis}
27	\label{sec:openvla_routing}
28	
29	Before testing cross-architectural generality, we establish three core phenomena on OpenVLA~\cite{kim2024_openvla} (full analysis in Appendix~\ref{sec:openvla_deepdive_appendix}).
30	At L1, three conditions form a gradient: 
…[truncated 13190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-25T22:56:05.657132+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/ | grep -v '.pdf$' | grep -v '.py$' | sort",
  "description": "List non-PDF non-Python artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/ | grep -v '.pdf$' | grep -v '.py$' | sort",
    "description": "List non-PDF non-Python artifacts"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-25T22:56:06.110395+00:00_

_project
ablation_narrative_playbook.md
abstract_submission.md
action_metrics_extended
action_probe_design.md
anticipated_rebuttal_v1.md
anticipated_rebuttal_v2.md
attention
attention_decomposition
behavioral_pilot_w4_diagnosis.md
bootstrap_progress.md
bootstrap_task_ratio.json
branch_split_rsa_results.md
cf_batch_missing_v1
cf_batch_part2_v1
cf_batch_part2_v1_analysis.md
citation_verification_2026.md
closedloop_diagnosis.md
clustered_bootstrap_reanalysis_v2
clustered_bootstrap_reanalysis_v3
concurrent_work_analysis.md
controlb_analysis
counterfactual_10tasks
counterfactual_spatial
counterfactual_token_overlap
cross_inst_extract_phase2
cross_instruction
d098_correlational_analysis.md
definitive_rsa_results.md
demo_standardized_rsa.md
dinov2_baseline
dream_reports
fig_cross_architecture_attention.png
fig_ood_diagnostics.png
fig_rsa_perlayer_curve.png
fig_specificity_bootstrap_30seeds.png
figures
groundtruth_action_error
kendall_w_cross_task.json
layer_stability_analysis.md
libero_finetuned_attention
libero_finetuned_probe_profile.json
libero_goal_feasibility.md
literature_linkage_4suite_consistency.md
literature_map.yaml
literature_map_probing.md
literature_survey_instruction_probing.md
manifest.yaml
matched_ablation_controls_diagnosis.md
matrix_summary_table.md
multi_threshold_robustness
mvp_controlb_trained
mvp_probe_trained
nlp_finetuning_control_v1
nora_analysis_report.md
number_consistency_check_v1.md
openvla_goal_spatial_data.md
openvla_goal_standardized_v1
openvla_libero_goal_compat.md
openvla_spatial_standardized_v1
openvla_spatial_trained_extraction.md
paper
paper_consistency_report.md
permutation_10k
phi3_nlp_control
phi3v_attention_profile
phi3v_attention_trained_10tasks
phi3v_attention_untrained
phi3v_probe_untrained
phi3v_r2_action_probe
phi3v_r2_seed_expansion
phi3v_r2_untrained_probe
phi3v_untrained_seed_expansion
pipeline_audit_libero_goal.md
plan_010_libero_spatial
plan_011_fulllayer_r2
plan_012_clip_vit_control
probe_design_plan.md
rebuttal_drafts.m
…[truncated 536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-25T22:56:06.662664+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/vla-ssd/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/vla-ssd/results/"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-25T22:56:07.266362+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-25T22:56:07.768507+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"trained_dryrun\\ntrained_dryrun_pca1024\\ntrained_pca1024\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1105
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-25T22:56:08.287718+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ablations\\naction_baselines.json\\naction_metrics_extended.json\\naction_probe\\naction_trajectory_L13_ablation.json\\naction_trajectory_L13_ablation.log\\naction_trajectory_L8_ablation.json\\naction_trajectory_L8_ablation.log\\naction_trajectory_analysis.json\\naction_trajectory_analysis.log\\naction_trajectory_control.json\\naction_trajectory_control.log\\naction_trajectory_cpu_analysis.json\\naction_trajectory_extended_analysis.json\\nanalysis\\narchitecture_audit\\nattention\\nattention_decomposition.json\\nattention_normalization_entropy.json\\nbootstrap_ci\\nbootstrap_ci_values.json\\nbootstrap_r2\\nbootstrap_v3\\nbootstrap_v3_dryrun\\ncka\\ncounterfactual_10tasks\\ncounterfactual_10tasks.log\\ncounterfactual_combined.json\\ncounterfactual_correct.json\\ncounterfactual_empty.json\\ncounterfactual_instruction.log\\ncounterfactual_paraphrased.json\\ncounterfactual_shuffled.json\\ncounterfactual_spatial\\ncounterfactual_spatial.log\\ncounterfactual_token_overlap.json\\ncounterfactual_wrong.json\\ncross_instruction\\ncross_instruction_dense\\ncross_instruction_finetuned\\ncross_instruction_spatial\\ndemo_sensitivity_25\\ndinov2\\ndinov2_libero_goal\\ndinov2_libero_goal_frame0\\ndinov2_libero_goal_linear\\ndinov2_libero_goal_pca1024\\ndinov2_shuffle\\ndose_response_cuda0.log\\ndose_response_cuda1.log\\ndose_response_curve_combined.json\\ndose_response_top12.json\\ndose_response_top16.json\\ndose_response_top20.json\\ndose_response_top24.json\\ndose_response_top28.json\\ndose_response_top32.json\\ndose_response_top4.json\\ndose_response_top8.json\\nfig_dose_response_curve.pdf\\nfig_dose_response_curve.png\\nfig_dose_response_draft.pdf\\nfig_dose_response_draft.png\\nfigure_data\\nfigures\\nfinetuned_probe_profile.log\\nfunctional_validation\\ngroundtruth_action_error.json\\ngroundtruth_action_error.log\\nl1_head_ablation\\nlibero_closedloop_probe\\nlibero_finetuned_attention.log\\nlibero_finetuned_attention_pr
…[truncated 1920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1021
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-25T22:56:25.051122+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\subsection|\\\\section",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\subsection|\\\\section",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-25T22:56:25.503226+00:00_

6:\section{Supplementary Material}
14:\subsection{Architecture Summary}
34:\subsection{OpenVLA-Specific Analysis Methods}
53:\subsection{OpenVLA Single-Architecture Deep Dive}
87:\subsection{Counterfactual Sensitivity Details}
124:\subsection{CKA Analysis Method}
136:\subsection{Metric Sensitivity: RSA versus CKA}
154:\subsection{Branch-Split Detailed Analysis}
162:\subsection{RSA Across Representation Sources}
174:\subsection{Per-Layer RSA Profiles}
186:\subsection{Per-Layer Action Decoding Across Training Stages}
206:\subsection{Random-Subset Ablation Details}
220:\subsection{Action Trajectory Analysis Details}
332:\subsection{Pretrained LLM Representation Quality Under Visual Input}
349:\subsection{Probe Architecture Sensitivity}
366:\subsection{Functional Probe Comparison}
378:\subsection{Training Effect and Instruction Invariance}
391:\subsection{Additional RSA Values}
397:\subsection{Cross-Suite Validation within LIBERO: Spatial}
467:\subsection{Robustness Analyses}
613:\subsection{Detailed Training Effects}
643:\subsection{Training Effect Size Summary}
669:\subsection{Instruction Classification Probes}
844:\subsection{L1 Attention Decomposition by Head Group}
873:\subsection{Per-Dimension Action MAE Under Head Ablation}
898:\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}
928:\subsection{Task Complexity and Attention Dependence}
968:\subsection{Specificity Control: Matched-Size Head Ablation}
992:\subsection{Paired Effect Sizes}
1016:\subsection{Cross-Architecture Action Decodability: $2 \times 2$ Design}
1108:\subsection{Global Multiple Comparison Correction}
1126:\subsection{Mechanistic Interpretation}
1133:\subsection{Functional Stages and Predictions}
1146:\subsection{Extended Discussion}
1184:\subsection{NLP Finetuning Controls}
1208:\subsection{Claim-Evidence Summary}
1218:\subsection{Cross-Architecture Design Rationale}
1250:\subsection{Convergent Evidence Summary}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-25T22:56:25.955491+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/probe_r2_vs_behavioral_rank_correlation.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/probe_r2_vs_behavioral_rank_correlation.json"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-25T22:56:26.409037+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"analysis\\\": \\\"Probe R2 vs Per-Task Behavioral Outcomes Rank Correlation\\\",\\n  \\\"n_tasks_behavioral\\\": 5,\\n  \\\"n_tasks_representational\\\": 10,\\n  \\\"limitation\\\": \\\"Only 5 tasks have both R2 and behavioral (paired_mse) data. With n=5, minimum |rho| for p<0.05 is ~0.9.\\\",\\n  \\\"per_task_data\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"paired_mse\\\": 0.022428,\\n      \\\"cohens_d\\\": 0.4329,\\n      \\\"token_divergence_rate\\\": 0.664,\\n      \\\"R2_baseline_L1_5demo\\\": 0.1971,\\n      \\\"R2_baseline_L8_5demo\\\": 0.4532,\\n      \\\"R2_baseline_L13_5demo\\\": 0.5686,\\n      \\\"R2_projector_50demo\\\": 0.4973,\\n      \\\"R2_dino_50demo\\\": 0.4813,\\n      \\\"R2_vla_last_L19_50demo\\\": 0.6015,\\n      \\\"R2_delta_L1_ablation\\\": 0.0218\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"paired_mse\\\": 0.044588,\\n      \\\"cohens_d\\\": 0.6866,\\n      \\\"token_divergence_rate\\\": 0.7094,\\n      \\\"R2_baseline_L1_5demo\\\": 0.2649,\\n      \\\"R2_baseline_L8_5demo\\\": 0.3757,\\n      \\\"R2_baseline_L13_5demo\\\": 0.5466,\\n      \\\"R2_projector_50demo\\\": 0.7499,\\n      \\\"R2_dino_50demo\\\": 0.7138,\\n      \\\"R2_vla_last_L19_50demo\\\": 0.7516,\\n      \\\"R2_delta_L1_ablation\\\": 0.0714\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"paired_mse\\\": 0.046815,\\n      \\\"cohens_d\\\": 0.7038,\\n      \\\"token_divergence_rate\\\": 0.7386,\\n      \\\"R2_baseline_L1_5demo\\\": 0.1901,\\n      \\\"R2_baseline_L8_5demo\\\": 0.3358,\\n      \\\"R2_baseline_L13_5demo\\\": 0.4092,\\n      \\\"R2_projector_50demo\\\": 0.5861,\\n      \\\"R2_dino_50demo\\\": 0.5821,\\n      \\\"R2_vla_last_L19_50demo\\\": 0.7096,\\n      \\\"R2_delta_L1_ablation\\\": 0.0404\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"paired_mse\\\": 0.045853,\\n      \\\"cohens_d\
…[truncated 3838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-25T22:56:26.911431+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/seed_robustness/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/seed_robustness/"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-25T22:56:27.363501+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"openvla_goal_seed_robustness.json\\ntracvla_goal_seed_robustness.json\\ntracvla_spatial_seed_robustness.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-25T22:56:41.976817+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/seed_robustness/openvla_goal_seed_robustness.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/seed_robustness/openvla_goal_seed_robustness.json"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-25T22:56:42.481484+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"cell\\\": \\\"openvla_goal\\\",\\n  \\\"seeds\\\": [\\n    0,\\n    1,\\n    2,\\n    42\\n  ],\\n  \\\"per_seed_r2\\\": {\\n    \\\"0\\\": {\\n      \\\"L0_image_mean\\\": 0.7613,\\n      \\\"L0_last_preaction\\\": 0.3964,\\n      \\\"L1_image_mean\\\": 0.7614,\\n      \\\"L1_last_preaction\\\": 0.5644,\\n      \\\"L2_image_mean\\\": 0.7613,\\n      \\\"L2_last_preaction\\\": 0.6972,\\n      \\\"L3_image_mean\\\": 0.7617,\\n      \\\"L3_last_preaction\\\": 0.6729,\\n      \\\"L4_image_mean\\\": 0.7618,\\n      \\\"L4_last_preaction\\\": 0.6832,\\n      \\\"L5_image_mean\\\": 0.7615,\\n      \\\"L5_last_preaction\\\": 0.684,\\n      \\\"L6_image_mean\\\": 0.7618,\\n      \\\"L6_last_preaction\\\": 0.6812,\\n      \\\"L7_image_mean\\\": 0.7622,\\n      \\\"L7_last_preaction\\\": 0.6811,\\n      \\\"L8_image_mean\\\": 0.762,\\n      \\\"L8_last_preaction\\\": 0.677,\\n      \\\"L9_image_mean\\\": 0.7618,\\n      \\\"L9_last_preaction\\\": 0.6805,\\n      \\\"L10_image_mean\\\": 0.7623,\\n      \\\"L10_last_preaction\\\": 0.6697,\\n      \\\"L11_image_mean\\\": 0.7615,\\n      \\\"L11_last_preaction\\\": 0.6792,\\n      \\\"L12_image_mean\\\": 0.7617,\\n      \\\"L12_last_preaction\\\": 0.6843,\\n      \\\"L13_image_mean\\\": 0.762,\\n      \\\"L13_last_preaction\\\": 0.6847,\\n      \\\"L14_image_mean\\\": 0.7622,\\n      \\\"L14_last_preaction\\\": 0.6924,\\n      \\\"L15_image_mean\\\": 0.7635,\\n      \\\"L15_last_preaction\\\": 0.6932,\\n      \\\"L16_image_mean\\\": 0.7643,\\n      \\\"L16_last_preaction\\\": 0.6914,\\n      \\\"L17_image_mean\\\": 0.7643,\\n      \\\"L17_last_preaction\\\": 0.6849,\\n      \\\"L18_image_mean\\\": 0.7642,\\n      \\\"L18_last_preaction\\\": 0.6841,\\n      \\\"L19_image_mean\\\": 0.7651,\\n      \\\"L19_last_preaction\\\": 0.6921,\\n      \\\"L20_image_mean\\\": 0.7651,\\n      \\\"L20_last_preaction\\\": 0.6816,\\n      \\\"L21_image_mean\\\": 0.7658,\\n      \\\"
…[truncated 8271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-25T22:56:42.481881+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-25T22:56:43.034897+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"per_task_r2_distribution\\\",\\n  \\\"tasks\\\": [\\n    \\\"open the middle drawer of the cabinet\\\",\\n    \\\"open the top drawer and put the bowl inside\\\",\\n    \\\"push the plate to the front of the stove\\\",\\n    \\\"put the bowl on the plate\\\",\\n    \\\"put the bowl on the stove\\\",\\n    \\\"put the bowl on top of the cabinet\\\",\\n    \\\"put the cream cheese in the bowl\\\",\\n    \\\"put the wine bottle on the rack\\\",\\n    \\\"put the wine bottle on top of the cabinet\\\",\\n    \\\"turn on the stove\\\"\\n  ],\\n  \\\"n_tasks\\\": 10,\\n  \\\"mlp_probe_5demo\\\": {\\n    \\\"description\\\": \\\"MLP(4096,256,7) probe, 5 demos/task, per-task R2 distribution\\\",\\n    \\\"conditions\\\": {\\n      \\\"baseline\\\": {\\n        \\\"L1\\\": {\\n          \\\"per_task_R2\\\": {\\n            \\\"open the middle drawer of the cabinet\\\": 0.1971,\\n            \\\"open the top drawer and put the bowl inside\\\": 0.2649,\\n            \\\"push the plate to the front of the stove\\\": 0.1901,\\n            \\\"put the bowl on the plate\\\": 0.3754,\\n            \\\"put the bowl on the stove\\\": 0.2352,\\n            \\\"put the bowl on top of the cabinet\\\": 0.2561,\\n            \\\"put the cream cheese in the bowl\\\": 0.186,\\n            \\\"put the wine bottle on the rack\\\": 0.1894,\\n            \\\"put the wine bottle on top of the cabinet\\\": 0.2789,\\n            \\\"turn on the stove\\\": 0.3854\\n          },\\n          \\\"mean\\\": 0.2559,\\n          \\\"std\\\": 0.0701,\\n          \\\"min\\\": 0.186,\\n          \\\"max\\\": 0.3854,\\n          \\\"range\\\": 0.1994\\n        },\\n        \\\"L8\\\": {\\n          \\\"per_task_R2\\\": {\\n            \\\"open the middle drawer of the cabinet\\\": 0.4532,\\n            \\\"open the top drawer and put the bowl inside\\\": 0.3757,\\n            \\\"push the plate to the front of the stove\\\": 0.3
…[truncated 8402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-25T22:56:43.035317+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/statistical_supplements/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/statistical_supplements/"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-25T22:56:43.487655+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bonferroni_global.json\\npaired_cohens_d.json\\npower_analysis.json\\ntost_equivalence.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T22:56:49.410288+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/statistical_supplements/power_analysis.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/statistical_supplements/power_analysis.json"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-25T22:56:49.863139+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"test\\\": \\\"Statistical power analysis\\\",\\n  \\\"min_detectable_d_n10\\\": 0.996,\\n  \\\"rsa_analysis\\\": {\\n    \\\"sd_within_task\\\": 0.030227,\\n    \\\"mean_diff_trained_vs_untrained\\\": 0.016508,\\n    \\\"n_tasks\\\": 10,\\n    \\\"delta_0017_cohens_d\\\": 0.5624,\\n    \\\"power_rsa_delta_0017\\\": 0.356,\\n    \\\"min_detectable_delta_rsa_n10\\\": 0.0301\\n  },\\n  \\\"r2_analysis\\\": {\\n    \\\"sd_within_task\\\": 0.02576,\\n    \\\"mean_diff_ablated_vs_baseline\\\": 0.03007,\\n    \\\"n_tasks\\\": 10,\\n    \\\"delta_0069_cohens_d\\\": 2.6785,\\n    \\\"power_r2_delta_0069\\\": 1.0,\\n    \\\"min_detectable_delta_r2_n10\\\": 0.0257\\n  },\\n  \\\"n_eff\\\": 10,\\n  \\\"alpha\\\": 0.05,\\n  \\\"target_power\\\": 0.8,\\n  \\\"metadata\\\": {\\n    \\\"rsa_source\\\": \\\"/root/autodl-tmp/vla-ssd/results/rsa/rsa_definitive.json\\\",\\n    \\\"r2_source\\\": \\\"/root/autodl-tmp/vla-ssd/results/l1_head_ablation/specificity_bootstrap_30seeds.json\\\",\\n    \\\"computed_at\\\": \\\"2026-05-21T01:50:04.403380\\\"\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-25T22:56:49.863600+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/statistical_supplements/tost_equivalence.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/statistical_supplements/tost_equivalence.json"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-25T22:56:50.867890+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"test\\\": \\\"Two One-Sided Tests (TOST) for equivalence\\\",\\n  \\\"openvla_peak_layer\\\": \\\"L9\\\",\\n  \\\"openvla_peak_mean\\\": 0.63723,\\n  \\\"openvla_peak_std\\\": 0.008595,\\n  \\\"phi3v_peak_layer\\\": \\\"L11\\\",\\n  \\\"phi3v_peak_mean\\\": 0.633977,\\n  \\\"phi3v_peak_std\\\": 0.008936,\\n  \\\"n_seeds_openvla\\\": 15,\\n  \\\"n_seeds_phi3v\\\": 15,\\n  \\\"mean_diff\\\": 0.003253,\\n  \\\"se\\\": 0.003201,\\n  \\\"epsilon\\\": 0.05,\\n  \\\"df_welch\\\": 27.96,\\n  \\\"t1_upper\\\": -14.6017,\\n  \\\"p1_upper\\\": 0.0,\\n  \\\"t2_lower\\\": 16.6338,\\n  \\\"p2_lower\\\": 0.0,\\n  \\\"p_tost\\\": 0.0,\\n  \\\"ci_90_lower\\\": -0.002193,\\n  \\\"ci_90_upper\\\": 0.008699,\\n  \\\"traditional_ttest_t\\\": 1.0161,\\n  \\\"traditional_ttest_p\\\": 0.318305,\\n  \\\"conclusion\\\": \\\"equivalent\\\",\\n  \\\"interpretation\\\": \\\"The 90% CI [-0.0022, 0.0087] falls entirely within [-0.05, +0.05]\\\",\\n  \\\"metadata\\\": {\\n    \\\"openvla_data_source\\\": \\\"/root/autodl-tmp/vla-ssd/results/functional_validation/r2_probe_15seeds.json\\\",\\n    \\\"phi3v_data_sources\\\": [\\n      \\\"/root/autodl-tmp/vla-ssd/results/functional_validation/phi3v_r2_action_probe.json\\\",\\n      \\\"/root/autodl-tmp/vla-ssd/results/phi3v_r2_seed_expansion/phi3v_r2_seed_expansion.json\\\"\\n    ],\\n    \\\"computed_at\\\": \\\"2026-05-21T01:48:42.413216\\\"\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1004
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-25T22:56:52.775170+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "power.analysis|post.hoc power|required.*sample",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "power.analysis|post.hoc power|required.*sample",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-25T22:56:52.825754+00:00_

582:Post-hoc power analysis ($N = 10$ tasks, $\alpha = 0.05$, target power $= 0.80$) indicates minimum detectable effect sizes of $\Delta_{\text{RSA}} = 0.030$ and $\Delta_{R^2} = 0.026$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-25T22:57:43.800445+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/ood_diagnostics.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/ood_diagnostics.json"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-25T22:57:43.800815+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -50 /root/autodl-tmp/vla-ssd/results/trajectory_level_cohens_d.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -50 /root/autodl-tmp/vla-ssd/results/trajectory_level_cohens_d.json"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-25T22:57:45.256734+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_layer\\\": {\\n    \\\"layer_0\\\": {\\n      \\\"activation_norm_llama2base\\\": 16.50991439819336,\\n      \\\"activation_norm_trained\\\": 16.50991439819336,\\n      \\\"cosine_sim_mean\\\": 1.0,\\n      \\\"cosine_sim_std\\\": 8.248837701785305e-08,\\n      \\\"variance_explained_top10_llama2base\\\": 0.6070719361305237,\\n      \\\"variance_explained_top10_trained\\\": 0.6070719361305237\\n    },\\n    \\\"layer_1\\\": {\\n      \\\"activation_norm_llama2base\\\": 16.55901336669922,\\n      \\\"activation_norm_trained\\\": 17.730854034423828,\\n      \\\"cosine_sim_mean\\\": 0.99040687084198,\\n      \\\"cosine_sim_std\\\": 0.0006290998426266015,\\n      \\\"variance_explained_top10_llama2base\\\": 0.6071038246154785,\\n      \\\"variance_explained_top10_trained\\\": 0.6071761250495911\\n    },\\n    \\\"layer_2\\\": {\\n      \\\"activation_norm_llama2base\\\": 16.76109504699707,\\n      \\\"activation_norm_trained\\\": 22.219118118286133,\\n      \\\"cosine_sim_mean\\\": 0.9401026964187622,\\n      \\\"cosine_sim_std\\\": 0.003356755478307605,\\n      \\\"variance_explained_top10_llama2base\\\": 0.6069490909576416,\\n      \\\"variance_explained_top10_trained\\\": 0.6114932894706726\\n    },\\n    \\\"layer_3\\\": {\\n      \\\"activation_norm_llama2base\\\": 17.382152557373047,\\n      \\\"activation_norm_trained\\\": 23.375831604003906,\\n      \\\"cosine_sim_mean\\\": 0.9136334657669067,\\n      \\\"cosine_sim_std\\\": 0.005947133060544729,\\n      \\\"variance_explained_top10_llama2base\\\": 0.6103928089141846,\\n      \\\"variance_explained_top10_trained\\\": 0.6125209927558899\\n    },\\n    \\\"layer_4\\\": {\\n      \\\"activation_norm_llama2base\\\": 18.4437198638916,\\n      \\\"activation_norm_trained\\\": 24.351722717285156,\\n      \\\"cosine_sim_mean\\\": 0.8848482370376587,\\n      \\\"cosine_sim_std\\\": 0.008445764891803265,\\n      \\\"variance_explained_top10_llama2base\\
…[truncated 7538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1456
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-25T22:57:45.257193+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"demo-level aggregation, paired Cohen's d, bootstrap CI B=10000\\\",\\n  \\\"description\\\": \\\"Each demo's MSE is the mean of its 50 timestep-level MSEs. Cohen's d = mean(demo_mses) / std(demo_mses, ddof=1). Bootstrap CI: 10000 resamples of demo-level values.\\\",\\n  \\\"n_timesteps_per_demo\\\": 50,\\n  \\\"results\\\": [\\n    {\\n      \\\"experiment\\\": \\\"counterfactual\\\",\\n      \\\"condition\\\": \\\"counterfactual_empty\\\",\\n      \\\"token_level_d\\\": 0.968,\\n      \\\"trajectory_level_d\\\": 3.4378,\\n      \\\"ci_lower\\\": 2.9209,\\n      \\\"ci_upper\\\": 4.4475,\\n      \\\"n_demos\\\": 30,\\n      \\\"demo_mses\\\": [\\n        0.082062,\\n        0.068606,\\n        0.053453,\\n        0.091422,\\n        0.105778,\\n        0.087411,\\n        0.079496,\\n        0.080063,\\n        0.091432,\\n        0.088599,\\n        0.06874,\\n        0.097388,\\n        0.083217,\\n        0.083121,\\n        0.060285,\\n        0.088588,\\n        0.059896,\\n        0.08625,\\n        0.079877,\\n        0.060748,\\n        0.034709,\\n        0.048997,\\n        0.049401,\\n        0.043439,\\n        0.037609,\\n        0.049011,\\n        0.051957,\\n        0.068949,\\n        0.037481,\\n        0.048885\\n      ],\\n      \\\"inflation_factor\\\": 0.282\\n    },\\n    {\\n      \\\"experiment\\\": \\\"counterfactual\\\",\\n      \\\"condition\\\": \\\"counterfactual_paraphrased\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1456
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-25T22:57:45.509115+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Bayes|BF10|bayes.factor|posterior",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Bayes|BF10|bayes.factor|posterior",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-25T22:57:45.861837+00:00_

&lt;persisted-output>
Output too large (27KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-reviewer-7b0fefde/636cd266-4398-44cf-91b0-9b9a7debd68a/tool-results/toolu_017Tqi5ffNNK6qnr9ssLN84n.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_survey_instruction_probing.md:54:### 2.1 ★★★ LangForce / BayesianVLA — Information Collapse in VLAs
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_survey_instruction_probing.md:55:- **引用**: Shijie Lian et al. *BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries.* arXiv:2601.15197, Jan 2026.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_survey_instruction_probing.md:57:- **关键发现**: 在 multi-task 场景中，VLA 倾向忽略 language 走 vision shortcut。LangForce 通过 Bayesian decomposition（vision-only prior + language-conditioned posterior）强制模型利用 language。
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_survey_instruction_probing.md:122:| 2 | **LangForce 2026** (BayesianVLA) | **中** | 提出 Information Collapse 理论——我们可以提供 representation-level 证据。他们是 solution paper（提出修复方法），我们是 analysis paper（诊断问题所在）。互补 > 竞争 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/libero_goal_feasibility.md:84:- **Bayesian 解释**: VLAs collapse 到 P(a|o) 而非正确加权 P(a|l,o)。Language 是 secondary conditioning signal
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/report/literature_survey_instruction_probing.md:54:### 2.1 ★★★ LangForce / BayesianVLA — Information Collapse in VLAs
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/report/literature_survey_instruction_probing.md:55:- **引用**: Shijie Lian et al. *BayesianVLA: Bayesian Decomposition of Vision Language Action Models
…[truncated 80 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-25T22:58:05.636763+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ood_diagnostic|representational divergence|cosine.*layer|activation norm",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ood_diagnostic|representational divergence|cosine.*layer|activation norm",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-25T22:58:06.642528+00:00_

121:NORA Goal produces saturated exit-layer cosine distances of $1.0$ for all conditions, with differentiation visible only at earlier layers (L24: wrong $= 0.123$, empty $= 0.098$).
333:\label{sec:ood_diagnostics}
338:Per-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.
340:These diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.
344:\includegraphics[width=\columnwidth]{figures/fig_ood_diagnostics.pdf}
345:\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}
346:\label{fig:ood_diagnostics}
473:The inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\ref{tab:metric_invariance}).
477:\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 1005
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-25T22:58:07.646782+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "trajectory.level|demo.level.*cohen|pseudo.replication|inflation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "trajectory.level|demo.level.*cohen|pseudo.replication|inflation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-25T22:58:08.109023+00:00_

80:Ablating all 24 instruction-dominant heads alters $72.3\%$ of action tokens (token-level $d = 0.65$, trajectory-level $d = 2.943$); control ablation of 8 random heads yields $d = 0.41$ ($29.3\%$ tokens affected), concentrated on the gripper dimension.
230:\paragraph{Trajectory-level aggregation.}
231:Aggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\sim}4\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).
234:Counterfactual trajectory-level $d$ (10 LIBERO-Goal tasks, $N = 100$): wrong $3.798$ (CI $[3.194, 4.938]$), empty $3.438$ ($[2.921, 4.448]$), shuffled $2.595$ ($[2.028, 3.791]$), paraphrased $2.131$ ($[1.740, 2.819]$).
235:Token-level $d$ underestimates trajectory-level effects by ${\times}3.1$--$4.5$, consistent with within-trajectory averaging reducing noise.
236:Fine-grained ordering is not reliably distinguished at trajectory level ($N = 100$); token-level comparisons ($N {\sim} 5{,}000$) provide higher resolution for ordering claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 462
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-25T22:58:08.782535+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cross.representational|projector.*vs.*vla|task difficulty ranking",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cross.representational|projector.*vs.*vla|task difficulty ranking",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-25T22:58:08.885719+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:1123:and (v)~$R^2$ projector vs.\ VLA Spearman correlation ($p = 0.003 \to p_{\text{adj}} = 0.183$).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 103
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-25T22:58:31.078002+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "BayesianVLA|LangForce|Lian.*2026|lian.*vla",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "BayesianVLA|LangForce|Lian.*2026|lian.*vla",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-25T22:58:31.128593+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:176:These probes measure decodability, not causal reliance; with this caveat, the consistent three-way pattern provides a first cross-architecture decomposition of VLA instruction routing.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl:18:  Levine, Liang, and Finn]{kim2024_openvla}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-25T22:58:32.433824+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "grover|hancock|preserving|representation.preserving",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "grover|hancock|preserving|representation.preserving",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-25T22:58:32.936200+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:6:Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; recent VLA-specific work proposes representation-preserving strategies~\cite{grover2025preserving,hancock2025actions}. Existing analyses target single architectures and cannot separate training dynamics from backbone artifacts.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl:155:\bibitem[Grover et~al.(2025)Grover, Gopalkrishnan, Ai, Christensen, Su, and
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl:156:  Li]{grover2025preserving}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl:157:S.~Grover, A.~Gopalkrishnan, B.~Ai, H.~I. Christensen, H.~Su, and X.~Li.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl:159:  preserving pretrained representations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl:162:\bibitem[Hancock et~al.(2025)Hancock, Wu, Zha, Russakovsky, and
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl:163:  Majumdar]{hancock2025actions}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl:164:A.~J. Hancock, X.~Wu, L.~Zha, O.~Russakovsky, and A.~Majumdar.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux:22:\citation{grover2025preserving,hancock2025actions}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux:139:\bibcite{grover2025preserving}{{20}{2025}{{Grover et~al.}}{{Grover, Gopalkrishnan, Ai, Christensen, Su, and Li}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux:140:\bibcite{hancock2025actions}{{21}{2025}{{Hancock et~al.}}{{Hancock, Wu, Zha, Russakovsky, 
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-25T22:58:33.087184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1146",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1146",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-25T22:58:33.137815+00:00_

1146	\subsection{Extended Discussion}
1147	\label{sec:extended_discussion_appendix}
1148	
1149	\paragraph{Observational three-tier gradient.}
1150	The cross-architecture matrix suggests a three-tier gradient of representational adaptation.
1151	Tier~1 (VLM bases, no action training): inherited L1 attention (TracVLA 32/32, NORA 13--14/16), negligible exit collapse ($\Delta R^2 \leq 0.048$), and minimal counterfactual sensitivity (cosine distance $\leq 0.185$).
1152	Tier~2 (general-purpose VLA, OXE-pretrained): strong L1 routing (24--26/32 heads), moderate counterfactual sensitivity ($d \approx 1.0$), and no systematic exit collapse across suites.
1153	Tier~3 (task-specific VLAs, fine-tuned on LIBERO): exit collapse at every VLM-to-VLA cell and medium-to-large counterfactual sensitivity ($d = 0.45$--$1.52$).
1154	This gradient is suggestive but limited: Tier~2 contains a single architecture (OpenVLA), and the Tier~2/Tier~3 boundary confounds training stage with architecture.
1155	Testing additional general-purpose VLAs (e.g., Octo~\cite{ghosh2024_octo}, $\pi_0$~\cite{black2024_pi0}) at Tier~2 is necessary before the three-tier structure can be treated as a robust empirical pattern.
1156	
1157	\paragraph{Exit collapse mechanism.}
1158	One possible explanation for the VLM-to-VLA / VLA-to-VLA asymmetry is that VLM-to-VLA references lack action-relevant exit-layer structure, forcing mid-layer construction without exit preservation (analogous to fine-tuning-induced feature distortion~\cite{kumar2022finetuning}), while VLA-to-VLA references already maintain this structure.
1159	Validating this explanation causally requires controlled training-stage experiments, but the consistency across architectures supports its directional value.
1160	
1161	\paragraph{Behavioral relevance.}
1162	Correlating trained $\Delta R^2$ with published LIBERO success rates across all nine available architecture-suite cells yields a positive but non-significant trend (Spearman $\rho = 0.583$, $p = 
…[truncated 3010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-25T22:59:45.119657+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "coefficient.of.variation|per.task.*vari|task.level.*R2|R2.*distribution|heterogen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "coefficient.of.variation|per.task.*vari|task.level.*R2|R2.*distribution|heterogen",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-25T22:59:45.621996+00:00_

1124:These concern auxiliary comparisons (encoder ranking, coefficient-of-variation ordering) rather than the core redistribution, probing, or counterfactual findings; no main-text conclusion requires revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-25T22:59:46.475652+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "power.*behavioral|required.*n.*correlation|sample.*size.*rho",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "power.*behavioral|required.*n.*correlation|sample.*size.*rho",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-25T22:59:46.526328+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-25T23:00:56.779821+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: warning] 天花板审查——距 Paper DDL (5/29) 4 天，识别 3 个高 ROI 改进点\n\n---\n\n## 1. Rebuttal 弱点分析\n\n### 最薄弱回答：Q1（behavioral correlation underpowered）— 6/10\n\nρ=0.583, p=0.10, n=9 是论文最大的统计软肋。当前 rebuttal 的辩护思路正确（large effect size, within-suite consistency），但**缺少一个关键量化**：post-hoc power analysis for the behavioral correlation itself。\n\n**现状**：appendix line 582 有 R² 和 RSA 的 power analysis，但**没有**行为相关性的 power analysis。这意味着 rebuttal Q1 说\"underpowered\"却没定量说\"多 underpowered\"——审稿人会追问。\n\n**建议补充**（0 GPU·h，纯 Python 计算）：\n- 对 Spearman ρ at |ρ|=0.583, α=0.05 做 post-hoc power analysis\n- 结论大致是：80% power 需 n≈18-20 cells（约 5 architectures × 4 suites）\n- 在 appendix \"Behavioral relevance\"段（line 1162-1167）加 2-3 句，同步更新 rebuttal Q1 引用\n- 效果：从\"we know it's underpowered\"升级为\"we quantify precisely how underpowered, and what future work needs\"，显著提升科学严谨性\n\n其他 Q 的评分：Q2(8/10)、Q3(7/10)、Q4(9/10)、Q5(9/10)、Q6(9/10)、Q7(7/10)、Q8(8/10)、Q9(7/10)。Q8 已有 convergent triangulation（probing + perturbation + ablation dose-response），无需加强。Q7 (N=2) 是硬限制，无轻量级修复。\n\n### 轻量实验可能性\n无 ≤4 GPU·h 的实验能补强 Q1 或 Q7——核心限制是 architecture 数量，不是计算量。唯一可做的是上述 power analysis（0 GPU·h）。\n\n---\n\n## 2. 叙事打磨空间\n\n### [warning] Related Work 遗漏：BayesianVLA / LangForce\n\n项目文献调查 (`literature_survey_instruction_probing.md`) 将 Lian et al. 2026 (arXiv:2601.15197) 标为 ★★★ 高相关：\n- 他们研究 VLA 的 \"Information Collapse\"——模型忽略 language 走 vision shortcut\n- 与本文直接互补：他们提出修复方案（Bayesian decomposition），本文提供诊断工具（ΔR²）\n- **当前论文未引用此工作**——审稿人若知此文会视为遗漏\n\n**建议**：WebSearch 验证论文存在后，在 related_work.tex 第 6 行区域加 1 句话 + 1 条 bib entry。工作量 ~15 min。\n\n### Intro hook + Discussion\n\nIntro hook 功能性足够，不建议最后 4 天改动（风险 > 收益）。Discussion 的 practical implications 段可考虑加一句 functional stages 的具体建议（\"L14-L31 decay phase, ~56% of parameters, may represent pruning candidates\"），但优先级低于上述两项。\n\n---\n\n## 3. Appendix 补充机会\n\n### [info] Cross-probe consistency（已有数据未呈现）\n\n`probe_r2_vs_behavioral_rank_correlation.json` 中有 R²_projector vs R²_vla_L19 across 10 tasks: ρ=0.83, p=0.003。当前仅在 Bonferroni correction section (line 1123) 作为\"correction 后不显著\"一笔带过。\n\n可在 Extended Discussion 中 reframe 为正面方法学验证：\"Cross-probe consistency: different probe placements (projector output vs. L19) agree on task difficulty ranking (ρ=0.83, p=0.003), supporting probe reliability independent of token position.\"——3-4 行，加强 probing methodology 可信度，间接回应 Q8。\n\n注意：此相关性在 Bonferroni correction 后不显著（p_adj=0.183），呈现时需标注\"uncorrected\"或在 methodological validation 语境下使用。\n\n---\n\n## 优先级排序\n\n| 改进 | ROI | 工作量 | GPU·h |\n|------|-----|--------|-------|\n| Q1 power analysis | ★★★ | ~1h (Python + appendix/rebuttal 更新) | 0 |\n| BayesianVLA 引用 | ★★☆ | ~30min (WebSearch + 1 句 + bib) | 0 |\n| Cross-probe consistency | ★☆☆ | ~20min (3-4 行 appendix) | 0 |\n\n三项合计 0 GPU·h，~2h 工时，均不影响现有数字和结论。建议至少完成前两项。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: warning] 天花板审查——距 Paper DDL (5/29) 4 天，识别 3 个高 ROI 改进点\n\n---\n\n## 1. Rebuttal 弱点分析\n\n### 最薄弱回答：Q1（behavioral correlation underpowered）— 6/10\n\nρ=0.583, p=0.10, n=9 是论文最大的统计软肋。当前 rebuttal 的辩护思路正确（large effect size, within-suite consistency），但**缺少一个关键量化**：post-hoc power analysis for the behavioral correlation itself。\n\n**现状**：appendix line 582 有 R² 和 RSA 的 power analysis，但**没有**行为相关性的 power analysis。这意味着 rebuttal Q1 说\"underpowered\"却没定量说\"多 underpowered\"——审稿人会追问。\n\n**建议补充**（0 GPU·h，纯 Python 计算）：\n- 对 Spearman ρ at |ρ|=0.583, α=0.05 做 post-hoc power analysis\n- 结论大致是：80% power 需 n≈18-20 cells（约 5 architectures × 4 suites）\n- 在 appendix \"Behavioral relevance\"段（line 1162-1167）加 2-3 句，同步更新 rebuttal Q1 引用\n- 效果：从\"we know it's underpowered\"升级为\"we quantify precisely how underpowered, and what future work needs\"，显著提升科学严谨性\n\n其他 Q 的评分：Q2(8/10)、Q3(7/10)、Q4(9/10)、Q5(9/10)、Q6(9/10)、Q7(7/10)、Q8(8/10)、Q9(7/10)。Q8 已有 convergent triangulation（probing + perturbation + ablation dose-response），无需加强。Q7 (N=2) 是硬限制，无轻量级修复。\n\n### 轻量实验可能性\n无 ≤4 GPU·h 的实验能补强 Q1 或 Q7——核心限制是 architecture 数量，不是计算量。唯一可做的是上述 power analysis（0 GPU·h）。\n\n---\n\n## 2. 叙事打磨空间\n\n### [warning] Related Work 遗漏：BayesianVLA / LangForce\n\n项目文献调查 (`literature_survey_instruction_probing.md`) 将 Lian et al. 2026 (arXiv:2601.15197) 标为 ★★★ 高相关：\n- 他们研究 VLA 的 \"Information Collapse\"——模型忽略 language 走 vision shortcut\n- 与本文直接互补：他们提出修复方案（Bayesian decomposition），本文提供诊断工具（ΔR²）\n- **当前论文未引用此工作**——审稿人若知此文会视为遗漏\n\n**建议**：WebSearch 验证论文存在后，在 related_work.tex 第 6 行区域加 1 句话 + 1 条 bib entry。工作量 ~15 min。\n\n### Intro hook + Discussion\n\nIntro hook 功能性足够，不建议最后 4 天改动（风险 > 收益）。Discussion 的 practical implications 段可考虑加一句 functional stages 的具体建议（\"L14-L31 decay phase, ~56% of parameters, may represent pruning candidates\"），但优先级低于上述两项。\n\n---\n\n## 3. Appendix 补充机会\n\n### [info] Cross-probe consistency（已有数据未呈现）\n\n`probe_r2_vs_behavioral_rank_correlation.json` 中有 R²_projector vs R²_vla_L19 across 10 tasks: ρ=0.83, p=0.003。当前仅在 Bonferroni correction section (line 1123) 作为\"correction 后不显著\"一笔带过。\n\n可在 Extended Discussion 中 reframe 为正面方法学验证：\"Cross-probe consistency: different probe placements (projector output vs. L19) agree on task difficulty ranking (ρ=0.83, p=0.003), supporting probe reliability independent of token position.\"——3-4 行，加强 probing methodology 可信度，间接回应 Q8。\n\n注意：此相关性在 Bonferroni correction 后不显著（p_adj=0.183），呈现时需标注\"uncorrected\"或在 methodological validation 语境下使用。\n\n---\n\n## 优先级排序\n\n| 改进 | ROI | 工作量 | GPU·h |\n|------|-----|--------|-------|\n| Q1 power analysis | ★★★ | ~1h (Python + appendix/rebuttal 更新) | 0 |\n| BayesianVLA 引用 | ★★☆ | ~30min (WebSearch + 1 句 + bib) | 0 |\n| Cross-probe consistency | ★☆☆ | ~20min (3-4 行 appendix) | 0 |\n\n三项合计 0 GPU·h，~2h 工时，均不影响现有数字和结论。建议至少完成前两项。",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-25T23:01:00.395633+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 3615
}
```

</details>

---

### Assistant

_source line 104 · 2026-05-25T23:01:07.598014+00:00_

天花板审查已发送。总结：

1. **Q1 behavioral correlation power analysis**（最高优先级）——rebuttal 最薄弱环节，0 GPU·h 纯计算即可补强，在 appendix 加 2-3 句定量说明"n≈20 才够 80% power"
2. **BayesianVLA/LangForce 引用遗漏**——文献调查标为高相关但论文未引用，30min 可修复
3. **Cross-probe consistency reframe**——已有数据（ρ=0.83）未充分呈现，可加强 probing 方法可信度

三项均 0 GPU·h，总工时约 2h，不影响现有结论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---

## Round 3

46 recorded events

### User

_source line 105 · 2026-05-25T23:47:06.273567+00:00_

[System 触发审查]:
v14 新增 5 项改进需要审查：

**新增内容**（均在 appendix/related work，无主文数字变动）：
1. NLP Control R² 3-panel 图（fig_nlp_control_r2.pdf）
2. Label Permutation Sanity Check 子节 + bar chart（fig_label_permutation.pdf）
3. Cross-Architecture L1 Bar Chart 引用（fig_cross_arch_l1.pdf）
4. Post-hoc power analysis 2 句（power=0.37, n≥21 for 80%）
5. BayesianVLA (Lian 2026) 引用 1 句 + bib entry

**请审查**：
1. 新增内容是否准确、无矛盾？
2. **主文叙事是否需要同步更新？** 5 项新 appendix 证据加强了 NLP control claim 和 probing reliability——主文是否充分利用（如 §4.3 可引用新图，§6 Limitations 可引用 power analysis）？
3. 新增 BayesianVLA 定位是否准确（"complementary diagnostic" vs "修复方案"的区分）？

不需要重做数字一致性（Loop 13 已验证主文数字未变）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system"
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-25T23:47:20.617339+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fig_nlp_control|nlp_control_r2|label.permutation|fig_label_perm",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fig_nlp_control|nlp_control_r2|label.permutation|fig_label_perm",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-25T23:47:20.617814+00:00_

579:\subsubsection{Label Permutation Sanity Check}
580:\label{sec:label_permutation}
582:To confirm that probe performance reflects genuine action-relevant structure rather than overfitting, we repeat the per-layer action probe with randomly shuffled labels (Figure~\ref{fig:label_permutation}).
588:\includegraphics[width=0.55\columnwidth]{figures/fig_label_permutation.pdf}
589:\caption{\textbf{Label permutation control.} Action-probe Spearman $\rho$ under real versus shuffled labels for OpenVLA trained and untrained conditions. Shuffled-label $\rho$ is indistinguishable from zero, confirming that probe performance reflects genuine representational structure.}
590:\label{fig:label_permutation}
1236:Figure~\ref{fig:nlp_control_r2} overlays the NLP control profiles (dashed gray) against the corresponding VLA trained and reference curves, illustrating the contrast between action-training-induced collapse and the flat NLP baseline across all three backbone families.
1240:\includegraphics[width=\columnwidth]{figures/fig_nlp_control_r2.pdf}
1242:\label{fig:nlp_control_r2}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-25T23:47:22.123278+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "BayesianVLA|LangForce|Lian.*2026|lian.*vla|information.collapse",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "BayesianVLA|LangForce|Lian.*2026|lian.*vla|information.collapse",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-25T23:47:23.077462+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:18:Concurrent work addresses visual representation collapse~\cite{kachaev2025dont} and instruction information collapse~\cite{lian2026bayesianvla} during VLA fine-tuning; our $\Delta R^2$ metric offers a complementary diagnostic for measuring such collapse across architectures.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:176:These probes measure decodability, not causal reliance; with this caveat, the consistent three-way pattern provides a first cross-architecture decomposition of VLA instruction routing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-25T23:47:23.988115+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "power.*0\\.37|n.*21|n.*geq.*21|post.hoc power|sample size.*correlation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "power.*0\\.37|n.*21|n.*geq.*21|post.hoc power|sample size.*correlation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-25T23:47:24.089015+00:00_

51:DINOv2 ViT-L/14~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}) and CLIP ViT-L/14~\cite{radford2021_clip} (\texttt{patch\_mean}) provide self-supervised and vision-language pretrained reference points for probing and RSA.
66:The 32-layer attention profile reveals qualitatively distinct organizations: Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads), while VLA fine-tuning produces an entry-exit bookend pattern with L0--L1 at 21--24 heads, L31 at 18, and intermediate layers at 0--11 (\S\ref{sec:threshold_sensitivity}).
103:OpenVLA & Object  & E\,1.21 & W\,1.19 & S\,1.12 & P\,0.90 \\
158:The two branches yield near-identical RSA: DINOv2 branch $\rho = 0.619$, SigLIP branch $\rho = 0.621$.
232:Instruction-head ablation ($N = 50$: 5 tasks $\times$ 10 demos) yields trajectory $d = 2.943$ (95\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).
234:Counterfactual trajectory-level $d$ (10 LIBERO-Goal tasks, $N = 100$): wrong $3.798$ (CI $[3.194, 4.938]$), empty $3.438$ ($[2.921, 4.448]$), shuffled $2.595$ ($[2.028, 3.791]$), paraphrased $2.131$ ($[1.740, 2.819]$).
326:Instruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\
408:Second, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\Delta_\text{layer}| = 1$).
596:Post-hoc power analysis ($N = 10$ tasks, $\alpha = 0.05$, target power $= 0.80$) indicates minimum detectable effect sizes of $\Delta_{\text{RSA}} = 0.030$ and $\Delta_{R^2} = 0.026$.
818:The full profile (Figure~\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the randomly initialized model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an e
…[truncated 531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-25T23:47:34.929098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "575",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "575",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-25T23:47:36.485370+00:00_

575	\bottomrule
576	\end{tabular}
577	\end{table}
578	
579	\subsubsection{Label Permutation Sanity Check}
580	\label{sec:label_permutation}
581	
582	To confirm that probe performance reflects genuine action-relevant structure rather than overfitting, we repeat the per-layer action probe with randomly shuffled labels (Figure~\ref{fig:label_permutation}).
583	Under permuted labels, Spearman $\rho$ drops from $0.955$ to $0.001$ (trained) and from $0.933$ to $0.000$ (untrained), with all 33 layers producing $|\rho| < 0.013$.
584	This establishes that the high probe accuracy reported throughout the paper is attributable to learned action-relevant representations, not probe capacity artifacts.
585	
586	\begin{figure}[h]
587	\centering
588	\includegraphics[width=0.55\columnwidth]{figures/fig_label_permutation.pdf}
589	\caption{\textbf{Label permutation control.} Action-probe Spearman $\rho$ under real versus shuffled labels for OpenVLA trained and untrained conditions. Shuffled-label $\rho$ is indistinguishable from zero, confirming that probe performance reflects genuine representational structure.}
590	\label{fig:label_permutation}
591	\end{figure}
592	
593	\subsubsection{Statistical Power}
594	\label{sec:statistical_power}
595	
596	Post-hoc power analysis ($N = 10$ tasks, $\alpha = 0.05$, target power $= 0.80$) indicates minimum detectable effect sizes of $\Delta_{\text{RSA}} = 0.030$ and $\Delta_{R^2} = 0.026$.
597	The observed RSA training effect ($\Delta = 0.017$, Cohen's $d_z = 0.56$) achieves power $= 0.356$, confirming the analysis is underpowered for this effect size; the non-significant RSA result (\S\ref{sec:routing_synthesis}) should not be interpreted as evidence of absence.
598	The observed $R^2$ readout effect ($\Delta = 0.069$, $d_z = 2.68$) achieves power $= 1.000$, confirming adequate sensitivity for the primary functional metric.
599	
600	\subsubsection{$\Delta R^2$ Threshold Robustness}
601	\label{sec:delta_r2_threshold}
602	
603	The main text classifi
…[truncated 285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 1556
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-25T23:47:36.737120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1185",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1185",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-25T23:47:36.787915+00:00_

1185	Validating this explanation causally requires controlled training-stage experiments, but the consistency across architectures supports its directional value.
1186	
1187	\paragraph{Behavioral relevance.}
1188	Correlating trained $\Delta R^2$ with published LIBERO success rates across all nine available architecture-suite cells yields a positive but non-significant trend (Spearman $\rho = 0.583$, $p = 0.10$, $n = 9$), marginally above the conventional significance threshold.
1189	Within-suite comparisons, which control for task difficulty, are uniformly positive: on Goal ($n = 3$ architectures), $\Delta R^2$ and success rate are perfectly rank-correlated ($\rho = 1.0$), and every remaining suite ($n = 2$ each) shows the same direction.
1190	This directional evidence is consistent with stronger mid-network action encoding (higher peak $R^2$) followed by more aggressive exit-layer compression being associated with better task performance.
1191	Several caveats temper this interpretation: architecture capacity differences (model size, backbone quality) are not controlled, suite difficulty co-varies with both $\Delta R^2$ and success rate, multiple suites from the same architecture are not independent observations, and the sample size limits statistical power.
1192	Post-hoc power analysis (Fisher $Z$-transform, two-tailed $\alpha = 0.05$) yields achieved power $= 0.37$ at $n = 9$; reaching $80\%$ power would require $n \geq 21$ architecture-suite cells.
1193	The current analysis is therefore underpowered, and the non-significant $p$-value should not be interpreted as evidence of absence; it reflects insufficient sample size rather than a weak effect.
1194	This correlational evidence does not establish a causal link between exit collapse and task success.
1195	Closed-loop behavioral validation, including intervention experiments that directly manipulate exit-layer representations, remains a priority for future work.
1196	
1197	\paragraph{Closed-loop evaluation attempt.
…[truncated 1822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-25T23:47:37.089431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1228",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1228",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-25T23:47:37.190274+00:00_

1228	Phi-3-mini-4k-instruct & TracVLA (Phi-3-mini) & 0.000 & $0.155 \pm 0.000$ & 32 \\
1229	Qwen2.5-3B-Instruct$^{*}$ & NORA (Qwen2.5-VL-3B) & 0.000 & $0.155 \pm 0.000$ & 36 \\
1230	\bottomrule
1231	\multicolumn{5}{l}{\footnotesize $^{*}$Qwen2.5-3B-Instruct shares the Qwen2.5 language backbone with NORA's}\\
1232	\multicolumn{5}{l}{\footnotesize Qwen2.5-VL-3B but lacks the vision encoder and cross-attention modules.}\\
1233	\end{tabular}
1234	\end{table}
1235	
1236	Figure~\ref{fig:nlp_control_r2} overlays the NLP control profiles (dashed gray) against the corresponding VLA trained and reference curves, illustrating the contrast between action-training-induced collapse and the flat NLP baseline across all three backbone families.
1237	
1238	\begin{figure}[h]
1239	\centering
1240	\includegraphics[width=\columnwidth]{figures/fig_nlp_control_r2.pdf}
1241	\caption{\textbf{NLP finetuning controls produce flat $R^2$ profiles.} Each panel shows the VLA trained (blue) and reference (orange) per-layer action-probe $R^2$ alongside the NLP control (dashed gray, $R^2 = 0.155$) for the matching backbone family. VLM-to-VLA transitions exhibit peak-to-exit collapse; NLP controls remain flat ($\Delta R^2 = 0.000$) in all three cases.}
1242	\label{fig:nlp_control_r2}
1243	\end{figure}
1244	
1245	\subsection{Claim-Evidence Summary}
1246	\label{sec:claim_evidence_appendix}
1247	
1248	\begin{figure}[h]
1249	\centering
1250	\includegraphics[width=\columnwidth]{figures/fig_claim_evidence.pdf}
1251	\caption{\textbf{Claim--evidence--scope summary.} Each main finding is paired with its supporting analysis and its main limitation. The figure distinguishes directly observed representational patterns from stronger causal interpretations that require interventional or training-dynamics evidence.}
1252	\label{fig:claim_evidence}
1253	\end{figure}
1254	
1255	\subsection{Cross-Architecture Design Rationale}
1256	\label{sec:cross_arch_rationale}
1257	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-25T23:47:43.534406+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-25T23:47:44.438372+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce actions from visual and language input~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora,xiao2025ava}.
5	NLP instruction tuning is well-characterized behaviorally~\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.
6	Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; recent VLA-specific work proposes representation-preserving strategies~\cite{grover2025preserving,hancock2025actions}. Existing analyses target single architectures and cannot separate training dynamics from backbone artifacts.
7	
8	\paragraph{Mechanistic and behavioral analysis.}
9	Mechanistic interpretability has revealed residual stream communication~\cite{elhage2021}, induction heads~\cite{olsson2022}, and task circuits~\cite{wang2023_ioi,conmy2023}; causal tracing localizes factual recall~\cite{meng2022_rome}; attention probing shows heads encode syntactic relations~\cite{clark2019} and most can be pruned~\cite{michel2019sixteen}.
10	In VLMs, recent work characterizes visual token redundancy~\cite{fan2026visual}, progressive visual-textual alignment~\cite{neo2025interpreting,long2026understanding}, and instruction tokens as shallow-layer modality arbitration anchors~\cite{zhang2026instruction}.
11	Behavioral evaluations of VLAs reveal visual dominance~\cite{grant2026,hou2026,fei2025}; mechanistic studies identify sparse semantic directions~\cite{haon2025}, interpretable features~\cite{swann2026,buurmeijer2026}, symbolic representations~\cite{lu2025,molinari2025}, comprehension-action trade-offs~\cite{fang2025}, and task-specific attention heads for selective fine-tuning~\cite{mitra2025mechanistic}.
12	Concurrent continual-learning
…[truncated 1779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-25T23:47:45.943853+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "lian2026|bayesianvla",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "-A": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "lian2026|bayesianvla",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "-A": "8"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-25T23:47:46.446114+00:00_

10:@article{lian2026bayesianvla,
11:  title     = {{BayesianVLA}: {B}ayesian Decomposition of Vision Language Action Models via Latent Action Queries},
12-  author    = {Lian, Shijie and others},
13-  journal   = {arXiv preprint arXiv:2601.15197},
14-  year      = {2026},
15-}
16-
17-@article{kachaev2025dont,
18-  title     = {Don't Blind Your {VLA}: Aligning Visual Representations for {OOD} Generalization},
19-  author    = {Kachaev, Nikita and Lyzhov, Alexander and Konovalov, Vladislav and Panov, Aleksandr},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-25T23:47:46.446547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "offset": "55",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "offset": "55",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-25T23:47:46.497079+00:00_

55	
56	\paragraph{NLP finetuning control.}
57	To test whether exit collapse is specific to action-oriented training, we probe three chat-finetuned models that share backbones with our VLAs but lack action heads or robot data: Llama-2-7b-chat (OpenVLA), Phi-3-mini-4k-instruct (TracVLA), and Qwen2.5-3B-Instruct (NORA).\footnote{Qwen2.5-3B-Instruct shares the Qwen2.5 language backbone with NORA's Qwen2.5-VL-3B but lacks the vision encoder and cross-attention modules; see Appendix~\ref{sec:nlp_control_appendix}.}
58	All three produce flat $R^2$ profiles ($\Delta R^2 = 0.000$; $R^2 = 0.155 \pm 0.001$, $0.155 \pm 0.000$, and $0.155 \pm 0.000$ respectively; Appendix~\ref{sec:nlp_control_appendix}), contrasting with VLM-to-VLA collapse ($\Delta R^2 = 0.156$--$0.455$).
59	The absence of exit collapse in any NLP control is inconsistent with exit collapse being a generic consequence of language-model fine-tuning.
60	\textbf{In sum, exit collapse is consistently associated with VLM-to-VLA transitions and absent in both VLA-to-VLA and NLP-only fine-tuning.}
61	
62	\begin{table}[t]
63	\centering
64	\caption{\textbf{Peak-to-exit action-probe drop across the architecture-suite matrix.} $\Delta R^2$ is computed as the difference between the maximum layer-wise action-probe $R^2$ and the exit-layer $R^2$. Values above 0.10 are treated as substantial descriptive drops. OpenVLA is a VLA-to-VLA comparison, whereas TracVLA and NORA are VLM-to-VLA comparisons.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-25T23:47:52.920806+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fig_cross_arch_l1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fig_cross_arch_l1",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-25T23:47:53.874837+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.fls:374:INPUT ./figures/fig_cross_arch_l1.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.fls:375:INPUT ./figures/fig_cross_arch_l1.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.fls:376:INPUT ./figures/fig_cross_arch_l1.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.fls:377:INPUT ./figures/fig_cross_arch_l1.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.fls:378:INPUT ./figures/fig_cross_arch_l1.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log:837:&lt;figures/fig_cross_arch_l1.pdf, id=1774, 489.34944pt x 308.18323pt>
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log:838:File: figures/fig_cross_arch_l1.pdf Graphic file (type pdf)
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log:839:&lt;use figures/fig_cross_arch_l1.pdf>
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log:840:Package pdftex.def Info: figures/fig_cross_arch_l1.pdf  used on input line 796.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log:880: [30 <./figures/fig_cross_arch_l1.pdf> <./figures/fig_l1_stacked_bar.pdf>]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:796:\includegraphics[width=0.65\columnwidth]{figures/fig_cross_arch_l1.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.fdb_latexmk:152:  "figures/fig_cross_arch_l1.pdf" 1779432422.54411 17060 22e11a5f202a1243bbbf2d934aa2b71d ""

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-25T23:47:53.875228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-25T23:47:55.280824+00:00_

1	\enlargethispage{2\baselineskip}
2	\section{Discussion and Conclusion}
3	\label{sec:discussion}
4	\vspace{-4pt}
5	
6	\paragraph{Scope and limitations.}\looseness=-1
7	All findings are correlational (confounded by data distribution and optimization; $N = 2$ VLM-to-VLA transitions; Appendix~\ref{sec:claim_evidence_appendix}); we analyze causal-decoder VLAs on LIBERO only (flow-matching~\cite{black2024_pi0} and diffusion~\cite{ghosh2024_octo} architectures may differ); all analyses are open-loop.
8	Trained $\Delta R^2$ correlates with published success rates ($\rho = 0.583$, $p = 0.10$; Appendix~\ref{sec:extended_discussion_appendix}) but is underpowered ($n = 9$; effect size is large, $|\rho| > 0.5$); tracing collapse onset remains for future work.
9	
10	\paragraph{Practical implications.}\looseness=-1
11	$\Delta R^2$ provides a cheap diagnostic ($> 0.10$ signals reorganization); preserved VLA-to-VLA exit structure justifies staged pipelines; mid-layer probes outperform exit-layer probes where collapse is pronounced (Appendix~\ref{sec:extended_discussion_appendix}).
12	
13	\vspace{-2pt}
14	\paragraph{Conclusion.}\looseness=-1
15	Across three architectures and four LIBERO suites, VLM-to-VLA fine-tuning produces exit collapse ($\Delta R^2 = 0.16$--$0.46$) while VLA-to-VLA conditions remain flat ($< 0.10$).
16	All trained VLAs show graded counterfactual sensitivity ($d = 0.45$--$1.52$); L1 instruction attention is inherited from pretrained backbones; NLP controls ($\Delta R^2 = 0.000$) confirm transition-type specificity, providing reusable diagnostics for future VLA evaluation and training pipeline design.
17	Code and data will be released upon acceptance.
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 1405
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-25T23:47:55.684164+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_nlp_control_r2.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_label_permutation.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_cross_arch_l1.pdf 2>&1",
  "description": "Check if new figure PDFs exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_nlp_control_r2.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_label_permutation.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_cross_arch_l1.pdf 2>&1",
    "description": "Check if new figure PDFs exist"
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-25T23:47:55.885805+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_cross_arch_l1.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_label_permutation.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_nlp_control_r2.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-25T23:48:10.391211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "788",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "788",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-25T23:48:10.442135+00:00_

788	
789	\subsubsection{Cross-Architecture L1 Instruction Dominance}
790	\label{sec:cross_arch_l1}
791	
792	Figure~\ref{fig:cross_arch_l1_bar} complements the main-text summary (Figure~\ref{fig:cross_arch_l1}) by showing the fraction of instruction-dominant heads at L1 across all three architectures in a single comparison. The trained/untrained fractions are comparable within each architecture (OpenVLA: 23/32 vs.\ 26/32; TracVLA: 27/32 vs.\ 32/32; NORA: 13/16 vs.\ 13/16), consistent with L1 instruction attention being largely inherited from the pretrained backbone rather than acquired during VLA fine-tuning.
793	
794	\begin{figure}[h]
795	\centering
796	\includegraphics[width=0.65\columnwidth]{figures/fig_cross_arch_l1.pdf}
797	\caption{\textbf{L1 instruction-dominant head fractions across three architectures.} Trained and untrained conditions show comparable fractions in all three VLAs, indicating that L1 instruction attention largely pre-exists in the pretrained backbone.}
798	\label{fig:cross_arch_l1_bar}
799	\end{figure}
800	
801	\subsubsection{L1 Attention Pattern Analysis}
802	\label{sec:attention_pattern}
803	
804	Figure~\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.
805	The three-level gradient (randomly initialized 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction attention and VLA fine-tuning shifts it further toward instruction dominance.
806	
807	\begin{figure}[h]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-25T23:49:31.133126+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "lian2026",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl",
  "output_mode": "content",
  "-n": "True",
  "-A": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "lian2026",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl",
    "output_mode": "content",
    "-n": "True",
    "-A": "5"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-25T23:49:31.585290+00:00_

318:\bibitem[Lian et~al.(2026)]{lian2026bayesianvla}
319-S.~Lian et~al.
320-\newblock {BayesianVLA}: {B}ayesian decomposition of vision language action
321-  models via latent action queries.
322-\newblock \emph{arXiv preprint arXiv:2601.15197}, 2026.
323-

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-25T23:49:32.689747+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Warning.*lian|undefined.*lian|Citation.*lian",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Warning.*lian|undefined.*lian|Citation.*lian",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-25T23:49:33.292558+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 602
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-25T23:49:33.945284+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "label_permutation|fig_label_perm|fig_nlp_control",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "label_permutation|fig_label_perm|fig_nlp_control",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-25T23:49:34.046176+00:00_

777:&lt;figures/fig_label_permutation.pdf, id=1686, 349.04214pt x 276.87314pt>
778:File: figures/fig_label_permutation.pdf Graphic file (type pdf)
779:&lt;use figures/fig_label_permutation.pdf>
780:Package pdftex.def Info: figures/fig_label_permutation.pdf  used on input line 
810:[26 <./figures/fig_label_permutation.pdf>] [27]
936:&lt;figures/fig_nlp_control_r2.pdf, id=2204, 1084.94249pt x 291.06995pt>
937:File: figures/fig_nlp_control_r2.pdf Graphic file (type pdf)
938:&lt;use figures/fig_nlp_control_r2.pdf>
939:Package pdftex.def Info: figures/fig_nlp_control_r2.pdf  used on input line 124
955:[38 <./figures/fig_nlp_control_r2.pdf>]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-25T23:49:51.222242+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/trained_label_perm/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/trained_label_perm/"
  }
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-25T23:49:52.026295+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -30 /root/autodl-tmp/vla-ssd/results/trained_label_perm/label_permutation_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -30 /root/autodl-tmp/vla-ssd/results/trained_label_perm/label_permutation_results.json"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-25T23:49:52.327882+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"temporal_distance\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1105
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-25T23:49:52.830118+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"head: cannot open '/root/autodl-tmp/vla-ssd/results/trained_label_perm/label_permutation_results.json' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 803
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-25T23:49:58.250903+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*label_perm*\" -o -name \"*permut*label*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*label_perm*\" -o -name \"*permut*label*\""
  }
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-25T23:49:58.702815+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-25T23:49:58.803677+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 552
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-25T23:49:59.255663+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"layer_0.json\\nlayer_1.json\\nlayer_10.json\\nlayer_11.json\\nlayer_12.json\\nlayer_13.json\\nlayer_14.json\\nlayer_15.json\\nlayer_16.json\\nlayer_17.json\\nlayer_18.json\\nlayer_19.json\\nlayer_2.json\\nlayer_20.json\\nlayer_21.json\\nlayer_22.json\\nlayer_23.json\\nlayer_24.json\\nlayer_25.json\\nlayer_26.json\\nlayer_27.json\\nlayer_28.json\\nlayer_29.json\\nlayer_3.json\\nlayer_30.json\\nlayer_31.json\\nlayer_32.json\\nlayer_4.json\\nlayer_5.json\\nlayer_6.json\\nlayer_7.json\\nlayer_8.json\\nlayer_9.json\\nsummary.csv\\nsummary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-25T23:50:02.669768+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.json"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-25T23:50:03.272598+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"probe_type\\\": \\\"temporal_distance\\\",\\n  \\\"n_entries\\\": 33,\\n  \\\"results\\\": {\\n    \\\"0\\\": {\\n      \\\"spearman_rho\\\": 0.0,\\n      \\\"spearman_p\\\": 1.0,\\n      \\\"r2\\\": -0.0001577138900756836,\\n      \\\"mae\\\": 0.24749204516410828,\\n      \\\"val_loss\\\": 0.08135151863098145,\\n      \\\"epochs_trained\\\": 6,\\n      \\\"layer\\\": 0,\\n      \\\"per_task_rho\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": 0.0,\\n        \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": 0.0\\n      },\\n      \\\"per_task_n_pairs\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 5000,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 5000,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_che
…[truncated 7080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 602
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-25T23:51:37.942595+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: warning] v14 新增 5 项审查报告\n\n---\n\n## 1. 内容准确性审查\n\n### ✅ Power analysis（appendix line 1192）\n\"power = 0.37 at n = 9; n ≥ 21 for 80% power\" — **数学验证通过**。Fisher Z-transform: z = arctanh(0.583) = 0.668, SE = 1/√(n-3) = 0.408, noncentrality = 0.668×√6 = 1.636, power = Φ(1.636 - 1.96) = 0.373 ≈ 0.37。n=21: power = Φ(0.668×√18 - 1.96) = Φ(0.874) = 0.809。✅\n\n### ✅ Label Permutation（appendix lines 579-584）\n服务器数据交叉验证：`trained_label_perm/temporal_distance/summary.json` 显示 best_rho = 0.0125（across 33 layers），与论文声明\"|ρ| < 0.013\"一致。所有 33 层的 shuffled ρ 均 <0.03。✅\n\n### ✅ NLP Control R² 图（appendix lines 1236-1243）\nCaption 称 \"dashed gray, R² = 0.155\"，与主文 §4.3 (line 58) 报告的三组 NLP control 值（0.155 ± 0.001, 0.155 ± 0.000, 0.155 ± 0.000）一致。✅\n\n### ✅ Cross-arch L1 bar chart（appendix lines 789-799）\nOpenVLA 23/32 vs 26/32, TracVLA 27/32 vs 32/32, NORA 13/16 vs 13/16 — 均在主文 experiments.tex:150-153 报告的范围内（trained 14-24/32, ref 24-26/32 等，套间变异正常）。✅\n\n### ✅ BayesianVLA citation（related_work.tex:18 + references.bib）\n- .bbl 正确编译为 `\\bibitem[Lian et~al.(2026)]{lian2026bayesianvla}`，无 LaTeX warning ✅\n- `author = {Lian, Shijie and others}` 在 bib 中偏简略（理想情况应列全部作者），但 bibtex 正确处理为 \"et al.\"，编译产出无误 ✅\n\n**所有 5 项新增内容无数字矛盾。**\n\n---\n\n## 2. 主文同步建议\n\n### [warning] §4.6 Synthesis 应引用 label permutation\n\nexperiments.tex:176 当前文字：\n> \"These probes measure decodability, not causal reliance; with this caveat...\"\n\n建议改为：\n> \"These probes measure decodability, not causal reliance (label-permutation controls confirm genuine structure; Appendix~\\ref{sec:label_permutation}); with this caveat...\"\n\n**理由**：Label permutation 是直接回应 Q8（probing ≠ causal reliance）最强的方法学防线之一。当前 appendix 有这个控制实验，主文却未引用——审稿人在主文读到 \"decodability, not causal reliance\" 时看不到这个 evidence 的存在。加一个括号引用零空间成本，显著提升论证链完整性。\n\n### [info] §4.3 NLP control 段可选引用新图\n\nexperiments.tex:58 末尾 \"Appendix~\\ref{sec:nlp_control_appendix}\" 可考虑加 \", Figure~\\ref{fig:nlp_control_r2}\"。纯可发现性改善，非必须。\n\n### [info] Discussion §6 power analysis 引用\n\nDiscussion line 8 已写 \"underpowered (n=9)\"，appendix 现在有具体数字（power=0.37, n≥21）。可在主文补 \"(power = 0.37; Appendix~\\ref{sec:extended_discussion_appendix})\"，但 Discussion 空间极紧（已用 \\enlargethispage），视排版余量决定。\n\n---\n\n## 3. BayesianVLA 定位审查\n\n### [info] 定位准确，措辞可微调\n\n当前（related_work.tex:18）：\n> \"Concurrent work addresses visual representation collapse~\\cite{kachaev2025dont} and **instruction information collapse**~\\cite{lian2026bayesianvla} during VLA fine-tuning; our $\\Delta R^2$ metric offers a **complementary diagnostic** for measuring such collapse across architectures.\"\n\n**定位判断**：准确。Lian et al. 是 solution paper（提出 BayesianVLA 修复 VLA 忽略 language 的问题），本文是 analysis paper（提供 ΔR² 诊断工具）。\"complementary diagnostic\" 正确传达了「互补」关系，没有越界声称本文也提供了修复方案。\n\n**微调建议**（optional）：\"instruction information collapse\" 是本文的 paraphrase——Lian et al. 原文可能用 \"information collapse\" 或 \"language shortcut\"。如果能快速 WebSearch 核实他们的原始术语，用原始术语更安全。但当前措辞不构成误引，优先级低。\n\n---\n\n## 4. 额外发现\n\n### [info] Label permutation baseline ρ = 0.955 的 metric 语境\n\nLabel permutation section 报告 real-label Spearman ρ = 0.955（trained），对应 R² ≈ 0.91。主文 demo-split R² 为 0.4-0.6。差异源于 label permutation 可能用 random-split 评估（与 method.tex:52 描述的 inflated R² 一致）。**这不影响 sanity check 的有效性**（关键是 shuffled → 0），但审稿人可能问 \"为什么 baseline ρ = 0.955 这么高？\"如果 label permutation 确实用 random-split，建议在 caption 或文字中加一句注明 \"(evaluated with random splitting; demo-level split values are lower, §3.3)\"，预防审稿人困惑。\n\n---\n\n## 总结\n\n| 项目 | 结论 |\n|------|------|\n| Power analysis 数学 | ✅ PASS |\n| Label permutation 数据 | ✅ PASS |\n| NLP control R² 图 | ✅ PASS |\n| Cross-arch L1 图 | ✅ PASS |\n| BayesianVLA 引用 | ✅ PASS（定位准确）|\n| 主文同步 | ⚠️ §4.6 应引用 label permutation |\n\n5 项新增内容全部准确无矛盾。唯一 warning 级建议：在主文 §4.6 加一个括号引用 label permutation appendix section。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: warning] v14 新增 5 项审查报告\n\n---\n\n## 1. 内容准确性审查\n\n### ✅ Power analysis（appendix line 1192）\n\"power = 0.37 at n = 9; n ≥ 21 for 80% power\" — **数学验证通过**。Fisher Z-transform: z = arctanh(0.583) = 0.668, SE = 1/√(n-3) = 0.408, noncentrality = 0.668×√6 = 1.636, power = Φ(1.636 - 1.96) = 0.373 ≈ 0.37。n=21: power = Φ(0.668×√18 - 1.96) = Φ(0.874) = 0.809。✅\n\n### ✅ Label Permutation（appendix lines 579-584）\n服务器数据交叉验证：`trained_label_perm/temporal_distance/summary.json` 显示 best_rho = 0.0125（across 33 layers），与论文声明\"|ρ| < 0.013\"一致。所有 33 层的 shuffled ρ 均 <0.03。✅\n\n### ✅ NLP Control R² 图（appendix lines 1236-1243）\nCaption 称 \"dashed gray, R² = 0.155\"，与主文 §4.3 (line 58) 报告的三组 NLP control 值（0.155 ± 0.001, 0.155 ± 0.000, 0.155 ± 0.000）一致。✅\n\n### ✅ Cross-arch L1 bar chart（appendix lines 789-799）\nOpenVLA 23/32 vs 26/32, TracVLA 27/32 vs 32/32, NORA 13/16 vs 13/16 — 均在主文 experiments.tex:150-153 报告的范围内（trained 14-24/32, ref 24-26/32 等，套间变异正常）。✅\n\n### ✅ BayesianVLA citation（related_work.tex:18 + references.bib）\n- .bbl 正确编译为 `\\bibitem[Lian et~al.(2026)]{lian2026bayesianvla}`，无 LaTeX warning ✅\n- `author = {Lian, Shijie and others}` 在 bib 中偏简略（理想情况应列全部作者），但 bibtex 正确处理为 \"et al.\"，编译产出无误 ✅\n\n**所有 5 项新增内容无数字矛盾。**\n\n---\n\n## 2. 主文同步建议\n\n### [warning] §4.6 Synthesis 应引用 label permutation\n\nexperiments.tex:176 当前文字：\n> \"These probes measure decodability, not causal reliance; with this caveat...\"\n\n建议改为：\n> \"These probes measure decodability, not causal reliance (label-permutation controls confirm genuine structure; Appendix~\\ref{sec:label_permutation}); with this caveat...\"\n\n**理由**：Label permutation 是直接回应 Q8（probing ≠ causal reliance）最强的方法学防线之一。当前 appendix 有这个控制实验，主文却未引用——审稿人在主文读到 \"decodability, not causal reliance\" 时看不到这个 evidence 的存在。加一个括号引用零空间成本，显著提升论证链完整性。\n\n### [info] §4.3 NLP control 段可选引用新图\n\nexperiments.tex:58 末尾 \"Appendix~\\ref{sec:nlp_control_appendix}\" 可考虑加 \", Figure~\\ref{fig:nlp_control_r2}\"。纯可发现性改善，非必须。\n\n### [info] Discussion §6 power analysis 引用\n\nDiscussion line 8 已写 \"underpowered (n=9)\"，appendix 现在有具体数字（power=0.37, n≥21）。可在主文补 \"(power = 0.37; Appendix~\\ref{sec:extended_discussion_appendix})\"，但 Discussion 空间极紧（已用 \\enlargethispage），视排版余量决定。\n\n---\n\n## 3. BayesianVLA 定位审查\n\n### [info] 定位准确，措辞可微调\n\n当前（related_work.tex:18）：\n> \"Concurrent work addresses visual representation collapse~\\cite{kachaev2025dont} and **instruction information collapse**~\\cite{lian2026bayesianvla} during VLA fine-tuning; our $\\Delta R^2$ metric offers a **complementary diagnostic** for measuring such collapse across architectures.\"\n\n**定位判断**：准确。Lian et al. 是 solution paper（提出 BayesianVLA 修复 VLA 忽略 language 的问题），本文是 analysis paper（提供 ΔR² 诊断工具）。\"complementary diagnostic\" 正确传达了「互补」关系，没有越界声称本文也提供了修复方案。\n\n**微调建议**（optional）：\"instruction information collapse\" 是本文的 paraphrase——Lian et al. 原文可能用 \"information collapse\" 或 \"language shortcut\"。如果能快速 WebSearch 核实他们的原始术语，用原始术语更安全。但当前措辞不构成误引，优先级低。\n\n---\n\n## 4. 额外发现\n\n### [info] Label permutation baseline ρ = 0.955 的 metric 语境\n\nLabel permutation section 报告 real-label Spearman ρ = 0.955（trained），对应 R² ≈ 0.91。主文 demo-split R² 为 0.4-0.6。差异源于 label permutation 可能用 random-split 评估（与 method.tex:52 描述的 inflated R² 一致）。**这不影响 sanity check 的有效性**（关键是 shuffled → 0），但审稿人可能问 \"为什么 baseline ρ = 0.955 这么高？\"如果 label permutation 确实用 random-split，建议在 caption 或文字中加一句注明 \"(evaluated with random splitting; demo-level split values are lower, §3.3)\"，预防审稿人困惑。\n\n---\n\n## 总结\n\n| 项目 | 结论 |\n|------|------|\n| Power analysis 数学 | ✅ PASS |\n| Label permutation 数据 | ✅ PASS |\n| NLP control R² 图 | ✅ PASS |\n| Cross-arch L1 图 | ✅ PASS |\n| BayesianVLA 引用 | ✅ PASS（定位准确）|\n| 主文同步 | ⚠️ §4.6 应引用 label permutation |\n\n5 项新增内容全部准确无矛盾。唯一 warning 级建议：在主文 §4.6 加一个括号引用 label permutation appendix section。",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-25T23:51:41.634141+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 3691
}
```

</details>

---

### Assistant

_source line 150 · 2026-05-25T23:51:45.446689+00:00_

v14 审查完成。5 项新增全部数据验证通过，无矛盾。唯一 warning 级建议：主文 §4.6 Synthesis 应加括号引用 label permutation appendix section，作为 probing reliability 的方法学防线。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---

## Round 4

16 recorded events

### User

_source line 151 · 2026-05-26T00:25:06.130690+00:00_

[System 触发审查]:
两个审查请求：

**请求 1（critical challenge）：n=9 是否真的无法扩展？**

当前判断是"n=9 behavioral correlation 需要新 VLA 架构才能扩展，不是 GPU·h 问题"。请严格 challenge 这个判断：

- 现有 3 架构 × 4 suites = 12 cells（10 filled, 1 excluded = 9 usable）。有没有办法在不引入新架构的前提下增加 n？
- **Sub-split**：能否把每个 cell 拆成多个独立 sub-samples（如 per-demo 或 per-task-variant），对每个 sub-sample 独立计算 ΔR² 和 SR，得到更多 data points？
- **Synthetic augmentation**：能否对现有 demo 做 augmentation（noise injection、frame sampling 变体）产生独立 ΔR² 估计？
- **Bootstrap resampling**：能否用 bootstrap 产生 pseudo-independent samples 来做 correlation？（可能不合法——请评估统计有效性）
- **Cross-layer**：不同 layer 的 ΔR² 算不同 observation？（可能违反独立性——请评估）

如果任何方法在统计上合法且可用 GPU 在 4h 内计算，报告具体方案。如果全部不合法，给出明确理由，我存档到 decisions.yaml 终结这个讨论。

**请求 2：Paper DDL 3 天内还能做什么？**

Rebuttal Q3 (closed-loop SR=0)、Q7 (N=2 transitions)、Q9 (training dynamics) 的回答分别 7/10。有没有任何 appendix 补充（0 GPU 或 ≤2 GPU·h）能把这三个中的任何一个提升 1 分？比如：
- Q9：能否从现有 10 cells 的数据推导出 coarse-grained dynamics insight 并可视化？
- Q3：能否加一个 "representational analysis vs behavioral evaluation" 的 methodological precedent 表格？
- 其他你认为高 ROI 的补充？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system"
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-26T00:26:37.935107+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/sr_corrected_3ep.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/sr_corrected_3ep.json"
  }
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-26T00:26:38.838337+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -40 /root/autodl-tmp/vla-ssd/results/random_subset_ablation.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -40 /root/autodl-tmp/vla-ssd/results/random_subset_ablation.json"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-26T00:26:39.240346+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": \\\"256x256_crop224_flip_native_predict\\\",\\n  \\\"task\\\": \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n  \\\"instruction\\\": \\\"open the middle drawer of the cabinet\\\",\\n  \\\"episodes\\\": [\\n    {\\n      \\\"success\\\": false,\\n      \\\"reward\\\": 0.0,\\n      \\\"steps\\\": 400\\n    },\\n    {\\n      \\\"success\\\": false,\\n      \\\"reward\\\": 0.0,\\n      \\\"steps\\\": 400\\n    },\\n    {\\n      \\\"success\\\": false,\\n      \\\"reward\\\": 0.0,\\n      \\\"steps\\\": 400\\n    }\\n  ],\\n  \\\"sr\\\": 0.0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1305
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-26T00:26:39.742545+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"baseline_r2\\\": 0.5169,\\n  \\\"dominant_24_r2\\\": 0.5592,\\n  \\\"dominant_24_r2_increase\\\": 0.0423,\\n  \\\"dominant_24_heads\\\": [\\n    0,\\n    1,\\n    2,\\n    4,\\n    7,\\n    8,\\n    10,\\n    11,\\n    12,\\n    14,\\n    15,\\n    16,\\n    17,\\n    18,\\n    19,\\n    20,\\n    22,\\n    23,\\n    25,\\n    26,\\n    27,\\n    29,\\n    30,\\n    31\\n  ],\\n  \\\"random_iterations\\\": [\\n    {\\n      \\\"seed\\\": 0,\\n      \\\"r2\\\": 0.5896,\\n      \\\"r2_increase\\\": 0.0727\\n    },\\n    {\\n      \\\"seed\\\": 1,\\n      \\\"r2\\\": 0.5845,\\n      \\\"r2_increase\\\": 0.0676\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 904
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-26T00:26:47.273198+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "three.tier|tier.*gradient|training.*stage|coarse.*dynamic",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "-A": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "three.tier|tier.*gradient|training.*stage|coarse.*dynamic",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "-A": "3"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-26T00:26:47.725548+00:00_

186:\subsection{Per-Layer Action Decoding Across Training Stages}
187-\label{sec:action_r2_threecond}
188-
189:Figure~\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (randomly initialized, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\pm$ std).
190-All three conditions share L0 representations ($R^2 = 0.645 \pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.
191-The trained model peaks at L9 ($R^2 = 0.643 \pm 0.014$), consistent with progressive specialization for action-relevant feature integration.
192-Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.
--
1175:\paragraph{Observational three-tier gradient.}
1176:The cross-architecture matrix suggests a three-tier gradient of representational adaptation.
1177-Tier~1 (VLM bases, no action training): inherited L1 attention (TracVLA 32/32, NORA 13--14/16), negligible exit collapse ($\Delta R^2 \leq 0.048$), and minimal counterfactual sensitivity (cosine distance $\leq 0.185$).
1178-Tier~2 (general-purpose VLA, OXE-pretrained): strong L1 routing (24--26/32 heads), moderate counterfactual sensitivity ($d \approx 1.0$), and no systematic exit collapse across suites.
1179-Tier~3 (task-specific VLAs, fine-tuned on LIBERO): exit collapse at every VLM-to-VLA cell and medium-to-large counterfactual sensitivity ($d = 0.45$--$1.52$).
1180:This gradient is suggestive but limited: Tier~2 contains a single architecture (OpenVLA), and the Tier~2/Tier~3 boundary confounds training stage with architecture.
1181:Testing additional general-purpose VLAs (e.g., Octo~\cite{ghosh2024_octo}, $\pi_0$~\cite{black2024_pi0}) at Tier~2 is necessary before the three-tier structure can be treated as a robust empirical pattern.
1182-
1183-\paragraph{Exit collapse mechanism.}
1184-One possible explanation for the VLM
…[truncated 1048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-26T00:26:48.077226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1149",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1149",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-26T00:26:48.127964+00:00_

1149	and (v)~$R^2$ projector vs.\ VLA Spearman correlation ($p = 0.003 \to p_{\text{adj}} = 0.183$).
1150	These concern auxiliary comparisons (encoder ranking, coefficient-of-variation ordering) rather than the core redistribution, probing, or counterfactual findings; no main-text conclusion requires revision.
1151	
1152	\subsection{Mechanistic Interpretation}
1153	\label{sec:mechanistic_interpretation}
1154	
1155	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed attention redistribution.
1156	Counterfactual perturbation produces large effects across all conditions ($d = 1.0$--$1.2$ on Goal; \S\ref{sec:openvla_routing}), with shuffled tokens exceeding paraphrased ($d = 1.096$ vs.\ $0.996$) despite identical token sets, indicating positional sensitivity.
1157	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \approx 0$; \S\ref{sec:action_trajectory}) reflects an information-computation dissociation~\cite{hewitt2019control}: instruction-dominant heads control direction rather than precision. Random ablation yields larger $R^2$ gains ($+0.071$ vs.\ $+0.030$; $z = -3.11$, $0$\textsuperscript{th} percentile), consistent with distinct $R^2$ signatures.
1158	
1159	\subsection{Functional Stages and Predictions}
1160	\label{sec:functional_stages}
1161	
1162	Per-layer profiles suggest three stages: redistribution (L0--L1; probe $99.6\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L31, ${\sim}56\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).
1163	Task-specific fine-tuning eliminates L31 re-engagement (18 $\to$ 0 heads; \S\ref{sec:openvla_routing}), consistent with exit-layer attention serving multi-task flexibility ($N{=}2$).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-26T00:27:45.828428+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -5 /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -5 /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_summary.json"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-26T00:27:46.631871+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"head: cannot open '/root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_summary.json' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 803
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-26T00:27:48.340106+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "per.task.*success|success.*per.task|task.level.*SR",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "per.task.*success|success.*per.task|task.level.*SR",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "head_limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-26T00:27:49.103586+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_12.md:52:- **建议**：(a) Ablation → LIBERO rollout 测量 task success rate；(b) 验证 probe R² 与 per-task success rate 的 rank correlation；(c) 或改投对 robotics relevance 无硬性要求的 ML venue（ICML/NeurIPS interpretability track）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260522T021705/logs/review_best.log:80:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260522T021705/logs/review_median.log:91:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260522T021705/logs/review_median.log:164:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260522T021705/logs/phase2_worst_attempt0.log:63:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260522T021705/logs/phase2_median_attempt0.log:48:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260522T021705/logs/phase2_median_attempt0.log:62:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260522T021705/logs/phase2_best_attempt0.log:42:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260522T021705/logs/phase2_best_attempt0.log:51:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260522T021705/logs/phase2_best_attempt0.log:115:[Omitted long matching line]

[Showing results with pagination = limit: 10]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 763
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-26T00:29:00.816507+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: info] 两项审查请求的完整回复\n\n---\n\n## 请求 1：n=9 是否真的无法扩展？\n\n### 逐方案评估\n\n**方案 A：Sub-split（per-demo / per-task）**\n- **技术可行性**：可以——`per_task_r2_distribution.json` 中有 10 个 task 的逐层 R²，可算 per-task ΔR²。\n- **统计有效性**：❌ **不合法**。行为相关性要求每个 data point 同时有 ΔR² 和 SR。Published SR 是 per-suite 聚合值（Kim 2024/Zheng 2024/Hung 2025 均不报告 per-task SR）。没有 per-task SR，无法做 sub-split 相关性。\n- **即使有 per-task SR 也有问题**：同一 cell 内的 task 共享模型权重、训练数据、checkpoint——违反独立性假设。这是 pseudo-replication，会人工膨胀 n 而不增加独立信息量。\n\n**方案 B：Synthetic augmentation（noise injection / frame sampling 变体）**\n- **统计有效性**：❌ **不合法**。对同一 checkpoint 的输入做 augmentation 产生的 ΔR² 估计之间 correlation 接近 1.0（共享所有模型参数）。审稿人会立即识别为 artificial sample inflation。在统计文献中这是已知的 pseudo-replication 陷阱 (Hurlbert 1984)。\n\n**方案 C：Bootstrap resampling**\n- **统计有效性**：❌ **不合法用于增加 n**。Bootstrap 可以估计 ρ 的 sampling distribution / CI（已通过 power analysis 隐含覆盖），但 bootstrap 样本是从原始 n=9 点有放回抽样——不包含新信息。Bootstrap CI 在 n=9 时会极宽（大约 [−0.05, 0.90]），这只是 **重新表述** underpoweredness，不能修复它。\n- **唯一合法用途**：计算 ρ 的 bootstrap CI 放入 appendix。但 power=0.37 已经传达了同样的信息，ROI 极低。\n\n**方案 D：Cross-layer（不同层的 ΔR² 作为不同 observation）**\n- **统计有效性**：❌ **严重违反独立性**。同一 cell 内 32 层的 R² profile 高度自相关（共享模型、共享数据）。且行为结果（SR）在所有层间相同——无法将 32 个 R² 值与 1 个 SR 值做有意义的相关性分析。用混合效应模型也无法绕过\"SR 是 cell 级变量\"这一根本约束。\n\n**方案 E（自行补充考虑）：替代行为指标**\n- 用 counterfactual Cohen's d（我们自己的数据）替代 published SR 做相关性？\n- 这改变了 research question（从 \"ΔR² predicts task success\" 变为 \"ΔR² predicts counterfactual sensitivity\"），且两者测量不同现象（exit collapse vs instruction influence），相关性的科学意义不明确。\n- 现有数据 (`probe_r2_vs_behavioral_rank_correlation.json`) 已尝试 probe R² vs counterfactual d：0/9 correlations significant at p<0.05，fundamental issue 是 n=5。❌\n\n### 终结判断\n\n**n=9 是设计层面的硬约束，不是计算层面的约束。**\n\n瓶颈分解：\n1. **行为结果是 cell 级变量**：Published SR 是每个 (architecture, suite) 一个值，不可分拆\n2. **独立性要求 cell 间变异**：同一 cell 内的任何 sub-split 都共享模型权重 → pseudo-replication\n3. **n 的计算**：3 arch × 4 suites = 12 cells，2 空缺 + 1 excluded = 9 usable\n\n唯一合法扩展路径：\n- 新增 VLA 架构（需有 published LIBERO SR）：如 π₀、Octo、RT-2 — 需要社区发布 checkpoint + 评测结果\n- 新增评估 suite：需要所有架构在新 suite 上都有 published SR\n\n两者都不可能在 3 天内完成，且不是 GPU·h 问题。\n\n**建议存档到 decisions.yaml**：「n=9 behavioral correlation 是设计硬约束。五种扩展方案（sub-split / augmentation / bootstrap / cross-layer / 替代指标）均因违反独立性或缺少 per-task behavioral data 而统计不合法。唯一合法路径是增加架构或评估 suite，需社区数据支持，不在论文控制范围内。已通过 post-hoc power analysis (power=0.37, n≥21 for 80%) 定量披露。」\n\n---\n\n## 请求 2：Paper DDL 3 天内的高 ROI 补充\n\n### 推荐 1：Q9 Coarse Training Dynamics 可视化 — ★★★ (0 GPU·h, ~1.5h)\n\n**现状**：Three-tier gradient 在 Extended Discussion 中只有文字描述（lines 1175-1181）。OpenVLA 三阶段 R² profile 有图（§sec:action_r2_threecond），但没有跨架构的 \"coarse dynamics\" 视图。\n\n**方案**：新增一个 appendix figure，x 轴是 training pathway（NLP finetune / VLM reference / VLA trained / VLA→VLA trained），y 轴是 ΔR²，每个 data point 是一个 cell。具体数据全部已有：\n\n| Training pathway | ΔR² range | n cells |\n|---|---|---|\n| NLP finetune | 0.000 (×3) | 3 |\n| VLM reference | 0.009–0.097 | 6 |\n| VLA trained (from VLM) | 0.156–0.455 | 6 |\n| VLA trained (from VLA) | 0.033–0.086 | 4 |\n\n这个图让审稿人**一眼看到** Q9 的回答：\"we have coarse-grained dynamics — collapse emerges at the VLM→VLA transition and doesn't intensify at VLA→VLA\"。比纯文字论证强得多。\n\n**Q9 提升预估**：7/10 → 8/10。将 \"we acknowledge this is missing\" 转变为 \"we provide cross-condition evidence of when collapse emerges\"。\n\n### 推荐 2：Q3 Methodological Precedent 表格 — ★★☆ (0 GPU·h, ~1h)\n\n**方案**：在 appendix 加 ~10 行 \"Methodological Context\" 小节 + 一个紧凑表格，列出 representational analysis papers that do NOT require behavioral validation：\n\n| Paper | Domain | Analysis | Behavioral eval? |\n|---|---|---|---|\n| Belinkov 2022 | NLP | Probing survey | No |\n| Olsson et al. 2022 | LM | Induction heads | No |\n| Wang et al. 2023 | LM | IOI circuit | No |\n| Meng et al. 2022 | LM | Causal tracing | No |\n| Grant et al. 2026 | VLA | Visual dominance | Partial |\n| Haon et al. 2025 | VLA | Sparse directions | No |\n\n这些引用全部已在 paper 中。表格的价值是让审稿人**立即看到** representational analysis 是一个成熟方法论传统，而不是本文的 ad hoc 辩护。\n\n**Q3 提升预估**：7/10 → 7.5/10。有帮助但 SR=0 仍是根本局限。\n\n### 推荐 3：Q7 不额外处理 — 确认 7/10 为上限\n\nN=2 transitions 是硬约束。Cross-architecture design rationale 表格（appendix §sec:cross_arch_rationale）+ 结构多样性论证已经是最优辩护。任何追加内容（如设计轴计数 \"9/9 axes differ\"）ROI 极低。\n\n---\n\n## 优先级排序\n\n| 项目 | 强化 Q# | 当前→预期 | 工时 | GPU·h |\n|---|---|---|---|---|\n| Coarse dynamics figure | Q9 | 7→8 | ~1.5h | 0 |\n| Precedent table | Q3 | 7→7.5 | ~1h | 0 |\n| Q7 追加 | Q7 | 7→7 | — | — |\n\n建议至少完成 #1（dynamics figure）。#2 视时间余量。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: info] 两项审查请求的完整回复\n\n---\n\n## 请求 1：n=9 是否真的无法扩展？\n\n### 逐方案评估\n\n**方案 A：Sub-split（per-demo / per-task）**\n- **技术可行性**：可以——`per_task_r2_distribution.json` 中有 10 个 task 的逐层 R²，可算 per-task ΔR²。\n- **统计有效性**：❌ **不合法**。行为相关性要求每个 data point 同时有 ΔR² 和 SR。Published SR 是 per-suite 聚合值（Kim 2024/Zheng 2024/Hung 2025 均不报告 per-task SR）。没有 per-task SR，无法做 sub-split 相关性。\n- **即使有 per-task SR 也有问题**：同一 cell 内的 task 共享模型权重、训练数据、checkpoint——违反独立性假设。这是 pseudo-replication，会人工膨胀 n 而不增加独立信息量。\n\n**方案 B：Synthetic augmentation（noise injection / frame sampling 变体）**\n- **统计有效性**：❌ **不合法**。对同一 checkpoint 的输入做 augmentation 产生的 ΔR² 估计之间 correlation 接近 1.0（共享所有模型参数）。审稿人会立即识别为 artificial sample inflation。在统计文献中这是已知的 pseudo-replication 陷阱 (Hurlbert 1984)。\n\n**方案 C：Bootstrap resampling**\n- **统计有效性**：❌ **不合法用于增加 n**。Bootstrap 可以估计 ρ 的 sampling distribution / CI（已通过 power analysis 隐含覆盖），但 bootstrap 样本是从原始 n=9 点有放回抽样——不包含新信息。Bootstrap CI 在 n=9 时会极宽（大约 [−0.05, 0.90]），这只是 **重新表述** underpoweredness，不能修复它。\n- **唯一合法用途**：计算 ρ 的 bootstrap CI 放入 appendix。但 power=0.37 已经传达了同样的信息，ROI 极低。\n\n**方案 D：Cross-layer（不同层的 ΔR² 作为不同 observation）**\n- **统计有效性**：❌ **严重违反独立性**。同一 cell 内 32 层的 R² profile 高度自相关（共享模型、共享数据）。且行为结果（SR）在所有层间相同——无法将 32 个 R² 值与 1 个 SR 值做有意义的相关性分析。用混合效应模型也无法绕过\"SR 是 cell 级变量\"这一根本约束。\n\n**方案 E（自行补充考虑）：替代行为指标**\n- 用 counterfactual Cohen's d（我们自己的数据）替代 published SR 做相关性？\n- 这改变了 research question（从 \"ΔR² predicts task success\" 变为 \"ΔR² predicts counterfactual sensitivity\"），且两者测量不同现象（exit collapse vs instruction influence），相关性的科学意义不明确。\n- 现有数据 (`probe_r2_vs_behavioral_rank_correlation.json`) 已尝试 probe R² vs counterfactual d：0/9 correlations significant at p<0.05，fundamental issue 是 n=5。❌\n\n### 终结判断\n\n**n=9 是设计层面的硬约束，不是计算层面的约束。**\n\n瓶颈分解：\n1. **行为结果是 cell 级变量**：Published SR 是每个 (architecture, suite) 一个值，不可分拆\n2. **独立性要求 cell 间变异**：同一 cell 内的任何 sub-split 都共享模型权重 → pseudo-replication\n3. **n 的计算**：3 arch × 4 suites = 12 cells，2 空缺 + 1 excluded = 9 usable\n\n唯一合法扩展路径：\n- 新增 VLA 架构（需有 published LIBERO SR）：如 π₀、Octo、RT-2 — 需要社区发布 checkpoint + 评测结果\n- 新增评估 suite：需要所有架构在新 suite 上都有 published SR\n\n两者都不可能在 3 天内完成，且不是 GPU·h 问题。\n\n**建议存档到 decisions.yaml**：「n=9 behavioral correlation 是设计硬约束。五种扩展方案（sub-split / augmentation / bootstrap / cross-layer / 替代指标）均因违反独立性或缺少 per-task behavioral data 而统计不合法。唯一合法路径是增加架构或评估 suite，需社区数据支持，不在论文控制范围内。已通过 post-hoc power analysis (power=0.37, n≥21 for 80%) 定量披露。」\n\n---\n\n## 请求 2：Paper DDL 3 天内的高 ROI 补充\n\n### 推荐 1：Q9 Coarse Training Dynamics 可视化 — ★★★ (0 GPU·h, ~1.5h)\n\n**现状**：Three-tier gradient 在 Extended Discussion 中只有文字描述（lines 1175-1181）。OpenVLA 三阶段 R² profile 有图（§sec:action_r2_threecond），但没有跨架构的 \"coarse dynamics\" 视图。\n\n**方案**：新增一个 appendix figure，x 轴是 training pathway（NLP finetune / VLM reference / VLA trained / VLA→VLA trained），y 轴是 ΔR²，每个 data point 是一个 cell。具体数据全部已有：\n\n| Training pathway | ΔR² range | n cells |\n|---|---|---|\n| NLP finetune | 0.000 (×3) | 3 |\n| VLM reference | 0.009–0.097 | 6 |\n| VLA trained (from VLM) | 0.156–0.455 | 6 |\n| VLA trained (from VLA) | 0.033–0.086 | 4 |\n\n这个图让审稿人**一眼看到** Q9 的回答：\"we have coarse-grained dynamics — collapse emerges at the VLM→VLA transition and doesn't intensify at VLA→VLA\"。比纯文字论证强得多。\n\n**Q9 提升预估**：7/10 → 8/10。将 \"we acknowledge this is missing\" 转变为 \"we provide cross-condition evidence of when collapse emerges\"。\n\n### 推荐 2：Q3 Methodological Precedent 表格 — ★★☆ (0 GPU·h, ~1h)\n\n**方案**：在 appendix 加 ~10 行 \"Methodological Context\" 小节 + 一个紧凑表格，列出 representational analysis papers that do NOT require behavioral validation：\n\n| Paper | Domain | Analysis | Behavioral eval? |\n|---|---|---|---|\n| Belinkov 2022 | NLP | Probing survey | No |\n| Olsson et al. 2022 | LM | Induction heads | No |\n| Wang et al. 2023 | LM | IOI circuit | No |\n| Meng et al. 2022 | LM | Causal tracing | No |\n| Grant et al. 2026 | VLA | Visual dominance | Partial |\n| Haon et al. 2025 | VLA | Sparse directions | No |\n\n这些引用全部已在 paper 中。表格的价值是让审稿人**立即看到** representational analysis 是一个成熟方法论传统，而不是本文的 ad hoc 辩护。\n\n**Q3 提升预估**：7/10 → 7.5/10。有帮助但 SR=0 仍是根本局限。\n\n### 推荐 3：Q7 不额外处理 — 确认 7/10 为上限\n\nN=2 transitions 是硬约束。Cross-architecture design rationale 表格（appendix §sec:cross_arch_rationale）+ 结构多样性论证已经是最优辩护。任何追加内容（如设计轴计数 \"9/9 axes differ\"）ROI 极低。\n\n---\n\n## 优先级排序\n\n| 项目 | 强化 Q# | 当前→预期 | 工时 | GPU·h |\n|---|---|---|---|---|\n| Coarse dynamics figure | Q9 | 7→8 | ~1.5h | 0 |\n| Precedent table | Q3 | 7→7.5 | ~1h | 0 |\n| Q7 追加 | Q7 | 7→7 | — | — |\n\n建议至少完成 #1（dynamics figure）。#2 视时间余量。",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-26T00:29:04.831865+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 4015
}
```

</details>

---

### Assistant

_source line 166 · 2026-05-26T00:29:07.023183+00:00_

分析完成。发送综合报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---

## Round 5

16 recorded events

### User

_source line 167 · 2026-05-26T01:03:46.553911+00:00_

[System 触发审查]:
任务 F+G 产出质量审查：

**F — Training Dynamics Figure (fig_training_dynamics.pdf)**
- 验证 19 个 data points 的 ΔR² 值是否与 Table 1 一致
- 验证 4 类 training pathway 分组是否正确（NLP finetune ×3 = 0.000; VLM reference ×6; VLM→VLA ×6; VLA→VLA ×4）
- caption 是否准确传达 "collapse emerges at VLM→VLA, doesn't intensify at VLA→VLA"
- 图风格是否清晰、适合学术论文

**G — Methodological Precedent Table**
- 7 篇引用是否准确（年份、方法描述、behavioral eval 列）
- 特别确认：Belinkov 2022 是 survey、Olsson 2022 是 induction heads、Wang 2023 是 IOI circuit、Meng 2022 是 causal tracing、Grant 2026 是 visual dominance、Haon 2025 是 sparse directions
- 表格定位（"representational analysis 是成熟方法论传统"）是否 overstate？

快速审查即可，不需要重做完整数字一致性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system"
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-26T01:03:56.643295+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fig_training_dynamics|training.dynamics|coarse.*dynamics",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "-A": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fig_training_dynamics|training.dynamics|coarse.*dynamics",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "-A": "2"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-26T01:03:57.647021+00:00_

1212:\paragraph{Coarse training dynamics.}
1213-Although intermediate checkpoints are unavailable (\S\ref{sec:discussion}), the cross-condition design provides coarse-grained evidence about when exit collapse emerges.
1214:Figure~\ref{fig:training_dynamics} plots $\Delta R^2$ across four training-pathway categories.
1215-NLP fine-tuning ($\Delta R^2 = 0.000$) and VLM references ($\Delta R^2 \leq 0.097$) cluster below the $0.10$ threshold; VLM-to-VLA fine-tuning produces large collapse ($\Delta R^2 = 0.156$--$0.455$); subsequent VLA-to-VLA fine-tuning does not intensify it ($\Delta R^2 = 0.033$--$0.086$).
1216-This constrains the onset: exit collapse emerges during the first action-grounded training stage and does not accumulate with continued task-specific fine-tuning.
--
1220:\includegraphics[width=0.55\columnwidth]{figures/fig_training_dynamics.pdf}
1221-\caption{\textbf{$\Delta R^2$ across training pathways.} Each point is one architecture-suite cell; markers distinguish backbone families. Exit collapse (above dashed line) is confined to VLM-to-VLA transitions and does not intensify during VLA-to-VLA fine-tuning.}
1222:\label{fig:training_dynamics}
1223-\end{figure}
1224-
--
1291:\caption{\textbf{Claim--evidence--scope summary.} Each main finding is paired with its supporting analysis and its main limitation. The figure distinguishes directly observed representational patterns from stronger causal interpretations that require interventional or training-dynamics evidence.}
1292-\label{fig:claim_evidence}
1293-\end{figure}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 1003
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-26T01:03:58.450095+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "methodological.*context|methodological.*precedent|precedent.*table|representational.*tradition",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "-A": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "methodological.*context|methodological.*precedent|precedent.*table|representational.*tradition",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "-A": "2"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-26T01:03:58.500646+00:00_

1225:\subsection{Methodological Context}
1226:\label{sec:methodological_context}
1227-
1228:Representational analysis is an established methodology in the interpretability tradition; behavioral validation provides complementary evidence but is not a prerequisite for mechanistic characterization.
1229:Table~\ref{tab:methodological_precedent} situates our approach within this tradition.
1230-
1231-\begin{table}[h]
--
1233:\caption{\textbf{Methodological precedent.} Representative interpretability studies and their use of behavioral evaluation. Partial behavioral eval includes correlational or indirect evidence.}
1234:\label{tab:methodological_precedent}
1235-\small
1236-\begin{tabular}{@{}llll@{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-26T01:04:01.567162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1210",
  "limit": "55"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1210",
    "limit": "55"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-26T01:04:01.618078+00:00_

1210	The three-tier gradient has $n = 1$ at Tier~2, limiting its inferential power; populating this tier with additional general-purpose VLAs is a priority for future work.
1211	
1212	\paragraph{Coarse training dynamics.}
1213	Although intermediate checkpoints are unavailable (\S\ref{sec:discussion}), the cross-condition design provides coarse-grained evidence about when exit collapse emerges.
1214	Figure~\ref{fig:training_dynamics} plots $\Delta R^2$ across four training-pathway categories.
1215	NLP fine-tuning ($\Delta R^2 = 0.000$) and VLM references ($\Delta R^2 \leq 0.097$) cluster below the $0.10$ threshold; VLM-to-VLA fine-tuning produces large collapse ($\Delta R^2 = 0.156$--$0.455$); subsequent VLA-to-VLA fine-tuning does not intensify it ($\Delta R^2 = 0.033$--$0.086$).
1216	This constrains the onset: exit collapse emerges during the first action-grounded training stage and does not accumulate with continued task-specific fine-tuning.
1217	
1218	\begin{figure}[h]
1219	\centering
1220	\includegraphics[width=0.55\columnwidth]{figures/fig_training_dynamics.pdf}
1221	\caption{\textbf{$\Delta R^2$ across training pathways.} Each point is one architecture-suite cell; markers distinguish backbone families. Exit collapse (above dashed line) is confined to VLM-to-VLA transitions and does not intensify during VLA-to-VLA fine-tuning.}
1222	\label{fig:training_dynamics}
1223	\end{figure}
1224	
1225	\subsection{Methodological Context}
1226	\label{sec:methodological_context}
1227	
1228	Representational analysis is an established methodology in the interpretability tradition; behavioral validation provides complementary evidence but is not a prerequisite for mechanistic characterization.
1229	Table~\ref{tab:methodological_precedent} situates our approach within this tradition.
1230	
1231	\begin{table}[h]
1232	\centering
1233	\caption{\textbf{Methodological precedent.} Representative interpretability studies and their use of behavioral evaluation. Partial behavioral eval 
…[truncated 1589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-26T01:05:09.202672+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_training_dynamics.pdf",
  "description": "Check training dynamics figure exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_training_dynamics.pdf",
    "description": "Check training dynamics figure exists"
  }
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-26T01:05:09.306120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "offset": "68",
  "limit": "23"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "offset": "68",
    "limit": "23"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-26T01:05:09.358457+00:00_

68	\begin{tabular}{@{}lll cccc@{}}
69	\toprule
70	& & & \multicolumn{4}{c}{$\Delta R^2$ (peak $-$ exit)} \\
71	\cmidrule(l){4-7}
72	Architecture & Suite & Transition & Trained & 95\% CI & Reference & 95\% CI \\
73	\midrule
74	OpenVLA & Goal    & VLA$\to$VLA & 0.086 & [$-$0.060, 0.110] & 0.056 & [0.010, 0.080] \\
75	OpenVLA & Spatial & VLA$\to$VLA & 0.037 & [0.010, 0.100]    & 0.044 & [0.030, 0.110] \\
76	OpenVLA & Object  & VLA$\to$VLA & 0.037 & [0.000, 0.090]    & 0.051 & [0.000, 0.090] \\
77	OpenVLA & Long    & VLA$\to$VLA & 0.033 & [0.000, 0.100]    & 0.035 & [0.030, 0.100] \\
78	\midrule
79	TracVLA & Goal    & VLM$\to$VLA & 0.333 & [0.210, 0.450]    & 0.065 & [$-$0.110, 0.050] \\
80	TracVLA & Spatial & VLM$\to$VLA & 0.156 & [0.090, 0.220]    & 0.048 & ---$^{a}$ \\
81	TracVLA & Object  & VLM$\to$VLA & 0.362 & [0.280, 0.500]    & 0.009 & [$-$0.070, 0.020] \\
82	TracVLA & Long    & VLM$\to$VLA & 0.358 & [0.170, 0.530]    & 0.097 & [$-$0.020, 0.110] \\
83	\midrule
84	NORA    & Goal    & VLM$\to$VLA & 0.455$^{b}$ & ---$^{b}$  & 0.081 & [$-$0.010, 0.110] \\
85	NORA    & Spatial & VLM$\to$VLA & 0.308 & [0.300, 0.510]    & 0.089 & [$-$0.010, 0.090] \\
86	\bottomrule
87	\multicolumn{7}{l}{\footnotesize NORA Object and Long-Horizon checkpoints are unavailable.}\\
88	\multicolumn{7}{l}{\footnotesize $^{a}$CI artifact from flat $R^2$ profile. $^{b}$Bootstrap CI unreliable (exit-layer $R^2 \approx -0.006$).}\\
89	\end{tabular}
90	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-26T01:05:09.459120+00:00_

-rw-r--r-- 1 ubuntu ubuntu 19885 May 26 00:30 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_training_dynamics.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 256
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-26T01:05:27.427057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_training_dynamics.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_training_dynamics.pdf"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-26T01:05:27.527995+00:00_

PDF file read: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_training_dynamics.pdf (19.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-26T01:07:07.976586+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: warning] 任务 F+G 产出审查报告\n\n---\n\n## F — Training Dynamics Figure\n\n### ✅ 数值准确性\n\n与 Table 1 (experiments.tex:74-85) 逐点核对：\n\n| 类别 | 预期 data points | ΔR² 范围 | 与 Table 1 一致？ |\n|---|---|---|---|\n| NLP finetune | 3 (Llama-2-chat, Phi-3-instruct, Qwen2.5-Instruct) | 0.000 ×3 | ✅ |\n| VLM reference | TracVLA ref ×4 + NORA ref ×2 = 6 | 0.009–0.097 | ✅ |\n| VLM→VLA trained | TracVLA trained ×4 + NORA trained ×2 = 6 | 0.156–0.455 | ✅ |\n| VLA→VLA trained | OpenVLA trained ×4 | 0.033–0.086 | ✅ |\n\n文本 (lines 1215) 中的 ΔR² 范围全部与 Table 1 吻合。\n\n### [warning] \"VLM reference\" 列包含 OpenVLA reference（VLA, 非 VLM）\n\n图中 \"VLM reference\" 列可见 ~4 个蓝色圆点（约 0.035-0.056），这对应 **OpenVLA reference**（OXE-pretrained VLA）。但 OpenVLA reference **不是 VLM**——它是通用 VLA checkpoint。将其归入 \"VLM reference\" 类别在术语上不准确。\n\n实际 data point 数应为 **23**（非 19）：3 + 10(含 OpenVLA ref 4) + 4 + 6。\n\n**两种修复方案**（选一）：\n- **方案 A（推荐）**：将 x 轴标签 \"VLM reference\" 改为 \"Reference (pretrained)\"——涵盖所有 reference checkpoint，不区分 VLM/VLA 来源。文本 line 1215 相应改为 \"pretrained references\"。\n- **方案 B**：从图中移除 OpenVLA reference 4 个点，保持 19 个点与\"VLM reference\"标签一致。\n\n方案 A 更好——多 4 个点视觉上加强了 \"reference 全在阈值下\" 的信息。审稿人读到 \"VLM reference\" 却看到 OpenVLA（蓝色圆点 ≠ VLM）可能追问。\n\n### ✅ Caption 准确\n\n\"Exit collapse (above dashed line) is confined to VLM-to-VLA transitions and does not intensify during VLA-to-VLA fine-tuning\" — 准确传达核心信息。dashed line 在 0.10 处清晰可见。\n\n### ✅ 视觉质量\n\n- 三种 marker 形状+颜色区分三个架构家族，图例清晰\n- 0.10 阈值虚线直观分隔 collapse / non-collapse 区域\n- 四类 x 轴排列逻辑上从\"无 action 训练\"到\"VLA 训练\"递进\n- 字体大小合适，适合学术论文 column width\n\n---\n\n## G — Methodological Precedent Table\n\n### 引用逐条验证\n\n| 论文 | 年份 | 方法描述 | Behav eval | 准确？ |\n|---|---|---|---|---|\n| Belinkov 2022 | ✅ | \"Probing survey\" ✅ | No ✅ | ✅ |\n| Olsson et al. 2022 | ✅ | \"Induction heads\" ✅ | No ✅ | ✅ |\n| Wang et al. 2023 | ✅ | \"IOI circuit\" ✅ | No ✅ | ✅ |\n| Meng et al. 2022 | ✅ | \"Causal tracing\" ✅ | No — 见下 | ⚠️ |\n| Grant et al. 2026 | ✅ | \"Visual dominance\" ✅ | Partial ✅ | ✅ |\n| Haon et al. 2025 | ✅ | \"Sparse directions\" ✅ | No ✅ | ✅ |\n| Ours | — | \"ΔR² + attn. profiling\" ✅ | Partial (ρ=0.583) ✅ | ✅ |\n\n### [info] Meng et al. 2022 (ROME) 的 \"Behavioral eval = No\" 可商榷\n\nROME 包含两部分：(1) causal tracing（定位知识存储位置）和 (2) knowledge editing + 成功率评估。后者 IS behavioral evaluation（修改事实后测试模型输出是否变化）。表格引用 ROME 的 \"causal tracing\" 部分，标 \"No\" 可辩护；但一个熟悉 ROME 的审稿人可能指出 ROME 实际包含 behavioral 验证。\n\n**建议**：将 Meng 2022 的 Behav eval 改为 \"Partial\" 或在 Method 列写 \"Causal tracing (localization)\"，更精确限定引用范围。风险极低但能避免可能的审稿人追问。\n\n### ✅ 表格定位准确——未 overstate\n\n关键措辞 (line 1228)：\"behavioral validation provides complementary evidence but is not a prerequisite for mechanistic characterization\"\n\n- \"complementary\"：正确——不否认 behavioral validation 的价值\n- \"not a prerequisite for mechanistic characterization\"：正确范围限定——仅声称 representational analysis 可以独立产生 mechanistic insight，不声称可以替代 behavioral validation\n- 这是 interpretability 社区的标准立场（Belinkov 2022 整篇 survey 就建立在这个前提上）\n- **没有 overstate**。\n\n---\n\n## 总结\n\n| 项目 | 结论 |\n|---|---|\n| F: ΔR² 数值 | ✅ PASS（全部与 Table 1 一致） |\n| F: 分类正确性 | ⚠️ WARNING（\"VLM reference\" 标签包含 OpenVLA ref，应改为 \"Reference (pretrained)\" 或类似） |\n| F: Caption | ✅ PASS |\n| F: 视觉质量 | ✅ PASS |\n| G: 引用准确性 | ✅ PASS（Meng 2022 建议微调为 \"Partial\"，info 级） |\n| G: 定位 | ✅ PASS（未 overstate） |\n\n唯一 warning 级：fig_training_dynamics 的 \"VLM reference\" x 轴标签需修正以避免将 OpenVLA reference（VLA）错误归类为 VLM。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: warning] 任务 F+G 产出审查报告\n\n---\n\n## F — Training Dynamics Figure\n\n### ✅ 数值准确性\n\n与 Table 1 (experiments.tex:74-85) 逐点核对：\n\n| 类别 | 预期 data points | ΔR² 范围 | 与 Table 1 一致？ |\n|---|---|---|---|\n| NLP finetune | 3 (Llama-2-chat, Phi-3-instruct, Qwen2.5-Instruct) | 0.000 ×3 | ✅ |\n| VLM reference | TracVLA ref ×4 + NORA ref ×2 = 6 | 0.009–0.097 | ✅ |\n| VLM→VLA trained | TracVLA trained ×4 + NORA trained ×2 = 6 | 0.156–0.455 | ✅ |\n| VLA→VLA trained | OpenVLA trained ×4 | 0.033–0.086 | ✅ |\n\n文本 (lines 1215) 中的 ΔR² 范围全部与 Table 1 吻合。\n\n### [warning] \"VLM reference\" 列包含 OpenVLA reference（VLA, 非 VLM）\n\n图中 \"VLM reference\" 列可见 ~4 个蓝色圆点（约 0.035-0.056），这对应 **OpenVLA reference**（OXE-pretrained VLA）。但 OpenVLA reference **不是 VLM**——它是通用 VLA checkpoint。将其归入 \"VLM reference\" 类别在术语上不准确。\n\n实际 data point 数应为 **23**（非 19）：3 + 10(含 OpenVLA ref 4) + 4 + 6。\n\n**两种修复方案**（选一）：\n- **方案 A（推荐）**：将 x 轴标签 \"VLM reference\" 改为 \"Reference (pretrained)\"——涵盖所有 reference checkpoint，不区分 VLM/VLA 来源。文本 line 1215 相应改为 \"pretrained references\"。\n- **方案 B**：从图中移除 OpenVLA reference 4 个点，保持 19 个点与\"VLM reference\"标签一致。\n\n方案 A 更好——多 4 个点视觉上加强了 \"reference 全在阈值下\" 的信息。审稿人读到 \"VLM reference\" 却看到 OpenVLA（蓝色圆点 ≠ VLM）可能追问。\n\n### ✅ Caption 准确\n\n\"Exit collapse (above dashed line) is confined to VLM-to-VLA transitions and does not intensify during VLA-to-VLA fine-tuning\" — 准确传达核心信息。dashed line 在 0.10 处清晰可见。\n\n### ✅ 视觉质量\n\n- 三种 marker 形状+颜色区分三个架构家族，图例清晰\n- 0.10 阈值虚线直观分隔 collapse / non-collapse 区域\n- 四类 x 轴排列逻辑上从\"无 action 训练\"到\"VLA 训练\"递进\n- 字体大小合适，适合学术论文 column width\n\n---\n\n## G — Methodological Precedent Table\n\n### 引用逐条验证\n\n| 论文 | 年份 | 方法描述 | Behav eval | 准确？ |\n|---|---|---|---|---|\n| Belinkov 2022 | ✅ | \"Probing survey\" ✅ | No ✅ | ✅ |\n| Olsson et al. 2022 | ✅ | \"Induction heads\" ✅ | No ✅ | ✅ |\n| Wang et al. 2023 | ✅ | \"IOI circuit\" ✅ | No ✅ | ✅ |\n| Meng et al. 2022 | ✅ | \"Causal tracing\" ✅ | No — 见下 | ⚠️ |\n| Grant et al. 2026 | ✅ | \"Visual dominance\" ✅ | Partial ✅ | ✅ |\n| Haon et al. 2025 | ✅ | \"Sparse directions\" ✅ | No ✅ | ✅ |\n| Ours | — | \"ΔR² + attn. profiling\" ✅ | Partial (ρ=0.583) ✅ | ✅ |\n\n### [info] Meng et al. 2022 (ROME) 的 \"Behavioral eval = No\" 可商榷\n\nROME 包含两部分：(1) causal tracing（定位知识存储位置）和 (2) knowledge editing + 成功率评估。后者 IS behavioral evaluation（修改事实后测试模型输出是否变化）。表格引用 ROME 的 \"causal tracing\" 部分，标 \"No\" 可辩护；但一个熟悉 ROME 的审稿人可能指出 ROME 实际包含 behavioral 验证。\n\n**建议**：将 Meng 2022 的 Behav eval 改为 \"Partial\" 或在 Method 列写 \"Causal tracing (localization)\"，更精确限定引用范围。风险极低但能避免可能的审稿人追问。\n\n### ✅ 表格定位准确——未 overstate\n\n关键措辞 (line 1228)：\"behavioral validation provides complementary evidence but is not a prerequisite for mechanistic characterization\"\n\n- \"complementary\"：正确——不否认 behavioral validation 的价值\n- \"not a prerequisite for mechanistic characterization\"：正确范围限定——仅声称 representational analysis 可以独立产生 mechanistic insight，不声称可以替代 behavioral validation\n- 这是 interpretability 社区的标准立场（Belinkov 2022 整篇 survey 就建立在这个前提上）\n- **没有 overstate**。\n\n---\n\n## 总结\n\n| 项目 | 结论 |\n|---|---|\n| F: ΔR² 数值 | ✅ PASS（全部与 Table 1 一致） |\n| F: 分类正确性 | ⚠️ WARNING（\"VLM reference\" 标签包含 OpenVLA ref，应改为 \"Reference (pretrained)\" 或类似） |\n| F: Caption | ✅ PASS |\n| F: 视觉质量 | ✅ PASS |\n| G: 引用准确性 | ✅ PASS（Meng 2022 建议微调为 \"Partial\"，info 级） |\n| G: 定位 | ✅ PASS（未 overstate） |\n\n唯一 warning 级：fig_training_dynamics 的 \"VLM reference\" x 轴标签需修正以避免将 OpenVLA reference（VLA）错误归类为 VLM。",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-26T01:07:12.747247+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 4770
}
```

</details>

---

### Assistant

_source line 182 · 2026-05-26T01:07:15.450161+00:00_

图表视觉清晰，配色区分三个架构家族直观。现在验证数据点对照和分类准确性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---

## Round 6

90 recorded events

### User

_source line 183 · 2026-05-26T08:44:20.989937+00:00_

[System 触发审查]:
Camera-ready 最终 QA（CoRL 2026 格式对照）：

1. **CoRL 格式合规**：确认论文使用正确模板、margin、字号、行距
2. **匿名性**：CoRL 是否双盲？如果是，检查全文是否有 de-anonymization 泄露（作者名、机构名、GitHub 链接、acknowledgments 等）
3. **References 格式**：bib entry 是否统一（会议名全称/缩写一致、页码格式一致）
4. **Figure/Table 规范**：caption 位置（fig 下方、table 上方）、编号连续、无孤立引用
5. **Appendix 合规**：CoRL 是否允许 appendix 附在 main PDF 后？还是需要单独 supplementary？

快速检查，发现问题即报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system"
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-26T08:44:30.403137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-26T08:44:31.407478+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	\usepackage{wrapfig}
16	
17	\title{Instruction Routing in Fine-Tuned Vision-Language-Action Models:\\ A Cross-Architecture Analysis}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	
23	\maketitle
24	
25	\begin{abstract}
26	\input{abstract}
27	\end{abstract}
28	
29	\keywords{Vision-Language-Action models, representational analysis, attention routing, fine-tuning}
30	
31	\input{introduction}
32	\input{related_work}
33	\input{method}
34	\input{experiments}
35	\input{discussion}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-26T08:44:32.363334+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "documentclass|usepackage.*corl|corl|anonymous|review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "documentclass|usepackage.*corl|corl|anonymous|review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-26T08:44:33.770359+00:00_

1:\documentclass{article}
3:\usepackage{corl_2026}
19:\author{Anonymous}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 1407
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-26T08:44:34.623855+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "github|gitlab|anonymous|acknowledgment|acknowledg|funding|grant.*number|institution|university|affiliation|author\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "github|gitlab|anonymous|acknowledgment|acknowledg|funding|grant.*number|institution|university|affiliation|author\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-26T08:44:34.724864+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex:19:\author{Anonymous}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:22:\author{
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:25:  University of California Berkeley 
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:31:  %% Affiliation \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:36:  %% Affiliation \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:41:  %% Affiliation \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:46:  %% Affiliation \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:137:% The acknowledgments are automatically included only in the final and preprint versions of the paper.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:138:\acknowledgments{If a paper is accepted, the final camera-ready version will (and probably should) include acknowledgments. All acknowledgments go at the end of the paper, including thanks to reviewers who gave useful comments, to colleagues who contributed to the ideas, and to funding agencies and corporate sponsors that provided financial support.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:1331:Table~\ref{tab:convergent_evidence} summarizes what each method measures, its key finding, evidence type, and acknowledged limitation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-26T08:44:46.919056+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "our previous|our prior|we previously|our earlier|in \\[anonymous\\]|our work in|we have shown|our code|github\\.com|code.*release|will be released|upon acceptance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "our previous|our prior|we previously|our earlier|in \\[anonymous\\]|our work in|we have shown|our code|github\\.com|code.*release|will be released|upon acceptance",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-26T08:44:48.425055+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex:17:Code and data will be released upon acceptance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 1505
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-26T08:44:48.928833+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty 2>/dev/null && head -40 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
  "description": "Check CoRL style file header for options"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty 2>/dev/null && head -40 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
    "description": "Check CoRL style file header for options"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-26T08:44:49.882663+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty
% File: corl_2026.sty 
%
% Latex templates for the Conference on Robot Learning (CoRL)
%
% This template is heavily inspired by the NeurIPS, ICML, ICLR and IEEE Transactions latex templates.
% Hence we would like to thank: Roman Garnett and the previous mantainers of the NIPS style, Percy Liang and the previous mantainers of the ICML style, Hugo Larochelle for the ICLR style, and Michael Shell for the IEEE Transactions style.
%
% History:
% 2017/04/16 - First revision by Roberto Calandra (roberto.calandra@berkeley.edu).
%	       Main changes:
%	       - The abstract is more compact compared to NeurIPS/ICML
%	       - References are by default using natbib with squared numbers (e.g., [1])
%	       - DOI fields from the bibtex are automatically converted to hyperlinks 
%	       to the corresponding page
%	       - acknowledgments are now a command, and the corresponding subsubsection is
%	       automatically included only in the final version
% 2017/06/12 - Modified to use corlabbrvnat.bst, which order the reference by order of appearance in the paper
% 2017/06/13 - fixed typo
% 2018/05/09 - Slightly modified for CoRL 2018 by Jun Morimoto (xmorimo@atr.jp)
% 2019/01/28 - Slightly modified for CoRL 2019 by Jun Nakanishi (jnakanis@meijo-u.ac.jp)
% 2020/02/02 - Slightly modified for CoRL 2020 by Cynthia Matuszek (cmat@umbc.edu)
% 2020/08/19 - Added preprint option by Roberto Calandra (rcalandra@fb.com)
% 2021/05/06 - Slightly modified for CoRL 2021 by Gerhard Neumann (gerhard.neumann@kit.edu)
% 2022/03/09 - Slightly modified for CoRL 2022 by Minas Liarokapis (minas.liarokapis@auckland.ac.nz)
% 2022/03/06 - Slightly modified for CoRL 2023 by Marc Toussaint (toussaint@tu-berlin.de)
% 2024/03/26 - Slightly modified for CoRL 2024 by David Held (dheld@andrew.cmu.edu)
% 2026/01/10 - Slightly modified for CoRL 2026 by Yoonchang Sung (yoonchang.sung@ntu.edu.sg)
%
% TODO: nohyperref is not 
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-26T08:44:50.435348+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\appendix|\\\\section.*Supplementary|\\\\section.*Appendix|newpage.*appendix",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\appendix|\\\\section.*Supplementary|\\\\section.*Appendix|newpage.*appendix",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-26T08:44:50.435837+00:00_

&lt;tool_use_error>InputValidationError: Grep failed due to the following issue:
An unexpected parameter `limit` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-26T08:44:59.822110+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\appendix|\\\\section.*Supplementary|\\\\section.*Appendix|newpage",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\appendix|\\\\section.*Supplementary|\\\\section.*Appendix|newpage",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-26T08:45:00.324614+00:00_

4:\appendix
6:\section{Supplementary Material}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-26T08:45:01.028266+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "final|preprint|review|submission",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "final|preprint|review|submission",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-26T08:45:01.129343+00:00_

16:%	       automatically included only in the final version
22:% 2020/08/19 - Added preprint option by Roberto Calandra (rcalandra@fb.com)
35:\ProvidesPackage{corl_2026}[2026/08/15 CORL2026 submission/preprint/camera-ready style file]
42:% Accepted options: [final,preprint,nonatbib,nohyperref]
44:% Declare the final option, which creates camera-ready copy
45:\newif\if@conferencefinal\@conferencefinalfalse
46:\DeclareOption{final}{
47:  \@conferencefinaltrue
50:% Declare the preprint option, which creates a camera-ready copy without the corl footnote
51:\newif\if@preprinttype\@preprinttypefalse
52:\DeclareOption{preprint}{
53:  \@preprinttypetrue
129:% Create acknowledgments -- only if the option 'final' is activated
132:\if@conferencefinal% 
135:\if@preprinttype% 
141:% handle tweaks for camera-ready copy vs. submission copy
142:\if@conferencefinal
148:  \if@preprinttype
157:    % line numbers for submission
407:    \if@conferencefinal

[Showing results with pagination = limit: 20]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-26T08:45:14.316683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
  "offset": "140",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
    "offset": "140",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-26T08:45:15.270616+00:00_

140	
141	% handle tweaks for camera-ready copy vs. submission copy
142	\if@conferencefinal
143	  \newcommand{\@noticestring}{%
144	    \@conferenceordinal\/ Conference on Robot Learning
145	    (CoRL \@conferenceyear), \@conferencelocation.%
146	  }
147	\else
148	  \if@preprinttype
149	    \newcommand{\@noticestring}{%
150	      % Nothing here.
151	    }
152	  \else
153	    \newcommand{\@noticestring}{%
154	      Submitted to the \@conferenceordinal\/ Conference on Robot Learning (CoRL \@conferenceyear). Do not distribute.%
155	    }
156	
157	    % line numbers for submission
158	    \linenumbers
159	
160	    % fix incompatibilities between lineno and amsmath, if required, by
161	    % transparently wrapping linenomath environments around amsmath
162	    % environments
163	    \AtBeginDocument{%
164	     \@ifpackageloaded{amsmath}{%
165	        \newcommand*\patchAmsMathEnvironmentForLineno[1]{%
166	          \expandafter\let\csname old#1\expandafter\endcsname\csname #1\endcsname
167	          \expandafter\let\csname oldend#1\expandafter\endcsname\csname end#1\endcsname
168	          \renewenvironment{#1}%
169	            {\linenomath\csname old#1\endcsname}%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-26T08:45:16.075117+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c '\\\\begin{figure\\|\\\\begin{wrapfig\\|\\\\begin{table' /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "description": "Count figures and tables in main text files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c '\\\\begin{figure\\|\\\\begin{wrapfig\\|\\\\begin{table' /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "description": "Count figures and tables in main text files"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-26T08:45:16.125768+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:6
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex:0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-26T08:45:16.627982+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\caption\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\caption\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-26T08:45:16.780064+00:00_

20:\caption{\textbf{Cross-architecture evaluation matrix.} Each cell reports $\Delta R^2$ (peak$-$exit). OpenVLA: VLA-to-VLA; TracVLA and NORA: VLM-to-VLA. Gray cells: checkpoints not released by original authors. Red borders indicate $\Delta R^2 > 0.10$.}
51:\caption{\textbf{Layer-wise action-probe $R^2$ (LIBERO-Goal, readout token).} Solid: trained; dashed: reference. VLM-to-VLA transitions show pronounced peak-to-exit drops ($\Delta R^2 = 0.16$--$0.46$); VLA-to-VLA remains flat ($< 0.09$). Quantitative $\Delta R^2$ values use demo-level splitting (\S\ref{sec:cross_arch_analyses}); see Table~\ref{tab:cross_arch_matrix} for all cells.}
64:\caption{\textbf{Peak-to-exit action-probe drop across the architecture-suite matrix.} $\Delta R^2$ is computed as the difference between the maximum layer-wise action-probe $R^2$ and the exit-layer $R^2$. Values above 0.10 are treated as substantial descriptive drops. OpenVLA is a VLA-to-VLA comparison, whereas TracVLA and NORA are VLM-to-VLA comparisons.}
107:\caption{Counterfactual sensitivity across the architecture-suite matrix. (a)~Cohen's $d$ for four perturbation conditions (E=empty, W=wrong, S=shuffled, P=paraphrased); asterisks mark the top condition per cell; dashed line: large-effect threshold ($d = 0.8$). (b)~Cosine distance on hidden representations (different scale).}
121:\caption{\textbf{Counterfactual sensitivity summary.} Cohen's $d$ range and most sensitive perturbation for action-producing models (OpenVLA, TracVLA). NORA uses cosine distance on hidden representations (different scale; see \S\ref{sec:cf_repr}).}
165:\caption{L1 instruction-dominant head counts (trained vs.\ reference; heads with $>50\%$ attention on instruction tokens). Reference VLMs already saturate or near-saturate; training does not increase counts. Medians across available LIBERO suites per architecture.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-26T08:45:29.478119+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\begin\\{figure|\\\\begin\\{table|\\\\begin\\{wrapfig|\\\\caption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\begin\\{figure|\\\\begin\\{table|\\\\begin\\{wrapfig|\\\\caption",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-26T08:45:29.980639+00:00_

16:\begin{figure}[t]
20:\caption{\textbf{Cross-architecture evaluation matrix.} Each cell reports $\Delta R^2$ (peak$-$exit). OpenVLA: VLA-to-VLA; TracVLA and NORA: VLM-to-VLA. Gray cells: checkpoints not released by original authors. Red borders indicate $\Delta R^2 > 0.10$.}
47:\begin{figure}[t]
51:\caption{\textbf{Layer-wise action-probe $R^2$ (LIBERO-Goal, readout token).} Solid: trained; dashed: reference. VLM-to-VLA transitions show pronounced peak-to-exit drops ($\Delta R^2 = 0.16$--$0.46$); VLA-to-VLA remains flat ($< 0.09$). Quantitative $\Delta R^2$ values use demo-level splitting (\S\ref{sec:cross_arch_analyses}); see Table~\ref{tab:cross_arch_matrix} for all cells.}
62:\begin{table}[t]
64:\caption{\textbf{Peak-to-exit action-probe drop across the architecture-suite matrix.} $\Delta R^2$ is computed as the difference between the maximum layer-wise action-probe $R^2$ and the exit-layer $R^2$. Values above 0.10 are treated as substantial descriptive drops. OpenVLA is a VLA-to-VLA comparison, whereas TracVLA and NORA are VLM-to-VLA comparisons.}
102:\begin{wrapfigure}{r}{0.46\columnwidth}
107:\caption{Counterfactual sensitivity across the architecture-suite matrix. (a)~Cohen's $d$ for four perturbation conditions (E=empty, W=wrong, S=shuffled, P=paraphrased); asterisks mark the top condition per cell; dashed line: large-effect threshold ($d = 0.8$). (b)~Cosine distance on hidden representations (different scale).}
119:\begin{table}[t]
121:\caption{\textbf{Counterfactual sensitivity summary.} Cohen's $d$ range and most sensitive perturbation for action-producing models (OpenVLA, TracVLA). NORA uses cosine distance on hidden representations (different scale; see \S\ref{sec:cf_repr}).}
160:\begin{wrapfigure}{r}{0.46\columnwidth}
165:\caption{L1 instruction-dominant head counts (trained vs.\ reference; heads with $>50\%$ attention on instruction tokens). Reference VLMs already saturate or near-saturate; training does not increase counts. Medians across available
…[truncated 33 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-26T08:45:30.934653+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\begin\\{figure|\\\\begin\\{table|\\\\caption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\begin\\{figure|\\\\begin\\{table|\\\\caption",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-26T08:45:32.290261+00:00_

13:\begin{figure}[t]
17:\caption{\textbf{Analysis framework.} We analyze hidden states at image-token averages and the readout token via layer-wise action probes, counterfactual instruction perturbations, and L1 attention profiling to distinguish training-associated changes from inherited backbone priors.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 1355
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-26T08:45:32.794111+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"^\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log | head -1 && grep \"Output written\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "description": "Check compiled PDF page count from LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"^\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log | head -1 && grep \"Output written\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "description": "Check compiled PDF page count from LaTeX log"
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-26T08:45:32.844780+00:00_

1110
Output written on main.pdf (40 pages, 1154154 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-26T08:47:54.086253+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read references.bib for format audit",
  "subagent_type": "Explore",
  "prompt": "Read the full contents of /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib and report back the entire file content. I need to audit reference format consistency (conference name abbreviations, page formats, year formats, author formats, DOI presence, etc.). Report any inconsistencies you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Agent",
  "tool_args": {
    "description": "Read references.bib for format audit",
    "subagent_type": "Explore",
    "prompt": "Read the full contents of /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib and report back the entire file content. I need to audit reference format consistency (conference name abbreviations, page formats, year formats, author formats, DOI presence, etc.). Report any inconsistencies you find."
  }
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-26T08:47:55.893114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 214 · 2026-05-26T08:47:55.943900+00:00_

1	% === VLA / Architecture ===
2	
3	@article{hancock2025actions,
4	  title     = {Actions as Language: Fine-Tuning {VLMs} into {VLAs} Without Catastrophic Forgetting},
5	  author    = {Hancock, Asher J. and Wu, Xindi and Zha, Lihan and Russakovsky, Olga and Majumdar, Anirudha},
6	  journal   = {arXiv preprint arXiv:2509.22195},
7	  year      = {2025},
8	}
9	
10	@article{lian2026bayesianvla,
11	  title     = {{BayesianVLA}: {B}ayesian Decomposition of Vision Language Action Models via Latent Action Queries},
12	  author    = {Lian, Shijie and others},
13	  journal   = {arXiv preprint arXiv:2601.15197},
14	  year      = {2026},
15	}
16	
17	@article{kachaev2025dont,
18	  title     = {Don't Blind Your {VLA}: Aligning Visual Representations for {OOD} Generalization},
19	  author    = {Kachaev, Nikita and Lyzhov, Alexander and Konovalov, Vladislav and Panov, Aleksandr},
20	  journal   = {arXiv preprint arXiv:2510.25616},
21	  year      = {2025},
22	}
23	
24	@article{mitra2025mechanistic,
25	  title     = {Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations},
26	  author    = {Mitra, Ananye and Luo, Sudeep and Saravanan, Dhruv and Niu, Sicheng and Pai, Deepak and Thomason, Jesse and Darrell, Trevor and Anwar, Mohamed and Ramanan, Deva and Herzig, Roei},
27	  journal   = {arXiv preprint arXiv:2511.22697},
28	  year      = {2025},
29	}
30	
31	@article{zhang2026instruction,
32	  title     = {Instruction Anchor: Dissecting the Mechanistic Dynamics of Modality Arbitration},
33	  author    = {Zhang, Zhenyu and Xu, Jiahe and Bai, Chao and Chen, Mingyu and Zhang, Xun and Xiang, Tao and Zhang, Ya},
34	  journal   = {arXiv preprint arXiv:2602.03677},
35	  year      = {2026},
36	}
37	
38	@article{liu2026forgetting,
39	  title     = {Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning},
40	  author    = {Liu, Huihan and Kim, Changyeon and Liu, Bo and Liu, Minghuan and Zhu, Yuke},
41	  journal   = {arXi
…[truncated 20696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-26T08:48:11.101720+00:00_

## Reference Format Consistency Audit

I've read the complete references.bib file. Here is my analysis of inconsistencies:

### **Major Format Inconsistencies Found:**

#### 1. **Conference/Venue Names**
- Inconsistent abbreviation conventions:
  - `Advances in Neural Information Processing Systems (NeurIPS)` - full name + abbreviation
  - `International Conference on Machine Learning (ICML)` - full name + abbreviation
  - `International Conference on Learning Representations (ICLR)` - full name + abbreviation
  - `Conference on Empirical Methods in Natural Language Processing (EMNLP)` - full name + abbreviation
  - `IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)` - full name + abbreviation
  - BUT `ACL Workshop BlackboxNLP` - no parenthetical expansion (line 296)
  - BUT `Robotics: Science and Systems` - no abbreviation given (lines 395, 402)

#### 2. **Page Number Format Inconsistencies**
- Some entries have pages: `pages = {2679--2713}` (line 79), `pages = {23123--23144}` (line 89)
- Some have pages: `pages = {2733--2743}` (line 306), `pages = {355--362}` (line 349)
- Some have pages: `pages = {e1003553}` (electronic, line 319)
- Some entries have NO pages despite being inproceedings (lines 106, 125, 126, 141, 155, etc.)

#### 3. **Journal Entry Issues**
- `journal = {Transformer Circuits Thread}` (line 265) - not a traditional journal, unusual format
- Mix of proper journals and arXiv preprints:
  - arXiv: `journal = {arXiv preprint arXiv:XXXX.XXXXX}` (standard format)
  - But inconsistency in how arXiv IDs are formatted across entries

#### 4. **Author Format Inconsistencies**
- Some use `and others` (lines 12, 68, 96)
- Some list all authors (lines 4-5, 33-34, etc.)
- Varying use of special characters: `Daumé III` (line 61), `H{\"a}on` (line 169), `Adri{\`a}` (line 286)

#### 5. **Missing Critical Metadata**

**DOI Presence (VERY INCONSISTENT):**
- Only 3 entries have DOI: 
  - Line 308: `doi = {10.18653/v1/D19-1275}`
  - Line 321: `doi 
…[truncated 2168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Agent",
  "elapsed_ms": 17015
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-26T08:48:15.270780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-26T08:48:15.624741+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.
5	
6	%------------------------------------------------------------------
7	\subsection{Architectures and Data}
8	\label{sec:arch_data}
9	
10	We study three VLAs that span distinct backbone families (Table~\ref{tab:arch_overview}).
11	\textbf{OpenVLA}~\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.
12	It is pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).
13	\textbf{TracVLA}~\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).
14	Spatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.
15	TracVLA is trained on an OXE subset.
16	\textbf{NORA}~\cite{hung2025nora} uses Qwen2.5-VL-3B ($\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.
17	
18	Each architecture is evaluated in trained and reference conditions; we define the \emph{reference checkpoint} as the corresponding pretrained model before LIBERO fine-tuning.
19	A critical asymmetry distinguishes the reference baselines: the OpenVLA reference is an OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while the TracVLA and NORA references are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
20	OpenVLA trained-vs-
…[truncated 5519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-26T08:48:15.625521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-26T08:48:16.127429+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) fine-tune pretrained language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but which of the resulting representational changes reflect action training and which are inherited from the pretrained backbone?
5	In these decoder-only architectures, image tokens precede instruction tokens, and the causal attention mask restricts multimodal integration to a single readout token~\cite{wang2025seeing,pei2025rethinking}; how representations at this critical position are reshaped by action fine-tuning remains unknown.
6	
7	Behavioral studies show that VLAs exhibit visual dominance~\cite{grant2026} and underweight instructions~\cite{haon2025}, but existing representational analyses target single architectures.
8	No prior work tests whether instruction routing mechanisms are consistent across backbone families or decomposes training-associated effects from inherited base-model priors.
9	
10	We address this gap with a cross-architecture analysis of three VLAs (OpenVLA~\cite{kim2024_openvla}, TracVLA~\cite{zheng2024tracevla}, and NORA~\cite{hung2025nora}) across four LIBERO~\cite{liu2023_libero} task suites (\S\ref{sec:setup}).
11	TracVLA and NORA baselines are pure VLMs ($N = 2$ independent VLM-to-VLA transitions); OpenVLA's baseline is the OXE-pretrained~\cite{padalkar2023_oxe} VLA (VLA-to-VLA transition).
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=0.88\linewidth]{figures/fig_overview.pdf}
16	\vspace{-6pt}
17	\caption{\textbf{Analysis framework.} We analyze hidden states at image-token averages and the readout token via layer-wise action probes, counterfactual instruction perturbations, and L1 attention profiling to distinguish training-associated changes from inherited backbone priors.}
18	\label{fig:overview}
19	\vspace{-6pt}
20	\end{figure}
21	
22	Our analysis reveals 
…[truncated 1427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-26T08:48:16.279251+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.log",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.log",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-26T08:48:16.330269+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-26T08:48:20.094302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-26T08:48:20.245337+00:00_

1	This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex 2026.5.2)  26 MAY 2026 08:12
2	entering extended mode
3	 restricted \write18 enabled.
4	 %&-line parsing enabled.
5	**main.tex
6	(./main.tex
7	LaTeX2e <2025-11-01>
8	L3 programming layer <2026-01-19>
9	(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
10	Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
11	(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo
12	File: size10.clo 2025/01/22 v1.4n Standard LaTeX file (size option)
13	)
14	\c@part=\count275
15	\c@section=\count276
16	\c@subsection=\count277
17	\c@subsubsection=\count278
18	\c@paragraph=\count279
19	\c@subparagraph=\count280
20	\c@figure=\count281
21	\c@table=\count282
22	\abovecaptionskip=\skip49
23	\belowcaptionskip=\skip50
24	\bibindent=\dimen148
25	) (./corl_2026.sty
26	Package: corl_2026 2026/08/15 CORL2026 submission/preprint/camera-ready style f
27	ile
28	
29	(/usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty
30	Package: lineno 2025/05/13 line numbers on paragraphs v5.5
31	
32	(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty
33	Package: etoolbox 2025/10/02 v2.5m e-TeX tools for LaTeX (JAW)
34	\etb@tempcnta=\count283
35	)
36	(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty
37	Package: kvoptions 2022-06-15 v3.15 Key value format for package options (HO)
38	
39	(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty
40	Package: keyval 2022/05/29 v1.15 key=value parser (DPC)
41	\KV@toks@=\toks17
42	)
43	(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty
44	Package: ltxcmds 2023-12-04 v1.26 LaTeX kernel commands for general use (HO)
45	)
46	(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty
47	Package: kvsetkeys 2022-10-05 v1.19 Key value parser (HO)
48	))
49	\linenopenalty=\count284
50	\output=\toks18
51	\linenoprevgraf=\count285
52	\linenumbersep=\dimen149
53	\linenumberwidth=\dimen150
54	\c@linenumber
…[truncated 1887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-26T08:48:20.647174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-26T08:48:20.748598+00:00_

1	\paragraph{Use of Generative AI.}
2	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
3	
4	\appendix
5	
6	\section{Supplementary Material}
7	\label{sec:appendix}
8	
9	Unless noted otherwise, all analyses use OpenVLA-7B (\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).
10	Model conditions, representation extraction, metric definitions, and probe architectures follow \S\ref{sec:method}.
11	Cross-suite experiments (\S\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\times$ 50 demonstrations).
12	All experiments ran on 2$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (96\,GB each); random seed is 42 unless stated otherwise.
13	
14	\subsection{Architecture Summary}
15	\label{sec:arch_table_appendix}
16	
17	\begin{table}[h]
18	\centering
19	\caption{Architectures studied. The reference baselines differ in kind: the OpenVLA reference is an OXE-pretrained VLA that produces actions; TracVLA and NORA references are pure VLMs with no action training.}
20	\label{tab:arch_overview}
21	\footnotesize
22	\setlength{\tabcolsep}{3pt}
23	\begin{tabular}{@{}llccll@{}}
24	\toprule
25	Arch. & Backbone & Layers & Attention & Vision Enc. & Reference Baseline \\
26	\midrule
27	OpenVLA & Llama-2-7B & 32 & 32 MHA & DinoSigLIP $\to$ MLP proj. & OXE-pret.\ VLA \\
28	TracVLA & Phi-3-mini & 32 & 32 MHA & SigLIP + spatial trace & Phi-3-Vision (VLM) \\
29	NORA & Qwen2.5-VL-3B & 36 & 16q/2kv GQA & Qwen2.5-VL native & Qwen2.5-VL (VLM) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\subsection{OpenVLA-Specific Analysis Methods}
35	\label{sec:openvla_methods_appendix}
36	
37	Three additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.
38	
39	\paragraph{Cross-instruction pro
…[truncated 1472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-26T08:48:28.082860+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"Warning\\|Overfull\\|Underfull\\|undefined\\|multiply defined\\|Missing\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log 2>/dev/null",
  "description": "Count warnings in LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"Warning\\|Overfull\\|Underfull\\|undefined\\|multiply defined\\|Missing\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log 2>/dev/null",
    "description": "Count warnings in LaTeX log"
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-26T08:48:28.133524+00:00_

74

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-26T08:48:33.352672+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Warning|Overfull|Underfull|undefined|multiply defined",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content",
  "head_limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Warning|Overfull|Underfull|undefined|multiply defined",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content",
    "head_limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-26T08:48:33.453645+00:00_

590:Underfull \vbox (badness 6396) has occurred while \output is active []
594:Underfull \hbox (badness 1342) in paragraph at lines 66--1
600:Underfull \vbox (badness 3098) has occurred while \output is active []
617:Underfull \vbox (badness 10000) has occurred while \output is active []
627:Underfull \hbox (badness 10000) in paragraph at lines 116--118
632:Underfull \hbox (badness 2150) in paragraph at lines 116--118
645:Underfull \hbox (badness 3471) in paragraph at lines 165--165
650:Package wrapfig Warning: Stationary wrapfigure forced to float on input line 17
654:Underfull \hbox (badness 1248) in paragraph at lines 174--2
659:Underfull \hbox (badness 1158) in paragraph at lines 174--2
665:Underfull \hbox (badness 1371) in paragraph at lines 174--2
672:LaTeX Warning: `h' float specifier changed to `ht'.
687:LaTeX Warning: `h' float specifier changed to `ht'.
712:LaTeX Warning: `h' float specifier changed to `ht'.
715:Underfull \vbox (badness 1616) has occurred while \output is active []
719:LaTeX Warning: `h' float specifier changed to `ht'.
722:Underfull \vbox (badness 10000) has occurred while \output is active []
733:LaTeX Warning: `h' float specifier changed to `ht'.
736:LaTeX Warning: `h' float specifier changed to `ht'.
763:LaTeX Warning: `h' float specifier changed to `ht'.
773:LaTeX Warning: `h' float specifier changed to `ht'.
776:Underfull \vbox (badness 10000) has occurred while \output is active []
780:LaTeX Warning: `h' float specifier changed to `ht'.
797:LaTeX Warning: `h' float specifier changed to `ht'.
800:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
804:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
808:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
812:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
817:LaTeX Warning: `h' float specifier changed to `ht'.
820:LaTeX Warning: `h' float specifier changed to `ht'.
823:Underfull \vbox (badness 10000) h
…[truncated 2932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-26T08:48:37.921314+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "undefined reference|multiply defined|Citation.*undefined",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "undefined reference|multiply defined|Citation.*undefined",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-26T08:48:37.971938+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-26T08:48:41.836946+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Output written|pages,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Output written|pages,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-26T08:48:41.939111+00:00_

1104:Output written on main.pdf (40 pages, 1154154 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 234 · 2026-05-26T08:48:45.759639+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Overfull \\\\hbox",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Overfull \\\\hbox",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-26T08:48:45.810322+00:00_

1066:Overfull \hbox (16.31764pt too wide) in paragraph at lines 1339--1350

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-26T08:48:48.069260+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "wrapfig Warning",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "wrapfig Warning",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-26T08:48:48.119831+00:00_

650:Package wrapfig Warning: Stationary wrapfigure forced to float on input line 17

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-26T08:48:52.342360+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\begin\\{(figure|table|wrapfigure)\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\begin\\{(figure|table|wrapfigure)\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-26T08:48:52.393075+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-26T08:48:56.208543+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\begin\\{(figure|table|wrapfigure)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\begin\\{(figure|table|wrapfigure)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 241 · 2026-05-26T08:48:56.259211+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:16:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:47:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:62:\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:102:\begin{wrapfigure}{r}{0.46\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:119:\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:160:\begin{wrapfigure}{r}{0.46\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:17:\begin{table}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:92:\begin{table}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:147:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:167:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:179:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:199:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:213:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:248:\begin{table}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:270:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:277:\begin{table}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:298:\begin{table}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_
…[truncated 4532 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-26T08:49:06.756230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 243 · 2026-05-26T08:49:06.807017+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	\usepackage{wrapfig}
16	
17	\title{Instruction Routing in Fine-Tuned Vision-Language-Action Models:\\ A Cross-Architecture Analysis}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	
23	\maketitle
24	
25	\begin{abstract}
26	\input{abstract}
27	\end{abstract}
28	
29	\keywords{Vision-Language-Action models, representational analysis, attention routing, fine-tuning}
30	
31	\input{introduction}
32	\input{related_work}
33	\input{method}
34	\input{experiments}
35	\input{discussion}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-26T08:49:07.259224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-26T08:49:07.309907+00:00_

1	% File: corl_2026.sty 
2	%
3	% Latex templates for the Conference on Robot Learning (CoRL)
4	%
5	% This template is heavily inspired by the NeurIPS, ICML, ICLR and IEEE Transactions latex templates.
6	% Hence we would like to thank: Roman Garnett and the previous mantainers of the NIPS style, Percy Liang and the previous mantainers of the ICML style, Hugo Larochelle for the ICLR style, and Michael Shell for the IEEE Transactions style.
7	%
8	% History:
9	% 2017/04/16 - First revision by Roberto Calandra (roberto.calandra@berkeley.edu).
10	%	       Main changes:
11	%	       - The abstract is more compact compared to NeurIPS/ICML
12	%	       - References are by default using natbib with squared numbers (e.g., [1])
13	%	       - DOI fields from the bibtex are automatically converted to hyperlinks 
14	%	       to the corresponding page
15	%	       - acknowledgments are now a command, and the corresponding subsubsection is
16	%	       automatically included only in the final version
17	% 2017/06/12 - Modified to use corlabbrvnat.bst, which order the reference by order of appearance in the paper
18	% 2017/06/13 - fixed typo
19	% 2018/05/09 - Slightly modified for CoRL 2018 by Jun Morimoto (xmorimo@atr.jp)
20	% 2019/01/28 - Slightly modified for CoRL 2019 by Jun Nakanishi (jnakanis@meijo-u.ac.jp)
21	% 2020/02/02 - Slightly modified for CoRL 2020 by Cynthia Matuszek (cmat@umbc.edu)
22	% 2020/08/19 - Added preprint option by Roberto Calandra (rcalandra@fb.com)
23	% 2021/05/06 - Slightly modified for CoRL 2021 by Gerhard Neumann (gerhard.neumann@kit.edu)
24	% 2022/03/09 - Slightly modified for CoRL 2022 by Minas Liarokapis (minas.liarokapis@auckland.ac.nz)
25	% 2022/03/06 - Slightly modified for CoRL 2023 by Marc Toussaint (toussaint@tu-berlin.de)
26	% 2024/03/26 - Slightly modified for CoRL 2024 by David Held (dheld@andrew.cmu.edu)
27	% 2026/01/10 - Slightly modified for CoRL 2026 by Yoonchang Sung (yoonchang.sung@ntu.edu.sg)
28	%
29	% TODO: nohyperref is not working at th
…[truncated 743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-26T08:49:11.829353+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "page.*limit|maximum.*page|8 page",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "page.*limit|maximum.*page|8 page",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-26T08:49:11.881119+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-26T08:49:17.024469+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\begin\\{table|\\\\caption|\\\\begin\\{tabular|\\\\end\\{table",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\begin\\{table|\\\\caption|\\\\begin\\{tabular|\\\\end\\{table",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-26T08:49:17.075215+00:00_

20:\caption{\textbf{Cross-architecture evaluation matrix.} Each cell reports $\Delta R^2$ (peak$-$exit). OpenVLA: VLA-to-VLA; TracVLA and NORA: VLM-to-VLA. Gray cells: checkpoints not released by original authors. Red borders indicate $\Delta R^2 > 0.10$.}
51:\caption{\textbf{Layer-wise action-probe $R^2$ (LIBERO-Goal, readout token).} Solid: trained; dashed: reference. VLM-to-VLA transitions show pronounced peak-to-exit drops ($\Delta R^2 = 0.16$--$0.46$); VLA-to-VLA remains flat ($< 0.09$). Quantitative $\Delta R^2$ values use demo-level splitting (\S\ref{sec:cross_arch_analyses}); see Table~\ref{tab:cross_arch_matrix} for all cells.}
62:\begin{table}[t]
64:\caption{\textbf{Peak-to-exit action-probe drop across the architecture-suite matrix.} $\Delta R^2$ is computed as the difference between the maximum layer-wise action-probe $R^2$ and the exit-layer $R^2$. Values above 0.10 are treated as substantial descriptive drops. OpenVLA is a VLA-to-VLA comparison, whereas TracVLA and NORA are VLM-to-VLA comparisons.}
68:\begin{tabular}{@{}lll cccc@{}}
90:\end{table}
107:\caption{Counterfactual sensitivity across the architecture-suite matrix. (a)~Cohen's $d$ for four perturbation conditions (E=empty, W=wrong, S=shuffled, P=paraphrased); asterisks mark the top condition per cell; dashed line: large-effect threshold ($d = 0.8$). (b)~Cosine distance on hidden representations (different scale).}
119:\begin{table}[t]
121:\caption{\textbf{Counterfactual sensitivity summary.} Cohen's $d$ range and most sensitive perturbation for action-producing models (OpenVLA, TracVLA). NORA uses cosine distance on hidden representations (different scale; see \S\ref{sec:cf_repr}).}
124:\begin{tabular}{@{}llcl@{}}
136:\end{table}
165:\caption{L1 instruction-dominant head counts (trained vs.\ reference; heads with $>50\%$ attention on instruction tokens). Reference VLMs already saturate or near-saturate; training does not increase counts. Medians across available LIBERO suites per architecture.
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-26T08:49:21.794072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1330",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1330",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-26T08:49:21.794435+00:00_

1330	Three methodologically distinct approaches triangulate instruction routing in VLAs.
1331	Table~\ref{tab:convergent_evidence} summarizes what each method measures, its key finding, evidence type, and acknowledged limitation.
1332	
1333	\begin{table}[h]
1334	\centering
1335	\caption{\textbf{Convergent evidence across three analytical methods.} Each method addresses a different aspect of instruction routing; no single method is sufficient alone, but their convergence strengthens the overall characterization.}
1336	\label{tab:convergent_evidence}
1337	\small
1338	\setlength{\tabcolsep}{3pt}
1339	\begin{tabular}{@{}p{2.2cm}p{3.0cm}p{3.5cm}p{2.0cm}p{3.0cm}@{}}
1340	\toprule
1341	Method & What it measures & Key finding & Evidence type & Limitation \\
1342	\midrule
1343	Layer-wise probing (\S\ref{sec:r2_collapse}) & Where action-relevant information is decodable & VLM-to-VLA: peak-to-exit collapse ($\Delta R^2 = 0.16$--$0.46$); VLA-to-VLA: flat & Correlational (decodability) & Does not establish causal necessity \\
1344	\addlinespace
1345	Counterfactual perturbation (\S\ref{sec:cf_sensitivity}) & Whether instruction content affects model outputs & All trained VLAs: graded divergence ($d = 0.45$--$1.52$) ordered by semantic distance & Behavioral (input--output) & Does not localize which layers are responsible \\
1346	\addlinespace
1347	Attention head ablation (Appendix~\ref{sec:action_trajectory}) & Whether identified structures carry functional signals & Dose-response: monotonic divergence ($d = 0.48$--$0.64$) upon progressive head removal & Interventional (causal contribution) & Single architecture (OpenVLA); contribution $\neq$ necessity \\
1348	\bottomrule
1349	\end{tabular}
1350	\end{table}
1351	
1352	The three methods form a complementary chain: probing identifies \emph{where} instruction information concentrates across layers, perturbation confirms \emph{whether} instruction content functionally affects behavior, and ablation demonstrates \emph{that} the identifi
…[truncated 212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-26T08:49:22.045447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1215",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1215",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-26T08:49:22.096131+00:00_

1215	NLP fine-tuning ($\Delta R^2 = 0.000$) and pretrained references ($\Delta R^2 \leq 0.097$) cluster below the $0.10$ threshold; VLM-to-VLA fine-tuning produces large collapse ($\Delta R^2 = 0.156$--$0.455$); subsequent VLA-to-VLA fine-tuning does not intensify it ($\Delta R^2 = 0.033$--$0.086$).
1216	This constrains the onset: exit collapse emerges during the first action-grounded training stage and does not accumulate with continued task-specific fine-tuning.
1217	
1218	\begin{figure}[h]
1219	\centering
1220	\includegraphics[width=0.55\columnwidth]{figures/fig_training_dynamics.pdf}
1221	\caption{\textbf{$\Delta R^2$ across training pathways.} Each point is one architecture-suite cell; markers distinguish backbone families. Exit collapse (above dashed line) is confined to VLM-to-VLA transitions and does not intensify during VLA-to-VLA fine-tuning.}
1222	\label{fig:training_dynamics}
1223	\end{figure}
1224	
1225	\subsection{Methodological Context}
1226	\label{sec:methodological_context}
1227	
1228	Representational analysis is an established methodology in the interpretability tradition; behavioral validation provides complementary evidence but is not a prerequisite for mechanistic characterization.
1229	Table~\ref{tab:methodological_precedent} situates our approach within this tradition.
1230	
1231	\begin{table}[h]
1232	\centering
1233	\caption{\textbf{Methodological precedent.} Representative interpretability studies and their use of behavioral evaluation. Partial behavioral eval includes correlational or indirect evidence.}
1234	\label{tab:methodological_precedent}
1235	\small
1236	\begin{tabular}{@{}llll@{}}
1237	\toprule
1238	Paper & Domain & Method & Behav.\ eval? \\
1239	\midrule
1240	Belinkov~\cite{belinkov2022} & NLP & Probing survey & No \\
1241	Olsson et al.~\cite{olsson2022} & LM & Induction heads & No \\
1242	Wang et al.~\cite{wang2023_ioi} & LM & IOI circuit & No \\
1243	Meng et al.~\cite{meng2022_rome} & LM & Causal tracing (localization) & No \\
1
…[truncated 1114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 254 · 2026-05-26T08:49:30.029435+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bibliographystyle|bibliography",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bibliographystyle|bibliography",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_2026.sty",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-26T08:49:30.082744+00:00_

79:  \bibliographystyle{corlabbrvnat}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 53
}
```

</details>

---

### Tool call

_source line 256 · 2026-05-26T08:49:34.051274+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\acknowledgments|acknowledgement|Acknowledge",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\acknowledgments|acknowledgement|Acknowledge",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-26T08:49:34.102006+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:138:\acknowledgments{If a paper is accepted, the final camera-ready version will (and probably should) include acknowledgments. All acknowledgments go at the end of the paper, including thanks to reviewers who gave useful comments, to colleagues who contributed to the ideas, and to funding agencies and corporate sponsors that provided financial support.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 258 · 2026-05-26T08:49:40.376912+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "github|gitlab|anonymous|author.*institution|university|lab\\b|funded|grant|support",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "github|gitlab|anonymous|author.*institution|university|lab\\b|funded|grant|support",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-26T08:49:40.477752+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:11:Behavioral evaluations of VLAs reveal visual dominance~\cite{grant2026,hou2026,fei2025}; mechanistic studies identify sparse semantic directions~\cite{haon2025}, interpretable features~\cite{swann2026,buurmeijer2026}, symbolic representations~\cite{lu2025,molinari2025}, comprehension-action trade-offs~\cite{fang2025}, and task-specific attention heads for selective fine-tuning~\cite{mitra2025mechanistic}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:45:Monte Carlo cross-validation supports this separation: VLM-to-VLA trained CIs lie entirely above zero (lower bounds $\geq 0.09$), while VLA-to-VLA trained CIs span or nearly span zero (Table~\ref{tab:cross_arch_matrix}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex:19:\author{Anonymous}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:22:For OpenVLA, two additional conditions support deep-dive analyses (\S\ref{sec:openvla_routing}): the Llama-2 base language model (no VLA fine-tuning) and a random-weight initialization via \texttt{from\_config()}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:38:OpenVLA additionally provides representations from the DinoSigLIP projector output (4{,}096-D), DINOv2 and CLIP external baselines, and the branch-split before fusion; these sources support the OpenVLA deep-dive analyses (\S\ref{sec:openvla_routing}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:66:OpenVLA additionally supports cross-instruction probes, representational similarity analysis (RSA)~\cite{kriegeskorte2008}, and external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}); these single-architecture methods are detailed in Appendix~\ref{sec:openvla_methods_appendix}.
/home/ubuntu/.agent-ml-r
…[truncated 2779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 260 · 2026-05-26T08:49:44.932103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "0",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "0",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-26T08:49:44.995340+00:00_

0	\paragraph{Use of Generative AI.}
1	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
2	
3	\appendix
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 63
}
```

</details>

---

### Tool call

_source line 262 · 2026-05-26T08:49:58.864174+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\[0-9]+\\\\$|shipout.*page|^\\\\[.*\\\\]$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\[0-9]+\\\\$|shipout.*page|^\\\\[.*\\\\]$",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-26T08:49:58.914696+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-26T08:50:01.678203+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "^\\[",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "^\\[",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-26T08:50:01.729200+00:00_

431:[Loading MPS to PDF converter (version 2006.09.02).]
584:[1
595:[]\T1/ptm/m/n/10 OpenVLA ad-di-tion-ally sup-ports cross-instruction probes, re
610:[5 <./figures/fig_matrix_heatmap.pdf>]
628:[]\T1/ptm/m/n/10 Two Open-VLA cells per-mit same-metric
638:[7 <./figures/fig_counterfactual_bar.pdf>]
646:[]\T1/ptm/m/n/10 Figure 5: []L1 instruction-dominant head
655:[]\T1/ptm/m/n/10 The three anal-y-ses sep-a-rate two em-pir-i-cal pat-
674:[12] [13] [14]
689:[15 <./figures/fig6.pdf>]
738:[19 <./figures/fig_dose_response.pdf>]
765:[21 <./figures/fig_linear_vs_mlp_probe.pdf> <./figures/fig4.pdf>]
782:[23 <./figures/fig7.pdf>]
815:[25]
836:[28 <./figures/fig_probe_conditions.pdf>]
850:[29 <./figures/fig_cross_architecture_attention.pdf>]
876:[30 <./figures/fig_cross_arch_l1.pdf> <./figures/fig_l1_stacked_bar.pdf>]
883:[31 <./figures/fig_multi_layer_attn.pdf>]
899:[32] [33]
918:[34]
925:[37]
939:[38 <./figures/fig_training_dynamics.pdf>]
964:[]\T1/ptm/m/n/9 Where action-relevant
974:[]\T1/ptm/m/n/9 Correlational
979:[]\T1/ptm/m/n/9 Does not es-tab-lish
984:[]\T1/ptm/m/n/9 Counterfactual
994:[]\T1/ptm/m/n/9 Whether in-struc-tion
1010:[]\T1/ptm/m/n/9 Behavioral
1015:[]\T1/ptm/m/n/9 Attention head
1025:[]\T1/ptm/m/n/9 Whether iden-ti-fied
1047:[]\T1/ptm/m/n/9 Interventional
1057:[]\T1/ptm/m/n/9 Single ar-chi-tec-ture

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 266 · 2026-05-26T08:50:18.394939+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\[8\\]|\\[9\\]|\\[10\\]|\\[11\\]|\\[12\\]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\[8\\]|\\[9\\]|\\[10\\]|\\[11\\]|\\[12\\]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 267 · 2026-05-26T08:50:18.445603+00:00_

669:) (./main.bbl [8 <./figures/fig_l1_attention.pdf>] [9] [10] [11])
674:[12] [13] [14]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 268 · 2026-05-26T08:50:35.067659+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 269 · 2026-05-26T08:50:35.118080+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 270 · 2026-05-26T08:51:10.367168+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: info] Camera-Ready QA — CoRL 2026 格式合规检查完成\n\n## 1. 模板/格式 ✅\n- `\\usepackage{corl_2026}` 正确加载，submission 模式（无 `[final]`），行号已启用\n- `corl_2026.sty` 版本 2026/08/15，10th CoRL, Austin TX\n- `\\bibliographystyle{corlabbrvnat}` 由 sty 自动设置\n- 主体约 8 页（pages 1-8），参考文献 3 页（9-11），附录 28 页（12-40），总 40 页。主体页数符合 CoRL 限制\n\n## 2. 匿名性 ✅\n- `\\author{Anonymous}`，无 `\\acknowledgments`\n- 全文 grep 无 github/gitlab/institution/university/lab/grant/funding 泄露\n- \"Code and data will be released upon acceptance\" — 标准非识别性表述\n- Generative AI 声明在 bibliography 后、appendix 前，无识别信息\n\n## 3. LaTeX 编译质量\n- **无 undefined reference / multiply defined / citation undefined** ✅\n- **1 个 Overfull hbox**（16.3pt）在 appendix lines 1339-1350（convergent evidence 表格）— 表格宽度超出 text width 约 5.7mm\n  - [severity: warning] 建议缩小该表格字号（`\\scriptsize`）或缩窄列宽（`p{2.8cm}` → `p{2.5cm}`）\n- **1 个 wrapfig warning**（line 170 experiments.tex，L1 attention 图被迫浮动）— 常见，不影响渲染\n- **~20 个 `h` float specifier changed to `ht`** — 全部在 appendix，LaTeX 正常行为，无需处理\n- **多个 Underfull hbox/vbox** — 排版微调级别，不影响审稿\n\n## 4. 图表规范 ✅\n- **Caption 位置**：所有 table caption 在 `\\begin{tabular}` 之上，所有 figure caption 在 `\\includegraphics` 之下，符合学术规范\n- 主文 2 个 figure（fig_matrix_heatmap, fig_r2_collapse）+ 2 个 wrapfigure（fig_counterfactual_bar, fig_l1_attention）+ 2 个 table（tab_cross_arch_matrix, tab_cf_summary）+ 1 个 overview figure\n- 编号连续，无跳号/重复\n\n## 5. 参考文献格式\n- [severity: warning] **格式一致性问题**（非阻塞但影响专业度）：\n  - `and others` vs 全列作者名不统一（3 处用 `and others`）\n  - DOI 仅 3/60+ 条目有，绝大多数缺失\n  - 部分 inproceedings 缺 pages 字段\n  - 少量 venue 名称不统一（`ACL Workshop BlackboxNLP` vs 全名+缩写模式）\n  - 4 个 2026 预印本用 `note = {arXiv:...}` 而非 `journal = {arXiv preprint}`\n  - **建议**：这些是 camera-ready 阶段修复项，submission 阶段不会因此被拒，但建议接收后统一\n\n## 6. Appendix 结构 ✅\n- `\\appendix` 在 `\\bibliography{references}` 之后，通过 `\\input{appendix}` 加入\n- CoRL 允许 same-PDF appendix，当前结构合规\n- Appendix 首节为 `\\section{Supplementary Material}`，编号自动为 A\n\n## 总结\n**无 critical 问题。** 2 个 warning（appendix 表格 overfull、参考文献格式不统一）均为非阻塞性质。论文格式满足 CoRL 2026 submission 要求。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: info] Camera-Ready QA — CoRL 2026 格式合规检查完成\n\n## 1. 模板/格式 ✅\n- `\\usepackage{corl_2026}` 正确加载，submission 模式（无 `[final]`），行号已启用\n- `corl_2026.sty` 版本 2026/08/15，10th CoRL, Austin TX\n- `\\bibliographystyle{corlabbrvnat}` 由 sty 自动设置\n- 主体约 8 页（pages 1-8），参考文献 3 页（9-11），附录 28 页（12-40），总 40 页。主体页数符合 CoRL 限制\n\n## 2. 匿名性 ✅\n- `\\author{Anonymous}`，无 `\\acknowledgments`\n- 全文 grep 无 github/gitlab/institution/university/lab/grant/funding 泄露\n- \"Code and data will be released upon acceptance\" — 标准非识别性表述\n- Generative AI 声明在 bibliography 后、appendix 前，无识别信息\n\n## 3. LaTeX 编译质量\n- **无 undefined reference / multiply defined / citation undefined** ✅\n- **1 个 Overfull hbox**（16.3pt）在 appendix lines 1339-1350（convergent evidence 表格）— 表格宽度超出 text width 约 5.7mm\n  - [severity: warning] 建议缩小该表格字号（`\\scriptsize`）或缩窄列宽（`p{2.8cm}` → `p{2.5cm}`）\n- **1 个 wrapfig warning**（line 170 experiments.tex，L1 attention 图被迫浮动）— 常见，不影响渲染\n- **~20 个 `h` float specifier changed to `ht`** — 全部在 appendix，LaTeX 正常行为，无需处理\n- **多个 Underfull hbox/vbox** — 排版微调级别，不影响审稿\n\n## 4. 图表规范 ✅\n- **Caption 位置**：所有 table caption 在 `\\begin{tabular}` 之上，所有 figure caption 在 `\\includegraphics` 之下，符合学术规范\n- 主文 2 个 figure（fig_matrix_heatmap, fig_r2_collapse）+ 2 个 wrapfigure（fig_counterfactual_bar, fig_l1_attention）+ 2 个 table（tab_cross_arch_matrix, tab_cf_summary）+ 1 个 overview figure\n- 编号连续，无跳号/重复\n\n## 5. 参考文献格式\n- [severity: warning] **格式一致性问题**（非阻塞但影响专业度）：\n  - `and others` vs 全列作者名不统一（3 处用 `and others`）\n  - DOI 仅 3/60+ 条目有，绝大多数缺失\n  - 部分 inproceedings 缺 pages 字段\n  - 少量 venue 名称不统一（`ACL Workshop BlackboxNLP` vs 全名+缩写模式）\n  - 4 个 2026 预印本用 `note = {arXiv:...}` 而非 `journal = {arXiv preprint}`\n  - **建议**：这些是 camera-ready 阶段修复项，submission 阶段不会因此被拒，但建议接收后统一\n\n## 6. Appendix 结构 ✅\n- `\\appendix` 在 `\\bibliography{references}` 之后，通过 `\\input{appendix}` 加入\n- CoRL 允许 same-PDF appendix，当前结构合规\n- Appendix 首节为 `\\section{Supplementary Material}`，编号自动为 A\n\n## 总结\n**无 critical 问题。** 2 个 warning（appendix 表格 overfull、参考文献格式不统一）均为非阻塞性质。论文格式满足 CoRL 2026 submission 要求。",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 271 · 2026-05-26T08:51:14.550084+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 4182
}
```

</details>

---

### Assistant

_source line 272 · 2026-05-26T08:51:18.058452+00:00_

Camera-ready QA 已完成并提交。两个 warning：appendix 中 convergent evidence 表格 overfull（16.3pt），参考文献格式不完全统一。无 critical 问题，submission 格式合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---

## Round 7

16 recorded events

### User

_source line 273 · 2026-05-26T12:28:33.020781+00:00_

[System 触发审查]:
两项审查请求（Paper DDL 5/29 前最后一轮深度审视）：

**请求 1：17 个 negative 结果逐条审查**
论文 107 success / 17 negative / 7 failed。请逐条审查 17 个 negative 结果：
- 每个 negative 的 hypothesis 是什么？为什么失败？
- 是否有任何一个值得用不同方法/参数/设置重试（≤4 GPU·h）？
- 是否有 negative 结果本身是有价值的 finding，应该在论文中更突出地呈现？（e.g., "X doesn't work, which is informative because..."）
- 特别关注：是否有 negative 暴露了 claim 的边界条件，需要在 limitation 中更明确讨论？

目标：给 GPU 利用一个最终答案——17 个 negative 中是否有任何一个值得用 idle GPU 重做。

**请求 2：论文 story 最终审视**
假设你是 CoRL reviewer，从头到尾读一遍当前论文的 claim 链：
- Claim 措辞强度是否匹配证据？有没有过强或过弱的地方？
- 107 个实验数据是否在正文+appendix 中充分利用？有没有遗漏的数据点可以加强叙事？
- Negative 结果在 Discussion/Limitation 中讨论是否充分？
- 整体 story 从 Intro → Method → Results → Discussion 的逻辑流是否有断裂？

不需要重复数字一致性检查。聚焦 story coherence 和 claim-evidence alignment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system"
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-26T12:28:43.239662+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 275 · 2026-05-26T12:28:43.290352+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 276 · 2026-05-26T12:28:46.302321+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'conclusion': 'negative'}",
  "project": "vla-ssd",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'conclusion': 'negative'}",
    "project": "vla-ssd",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-26T12:28:48.160358+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"object_untrained_pipeline_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:59:29.590Z\", \"updated_at\": \"2026-05-21T10:39:10.742Z\", \"hypothesis\": \"Untrained OpenVLA base model (openvla-7b) on LIBERO-Object lacks the convergent routing pattern (R² collapse, L1 specialization, counterfactual convergence) seen in the fine-tuned model, confirming routing is training-induced.\", \"parent\": \"object_pipeline_ridge_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py --conditions untrained\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"546802\", \"log_path\": \"~/runs/vla-ssd/object_untrained_pipeline_v1.log\", \"submitted_at\": \"2026-05-21T08:59:56.591Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/libero_object_untrained/\", \"wall_clock_seconds\": 5954.2, \"gpu_hours\": 1.65}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T10:39:10.742Z\"}, \"behavioral_smoketest\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:26:07.290Z\", \"updated_at\": \"2026-05-20T20:34:40.914Z\", \"parent\": \"behavioral_pilot_w4\", \"hypothesis\": \"Fine-tuned OpenVLA can successfully execute LIBERO-Goal tasks in closed-loop rollout on westd-19183, establishing a baseline success rate for subsequent ablation comparison.\", \"spec\": {\"command\": \"NUMBA_DISABLE_JIT=1 CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python behavioral_smoketest.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/LIBERO\", \"data_count\": \"1 task x 3 ep\", \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/ope
…[truncated 30051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1858
}
```

</details>

---

### Tool call

_source line 278 · 2026-05-26T12:28:48.160720+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 279 · 2026-05-26T12:28:48.612778+00:00_

1	When vision-language models are fine-tuned for robotic action prediction, which representational changes reflect training and which are inherited from the pretrained backbone?
2	We conduct a cross-architecture representational analysis of three Vision-Language-Action models across four LIBERO task suites, using layer-wise action probes, attention profiling, and counterfactual instruction perturbations to compare trained and reference checkpoints.
3	We find that VLM-to-VLA fine-tuning produces a consistent exit-layer collapse in action-probe decodability that is absent in VLA-to-VLA transitions and in NLP instruction-tuning controls, suggesting this reorganization is specific to action-oriented training.
4	Complementary analyses reveal that trained VLAs develop substantial sensitivity to instruction content while the dominant attention patterns at early layers largely pre-exist in pretrained backbones.
5	These findings provide a cross-architecture decomposition of instruction routing in fine-tuned VLAs, disentangling training-associated representational changes from inherited structure.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 280 · 2026-05-26T12:28:48.813954+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1086",
  "limit": "130"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1086",
    "limit": "130"
  }
}
```

</details>

---

### Tool result

_source line 281 · 2026-05-26T12:28:48.915291+00:00_

1086	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
1087	 & Reference & Trained & Reference & Trained \\
1088	\midrule
1089	L0  & $\mathbf{0.629 \pm 0.016}$ & $0.629 \pm 0.016$ & $-0.330 \pm 0.003$ & $-0.330 \pm 0.002$ \\
1090	L1  & $0.539 \pm 0.023$ & $0.625 \pm 0.017$ & $0.429 \pm 0.034$ & $0.447 \pm 0.013$ \\
1091	L2  & $0.517 \pm 0.047$ & $0.622 \pm 0.010$ & $0.458 \pm 0.023$ & $0.522 \pm 0.014$ \\
1092	L3  & $0.448 \pm 0.216$ & $0.624 \pm 0.014$ & $0.498 \pm 0.036$ & $0.579 \pm 0.011$ \\
1093	L4  & $0.496 \pm 0.057$ & $0.628 \pm 0.014$ & $0.572 \pm 0.021$ & $0.592 \pm 0.009$ \\
1094	L5  & $0.475 \pm 0.101$ & $0.627 \pm 0.019$ & $0.573 \pm 0.020$ & $0.602 \pm 0.010$ \\
1095	L6  & $0.422 \pm 0.119$ & $0.631 \pm 0.012$ & $\mathbf{0.578 \pm 0.018}$ & $0.609 \pm 0.012$ \\
1096	L7  & $0.459 \pm 0.093$ & $0.632 \pm 0.012$ & $0.569 \pm 0.023$ & $0.616 \pm 0.014$ \\
1097	L8  & $0.347 \pm 0.283$ & $0.635 \pm 0.013$ & $0.560 \pm 0.025$ & $0.615 \pm 0.010$ \\
1098	L9  & $0.445 \pm 0.127$ & $\mathbf{0.637 \pm 0.008}$ & $0.564 \pm 0.021$ & $0.617 \pm 0.013$ \\
1099	L10 & $0.353 \pm 0.224$ & $0.624 \pm 0.014$ & $0.551 \pm 0.027$ & $0.625 \pm 0.007$ \\
1100	L11 & $0.356 \pm 0.122$ & $0.623 \pm 0.016$ & $0.561 \pm 0.025$ & $\mathbf{0.634 \pm 0.009}$ \\
1101	L12 & $0.409 \pm 0.203$ & $0.626 \pm 0.011$ & $0.557 \pm 0.026$ & $0.632 \pm 0.005$ \\
1102	L13 & $0.341 \pm 0.227$ & $0.624 \pm 0.013$ & $0.547 \pm 0.028$ & $0.633 \pm 0.008$ \\
1103	L14 & $0.374 \pm 0.211$ & $0.623 \pm 0.015$ & $0.550 \pm 0.023$ & $0.631 \pm 0.009$ \\
1104	L15 & $0.297 \pm 0.225$ & $0.619 \pm 0.012$ & $0.550 \pm 0.022$ & $0.633 \pm 0.010$ \\
1105	L16 & $0.323 \pm 0.226$ & $0.619 \pm 0.011$ & $0.534 \pm 0.018$ & $0.631 \pm 0.010$ \\
1106	L17 & $0.395 \pm 0.109$ & $0.609 \pm 0.023$ & $0.519 \pm 0.024$ & $0.633 \pm 0.007$ \\
1107	L18 & $0.214 \pm 0.307$ & $0.613 \pm 0.017$ & $0.502 \pm 0.047$ & $0.629 \pm 0.012$ \\
1108	L19 & $0.241 \pm 0.258$ & $0.613 \pm 0.013$ & $0.499 \pm 0.058$ & $0.627 \pm 0.008$ \\
1109	L20 & $
…[truncated 12767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 282 · 2026-05-26T12:30:12.339857+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1150",
  "limit": "65"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1150",
    "limit": "65"
  }
}
```

</details>

---

### Tool result

_source line 283 · 2026-05-26T12:30:12.741884+00:00_

1150	These concern auxiliary comparisons (encoder ranking, coefficient-of-variation ordering) rather than the core redistribution, probing, or counterfactual findings; no main-text conclusion requires revision.
1151	
1152	\subsection{Mechanistic Interpretation}
1153	\label{sec:mechanistic_interpretation}
1154	
1155	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed attention redistribution.
1156	Counterfactual perturbation produces large effects across all conditions ($d = 1.0$--$1.2$ on Goal; \S\ref{sec:openvla_routing}), with shuffled tokens exceeding paraphrased ($d = 1.096$ vs.\ $0.996$) despite identical token sets, indicating positional sensitivity.
1157	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \approx 0$; \S\ref{sec:action_trajectory}) reflects an information-computation dissociation~\cite{hewitt2019control}: instruction-dominant heads control direction rather than precision. Random ablation yields larger $R^2$ gains ($+0.071$ vs.\ $+0.030$; $z = -3.11$, $0$\textsuperscript{th} percentile), consistent with distinct $R^2$ signatures.
1158	
1159	\subsection{Functional Stages and Predictions}
1160	\label{sec:functional_stages}
1161	
1162	Per-layer profiles suggest three stages: redistribution (L0--L1; probe $99.6\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L31, ${\sim}56\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).
1163	Task-specific fine-tuning eliminates L31 re-engagement (18 $\to$ 0 heads; \S\ref{sec:openvla_routing}), consistent with exit-layer attention serving multi-task flexibility ($N{=}2$).
1164	TraceVLA~\cite{zheng2024tracevla} (Phi-3-V) shows consistent entry-exit attention concentration from an opposite starting point (\S\ref{sec:openvla_rout
…[truncated 6891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 284 · 2026-05-26T12:30:13.093675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "400",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "400",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 285 · 2026-05-26T12:30:13.345632+00:00_

400	To assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\times$ 50 demonstrations each, requiring spatial reasoning).
401	Figure~\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.
402	
403	The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
404	Training produces a significant geometric gain (best-vs-best $\Delta = +0.023$, 95\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\Delta = +0.017$, CI includes zero).
405	
406	Two notable differences are observed.
407	First, the absolute RSA values are higher on Spatial ($0.691$ vs.\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.
408	Second, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\Delta_\text{layer}| = 1$).
409	This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
410	
411	\begin{figure}[t]
412	\centering
413	\includegraphics[width=\columnwidth]{figures/fig7.pdf}
414	\caption{Cross-suite validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\ LIBERO-Spatial (right). The inverted-U replicates across suites. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}
415	\label{fig:cross_benchmark}
416	\end{figure}
417	
418	\subsubsection{Cross-Suite Counterfactual Replication}
419	\label{sec:spatial
…[truncated 3234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 286 · 2026-05-26T12:32:58.564316+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "## 审查报告 — 17 Negative 逐条审查 + 论文 Story 最终审视\n\n---\n\n# Part 1: 17 个 Negative 逐条审查\n\n按实验关联性分五组。\n\n## 组 A：Pre-pivot 时间距离方向（5 个）— 无重试价值\n\n| ID | Hypothesis | 失败原因 | 重试？ |\n|----|-----------|---------|-------|\n| `mvp_001` | 隐状态编码 temporal distance，信号来自训练 | Δρ(trained-untrained)=0.043，远低于门槛 0.10 | 否——方向已放弃 |\n| `mvp_probe_trained` | Trained model per-task ρ>0.5, Δρ>0.1 | Gate 2 FAIL，同上 | 否 |\n| `lg_gc_untrained` | 未训练 VLA goal classification 应显著低于训练 | 未训练 VLA 从 L1 起就 100%，probe 在 4096-D 上 trivially separates 10 classes | 否——ceiling effect 是设计问题 |\n| `lg_pca1024_linear_pertimestep` | 训练 VLA 在 t=0 bin 应比未训练高>15pp | 两者均 100%，Δ=-0.0008 | 否——同上 ceiling |\n| `lg_rsa_analysis` | RSA Δρ(trained-untrained)>0.08 | Δρ=0.003，但 trained>DINO +0.10 | 否——RSA 数据已部分用于附录 |\n\n**判断**：这 5 个 negative 驱动了从 \"temporal distance\" 到 \"instruction routing\" 的 pivot。Pivot 有数据支撑。无重试需要。\n\n## 组 B：Closed-loop 失败（3 个）— 无重试价值\n\n| ID | Hypothesis | 失败原因 |\n|----|-----------|---------|\n| `behavioral_smoketest` | 细调 OpenVLA 能在 closed-loop 执行任务 | SR=0/3 |\n| `closedloop_diagnosis` | 修 pipeline bug 后 SR>0 | 修 6 个 bug 后仍 SR=0/9 |\n| `official_checkpoint_sr_test` | 官方 checkpoint SR>0 | SR=0/15，已知复现性问题 |\n\n**判断**：Closed-loop 路径已正式关闭（D078）。附录已报告此 negative（\"Closed-loop evaluation attempt\" 段落）。这些 negative 实际上**为论文开放循环方法提供了 motivation**——已合理利用。不需重试。\n\n## 组 C：Ablation 特异性实验（5 个）— 含重要信息性 negative\n\n| ID | Hypothesis | 结果 | 论文中处理 |\n|----|-----------|------|----------|\n| `phi3v_attention_untrained` | 基座 Phi-3 不应有 L1 指令路由 | **28/32 heads 已指令主导** | ✅ 直接支撑 Finding 3（L1 inherited） |\n| `groundtruth_action_error` | Ablate 指令头应增加 GT error | ΔMSE=-0.001, n.s. | ✅ 已在论文中：\"direction not precision\" |\n| `action_trajectory_control` | 8 non-instruction heads d << 24 instruction heads d | 控制 d=0.41 vs 指令 d=0.65 | ✅ 附录 mechanistic interpretation |\n| `specificity_control_action` | Bottom-24 d 应远低于 Top-24 d | Bottom-24 d=0.565 vs Top-24 d=0.65 (ratio 1.15) | ⚠️ 附录有但主文未显式提及 |\n| `cross_layer_L8/L13_ablation` (2个) | L8/L13 d 应远低于 L1 d | 均 d≈0.65，cross-layer gradient 未确认 | 标注 \"Not for paper\"，设计问题（partial vs full knockout 不可比） |\n\n**关键发现**：`specificity_control_action` 是最重要的信息性 negative——ablating bottom-24 non-instruction heads（d=0.565）与 top-24 instruction heads（d=0.65）效果接近（ratio 仅 1.15x）。这意味着**\"指令主导\"分类在功能层面的特异性有限**。论文在附录用 \"distributed attention redistribution\" 和 \"direction vs precision\" 处理了这一点，但主文 §4.6 Synthesis 未显式提及。\n\n[severity: warning] 建议在 §4.6 或 Discussion 加一句：\"Matched-size ablation in OpenVLA reveals distributed rather than head-specific causal contribution (Appendix~\\ref{sec:mechanistic_interpretation}), indicating that L1 classification identifies attention concentration rather than functional exclusivity.\" 这预防审稿人攻击 \"instruction-dominant\" 分类的功能意义。\n\n## 组 D：Weight 分析 / 指令消融 RSA（2 个）— 已利用或不相关\n\n| ID | Hypothesis | 结果 |\n|----|-----------|------|\n| `d021_output_head_analysis` | Output head weight 变化 >> LLM 平均 (>3x) | Ratio 仅 1.12x，weight diff 均匀分布 |\n| `d021_instruction_ablation` | 移除指令应显著降低 RSA | Δ=0.0044（阈值 0.10），RSA 是视觉驱动的 |\n\n**判断**：`d021_output_head_analysis` 来自 pre-pivot 方向。`d021_instruction_ablation` 是有趣的——RSA 不受指令影响说明 RSA 捕获的是视觉几何结构，而 probe 捕获的是指令上下文信息。这与论文在附录中 \"RSA 和 CKA 可以在同一数据上 diverge\" 的讨论一致，但没有显式连接到指令消融。低优先级，不需要改。\n\n---\n\n## GPU 最终答案\n\n**17 个 negative 中无一值得用 idle GPU 重做。** 理由：\n- 5 个来自已放弃方向\n- 3 个是硬件/复现性问题\n- 7 个设计层面的 negative（ceiling、comparable effect sizes、methodological incomparability），重跑不会改变结论\n- 2 个 cross-layer ablation 需要根本性方法重设计（控制 head 数量），但这对论文核心 claim 不必要\n\n---\n\n# Part 2: 论文 Story 最终审视\n\n## Claim 链完整性追踪\n\n### Abstract → Intro → Method → Experiments → Discussion\n\n**叙事核心**：\"VLM→VLA 微调产生 exit collapse（训练相关），L1 注意力是继承的（非训练产物），两者构成指令路由的双重分解。\"\n\n| 节点 | Claim | 证据 | 强度匹配？ |\n|------|-------|------|-----------|\n| Abstract: \"consistent exit-layer collapse\" | ΔR²=0.16-0.46 across 6 VLM→VLA cells | 6/6 cells >0.10, permutation p=0.008 | ✅ 匹配 |\n| Abstract: \"absent in VLA-to-VLA\" | 4 OpenVLA cells ΔR²=0.033-0.086 | All <0.10, CIs span zero | ✅ 匹配 |\n| Abstract: \"NLP controls\" | 3 models ΔR²=0.000 | Clean, all flat profiles | ✅ 匹配 |\n| Abstract: \"substantial sensitivity to instruction content\" | d=0.45-1.52 across 8 cells | All >0.45, graded by semantic distance | ✅ 匹配 |\n| Abstract: \"attention patterns...largely pre-exist\" | \"largely\" = TracVLA 32→27-30, NORA 14→12-13 | Reference near-saturation, training ≤ or ↓ | ✅ \"largely\" 措辞准确 |\n| Intro contribution 1: \"cross-architecture\" | 3 architectures × 4 suites, 10/12 filled | ✅ |\n| Intro contribution 2: \"ΔR² exit collapse associated with VLM→VLA\" | Same as above | ✅ |\n| Intro contribution 3: \"decomposition...training-associated vs inherited\" | L1=inherited + exit collapse=training | ✅ 但 \"decomposition\" 暗示穷举性 |\n\n### Claim 强度问题\n\n**1. [severity: info] Title 与核心发现的对齐**\n\n标题 \"Instruction Routing\" 暗示论文主要研究指令信息如何在模型中路由。实际上：\n- 最强发现（exit collapse）是关于 **action-probe decodability**，不直接测量指令路由\n- L1 分析（真正关于指令路由）的结论是它是**继承的**\n- 反事实扰动测量**行为敏感性**，非路由机制\n\n标题并不 misleading——\"instruction routing\" 在可解释性文献中宽泛使用——但审稿人可能期望更多 mechanistic routing 分析（如 causal tracing 或 information flow）。**不建议改标题**（DDL 前风险太大），但建议准备 rebuttal 段落解释 \"routing\" 的操作性定义。\n\n**2. [severity: info] Contribution 3 \"decomposition\" 的穷举性**\n\n\"A decomposition of VLA instruction routing into training-associated effects and inherited base-model priors\" 暗示这是完整分解。实际上只覆盖三个维度（probe decodability、L1 attention、counterfactual sensitivity），不覆盖 mid-layer routing、cross-layer information flow 等。论文在 §4.6 Synthesis 用 \"these probes measure decodability, not causal reliance\" 适当限定了。措辞可接受，不需改。\n\n**3. [severity: info] §4.5 bold summary 强度**\n\n> \"L1 instruction routing is an inherited backbone property, not a consequence of VLA training.\"\n\n这是论文中最强的因果措辞之一。证据：2 个 VLM reference 已饱和/近饱和，训练未增加。但 OpenVLA random-weight control（0/32 heads）到 trained（24/32）说明训练**可以**创建 L1 routing from scratch。当前措辞正确（指已有预训练 backbone 的场景），但一个 careful reviewer 可能问 \"isn't it both?\" 实际上论文正文已处理此 nuance（§4.5 倒数第二句），但 bold summary 可能被孤立引用。低风险。\n\n### 107 实验数据利用率\n\n107 success 实验充分分布在：\n- 10 cells × 3 analyses（probe, counterfactual, L1）= 30 核心分析\n- OpenVLA deep-dive（RSA, CKA, dose-response, cross-instruction, external baselines）≈ 20+\n- Cross-suite replication（Spatial: RSA, probe, counterfactual, cross-instruction）≈ 10\n- Robustness（metric invariance, threshold sensitivity, demo-split, seed）≈ 10\n- Controls（NLP×3, label permutation, TOST, Bonferroni）≈ 10\n- Additional supplements（training dynamics, convergent evidence, power analysis）≈ 10\n\n**未发现有遗漏的数据点能显著加强叙事。** 数据利用率高。\n\n### Negative 结果在 Discussion/Limitation 中的讨论\n\n| Negative 主题 | 讨论位置 | 充分度 |\n|-------------|---------|-------|\n| Closed-loop SR=0 | 附录 \"Closed-loop evaluation attempt\" | ✅ |\n| N=2 VLM→VLA | 主文 discussion line 7 | ✅ |\n| 行为相关性 underpowered | 主文 + 附录 power analysis | ✅ 详尽 |\n| 开放循环 | 主文 + 附录 extended limitations | ✅ |\n| 特异性控制 negative | 附录 mechanistic interpretation | ⚠️ 见上方 warning |\n| 单 checkpoint | 附录 extended limitations | ✅ |\n\n### 逻辑流断裂检查\n\n**Intro → Method**: 问题（什么是训练产物/什么是继承？）→ 三个分析方法。✅ 无断裂。\n\n**Method → Experiments**: 方法定义 → 按分析维度报告结果。✅ 无断裂。\n\n**Experiments → Discussion**: §4.6 Synthesis 将三个发现整合 → Discussion 总结 + 限制。✅ 无断裂。\n\n**唯一微弱断点**: §4.2 OpenVLA deep-dive（动机：\"before testing cross-architectural generality\"）的 dose-response ablation 发现（d=0.48-0.64）在跨架构部分没有对应实验（TracVLA/NORA 没做 ablation）。这意味着 ablation 证据仅来自单一架构，而论文标题声称 \"cross-architecture analysis\"。论文在附录 convergent evidence 表中注明 \"Single architecture (OpenVLA); contribution ≠ necessity\"，处理得当。\n\n---\n\n## 总结\n\n**结论**: 论文 story 连贯，claim-evidence alignment 总体良好，17 个 negative 无需重试。\n\n**唯一 actionable warning**: 在主文中加一句关于 L1 ablation specificity 未确认的说明（预防审稿人攻击），建议位置在 §4.6 Synthesis 或 Discussion。\n\n**其他均为 info 级别**，供 rebuttal 准备参考。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "## 审查报告 — 17 Negative 逐条审查 + 论文 Story 最终审视\n\n---\n\n# Part 1: 17 个 Negative 逐条审查\n\n按实验关联性分五组。\n\n## 组 A：Pre-pivot 时间距离方向（5 个）— 无重试价值\n\n| ID | Hypothesis | 失败原因 | 重试？ |\n|----|-----------|---------|-------|\n| `mvp_001` | 隐状态编码 temporal distance，信号来自训练 | Δρ(trained-untrained)=0.043，远低于门槛 0.10 | 否——方向已放弃 |\n| `mvp_probe_trained` | Trained model per-task ρ>0.5, Δρ>0.1 | Gate 2 FAIL，同上 | 否 |\n| `lg_gc_untrained` | 未训练 VLA goal classification 应显著低于训练 | 未训练 VLA 从 L1 起就 100%，probe 在 4096-D 上 trivially separates 10 classes | 否——ceiling effect 是设计问题 |\n| `lg_pca1024_linear_pertimestep` | 训练 VLA 在 t=0 bin 应比未训练高>15pp | 两者均 100%，Δ=-0.0008 | 否——同上 ceiling |\n| `lg_rsa_analysis` | RSA Δρ(trained-untrained)>0.08 | Δρ=0.003，但 trained>DINO +0.10 | 否——RSA 数据已部分用于附录 |\n\n**判断**：这 5 个 negative 驱动了从 \"temporal distance\" 到 \"instruction routing\" 的 pivot。Pivot 有数据支撑。无重试需要。\n\n## 组 B：Closed-loop 失败（3 个）— 无重试价值\n\n| ID | Hypothesis | 失败原因 |\n|----|-----------|---------|\n| `behavioral_smoketest` | 细调 OpenVLA 能在 closed-loop 执行任务 | SR=0/3 |\n| `closedloop_diagnosis` | 修 pipeline bug 后 SR>0 | 修 6 个 bug 后仍 SR=0/9 |\n| `official_checkpoint_sr_test` | 官方 checkpoint SR>0 | SR=0/15，已知复现性问题 |\n\n**判断**：Closed-loop 路径已正式关闭（D078）。附录已报告此 negative（\"Closed-loop evaluation attempt\" 段落）。这些 negative 实际上**为论文开放循环方法提供了 motivation**——已合理利用。不需重试。\n\n## 组 C：Ablation 特异性实验（5 个）— 含重要信息性 negative\n\n| ID | Hypothesis | 结果 | 论文中处理 |\n|----|-----------|------|----------|\n| `phi3v_attention_untrained` | 基座 Phi-3 不应有 L1 指令路由 | **28/32 heads 已指令主导** | ✅ 直接支撑 Finding 3（L1 inherited） |\n| `groundtruth_action_error` | Ablate 指令头应增加 GT error | ΔMSE=-0.001, n.s. | ✅ 已在论文中：\"direction not precision\" |\n| `action_trajectory_control` | 8 non-instruction heads d << 24 instruction heads d | 控制 d=0.41 vs 指令 d=0.65 | ✅ 附录 mechanistic interpretation |\n| `specificity_control_action` | Bottom-24 d 应远低于 Top-24 d | Bottom-24 d=0.565 vs Top-24 d=0.65 (ratio 1.15) | ⚠️ 附录有但主文未显式提及 |\n| `cross_layer_L8/L13_ablation` (2个) | L8/L13 d 应远低于 L1 d | 均 d≈0.65，cross-layer gradient 未确认 | 标注 \"Not for paper\"，设计问题（partial vs full knockout 不可比） |\n\n**关键发现**：`specificity_control_action` 是最重要的信息性 negative——ablating bottom-24 non-instruction heads（d=0.565）与 top-24 instruction heads（d=0.65）效果接近（ratio 仅 1.15x）。这意味着**\"指令主导\"分类在功能层面的特异性有限**。论文在附录用 \"distributed attention redistribution\" 和 \"direction vs precision\" 处理了这一点，但主文 §4.6 Synthesis 未显式提及。\n\n[severity: warning] 建议在 §4.6 或 Discussion 加一句：\"Matched-size ablation in OpenVLA reveals distributed rather than head-specific causal contribution (Appendix~\\ref{sec:mechanistic_interpretation}), indicating that L1 classification identifies attention concentration rather than functional exclusivity.\" 这预防审稿人攻击 \"instruction-dominant\" 分类的功能意义。\n\n## 组 D：Weight 分析 / 指令消融 RSA（2 个）— 已利用或不相关\n\n| ID | Hypothesis | 结果 |\n|----|-----------|------|\n| `d021_output_head_analysis` | Output head weight 变化 >> LLM 平均 (>3x) | Ratio 仅 1.12x，weight diff 均匀分布 |\n| `d021_instruction_ablation` | 移除指令应显著降低 RSA | Δ=0.0044（阈值 0.10），RSA 是视觉驱动的 |\n\n**判断**：`d021_output_head_analysis` 来自 pre-pivot 方向。`d021_instruction_ablation` 是有趣的——RSA 不受指令影响说明 RSA 捕获的是视觉几何结构，而 probe 捕获的是指令上下文信息。这与论文在附录中 \"RSA 和 CKA 可以在同一数据上 diverge\" 的讨论一致，但没有显式连接到指令消融。低优先级，不需要改。\n\n---\n\n## GPU 最终答案\n\n**17 个 negative 中无一值得用 idle GPU 重做。** 理由：\n- 5 个来自已放弃方向\n- 3 个是硬件/复现性问题\n- 7 个设计层面的 negative（ceiling、comparable effect sizes、methodological incomparability），重跑不会改变结论\n- 2 个 cross-layer ablation 需要根本性方法重设计（控制 head 数量），但这对论文核心 claim 不必要\n\n---\n\n# Part 2: 论文 Story 最终审视\n\n## Claim 链完整性追踪\n\n### Abstract → Intro → Method → Experiments → Discussion\n\n**叙事核心**：\"VLM→VLA 微调产生 exit collapse（训练相关），L1 注意力是继承的（非训练产物），两者构成指令路由的双重分解。\"\n\n| 节点 | Claim | 证据 | 强度匹配？ |\n|------|-------|------|-----------|\n| Abstract: \"consistent exit-layer collapse\" | ΔR²=0.16-0.46 across 6 VLM→VLA cells | 6/6 cells >0.10, permutation p=0.008 | ✅ 匹配 |\n| Abstract: \"absent in VLA-to-VLA\" | 4 OpenVLA cells ΔR²=0.033-0.086 | All <0.10, CIs span zero | ✅ 匹配 |\n| Abstract: \"NLP controls\" | 3 models ΔR²=0.000 | Clean, all flat profiles | ✅ 匹配 |\n| Abstract: \"substantial sensitivity to instruction content\" | d=0.45-1.52 across 8 cells | All >0.45, graded by semantic distance | ✅ 匹配 |\n| Abstract: \"attention patterns...largely pre-exist\" | \"largely\" = TracVLA 32→27-30, NORA 14→12-13 | Reference near-saturation, training ≤ or ↓ | ✅ \"largely\" 措辞准确 |\n| Intro contribution 1: \"cross-architecture\" | 3 architectures × 4 suites, 10/12 filled | ✅ |\n| Intro contribution 2: \"ΔR² exit collapse associated with VLM→VLA\" | Same as above | ✅ |\n| Intro contribution 3: \"decomposition...training-associated vs inherited\" | L1=inherited + exit collapse=training | ✅ 但 \"decomposition\" 暗示穷举性 |\n\n### Claim 强度问题\n\n**1. [severity: info] Title 与核心发现的对齐**\n\n标题 \"Instruction Routing\" 暗示论文主要研究指令信息如何在模型中路由。实际上：\n- 最强发现（exit collapse）是关于 **action-probe decodability**，不直接测量指令路由\n- L1 分析（真正关于指令路由）的结论是它是**继承的**\n- 反事实扰动测量**行为敏感性**，非路由机制\n\n标题并不 misleading——\"instruction routing\" 在可解释性文献中宽泛使用——但审稿人可能期望更多 mechanistic routing 分析（如 causal tracing 或 information flow）。**不建议改标题**（DDL 前风险太大），但建议准备 rebuttal 段落解释 \"routing\" 的操作性定义。\n\n**2. [severity: info] Contribution 3 \"decomposition\" 的穷举性**\n\n\"A decomposition of VLA instruction routing into training-associated effects and inherited base-model priors\" 暗示这是完整分解。实际上只覆盖三个维度（probe decodability、L1 attention、counterfactual sensitivity），不覆盖 mid-layer routing、cross-layer information flow 等。论文在 §4.6 Synthesis 用 \"these probes measure decodability, not causal reliance\" 适当限定了。措辞可接受，不需改。\n\n**3. [severity: info] §4.5 bold summary 强度**\n\n> \"L1 instruction routing is an inherited backbone property, not a consequence of VLA training.\"\n\n这是论文中最强的因果措辞之一。证据：2 个 VLM reference 已饱和/近饱和，训练未增加。但 OpenVLA random-weight control（0/32 heads）到 trained（24/32）说明训练**可以**创建 L1 routing from scratch。当前措辞正确（指已有预训练 backbone 的场景），但一个 careful reviewer 可能问 \"isn't it both?\" 实际上论文正文已处理此 nuance（§4.5 倒数第二句），但 bold summary 可能被孤立引用。低风险。\n\n### 107 实验数据利用率\n\n107 success 实验充分分布在：\n- 10 cells × 3 analyses（probe, counterfactual, L1）= 30 核心分析\n- OpenVLA deep-dive（RSA, CKA, dose-response, cross-instruction, external baselines）≈ 20+\n- Cross-suite replication（Spatial: RSA, probe, counterfactual, cross-instruction）≈ 10\n- Robustness（metric invariance, threshold sensitivity, demo-split, seed）≈ 10\n- Controls（NLP×3, label permutation, TOST, Bonferroni）≈ 10\n- Additional supplements（training dynamics, convergent evidence, power analysis）≈ 10\n\n**未发现有遗漏的数据点能显著加强叙事。** 数据利用率高。\n\n### Negative 结果在 Discussion/Limitation 中的讨论\n\n| Negative 主题 | 讨论位置 | 充分度 |\n|-------------|---------|-------|\n| Closed-loop SR=0 | 附录 \"Closed-loop evaluation attempt\" | ✅ |\n| N=2 VLM→VLA | 主文 discussion line 7 | ✅ |\n| 行为相关性 underpowered | 主文 + 附录 power analysis | ✅ 详尽 |\n| 开放循环 | 主文 + 附录 extended limitations | ✅ |\n| 特异性控制 negative | 附录 mechanistic interpretation | ⚠️ 见上方 warning |\n| 单 checkpoint | 附录 extended limitations | ✅ |\n\n### 逻辑流断裂检查\n\n**Intro → Method**: 问题（什么是训练产物/什么是继承？）→ 三个分析方法。✅ 无断裂。\n\n**Method → Experiments**: 方法定义 → 按分析维度报告结果。✅ 无断裂。\n\n**Experiments → Discussion**: §4.6 Synthesis 将三个发现整合 → Discussion 总结 + 限制。✅ 无断裂。\n\n**唯一微弱断点**: §4.2 OpenVLA deep-dive（动机：\"before testing cross-architectural generality\"）的 dose-response ablation 发现（d=0.48-0.64）在跨架构部分没有对应实验（TracVLA/NORA 没做 ablation）。这意味着 ablation 证据仅来自单一架构，而论文标题声称 \"cross-architecture analysis\"。论文在附录 convergent evidence 表中注明 \"Single architecture (OpenVLA); contribution ≠ necessity\"，处理得当。\n\n---\n\n## 总结\n\n**结论**: 论文 story 连贯，claim-evidence alignment 总体良好，17 个 negative 无需重试。\n\n**唯一 actionable warning**: 在主文中加一句关于 L1 ablation specificity 未确认的说明（预防审稿人攻击），建议位置在 §4.6 Synthesis 或 Discussion。\n\n**其他均为 info 级别**，供 rebuttal 准备参考。",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 287 · 2026-05-26T12:33:02.850009+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 4285
}
```

</details>

---

### Assistant

_source line 288 · 2026-05-26T12:33:15.060159+00:00_

审查完成。核心结论：

1. **17 个 negative 无一值得重做** — 5 个来自已放弃方向，3 个是复现性硬限制，9 个是设计层面的 negative（重跑不改变结论）。

2. **论文 story 连贯**，claim-evidence alignment 总体良好。唯一 actionable warning：主文应补一句关于 L1 ablation 特异性未确认的说明（specificity_control_action 中 bottom-24 d=0.565 ≈ top-24 d=0.65），防止审稿人攻击 "instruction-dominant" 分类的功能意义。其余均为 info 级别。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---

## Round 8

8 recorded events

### User

_source line 289 · 2026-05-26T13:05:43.136905+00:00_

[系统通知 — roadmap_updated]:
[系统通知] ROADMAP.md 已更新（原因：论文 v14 终稿状态同步——全部改进完成，Reviewer 最终审查通过，等待用户提交），请审查研究方向和计划的合理性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "roadmap_updated"
}
```

</details>

---

### Tool call

_source line 290 · 2026-05-26T13:05:50.306108+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_roadmap",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_roadmap",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 291 · 2026-05-26T13:05:50.457071+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 292 · 2026-05-26T13:05:53.721332+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 293 · 2026-05-26T13:05:54.123386+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-26 13:05 UTC | 更新原因: 论文 v14 终稿状态同步——全部改进完成，Reviewer 最终审查通过，等待用户提交\\n\\n> 核心方向详见 paper_framing.md（D095→D105 修正链）\\n\\n## 核心方向\\nVLA 微调如何重组 instruction routing——跨架构 × 跨任务。R² exit collapse 在所有 VLM→VLA 转换一致出现 (6/6, Δ=0.156-0.455)，VLA→VLA 转换无实质性 collapse (0/4, Δ=0.033-0.086)。三个 NLP controls (Llama-2-chat + Phi-3-mini + Qwen2.5-3B-Instruct) 确认 VLA-specificity (均 Δ=0.000)，覆盖 3/3 backbone families。\\n\\n## 当前进展\\n- **阶段**: 论文 v14 终稿就绪，等待用户提交\\n- **实验**: 107 success / 17 negative / 7 failed / 154 total。Reviewer 逐条审查 17 negative，确认无需重试（D110）\\n- **统计加固**: seed robustness (4 seeds × 3 cells, std < 0.02)、bootstrap CI (MCCV 1000 iter)、permutation test (p=0.008)、post-hoc power analysis (power=0.37, n≥21)\\n- **Reviewer 内部评估**: CoRL 2026 中稿率 45-60% (MEDIUM-HIGH)\\n- **写作**: v14 — 全部 A-G 7 项 appendix 补强 + proofreading + notation 扫描 + §4.6 specificity caveat + camera-ready QA 全部完成\\n- **编译**: 0 error, 8 页正文, 42 页含 appendix\\n- **字体**: Type 3 文本字体全部清除，mathtext glyph 残留（CoRL 可接受），Worker 修复中\\n- **Abstract DDL (5/26)**: 已过，用户未确认提交状态（D109）\\n- **Paper DDL (5/29)**: 论文就绪，等待用户操作 OpenReview 提交\\n\\n## 近期任务\\n- [x] 全部实验完成（107 success）\\n- [x] NLP controls 3/3 覆盖\\n- [x] 论文 v14 终稿（A-G 补强 + proofreading + notation + QA）\\n- [x] Reviewer 17 negative 逐条审查（D110：无需重试）\\n- [x] Reviewer story 最终审视（claim-evidence alignment 良好）\\n- [x] Camera-ready 格式检查（CoRL 2026 模板合规）\\n- [x] §4.6 L1 ablation specificity caveat\\n- [x] Post-hoc power analysis + BayesianVLA 引用\\n- [ ] Type 3 mathtext 字体完全清除（Worker 进行中，非阻塞）\\n- [ ] 用户确认 abstract 提交状态\\n- [ ] 用户操作 Paper 提交 (DDL 5/29)\\n\\n## GPU 预算\\nwestd-19183: 2× RTX PRO 6000 — 释放请求已提交 Manager 5 次未回复。全部实验完成，Reviewer 确认无可行实验（D108, D110）。GPU 保留仅因 Manager 未批准释放。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D110 | 2026-05-26 | GPU 利用终结：
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-26T13:06:21.988486+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: info] ROADMAP 更新审查 — 无异常\n\nROADMAP 准确反映当前状态：\n\n- **实验完整性**：107 success / 17 negative / 7 failed，与 registry 一致。D110（17 negative 无需重试）是我的审查结论。\n- **论文状态**：v14 终稿就绪，与我 camera-ready QA + story 审视结论一致。\n- **近期任务**：全部已完成项与我核实一致。剩余 3 项（Type 3 字体、abstract 确认、paper 提交）均为非阻塞/用户操作。\n- **GPU**：全部实验完成，无可行追加实验，GPU 释放待 Manager 批准。合理。\n- **DDL 风险**：Paper DDL 5/29，论文已就绪，无算力-时间冲突。唯一风险是用户操作提交的时效性。\n\n**一处小差异**（非阻塞）：ROADMAP 写 \"42 页含 appendix\"，我上次 QA 时 main.log 显示 40 页（编译时间 2026-05-26 08:12）。可能是后续编译增加了内容。不影响合规性（CoRL 无 appendix 页数限制）。\n\n无需调整研究方向或计划。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: info] ROADMAP 更新审查 — 无异常\n\nROADMAP 准确反映当前状态：\n\n- **实验完整性**：107 success / 17 negative / 7 failed，与 registry 一致。D110（17 negative 无需重试）是我的审查结论。\n- **论文状态**：v14 终稿就绪，与我 camera-ready QA + story 审视结论一致。\n- **近期任务**：全部已完成项与我核实一致。剩余 3 项（Type 3 字体、abstract 确认、paper 提交）均为非阻塞/用户操作。\n- **GPU**：全部实验完成，无可行追加实验，GPU 释放待 Manager 批准。合理。\n- **DDL 风险**：Paper DDL 5/29，论文已就绪，无算力-时间冲突。唯一风险是用户操作提交的时效性。\n\n**一处小差异**（非阻塞）：ROADMAP 写 \"42 页含 appendix\"，我上次 QA 时 main.log 显示 40 页（编译时间 2026-05-26 08:12）。可能是后续编译增加了内容。不影响合规性（CoRL 无 appendix 页数限制）。\n\n无需调整研究方向或计划。",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-26T13:06:25.907009+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 3918
}
```

</details>

---

### Assistant

_source line 296 · 2026-05-26T13:06:28.851594+00:00_

ROADMAP 审查完成，无异常。项目处于提交就绪状态，等待用户操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---

## Round 9

2 recorded events

### User

_source line 297 · 2026-05-26T16:52:39.117586+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 298 · 2026-05-26T16:53:29.742052+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-19183 上 cuda:0 和 cuda:1（2× RTX PRO 6000 96GB）。项目已无实验可跑，GPU 释放请求已提 Manager 5 次未回复。
- 论文处于 anonymous submission 模式（`\author{Anonymous}`，无 `[final]` flag）。任何修改不得引入 identifying information。
- Paper DDL 2026-05-29，用户需自行操作 OpenReview 提交。Reviewer 不执行实验、不修改文件、不提交。
- 17 个 negative 结果经 D110 决策终结——不再重试任何一个。

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，代码根目录 `/root/vla-ssd`，数据盘 `/root/autodl-tmp/vla-ssd/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型 checkpoints：`/root/autodl-tmp/vla-ssd/checkpoints/`（openvla-7b, tracvla, nora 等）
- 数据集：`/root/autodl-tmp/vla-ssd/data/libero/`（4 suites × 10 tasks × 50 demos）
- 实验结果：`/root/autodl-tmp/vla-ssd/results/`
- 本地论文：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/`
- 活跃进程：无。全部实验已完成（107 success / 17 negative / 7 failed）。无 tmux session / cron。

### 3. 📊 当前状态
**刚完成**：
1. 17 个 negative 逐条审查（结论：无一值得重试）→ posted D110
2. 论文 story 最终审视（claim-evidence alignment 良好，1 个 warning：§4.6 specificity caveat 建议加一句）
3. Camera-ready QA（CoRL 2026 格式合规，2 个 non-blocking warning：appendix overfull hbox + 参考文献格式不统一）
4. ROADMAP 更新审查（与审查结论一致，无异常）

**Registry 状态**：全部 DONE，无 RUNNING/PREPARING。

**等待中**：
- 用户确认 abstract 提交状态（DDL 5/26 已过）
- 用户操作 paper 提交（DDL 5/29）
- Type 3 mathtext 字体清除（Worker 进行中，非阻塞）
- Manager 批准 GPU 释放

### 4. 📋 待办（条件触发式）
- Director 转发章节修改审查请求 → 模式 B 对抗审查（先读 paper-quality-lessons skill）
- Director 转发 Framing 调整提案 → 读 negative-framing-review skill，四维度审查
- 论文被 rebuttal → 读 rebuttal skill，对照 `artifacts/anticipated_rebuttal_v2.md`（9 个预期问题已准备好）
- Worker 报告 Type 3 字体修复完成 → 验证 `pdffonts main.pdf` 无 Type 3 残留
- ROADMAP 再次更新 → 快速一致性检查（当前状态 = 等待提交，无实验变动）

### 5. 🎯 战略上下文
**核心结论**：VLM→VLA 微调产生 exit collapse（ΔR²=0.16-0.46），VLA→VLA 不产生（<0.10），NLP controls 确认 VLA-specificity（0.000）。L1 instruction attention 是继承的，非训练产物。三个分析方法（probe + counterfactual + L1 profiling）构成跨架构分解。

**关键决策链**：D101（Weak Reject 4.5/10 → 统计框架重构）→ D102（转 effect size threshold）→ D103（framing 路径）→ D105（Qwen NLP control 闭合 limitation）→ D107（n=9 硬约束终结）→ D110（17 negative 终结，GPU 释放）

**易错点**：
- **n=9 behavioral correlation（ρ=0.583, p=0.10）是设计硬约束**，不可通过 sub-split/bootstrap/augmentation 扩展。D107 已终结讨论。别再试。
- **L1 "instruction-dominant" 分类是 attention-based，不是 functional-specificity**。specificity_control_action 显示 ablating non-instruction heads 产生类似 d 值（0.565 vs 0.65）。论文用 "distributed redistribution" 处理。审稿人可能攻击这个点——准备好 rebuttal。
- **OpenVLA reference 是 VLA（OXE-pretrained），不是 VLM**。TracVLA/NORA reference 才是 VLM。这个不对称是论文的核心设计，不是 bug。
- **counterfactual sensitivity 跨 metric 不可比**：Cohen's d（OpenVLA/TracVLA）vs cosine distance（NORA/reference VLMs），论文已反复强调。
- **页数**：ROADMAP 写 42 页，main.log 编译显示 40 页。可能编译版本差异，不影响合规。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---
