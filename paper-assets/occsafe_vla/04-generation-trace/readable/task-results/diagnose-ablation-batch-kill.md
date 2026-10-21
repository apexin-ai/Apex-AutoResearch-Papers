# diagnose ablation batch kill

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ablation_batch_kill_20260521T045340_result.json`
- **Structured JSON:** [`c3ba2a5f2b86003a1d12.json`](../../sessions/c3/c3ba2a5f2b86003a1d12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已充分。以下是诊断报告。

---

## 诊断报告：westd-10894 Ablation 实验批量 SIGTERM

### 1. 杀死原因

**结论：外部批量 `kill` 命令（非 OOM、非重启、非 cron）**

证据：
- 4 个进程在 **完全相同的秒**（`12:52:12`）收到 SIGTERM，时间精确到毫秒级（.120/.125/.131/.137/.138）
- **无重启**：uptime 156 天，无 reboot 记录
- **无 OOM**：dmesg 被容器限制无法读取，但进程是收到 SIGTERM(15) 而非 SIGKILL(9)，排除 OOM Killer
- **无 crontab**，bash_history 中无 kill 命令
- **无 syslog/auth.log** 记录
- ablation 实验没有 tmux session（vanilla 的 3 个 tmux session 仍存在），说明是通过 ssh_execute 后台启动的

**最可能的场景**：通过 agent 系统的 `ssh_execute` 发出了 `pkill -f torchrun` 或类似命令。这类命令不会写入 bash_history。

### 2. 每个实验最后 step

| 实验 | GPU | 启动 | 最后 step | 进度 | 运行时长 |
|------|-----|------|-----------|------|----------|
| ablation_occ_detach_s0 | cuda:0 | 11:44 | **4006**/50005 | 8.0% | ~1h08m |
| ablation_random_occ_s0 | cuda:1 | 11:44 | **3993**/50005 | 8.0% | ~1h08m |
| ablation_occ_detach_s1 | cuda:2 | 12:22 | **1546**/50005 | 3.1% | ~30m |
| ablation_random_occ_s1 | cuda:3 | 12:22 | **1545**/50005 | 3.1% | ~30m |

**Loss 值不可用**：WANDB_MODE=disabled 且 tqdm 没有打印 loss。

### 3. Checkpoint 状况

| 实验 | Checkpoint | 大小 |
|------|------------|------|
| ablation_occ_detach_s0 | **step 2500** ✅ 完整 | ~14GB（含 merged model + action_head/occ_head/proprio_projector） |
| ablation_random_occ_s0 | **step 2500** ✅ 完整 | ~14GB |
| ablation_occ_detach_s1 | **无** ❌（被杀时仅到 step 1546） | - |
| ablation_random_occ_s1 | **无** ❌（被杀时仅到 step 1545） | - |

### 4. GPU 当前可用性

4× NVIDIA RTX PRO 6000 Blackwell（98GB each）：
- **全部空闲**：0MiB 显存占用，无运行进程
- GPU 0-2 显示 100% util 是残留状态，实际无负载
- **可立即使用**

磁盘：根分区 66%（11GB 可用），数据盘 51%（416GB 可用）— 充足。

### 5. 建议

- **可立即重启全部 4 个实验**
- **s0 实验**（occ_detach_s0 / random_occ_s0）：从 **step 2500 checkpoint resume**，节省 ~40 分钟
- **s1 实验**（occ_detach_s1 / random_occ_s1）：**从头开始**
- 建议用 **tmux** 或 **nohup** 启动并将日志重定向到文件，避免被 SSH 断连影响
- 注意：之前 vanilla_s2 在 step 25000 因根分区磁盘满而失败（"No space left on device"），确保 checkpoint 存到数据盘 `/root/autodl-tmp/`

---
