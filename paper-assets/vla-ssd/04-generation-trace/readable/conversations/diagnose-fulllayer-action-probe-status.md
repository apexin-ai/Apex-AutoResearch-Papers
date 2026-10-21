# diagnose fulllayer action probe status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_diagnose_fulllayer_action_probe_status_20260516T044354.jsonl`
- **Structured JSON:** [`2434766a31292459d4d0.json`](../../sessions/24/2434766a31292459d4d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-16T04:44:25.204222+00:00_

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
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
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

_source line 2 · 2026-05-16T04:44:25.204622+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T04:44:25.204813+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ps -p 700649 -o pid,stat,etime,cmd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ps -p 700649 -o pid,stat,etime,cmd"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T04:44:25.204989+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tmux list-sessions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tmux list-sessions"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T04:44:25.205157+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T04:44:25.205289+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T04:44:25.205555+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -50 /root/runs/vla-ssd/fulllayer_action_probe.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -50 /root/runs/vla-ssd/fulllayer_action_probe.log"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T04:44:25.205708+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T04:44:25.206070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  trained/image_mean/L31: mean_R2=0.3803 (14.8s, ep=32)\\n  trained/image_mean/L32: mean_R2=0.5390 (13.4s, ep=17)\\n  trained/last_preaction/L0: mean_R2=-0.3314 (14.9s, ep=10)\\n  trained/last_preaction/L1: mean_R2=0.4403 (18.9s, ep=50)\\n  trained/last_preaction/L2: mean_R2=0.5534 (19.2s, ep=50)\\n  trained/last_preaction/L3: mean_R2=0.5211 (19.2s, ep=50)\\n  trained/last_preaction/L4: mean_R2=0.5604 (19.0s, ep=50)\\n  trained/last_preaction/L5: mean_R2=0.5553 (21.3s, ep=48)\\n  trained/last_preaction/L6: mean_R2=0.5705 (20.5s, ep=42)\\n  trained/last_preaction/L7: mean_R2=0.5788 (18.8s, ep=25)\\n  trained/last_preaction/L8: mean_R2=0.6184 (18.6s, ep=29)\\n  trained/last_preaction/L9: mean_R2=0.6305 (18.3s, ep=24)\\n  trained/last_preaction/L10: mean_R2=0.6590 (18.1s, ep=24)\\n  trained/last_preaction/L11: mean_R2=0.6579 (18.2s, ep=24)\\n  trained/last_preaction/L12: mean_R2=0.6663 (17.2s, ep=15)\\n  trained/last_preaction/L13: mean_R2=0.6779 (17.3s, ep=15)\\n  trained/last_preaction/L14: mean_R2=0.6760 (17.3s, ep=15)\\n  trained/last_preaction/L15: mean_R2=0.6553 (16.6s, ep=9)\\n  trained/last_preaction/L16: mean_R2=0.6581 (16.8s, ep=9)\\n  trained/last_preaction/L17: mean_R2=0.6663 (16.6s, ep=9)\\n  trained/last_preaction/L18: mean_R2=0.6675 (16.8s, ep=9)\\n  trained/last_preaction/L19: mean_R2=0.6711 (16.5s, ep=9)\\n  trained/last_preaction/L20: mean_R2=0.6672 (16.6s, ep=9)\\n  trained/last_preaction/L21: mean_R2=0.6621 (17.1s, ep=9)\\n  trained/last_preaction/L22: mean_R2=0.6711 (16.9s, ep=9)\\n  trained/last_preaction/L23: mean_R2=0.6688 (16.5s, ep=9)\\n  trained/last_preaction/L24: mean_R2=0.6694 (16.6s, ep=9)\\n  trained/last_preaction/L25: mean_R2=0.6736 (16.6s, ep=9)\\n  trained/last_preaction/L26: mean_R2=0.6744 (16.8s, ep=9)\\n  trained/last_preaction/L27: mean_R2=0.6743 (16.9s, ep=9)\\n  trained/last_preaction/L28: mean_R2=0.6471 (16.6s, ep=7)\\n  trained/last_preaction/L29: mean_R2=0.6347 (16.6s, 
…[truncated 1251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T04:44:25.206282+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T04:44:25.206416+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T04:44:25.206540+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/action_probe/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/action_probe/"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T04:44:25.206664+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 0 %\\n1, 0 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T04:44:25.206781+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/vla-ssd/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/vla-ssd/results/"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T04:44:25.206911+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/vla-ssd/results/action_probe/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T04:44:25.207081+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x 5 root root   97 May 15 23:24 .\\ndrwxr-xr-x 7 root root 4096 May 16 11:41 ..\\ndrwxr-xr-x 3 root root   39 May 15 22:35 trained_dryrun\\ndrwxr-xr-x 3 root root   39 May 15 22:37 trained_dryrun_pca1024\\ndrwxr-xr-x 4 root root   63 May 15 23:29 trained_pca1024\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T04:44:25.207228+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T04:44:25.207353+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 120236 May 16 12:10 /root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T04:44:25.207512+00:00_

**结论：DONE** — 进程已正常完成。

| 项目 | 状态 |
|------|------|
| PID 700649 | 已退出（不在进程表中） |
| 退出码 | `EXIT_CODE=0`（成功） |
| 运行时长 | 19.5 分钟 |
| GPU | 两块 GPU 均已释放（0 MiB / 0% 利用率） |
| 结果文件 | `/root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json`（120KB，写入时间 12:10） |

### 实验结果摘要

**Trained model probing（33层，L0-L32）：**
- `image_mean` peak: **L8, R²=0.6553**
- `last_preaction` peak: **L13, R²=0.6779**

**Untrained model probing：**
- `image_mean` peak: **L0, R²=0.6403**
- `last_preaction` peak: **L32, R²=0.6093**

**Bootstrap 对比（全部显著）：**
- trained(L8) vs untrained(L0) image_mean: delta=+0.0149, p=0.006
- trained(L13) vs untrained(L32) last_preaction: delta=+0.0686, p<0.0001
- same-layer(L8) image_mean trained vs untrained: delta=+0.1229, p<0.0001
- same-layer(L13) last_preaction trained vs untrained: delta=+1.0071, p<0.0001

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diagnose_fulllayer_action_probe_status_20260516T044354"
}
```

</details>

---
