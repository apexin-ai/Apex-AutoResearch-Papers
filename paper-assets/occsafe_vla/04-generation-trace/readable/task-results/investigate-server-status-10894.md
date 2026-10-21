# investigate server status 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_server_status_10894_20260526T234544_result.json`
- **Structured JSON:** [`b134e9fb03a0f71b1a7a.json`](../../sessions/b1/b134e9fb03a0f71b1a7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 train.log 只记录了前 ~275 步就停止写入了，但 10k checkpoint 已保存、GPU 利用率 99%，表明训练正常进行。以下是汇总报告。

---

## westd-10894 GPU 进程状态报告

### GPU 总览

| GPU | PID | 实验 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| 0 | 428963 | reverse_cutoff_s2_v2_eval (评估) | 16,759 MiB | 99% |
| 0 | 433768 | **detach_ln_v2_s1** (训练) | 63,004 MiB | 99% |
| 1 | 390852 | **full_occ_ln_v2_s0** (训练) | 62,194 MiB | 99% |
| 2 | 391060 | **full_occ_ln_v2_s1** (训练) | 63,004 MiB | 99% |
| 3 | 391402 | **detach_ln_v2_s0** (训练) | 62,194 MiB | 45% |

磁盘：`/root/autodl-tmp` 250G 用了 171G，剩余 80G，充裕。

---

### 各实验详情

**1. full_occ_ln_v2_s0** (PID 390852, GPU 1)
- 状态：**正常训练中**
- 首次启动 ~02:08 因 `--resume_from_checkpoint` 参数不被识别而崩溃（exitcode=2）
- 随后被 cron 重启（不含该参数），从 pretrained 权重从头训练，~02:15 开始
- 已运行 5h21m，10k checkpoint 已于 05:12 保存
- 预估当前 step: ~19,000-20,000（基于 ~1.08 it/s）
- 预计完成：~15:10 UTC May 27

**2. full_occ_ln_v2_s1** (PID 391060, GPU 2)
- 状态：**正常训练中**
- 同上，首次启动崩溃后被重启，~02:15 开始
- 10k checkpoint 已于 05:13 保存
- 预计完成：~15:10 UTC May 27

**3. detach_ln_v2_s0** (PID 391402, GPU 3)
- 状态：**正常训练中**
- 同上，首次启动崩溃后被重启，~02:15 开始
- 10k checkpoint 已于 05:12 保存
- GPU 利用率偶尔较低 (45%)，但正在训练
- 预计完成：~15:10 UTC May 27

**4. detach_ln_v2_s1** (PID 433768, GPU 0)
- 状态：**正常训练中**，刚启动约 20 分钟
- Registry 中 PID 681124 已死，433768 是重新启动的新进程
- 当前 step: ~750/50005
- 预计完成：~20:10 UTC May 27

**5. reverse_cutoff_s2_v2** (PID 428963, GPU 0)
- 状态：**训练已完成** (50005 步, EXIT_CODE=0)，checkpoint 已保存
- 当前正在执行评估 (evaluate_safelibero.py)，运行约 22 分钟

---

### Registry 矛盾解释

- `full_occ_ln_v2_s0/s1` registry 显示 conclusion=failed：**首次启动确实失败了**（`--resume_from_checkpoint` 参数错误），但 cron 已自动重启，实际在正常训练。Registry 的 PID (390852/391060) 指向的是重启后的进程。
- `detach_ln_v2_s1` registry PID=681124：该进程已死，实际训练进程是新启动的 PID 433768。

### 失败原因

三个实验首次启动都因同一原因失败：`finetune.py` 不认识 `--resume_from_checkpoint` 参数。这是启动脚本的 bug——该参数不在 finetune.py 的 argparse 中。重启时去掉了该参数，训练正常进行。

### 时间线风险

所有实验预计在 May 27 15:10-20:10 UTC 完成训练。DDL 是 May 28 12:00 UTC。评估还需额外时间。**detach_ln_v2_s1 完成最晚（~20:10 UTC May 27），加上评估时间仍在 DDL 内，但余量不大。**

---
