# ops westb disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_ops_westb_disk_cleanup_20260519T101715.jsonl`
- **Structured JSON:** [`0b3428ffefc0e51765a4.json`](../../sessions/0b/0b3428ffefc0e51765a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-19T10:18:52.255403+00:00_

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
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
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

_source line 2 · 2026-05-19T10:18:52.255753+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T10:18:52.255912+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "df -h /autodl-pub",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "df -h /autodl-pub",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T10:18:52.256044+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -sh /root/autodl-pub/recovery_aware_struct_prune/*/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -sh /root/autodl-pub/recovery_aware_struct_prune/*/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T10:18:52.256173+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\n/dev/md0         14T  7.5T  6.6T  54% /autodl-pub\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T10:18:52.256347+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"du: cannot access '/root/autodl-pub/recovery_aware_struct_prune/*/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T10:18:52.256526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "df -h /root/autodl-tmp",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "df -h /root/autodl-tmp",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T10:18:52.256654+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T10:18:52.256783+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\n/dev/md0        250G  227G   24G  91% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T10:18:52.256941+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"artifacts\\ncka_scores_1p5b.pt\\neval_results\\neval_sft_standard_20_n100.json\\ngrpo_cka_only_20\\ngrpo_cka_only_20_1p5b\\ngrpo_cka_only_20_seed123\\ngrpo_random_20\\ngrpo_rasp_20_1p5b\\ngrpo_rasp_25\\ngrpo_rasp_rlvr_20.log\\ngrpo_standard_20_1p5b\\ngrpo_standard_25.log\\nimportance_scores_1p5b.pt\\nlog_e1b_pipeline.txt\\nlog_importance_1p5b.txt\\nlogs\\nmodels\\npruned_cka_only_20\\npruned_cka_only_20_1p5b\\npruned_random_20\\npruned_rasp_20\\npruned_rasp_20_1p5b\\npruned_rasp_25\\npruned_rasp_rlvr_20\\npruned_standard_20\\npruned_standard_20_1p5b\\npruned_standard_25\\npruned_unstructured_20\\nresults\\nsft_cka_only_20\\nsft_cka_only_20_1p5b\\nsft_gradient_20\\nsft_random_20\\nsft_rasp_20_1p5b\\nsft_rasp_25\\nsft_rasp_rlvr_20\\nsft_standard_20_1p5b\\nsft_standard_25\\nwestd_diagnostic_20260518.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.68}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T10:18:52.257159+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/grpo_*/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/grpo_*/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T10:18:52.257321+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/pruned_*/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/pruned_*/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T10:18:52.257468+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"12G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/\\n96K\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123/\\n220K\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/\\n11G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25/\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T10:18:52.257596+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/sft_*/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/sft_*/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T10:18:52.257736+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/models/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/models/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T10:18:52.258088+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"12G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20/\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_1p5b/\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20/\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20/\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b/\\n11G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25/\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20/\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_1p5b/\\n11G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25/\\n15G\\t/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.95}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T10:18:52.258363+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"12G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b/\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20/\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b/\\n11G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25/\\n12G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/\\n2.8G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b/\\n11G\\t/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T10:18:52.258534+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3.4G\\t/root/autodl-tmp/recovery_aware_struct_prune/models/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.68}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T10:18:52.258679+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T10:18:52.258817+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8\\ndrwxr-xr-x  3 root root   33 May 19 11:40 .\\ndrwxr-xr-x 34 root root 4096 May 19 16:07 ..\\ndrwxr-xr-x  2 root root 4096 May 19 17:30 completions\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T10:18:52.258966+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/eval_results/ /root/autodl-tmp/recovery_aware_struct_prune/results/ /root/autodl-tmp/recovery_aware_struct_prune/logs/ /root/autodl-tmp/recovery_aware_struct_prune/artifacts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "du -sh /root/autodl-tmp/recovery_aware_struct_prune/eval_results/ /root/autodl-tmp/recovery_aware_struct_prune/results/ /root/autodl-tmp/recovery_aware_struct_prune/logs/ /root/autodl-tmp/recovery_aware_struct_prune/artifacts/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T10:18:52.259102+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "df -h /",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "df -h /",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T10:18:52.259240+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"8.0K\\t/root/autodl-tmp/recovery_aware_struct_prune/eval_results/\\n19M\\t/root/autodl-tmp/recovery_aware_struct_prune/results/\\n20M\\t/root/autodl-tmp/recovery_aware_struct_prune/logs/\\n8.0K\\t/root/autodl-tmp/recovery_aware_struct_prune/artifacts/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T10:18:52.259403+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\noverlay          30G  8.3G   22G  28% /\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T10:18:52.259618+00:00_

## 磁盘状态汇报

### 分区概况

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/root/autodl-tmp` (数据盘) | 250G | 227G | **24G** | 91% |
| `/` (根分区) | 30G | 8.3G | 22G | 28% |

**注意**: 用户提到的 `/autodl-pub` 实际有 6.6T 可用，不紧张。真正紧张的是 `/root/autodl-tmp`。

### grpo_cka_only_20_seed123 训练状态

- 当前已用空间: **96K**（刚开始，尚无 checkpoint）
- 目录内仅有 `completions/` 子目录
- 预计完成后占用 ~12G（参考同类 grpo_cka_only_20 = 12G）
- 24G 可用 > 12G 预计需求，**暂时安全但余量不大**

### 各目录大小明细

**7B 模型目录 (10-15G 级)**:

| 目录 | 大小 | 说明 |
|------|------|------|
| `pruned_unstructured_20` | **15G** | unstructured pruning，清理候选 |
| `pruned_cka_only_20` | 12G | |
| `pruned_random_20` | 12G | |
| `pruned_rasp_20` | 12G | |
| `pruned_rasp_rlvr_20` | 12G | |
| `pruned_standard_20` | 12G | |
| `pruned_rasp_25` | 11G | |
| `pruned_standard_25` | 11G | |
| `grpo_cka_only_20` | 12G | |
| `grpo_rasp_25` | 11G | |
| `sft_cka_only_20` | 12G | |
| `sft_gradient_20` | 12G | |
| `sft_random_20` | 12G | |
| `sft_rasp_rlvr_20` | 12G | |
| `sft_rasp_25` | 11G | |
| `sft_standard_25` | 11G | |

**1.5B 模型目录 (2.8G 级)**: grpo/pruned/sft × {cka_only_20, rasp_20, standard_20}_1p5b — 各 2.8G，共 9 个 = ~25G

**其他**: models 3.4G, logs 20M, results 19M

### 清理建议（不执行，仅汇报）

| 优先级 | 目录 | 大小 | 理由 |
|--------|------|------|------|
| **P0** | `pruned_unstructured_20` | 15G | unstructured pruning control 实验，如已完成 eval 且结果已记录，可安全清理 |
| P1 | `grpo_random_20` | 220K | 仅 220K，清不清都无所谓 |

**用户提到的 `grpo_unstructured_20` 目录不存在**。仅有 `pruned_unstructured_20`。

### 结论

当前 24G 可用空间可以支撑 grpo_cka_only_20_seed123 完成训练（预计 ~12G），但训练后仅剩 ~12G。如果后续还有更多实验，建议清理 `pruned_unstructured_20`（释放 15G）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_westb_disk_cleanup_20260519T101715"
}
```

</details>

---
