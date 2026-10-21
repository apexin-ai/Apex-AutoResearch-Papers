# Reviewer coordination (archived snapshot)

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 112
- **Recorded user turns:** 2
- **Tool calls:** 54
- **Original source:** `logs/chats/archive/feishu_group_oc_a79563aecf81c0da6bbb0710df2f0b6d_reviewer_20260525T061307_373577.jsonl`
- **Structured JSON:** [`e72cba633563886b28e3.json`](../../sessions/e7/e72cba633563886b28e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

110 recorded events

### User

_source line 1 · 2026-05-24T19:49:38.159726+00:00_

[HANDOFF] 你是 Research Reviewer，这是 Loop #26。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-21977，项目 gpu_ids 需从 constraints.yaml 确认（之前有越界事故）
- 论文 DDL: EMNLP 2026 via ARR，2026-05-25（明天）
- experimental_setup.tex 中 "three cross-family models" 应为 "four"（含 Falcon3），已标 warning 但截至本轮仍未修复
- Phi-4 per-seed 数据在 westd server，cqa1 无法直接验证——Figure 3 和 Figure 4 对 Phi-4 s123 数值不一致（见§4待办）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，远程代码根目录 `/root/contamcal-irt-calibration`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
- 论文源码：`docs/paper/`（main.tex 入口），图表脚本：`docs/paper/figures/` + `figures/paper/`
- 审计数据：`artifacts/data_audit_part3_crossseed_volume.md`（Phi-4/Gemma-2/OLMo-2 per-seed 数据标注 "westd only"）
- 活跃进程：无（registry 无 RUNNING 实验）
- 备份：3 个 tar.gz，共 7.8G；`/root/democalib/` 3.1G 非 git 数据仍在服务器上

### 3. 📊 当前状态
刚完成 Figure 3 (baseline_vulnerability) 重设计后的数据一致性审查。发现 3 处 cross-seed 数据错误（Phi-4/Falcon3/Qwen-7B）→ 已被 Agent 修复 → 我已复核确认修复正确。同时发现 Phi-4 跨图一致性问题（Fig3 vs Fig4 mean 不匹配）→ 已 post warning 给 Director。

registry: 433 总实验，无 RUNNING/PREPARING。项目处于论文提交最终阶段。

此前完成的审查：
- 全文 claim-data 一致性（PASS）
- ARC heatmap + domain gamma 修复复核（PASS）
- 匿名化 + 格式合规 + 补充材料 checklist（PASS，附 minor issues）

### 4. 📋 待办（条件触发式）
- Director 确认 Phi-4 s123 精确值 → 验证 Figure 3 range 上界（+1.83）和 Figure 4 mean（+0.50）哪个需修正。如 s123=+1.15 → Fig3 改 (-0.17, +1.15)；如 s123=+1.83 → Fig4 改 mean=+0.73
- Agent 修复 "three cross-family models" → "four" → 确认 experimental_setup.tex 更新
- 提交完成后 → 进入等待审稿状态，切换到 rebuttal 准备模式
- 收到 ARR reviewer comments → 加载 `rebuttal.skill.md`，逐条审查 reviewer 意见并辅助 response letter

### 5. 🎯 战略上下文
- 论文核心贡献：(1) dose-response taxonomy（Immune/Benefit/Collapse/V-recovery），(2) DiD 排除 item-level memorization，(3) ContamCal IRT 框架的 domain-level γ_d 分析
- Social Sciences γ_d < 0（99.7% posterior probability）是最强 domain-level finding；pooled γ 不显著是 dilution masking 的证据
- 最容易判断错的事：
  - Table 1 的 Phi-4 Δacc "±0.5pp" 是定性描述（≈0），不是精确数值——s42 实际是 -0.17pp
  - cross_seed_ranges（Figure 3）是 raw min/max of per-seed values，cross_seed CI（Figure 4）是 BCa bootstrap CI on the mean——两者概念不同，不能直接比较 bound
  - "86% (6/7)" ARC direction agreement 包含 LLaMA-3.1（7 families），不含 Falcon3 ARC（因为 Falcon3 ARC 在 main table 里不是 cross-benchmark 分析的一部分）——这个已验证正确但容易误查
  - Appendix F 的 internal label 仍为 `tab:s1_pipeline` / `tab:s1_domain`（未改），但对读者不可见（section ref 已改为 `sec:s2_only_pipeline`）——不需要修

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
前 24 轮 handoff 在 `task_context/history/reviewer/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-24T19:49:46.069966+00:00_

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
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
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

_source line 3 · 2026-05-24T19:49:46.171378+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T19:50:00.801434+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'status': 'RUNNING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'status': 'RUNNING'}"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T19:50:01.855796+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0328}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1054
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T19:50:05.024054+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'status': 'PREPARING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'status': 'PREPARING'}"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T19:50:06.028267+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_phi4_mmlu_arc_westd_v2\": {\"created_at\": \"2026-05-19T07:41:08.617Z\", \"hypothesis\": \"Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T17:16:34.577Z\", \"conclusion\": \"killed\"}, \"gsm8k_phi4_s42_westd\": {\"created_at\": \"2026-05-19T22:46:09.117Z\", \"hypothesis\": \"GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.\", \"parent\": \"gsm8k_qwen7b_s42_cqa1\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T17:16:32.968Z\", \"conclusion\": \"killed\"}, \"sft_gemma2_s0_sweep_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T09:48:50.562Z\", \"updated_at\": \"2026-05-22T17:16:31.256Z\", \"conclusion\": \"killed\"}, \"falcon3-7b-download\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:04:13.395Z\", \"updated_at\": \"2026-05-22T17:16:29.531Z\", \"conclusion\": \"killed\"}, \"falcon3-7b-dl-v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:05:00.669Z\", \"updated_at\": \"2026-05-22T17:16:27.904Z\", \"conclusion\": \"killed\"}, \"falcon3-7b-dl-v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:09:28.149Z\", \"updated_at\": \"2026-05-22T17:16:26.241Z\", \"conclusion\": \"killed\"}, \"falcon3-7b-dl-v4\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:11:14.996Z\", \"updated_at\": \"2026-05-22T17:16:24.550Z\", \"conclusion\": \"killed\"}, \"falcon3-7b-dl-v5\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:41:36.216Z\", \"updated_at\": \"2026-05-22T17:16:22.625Z\", \"conclusion\": \"killed\"}, \"prior_sensitivity_j16_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T18:13:16.179Z\", \"updated_at\": \"2026-05-21T18:13:16.179Z\"}, \"prior
…[truncated 10082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1004
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T19:50:15.557727+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T19:50:15.608417+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T19:50:18.973218+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"cross-family\" /root/contamcal-irt-calibration/docs/paper/sections/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"cross-family\" /root/contamcal-irt-calibration/docs/paper/sections/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T19:50:20.379295+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/contamcal-irt-calibration/docs/paper/sections/experimental_setup.tex: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1406
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T19:50:21.132847+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cross-family",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cross-family",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T19:50:21.233556+00:00_

&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/sections. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/reviewer_e442a828.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T19:50:25.656458+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/docs/paper -name \"experimental_setup.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/docs/paper -name \"experimental_setup.tex\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T19:50:25.907724+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/experimental_setup.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/experimental_setup.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T19:50:26.010497+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/contamcal-irt-calibration/docs/paper': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 354
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T19:50:26.111433+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "elapsed_ms": 203
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T19:50:28.831057+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cross-family",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cross-family",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T19:50:29.383863+00:00_

9:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T19:50:29.434451+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration -name \"experimental_setup.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration -name \"experimental_setup.tex\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T19:50:29.835723+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-24T19:50:34.358863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex",
  "offset": "5",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex",
    "offset": "5",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T19:50:34.459527+00:00_

5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning five independent model families from five labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), Gemma-2 \citep{gemmateam2024gemma2} (9B), and Falcon3 \citep{tiiuae2024falcon3} (7B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, dropout$=0$, targeting all attention and multilayer perceptron (MLP) projections; lr$=5\times10^{-5}$, bf16, 1 epoch, batch size$=1$, gradient accumulation$=16$, warmup ratio$=0.03$; trainable parameters range from 0.45\% of Phi-4 14.7B to 2.10\% of Qwen2.5-0.5B; convergence in Appendix~\ref{sec:training_convergence}) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus, yielding 50.0k (d000), 50.8k (d005), 54.1k (d025), 58.3k (d050), and 66.5k (d100) total training examples ($+$33\% volume at d100 vs.\ d000).
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The four cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 55 checkpoints spanning nine sizes across five families. We exclude 0.5B from multiple-choice (MC) IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}; details in Appendix~\ref{sec:exclusion_details}). We additionally validate our dose-response profiles on a held-out sixth family, LLaMA-3.1-8B \citep{grattafiori2024llama3} (Meta), which was not used during profile co
…[truncated 813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T19:50:43.497397+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/figures/**baseline_vulnerability*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/figures/**baseline_vulnerability*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-24T19:50:43.698486+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_baseline_vulnerability.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_baseline_vulnerability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_baseline_vulnerability.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T19:50:43.698866+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/figures/**cross_seed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/figures/**cross_seed*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T19:50:43.799472+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_cross_seed_ci.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_cross_seed_ci.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-24T19:50:47.462243+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Phi-4|phi.?4|phi4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_baseline_vulnerability.py",
  "output_mode": "content",
  "-i": "True",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Phi-4|phi.?4|phi4",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_baseline_vulnerability.py",
    "output_mode": "content",
    "-i": "True",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-24T19:50:47.864079+00:00_

51:    'Phi-4 14.7B':  (76.44, -0.17, 'Immune'),
61:    'Phi-4 14.7B':  (-0.17, +1.83),
70:    'Phi-4 14.7B':  (-12, 8),

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T19:50:47.914775+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/figures/*cross_seed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/figures/*cross_seed*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T19:50:47.965421+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_cross_seed_ci.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_cross_seed_ci.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T19:50:50.476184+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen_cross_seed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen_cross_seed*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T19:50:50.677490+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T19:51:09.487699+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/figures/gen_*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/figures/gen_*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T19:51:09.538530+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/gen_signal_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_cross_benchmark_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_baseline_vulnerability.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_fig_pipeline_v2.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-24T19:51:14.459766+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_baseline_vulnerability.py",
  "offset": "45",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_baseline_vulnerability.py",
    "offset": "45",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T19:51:14.510500+00:00_

45	
46	models = {
47	    'OLMo-2 7B':    (53.79, +3.21, 'Benefit'),
48	    'Falcon3 7B':   (58.77, +4.19, 'Benefit'),
49	    'Gemma-2 9B':   (61.86, +3.76, 'Benefit'),
50	    'Qwen2.5-7B':   (66.11, -1.78, 'V-recovery'),
51	    'Phi-4 14.7B':  (76.44, -0.17, 'Immune'),
52	    'Qwen2.5-14B':  (69.44, -9.37, 'Collapse'),
53	}
54	
55	# Cross-seed Δacc ranges (min, max) from per-seed eval results
56	cross_seed_ranges = {
57	    'OLMo-2 7B':    (-0.55, +3.21),
58	    'Falcon3 7B':   (+3.91, +4.19),
59	    'Gemma-2 9B':   (+1.49, +3.76),
60	    'Qwen2.5-7B':   (-1.78, -0.01),
61	    'Phi-4 14.7B':  (-0.17, +1.83),
62	    'Qwen2.5-14B':  (-25.03, -9.37),
63	}
64	
65	label_offsets = {
66	    'OLMo-2 7B':   (10, -2),
67	    'Falcon3 7B':   (10, 4),
68	    'Gemma-2 9B':   (10, -3),
69	    'Qwen2.5-7B':   (10, 6),
70	    'Phi-4 14.7B':  (-12, 8),
71	    'Qwen2.5-14B':  (10, 5),
72	}
73	
74	fig, ax = plt.subplots(figsize=(6.5, 3.8))
75	
76	# Background zones
77	ax.axhspan(0, 7, color='#2e86ab', alpha=0.04, zorder=0)
78	ax.axhspan(-27, 0, color='#c0392b', alpha=0.04, zorder=0)
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-24T19:51:19.679199+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Phi-4|phi.?4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "-i": "True",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Phi-4|phi.?4",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "output_mode": "content",
    "-i": "True",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-24T19:51:19.730713+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex:1:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:38:Phi-4 14.7B & 84.46 & --- & --- & --- & 85.60 & $+$1.14 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:345:Phi-4 14.7B & $-$0.27 & 1.25 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:363:Phi-4 14.7B & $-$0.83 & 2.28 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:397:The cross-benchmark consistency of the decomposition (MMLU 45\% vs.\ ARC 43\%) strengthens confidence in the estimate. Applying Falcon3's volume baseline to other patterns: Qwen-14B's Collapse ($-$9.4pp) against a $+$1.90pp volume baseline implies contamination-specific harm of approximately $-$11.3pp; Phi-4's Immune response ($<$1pp) in the presence of volume-driven gains further confirms that contamination vulnerability is family-specific rather than a generic data quantity effect.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:457:Phi-4 14.7B & Immune & 100\% & 82\% & $\tau < 0.35$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-cali
…[truncated 3016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T19:51:35.839973+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
  "offset": "90",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
    "offset": "90",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-24T19:51:37.295919+00:00_

90	\label{fig:cross_seed_ci}
91	\end{figure}
92	
93	\begin{table}[t]
94	\centering
95	\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 3/6; classification-level direction agreement is 5/6 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 3/6.}
96	\label{tab:cross_seed}
97	\footnotesize
98	\resizebox{\columnwidth}{!}{%
99	\begin{tabular}{lcccccccl}
100	\toprule
101	Model & $n$ & s42 & s123 & s0 & 95\% CI & Dir. & Cons.\ & Pattern\textsuperscript{$\ddagger$} \\
102	\midrule
103	Phi-4 & 3 & 0 & $+$ & 0 & [$-$0.17, $+$1.39]\textsuperscript{B} & Immune & $\times$ & --- \\
104	Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\textsuperscript{B} & Harm & \checkmark & Collapse \\
105	Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\textsuperscript{B} & Harm & $\times$ & V-recovery \\
106	Gemma-2 & 3 & $+$ & $+$ & $+$ & [$+$1.49, $+$3.14]\textsuperscript{B} & Benefit & \checkmark & Benefit \\
107	OLMo-2 & 3 & $+$ & 0 & $+$ & [$-$0.55, $+$2.60]\textsuperscript{B} & Borderl.\ & $\times$ & ---\textsuperscript{b} \\
108	Falcon3-7B & 2 & $+$ & $+$ & --- & [$+$3.91, $+$4.19]\textsuperscript{c} & Benefit & \checkmark & Benefit \\
109	\bottomrule
110	\multicolumn{9}{l}{\scriptsize \textsuperscript{B}BCa bootstrap ($B\!=\!10{,}000$); original five families at $n\!=\!3$.} \\
111	\multicolumn{9}{l}{\scriptsize \textsuperscript{$\ddagger$}Per-seed shape may differ from family-level direction-based classification (\S\ref{sec:classification}).} \\
112	\multicolumn{9}{l}{\scriptsize \textsuperscript{b}$+$/0/$+$ across seeds. Signs: $+$/$-$ = $|\Delta|{\ge}1$pp; $0$ = $|\Delta|{<}1$pp.} \\
113	\multicolumn{9}{l}{\scriptsize \textsuperscript{c}$n\!=\!2$ seeds only; range shown instead of BCa CI.}
114	\end{tabular}}
115	\end{table}
116	
117	Gemma-2 is the only family with a statistically significant cross-seed Benefit (BCa 95\% CI $[+1.49, +3.14]$; Figure~\ref{fig:cross_seed_ci}); Falcon3 and OLMo-2 are directionally c
…[truncated 187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 1455
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T19:51:38.249630+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cross.?seed|fig_cross_seed|Figure.*4|fig:cross",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
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
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cross.?seed|fig_cross_seed|Figure.*4|fig:cross",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-24T19:51:38.300234+00:00_

12:\caption{Baseline MMLU accuracy vs.\ contamination response at d100 ($N\!=\!6$). Vertical bars show cross-seed range ($n\!=\!2$--$3$ seeds). Shaded band marks the threshold region (61.9--66.1\%) separating Benefit from Harm patterns (observational, not validated; extended in Appendix~\ref{sec:baseline_vs_effect}).}
33:\multicolumn{8}{l}{\scriptsize $^{\ddagger}$Cross-seed range $-$9.4 to $-$25.0pp (s42/s123/s0); see Table~\ref{tab:cross_seed}.} \\
34:\multicolumn{8}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.55pp ($<$1pp threshold), s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.} \\
42:[Omitted long matching line]
54:\label{fig:cross_benchmark_heatmap}
83:\subsection{Cross-Seed Stability}
84:\label{sec:cross_seed}
88:\includegraphics[width=\columnwidth]{figures/fig_cross_seed_ci.pdf}
89:\caption{Cross-seed mean $\Delta$acc at d100 with bias-corrected and accelerated (BCa) bootstrap 95\% CIs ($n\!=\!3$ seeds; Falcon3 $n\!=\!2$). Filled markers: CI excludes zero.}
90:\label{fig:cross_seed_ci}
95:\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 3/6; classification-level direction agreement is 5/6 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 3/6.}
96:\label{tab:cross_seed}
112:\multicolumn{9}{l}{\scriptsize \textsuperscript{b}$+$/0/$+$ across seeds. Signs: $+$/$-$ = $|\Delta|{\ge}1$pp; $0$ = $|\Delta|{<}1$pp.} \\
117:Gemma-2 is the only family with a statistically significant cross-seed Benefit (BCa 95\% CI $[+1.49, +3.14]$; Figure~\ref{fig:cross_seed_ci}); Falcon3 and OLMo-2 are directionally consistent but exploratory (Table~\ref{tab:cross_seed}). Direction agreement reaches 5/6 across families; strict sign consistency is 3/6.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-24T19:52:03.603194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_part3_crossseed_volume.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_part3_crossseed_volume.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-24T19:52:03.653940+00:00_

1	# Data Audit Part 3 — Cross-seed, Volume Control, Appendix Tables
2	
3	Generated: 2026-05-23
4	Paper files: `docs/paper/results.tex`, `docs/paper/appendix.tex`
5	
6	---
7	
8	## A. §5.3 Cross-seed stability
9	
10	### A1. Main text claims (results.tex line 62)
11	
12	| Claim | Paper | Verified | 一致？ | 备注 |
13	|-------|-------|----------|--------|------|
14	| Direction agreement | 5/6 families | 5/6 (from appendix tab:cross_seed Dir. column: Immune, Harm, Harm, Benefit, **Borderl.**, Benefit) | ✅ | OLMo-2 is the ambiguous one |
15	| Strict sign consistency | 3/6 families | 3/6 (Qwen-14B ✓, Gemma-2 ✓, Falcon3 ✓) | ✅ | Matches Cons. column in tab:cross_seed |
16	| CI widths | 1.5–14.5pp | Calculated from BCa CIs: Qwen-7B 1.48pp (≈1.5), Qwen-14B 14.50pp | ✅ | Rounded |
17	
18	### A2. Appendix tab:cross_seed (appendix.tex lines 350–372)
19	
20	| Model | Seed | Paper sign | Source MMLU d000→d100 Δ | Calculated sign | 一致？ |
21	|-------|------|-----------|------------------------|----------------|--------|
22	| Qwen-7B | s42 | − | 66.14→64.32, Δ=−1.82pp | − (|Δ|≥1pp) | ✅ |
23	| Qwen-7B | s123 | 0 | 66.59→66.59, Δ=−0.01pp | 0 (|Δ|<1pp) | ✅ |
24	| Qwen-7B | s0 | − | 66.32→65.29, Δ=−1.03pp | − (|Δ|≥1pp) | ✅ |
25	| Qwen-7B | CI | [−1.82, −0.34] | Range of deltas: −1.82 to −0.01 | BCa bootstrap | ✅ plausible |
26	| Falcon3 | s42 | + | 58.77→62.96, Δ=+4.19pp | + | ✅ |
27	| Falcon3 | s123 | + | 58.77→62.68, Δ=+3.91pp | + | ✅ |
28	| Falcon3 | CI | [+3.91, +4.19] | Range = [+3.91, +4.19] | n=2, range not BCa | ✅ |
29	
30	Source files (cqa1):
31	- Qwen-7B s42: `/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d{000,100}_s42_v2/mmlu_results.json`
32	- Qwen-7B s0: `/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d{000,100}_s0/mmlu_results.json`
33	- Qwen-7B s123: `/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d{000,100}_s123/mmlu_results.json`
34	- Falcon3 d100 s42: `/root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_d100_s42_aligned/mmlu_results.json`
35	- Falcon3 d100 s123: `/root/co
…[truncated 2595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-24T19:52:07.573508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_part3_crossseed_volume.md",
  "offset": "80",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_part3_crossseed_volume.md",
    "offset": "80",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-24T19:52:07.624395+00:00_

80	|------|---------------|----------------------------------|--------|
81	| d000 MMLU | 58.77% | implicit (62.96 − 4.19 = 58.77) | ✅ |
82	| volctrl MMLU | 60.67% | 60.67% | ✅ |
83	| d100 MMLU | 62.96% | implicit | ✅ |
84	| d000 ARC | 81.57% | implicit | ✅ |
85	| volctrl ARC | 83.28% | implicit | ✅ |
86	| d100 ARC | 85.58% | implicit | ✅ |
87	| d000 GSM8K | 74.53% | implicit | ✅ |
88	| volctrl GSM8K | 75.21% | implicit | ✅ |
89	| d100 GSM8K | 75.82% | implicit | ✅ |
90	| vs d000 MMLU | +1.90 / +4.19pp | +1.90pp (45%) / +2.29pp (55%) of 4.19 | ✅ |
91	| vs d000 ARC | +1.71 / +4.01pp | 43%/57% split | ✅ |
92	| vs d000 GSM8K | +0.68 / +1.29pp | 53%/47% (+0.68/+0.61 of +1.29pp) | ✅ |
93	
94	**Appendix table and main text are fully consistent.**
95	
96	---
97	
98	## D. tab:gsm8k_transfer (appendix.tex lines 47–67)
99	
100	| Model | Paper MMLU Δ | Paper GSM8K Δ | Source MMLU Δ | Source GSM8K Δ | 一致？ |
101	|-------|-------------|--------------|--------------|---------------|--------|
102	| Phi-4 14.7B | ±0.5pp | −0.5pp | s42: 76.44→76.27=−0.17pp (within ±0.5) | s123: 84.31→83.85=−0.46pp→−0.5pp | ✅ MMLU seed-range matches; GSM8K from s123 |
103	| OLMo-2 7B | +3.2pp | +2.1pp§ | s42: westd registry 53.79→57.00=+3.21→+3.2pp | mean(s42:+1.7, s123:+2.4)=+2.1pp | ✅ |
104	| Falcon3 7B | +4.2pp | +1.3pp | s42: 58.77→62.96=+4.19→+4.2pp | s42: 74.53→75.82=+1.29→+1.3pp | ✅ |
105	| Qwen-7B | −1.8pp | +11.1pp | s42: 66.14→64.32=−1.82→−1.8pp | s42: 70.58→81.65=+11.07→+11.1pp | ✅ |
106	| Qwen-14B | −9.4pp | +13.1pp | s42: westd 69.44→60.07=−9.37→−9.4pp | mean(s42:+20.5, s123:+5.7)=+13.1pp | ✅ |
107	| LLaMA-3.1 8B | −0.7pp | +16.4pp‡ | westd: 53.50→52.81=−0.69→−0.7pp | s0: 38.74→55.12=+16.38→+16.4pp | ✅ |
108	
109	Source files verified on cqa1:
110	- Qwen-7B MMLU s42: `/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d{000,100}_s42_v2/mmlu_results.json` → 0.6614 / 0.6432
111	- Qwen-7B GSM8K s42: `/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d{000,100}_s42/gsm8k_results.json` → 0.7058 
…[truncated 1213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-24T19:52:11.543521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_part3_crossseed_volume.md",
  "offset": "138",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_part3_crossseed_volume.md",
    "offset": "138",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-24T19:52:11.594289+00:00_

138	### E2. Falcon3-7B (verified on cqa1 except d000)
139	
140	| Field | Paper | Source | 一致？ |
141	|-------|-------|--------|--------|
142	| n | 2 | 2 seeds (s42, s123) | ✅ |
143	| s42 | + | Δ=+4.19pp → + | ✅ |
144	| s123 | + | Δ=+3.91pp → + | ✅ |
145	| 95% CI | [+3.91, +4.19] | Range of 2 values = [3.91, 4.19] | ✅ |
146	| Dir. | Benefit | Both positive → Benefit | ✅ |
147	| Cons. | ✓ | Both + | ✅ |
148	
149	### E3. Phi-4 (westd registry, not directly verified)
150	
151	| Field | Paper | Registry source | 一致？ |
152	|-------|-------|----------------|--------|
153	| n | 3 | 3 seeds (s42, s123, s0) | ✅ |
154	| s42 | 0 | 76.44→76.27=−0.17pp, |Δ|<1 → 0 | ✅ |
155	| s123 | + | 76.31→78.14=+1.83pp, |Δ|≥1 → + | ✅ |
156	| s0 | 0 | 76.43→76.95=+0.52pp, |Δ|<1 → 0 | ✅ |
157	| 95% CI | [−0.17, +1.39] | BCa on {−0.17, +1.83, +0.52} | ✅ plausible |
158	| Dir. | Immune | 2/3 within ±1pp → Immune | ✅ |
159	
160	---
161	
162	## F. tab:gsm8k_dose (appendix.tex lines 99–113)
163	
164	All values seed=0.
165	
166	### F1. Qwen2.5-7B (fully verified on cqa1)
167	
168	| Dosage | Paper | Source file accuracy | Calculated % | 一致？ |
169	|--------|-------|---------------------|-------------|--------|
170	| d000 | 73.31 | 0.733131159969674 | 73.31% | ✅ |
171	| d005 | 78.32 | 0.7831690674753601 | 78.32% | ✅ |
172	| d025 | 78.24 | 0.7824109173616376 | 78.24% | ✅ |
173	| d050 | 79.38 | 0.7937831690674754 | 79.38% | ✅ |
174	| d100 | 81.20 | 0.8119787717968158 | 81.20% | ✅ |
175	| Δ | +7.89 | 81.20−73.31=7.89 | +7.89 | ✅ |
176	
177	Source: `/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d{000,005,025,050,100}_s0/gsm8k_results.json`
178	
179	### F2. Phi-4 14.7B (westd registry)
180	
181	| Dosage | Paper | Registry | 一致？ |
182	|--------|-------|----------|--------|
183	| d000 | 84.46 | 84.46% (westd) | ✅ (not directly verified) |
184	| d100 | 85.60 | 85.60% (westd) | ✅ (not directly verified) |
185	| Δ | +1.14 | 85.60−84.46=1.14 | ✅ |
186	
187	### F3. Qwen2.5-14B (westd registry)
188	
189	| Dosage | Pa
…[truncated 494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-24T19:52:29.382520+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cross_seed_ci",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "glob": "*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cross_seed_ci",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
    "glob": "*.py"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-24T19:52:29.583953+00:00_

Found 2 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci_v3.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-24T19:52:33.152715+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Phi|phi",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci_v3.py",
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
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Phi|phi",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci_v3.py",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-24T19:52:33.253404+00:00_

37:    ('Phi-4 14.7B',  'Immune',     +0.73,  -0.17,  +1.39,  False),

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-24T19:52:36.970363+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Phi|phi",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci.py",
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
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Phi|phi",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci.py",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-24T19:52:37.071203+00:00_

48:    ('Phi-4 14.7B',  'Immune',     +0.73,  -0.17,  +1.39,  False),

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-24T19:52:45.415992+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_cross_seed_ci.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci_v3.py /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci.py",
  "description": "Compare timestamps of figure PDF vs generation scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_cross_seed_ci.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci_v3.py /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci.py",
    "description": "Compare timestamps of figure PDF vs generation scripts"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-24T19:52:45.619056+00:00_

-rw-r--r-- 1 ubuntu ubuntu 24048 May 24 11:31 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/fig_cross_seed_ci.pdf
-rw-r--r-- 1 ubuntu ubuntu  4368 May 24 11:18 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci.py
-rw-r--r-- 1 ubuntu ubuntu  6308 May 24 11:31 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci_v3.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-24T19:53:05.576079+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper -name \"*.tex\" -newer /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_part3_crossseed_volume.md -type f | sort",
  "description": "Find tex files modified after last audit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper -name \"*.tex\" -newer /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_part3_crossseed_volume.md -type f | sort",
    "description": "Find tex files modified after last audit"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-24T19:53:05.728226+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-24T19:53:05.829062+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\begin\\{abstract\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\begin\\{abstract\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-24T19:53:05.879975+00:00_

Found 1 file
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-24T19:53:09.949883+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-24T19:53:10.453057+00:00_

1	Benchmark contamination is widely assumed to inflate language model scores, yet its actual effect has never been measured across model families. We perform controlled supervised fine-tuning (SFT) injection at five dosage levels into six models (7B--14.7B) from five open-source families and discover a spectrum of dose-response patterns, not uniform inflation. Two patterns replicate across independent families: Immune (Phi-4, LLaMA-3.1) and Benefit (statistically significant for Gemma-2, bootstrap 95\% CI [$+$1.49, $+$3.14]\,pp; borderline for OLMo-2 and Falcon3). Collapse and V-recovery are each observed in one family (Qwen2.5) across three seeds but remain preliminary pending independent replication. Effects are benchmark-conditional: MMLU-targeted contamination improves GSM8K in five of six families, even those harmed on MMLU. Difference-in-differences analysis detects no item-specific memorization; a volume-matched control attributes 45\% of Benefit to data quantity. ContamCal, our diagnostic framework combining multi-signal exposure mapping with contamination-augmented Item Response Theory (IRT), enables domain-level contamination diagnosis with credible intervals---revealing that Social Sciences contamination effects are negative while STEM effects are positive, a pattern invisible to aggregate scoring. Out-of-sample validation on LLaMA-3.1-8B confirms that model family characteristics beyond baseline ability modulate vulnerability. Model-specific dose-response profiling is necessary for reliable benchmark interpretation.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-24T19:53:10.453518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T19:53:10.956478+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use models $\leq$14.7B with $n\!=\!3$ seeds; 70B+ models may exhibit different contamination dynamics, and borderline classifications (e.g., OLMo-2) should be interpreted with caution. Our LoRA-based SFT injection differs from pretraining-stage leakage; the AUGMENT protocol increases training volume with dosage ($+$33\% at d100), partially confounding content and quantity effects. IRT is fitted on 300 subsampled items (2.1\% of MMLU), and RRF exposure scores are point estimates whose measurement uncertainty is not propagated into $\gamma$ credible intervals.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-24T19:53:10.956974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T19:53:11.107552+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-24T19:53:13.407790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-24T19:53:15.102631+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (0). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 1694
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-24T19:53:15.504406+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$%\\\\]//g; s/\\[.*\\]//g' | wc -w",
  "description": "Count words in abstract (stripped of LaTeX commands)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$%\\\\]//g; s/\\[.*\\]//g' | wc -w",
    "description": "Count words in abstract (stripped of LaTeX commands)"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-24T19:53:15.605464+00:00_

188

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-24T19:53:32.768473+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "three.*(cross-family|families|model|lower|benefit|gain)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "three.*(cross-family|families|model|lower|benefit|gain)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-24T19:53:32.819244+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex:7:\caption{ContamCal three-stage pipeline. Stage~1 fuses training-free detection signals into per-item exposure scores via Reciprocal Rank Fusion. Stage~2 embeds these scores in a contamination-augmented 2PL IRT model, recovering clean ability estimates with credible intervals. Stage~3 classifies the resulting dose-response trajectories into canonical patterns.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex:11:ContamCal operates in three stages (Figure~\ref{fig:pipeline}): Stage~1 estimates per-item contamination exposure via training-free signal fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to recover clean ability estimates with credible intervals; Stage~3 classifies dose-response trajectories into canonical patterns.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex:1:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:254:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex:9:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex:5:We perform controlled supervised fine-tuning (SFT) injection (Low-Rank Adaptation [LoRA], five dosage levels) 
…[truncated 1356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-24T19:53:44.979728+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
  "offset": "38",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
    "offset": "38",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-24T19:53:45.281088+00:00_

38	
39	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields a spectrum of dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. Figure~\ref{fig:baseline_vulnerability} visualizes how contamination response correlates with baseline accuracy across families.
40	
41	\paragraph{Replication status.}
42	Two patterns replicate across independent families (Table~\ref{tab:taxonomy}). \textit{Immune}: Phi-4 ($\pm$0.5pp), confirmed out-of-sample by LLaMA-3.1 ($-$0.69pp). \textit{Benefit}: three families gain $+$3.2 to $+$4.2pp (Gemma-2, Falcon3, OLMo-2 borderline; \S\ref{sec:cross_seed}). Two patterns are Qwen2.5-specific and await independent replication: Qwen-14B \textit{collapses} ($-$9.4 to $-$25.0pp across seeds) while Qwen-7B shows \textit{V-recovery}. ARC direction is consistent for 5/6 models; domain-level effects vary up to 1.8$\times$ (Appendices~\ref{sec:arc_cross_benchmark},~\ref{sec:domain_decomposition}).
43	
44	\paragraph{Out-of-sample validation.}
45	LLaMA-3.1-8B (Meta; d000, d025, d100) is classified Immune on both MMLU ($-$0.69pp) and ARC ($+$0.09pp), despite matching OLMo-2's Benefit baseline (53.5\% vs.\ 53.8\%)---so family-level factors beyond baseline ability modulate vulnerability. LLaMA-3.1 also shows the strongest GSM8K transfer ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}): target-benchmark immunity does not imply transfer immunity.
46	
47	\subsection{Cross-Benchmark Transfer}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-24T19:53:45.632420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
  "offset": "78",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
    "offset": "78",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-24T19:53:45.733181+00:00_

78	\end{tabular}}
79	\end{table}
80	
81	Contamination patterns are a property of the (model, benchmark) pair, not the model alone. Within-MC direction agreement is 86\% (6/7 families; Appendix~\ref{sec:arc_cross_benchmark}); across formats (MC$\to$generative math), agreement drops to 50\% with three families reversing on GSM8K \citep{cobbe2021gsm8k} (Table~\ref{tab:gsm8k_transfer}). Qwen-14B ($-$9.4pp MMLU) gains $+$13.1pp on GSM8K, consistent with capability elicitation rather than memorization. Volume effects are ruled out: d005 ($+$1.5\% data) already yields $+$6.4pp GSM8K transfer for Qwen-7B.
82	
83	\subsection{Cross-Seed Stability}
84	\label{sec:cross_seed}
85	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-24T19:54:06.446802+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "github\\.com|huggingface\\.co/[a-zA-Z]|our lab|our group|university of|our institution",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "github\\.com|huggingface\\.co/[a-zA-Z]|our lab|our group|university of|our institution",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-24T19:54:06.849720+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex:23:\noindent Code and data are available at \url{https://github.com/anonymous-nlp-2026-2/contamcal-irt-calibration}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-24T19:54:07.000499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-24T19:54:07.051205+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{float}
15	\usepackage{alphalph}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning,shapes.geometric}
18	
19	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	\input{introduction}
31	\input{related_work}
32	\input{method}
33	\input{experimental_setup}
34	\input{results}
35	\input{conclusion}
36	
37	\input{limitations}
38	\input{ethics}
39	
40	\bibliography{references}
41	
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-24T19:54:18.225367+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "limitation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
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
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "tool_args": {
    "pattern": "limitation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-24T19:54:18.226283+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-24T19:54:22.196508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-24T19:54:22.297575+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models (LLMs), yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled supervised fine-tuning (SFT) injection (Low-Rank Adaptation [LoRA], five dosage levels) into six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII) and discover a spectrum of dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4, $\pm$0.5pp) and benefit ($+$3--4pp, three families) to collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/fig_dose_response.pdf}
10	\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; LLaMA-3.1 at seed$=$0). Immune and Benefit replicate across families; Collapse and V-recovery are preliminary (Qwen2.5-specific). Cross-seed stability in Table~\ref{tab:cross_seed}.}
11	\label{fig:dose_response}
12	\end{figure}
13	
14	Across six models, three lower-baseline models benefit ($+$3.2 to $+$4.2pp), one is immune (Phi-4), and the remaining two (both Qwen2.5) show harm---with the 14B model 5$\times$ more fragile than 7B. These effects are benchmark-conditional: the same model can collapse on MMLU ($-$9.4pp) yet gain on GSM8K ($+$13pp). ContamCal, our diagnostic f
…[truncated 1957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-24T19:54:49.445705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
  "offset": "55",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
    "offset": "55",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-24T19:54:49.496397+00:00_

55	\end{figure}
56	
57	\begin{table}[t]
58	\centering
59	\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
60	\label{tab:gsm8k_transfer}
61	\footnotesize
62	\resizebox{\columnwidth}{!}{%
63	\begin{tabular}{lcccl}
64	\toprule
65	Model & MMLU $\Delta$ & GSM8K $\Delta$ & Range & Transfer \\
66	\midrule
67	Phi-4 14.7B & $\pm$0.5pp & $-$0.5pp$^{\diamond}$ & --- & Null \\
68	OLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\S}$ & --- & Consistent \\
69	Falcon3 7B & $+$4.2pp & $+$1.3pp & --- & Consistent \\
70	Qwen-7B & $-$1.8pp & $+$10.1pp & $\pm$0.9 & Reversal \\
71	Qwen-14B & $-$9.4pp & $+$13.1pp & $\pm$7.4 & Reversal$^{\dagger}$ \\
72	LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
73	\bottomrule
74	\multicolumn{5}{l}{\scriptsize $^{\dagger}$d000 baseline seed-sensitive (s42$=$60.8\% vs.\ s123$=$76.7\%); d100 stable ($82\pm0.5$\%).} \\
75	\multicolumn{5}{l}{\scriptsize $^{\S}$Mean of s42 and s123: $+$2.1pp (s42: $+$1.7pp, s123: $+$2.4pp); s0 excluded ($+$9.2pp outlier).} \\
76	\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.} \\
77	\multicolumn{5}{l}{\scriptsize $^{\diamond}$Seed s123; Table~\ref{tab:gsm8k_dose} reports s0 ($+$1.14pp).}
78	\end{tabular}}
79	\end{table}
80	
81	Contamination patterns are a property of the (model, benchmark) pair, not the model alone. Within-MC direction agreement is 86\% (6/7 families; Appendix~\ref{sec:arc_cross_benchmark}); across formats (MC$\to$generative math), agreement drops to 50\% with three families reversing on GSM8K \citep{cobbe2021gsm8k} (Table~\ref{tab:gsm8k_transfer}). Qwen-14B ($-$9.4pp MMLU) gains $+$13.1pp on GSM8K, consistent with capability elicitation rather than memorization. Volume effects are ruled out: d005 ($+$1.5\% data) already yields $+$6.4pp GSM8K transf
…[truncated 82 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-24T19:55:54.400485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d000_s42/gsm8k_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d000_s42/gsm8k_results.json"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-24T19:55:54.902151+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d100_s42/gsm8k_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d100_s42/gsm8k_results.json"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-24T19:55:55.003460+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"gsm8k\\\",\\n  \\\"accuracy\\\": 0.7058377558756633,\\n  \\\"correct\\\": 931,\\n  \\\"total\\\": 1319,\\n  \\\"per_item\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"18\\\",\\n      \\\"gold\\\": \\\"18\\\"\\n    },\\n    {\\n      \\\"index\\\": 1,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"3\\\",\\n      \\\"gold\\\": \\\"3\\\"\\n    },\\n    {\\n      \\\"index\\\": 2,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"130\\\",\\n      \\\"gold\\\": \\\"70000\\\"\\n    },\\n    {\\n      \\\"index\\\": 3,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"540\\\",\\n      \\\"gold\\\": \\\"540\\\"\\n    },\\n    {\\n      \\\"index\\\": 4,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"40\\\",\\n      \\\"gold\\\": \\\"20\\\"\\n    },\\n    {\\n      \\\"index\\\": 5,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"64\\\",\\n      \\\"gold\\\": \\\"64\\\"\\n    },\\n    {\\n      \\\"index\\\": 6,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"260\\\",\\n      \\\"gold\\\": \\\"260\\\"\\n    },\\n    {\\n      \\\"index\\\": 7,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"60\\\",\\n      \\\"gold\\\": \\\"160\\\"\\n    },\\n    {\\n      \\\"index\\\": 8,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"15\\\",\\n      \\\"gold\\\": \\\"45\\\"\\n    },\\n    {\\n      \\\"index\\\": 9,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"460\\\",\\n      \\\"gold\\\": \\\"460\\\"\\n    },\\n    {\\n      \\\"index\\\": 10,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"366\\\",\\n      \\\"gold\\\": \\\"366\\\"\\n    },\\n    {\\n      \\\"index\\\": 11,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"10\\\",\\n      \\\"gold\\\": \\\"694\\\"\\n    },\\n    {\\n      \\\"index\\\": 12,\\n      \\\"correct\\\": false,\\n      \
…[truncated 10215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 602
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-24T19:55:55.509595+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"gsm8k\\\",\\n  \\\"accuracy\\\": 0.8165276724791509,\\n  \\\"correct\\\": 1077,\\n  \\\"total\\\": 1319,\\n  \\\"per_item\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"18\\\",\\n      \\\"gold\\\": \\\"18\\\"\\n    },\\n    {\\n      \\\"index\\\": 1,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"3\\\",\\n      \\\"gold\\\": \\\"3\\\"\\n    },\\n    {\\n      \\\"index\\\": 2,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"130000\\\",\\n      \\\"gold\\\": \\\"70000\\\"\\n    },\\n    {\\n      \\\"index\\\": 3,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"540\\\",\\n      \\\"gold\\\": \\\"540\\\"\\n    },\\n    {\\n      \\\"index\\\": 4,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"20\\\",\\n      \\\"gold\\\": \\\"20\\\"\\n    },\\n    {\\n      \\\"index\\\": 5,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"64\\\",\\n      \\\"gold\\\": \\\"64\\\"\\n    },\\n    {\\n      \\\"index\\\": 6,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"260\\\",\\n      \\\"gold\\\": \\\"260\\\"\\n    },\\n    {\\n      \\\"index\\\": 7,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"16\\\",\\n      \\\"gold\\\": \\\"160\\\"\\n    },\\n    {\\n      \\\"index\\\": 8,\\n      \\\"correct\\\": false,\\n      \\\"pred\\\": \\\"315\\\",\\n      \\\"gold\\\": \\\"45\\\"\\n    },\\n    {\\n      \\\"index\\\": 9,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"460\\\",\\n      \\\"gold\\\": \\\"460\\\"\\n    },\\n    {\\n      \\\"index\\\": 10,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"366\\\",\\n      \\\"gold\\\": \\\"366\\\"\\n    },\\n    {\\n      \\\"index\\\": 11,\\n      \\\"correct\\\": true,\\n      \\\"pred\\\": \\\"694\\\",\\n      \\\"gold\\\": \\\"694\\\"\\n    },\\n    {\\n      \\\"index\\\": 12,\\n      \\\"correct\\\": false,\\n   
…[truncated 10212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 607
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-24T19:56:37.187233+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root -path \"*/qwen7b*d005*gsm8k*\" -name \"gsm8k_results.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root -path \"*/qwen7b*d005*gsm8k*\" -name \"gsm8k_results.json\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-24T19:56:37.338106+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root -path \"*/qwen7b*gsm8k*d005*\" -name \"gsm8k_results.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root -path \"*/qwen7b*gsm8k*d005*\" -name \"gsm8k_results.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-24T19:56:38.191938+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d005_s0/gsm8k_results.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d005_s42/gsm8k_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1004
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-24T19:56:39.096778+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1758
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-24T19:56:41.608740+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -5 /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d005_s42/gsm8k_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -5 /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d005_s42/gsm8k_results.json"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-24T19:56:41.960154+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"gsm8k\\\",\\n  \\\"accuracy\\\": 0.7695223654283548,\\n  \\\"correct\\\": 1015,\\n  \\\"total\\\": 1319,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-24T19:56:55.102239+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root -path \"*qwen7b*d100*\" -name \"gsm8k_results.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root -path \"*qwen7b*d100*\" -name \"gsm8k_results.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-24T19:56:55.906625+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d100_s0/gsm8k_results.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d100_s42/gsm8k_results.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d100_s123/gsm8k_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.82}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 804
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-24T19:57:02.644021+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -5 /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d100_s123/gsm8k_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -5 /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d100_s123/gsm8k_results.json"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-24T19:57:03.046161+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"gsm8k\\\",\\n  \\\"accuracy\\\": 0.7922668688400303,\\n  \\\"correct\\\": 1045,\\n  \\\"total\\\": 1319,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-24T19:57:03.046580+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root -path \"*qwen7b*d000*\" -name \"gsm8k_results.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root -path \"*qwen7b*d000*\" -name \"gsm8k_results.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-24T19:57:03.949571+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d000_s0/gsm8k_results.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d000_s42/gsm8k_results.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d000_s123/gsm8k_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.88}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 902
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-24T19:57:06.210983+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -5 /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d000_s123/gsm8k_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -5 /root/contamcal-irt-calibration/results/gsm8k/qwen7b_d000_s123/gsm8k_results.json"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-24T19:57:06.612830+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"gsm8k\\\",\\n  \\\"accuracy\\\": 0.7005307050796058,\\n  \\\"correct\\\": 924,\\n  \\\"total\\\": 1319,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-24T19:58:04.023771+00:00_

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
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
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

_source line 107 · 2026-05-24T19:58:04.075506+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-24T19:58:28.930417+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "## 审查报告 — Loop #26 最终提交前检查\n\n### 已解决的待办\n\n1. ✅ **\"three→four\" 已修复**：`experimental_setup.tex` 第9行现为 \"The four cross-family models\"，正确。\n\n2. ✅ **Phi-4 跨图一致性已修复**：\n   - Figure 3 (baseline_vulnerability): range = (-0.17, +1.83)，对应 s42=-0.17, s123=+1.83 ✓\n   - Figure 4 (cross_seed_ci): mean = +0.73, CI = [-0.17, +1.39]，与 per-seed 数据 {-0.17, +1.83, +0.52} 的 BCa bootstrap 一致 ✓\n   - v3 脚本时间戳 (11:31) = PDF 时间戳 (11:31)，确认从正确脚本生成 ✓\n\n### EMNLP 合规检查\n\n- [severity: info] Abstract 188 words (< 200 限制) ✓\n- [severity: info] Limitations: 主文一段，覆盖 3 点（模型规模/注入方式/IRT 子采样），appendix 无重复 ✓\n- [severity: info] 匿名化正确：author=\"Anonymous\"，GitHub URL 匿名化 ✓\n- [severity: info] ACL review 模式 (`\\usepackage[review,hyperref]{acl}`) ✓\n\n### 新发现\n\n- [severity: warning] **Table 2 (tab:gsm8k_transfer) Qwen-7B GSM8K Δ 缺少 s0 排除脚注**\n\n  Table 2 Qwen-7B GSM8K 写的 +10.1pp，经原始文件验证是 mean(s42=+11.07, s123=+9.18) = +10.13pp，排除了 s0=+7.89pp。\n\n  问题：OLMo-2 排除 s0 有显式脚注 (\"s0 excluded (+9.2pp outlier)\")，但 Qwen-7B 没有。而且 Qwen-7B s0 (+7.89) 并不像 OLMo-2 s0 (+9.2 vs mean 2.05) 那样是明显离群值——它只是三个 seed 中最低的。\n\n  如果用三 seed mean，应为 +9.38pp（而非 +10.1pp）。排除最低值而不注明，可能被审稿人质疑为选择性报告。\n\n  原始数据（均从 cqa1 JSON 验证）：\n  - s42: d000=70.58% → d100=81.65%, Δ=+11.07pp\n  - s123: d000=70.05% → d100=79.23%, Δ=+9.18pp  \n  - s0: d000=73.31% → d100=81.20%, Δ=+7.89pp\n\n  **建议**：(a) 加脚注说明 s0 被排除及原因，或 (b) 改用三 seed mean (+9.4pp)，或 (c) 改回 s42 单 seed (+11.1pp) 与 MMLU 列保持同 seed 一致。Range 列相应调整。\n\n- [severity: info] \"+6.4pp GSM8K transfer for Qwen-7B at d005\" (results.tex:81) 验证正确：s42 d005=76.95% - d000=70.58% = +6.37pp ≈ +6.4pp ✓\n\n### 结论\n\n**PASS（附 1 warning）**。DDL 明天，唯一待修项是 Table 2 Qwen-7B GSM8K 的 seed 透明性。建议在提交前加一个脚注或统一 seed 选择逻辑。",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "## 审查报告 — Loop #26 最终提交前检查\n\n### 已解决的待办\n\n1. ✅ **\"three→four\" 已修复**：`experimental_setup.tex` 第9行现为 \"The four cross-family models\"，正确。\n\n2. ✅ **Phi-4 跨图一致性已修复**：\n   - Figure 3 (baseline_vulnerability): range = (-0.17, +1.83)，对应 s42=-0.17, s123=+1.83 ✓\n   - Figure 4 (cross_seed_ci): mean = +0.73, CI = [-0.17, +1.39]，与 per-seed 数据 {-0.17, +1.83, +0.52} 的 BCa bootstrap 一致 ✓\n   - v3 脚本时间戳 (11:31) = PDF 时间戳 (11:31)，确认从正确脚本生成 ✓\n\n### EMNLP 合规检查\n\n- [severity: info] Abstract 188 words (< 200 限制) ✓\n- [severity: info] Limitations: 主文一段，覆盖 3 点（模型规模/注入方式/IRT 子采样），appendix 无重复 ✓\n- [severity: info] 匿名化正确：author=\"Anonymous\"，GitHub URL 匿名化 ✓\n- [severity: info] ACL review 模式 (`\\usepackage[review,hyperref]{acl}`) ✓\n\n### 新发现\n\n- [severity: warning] **Table 2 (tab:gsm8k_transfer) Qwen-7B GSM8K Δ 缺少 s0 排除脚注**\n\n  Table 2 Qwen-7B GSM8K 写的 +10.1pp，经原始文件验证是 mean(s42=+11.07, s123=+9.18) = +10.13pp，排除了 s0=+7.89pp。\n\n  问题：OLMo-2 排除 s0 有显式脚注 (\"s0 excluded (+9.2pp outlier)\")，但 Qwen-7B 没有。而且 Qwen-7B s0 (+7.89) 并不像 OLMo-2 s0 (+9.2 vs mean 2.05) 那样是明显离群值——它只是三个 seed 中最低的。\n\n  如果用三 seed mean，应为 +9.38pp（而非 +10.1pp）。排除最低值而不注明，可能被审稿人质疑为选择性报告。\n\n  原始数据（均从 cqa1 JSON 验证）：\n  - s42: d000=70.58% → d100=81.65%, Δ=+11.07pp\n  - s123: d000=70.05% → d100=79.23%, Δ=+9.18pp  \n  - s0: d000=73.31% → d100=81.20%, Δ=+7.89pp\n\n  **建议**：(a) 加脚注说明 s0 被排除及原因，或 (b) 改用三 seed mean (+9.4pp)，或 (c) 改回 s42 单 seed (+11.1pp) 与 MMLU 列保持同 seed 一致。Range 列相应调整。\n\n- [severity: info] \"+6.4pp GSM8K transfer for Qwen-7B at d005\" (results.tex:81) 验证正确：s42 d005=76.95% - d000=70.58% = +6.37pp ≈ +6.4pp ✓\n\n### 结论\n\n**PASS（附 1 warning）**。DDL 明天，唯一待修项是 Table 2 Qwen-7B GSM8K 的 seed 透明性。建议在提交前加一个脚注或统一 seed 选择逻辑。",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-24T19:58:32.493002+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 3562
}
```

</details>

---

### Assistant

_source line 110 · 2026-05-24T19:58:38.416868+00:00_

已提交审查报告。总结：

- 两个历史待办（"three→four"、Phi-4 跨图一致性）均已确认修复
- EMNLP 合规项全部通过（abstract 字数、limitations、匿名化、格式）
- 发现 1 个新 warning：Table 2 Qwen-7B GSM8K +10.1pp 是 mean(s42, s123) 但排除了 s0 且无脚注说明，建议提交前补脚注或统一 seed 选择

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 111 · 2026-05-25T06:12:27.340056+00:00_

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
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 112 · 2026-05-25T06:13:07.371617+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-21977，项目 gpu_ids 需从 constraints.yaml 确认（2026-04-24 有越界事故）
- 论文 DDL: EMNLP 2026 via ARR，2026-05-25（今天）
- Phi-4/Gemma-2/OLMo-2 per-seed 原始数据在 westd server，cqa1 无法直接验证——但 Qwen-7B 三 seed GSM8K 数据已在 cqa1 验证完毕
- Table 2 Qwen-7B GSM8K Δ=+10.1pp 是 mean(s42, s123)，排除了 s0=+7.89pp 但无脚注——已 post warning 给 Director，等回复决定是加脚注/改值/保留

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，远程代码根目录 `/root/contamcal-irt-calibration`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
- 论文源码：`docs/paper/`（main.tex 入口），图表脚本：`docs/paper/figures/` + `figures/paper/`
- 审计数据：`artifacts/data_audit_part3_crossseed_volume.md`
- 活跃进程：无（registry 0 RUNNING，42 PREPARING 全部 killed/failed/stale）
- 备份：3 个 tar.gz 共 7.8G；`/root/democalib/` 3.1G 非 git 数据仍在服务器

### 3. 📊 当前状态
刚完成 Loop #26 最终提交前全面检查，已 post 审查报告给 Director。

确认已修复：
- "three→four cross-family models"（experimental_setup.tex:9）✅
- Phi-4 跨图一致性（Fig3 range=(-0.17,+1.83), Fig4 mean=+0.73, CI=[-0.17,+1.39]）✅

确认合规：Abstract 188 words, Limitations 1段3点, 匿名化正确, ACL review mode ✅

新发现 1 warning：Table 2 Qwen-7B GSM8K s0 排除无脚注（已 post Director）

registry: 433 总实验，0 RUNNING/活跃。项目在最终提交阶段。

### 4. 📋 待办（条件触发式）
- Director 回复 Table 2 Qwen-7B warning → 确认修复方案（加脚注/改值/保留）→ 验证修改
- 提交完成 → 进入等待审稿状态，切换到 rebuttal 准备模式
- 收到 ARR reviewer comments → 加载 `rebuttal.skill.md`，逐条审查 reviewer 意见并辅助 response letter
- Appendix F internal label (`tab:s1_pipeline` / `tab:s1_domain`) 对读者不可见，不需要修

### 5. 🎯 战略上下文
- 论文核心贡献：(1) dose-response taxonomy（Immune/Benefit/Collapse/V-recovery），(2) DiD 排除 item-level memorization，(3) ContamCal IRT 框架的 domain-level γ_d 分析
- Social Sciences γ_d < 0（99.7% posterior probability）是最强 domain-level finding；pooled γ 不显著是 dilution masking 的证据
- 最容易判断错的事：
  - Table 1 的 Phi-4 Δacc "±0.5pp" 是定性描述（≈0），不是精确数值——s42 实际是 -0.17pp
  - cross_seed_ranges（Figure 3）是 raw min/max，cross_seed CI（Figure 4）是 BCa bootstrap CI on the mean——概念不同，不能直接比较 bound
  - Table 2 GSM8K 列各模型 seed 选择不统一：有的用 s42，有的用 mean(s42,s123) 排除 s0——OLMo-2 有脚注，Qwen-7B 没有。Qwen-7B 的 s0 (+7.89pp) 不是明显 outlier（不像 OLMo-2 s0 +9.2pp vs mean 2.05pp），排除缺乏明确 justification
  - "86% (6/7)" ARC direction agreement 包含 LLaMA-3.1，不含 Falcon3 ARC——这已验证正确但容易误查
  - Qwen-7B d005 GSM8K "+6.4pp" 用的是 s42（已验证：76.95-70.58=6.37pp），正确
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_a79563aecf81c0da6bbb0710df2f0b6d:reviewer"
}
```

</details>

---
