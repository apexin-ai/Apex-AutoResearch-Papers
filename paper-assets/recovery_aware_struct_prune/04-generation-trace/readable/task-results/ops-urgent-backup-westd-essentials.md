# ops urgent backup westd essentials

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_backup_westd_essentials_20260524T160353_result.json`
- **Structured JSON:** [`a686931dd02a74eba998.json`](../../sessions/a6/a686931dd02a74eba998.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部备份完成。汇报：

---

### 备份结果

| 文件 | 大小 | 状态 |
|------|------|------|
| **westd 代码** (`rasp_westd_essentials_code.tar.gz`) | 4.4M | ✓ 已传至 westb |
| **westd 数据** (`rasp_westd_essentials_data.tar.gz`) | 109M | ✓ 已传至 westb |
| **westb 代码** (`rasp_westb_essentials_code.tar.gz`) | 3.6M | ✓ 本地备份完成 |
| **westb 数据** (`rasp_westb_essentials_data.tar.gz`) | 65M | ✓ 本地备份完成 |

### westb `/root/autodl-tmp/backups/` 最终内容

```
total 251M
rasp_westb_backup.tar.gz          70M   (之前已有)
rasp_westb_essentials_code.tar.gz 3.6M  ← 新
rasp_westb_essentials_data.tar.gz 65M   ← 新
rasp_westd_backup.tar.gz          114M  (之前已有)
westd_backup/
  rasp_westd_essentials_code.tar.gz 4.4M  ← 新
  rasp_westd_essentials_data.tar.gz 109M  ← 新
```

所有关键文件已安全备份到 westb 数据盘。westd 数据盘即使回收也不会丢失实验记录。

---
