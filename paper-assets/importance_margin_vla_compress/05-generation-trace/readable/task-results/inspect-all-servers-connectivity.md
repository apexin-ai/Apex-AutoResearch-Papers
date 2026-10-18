# inspect all servers connectivity

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_inspect_all_servers_connectivity_20260526T020043_result.json`
- **Structured JSON:** [`c2f7c85be5af5d92e5df.json`](../../sessions/c2/c2f7c85be5af5d92e5df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

```
westd-38929  | ✅ 连通 | GPU0: 63% 15780MiB | GPU1: 67% 15780MiB | GPU2: 75% 15938MiB | GPU3: 66% 15938MiB
cqa1-33015   | ❌ 离线 | Unable to connect to port 33015 on 58.144.141.28
westd-27271  | ❌ 离线 | Unable to connect to port 27271 on 36.103.198.204
```

### westd-38929 详情

4 个实验全部正常运行中，PID 与预期匹配：

| GPU | 实验 | PID | CPU 时间 |
|-----|------|-----|---------|
| GPU0 | `attention_prune k=0.7 seed42` | 6815 | 3559 min |
| GPU1 | `l2norm_prune k=0.7 seed42` | 7009 | (running) |
| GPU2 | `random_prune k=0.7 seed42` | 7384 | 3721 min |
| GPU3 | `l2norm_prune k=0.85 seed42` | 8069 | 3674 min |

4 个 tmux session 均存活，均从 `02:12` 启动至今（约 7.8 小时）。

### cqa1-33015 & westd-27271

两台都是 **connection refused**（端口不通），AutoDL 实例可能已关机或重启后端口变更。需要去 AutoDL 控制台确认实例状态，如果已重启需更新 `~/.ssh/config` 中的端口。

---
