# fix bashrc old path and resubmit

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bashrc_old_path_and_resubmit_20260513T164137_result.json`
- **Structured JSON:** [`64a54d0c0eee33ee129c.json`](../../sessions/64/64a54d0c0eee33ee129c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 排查结果

**服务器上未找到旧路径引用** — `.bashrc`、`.profile`、`/etc/profile`、`/etc/bash.bashrc`、`.conda/`、`miniconda3/etc/profile.d/`、所有 `.sh` 脚本均已是新路径 `/root/div_cal_verify`。

**根因**：`cd /root/phase-gated-compound-sparse` 来自 `submit_training_job` 工具，它从 `config/projects/div_cal_verify.yaml` 的 `execution.project_path` 读取工作目录。该配置此前已被修复为 `/root/div_cal_verify`（line 9），所以问题发生在配置修改之前的 job 提交。

### 修改内容

| 位置 | 操作 |
|------|------|
| 服务器 `/root/div_cal_verify/__pycache__/*.pyc` | 清理（含旧路径的编译缓存） |
| 本地 `config/crons.yaml` 行 10/24/38/52 | `phase-gated-compound-sparse` → `div_cal_verify`（4 处 log_path） |

### tmux session 清理

tmux 服务器无活跃 session（`no server running`）— 两个失败的 session 已自行退出，无需手动清理。

### 验证

- 服务器 shell 配置：CLEAN（无旧路径残留）
- pyc 缓存：已清空
- crons.yaml：已更新
- 项目配置 `project_path`：已是 `/root/div_cal_verify`，后续 `submit_training_job` 不会再产生旧路径 `cd` 命令

---
