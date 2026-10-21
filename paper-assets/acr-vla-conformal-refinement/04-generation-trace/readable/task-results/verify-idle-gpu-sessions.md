# verify idle gpu sessions

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_idle-gpu-sessions_20260516T050104_result.json`
- **Structured JSON:** [`79e2392de6ee9b71c1aa.json`](../../sessions/79/79e2392de6ee9b71c1aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### bjb1-18228: `eval-perdof-object-seed44`

| 项目 | 状态 |
|------|------|
| tmux session | **存在** (创建于 12:57:06) |
| 进程 PID | 452987 (CPU 191%, 活跃) |
| GPU | CUDA:1 (GPU-bf477c88), 5645 MiB |
| 进度 | **刚启动** — 模型和环境已加载完毕，尚未开始跑 task |

日志最后输出：加载了 10 个 task，CRM checkpoint 已加载 (337,438 params)，`max_correction_norm = 0.1`。

---

### bjb1-32546: `eval-vla-mean-object-seed44`

| 项目 | 状态 |
|------|------|
| tmux session | **存在** (创建于 12:58:49) |
| 进程 PID | 212665 (CPU 238%, 活跃) |
| GPU | CUDA:1 (GPU-ade291cb), 5609 MiB |
| 进度 | **刚启动** — 模型和环境已加载完毕，尚未开始跑 task |

日志最后输出：加载了 10 个 task，mode=vla_only, baseline_mode=mean。

---

**结论**：两个 eval session 都在正常运行，刚完成初始化（启动约 2-3 分钟），即将开始执行 rollouts。尚无已完成 task。

---
