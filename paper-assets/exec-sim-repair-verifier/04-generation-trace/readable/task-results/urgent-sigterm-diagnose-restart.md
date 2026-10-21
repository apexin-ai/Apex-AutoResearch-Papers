# urgent sigterm diagnose restart

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_sigterm-diagnose-restart_20260514T141913_result.json`
- **Structured JSON:** [`79f8e3e98375f0256dd9.json`](../../sessions/79/79f8e3e98375f0256dd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都已成功重启：

**GPU 状态（4x5090 全部在用）：**
| GPU | 任务 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | CWM eval | 12990 MiB | 88% |
| 1 | CLS eval | 12990 MiB | 88% |
| 2 | **CWM 8B 训练** (PID 243700) | 26998 MiB | 98% |
| 3 | **CLS 8B s123 训练** (PID 243778) | 26740 MiB | 97% |

**训练进度：**
- **CWM 8B**: 从 checkpoint-1200 resume，0/6633 步（刚开始跳过已训练数据）
- **CLS 8B s123**: 从 checkpoint-2400 resume，已到 step 2408/6633，正常训练中

**诊断结论：** 容器环境无内核日志权限，无 OOM/配额证据，判断为一次性系统事件。

**所做修改：**
- `train_repo_cwm.py` 新增 `--save_total_limit` CLI 参数（原来硬编码为 5）
- 两个训练均设 `--save_total_limit 20`
- 清理了 22:17 的重复旧进程（`train_cwm_8b` / `train_cls_8b_s123` tmux 会话）

---
