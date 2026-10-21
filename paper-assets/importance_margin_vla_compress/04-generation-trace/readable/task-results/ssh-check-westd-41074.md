# ssh check westd 41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh-check_westd-41074_20260525T172616_result.json`
- **Structured JSON:** [`a4e7155aad428f0791bd.json`](../../sessions/a4/a4e7155aad428f0791bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇报：westd-41074

| 项目 | 状态 |
|------|------|
| **连接状态** | 成功 |
| **GPU** | 4× NVIDIA RTX PRO 6000 Blackwell Server Edition，每卡 96GB 显存，全部空闲（0 MiB 占用，0% 利用率） |
| **实验进程** | 无残留实验进程（仅系统服务：sshd、supervisord、tensorboard、jupyter-lab、autopanel） |
| **项目目录** | `/root/autodl-tmp/importance_margin_vla_compress/` 存在，大小 67GB |
| **磁盘空间** | 根分区：30GB 用 5.0GB，剩余 26GB (17%)；**数据盘：250GB 用 249GB，剩余 1.9GB (100%)**  |

**关键警告**：数据盘 `/root/autodl-tmp/` 几乎满了（仅剩 1.9GB），需要清理空间后才能跑新实验。

---
