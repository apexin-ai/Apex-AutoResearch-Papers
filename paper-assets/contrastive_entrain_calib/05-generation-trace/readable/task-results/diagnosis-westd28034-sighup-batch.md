# diagnosis westd28034 sighup batch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_westd28034-sighup-batch_20260521T072404_result.json`
- **Structured JSON:** [`32284aeddd8c3920920e.json`](../../sessions/32/32284aeddd8c3920920e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实际情况与报告不符：只有 ckpt5000-v2 真正失败，其余 3 个从未失败。**

### 关键发现

| 实验 | 报告状态 | 实际状态 |
|------|----------|----------|
| ckpt5000-v2 | FAILED (129) | ❌ 已失败 → 已重试，PID 497834 在 GPU 0 运行中 |
| ckpt6000 | FAILED (129) | ✅ 正在运行（PID 498441/498446，GPU 1） |
| ckpt6500 | FAILED (129) | ✅ 正在运行（PID 498579/498584，GPU 2） |
| ckpt7000 | ALLOCATED | ✅ 正在运行（PID 498661/498666，GPU 3） |

### ckpt5000-v2 失败根因

- 子进程（PID 495837）在 eval 开始 ~20 秒后被 **SIGKILL**（bash 报 "Killed"）
- wrapper 的 HUP trap 记录了 EXIT_CODE=129
- **非 OOM**（791GB RAM，761GB 可用）
- 容器无内核日志，无法确定精确来源。最可能是外部干预或 GPU 残留进程冲突
- 已自动重试并在 GPU 0 上运行

### 建议

4 个 GPU 全部被活跃 eval 占用，**无需任何操作**，等待完成即可。监控系统可能存在误报问题，建议排查。

报告已存至 `art_20260521_89bbca`。

---
