# ops disk cleanup 10894 r2 exec

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-10894-r2-exec_20260521T191154_result.json`
- **Structured JSON:** [`ca3f98f441188f010c7a.json`](../../sessions/ca/ca3f98f441188f010c7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 产出报告

### 1. 轮询记录
| 轮次 | 等待时间(累计) | 结果 |
|------|------------|------|
| #1-#17 | 0-34 min | 全部 NOT YET |
| #18 | ~36 min | random_occ_s0 保存完成 (22 files) |
| #19-#20 | ~38-40 min | 1/4 完成 |
| #21 | ~42 min | +occ_detach_s1 保存中 (13 files) |
| #22 | ~44 min | 全部 4 个出现，occ_detach_s0 仍在写入 (17 files) |
| #23 | ~46 min | 全部完整 (各 22 files) |

### 2. 30K 保存确认时间
轮询 #23（约 46 分钟后），全部 4 个 30000_chkpt 保存完整。

### 3. 删除时各 ablation 的 step
| 实验 | 删除时 step |
|------|-----------|
| occ_detach_s0 | 30083 |
| random_occ_s0 | 30423 |
| occ_detach_s1 | 30119 |
| random_occ_s1 | 30106 |

### 4. 释放空间
4 × 15GB = **60GB** 释放

### 5. 最终 df -h
```
/dev/md0   250G   97G  154G  39%  /root/autodl-tmp
```

---
