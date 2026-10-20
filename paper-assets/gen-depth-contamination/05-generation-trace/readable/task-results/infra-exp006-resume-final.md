# infra exp006 resume final

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006-resume-final_20260515T022102_result.json`
- **Structured JSON:** [`86c35f31f85901f58b7a.json`](../../sessions/86/86c35f31f85901f58b7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告：exp-006 **没有崩溃，正在正常运行**

GPU 并非空转——进程 PID 94570 正在执行 `graduated_a0.9_s789` 的 eval，已运行约 5 分钟。

### 当前进度

| 项目 | 数值 |
|------|------|
| **已完成 eval** | **39 / 51** |
| **正在运行** | `graduated_a0.9_s789` (eval 阶段) |
| **tmux session** | `exp_006_graduated_filtering` (活跃) |

### 剩余 run (11 个，当前这个完成后)

1. `graduated_a0.9_s1024` (train + eval)
2. `surprisal_s42`, `s123`, `s456`, `s789`, `s1024` (5 runs)
3. `dsir_s42`, `s123`, `s456`, `s789`, `s1024` (5 runs)

### ETA

- 当前 eval 应在 ~5-10 分钟内完成
- 剩余 11 runs × ~25 min/run ≈ **4.5-5 小时**
- 预计完成时间：约 **15:30-16:00 (UTC)**

无需任何干预，脚本 `scripts/run_exp006.sh` 在 tmux 中正常运行，内建 skip 逻辑会自动跳过已完成的 run。

---
