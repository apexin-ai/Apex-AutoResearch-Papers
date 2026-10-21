# infra kill structfuse v2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill_structfuse_v2_20260516T200116_result.json`
- **Structured JSON:** [`d74378abb2e37cb3d4ca.json`](../../sessions/d7/d74378abb2e37cb3d4ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

## Step 4: GPU 状态

```
# 无计算进程
---
0, 0 MiB, 97253 MiB
1, 0 MiB, 97253 MiB
```

**两块 GPU 完全释放，各 97GB 显存可用，structfuse 已清除干净。**

## Step 5: 下载状态

```
QwQ RUNNING
R1-32B RUNNING
---
(download_full.log 为空或不存在)
---
Filesystem      Size  Used Avail Use% Mounted on
/dev/md0        250G   73G  178G  29% /root/autodl-tmp
```

**两个下载进程均在运行中。数据盘已用 73G / 250G (29%)，剩余 178G 空间充足。**

---
