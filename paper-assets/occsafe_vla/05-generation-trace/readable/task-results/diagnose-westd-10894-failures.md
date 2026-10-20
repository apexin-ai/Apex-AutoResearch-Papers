# diagnose westd 10894 failures

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-10894-failures_20260521T050337_result.json`
- **Structured JSON:** [`f578c13794907f4ea100.json`](../../sessions/f5/f578c13794907f4ea100.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果汇总

### 根因：外部 SIGTERM，疑似 AutoDL 平台操作

4 个 ablation 实验在 `2026-05-21 12:52:12` UTC+8 被 SIGTERM 同时杀死（17ms 窗口内）。

**排除的原因：**
- ❌ 服务器重启 — 容器自 May 20 持续运行，SSH 正常
- ❌ OOM killer — OOM 发 SIGKILL(9) 而非 SIGTERM(15)
- ❌ 用户手动 kill — bash_history 无 kill 命令
- ❌ 磁盘满 — root 66%, 数据盘 51%

**最可能原因：** AutoDL 平台级操作（维护、计费、GPU 抢占等），对所有用户进程批量发了 SIGTERM。

---

### 各实验被 kill 时的进度和可用 checkpoint

| 实验 | GPU | 被杀时 step | 运行时长 | 可恢复 checkpoint |
|---|---|---|---|---|
| ablation_occ_detach_s0 | cuda:0 | 4006/50005 (8%) | ~1h07m | **2500_chkpt** ✓ |
| ablation_random_occ_s0 | cuda:1 | 3993/50005 (8%) | ~1h07m | **2500_chkpt** ✓ |
| ablation_occ_detach_s1 | cuda:2 | 1546/50005 (3%) | ~29m | **无** ✗ |
| ablation_random_occ_s1 | cuda:3 | 1545/50005 (3%) | ~29m | **无** ✗ |

s0 两个实验有 2500 step checkpoint（~14.4GB，文件完整），可从 2500 resume。s1 两个实验没到 2500 步，需从头训练。

---

### Vanilla 实验状态（均完成）

| 实验 | 训练 | Eval | TSR | CAR |
|---|---|---|---|---|
| vanilla_s0 | ✅ 50005 steps | ✅ 200 episodes | 0.910 | 0.775 |
| vanilla_s1 | ✅ 50005 steps | ✅ 200 episodes | 0.935 | 0.765 |
| vanilla_s2 | ✅ 50005 steps (resumed) | ✅ 200 episodes | 0.910 | 0.770 |

三个 vanilla eval 结果文件在 `/root/occsafe_vla/eval_results/` 下，数据完整。

---

### 服务器当前状态

- 4× RTX PRO 6000 Black (96GB) 全部空闲，0MB 显存占用
- 无训练进程运行
- **可以立即重启 ablation 实验**

---
