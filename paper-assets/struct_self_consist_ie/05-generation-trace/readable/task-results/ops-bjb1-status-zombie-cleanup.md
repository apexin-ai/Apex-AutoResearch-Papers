# ops bjb1 status zombie cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_status_zombie_cleanup_20260514T142422_result.json`
- **Structured JSON:** [`849cdb9b9660ac3256e2.json`](../../sessions/84/849cdb9b9660ac3256e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-21071 服务器状态报告

### GPU 状态
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0-3 | RTX 5090 | 2/32607 MiB | 0% |

**4 张卡全部空闲，无 GPU 进程。**

### 磁盘
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 11G | 20G | 37% |
| /root/autodl-tmp | 250G | 138G | 113G | 55% |

### 进程检查
- **Python 进程**：仅 AutoDL 平台服务（TensorBoard port 6007 + Jupyter Lab），非训练进程，保留不动
- **tmux 会话**：无
- **GPU 占用进程**：无
- **僵尸进程 (Z state)**：无

### 项目代码状态
- 目录 `/root/autodl-tmp/struct_self_consist_ie/` 存在，code/data/checkpoints/output/ 均完整
- **非 git 仓库**（`git log` 返回 NO_GIT）——代码是直接拷贝过来的，不是 git clone
- checkpoints 下有 6 个模型（qwen3-8b 系列 + llama3.1-8b），output 下有大量实验结果

### 结论
- **无僵尸进程需要清理**
- **GPU 全部空闲，磁盘充足（数据盘 113G 可用）**
- **服务器就绪，可接受新实验**
- 唯一注意点：项目代码未用 git 管理，同步代码需要手动 rsync 或重新 clone

---
