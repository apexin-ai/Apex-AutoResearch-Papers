# investigate bjb1 gpu audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_bjb1-gpu-audit_20260514T221229_result.json`
- **Structured JSON:** [`387123d6010586a8854f.json`](../../sessions/38/387123d6010586a8854f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是审计报告：

---

## bjb1-18228 GPU 审计报告

### 架构说明
所有 4 个 eval 进程**共享 GPU 0** 加载 SmolVLA 模型（Type G），各自在独立 GPU 上做 compute（Type C）。PID 252489 是唯一例外——它的 compute 也在 GPU 0 上。

### GPU 0 — 14764 MiB / 24564 MiB (60%) — 4 进程共享

| PID | 显存 | Type | 实验 |
|-----|------|------|------|
| 231426 | 2655 MiB | G | eval-argmin-only-spatial |
| 232820 | 2655 MiB | G | eval-tiny-correction-spatial |
| 252489 | 5692 MiB | **C+G** | eval-acr-spatial-v4-default |
| 253085 | 3714 MiB | G | eval-acr-spatial-v4-small |

### GPU 1 — 1423 MiB / 24564 MiB (6%)
- **PID 231426** — eval-argmin-only-spatial
- Mode: `reconvla` (无 CRM)
- **进度: 4/10 tasks** — 运行 4h25m
- 已完成结果: task1=60%, task2=100%, task3=0%, task4=30%

### GPU 2 — 1459 MiB / 24564 MiB (6%)
- **PID 232820** — eval-tiny-correction-spatial
- Mode: `acr_vla`, CRM v2, `max_correction_norm=0.05`
- **进度: 4/10 tasks** — 运行 4h24m
- 已完成结果: task1=70%, task2=90%, task3=0%, task4=30%

### GPU 3 — 1459 MiB / 24564 MiB (6%)
- **PID 253085** — eval-acr-spatial-v4-small
- Mode: `acr_vla`, CRM v3_norm, `max_correction_norm=0.1`
- **进度: 2/10 tasks** — 运行 1h42m
- 已完成结果: task1=60%, task2=100%

### 重要修正

1. **cuda:3 不是不明进程**——是 eval-acr-spatial-v4-small (PID 253085) 的 compute 进程
2. **eval-acr-spatial-v4-default 未 failed**——PID 252489 正在运行，已完成 1/10 tasks (task1=0%)。它的 stdout 走 pipe 到 tmux pane 而非 log 文件，可能是之前检测不到的原因
3. **没有 stale 进程**——所有 4 个 PID 都活跃且在推进

### Tmux Sessions
- `eval-acr-spatial-v4-default` — PID 252489 ✅ RUNNING
- `eval-argmin-only-spatial` — PID 231426 ✅ RUNNING
- `eval-tiny-correction-spatial` — PID 232820 ✅ RUNNING
- ⚠️ eval-acr-spatial-v4-small (PID 253085) **没有对应 tmux session**，日志写到 `/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log`

---
