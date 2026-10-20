# diagnose westd 34685 failures

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-34685-failures_20260521T050321_result.json`
- **Structured JSON:** [`55fcc4a9b89b335366d0.json`](../../sessions/55/55fcc4a9b89b335366d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在信息足够了。汇总诊断结果：

---

## 诊断报告

### 根因：两种失败模式叠加

**1. 磁盘 I/O 错误（主因）**
`occ_s1_restart.log` 明确记录了 `RuntimeError: basic_ios::clear: iostream error` — 在 `torch.save()` 保存 checkpoint 时发生磁盘写入错误（`inline_container.cc:672: unexpected pos 148992 vs 148880`）。这是之前磁盘满事件的后遗症/重现。保存 checkpoint 时磁盘空间不足或文件系统异常导致进程崩溃。

**2. SIGTERM 外部杀进程（衍生）**
所有 3 个实验都收到了 `Signals.SIGTERM` (signal 15)，不是内部崩溃。这是监控/自动化系统检测到进程异常后发送的 kill 信号，用于重启。

**3 个实验是同一根因**：磁盘 I/O 问题导致进程死亡 → 监控系统检测到 → 发 SIGTERM 重启。

### 各实验最后训练到的 step

| 实验 | 崩溃前最后 step（本轮 local） | 失败时间 | 失败方式 |
|------|------|------|------|
| occ_s0 | 无日志可查（mvp_occ_s0.log 不存在） | ~05:00 UTC | process dead 5× |
| occ_s1 | step 5894 (mvp_occ_s1.log) → 后来 restart 到 step 12500 再崩 → resume2 到 step 307 再被杀 | 09:15 / 12:35 / 13:03 UTC | SIGTERM → I/O error → SIGTERM |
| occ_s2 | 无日志可查（mvp_occ_s2.log 不存在） | ~05:00 UTC | process dead 5× |

### 最新可用 checkpoint

| 实验 | 最新 checkpoint | checkpoint step |
|------|------|------|
| occ_s0 | `42500_chkpt` | 42500 |
| occ_s1 | `17500_chkpt` | 17500 |
| occ_s2 | `42500_chkpt` | 42500 |

**无任何新 checkpoint 产生** — 崩溃后所有重启都未训练到下一个 save 点。

### 当前状态

3 个实验已被自动重启且正在运行（GPU 0/1/2 util 68-99%）：

| 实验 | 日志 | 当前 local step | Resume from | PID |
|------|------|------|------|------|
| occ_s0 | occ_s0_resume2.log | ~454 | 42500_chkpt | 76998 |
| occ_s1 | occ_s1_resume3.log | 刚启动（加载中） | 17500_chkpt | 80898 |
| occ_s2 | occ_s2_resume2.log | ~413 | 42500_chkpt | 78171 |

磁盘当前正常：root 40%（12G/30G），数据盘 2%（15G/879G）。

### 风险提示

**step 计数器每次重启从 0 开始**，意味着之前所有 checkpoint 之间的训练 step 全部浪费。occ_s1 尤其严重 — 从 7500 训到 ~20000 的过程中，17500 checkpoint 保存成功，但 20000 checkpoint 写入失败，然后又反复从 17500 重启了 3 次。

**occ_s1 持续被 SIGTERM**：resume2 在仅训练 307 步后就被杀掉（13:03 UTC），然后立即启动了 resume3。需要确认什么在发 SIGTERM — 可能是自动化系统检测到某种异常触发了重启循环。

### 是否可以 resume

可以，且已在 resume 中：
- **occ_s0**: 从 `42500_chkpt` resume ✓（已在运行）
- **occ_s1**: 从 `17500_chkpt` resume ✓（已在运行，但注意反复被杀的问题）
- **occ_s2**: 从 `42500_chkpt` resume ✓（已在运行）

---
