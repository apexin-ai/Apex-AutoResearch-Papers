# ops westd crash forensics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-crash-forensics_20260519T060725_result.json`
- **Structured JSON:** [`9c4bcd2abf63b8074ca8.json`](../../sessions/9c/9c4bcd2abf63b8074ca8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有诊断数据已收集完毕。

---

## 诊断结果

### 每条诊断命令输出摘要

| 命令 | 结果 |
|------|------|
| `uptime` | 1 day 20h — 容器未重启 |
| `tmux ls` | "no server running on /tmp/tmux-0/default" — tmux server 已死，但 socket 文件残留（创建于 13:05） |
| `nvidia-smi` | 4×RTX PRO 6000 全空闲，0MiB，无 GPU 进程 |
| `last reboot` | wtmp begins Feb 3 — 无近期重启记录 |
| `dmesg` | Operation not permitted（容器内无权限） |
| `/var/log/syslog` | 不存在 |
| `journalctl -k` | No entries |
| `crontab -l` | 无定时任务 |
| `df -h /` | **overlay 30G，已用 27G (88%)，仅剩 3.8G**。`/tmp` 在此分区上 |
| `df -h /dev/sda2` | 879G 仅用 21G（挂载于 nvidia-smi 路径，autodl-tmp 在此） |
| `ps aux` | 仅 scienceworld_sft_gen.py + 系统服务存活，无训练/eval 进程 |

### 各日志死因

| 日志 | 最后写入 | 死因 |
|------|---------|------|
| `exp029_seed2_ood_v3.log` | 5/19 13:09 | **`OSError: [Errno 28] No space left on device`** — `/tmp` 满，AlfWorld 无法复制 libdownward.so |
| `exp029_seed2_ood_reeval.log` | 5/19 ~10:46 | **Raylet 意外终止** → `ActorUnavailableError: Socket closed`。Raylet 日志提示可能 SIGKILL/SIGSEGV |
| `exp029_seed2_ood_reeval_1gpu.log` | 5/19 | **`FileNotFoundError`** — checkpoint 以 world_size=2 保存，1gpu eval 找 world_size=1 格式文件 |
| `exp029_seed2_ood_reeval_2gpu.log` | 5/19 | **`RuntimeError: Expected all tensors on same device, found cuda:0 and cpu`** — optimizer step 中 tensor 设备不一致 |
| `exp029_seed2_westd_resume.log` | 5/19 10:31 | **SIGTERM** 连续轰炸 Ray 进程 → core dump（`timeout: the monitored command dumped core`） |
| `zeroshot_eval.log` | 5/19 | eval 完成输出了 metrics，但 W&B teardown `BrokenPipeError`（连接断裂） |

### 根因判断：**D（磁盘空间耗尽触发连锁崩溃）**

**不是 A（容器重启）、不是 B（SSH 断开）、不是 C（OOM）、不是 E（定时清理）。**

**因果链：**

1. 根分区 overlay 仅 30G，基线占用已达 27G（miniconda3 14G + provenance_weight_training 13G），仅剩 ~3G
2. 多个实验同时运行时，Ray temp files + Python temp files + W&B logs + core dumps 迅速吃掉剩余空间 → **根分区 100% 满**
3. `/tmp` 写满后的连锁效应：
   - AlfWorld 环境创建失败 → OOD eval 直接 ENOSPC 崩溃
   - Ray raylet 无法写 temp 文件 → raylet 异常终止 → 所有 Ray actor 丢失
   - tmux socket (`/tmp/tmux-0/default`) 损坏 → tmux server 死亡 → 所有 session 消失 → 所有子进程收 SIGHUP/SIGTERM
4. 进程全部死亡后释放 temp 文件，磁盘回到 88%（现在看到的状态）

**次要原因（个别 eval 的代码/配置错误）：**
- `ood_reeval_1gpu`: checkpoint world_size 不匹配（配置错误）
- `ood_reeval_2gpu`: CUDA/CPU tensor 混合（可能由磁盘满导致加载不完整引发）

### tmux+nohup 双保险是否可行？

**不能解决此问题。** 根因不是 SSH 断开，而是磁盘满。tmux 本身就是受害者（socket 在 /tmp 上）。即使用 nohup，进程也会因 ENOSPC 崩溃。

**真正的修复方案：**
1. **清理根分区**：`/root/provenance_weight_training`（13G）是否还需要？删除后可腾出 13G
2. **重定向 temp 目录**：设置 `TMPDIR=/root/autodl-tmp/tmp` 和 `RAY_TMPDIR=/root/autodl-tmp/ray_tmp`，把临时文件写到 879G 的数据盘
3. **tmux socket 也要迁移**：`export TMUX_TMPDIR=/root/autodl-tmp/tmux`，避免 tmux socket 受根分区影响

---
