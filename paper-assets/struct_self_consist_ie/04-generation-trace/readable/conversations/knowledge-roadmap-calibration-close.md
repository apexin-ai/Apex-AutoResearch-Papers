# knowledge roadmap calibration close

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_knowledge_roadmap-calibration-close_20260519T220853.jsonl`
- **Structured JSON:** [`faf06ef773e6995be395.json`](../../sessions/fa/faf06ef773e6995be395.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-19T22:09:36.431724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T22:09:36.432076+00:00_

1	# struct_self_consist_ie — Research Dashboard
2	
3	> 最后更新: 2026-05-19 20:45 UTC | 更新原因: 全部 4 实验 ETA 大幅修正（延后 6-13h）
4	
5	## 核心方向
6	Self-consistency for NER: diagnosing correlation-selection gap + entity-level construction as resolution. 详见 paper_framing.md。
7	
8	## 当前阶段
9	**Scale Upgrade + Paper Finalization**。DDL: EMNLP 2026 ARR May (2026-05-25, ~6 天)。
10	
11	Round 24 审稿: borderline (3.25/5)。冲 Main Conference 4.0。
12	
13	## 数值审计状态 — 全部关闭 ✅
14	
15	- [x] appendix L231: FewNERD degen 12.7%→13.0%, diff +10.7pp→+10.4pp
16	- [x] appendix L360/L363-365/L687 数值修正 (3-seed mean)
17	- [x] Table 5 degen 同步修正 (CoNLL 61.7%, FewNERD 13.0%)
18	- [x] Scaling script 8B FT 12处数据修正 + 2处 degen 同步
19	- [x] CoNLL oracle/headroom 全局修正: .957→.948, ≈5pp→≈4pp (appendix L248, experiments L102, appendix L932)
20	- [ ] tab:calibration caption 待 Director 决策（已发现 N=16 非 N=8、非 gold-filtered、单 seed 问题，等 Director 选方案）
21	
22	## RUNNING 实验（4 个，12/12 GPU 满载）
23	
24	### Server A (autodl-5090, 4 GPU): exp_qwen25_32b_fewnerd
25	- QLoRA 训练中，PID 804438, 29.1% (12000/41180)
26	- ETA ~05-20 23:15 UTC（**最慢瓶颈，+13h 延后**）
27	- 完成后: export → 3-seed N=8 inference → signals → construction (~4-6h)
28	
29	### Server B (autodl-5090-b, 4 GPU): exp_qwen25_72b_fewshot
30	- 72B AWQ 3-shot 推理，PID 131293, SciERC done / CoNLL 56% / FewNERD 未开始
31	- ETA ~05-20 06:00+ UTC（**+6h 延后**）
32	- 完成后: signal computation + construction pipeline
33	
34	### Server C (autodl-5090-c, 4 GPU):
35	- **exp_qwen25_14b_fewnerd** (cuda:0,1) — QLoRA 训练中，PID 56773, 42.5% (17500/41180)
36	  - ETA ~05-20 13:45 UTC（**+11h 延后**）
37	  - 完成后: export → 3-seed N=8 inference → signals → construction (~4h)
38	- **exp_qwen25_7b_fewnerd** (cuda:2,3) — 全自动 pipeline，PID 71837, 训练 63% (13016/20590)
39	  - ETA ~05-20 04:00 UTC（**+8h 延后，仍最先完成**）
40	  - Pipeline 自动执行: train → export → 3-seed inference → signals → construction
41	
42	### 完成时间线（更新 05-19 20:45 UTC）
43	1. **~05-20 04:00 UTC**: 7B pipeline 完成 → scaling curve 最小点（+8h）
44	2. **~05-20 06:00+ UTC**: 72B few-
…[truncated 3677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T22:09:36.432338+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md",
  "old_string": "- [ ] tab:calibration caption 待 Director 决策（已发现 N=16 非 N=8、非 gold-filtered、单 seed 问题，等 Director 选方案）",
  "new_string": "- [x] tab:calibration caption 修复（N=8/16 分标、non-gold-filtered 说明、single seed 标注）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md",
    "old_string": "- [ ] tab:calibration caption 待 Director 决策（已发现 N=16 非 N=8、非 gold-filtered、单 seed 问题，等 Director 选方案）",
    "new_string": "- [x] tab:calibration caption 修复（N=8/16 分标、non-gold-filtered 说明、single seed 标注）"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T22:09:36.432513+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T22:09:36.432649+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md",
  "old_string": "- [ ] tab:calibration caption/重跑（待 Director 决策）",
  "new_string": "- [x] tab:calibration caption 修复完成（Reviewer PASS）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md",
    "old_string": "- [ ] tab:calibration caption/重跑（待 Director 决策）",
    "new_string": "- [x] tab:calibration caption 修复完成（Reviewer PASS）"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T22:09:36.432812+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T22:09:36.432942+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md",
  "old_string": "> 最后更新: 2026-05-19 20:45 UTC | 更新原因: 全部 4 实验 ETA 大幅修正（延后 6-13h）",
  "new_string": "> 最后更新: 2026-05-19 21:30 UTC | 更新原因: tab:calibration 已修复关闭 + 数值审计全部完成"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md",
    "old_string": "> 最后更新: 2026-05-19 20:45 UTC | 更新原因: 全部 4 实验 ETA 大幅修正（延后 6-13h）",
    "new_string": "> 最后更新: 2026-05-19 21:30 UTC | 更新原因: tab:calibration 已修复关闭 + 数值审计全部完成"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T22:09:36.433097+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T22:09:36.433265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md",
  "limit": "85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md",
    "limit": "85"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T22:09:36.433421+00:00_

1	# struct_self_consist_ie — Research Dashboard
2	
3	> 最后更新: 2026-05-19 21:30 UTC | 更新原因: tab:calibration 已修复关闭 + 数值审计全部完成
4	
5	## 核心方向
6	Self-consistency for NER: diagnosing correlation-selection gap + entity-level construction as resolution. 详见 paper_framing.md。
7	
8	## 当前阶段
9	**Scale Upgrade + Paper Finalization**。DDL: EMNLP 2026 ARR May (2026-05-25, ~6 天)。
10	
11	Round 24 审稿: borderline (3.25/5)。冲 Main Conference 4.0。
12	
13	## 数值审计状态 — 全部关闭 ✅
14	
15	- [x] appendix L231: FewNERD degen 12.7%→13.0%, diff +10.7pp→+10.4pp
16	- [x] appendix L360/L363-365/L687 数值修正 (3-seed mean)
17	- [x] Table 5 degen 同步修正 (CoNLL 61.7%, FewNERD 13.0%)
18	- [x] Scaling script 8B FT 12处数据修正 + 2处 degen 同步
19	- [x] CoNLL oracle/headroom 全局修正: .957→.948, ≈5pp→≈4pp (appendix L248, experiments L102, appendix L932)
20	- [x] tab:calibration caption 修复（N=8/16 分标、non-gold-filtered 说明、single seed 标注）
21	
22	## RUNNING 实验（4 个，12/12 GPU 满载）
23	
24	### Server A (autodl-5090, 4 GPU): exp_qwen25_32b_fewnerd
25	- QLoRA 训练中，PID 804438, 29.1% (12000/41180)
26	- ETA ~05-20 23:15 UTC（**最慢瓶颈，+13h 延后**）
27	- 完成后: export → 3-seed N=8 inference → signals → construction (~4-6h)
28	
29	### Server B (autodl-5090-b, 4 GPU): exp_qwen25_72b_fewshot
30	- 72B AWQ 3-shot 推理，PID 131293, SciERC done / CoNLL 56% / FewNERD 未开始
31	- ETA ~05-20 06:00+ UTC（**+6h 延后**）
32	- 完成后: signal computation + construction pipeline
33	
34	### Server C (autodl-5090-c, 4 GPU):
35	- **exp_qwen25_14b_fewnerd** (cuda:0,1) — QLoRA 训练中，PID 56773, 42.5% (17500/41180)
36	  - ETA ~05-20 13:45 UTC（**+11h 延后**）
37	  - 完成后: export → 3-seed N=8 inference → signals → construction (~4h)
38	- **exp_qwen25_7b_fewnerd** (cuda:2,3) — 全自动 pipeline，PID 71837, 训练 63% (13016/20590)
39	  - ETA ~05-20 04:00 UTC（**+8h 延后，仍最先完成**）
40	  - Pipeline 自动执行: train → export → 3-seed inference → signals → construction
41	
42	### 完成时间线（更新 05-19 20:45 UTC）
43	1. **~05-20 04:00 UTC**: 7B pipeline 完成 → scaling curve 最小点（+8h）
44	2. **~05-20 06:00+ UTC**: 72B few-shot 完成 → ZS vs
…[truncated 2030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T22:09:36.433610+00:00_

修改完成。审查结果：

**已更新 (2处)**：
- `数值审计状态` line 20: tab:calibration → `[x]`，现在该 section 6/6 全部关闭，与标题 "全部关闭 ✅" 一致
- `近期任务 Checklist` line 82: tab:calibration → `[x]`

**其他 checklist 项审查 — 无遗漏**：
- `论文修复状态` 3 项未完成 (lines 72-74) 均依赖正在运行的实验 (7B/14B/32B/72B-FS)，状态正确
- `近期任务 Checklist` 6 项未完成均依赖实验产出，状态正确
- Scaling section 没有独立的 "进行中" 标记需要加，因为它明确标注了依赖实验完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_knowledge_roadmap-calibration-close_20260519T220853"
}
```

</details>

---
