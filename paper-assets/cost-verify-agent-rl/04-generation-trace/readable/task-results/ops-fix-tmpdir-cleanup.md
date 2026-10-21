# ops fix tmpdir cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-tmpdir-cleanup_20260514T050848_result.json`
- **Structured JSON:** [`5445289455fc18d03d2a.json`](../../sessions/54/5445289455fc18d03d2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有步骤完成。汇总：

| 项目 | 状态 |
|------|------|
| /tmp 清理 | 已完成，`/tmp/tmp*` 和 `/tmp/ray` 已删除 |
| 根分区 `/` | 30G 总量，7.3G 已用 (25%)，23G 可用 |
| 数据盘 `/root/autodl-tmp/` | 250G 总量，92G 已用 (37%)，159G 可用 |
| `TMPDIR` 环境变量 | 已添加 `export TMPDIR=/root/autodl-tmp/tmp/` 到 `.bashrc` |
| exp010 train.py 进程 | 已退出，无残留 |
| tmux sessions | 无活跃 session |

**根因修复**：`TMPDIR=/root/autodl-tmp/tmp/` 会让 ALFWorld fast_downward 的 `libdownward.so` 临时文件写到数据盘（250G）而非根分区（30G），下次训练不会再因 /tmp 满崩溃。

---
