# cron hook eval acr object v4 obs only

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/cron_hook_eval-acr-object-v4-obs-only.jsonl`
- **Structured JSON:** [`d3fbaaebb54c43a58c20.json`](../../sessions/d3/d3fbaaebb54c43a58c20.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-16T00:43:19.863421+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #12。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**（17 张）：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5。白名单外的 GPU 严禁使用，即使 Director 指令也必须 push back。
- **submit_training_job 命令必须 bash -c 包裹**：`bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u ..."`。裸 `python` 会 EXIT_CODE=127。
- **exp_id 命名**：norm 值用 `p` 替代小数点（norm0p3 = 0.3），禁止 norm03 等歧义缩写。
- **Kill 操作**：必须 `ps aux | grep` 完整命令行逐参数比对，曾因 norm03/norm003 混淆 kill 错进程空转 9 小时。
- **Per-DOF conformal claim 已死**（D029-D030）——不要试图复活。obs_only CRM 是唯一存活路径。

### 2. 🖥️ 基础设施快照
- **服务器 / 工作目录**：全部 `/root/acr-vla-conformal-refinement`，account=root
  - bjb2-40593（1× 4090D）、bjb1-18228（4× 4090）、bjb1-32546（6× 4090）、bjb2-28827（6× 4090）
- **Python**：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型 checkpoints**：`/root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar_unc}/crm_best.pt`
- **数据集**：`/root/autodl-tmp/libero_data/`（spatial + object）
- **HF cache**：`/root/autodl-tmp/.hf_cache`（必须设 HF_HOME 指向此路径）
- **活跃进程**：16 个 RUNNING 实验，全部 cron 监控正常（reconcile_crons 刚确认全 alive）。分布见第 3 节。

### 3. 📊 当前状态
**Phase 3：Paper writing + seed=43 statistical validation。CoRL 2026 abstract DDL ~May 26（~10 天）。**

刚完成 session-start 初始化，16 个实验全部 alive，无需干预。Paper 正文 5 章全部完成（Intro/Method/Experiments/RelatedWork/Discussion-Conclusion），引用审计 PASSED。Figures 是论文最后短板（fig1 WIP，fig2/fig3 pending）。

**RUNNING 实验（16 个，3 类）：**

| 类别 | 数量 | 关键实验 | 进度 |
|------|------|----------|------|
| Seed=43 统计验证 | 5 | obs_only-seed43 6/10, perdof-seed43 5/10, scalar-seed43 3/10, vla-mean-seed43 3/10, obs-only-norm02-seed43-r2 1/10 | argmin-seed43 已 DONE |
| Object magnitude sweep | 8 | obs_only norm=0.03/0.05/0.3 + perdof norm=0.03/0.05/0.2/0.3 + perdof-norm02-seed43 | 均 0-2/10 tasks |
| Default norm ablation + spatial | 3 | obs-only-default 2/10, perdof-default-r2 1/10, spatial-norm003-b2 8/10 | |

**⚠️ 关键风险**：obs_only seed=43 partial SR = 8.3%（6/10 tasks），远低于 seed=42 的 19%。剩余 4 tasks 在 seed=42 中 SR 较高（bbq_sauce 30%, tomato_sauce 10% 等），可能回升。但若 10-task final 仍低，Fisher test 可能 fail。

**等待中**：eval-mag-obsonly-norm03-b2 在 PENDING 等人工审批。

### 4. 📋 待办（条件触发式）
- **eval-obs-only-object-seed43 完成 → 立即做 Fisher exact test**：combined 200 trials (seed42: 19/100 + seed43: ?/100) vs argmin combined。p<0.05 → 更新 paper claim + abstract；p=0.05-0.10 → 部署 seed=44 第三轮；p>0.10 → 调整 claim 为 "suggestive improvement"
- **6 个 seed=43 全完 → spawn Worker 跑 Fisher + bootstrap CI 脚本 → 结果补入 Experiments section**
- **Object magnitude sweep 全完 → spawn Worker 绘制 fig3（norm sensitivity curve: obs_only vs perdof across 5 norms）**
- **obs-only-default + perdof-default-r2 完成 → 确认 norm=1.42 catastrophic failure → 补入 magnitude narrative**
- **所有 figures 完成 → Abstract 最终版 → 提交前 Reviewer 全文审查**
- **spatial norm003-b2（8/10）即将完成 → 更新 spatial magnitude sweep 表（obs_only norm=0.03 数据点）**

### 5. 🎯 战略上下文
**核心结论链**：MVP passed (D003) → per-DOF claim dead on spatial (D027-D029) → per-DOF dead on object too (D030) → obs_only CRM +7.0pp on object is sole signal (D033) → paper pivoted to "sample-then-correct" narrative with honest negative about per-DOF features。

**最容易判断错的事**：
1. **Seed=43 partial SR 低不代表最终低**——LIBERO object tasks SR 分布极不均匀（有的 task 30%，有的 0%），partial 结果取决于已完成的 task 分布。等 10-task final 再下结论。
2. **不要把 spatial 和 object 的 magnitude 趋势混用**——spatial 全 norm obs_only ≈ 35%（无效应），object 随 norm 增大有真实增益（0.1→19%, 0.2→22%）。论文以 object 为主载体。
3. **ReconVLA 不是直接竞品**（D034）——它做 UQ+OOD 检测（"何时不信任"），ACR-VLA 做 selection+correction（"如何改进"）。A2C2 才是最近竞品（correction only，无 selection）。
4. **论文是 single-claim paper**（D023）——Claim 1: obs_only CRM correction > selection-only。ACI/COC (Claim 2) 和 SRPO stacking (Claim 3) 已砍。不要试图复活。
5. **bjb2-40593 环境特殊**——无 .git repo，CRM cache 在旧路径 `/root/autodl-tmp/crm_cache/spatial/`。

## 项目硬约束 (memory.md 节选)

## bjb2-40593 环境问题 (2026-05-14-15)

- 无 .git repo
- CRM cache 路径 /root/autodl-tmp/crm_cache/spatial/（旧路径，非 v5）
- Ghost PID 211962 已 kill，eval-mag-obsonly-norm003-b2 恢复运行

## [失败模式] submit_training_job EXIT_CODE=127 (2026-05-15)

tmux 用 `sh` 而非 `bash` 执行命令，`python` 等 conda/venv 命令不在 `sh` PATH 中。修复：命令必须用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."` 包裹。裸 `python -u ...` 有时可行（取决于服务器 PATH 配置），但不可靠。

## [失败模式] Kill 操作前必须逐参数比对 (2026-05-15)

**事故**: Worker 将 norm=0.3 (norm03) 误判为 norm=0.03 (norm003) 的重复实验，kill 了有效进程。cuda:0 空闲 9 小时。
**根因**: Worker 只看 session 名和 output_file 路径，未核对 `--max_correction_norm` 参数值。
**规则**: kill 实验前必须 `ps aux | grep` 完整命令行，逐一比对关键参数（mode, norm, checkpoint, benchmark）。名字相似 ≠ 同一实验。

## 可查的历史
前 105 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-16T00:43:43.113227+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
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

_source line 3 · 2026-05-16T00:43:43.165577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T00:43:48.606080+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read registry 确认实验状态', 'status': 'in_progress', 'activeForm': '读取 registry 确认实验状态'}, {'content': 'Reconcile crons 同步监控', 'status': 'pending', 'activeForm': '同步 cron 监控状态'}, {'content': '读 report.md 了解上次状态', 'status': 'pending', 'activeForm': '读取 report.md'}, {'content': '读 ROADMAP.md 了解研究方向', 'status': 'pending', 'activeForm': '读取 ROADMAP.md'}, {'content': '向 Director 汇报当前状态', 'status': 'pending', 'activeForm': '向 Director 汇报'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read registry 确认实验状态', 'status': 'in_progress', 'activeForm': '读取 registry 确认实验状态'}, {'content': 'Reconcile crons 同步监控', 'status': 'pending', 'activeForm': '同步 cron 监控状态'}, {'content': '读 report.md 了解上次状态', 'status': 'pending', 'activeForm': '读取 report.md'}, {'content': '读 ROADMAP.md 了解研究方向', 'status': 'pending', 'activeForm': '读取 ROADMAP.md'}, {'content': '向 Director 汇报当前状态', 'status': 'pending', 'activeForm': '向 Director 汇报'}]"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T00:43:48.664454+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "TodoWrite",
  "elapsed_ms": 58
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T00:43:51.737164+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
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

_source line 7 · 2026-05-16T00:43:51.787815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T00:43:56.193493+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T00:43:56.244138+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T00:43:57.150512+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "report.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T00:43:57.252427+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T00:44:00.883132+00:00_

Error: result (59,682 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-22463a65/20fb32a0-2f1c-45d2-9539-a110285f5588/tool-results/mcp-agent-ml-research-read_registry-1778892240621.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-22463a65/20fb32a0-2f1c-45d2-9539-a110285f5588/tool-results/mcp-agent-ml-research-read_registry-1778892240621.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 4689
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T00:45:58.666593+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 14, \"results\": [{\"exp_id\": \"eval-perdof-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=365925)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm03-object\", \"success\": true, \"actions\": [\"Job still running (pid=103028)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm005-object\", \"success\": true, \"actions\": [\"Job still running (pid=101610)\"]}, {\"exp_id\": \"eval-vla-mean-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=111709)\"]}, {\"exp_id\": \"eval-scalar-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=114664)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm003-object\", \"success\": true, \"actions\": [\"Job still running (pid=121325)\"]}, {\"exp_id\": \"eval-acr-object-v4-default-r2\", \"success\": true, \"actions\": [\"Job still running (pid=390936)\"]}, {\"exp_id\": \"eval-mag-perdof-norm02-object\", \"success\": true, \"actions\": [\"Job still running (pid=127732)\"]}, {\"exp_id\": \"eval-mag-perdof-norm005-object\", \"success\": true, \"actions\": [\"Job still running (pid=109650)\"]}, {\"exp_id\": \"eval-mag-perdof-norm003-object\", \"success\": true, \"actions\": [\"Job still running (pid=105938)\"]}, {\"exp_id\": \"eval-acr-object-obs-only-default\", \"success\": true, \"actions\": [\"Job still running (pid=134103)\"]}, {\"exp_id\": \"eval-obs-only-object-norm02-seed43-r2\", \"success\": true, \"actions\": [\"Job still running (pid=148788)\"]}, {\"exp_id\": \"eval-mag-perdof-norm02-seed43-object-r3\", \"success\": true, \"actions\": [\"Job still running (pid=144504)\"]}, {\"exp_id\": \"eval-mag-perdof-norm03-object-r3\", \"success\": true, \"actions\": [\"Job still running (pid=140759)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 122422
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T00:45:58.772394+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-16T00:43:07Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 125 个实验 — ANALYZING 2, DEPLOYED 1, DONE 107, PENDING 1, RUNNING 14\\n**DONE 分布**: failed 17, killed 49, negative 5, success 36\\n\\n### GPU 占用\\n- **实际运行**: 12 张 — bjb1-18228:cuda:1(eval-perdof-object-seed43), bjb1-32546:cuda:1(eval-vla-mean-object-seed43), bjb1-32546:cuda:2(eval-scalar-object-seed43), bjb1-32546:cuda:0(eval-mag-obsonly-norm003-object), bjb2-28827:cuda:0(eval-mag-perdof-norm003-object), bjb2-28827:1(eval-mag-perdof-norm005-object), bjb1-32546:cuda:5(eval-mag-perdof-norm02-object), bjb1-32546:cuda:4(eval-acr-object-obs-only-default), bjb1-18228:cuda:0(eval-acr-object-v4-default-r2), bjb1-32546:cuda:3(eval-obs-only-object-norm02-seed43-r2), bjb2-28827:cuda:2(eval-mag-perdof-norm03-object-r3), bjb2-28827:cuda:3(eval-mag-perdof-norm02-seed43-object-r3)\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-perdof-object-seed43` | bjb1-18228 | cuda:1 | 365925 | `…/acr-vla-conformal-refinement/eval-perdof-object-seed43.log` |\\n| `eval-vla-mean-object-seed43` | bjb1-32546 | cuda:1 | 111709 | `…cr-vla-conformal-refinement/eval-vla-mean-object-seed43.log` |\\n| `eval-scalar-object-seed43` | bjb1-32546 | cuda:2 | 114664 | `…/acr-vla-conformal-refinement/eval-scalar-object-seed43.log` |\\n| `eval-mag-obsonly-norm005-object` | bjb2-28827 | ? | 101610 | `…-conformal-refinement/logs/eval_object_obs_only_norm005.log` |\\n| `eval-mag-obsonly-norm03-object` | bjb2-28827 | ? | 103028 | `…a-conformal-refinement/logs/eval_object_obs_only_norm03.log` |\\n| `eval-mag-obsonly-norm003-object` | bjb1-32546 | cuda:0 | 121325 | `…la-conformal-refinement/eval-mag-obsonly-norm003-object.log` |\\n
…[truncated 6518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 121621
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T00:45:58.932956+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 20:48 UTC | 更新原因: 引用审计 PASSED + ±1pp 统一完成 + Discussion/Conclusion 完成; 更新近期任务清单\\n\\n## 核心方向\\nobs_only CRM（基于观测特征的 learned correction）是唯一存活路径。Per-DOF conformal claim 已死。论文 story：sample-then-correct > sample-then-select，obs features > conformal features（honest negative）。详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 3 — Paper writing + seed=43 statistical validation\\n- **MVP**: PASS\\n- **Object 10/10 FINAL ✅**: obs_only 19.0% vs argmin 12.0% (+7.0pp) — 超过 5pp claim 门槛 (D033)\\n- **Object obs_only norm=0.2 FINAL ✅**: **22.0%** (+10.0pp over argmin) — **PROJECT HIGH**\\n- **Spatial LOCKED ✅**: 全部 CRM 变体确认 dead（argmin 34%, perdof 35%, obs_only 35%, scalar 32%）\\n- **Magnitude sweep**: obs_only stable 35-44% across norms, perdof collapses away from 0.1 (D032)\\n- **Seed=43 部署中**: 6 方在跑，obs_only 6/10, argmin 6/10, 预计 ~4-5h\\n- **Paper Agent**: Intro ✅ Method ✅ Experiments ✅ Related Work ✅ Discussion/Conclusion ✅ → Figures 进行中 (fig1 WIP, fig2/fig3 pending)\\n- **引用审计**: ✅ PASSED — 29 cited keys 全部验证, 22 方法归因验证通过, 0 NEEDS_REVIEW, chen2026reconvla + braun2025cgs 两个 blocking issue 已修复\\n- **±1pp 措辞**: ✅ 全文统一为 `best CRM within 1\\\\,pp of the selection baseline`\\n\\n## Object Benchmark（seed=42, ALL FINAL ✅）\\n\\n| 方法 | SR | vs argmin | 状态 |\\n|------|-----|-----------|------|\\n| **obs_only 0.2** | **22.0%** | **+10.0pp** | FINAL ✅ PROJECT HIGH |\\n| **obs_only 0.1** | **19.0%** | **+7.0pp** | FINAL ✅ |\\n| argmin K=10 | 12.0% | baseline | FINAL ✅ |\\n| VLA-only K=1 | 12.0% | 0pp | FINAL ✅ |\\n| VLA-mean K=10 | 12.0% | 0pp | FINAL ✅ |\\n| perdof 0.1 | 11.0% | -1.0pp | FINAL ✅ |\\n| scalar 0.1 | 9.0% | -3.0pp | FINAL ✅ (negative) |\\n\\n## Spatial
…[truncated 3923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 121680
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T00:46:04.496947+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['exp_id', 'status', 'hypothesis', 'server', 'gpu', 'pid', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['exp_id', 'status', 'hypothesis', 'server', 'gpu', 'pid', 'metrics']"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T00:46:05.461090+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'ANALYZING'}",
  "fields": "['exp_id', 'status', 'hypothesis', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'ANALYZING'}",
    "fields": "['exp_id', 'status', 'hypothesis', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T00:46:06.074291+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'PENDING'}",
  "fields": "['exp_id', 'status', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'PENDING'}",
    "fields": "['exp_id', 'status', 'hypothesis']"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T00:46:07.793817+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-mag-obsonly-norm03-object\": {\"status\": \"RUNNING\", \"metrics\": {\"tasks_done\": 2, \"tasks_total\": 10, \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0}, \"server\": \"bjb2-28827\", \"pid\": 103034, \"gpu\": \"cuda:5\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"RUNNING\", \"metrics\": {\"tasks_done\": 2, \"tasks_total\": 10, \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0}, \"server\": \"bjb2-28827\", \"pid\": 101616, \"gpu\": \"cuda:4\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"RUNNING\", \"metrics\": {\"tasks_done\": 0, \"tasks_total\": 10, \"partial_sr\": {}, \"server\": \"bjb2-28827\", \"pid\": 144513, \"gpu\": \"cuda:3\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"RUNNING\", \"metrics\": {\"tasks_done\": 0, \"tasks_total\": 10, \"partial_sr\": {}, \"server\": \"bjb2-28827\", \"pid\": 140759, \"gpu\": \"cuda:2\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"RUNNING\", \"metrics\": {\"tasks_done\": 2, \"tasks_total\": 10, \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0}, \"server\": \"bjb2-28827\", \"pid\": 109655, \"gpu\": \"cuda:1\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-perdof-norm003-object\": {\"status\": \"RUNNING\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"metrics\": {\"tasks_done\": 2, \"tasks_total\": 10, \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0}, \"server\": \"bjb2-2
…[truncated 4666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3296
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T00:46:10.263618+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-mag-obsonly-norm003-b2\": {\"status\": \"ANALYZING\", \"metrics\": {\"tasks_done\": 8, \"tasks_total\": 10, \"partial_sr\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0}, \"server\": \"bjb2-40593\", \"pid\": 227434, \"gpu\": \"cuda:0\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-obs-only-object-seed43\": {\"status\": \"ANALYZING\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"metrics\": {\"tasks_done\": 6, \"tasks_total\": 10, \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0}, \"server\": \"bjb1-18228\", \"pid\": 356495, \"gpu\": \"cuda:2\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}}, \"count\": 2, \"total\": 2, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4257}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 4802
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T00:46:12.740776+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-mag-obsonly-norm03-b2\": {\"status\": \"PENDING\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4072}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 6666
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T00:46:52.625733+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-obs-only-object-seed43'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-obs-only-object-seed43'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T00:46:53.130071+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3596}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T00:46:53.182558+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-mag-obsonly-norm003-b2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-mag-obsonly-norm003-b2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T00:46:54.336289+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.906}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1153
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T00:46:54.487117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T00:46:54.538440+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_22463a65.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T00:47:10.156426+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'ANALYZING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'ANALYZING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T00:47:10.158722+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T00:47:10.611669+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-mag-obsonly-norm003-b2\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-16T00:42:56.186Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"225139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_spatial\"}, \"pid\": 227426, \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"tasks_done\": 8, \"tasks_total\": 10, \"partial_sr\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0}, \"server\": \"bjb2-40593\", \"pid\": 227434, \"gpu\": \"cuda:0\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:42:50.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:43:27.876843+00:00\"}]}}, \"eval-obs-only-object-seed43\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T
…[truncated 1839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 455
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T00:47:10.662317+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "Glob",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T00:47:45.464115+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_project_resource_usage",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_project_resource_usage",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T00:47:45.464576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T00:47:48.747621+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read registry 确认实验状态', 'status': 'completed', 'activeForm': '读取 registry 确认实验状态'}, {'content': 'Reconcile crons 同步监控', 'status': 'completed', 'activeForm': '同步 cron 监控状态'}, {'content': '读 report.md 了解上次状态', 'status': 'completed', 'activeForm': '读取 report.md'}, {'content': '读 ROADMAP.md 了解研究方向', 'status': 'completed', 'activeForm': '读取 ROADMAP.md'}, {'content': '调查 eval-obs-only-object-seed43 ANALYZING 状态 (P0)', 'status': 'in_progress', 'activeForm': '调查 P0 实验 ANALYZING 状态'}, {'content': '调查 eval-mag-obsonly-norm003-b2 ANALYZING 状态', 'status': 'pending', 'activeForm': '调查 spatial norm003 ANALYZING 状态'}, {'content': '检查空闲 GPU 并填充', 'status': 'pending', 'activeForm': '检查空闲 GPU'}, {'content': '向 Director 汇报当前状态', 'status': 'pending', 'activeForm': '向 Director 汇报'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read registry 确认实验状态', 'status': 'completed', 'activeForm': '读取 registry 确认实验状态'}, {'content': 'Reconcile crons 同步监控', 'status': 'completed', 'activeForm': '同步 cron 监控状态'}, {'content': '读 report.md 了解上次状态', 'status': 'completed', 'activeForm': '读取 report.md'}, {'content': '读 ROADMAP.md 了解研究方向', 'status': 'completed', 'activeForm': '读取 ROADMAP.md'}, {'content': '调查 eval-obs-only-object-seed43 ANALYZING 状态 (P0)', 'status': 'in_progress', 'activeForm': '调查 P0 实验 ANALYZING 状态'}, {'content': '调查 eval-mag-obsonly-norm003-b2 ANALYZING 状态', 'status': 'pending', 'activeForm': '调查 spatial norm003 ANALYZING 状态'}, {'content': '检查空闲 GPU 并填充', 'status': 'pending', 'activeForm': '检查空闲 GPU'}, {'content': '向 Director 汇报当前状态', 'status': 'pending', 'activeForm': '向 Director 汇报'}]"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T00:47:48.748120+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T00:47:52.023467+00:00_

called mcp__agent-ml-research__get_project_resource_usage

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_project_resource_usage</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-16T00:47:52.500070+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [], \"actually_running_gpus\": [{\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"eval-perdof-object-seed43\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"eval-vla-mean-object-seed43\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"eval-scalar-object-seed43\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-mag-obsonly-norm003-object\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-mag-perdof-norm003-object\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"1\", \"exp_id\": \"eval-mag-perdof-norm005-object\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:5\", \"exp_id\": \"eval-mag-perdof-norm02-object\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:4\", \"exp_id\": \"eval-acr-object-obs-only-default\"}, {\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-acr-object-v4-default-r2\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"eval-obs-only-object-norm02-seed43-r2\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"eval-mag-perdof-norm03-object-r3\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"eval-mag-perdof-norm02-seed43-object-r3\"}], \"allocated_but_idle\": [], \"running_experiments\": [{\"exp_id\": \"eval-perdof-object-seed43\", \"gpus\": [\"cuda:1\"], \"util_avg\": null}, {\"exp_id\": \"eval-vla-mean-object-seed43\", \"gpus\": [\"cuda:1\"], \"util_avg\": null}, {\"exp_id\": \"eval-scalar-object-seed43\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}, {\"exp_id\": \"eval-mag-obsonly-norm003-object\", \"gpus\": [\"cuda:0\"], \"util_avg\": null}, {\"exp_id\": \"eval-mag-perdof-norm003-object\", \"gpus\": [\"cuda:0\"], \"util_avg\": null}, {\"exp_id\": \"eval-mag-perdof-norm005-object\", \"gpus\": [\"1\"], \"util_avg\": null}, {\"exp_id\": \"eval-mag-perdof-norm02-object\", \"gpus\": [\"cuda:5\"], \"util_
…[truncated 955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 476
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T00:47:52.500533+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T00:47:52.553238+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_analysis_eval-obs-only-object-seed43_20260516T004714\", \"task_type\": \"analysis:eval-obs-only-object-seed43\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-16T00:47:15.177507+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_analysis_eval-mag-obsonly-norm003-b2_20260516T004734\", \"task_type\": \"analysis:eval-mag-obsonly-norm003-b2\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-16T00:47:35.146139+00:00\", \"ended_at\": null}], \"count\": 2}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T00:48:52.873533+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cancel_worker,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cancel_worker,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T00:48:52.936564+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "ToolSearch",
  "elapsed_ms": 63
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T00:48:56.614571+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_analysis_eval-obs-only-object-seed43_20260516T004714",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_analysis_eval-obs-only-object-seed43_20260516T004714",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T00:48:56.786941+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_eval-obs-only-object-seed43_20260516T004714\", \"status\": \"done\", \"task_type\": \"analysis:eval-obs-only-object-seed43\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-16T00:47:15.177507+00:00\", \"ended_at\": \"2026-05-16T00:48:45.406307+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"Registry 已更新为 DONE/negative。以下是完整分析结果：\\n\\n## eval-obs-only-object-seed43 结果\\n\\n### 完成状态\\n**10/10 task 全部完成**，EXIT_CODE=0，正常退出。\\n\\n### Per-task Success Rate\\n\\n| Task | SR |\\n|------|-----|\\n| alphabet_soup | 0% (0/10) |\\n| cream_cheese | 10% (1/10) |\\n| salad_dressing | 10% (1/10) |\\n| bbq_sauce | 30% (3/10) |\\n| ketchup | 0% (0/10) |\\n| tomato_sauce | 0% (0/10) |\\n| butter | 0% (0/10) |\\n| milk | 10% (1/10) |\\n| chocolate_pudding | 40% (4/10) |\\n| orange_juice | 20% (2/10) |\\n\\n### Overall SR: **12% (12/100)**\\n\\n### vs Argmin seed=43 对比\\n- obs_only: **12%** vs argmin: **17%** → **-5pp，obs_only 更差**\\n\\n### 两个 seed 汇总\\n\\n| | seed=42 | seed=43 | Pooled |\\n|--|---------|---------|--------|\\n| obs_only | 19% | 12% | 31/200 (15.5%) |\\n| argmin | 12% | 17% | 29/200 (14.5%) |\\n| diff | +7pp | -5pp | +1pp |\\n\\n### Fisher Exact Test\\n- **Pooled one-sided p = 0.4444**（obs_only > argmin）\\n- Pooled two-sided p = 0.8888\\n- Odds ratio = 1.08\\n\\n### 结论：**NEGATIVE**\\n\\nobs_only 在 object benchmark 上没有显著优于 argmin。seed=42 的+7pp优势在 seed=43 上完全没有复现（反而-5pp），pooled 200 trials 仅差1pp，p=0.44 远未达到显著性。obs_only 对 object benchmark 的改进不成立。\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 172
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T00:48:56.793803+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_analysis_eval-mag-obsonly-norm003-b2_20260516T004734",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_analysis_eval-mag-obsonly-norm003-b2_20260516T004734",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-16T00:48:56.909649+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_eval-mag-obsonly-norm003-b2_20260516T004734\", \"status\": \"done\", \"task_type\": \"analysis:eval-mag-obsonly-norm003-b2\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-16T00:47:35.146139+00:00\", \"ended_at\": \"2026-05-16T00:48:21.054289+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"Registry 已更新为 DONE(success)。\\n\\n## 结果汇报\\n\\n**数据来源**: `/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json`\\n\\n### 10-task Final SR: **34%** (34/100)\\n\\n### Per-task breakdown\\n\\n| Task | SR | Successes |\\n|---|---|---|\\n| between_plate_and_ramekin | 0.9 | 9/10 |\\n| next_to_ramekin | **1.0** | 10/10 |\\n| next_to_cookie_box | 0.8 | 8/10 |\\n| on_cookie_box | 0.3 | 3/10 |\\n| next_to_plate | 0.3 | 3/10 |\\n| in_top_drawer | 0.1 | 1/10 |\\n| from_table_center | 0.0 | 0/10 |\\n| on_ramekin | 0.0 | 0/10 |\\n| on_stove | 0.0 | 0/10 |\\n| on_wooden_cabinet | 0.0 | 0/10 |\\n\\n### Obs-only Spatial Magnitude Sweep 完整对比\\n\\n| norm | SR (10-task) |\\n|---|---|\\n| **0.03** | **34%** |\\n| 0.05 | 35% |\\n| 0.10 | 35% |\\n| 0.20 | 35% |\\n| 0.30 | 36% |\\n\\n### 分析\\n\\nMagnitude sweep 结论非常清晰：**obs_only CRM 对 correction magnitude 几乎不敏感**。从 norm=0.03 到 norm=0.30（10倍跨度），SR 仅在 34%-36% 之间波动，差异在统计噪声范围内。\\n\\nnorm=0.03 的 34% 比 partial 8-task 数据（38.75%）低，因为新增的两个 task（next_to_plate: 0.3, on_wooden_cabinet: 0.0）拉低了均值。\\n\\n关键发现：即使 correction 被限制到极小的 0.03 norm，obs_only 模式的表现与大 norm 几乎一致。这说明 obs_only CRM 的有效性不依赖于 correction 幅度——模型本质上在做某种\\\"方向性\\\"修正而非\\\"幅度性\\\"修正，或者修正本身就很小使得 norm clipping 基本不生效。\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 115
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T00:49:49.013172+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-obs-only-object-seed43'}",
  "fields": "['status', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-obs-only-object-seed43'}",
    "fields": "['status', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-16T00:49:50.027791+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.707}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1014
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-16T00:49:50.028225+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-mag-obsonly-norm003-b2'}",
  "fields": "['status', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-mag-obsonly-norm003-b2'}",
    "fields": "['status', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T00:49:50.786459+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5656}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 758
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-16T00:49:50.786900+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-16T00:49:50.838224+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight (Scenario C — ACTIVE, D029+D030 confirmed)\\nA lightweight observation-conditioned learned correction module (CRM), applied after conformal sample selection, can synthesize actions better than any individual VLA sample. The key contribution is the **sample-then-correct** pipeline itself and the discovery that **correction magnitude control is critical for closed-loop stability**. Per-DOF conformal features as CRM input offer no additional value over observation features — an honest negative result that challenges the intuition from synthetic experiments.\\n\\n## Active Framing: Scenario C\\n**Confirmed by data**: obs_only CRM > perdof CRM ≈ scalar CRM ≈ argmin on spatial (D029-D030); obs_only CRM **+7.0pp** over argmin on object 10/10 tasks FINAL (19.0% vs 12.0%); magnitude sweep shows obs_only robust to norm while perdof collapses at high norm (D032).\\n\\nStory: \\\"Observation-conditioned residual correction is the key contribution. The sample-then-correct pipeline (K=10 conformal selection + learned CRM correction) significantly outperforms pure sample selection on object manipulation tasks. Per-DOF conformal statistics as direct CRM input offer no advantage over observation features — but conformal prediction remains essential for the sample selection stage. Correction magnitude control is a critical and previously unrecognized factor for closed-loop VLA correction.\\\"\\n\\n## Core Claims (CoRL 单 Claim 论文)\\n\\n1. **Observation-conditioned learned correction (CRM) significantly improves VLA robustness beyond sample selection**\\n   - **主 claim**: obs_only CRM vs argmin-only ≥ 5pp on object bench
…[truncated 6928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T00:51:08.443293+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read registry 确认实验状态', 'status': 'completed', 'activeForm': '读取 registry 确认实验状态'}, {'content': 'Reconcile crons 同步监控', 'status': 'completed', 'activeForm': '同步 cron 监控状态'}, {'content': '读 report.md 了解上次状态', 'status': 'completed', 'activeForm': '读取 report.md'}, {'content': '读 ROADMAP.md 了解研究方向', 'status': 'completed', 'activeForm': '读取 ROADMAP.md'}, {'content': '调查 eval-obs-only-object-seed43 ANALYZING 状态 (P0)', 'status': 'completed', 'activeForm': '调查 P0 实验 ANALYZING 状态'}, {'content': '调查 eval-mag-obsonly-norm003-b2 ANALYZING 状态', 'status': 'completed', 'activeForm': '调查 spatial norm003 ANALYZING 状态'}, {'content': '产出 Framing 调整提案 (red-section)', 'status': 'in_progress', 'activeForm': '撰写 Framing 调整提案'}, {'content': '向 Director 汇报 NEGATIVE 结果 + 提案', 'status': 'pending', 'activeForm': '向 Director 汇报'}, {'content': '检查空闲 GPU 并填充', 'status': 'pending', 'activeForm': '检查空闲 GPU'}, {'content': '更新 memory.md 记录关键教训', 'status': 'pending', 'activeForm': '更新 memory.md'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read registry 确认实验状态', 'status': 'completed', 'activeForm': '读取 registry 确认实验状态'}, {'content': 'Reconcile crons 同步监控', 'status': 'completed', 'activeForm': '同步 cron 监控状态'}, {'content': '读 report.md 了解上次状态', 'status': 'completed', 'activeForm': '读取 report.md'}, {'content': '读 ROADMAP.md 了解研究方向', 'status': 'completed', 'activeForm': '读取 ROADMAP.md'}, {'content': '调查 eval-obs-only-object-seed43 ANALYZING 状态 (P0)', 'status': 'completed', 'activeForm': '调查 P0 实验 ANALYZING 状态'}, {'content': '调查 eval-mag-obsonly-norm003-b2 ANALYZING 状态', 'status': 'completed', 'activeForm': '调查 spatial norm003 ANALYZING 状态'}, {'content': '产出 Framing 调整提案 (red-section)', 'status': 'in_progress', 'activeForm': '撰写 Framing 调整提案'}, {'content': '向 Director 汇报 NEGATIVE 结果 + 提案', 'status': 'pending', 'activeForm': '向 Director 汇报'}, {'content': '检查空闲 GPU 并填充', 'status': 'pending', 'activeForm': '检查空闲 GPU'}, {'content': '更新 memory.md 记录关键教训', 'status': 'pending', 'activeForm': '更新 memory.md'}]"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-16T00:51:08.445573+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "TodoWrite",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-16T00:52:15.839178+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "text": "[资源] GPU 分配 17 / 实际跑 14 | Worker 池 0 (GPU 0 / CPU 0) | ⚠️ 3 GPU 空闲 (bjb1-18228:cuda:2,3 + bjb2-40593:cuda:0)\n\n# 🔴 CRITICAL NEGATIVE: obs_only seed=43 不复现，核心 claim 不成立\n\n## 实验结果（来源：registry + Worker 分析 eval-obs-only-object-seed43）\n\n| | seed=42 | seed=43 | Pooled (200 trials) |\n|--|---------|---------|---------------------|\n| obs_only (norm=0.1) | 19% | **12%** | 15.5% (31/200) |\n| argmin | 12% | **17%** | 14.5% (29/200) |\n| diff | +7pp | **-5pp** | **+1pp** |\n\n**Fisher exact test (one-sided): p = 0.4444** — 远未达显著性。\n\nseed=43 的 argmin 基线反而升高（12%→17%），obs_only 反而下降（19%→12%）。seed=42 的 +7pp 优势是种子特异性噪声，不是真实效应。\n\n**按 kill criteria（paper_framing.md）：pooled +1pp < 3pp 内部 kill 门槛。norm=0.1 claim 已死。**\n\n## 📊 同时完成：eval-mag-obsonly-norm003-b2 (SUCCESS)\n\nSpatial obs_only norm=0.03 = 34%。5 点 magnitude sweep 完成：34%/35%/35%/35%/36%（norm=0.03/0.05/0.1/0.2/0.3）。**obs_only 对 magnitude 完全不敏感**——这是真实的、可复现的发现。\n\n## Framing 调整提案（red-section）\n\n### 1. 原 claim\nobs_only CRM correction > argmin selection，≥5pp + p<0.05 on LIBERO object。\n\n### 2. 实验结果\nPooled 200 trials: +1pp, p=0.44。Claim 不成立。\n\n### 3. 重新审视\n- **被挑战的 hypothesis**：obs_only CRM 能产生优于 argmin 选择的动作\n- **被忽视的变量**：seed sensitivity——LIBERO object 100-trial 的标准误 SE ≈ 3.6%，+7pp 落在 2σ 内，本就不稳定\n- **已做实验中仍然有效的部分**：\n  - ✅ Magnitude sensitivity 发现（obs_only stable vs perdof collapse）——跨两个 benchmark + 多个 seed 一致\n  - ✅ Per-DOF features 无效（honest negative）——spatial + object 一致\n  - ✅ Default norm=1.42 catastrophic failure（ablation 进行中）\n  - ❌ obs_only > argmin 的绝对改进——不可靠\n  \n### 4. 新 narrative 骨架（3 种备选）\n\n**Option A: \"Magnitude Sensitivity 是核心发现\" pivot（推荐）**\n- Story: \"correction magnitude control 是此前被忽视的关键因素。我们发现 (1) unbounded correction = catastrophic (0%), bounded correction = functional; (2) obs_only CRM 对 magnitude 完全鲁棒（34-36% spatial, 12-22% object across norms），perdof CRM 在高 norm 崩塌; (3) per-DOF features 无效。\"\n- Headline result: magnitude robustness + obs vs perdof divergence（真实信号，跨 benchmark/seed 一致）\n- 优势：基于可复现的真实信号，novelty 明确（无人研究 VLA correction magnitude sensitivity）\n- 风险：从 \"我们的方法更好\" 变成 \"我们发现一个重要的设计选择\"——审稿人可能觉得贡献不够 actionable\n- CoRL 适配度：中等——CoRL 欢迎 empirical insights，但没有\"我们方法赢了\"的 headline 会弱一些\n\n**Option B: \"norm=0.2 Last Hope\"——等 seed=43 norm=0.2 结果**\n- eval-obs-only-object-norm02-seed43-r2 正在跑（1/10 tasks，bjb1-32546:cuda:3）\n- seed=42 norm=0.2 = 22%（+10pp，PROJECT HIGH）\n- 如果 norm=0.2 seed=43 也显著 → 窄化 claim 为 \"with appropriate magnitude tuning (norm=0.2)\"\n- 风险：极高——norm=0.1 已失败，norm=0.2 可能同样是种子噪声\n- 预计完成时间：~30-40 小时（按当前 1/10 tasks 速度）\n- 如果也失败：彻底确认无真实效应\n\n**Option C: \"Honest Null Result\" paper**\n- \"我们提出 sample-then-correct pipeline 并系统性评估发现：learned correction 不能一致地超越 argmin selection。贡献：(1) pipeline framework, (2) 系统性 conditioning comparison, (3) magnitude sensitivity 发现, (4) honest negative about per-DOF features。\"\n- 适合 workshop 或 Findings track，CoRL 主会接受度低\n\n### 5. 对论文各章节的影响\n\n| 章节 | 当前状态 | 需要改动 |\n|------|---------|---------|\n| Abstract | \"+Xpp over argmin (p&lt;Y)\" | 必须删除或改为 \"marginal/non-significant\" |\n| Intro | \"significantly improves\" | 去掉 significantly，改为 empirical study framing |\n| Method | pipeline 描述 | 基本不变 |\n| Experiments | Table 1 只有 seed=42 | 加 seed=43 + pooled + Fisher test，诚实报告 |\n| Discussion | \"CRM works\" narrative | 大改→magnitude sensitivity + conditioning comparison 为主线 |\n| Conclusion | method contribution | 改为 insight/empirical contribution |\n| **Figures** | fig1 WIP, fig2/fig3 pending | 需重新规划——magnitude curve 成为核心 figure |\n\n### 6. 建议下一步实验\n\na. **等 norm=0.2 seed=43**（已在跑，~30-40h）——最后一根稻草\nb. **等 default norm=1.42 ablation 完成**（bjb1-18228:cuda:0, 1/10）——确认 catastrophic failure\nc. **如果 norm=0.2 也失败：pivot to Option A**，不再追加更多 seed\nd. **3 个空闲 GPU 可选**：\n   - bjb2-40593:cuda:0 — submit eval-mag-obsonly-norm03-b2（PENDING，spatial norm=0.3，补完 spatial magnitude sweep 最后一格）\n   - bjb1-18228:cuda:2,3 — 可跑 object magnitude sweep 的其他数据点（如 argmin baseline for norm=0.2 control），或等 Director 决定方向后再分配\n\n### 反思实验计划\n\n1. **这个 negative 是方法问题还是 hypothesis 方向错？**——hypothesis 方向可能错。obs_only CRM 的 correction 在 object 上可能没有真实效应。100-trial eval 的统计力不足（SE≈3.6%）让 seed=42 的噪声看起来像信号。\n2. **受影响的矩阵格**：所有 \"obs_only > argmin\" 的 claim 格子。magnitude sweep 格子不受影响（那是 obs_only 内部 norm 鲁棒性比较，不涉及 vs argmin）。\n3. **2-3 个 negative 已连续出现**：per-DOF dead (D029-D030) → obs_only norm=0.1 无显著性 → **建议 pivot 到 Option A（magnitude sensitivity 为核心）**\n4. **pivot ≠ 降级 venue**——仍冲 CoRL 2026，只是换研究角度\n\n## 请 Director 决策\n\n1. **等 norm=0.2 seed=43（Option B）还是立即 pivot（Option A）？** 我倾向等 norm=0.2 结果再决定——但 Director 可以 override。\n2. **3 个空闲 GPU 怎么用？** bjb2-40593 可先 submit 已 PENDING 的 spatial norm=0.3。bjb1-18228 两张卡等指令。\n3. **Paper writing 是否暂停？** 当前 5 章 + 引用审计已完成，但 headline result 需要改。建议暂停直到 framing 确定。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "text": "[资源] GPU 分配 17 / 实际跑 14 | Worker 池 0 (GPU 0 / CPU 0) | ⚠️ 3 GPU 空闲 (bjb1-18228:cuda:2,3 + bjb2-40593:cuda:0)\n\n# 🔴 CRITICAL NEGATIVE: obs_only seed=43 不复现，核心 claim 不成立\n\n## 实验结果（来源：registry + Worker 分析 eval-obs-only-object-seed43）\n\n| | seed=42 | seed=43 | Pooled (200 trials) |\n|--|---------|---------|---------------------|\n| obs_only (norm=0.1) | 19% | **12%** | 15.5% (31/200) |\n| argmin | 12% | **17%** | 14.5% (29/200) |\n| diff | +7pp | **-5pp** | **+1pp** |\n\n**Fisher exact test (one-sided): p = 0.4444** — 远未达显著性。\n\nseed=43 的 argmin 基线反而升高（12%→17%），obs_only 反而下降（19%→12%）。seed=42 的 +7pp 优势是种子特异性噪声，不是真实效应。\n\n**按 kill criteria（paper_framing.md）：pooled +1pp < 3pp 内部 kill 门槛。norm=0.1 claim 已死。**\n\n## 📊 同时完成：eval-mag-obsonly-norm003-b2 (SUCCESS)\n\nSpatial obs_only norm=0.03 = 34%。5 点 magnitude sweep 完成：34%/35%/35%/35%/36%（norm=0.03/0.05/0.1/0.2/0.3）。**obs_only 对 magnitude 完全不敏感**——这是真实的、可复现的发现。\n\n## Framing 调整提案（red-section）\n\n### 1. 原 claim\nobs_only CRM correction > argmin selection，≥5pp + p<0.05 on LIBERO object。\n\n### 2. 实验结果\nPooled 200 trials: +1pp, p=0.44。Claim 不成立。\n\n### 3. 重新审视\n- **被挑战的 hypothesis**：obs_only CRM 能产生优于 argmin 选择的动作\n- **被忽视的变量**：seed sensitivity——LIBERO object 100-trial 的标准误 SE ≈ 3.6%，+7pp 落在 2σ 内，本就不稳定\n- **已做实验中仍然有效的部分**：\n  - ✅ Magnitude sensitivity 发现（obs_only stable vs perdof collapse）——跨两个 benchmark + 多个 seed 一致\n  - ✅ Per-DOF features 无效（honest negative）——spatial + object 一致\n  - ✅ Default norm=1.42 catastrophic failure（ablation 进行中）\n  - ❌ obs_only > argmin 的绝对改进——不可靠\n  \n### 4. 新 narrative 骨架（3 种备选）\n\n**Option A: \"Magnitude Sensitivity 是核心发现\" pivot（推荐）**\n- Story: \"correction magnitude control 是此前被忽视的关键因素。我们发现 (1) unbounded correction = catastrophic (0%), bounded correction = functional; (2) obs_only CRM 对 magnitude 完全鲁棒（34-36% spatial, 12-22% object across norms），perdof CRM 在高 norm 崩塌; (3) per-DOF features 无效。\"\n- Headline result: magnitude robustness + obs vs perdof divergence（真实信号，跨 benchmark/seed 一致）\n- 优势：基于可复现的真实信号，novelty 明确（无人研究 VLA correction magnitude sensitivity）\n- 风险：从 \"我们的方法更好\" 变成 \"我们发现一个重要的设计选择\"——审稿人可能觉得贡献不够 actionable\n- CoRL 适配度：中等——CoRL 欢迎 empirical insights，但没有\"我们方法赢了\"的 headline 会弱一些\n\n**Option B: \"norm=0.2 Last Hope\"——等 seed=43 norm=0.2 结果**\n- eval-obs-only-object-norm02-seed43-r2 正在跑（1/10 tasks，bjb1-32546:cuda:3）\n- seed=42 norm=0.2 = 22%（+10pp，PROJECT HIGH）\n- 如果 norm=0.2 seed=43 也显著 → 窄化 claim 为 \"with appropriate magnitude tuning (norm=0.2)\"\n- 风险：极高——norm=0.1 已失败，norm=0.2 可能同样是种子噪声\n- 预计完成时间：~30-40 小时（按当前 1/10 tasks 速度）\n- 如果也失败：彻底确认无真实效应\n\n**Option C: \"Honest Null Result\" paper**\n- \"我们提出 sample-then-correct pipeline 并系统性评估发现：learned correction 不能一致地超越 argmin selection。贡献：(1) pipeline framework, (2) 系统性 conditioning comparison, (3) magnitude sensitivity 发现, (4) honest negative about per-DOF features。\"\n- 适合 workshop 或 Findings track，CoRL 主会接受度低\n\n### 5. 对论文各章节的影响\n\n| 章节 | 当前状态 | 需要改动 |\n|------|---------|---------|\n| Abstract | \"+Xpp over argmin (p&lt;Y)\" | 必须删除或改为 \"marginal/non-significant\" |\n| Intro | \"significantly improves\" | 去掉 significantly，改为 empirical study framing |\n| Method | pipeline 描述 | 基本不变 |\n| Experiments | Table 1 只有 seed=42 | 加 seed=43 + pooled + Fisher test，诚实报告 |\n| Discussion | \"CRM works\" narrative | 大改→magnitude sensitivity + conditioning comparison 为主线 |\n| Conclusion | method contribution | 改为 insight/empirical contribution |\n| **Figures** | fig1 WIP, fig2/fig3 pending | 需重新规划——magnitude curve 成为核心 figure |\n\n### 6. 建议下一步实验\n\na. **等 norm=0.2 seed=43**（已在跑，~30-40h）——最后一根稻草\nb. **等 default norm=1.42 ablation 完成**（bjb1-18228:cuda:0, 1/10）——确认 catastrophic failure\nc. **如果 norm=0.2 也失败：pivot to Option A**，不再追加更多 seed\nd. **3 个空闲 GPU 可选**：\n   - bjb2-40593:cuda:0 — submit eval-mag-obsonly-norm03-b2（PENDING，spatial norm=0.3，补完 spatial magnitude sweep 最后一格）\n   - bjb1-18228:cuda:2,3 — 可跑 object magnitude sweep 的其他数据点（如 argmin baseline for norm=0.2 control），或等 Director 决定方向后再分配\n\n### 反思实验计划\n\n1. **这个 negative 是方法问题还是 hypothesis 方向错？**——hypothesis 方向可能错。obs_only CRM 的 correction 在 object 上可能没有真实效应。100-trial eval 的统计力不足（SE≈3.6%）让 seed=42 的噪声看起来像信号。\n2. **受影响的矩阵格**：所有 \"obs_only > argmin\" 的 claim 格子。magnitude sweep 格子不受影响（那是 obs_only 内部 norm 鲁棒性比较，不涉及 vs argmin）。\n3. **2-3 个 negative 已连续出现**：per-DOF dead (D029-D030) → obs_only norm=0.1 无显著性 → **建议 pivot 到 Option A（magnitude sensitivity 为核心）**\n4. **pivot ≠ 降级 venue**——仍冲 CoRL 2026，只是换研究角度\n\n## 请 Director 决策\n\n1. **等 norm=0.2 seed=43（Option B）还是立即 pivot（Option A）？** 我倾向等 norm=0.2 结果再决定——但 Director 可以 override。\n2. **3 个空闲 GPU 怎么用？** bjb2-40593 可先 submit 已 PENDING 的 spatial norm=0.3。bjb1-18228 两张卡等指令。\n3. **Paper writing 是否暂停？** 当前 5 章 + 引用审计已完成，但 headline result 需要改。建议暂停直到 framing 确定。"
  }
}
```

</details>

---
