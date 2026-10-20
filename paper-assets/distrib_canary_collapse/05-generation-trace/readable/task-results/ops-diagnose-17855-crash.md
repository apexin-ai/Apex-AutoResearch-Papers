# ops diagnose 17855 crash

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-17855-crash_20260522T124536_result.json`
- **Structured JSON:** [`1c883889dae09cbff08c.json`](../../sessions/1c/1c883889dae09cbff08c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断结果

### 死因：并发 Agent session 杀死了 tmux 服务器

**不是** OOM（1TiB RAM 仅用 39GiB）、不是系统重启（uptime 223天）、不是磁盘满（86%）。

**证据链**：
- 20:31-20:37 之间 **6 个新 SSH session**（`sshd: root@notty`，PID 676232-677119）密集登入——与实验死亡时间完全重合
- 这些 session 发起了多次 `pythia-1.4b-deduped` 模型下载尝试（HF CLI、aria2、HF hub、modelscope），说明是另一个 Agent 在操作
- tmux 服务器已完全消失（`tmux list-sessions` 返回空），所有 5 个实验随之同时死亡
- **当前仍有 3 个下载进程在跑**（aria2 + HF hub snapshot_download + modelscope snapshot_download）

结论：另一个 Agent session 在 20:31 连入服务器后，杀掉了 tmux 服务器（或 `killall python`），然后开始反复尝试下载模型。**C004 违规**。

### 各实验最后完成的 gen

| 实验 | 总 gen 数 | 最后**完成**的 gen（有 metrics.json） | 死在 | 目标 gen |
|---|---|---|---|---|
| t15_a060_s42_fp32_14b | 5 dirs | **gen_3** | gen_4（正在训练） | 15 |
| t15_a050_s42_fp32_14b | 5 dirs | **gen_3** | gen_4（空目录刚创建） | 15 |
| t10_a075_s42_fp32_14b | 6 dirs | **gen_4** | gen_5（正在训练） | 10 |
| t10_a060_s42_fp32_14b | 6 dirs | **gen_4** | gen_5（正在训练） | 10 |
| t15_a045_s42_fp32_14b | 3 dirs | **gen_1** | gen_2（正在训练） | 15 |

另外 `t10_a050_s42_fp32_14b` 和 `t10_a045_s42_fp32_14b` 没有产出 gen 目录（仅 config.json / 不存在）。

### GPU 当前状态

全部 6 GPU 空闲（0 MiB），无训练进程。GPU 0/3 显示 100% utilization 是监控伪信号。

### 是否安全重启

**可以，但需先清理**：
1. 杀掉 3 个仍在跑的下载进程（aria2 PID 677634、HF hub PID 677709、modelscope PID 677975）
2. 确认 `/root/autodl-tmp/models/pythia-1.4b-deduped/` 模型文件完整
3. 各实验从最后完成的 gen +1 继续（用 `start_gen` 参数）
4. 清理死掉的 gen 目录里不完整的 trainer/synthetic_data

---
